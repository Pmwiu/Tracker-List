# Tracker 活性测试 + 测速排序报告

- 测试时间: 2026-09-28 05:59:22 UTC
- 总 Tracker 数: 355
- 存活 (alive): **296** (83%)
- 失效 (dead): **58**
- 不安全 (unsafe): **1**
- 无法测试 (untestable): 0
- 速度排序后保留前 39 个，淘汰 257 个
- 耗时: 66.8 秒

## 存活 Tracker（按响应速度升序，前 N 个进入订阅列表）

1. `udp://120.78.150.131:6969/announce` — 31ms — valid connect + announce
2. `udp://60.172.236.18:6969/announce` — 31ms — valid connect + announce
3. `udp://v2.iperson.xyz:6969/announce` — 34ms — valid connect + announce
4. `udp://118.196.100.63:6969/announce` — 36ms — valid connect + announce
5. `udp://47.76.201.250:6969/announce` — 38ms — valid connect + announce
6. `udp://43.154.112.29:17272/announce` — 41ms — valid connect + announce
7. `udp://tracker.cn.nyaa.net:6969/announce` — 50ms — valid connect + announce
8. `udp://admin.52ywp.com:6969/announce` — 53ms — valid connect (announce not confirmed)
9. `http://tracker.ali213.net:8000/announce` — 59ms — online (failure reason)
10. `udp://211.75.205.188:6969/announce` — 60ms — valid connect + announce
11. `udp://211.75.205.187:80/announce` — 61ms — valid connect + announce
12. `udp://211.75.210.221:80/announce` — 62ms — valid connect + announce
13. `udp://60.249.37.20:6969/announce` — 64ms — valid connect + announce
14. `udp://211.75.205.189:6969/announce` — 64ms — valid connect + announce
15. `udp://211.75.205.189:80/announce` — 65ms — valid connect + announce
16. `udp://211.75.205.188:80/announce` — 65ms — valid connect + announce
17. `udp://211.75.210.221:6969/announce` — 66ms — valid connect + announce
18. `udp://211.75.205.187:6969/announce` — 67ms — valid connect + announce
19. `udp://tracker2.dler.com:80/announce` — 69ms — valid connect + announce
20. `udp://tracker.leechers-paradise.org:6969/announce` — 69ms — valid connect + announce
21. `udp://60.249.37.20:80/announce` — 70ms — valid connect + announce
22. `udp://tracker2.dler.org:80/announce` — 73ms — valid connect + announce
23. `udp://tracker.dler.org:6969/announce` — 75ms — valid connect + announce
24. `udp://tracker.dler.com:6969/announce` — 77ms — valid connect + announce
25. `http://tracker.ali213.net:8080/announce` — 81ms — online (failure reason)
26. `udp://221.153.216.56:8081/announce` — 91ms — valid connect + announce
27. `udp://132.226.6.145:6969/announce` — 93ms — valid connect + announce
28. `udp://anime-tracker.aruku.kro.kr:8081/announce` — 97ms — valid connect + announce
29. `http://tracker.dm258.cn:7070/announce` — 98ms — online (failure reason)
30. `http://tracker2.dler.com/announce` — 128ms — valid announce response
31. `http://211.75.205.189/announce` — 131ms — valid announce response
32. `http://211.75.210.221/announce` — 131ms — valid announce response
33. `http://211.75.205.188:6969/announce` — 132ms — valid announce response
34. `udp://yuptracker-sa.gaijinent.com:27022/announce` — 137ms — valid connect + announce
35. `http://211.75.205.187/announce` — 138ms — valid announce response
36. `http://tracker2.dler.org/announce` — 138ms — valid announce response
37. `http://tracker2.dler.org:80/announce` — 138ms — valid announce response
38. `http://211.75.205.188/announce` — 140ms — valid announce response
39. `http://tracker.dler.org:6969/announce` — 145ms — valid announce response

## 失效 Tracker

- `http://0123456789nonexistent.com/announce` — timeout
- `http://216.144.239.90:6969/announce` — URLError: <urlopen error timed out>
- `http://34.66.57.33:2701/announce` — timeout
- `http://79.111.12.213:6969/announce` — URLError: <urlopen error timed out>
- `http://bt.poletracker.org:2710/announce` — timeout
- `http://bt1.archive.org:6969/announce` — URLError: <urlopen error timed out>
- `http://bt2.archive.org:6969/announce` — URLError: <urlopen error timed out>
- `http://btracker.top:11451/announce` — timeout
- `http://buny.uk:6969/announce` — timeout
- `http://ch3oh.ru:6969/announce` — URLError: <urlopen error timed out>
- `http://jvavav.com/announce` — timeout
- `http://opentracker.acgnx.se/announce` — URLError: <urlopen error timed out>
- `http://seeders-paradise.org/announce` — timeout
- `http://t-backup.213891.xyz/announce` — ConnectionResetError: [WinError 10054] 远程主机强迫关闭了一个现有的连接。
- `http://torrentsmd.com:8080/announce` — HTTPError: HTTP Error 403: Forbidden
- `http://tracker-udp.anirena.com/announce` — URLError: <urlopen error timed out>
- `http://tracker.004430.xyz:1337/announce` — timeout
- `http://tracker.acgnx.se/announce` — URLError: <urlopen error timed out>
- `http://tracker.bt-hash.com/announce` — timeout
- `http://tracker.k.vu:6969/announce` — URLError: <urlopen error timed out>
- `http://tracker.lintk.me:2710/announce` — URLError: <urlopen error timed out>
- `http://tracker.nucozer-tracker.ml:2710/announce` — timeout
- `http://tracker.waaa.moe:6969/announce` — timeout
- `http://tracker1.itzmx.com:8080/announce` — timeout
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://004430.xyz/announce` — timeout
- `https://1.tracker.eu.org/announce` — timeout
- `https://3.tracker.eu.org/announce` — timeout
- `https://bt.beatrice-raws.org/announce` — timeout
- `https://open.ftorrent.com/announce` — timeout
- `https://retracker.x2k.ru/announce` — timeout
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1082)>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error _ssl.c:1064: The handshake operation timed out>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1082)>
- `https://tr2.trkb.ru/announce` — timeout
- `https://tracker-zhuqiy.dgj055.icu/announce` — timeout
- `https://tracker.foreverpirates.co/announce` — timeout
- `https://tracker.kuroy.me:443/announce` — HTTPError: HTTP Error 503: Service Unavailable
- `https://tracker.nekomi.cn:443/announce` — timeout
- `https://tracker.pmman.tech/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tracker1.520.jp:443/announce` — HTTPError: HTTP Error 521: <none>
- `https://wolf.parrot.run/announce` — timeout
- `udp://160.30.240.158:1337/announce` — ConnectionResetError: [WinError 10054] 远程主机强迫关闭了一个现有的连接。
- `udp://45.38.170.167:6969/announce` — no connect response
- `udp://archive.torrentonline.cc:42069/announce` — no connect response
- `udp://ipv6.govt.hu:6969/announce` — DNS resolution failed
- `udp://kolankoalastree.newtrackon.co.nz:1337/announce` — ConnectionResetError: [WinError 10054] 远程主机强迫关闭了一个现有的连接。
- `udp://open.stealth.si/announce` — ConnectionResetError: [WinError 10054] 远程主机强迫关闭了一个现有的连接。
- `udp://open.tracker.ink:6969/announce` — no connect response
- `udp://opentor.org:2710/announce` — no connect response
- `udp://p4p.arenabg.com:1337/announce` — no connect response
- `udp://retracker.hotplug.ru:2710/announce` — DNS resolution failed
- `udp://tracker-udp.anirena.com:80/announce` — no connect response
- `udp://tracker.k.vu:6969/announce` — no connect response
- `udp://tracker.skyts.net:6969/announce` — no connect response
- `wss://qot.abiir.top/announce` — SSLEOFError: [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1082)
- `wss://spacetradersapi-chatbox.herokuapp.com/announce` — timeout

## 不安全 Tracker（已过滤）

- `http://tracker.pussytorrents.org:3000/announce` — resolves to private IP: 2001::1f0d:4621
