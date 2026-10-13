# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-13 10:37:33 UTC
- 总 Tracker 数: 320
- 存活 (alive): **115** (35%)
- 失效 (dead): **182**
- 不安全 (unsafe): **6**
- 无法测试 (untestable): 17
- 低速淘汰 (low-speed >5s): 1
- 同网段/同域名去重 (kept fastest): 65
- 综合评分后保留前 25 个，淘汰 24 个
- 评分维度: 速度 50% + 历史稳定性 20% + 响应质量 15%（含 peers 计数与 scrape 热度） + 跨源一致性 10% + 近期成功率 5%（速度标度自适应 + 经典高可用加分 + 反退化）
- 配额: 保底 4 条非 UDP + 保底 4 条经典高可用
- 协议多样性配额: 保底 4 条非 UDP，实际保留 8 条
- 耗时: 94.8 秒

## 协议分布

- udp: 60
- http: 41
- https: 14

## 最终订阅列表（前 25 个，按综合评分降序）

1. `https://t.213891.xyz:443/announce` — score=97.2, 25ms, 存活率100%, 质量90, 经典+0
2. `http://tracker.dhitechnical.com:6969/announce` — score=92.1, 142ms, 存活率100%, 质量95, 经典+0
3. `udp://open.ftorrent.com:443/announce` — score=91.1, 50ms, 存活率98%, 质量60, 经典+0
4. `https://tracker.nekomi.cn:443/announce` — score=90.3, 178ms, 存活率100%, 质量95, 经典+0
5. `udp://tracker.qu.ax:6969/announce` — score=89.8, 84ms, 存活率100%, 质量60, 经典+0
6. `http://207.241.231.226:6969/announce` — score=89.7, 139ms, 存活率100%, 质量98, 经典+0
7. `http://207.241.226.111:6969/announce` — score=89.7, 140ms, 存活率100%, 质量98, 经典+0
8. `udp://evan.im:6969/announce` — score=89.4, 23ms, 存活率98%, 质量60, 经典+0
9. `udp://tracker.ducks.party:1984/announce` — score=89.3, 94ms, 存活率100%, 质量60, 经典+0
10. `udp://martin-gebhardt.eu:25/announce` — score=88.8, 95ms, 存活率98%, 质量60, 经典+0
11. `udp://opentracker.lain.moscow:6969/announce` — score=88.4, 103ms, 存活率98%, 质量60, 经典+0
12. `udp://tracker.peerfect.org:6969/announce` — score=87.7, 117ms, 存活率98%, 质量60, 经典+0
13. `https://3.tracker.eu.org:443/announce` — score=87.1, 26ms, 存活率100%, 质量90, 经典+0
14. `udp://t.overflow.biz:6969/announce` — score=86.0, 126ms, 存活率92%, 质量60, 经典+0
15. `udp://34.66.57.33:1337/announce` — score=85.1, 32ms, 存活率99%, 质量60, 经典+0
16. `http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce` — score=85.0, 218ms, 存活率98%, 质量95, 经典+0
17. `udp://193.148.251.93:6969/announce` — score=84.5, 41ms, 存活率98%, 质量60, 经典+0
18. `udp://tracker.dler.org:6969/announce` — score=84.2, 196ms, 存活率100%, 质量60, 经典+0
19. `https://4.tracker.eu.org:443/announce` — score=83.8, 28ms, 存活率83%, 质量90, 经典+0
20. `udp://tracker.004430.xyz:1337/announce` — score=83.0, 80ms, 存活率100%, 质量60, 经典+0
21. `udp://51.81.222.188:6969/announce` — score=82.7, 68ms, 存活率96%, 质量60, 经典+0
22. `udp://109.201.134.183:80/announce` — score=82.7, 86ms, 存活率100%, 质量60, 经典+0
23. `udp://45.137.199.107:6969/announce` — score=82.5, 81ms, 存活率98%, 质量60, 经典+0
24. `udp://51.15.41.46:6969/announce` — score=82.2, 86ms, 存活率98%, 质量60, 经典+0
25. `udp://ipv4announce.sktorrent.eu:6969/announce` — score=82.2, 87ms, 存活率98%, 质量60, 经典+0

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
- `http://185.148.3.231:80/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://185.185.40.51:6969/announce` — URLError: <urlopen error timed out>
- `http://185.185.40.95:6969/announce` — URLError: <urlopen error timed out>
- `http://34.66.57.33:1337/announce` — timeout
- `http://34.66.57.33:2701/announce` — timeout
- `http://34.66.57.33:443/announce` — timeout
- `http://504e163a.host.njalla.net:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://66691337.xyz:6969/announce` — URLError: <urlopen error timed out>
- `http://79.111.12.213:6969/announce` — restricted (failure reason)
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
- `http://h4.trakx.nibba.trade:80/announce` — timeout
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
- `http://retracker.joxnet.ru:80/announce` — HTTPError: HTTP Error 500: Internal Server Error
- `http://retracker.krs-ix.ru:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://retracker.ohys.net:80/announce` — URLError: <urlopen error timed out>
- `http://retracker.x2k.ru:80/announce` — restricted (failure reason)
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
- `http://torrenteditor.com:80` — invalid bencoded response
- `http://torrenttracker.nwc.acsalaska.net:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `https://ht.therarbg.to:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>
- `https://tracker.midnightprogrammer.net:443/announce` — HTTPError: HTTP Error 502: Bad Gateway
- `https://tracker.zhuqiy.com:443/announce` — timeout
- `udp://52.58.128.163:6969/announce` — no connect response
- `udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce` — no connect response
- `udp://exodus.desync.com:6969/announce` — no connect response
- `udp://open.tracker.ink:6969/announce` — no connect response
- `udp://opentor.org:2710/announce` — no connect response
- `udp://p4p.arenabg.com:1337/announce` — no connect response
- `udp://retracker.hotplug.ru:2710/announce` — no connect response
- `udp://tracker.srv00.com:6969/announce` — no connect response
- `udp://tracker.theoks.net:6969/announce` — no connect response
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

- `http://216.144.239.90:6969/announce` — 5064ms

## 同网段/同域名去重（保留响应最快）

- `http://004430.xyz:80/announce`
- `http://107.189.2.131:1337/announce`
- `http://1337.abcvg.info:80/announce`
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
- `http://open.tracker.cl:1337/announce`
- `http://opentracker.xyz:80/announce`
- `http://retracker01-msk-virt.corbina.net:80/announce`
- `http://t.nyaatracker.com:80/announce`
- `http://t.overflow.biz:6969/announce`
- `http://tracker.auctor.tv:6969/announce`
- `http://tracker.dler.com:6969/announce`
- `http://tracker.dler.org:6969/announce`
- `http://tracker.mywaifu.best:6969/announce`
- `http://tracker.nyaa.vc:6969/announce`
- `http://tracker.opentrackr.org:1337/announce`
- `http://tracker.qu.ax:6969/announce`
- `http://tracker.renfei.net:8080/announce`
- `http://tracker2.dler.org:80/announce`
- `https://004430.xyz:443/announce`
- `https://1.tracker.eu.org:443/announce`
- `https://2.tracker.eu.org:443/announce`
- `https://337hhh.xyz:443/announce`
- `https://5.tracker.eu.org:443/announce`
- `https://open.ftorrent.com:443/announce`
- `https://retracker.x2k.ru:443/announce`
- `https://tr.nyacat.pw:443/announce`
- `https://tracker.7471.top:443/announce`
- `https://tracker.foreverpirates.co:443/announce`
- `udp://135.125.198.235:1984/announce`
- `udp://211.75.205.187:6969/announce`
- `udp://34.66.57.33:80/announce`
- `udp://43.250.54.126:6969/announce`
- `udp://65.109.28.17:6969/announce`
- `udp://65.109.28.33:6969/announce`
- `udp://93.158.213.92:6969/announce`
- `udp://95.217.80.22:6969/announce`
- `udp://explodie.org:6969/announce`
- `udp://mail.segso.net:6969/announce`
- `udp://open.demonii.com:1337/announce`
- `udp://open.stealth.si:80/announce`
- `udp://retracker01-msk-virt.corbina.net:80/announce`
- `udp://tracker-udp.gbitt.info:80/announce`
- `udp://tracker.bittor.pw:1337/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.farted.net:6969/announce`
- `udp://tracker.gmi.gd:6969/announce`
- `udp://tracker.nyaa.vc:6969/announce`
- `udp://tracker.opentrackr.org:1337/announce`
- `udp://tracker.skynetcloud.site:6969/announce`
- `udp://tracker.torrent.eu.org:451/announce`
- `udp://tracker2.dler.org:80/announce`

## Discovery（自动发现的候选，Phase 1 隔离，不进 best/all）

- 候选总数: 164
- 通过探活: 9
- 若允许参与排名会入选的（前 3 条）:
  - `udp://tracker.aruku.ovh:8081/announce`
  - `udp://23.157.120.14:6969/announce`
  - `udp://211.75.205.187:80/announce`

转正方式：人工 review 后加入 `scripts/update_trackers.py` 的 SOURCES，或写进 `trackers/discovered/PROMOTE.md`（Phase 2）。


## 备选库（trackers_reserve.txt，前 9 条，按评分降序）

独立于 best/all 的候选订阅源，供人工审查转正。
1. `https://open.ftorrent.com:443/announce`
2. `udp://tracker.aruku.ovh:8081/announce`
3. `udp://23.157.120.14:6969/announce`
4. `udp://211.75.205.187:80/announce`
5. `udp://211.75.205.187:6969/announce`
6. `http://t.nyaatracker.com:80/announce`
7. `http://t.overflow.biz:6969/announce`
8. `http://open.tracker.cl:1337/announce`
9. `http://opentracker.xyz:80/announce`

