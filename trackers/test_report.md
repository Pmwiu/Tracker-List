# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-08 01:55:05 UTC
- 总 Tracker 数: 100
- 存活 (alive): **78** (78%)
- 失效 (dead): **22**
- 不安全 (unsafe): **0**
- 无法测试 (untestable): 0
- 低速淘汰 (low-speed >5s): 0
- 同 IP 去重 (kept faster): 15
- 综合评分后保留前 20 个，淘汰 43 个
- 耗时: 22.5 秒

## 协议分布

- udp: 45
- http: 22
- https: 10
- wss: 1

## 最终订阅列表（前 20 个，按综合评分降序）

1. `udp://admin.52ywp.com:6969/announce` — score=70.0, 29ms, 存活率0%
2. `udp://43.154.112.29:17272/announce` — score=70.0, 36ms, 存活率0%
3. `udp://tracker.cn.nyaa.net:6969/announce` — score=70.0, 42ms, 存活率0%
4. `udp://tracker.dler.org:6969/announce` — score=70.0, 55ms, 存活率0%
5. `udp://tracker2.dler.org:80/announce` — score=70.0, 59ms, 存活率0%
6. `udp://tracker.dler.com:6969/announce` — score=70.0, 62ms, 存活率0%
7. `udp://tracker.willy.pro:6969/announce` — score=70.0, 73ms, 存活率0%
8. `udp://132.226.6.145:6969/announce` — score=70.0, 95ms, 存活率0%
9. `udp://51.81.222.188:6969/announce` — score=62.4, 198ms, 存活率0%
10. `udp://open.ftorrent.com:443/announce` — score=61.7, 206ms, 存活率0%
11. `udp://135.125.198.235:1984/announce` — score=61.3, 212ms, 存活率0%
12. `udp://martin-gebhardt.eu:25/announce` — score=60.6, 220ms, 存活率0%
13. `udp://tracker.qu.ax:6969/announce` — score=60.5, 222ms, 存活率0%
14. `udp://tracker.corpscorp.online:80/announce` — score=59.9, 229ms, 存活率0%
15. `udp://tracker.wildkat.net:6969/announce` — score=59.9, 230ms, 存活率0%
16. `udp://mail.segso.net:6969/announce` — score=59.6, 234ms, 存活率0%
17. `udp://tracker.nyaa.vc:6969/announce` — score=59.4, 236ms, 存活率0%
18. `udp://tracker.torrents.observer:80/announce` — score=59.3, 237ms, 存活率0%
19. `udp://ipv4announce.sktorrent.eu:6969/announce` — score=59.2, 239ms, 存活率0%
20. `udp://tracker.ilibr.org:6969/announce` — score=59.0, 241ms, 存活率0%

## 失效 Tracker

- `http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce` — HTTPError: HTTP Error 502: Bad Gateway
- `http://echostar.ddnsfree.com:8080/announce` — timeout
- `http://torrentsmd.com:8080/announce` — HTTPError: HTTP Error 403: Forbidden
- `http://www.wareztorrent.com:80/announce` — HTTPError: HTTP Error 502: Bad Gateway
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate (_ssl.c:1010)>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.kuroy.me:443/announce` — HTTPError: HTTP Error 503: Service Unavailable
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tracker1.520.jp:443/announce` — HTTPError: HTTP Error 521: <none>
- `udp://open.tracker.ink:6969/announce` — no connect response
- `udp://opentor.org:2710/announce` — no connect response
- `udp://p4p.arenabg.com:1337/announce` — no connect response
- `udp://retracker.hotplug.ru:2710/announce` — no connect response
- `udp://tracker.aruku.ovh:8081/announce` — no connect response
- `udp://tracker.gmi.gd:6969/announce` — no connect response
- `udp://tracker.nyaa.net:6969/announce` — no connect response
- `udp://tracker.skyts.net:6969/announce` — no connect response
- `udp://tracker.torrent.eu.org:451/announce` — no connect response
- `udp://tracker.tryhackx.org:6969/announce` — no connect response
- `udp://v2.iperson.xyz:6969/announce` — no connect response
- `udp://wegkxfcivgx.ydns.eu:80/announce` — no connect response

## 同 IP 去重（保留响应最快）

- `http://211.75.205.187:6969/announce`
- `http://211.75.205.188:80/announce`
- `http://211.75.210.221:6969/announce`
- `http://211.75.210.221:80/announce`
- `http://ipv4announce.sktorrent.eu:6969/announce`
- `http://tracker.auctor.tv:6969/announce`
- `http://tracker.dler.com:6969/announce`
- `http://tracker.dler.org:6969/announce`
- `http://tracker.nyaa.vc:6969/announce`
- `http://tracker.qu.ax:6969/announce`
- `https://1337.abcvg.info:443/announce`
- `udp://tracker-udp.gbitt.info:80/announce`
- `udp://tracker.bittor.pw:1337/announce`
- `udp://tracker.ducks.party:1984/announce`
- `udp://tracker.skynetcloud.site:6969/announce`
