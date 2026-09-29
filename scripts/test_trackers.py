#!/usr/bin/env python3
"""
Tracker 活性自动测试 + 测速排序脚本（v3.0 优化版）。

对合并列表中的每个 Tracker 执行:
  1. 安全过滤（排除内网/localhost/非标准地址，DNS 解析缓存）
  2. 协议级探活 + 响应速度测量
     - http/https : 发送标准 BitTorrent announce 请求，验证 bencoded 响应
     - udp        : 完整 UDP tracker connect 握手（带重试），记录耗时
     - wss/ws     : TCP + TLS 连通性检查
  3. 第二轮精测：对第一轮存活的前 100 个再次测速，取较优值
  4. 历史加权：读取上一次 alive 列表，连续存活的 tracker 获得稳定性加分
  5. 综合评分排序：速度(70%) + 历史稳定性(30%)
  6. 取前 MAX_TRACKERS 个写入 alive.txt

输出:
  - trackers/trackers_alive.txt   通过测试且综合评分最高的前 N 个
  - trackers/trackers_dead.txt    失效 / 被淘汰的 Tracker
  - trackers/test_report.md       人类可读测试报告
  - trackers/test_state.json      测试状态持久化（供下次加权）

用法:
  python scripts/test_trackers.py
  python scripts/test_trackers.py --timeout 10 --workers 30
"""

import os
import sys
import ssl
import json
import time
import random
import socket
import struct
import argparse
import ipaddress
import urllib.parse
import urllib.request
import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
import update_trackers as ut


# ============================================================
# DNS 缓存（避免同一域名重复解析）
# ============================================================
_dns_cache = {}
_dns_lock = None  # 线程安全由 GIL 保证简单操作


def cached_getaddrinfo(host, port=None):
    """带缓存的 DNS 解析。"""
    key = (host, port)
    if key in _dns_cache:
        return _dns_cache[key]
    try:
        result = socket.getaddrinfo(host, port)
        _dns_cache[key] = result
        return result
    except socket.gaierror as e:
        _dns_cache[key] = e
        raise


# ============================================================
# bencode 解码器
# ============================================================
def bdecode(data):
    def parse(index):
        c = data[index:index + 1]
        if c == b'i':
            end = data.index(b'e', index)
            return int(data[index + 1:end]), end + 1
        if c == b'l':
            result = []
            index += 1
            while data[index:index + 1] != b'e':
                item, index = parse(index)
                result.append(item)
            return result, index + 1
        if c == b'd':
            result = {}
            index += 1
            while data[index:index + 1] != b'e':
                key, index = parse(index)
                value, index = parse(index)
                result[key] = value
            return result, index + 1
        colon = data.index(b':', index)
        length = int(data[index:colon])
        start = colon + 1
        return data[start:start + length], start + length
    obj, _ = parse(0)
    return obj


def make_identity():
    info_hash = os.urandom(20)
    peer_id = b'-TT0300-' + os.urandom(12)
    return info_hash, peer_id


def encode_bytes(b):
    return ''.join('%%%02X' % x for x in b)


# ============================================================
# 安全过滤
# ============================================================
def is_safe_tracker(tracker_url):
    try:
        parsed = urllib.parse.urlparse(tracker_url)
    except Exception:
        return False, "unparseable URL"

    host = parsed.hostname
    if not host:
        return False, "no hostname"

    host_lower = host.lower()
    if host_lower in ('localhost', 'localhost.localdomain') or host_lower.endswith('.local'):
        return False, "localhost address"

    # 直接是 IP
    try:
        ip = ipaddress.ip_address(host)
        if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved or ip.is_multicast:
            return False, f"private/reserved IP: {host}"
        return True, "safe"
    except ValueError:
        pass

    # 域名：DNS 解析后检查
    try:
        infos = cached_getaddrinfo(host, None)
        for family, _, _, _, sockaddr in infos:
            ip_str = sockaddr[0]
            try:
                ip = ipaddress.ip_address(ip_str)
                if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved:
                    return False, f"resolves to private IP: {ip_str}"
            except ValueError:
                continue
    except socket.gaierror:
        pass  # DNS 失败交给活性测试

    return True, "safe"


# ============================================================
# HTTP / HTTPS 测试
# ============================================================
def test_http(tracker_url, timeout):
    info_hash, peer_id = make_identity()
    query = (
        'info_hash=' + encode_bytes(info_hash)
        + '&peer_id=' + encode_bytes(peer_id)
        + '&port=6881&uploaded=0&downloaded=0&left=1000000&compact=1&event=started'
    )
    sep = '&' if '?' in tracker_url else '?'
    full = tracker_url + sep + query

    req = urllib.request.Request(
        full,
        headers={'User-Agent': 'Mozilla/5.0 TrackerListBot/3.0'},
    )

    start = time.time()
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read()
    elapsed = (time.time() - start) * 1000

    if not data:
        return False, elapsed, 'empty response'
    try:
        decoded = bdecode(data)
    except Exception:
        return False, elapsed, 'invalid bencoded response'

    if not isinstance(decoded, dict):
        return False, elapsed, 'response is not a bencoded dictionary'

    # bdecode 的 key 都是 bytes，直接检查 bytes key
    if b'failure reason' in decoded:
        return True, elapsed, 'online (failure reason)'
    if b'interval' in decoded or b'complete' in decoded or b'incomplete' in decoded:
        return True, elapsed, 'valid announce response'
    # 有 peers 字段也算有效
    if b'peers' in decoded:
        return True, elapsed, 'valid announce response'
    return True, elapsed, 'online (bencoded dict)'


# ============================================================
# UDP 测试（带重试）
# ============================================================
def test_udp(host, port, timeout, max_retries=2):
    family = socket.AF_INET6 if ':' in host else socket.AF_INET
    sock = socket.socket(family, socket.SOCK_DGRAM)
    sock.settimeout(timeout)
    addr = (host, port)

    txn = random.randint(0, 0xFFFFFFFF)
    connect_packet = struct.pack('>QII', 0x41727101980, 0, txn)

    start = time.time()
    data = None

    for attempt in range(max_retries):
        try:
            sock.sendto(connect_packet, addr)
            remaining = timeout - (time.time() - start)
            if remaining <= 0:
                break
            sock.settimeout(min(remaining, timeout))
            data, _ = sock.recvfrom(2048)
            break
        except socket.timeout:
            continue
        except Exception:
            break

    elapsed = (time.time() - start) * 1000

    if not data or len(data) < 16:
        sock.close()
        return False, elapsed, 'no connect response'

    action, r_txn = struct.unpack('>II', data[:8])
    if r_txn != txn or action != 0:
        sock.close()
        return False, elapsed, 'invalid connect response'

    connection_id = struct.unpack('>Q', data[8:16])[0]

    # 尝试 announce（失败不影响存活判定）
    try:
        info_hash, peer_id = make_identity()
        ap = struct.pack('>QII', connection_id, 1, txn)
        ap += info_hash + peer_id
        ap += struct.pack('>QQQ', 0, 1000000, 0)
        ap += struct.pack('>III', 0, 0, random.randint(0, 0xFFFFFFFF))
        ap += struct.pack('>iH', -1, 6881)
        sock.sendto(ap, addr)
        remaining = timeout - (time.time() - start)
        if remaining > 0:
            sock.settimeout(min(remaining, 3))
            try:
                adata, _ = sock.recvfrom(2048)
                if adata and len(adata) >= 8:
                    sock.close()
                    return True, elapsed, 'valid connect + announce'
            except socket.timeout:
                pass
    except Exception:
        pass

    sock.close()
    return True, elapsed, 'valid connect (announce not confirmed)'


# ============================================================
# WSS / WS 测试
# ============================================================
def test_wss(host, port, timeout):
    context = ssl.create_default_context()
    start = time.time()
    sock = None
    ssock = None
    try:
        sock = socket.create_connection((host, port), timeout=timeout)
        ssock = context.wrap_socket(sock, server_hostname=host)
        elapsed = (time.time() - start) * 1000
        return True, elapsed, 'TLS reachable'
    finally:
        if ssock:
            try:
                ssock.close()
            except Exception:
                pass
        elif sock:
            try:
                sock.close()
            except Exception:
                pass


def test_ws(host, port, timeout):
    start = time.time()
    sock = None
    try:
        sock = socket.create_connection((host, port), timeout=timeout)
        elapsed = (time.time() - start) * 1000
        return True, elapsed, 'TCP reachable'
    finally:
        if sock:
            try:
                sock.close()
            except Exception:
                pass


# ============================================================
# 单个 tracker 分发测试
# ============================================================
def test_one(tracker, timeout):
    safe, reason = is_safe_tracker(tracker)
    if not safe:
        return tracker, 'unsafe', reason, 0.0

    try:
        parsed = urllib.parse.urlparse(tracker)
    except Exception:
        return tracker, 'dead', 'unparseable URL', 0.0

    scheme = parsed.scheme.lower()
    host = parsed.hostname
    port = parsed.port

    if host and host.endswith('.i2p'):
        return tracker, 'untestable', 'I2P network required', 0.0

    try:
        if scheme in ('http', 'https'):
            ok, elapsed, detail = test_http(tracker, timeout)
            return tracker, 'alive' if ok else 'dead', detail, elapsed

        if scheme == 'udp':
            if port is None:
                port = 6969
            ok, elapsed, detail = test_udp(host, port, timeout)
            return tracker, 'alive' if ok else 'dead', detail, elapsed

        if scheme == 'wss':
            if port is None:
                port = 443
            ok, elapsed, detail = test_wss(host, port, timeout)
            return tracker, 'alive' if ok else 'dead', detail, elapsed

        if scheme == 'ws':
            if port is None:
                port = 80
            ok, elapsed, detail = test_ws(host, port, timeout)
            return tracker, 'alive' if ok else 'dead', detail, elapsed

        return tracker, 'untestable', f'unsupported scheme: {scheme}', 0.0

    except socket.timeout:
        return tracker, 'dead', 'timeout', float(timeout * 1000)
    except ConnectionRefusedError:
        return tracker, 'dead', 'connection refused', 0.0
    except socket.gaierror:
        return tracker, 'dead', 'DNS resolution failed', 0.0
    except Exception as e:
        return tracker, 'dead', f'{type(e).__name__}: {e}', 0.0


# ============================================================
# 历史状态加载/保存
# ============================================================
def load_history():
    """加载上一次的 alive 列表，用于稳定性加权。"""
    path = os.path.join(ut.OUTPUT_DIR, 'test_state.json')
    if os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return {"alive_history": [], "consecutive_alive": {}}


def save_history(alive_trackers):
    """保存本次 alive 列表和连续存活计数。"""
    old = load_history()
    old_set = set(old.get("alive_history", []))
    consecutive = old.get("consecutive_alive", {})

    new_consecutive = {}
    for t in alive_trackers:
        new_consecutive[t] = consecutive.get(t, 0) + 1

    state = {
        "alive_history": alive_trackers,
        "consecutive_alive": new_consecutive,
        "last_update": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }
    path = os.path.join(ut.OUTPUT_DIR, 'test_state.json')
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(state, f, indent=2, ensure_ascii=False)
    except IOError:
        pass


# ============================================================
# 综合评分排序
# ============================================================
def compute_score(elapsed_ms, consecutive_days):
    """
    综合评分 = 速度分(70%) + 稳定性分(30%)
    速度分：基于响应时间的归一化（越快分越高）
    稳定性分：连续存活天数（越多分越高）
    返回分数，越高越好。
    """
    # 速度分：100ms 满分，1000ms 归零，超过 1000ms 为 0（连续单调递减）
    if elapsed_ms <= 0:
        speed_score = 0
    elif elapsed_ms <= 100:
        speed_score = 100
    elif elapsed_ms <= 1000:
        speed_score = 100 - (elapsed_ms - 100) / 9  # 100ms=100, 1000ms=0
    else:
        speed_score = 0

    # 稳定性分：连续存活天数，最多 7 天满分
    stability_score = min(consecutive_days, 7) / 7 * 100

    return speed_score * 0.7 + stability_score * 0.3


# ============================================================
# 读取合并列表
# ============================================================
def read_merged():
    path = os.path.join(ut.OUTPUT_DIR, ut.MERGED_FILE)
    trackers = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                trackers.append(line)
    return trackers


def read_candidates(max_count=500):
    """按来源优先级读取候选 tracker。

    精选源（XIU2 / newtrackon / ngosang，人工维护、质量高）优先测试，
    再从合并大列表（含 adysec 数千条）中补足到 max_count，
    避免在 GitHub Actions 中对数千个 tracker 全量测试而超时。
    """
    seen = set()
    ordered = []

    def _ingest(filename):
        path = os.path.join(ut.OUTPUT_DIR, filename)
        if not os.path.exists(path):
            return
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and line not in seen:
                    seen.add(line)
                    ordered.append(line)

    # 1. 精选源优先（这些列表本身已做过筛选，存活率高）
    for priority_file in ("trackers_xiu2.txt", "trackers_newtrackon.txt",
                          "trackers_ngosang.txt"):
        _ingest(priority_file)

    # 2. 从合并大列表补足（adysec 等海量来源）
    for t in read_merged():
        if len(ordered) >= max_count:
            break
        if t not in seen:
            seen.add(t)
            ordered.append(t)

    return ordered[:max_count]


# ============================================================
# 写结果文件
# ============================================================
def write_result_file(filename, trackers, description):
    now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
    header = [
        '# Auto-generated by test_trackers.py',
        f'# Last tested: {now} UTC',
        f'# {description}',
        f'# Total: {len(trackers)}',
        '',
    ]
    body = '\n'.join(trackers)
    if trackers:
        body += '\n'
    content = '\n'.join(header) + body
    ut.atomic_write(os.path.join(ut.OUTPUT_DIR, filename), content)


# ============================================================
# 写测试报告
# ============================================================
def write_report(results, alive_final, alive_sorted, capped, elapsed, protocol_stats):
    alive = [(t, d, e) for t, s, d, e in results if s == 'alive']
    dead = [(t, d, e) for t, s, d, e in results if s == 'dead']
    unsafe = [(t, d, e) for t, s, d, e in results if s == 'unsafe']
    untestable = [(t, d, e) for t, s, d, e in results if s == 'untestable']
    total = len(results)
    now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

    lines = [
        '# Tracker 活性测试 + 综合评分排序报告',
        '',
        f'- 测试时间: {now}',
        f'- 总 Tracker 数: {total}',
        f'- 存活 (alive): **{len(alive)}** ({len(alive) * 100 // total if total else 0}%)',
        f'- 失效 (dead): **{len(dead)}**',
        f'- 不安全 (unsafe): **{len(unsafe)}**',
        f'- 无法测试 (untestable): {len(untestable)}',
        f'- 综合评分后保留前 {ut.MAX_TRACKERS} 个，淘汰 {len(capped)} 个',
        f'- 耗时: {elapsed:.1f} 秒',
        '',
        '## 协议分布',
        '',
    ]
    for proto, count in sorted(protocol_stats.items(), key=lambda x: -x[1]):
        lines.append(f'- {proto}: {count}')

    lines += ['', f'## 最终订阅列表（前 {ut.MAX_TRACKERS} 个，按综合评分降序）', '']
    for rank, (t, score, speed, days) in enumerate(alive_final, 1):
        lines.append(f'{rank}. `{t}` — score={score:.1f}, {speed:.0f}ms, 连续{days}天')

    if dead:
        lines += ['', '## 失效 Tracker', '']
        for t, d, e in sorted(dead):
            lines.append(f'- `{t}` — {d}')

    if unsafe:
        lines += ['', '## 不安全 Tracker（已过滤）', '']
        for t, d, e in sorted(unsafe):
            lines.append(f'- `{t}` — {d}')

    if untestable:
        lines += ['', '## 无法测试（特殊网络）', '']
        for t, d, e in sorted(untestable):
            lines.append(f'- `{t}` — {d}')

    ut.atomic_write(os.path.join(ut.OUTPUT_DIR, 'test_report.md'), '\n'.join(lines) + '\n')


# ============================================================
# 主流程
# ============================================================
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout', type=int, default=10)
    parser.add_argument('--workers', type=int, default=30)
    parser.add_argument('--no-second-pass', action='store_true', help='跳过第二轮精测')
    parser.add_argument('--max-candidates', type=int, default=500,
                        help='第一轮最多测试的候选数（精选源优先，默认500）')
    args = parser.parse_args()

    total_available = len(read_merged())
    trackers = read_candidates(args.max_candidates)
    print(f'[INFO] Testing {len(trackers)} of {total_available} candidates '
          f'(timeout={args.timeout}s, workers={args.workers}, '
          f'priority sources first)')
    print(f'[INFO] Max alive trackers after scoring: {ut.MAX_TRACKERS}')

    history = load_history()
    consecutive = history.get("consecutive_alive", {})

    # ---- 第一轮：全量探活 ----
    results = []
    start = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(test_one, t, args.timeout): t for t in trackers}
        done_count = 0
        for future in as_completed(futures):
            try:
                tracker, status, detail, elapsed_ms = future.result()
            except Exception as e:
                tracker = futures[future]
                status, detail, elapsed_ms = 'dead', f'worker exception: {e}', 0.0
            results.append((tracker, status, detail, elapsed_ms))
            done_count += 1
            marker = {'alive': '[ALIVE]', 'dead': '[DEAD] ', 'untestable': '[SKIP]  ',
                      'unsafe': '[BLOCK]'}[status]
            speed = f' {elapsed_ms:.0f}ms' if status == 'alive' else ''
            if done_count % 25 == 0 or status == 'alive':
                print(f'  {marker} ({done_count}/{len(trackers)}) {tracker}{speed} — {detail}')

    first_pass_elapsed = time.time() - start
    print(f'\n[INFO] First pass done in {first_pass_elapsed:.1f}s')

    # ---- 第二轮：对存活的前 100 个精测 ----
    alive_first = [(t, d, e) for t, s, d, e in results if s == 'alive']
    alive_first.sort(key=lambda x: x[2])  # 按速度升序
    second_pass_targets = [t for t, _, _ in alive_first[:100]]

    if not args.no_second_pass and second_pass_targets:
        print(f'[INFO] Second pass: re-testing top {len(second_pass_targets)} alive trackers...')
        second_results = {}
        with ThreadPoolExecutor(max_workers=min(args.workers, 15)) as pool:
            futures = {pool.submit(test_one, t, max(args.timeout - 2, 5)): t for t in second_pass_targets}
            for future in as_completed(futures):
                try:
                    tracker, status, detail, elapsed_ms = future.result()
                    if status == 'alive':
                        second_results[tracker] = elapsed_ms
                except Exception:
                    pass

        # 合并两轮结果：取较优（较快）的速度
        updated_results = []
        for tracker, status, detail, elapsed_ms in results:
            if tracker in second_results:
                best_speed = min(elapsed_ms, second_results[tracker])
                updated_results.append((tracker, status, detail, best_speed)
            else:
                updated_results.append((tracker, status, detail, elapsed_ms))
        results = updated_results
        print(f'[INFO] Second pass done, refined {len(second_results)} trackers')

    total_elapsed = time.time() - start

    # ---- 协议统计 ----
    protocol_stats = {}
    for t, s, _, _ in results:
        if s == 'alive':
            scheme = t.split('://')[0].lower() if '://' in t else 'unknown'
            protocol_stats[scheme] = protocol_stats.get(scheme, 0) + 1

    # ---- 综合评分排序 ----
    alive_with_speed = [(t, d, e) for t, s, d, e in results if s == 'alive']
    scored = []
    for t, d, e in alive_with_speed:
        days = consecutive.get(t, 0)
        score = compute_score(e, days)
        scored.append((t, score, e, days, d))

    # 按综合评分降序，分数相同按速度升序
    scored.sort(key=lambda x: (-x[1], x[2]))

    alive_final_list = [t for t, _, _, _, _ in scored[:ut.MAX_TRACKERS]]
    alive_final_detail = [(t, score, speed, days) for t, score, speed, days, _ in scored[:ut.MAX_TRACKERS]]
    capped = scored[ut.MAX_TRACKERS:]

    # 失效 = dead + unsafe + 被淘汰的
    dead_final = sorted(
        [t for t, s, _, _ in results if s in ('dead', 'unsafe')]
        + [t for t, _, _, _, _ in capped]
    )

    write_result_file(
        ut.ALIVE_FILE, alive_final_list,
        f'Trackers that PASSED liveness test, top {ut.MAX_TRACKERS} by composite score'
    )
    write_result_file(
        ut.DEAD_FILE, dead_final,
        'Trackers that FAILED, were unsafe, or were capped by score limit'
    )
    write_report(results, alive_final_detail, scored, capped, total_elapsed, protocol_stats)
    save_history(alive_final_list)

    n_alive = len(alive_final_list)
    n_dead = len(dead_final)
    n_capped = len(capped)
    n_unsafe = sum(1 for _, s, _, _ in results if s == 'unsafe')

    print(f'\n===== Test Summary =====')
    print(f'  Total tested:   {len(trackers)}')
    print(f'  Alive (raw):    {len(alive_with_speed)}')
    print(f'  Alive (final):  {n_alive} (top {ut.MAX_TRACKERS} by composite score)')
    print(f'  Score-capped:   {n_capped}')
    print(f'  Unsafe filtered:{n_unsafe}')
    print(f'  Dead final:     {n_dead}')
    print(f'  Time:           {total_elapsed:.1f}s')
    print(f'  Protocols:      {protocol_stats}')
    print('=========================')

    # 重新生成主页
    repo = ut.get_repo()
    page_stats = [
        (ut.ALIVE_FILE, n_alive),
        (ut.MERGED_FILE, total_available),
        (ut.DEAD_FILE, n_dead),
    ]
    ut.generate_pages(repo, page_stats)
    print('[OK] Pages regenerated with alive statistics.')

    ut.sync_plain_text_files()
    print('[OK] Plain-text files synced to docs/.')


if __name__ == '__main__':
    main()
