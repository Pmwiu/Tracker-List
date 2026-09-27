#!/usr/bin/env python3
"""
自动从公开 GitHub 项目下载 Tracker 列表，合并去重后写入本地仓库，
并生成 GitHub Pages 短链接重定向页面、服务主页与多 CDN 镜像清单。

DNS 防污染策略:
  - GitHub raw 直连（默认）
  - jsDelivr CDN（cdn.jsdelivr.net）
  - jsDelivr Fastly 节点（fastly.jsdelivr.net）
  - jsDelivr Gcore 节点（gcore.jsdelivr.net）
  - ghproxy 代理镜像
  - GitHub Pages 跳转层

数据源: ngosang/trackerslist
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
        "trackers_all.txt",
        "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt",
    ),
    (
        "trackers_all_ip.txt",
        "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ip.txt",
    ),
    (
        "trackers_all_i2p.txt",
        "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_i2p.txt",
    ),
    (
        "trackers_all_yggdrasil.txt",
        "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_yggdrasil.txt",
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
    # --- 核心订阅：合并总表（多CDN） ---
    ("all",        "核心订阅", "合并总表（Raw 直连，推荐）",
     "https://raw.githubusercontent.com/{repo}/main/trackers/trackers_merged.txt"),
    ("all-cdn",     "核心订阅", "合并总表（jsDelivr CDN）",
     "https://cdn.jsdelivr.net/gh/{repo}@main/trackers/trackers_merged.txt"),
    ("all-fastly",  "核心订阅", "合并总表（Fastly 节点）",
     "https://fastly.jsdelivr.net/gh/{repo}@main/trackers/trackers_merged.txt"),
    ("all-gcore",   "核心订阅", "合并总表（Gcore 节点）",
     "https://gcore.jsdelivr.net/gh/{repo}@main/trackers/trackers_merged.txt"),
    ("all-proxy",   "核心订阅", "合并总表（ghproxy 代理）",
     "https://ghproxy.net/https://raw.githubusercontent.com/{repo}/main/trackers/trackers_merged.txt"),

    # --- 分类列表（Raw 直连） ---
    ("trackers", "分类列表", "全部 Tracker 列表",
     "https://raw.githubusercontent.com/{repo}/main/trackers/trackers_all.txt"),
    ("ip",       "分类列表", "IP 类 Tracker",
     "https://raw.githubusercontent.com/{repo}/main/trackers/trackers_all_ip.txt"),
    ("i2p",      "分类列表", "I2P 网络 Tracker",
     "https://raw.githubusercontent.com/{repo}/main/trackers/trackers_all_i2p.txt"),
    ("ygg",      "分类列表", "Yggdrasil 网络 Tracker",
     "https://raw.githubusercontent.com/{repo}/main/trackers/trackers_all_yggdrasil.txt"),

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
    <p>Copy the short link into your BitTorrent client's tracker subscription field:</p>
    <div class="usage">{pages_base}/s/all</div>
    <p style="margin-top:0.8rem; font-size:0.88rem; color:#8b949e;">
      If blocked, try CDN mirrors: <code style="color:#7ee787;">/s/all-cdn</code>,
      <code style="color:#7ee787;">/s/all-fastly</code>,
      <code style="color:#7ee787;">/s/all-gcore</code>,
      <code style="color:#7ee787;">/s/all-proxy</code>.
    </p>
  </section>

  <div class="footer">
    <p>Last updated: {now}</p>
    <p>Source: <a href="https://github.com/ngosang/trackerslist">ngosang/trackerslist</a> &middot;
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

    print("\n===== Summary =====")
    for name, count in results:
        print(f"  {name}: {count}")
    print("===================")

    if not results:
        print("[ERROR] No tracker files were updated.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
