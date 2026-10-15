# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-15 17:14:53 UTC
- 总 Tracker 数: 320
- 存活 (alive): **116** (36%)
- 失效 (dead): **179**
- 不安全 (unsafe): **8**
- 无法测试 (untestable): 17
- 低速淘汰 (low-speed >5s): 0
- 同网段/同域名去重 (kept fastest): 59
- 综合评分后保留前 25 个，淘汰 32 个
- 评分维度: 速度 50% + 历史稳定性 20% + 响应质量 15%（含 peers 计数与 scrape 热度） + 跨源一致性 10% + 近期成功率 5%（速度标度自适应 + 经典高可用加分 + 反退化）
- 配额: 保底 4 条非 UDP + 保底 4 条经典高可用
- 协议多样性配额: 保底 4 条非 UDP，实际保留 8 条
- 耗时: 131.8 秒

## 协议分布

- udp: 64
- http: 41
- https: 11

## 最终订阅列表（前 25 个，按综合评分降序）

1. `http://tracker.renfei.net:8080/announce` — score=98.0, 26ms, 存活率100%, 质量95, 经典+0
2. `udp://open.stealth.si:80/announce` — score=95.4, 92ms, 存活率100%, 质量60, 经典+6
3. `udp://evan.im:6969/announce` — score=93.9, 2ms, 存活率100%, 质量60, 经典+0
4. `https://1.tracker.eu.org:443/announce` — score=93.4, 42ms, 存活率100%, 质量90, 经典+0
5. `udp://tracker.bittor.pw:1337/announce` — score=92.8, 24ms, 存活率100%, 质量60, 经典+0
6. `udp://open.ftorrent.com:443/announce` — score=91.7, 45ms, 存活率100%, 质量60, 经典+0
7. `https://tracker.7471.top:443/announce` — score=91.3, 145ms, 存活率100%, 质量90, 经典+0
8. `https://tracker.nekomi.cn:443/announce` — score=90.6, 172ms, 存活率100%, 质量95, 经典+0
9. `udp://tracker.qu.ax:6969/announce` — score=89.9, 81ms, 存活率100%, 质量60, 经典+0
10. `udp://tracker.nyaa.vc:6969/announce` — score=89.8, 83ms, 存活率100%, 质量60, 经典+0
11. `http://207.241.226.111:6969/announce` — score=89.7, 131ms, 存活率100%, 质量95, 经典+0
12. `http://207.241.231.226:6969/announce` — score=89.6, 134ms, 存活率100%, 质量95, 经典+0
13. `udp://martin-gebhardt.eu:25/announce` — score=89.1, 96ms, 存活率100%, 质量60, 经典+0
14. `udp://t.overflow.biz:6969/announce` — score=88.1, 115ms, 存活率99%, 质量60, 经典+0
15. `udp://opentracker.lain.moscow:6969/announce` — score=87.2, 99ms, 存活率93%, 质量60, 经典+0
16. `https://3.tracker.eu.org:443/announce` — score=86.5, 40ms, 存活率100%, 质量90, 经典+0
17. `https://t.213891.xyz:443/announce` — score=85.3, 265ms, 存活率100%, 质量90, 经典+0
18. `udp://tracker.dler.org:6969/announce` — score=84.6, 189ms, 存活率100%, 质量60, 经典+0
19. `udp://tracker2.dler.org:80/announce` — score=84.5, 190ms, 存活率100%, 质量60, 经典+0
20. `udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce` — score=84.1, 177ms, 存活率97%, 质量60, 经典+0
21. `udp://tracker.004430.xyz:1337/announce` — score=84.0, 60ms, 存活率100%, 质量60, 经典+0
22. `udp://109.201.134.183:80/announce` — score=82.9, 82ms, 存活率100%, 质量60, 经典+0
23. `udp://kolankoalastree.newtrackon.co.nz:1337/announce` — score=82.9, 219ms, 存活率99%, 质量60, 经典+0
24. `udp://ipv4announce.sktorrent.eu:6969/announce` — score=82.7, 86ms, 存活率100%, 质量60, 经典+0
25. `udp://93.158.213.92:6969/announce` — score=82.6, 86ms, 存活率100%, 质量60, 经典+0

## 失效 Tracker

- `http://157.7.202.64:8080/announce` — URLError: <urlopen error timed out>
- `http://157.90.169.123:80/announce` — HTTPError: HTTP Error 404: Not Found
- `http://158.101.137.177:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://158.69.146.212:7777/announce` — URLError: <urlopen error timed out>
- `http://159.69.65.157:6969/announce` — URLError: <urlopen error timed out>
- `http://160.251.78.190:6969/announce` — URLError: <urlopen error timed out>
- `http://163.172.209.40:80/announce` — URLError: <urlopen error timed out>
- `http://163.172.29.130:80/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://167.235.245.209:80/announce` — HTTPError: HTTP Error 404: Not Found
- `http://167.253.78.20:8080/announce` — URLError: <urlopen error timed out>
- `http://171.104.110.193:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://171.104.110.21:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://171.104.110.88:6969/announce` — URLError: <urlopen error timed out>
- `http://171.104.110.95:6969/announce` — URLError: <urlopen error timed out>
- `http://171.104.111.14:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://171.104.111.201:6969/announce` — URLError: <urlopen error timed out>
- `http://171.104.111.20:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://171.104.111.250:6969/announce` — URLError: <urlopen error timed out>
- `http://171.104.111.30:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://171.104.111.83:6969/announce` — URLError: <urlopen error timed out>
- `http://171.104.111.89:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://171.104.226.15:6969/announce` — URLError: <urlopen error timed out>
- `http://171.104.226.221:6969/announce` — URLError: <urlopen error timed out>
- `http://171.104.226.25:6969/announce` — URLError: <urlopen error timed out>
- `http://171.104.226.31:6969/announce` — URLError: <urlopen error timed out>
- `http://171.104.226.87:6969/announce` — URLError: <urlopen error timed out>
- `http://173.254.204.71:1096/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://178.175.143.27:80/announce` — URLError: <urlopen error timed out>
- `http://178.33.73.26:2710/announce` — URLError: <urlopen error timed out>
- `http://179.100.24.134:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://180.139.151.58:6969/announce` — URLError: <urlopen error timed out>
- `http://180.97.219.76:8070/announce` — URLError: <urlopen error timed out>
- `http://182.176.139.129:6969/announce` — URLError: <urlopen error timed out>
- `http://185.130.47.2:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://185.148.3.231:80/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://185.185.40.51:6969/announce` — URLError: <urlopen error timed out>
- `http://185.185.40.95:6969/announce` — URLError: <urlopen error timed out>
- `http://185.197.195.20:1919/announce` — URLError: <urlopen error timed out>
- `http://185.216.178.49:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://185.230.4.150:1337/announce` — URLError: <urlopen error timed out>
- `http://185.232.169.109:80/announce` — URLError: <urlopen error timed out>
- `http://185.5.97.139:8089/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://185.70.187.79:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://187.57.14.62:6969/announce` — URLError: <urlopen error timed out>
- `http://188.165.253.109:1337/announce` — URLError: <urlopen error timed out>
- `http://189.0.196.51:6969/announce` — URLError: <urlopen error timed out>
- `http://189.110.233.96:6969/announce` — URLError: <urlopen error timed out>
- `http://192.3.165.191:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://192.9.228.30:6699/announce` — URLError: <urlopen error timed out>
- `http://193.37.214.12:6969/announce` — URLError: <urlopen error timed out>
- `http://194.106.216.222:80/announce` — URLError: <urlopen error timed out>
- `http://195.123.209.37:1337/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://198.251.84.144:80/announce` — URLError: <urlopen error timed out>
- `http://200.232.254.1:6969/announce` — URLError: <urlopen error timed out>
- `http://201.42.214.55:6969/announce` — URLError: <urlopen error timed out>
- `http://201.43.209.254:6969/announce` — URLError: <urlopen error timed out>
- `http://207.246.118.100:6961/announce` — URLError: <urlopen error timed out>
- `http://207.246.79.17:2710/announce` — URLError: <urlopen error timed out>
- `http://207.246.79.17:6961/announce` — URLError: <urlopen error timed out>
- `http://207.246.79.17:8080/announce` — URLError: <urlopen error timed out>
- `http://209.209.112.121:2710/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://210.244.71.25:6969/announce` — URLError: <urlopen error timed out>
- `http://210.244.71.26:6969/announce` — URLError: <urlopen error timed out>
- `http://211.20.122.47:6969/announce` — URLError: <urlopen error timed out>
- `http://211.22.29.93:80/announce` — URLError: <urlopen error timed out>
- `http://211.75.29.254:6969/announce` — URLError: <urlopen error timed out>
- `http://212.6.3.67:80/announce` — URLError: <urlopen error timed out>
- `http://213.163.67.56:1337/announce` — URLError: <urlopen error timed out>
- `http://217.30.10.18:6969/announce` — URLError: <urlopen error timed out>
- `http://217.30.10.77:6969/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `http://220.130.15.27:6969/announce` — URLError: <urlopen error timed out>
- `http://220.130.15.30:6969/announce` — URLError: <urlopen error timed out>
- `http://34.66.57.33:1337/announce` — URLError: <urlopen error timed out>
- `http://bittorrent.kali.org:80/announce` — restricted (failure reason)
- `http://echostar.ddnsfree.com:8080/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://ehtracker.org:80/1104308/announce` — restricted (failure reason)
- `http://ehtracker.org:80/1113709/announce` — restricted (failure reason)
- `http://ehtracker.org:80/1226599/1080494xo5eXcwFOBq/announce` — restricted (failure reason)
- `http://ehtracker.org:80/2496841/announce` — restricted (failure reason)
- `http://ehtracker.org:80/2541477/announce` — restricted (failure reason)
- `http://ehtracker.org:80/2566145/1159106xUfsJkT9Btg/announce` — restricted (failure reason)
- `http://h4.trakx.nibba.trade:80/announce` — timeout
- `http://retracker.hotplug.ru:2710/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://ht.therarbg.to:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.bt4g.com:443/announce` — timeout
- `https://tracker.foreverpirates.co:443/announce` — timeout
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `udp://6ahddutb1ucc3cp.ru:6969/announce` — no connect response
- `udp://exodus.desync.com:6969/announce` — no connect response
- `udp://open.tracker.ink:6969/announce` — no connect response
- `udp://opentor.org:2710/announce` — no connect response
- `udp://p4p.arenabg.com:1337/announce` — no connect response
- `udp://retracker.hotplug.ru:2710/announce` — no connect response
- `udp://torrentclub.online:54123/announce` — no connect response
- `udp://torrents.tmtime.dev:6969/announce` — no connect response
- `udp://tracker.alaskantf.com:6969/announce` — no connect response
- `udp://tracker.kicks-ass.net:80/announce` — no connect response
- `udp://tracker.kuroy.me:5944/announce` — no connect response
- `udp://tracker.lelux.fi:6969/announce` — no connect response
- `udp://tracker.mg64.net:2710/announce` — no connect response
- `udp://tracker.mg64.net:6969/announce` — no connect response
- `udp://tracker.monitorit4.me:6969/announce` — no connect response
- `udp://tracker.nexusstream.eu:6969/announce` — no connect response
- `udp://tracker.ololosh.space:6969/announce` — no connect response
- `udp://tracker.openbittorrent.com:80/announce` — no connect response
- `udp://tracker.openbtba.com:6969/announce` — no connect response
- `udp://tracker.opentorrent.top:6969/announce` — no connect response
- `udp://tracker.piratepublic.com:1337/announce` — no connect response
- `udp://tracker.plx.im:6969/announce` — no connect response
- `udp://tracker.ptrmc.net:6969/announce` — no connect response
- `udp://tracker.riverarmy.xyz:6969/announce` — no connect response
- `udp://tracker.silksa.co.za:6969/announce` — no connect response
- `udp://tracker.sktorrent.net:6969/announce` — no connect response
- `udp://tracker.srv00.com:6969/announce` — no connect response
- `udp://tracker.swateam.org.uk:2710/announce` — no connect response
- `udp://tracker.sylphix.com:6969/announce` — no connect response
- `udp://tracker.t-1.org:6969/announce` — no connect response
- `udp://tracker.tcp.exchange:6969/announce` — no connect response
- `udp://tracker.theoks.net:6969/announce` — no connect response
- `udp://tracker.tiny-vps.com:6969/announce` — no connect response
- `udp://tracker.tnl.one:8000/announce` — no connect response
- `udp://tracker.torrentclaw.com:1337/announce` — no connect response
- `udp://tracker.torrust-demo.com:6969/announce` — no connect response
- `udp://tracker.trackarr.org:6969/announce` — no connect response
- `udp://tracker.trackerfix.com:80/announce` — no connect response
- `udp://tracker.trackerfix.com:82/announce` — no connect response
- `udp://tracker.tvunderground.org.ru:3218/announce` — no connect response
- `udp://tracker.valete.tf:9999/announce` — no connect response
- `udp://tracker.vds.nz:6969/announce` — no connect response
- `udp://tracker.wepzone.net:6969/announce` — no connect response
- `udp://tracker.x6c.co:6969/announce` — no connect response
- `udp://tracker.yangxiaoguozi.cn:6969/announce` — no connect response
- `udp://tracker.yoshi210.com:6969/announce` — no connect response
- `udp://tracker.zaluan.xyz:6969/announce` — no connect response
- `udp://tracker.zemoj.com:6969/announce` — no connect response
- `udp://tracker.zerobytes.xyz:1337/announce` — no connect response
- `udp://tracker1.bt.moack.co.kr:80/announce` — no connect response
- `udp://tracker1.itzmx.com:8080/announce` — no connect response
- `udp://tracker1.myporn.club:9337/announce` — no connect response
- `udp://tracker2.indowebster.com:6969/announce` — no connect response
- `udp://tracker4.piratux.com:6969/announce` — no connect response
- `udp://trackthis.cyber.pz.it:1337/announce` — no connect response
- `udp://tsundere.pw:6969/announce` — no connect response
- `udp://ttk2.nbaonlineservice.com:6969/announce` — no connect response
- `udp://uabits.today:6990/announce` — no connect response
- `udp://udp-tracker.adgk.net:6969/announce` — no connect response
- `udp://udp.tracker.linvk.com:6969/announce` — no connect response
- `udp://udp1.torrust-tracker-demo.com:6969/announce` — no connect response
- `udp://uploads.gamecoast.net:6969/announce` — no connect response
- `udp://v1046920.hosted-by-vdsina.ru:6969/announce` — no connect response
- `udp://v6.vito-tracker.space:6969/announce` — no connect response
- `udp://v74853.hosted-by-vdsina.com:6969/announce` — no connect response
- `udp://vibe.sleepyinternetfun.xyz:1738/announce` — no connect response
- `udp://vps-dd0a0715.vps.ovh.net:6969/announce` — no connect response
- `udp://wepzone.net:6969/announce` — no connect response
- `udp://www.2600.com:6969/announce` — no connect response
- `udp://www.peckservers.com:9000/announce` — no connect response
- `udp://yahor.ftp.sh:6969/announce` — no connect response
- `udp://yahor.of.by:6969/announce` — no connect response
- `udp://yann5.hexanyn.fr:6969/announce` — no connect response
- `udp://yuki.bt.bontal.net:6969/announce` — no connect response
- `udp://yuptracker-sa.gaijinent.com:27022/announce` — announce no response
- `udp://yuptracker-us.gaijinent.com:27022/announce` — announce no response
- `udp://yuptracker.gaijinent.com:27022/announce` — announce no response
- `udp://z.mercax.com:53/announce` — no connect response
- `udp://zecircle.xyz:6969/announce` — no connect response
- `udp://zer0day.to:1337/announce` — no connect response
- `wss://qot.abiir.top:443/announce` — SSLEOFError: [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)
- `wss://spacetradersapi-chatbox.herokuapp.com:443/announce` — SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: IP address mismatch, certificate is not valid for '15.197.132.233'. (_ssl.c:1010)
- `wss://tracker.dnlab.net:443/announce` — OSError: [Errno 101] Network is unreachable
- `wss://tracker.files.fm:7073/announce` — SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: IP address mismatch, certificate is not valid for '80.232.242.115'. (_ssl.c:1010)
- `wss://tracker.magnetoo.io/announce` — SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate (_ssl.c:1010)
- `wss://tracker.openwebtorrent.com/announce` — SSLError: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1010)
- `wss://tracker.openwebtorrent.com:443/announce` — SSLError: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1010)

## 不安全 Tracker（已过滤）

- `http://yggtracker.i2p.rocks:80/announce` — resolves to private IP: 200:1e2f:e608:eb3a:2bf:1e62:87ba:e2f7
- `udp://open.dstud.io:6969/announce` — resolves to private IP: 0.0.0.0
- `udp://tracker.pomf.se:80/announce` — resolves to private IP: 127.0.0.1
- `udp://tracker.teambelgium.net:6969/announce` — resolves to private IP: 127.0.0.1
- `udp://udp.tracker.projectk.org:23333/announce` — resolves to private IP: 127.0.0.1
- `udp://vito-tracker.duckdns.org:6969/announce` — resolves to private IP: 127.0.0.1
- `wss://tracker.btorrent.xyz:443` — resolves to private IP: 127.0.0.1
- `wss://tracker.btorrent.xyz:443/announce` — resolves to private IP: 127.0.0.1

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
- `http://tracker.mywaifu.best:6969/announce`
- `http://tracker.nyaa.vc:6969/announce`
- `http://tracker.opentrackr.org:1337/announce`
- `http://tracker.qu.ax:6969/announce`
- `http://tracker.waaa.moe:6969/announce`
- `http://tracker2.dler.org:80/announce`
- `https://004430.xyz:443/announce`
- `https://2.tracker.eu.org:443/announce`
- `https://337hhh.xyz:443/announce`
- `udp://151.242.104.187:80/announce`
- `udp://189.18.97.208:6969/announce`
- `udp://211.75.205.188:6969/announce`
- `udp://211.75.205.188:80/announce`
- `udp://31.56.179.159:6969/announce`
- `udp://34.66.57.33:1337/announce`
- `udp://34.66.57.33:80/announce`
- `udp://43.250.54.126:6969/announce`
- `udp://45.137.199.107:6969/announce`
- `udp://65.109.28.33:6969/announce`
- `udp://93.158.213.92:1337/announce`
- `udp://95.217.80.22:6969/announce`
- `udp://explodie.org:6969/announce`
- `udp://mail.segso.net:6969/announce`
- `udp://open.demonii.com:1337/announce`
- `udp://retracker01-msk-virt.corbina.net:80/announce`
- `udp://tracker-udp.gbitt.info:80/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.ducks.party:1984/announce`
- `udp://tracker.filemail.com:6969/announce`
- `udp://tracker.leechers-paradise.org:6969/announce`
- `udp://tracker.opentrackr.com:6969/announce`
- `udp://tracker.opentrackr.org:1337/announce`
- `udp://tracker.peerfect.org:6969/announce`
- `udp://tracker.skynetcloud.site:6969/announce`
- `udp://tracker.torrent.eu.org:451/announce`

## Discovery（自动发现的候选，Phase 1 隔离，不进 best/all）

- 候选总数: 154
- 通过探活: 3
- 若允许参与排名会入选的（前 2 条）:
  - `udp://tracker.wildkat.net:6969/announce`
  - `udp://tracker.orsvarn.com:6969/announce`

转正方式：人工 review 后加入 `scripts/update_trackers.py` 的 SOURCES，或写进 `trackers/discovered/PROMOTE.md`（Phase 2）。


## 备选库（trackers_reserve.txt，前 3 条，按评分降序）

独立于 best/all 的候选订阅源，供人工审查转正。
1. `udp://tracker.wildkat.net:6969/announce`
2. `udp://tracker.leechers-paradise.org:6969/announce`
3. `udp://tracker.orsvarn.com:6969/announce`

