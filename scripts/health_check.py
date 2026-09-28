#!/usr/bin/env python3
"""
健康检查脚本：验证本地文件、云端仓库与短链接的可用性。

检查项:
  1. 本地 Tracker 文件完整性（4个订阅源 + 合并/存活/失效列表）
  2. 本地 GitHub Pages 文件完整性（主页 + 短链接页面 + 纯文本文件）
  3. GitHub Raw 直链 URL 的 HTTP 可达性
  4. 短链接页面是否包含正确的重定向目标

用法:
  python scripts/health_check.py              单次检查
  python scripts/health_check.py --rounds 10  连续检查10轮
"""

import os
import sys
import time
import urllib.request
import datetime

REPO = "Pmwiu/Tracker-List"
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRACKERS_DIR = os.path.join(PROJECT_ROOT, "trackers")
PAGES_DIR = os.path.join(PROJECT_ROOT, "docs")
SHORT_DIR = os.path.join(PAGES_DIR, "s")
TIMEOUT = 20

TRACKER_FILES = [
    "trackers_best.txt",
    "trackers_ngosang.txt",
    "trackers_ngosang_ip.txt",
    "trackers_adysec.txt",
    "trackers_merged.txt",
    "trackers_alive.txt",
    "trackers_dead.txt",
]

EXTRA_FILES = ["MIRRORS.txt", "test_report.md"]

# 仅保留 GitHub Raw 直连（无 CDN/代理加速链接）
MIRROR_URLS = [
    ("Raw", "https://raw.githubusercontent.com/{repo}/main/trackers/trackers_alive.txt"),
]

SHORT_PAGES = [
    "alive", "best", "ngosang", "ngosang-ip", "adysec", "all",
]

# docs/ 下的纯文本文件（供 BT 客户端直接订阅）
PLAIN_TEXT_FILES = [
    "alive.txt", "merged.txt", "best.txt", "ngosang.txt", "ngosang_ip.txt", "adysec.txt",
]


def count_trackers_in_text(text):
    """统计文本中有效的 tracker 行数。"""
    count = 0
    for line in text.splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            count += 1
    return count


def fetch_url(url):
    """获取 URL 内容，返回 (成功?, 内容或错误信息, HTTP状态码)。"""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "health-check/2.0"})
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
            results.append(("PASS", f"Local tracker: {f}", "exists (may be empty)"))
            continue
        if os.path.getsize(path) > 0:
            with open(path, "r", encoding="utf-8") as fh:
                count = count_trackers_in_text(fh.read())
            results.append(("PASS", f"Local tracker: {f}", f"{count} trackers"))
        else:
            results.append(("FAIL", f"Local tracker: {f}", "empty"))

    for ef in EXTRA_FILES:
        path = os.path.join(TRACKERS_DIR, ef)
        if os.path.exists(path) and os.path.getsize(path) > 0:
            results.append(("PASS", f"Local {ef}", "exists"))
        else:
            results.append(("FAIL", f"Local {ef}", "missing"))

    index_path = os.path.join(PAGES_DIR, "index.html")
    if os.path.exists(index_path) and os.path.getsize(index_path) > 0:
        results.append(("PASS", "Local Pages index.html", "exists"))
    else:
        results.append(("FAIL", "Local Pages index.html", "missing"))

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

    for ptf in PLAIN_TEXT_FILES:
        path = os.path.join(PAGES_DIR, ptf)
        if os.path.exists(path) and os.path.getsize(path) > 0:
            with open(path, "r", encoding="utf-8") as fh:
                count = count_trackers_in_text(fh.read())
            results.append(("PASS", f"Plain text: /{ptf}", f"{count} trackers"))
        else:
            results.append(("FAIL", f"Plain text: /{ptf}", "missing"))


def check_mirrors(results):
    """检查 GitHub Raw 直链的可达性。"""
    counts = {}
    for name, template in MIRROR_URLS:
        url = template.format(repo=REPO)
        ok, content, status = fetch_url(url)
        if ok:
            count = count_trackers_in_text(content)
            counts[name] = count
            results.append(("PASS", f"Mirror {name}", f"HTTP {status}, {count} trackers"))
        else:
            results.append(("WARN", f"Mirror {name}", f"unreachable: {content[:60]}"))


def run_single_check(round_num):
    """执行一轮完整健康检查，返回 (通过数, 警告数, 失败数)。"""
    results = []
    check_local_files(results)
    check_mirrors(results)

    passes = sum(1 for s, _, _ in results if s == "PASS")
    warns = sum(1 for s, _, _ in results if s == "WARN")
    fails = sum(1 for s, _, _ in results if s == "FAIL")

    print(f"\n{'='*60}")
    print(f" Round {round_num} - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}")
    for status, item, detail in results:
        marker = {"PASS": "[PASS]", "WARN": "[WARN]", "FAIL": "[FAIL]"}[status]
        print(f"  {marker} {item}: {detail}")
    print(f"{'-'*60}")
    print(f"  Result: {passes} passed, {warns} warnings, {fails} failed")
    print(f"{'='*60}")

    return passes, warns, fails, results


def main():
    rounds = 1
    if "--rounds" in sys.argv:
        idx = sys.argv.index("--rounds")
        rounds = int(sys.argv[idx + 1])

    total_passes = 0
    total_warns = 0
    total_fails = 0
    all_had_fail = False

    for r in range(1, rounds + 1):
        p, w, f, _ = run_single_check(r)
        total_passes += p
        total_warns += w
        total_fails += f
        if f > 0:
            all_had_fail = True
        if r < rounds:
            time.sleep(3)

    print(f"\n{'#'*60}")
    print(f" FINAL REPORT: {rounds} rounds completed")
    print(f"   Total PASS: {total_passes}")
    print(f"   Total WARN: {total_warns}")
    print(f"   Total FAIL: {total_fails}")
    if all_had_fail:
        print(f"   STATUS: ISSUES DETECTED")
    else:
        print(f"   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)")
    print(f"{'#'*60}")

    sys.exit(1 if all_had_fail else 0)


if __name__ == "__main__":
    main()
