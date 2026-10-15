# Tracker 活性测试 + 综合评分排序报告

- 测试时间: 2026-10-15 04:56:03 UTC
- 总 Tracker 数: 320
- 存活 (alive): **111** (34%)
- 失效 (dead): **186**
- 不安全 (unsafe): **6**
- 无法测试 (untestable): 17
- 低速淘汰 (low-speed >5s): 0
- 同网段/同域名去重 (kept fastest): 58
- 综合评分后保留前 25 个，淘汰 28 个
- 评分维度: 速度 50% + 历史稳定性 20% + 响应质量 15%（含 peers 计数与 scrape 热度） + 跨源一致性 10% + 近期成功率 5%（速度标度自适应 + 经典高可用加分 + 反退化）
- 配额: 保底 4 条非 UDP + 保底 4 条经典高可用
- 协议多样性配额: 保底 4 条非 UDP，实际保留 11 条
- 耗时: 60.4 秒

## 协议分布

- udp: 60
- http: 39
- https: 12

## 最终订阅列表（前 25 个，按综合评分降序）

1. `http://tracker.renfei.net:8080/announce` — score=98.4, 17ms, 存活率100%, 质量95, 经典+0
2. `https://t.213891.xyz:443/announce` — score=97.6, 17ms, 存活率100%, 质量90, 经典+0
3. `http://tracker.dhitechnical.com:6969/announce` — score=94.6, 102ms, 存活率100%, 质量98, 经典+0
4. `udp://explodie.org:6969/announce` — score=94.2, 91ms, 存活率96%, 质量60, 经典+6
5. `udp://evan.im:6969/announce` — score=93.8, 2ms, 存活率100%, 质量60, 经典+0
6. `udp://tracker.torrent.eu.org:451/announce` — score=93.2, 93ms, 存活率92%, 质量60, 经典+6
7. `udp://tracker.bittor.pw:1337/announce` — score=92.7, 25ms, 存活率100%, 质量60, 经典+0
8. `udp://open.ftorrent.com:443/announce` — score=91.5, 48ms, 存活率100%, 质量60, 经典+0
9. `https://tracker.foreverpirates.co:443/announce` — score=90.7, 155ms, 存活率100%, 质量90, 经典+0
10. `https://tracker.nekomi.cn:443/announce` — score=90.5, 175ms, 存活率100%, 质量95, 经典+0
11. `http://207.241.226.111:6969/announce` — score=90.0, 133ms, 存活率100%, 质量98, 经典+0
12. `udp://tracker.skynetcloud.site:6969/announce` — score=90.0, 81ms, 存活率100%, 质量60, 经典+0
13. `udp://tracker-udp.gbitt.info:80/announce` — score=89.9, 82ms, 存活率100%, 质量60, 经典+0
14. `https://tracker.zhuqiy.com:443/announce` — score=89.8, 76ms, 存活率79%, 质量95, 经典+0
15. `udp://open.demonii.com:1337/announce` — score=89.8, 202ms, 存活率100%, 质量60, 经典+6
16. `udp://tracker.nyaa.vc:6969/announce` — score=89.8, 84ms, 存活率100%, 质量60, 经典+0
17. `http://207.241.231.226:6969/announce` — score=89.3, 138ms, 存活率100%, 质量95, 经典+0
18. `udp://martin-gebhardt.eu:25/announce` — score=89.3, 92ms, 存活率100%, 质量60, 经典+0
19. `udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce` — score=88.0, 92ms, 存活率96%, 质量60, 经典+0
20. `udp://retracker01-msk-virt.corbina.net:80/announce` — score=87.6, 129ms, 存活率100%, 质量60, 经典+0
21. `https://tracker.7471.top:443/announce` — score=87.0, 230ms, 存活率100%, 质量90, 经典+0
22. `https://3.tracker.eu.org:443/announce` — score=86.8, 34ms, 存活率100%, 质量90, 经典+0
23. `udp://opentracker.lain.moscow:6969/announce` — score=86.7, 94ms, 存活率89%, 质量60, 经典+0
24. `https://2.tracker.eu.org:443/announce` — score=86.5, 40ms, 存活率100%, 质量90, 经典+0
25. `udp://mail.segso.net:6969/announce` — score=85.3, 112ms, 存活率100%, 质量60, 经典+0

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
- `http://34.66.57.33:2701/announce` — timeout
- `http://34.66.57.33:2710/announce` — timeout
- `http://79.111.12.213:6969/announce` — timeout
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
- `https://tr.abiir.top:443/announce` — URLError: <urlopen error [Errno 104] Connection reset by peer>
- `https://tr.abir.ga:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate (_ssl.c:1010)>
- `https://tr.burnabyhighstar.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
- `https://tracker.bt4g.com:443/announce` — timeout
- `https://tracker.kuroy.me:443/announce` — timeout
- `https://tracker.lenition.de:443/announce` — URLError: <urlopen error timed out>
- `https://tracker.lilithraws.org:443/announce` — timeout
- `https://tracker.logirl.moe:443/announce` — URLError: <urlopen error timed out>
- `https://tracker.loli.co.nz:443/announce` — HTTPError: HTTP Error 530: <none>
- `https://tracker.loligirl.cn:443/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `https://tracker.manager.itislove.cz:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>
- `https://tracker.manager.v6.navy:443/announce` — URLError: <urlopen error [Errno -3] Temporary failure in name resolution>
- `https://tracker.maya.no.eu.org:443/announce` — HTTPError: HTTP Error 429: Too Many Requests
- `https://tracker.mlsub.net:443/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `https://tracker.moeblog.cn:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.moeking.me:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.monikadesign.uk:443/announce/63ea34cb9815cd28d63fc75b2f2c5a56` — restricted (failure reason)
- `https://tracker.monikadesign.uk:443/announce/a46be21ab845cc0d534d06fea801f95a` — restricted (failure reason)
- `https://tracker.moxing.party:6969/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate (_ssl.c:1010)>
- `https://tracker.nanoha.org:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.netmap.top:8443/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `https://tracker.nitrix.me:443/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `https://tracker.novy.vip:443/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `https://tracker.nyaa.tk:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.onetracker.net:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.opentracker.se:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate (_ssl.c:1010)>
- `https://tracker.parrotlinux.org:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.pmman.tech:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://tracker.pterclub.com:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>
- `https://tracker.publictorrent.net:443/announce` — URLError: <urlopen error [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:1010)>
- `https://tracker.puvvadi.net:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.qingwa.pro:443/announce` — invalid bencoded response
- `https://tracker.renfei.net:443/announce` — URLError: <urlopen error [Errno 111] Connection refused>
- `https://tracker.sakurato.art:23334/announce` — URLError: <urlopen error timed out>
- `https://tracker.samcze.pl:443/announce` — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate (_ssl.c:1010)>
- `https://tracker.skynetcloud.site:8443/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `https://tracker.srv00.com:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://tracker.tamersunion.org:443/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `https://tracker.tvgc.win:443/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://tracker.vectahosting.eu:443/announce` — URLError: <urlopen error [Errno -5] No address associated with hostname>
- `https://tracker.yemekyedim.com:443/announce` — HTTPError: HTTP Error 521: <none>
- `https://tracker.yggleak.top:443/announce` — HTTPError: HTTP Error 521: <none>
- `https://tracker1.loli.co.nz:443/announce` — HTTPError: HTTP Error 530: <none>
- `https://tracker1.wimix.org:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://trackme.theom.nz:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://trakx.herokuapp.com:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://ttk.pp.ua:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://ttracker.just-h.party:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://voxhost.fr:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://w.wwwww.wtf:443/announce` — URLError: <urlopen error [Errno -2] Name or service not known>
- `https://wolf.parrot.run:443/announce` — timeout
- `https://wsad.run.place:443/announce` — URLError: <urlopen error [Errno -3] Temporary failure in name resolution>
- `https://www.peckservers.com:9443/announce` — URLError: <urlopen error [Errno 101] Network is unreachable>
- `https://www.wareztorrent.com:443/announce` — RemoteDisconnected: Remote end closed connection without response
- `https://x7x.up.railway.app:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://xtremex.herokuapp.com:443/announce` — HTTPError: HTTP Error 404: Not Found
- `https://zer0day.000webhostapp.com:443/announce` — URLError: <urlopen error [Errno -3] Temporary failure in name resolution>
- `udp://11.rarbg.com:80/announce` — no connect response
- `udp://1c.premierzal.ru:6969/announce` — no connect response
- `udp://47.ip-51-68-199.eu:6969/announce` — no connect response
- `udp://6.pocketnet.app:6969/announce` — no connect response
- `udp://6ahddutb1ucc3cp.ru:6969/announce` — no connect response
- `udp://94-227-232-84.access.telenet.be:6969/announce` — no connect response
- `udp://960303.xyz:6969/announce` — no connect response
- `udp://aaa.army:8866/announce` — no connect response
- `udp://acxx.de:6969/announce` — no connect response
- `udp://admin.videoenpoche.info:6969/announce` — no connect response
- `udp://aegir.sexy:6969/announce` — no connect response
- `udp://amigacity.xyz:6969/announce` — no connect response
- `udp://anime-tracker.aruku.kro.kr:8081/announce` — no connect response
- `udp://anna.bt.bontal.net:6969/announce` — no connect response
- `udp://app.icon256.com:8000/announce` — no connect response
- `udp://astrr.ru:6969/announce` — no connect response
- `udp://bananas.space:6969/announce` — no connect response
- `udp://bandito.byterunner.io:6969/announce` — no connect response
- `udp://banzaitracker.com:2710/announce` — no connect response
- `udp://bedro.cloud:6969/announce` — no connect response
- `udp://ben.kerbertools.xyz:6969/announce` — no connect response
- `udp://black-bird.ynh.fr:6969/announce` — no connect response
- `udp://brokenhelix.loseyourip.com:6969/announce` — no connect response
- `udp://bt.bontal.net:6969/announce` — no connect response
- `udp://bt.ktrackers.com:6666/announce` — no connect response
- `udp://bt.letpo.com:6969/announce` — no connect response
- `udp://bt.oiyo.tk:6969/announce` — no connect response
- `udp://bt.rer.lol:6969/announce` — no connect response
- `udp://bt.xxx-tracker.com:2710/announce` — no connect response
- `udp://bt1.archive.org:6969/announce` — no connect response
- `udp://bt2.archive.org:6969/announce` — no connect response
- `udp://bubu.mapfactor.com:6969/announce` — no connect response
- `udp://buddyfly.top:6969/announce` — no connect response
- `udp://burmese.app:6969/announce` — no connect response
- `udp://camera.lei001.com:6969/announce` — no connect response
- `udp://carr.codes:6969/announce` — no connect response
- `udp://cerf.cs.umd.edu:8000/announce` — no connect response
- `udp://chouchou.top:8080/announce` — no connect response
- `udp://concen.org:6969/announce` — no connect response
- `udp://cpe-104-34-3-152.socal.res.rr.com:6969/announce` — no connect response
- `udp://cutscloud.duckdns.org:6969/announce` — no connect response
- `udp://d40969.acod.regrucolo.ru:6969/announce` — no connect response
- `udp://db.koikia.eu:6969/announce` — no connect response
- `udp://devops.gay:6969/announce` — no connect response
- `udp://dht.bt251.com:6969/announce` — no connect response
- `udp://download.nerocloud.me:6969/announce` — no connect response
- `udp://ds32244.seedhost.eu:6969/announce` — no connect response
- `udp://ec2-18-191-163-220.us-east-2.compute.amazonaws.com:6969/announce` — no connect response
- `udp://eddie4.nl:6969/announce` — no connect response
- `udp://elementsbrowser.com:6969/announce` — no connect response
- `udp://epider.me:6969/announce` — no connect response
- `udp://exodus.desync.com:6969/announce` — no connect response
- `udp://f1sh.de:6969/announce` — no connect response
- `udp://fe.dealclub.de:6969/announce` — no connect response
- `udp://fh2.cmp-gaming.com:6969/announce` — no connect response
- `udp://files.project-cataclysm.ru:6969/announce` — no connect response
- `udp://free.publictracker.xyz:6969/announce` — no connect response
- `udp://freedom.1776.ga:6969/announce` — no connect response
- `udp://freedomalternative.com:6969/announce` — no connect response
- `udp://htz3.noho.st:6969/announce` — no connect response
- `udp://ibksturm.synology.me:6969/announce` — no connect response
- `udp://jutone.com:6969/announce` — no connect response
- `udp://keke.re:6969/announce` — no connect response
- `udp://kokodayo.site:6969/announce` — no connect response
- `udp://kolanopentracker.airdns.org:3392/announce` — no connect response
- `udp://laestrygonian.ooguy.com:9001/announce` — no connect response
- `udp://open.tracker.ink:6969/announce` — no connect response
- `udp://opentor.org:2710/announce` — no connect response
- `udp://p4p.arenabg.com:1337/announce` — no connect response
- `udp://retracker.hotplug.ru:2710/announce` — no connect response
- `udp://torrentclub.online:54123/announce` — no connect response
- `udp://torrents.tmtime.dev:6969/announce` — no connect response
- `udp://tracker.alaskantf.com:6969/announce` — no connect response
- `udp://tracker.srv00.com:6969/announce` — no connect response
- `udp://tracker.theoks.net:6969/announce` — no connect response
- `udp://tracker.tryhackx.org:6969/announce` — no connect response
- `udp://tracker.wepzone.net:6969/announce` — no connect response
- `udp://tracker1.itzmx.com:8080/announce` — no connect response
- `udp://tracker1.myporn.club:9337/announce` — no connect response
- `udp://wepzone.net:6969/announce` — no connect response
- `wss://tracker.openwebtorrent.com:443/announce` — SSLError: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1010)

## 不安全 Tracker（已过滤）

- `http://yggtracker.i2p.rocks:80/announce` — resolves to private IP: 200:1e2f:e608:eb3a:2bf:1e62:87ba:e2f7
- `https://tracker.parrotsec.org:443/announce` — resolves to private IP: 0.0.0.0
- `udp://ipv4.tracker.harry.lu/announce` — resolves to private IP: 127.0.0.1
- `udp://ipv4.tracker.harry.lu:80/announce` — resolves to private IP: 127.0.0.1
- `udp://ipv6.tracker.harry.lu/announce` — resolves to private IP: ::1
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
- `http://34.66.57.33:1337/announce`
- `http://43.250.54.126:6969/announce`
- `http://93.158.213.92:1337/announce`
- `http://94.23.207.177:6969/announce`
- `http://announce.sktorrent.eu:6969/announce`
- `http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce`
- `http://h4.trakx.nibba.trade:80/announce`
- `http://ipv4announce.sktorrent.eu:6969/announce`
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
- `https://1.tracker.eu.org:443/announce`
- `https://337hhh.xyz:443/announce`
- `udp://109.201.134.183:80/announce`
- `udp://185.121.168.96:1337/announce`
- `udp://211.75.205.188:6969/announce`
- `udp://23.157.120.14:6969/announce`
- `udp://34.66.57.33:1337/announce`
- `udp://34.66.57.33:80/announce`
- `udp://43.250.54.126:6969/announce`
- `udp://45.137.199.107:6969/announce`
- `udp://52.58.128.163:6969/announce`
- `udp://65.109.28.17:6969/announce`
- `udp://65.109.28.33:6969/announce`
- `udp://83.102.180.21:80/announce`
- `udp://89.234.156.205:451/announce`
- `udp://93.158.213.92:6969/announce`
- `udp://95.217.80.20:6969/announce`
- `udp://open.stealth.si:80/announce`
- `udp://t.overflow.biz:6969/announce`
- `udp://tracker.corpscorp.online:80/announce`
- `udp://tracker.dler.org:6969/announce`
- `udp://tracker.ducks.party:1984/announce`
- `udp://tracker.farted.net:6969/announce`
- `udp://tracker.opentrackr.com:6969/announce`
- `udp://tracker.opentrackr.org:1337/announce`
- `udp://tracker.peerfect.org:6969/announce`
- `udp://tracker.qu.ax:6969/announce`

## Discovery（自动发现的候选，Phase 1 隔离，不进 best/all）

- 候选总数: 161
- 通过探活: 6
- 若允许参与排名会入选的（前 4 条）:
  - `udp://189.18.97.208:6969/announce`
  - `udp://211.75.205.188:80/announce`
  - `https://tracker.midnightprogrammer.net:443/announce`
  - `udp://coeus.torrentonline.cc:42069/announce`

转正方式：人工 review 后加入 `scripts/update_trackers.py` 的 SOURCES，或写进 `trackers/discovered/PROMOTE.md`（Phase 2）。


## 备选库（trackers_reserve.txt，前 6 条，按评分降序）

独立于 best/all 的候选订阅源，供人工审查转正。
1. `http://h4.trakx.nibba.trade:80/announce`
2. `http://34.66.57.33:1337/announce`
3. `udp://189.18.97.208:6969/announce`
4. `udp://211.75.205.188:80/announce`
5. `https://tracker.midnightprogrammer.net:443/announce`
6. `udp://coeus.torrentonline.cc:42069/announce`

