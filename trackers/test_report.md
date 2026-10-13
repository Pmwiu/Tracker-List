# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-13 06:53:38 UTC
- 总 Tracker 数: 320
- 存活 (alive): **106** (33%)
- 失效 (dead): **189**
- 不安全 (unsafe): **4**
- 无法测试 (untestable): 21
- 低速淘汰 (low-speed >5s): 0
- 同网段/同域名去重 (kept fastest): 55
- 综合评分后保留前 25 个，淘汰 26 个
- 评分维度: 速度 50% + 历史稳定性 20% + 响应质量 15%（含 peers 计数与 scrape 热度） + 跨源一致性 10% + 近期成功率 5%（速度标度自适应 + 经典高可用加分 + 反退化）
- 配额: 保底 4 条非 UDP + 保底 4 条经典高可用
- 协议多样性配额: 保底 4 条非 UDP，实际保留 10 条
- 耗时: 99.2 秒

## 协议分布

- udp: 57
- http: 38
- https: 11

## 最终订阅列表（前 25 个，按综合评分降序）

1. `udp://explodie.org:6969/announce` — score=97.2, 37ms, 存活率95%, 质量60, 经典+6
2. `http://207.241.226.111:6969/announce` — score=94.9, 35ms, 存活率100%, 质量98, 经典+0
3. `http://207.241.231.226:6969/announce` — score=94.8, 35ms, 存活率100%, 质量98, 经典+0
4. `udp://tracker.opentrackr.org:1337/announce` — score=93.6, 128ms, 存活率100%, 质量60, 经典+6
5. `udp://open.stealth.si:80/announce` — score=93.0, 138ms, 存活率100%, 质量60, 经典+6
6. `udp://open.demonii.com:1337/announce` — score=92.9, 130ms, 存活率97%, 质量60, 经典+6
7. `udp://open.ftorrent.com:443/announce` — score=91.1, 35ms, 存活率95%, 质量60, 经典+0
8. `udp://tracker.gmi.gd:6969/announce` — score=90.9, 28ms, 存活率92%, 质量60, 经典+0
9. `http://tracker.renfei.net:8080/announce` — score=90.2, 181ms, 存活率100%, 质量95, 经典+0
10. `https://tracker.nekomi.cn:443/announce` — score=89.6, 192ms, 存活率100%, 质量95, 经典+0
11. `http://tracker.dhitechnical.com:6969/announce` — score=88.2, 219ms, 存活率100%, 质量95, 经典+0
12. `udp://tracker.qu.ax:6969/announce` — score=87.5, 129ms, 存活率100%, 质量60, 经典+0
13. `udp://evan.im:6969/announce` — score=87.5, 49ms, 存活率95%, 质量60, 经典+0
14. `https://t.213891.xyz:443/announce` — score=87.3, 223ms, 存活率100%, 质量90, 经典+0
15. `udp://tracker-udp.gbitt.info:80/announce` — score=87.3, 133ms, 存活率100%, 质量60, 经典+0
16. `udp://tracker.dler.org:6969/announce` — score=87.0, 140ms, 存活率100%, 质量60, 经典+0
17. `http://004430.xyz:80/announce` — score=87.0, 43ms, 存活率100%, 质量95, 经典+0
18. `http://216.144.239.90:6969/announce` — score=86.9, 24ms, 存活率95%, 质量95, 经典+0
19. `udp://tracker.ducks.party:1984/announce` — score=86.8, 144ms, 存活率100%, 质量60, 经典+0
20. `udp://tracker.004430.xyz:1337/announce` — score=86.6, 9ms, 存活率100%, 质量60, 经典+0
21. `https://2.tracker.eu.org:443/announce` — score=86.3, 40ms, 存活率99%, 质量90, 经典+0
22. `udp://martin-gebhardt.eu:25/announce` — score=85.9, 139ms, 存活率95%, 质量60, 经典+0
23. `udp://opentracker.lain.moscow:6969/announce` — score=85.7, 143ms, 存活率95%, 质量60, 经典+0
24. `udp://tracker.farted.net:6969/announce` — score=85.3, 157ms, 存活率96%, 质量60, 经典+0
25. `http://tracker.dler.com:6969/announce` — score=85.0, 284ms, 存活率100%, 质量95, 经典+0

## 失效 Tracker

- `http://00.mercax.com:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://00.xxtor.com:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://0205.uptm.ch:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://0d.kebhana.mx:443/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
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
- `http://34.66.57.33:1337/announce` — timeout
- `http://34.66.57.33:2701/announce` — timeout
- `http://34.66.57.33:443/announce` — URLError: <urlopen error timed out>
- `http://504e163a.host.njalla.net:6969/announce` — URLError: <urlopen error [Errno -3] Temporary failure in name resolution>
- `http://60-fps.org:80/bt/announce.php` — HTTPError: HTTP Error 410: Gone
- `http://60-fps.org:80/bt:80/announce.php` — HTTPError: HTTP Error 410: Gone
- `http://66691337.xyz:6969/announce` — URLError: <urlopen error timed out>
- `http://79.111.12.213:6969/announce` — restricted (failure reason)
- `http://aaa.army:8866/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://aboutbeautifulgallopinghorsesinthegreenpasture.online:80/announce` — HTTPError: HTTP Error 404: Not Found
- `http://all4nothin.net:80/announce.php` — URLError: <urlopen error timed out>
- `http://alltorrents.net:80/bt/announce.php` — restricted (failure reason)
- `http://alltorrents.net:80/bt:80/announce.php` — HTTPError: HTTP Error 404: Not Found
- `http://anidex.moe:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://anisource.spb.ru:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://announce.partis.si:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://asiatorrent.ddns.net:51413/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `http://asiatorrent.giize.com:51413/announce` — URLError: <urlopen error timed out>
- `http://atrack.pow7.com:80/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://baibako.tv:80/announce` — URLError: <urlopen error timed out>
- `http://big-boss-tracker.net:80/announce.php` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bigfoot1942.sektori.org:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bithq.org:80/announce.php` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bittorrent.kali.org:80/announce` — restricted (failure reason)
- `http://blackz.ro:80/announce.php` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bluebird-hd.org:80/announce.php` — HTTPError: HTTP Error 404: Not Found
- `http://bobbialbano.com:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://bt-club.ws:80/announce` — URLError: <urlopen error [Errno -3] Temporary failure in name resolution>
- `http://bt-tracker.gamexp.ru:2710/announce` — URLError: <urlopen error timed out>
- `http://bt.3kb.xyz:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bt.ali213.net:8000/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://bt.ali213.net:8080/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://bt.beatrice-raws.org:80/announce` — restricted (failure reason)
- `http://bt.dl1234.com:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bt.edwardk.info:12891/announce` — restricted (failure reason)
- `http://bt.edwardk.info:2710/announce` — restricted (failure reason)
- `http://bt.edwardk.info:4040/announce` — restricted (failure reason)
- `http://bt.edwardk.info:63124/announce` — restricted (failure reason)
- `http://bt.edwardk.info:676/announce` — restricted (failure reason)
- `http://bt.edwardk.info:6767/announce` — restricted (failure reason)
- `http://bt.edwardk.info:6969/announce` — restricted (failure reason)
- `http://bt.endpot.com:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bt.henbt.com:2710/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bt.ktkj.com:8080/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bt.nnm-club.info:2710/announce` — restricted (failure reason)
- `http://bt.okmp3.ru:2710/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bt.poletracker.org:2710/announce` — timeout
- `http://bt.publicvm.com:8080/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bt.pusacg.org:8080/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `http://bt.rghost.net:80/announce` — timeout
- `http://bt.xcty.eu.org:2095/announce` — timeout
- `http://bt.zlofenix.org:81/announce` — restricted (failure reason)
- `http://bt02.nnm-club.cc:2710/announce` — restricted (failure reason)
- `http://bt02.nnm-club.info:2710/announce` — restricted (failure reason)
- `http://bt1.letpo.com:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bt1.xxxxbt.cc:6969/announce` — timeout
- `http://bt2.careland.com.cn:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bt2.edwardk.info:2710/announce` — restricted (failure reason)
- `http://bt2.edwardk.info:4040/announce` — restricted (failure reason)
- `http://bt2.edwardk.info:6969/announce` — restricted (failure reason)
- `http://btracker.top:11451/announce` — ConnectionResetError: [Errno 104] Connection reset by peer
- `http://bttracker.debian.org:6969/announce` — restricted (failure reason)
- `http://btx.anifilm.tv:80/announce.php` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bughome.de:2832/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://buny.uk:6969/announce` — timeout
- `http://bvarf.tracker.sh:2086/announce` — timeout
- `http://bz.tracker.bz:80/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://canardscitrons.nohost.me:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://carbon-bonsai-621.appspot.com:80/announce` — HTTPError: HTTP Error 404: Not Found
- `http://ch3oh.ru:6969/announce` — restricted (failure reason)
- `http://chihaya.de:80/announce` — URLError: <urlopen error timed out>
- `http://chouchou.top:8080/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://cloud.nyap2p.com:8080/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://cn.pcfreetime.com:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://concen.org:6969/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `http://data-bg.net:80/announce.php` — URLError: <urlopen error timed out>
- `http://datascene.net:80/announce.php` — timeout
- `http://de7c0e7a567e.sn.mynetname.net:59002/announce` — URLError: <urlopen error timed out>
- `http://debuz.com:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://dht.dhtclub.com:666/announce` — URLError: <urlopen error timed out>
- `http://dn42.smrsh.net:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://echostar.ddnsfree.com:8080/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://ehtracker.org:80/1/announce` — restricted (failure reason)
- `http://ehtracker.org:80/1104308/announce` — restricted (failure reason)
- `http://ehtracker.org:80/1113709/announce` — restricted (failure reason)
- `http://ehtracker.org:80/1226599/1080494xo5eXcwFOBq/announce` — restricted (failure reason)
- `http://ehtracker.org:80/2496841/announce` — restricted (failure reason)
- `http://ehtracker.org:80/2541477/announce` — restricted (failure reason)
- `http://ehtracker.org:80/2566145/1159106xUfsJkT9Btg/announce` — restricted (failure reason)
- `http://explodie.org:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://fe.dealclub.de:6969/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `http://finbytes.org:80/announce.php` — ConnectionResetError: [Errno 104] Connection reset by peer
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
- `http://highteahop.top:6960/announce` — ConnectionResetError: [Errno 104] Connection reset by peer
- `http://home.kray.pw:6969/announce` — URLError: <urlopen error timed out>
- `http://home.yxgz.club:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://houniao.ddns.net:8888/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `http://hzzwly.gq:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://i.bandito.org:80/announce.php` — HTTPError: HTTP Error 429: Too Many Requests
- `http://incine.ru:6969/announce` — URLError: <urlopen error timed out>
- `http://ipv4.rer.lol:2710/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `http://ipv6.rer.lol:6969/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `http://irrenhaus.dyndns.dk:80/announce.php` — empty response
- `http://joczo.duckdns.org:6969/announce` — URLError: <urlopen error timed out>
- `http://jp.moeweb.pw:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://jvavav.com:80/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://kamikazee.duckdns.org:7777/announce` — HTTPError: HTTP Error 404: Not Found
- `http://kinorun.com:80/announce.php` — HTTPError: HTTP Error 404: Not Found
- `http://kiryuu-test.mywaifu.best:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://li1406-230.members.linode.com:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://li2021-95.members.linode.com:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://lima-peru.subventas.com:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://lucke.fenesisu.moe:6969/announce` — URLError: <urlopen error timed out>
- `http://mail.lakameraobscura.com:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://masters-tb.com:80/announce.php` — timeout
- `http://mediaclub.tv:80/announce` — invalid bencoded response
- `http://mediaclub.tv:80/announce.php` — invalid bencoded response
- `http://mgtracker.org:2710/announce` — URLError: <urlopen error timed out>
- `http://mgtracker.org:6969/announce` — URLError: <urlopen error timed out>
- `http://retracker.hotplug.ru:2710/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
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
- `udp://tracker.theoks.net:6969/announce` — no connect response
- `udp://tracker.torrent.eu.org:451/announce` — no connect response
- `udp://tracker.wepzone.net:6969/announce` — no connect response
- `udp://tracker1.itzmx.com:8080/announce` — no connect response
- `udp://tracker1.myporn.club:9337/announce` — no connect response
- `udp://wepzone.net:6969/announce` — no connect response
- `wss://tracker.openwebtorrent.com:443/announce` — SSLError: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1010)

## 不安全 Tracker（已过滤）

- `http://alpha.torrenttracker.nl:443/announce` — resolves to private IP: ::1
- `http://ipv4.tracker.harry.lu:80/announce` — resolves to private IP: 127.0.0.1
- `http://yggtracker.i2p.rocks:80/announce` — resolves to private IP: 200:1e2f:e608:eb3a:2bf:1e62:87ba:e2f7
- `udp://open.dstud.io:6969/announce` — resolves to private IP: 0.0.0.0

## 无法测试（特殊网络）

- `http://[2605:6400:30:fad6::dead:c0d3]:1337/announce` — IPv6 unavailable here
- `http://[2a04:ac00:1:3dd8::1:2710]:2710/announce` — IPv6 unavailable here
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
- `udp://[2a03:7220:8083:cd00::1]:451/announce` — IPv6 unavailable here
- `udp://[2a04:ac00:1:3dd8::1:2710]:2710/announce` — IPv6 unavailable here
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
- `http://bt1.archive.org:6969/announce`
- `http://bt2.archive.org:6969/announce`
- `http://ipv4announce.sktorrent.eu:6969/announce`
- `http://retracker01-msk-virt.corbina.net:80/announce`
- `http://tracker.auctor.tv:6969/announce`
- `http://tracker.dler.org:6969/announce`
- `http://tracker.mywaifu.best:6969/announce`
- `http://tracker.nyaa.vc:6969/announce`
- `http://tracker.opentrackr.org:1337/announce`
- `http://tracker.qu.ax:6969/announce`
- `http://tracker.waaa.moe:6969/announce`
- `http://tracker2.dler.org:80/announce`
- `https://004430.xyz:443/announce`
- `https://1.tracker.eu.org:443/announce`
- `https://3.tracker.eu.org:443/announce`
- `https://337hhh.xyz:443/announce`
- `udp://109.201.134.183:80/announce`
- `udp://135.125.198.235:1984/announce`
- `udp://151.242.104.187:80/announce`
- `udp://185.121.168.96:1337/announce`
- `udp://209.141.59.25:6969/announce`
- `udp://211.75.205.187:6969/announce`
- `udp://211.75.205.187:80/announce`
- `udp://23.157.120.14:6969/announce`
- `udp://31.56.179.159:6969/announce`
- `udp://34.66.57.33:80/announce`
- `udp://43.250.54.126:6969/announce`
- `udp://65.109.28.17:6969/announce`
- `udp://65.109.28.33:6969/announce`
- `udp://93.158.213.92:1337/announce`
- `udp://93.158.213.92:6969/announce`
- `udp://95.217.80.22:6969/announce`
- `udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce`
- `udp://mail.segso.net:6969/announce`
- `udp://retracker01-msk-virt.corbina.net:80/announce`
- `udp://tracker.bittor.pw:1337/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.nyaa.vc:6969/announce`
- `udp://tracker.skynetcloud.site:6969/announce`
- `udp://tracker2.dler.org:80/announce`

## Discovery（自动发现的候选，Phase 1 隔离，不进 best/all）

- 候选总数: 152
- 通过探活: 2

转正方式：人工 review 后加入 `scripts/update_trackers.py` 的 SOURCES，或写进 `trackers/discovered/PROMOTE.md`（Phase 2）。

