# Tracker-List 运行手册（RUNBOOK）

面向维护者与 AI 会话的交接文档。读完本文档即可安全地操作本项目。

---

## 1. 项目是什么

生产级 BitTorrent Tracker 订阅聚合服务：每 6 小时从 14 个白名单订阅源抓取
tracker 列表，合并去重后做**协议级活性测试**（HTTP bencoded announce 校验 /
UDP connect+announce 握手 / WSS TLS），按综合评分排序，产出两个订阅计划：

| 计划 | 条数 | 文件 | 说明 |
|---|---|---|---|
| **best** 精选 | ≤ 25 | `trackers/trackers_alive.txt` | 评分前 25，含协议多样性配额（非 UDP ≥ 4）与经典高可用配额（≥ 4） |
| **all** 存活 | ≤ 59 | `trackers/trackers_all.txt` | 全部通过完整 announce 握手的存活 tracker，按评分降序 |

用户通过短链接 `https://tracker.pmwiu.com/best.txt` / `/all.txt` 订阅
（Cloudflare Worker 网关；加 `/jsd/` 前缀走 jsDelivr 全球加速）。

**技术要点：纯 Python 标准库，零外部依赖；仓库不存储任何密钥。**

## 2. 架构与数据流

```
14 个订阅源 (ngosang/cf.trackerslist/adysec/各 fork/pexcn/OpenTracker/trackers.run/i2p/yggdrasil)
        │
        ▼  (GitHub Actions, 每 6h, cron "23 */6 * * *")
scripts/update_trackers.py        抓取 → 规范化/去重 → 域名+URL 黑名单过滤
        │                         → 两阶段合并(协议保底+轮转填充, 候选池≤200)
        ▼
scripts/test_trackers.py          协议级探活 → 二轮精测 → 综合评分
        │                         (速度60%自适应 + 稳定性EMA25% + 质量15% + 经典+6)
        ▼                         → 配额选取 → alive(25) / all(59) / dead
scripts/health_check.py           本地完整性 + Raw/Pages/Worker 全链路检查
        │
        ▼  git commit & push (bot)
分发链路:
  GitHub Raw ──► Cloudflare Worker (tracker.pmwiu.com 短链接, 限流120次/60s/IP)
  GitHub Pages (docs/) ──► 回退链: raw → CF Pages → GH Pages
  jsDelivr CDN (/jsd/ 加速)
监控: reports/run_summary.json · reports/health.json · reports/source_state.json · docs/ci-diag.md
```

### 产物文件速查

| 路径 | 内容 | 谁生成 |
|---|---|---|
| `trackers/trackers_<源>.txt` | 各源原始列表 | update_trackers.py |
| `trackers/trackers_merged.txt` | 合并候选池（≤200） | update_trackers.py |
| `trackers/trackers_alive.txt` | best 25（评分排序） | test_trackers.py |
| `trackers/trackers_all.txt` | all 59（评分排序） | test_trackers.py |
| `trackers/trackers_dead.txt` | 失效/被淘汰 | test_trackers.py |
| `trackers/blacklist_dynamic.txt` | 动态黑名单（连续失效 ≥20 次） | test_trackers.py |
| `trackers/test_state.json` | 存活率 EMA + 连续失效计数 | test_trackers.py |
| `trackers/backup/` | 源文件降级备份 + 7 天 alive 历史 | 两个脚本共同维护 |
| `docs/*.txt`、`docs/index.html` | GitHub Pages 站点内容 | sync/generate |
| `trackers/MIRRORS.txt` | 全部订阅地址清单 | update_trackers.py |
| `reports/*.json` | 运行摘要 / 健康状态 / 源新鲜度 | 各脚本 |
| `docs/ci-diag.md` | 最近一次 CI 诊断日志 | workflow |

## 3. 常用操作

### 3.1 本地跑全流程（Windows）

```bash
# 建环境（仅需一次，需要 uv 或 Python 3.12）
uv venv --python 3.12 .venv

# 依次执行（CI 同款参数）
.venv\Scripts\python.exe scripts\update_trackers.py
.venv\Scripts\python.exe scripts\test_trackers.py --timeout 10 --workers 30 --max-candidates 1000
.venv\Scripts\python.exe scripts\health_check.py --skip-net      # 纯本地
.venv\Scripts\python.exe scripts\health_check.py --rounds 3      # 含网络
.venv\Scripts\python.exe scripts\monthly_subscription_check.py   # 线上地址
```

注意：本地跑会改写 `trackers/`、`docs/`、`reports/` 下的生成物。验证完后用
`git checkout -- .` 还原，保持本地克隆与远程一致（线上数据以 CI 为准）。

`test_trackers.py` 会向公网 tracker 发送 announce 探测包（30 并发），
这是**设计行为**，不是攻击。

### 3.2 触发 CI

- 自动：每 6 小时（UTC 02:23/08:23/14:23/20:23）；push 到 main 且改动
  `.github/workflows/update-trackers.yml` 或 `scripts/**` 时也会触发。
- 手动：GitHub 仓库页 → Actions → Auto Update Trackers → Run workflow。
- 月度检查（每月 1 日 05:00 UTC）：Actions → Monthly Subscription Check。

### 3.3 新增 / 移除订阅源

`SOURCES` 是唯一配置点（`scripts/update_trackers.py` 顶部），格式：
`("trackers_xxx.txt", "https://源地址", "短名")`。白名单
`ALLOWED_SOURCE_URLS` 自动从 SOURCES 派生，无需手动同步。新增源后还需同步：

1. `generate_source_links()` 的 `label_map`（首页 footer 显示名）
2. `scripts/health_check.py` 的 `TRACKER_FILES` / `PLAIN_TEXT_FILES` / `CONSISTENCY_MAP`
3. `sync_plain_text_files()` 的 mapping（docs/ 镜像文件名）
4. `scripts/monthly_subscription_check.py` 的 `CHECKS`（仅当新增的是主订阅地址）
5. `cloudflare/tracker-proxy.js` 的 `ALIASES`（可选；`/src/<名>.txt` 路由是
   通用的，会自动覆盖）
6. README 的源数量徽章与说明

移除源：把条目从 `SOURCES` 删掉，并把其短名加入 `REMOVED_SOURCE_NAMES`，
脚本会自动清理残留文件。

### 3.4 修改 / 部署 Cloudflare Worker

Worker 源码：`cloudflare/tracker-proxy.js`（路由 `tracker.pmwiu.com/*`）。

- 方式 A（推荐）：Cloudflare Dashboard → Workers & Pages → 对应 Worker →
  粘贴源码 → Deploy。
- 方式 B：`npx wrangler deploy cloudflare/tracker-proxy.js --name tracker-proxy
  --compatibility-date <date>`（需 `wrangler` 登录，Node ≥ 18）。

Worker 是手工部署的，**改完仓库里的 js 不会自动上线**，需要手动同步。

### 3.5 回滚

```bash
bash rollback.sh          # 交互式：列出最近 10 条提交，输入 hash 恢复
```

或手动：`git revert <坏提交>` 后推送。注意回滚后下一次 CI 运行会重新生成
tracker 列表（数据类提交的回滚会被下次自动更新覆盖，代码类回滚不会）。

### 3.6 失败告警处理

工作流失败会自动创建带 `automated-alert` 标签的 Issue（成功后自动关闭）。
定位顺序：

1. Issue 正文里的 run 链接 → Actions 日志尾部
2. `docs/ci-diag.md`（最近一次运行的诊断：环境、锁、各源连通性）
3. `reports/run_summary.json`（哪个源失败、`failed_sources`）
4. `reports/health.json`（FAIL 项明细）
5. `trackers/test_report.md`（探活明细：协议分布、死因分类）

常见处置：
- 单个源失败 → 脚本自动用 `trackers/backup/` 的备份降级，通常无需处理；
  长期失败再从 SOURCES 移除。
- 大面积失败 → 先看 ci-diag.md 里各源连通性，区分"源挂了"还是
  "运行器网络挂了"（后者重跑即可）。
- `circuit_breaker_triggered` → 连续超时熔断，属网络异常，保留上次结果，重跑。

## 4. 设计不变量（接管后不可破坏）

1. **best ⊆ all**：`health_check.py` 有专项校验（Alive subset check）。
2. **best ≤ 25（MAX_TRACKERS）、all ≤ 59（MAX_ALL）**：改条数需同时改
   README 徽章、`health_check.py` 的 `MAX_ALIVE`、Worker 注释。
3. **纯标准库零依赖**：不要引入第三方包（CI 的 install 步骤是预留空位）。
4. **仓库零密钥**：只用 `GITHUB_TOKEN` 临时权限；Worker 无任何凭据。
5. **白名单校验**：`download_trackers()` 拒绝 `ALLOWED_SOURCE_URLS` 之外的
   一切 URL；`SOURCES` 里出现非白名单条目会在启动时硬失败。
6. **仅 5 种协议**（udp/http/https/wss/ws），localhost / 内网 / 保留段地址在
   探活前被 `is_safe_tracker()` 拦截；UDP 连接固定使用已校验的解析 IP
   （DNS 重绑定防护）。
7. **存活判定 = 完整 announce 握手**：HTTP 须 bencoded 且无 failure reason；
   UDP 须 connect+announce 双响应；WSS/WS 为 TLS/TCP 连通性（质量分级打分）。
8. **历史状态按真实探活记录**："存活但被淘汰"（capped/低速/同网段去重）
   绝不能记为 dead，否则稳定性 EMA 被污染、动态黑名单误杀。
9. 失败时**保留上次 best/all**（熔断与备份降级机制），宁可不更新也不发坏列表。

## 5. 本机（Windows）环境注意事项

- **Git Bash 中文路径坑**：工作目录 `E:\工作` 含中文，直接向 bash 传含中文
  的命令行参数会因编码失败（exit 127）。绕行：用变量
  `ws="/e/$(printf '\xe5\xb7\xa5\xe4\xbd\x9c')"`，或把 cwd 设到 ASCII 路径。
  Read/Write/Edit/Glob 工具不受影响。
- **文件锁**：Windows 无 fcntl，`acquire_lock()` 走 `O_CREAT|O_EXCL` 原子建锁
  文件 `.update.lock`（已 gitignore），带死锁检测与 PID 抢占。
- **控制台中文乱码**：Windows 终端代码页是 GBK，脚本 print 的中文显示为乱码
  属正常，文件内容本身是 UTF-8，不受影响。
- Python 版本：CI 用 3.12；本地 `uv venv --python 3.12 .venv` 对齐。

## 6. 关键参数速查

| 参数 | 位置 | 值 | 含义 |
|---|---|---|---|
| `MAX_TRACKERS` | update_trackers.py | 25 | best 条数上限 |
| `MAX_ALL` | update_trackers.py | 59 | all 条数上限 |
| `MAX_CANDIDATES` | update_trackers.py | 200 | 合并候选池上限 |
| `MIN_NON_UDP_TRACKERS` | update_trackers.py | 4 | best 非 UDP 保底 |
| `ALL_PROTOCOL_FLOORS` | update_trackers.py | wss1/ws1/https15/http15/udp20 | all 协议保底 |
| `MIN_CLASSIC_TRACKERS` | test_trackers.py | 4 | best 经典高可用保底 |
| `CLASSIC_BONUS` | test_trackers.py | 6.0 | 经典主机加分 |
| 评分权重 | test_trackers.py | 60/25/15 | 速度/稳定性/质量 |
| `LOW_SPEED_THRESHOLD_MS` | test_trackers.py | 5000 | 低速淘汰线 |
| `DEAD_BLACKLIST_RUNS` | test_trackers.py | 20 | 连续失效入动态黑名单 |
| `UPTIME_ALPHA` | test_trackers.py | 0.2 | 存活率 EMA 权重 |
| `STALE_SOURCE_DAYS` | health_check.py | 7 | 源内容不变告警天数 |
