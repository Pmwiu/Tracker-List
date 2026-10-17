// ==========================================================================
// tracker-proxy — Tracker-List 订阅短链接与加速网关（ES Module Worker）
// 路由: tracker.pmwiu.com/*
//
// 端点:
//   /all.txt -> trackers_all.txt | /merged.txt -> trackers_merged.txt
//   /p/<proto>.txt | /src/<name>.txt | /jsd/<路径> (jsDelivr 加速)
//   / 或 /index.html | /s/all | /mirrors.txt
//   /health -> 200 ok / 502 degraded（探上游，供监控）
//   /stats  -> 访问统计（单 isolate 内存，冷启动重置）
// 稳定性:
//   - 上游 fetch 带超时(AbortController)；限流桶/路由表有界(防内存泄漏)
//   - KV(CACHE) 存 last-known-good：上游全挂时返回缓存，保证订阅端点可用
//   - 每日 Cron 预热 KV，即使上游长时间不可用也有 ≤24h 的新鲜数据
//   - txt 响应 max-age=300 + stale-while-revalidate，降低上游压力与尾延迟
// 内容回退链: raw → CF Pages → GH Pages → KV 缓存
// ==========================================================================

const REPO_RAW = "https://raw.githubusercontent.com/Pmwiu/Tracker-List/main";
const CF_PAGES = "https://tracker-list-edj.pages.dev";
const GH_PAGES = "https://pmwiu.github.io/Tracker-List";
const JSD_BASE = "https://cdn.jsdelivr.net/gh/Pmwiu/Tracker-List@main";

const RATE_WINDOW_MS = 60_000;
const RATE_LIMIT = 120;
const MAX_BUCKETS = 50_000;
const MAX_ROUTES = 500;
const UPSTREAM_TIMEOUT_MS = 4000;
const KV_TTL_SEC = 7 * 86400;      // last-known-good 保留 7 天
// 每日 Cron 预热的关键文件
const PREWARM_KEYS = [
  "trackers/trackers_all.txt",
  "trackers/trackers_merged.txt",
  "trackers/trackers_udp.txt",
  "trackers/trackers_http.txt",
  "trackers/trackers_https.txt",
  "trackers/trackers_wss.txt",
  "trackers/trackers_ws.txt",
];

const ALIASES = {
  "all.txt": "trackers/trackers_all.txt",
  "merged.txt": "trackers/trackers_merged.txt",
  "udp.txt": "trackers/trackers_udp.txt",
  "http.txt": "trackers/trackers_http.txt",
  "https.txt": "trackers/trackers_https.txt",
  "wss.txt": "trackers/trackers_wss.txt",
  "ws.txt": "trackers/trackers_ws.txt",
  "ngosang_all.txt": "trackers/trackers_ngosang_all.txt",
  "ngosang_all_ip.txt": "trackers/trackers_ngosang_all_ip.txt",
  "ngosang_yggdrasil_ip.txt": "trackers/trackers_ngosang_yggdrasil_ip.txt",
  "cf_all.txt": "trackers/trackers_cf_all.txt",
  "adysec_all.txt": "trackers/trackers_adysec_all.txt",
  "kris3713_ultimate.txt": "trackers/trackers_kris3713_ultimate.txt",
  "entr0pia_https.txt": "trackers/trackers_entr0pia_https.txt",
  "mirrors.txt": "trackers/MIRRORS.txt",
  "index.html": "docs/index.html",
  "s/all": "docs/s/all.html",
  "health.json": "reports/health.json",
};

const buckets = new Map();
const stats = { startedAt: 0, requests: 0, rateLimited: 0, routes: {} };

function clientIP(request) {
  return request.headers.get("CF-Connecting-IP") || "unknown";
}

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

function cacheControlFor(repoPath) {
  if (repoPath.endsWith(".html")) return "public, max-age=60, stale-while-revalidate=600";
  return "public, max-age=300, stale-while-revalidate=3600";
}

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
    if (head.startsWith("<!doctype") || head.startsWith("<html")) return null;
  }
  return text;
}

function respond(repoPath, upstream, body, isHead, stale) {
  const headers = {
    "content-type": contentType(repoPath),
    "cache-control": cacheControlFor(repoPath),
    "access-control-allow-origin": "*",
    "access-control-allow-methods": "GET, HEAD, OPTIONS",
    "x-tracker-upstream": upstream,
  };
  if (stale) headers["x-tracker-stale"] = "1";
  return new Response(isHead ? null : body, { status: 200, headers });
}

// ---- KV last-known-good（env.CACHE 未绑定时全部 no-op，向后兼容）----
async function kvPut(env, key, value) {
  if (!env || !env.CACHE) return;
  try { await env.CACHE.put(key, value, { expirationTtl: KV_TTL_SEC }); } catch (e) {}
}
async function kvGet(env, key) {
  if (!env || !env.CACHE) return null;
  try { return await env.CACHE.get(key); } catch (e) { return null; }
}

async function handle(request, env, ctx) {
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
      status: 429, headers: { "retry-after": "60", "access-control-allow-origin": "*" },
    });
  }
  stats.requests += 1;
  if (!stats.startedAt) stats.startedAt = Date.now();

  const p = normalize(url.pathname);

  if (p === "stats" || p === "stats.json") {
    const body = JSON.stringify({
      ...stats, now: new Date().toISOString(),
      uptimeSec: Math.round((Date.now() - stats.startedAt) / 1000),
      rateWindowSec: RATE_WINDOW_MS / 1000, rateLimitPerIP: RATE_LIMIT,
      distinctClients: buckets.size, routes: stats.routes,
    }, null, 2) + "\n";
    return new Response(body, {
      headers: { "content-type": "application/json; charset=utf-8",
                 "cache-control": "no-store", "access-control-allow-origin": "*" },
    });
  }

  if (p === "health") {
    let ok = false, by = "";
    try {
      const body = await tryFetch(REPO_RAW + "/trackers/trackers_all.txt", 30, true);
      if (body !== null) { ok = true; by = REPO_RAW; }
      else { const c = await kvGet(env, "trackers/trackers_all.txt"); if (c !== null) { ok = true; by = "kv"; } }
    } catch (e) {}
    const payload = JSON.stringify({
      status: ok ? "ok" : "degraded", upstream: by,
      uptimeSec: Math.round((Date.now() - (stats.startedAt || Date.now())) / 1000),
      requests: stats.requests, now: new Date().toISOString(),
    }, null, 2) + "\n";
    return new Response(payload, {
      status: ok ? 200 : 502,
      headers: { "content-type": "application/json; charset=utf-8",
                 "cache-control": "no-store", "access-control-allow-origin": "*" },
    });
  }

  noteRoute(stats.routes, p, MAX_ROUTES);

  // ---- jsDelivr 加速镜像 ----
  if (p.startsWith("jsd/")) {
    const repoPath = resolveRepoPath(normalize("/" + p.slice(4)));
    const expectText = !repoPath.endsWith(".html");
    for (const t of [JSD_BASE + "/" + repoPath, REPO_RAW + "/" + repoPath]) {
      try {
        const body = await tryFetch(t, 300, expectText);
        if (body !== null) { if (ctx) ctx.waitUntil(kvPut(env, repoPath, body)); return respond(repoPath, t, body, isHead); }
      } catch (e) {}
    }
    const cached = await kvGet(env, repoPath);
    if (cached !== null) return respond(repoPath, "kv-cache", cached, isHead, true);
    return new Response("jsdelivr mirror unavailable\n", { status: 502 });
  }

  // ---- 常规短链接: raw -> CF Pages -> GH Pages -> KV ----
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
      if (body !== null) { if (ctx) ctx.waitUntil(kvPut(env, repoPath, body)); return respond(repoPath, t, body, isHead); }
      notFound = true;
    } catch (e) {}
  }
  const cached = await kvGet(env, repoPath);
  if (cached !== null) return respond(repoPath, "kv-cache", cached, isHead, true);
  return new Response(notFound ? "not found\n" : "upstream unavailable\n",
    { status: notFound ? 404 : 502 });
}

// 每日 Cron 预热：抓关键文件写入 KV，保证上游抖动时仍可降级服务
async function preWarm(env) {
  for (const repoPath of PREWARM_KEYS) {
    try {
      const body = await tryFetch(REPO_RAW + "/" + repoPath, 300, true);
      if (body !== null) await kvPut(env, repoPath, body);
    } catch (e) {}
  }
}

export default {
  async fetch(request, env, ctx) { return handle(request, env, ctx); },
  async scheduled(event, env, ctx) { ctx.waitUntil(preWarm(env)); },
};

export { pruneBuckets, noteRoute, normalize, resolveRepoPath, contentType,
         cacheControlFor, fetchWithTimeout, tryFetch, handle, preWarm,
         MAX_BUCKETS, MAX_ROUTES, UPSTREAM_TIMEOUT_MS, PREWARM_KEYS };
