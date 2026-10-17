<div align="center">

# Tracker List

生产级 BitTorrent Tracker 订阅服务 · 自动聚合 · 协议级探活 · 多维综合评分

<img src="https://img.shields.io/github/actions/workflow/status/Pmwiu/Tracker-List/update-trackers.yml?branch=main&label=build&style=flat-square" alt="build">
<img src="https://img.shields.io/badge/all-59-2563eb?style=flat-square" alt="all 59">
<img src="https://img.shields.io/badge/sources-14-2563eb?style=flat-square" alt="14 sources">
<img src="https://img.shields.io/badge/secure-no%20secrets-16a34a?style=flat-square" alt="no secrets">

</div>

---

## 订阅

| 计划 | 条数 | 短链接 (txt) | 加速短链接 (txt) |
|:---:|:---:|---|---|
| **all** 存活 | 59 | `https://tracker.pmwiu.com/all.txt` | `https://tracker.pmwiu.com/jsd/all.txt` |

> 短链接由 Cloudflare Worker 网关提供；加速短链接走 jsDelivr 全球 CDN。
> qBittorrent、Aria2 等客户端直接粘贴短链接即可订阅。

<details>
<summary><b>按协议 / 按源订阅</b></summary>

**按协议** `/p/<协议>.txt`（加速：前缀加 `/jsd/`）

`tracker.pmwiu.com/p/udp.txt` · `/p/http.txt` · `/p/https.txt` · `/p/wss.txt` · `/p/ws.txt`

**按源** `/src/<源>.txt`（覆盖全部 14 个源，如 `/src/ngosang_best.txt`、`/src/adysec_best.txt`、`/src/pexcn_best.txt`）

</details>

## 可靠性

- **更新**：每 6 小时自动更新（定时计划 + 手动触发）
- **测活**：协议级活性测试（HTTP bencoded announce 校验 / UDP connect+announce 握手 / WSS TLS / WS TCP）、IPv4/IPv6 双栈、低速淘汰、announce peers 计数、BEP 15 scrape 热度探针
- **筛选**：同网段(/24) + 同域名去重（ngosang 方法）、动态黑名单 + 知名项目远程黑名单（ngosang/XIU2，精确 URL 屏蔽）
- **评分**：速度 50% + 历史稳定性 EMA 20% + 响应质量 15%（含 peers/scrape 热度）+ 跨源一致性 10% + 近期成功率 5%，速度标度自适应 + 经典高可用加分 + 反退化惩罚
- **自动发现**：从 GitHub topic + 公开全量列表（cf.trackerslist / ngosang all）发现候选，探活评分后与 all 隔离，供人工审查转正
- **监控**：心跳 + 运行摘要 + 失败自动告警 + 全量健康检查（3 轮全绿）

## 安全

- 仓库不包含、不存储任何密码 / 令牌 / API Key
- 工作流使用最小权限临时 `GITHUB_TOKEN`，来源白名单校验，拒绝非白名单内容
- 仅支持 `udp / http / https / wss / ws` 协议，排除 localhost、内网、保留段等不安全地址
- 自动发现的候选永不直接进入 all 订阅，转正须人工审查（防污染）

## 链接

- 订阅主页：`https://tracker.pmwiu.com/`
- 完整地址清单：[`trackers/MIRRORS.txt`](trackers/MIRRORS.txt)
- 变更记录：[`CHANGELOG.md`](CHANGELOG.md) · 安全策略：[`SECURITY.md`](SECURITY.md)
- Worker 源码：[`cloudflare/tracker-proxy.js`](cloudflare/tracker-proxy.js)
