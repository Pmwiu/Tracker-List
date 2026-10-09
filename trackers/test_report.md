# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-09 18:26:29 UTC
- 总 Tracker 数: 100
- 存活 (alive): **71** (71%)
- 失效 (dead): **15**
- 不安全 (unsafe): **2**
- 无法测试 (untestable): 12
- 低速淘汰 (low-speed >5s): 0
- 同网段去重 (/24, kept faster): 34
- 综合评分后保留前 20 个，淘汰 17 个
- 评分维度: 速度 60% + 历史稳定性 25% + 响应质量 15%（速度标度自适应 + 经典高可用加分）
- 配额: 保底 4 条非 UDP + 保底 4 条经典高可用
- 协议多样性配额: 保底 4 条非 UDP，实际保留 6 条
- 耗时: 18.7 秒

## 协议分布

- udp: 31
- http: 29
- https: 10
- wss: 1

## 最终订阅列表（前 20 个，按综合评分降序）

1. `udp://tracker.opentrackr.org:1337/announce` — score=100.0, 88ms, 存活率97%, 质量100, 经典+6
2. `udp://open.stealth.si:80/announce` — score=98.7, 98ms, 存活率95%, 质量100, 经典+6
3. `udp://tracker.torrent.eu.org:451/announce` — score=98.2, 91ms, 存活率90%, 质量100, 经典+6
4. `https://1.tracker.eu.org:443/announce` — score=97.7, 37ms, 存活率99%, 质量100, 经典+0
5. `http://tracker.renfei.net:8080/announce` — score=97.6, 38ms, 存活率99%, 质量100, 经典+0
6. `https://t.213891.xyz:443/announce` — score=97.5, 39ms, 存活率99%, 质量100, 经典+0
7. `udp://tracker.corpscorp.online:80/announce` — score=97.1, 29ms, 存活率95%, 质量100, 经典+0
8. `wss://tracker.openwebtorrent.com:443/announce` — score=96.8, 27ms, 存活率99%, 质量90, 经典+0
9. `udp://tracker.004430.xyz:1337/announce` — score=96.2, 61ms, 存活率99%, 质量100, 经典+0
10. `udp://tracker.gmi.gd:6969/announce` — score=96.0, 61ms, 存活率99%, 质量100, 经典+0
11. `udp://exodus.desync.com:6969/announce` — score=94.8, 74ms, 存活率73%, 质量100, 经典+6
12. `udp://tracker.ducks.party:1984/announce` — score=94.2, 91ms, 存活率99%, 质量100, 经典+0
13. `http://140.235.237.23:6969/announce` — score=94.1, 53ms, 存活率89%, 质量100, 经典+0
14. `udp://tracker-udp.gbitt.info:80/announce` — score=94.1, 88ms, 存活率97%, 质量100, 经典+0
15. `udp://tracker.nyaa.vc:6969/announce` — score=94.0, 90ms, 存活率97%, 质量100, 经典+0
16. `udp://explodie.org:6969/announce` — score=93.6, 84ms, 存活率71%, 质量100, 经典+6
17. `udp://tracker.skynetcloud.site:6969/announce` — score=93.5, 87ms, 存活率95%, 质量100, 经典+0
18. `udp://31.56.179.159:6969/announce` — score=92.5, 110ms, 存活率96%, 质量100, 经典+0
19. `udp://t.overflow.biz:6969/announce` — score=91.7, 116ms, 存活率95%, 质量100, 经典+0
20. `https://3.tracker.eu.org:443/announce` — score=91.0, 41ms, 存活率74%, 质量100, 经典+0

## 失效 Tracker

- `http://echostar.ddnsfree.com:8080/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://retracker.hotplug.ru:2710/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://ht.therarbg.to:443/announce` — timeout
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [Errno 104] Connection reset by peer>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.bt4g.com:443/announce` — timeout
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tracker.zhuqiy.com:443/announce` — timeout
- `udp://6ahddutb1ucc3cp.ru:6969/announce` — no connect response
- `udp://torrentclub.online:54123/announce` — no connect response
- `udp://torrents.tmtime.dev:6969/announce` — no connect response
- `udp://tracker.alaskantf.com:6969/announce` — no connect response

## 不安全 Tracker（已过滤）

- `http://yggtracker.i2p.rocks:80/announce` — resolves to private IP: 200:1e2f:e608:eb3a:2bf:1e62:87ba:e2f7
- `udp://open.dstud.io:6969/announce` — resolves to private IP: 0.0.0.0

## 无法测试（特殊网络）

- `http://[2605:6400:30:fad6::dead:c0d3]:1337/announce` — IPv6 unavailable here
- `http://[2a04:ac00:1:3dd8::1:2710]:2710/announce` — IPv6 unavailable here
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

## 同网段去重（/24，保留响应最快）

- `http://107.189.2.131:1337/announce`
- `http://135.125.198.235:2710/announce`
- `http://135.125.198.235:80/announce`
- `http://211.75.205.187:6969/announce`
- `http://211.75.205.187:80/announce`
- `http://211.75.205.188:80/announce`
- `http://211.75.210.221:6969/announce`
- `http://211.75.210.221:80/announce`
- `http://94.23.207.177:6969/announce`
- `http://announce.sktorrent.eu:6969/announce`
- `http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce`
- `http://tracker.auctor.tv:6969/announce`
- `http://tracker.dhitechnical.com:6969/announce`
- `http://tracker.dler.com:6969/announce`
- `http://tracker.dler.org:6969/announce`
- `http://tracker.mywaifu.best:6969/announce`
- `http://tracker.nyaa.vc:6969/announce`
- `http://tracker.opentrackr.org:1337/announce`
- `http://tracker.qu.ax:6969/announce`
- `https://004430.xyz:443/announce`
- `https://2.tracker.eu.org:443/announce`
- `https://337hhh.xyz:443/announce`
- `udp://109.201.134.183:80/announce`
- `udp://135.125.198.235:1984/announce`
- `udp://151.242.104.187:80/announce`
- `udp://209.141.59.25:6969/announce`
- `udp://211.75.210.221:6969/announce`
- `udp://34.66.57.33:1337/announce`
- `udp://34.66.57.33:80/announce`
- `udp://open.demonii.com:1337/announce`
- `udp://tracker.bittor.pw:1337/announce`
- `udp://tracker.farted.net:6969/announce`
- `udp://tracker.qu.ax:6969/announce`
- `udp://tracker2.dler.org:80/announce`
