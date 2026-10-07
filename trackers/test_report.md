# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-07 01:31:02 UTC
- 总 Tracker 数: 376
- 存活 (alive): **281** (74%)
- 失效 (dead): **92**
- 不安全 (unsafe): **3**
- 无法测试 (untestable): 0
- 低速淘汰 (low-speed >5s): 18
- 同 IP 去重 (kept faster): 140
- 综合评分后保留前 20 个，淘汰 103 个
- 耗时: 33.0 秒

## 协议分布

- udp: 137
- http: 109
- https: 30
- wss: 5

## 最终订阅列表（前 20 个，按综合评分降序）

1. `udp://51.81.222.188:6969/announce` — score=70.3, 206ms, 连续2天
2. `udp://120.78.150.131:6969/announce` — score=70.0, 29ms, 连续0天
3. `udp://admin.52ywp.com:6969/announce` — score=70.0, 31ms, 连续0天
4. `udp://118.196.100.63:6969/announce` — score=70.0, 34ms, 连续0天
5. `udp://47.76.201.250:6969/announce` — score=70.0, 39ms, 连续0天
6. `udp://43.154.112.29:17272/announce` — score=70.0, 43ms, 连续0天
7. `udp://211.75.205.187:80/announce` — score=70.0, 58ms, 连续0天
8. `udp://211.75.210.221:6969/announce` — score=70.0, 61ms, 连续0天
9. `udp://211.75.205.188:6969/announce` — score=70.0, 63ms, 连续0天
10. `udp://132.226.6.145:6969/announce` — score=70.0, 88ms, 连续0天
11. `http://tracker.ali213.net:8000/announce` — score=70.0, 88ms, 连续0天
12. `udp://149.106.106.25:443/announce` — score=69.9, 211ms, 连续2天
13. `udp://yuptracker-sa.gaijinent.com:27022/announce` — score=68.3, 122ms, 连续0天
14. `udp://tracker.willy.pro:6969/announce` — score=66.6, 144ms, 连续0天
15. `udp://leet-tracker.moe:38151/announce` — score=65.2, 217ms, 连续1天
16. `udp://192.3.130.53:1337/announce` — score=63.7, 236ms, 连续1天
17. `udp://tracker.004430.xyz:1337/announce` — score=61.5, 210ms, 连续0天
18. `udp://185.216.179.62:25/announce` — score=61.2, 213ms, 连续0天
19. `udp://74.119.149.136:6969/announce` — score=61.0, 271ms, 连续1天
20. `udp://tracker.sigterm.xyz:6969/announce` — score=60.3, 225ms, 连续0天

## 失效 Tracker

- `http://004430.xyz:80/announce` — invalid bencoded response
- `http://123.245.62.62:6969/announce` — URLError: <urlopen error timed out>
- `http://123.245.62.74:6969/announce` — URLError: <urlopen error timed out>
- `http://177.188.141.75:6969/announce` — URLError: <urlopen error timed out>
- `http://51.79.71.167:80/announce` — URLError: <urlopen error timed out>
- `http://[2605:6400:30:fad6::dead:c0d3]:1337/announce` — URLError: <urlopen error timed out>
- `http://asiatorrent.giize.com:51413/announce` — URLError: <urlopen error timed out>
- `http://bt1.archive.org:6969/announce` — URLError: <urlopen error timed out>
- `http://buny.uk:6969/announce` — timeout
- `http://open.demonii.si:80/announce` — URLError: <urlopen error timed out>
- `http://opentracker.acgnx.se:80/announce` — URLError: <urlopen error timed out>
- `http://share.hkg-fansub.info:80/announce` — timeout
- `http://t-backup.213891.xyz:80/announce` — ConnectionResetError: [WinError 10054] 远程主机强迫关闭了一个现有的连接。
- `http://tk.greedland.net:80/announce` — URLError: <urlopen error [Errno 11001] getaddrinfo failed>
- `http://torrentsmd.com:8080/announce` — URLError: <urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>
- `http://tracker-udp.anirena.com:80/announce` — URLError: <urlopen error timed out>
- `http://tracker.004430.xyz:1337/announce` — URLError: <urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>
- `http://tracker.acgnx.se:80/announce` — URLError: <urlopen error timed out>
- `http://tracker.electro-torrent.pl:80/announce` — URLError: <urlopen error [Errno 11001] getaddrinfo failed>
- `http://tracker.fansub.id:80/announce` — invalid bencoded response
- `http://tracker.gbitt.info:80/announce` — URLError: <urlopen error [Errno 11001] getaddrinfo failed>
- `http://tracker.k.vu:6969/announce` — URLError: <urlopen error timed out>
- `http://tracker.minglong.org:8080/announce` — URLError: <urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>
- `http://tracker.moxing.party:6969/announce` — URLError: <urlopen error timed out>
- `http://tracker.nucozer-tracker.ml:2710/announce` — timeout
- `http://tracker.opentorrent.top:6969/announce` — URLError: <urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>
- `http://tracker.plx.im:6969/announce` — URLError: <urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>
- `http://tracker.therarbg.to:6969/announce` — URLError: <urlopen error timed out>
- `http://tracker3.ctix.cn:8080/announce` — URLError: <urlopen error [Errno 11001] getaddrinfo failed>
- `http://trackme.theom.nz:80/announce` — URLError: <urlopen error [Errno 11001] getaddrinfo failed>
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://004430.xyz:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for '004430.xyz'. (_ssl.c:1010)>
- `https://pybittrack.retiolus.net:443/announce` — timeout
- `https://t.btcland.xyz:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 't.btcland.xyz'. (_ssl.c:1010)>
- `https://tr-rh-zhuqiy.dgj055.icu:443/announce` — URLError: <urlopen error timed out>
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate (_ssl.c:1010)>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.gbitt.info:443/announce` — URLError: <urlopen error [Errno 11001] getaddrinfo failed>
- `https://tracker.kuroy.me:443/announce` — HTTPError: HTTP Error 503: Service Unavailable
- `https://tracker.lilithraws.cf:443/announce` — URLError: <urlopen error [Errno 11001] getaddrinfo failed>
- `https://tracker.loligirl.cn:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tracker.loligirl.cn'. (_ssl.c:1010)>
- `https://tracker.m-team.cc:443/announce.php` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tracker.m-team.cc'. (_ssl.c:1010)>
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tracker.tamersunion.org:443/announce` — URLError: <urlopen error [Errno 11001] getaddrinfo failed>
- `https://tracker1.520.jp:443/announce` — HTTPError: HTTP Error 521: <none>
- `https://trackme.theom.nz:443/announce` — URLError: <urlopen error [Errno 11001] getaddrinfo failed>
- `udp://135.125.236.64:6969/announce` — no connect response
- `udp://15.235.207.99:8081/announce` — no connect response
- `udp://173.201.36.219:6969/announce` — no connect response
- `udp://177.188.141.75:6969/announce` — no connect response
- `udp://209.141.59.25:6969/announce` — no connect response
- `udp://212.42.38.197:6969/announce` — no connect response
- `udp://221.153.216.56:8081/announce` — no connect response
- `udp://23.94.174.203:1337/announce` — no connect response
- `udp://37.120.182.83:15480/announce` — no connect response
- `udp://38.180.157.12:2715/announce` — no connect response
- `udp://45.38.170.167:6969/announce` — no connect response
- `udp://52.58.128.163:6969/announce` — no connect response
- `udp://91.177.126.188:6969/announce` — no connect response
- `udp://95.217.80.22:6969/announce` — no connect response
- `udp://anime-tracker.aruku.kro.kr:8081/announce` — no connect response
- `udp://archive.torrentonline.cc:42069/announce` — no connect response
- `udp://bttracker.debian.org:6969/announce` — no connect response
- `udp://explodie.org:6969/announce` — no connect response
- `udp://ipv6.govt.hu:6969/announce` — no connect response
- `udp://open.stealth.si/announce` — missing port
- `udp://open.tracker.ink:6969/announce` — no connect response
- `udp://opentor.org:2710/announce` — no connect response
- `udp://p4p.arenabg.com:1337/announce` — no connect response
- `udp://rekcart.duckdns.org:15480/announce` — no connect response
- `udp://retracker.hotplug.ru:2710/announce` — no connect response
- `udp://santost12.xyz:6969/announce` — no connect response
- `udp://torrent.tracker.durukanbal.com:6969/announce` — no connect response
- `udp://tr3.ysagin.top:2715/announce` — no connect response
- `udp://tracker-udp.anirena.com:80/announce` — no connect response
- `udp://tracker.aruku.ovh:8081/announce` — no connect response
- `udp://tracker.breizh.pm:6969/announce` — no connect response
- `udp://tracker.dhitechnical.com:6969/announce` — no connect response
- `udp://tracker.flatuslifir.is:6969/announce` — no connect response
- `udp://tracker.k.vu:6969/announce` — no connect response
- `udp://tracker.skyts.net:6969/announce` — no connect response
- `udp://tracker.sylphix.com:6969/announce` — no connect response
- `udp://tracker.tallpenguin.org:15750/announce` — no connect response
- `udp://tracker.teambelgium.net:6969/announce` — no connect response
- `udp://tracker.theoks.net:6969/announce` — no connect response
- `udp://tracker.tryhackx.org:6969/announce` — no connect response
- `udp://tracker.yume-hatsuyuki.moe:6969/announce` — no connect response
- `udp://tracker1.itzmx.com:8080/announce` — no connect response
- `udp://v2.iperson.xyz:6969/announce` — no connect response
- `wss://qot.abiir.top/announce` — SSLEOFError: [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)
- `wss://spacetradersapi-chatbox.herokuapp.com/announce` — timeout

## 不安全 Tracker（已过滤）

- `http://bt2.archive.org:6969/announce` — resolves to private IP: 2001::80f2:f5d4
- `http://tracker.pussytorrents.org:3000/announce` — resolves to private IP: 2001::80f2:f5d4
- `https://tp.m-team.cc:443/announce.php` — resolves to private IP: 2001::c73b:95ef

## 低速 Tracker（>5s，已排除）

- `http://tracker.dm258.cn:7070/announce` — 5475ms
- `wss://tracker.openwebtorrent.com:443/announce` — 6355ms
- `wss://tracker.openwebtorrent.com/announce` — 6432ms
- `http://tracker.bittor.pw:1337/announce` — 6499ms
- `http://bt.edwardk.info:63124/announce` — 6714ms
- `http://bt.edwardk.info:6767/announce` — 6716ms
- `http://bt2.edwardk.info:2710/announce` — 6718ms
- `https://tracker.foreverpirates.co:443/announce` — 6729ms
- `http://bt2.edwardk.info:4040/announce` — 6737ms
- `http://bt2.edwardk.info:6969/announce` — 6740ms
- `http://bt.edwardk.info:6969/announce` — 6764ms
- `http://bt.edwardk.info:676/announce` — 6778ms
- `http://bt.edwardk.info:12891/announce` — 6785ms
- `http://bt.edwardk.info:4040/announce` — 6785ms
- `http://bt.edwardk.info:2710/announce` — 6796ms
- `http://tracker.waaa.moe:6969/announce` — 6893ms
- `http://216.144.239.90:6969/announce` — 7211ms
- `https://tracker.moviesdb.top:443/announce` — 7614ms

## 同 IP 去重（保留响应最快）

- `http://107.189.2.131:1337/announce`
- `http://135.125.198.235:2710/announce`
- `http://135.125.198.235:80/announce`
- `http://138.186.10.167:1337/announce`
- `http://140.235.237.23:6969/announce`
- `http://152.249.214.196:6969/announce`
- `http://185.126.65.92:6969/announce`
- `http://211.75.205.187:6969/announce`
- `http://211.75.205.187:80/announce`
- `http://211.75.205.188:6969/announce`
- `http://211.75.205.188:80/announce`
- `http://211.75.210.221:6969/announce`
- `http://211.75.210.221:80/announce`
- `http://31.38.161.123:6969/announce`
- `http://43.250.54.126:6969/announce`
- `http://79.111.12.213:6969/announce`
- `http://93.158.213.92:1337/announce`
- `http://94.23.207.177:6969/announce`
- `http://[2a04:ac00:1:3dd8::1:2710]:2710/announce`
- `http://announce.sktorrent.eu:6969/announce`
- `http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce`
- `http://bittorrent.kali.org:80/announce`
- `http://bt.nnm-club.info:2710/announce`
- `http://ch3oh.ru:6969/announce`
- `http://ehtracker.org:80/1/announce`
- `http://ehtracker.org:80/1113709/announce`
- `http://ehtracker.org:80/1226599/1080494xo5eXcwFOBq/announce`
- `http://ehtracker.org:80/2496841/announce`
- `http://ehtracker.org:80/2541477/announce`
- `http://ehtracker.org:80/2566145/1159106xUfsJkT9Btg/announce`
- `http://ipv4announce.sktorrent.eu:6969/announce`
- `http://open.tracker.cl:1337/announce`
- `http://opentracker.xyz:80/announce`
- `http://opentrackr.org:1337/announce`
- `http://retracker.hotplug.ru:2710/announce`
- `http://retracker.x2k.ru:80/announce`
- `http://retracker01-msk-virt.corbina.net:80/announce`
- `http://t.overflow.biz:6969/announce`
- `http://torrent.ubuntu.com:6969/announce`
- `http://tracker.ali213.net:8080/announce`
- `http://tracker.auctor.tv:6969/announce`
- `http://tracker.coppersurfer.site:2710/announce`
- `http://tracker.ddunlimited.net:6969/announce`
- `http://tracker.dler.com:6969/announce`
- `http://tracker.dler.org:6969/announce`
- `http://tracker.kali.org:6969/announce`
- `http://tracker.novaopcj.eu.org:6969/announce`
- `http://tracker.nyaa.vc:6969/announce`
- `http://tracker.opentrackr.org:1337/announce`
- `http://tracker.qu.ax:6969/announce`
- `http://tracker.torrents.observer:80/announce`
- `http://tracker.xfapi.top:7070/announce`
- `http://tracker.xfapi.top:9999/announce`
- `http://tracker.zhuqiy.dgj055.icu:80/announce`
- `http://tracker2.dler.com:80/announce`
- `http://tracker2.dler.org:80/announce`
- `http://tracker2.itzmx.com:6961/announce`
- `http://tracker3.dler.org:2710/announce`
- `http://tracker3.itzmx.com:6961/announce`
- `http://tracker4.itzmx.com:2710/announce`
- `https://1.tracker.eu.org:443/announce`
- `https://1337.abcvg.info:443/announce`
- `https://337hhh.xyz:443/announce`
- `https://4.tracker.eu.org:443/announce`
- `https://5.tracker.eu.org:443/announce`
- `https://bt.beatrice-raws.org:443/announce`
- `https://open.ftorrent.com:443/announce`
- `https://retracker.x2k.ru:443/announce`
- `https://tr-zhuqiy-1.dgj055.icu:443/announce`
- `https://tr-zhuqiy-2.dgj055.icu:443/announce`
- `https://tr.nyacat.pw:443/announce`
- `https://tr.torland.ga:443/announce`
- `https://tracker-zhuqiy.dgj055.icu:443/announce`
- `https://tracker.zhuqiy.com:443/announce`
- `udp://135.125.198.235:1984/announce`
- `udp://152.249.214.196:6969/announce`
- `udp://160.30.240.158:1337/announce`
- `udp://164.152.110.70:6969/announce`
- `udp://193.187.90.12:6969/announce`
- `udp://208.83.20.20:6969/announce`
- `udp://211.75.205.187:6969/announce`
- `udp://211.75.205.188:80/announce`
- `udp://211.75.210.221:80/announce`
- `udp://31.56.179.159:6969/announce`
- `udp://34.66.57.33:1337/announce`
- `udp://34.66.57.33:80/announce`
- `udp://43.250.54.126:6969/announce`
- `udp://51.222.82.36:6969/announce`
- `udp://60.172.236.18:6969/announce`
- `udp://65.109.28.17:6969/announce`
- `udp://89.234.156.205:451/announce`
- `udp://93.158.213.92:1337/announce`
- `udp://93.158.213.92:6969/announce`
- `udp://chihaya.toss.li:9696/announce`
- `udp://evan.im:6969/announce`
- `udp://exodus.desync.com:6969/announce`
- `udp://ipv4announce.sktorrent.eu:6969/announce`
- `udp://leet-tracker.moe:1337/announce`
- `udp://leet-tracker.moe:23861/announce`
- `udp://mail.segso.net:6969/announce`
- `udp://martin-gebhardt.eu:25/announce`
- `udp://open.demonii.com:1337/announce`
- `udp://open.ftorrent.com:443/announce`
- `udp://open.stealth.si:80/announce`
- `udp://opentrackr.org:1337/announce`
- `udp://peerfect.org:6969/announce`
- `udp://qg.lorzl.gq:2710/announce`
- `udp://retracker01-msk-virt.corbina.net:80/announce`
- `udp://secure.pow7.com:6969/announce`
- `udp://seedpeer.net:6969/announce`
- `udp://tr4ck3r.duckdns.org:6969/announce`
- `udp://tracker-udp.gbitt.info:80/announce`
- `udp://tracker.auctor.tv:6969/announce`
- `udp://tracker.bittor.pw:1337/announce`
- `udp://tracker.btzoo.eu:80/announce`
- `udp://tracker.cn.nyaa.net:6969/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.dler.com:6969/announce`
- `udp://tracker.dler.org:6969/announce`
- `udp://tracker.ducks.party:1984/announce`
- `udp://tracker.fatkhoala.org:13710/announce`
- `udp://tracker.fatkhoala.org:13790/announce`
- `udp://tracker.ilibr.org:6969/announce`
- `udp://tracker.leechers-paradise.org:6969/announce`
- `udp://tracker.novaopcj.eu.org:6969/announce`
- `udp://tracker.nyaa.net:6969/announce`
- `udp://tracker.nyaa.vc:6969/announce`
- `udp://tracker.opentrackr.com:1337/announce`
- `udp://tracker.opentrackr.com:6969/announce`
- `udp://tracker.opentrackr.org:1337/announce`
- `udp://tracker.qu.ax:6969/announce`
- `udp://tracker.sbsub.com:2710/announce`
- `udp://tracker.segso.net:6969/announce`
- `udp://tracker.torrents.observer:80/announce`
- `udp://tracker.uw0.xyz:6969/announce`
- `udp://tracker2.dler.com:80/announce`
- `udp://tracker2.dler.org:80/announce`
- `udp://tracker3.itzmx.com:6961/announce`
- `udp://www.torrent.eu.org:451/announce`
- `udp://yuptracker-eu.gaijinent.com:27022/announce`
