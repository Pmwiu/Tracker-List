# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-08 06:33:12 UTC
- 总 Tracker 数: 95
- 存活 (alive): **66** (69%)
- 失效 (dead): **28**
- 不安全 (unsafe): **1**
- 无法测试 (untestable): 0
- 低速淘汰 (low-speed >5s): 0
- 同 IP 去重 (kept faster): 10
- 综合评分后保留前 20 个，淘汰 36 个
- 评分维度: 速度 50% + 历史稳定性 30% + 响应质量 20% + 地域适配加分(最高 +11)
- 协议多样性配额: 保底 4 条非 UDP，实际保留 4 条
- 耗时: 20.9 秒

## 协议分布

- udp: 43
- http: 12
- https: 10
- wss: 1

## 最终订阅列表（前 20 个，按综合评分降序）

1. `https://t.213891.xyz:443/announce` — score=93.9, 37ms, 存活率79%, 质量100, 地域+2
2. `https://1.tracker.eu.org:443/announce` — score=93.6, 42ms, 存活率79%, 质量100, 地域+2
3. `udp://tracker.004430.xyz:1337/announce` — score=93.3, 9ms, 存活率79%, 质量100, 地域+0
4. `udp://tracker.gmi.gd:6969/announce` — score=93.1, 12ms, 存活率79%, 质量100, 地域+0
5. `udp://open.ftorrent.com:443/announce` — score=91.9, 36ms, 存活率79%, 质量100, 地域+0
6. `udp://tracker.wildkat.net:6969/announce` — score=91.3, 48ms, 存活率79%, 质量100, 地域+0
7. `udp://evan.im:6969/announce` — score=91.2, 49ms, 存活率79%, 质量100, 地域+0
8. `wss://tracker.openwebtorrent.com:443/announce` — score=90.6, 22ms, 存活率79%, 质量90, 地域+0
9. `udp://tr4ck3r.duckdns.org:6969/announce` — score=90.2, 70ms, 存活率79%, 质量100, 地域+0
10. `udp://explodie.org:6969/announce` — score=87.8, 22ms, 存活率63%, 质量100, 地域+0
11. `udp://tracker-udp.gbitt.info:80/announce` — score=87.1, 133ms, 存活率79%, 质量100, 地域+0
12. `udp://torrent.tracker.durukanbal.com:6969/announce` — score=87.0, 133ms, 存活率79%, 质量100, 地域+0
13. `udp://exodus.desync.com:6969/announce` — score=86.6, 23ms, 存活率59%, 质量100, 地域+0
14. `udp://tracker.nyaa.vc:6969/announce` — score=86.4, 145ms, 存活率79%, 质量100, 地域+0
15. `udp://tracker.ducks.party:1984/announce` — score=86.4, 146ms, 存活率79%, 质量100, 地域+0
16. `http://tracker.renfei.net:8080/announce` — score=85.0, 174ms, 存活率79%, 质量100, 地域+0
17. `udp://tracker.dler.org:6969/announce` — score=80.7, 141ms, 存活率59%, 质量100, 地域+0
18. `udp://zer0day.ch:1337/announce` — score=80.2, 132ms, 存活率56%, 质量100, 地域+0
19. `udp://tracker.filemail.com:6969/announce` — score=79.0, 136ms, 存活率53%, 质量100, 地域+0
20. `udp://leet-tracker.moe:1337/announce` — score=76.5, 52ms, 存活率30%, 质量100, 地域+0

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
- `udp://tracker.nyaa.net:6969/announce` — no connect response
- `udp://tracker.publictracker.xyz:6969/announce` — no connect response
- `udp://tracker.skyts.net:6969/announce` — no connect response
- `udp://tracker.srv00.com:6969/announce` — no connect response
- `udp://tracker.theoks.net:6969/announce` — no connect response
- `udp://tracker.therarbg.to:6969/announce` — no connect response
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
- `udp://tracker.bittor.pw:1337/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.opentrackr.org:1337/announce`
- `udp://tracker.qu.ax:6969/announce`
- `udp://tracker.skynetcloud.site:6969/announce`
- `udp://tracker2.dler.org:80/announce`
