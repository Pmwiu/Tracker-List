# Tracker List

精选 BitTorrent Tracker 订阅 · 每 6 小时自动更新 · GitHub + Cloudflare 双托管

## 订阅地址

| 计划 | 条数上限 | txt 订阅链接 |
|------|---------|-------------|
| **best 存活**（推荐） | 59 | `https://tracker.pmwiu.com/alive.txt` |
| **all 合并** | 599 | `https://tracker.pmwiu.com/merged.txt` |

备用通道：`https://pmwiu.github.io/Tracker-List/alive.txt`、`https://pmwiu.github.io/Tracker-List/merged.txt`

完整多通道清单见 [`trackers/MIRRORS.txt`](trackers/MIRRORS.txt)。

## 订阅源（21 个，按仓库分组）

### cf.trackerslist.com（2）
| 源 | 条数 |
|----|------|
| https://cf.trackerslist.com/best.txt | 71 |
| https://cf.trackerslist.com/all.txt | 118 |

### ngosang/trackerslist（7）
| 源 | 条数 |
|----|------|
| https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best_ip.txt | 20 |
| https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt | 20 |
| https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt | 74 |
| https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ip.txt | 55 |
| https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_i2p.txt | 17 |
| https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_yggdrasil.txt | 1 |
| https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_yggdrasil_ip.txt | 4 |

### adysec/tracker（6）
| 源 | 条数 |
|----|------|
| https://tracker.adysec.com/trackers_best.txt | 332 |
| https://tracker.adysec.com/trackers_best_http.txt | 131 |
| https://tracker.adysec.com/trackers_best_https.txt | 32 |
| https://tracker.adysec.com/trackers_best_udp.txt | 163 |
| https://tracker.adysec.com/trackers_best_wss.txt | 6 |
| https://raw.githubusercontent.com/adysec/tracker/refs/heads/main/trackers_all.txt | 3535 |

### pkgforge-security/Trackers（2）
| 源 | 条数 |
|----|------|
| https://raw.githubusercontent.com/pkgforge-security/Trackers/refs/heads/main/trackers_all.txt | 970 |
| https://raw.githubusercontent.com/pkgforge-security/Trackers/refs/heads/main/trackers_all_general.txt | 105 |

### DeSireFire/animeTrackerList（2）
| 源 | 条数 |
|----|------|
| https://raw.githubusercontent.com/DeSireFire/animeTrackerList/refs/heads/master/ATline_best.txt | 25 |
| https://raw.githubusercontent.com/DeSireFire/animeTrackerList/refs/heads/master/ATline_best_ip.txt | 1 |

### kris3713/UltimateBTTrackersList（1）
| 源 | 条数 |
|----|------|
| https://raw.githubusercontent.com/kris3713/UltimateBTTrackersList/refs/heads/master/ultimate_trackers.txt | 183 |

### 1265578519/OpenTracker（1）
| 源 | 条数 |
|----|------|
| https://raw.githubusercontent.com/1265578519/OpenTracker/master/tracker.txt | 38 |

## 特性

- 21 个源合并去重（按仓库分类，受白名单保护）
- 协议级活性测试（HTTP/HTTPS/UDP/WSS/WS）+ 综合评分：速度 70% + 稳定性 30%
- 低速淘汰（>5s）、同 IP 去重、域名黑名单、失败降级备份、测试熔断
- all 计划按源优先级取前 599 条（精选源优先）
- 每 6 小时自动更新 · GitHub Pages/Raw + Cloudflare Pages 双托管

## 许可

仅供个人订阅使用，Tracker 内容版权归各来源所有。
