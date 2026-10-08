# Changelog

本文件记录项目的主要变更。格式：`## [日期] - 类型` + 变更描述。

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
