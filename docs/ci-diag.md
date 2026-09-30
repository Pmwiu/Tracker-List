=== Diagnostics Wed Sep 30 10:50:24 UTC 2026 ===
Python: Python 3.12.14
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://cf.trackerslist.com/best.txt
  HTTP 200, total 0.200061s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best_ip.txt
  HTTP 200, total 0.245632s
>>> https://tracker.adysec.com/trackers_best.txt
  HTTP 200, total 0.160899s
>>> https://tracker.adysec.com/trackers_best_http.txt
  HTTP 200, total 0.085088s
>>> https://tracker.adysec.com/trackers_best_https.txt
  HTTP 200, total 0.073211s
>>> https://tracker.adysec.com/trackers_best_udp.txt
  HTTP 200, total 0.071853s
>>> https://tracker.adysec.com/trackers_best_wss.txt
  HTTP 200, total 0.073724s
>>> https://raw.githubusercontent.com/DeSireFire/animeTrackerList/refs/heads/master/ATline_best.txt
  HTTP 200, total 0.262018s
>>> https://raw.githubusercontent.com/DeSireFire/animeTrackerList/refs/heads/master/ATline_best_ip.txt
  HTTP 200, total 0.140169s
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

[OK]   merged: 364
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
  trackers_adysec_best.txt: 332
  trackers_adysec_http.txt: 131
  trackers_adysec_https.txt: 32
  trackers_adysec_udp.txt: 163
  trackers_adysec_wss.txt: 6
  trackers_anime_best.txt: 25
  trackers_anime_ip.txt: 1
  trackers_merged.txt: 364
  alive capped at 59 after test+sort
===================
[INFO] Testing 364 of 364 candidates (timeout=10s, workers=30, priority sources first)
[INFO] Max alive trackers after scoring: 59
  [ALIVE] (1/364) http://207.241.226.111:6969/announce 53ms — valid announce response
  [ALIVE] (2/364) http://207.241.231.226:6969/announce 91ms — valid announce response
  [ALIVE] (3/364) http://004430.xyz:80/announce 87ms — valid announce response
  [ALIVE] (4/364) http://216.144.239.90:6969/announce 163ms — valid announce response
  [ALIVE] (5/364) http://bt.edwardk.info:12891/announce 90ms — online (failure reason)
  [ALIVE] (6/364) http://bt.edwardk.info:2710/announce 86ms — online (failure reason)
  [ALIVE] (7/364) http://bt.edwardk.info:4040/announce 87ms — online (failure reason)
  [ALIVE] (8/364) http://43.250.54.126:6969/announce 237ms — valid announce response
  [ALIVE] (9/364) http://94.23.207.177:6969/announce 240ms — valid announce response
  [ALIVE] (10/364) http://185.126.65.92:6969/announce 251ms — valid announce response
  [ALIVE] (11/364) http://135.125.198.235:2710/announce 256ms — valid announce response
  [ALIVE] (12/364) http://bt.edwardk.info:63124/announce 90ms — online (failure reason)
  [ALIVE] (13/364) http://135.125.198.235:80/announce 261ms — valid announce response
  [ALIVE] (14/364) http://bt.edwardk.info:676/announce 86ms — online (failure reason)
  [ALIVE] (15/364) http://93.158.213.92:1337/announce 260ms — valid announce response
  [ALIVE] (16/364) http://bt.edwardk.info:6767/announce 91ms — online (failure reason)
  [ALIVE] (17/364) http://31.38.161.123:6969/announce 284ms — valid announce response
  [ALIVE] (18/364) http://211.75.205.188:80/announce 304ms — valid announce response
  [ALIVE] (19/364) http://211.75.205.188:6969/announce 304ms — valid announce response
  [ALIVE] (20/364) http://211.75.205.189:80/announce 304ms — valid announce response
  [ALIVE] (21/364) http://211.75.210.221:80/announce 304ms — valid announce response
  [ALIVE] (22/364) http://211.75.205.189:6969/announce 305ms — valid announce response
  [ALIVE] (23/364) http://211.75.205.187:80/announce 307ms — valid announce response
  [ALIVE] (24/364) http://177.188.141.75:6969/announce 310ms — valid announce response
  [ALIVE] (25/364) http://60.249.37.20:80/announce 305ms — valid announce response
  [ALIVE] (26/364) http://60.249.37.20:6969/announce 305ms — valid announce response
  [ALIVE] (27/364) http://211.75.205.187:6969/announce 314ms — valid announce response
  [ALIVE] (28/364) http://211.75.210.221:6969/announce 314ms — valid announce response
  [ALIVE] (29/364) http://announce.sktorrent.eu:6969/announce 264ms — valid announce response
  [ALIVE] (30/364) http://bt.edwardk.info:6969/announce 86ms — online (failure reason)
  [ALIVE] (31/364) http://79.111.12.213:6969/announce 326ms — online (failure reason)
  [ALIVE] (32/364) http://bt1.archive.org:6969/announce 71ms — valid announce response
  [ALIVE] (33/364) http://bittorrent.kali.org:80/announce 244ms — online (failure reason)
  [ALIVE] (34/364) http://bt2.edwardk.info:6969/announce 85ms — online (failure reason)
  [ALIVE] (35/364) http://bt2.edwardk.info:4040/announce 89ms — online (failure reason)
  [ALIVE] (36/364) http://bt2.edwardk.info:2710/announce 89ms — online (failure reason)
  [ALIVE] (37/364) http://ipv4announce.sktorrent.eu:6969/announce 237ms — valid announce response
  [ALIVE] (38/364) http://bt.beatrice-raws.org:80/announce 487ms — online (failure reason)
  [ALIVE] (39/364) http://bt2.archive.org:6969/announce 112ms — valid announce response
  [ALIVE] (40/364) http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 669ms — valid announce response
  [ALIVE] (41/364) http://open.demonii.si:80/announce 314ms — valid announce response
  [ALIVE] (42/364) http://ehtracker.org:80/2541477/announce 236ms — online (failure reason)
  [ALIVE] (43/364) http://ehtracker.org:80/2566145/1159106xUfsJkT9Btg/announce 239ms — online (failure reason)
  [ALIVE] (44/364) http://ehtracker.org:80/1113709/announce 242ms — online (failure reason)
  [ALIVE] (45/364) http://ehtracker.org:80/1226599/1080494xo5eXcwFOBq/announce 250ms — online (failure reason)
  [ALIVE] (46/364) http://ehtracker.org:80/1/announce 253ms — online (failure reason)
  [ALIVE] (47/364) http://ehtracker.org:80/1104308/announce 253ms — online (failure reason)
  [ALIVE] (48/364) http://ehtracker.org:80/2496841/announce 254ms — online (failure reason)
  [ALIVE] (49/364) http://ch3oh.ru:6969/announce 400ms — online (failure reason)
  [ALIVE] (50/364) http://bt.zlofenix.org:81/announce 621ms — online (failure reason)
  [ALIVE] (51/364) http://t-backup.213891.xyz:80/announce 109ms — valid announce response
  [ALIVE] (52/364) http://torrent.fedoraproject.org:6969/announce 100ms — online (failure reason)
  [ALIVE] (53/364) http://nyaa.tracker.wf:7777/announce 483ms — valid announce response
  [ALIVE] (54/364) http://opentracker.acgnx.se:80/announce 457ms — online (failure reason)
  [ALIVE] (55/364) http://tr.nyacat.pw:80/announce 174ms — valid announce response
  [ALIVE] (56/364) http://retracker.x2k.ru:80/announce 245ms — valid announce response
  [ALIVE] (57/364) http://tracker.004430.xyz:1337/announce 93ms — valid announce response
  [ALIVE] (58/364) http://t.nyaatracker.com:80/announce 313ms — valid announce response
  [ALIVE] (59/364) http://sukebei.tracker.wf:8888/announce 274ms — valid announce response
  [ALIVE] (60/364) http://open.touki.ru:80/announce 501ms — online (failure reason)
  [ALIVE] (61/364) http://tracker-udp.anirena.com:80/announce 233ms — online (failure reason)
  [ALIVE] (62/364) http://opentrackr.org:1337/announce 378ms — valid announce response
  [ALIVE] (63/364) http://tracker.acgnx.se:80/announce 380ms — online (failure reason)
  [ALIVE] (64/364) http://tracker.coppersurfer.site:2710/announce 267ms — valid announce response
  [ALIVE] (65/364) http://retracker01-msk-virt.corbina.net:80/announce 517ms — valid announce response
  [ALIVE] (66/364) http://torrent.ubuntu.com:6969/announce 687ms — online (failure reason)
  [ALIVE] (67/364) http://tracker.ddunlimited.net:6969/announce 348ms — online (failure reason)
  [ALIVE] (68/364) http://bt02.nnm-club.info:2710/announce 556ms — online (failure reason)
  [ALIVE] (69/364) http://bt02.nnm-club.cc:2710/announce 391ms — online (failure reason)
  [ALIVE] (70/364) http://tracker.auctor.tv:6969/announce 249ms — valid announce response
  [ALIVE] (71/364) http://opentracker.xyz:80/announce 764ms — valid announce response
  [ALIVE] (72/364) http://tracker-zhuqiy.dgj055.icu:80/announce 303ms — valid announce response
  [ALIVE] (73/364) http://tracker.gcvchp.com:2710/announce 119ms — online (failure reason)
  [ALIVE] (74/364) http://tracker.dler.org:6969/announce 349ms — valid announce response
  [ALIVE] (75/364) http://tracker.dler.com:6969/announce 350ms — valid announce response
  [ALIVE] (76/364) http://tracker.breizh.pm:6969/announce 365ms — valid announce response
  [ALIVE] (77/364) http://torrent.unix-ag.uni-kl.de:80/announce 691ms — online (failure reason)
  [ALIVE] (78/364) http://tracker.fansub.id:80/announce 337ms — valid announce response
  [ALIVE] (79/364) http://tracker.kali.org:6969/announce 99ms — online (failure reason)
  [ALIVE] (80/364) http://tracker.ali213.net:8000/announce 486ms — online (failure reason)
  [ALIVE] (81/364) http://bt.nnm-club.info:2710/announce 1264ms — online (failure reason)
  [ALIVE] (82/364) http://tracker.ali213.net:8080/announce 502ms — online (failure reason)
  [ALIVE] (83/364) http://open.tracker.cl:1337/announce 638ms — valid announce response
  [ALIVE] (84/364) http://tracker.minglong.org:8080/announce 288ms — online (failure reason)
  [ALIVE] (85/364) http://tracker.nyaa.vc:6969/announce 273ms — valid announce response
  [ALIVE] (86/364) http://tracker.dhitechnical.com:6969/announce 1171ms — valid announce response
  [ALIVE] (87/364) http://tracker.privateseedbox.xyz:2710/announce 267ms — valid announce response
  [ALIVE] (88/364) http://tracker.mywaifu.best:6969/announce 411ms — valid announce response
  [ALIVE] (89/364) http://tracker.k.vu:6969/announce 512ms — valid announce response
  [ALIVE] (90/364) http://tracker.opentorrent.top:6969/announce 431ms — valid announce response
  [ALIVE] (91/364) http://tracker.opentrackr.org:1337/announce 276ms — valid announce response
  [ALIVE] (92/364) http://tracker.qu.ax:6969/announce 234ms — valid announce response
  [ALIVE] (93/364) http://tracker.linkomanija.org:2710/announce 496ms — online (failure reason)
  [ALIVE] (94/364) http://tracker.dm258.cn:7070/announce 462ms — online (failure reason)
  [ALIVE] (95/364) http://tracker.novaopcj.eu.org:6969/announce 254ms — valid announce response
  [ALIVE] (96/364) http://tracker.renfei.net:8080/announce 106ms — valid announce response
  [ALIVE] (97/364) http://tracker.gigatorrents.ws:2710/announce 781ms — online (failure reason)
  [ALIVE] (98/364) http://tracker.trancetraffic.com:80/announce 144ms — online (failure reason)
  [ALIVE] (99/364) http://tracker.pussytorrents.org:3000/announce 312ms — online (failure reason)
  [ALIVE] (100/364) http://tracker.torrents.observer:80/announce 243ms — valid announce response
  [ALIVE] (101/364) http://t.overflow.biz:6969/announce 310ms — valid announce response
  [ALIVE] (102/364) http://tracker.waaa.moe:6969/announce 285ms — valid announce response
  [ALIVE] (103/364) http://tracker.zhuqiy.com:80/announce 326ms — valid announce response
  [ALIVE] (104/364) http://tracker.xfapi.top:7070/announce 487ms — online (failure reason)
  [ALIVE] (105/364) http://www.arabp2p.net:2052/f5a1e35785c9f3885fd54f34b6e262b8/announce 141ms — online (failure reason)
  [ALIVE] (106/364) http://tracker.xfapi.top:9999/announce 499ms — online (failure reason)
  [ALIVE] (107/364) http://tracker.zhuqiy.dgj055.icu:80/announce 310ms — valid announce response
  [ALIVE] (108/364) https://004430.xyz:443/announce 103ms — valid announce response
  [ALIVE] (109/364) http://tracker2.dler.org:80/announce 307ms — valid announce response
  [ALIVE] (110/364) http://tracker2.dler.com:80/announce 307ms — valid announce response
  [ALIVE] (111/364) http://tracker3.dler.org:2710/announce 306ms — valid announce response
  [ALIVE] (112/364) https://open.ftorrent.com:443/announce 25ms — valid announce response
  [ALIVE] (113/364) http://tracker.openzim.org:80/announce 1114ms — online (failure reason)
  [ALIVE] (114/364) http://tracker.internetwarriors.net:1337/announce 1319ms — valid announce response
  [ALIVE] (115/364) https://1.tracker.eu.org:443/announce 84ms — valid announce response
  [ALIVE] (116/364) http://tracker1.itzmx.com:8080/announce 471ms — valid announce response
  [ALIVE] (117/364) https://bt.beatrice-raws.org:443/announce 252ms — online (failure reason)
  [ALIVE] (118/364) https://3.tracker.eu.org:443/announce 91ms — valid announce response
  [ALIVE] (119/364) https://1337.abcvg.info:443/announce 333ms — valid announce response
  [ALIVE] (120/364) https://5.tracker.eu.org:443/announce 132ms — valid announce response
  [ALIVE] (121/364) https://2.tracker.eu.org:443/announce 76ms — valid announce response
  [ALIVE] (122/364) https://t.213891.xyz:443/announce 66ms — valid announce response
  [ALIVE] (123/364) https://4.tracker.eu.org:443/announce 94ms — valid announce response
  [ALIVE] (124/364) https://337hhh.xyz:443/announce 394ms — valid announce response
  [ALIVE] (125/364) https://retracker.x2k.ru:443/announce 266ms — valid announce response
  [ALIVE] (126/364) https://tr.nyacat.pw:443/announce 186ms — valid announce response
  [ALIVE] (127/364) https://retracker2.x2k.ru:443/announce 213ms — online (failure reason)
  [ALIVE] (128/364) https://tr2.trkb.ru:443/announce 216ms — online (failure reason)
  [ALIVE] (129/364) http://tracker.xfapi.top:6868/announce 1225ms — online (failure reason)
  [ALIVE] (130/364) https://t.btcland.xyz:443/announce 403ms — valid announce response
  [ALIVE] (131/364) https://tracker.7471.top:443/announce 205ms — valid announce response
  [ALIVE] (132/364) https://tracker.anibt.net:443/announce 190ms — online (failure reason)
  [ALIVE] (133/364) https://torrent.ubuntu.com:443/announce 445ms — online (failure reason)
  [ALIVE] (134/364) https://tracker.keepfrds.com:443/announce 113ms — online (failure reason)
  [ALIVE] (135/364) https://tracker.foreverpirates.co:443/announce 215ms — valid announce response
  [ALIVE] (136/364) https://tracker-zhuqiy.dgj055.icu:443/announce 457ms — valid announce response
  [ALIVE] (137/364) https://tr.torland.ga:443/announce 464ms — valid announce response
  [ALIVE] (138/364) https://tr-rh-zhuqiy.dgj055.icu:443/announce 474ms — valid announce response
  [ALIVE] (139/364) https://tracker.monikadesign.uk:443/announce 219ms — online (failure reason)
  [ALIVE] (140/364) https://tr-zhuqiy-2.dgj055.icu:443/announce 471ms — valid announce response
  [ALIVE] (141/364) udp://149.106.106.25:443/announce 7ms — valid connect + announce
  [ALIVE] (142/364) https://tr-zhuqiy-1.dgj055.icu:443/announce 475ms — valid announce response
  [ALIVE] (144/364) udp://109.201.134.183:80/announce 122ms — valid connect + announce
  [ALIVE] (145/364) https://tracker.midnightprogrammer.net:443/announce 328ms — valid announce response
  [ALIVE] (146/364) udp://164.152.110.70:6969/announce 24ms — valid connect + announce
  [ALIVE] (147/364) https://tracker.zhuqiy.com:443/announce 355ms — valid announce response
  [ALIVE] (148/364) https://tracker.qingwapt.org:443/announce 217ms — online (failure reason)
  [ALIVE] (149/364) udp://173.201.36.219:6969/announce 31ms — valid connect + announce
  [ALIVE] (150/364) udp://132.226.6.145:6969/announce 120ms — valid connect + announce
  [ALIVE] (151/364) udp://135.125.198.235:1984/announce 134ms — valid connect + announce
  [ALIVE] (152/364) udp://118.196.100.63:6969/announce 203ms — valid connect + announce
  [ALIVE] (153/364) https://tracker.nekomi.cn:443/announce 103ms — valid announce response
  [ALIVE] (154/364) udp://180.131.145.175:6969/announce 72ms — valid connect + announce
  [ALIVE] (155/364) udp://192.3.130.53:1337/announce 32ms — valid connect + announce
  [ALIVE] (156/364) udp://151.242.104.187:80/announce 148ms — valid connect + announce
  [ALIVE] (157/364) udp://120.78.150.131:6969/announce 218ms — valid connect + announce
  [ALIVE] (158/364) udp://193.148.251.93:6969/announce 39ms — valid connect + announce
  [ALIVE] (159/364) udp://178.239.19.29:80/announce 117ms — valid connect + announce
  [ALIVE] (160/364) udp://192.99.100.68:6969/announce 47ms — valid connect + announce
  [ALIVE] (161/364) udp://160.30.240.158:1337/announce 169ms — valid connect + announce
  [ALIVE] (162/364) udp://15.235.207.99:8081/announce 182ms — valid connect + announce
  [ALIVE] (163/364) udp://209.141.59.25:6969/announce 27ms — valid connect + announce
  [ALIVE] (164/364) udp://177.188.141.75:6969/announce 154ms — valid connect + announce
  [ALIVE] (165/364) udp://208.83.20.20:6969/announce 44ms — valid connect + announce
  [ALIVE] (166/364) udp://185.121.168.96:1337/announce 161ms — valid connect + announce
  [ALIVE] (167/364) udp://185.216.179.62:25/announce 129ms — valid connect + announce
  [ALIVE] (168/364) udp://185.121.168.96:6969/announce 162ms — valid connect + announce
  [ALIVE] (169/364) udp://193.187.90.12:6969/announce 143ms — valid connect + announce
  [ALIVE] (170/364) udp://193.34.92.5:80/announce 164ms — valid connect + announce
  [ALIVE] (171/364) udp://211.75.205.187:6969/announce 163ms — valid connect + announce
  [ALIVE] (172/364) udp://211.75.205.187:80/announce 153ms — valid connect + announce
  [ALIVE] (173/364) udp://211.75.205.188:6969/announce 153ms — valid connect + announce
  [ALIVE] (174/364) udp://211.75.205.188:80/announce 152ms — valid connect + announce
  [ALIVE] (175/364) udp://211.75.205.189:6969/announce 153ms — valid connect + announce
  [ALIVE] (176/364) udp://211.75.205.189:80/announce 152ms — valid connect + announce
  [ALIVE] (177/364) udp://23.175.184.30:23333/announce 34ms — valid connect + announce
  [ALIVE] (178/364) udp://211.75.210.221:6969/announce 153ms — valid connect + announce
  [ALIVE] (179/364) udp://34.66.57.33:1337/announce 33ms — valid connect + announce
  [ALIVE] (180/364) udp://211.75.210.221:80/announce 152ms — valid connect + announce
  [ALIVE] (181/364) udp://34.66.57.33:80/announce 31ms — valid connect + announce
  [ALIVE] (182/364) udp://212.42.38.197:6969/announce 158ms — valid connect + announce
  [ALIVE] (183/364) udp://221.153.216.56:8081/announce 148ms — valid connect + announce
  [ALIVE] (184/364) udp://23.154.104.2:23333/announce 125ms — valid connect + announce
  [ALIVE] (185/364) udp://31.38.161.123:6969/announce 137ms — valid connect + announce
  [ALIVE] (186/364) udp://51.222.82.36:6969/announce 44ms — valid connect + announce
  [ALIVE] (187/364) udp://31.56.179.159:6969/announce 149ms — valid connect + announce
  [ALIVE] (188/364) udp://43.250.54.126:6969/announce 123ms — valid connect + announce
  [ALIVE] (189/364) udp://51.81.222.188:6969/announce 30ms — valid connect + announce
  [ALIVE] (190/364) udp://45.137.199.107:6969/announce 127ms — valid connect + announce
  [ALIVE] (191/364) udp://31.59.141.120:6969/announce 174ms — valid connect + announce
  [ALIVE] (192/364) udp://43.154.112.29:17272/announce 160ms — valid connect + announce
  [ALIVE] (193/364) udp://45.38.170.167:6969/announce 144ms — valid connect + announce
  [ALIVE] (194/364) udp://51.15.41.46:6969/announce 116ms — valid connect + announce
  [ALIVE] (195/364) udp://47.76.201.250:6969/announce 160ms — valid connect + announce
  [ALIVE] (196/364) udp://74.119.149.136:6969/announce 40ms — valid connect + announce
  [ALIVE] (197/364) udp://52.211.139.85:27022/announce 114ms — valid connect + announce
  [ALIVE] (198/364) http://bttracker.debian.org:6969/announce 296ms — online (failure reason)
  [ALIVE] (199/364) udp://60.249.37.20:6969/announce 153ms — valid connect + announce
  [ALIVE] (200/364) udp://60.249.37.20:80/announce 153ms — valid connect + announce
  [ALIVE] (201/364) udp://65.109.28.17:6969/announce 153ms — valid connect + announce
  [ALIVE] (202/364) udp://85.17.55.112:6969/announce 118ms — valid connect + announce
  [ALIVE] (203/364) udp://65.109.28.33:6969/announce 157ms — valid connect + announce
  [ALIVE] (204/364) udp://89.234.156.205:451/announce 129ms — valid connect + announce
  [ALIVE] (205/364) udp://83.102.180.21:80/announce 165ms — valid connect + announce
  [ALIVE] (206/364) udp://91.177.126.188:6969/announce 123ms — valid connect + announce
  [ALIVE] (207/364) udp://60.172.236.18:6969/announce 240ms — valid connect + announce
  [ALIVE] (208/364) udp://93.158.213.92:1337/announce 121ms — valid connect + announce
  [ALIVE] (209/364) udp://94.23.207.177:6969/announce 122ms — valid connect + announce
  [ALIVE] (210/364) udp://93.158.213.92:6969/announce 128ms — valid connect + announce
  [ALIVE] (211/364) udp://91.216.110.53:451/announce 138ms — valid connect + announce
  [ALIVE] (212/364) http://tracker.xn--djrq4gl4hvoi.top:80/announce 3120ms — valid announce response
  [ALIVE] (213/364) udp://95.217.80.20:6969/announce 151ms — valid connect + announce
  [ALIVE] (214/364) udp://95.217.80.22:6969/announce 157ms — valid connect + announce
  [ALIVE] (215/364) udp://bttracker.debian.org:6969/announce 152ms — valid connect + announce
  [ALIVE] (216/364) udp://evan.im:6969/announce 47ms — valid connect + announce
  [ALIVE] (217/364) udp://leet-tracker.moe:1337/announce 32ms — valid connect + announce
  [ALIVE] (218/364) udp://leet-tracker.moe:23861/announce 32ms — valid connect + announce
  [ALIVE] (219/364) udp://chihaya.toss.li:9696/announce 31ms — valid connect + announce
  [ALIVE] (220/364) udp://ipv4announce.sktorrent.eu:6969/announce 122ms — valid connect + announce
  [ALIVE] (221/364) udp://leet-tracker.moe:38151/announce 31ms — valid connect + announce
  [ALIVE] (222/364) udp://ch3oh.ru:6969/announce 161ms — valid connect + announce
  [ALIVE] (223/364) udp://open.ftorrent.com:443/announce 6ms — valid connect + announce
  [ALIVE] (224/364) udp://explodie.org:6969/announce 76ms — valid connect + announce
  [DEAD]  (225/364) udp://open.stealth.si/announce — missing port
  [ALIVE] (226/364) udp://ns575949.ip-51-222-82.net:6969/announce 47ms — valid connect + announce
  [ALIVE] (227/364) udp://kolankoalastree.newtrackon.co.nz:1337/announce 172ms — valid connect + announce
  [ALIVE] (228/364) udp://martin-gebhardt.eu:25/announce 130ms — valid connect + announce
  [ALIVE] (229/364) udp://opentrackr.org:1337/announce 118ms — valid connect + announce
  [ALIVE] (230/364) udp://91.211.5.21:6969/announce 442ms — valid connect + announce
  [ALIVE] (231/364) udp://mail.segso.net:6969/announce 160ms — valid connect + announce
  [ALIVE] (232/364) udp://open.stealth.si:80/announce 141ms — valid connect + announce
  [ALIVE] (233/364) udp://open.demonii.com:1337/announce 177ms — valid connect + announce
  [ALIVE] (234/364) udp://peerfect.org:6969/announce 157ms — valid connect + announce
  [ALIVE] (235/364) udp://seedpeer.net:6969/announce 68ms — valid connect + announce
  [ALIVE] (236/364) udp://qg.lorzl.gq:2710/announce 32ms — valid connect + announce
  [ALIVE] (237/364) udp://retracker01-msk-virt.corbina.net:80/announce 170ms — valid connect + announce
  [ALIVE] (238/364) udp://santost12.xyz:6969/announce 134ms — valid connect + announce
  [ALIVE] (239/364) udp://t.overflow.biz:6969/announce 155ms — valid connect + announce
  [ALIVE] (240/364) udp://opentracker.lain.moscow:6969/announce 141ms — valid connect + announce
  [ALIVE] (241/364) udp://tr4ck3r.duckdns.org:6969/announce 47ms — valid connect + announce
  [ALIVE] (242/364) udp://tracker.004430.xyz:1337/announce 31ms — valid connect + announce
  [ALIVE] (243/364) udp://tracker-udp.anirena.com:80/announce 129ms — valid connect + announce
  [ALIVE] (244/364) udp://anime-tracker.aruku.kro.kr:8081/announce 145ms — valid connect + announce
  [ALIVE] (245/364) udp://tracker-udp.gbitt.info:80/announce 118ms — valid connect + announce
  [ALIVE] (246/364) udp://tracker.auctor.tv:6969/announce 119ms — valid connect + announce
  [ALIVE] (247/364) udp://tracker.bittor.pw:1337/announce 32ms — valid connect + announce
  [ALIVE] (248/364) udp://torrent.tracker.durukanbal.com:6969/announce 119ms — valid connect + announce
  [ALIVE] (249/364) udp://torrents.artixlinux.org:6969/announce 166ms — valid connect + announce
  [ALIVE] (250/364) udp://tracker.corpscorp.online:80/announce 31ms — valid connect + announce
  [ALIVE] (251/364) udp://tracker.btzoo.eu:80/announce 31ms — valid connect + announce
  [ALIVE] (252/364) udp://135.125.236.64:6969/announce 132ms — valid connect (announce not confirmed)
  [ALIVE] (253/364) udp://tracker.breizh.pm:6969/announce 158ms — valid connect + announce
  [ALIVE] (254/364) http://140.235.237.23:6969/announce 7312ms — valid announce response
  [ALIVE] (255/364) udp://tracker.ddunlimited.net:6969/announce 134ms — valid connect + announce
  [ALIVE] (256/364) udp://tracker.aruku.ovh:8081/announce 181ms — valid connect + announce
  [ALIVE] (257/364) udp://tracker.cn.nyaa.net:6969/announce 160ms — valid connect + announce
  [ALIVE] (258/364) udp://tracker.dler.com:6969/announce 153ms — valid connect + announce
  [ALIVE] (259/364) udp://tracker.fatkhoala.org:13790/announce 32ms — valid connect + announce
  [ALIVE] (260/364) udp://tracker.fatkhoala.org:13710/announce 34ms — valid connect + announce
  [ALIVE] (261/364) udp://tracker.dler.org:6969/announce 157ms — valid connect + announce
  [ALIVE] (262/364) udp://tracker.farted.net:6969/announce 141ms — valid connect + announce
  [ALIVE] (263/364) udp://tracker.cyberia.is:6969/announce 154ms — valid connect + announce
  [ALIVE] (264/364) udp://tracker.filemail.com:6969/announce 131ms — valid connect + announce
  [ALIVE] (265/364) udp://tracker.kali.org:6969/announce 42ms — valid connect + announce
  [ALIVE] (266/364) udp://tracker.ducks.party:1984/announce 132ms — valid connect + announce
  [ALIVE] (267/364) udp://tracker.k.vu:6969/announce 149ms — valid connect + announce
  [ALIVE] (268/364) udp://tracker.gmi.gd:6969/announce 27ms — valid connect + announce
  [ALIVE] (269/364) udp://23.157.120.14:6969/announce 79ms — valid connect (announce not confirmed)
  [ALIVE] (270/364) udp://tracker.ilibr.org:80/announce 152ms — valid connect + announce
  [ALIVE] (271/364) udp://tracker.ilibr.org:6969/announce 158ms — valid connect + announce
  [ALIVE] (272/364) udp://tracker.novaopcj.eu.org:6969/announce 115ms — valid connect + announce
  [ALIVE] (273/364) udp://tracker.nyaa.vc:6969/announce 130ms — valid connect + announce
  [ALIVE] (274/364) udp://tracker.nyaa.net:6969/announce 167ms — valid connect + announce
  [ALIVE] (275/364) udp://tracker.opentrackr.org:1337/announce 119ms — valid connect + announce
  [ALIVE] (276/364) udp://tracker.leechers-paradise.org:6969/announce 152ms — valid connect + announce
  [ALIVE] (277/364) udp://tracker.opentrackr.com:6969/announce 154ms — valid connect + announce
  [ALIVE] (278/364) udp://tracker.opentrackr.com:1337/announce 154ms — valid connect + announce
  [ALIVE] (279/364) udp://tracker.orsvarn.com:6969/announce 126ms — valid connect + announce
  [ALIVE] (280/364) udp://tracker.qu.ax:6969/announce 117ms — valid connect + announce
  [ALIVE] (281/364) udp://tracker.peerfect.org:6969/announce 157ms — valid connect + announce
  [ALIVE] (282/364) udp://tracker.tallpenguin.org:15750/announce 32ms — valid connect + announce
  [ALIVE] (283/364) udp://tracker.skynetcloud.site:6969/announce 116ms — valid connect + announce
  [ALIVE] (284/364) udp://tracker.segso.net:6969/announce 156ms — valid connect + announce
  [ALIVE] (285/364) udp://tracker.sigterm.xyz:6969/announce 134ms — valid connect + announce
  [ALIVE] (286/364) udp://tracker.teambelgium.net:6969/announce 134ms — valid connect + announce
  [ALIVE] (287/364) udp://tracker.torrents.observer:80/announce 119ms — valid connect + announce
  [ALIVE] (288/364) udp://tracker.playground.ru:6969/announce 160ms — valid connect + announce
  [ALIVE] (289/364) udp://tracker.wildkat.net:6969/announce 26ms — valid connect + announce
  [ALIVE] (290/364) udp://admin.52ywp.com:6969/announce 216ms — valid connect (announce not confirmed)
  [ALIVE] (291/364) udp://tracker2.dler.com:80/announce 157ms — valid connect + announce
  [ALIVE] (292/364) udp://tracker2.dler.org:80/announce 163ms — valid connect + announce
  [ALIVE] (293/364) udp://tracker.uw0.xyz:6969/announce 126ms — valid connect + announce
  [ALIVE] (294/364) udp://tracker.torrent.eu.org:451/announce 127ms — valid connect + announce
  [ALIVE] (295/364) udp://v2.iperson.xyz:6969/announce 213ms — valid connect + announce
  [ALIVE] (296/364) udp://tracker.willy.pro:6969/announce 287ms — valid connect + announce
  [ALIVE] (297/364) udp://yuptracker-eu.gaijinent.com:27022/announce 104ms — valid connect + announce
  [ALIVE] (298/364) udp://www.torrent.eu.org:451/announce 141ms — valid connect + announce
  [ALIVE] (300/364) udp://yuptracker.gaijinent.com:27022/announce 133ms — valid connect + announce
  [ALIVE] (301/364) udp://yuptracker-us.gaijinent.com:27022/announce 37ms — valid connect + announce
  [ALIVE] (302/364) udp://zer0day.ch:1337/announce 134ms — valid connect + announce
  [ALIVE] (303/364) wss://spacetradersapi-chatbox.herokuapp.com/announce 160ms — TLS reachable
  [ALIVE] (304/364) wss://tracker.openwebtorrent.com/announce 40ms — TLS reachable
  [ALIVE] (305/364) wss://tracker.magnetoo.io/announce 95ms — TLS reachable
  [ALIVE] (307/364) http://1337.abcvg.info:80/announce 348ms — valid announce response
  [ALIVE] (308/364) udp://yuptracker-sa.gaijinent.com:27022/announce 193ms — valid connect + announce
  [ALIVE] (310/364) wss://tracker.webtorrent.dev/announce 412ms — TLS reachable
  [ALIVE] (313/364) wss://tracker.files.fm:7073/announce 547ms — TLS reachable
  [ALIVE] (314/364) udp://exodus.desync.com:6969/announce 44ms — valid connect + announce
  [ALIVE] (320/364) wss://tracker.openwebtorrent.com:443/announce 40ms — TLS reachable
  [ALIVE] (324/364) udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 386ms — valid connect + announce
  [DEAD]  (325/364) http://tracker.electro-torrent.pl:80/announce — URLError: <urlopen error [Errno -2] Name or service not known>
  [DEAD]  (350/364) udp://secure.pow7.com:6969/announce — no connect response

[INFO] First pass done in 25.4s
[INFO] Second pass: re-testing top 100 alive trackers...
[INFO] Second pass done, refined 91 trackers
[INFO] Low-speed filtered (>5s): 1 trackers
[INFO] Same-IP dedup removed 173 slower tracker(s)

===== Test Summary =====
  Total tested:   364
  Alive (raw):    135
  Alive (final):  59 (top 59 by composite score)
  Score-capped:   76
  Unsafe filtered:0
  Low-speed:      1 (>5s excluded)
  Same-IP dedup:  173 (kept faster)
  Dead final:     305
  Time:           33.4s
=== 协议分布统计 ===
  HTTP  : 118 个
  HTTPS : 31 个
  UDP   : 154 个
  WSS   : 6 个
  WS    : 0 个
  总计: 309 个（存活）
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
 Round 1 - 2026-09-30 10:51:00
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
  [PASS] Local tracker: trackers_merged.txt: 364 trackers
  [PASS] Local tracker: trackers_alive.txt: 59 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 59 trackers
  [PASS] Plain text: /merged.txt: 364 trackers
  [PASS] Plain text: /cf_best.txt: 71 trackers
  [PASS] Plain text: /ngosang_ip.txt: 20 trackers
  [PASS] Plain text: /adysec_best.txt: 332 trackers
  [PASS] Plain text: /adysec_http.txt: 131 trackers
  [PASS] Plain text: /adysec_https.txt: 32 trackers
  [PASS] Plain text: /adysec_udp.txt: 163 trackers
  [PASS] Plain text: /adysec_wss.txt: 6 trackers
  [PASS] Plain text: /anime_best.txt: 25 trackers
  [PASS] Plain text: /anime_ip.txt: 1 trackers
  [PASS] Alive count check: 59 in [0, 59]
  [PASS] Merged dedup check: 364 unique
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
  [PASS] URL format check: all 364 valid
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

============================================================
 Round 1 - 2026-09-30 10:51:08
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
  [PASS] Local tracker: trackers_merged.txt: 364 trackers
  [PASS] Local tracker: trackers_alive.txt: 59 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 59 trackers
  [PASS] Plain text: /merged.txt: 364 trackers
  [PASS] Plain text: /cf_best.txt: 71 trackers
  [PASS] Plain text: /ngosang_ip.txt: 20 trackers
  [PASS] Plain text: /adysec_best.txt: 332 trackers
  [PASS] Plain text: /adysec_http.txt: 131 trackers
  [PASS] Plain text: /adysec_https.txt: 32 trackers
  [PASS] Plain text: /adysec_udp.txt: 163 trackers
  [PASS] Plain text: /adysec_wss.txt: 6 trackers
  [PASS] Plain text: /anime_best.txt: 25 trackers
  [PASS] Plain text: /anime_ip.txt: 1 trackers
  [PASS] Alive count check: 59 in [0, 59]
  [PASS] Merged dedup check: 364 unique
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
  [PASS] URL format check: all 364 valid
  [PASS] Raw: alive (Raw): HTTP 200, 59 trackers
  [PASS] Raw: merged (Raw): HTTP 200, 364 trackers
  [PASS] Pages: /alive.txt: HTTP 200, 59 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 364 trackers
  [PASS] Pages short: /s/alive: HTTP 200, redirect OK
  [WARN] Pages short: /s/cf: unreachable: HTTP Error 404: Not Found
------------------------------------------------------------
  Result: 48 passed, 1 warnings, 0 failed
============================================================

============================================================
 Round 2 - 2026-09-30 10:51:13
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
  [PASS] Local tracker: trackers_merged.txt: 364 trackers
  [PASS] Local tracker: trackers_alive.txt: 59 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 59 trackers
  [PASS] Plain text: /merged.txt: 364 trackers
  [PASS] Plain text: /cf_best.txt: 71 trackers
  [PASS] Plain text: /ngosang_ip.txt: 20 trackers
  [PASS] Plain text: /adysec_best.txt: 332 trackers
  [PASS] Plain text: /adysec_http.txt: 131 trackers
  [PASS] Plain text: /adysec_https.txt: 32 trackers
  [PASS] Plain text: /adysec_udp.txt: 163 trackers
  [PASS] Plain text: /adysec_wss.txt: 6 trackers
  [PASS] Plain text: /anime_best.txt: 25 trackers
  [PASS] Plain text: /anime_ip.txt: 1 trackers
  [PASS] Alive count check: 59 in [0, 59]
  [PASS] Merged dedup check: 364 unique
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
  [PASS] URL format check: all 364 valid
  [PASS] Raw: alive (Raw): HTTP 200, 59 trackers
  [PASS] Raw: merged (Raw): HTTP 200, 364 trackers
  [PASS] Pages: /alive.txt: HTTP 200, 59 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 364 trackers
  [PASS] Pages short: /s/alive: HTTP 200, redirect OK
  [WARN] Pages short: /s/cf: unreachable: HTTP Error 404: Not Found
------------------------------------------------------------
  Result: 48 passed, 1 warnings, 0 failed
============================================================

============================================================
 Round 3 - 2026-09-30 10:51:19
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
  [PASS] Local tracker: trackers_merged.txt: 364 trackers
  [PASS] Local tracker: trackers_alive.txt: 59 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 59 trackers
  [PASS] Plain text: /merged.txt: 364 trackers
  [PASS] Plain text: /cf_best.txt: 71 trackers
  [PASS] Plain text: /ngosang_ip.txt: 20 trackers
  [PASS] Plain text: /adysec_best.txt: 332 trackers
  [PASS] Plain text: /adysec_http.txt: 131 trackers
  [PASS] Plain text: /adysec_https.txt: 32 trackers
  [PASS] Plain text: /adysec_udp.txt: 163 trackers
  [PASS] Plain text: /adysec_wss.txt: 6 trackers
  [PASS] Plain text: /anime_best.txt: 25 trackers
  [PASS] Plain text: /anime_ip.txt: 1 trackers
  [PASS] Alive count check: 59 in [0, 59]
  [PASS] Merged dedup check: 364 unique
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
  [PASS] URL format check: all 364 valid
  [PASS] Raw: alive (Raw): HTTP 200, 59 trackers
  [PASS] Raw: merged (Raw): HTTP 200, 364 trackers
  [PASS] Pages: /alive.txt: HTTP 200, 59 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 364 trackers
  [PASS] Pages short: /s/alive: HTTP 200, redirect OK
  [WARN] Pages short: /s/cf: unreachable: HTTP Error 404: Not Found
------------------------------------------------------------
  Result: 48 passed, 1 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 3 rounds completed
   Total PASS: 144
   Total WARN: 3
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################
=== End of diagnostics (Wed Sep 30 10:51:19 UTC 2026) ===
