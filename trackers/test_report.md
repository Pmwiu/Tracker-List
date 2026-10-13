# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-13 14:27:37 UTC
- 总 Tracker 数: 320
- 存活 (alive): **111** (34%)
- 失效 (dead): **186**
- 不安全 (unsafe): **6**
- 无法测试 (untestable): 17
- 低速淘汰 (low-speed >5s): 0
- 同网段/同域名去重 (kept fastest): 57
- 综合评分后保留前 25 个，淘汰 29 个
- 评分维度: 速度 50% + 历史稳定性 20% + 响应质量 15%（含 peers 计数与 scrape 热度） + 跨源一致性 10% + 近期成功率 5%（速度标度自适应 + 经典高可用加分 + 反退化）
- 配额: 保底 4 条非 UDP + 保底 4 条经典高可用
- 协议多样性配额: 保底 4 条非 UDP，实际保留 7 条
- 耗时: 92.0 秒

## 协议分布

- udp: 55
- http: 43
- https: 13

## 最终订阅列表（前 25 个，按综合评分降序）

1. `https://tracker.nekomi.cn:443/announce` — score=94.9, 87ms, 存活率100%, 质量95, 经典+0
2. `https://1.tracker.eu.org:443/announce` — score=94.3, 24ms, 存活率100%, 质量90, 经典+0
3. `http://207.241.231.226:6969/announce` — score=94.3, 48ms, 存活率100%, 质量98, 经典+0
4. `http://207.241.226.111:6969/announce` — score=94.2, 49ms, 存活率100%, 质量98, 经典+0
5. `udp://explodie.org:6969/announce` — score=93.7, 42ms, 存活率82%, 质量60, 经典+6
6. `udp://tracker.opentrackr.org:1337/announce` — score=93.2, 136ms, 存活率100%, 质量60, 经典+6
7. `udp://open.ftorrent.com:443/announce` — score=92.3, 27ms, 存活率98%, 质量60, 经典+0
8. `http://tracker.renfei.net:8080/announce` — score=92.2, 142ms, 存活率100%, 质量95, 经典+0
9. `udp://tracker.torrent.eu.org:451/announce` — score=88.8, 177ms, 存活率92%, 质量60, 经典+6
10. `udp://tracker2.dler.org:80/announce` — score=87.5, 131ms, 存活率100%, 质量60, 经典+0
11. `udp://tracker.dler.org:6969/announce` — score=87.4, 131ms, 存活率100%, 质量60, 经典+0
12. `udp://evan.im:6969/announce` — score=87.2, 68ms, 存活率98%, 质量60, 经典+0
13. `udp://tracker-udp.gbitt.info:80/announce` — score=87.0, 141ms, 存活率100%, 质量60, 经典+0
14. `udp://tracker.skynetcloud.site:6969/announce` — score=86.9, 142ms, 存活率100%, 质量60, 经典+0
15. `https://3.tracker.eu.org:443/announce` — score=86.8, 32ms, 存活率100%, 质量90, 经典+0
16. `udp://opentracker.lain.moscow:6969/announce` — score=86.1, 151ms, 存活率98%, 质量60, 经典+0
17. `udp://tracker.004430.xyz:1337/announce` — score=85.5, 30ms, 存活率100%, 质量60, 经典+0
18. `udp://tracker.farted.net:6969/announce` — score=85.5, 165ms, 存活率99%, 质量60, 经典+0
19. `udp://tracker.peerfect.org:6969/announce` — score=85.3, 167ms, 存活率98%, 质量60, 经典+0
20. `http://004430.xyz:80/announce` — score=85.0, 85ms, 存活率100%, 质量95, 经典+0
21. `udp://retracker01-msk-virt.corbina.net:80/announce` — score=84.6, 189ms, 存活率100%, 质量60, 经典+0
22. `udp://193.148.251.93:6969/announce` — score=84.4, 44ms, 存活率98%, 质量60, 经典+0
23. `udp://34.66.57.33:1337/announce` — score=84.3, 49ms, 存活率99%, 质量60, 经典+0
24. `udp://t.overflow.biz:6969/announce` — score=83.9, 176ms, 存活率93%, 质量60, 经典+0
25. `udp://martin-gebhardt.eu:25/announce` — score=83.1, 152ms, 存活率98%, 质量60, 经典+0

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
- `http://tr.bangumi.moe:80/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://tr.cili001.com:8070/announce` — URLError: <urlopen error timed out>
- `http://tr.kxmp.cf:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tr1.aag.moe:2095/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `http://tracker.23794.top:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://tracker.aibt.xyz:900/announce` — URLError: <urlopen error timed out>
- `http://tracker.aletorrenty.pl:2710/announce` — URLError: <urlopen error timed out>
- `http://tracker.baka-sub.cf:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.baravik.org:6970/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.beeimg.com:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://tracker.bittor.pw:1337/announce` — timeout
- `http://tracker.bittorrent.am:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `http://tracker.bittorrent.nibblepoker.lu:49227/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.bt-chat.com:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.bt4g.com:2095/announce` — timeout
- `http://tracker.btcake.com:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.btsync.gq:233/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.btzero.net:8080/announce` — URLError: <urlopen error timed out>
- `http://tracker.calculate.ru:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.cbase.cc:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.chaoz.li:2710/announce` — URLError: <urlopen error timed out>
- `http://tracker.digital-alpha-world.de:6969/announce` — URLError: <urlopen error timed out>
- `http://tracker.dutchtracking.com:80/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `http://tracker.dutchtracking.nl:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.edkj.club:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.edoardocolombo.eu:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.encrypted-data.xyz:1337/announce` — URLError: <urlopen error timed out>
- `http://tracker.ex.ua:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.exe.in.th:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://tracker.file09.com:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.filemail.com:6969/announce` — URLError: <urlopen error timed out>
- `http://tracker.files.fm:6969/announce` — URLError: <urlopen error timed out>
- `http://tracker.filetracker.pl:8089/announce` — URLError: <urlopen error timed out>
- `http://tracker.flashtorrents.org:6969/announce` — URLError: <urlopen error timed out>
- `http://tracker.gbitt.info:80/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `http://tracker.gdp.pw:900/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://tracker.grepler.com:6969/announce` — URLError: <urlopen error timed out>
- `http://tracker.guguan.000.pe:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.h0me.cc:8880/announce` — timeout
- `http://tracker.hiyj.cn:80/announce` — HTTPError: HTTP Error 502: Bad Gateway
- `http://tracker.imgdump.lol:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.ipv6tracker.ru:80/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://tracker.iro.moe:80/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
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
- `http://tracker2.torrentino.com:80/announce` — HTTPError: HTTP Error 429: Too Many Requests
- `http://tracker2.wasabii.com.tw:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker3.ctix.cn:2095/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker3.ctix.cn:8080/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker3.torrentino.com:80/announce` — HTTPError: HTTP Error 429: Too Many Requests
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
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://ht.therarbg.to:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [Errno 104] Connection reset by peer>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error [Errno 104] Connection reset by peer>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.bt4g.com:443/announce` — timeout
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `udp://52.58.128.163:6969/announce` — no connect response
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
- `udp://tracker.tryhackx.org:6969/announce` — no connect response
- `udp://tracker.wepzone.net:6969/announce` — no connect response
- `udp://tracker1.itzmx.com:8080/announce` — no connect response
- `udp://tracker1.myporn.club:9337/announce` — no connect response
- `udp://wegkxfcivgx.ydns.eu:80/announce` — no connect response
- `udp://wepzone.net:6969/announce` — no connect response
- `wss://spacetradersapi-chatbox.herokuapp.com:443/announce` — SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: IP address mismatch, certificate is not valid for '166.117.185.84'. (_ssl.c:1010)
- `wss://tracker.files.fm:7073/announce` — SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: IP address mismatch, certificate is not valid for '80.232.242.115'. (_ssl.c:1010)
- `wss://tracker.openwebtorrent.com:443/announce` — SSLError: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1010)

## 不安全 Tracker（已过滤）

- `http://tracker.ccc.de:80/announce` — resolves to private IP: 127.0.0.1
- `http://tracker.computel.fr:80/announce` — resolves to private IP: 0.0.0.0
- `http://tracker.istole.it:80/announce` — resolves to private IP: 127.0.0.1
- `http://yggtracker.i2p.rocks:80/announce` — resolves to private IP: 200:1e2f:e608:eb3a:2bf:1e62:87ba:e2f7
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

## 同网段/同域名去重（保留响应最快）

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
- `http://open.demonii.si:80/announce`
- `http://opentracker.xyz:80/announce`
- `http://retracker01-msk-virt.corbina.net:80/announce`
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
- `http://tracker.waaa.moe:6969/announce`
- `http://tracker2.dler.org:80/announce`
- `https://004430.xyz:443/announce`
- `https://2.tracker.eu.org:443/announce`
- `https://337hhh.xyz:443/announce`
- `https://4.tracker.eu.org:443/announce`
- `https://tr.nyacat.pw:443/announce`
- `udp://109.201.134.183:80/announce`
- `udp://211.75.205.188:80/announce`
- `udp://31.56.179.159:6969/announce`
- `udp://34.66.57.33:80/announce`
- `udp://43.250.54.126:6969/announce`
- `udp://65.109.28.17:6969/announce`
- `udp://65.109.28.33:6969/announce`
- `udp://83.102.180.21:80/announce`
- `udp://93.158.213.92:1337/announce`
- `udp://93.158.213.92:6969/announce`
- `udp://95.217.80.22:6969/announce`
- `udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce`
- `udp://mail.segso.net:6969/announce`
- `udp://open.demonii.com:1337/announce`
- `udp://open.stealth.si:80/announce`
- `udp://tracker.bittor.pw:1337/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.ducks.party:1984/announce`
- `udp://tracker.gmi.gd:6969/announce`
- `udp://tracker.nyaa.vc:6969/announce`
- `udp://tracker.qu.ax:6969/announce`

## Discovery（自动发现的候选，Phase 1 隔离，不进 best/all）

- 候选总数: 168
- 通过探活: 6
- 若允许参与排名会入选的（前 3 条）:
  - `udp://208.83.20.20:6969/announce`
  - `http://tr.nyacat.pw:80/announce`
  - `http://tracker.zhuqiy.dgj055.icu:80/announce`

转正方式：人工 review 后加入 `scripts/update_trackers.py` 的 SOURCES，或写进 `trackers/discovered/PROMOTE.md`（Phase 2）。


## 备选库（trackers_reserve.txt，前 6 条，按评分降序）

独立于 best/all 的候选订阅源，供人工审查转正。
1. `udp://208.83.20.20:6969/announce`
2. `udp://211.75.205.188:80/announce`
3. `http://tr.nyacat.pw:80/announce`
4. `http://tracker.novaopcj.eu.org:6969/announce`
5. `http://tracker.coppersurfer.site:2710/announce`
6. `http://tracker.zhuqiy.dgj055.icu:80/announce`

