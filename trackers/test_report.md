# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-13 22:58:45 UTC
- 总 Tracker 数: 320
- 存活 (alive): **124** (38%)
- 失效 (dead): **176**
- 不安全 (unsafe): **3**
- 无法测试 (untestable): 17
- 低速淘汰 (low-speed >5s): 0
- 同网段/同域名去重 (kept fastest): 61
- 综合评分后保留前 25 个，淘汰 38 个
- 评分维度: 速度 50% + 历史稳定性 20% + 响应质量 15%（含 peers 计数与 scrape 热度） + 跨源一致性 10% + 近期成功率 5%（速度标度自适应 + 经典高可用加分 + 反退化）
- 配额: 保底 4 条非 UDP + 保底 4 条经典高可用
- 协议多样性配额: 保底 4 条非 UDP，实际保留 8 条
- 耗时: 67.8 秒

## 协议分布

- udp: 63
- http: 46
- https: 15

## 最终订阅列表（前 25 个，按综合评分降序）

1. `http://207.241.226.111:6969/announce` — score=95.0, 34ms, 存活率100%, 质量98, 经典+0
2. `http://207.241.231.226:6969/announce` — score=94.4, 37ms, 存活率100%, 质量95, 经典+0
3. `udp://explodie.org:6969/announce` — score=93.1, 83ms, 存活率89%, 质量60, 经典+6
4. `udp://open.stealth.si:80/announce` — score=92.5, 149ms, 存活率100%, 质量60, 经典+6
5. `udp://open.ftorrent.com:443/announce` — score=92.0, 35ms, 存活率99%, 质量60, 经典+0
6. `udp://tracker.gmi.gd:6969/announce` — score=91.6, 40ms, 存活率98%, 质量60, 经典+0
7. `udp://tracker.bittor.pw:1337/announce` — score=91.4, 52ms, 存活率100%, 质量60, 经典+0
8. `http://tracker.renfei.net:8080/announce` — score=91.0, 165ms, 存活率100%, 质量95, 经典+0
9. `https://tracker.nekomi.cn:443/announce` — score=90.5, 175ms, 存活率100%, 质量95, 经典+0
10. `udp://evan.im:6969/announce` — score=88.3, 49ms, 存活率99%, 质量60, 经典+0
11. `http://004430.xyz:80/announce` — score=88.0, 24ms, 存活率100%, 质量95, 经典+0
12. `udp://tracker.skynetcloud.site:6969/announce` — score=87.6, 129ms, 存活率100%, 质量60, 经典+0
13. `udp://tracker.nyaa.vc:6969/announce` — score=87.1, 138ms, 存活率100%, 质量60, 经典+0
14. `udp://martin-gebhardt.eu:25/announce` — score=87.0, 135ms, 存活率99%, 质量60, 经典+0
15. `udp://tracker.ducks.party:1984/announce` — score=86.7, 146ms, 存活率100%, 质量60, 经典+0
16. `udp://opentracker.lain.moscow:6969/announce` — score=86.6, 143ms, 存活率99%, 质量60, 经典+0
17. `udp://tracker.004430.xyz:1337/announce` — score=86.6, 8ms, 存活率100%, 质量60, 经典+0
18. `udp://tracker2.dler.org:80/announce` — score=86.4, 152ms, 存活率100%, 质量60, 经典+0
19. `udp://tracker.torrent.eu.org:451/announce` — score=86.3, 150ms, 存活率75%, 质量60, 经典+6
20. `https://3.tracker.eu.org:443/announce` — score=86.2, 46ms, 存活率100%, 质量90, 经典+0
21. `udp://t.overflow.biz:6969/announce` — score=85.5, 153ms, 存活率96%, 质量60, 经典+0
22. `https://4.tracker.eu.org:443/announce` — score=84.7, 42ms, 存活率91%, 质量90, 经典+0
23. `http://tracker.dhitechnical.com:6969/announce` — score=84.2, 309ms, 存活率100%, 质量98, 经典+0
24. `udp://89.234.156.205:451/announce` — score=84.0, 136ms, 存活率99%, 质量60, 经典+0
25. `udp://exodus.desync.com:6969/announce` — score=79.8, 22ms, 存活率41%, 质量60, 经典+6

## 失效 Tracker

- `http://151.115.49.115:1337/announce` — URLError: <urlopen error timed out>
- `http://155.248.200.105:80/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://156.234.201.18:80/announce` — URLError: <urlopen error timed out>
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
- `http://179.100.24.134:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://180.139.151.58:6969/announce` — URLError: <urlopen error timed out>
- `http://185.148.3.231:80/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://185.185.40.51:6969/announce` — URLError: <urlopen error timed out>
- `http://185.185.40.95:6969/announce` — URLError: <urlopen error timed out>
- `http://185.197.195.20:1919/announce` — URLError: <urlopen error timed out>
- `http://185.216.178.49:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://185.230.4.150:1337/announce` — URLError: <urlopen error timed out>
- `http://79.111.12.213:6969/announce` — restricted (failure reason)
- `http://echostar.ddnsfree.com:8080/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://retracker.hotplug.ru:2710/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://tracker-udp.anirena.com:80/announce` — restricted (failure reason)
- `http://tracker.waaa.moe:6969/announce` — ConnectionResetError: [Errno 104] Connection reset by peer
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://ht.therarbg.to:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://simeon-vanov.github.io:443/cortiq-public` — invalid bencoded response
- `https://staticfile-bobcat.wasmer.app:443/announce` — HTTPError: HTTP Error 400: Bad Request
- `https://t.quic.ws:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://t.zerg.pw:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://t1.hloli.org:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://t1.tokhmi.xyz:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>
- `https://threads.canofsocks.com:443/announce` — HTTPError: HTTP Error 525: <none>
- `https://tixati.com:443/news` — invalid bencoded response
- `https://tk.mabo.ltd:443/announce` — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>
- `https://token.actions.githubusercontent.com:443` — HTTPError: HTTP Error 404: Not Found
- `https://torrent-tracker.hama3.net:443/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `https://torrents.tmtime.dev:443/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)>
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
- `https://tracker.kawaii.id:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
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
- `https://tracker.maya.no.eu.org:443/announce` — HTTPError: HTTP Error 429: Too Many Requests
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
- `https://tracker.opentracker.se:443/announce` — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>
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
- `https://tracker.yemekyedim.com:443/announce` — HTTPError: HTTP Error 521: <none>
- `https://tracker.yggleak.top:443/announce` — HTTPError: HTTP Error 521: <none>
- `https://tracker1.loli.co.nz:443/announce` — HTTPError: HTTP Error 530: <none>
- `https://tracker1.wimix.org:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://trackme.theom.nz:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://trakx.herokuapp.com:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://ttk.pp.ua:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://ttracker.just-h.party:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://voxhost.fr:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://w.wwwww.wtf:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://webtorrent.io:443` — invalid bencoded response
- `https://wolf.parrot.run:443/announce` — timeout
- `https://wsad.run.place:443/announce` — URLError: <urlopen error [Errno -3] Temporary failure in name resolution>
- `https://www.cloudflare.com:443/ips` — invalid bencoded response
- `https://www.peckservers.com:9443/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `https://www.wareztorrent.com:443/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://x7x.up.railway.app:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://xtremex.herokuapp.com:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://yggdrasil-network.github.io:443` — invalid bencoded response
- `https://zer0day.000webhostapp.com:443/announce` — URLError: <urlopen error [Errno -3] Temporary failure in name resolution>
- `udp://11.rarbg.com:80/announce` — no connect response
- `udp://1c.premierzal.ru:6969/announce` — no connect response
- `udp://208.83.20.20:6969/announce` — no connect response
- `udp://47.ip-51-68-199.eu:6969/announce` — no connect response
- `udp://6.pocketnet.app:6969/announce` — no connect response
- `udp://6ahddutb1ucc3cp.ru:6969/announce` — no connect response
- `udp://94-227-232-84.access.telenet.be:6969/announce` — no connect response
- `udp://960303.xyz:6969/announce` — no connect response
- `udp://aaa.army:8866/announce` — no connect response
- `udp://acxx.de:6969/announce` — no connect response
- `udp://admin.videoenpoche.info:6969/announce` — no connect response
- `udp://aegir.sexy:6969/announce` — no connect response
- `udp://torrentclub.online:54123/announce` — no connect response
- `udp://torrents.tmtime.dev:6969/announce` — no connect response
- `udp://tracker.alaskantf.com:6969/announce` — no connect response
- `udp://tracker.theoks.net:6969/announce` — no connect response
- `udp://tracker.tryhackx.org:6969/announce` — no connect response
- `wss://tracker.openwebtorrent.com:443/announce` — SSLError: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1010)

## 不安全 Tracker（已过滤）

- `http://yggtracker.i2p.rocks:80/announce` — resolves to private IP: 200:1e2f:e608:eb3a:2bf:1e62:87ba:e2f7
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
- `http://open.demonii.si:80/announce`
- `http://open.tracker.cl:1337/announce`
- `http://opentracker.xyz:80/announce`
- `http://retracker01-msk-virt.corbina.net:80/announce`
- `http://t.nyaatracker.com:80/announce`
- `http://t.overflow.biz:6969/announce`
- `http://tracker.004430.xyz:1337/announce`
- `http://tracker.auctor.tv:6969/announce`
- `http://tracker.coppersurfer.site:2710/announce`
- `http://tracker.dler.com:6969/announce`
- `http://tracker.dler.org:6969/announce`
- `http://tracker.mywaifu.best:6969/announce`
- `http://tracker.nyaa.vc:6969/announce`
- `http://tracker.opentrackr.org:1337/announce`
- `http://tracker.qu.ax:6969/announce`
- `http://tracker2.dler.org:80/announce`
- `https://004430.xyz:443/announce`
- `https://1.tracker.eu.org:443/announce`
- `https://2.tracker.eu.org:443/announce`
- `https://337hhh.xyz:443/announce`
- `https://tr.nyacat.pw:443/announce`
- `https://tr.torland.ga:443/announce`
- `udp://135.125.198.235:1984/announce`
- `udp://151.242.104.187:80/announce`
- `udp://209.141.59.25:6969/announce`
- `udp://34.66.57.33:1337/announce`
- `udp://34.66.57.33:80/announce`
- `udp://43.250.54.126:6969/announce`
- `udp://45.137.199.107:6969/announce`
- `udp://65.109.28.17:6969/announce`
- `udp://65.109.28.33:6969/announce`
- `udp://93.158.213.92:1337/announce`
- `udp://95.217.80.20:6969/announce`
- `udp://95.217.80.22:6969/announce`
- `udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce`
- `udp://open.demonii.com:1337/announce`
- `udp://retracker01-msk-virt.corbina.net:80/announce`
- `udp://tracker-udp.gbitt.info:80/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.dler.org:6969/announce`
- `udp://tracker.farted.net:6969/announce`
- `udp://tracker.filemail.com:6969/announce`
- `udp://tracker.opentrackr.org:1337/announce`
- `udp://tracker.peerfect.org:6969/announce`
- `udp://tracker.qu.ax:6969/announce`

## Discovery（自动发现的候选，Phase 1 隔离，不进 best/all）

- 候选总数: 167
- 通过探活: 10
- 若允许参与排名会入选的（前 6 条）:
  - `udp://tracker.cn.nyaa.net:6969/announce`
  - `udp://tracker.ilibr.org:6969/announce`
  - `udp://tracker.aruku.ovh:8081/announce`
  - `http://tr.nyacat.pw:80/announce`
  - `udp://admin.52ywp.com:6969/announce`
  - `https://tracker.bug38.com:443/announce`

转正方式：人工 review 后加入 `scripts/update_trackers.py` 的 SOURCES，或写进 `trackers/discovered/PROMOTE.md`（Phase 2）。


## 备选库（trackers_reserve.txt，前 10 条，按评分降序）

独立于 best/all 的候选订阅源，供人工审查转正。
1. `udp://tracker.cn.nyaa.net:6969/announce`
2. `udp://tracker.ilibr.org:6969/announce`
3. `udp://tracker.aruku.ovh:8081/announce`
4. `http://tr.nyacat.pw:80/announce`
5. `http://tracker.coppersurfer.site:2710/announce`
6. `http://t.nyaatracker.com:80/announce`
7. `http://t.overflow.biz:6969/announce`
8. `udp://admin.52ywp.com:6969/announce`
9. `https://tr.torland.ga:443/announce`
10. `https://tracker.bug38.com:443/announce`

