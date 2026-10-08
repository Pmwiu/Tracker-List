# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-08 02:49:19 UTC
- 总 Tracker 数: 100
- 存活 (alive): **80** (80%)
- 失效 (dead): **20**
- 不安全 (unsafe): **0**
- 无法测试 (untestable): 0
- 低速淘汰 (low-speed >5s): 0
- 同 IP 去重 (kept faster): 19
- 综合评分后保留前 20 个，淘汰 41 个
- 耗时: 19.9 秒

## 协议分布

- udp: 48
- http: 21
- https: 10
- wss: 1

## 最终订阅列表（前 20 个，按综合评分降序）

1. `udp://tracker.wildkat.net:6969/announce` — score=87.7, 18ms, 存活率59%
2. `udp://open.ftorrent.com:443/announce` — score=87.7, 42ms, 存活率59%
3. `udp://51.81.222.188:6969/announce` — score=87.7, 68ms, 存活率59%
4. `udp://ipv4announce.sktorrent.eu:6969/announce` — score=87.7, 84ms, 存活率59%
5. `udp://tracker.torrents.observer:80/announce` — score=87.7, 85ms, 存活率59%
6. `udp://tracker.nyaa.vc:6969/announce` — score=87.7, 90ms, 存活率59%
7. `udp://martin-gebhardt.eu:25/announce` — score=87.7, 92ms, 存活率59%
8. `udp://mail.segso.net:6969/announce` — score=86.5, 116ms, 存活率59%
9. `udp://tracker.ilibr.org:6969/announce` — score=86.3, 118ms, 存活率59%
10. `udp://evan.im:6969/announce` — score=84.6, 2ms, 存活率49%
11. `udp://193.148.251.93:6969/announce` — score=84.6, 37ms, 存活率49%
12. `udp://tracker.gmi.gd:6969/announce` — score=84.6, 62ms, 存活率49%
13. `udp://132.226.6.145:6969/announce` — score=83.0, 160ms, 存活率59%
14. `udp://135.125.198.235:1984/announce` — score=81.7, 89ms, 存活率39%
15. `udp://tracker.dler.com:6969/announce` — score=80.9, 187ms, 存活率59%
16. `wss://tracker.openwebtorrent.com:443/announce` — score=80.8, 10ms, 存活率36%
17. `udp://tracker.cn.nyaa.net:6969/announce` — score=80.2, 196ms, 存活率59%
18. `udp://43.154.112.29:17272/announce` — score=80.0, 199ms, 存活率59%
19. `udp://tracker2.dler.org:80/announce` — score=75.8, 191ms, 存活率43%
20. `udp://tracker.bittor.pw:1337/announce` — score=73.8, 26ms, 存活率13%

## 失效 Tracker

- `http://echostar.ddnsfree.com:8080/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://torrentsmd.com:8080/announce` — HTTPError: HTTP Error 403: Forbidden
- `http://tracker.xn--djrq4gl4hvoi.top:80/announce` — ConnectionResetError: [Errno 104] Connection reset by peer
- `http://tracker2.itzmx.com:6961/announce` — URLError: <urlopen error timed out>
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate (_ssl.c:1010)>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tracker1.520.jp:443/announce` — HTTPError: HTTP Error 521: <none>
- `udp://exodus.desync.com:6969/announce` — no connect response
- `udp://open.tracker.ink:6969/announce` — no connect response
- `udp://opentor.org:2710/announce` — no connect response
- `udp://p4p.arenabg.com:1337/announce` — no connect response
- `udp://retracker.hotplug.ru:2710/announce` — no connect response
- `udp://tracker.nyaa.net:6969/announce` — no connect response
- `udp://tracker.skyts.net:6969/announce` — no connect response
- `udp://tracker.tryhackx.org:6969/announce` — no connect response
- `udp://wegkxfcivgx.ydns.eu:80/announce` — no connect response

## 同 IP 去重（保留响应最快）

- `http://1337.abcvg.info:80/announce`
- `http://211.75.205.187:6969/announce`
- `http://211.75.205.188:80/announce`
- `http://211.75.210.221:80/announce`
- `http://bt1.archive.org:6969/announce`
- `http://bt2.archive.org:6969/announce`
- `http://ipv4announce.sktorrent.eu:6969/announce`
- `http://tracker.auctor.tv:6969/announce`
- `http://tracker.dler.com:6969/announce`
- `http://tracker.dler.org:6969/announce`
- `http://tracker.nyaa.vc:6969/announce`
- `http://tracker.qu.ax:6969/announce`
- `udp://109.201.134.183:80/announce`
- `udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.dler.org:6969/announce`
- `udp://tracker.ducks.party:1984/announce`
- `udp://tracker.qu.ax:6969/announce`
- `udp://tracker.torrent.eu.org:451/announce`
