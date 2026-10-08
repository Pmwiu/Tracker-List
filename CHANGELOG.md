# Changelog

本文件记录项目的主要变更。格式：`## [日期] - 类型` + 变更描述。

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
