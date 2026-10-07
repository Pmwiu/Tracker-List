# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-07 06:14:03 UTC
- 总 Tracker 数: 100
- 存活 (alive): **84** (84%)
- 失效 (dead): **16**
- 不安全 (unsafe): **0**
- 无法测试 (untestable): 0
- 低速淘汰 (low-speed >5s): 0
- 同 IP 去重 (kept faster): 30
- 综合评分后保留前 20 个，淘汰 34 个
- 耗时: 23.6 秒

## 协议分布

- udp: 56
- http: 19
- https: 8
- wss: 1

## 最终订阅列表（前 20 个，按综合评分降序）

1. `wss://tracker.openwebtorrent.com:443/announce` — score=76.0, 15ms, 存活率20%
2. `udp://open.ftorrent.com:443/announce` — score=76.0, 28ms, 存活率20%
3. `https://1.tracker.eu.org:443/announce` — score=76.0, 32ms, 存活率20%
4. `udp://exodus.desync.com:6969/announce` — score=76.0, 33ms, 存活率20%
5. `udp://explodie.org:6969/announce` — score=76.0, 35ms, 存活率20%
6. `https://t.213891.xyz:443/announce` — score=76.0, 36ms, 存活率20%
7. `udp://209.141.59.25:6969/announce` — score=76.0, 39ms, 存活率20%
8. `udp://tracker.wildkat.net:6969/announce` — score=76.0, 47ms, 存活率20%
9. `udp://evan.im:6969/announce` — score=76.0, 59ms, 存活率20%
10. `udp://tr4ck3r.duckdns.org:6969/announce` — score=76.0, 67ms, 存活率20%
11. `http://bt2.archive.org:6969/announce` — score=76.0, 77ms, 存活率20%
12. `http://004430.xyz:80/announce` — score=76.0, 81ms, 存活率20%
13. `https://tracker.nekomi.cn:443/announce` — score=76.0, 97ms, 存活率20%
14. `udp://211.75.205.188:80/announce` — score=73.6, 131ms, 存活率20%
15. `udp://tracker.dler.org:6969/announce` — score=73.6, 131ms, 存活率20%
16. `udp://185.121.168.96:1337/announce` — score=73.3, 135ms, 存活率20%
17. `udp://torrent.tracker.durukanbal.com:6969/announce` — score=72.4, 147ms, 存活率20%
18. `udp://tracker.corpscorp.online:80/announce` — score=70.0, 49ms, 存活率0%
19. `http://207.241.226.111:6969/announce` — score=70.0, 51ms, 存活率0%
20. `udp://tracker2.dler.org:80/announce` — score=67.5, 132ms, 存活率0%

## 失效 Tracker

- `http://torrentsmd.com:8080/announce` — HTTPError: HTTP Error 403: Forbidden
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.midnightprogrammer.net:443/announce` — HTTPError: HTTP Error 530: <none>
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tracker1.520.jp:443/announce` — HTTPError: HTTP Error 521: <none>
- `udp://open.tracker.ink:6969/announce` — no connect response
- `udp://opentor.org:2710/announce` — no connect response
- `udp://p4p.arenabg.com:1337/announce` — no connect response
- `udp://retracker.hotplug.ru:2710/announce` — no connect response
- `udp://tracker.skyts.net:6969/announce` — no connect response
- `udp://tracker.theoks.net:6969/announce` — no connect response
- `udp://tracker.tryhackx.org:6969/announce` — no connect response

## 同 IP 去重（保留响应最快）

- `http://135.125.198.235:2710/announce`
- `http://135.125.198.235:80/announce`
- `http://140.235.237.23:6969/announce`
- `http://152.249.214.196:6969/announce`
- `http://211.75.205.187:6969/announce`
- `http://bt1.archive.org:6969/announce`
- `http://tracker.dler.com:6969/announce`
- `http://tracker.mywaifu.best:6969/announce`
- `https://004430.xyz:443/announce`
- `https://1337.abcvg.info:443/announce`
- `udp://109.201.134.183:80/announce`
- `udp://211.75.205.188:6969/announce`
- `udp://23.157.120.14:6969/announce`
- `udp://34.66.57.33:1337/announce`
- `udp://34.66.57.33:80/announce`
- `udp://43.250.54.126:6969/announce`
- `udp://45.137.199.107:6969/announce`
- `udp://65.109.28.17:6969/announce`
- `udp://91.216.110.53:451/announce`
- `udp://93.158.213.92:1337/announce`
- `udp://open.demonii.com:1337/announce`
- `udp://open.stealth.si:80/announce`
- `udp://retracker01-msk-virt.corbina.net:80/announce`
- `udp://tracker.bittor.pw:1337/announce`
- `udp://tracker.dler.com:6969/announce`
- `udp://tracker.ducks.party:1984/announce`
- `udp://tracker.gmi.gd:6969/announce`
- `udp://tracker.ilibr.org:6969/announce`
- `udp://tracker.opentrackr.com:6969/announce`
- `udp://tracker.qu.ax:6969/announce`
