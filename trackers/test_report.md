# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-07 02:37:51 UTC
- 总 Tracker 数: 100
- 存活 (alive): **83** (83%)
- 失效 (dead): **17**
- 不安全 (unsafe): **0**
- 无法测试 (untestable): 0
- 低速淘汰 (low-speed >5s): 0
- 同 IP 去重 (kept faster): 28
- 综合评分后保留前 20 个，淘汰 35 个
- 耗时: 25.6 秒

## 协议分布

- udp: 56
- http: 17
- https: 9
- wss: 1

## 最终订阅列表（前 20 个，按综合评分降序）

1. `udp://23.157.120.14:6969/announce` — score=82.9, 68ms, 连续3天
2. `udp://open.ftorrent.com:443/announce` — score=78.6, 45ms, 连续2天
3. `udp://martin-gebhardt.eu:25/announce` — score=78.6, 92ms, 连续2天
4. `udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce` — score=78.6, 98ms, 连续2天
5. `udp://31.56.179.159:6969/announce` — score=78.1, 105ms, 连续2天
6. `udp://tracker.ilibr.org:6969/announce` — score=77.5, 114ms, 连续2天
7. `udp://evan.im:6969/announce` — score=74.3, 2ms, 连续1天
8. `wss://tracker.openwebtorrent.com:443/announce` — score=74.3, 10ms, 连续1天
9. `udp://tr4ck3r.duckdns.org:6969/announce` — score=74.3, 15ms, 连续1天
10. `udp://tracker.wildkat.net:6969/announce` — score=74.3, 18ms, 连续1天
11. `https://t.213891.xyz:443/announce` — score=74.3, 20ms, 连续1天
12. `https://1.tracker.eu.org:443/announce` — score=74.3, 27ms, 连续1天
13. `http://140.235.237.23:6969/announce` — score=74.3, 45ms, 连续1天
14. `udp://43.250.54.126:6969/announce` — score=74.3, 81ms, 连续1天
15. `http://bt1.archive.org:6969/announce` — score=71.6, 135ms, 连续1天
16. `http://tracker.renfei.net:8080/announce` — score=70.0, 25ms, 连续0天
17. `udp://34.66.57.33:1337/announce` — score=70.0, 27ms, 连续0天
18. `udp://209.141.59.25:6969/announce` — score=70.0, 61ms, 连续0天
19. `udp://torrent.tracker.durukanbal.com:6969/announce` — score=70.0, 82ms, 连续0天
20. `udp://109.201.134.183:80/announce` — score=70.0, 82ms, 连续0天

## 失效 Tracker

- `http://123.245.62.62:6969/announce` — timeout
- `http://123.245.62.74:6969/announce` — timeout
- `http://torrentsmd.com:8080/announce` — HTTPError: HTTP Error 403: Forbidden
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [Errno 104] Connection reset by peer>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tracker1.520.jp:443/announce` — HTTPError: HTTP Error 521: <none>
- `udp://exodus.desync.com:6969/announce` — no connect response
- `udp://open.tracker.ink:6969/announce` — no connect response
- `udp://opentor.org:2710/announce` — no connect response
- `udp://p4p.arenabg.com:1337/announce` — no connect response
- `udp://retracker.hotplug.ru:2710/announce` — no connect response
- `udp://tracker.skyts.net:6969/announce` — no connect response
- `udp://tracker.theoks.net:6969/announce` — no connect response

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
- `udp://151.242.104.187:80/announce`
- `udp://211.75.205.188:6969/announce`
- `udp://34.66.57.33:80/announce`
- `udp://45.137.199.107:6969/announce`
- `udp://65.109.28.17:6969/announce`
- `udp://93.158.213.92:1337/announce`
- `udp://95.217.80.20:6969/announce`
- `udp://95.217.80.22:6969/announce`
- `udp://explodie.org:6969/announce`
- `udp://open.demonii.com:1337/announce`
- `udp://retracker01-msk-virt.corbina.net:80/announce`
- `udp://tracker-udp.gbitt.info:80/announce`
- `udp://tracker.bittor.pw:1337/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.dler.com:6969/announce`
- `udp://tracker.gmi.gd:6969/announce`
- `udp://tracker.qu.ax:6969/announce`
- `udp://tracker.skynetcloud.site:6969/announce`
- `udp://tracker.torrent.eu.org:451/announce`
