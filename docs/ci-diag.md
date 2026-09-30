=== Diagnostics Wed Sep 30 11:59:37 UTC 2026 ===
Python: Python 3.12.14
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://cf.trackerslist.com/best.txt
  HTTP 200, total 0.119112s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best_ip.txt
  HTTP 200, total 0.091853s
>>> https://tracker.adysec.com/trackers_best.txt
  HTTP 200, total 0.182203s
>>> https://tracker.adysec.com/trackers_best_http.txt
  HTTP 200, total 0.203058s
>>> https://tracker.adysec.com/trackers_best_https.txt
  HTTP 200, total 0.192743s
>>> https://tracker.adysec.com/trackers_best_udp.txt
  HTTP 200, total 0.187000s
>>> https://tracker.adysec.com/trackers_best_wss.txt
  HTTP 200, total 0.178967s
>>> https://raw.githubusercontent.com/DeSireFire/animeTrackerList/refs/heads/master/ATline_best.txt
  HTTP 200, total 0.150967s
>>> https://raw.githubusercontent.com/DeSireFire/animeTrackerList/refs/heads/master/ATline_best_ip.txt
  HTTP 200, total 0.139979s
>>> https://raw.githubusercontent.com/kris3713/UltimateBTTrackersList/refs/heads/master/ultimate_trackers.txt
  HTTP 200, total 0.154500s
>>> https://raw.githubusercontent.com/1265578519/OpenTracker/master/tracker.txt
  HTTP 200, total 0.251882s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.122605s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_i2p.txt
  HTTP 200, total 0.208336s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_yggdrasil.txt
  HTTP 200, total 0.132406s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ip.txt
  HTTP 200, total 0.091928s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_yggdrasil_ip.txt
  HTTP 200, total 0.155021s
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

[INFO] trackers_ngosang_best.txt (ngosang-best)
[OK]   20 unique

[INFO] trackers_ngosang_i2p.txt (ngosang-i2p)
[OK]   17 unique

[INFO] trackers_ngosang_ygg.txt (ngosang-ygg)
[OK]   1 unique

[INFO] trackers_ngosang_all_ip.txt (ngosang-all-ip)
[OK]   55 unique

[INFO] trackers_ngosang_ygg_ip.txt (ngosang-ygg-ip)
[OK]   4 unique

[OK]   merged: 425
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
[OK]   docs/ngosang_best.txt
[OK]   docs/ngosang_i2p.txt
[OK]   docs/ngosang_ygg.txt
[OK]   docs/ngosang_all_ip.txt
[OK]   docs/ngosang_ygg_ip.txt

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
  trackers_ngosang_best.txt: 20
  trackers_ngosang_i2p.txt: 17
  trackers_ngosang_ygg.txt: 1
  trackers_ngosang_all_ip.txt: 55
  trackers_ngosang_ygg_ip.txt: 4
  trackers_merged.txt: 425
  alive capped at 59 after test+sort
===================
[INFO] Testing 425 of 425 candidates (timeout=10s, workers=30, priority sources first)
[INFO] Max alive trackers after scoring: 59
  [ALIVE] (1/425) http://207.241.226.111:6969/announce 37ms — valid announce response
  [ALIVE] (2/425) http://207.241.231.226:6969/announce 42ms — valid announce response
  [ALIVE] (3/425) http://004430.xyz:80/announce 97ms — valid announce response
  [ALIVE] (4/425) http://bt.edwardk.info:2710/announce 147ms — online (failure reason)
  [ALIVE] (5/425) http://bt.edwardk.info:12891/announce 149ms — online (failure reason)
  [ALIVE] (6/425) http://43.250.54.126:6969/announce 268ms — valid announce response
  [ALIVE] (7/425) http://185.126.65.92:6969/announce 277ms — valid announce response
  [ALIVE] (8/425) http://93.158.213.92:1337/announce 270ms — valid announce response
  [ALIVE] (9/425) http://bt.edwardk.info:4040/announce 150ms — online (failure reason)
  [ALIVE] (10/425) http://211.75.205.188:6969/announce 279ms — valid announce response
  [ALIVE] (11/425) http://211.75.205.189:6969/announce 279ms — valid announce response
  [ALIVE] (12/425) http://211.75.205.187:6969/announce 281ms — valid announce response
  [ALIVE] (13/425) http://31.38.161.123:6969/announce 278ms — valid announce response
  [ALIVE] (14/425) http://211.75.205.189:80/announce 280ms — valid announce response
  [ALIVE] (15/425) http://211.75.205.188:80/announce 282ms — valid announce response
  [ALIVE] (16/425) http://211.75.210.221:80/announce 281ms — valid announce response
  [ALIVE] (17/425) http://60.249.37.20:6969/announce 280ms — valid announce response
  [ALIVE] (18/425) http://135.125.198.235:80/announce 293ms — valid announce response
  [ALIVE] (19/425) http://211.75.205.187:80/announce 292ms — valid announce response
  [ALIVE] (20/425) http://94.23.207.177:6969/announce 287ms — valid announce response
  [ALIVE] (21/425) http://211.75.210.221:6969/announce 293ms — valid announce response
  [ALIVE] (22/425) http://135.125.198.235:2710/announce 302ms — valid announce response
  [ALIVE] (23/425) http://60.249.37.20:80/announce 294ms — valid announce response
  [ALIVE] (24/425) http://177.188.141.75:6969/announce 310ms — valid announce response
  [ALIVE] (25/425) http://bt.edwardk.info:676/announce 136ms — online (failure reason)
  [ALIVE] (26/425) http://79.111.12.213:6969/announce 344ms — online (failure reason)
  [ALIVE] (27/425) http://bt.edwardk.info:63124/announce 152ms — online (failure reason)
  [ALIVE] (28/425) http://announce.sktorrent.eu:6969/announce 305ms — valid announce response
  [ALIVE] (29/425) http://bittorrent.kali.org:80/announce 129ms — online (failure reason)
  [ALIVE] (30/425) http://bt1.archive.org:6969/announce 46ms — valid announce response
  [ALIVE] (31/425) http://bt2.archive.org:6969/announce 61ms — valid announce response
  [ALIVE] (32/425) http://bt.edwardk.info:6767/announce 148ms — online (failure reason)
  [ALIVE] (33/425) http://bt.edwardk.info:6969/announce 149ms — online (failure reason)
  [ALIVE] (34/425) http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 348ms — valid announce response
  [ALIVE] (35/425) http://216.144.239.90:6969/announce 433ms — valid announce response
  [ALIVE] (36/425) http://bt2.edwardk.info:4040/announce 135ms — online (failure reason)
  [ALIVE] (37/425) http://bt2.edwardk.info:2710/announce 141ms — online (failure reason)
  [ALIVE] (38/425) http://bt2.edwardk.info:6969/announce 149ms — online (failure reason)
  [ALIVE] (39/425) http://ipv4announce.sktorrent.eu:6969/announce 287ms — valid announce response
  [ALIVE] (40/425) http://ehtracker.org:80/1104308/announce 264ms — online (failure reason)
  [ALIVE] (41/425) http://ehtracker.org:80/2496841/announce 264ms — online (failure reason)
  [ALIVE] (42/425) http://ehtracker.org:80/1226599/1080494xo5eXcwFOBq/announce 262ms — online (failure reason)
  [ALIVE] (43/425) http://ehtracker.org:80/1113709/announce 262ms — online (failure reason)
  [ALIVE] (44/425) http://ehtracker.org:80/2566145/1159106xUfsJkT9Btg/announce 263ms — online (failure reason)
  [ALIVE] (45/425) http://ehtracker.org:80/2541477/announce 263ms — online (failure reason)
  [ALIVE] (46/425) http://ehtracker.org:80/1/announce 271ms — online (failure reason)
  [ALIVE] (47/425) http://bt.beatrice-raws.org:80/announce 540ms — online (failure reason)
  [ALIVE] (48/425) http://bttracker.debian.org:6969/announce 315ms — online (failure reason)
  [ALIVE] (49/425) http://open.demonii.si:80/announce 334ms — valid announce response
  [ALIVE] (50/425) http://ch3oh.ru:6969/announce 383ms — online (failure reason)
  [ALIVE] (51/425) http://nyaa.tracker.wf:7777/announce 405ms — valid announce response
  [ALIVE] (52/425) http://t-backup.213891.xyz:80/announce 137ms — valid announce response
  [ALIVE] (53/425) http://sukebei.tracker.wf:8888/announce 288ms — valid announce response
  [ALIVE] (54/425) http://tr.nyacat.pw:80/announce 160ms — valid announce response
  [ALIVE] (55/425) http://bt02.nnm-club.cc:2710/announce 432ms — online (failure reason)
  [ALIVE] (56/425) http://t.nyaatracker.com:80/announce 334ms — valid announce response
  [ALIVE] (57/425) http://retracker.x2k.ru:80/announce 419ms — valid announce response
  [ALIVE] (58/425) http://tracker.004430.xyz:1337/announce 134ms — valid announce response
  [ALIVE] (59/425) http://tracker-udp.anirena.com:80/announce 258ms — online (failure reason)
  [ALIVE] (60/425) http://bt.zlofenix.org:81/announce 754ms — online (failure reason)
  [ALIVE] (61/425) http://opentrackr.org:1337/announce 408ms — valid announce response
  [ALIVE] (62/425) http://open.touki.ru:80/announce 677ms — online (failure reason)
  [ALIVE] (63/425) http://tracker.acgnx.se:80/announce 422ms — online (failure reason)
  [ALIVE] (64/425) http://tracker.coppersurfer.site:2710/announce 301ms — valid announce response
  [ALIVE] (65/425) http://opentracker.acgnx.se:80/announce 933ms — online (failure reason)
  [ALIVE] (66/425) http://retracker01-msk-virt.corbina.net:80/announce 562ms — valid announce response
  [ALIVE] (67/425) http://tracker-zhuqiy.dgj055.icu:80/announce 325ms — valid announce response
  [ALIVE] (68/425) http://tracker.ali213.net:8080/announce 444ms — online (failure reason)
  [ALIVE] (69/425) http://tracker.ddunlimited.net:6969/announce 322ms — online (failure reason)
  [ALIVE] (70/425) http://tracker.auctor.tv:6969/announce 269ms — valid announce response
  [ALIVE] (71/425) http://tracker.ali213.net:8000/announce 470ms — online (failure reason)
  [ALIVE] (72/425) http://tracker.gcvchp.com:2710/announce 40ms — online (failure reason)
  [ALIVE] (73/425) http://torrent.unix-ag.uni-kl.de:80/announce 466ms — online (failure reason)
  [ALIVE] (74/425) http://torrent.ubuntu.com:6969/announce 778ms — online (failure reason)
  [ALIVE] (75/425) http://tracker.dhitechnical.com:6969/announce 330ms — valid announce response
  [ALIVE] (76/425) http://bt02.nnm-club.info:2710/announce 718ms — online (failure reason)
  [ALIVE] (77/425) http://bt.nnm-club.info:2710/announce 563ms — online (failure reason)
  [ALIVE] (78/425) http://tracker.dler.org:6969/announce 441ms — valid announce response
  [ALIVE] (79/425) http://open.tracker.cl:1337/announce 815ms — valid announce response
  [ALIVE] (80/425) http://tracker.fansub.id:80/announce 367ms — valid announce response
  [ALIVE] (81/425) http://opentracker.xyz:80/announce 939ms — valid announce response
  [ALIVE] (82/425) http://tracker.kali.org:6969/announce 118ms — online (failure reason)
  [ALIVE] (83/425) http://tracker.dler.com:6969/announce 301ms — valid announce response
  [ALIVE] (84/425) http://tracker.mywaifu.best:6969/announce 289ms — valid announce response
  [ALIVE] (85/425) http://tracker.minglong.org:8080/announce 266ms — online (failure reason)
  [ALIVE] (86/425) http://torrent.fedoraproject.org:6969/announce 121ms — online (failure reason)
  [ALIVE] (87/425) http://tracker.nyaa.vc:6969/announce 293ms — valid announce response
  [ALIVE] (88/425) http://tracker.dm258.cn:7070/announce 511ms — online (failure reason)
  [ALIVE] (89/425) http://tracker.privateseedbox.xyz:2710/announce 290ms — valid announce response
  [ALIVE] (90/425) http://tracker.opentorrent.top:6969/announce 346ms — valid announce response
  [ALIVE] (91/425) http://tracker.novaopcj.eu.org:6969/announce 258ms — valid announce response
  [ALIVE] (92/425) http://tracker.qu.ax:6969/announce 259ms — valid announce response
  [ALIVE] (93/425) http://tracker.trancetraffic.com:80/announce 104ms — online (failure reason)
  [ALIVE] (94/425) http://tracker.gigatorrents.ws:2710/announce 645ms — online (failure reason)
  [ALIVE] (95/425) http://tracker.k.vu:6969/announce 540ms — valid announce response
  [ALIVE] (96/425) http://tracker.renfei.net:8080/announce 191ms — valid announce response
  [ALIVE] (97/425) http://tracker.linkomanija.org:2710/announce 762ms — online (failure reason)
  [ALIVE] (98/425) http://tracker.internetwarriors.net:1337/announce 776ms — valid announce response
  [ALIVE] (99/425) http://tracker.opentrackr.org:1337/announce 410ms — valid announce response
  [ALIVE] (100/425) http://tracker.pussytorrents.org:3000/announce 517ms — online (failure reason)
  [ALIVE] (101/425) http://tracker.xfapi.top:6868/announce 474ms — online (failure reason)
  [ALIVE] (102/425) http://tracker.xfapi.top:9999/announce 470ms — online (failure reason)
  [ALIVE] (103/425) http://tracker.xfapi.top:7070/announce 474ms — online (failure reason)
  [ALIVE] (104/425) http://tracker2.dler.org:80/announce 294ms — valid announce response
  [ALIVE] (105/425) http://tracker2.dler.com:80/announce 303ms — valid announce response
  [ALIVE] (106/425) http://www.arabp2p.net:2052/f5a1e35785c9f3885fd54f34b6e262b8/announce 41ms — online (failure reason)
  [ALIVE] (107/425) https://004430.xyz:443/announce 156ms — valid announce response
  [ALIVE] (108/425) http://tracker1.itzmx.com:8080/announce 287ms — valid announce response
  [ALIVE] (109/425) http://tracker.zhuqiy.dgj055.icu:80/announce 343ms — valid announce response
  [ALIVE] (110/425) http://tracker3.dler.org:2710/announce 515ms — valid announce response
  [ALIVE] (111/425) http://tracker.zhuqiy.com:80/announce 351ms — valid announce response
  [ALIVE] (112/425) https://3.tracker.eu.org:443/announce 37ms — valid announce response
  [ALIVE] (113/425) http://tracker.waaa.moe:6969/announce 543ms — valid announce response
  [ALIVE] (114/425) https://1.tracker.eu.org:443/announce 51ms — valid announce response
  [ALIVE] (115/425) https://2.tracker.eu.org:443/announce 41ms — valid announce response
  [ALIVE] (116/425) https://4.tracker.eu.org:443/announce 40ms — valid announce response
  [ALIVE] (117/425) https://5.tracker.eu.org:443/announce 67ms — valid announce response
  [ALIVE] (118/425) https://t.213891.xyz:443/announce 119ms — valid announce response
  [ALIVE] (119/425) https://bt.beatrice-raws.org:443/announce 303ms — online (failure reason)
  [ALIVE] (120/425) https://337hhh.xyz:443/announce 450ms — valid announce response
  [ALIVE] (121/425) https://open.ftorrent.com:443/announce 112ms — valid announce response
  [ALIVE] (122/425) https://retracker.x2k.ru:443/announce 326ms — valid announce response
  [ALIVE] (123/425) http://tracker.openzim.org:80/announce 1372ms — online (failure reason)
  [ALIVE] (124/425) https://retracker2.x2k.ru:443/announce 276ms — valid announce response
  [ALIVE] (125/425) https://t.btcland.xyz:443/announce 438ms — valid announce response
  [ALIVE] (126/425) https://tr.nyacat.pw:443/announce 245ms — valid announce response
  [ALIVE] (127/425) https://tr2.trkb.ru:443/announce 265ms — valid announce response
  [ALIVE] (128/425) https://torrent.ubuntu.com:443/announce 533ms — online (failure reason)
  [ALIVE] (129/425) https://tr-rh-zhuqiy.dgj055.icu:443/announce 512ms — valid announce response
  [ALIVE] (130/425) https://tracker.7471.top:443/announce 265ms — valid announce response
  [ALIVE] (131/425) https://tracker.anibt.net:443/announce 245ms — online (failure reason)
  [ALIVE] (132/425) https://tracker.keepfrds.com:443/announce 162ms — online (failure reason)
  [ALIVE] (133/425) https://tr-zhuqiy-2.dgj055.icu:443/announce 511ms — valid announce response
  [ALIVE] (134/425) https://tr.torland.ga:443/announce 493ms — valid announce response
  [ALIVE] (135/425) https://tracker.foreverpirates.co:443/announce 281ms — valid announce response
  [ALIVE] (136/425) https://tracker-zhuqiy.dgj055.icu:443/announce 504ms — valid announce response
  [ALIVE] (137/425) https://tracker.monikadesign.uk:443/announce 297ms — online (failure reason)
  [ALIVE] (138/425) udp://109.201.134.183:80/announce 129ms — valid connect + announce
  [ALIVE] (139/425) https://tracker.midnightprogrammer.net:443/announce 441ms — valid announce response
  [ALIVE] (140/425) https://tr-zhuqiy-1.dgj055.icu:443/announce 502ms — valid announce response
  [ALIVE] (142/425) udp://149.106.106.25:443/announce 35ms — valid connect + announce
  [ALIVE] (143/425) https://tracker.zhuqiy.com:443/announce 391ms — valid announce response
  [ALIVE] (144/425) https://tracker.qingwapt.org:443/announce 261ms — online (failure reason)
  [ALIVE] (145/425) udp://132.226.6.145:6969/announce 111ms — valid connect + announce
  [ALIVE] (146/425) udp://118.196.100.63:6969/announce 202ms — valid connect + announce
  [ALIVE] (147/425) udp://120.78.150.131:6969/announce 202ms — valid connect + announce
  [ALIVE] (148/425) udp://164.152.110.70:6969/announce 55ms — valid connect + announce
  [ALIVE] (149/425) https://tracker.nekomi.cn:443/announce 150ms — valid announce response
  [ALIVE] (150/425) udp://173.201.36.219:6969/announce 50ms — valid connect + announce
  [ALIVE] (151/425) udp://180.131.145.175:6969/announce 32ms — valid connect + announce
  [ALIVE] (152/425) udp://135.125.198.235:1984/announce 150ms — valid connect + announce
  [ALIVE] (153/425) udp://160.30.240.158:1337/announce 142ms — valid connect + announce
  [ALIVE] (154/425) udp://151.242.104.187:80/announce 147ms — valid connect + announce
  [ALIVE] (155/425) http://t.overflow.biz:6969/announce 514ms — valid announce response
  [ALIVE] (156/425) udp://192.3.130.53:1337/announce 53ms — valid connect + announce
  [ALIVE] (157/425) udp://15.235.207.99:8081/announce 178ms — valid connect + announce
  [ALIVE] (158/425) udp://177.188.141.75:6969/announce 152ms — valid connect + announce
  [ALIVE] (159/425) udp://193.148.251.93:6969/announce 65ms — valid connect + announce
  [ALIVE] (160/425) udp://192.99.100.68:6969/announce 69ms — valid connect + announce
  [ALIVE] (161/425) udp://185.121.168.96:6969/announce 150ms — valid connect + announce
  [ALIVE] (162/425) udp://209.141.59.25:6969/announce 12ms — valid connect + announce
  [ALIVE] (163/425) udp://185.216.179.62:25/announce 136ms — valid connect + announce
  [ALIVE] (164/425) udp://185.121.168.96:1337/announce 178ms — valid connect + announce
  [ALIVE] (165/425) udp://193.187.90.12:6969/announce 152ms — valid connect + announce
  [ALIVE] (166/425) udp://193.34.92.5:80/announce 169ms — valid connect + announce
  [ALIVE] (167/425) udp://211.75.205.187:6969/announce 146ms — valid connect + announce
  [ALIVE] (168/425) udp://211.75.205.187:80/announce 141ms — valid connect + announce
  [ALIVE] (169/425) udp://211.75.205.188:6969/announce 141ms — valid connect + announce
  [ALIVE] (170/425) udp://211.75.205.188:80/announce 140ms — valid connect + announce
  [ALIVE] (171/425) udp://211.75.205.189:6969/announce 140ms — valid connect + announce
  [ALIVE] (172/425) udp://23.157.120.14:6969/announce 53ms — valid connect + announce
  [ALIVE] (173/425) udp://211.75.205.189:80/announce 141ms — valid connect + announce
  [ALIVE] (174/425) udp://211.75.210.221:6969/announce 147ms — valid connect + announce
  [ALIVE] (175/425) udp://23.175.184.30:23333/announce 48ms — valid connect + announce
  [ALIVE] (176/425) udp://221.153.216.56:8081/announce 134ms — valid connect + announce
  [ALIVE] (177/425) udp://211.75.210.221:80/announce 141ms — valid connect + announce
  [ALIVE] (178/425) udp://23.154.104.2:23333/announce 129ms — valid connect + announce
  [ALIVE] (179/425) udp://212.42.38.197:6969/announce 169ms — valid connect + announce
  [ALIVE] (180/425) udp://34.66.57.33:1337/announce 49ms — valid connect + announce
  [ALIVE] (181/425) udp://34.66.57.33:80/announce 50ms — valid connect + announce
  [ALIVE] (182/425) udp://31.38.161.123:6969/announce 138ms — valid connect + announce
  [ALIVE] (183/425) udp://31.56.179.159:6969/announce 153ms — valid connect + announce
  [ALIVE] (184/425) udp://43.154.112.29:17272/announce 153ms — valid connect + announce
  [ALIVE] (185/425) udp://31.59.141.120:6969/announce 183ms — valid connect + announce
  [ALIVE] (186/425) udp://43.250.54.126:6969/announce 135ms — valid connect + announce
  [ALIVE] (187/425) udp://51.81.222.188:6969/announce 30ms — valid connect + announce
  [ALIVE] (188/425) udp://45.137.199.107:6969/announce 146ms — valid connect + announce
  [ALIVE] (189/425) udp://45.38.170.167:6969/announce 165ms — valid connect + announce
  [ALIVE] (190/425) udp://51.222.82.36:6969/announce 69ms — valid connect + announce
  [ALIVE] (191/425) udp://47.76.201.250:6969/announce 152ms — valid connect + announce
  [ALIVE] (192/425) udp://51.15.41.46:6969/announce 130ms — valid connect + announce
  [ALIVE] (193/425) udp://52.211.139.85:27022/announce 118ms — valid connect + announce
  [ALIVE] (195/425) udp://74.119.149.136:6969/announce 49ms — valid connect + announce
  [ALIVE] (196/425) udp://60.249.37.20:6969/announce 147ms — valid connect + announce
  [ALIVE] (197/425) udp://60.249.37.20:80/announce 141ms — valid connect + announce
  [ALIVE] (198/425) udp://65.109.28.17:6969/announce 166ms — valid connect + announce
  [ALIVE] (199/425) udp://60.172.236.18:6969/announce 205ms — valid connect + announce
  [ALIVE] (200/425) udp://65.109.28.33:6969/announce 162ms — valid connect + announce
  [ALIVE] (201/425) udp://85.17.55.112:6969/announce 129ms — valid connect + announce
  [ALIVE] (202/425) udp://89.234.156.205:451/announce 134ms — valid connect + announce
  [ALIVE] (203/425) udp://83.102.180.21:80/announce 172ms — valid connect + announce
  [ALIVE] (204/425) udp://91.177.126.188:6969/announce 135ms — valid connect + announce
  [ALIVE] (205/425) udp://91.216.110.53:451/announce 136ms — valid connect + announce
  [ALIVE] (206/425) udp://93.158.213.92:1337/announce 134ms — valid connect + announce
  [ALIVE] (207/425) udp://93.158.213.92:6969/announce 134ms — valid connect + announce
  [ALIVE] (208/425) udp://91.211.5.21:6969/announce 182ms — valid connect + announce
  [ALIVE] (209/425) udp://94.23.207.177:6969/announce 143ms — valid connect + announce
  [ALIVE] (210/425) udp://95.217.80.20:6969/announce 166ms — valid connect + announce
  [ALIVE] (211/425) udp://95.217.80.22:6969/announce 169ms — valid connect + announce
  [ALIVE] (212/425) udp://chihaya.toss.li:9696/announce 54ms — valid connect + announce
  [ALIVE] (213/425) udp://bttracker.debian.org:6969/announce 164ms — valid connect + announce
  [ALIVE] (214/425) udp://evan.im:6969/announce 49ms — valid connect + announce
  [ALIVE] (215/425) udp://ipv4announce.sktorrent.eu:6969/announce 143ms — valid connect + announce
  [ALIVE] (216/425) udp://anime-tracker.aruku.kro.kr:8081/announce 135ms — valid connect + announce
  [ALIVE] (217/425) udp://kolankoalastree.newtrackon.co.nz:1337/announce 143ms — valid connect + announce
  [ALIVE] (218/425) udp://admin.52ywp.com:6969/announce 239ms — valid connect + announce
  [ALIVE] (219/425) udp://leet-tracker.moe:23861/announce 50ms — valid connect + announce
  [ALIVE] (220/425) udp://leet-tracker.moe:38151/announce 51ms — valid connect + announce
  [ALIVE] (221/425) udp://leet-tracker.moe:1337/announce 52ms — valid connect + announce
  [ALIVE] (222/425) udp://open.ftorrent.com:443/announce 36ms — valid connect + announce
  [ALIVE] (224/425) udp://135.125.236.64:6969/announce 148ms — valid connect (announce not confirmed)
  [ALIVE] (225/425) udp://mail.segso.net:6969/announce 167ms — valid connect + announce
  [ALIVE] (226/425) udp://martin-gebhardt.eu:25/announce 137ms — valid connect + announce
  [ALIVE] (227/425) udp://open.demonii.com:1337/announce 160ms — valid connect + announce
  [ALIVE] (228/425) udp://open.stealth.si:80/announce 151ms — valid connect + announce
  [ALIVE] (229/425) udp://opentrackr.org:1337/announce 131ms — valid connect + announce
  [ALIVE] (230/425) udp://ns575949.ip-51-222-82.net:6969/announce 69ms — valid connect + announce
  [ALIVE] (231/425) udp://qg.lorzl.gq:2710/announce 50ms — valid connect + announce
  [ALIVE] (232/425) udp://opentracker.lain.moscow:6969/announce 151ms — valid connect + announce
  [ALIVE] (233/425) udp://seedpeer.net:6969/announce 34ms — valid connect + announce
  [ALIVE] (234/425) udp://retracker01-msk-virt.corbina.net:80/announce 179ms — valid connect + announce
  [ALIVE] (235/425) udp://peerfect.org:6969/announce 169ms — valid connect + announce
  [ALIVE] (236/425) udp://secure.pow7.com:6969/announce 23ms — valid connect + announce
  [ALIVE] (237/425) udp://santost12.xyz:6969/announce 149ms — valid connect + announce
  [ALIVE] (238/425) udp://t1.pow7.com:6969/announce 23ms — valid connect + announce
  [ALIVE] (239/425) udp://t.overflow.biz:6969/announce 153ms — valid connect + announce
  [ALIVE] (240/425) udp://tr4ck3r.duckdns.org:6969/announce 69ms — valid connect + announce
  [ALIVE] (241/425) udp://tracker-udp.anirena.com:80/announce 141ms — valid connect + announce
  [ALIVE] (242/425) udp://tracker.004430.xyz:1337/announce 48ms — valid connect + announce
  [ALIVE] (243/425) udp://torrents.artixlinux.org:6969/announce 195ms — valid connect + announce
  [ALIVE] (244/425) udp://tracker-udp.gbitt.info:80/announce 131ms — valid connect + announce
  [ALIVE] (245/425) udp://torrent.tracker.durukanbal.com:6969/announce 132ms — valid connect + announce
  [ALIVE] (246/425) udp://tracker.auctor.tv:6969/announce 142ms — valid connect + announce
  [ALIVE] (247/425) udp://tracker.bittor.pw:1337/announce 51ms — valid connect + announce
  [ALIVE] (248/425) udp://tracker.btzoo.eu:80/announce 50ms — valid connect + announce
  [ALIVE] (249/425) udp://tracker.cn.nyaa.net:6969/announce 157ms — valid connect + announce
  [ALIVE] (250/425) udp://tracker.aruku.ovh:8081/announce 176ms — valid connect + announce
  [ALIVE] (251/425) udp://tracker.ddunlimited.net:6969/announce 154ms — valid connect + announce
  [ALIVE] (252/425) udp://tracker.dler.com:6969/announce 141ms — valid connect + announce
  [ALIVE] (253/425) udp://tracker.dler.org:6969/announce 147ms — valid connect + announce
  [ALIVE] (254/425) udp://tracker.cyberia.is:6969/announce 161ms — valid connect + announce
  [ALIVE] (257/425) udp://tracker.ducks.party:1984/announce 146ms — valid connect + announce
  [ALIVE] (258/425) udp://tracker.fatkhoala.org:13790/announce 51ms — valid connect + announce
  [ALIVE] (259/425) udp://tracker.fatkhoala.org:13710/announce 53ms — valid connect + announce
  [ALIVE] (260/425) udp://tracker.farted.net:6969/announce 160ms — valid connect + announce
  [ALIVE] (261/425) udp://tracker.gmi.gd:6969/announce 12ms — valid connect + announce
  [ALIVE] (263/425) udp://tracker.ilibr.org:6969/announce 169ms — valid connect + announce
  [ALIVE] (264/425) udp://tracker.ilibr.org:80/announce 173ms — valid connect + announce
  [ALIVE] (266/425) udp://tracker.kali.org:6969/announce 55ms — valid connect + announce
  [ALIVE] (268/425) udp://tracker.k.vu:6969/announce 161ms — valid connect + announce
  [ALIVE] (271/425) udp://tracker.novaopcj.eu.org:6969/announce 131ms — valid connect + announce
  [ALIVE] (272/425) udp://tracker.nyaa.vc:6969/announce 146ms — valid connect + announce
  [ALIVE] (273/425) udp://tracker.nyaa.net:6969/announce 183ms — valid connect + announce
  [ALIVE] (274/425) udp://tracker.opentrackr.org:1337/announce 131ms — valid connect + announce
  [ALIVE] (275/425) udp://tracker.opentrackr.com:6969/announce 166ms — valid connect + announce
  [ALIVE] (276/425) udp://tracker.leechers-paradise.org:6969/announce 141ms — valid connect + announce
  [ALIVE] (277/425) udp://tracker.opentrackr.com:1337/announce 169ms — valid connect + announce
  [ALIVE] (278/425) udp://tracker.orsvarn.com:6969/announce 146ms — valid connect + announce
  [ALIVE] (279/425) udp://tracker.sbsub.com:2710/announce 50ms — valid connect + announce
  [ALIVE] (281/425) udp://tracker.qu.ax:6969/announce 130ms — valid connect + announce
  [ALIVE] (282/425) udp://t2.pow7.com:6969/announce 23ms — valid connect (announce not confirmed)
  [ALIVE] (283/425) udp://tracker.sigterm.xyz:6969/announce 145ms — valid connect + announce
  [ALIVE] (284/425) udp://tracker.peerfect.org:6969/announce 170ms — valid connect + announce
  [ALIVE] (285/425) udp://tracker.segso.net:6969/announce 167ms — valid connect + announce
  [ALIVE] (287/425) udp://tracker.skynetcloud.site:6969/announce 129ms — valid connect + announce
  [ALIVE] (290/425) udp://tracker.wildkat.net:6969/announce 51ms — valid connect + announce
  [ALIVE] (291/425) udp://tracker.teambelgium.net:6969/announce 132ms — valid connect + announce
  [ALIVE] (293/425) udp://tracker.playground.ru:6969/announce 169ms — valid connect + announce
  [ALIVE] (294/425) udp://tracker2.dler.com:80/announce 146ms — valid connect + announce
  [ALIVE] (295/425) udp://tracker2.dler.org:80/announce 141ms — valid connect + announce
  [ALIVE] (296/425) udp://tracker.tryhackx.org:6969/announce 151ms — valid connect + announce
  [ALIVE] (297/425) udp://yuptracker-eu.gaijinent.com:27022/announce 123ms — valid connect + announce
  [ALIVE] (298/425) udp://v2.iperson.xyz:6969/announce 207ms — valid connect + announce
  [ALIVE] (299/425) udp://tracker.willy.pro:6969/announce 289ms — valid connect + announce
  [DEAD]  (300/425) wss://qot.abiir.top/announce — SSLEOFError: [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)
  [ALIVE] (302/425) udp://tracker.uw0.xyz:6969/announce 136ms — valid connect + announce
  [ALIVE] (303/425) wss://tracker.magnetoo.io/announce 50ms — TLS reachable
  [ALIVE] (304/425) wss://spacetradersapi-chatbox.herokuapp.com/announce 178ms — TLS reachable
  [ALIVE] (305/425) udp://zer0day.ch:1337/announce 130ms — valid connect + announce
  [ALIVE] (306/425) wss://tracker.openwebtorrent.com/announce 75ms — TLS reachable
  [ALIVE] (307/425) udp://www.torrent.eu.org:451/announce 141ms — valid connect + announce
  [ALIVE] (308/425) udp://yuptracker.gaijinent.com:27022/announce 143ms — valid connect + announce
  [ALIVE] (310/425) udp://yuptracker-us.gaijinent.com:27022/announce 49ms — valid connect + announce
  [ALIVE] (313/425) udp://exodus.desync.com:6969/announce 23ms — valid connect + announce
  [ALIVE] (315/425) wss://tracker.files.fm:7073/announce 340ms — TLS reachable
  [ALIVE] (316/425) wss://tracker.webtorrent.dev/announce 434ms — TLS reachable
  [ALIVE] (322/425) udp://tracker.filemail.com:6969/announce 170ms — valid connect (announce not confirmed)
  [ALIVE] (324/425) udp://yuptracker-sa.gaijinent.com:27022/announce 186ms — valid connect + announce
  [ALIVE] (325/425) wss://tracker.openwebtorrent.com:443/announce 142ms — TLS reachable
  [ALIVE] (338/425) udp://tracker.torrent.eu.org:451/announce 138ms — valid connect + announce
  [ALIVE] (340/425) http://107.189.2.131:1337/announce 284ms — valid announce response
  [DEAD]  (350/425) udp://ch3oh.ru:6969/announce — no connect response
  [DEAD]  (375/425) http://51.79.71.167:80/announce — URLError: <urlopen error timed out>
  [SKIP]   (400/425) http://qimlze77z7w32lx2ntnwkuqslrzlsqy7774v3urueuarafyqik5a.b32.i2p:80/a — I2P network required
  [DEAD]  (425/425) http://138.186.10.167:1337/announce — URLError: <urlopen error timed out>

[INFO] First pass done in 33.4s
[INFO] Second pass: re-testing top 100 alive trackers...
[INFO] Second pass done, refined 92 trackers
[INFO] Same-IP dedup removed 169 slower tracker(s)

===== Test Summary =====
  Total tested:   425
  Alive (raw):    131
  Alive (final):  59 (top 59 by composite score)
  Score-capped:   72
  Unsafe filtered:5
  Low-speed:      0 (>5s excluded)
  Same-IP dedup:  169 (kept faster)
  Dead final:     352
  Time:           41.6s
=== 协议分布统计 ===
  HTTP  : 114 个
  HTTPS : 30 个
  UDP   : 150 个
  WSS   : 6 个
  WS    : 0 个
  总计: 300 个（存活）
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
[OK]   docs/ngosang_best.txt
[OK]   docs/ngosang_i2p.txt
[OK]   docs/ngosang_ygg.txt
[OK]   docs/ngosang_all_ip.txt
[OK]   docs/ngosang_ygg_ip.txt
[OK] Plain-text files synced to docs/.

============================================================
 Round 1 - 2026-09-30 12:00:24
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
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_ygg.txt: 1 trackers
  [PASS] Local tracker: trackers_ngosang_all_ip.txt: 55 trackers
  [PASS] Local tracker: trackers_ngosang_ygg_ip.txt: 4 trackers
  [PASS] Local tracker: trackers_merged.txt: 425 trackers
  [PASS] Local tracker: trackers_alive.txt: 59 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 59 trackers
  [PASS] Plain text: /merged.txt: 425 trackers
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
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_ygg.txt: 1 trackers
  [PASS] Plain text: /ngosang_all_ip.txt: 55 trackers
  [PASS] Plain text: /ngosang_ygg_ip.txt: 4 trackers
  [PASS] Alive count check: 59 in [0, 59]
  [PASS] Merged dedup check: 425 unique
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
  [PASS] Consistency: trackers_ngosang_best.txt vs ngosang_best.txt: identical
  [PASS] Consistency: trackers_ngosang_i2p.txt vs ngosang_i2p.txt: identical
  [PASS] Consistency: trackers_ngosang_ygg.txt vs ngosang_ygg.txt: identical
  [PASS] Consistency: trackers_ngosang_all_ip.txt vs ngosang_all_ip.txt: identical
  [PASS] Consistency: trackers_ngosang_ygg_ip.txt vs ngosang_ygg_ip.txt: identical
  [PASS] URL format check: all 425 valid
------------------------------------------------------------
  Result: 64 passed, 0 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 1 rounds completed
   Total PASS: 64
   Total WARN: 0
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################

============================================================
 Round 1 - 2026-09-30 12:00:31
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
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_ygg.txt: 1 trackers
  [PASS] Local tracker: trackers_ngosang_all_ip.txt: 55 trackers
  [PASS] Local tracker: trackers_ngosang_ygg_ip.txt: 4 trackers
  [PASS] Local tracker: trackers_merged.txt: 425 trackers
  [PASS] Local tracker: trackers_alive.txt: 59 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 59 trackers
  [PASS] Plain text: /merged.txt: 425 trackers
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
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_ygg.txt: 1 trackers
  [PASS] Plain text: /ngosang_all_ip.txt: 55 trackers
  [PASS] Plain text: /ngosang_ygg_ip.txt: 4 trackers
  [PASS] Alive count check: 59 in [0, 59]
  [PASS] Merged dedup check: 425 unique
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
  [PASS] Consistency: trackers_ngosang_best.txt vs ngosang_best.txt: identical
  [PASS] Consistency: trackers_ngosang_i2p.txt vs ngosang_i2p.txt: identical
  [PASS] Consistency: trackers_ngosang_ygg.txt vs ngosang_ygg.txt: identical
  [PASS] Consistency: trackers_ngosang_all_ip.txt vs ngosang_all_ip.txt: identical
  [PASS] Consistency: trackers_ngosang_ygg_ip.txt vs ngosang_ygg_ip.txt: identical
  [PASS] URL format check: all 425 valid
  [PASS] Raw: alive (Raw): HTTP 200, 59 trackers
  [PASS] Raw: merged (Raw): HTTP 200, 425 trackers
  [PASS] Pages: /alive.txt: HTTP 200, 59 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 425 trackers
  [PASS] Pages short: /s/alive: HTTP 200, redirect OK
  [WARN] Pages short: /s/cf: unreachable: HTTP Error 404: Not Found
------------------------------------------------------------
  Result: 69 passed, 1 warnings, 0 failed
============================================================

============================================================
 Round 2 - 2026-09-30 12:00:37
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
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_ygg.txt: 1 trackers
  [PASS] Local tracker: trackers_ngosang_all_ip.txt: 55 trackers
  [PASS] Local tracker: trackers_ngosang_ygg_ip.txt: 4 trackers
  [PASS] Local tracker: trackers_merged.txt: 425 trackers
  [PASS] Local tracker: trackers_alive.txt: 59 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 59 trackers
  [PASS] Plain text: /merged.txt: 425 trackers
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
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_ygg.txt: 1 trackers
  [PASS] Plain text: /ngosang_all_ip.txt: 55 trackers
  [PASS] Plain text: /ngosang_ygg_ip.txt: 4 trackers
  [PASS] Alive count check: 59 in [0, 59]
  [PASS] Merged dedup check: 425 unique
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
  [PASS] Consistency: trackers_ngosang_best.txt vs ngosang_best.txt: identical
  [PASS] Consistency: trackers_ngosang_i2p.txt vs ngosang_i2p.txt: identical
  [PASS] Consistency: trackers_ngosang_ygg.txt vs ngosang_ygg.txt: identical
  [PASS] Consistency: trackers_ngosang_all_ip.txt vs ngosang_all_ip.txt: identical
  [PASS] Consistency: trackers_ngosang_ygg_ip.txt vs ngosang_ygg_ip.txt: identical
  [PASS] URL format check: all 425 valid
  [PASS] Raw: alive (Raw): HTTP 200, 59 trackers
  [PASS] Raw: merged (Raw): HTTP 200, 425 trackers
  [PASS] Pages: /alive.txt: HTTP 200, 59 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 425 trackers
  [PASS] Pages short: /s/alive: HTTP 200, redirect OK
  [WARN] Pages short: /s/cf: unreachable: HTTP Error 404: Not Found
------------------------------------------------------------
  Result: 69 passed, 1 warnings, 0 failed
============================================================

============================================================
 Round 3 - 2026-09-30 12:00:43
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
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_ygg.txt: 1 trackers
  [PASS] Local tracker: trackers_ngosang_all_ip.txt: 55 trackers
  [PASS] Local tracker: trackers_ngosang_ygg_ip.txt: 4 trackers
  [PASS] Local tracker: trackers_merged.txt: 425 trackers
  [PASS] Local tracker: trackers_alive.txt: 59 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 59 trackers
  [PASS] Plain text: /merged.txt: 425 trackers
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
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_ygg.txt: 1 trackers
  [PASS] Plain text: /ngosang_all_ip.txt: 55 trackers
  [PASS] Plain text: /ngosang_ygg_ip.txt: 4 trackers
  [PASS] Alive count check: 59 in [0, 59]
  [PASS] Merged dedup check: 425 unique
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
  [PASS] Consistency: trackers_ngosang_best.txt vs ngosang_best.txt: identical
  [PASS] Consistency: trackers_ngosang_i2p.txt vs ngosang_i2p.txt: identical
  [PASS] Consistency: trackers_ngosang_ygg.txt vs ngosang_ygg.txt: identical
  [PASS] Consistency: trackers_ngosang_all_ip.txt vs ngosang_all_ip.txt: identical
  [PASS] Consistency: trackers_ngosang_ygg_ip.txt vs ngosang_ygg_ip.txt: identical
  [PASS] URL format check: all 425 valid
  [PASS] Raw: alive (Raw): HTTP 200, 59 trackers
  [PASS] Raw: merged (Raw): HTTP 200, 425 trackers
  [PASS] Pages: /alive.txt: HTTP 200, 59 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 425 trackers
  [PASS] Pages short: /s/alive: HTTP 200, redirect OK
  [WARN] Pages short: /s/cf: unreachable: HTTP Error 404: Not Found
------------------------------------------------------------
  Result: 69 passed, 1 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 3 rounds completed
   Total PASS: 207
   Total WARN: 3
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################
=== End of diagnostics (Wed Sep 30 12:00:43 UTC 2026) ===
