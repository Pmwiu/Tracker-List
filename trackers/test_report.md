# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-10 02:23:16 UTC
- 总 Tracker 数: 200
- 存活 (alive): **136** (68%)
- 失效 (dead): **40**
- 不安全 (unsafe): **3**
- 无法测试 (untestable): 21
- 低速淘汰 (low-speed >5s): 0
- 同网段去重 (/24, kept faster): 68
- 综合评分后保留前 25 个，淘汰 43 个
- 评分维度: 速度 60% + 历史稳定性 25% + 响应质量 15%（速度标度自适应 + 经典高可用加分）
- 配额: 保底 4 条非 UDP + 保底 4 条经典高可用
- 协议多样性配额: 保底 4 条非 UDP，实际保留 12 条
- 耗时: 21.6 秒

## 协议分布

- udp: 69
- http: 50
- https: 13
- wss: 4

## 最终订阅列表（前 25 个，按综合评分降序）

1. `https://t.213891.xyz:443/announce` — score=98.6, 21ms, 存活率100%, 质量100, 经典+0
2. `http://tracker.renfei.net:8080/announce` — score=98.6, 21ms, 存活率100%, 质量100, 经典+0
3. `https://1.tracker.eu.org:443/announce` — score=97.9, 33ms, 存活率100%, 质量100, 经典+0
4. `wss://tracker.openwebtorrent.com:443/announce` — score=97.9, 9ms, 存活率100%, 质量90, 经典+0
5. `udp://tracker.bittor.pw:1337/announce` — score=97.5, 26ms, 存活率96%, 质量100, 经典+0
6. `udp://tracker.torrent.eu.org:451/announce` — score=97.2, 116ms, 存活率92%, 质量100, 经典+6
7. `udp://tracker.004430.xyz:1337/announce` — score=96.2, 62ms, 存活率100%, 质量100, 经典+0
8. `udp://tracker.gmi.gd:6969/announce` — score=96.0, 62ms, 存活率99%, 质量100, 经典+0
9. `udp://exodus.desync.com:6969/announce` — score=95.9, 77ms, 存活率78%, 质量100, 经典+6
10. `udp://explodie.org:6969/announce` — score=95.6, 75ms, 存活率77%, 质量100, 经典+6
11. `http://140.235.237.23:6969/announce` — score=95.0, 47ms, 存活率91%, 质量100, 经典+0
12. `udp://tracker.nyaa.vc:6969/announce` — score=94.4, 84ms, 存活率98%, 质量100, 经典+0
13. `udp://tracker.ducks.party:1984/announce` — score=94.4, 88ms, 存活率99%, 质量100, 经典+0
14. `udp://109.201.134.183:80/announce` — score=94.3, 83ms, 存活率97%, 质量100, 经典+0
15. `udp://151.242.104.187:80/announce` — score=93.8, 92ms, 存活率97%, 质量100, 经典+0
16. `udp://31.56.179.159:6969/announce` — score=93.0, 106ms, 存活率97%, 质量100, 经典+0
17. `https://2.tracker.eu.org:443/announce` — score=92.8, 32ms, 存活率79%, 质量100, 经典+0
18. `udp://t.overflow.biz:6969/announce` — score=92.0, 115ms, 存活率96%, 质量100, 经典+0
19. `https://tracker.7471.top:443/announce` — score=91.6, 122ms, 存活率96%, 质量100, 经典+0
20. `udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce` — score=90.6, 99ms, 存活率86%, 质量100, 经典+0
21. `http://tracker.waaa.moe:6969/announce` — score=90.3, 144ms, 存活率96%, 质量100, 经典+0
22. `https://tracker.foreverpirates.co:443/announce` — score=90.1, 147ms, 存活率96%, 质量100, 经典+0
23. `http://207.241.226.111:6969/announce` — score=90.0, 131ms, 存活率91%, 质量100, 经典+0
24. `https://tracker.nekomi.cn:443/announce` — score=89.8, 151ms, 存活率96%, 质量100, 经典+0
25. `http://207.241.231.226:6969/announce` — score=89.8, 134ms, 存活率91%, 质量100, 经典+0

## 失效 Tracker

- `http://79.111.12.213:6969/announce` — timeout
- `http://bittorrent.kali.org:80/announce` — restricted (failure reason)
- `http://echostar.ddnsfree.com:8080/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://ehtracker.org:80/1104308/announce` — restricted (failure reason)
- `http://ehtracker.org:80/1113709/announce` — restricted (failure reason)
- `http://ehtracker.org:80/1226599/1080494xo5eXcwFOBq/announce` — restricted (failure reason)
- `http://ehtracker.org:80/2496841/announce` — restricted (failure reason)
- `http://ehtracker.org:80/2541477/announce` — restricted (failure reason)
- `http://ehtracker.org:80/2566145/1159106xUfsJkT9Btg/announce` — restricted (failure reason)
- `http://retracker.hotplug.ru:2710/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://retracker.x2k.ru:80/announce` — restricted (failure reason)
- `http://tracker-udp.anirena.com:80/announce` — restricted (failure reason)
- `http://tracker.openzim.org:80/announce` — restricted (failure reason)
- `http://tracker.trancetraffic.com:80/announce` — restricted (failure reason)
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [Errno 104] Connection reset by peer>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate (_ssl.c:1010)>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.bt4g.com:443/announce` — timeout
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tracker.zhuqiy.com:443/announce` — timeout
- `udp://52.58.128.163:6969/announce` — no connect response
- `udp://6ahddutb1ucc3cp.ru:6969/announce` — no connect response
- `udp://open.demonii.com:1337/announce` — no connect response
- `udp://open.tracker.ink:6969/announce` — no connect response
- `udp://opentor.org:2710/announce` — no connect response
- `udp://p4p.arenabg.com:1337/announce` — no connect response
- `udp://retracker.hotplug.ru:2710/announce` — no connect response
- `udp://torrentclub.online:54123/announce` — no connect response
- `udp://torrents.tmtime.dev:6969/announce` — no connect response
- `udp://tracker.alaskantf.com:6969/announce` — no connect response
- `udp://tracker.skyts.net:6969/announce` — no connect response
- `udp://tracker.srv00.com:6969/announce` — no connect response
- `udp://tracker.tryhackx.org:6969/announce` — no connect response
- `udp://tracker.wepzone.net:6969/announce` — no connect response
- `udp://tracker1.itzmx.com:8080/announce` — no connect response
- `udp://tracker1.myporn.club:9337/announce` — no connect response
- `udp://wegkxfcivgx.ydns.eu:80/announce` — no connect response
- `udp://wepzone.net:6969/announce` — no connect response

## 不安全 Tracker（已过滤）

- `http://yggtracker.i2p.rocks:80/announce` — resolves to private IP: 200:1e2f:e608:eb3a:2bf:1e62:87ba:e2f7
- `udp://open.dstud.io:6969/announce` — resolves to private IP: 0.0.0.0
- `wss://tracker.btorrent.xyz:443/announce` — resolves to private IP: 127.0.0.1

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
- `http://tracker.nyaa2p.i2p:80/announce` — I2P network required
- `http://yet-another-public-tracker.i2p:80/announce` — I2P network required
- `udp://[2a03:7220:8083:cd00::1]:451/announce` — IPv6 unavailable here
- `udp://[2a04:ac00:1:3dd8::1:2710]:2710/announce` — IPv6 unavailable here
- `udp://freetracker.i2p:1337/announce` — I2P network required
- `udp://opentracker.simp.i2p:6969/a` — I2P network required
- `udp://opentracker.skank.i2p:6969/a` — I2P network required

## 同网段去重（/24，保留响应最快）

- `http://107.189.2.131:1337/announce`
- `http://1337.abcvg.info:80/announce`
- `http://135.125.198.235:2710/announce`
- `http://135.125.198.235:80/announce`
- `http://211.75.205.187:6969/announce`
- `http://211.75.205.187:80/announce`
- `http://211.75.205.188:6969/announce`
- `http://211.75.205.188:80/announce`
- `http://211.75.210.221:6969/announce`
- `http://211.75.210.221:80/announce`
- `http://216.144.239.90:6969/announce`
- `http://31.38.161.123:6969/announce`
- `http://43.250.54.126:6969/announce`
- `http://93.158.213.92:1337/announce`
- `http://94.23.207.177:6969/announce`
- `http://announce.sktorrent.eu:6969/announce`
- `http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce`
- `http://ipv4announce.sktorrent.eu:6969/announce`
- `http://open.demonii.si:80/announce`
- `http://open.tracker.cl:1337/announce`
- `http://opentracker.xyz:80/announce`
- `http://retracker01-msk-virt.corbina.net:80/announce`
- `http://t-backup.213891.xyz:80/announce`
- `http://t.nyaatracker.com:80/announce`
- `http://t.overflow.biz:6969/announce`
- `http://tracker.004430.xyz:1337/announce`
- `http://tracker.auctor.tv:6969/announce`
- `http://tracker.coppersurfer.site:2710/announce`
- `http://tracker.dhitechnical.com:6969/announce`
- `http://tracker.dler.com:6969/announce`
- `http://tracker.dler.org:6969/announce`
- `http://tracker.mywaifu.best:6969/announce`
- `http://tracker.novaopcj.eu.org:6969/announce`
- `http://tracker.nyaa.vc:6969/announce`
- `http://tracker.opentrackr.org:1337/announce`
- `http://tracker.qu.ax:6969/announce`
- `http://tracker.torrents.observer:80/announce`
- `http://tracker.zhuqiy.dgj055.icu:80/announce`
- `http://tracker2.dler.org:80/announce`
- `https://004430.xyz:443/announce`
- `https://3.tracker.eu.org:443/announce`
- `https://337hhh.xyz:443/announce`
- `https://4.tracker.eu.org:443/announce`
- `https://tr.nyacat.pw:443/announce`
- `udp://135.125.198.235:1984/announce`
- `udp://209.141.59.25:6969/announce`
- `udp://211.75.210.221:80/announce`
- `udp://34.66.57.33:1337/announce`
- `udp://34.66.57.33:80/announce`
- `udp://45.137.199.107:6969/announce`
- `udp://65.109.28.33:6969/announce`
- `udp://91.216.110.53:451/announce`
- `udp://93.158.213.92:6969/announce`
- `udp://95.217.80.22:6969/announce`
- `udp://mail.segso.net:6969/announce`
- `udp://open.stealth.si:80/announce`
- `udp://retracker01-msk-virt.corbina.net:80/announce`
- `udp://tracker-udp.gbitt.info:80/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.dler.org:6969/announce`
- `udp://tracker.farted.net:6969/announce`
- `udp://tracker.ilibr.org:6969/announce`
- `udp://tracker.opentrackr.com:6969/announce`
- `udp://tracker.opentrackr.org:1337/announce`
- `udp://tracker.peerfect.org:6969/announce`
- `udp://tracker.qu.ax:6969/announce`
- `udp://tracker.skynetcloud.site:6969/announce`
- `udp://tracker.theoks.net:6969/announce`
