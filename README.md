<h1 align="center">Tracker List</h1>

<p align="center">自动聚合 · 智能去重 · 协议级活性测试 · 综合评分排序<br>每 6 小时自动更新的 BitTorrent Tracker 订阅服务</p>

<p align="center">
<img src="https://img.shields.io/github/actions/workflow/status/Pmwiu/Tracker-List/update-trackers.yml?branch=main&label=auto%20update" alt="auto update">
<img src="https://img.shields.io/badge/best-20-2563eb" alt="best 20">
<img src="https://img.shields.io/badge/all-100-2563eb" alt="all 100">
</p>

> **当前状态：订阅源待配置。** `scripts/update_trackers.py` 中的 `SOURCES` 为空。
> 仓库框架、脚本、工作流与托管（GitHub Pages + Cloudflare Worker/Pages）保持完整，
> 填入订阅源后定时任务会自动恢复生成 best / all 订阅列表。

## 机制

- **聚合**：多源按优先级合并，来源白名单 + 内容校验 + 原子写入
- **清洗**：URL 规范化去重、同 IP 保留最快、动态黑名单
- **探活**：HTTP/HTTPS 验证 bencoded 响应、UDP connect+announce、WSS/WS TLS 连通；>5s 低速淘汰
- **评分**：速度 70% + 稳定性 EMA 30%；best 保底 4 条非 UDP、all 协议保底
- **托管**：GitHub Pages + Cloudflare Pages 双托管，Worker 短链接网关，`/jsd/` 前缀切换 jsDelivr 加速
- **监控**：定时任务 + 心跳 + 运行摘要 + 失败告警 + 健康检查 + 月度订阅地址清单

## 链接

- Cloudflare Worker 源码：[`cloudflare/tracker-proxy.js`](cloudflare/tracker-proxy.js)
- 变更记录：[`CHANGELOG.md`](CHANGELOG.md) · 安全说明：[`SECURITY.md`](SECURITY.md)
- 订阅源配置：[`scripts/update_trackers.py`](scripts/update_trackers.py)
