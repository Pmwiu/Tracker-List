// ==========================================================================
// tracker-proxy — Tracker-List 订阅短链接与加速网关
// 路由: tracker.pmwiu.com/*
//
// 短链接规范（全部 txt）:
//   /best.txt  /alive.txt   → trackers_alive.txt   (best, 20 条, 协议多样性配额)
//   /all.txt   /merged.txt  → trackers_merged.txt  (all, 100 条)
//   /p/{udp,http,https,wss,ws}.txt → 协议子列表
//   /src/{cf_best,run_best,ngosang_best,ngosang_best_ip,opentracker}.txt → 源列表
//   /jsd/<上述任意路径>    → jsDelivr 加速镜像（失败回退 Raw）
//   / 或 /index.html        → 订阅主页(HTML)
//   /s/alive  /s/all        → Pages 短跳(HTML)
//   /mirrors.txt            → 全部订阅地址清单
// 内容回退链: raw.githubusercontent → Cloudflare Pages → GitHub Pages
// ==========================================================================

const REPO_RAW = "https://raw.githubusercontent.com/Pmwiu/Tracker-List/main";
const CF_PAGES = "https://tracker-list-edj.pages.dev";
const GH_PAGES = "https://pmwiu.github.io/Tracker-List";
const JSD_BASE = "https://cdn.jsdelivr.net/gh/Pmwiu/Tracker-List@main";

const ALIASES = {
  "alive.txt": "trackers/trackers_alive.txt",
  "best.txt": "trackers/trackers_alive.txt",
  "merged.txt": "trackers/trackers_merged.txt",
  "all.txt": "trackers/trackers_merged.txt",
  "udp.txt": "trackers/trackers_udp.txt",
  "http.txt": "trackers/trackers_http.txt",
  "https.txt": "trackers/trackers_https.txt",
  "wss.txt": "trackers/trackers_wss.txt",
  "ws.txt": "trackers/trackers_ws.txt",
  "cf_best.txt": "trackers/trackers_cf_best.txt",
  "run_best.txt": "trackers/trackers_run_best.txt",
  "ngosang_best.txt": "trackers/trackers_ngosang_best.txt",
  "ngosang_best_ip.txt": "trackers/trackers_ngosang_best_ip.txt",
  "opentracker.txt": "trackers/trackers_opentracker.txt",
  "mirrors.txt": "trackers/MIRRORS.txt",
  "index.html": "docs/index.html",
  "s/alive": "docs/s/alive.html",
  "s/all": "docs/s/all.html",
  "health.json": "reports/health.json",
};

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

async function tryFetch(url, ttl) {
  const resp = await fetch(url, { cf: { cacheEverything: true, cacheTtl: ttl } });
  return resp.ok ? resp : null;
}

function respond(resp, repoPath, upstream) {
  const headers = {
    "content-type": contentType(repoPath),
    "cache-control": "no-cache",
    "access-control-allow-origin": "*",
    "x-tracker-upstream": upstream,
  };
  return new Response(resp.body, { status: 200, headers });
}

async function handle(request) {
  const url = new URL(request.url);
  const p = normalize(url.pathname);

  // ---- jsDelivr 加速镜像: /jsd/<任意短链接> ----
  if (p.startsWith("jsd/")) {
    const repoPath = resolveRepoPath(normalize("/" + p.slice(4)));
    for (const t of [JSD_BASE + "/" + repoPath, REPO_RAW + "/" + repoPath]) {
      try {
        const resp = await tryFetch(t, 300);
        if (resp) return respond(resp, repoPath, t);
      } catch (e) {}
    }
    return new Response("jsdelivr mirror unavailable\n", { status: 502 });
  }

  // ---- 常规短链接: raw → CF Pages → GH Pages ----
  const repoPath = resolveRepoPath(p);
  const ttl = repoPath.endsWith(".html") ? 60 : 300;
  const pagesPath = repoPath.replace(/^docs\//, ""); // Pages 站点以 docs/ 为根
  let notFound = false;
  for (const t of [REPO_RAW + "/" + repoPath, CF_PAGES + "/" + pagesPath, GH_PAGES + "/" + pagesPath]) {
    try {
      const resp = await tryFetch(t, ttl);
      if (resp) return respond(resp, repoPath, t);
      notFound = true;
    } catch (e) {}
  }
  return new Response(notFound ? "not found\n" : "upstream unavailable\n",
    { status: notFound ? 404 : 502 });
}

addEventListener("fetch", (event) => { event.respondWith(handle(event.request)); });
