# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-07 02:22:40 UTC
- 总 Tracker 数: 100
- 存活 (alive): **82** (82%)
- 失效 (dead): **18**
- 不安全 (unsafe): **0**
- 无法测试 (untestable): 0
- 低速淘汰 (low-speed >5s): 0
- 同 IP 去重 (kept faster): 28
- 综合评分后保留前 20 个，淘汰 34 个
- 耗时: 21.5 秒

## 协议分布

- udp: 55
- http: 17
- https: 9
- wss: 1

## 最终订阅列表（前 20 个，按综合评分降序）

1. `udp://23.157.120.14:6969/announce` — score=78.6, 89ms, 连续2天
2. `udp://open.ftorrent.com:443/announce` — score=74.3, 21ms, 连续1天
3. `udp://tracker.gmi.gd:6969/announce` — score=74.3, 42ms, 连续1天
4. `udp://martin-gebhardt.eu:25/announce` — score=73.4, 111ms, 连续1天
5. `udp://151.242.104.187:80/announce` — score=72.9, 118ms, 连续1天
6. `udp://tracker.torrent.eu.org:451/announce` — score=72.8, 120ms, 连续1天
7. `udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce` — score=72.5, 123ms, 连续1天
8. `udp://65.109.28.17:6969/announce` — score=71.4, 137ms, 连续1天
9. `udp://31.56.179.159:6969/announce` — score=71.4, 137ms, 连续1天
10. `udp://tracker.ilibr.org:6969/announce` — score=71.2, 140ms, 连续1天
11. `udp://tracker.wildkat.net:6969/announce` — score=70.0, 13ms, 连续0天
12. `udp://tracker.corpscorp.online:80/announce` — score=70.0, 20ms, 连续0天
13. `udp://evan.im:6969/announce` — score=70.0, 32ms, 连续0天
14. `udp://tr4ck3r.duckdns.org:6969/announce` — score=70.0, 34ms, 连续0天
15. `wss://tracker.openwebtorrent.com:443/announce` — score=70.0, 50ms, 连续0天
16. `https://t.213891.xyz:443/announce` — score=70.0, 69ms, 连续0天
17. `https://1.tracker.eu.org:443/announce` — score=70.0, 71ms, 连续0天
18. `http://140.235.237.23:6969/announce` — score=70.0, 92ms, 连续0天
19. `http://bt1.archive.org:6969/announce` — score=70.0, 96ms, 连续0天
20. `udp://43.250.54.126:6969/announce` — score=69.5, 106ms, 连续0天

## 失效 Tracker

- `http://123.245.62.62:6969/announce` — URLError: <urlopen error timed out>
- `http://123.245.62.74:6969/announce` — URLError: <urlopen error timed out>
- `http://torrentsmd.com:8080/announce` — HTTPError: HTTP Error 403: Forbidden
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)>
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
- `udp://tracker.tryhackx.org:6969/announce` — no connect response

## 同 IP 去重（保留响应最快）

- `http://1337.abcvg.info:80/announce`
- `http://135.125.198.235:2710/announce`
- `http://135.125.198.235:80/announce`
- `http://152.249.214.196:6969/announce`
- `http://211.75.205.187:6969/announce`
- `http://tracker.dhitechnical.com:6969/announce`
- `http://tracker.dler.com:6969/announce`
- `https://004430.xyz:443/announce`
- `udp://109.201.134.183:80/announce`
- `udp://135.125.198.235:1984/announce`
- `udp://185.121.168.96:1337/announce`
- `udp://209.141.59.25:6969/announce`
- `udp://211.75.205.188:6969/announce`
- `udp://34.66.57.33:1337/announce`
- `udp://34.66.57.33:80/announce`
- `udp://95.217.80.20:6969/announce`
- `udp://95.217.80.22:6969/announce`
- `udp://explodie.org:6969/announce`
- `udp://open.stealth.si:80/announce`
- `udp://retracker01-msk-virt.corbina.net:80/announce`
- `udp://tracker.bittor.pw:1337/announce`
- `udp://tracker.dler.com:6969/announce`
- `udp://tracker.dler.org:6969/announce`
- `udp://tracker.nyaa.vc:6969/announce`
- `udp://tracker.opentrackr.org:1337/announce`
- `udp://tracker.peerfect.org:6969/announce`
- `udp://tracker.qu.ax:6969/announce`
- `udp://tracker.skynetcloud.site:6969/announce`
