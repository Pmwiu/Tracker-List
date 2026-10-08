// ==========================================================================
// tracker-proxy — Tracker-List 订阅短链接与加速网关
// 路由: tracker.pmwiu.com/*
//
// 短链接规范（全部 txt）:
//   /best.txt  /alive.txt   → trackers_alive.txt   (best, 20 条, 协议多样性配额)
//   /all.txt                → trackers_all.txt     (all, 存活去重, 完整 announce)
//   /merged.txt             → trackers_merged.txt  (原始候选池)
//   /p/{udp,http,https,wss,ws}.txt → 协议子列表
//   /src/{<任意源短名>}.txt → 源列表（通用命名空间，随 SOURCES 自动扩展）
//   /jsd/<上述任意路径>    → jsDelivr 加速镜像（失败回退 Raw）
//   / 或 /index.html        → 订阅主页(HTML)
//   /s/alive  /s/all        → Pages 短跳(HTML)
//   /mirrors.txt            → 全部订阅地址清单
//   /stats                  → 访问统计(JSON, 单 isolate 内存, 冷启动重置)
// 内容回退链: raw.githubusercontent → Cloudflare Pages → GitHub Pages
// 简单限流: 每 IP 每 60s 最多 120 次, 超限返回 429
// ==========================================================================

const REPO_RAW = "https://raw.githubusercontent.com/Pmwiu/Tracker-List/main";
const CF_PAGES = "https://tracker-list-edj.pages.dev";
const GH_PAGES = "https://pmwiu.github.io/Tracker-List";
const JSD_BASE = "https://cdn.jsdelivr.net/gh/Pmwiu/Tracker-List@main";

const RATE_WINDOW_MS = 60_000;
const RATE_LIMIT = 120;

const ALIASES = {
  "alive.txt": "trackers/trackers_alive.txt",
  "best.txt": "trackers/trackers_alive.txt",
  "all.txt": "trackers/trackers_all.txt",
  "merged.txt": "trackers/trackers_merged.txt",
  "udp.txt": "trackers/trackers_udp.txt",
  "http.txt": "trackers/trackers_http.txt",
  "https.txt": "trackers/trackers_https.txt",
  "wss.txt": "trackers/trackers_wss.txt",
  "ws.txt": "trackers/trackers_ws.txt",
  "cf_best.txt": "trackers/trackers_cf_best.txt",
  "ngosang_best.txt": "trackers/trackers_ngosang_best.txt",
  "mirrors.txt": "trackers/MIRRORS.txt",
  "index.html": "docs/index.html",
  "s/alive": "docs/s/alive.html",
  "s/all": "docs/s/all.html",
  "health.json": "reports/health.json",
};

// ---- 简单限流与访问统计（单 isolate 内存，冷启动后重置）----
const buckets = new Map(); // ip -> { windowStart, count }
const stats = {
  startedAt: 0, // 在首次请求时惰性初始化（模块顶层 Date.now() 在部分 isolate 上可能为 0）
  requests: 0,
  rateLimited: 0,
  routes: {},
};

function clientIP(request) {
  return request.headers.get("CF-Connecting-IP") || "unknown";
}

function rateLimited(ip) {
  const now = Date.now();
  let b = buckets.get(ip);
  if (!b || now - b.windowStart >= RATE_WINDOW_MS) {
    b = { windowStart: now, count: 0 };
    buckets.set(ip, b);
  }
  b.count += 1;
  return b.count > RATE_LIMIT;
}

function normalize(pathname) {
  let p = decodeURIComponent(pathname).replace(/^\/+|\/+$/g, "").toLowerCase();
  if (p === "" || p === "s" || p === "index.htm") p = "index.html";
  return p;
}

function resolveRepoPath(p) {
  if (ALIASES[p]) return ALIASES[p];
  let m = p.match(/^p\/([a-z0-9_]+)\.txt$/);
  if (m) return "trackers/trackers_" + m[1] + ".txt";
  m = p.match(/^src\/([a-z0-9_]+)\.txt$/);
  if (m) return "trackers/trackers_" + m[1] + ".txt";
  return "docs/" + p; // 兜底: docs/ 镜像内容
}

function contentType(repoPath) {
  if (repoPath.endsWith(".html")) return "text/html; charset=utf-8";
  if (repoPath.endsWith(".json")) return "application/json; charset=utf-8";
  return "text/plain; charset=utf-8";
}

async function tryFetch(url, ttl, expectText) {
  const resp = await fetch(url, { cf: { cacheEverything: true, cacheTtl: ttl } });
  if (!resp.ok) return null;
  const text = await resp.text();
  if (expectText) {
    // Pages 对未知 .txt 路径回退 index.html，且 _headers 会把 content-type
    // 伪装成 text/plain，故必须按正文特征识别 HTML 回退页
    const head = text.trimStart().toLowerCase();
    if (head.startsWith("<!doctype") || head.startsWith("<html") || head.startsWith("<!DOCTYPE")) {
      return null;
    }
  }
  return text;
}

function respond(repoPath, upstream, body, isHead) {
  const headers = {
    "content-type": contentType(repoPath),
    "cache-control": "no-cache",
    "access-control-allow-origin": "*",
    "access-control-allow-methods": "GET, HEAD, OPTIONS",
    "x-tracker-upstream": upstream,
  };
  return new Response(isHead ? null : body, { status: 200, headers });
}

async function handle(request) {
  const url = new URL(request.url);
  const isHead = request.method === "HEAD";

  // CORS 预检
  if (request.method === "OPTIONS") {
    return new Response(null, {
      status: 204,
      headers: {
        "access-control-allow-origin": "*",
        "access-control-allow-methods": "GET, HEAD, OPTIONS",
        "access-control-max-age": "86400",
      },
    });
  }

  const ip = clientIP(request);
  if (rateLimited(ip)) {
    stats.rateLimited += 1;
    return new Response("rate limited\n", {
      status: 429,
      headers: { "retry-after": "60", "access-control-allow-origin": "*" },
    });
  }
  stats.requests += 1;
  if (!stats.startedAt) stats.startedAt = Date.now();

  const p = normalize(url.pathname);

  // ---- 访问统计 ----
  if (p === "stats" || p === "stats.json") {
    const body = JSON.stringify({
      ...stats,
      now: new Date().toISOString(),
      uptimeSec: Math.round((Date.now() - stats.startedAt) / 1000),
      rateWindowSec: RATE_WINDOW_MS / 1000,
      rateLimitPerIP: RATE_LIMIT,
      distinctClients: buckets.size,
      routes: stats.routes,
    }, null, 2) + "\n";
    return new Response(body, {
      headers: { "content-type": "application/json; charset=utf-8", "access-control-allow-origin": "*" },
    });
  }

  stats.routes[p] = (stats.routes[p] || 0) + 1;

  // ---- jsDelivr 加速镜像: /jsd/<任意短链接> ----
  if (p.startsWith("jsd/")) {
    const repoPath = resolveRepoPath(normalize("/" + p.slice(4)));
    const expectText = !repoPath.endsWith(".html");
    for (const t of [JSD_BASE + "/" + repoPath, REPO_RAW + "/" + repoPath]) {
      try {
        const body = await tryFetch(t, 300, expectText);
        if (body !== null) return respond(repoPath, t, body, isHead);
      } catch (e) {}
    }
    return new Response("jsdelivr mirror unavailable\n", { status: 502 });
  }

  // ---- 常规短链接: raw → CF Pages → GH Pages ----
  const repoPath = resolveRepoPath(p);
  const isHtml = repoPath.endsWith(".html");
  const ttl = isHtml ? 60 : 300;
  const targets = [REPO_RAW + "/" + repoPath];
  // Pages 站点以 docs/ 为根，仅 docs/ 内容有 Pages 镜像；trackers/、reports/ 仅存于 Raw
  if (repoPath.startsWith("docs/")) {
    const pagesPath = repoPath.replace(/^docs\//, "");
    targets.push(CF_PAGES + "/" + pagesPath, GH_PAGES + "/" + pagesPath);
  }
  let notFound = false;
  for (const t of targets) {
    try {
      const body = await tryFetch(t, ttl, !isHtml);
      if (body !== null) return respond(repoPath, t, body, isHead);
      notFound = true;
    } catch (e) {}
  }
  return new Response(notFound ? "not found\n" : "upstream unavailable\n",
    { status: notFound ? 404 : 502 });
}

addEventListener("fetch", (event) => { event.respondWith(handle(event.request)); });
