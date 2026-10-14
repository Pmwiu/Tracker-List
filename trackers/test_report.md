# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-14 21:51:24 UTC
- 总 Tracker 数: 320
- 存活 (alive): **112** (35%)
- 失效 (dead): **187**
- 不安全 (unsafe): **4**
- 无法测试 (untestable): 17
- 低速淘汰 (low-speed >5s): 0
- 同网段/同域名去重 (kept fastest): 59
- 综合评分后保留前 25 个，淘汰 28 个
- 评分维度: 速度 50% + 历史稳定性 20% + 响应质量 15%（含 peers 计数与 scrape 热度） + 跨源一致性 10% + 近期成功率 5%（速度标度自适应 + 经典高可用加分 + 反退化）
- 配额: 保底 4 条非 UDP + 保底 4 条经典高可用
- 协议多样性配额: 保底 4 条非 UDP，实际保留 12 条
- 耗时: 73.6 秒

## 协议分布

- udp: 57
- http: 41
- https: 14

## 最终订阅列表（前 25 个，按综合评分降序）

1. `udp://explodie.org:6969/announce` — score=96.5, 42ms, 存活率95%, 质量60, 经典+6
2. `udp://tracker.opentrackr.org:1337/announce` — score=94.7, 107ms, 存活率100%, 质量60, 经典+6
3. `https://t.213891.xyz:443/announce` — score=94.2, 86ms, 存活率100%, 质量90, 经典+0
4. `udp://tracker.bittor.pw:1337/announce` — score=92.9, 22ms, 存活率100%, 质量60, 经典+0
5. `http://207.241.226.111:6969/announce` — score=92.9, 77ms, 存活率100%, 质量98, 经典+0
6. `udp://open.ftorrent.com:443/announce` — score=92.8, 21ms, 存活率100%, 质量60, 经典+0
7. `udp://evan.im:6969/announce` — score=92.3, 32ms, 存活率100%, 质量60, 经典+0
8. `http://tracker.renfei.net:8080/announce` — score=92.1, 143ms, 存活率100%, 质量95, 经典+0
9. `udp://tracker.torrent.eu.org:451/announce` — score=91.7, 114ms, 存活率90%, 质量60, 经典+6
10. `http://207.241.231.226:6969/announce` — score=91.5, 94ms, 存活率100%, 质量95, 经典+0
11. `https://tracker.nekomi.cn:443/announce` — score=90.6, 174ms, 存活率100%, 质量95, 经典+0
12. `https://tracker.7471.top:443/announce` — score=88.2, 207ms, 存活率100%, 质量90, 经典+0
13. `udp://tracker.ducks.party:1984/announce` — score=87.9, 122ms, 存活率100%, 质量60, 经典+0
14. `udp://martin-gebhardt.eu:25/announce` — score=87.6, 126ms, 存活率100%, 质量60, 经典+0
15. `udp://t.overflow.biz:6969/announce` — score=86.3, 147ms, 存活率98%, 质量60, 经典+0
16. `udp://retracker01-msk-virt.corbina.net:80/announce` — score=85.8, 164ms, 存活率100%, 质量60, 经典+0
17. `udp://tracker.dler.org:6969/announce` — score=85.4, 171ms, 存活率100%, 质量60, 经典+0
18. `udp://tracker.004430.xyz:1337/announce` — score=85.0, 39ms, 存活率100%, 质量60, 经典+0
19. `http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce` — score=84.8, 237ms, 存活率100%, 质量98, 经典+0
20. `https://3.tracker.eu.org:443/announce` — score=84.2, 85ms, 存活率100%, 质量90, 经典+0
21. `https://tracker.zhuqiy.com:443/announce` — score=84.2, 158ms, 存活率74%, 质量95, 经典+0
22. `udp://opentracker.lain.moscow:6969/announce` — score=84.1, 135ms, 存活率87%, 质量60, 经典+0
23. `https://4.tracker.eu.org:443/announce` — score=83.3, 91ms, 存活率96%, 质量90, 经典+0
24. `http://004430.xyz:80/announce` — score=83.1, 124ms, 存活率100%, 质量95, 经典+0
25. `http://140.235.237.23:6969/announce` — score=82.5, 145ms, 存活率100%, 质量98, 经典+0

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
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `http://www.yqzuji.com:80/announce` — HTTPError: HTTP Error 403: Forbidden
- `http://ydlkccp.dscloud.me:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://021912.xyz:443/announce` — timeout
- `https://9001-digitaladeel-bkwl-launch-oovrfk6mpz.app.codeanywhere.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for '9001-digitaladeel-bkwl-launch-oovrfk6mpz.app.codeanywhere.com'. (_ssl.c:1010)>
- `https://aaa.army:8866/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://abir0dev.github.io:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://anishkverma1-commits.github.io:443` — invalid bencoded response
- `https://api.ipv4online.uk:443/announce` — URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)>
- `https://banananetwork.qzz.io:443/announce` — timeout
- `https://bittorrent.gongt.net:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://bittracker.nekosunevr.co.uk:443/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `https://bt.080609.xyz:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://bt.endpot.com:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://bt2.080609.xyz:443/announce` — HTTPError: HTTP Error 403: Forbidden
- `https://buymeacoffee.com:443/SinZZzz` — invalid bencoded response
- `https://carapax.net:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://cernet-tracker.appspot.com:443/announce` — HTTPError: HTTP Error 503: Service Unavailable
- `https://cf.trackerslist.com:443/all.txt` — invalid bencoded response
- `https://chihaya-heroku.120181311.xyz:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://cny.fan:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://colibri.parrot.run:443/announce` — timeout
- `https://dev.tracker.cf-identity-wallet.metadata.dev.cf-deployments.org:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://docker-tracker-production.up.railway.app:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://docs.sigstore.dev:443` — invalid bencoded response
- `https://edgev.duckdns.org:443/announce` — HTTPError: HTTP Error 401: Unauthorized
- `https://evening-badlands-6215.herokuapp.com:443/announce` — HTTPError: HTTP Error 404: Not Found
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
- `https://grifon.info:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://hcbt.pp.ua:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://ht.therarbg.to:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://http1.torrust-tracker-demo.com:443/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `https://inferno.demonoid.is:443/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `https://k3tracker.cc:443/announce/0b0b5b2bb71770aa0df56f80a4863f07` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://nyaa.tracker.wf:7777/announce` — URLError: <urlopen error [SSL: WRONG_VERSION_NUMBER] wrong version number (_ssl.c:1010)>
- `https://open.kickasstracker.com:443/announce` — URLError: <urlopen error [SSL: TLSV1_UNRECOGNIZED_NAME] tlsv1 unrecognized name (_ssl.c:1010)>
- `https://opentracker.8880085.xyz:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://opentracker.cc:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate (_ssl.c:1010)>
- `https://opentracker.i2p.rocks:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://opentracker.xyz:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'opentracker.xyz'. (_ssl.c:1010)>
- `https://orgtgju.org:443/announce` — timeout
- `https://seeders-paradise.org:443/announce` — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>
- `https://shahidrazi.online:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://staticfile-bobcat.wasmer.app:443/announce` — HTTPError: HTTP Error 400: Bad Request
- `https://t.quic.ws:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://t.zerg.pw:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://t1.hloli.org:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://t1.tokhmi.xyz:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>
- `https://threads.canofsocks.com:443/announce` — HTTPError: HTTP Error 525: <none>
- `https://tk.mabo.ltd:443/announce` — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>
- `https://torrent-tracker.hama3.net:443/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `https://torrents.tmtime.dev:443/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `https://tr.bangumi.moe:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tr.doogh.club:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate (_ssl.c:1010)>
- `https://tr.kxmp.cf:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tr.ready4.icu:443/announce` — HTTPError: HTTP Error 521: <none>
- `https://tr.zukizuki.org:443/announce` — timeout
- `https://track3r.site:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker-zhuqiy.xn--1r3au8b.space:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.4.babico.name.tr:443/announce` — URLError: <urlopen error timed out>
- `https://tracker.aburaya.live:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.adgk.net:443/announce` — HTTPError: HTTP Error 522: Connection Timeout with Origin Server
- `https://tracker.alaskantf.com:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.anibt.net:443/announce` — restricted (failure reason)
- `https://tracker.baka.ink:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.bangumi.zip:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.belmult.online:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.bigbewbs.online:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.bjut.jp:443/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `https://tracker.bt-hash.com:443/announce` — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>
- `https://tracker.bt4g.com:443/announce` — timeout
- `https://tracker.cangku.moe:443/announce` — HTTPError: HTTP Error 500: Internal Server Error
- `https://tracker.cloudit.top:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.crawfish.cf:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.cutie.dating:443/announce` — URLError: <urlopen error timed out>
- `https://tracker.cybar.xyz:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.cyber-hub.net:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.dmhy.pw:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.dnlab.net:443/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `https://tracker.expli.top:443/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `https://tracker.feb217.tk:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.feb217.tk:8443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.gbitt.info:443/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `https://tracker.gcrenwp.top:443/announce` — HTTPError: HTTP Error 403: Forbidden
- `https://tracker.guguan.us.kg:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.h3o2.me:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.imgoingto.icu:443/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://tracker.iochimari.moe:443/announce` — HTTPError: HTTP Error 429: Too Many Requests
- `https://tracker.ipfsscan.io:443/announce` — URLError: <urlopen error timed out>
- `https://tracker.iriseden.fr:443/announce` — URLError: <urlopen error timed out>
- `https://tracker.kawaii.id:443/announce` — URLError: <urlopen error [Errno -3] Temporary failure in name resolution>
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.leechshield.link:443/announce` — timeout
- `https://tracker.lelux.fi:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `udp://23.157.120.14:6969/announce` — no connect response
- `udp://6ahddutb1ucc3cp.ru:6969/announce` — no connect response
- `udp://exodus.desync.com:6969/announce` — no connect response
- `udp://open.tracker.ink:6969/announce` — no connect response
- `udp://opentor.org:2710/announce` — no connect response
- `udp://p4p.arenabg.com:1337/announce` — no connect response
- `udp://retracker.hotplug.ru:2710/announce` — no connect response
- `udp://torrentclub.online:54123/announce` — no connect response
- `udp://torrents.tmtime.dev:6969/announce` — no connect response
- `udp://tracker.alaskantf.com:6969/announce` — no connect response
- `udp://tracker.gmi.gd:6969/announce` — no connect response
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
- `https://bt.nfshost.com:443/announce` — resolves to private IP: 127.0.0.1
- `https://k.avc.cx:443/announce.php` — resolves to private IP: 127.0.0.1
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
- `http://1337.abcvg.info:80/announce`
- `http://135.125.198.235:2710/announce`
- `http://135.125.198.235:80/announce`
- `http://189.18.97.208:6969/announce`
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
- `http://tracker.waaa.moe:6969/announce`
- `http://tracker2.dler.org:80/announce`
- `https://004430.xyz:443/announce`
- `https://1.tracker.eu.org:443/announce`
- `https://2.tracker.eu.org:443/announce`
- `https://337hhh.xyz:443/announce`
- `https://5.tracker.eu.org:443/announce`
- `https://tr.torland.ga:443/announce`
- `udp://135.125.198.235:1984/announce`
- `udp://211.75.205.188:6969/announce`
- `udp://34.66.57.33:1337/announce`
- `udp://34.66.57.33:80/announce`
- `udp://52.58.128.163:6969/announce`
- `udp://65.109.28.17:6969/announce`
- `udp://83.102.180.21:80/announce`
- `udp://91.216.110.53:451/announce`
- `udp://93.158.213.92:1337/announce`
- `udp://93.158.213.92:6969/announce`
- `udp://95.217.80.20:6969/announce`
- `udp://95.217.80.22:6969/announce`
- `udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce`
- `udp://mail.segso.net:6969/announce`
- `udp://open.demonii.com:1337/announce`
- `udp://open.stealth.si:80/announce`
- `udp://tracker-udp.gbitt.info:80/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.farted.net:6969/announce`
- `udp://tracker.nyaa.vc:6969/announce`
- `udp://tracker.peerfect.org:6969/announce`
- `udp://tracker.qu.ax:6969/announce`
- `udp://tracker.skynetcloud.site:6969/announce`

## Discovery（自动发现的候选，Phase 1 隔离，不进 best/all）

- 候选总数: 157
- 通过探活: 3
- 若允许参与排名会入选的（前 1 条）:
  - `http://asiatorrent.giize.com:51413/announce`

转正方式：人工 review 后加入 `scripts/update_trackers.py` 的 SOURCES，或写进 `trackers/discovered/PROMOTE.md`（Phase 2）。


## 备选库（trackers_reserve.txt，前 3 条，按评分降序）

独立于 best/all 的候选订阅源，供人工审查转正。
1. `http://189.18.97.208:6969/announce`
2. `https://tr.torland.ga:443/announce`
3. `http://asiatorrent.giize.com:51413/announce`

