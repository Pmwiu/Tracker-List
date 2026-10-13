// ==========================================================================
// tracker-proxy — Tracker-List 订阅短链接与加速网关
// 路由: tracker.pmwiu.com/*
//
// 短链接规范（全部 txt）:
//   /best.txt  /alive.txt   → trackers_alive.txt   (best, ≤25 条, 协议多样性配额)
//   /all.txt                → trackers_all.txt     (all, 存活去重, 完整 announce)
//   /reserve.txt            → trackers_reserve.txt (备选库, 自动发现候选)
//   /merged.txt             → trackers_merged.txt  (原始候选池)
//   /p/{udp,http,https,wss,ws}.txt → 协议子列表
//   /src/{<任意源短名>}.txt → 源列表（通用命名空间，随 SOURCES 自动扩展）
//   /jsd/<上述任意路径>    → jsDelivr 加速镜像（失败回退 Raw）
//   / 或 /index.html        → 订阅主页(HTML)
//   /s/alive  /s/all        → Pages 短跳(HTML)
//   /mirrors.txt            → 全部订阅地址清单
//   /health                 → 健康检查端点(200 + 上游连通性, 供监控)
//   /stats                  → 访问统计(JSON, 单 isolate 内存, 冷启动重置)
// 内容回退链: raw.githubusercontent → Cloudflare Pages → GitHub Pages
// 稳定性: 上游 fetch 带超时(AbortController)；限流桶/路由表有界(防内存泄漏)；
//         txt 响应带 max-age + stale-while-revalidate，降低上游压力与尾延迟。
// 简单限流: 每 IP 每 60s 最多 120 次, 超限返回 429
// ==========================================================================

const REPO_RAW = "https://raw.githubusercontent.com/Pmwiu/Tracker-List/main";
const CF_PAGES = "https://tracker-list-edj.pages.dev";
const GH_PAGES = "https://pmwiu.github.io/Tracker-List";
const JSD_BASE = "https://cdn.jsdelivr.net/gh/Pmwiu/Tracker-List@main";

const RATE_WINDOW_MS = 60_000;
const RATE_LIMIT = 120;
const MAX_BUCKETS = 50_000;   // 限流桶上限，超出按过期回收（防 isolate 内存无限增长）
const MAX_ROUTES = 500;       // 访问统计路由数上限，超出归并到 "other"
const UPSTREAM_TIMEOUT_MS = 4000;  // 单个上游 fetch 超时，保证回退链及时切换

const ALIASES = {
  "alive.txt": "trackers/trackers_alive.txt",
  "best.txt": "trackers/trackers_alive.txt",
  "all.txt": "trackers/trackers_all.txt",
  "reserve.txt": "trackers/trackers_reserve.txt",
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
  startedAt: 0,
  requests: 0,
  rateLimited: 0,
  routes: {},
};

function clientIP(request) {
  return request.headers.get("CF-Connecting-IP") || "unknown";
}

// 回收过期限流桶；超过 max 时按最旧优先丢弃。返回剩余条目数。
function pruneBuckets(map, now, windowMs, max) {
  for (const [k, b] of map) {
    if (now - b.windowStart >= windowMs) map.delete(k);
  }
  if (map.size > max) {
    const entries = [...map.entries()].sort((a, b) => a[1].windowStart - b[1].windowStart);
    for (let i = 0; i < entries.length && map.size > max; i++) map.delete(entries[i][0]);
  }
  return map.size;
}

function rateLimited(ip) {
  const now = Date.now();
  // 每 ~1024 次请求顺带回收一次，摊还成本，防内存泄漏
  if ((stats.requests & 1023) === 0 && buckets.size > 0) {
    pruneBuckets(buckets, now, RATE_WINDOW_MS * 2, MAX_BUCKETS);
  }
  let b = buckets.get(ip);
  if (!b || now - b.windowStart >= RATE_WINDOW_MS) {
    b = { windowStart: now, count: 0 };
    buckets.set(ip, b);
  }
  b.count += 1;
  return b.count > RATE_LIMIT;
}

// 记录路由计数，distinct 路由数超上限后归并到 "other"（防 stats.routes 无界增长）
function noteRoute(routes, path, max) {
  if (routes[path] === undefined && Object.keys(routes).length >= max) {
    routes.other = (routes.other || 0) + 1;
    return;
  }
  routes[path] = (routes[path] || 0) + 1;
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
  return "docs/" + p;
}

function contentType(repoPath) {
  if (repoPath.endsWith(".html")) return "text/html; charset=utf-8";
  if (repoPath.endsWith(".json")) return "application/json; charset=utf-8";
  return "text/plain; charset=utf-8";
}

// 缓存策略：内容每 6h 更新，txt 给 5min 客户端缓存 + 1h stale-while-revalidate，
// 大幅降低上游压力与尾延迟；html 短缓存；动态端点不缓存。
function cacheControlFor(repoPath) {
  if (repoPath.endsWith(".html")) return "public, max-age=60, stale-while-revalidate=600";
  return "public, max-age=300, stale-while-revalidate=3600";
}

// 带超时的 fetch（AbortController）；fetchImpl 可注入以便测试。
async function fetchWithTimeout(url, ms, fetchImpl) {
  const _fetch = fetchImpl || ((u, o) => fetch(u, o));
  const ctrl = new AbortController();
  const timer = setTimeout(() => ctrl.abort(), ms);
  try {
    return await _fetch(url, { signal: ctrl.signal });
  } finally {
    clearTimeout(timer);
  }
}

async function tryFetch(url, ttl, expectText) {
  const resp = await fetchWithTimeout(url, UPSTREAM_TIMEOUT_MS,
    (u, o) => fetch(u, { ...o, cf: { cacheEverything: true, cacheTtl: ttl } }));
  if (!resp.ok) return null;
  const text = await resp.text();
  if (expectText) {
    const head = text.trimStart().toLowerCase();
    if (head.startsWith("<!doctype") || head.startsWith("<html")) {
      return null;
    }
  }
  return text;
}

function respond(repoPath, upstream, body, isHead) {
  const headers = {
    "content-type": contentType(repoPath),
    "cache-control": cacheControlFor(repoPath),
    "access-control-allow-origin": "*",
    "access-control-allow-methods": "GET, HEAD, OPTIONS",
    "x-tracker-upstream": upstream,
  };
  return new Response(isHead ? null : body, { status: 200, headers });
}

async function handle(request) {
  const url = new URL(request.url);
  const isHead = request.method === "HEAD";

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
      headers: {
        "content-type": "application/json; charset=utf-8",
        "cache-control": "no-store",
        "access-control-allow-origin": "*",
      },
    });
  }

  // 健康检查：探一次 best.txt 上游，返回 200(ok)/502(degraded)
  if (p === "health") {
    let upstreamOk = false;
    let servedBy = "";
    try {
      const body = await tryFetch(REPO_RAW + "/trackers/trackers_alive.txt", 30, true);
      if (body !== null) { upstreamOk = true; servedBy = REPO_RAW; }
    } catch (e) {}
    const payload = JSON.stringify({
      status: upstreamOk ? "ok" : "degraded",
      upstream: servedBy,
      uptimeSec: Math.round((Date.now() - (stats.startedAt || Date.now())) / 1000),
      requests: stats.requests,
      now: new Date().toISOString(),
    }, null, 2) + "\n";
    return new Response(payload, {
      status: upstreamOk ? 200 : 502,
      headers: {
        "content-type": "application/json; charset=utf-8",
        "cache-control": "no-store",
        "access-control-allow-origin": "*",
      },
    });
  }

  noteRoute(stats.routes, p, MAX_ROUTES);

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

// Workers 运行时注册；在 node（测试）环境下跳过。
if (typeof addEventListener === "function") {
  addEventListener("fetch", (event) => { event.respondWith(handle(event.request)); });
}

// 导出纯函数供 node:test 测试（Workers 模块允许 export，不影响运行时）。
export { pruneBuckets, noteRoute, normalize, resolveRepoPath, contentType,
         cacheControlFor, fetchWithTimeout, handle, MAX_BUCKETS, MAX_ROUTES,
         UPSTREAM_TIMEOUT_MS };
