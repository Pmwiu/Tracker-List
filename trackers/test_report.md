# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-08 01:59:40 UTC
- 总 Tracker 数: 100
- 存活 (alive): **82** (82%)
- 失效 (dead): **18**
- 不安全 (unsafe): **0**
- 无法测试 (untestable): 0
- 低速淘汰 (low-speed >5s): 0
- 同 IP 去重 (kept faster): 19
- 综合评分后保留前 20 个，淘汰 43 个
- 耗时: 20.8 秒

## 协议分布

- udp: 49
- http: 22
- https: 10
- wss: 1

## 最终订阅列表（前 20 个，按综合评分降序）

1. `udp://51.81.222.188:6969/announce` — score=80.8, 30ms, 存活率36%
2. `udp://open.ftorrent.com:443/announce` — score=80.8, 36ms, 存活率36%
3. `udp://tracker.wildkat.net:6969/announce` — score=80.8, 52ms, 存活率36%
4. `udp://132.226.6.145:6969/announce` — score=80.1, 108ms, 存活率36%
5. `udp://tracker.dler.com:6969/announce` — score=77.7, 140ms, 存活率36%
6. `udp://martin-gebhardt.eu:25/announce` — score=77.6, 141ms, 存活率36%
7. `udp://tracker.torrents.observer:80/announce` — score=77.5, 143ms, 存活率36%
8. `udp://ipv4announce.sktorrent.eu:6969/announce` — score=77.4, 144ms, 存活率36%
9. `udp://135.125.198.235:1984/announce` — score=77.3, 144ms, 存活率36%
10. `udp://tracker.nyaa.vc:6969/announce` — score=77.2, 146ms, 存活率36%
11. `udp://43.154.112.29:17272/announce` — score=76.6, 153ms, 存活率36%
12. `udp://tracker.cn.nyaa.net:6969/announce` — score=76.4, 157ms, 存活率36%
13. `udp://tracker.ilibr.org:6969/announce` — score=76.2, 160ms, 存活率36%
14. `udp://tracker.gmi.gd:6969/announce` — score=76.0, 14ms, 存活率20%
15. `udp://exodus.desync.com:6969/announce` — score=76.0, 24ms, 存活率20%
16. `udp://evan.im:6969/announce` — score=76.0, 49ms, 存活率20%
17. `udp://193.148.251.93:6969/announce` — score=76.0, 70ms, 存活率20%
18. `udp://mail.segso.net:6969/announce` — score=76.0, 162ms, 存活率36%
19. `udp://tracker.corpscorp.online:80/announce` — score=74.8, 51ms, 存活率16%
20. `wss://tracker.openwebtorrent.com:443/announce` — score=70.0, 21ms, 存活率0%

## 失效 Tracker

- `http://echostar.ddnsfree.com:8080/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://torrentsmd.com:8080/announce` — HTTPError: HTTP Error 403: Forbidden
- `http://tracker2.itzmx.com:6961/announce` — URLError: <urlopen error timed out>
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tracker1.520.jp:443/announce` — HTTPError: HTTP Error 521: <none>
- `udp://explodie.org:6969/announce` — no connect response
- `udp://open.tracker.ink:6969/announce` — no connect response
- `udp://opentor.org:2710/announce` — no connect response
- `udp://p4p.arenabg.com:1337/announce` — no connect response
- `udp://retracker.hotplug.ru:2710/announce` — no connect response
- `udp://tracker.nyaa.net:6969/announce` — no connect response
- `udp://tracker.skyts.net:6969/announce` — no connect response
- `udp://wegkxfcivgx.ydns.eu:80/announce` — no connect response

## 同 IP 去重（保留响应最快）

- `http://211.75.205.187:6969/announce`
- `http://211.75.210.221:80/announce`
- `http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce`
- `http://bt1.archive.org:6969/announce`
- `http://bt2.archive.org:6969/announce`
- `http://ipv4announce.sktorrent.eu:6969/announce`
- `http://tracker.auctor.tv:6969/announce`
- `http://tracker.dler.com:6969/announce`
- `http://tracker.dler.org:6969/announce`
- `http://tracker.nyaa.vc:6969/announce`
- `http://tracker.qu.ax:6969/announce`
- `https://1337.abcvg.info:443/announce`
- `udp://109.201.134.183:80/announce`
- `udp://tracker.bittor.pw:1337/announce`
- `udp://tracker.dler.org:6969/announce`
- `udp://tracker.ducks.party:1984/announce`
- `udp://tracker.qu.ax:6969/announce`
- `udp://tracker.torrent.eu.org:451/announce`
- `udp://tracker2.dler.org:80/announce`
