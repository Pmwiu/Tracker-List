# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-17 00:01:39 UTC
- 总 Tracker 数: 320
- 存活 (alive): **117** (36%)
- 失效 (dead): **182**
- 不安全 (unsafe): **4**
- 无法测试 (untestable): 17
- 低速淘汰 (low-speed >5s): 0
- 同网段/同域名去重 (kept fastest): 57
- 综合评分后保留前 25 个，淘汰 35 个
- 评分维度: 速度 50% + 历史稳定性 20% + 响应质量 15%（含 peers 计数与 scrape 热度） + 跨源一致性 10% + 近期成功率 5%（速度标度自适应 + 经典高可用加分 + 反退化）
- 配额: 保底 4 条非 UDP + 保底 4 条经典高可用
- 协议多样性配额: 保底 4 条非 UDP，实际保留 8 条
- 耗时: 69.7 秒

## 协议分布

- udp: 63
- http: 40
- https: 14

## 最终订阅列表（前 25 个，按综合评分降序）

1. `https://t.213891.xyz:443/announce` — score=95.3, 64ms, 存活率100%, 质量90, 经典+0
2. `https://tracker.zhuqiy.com:443/announce` — score=94.2, 88ms, 存活率97%, 质量95, 经典+0
3. `udp://tracker.torrent.eu.org:451/announce` — score=94.1, 113ms, 存活率99%, 质量60, 经典+6
4. `http://207.241.226.111:6969/announce` — score=92.8, 77ms, 存活率100%, 质量98, 经典+0
5. `udp://open.ftorrent.com:443/announce` — score=92.8, 24ms, 存活率100%, 质量60, 经典+0
6. `http://tracker.renfei.net:8080/announce` — score=92.7, 132ms, 存活率100%, 质量95, 经典+0
7. `udp://evan.im:6969/announce` — score=92.2, 35ms, 存活率100%, 质量60, 经典+0
8. `udp://open.demonii.com:1337/announce` — score=91.9, 161ms, 存活率100%, 质量60, 经典+6
9. `http://207.241.231.226:6969/announce` — score=91.6, 92ms, 存活率100%, 质量95, 经典+0
10. `https://tracker.nekomi.cn:443/announce` — score=90.7, 170ms, 存活率100%, 质量95, 经典+0
11. `https://tracker.7471.top:443/announce` — score=90.1, 168ms, 存活率100%, 质量90, 经典+0
12. `udp://tracker.gmi.gd:6969/announce` — score=89.0, 76ms, 存活率97%, 质量60, 经典+0
13. `udp://tracker.qu.ax:6969/announce` — score=88.4, 112ms, 存活率100%, 质量60, 经典+0
14. `udp://tracker-udp.gbitt.info:80/announce` — score=88.4, 112ms, 存活率100%, 质量60, 经典+0
15. `udp://martin-gebhardt.eu:25/announce` — score=87.8, 123ms, 存活率100%, 质量60, 经典+0
16. `udp://opentracker.lain.moscow:6969/announce` — score=87.0, 132ms, 存活率98%, 质量60, 经典+0
17. `udp://t.overflow.biz:6969/announce` — score=86.5, 150ms, 存活率100%, 质量60, 经典+0
18. `udp://retracker01-msk-virt.corbina.net:80/announce` — score=86.0, 161ms, 存活率100%, 质量60, 经典+0
19. `https://3.tracker.eu.org:443/announce` — score=85.8, 55ms, 存活率100%, 质量90, 经典+0
20. `udp://tracker2.dler.org:80/announce` — score=85.7, 167ms, 存活率100%, 质量60, 经典+0
21. `udp://34.66.57.33:1337/announce` — score=85.5, 22ms, 存活率98%, 质量60, 经典+0
22. `udp://kolankoalastree.newtrackon.co.nz:1337/announce` — score=85.2, 174ms, 存活率100%, 质量60, 经典+0
23. `udp://tracker.004430.xyz:1337/announce` — score=84.9, 42ms, 存活率100%, 质量60, 经典+0
24. `udp://89.234.156.205:451/announce` — score=84.7, 127ms, 存活率100%, 质量60, 经典+0
25. `udp://exodus.desync.com:6969/announce` — score=84.0, 52ms, 存活率48%, 质量60, 经典+6

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
- `http://185.185.40.51:6969/announce` — URLError: <urlopen error timed out>
- `http://185.197.195.20:1919/announce` — URLError: <urlopen error timed out>
- `http://79.111.12.213:6969/announce` — restricted (failure reason)
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
- `https://opentracker.cc:443/announce` — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>
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
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>
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
- `https://tracker.iochimari.moe:443/announce` — HTTPError: HTTP Error 403: Forbidden
- `https://tracker.ipfsscan.io:443/announce` — URLError: <urlopen error timed out>
- `https://tracker.iriseden.fr:443/announce` — URLError: <urlopen error timed out>
- `https://tracker.kawaii.id:443/announce` — URLError: <urlopen error [Errno -3] Temporary failure in name resolution>
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.leechshield.link:443/announce` — timeout
- `https://tracker.lelux.fi:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.lenition.de:443/announce` — URLError: <urlopen error timed out>
- `https://tracker.lilithraws.org:443/announce` — timeout
- `https://tracker.logirl.moe:443/announce` — URLError: <urlopen error timed out>
- `https://tracker.loli.co.nz:443/announce` — HTTPError: HTTP Error 530: <none>
- `https://tracker.loligirl.cn:443/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `https://tracker.manager.itislove.cz:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>
- `https://tracker.manager.v6.navy:443/announce` — URLError: <urlopen error [Errno -3] Temporary failure in name resolution>
- `https://tracker.maya.no.eu.org:443/announce` — restricted (failure reason)
- `https://tracker.mlsub.net:443/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `https://tracker.moeblog.cn:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.moeking.me:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.monikadesign.uk:443/announce/63ea34cb9815cd28d63fc75b2f2c5a56` — restricted (failure reason)
- `https://tracker.monikadesign.uk:443/announce/a46be21ab845cc0d534d06fea801f95a` — restricted (failure reason)
- `https://tracker.moxing.party:6969/announce` — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>
- `https://tracker.nanoha.org:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.netmap.top:8443/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `https://tracker.nitrix.me:443/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `https://tracker.novy.vip:443/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `https://tracker.nyaa.tk:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.onetracker.net:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.opentracker.se:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate (_ssl.c:1010)>
- `https://tracker.parrotlinux.org:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tracker.pterclub.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>
- `https://tracker.publictorrent.net:443/announce` — URLError: <urlopen error [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:1010)>
- `https://tracker.puvvadi.net:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.qingwa.pro:443/announce` — invalid bencoded response
- `https://tracker.renfei.net:443/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `https://tracker.sakurato.art:23334/announce` — URLError: <urlopen error timed out>
- `https://tracker.samcze.pl:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate (_ssl.c:1010)>
- `https://tracker.skynetcloud.site:8443/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `https://tracker.srv00.com:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.tamersunion.org:443/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `https://tracker.tvgc.win:443/announce` — empty response
- `https://tracker.vectahosting.eu:443/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `udp://6ahddutb1ucc3cp.ru:6969/announce` — no connect response
- `udp://74.81.245.60:2010/announce` — no connect response
- `udp://edgev.duckdns.org:6969/announce` — no connect response
- `udp://open.tracker.ink:6969/announce` — no connect response
- `udp://opentor.org:2710/announce` — no connect response
- `udp://p4p.arenabg.com:1337/announce` — no connect response
- `udp://retracker.hotplug.ru:2710/announce` — no connect response
- `udp://torrentclub.online:54123/announce` — no connect response
- `udp://torrents.tmtime.dev:6969/announce` — no connect response
- `udp://tracker.alaskantf.com:6969/announce` — no connect response
- `udp://tracker.filemail.com:6969/announce` — no connect response
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
- `https://k.avc.cx:443/announce.php` — resolves to private IP: 127.0.0.1
- `https://tracker.parrotsec.org:443/announce` — resolves to private IP: 0.0.0.0
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

- `http://135.125.198.235:2710/announce`
- `http://135.125.198.235:80/announce`
- `http://140.235.237.23:6969/announce`
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
- `http://tracker.dler.com:6969/announce`
- `http://tracker.dler.org:6969/announce`
- `http://tracker.mywaifu.best:6969/announce`
- `http://tracker.opentrackr.org:1337/announce`
- `http://tracker.qu.ax:6969/announce`
- `http://tracker.waaa.moe:6969/announce`
- `http://tracker2.dler.org:80/announce`
- `https://004430.xyz:443/announce`
- `https://1.tracker.eu.org:443/announce`
- `https://337hhh.xyz:443/announce`
- `https://4.tracker.eu.org:443/announce`
- `https://tr.torland.ga:443/announce`
- `udp://109.201.134.183:80/announce`
- `udp://185.121.168.96:1337/announce`
- `udp://209.141.59.25:6969/announce`
- `udp://211.75.205.187:6969/announce`
- `udp://211.75.205.188:6969/announce`
- `udp://211.75.210.221:80/announce`
- `udp://34.66.57.33:80/announce`
- `udp://43.250.54.126:6969/announce`
- `udp://45.137.199.107:6969/announce`
- `udp://65.109.28.17:6969/announce`
- `udp://91.216.110.53:451/announce`
- `udp://93.158.213.92:6969/announce`
- `udp://95.217.80.20:6969/announce`
- `udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce`
- `udp://explodie.org:6969/announce`
- `udp://open.stealth.si:80/announce`
- `udp://tracker.bittor.pw:1337/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.dler.org:6969/announce`
- `udp://tracker.ducks.party:1984/announce`
- `udp://tracker.farted.net:6969/announce`
- `udp://tracker.nyaa.vc:6969/announce`
- `udp://tracker.opentrackr.org:1337/announce`
- `udp://tracker.peerfect.org:6969/announce`
- `udp://tracker.skynetcloud.site:6969/announce`

## Discovery（自动发现的候选，Phase 1 隔离，不进 best/all）

- 候选总数: 157
- 通过探活: 8
- 若允许参与排名会入选的（前 5 条）:
  - `udp://tr.btube3.com:2010/announce`
  - `udp://38.180.157.12:2715/announce`
  - `udp://159.146.99.45:6969/announce`
  - `udp://211.75.205.187:80/announce`
  - `http://asiatorrent.giize.com:51413/announce`

转正方式：人工 review 后加入 `scripts/update_trackers.py` 的 SOURCES。

