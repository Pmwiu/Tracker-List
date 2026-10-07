# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-07 01:32:03 UTC
- 总 Tracker 数: 376
- 存活 (alive): **301** (80%)
- 失效 (dead): **71**
- 不安全 (unsafe): **0**
- 无法测试 (untestable): 4
- 低速淘汰 (low-speed >5s): 2
- 同 IP 去重 (kept faster): 167
- 综合评分后保留前 20 个，淘汰 112 个
- 耗时: 34.0 秒

## 协议分布

- udp: 146
- http: 116
- https: 33
- wss: 6

## 最终订阅列表（前 20 个，按综合评分降序）

1. `udp://51.81.222.188:6969/announce` — score=82.9, 15ms, 连续3天
2. `udp://149.106.106.25:443/announce` — score=82.9, 28ms, 连续3天
3. `udp://192.3.130.53:1337/announce` — score=78.6, 46ms, 连续2天
4. `udp://74.119.149.136:6969/announce` — score=78.6, 64ms, 连续2天
5. `udp://132.226.6.145:6969/announce` — score=73.9, 105ms, 连续1天
6. `udp://211.75.210.221:6969/announce` — score=71.4, 137ms, 连续1天
7. `udp://43.154.112.29:17272/announce` — score=70.7, 146ms, 连续1天
8. `udp://185.216.179.62:25/announce` — score=70.3, 151ms, 连续1天
9. `udp://23.157.120.14:6969/announce` — score=70.0, 2ms, 连续0天
10. `udp://t2.pow7.com:6969/announce` — score=70.0, 4ms, 连续0天
11. `http://207.241.226.111:6969/announce` — score=70.0, 6ms, 连续0天
12. `wss://tracker.openwebtorrent.com/announce` — score=70.0, 7ms, 连续0天
13. `udp://23.94.174.203:1337/announce` — score=70.0, 8ms, 连续0天
14. `http://207.241.231.226:6969/announce` — score=70.0, 8ms, 连续0天
15. `udp://180.131.145.175:6969/announce` — score=70.0, 17ms, 连续0天
16. `https://2.tracker.eu.org:443/announce` — score=70.0, 17ms, 连续0天
17. `udp://209.141.59.25:6969/announce` — score=70.0, 18ms, 连续0天
18. `https://t.213891.xyz:443/announce` — score=70.0, 20ms, 连续0天
19. `https://5.tracker.eu.org:443/announce` — score=70.0, 22ms, 连续0天
20. `udp://tracker.theoks.net:6969/announce` — score=70.0, 22ms, 连续0天

## 失效 Tracker

- `http://123.245.62.74:6969/announce` — timeout
- `http://177.188.141.75:6969/announce` — URLError: <urlopen error timed out>
- `http://51.79.71.167:80/announce` — URLError: <urlopen error timed out>
- `http://asiatorrent.giize.com:51413/announce` — URLError: <urlopen error timed out>
- `http://buny.uk:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://retracker.hotplug.ru:2710/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://share.hkg-fansub.info:80/announce` — timeout
- `http://tk.greedland.net:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://torrentsmd.com:8080/announce` — HTTPError: HTTP Error 403: Forbidden
- `http://tracker.bittor.pw:1337/announce` — timeout
- `http://tracker.electro-torrent.pl:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker.gbitt.info:80/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `http://tracker.moxing.party:6969/announce` — timeout
- `http://tracker.nucozer-tracker.ml:2710/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://tracker.opentorrent.top:6969/announce` — URLError: <urlopen error timed out>
- `http://tracker.plx.im:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://tracker.therarbg.to:6969/announce` — URLError: <urlopen error timed out>
- `http://tracker2.itzmx.com:6961/announce` — URLError: <urlopen error timed out>
- `http://tracker3.ctix.cn:8080/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://tracker3.itzmx.com:6961/announce` — URLError: <urlopen error timed out>
- `http://tracker4.itzmx.com:2710/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://trackme.theom.nz:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://www.all4nothin.net:80/announce.php` — URLError: <urlopen error timed out>
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://pybittrack.retiolus.net:443/announce` — timeout
- `https://tp.m-team.cc:443/announce.php` — HTTPError: HTTP Error 403: Forbidden
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.gbitt.info:443/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.lilithraws.cf:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.loligirl.cn:443/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `https://tracker.m-team.cc:443/announce.php` — HTTPError: HTTP Error 403: Forbidden
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tracker.tamersunion.org:443/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `https://tracker1.520.jp:443/announce` — HTTPError: HTTP Error 521: <none>
- `https://trackme.theom.nz:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `udp://135.125.236.64:6969/announce` — no connect response
- `udp://177.188.141.75:6969/announce` — no connect response
- `udp://221.153.216.56:8081/announce` — no connect response
- `udp://37.120.182.83:15480/announce` — no connect response
- `udp://38.180.157.12:2715/announce` — no connect response
- `udp://91.177.126.188:6969/announce` — no connect response
- `udp://91.216.110.53:451/announce` — no connect response
- `udp://anime-tracker.aruku.kro.kr:8081/announce` — no connect response
- `udp://archive.torrentonline.cc:42069/announce` — no connect response
- `udp://exodus.desync.com:6969/announce` — no connect response
- `udp://ipv6.govt.hu:6969/announce` — no connect response
- `udp://open.stealth.si/announce` — missing port
- `udp://open.tracker.ink:6969/announce` — no connect response
- `udp://opentor.org:2710/announce` — no connect response
- `udp://p4p.arenabg.com:1337/announce` — no connect response
- `udp://rekcart.duckdns.org:15480/announce` — no connect response
- `udp://retracker.hotplug.ru:2710/announce` — no connect response
- `udp://secure.pow7.com:6969/announce` — no connect response
- `udp://tr3.ysagin.top:2715/announce` — no connect response
- `udp://tracker.breizh.pm:6969/announce` — no connect response
- `udp://tracker.fnix.net:6969/announce` — no connect response
- `udp://tracker.sbsub.com:2710/announce` — no connect response
- `udp://tracker.skyts.net:6969/announce` — no connect response
- `udp://tracker.sylphix.com:6969/announce` — no connect response
- `udp://tracker.tallpenguin.org:15750/announce` — no connect response
- `udp://tracker.teambelgium.net:6969/announce` — no connect response
- `udp://tracker.tryhackx.org:6969/announce` — no connect response
- `udp://tracker.yume-hatsuyuki.moe:6969/announce` — no connect response
- `udp://tracker1.itzmx.com:8080/announce` — no connect response
- `udp://tracker2.itzmx.com:6961/announce` — no connect response
- `udp://tracker3.itzmx.com:6961/announce` — no connect response
- `udp://tracker4.itzmx.com:2710/announce` — no connect response
- `wss://qot.abiir.top/announce` — ConnectionResetError: [Errno 104] Connection reset by peer

## 无法测试（特殊网络）

- `http://[2605:6400:30:fad6::dead:c0d3]:1337/announce` — IPv6 unavailable here
- `http://[2a04:ac00:1:3dd8::1:2710]:2710/announce` — IPv6 unavailable here
- `udp://[2a03:7220:8083:cd00::1]:451/announce` — IPv6 unavailable here
- `udp://[2a04:ac00:1:3dd8::1:2710]:2710/announce` — IPv6 unavailable here

## 低速 Tracker（>5s，已排除）

- `http://123.245.62.62:6969/announce` — 9548ms
- `https://tracker.bug38.com:443/announce` — 13768ms

## 同 IP 去重（保留响应最快）

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
- `http://31.38.161.123:6969/announce`
- `http://43.250.54.126:6969/announce`
- `http://79.111.12.213:6969/announce`
- `http://93.158.213.92:1337/announce`
- `http://94.23.207.177:6969/announce`
- `http://announce.sktorrent.eu:6969/announce`
- `http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce`
- `http://bittorrent.kali.org:80/announce`
- `http://bt.edwardk.info:12891/announce`
- `http://bt.edwardk.info:2710/announce`
- `http://bt.edwardk.info:4040/announce`
- `http://bt.edwardk.info:63124/announce`
- `http://bt.edwardk.info:676/announce`
- `http://bt.edwardk.info:6969/announce`
- `http://bt.nnm-club.info:2710/announce`
- `http://bt1.archive.org:6969/announce`
- `http://bt2.archive.org:6969/announce`
- `http://bt2.edwardk.info:2710/announce`
- `http://bt2.edwardk.info:4040/announce`
- `http://bt2.edwardk.info:6969/announce`
- `http://bttracker.debian.org:6969/announce`
- `http://ch3oh.ru:6969/announce`
- `http://ehtracker.org:80/1/announce`
- `http://ehtracker.org:80/1104308/announce`
- `http://ehtracker.org:80/1113709/announce`
- `http://ehtracker.org:80/1226599/1080494xo5eXcwFOBq/announce`
- `http://ehtracker.org:80/2496841/announce`
- `http://ehtracker.org:80/2566145/1159106xUfsJkT9Btg/announce`
- `http://ipv4announce.sktorrent.eu:6969/announce`
- `http://open.demonii.si:80/announce`
- `http://open.tracker.cl:1337/announce`
- `http://opentracker.acgnx.se:80/announce`
- `http://opentracker.xyz:80/announce`
- `http://opentrackr.org:1337/announce`
- `http://retracker.x2k.ru:80/announce`
- `http://retracker01-msk-virt.corbina.net:80/announce`
- `http://t-backup.213891.xyz:80/announce`
- `http://t.overflow.biz:6969/announce`
- `http://torrent.ubuntu.com:6969/announce`
- `http://tracker-udp.anirena.com:80/announce`
- `http://tracker-zhuqiy.dgj055.icu:80/announce`
- `http://tracker.004430.xyz:1337/announce`
- `http://tracker.ali213.net:8080/announce`
- `http://tracker.auctor.tv:6969/announce`
- `http://tracker.coppersurfer.site:2710/announce`
- `http://tracker.ddunlimited.net:6969/announce`
- `http://tracker.dhitechnical.com:6969/announce`
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
- `http://tracker.torrents.observer:80/announce`
- `http://tracker.waaa.moe:6969/announce`
- `http://tracker.xfapi.top:6868/announce`
- `http://tracker.xfapi.top:9999/announce`
- `http://tracker2.dler.com:80/announce`
- `http://tracker2.dler.org:80/announce`
- `http://tracker3.dler.org:2710/announce`
- `https://004430.xyz:443/announce`
- `https://1.tracker.eu.org:443/announce`
- `https://3.tracker.eu.org:443/announce`
- `https://337hhh.xyz:443/announce`
- `https://4.tracker.eu.org:443/announce`
- `https://bt.beatrice-raws.org:443/announce`
- `https://open.ftorrent.com:443/announce`
- `https://retracker.x2k.ru:443/announce`
- `https://t.btcland.xyz:443/announce`
- `https://tr-rh-zhuqiy.dgj055.icu:443/announce`
- `https://tr-zhuqiy-1.dgj055.icu:443/announce`
- `https://tr-zhuqiy-2.dgj055.icu:443/announce`
- `https://tr.nyacat.pw:443/announce`
- `https://tr.torland.ga:443/announce`
- `https://tracker-zhuqiy.dgj055.icu:443/announce`
- `https://tracker.zhuqiy.com:443/announce`
- `udp://120.78.150.131:6969/announce`
- `udp://151.242.104.187:80/announce`
- `udp://160.30.240.158:1337/announce`
- `udp://208.83.20.20:6969/announce`
- `udp://211.75.205.187:6969/announce`
- `udp://211.75.205.187:80/announce`
- `udp://211.75.205.188:6969/announce`
- `udp://211.75.210.221:80/announce`
- `udp://212.42.38.197:6969/announce`
- `udp://34.66.57.33:1337/announce`
- `udp://34.66.57.33:80/announce`
- `udp://43.250.54.126:6969/announce`
- `udp://45.38.170.167:6969/announce`
- `udp://47.76.201.250:6969/announce`
- `udp://51.222.82.36:6969/announce`
- `udp://52.58.128.163:6969/announce`
- `udp://60.172.236.18:6969/announce`
- `udp://65.109.28.17:6969/announce`
- `udp://83.102.180.21:80/announce`
- `udp://85.17.55.112:6969/announce`
- `udp://93.158.213.92:6969/announce`
- `udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce`
- `udp://chihaya.toss.li:9696/announce`
- `udp://evan.im:6969/announce`
- `udp://explodie.org:6969/announce`
- `udp://ipv4announce.sktorrent.eu:6969/announce`
- `udp://leet-tracker.moe:1337/announce`
- `udp://leet-tracker.moe:38151/announce`
- `udp://mail.segso.net:6969/announce`
- `udp://martin-gebhardt.eu:25/announce`
- `udp://open.demonii.com:1337/announce`
- `udp://open.ftorrent.com:443/announce`
- `udp://opentrackr.org:1337/announce`
- `udp://peerfect.org:6969/announce`
- `udp://qg.lorzl.gq:2710/announce`
- `udp://santost12.xyz:6969/announce`
- `udp://seedpeer.net:6969/announce`
- `udp://t.overflow.biz:6969/announce`
- `udp://tr4ck3r.duckdns.org:6969/announce`
- `udp://tracker-udp.gbitt.info:80/announce`
- `udp://tracker.004430.xyz:1337/announce`
- `udp://tracker.aruku.ovh:8081/announce`
- `udp://tracker.auctor.tv:6969/announce`
- `udp://tracker.bittor.pw:1337/announce`
- `udp://tracker.btzoo.eu:80/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.ddunlimited.net:6969/announce`
- `udp://tracker.dler.com:6969/announce`
- `udp://tracker.dler.org:6969/announce`
- `udp://tracker.ducks.party:1984/announce`
- `udp://tracker.farted.net:6969/announce`
- `udp://tracker.fatkhoala.org:13710/announce`
- `udp://tracker.fatkhoala.org:13790/announce`
- `udp://tracker.gmi.gd:6969/announce`
- `udp://tracker.ilibr.org:6969/announce`
- `udp://tracker.ilibr.org:80/announce`
- `udp://tracker.novaopcj.eu.org:6969/announce`
- `udp://tracker.nyaa.net:6969/announce`
- `udp://tracker.nyaa.vc:6969/announce`
- `udp://tracker.opentrackr.com:1337/announce`
- `udp://tracker.opentrackr.com:6969/announce`
- `udp://tracker.opentrackr.org:1337/announce`
- `udp://tracker.qu.ax:6969/announce`
- `udp://tracker.segso.net:6969/announce`
- `udp://tracker.sigterm.xyz:6969/announce`
- `udp://tracker.torrents.observer:80/announce`
- `udp://tracker.uw0.xyz:6969/announce`
- `udp://tracker.wildkat.net:6969/announce`
- `udp://tracker2.dler.com:80/announce`
- `udp://tracker2.dler.org:80/announce`
- `udp://www.torrent.eu.org:451/announce`
- `udp://yuptracker-eu.gaijinent.com:27022/announce`
- `udp://zer0day.ch:1337/announce`
- `wss://tracker.openwebtorrent.com:443/announce`
