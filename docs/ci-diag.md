=== Diagnostics Tue Sep 29 11:46:15 UTC 2026 ===
Python: Python 3.12.14
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://cf.trackerslist.com/best.txt
  HTTP 200, total 0.198407s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best_ip.txt
  HTTP 200, total 0.082539s
>>> https://tracker.adysec.com/trackers_best.txt
  HTTP 200, total 0.170575s
>>> https://tracker.adysec.com/trackers_best_http.txt
  HTTP 200, total 0.072513s
>>> https://tracker.adysec.com/trackers_best_https.txt
  HTTP 200, total 0.077421s
>>> https://tracker.adysec.com/trackers_best_udp.txt
  HTTP 200, total 0.040362s
>>> https://tracker.adysec.com/trackers_best_wss.txt
  HTTP 200, total 0.087277s
>>> https://raw.githubusercontent.com/DeSireFire/animeTrackerList/refs/heads/master/ATline_best.txt
  HTTP 200, total 0.140460s
>>> https://raw.githubusercontent.com/DeSireFire/animeTrackerList/refs/heads/master/ATline_best_ip.txt
  HTTP 200, total 0.136293s
[INFO] Repo: Pmwiu/Tracker-List, Max: 59
[CLEAN] trackers/trackers_adysec.txt
[CLEAN] docs/cf.txt
[CLEAN] docs/adysec.txt
[OK]   Cleaned 3 legacy files.

[INFO] trackers_cf_best.txt (cf-best)
[OK]   71 unique

[INFO] trackers_ngosang_ip.txt (ngosang-ip)
[OK]   20 unique

[INFO] trackers_adysec_best.txt (adysec-best)
[OK]   318 unique

[INFO] trackers_adysec_http.txt (adysec-http)
[OK]   115 unique

[INFO] trackers_adysec_https.txt (adysec-https)
[OK]   32 unique

[INFO] trackers_adysec_udp.txt (adysec-udp)
[OK]   165 unique

[INFO] trackers_adysec_wss.txt (adysec-wss)
[OK]   6 unique

[INFO] trackers_anime_best.txt (anime-best)
[OK]   25 unique

[INFO] trackers_anime_ip.txt (anime-ip)
[OK]   1 unique

[OK]   merged: 349
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

===== Summary =====
  trackers_cf_best.txt: 71
  trackers_ngosang_ip.txt: 20
  trackers_adysec_best.txt: 318
  trackers_adysec_http.txt: 115
  trackers_adysec_https.txt: 32
  trackers_adysec_udp.txt: 165
  trackers_adysec_wss.txt: 6
  trackers_anime_best.txt: 25
  trackers_anime_ip.txt: 1
  trackers_merged.txt: 349
  alive capped at 59 after test+sort
===================
[INFO] Testing 349 of 349 candidates (timeout=10s, workers=30, priority sources first)
[INFO] Max alive trackers after scoring: 59
  [ALIVE] (1/349) http://004430.xyz:80/announce 45ms — valid announce response
  [ALIVE] (2/349) http://207.241.226.111:6969/announce 134ms — valid announce response
  [ALIVE] (3/349) http://207.241.231.226:6969/announce 136ms — valid announce response
  [ALIVE] (4/349) http://216.144.239.90:6969/announce 133ms — valid announce response
  [ALIVE] (5/349) http://bittorrent.kali.org:80/announce 126ms — online (failure reason)
  [ALIVE] (6/349) http://185.126.65.92:6969/announce 172ms — valid announce response
  [ALIVE] (7/349) http://93.158.213.92:1337/announce 165ms — valid announce response
  [ALIVE] (8/349) http://135.125.198.235:2710/announce 182ms — valid announce response
  [ALIVE] (9/349) http://43.250.54.126:6969/announce 175ms — valid announce response
  [ALIVE] (10/349) http://94.23.207.177:6969/announce 174ms — valid announce response
  [ALIVE] (11/349) http://135.125.198.235:80/announce 188ms — valid announce response
  [ALIVE] (12/349) http://37.120.182.83:2710/announce 186ms — valid announce response
  [ALIVE] (13/349) http://37.120.182.83:80/announce 187ms — valid announce response
  [ALIVE] (14/349) http://31.38.161.123:6969/announce 215ms — valid announce response
  [ALIVE] (15/349) http://177.188.141.75:6969/announce 234ms — valid announce response
  [ALIVE] (16/349) http://1337.abcvg.info:80/announce 187ms — valid announce response
  [ALIVE] (17/349) http://211.75.205.187:6969/announce 375ms — valid announce response
  [ALIVE] (18/349) http://211.75.210.221:80/announce 374ms — valid announce response
  [ALIVE] (19/349) http://211.75.205.187:80/announce 381ms — valid announce response
  [ALIVE] (20/349) http://211.75.205.188:80/announce 382ms — valid announce response
  [ALIVE] (21/349) http://211.75.205.189:80/announce 381ms — valid announce response
  [ALIVE] (22/349) http://211.75.210.221:6969/announce 382ms — valid announce response
  [ALIVE] (23/349) http://60.249.37.20:80/announce 382ms — valid announce response
  [ALIVE] (24/349) http://60.249.37.20:6969/announce 387ms — valid announce response
  [ALIVE] (25/349) http://bt2.archive.org:6969/announce 136ms — valid announce response
  [ALIVE] (26/349) http://211.75.205.188:6969/announce 396ms — valid announce response
  [ALIVE] (27/349) http://211.75.205.189:6969/announce 402ms — valid announce response
  [ALIVE] (28/349) http://bt.zlofenix.org:81/announce 184ms — online (failure reason)
  [ALIVE] (29/349) http://bt1.archive.org:6969/announce 196ms — valid announce response
  [ALIVE] (30/349) http://announce.sktorrent.eu:6969/announce 389ms — valid announce response
  [ALIVE] (31/349) http://bt02.nnm-club.cc:2710/announce 312ms — online (failure reason)
  [ALIVE] (32/349) http://bttracker.debian.org:6969/announce 225ms — online (failure reason)
  [ALIVE] (33/349) http://bt02.nnm-club.info:2710/announce 267ms — online (failure reason)
  [ALIVE] (34/349) http://ehtracker.org:80/2541477/announce 167ms — online (failure reason)
  [ALIVE] (35/349) http://ehtracker.org:80/2496841/announce 170ms — online (failure reason)
  [ALIVE] (36/349) http://ehtracker.org:80/1226599/1080494xo5eXcwFOBq/announce 172ms — online (failure reason)
  [ALIVE] (37/349) http://ehtracker.org:80/1104308/announce 176ms — online (failure reason)
  [ALIVE] (38/349) http://ehtracker.org:80/2566145/1159106xUfsJkT9Btg/announce 174ms — online (failure reason)
  [ALIVE] (39/349) http://ehtracker.org:80/1/announce 173ms — online (failure reason)
  [ALIVE] (40/349) http://ehtracker.org:80/1113709/announce 179ms — online (failure reason)
  [ALIVE] (41/349) http://ipv4announce.sktorrent.eu:6969/announce 174ms — valid announce response
  [ALIVE] (42/349) http://open.demonii.si:80/announce 228ms — valid announce response
  [ALIVE] (43/349) http://t-backup.213891.xyz:80/announce 54ms — valid announce response
  [ALIVE] (44/349) http://nyaa.tracker.wf:7777/announce 343ms — valid announce response
  [ALIVE] (45/349) http://torrent.fedoraproject.org:6969/announce 40ms — online (failure reason)
  [ALIVE] (46/349) http://tr.nyacat.pw:80/announce 114ms — valid announce response
  [ALIVE] (47/349) http://tracker.004430.xyz:1337/announce 80ms — valid announce response
  [ALIVE] (48/349) http://bt.nnm-club.info:2710/announce 393ms — online (failure reason)
  [ALIVE] (49/349) http://t.nyaatracker.com:80/announce 232ms — valid announce response
  [ALIVE] (50/349) http://sukebei.tracker.wf:8888/announce 200ms — valid announce response
  [ALIVE] (51/349) http://tracker-udp.anirena.com:80/announce 180ms — online (failure reason)
  [ALIVE] (52/349) http://opentrackr.org:1337/announce 251ms — valid announce response
  [ALIVE] (53/349) http://tracker-zhuqiy.dgj055.icu:80/announce 227ms — valid announce response
  [ALIVE] (54/349) http://tracker.breizh.pm:6969/announce 186ms — valid announce response
  [ALIVE] (55/349) http://opentracker.acgnx.se:80/announce 583ms — online (failure reason)
  [ALIVE] (56/349) http://tracker.coppersurfer.site:2710/announce 180ms — valid announce response
  [ALIVE] (57/349) http://open.touki.ru:80/announce 478ms — online (failure reason)
  [ALIVE] (58/349) http://torrent.ubuntu.com:6969/announce 484ms — online (failure reason)
  [ALIVE] (59/349) http://tracker.gcvchp.com:2710/announce 124ms — online (failure reason)
  [ALIVE] (60/349) http://tracker.acgnx.se:80/announce 435ms — online (failure reason)
  [ALIVE] (61/349) http://tracker.auctor.tv:6969/announce 168ms — valid announce response
  [ALIVE] (62/349) http://retracker01-msk-virt.corbina.net:80/announce 398ms — valid announce response
  [ALIVE] (63/349) http://bt.beatrice-raws.org:80/announce 1514ms — online (failure reason)
  [ALIVE] (64/349) http://tracker.fansub.id:80/announce 309ms — valid announce response
  [ALIVE] (65/349) http://tracker.kali.org:6969/announce 9ms — online (failure reason)
  [ALIVE] (66/349) http://tracker.ali213.net:8000/announce 579ms — online (failure reason)
  [ALIVE] (67/349) http://tracker.ali213.net:8080/announce 604ms — online (failure reason)
  [ALIVE] (68/349) http://tracker.dler.org:6969/announce 515ms — valid announce response
  [ALIVE] (69/349) http://tracker.minglong.org:8080/announce 176ms — online (failure reason)
  [ALIVE] (70/349) http://tracker.dler.com:6969/announce 382ms — valid announce response
  [ALIVE] (71/349) http://opentracker.xyz:80/announce 806ms — valid announce response
  [ALIVE] (72/349) http://tracker.nyaa.vc:6969/announce 193ms — valid announce response
  [ALIVE] (73/349) http://tracker.opentorrent.top:6969/announce 207ms — valid announce response
  [ALIVE] (74/349) http://tracker.k.vu:6969/announce 264ms — valid announce response
  [ALIVE] (75/349) http://tracker.mywaifu.best:6969/announce 197ms — valid announce response
  [ALIVE] (76/349) http://tracker.gigatorrents.ws:2710/announce 469ms — online (failure reason)
  [ALIVE] (77/349) http://tracker.privateseedbox.xyz:2710/announce 181ms — valid announce response
  [ALIVE] (78/349) http://tracker.qu.ax:6969/announce 175ms — valid announce response
  [ALIVE] (79/349) http://tracker.pussytorrents.org:3000/announce 186ms — online (failure reason)
  [ALIVE] (80/349) http://tracker.trancetraffic.com:80/announce 67ms — online (failure reason)
  [ALIVE] (81/349) http://bt.edwardk.info:12891/announce 1867ms — online (failure reason)
  [ALIVE] (82/349) http://tracker.novaopcj.eu.org:6969/announce 167ms — valid announce response
  [ALIVE] (83/349) http://tracker.renfei.net:8080/announce 17ms — valid announce response
  [ALIVE] (84/349) http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 1994ms — valid announce response
  [ALIVE] (85/349) http://bt.edwardk.info:676/announce 1943ms — online (failure reason)
  [ALIVE] (86/349) http://tracker.opentrackr.org:1337/announce 441ms — valid announce response
  [ALIVE] (87/349) http://tracker.linkomanija.org:2710/announce 478ms — online (failure reason)
  [ALIVE] (88/349) https://004430.xyz:443/announce 60ms — valid announce response
  [ALIVE] (89/349) http://tracker.dm258.cn:7070/announce 583ms — online (failure reason)
  [ALIVE] (90/349) http://bt.edwardk.info:6767/announce 2003ms — online (failure reason)
  [ALIVE] (91/349) http://bt.edwardk.info:63124/announce 2037ms — online (failure reason)
  [ALIVE] (92/349) http://tracker.torrents.observer:80/announce 174ms — valid announce response
  [ALIVE] (93/349) http://www.arabp2p.net:2052/f5a1e35785c9f3885fd54f34b6e262b8/announce 127ms — online (failure reason)
  [ALIVE] (94/349) http://tracker.dhitechnical.com:6969/announce 1185ms — valid announce response
  [ALIVE] (95/349) http://tracker.zhuqiy.dgj055.icu:80/announce 227ms — valid announce response
  [ALIVE] (96/349) http://bt.edwardk.info:2710/announce 2158ms — online (failure reason)
  [ALIVE] (97/349) https://2.tracker.eu.org:443/announce 35ms — valid announce response
  [ALIVE] (98/349) http://tracker.waaa.moe:6969/announce 327ms — valid announce response
  [ALIVE] (99/349) https://t.213891.xyz:443/announce 19ms — valid announce response
  [ALIVE] (100/349) https://4.tracker.eu.org:443/announce 45ms — valid announce response
  [ALIVE] (101/349) https://1337.abcvg.info:443/announce 196ms — valid announce response
  [ALIVE] (102/349) https://1.tracker.eu.org:443/announce 35ms — valid announce response
  [ALIVE] (103/349) http://tracker.xn--djrq4gl4hvoi.top:80/announce 334ms — valid announce response
  [ALIVE] (104/349) http://tracker.xfapi.top:7070/announce 564ms — online (failure reason)
  [ALIVE] (105/349) http://tracker.xfapi.top:6868/announce 574ms — online (failure reason)
  [ALIVE] (106/349) http://tracker.xfapi.top:9999/announce 559ms — online (failure reason)
  [ALIVE] (107/349) http://bt.edwardk.info:6969/announce 2252ms — online (failure reason)
  [ALIVE] (108/349) http://bt.edwardk.info:4040/announce 2296ms — online (failure reason)
  [ALIVE] (109/349) https://3.tracker.eu.org:443/announce 32ms — valid announce response
  [ALIVE] (110/349) https://337hhh.xyz:443/announce 274ms — valid announce response
  [ALIVE] (111/349) http://tracker.zhuqiy.com:80/announce 227ms — valid announce response
  [ALIVE] (112/349) https://open.ftorrent.com:443/announce 130ms — valid announce response
  [ALIVE] (113/349) http://tracker3.dler.org:2710/announce 387ms — valid announce response
  [ALIVE] (114/349) https://tr.nyacat.pw:443/announce 116ms — valid announce response
  [ALIVE] (115/349) http://tracker.openzim.org:80/announce 708ms — online (failure reason)
  [ALIVE] (116/349) https://tracker.anibt.net:443/announce 107ms — online (failure reason)
  [ALIVE] (117/349) http://tracker2.dler.com:80/announce 377ms — valid announce response
  [ALIVE] (118/349) http://tracker2.dler.org:80/announce 468ms — valid announce response
  [ALIVE] (119/349) https://tracker.foreverpirates.co:443/announce 137ms — valid announce response
  [ALIVE] (120/349) https://t.btcland.xyz:443/announce 279ms — valid announce response
  [ALIVE] (121/349) https://tracker.7471.top:443/announce 127ms — valid announce response
  [ALIVE] (123/349) http://tracker1.itzmx.com:8080/announce 376ms — valid announce response
  [ALIVE] (124/349) https://torrent.ubuntu.com:443/announce 332ms — online (failure reason)
  [ALIVE] (125/349) https://5.tracker.eu.org:443/announce 38ms — valid announce response
  [ALIVE] (126/349) https://tracker-zhuqiy.dgj055.icu:443/announce 351ms — valid announce response
  [ALIVE] (127/349) udp://109.201.134.183:80/announce 87ms — valid connect + announce
  [ALIVE] (128/349) udp://149.106.106.25:443/announce 41ms — valid connect + announce
  [ALIVE] (129/349) https://tr2.trkb.ru:443/announce 290ms — valid announce response
  [ALIVE] (130/349) https://tr.torland.ga:443/announce 346ms — valid announce response
  [ALIVE] (131/349) https://tracker.nekomi.cn:443/announce 56ms — valid announce response
  [ALIVE] (132/349) https://tracker.monikadesign.uk:443/announce 331ms — online (failure reason)
  [ALIVE] (133/349) https://tracker.keepfrds.com:443/announce 279ms — online (failure reason)
  [ALIVE] (134/349) https://tracker.qingwapt.org:443/announce 138ms — online (failure reason)
  [ALIVE] (135/349) https://tr-zhuqiy-1.dgj055.icu:443/announce 343ms — valid announce response
  [ALIVE] (136/349) https://tr-zhuqiy-2.dgj055.icu:443/announce 350ms — valid announce response
  [ALIVE] (137/349) udp://135.125.198.235:1984/announce 92ms — valid connect + announce
  [ALIVE] (138/349) https://tracker.zhuqiy.com:443/announce 235ms — valid announce response
  [ALIVE] (139/349) udp://135.125.236.64:6969/announce 95ms — valid connect + announce
  [ALIVE] (140/349) udp://192.99.100.68:6969/announce 15ms — valid connect + announce
  [ALIVE] (141/349) udp://164.152.110.70:6969/announce 21ms — valid connect + announce
  [ALIVE] (142/349) udp://192.3.130.53:1337/announce 18ms — valid connect + announce
  [ALIVE] (143/349) udp://173.201.36.219:6969/announce 25ms — valid connect + announce
  [ALIVE] (144/349) https://tr-rh-zhuqiy.dgj055.icu:443/announce 350ms — valid announce response
  [ALIVE] (145/349) udp://193.148.251.93:6969/announce 42ms — valid connect + announce
  [ALIVE] (146/349) http://bt2.edwardk.info:6969/announce 2259ms — online (failure reason)
  [ALIVE] (147/349) http://bt2.edwardk.info:2710/announce 2258ms — online (failure reason)
  [ALIVE] (148/349) http://bt2.edwardk.info:4040/announce 2262ms — online (failure reason)
  [ALIVE] (149/349) https://bt.beatrice-raws.org:443/announce 678ms — online (failure reason)
  [ALIVE] (150/349) udp://132.226.6.145:6969/announce 165ms — valid connect + announce
  [ALIVE] (151/349) http://t.overflow.biz:6969/announce 250ms — valid announce response
  [ALIVE] (152/349) udp://151.242.104.187:80/announce 102ms — valid connect + announce
  [ALIVE] (153/349) udp://178.239.19.29:80/announce 85ms — valid connect + announce
  [ALIVE] (154/349) udp://180.131.145.175:6969/announce 79ms — valid connect + announce
  [ALIVE] (155/349) udp://208.83.20.20:6969/announce 69ms — valid connect + announce
  [ALIVE] (156/349) https://retracker2.x2k.ru:443/announce 581ms — valid announce response
  [ALIVE] (157/349) udp://185.216.179.62:25/announce 93ms — valid connect + announce
  [ALIVE] (158/349) udp://177.188.141.75:6969/announce 114ms — valid connect + announce
  [ALIVE] (159/349) udp://193.187.90.12:6969/announce 100ms — valid connect + announce
  [ALIVE] (160/349) udp://23.175.184.30:23333/announce 35ms — valid connect + announce
  [ALIVE] (161/349) udp://118.196.100.63:6969/announce 254ms — valid connect + announce
  [ALIVE] (162/349) udp://193.34.92.5:80/announce 122ms — valid connect + announce
  [ALIVE] (163/349) udp://120.78.150.131:6969/announce 252ms — valid connect + announce
  [ALIVE] (164/349) udp://34.66.57.33:1337/announce 31ms — valid connect + announce
  [ALIVE] (165/349) udp://34.66.57.33:80/announce 27ms — valid connect + announce
  [ALIVE] (166/349) udp://23.154.104.2:23333/announce 84ms — valid connect + announce
  [ALIVE] (167/349) udp://15.235.207.99:8081/announce 223ms — valid connect + announce
  [ALIVE] (168/349) udp://31.38.161.123:6969/announce 106ms — valid connect + announce
  [ALIVE] (169/349) udp://212.42.38.197:6969/announce 132ms — valid connect + announce
  [ALIVE] (170/349) udp://185.121.168.96:6969/announce 215ms — valid connect + announce
  [ALIVE] (171/349) udp://31.56.179.159:6969/announce 113ms — valid connect + announce
  [ALIVE] (172/349) udp://211.75.205.187:6969/announce 194ms — valid connect + announce
  [ALIVE] (173/349) udp://211.75.205.187:80/announce 188ms — valid connect + announce
  [ALIVE] (174/349) udp://37.120.182.83:15480/announce 93ms — valid connect + announce
  [ALIVE] (175/349) udp://211.75.205.188:6969/announce 190ms — valid connect + announce
  [ALIVE] (176/349) udp://211.75.205.188:80/announce 190ms — valid connect + announce
  [ALIVE] (177/349) udp://31.59.141.120:6969/announce 127ms — valid connect + announce
  [ALIVE] (178/349) udp://37.120.182.83:1984/announce 93ms — valid connect + announce
  [ALIVE] (179/349) udp://51.222.82.36:6969/announce 15ms — valid connect + announce
  [ALIVE] (180/349) udp://160.30.240.158:1337/announce 268ms — valid connect + announce
  [ALIVE] (181/349) udp://74.119.149.136:6969/announce 1ms — valid connect + announce
  [ALIVE] (182/349) udp://211.75.205.189:80/announce 190ms — valid connect + announce
  [ALIVE] (183/349) https://tracker.midnightprogrammer.net:443/announce 769ms — valid announce response
  [ALIVE] (184/349) udp://37.120.182.83:54123/announce 95ms — valid connect + announce
  [ALIVE] (185/349) udp://211.75.205.189:6969/announce 201ms — valid connect + announce
  [ALIVE] (186/349) udp://38.180.157.12:2715/announce 93ms — valid connect + announce
  [ALIVE] (187/349) udp://211.75.210.221:6969/announce 190ms — valid connect + announce
  [ALIVE] (188/349) udp://211.75.210.221:80/announce 201ms — valid connect + announce
  [ALIVE] (189/349) udp://221.153.216.56:8081/announce 193ms — valid connect + announce
  [ALIVE] (190/349) udp://43.250.54.126:6969/announce 89ms — valid connect + announce
  [ALIVE] (191/349) udp://45.137.199.107:6969/announce 84ms — valid connect + announce
  [ALIVE] (192/349) udp://51.81.222.188:6969/announce 71ms — valid connect + announce
  [ALIVE] (193/349) udp://52.211.139.85:27022/announce 71ms — valid connect + announce
  [ALIVE] (194/349) udp://45.38.170.167:6969/announce 105ms — valid connect + announce
  [ALIVE] (195/349) udp://51.15.41.46:6969/announce 94ms — valid connect + announce
  [ALIVE] (196/349) udp://85.17.55.112:6969/announce 83ms — valid connect + announce
  [ALIVE] (197/349) udp://89.234.156.205:451/announce 93ms — valid connect + announce
  [ALIVE] (198/349) udp://91.177.126.188:6969/announce 93ms — valid connect + announce
  [ALIVE] (199/349) udp://93.158.213.92:1337/announce 88ms — valid connect + announce
  [ALIVE] (200/349) udp://90.226.147.124:6969/announce 106ms — valid connect + announce
  [ALIVE] (201/349) udp://65.109.28.33:6969/announce 115ms — valid connect + announce
  [ALIVE] (202/349) udp://65.109.28.17:6969/announce 116ms — valid connect + announce
  [ALIVE] (203/349) udp://94.23.207.177:6969/announce 87ms — valid connect + announce
  [ALIVE] (204/349) udp://93.158.213.92:6969/announce 91ms — valid connect + announce
  [ALIVE] (205/349) udp://43.154.112.29:17272/announce 198ms — valid connect + announce
  [ALIVE] (206/349) udp://83.102.180.21:80/announce 130ms — valid connect + announce
  [ALIVE] (207/349) udp://91.211.5.21:6969/announce 120ms — valid connect + announce
  [ALIVE] (208/349) udp://95.217.80.20:6969/announce 115ms — valid connect + announce
  [ALIVE] (209/349) udp://evan.im:6969/announce 2ms — valid connect + announce
  [ALIVE] (210/349) udp://95.217.80.22:6969/announce 116ms — valid connect + announce
  [ALIVE] (211/349) udp://chihaya.toss.li:9696/announce 25ms — valid connect + announce
  [ALIVE] (212/349) udp://47.76.201.250:6969/announce 199ms — valid connect + announce
  [ALIVE] (213/349) udp://leet-tracker.moe:1337/announce 27ms — valid connect + announce
  [ALIVE] (214/349) udp://leet-tracker.moe:23861/announce 26ms — valid connect + announce
  [ALIVE] (215/349) udp://leet-tracker.moe:38151/announce 28ms — valid connect + announce
  [ALIVE] (216/349) udp://bttracker.debian.org:6969/announce 115ms — valid connect + announce
  [ALIVE] (217/349) udp://60.249.37.20:6969/announce 188ms — valid connect + announce
  [ALIVE] (218/349) udp://ipv4announce.sktorrent.eu:6969/announce 87ms — valid connect + announce
  [ALIVE] (219/349) udp://60.249.37.20:80/announce 193ms — valid connect + announce
  [ALIVE] (220/349) udp://ns575949.ip-51-222-82.net:6969/announce 15ms — valid connect + announce
  [ALIVE] (221/349) udp://open.ftorrent.com:443/announce 63ms — valid connect + announce
  [ALIVE] (223/349) udp://opentrackr.org:1337/announce 86ms — valid connect + announce
  [ALIVE] (224/349) udp://explodie.org:6969/announce 104ms — valid connect + announce
  [ALIVE] (225/349) udp://60.172.236.18:6969/announce 274ms — valid connect + announce
  [ALIVE] (226/349) udp://ch3oh.ru:6969/announce 134ms — valid connect + announce
  [ALIVE] (227/349) udp://mail.segso.net:6969/announce 116ms — valid connect + announce
  [ALIVE] (228/349) udp://santost12.xyz:6969/announce 91ms — valid connect + announce
  [ALIVE] (229/349) udp://tr4ck3r.duckdns.org:6969/announce 15ms — valid connect + announce
  [ALIVE] (230/349) udp://tracker.004430.xyz:1337/announce 18ms — valid connect + announce
  [ALIVE] (231/349) udp://open.stealth.si:80/announce 92ms — valid connect + announce
  [ALIVE] (232/349) udp://t.overflow.biz:6969/announce 114ms — valid connect + announce
  [ALIVE] (233/349) udp://seedpeer.net:6969/announce 76ms — valid connect + announce
  [ALIVE] (234/349) udp://retracker01-msk-virt.corbina.net:80/announce 132ms — valid connect + announce
  [ALIVE] (235/349) udp://martin-gebhardt.eu:25/announce 97ms — valid connect + announce
  [ALIVE] (236/349) udp://209.141.59.25:6969/announce 614ms — valid connect + announce
  [ALIVE] (237/349) udp://tracker.bittor.pw:1337/announce 26ms — valid connect + announce
  [ALIVE] (238/349) udp://qg.lorzl.gq:2710/announce 25ms — valid connect + announce
  [ALIVE] (239/349) udp://peerfect.org:6969/announce 116ms — valid connect + announce
  [ALIVE] (240/349) udp://rekcart.duckdns.org:15480/announce 99ms — valid connect + announce
  [ALIVE] (241/349) udp://open.demonii.com:1337/announce 206ms — valid connect + announce
  [ALIVE] (242/349) udp://tracker-udp.anirena.com:80/announce 91ms — valid connect + announce
  [ALIVE] (243/349) udp://tracker.corpscorp.online:80/announce 28ms — valid connect + announce
  [ALIVE] (244/349) udp://opentracker.lain.moscow:6969/announce 95ms — valid connect + announce
  [ALIVE] (245/349) udp://kolankoalastree.newtrackon.co.nz:1337/announce 254ms — valid connect + announce
  [ALIVE] (246/349) udp://tracker.auctor.tv:6969/announce 86ms — valid connect + announce
  [ALIVE] (247/349) udp://tracker.breizh.pm:6969/announce 92ms — valid connect + announce
  [ALIVE] (248/349) udp://tr3.ysagin.top:2715/announce 91ms — valid connect + announce
  [ALIVE] (249/349) udp://tracker.kali.org:6969/announce 2ms — valid connect + announce
  [ALIVE] (250/349) udp://tracker-udp.gbitt.info:80/announce 87ms — valid connect + announce
  [ALIVE] (251/349) udp://torrent.tracker.durukanbal.com:6969/announce 82ms — valid connect + announce
  [ALIVE] (252/349) udp://anime-tracker.aruku.kro.kr:8081/announce 185ms — valid connect + announce
  [ALIVE] (253/349) udp://tracker.btzoo.eu:80/announce 27ms — valid connect + announce
  [ALIVE] (254/349) udp://torrents.artixlinux.org:6969/announce 129ms — valid connect + announce
  [ALIVE] (255/349) udp://tracker.ddunlimited.net:6969/announce 106ms — valid connect + announce
  [ALIVE] (256/349) udp://tracker.fatkhoala.org:13790/announce 26ms — valid connect + announce
  [ALIVE] (257/349) udp://tracker.fatkhoala.org:13710/announce 31ms — valid connect + announce
  [ALIVE] (258/349) http://140.235.237.23:6969/announce 4319ms — valid announce response
  [ALIVE] (259/349) udp://tracker.novaopcj.eu.org:6969/announce 86ms — valid connect + announce
  [ALIVE] (260/349) udp://tracker.ducks.party:1984/announce 91ms — valid connect + announce
  [ALIVE] (261/349) udp://tracker.k.vu:6969/announce 119ms — valid connect + announce
  [ALIVE] (262/349) udp://tracker.farted.net:6969/announce 108ms — valid connect + announce
  [ALIVE] (263/349) udp://tracker.nyaa.vc:6969/announce 92ms — valid connect + announce
  [ALIVE] (264/349) udp://tracker.opentorrent.top:6969/announce 96ms — valid connect + announce
  [ALIVE] (265/349) udp://tracker.dler.com:6969/announce 190ms — valid connect + announce
  [ALIVE] (266/349) udp://tracker.cyberia.is:6969/announce 117ms — valid connect + announce
  [ALIVE] (267/349) udp://tracker.opentrackr.org:1337/announce 88ms — valid connect + announce
  [ALIVE] (268/349) udp://tracker.dler.org:6969/announce 191ms — valid connect + announce
  [ALIVE] (269/349) udp://tracker.cn.nyaa.net:6969/announce 213ms — valid connect + announce
  [ALIVE] (270/349) udp://tracker.opentrackr.com:6969/announce 114ms — valid connect + announce
  [ALIVE] (271/349) udp://tracker.opentrackr.com:1337/announce 116ms — valid connect + announce
  [ALIVE] (272/349) udp://tracker.tallpenguin.org:15750/announce 27ms — valid connect + announce
  [ALIVE] (273/349) udp://tracker.nyaa.net:6969/announce 128ms — valid connect + announce
  [ALIVE] (274/349) udp://tracker.ilibr.org:80/announce 114ms — valid connect + announce
  [ALIVE] (275/349) udp://tracker.ilibr.org:6969/announce 114ms — valid connect + announce
  [ALIVE] (276/349) udp://tracker.aruku.ovh:8081/announce 221ms — valid connect + announce
  [ALIVE] (277/349) udp://tracker.qu.ax:6969/announce 90ms — valid connect + announce
  [ALIVE] (278/349) udp://tracker.orsvarn.com:6969/announce 95ms — valid connect + announce
  [ALIVE] (279/349) udp://tracker.wildkat.net:6969/announce 17ms — valid connect + announce
  [ALIVE] (280/349) udp://tracker.torrents.observer:80/announce 85ms — valid connect + announce
  [ALIVE] (281/349) udp://tracker.sigterm.xyz:6969/announce 90ms — valid connect + announce
  [ALIVE] (282/349) udp://tracker.segso.net:6969/announce 114ms — valid connect + announce
  [ALIVE] (283/349) udp://tracker.peerfect.org:6969/announce 115ms — valid connect + announce
  [ALIVE] (284/349) udp://tracker.skynetcloud.site:6969/announce 94ms — valid connect + announce
  [ALIVE] (285/349) udp://tracker.teambelgium.net:6969/announce 89ms — valid connect + announce
  [ALIVE] (286/349) udp://tracker.leechers-paradise.org:6969/announce 190ms — valid connect + announce
  [ALIVE] (287/349) udp://tracker2.dler.com:80/announce 190ms — valid connect + announce
  [ALIVE] (288/349) udp://tracker.uw0.xyz:6969/announce 87ms — valid connect + announce
  [ALIVE] (289/349) udp://tracker2.dler.org:80/announce 191ms — valid connect + announce
  [ALIVE] (290/349) wss://tracker.openwebtorrent.com/announce 10ms — TLS reachable
  [ALIVE] (291/349) udp://yuptracker-eu.gaijinent.com:27022/announce 72ms — valid connect + announce
  [ALIVE] (292/349) udp://tracker.playground.ru:6969/announce 127ms — valid connect + announce
  [ALIVE] (294/349) wss://spacetradersapi-chatbox.herokuapp.com/announce 219ms — TLS reachable
  [ALIVE] (295/349) udp://yuptracker.gaijinent.com:27022/announce 98ms — valid connect + announce
  [ALIVE] (296/349) wss://tracker.files.fm:7073/announce 237ms — TLS reachable
  [ALIVE] (298/349) udp://v2.iperson.xyz:6969/announce 251ms — valid connect + announce
  [ALIVE] (300/349) udp://tracker.willy.pro:6969/announce 246ms — valid connect + announce
  [ALIVE] (301/349) udp://yuptracker-us.gaijinent.com:27022/announce 2ms — valid connect + announce
  [ALIVE] (303/349) udp://zer0day.ch:1337/announce 91ms — valid connect + announce
  [ALIVE] (304/349) wss://tracker.magnetoo.io/announce 228ms — TLS reachable
  [ALIVE] (305/349) wss://tracker.openwebtorrent.com:443/announce 10ms — TLS reachable
  [ALIVE] (309/349) wss://tracker.webtorrent.dev/announce 296ms — TLS reachable
  [ALIVE] (314/349) udp://www.torrent.eu.org:451/announce 102ms — valid connect + announce
  [ALIVE] (319/349) udp://tracker.gmi.gd:6969/announce 518ms — valid connect + announce
  [DEAD]  (325/349) https://tr.burnabyhighstar.com:443/announce — URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'tr.burnabyhighstar.com'. (_ssl.c:1010)>
  [ALIVE] (326/349) udp://yuptracker-sa.gaijinent.com:27022/announce 234ms — valid connect + announce
  [ALIVE] (327/349) udp://185.121.168.96:1337/announce 198ms — valid connect (announce not confirmed)
  [ALIVE] (328/349) http://tracker.ddunlimited.net:6969/announce 4950ms — online (failure reason)
  [ALIVE] (329/349) udp://tracker.tryhackx.org:6969/announce 92ms — valid connect (announce not confirmed)
  [ALIVE] (330/349) udp://143.20.154.229:42069/announce 2396ms — valid connect (announce not confirmed)
  [ALIVE] (332/349) https://retracker.x2k.ru:443/announce 8126ms — valid announce response

[INFO] First pass done in 15.6s
[INFO] Second pass: re-testing top 100 alive trackers...
[INFO] Second pass done, refined 90 trackers
[INFO] Low-speed filtered (>5s): 1 trackers
[INFO] Same-IP dedup removed 173 slower tracker(s)

===== Test Summary =====
  Total tested:   349
  Alive (raw):    134
  Alive (final):  59 (top 59 by composite score)
  Score-capped:   75
  Unsafe filtered:0
  Low-speed:      1 (>5s excluded)
  Same-IP dedup:  173 (kept faster)
  Dead final:     290
  Time:           24.8s
=== 协议分布统计 ===
  HTTP  : 114 个
  HTTPS : 31 个
  UDP   : 157 个
  WSS   : 6 个
  WS    : 0 个
  总计: 308 个（存活）
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
[OK] Plain-text files synced to docs/.

============================================================
 Round 1 - 2026-09-29 11:46:41
============================================================
  [PASS] Local tracker: trackers_cf_best.txt: 71 trackers
  [PASS] Local tracker: trackers_ngosang_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 318 trackers
  [PASS] Local tracker: trackers_adysec_http.txt: 115 trackers
  [PASS] Local tracker: trackers_adysec_https.txt: 32 trackers
  [PASS] Local tracker: trackers_adysec_udp.txt: 165 trackers
  [PASS] Local tracker: trackers_adysec_wss.txt: 6 trackers
  [PASS] Local tracker: trackers_anime_best.txt: 25 trackers
  [PASS] Local tracker: trackers_anime_ip.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 349 trackers
  [PASS] Local tracker: trackers_alive.txt: 59 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 59 trackers
  [PASS] Plain text: /merged.txt: 349 trackers
  [PASS] Plain text: /cf_best.txt: 71 trackers
  [PASS] Plain text: /ngosang_ip.txt: 20 trackers
  [PASS] Plain text: /adysec_best.txt: 318 trackers
  [PASS] Plain text: /adysec_http.txt: 115 trackers
  [PASS] Plain text: /adysec_https.txt: 32 trackers
  [PASS] Plain text: /adysec_udp.txt: 165 trackers
  [PASS] Plain text: /adysec_wss.txt: 6 trackers
  [PASS] Plain text: /anime_best.txt: 25 trackers
  [PASS] Plain text: /anime_ip.txt: 1 trackers
  [PASS] Alive count check: 59 in [0, 59]
  [PASS] Merged dedup check: 349 unique
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
  [PASS] URL format check: all 349 valid
------------------------------------------------------------
  Result: 43 passed, 0 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 1 rounds completed
   Total PASS: 43
   Total WARN: 0
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################
=== End of diagnostics (Tue Sep 29 11:46:56 UTC 2026) ===
