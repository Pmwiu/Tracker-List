#!/usr/bin/env python3
"""
Tracker 活性自动测试 + 测速排序脚本。

对合并列表中的每个 Tracker 执行:
  1. 安全过滤（排除内网/localhost/非标准地址）
  2. 协议级探活 + 响应速度测量
     - http/https : 发送标准 BitTorrent announce 请求，验证 bencoded 响应，记录耗时
     - udp        : 完整 UDP tracker connect 握手，记录耗时
     - wss        : TCP + TLS 连通性检查，记录耗时
  3. 存活 Tracker 按响应速度升序排序
  4. 取前 MAX_TRACKERS 个写入 alive.txt，超出部分标记为 speed-capped

输出:
  - trackers/trackers_alive.txt   通过测试且速度最快的前 N 个（推荐订阅）
  - trackers/trackers_dead.txt    失效 / 被限速淘汰的 Tracker
  - trackers/test_report.md       人类可读测试报告（含速度排名）

用法:
  python scripts/test_trackers.py
  python scripts/test_trackers.py --timeout 12 --workers 25
"""

import os
import sys
import ssl
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

# 复用主脚本的路径、常量与页面生成函数
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
import update_trackers as ut


# ============================================================
# bencode 解码器（用于验证 HTTP tracker 响应）
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


# ============================================================
# 构造测试用固定身份
# ============================================================
def make_identity():
    info_hash = os.urandom(20)
    peer_id = b'-TT0200-' + os.urandom(12)
    return info_hash, peer_id


def encode_bytes(b):
    """按 BitTorrent 规范对二进制参数逐字节 URL 编码。"""
    return ''.join('%%%02X' % x for x in b)


# ============================================================
# 安全过滤：排除内网、localhost、保留地址等危险/无效 Tracker
# ============================================================
def is_safe_tracker(tracker_url):
    """检查 tracker 地址是否安全（非内网、非保留地址、非 localhost）。"""
    try:
        parsed = urllib.parse.urlparse(tracker_url)
    except Exception:
        return False, "unparseable URL"

    host = parsed.hostname
    if not host:
        return False, "no hostname"

    host_lower = host.lower()
    # 排除 localhost 和本地域名
    if host_lower in ('localhost', 'localhost.localdomain') or host_lower.endswith('.local'):
        return False, "localhost address"

    # 尝试解析为 IP，检查是否为内网/保留地址
    try:
        ip = ipaddress.ip_address(host)
        if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved or ip.is_multicast:
            return False, f"private/reserved IP: {host}"
    except ValueError:
        # 不是 IP 而是域名，通过 DNS 解析后检查
        try:
            infos = socket.getaddrinfo(host, None)
            for family, _, _, _, sockaddr in infos:
                ip_str = sockaddr[0]
                try:
                    ip = ipaddress.ip_address(ip_str)
                    if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved:
                        return False, f"resolves to private IP: {ip_str}"
                except ValueError:
                    continue
        except socket.gaierror:
            # DNS 解析失败，交给后续活性测试判定
            pass

    return True, "safe"


# ============================================================
# HTTP / HTTPS tracker 测试（含测速）
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
        headers={'User-Agent': 'Mozilla/5.0 TrackerListBot/2.0'},
    )

    start = time.time()
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read()
    elapsed = (time.time() - start) * 1000  # ms

    if not data:
        return False, elapsed, 'empty response'
    try:
        decoded = bdecode(data)
    except Exception:
        return False, elapsed, 'invalid bencoded response'

    if not isinstance(decoded, dict):
        return False, elapsed, 'response is not a bencoded dictionary'

    if b'failure reason' in decoded or b'failure reason'.decode() in decoded:
        return True, elapsed, 'online (failure reason)'
    return True, elapsed, 'valid announce response'


# ============================================================
# UDP tracker 测试（含测速）
# ============================================================
def test_udp(host, port, timeout):
    family = socket.AF_INET6 if ':' in host else socket.AF_INET
    sock = socket.socket(family, socket.SOCK_DGRAM)
    sock.settimeout(timeout)
    addr = (host, port)

    txn = random.randint(0, 0xFFFFFFFF)
    connect_packet = struct.pack('>QII', 0x41727101980, 0, txn)

    deadline = time.time() + timeout
    connection_id = None
    sent = False
    data = None
    start = time.time()
    while time.time() < deadline:
        if not sent:
            sock.sendto(connect_packet, addr)
            sent = True
        remaining = deadline - time.time()
        if remaining <= 0:
            break
        sock.settimeout(min(remaining, max(remaining / 2, 1)))
        try:
            data, _ = sock.recvfrom(2048)
            break
        except socket.timeout:
            sent = False
            continue
    else:
        data = None

    elapsed = (time.time() - start) * 1000  # ms

    if not data or len(data) < 16:
        sock.close()
        return False, elapsed, 'no connect response'

    action, r_txn = struct.unpack('>II', data[:8])
    connection_id = struct.unpack('>Q', data[8:16])[0]
    if r_txn != txn or action != 0:
        sock.close()
        return False, elapsed, 'invalid connect response'

    # connect 成功即证明在线；尝试 announce（失败不影响存活）
    try:
        info_hash, peer_id = make_identity()
        ap = struct.pack('>QII', connection_id, 1, txn)
        ap += info_hash + peer_id
        ap += struct.pack('>QQQ', 0, 1000000, 0)
        ap += struct.pack('>III', 0, 0, random.randint(0, 0xFFFFFFFF))
        ap += struct.pack('>iH', -1, 6881)
        sock.sendto(ap, addr)
        remaining = deadline - time.time()
        if remaining > 0:
            sock.settimeout(remaining)
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
# WSS tracker 测试（含测速）
# ============================================================
def test_wss(host, port, timeout):
    context = ssl.create_default_context()
    start = time.time()
    sock = socket.create_connection((host, port), timeout=timeout)
    try:
        ssock = context.wrap_socket(sock, server_hostname=host)
        ssock.close()
    except Exception:
        sock.close()
        raise
    elapsed = (time.time() - start) * 1000
    return True, elapsed, 'TLS reachable'


# ============================================================
# 单个 tracker 分发测试（含安全过滤+测速）
# ============================================================
def test_one(tracker, timeout):
    """返回 (tracker, 状态, 详情, 响应时间ms)，状态: alive/dead/untestable/unsafe"""
    # 第一步：安全过滤
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

        if scheme in ('wss', 'ws'):
            if port is None:
                port = 443 if scheme == 'wss' else 80
            if scheme == 'wss':
                ok, elapsed, detail = test_wss(host, port, timeout)
            else:
                start = time.time()
                sock = socket.create_connection((host, port), timeout=timeout)
                sock.close()
                elapsed = (time.time() - start) * 1000
                ok, detail = True, 'TCP reachable'
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
    path = os.path.join(ut.OUTPUT_DIR, filename)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(header) + '\n'.join(trackers) + ('\n' if trackers else ''))


# ============================================================
# 写测试报告（含速度排名）
# ============================================================
def write_report(results, alive_sorted, capped, elapsed):
    alive = [(t, d, e) for t, s, d, e in results if s == 'alive']
    dead = [(t, d, e) for t, s, d, e in results if s == 'dead']
    unsafe = [(t, d, e) for t, s, d, e in results if s == 'unsafe']
    untestable = [(t, d, e) for t, s, d, e in results if s == 'untestable']
    total = len(results)
    now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

    lines = [
        '# Tracker 活性测试 + 测速排序报告',
        '',
        f'- 测试时间: {now}',
        f'- 总 Tracker 数: {total}',
        f'- 存活 (alive): **{len(alive)}** ({len(alive) * 100 // total if total else 0}%)',
        f'- 失效 (dead): **{len(dead)}**',
        f'- 不安全 (unsafe): **{len(unsafe)}**',
        f'- 无法测试 (untestable): {len(untestable)}',
        f'- 速度排序后保留前 {ut.MAX_TRACKERS} 个，淘汰 {len(capped)} 个',
        f'- 耗时: {elapsed:.1f} 秒',
        '',
        '## 存活 Tracker（按响应速度升序，前 N 个进入订阅列表）',
        '',
    ]
    for rank, (t, d, e) in enumerate(alive_sorted, 1):
        cap_mark = ' [CAP-OUT]' if rank > ut.MAX_TRACKERS else ''
        lines.append(f'{rank}. `{t}` — {e:.0f}ms — {d}{cap_mark}')

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

    path = os.path.join(ut.OUTPUT_DIR, 'test_report.md')
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')


# ============================================================
# 主流程
# ============================================================
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout', type=int, default=12)
    parser.add_argument('--workers', type=int, default=25)
    args = parser.parse_args()

    trackers = read_merged()
    print(f'[INFO] Testing {len(trackers)} trackers '
          f'(timeout={args.timeout}s, workers={args.workers})')
    print(f'[INFO] Max alive trackers after speed sort: {ut.MAX_TRACKERS}')

    results = []
    start = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(test_one, t, args.timeout): t for t in trackers}
        done_count = 0
        for future in as_completed(futures):
            tracker, status, detail, elapsed_ms = future.result()
            results.append((tracker, status, detail, elapsed_ms))
            done_count += 1
            marker = {'alive': '[ALIVE]', 'dead': '[DEAD] ', 'untestable': '[SKIP]  ',
                      'unsafe': '[BLOCK]'}[status]
            speed = f' {elapsed_ms:.0f}ms' if status == 'alive' else ''
            print(f'  {marker} ({done_count}/{len(trackers)}) {tracker}{speed} — {detail}')

    elapsed = time.time() - start

    # 存活 Tracker 按响应速度升序排序
    alive_with_speed = [(t, d, e) for t, s, d, e in results if s == 'alive']
    alive_sorted = sorted(alive_with_speed, key=lambda x: x[2])  # 按耗时升序

    # 取前 MAX_TRACKERS 个
    alive_final = [t for t, d, e in alive_sorted[:ut.MAX_TRACKERS]]
    capped = [(t, d, e) for t, d, e in alive_sorted[ut.MAX_TRACKERS:]]

    # 失效 = dead + unsafe + 被速度淘汰的
    dead_final = sorted(
        [t for t, s, d, e in results if s in ('dead', 'unsafe')]
        + [t for t, d, e in capped]
    )

    write_result_file(
        ut.ALIVE_FILE, alive_final,
        f'Trackers that PASSED liveness test, sorted by speed, top {ut.MAX_TRACKERS}'
    )
    write_result_file(
        ut.DEAD_FILE, dead_final,
        'Trackers that FAILED, were unsafe, or were capped by speed limit'
    )
    write_report(results, alive_sorted, capped, elapsed)

    n_alive = len(alive_final)
    n_dead = len(dead_final)
    n_capped = len(capped)
    n_unsafe = sum(1 for _, s, _, _ in results if s == 'unsafe')

    print(f'\n===== Test Summary =====')
    print(f'  Total tested:   {len(trackers)}')
    print(f'  Alive (raw):    {len(alive_with_speed)}')
    print(f'  Alive (final):  {n_alive} (top {ut.MAX_TRACKERS} by speed)')
    print(f'  Speed-capped:   {n_capped}')
    print(f'  Unsafe filtered:{n_unsafe}')
    print(f'  Dead final:     {n_dead}')
    print(f'  Time:           {elapsed:.1f}s')
    print('=========================')

    # 重新生成主页
    repo = ut.get_repo()
    page_stats = [
        (ut.ALIVE_FILE, n_alive),
        (ut.MERGED_FILE, len(trackers)),
        (ut.DEAD_FILE, n_dead),
    ]
    ut.generate_pages(repo, page_stats)
    print('[OK] Pages regenerated with alive statistics.')

    # 同步纯文本文件
    ut.sync_plain_text_files()
    print('[OK] Plain-text files synced to docs/.')


if __name__ == '__main__':
    main()
