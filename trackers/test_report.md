# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-08 13:49:27 UTC
- 总 Tracker 数: 100
- 存活 (alive): **69** (69%)
- 失效 (dead): **17**
- 不安全 (unsafe): **2**
- 无法测试 (untestable): 12
- 低速淘汰 (low-speed >5s): 0
- 同网段去重 (/24, kept faster): 31
- 综合评分后保留前 20 个，淘汰 18 个
- 评分维度: 速度 60% + 历史稳定性 25% + 响应质量 15%（速度标度自适应 + 经典高可用加分）
- 配额: 保底 4 条非 UDP + 保底 4 条经典高可用
- 协议多样性配额: 保底 4 条非 UDP，实际保留 5 条
- 耗时: 20.5 秒

## 协议分布

- http: 30
- udp: 27
- https: 11
- wss: 1

## 最终订阅列表（前 20 个，按综合评分降序）

1. `udp://tracker.opentrackr.org:1337/announce` — score=99.0, 88ms, 存活率93%, 质量100, 经典+6
2. `http://tracker.renfei.net:8080/announce` — score=97.9, 29ms, 存活率99%, 质量100, 经典+0
3. `https://t.213891.xyz:443/announce` — score=97.3, 39ms, 存活率99%, 质量100, 经典+0
4. `https://1.tracker.eu.org:443/announce` — score=97.0, 43ms, 存活率99%, 质量100, 经典+0
5. `wss://tracker.openwebtorrent.com:443/announce` — score=96.9, 21ms, 存活率99%, 质量90, 经典+0
6. `udp://tracker.004430.xyz:1337/announce` — score=96.0, 61ms, 存活率99%, 质量100, 经典+0
7. `udp://tracker.bittor.pw:1337/announce` — score=95.4, 26ms, 存活率88%, 质量100, 经典+0
8. `udp://exodus.desync.com:6969/announce` — score=94.6, 76ms, 存活率73%, 质量100, 经典+6
9. `udp://209.141.59.25:6969/announce` — score=93.5, 62ms, 存活率89%, 质量100, 经典+0
10. `udp://tracker.nyaa.vc:6969/announce` — score=93.4, 84ms, 存活率94%, 质量100, 经典+0
11. `udp://tracker-udp.gbitt.info:80/announce` — score=93.4, 84ms, 存活率94%, 质量100, 经典+0
12. `udp://tracker.torrent.eu.org:451/announce` — score=93.4, 113ms, 存活率77%, 质量100, 经典+6
13. `udp://23.157.120.14:6969/announce` — score=93.1, 79ms, 存活率91%, 质量100, 经典+0
14. `udp://151.242.104.187:80/announce` — score=92.3, 92ms, 存活率91%, 质量100, 经典+0
15. `udp://135.125.198.235:1984/announce` — score=91.9, 88ms, 存活率89%, 质量100, 经典+0
16. `udp://tracker.skynetcloud.site:6969/announce` — score=91.6, 86ms, 存活率87%, 质量100, 经典+0
17. `udp://31.56.179.159:6969/announce` — score=91.4, 108ms, 存活率91%, 质量100, 经典+0
18. `http://140.235.237.23:6969/announce` — score=90.7, 46ms, 存活率74%, 质量100, 经典+0
19. `udp://t.overflow.biz:6969/announce` — score=89.8, 115ms, 存活率87%, 质量100, 经典+0
20. `udp://retracker01-msk-virt.corbina.net:80/announce` — score=88.8, 131ms, 存活率87%, 质量100, 经典+0

## 失效 Tracker

- `http://echostar.ddnsfree.com:8080/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://retracker.hotplug.ru:2710/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://ht.therarbg.to:443/announce` — timeout
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [Errno 104] Connection reset by peer>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.bt4g.com:443/announce` — timeout
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `udp://208.83.20.20:6969/announce` — no connect response
- `udp://6ahddutb1ucc3cp.ru:6969/announce` — no connect response
- `udp://explodie.org:6969/announce` — no connect response
- `udp://torrentclub.online:54123/announce` — no connect response
- `udp://torrents.tmtime.dev:6969/announce` — no connect response
- `udp://tracker.alaskantf.com:6969/announce` — no connect response
- `udp://tracker.tryhackx.org:6969/announce` — no connect response

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
- `http://152.249.214.196:6969/announce`
- `http://211.75.205.187:6969/announce`
- `http://211.75.205.188:80/announce`
- `http://211.75.210.221:6969/announce`
- `http://211.75.210.221:80/announce`
- `http://announce.sktorrent.eu:6969/announce`
- `http://ipv4announce.sktorrent.eu:6969/announce`
- `http://retracker01-msk-virt.corbina.net:80/announce`
- `http://tracker.auctor.tv:6969/announce`
- `http://tracker.dhitechnical.com:6969/announce`
- `http://tracker.dler.com:6969/announce`
- `http://tracker.dler.org:6969/announce`
- `http://tracker.mywaifu.best:6969/announce`
- `http://tracker.nyaa.vc:6969/announce`
- `http://tracker.opentrackr.org:1337/announce`
- `http://tracker.qu.ax:6969/announce`
- `https://004430.xyz:443/announce`
- `https://3.tracker.eu.org:443/announce`
- `https://337hhh.xyz:443/announce`
- `udp://109.201.134.183:80/announce`
- `udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce`
- `udp://open.demonii.com:1337/announce`
- `udp://open.stealth.si:80/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.ducks.party:1984/announce`
- `udp://tracker.gmi.gd:6969/announce`
- `udp://tracker.qu.ax:6969/announce`
- `udp://tracker2.dler.org:80/announce`
