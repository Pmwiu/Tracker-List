#!/usr/bin/env python3
"""自动发现公开 tracker 候选（Phase 1：纯观察 + 报告，不进 best/all）。

- 从 GitHub topic（bt-tracker / public-tracker / tracker-list）搜索仓库
- 每个仓库抓 README + 名称含 tracker 的 .txt 文件（≤10 文件、≤100KB）
- 解析出合法 tracker URL，去重后写入 trackers/discovered/candidates_<date>.txt
- 失败优雅：单个源失败不中断；离线场景下产生空文件，CI 仍能跑通
- 纯 stdlib：urllib, re, json, html.parser
"""

import argparse
import datetime
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

# 复用 update_trackers 的 tracker 校验 + 规范化
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import update_trackers as ut

GITHUB_API = "https://api.github.com"
TOPICS = ("bt-tracker", "public-tracker", "tracker-list")
PER_REPO_FILE_CAP = 10
PER_FILE_BYTE_CAP = 100 * 1024
TIMEOUT = 15
USER_AGENT = "Tracker-List-Discover/1.0 (https://github.com/Pmwiu/Tracker-List)"

# 公开"全量"列表（比白名单 best 源更宽，作为发现候选；不进 SOURCES 白名单）
PUBLIC_ALL_LISTS = [
    "https://cf.trackerslist.com/all.txt",
    "https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all.txt",
    "https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ip.txt",
    "https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_udp.txt",
    "https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_http.txt",
    "https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_https.txt",
    "https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ws.txt",
    "https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_wss.txt",
]
PUBLIC_LIST_CAP = 20  # 单次发现最多抓取的公开列表数（防失控）


def _github_headers():
    """GitHub API 请求头；CI 环境有 GITHUB_TOKEN 时带上以提升速率限制。"""
    headers = {"User-Agent": USER_AGENT, "Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers

# 仅匹配协议 (udp|http|https|wss|ws)://host[:port]/path
_URL_RE = re.compile(
    r'((?:udp|http|https|wss|ws)://[^\s<>"\']+)',
    re.IGNORECASE,
)


def extract_tracker_urls(text):
    """从自由文本中抽取候选 tracker URL，用 TRACKER_PATTERN 严格校验。"""
    if not text:
        return set()
    out = set()
    for m in _URL_RE.findall(text):
        candidate = m.rstrip(".,;:)]}\"'")
        normalized = ut.normalize_tracker(candidate)
        if normalized and ut.is_valid_tracker(normalized):
            out.add(normalized)
    return out


def filter_known(urls, known_urls):
    """返回 urls 中不与 known_urls 相交的子集（精确 URL 匹配）。"""
    return {u for u in urls if u not in known_urls}


def _http_get_json(url, timeout=TIMEOUT):
    """GET URL，期望 JSON 响应，失败抛异常。带 GITHUB_TOKEN（若有）时速率更高。"""
    req = urllib.request.Request(url, headers=_github_headers())
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8", errors="replace"))


def _http_get_text(url, timeout=TIMEOUT, max_bytes=PER_FILE_BYTE_CAP):
    """GET URL，返回前 max_bytes 字节的文本。失败抛异常。"""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read(max_bytes + 1)
    if len(data) > max_bytes:
        data = data[:max_bytes]
    return data.decode("utf-8", errors="replace")


def fetch_github_topic_repos(topic, timeout=TIMEOUT):
    """搜索 GitHub repos tagged with `topic`，返回 (full_name, default_branch) 列表。"""
    url = f"{GITHUB_API}/search/repositories?q=topic:{topic}&sort=updated&per_page=30"
    try:
        data = _http_get_json(url, timeout=timeout)
    except Exception as e:
        print(f"[WARN] github topic search failed ({topic}): {e}")
        return []
    out = []
    for repo in data.get("items", []):
        name = repo.get("full_name")
        branch = repo.get("default_branch") or "main"
        if name:
            out.append((name, branch))
    return out


def fetch_repo_tracker_files(full_name, default_branch="main",
                              timeout=TIMEOUT, file_cap=PER_REPO_FILE_CAP,
                              byte_cap=PER_FILE_BYTE_CAP):
    """对单个仓库抓 README.md + 名称含 tracker 的 .txt 文件。返回 (文件名, 内容) 列表。"""
    out = []
    # README
    for readme in ("README.md", "readme.md", "Readme.md"):
        url = (f"https://raw.githubusercontent.com/{full_name}/{default_branch}/"
               f"{readme}")
        try:
            text = _http_get_text(url, timeout=timeout, max_bytes=byte_cap)
            out.append((readme, text))
            break
        except Exception:
            continue
    # 仓库文件列表（用 GitHub API 列树；超时/失败时返回空）
    try:
        tree_url = (f"{GITHUB_API}/repos/{full_name}/git/trees/"
                    f"{default_branch}?recursive=1")
        data = _http_get_json(tree_url, timeout=timeout)
    except Exception:
        return out
    candidates = []
    for item in data.get("tree", []):
        path = item.get("path", "")
        if (item.get("type") == "blob"
                and path.lower().endswith(".txt")
                and "tracker" in path.lower()):
            candidates.append(path)
    for path in candidates[:file_cap - len(out)]:
        url = (f"https://raw.githubusercontent.com/{full_name}/{default_branch}/"
               f"{urllib.parse.quote(path)}")
        try:
            text = _http_get_text(url, timeout=timeout, max_bytes=byte_cap)
            out.append((path, text))
        except Exception as e:
            print(f"[WARN] {full_name}/{path} failed: {e}")
    return out


def _collect_known_urls():
    """从 update_trackers.SOURCES 与 tracker_merged.txt 当前内容构建已知 URL 集合。"""
    known = set()
    if hasattr(ut, "SOURCES"):
        for _name, url, _short in ut.SOURCES:
            known.add(url)
    project_root = ut.PROJECT_ROOT
    for fname in ("trackers_merged.txt", "trackers_alive.txt",
                  "trackers_all.txt"):
        path = os.path.join(project_root, "trackers", fname)
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        known.add(line)
    return known


def _existing_recent_candidates(out_dir, max_age_days=7):
    """加载过去 7 天的 candidates_*.txt，返回 set 形式（用于去重）。"""
    import glob
    out = set()
    if not os.path.isdir(out_dir):
        return out
    cutoff = datetime.datetime.now(datetime.timezone.utc).timestamp() - max_age_days * 86400
    for path in glob.glob(os.path.join(out_dir, "candidates_*.txt")):
        try:
            if os.path.getmtime(path) < cutoff:
                continue
        except OSError:
            continue
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    out.add(line)
    return out


def fetch_public_lists(urls=None, cap=PUBLIC_LIST_CAP, timeout=TIMEOUT):
    """抓取公开"全量"列表（cf.trackerslist/ngosang all 等），抽取候选 tracker URL。

    这些是发现候选的补充来源（比白名单 best 源宽得多）。单个列表失败仅告警跳过。
    """
    urls = urls or PUBLIC_ALL_LISTS
    out = set()
    for url in urls[:cap]:
        try:
            text = _http_get_text(url, timeout=timeout, max_bytes=PER_FILE_BYTE_CAP)
            found = extract_tracker_urls(text)
            out |= found
            print(f"[INFO] public list {url}: {len(found)} urls")
        except Exception as e:
            print(f"[WARN] public list fetch failed {url}: {e}")
    return out


def discover_trackers(out_dir="trackers/discovered", known_urls=None):
    """运行一次发现流程；返回新写入的 URL 数量。"""
    if known_urls is None:
        known_urls = _collect_known_urls()
    known_urls |= _existing_recent_candidates(out_dir)

    collected = set()
    # 1) 公开"全量"列表（宽口径候选）
    collected |= fetch_public_lists()
    # 2) GitHub topic 仓库扫描
    for topic in TOPICS:
        repos = fetch_github_topic_repos(topic)
        for full_name, branch in repos:
            for _fname, text in fetch_repo_tracker_files(full_name, branch):
                collected |= extract_tracker_urls(text)
            if len(collected) >= 2000:  # 全局硬上限，避免单次失控
                break
        if len(collected) >= 2000:
            break

    new_urls = filter_known(collected, known_urls)
    os.makedirs(out_dir, exist_ok=True)
    date_str = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d")
    out_path = os.path.join(out_dir, f"candidates_{date_str}.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        for url in sorted(new_urls):
            f.write(url + "\n")
    print(f"[OK]   {len(new_urls)} new candidates -> {os.path.basename(out_path)}")
    return len(new_urls)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", default="trackers/discovered")
    args = parser.parse_args()
    n = discover_trackers(args.out_dir)
    print(f"[OK]   {n} new candidates")
    return 0


if __name__ == "__main__":
    sys.exit(main())
