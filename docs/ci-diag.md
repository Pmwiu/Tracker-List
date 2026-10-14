=== Diagnostics Wed Oct 14 05:06:35 UTC 2026 ===
Python: Python 3.12.15
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_best.txt
  HTTP 200, total 0.068115s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_best_ip.txt
  HTTP 200, total 0.065836s
>>> https://cf.trackerslist.com/best.txt
  HTTP 200, total 0.102918s
>>> https://tracker.adysec.com/trackers_best.txt
  HTTP 200, total 0.213212s
>>> https://raw.githubusercontent.com/gonghailink/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.180268s
>>> https://raw.githubusercontent.com/panda-men/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.160230s
>>> https://raw.githubusercontent.com/gspu/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.269544s
>>> https://raw.githubusercontent.com/linux-jin/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.420486s
>>> https://raw.githubusercontent.com/AlphaCatMeow/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.171440s
>>> https://raw.githubusercontent.com/pexcn/daily/gh-pages/trackerlist/trackerlist-best.txt
  HTTP 200, total 0.112192s
>>> https://raw.githubusercontent.com/1265578519/OpenTracker/refs/heads/master/tracker.txt
  HTTP 200, total 0.188137s
>>> https://trackers.run/s/rw_ws_up_hp_hs_v4_v6.txt
  HTTP 200, total 0.621537s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_i2p.txt
  HTTP 200, total 0.342482s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_yggdrasil.txt
  HTTP 200, total 0.297376s
[INFO] public list https://cf.trackerslist.com/all.txt: 121 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all.txt: 74 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ip.txt: 52 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_udp.txt: 46 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_http.txt: 19 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_https.txt: 12 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ws.txt: 3 urls
[OK]   164 new candidates -> candidates_20261014.txt
[OK]   164 new candidates
[INFO] Repo: Pmwiu/Tracker-List, Max: 25
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/ngosang/trackerslist/master/blacklist.txt (391 URLs)
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/blacklist.txt (20 URLs)
[INFO] URL blacklist: 392 URLs (dynamic + remote sources)
[INFO] Protected hosts (防误杀): 61
[INFO] discovered candidates: 148 URLs in 1 file(s)

[INFO] trackers_ngosang_best.txt (ngosang-best)
[OK]   20 unique

[INFO] trackers_ngosang_best_ip.txt (ngosang-best-ip)
[OK]   20 unique

[INFO] trackers_cf_best.txt (cf-best)
  [INFO] Skipped 10 dynamic-blacklisted lines
[OK]   58 unique

[INFO] trackers_adysec_best.txt (adysec-best)
  [INFO] Skipped 74 dynamic-blacklisted lines
[OK]   248 unique

[INFO] trackers_gonghailink_best.txt (gonghailink-best)
  [INFO] Skipped 3 dynamic-blacklisted lines
[OK]   17 unique

[INFO] trackers_pandamen_best.txt (pandamen-best)
  [INFO] Skipped 3 dynamic-blacklisted lines
[OK]   17 unique

[INFO] trackers_gspu_best.txt (gspu-best)
  [INFO] Skipped 2 dynamic-blacklisted lines
[OK]   18 unique

[INFO] trackers_linuxjin_best.txt (linuxjin-best)
[OK]   20 unique

[INFO] trackers_alphacatmeow_best.txt (alphacatmeow-best)
  [INFO] Skipped 6 dynamic-blacklisted lines
[OK]   14 unique

[INFO] trackers_pexcn_best.txt (pexcn-best)
  [INFO] Skipped 10 dynamic-blacklisted lines
[OK]   62 unique

[INFO] trackers_opentracker.txt (opentracker)
  [INFO] Skipped 4 invalid lines
  [INFO] Skipped 8 dynamic-blacklisted lines
[OK]   23 unique

[INFO] trackers_run_ws.txt (trackersrun-ws)
  [INFO] Skipped 2 dynamic-blacklisted lines
[OK]   47 unique

[INFO] trackers_ngosang_i2p.txt (ngosang-i2p)
[OK]   17 unique

[INFO] trackers_ngosang_yggdrasil.txt (ngosang-yggdrasil)
  [INFO] Skipped 1 dynamic-blacklisted lines
[WARN] trackers_ngosang_yggdrasil.txt failed (No valid trackers found in response); using backup (1 trackers)
[OK]   1 unique

[INFO] all 合并贡献: ngosang-best=20, ngosang-best-ip=20, cf-best=27, adysec-best=31, gonghailink-best=8, pandamen-best=6, gspu-best=3, linuxjin-best=1, alphacatmeow-best=1, pexcn-best=1, opentracker=9, trackersrun-ws=20, ngosang-i2p=17, ngosang-yggdrasil=1
[INFO] all 协议分布: http=71, https=49, udp=79, wss=1, ws=0

[OK]   merged: 200
[OK]   source_counts.json (200)
[OK]   discovered_set.json (148)
[OK]   MIRRORS.txt
[OK]   /s/alive
[OK]   /s/all
[OK]   index.html
[OK]   docs/alive.txt
[OK]   docs/all.txt
[OK]   docs/reserve.txt
[OK]   docs/merged.txt
[OK]   docs/ngosang_best.txt
[OK]   docs/ngosang_best_ip.txt
[OK]   docs/cf_best.txt
[OK]   docs/adysec_best.txt
[OK]   docs/gonghailink_best.txt
[OK]   docs/pandamen_best.txt
[OK]   docs/gspu_best.txt
[OK]   docs/linuxjin_best.txt
[OK]   docs/alphacatmeow_best.txt
[OK]   docs/pexcn_best.txt
[OK]   docs/opentracker.txt
[OK]   docs/run_ws.txt
[OK]   docs/ngosang_i2p.txt
[OK]   docs/ngosang_yggdrasil.txt
[OK]   docs/udp.txt
[OK]   docs/http.txt
[OK]   docs/https.txt
[OK]   docs/wss.txt
[OK]   docs/ws.txt

===== Summary =====
  trackers_ngosang_best.txt: 20
  trackers_ngosang_best_ip.txt: 20
  trackers_cf_best.txt: 58
  trackers_adysec_best.txt: 248
  trackers_gonghailink_best.txt: 17
  trackers_pandamen_best.txt: 17
  trackers_gspu_best.txt: 18
  trackers_linuxjin_best.txt: 20
  trackers_alphacatmeow_best.txt: 14
  trackers_pexcn_best.txt: 62
  trackers_opentracker.txt: 23
  trackers_run_ws.txt: 47
  trackers_ngosang_i2p.txt: 17
  trackers_ngosang_yggdrasil.txt: 1
  trackers_merged.txt: 200
  alive capped at 25 after test+sort
===================
[INFO] reserve: +107 discovered candidates for liveness test (rotation, cap 120)
[INFO] Testing 307 candidates (all-pool=200, timeout=10s, workers=30)
[INFO] Max alive trackers after scoring: 25
  [ALIVE] (1/307) http://207.241.226.111:6969/announce 49ms — announce with peers:1
  [ALIVE] (2/307) http://207.241.231.226:6969/announce 50ms — announce with peers:1
  [ALIVE] (3/307) http://004430.xyz:80/announce 83ms — announce with peers:1
  [ALIVE] (5/307) http://140.235.237.23:6969/announce 164ms — announce with peers:1
  [ALIVE] (7/307) http://211.75.205.187:6969/announce 262ms — announce with peers:1
  [ALIVE] (8/307) http://211.75.205.188:6969/announce 261ms — announce with peers:1
  [ALIVE] (9/307) http://211.75.205.188:80/announce 262ms — announce with peers:1
  [ALIVE] (10/307) http://211.75.205.187:80/announce 262ms — announce with peers:1
  [ALIVE] (11/307) http://211.75.210.221:6969/announce 262ms — announce with peers:1
  [ALIVE] (12/307) http://211.75.210.221:80/announce 262ms — announce with peers:1
  [ALIVE] (13/307) http://185.126.65.92:6969/announce 280ms — announce without peers
  [ALIVE] (14/307) http://43.250.54.126:6969/announce 276ms — announce with peers:1
  [ALIVE] (15/307) http://93.158.213.92:1337/announce 277ms — announce with peers:1
  [ALIVE] (16/307) http://1337.abcvg.info:80/announce 243ms — announce with peers:1
  [ALIVE] (17/307) http://135.125.198.235:2710/announce 299ms — announce without peers
  [ALIVE] (18/307) http://135.125.198.235:80/announce 301ms — announce without peers
  [ALIVE] (19/307) http://94.23.207.177:6969/announce 295ms — announce with peers:1
  [ALIVE] (20/307) http://138.186.10.167:1337/announce 317ms — announce with peers:1
  [ALIVE] (21/307) http://107.189.2.131:1337/announce 325ms — announce with peers:1
  [ALIVE] (22/307) http://31.38.161.123:6969/announce 328ms — announce with peers:1
  [ALIVE] (23/307) http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 323ms — announce with peers:1
  [DEAD]  (25/307) http://ehtracker.org:80/2566145/1159106xUfsJkT9Btg/announce — restricted (failure reason)
  [ALIVE] (31/307) http://ipv4announce.sktorrent.eu:6969/announce 296ms — announce with peers:1
  [ALIVE] (33/307) http://tracker.dhitechnical.com:6969/announce 194ms — announce with peers:1
  [ALIVE] (34/307) http://announce.sktorrent.eu:6969/announce 749ms — announce with peers:1
  [ALIVE] (35/307) http://retracker.x2k.ru:80/announce 488ms — announce with peers:1
  [ALIVE] (36/307) http://tracker.dler.org:6969/announce 264ms — announce with peers:1
  [ALIVE] (37/307) http://tracker.auctor.tv:6969/announce 288ms — announce with peers:1
  [ALIVE] (38/307) http://open.demonii.si:80/announce 347ms — announce without peers
  [ALIVE] (39/307) http://tracker.dler.com:6969/announce 269ms — announce with peers:1
  [ALIVE] (40/307) http://tracker.nyaa.vc:6969/announce 276ms — announce without peers
  [ALIVE] (41/307) http://tracker.mywaifu.best:6969/announce 324ms — announce without peers
  [ALIVE] (43/307) http://tracker.qu.ax:6969/announce 287ms — announce with peers:1
  [ALIVE] (44/307) http://retracker01-msk-virt.corbina.net:80/announce 638ms — announce with peers:1
  [ALIVE] (45/307) https://004430.xyz:443/announce 93ms — announce with peers:1
  [ALIVE] (46/307) http://tracker2.dler.org:80/announce 292ms — announce with peers:1
  [ALIVE] (48/307) http://tracker.zhuqiy.dgj055.icu:80/announce 349ms — announce without peers
  [ALIVE] (49/307) http://tracker.renfei.net:8080/announce 143ms — announce with peers:1
  [DEAD]  (50/307) https://anishkverma1-commits.github.io:443 — invalid bencoded response
  [ALIVE] (51/307) http://open.tracker.cl:1337/announce 821ms — announce with peers:1
  [ALIVE] (53/307) https://5.tracker.eu.org:443/announce 34ms — announce without peers
  [ALIVE] (54/307) https://1.tracker.eu.org:443/announce 46ms — announce without peers
  [ALIVE] (55/307) https://3.tracker.eu.org:443/announce 43ms — announce without peers
  [ALIVE] (56/307) http://opentracker.xyz:80/announce 838ms — announce with peers:1
  [ALIVE] (57/307) http://tracker.opentrackr.org:1337/announce 663ms — announce with peers:1
  [ALIVE] (58/307) https://4.tracker.eu.org:443/announce 42ms — announce without peers
  [ALIVE] (59/307) https://337hhh.xyz:443/announce 447ms — announce without peers
  [DEAD]  (75/307) http://www.wareztorrent.com:80/announce — RemoteDisconnected: Remote end closed connection without response
  [ALIVE] (89/307) https://2.tracker.eu.org:443/announce 44ms — announce without peers
  [ALIVE] (92/307) https://t.213891.xyz:443/announce 31ms — announce without peers
  [SKIP]   (100/307) http://tracker.insulaocculta.i2p:80/a — I2P network required
  [ALIVE] (101/307) https://tr.nyacat.pw:443/announce 173ms — announce without peers
  [ALIVE] (102/307) udp://132.226.6.145:6969/announce 98ms — valid connect + announce (v4)
  [ALIVE] (104/307) https://tracker.foreverpirates.co:443/announce 219ms — announce without peers
  [ALIVE] (105/307) https://tracker.7471.top:443/announce 187ms — announce without peers
  [ALIVE] (106/307) udp://209.141.59.25:6969/announce 48ms — valid connect + announce (v4)
  [ALIVE] (107/307) udp://109.201.134.183:80/announce 139ms — valid connect + announce (v4)
  [ALIVE] (108/307) https://tracker.nekomi.cn:443/announce 94ms — announce with peers:1
  [ALIVE] (109/307) udp://34.66.57.33:80/announce 53ms — valid connect + announce (v4)
  [ALIVE] (110/307) udp://135.125.198.235:1984/announce 151ms — valid connect + announce (v4)
  [ALIVE] (111/307) https://tracker.midnightprogrammer.net:443/announce 306ms — announce without peers
  [ALIVE] (112/307) udp://151.242.104.187:80/announce 148ms — valid connect + announce (v4)
  [ALIVE] (113/307) udp://185.121.168.96:1337/announce 135ms — valid connect + announce (v4)
  [ALIVE] (114/307) udp://51.81.222.188:6969/announce 9ms — valid connect + announce (v4)
  [ALIVE] (115/307) https://tracker.zhuqiy.com:443/announce 112ms — announce with peers:1
  [ALIVE] (116/307) udp://211.75.205.188:80/announce 131ms — valid connect + announce (v4)
  [ALIVE] (118/307) udp://193.34.92.5:80/announce 177ms — valid connect + announce (v4)
  [ALIVE] (119/307) udp://43.154.112.29:17272/announce 139ms — valid connect + announce (v4)
  [ALIVE] (120/307) udp://43.250.54.126:6969/announce 144ms — valid connect + announce (v4)
  [ALIVE] (121/307) udp://31.38.161.123:6969/announce 168ms — valid connect + announce (v4)
  [ALIVE] (122/307) udp://31.56.179.159:6969/announce 174ms — valid connect + announce (v4)
  [ALIVE] (123/307) udp://45.137.199.107:6969/announce 137ms — valid connect + announce (v4)
  [ALIVE] (124/307) udp://51.15.41.46:6969/announce 146ms — valid connect + announce (v4)
  [ALIVE] (125/307) udp://65.109.28.33:6969/announce 170ms — valid connect + announce (v4)
  [ALIVE] (126/307) udp://65.109.28.17:6969/announce 174ms — valid connect + announce (v4)
  [ALIVE] (127/307) udp://93.158.213.92:1337/announce 139ms — valid connect + announce (v4)
  [ALIVE] (128/307) udp://89.234.156.205:451/announce 156ms — valid connect + announce (v4)
  [ALIVE] (129/307) udp://93.158.213.92:6969/announce 145ms — valid connect + announce (v4)
  [ALIVE] (130/307) udp://83.102.180.21:80/announce 189ms — valid connect + announce (v4)
  [ALIVE] (132/307) udp://95.217.80.20:6969/announce 171ms — valid connect + announce (v4)
  [ALIVE] (135/307) udp://95.217.80.22:6969/announce 171ms — valid connect + announce (v4)
  [ALIVE] (136/307) udp://evan.im:6969/announce 65ms — valid connect + announce (v4)
  [ALIVE] (137/307) udp://explodie.org:6969/announce 30ms — valid connect + announce (v4)
  [ALIVE] (138/307) udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 194ms — valid connect + announce (v4)
  [ALIVE] (142/307) udp://open.ftorrent.com:443/announce 27ms — valid connect + announce (v4)
  [ALIVE] (143/307) udp://ipv4announce.sktorrent.eu:6969/announce 141ms — valid connect + announce (v4)
  [ALIVE] (145/307) udp://open.demonii.com:1337/announce 135ms — valid connect + announce (v4)
  [ALIVE] (146/307) udp://mail.segso.net:6969/announce 169ms — valid connect + announce (v4)
  [ALIVE] (147/307) udp://kolankoalastree.newtrackon.co.nz:1337/announce 148ms — valid connect + announce (v4)
  [ALIVE] (148/307) udp://martin-gebhardt.eu:25/announce 147ms — valid connect + announce (v4)
  [ALIVE] (149/307) udp://tr.btube3.com:2010/announce 69ms — valid connect + announce (v4)
  [ALIVE] (150/307) udp://retracker01-msk-virt.corbina.net:80/announce 188ms — valid connect + announce (v4)
  [ALIVE] (151/307) udp://tracker.004430.xyz:1337/announce 30ms — valid connect + announce (v4)
  [ALIVE] (152/307) udp://open.stealth.si:80/announce 157ms — valid connect + announce (v4)
  [ALIVE] (153/307) udp://tracker.bittor.pw:1337/announce 49ms — valid connect + announce (v4)
  [ALIVE] (154/307) udp://tr4ck3r.duckdns.org:6969/announce 65ms — valid connect + announce (v4)
  [ALIVE] (155/307) udp://tracker-udp.gbitt.info:80/announce 151ms — valid connect + announce (v4)
  [ALIVE] (156/307) udp://tracker.corpscorp.online:80/announce 49ms — valid connect + announce (v4)
  [ALIVE] (157/307) udp://tracker.cn.nyaa.net:6969/announce 139ms — valid connect + announce (v4)
  [ALIVE] (158/307) udp://tracker.dler.org:6969/announce 131ms — valid connect + announce (v4)
  [ALIVE] (159/307) udp://tracker.ducks.party:1984/announce 150ms — valid connect + announce (v4)
  [ALIVE] (160/307) udp://tracker.gmi.gd:6969/announce 39ms — valid connect + announce (v4)
  [ALIVE] (161/307) udp://tracker.nyaa.vc:6969/announce 143ms — valid connect + announce (v4)
  [ALIVE] (162/307) udp://tracker.opentrackr.org:1337/announce 153ms — valid connect + announce (v4)
  [ALIVE] (163/307) udp://tracker.farted.net:6969/announce 165ms — valid connect + announce (v4)
  [ALIVE] (164/307) udp://tracker.qu.ax:6969/announce 144ms — valid connect + announce (v4)
  [ALIVE] (165/307) udp://tracker.peerfect.org:6969/announce 169ms — valid connect + announce (v4)
  [ALIVE] (166/307) udp://tracker.skynetcloud.site:6969/announce 146ms — valid connect + announce (v4)
  [ALIVE] (168/307) udp://tracker.tryhackx.org:6969/announce 159ms — valid connect + announce (v4)
  [ALIVE] (170/307) udp://t.overflow.biz:6969/announce 181ms — valid connect + announce (v4)
  [ALIVE] (172/307) udp://tracker2.dler.org:80/announce 131ms — valid connect + announce (v4)
  [ALIVE] (174/307) udp://tracker.torrent.eu.org:451/announce 168ms — valid connect + announce (v4)
  [ALIVE] (175/307) udp://archive.torrentonline.cc:42069/announce 190ms — valid connect + announce (v4)
  [ALIVE] (177/307) udp://seedpeer.net:6969/announce 12ms — valid connect + announce (v4)
  [ALIVE] (178/307) udp://bt-tracker.de:6969/announce 154ms — valid connect + announce (v4)
  [ALIVE] (179/307) udp://ns575949.ip-51-222-82.net:6969/announce 65ms — valid connect + announce (v4)
  [ALIVE] (180/307) http://216.144.239.90:6969/announce 5837ms — announce with peers:1
  [ALIVE] (181/307) udp://52.58.128.163:6969/announce 142ms — valid connect + announce (v4)
  [ALIVE] (182/307) udp://tr3.ysagin.top:2715/announce 166ms — valid connect + announce (v4)
  [ALIVE] (183/307) udp://tracker.ddunlimited.net:6969/announce 158ms — valid connect + announce (v4)
  [ALIVE] (184/307) udp://tracker.nyaa.net:6969/announce 180ms — valid connect + announce (v4)
  [ALIVE] (185/307) udp://tracker.okade.pro:1337/announce 158ms — valid connect + announce (v4)
  [ALIVE] (186/307) udp://tracker.k.vu:6969/announce 170ms — valid connect + announce (v4)
  [ALIVE] (187/307) udp://tracker.opentrackr.com:6969/announce 167ms — valid connect + announce (v4)
  [ALIVE] (188/307) udp://tracker.playground.ru:6969/announce 180ms — valid connect + announce (v4)
  [ALIVE] (189/307) udp://tracker.torrents.observer:80/announce 149ms — valid connect + announce (v4)
  [ALIVE] (191/307) udp://tracker.willy.pro:6969/announce 230ms — valid connect + announce (v4)
  [ALIVE] (192/307) udp://v2.iperson.xyz:6969/announce 183ms — valid connect + announce (v4)
  [ALIVE] (198/307) udp://149.106.106.25:443/announce 28ms — valid connect + announce (v4)
  [ALIVE] (199/307) http://tracker.waaa.moe:6969/announce 7832ms — announce with peers:1
  [DEAD]  (200/307) wss://tracker.webtorrent.dev:443 — SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: IP address mismatch, certificate is not valid for '49.13.90.136'. (_ssl.c:1010)
  [ALIVE] (201/307) udp://15.235.207.99:8081/announce 161ms — valid connect + announce (v4)
  [ALIVE] (202/307) udp://107.189.2.131:1337/announce 230ms — valid connect + announce (v4)
  [ALIVE] (203/307) udp://164.152.110.70:6969/announce 46ms — valid connect + announce (v4)
  [ALIVE] (204/307) udp://tracker.fnix.net:6969/announce 164ms — valid connect + announce (v4)
  [ALIVE] (205/307) udp://180.131.145.175:6969/announce 13ms — valid connect + announce (v4)
  [ALIVE] (208/307) udp://192.99.100.68:6969/announce 65ms — valid connect + announce (v4)
  [ALIVE] (209/307) udp://160.30.240.158:1337/announce 147ms — valid connect + announce (v4)
  [ALIVE] (210/307) udp://23.94.174.203:1337/announce 30ms — valid connect + announce (v4)
  [ALIVE] (211/307) udp://178.239.19.29:80/announce 149ms — valid connect + announce (v4)
  [ALIVE] (212/307) udp://185.216.179.62:25/announce 148ms — valid connect + announce (v4)
  [ALIVE] (213/307) udp://211.75.205.187:6969/announce 132ms — valid connect + announce (v4)
  [ALIVE] (214/307) udp://193.187.90.12:6969/announce 161ms — valid connect + announce (v4)
  [ALIVE] (215/307) udp://51.222.82.36:6969/announce 66ms — valid connect + announce (v4)
  [ALIVE] (216/307) udp://212.42.38.197:6969/announce 176ms — valid connect + announce (v4)
  [ALIVE] (217/307) udp://47.76.201.250:6969/announce 138ms — valid connect + announce (v4)
  [ALIVE] (218/307) udp://45.38.170.167:6969/announce 161ms — valid connect + announce (v4)
  [ALIVE] (219/307) udp://31.59.141.120:6969/announce 186ms — valid connect + announce (v4)
  [ALIVE] (220/307) udp://74.119.149.136:6969/announce 65ms — valid connect + announce (v4)
  [ALIVE] (222/307) udp://74.81.245.60:2010/announce 70ms — valid connect + announce (v4)
  [DEAD]  (225/307) https://github.com:443/wuyuansushen/aria2c_TrackersList — HTTPError: HTTP Error 400: Bad Request
  [ALIVE] (228/307) udp://60.172.236.18:6969/announce 201ms — valid connect + announce (v4)
  [ALIVE] (229/307) udp://94.23.207.177:6969/announce 142ms — valid connect + announce (v4)
  [ALIVE] (249/307) https://open.ftorrent.com:443/announce 87ms — announce without peers
  [DEAD]  (250/307) http://tracker.bittor.pw:1337/announce — URLError: <urlopen error [Errno 101] Network is unreachable>
  [DEAD]  (275/307) https://sheraza2895.github.io:443 — invalid bencoded response
  [ALIVE] (283/307) udp://admin.52ywp.com:6969/announce 203ms — valid connect + announce (v4)
  [DEAD]  (300/307) udp://wepzone.net:6969/announce — no connect response
  [ALIVE] (306/307) https://tracker.bug38.com:443/announce 10753ms — announce with peers:1

[INFO] First pass done in 23.9s
[INFO] Multi-sample: 3 samples on top 50 alive trackers...
[INFO] Multi-sample refined 50 trackers (median + jitter penalty)
[INFO] Low-speed filtered (>5s): 3 trackers
[INFO] Same-subnet(/24) dedup removed 75 slower tracker(s)
[INFO] scrape probe: 18 http/https alive trackers
[INFO] scrape: 4 responded, 3 with seeders
[INFO] discovered candidates excluded from best/all: 148
[INFO] reserve pool: 20 discovered candidates -> trackers_reserve.txt
[INFO] promote queue: 60 tracked, 0 ready to promote
[INFO] Dynamic blacklist: 1 consistently-dead trackers

===== Test Summary =====
  Total tested:   307
  Alive (raw):    72
  Alive (final):  25 (top 25 by composite score)
  Non-UDP kept:   9 (quota >= 4)
  Classic kept:   3 (quota >= 4)
  Score-capped:   47
  Unsafe filtered:2
  Low-speed:      3 (>5s excluded)
  Same-subnet dedup:  75 (kept faster)
  Dead final:     265
  Time:           32.9s
=== 协议分布统计 ===
  HTTP  : 41 个
  HTTPS : 16 个
  UDP   : 93 个
  WSS   : 0 个
  WS    : 0 个
  总计: 150 个（存活）
=========================
[OK]   /s/alive
[OK]   /s/all
[OK]   index.html
[OK] Pages regenerated with alive statistics.
[OK]   docs/alive.txt
[OK]   docs/all.txt
[OK]   docs/reserve.txt
[OK]   docs/merged.txt
[OK]   docs/ngosang_best.txt
[OK]   docs/ngosang_best_ip.txt
[OK]   docs/cf_best.txt
[OK]   docs/adysec_best.txt
[OK]   docs/gonghailink_best.txt
[OK]   docs/pandamen_best.txt
[OK]   docs/gspu_best.txt
[OK]   docs/linuxjin_best.txt
[OK]   docs/alphacatmeow_best.txt
[OK]   docs/pexcn_best.txt
[OK]   docs/opentracker.txt
[OK]   docs/run_ws.txt
[OK]   docs/ngosang_i2p.txt
[OK]   docs/ngosang_yggdrasil.txt
[OK]   docs/udp.txt
[OK]   docs/http.txt
[OK]   docs/https.txt
[OK]   docs/wss.txt
[OK]   docs/ws.txt
[OK] Plain-text files synced to docs/.

============================================================
 Round 1 - 2026-10-14 05:07:19
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 58 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 248 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 17 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 17 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 18 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 14 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 62 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 23 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 47 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_all.txt: 49 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 164 candidates in 1 file(s)
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /all.txt: 49 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 58 trackers
  [PASS] Plain text: /adysec_best.txt: 248 trackers
  [PASS] Plain text: /gonghailink_best.txt: 17 trackers
  [PASS] Plain text: /pandamen_best.txt: 17 trackers
  [PASS] Plain text: /gspu_best.txt: 18 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 14 trackers
  [PASS] Plain text: /pexcn_best.txt: 62 trackers
  [PASS] Plain text: /opentracker.txt: 23 trackers
  [PASS] Plain text: /run_ws.txt: 47 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 79 trackers
  [PASS] Plain text: /http.txt: 71 trackers
  [PASS] Plain text: /https.txt: 49 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset-of-all check: all 25 best trackers present in all (49)
  [PASS] Reserve pool check: 20 candidates, disjoint
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_all.txt vs all.txt: identical
  [PASS] Consistency: trackers_reserve.txt vs reserve.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_ngosang_best.txt vs ngosang_best.txt: identical
  [PASS] Consistency: trackers_ngosang_best_ip.txt vs ngosang_best_ip.txt: identical
  [PASS] Consistency: trackers_cf_best.txt vs cf_best.txt: identical
  [PASS] Consistency: trackers_adysec_best.txt vs adysec_best.txt: identical
  [PASS] Consistency: trackers_gonghailink_best.txt vs gonghailink_best.txt: identical
  [PASS] Consistency: trackers_pandamen_best.txt vs pandamen_best.txt: identical
  [PASS] Consistency: trackers_gspu_best.txt vs gspu_best.txt: identical
  [PASS] Consistency: trackers_linuxjin_best.txt vs linuxjin_best.txt: identical
  [PASS] Consistency: trackers_alphacatmeow_best.txt vs alphacatmeow_best.txt: identical
  [PASS] Consistency: trackers_pexcn_best.txt vs pexcn_best.txt: identical
  [PASS] Consistency: trackers_opentracker.txt vs opentracker.txt: identical
  [PASS] Consistency: trackers_run_ws.txt vs run_ws.txt: identical
  [PASS] Consistency: trackers_ngosang_i2p.txt vs ngosang_i2p.txt: identical
  [PASS] Consistency: trackers_ngosang_yggdrasil.txt vs ngosang_yggdrasil.txt: identical
  [PASS] Consistency: trackers_udp.txt vs udp.txt: identical
  [PASS] Consistency: trackers_http.txt vs http.txt: identical
  [PASS] Consistency: trackers_https.txt vs https.txt: identical
  [PASS] Consistency: trackers_wss.txt vs wss.txt: identical
  [PASS] Consistency: trackers_ws.txt vs ws.txt: identical
  [PASS] URL format check: all 200 valid
------------------------------------------------------------
  Result: 75 passed, 0 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 1 rounds completed
   Total PASS: 75
   Total WARN: 0
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################

============================================================
 Round 1 - 2026-10-14 05:07:30
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 58 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 248 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 17 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 17 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 18 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 14 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 62 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 23 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 47 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_all.txt: 49 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 164 candidates in 1 file(s)
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /all.txt: 49 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 58 trackers
  [PASS] Plain text: /adysec_best.txt: 248 trackers
  [PASS] Plain text: /gonghailink_best.txt: 17 trackers
  [PASS] Plain text: /pandamen_best.txt: 17 trackers
  [PASS] Plain text: /gspu_best.txt: 18 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 14 trackers
  [PASS] Plain text: /pexcn_best.txt: 62 trackers
  [PASS] Plain text: /opentracker.txt: 23 trackers
  [PASS] Plain text: /run_ws.txt: 47 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 79 trackers
  [PASS] Plain text: /http.txt: 71 trackers
  [PASS] Plain text: /https.txt: 49 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset-of-all check: all 25 best trackers present in all (49)
  [PASS] Reserve pool check: 20 candidates, disjoint
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_all.txt vs all.txt: identical
  [PASS] Consistency: trackers_reserve.txt vs reserve.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_ngosang_best.txt vs ngosang_best.txt: identical
  [PASS] Consistency: trackers_ngosang_best_ip.txt vs ngosang_best_ip.txt: identical
  [PASS] Consistency: trackers_cf_best.txt vs cf_best.txt: identical
  [PASS] Consistency: trackers_adysec_best.txt vs adysec_best.txt: identical
  [PASS] Consistency: trackers_gonghailink_best.txt vs gonghailink_best.txt: identical
  [PASS] Consistency: trackers_pandamen_best.txt vs pandamen_best.txt: identical
  [PASS] Consistency: trackers_gspu_best.txt vs gspu_best.txt: identical
  [PASS] Consistency: trackers_linuxjin_best.txt vs linuxjin_best.txt: identical
  [PASS] Consistency: trackers_alphacatmeow_best.txt vs alphacatmeow_best.txt: identical
  [PASS] Consistency: trackers_pexcn_best.txt vs pexcn_best.txt: identical
  [PASS] Consistency: trackers_opentracker.txt vs opentracker.txt: identical
  [PASS] Consistency: trackers_run_ws.txt vs run_ws.txt: identical
  [PASS] Consistency: trackers_ngosang_i2p.txt vs ngosang_i2p.txt: identical
  [PASS] Consistency: trackers_ngosang_yggdrasil.txt vs ngosang_yggdrasil.txt: identical
  [PASS] Consistency: trackers_udp.txt vs udp.txt: identical
  [PASS] Consistency: trackers_http.txt vs http.txt: identical
  [PASS] Consistency: trackers_https.txt vs https.txt: identical
  [PASS] Consistency: trackers_wss.txt vs wss.txt: identical
  [PASS] Consistency: trackers_ws.txt vs ws.txt: identical
  [PASS] URL format check: all 200 valid
  [PASS] Raw: alive (Raw): HTTP 200, 25 trackers
  [PASS] Raw: merged (Raw): HTTP 200, 200 trackers
  [PASS] Pages: /alive.txt: HTTP 200, 25 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 200 trackers
  [PASS] Pages short: /s/alive: HTTP 200, redirect OK
  [PASS] Pages short: /s/all: HTTP 200, redirect OK
  [PASS] Worker best 短链: HTTP 200, 25 trackers
  [PASS] Worker all 短链: HTTP 200, 49 trackers
  [PASS] Worker best 加速: HTTP 200, 25 trackers
  [PASS] Worker all 加速: HTTP 200, 49 trackers
------------------------------------------------------------
  Result: 85 passed, 0 warnings, 0 failed
============================================================

============================================================
 Round 2 - 2026-10-14 05:07:35
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 58 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 248 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 17 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 17 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 18 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 14 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 62 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 23 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 47 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_all.txt: 49 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 164 candidates in 1 file(s)
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /all.txt: 49 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 58 trackers
  [PASS] Plain text: /adysec_best.txt: 248 trackers
  [PASS] Plain text: /gonghailink_best.txt: 17 trackers
  [PASS] Plain text: /pandamen_best.txt: 17 trackers
  [PASS] Plain text: /gspu_best.txt: 18 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 14 trackers
  [PASS] Plain text: /pexcn_best.txt: 62 trackers
  [PASS] Plain text: /opentracker.txt: 23 trackers
  [PASS] Plain text: /run_ws.txt: 47 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 79 trackers
  [PASS] Plain text: /http.txt: 71 trackers
  [PASS] Plain text: /https.txt: 49 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset-of-all check: all 25 best trackers present in all (49)
  [PASS] Reserve pool check: 20 candidates, disjoint
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_all.txt vs all.txt: identical
  [PASS] Consistency: trackers_reserve.txt vs reserve.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_ngosang_best.txt vs ngosang_best.txt: identical
  [PASS] Consistency: trackers_ngosang_best_ip.txt vs ngosang_best_ip.txt: identical
  [PASS] Consistency: trackers_cf_best.txt vs cf_best.txt: identical
  [PASS] Consistency: trackers_adysec_best.txt vs adysec_best.txt: identical
  [PASS] Consistency: trackers_gonghailink_best.txt vs gonghailink_best.txt: identical
  [PASS] Consistency: trackers_pandamen_best.txt vs pandamen_best.txt: identical
  [PASS] Consistency: trackers_gspu_best.txt vs gspu_best.txt: identical
  [PASS] Consistency: trackers_linuxjin_best.txt vs linuxjin_best.txt: identical
  [PASS] Consistency: trackers_alphacatmeow_best.txt vs alphacatmeow_best.txt: identical
  [PASS] Consistency: trackers_pexcn_best.txt vs pexcn_best.txt: identical
  [PASS] Consistency: trackers_opentracker.txt vs opentracker.txt: identical
  [PASS] Consistency: trackers_run_ws.txt vs run_ws.txt: identical
  [PASS] Consistency: trackers_ngosang_i2p.txt vs ngosang_i2p.txt: identical
  [PASS] Consistency: trackers_ngosang_yggdrasil.txt vs ngosang_yggdrasil.txt: identical
  [PASS] Consistency: trackers_udp.txt vs udp.txt: identical
  [PASS] Consistency: trackers_http.txt vs http.txt: identical
  [PASS] Consistency: trackers_https.txt vs https.txt: identical
  [PASS] Consistency: trackers_wss.txt vs wss.txt: identical
  [PASS] Consistency: trackers_ws.txt vs ws.txt: identical
  [PASS] URL format check: all 200 valid
  [PASS] Raw: alive (Raw): HTTP 200, 25 trackers
  [PASS] Raw: merged (Raw): HTTP 200, 200 trackers
  [PASS] Pages: /alive.txt: HTTP 200, 25 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 200 trackers
  [PASS] Pages short: /s/alive: HTTP 200, redirect OK
  [PASS] Pages short: /s/all: HTTP 200, redirect OK
  [PASS] Worker best 短链: HTTP 200, 25 trackers
  [PASS] Worker all 短链: HTTP 200, 49 trackers
  [PASS] Worker best 加速: HTTP 200, 25 trackers
  [PASS] Worker all 加速: HTTP 200, 49 trackers
------------------------------------------------------------
  Result: 85 passed, 0 warnings, 0 failed
============================================================

============================================================
 Round 3 - 2026-10-14 05:07:41
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 58 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 248 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 17 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 17 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 18 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 14 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 62 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 23 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 47 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_all.txt: 49 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 164 candidates in 1 file(s)
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /all.txt: 49 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 58 trackers
  [PASS] Plain text: /adysec_best.txt: 248 trackers
  [PASS] Plain text: /gonghailink_best.txt: 17 trackers
  [PASS] Plain text: /pandamen_best.txt: 17 trackers
  [PASS] Plain text: /gspu_best.txt: 18 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 14 trackers
  [PASS] Plain text: /pexcn_best.txt: 62 trackers
  [PASS] Plain text: /opentracker.txt: 23 trackers
  [PASS] Plain text: /run_ws.txt: 47 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 79 trackers
  [PASS] Plain text: /http.txt: 71 trackers
  [PASS] Plain text: /https.txt: 49 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset-of-all check: all 25 best trackers present in all (49)
  [PASS] Reserve pool check: 20 candidates, disjoint
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_all.txt vs all.txt: identical
  [PASS] Consistency: trackers_reserve.txt vs reserve.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_ngosang_best.txt vs ngosang_best.txt: identical
  [PASS] Consistency: trackers_ngosang_best_ip.txt vs ngosang_best_ip.txt: identical
  [PASS] Consistency: trackers_cf_best.txt vs cf_best.txt: identical
  [PASS] Consistency: trackers_adysec_best.txt vs adysec_best.txt: identical
  [PASS] Consistency: trackers_gonghailink_best.txt vs gonghailink_best.txt: identical
  [PASS] Consistency: trackers_pandamen_best.txt vs pandamen_best.txt: identical
  [PASS] Consistency: trackers_gspu_best.txt vs gspu_best.txt: identical
  [PASS] Consistency: trackers_linuxjin_best.txt vs linuxjin_best.txt: identical
  [PASS] Consistency: trackers_alphacatmeow_best.txt vs alphacatmeow_best.txt: identical
  [PASS] Consistency: trackers_pexcn_best.txt vs pexcn_best.txt: identical
  [PASS] Consistency: trackers_opentracker.txt vs opentracker.txt: identical
  [PASS] Consistency: trackers_run_ws.txt vs run_ws.txt: identical
  [PASS] Consistency: trackers_ngosang_i2p.txt vs ngosang_i2p.txt: identical
  [PASS] Consistency: trackers_ngosang_yggdrasil.txt vs ngosang_yggdrasil.txt: identical
  [PASS] Consistency: trackers_udp.txt vs udp.txt: identical
  [PASS] Consistency: trackers_http.txt vs http.txt: identical
  [PASS] Consistency: trackers_https.txt vs https.txt: identical
  [PASS] Consistency: trackers_wss.txt vs wss.txt: identical
  [PASS] Consistency: trackers_ws.txt vs ws.txt: identical
  [PASS] URL format check: all 200 valid
  [PASS] Raw: alive (Raw): HTTP 200, 25 trackers
  [PASS] Raw: merged (Raw): HTTP 200, 200 trackers
  [PASS] Pages: /alive.txt: HTTP 200, 25 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 200 trackers
  [PASS] Pages short: /s/alive: HTTP 200, redirect OK
  [PASS] Pages short: /s/all: HTTP 200, redirect OK
  [PASS] Worker best 短链: HTTP 200, 25 trackers
  [PASS] Worker all 短链: HTTP 200, 49 trackers
  [PASS] Worker best 加速: HTTP 200, 25 trackers
  [PASS] Worker all 加速: HTTP 200, 49 trackers
------------------------------------------------------------
  Result: 85 passed, 0 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 3 rounds completed
   Total PASS: 255
   Total WARN: 0
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################
=== End of diagnostics (Wed Oct 14 05:07:41 UTC 2026) ===
