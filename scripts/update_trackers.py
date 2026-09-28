#!/usr/bin/env python3
"""
自动从订阅源下载 Tracker 列表，合并去重后写入本地仓库，
并生成 GitHub Pages 短链接重定向页面、服务主页与纯文本订阅文件。

订阅源（均为 best 精选列表）:
  - https://cf.trackerslist.com/best.txt
  - https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt
  - https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best_ip.txt
  - https://tracker.adysec.com/trackers_best.txt

特性:
  - 多源合并去重（URL 规范化后去重）
  - 下载内容校验（拒绝非 tracker 内容）
  - 原子写入（临时文件 + rename，防止中途崩溃损坏文件）
  - 文件锁防止并发运行
  - 仅保留 GitHub Raw 直链与 Pages 短链接，无 CDN/代理加速链接
  - 纯文本 .txt 直链供 BT 客户端直接订阅
"""

import os
import re
import sys
import time
import html
import urllib.request
import urllib.error
import datetime

try:
    import fcntl
    _HAS_FCNTL = True
except ImportError:
    _HAS_FCNTL = False

SOURCES = [
    ("trackers_best.txt", "https://cf.trackerslist.com/best.txt", "cf-best"),
    ("trackers_ngosang.txt", "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt", "ngosang-best"),
    ("trackers_ngosang_ip.txt", "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best_ip.txt", "ngosang-best-ip"),
    ("trackers_adysec.txt", "https://tracker.adysec.com/trackers_best.txt", "adysec-best"),
]

MAX_TRACKERS = 39

MIRRORS = [
    ("GitHub Raw", "https://raw.githubusercontent.com/{repo}/main/trackers/{file}"),
]

SHORT_LINKS = [
    ("alive", "核心订阅", "存活 Tracker（活性测试+测速排序，推荐）",
     "https://raw.githubusercontent.com/{repo}/main/trackers/trackers_alive.txt"),
    ("best", "订阅源", "cf.trackerslist.com best",
     "https://raw.githubusercontent.com/{repo}/main/trackers/trackers_best.txt"),
    ("ngosang", "订阅源", "ngosang trackers_best",
     "https://raw.githubusercontent.com/{repo}/main/trackers/trackers_ngosang.txt"),
    ("ngosang-ip", "订阅源", "ngosang trackers_best_ip",
     "https://raw.githubusercontent.com/{repo}/main/trackers/trackers_ngosang_ip.txt"),
    ("adysec", "订阅源", "adysec trackers_best",
     "https://raw.githubusercontent.com/{repo}/main/trackers/trackers_adysec.txt"),
    ("all", "合并总表", "合并去重总表",
     "https://raw.githubusercontent.com/{repo}/main/trackers/trackers_merged.txt"),
]

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "trackers")
PAGES_DIR = os.path.join(PROJECT_ROOT, "docs")
SHORT_LINKS_DIR = os.path.join(PAGES_DIR, "s")
MERGED_FILE = "trackers_merged.txt"
ALIVE_FILE = "trackers_alive.txt"
DEAD_FILE = "trackers_dead.txt"
LOCK_FILE = os.path.join(PROJECT_ROOT, ".update.lock")

LEGACY_FILES = [
    os.path.join(OUTPUT_DIR, "trackers_http.txt"),
    os.path.join(OUTPUT_DIR, "trackers_all.txt"),
    os.path.join(OUTPUT_DIR, "trackers_run.txt"),
    os.path.join(PAGES_DIR, "http.txt"),
    os.path.join(PAGES_DIR, "full.txt"),
    os.path.join(SHORT_LINKS_DIR, "http.html"),
    os.path.join(SHORT_LINKS_DIR, "full.html"),
    os.path.join(SHORT_LINKS_DIR, "run.html"),
    os.path.join(SHORT_LINKS_DIR, "repo.html"),
    os.path.join(SHORT_LINKS_DIR, "alive-cdn.html"),
    os.path.join(SHORT_LINKS_DIR, "all-cdn.html"),
    os.path.join(SHORT_LINKS_DIR, "all-fastly.html"),
    os.path.join(SHORT_LINKS_DIR, "all-gcore.html"),
    os.path.join(SHORT_LINKS_DIR, "all-proxy.html"),
]

TIMEOUT = 30
MAX_RETRIES = 3
RETRY_DELAY = 5

TRACKER_PATTERN = re.compile(
    r'^(udp|http|https|wss|ws)://[^\s/$.?#].[^\s]*$', re.IGNORECASE
)


def get_repo():
    repo = os.environ.get("GITHUB_REPOSITORY", "").strip()
    return repo if repo else "Pmwiu/Tracker-List"


def acquire_lock():
    os.makedirs(os.path.dirname(LOCK_FILE), exist_ok=True)
    deadline = time.time() + 10
    lock_fd = None
    while time.time() < deadline:
        if _HAS_FCNTL:
            try:
                lock_fd = open(LOCK_FILE, "w")
                fcntl.flock(lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                lock_fd.write(str(os.getpid()))
                lock_fd.flush()
                return lock_fd
            except (IOError, OSError):
                if lock_fd:
                    lock_fd.close()
                time.sleep(0.5)
                continue
        else:
            try:
                fd = os.open(LOCK_FILE, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                with os.fdopen(fd, "w") as f:
                    f.write(str(os.getpid()))
                return LOCK_FILE
            except FileExistsError:
                try:
                    with open(LOCK_FILE, "r") as f:
                        old_pid = f.read().strip()
                    if old_pid and old_pid.isdigit():
                        try:
                            os.kill(int(old_pid), 0)
                            time.sleep(0.5)
                            continue
                        except (OSError, ValueError):
                            pass
                    try:
                        os.remove(LOCK_FILE)
                    except OSError:
                        pass
                    continue
                except (IOError, OSError):
                    time.sleep(0.5)
                    continue
    print("[ERROR] Could not acquire lock (another instance running?)", file=sys.stderr)
    sys.exit(1)


def release_lock(lock_handle):
    try:
        if _HAS_FCNTL and hasattr(lock_handle, 'fileno'):
            fcntl.flock(lock_handle, fcntl.LOCK_UN)
            lock_handle.close()
        if os.path.exists(LOCK_FILE):
            try:
                os.remove(LOCK_FILE)
            except OSError:
                pass
    except OSError:
        pass


def normalize_tracker(url):
    url = url.strip()
    if not url:
        return None
    if "://" in url:
        scheme, rest = url.split("://", 1)
        scheme = scheme.lower()
        rest = rest.rstrip("/")
        return f"{scheme}://{rest}"
    return url


def is_valid_tracker(url):
    if not url or len(url) > 500:
        return False
    return bool(TRACKER_PATTERN.match(url))


def cleanup_legacy_files():
    removed = 0
    for path in LEGACY_FILES:
        if os.path.exists(path):
            try:
                os.remove(path)
                print(f"[CLEAN] {os.path.relpath(path, PROJECT_ROOT)}")
                removed += 1
            except OSError as e:
                print(f"[WARN]  {path}: {e}")
    if removed:
        print(f"[OK]   Cleaned {removed} legacy files.")


def download_trackers(url):
    last_error = None
    raw = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "Mozilla/5.0 (compatible; TrackerListBot/3.0)",
                "Accept": "text/plain,*/*",
            })
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                if resp.status != 200:
                    raise urllib.error.HTTPError(url, resp.status, "Non-200", {}, None)
                raw = resp.read().decode("utf-8", errors="replace")
            break
        except Exception as e:
            last_error = e
            if attempt < MAX_RETRIES:
                print(f"  [RETRY] {attempt}/{MAX_RETRIES}: {e}")
                time.sleep(RETRY_DELAY)
            else:
                raise last_error
    if raw is None:
        raise RuntimeError("Empty response")
    if raw.lstrip().startswith("<!DOCTYPE") or raw.lstrip().startswith("<html"):
        raise RuntimeError("Response is HTML, not tracker list")
    trackers = set()
    invalid = 0
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        normalized = normalize_tracker(line)
        if normalized and is_valid_tracker(normalized):
            trackers.add(normalized)
        else:
            invalid += 1
    if invalid > 0:
        print(f"  [INFO] Skipped {invalid} invalid lines")
    if not trackers:
        raise RuntimeError("No valid trackers found in response")
    return sorted(trackers)


def atomic_write(filepath, content):
    tmp_path = filepath + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, filepath)


def write_trackers(filepath, trackers, source_url=None, extra_header=None):
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    header = [
        "# Auto-generated by update_trackers.py",
        f"# Last updated: {now} UTC",
    ]
    if source_url:
        header.append(f"# Source: {source_url}")
    if extra_header:
        header.append(extra_header)
    header.append(f"# Total unique trackers: {len(trackers)}")
    header.append("")
    body = "\n".join(trackers)
    if trackers:
        body += "\n"
    content = "\n".join(header) + body
    atomic_write(filepath, content)


def write_mirrors_file(repo):
    lines = [
        "# Tracker 订阅地址清单",
        f"# Generated: {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC",
        "# 仅保留 GitHub Raw 直连，无 CDN/代理加速链接",
        "",
    ]
    for name, template in MIRRORS:
        url = template.format(repo=repo, file=MERGED_FILE)
        lines += [f"# [{name}]", url, ""]
    atomic_write(os.path.join(OUTPUT_DIR, "MIRRORS.txt"), "\n".join(lines))
    print("[OK]   MIRRORS.txt")


def generate_redirect_page(target_url, description=""):
    eu = html.escape(target_url, quote=True)
    ed = html.escape(description)
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="refresh" content="0; url={eu}">
<link rel="canonical" href="{eu}">
<title>Redirect &mdash; Tracker List</title>
<style>
  body{{font-family:"SF Pro Display","Helvetica Neue",Arial,sans-serif;background:#fafafa;color:#666;
       display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}}
  .box{{text-align:center}}
  .box p{{margin:8px 0;font-size:14px}}
  a{{color:#2563eb;text-decoration:none}}
  a:hover{{text-decoration:underline}}
</style>
</head>
<body>
<div class="box">
  <p>{ed}</p>
  <p><a href="{eu}">Continue &rarr;</a></p>
</div>
<script>window.location.replace("{eu}");</script>
</body>
</html>
"""


def generate_source_links():
    label_map = {
        "cf-best": "cf/best",
        "ngosang-best": "ngosang/best",
        "ngosang-best-ip": "ngosang/best-ip",
        "adysec-best": "adysec/best",
    }
    parts = []
    for _, url, short_name in SOURCES:
        label = label_map.get(short_name, short_name)
        parts.append(f'<a href="{html.escape(url)}">{html.escape(label)}</a>')
    return " &middot;\n      ".join(parts)


def generate_index_page(repo, short_links_with_urls, tracker_counts):
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    owner = repo.split("/")[0] if "/" in repo else repo
    repo_name = repo.split("/")[-1] if "/" in repo else "Tracker-List"
    pages_base = f"https://{owner}.github.io/{repo_name}"
    groups = {}
    for short, group, desc, target in short_links_with_urls:
        groups.setdefault(group, []).append((short, desc, target))
    sections_html = ""
    for group_name in ["核心订阅", "订阅源", "合并总表"]:
        items = groups.get(group_name, [])
        if not items:
            continue
        rows = ""
        for short, desc, target in items:
            short_url = f"{pages_base}/s/{short}"
            rows += f"""      <div class="row">
        <div class="row-label">{html.escape(desc)}</div>
        <div class="row-link"><a href="{html.escape(short_url)}">{html.escape(short_url)}</a></div>
      </div>
"""
        sections_html += f"""    <div class="block">
      <div class="block-title">{html.escape(group_name)}</div>
{rows}    </div>
"""
    counts_rows = ""
    for name, count in tracker_counts:
        counts_rows += f"""      <tr><td>{html.escape(name)}</td><td class="num">{count}</td></tr>
"""
    source_links = generate_source_links()
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tracker List</title>
<style>
  *,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
  html{{-webkit-font-smoothing:antialiased}}
  body{{font-family:"SF Pro Display","Helvetica Neue",Arial,sans-serif;
        background:#fafafa;color:#1a1a1a;line-height:1.7;font-size:15px}}
  .wrap{{max-width:680px;margin:0 auto;padding:64px 32px 48px}}
  header{{margin-bottom:56px}}
  .brand{{font-size:11px;letter-spacing:3px;text-transform:uppercase;color:#999;margin-bottom:16px}}
  h1{{font-size:32px;font-weight:600;letter-spacing:-0.5px;color:#111;margin-bottom:12px}}
  .tagline{{font-size:14px;color:#666;max-width:480px}}
  .meta{{display:flex;gap:24px;margin-top:24px;font-size:12px;color:#999;flex-wrap:wrap}}
  .meta span{{display:flex;align-items:center;gap:6px}}
  .meta .dot{{width:6px;height:6px;border-radius:50%;background:#22c55e;display:inline-block}}
  .block{{border-top:1px solid #e5e5e5;padding:28px 0}}
  .block-title{{font-size:11px;letter-spacing:2px;text-transform:uppercase;color:#999;margin-bottom:16px}}
  .row{{display:flex;justify-content:space-between;align-items:baseline;padding:10px 0;border-bottom:1px solid #f0f0f0}}
  .row:last-child{{border-bottom:none}}
  .row-label{{font-size:14px;color:#333;flex-shrink:0;margin-right:16px}}
  .row-link{{font-size:13px;font-family:"SF Mono",Menlo,monospace;text-align:right}}
  .row-link a{{color:#2563eb;text-decoration:none;word-break:break-all}}
  .row-link a:hover{{text-decoration:underline}}
  table{{width:100%;border-collapse:collapse;font-size:13px}}
  th,td{{text-align:left;padding:8px 0;border-bottom:1px solid #f0f0f0}}
  th{{font-size:11px;letter-spacing:1px;text-transform:uppercase;color:#999;font-weight:500}}
  td.num{{text-align:right;font-family:"SF Mono",Menlo,monospace;color:#333}}
  .subscribe{{background:#111;color:#fff;padding:32px;border-radius:4px;margin:32px 0}}
  .subscribe-label{{font-size:11px;letter-spacing:2px;text-transform:uppercase;color:#888;margin-bottom:12px}}
  .subscribe-url{{font-family:"SF Mono",Menlo,monospace;font-size:14px;color:#fff;word-break:break-all}}
  .subscribe-url a{{color:#fff;text-decoration:none;border-bottom:1px solid #444}}
  .subscribe-url a:hover{{border-bottom-color:#fff}}
  .subscribe-note{{font-size:12px;color:#888;margin-top:12px}}
  footer{{margin-top:56px;padding-top:24px;border-top:1px solid #e5e5e5;font-size:12px;color:#999}}
  footer a{{color:#666;text-decoration:none}}
  footer a:hover{{color:#111}}
  footer .sources{{margin-top:8px}}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <div class="brand">Pmwiu / Tracker-List</div>
    <h1>Tracker List</h1>
    <p class="tagline">自动聚合、去重、活性测试与测速排序的 BitTorrent Tracker 订阅服务。每日更新，仅保留最快最稳定的 {MAX_TRACKERS} 个。</p>
    <div class="meta">
      <span><span class="dot"></span> 7x24H Auto Update</span>
      <span>Top {MAX_TRACKERS} by Speed</span>
      <span>Direct Links Only</span>
    </div>
  </header>

{sections_html}  <div class="block">
    <div class="block-title">Statistics</div>
    <table>
      <thead><tr><th>List</th><th>Count</th></tr></thead>
      <tbody>
{counts_rows}      </tbody>
    </table>
  </div>

  <div class="subscribe">
    <div class="subscribe-label">BT Client Subscription</div>
    <div class="subscribe-url"><a href="{pages_base}/alive.txt">{pages_base}/alive.txt</a></div>
    <p class="subscribe-note">纯文本直链，qBittorrent 等客户端可直接订阅。经活性测试 + 测速排序，最多 {MAX_TRACKERS} 个。</p>
  </div>

  <footer>
    <p>Last updated: {now}</p>
    <p class="sources">Sources:
      {source_links} &middot;
      <a href="https://github.com/{repo}">GitHub</a>
    </p>
  </footer>
</div>
</body>
</html>
"""


def generate_pages(repo, results):
    os.makedirs(SHORT_LINKS_DIR, exist_ok=True)
    sl = []
    for short, group, desc, template in SHORT_LINKS:
        target = template.format(repo=repo)
        sl.append((short, group, desc, target))
        page_content = generate_redirect_page(target, desc)
        atomic_write(os.path.join(SHORT_LINKS_DIR, f"{short}.html"), page_content)
        print(f"[OK]   /s/{short}")
    index_content = generate_index_page(repo, sl, results)
    atomic_write(os.path.join(PAGES_DIR, "index.html"), index_content)
    print("[OK]   index.html")
    nj = os.path.join(PAGES_DIR, ".nojekyll")
    if not os.path.exists(nj):
        open(nj, "w").close()


def sync_plain_text_files():
    mapping = {
        "trackers_alive.txt": "alive.txt",
        "trackers_merged.txt": "merged.txt",
        "trackers_best.txt": "best.txt",
        "trackers_ngosang.txt": "ngosang.txt",
        "trackers_ngosang_ip.txt": "ngosang_ip.txt",
        "trackers_adysec.txt": "adysec.txt",
    }
    os.makedirs(PAGES_DIR, exist_ok=True)
    for src, dst in mapping.items():
        sp = os.path.join(OUTPUT_DIR, src)
        if os.path.exists(sp):
            with open(sp, "r", encoding="utf-8") as f:
                content = f.read()
            atomic_write(os.path.join(PAGES_DIR, dst), content)
            print(f"[OK]   docs/{dst}")


def count_trackers_in_text(text):
    return sum(1 for line in text.splitlines() if line.strip() and not line.strip().startswith("#"))


def main():
    lock_fd = acquire_lock()
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        repo = get_repo()
        print(f"[INFO] Repo: {repo}, Max: {MAX_TRACKERS}")
        cleanup_legacy_files()
        all_merged = set()
        results = []
        failures = []
        for filename, url, short_name in SOURCES:
            print(f"\n[INFO] {filename} ({short_name})")
            try:
                trackers = download_trackers(url)
            except Exception as e:
                print(f"[ERROR] {e}", file=sys.stderr)
                failures.append((filename, short_name, str(e)))
                continue
            write_trackers(os.path.join(OUTPUT_DIR, filename), trackers, source_url=url)
            all_merged.update(trackers)
            results.append((filename, len(trackers)))
            print(f"[OK]   {len(trackers)} unique")
        if failures:
            print(f"\n[WARN] {len(failures)} source(s) failed:")
            for fn, sn, err in failures:
                print(f"  - {sn}: {err}")
        if all_merged:
            merged = sorted(all_merged)
            write_trackers(
                os.path.join(OUTPUT_DIR, MERGED_FILE), merged,
                source_url=", ".join(u for _, u, _ in SOURCES),
            )
            results.append((MERGED_FILE, len(merged)))
            print(f"\n[OK]   merged: {len(merged)}")
        else:
            print("[ERROR] No trackers downloaded from any source!", file=sys.stderr)
            sys.exit(1)
        write_mirrors_file(repo)
        generate_pages(repo, results)
        sync_plain_text_files()
        print(f"\n===== Summary =====")
        for n, c in results:
            print(f"  {n}: {c}")
        print(f"  alive capped at {MAX_TRACKERS} after test+sort")
        if failures:
            print(f"  FAILED SOURCES: {len(failures)}")
        print("===================")
    finally:
        release_lock(lock_fd)


if __name__ == "__main__":
    main()
