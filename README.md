# Trackers List 自动订阅与短链接服务

自动从公开 GitHub 项目 [ngosang/trackerslist](https://github.com/ngosang/trackerslist) 检索 Tracker 列表，合并去重后托管在本仓库，并通过 **GitHub Pages** 提供 7×24H 稳定短链接服务，每 24 小时自动更新。

## 短链接一览

> 基础域名：`https://pmwiu.github.io/Tracker-List`

| 短链接 | 目标 | 说明 |
|--------|------|------|
| `/s/all` | `trackers_merged.txt` | **推荐订阅**，四类合并去重总表 |
| `/s/all-cdn` | jsDelivr CDN | CDN 加速备用 |
| `/s/all-fastly` | Fastly 节点 | CDN 加速备用 |
| `/s/all-gcore` | Gcore 节点 | CDN 加速备用 |
| `/s/all-proxy` | ghproxy 代理 | 代理备用 |
| `/s/trackers` | `trackers_all.txt` | 全部 Tracker |
| `/s/ip` | `trackers_all_ip.txt` | IP 类 Tracker |
| `/s/i2p` | `trackers_all_i2p.txt` | I2P 网络 Tracker |
| `/s/ygg` | `trackers_all_yggdrasil.txt` | Yggdrasil 网络 Tracker |
| `/s/repo` | GitHub 仓库主页 | 项目仓库 |

服务主页：`https://pmwiu.github.io/Tracker-List/`

## 数据源

| 文件名 | 来源 URL |
|--------|----------|
| `trackers_all.txt` | https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt |
| `trackers_all_ip.txt` | https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ip.txt |
| `trackers_all_i2p.txt` | https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_i2p.txt |
| `trackers_all_yggdrasil.txt` | https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_yggdrasil.txt |

## DNS 防污染与多 CDN 策略

为确保订阅链接在各种网络环境下均可访问，提供 6 条独立链路：

1. **GitHub Raw 直连**（默认）
2. **jsDelivr CDN**（cdn.jsdelivr.net，全球 CDN）
3. **jsDelivr Fastly**（fastly.jsdelivr.net，Fastly 节点）
4. **jsDelivr Gcore**（gcore.jsdelivr.net，Gcore 节点）
5. **ghproxy 代理**（ghproxy.net，国内代理）
6. **gh-proxy 代理**（gh-proxy.com，备用代理）

镜像地址清单见 `trackers/MIRRORS.txt`，若默认链接被污染，依次尝试备用链路。

## 自动更新机制

通过 GitHub Actions 工作流 `.github/workflows/update-trackers.yml` 实现：

- **定时触发**：每天 UTC 00:00（北京时间 08:00）自动运行
- **手动触发**：可在仓库 Actions 页面手动运行 `workflow_dispatch`
- **工作流程**：下载源列表 → 逐类去重排序 → 生成合并总表 → 生成短链接页面 → 检测变更 → 自动提交推送 → 健康检查
- **仅在有变化时提交**：无变化则不产生空提交
- **下载容错**：失败自动重试 3 次，单个源失败不影响其他源
- **自动健康检查**：每次更新后自动运行 3 轮健康检查

## 在 BitTorrent 客户端中使用

将短链接填入客户端的 Tracker 订阅地址（推荐使用合并总表）：

```
https://pmwiu.github.io/Tracker-List/s/all
```

若无法访问，依次尝试：`/s/all-cdn`、`/s/all-fastly`、`/s/all-gcore`、`/s/all-proxy`。

## 本地手动运行

```bash
python scripts/update_trackers.py
```

健康检查：

```bash
python scripts/health_check.py --rounds 10
```

## 项目结构

```
Tracker-List/
├── .github/workflows/update-trackers.yml   # GitHub Actions 自动更新工作流
├── scripts/
│   ├── update_trackers.py                  # 下载、合并、去重、短链接生成脚本
│   └── health_check.py                     # 健康检查脚本
├── trackers/                               # 自动生成的 Tracker 列表
│   ├── trackers_all.txt
│   ├── trackers_all_ip.txt
│   ├── trackers_all_i2p.txt
│   ├── trackers_all_yggdrasil.txt
│   ├── trackers_merged.txt
│   └── MIRRORS.txt                         # 多CDN镜像清单
├── docs/                                   # GitHub Pages 站点（自动生成）
│   ├── index.html
│   ├── .nojekyll
│   └── s/                                  # 短链接重定向页面
│       ├── all.html
│       ├── all-cdn.html
│       ├── all-fastly.html
│       ├── all-gcore.html
│       ├── all-proxy.html
│       ├── trackers.html
│       ├── ip.html
│       ├── i2p.html
│       ├── ygg.html
│       └── repo.html
└── README.md
```
