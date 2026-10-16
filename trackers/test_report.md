# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-16 21:28:02 UTC
- 总 Tracker 数: 320
- 存活 (alive): **114** (35%)
- 失效 (dead): **185**
- 不安全 (unsafe): **4**
- 无法测试 (untestable): 17
- 低速淘汰 (low-speed >5s): 0
- 同网段/同域名去重 (kept fastest): 57
- 综合评分后保留前 25 个，淘汰 32 个
- 评分维度: 速度 50% + 历史稳定性 20% + 响应质量 15%（含 peers 计数与 scrape 热度） + 跨源一致性 10% + 近期成功率 5%（速度标度自适应 + 经典高可用加分 + 反退化）
- 配额: 保底 4 条非 UDP + 保底 4 条经典高可用
- 协议多样性配额: 保底 4 条非 UDP，实际保留 9 条
- 耗时: 83.2 秒

## 协议分布

- udp: 58
- http: 43
- https: 13

## 最终订阅列表（前 25 个，按综合评分降序）

1. `https://t.213891.xyz:443/announce` — score=94.9, 71ms, 存活率100%, 质量90, 经典+0
2. `udp://open.stealth.si:80/announce` — score=93.6, 129ms, 存活率100%, 质量60, 经典+6
3. `udp://tracker.torrent.eu.org:451/announce` — score=93.4, 125ms, 存活率98%, 质量60, 经典+6
4. `udp://open.ftorrent.com:443/announce` — score=93.1, 19ms, 存活率100%, 质量60, 经典+0
5. `http://tracker.renfei.net:8080/announce` — score=92.8, 129ms, 存活率100%, 质量95, 经典+0
6. `https://tracker.zhuqiy.com:443/announce` — score=92.7, 114ms, 存活率96%, 质量95, 经典+0
7. `http://207.241.226.111:6969/announce` — score=92.2, 81ms, 存活率100%, 质量95, 经典+0
8. `udp://evan.im:6969/announce` — score=92.1, 37ms, 存活率100%, 质量60, 经典+0
9. `http://207.241.231.226:6969/announce` — score=92.1, 92ms, 存活率100%, 质量98, 经典+0
10. `https://tracker.nekomi.cn:443/announce` — score=91.9, 146ms, 存活率100%, 质量95, 经典+0
11. `https://tracker.7471.top:443/announce` — score=89.0, 190ms, 存活率100%, 质量90, 经典+0
12. `udp://martin-gebhardt.eu:25/announce` — score=88.1, 118ms, 存活率100%, 质量60, 经典+0
13. `udp://opentracker.lain.moscow:6969/announce` — score=87.7, 117ms, 存活率98%, 质量60, 经典+0
14. `udp://tracker.nyaa.vc:6969/announce` — score=87.3, 133ms, 存活率100%, 质量60, 经典+0
15. `udp://t.overflow.biz:6969/announce` — score=86.3, 152ms, 存活率100%, 质量60, 经典+0
16. `udp://retracker01-msk-virt.corbina.net:80/announce` — score=86.0, 159ms, 存活率100%, 质量60, 经典+0
17. `udp://tracker2.dler.org:80/announce` — score=85.7, 167ms, 存活率100%, 质量60, 经典+0
18. `https://2.tracker.eu.org:443/announce` — score=85.4, 61ms, 存活率100%, 质量90, 经典+0
19. `udp://34.66.57.33:1337/announce` — score=85.4, 23ms, 存活率98%, 质量60, 经典+0
20. `udp://kolankoalastree.newtrackon.co.nz:1337/announce` — score=85.4, 172ms, 存活率100%, 质量60, 经典+0
21. `http://140.235.237.23:6969/announce` — score=85.3, 88ms, 存活率100%, 质量98, 经典+0
22. `udp://tracker.004430.xyz:1337/announce` — score=85.0, 41ms, 存活率100%, 质量60, 经典+0
23. `udp://89.234.156.205:451/announce` — score=84.9, 122ms, 存活率100%, 质量60, 经典+0
24. `udp://mail.segso.net:6969/announce` — score=84.1, 138ms, 存活率100%, 质量60, 经典+0
25. `udp://193.148.251.93:6969/announce` — score=84.0, 23ms, 存活率91%, 质量60, 经典+0

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
- `http://185.185.40.95:6969/announce` — URLError: <urlopen error timed out>
- `http://bittorrent.kali.org:80/announce` — restricted (failure reason)
- `http://echostar.ddnsfree.com:8080/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://ehtracker.org:80/1104308/announce` — restricted (failure reason)
- `http://ehtracker.org:80/1113709/announce` — restricted (failure reason)
- `http://ehtracker.org:80/1226599/1080494xo5eXcwFOBq/announce` — restricted (failure reason)
- `http://ehtracker.org:80/2496841/announce` — restricted (failure reason)
- `http://ehtracker.org:80/2541477/announce` — restricted (failure reason)
- `http://ehtracker.org:80/2566145/1159106xUfsJkT9Btg/announce` — restricted (failure reason)
- `http://retracker.hotplug.ru:2710/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://tracker.hiyj.cn:80/announce` — HTTPError: HTTP Error 502: Bad Gateway
- `http://tracker.imgdump.lol:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.ipv6tracker.ru:80/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://tracker.iro.moe:80/announce` — timeout
- `http://tracker.kicks-ass.net:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.kuroy.me:5944/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://tracker.lelux.fi:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.letpo.com:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.lyretain.site:2710/announce` — URLError: <urlopen error timed out>
- `http://tracker.mg64.net:6881/announce` — URLError: <urlopen error timed out>
- `http://tracker.nartlof.com.br:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.netmap.top:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://tracker.noobsubs.net:80/announce` — URLError: <urlopen error [Errno -3] Temporary failure in name resolution>
- `http://tracker.nucozer-tracker.ml:2710/announce` — timeout
- `http://tracker.nyacat.pw:7000/announce.php` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.openbittorrent.com:80/announce` — URLError: <urlopen error [Errno -3] Temporary failure in name resolution>
- `http://tracker.openbittorrrent.com:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.openzim.org:80/announce` — restricted (failure reason)
- `http://tracker.pcfreetime.com:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://tracker.peckservers.com:9000/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://tracker.pimp4003.net:80/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `http://tracker.plx.im:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://tracker.publictorrent.net:80/announce` — URLError: <urlopen error [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:1010)>
- `http://tracker.sakurato.art:23333/announce` — URLError: <urlopen error timed out>
- `http://tracker.servequake.com:9999/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `http://tracker.sheesh.rip:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.shuntv.net:80/announce.php` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.skyts.net:6969/announce` — URLError: <urlopen error timed out>
- `http://tracker.srv00.com:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.srv00.com:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.sushirave.net:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.swateam.org.uk:2710/announce` — URLError: <urlopen error timed out>
- `http://tracker.swifte.space:2710/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.tfile.co:80/announce` — HTTPError: HTTP Error 403: Forbidden
- `http://tracker.tfile.me:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.tiny-vps.com:6969/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `http://tracker.torrentyorg.pl:80/announce` — URLError: <urlopen error [Errno -3] Temporary failure in name resolution>
- `http://tracker.trackerfix.com:80/announce` — URLError: <urlopen error [Errno -3] Temporary failure in name resolution>
- `http://tracker.tritan.gg:8080/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://tracker.tvunderground.org.ru:3218/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://tracker.umunu.ru:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://tracker.vrpnet.org:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.xfapi.top:6868/announce` — restricted (failure reason)
- `http://tracker.xfapi.top:9999/announce` — restricted (failure reason)
- `http://tracker.ygsub.com:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://tracker.yoshi210.com:6969/announce` — URLError: <urlopen error timed out>
- `http://tracker.yuelili.com:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.zerobytes.xyz:1337/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://tracker1.bt.moack.co.kr:80/announce` — URLError: <urlopen error timed out>
- `http://tracker1.torrentino.com:80/announce` — invalid bencoded response
- `http://tracker1.wasabii.com.tw:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker2.ctix.cn:2095/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker2.torrentino.com:80/announce` — invalid bencoded response
- `http://tracker2.wasabii.com.tw:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker3.ctix.cn:2095/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker3.ctix.cn:8080/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker3.torrentino.com:80/announce` — invalid bencoded response
- `http://trackers.ibzu.me:80/announce.php` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://trackers.ydns.eu:10036/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://trackme.theom.nz:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://trackr.appolon.dev:6969/announce` — URLError: <urlopen error timed out>
- `http://trun.tom.ru:80/announce` — HTTPError: HTTP Error 404: Not Found
- `http://unknownsite.de:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://uraniumhexafluori.de:1919/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://vps-c1adea63.vps.ovh.net:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://vps-dd0a0715.vps.ovh.net:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://vps02.net.orel.ru:80/announce` — URLError: <urlopen error timed out>
- `http://web.open-tracker.cf:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://wegkxfcivgx.ydns.eu:80/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://wepzone.net:6969/announce` — URLError: <urlopen error timed out>
- `http://wg.mortis.me:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://widemus.de:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://www.arabp2p.net:2052/f5a1e35785c9f3885fd54f34b6e262b8/announce` — restricted (failure reason)
- `http://www.chouchou.club:8080/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://www.nartlof.com.br:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
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
- `https://ht.therarbg.to:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.bt4g.com:443/announce` — timeout
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `udp://209.141.59.25:6969/announce` — no connect response
- `udp://6ahddutb1ucc3cp.ru:6969/announce` — no connect response
- `udp://exodus.desync.com:6969/announce` — no connect response
- `udp://open.tracker.ink:6969/announce` — no connect response
- `udp://opentor.org:2710/announce` — no connect response
- `udp://p4p.arenabg.com:1337/announce` — no connect response
- `udp://retracker.hotplug.ru:2710/announce` — no connect response
- `udp://torrentclub.online:54123/announce` — no connect response
- `udp://torrents.tmtime.dev:6969/announce` — no connect response
- `udp://tracker.alaskantf.com:6969/announce` — no connect response
- `udp://tracker.filemail.com:6969/announce` — no connect response
- `udp://tracker.srv00.com:6969/announce` — no connect response
- `udp://tracker.wepzone.net:6969/announce` — no connect response
- `udp://tracker1.itzmx.com:8080/announce` — no connect response
- `udp://tracker1.myporn.club:9337/announce` — no connect response
- `udp://wepzone.net:6969/announce` — no connect response
- `wss://tracker.openwebtorrent.com:443/announce` — SSLError: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1010)

## 不安全 Tracker（已过滤）

- `http://tracker.istole.it:80/announce` — resolves to private IP: 127.0.0.1
- `http://yggtracker.i2p.rocks:80/announce` — resolves to private IP: 200:1e2f:e608:eb3a:2bf:1e62:87ba:e2f7
- `https://bt.nfshost.com:443/announce` — resolves to private IP: 127.0.0.1
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
- `http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce`
- `http://ipv4announce.sktorrent.eu:6969/announce`
- `http://open.demonii.si:80/announce`
- `http://open.tracker.cl:1337/announce`
- `http://opentracker.xyz:80/announce`
- `http://retracker01-msk-virt.corbina.net:80/announce`
- `http://tracker.auctor.tv:6969/announce`
- `http://tracker.dhitechnical.com:6969/announce`
- `http://tracker.dler.com:6969/announce`
- `http://tracker.dler.org:6969/announce`
- `http://tracker.mywaifu.best:6969/announce`
- `http://tracker.novaopcj.eu.org:6969/announce`
- `http://tracker.nyaa.vc:6969/announce`
- `http://tracker.opentrackr.org:1337/announce`
- `http://tracker.qu.ax:6969/announce`
- `http://tracker.waaa.moe:6969/announce`
- `http://tracker2.dler.org:80/announce`
- `https://004430.xyz:443/announce`
- `https://1.tracker.eu.org:443/announce`
- `https://337hhh.xyz:443/announce`
- `https://4.tracker.eu.org:443/announce`
- `udp://151.242.104.187:80/announce`
- `udp://211.75.205.188:6969/announce`
- `udp://34.66.57.33:80/announce`
- `udp://45.137.199.107:6969/announce`
- `udp://65.109.28.17:6969/announce`
- `udp://93.158.213.92:6969/announce`
- `udp://95.217.80.20:6969/announce`
- `udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce`
- `udp://explodie.org:6969/announce`
- `udp://open.demonii.com:1337/announce`
- `udp://tracker-udp.gbitt.info:80/announce`
- `udp://tracker.bittor.pw:1337/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.dler.org:6969/announce`
- `udp://tracker.ducks.party:1984/announce`
- `udp://tracker.farted.net:6969/announce`
- `udp://tracker.gmi.gd:6969/announce`
- `udp://tracker.opentrackr.org:1337/announce`
- `udp://tracker.peerfect.org:6969/announce`
- `udp://tracker.qu.ax:6969/announce`
- `udp://tracker.skynetcloud.site:6969/announce`

## Discovery（自动发现的候选，Phase 1 隔离，不进 best/all）

- 候选总数: 158
- 通过探活: 3
- 若允许参与排名会入选的（前 2 条）:
  - `udp://tracker.aruku.ovh:8081/announce`
  - `http://tracker.zhuqiy.dgj055.icu:80/announce`

转正方式：人工 review 后加入 `scripts/update_trackers.py` 的 SOURCES，或写进 `trackers/discovered/PROMOTE.md`（Phase 2）。


## 备选库（trackers_reserve.txt，前 3 条，按评分降序）

独立于 best/all 的候选订阅源，供人工审查转正。
1. `udp://tracker.aruku.ovh:8081/announce`
2. `http://tracker.novaopcj.eu.org:6969/announce`
3. `http://tracker.zhuqiy.dgj055.icu:80/announce`

