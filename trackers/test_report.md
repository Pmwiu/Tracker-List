# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-16 04:46:48 UTC
- 总 Tracker 数: 320
- 存活 (alive): **115** (35%)
- 失效 (dead): **186**
- 不安全 (unsafe): **2**
- 无法测试 (untestable): 17
- 低速淘汰 (low-speed >5s): 0
- 同网段/同域名去重 (kept fastest): 59
- 综合评分后保留前 25 个，淘汰 31 个
- 评分维度: 速度 50% + 历史稳定性 20% + 响应质量 15%（含 peers 计数与 scrape 热度） + 跨源一致性 10% + 近期成功率 5%（速度标度自适应 + 经典高可用加分 + 反退化）
- 配额: 保底 4 条非 UDP + 保底 4 条经典高可用
- 协议多样性配额: 保底 4 条非 UDP，实际保留 9 条
- 耗时: 59.6 秒

## 协议分布

- udp: 60
- http: 41
- https: 14

## 最终订阅列表（前 25 个，按综合评分降序）

1. `https://tracker.nekomi.cn:443/announce` — score=96.8, 49ms, 存活率100%, 质量95, 经典+0
2. `https://t.213891.xyz:443/announce` — score=96.4, 41ms, 存活率100%, 质量90, 经典+0
3. `http://207.241.226.111:6969/announce` — score=95.0, 34ms, 存活率100%, 质量98, 经典+0
4. `http://207.241.231.226:6969/announce` — score=94.2, 40ms, 存活率100%, 质量95, 经典+0
5. `udp://open.demonii.com:1337/announce` — score=93.6, 127ms, 存活率100%, 质量60, 经典+6
6. `udp://open.stealth.si:80/announce` — score=92.9, 142ms, 存活率100%, 质量60, 经典+6
7. `udp://open.ftorrent.com:443/announce` — score=92.2, 36ms, 存活率100%, 质量60, 经典+0
8. `udp://tracker.torrent.eu.org:451/announce` — score=91.7, 141ms, 存活率97%, 质量60, 经典+6
9. `udp://evan.im:6969/announce` — score=91.5, 50ms, 存活率100%, 质量60, 经典+0
10. `https://tracker.zhuqiy.com:443/announce` — score=91.1, 128ms, 存活率92%, 质量95, 经典+0
11. `http://tracker.renfei.net:8080/announce` — score=90.1, 182ms, 存活率100%, 质量95, 经典+0
12. `https://tracker.7471.top:443/announce` — score=88.8, 194ms, 存活率100%, 质量90, 经典+0
13. `http://004430.xyz:80/announce` — score=88.0, 25ms, 存活率100%, 质量95, 经典+0
14. `udp://tracker.skynetcloud.site:6969/announce` — score=87.5, 129ms, 存活率100%, 质量60, 经典+0
15. `udp://tracker-udp.gbitt.info:80/announce` — score=87.5, 130ms, 存活率100%, 质量60, 经典+0
16. `udp://martin-gebhardt.eu:25/announce` — score=87.2, 136ms, 存活率100%, 质量60, 经典+0
17. `udp://tracker2.dler.org:80/announce` — score=87.0, 140ms, 存活率100%, 质量60, 经典+0
18. `udp://kolankoalastree.newtrackon.co.nz:1337/announce` — score=86.6, 146ms, 存活率99%, 质量60, 经典+0
19. `udp://tracker.004430.xyz:1337/announce` — score=86.6, 9ms, 存活率100%, 质量60, 经典+0
20. `udp://t.overflow.biz:6969/announce` — score=86.2, 153ms, 存活率99%, 质量60, 经典+0
21. `udp://tracker.peerfect.org:6969/announce` — score=86.0, 159ms, 存活率100%, 质量60, 经典+0
22. `https://3.tracker.eu.org:443/announce` — score=86.0, 50ms, 存活率100%, 质量90, 经典+0
23. `udp://opentracker.lain.moscow:6969/announce` — score=85.4, 145ms, 存活率96%, 质量60, 经典+0
24. `udp://retracker01-msk-virt.corbina.net:80/announce` — score=85.4, 173ms, 存活率100%, 质量60, 经典+0
25. `udp://34.66.57.33:80/announce` — score=84.4, 51ms, 存活率100%, 质量60, 经典+0

## 失效 Tracker

- `http://157.7.202.64:8080/announce` — URLError: <urlopen error timed out>
- `http://157.90.169.123:80/announce` — HTTPError: HTTP Error 404: Not Found
- `http://158.101.137.177:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://158.69.146.212:7777/announce` — URLError: <urlopen error timed out>
- `http://159.69.65.157:6969/announce` — URLError: <urlopen error timed out>
- `http://160.251.78.190:6969/announce` — URLError: <urlopen error timed out>
- `http://163.172.209.40:80/announce` — URLError: <urlopen error timed out>
- `http://163.172.29.130:80/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://167.235.245.209:80/announce` — HTTPError: HTTP Error 404: Not Found
- `http://167.253.78.20:8080/announce` — URLError: <urlopen error timed out>
- `http://171.104.110.193:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://171.104.110.21:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://171.104.110.88:6969/announce` — URLError: <urlopen error timed out>
- `http://171.104.110.95:6969/announce` — URLError: <urlopen error timed out>
- `http://171.104.111.14:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://171.104.111.201:6969/announce` — URLError: <urlopen error timed out>
- `http://171.104.111.20:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://171.104.111.250:6969/announce` — URLError: <urlopen error timed out>
- `http://171.104.111.30:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://171.104.111.83:6969/announce` — URLError: <urlopen error timed out>
- `http://171.104.111.89:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://171.104.226.15:6969/announce` — URLError: <urlopen error timed out>
- `http://171.104.226.221:6969/announce` — URLError: <urlopen error timed out>
- `http://171.104.226.25:6969/announce` — URLError: <urlopen error timed out>
- `http://171.104.226.31:6969/announce` — URLError: <urlopen error timed out>
- `http://171.104.226.87:6969/announce` — URLError: <urlopen error timed out>
- `http://173.254.204.71:1096/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://178.175.143.27:80/announce` — URLError: <urlopen error timed out>
- `http://178.33.73.26:2710/announce` — URLError: <urlopen error timed out>
- `http://179.100.24.134:6969/announce` — URLError: <urlopen error timed out>
- `http://180.139.151.58:6969/announce` — URLError: <urlopen error timed out>
- `http://180.97.219.76:8070/announce` — URLError: <urlopen error timed out>
- `http://182.176.139.129:6969/announce` — URLError: <urlopen error timed out>
- `http://185.130.47.2:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://34.66.57.33:11450/announce` — timeout
- `http://79.111.12.213:6969/announce` — restricted (failure reason)
- `http://bittorrent.kali.org:80/announce` — restricted (failure reason)
- `http://echostar.ddnsfree.com:8080/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://ehtracker.org:80/1104308/announce` — restricted (failure reason)
- `http://ehtracker.org:80/1113709/announce` — restricted (failure reason)
- `http://ehtracker.org:80/1226599/1080494xo5eXcwFOBq/announce` — restricted (failure reason)
- `http://ehtracker.org:80/2496841/announce` — restricted (failure reason)
- `http://ehtracker.org:80/2541477/announce` — restricted (failure reason)
- `http://retracker.hotplug.ru:2710/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://github.com:443/stefantalpalaru/deluge-default-trackers` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/transmission/transmission` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/wuyuansushen/aria2c_TrackersList` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/xXSalamanderXx/HDEncode-Search-Plus` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/xXSalamanderXx/RLSBB-Search-Plus` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/xXSalamanderXx/SlimBrave` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/xXSalamanderXx/caesium-image-compressor-linux` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/xXSalamanderXx/salamander-trackers/blob/main/LICENSE` — HTTPError: HTTP Error 400: Bad Request
- `https://ht.therarbg.to:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://i2pplus.github.io:443` — invalid bencoded response
- `https://img.shields.io:443/badge/Download-Release-blue.svg` — invalid bencoded response
- `https://img.shields.io:443/github/stars/ngosang/trackerslist` — invalid bencoded response
- `https://madeby.lynx.pink:443/magnets` — invalid bencoded response
- `https://mrgusux.github.io:443/automatic-trackers` — HTTPError: HTTP Error 404: Not Found
- `https://newtrackon.com:443` — HTTPError: HTTP Error 403: Forbidden
- `https://ngosang.github.io:443/trackerslist/trackers_all.txt` — invalid bencoded response
- `https://ngosang.github.io:443/trackerslist/trackers_all_http.txt` — invalid bencoded response
- `https://ngosang.github.io:443/trackerslist/trackers_all_https.txt` — invalid bencoded response
- `https://ngosang.github.io:443/trackerslist/trackers_all_i2p.txt` — invalid bencoded response
- `https://ngosang.github.io:443/trackerslist/trackers_all_ip.txt` — invalid bencoded response
- `https://ngosang.github.io:443/trackerslist/trackers_all_udp.txt` — invalid bencoded response
- `https://ngosang.github.io:443/trackerslist/trackers_all_ws.txt` — invalid bencoded response
- `https://ngosang.github.io:443/trackerslist/trackers_all_yggdrasil.txt` — invalid bencoded response
- `https://ngosang.github.io:443/trackerslist/trackers_all_yggdrasil_ip.txt` — invalid bencoded response
- `https://ngosang.github.io:443/trackerslist/trackers_best.txt` — invalid bencoded response
- `https://ngosang.github.io:443/trackerslist/trackers_best_ip.txt` — invalid bencoded response
- `https://pybittrack.retiolus.net:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'pybittrack.retiolus.net'. (_ssl.c:1010)>
- `https://raw.githubusercontent.com:443/B0zrx/RationTrack/main/docs/docs/docs/Ration-Track-2.6-beta.5.zip` — invalid bencoded response
- `https://raw.githubusercontent.com:443/gitovamb/trackers/main/logo/Software_v1.1.zip` — HTTPError: HTTP Error 404: Not Found
- `https://raw.githubusercontent.com:443/gitovamb/trackers/main/wbx_logo.png` — invalid bencoded response
- `https://raw.githubusercontent.com:443/mrgusux/automatic-trackers/main/SHA256SUMS.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/mrgusux/automatic-trackers/main/all_trackers.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/mrgusux/automatic-trackers/main/all_trackers_comma.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/mrgusux/automatic-trackers/main/api/badge.json` — invalid bencoded response
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [Errno 104] Connection reset by peer>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate (_ssl.c:1010)>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.bt4g.com:443/announce` — timeout
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `udp://135.125.106.92:6969/announce` — no connect response
- `udp://144.91.88.22:6969/announce` — no connect response
- `udp://148.251.53.72:6969/announce` — no connect response
- `udp://151.80.120.114:2710/announce` — no connect response
- `udp://152.53.194.103:54123/announce` — no connect response
- `udp://156.234.201.18:80/announce` — no connect response
- `udp://158.101.161.60:3131/announce` — no connect response
- `udp://161.97.67.210:6969/announce` — no connect response
- `udp://163.172.29.130:80/announce` — no connect response
- `udp://163.5.63.253:6990/announce` — no connect response
- `udp://167.99.185.219:6969/announce` — no connect response
- `udp://168.235.67.63:6969/announce` — no connect response
- `udp://172.105.235.127:6969/announce` — no connect response
- `udp://173.249.201.201:6969/announce` — no connect response
- `udp://176.31.250.174:6969/announce` — no connect response
- `udp://178.170.48.154:1337/announce` — no connect response
- `udp://178.33.73.26:2710/announce` — no connect response
- `udp://182.176.139.129:6969/announce` — no connect response
- `udp://185.102.219.163:6969/announce` — no connect response
- `udp://185.181.60.155:80/announce` — no connect response
- `udp://185.181.60.67:80/announce` — no connect response
- `udp://185.230.4.150:1337/announce` — no connect response
- `udp://185.243.218.213:80/announce` — no connect response
- `udp://185.44.82.25:1337/announce` — no connect response
- `udp://185.5.97.139:8089/announce` — no connect response
- `udp://185.86.149.205:1337/announce` — no connect response
- `udp://188.165.253.109:1337/announce` — no connect response
- `udp://191.101.229.236:1337/announce` — no connect response
- `udp://192.3.130.53:1337/announce` — no connect response
- `udp://192.95.46.115:6969/announce` — no connect response
- `udp://193.148.251.143:6969/announce` — no connect response
- `udp://193.37.214.12:6969/announce` — no connect response
- `udp://194.106.216.222:80/announce` — no connect response
- `udp://194.38.21.77:6969/announce` — no connect response
- `udp://195.123.209.37:1337/announce` — no connect response
- `udp://195.123.209.40:80/announce` — no connect response
- `udp://198.100.149.66:6969/announce` — no connect response
- `udp://2.57.214.218:6969/announce` — no connect response
- `udp://207.241.226.111:6969/announce` — no connect response
- `udp://207.241.231.226:6969/announce` — no connect response
- `udp://208.67.16.113:8000/announce` — no connect response
- `udp://209.126.11.233:6969/announce` — no connect response
- `udp://211.75.29.254:6969/announce` — no connect response
- `udp://213.163.67.56:1337/announce` — no connect response
- `udp://217.30.10.77:6969/announce` — no connect response
- `udp://23.137.251.45:6969/announce` — no connect response
- `udp://37.187.111.136:6969/announce` — no connect response
- `udp://37.187.95.112:6969/announce` — no connect response
- `udp://37.19.5.155:2710/announce` — no connect response
- `udp://37.59.48.81:6969/announce` — no connect response
- `udp://44.30.4.4:6969/announce` — no connect response
- `udp://45.9.60.30:6969/announce` — no connect response
- `udp://46.138.242.240:6969/announce` — no connect response
- `udp://46.4.109.148:6969/announce` — no connect response
- `udp://5.196.67.51:6969/announce` — no connect response
- `udp://5.196.89.204:6969/announce` — no connect response
- `udp://5.79.249.77:6969/announce` — no connect response
- `udp://5.79.83.193:6969/announce` — no connect response
- `udp://51.15.26.25:6969/announce` — no connect response
- `udp://51.15.3.74:6969/announce` — no connect response
- `udp://51.158.144.42:6969/announce` — no connect response
- `udp://51.159.54.68:6666/announce` — no connect response
- `udp://51.254.244.161:6969/announce` — no connect response
- `udp://51.68.174.87:6969/announce` — no connect response
- `udp://62.138.0.158:6969/announce` — no connect response
- `udp://62.212.85.66:2710/announce` — no connect response
- `udp://6ahddutb1ucc3cp.ru:6969/announce` — no connect response
- `udp://74.82.52.209:6969/announce` — no connect response
- `udp://81.230.84.201:6969/announce` — no connect response
- `udp://82.65.115.10:6969/announce` — no connect response
- `udp://85.17.19.180:80/announce` — no connect response
- `udp://87.106.210.134:6969/announce` — no connect response
- `udp://88.80.22.67:2710/announce` — no connect response
- `udp://88.80.28.7:6969/announce` — no connect response
- `udp://88.99.2.212:6969/announce` — no connect response
- `udp://89.117.57.95:1337/announce` — no connect response
- `udp://89.234.156.205:80/announce` — no connect response
- `udp://89.36.216.8:6969/announce` — no connect response
- `udp://91.218.230.81:6969/announce` — no connect response
- `udp://93.104.214.40:6969/announce` — no connect response
- `udp://94.103.87.87:6969/announce` — no connect response
- `udp://94.23.183.33:6969/announce` — no connect response
- `udp://94.243.222.100:6969/announce` — no connect response
- `udp://95.216.74.39:6969/announce` — no connect response
- `udp://95.31.11.224:6969/announce` — no connect response
- `udp://exodus.desync.com:6969/announce` — no connect response
- `udp://open.tracker.ink:6969/announce` — no connect response
- `udp://opentor.org:2710/announce` — no connect response
- `udp://p4p.arenabg.com:1337/announce` — no connect response
- `udp://retracker.hotplug.ru:2710/announce` — no connect response
- `udp://torrentclub.online:54123/announce` — no connect response
- `udp://torrents.tmtime.dev:6969/announce` — no connect response
- `udp://tracker.alaskantf.com:6969/announce` — no connect response
- `udp://tracker.srv00.com:6969/announce` — no connect response
- `udp://tracker.theoks.net:6969/announce` — no connect response
- `udp://tracker.tryhackx.org:6969/announce` — no connect response
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
- `http://140.235.237.23:6969/announce`
- `http://189.18.97.208:6969/announce`
- `http://211.75.205.187:6969/announce`
- `http://211.75.205.187:80/announce`
- `http://211.75.205.188:6969/announce`
- `http://211.75.205.188:80/announce`
- `http://211.75.210.221:6969/announce`
- `http://211.75.210.221:80/announce`
- `http://31.38.161.123:6969/announce`
- `http://34.66.57.33:1337/announce`
- `http://34.66.57.33:2701/announce`
- `http://34.66.57.33:443/announce`
- `http://34.66.57.33:6969/announce`
- `http://43.250.54.126:6969/announce`
- `http://93.158.213.92:1337/announce`
- `http://94.23.207.177:6969/announce`
- `http://announce.sktorrent.eu:6969/announce`
- `http://ipv4announce.sktorrent.eu:6969/announce`
- `http://retracker01-msk-virt.corbina.net:80/announce`
- `http://tracker.auctor.tv:6969/announce`
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
- `https://2.tracker.eu.org:443/announce`
- `https://337hhh.xyz:443/announce`
- `https://open.ftorrent.com:443/announce`
- `udp://109.201.134.183:80/announce`
- `udp://151.242.104.187:80/announce`
- `udp://185.121.168.96:1337/announce`
- `udp://211.75.210.221:80/announce`
- `udp://31.56.179.159:6969/announce`
- `udp://34.66.57.33:1337/announce`
- `udp://43.250.54.126:6969/announce`
- `udp://52.58.128.163:6969/announce`
- `udp://65.109.28.17:6969/announce`
- `udp://93.158.213.92:6969/announce`
- `udp://95.217.80.20:6969/announce`
- `udp://95.217.80.22:6969/announce`
- `udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce`
- `udp://explodie.org:6969/announce`
- `udp://mail.segso.net:6969/announce`
- `udp://tracker.bittor.pw:1337/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.dler.org:6969/announce`
- `udp://tracker.ducks.party:1984/announce`
- `udp://tracker.gmi.gd:6969/announce`
- `udp://tracker.nyaa.vc:6969/announce`
- `udp://tracker.opentrackr.org:1337/announce`
- `udp://tracker.qu.ax:6969/announce`

## Discovery（自动发现的候选，Phase 1 隔离，不进 best/all）

- 候选总数: 161
- 通过探活: 10
- 若允许参与排名会入选的（前 4 条）:
  - `udp://tr4ck3r.duckdns.org:6969/announce`
  - `udp://209.141.59.25:6969/announce`
  - `udp://91.211.5.21:6969/announce`
  - `udp://tr.btube3.com:2010/announce`

转正方式：人工 review 后加入 `scripts/update_trackers.py` 的 SOURCES，或写进 `trackers/discovered/PROMOTE.md`（Phase 2）。


## 备选库（trackers_reserve.txt，前 10 条，按评分降序）

独立于 best/all 的候选订阅源，供人工审查转正。
1. `udp://tr4ck3r.duckdns.org:6969/announce`
2. `udp://209.141.59.25:6969/announce`
3. `http://34.66.57.33:1337/announce`
4. `http://34.66.57.33:443/announce`
5. `udp://211.75.210.221:80/announce`
6. `https://open.ftorrent.com:443/announce`
7. `udp://91.211.5.21:6969/announce`
8. `udp://tr.btube3.com:2010/announce`
9. `http://34.66.57.33:6969/announce`
10. `http://34.66.57.33:2701/announce`

