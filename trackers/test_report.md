# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-08 04:02:04 UTC
- 总 Tracker 数: 100
- 存活 (alive): **82** (82%)
- 失效 (dead): **18**
- 不安全 (unsafe): **0**
- 无法测试 (untestable): 0
- 低速淘汰 (low-speed >5s): 0
- 同 IP 去重 (kept faster): 18
- 综合评分后保留前 20 个，淘汰 44 个
- 协议多样性配额: 保底 4 条非 UDP，实际保留 4 条
- 耗时: 22.2 秒

## 协议分布

- udp: 48
- http: 22
- https: 11
- wss: 1

## 最终订阅列表（前 20 个，按综合评分降序）

1. `udp://tracker.wildkat.net:6969/announce` — score=95.0, 18ms, 存活率83%
2. `udp://open.ftorrent.com:443/announce` — score=95.0, 44ms, 存活率83%
3. `udp://51.81.222.188:6969/announce` — score=95.0, 65ms, 存活率83%
4. `udp://tracker.nyaa.vc:6969/announce` — score=95.0, 85ms, 存活率83%
5. `udp://tracker.torrents.observer:80/announce` — score=95.0, 85ms, 存活率83%
6. `udp://ipv4announce.sktorrent.eu:6969/announce` — score=95.0, 86ms, 存活率83%
7. `udp://martin-gebhardt.eu:25/announce` — score=95.0, 97ms, 存活率83%
8. `udp://mail.segso.net:6969/announce` — score=93.9, 114ms, 存活率83%
9. `udp://tracker.ilibr.org:6969/announce` — score=93.9, 114ms, 存活率83%
10. `udp://evan.im:6969/announce` — score=93.7, 2ms, 存活率79%
11. `udp://193.148.251.93:6969/announce` — score=93.7, 38ms, 存活率79%
12. `udp://tracker.gmi.gd:6969/announce` — score=93.7, 63ms, 存活率79%
13. `wss://tracker.openwebtorrent.com:443/announce` — score=92.1, 10ms, 存活率74%
14. `udp://132.226.6.145:6969/announce` — score=90.2, 161ms, 存活率83%
15. `udp://tracker.cn.nyaa.net:6969/announce` — score=87.4, 197ms, 存活率83%
16. `udp://43.154.112.29:17272/announce` — score=87.3, 199ms, 存活率83%
17. `https://t.213891.xyz:443/announce` — score=84.6, 19ms, 存活率49%
18. `http://207.241.231.226:6969/announce` — score=82.7, 125ms, 存活率49%
19. `udp://135.125.198.235:1984/announce` — score=77.9, 89ms, 存活率26%
20. `http://bt1.archive.org:6969/announce` — score=71.6, 129ms, 存活率13%

## 失效 Tracker

- `http://echostar.ddnsfree.com:8080/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://torrentsmd.com:8080/announce` — HTTPError: HTTP Error 403: Forbidden
- `http://tracker2.itzmx.com:6961/announce` — URLError: <urlopen error timed out>
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
- `udp://tracker.torrent.eu.org:451/announce` — no connect response
- `udp://wegkxfcivgx.ydns.eu:80/announce` — no connect response

## 同 IP 去重（保留响应最快）

- `http://207.241.226.111:6969/announce`
- `http://211.75.205.188:80/announce`
- `http://211.75.210.221:6969/announce`
- `http://211.75.210.221:80/announce`
- `http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce`
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
- `udp://tracker.skynetcloud.site:6969/announce`
