#!/usr/bin/env python3
"""
自动从订阅源下载 Tracker 列表，合并去重后写入本地仓库，
并生成 GitHub Pages 短链接重定向页面、服务主页与多 CDN 镜像清单。

订阅源:
  - https://cf.trackerslist.com/best.txt
  - https://cf.trackerslist.com/http.txt
  - https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt

DNS 防污染策略:
  - GitHub raw 直连（默认）
  - jsDelivr CDN（cdn.jsdelivr.net）
  - jsDelivr Fastly 节点（fastly.jsdelivr.net）
  - jsDelivr Gcore 节点（gcore.jsdelivr.net）
  - ghproxy / gh-proxy 代理镜像
  - GitHub Pages 跳转层
"""

import os
import sys
import time
import html
import urllib.request
import datetime

# ============================================================
# 数据源配置: (输出文件名, 源URL)
# ============================================================
SOURCES = [
    (
        "trackers_best.txt",
        "https://cf.trackerslist.com/best.txt",
    ),
    (
        "trackers_http.txt",
        "https://cf.trackerslist.com/http.txt",
    ),
    (
        "trackers_all.txt",
        "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt",
    ),
]

# ============================================================
# CDN 镜像模板（{repo}=owner/repo, {file}=文件名）
# ============================================================
MIRRORS = [
    ("GitHub Raw 直连", "https://raw.githubusercontent.com/{repo}/main/trackers/{file}"),
    ("jsDelivr CDN", "https://cdn.jsdelivr.net/gh/{repo}@main/trackers/{file}"),
    ("jsDelivr Fastly", "https://fastly.jsdelivr.net/gh/{repo}@main/trackers/{file}"),
    ("jsDelivr Gcore", "https://gcore.jsdelivr.net/gh/{repo}@main/trackers/{file}"),
    ("ghproxy 代理", "https://ghproxy.net/https://raw.githubusercontent.com/{repo}/main/trackers/{file}"),
    ("gh-proxy 代理", "https://gh-proxy.com/https://raw.githubusercontent.com/{repo}/main/trackers/{file}"),
]

# ============================================================
# 短链接配置: (短名, 分组, 描述, 目标URL模板)
# ============================================================
SHORT_LINKS = [
    # --- 核心订阅：存活列表（经活性测试，最推荐） ---
    ("alive",      "核心订阅", "存活 Tracker（经活性测试，最推荐）",
     "https://raw.githubusercontent.com/{repo}/main/trackers/trackers_alive.txt"),
    ("alive-cdn",  "核心订阅", "存活 Tracker（jsDelivr CDN）",
     "https://cdn.jsdelivr.net/gh/{repo}@main/trackers/trackers_alive.txt"),

    # --- 核心订阅：三个订阅源 ---
    ("best",       "核心订阅", "最佳 Tracker 列表（best，cf.trackerslist.com）",
     "https://raw.githubusercontent.com/{repo}/main/trackers/trackers_best.txt"),
    ("http",       "核心订阅", "HTTP/HTTPS Tracker 列表（cf.trackerslist.com）",
     "https://raw.githubusercontent.com/{repo}/main/trackers/trackers_http.txt"),
    ("full",       "核心订阅", "完整 Tracker 列表（ngosang trackers_all）",
     "https://raw.githubusercontent.com/{repo}/main/trackers/trackers_all.txt"),

    # --- 核心订阅：合并总表（多CDN） ---
    ("all",        "核心订阅", "合并总表（Raw 直连）",
     "https://raw.githubusercontent.com/{repo}/main/trackers/trackers_merged.txt"),
    ("all-cdn",     "核心订阅", "合并总表（jsDelivr CDN）",
     "https://cdn.jsdelivr.net/gh/{repo}@main/trackers/trackers_merged.txt"),
    ("all-fastly",  "核心订阅", "合并总表（Fastly 节点）",
     "https://fastly.jsdelivr.net/gh/{repo}@main/trackers/trackers_merged.txt"),
    ("all-gcore",   "核心订阅", "合并总表（Gcore 节点）",
     "https://gcore.jsdelivr.net/gh/{repo}@main/trackers/trackers_merged.txt"),
    ("all-proxy",   "核心订阅", "合并总表（ghproxy 代理）",
     "https://ghproxy.net/https://raw.githubusercontent.com/{repo}/main/trackers/trackers_merged.txt"),

    # --- 其他 ---
    ("repo", "其他", "GitHub 仓库主页",
     "https://github.com/{repo}"),
]

# ============================================================
# 路径配置
# ============================================================
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "trackers")
PAGES_DIR = os.path.join(PROJECT_ROOT, "docs")
SHORT_LINKS_DIR = os.path.join(PAGES_DIR, "s")
MERGED_FILE = "trackers_merged.txt"
ALIVE_FILE = "trackers_alive.txt"
DEAD_FILE = "trackers_dead.txt"

# ============================================================
# 网络配置
# ============================================================
TIMEOUT = 30
MAX_RETRIES = 3
RETRY_DELAY = 5


def get_repo():
    """获取当前仓库 owner/repo，优先从环境变量读取。"""
    repo = os.environ.get("GITHUB_REPOSITORY", "").strip()
    if repo:
        return repo
    return "Pmwiu/Tracker-List"


def download_trackers(url):
    """从 URL 下载 tracker 列表，带重试机制，返回去重排序后的列表。"""
    last_error = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "trackers-list-bot/1.0"})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                raw = resp.read().decode("utf-8", errors="replace")
            break
        except Exception as e:
            last_error = e
            if attempt < MAX_RETRIES:
                print(f"  [RETRY] Attempt {attempt}/{MAX_RETRIES} failed: {e}. Retrying in {RETRY_DELAY}s...")
                time.sleep(RETRY_DELAY)
            else:
                raise last_error

    trackers = set()
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        trackers.add(line)

    return sorted(trackers)


def write_trackers(filepath, trackers, source_url=None):
    """将 tracker 列表写入文件，带文件头注释。"""
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    header_lines = [
        "# Auto-generated by update_trackers.py",
        f"# Last updated: {now} UTC",
    ]
    if source_url:
        header_lines.append(f"# Source: {source_url}")
    header_lines.append(f"# Total unique trackers: {len(trackers)}")
    header_lines.append("")

    content = "\n".join(header_lines) + "\n".join(trackers) + "\n"
    with open(filepath, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)


def write_mirrors_file(repo):
    """生成镜像清单 MIRRORS.txt。"""
    lines = [
        "# Tracker 订阅镜像地址清单",
        f"# Generated: {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC",
        "# 若默认链接无法访问，请依次尝试以下镜像：",
        "",
    ]
    for mirror_name, template in MIRRORS:
        url = template.format(repo=repo, file=MERGED_FILE)
        lines.append(f"# [{mirror_name}]")
        lines.append(url)
        lines.append("")

    path = os.path.join(OUTPUT_DIR, "MIRRORS.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))
    print(f"[OK]   MIRRORS.txt generated ({len(MIRRORS)} mirrors).")


def generate_redirect_page(target_url, description=""):
    """生成短链接重定向 HTML 页面（三重兜底）。"""
    escaped_url = html.escape(target_url, quote=True)
    escaped_desc = html.escape(description)
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="refresh" content="0; url={escaped_url}">
<link rel="canonical" href="{escaped_url}">
<title>Redirecting... | Tracker List</title>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
         display: flex; justify-content: center; align-items: center;
         min-height: 100vh; margin: 0; background: #0d1117; color: #c9d1d9; }}
  .box {{ text-align: center; padding: 2rem; }}
  .spinner {{ width: 40px; height: 40px; border: 3px solid #30363d; border-top-color: #58a6ff;
              border-radius: 50%; animation: spin 0.8s linear infinite; margin: 0 auto 1.5rem; }}
  @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
  a {{ color: #58a6ff; }}
</style>
</head>
<body>
<div class="box">
  <div class="spinner"></div>
  <p>{escaped_desc}</p>
  <p>If not redirected, <a href="{escaped_url}">click here</a>.</p>
</div>
<script>window.location.replace("{escaped_url}");</script>
</body>
</html>
"""


def generate_index_page(repo, short_links_with_urls, tracker_counts):
    """生成 GitHub Pages 服务主页，按分组展示短链接。"""
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    owner = repo.split("/")[0] if "/" in repo else repo
    repo_name = repo.split("/")[-1] if "/" in repo else "Tracker-List"
    pages_base = f"https://{owner}.github.io/{repo_name}"

    groups = {}
    for short, group, desc, target in short_links_with_urls:
        groups.setdefault(group, []).append((short, desc, target))

    sections_html = ""
    for group_name in ["核心订阅", "分类列表", "其他"]:
        items = groups.get(group_name, [])
        if not items:
            continue
        cards = ""
        for short, desc, target in items:
            short_url = f"{pages_base}/s/{short}"
            cards += f"""        <div class="link-card">
          <div class="link-short"><a href="{html.escape(short_url)}">{html.escape(short_url)}</a></div>
          <div class="link-desc">{html.escape(desc)}</div>
          <div class="link-target">&#8594; {html.escape(target)}</div>
        </div>
"""
        sections_html += f"""  <section>
    <h2>{html.escape(group_name)}</h2>
{cards}  </section>

"""

    counts_rows = ""
    for name, count in tracker_counts:
        counts_rows += f"        <tr><td>{html.escape(name)}</td><td>{count}</td></tr>\n"

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tracker List - Auto Subscription Service</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
         background: #0d1117; color: #c9d1d9; line-height: 1.6; }}
  .container {{ max-width: 820px; margin: 0 auto; padding: 2rem 1.5rem; }}
  header {{ text-align: center; padding: 3rem 0 2rem; }}
  h1 {{ font-size: 2rem; color: #f0f6fc; margin-bottom: 0.5rem; }}
  .subtitle {{ color: #8b949e; font-size: 1rem; }}
  .badges {{ margin-top: 0.8rem; }}
  .badge {{ display: inline-block; background: #238636; color: #fff; font-size: 0.75rem;
            padding: 0.2rem 0.6rem; border-radius: 12px; margin: 0 0.2rem; }}
  .badge.blue {{ background: #1f6feb; }}
  section {{ background: #161b22; border: 1px solid #30363d; border-radius: 8px;
             padding: 1.5rem; margin-bottom: 1.5rem; }}
  h2 {{ font-size: 1.15rem; color: #f0f6fc; margin-bottom: 1rem; padding-bottom: 0.5rem;
        border-bottom: 1px solid #21262d; }}
  .link-card {{ padding: 0.8rem 0; border-bottom: 1px solid #21262d; }}
  .link-card:last-child {{ border-bottom: none; }}
  .link-short a {{ color: #58a6ff; text-decoration: none; font-weight: 600; word-break: break-all; }}
  .link-short a:hover {{ text-decoration: underline; }}
  .link-desc {{ color: #c9d1d9; font-size: 0.9rem; margin-top: 0.2rem; }}
  .link-target {{ color: #8b949e; font-size: 0.78rem; margin-top: 0.2rem; word-break: break-all; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 0.9rem; }}
  th, td {{ text-align: left; padding: 0.5rem 0.75rem; border-bottom: 1px solid #21262d; }}
  th {{ color: #8b949e; font-weight: 600; }}
  td:last-child {{ text-align: right; font-variant-numeric: tabular-nums; }}
  .usage {{ background: #0d1117; border: 1px solid #30363d; border-radius: 6px;
            padding: 1rem; font-family: monospace; font-size: 0.85rem;
            overflow-x: auto; color: #7ee787; margin-top: 0.5rem; word-break: break-all; }}
  .footer {{ text-align: center; color: #484f58; font-size: 0.8rem; padding: 2rem 0; }}
  .footer a {{ color: #58a6ff; text-decoration: none; }}
</style>
</head>
<body>
<div class="container">
  <header>
    <h1>Tracker List</h1>
    <p class="subtitle">Auto Subscription &middot; Deduplicated &middot; Short Links &middot; Multi-CDN</p>
    <div class="badges">
      <span class="badge">7x24H Auto Update</span>
      <span class="badge blue">DNS Anti-Pollution</span>
      <span class="badge blue">Multi-CDN Failover</span>
    </div>
  </header>

{sections_html}  <section>
    <h2>Tracker Statistics</h2>
    <table>
      <thead><tr><th>List</th><th>Unique Count</th></tr></thead>
      <tbody>
{counts_rows}      </tbody>
    </table>
  </section>

  <section>
    <h2>Quick Start</h2>
    <p>For BT clients, use the plain-text link (no HTML redirect):</p>
    <div class="usage">{pages_base}/alive.txt</div>
    <p style="margin-top:0.8rem; font-size:0.88rem; color:#8b949e;">
      <code style="color:#7ee787;">/alive.txt</code> is pure text, directly subscribable in qBittorrent etc.
      Browser short link: <code style="color:#7ee787;">/s/alive</code> &middot;
      CDN: <code style="color:#7ee787;">/s/alive-cdn</code>.
    </p>
  </section>

  <div class="footer">
    <p>Last updated: {now}</p>
    <p>Sources: <a href="https://cf.trackerslist.com/best.txt">cf.trackerslist.com/best</a> &middot;
       <a href="https://cf.trackerslist.com/http.txt">cf.trackerslist.com/http</a> &middot;
       <a href="https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt">ngosang/trackerslist</a> &middot;
       Repo: <a href="https://github.com/{repo}">{repo}</a></p>
  </div>
</div>
</body>
</html>
"""


def generate_pages(repo, results):
    """生成 GitHub Pages 主页和所有短链接重定向页面。"""
    os.makedirs(SHORT_LINKS_DIR, exist_ok=True)

    short_links_with_urls = []
    for short, group, desc, template in SHORT_LINKS:
        target = template.format(repo=repo)
        short_links_with_urls.append((short, group, desc, target))

        page_content = generate_redirect_page(target, desc)
        page_path = os.path.join(SHORT_LINKS_DIR, f"{short}.html")
        with open(page_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(page_content)
        print(f"[OK]   /s/{short} -> {target}")

    index_content = generate_index_page(repo, short_links_with_urls, results)
    index_path = os.path.join(PAGES_DIR, "index.html")
    with open(index_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(index_content)
    print("[OK]   index.html generated.")

    nojekyll_path = os.path.join(PAGES_DIR, ".nojekyll")
    if not os.path.exists(nojekyll_path):
        with open(nojekyll_path, "w", encoding="utf-8") as f:
            f.write("")
        print("[OK]   .nojekyll created.")


def sync_plain_text_files():
    """将 trackers/ 下的关键列表同步为 docs/ 下的纯文本 .txt 文件。

    GitHub Pages 直接以 text/plain 提供这些文件，BT 客户端可直接订阅，
    无需经过 HTML 重定向页。这是修复 /s/alive 无法订阅问题的核心补丁。
    """
    mapping = {
        "trackers_alive.txt": "alive.txt",
        "trackers_merged.txt": "merged.txt",
        "trackers_best.txt": "best.txt",
        "trackers_http.txt": "http.txt",
        "trackers_all.txt": "full.txt",
    }
    os.makedirs(PAGES_DIR, exist_ok=True)
    for src_name, dst_name in mapping.items():
        src = os.path.join(OUTPUT_DIR, src_name)
        dst = os.path.join(PAGES_DIR, dst_name)
        if os.path.exists(src):
            with open(src, "r", encoding="utf-8") as f:
                content = f.read()
            with open(dst, "w", encoding="utf-8", newline="\n") as f:
                f.write(content)
            count = count_trackers_in_text(content)
            print(f"[OK]   docs/{dst_name} synced ({count} trackers, plain text for BT clients)")


def count_trackers_in_text(text):
    """统计文本中有效的 tracker 行数。"""
    count = 0
    for line in text.splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            count += 1
    return count


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    repo = get_repo()
    print(f"[INFO] Repository: {repo}")

    all_merged = set()
    results = []

    for filename, url in SOURCES:
        print(f"[INFO] Downloading {filename} ...")
        try:
            trackers = download_trackers(url)
        except Exception as e:
            print(f"[ERROR] Failed to download {filename}: {e}", file=sys.stderr)
            existing = os.path.join(OUTPUT_DIR, filename)
            if os.path.exists(existing):
                print(f"[WARN] Keeping existing {filename}.")
            continue

        filepath = os.path.join(OUTPUT_DIR, filename)
        write_trackers(filepath, trackers, source_url=url)
        all_merged.update(trackers)
        results.append((filename, len(trackers)))
        print(f"[OK]   {filename}: {len(trackers)} unique trackers.")

    if all_merged:
        merged_sorted = sorted(all_merged)
        merged_path = os.path.join(OUTPUT_DIR, MERGED_FILE)
        write_trackers(
            merged_path,
            merged_sorted,
            source_url=", ".join(url for _, url in SOURCES),
        )
        results.append((MERGED_FILE, len(merged_sorted)))
        print(f"[OK]   {MERGED_FILE}: {len(merged_sorted)} unique trackers (merged).")

    write_mirrors_file(repo)

    print("\n[INFO] Generating GitHub Pages ...")
    generate_pages(repo, results)

    print("\n[INFO] Syncing plain-text files for BT clients ...")
    sync_plain_text_files()

    print("\n===== Summary =====")
    for name, count in results:
        print(f"  {name}: {count}")
    print("===================")

    if not results:
        print("[ERROR] No tracker files were updated.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
