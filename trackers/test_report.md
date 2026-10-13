# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-13 15:18:08 UTC
- 总 Tracker 数: 320
- 存活 (alive): **105** (32%)
- 失效 (dead): **193**
- 不安全 (unsafe): **5**
- 无法测试 (untestable): 17
- 低速淘汰 (low-speed >5s): 1
- 同网段/同域名去重 (kept fastest): 54
- 综合评分后保留前 25 个，淘汰 25 个
- 评分维度: 速度 50% + 历史稳定性 20% + 响应质量 15%（含 peers 计数与 scrape 热度） + 跨源一致性 10% + 近期成功率 5%（速度标度自适应 + 经典高可用加分 + 反退化）
- 配额: 保底 4 条非 UDP + 保底 4 条经典高可用
- 协议多样性配额: 保底 4 条非 UDP，实际保留 10 条
- 耗时: 44.6 秒

## 协议分布

- udp: 52
- http: 39
- https: 14

## 最终订阅列表（前 25 个，按综合评分降序）

1. `https://tracker.nekomi.cn:443/announce` — score=97.2, 41ms, 存活率100%, 质量95, 经典+0
2. `http://207.241.226.111:6969/announce` — score=96.3, 9ms, 存活率100%, 质量98, 经典+0
3. `udp://explodie.org:6969/announce` — score=96.2, 7ms, 存活率86%, 质量60, 经典+6
4. `http://207.241.231.226:6969/announce` — score=96.2, 9ms, 存活率100%, 质量98, 经典+0
5. `https://t.213891.xyz:443/announce` — score=94.5, 20ms, 存活率100%, 质量90, 经典+0
6. `https://1.tracker.eu.org:443/announce` — score=94.4, 22ms, 存活率100%, 质量90, 经典+0
7. `udp://open.stealth.si:80/announce` — score=92.4, 151ms, 存活率100%, 质量60, 经典+6
8. `udp://open.ftorrent.com:443/announce` — score=92.3, 28ms, 存活率99%, 质量60, 经典+0
9. `udp://tracker.gmi.gd:6969/announce` — score=91.4, 43ms, 存活率98%, 质量60, 经典+0
10. `http://tracker.renfei.net:8080/announce` — score=91.3, 160ms, 存活率100%, 质量95, 经典+0
11. `udp://evan.im:6969/announce` — score=87.2, 70ms, 存活率99%, 质量60, 经典+0
12. `http://004430.xyz:80/announce` — score=87.2, 40ms, 存活率100%, 质量95, 经典+0
13. `udp://tracker.dler.org:6969/announce` — score=87.1, 138ms, 存活率100%, 质量60, 经典+0
14. `udp://tracker-udp.gbitt.info:80/announce` — score=86.8, 144ms, 存活率100%, 质量60, 经典+0
15. `udp://tracker.skynetcloud.site:6969/announce` — score=86.8, 144ms, 存活率100%, 质量60, 经典+0
16. `udp://tracker.004430.xyz:1337/announce` — score=86.5, 10ms, 存活率100%, 质量60, 经典+0
17. `udp://tracker.ducks.party:1984/announce` — score=86.4, 151ms, 存活率100%, 质量60, 经典+0
18. `https://tracker.7471.top:443/announce` — score=86.1, 187ms, 存活率100%, 质量90, 经典+0
19. `udp://martin-gebhardt.eu:25/announce` — score=86.1, 153ms, 存活率99%, 质量60, 经典+0
20. `https://4.tracker.eu.org:443/announce` — score=85.3, 20ms, 存活率89%, 质量90, 经典+0
21. `udp://tracker.peerfect.org:6969/announce` — score=85.1, 172ms, 存活率99%, 质量60, 经典+0
22. `udp://34.66.57.33:1337/announce` — score=84.5, 45ms, 存活率99%, 质量60, 经典+0
23. `udp://t.overflow.biz:6969/announce` — score=84.5, 169ms, 存活率95%, 质量60, 经典+0
24. `udp://retracker01-msk-virt.corbina.net:80/announce` — score=84.3, 193ms, 存活率100%, 质量60, 经典+0
25. `https://tracker.foreverpirates.co:443/announce` — score=83.3, 243ms, 存活率100%, 质量90, 经典+0

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
- `http://180.97.219.76:8070/announce` — URLError: <urlopen error timed out>
- `http://182.176.139.129:6969/announce` — URLError: <urlopen error timed out>
- `http://185.130.47.2:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://216.144.239.90:6969/announce` — URLError: <urlopen error timed out>
- `http://bittorrent.kali.org:80/announce` — restricted (failure reason)
- `http://echostar.ddnsfree.com:8080/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://ehtracker.org:80/1104308/announce` — restricted (failure reason)
- `http://ehtracker.org:80/1113709/announce` — restricted (failure reason)
- `http://ehtracker.org:80/1226599/1080494xo5eXcwFOBq/announce` — restricted (failure reason)
- `http://ehtracker.org:80/2496841/announce` — restricted (failure reason)
- `http://ehtracker.org:80/2541477/announce` — restricted (failure reason)
- `http://ehtracker.org:80/2566145/1159106xUfsJkT9Btg/announce` — restricted (failure reason)
- `http://retracker.hotplug.ru:2710/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
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
- `https://edgev.duckdns.org:443/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
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
- `https://github.com:443/stefantalpalaru/deluge-default-trackers` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/transmission/transmission` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/wuyuansushen/aria2c_TrackersList` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/xXSalamanderXx/HDEncode-Search-Plus` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/xXSalamanderXx/RLSBB-Search-Plus` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/xXSalamanderXx/SlimBrave` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/xXSalamanderXx/caesium-image-compressor-linux` — HTTPError: HTTP Error 400: Bad Request
- `https://github.com:443/xXSalamanderXx/salamander-trackers/blob/main/LICENSE` — HTTPError: HTTP Error 400: Bad Request
- `https://grifon.info:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://hcbt.pp.ua:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://ht.therarbg.to:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://http1.torrust-tracker-demo.com:443/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `https://i2pplus.github.io:443` — invalid bencoded response
- `https://img.shields.io:443/badge/Download-Release-blue.svg` — invalid bencoded response
- `https://img.shields.io:443/github/stars/ngosang/trackerslist` — invalid bencoded response
- `https://inferno.demonoid.is:443/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `https://k3tracker.cc:443/announce/0b0b5b2bb71770aa0df56f80a4863f07` — URLError: <urlopen error [Errno -2] Name or service not known>
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
- `https://nyaa.tracker.wf:7777/announce` — URLError: <urlopen error [SSL: WRONG_VERSION_NUMBER] wrong version number (_ssl.c:1010)>
- `https://open.kickasstracker.com:443/announce` — URLError: <urlopen error [SSL: TLSV1_UNRECOGNIZED_NAME] tlsv1 unrecognized name (_ssl.c:1010)>
- `https://opentracker.8880085.xyz:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://opentracker.cc:443/announce` — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>
- `https://opentracker.i2p.rocks:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://opentracker.xyz:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'opentracker.xyz'. (_ssl.c:1010)>
- `https://orgtgju.org:443/announce` — timeout
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
- `https://seeders-paradise.org:443/announce` — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>
- `https://shahidrazi.online:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://sheraza2895.github.io:443` — invalid bencoded response
- `https://shields.io:443/badges/endpoint-badge` — invalid bencoded response
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.bt4g.com:443/announce` — timeout
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `udp://208.83.20.20:6969/announce` — no connect response
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
- `udp://tracker.srv00.com:6969/announce` — no connect response
- `udp://tracker.theoks.net:6969/announce` — no connect response
- `udp://tracker.torrent.eu.org:451/announce` — no connect response
- `udp://tracker.tryhackx.org:6969/announce` — no connect response
- `udp://tracker.wepzone.net:6969/announce` — no connect response
- `udp://tracker1.itzmx.com:8080/announce` — no connect response
- `udp://tracker1.myporn.club:9337/announce` — no connect response
- `udp://wegkxfcivgx.ydns.eu:80/announce` — no connect response
- `udp://wepzone.net:6969/announce` — no connect response
- `wss://spacetradersapi-chatbox.herokuapp.com:443/announce` — SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: IP address mismatch, certificate is not valid for '166.117.195.59'. (_ssl.c:1010)
- `wss://tracker.files.fm:7073/announce` — SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: IP address mismatch, certificate is not valid for '80.232.242.115'. (_ssl.c:1010)
- `wss://tracker.magnetoo.io:443/announce` — SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate (_ssl.c:1010)
- `wss://tracker.openwebtorrent.com:443/announce` — SSLError: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1010)

## 不安全 Tracker（已过滤）

- `http://yggtracker.i2p.rocks:80/announce` — resolves to private IP: 200:1e2f:e608:eb3a:2bf:1e62:87ba:e2f7
- `https://bt.nfshost.com:443/announce` — resolves to private IP: 127.0.0.1
- `https://k.avc.cx:443/announce.php` — resolves to private IP: 127.0.0.1
- `udp://open.dstud.io:6969/announce` — resolves to private IP: 0.0.0.0
- `wss://tracker.btorrent.xyz:443/announce` — resolves to private IP: 127.0.0.1

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

- `http://tracker.waaa.moe:6969/announce` — 5151ms

## 同网段/同域名去重（保留响应最快）

- `http://107.189.2.131:1337/announce`
- `http://1337.abcvg.info:80/announce`
- `http://135.125.198.235:2710/announce`
- `http://135.125.198.235:80/announce`
- `http://140.235.237.23:6969/announce`
- `http://211.75.205.187:6969/announce`
- `http://211.75.205.187:80/announce`
- `http://211.75.205.188:6969/announce`
- `http://211.75.205.188:80/announce`
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
- `http://tracker.dler.com:6969/announce`
- `http://tracker.dler.org:6969/announce`
- `http://tracker.mywaifu.best:6969/announce`
- `http://tracker.opentrackr.org:1337/announce`
- `http://tracker.qu.ax:6969/announce`
- `http://tracker2.dler.org:80/announce`
- `https://004430.xyz:443/announce`
- `https://2.tracker.eu.org:443/announce`
- `https://3.tracker.eu.org:443/announce`
- `https://337hhh.xyz:443/announce`
- `https://open.ftorrent.com:443/announce`
- `udp://109.201.134.183:80/announce`
- `udp://135.125.198.235:1984/announce`
- `udp://151.242.104.187:80/announce`
- `udp://211.75.205.188:80/announce`
- `udp://34.66.57.33:80/announce`
- `udp://43.250.54.126:6969/announce`
- `udp://45.137.199.107:6969/announce`
- `udp://65.109.28.17:6969/announce`
- `udp://65.109.28.33:6969/announce`
- `udp://83.102.180.21:80/announce`
- `udp://93.158.213.92:1337/announce`
- `udp://95.217.80.22:6969/announce`
- `udp://mail.segso.net:6969/announce`
- `udp://open.demonii.com:1337/announce`
- `udp://tracker.bittor.pw:1337/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.farted.net:6969/announce`
- `udp://tracker.filemail.com:6969/announce`
- `udp://tracker.nyaa.vc:6969/announce`
- `udp://tracker.opentrackr.org:1337/announce`
- `udp://tracker.qu.ax:6969/announce`
- `udp://tracker2.dler.org:80/announce`

## Discovery（自动发现的候选，Phase 1 隔离，不进 best/all）

- 候选总数: 157
- 通过探活: 4
- 若允许参与排名会入选的（前 3 条）:
  - `udp://tracker.wildkat.net:6969/announce`
  - `udp://tr4ck3r.duckdns.org:6969/announce`
  - `udp://51.81.222.188:6969/announce`

转正方式：人工 review 后加入 `scripts/update_trackers.py` 的 SOURCES，或写进 `trackers/discovered/PROMOTE.md`（Phase 2）。


## 备选库（trackers_reserve.txt，前 4 条，按评分降序）

独立于 best/all 的候选订阅源，供人工审查转正。
1. `udp://tracker.wildkat.net:6969/announce`
2. `udp://tr4ck3r.duckdns.org:6969/announce`
3. `udp://51.81.222.188:6969/announce`
4. `https://open.ftorrent.com:443/announce`

