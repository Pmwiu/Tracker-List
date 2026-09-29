# Tracker List 自动订阅、活性测试与短链接服务

自动从 [ngosang/trackerslist](https://github.com/ngosang/trackerslist) 检索 Tracker，**合并去重、协议级活性测试、自动剔除失效节点**，通过 GitHub Pages 提供 7×24H 短链接服务，每 24 小时自动维护。

## 三大自动化能力

1. **自动检索更新**：定时拉取 6 类公开 Tracker 列表
2. **自动去重**：跨源合并，去除重复 Tracker
3. **自动活性测试与剔除**：对每个 Tracker 发起协议级探活，失效节点自动剔除

## 推荐订阅地址

```
https://pmwiu.github.io/Tracker-List/s/alive
```

`/s/alive` 只包含通过活性测试的 Tracker，最稳定。若被 DNS 污染，依次尝试下表中的 CDN 备用链接。

## 短链接一览

基础域名：`https://pmwiu.github.io/Tracker-List`

### 核心订阅

| 短链接 | 说明 |
|--------|------|
| `/s/alive` | **存活 Tracker（经活性测试，最推荐）** |
| `/s/alive-cdn` | 存活 Tracker（jsDelivr CDN） |
| `/s/all` | 完整合并总表（Raw 直连） |
| `/s/all-cdn` | 完整总表（jsDelivr CDN） |
| `/s/all-fastly` | 完整总表（Fastly 节点） |
| `/s/all-gcore` | 完整总表（Gcore 节点） |
| `/s/all-proxy` | 完整总表（ghproxy 代理） |

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

## 数据源（6 类）

| 文件 | 协议类型 |
|------|---------|
| `trackers_all.txt` | 全部（HTTP/UDP） |
| `trackers_all_ip.txt` | IP 直连 |
| `trackers_all_ws.txt` | WebSocket (wss) |
| `trackers_all_i2p.txt` | I2P 匿名网络 |
| `trackers_all_yggdrasil.txt` | Yggdrasil 网络 |
| `trackers_all_yggdrasil_ip.txt` | Yggdrasil IP |

## 活性测试原理

对每个 Tracker 执行协议级探活（25 并发，单个超时 12 秒）：

- **HTTP/HTTPS**：发送标准 BitTorrent `announce` 请求（携带 info_hash、peer_id 等参数），验证返回的 bencoded 响应
- **UDP**：完整 UDP Tracker 握手（`connect` + `announce`），验证 connection_id 与事务 ID
- **WSS**：TCP + TLS 连通性检查
- **I2P（.i2p 域名）**：标记为 untestable（需 I2P 网络，普通环境无法测试）

测试结果：

- `trackers/trackers_alive.txt` — 通过测试的存活 Tracker
- `trackers/trackers_dead.txt` — 未通过测试的失效 Tracker
- `trackers/test_report.md` — 测试报告（存活/失效明细）

## DNS 防污染策略

提供 6 条独立链路，任一被污染时切换其他链路：

1. GitHub Raw 直连
2. jsDelivr CDN（cdn.jsdelivr.net）
3. jsDelivr Fastly（fastly.jsdelivr.net）
4. jsDelivr Gcore（gcore.jsdelivr.net）
5. ghproxy 代理（ghproxy.net）
6. gh-proxy 代理（gh-proxy.com）

镜像地址清单见 `trackers/MIRRORS.txt`。

## 自动维护流程（GitHub Actions）

工作流 `.github/workflows/update-trackers.yml` 每天 UTC 00:00（北京时间 08:00）自动执行：

```
下载 6 类源 → 合并去重 → 协议级活性测试 → 剔除失效 → 检测变更 → 自动提交推送 → 健康检查
```

- 支持手动触发（Actions 页面 → Run workflow）
- 无变化时不产生空提交
- 下载失败自动重试 3 次
- 每次更新后自动运行 3 轮健康检查

## 本地手动运行

```bash
# 1. 下载、合并、去重、生成短链接
python scripts/update_trackers.py

# 2. 活性测试，剔除失效 Tracker
python scripts/test_trackers.py --timeout 12 --workers 25

# 3. 健康检查（可指定轮数）
python scripts/health_check.py --rounds 10
```

## 项目结构

```
Tracker-List/
├── .github/workflows/update-trackers.yml   # 自动维护工作流
├── scripts/
│   ├── update_trackers.py                  # 下载、合并、去重、短链接生成
│   ├── test_trackers.py                   # 协议级活性测试
│   └── health_check.py                    # 健康检查
├── trackers/                              # Tracker 列表
│   ├── trackers_all.txt
│   ├── trackers_all_ip.txt
│   ├── trackers_all_ws.txt
│   ├── trackers_all_i2p.txt
│   ├── trackers_all_yggdrasil.txt
│   ├── trackers_all_yggdrasil_ip.txt
│   ├── trackers_merged.txt                # 完整合并去重总表
│   ├── trackers_alive.txt                 # 存活列表（推荐）
│   ├── trackers_dead.txt                  # 失效列表
│   ├── test_report.md                     # 测试报告
│   └── MIRRORS.txt                        # CDN 镜像清单
├── docs/                                  # GitHub Pages（自动生成）
│   ├── index.html
│   ├── .nojekyll
│   └── s/                                 # 短链接重定向页面
└── README.md
```
