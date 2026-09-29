=== Diagnostics Tue Sep 29 11:59:30 UTC 2026 ===
Python: Python 3.12.14
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://cf.trackerslist.com/best.txt
  HTTP 200, total 0.095729s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best_ip.txt
  HTTP 200, total 0.116176s
>>> https://tracker.adysec.com/trackers_best.txt
  HTTP 200, total 0.351544s
>>> https://tracker.adysec.com/trackers_best_http.txt
  HTTP 200, total 0.269191s
>>> https://tracker.adysec.com/trackers_best_https.txt
  HTTP 200, total 0.191211s
>>> https://tracker.adysec.com/trackers_best_udp.txt
  HTTP 200, total 0.233431s
>>> https://tracker.adysec.com/trackers_best_wss.txt
  HTTP 200, total 0.199513s
>>> https://raw.githubusercontent.com/DeSireFire/animeTrackerList/refs/heads/master/ATline_best.txt
  HTTP 200, total 0.166759s
>>> https://raw.githubusercontent.com/DeSireFire/animeTrackerList/refs/heads/master/ATline_best_ip.txt
  HTTP 200, total 0.128058s
[INFO] Repo: Pmwiu/Tracker-List, Max: 59

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
  [ALIVE] (1/349) http://207.241.226.111:6969/announce 41ms — valid announce response
  [ALIVE] (2/349) http://207.241.231.226:6969/announce 44ms — valid announce response
  [ALIVE] (3/349) http://216.144.239.90:6969/announce 136ms — valid announce response
  [ALIVE] (4/349) http://140.235.237.23:6969/announce 147ms — valid announce response
  [ALIVE] (5/349) http://004430.xyz:80/announce 94ms — valid announce response
  [ALIVE] (6/349) http://bt.edwardk.info:2710/announce 154ms — online (failure reason)
  [ALIVE] (7/349) http://bt.edwardk.info:12891/announce 155ms — online (failure reason)
  [ALIVE] (8/349) http://185.126.65.92:6969/announce 267ms — valid announce response
  [ALIVE] (9/349) http://43.250.54.126:6969/announce 270ms — valid announce response
  [ALIVE] (10/349) http://93.158.213.92:1337/announce 271ms — valid announce response
  [ALIVE] (11/349) http://31.38.161.123:6969/announce 278ms — valid announce response
  [ALIVE] (12/349) http://bittorrent.kali.org:80/announce 131ms — online (failure reason)
  [ALIVE] (13/349) http://94.23.207.177:6969/announce 279ms — valid announce response
  [ALIVE] (14/349) http://211.75.210.221:80/announce 282ms — valid announce response
  [ALIVE] (15/349) http://211.75.205.189:80/announce 282ms — valid announce response
  [ALIVE] (16/349) http://211.75.205.187:6969/announce 283ms — valid announce response
  [ALIVE] (17/349) http://211.75.205.189:6969/announce 283ms — valid announce response
  [ALIVE] (18/349) http://211.75.205.187:80/announce 283ms — valid announce response
  [ALIVE] (19/349) http://211.75.205.188:80/announce 283ms — valid announce response
  [ALIVE] (20/349) http://60.249.37.20:6969/announce 282ms — valid announce response
  [ALIVE] (21/349) http://60.249.37.20:80/announce 282ms — valid announce response
  [ALIVE] (22/349) http://211.75.210.221:6969/announce 283ms — valid announce response
  [ALIVE] (23/349) http://37.120.182.83:2710/announce 283ms — valid announce response
  [ALIVE] (24/349) http://37.120.182.83:80/announce 283ms — valid announce response
  [ALIVE] (25/349) http://bt.edwardk.info:4040/announce 152ms — online (failure reason)
  [ALIVE] (26/349) http://135.125.198.235:2710/announce 293ms — valid announce response
  [ALIVE] (27/349) http://211.75.205.188:6969/announce 299ms — valid announce response
  [ALIVE] (28/349) http://135.125.198.235:80/announce 305ms — valid announce response
  [ALIVE] (29/349) http://bt.edwardk.info:63124/announce 160ms — online (failure reason)
  [ALIVE] (30/349) http://177.188.141.75:6969/announce 310ms — valid announce response
  [ALIVE] (31/349) http://bt.edwardk.info:676/announce 163ms — online (failure reason)
  [ALIVE] (32/349) http://announce.sktorrent.eu:6969/announce 306ms — valid announce response
  [ALIVE] (33/349) http://bt.edwardk.info:6767/announce 169ms — online (failure reason)
  [ALIVE] (34/349) http://bt.edwardk.info:6969/announce 182ms — online (failure reason)
  [ALIVE] (35/349) http://bt1.archive.org:6969/announce 54ms — valid announce response
  [ALIVE] (36/349) http://1337.abcvg.info:80/announce 251ms — valid announce response
  [ALIVE] (37/349) http://bt2.edwardk.info:2710/announce 175ms — online (failure reason)
  [ALIVE] (38/349) http://bt2.edwardk.info:4040/announce 176ms — online (failure reason)
  [ALIVE] (39/349) http://bt2.edwardk.info:6969/announce 184ms — online (failure reason)
  [ALIVE] (40/349) http://bt2.archive.org:6969/announce 201ms — valid announce response
  [ALIVE] (41/349) http://t-backup.213891.xyz:80/announce 146ms — valid announce response
  [ALIVE] (42/349) http://ipv4announce.sktorrent.eu:6969/announce 332ms — valid announce response
  [ALIVE] (43/349) http://ehtracker.org:80/2496841/announce 269ms — online (failure reason)
  [ALIVE] (44/349) http://ehtracker.org:80/1226599/1080494xo5eXcwFOBq/announce 269ms — online (failure reason)
  [ALIVE] (45/349) http://ehtracker.org:80/2541477/announce 273ms — online (failure reason)
  [ALIVE] (46/349) http://nyaa.tracker.wf:7777/announce 353ms — valid announce response
  [ALIVE] (47/349) http://ehtracker.org:80/1/announce 315ms — online (failure reason)
  [ALIVE] (48/349) http://ehtracker.org:80/1104308/announce 316ms — online (failure reason)
  [ALIVE] (49/349) http://ehtracker.org:80/2566145/1159106xUfsJkT9Btg/announce 320ms — online (failure reason)
  [ALIVE] (50/349) http://ehtracker.org:80/1113709/announce 321ms — online (failure reason)
  [ALIVE] (51/349) http://torrent.fedoraproject.org:6969/announce 118ms — online (failure reason)
  [ALIVE] (52/349) http://retracker.x2k.ru:80/announce 419ms — valid announce response
  [ALIVE] (53/349) http://bt.zlofenix.org:81/announce 364ms — online (failure reason)
  [ALIVE] (54/349) http://bt.beatrice-raws.org:80/announce 669ms — online (failure reason)
  [ALIVE] (55/349) http://open.demonii.si:80/announce 317ms — valid announce response
  [ALIVE] (56/349) http://sukebei.tracker.wf:8888/announce 379ms — valid announce response
  [ALIVE] (57/349) http://opentracker.acgnx.se:80/announce 479ms — online (failure reason)
  [ALIVE] (58/349) http://tracker.004430.xyz:1337/announce 137ms — valid announce response
  [ALIVE] (59/349) http://tr.nyacat.pw:80/announce 363ms — valid announce response
  [ALIVE] (60/349) http://tracker.gcvchp.com:2710/announce 76ms — online (failure reason)
  [ALIVE] (61/349) http://tracker-udp.anirena.com:80/announce 272ms — online (failure reason)
  [ALIVE] (62/349) http://bttracker.debian.org:6969/announce 319ms — online (failure reason)
  [ALIVE] (63/349) http://t.nyaatracker.com:80/announce 315ms — valid announce response
  [ALIVE] (64/349) http://tracker-zhuqiy.dgj055.icu:80/announce 321ms — valid announce response
  [ALIVE] (65/349) http://t.overflow.biz:6969/announce 392ms — valid announce response
  [ALIVE] (66/349) http://tracker.coppersurfer.site:2710/announce 294ms — valid announce response
  [ALIVE] (67/349) http://tracker.ddunlimited.net:6969/announce 353ms — online (failure reason)
  [ALIVE] (68/349) http://opentrackr.org:1337/announce 555ms — valid announce response
  [ALIVE] (69/349) http://tracker.dler.org:6969/announce 334ms — valid announce response
  [ALIVE] (70/349) http://tracker.breizh.pm:6969/announce 270ms — valid announce response
  [ALIVE] (71/349) http://open.touki.ru:80/announce 568ms — online (failure reason)
  [ALIVE] (72/349) http://tracker.ali213.net:8000/announce 473ms — online (failure reason)
  [ALIVE] (73/349) http://tracker.ali213.net:8080/announce 474ms — online (failure reason)
  [ALIVE] (74/349) http://tracker.acgnx.se:80/announce 505ms — online (failure reason)
  [ALIVE] (75/349) http://tracker.kali.org:6969/announce 257ms — online (failure reason)
  [ALIVE] (76/349) http://tracker.auctor.tv:6969/announce 261ms — valid announce response
  [ALIVE] (77/349) http://tracker.fansub.id:80/announce 367ms — valid announce response
  [ALIVE] (78/349) http://retracker01-msk-virt.corbina.net:80/announce 645ms — valid announce response
  [ALIVE] (79/349) http://tracker.dler.com:6969/announce 331ms — valid announce response
  [ALIVE] (80/349) http://tracker.nyaa.vc:6969/announce 302ms — valid announce response
  [ALIVE] (81/349) http://bt02.nnm-club.info:2710/announce 347ms — online (failure reason)
  [ALIVE] (82/349) http://tracker.minglong.org:8080/announce 284ms — online (failure reason)
  [ALIVE] (83/349) http://torrent.ubuntu.com:6969/announce 780ms — online (failure reason)
  [ALIVE] (84/349) http://tracker.qu.ax:6969/announce 259ms — valid announce response
  [ALIVE] (85/349) http://tracker.privateseedbox.xyz:2710/announce 293ms — valid announce response
  [ALIVE] (86/349) http://tracker.gigatorrents.ws:2710/announce 475ms — online (failure reason)
  [ALIVE] (87/349) http://tracker.trancetraffic.com:80/announce 183ms — online (failure reason)
  [ALIVE] (88/349) http://tracker.pussytorrents.org:3000/announce 311ms — online (failure reason)
  [ALIVE] (89/349) http://opentracker.xyz:80/announce 911ms — valid announce response
  [ALIVE] (90/349) http://tracker.mywaifu.best:6969/announce 310ms — valid announce response
  [ALIVE] (91/349) http://tracker.waaa.moe:6969/announce 64ms — valid announce response
  [ALIVE] (92/349) http://www.arabp2p.net:2052/f5a1e35785c9f3885fd54f34b6e262b8/announce 27ms — online (failure reason)
  [ALIVE] (93/349) http://tracker.opentorrent.top:6969/announce 380ms — valid announce response
  [ALIVE] (94/349) http://tracker.torrents.observer:80/announce 288ms — valid announce response
  [ALIVE] (95/349) http://tracker.novaopcj.eu.org:6969/announce 267ms — valid announce response
  [ALIVE] (96/349) http://tracker.opentrackr.org:1337/announce 423ms — valid announce response
  [ALIVE] (97/349) https://004430.xyz:443/announce 208ms — valid announce response
  [ALIVE] (98/349) http://tracker.k.vu:6969/announce 579ms — valid announce response
  [ALIVE] (99/349) http://tracker.zhuqiy.dgj055.icu:80/announce 325ms — valid announce response
  [ALIVE] (100/349) http://tracker2.dler.org:80/announce 301ms — valid announce response
  [ALIVE] (101/349) http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 1707ms — valid announce response
  [ALIVE] (102/349) https://1.tracker.eu.org:443/announce 44ms — valid announce response
  [ALIVE] (103/349) http://tracker.renfei.net:8080/announce 198ms — valid announce response
  [ALIVE] (104/349) http://tracker.linkomanija.org:2710/announce 516ms — online (failure reason)
  [ALIVE] (105/349) http://tracker.zhuqiy.com:80/announce 359ms — valid announce response
  [ALIVE] (106/349) https://1337.abcvg.info:443/announce 310ms — valid announce response
  [ALIVE] (107/349) https://open.ftorrent.com:443/announce 113ms — valid announce response
  [ALIVE] (108/349) https://2.tracker.eu.org:443/announce 51ms — valid announce response
  [ALIVE] (109/349) https://3.tracker.eu.org:443/announce 44ms — valid announce response
  [ALIVE] (110/349) https://t.213891.xyz:443/announce 154ms — valid announce response
  [ALIVE] (111/349) https://bt.beatrice-raws.org:443/announce 315ms — online (failure reason)
  [ALIVE] (112/349) http://tracker3.dler.org:2710/announce 337ms — valid announce response
  [ALIVE] (113/349) http://tracker2.dler.com:80/announce 315ms — valid announce response
  [ALIVE] (114/349) http://tracker1.itzmx.com:8080/announce 306ms — valid announce response
  [ALIVE] (115/349) https://retracker.x2k.ru:443/announce 319ms — online (failure reason)
  [ALIVE] (116/349) https://5.tracker.eu.org:443/announce 56ms — valid announce response
  [ALIVE] (117/349) https://4.tracker.eu.org:443/announce 50ms — valid announce response
  [ALIVE] (118/349) http://tracker.xfapi.top:7070/announce 614ms — online (failure reason)
  [ALIVE] (119/349) http://tracker.xfapi.top:9999/announce 623ms — online (failure reason)
  [ALIVE] (120/349) http://tracker.xfapi.top:6868/announce 624ms — online (failure reason)
  [ALIVE] (121/349) http://tracker.dhitechnical.com:6969/announce 1202ms — valid announce response
  [ALIVE] (122/349) https://tr.nyacat.pw:443/announce 245ms — valid announce response
  [ALIVE] (123/349) https://337hhh.xyz:443/announce 447ms — valid announce response
  [ALIVE] (124/349) https://tracker.anibt.net:443/announce 235ms — online (failure reason)
  [ALIVE] (125/349) https://retracker2.x2k.ru:443/announce 343ms — valid announce response
  [ALIVE] (126/349) https://tracker.7471.top:443/announce 265ms — valid announce response
  [ALIVE] (127/349) udp://132.226.6.145:6969/announce 110ms — valid connect + announce
  [ALIVE] (128/349) https://tracker.keepfrds.com:443/announce 273ms — online (failure reason)
  [ALIVE] (129/349) https://tracker.foreverpirates.co:443/announce 288ms — valid announce response
  [ALIVE] (130/349) https://tr-rh-zhuqiy.dgj055.icu:443/announce 482ms — valid announce response
  [ALIVE] (131/349) https://torrent.ubuntu.com:443/announce 526ms — online (failure reason)
  [ALIVE] (132/349) https://t.btcland.xyz:443/announce 444ms — valid announce response
  [ALIVE] (133/349) https://tr2.trkb.ru:443/announce 277ms — valid announce response
  [ALIVE] (134/349) udp://149.106.106.25:443/announce 39ms — valid connect + announce
  [ALIVE] (135/349) udp://109.201.134.183:80/announce 142ms — valid connect + announce
  [ALIVE] (136/349) http://tracker.openzim.org:80/announce 871ms — online (failure reason)
  [ALIVE] (137/349) https://tracker.monikadesign.uk:443/announce 313ms — online (failure reason)
  [ALIVE] (138/349) https://tracker-zhuqiy.dgj055.icu:443/announce 474ms — valid announce response
  [ALIVE] (139/349) https://tracker.qingwapt.org:443/announce 266ms — online (failure reason)
  [ALIVE] (140/349) udp://135.125.198.235:1984/announce 147ms — valid connect + announce
  [ALIVE] (141/349) udp://180.131.145.175:6969/announce 41ms — valid connect + announce
  [ALIVE] (142/349) udp://173.201.36.219:6969/announce 52ms — valid connect + announce
  [ALIVE] (143/349) udp://164.152.110.70:6969/announce 54ms — valid connect + announce
  [ALIVE] (144/349) http://tracker.dm258.cn:7070/announce 1187ms — online (failure reason)
  [ALIVE] (145/349) https://tracker.zhuqiy.com:443/announce 384ms — valid announce response
  [ALIVE] (146/349) udp://209.141.59.25:6969/announce 14ms — valid connect + announce
  [ALIVE] (148/349) udp://192.3.130.53:1337/announce 65ms — valid connect + announce
  [ALIVE] (149/349) udp://120.78.150.131:6969/announce 216ms — valid connect + announce
  [ALIVE] (150/349) https://tr-zhuqiy-1.dgj055.icu:443/announce 488ms — valid announce response
  [ALIVE] (151/349) https://tr.torland.ga:443/announce 480ms — valid announce response
  [ALIVE] (152/349) udp://193.148.251.93:6969/announce 68ms — valid connect + announce
  [ALIVE] (153/349) udp://192.99.100.68:6969/announce 73ms — valid connect + announce
  [ALIVE] (154/349) https://tracker.midnightprogrammer.net:443/announce 447ms — valid announce response
  [ALIVE] (155/349) udp://118.196.100.63:6969/announce 238ms — valid connect + announce
  [ALIVE] (156/349) https://tracker.nekomi.cn:443/announce 106ms — valid announce response
  [ALIVE] (157/349) udp://23.157.120.14:6969/announce 27ms — valid connect + announce
  [ALIVE] (158/349) udp://185.121.168.96:1337/announce 133ms — valid connect + announce
  [ALIVE] (159/349) udp://151.242.104.187:80/announce 152ms — valid connect + announce
  [ALIVE] (160/349) https://tr-zhuqiy-2.dgj055.icu:443/announce 478ms — valid announce response
  [ALIVE] (161/349) udp://178.239.19.29:80/announce 145ms — valid connect + announce
  [ALIVE] (162/349) udp://185.216.179.62:25/announce 142ms — valid connect + announce
  [ALIVE] (163/349) udp://177.188.141.75:6969/announce 155ms — valid connect + announce
  [ALIVE] (164/349) udp://15.235.207.99:8081/announce 181ms — valid connect + announce
  [ALIVE] (165/349) udp://23.175.184.30:23333/announce 50ms — valid connect + announce
  [ALIVE] (166/349) udp://160.30.240.158:1337/announce 179ms — valid connect + announce
  [ALIVE] (167/349) udp://193.187.90.12:6969/announce 148ms — valid connect + announce
  [ALIVE] (168/349) udp://185.121.168.96:6969/announce 181ms — valid connect + announce
  [ALIVE] (169/349) udp://34.66.57.33:1337/announce 54ms — valid connect + announce
  [ALIVE] (170/349) udp://34.66.57.33:80/announce 55ms — valid connect + announce
  [ALIVE] (171/349) udp://211.75.205.187:6969/announce 152ms — valid connect + announce
  [ALIVE] (172/349) udp://211.75.205.188:6969/announce 148ms — valid connect + announce
  [ALIVE] (173/349) udp://211.75.205.188:80/announce 141ms — valid connect + announce
  [ALIVE] (174/349) udp://211.75.205.187:80/announce 159ms — valid connect + announce
  [ALIVE] (175/349) udp://211.75.205.189:6969/announce 141ms — valid connect + announce
  [ALIVE] (176/349) udp://193.34.92.5:80/announce 179ms — valid connect + announce
  [ALIVE] (177/349) udp://211.75.205.189:80/announce 151ms — valid connect + announce
  [ALIVE] (178/349) udp://23.154.104.2:23333/announce 137ms — valid connect + announce
  [ALIVE] (179/349) udp://211.75.210.221:6969/announce 148ms — valid connect + announce
  [ALIVE] (180/349) udp://221.153.216.56:8081/announce 140ms — valid connect + announce
  [ALIVE] (181/349) udp://211.75.210.221:80/announce 150ms — valid connect + announce
  [ALIVE] (182/349) udp://51.81.222.188:6969/announce 32ms — valid connect + announce
  [ALIVE] (183/349) udp://212.42.38.197:6969/announce 178ms — valid connect + announce
  [ALIVE] (184/349) udp://31.38.161.123:6969/announce 151ms — valid connect + announce
  [ALIVE] (185/349) udp://51.222.82.36:6969/announce 81ms — valid connect + announce
  [ALIVE] (186/349) udp://74.119.149.136:6969/announce 59ms — valid connect + announce
  [ALIVE] (187/349) udp://37.120.182.83:15480/announce 141ms — valid connect + announce
  [ALIVE] (188/349) udp://37.120.182.83:1984/announce 143ms — valid connect + announce
  [ALIVE] (189/349) udp://31.56.179.159:6969/announce 154ms — valid connect + announce
  [ALIVE] (190/349) udp://37.120.182.83:54123/announce 142ms — valid connect + announce
  [ALIVE] (191/349) udp://38.180.157.12:2715/announce 147ms — valid connect + announce
  [ALIVE] (192/349) udp://43.250.54.126:6969/announce 135ms — valid connect + announce
  [ALIVE] (193/349) udp://31.59.141.120:6969/announce 180ms — valid connect + announce
  [ALIVE] (194/349) udp://43.154.112.29:17272/announce 156ms — valid connect + announce
  [ALIVE] (195/349) udp://52.211.139.85:27022/announce 117ms — valid connect + announce
  [ALIVE] (196/349) udp://51.15.41.46:6969/announce 137ms — valid connect + announce
  [ALIVE] (197/349) udp://45.137.199.107:6969/announce 149ms — valid connect + announce
  [ALIVE] (198/349) udp://47.76.201.250:6969/announce 155ms — valid connect + announce
  [ALIVE] (199/349) udp://45.38.170.167:6969/announce 155ms — valid connect + announce
  [ALIVE] (200/349) udp://60.249.37.20:6969/announce 145ms — valid connect + announce
  [ALIVE] (201/349) udp://85.17.55.112:6969/announce 134ms — valid connect + announce
  [ALIVE] (202/349) udp://60.249.37.20:80/announce 145ms — valid connect + announce
  [ALIVE] (203/349) udp://65.109.28.33:6969/announce 157ms — valid connect + announce
  [ALIVE] (204/349) udp://65.109.28.17:6969/announce 163ms — valid connect + announce
  [ALIVE] (205/349) udp://89.234.156.205:451/announce 136ms — valid connect + announce
  [ALIVE] (206/349) udp://83.102.180.21:80/announce 183ms — valid connect + announce
  [ALIVE] (207/349) udp://91.177.126.188:6969/announce 142ms — valid connect + announce
  [ALIVE] (208/349) udp://93.158.213.92:6969/announce 130ms — valid connect + announce
  [ALIVE] (209/349) udp://93.158.213.92:1337/announce 139ms — valid connect + announce
  [ALIVE] (210/349) udp://94.23.207.177:6969/announce 142ms — valid connect + announce
  [ALIVE] (211/349) udp://90.226.147.124:6969/announce 161ms — valid connect + announce
  [ALIVE] (212/349) udp://open.ftorrent.com:443/announce 36ms — valid connect + announce
  [ALIVE] (213/349) udp://explodie.org:6969/announce 25ms — valid connect + announce
  [ALIVE] (214/349) udp://95.217.80.20:6969/announce 166ms — valid connect + announce
  [ALIVE] (215/349) udp://leet-tracker.moe:1337/announce 50ms — valid connect + announce
  [ALIVE] (216/349) udp://leet-tracker.moe:38151/announce 51ms — valid connect + announce
  [ALIVE] (217/349) udp://evan.im:6969/announce 50ms — valid connect + announce
  [ALIVE] (218/349) udp://leet-tracker.moe:23861/announce 53ms — valid connect + announce
  [ALIVE] (219/349) udp://95.217.80.22:6969/announce 163ms — valid connect + announce
  [ALIVE] (220/349) udp://91.211.5.21:6969/announce 187ms — valid connect + announce
  [ALIVE] (221/349) udp://bttracker.debian.org:6969/announce 171ms — valid connect + announce
  [ALIVE] (222/349) udp://ipv4announce.sktorrent.eu:6969/announce 145ms — valid connect + announce
  [ALIVE] (223/349) udp://chihaya.toss.li:9696/announce 51ms — valid connect + announce
  [ALIVE] (225/349) udp://seedpeer.net:6969/announce 36ms — valid connect + announce
  [ALIVE] (226/349) udp://martin-gebhardt.eu:25/announce 145ms — valid connect + announce
  [ALIVE] (227/349) udp://kolankoalastree.newtrackon.co.nz:1337/announce 191ms — valid connect + announce
  [ALIVE] (228/349) udp://open.demonii.com:1337/announce 137ms — valid connect + announce
  [ALIVE] (229/349) udp://opentrackr.org:1337/announce 130ms — valid connect + announce
  [ALIVE] (230/349) udp://mail.segso.net:6969/announce 158ms — valid connect + announce
  [ALIVE] (231/349) udp://tracker.004430.xyz:1337/announce 48ms — valid connect + announce
  [ALIVE] (232/349) udp://anime-tracker.aruku.kro.kr:8081/announce 137ms — valid connect + announce
  [ALIVE] (233/349) udp://t.overflow.biz:6969/announce 154ms — valid connect + announce
  [ALIVE] (234/349) udp://santost12.xyz:6969/announce 152ms — valid connect + announce
  [ALIVE] (235/349) udp://tr4ck3r.duckdns.org:6969/announce 74ms — valid connect + announce
  [ALIVE] (236/349) udp://retracker01-msk-virt.corbina.net:80/announce 176ms — valid connect + announce
  [ALIVE] (237/349) udp://rekcart.duckdns.org:15480/announce 144ms — valid connect + announce
  [ALIVE] (238/349) udp://peerfect.org:6969/announce 159ms — valid connect + announce
  [ALIVE] (239/349) udp://open.stealth.si:80/announce 151ms — valid connect + announce
  [ALIVE] (240/349) udp://qg.lorzl.gq:2710/announce 55ms — valid connect + announce
  [ALIVE] (241/349) udp://tracker-udp.anirena.com:80/announce 134ms — valid connect + announce
  [ALIVE] (242/349) udp://tracker.btzoo.eu:80/announce 52ms — valid connect + announce
  [ALIVE] (243/349) udp://tracker.bittor.pw:1337/announce 56ms — valid connect + announce
  [ALIVE] (244/349) udp://tracker.corpscorp.online:80/announce 58ms — valid connect + announce
  [ALIVE] (245/349) udp://tracker.auctor.tv:6969/announce 133ms — valid connect + announce
  [ALIVE] (246/349) udp://tracker-udp.gbitt.info:80/announce 140ms — valid connect + announce
  [ALIVE] (247/349) udp://tr3.ysagin.top:2715/announce 161ms — valid connect + announce
  [ALIVE] (248/349) udp://tracker.breizh.pm:6969/announce 134ms — valid connect + announce
  [ALIVE] (249/349) udp://torrents.artixlinux.org:6969/announce 185ms — valid connect + announce
  [ALIVE] (250/349) udp://opentracker.lain.moscow:6969/announce 155ms — valid connect + announce
  [ALIVE] (251/349) udp://tracker.dler.com:6969/announce 146ms — valid connect + announce
  [ALIVE] (252/349) udp://tracker.ddunlimited.net:6969/announce 154ms — valid connect + announce
  [ALIVE] (253/349) udp://tracker.gmi.gd:6969/announce 20ms — valid connect + announce
  [ALIVE] (254/349) udp://torrent.tracker.durukanbal.com:6969/announce 130ms — valid connect + announce
  [ALIVE] (255/349) udp://tracker.fatkhoala.org:13710/announce 52ms — valid connect + announce
  [ALIVE] (256/349) udp://tracker.dler.org:6969/announce 142ms — valid connect + announce
  [ALIVE] (257/349) udp://tracker.fatkhoala.org:13790/announce 62ms — valid connect + announce
  [ALIVE] (258/349) udp://tracker.kali.org:6969/announce 54ms — valid connect + announce
  [ALIVE] (259/349) udp://tracker.cn.nyaa.net:6969/announce 161ms — valid connect + announce
  [ALIVE] (260/349) udp://tracker.ducks.party:1984/announce 150ms — valid connect + announce
  [ALIVE] (261/349) udp://ns575949.ip-51-222-82.net:6969/announce 82ms — valid connect + announce
  [ALIVE] (262/349) udp://tracker.novaopcj.eu.org:6969/announce 141ms — valid connect + announce
  [ALIVE] (263/349) udp://tracker.farted.net:6969/announce 165ms — valid connect + announce
  [ALIVE] (264/349) udp://tracker.k.vu:6969/announce 171ms — valid connect + announce
  [ALIVE] (265/349) udp://tracker.cyberia.is:6969/announce 168ms — valid connect + announce
  [ALIVE] (266/349) udp://tracker.opentrackr.org:1337/announce 140ms — valid connect + announce
  [ALIVE] (267/349) udp://tracker.nyaa.vc:6969/announce 150ms — valid connect + announce
  [ALIVE] (268/349) udp://tracker.leechers-paradise.org:6969/announce 160ms — valid connect + announce
  [ALIVE] (269/349) udp://tracker.opentorrent.top:6969/announce 165ms — valid connect + announce
  [ALIVE] (270/349) udp://tracker.aruku.ovh:8081/announce 185ms — valid connect + announce
  [ALIVE] (271/349) udp://tracker.ilibr.org:6969/announce 165ms — valid connect + announce
  [ALIVE] (272/349) udp://tracker.ilibr.org:80/announce 171ms — valid connect + announce
  [ALIVE] (273/349) udp://tracker.peerfect.org:6969/announce 166ms — valid connect + announce
  [ALIVE] (274/349) udp://tracker.sbsub.com:2710/announce 56ms — valid connect + announce
  [ALIVE] (275/349) udp://tracker.opentrackr.com:6969/announce 163ms — valid connect + announce
  [ALIVE] (276/349) udp://tracker.opentrackr.com:1337/announce 164ms — valid connect + announce
  [ALIVE] (277/349) udp://tracker.nyaa.net:6969/announce 189ms — valid connect + announce
  [ALIVE] (278/349) udp://tracker.qu.ax:6969/announce 146ms — valid connect + announce
  [ALIVE] (279/349) udp://tracker.orsvarn.com:6969/announce 149ms — valid connect + announce
  [ALIVE] (280/349) udp://tracker.wildkat.net:6969/announce 56ms — valid connect + announce
  [ALIVE] (281/349) udp://tracker.sigterm.xyz:6969/announce 148ms — valid connect + announce
  [ALIVE] (282/349) udp://tracker.torrents.observer:80/announce 137ms — valid connect + announce
  [ALIVE] (283/349) udp://tracker.segso.net:6969/announce 159ms — valid connect + announce
  [ALIVE] (284/349) udp://tracker.teambelgium.net:6969/announce 132ms — valid connect + announce
  [ALIVE] (285/349) udp://tracker2.dler.com:80/announce 146ms — valid connect + announce
  [ALIVE] (286/349) udp://tracker2.dler.org:80/announce 142ms — valid connect + announce
  [ALIVE] (287/349) udp://tracker.skynetcloud.site:6969/announce 131ms — valid connect + announce
  [ALIVE] (288/349) udp://yuptracker-eu.gaijinent.com:27022/announce 119ms — valid connect + announce
  [ALIVE] (289/349) udp://tracker.tallpenguin.org:15750/announce 54ms — valid connect + announce
  [ALIVE] (290/349) udp://tracker.uw0.xyz:6969/announce 138ms — valid connect + announce
  [ALIVE] (291/349) udp://v2.iperson.xyz:6969/announce 211ms — valid connect + announce
  [ALIVE] (293/349) wss://tracker.openwebtorrent.com/announce 94ms — TLS reachable
  [ALIVE] (294/349) wss://spacetradersapi-chatbox.herokuapp.com/announce 185ms — TLS reachable
  [ALIVE] (296/349) udp://tracker.tryhackx.org:6969/announce 151ms — valid connect + announce
  [ALIVE] (297/349) udp://tracker.playground.ru:6969/announce 178ms — valid connect + announce
  [ALIVE] (298/349) udp://yuptracker.gaijinent.com:27022/announce 139ms — valid connect + announce
  [ALIVE] (299/349) udp://exodus.desync.com:6969/announce 35ms — valid connect + announce
  [ALIVE] (300/349) udp://zer0day.ch:1337/announce 140ms — valid connect + announce
  [ALIVE] (301/349) udp://tracker.willy.pro:6969/announce 300ms — valid connect + announce
  [ALIVE] (302/349) udp://yuptracker-us.gaijinent.com:27022/announce 51ms — valid connect + announce
  [ALIVE] (304/349) wss://tracker.files.fm:7073/announce 349ms — TLS reachable
  [ALIVE] (306/349) udp://tracker.torrent.eu.org:451/announce 135ms — valid connect + announce
  [ALIVE] (308/349) wss://tracker.openwebtorrent.com:443/announce 82ms — TLS reachable
  [ALIVE] (311/349) udp://www.torrent.eu.org:451/announce 138ms — valid connect + announce
  [ALIVE] (313/349) wss://tracker.webtorrent.dev/announce 429ms — TLS reachable
  [ALIVE] (320/349) wss://tracker.magnetoo.io/announce 449ms — TLS reachable
  [ALIVE] (324/349) udp://yuptracker-sa.gaijinent.com:27022/announce 190ms — valid connect + announce
  [DEAD]  (325/349) https://tracker.lilithraws.cf:443/announce — URLError: <urlopen error [Errno -2] Name or service not known>

[INFO] First pass done in 16.7s
[INFO] Second pass: re-testing top 100 alive trackers...
[INFO] Second pass done, refined 89 trackers
[INFO] Same-IP dedup removed 175 slower tracker(s)

===== Test Summary =====
  Total tested:   349
  Alive (raw):    130
  Alive (final):  59 (top 59 by composite score)
  Score-capped:   71
  Unsafe filtered:0
  Low-speed:      0 (>5s excluded)
  Same-IP dedup:  175 (kept faster)
  Dead final:     290
  Time:           24.9s
=== 协议分布统计 ===
  HTTP  : 112 个
  HTTPS : 31 个
  UDP   : 156 个
  WSS   : 6 个
  WS    : 0 个
  总计: 305 个（存活）
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
 Round 1 - 2026-09-29 11:59:58
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
=== End of diagnostics (Tue Sep 29 12:00:13 UTC 2026) ===
