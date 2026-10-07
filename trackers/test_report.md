# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-07 13:39:47 UTC
- 总 Tracker 数: 100
- 存活 (alive): **87** (87%)
- 失效 (dead): **13**
- 不安全 (unsafe): **0**
- 无法测试 (untestable): 0
- 低速淘汰 (low-speed >5s): 0
- 同 IP 去重 (kept faster): 30
- 综合评分后保留前 20 个，淘汰 37 个
- 耗时: 20.3 秒

## 协议分布

- udp: 58
- http: 19
- https: 9
- wss: 1

## 最终订阅列表（前 20 个，按综合评分降序）

1. `udp://209.141.59.25:6969/announce` — score=80.8, 12ms, 存活率36%
2. `wss://tracker.openwebtorrent.com:443/announce` — score=80.8, 22ms, 存活率36%
3. `udp://exodus.desync.com:6969/announce` — score=80.8, 23ms, 存活率36%
4. `http://004430.xyz:80/announce` — score=80.8, 28ms, 存活率36%
5. `https://t.213891.xyz:443/announce` — score=80.8, 37ms, 存活率36%
6. `udp://open.ftorrent.com:443/announce` — score=80.8, 37ms, 存活率36%
7. `https://tracker.nekomi.cn:443/announce` — score=80.8, 39ms, 存活率36%
8. `https://1.tracker.eu.org:443/announce` — score=80.8, 44ms, 存活率36%
9. `udp://evan.im:6969/announce` — score=80.8, 49ms, 存活率36%
10. `udp://tracker.wildkat.net:6969/announce` — score=80.8, 54ms, 存活率36%
11. `http://bt2.archive.org:6969/announce` — score=80.8, 61ms, 存活率36%
12. `udp://tr4ck3r.duckdns.org:6969/announce` — score=80.8, 70ms, 存活率36%
13. `udp://tracker.dler.org:6969/announce` — score=77.7, 140ms, 存活率36%
14. `udp://torrent.tracker.durukanbal.com:6969/announce` — score=77.3, 145ms, 存活率36%
15. `http://207.241.226.111:6969/announce` — score=76.0, 34ms, 存活率20%
16. `udp://34.66.57.33:80/announce` — score=74.8, 49ms, 存活率16%
17. `udp://tracker.theoks.net:6969/announce` — score=70.0, 23ms, 存活率0%
18. `udp://23.157.120.14:6969/announce` — score=70.0, 44ms, 存活率0%
19. `udp://open.demonii.com:1337/announce` — score=67.7, 130ms, 存活率0%
20. `udp://43.250.54.126:6969/announce` — score=67.5, 132ms, 存活率0%

## 失效 Tracker

- `http://torrentsmd.com:8080/announce` — HTTPError: HTTP Error 403: Forbidden
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [Errno 104] Connection reset by peer>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error [Errno 104] Connection reset by peer>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tracker1.520.jp:443/announce` — HTTPError: HTTP Error 521: <none>
- `udp://open.tracker.ink:6969/announce` — no connect response
- `udp://opentor.org:2710/announce` — no connect response
- `udp://p4p.arenabg.com:1337/announce` — no connect response
- `udp://retracker.hotplug.ru:2710/announce` — no connect response
- `udp://tracker.skyts.net:6969/announce` — no connect response

## 同 IP 去重（保留响应最快）

- `http://135.125.198.235:2710/announce`
- `http://135.125.198.235:80/announce`
- `http://152.249.214.196:6969/announce`
- `http://211.75.205.187:6969/announce`
- `http://bt1.archive.org:6969/announce`
- `http://tracker.dhitechnical.com:6969/announce`
- `http://tracker.dler.com:6969/announce`
- `http://tracker.mywaifu.best:6969/announce`
- `https://004430.xyz:443/announce`
- `https://1337.abcvg.info:443/announce`
- `udp://109.201.134.183:80/announce`
- `udp://151.242.104.187:80/announce`
- `udp://185.121.168.96:1337/announce`
- `udp://211.75.205.188:80/announce`
- `udp://34.66.57.33:1337/announce`
- `udp://65.109.28.17:6969/announce`
- `udp://95.217.80.22:6969/announce`
- `udp://explodie.org:6969/announce`
- `udp://retracker01-msk-virt.corbina.net:80/announce`
- `udp://tracker.bittor.pw:1337/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.dler.com:6969/announce`
- `udp://tracker.ducks.party:1984/announce`
- `udp://tracker.gmi.gd:6969/announce`
- `udp://tracker.nyaa.vc:6969/announce`
- `udp://tracker.opentrackr.com:6969/announce`
- `udp://tracker.opentrackr.org:1337/announce`
- `udp://tracker.qu.ax:6969/announce`
- `udp://tracker.skynetcloud.site:6969/announce`
- `udp://tracker2.dler.org:80/announce`
