#!/usr/bin/env python3
"""健康检查：本地文件、CDN 镜像、短链接页面。"""
import os, sys, time, urllib.request, datetime

REPO = "Pmwiu/Tracker-List"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TD = os.path.join(ROOT, "trackers")
PD = os.path.join(ROOT, "docs")
SD = os.path.join(PD, "s")
TIMEOUT = 20

TRACKER_FILES = [
    "trackers_all.txt", "trackers_all_ip.txt", "trackers_all_ws.txt",
    "trackers_all_i2p.txt", "trackers_all_yggdrasil.txt",
    "trackers_all_yggdrasil_ip.txt", "trackers_merged.txt",
]
MIRRORS = [
    ("Raw", "https://raw.githubusercontent.com/{r}/main/trackers/trackers_merged.txt"),
    ("jsDelivr", "https://cdn.jsdelivr.net/gh/{r}@main/trackers/trackers_merged.txt"),
    ("Fastly", "https://fastly.jsdelivr.net/gh/{r}@main/trackers/trackers_merged.txt"),
    ("Gcore", "https://gcore.jsdelivr.net/gh/{r}@main/trackers/trackers_merged.txt"),
    ("ghproxy", "https://ghproxy.net/https://raw.githubusercontent.com/{r}/main/trackers/trackers_merged.txt"),
    ("gh-proxy", "https://gh-proxy.com/https://raw.githubusercontent.com/{r}/main/trackers/trackers_merged.txt"),
]
PAGES = ["all","all-cdn","all-fastly","all-gcore","all-proxy",
         "trackers","ip","ws","i2p","ygg","ygg-ip","repo"]


def count(text):
    return sum(1 for l in text.splitlines() if l.strip() and not l.startswith("#"))


def fetch(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "health-check"})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return True, r.read().decode("utf-8","replace"), r.status
    except urllib.error.HTTPError as e:
        return False, str(e), e.code
    except Exception as e:
        return False, str(e), 0


def check_local(res):
    for f in TRACKER_FILES:
        p = os.path.join(TD, f)
        if os.path.exists(p) and os.path.getsize(p) > 0:
            res.append(("PASS", f"tracker: {f}", f"{count(open(p,encoding='utf-8').read())} entries"))
        else:
            res.append(("FAIL", f"tracker: {f}", "missing"))
    mp = os.path.join(TD, "MIRRORS.txt")
    res.append(("PASS" if os.path.exists(mp) else "FAIL", "MIRRORS.txt", "ok" if os.path.exists(mp) else "missing"))
    ip = os.path.join(PD, "index.html")
    res.append(("PASS" if os.path.exists(ip) else "FAIL", "index.html", "ok" if os.path.exists(ip) else "missing"))
    for sp in PAGES:
        p = os.path.join(SD, f"{sp}.html")
        if os.path.exists(p):
            c = open(p, encoding="utf-8").read()
            ok = "http" in c and ("refresh" in c or "location" in c)
            res.append(("PASS" if ok else "FAIL", f"page: /s/{sp}", "valid" if ok else "invalid"))
        else:
            res.append(("FAIL", f"page: /s/{sp}", "missing"))


def check_mirrors(res):
    counts = {}
    for n, t in MIRRORS:
        ok, c, st = fetch(t.format(r=REPO))
        if ok:
            counts[n] = count(c)
            res.append(("PASS", f"mirror: {n}", f"HTTP {st}, {count(c)}"))
        else:
            res.append(("WARN", f"mirror: {n}", c[:50]))
    if len(counts) >= 2:
        u = set(counts.values())
        if len(u) == 1:
            res.append(("PASS", "consistency", f"match ({list(counts.values())[0]})"))
        else:
            res.append(("WARN", "consistency", str(counts)))


def round_(n):
    res = []
    check_local(res)
    check_mirrors(res)
    p = sum(1 for s,_,_ in res if s=="PASS")
    w = sum(1 for s,_,_ in res if s=="WARN")
    f = sum(1 for s,_,_ in res if s=="FAIL")
    print(f"\n{'='*60}\n Round {n} - {datetime.datetime.now().strftime('%H:%M:%S')}\n{'='*60}")
    for s, i, d in res:
        print(f"  [{s}] {i}: {d}")
    print(f"{'-'*60}\n  {p} pass, {w} warn, {f} fail\n{'='*60}")
    return p, w, f


def main():
    rounds = 1
    if "--rounds" in sys.argv:
        rounds = int(sys.argv[sys.argv.index("--rounds")+1])
    tp=tw=tf=0; bad=False
    for r in range(1, rounds+1):
        p,w,f = round_(r)
        tp+=p; tw+=w; tf+=f
        if f: bad=True
        if r<rounds: time.sleep(3)
    print(f"\n{'#'*60}")
    print(f" REPORT: {rounds} rounds | PASS {tp} | WARN {tw} | FAIL {tf}")
    print(f" {'ISSUES' if bad else 'ALL HEALTHY'}")
    print(f"{'#'*60}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
