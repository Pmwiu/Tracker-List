# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-08 04:34:34 UTC
- 总 Tracker 数: 100
- 存活 (alive): **80** (80%)
- 失效 (dead): **18**
- 不安全 (unsafe): **0**
- 无法测试 (untestable): 2
- 低速淘汰 (low-speed >5s): 0
- 同 IP 去重 (kept faster): 32
- 综合评分后保留前 20 个，淘汰 28 个
- 协议多样性配额: 保底 4 条非 UDP，实际保留 4 条
- 耗时: 20.6 秒

## 协议分布

- udp: 43
- http: 26
- https: 10
- wss: 1

## 最终订阅列表（前 20 个，按综合评分降序）

1. `udp://open.ftorrent.com:443/announce` — score=96.0, 36ms, 存活率87%
2. `udp://evan.im:6969/announce` — score=95.0, 51ms, 存活率83%
3. `wss://tracker.openwebtorrent.com:443/announce` — score=93.7, 21ms, 存活率79%
4. `udp://mail.segso.net:6969/announce` — score=90.9, 165ms, 存活率87%
5. `udp://martin-gebhardt.eu:25/announce` — score=90.8, 166ms, 存活率87%
6. `http://207.241.231.226:6969/announce` — score=90.2, 39ms, 存活率67%
7. `https://t.213891.xyz:443/announce` — score=90.2, 42ms, 存活率67%
8. `udp://tracker.gmi.gd:6969/announce` — score=90.0, 12ms, 存活率67%
9. `udp://tracker.nyaa.vc:6969/announce` — score=86.9, 150ms, 存活率69%
10. `udp://exodus.desync.com:6969/announce` — score=86.7, 24ms, 存活率56%
11. `http://207.241.226.111:6969/announce` — score=82.9, 39ms, 存活率43%
12. `udp://explodie.org:6969/announce` — score=76.0, 25ms, 存活率20%
13. `udp://109.201.134.183:80/announce` — score=73.1, 137ms, 存活率20%
14. `udp://43.250.54.126:6969/announce` — score=73.1, 137ms, 存活率20%
15. `udp://tracker.bittor.pw:1337/announce` — score=73.0, 50ms, 存活率10%
16. `udp://open.stealth.si:80/announce` — score=72.2, 149ms, 存活率20%
17. `udp://89.234.156.205:451/announce` — score=71.1, 163ms, 存活率20%
18. `udp://tr4ck3r.duckdns.org:6969/announce` — score=70.0, 72ms, 存活率0%
19. `udp://open.demonii.com:1337/announce` — score=67.6, 130ms, 存活率0%
20. `udp://torrent.tracker.durukanbal.com:6969/announce` — score=67.1, 137ms, 存活率0%

## 失效 Tracker

- `http://echostar.ddnsfree.com:8080/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://retracker.hotplug.ru:2710/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://torrentsmd.com:8080/announce` — HTTPError: HTTP Error 403: Forbidden
- `http://tracker.opentorrent.top:6969/announce` — URLError: <urlopen error timed out>
- `http://tracker.plx.im:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://tracker.therarbg.to:6969/announce` — URLError: <urlopen error timed out>
- `http://tracker2.itzmx.com:6961/announce` — URLError: <urlopen error timed out>
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.kuroy.me:443/announce` — HTTPError: HTTP Error 503: Service Unavailable
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tracker1.520.jp:443/announce` — HTTPError: HTTP Error 521: <none>
- `udp://open.tracker.ink:6969/announce` — no connect response
- `udp://opentor.org:2710/announce` — no connect response
- `udp://p4p.arenabg.com:1337/announce` — no connect response
- `udp://retracker.hotplug.ru:2710/announce` — no connect response

## 无法测试（特殊网络）

- `http://[2605:6400:30:fad6::dead:c0d3]:1337/announce` — IPv6 unavailable here
- `http://[2a04:ac00:1:3dd8::1:2710]:2710/announce` — IPv6 unavailable here

## 同 IP 去重（保留响应最快）

- `http://107.189.2.131:1337/announce`
- `http://211.75.205.188:80/announce`
- `http://211.75.210.221:6969/announce`
- `http://211.75.210.221:80/announce`
- `http://announce.sktorrent.eu:6969/announce`
- `http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce`
- `http://bt1.archive.org:6969/announce`
- `http://bt2.archive.org:6969/announce`
- `http://ipv4announce.sktorrent.eu:6969/announce`
- `http://retracker01-msk-virt.corbina.net:80/announce`
- `http://tracker.auctor.tv:6969/announce`
- `http://tracker.dler.com:6969/announce`
- `http://tracker.nyaa.vc:6969/announce`
- `http://tracker.opentrackr.org:1337/announce`
- `http://tracker.qu.ax:6969/announce`
- `https://1337.abcvg.info:443/announce`
- `udp://135.125.198.235:1984/announce`
- `udp://151.242.104.187:80/announce`
- `udp://185.121.168.96:1337/announce`
- `udp://208.83.20.20:6969/announce`
- `udp://209.141.59.25:6969/announce`
- `udp://23.157.120.14:6969/announce`
- `udp://34.66.57.33:1337/announce`
- `udp://34.66.57.33:80/announce`
- `udp://45.137.199.107:6969/announce`
- `udp://93.158.213.92:1337/announce`
- `udp://retracker01-msk-virt.corbina.net:80/announce`
- `udp://tracker-udp.gbitt.info:80/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.qu.ax:6969/announce`
- `udp://tracker.skynetcloud.site:6969/announce`
- `udp://tracker.torrent.eu.org:451/announce`
