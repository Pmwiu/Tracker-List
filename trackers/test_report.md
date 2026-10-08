# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-08 04:21:14 UTC
- 总 Tracker 数: 100
- 存活 (alive): **77** (77%)
- 失效 (dead): **20**
- 不安全 (unsafe): **0**
- 无法测试 (untestable): 3
- 低速淘汰 (low-speed >5s): 0
- 同 IP 去重 (kept faster): 32
- 综合评分后保留前 20 个，淘汰 25 个
- 协议多样性配额: 保底 4 条非 UDP，实际保留 4 条
- 耗时: 14.4 秒

## 协议分布

- udp: 38
- http: 28
- https: 11

## 最终订阅列表（前 20 个，按综合评分降序）

1. `udp://193.148.251.93:6969/announce` — score=95.0, 38ms, 存活率83%
2. `udp://132.226.6.145:6969/announce` — score=91.9, 152ms, 存活率87%
3. `https://t.213891.xyz:443/announce` — score=87.7, 34ms, 存活率59%
4. `http://207.241.231.226:6969/announce` — score=85.3, 130ms, 存活率59%
5. `udp://exodus.desync.com:6969/announce` — score=83.4, 68ms, 存活率45%
6. `udp://135.125.198.235:1984/announce` — score=82.3, 92ms, 存活率41%
7. `http://207.241.226.111:6969/announce` — score=77.0, 121ms, 存活率29%
8. `udp://tracker2.dler.org:80/announce` — score=70.1, 184ms, 存活率22%
9. `http://tracker.renfei.net:8080/announce` — score=70.0, 28ms, 存活率0%
10. `udp://34.66.57.33:1337/announce` — score=70.0, 29ms, 存活率0%
11. `udp://209.141.59.25:6969/announce` — score=70.0, 62ms, 存活率0%
12. `udp://explodie.org:6969/announce` — score=70.0, 83ms, 存活率0%
13. `udp://43.250.54.126:6969/announce` — score=70.0, 87ms, 存活率0%
14. `udp://45.137.199.107:6969/announce` — score=70.0, 88ms, 存活率0%
15. `udp://93.158.213.92:6969/announce` — score=70.0, 89ms, 存活率0%
16. `udp://109.201.134.183:80/announce` — score=70.0, 89ms, 存活率0%
17. `udp://open.stealth.si:80/announce` — score=70.0, 97ms, 存活率0%
18. `udp://89.234.156.205:451/announce` — score=70.0, 97ms, 存活率0%
19. `udp://31.38.161.123:6969/announce` — score=69.7, 103ms, 存活率0%
20. `udp://tracker.torrent.eu.org:451/announce` — score=69.0, 113ms, 存活率0%

## 失效 Tracker

- `http://echostar.ddnsfree.com:8080/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://retracker.hotplug.ru:2710/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://torrentsmd.com:8080/announce` — HTTPError: HTTP Error 403: Forbidden
- `http://tracker.opentorrent.top:6969/announce` — URLError: <urlopen error timed out>
- `http://tracker.plx.im:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://tracker.therarbg.to:6969/announce` — URLError: <urlopen error timed out>
- `http://tracker.xn--djrq4gl4hvoi.top:80/announce` — ConnectionResetError: [Errno 104] Connection reset by peer
- `http://tracker2.itzmx.com:6961/announce` — URLError: <urlopen error timed out>
- `http://tracker3.itzmx.com:6961/announce` — URLError: <urlopen error timed out>
- `http://tracker4.itzmx.com:2710/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tracker1.520.jp:443/announce` — HTTPError: HTTP Error 521: <none>
- `udp://208.83.20.20:6969/announce` — no connect response
- `udp://52.58.128.163:6969/announce` — no connect response
- `udp://tracker.tryhackx.org:6969/announce` — no connect response

## 无法测试（特殊网络）

- `http://[2605:6400:30:fad6::dead:c0d3]:1337/announce` — IPv6 unavailable here
- `http://[2a04:ac00:1:3dd8::1:2710]:2710/announce` — IPv6 unavailable here
- `udp://[2a03:7220:8083:cd00::1]:451/announce` — IPv6 unavailable here

## 同 IP 去重（保留响应最快）

- `http://107.189.2.131:1337/announce`
- `http://211.75.205.188:80/announce`
- `http://211.75.210.221:6969/announce`
- `http://211.75.210.221:80/announce`
- `http://94.23.207.177:6969/announce`
- `http://announce.sktorrent.eu:6969/announce`
- `http://bt1.archive.org:6969/announce`
- `http://bt2.archive.org:6969/announce`
- `http://retracker01-msk-virt.corbina.net:80/announce`
- `http://tracker.auctor.tv:6969/announce`
- `http://tracker.dler.com:6969/announce`
- `http://tracker.dler.org:6969/announce`
- `http://tracker.nyaa.vc:6969/announce`
- `http://tracker.opentrackr.org:1337/announce`
- `http://tracker.qu.ax:6969/announce`
- `http://tracker2.dler.org:80/announce`
- `https://1337.abcvg.info:443/announce`
- `udp://151.242.104.187:80/announce`
- `udp://23.157.120.14:6969/announce`
- `udp://34.66.57.33:80/announce`
- `udp://83.102.180.21:80/announce`
- `udp://93.158.213.92:1337/announce`
- `udp://open.demonii.com:1337/announce`
- `udp://tracker-udp.gbitt.info:80/announce`
- `udp://tracker.bittor.pw:1337/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.ducks.party:1984/announce`
- `udp://tracker.gmi.gd:6969/announce`
- `udp://tracker.nyaa.vc:6969/announce`
- `udp://tracker.opentrackr.org:1337/announce`
- `udp://tracker.qu.ax:6969/announce`
- `udp://tracker.skynetcloud.site:6969/announce`
