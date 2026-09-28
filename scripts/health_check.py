#!/usr/bin/env python3
"""健康检查：本地文件完整性 + Raw直链可达性 + 短链接验证"""
import os, sys, time, urllib.request, datetime

REPO = "Pmwiu/Tracker-List"
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRACKERS_DIR = os.path.join(PROJECT_ROOT, "trackers")
PAGES_DIR = os.path.join(PROJECT_ROOT, "docs")
SHORT_DIR = os.path.join(PAGES_DIR, "s")
TIMEOUT = 20

TRACKER_FILES = ["trackers_best.txt", "trackers_ngosang.txt", "trackers_adysec.txt",
                 "trackers_merged.txt", "trackers_alive.txt", "trackers_dead.txt"]
EXTRA_FILES = ["MIRRORS.txt", "test_report.md"]
MIRROR_URLS = [("Raw", "https://raw.githubusercontent.com/{repo}/main/trackers/trackers_alive.txt")]
SHORT_PAGES = ["alive", "best", "ngosang", "adysec", "all", "repo"]
PLAIN_TEXT_FILES = ["alive.txt", "merged.txt", "best.txt", "ngosang.txt", "adysec.txt"]


def count_trackers(text):
    return sum(1 for l in text.splitlines() if l.strip() and not l.strip().startswith("#"))


def fetch_url(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "hc/2.0"})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return True, r.read().decode("utf-8", errors="replace"), r.status
    except urllib.error.HTTPError as e:
        return False, str(e), e.code
    except Exception as e:
        return False, str(e), 0


def check_local(results):
    for f in TRACKER_FILES:
        p = os.path.join(TRACKERS_DIR, f)
        if not os.path.exists(p):
            results.append(("FAIL", f"{f}", "missing")); continue
        if f == "trackers_dead.txt":
            results.append(("PASS", f"{f}", "exists")); continue
        if os.path.getsize(p) > 0:
            with open(p, "r", encoding="utf-8") as fh:
                results.append(("PASS", f"{f}", f"{count_trackers(fh.read())} trackers"))
        else:
            results.append(("FAIL", f"{f}", "empty"))
    for ef in EXTRA_FILES:
        p = os.path.join(TRACKERS_DIR, ef)
        results.append(("PASS" if os.path.exists(p) and os.path.getsize(p)>0 else "FAIL", ef, "exists" if os.path.exists(p) else "missing"))
    ip = os.path.join(PAGES_DIR, "index.html")
    results.append(("PASS" if os.path.exists(ip) and os.path.getsize(ip)>0 else "FAIL", "index.html", "exists"))
    for sp in SHORT_PAGES:
        p = os.path.join(SHORT_DIR, f"{sp}.html")
        if os.path.exists(p) and os.path.getsize(p)>0:
            with open(p, "r", encoding="utf-8") as fh:
                c = fh.read()
            results.append(("PASS" if 'http' in c and ('refresh' in c or 'location' in c) else "FAIL", f"/s/{sp}", "redirect"))
        else:
            results.append(("FAIL", f"/s/{sp}", "missing"))
    for ptf in PLAIN_TEXT_FILES:
        p = os.path.join(PAGES_DIR, ptf)
        if os.path.exists(p) and os.path.getsize(p)>0:
            with open(p, "r", encoding="utf-8") as fh:
                results.append(("PASS", f"/{ptf}", f"{count_trackers(fh.read())} trackers"))
        else:
            results.append(("FAIL", f"/{ptf}", "missing"))


def check_mirrors(results):
    for name, tmpl in MIRROR_URLS:
        url = tmpl.format(repo=REPO)
        ok, content, status = fetch_url(url)
        if ok:
            results.append(("PASS", f"Mirror {name}", f"HTTP {status}, {count_trackers(content)} trackers"))
        else:
            results.append(("WARN", f"Mirror {name}", f"unreachable: {content[:60]}"))


def run_round(n):
    results = []; check_local(results); check_mirrors(results)
    p = sum(1 for s,_,_ in results if s=="PASS")
    w = sum(1 for s,_,_ in results if s=="WARN")
    f = sum(1 for s,_,_ in results if s=="FAIL")
    print(f"\n{'='*60}\n Round {n} - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n{'='*60}")
    for s, item, detail in results:
        print(f"  [{s}] {item}: {detail}")
    print(f"{'-'*60}\n  {p} passed, {w} warnings, {f} failed\n{'='*60}")
    return p, w, f


def main():
    rounds = 1
    if "--rounds" in sys.argv:
        rounds = int(sys.argv[sys.argv.index("--rounds")+1])
    tp = tw = tf = 0; any_fail = False
    for r in range(1, rounds+1):
        p,w,f = run_round(r); tp+=p; tw+=w; tf+=f
        if f>0: any_fail=True
        if r<rounds: time.sleep(3)
    print(f"\n{'#'*60}\n FINAL: {rounds} rounds, PASS={tp}, WARN={tw}, FAIL={tf}\n{'#'*60}")
    sys.exit(1 if any_fail else 0)


if __name__ == "__main__":
    main()
