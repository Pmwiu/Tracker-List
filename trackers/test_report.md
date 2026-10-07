# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-07 02:21:31 UTC
- 总 Tracker 数: 100
- 存活 (alive): **71** (71%)
- 失效 (dead): **29**
- 不安全 (unsafe): **0**
- 无法测试 (untestable): 0
- 低速淘汰 (low-speed >5s): 2
- 同 IP 去重 (kept faster): 25
- 综合评分后保留前 20 个，淘汰 24 个
- 耗时: 15.4 秒

## 协议分布

- udp: 52
- http: 13
- https: 5
- wss: 1

## 最终订阅列表（前 20 个，按综合评分降序）

1. `udp://tracker.cn.nyaa.net:6969/announce` — score=70.0, 38ms, 连续0天
2. `udp://211.75.205.188:6969/announce` — score=70.0, 59ms, 连续0天
3. `udp://tracker.dler.com:6969/announce` — score=70.0, 63ms, 连续0天
4. `udp://tracker.dler.org:6969/announce` — score=70.0, 69ms, 连续0天
5. `udp://tracker.willy.pro:6969/announce` — score=70.0, 73ms, 连续0天
6. `udp://martin-gebhardt.eu:25/announce` — score=63.0, 190ms, 连续0天
7. `udp://tracker.gmi.gd:6969/announce` — score=61.9, 204ms, 连续0天
8. `udp://tracker.qu.ax:6969/announce` — score=61.2, 213ms, 连续0天
9. `udp://open.ftorrent.com:443/announce` — score=61.0, 216ms, 连续0天
10. `udp://135.125.198.235:1984/announce` — score=60.3, 224ms, 连续0天
11. `udp://tracker.nyaa.vc:6969/announce` — score=60.2, 225ms, 连续0天
12. `udp://34.66.57.33:80/announce` — score=59.7, 233ms, 连续0天
13. `udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce` — score=58.9, 243ms, 连续0天
14. `udp://151.242.104.187:80/announce` — score=57.8, 257ms, 连续0天
15. `udp://tracker.ilibr.org:6969/announce` — score=57.7, 259ms, 连续0天
16. `udp://tracker.torrent.eu.org:451/announce` — score=57.6, 259ms, 连续0天
17. `udp://23.157.120.14:6969/announce` — score=57.5, 315ms, 连续1天
18. `udp://95.217.80.20:6969/announce` — score=57.5, 261ms, 连续0天
19. `udp://31.56.179.159:6969/announce` — score=57.2, 265ms, 连续0天
20. `udp://65.109.28.17:6969/announce` — score=57.1, 266ms, 连续0天

## 失效 Tracker

- `http://004430.xyz:80/announce` — invalid bencoded response
- `http://123.245.62.62:6969/announce` — URLError: <urlopen error timed out>
- `http://123.245.62.74:6969/announce` — URLError: <urlopen error timed out>
- `http://bt1.archive.org:6969/announce` — URLError: <urlopen error timed out>
- `http://bt2.archive.org:6969/announce` — URLError: <urlopen error timed out>
- `http://torrentsmd.com:8080/announce` — URLError: <urlopen error timed out>
- `http://tracker.waaa.moe:6969/announce` — URLError: <urlopen error timed out>
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://004430.xyz:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for '004430.xyz'. (_ssl.c:1010)>
- `https://t.213891.xyz:443/announce` — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.kuroy.me:443/announce` — HTTPError: HTTP Error 503: Service Unavailable
- `https://tracker.nekomi.cn:443/announce` — timeout
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tracker.qingwapt.org:443/announce` — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>
- `https://tracker1.520.jp:443/announce` — HTTPError: HTTP Error 521: <none>
- `udp://209.141.59.25:6969/announce` — no connect response
- `udp://kolankoalastree.newtrackon.co.nz:1337/announce` — no connect response
- `udp://open.tracker.ink:6969/announce` — no connect response
- `udp://opentor.org:2710/announce` — no connect response
- `udp://p4p.arenabg.com:1337/announce` — no connect response
- `udp://retracker.hotplug.ru:2710/announce` — no connect response
- `udp://tracker.aruku.ovh:8081/announce` — no connect response
- `udp://tracker.skyts.net:6969/announce` — no connect response
- `udp://tracker.theoks.net:6969/announce` — no connect response
- `udp://tracker.tryhackx.org:6969/announce` — no connect response
- `udp://v2.iperson.xyz:6969/announce` — no connect response

## 低速 Tracker（>5s，已排除）

- `wss://tracker.openwebtorrent.com:443/announce` — 6367ms
- `https://tracker.foreverpirates.co:443/announce` — 6736ms

## 同 IP 去重（保留响应最快）

- `http://135.125.198.235:2710/announce`
- `http://135.125.198.235:80/announce`
- `http://140.235.237.23:6969/announce`
- `http://152.249.214.196:6969/announce`
- `http://211.75.205.187:6969/announce`
- `http://tracker.dler.com:6969/announce`
- `https://1337.abcvg.info:443/announce`
- `udp://109.201.134.183:80/announce`
- `udp://211.75.205.188:80/announce`
- `udp://34.66.57.33:1337/announce`
- `udp://43.250.54.126:6969/announce`
- `udp://45.137.199.107:6969/announce`
- `udp://83.102.180.21:80/announce`
- `udp://91.216.110.53:451/announce`
- `udp://93.158.213.92:1337/announce`
- `udp://95.217.80.22:6969/announce`
- `udp://explodie.org:6969/announce`
- `udp://open.stealth.si:80/announce`
- `udp://tracker.bittor.pw:1337/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.ducks.party:1984/announce`
- `udp://tracker.opentrackr.com:6969/announce`
- `udp://tracker.peerfect.org:6969/announce`
- `udp://tracker.skynetcloud.site:6969/announce`
- `udp://tracker2.dler.org:80/announce`
