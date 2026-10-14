# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-14 05:07:19 UTC
- 总 Tracker 数: 307
- 存活 (alive): **150** (48%)
- 失效 (dead): **138**
- 不安全 (unsafe): **2**
- 无法测试 (untestable): 17
- 低速淘汰 (low-speed >5s): 3
- 同网段/同域名去重 (kept fastest): 75
- 综合评分后保留前 25 个，淘汰 47 个
- 评分维度: 速度 50% + 历史稳定性 20% + 响应质量 15%（含 peers 计数与 scrape 热度） + 跨源一致性 10% + 近期成功率 5%（速度标度自适应 + 经典高可用加分 + 反退化）
- 配额: 保底 4 条非 UDP + 保底 4 条经典高可用
- 协议多样性配额: 保底 4 条非 UDP，实际保留 9 条
- 耗时: 32.9 秒

## 协议分布

- udp: 93
- http: 41
- https: 16

## 最终订阅列表（前 25 个，按综合评分降序）

1. `https://t.213891.xyz:443/announce` — score=96.9, 32ms, 存活率100%, 质量90, 经典+0
2. `udp://explodie.org:6969/announce` — score=96.0, 34ms, 存活率91%, 质量60, 经典+6
3. `https://tracker.nekomi.cn:443/announce` — score=94.6, 93ms, 存活率100%, 质量95, 经典+0
4. `http://207.241.226.111:6969/announce` — score=94.2, 49ms, 存活率100%, 质量98, 经典+0
5. `http://207.241.231.226:6969/announce` — score=93.7, 51ms, 存活率100%, 质量95, 经典+0
6. `udp://open.demonii.com:1337/announce` — score=93.2, 135ms, 存活率99%, 质量60, 经典+6
7. `http://tracker.renfei.net:8080/announce` — score=92.1, 143ms, 存活率100%, 质量95, 经典+0
8. `udp://tracker.corpscorp.online:80/announce` — score=91.5, 49ms, 存活率100%, 质量60, 经典+0
9. `udp://tracker.gmi.gd:6969/announce` — score=91.4, 46ms, 存活率99%, 质量60, 经典+0
10. `https://tracker.7471.top:443/announce` — score=89.2, 187ms, 存活率100%, 质量90, 经典+0
11. `https://tracker.foreverpirates.co:443/announce` — score=87.5, 219ms, 存活率100%, 质量90, 经典+0
12. `udp://tracker.dler.org:6969/announce` — score=87.5, 131ms, 存活率100%, 质量60, 经典+0
13. `udp://tracker2.dler.org:80/announce` — score=87.4, 131ms, 存活率100%, 质量60, 经典+0
14. `udp://tracker.qu.ax:6969/announce` — score=86.8, 144ms, 存活率100%, 质量60, 经典+0
15. `udp://tracker.torrent.eu.org:451/announce` — score=86.5, 168ms, 存活率80%, 质量60, 经典+6
16. `udp://tracker.ducks.party:1984/announce` — score=86.5, 150ms, 存活率100%, 质量60, 经典+0
17. `udp://martin-gebhardt.eu:25/announce` — score=86.5, 147ms, 存活率99%, 质量60, 经典+0
18. `https://3.tracker.eu.org:443/announce` — score=86.4, 41ms, 存活率100%, 质量90, 经典+0
19. `udp://tracker.farted.net:6969/announce` — score=85.6, 165ms, 存活率99%, 质量60, 经典+0
20. `udp://tracker.004430.xyz:1337/announce` — score=85.5, 29ms, 存活率100%, 质量60, 经典+0
21. `udp://tracker.peerfect.org:6969/announce` — score=85.4, 169ms, 存活率99%, 质量60, 经典+0
22. `http://004430.xyz:80/announce` — score=85.0, 84ms, 存活率100%, 质量95, 经典+0
23. `udp://retracker01-msk-virt.corbina.net:80/announce` — score=84.6, 188ms, 存活率100%, 质量60, 经典+0
24. `udp://t.overflow.biz:6969/announce` — score=84.3, 181ms, 存活率97%, 质量60, 经典+0
25. `udp://89.234.156.205:451/announce` — score=83.0, 156ms, 存活率99%, 质量60, 经典+0

## 失效 Tracker

- `http://79.111.12.213:6969/announce` — restricted (failure reason)
- `http://bittorrent.kali.org:80/announce` — restricted (failure reason)
- `http://echostar.ddnsfree.com:8080/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://ehtracker.org:80/1104308/announce` — restricted (failure reason)
- `http://ehtracker.org:80/1113709/announce` — restricted (failure reason)
- `http://ehtracker.org:80/1226599/1080494xo5eXcwFOBq/announce` — restricted (failure reason)
- `http://ehtracker.org:80/2496841/announce` — restricted (failure reason)
- `http://ehtracker.org:80/2541477/announce` — restricted (failure reason)
- `http://ehtracker.org:80/2566145/1159106xUfsJkT9Btg/announce` — restricted (failure reason)
- `http://h4.trakx.nibba.trade:80/announce` — timeout
- `http://retracker.hotplug.ru:2710/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://torrenteditor.com:80` — invalid bencoded response
- `http://tracker.23794.top:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://tracker.bittor.pw:1337/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://anishkverma1-commits.github.io:443` — invalid bencoded response
- `https://buymeacoffee.com:443/SinZZzz` — invalid bencoded response
- `https://cf.trackerslist.com:443/all.txt` — invalid bencoded response
- `https://docs.sigstore.dev:443` — invalid bencoded response
- `https://geti2p.net:443` — invalid bencoded response
- `https://geti2p.net:443/en/docs/applications/bittorrent` — invalid bencoded response
- `https://gist.github.com:443/HaleTom/fe873dc2f3c5bd14f7418efefc2b91a8` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/AndrewMarchukov/tracker-add` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/BiglySoftware/BiglyBT` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/DeSireFire/animeTrackerList` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/GerryFerdinandus/bittorrent-tracker-editor` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/Jorman/Scripts` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/XIU2/TrackersListCollection` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/aria2/aria2` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/arvidn/libtorrent` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/blind-oracle/transmission-trackers` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/deluge-torrent/deluge` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/differentiated-aquilege508/MegaflowTracker-for-Nuke/raw/refs/heads/main/quaternity/Tracker-Nuke-Megaflow-for-1.6.zip` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/hezhijie0327/Trackerslist` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/mrgusux/automatic-trackers` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/mrgusux/automatic-trackers.git` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/ngosang/trackerslist` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/ngosang/trackerslist/issues/new` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/oilervoss/transmission` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/qbittorrent/qBittorrent` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/rocket049/aria2-trackers` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/simeon-vanov/cortiq-public/discussions` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/simeon-vanov/cortiq-public/issues/new/choose` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/simeon-vanov/cortiq-public/releases/latest` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/simeon-vanov/cortiq-public/releases/latest/download/Cortiq-win-Setup.exe` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/stefantalpalaru/deluge-default-trackers` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/transmission/transmission` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/wuyuansushen/aria2c_TrackersList` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/xXSalamanderXx/HDEncode-Search-Plus` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/xXSalamanderXx/RLSBB-Search-Plus` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/xXSalamanderXx/SlimBrave` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/xXSalamanderXx/caesium-image-compressor-linux` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/xXSalamanderXx/salamander-trackers/blob/main/LICENSE` — HTTPError: HTTP Error 400: Bad Request
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
- `https://pybittrack.retiolus.net:443/announce` — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>
- `https://raw.githubusercontent.com:443/B0zrx/RationTrack/main/docs/docs/docs/Ration-Track-2.6-beta.5.zip` — invalid bencoded response
- `https://raw.githubusercontent.com:443/gitovamb/trackers/main/logo/Software_v1.1.zip` — HTTPError: HTTP Error 404: Not Found
- `https://raw.githubusercontent.com:443/gitovamb/trackers/main/wbx_logo.png` — invalid bencoded response
- `https://raw.githubusercontent.com:443/mrgusux/automatic-trackers/main/SHA256SUMS.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/mrgusux/automatic-trackers/main/all_trackers.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/mrgusux/automatic-trackers/main/all_trackers_comma.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/mrgusux/automatic-trackers/main/api/badge.json` — invalid bencoded response
- `https://raw.githubusercontent.com:443/mrgusux/automatic-trackers/main/api/stats.json` — invalid bencoded response
- `https://raw.githubusercontent.com:443/mrgusux/automatic-trackers/main/api/trackers.json` — invalid bencoded response
- `https://raw.githubusercontent.com:443/mrgusux/automatic-trackers/main/trackers.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/ngosang/trackerslist/master/trackers_all.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/ngosang/trackerslist/master/trackers_all_http.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/ngosang/trackerslist/master/trackers_all_https.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/ngosang/trackerslist/master/trackers_all_i2p.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/ngosang/trackerslist/master/trackers_all_ip.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/ngosang/trackerslist/master/trackers_all_udp.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/ngosang/trackerslist/master/trackers_all_ws.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/ngosang/trackerslist/master/trackers_all_yggdrasil.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/ngosang/trackerslist/master/trackers_all_yggdrasil_ip.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/ngosang/trackerslist/master/trackers_best.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/ngosang/trackerslist/master/trackers_best_ip.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/xXSalamanderXx/salamander-trackers/refs/heads/main/combined.txt` — invalid bencoded response
- `https://sheraza2895.github.io:443` — invalid bencoded response
- `https://shields.io:443/badges/endpoint-badge` — invalid bencoded response
- `https://simeon-vanov.github.io:443/cortiq-public` — invalid bencoded response
- `https://tixati.com:443/news` — invalid bencoded response
- `https://token.actions.githubusercontent.com:443` — HTTPError: HTTP Error 404: Not Found
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.bt4g.com:443/announce` — timeout
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://webtorrent.io:443` — invalid bencoded response
- `https://www.cloudflare.com:443/ips` — invalid bencoded response
- `https://yggdrasil-network.github.io:443` — invalid bencoded response
- `udp://159.146.99.45:6969/announce` — no connect response
- `udp://193.148.251.93:6969/announce` — no connect response
- `udp://208.83.20.20:6969/announce` — announce no response
- `udp://34.66.57.33:1337/announce` — no connect response
- `udp://52.211.139.85:27022/announce` — announce no response
- `udp://6ahddutb1ucc3cp.ru:6969/announce` — no connect response
- `udp://edgev.duckdns.org:6969/announce` — no connect response
- `udp://exodus.desync.com:6969/announce` — no connect response
- `udp://ipv6.govt.hu:6969/announce` — no connect response
- `udp://open.tracker.ink:6969/announce` — no connect response
- `udp://opentor.org:2710/announce` — no connect response
- `udp://opentracker.lain.moscow:6969/announce` — no connect response
- `udp://p4p.arenabg.com:1337/announce` — no connect response
- `udp://retracker.hotplug.ru:2710/announce` — no connect response
- `udp://torrentclub.online:54123/announce` — no connect response
- `udp://torrents.tmtime.dev:6969/announce` — no connect response
- `udp://tracker.alaskantf.com:6969/announce` — no connect response
- `udp://tracker.filemail.com:6969/announce` — no connect response
- `udp://tracker.flatuslifir.is:6969/announce` — no connect response
- `udp://tracker.skyts.net:6969/announce` — no connect response
- `udp://tracker.srv00.com:6969/announce` — no connect response
- `udp://tracker.wepzone.net:6969/announce` — no connect response
- `udp://tracker.yume-hatsuyuki.moe:6969/announce` — no connect response
- `udp://tracker1.itzmx.com:8080/announce` — no connect response
- `udp://tracker1.myporn.club:9337/announce` — no connect response
- `udp://wepzone.net:6969/announce` — no connect response
- `udp://whybother.torrentonline.cc:42069/announce` — no connect response
- `udp://yuptracker-eu.gaijinent.com:27022/announce` — announce no response
- `wss://open.ftorrent.com:443` — SSLError: [SSL: TLSV1_UNRECOGNIZED_NAME] tlsv1 unrecognized name (_ssl.c:1010)
- `wss://tracker.openwebtorrent.com:443` — SSLError: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1010)
- `wss://tracker.openwebtorrent.com:443/announce` — SSLError: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1010)
- `wss://tracker.webtorrent.dev:443` — SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: IP address mismatch, certificate is not valid for '49.13.90.136'. (_ssl.c:1010)

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

## 低速 Tracker（>5s，已排除）

- `http://216.144.239.90:6969/announce` — 5837ms
- `http://tracker.waaa.moe:6969/announce` — 7832ms
- `https://tracker.bug38.com:443/announce` — 10753ms

## 同网段/同域名去重（保留响应最快）

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
- `http://31.38.161.123:6969/announce`
- `http://43.250.54.126:6969/announce`
- `http://93.158.213.92:1337/announce`
- `http://94.23.207.177:6969/announce`
- `http://announce.sktorrent.eu:6969/announce`
- `http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce`
- `http://ipv4announce.sktorrent.eu:6969/announce`
- `http://open.tracker.cl:1337/announce`
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
- `http://tracker.zhuqiy.dgj055.icu:80/announce`
- `http://tracker2.dler.org:80/announce`
- `https://004430.xyz:443/announce`
- `https://1.tracker.eu.org:443/announce`
- `https://2.tracker.eu.org:443/announce`
- `https://337hhh.xyz:443/announce`
- `https://4.tracker.eu.org:443/announce`
- `https://open.ftorrent.com:443/announce`
- `udp://107.189.2.131:1337/announce`
- `udp://135.125.198.235:1984/announce`
- `udp://178.239.19.29:80/announce`
- `udp://185.121.168.96:1337/announce`
- `udp://185.216.179.62:25/announce`
- `udp://193.187.90.12:6969/announce`
- `udp://209.141.59.25:6969/announce`
- `udp://211.75.205.187:6969/announce`
- `udp://211.75.205.188:80/announce`
- `udp://23.94.174.203:1337/announce`
- `udp://31.56.179.159:6969/announce`
- `udp://31.59.141.120:6969/announce`
- `udp://34.66.57.33:80/announce`
- `udp://43.250.54.126:6969/announce`
- `udp://47.76.201.250:6969/announce`
- `udp://65.109.28.17:6969/announce`
- `udp://65.109.28.33:6969/announce`
- `udp://74.81.245.60:2010/announce`
- `udp://83.102.180.21:80/announce`
- `udp://93.158.213.92:6969/announce`
- `udp://94.23.207.177:6969/announce`
- `udp://95.217.80.20:6969/announce`
- `udp://95.217.80.22:6969/announce`
- `udp://admin.52ywp.com:6969/announce`
- `udp://evan.im:6969/announce`
- `udp://kolankoalastree.newtrackon.co.nz:1337/announce`
- `udp://mail.segso.net:6969/announce`
- `udp://ns575949.ip-51-222-82.net:6969/announce`
- `udp://open.ftorrent.com:443/announce`
- `udp://open.stealth.si:80/announce`
- `udp://seedpeer.net:6969/announce`
- `udp://tr4ck3r.duckdns.org:6969/announce`
- `udp://tracker-udp.gbitt.info:80/announce`
- `udp://tracker.bittor.pw:1337/announce`
- `udp://tracker.k.vu:6969/announce`
- `udp://tracker.nyaa.vc:6969/announce`
- `udp://tracker.opentrackr.org:1337/announce`
- `udp://tracker.playground.ru:6969/announce`
- `udp://tracker.skynetcloud.site:6969/announce`

## Discovery（自动发现的候选，Phase 1 隔离，不进 best/all）

- 候选总数: 148
- 通过探活: 42
- 若允许参与排名会入选的（前 10 条）:
  - `udp://tr.btube3.com:2010/announce`
  - `udp://180.131.145.175:6969/announce`
  - `udp://149.106.106.25:443/announce`
  - `udp://164.152.110.70:6969/announce`
  - `udp://74.119.149.136:6969/announce`
  - `udp://51.222.82.36:6969/announce`
  - `udp://192.99.100.68:6969/announce`
  - `udp://160.30.240.158:1337/announce`
  - `udp://tracker.torrents.observer:80/announce`
  - `udp://bt-tracker.de:6969/announce`

转正方式：人工 review 后加入 `scripts/update_trackers.py` 的 SOURCES，或写进 `trackers/discovered/PROMOTE.md`（Phase 2）。


## 备选库（trackers_reserve.txt，前 20 条，按评分降序）

独立于 best/all 的候选订阅源，供人工审查转正。
1. `udp://tr.btube3.com:2010/announce`
2. `https://open.ftorrent.com:443/announce`
3. `udp://180.131.145.175:6969/announce`
4. `udp://seedpeer.net:6969/announce`
5. `udp://149.106.106.25:443/announce`
6. `udp://23.94.174.203:1337/announce`
7. `udp://164.152.110.70:6969/announce`
8. `udp://74.119.149.136:6969/announce`
9. `udp://51.222.82.36:6969/announce`
10. `udp://192.99.100.68:6969/announce`
11. `udp://ns575949.ip-51-222-82.net:6969/announce`
12. `udp://74.81.245.60:2010/announce`
13. `udp://211.75.205.187:6969/announce`
14. `udp://47.76.201.250:6969/announce`
15. `udp://94.23.207.177:6969/announce`
16. `udp://160.30.240.158:1337/announce`
17. `udp://185.216.179.62:25/announce`
18. `udp://tracker.torrents.observer:80/announce`
19. `udp://178.239.19.29:80/announce`
20. `udp://bt-tracker.de:6969/announce`

