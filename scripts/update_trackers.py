#!/usr/bin/env python3
"""
自动从订阅源下载 Tracker 列表，合并去重后写入本地仓库，
并生成 GitHub Pages 短链接重定向页面、服务主页与纯文本订阅文件。

订阅源（8 个 best 精选源，SOURCES 顺序即优先级）:
  - ngosang/trackerslist trackers_best.txt（经 jsDelivr 加速）
  - cf.trackerslist.com/best.txt
  - gonghailink / panda-men / gspu / linux-jin / AlphaCatMeow（ngosang 各 fork 的 trackers_best.txt）
  - pexcn/daily trackerlist-best.txt
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
    ("trackers_ngosang_best.txt", "https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_best.txt", "ngosang-best"),
    ("trackers_cf_best.txt", "https://cf.trackerslist.com/best.txt", "cf-best"),
    ("trackers_gonghailink_best.txt", "https://raw.githubusercontent.com/gonghailink/trackerslist/master/trackers_best.txt", "gonghailink-best"),
    ("trackers_pandamen_best.txt", "https://raw.githubusercontent.com/panda-men/trackerslist/master/trackers_best.txt", "pandamen-best"),
    ("trackers_gspu_best.txt", "https://raw.githubusercontent.com/gspu/trackerslist/master/trackers_best.txt", "gspu-best"),
    ("trackers_linuxjin_best.txt", "https://raw.githubusercontent.com/linux-jin/trackerslist/master/trackers_best.txt", "linuxjin-best"),
    ("trackers_alphacatmeow_best.txt", "https://raw.githubusercontent.com/AlphaCatMeow/trackerslist/master/trackers_best.txt", "alphacatmeow-best"),
    ("trackers_pexcn_best.txt", "https://raw.githubusercontent.com/pexcn/daily/gh-pages/trackerlist/trackerlist-best.txt", "pexcn-best"),
]

# 白名单：仅接受 SOURCES 中声明的订阅源，拒绝任何其它来源的内容
ALLOWED_SOURCE_URLS = {url for _, url, _ in SOURCES}

MAX_TRACKERS = 20   # best 存活，正好 20 条
MAX_ALL = 100       # all 合并，正好 100 条
MIN_NON_UDP_TRACKERS = 4  # best 列表保底非 UDP（http/https/wss/ws）条数，防止单一协议失效时订阅整体不可用

# all 列表协议保底：稀有协议（wss/ws）只要存在就保留；常见协议保证最小席位，其余由轮转填充
ALL_PROTOCOL_FLOORS = {"wss": 1, "ws": 1, "https": 15, "http": 15, "udp": 20}

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
    "run_best", "ngosang_best_ip", "opentracker",
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
    """返回订阅源的镜像候选地址（原始地址不可达时回退）。

    仅对白名单内的 URL 调用。raw.githubusercontent.com 地址回退到
    jsDelivr（cdn.jsdelivr.net/gh/<owner>/<repo>@<ref>/<path>）。
    """
    candidates = []
    prefix = "https://raw.githubusercontent.com/"
    if url.startswith(prefix):
        rest = url[len(prefix):]
        parts = rest.split("/")
        ref_index = 2
        if len(parts) >= 6 and parts[2] == "refs" and parts[3] == "heads":
            ref_index = 4
        if len(parts) >= ref_index + 2:
            owner, repo = parts[0], parts[1]
            ref = parts[ref_index]
            path = "/".join(parts[ref_index + 1:])
            candidates.append(f"https://cdn.jsdelivr.net/gh/{owner}/{repo}@{ref}/{path}")

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
    """写入纯 tracker 列表：每行一个 tracker，无注释头、无空行。

    source_url / extra_header 仅为兼容旧调用签名保留，不再写入文件内容。
    """
    content = NL.join(trackers)
    if trackers:
        content += NL
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

    每个协议都写出文件：有条目时为纯 tracker 列表，无条目时为空文件，
    保证 5 个协议订阅地址始终存在。
    """
    for name, prefix in PROTOCOL_SUBLISTS.items():
        subset = [t for t in merged if t.startswith(prefix)]
        write_trackers(os.path.join(OUTPUT_DIR, f"trackers_{name}.txt"), subset)


def write_mirrors_file(repo):
    """生成完整订阅地址清单：短链接（Worker）、jsDelivr 加速、双托管直链。

    首页只展示短链接；本文件是全量参考（含长链接与镜像）。
    """
    owner = repo.split("/")[0] if "/" in repo else repo
    repo_name = repo.split("/")[-1] if "/" in repo else repo
    pages = f"https://pmwiu.github.io/{repo_name}"
    cf_pages = "https://tracker-list-edj.pages.dev"
    raw_base = f"https://raw.githubusercontent.com/{owner}/{repo_name}/main"
    jsd_base = f"https://cdn.jsdelivr.net/gh/{owner}/{repo_name}@main"
    cf = "https://tracker.pmwiu.com"

    def block(title, pairs):
        out = [f"# === {title} ==="]
        for name, url in pairs:
            out += [f"# [{name}]", url]
        out.append("")
        return out

    lines = [
        "# Tracker 订阅地址清单",
        f"# Generated: {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC",
        "# 短链接网关: tracker.pmwiu.com (Cloudflare Worker)；加速: /jsd/ 前缀走 jsDelivr",
        "# 双托管: GitHub Pages + Cloudflare Pages (tracker-list-edj.pages.dev)",
        "",
    ]
    lines += block("best 精选 (trackers_alive.txt)", [
        ("短链接", f"{cf}/best.txt"),
        ("加速短链接 (jsDelivr)", f"{cf}/jsd/best.txt"),
        ("兼容短链接", f"{cf}/alive.txt"),
        ("Pages 短跳", f"{pages}/s/alive"),
        ("Pages 直链", f"{pages}/alive.txt"),
        ("Cloudflare Pages 直链", f"{cf_pages}/alive.txt"),
        ("GitHub Raw", f"{raw_base}/trackers/trackers_alive.txt"),
        ("jsDelivr 直链", f"{jsd_base}/trackers/trackers_alive.txt"),
    ])
    lines += block("all 合并 (trackers_merged.txt)", [
        ("短链接", f"{cf}/all.txt"),
        ("加速短链接 (jsDelivr)", f"{cf}/jsd/all.txt"),
        ("兼容短链接", f"{cf}/merged.txt"),
        ("Pages 短跳", f"{pages}/s/all"),
        ("Pages 直链", f"{pages}/merged.txt"),
        ("Cloudflare Pages 直链", f"{cf_pages}/merged.txt"),
        ("GitHub Raw", f"{raw_base}/trackers/trackers_merged.txt"),
        ("jsDelivr 直链", f"{jsd_base}/trackers/trackers_merged.txt"),
    ])
    proto_pairs = []
    for proto in PROTOCOL_SUBLISTS:
        proto_pairs += [
            (f"{proto} 短链接", f"{cf}/p/{proto}.txt"),
            (f"{proto} 加速", f"{cf}/jsd/p/{proto}.txt"),
        ]
    lines += block("按协议 /p/<协议>.txt", proto_pairs)
    src_pairs = []
    for filename, url, short_name in SOURCES:
        base = filename[:-4].replace("trackers_", "")
        src_pairs += [
            (f"{short_name} 短链接", f"{cf}/src/{base}.txt"),
            (f"{short_name} 加速", f"{cf}/jsd/src/{base}.txt"),
        ]
    lines += block("按源 /src/<源>.txt", src_pairs)
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
        "ngosang-best": "ngosang/best",
        "cf-best": "trackerslist/best",
        "gonghailink-best": "gonghailink/best",
        "pandamen-best": "panda-men/best",
        "gspu-best": "gspu/best",
        "linuxjin-best": "linux-jin/best",
        "alphacatmeow-best": "AlphaCatMeow/best",
        "pexcn-best": "pexcn/daily",
    }
    parts = []
    for _, url, short_name in SOURCES:
        label = label_map.get(short_name, short_name)
        parts.append(f'<a href="{html.escape(url)}">{html.escape(label)}</a>')
    return (" &middot;" + NL + "      ").join(parts)


def generate_index_page(repo, short_links_with_urls, tracker_counts):
    """生成现代化订阅主页：卡片式订阅区（短链接 + jsDelivr 加速短链接）、
    协议芯片、统计表。所有订阅入口均为 tracker.pmwiu.com 短链接（txt）。"""
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    repo_name = repo.split("/")[-1] if "/" in repo else "Tracker-List"
    short_base = "https://tracker.pmwiu.com"
    n_sources = len(SOURCES)

    def plan_card(key, name, count, desc, note):
        short = f"{short_base}/{key}.txt"
        accel = f"{short_base}/jsd/{key}.txt"
        return f'''    <div class="card">
      <div class="card-head">
        <span class="card-name">{name}</span>
        <span class="card-count">{count}</span>
      </div>
      <p class="card-desc">{desc}</p>
      <div class="link-row">
        <span class="link-label">短链接</span>
        <code class="link-url" title="{short}">{short}</code>
        <button class="copy" data-copy="{short}" type="button">复制</button>
      </div>
      <div class="link-row">
        <span class="link-label">加速短链接</span>
        <code class="link-url" title="{accel}">{accel}</code>
        <button class="copy" data-copy="{accel}" type="button">复制</button>
      </div>
      <p class="card-note">{note}</p>
    </div>'''

    cards = (
        plan_card("best", "best 精选", MAX_TRACKERS,
                  "协议级活性测试 + 多维综合评分（速度 50% + 稳定性 30% + 响应质量 20%），保底 "
                  f"{MIN_NON_UDP_TRACKERS} 条非 UDP",
                  "qBittorrent / Aria2 等客户端直接粘贴订阅")
        + "\n"
        + plan_card("all", "all 合并", MAX_ALL,
                    f"{n_sources} 个精选源按优先级合并去重",
                    "追求覆盖面的完整列表")
    )

    proto_chips = "".join(
        f'      <a class="chip" href="{short_base}/p/{p}.txt">{p}.txt</a>\n'
        for p in ("udp", "http", "https", "wss", "ws")
    )

    counts_rows = "".join(
        f'        <tr><td>{html.escape(n)}</td><td class="num">{c}</td></tr>\n'
        for n, c in tracker_counts
    )

    source_links = generate_source_links()

    css = """
  *,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
  :root{--accent:#2563eb;--ink:#111827;--sub:#6b7280;--line:#e5e7eb;--bg:#f6f7f9}
  html{-webkit-font-smoothing:antialiased}
  body{font-family:-apple-system,BlinkMacSystemFont,"SF Pro Display","Segoe UI","PingFang SC","Microsoft YaHei",Arial,sans-serif;
       background:var(--bg);color:var(--ink);line-height:1.7;font-size:15px;
       background-image:radial-gradient(1200px 400px at 50% -10%,rgba(37,99,235,.08),transparent)}
  .wrap{max-width:860px;margin:0 auto;padding:56px 24px 48px}
  header{text-align:center;margin-bottom:40px}
  .brand{font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#9ca3af;margin-bottom:14px}
  h1{font-size:36px;font-weight:700;letter-spacing:-1px;margin-bottom:10px}
  .tagline{color:var(--sub);max-width:560px;margin:0 auto;font-size:14px}
  .badges{display:flex;justify-content:center;gap:10px;margin-top:20px;flex-wrap:wrap}
  .badge{font-size:12px;color:var(--sub);background:#fff;border:1px solid var(--line);
         border-radius:999px;padding:4px 12px;display:inline-flex;align-items:center;gap:6px}
  .badge .dot{width:7px;height:7px;border-radius:50%;background:#22c55e}
  .plans{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px;margin:8px 0 24px}
  .card{background:#fff;border:1px solid var(--line);border-radius:16px;padding:24px;
        box-shadow:0 1px 2px rgba(0,0,0,.04),0 8px 24px rgba(0,0,0,.05)}
  .card-head{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:6px}
  .card-name{font-size:18px;font-weight:600}
  .card-count{font-family:"SF Mono",Menlo,Consolas,monospace;font-size:13px;color:var(--accent);
              background:rgba(37,99,235,.08);border-radius:999px;padding:2px 10px}
  .card-desc{font-size:13px;color:var(--sub);margin-bottom:16px}
  .link-row{display:flex;align-items:center;gap:10px;padding:9px 12px;border:1px solid var(--line);
            border-radius:10px;margin-bottom:10px;background:#fafafa}
  .link-label{font-size:12px;color:var(--sub);flex-shrink:0;width:64px}
  .link-url{font-family:"SF Mono",Menlo,Consolas,monospace;font-size:12.5px;color:var(--ink);
            flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .copy{flex-shrink:0;font-size:12px;color:var(--accent);background:#fff;border:1px solid var(--line);
        border-radius:8px;padding:4px 10px;cursor:pointer;transition:all .15s}
  .copy:hover{border-color:var(--accent);background:rgba(37,99,235,.06)}
  .copy.done{color:#16a34a;border-color:#16a34a}
  .card-note{font-size:12px;color:#9ca3af;margin-top:4px}
  .section{background:#fff;border:1px solid var(--line);border-radius:16px;padding:24px;margin-bottom:20px;
           box-shadow:0 1px 2px rgba(0,0,0,.04)}
  .section-title{font-size:12px;letter-spacing:2px;text-transform:uppercase;color:#9ca3af;margin-bottom:14px}
  .chips{display:flex;gap:10px;flex-wrap:wrap}
  .chip{font-family:"SF Mono",Menlo,Consolas,monospace;font-size:13px;color:var(--accent);
        background:rgba(37,99,235,.08);border-radius:10px;padding:8px 14px;text-decoration:none;
        transition:background .15s}
  .chip:hover{background:rgba(37,99,235,.16)}
  .hint{font-size:12px;color:#9ca3af;margin-top:12px}
  table{width:100%;border-collapse:collapse;font-size:13px}
  th,td{text-align:left;padding:9px 0;border-bottom:1px solid #f3f4f6}
  th{font-size:11px;letter-spacing:1px;text-transform:uppercase;color:#9ca3af;font-weight:500}
  td.num{text-align:right;font-family:"SF Mono",Menlo,monospace}
  tr:last-child td{border-bottom:none}
  footer{margin-top:32px;padding-top:20px;border-top:1px solid var(--line);font-size:12px;color:#9ca3af;text-align:center}
  footer a{color:var(--sub);text-decoration:none}
  footer a:hover{color:var(--ink)}
  footer .sources{margin-top:8px;line-height:2}
  @media (max-width:520px){.wrap{padding:40px 16px 32px}h1{font-size:28px}.link-label{display:none}}
"""

    js = """
  document.querySelectorAll('.copy').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var url = this.getAttribute('data-copy');
      var self = this;
      var done = function () {
        self.textContent = '已复制';
        self.classList.add('done');
        setTimeout(function () { self.textContent = '复制'; self.classList.remove('done'); }, 1500);
      };
      var fallback = function () {
        var ta = document.createElement('textarea');
        ta.value = url;
        ta.style.position = 'fixed';
        ta.style.opacity = '0';
        document.body.appendChild(ta);
        ta.select();
        try { document.execCommand('copy'); done(); } catch (e) {}
        document.body.removeChild(ta);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(url).then(done).catch(fallback);
      } else { fallback(); }
    });
  });
"""

    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="自动聚合、去重、协议级活性测试与综合评分排序的 BitTorrent Tracker 订阅服务">
<title>Tracker List — BitTorrent Tracker 订阅</title>
<style>{css}</style>
</head>
<body>
<div class="wrap">
  <header>
    <div class="brand">Pmwiu / {html.escape(repo_name)}</div>
    <h1>Tracker List</h1>
    <p class="tagline">自动聚合、去重、协议级活性测试与测速排序的 BitTorrent Tracker 订阅服务</p>
    <div class="badges">
      <span class="badge"><span class="dot"></span>每 6 小时自动更新</span>
      <span class="badge">{n_sources} 个精选源</span>
      <span class="badge">best 保底 {MIN_NON_UDP_TRACKERS} 条非 UDP</span>
      <span class="badge">txt 短链接直订</span>
    </div>
  </header>

  <section class="plans">
{cards}
  </section>

  <section class="section">
    <div class="section-title">按协议订阅 · /p/&lt;协议&gt;.txt</div>
    <div class="chips">
{proto_chips}    </div>
    <p class="hint">加速方式：任意短链接前加 <code>/jsd/</code> 前缀，即走 jsDelivr 全球加速镜像（如 {short_base}/jsd/p/udp.txt）。</p>
  </section>

  <section class="section">
    <div class="section-title">Statistics</div>
    <table>
      <thead><tr><th>List</th><th>Count</th></tr></thead>
      <tbody>
{counts_rows}      </tbody>
    </table>
  </section>

  <footer>
    <p>Last updated: {now}</p>
    <p class="sources">Sources: {source_links} &middot; <a href="https://github.com/{html.escape(repo)}">GitHub</a></p>
  </footer>
</div>
<script>{js}</script>
</body>
</html>
'''


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
        "trackers_ngosang_best.txt": "ngosang_best.txt",
        "trackers_cf_best.txt": "cf_best.txt",
        "trackers_gonghailink_best.txt": "gonghailink_best.txt",
        "trackers_pandamen_best.txt": "pandamen_best.txt",
        "trackers_gspu_best.txt": "gspu_best.txt",
        "trackers_linuxjin_best.txt": "linuxjin_best.txt",
        "trackers_alphacatmeow_best.txt": "alphacatmeow_best.txt",
        "trackers_pexcn_best.txt": "pexcn_best.txt",
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

        all_merged = []          # 轮转合并结果（见下方），去重后取前 MAX_ALL 条
        per_source = []          # [(short_name, sorted_trackers), ...]
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
            per_source.append((short_name, trackers))
            results.append((filename, len(trackers)))
            print(f"[OK]   {len(trackers)} unique")

        if failures:
            print(f"{NL}[WARN] {len(failures)} source(s) failed:")
            for fn, sn, err in failures:
                print(f"  - {sn}: {err}")

        # 两阶段合并：协议保底（稀有协议优先占位）+ 按源轮转填充，去重后取 MAX_ALL 条。
        # 目的：all 既保证各协议有席位（wss/ws 只要存在就保留、https/http/udp 保底），
        # 又保证每个精选源都能贡献（避免 cf/trackers.run 占满名额）。
        seen_merged = set()
        valid_prefixes = ("http://", "https://", "udp://", "wss://", "ws://")
        contribution = {}

        def _pick(t, src):
            if t in seen_merged or not t.startswith(valid_prefixes):
                return False
            seen_merged.add(t)
            all_merged.append(t)
            contribution[src] = contribution.get(src, 0) + 1
            return True

        # Phase A：协议保底（稀有协议在前，确保 wss/ws 不被常见协议挤掉）
        for proto, floor in ALL_PROTOCOL_FLOORS.items():
            got = 0
            for short_name, ts in per_source:
                for t in ts:
                    if got >= floor or len(all_merged) >= MAX_ALL:
                        break
                    if t.startswith(proto + "://") and _pick(t, short_name):
                        got += 1
                if got >= floor or len(all_merged) >= MAX_ALL:
                    break

        # Phase B：轮转填充剩余席位（按 SOURCES 顺序逐源轮流取一条）
        if len(all_merged) < MAX_ALL:
            max_len = max((len(ts) for _, ts in per_source), default=0)
            for i in range(max_len):
                for short_name, ts in per_source:
                    if i < len(ts):
                        if _pick(ts[i], short_name) and len(all_merged) >= MAX_ALL:
                            break
                if len(all_merged) >= MAX_ALL:
                    break

        proto_counts = {}
        for t in all_merged:
            p = t.split("://")[0].lower()
            proto_counts[p] = proto_counts.get(p, 0) + 1
        print(f"{NL}[INFO] all 合并贡献: " +
              ", ".join(f"{sn}={contribution.get(sn, 0)}" for _, _, sn in SOURCES))
        print(f"[INFO] all 协议分布: " +
              ", ".join(f"{p}={proto_counts.get(p, 0)}" for p in ("http", "https", "udp", "wss", "ws")))

        if all_merged:
            merged = sorted(all_merged)  # 轮转合并 + 去重，取前 MAX_ALL 条
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
