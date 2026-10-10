=== Diagnostics Sat Oct 10 06:04:56 UTC 2026 ===
Python: Python 3.12.15
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_best.txt
  HTTP 200, total 0.031714s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_best_ip.txt
  HTTP 200, total 0.216905s
>>> https://cf.trackerslist.com/best.txt
  HTTP 200, total 0.133840s
>>> https://tracker.adysec.com/trackers_best.txt
  HTTP 200, total 0.103086s
>>> https://raw.githubusercontent.com/gonghailink/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.122662s
>>> https://raw.githubusercontent.com/panda-men/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.107393s
>>> https://raw.githubusercontent.com/gspu/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.116299s
>>> https://raw.githubusercontent.com/linux-jin/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.108339s
>>> https://raw.githubusercontent.com/AlphaCatMeow/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.104065s
>>> https://raw.githubusercontent.com/pexcn/daily/gh-pages/trackerlist/trackerlist-best.txt
  HTTP 200, total 0.083259s
>>> https://raw.githubusercontent.com/1265578519/OpenTracker/refs/heads/master/tracker.txt
  HTTP 200, total 0.070160s
>>> https://trackers.run/s/rw_ws_up_hp_hs_v4_v6.txt
  HTTP 200, total 0.416083s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_i2p.txt
  HTTP 200, total 0.025499s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_yggdrasil.txt
  HTTP 200, total 0.026907s
[INFO] Repo: Pmwiu/Tracker-List, Max: 25
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/ngosang/trackerslist/master/blacklist.txt (391 URLs)
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/blacklist.txt (20 URLs)
[INFO] URL blacklist: 389 URLs (dynamic + remote sources)

[INFO] trackers_ngosang_best.txt (ngosang-best)
[OK]   20 unique

[INFO] trackers_ngosang_best_ip.txt (ngosang-best-ip)
[OK]   20 unique

[INFO] trackers_cf_best.txt (cf-best)
  [INFO] Skipped 10 dynamic-blacklisted lines
[OK]   60 unique

[INFO] trackers_adysec_best.txt (adysec-best)
  [INFO] Skipped 66 dynamic-blacklisted lines
[OK]   235 unique

[INFO] trackers_gonghailink_best.txt (gonghailink-best)
  [INFO] Skipped 3 dynamic-blacklisted lines
[OK]   17 unique

[INFO] trackers_pandamen_best.txt (pandamen-best)
  [INFO] Skipped 2 dynamic-blacklisted lines
[OK]   18 unique

[INFO] trackers_gspu_best.txt (gspu-best)
  [INFO] Skipped 1 dynamic-blacklisted lines
[OK]   19 unique

[INFO] trackers_linuxjin_best.txt (linuxjin-best)
[OK]   20 unique

[INFO] trackers_alphacatmeow_best.txt (alphacatmeow-best)
  [INFO] Skipped 5 dynamic-blacklisted lines
[OK]   15 unique

[INFO] trackers_pexcn_best.txt (pexcn-best)
  [INFO] Skipped 9 dynamic-blacklisted lines
[OK]   62 unique

[INFO] trackers_opentracker.txt (opentracker)
  [INFO] Skipped 8 dynamic-blacklisted lines
[OK]   27 unique

[INFO] trackers_run_ws.txt (trackersrun-ws)
  [INFO] Skipped 2 dynamic-blacklisted lines
[OK]   45 unique

[INFO] trackers_ngosang_i2p.txt (ngosang-i2p)
[OK]   17 unique

[INFO] trackers_ngosang_yggdrasil.txt (ngosang-yggdrasil)
[OK]   1 unique

[INFO] all 合并贡献: ngosang-best=20, ngosang-best-ip=20, cf-best=31, adysec-best=46, gonghailink-best=7, pandamen-best=7, gspu-best=3, linuxjin-best=2, alphacatmeow-best=2, pexcn-best=1, opentracker=14, trackersrun-ws=29, ngosang-i2p=17, ngosang-yggdrasil=1
[INFO] all 协议分布: http=84, https=20, udp=91, wss=5, ws=0

[OK]   merged: 200
[OK]   MIRRORS.txt
[OK]   /s/alive
[OK]   /s/all
[OK]   index.html
[OK]   docs/alive.txt
[OK]   docs/all.txt
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
  trackers_cf_best.txt: 60
  trackers_adysec_best.txt: 235
  trackers_gonghailink_best.txt: 17
  trackers_pandamen_best.txt: 18
  trackers_gspu_best.txt: 19
  trackers_linuxjin_best.txt: 20
  trackers_alphacatmeow_best.txt: 15
  trackers_pexcn_best.txt: 62
  trackers_opentracker.txt: 27
  trackers_run_ws.txt: 45
  trackers_ngosang_i2p.txt: 17
  trackers_ngosang_yggdrasil.txt: 1
  trackers_merged.txt: 200
  alive capped at 25 after test+sort
===================
[INFO] Testing 200 candidates (all-pool=200, timeout=10s, workers=30)
[INFO] Max alive trackers after scoring: 25
  [ALIVE] (3/200) http://207.241.226.111:6969/announce 130ms — announce with peers
  [ALIVE] (4/200) http://207.241.231.226:6969/announce 134ms — announce with peers
  [ALIVE] (6/200) http://004430.xyz:80/announce 143ms — announce with peers
  [ALIVE] (8/200) http://93.158.213.92:1337/announce 166ms — announce with peers
  [ALIVE] (9/200) http://94.23.207.177:6969/announce 170ms — announce with peers
  [ALIVE] (10/200) http://185.126.65.92:6969/announce 179ms — announce with peers
  [ALIVE] (11/200) http://43.250.54.126:6969/announce 175ms — announce with peers
  [ALIVE] (12/200) http://135.125.198.235:2710/announce 184ms — announce with peers
  [ALIVE] (13/200) http://135.125.198.235:80/announce 187ms — announce with peers
  [ALIVE] (14/200) http://31.38.161.123:6969/announce 215ms — announce with peers
  [ALIVE] (15/200) http://138.186.10.167:1337/announce 228ms — announce without peers
  [ALIVE] (16/200) http://107.189.2.131:1337/announce 234ms — announce with peers
  [ALIVE] (17/200) http://announce.sktorrent.eu:6969/announce 216ms — announce with peers
  [ALIVE] (18/200) http://216.144.239.90:6969/announce 254ms — announce with peers
  [ALIVE] (20/200) http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 198ms — announce with peers
  [ALIVE] (21/200) http://140.235.237.23:6969/announce 318ms — announce with peers
  [ALIVE] (22/200) http://1337.abcvg.info:80/announce 269ms — announce with peers
  [ALIVE] (23/200) http://ipv4announce.sktorrent.eu:6969/announce 183ms — announce with peers
  [ALIVE] (24/200) http://211.75.205.187:6969/announce 376ms — announce with peers
  [ALIVE] (25/200) http://211.75.205.188:6969/announce 377ms — announce with peers
  [ALIVE] (26/200) http://211.75.205.187:80/announce 378ms — announce with peers
  [ALIVE] (27/200) http://211.75.205.188:80/announce 380ms — announce with peers
  [ALIVE] (28/200) http://211.75.210.221:6969/announce 381ms — announce with peers
  [ALIVE] (29/200) http://211.75.210.221:80/announce 381ms — announce with peers
  [ALIVE] (30/200) http://t-backup.213891.xyz:80/announce 29ms — announce with peers
  [ALIVE] (31/200) http://open.demonii.si:80/announce 232ms — announce with peers
  [ALIVE] (32/200) http://tr.nyacat.pw:80/announce 111ms — announce with peers
  [ALIVE] (33/200) http://tracker.004430.xyz:1337/announce 138ms — announce with peers
  [ALIVE] (34/200) http://tracker.coppersurfer.site:2710/announce 180ms — announce with peers
  [ALIVE] (36/200) http://tracker.auctor.tv:6969/announce 176ms — announce with peers
  [ALIVE] (40/200) http://retracker.x2k.ru:80/announce 353ms — announce with peers
  [ALIVE] (44/200) http://t.nyaatracker.com:80/announce 242ms — announce with peers
  [ALIVE] (45/200) http://tracker.dhitechnical.com:6969/announce 313ms — announce with peers
  [ALIVE] (46/200) http://tracker-zhuqiy.dgj055.icu:80/announce 243ms — announce with peers
  [ALIVE] (47/200) http://tracker.nyaa.vc:6969/announce 183ms — announce with peers
  [ALIVE] (48/200) http://tracker.mywaifu.best:6969/announce 201ms — announce with peers
  [ALIVE] (49/200) http://tracker.qu.ax:6969/announce 189ms — announce with peers
  [DEAD]  (50/200) http://tracker.trancetraffic.com:80/announce — restricted (failure reason)
  [ALIVE] (51/200) http://open.tracker.cl:1337/announce 282ms — announce without peers
  [ALIVE] (52/200) http://retracker01-msk-virt.corbina.net:80/announce 446ms — announce with peers
  [ALIVE] (53/200) http://tracker.dler.com:6969/announce 380ms — announce with peers
  [ALIVE] (54/200) http://tracker.renfei.net:8080/announce 30ms — announce with peers
  [ALIVE] (55/200) http://tracker.torrents.observer:80/announce 183ms — announce with peers
  [ALIVE] (57/200) http://opentracker.xyz:80/announce 568ms — announce with peers
  [ALIVE] (59/200) http://tracker.k.vu:6969/announce 520ms — announce with peers
  [ALIVE] (60/200) https://004430.xyz:443/announce 147ms — announce with peers
  [ALIVE] (61/200) http://tracker.opentrackr.org:1337/announce 273ms — announce with peers
  [ALIVE] (62/200) http://tracker.dler.org:6969/announce 554ms — announce with peers
  [ALIVE] (63/200) https://t.213891.xyz:443/announce 16ms — announce with peers
  [ALIVE] (65/200) http://tracker.waaa.moe:6969/announce 309ms — announce with peers
  [ALIVE] (66/200) https://1.tracker.eu.org:443/announce 47ms — announce with peers
  [ALIVE] (67/200) https://2.tracker.eu.org:443/announce 34ms — announce with peers
  [ALIVE] (68/200) http://tracker.zhuqiy.dgj055.icu:80/announce 243ms — announce with peers
  [ALIVE] (69/200) https://3.tracker.eu.org:443/announce 43ms — announce with peers
  [ALIVE] (72/200) https://tr.nyacat.pw:443/announce 117ms — announce with peers
  [ALIVE] (73/200) https://tracker.7471.top:443/announce 118ms — announce with peers
  [ALIVE] (74/200) https://4.tracker.eu.org:443/announce 32ms — announce with peers
  [ALIVE] (75/200) https://337hhh.xyz:443/announce 279ms — announce with peers
  [ALIVE] (76/200) http://tracker2.dler.org:80/announce 482ms — announce with peers
  [ALIVE] (80/200) udp://109.201.134.183:80/announce 83ms — valid connect + announce
  [ALIVE] (81/200) http://tracker2.dler.com:80/announce 551ms — announce with peers
  [ALIVE] (82/200) udp://193.148.251.93:6969/announce 37ms — valid connect + announce
  [ALIVE] (83/200) udp://135.125.198.235:1984/announce 91ms — valid connect + announce
  [ALIVE] (84/200) https://tracker.foreverpirates.co:443/announce 327ms — announce with peers
  [ALIVE] (85/200) http://tracker.novaopcj.eu.org:6969/announce 176ms — announce with peers
  [ALIVE] (86/200) udp://151.242.104.187:80/announce 94ms — valid connect + announce
  [ALIVE] (87/200) udp://209.141.59.25:6969/announce 67ms — valid connect + announce
  [ALIVE] (89/200) udp://193.34.92.5:80/announce 122ms — valid connect + announce
  [ALIVE] (90/200) udp://34.66.57.33:1337/announce 32ms — valid connect + announce
  [ALIVE] (91/200) udp://34.66.57.33:80/announce 30ms — valid connect + announce
  [ALIVE] (92/200) udp://31.38.161.123:6969/announce 106ms — valid connect + announce
  [ALIVE] (95/200) udp://23.157.120.14:6969/announce 115ms — valid connect + announce
  [ALIVE] (96/200) udp://185.121.168.96:1337/announce 178ms — valid connect + announce
  [ALIVE] (98/200) udp://31.56.179.159:6969/announce 107ms — valid connect + announce
  [SKIP]   (100/200) http://opentracker.dg2.i2p:80/a — I2P network required
  [ALIVE] (103/200) udp://211.75.205.188:6969/announce 190ms — valid connect + announce
  [ALIVE] (106/200) udp://43.250.54.126:6969/announce 90ms — valid connect + announce
  [ALIVE] (107/200) udp://51.81.222.188:6969/announce 67ms — valid connect + announce
  [ALIVE] (109/200) udp://211.75.210.221:80/announce 191ms — valid connect + announce
  [ALIVE] (110/200) udp://45.137.199.107:6969/announce 90ms — valid connect + announce
  [ALIVE] (111/200) udp://51.15.41.46:6969/announce 83ms — valid connect + announce
  [ALIVE] (112/200) udp://52.58.128.163:6969/announce 90ms — valid connect + announce
  [ALIVE] (115/200) udp://89.234.156.205:451/announce 94ms — valid connect + announce
  [ALIVE] (116/200) udp://evan.im:6969/announce 2ms — valid connect + announce
  [ALIVE] (117/200) https://tracker.nekomi.cn:443/announce 151ms — announce with peers
  [ALIVE] (118/200) udp://93.158.213.92:1337/announce 83ms — valid connect + announce
  [ALIVE] (119/200) udp://65.109.28.17:6969/announce 115ms — valid connect + announce
  [ALIVE] (121/200) udp://93.158.213.92:6969/announce 89ms — valid connect + announce
  [ALIVE] (122/200) udp://83.102.180.21:80/announce 131ms — valid connect + announce
  [ALIVE] (123/200) udp://95.217.80.22:6969/announce 113ms — valid connect + announce
  [ALIVE] (124/200) udp://95.217.80.20:6969/announce 115ms — valid connect + announce
  [ALIVE] (125/200) udp://43.154.112.29:17272/announce 201ms — valid connect + announce
  [ALIVE] (127/200) udp://ipv4announce.sktorrent.eu:6969/announce 91ms — valid connect + announce
  [ALIVE] (128/200) udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 125ms — valid connect + announce
  [ALIVE] (129/200) udp://open.ftorrent.com:443/announce 46ms — valid connect + announce
  [ALIVE] (131/200) udp://martin-gebhardt.eu:25/announce 94ms — valid connect + announce
  [ALIVE] (132/200) udp://tr4ck3r.duckdns.org:6969/announce 15ms — valid connect + announce
  [ALIVE] (134/200) udp://mail.segso.net:6969/announce 119ms — valid connect + announce
  [ALIVE] (135/200) udp://explodie.org:6969/announce 119ms — valid connect + announce
  [ALIVE] (137/200) udp://tracker.004430.xyz:1337/announce 61ms — valid connect + announce
  [ALIVE] (138/200) udp://tracker.bittor.pw:1337/announce 27ms — valid connect + announce
  [ALIVE] (139/200) udp://retracker01-msk-virt.corbina.net:80/announce 135ms — valid connect + announce
  [ALIVE] (141/200) udp://open.stealth.si:80/announce 92ms — valid connect + announce
  [ALIVE] (142/200) udp://opentracker.lain.moscow:6969/announce 95ms — valid connect + announce
  [ALIVE] (143/200) udp://admin.52ywp.com:6969/announce 260ms — valid connect + announce
  [ALIVE] (144/200) udp://tracker-udp.gbitt.info:80/announce 89ms — valid connect + announce
  [ALIVE] (145/200) udp://kolankoalastree.newtrackon.co.nz:1337/announce 208ms — valid connect + announce
  [ALIVE] (146/200) udp://tracker.ducks.party:1984/announce 91ms — valid connect + announce
  [ALIVE] (147/200) udp://tracker.corpscorp.online:80/announce 27ms — valid connect + announce
  [ALIVE] (149/200) udp://tracker.filemail.com:6969/announce 90ms — valid connect + announce
  [ALIVE] (150/200) udp://tracker.farted.net:6969/announce 105ms — valid connect + announce
  [ALIVE] (151/200) udp://tracker.nyaa.vc:6969/announce 90ms — valid connect + announce
  [ALIVE] (152/200) udp://tracker.dler.org:6969/announce 192ms — valid connect + announce
  [ALIVE] (153/200) udp://tracker.opentrackr.org:1337/announce 95ms — valid connect + announce
  [ALIVE] (154/200) udp://tracker.nyaa.net:6969/announce 130ms — valid connect + announce
  [ALIVE] (155/200) udp://tracker.qu.ax:6969/announce 82ms — valid connect + announce
  [ALIVE] (156/200) udp://tracker.opentrackr.com:6969/announce 112ms — valid connect + announce
  [ALIVE] (157/200) udp://tracker.gmi.gd:6969/announce 66ms — valid connect + announce
  [ALIVE] (158/200) udp://tracker.cn.nyaa.net:6969/announce 200ms — valid connect + announce
  [ALIVE] (159/200) udp://tracker.wildkat.net:6969/announce 21ms — valid connect + announce
  [ALIVE] (160/200) udp://tracker.ilibr.org:6969/announce 116ms — valid connect + announce
  [ALIVE] (161/200) udp://tracker.skynetcloud.site:6969/announce 84ms — valid connect + announce
  [ALIVE] (162/200) udp://tracker.torrents.observer:80/announce 91ms — valid connect + announce
  [ALIVE] (163/200) udp://tracker.aruku.ovh:8081/announce 223ms — valid connect + announce
  [ALIVE] (164/200) udp://tracker.peerfect.org:6969/announce 119ms — valid connect + announce
  [ALIVE] (165/200) udp://tracker.tryhackx.org:6969/announce 139ms — valid connect + announce
  [ALIVE] (166/200) udp://tracker.willy.pro:6969/announce 229ms — valid connect + announce
  [ALIVE] (167/200) udp://tracker.torrent.eu.org:451/announce 111ms — valid connect + announce
  [ALIVE] (169/200) udp://tracker2.dler.org:80/announce 190ms — valid connect + announce
  [ALIVE] (170/200) wss://spacetradersapi-chatbox.herokuapp.com:443/announce 43ms — TLS reachable
  [ALIVE] (171/200) udp://v2.iperson.xyz:6969/announce 249ms — valid connect + announce
  [ALIVE] (172/200) wss://tracker.openwebtorrent.com:443/announce 9ms — TLS reachable
  [ALIVE] (173/200) wss://tracker.files.fm:7073/announce 244ms — TLS reachable
  [ALIVE] (175/200) wss://tracker.magnetoo.io:443/announce 248ms — TLS reachable
  [ALIVE] (178/200) udp://t.overflow.biz:6969/announce 116ms — valid connect + announce
  [ALIVE] (179/200) http://t.overflow.biz:6969/announce 250ms — announce with peers
  [DEAD]  (200/200) udp://wepzone.net:6969/announce — no connect response

[INFO] First pass done in 14.0s
[INFO] Second pass: re-testing top 100 alive trackers...
[INFO] Second pass done, refined 97 trackers
[INFO] Same-subnet(/24) dedup removed 66 slower tracker(s)

===== Test Summary =====
  Total tested:   200
  Alive (raw):    68
  Alive (final):  25 (top 25 by composite score)
  Non-UDP kept:   10 (quota >= 4)
  Classic kept:   1 (quota >= 4)
  Score-capped:   43
  Unsafe filtered:3
  Low-speed:      0 (>5s excluded)
  Same-subnet dedup:  66 (kept faster)
  Dead final:     154
  Time:           22.6s
=== 协议分布统计 ===
  HTTP  : 52 个
  HTTPS : 11 个
  UDP   : 67 个
  WSS   : 4 个
  WS    : 0 个
  总计: 134 个（存活）
=========================
[OK]   /s/alive
[OK]   /s/all
[OK]   index.html
[OK] Pages regenerated with alive statistics.
[OK]   docs/alive.txt
[OK]   docs/all.txt
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
 Round 1 - 2026-10-10 06:05:22
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 60 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 235 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 17 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 18 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 19 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 62 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 27 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 45 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_all.txt: 59 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /all.txt: 59 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 60 trackers
  [PASS] Plain text: /adysec_best.txt: 235 trackers
  [PASS] Plain text: /gonghailink_best.txt: 17 trackers
  [PASS] Plain text: /pandamen_best.txt: 18 trackers
  [PASS] Plain text: /gspu_best.txt: 19 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 15 trackers
  [PASS] Plain text: /pexcn_best.txt: 62 trackers
  [PASS] Plain text: /opentracker.txt: 27 trackers
  [PASS] Plain text: /run_ws.txt: 45 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 91 trackers
  [PASS] Plain text: /http.txt: 84 trackers
  [PASS] Plain text: /https.txt: 20 trackers
  [PASS] Plain text: /wss.txt: 5 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset check: best is subset of all
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_all.txt vs all.txt: identical
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
  Result: 72 passed, 0 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 1 rounds completed
   Total PASS: 72
   Total WARN: 0
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################

============================================================
 Round 1 - 2026-10-10 06:05:29
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 60 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 235 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 17 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 18 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 19 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 62 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 27 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 45 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_all.txt: 59 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /all.txt: 59 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 60 trackers
  [PASS] Plain text: /adysec_best.txt: 235 trackers
  [PASS] Plain text: /gonghailink_best.txt: 17 trackers
  [PASS] Plain text: /pandamen_best.txt: 18 trackers
  [PASS] Plain text: /gspu_best.txt: 19 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 15 trackers
  [PASS] Plain text: /pexcn_best.txt: 62 trackers
  [PASS] Plain text: /opentracker.txt: 27 trackers
  [PASS] Plain text: /run_ws.txt: 45 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 91 trackers
  [PASS] Plain text: /http.txt: 84 trackers
  [PASS] Plain text: /https.txt: 20 trackers
  [PASS] Plain text: /wss.txt: 5 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset check: best is subset of all
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_all.txt vs all.txt: identical
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
  [PASS] Worker all 短链: HTTP 200, 59 trackers
  [PASS] Worker best 加速: HTTP 200, 20 trackers
  [PASS] Worker all 加速: HTTP 200, 37 trackers
------------------------------------------------------------
  Result: 82 passed, 0 warnings, 0 failed
============================================================

============================================================
 Round 2 - 2026-10-10 06:05:34
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 60 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 235 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 17 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 18 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 19 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 62 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 27 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 45 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_all.txt: 59 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /all.txt: 59 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 60 trackers
  [PASS] Plain text: /adysec_best.txt: 235 trackers
  [PASS] Plain text: /gonghailink_best.txt: 17 trackers
  [PASS] Plain text: /pandamen_best.txt: 18 trackers
  [PASS] Plain text: /gspu_best.txt: 19 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 15 trackers
  [PASS] Plain text: /pexcn_best.txt: 62 trackers
  [PASS] Plain text: /opentracker.txt: 27 trackers
  [PASS] Plain text: /run_ws.txt: 45 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 91 trackers
  [PASS] Plain text: /http.txt: 84 trackers
  [PASS] Plain text: /https.txt: 20 trackers
  [PASS] Plain text: /wss.txt: 5 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset check: best is subset of all
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_all.txt vs all.txt: identical
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
  [PASS] Worker all 短链: HTTP 200, 59 trackers
  [PASS] Worker best 加速: HTTP 200, 20 trackers
  [PASS] Worker all 加速: HTTP 200, 37 trackers
------------------------------------------------------------
  Result: 82 passed, 0 warnings, 0 failed
============================================================

============================================================
 Round 3 - 2026-10-10 06:05:39
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 60 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 235 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 17 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 18 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 19 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 62 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 27 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 45 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_all.txt: 59 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /all.txt: 59 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 60 trackers
  [PASS] Plain text: /adysec_best.txt: 235 trackers
  [PASS] Plain text: /gonghailink_best.txt: 17 trackers
  [PASS] Plain text: /pandamen_best.txt: 18 trackers
  [PASS] Plain text: /gspu_best.txt: 19 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 15 trackers
  [PASS] Plain text: /pexcn_best.txt: 62 trackers
  [PASS] Plain text: /opentracker.txt: 27 trackers
  [PASS] Plain text: /run_ws.txt: 45 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 91 trackers
  [PASS] Plain text: /http.txt: 84 trackers
  [PASS] Plain text: /https.txt: 20 trackers
  [PASS] Plain text: /wss.txt: 5 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset check: best is subset of all
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_all.txt vs all.txt: identical
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
  [PASS] Worker all 短链: HTTP 200, 59 trackers
  [PASS] Worker best 加速: HTTP 200, 20 trackers
  [PASS] Worker all 加速: HTTP 200, 37 trackers
------------------------------------------------------------
  Result: 82 passed, 0 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 3 rounds completed
   Total PASS: 246
   Total WARN: 0
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################
=== End of diagnostics (Sat Oct 10 06:05:39 UTC 2026) ===
