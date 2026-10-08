<h1 align="center">Tracker List</h1>

<p align="center">
自动聚合 · 智能去重 · 协议级活性测试 · 综合评分排序<br>
每 6 小时自动更新的 BitTorrent Tracker 订阅服务
</p>

<p align="center">
<img src="https://img.shields.io/github/actions/workflow/status/Pmwiu/Tracker-List/update-trackers.yml?branch=main&label=auto%20update" alt="auto update">
<img src="https://img.shields.io/badge/best-20-2563eb" alt="best 20">
<img src="https://img.shields.io/badge/all-100-2563eb" alt="all 100">
<img src="https://img.shields.io/badge/sources-5-2563eb" alt="5 sources">
<img src="https://img.shields.io/badge/non--UDP%20quota-%E2%89%A54-2563eb" alt="non-UDP quota">
</p>

## 订阅

| 计划 | 条数 | 短链接 (txt) | 加速短链接 (txt) |
|:---:|:---:|---|---|
| **best** 精选 | 20 | `https://tracker.pmwiu.com/best.txt` | `https://tracker.pmwiu.com/jsd/best.txt` |
| **all** 合并 | 100 | `https://tracker.pmwiu.com/all.txt` | `https://tracker.pmwiu.com/jsd/all.txt` |

> 加速短链接走 jsDelivr 全球 CDN；短链接网关为 Cloudflare Worker（`tracker.pmwiu.com`）。
> qBittorrent、Aria2 等客户端直接粘贴短链接即可订阅。

<details>
<summary><b>按协议 / 按源订阅</b>（点击展开，均为 txt 短链接）</summary>

**按协议** `/p/<协议>.txt`（加速：前缀加 `/jsd/`）

| udp | http | https | wss | ws |
|---|---|---|---|---|
| `tracker.pmwiu.com/p/udp.txt` | `tracker.pmwiu.com/p/http.txt` | `tracker.pmwiu.com/p/https.txt` | `tracker.pmwiu.com/p/wss.txt` | `tracker.pmwiu.com/p/ws.txt` |

**按源** `/src/<源>.txt`

| cf best | trackers.run | ngosang best | ngosang best-ip | OpenTracker |
|---|---|---|---|---|
| `tracker.pmwiu.com/src/cf_best.txt` | `tracker.pmwiu.com/src/run_best.txt` | `tracker.pmwiu.com/src/ngosang_best.txt` | `tracker.pmwiu.com/src/ngosang_best_ip.txt` | `tracker.pmwiu.com/src/opentracker.txt` |

</details>

## 机制

- **聚合**：5 个国际精选源按优先级合并，来源白名单 + 内容校验 + 原子写入
- **清洗**：URL 规范化去重、同 IP 保留最快、动态黑名单（连续失效自动下线）
- **探活**：HTTP/HTTPS 验证 bencoded announce 响应、UDP connect+announce 握手、WSS/WS TLS 连通；>5s 低速淘汰
- **评分**：速度 70% + 历史稳定性 EMA 30%；best 保底 4 条非 UDP（协议多样性配额）
- **托管**：GitHub Pages + Cloudflare Pages 双托管，Worker 短链接网关，`/jsd/` 前缀切换 jsDelivr 加速
- **监控**：定时任务 + 心跳 + 运行摘要 + 失败自动告警 Issue + 3 轮网络健康检查

## 链接

- 订阅主页：`https://tracker.pmwiu.com/`
- 完整地址清单（含各镜像长链接）：[`trackers/MIRRORS.txt`](trackers/MIRRORS.txt)
- 变更记录：[`CHANGELOG.md`](CHANGELOG.md) · 安全说明：[`SECURITY.md`](SECURITY.md)
- Cloudflare Worker 源码：[`cloudflare/tracker-proxy.js`](cloudflare/tracker-proxy.js)
