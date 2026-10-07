# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-07 23:13:16 UTC
- 总 Tracker 数: 100
- 存活 (alive): **83** (83%)
- 失效 (dead): **17**
- 不安全 (unsafe): **0**
- 无法测试 (untestable): 0
- 低速淘汰 (low-speed >5s): 0
- 同 IP 去重 (kept faster): 28
- 综合评分后保留前 20 个，淘汰 35 个
- 耗时: 19.4 秒

## 协议分布

- udp: 53
- http: 20
- https: 9
- wss: 1

## 最终订阅列表（前 20 个，按综合评分降序）

1. `udp://tracker.wildkat.net:6969/announce` — score=84.6, 10ms, 存活率49%
2. `udp://open.ftorrent.com:443/announce` — score=84.6, 20ms, 存活率49%
3. `udp://evan.im:6969/announce` — score=84.6, 27ms, 存活率49%
4. `udp://tr4ck3r.duckdns.org:6969/announce` — score=84.6, 30ms, 存活率49%
5. `udp://209.141.59.25:6969/announce` — score=84.6, 42ms, 存活率49%
6. `udp://exodus.desync.com:6969/announce` — score=84.6, 48ms, 存活率49%
7. `wss://tracker.openwebtorrent.com:443/announce` — score=84.6, 54ms, 存活率49%
8. `https://1.tracker.eu.org:443/announce` — score=84.6, 67ms, 存活率49%
9. `udp://torrent.tracker.durukanbal.com:6969/announce` — score=84.3, 104ms, 存活率49%
10. `https://t.213891.xyz:443/announce` — score=83.8, 111ms, 存活率49%
11. `http://bt2.archive.org:6969/announce` — score=82.2, 132ms, 存活率49%
12. `http://004430.xyz:80/announce` — score=82.1, 132ms, 存活率49%
13. `https://tracker.nekomi.cn:443/announce` — score=81.0, 147ms, 存活率49%
14. `http://207.241.226.111:6969/announce` — score=80.8, 77ms, 存活率36%
15. `udp://tracker.dler.org:6969/announce` — score=79.4, 167ms, 存活率49%
16. `udp://23.157.120.14:6969/announce` — score=76.0, 95ms, 存活率20%
17. `udp://tracker.corpscorp.online:80/announce` — score=74.8, 19ms, 存活率16%
18. `udp://185.121.168.96:1337/announce` — score=74.1, 158ms, 存活率29%
19. `http://tracker.waaa.moe:6969/announce` — score=70.4, 144ms, 存活率13%
20. `http://tracker.renfei.net:8080/announce` — score=70.0, 87ms, 存活率0%

## 失效 Tracker

- `http://torrentsmd.com:8080/announce` — HTTPError: HTTP Error 403: Forbidden
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [Errno 104] Connection reset by peer>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tracker1.520.jp:443/announce` — HTTPError: HTTP Error 521: <none>
- `udp://208.83.20.20:6969/announce` — no connect response
- `udp://open.tracker.ink:6969/announce` — no connect response
- `udp://opentor.org:2710/announce` — no connect response
- `udp://p4p.arenabg.com:1337/announce` — no connect response
- `udp://retracker.hotplug.ru:2710/announce` — no connect response
- `udp://tracker.skyts.net:6969/announce` — no connect response
- `udp://tracker.theoks.net:6969/announce` — no connect response
- `udp://tracker.torrent.eu.org:451/announce` — no connect response
- `udp://tracker.tryhackx.org:6969/announce` — no connect response

## 同 IP 去重（保留响应最快）

- `http://1337.abcvg.info:80/announce`
- `http://135.125.198.235:2710/announce`
- `http://135.125.198.235:80/announce`
- `http://152.249.214.196:6969/announce`
- `http://211.75.205.187:6969/announce`
- `http://211.75.210.221:6969/announce`
- `http://bt1.archive.org:6969/announce`
- `http://tracker.dhitechnical.com:6969/announce`
- `http://tracker.dler.com:6969/announce`
- `http://tracker.mywaifu.best:6969/announce`
- `https://004430.xyz:443/announce`
- `udp://211.75.210.221:80/announce`
- `udp://34.66.57.33:1337/announce`
- `udp://34.66.57.33:80/announce`
- `udp://43.250.54.126:6969/announce`
- `udp://93.158.213.92:1337/announce`
- `udp://explodie.org:6969/announce`
- `udp://open.demonii.com:1337/announce`
- `udp://open.stealth.si:80/announce`
- `udp://retracker01-msk-virt.corbina.net:80/announce`
- `udp://tracker-udp.gbitt.info:80/announce`
- `udp://tracker.bittor.pw:1337/announce`
- `udp://tracker.ducks.party:1984/announce`
- `udp://tracker.gmi.gd:6969/announce`
- `udp://tracker.nyaa.vc:6969/announce`
- `udp://tracker.opentrackr.com:6969/announce`
- `udp://tracker.peerfect.org:6969/announce`
- `udp://tracker.qu.ax:6969/announce`
