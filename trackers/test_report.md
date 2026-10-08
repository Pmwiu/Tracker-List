# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-08 10:48:58 UTC
- 总 Tracker 数: 100
- 存活 (alive): **64** (64%)
- 失效 (dead): **18**
- 不安全 (unsafe): **2**
- 无法测试 (untestable): 16
- 低速淘汰 (low-speed >5s): 0
- 同网段去重 (/24, kept faster): 24
- 综合评分后保留前 20 个，淘汰 20 个
- 评分维度: 速度 60% + 历史稳定性 25% + 响应质量 15%（速度标度自适应）
- 协议多样性配额: 保底 4 条非 UDP，实际保留 4 条
- 耗时: 20.7 秒

## 协议分布

- udp: 40
- http: 13
- https: 10
- wss: 1

## 最终订阅列表（前 20 个，按综合评分降序）

1. `udp://tracker.004430.xyz:1337/announce` — score=97.2, 10ms, 存活率91%, 质量100
2. `https://t.213891.xyz:443/announce` — score=96.8, 18ms, 存活率91%, 质量100
3. `https://1.tracker.eu.org:443/announce` — score=96.6, 21ms, 存活率91%, 质量100
4. `wss://tracker.openwebtorrent.com:443/announce` — score=95.9, 8ms, 存活率91%, 质量90
5. `udp://explodie.org:6969/announce` — score=88.7, 6ms, 存活率56%, 质量100
6. `http://tracker.renfei.net:8080/announce` — score=88.2, 161ms, 存活率91%, 质量100
7. `udp://exodus.desync.com:6969/announce` — score=86.5, 5ms, 存活率47%, 质量100
8. `udp://tracker.ducks.party:1984/announce` — score=85.5, 152ms, 存活率79%, 质量100
9. `udp://209.141.59.25:6969/announce` — score=82.1, 18ms, 存活率33%, 质量100
10. `udp://tracker.nyaa.vc:6969/announce` — score=82.0, 145ms, 存活率63%, 质量100
11. `udp://tracker.opentrackr.org:1337/announce` — score=80.8, 145ms, 存活率58%, 质量100
12. `udp://34.66.57.33:1337/announce` — score=80.4, 46ms, 存活率33%, 质量100
13. `udp://109.201.134.183:80/announce` — score=78.4, 146ms, 存活率49%, 质量100
14. `udp://185.121.168.96:1337/announce` — score=78.4, 147ms, 存活率49%, 质量100
15. `udp://31.56.179.159:6969/announce` — score=77.0, 170ms, 存活率49%, 质量100
16. `udp://211.75.205.188:6969/announce` — score=74.9, 138ms, 存活率33%, 质量100
17. `udp://tracker2.dler.org:80/announce` — score=71.7, 139ms, 存活率20%, 质量100
18. `udp://43.250.54.126:6969/announce` — score=71.1, 149ms, 存活率20%, 质量100
19. `udp://open.stealth.si:80/announce` — score=71.0, 150ms, 存活率20%, 质量100
20. `udp://t.overflow.biz:6969/announce` — score=69.9, 169ms, 存活率20%, 质量100

## 失效 Tracker

- `http://torrentsmd.com:8080/announce` — HTTPError: HTTP Error 403: Forbidden
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://ht.therarbg.to:443/announce` — timeout
- `https://torrent.tracker.durukanbal.com:443/announce` — URLError: <urlopen error timed out>
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.bt4g.com:443/announce` — timeout
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tracker1.520.jp:443/announce` — HTTPError: HTTP Error 521: <none>
- `udp://6ahddutb1ucc3cp.ru:6969/announce` — no connect response
- `udp://torrentclub.online:54123/announce` — no connect response
- `udp://torrents.tmtime.dev:6969/announce` — no connect response
- `udp://tracker.alaskantf.com:6969/announce` — no connect response
- `udp://tracker.filemail.com:6969/announce` — no connect response
- `udp://tracker.publictracker.xyz:6969/announce` — no connect response
- `udp://tracker.srv00.com:6969/announce` — no connect response

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
- `udp://freetracker.i2p:1337/announce` — I2P network required
- `udp://opentracker.simp.i2p:6969/a` — I2P network required

## 同网段去重（/24，保留响应最快）

- `http://1337.abcvg.info:80/announce`
- `http://211.75.205.187:6969/announce`
- `http://tracker.dler.com:6969/announce`
- `http://tracker.dler.org:6969/announce`
- `http://tracker.opentrackr.org:1337/announce`
- `udp://135.125.198.235:1984/announce`
- `udp://151.242.104.187:80/announce`
- `udp://211.75.205.188:80/announce`
- `udp://23.157.120.14:6969/announce`
- `udp://34.66.57.33:80/announce`
- `udp://45.137.199.107:6969/announce`
- `udp://83.102.180.21:80/announce`
- `udp://leet-tracker.moe:1337/announce`
- `udp://open.demonii.com:1337/announce`
- `udp://tracker-udp.gbitt.info:80/announce`
- `udp://tracker.auctor.tv:6969/announce`
- `udp://tracker.bittor.pw:1337/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.dler.org:6969/announce`
- `udp://tracker.farted.net:6969/announce`
- `udp://tracker.gmi.gd:6969/announce`
- `udp://tracker.peerfect.org:6969/announce`
- `udp://tracker.qu.ax:6969/announce`
- `udp://tracker.skynetcloud.site:6969/announce`
