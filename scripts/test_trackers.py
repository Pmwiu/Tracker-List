#!/usr/bin/env python3
"""Tracker 活性测试 + 测速排序：安全过滤→协议探活+测速→按速度排序取前89"""
import os, sys, ssl, time, random, socket, struct, argparse, ipaddress
import urllib.parse, urllib.request, datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
import update_trackers as ut


def bdecode(data):
    def parse(i):
        c = data[i:i+1]
        if c == b'i':
            e = data.index(b'e', i); return int(data[i+1:e]), e+1
        if c == b'l':
            r = []; i += 1
            while data[i:i+1] != b'e':
                item, i = parse(i); r.append(item)
            return r, i+1
        if c == b'd':
            r = {}; i += 1
            while data[i:i+1] != b'e':
                k, i = parse(i); v, i = parse(i); r[k] = v
            return r, i+1
        colon = data.index(b':', i); l = int(data[i:colon]); s = colon+1
        return data[s:s+l], s+l
    obj, _ = parse(0); return obj


def make_identity():
    return os.urandom(20), b'-TT0200-' + os.urandom(12)


def encode_bytes(b):
    return ''.join('%%%02X' % x for x in b)


def is_safe_tracker(url):
    try:
        p = urllib.parse.urlparse(url)
    except Exception:
        return False, "unparseable"
    host = p.hostname
    if not host:
        return False, "no host"
    h = host.lower()
    if h in ('localhost',) or h.endswith('.local'):
        return False, "localhost"
    try:
        ip = ipaddress.ip_address(host)
        if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved:
            return False, f"private IP: {host}"
    except ValueError:
        try:
            for _, _, _, _, sa in socket.getaddrinfo(host, None):
                try:
                    ip = ipaddress.ip_address(sa[0])
                    if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved:
                        return False, f"resolves private: {sa[0]}"
                except ValueError:
                    continue
        except socket.gaierror:
            pass
    return True, "safe"


def test_http(url, timeout):
    ih, pid = make_identity()
    q = 'info_hash=' + encode_bytes(ih) + '&peer_id=' + encode_bytes(pid) + '&port=6881&uploaded=0&downloaded=0&left=1000000&compact=1&event=started'
    full = url + ('&' if '?' in url else '?') + q
    req = urllib.request.Request(full, headers={'User-Agent': 'TrackerBot/2.0'})
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = r.read()
    el = (time.time() - t0) * 1000
    if not data:
        return False, el, 'empty'
    try:
        d = bdecode(data)
    except Exception:
        return False, el, 'bad bencode'
    if not isinstance(d, dict):
        return False, el, 'not dict'
    if b'failure reason' in d or 'failure reason' in d:
        return True, el, 'online (failure)'
    return True, el, 'valid announce'


def test_udp(host, port, timeout):
    fam = socket.AF_INET6 if ':' in host else socket.AF_INET
    sock = socket.socket(fam, socket.SOCK_DGRAM)
    sock.settimeout(timeout)
    addr = (host, port)
    txn = random.randint(0, 0xFFFFFFFF)
    pkt = struct.pack('>QII', 0x41727101980, 0, txn)
    deadline = time.time() + timeout
    sent = False; data = None; t0 = time.time()
    while time.time() < deadline:
        if not sent:
            sock.sendto(pkt, addr); sent = True
        rem = deadline - time.time()
        if rem <= 0: break
        sock.settimeout(min(rem, max(rem/2, 1)))
        try:
            data, _ = sock.recvfrom(2048); break
        except socket.timeout:
            sent = False; continue
    else:
        data = None
    el = (time.time() - t0) * 1000
    if not data or len(data) < 16:
        sock.close(); return False, el, 'no response'
    act, rtx = struct.unpack('>II', data[:8])
    cid = struct.unpack('>Q', data[8:16])[0]
    if rtx != txn or act != 0:
        sock.close(); return False, el, 'bad response'
    try:
        ih, pid = make_identity()
        ap = struct.pack('>QII', cid, 1, txn) + ih + pid
        ap += struct.pack('>QQQ', 0, 1000000, 0)
        ap += struct.pack('>III', 0, 0, random.randint(0, 0xFFFFFFFF))
        ap += struct.pack('>iH', -1, 6881)
        sock.sendto(ap, addr)
        rem = deadline - time.time()
        if rem > 0:
            sock.settimeout(rem)
            try:
                ad, _ = sock.recvfrom(2048)
                if ad and len(ad) >= 8:
                    sock.close(); return True, el, 'connect+announce'
            except socket.timeout:
                pass
    except Exception:
        pass
    sock.close()
    return True, el, 'connect ok'


def test_wss(host, port, timeout):
    ctx = ssl.create_default_context()
    t0 = time.time()
    s = socket.create_connection((host, port), timeout=timeout)
    try:
        ss = ctx.wrap_socket(s, server_hostname=host); ss.close()
    except Exception:
        s.close(); raise
    return True, (time.time()-t0)*1000, 'TLS ok'


def test_one(tracker, timeout):
    safe, reason = is_safe_tracker(tracker)
    if not safe:
        return tracker, 'unsafe', reason, 0.0
    try:
        p = urllib.parse.urlparse(tracker)
    except Exception:
        return tracker, 'dead', 'unparseable', 0.0
    scheme = p.scheme.lower(); host = p.hostname; port = p.port
    if host and host.endswith('.i2p'):
        return tracker, 'untestable', 'I2P', 0.0
    try:
        if scheme in ('http', 'https'):
            ok, el, d = test_http(tracker, timeout)
            return tracker, 'alive' if ok else 'dead', d, el
        if scheme == 'udp':
            if port is None: port = 6969
            ok, el, d = test_udp(host, port, timeout)
            return tracker, 'alive' if ok else 'dead', d, el
        if scheme in ('wss', 'ws'):
            if port is None: port = 443 if scheme == 'wss' else 80
            if scheme == 'wss':
                ok, el, d = test_wss(host, port, timeout)
            else:
                t0 = time.time(); s = socket.create_connection((host, port), timeout=timeout); s.close()
                ok, el, d = True, (time.time()-t0)*1000, 'TCP ok'
            return tracker, 'alive' if ok else 'dead', d, el
        return tracker, 'untestable', f'unknown: {scheme}', 0.0
    except socket.timeout:
        return tracker, 'dead', 'timeout', float(timeout*1000)
    except ConnectionRefusedError:
        return tracker, 'dead', 'refused', 0.0
    except socket.gaierror:
        return tracker, 'dead', 'DNS fail', 0.0
    except Exception as e:
        return tracker, 'dead', f'{type(e).__name__}: {e}', 0.0


def read_merged():
    path = os.path.join(ut.OUTPUT_DIR, ut.MERGED_FILE)
    with open(path, 'r', encoding='utf-8') as f:
        return [l.strip() for l in f if l.strip() and not l.strip().startswith('#')]


def write_result_file(filename, trackers, desc):
    now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
    h = ['# Auto-generated by test_trackers.py', f'# Last tested: {now} UTC', f'# {desc}', f'# Total: {len(trackers)}', '']
    with open(os.path.join(ut.OUTPUT_DIR, filename), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(h) + '\n'.join(trackers) + ('\n' if trackers else ''))


def write_report(results, alive_sorted, capped, elapsed):
    alive = [(t,d,e) for t,s,d,e in results if s=='alive']
    dead = [(t,d,e) for t,s,d,e in results if s=='dead']
    unsafe = [(t,d,e) for t,s,d,e in results if s=='unsafe']
    total = len(results)
    now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    lines = ['# Tracker 活性+测速报告', '', f'- 时间: {now}', f'- 总数: {total}',
             f'- 存活: {len(alive)}', f'- 失效: {len(dead)}', f'- 不安全: {len(unsafe)}',
             f'- 速度排序保留前{ut.MAX_TRACKERS}, 淘汰{len(capped)}', f'- 耗时: {elapsed:.1f}s', '',
             '## 存活（按速度升序）', '']
    for rank, (t,d,e) in enumerate(alive_sorted, 1):
        mark = ' [OUT]' if rank > ut.MAX_TRACKERS else ''
        lines.append(f'{rank}. `{t}` — {e:.0f}ms — {d}{mark}')
    if dead: lines += ['', '## 失效', ''] + [f'- `{t}` — {d}' for t,d,e in sorted(dead)]
    if unsafe: lines += ['', '## 不安全（已过滤）', ''] + [f'- `{t}` — {d}' for t,d,e in sorted(unsafe)]
    with open(os.path.join(ut.OUTPUT_DIR, 'test_report.md'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--timeout', type=int, default=12)
    ap.add_argument('--workers', type=int, default=25)
    args = ap.parse_args()
    trackers = read_merged()
    print(f'[INFO] Testing {len(trackers)} (timeout={args.timeout}s, workers={args.workers}), max={ut.MAX_TRACKERS}')
    results = []; t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futs = {pool.submit(test_one, t, args.timeout): t for t in trackers}
        done = 0
        for f in as_completed(futs):
            t, s, d, e = f.result(); results.append((t,s,d,e)); done += 1
            mk = {'alive':'[ALIVE]','dead':'[DEAD] ','untestable':'[SKIP]  ','unsafe':'[BLOCK]'}[s]
            sp = f' {e:.0f}ms' if s=='alive' else ''
            print(f'  {mk} ({done}/{len(trackers)}) {t}{sp} — {d}')
    elapsed = time.time() - t0
    alive_ws = [(t,d,e) for t,s,d,e in results if s=='alive']
    alive_sorted = sorted(alive_ws, key=lambda x: x[2])
    alive_final = [t for t,d,e in alive_sorted[:ut.MAX_TRACKERS]]
    capped = [(t,d,e) for t,d,e in alive_sorted[ut.MAX_TRACKERS:]]
    dead_final = sorted([t for t,s,d,e in results if s in ('dead','unsafe')] + [t for t,d,e in capped])
    write_result_file(ut.ALIVE_FILE, alive_final, f'PASSED liveness, speed-sorted, top {ut.MAX_TRACKERS}')
    write_result_file(ut.DEAD_FILE, dead_final, 'FAILED/unsafe/speed-capped')
    write_report(results, alive_sorted, capped, elapsed)
    na = len(alive_final); nd = len(dead_final); nc = len(capped); nu = sum(1 for _,s,_,_ in results if s=='unsafe')
    print(f'\n===== Summary =====')
    print(f'  Total: {len(trackers)}  Alive(raw): {len(alive_ws)}  Alive(final): {na}  Capped: {nc}  Unsafe: {nu}  Dead: {nd}')
    print(f'  Time: {elapsed:.1f}s')
    print('===================')
    repo = ut.get_repo()
    ut.generate_pages(repo, [(ut.ALIVE_FILE, na), (ut.MERGED_FILE, len(trackers)), (ut.DEAD_FILE, nd)])
    ut.sync_plain_text_files()
    print('[OK] Done.')


if __name__ == '__main__':
    main()
