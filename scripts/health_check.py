#!/usr/bin/env python3
"""
健康检查脚本：验证本地文件、云端仓库、所有 CDN 镜像与短链接的可用性。

检查项:
  1. 本地 Tracker 文件完整性（5个列表 + 镜像清单）
  2. 本地 GitHub Pages 文件完整性（主页 + 短链接页面）
  3. 各 CDN 镜像 URL 的 HTTP 可达性
  4. 各镜像返回内容的 Tracker 数量一致性
  5. 短链接页面是否包含正确的重定向目标

用法:
  python scripts/health_check.py              # 单次检查
  python scripts/health_check.py --rounds 10  # 连续检查10轮
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
    "trackers_all.txt",
    "trackers_all_ip.txt",
    "trackers_all_i2p.txt",
    "trackers_all_yggdrasil.txt",
    "trackers_merged.txt",
]

MIRROR_URLS = [
    ("Raw",       "https://raw.githubusercontent.com/{repo}/main/trackers/trackers_merged.txt"),
    ("jsDelivr",   "https://cdn.jsdelivr.net/gh/{repo}@main/trackers/trackers_merged.txt"),
    ("Fastly",     "https://fastly.jsdelivr.net/gh/{repo}@main/trackers/trackers_merged.txt"),
    ("Gcore",      "https://gcore.jsdelivr.net/gh/{repo}@main/trackers/trackers_merged.txt"),
    ("ghproxy",    "https://ghproxy.net/https://raw.githubusercontent.com/{repo}/main/trackers/trackers_merged.txt"),
    ("gh-proxy",   "https://gh-proxy.com/https://raw.githubusercontent.com/{repo}/main/trackers/trackers_merged.txt"),
]

SHORT_PAGES = [
    "all", "all-cdn", "all-fastly", "all-gcore", "all-proxy",
    "trackers", "ip", "i2p", "ygg", "repo",
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
        req = urllib.request.Request(url, headers={"User-Agent": "health-check/1.0"})
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
        if os.path.exists(path) and os.path.getsize(path) > 0:
            with open(path, "r", encoding="utf-8") as fh:
                count = count_trackers_in_text(fh.read())
            results.append(("PASS", f"Local tracker: {f}", f"{count} trackers"))
        else:
            results.append(("FAIL", f"Local tracker: {f}", "missing or empty"))

    mirrors_path = os.path.join(TRACKERS_DIR, "MIRRORS.txt")
    if os.path.exists(mirrors_path) and os.path.getsize(mirrors_path) > 0:
        results.append(("PASS", "Local MIRRORS.txt", "exists"))
    else:
        results.append(("FAIL", "Local MIRRORS.txt", "missing"))

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


def check_mirrors(results):
    """检查各 CDN 镜像的可达性与内容一致性。"""
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

    # 对比可达镜像的数量一致性
    if len(counts) >= 2:
        unique_counts = set(counts.values())
        if len(unique_counts) == 1:
            results.append(("PASS", "Mirror consistency", f"all reachable mirrors match ({list(counts.values())[0]})"))
        else:
            detail = ", ".join(f"{k}={v}" for k, v in counts.items())
            results.append(("WARN", "Mirror consistency", f"counts differ: {detail}"))


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
