#!/usr/bin/env python3
"""
自动从订阅源下载 Tracker 列表，合并去重后写入本地仓库，
并生成 GitHub Pages 短链接重定向页面、服务主页与纯文本订阅文件。

订阅源（5 个精选源，SOURCES 顺序即优先级）:
  - cf.trackerslist.com/best.txt
  - trackers.run/s/rw_up_hp_hs_v4_v6.txt
  - ngosang/trackerslist trackers_best.txt + trackers_best_ip.txt
  - 1265578519/OpenTracker tracker.txt
  在下方 SOURCES 中增删 (输出文件名, 源 URL, 短名) 三元组即可调整；
  白名单 ALLOWED_SOURCE_URLS 与下游脚本会自动同步，无需其它改动。

特性:
  - 多源合并去重（URL 规范化后去重）
  - 来源白名单校验（仅接受 ALLOWED_SOURCE_URLS 内的订阅源，其余一律拒绝）
  - 下载内容校验（拒绝非 tracker 内容）
  - 原子写入（临时文件 + rename，防止中途崩溃损坏文件）
  - 文件锁防止并发运行
  - 仅保留 GitHub Raw 直链与 Pages 短链接，无 CDN/代理加速链接
  - 纯文本 .txt 直链供 BT 客户端直接订阅
"""

import os
import re
import sys
import socket
import tempfile
import time
import html
import json
import urllib.request
import urllib.error
import urllib.parse
import datetime

try:
    import fcntl
    _HAS_FCNTL = True
except ImportError:
    _HAS_FCNTL = False

# 订阅源清单：每条为 (输出文件名, 源 URL, 短名)。
# 顺序即优先级：靠前的源在合并 all 列表时优先入选。
SOURCES = [
    ("trackers_cf_best.txt", "https://cf.trackerslist.com/best.txt", "cf-best"),
    ("trackers_run_best.txt", "https://trackers.run/s/rw_up_hp_hs_v4_v6.txt", "trackersrun-best"),
    ("trackers_ngosang_best.txt", "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt", "ngosang-best"),
    ("trackers_ngosang_best_ip.txt", "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best_ip.txt", "ngosang-best-ip"),
    ("trackers_opentracker.txt", "https://raw.githubusercontent.com/1265578519/OpenTracker/refs/heads/master/tracker.txt", "opentracker"),
]

# 白名单：仅接受 SOURCES 中声明的订阅源，拒绝任何其它来源的内容
ALLOWED_SOURCE_URLS = {url for _, url, _ in SOURCES}

MAX_TRACKERS = 20   # best 存活，正好 20 条
MAX_ALL = 100       # all 合并，正好 100 条
MIN_NON_UDP_TRACKERS = 4  # best 列表保底非 UDP（http/https/wss/ws）条数，防止单一协议失效时订阅整体不可用

SHORT_LINKS = [
    ("alive", "核心订阅", "存活 Tracker（活性测试+综合评分，推荐）",
     "https://pmwiu.github.io/{repo}/alive.txt"),
    ("all", "合并总表", "合并去重总表",
     "https://pmwiu.github.io/{repo}/merged.txt"),
]

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "trackers")
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports")
RUN_SUMMARY_FILE = os.path.join(REPORTS_DIR, "run_summary.json")
BACKUP_DIR = os.path.join(OUTPUT_DIR, "backup")
INVALID_LINES_LOG = os.path.join(PROJECT_ROOT, "invalid_lines.log")
PAGES_DIR = os.path.join(PROJECT_ROOT, "docs")
SHORT_LINKS_DIR = os.path.join(PAGES_DIR, "s")
MERGED_FILE = "trackers_merged.txt"
ALIVE_FILE = "trackers_alive.txt"
DEAD_FILE = "trackers_dead.txt"
LOCK_FILE = os.path.join(PROJECT_ROOT, ".update.lock")

# 已下线的订阅源短名（用于主动清理其残留文件）
REMOVED_SOURCE_NAMES = [
    "adysec_best", "adysec_http", "adysec_https", "adysec_udp", "adysec_wss",
    "adysec_all", "anime_best", "anime_ip", "ultimate", "ngosang_ip",
    "ngosang_i2p", "ngosang_ygg", "ngosang_all_ip", "ngosang_ygg_ip",
    "ngosang_all", "pkgforge_all", "pkgforge_general", "cf_all",
]

LEGACY_FILES = [
    os.path.join(OUTPUT_DIR, "trackers_all.txt"),
    os.path.join(OUTPUT_DIR, "trackers_run.txt"),
    os.path.join(OUTPUT_DIR, "trackers_best.txt"),
    os.path.join(PAGES_DIR, "full.txt"),
    os.path.join(PAGES_DIR, "best.txt"),
    os.path.join(SHORT_LINKS_DIR, "http.html"),
    os.path.join(SHORT_LINKS_DIR, "full.html"),
    os.path.join(SHORT_LINKS_DIR, "run.html"),
    os.path.join(SHORT_LINKS_DIR, "repo.html"),
    os.path.join(SHORT_LINKS_DIR, "best.html"),
    os.path.join(SHORT_LINKS_DIR, "ngosang-ip.html"),
    os.path.join(SHORT_LINKS_DIR, "alive-cdn.html"),
    os.path.join(SHORT_LINKS_DIR, "all-cdn.html"),
    os.path.join(SHORT_LINKS_DIR, "all-fastly.html"),
    os.path.join(SHORT_LINKS_DIR, "all-gcore.html"),
    os.path.join(SHORT_LINKS_DIR, "all-proxy.html"),
    # 已移除的旧订阅源（XIU2 / newtrackon）
    os.path.join(OUTPUT_DIR, "trackers_xiu2.txt"),
    os.path.join(OUTPUT_DIR, "trackers_newtrackon.txt"),
    os.path.join(PAGES_DIR, "xiu2.txt"),
    os.path.join(PAGES_DIR, "newtrackon.txt"),
    os.path.join(SHORT_LINKS_DIR, "xiu2.html"),
    os.path.join(SHORT_LINKS_DIR, "newtrackon.html"),
    # 旧的 all 三源（已替换为 best 源）
    os.path.join(OUTPUT_DIR, "trackers_cf.txt"),
    os.path.join(OUTPUT_DIR, "trackers_adysec.txt"),
    os.path.join(OUTPUT_DIR, "trackers_ngosang.txt"),
    os.path.join(PAGES_DIR, "cf.txt"),
    os.path.join(PAGES_DIR, "adysec.txt"),
    os.path.join(PAGES_DIR, "ngosang.txt"),
    os.path.join(SHORT_LINKS_DIR, "cf.html"),
    os.path.join(SHORT_LINKS_DIR, "adysec.html"),
    os.path.join(SHORT_LINKS_DIR, "ngosang.html"),
    # 已下线的订阅源文件（脚本会主动清理，避免残留）
    *[os.path.join(OUTPUT_DIR, f"trackers_{n}.txt") for n in REMOVED_SOURCE_NAMES],
    *[os.path.join(PAGES_DIR, f"{n}.txt") for n in REMOVED_SOURCE_NAMES],
]

TIMEOUT = 30
MAX_RETRIES = 3
RETRY_DELAY = 5

# 合法 tracker URL 模式
TRACKER_PATTERN = re.compile(
    r'^(udp|http|https|wss|ws)://[^\s/$.?#].[^\s]*$', re.IGNORECASE
)

# 换行常量（用 chr 避免源码中出现字面反斜杠 n，防止传输时被转义破坏）
NL = chr(10)


def get_repo():
    repo = os.environ.get("GITHUB_REPOSITORY", "").strip()
    return repo if repo else "Pmwiu/Tracker-List"


BLACKLIST_FILE = os.path.join(PROJECT_ROOT, "blacklist.txt")


def load_blacklist():
    """读取 blacklist.txt，返回需排除的域名集合（小写，精确匹配主机名）。"""
    blacklist = set()
    if not os.path.exists(BLACKLIST_FILE):
        return blacklist
    with open(BLACKLIST_FILE, "r", encoding="utf-8") as f:
        for line in f:
            entry = line.strip().lower()
            if entry and not entry.startswith("#"):
                blacklist.add(entry)
    return blacklist


def load_url_blacklist():
    """读取 trackers/blacklist_dynamic.txt，返回需排除的精确 URL 集合。"""
    path = os.path.join(OUTPUT_DIR, "blacklist_dynamic.txt")
    if not os.path.exists(path):
        return set()
    urls = set()
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                urls.add(line)
    return urls


def write_run_summary(status, duration_sec, source_stats, merged_lines, failed_sources):
    """生成 reports/run_summary.json 运行摘要。"""
    os.makedirs(REPORTS_DIR, exist_ok=True)
    summary = {
        "timestamp": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "status": status,
        "duration_sec": duration_sec,
        "sources": source_stats,
        "merged_lines": merged_lines,
        "alive_lines": None,
        "failed_sources": failed_sources,
    }
    atomic_write(RUN_SUMMARY_FILE, json.dumps(summary, ensure_ascii=False, indent=2) + NL)


def _backup_file(filename):
    """把成功生成的源文件复制到 trackers/backup/ 作为降级备份。"""
    src = os.path.join(OUTPUT_DIR, filename)
    if not os.path.exists(src):
        return
    os.makedirs(BACKUP_DIR, exist_ok=True)
    with open(src, "r", encoding="utf-8") as f:
        content = f.read()
    atomic_write(os.path.join(BACKUP_DIR, filename), content)


def _load_backup(filename):
    """从备份文件读取 tracker 列表；无备份返回 None。"""
    dst = os.path.join(BACKUP_DIR, filename)
    if not os.path.exists(dst):
        return None
    trackers = set()
    with open(dst, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                trackers.add(line)
    return sorted(trackers) if trackers else None


def _log_invalid_line(line):
    """把无效行追加写入 invalid_lines.log（补丁 E）。"""
    try:
        with open(INVALID_LINES_LOG, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except OSError:
        pass


def acquire_lock():
    """获取文件锁，防止并发运行。超时10秒。跨平台兼容。"""
    os.makedirs(os.path.dirname(LOCK_FILE), exist_ok=True)
    deadline = time.time() + 10
    lock_fd = None

    while time.time() < deadline:
        if _HAS_FCNTL:
            # Linux/macOS: fcntl  flock
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
            # Windows: 原子创建锁文件（O_CREAT|O_EXCL 保证原子性）
            try:
                fd = os.open(LOCK_FILE, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                with os.fdopen(fd, "w") as f:
                    f.write(str(os.getpid()))
                # 保存 fd 以便释放时删除文件
                return LOCK_FILE  # 返回路径而非 fd，Windows 下用路径管理
            except FileExistsError:
                # 锁文件存在，检查持有进程是否还活着
                try:
                    with open(LOCK_FILE, "r") as f:
                        old_pid = f.read().strip()
                    if old_pid and old_pid.isdigit():
                        try:
                            os.kill(int(old_pid), 0)
                            # 进程还在，等待
                            time.sleep(0.5)
                            continue
                        except (OSError, ValueError):
                            pass  # 进程已结束，抢占锁
                    # 旧进程已结束，删除锁文件并重试
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
    """释放文件锁。"""
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
    """规范化 tracker URL：统一协议小写、补全默认端口、去除末尾斜杠。

    补全 http=80 / https=443 默认端口，使
    http://example.com/announce 与 http://example.com:80/announce 正确合并。
    """
    url = url.strip()
    if not url:
        return None
    try:
        parsed = urllib.parse.urlparse(url)
    except Exception:
        return url

    scheme = (parsed.scheme or "").lower()
    hostname = parsed.hostname
    if not hostname:
        return url

    port = parsed.port
    if port is None:
        if scheme == "http":
            port = 80
        elif scheme == "https":
            port = 443

    # IPv6 主机加括号
    host = f"[{hostname}]" if ":" in hostname else hostname
    netloc = f"{host}:{port}" if port else host
    path = parsed.path.rstrip("/")

    return urllib.parse.urlunparse(
        (scheme, netloc, path, parsed.params, parsed.query, "")
    )


def is_valid_tracker(url):
    """校验是否为合法的 tracker URL。"""
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


def _fetch(url):
    """单次抓取并返回文本响应体（非 200 视为错误）。"""
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (compatible; TrackerListBot/3.0)",
        "Accept": "text/plain,*/*",
    })
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        if resp.status != 200:
            raise urllib.error.HTTPError(url, resp.status, "Non-200", {}, None)
        return resp.read().decode("utf-8", errors="replace")


def _is_retryable(err):
    """DNS 解析失败属确定性错误，重试无意义，直接快速失败。"""
    for candidate in (getattr(err, "reason", None), err):
        if isinstance(candidate, socket.gaierror):
            return False
    return True


def mirror_urls(url):
    """返回订阅源的镜像候选地址（原始地址不可达时按顺序回退）。

    仅对白名单内的 URL 调用。raw.githubusercontent.com 地址额外支持
    raw.pmwiu.com（专属 Raw 镜像）与 jsDelivr；其余地址走 gh.pmwiu.com 代理。
    """
    candidates = []
    prefix = "https://raw.githubusercontent.com/"
    if url.startswith(prefix):
        rest = url[len(prefix):]
        candidates.append("https://raw.pmwiu.com/" + rest)
        parts = rest.split("/")
        ref_index = 2
        if len(parts) >= 6 and parts[2] == "refs" and parts[3] == "heads":
            ref_index = 4
        if len(parts) >= ref_index + 2:
            owner, repo = parts[0], parts[1]
            ref = parts[ref_index]
            path = "/".join(parts[ref_index + 1:])
            candidates.append(f"https://cdn.jsdelivr.net/gh/{owner}/{repo}@{ref}/{path}")
    candidates.append("https://gh.pmwiu.com/" + url)

    seen = set()
    ordered = []
    for c in candidates:
        if c != url and c not in seen:
            seen.add(c)
            ordered.append(c)
    return ordered


def download_trackers(url, blacklist=None, url_blacklist=None):
    """下载并校验 tracker 列表，返回去重后的排序列表。

    仅接受 ALLOWED_SOURCE_URLS 白名单内的订阅源；非白名单来源直接拒绝，
    其内容不会被下载、解析或合并。原始地址不可达时按 MIRROR_PREFIXES
    顺序回退到镜像地址。blacklist 为需排除的域名集合（小写），
    url_blacklist 为需排除的精确 URL 集合（动态黑名单）。
    """
    if url not in ALLOWED_SOURCE_URLS:
        raise RuntimeError(f"Source not in whitelist, rejected: {url}")
    blacklist = blacklist or set()
    url_blacklist = url_blacklist or set()

    raw = None
    last_error = None
    sources = [url] + mirror_urls(url)
    for index, candidate in enumerate(sources):
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                raw = _fetch(candidate)
                break
            except Exception as e:
                last_error = e
                if not _is_retryable(e):
                    break
                if attempt < MAX_RETRIES:
                    print(f"  [RETRY] {attempt}/{MAX_RETRIES} {candidate}: {e}")
                    time.sleep(RETRY_DELAY)
        if raw is not None:
            if index > 0:
                print(f"  [MIRROR] fetched via {candidate}")
            break
        if index + 1 < len(sources):
            print(f"  [MIRROR] direct fetch failed ({last_error}); trying mirror...")

    if raw is None:
        raise last_error if last_error else RuntimeError("Empty response")

    # 内容校验：拒绝明显的 HTML 错误页
    if raw.lstrip().startswith("<!DOCTYPE") or raw.lstrip().startswith("<html"):
        raise RuntimeError("Response is HTML, not tracker list")

    trackers = set()
    invalid = 0
    blacklisted = 0
    url_blacklisted = 0
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        normalized = normalize_tracker(line)
        if normalized and is_valid_tracker(normalized):
            if normalized in url_blacklist:
                url_blacklisted += 1
                continue
            host = (urllib.parse.urlparse(normalized).hostname or "").lower()
            if host and host in blacklist:
                blacklisted += 1
                continue
            trackers.add(normalized)
        else:
            invalid += 1
            _log_invalid_line(line)

    if invalid > 0:
        print(f"  [INFO] Skipped {invalid} invalid lines")
    if blacklisted > 0:
        print(f"  [INFO] Skipped {blacklisted} blacklisted lines")
    if url_blacklisted > 0:
        print(f"  [INFO] Skipped {url_blacklisted} dynamic-blacklisted lines")

    if not trackers:
        raise RuntimeError("No valid trackers found in response")

    return sorted(trackers)


def atomic_write(filepath, content):
    """原子写入：写入同目录临时文件（tempfile），fsync 后 os.replace 原子替换。"""
    dirpath = os.path.dirname(filepath) or "."
    fd, tmp_path = tempfile.mkstemp(dir=dirpath, prefix="tmp_", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline=NL) as f:
            f.write(content)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_path, filepath)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


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
    body = NL.join(trackers)
    if trackers:
        body += NL
    content = NL.join(header) + body
    atomic_write(filepath, content)


PROTOCOL_SUBLISTS = {
    "udp": "udp://",
    "http": "http://",
    "https": "https://",
    "wss": "wss://",
    "ws": "ws://",
}


def write_protocol_sublists(merged):
    """按协议拆分合并列表，生成各协议子列表（对齐国际聚合项目的多格式列表）。

    即使某协议当前没有条目也写出文件（仅含头部），保证 5 个协议订阅地址始终存在。
    """
    for name, prefix in PROTOCOL_SUBLISTS.items():
        subset = [t for t in merged if t.startswith(prefix)]
        write_trackers(
            os.path.join(OUTPUT_DIR, f"trackers_{name}.txt"),
            subset,
            extra_header=f"# 协议: {name}",
        )


def write_mirrors_file(repo):
    owner = repo.split("/")[0] if "/" in repo else repo
    repo_name = repo.split("/")[-1] if "/" in repo else repo
    pages = f"https://pmwiu.github.io/{repo_name}"
    raw_base = f"https://raw.githubusercontent.com/{owner}/{repo_name}/main"
    mirror = "https://gh.pmwiu.com"
    cf = "https://tracker.pmwiu.com"
    entries = [
        ("存活 best - Pages 短链", f"{pages}/s/alive"),
        ("存活 best - Pages 直链", f"{pages}/alive.txt"),
        ("存活 best - Raw", f"{raw_base}/trackers/trackers_alive.txt"),
        ("存活 best - 镜像代理", f"{mirror}/{raw_base}/trackers/trackers_alive.txt"),
        ("存活 best - Cloudflare Pages", f"{cf}/alive.txt"),
        ("合并 all - Pages 短链", f"{pages}/s/all"),
        ("合并 all - Pages 直链", f"{pages}/merged.txt"),
        ("合并 all - Raw", f"{raw_base}/trackers/trackers_merged.txt"),
        ("合并 all - 镜像代理", f"{mirror}/{raw_base}/trackers/trackers_merged.txt"),
        ("合并 all - Cloudflare Pages", f"{cf}/merged.txt"),
    ]
    lines = [
        "# Tracker 订阅地址清单",
        f"# Generated: {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC",
        "# 双托管：GitHub Pages/Raw + Cloudflare Pages；镜像代理：gh.pmwiu.com",
        "",
    ]
    for name, url in entries:
        lines += [f"# [{name}]", url, ""]
    atomic_write(os.path.join(OUTPUT_DIR, "MIRRORS.txt"), NL.join(lines))
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
    """从 SOURCES 动态生成 footer 中的来源链接。"""
    label_map = {
        "cf-best": "trackerslist/best",
        "trackersrun-best": "trackers.run/best",
        "ngosang-best": "ngosang/best",
        "ngosang-best-ip": "ngosang/best-ip",
        "opentracker": "OpenTracker",
    }
    parts = []
    for _, url, short_name in SOURCES:
        label = label_map.get(short_name, short_name)
        parts.append(f'<a href="{html.escape(url)}">{html.escape(label)}</a>')
    return (" &middot;" + NL + "      ").join(parts)


def generate_index_page(repo, short_links_with_urls, tracker_counts):
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    owner = (repo.split("/")[0] if "/" in repo else repo).lower()
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
    repo_name = repo.split("/")[-1]
    os.makedirs(SHORT_LINKS_DIR, exist_ok=True)
    sl = []
    for short, group, desc, template in SHORT_LINKS:
        target = template.format(repo=repo_name)
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
        "trackers_cf_best.txt": "cf_best.txt",
        "trackers_run_best.txt": "run_best.txt",
        "trackers_ngosang_best.txt": "ngosang_best.txt",
        "trackers_ngosang_best_ip.txt": "ngosang_best_ip.txt",
        "trackers_opentracker.txt": "opentracker.txt",
        "trackers_udp.txt": "udp.txt",
        "trackers_http.txt": "http.txt",
        "trackers_https.txt": "https.txt",
        "trackers_wss.txt": "wss.txt",
        "trackers_ws.txt": "ws.txt",
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
    # 无订阅源时优雅退出：不写运行摘要、不触发失败告警，等待配置新源后自动恢复
    if not SOURCES:
        print("[INFO] SOURCES is empty - no subscription sources configured.")
        print("[INFO] Add (filename, url, short_name) entries to SOURCES in "
              "scripts/update_trackers.py to enable updates.")
        return

    lock_fd = acquire_lock()
    start_time = time.time()
    source_stats = {}
    failed_names = []
    merged_lines = 0
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        repo = get_repo()
        print(f"[INFO] Repo: {repo}, Max: {MAX_TRACKERS}")
        cleanup_legacy_files()

        blacklist = load_blacklist()
        if blacklist:
            print(f"[INFO] Blacklist: {len(blacklist)} domains")
        url_blacklist = load_url_blacklist()
        if url_blacklist:
            print(f"[INFO] Dynamic blacklist: {len(url_blacklist)} URLs")

        all_merged = []          # 按源优先级（SOURCES 顺序，精选源在前）收集
        seen_merged = set()
        results = []
        failures = []

        # 硬校验：SOURCES 中任何非白名单来源都是配置错误，立即失败
        rogue = [u for _, u, _ in SOURCES if u not in ALLOWED_SOURCE_URLS]
        if rogue:
            for u in rogue:
                print(f"[ERROR] Source not in whitelist: {u}", file=sys.stderr)
            sys.exit(1)

        for filename, url, short_name in SOURCES:
            print(f"{NL}[INFO] {filename} ({short_name})")
            source_stats[short_name] = {"http_code": 0, "lines": 0, "ok": False}
            trackers = None
            try:
                trackers = download_trackers(url, blacklist=blacklist, url_blacklist=url_blacklist)
                source_stats[short_name] = {"http_code": 200, "lines": len(trackers), "ok": True}
            except Exception as e:
                # 补丁 D：下载失败或异常源 → 降级到上次成功备份
                backup = _load_backup(filename)
                if backup is not None:
                    print(f"[WARN] {filename} failed ({e}); using backup ({len(backup)} trackers)")
                    trackers = backup
                    source_stats[short_name] = {"http_code": 0, "lines": len(trackers), "ok": True}
                else:
                    print(f"[ERROR] {e}", file=sys.stderr)
                    failures.append((filename, short_name, str(e)))
                    failed_names.append(short_name)
                    continue
            write_trackers(os.path.join(OUTPUT_DIR, filename), trackers, source_url=url)
            _backup_file(filename)
            for t in trackers:
                if t in seen_merged or not t.startswith(("http://", "https://", "udp://", "wss://", "ws://")):
                    continue
                seen_merged.add(t)
                if len(all_merged) < MAX_ALL:
                    all_merged.append(t)
            results.append((filename, len(trackers)))
            print(f"[OK]   {len(trackers)} unique")

        if failures:
            print(f"{NL}[WARN] {len(failures)} source(s) failed:")
            for fn, sn, err in failures:
                print(f"  - {sn}: {err}")

        if all_merged:
            merged = sorted(all_merged)  # 已按源优先级（精选源在前）取前 MAX_ALL 条
            write_trackers(
                os.path.join(OUTPUT_DIR, MERGED_FILE), merged,
                source_url=", ".join(u for _, u, _ in SOURCES),
            )
            results.append((MERGED_FILE, len(merged)))
            merged_lines = len(merged)
            print(f"{NL}[OK]   merged: {len(merged)}")
            write_protocol_sublists(merged)
        else:
            print("[ERROR] No trackers downloaded from any source!", file=sys.stderr)
            sys.exit(1)

        write_mirrors_file(repo)
        generate_pages(repo, results)
        sync_plain_text_files()

        print(f"{NL}===== Summary =====")
        for n, c in results:
            print(f"  {n}: {c}")
        print(f"  alive capped at {MAX_TRACKERS} after test+sort")
        if failures:
            print(f"  FAILED SOURCES: {len(failures)}")
        print("===================")
    finally:
        status = "success" if (not failed_names and merged_lines > 0) else "failure"
        write_run_summary(status, round(time.time() - start_time, 1),
                          source_stats, merged_lines, failed_names)
        release_lock(lock_fd)


if __name__ == "__main__":
    main()
