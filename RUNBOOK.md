# Tracker-List 运行手册（RUNBOOK）

面向维护者与 AI 会话的交接文档。读完本文档即可安全地操作本项目。

---

## 1. 项目是什么

生产级 BitTorrent Tracker 订阅聚合服务：每 6 小时从 14 个白名单订阅源抓取
tracker 列表，合并去重后做**协议级活性测试**（HTTP bencoded announce 校验 /
UDP connect+announce 握手 / WSS TLS），按综合评分排序，产出两个订阅计划：

| 计划 | 条数 | 文件 | 说明 |
|---|---|---|---|
| **all** 存活 | ≤ 59 | `trackers/trackers_all.txt` | 全部通过完整 announce 握手的存活 tracker，按评分降序 |

用户通过直链 `https://raw.githubusercontent.com/Pmwiu/Tracker-List/main/trackers/trackers_all.txt` 订阅
（jsDelivr CDN 加速直链可选）。

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
        ▼                         → all(59) / dead
scripts/health_check.py           本地完整性 + URL 格式 + 去重 + 最低数量 + 源新鲜度
        │
        ▼  git commit & push (bot)
分发链路:
  GitHub Raw ──► jsDelivr CDN (全球加速)
监控: reports/run_summary.json · reports/health.json · reports/source_state.json · .github/ci-diag.md
```

### 产物文件速查

| 路径 | 内容 | 谁生成 |
|---|---|---|
| `trackers/trackers_<源>.txt` | 各源原始列表 | update_trackers.py |
| `trackers/trackers_merged.txt` | 合并候选池（≤200） | update_trackers.py |
| `trackers/trackers_all.txt` | all 59（评分排序） | test_trackers.py |
| `trackers/trackers_dead.txt` | 失效/被淘汰 | test_trackers.py |
| `trackers/blacklist_dynamic.txt` | 动态黑名单（连续失效 ≥20 次） | test_trackers.py |
| `trackers/test_state.json` | 存活率 EMA + 连续失效计数 | test_trackers.py |
| `reports/*.json` | 运行摘要 / 健康状态 / 源新鲜度 | 各脚本 |
| `.github/ci-diag.md` | 最近一次 CI 诊断日志 | workflow |

## 3. 常用操作

### 3.1 本地跑全流程（Windows）

```bash
# 建环境（仅需一次，需要 uv 或 Python 3.12）
uv venv --python 3.12 .venv

# 依次执行（CI 同款参数）
.venv\Scripts\python.exe scripts\update_trackers.py
.venv\Scripts\python.exe scripts\test_trackers.py --timeout 10 --workers 30 --max-candidates 1000
.venv\Scripts\python.exe scripts\health_check.py --skip-net      # 纯本地
.venv\Scripts\python.exe scripts\health_check.py --rounds 3      # 多轮检查
.venv\Scripts\python.exe scripts\monthly_subscription_check.py   # 线上地址
```

注意：本地跑会改写 `trackers/`、`reports/` 下的生成物。验证完后用
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

1. `scripts/health_check.py` 的 `TRACKER_FILES`
2. `scripts/monthly_subscription_check.py` 的 `CHECKS`（仅当新增的是主订阅地址）
3. README 的源数量徽章与说明

移除源：把条目从 `SOURCES` 删掉，并手动删除其残留的 `trackers/trackers_<短名>.txt`。

### 3.4 回滚

```bash
bash rollback.sh          # 交互式：列出最近 10 条提交，输入 hash 恢复
```

或手动：`git revert <坏提交>` 后推送。注意回滚后下一次 CI 运行会重新生成
tracker 列表（数据类提交的回滚会被下次自动更新覆盖，代码类回滚不会）。

### 3.6 失败告警处理

工作流失败会自动创建带 `automated-alert` 标签的 Issue（成功后自动关闭）。
定位顺序：

1. Issue 正文里的 run 链接 → Actions 日志尾部
2. `.github/ci-diag.md`（最近一次运行的诊断：环境、锁、各源连通性）
3. `reports/run_summary.json`（哪个源失败、`failed_sources`）
4. `reports/health.json`（FAIL 项明细）
5. `trackers/test_report.md`（探活明细：协议分布、死因分类）

常见处置：
- 单个源失败 → 脚本跳过该源继续合并，通常无需处理；
  长期失败再从 SOURCES 移除。
- 大面积失败 → 先看 ci-diag.md 里各源连通性，区分"源挂了"还是
  "运行器网络挂了"（后者重跑即可）。
- `circuit_breaker_triggered` → 连续超时熔断，属网络异常，保留上次结果，重跑。

## 4. 设计不变量（接管后不可破坏）

2. **all ≤ 59（MAX_ALL）**：改条数需同时改 README 徽章。
3. **纯标准库零依赖**：不要引入第三方包（CI 的 install 步骤是预留空位）。
4. **仓库零密钥**：只用 `GITHUB_TOKEN` 临时权限。
5. **白名单校验**：`download_trackers()` 拒绝 `ALLOWED_SOURCE_URLS` 之外的
   一切 URL；`SOURCES` 里出现非白名单条目会在启动时硬失败。
6. **仅 5 种协议**（udp/http/https/wss/ws），localhost / 内网 / 保留段地址在
   探活前被 `is_safe_tracker()` 拦截；UDP 连接固定使用已校验的解析 IP
   （DNS 重绑定防护）。
7. **存活判定 = 完整 announce 握手**：HTTP 须 bencoded 且无 failure reason；
   UDP 须 connect+announce 双响应；WSS/WS 为 TLS/TCP 连通性（质量分级打分）。
8. **历史状态按真实探活记录**："存活但被淘汰"（低速/同网段去重）
   绝不能记为 dead，否则稳定性 EMA 被污染、动态黑名单误杀。
9. 失败时**保留上次 all**（熔断机制），宁可不更新也不发坏列表。
10. **发现模块与生产隔离（Phase 1）**：`discover_trackers.py` 找到的候选只写
    `trackers/discovered/`，参与 merge pool 与评分，但**绝不进入 all**
    （`reports/discovered_set.json` 列出候选集，`whitelist_only_set` 参数把它们排除）。转正必须人工改 SOURCES。

## 4b. 评分与筛选机制（v2）

**评分权重（总和 1.0）**：速度 50% + 稳定性 EMA 20% + 响应质量 15% +
**跨源一致性 10%** + **近期成功率 5%**；经典高可用主机名额外 +6。

- **跨源一致性**：同一 tracker 出现在 N 个独立白名单源 → 1源0 / 2源30 / 3源70 / ≥4源100。
  数据来源 `reports/source_counts.json`（update_trackers.py 产出）。
- **近期成功率**：`test_state.json` 的 `last_outcomes`（最近 10 次 0/1）算 alive 占比。
- **反退化**：最近 3 次结果全 0 → 最终分 −5。
- **多次采样测速**：对首轮存活最快的 50 个各跑 3 个样本，取**中位**；抖动扣分
  `max(0.7, 1 - (max-min)/median*0.3)`（最多扣 30%）。
- **双栈测试**：udp/wss/ws 若主机名同时有 A+AAAA 记录，两栈各测一次，取较优
  （http/https 保持单栈）。

- **peers 计数**：HTTP/HTTPS announce 解析 compact `peers`/`peers6` 字节长度得节点数，
  detail 记为 `announce with peers:N`，质量分档 N≥3→100 / 1-2→95 / 0→90（活跃/优秀信号）。
- **scrape 热度（BEP 15）**：对 http/https 存活者请求 `/scrape`（截断读 64KB，正则累计
  前 50 个 `complete` 种子数），分档 ≥100→100 / 10-99→98 / 1-9→95 / 0→90，与 announce
  质量取较高者；scrape 禁用/失败不惩罚（很多开放 tracker 有意关 scrape）。
- **同域名去重**：同主机名（跨端口/协议，ngosang 方法）连同 /24 网段一起去重，各留最快。

**私有冒烟测试**：`python scripts/_smoke.py`（21 项断言，无 pytest 依赖）。
CI 不跑它；改动评分/选优/发现逻辑后本地跑一遍。

## 4c. 自动发现模块（Phase 1 + 2）

- **入口**：`scripts/discover_trackers.py`（也可 `--out-dir` 指定目录）
- **产出**：`trackers/discovered/candidates_<UTC日期>.txt`（每行一个 URL，UTC 日粒度）
- **发现源**：GitHub topic `bt-tracker` / `public-tracker` / `tracker-list`（每仓库抓
  README.md + 名称含 `tracker` 的 `.txt`，≤10 文件、≤100KB）；**公开全量列表**
  （cf.trackerslist.com/all.txt + ngosang `trackers_all*` 经 jsDelivr）
- **速率**：CI 环境自动读取 `GITHUB_TOKEN`（Actions 内置）提升 GitHub API 限额
- **去重**：对 SOURCES 白名单 URL、当前 merged/alive/all 内容、过去 7 天发现结果去重
- **CI**：`update-trackers.yml` 的 "Discover candidate trackers" 步骤，
  `continue-on-error: true`（失败不阻断主流程）
- **本机限制**：国内网络对 `raw.githubusercontent.com` / `cdn.jsdelivr.net` 直连
  常被重置（WinError 10054），本地跑发现常得 0 条；CI（US runner）正常。

## 4d. 黑名单机制（整合 + 去重 + 防误杀）

三类黑名单经 `build_blacklists(source_counts)` 整合为 `(domain_set, url_set, protected_set)`，
各自去重，`main()` 单一入口加载，`download_trackers` 与 `load_discovered_candidates` 共用：

| 来源 | 级别 | 文件/端点 | 作用 |
|---|---|---|---|
| 域名黑名单 | 域名 | `blacklist.txt` | 排除整个主机 |
| 远程知名项目 | 精确 URL | ngosang + XIU2 `blacklist.txt` | 拉黑已知坏 tracker |
| 动态黑名单 | 精确 URL | `trackers/blacklist_dynamic.txt` | 连续失效 ≥20 次自动拉黑 |

**防误杀（false-kill protection）**：
- `protected_set` = `PROTECTED_HOSTS`（14 个经典公共 tracker 主机）∪ 上一轮跨源一致性 ≥3 的主机。
- **域名级黑名单不能杀受保护主机**（`is_blacklisted`：域名命中但主机在保护集 → 放行）。
- **URL 级仍可精确杀**任意单条 URL（含受保护主机的某条坏 URL）——精确匹配不误伤同主机其它路径。
- **动态黑名单跳过受保护主机**：经典 tracker 偶发连续下线不会被自动永久拉黑（`write_dynamic_blacklist`）。
- 畸形 IPv6 URL（`udp://[::1:6969`）经 `is_blacklisted` 安全跳过，不崩不误杀。

## 5. 本机（Windows）环境注意事项

- **Git Bash 中文路径坑**：工作目录 `E:\工作` 含中文，直接向 bash 传含中文
  的命令行参数会因编码失败（exit 127）。绕行：用变量
  `ws="/e/$(printf '\xe5\xb7\xa5\xe4\xbd\x9c')"`，或把 cwd 设到 ASCII 路径。
  Read/Write/Edit/Glob 工具不受影响。
- **文件锁**：Windows 无 fcntl，`acquire_lock()` 走 `O_CREAT|O_EXCL` 原子建锁
  文件 `.update.lock`（已 gitignore），带死锁检测与 PID 抢占。
- **控制台中文乱码**：Windows 终端代码页是 GBK，脚本 print 的中文显示为乱码
  属正常，文件内容本身是 UTF-8，不受影响。
- **不要写非 GBK 字符到 print**：`⊆` 等符号会触发 `UnicodeEncodeError`（已改成 ASCII）。
- Python 版本：CI 用 3.12；本地 `uv venv --python 3.12 .venv` 对齐。
- **HTTPS 到 GitHub 被劫持**：本机 DNS 把 github 解析到 localhost，git 走 SSH-over-443
  真实 IP（见 `~/.ssh/config`）；`git push` 前先确认能 `ssh -T git@github.com`。

## 6. 关键参数速查

| 参数 | 位置 | 值 | 含义 |
|---|---|---|---|
| `MAX_ALL` | update_trackers.py | 59 | all 条数上限 |
| `MAX_CANDIDATES` | update_trackers.py | 200 | 合并候选池上限 |
| `ALL_PROTOCOL_FLOORS` | update_trackers.py | wss1/ws1/https15/http15/udp20 | all 协议保底 |
| `CLASSIC_BONUS` | test_trackers.py | 6.0 | 经典主机加分 |
| 评分权重 | test_trackers.py | 50/20/15/10/5 | 速度/稳定性/质量/跨源/近期 |
| `SCORE_*_WEIGHT` | test_trackers.py | 见上 | 五个独立权重常量 |
| `SOURCE_AGREEMENT_SCORES` | test_trackers.py | 1:0/2:30/3:70/≥4:100 | 跨源一致性映射 |

| `multi_sample_refine` | test_trackers.py | 3 样本 | 中位 + 抖动扣分（≤30%） |
| `LOW_SPEED_THRESHOLD_MS` | test_trackers.py | 5000 | 低速淘汰线 |
| `DEAD_BLACKLIST_RUNS` | test_trackers.py | 20 | 连续失效入动态黑名单 |
| `UPTIME_ALPHA` | test_trackers.py | 0.2 | 存活率 EMA 权重 |
| `STALE_SOURCE_DAYS` | health_check.py | 7 | 源内容不变告警天数 |
| `PUBLIC_ALL_LISTS` | discover_trackers.py | 8 条 | 公开全量发现列表 |
| `PER_REPO_FILE_CAP` | discover_trackers.py | 10 | 每仓库最多抓文件数 |
| `PER_REPO_FILE_CAP` | discover_trackers.py | 10 | 每仓库最多抓文件数 |
| `PER_FILE_BYTE_CAP` | discover_trackers.py | 102400 | 单文件字节上限 |
