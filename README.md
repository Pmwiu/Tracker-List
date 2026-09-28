# Tracker List 自动订阅、活性测试与短链接服务


## 三大自动化能力

1. **自动检索更新**：定时拉取 6 类公开 Tracker 列表
2. **自动去重**：跨源合并，去除重复 Tracker
3. **自动活性测试与剔除**：对每个 Tracker 发起协议级探活，失效节点自动剔除

## 推荐订阅地址

```
https://pmwiu.github.io/Tracker-List/s/alive
```

`/s/alive` 只包含通过活性测试的 Tracker，最稳定。若被 DNS 污染，依次尝试 CDN 备用链接。

## 短链接一览

基础域名：`https://pmwiu.github.io/Tracker-List`

### 核心订阅

| 短链接 | 说明 |
|--------|------|
| `/s/alive` | **存活 Tracker（经活性测试，最推荐）** |
| `/s/alive-cdn` | 存活 Tracker（jsDelivr CDN） |
| `/s/all` | 完整合并总表（Raw 直连） |
| `/s/all-cdn` | 完整总表（jsDelivr CDN） |
| `/s/all-fastly` | 完整总表（Fastly） |
| `/s/all-gcore` | 完整总表（Gcore） |
| `/s/all-proxy` | 完整总表（ghproxy） |

### 分类列表

| 短链接 | 说明 |
|--------|------|
| `/s/trackers` | 全部 Tracker |
| `/s/ip` | IP 类 Tracker |
| `/s/ws` | WebSocket 类 Tracker |
| `/s/i2p` | I2P 网络 Tracker |
| `/s/ygg` | Yggdrasil 网络 Tracker |
| `/s/ygg-ip` | Yggdrasil IP 类 Tracker |
| `/s/repo` | GitHub 仓库主页 |

## 活性测试原理

- **HTTP/HTTPS**：发送标准 BitTorrent announce 请求，验证 bencoded 响应
- **UDP**：完整 UDP Tracker 握手（connect + announce）
- **WSS**：TCP + TLS 连通性检查
- **I2P（.i2p）**：标记为 untestable（需 I2P 网络）

输出 trackers_alive.txt（存活）、trackers_dead.txt（失效）、test_report.md（报告）。

## DNS 防污染

6 条独立链路：GitHub Raw、jsDelivr、Fastly、Gcore、ghproxy、gh-proxy。清单见 MIRRORS.txt。

## 自动维护（GitHub Actions）

工作流每天 UTC 00:00（北京时间 08:00）执行：下载 6 类源 → 合并去重 → 活性测试 → 剔除失效 → 自动提交 → 健康检查。支持手动触发。

## 本地运行

```bash
python scripts/update_trackers.py
python scripts/test_trackers.py --timeout 12 --workers 25
python scripts/health_check.py --rounds 10
```

## 项目结构

```
Tracker-List/
├── .github/workflows/update-trackers.yml
├── scripts/
│   ├── update_trackers.py    # 下载、合并、去重、短链接
│   ├── test_trackers.py      # 活性测试
│   └── health_check.py       # 健康检查
├── trackers/
│   ├── trackers_merged.txt   # 完整合并去重总表
│   ├── trackers_alive.txt    # 存活列表（推荐）
│   ├── trackers_dead.txt     # 失效列表
│   ├── test_report.md        # 测试报告
│   └── MIRRORS.txt           # CDN 镜像清单
├── docs/                     # GitHub Pages（自动生成）
│   ├── index.html
│   └── s/                    # 短链接重定向页面
└── README.md
```
