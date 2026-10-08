# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-08 01:56:28 UTC
- 总 Tracker 数: 100
- 存活 (alive): **80** (80%)
- 失效 (dead): **20**
- 不安全 (unsafe): **0**
- 无法测试 (untestable): 0
- 低速淘汰 (low-speed >5s): 0
- 同 IP 去重 (kept faster): 17
- 综合评分后保留前 20 个，淘汰 43 个
- 耗时: 14.9 秒

## 协议分布

- udp: 48
- http: 21
- https: 10
- wss: 1

## 最终订阅列表（前 20 个，按综合评分降序）

1. `udp://open.ftorrent.com:443/announce` — score=76.0, 6ms, 存活率20%
2. `udp://tracker.wildkat.net:6969/announce` — score=76.0, 26ms, 存活率20%
3. `udp://51.81.222.188:6969/announce` — score=76.0, 29ms, 存活率20%
4. `udp://tracker.torrents.observer:80/announce` — score=74.6, 118ms, 存活率20%
5. `udp://ipv4announce.sktorrent.eu:6969/announce` — score=74.5, 119ms, 存活率20%
6. `udp://132.226.6.145:6969/announce` — score=74.3, 122ms, 存活率20%
7. `udp://martin-gebhardt.eu:25/announce` — score=74.1, 124ms, 存活率20%
8. `udp://135.125.198.235:1984/announce` — score=73.6, 131ms, 存活率20%
9. `udp://tracker.nyaa.vc:6969/announce` — score=73.4, 134ms, 存活率20%
10. `udp://mail.segso.net:6969/announce` — score=72.6, 144ms, 存活率20%
11. `udp://tracker.ilibr.org:6969/announce` — score=72.6, 144ms, 存活率20%
12. `udp://tracker2.dler.org:80/announce` — score=72.0, 152ms, 存活率20%
13. `udp://tracker.dler.com:6969/announce` — score=71.9, 152ms, 存活率20%
14. `udp://43.154.112.29:17272/announce` — score=71.4, 160ms, 存活率20%
15. `udp://tracker.cn.nyaa.net:6969/announce` — score=71.3, 160ms, 存活率20%
16. `udp://tracker.bittor.pw:1337/announce` — score=70.0, 31ms, 存活率0%
17. `udp://193.148.251.93:6969/announce` — score=70.0, 35ms, 存活率0%
18. `udp://evan.im:6969/announce` — score=70.0, 37ms, 存活率0%
19. `udp://tracker.gmi.gd:6969/announce` — score=70.0, 38ms, 存活率0%
20. `udp://exodus.desync.com:6969/announce` — score=70.0, 43ms, 存活率0%

## 失效 Tracker

- `http://echostar.ddnsfree.com:8080/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://torrentsmd.com:8080/announce` — HTTPError: HTTP Error 403: Forbidden
- `http://tracker.xn--djrq4gl4hvoi.top:80/announce` — ConnectionResetError: [Errno 104] Connection reset by peer
- `http://tracker2.itzmx.com:6961/announce` — URLError: <urlopen error timed out>
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [Errno 104] Connection reset by peer>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tracker1.520.jp:443/announce` — HTTPError: HTTP Error 521: <none>
- `udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce` — no connect response
- `udp://open.tracker.ink:6969/announce` — no connect response
- `udp://opentor.org:2710/announce` — no connect response
- `udp://p4p.arenabg.com:1337/announce` — no connect response
- `udp://retracker.hotplug.ru:2710/announce` — no connect response
- `udp://tracker.nyaa.net:6969/announce` — no connect response
- `udp://tracker.skyts.net:6969/announce` — no connect response
- `udp://tracker.tryhackx.org:6969/announce` — no connect response
- `udp://wegkxfcivgx.ydns.eu:80/announce` — no connect response

## 同 IP 去重（保留响应最快）

- `http://211.75.205.187:6969/announce`
- `http://211.75.210.221:6969/announce`
- `http://211.75.210.221:80/announce`
- `http://bt1.archive.org:6969/announce`
- `http://bt2.archive.org:6969/announce`
- `http://ipv4announce.sktorrent.eu:6969/announce`
- `http://tracker.auctor.tv:6969/announce`
- `http://tracker.dler.com:6969/announce`
- `http://tracker.dler.org:6969/announce`
- `http://tracker.nyaa.vc:6969/announce`
- `http://tracker.qu.ax:6969/announce`
- `https://1337.abcvg.info:443/announce`
- `udp://tracker-udp.gbitt.info:80/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.dler.org:6969/announce`
- `udp://tracker.ducks.party:1984/announce`
- `udp://tracker.qu.ax:6969/announce`
