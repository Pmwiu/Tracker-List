# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-08 06:25:49 UTC
- 总 Tracker 数: 95
- 存活 (alive): **66** (69%)
- 失效 (dead): **28**
- 不安全 (unsafe): **1**
- 无法测试 (untestable): 0
- 低速淘汰 (low-speed >5s): 0
- 同 IP 去重 (kept faster): 9
- 综合评分后保留前 20 个，淘汰 37 个
- 评分维度: 速度 50% + 历史稳定性 30% + 响应质量 20%
- 协议多样性配额: 保底 4 条非 UDP，实际保留 4 条
- 耗时: 15.3 秒

## 协议分布

- udp: 43
- http: 12
- https: 10
- wss: 1

## 最终订阅列表（前 20 个，按综合评分降序）

1. `udp://open.ftorrent.com:443/announce` — score=90.8, 28ms, 存活率74%, 质量100
2. `https://t.213891.xyz:443/announce` — score=90.6, 30ms, 存活率74%, 质量100
3. `udp://tracker.004430.xyz:1337/announce` — score=90.6, 31ms, 存活率74%, 质量100
4. `https://1.tracker.eu.org:443/announce` — score=90.2, 38ms, 存活率74%, 质量100
5. `udp://tracker.gmi.gd:6969/announce` — score=90.2, 40ms, 存活率74%, 质量100
6. `udp://tracker.wildkat.net:6969/announce` — score=89.8, 47ms, 存活率74%, 质量100
7. `wss://tracker.openwebtorrent.com:443/announce` — score=89.4, 14ms, 存活率74%, 质量90
8. `udp://evan.im:6969/announce` — score=89.1, 61ms, 存活率74%, 质量100
9. `udp://tr4ck3r.duckdns.org:6969/announce` — score=88.8, 67ms, 存活率74%, 质量100
10. `http://tracker.renfei.net:8080/announce` — score=85.7, 129ms, 存活率74%, 质量100
11. `udp://tracker.nyaa.vc:6969/announce` — score=85.0, 142ms, 存活率74%, 质量100
12. `udp://torrent.tracker.durukanbal.com:6969/announce` — score=84.9, 144ms, 存活率74%, 质量100
13. `udp://explodie.org:6969/announce` — score=84.9, 25ms, 存活率54%, 质量100
14. `udp://tracker-udp.gbitt.info:80/announce` — score=84.7, 149ms, 存活率74%, 质量100
15. `udp://tracker.ducks.party:1984/announce` — score=84.5, 154ms, 存活率74%, 质量100
16. `udp://tracker.dler.org:6969/announce` — score=78.0, 132ms, 存活率49%, 质量100
17. `udp://zer0day.ch:1337/announce` — score=76.1, 148ms, 存活率45%, 质量100
18. `udp://leet-tracker.moe:1337/announce` — score=71.3, 51ms, 存活率13%, 质量100
19. `udp://tracker.theoks.net:6969/announce` — score=70.3, 43ms, 存活率8%, 质量100
20. `udp://tracker.filemail.com:6969/announce` — score=68.8, 150ms, 存活率41%, 质量70

## 失效 Tracker

- `http://torrentsmd.com:8080/announce` — HTTPError: HTTP Error 403: Forbidden
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://ht.therarbg.to:443/announce` — timeout
- `https://torrent.tracker.durukanbal.com:443/announce` — URLError: <urlopen error timed out>
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.bt4g.com:443/announce` — timeout
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tracker1.520.jp:443/announce` — HTTPError: HTTP Error 521: <none>
- `udp://6ahddutb1ucc3cp.ru:6969/announce` — no connect response
- `udp://exodus.desync.com:6969/announce` — no connect response
- `udp://open.tracker.ink:6969/announce` — no connect response
- `udp://opentor.org:2710/announce` — no connect response
- `udp://p4p.arenabg.com:1337/announce` — no connect response
- `udp://retracker.hotplug.ru:2710/announce` — no connect response
- `udp://torrentclub.online:54123/announce` — no connect response
- `udp://torrents.tmtime.dev:6969/announce` — no connect response
- `udp://tracker.alaskantf.com:6969/announce` — no connect response
- `udp://tracker.publictracker.xyz:6969/announce` — no connect response
- `udp://tracker.skyts.net:6969/announce` — no connect response
- `udp://tracker.srv00.com:6969/announce` — no connect response
- `udp://tracker.therarbg.to:6969/announce` — no connect response
- `udp://tracker.tryhackx.org:6969/announce` — no connect response
- `udp://tracker.wepzone.net:6969/announce` — no connect response
- `udp://tracker1.myporn.club:9337/announce` — no connect response
- `udp://wepzone.net:6969/announce` — no connect response

## 不安全 Tracker（已过滤）

- `udp://open.dstud.io:6969/announce` — resolves to private IP: 0.0.0.0

## 同 IP 去重（保留响应最快）

- `http://tracker.dler.com:6969/announce`
- `http://tracker.dler.org:6969/announce`
- `http://tracker.opentrackr.org:1337/announce`
- `https://1337.abcvg.info:443/announce`
- `udp://tracker.auctor.tv:6969/announce`
- `udp://tracker.bittor.pw:1337/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.opentrackr.org:1337/announce`
- `udp://tracker.qu.ax:6969/announce`
