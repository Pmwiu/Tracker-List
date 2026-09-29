# Tracker List 自动订阅、活性测试与短链接服务

自动从 9 个 best 精选订阅源检索 Tracker，**合并去重、协议级活性测试、自动剔除失效节点**，通过 GitHub Pages 提供 7×24H 短链接服务，每 24 小时自动维护。

## 三大自动化能力

1. **自动检索更新**：定时拉取 9 个 best 精选 Tracker 订阅源
2. **自动去重**：跨源合并，规范化后去除重复 Tracker
3. **自动活性测试与剔除**：对每个 Tracker 发起协议级探活，失效/低速节点自动剔除

## 推荐订阅地址

```
https://pmwiu.github.io/Tracker-List/s/alive
```

`/s/alive` 只包含通过活性测试的最优 Tracker（最多 59 个），最稳定。所有订阅均使用 github.io / raw.githubusercontent.com 直链，无 CDN/代理加速链接。

## 短链接一览

基础域名：`https://pmwiu.github.io/Tracker-List`

| 短链接 | 说明 |
|--------|------|
| `/s/alive` | 存活 Tracker（活性测试 + 综合评分，推荐） |
| `/s/all` | 合并去重总表 |

## 数据源（9 个 best 精选源）

| 输出文件 | 来源 |
|---------|------|
| `trackers/trackers_cf_best.txt` | https://cf.trackerslist.com/best.txt |
| `trackers/trackers_ngosang_ip.txt` | https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best_ip.txt |
| `trackers/trackers_adysec_best.txt` | https://tracker.adysec.com/trackers_best.txt |
| `trackers/trackers_adysec_http.txt` | https://tracker.adysec.com/trackers_best_http.txt |
| `trackers/trackers_adysec_https.txt` | https://tracker.adysec.com/trackers_best_https.txt |
| `trackers/trackers_adysec_udp.txt` | https://tracker.adysec.com/trackers_best_udp.txt |
| `trackers/trackers_adysec_wss.txt` | https://tracker.adysec.com/trackers_best_wss.txt |
| `trackers/trackers_anime_best.txt` | https://raw.githubusercontent.com/DeSireFire/animeTrackerList/refs/heads/master/ATline_best.txt |
| `trackers/trackers_anime_ip.txt` | https://raw.githubusercontent.com/DeSireFire/animeTrackerList/refs/heads/master/ATline_best_ip.txt |

多源合并去重后生成 `trackers/trackers_merged.txt`。

## 活性测试原理

对合并列表中的 Tracker 执行协议级探活（30 并发，单个超时 10 秒，最多测试 500 个候选）：

- **HTTP/HTTPS**：发送标准 BitTorrent `announce` 请求（携带 info_hash、peer_id 等参数），验证返回的 bencoded 响应
- **UDP**：完整 UDP Tracker 握手（`connect` + `announce`），验证 connection_id 与事务 ID
- **WSS**：TCP + TLS 连通性检查
- **WS**：TCP 连通性检查
- **I2P（.i2p 域名）**：标记为 untestable（需 I2P 网络，普通环境无法测试）

评分排序：**速度 70% + 历史稳定性 30%**；响应时间超过 5 秒的 Tracker 标记为低速并排除。最终保留前 59 个写入 `trackers/trackers_alive.txt`。

测试结果：

- `trackers/trackers_alive.txt` — 通过测试的存活 Tracker（≤59）
- `trackers/trackers_dead.txt` — 未通过测试的失效 Tracker
- `trackers/test_report.md` — 测试报告（存活/失效/低速明细）

## 自动维护流程（GitHub Actions）

工作流 `.github/workflows/update-trackers.yml` 每天 UTC 00:23（北京时间 08:23）自动执行，也支持手动触发（Actions 页面 → Run workflow）：

```
下载 9 个源 → 合并去重 → 协议级活性测试 → 剔除失效/低速 → 检测变更 → 自动提交推送 → 健康检查
```

- 同一时间只允许一个实例运行（concurrency 防并发）
- 下载失败自动降级到上次成功备份
- 无变化时不产生空提交
- 每次更新后自动运行健康检查

## 本地手动运行

```bash
# 1. 下载、合并、去重、生成短链接
python scripts/update_trackers.py

# 2. 活性测试，剔除失效 Tracker
python scripts/test_trackers.py --timeout 10 --workers 30

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
│   ├── trackers_*_best.txt                # 9 个 best 订阅源输出
│   ├── trackers_merged.txt                # 完整合并去重总表
│   ├── trackers_alive.txt                 # 存活列表（推荐，≤59）
│   ├── trackers_dead.txt                  # 失效列表
│   ├── backup/                            # 降级备份 + 每日 alive 快照
│   ├── test_report.md                     # 测试报告
│   └── MIRRORS.txt                        # 订阅地址清单
├── docs/                                  # GitHub Pages（自动生成）
│   ├── index.html
│   ├── .nojekyll
│   ├── *.txt                              # 纯文本直链（alive/merged/各源）
│   └── s/                                 # 短链接重定向页面
└── README.md
```
