#!/usr/bin/env python3
"""
Tracker 活性自动测试脚本。

对合并列表中的每个 Tracker 执行协议级探活:
  - http/https : 发送标准 BitTorrent announce 请求，验证 bencoded 响应
  - udp        : 完整 UDP tracker connect（+announce）握手
  - wss        : TCP + TLS 连通性检查
  - .i2p       : 标记为 untestable（需 I2P 网络，当前环境无法测试）

输出:
  - trackers/trackers_alive.txt   通过测试的 Tracker（推荐订阅）
  - trackers/trackers_dead.txt    未通过测试的 Tracker
  - trackers/test_report.md       人类可读测试报告

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
import urllib.parse
import urllib.request
import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
import update_trackers as ut


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
    peer_id = b'-TT0100-' + os.urandom(12)
    return info_hash, peer_id


def encode_bytes(b):
    return ''.join('%%%02X' % x for x in b)


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
        headers={'User-Agent': 'Mozilla/5.0 TrackerListBot/1.0'},
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read()

    if not data:
        return False, 'empty response'
    try:
        decoded = bdecode(data)
    except Exception:
        return False, 'invalid bencoded response'

    if not isinstance(decoded, dict):
        return False, 'response is not a bencoded dictionary'

    if b'failure reason' in decoded:
        return True, 'online (returned failure reason)'
    return True, 'valid announce response'


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

    if not data or len(data) < 16:
        return False, 'no connect response'

    action, r_txn = struct.unpack('>II', data[:8])
    connection_id = struct.unpack('>Q', data[8:16])[0]
    if r_txn != txn or action != 0:
        return False, 'invalid connect response'

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
                    return True, 'valid connect + announce'
            except socket.timeout:
                pass
    except Exception:
        pass

    return True, 'valid connect (announce not confirmed)'


def test_wss(host, port, timeout):
    context = ssl.create_default_context()
    sock = socket.create_connection((host, port), timeout=timeout)
    try:
        ssock = context.wrap_socket(sock, server_hostname=host)
        ssock.close()
    except Exception:
        sock.close()
        raise
    return True, 'TLS reachable (WebSocket handshake not performed)'


def test_one(tracker, timeout):
    try:
        parsed = urllib.parse.urlparse(tracker)
    except Exception:
        return tracker, 'dead', 'unparseable URL'

    scheme = parsed.scheme.lower()
    host = parsed.hostname
    port = parsed.port

    if host and host.endswith('.i2p'):
        return tracker, 'untestable', 'I2P network required'

    try:
        if scheme in ('http', 'https'):
            ok, detail = test_http(tracker, timeout)
            return tracker, 'alive' if ok else 'dead', detail

        if scheme == 'udp':
            if port is None:
                port = 6969
            ok, detail = test_udp(host, port, timeout)
            return tracker, 'alive' if ok else 'dead', detail

        if scheme in ('wss', 'ws'):
            if port is None:
                port = 443 if scheme == 'wss' else 80
            if scheme == 'wss':
                ok, detail = test_wss(host, port, timeout)
            else:
                sock = socket.create_connection((host, port), timeout=timeout)
                sock.close()
                ok, detail = True, 'TCP reachable'
            return tracker, 'alive' if ok else 'dead', detail

        return tracker, 'untestable', f'unsupported scheme: {scheme}'

    except socket.timeout:
        return tracker, 'dead', 'timeout'
    except ConnectionRefusedError:
        return tracker, 'dead', 'connection refused'
    except socket.gaierror:
        return tracker, 'dead', 'DNS resolution failed'
    except Exception as e:
        return tracker, 'dead', f'{type(e).__name__}: {e}'


def read_merged():
    path = os.path.join(ut.OUTPUT_DIR, ut.MERGED_FILE)
    trackers = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                trackers.append(line)
    return trackers


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


def write_report(results, elapsed):
    alive = [(t, d) for t, s, d in results if s == 'alive']
    dead = [(t, d) for t, s, d in results if s == 'dead']
    untestable = [(t, d) for t, s, d in results if s == 'untestable']
    total = len(results)
    now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

    lines = [
        '# Tracker 活性测试报告',
        '',
        f'- 测试时间: {now}',
        f'- 总 Tracker 数: {total}',
        f'- 存活 (alive): **{len(alive)}** ({len(alive) * 100 // total if total else 0}%)',
        f'- 失效 (dead): **{len(dead)}** ({len(dead) * 100 // total if total else 0}%)',
        f'- 无法测试 (untestable): {len(untestable)}',
        f'- 耗时: {elapsed:.1f} 秒',
        '',
        '## 存活 Tracker',
        '',
    ]
    for t, d in sorted(alive):
        lines.append(f'- `{t}` — {d}')

    lines += ['', '## 失效 Tracker', '']
    for t, d in sorted(dead):
        lines.append(f'- `{t}` — {d}')

    if untestable:
        lines += ['', '## 无法测试（特殊网络）', '']
        for t, d in sorted(untestable):
            lines.append(f'- `{t}` — {d}')

    path = os.path.join(ut.OUTPUT_DIR, 'test_report.md')
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout', type=int, default=12)
    parser.add_argument('--workers', type=int, default=25)
    args = parser.parse_args()

    trackers = read_merged()
    print(f'[INFO] Testing {len(trackers)} trackers '
          f'(timeout={args.timeout}s, workers={args.workers})')

    results = []
    start = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(test_one, t, args.timeout): t for t in trackers}
        done_count = 0
        for future in as_completed(futures):
            tracker, status, detail = future.result()
            results.append((tracker, status, detail))
            done_count += 1
            marker = {'alive': '[ALIVE]', 'dead': '[DEAD] ', 'untestable': '[SKIP]  '}[status]
            print(f'  {marker} ({done_count}/{len(trackers)}) {tracker} — {detail}')

    elapsed = time.time() - start

    alive_sorted = sorted(t for t, s, _ in results if s == 'alive')
    dead_sorted = sorted(t for t, s, _ in results if s == 'dead')

    write_result_file(ut.ALIVE_FILE, alive_sorted,
                      'Trackers that PASSED the liveness test')
    write_result_file(ut.DEAD_FILE, dead_sorted,
                      'Trackers that FAILED the liveness test')
    write_report(results, elapsed)

    n_alive = len(alive_sorted)
    n_dead = len(dead_sorted)
    n_skip = sum(1 for _, s, _ in results if s == 'untestable')

    print(f'\n===== Test Summary =====')
    print(f'  Total: {len(trackers)}')
    print(f'  Alive: {n_alive}')
    print(f'  Dead:  {n_dead}')
    print(f'  Untestable: {n_skip}')
    print(f'  Time:  {elapsed:.1f}s')
    print('=========================')

    repo = ut.get_repo()
    page_stats = [
        (ut.ALIVE_FILE, n_alive),
        (ut.MERGED_FILE, len(trackers)),
        (ut.DEAD_FILE, n_dead),
    ]
    ut.generate_pages(repo, page_stats)
    print('[OK] Pages regenerated with alive statistics.')


if __name__ == '__main__':
    main()
