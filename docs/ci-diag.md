=== Diagnostics Wed Sep 30 11:55:56 UTC 2026 ===
Python: Python 3.12.14
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://cf.trackerslist.com/best.txt
  HTTP 200, total 0.089692s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best_ip.txt
  HTTP 200, total 0.052216s
>>> https://tracker.adysec.com/trackers_best.txt
  HTTP 200, total 0.173120s
>>> https://tracker.adysec.com/trackers_best_http.txt
  HTTP 200, total 0.125279s
>>> https://tracker.adysec.com/trackers_best_https.txt
  HTTP 200, total 0.066642s
>>> https://tracker.adysec.com/trackers_best_udp.txt
  HTTP 200, total 0.091824s
>>> https://tracker.adysec.com/trackers_best_wss.txt
  HTTP 200, total 0.069602s
>>> https://raw.githubusercontent.com/DeSireFire/animeTrackerList/refs/heads/master/ATline_best.txt
  HTTP 200, total 0.079830s
>>> https://raw.githubusercontent.com/DeSireFire/animeTrackerList/refs/heads/master/ATline_best_ip.txt
  HTTP 200, total 0.124722s
>>> https://raw.githubusercontent.com/kris3713/UltimateBTTrackersList/refs/heads/master/ultimate_trackers.txt
  HTTP 200, total 0.115577s
>>> https://raw.githubusercontent.com/1265578519/OpenTracker/master/tracker.txt
  HTTP 200, total 0.219361s
[INFO] Repo: Pmwiu/Tracker-List, Max: 59

[INFO] trackers_cf_best.txt (cf-best)
[OK]   71 unique

[INFO] trackers_ngosang_ip.txt (ngosang-ip)
[OK]   20 unique

[INFO] trackers_adysec_best.txt (adysec-best)
[OK]   332 unique

[INFO] trackers_adysec_http.txt (adysec-http)
[OK]   131 unique

[INFO] trackers_adysec_https.txt (adysec-https)
[OK]   32 unique

[INFO] trackers_adysec_udp.txt (adysec-udp)
[OK]   163 unique

[INFO] trackers_adysec_wss.txt (adysec-wss)
[OK]   6 unique

[INFO] trackers_anime_best.txt (anime-best)
[OK]   25 unique

[INFO] trackers_anime_ip.txt (anime-ip)
[OK]   1 unique

[INFO] trackers_ultimate.txt (ultimate)
[OK]   183 unique

[INFO] trackers_opentracker.txt (opentracker)
[OK]   38 unique

[OK]   merged: 402
[OK]   MIRRORS.txt
[OK]   /s/alive
[OK]   /s/all
[OK]   index.html
[OK]   docs/alive.txt
[OK]   docs/merged.txt
[OK]   docs/cf_best.txt
[OK]   docs/ngosang_ip.txt
[OK]   docs/adysec_best.txt
[OK]   docs/adysec_http.txt
[OK]   docs/adysec_https.txt
[OK]   docs/adysec_udp.txt
[OK]   docs/adysec_wss.txt
[OK]   docs/anime_best.txt
[OK]   docs/anime_ip.txt
[OK]   docs/ultimate.txt
[OK]   docs/opentracker.txt

===== Summary =====
  trackers_cf_best.txt: 71
  trackers_ngosang_ip.txt: 20
  trackers_adysec_best.txt: 332
  trackers_adysec_http.txt: 131
  trackers_adysec_https.txt: 32
  trackers_adysec_udp.txt: 163
  trackers_adysec_wss.txt: 6
  trackers_anime_best.txt: 25
  trackers_anime_ip.txt: 1
  trackers_ultimate.txt: 183
  trackers_opentracker.txt: 38
  trackers_merged.txt: 402
  alive capped at 59 after test+sort
===================
[INFO] Testing 402 of 402 candidates (timeout=10s, workers=30, priority sources first)
[INFO] Max alive trackers after scoring: 59
  [ALIVE] (1/402) http://004430.xyz:80/announce 59ms — valid announce response
  [ALIVE] (2/402) http://207.241.226.111:6969/announce 135ms — valid announce response
  [ALIVE] (3/402) http://207.241.231.226:6969/announce 130ms — valid announce response
  [ALIVE] (4/402) http://bittorrent.kali.org:80/announce 11ms — online (failure reason)
  [ALIVE] (5/402) http://135.125.198.235:2710/announce 182ms — valid announce response
  [ALIVE] (6/402) http://185.126.65.92:6969/announce 179ms — valid announce response
  [ALIVE] (7/402) http://135.125.198.235:80/announce 185ms — valid announce response
  [ALIVE] (8/402) http://94.23.207.177:6969/announce 172ms — valid announce response
  [ALIVE] (9/402) http://43.250.54.126:6969/announce 178ms — valid announce response
  [ALIVE] (10/402) http://93.158.213.92:1337/announce 190ms — valid announce response
  [ALIVE] (11/402) http://177.188.141.75:6969/announce 230ms — valid announce response
  [ALIVE] (12/402) http://31.38.161.123:6969/announce 216ms — valid announce response
  [ALIVE] (13/402) http://bt.edwardk.info:6767/announce 58ms — online (failure reason)
  [ALIVE] (14/402) http://bt.edwardk.info:676/announce 64ms — online (failure reason)
  [ALIVE] (15/402) http://bt.edwardk.info:63124/announce 63ms — online (failure reason)
  [ALIVE] (16/402) http://bt.edwardk.info:4040/announce 67ms — online (failure reason)
  [ALIVE] (17/402) http://bt.edwardk.info:6969/announce 74ms — online (failure reason)
  [ALIVE] (18/402) http://bt.edwardk.info:12891/announce 81ms — online (failure reason)
  [ALIVE] (19/402) http://bt.edwardk.info:2710/announce 81ms — online (failure reason)
  [ALIVE] (20/402) http://79.111.12.213:6969/announce 266ms — online (failure reason)
  [ALIVE] (21/402) http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 195ms — valid announce response
  [ALIVE] (22/402) http://211.75.205.187:6969/announce 376ms — valid announce response
  [ALIVE] (23/402) http://211.75.205.187:80/announce 376ms — valid announce response
  [ALIVE] (24/402) http://211.75.205.189:6969/announce 375ms — valid announce response
  [ALIVE] (25/402) http://211.75.205.188:6969/announce 377ms — valid announce response
  [ALIVE] (26/402) http://211.75.205.188:80/announce 377ms — valid announce response
  [ALIVE] (27/402) http://211.75.205.189:80/announce 377ms — valid announce response
  [ALIVE] (28/402) http://211.75.210.221:80/announce 375ms — valid announce response
  [ALIVE] (29/402) http://211.75.210.221:6969/announce 377ms — valid announce response
  [ALIVE] (30/402) http://60.249.37.20:6969/announce 377ms — valid announce response
  [ALIVE] (31/402) http://60.249.37.20:80/announce 378ms — valid announce response
  [ALIVE] (32/402) http://bt2.edwardk.info:2710/announce 57ms — online (failure reason)
  [ALIVE] (33/402) http://bt2.edwardk.info:4040/announce 64ms — online (failure reason)
  [ALIVE] (34/402) http://bt2.edwardk.info:6969/announce 74ms — online (failure reason)
  [ALIVE] (35/402) http://ipv4announce.sktorrent.eu:6969/announce 173ms — valid announce response
  [ALIVE] (36/402) http://bt2.archive.org:6969/announce 210ms — valid announce response
  [ALIVE] (37/402) http://announce.sktorrent.eu:6969/announce 389ms — valid announce response
  [ALIVE] (38/402) http://bttracker.debian.org:6969/announce 235ms — online (failure reason)
  [ALIVE] (39/402) http://bt1.archive.org:6969/announce 195ms — valid announce response
  [ALIVE] (40/402) http://bt.zlofenix.org:81/announce 309ms — online (failure reason)
  [ALIVE] (41/402) http://bt.beatrice-raws.org:80/announce 524ms — online (failure reason)
  [ALIVE] (42/402) http://open.demonii.si:80/announce 249ms — valid announce response
  [ALIVE] (43/402) http://bt02.nnm-club.cc:2710/announce 282ms — online (failure reason)
  [ALIVE] (44/402) http://ehtracker.org:80/2496841/announce 167ms — online (failure reason)
  [ALIVE] (45/402) http://ehtracker.org:80/1113709/announce 172ms — online (failure reason)
  [ALIVE] (46/402) http://ehtracker.org:80/1/announce 167ms — online (failure reason)
  [ALIVE] (47/402) http://ehtracker.org:80/1104308/announce 171ms — online (failure reason)
  [ALIVE] (48/402) http://ehtracker.org:80/2566145/1159106xUfsJkT9Btg/announce 175ms — online (failure reason)
  [ALIVE] (49/402) http://ehtracker.org:80/2541477/announce 177ms — online (failure reason)
  [ALIVE] (50/402) http://ehtracker.org:80/1226599/1080494xo5eXcwFOBq/announce 178ms — online (failure reason)
  [ALIVE] (51/402) http://nyaa.tracker.wf:7777/announce 200ms — valid announce response
  [ALIVE] (52/402) http://t-backup.213891.xyz:80/announce 51ms — valid announce response
  [ALIVE] (53/402) http://bt02.nnm-club.info:2710/announce 268ms — online (failure reason)
  [ALIVE] (54/402) http://torrent.fedoraproject.org:6969/announce 44ms — online (failure reason)
  [ALIVE] (55/402) http://ch3oh.ru:6969/announce 389ms — online (failure reason)
  [ALIVE] (56/402) http://tracker.004430.xyz:1337/announce 78ms — valid announce response
  [ALIVE] (57/402) http://tr.nyacat.pw:80/announce 109ms — valid announce response
  [ALIVE] (58/402) http://retracker.x2k.ru:80/announce 193ms — valid announce response
  [ALIVE] (59/402) http://opentracker.acgnx.se:80/announce 316ms — online (failure reason)
  [ALIVE] (60/402) http://bt.nnm-club.info:2710/announce 526ms — online (failure reason)
  [ALIVE] (61/402) http://tracker-udp.anirena.com:80/announce 169ms — online (failure reason)
  [ALIVE] (62/402) http://opentrackr.org:1337/announce 374ms — valid announce response
  [ALIVE] (63/402) http://sukebei.tracker.wf:8888/announce 332ms — valid announce response
  [ALIVE] (64/402) http://tracker-zhuqiy.dgj055.icu:80/announce 237ms — valid announce response
  [ALIVE] (65/402) http://tracker.acgnx.se:80/announce 347ms — online (failure reason)
  [ALIVE] (66/402) http://tracker.auctor.tv:6969/announce 168ms — valid announce response
  [ALIVE] (67/402) http://t.overflow.biz:6969/announce 261ms — valid announce response
  [ALIVE] (68/402) http://tracker.coppersurfer.site:2710/announce 176ms — valid announce response
  [ALIVE] (69/402) http://t.nyaatracker.com:80/announce 248ms — valid announce response
  [ALIVE] (70/402) http://torrent.ubuntu.com:6969/announce 463ms — online (failure reason)
  [ALIVE] (71/402) http://retracker01-msk-virt.corbina.net:80/announce 440ms — valid announce response
  [ALIVE] (72/402) http://open.touki.ru:80/announce 517ms — online (failure reason)
  [ALIVE] (73/402) http://tracker.ddunlimited.net:6969/announce 282ms — online (failure reason)
  [ALIVE] (74/402) http://tracker.ali213.net:8000/announce 489ms — online (failure reason)
  [ALIVE] (75/402) http://tracker.kali.org:6969/announce 17ms — online (failure reason)
  [ALIVE] (76/402) http://tracker.gcvchp.com:2710/announce 203ms — online (failure reason)
  [ALIVE] (77/402) http://tracker.ali213.net:8080/announce 535ms — online (failure reason)
  [ALIVE] (78/402) http://opentracker.xyz:80/announce 720ms — valid announce response
  [ALIVE] (79/402) http://tracker.fansub.id:80/announce 305ms — valid announce response
  [ALIVE] (80/402) http://tracker.dler.org:6969/announce 497ms — valid announce response
  [ALIVE] (81/402) http://tracker.dler.com:6969/announce 383ms — valid announce response
  [ALIVE] (82/402) http://216.144.239.90:6969/announce 1693ms — valid announce response
  [ALIVE] (83/402) http://tracker.nyaa.vc:6969/announce 171ms — valid announce response
  [ALIVE] (84/402) http://tracker.minglong.org:8080/announce 166ms — online (failure reason)
  [ALIVE] (85/402) http://tracker.mywaifu.best:6969/announce 287ms — valid announce response
  [ALIVE] (86/402) http://tracker.opentorrent.top:6969/announce 231ms — valid announce response
  [ALIVE] (87/402) http://tracker.dm258.cn:7070/announce 524ms — online (failure reason)
  [ALIVE] (88/402) http://tracker.qu.ax:6969/announce 172ms — valid announce response
  [ALIVE] (89/402) http://tracker.privateseedbox.xyz:2710/announce 185ms — valid announce response
  [ALIVE] (90/402) http://tracker.gigatorrents.ws:2710/announce 488ms — online (failure reason)
  [ALIVE] (91/402) http://tracker.pussytorrents.org:3000/announce 187ms — online (failure reason)
  [ALIVE] (92/402) http://tracker.novaopcj.eu.org:6969/announce 177ms — valid announce response
  [ALIVE] (93/402) http://tracker.trancetraffic.com:80/announce 65ms — online (failure reason)
  [ALIVE] (94/402) http://tracker.renfei.net:8080/announce 18ms — valid announce response
  [ALIVE] (95/402) http://tracker.linkomanija.org:2710/announce 489ms — online (failure reason)
  [ALIVE] (96/402) http://tracker.torrents.observer:80/announce 176ms — valid announce response
  [ALIVE] (97/402) http://tracker.opentrackr.org:1337/announce 256ms — valid announce response
  [ALIVE] (98/402) http://tracker.xn--djrq4gl4hvoi.top:80/announce 299ms — valid announce response
  [ALIVE] (99/402) http://tracker.zhuqiy.dgj055.icu:80/announce 245ms — valid announce response
  [ALIVE] (100/402) http://tracker.xfapi.top:6868/announce 509ms — online (failure reason)
  [ALIVE] (101/402) http://tracker.xfapi.top:7070/announce 505ms — online (failure reason)
  [ALIVE] (102/402) http://tracker.k.vu:6969/announce 450ms — valid announce response
  [ALIVE] (103/402) http://tracker.xfapi.top:9999/announce 527ms — online (failure reason)
  [ALIVE] (104/402) http://tracker.internetwarriors.net:1337/announce 1295ms — valid announce response
  [ALIVE] (105/402) http://tracker.openzim.org:80/announce 782ms — online (failure reason)
  [ALIVE] (106/402) https://004430.xyz:443/announce 61ms — valid announce response
  [ALIVE] (107/402) http://tracker.zhuqiy.com:80/announce 233ms — valid announce response
  [ALIVE] (108/402) http://www.arabp2p.net:2052/f5a1e35785c9f3885fd54f34b6e262b8/announce 201ms — online (failure reason)
  [ALIVE] (109/402) http://tracker1.itzmx.com:8080/announce 432ms — valid announce response
  [ALIVE] (110/402) http://tracker.waaa.moe:6969/announce 821ms — valid announce response
  [ALIVE] (111/402) https://337hhh.xyz:443/announce 278ms — valid announce response
  [ALIVE] (112/402) https://3.tracker.eu.org:443/announce 54ms — valid announce response
  [ALIVE] (113/402) http://tracker2.dler.org:80/announce 519ms — valid announce response
  [ALIVE] (114/402) http://tracker3.dler.org:2710/announce 514ms — valid announce response
  [ALIVE] (115/402) https://1.tracker.eu.org:443/announce 47ms — valid announce response
  [ALIVE] (116/402) http://tracker2.dler.com:80/announce 581ms — valid announce response
  [ALIVE] (117/402) https://5.tracker.eu.org:443/announce 44ms — valid announce response
  [ALIVE] (118/402) https://t.213891.xyz:443/announce 24ms — valid announce response
  [ALIVE] (119/402) https://2.tracker.eu.org:443/announce 37ms — valid announce response
  [ALIVE] (120/402) https://bt.beatrice-raws.org:443/announce 185ms — online (failure reason)
  [ALIVE] (121/402) https://open.ftorrent.com:443/announce 129ms — valid announce response
  [ALIVE] (122/402) https://retracker.x2k.ru:443/announce 213ms — valid announce response
  [ALIVE] (123/402) https://tr.nyacat.pw:443/announce 116ms — valid announce response
  [ALIVE] (124/402) https://t.btcland.xyz:443/announce 267ms — valid announce response
  [ALIVE] (125/402) http://open.tracker.cl:1337/announce 1434ms — valid announce response
  [ALIVE] (126/402) https://1337.abcvg.info:443/announce 642ms — valid announce response
  [ALIVE] (127/402) https://torrent.ubuntu.com:443/announce 335ms — online (failure reason)
  [ALIVE] (128/402) https://tr-rh-zhuqiy.dgj055.icu:443/announce 368ms — valid announce response
  [ALIVE] (129/402) https://tracker.7471.top:443/announce 138ms — valid announce response
  [ALIVE] (130/402) https://tr-zhuqiy-2.dgj055.icu:443/announce 367ms — valid announce response
  [ALIVE] (131/402) https://tracker.anibt.net:443/announce 113ms — online (failure reason)
  [ALIVE] (132/402) http://140.235.237.23:6969/announce 3535ms — valid announce response
  [ALIVE] (133/402) https://tracker.foreverpirates.co:443/announce 137ms — valid announce response
  [ALIVE] (134/402) https://tr-zhuqiy-1.dgj055.icu:443/announce 367ms — valid announce response
  [ALIVE] (135/402) https://4.tracker.eu.org:443/announce 37ms — valid announce response
  [ALIVE] (136/402) https://tracker.keepfrds.com:443/announce 163ms — online (failure reason)
  [ALIVE] (137/402) https://tracker-zhuqiy.dgj055.icu:443/announce 376ms — valid announce response
  [ALIVE] (138/402) https://tr.torland.ga:443/announce 377ms — valid announce response
  [ALIVE] (139/402) https://retracker2.x2k.ru:443/announce 544ms — valid announce response
  [ALIVE] (140/402) https://tracker.zhuqiy.com:443/announce 216ms — valid announce response
  [ALIVE] (141/402) udp://109.201.134.183:80/announce 87ms — valid connect + announce
  [ALIVE] (142/402) https://tracker.qingwapt.org:443/announce 147ms — online (failure reason)
  [ALIVE] (143/402) https://tracker.monikadesign.uk:443/announce 328ms — online (failure reason)
  [ALIVE] (145/402) udp://149.106.106.25:443/announce 44ms — valid connect + announce
  [ALIVE] (146/402) udp://135.125.198.235:1984/announce 91ms — valid connect + announce
  [ALIVE] (147/402) https://tracker.midnightprogrammer.net:443/announce 312ms — valid announce response
  [ALIVE] (148/402) udp://164.152.110.70:6969/announce 22ms — valid connect + announce
  [ALIVE] (149/402) udp://173.201.36.219:6969/announce 25ms — valid connect + announce
  [ALIVE] (150/402) https://tr2.trkb.ru:443/announce 541ms — valid announce response
  [ALIVE] (151/402) udp://132.226.6.145:6969/announce 156ms — valid connect + announce
  [ALIVE] (152/402) udp://151.242.104.187:80/announce 107ms — valid connect + announce
  [ALIVE] (153/402) udp://118.196.100.63:6969/announce 214ms — valid connect + announce
  [ALIVE] (154/402) udp://180.131.145.175:6969/announce 93ms — valid connect + announce
  [ALIVE] (155/402) udp://192.3.130.53:1337/announce 18ms — valid connect + announce
  [ALIVE] (156/402) udp://192.99.100.68:6969/announce 14ms — valid connect + announce
  [ALIVE] (157/402) udp://178.239.19.29:80/announce 93ms — valid connect + announce
  [ALIVE] (158/402) udp://177.188.141.75:6969/announce 114ms — valid connect + announce
  [ALIVE] (159/402) https://tracker.nekomi.cn:443/announce 76ms — valid announce response
  [ALIVE] (160/402) udp://120.78.150.131:6969/announce 237ms — valid connect + announce
  [ALIVE] (161/402) udp://193.148.251.93:6969/announce 36ms — valid connect + announce
  [ALIVE] (162/402) udp://185.216.179.62:25/announce 96ms — valid connect + announce
  [ALIVE] (163/402) udp://208.83.20.20:6969/announce 75ms — valid connect + announce
  [ALIVE] (164/402) udp://209.141.59.25:6969/announce 61ms — valid connect + announce
  [ALIVE] (165/402) udp://15.235.207.99:8081/announce 231ms — valid connect + announce
  [ALIVE] (166/402) udp://193.187.90.12:6969/announce 100ms — valid connect + announce
  [ALIVE] (167/402) udp://160.30.240.158:1337/announce 214ms — valid connect + announce
  [ALIVE] (168/402) udp://185.121.168.96:6969/announce 185ms — valid connect + announce
  [ALIVE] (169/402) udp://193.34.92.5:80/announce 124ms — valid connect + announce
  [ALIVE] (170/402) http://tracker.dhitechnical.com:6969/announce 3264ms — valid announce response
  [ALIVE] (171/402) udp://211.75.205.187:6969/announce 188ms — valid connect + announce
  [ALIVE] (172/402) udp://211.75.205.187:80/announce 188ms — valid connect + announce
  [ALIVE] (173/402) udp://23.154.104.2:23333/announce 86ms — valid connect + announce
  [ALIVE] (174/402) udp://211.75.205.188:6969/announce 188ms — valid connect + announce
  [ALIVE] (175/402) udp://212.42.38.197:6969/announce 126ms — valid connect + announce
  [ALIVE] (176/402) udp://23.175.184.30:23333/announce 31ms — valid connect + announce
  [ALIVE] (177/402) udp://211.75.205.188:80/announce 188ms — valid connect + announce
  [ALIVE] (178/402) udp://211.75.205.189:6969/announce 188ms — valid connect + announce
  [ALIVE] (179/402) udp://211.75.205.189:80/announce 188ms — valid connect + announce
  [ALIVE] (180/402) udp://34.66.57.33:1337/announce 29ms — valid connect + announce
  [ALIVE] (181/402) udp://211.75.210.221:6969/announce 190ms — valid connect + announce
  [ALIVE] (182/402) udp://23.157.120.14:6969/announce 71ms — valid connect + announce
  [ALIVE] (183/402) udp://34.66.57.33:80/announce 25ms — valid connect + announce
  [ALIVE] (184/402) udp://211.75.210.221:80/announce 189ms — valid connect + announce
  [ALIVE] (185/402) udp://221.153.216.56:8081/announce 177ms — valid connect + announce
  [ALIVE] (186/402) udp://51.222.82.36:6969/announce 15ms — valid connect + announce
  [ALIVE] (187/402) udp://31.38.161.123:6969/announce 108ms — valid connect + announce
  [ALIVE] (188/402) udp://31.56.179.159:6969/announce 109ms — valid connect + announce
  [ALIVE] (189/402) udp://43.250.54.126:6969/announce 84ms — valid connect + announce
  [ALIVE] (190/402) udp://51.81.222.188:6969/announce 64ms — valid connect + announce
  [ALIVE] (191/402) udp://31.59.141.120:6969/announce 121ms — valid connect + announce
  [ALIVE] (192/402) udp://52.211.139.85:27022/announce 69ms — valid connect + announce
  [ALIVE] (193/402) udp://74.119.149.136:6969/announce 1ms — valid connect + announce
  [ALIVE] (194/402) udp://51.15.41.46:6969/announce 94ms — valid connect + announce
  [ALIVE] (195/402) udp://45.137.199.107:6969/announce 100ms — valid connect + announce
  [ALIVE] (196/402) udp://45.38.170.167:6969/announce 114ms — valid connect + announce
  [ALIVE] (197/402) udp://43.154.112.29:17272/announce 198ms — valid connect + announce
  [ALIVE] (198/402) udp://85.17.55.112:6969/announce 87ms — valid connect + announce
  [ALIVE] (199/402) udp://65.109.28.17:6969/announce 121ms — valid connect + announce
  [ALIVE] (200/402) udp://89.234.156.205:451/announce 95ms — valid connect + announce
  [ALIVE] (201/402) udp://65.109.28.33:6969/announce 122ms — valid connect + announce
  [ALIVE] (202/402) udp://47.76.201.250:6969/announce 208ms — valid connect + announce
  [ALIVE] (203/402) udp://83.102.180.21:80/announce 131ms — valid connect + announce
  [ALIVE] (204/402) udp://60.249.37.20:6969/announce 188ms — valid connect + announce
  [ALIVE] (205/402) udp://60.172.236.18:6969/announce 209ms — valid connect + announce
  [ALIVE] (206/402) udp://60.249.37.20:80/announce 188ms — valid connect + announce
  [ALIVE] (207/402) udp://91.177.126.188:6969/announce 90ms — valid connect + announce
  [ALIVE] (208/402) udp://93.158.213.92:1337/announce 86ms — valid connect + announce
  [ALIVE] (209/402) udp://93.158.213.92:6969/announce 90ms — valid connect + announce
  [ALIVE] (210/402) udp://94.23.207.177:6969/announce 88ms — valid connect + announce
  [ALIVE] (211/402) udp://91.216.110.53:451/announce 95ms — valid connect + announce
  [ALIVE] (212/402) udp://91.211.5.21:6969/announce 140ms — valid connect + announce
  [ALIVE] (213/402) udp://95.217.80.20:6969/announce 121ms — valid connect + announce
  [ALIVE] (214/402) udp://evan.im:6969/announce 2ms — valid connect + announce
  [ALIVE] (215/402) udp://95.217.80.22:6969/announce 122ms — valid connect + announce
  [ALIVE] (216/402) udp://chihaya.toss.li:9696/announce 25ms — valid connect + announce
  [ALIVE] (217/402) udp://bttracker.debian.org:6969/announce 113ms — valid connect + announce
  [ALIVE] (218/402) udp://ipv4announce.sktorrent.eu:6969/announce 85ms — valid connect + announce
  [ALIVE] (219/402) udp://ch3oh.ru:6969/announce 133ms — valid connect + announce
  [ALIVE] (220/402) udp://90.226.147.124:6969/announce 292ms — valid connect + announce
  [ALIVE] (221/402) udp://leet-tracker.moe:23861/announce 27ms — valid connect + announce
  [ALIVE] (222/402) udp://leet-tracker.moe:38151/announce 27ms — valid connect + announce
  [ALIVE] (223/402) udp://leet-tracker.moe:1337/announce 27ms — valid connect + announce
  [ALIVE] (224/402) udp://ns575949.ip-51-222-82.net:6969/announce 15ms — valid connect + announce
  [DEAD]  (225/402) udp://open.stealth.si/announce — missing port
  [ALIVE] (226/402) udp://open.ftorrent.com:443/announce 42ms — valid connect + announce
  [ALIVE] (227/402) udp://mail.segso.net:6969/announce 121ms — valid connect + announce
  [ALIVE] (228/402) udp://opentrackr.org:1337/announce 84ms — valid connect + announce
  [ALIVE] (229/402) udp://open.stealth.si:80/announce 93ms — valid connect + announce
  [ALIVE] (230/402) udp://kolankoalastree.newtrackon.co.nz:1337/announce 197ms — valid connect + announce
  [ALIVE] (231/402) udp://anime-tracker.aruku.kro.kr:8081/announce 189ms — valid connect + announce
  [ALIVE] (232/402) udp://martin-gebhardt.eu:25/announce 99ms — valid connect + announce
  [ALIVE] (233/402) udp://qg.lorzl.gq:2710/announce 26ms — valid connect + announce
  [ALIVE] (234/402) udp://open.demonii.com:1337/announce 209ms — valid connect + announce
  [ALIVE] (235/402) udp://opentracker.lain.moscow:6969/announce 100ms — valid connect + announce
  [ALIVE] (236/402) udp://seedpeer.net:6969/announce 92ms — valid connect + announce
  [ALIVE] (237/402) udp://retracker01-msk-virt.corbina.net:80/announce 133ms — valid connect + announce
  [ALIVE] (238/402) udp://santost12.xyz:6969/announce 89ms — valid connect + announce
  [ALIVE] (239/402) udp://peerfect.org:6969/announce 121ms — valid connect + announce
  [ALIVE] (240/402) udp://t.overflow.biz:6969/announce 114ms — valid connect + announce
  [ALIVE] (241/402) udp://tr4ck3r.duckdns.org:6969/announce 15ms — valid connect + announce
  [ALIVE] (242/402) udp://tracker.004430.xyz:1337/announce 18ms — valid connect + announce
  [ALIVE] (243/402) udp://tracker-udp.anirena.com:80/announce 89ms — valid connect + announce
  [ALIVE] (244/402) udp://tracker-udp.gbitt.info:80/announce 83ms — valid connect + announce
  [ALIVE] (245/402) udp://tracker.auctor.tv:6969/announce 86ms — valid connect + announce
  [ALIVE] (246/402) udp://torrent.tracker.durukanbal.com:6969/announce 85ms — valid connect + announce
  [ALIVE] (247/402) udp://torrents.artixlinux.org:6969/announce 129ms — valid connect + announce
  [ALIVE] (248/402) udp://tracker.btzoo.eu:80/announce 26ms — valid connect + announce
  [ALIVE] (249/402) udp://tracker.aruku.ovh:8081/announce 221ms — valid connect + announce
  [ALIVE] (250/402) udp://tracker.cn.nyaa.net:6969/announce 195ms — valid connect + announce
  [ALIVE] (251/402) udp://tracker.ddunlimited.net:6969/announce 111ms — valid connect + announce
  [ALIVE] (252/402) udp://tracker.cyberia.is:6969/announce 119ms — valid connect + announce
  [ALIVE] (253/402) udp://tracker.dler.com:6969/announce 189ms — valid connect + announce
  [ALIVE] (254/402) udp://tracker.dler.org:6969/announce 188ms — valid connect + announce
  [ALIVE] (255/402) udp://tracker.farted.net:6969/announce 110ms — valid connect + announce
  [ALIVE] (256/402) udp://tracker.fatkhoala.org:13790/announce 27ms — valid connect + announce
  [ALIVE] (257/402) udp://tracker.ducks.party:1984/announce 91ms — valid connect + announce
  [ALIVE] (258/402) udp://explodie.org:6969/announce 90ms — valid connect (announce not confirmed)
  [ALIVE] (259/402) udp://tracker.gmi.gd:6969/announce 62ms — valid connect + announce
  [ALIVE] (260/402) udp://tracker.ilibr.org:6969/announce 122ms — valid connect + announce
  [ALIVE] (261/402) udp://tracker.ilibr.org:80/announce 118ms — valid connect + announce
  [ALIVE] (262/402) udp://tracker.k.vu:6969/announce 110ms — valid connect + announce
  [ALIVE] (263/402) udp://tracker.kali.org:6969/announce 3ms — valid connect + announce
  [ALIVE] (265/402) udp://tracker.novaopcj.eu.org:6969/announce 88ms — valid connect + announce
  [ALIVE] (266/402) udp://tracker.leechers-paradise.org:6969/announce 189ms — valid connect + announce
  [ALIVE] (268/402) udp://tracker.nyaa.net:6969/announce 123ms — valid connect + announce
  [ALIVE] (269/402) udp://tracker.nyaa.vc:6969/announce 86ms — valid connect + announce
  [ALIVE] (270/402) udp://tracker.opentorrent.top:6969/announce 115ms — valid connect + announce
  [ALIVE] (272/402) udp://tracker.opentrackr.com:1337/announce 119ms — valid connect + announce
  [ALIVE] (273/402) udp://tracker.opentrackr.com:6969/announce 117ms — valid connect + announce
  [ALIVE] (275/402) udp://tracker.opentrackr.org:1337/announce 89ms — valid connect + announce
  [ALIVE] (276/402) udp://tracker.orsvarn.com:6969/announce 98ms — valid connect + announce
  [ALIVE] (277/402) udp://tracker.qu.ax:6969/announce 90ms — valid connect + announce
  [ALIVE] (280/402) udp://tracker.peerfect.org:6969/announce 124ms — valid connect + announce
  [ALIVE] (282/402) udp://tracker.sigterm.xyz:6969/announce 91ms — valid connect + announce
  [ALIVE] (283/402) udp://tracker.segso.net:6969/announce 121ms — valid connect + announce
  [ALIVE] (284/402) udp://tracker.playground.ru:6969/announce 127ms — valid connect + announce
  [ALIVE] (285/402) udp://tracker.skynetcloud.site:6969/announce 88ms — valid connect + announce
  [ALIVE] (286/402) udp://tracker.teambelgium.net:6969/announce 87ms — valid connect + announce
  [ALIVE] (287/402) udp://tracker.wildkat.net:6969/announce 18ms — valid connect + announce
  [ALIVE] (288/402) udp://tracker.torrents.observer:80/announce 94ms — valid connect + announce
  [ALIVE] (289/402) udp://tracker2.dler.com:80/announce 188ms — valid connect + announce
  [ALIVE] (290/402) udp://tracker.uw0.xyz:6969/announce 89ms — valid connect + announce
  [ALIVE] (291/402) udp://tracker.torrent.eu.org:451/announce 96ms — valid connect + announce
  [ALIVE] (292/402) udp://tracker.willy.pro:6969/announce 252ms — valid connect + announce
  [ALIVE] (293/402) udp://tracker2.dler.org:80/announce 189ms — valid connect + announce
  [ALIVE] (295/402) udp://v2.iperson.xyz:6969/announce 228ms — valid connect + announce
  [ALIVE] (296/402) udp://yuptracker-eu.gaijinent.com:27022/announce 69ms — valid connect + announce
  [ALIVE] (299/402) udp://www.torrent.eu.org:451/announce 96ms — valid connect + announce
  [ALIVE] (300/402) wss://spacetradersapi-chatbox.herokuapp.com/announce 16ms — TLS reachable
  [ALIVE] (302/402) wss://tracker.openwebtorrent.com/announce 10ms — TLS reachable
  [ALIVE] (303/402) udp://yuptracker.gaijinent.com:27022/announce 98ms — valid connect + announce
  [ALIVE] (304/402) wss://tracker.files.fm:7073/announce 251ms — TLS reachable
  [ALIVE] (305/402) udp://yuptracker-us.gaijinent.com:27022/announce 3ms — valid connect + announce
  [ALIVE] (306/402) udp://zer0day.ch:1337/announce 87ms — valid connect + announce
  [ALIVE] (309/402) wss://tracker.webtorrent.dev/announce 296ms — TLS reachable
  [ALIVE] (313/402) wss://tracker.magnetoo.io/announce 553ms — TLS reachable
  [ALIVE] (315/402) udp://yuptracker-sa.gaijinent.com:27022/announce 227ms — valid connect + announce
  [ALIVE] (318/402) http://1337.abcvg.info:80/announce 902ms — valid announce response
  [ALIVE] (319/402) wss://tracker.openwebtorrent.com:443/announce 10ms — TLS reachable
  [DEAD]  (325/402) udp://185.121.168.96:1337/announce — no connect response
  [ALIVE] (338/402) http://107.189.2.131:1337/announce 196ms — valid announce response
  [DEAD]  (350/402) http://bt.poletracker.org:2710/announce — timeout
  [DEAD]  (375/402) http://200.168.117.238:6969/announce — URLError: <urlopen error timed out>
  [DEAD]  (400/402) udp://tracker4.itzmx.com:2710/announce — no connect response

[INFO] First pass done in 33.9s
[INFO] Second pass: re-testing top 100 alive trackers...
[INFO] Second pass done, refined 97 trackers
[INFO] Same-IP dedup removed 167 slower tracker(s)

===== Test Summary =====
  Total tested:   402
  Alive (raw):    132
  Alive (final):  59 (top 59 by composite score)
  Score-capped:   73
  Unsafe filtered:0
  Low-speed:      0 (>5s excluded)
  Same-IP dedup:  167 (kept faster)
  Dead final:     343
  Time:           42.0s
=== 协议分布统计 ===
  HTTP  : 117 个
  HTTPS : 31 个
  UDP   : 145 个
  WSS   : 6 个
  WS    : 0 个
  总计: 299 个（存活）
=========================
[OK]   /s/alive
[OK]   /s/all
[OK]   index.html
[OK] Pages regenerated with alive statistics.
[OK]   docs/alive.txt
[OK]   docs/merged.txt
[OK]   docs/cf_best.txt
[OK]   docs/ngosang_ip.txt
[OK]   docs/adysec_best.txt
[OK]   docs/adysec_http.txt
[OK]   docs/adysec_https.txt
[OK]   docs/adysec_udp.txt
[OK]   docs/adysec_wss.txt
[OK]   docs/anime_best.txt
[OK]   docs/anime_ip.txt
[OK]   docs/ultimate.txt
[OK]   docs/opentracker.txt
[OK] Plain-text files synced to docs/.

============================================================
 Round 1 - 2026-09-30 11:56:40
============================================================
  [PASS] Local tracker: trackers_cf_best.txt: 71 trackers
  [PASS] Local tracker: trackers_ngosang_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 332 trackers
  [PASS] Local tracker: trackers_adysec_http.txt: 131 trackers
  [PASS] Local tracker: trackers_adysec_https.txt: 32 trackers
  [PASS] Local tracker: trackers_adysec_udp.txt: 163 trackers
  [PASS] Local tracker: trackers_adysec_wss.txt: 6 trackers
  [PASS] Local tracker: trackers_anime_best.txt: 25 trackers
  [PASS] Local tracker: trackers_anime_ip.txt: 1 trackers
  [PASS] Local tracker: trackers_ultimate.txt: 183 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 38 trackers
  [PASS] Local tracker: trackers_merged.txt: 402 trackers
  [PASS] Local tracker: trackers_alive.txt: 59 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 59 trackers
  [PASS] Plain text: /merged.txt: 402 trackers
  [PASS] Plain text: /cf_best.txt: 71 trackers
  [PASS] Plain text: /ngosang_ip.txt: 20 trackers
  [PASS] Plain text: /adysec_best.txt: 332 trackers
  [PASS] Plain text: /adysec_http.txt: 131 trackers
  [PASS] Plain text: /adysec_https.txt: 32 trackers
  [PASS] Plain text: /adysec_udp.txt: 163 trackers
  [PASS] Plain text: /adysec_wss.txt: 6 trackers
  [PASS] Plain text: /anime_best.txt: 25 trackers
  [PASS] Plain text: /anime_ip.txt: 1 trackers
  [PASS] Plain text: /ultimate.txt: 183 trackers
  [PASS] Plain text: /opentracker.txt: 38 trackers
  [PASS] Alive count check: 59 in [0, 59]
  [PASS] Merged dedup check: 402 unique
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_cf_best.txt vs cf_best.txt: identical
  [PASS] Consistency: trackers_ngosang_ip.txt vs ngosang_ip.txt: identical
  [PASS] Consistency: trackers_adysec_best.txt vs adysec_best.txt: identical
  [PASS] Consistency: trackers_adysec_http.txt vs adysec_http.txt: identical
  [PASS] Consistency: trackers_adysec_https.txt vs adysec_https.txt: identical
  [PASS] Consistency: trackers_adysec_udp.txt vs adysec_udp.txt: identical
  [PASS] Consistency: trackers_adysec_wss.txt vs adysec_wss.txt: identical
  [PASS] Consistency: trackers_anime_best.txt vs anime_best.txt: identical
  [PASS] Consistency: trackers_anime_ip.txt vs anime_ip.txt: identical
  [PASS] Consistency: trackers_ultimate.txt vs ultimate.txt: identical
  [PASS] Consistency: trackers_opentracker.txt vs opentracker.txt: identical
  [PASS] URL format check: all 402 valid
------------------------------------------------------------
  Result: 49 passed, 0 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 1 rounds completed
   Total PASS: 49
   Total WARN: 0
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################

============================================================
 Round 1 - 2026-09-30 11:56:47
============================================================
  [PASS] Local tracker: trackers_cf_best.txt: 71 trackers
  [PASS] Local tracker: trackers_ngosang_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 332 trackers
  [PASS] Local tracker: trackers_adysec_http.txt: 131 trackers
  [PASS] Local tracker: trackers_adysec_https.txt: 32 trackers
  [PASS] Local tracker: trackers_adysec_udp.txt: 163 trackers
  [PASS] Local tracker: trackers_adysec_wss.txt: 6 trackers
  [PASS] Local tracker: trackers_anime_best.txt: 25 trackers
  [PASS] Local tracker: trackers_anime_ip.txt: 1 trackers
  [PASS] Local tracker: trackers_ultimate.txt: 183 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 38 trackers
  [PASS] Local tracker: trackers_merged.txt: 402 trackers
  [PASS] Local tracker: trackers_alive.txt: 59 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 59 trackers
  [PASS] Plain text: /merged.txt: 402 trackers
  [PASS] Plain text: /cf_best.txt: 71 trackers
  [PASS] Plain text: /ngosang_ip.txt: 20 trackers
  [PASS] Plain text: /adysec_best.txt: 332 trackers
  [PASS] Plain text: /adysec_http.txt: 131 trackers
  [PASS] Plain text: /adysec_https.txt: 32 trackers
  [PASS] Plain text: /adysec_udp.txt: 163 trackers
  [PASS] Plain text: /adysec_wss.txt: 6 trackers
  [PASS] Plain text: /anime_best.txt: 25 trackers
  [PASS] Plain text: /anime_ip.txt: 1 trackers
  [PASS] Plain text: /ultimate.txt: 183 trackers
  [PASS] Plain text: /opentracker.txt: 38 trackers
  [PASS] Alive count check: 59 in [0, 59]
  [PASS] Merged dedup check: 402 unique
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_cf_best.txt vs cf_best.txt: identical
  [PASS] Consistency: trackers_ngosang_ip.txt vs ngosang_ip.txt: identical
  [PASS] Consistency: trackers_adysec_best.txt vs adysec_best.txt: identical
  [PASS] Consistency: trackers_adysec_http.txt vs adysec_http.txt: identical
  [PASS] Consistency: trackers_adysec_https.txt vs adysec_https.txt: identical
  [PASS] Consistency: trackers_adysec_udp.txt vs adysec_udp.txt: identical
  [PASS] Consistency: trackers_adysec_wss.txt vs adysec_wss.txt: identical
  [PASS] Consistency: trackers_anime_best.txt vs anime_best.txt: identical
  [PASS] Consistency: trackers_anime_ip.txt vs anime_ip.txt: identical
  [PASS] Consistency: trackers_ultimate.txt vs ultimate.txt: identical
  [PASS] Consistency: trackers_opentracker.txt vs opentracker.txt: identical
  [PASS] URL format check: all 402 valid
  [PASS] Raw: alive (Raw): HTTP 200, 59 trackers
  [PASS] Raw: merged (Raw): HTTP 200, 402 trackers
  [PASS] Pages: /alive.txt: HTTP 200, 59 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 402 trackers
  [PASS] Pages short: /s/alive: HTTP 200, redirect OK
  [WARN] Pages short: /s/cf: unreachable: HTTP Error 404: Not Found
------------------------------------------------------------
  Result: 54 passed, 1 warnings, 0 failed
============================================================

============================================================
 Round 2 - 2026-09-30 11:56:52
============================================================
  [PASS] Local tracker: trackers_cf_best.txt: 71 trackers
  [PASS] Local tracker: trackers_ngosang_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 332 trackers
  [PASS] Local tracker: trackers_adysec_http.txt: 131 trackers
  [PASS] Local tracker: trackers_adysec_https.txt: 32 trackers
  [PASS] Local tracker: trackers_adysec_udp.txt: 163 trackers
  [PASS] Local tracker: trackers_adysec_wss.txt: 6 trackers
  [PASS] Local tracker: trackers_anime_best.txt: 25 trackers
  [PASS] Local tracker: trackers_anime_ip.txt: 1 trackers
  [PASS] Local tracker: trackers_ultimate.txt: 183 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 38 trackers
  [PASS] Local tracker: trackers_merged.txt: 402 trackers
  [PASS] Local tracker: trackers_alive.txt: 59 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 59 trackers
  [PASS] Plain text: /merged.txt: 402 trackers
  [PASS] Plain text: /cf_best.txt: 71 trackers
  [PASS] Plain text: /ngosang_ip.txt: 20 trackers
  [PASS] Plain text: /adysec_best.txt: 332 trackers
  [PASS] Plain text: /adysec_http.txt: 131 trackers
  [PASS] Plain text: /adysec_https.txt: 32 trackers
  [PASS] Plain text: /adysec_udp.txt: 163 trackers
  [PASS] Plain text: /adysec_wss.txt: 6 trackers
  [PASS] Plain text: /anime_best.txt: 25 trackers
  [PASS] Plain text: /anime_ip.txt: 1 trackers
  [PASS] Plain text: /ultimate.txt: 183 trackers
  [PASS] Plain text: /opentracker.txt: 38 trackers
  [PASS] Alive count check: 59 in [0, 59]
  [PASS] Merged dedup check: 402 unique
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_cf_best.txt vs cf_best.txt: identical
  [PASS] Consistency: trackers_ngosang_ip.txt vs ngosang_ip.txt: identical
  [PASS] Consistency: trackers_adysec_best.txt vs adysec_best.txt: identical
  [PASS] Consistency: trackers_adysec_http.txt vs adysec_http.txt: identical
  [PASS] Consistency: trackers_adysec_https.txt vs adysec_https.txt: identical
  [PASS] Consistency: trackers_adysec_udp.txt vs adysec_udp.txt: identical
  [PASS] Consistency: trackers_adysec_wss.txt vs adysec_wss.txt: identical
  [PASS] Consistency: trackers_anime_best.txt vs anime_best.txt: identical
  [PASS] Consistency: trackers_anime_ip.txt vs anime_ip.txt: identical
  [PASS] Consistency: trackers_ultimate.txt vs ultimate.txt: identical
  [PASS] Consistency: trackers_opentracker.txt vs opentracker.txt: identical
  [PASS] URL format check: all 402 valid
  [PASS] Raw: alive (Raw): HTTP 200, 59 trackers
  [PASS] Raw: merged (Raw): HTTP 200, 402 trackers
  [PASS] Pages: /alive.txt: HTTP 200, 59 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 402 trackers
  [PASS] Pages short: /s/alive: HTTP 200, redirect OK
  [WARN] Pages short: /s/cf: unreachable: HTTP Error 404: Not Found
------------------------------------------------------------
  Result: 54 passed, 1 warnings, 0 failed
============================================================

============================================================
 Round 3 - 2026-09-30 11:56:57
============================================================
  [PASS] Local tracker: trackers_cf_best.txt: 71 trackers
  [PASS] Local tracker: trackers_ngosang_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 332 trackers
  [PASS] Local tracker: trackers_adysec_http.txt: 131 trackers
  [PASS] Local tracker: trackers_adysec_https.txt: 32 trackers
  [PASS] Local tracker: trackers_adysec_udp.txt: 163 trackers
  [PASS] Local tracker: trackers_adysec_wss.txt: 6 trackers
  [PASS] Local tracker: trackers_anime_best.txt: 25 trackers
  [PASS] Local tracker: trackers_anime_ip.txt: 1 trackers
  [PASS] Local tracker: trackers_ultimate.txt: 183 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 38 trackers
  [PASS] Local tracker: trackers_merged.txt: 402 trackers
  [PASS] Local tracker: trackers_alive.txt: 59 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 59 trackers
  [PASS] Plain text: /merged.txt: 402 trackers
  [PASS] Plain text: /cf_best.txt: 71 trackers
  [PASS] Plain text: /ngosang_ip.txt: 20 trackers
  [PASS] Plain text: /adysec_best.txt: 332 trackers
  [PASS] Plain text: /adysec_http.txt: 131 trackers
  [PASS] Plain text: /adysec_https.txt: 32 trackers
  [PASS] Plain text: /adysec_udp.txt: 163 trackers
  [PASS] Plain text: /adysec_wss.txt: 6 trackers
  [PASS] Plain text: /anime_best.txt: 25 trackers
  [PASS] Plain text: /anime_ip.txt: 1 trackers
  [PASS] Plain text: /ultimate.txt: 183 trackers
  [PASS] Plain text: /opentracker.txt: 38 trackers
  [PASS] Alive count check: 59 in [0, 59]
  [PASS] Merged dedup check: 402 unique
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_cf_best.txt vs cf_best.txt: identical
  [PASS] Consistency: trackers_ngosang_ip.txt vs ngosang_ip.txt: identical
  [PASS] Consistency: trackers_adysec_best.txt vs adysec_best.txt: identical
  [PASS] Consistency: trackers_adysec_http.txt vs adysec_http.txt: identical
  [PASS] Consistency: trackers_adysec_https.txt vs adysec_https.txt: identical
  [PASS] Consistency: trackers_adysec_udp.txt vs adysec_udp.txt: identical
  [PASS] Consistency: trackers_adysec_wss.txt vs adysec_wss.txt: identical
  [PASS] Consistency: trackers_anime_best.txt vs anime_best.txt: identical
  [PASS] Consistency: trackers_anime_ip.txt vs anime_ip.txt: identical
  [PASS] Consistency: trackers_ultimate.txt vs ultimate.txt: identical
  [PASS] Consistency: trackers_opentracker.txt vs opentracker.txt: identical
  [PASS] URL format check: all 402 valid
  [PASS] Raw: alive (Raw): HTTP 200, 59 trackers
  [PASS] Raw: merged (Raw): HTTP 200, 402 trackers
  [PASS] Pages: /alive.txt: HTTP 200, 59 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 402 trackers
  [PASS] Pages short: /s/alive: HTTP 200, redirect OK
  [WARN] Pages short: /s/cf: unreachable: HTTP Error 404: Not Found
------------------------------------------------------------
  Result: 54 passed, 1 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 3 rounds completed
   Total PASS: 162
   Total WARN: 3
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################
=== End of diagnostics (Wed Sep 30 11:56:57 UTC 2026) ===
