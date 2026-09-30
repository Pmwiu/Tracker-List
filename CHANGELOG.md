# Changelog

本文件记录项目的主要变更。格式：`## [日期] - 类型` + 变更描述。

## [2026-09-30] - feat
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
