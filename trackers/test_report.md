# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-07 02:48:29 UTC
- 总 Tracker 数: 100
- 存活 (alive): **82** (82%)
- 失效 (dead): **18**
- 不安全 (unsafe): **0**
- 无法测试 (untestable): 0
- 低速淘汰 (low-speed >5s): 0
- 同 IP 去重 (kept faster): 27
- 综合评分后保留前 20 个，淘汰 35 个
- 耗时: 17.7 秒

## 协议分布

- udp: 55
- http: 17
- https: 9
- wss: 1

## 最终订阅列表（前 20 个，按综合评分降序）

1. `udp://explodie.org:6969/announce` — score=70.0, 3ms, 存活率0%
2. `udp://exodus.desync.com:6969/announce` — score=70.0, 4ms, 存活率0%
3. `wss://tracker.openwebtorrent.com:443/announce` — score=70.0, 9ms, 存活率0%
4. `http://bt1.archive.org:6969/announce` — score=70.0, 15ms, 存活率0%
5. `http://bt2.archive.org:6969/announce` — score=70.0, 16ms, 存活率0%
6. `udp://209.141.59.25:6969/announce` — score=70.0, 18ms, 存活率0%
7. `udp://open.ftorrent.com:443/announce` — score=70.0, 28ms, 存活率0%
8. `https://t.213891.xyz:443/announce` — score=70.0, 29ms, 存活率0%
9. `http://004430.xyz:80/announce` — score=70.0, 40ms, 存活率0%
10. `https://1.tracker.eu.org:443/announce` — score=70.0, 44ms, 存活率0%
11. `https://tracker.nekomi.cn:443/announce` — score=70.0, 44ms, 存活率0%
12. `udp://tracker.wildkat.net:6969/announce` — score=70.0, 44ms, 存活率0%
13. `udp://34.66.57.33:80/announce` — score=70.0, 45ms, 存活率0%
14. `http://tracker.waaa.moe:6969/announce` — score=70.0, 46ms, 存活率0%
15. `udp://evan.im:6969/announce` — score=70.0, 63ms, 存活率0%
16. `udp://tr4ck3r.duckdns.org:6969/announce` — score=70.0, 66ms, 存活率0%
17. `udp://185.121.168.96:1337/announce` — score=67.2, 136ms, 存活率0%
18. `udp://torrent.tracker.durukanbal.com:6969/announce` — score=67.1, 138ms, 存活率0%
19. `udp://211.75.205.188:80/announce` — score=67.0, 138ms, 存活率0%
20. `udp://tracker.dler.org:6969/announce` — score=67.0, 138ms, 存活率0%

## 失效 Tracker

- `http://123.245.62.62:6969/announce` — URLError: <urlopen error timed out>
- `http://123.245.62.74:6969/announce` — URLError: <urlopen error timed out>
- `http://torrentsmd.com:8080/announce` — HTTPError: HTTP Error 403: Forbidden
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tracker1.520.jp:443/announce` — HTTPError: HTTP Error 521: <none>
- `udp://23.157.120.14:6969/announce` — no connect response
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
- `http://152.249.214.196:6969/announce`
- `http://tracker.dhitechnical.com:6969/announce`
- `http://tracker.dler.com:6969/announce`
- `https://004430.xyz:443/announce`
- `https://1337.abcvg.info:443/announce`
- `udp://109.201.134.183:80/announce`
- `udp://135.125.198.235:1984/announce`
- `udp://151.242.104.187:80/announce`
- `udp://211.75.205.188:6969/announce`
- `udp://34.66.57.33:1337/announce`
- `udp://43.250.54.126:6969/announce`
- `udp://45.137.199.107:6969/announce`
- `udp://65.109.28.17:6969/announce`
- `udp://93.158.213.92:1337/announce`
- `udp://open.demonii.com:1337/announce`
- `udp://retracker01-msk-virt.corbina.net:80/announce`
- `udp://tracker.bittor.pw:1337/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.dler.com:6969/announce`
- `udp://tracker.gmi.gd:6969/announce`
- `udp://tracker.ilibr.org:6969/announce`
- `udp://tracker.opentrackr.com:6969/announce`
- `udp://tracker.skynetcloud.site:6969/announce`
- `udp://tracker.torrent.eu.org:451/announce`
- `udp://tracker2.dler.org:80/announce`
