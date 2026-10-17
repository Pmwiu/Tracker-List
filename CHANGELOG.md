# Changelog

本文件记录项目的主要变更。格式：`## [日期] - 类型` + 变更描述。

## [2026-10-17] - chore
- **移除 best 订阅分类**：删除 `trackers_alive.txt`、`docs/alive.txt`、
  `docs/s/alive.html` 及 7 个 alive 备份文件；清理 `select_top_with_quotas`/
  `MIN_CLASSIC_TRACKERS`/`MAX_TRACKERS`/`MIN_NON_UDP_TRACKERS` 及 ASN 多样性
  demotion 基础设施；移除 Worker `best.txt`/`alive.txt` 路由、MIRRORS best 块、
  health_check 中 alive 数量与 best⊆all 子集校验、monthly-check 中 best 验证。
  只保留 all 订阅，评分排序与自动发现功能不受影响。

## [2026-10-17] - chore
- **移除备选库 reserve 功能**：删除 `trackers_reserve.txt`、`docs/reserve.txt`、
  `reports/promote_queue.json`、`trackers/discovered/PROMOTE.md` 及 Phase 2 计划文档；
  清理 `build_reserve`/`select_reserve`/`update_promote_queue`/`check_reserve_pool` 函数、
  `RESERVE_MAX`/`PROMOTE_*` 常量、Worker `/reserve.txt` 路由、MIRRORS 块、
  monthly-check 转正 Issue 步骤及各文档中的相关描述。自动发现功能保留。

## [2026-10-14] - feat
- **黑名单整合 + 去重 + 防误杀**：新增 `build_blacklists(source_counts)` 把域名级
  (`blacklist.txt`)、远程 URL 级 (ngosang+XIU2)、动态 URL 级 (连续失效) 三类整合为
  `(domain_set, url_set, protected_set)` 单一入口，各自去重；`download_trackers` 与
  `load_discovered_candidates` 共用
- **防误杀保护集**：`PROTECTED_HOSTS`（14 经典主机）∪ 上一轮跨源一致性≥3 的主机；
  域名级黑名单不能杀受保护主机（`is_blacklisted`），URL 级仍可精确杀；动态黑名单
  (`write_dynamic_blacklist`) 跳过受保护主机，经典 tracker 偶发下线不被自动永久拉黑
- 清理了一处重复的 `load_discovered_candidates` 定义
- **Cloudflare 托管加固上线**：`tracker-proxy` Worker 重新部署为 ES-Module 加固版
  （内存泄漏修复 + 上游 4s 超时 + KV last-known-good 降级 + `cache-control` + `/health`），
  新建 KV `tracker-cache` 并绑定，每日 Cron `17 3 * * *` 预热（wrangler 部署）

## [2026-10-14] - feat
- **测活增强**：HTTP/HTTPS announce 解析 compact peers/peers6 字节长度得节点数
  （`announce with peers:N`），质量分档 N≥3→100/1-2→95/0→90；新增 BEP 15 `scrape`
  热度探针（http/https 存活者，截断读 64KB 正则累计种子数，禁用/失败不惩罚），
  与 announce 质量取较高者——对齐 ngosang「按 popularity + latency 排序」
- **筛选增强**：同域名去重（跨端口/协议，ngosang 方法）连同 /24 网段一起去重，各留最快
- **备选库 reserve（新订阅源）**：discovered 候选通过探活+评分后前 20 条写入
  `trackers/trackers_reserve.txt`，发布为 `/reserve.txt`（Worker alias + docs 镜像 +
  MIRRORS），与 best/all 严格不相交；health_check 校验数量与不相交不变量
- **自动发现扩充**：新增公开全量列表源（cf.trackerslist.com/all.txt + ngosang
  `trackers_all*` 经 jsDelivr）；CI 环境读取 `GITHUB_TOKEN` 提升 API 限额
- **转正队列（B3）**：`reports/promote_queue.json` 跟踪 discovered 候选连续存活轮数
  （活+1 / 连续死 3 次剔除 / 30 天未见裁剪）；连续存活 ≥5 轮进
  `trackers/discovered/PROMOTE.md`，月度 workflow 自动开/更新 `tracker-promotion`
  Issue 供人工审查转正（`issues: write`）
- **修复**：CI run #122 因 `contribution` 在 discovered 循环里先于定义被引用而失败
  （本机网络屏蔽 discovered=0 掩盖了该路径，CI 有真实候选才暴露）→ 提取
  `append_discovered_sources` 并前置初始化，加回归测试
- 文档：README 可靠性/安全/订阅表更新（此前权重描述停留在 60/25/15 未同步，一并修正）；
  RUNBOOK 补 peers/scrape/同域名去重/备选库/转正队列；Phase 2 设计计划入库

## [2026-10-13] - feat
- **评分 v2：5 维加权 + 反退化**。权重 速度50% + 稳定性EMA20% + 响应质量15%
  + 跨源一致性10% + 近期成功率5%（此前 60/25/15）；经典高可用 +6 不变。
  - 跨源一致性：同一 tracker 出现在 N 个独立源 → 1源0/2源30/3源70/≥4源100；
    数据来自新的 `reports/source_counts.json`（update_trackers.py 产出）
  - 近期成功率：`test_state.json` 新增 `last_outcomes`（最近 10 次 0/1）
  - 反退化：最近 3 次全 0 → 最终分 −5
- **多次采样测速**：首轮存活最快的 50 个各跑 3 样本，取中位；抖动扣分
  `max(0.7, 1-(max-min)/median*0.3)`（最多 −30%），替换原「两轮取较快」逻辑
- **IPv4/IPv6 双栈测试**：udp/wss/ws 若主机名同时有 A+AAAA，两栈各测一次取较优
  （http/https 保持单栈）
- **ASN /24 多样性 demotion + 冷门命中偏好**：best/all 选优后同 /24（IPv6 /48）
  至多 3 条；非 UDP 保底阶段优先 uptime≥0.7；缓存 `trackers/cache/asn_cache.json`
  （7 天 TTL，gitignored）
- **自动发现模块（Phase 1）**：新增 `scripts/discover_trackers.py`，从 GitHub topic
  （bt-tracker / public-tracker / tracker-list）+ 公开列表发现候选，写
  `trackers/discovered/candidates_<date>.txt`；`update_trackers.py` 把它们并入
  merge pool（计入 MAX_CANDIDATES）**但不进 best/all**（`reports/discovered_set.json`
  + `select_top_with_quotas(whitelist_only_set=...)` 隔离）；`test_report.md`
  新增 Discovery 段；转正需人工改 SOURCES
- **CI**：`update-trackers.yml` 新增 "Discover candidate trackers" 步骤
  （`continue-on-error: true`）；`health_check.py` 新增 Discovery 输出校验
- **私有冒烟测试**：新增 `scripts/_smoke.py`（13 项断言，无 pytest 依赖）
- **文档**：RUNBOOK 补充 4b（评分机制 v2）/4c（发现模块）/参数速查表；新增设计文档
  `docs/superpowers/specs/2026-10-13-tracker-discovery-design.md` 与实施计划
  `docs/superpowers/plans/2026-10-13-tracker-discovery-and-mechanism-improvements.md`

## [2026-10-12] - fix
- health_check 不变量检查名实不符：原 `check_alive_subset_of_merged` 注释与输出都
  标榜"best ⊆ all"，实际检查的是 `best ⊆ merged`（候选池 200），是平凡不变量，
  无法捕获「配额（经典 ≥4 / 非 UDP ≥4）把低分条目拉入 best、却不在 all 前 59 名」
  的违规。改为对照 `trackers_all.txt` 校验 `best ⊆ all`；检查项 label 改用 ASCII
  避免 Windows GBK 控制台崩溃
- health_check 重复硬编码：`MAX_ALIVE = 25` 与 update_trackers 的 `MAX_TRACKERS`
  历史上漂移过（20→25 时手动同步过一次），改为 `getattr(ut, "MAX_TRACKERS", 25)`
  单一真相源
- update_trackers 注释与代码不符：第 1097 行 `merged = sorted(all_merged)` 注释
  写"取前 MAX_ALL 条"但实际写入全部 200 条候选池；改为准确描述（候选池写入，
  下游按评分选 best/all）

## [2026-10-12] - docs
- 新增 `RUNBOOK.md`：维护者/AI 会话运行手册，覆盖架构图、产物速查、本地/CI
  常用操作、订阅源增删、Worker 部署、回滚、告警处理、9 条设计不变量、关键参数

## [2026-10-10] - feat
- best 总数 20→25（最多 25）、all 总数 100→59（最多 59），均按评分降序取足目标条数；
  为保证 all 能填满 59，新增独立的候选池上限 `MAX_CANDIDATES=200`（merge 阶段测试
  足够多候选，独立于 all 输出上限），让存活池有足够多 tracker 填入 59 条
- 同步更新：health_check MAX_ALIVE 20→25、README 徽章与订阅表、Worker 注释

## [2026-10-08] - chore
- 清理死参数与冗余：write_trackers 移除 source_url/extra_header、write_result_file
  移除 description、generate_index_page 移除 short_links_with_urls、write_report 移除
  alive_sorted；首页统计改用 ALL_FILE（all 存活）而非 merged 候选池
- 修正过时/矛盾文本：SECURITY.md「功能收敛」说明 Issues 仅用于自动告警（不再宣称关闭）、
  DNS 重绑定已知限制更新（UDP 已硬化）；README 健康检查项数改为非硬编码

## [2026-10-08] - feat
- 补充 2 个订阅源：1265578519/OpenTracker tracker.txt、trackers.run rw_ws
  （WebSocket 列表），源数 12→14；同步更新白名单、docs 镜像、健康检查清单与 README

## [2026-10-08] - feat
- 冷门/死种/老种子优化：best 新增「经典高可用」保底配额（≥4 条），经典 tracker
  长期稳定、拥有深厚 peer 数据库、真正开放，对老资源加速显著；all 天然含全部存活经典
- 补充知名热门黑名单项目源：ngosang、XIU2 的 blacklist.txt 拉取并合并（精确 URL 级
  匹配，避免误伤同域名的经典/正常 tracker），增强对黑名单 tracker 的屏蔽拦截，
  严厉禁止入选 best/all

## [2026-10-08] - feat
- all 列表同样改为「只含完整 announce 握手、返回有效响应」的存活 tracker：
  新增 trackers_all.txt（全部存活去重、按评分降序、取前 MAX_ALL），
  all.txt 短链接与 Pages/jsDelivr 直链改指向该存活列表；trackers_merged.txt
  保留为原始候选池（供参考与下次重测）
- 同步更新 Worker 别名、docs 同步、health_check 清单、MIRRORS.txt、月度检查清单

## [2026-10-08] - fix
- 收紧判活标准（参照 ngosang/XIU2 只收录真正开放的 tracker，修复「订阅列表大部分
  不可用」问题）：
  - HTTP「failure reason」= 私有/受限 tracker（拒绝未知 info_hash）→ 判为失效
  - HTTP「仅 bencoded 无 announce 字段」→ 判为失效
  - UDP「仅 connect 成功、announce 无响应」→ 判为失效；announce 响应须校验
    action==1 且事务号匹配，并增加一次重试降低高并发 UDP 丢包假阴性
  - 存活列表现仅含「完成完整 announce 握手且返回有效响应」的 tracker

## [2026-10-08] - feat
- 评分新增「经典高可用加分」：长期稳定、广泛使用的经典公共 tracker 主机名
  （opentrackr / stealth.si / torrent.eu.org / demonii / desync / explodie 等）
  在综合评分中额外 +6，实现「经典高可用 Tracker 优先」的高质量要求

## [2026-10-08] - feat
- 补充订阅源 tracker.adysec.com/trackers_best.txt（adysec 成熟 Rust 聚合项目），
  同步更新白名单、docs 镜像、健康检查清单与 README（源数 11→12）

## [2026-10-08] - feat
- UDP 探活 DNS 重绑定防护：连接固定使用 is_safe_tracker 已校验并缓存的解析 IP，
  避免发送时被 OS 重新解析到不同（可能是内网）地址
- 源内容新鲜度检测：update_trackers 记录各源内容指纹与首次出现时间
  （reports/source_state.json），health_check 在源内容连续不变超过 7 天时告警，
  检测「源已停止更新但返回 200」的静默失效

## [2026-10-08] - feat
- 评分机制重写：移除「地域适配加分」，权重调整为速度 60% + 历史稳定性 25% + 响应质量
  15%（速度 > 稳定性 > 质量）；速度分改为自适应线性标度，以本 run 存活 tracker 的
  中位延迟为参照自校准，网络整体快时标度收紧、整体慢时放宽
- 自动维护增强：`save_history` 增加候选集裁剪（candidates 参数），自动剔除已
  不在当前 merged 列表的历史条目，防止 test_state.json 无限增长
- 同步更新：测试报告、首页卡片、README 评分说明

## [2026-10-08] - fix
- 修复历史状态记录 bug：此前 `save_history(alive_final, dead_final)` 把「存活但被
  淘汰」（capped/低速/同网段去重）的 tracker 错误记为失效，导致其稳定性 EMA 被拉低、
  连续失效计数累积、20 次后被动态黑名单误杀。现改为按真实探活结果记录 alive/dead
- health_check 新增「best ⊆ all」不变量校验（Alive subset check）
- SECURITY.md 补充 SSRF 防护说明与 DNS 重绑定已知限制（低风险）

## [2026-10-08] - feat
- 细分响应质量评分：HTTP 区分「返回 peers（可用节点，100）」与「仅 interval/complete
  等字段（90）」，使「真正能返回节点」的 tracker 评分更高
- 筛选细化：同 IP 去重升级为同网段去重（IPv4 按 /24、IPv6 按精确 IP），
  避免同一主机/同一运营商的冗余节点占据名额
- 自动维护增强：health.json 新增 alive/merged 实时计数；新增最低数量异常告警
  （alive < 5 或 merged < 30 时 WARN），防止源大面积失效时的静默退化

## [2026-10-08] - feat
- 补充 3 个 ngosang 订阅源：trackers_best_ip.txt（IP 直连最佳，契合内地/内网地域加分）、
  trackers_all_i2p.txt、trackers_all_yggdrasil.txt（特殊网络，仅入 all 不计 best）

## [2026-10-08] - feat
- 针对中国内地/内网环境增加地域适配精细加分（参考 XIU2 TrackersListCollection 的
  best_ip 思路）：IPv4 直连 +5、IPv6 直连 +2、.cn 域名 +4、https +2（最高 +11），
  使规避 DNS 污染、国内低延迟、穿透网络干扰的 tracker 在综合评分中优先
- 评分维度更新为：速度 50% + 稳定性 30% + 响应质量 20% + 地域适配加分；报告新增地域列
- README 重设计：现代化/极简/安全/商务风（状态徽章 + 订阅表 + 可靠性与安全分节）

## [2026-10-08] - feat
- 最终订阅列表改为纯 tracker 内容：移除注释头、空行与统计信息，每个 tracker
  单独一行、行间不空行（best/all/协议子列表/各源文件全部纯文本化），便于直接复制
- health_check 适配：空协议列表（如 ws.txt 无条目）按 0 trackers 视为合法

## [2026-10-08] - feat
- 评分机制升级为多维综合评分：速度 50% + 历史稳定性 EMA 30% + 响应质量 20%。
  新增「响应质量」维度，按协议级握手/响应完整性分级：完整 announce 响应(100) >
  仅 TCP/TLS 建连(80-90) > UDP 仅 connect(70) > HTTP 仅可达/拒绝请求(55)，
  参考 ngosang/adysec 的存活测试分级思路，确保综合最优而非单纯比快
- 测试报告与首页卡片同步展示三维评分与质量分

## [2026-10-08] - fix
- 清理失效参数：mirror_urls 移除无 DNS 的 raw.pmwiu.com / gh.pmwiu.com 镜像主机，
  仅保留可用的 jsDelivr 回退
- Worker 修复「失效/未知路径返回 200 index.html」：Pages 对未知 .txt 路径会回退
  index.html 且 _headers 把 content-type 伪装成 text/plain，改为按正文特征识别并
  拒绝；Pages/GH 回退仅作用于 docs/ 内容（trackers//reports/ 仅走 Raw）
- 重新部署 Worker，失效别名（run_best/opentracker 等）现正确返回 404
- SECURITY.md 同步：权限（+issues:write）、Action 版本（v5/v6/v8）、触发方式
  （含 push）、推荐订阅短链接改为 tracker.pmwiu.com/best.txt

## [2026-10-08] - feat
- 订阅源替换为 8 个 best 精选源：ngosang（jsDelivr 加速）、cf、以及
  gonghailink / panda-men / gspu / linux-jin / AlphaCatMeow / pexcn 的
  trackers_best 派生源；同步更新白名单、docs 镜像、健康检查清单、Worker
  /src 命名空间与 README 订阅表

## [2026-10-08] - chore
- 清空全部订阅源（SOURCES = []）与订阅数据内容（trackers/ 生成物、docs/ 镜像与主页、
  reports/ 摘要、backup/），等待重新提供订阅源配置
- 仓库框架与结构保持不变：三个核心脚本、Cloudflare Worker 源码、双托管配置、
  GitHub Actions（定时/月度/告警）全部保留
- 零订阅源优雅降级：update/test 直接退出、health_check 数据缺失降级为 WARN、
  monthly_subscription_check 跳过、workflow 仅保留心跳提交

## [2026-10-08] - feat
- all 列表增加协议保底配额（ALL_PROTOCOL_FLOORS）：wss/ws 只要存在就保留，
  https/http/udp 保底 15/15/20 条，其余由按源轮转填充；all 现覆盖 4 种协议
  （此前 wss 因 100 条上限被挤出）
- Worker 增加简单限流（每 IP 每 60s 120 次，超限 429）与访问统计（/stats，
  单 isolate 内存统计，含各路由计数与限流次数）；支持 HEAD/OPTIONS(CORS 预检)
- 月度订阅地址清单固化为 scripts/monthly_subscription_check.py，并接入
  monthly-check.yml：每月验证 Worker 短链接/jsDelivr 加速/Pages/Raw/jsDelivr 直链
  共 10 个地址，best 校验 1..MAX_TRACKERS 条、all 校验 >0 条

## [2026-10-08] - fix
- all 合并改为「按源轮转」：原顺序取满 100 条会让 cf/trackers.run 占满名额，
  ngosang best_ip（16 条）与 OpenTracker（24 条）的独有 tracker 永远进不了 all；
  轮转后每个精选源都能贡献，all 覆盖更全、候选更多
- 合并日志新增各源贡献统计（cf=… run=… ngosang=…）

## [2026-10-08] - feat
- 短链接服务规范化：Worker 重写并入库（cloudflare/tracker-proxy.js）。
  规范：`/best.txt` `/all.txt`（兼容 /alive.txt /merged.txt）、`/p/<协议>.txt`、
  `/src/<源>.txt`、`/jsd/<任意短链接>` 切换 jsDelivr 加速镜像；
  按扩展名返回正确 content-type（修复旧版全站 text/plain）、新增 x-tracker-upstream
  调试头、路径大小写不敏感、404/502 区分
- 首页（README + Pages index.html）现代化：卡片式订阅区（短链接 + 加速短链接 +
  一键复制）、协议芯片、统计区块；首页订阅链接只展示 txt 短链接与加速短链接，
  去除全部长链接
- MIRRORS.txt 重写为分组全量清单（best/all/按协议/按源 × 短链接/加速/Pages/Raw/jsDelivr）
- 新增 cloudflare/ 目录：Worker 源码纳入版本管理

## [2026-10-08] - feat
- best 列表增加协议多样性配额：保底 4 条非 UDP（http/https/wss/ws）。
  UDP 握手往返天然快于 HTTP announce，纯速度排序会让 best 变成单一协议，
  一旦订阅者网络封 UDP 整份订阅即失效；配额后其余 16 条仍按综合评分
  （速度 70% + 稳定性 30%）填充，非 UDP 不足 4 条时有多少取多少

## [2026-10-08] - feat
- 订阅源重新配置为 5 个精选源（cf best / trackers.run best / ngosang best + best_ip /
  OpenTracker），顺序即优先级；下线源文件由 REMOVED_SOURCE_NAMES 自动清理
- 新增镜像回退：原始地址不可达时按 raw.pmwiu.com → jsDelivr → gh.pmwiu.com 顺序重试；
  DNS 解析失败快速失败，不再空转重试
- 协议子列表（udp/http/https/wss/ws）即使为空也写出文件，5 个协议订阅地址始终可用
- 实测：5 源全部抓取成功，all = 100、best = 20（best ⊆ all 成立），健康检查 41/0/0

## [2026-10-08] - chore
- 清空全部订阅源（SOURCES = []）及订阅数据内容（trackers/、docs/ 生成物、reports/），
  等待重新提供订阅源配置；仓库框架、脚本与工作流保持不变
- 零订阅源状态下优雅跳过：update_trackers.py / test_trackers.py 直接退出（不做无效下载、
  不写失败摘要、不触发告警），health_check.py 将数据文件缺失降级为 WARN
- workflow 新增 "Check subscription sources" 步骤，未配置源时跳过抓取/测试/健康检查，
  仅保留心跳提交；诊断步骤的源列表改为从 SOURCES 动态生成

## [2026-10-07] - feat
- 存活率历史加权评分：稳定性从「连续存活天数」升级为「存活率 EMA（指数滑动平均）」
  （偶发失效不会直接清零稳定性）；test_state.json 记录 uptime_ema

## [2026-10-07] - feat
- 按协议出子列表：trackers_udp/http/https/wss/ws.txt（从 all 合并列表按协议拆分），
  同步 docs/ 直链（udp.txt 等），对齐国际聚合项目的多格式列表

## [2026-10-07] - feat
- 动态黑名单：连续失效 20 次（约 5 天）的 tracker 自动列入 blacklist_dynamic.txt，
  后续下载自动过滤（精确 URL 匹配，dead_streak 记录在 test_state.json）

## [2026-10-07] - fix
- 修复 best ⊆ all 不成立（best 20 里有 16 条不在 all 100 里）：read_candidates 只返回
  all 列表，best 严格从 all 精筛；测试候选 376 → 100（更快、更聚焦）
- 修复 health_check 硬编码 /s/cf 404、IPv6 误判、日志语义、CI 变更检测

## [2026-10-06] - feat
- best 计划精确 20 条、all 计划精确 100 条（原 59/599）
- best 从 all 列表精测精选（best ⊆ all），机制对齐国际合集做减量聚焦

## [2026-09-30] - feat
- 新增 5 个源：pkgforge-security(all/general)、adysec all、ngosang all、cf all（共 21 源）
- all 计划改为按源优先级取前 599 条（精选源优先），候选数 500→1000
- README 订阅源按仓库分组
- 新增 5 个 ngosang 源：best / all_i2p / all_yggdrasil / all_ip / all_yggdrasil_ip（共 16 源）
- 新增 2 个聚合源：kris3713/UltimateBTTrackersList、1265578519/OpenTracker（共 11 源）
- 双托管：新增 Cloudflare Pages 同步部署（可选，需 CF_API_TOKEN/CF_ACCOUNT_ID secrets）
- 更新频率：cron 每日 → 每 6 小时
- Cloudflare Pages 缓存策略 docs/_headers（txt 实时 no-cache）

## [2026-09-29] - feat
- 订阅源替换为 9 个 best 精选源（cf best / ngosang best_ip / adysec best 系列 / animeTrackerList best），MAX_TRACKERS 25→59
- 来源白名单（仅 cf/adysec/ngosang 三源），协议白名单过滤，tempfile 原子写入
- 低速淘汰（>5s）、同 IP 去重（保留最快）、域名黑名单 blacklist.txt
- 存活数区间校验 [0,25]、协议分布统计
- 自动化监控：reports/run_summary.json、reports/health.json、.github/last_run.txt 心跳
- 失败告警 Issue（自动创建 / 自动关闭）
- 脚本健壮性：下载失败降级到备份、无效行日志 invalid_lines.log、测试熔断
- 定时任务优化：cron "23 0 * * *"、cancel-in-progress true

## [2026-09-28] - feat
- 初始版本：多源合并去重、协议级活性测试、GitHub Pages 短链接
