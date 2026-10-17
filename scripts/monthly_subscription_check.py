#!/usr/bin/env python3
"""月度订阅地址清单校验。

每月（或手动 workflow_dispatch）验证订阅地址的可用性与内容：
  - all  类地址：期望 条数 > 0
任一失败则退出码非 0，供 monthly-check.yml 判定失败。

地址清单覆盖：GitHub Raw / jsDelivr 直链。
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

CHECKS = [
    ("all Raw", "https://raw.githubusercontent.com/Pmwiu/Tracker-List/main/trackers/trackers_all.txt"),
    ("all jsDelivr 直链", "https://cdn.jsdelivr.net/gh/Pmwiu/Tracker-List@main/trackers/trackers_all.txt"),
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
    for name, url in CHECKS:
        try:
            body, status = fetch(url)
            count = count_trackers(body)
            if count <= 0:
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
