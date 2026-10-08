#!/usr/bin/env python3
"""月度订阅地址清单校验。

每月（或手动 workflow_dispatch）验证 5 类订阅地址的可用性与内容：
  - best 类地址：期望 1 <= 条数 <= MAX_TRACKERS
  - all  类地址：期望 条数 > 0
任一失败则退出码非 0，供 monthly-check.yml 判定失败。

地址清单覆盖：Worker 短链接 / jsDelivr 加速 / GitHub Pages / GitHub Raw / jsDelivr 直链。
"""

import os
import sys
import urllib.request
import urllib.error

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
import update_trackers as ut

TIMEOUT = 20
USER_AGENT = "monthly-subscription-check/1.0"
BEST_MAX = ut.MAX_TRACKERS

CHECKS = [
    ("best 短链接 (Worker)", "https://tracker.pmwiu.com/best.txt", "best"),
    ("best 加速 (jsDelivr)", "https://tracker.pmwiu.com/jsd/best.txt", "best"),
    ("all 短链接 (Worker)", "https://tracker.pmwiu.com/all.txt", "all"),
    ("all 加速 (jsDelivr)", "https://tracker.pmwiu.com/jsd/all.txt", "all"),
    ("best Pages 直链", "https://pmwiu.github.io/Tracker-List/alive.txt", "best"),
    ("all Pages 直链", "https://pmwiu.github.io/Tracker-List/all.txt", "all"),
    ("best Raw", "https://raw.githubusercontent.com/Pmwiu/Tracker-List/main/trackers/trackers_alive.txt", "best"),
    ("all Raw", "https://raw.githubusercontent.com/Pmwiu/Tracker-List/main/trackers/trackers_all.txt", "all"),
    ("best jsDelivr 直链", "https://cdn.jsdelivr.net/gh/Pmwiu/Tracker-List@main/trackers/trackers_alive.txt", "best"),
    ("all jsDelivr 直链", "https://cdn.jsdelivr.net/gh/Pmwiu/Tracker-List@main/trackers/trackers_all.txt", "all"),
]


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.read().decode("utf-8", errors="replace"), resp.status


def count_trackers(text):
    return sum(1 for line in text.splitlines()
               if line.strip() and not line.strip().startswith("#"))


def main():
    if not ut.SOURCES:
        print("订阅源为空（SOURCES = []），月度订阅地址清单校验跳过。")
        return 0

    fails = 0
    print("=" * 60)
    print(" 月度订阅地址清单校验")
    print("=" * 60)
    for name, url, kind in CHECKS:
        try:
            body, status = fetch(url)
            count = count_trackers(body)
            if kind == "best" and not (0 < count <= BEST_MAX):
                print(f"[FAIL] {name}: HTTP {status}, {count} 条 (期望 1..{BEST_MAX})")
                fails += 1
            elif kind == "all" and count <= 0:
                print(f"[FAIL] {name}: HTTP {status}, {count} 条 (期望 > 0)")
                fails += 1
            else:
                print(f"[PASS] {name}: HTTP {status}, {count} 条")
        except Exception as e:
            print(f"[FAIL] {name}: {e}")
            fails += 1
    print("-" * 60)
    print(f" 结果: {len(CHECKS) - fails}/{len(CHECKS)} 通过")
    print("=" * 60)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
