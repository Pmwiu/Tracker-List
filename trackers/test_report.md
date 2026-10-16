# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-16 11:42:38 UTC
- 总 Tracker 数: 320
- 存活 (alive): **145** (45%)
- 失效 (dead): **155**
- 不安全 (unsafe): **3**
- 无法测试 (untestable): 17
- 低速淘汰 (low-speed >5s): 0
- 同网段/同域名去重 (kept fastest): 74
- 综合评分后保留前 25 个，淘汰 46 个
- 评分维度: 速度 50% + 历史稳定性 20% + 响应质量 15%（含 peers 计数与 scrape 热度） + 跨源一致性 10% + 近期成功率 5%（速度标度自适应 + 经典高可用加分 + 反退化）
- 配额: 保底 4 条非 UDP + 保底 4 条经典高可用
- 协议多样性配额: 保底 4 条非 UDP，实际保留 10 条
- 耗时: 61.8 秒

## 协议分布

- udp: 93
- http: 39
- https: 13

## 最终订阅列表（前 25 个，按综合评分降序）

1. `https://tracker.nekomi.cn:443/announce` — score=97.4, 36ms, 存活率100%, 质量95, 经典+0
2. `https://t.213891.xyz:443/announce` — score=96.8, 34ms, 存活率100%, 质量90, 经典+0
3. `http://207.241.226.111:6969/announce` — score=94.9, 35ms, 存活率100%, 质量98, 经典+0
4. `http://207.241.231.226:6969/announce` — score=94.4, 38ms, 存活率100%, 质量95, 经典+0
5. `udp://open.demonii.com:1337/announce` — score=93.5, 131ms, 存活率100%, 质量60, 经典+6
6. `https://1.tracker.eu.org:443/announce` — score=93.4, 41ms, 存活率100%, 质量90, 经典+0
7. `udp://open.stealth.si:80/announce` — score=92.9, 142ms, 存活率100%, 质量60, 经典+6
8. `udp://tracker.torrent.eu.org:451/announce` — score=92.6, 138ms, 存活率97%, 质量60, 经典+6
9. `udp://open.ftorrent.com:443/announce` — score=92.2, 35ms, 存活率100%, 质量60, 经典+0
10. `https://tracker.zhuqiy.com:443/announce` — score=91.8, 122ms, 存活率93%, 质量95, 经典+0
11. `udp://evan.im:6969/announce` — score=91.5, 49ms, 存活率100%, 质量60, 经典+0
12. `https://tracker.7471.top:443/announce` — score=89.0, 191ms, 存活率100%, 质量90, 经典+0
13. `http://004430.xyz:80/announce` — score=87.9, 28ms, 存活率100%, 质量95, 经典+0
14. `udp://tracker.qu.ax:6969/announce` — score=87.5, 131ms, 存活率100%, 质量60, 经典+0
15. `udp://tracker-udp.gbitt.info:80/announce` — score=87.4, 132ms, 存活率100%, 质量60, 经典+0
16. `udp://martin-gebhardt.eu:25/announce` — score=87.1, 137ms, 存活率100%, 质量60, 经典+0
17. `udp://tracker.nyaa.vc:6969/announce` — score=86.9, 142ms, 存活率100%, 质量60, 经典+0
18. `udp://kolankoalastree.newtrackon.co.nz:1337/announce` — score=86.7, 145ms, 存活率100%, 质量60, 经典+0
19. `udp://tracker.004430.xyz:1337/announce` — score=86.6, 8ms, 存活率100%, 质量60, 经典+0
20. `https://3.tracker.eu.org:443/announce` — score=86.5, 40ms, 存活率100%, 质量90, 经典+0
21. `udp://tracker.farted.net:6969/announce` — score=86.3, 154ms, 存活率100%, 质量60, 经典+0
22. `udp://t.overflow.biz:6969/announce` — score=86.3, 153ms, 存活率100%, 质量60, 经典+0
23. `http://216.144.239.90:6969/announce` — score=85.7, 17ms, 存活率87%, 质量95, 经典+0
24. `udp://opentracker.lain.moscow:6969/announce` — score=85.4, 148ms, 存活率97%, 质量60, 经典+0
25. `udp://exodus.desync.com:6969/announce` — score=83.3, 24ms, 存活率37%, 质量60, 经典+6

## 失效 Tracker

- `http://00.mercax.com:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://00.xxtor.com:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://0205.uptm.ch:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://104.143.10.186:8000/announce` — URLError: <urlopen error timed out>
- `http://104.244.77.14:1337/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://104.28.1.30:8080/announce` — URLError: <urlopen error timed out>
- `http://104.28.16.69:80/announce` — URLError: <urlopen error timed out>
- `http://106.14.254.164:6969/announce` — URLError: <urlopen error timed out>
- `http://107.150.14.110:6969/announce` — URLError: <urlopen error timed out>
- `http://107.152.127.9:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://107.189.10.20.sslip.io:7777/announce` — URLError: <urlopen error timed out>
- `http://107.189.31.134:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://107.189.7.143:6969/announce` — URLError: <urlopen error timed out>
- `http://109.121.134.121:1337/announce` — URLError: <urlopen error timed out>
- `http://114.55.113.60:6969/announce` — URLError: <urlopen error timed out>
- `http://116.252.176.125:6969/announce` — URLError: <urlopen error timed out>
- `http://116.9.207.121:6969/announce` — URLError: <urlopen error timed out>
- `http://116.9.207.164:6969/announce` — URLError: <urlopen error timed out>
- `http://116.9.207.198:6969/announce` — URLError: <urlopen error timed out>
- `http://116.9.207.226:6969/announce` — URLError: <urlopen error timed out>
- `http://119.28.71.45:8080/announce` — URLError: <urlopen error timed out>
- `http://125.227.35.196:6969/announce` — URLError: <urlopen error timed out>
- `http://128.199.70.66:5944/announce` — URLError: <urlopen error timed out>
- `http://129.146.193.240:6699/announce` — URLError: <urlopen error timed out>
- `http://13.115.115.32:6969/announce` — URLError: <urlopen error timed out>
- `http://140.82.21.192:8080/announce` — URLError: <urlopen error timed out>
- `http://141.144.224.250:2710/announce` — URLError: <urlopen error timed out>
- `http://141.144.224.250:6969/announce` — URLError: <urlopen error timed out>
- `http://144.202.33.210:6961/announce` — URLError: <urlopen error timed out>
- `http://144.76.118.107:6969/announce` — URLError: <urlopen error timed out>
- `http://147job.com:6969/announce` — URLError: <urlopen error timed out>
- `http://151.115.49.115:1337/announce` — URLError: <urlopen error timed out>
- `http://155.248.200.105:80/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://156.234.201.18:80/announce` — URLError: <urlopen error timed out>
- `http://185.148.3.231:80/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://34.66.57.33:11450/announce` — timeout
- `http://34.66.57.33:80/announce` — timeout
- `http://504e163a.host.njalla.net:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://66691337.xyz:6969/announce` — URLError: <urlopen error timed out>
- `http://79.111.12.213:6969/announce` — timeout
- `http://aaa.army:8866/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://aboutbeautifulgallopinghorsesinthegreenpasture.online:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://anisource.spb.ru:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://asiatorrent.ddns.net:51413/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `http://bigfoot1942.sektori.org:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bittorrent.kali.org:80/announce` — restricted (failure reason)
- `http://bobbialbano.com:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://bt.3kb.xyz:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bt.dl1234.com:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bt.endpot.com:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bt.henbt.com:2710/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bt.ktkj.com:8080/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bt.publicvm.com:8080/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bt.pusacg.org:8080/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `http://bt.rghost.net:80/announce` — timeout
- `http://bt.xcty.eu.org:2095/announce` — timeout
- `http://bt1.letpo.com:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bt2.careland.com.cn:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://bughome.de:2832/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://bvarf.tracker.sh:2086/announce` — timeout
- `http://canardscitrons.nohost.me:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://chihaya.de:80/announce` — URLError: <urlopen error timed out>
- `http://chouchou.top:8080/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://cloud.nyap2p.com:8080/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://cn.pcfreetime.com:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://de7c0e7a567e.sn.mynetname.net:59002/announce` — URLError: <urlopen error timed out>
- `http://debuz.com:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://dht.dhtclub.com:666/announce` — URLError: <urlopen error timed out>
- `http://dn42.smrsh.net:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://echostar.ddnsfree.com:8080/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://ehtracker.org:80/1104308/announce` — restricted (failure reason)
- `http://ehtracker.org:80/1113709/announce` — restricted (failure reason)
- `http://ehtracker.org:80/1226599/1080494xo5eXcwFOBq/announce` — restricted (failure reason)
- `http://ehtracker.org:80/2496841/announce` — restricted (failure reason)
- `http://ehtracker.org:80/2541477/announce` — restricted (failure reason)
- `http://ehtracker.org:80/2566145/1159106xUfsJkT9Btg/announce` — restricted (failure reason)
- `http://explodie.org:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://fe.dealclub.de:6969/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `http://fleira.no:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://fosstorrents.com:6969/announce` — URLError: <urlopen error timed out>
- `http://frp.v2fy.com:8000/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://ftp.pet:2710/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://ftp.pet:6969/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://ftp.pet:7777/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://ftp.pet:999/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://fxtt.ru:80/announce` — URLError: <urlopen error timed out>
- `http://grifon.info:80/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://highteahop.top:6960/announce` — ConnectionResetError: [Errno 104] Connection reset by peer
- `http://home.kray.pw:6969/announce` — URLError: <urlopen error timed out>
- `http://houniao.ddns.net:8888/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `http://hzzwly.gq:6969/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `http://i.bandito.org:80/announce.php` — HTTPError: HTTP Error 403: Forbidden
- `http://retracker.hotplug.ru:2710/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://ht.therarbg.to:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://raw.githubusercontent.com:443/mrgusux/automatic-trackers/main/api/stats.json` — invalid bencoded response
- `https://raw.githubusercontent.com:443/mrgusux/automatic-trackers/main/api/trackers.json` — invalid bencoded response
- `https://raw.githubusercontent.com:443/mrgusux/automatic-trackers/main/trackers.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/ngosang/trackerslist/master/trackers_all.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/ngosang/trackerslist/master/trackers_all_http.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/ngosang/trackerslist/master/trackers_all_https.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/ngosang/trackerslist/master/trackers_all_i2p.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/ngosang/trackerslist/master/trackers_all_ip.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/ngosang/trackerslist/master/trackers_all_udp.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/ngosang/trackerslist/master/trackers_all_ws.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/ngosang/trackerslist/master/trackers_all_yggdrasil.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/ngosang/trackerslist/master/trackers_all_yggdrasil_ip.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/ngosang/trackerslist/master/trackers_best.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/ngosang/trackerslist/master/trackers_best_ip.txt` — invalid bencoded response
- `https://raw.githubusercontent.com:443/xXSalamanderXx/salamander-trackers/refs/heads/main/combined.txt` — invalid bencoded response
- `https://sheraza2895.github.io:443` — invalid bencoded response
- `https://shields.io:443/badges/endpoint-badge` — invalid bencoded response
- `https://simeon-vanov.github.io:443/cortiq-public` — invalid bencoded response
- `https://tixati.com:443/news` — invalid bencoded response
- `https://token.actions.githubusercontent.com:443` — HTTPError: HTTP Error 404: Not Found
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.bt4g.com:443/announce` — timeout
- `https://tracker.bug38.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tracker.bug38.com'. (_ssl.c:1010)>
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://webtorrent.io:443` — invalid bencoded response
- `https://www.cloudflare.com:443/ips` — invalid bencoded response
- `https://yggdrasil-network.github.io:443` — invalid bencoded response
- `udp://52.211.139.85:27022/announce` — announce no response
- `udp://52.58.128.163:6969/announce` — no connect response
- `udp://60.172.236.18:6969/announce` — no connect response
- `udp://6ahddutb1ucc3cp.ru:6969/announce` — no connect response
- `udp://archive.torrentonline.cc:42069/announce` — no connect response
- `udp://ipv6.govt.hu:6969/announce` — no connect response
- `udp://open.tracker.ink:6969/announce` — no connect response
- `udp://opentor.org:2710/announce` — no connect response
- `udp://p4p.arenabg.com:1337/announce` — no connect response
- `udp://retracker.hotplug.ru:2710/announce` — no connect response
- `udp://torrentclub.online:54123/announce` — no connect response
- `udp://torrents.tmtime.dev:6969/announce` — no connect response
- `udp://tracker.alaskantf.com:6969/announce` — no connect response
- `udp://tracker.filemail.com:6969/announce` — announce no response
- `udp://tracker.flatuslifir.is:6969/announce` — no connect response
- `udp://tracker.fnix.net:6969/announce` — no connect response
- `udp://tracker.skyts.net:6969/announce` — no connect response
- `udp://tracker.srv00.com:6969/announce` — no connect response
- `udp://tracker.theoks.net:6969/announce` — no connect response
- `udp://tracker.wepzone.net:6969/announce` — no connect response
- `udp://tracker.yume-hatsuyuki.moe:6969/announce` — no connect response
- `udp://tracker1.itzmx.com:8080/announce` — no connect response
- `udp://tracker1.myporn.club:9337/announce` — no connect response
- `udp://wepzone.net:6969/announce` — no connect response
- `udp://whybother.torrentonline.cc:42069/announce` — no connect response
- `udp://yuptracker-eu.gaijinent.com:27022/announce` — announce no response
- `wss://open.ftorrent.com:443` — SSLError: [SSL: TLSV1_UNRECOGNIZED_NAME] tlsv1 unrecognized name (_ssl.c:1010)
- `wss://tracker.openwebtorrent.com:443` — SSLError: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1010)
- `wss://tracker.openwebtorrent.com:443/announce` — SSLError: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1010)
- `wss://tracker.webtorrent.dev:443` — SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: IP address mismatch, certificate is not valid for '49.13.90.136'. (_ssl.c:1010)

## 不安全 Tracker（已过滤）

- `http://alpha.torrenttracker.nl:443/announce` — resolves to private IP: ::1
- `http://yggtracker.i2p.rocks:80/announce` — resolves to private IP: 200:1e2f:e608:eb3a:2bf:1e62:87ba:e2f7
- `udp://open.dstud.io:6969/announce` — resolves to private IP: 0.0.0.0

## 无法测试（特殊网络）

- `http://btrackrqkjp6kgelov5a3uxisis77ofxqt5nvy5hvvtoybjpmq4q.b32.i2p:80/announce` — I2P network required
- `http://freetracker.i2p:7331/announce` — I2P network required
- `http://nyaaplus.i2p:80/announce` — I2P network required
- `http://opentracker.dg2.i2p:80/a` — I2P network required
- `http://opentracker.eeptorrent.i2p:80/a` — I2P network required
- `http://opentracker.fattydove.i2p:80/a` — I2P network required
- `http://opentracker.r4sas.i2p:80/a` — I2P network required
- `http://opentracker.simp.i2p:80/a` — I2P network required
- `http://opentracker.skank.i2p:80/a` — I2P network required
- `http://qimlze77z7w32lx2ntnwkuqslrzlsqy7774v3urueuarafyqik5a.b32.i2p:80/a` — I2P network required
- `http://sigmatracker.i2p:80/a` — I2P network required
- `http://tracker.insulaocculta.i2p:80/a` — I2P network required
- `http://tracker.nyaa2p.i2p:80/announce` — I2P network required
- `http://yet-another-public-tracker.i2p:80/announce` — I2P network required
- `udp://freetracker.i2p:1337/announce` — I2P network required
- `udp://opentracker.simp.i2p:6969/a` — I2P network required
- `udp://opentracker.skank.i2p:6969/a` — I2P network required

## 同网段/同域名去重（保留响应最快）

- `http://107.189.2.131:1337/announce`
- `http://1337.abcvg.info:80/announce`
- `http://135.125.198.235:2710/announce`
- `http://135.125.198.235:80/announce`
- `http://140.235.237.23:6969/announce`
- `http://189.18.97.208:6969/announce`
- `http://211.75.205.187:6969/announce`
- `http://211.75.205.187:80/announce`
- `http://211.75.205.188:6969/announce`
- `http://211.75.205.188:80/announce`
- `http://211.75.210.221:6969/announce`
- `http://211.75.210.221:80/announce`
- `http://31.38.161.123:6969/announce`
- `http://43.250.54.126:6969/announce`
- `http://93.158.213.92:1337/announce`
- `http://94.23.207.177:6969/announce`
- `http://announce.sktorrent.eu:6969/announce`
- `http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce`
- `http://ipv4announce.sktorrent.eu:6969/announce`
- `http://open.tracker.cl:1337/announce`
- `http://opentracker.xyz:80/announce`
- `http://retracker01-msk-virt.corbina.net:80/announce`
- `http://tracker.auctor.tv:6969/announce`
- `http://tracker.dler.com:6969/announce`
- `http://tracker.dler.org:6969/announce`
- `http://tracker.nyaa.vc:6969/announce`
- `http://tracker.opentrackr.org:1337/announce`
- `http://tracker.qu.ax:6969/announce`
- `http://tracker.waaa.moe:6969/announce`
- `http://tracker2.dler.org:80/announce`
- `https://004430.xyz:443/announce`
- `https://2.tracker.eu.org:443/announce`
- `https://337hhh.xyz:443/announce`
- `https://4.tracker.eu.org:443/announce`
- `udp://109.201.134.183:80/announce`
- `udp://149.106.106.25:443/announce`
- `udp://151.242.104.187:80/announce`
- `udp://160.30.240.158:1337/announce`
- `udp://185.121.168.96:1337/announce`
- `udp://185.216.179.62:25/announce`
- `udp://189.18.97.208:6969/announce`
- `udp://192.99.100.68:6969/announce`
- `udp://193.187.90.12:6969/announce`
- `udp://211.75.205.188:80/announce`
- `udp://212.42.38.197:6969/announce`
- `udp://23.94.174.203:1337/announce`
- `udp://31.56.179.159:6969/announce`
- `udp://31.59.141.120:6969/announce`
- `udp://34.66.57.33:1337/announce`
- `udp://43.250.54.126:6969/announce`
- `udp://45.137.199.107:6969/announce`
- `udp://51.222.82.36:6969/announce`
- `udp://65.109.28.17:6969/announce`
- `udp://65.109.28.33:6969/announce`
- `udp://74.119.149.136:6969/announce`
- `udp://83.102.180.21:80/announce`
- `udp://89.234.156.205:451/announce`
- `udp://93.158.213.92:1337/announce`
- `udp://95.217.80.20:6969/announce`
- `udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce`
- `udp://explodie.org:6969/announce`
- `udp://ipv4announce.sktorrent.eu:6969/announce`
- `udp://seedpeer.net:6969/announce`
- `udp://tracker.bittor.pw:1337/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.dler.org:6969/announce`
- `udp://tracker.ducks.party:1984/announce`
- `udp://tracker.gmi.gd:6969/announce`
- `udp://tracker.k.vu:6969/announce`
- `udp://tracker.opentrackr.org:1337/announce`
- `udp://tracker.peerfect.org:6969/announce`
- `udp://tracker.skynetcloud.site:6969/announce`
- `udp://tracker.torrents.observer:80/announce`
- `udp://tracker2.dler.org:80/announce`

## Discovery（自动发现的候选，Phase 1 隔离，不进 best/all）

- 候选总数: 158
- 通过探活: 38
- 若允许参与排名会入选的（前 10 条）:
  - `udp://180.131.145.175:6969/announce`
  - `udp://164.152.110.70:6969/announce`
  - `udp://ns575949.ip-51-222-82.net:6969/announce`
  - `udp://bt-tracker.de:6969/announce`
  - `udp://178.239.19.29:80/announce`
  - `udp://tracker.okade.pro:1337/announce`
  - `udp://94.23.207.177:6969/announce`
  - `udp://107.189.2.131:1337/announce`
  - `udp://47.76.201.250:6969/announce`
  - `udp://tracker.ddunlimited.net:6969/announce`

转正方式：人工 review 后加入 `scripts/update_trackers.py` 的 SOURCES，或写进 `trackers/discovered/PROMOTE.md`（Phase 2）。


## 备选库（trackers_reserve.txt，前 20 条，按评分降序）

独立于 best/all 的候选订阅源，供人工审查转正。
1. `udp://23.94.174.203:1337/announce`
2. `udp://180.131.145.175:6969/announce`
3. `udp://seedpeer.net:6969/announce`
4. `udp://149.106.106.25:443/announce`
5. `udp://74.119.149.136:6969/announce`
6. `udp://164.152.110.70:6969/announce`
7. `udp://ns575949.ip-51-222-82.net:6969/announce`
8. `udp://192.99.100.68:6969/announce`
9. `udp://51.222.82.36:6969/announce`
10. `udp://bt-tracker.de:6969/announce`
11. `udp://178.239.19.29:80/announce`
12. `udp://tracker.torrents.observer:80/announce`
13. `udp://tracker.okade.pro:1337/announce`
14. `udp://94.23.207.177:6969/announce`
15. `udp://185.216.179.62:25/announce`
16. `udp://107.189.2.131:1337/announce`
17. `udp://211.75.205.188:80/announce`
18. `udp://160.30.240.158:1337/announce`
19. `udp://47.76.201.250:6969/announce`
20. `udp://tracker.ddunlimited.net:6969/announce`

