# tracker-proxy Worker 部署 runbook

> **状态：已于 2026-10-13 经 API 部署上线**（KV `tracker-cache` id `3b405b92…`、
> Worker `tracker-proxy` 加固 ES-Module 版、**每日 cron `17 3 * * *` 已挂**）。
> 验证：`/health` 返回 `{"status":"ok"}`、`all.txt` `cache-control: public, max-age=300,
> stale-while-revalidate=3600`、KV 绑定已挂、schedules 端点确认 cron 存在。
> 注：cron 经 wrangler 部署成功（原始 `/schedules` PUT 对 JSON body 报 10026，wrangler 走
> 正确通道）。以下步骤保留为重建/回滚 runbook。

加固版 Worker（内存泄漏修复 + 上游超时 + KV last-known-good 降级 + 每日 Cron 预热 +
`/health`）。以下步骤用于重建或回滚。

## 为什么需要你来部署

本会话给的 API token 是**只读**的（GET 可，POST/PUT 被拒："Authentication error" /
"No access to the specified resource"）。部署需要**写权限**。二选一：

### 方案 1：Cloudflare Dashboard 手动（最简单，无需 token/wrangler）

1. **建 KV 命名空间**：Dashboard → Workers & Pages → **KV** → Create namespace →
   名字 `tracker-cache`。复制它的 **Namespace ID**。
2. **编辑 Worker**：Workers & Pages → 找到 **tracker-proxy** → **Code** 标签 →
   把本目录 `tracker-proxy.js` 全部内容粘贴进去 → **Save and Deploy**。
3. **绑 KV**：该 Worker → **Settings → Variables and bindings** → KV namespace
   bindings → Add：Variable name = `CACHE`，KV namespace = `tracker-cache` → Save
   and Deploy。
4. **加 Cron**：该 Worker → **Settings → Triggers** → Cron Schedules → Add：
   `17 3 * * *`（每天 03:17 UTC）→ Save。
5. **兼容性日期**：Settings → 若提示 compatibility date，设 `2026-01-01`。

### 方案 2：wrangler CLI（需一个有写权限的 token）

1. **建一个有权限的 token**：Dashboard → My Profile → API Tokens → Create Token，
   模板 "Edit Cloudflare Workers"（含 Account → **Workers Scripts: Edit**、
   **Workers KV Storage: Edit**、Zone → DNS: Read）。
2. 建 KV 拿 id：
   ```bash
   npx wrangler kv:namespace create CACHE   # 或先建 tracker-cache，把 id 填进 wrangler.toml
   ```
   把返回的 id 填进 `wrangler.toml` 的 `id = "..."`。
3. 部署（Worker + KV 绑定 + cron 一次到位）：
   ```bash
   cd cloudflare
   CF_API_TOKEN=<新token> HTTPS_PROXY=http://127.0.0.1:3067 npx wrangler deploy
   ```
   （wrangler 读 `wrangler.toml`，含 `[[kv_namespaces]]` 与 `[triggers] crons`）

## 验证

```bash
curl -s https://tracker.pmwiu.com/health          # {"status":"ok",...}
curl -sI https://tracker.pmwiu.com/all.txt | grep -i cache-control   # public, max-age=300...
curl -s https://tracker.pmwiu.com/stats           # 访问统计
```
降级验证（可选）：临时把上游打不通时，`/all.txt` 应返回带 `x-tracker-stale: 1` 的 KV 缓存副本而非 502。

## 回滚

线上旧版代码已备份在仓库 `.cf-backup/tracker-proxy.live.js`。Dashboard 里把 Worker 代码
换回该文件内容即可回滚；或 `wrangler deployments list` / `rollback`。

## 额度（稳跑一年有余）

- Workers 免费：10 万请求/天、10ms CPU/请求。订阅端点 + 每日 1 次 cron → 用量 < 1%。
- KV 免费：10 万读/天、1000 写/天。每请求最多 1 次 KV 写（异步 waitUntil）+ 每日预热
  9 个 key → 远低于上限。
- 无需 R2（本账户 R2 未开通，需 Dashboard 绑卡启用；KV 已满足缓存/降级需求）。

## 关于 DHT / infohash 发现

DHT 需常驻 UDP 主机，Cloudflare 免费层不提供原始 UDP 套接字，且已决定放弃 DHT 节点，
故本 Worker 只做"订阅列表云端托管 + 高可用缓存"，不含 DHT 发现。
