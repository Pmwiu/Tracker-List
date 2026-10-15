# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-15 21:35:22 UTC
- 总 Tracker 数: 320
- 存活 (alive): **116** (36%)
- 失效 (dead): **185**
- 不安全 (unsafe): **2**
- 无法测试 (untestable): 17
- 低速淘汰 (low-speed >5s): 0
- 同网段/同域名去重 (kept fastest): 59
- 综合评分后保留前 25 个，淘汰 32 个
- 评分维度: 速度 50% + 历史稳定性 20% + 响应质量 15%（含 peers 计数与 scrape 热度） + 跨源一致性 10% + 近期成功率 5%（速度标度自适应 + 经典高可用加分 + 反退化）
- 配额: 保底 4 条非 UDP + 保底 4 条经典高可用
- 协议多样性配额: 保底 4 条非 UDP，实际保留 9 条
- 耗时: 76.6 秒

## 协议分布

- udp: 62
- http: 42
- https: 12

## 最终订阅列表（前 25 个，按综合评分降序）

1. `udp://explodie.org:6969/announce` — score=98.0, 32ms, 存活率98%, 质量60, 经典+6
2. `https://t.213891.xyz:443/announce` — score=96.9, 33ms, 存活率100%, 质量90, 经典+0
3. `https://tracker.nekomi.cn:443/announce` — score=94.3, 99ms, 存活率100%, 质量95, 经典+0
4. `http://207.241.226.111:6969/announce` — score=94.2, 49ms, 存活率100%, 质量98, 经典+0
5. `http://207.241.231.226:6969/announce` — score=93.7, 52ms, 存活率100%, 质量95, 经典+0
6. `udp://tracker.opentrackr.org:1337/announce` — score=92.9, 142ms, 存活率100%, 质量60, 经典+6
7. `udp://open.ftorrent.com:443/announce` — score=92.6, 27ms, 存活率100%, 质量60, 经典+0
8. `udp://tracker.bittor.pw:1337/announce` — score=91.6, 48ms, 存活率100%, 质量60, 经典+0
9. `https://tracker.zhuqiy.com:443/announce` — score=91.2, 119ms, 存活率89%, 质量95, 经典+0
10. `http://tracker.renfei.net:8080/announce` — score=90.6, 173ms, 存活率100%, 质量95, 经典+0
11. `udp://evan.im:6969/announce` — score=90.6, 67ms, 存活率100%, 质量60, 经典+0
12. `udp://tracker.torrent.eu.org:451/announce` — score=90.5, 164ms, 存活率96%, 质量60, 经典+6
13. `https://tracker.7471.top:443/announce` — score=88.9, 192ms, 存活率100%, 质量90, 经典+0
14. `udp://tracker.dler.org:6969/announce` — score=87.5, 131ms, 存活率100%, 质量60, 经典+0
15. `udp://tracker2.dler.org:80/announce` — score=87.5, 131ms, 存活率100%, 质量60, 经典+0
16. `https://2.tracker.eu.org:443/announce` — score=87.0, 30ms, 存活率100%, 质量90, 经典+0
17. `udp://tracker.qu.ax:6969/announce` — score=86.8, 143ms, 存活率100%, 质量60, 经典+0
18. `udp://martin-gebhardt.eu:25/announce` — score=86.6, 147ms, 存活率100%, 质量60, 经典+0
19. `https://3.tracker.eu.org:443/announce` — score=86.6, 38ms, 存活率100%, 质量90, 经典+0
20. `udp://kolankoalastree.newtrackon.co.nz:1337/announce` — score=86.5, 147ms, 存活率99%, 质量60, 经典+0
21. `udp://tracker.004430.xyz:1337/announce` — score=85.5, 29ms, 存活率100%, 质量60, 经典+0
22. `udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce` — score=85.3, 166ms, 存活率98%, 质量60, 经典+0
23. `udp://t.overflow.biz:6969/announce` — score=85.1, 175ms, 存活率99%, 质量60, 经典+0
24. `udp://retracker01-msk-virt.corbina.net:80/announce` — score=84.8, 185ms, 存活率100%, 质量60, 经典+0
25. `udp://exodus.desync.com:6969/announce` — score=81.7, 30ms, 存活率34%, 质量60, 经典+6

## 失效 Tracker

- `http://00.mercax.com:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://00.xxtor.com:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://0205.uptm.ch:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://104.143.10.186:8000/announce` — URLError: <urlopen error timed out>
- `http://104.244.77.14:1337/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://104.28.1.30:8080/announce` — URLError: <urlopen error timed out>
- `http://104.28.16.69:80/announce` — URLError: <urlopen error timed out>
- `http://106.14.254.164:6969/announce` — URLError: <urlopen error timed out>
- `http://107.150.14.110:6969/announce` — URLError: <urlopen error timed out>
- `http://107.152.127.9:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://107.189.10.20.sslip.io:7777/announce` — URLError: <urlopen error timed out>
- `http://107.189.31.134:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://107.189.7.143:6969/announce` — URLError: <urlopen error timed out>
- `http://109.121.134.121:1337/announce` — URLError: <urlopen error timed out>
- `http://114.55.113.60:6969/announce` — URLError: <urlopen error timed out>
- `http://116.252.176.125:6969/announce` — URLError: <urlopen error timed out>
- `http://116.9.207.121:6969/announce` — URLError: <urlopen error timed out>
- `http://116.9.207.164:6969/announce` — URLError: <urlopen error timed out>
- `http://116.9.207.198:6969/announce` — URLError: <urlopen error timed out>
- `http://116.9.207.226:6969/announce` — URLError: <urlopen error timed out>
- `http://119.28.71.45:8080/announce` — URLError: <urlopen error timed out>
- `http://125.227.35.196:6969/announce` — URLError: <urlopen error timed out>
- `http://128.199.70.66:5944/announce` — URLError: <urlopen error timed out>
- `http://129.146.193.240:6699/announce` — URLError: <urlopen error timed out>
- `http://13.115.115.32:6969/announce` — URLError: <urlopen error timed out>
- `http://140.82.21.192:8080/announce` — URLError: <urlopen error timed out>
- `http://141.144.224.250:2710/announce` — URLError: <urlopen error timed out>
- `http://141.144.224.250:6969/announce` — URLError: <urlopen error timed out>
- `http://144.202.33.210:6961/announce` — URLError: <urlopen error timed out>
- `http://144.76.118.107:6969/announce` — URLError: <urlopen error timed out>
- `http://147job.com:6969/announce` — URLError: <urlopen error timed out>
- `http://151.115.49.115:1337/announce` — URLError: <urlopen error timed out>
- `http://155.248.200.105:80/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://156.234.201.18:80/announce` — URLError: <urlopen error timed out>
- `http://185.148.3.231:80/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://34.66.57.33:2701/announce` — timeout
- `http://34.66.57.33:443/announce` — URLError: <urlopen error timed out>
- `http://34.89.30.59:2710/announce` — URLError: <urlopen error timed out>
- `http://34.89.30.59:80/announce` — URLError: <urlopen error timed out>
- `http://34.94.213.23:11451/announce` — URLError: <urlopen error timed out>
- `http://34.94.213.23:2710/announce` — URLError: <urlopen error timed out>
- `http://34.94.213.23:80/announce` — URLError: <urlopen error timed out>
- `http://35.227.12.84:2710/announce` — URLError: <urlopen error timed out>
- `http://35.227.12.84:80/announce` — URLError: <urlopen error timed out>
- `http://37.120.182.83:2710/announce` — URLError: <urlopen error timed out>
- `http://37.120.182.83:80/announce` — URLError: <urlopen error timed out>
- `http://37.19.5.139:6969/announce` — URLError: <urlopen error timed out>
- `http://37.19.5.155:6881/announce` — URLError: <urlopen error timed out>
- `http://37.235.174.46:2710/announce` — URLError: <urlopen error timed out>
- `http://38.145.197.79:6961/announce` — URLError: <urlopen error timed out>
- `http://43.139.20.56:6969/announce` — URLError: <urlopen error timed out>
- `http://45.154.253.10:80/announce` — URLError: <urlopen error timed out>
- `http://45.154.253.4:80/announce` — URLError: <urlopen error timed out>
- `http://45.154.253.5:80/announce` — URLError: <urlopen error timed out>
- `http://45.154.253.6:80/announce` — URLError: <urlopen error timed out>
- `http://45.154.253.7:80/announce` — URLError: <urlopen error timed out>
- `http://45.154.253.8:80/announce` — URLError: <urlopen error timed out>
- `http://45.154.253.9:80/announce` — URLError: <urlopen error timed out>
- `http://45.154.98.215:6969/announce` — URLError: <urlopen error timed out>
- `http://45.63.111.135:2710/announce` — URLError: <urlopen error timed out>
- `http://45.63.111.135:6961/announce` — URLError: <urlopen error timed out>
- `http://45.63.111.135:8080/announce` — URLError: <urlopen error timed out>
- `http://45.67.35.111:6969/announce` — URLError: <urlopen error timed out>
- `http://46.17.46.112:8080/announce` — URLError: <urlopen error timed out>
- `http://46.231.241.43:6969/announce` — URLError: <urlopen error timed out>
- `http://46.4.109.148:6969/announce` — URLError: <urlopen error timed out>
- `http://47.243.23.189:6969/announce` — URLError: <urlopen error timed out>
- `http://47.54.245.23:6969/announce` — URLError: <urlopen error timed out>
- `http://49.12.76.8:6961/announce` — URLError: <urlopen error timed out>
- `http://49.12.76.8:8080/announce` — URLError: <urlopen error timed out>
- `http://5.182.206.171:1096/announce` — URLError: <urlopen error timed out>
- `http://5.188.6.45:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://5.78.67.213:6699/announce` — URLError: <urlopen error timed out>
- `http://5.79.249.77:6969/announce` — URLError: <urlopen error timed out>
- `http://5.79.83.193:2710/announce` — URLError: <urlopen error timed out>
- `http://51.254.244.161:6969/announce` — URLError: <urlopen error timed out>
- `http://51.38.230.101:80/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://51.68.122.172:80/announce` — HTTPError: HTTP Error 404: Not Found
- `http://51.81.200.170:6699/announce` — URLError: <urlopen error timed out>
- `http://51.81.46.170:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://52.70.94.249:80/announce` — URLError: <urlopen error timed out>
- `http://54.39.98.124:80/announce` — URLError: <urlopen error timed out>
- `http://59.36.96.77:6969/announce` — URLError: <urlopen error timed out>
- `http://61.216.109.95:6969/announce` — URLError: <urlopen error timed out>
- `http://61.216.149.33:6969/announce` — URLError: <urlopen error timed out>
- `http://61.216.166.123:6969/announce` — URLError: <urlopen error timed out>
- `http://61.222.178.227:6969/announce` — URLError: <urlopen error timed out>
- `http://61.222.178.254:6969/announce` — URLError: <urlopen error timed out>
- `http://62.182.85.138:666/announce` — URLError: <urlopen error timed out>
- `http://65.108.2.176:2710/announce` — URLError: <urlopen error timed out>
- `http://65.130.205.148:9000/announce` — URLError: <urlopen error timed out>
- `http://74.82.52.209:6969/announce` — URLError: <urlopen error timed out>
- `http://75.127.14.224:2710/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://79.137.198.96:6969/announce` — URLError: <urlopen error timed out>
- `http://80.246.243.18:6969/announce` — URLError: <urlopen error timed out>
- `http://81.200.2.231:80/announce` — URLError: <urlopen error timed out>
- `http://83.31.190.19:6969/announce` — URLError: <urlopen error timed out>
- `http://83.31.191.97:6969/announce` — URLError: <urlopen error timed out>
- `http://83.31.199.157:6969/announce` — URLError: <urlopen error timed out>
- `http://83.31.209.3:6969/announce` — URLError: <urlopen error timed out>
- `http://83.31.211.243:6969/announce` — URLError: <urlopen error timed out>
- `http://83.31.212.134:6969/announce` — URLError: <urlopen error timed out>
- `http://83.31.216.220:6969/announce` — URLError: <urlopen error timed out>
- `http://83.31.219.73:6969/announce` — URLError: <urlopen error timed out>
- `http://83.31.33.73:6969/announce` — URLError: <urlopen error timed out>
- `http://83.6.208.20:6969/announce` — URLError: <urlopen error timed out>
- `http://83.6.209.31:6969/announce` — URLError: <urlopen error timed out>
- `http://83.6.211.179:6969/announce` — URLError: <urlopen error timed out>
- `http://83.6.220.156:6969/announce` — URLError: <urlopen error timed out>
- `http://83.6.223.8:6969/announce` — URLError: <urlopen error timed out>
- `http://83.6.226.63:6969/announce` — URLError: <urlopen error timed out>
- `http://83.6.227.65:6969/announce` — URLError: <urlopen error timed out>
- `http://83.6.231.40:6969/announce` — URLError: <urlopen error timed out>
- `http://83.6.232.23:6969/announce` — URLError: <urlopen error timed out>
- `http://83.6.234.75:6969/announce` — URLError: <urlopen error timed out>
- `http://83.6.237.118:6969/announce` — URLError: <urlopen error timed out>
- `http://85.17.19.180:80/announce` — URLError: <urlopen error timed out>
- `http://87.248.186.252:8080/announce` — URLError: <urlopen error timed out>
- `http://87.253.152.137:80/announce` — URLError: <urlopen error timed out>
- `http://88.99.189.199:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://91.216.110.47:80/announce` — URLError: <urlopen error timed out>
- `http://91.217.91.21:3218/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://91.218.230.81:6969/announce` — URLError: <urlopen error timed out>
- `http://91.224.92.110:6969/announce` — URLError: <urlopen error timed out>
- `http://93.88.129.16:80/announce` — timeout
- `http://93.92.64.5:80/announce` — URLError: <urlopen error timed out>
- `http://95.107.48.115:80/announce` — URLError: <urlopen error timed out>
- `http://95.217.161.135:80/announce` — URLError: <urlopen error timed out>
- `http://95.217.167.10:6969/announce` — URLError: <urlopen error timed out>
- `http://97.117.101.163:9000/announce` — URLError: <urlopen error timed out>
- `http://97.117.102.248:9000/announce` — URLError: <urlopen error timed out>
- `http://97.117.105.168:9000/announce` — URLError: <urlopen error timed out>
- `http://97.117.114.88:9000/announce` — URLError: <urlopen error timed out>
- `http://97.117.128.139:9000/announce` — URLError: <urlopen error timed out>
- `http://97.117.145.39:9000/announce` — URLError: <urlopen error timed out>
- `http://97.117.150.188:9000/announce` — URLError: <urlopen error timed out>
- `http://97.117.75.139:9000/announce` — URLError: <urlopen error timed out>
- `http://97.117.78.100:9000/announce` — URLError: <urlopen error timed out>
- `http://97.117.85.73:9000/announce` — URLError: <urlopen error timed out>
- `http://99.192.12.191:6969/announce` — URLError: <urlopen error timed out>
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
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://104.28.17.69:443/announce` — URLError: <urlopen error timed out>
- `https://ht.therarbg.to:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [Errno 104] Connection reset by peer>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.bt4g.com:443/announce` — timeout
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `udp://103.122.21.50:6969/announce` — no connect response
- `udp://104.131.98.232:6969/announce` — no connect response
- `udp://104.143.10.186:8000/announce` — no connect response
- `udp://107.150.14.110:6969/announce` — no connect response
- `udp://107.175.221.194:6969/announce` — no connect response
- `udp://107.189.7.165:6969/announce` — no connect response
- `udp://109.121.134.121:1337/announce` — no connect response
- `udp://114.55.113.60:6969/announce` — no connect response
- `udp://119.28.71.45:8080/announce` — no connect response
- `udp://128.199.70.66:5944/announce` — no connect response
- `udp://132.243.161.144:6969/announce` — no connect response
- `udp://6ahddutb1ucc3cp.ru:6969/announce` — no connect response
- `udp://open.tracker.ink:6969/announce` — no connect response
- `udp://opentor.org:2710/announce` — no connect response
- `udp://p4p.arenabg.com:1337/announce` — no connect response
- `udp://retracker.hotplug.ru:2710/announce` — no connect response
- `udp://torrentclub.online:54123/announce` — no connect response
- `udp://torrents.tmtime.dev:6969/announce` — no connect response
- `udp://tracker.alaskantf.com:6969/announce` — no connect response
- `udp://tracker.srv00.com:6969/announce` — no connect response
- `udp://tracker.theoks.net:6969/announce` — no connect response
- `udp://tracker.wepzone.net:6969/announce` — no connect response
- `udp://tracker1.itzmx.com:8080/announce` — no connect response
- `udp://tracker1.myporn.club:9337/announce` — no connect response
- `udp://wepzone.net:6969/announce` — no connect response
- `wss://tracker.openwebtorrent.com:443/announce` — SSLError: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1010)

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
- `udp://opentracker.skank.i2p:6969/a` — I2P network required

## 同网段/同域名去重（保留响应最快）

- `http://107.189.2.131:1337/announce`
- `http://135.125.198.235:2710/announce`
- `http://135.125.198.235:80/announce`
- `http://138.186.10.167:1337/announce`
- `http://189.18.97.208:6969/announce`
- `http://211.75.205.187:6969/announce`
- `http://211.75.205.187:80/announce`
- `http://211.75.205.188:6969/announce`
- `http://211.75.205.188:80/announce`
- `http://211.75.210.221:6969/announce`
- `http://211.75.210.221:80/announce`
- `http://31.38.161.123:6969/announce`
- `http://34.66.57.33:6969/announce`
- `http://34.66.57.33:80/announce.php`
- `http://43.250.54.126:6969/announce`
- `http://93.158.213.92:1337/announce`
- `http://94.23.207.177:6969/announce`
- `http://announce.sktorrent.eu:6969/announce`
- `http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce`
- `http://ipv4announce.sktorrent.eu:6969/announce`
- `http://opentracker.xyz:80/announce`
- `http://retracker01-msk-virt.corbina.net:80/announce`
- `http://tracker.auctor.tv:6969/announce`
- `http://tracker.dhitechnical.com:6969/announce`
- `http://tracker.dler.com:6969/announce`
- `http://tracker.dler.org:6969/announce`
- `http://tracker.mywaifu.best:6969/announce`
- `http://tracker.nyaa.vc:6969/announce`
- `http://tracker.opentrackr.org:1337/announce`
- `http://tracker.qu.ax:6969/announce`
- `http://tracker.waaa.moe:6969/announce`
- `http://tracker2.dler.org:80/announce`
- `https://004430.xyz:443/announce`
- `https://1.tracker.eu.org:443/announce`
- `https://337hhh.xyz:443/announce`
- `udp://189.18.97.208:6969/announce`
- `udp://211.75.205.188:6969/announce`
- `udp://211.75.205.188:80/announce`
- `udp://23.157.120.14:6969/announce`
- `udp://31.56.179.159:6969/announce`
- `udp://34.66.57.33:1337/announce`
- `udp://34.66.57.33:80/announce`
- `udp://43.250.54.126:6969/announce`
- `udp://52.58.128.163:6969/announce`
- `udp://65.109.28.17:6969/announce`
- `udp://83.102.180.21:80/announce`
- `udp://93.158.213.92:1337/announce`
- `udp://93.158.213.92:6969/announce`
- `udp://95.217.80.22:6969/announce`
- `udp://mail.segso.net:6969/announce`
- `udp://open.demonii.com:1337/announce`
- `udp://open.stealth.si:80/announce`
- `udp://tracker-udp.gbitt.info:80/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.ducks.party:1984/announce`
- `udp://tracker.nyaa.vc:6969/announce`
- `udp://tracker.opentrackr.com:6969/announce`
- `udp://tracker.peerfect.org:6969/announce`
- `udp://tracker.skynetcloud.site:6969/announce`

## Discovery（自动发现的候选，Phase 1 隔离，不进 best/all）

- 候选总数: 155
- 通过探活: 3
- 若允许参与排名会入选的（前 1 条）:
  - `udp://118.196.100.63:6969/announce`

转正方式：人工 review 后加入 `scripts/update_trackers.py` 的 SOURCES，或写进 `trackers/discovered/PROMOTE.md`（Phase 2）。


## 备选库（trackers_reserve.txt，前 3 条，按评分降序）

独立于 best/all 的候选订阅源，供人工审查转正。
1. `http://34.66.57.33:6969/announce`
2. `udp://118.196.100.63:6969/announce`
3. `http://34.66.57.33:80/announce.php`

