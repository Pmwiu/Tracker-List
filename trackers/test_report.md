# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-08 06:13:30 UTC
- 总 Tracker 数: 95
- 存活 (alive): **65** (68%)
- 失效 (dead): **29**
- 不安全 (unsafe): **1**
- 无法测试 (untestable): 0
- 低速淘汰 (low-speed >5s): 0
- 同 IP 去重 (kept faster): 10
- 综合评分后保留前 20 个，淘汰 35 个
- 评分维度: 速度 50% + 历史稳定性 30% + 响应质量 20%
- 协议多样性配额: 保底 4 条非 UDP，实际保留 4 条
- 耗时: 21.0 秒

## 协议分布

- udp: 42
- http: 12
- https: 10
- wss: 1

## 最终订阅列表（前 20 个，按综合评分降序）

1. `udp://tracker.004430.xyz:1337/announce` — score=84.6, 9ms, 存活率49%, 质量100
2. `udp://tracker.gmi.gd:6969/announce` — score=84.6, 13ms, 存活率49%, 质量100
3. `udp://open.ftorrent.com:443/announce` — score=84.6, 36ms, 存活率49%, 质量100
4. `https://t.213891.xyz:443/announce` — score=84.6, 40ms, 存活率49%, 质量100
5. `udp://explodie.org:6969/announce` — score=84.6, 42ms, 存活率49%, 质量100
6. `https://1.tracker.eu.org:443/announce` — score=84.6, 43ms, 存活率49%, 质量100
7. `udp://evan.im:6969/announce` — score=84.6, 49ms, 存活率49%, 质量100
8. `udp://tracker.wildkat.net:6969/announce` — score=84.6, 54ms, 存活率49%, 质量100
9. `udp://tr4ck3r.duckdns.org:6969/announce` — score=84.6, 71ms, 存活率49%, 质量100
10. `wss://tracker.openwebtorrent.com:443/announce` — score=82.6, 21ms, 存活率49%, 质量90
11. `udp://torrent.tracker.durukanbal.com:6969/announce` — score=82.5, 138ms, 存活率49%, 质量100
12. `udp://tracker-udp.gbitt.info:80/announce` — score=82.4, 140ms, 存活率49%, 质量100
13. `udp://tracker.nyaa.vc:6969/announce` — score=82.1, 146ms, 存活率49%, 质量100
14. `udp://tracker.ducks.party:1984/announce` — score=81.8, 150ms, 存活率49%, 质量100
15. `http://tracker.renfei.net:8080/announce` — score=80.2, 180ms, 存活率49%, 质量100
16. `udp://exodus.desync.com:6969/announce` — score=78.6, 24ms, 存活率49%, 质量70
17. `udp://tracker.qu.ax:6969/announce` — score=72.1, 131ms, 存活率13%, 质量100
18. `udp://leet-tracker.moe:1337/announce` — score=70.0, 53ms, 存活率0%, 质量100
19. `udp://tracker.opentrackr.org:1337/announce` — score=68.1, 135ms, 存活率0%, 质量100
20. `udp://tracker.dler.org:6969/announce` — score=67.7, 141ms, 存活率0%, 质量100

## 失效 Tracker

- `http://torrentsmd.com:8080/announce` — HTTPError: HTTP Error 403: Forbidden
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://ht.therarbg.to:443/announce` — timeout
- `https://torrent.tracker.durukanbal.com:443/announce` — URLError: <urlopen error timed out>
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.bt4g.com:443/announce` — timeout
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tracker1.520.jp:443/announce` — HTTPError: HTTP Error 521: <none>
- `udp://6ahddutb1ucc3cp.ru:6969/announce` — no connect response
- `udp://open.tracker.ink:6969/announce` — no connect response
- `udp://opentor.org:2710/announce` — no connect response
- `udp://p4p.arenabg.com:1337/announce` — no connect response
- `udp://retracker.hotplug.ru:2710/announce` — no connect response
- `udp://torrentclub.online:54123/announce` — no connect response
- `udp://torrents.tmtime.dev:6969/announce` — no connect response
- `udp://tracker.alaskantf.com:6969/announce` — no connect response
- `udp://tracker.filemail.com:6969/announce` — no connect response
- `udp://tracker.publictracker.xyz:6969/announce` — no connect response
- `udp://tracker.skyts.net:6969/announce` — no connect response
- `udp://tracker.srv00.com:6969/announce` — no connect response
- `udp://tracker.theoks.net:6969/announce` — no connect response
- `udp://tracker.therarbg.to:6969/announce` — no connect response
- `udp://tracker.torrent.eu.org:451/announce` — no connect response
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
- `udp://tracker.skynetcloud.site:6969/announce`
- `udp://tracker2.dler.org:80/announce`
- `udp://zer0day.ch:1337/announce`
