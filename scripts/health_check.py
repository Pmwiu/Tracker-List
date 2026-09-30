#!/usr/bin/env python3
"""
健康检查脚本 v3.0：验证本地文件、云端仓库与短链接的可用性。

检查项:
  1. 本地 Tracker 文件完整性（3个订阅源 + 合并/存活/失效列表）
  2. 本地 GitHub Pages 文件完整性（主页 + 短链接页面 + 纯文本文件）
  3. alive.txt 数量校验（0 <= count <= MAX_ALIVE）
  4. merged.txt 去重校验（无重复）
  5. 内容一致性校验（trackers/ vs docs/ 纯文本文件一致）
  6. GitHub Raw 直链 URL 的 HTTP 可达性
  7. GitHub Pages 短链接页面可达性
  8. Tracker URL 格式校验

用法:
  python scripts/health_check.py              单次检查
  python scripts/health_check.py --rounds 5   连续检查5轮
  python scripts/health_check.py --skip-net   跳过网络检查（仅本地）
"""

import os
import re
import sys
import time
import json
import urllib.request
import urllib.error
import datetime

REPO = "Pmwiu/Tracker-List"
OWNER = REPO.split("/")[0]
REPO_NAME = REPO.split("/")[-1]
PAGES_BASE = f"https://{OWNER}.github.io/{REPO_NAME}"
RAW_BASE = f"https://raw.githubusercontent.com/{REPO}/main"

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRACKERS_DIR = os.path.join(PROJECT_ROOT, "trackers")
PAGES_DIR = os.path.join(PROJECT_ROOT, "docs")
SHORT_DIR = os.path.join(PAGES_DIR, "s")
TIMEOUT = 15

TRACKER_FILES = [
    "trackers_cf_best.txt",
    "trackers_ngosang_ip.txt",
    "trackers_adysec_best.txt",
    "trackers_adysec_http.txt",
    "trackers_adysec_https.txt",
    "trackers_adysec_udp.txt",
    "trackers_adysec_wss.txt",
    "trackers_anime_best.txt",
    "trackers_anime_ip.txt",
    "trackers_ultimate.txt",
    "trackers_opentracker.txt",
    "trackers_ngosang_best.txt",
    "trackers_ngosang_i2p.txt",
    "trackers_ngosang_ygg.txt",
    "trackers_ngosang_all_ip.txt",
    "trackers_ngosang_ygg_ip.txt",
    "trackers_merged.txt",
    "trackers_alive.txt",
    "trackers_dead.txt",
]

EXTRA_FILES = ["MIRRORS.txt", "test_report.md", "test_state.json"]

SHORT_PAGES = [
    "alive", "all",
]

PLAIN_TEXT_FILES = [
    "alive.txt", "merged.txt",
    "cf_best.txt", "ngosang_ip.txt", "adysec_best.txt", "adysec_http.txt",
    "adysec_https.txt", "adysec_udp.txt", "adysec_wss.txt", "anime_best.txt",
    "anime_ip.txt", "ultimate.txt", "opentracker.txt",
    "ngosang_best.txt", "ngosang_i2p.txt", "ngosang_ygg.txt",
    "ngosang_all_ip.txt", "ngosang_ygg_ip.txt",
]

# trackers/ 到 docs/ 的映射
CONSISTENCY_MAP = {
    "trackers_alive.txt": "alive.txt",
    "trackers_merged.txt": "merged.txt",
    "trackers_cf_best.txt": "cf_best.txt",
    "trackers_ngosang_ip.txt": "ngosang_ip.txt",
    "trackers_adysec_best.txt": "adysec_best.txt",
    "trackers_adysec_http.txt": "adysec_http.txt",
    "trackers_adysec_https.txt": "adysec_https.txt",
    "trackers_adysec_udp.txt": "adysec_udp.txt",
    "trackers_adysec_wss.txt": "adysec_wss.txt",
    "trackers_anime_best.txt": "anime_best.txt",
    "trackers_anime_ip.txt": "anime_ip.txt",
    "trackers_ultimate.txt": "ultimate.txt",
    "trackers_opentracker.txt": "opentracker.txt",
    "trackers_ngosang_best.txt": "ngosang_best.txt",
    "trackers_ngosang_i2p.txt": "ngosang_i2p.txt",
    "trackers_ngosang_ygg.txt": "ngosang_ygg.txt",
    "trackers_ngosang_all_ip.txt": "ngosang_all_ip.txt",
    "trackers_ngosang_ygg_ip.txt": "ngosang_ygg_ip.txt",
}

MAX_ALIVE = 59
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports")
HEALTH_FILE = os.path.join(REPORTS_DIR, "health.json")
TRACKER_PATTERN = re.compile(r'^(udp|http|https|wss|ws)://[^\s/$.?#].[^\s]*$', re.IGNORECASE)


def count_trackers_in_text(text):
    count = 0
    for line in text.splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            count += 1
    return count


def extract_trackers(text):
    """提取文本中的 tracker 行（去注释、去空行）。"""
    return [line.strip() for line in text.splitlines()
            if line.strip() and not line.strip().startswith("#")]


def fetch_url(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "health-check/3.0"})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return True, resp.read().decode("utf-8", errors="replace"), resp.status
    except urllib.error.HTTPError as e:
        return False, str(e), e.code
    except Exception as e:
        return False, str(e), 0


def check_local_files(results):
    """检查本地文件完整性。"""
    for f in TRACKER_FILES:
        path = os.path.join(TRACKERS_DIR, f)
        if not os.path.exists(path):
            results.append(("FAIL", f"Local tracker: {f}", "missing"))
            continue
        if f == "trackers_dead.txt":
            results.append(("PASS", f"Local tracker: {f}", "exists"))
            continue
        if os.path.getsize(path) > 0:
            with open(path, "r", encoding="utf-8") as fh:
                content = fh.read()
            count = count_trackers_in_text(content)
            if count == 0:
                results.append(("FAIL", f"Local tracker: {f}", "no valid trackers"))
            else:
                results.append(("PASS", f"Local tracker: {f}", f"{count} trackers"))
        else:
            results.append(("FAIL", f"Local tracker: {f}", "empty"))

    for ef in EXTRA_FILES:
        path = os.path.join(TRACKERS_DIR, ef)
        if os.path.exists(path) and os.path.getsize(path) > 0:
            results.append(("PASS", f"Local {ef}", "exists"))
        else:
            if ef == "test_state.json":
                results.append(("WARN", f"Local {ef}", "missing (first run?)"))
            else:
                results.append(("FAIL", f"Local {ef}", "missing"))

    # index.html
    index_path = os.path.join(PAGES_DIR, "index.html")
    if os.path.exists(index_path) and os.path.getsize(index_path) > 0:
        results.append(("PASS", "Local Pages index.html", "exists"))
    else:
        results.append(("FAIL", "Local Pages index.html", "missing"))

    # 短链接页面
    for sp in SHORT_PAGES:
        path = os.path.join(SHORT_DIR, f"{sp}.html")
        if os.path.exists(path) and os.path.getsize(path) > 0:
            with open(path, "r", encoding="utf-8") as fh:
                content = fh.read()
            if 'http' in content and ('refresh' in content or 'location' in content):
                results.append(("PASS", f"Local short page: /s/{sp}", "valid redirect"))
            else:
                results.append(("FAIL", f"Local short page: /s/{sp}", "invalid content"))
        else:
            results.append(("FAIL", f"Local short page: /s/{sp}", "missing"))

    # 纯文本文件
    for ptf in PLAIN_TEXT_FILES:
        path = os.path.join(PAGES_DIR, ptf)
        if os.path.exists(path) and os.path.getsize(path) > 0:
            with open(path, "r", encoding="utf-8") as fh:
                count = count_trackers_in_text(fh.read())
            results.append(("PASS", f"Plain text: /{ptf}", f"{count} trackers"))
        else:
            results.append(("FAIL", f"Plain text: /{ptf}", "missing"))


def check_alive_count(results):
    """校验 alive.txt 数量在 [0, MAX_ALIVE] 区间内。"""
    path = os.path.join(TRACKERS_DIR, "trackers_alive.txt")
    if not os.path.exists(path):
        results.append(("FAIL", "Alive count check", "file missing"))
        return
    with open(path, "r", encoding="utf-8") as f:
        count = count_trackers_in_text(f.read())
    if 0 <= count <= MAX_ALIVE:
        results.append(("PASS", "Alive count check", f"{count} in [0, {MAX_ALIVE}]"))
    else:
        results.append(("FAIL", "Alive count check", f"{count} out of [0, {MAX_ALIVE}]"))


def check_merged_dedup(results):
    """校验 merged.txt 无重复。"""
    path = os.path.join(TRACKERS_DIR, "trackers_merged.txt")
    if not os.path.exists(path):
        results.append(("FAIL", "Merged dedup check", "file missing"))
        return
    with open(path, "r", encoding="utf-8") as f:
        trackers = extract_trackers(f.read())
    unique = set(trackers)
    if len(trackers) == len(unique):
        results.append(("PASS", "Merged dedup check", f"{len(trackers)} unique"))
    else:
        dupes = len(trackers) - len(unique)
        results.append(("FAIL", "Merged dedup check", f"{dupes} duplicates found"))


def check_consistency(results):
    """校验 trackers/ 与 docs/ 纯文本文件内容一致。"""
    for src, dst in CONSISTENCY_MAP.items():
        src_path = os.path.join(TRACKERS_DIR, src)
        dst_path = os.path.join(PAGES_DIR, dst)
        if not os.path.exists(src_path) or not os.path.exists(dst_path):
            results.append(("WARN", f"Consistency: {src} vs {dst}", "one side missing"))
            continue
        with open(src_path, "r", encoding="utf-8") as f:
            src_trackers = set(extract_trackers(f.read()))
        with open(dst_path, "r", encoding="utf-8") as f:
            dst_trackers = set(extract_trackers(f.read()))
        if src_trackers == dst_trackers:
            results.append(("PASS", f"Consistency: {src} vs {dst}", "identical"))
        else:
            diff = len(src_trackers.symmetric_difference(dst_trackers))
            results.append(("FAIL", f"Consistency: {src} vs {dst}", f"{diff} differing entries"))


def check_url_format(results):
    """校验 merged.txt 中所有 tracker URL 格式合法。"""
    path = os.path.join(TRACKERS_DIR, "trackers_merged.txt")
    if not os.path.exists(path):
        results.append(("FAIL", "URL format check", "file missing"))
        return
    with open(path, "r", encoding="utf-8") as f:
        trackers = extract_trackers(f.read())
    invalid = [t for t in trackers if not TRACKER_PATTERN.match(t)]
    if not invalid:
        results.append(("PASS", "URL format check", f"all {len(trackers)} valid"))
    else:
        results.append(("FAIL", "URL format check", f"{len(invalid)} invalid URLs"))


def check_raw_mirrors(results):
    """检查 GitHub Raw 直链可达性，并校验 alive ≤ MAX_ALIVE、merged 非空。"""
    urls = [
        ("alive (Raw)", f"{RAW_BASE}/trackers/trackers_alive.txt", "alive"),
        ("merged (Raw)", f"{RAW_BASE}/trackers/trackers_merged.txt", "merged"),
    ]
    for name, url, kind in urls:
        ok, content, status = fetch_url(url)
        if ok:
            count = count_trackers_in_text(content)
            if kind == "alive" and count > MAX_ALIVE:
                results.append(("FAIL", f"Raw: {name}", f"{count} > {MAX_ALIVE}"))
            elif kind == "merged" and count <= 0:
                results.append(("FAIL", f"Raw: {name}", f"{count} trackers (empty)"))
            else:
                results.append(("PASS", f"Raw: {name}", f"HTTP {status}, {count} trackers"))
        else:
            results.append(("WARN", f"Raw: {name}", f"unreachable: {content[:80]}"))


def check_pages_links(results):
    """检查 GitHub Pages 短链接和纯文本可达性。"""
    # 纯文本直链
    for ptf in ["alive.txt", "merged.txt"]:
        url = f"{PAGES_BASE}/{ptf}"
        ok, content, status = fetch_url(url)
        if ok:
            count = count_trackers_in_text(content)
            results.append(("PASS", f"Pages: /{ptf}", f"HTTP {status}, {count} trackers"))
        else:
            results.append(("WARN", f"Pages: /{ptf}", f"unreachable: {content[:80]}"))

    # 短链接页面（检查是否返回 200 且包含重定向）
    for sp in ["alive", "cf"]:
        url = f"{PAGES_BASE}/s/{sp}"
        ok, content, status = fetch_url(url)
        if ok and ('refresh' in content or 'location.replace' in content):
            results.append(("PASS", f"Pages short: /s/{sp}", f"HTTP {status}, redirect OK"))
        elif ok:
            results.append(("WARN", f"Pages short: /s/{sp}", f"HTTP {status} but no redirect found"))
        else:
            results.append(("WARN", f"Pages short: /s/{sp}", f"unreachable: {content[:80]}"))


def run_single_check(round_num, skip_net=False):
    results = []
    check_local_files(results)
    check_alive_count(results)
    check_merged_dedup(results)
    check_consistency(results)
    check_url_format(results)
    if not skip_net:
        check_raw_mirrors(results)
        check_pages_links(results)

    passes = sum(1 for s, _, _ in results if s == "PASS")
    warns = sum(1 for s, _, _ in results if s == "WARN")
    fails = sum(1 for s, _, _ in results if s == "FAIL")

    print(f"{chr(10)}{'='*60}")
    print(f" Round {round_num} - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}")
    for status, item, detail in results:
        marker = {"PASS": "[PASS]", "WARN": "[WARN]", "FAIL": "[FAIL]"}[status]
        print(f"  {marker} {item}: {detail}")
    print(f"{'-'*60}")
    print(f"  Result: {passes} passed, {warns} warnings, {fails} failed")
    print(f"{'='*60}")

    return passes, warns, fails, results


def write_health_json(rounds, total_passes, total_warns, total_fails):
    """生成 reports/health.json 健康检查结果。"""
    os.makedirs(REPORTS_DIR, exist_ok=True)
    data = {
        "timestamp": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "rounds": rounds,
        "pass": total_passes,
        "warn": total_warns,
        "fail": total_fails,
        "status": "healthy" if total_fails == 0 else "issues",
    }
    try:
        with open(HEALTH_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write("\n")
    except OSError as e:
        print(f"[WARN]  Failed to write {HEALTH_FILE}: {e}")


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--rounds', type=int, default=1)
    parser.add_argument('--skip-net', action='store_true')
    parser.add_argument('--interval', type=int, default=3, help='seconds between rounds')
    args = parser.parse_args()

    total_passes = 0
    total_warns = 0
    total_fails = 0
    all_had_fail = False

    for r in range(1, args.rounds + 1):
        p, w, f, _ = run_single_check(r, skip_net=args.skip_net)
        total_passes += p
        total_warns += w
        total_fails += f
        if f > 0:
            all_had_fail = True
        if r < args.rounds:
            time.sleep(args.interval)

    print(f"{chr(10)}{'#'*60}")
    print(f" FINAL REPORT: {args.rounds} rounds completed")
    print(f"   Total PASS: {total_passes}")
    print(f"   Total WARN: {total_warns}")
    print(f"   Total FAIL: {total_fails}")
    if all_had_fail:
        print(f"   STATUS: ISSUES DETECTED")
    else:
        print(f"   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)")
    print(f"{'#'*60}")

    write_health_json(args.rounds, total_passes, total_warns, total_fails)

    sys.exit(1 if all_had_fail else 0)


if __name__ == "__main__":
    main()
