# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-13 09:59:50 UTC
- 总 Tracker 数: 320
- 存活 (alive): **110** (34%)
- 失效 (dead): **186**
- 不安全 (unsafe): **7**
- 无法测试 (untestable): 17
- 低速淘汰 (low-speed >5s): 2
- 同网段/同域名去重 (kept fastest): 56
- 综合评分后保留前 25 个，淘汰 27 个
- 评分维度: 速度 50% + 历史稳定性 20% + 响应质量 15%（含 peers 计数与 scrape 热度） + 跨源一致性 10% + 近期成功率 5%（速度标度自适应 + 经典高可用加分 + 反退化）
- 配额: 保底 4 条非 UDP + 保底 4 条经典高可用
- 协议多样性配额: 保底 4 条非 UDP，实际保留 7 条
- 耗时: 94.0 秒

## 协议分布

- udp: 58
- http: 41
- https: 11

## 最终订阅列表（前 25 个，按综合评分降序）

1. `https://t.213891.xyz:443/announce` — score=95.7, 57ms, 存活率100%, 质量90, 经典+0
2. `udp://open.stealth.si:80/announce` — score=93.8, 123ms, 存活率100%, 质量60, 经典+6
3. `http://tracker.renfei.net:8080/announce` — score=93.7, 111ms, 存活率100%, 质量95, 经典+0
4. `https://1.tracker.eu.org:443/announce` — score=93.2, 46ms, 存活率100%, 质量90, 经典+0
5. `udp://tracker.corpscorp.online:80/announce` — score=93.0, 19ms, 存活率100%, 质量60, 经典+0
6. `udp://open.ftorrent.com:443/announce` — score=92.5, 18ms, 存活率97%, 质量60, 经典+0
7. `http://207.241.231.226:6969/announce` — score=92.0, 93ms, 存活率100%, 质量98, 经典+0
8. `http://tracker.dhitechnical.com:6969/announce` — score=91.8, 149ms, 存活率100%, 质量95, 经典+0
9. `udp://exodus.desync.com:6969/announce` — score=91.2, 53ms, 存活率74%, 质量60, 经典+6
10. `https://tracker.nekomi.cn:443/announce` — score=90.8, 168ms, 存活率100%, 质量95, 经典+0
11. `udp://open.demonii.com:1337/announce` — score=90.5, 182ms, 存活率98%, 质量60, 经典+6
12. `udp://evan.im:6969/announce` — score=89.0, 29ms, 存活率97%, 质量60, 经典+0
13. `udp://tracker-udp.gbitt.info:80/announce` — score=88.5, 111ms, 存活率100%, 质量60, 经典+0
14. `udp://tracker.nyaa.vc:6969/announce` — score=88.4, 111ms, 存活率100%, 质量60, 经典+0
15. `udp://tracker.qu.ax:6969/announce` — score=88.3, 113ms, 存活率100%, 质量60, 经典+0
16. `udp://martin-gebhardt.eu:25/announce` — score=87.3, 122ms, 存活率97%, 质量60, 经典+0
17. `udp://opentracker.lain.moscow:6969/announce` — score=87.2, 124ms, 存活率97%, 质量60, 经典+0
18. `udp://retracker01-msk-virt.corbina.net:80/announce` — score=86.3, 153ms, 存活率100%, 质量60, 经典+0
19. `udp://tracker2.dler.org:80/announce` — score=85.7, 166ms, 存活率100%, 质量60, 经典+0
20. `udp://tracker.dler.org:6969/announce` — score=85.6, 168ms, 存活率100%, 质量60, 经典+0
21. `udp://193.148.251.93:6969/announce` — score=85.4, 21ms, 存活率97%, 质量60, 经典+0
22. `udp://tracker.004430.xyz:1337/announce` — score=85.0, 40ms, 存活率100%, 质量60, 经典+0
23. `udp://89.234.156.205:451/announce` — score=84.6, 117ms, 存活率97%, 质量60, 经典+0
24. `udp://t.overflow.biz:6969/announce` — score=84.5, 149ms, 存活率90%, 质量60, 经典+0
25. `https://3.tracker.eu.org:443/announce` — score=83.8, 91ms, 存活率99%, 质量90, 经典+0

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
- `http://34.66.57.33:1337/announce` — timeout
- `http://34.66.57.33:2701/announce` — timeout
- `http://34.66.57.33:443/announce` — timeout
- `http://504e163a.host.njalla.net:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://66691337.xyz:6969/announce` — URLError: <urlopen error timed out>
- `http://79.111.12.213:6969/announce` — timeout
- `http://aaa.army:8866/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://aboutbeautifulgallopinghorsesinthegreenpasture.online:80/announce` — HTTPError: HTTP Error 404: Not Found
- `http://anisource.spb.ru:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://asiatorrent.ddns.net:51413/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `http://asiatorrent.giize.com:51413/announce` — URLError: <urlopen error timed out>
- `http://bigfoot1942.sektori.org:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bittorrent.kali.org:80/announce` — restricted (failure reason)
- `http://bobbialbano.com:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://bt.3kb.xyz:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bt.dl1234.com:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bt.endpot.com:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bt.henbt.com:2710/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bt.ktkj.com:8080/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bt.publicvm.com:8080/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bt.pusacg.org:8080/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `http://bt.rghost.net:80/announce` — timeout
- `http://bt.xcty.eu.org:2095/announce` — timeout
- `http://bt1.letpo.com:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bt2.careland.com.cn:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bughome.de:2832/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://bvarf.tracker.sh:2086/announce` — timeout
- `http://canardscitrons.nohost.me:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://chihaya.de:80/announce` — URLError: <urlopen error timed out>
- `http://chouchou.top:8080/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://cloud.nyap2p.com:8080/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://cn.pcfreetime.com:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://de7c0e7a567e.sn.mynetname.net:59002/announce` — URLError: <urlopen error timed out>
- `http://debuz.com:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://dht.dhtclub.com:666/announce` — URLError: <urlopen error timed out>
- `http://dn42.smrsh.net:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://echostar.ddnsfree.com:8080/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://ehtracker.org:80/1104308/announce` — restricted (failure reason)
- `http://ehtracker.org:80/1113709/announce` — restricted (failure reason)
- `http://ehtracker.org:80/1226599/1080494xo5eXcwFOBq/announce` — restricted (failure reason)
- `http://ehtracker.org:80/2496841/announce` — restricted (failure reason)
- `http://ehtracker.org:80/2541477/announce` — restricted (failure reason)
- `http://ehtracker.org:80/2566145/1159106xUfsJkT9Btg/announce` — restricted (failure reason)
- `http://explodie.org:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://fe.dealclub.de:6969/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `http://fleira.no:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://fosstorrents.com:6969/announce` — URLError: <urlopen error timed out>
- `http://frp.v2fy.com:8000/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://ftp.pet:2710/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://ftp.pet:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://ftp.pet:7777/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://ftp.pet:999/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://fxtt.ru:80/announce` — URLError: <urlopen error timed out>
- `http://grifon.info:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://h4.trakx.nibba.trade:80/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://highteahop.top:6960/announce` — RemoteDisconnected: Remote end closed connection without response
- `http://home.kray.pw:6969/announce` — URLError: <urlopen error timed out>
- `http://houniao.ddns.net:8888/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `http://hzzwly.gq:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://i.bandito.org:80/announce.php` — HTTPError: HTTP Error 403: Forbidden
- `http://incine.ru:6969/announce` — URLError: <urlopen error timed out>
- `http://ipv6.rer.lol:6969/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `http://joczo.duckdns.org:6969/announce` — URLError: <urlopen error timed out>
- `http://jp.moeweb.pw:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://kamikazee.duckdns.org:7777/announce` — HTTPError: HTTP Error 404: Not Found
- `http://kiryuu-test.mywaifu.best:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://li1406-230.members.linode.com:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://li2021-95.members.linode.com:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://lima-peru.subventas.com:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://lucke.fenesisu.moe:6969/announce` — URLError: <urlopen error timed out>
- `http://mail.lakameraobscura.com:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://mgtracker.org:2710/announce` — URLError: <urlopen error timed out>
- `http://mgtracker.org:6969/announce` — URLError: <urlopen error timed out>
- `http://mkfs.ru:80/announce` — invalid bencoded response
- `http://montreal.nyap2p.com:8080/announce` — timeout
- `http://movies.zsw.ca:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://ns3109441.mypdns.org:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://open.8a.is:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://open.acgnxtracker.com:80/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `http://open.acgtracker.com:1096/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://open.miotracker.com:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://open.nyap2p.com:8080/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://open.tracker.ink:6969/announce` — URLError: <urlopen error timed out>
- `http://opentracker.91kf.top:16969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://opentracker.i2p.rocks:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://opentracker.io:80/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `http://p4p.arenabg.ch:1337/announce` — URLError: <urlopen error timed out>
- `http://p4p.arenabg.com:1337/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://parag.rs:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://peersteers.org:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://play.aimisayo.com:6969/announce` — URLError: <urlopen error timed out>
- `http://region.nl1.privex.cc:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://reisub.nsupdate.info:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://retracker.gorcomnet.ru:80/announce` — invalid bencoded response
- `http://retracker.hotplug.ru:2710/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://retracker.joxnet.ru:80/announce` — URLError: <urlopen error timed out>
- `http://retracker.krs-ix.ru:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://retracker.ohys.net:80/announce` — URLError: <urlopen error timed out>
- `http://rfc5746.mywaifu.best:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://rotracker.ohys.net:80/announce` — URLError: <urlopen error timed out>
- `http://rstracker.ohys.net:80/announce` — URLError: <urlopen error timed out>
- `http://s1124554.ha012.t.mydomain.zone:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://s1130638.ha016.t.mydomain.zone:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://s1130639.ha009.t.mydomain.zone:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://s1130642.ha014.t.mydomain.zone:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://s926723.ha016.t.mydomain.zone:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://servandroidkino.ru:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://shogiroom.com:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://siambit.org:80/announce.php` — HTTPError: HTTP Error 404: Not Found
- `http://siwserver.duckdns.org:9900/announce` — URLError: <urlopen error timed out>
- `http://smurfsoft.com:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://speedtest.iperson.xyz:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://t.al.uy:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://t.jaekr.sh:6969/announce` — ConnectionResetError: [Errno 104] Connection reset by peer
- `http://t.publictracker.xyz:6969/announce` — URLError: <urlopen error timed out>
- `http://t1.chfs.ch:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://taciturn-shadow.spb.ru:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://thetracker.org:80/announce` — HTTPError: HTTP Error 403: Forbidden
- `http://thitgaluoc.dynu.net:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://tk.greedland.net:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tk2.greedland.net:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://torrent-tracker.ru:80/announce.php` — URLError: <urlopen error [Errno -3] Temporary failure in name resolution>
- `http://torrent.gresille.org:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://torrent.nwps.ws:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://ht.therarbg.to:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.bt4g.com:443/announce` — timeout
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.midnightprogrammer.net:443/announce` — HTTPError: HTTP Error 502: Bad Gateway
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tracker.zhuqiy.com:443/announce` — timeout
- `udp://208.83.20.20:6969/announce` — no connect response
- `udp://6ahddutb1ucc3cp.ru:6969/announce` — no connect response
- `udp://explodie.org:6969/announce` — no connect response
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

- `http://alpha.torrenttracker.nl:443/announce` — resolves to private IP: ::1
- `http://ipv4.tracker.harry.lu:80/announce` — resolves to private IP: 127.0.0.1
- `http://milanesitracker.tekcities.com:80/announce` — resolves to private IP: 127.6.7.8
- `http://prestige.minimafia.nl:443/announce` — resolves to private IP: ::1
- `http://private.minimafia.nl:443/announce` — resolves to private IP: ::1
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

- `http://tracker.waaa.moe:6969/announce` — 6411ms
- `http://216.144.239.90:6969/announce` — 6911ms

## 同网段/同域名去重（保留响应最快）

- `http://107.189.2.131:1337/announce`
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
- `http://ipv4announce.sktorrent.eu:6969/announce`
- `http://open.demonii.si:80/announce`
- `http://open.tracker.cl:1337/announce`
- `http://opentracker.xyz:80/announce`
- `http://retracker01-msk-virt.corbina.net:80/announce`
- `http://t.overflow.biz:6969/announce`
- `http://tracker.auctor.tv:6969/announce`
- `http://tracker.dler.com:6969/announce`
- `http://tracker.dler.org:6969/announce`
- `http://tracker.mywaifu.best:6969/announce`
- `http://tracker.nyaa.vc:6969/announce`
- `http://tracker.opentrackr.org:1337/announce`
- `http://tracker.qu.ax:6969/announce`
- `http://tracker2.dler.org:80/announce`
- `https://004430.xyz:443/announce`
- `https://2.tracker.eu.org:443/announce`
- `https://337hhh.xyz:443/announce`
- `https://4.tracker.eu.org:443/announce`
- `udp://109.201.134.183:80/announce`
- `udp://151.242.104.187:80/announce`
- `udp://185.121.168.96:1337/announce`
- `udp://211.75.205.188:80/announce`
- `udp://34.66.57.33:1337/announce`
- `udp://34.66.57.33:80/announce`
- `udp://43.250.54.126:6969/announce`
- `udp://45.137.199.107:6969/announce`
- `udp://65.109.28.17:6969/announce`
- `udp://65.109.28.33:6969/announce`
- `udp://83.102.180.21:80/announce`
- `udp://93.158.213.92:1337/announce`
- `udp://95.217.80.22:6969/announce`
- `udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce`
- `udp://tracker.bittor.pw:1337/announce`
- `udp://tracker.ducks.party:1984/announce`
- `udp://tracker.farted.net:6969/announce`
- `udp://tracker.filemail.com:6969/announce`
- `udp://tracker.gmi.gd:6969/announce`
- `udp://tracker.opentrackr.org:1337/announce`
- `udp://tracker.peerfect.org:6969/announce`
- `udp://tracker.skynetcloud.site:6969/announce`
- `udp://tracker.torrent.eu.org:451/announce`

## Discovery（自动发现的候选，Phase 1 隔离，不进 best/all）

- 候选总数: 158
- 通过探活: 7
- 若允许参与排名会入选的（前 3 条）:
  - `udp://tr4ck3r.duckdns.org:6969/announce`
  - `udp://tracker.cn.nyaa.net:6969/announce`
  - `http://t.nyaatracker.com:80/announce`

转正方式：人工 review 后加入 `scripts/update_trackers.py` 的 SOURCES，或写进 `trackers/discovered/PROMOTE.md`（Phase 2）。


## 备选库（trackers_reserve.txt，前 7 条，按评分降序）

独立于 best/all 的候选订阅源，供人工审查转正。
1. `udp://tr4ck3r.duckdns.org:6969/announce`
2. `udp://tracker.cn.nyaa.net:6969/announce`
3. `udp://211.75.205.188:80/announce`
4. `http://t.nyaatracker.com:80/announce`
5. `http://t.overflow.biz:6969/announce`
6. `http://open.tracker.cl:1337/announce`
7. `http://opentracker.xyz:80/announce`

