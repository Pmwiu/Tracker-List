# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-06 11:06:08 UTC
- 总 Tracker 数: 365
- 存活 (alive): **288** (78%)
- 失效 (dead): **77**
- 不安全 (unsafe): **0**
- 无法测试 (untestable): 0
- 低速淘汰 (low-speed >5s): 1
- 同 IP 去重 (kept faster): 153
- 综合评分后保留前 20 个，淘汰 114 个
- 耗时: 35.1 秒

## 协议分布

- udp: 146
- http: 102
- https: 34
- wss: 6

## 最终订阅列表（前 20 个，按综合评分降序）

1. `udp://explodie.org:6969/announce` — score=70.0, 3ms, 连续0天
2. `udp://exodus.desync.com:6969/announce` — score=70.0, 4ms, 连续0天
3. `http://207.241.226.111:6969/announce` — score=70.0, 6ms, 连续0天
4. `wss://tracker.openwebtorrent.com:443/announce` — score=70.0, 8ms, 连续0天
5. `udp://23.94.174.203:1337/announce` — score=70.0, 8ms, 连续0天
6. `http://207.241.231.226:6969/announce` — score=70.0, 8ms, 连续0天
7. `udp://180.131.145.175:6969/announce` — score=70.0, 15ms, 连续0天
8. `udp://51.81.222.188:6969/announce` — score=70.0, 15ms, 连续0天
9. `https://t.213891.xyz:443/announce` — score=70.0, 17ms, 连续0天
10. `udp://tracker.gmi.gd:6969/announce` — score=70.0, 17ms, 连续0天
11. `https://4.tracker.eu.org:443/announce` — score=70.0, 19ms, 连续0天
12. `https://1.tracker.eu.org:443/announce` — score=70.0, 19ms, 连续0天
13. `http://t-backup.213891.xyz:80/announce` — score=70.0, 22ms, 连续0天
14. `udp://149.106.106.25:443/announce` — score=70.0, 28ms, 连续0天
15. `http://tracker.gcvchp.com:2710/announce` — score=70.0, 30ms, 连续0天
16. `http://tracker.waaa.moe:6969/announce` — score=70.0, 31ms, 连续0天
17. `http://www.arabp2p.net:2052/f5a1e35785c9f3885fd54f34b6e262b8/announce` — score=70.0, 31ms, 连续0天
18. `http://004430.xyz:80/announce` — score=70.0, 37ms, 连续0天
19. `https://tracker.nekomi.cn:443/announce` — score=70.0, 41ms, 连续0天
20. `udp://tracker.wildkat.net:6969/announce` — score=70.0, 44ms, 连续0天

## 失效 Tracker

- `http://177.188.141.75:6969/announce` — URLError: <urlopen error timed out>
- `http://34.66.57.33:11450/announce` — timeout
- `http://34.66.57.33:1337/announce` — timeout
- `http://51.79.71.167:80/announce` — URLError: <urlopen error timed out>
- `http://[2605:6400:30:fad6::dead:c0d3]:1337/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://[2a04:ac00:1:3dd8::1:2710]:2710/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://btracker.top:11451/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://retracker.hotplug.ru:2710/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://tk.greedland.net:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://torrentsmd.com:8080/announce` — HTTPError: HTTP Error 403: Forbidden
- `http://tracker.dump.cl:6969/announce` — timeout
- `http://tracker.electro-torrent.pl:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.gbitt.info:80/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `http://tracker.opentorrent.top:6969/announce` — URLError: <urlopen error timed out>
- `http://tracker.plx.im:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://tracker.therarbg.to:6969/announce` — URLError: <urlopen error timed out>
- `http://tracker.xiaoduola.xyz:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://tracker.xn--djrq4gl4hvoi.top:80/announce` — timeout
- `http://tracker2.itzmx.com:6961/announce` — URLError: <urlopen error timed out>
- `http://tracker3.ctix.cn:8080/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker3.itzmx.com:6961/announce` — URLError: <urlopen error timed out>
- `http://tracker4.itzmx.com:2710/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://tracker810.xyz:11450/announce` — timeout
- `http://trackme.theom.nz:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://www.all4nothin.net:80/announce.php` — URLError: <urlopen error timed out>
- `http://www.genesis-sp.org:2710/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://tp.m-team.cc:443/announce.php` — HTTPError: HTTP Error 403: Forbidden
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [Errno 104] Connection reset by peer>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.gbitt.info:443/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.lilithraws.cf:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.loligirl.cn:443/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `https://tracker.m-team.cc:443/announce.php` — HTTPError: HTTP Error 403: Forbidden
- `https://tracker.maya.no.eu.org:443/announce` — HTTPError: HTTP Error 429: Too Many Requests
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tracker.tamersunion.org:443/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `https://tracker1.520.jp:443/announce` — HTTPError: HTTP Error 521: <none>
- `https://trackme.theom.nz:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `udp://159.146.99.45:6969/announce` — no connect response
- `udp://177.188.141.75:6969/announce` — no connect response
- `udp://178.239.19.29:80/announce` — no connect response
- `udp://208.83.20.20:6969/announce` — no connect response
- `udp://209.141.59.16:6969/announce` — no connect response
- `udp://221.153.216.56:8081/announce` — no connect response
- `udp://37.120.182.83:15480/announce` — no connect response
- `udp://38.180.157.12:2715/announce` — no connect response
- `udp://52.58.128.163:6969/announce` — no connect response
- `udp://91.177.126.188:6969/announce` — no connect response
- `udp://93.158.213.92:6969/announce` — no connect response
- `udp://[2a03:7220:8083:cd00::1]:451/announce` — no connect response
- `udp://[2a04:ac00:1:3dd8::1:2710]:2710/announce` — no connect response
- `udp://anime-tracker.aruku.kro.kr:8081/announce` — no connect response
- `udp://ipv6.govt.hu:6969/announce` — no connect response
- `udp://open.stealth.si/announce` — missing port
- `udp://open.tracker.ink:6969/announce` — no connect response
- `udp://opentor.org:2710/announce` — no connect response
- `udp://opentrackr.org:1337/announce` — no connect response
- `udp://p4p.arenabg.com:1337/announce` — no connect response
- `udp://rekcart.duckdns.org:15480/announce` — no connect response
- `udp://retracker.hotplug.ru:2710/announce` — no connect response
- `udp://seedpeer.net:6969/announce` — no connect response
- `udp://tr3.ysagin.top:2715/announce` — no connect response
- `udp://tracker.flatuslifir.is:6969/announce` — no connect response
- `udp://tracker.skyts.net:6969/announce` — no connect response
- `udp://tracker.sylphix.com:6969/announce` — no connect response
- `udp://tracker.teambelgium.net:6969/announce` — no connect response
- `udp://tracker.theoks.net:6969/announce` — no connect response
- `udp://tracker.torrents.observer:80/announce` — no connect response
- `udp://tracker.yume-hatsuyuki.moe:6969/announce` — no connect response
- `udp://tracker1.itzmx.com:8080/announce` — no connect response
- `udp://tracker2.itzmx.com:6961/announce` — no connect response
- `udp://tracker3.itzmx.com:6961/announce` — no connect response
- `udp://tracker4.itzmx.com:2710/announce` — no connect response
- `wss://qot.abiir.top/announce` — SSLEOFError: [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)

## 低速 Tracker（>5s，已排除）

- `https://pybittrack.retiolus.net:443/announce` — 10473ms

## 同 IP 去重（保留响应最快）

- `http://107.189.2.131:1337/announce`
- `http://1337.abcvg.info:80/announce`
- `http://135.125.198.235:2710/announce`
- `http://135.125.198.235:80/announce`
- `http://140.235.237.23:6969/announce`
- `http://152.249.214.196:6969/announce`
- `http://211.75.205.187:6969/announce`
- `http://211.75.205.187:80/announce`
- `http://211.75.205.188:6969/announce`
- `http://211.75.205.188:80/announce`
- `http://211.75.210.221:6969/announce`
- `http://211.75.210.221:80/announce`
- `http://216.144.239.90:6969/announce`
- `http://31.38.161.123:6969/announce`
- `http://43.250.54.126:6969/announce`
- `http://79.111.12.213:6969/announce`
- `http://93.158.213.92:1337/announce`
- `http://94.23.207.177:6969/announce`
- `http://announce.sktorrent.eu:6969/announce`
- `http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce`
- `http://bittorrent.kali.org:80/announce`
- `http://bt02.nnm-club.cc:2710/announce`
- `http://bt1.archive.org:6969/announce`
- `http://bt2.archive.org:6969/announce`
- `http://bttracker.debian.org:6969/announce`
- `http://ch3oh.ru:6969/announce`
- `http://ehtracker.org:80/1104308/announce`
- `http://ehtracker.org:80/1113709/announce`
- `http://ehtracker.org:80/1226599/1080494xo5eXcwFOBq/announce`
- `http://ehtracker.org:80/2496841/announce`
- `http://ehtracker.org:80/2541477/announce`
- `http://ehtracker.org:80/2566145/1159106xUfsJkT9Btg/announce`
- `http://ipv4announce.sktorrent.eu:6969/announce`
- `http://open.demonii.si:80/announce`
- `http://open.tracker.cl:1337/announce`
- `http://opentracker.xyz:80/announce`
- `http://opentrackr.org:1337/announce`
- `http://retracker.x2k.ru:80/announce`
- `http://retracker01-msk-virt.corbina.net:80/announce`
- `http://t.overflow.biz:6969/announce`
- `http://torrent.ubuntu.com:6969/announce`
- `http://tracker-udp.anirena.com:80/announce`
- `http://tracker-zhuqiy.dgj055.icu:80/announce`
- `http://tracker.004430.xyz:1337/announce`
- `http://tracker.ali213.net:8000/announce`
- `http://tracker.auctor.tv:6969/announce`
- `http://tracker.breizh.pm:6969/announce`
- `http://tracker.coppersurfer.site:2710/announce`
- `http://tracker.ddunlimited.net:6969/announce`
- `http://tracker.dler.com:6969/announce`
- `http://tracker.dler.org:6969/announce`
- `http://tracker.dm258.cn:7070/announce`
- `http://tracker.internetwarriors.net:1337/announce`
- `http://tracker.k.vu:6969/announce`
- `http://tracker.kali.org:6969/announce`
- `http://tracker.mywaifu.best:6969/announce`
- `http://tracker.novaopcj.eu.org:6969/announce`
- `http://tracker.nyaa.vc:6969/announce`
- `http://tracker.opentrackr.org:1337/announce`
- `http://tracker.privateseedbox.xyz:2710/announce`
- `http://tracker.qu.ax:6969/announce`
- `http://tracker.xfapi.top:6868/announce`
- `http://tracker.xfapi.top:7070/announce`
- `http://tracker2.dler.com:80/announce`
- `http://tracker2.dler.org:80/announce`
- `http://tracker3.dler.org:2710/announce`
- `https://004430.xyz:443/announce`
- `https://2.tracker.eu.org:443/announce`
- `https://3.tracker.eu.org:443/announce`
- `https://337hhh.xyz:443/announce`
- `https://5.tracker.eu.org:443/announce`
- `https://bt.beatrice-raws.org:443/announce`
- `https://open.ftorrent.com:443/announce`
- `https://t.btcland.xyz:443/announce`
- `https://tr-rh-zhuqiy.dgj055.icu:443/announce`
- `https://tr-zhuqiy-1.dgj055.icu:443/announce`
- `https://tr-zhuqiy-2.dgj055.icu:443/announce`
- `https://tr.nyacat.pw:443/announce`
- `https://tr.torland.ga:443/announce`
- `https://tracker-zhuqiy.dgj055.icu:443/announce`
- `udp://135.125.198.235:1984/announce`
- `udp://135.125.236.64:6969/announce`
- `udp://151.242.104.187:80/announce`
- `udp://152.249.214.196:6969/announce`
- `udp://164.152.110.70:6969/announce`
- `udp://185.216.179.62:25/announce`
- `udp://209.141.59.25:6969/announce`
- `udp://211.75.205.187:6969/announce`
- `udp://211.75.205.188:6969/announce`
- `udp://211.75.205.188:80/announce`
- `udp://211.75.210.221:6969/announce`
- `udp://212.42.38.197:6969/announce`
- `udp://23.157.120.14:6969/announce`
- `udp://31.59.141.120:6969/announce`
- `udp://34.66.57.33:80/announce`
- `udp://45.137.199.107:6969/announce`
- `udp://45.38.170.167:6969/announce`
- `udp://52.211.139.85:27022/announce`
- `udp://65.109.28.17:6969/announce`
- `udp://65.109.28.33:6969/announce`
- `udp://74.119.149.136:6969/announce`
- `udp://83.102.180.21:80/announce`
- `udp://89.234.156.205:451/announce`
- `udp://91.216.110.53:451/announce`
- `udp://93.158.213.92:1337/announce`
- `udp://94.23.207.177:6969/announce`
- `udp://95.217.80.22:6969/announce`
- `udp://admin.52ywp.com:6969/announce`
- `udp://atrack.pow7.com:6969/announce`
- `udp://kolankoalastree.newtrackon.co.nz:1337/announce`
- `udp://leet-tracker.moe:1337/announce`
- `udp://leet-tracker.moe:23861/announce`
- `udp://leet-tracker.moe:38151/announce`
- `udp://mail.segso.net:6969/announce`
- `udp://ns575949.ip-51-222-82.net:6969/announce`
- `udp://open.demonii.com:1337/announce`
- `udp://open.ftorrent.com:443/announce`
- `udp://qg.lorzl.gq:2710/announce`
- `udp://secure.pow7.com:6969/announce`
- `udp://torrent.tracker.durukanbal.com:6969/announce`
- `udp://tr4ck3r.duckdns.org:6969/announce`
- `udp://tracker-udp.gbitt.info:80/announce`
- `udp://tracker.004430.xyz:1337/announce`
- `udp://tracker.aruku.ovh:8081/announce`
- `udp://tracker.auctor.tv:6969/announce`
- `udp://tracker.bittor.pw:1337/announce`
- `udp://tracker.btzoo.eu:80/announce`
- `udp://tracker.cn.nyaa.net:6969/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.ddunlimited.net:6969/announce`
- `udp://tracker.dler.com:6969/announce`
- `udp://tracker.ducks.party:1984/announce`
- `udp://tracker.farted.net:6969/announce`
- `udp://tracker.fatkhoala.org:13710/announce`
- `udp://tracker.fatkhoala.org:13790/announce`
- `udp://tracker.fnix.net:6969/announce`
- `udp://tracker.ilibr.org:80/announce`
- `udp://tracker.leechers-paradise.org:6969/announce`
- `udp://tracker.novaopcj.eu.org:6969/announce`
- `udp://tracker.opentrackr.com:1337/announce`
- `udp://tracker.opentrackr.com:6969/announce`
- `udp://tracker.peerfect.org:6969/announce`
- `udp://tracker.qu.ax:6969/announce`
- `udp://tracker.sbsub.com:2710/announce`
- `udp://tracker.sigterm.xyz:6969/announce`
- `udp://tracker.skynetcloud.site:6969/announce`
- `udp://tracker.tallpenguin.org:15750/announce`
- `udp://tracker.uw0.xyz:6969/announce`
- `udp://tracker2.dler.com:80/announce`
- `udp://tracker2.dler.org:80/announce`
- `udp://v2.iperson.xyz:6969/announce`
- `udp://zer0day.ch:1337/announce`
- `wss://tracker.openwebtorrent.com/announce`
