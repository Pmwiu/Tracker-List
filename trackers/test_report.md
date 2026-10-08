# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-08 13:51:31 UTC
- 总 Tracker 数: 100
- 存活 (alive): **80** (80%)
- 失效 (dead): **5**
- 不安全 (unsafe): **1**
- 无法测试 (untestable): 14
- 低速淘汰 (low-speed >5s): 0
- 同网段去重 (/24, kept faster): 39
- 综合评分后保留前 20 个，淘汰 21 个
- 评分维度: 速度 60% + 历史稳定性 25% + 响应质量 15%（速度标度自适应 + 经典高可用加分）
- 配额: 保底 4 条非 UDP + 保底 4 条经典高可用
- 协议多样性配额: 保底 4 条非 UDP，实际保留 5 条
- 耗时: 19.8 秒

## 协议分布

- udp: 33
- http: 31
- https: 15
- wss: 1

## 最终订阅列表（前 20 个，按综合评分降序）

1. `udp://tracker.opentrackr.org:1337/announce` — score=98.1, 108ms, 存活率94%, 质量100, 经典+6
2. `udp://tracker.004430.xyz:1337/announce` — score=96.8, 48ms, 存活率99%, 质量100, 经典+0
3. `udp://tracker.bittor.pw:1337/announce` — score=96.5, 18ms, 存活率90%, 质量100, 经典+0
4. `udp://explodie.org:6969/announce` — score=95.3, 71ms, 存活率74%, 质量100, 经典+6
5. `wss://tracker.openwebtorrent.com:443/announce` — score=95.2, 51ms, 存活率99%, 质量90, 经典+0
6. `udp://209.141.59.25:6969/announce` — score=94.7, 51ms, 存活率91%, 质量100, 经典+0
7. `udp://tracker.torrent.eu.org:451/announce` — score=93.6, 130ms, 存活率81%, 质量100, 经典+6
8. `http://tracker.renfei.net:8080/announce` — score=93.0, 112ms, 存活率99%, 质量100, 经典+0
9. `udp://tracker.ducks.party:1984/announce` — score=92.6, 112ms, 存活率97%, 质量100, 经典+0
10. `udp://tracker.nyaa.vc:6969/announce` — score=92.3, 108ms, 存活率95%, 质量100, 经典+0
11. `https://t.213891.xyz:443/announce` — score=91.7, 133ms, 存活率99%, 质量100, 经典+0
12. `udp://109.201.134.183:80/announce` — score=91.6, 111ms, 存活率93%, 质量100, 经典+0
13. `udp://151.242.104.187:80/announce` — score=91.6, 112ms, 存活率93%, 质量100, 经典+0
14. `udp://tracker.skynetcloud.site:6969/announce` — score=90.9, 109ms, 存活率90%, 质量100, 经典+0
15. `udp://31.56.179.159:6969/announce` — score=89.9, 139ms, 存活率93%, 质量100, 经典+0
16. `http://207.241.226.111:6969/announce` — score=89.9, 81ms, 存活率79%, 质量100, 经典+0
17. `udp://tracker.dler.org:6969/announce` — score=89.4, 167ms, 存活率98%, 质量100, 经典+0
18. `http://207.241.231.226:6969/announce` — score=89.1, 95ms, 存活率79%, 质量100, 经典+0
19. `udp://t.overflow.biz:6969/announce` — score=88.6, 145ms, 存活率89%, 质量100, 经典+0
20. `udp://185.121.168.96:1337/announce` — score=88.4, 165ms, 存活率93%, 质量100, 经典+0

## 失效 Tracker

- `http://echostar.ddnsfree.com:8080/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://retracker.hotplug.ru:2710/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `https://pybittrack.retiolus.net:443/announce` — URLError: <urlopen error timed out>
- `udp://tracker.srv00.com:6969/announce` — no connect response
- `udp://tracker.tryhackx.org:6969/announce` — no connect response

## 不安全 Tracker（已过滤）

- `http://yggtracker.i2p.rocks:80/announce` — resolves to private IP: 200:1e2f:e608:eb3a:2bf:1e62:87ba:e2f7

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
- `http://sigmatracker.i2p:80/a` — I2P network required
- `http://tracker.insulaocculta.i2p:80/a` — I2P network required

## 同网段去重（/24，保留响应最快）

- `http://1337.abcvg.info:80/announce`
- `http://135.125.198.235:2710/announce`
- `http://135.125.198.235:80/announce`
- `http://152.249.214.196:6969/announce`
- `http://211.75.205.187:6969/announce`
- `http://211.75.205.187:80/announce`
- `http://211.75.205.188:80/announce`
- `http://211.75.210.221:6969/announce`
- `http://211.75.210.221:80/announce`
- `http://94.23.207.177:6969/announce`
- `http://announce.sktorrent.eu:6969/announce`
- `http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce`
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
- `https://1.tracker.eu.org:443/announce`
- `https://2.tracker.eu.org:443/announce`
- `https://3.tracker.eu.org:443/announce`
- `https://337hhh.xyz:443/announce`
- `udp://135.125.198.235:1984/announce`
- `udp://211.75.210.221:80/announce`
- `udp://23.157.120.14:6969/announce`
- `udp://34.66.57.33:1337/announce`
- `udp://34.66.57.33:80/announce`
- `udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce`
- `udp://exodus.desync.com:6969/announce`
- `udp://open.demonii.com:1337/announce`
- `udp://open.stealth.si:80/announce`
- `udp://tracker-udp.gbitt.info:80/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.gmi.gd:6969/announce`
- `udp://tracker.qu.ax:6969/announce`
