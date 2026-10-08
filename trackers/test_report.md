# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-08 13:15:29 UTC
- 总 Tracker 数: 100
- 存活 (alive): **71** (71%)
- 失效 (dead): **13**
- 不安全 (unsafe): **2**
- 无法测试 (untestable): 14
- 低速淘汰 (low-speed >5s): 0
- 同网段去重 (/24, kept faster): 32
- 综合评分后保留前 20 个，淘汰 19 个
- 评分维度: 速度 60% + 历史稳定性 25% + 响应质量 15%（速度标度自适应 + 经典高可用加分）
- 配额: 保底 4 条非 UDP + 保底 4 条经典高可用
- 协议多样性配额: 保底 4 条非 UDP，实际保留 6 条
- 耗时: 19.9 秒

## 协议分布

- udp: 37
- http: 22
- https: 11
- wss: 1

## 最终订阅列表（前 20 个，按综合评分降序）

1. `udp://explodie.org:6969/announce` — score=101.5, 28ms, 存活率88%, 质量100, 经典+6
2. `udp://tracker.004430.xyz:1337/announce` — score=97.6, 30ms, 存活率98%, 质量100, 经典+0
3. `https://t.213891.xyz:443/announce` — score=97.4, 34ms, 存活率98%, 质量100, 经典+0
4. `wss://tracker.openwebtorrent.com:443/announce` — score=97.1, 15ms, 存活率98%, 质量90, 经典+0
5. `udp://tracker.gmi.gd:6969/announce` — score=96.2, 39ms, 存活率94%, 质量100, 经典+0
6. `udp://tracker.opentrackr.org:1337/announce` — score=94.3, 149ms, 存活率89%, 质量100, 经典+6
7. `udp://exodus.desync.com:6969/announce` — score=93.5, 31ms, 存活率57%, 质量100, 经典+6
8. `udp://open.demonii.com:1337/announce` — score=92.7, 135ms, 存活率79%, 质量100, 经典+6
9. `udp://tracker.corpscorp.online:80/announce` — score=92.6, 49ms, 存活率82%, 质量100, 经典+0
10. `http://tracker.renfei.net:8080/announce` — score=91.7, 130ms, 存活率98%, 质量100, 经典+0
11. `udp://tracker.ducks.party:1984/announce` — score=89.5, 152ms, 存活率94%, 质量100, 经典+0
12. `https://tracker.nekomi.cn:443/announce` — score=89.2, 92ms, 存活率79%, 质量100, 经典+0
13. `udp://109.201.134.183:80/announce` — score=88.3, 138ms, 存活率87%, 质量100, 经典+0
14. `udp://211.75.205.188:80/announce` — score=88.0, 131ms, 存活率83%, 质量100, 经典+0
15. `udp://151.242.104.187:80/announce` — score=87.8, 148ms, 存活率87%, 质量100, 经典+0
16. `udp://tracker.torrent.eu.org:451/announce` — score=87.3, 159ms, 存活率64%, 质量100, 经典+6
17. `udp://tracker2.dler.org:80/announce` — score=86.9, 131ms, 存活率79%, 质量100, 经典+0
18. `http://207.241.231.226:6969/announce` — score=86.8, 49ms, 存活率59%, 质量100, 经典+0
19. `udp://31.56.179.159:6969/announce` — score=86.6, 167ms, 存活率87%, 质量100, 经典+0
20. `http://207.241.226.111:6969/announce` — score=86.6, 53ms, 存活率59%, 质量100, 经典+0

## 失效 Tracker

- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://ht.therarbg.to:443/announce` — timeout
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.bt4g.com:443/announce` — timeout
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `udp://6ahddutb1ucc3cp.ru:6969/announce` — no connect response
- `udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce` — no connect response
- `udp://torrentclub.online:54123/announce` — no connect response
- `udp://torrents.tmtime.dev:6969/announce` — no connect response
- `udp://tracker.alaskantf.com:6969/announce` — no connect response

## 不安全 Tracker（已过滤）

- `http://yggtracker.i2p.rocks:80/announce` — resolves to private IP: 200:1e2f:e608:eb3a:2bf:1e62:87ba:e2f7
- `udp://open.dstud.io:6969/announce` — resolves to private IP: 0.0.0.0

## 无法测试（特殊网络）

- `http://btrackrqkjp6kgelov5a3uxisis77ofxqt5nvy5hvvtoybjpmq4q.b32.i2p:80/announce` — I2P network required
- `http://freetracker.i2p:7331/announce` — I2P network required
- `http://nyaaplus.i2p:80/announce` — I2P network required
- `http://opentracker.dg2.i2p:80/a` — I2P network required
- `http://opentracker.eeptorrent.i2p:80/a` — I2P network required
- `http://opentracker.fattydove.i2p:80/a` — I2P network required
- `http://opentracker.r4sas.i2p:80/a` — I2P network required
- `http://opentracker.simp.i2p:80/a` — I2P network required
- `http://opentracker.skank.i2p:80/a` — I2P network required
- `http://qimlze77z7w32lx2ntnwkuqslrzlsqy7774v3urueuarafyqik5a.b32.i2p:80/a` — I2P network required
- `http://sigmatracker.i2p:80/a` — I2P network required
- `http://tracker.insulaocculta.i2p:80/a` — I2P network required
- `http://tracker.nyaa2p.i2p:80/announce` — I2P network required
- `http://yet-another-public-tracker.i2p:80/announce` — I2P network required

## 同网段去重（/24，保留响应最快）

- `http://135.125.198.235:2710/announce`
- `http://135.125.198.235:80/announce`
- `http://152.249.214.196:6969/announce`
- `http://211.75.205.187:6969/announce`
- `http://211.75.205.187:80/announce`
- `http://211.75.205.188:6969/announce`
- `http://211.75.205.188:80/announce`
- `http://tracker.dhitechnical.com:6969/announce`
- `http://tracker.dler.com:6969/announce`
- `http://tracker.dler.org:6969/announce`
- `http://tracker.mywaifu.best:6969/announce`
- `http://tracker.opentrackr.org:1337/announce`
- `https://004430.xyz:443/announce`
- `https://1.tracker.eu.org:443/announce`
- `https://2.tracker.eu.org:443/announce`
- `https://337hhh.xyz:443/announce`
- `udp://135.125.198.235:1984/announce`
- `udp://185.121.168.96:1337/announce`
- `udp://209.141.59.25:6969/announce`
- `udp://211.75.205.188:6969/announce`
- `udp://23.157.120.14:6969/announce`
- `udp://34.66.57.33:1337/announce`
- `udp://34.66.57.33:80/announce`
- `udp://43.250.54.126:6969/announce`
- `udp://open.stealth.si:80/announce`
- `udp://tracker-udp.gbitt.info:80/announce`
- `udp://tracker.bittor.pw:1337/announce`
- `udp://tracker.dler.org:6969/announce`
- `udp://tracker.farted.net:6969/announce`
- `udp://tracker.nyaa.vc:6969/announce`
- `udp://tracker.peerfect.org:6969/announce`
- `udp://tracker.skynetcloud.site:6969/announce`
