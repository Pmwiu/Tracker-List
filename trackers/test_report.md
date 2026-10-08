# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-08 05:21:54 UTC
- 总 Tracker 数: 95
- 存活 (alive): **67** (70%)
- 失效 (dead): **27**
- 不安全 (unsafe): **1**
- 无法测试 (untestable): 0
- 低速淘汰 (low-speed >5s): 0
- 同 IP 去重 (kept faster): 10
- 综合评分后保留前 20 个，淘汰 37 个
- 协议多样性配额: 保底 4 条非 UDP，实际保留 4 条
- 耗时: 19.6 秒

## 协议分布

- udp: 44
- http: 12
- https: 10
- wss: 1

## 最终订阅列表（前 20 个，按综合评分降序）

1. `udp://evan.im:6969/announce` — score=70.0, 5ms, 存活率0%
2. `wss://tracker.openwebtorrent.com:443/announce` — score=70.0, 17ms, 存活率0%
3. `udp://tr4ck3r.duckdns.org:6969/announce` — score=70.0, 19ms, 存活率0%
4. `udp://tracker.wildkat.net:6969/announce` — score=70.0, 21ms, 存活率0%
5. `http://tracker.renfei.net:8080/announce` — score=70.0, 27ms, 存活率0%
6. `https://t.213891.xyz:443/announce` — score=70.0, 29ms, 存活率0%
7. `https://1.tracker.eu.org:443/announce` — score=70.0, 30ms, 存活率0%
8. `udp://tracker.bittor.pw:1337/announce` — score=70.0, 31ms, 存活率0%
9. `udp://open.ftorrent.com:443/announce` — score=70.0, 48ms, 存活率0%
10. `udp://tracker.004430.xyz:1337/announce` — score=70.0, 61ms, 存活率0%
11. `udp://tracker.gmi.gd:6969/announce` — score=70.0, 62ms, 存活率0%
12. `udp://exodus.desync.com:6969/announce` — score=70.0, 67ms, 存活率0%
13. `udp://explodie.org:6969/announce` — score=70.0, 76ms, 存活率0%
14. `udp://torrent.tracker.durukanbal.com:6969/announce` — score=70.0, 86ms, 存活率0%
15. `udp://tracker.qu.ax:6969/announce` — score=70.0, 86ms, 存活率0%
16. `udp://zer0day.ch:1337/announce` — score=70.0, 87ms, 存活率0%
17. `udp://tracker-udp.gbitt.info:80/announce` — score=70.0, 87ms, 存活率0%
18. `udp://tracker.filemail.com:6969/announce` — score=70.0, 92ms, 存活率0%
19. `udp://tracker.nyaa.vc:6969/announce` — score=70.0, 95ms, 存活率0%
20. `udp://tracker.ducks.party:1984/announce` — score=70.0, 95ms, 存活率0%

## 失效 Tracker

- `http://torrentsmd.com:8080/announce` — HTTPError: HTTP Error 403: Forbidden
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://ht.therarbg.to:443/announce` — timeout
- `https://torrent.tracker.durukanbal.com:443/announce` — URLError: <urlopen error timed out>
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.bt4g.com:443/announce` — timeout
- `https://tracker.kuroy.me:443/announce` — HTTPError: HTTP Error 503: Service Unavailable
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
- `udp://leet-tracker.moe:1337/announce`
- `udp://tracker.auctor.tv:6969/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.dler.org:6969/announce`
- `udp://tracker.opentrackr.org:1337/announce`
- `udp://tracker.skynetcloud.site:6969/announce`
