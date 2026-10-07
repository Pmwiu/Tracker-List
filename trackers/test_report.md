# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-07 02:41:14 UTC
- 总 Tracker 数: 100
- 存活 (alive): **84** (84%)
- 失效 (dead): **16**
- 不安全 (unsafe): **0**
- 无法测试 (untestable): 0
- 低速淘汰 (low-speed >5s): 2
- 同 IP 去重 (kept faster): 27
- 综合评分后保留前 20 个，淘汰 35 个
- 耗时: 27.7 秒

## 协议分布

- udp: 55
- http: 19
- https: 9
- wss: 1

## 最终订阅列表（前 20 个，按综合评分降序）

1. `udp://23.157.120.14:6969/announce` — score=87.1, 97ms, 连续4天
2. `udp://open.ftorrent.com:443/announce` — score=82.9, 44ms, 连续3天
3. `udp://martin-gebhardt.eu:25/announce` — score=82.9, 92ms, 连续3天
4. `udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce` — score=82.9, 97ms, 连续3天
5. `udp://31.56.179.159:6969/announce` — score=82.2, 108ms, 连续3天
6. `udp://evan.im:6969/announce` — score=78.6, 2ms, 连续2天
7. `wss://tracker.openwebtorrent.com:443/announce` — score=78.6, 10ms, 连续2天
8. `udp://tr4ck3r.duckdns.org:6969/announce` — score=78.6, 15ms, 连续2天
9. `udp://tracker.wildkat.net:6969/announce` — score=78.6, 17ms, 连续2天
10. `https://t.213891.xyz:443/announce` — score=78.6, 18ms, 连续2天
11. `https://1.tracker.eu.org:443/announce` — score=78.6, 22ms, 连续2天
12. `http://140.235.237.23:6969/announce` — score=78.6, 46ms, 连续2天
13. `udp://43.250.54.126:6969/announce` — score=78.6, 82ms, 连续2天
14. `http://tracker.renfei.net:8080/announce` — score=74.3, 23ms, 连续1天
15. `udp://34.66.57.33:1337/announce` — score=74.3, 25ms, 连续1天
16. `udp://209.141.59.25:6969/announce` — score=74.3, 62ms, 连续1天
17. `udp://torrent.tracker.durukanbal.com:6969/announce` — score=74.3, 83ms, 连续1天
18. `udp://109.201.134.183:80/announce` — score=74.3, 84ms, 连续1天
19. `http://bt1.archive.org:6969/announce` — score=70.9, 198ms, 连续2天
20. `udp://exodus.desync.com:6969/announce` — score=70.0, 70ms, 连续0天

## 失效 Tracker

- `http://torrentsmd.com:8080/announce` — HTTPError: HTTP Error 403: Forbidden
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [Errno 104] Connection reset by peer>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tracker1.520.jp:443/announce` — HTTPError: HTTP Error 521: <none>
- `udp://185.121.168.96:1337/announce` — no connect response
- `udp://open.tracker.ink:6969/announce` — no connect response
- `udp://opentor.org:2710/announce` — no connect response
- `udp://p4p.arenabg.com:1337/announce` — no connect response
- `udp://retracker.hotplug.ru:2710/announce` — no connect response
- `udp://tracker.skyts.net:6969/announce` — no connect response
- `udp://tracker.theoks.net:6969/announce` — no connect response
- `udp://tracker.tryhackx.org:6969/announce` — no connect response

## 低速 Tracker（>5s，已排除）

- `http://123.245.62.74:6969/announce` — 6743ms
- `http://123.245.62.62:6969/announce` — 13312ms

## 同 IP 去重（保留响应最快）

- `http://135.125.198.235:2710/announce`
- `http://135.125.198.235:80/announce`
- `http://152.249.214.196:6969/announce`
- `http://211.75.205.187:6969/announce`
- `http://tracker.dhitechnical.com:6969/announce`
- `http://tracker.dler.com:6969/announce`
- `https://004430.xyz:443/announce`
- `https://1337.abcvg.info:443/announce`
- `udp://135.125.198.235:1984/announce`
- `udp://211.75.205.188:80/announce`
- `udp://34.66.57.33:80/announce`
- `udp://45.137.199.107:6969/announce`
- `udp://91.216.110.53:451/announce`
- `udp://95.217.80.20:6969/announce`
- `udp://explodie.org:6969/announce`
- `udp://open.stealth.si:80/announce`
- `udp://retracker01-msk-virt.corbina.net:80/announce`
- `udp://tracker-udp.gbitt.info:80/announce`
- `udp://tracker.bittor.pw:1337/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.dler.org:6969/announce`
- `udp://tracker.gmi.gd:6969/announce`
- `udp://tracker.ilibr.org:6969/announce`
- `udp://tracker.opentrackr.org:1337/announce`
- `udp://tracker.peerfect.org:6969/announce`
- `udp://tracker.qu.ax:6969/announce`
- `udp://tracker.skynetcloud.site:6969/announce`
