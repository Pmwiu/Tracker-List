# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-15 11:49:05 UTC
- 总 Tracker 数: 320
- 存活 (alive): **120** (37%)
- 失效 (dead): **178**
- 不安全 (unsafe): **5**
- 无法测试 (untestable): 17
- 低速淘汰 (low-speed >5s): 0
- 同网段/同域名去重 (kept fastest): 60
- 综合评分后保留前 25 个，淘汰 35 个
- 评分维度: 速度 50% + 历史稳定性 20% + 响应质量 15%（含 peers 计数与 scrape 热度） + 跨源一致性 10% + 近期成功率 5%（速度标度自适应 + 经典高可用加分 + 反退化）
- 配额: 保底 4 条非 UDP + 保底 4 条经典高可用
- 协议多样性配额: 保底 4 条非 UDP，实际保留 12 条
- 耗时: 101.1 秒

## 协议分布

- udp: 68
- http: 40
- https: 12

## 最终订阅列表（前 25 个，按综合评分降序）

1. `https://t.213891.xyz:443/announce` — score=97.3, 24ms, 存活率100%, 质量90, 经典+0
2. `http://tracker.renfei.net:8080/announce` — score=96.1, 63ms, 存活率100%, 质量95, 经典+0
3. `https://1.tracker.eu.org:443/announce` — score=93.9, 32ms, 存活率100%, 质量90, 经典+0
4. `udp://tracker.bittor.pw:1337/announce` — score=93.5, 11ms, 存活率100%, 质量60, 经典+0
5. `https://tracker.nekomi.cn:443/announce` — score=93.4, 116ms, 存活率100%, 质量95, 经典+0
6. `https://004430.xyz:443/announce` — score=93.0, 125ms, 存活率100%, 质量95, 经典+0
7. `udp://tracker.torrent.eu.org:451/announce` — score=92.7, 109ms, 存活率93%, 质量60, 经典+6
8. `udp://evan.im:6969/announce` — score=92.7, 25ms, 存活率100%, 质量60, 经典+0
9. `https://tracker.zhuqiy.com:443/announce` — score=92.5, 48ms, 存活率83%, 质量95, 经典+0
10. `udp://open.ftorrent.com:443/announce` — score=92.5, 28ms, 存活率100%, 质量60, 经典+0
11. `https://tracker.7471.top:443/announce` — score=91.7, 136ms, 存活率100%, 质量90, 经典+0
12. `http://207.241.226.111:6969/announce` — score=91.5, 96ms, 存活率100%, 质量95, 经典+0
13. `http://207.241.231.226:6969/announce` — score=91.4, 96ms, 存活率100%, 质量95, 经典+0
14. `udp://open.demonii.com:1337/announce` — score=90.5, 190ms, 存活率100%, 质量60, 经典+6
15. `https://tracker.foreverpirates.co:443/announce` — score=89.9, 171ms, 存活率100%, 质量90, 经典+0
16. `udp://tracker.nyaa.vc:6969/announce` — score=89.2, 97ms, 存活率100%, 质量60, 经典+0
17. `udp://tracker-udp.gbitt.info:80/announce` — score=89.1, 98ms, 存活率100%, 质量60, 经典+0
18. `udp://tracker.qu.ax:6969/announce` — score=89.0, 99ms, 存活率100%, 质量60, 经典+0
19. `udp://tracker.ducks.party:1984/announce` — score=88.6, 108ms, 存活率100%, 质量60, 经典+0
20. `udp://martin-gebhardt.eu:25/announce` — score=88.6, 107ms, 存活率100%, 质量60, 经典+0
21. `http://tracker.dhitechnical.com:6969/announce` — score=87.9, 227ms, 存活率100%, 质量95, 经典+0
22. `udp://retracker01-msk-virt.corbina.net:80/announce` — score=86.8, 144ms, 存活率100%, 质量60, 经典+0
23. `https://3.tracker.eu.org:443/announce` — score=86.7, 36ms, 存活率100%, 质量90, 经典+0
24. `udp://opentracker.lain.moscow:6969/announce` — score=86.3, 109ms, 存活率92%, 质量60, 经典+0
25. `udp://exodus.desync.com:6969/announce` — score=74.4, 53ms, 存活率27%, 质量60, 经典+6

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
- `http://79.111.12.213:6969/announce` — URLError: <urlopen error timed out>
- `http://asiatorrent.giize.com:51413/announce` — URLError: <urlopen error timed out>
- `http://bittorrent.kali.org:80/announce` — restricted (failure reason)
- `http://echostar.ddnsfree.com:8080/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://ehtracker.org:80/1104308/announce` — restricted (failure reason)
- `http://ehtracker.org:80/1113709/announce` — restricted (failure reason)
- `http://ehtracker.org:80/1226599/1080494xo5eXcwFOBq/announce` — restricted (failure reason)
- `http://ehtracker.org:80/2496841/announce` — restricted (failure reason)
- `http://ehtracker.org:80/2541477/announce` — restricted (failure reason)
- `http://ehtracker.org:80/2566145/1159106xUfsJkT9Btg/announce` — restricted (failure reason)
- `http://retracker.hotplug.ru:2710/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `http://www.wareztorrent.com:80/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://ht.therarbg.to:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.bt4g.com:443/announce` — timeout
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `udp://6ahddutb1ucc3cp.ru:6969/announce` — no connect response
- `udp://laze.cc:6969/announce` — no connect response
- `udp://leefafa.tk:6969/announce` — no connect response
- `udp://ln.mtahost.co:6969/announce` — no connect response
- `udp://lotus-eater.mywire.org:9001/announce` — no connect response
- `udp://mail.artixlinux.org:6969/announce` — no connect response
- `udp://mail.zasaonsk.ga:6969/announce` — no connect response
- `udp://market-re.quest:6969/announce` — no connect response
- `udp://mgtracker.org:2710/announce` — no connect response
- `udp://mikrotik2.draatman.net:6969/announce` — no connect response
- `udp://mirror.aptus.co.tz:6969/announce` — no connect response
- `udp://moonburrow.club:6969/announce` — no connect response
- `udp://movies.zsw.ca:6969/announce` — no connect response
- `udp://mserver.link:6969/announce` — no connect response
- `udp://mts.tvbit.co:6969/announce` — no connect response
- `udp://nagios.tks.sumy.ua:80/announce` — no connect response
- `udp://navegador.click:6969/announce` — no connect response
- `udp://new-line.net:6969/announce` — no connect response
- `udp://node01.madtia.cc:42069/announce` — no connect response
- `udp://node01.torrentonline.cc:42069/announce` — no connect response
- `udp://node01.trackerstatus.live:42069/announce` — no connect response
- `udp://node02.madtia.cc:42069/announce` — no connect response
- `udp://node02.torrentonline.cc:42069/announce` — no connect response
- `udp://ns1.monolithindustries.com:6969/announce` — no connect response
- `udp://odd-hd.fr:6969/announce` — no connect response
- `udp://oh.fuuuuuck.com:6969/announce` — no connect response
- `udp://open.4ever.tk:6969/announce` — no connect response
- `udp://open.publictracker.xyz:6969/announce` — no connect response
- `udp://open.stealth.si/announce` — missing port
- `udp://open.tracker.cl:1337/announce` — no connect response
- `udp://open.tracker.ink:6969/announce` — no connect response
- `udp://open.u-p.pw:6969/announce` — no connect response
- `udp://opentor.org:2710/announce` — no connect response
- `udp://opentracker.i2p.rocks:6969/announce` — no connect response
- `udp://opentracker.io:6969/announce` — no connect response
- `udp://p2p.publictracker.xyz:6969/announce` — no connect response
- `udp://p4p.arenabg.com:1337/announce` — no connect response
- `udp://private.anonseed.com:6969/announce` — no connect response
- `udp://psyco.fr:6969/announce` — no connect response
- `udp://public-tracker.cf:6969/announce` — no connect response
- `udp://public.popcorn-tracker.org:6969/announce` — no connect response
- `udp://public.publictracker.xyz:6969/announce` — no connect response
- `udp://public.tracker.vraphim.com:6969/announce` — no connect response
- `udp://qtstm32fan.ru:6969/announce` — no connect response
- `udp://r.l5.ca:6969/announce` — no connect response
- `udp://rep-art.ynh.fr:6969/announce` — no connect response
- `udp://retracker.hotplug.ru:2710/announce` — no connect response
- `udp://retracker.lanta-net.ru:2710/announce` — no connect response
- `udp://retracker.lanta.me:2710/announce` — no connect response
- `udp://rt.tace.ru:6969/announce` — no connect response
- `udp://run-2.publictracker.xyz:6969/announce` — no connect response
- `udp://run.publictracker.xyz:6969/announce` — no connect response
- `udp://rutorrent.frontline-mod.com:6969/announce` — no connect response
- `udp://ryjer.com:6969/announce` — no connect response
- `udp://sanincode.com:6969/announce` — no connect response
- `udp://shadowshq.eddie4.nl:6969/announce` — no connect response
- `udp://shadowshq.yi.org:6969/announce` — no connect response
- `udp://shahidrazi.online:1984/announce` — no connect response
- `udp://shizzle.hammetjus.nl:6969/announce` — no connect response
- `udp://slicie.icon256.com:8000/announce` — no connect response
- `udp://smtp-relay.odysseylabel.com.au:6969/announce` — no connect response
- `udp://srv5.digiboy.ir:6969/announce` — no connect response
- `udp://ssb14.nohost.me:6969/announce` — no connect response
- `udp://stargrave.org:6969/announce` — no connect response
- `udp://static.54.161.216.95.clients.your-server.de:6969/announce` — no connect response
- `udp://su-data.com:6969/announce` — no connect response
- `udp://t.zerg.pw:6969/announce` — no connect response
- `udp://thagoat.rocks:6969/announce` — no connect response
- `udp://theodoric.fr:6969/announce` — no connect response
- `udp://thetracker.org:80/announce` — no connect response
- `udp://thinking.duckdns.org:6969/announce` — no connect response
- `udp://thouvenin.cloud:6969/announce` — no connect response
- `udp://tk1.trackerservers.com:8080/announce` — no connect response
- `udp://torrent.bowed.net:8081/announce` — no connect response
- `udp://torrent.gresille.org:80/announce` — no connect response
- `udp://torrent.i.ng:6969/announce` — no connect response
- `udp://torrentclub.online:1984/announce` — no connect response
- `udp://torrentclub.online:54123/announce` — no connect response
- `udp://torrentclub.space:6969/announce` — no connect response
- `udp://torrents.tmtime.dev:6969/announce` — no connect response
- `udp://torrentvpn.club:6990/announce` — no connect response
- `udp://tr.bangumi.moe:6969/announce` — no connect response
- `udp://tr.btube3.com:2010/announce` — no connect response
- `udp://tr.cili001.com:8070/announce` — no connect response
- `udp://tracker-de-2.cutie.dating:1337/announce` — no connect response
- `udp://tracker-udp.anirena.com:80/announce` — no connect response
- `udp://tracker-us.silksa.co.za:6969/announce` — no connect response
- `udp://tracker.0x.tf:6969/announce` — no connect response
- `udp://tracker.0x7c0.com:6969/announce` — no connect response
- `udp://tracker.1h.is:1337/announce` — no connect response
- `udp://tracker.4.babico.name.tr:3131/announce` — no connect response
- `udp://tracker.alaskantf.com:6969/announce` — no connect response
- `udp://tracker.aletorrenty.pl:2710/announce` — no connect response
- `udp://tracker.army:6969/announce` — no connect response
- `udp://tracker.artixlinux.org:6969/announce` — no connect response
- `udp://tracker.bitsearch.to:1337/announce` — no connect response
- `udp://tracker.blacksparrowmedia.net:6969/announce` — no connect response
- `udp://tracker.bluefrog.pw:2710/announce` — no connect response
- `udp://tracker.ccp.ovh:6969/announce` — no connect response
- `udp://tracker.coppersurfer.tk:6969/announce` — no connect response
- `udp://tracker.cubonegro.org:80/announce` — no connect response
- `udp://tracker.cubonegro.xyz:6969/announce` — no connect response
- `udp://tracker.cynma.tv:6969/announce` — no connect response
- `udp://tracker.darkness.services:6969/announce` — no connect response
- `udp://tracker.deadorbit.nl:6969/announce` — no connect response
- `udp://tracker.dorcus.digital:1337/announce` — no connect response
- `udp://tracker.draatman.uk:6969/announce` — no connect response
- `udp://tracker.eddie4.nl:6969/announce` — no connect response
- `udp://tracker.edkj.club:6969/announce` — no connect response
- `udp://tracker.ex.ua:80/announce` — no connect response
- `udp://tracker.filemail.com:6969/announce` — no connect response
- `udp://tracker.filetracker.pl:8089/announce` — no connect response
- `udp://tracker.flashtorrents.org:6969/announce` — no connect response
- `udp://tracker.govt.hu:6969/announce` — no connect response
- `udp://tracker.grepler.com:6969/announce` — no connect response
- `udp://tracker.hismz.cn:6969/announce` — no connect response
- `udp://tracker.huadongblower.xyz:8080/announce` — no connect response
- `udp://tracker.iperson.xyz:6969/announce` — no connect response
- `udp://tracker.ixuexi.click:6969/announce` — no connect response
- `udp://tracker.srv00.com:6969/announce` — no connect response
- `udp://tracker.wepzone.net:6969/announce` — no connect response
- `udp://tracker1.itzmx.com:8080/announce` — no connect response
- `udp://tracker1.myporn.club:9337/announce` — no connect response
- `udp://wepzone.net:6969/announce` — no connect response
- `wss://tracker.openwebtorrent.com:443/announce` — SSLError: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1010)

## 不安全 Tracker（已过滤）

- `http://yggtracker.i2p.rocks:80/announce` — resolves to private IP: 200:1e2f:e608:eb3a:2bf:1e62:87ba:e2f7
- `udp://open.dstud.io:6969/announce` — resolves to private IP: 0.0.0.0
- `udp://tamas3.ynh.fr:6969/announce` — resolves to private IP: 127.0.0.12
- `udp://tracker.ccc.de:80/announce` — resolves to private IP: 127.0.0.1
- `udp://tracker.istole.it:80/announce` — resolves to private IP: 127.0.0.1

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

- `http://004430.xyz:80/announce`
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
- `https://2.tracker.eu.org:443/announce`
- `https://337hhh.xyz:443/announce`
- `udp://109.201.134.183:80/announce`
- `udp://135.125.198.235:1984/announce`
- `udp://185.121.168.96:1337/announce`
- `udp://211.75.205.188:6969/announce`
- `udp://31.56.179.159:6969/announce`
- `udp://34.66.57.33:1337/announce`
- `udp://34.66.57.33:80/announce`
- `udp://43.250.54.126:6969/announce`
- `udp://45.137.199.107:6969/announce`
- `udp://65.109.28.17:6969/announce`
- `udp://65.109.28.33:6969/announce`
- `udp://83.102.180.21:80/announce`
- `udp://89.234.156.205:451/announce`
- `udp://93.158.213.92:6969/announce`
- `udp://95.217.80.20:6969/announce`
- `udp://95.217.80.22:6969/announce`
- `udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce`
- `udp://explodie.org:6969/announce`
- `udp://open.stealth.si:80/announce`
- `udp://t.overflow.biz:6969/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.gmi.gd:6969/announce`
- `udp://tracker.ilibr.org:6969/announce`
- `udp://tracker.ilibr.org:80/announce`
- `udp://tracker.opentrackr.org:1337/announce`
- `udp://tracker.peerfect.org:6969/announce`
- `udp://tracker.skynetcloud.site:6969/announce`
- `udp://tracker2.dler.org:80/announce`

## Discovery（自动发现的候选，Phase 1 隔离，不进 best/all）

- 候选总数: 156
- 通过探活: 9
- 若允许参与排名会入选的（前 5 条）:
  - `udp://tracker.cyberia.is:6969/announce`
  - `udp://tr4ck3r.duckdns.org:6969/announce`
  - `udp://tracker.cn.nyaa.net:6969/announce`
  - `udp://tracker.aruku.ovh:8081/announce`
  - `udp://obey.torrentonline.cc:42069/announce`

转正方式：人工 review 后加入 `scripts/update_trackers.py` 的 SOURCES，或写进 `trackers/discovered/PROMOTE.md`（Phase 2）。


## 备选库（trackers_reserve.txt，前 9 条，按评分降序）

独立于 best/all 的候选订阅源，供人工审查转正。
1. `udp://tracker.cyberia.is:6969/announce`
2. `udp://tr4ck3r.duckdns.org:6969/announce`
3. `http://open.tracker.cl:1337/announce`
4. `udp://tracker.ilibr.org:80/announce`
5. `udp://tracker.ilibr.org:6969/announce`
6. `udp://tracker.cn.nyaa.net:6969/announce`
7. `udp://tracker.aruku.ovh:8081/announce`
8. `http://opentracker.xyz:80/announce`
9. `udp://obey.torrentonline.cc:42069/announce`

