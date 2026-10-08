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
DNS_RETRIES = 3


def cached_getaddrinfo(host, port=None):
    """带缓存的 DNS 解析。

    仅缓存成功结果；失败时重试且不缓存，避免瞬时解析失败（DNS 污染/抖动）
    被永久固化，从而提升解析稳定性。
    """
    key = (host, port)
    cached = _dns_cache.get(key)
    if cached is not None:
        return cached
    last_error = None
    for attempt in range(DNS_RETRIES):
        try:
            result = socket.getaddrinfo(host, port)
            _dns_cache[key] = result
            return result
        except socket.gaierror as e:
            last_error = e
            time.sleep(0.3 * (attempt + 1))
    raise last_error


def _is_ipv6_literal(host):
    try:
        return ipaddress.ip_address(host).version == 6
    except ValueError:
        return False


_ipv6_available = None


def ipv6_available():
    """探测本机是否具备 IPv6 出口。

    不具备时把 IPv6 字面量 tracker 标为 untestable（而非 dead），
    避免在无 IPv6 网络环境下把它们误判为失效并浪费时间探活。
    """
    global _ipv6_available
    if _ipv6_available is None:
        if not socket.has_ipv6:
            _ipv6_available = False
        else:
            try:
                s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
                s.settimeout(2)
                try:
                    s.connect(("2001:4860:4860::8888", 53))
                    _ipv6_available = True
                finally:
                    s.close()
            except Exception:
                _ipv6_available = False
    return _ipv6_available


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
class _LimitedRedirectHandler(urllib.request.HTTPRedirectHandler):
    max_redirections = 3


_http_opener = urllib.request.build_opener(_LimitedRedirectHandler())


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
    with _http_opener.open(req, timeout=timeout) as resp:
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

    if host and _is_ipv6_literal(host) and not ipv6_available():
        return tracker, 'untestable', 'IPv6 unavailable here', 0.0

    try:
        if scheme in ('http', 'https'):
            ok, elapsed, detail = test_http(tracker, timeout)
            return tracker, 'alive' if ok else 'dead', detail, elapsed

        if scheme == 'udp':
            if port is None:
                return tracker, 'dead', 'missing port', 0.0
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
    """加载上一次的状态，用于存活率 EMA 加权与动态黑名单。"""
    path = os.path.join(ut.OUTPUT_DIR, 'test_state.json')
    if os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return {"alive_history": [], "uptime_ema": {}, "dead_streak": {}}


DEAD_BLACKLIST_RUNS = 20  # 连续失效 N 次（约 5 天 @ 4 次/天）→ 自动列入动态黑名单
UPTIME_ALPHA = 0.2       # 存活率 EMA 权重（半衰期约 3 次运行）


def save_history(alive_trackers, dead_trackers=None):
    """保存本次 alive/dead 列表，维护存活率 EMA 与连续失效计数。

    返回新的 dead_streak 字典，供动态黑名单生成。
    """
    old = load_history()
    uptime = old.get("uptime_ema", {})
    dead_streak = old.get("dead_streak", {})

    alive_set = set(alive_trackers)
    dead_set = set(dead_trackers or [])
    observed = alive_set | dead_set

    new_uptime = dict(uptime)
    for t in observed:
        val = 1.0 if t in alive_set else 0.0
        new_uptime[t] = uptime.get(t, 0.0) * (1 - UPTIME_ALPHA) + UPTIME_ALPHA * val

    new_dead_streak = dict(dead_streak)
    for t in alive_set:
        new_dead_streak.pop(t, None)   # 存活即清零失效 streak
    for t in dead_set:
        new_dead_streak[t] = dead_streak.get(t, 0) + 1

    state = {
        "alive_history": sorted(alive_set),
        "uptime_ema": new_uptime,
        "dead_streak": new_dead_streak,
        "last_update": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }
    path = os.path.join(ut.OUTPUT_DIR, 'test_state.json')
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(state, f, indent=2, ensure_ascii=False)
    except IOError:
        pass
    return new_dead_streak


def write_dynamic_blacklist(dead_streak, threshold=DEAD_BLACKLIST_RUNS):
    """连续失效 ≥ threshold 次的 tracker 写入动态黑名单（精确 URL）。"""
    urls = sorted(t for t, n in dead_streak.items() if n >= threshold)
    path = os.path.join(ut.OUTPUT_DIR, 'blacklist_dynamic.txt')
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write("# 动态黑名单：连续失效 >= %d 次，由 test_trackers.py 自动生成\n" % threshold)
            for u in urls:
                f.write(u + "\n")
    except IOError:
        pass
    return urls


# ============================================================
# 综合评分排序
# ============================================================
def compute_score(elapsed_ms, uptime):
    """
    综合评分 = 速度分(70%) + 稳定性分(30%)
    速度分：基于响应时间的归一化（越快分越高）
    稳定性分：存活率 EMA（0~1，越接近 1 越稳定；偶发失效不会直接清零）
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

    # 稳定性分：存活率 EMA（0~1）→ 0~100
    stability_score = max(0.0, min(1.0, uptime)) * 100

    return speed_score * 0.7 + stability_score * 0.3


def select_top_with_protocol_quota(scored, max_total, min_non_udp):
    """按综合评分选取前 max_total 个，同时保底 min_non_udp 条非 UDP（协议多样性配额）。

    scored 元素为 (tracker, score, speed, uptime, detail)，已按评分降序。
    UDP 握手往返天然快于 HTTP announce，纯速度排序会让 best 列表变成单一协议——
    一旦订阅者网络封 UDP，整份订阅即失效。配额保证 http/https/wss/ws 保底占位，
    其余仍按评分从高到低填充；非 UDP 不足配额时有多少取多少。
    返回 (selected, capped)，selected 仍按评分降序。
    """
    non_udp = [e for e in scored if not e[0].startswith('udp://')]
    udp = [e for e in scored if e[0].startswith('udp://')]

    take_non_udp = min(min_non_udp, len(non_udp), max_total)
    selected = non_udp[:take_non_udp] + udp[:max_total - take_non_udp]

    # 边缘情况：UDP 不足以填满时，用剩余评分最高的条目补齐
    if len(selected) < max_total:
        chosen = {e[0] for e in selected}
        remaining = [e for e in scored if e[0] not in chosen]
        selected += remaining[:max_total - len(selected)]

    selected.sort(key=lambda x: (-x[1], x[2]))
    chosen = {e[0] for e in selected}
    capped = [e for e in scored if e[0] not in chosen]
    return selected, capped


def dedup_same_ip(entries):
    """同 IP 去重：解析到同一 IP 的多个 tracker 只保留响应最快的。

    entries: [(tracker, detail, elapsed_ms)]，返回需移除的 tracker 集合（同 IP 中较慢者）。
    """
    groups = {}
    for t, _, e in entries:
        try:
            host = urllib.parse.urlparse(t).hostname
            if not host:
                continue
            infos = cached_getaddrinfo(host, None)
            ip = infos[0][4][0]
        except Exception:
            continue
        groups.setdefault(ip, []).append((t, e))

    removed = set()
    for lst in groups.values():
        if len(lst) > 1:
            lst.sort(key=lambda x: x[1])  # 按耗时升序，最快在前
            removed.update(t for t, _ in lst[1:])
    return removed


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
    """读取候选 tracker：即 all 合并列表（merged，已按源优先级精选前 MAX_ALL 条）。

    best 计划从中精测，确保 best 严格子集于 all；max_count 仅作上限保护。
    """
    return read_merged()[:max_count]


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
    body = ut.NL.join(trackers)
    if trackers:
        body += ut.NL
    content = ut.NL.join(header) + body
    ut.atomic_write(os.path.join(ut.OUTPUT_DIR, filename), content)


# ============================================================
# 写测试报告
# ============================================================
def write_report(results, alive_final, alive_sorted, capped, elapsed, protocol_stats, low_speed=None, same_ip_removed=None):
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
        f'- 低速淘汰 (low-speed >5s): {len(low_speed or [])}',
        f'- 同 IP 去重 (kept faster): {len(same_ip_removed or [])}',
        f'- 综合评分后保留前 {ut.MAX_TRACKERS} 个，淘汰 {len(capped)} 个',
        f'- 协议多样性配额: 保底 {ut.MIN_NON_UDP_TRACKERS} 条非 UDP，'
        f'实际保留 {sum(1 for t, *_ in alive_final if not t.startswith("udp://"))} 条',
        f'- 耗时: {elapsed:.1f} 秒',
        '',
        '## 协议分布',
        '',
    ]
    for proto, count in sorted(protocol_stats.items(), key=lambda x: -x[1]):
        lines.append(f'- {proto}: {count}')

    lines += ['', f'## 最终订阅列表（前 {ut.MAX_TRACKERS} 个，按综合评分降序）', '']
    for rank, (t, score, speed, up) in enumerate(alive_final, 1):
        lines.append(f'{rank}. `{t}` — score={score:.1f}, {speed:.0f}ms, 存活率{up*100:.0f}%')

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

    if low_speed:
        lines += ['', '## 低速 Tracker（>5s，已排除）', '']
        for t, e in sorted(low_speed, key=lambda x: x[1]):
            lines.append(f'- `{t}` — {e:.0f}ms')

    if same_ip_removed:
        lines += ['', '## 同 IP 去重（保留响应最快）', '']
        for t in sorted(same_ip_removed):
            lines.append(f'- `{t}`')

    ut.atomic_write(os.path.join(ut.OUTPUT_DIR, 'test_report.md'), ut.NL.join(lines) + ut.NL)


# ============================================================
# 主流程
# ============================================================
def daily_backup_alive():
    """把 trackers_alive.txt 按日期备份到 trackers/backup/，保留7天。"""
    src = os.path.join(ut.OUTPUT_DIR, ut.ALIVE_FILE)
    if not os.path.exists(src):
        return
    backup_dir = os.path.join(ut.OUTPUT_DIR, "backup")
    os.makedirs(backup_dir, exist_ok=True)
    today = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d")
    dst = os.path.join(backup_dir, f"trackers_alive_{today}.txt")
    with open(src, "r", encoding="utf-8") as f:
        content = f.read()
    ut.atomic_write(dst, content)
    cutoff = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=7)
    for fn in os.listdir(backup_dir):
        if fn.startswith("trackers_alive_") and fn.endswith(".txt"):
            try:
                d = datetime.datetime.strptime(fn[len("trackers_alive_"):-4], "%Y%m%d").replace(tzinfo=datetime.timezone.utc)
                if d < cutoff:
                    os.remove(os.path.join(backup_dir, fn))
            except ValueError:
                pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout', type=int, default=10)
    parser.add_argument('--workers', type=int, default=30)
    parser.add_argument('--no-second-pass', action='store_true', help='跳过第二轮精测')
    parser.add_argument('--max-candidates', type=int, default=500,
                        help='第一轮最多测试的候选数（精选源优先，默认500）')
    parser.add_argument('--breaker-consecutive', type=int, default=20,
                        help='连续超时达到该值触发一次熔断暂停（默认20）')
    parser.add_argument('--breaker-trips', type=int, default=3,
                        help='熔断累计次数达到该值则终止（默认3）')
    parser.add_argument('--breaker-pause', type=int, default=60,
                        help='每次熔断暂停秒数（默认60）')
    args = parser.parse_args()

    if not ut.SOURCES:
        print('[INFO] SOURCES is empty - no subscription sources configured, nothing to test.')
        return

    merged_path = os.path.join(ut.OUTPUT_DIR, ut.MERGED_FILE)
    if not os.path.exists(merged_path):
        print(f'[INFO] {os.path.relpath(merged_path, ut.PROJECT_ROOT)} not found - nothing to test.')
        return

    total_available = len(read_merged())
    trackers = read_candidates(args.max_candidates)
    print(f'[INFO] Testing {len(trackers)} candidates '
          f'(all-pool={total_available}, timeout={args.timeout}s, '
          f'workers={args.workers})')
    print(f'[INFO] Max alive trackers after scoring: {ut.MAX_TRACKERS}')

    history = load_history()
    uptime_map = history.get("uptime_ema", {})

    # ---- 第一轮：全量探活（带熔断）----
    results = []
    start = time.time()
    consecutive_timeouts = 0
    breaker_trips = 0
    aborted = False
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

            # 熔断：连续超时 → 暂停；累计次数 → 终止（保留上次 alive.txt）
            # 有存活即重置累计，避免正常的“连遇死节点”被误判为网络故障
            if status == 'dead' and detail == 'timeout':
                consecutive_timeouts += 1
            else:
                consecutive_timeouts = 0
                if status == 'alive':
                    breaker_trips = 0
            if consecutive_timeouts >= args.breaker_consecutive:
                breaker_trips += 1
                consecutive_timeouts = 0
                print(f'[WARN] circuit_breaker: {args.breaker_consecutive} consecutive timeouts, '
                      f'pausing {args.breaker_pause}s (trip {breaker_trips}/{args.breaker_trips})')
                time.sleep(args.breaker_pause)
                if breaker_trips >= args.breaker_trips:
                    print('[ERROR] circuit_breaker_triggered: aborting, keeping previous trackers_alive.txt')
                    aborted = True
                    for f in futures:
                        f.cancel()
                    break

    first_pass_elapsed = time.time() - start
    print(f'{ut.NL}[INFO] First pass done in {first_pass_elapsed:.1f}s')

    if aborted:
        print('[WARN] Circuit breaker triggered; keeping previous trackers_alive.txt, exiting.')
        return

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
                updated_results.append((tracker, status, detail, best_speed))
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

    # ---- 低速淘汰：响应 > 5 秒直接标记为低速并排除（参考 adysec/tracker Rust 清洗工具）----
    LOW_SPEED_THRESHOLD_MS = 5000.0  # 5.0 秒
    low_speed = sorted(
        (t, e) for t, s, d, e in results if s == 'alive' and e > LOW_SPEED_THRESHOLD_MS
    )
    low_speed_trackers = {t for t, _ in low_speed}
    if low_speed:
        print(f'[INFO] Low-speed filtered (>5s): {len(low_speed)} trackers')

    # ---- 综合评分排序 ----
    alive_with_speed = [(t, d, e) for t, s, d, e in results
                        if s == 'alive' and t not in low_speed_trackers]

    # ---- 同 IP 去重：解析到同一 IP 只保留响应最快的 ----
    same_ip_removed = dedup_same_ip(alive_with_speed)
    if same_ip_removed:
        print(f'[INFO] Same-IP dedup removed {len(same_ip_removed)} slower tracker(s)')
    alive_with_speed = [(t, d, e) for t, d, e in alive_with_speed if t not in same_ip_removed]

    scored = []
    for t, d, e in alive_with_speed:
        up = uptime_map.get(t, 0.0)
        score = compute_score(e, up)
        scored.append((t, score, e, up, d))

    # 按综合评分降序，分数相同按速度升序
    scored.sort(key=lambda x: (-x[1], x[2]))

    # 协议多样性配额：保底 MIN_NON_UDP_TRACKERS 条非 UDP，其余按评分填充
    selected, capped = select_top_with_protocol_quota(
        scored, ut.MAX_TRACKERS, ut.MIN_NON_UDP_TRACKERS
    )
    alive_final_list = [t for t, _, _, _, _ in selected]
    alive_final_detail = [(t, score, speed, up) for t, score, speed, up, _ in selected]
    n_non_udp_kept = sum(1 for t in alive_final_list if not t.startswith('udp://'))

    # 失效 = dead + unsafe + 低速 + 同IP重复 + 被淘汰的
    dead_final = sorted(
        [t for t, s, _, _ in results if s in ('dead', 'unsafe')]
        + [t for t, _, _, _, _ in capped]
        + sorted(low_speed_trackers)
        + sorted(same_ip_removed)
    )

    write_result_file(
        ut.ALIVE_FILE, alive_final_list,
        f'Trackers that PASSED liveness test, top {ut.MAX_TRACKERS} by composite score '
        f'(>= {ut.MIN_NON_UDP_TRACKERS} non-UDP by protocol quota)'
    )
    write_result_file(
        ut.DEAD_FILE, dead_final,
        'Trackers that FAILED, were unsafe, were low-speed, were same-IP duplicates, or were capped by score limit'
    )
    write_report(results, alive_final_detail, scored, capped, total_elapsed, protocol_stats, low_speed, same_ip_removed)
    dead_streak = save_history(alive_final_list, dead_final)
    dyn_blacklist = write_dynamic_blacklist(dead_streak)
    if dyn_blacklist:
        print(f'[INFO] Dynamic blacklist: {len(dyn_blacklist)} consistently-dead trackers')

    n_alive = len(alive_final_list)
    n_dead = len(dead_final)
    n_capped = len(capped)
    n_unsafe = sum(1 for _, s, _, _ in results if s == 'unsafe')

    print(f'{ut.NL}===== Test Summary =====')
    print(f'  Total tested:   {len(trackers)}')
    print(f'  Alive (raw):    {len(alive_with_speed)}')
    print(f'  Alive (final):  {n_alive} (top {ut.MAX_TRACKERS} by composite score)')
    print(f'  Non-UDP kept:   {n_non_udp_kept} (quota >= {ut.MIN_NON_UDP_TRACKERS})')
    print(f'  Score-capped:   {n_capped}')
    print(f'  Unsafe filtered:{n_unsafe}')
    print(f'  Low-speed:      {len(low_speed)} (>5s excluded)')
    print(f'  Same-IP dedup:  {len(same_ip_removed)} (kept faster)')
    print(f'  Dead final:     {n_dead}')
    print(f'  Time:           {total_elapsed:.1f}s')
    print('=== 协议分布统计 ===')
    for proto in ('http', 'https', 'udp', 'wss', 'ws'):
        print(f'  {proto.upper():<6}: {protocol_stats.get(proto, 0)} 个')
    print(f'  总计: {sum(protocol_stats.values())} 个（存活）')
    print('=========================')

    # 回填 run_summary.json 的 alive_lines（update_trackers.py 先于测试运行，恒为 null）
    try:
        if os.path.exists(ut.RUN_SUMMARY_FILE):
            with open(ut.RUN_SUMMARY_FILE, 'r', encoding='utf-8') as fh:
                summary = json.load(fh)
            summary['alive_lines'] = n_alive
            ut.atomic_write(ut.RUN_SUMMARY_FILE,
                            json.dumps(summary, ensure_ascii=False, indent=2) + ut.NL)
    except Exception as e:
        print(f'[WARN] Could not backfill alive_lines into run_summary.json: {e}')

    daily_backup_alive()

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
