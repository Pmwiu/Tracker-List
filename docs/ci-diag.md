=== Diagnostics Tue Oct 13 02:31:24 UTC 2026 ===
Python: Python 3.12.15
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_best.txt
  HTTP 200, total 0.041381s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_best_ip.txt
  HTTP 200, total 0.032497s
>>> https://cf.trackerslist.com/best.txt
  HTTP 200, total 0.138761s
>>> https://tracker.adysec.com/trackers_best.txt
  HTTP 200, total 0.406135s
>>> https://raw.githubusercontent.com/gonghailink/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.224158s
>>> https://raw.githubusercontent.com/panda-men/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.223331s
>>> https://raw.githubusercontent.com/gspu/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.167019s
>>> https://raw.githubusercontent.com/linux-jin/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.290763s
>>> https://raw.githubusercontent.com/AlphaCatMeow/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.166437s
>>> https://raw.githubusercontent.com/pexcn/daily/gh-pages/trackerlist/trackerlist-best.txt
  HTTP 200, total 0.137232s
>>> https://raw.githubusercontent.com/1265578519/OpenTracker/refs/heads/master/tracker.txt
  HTTP 200, total 0.205202s
>>> https://trackers.run/s/rw_ws_up_hp_hs_v4_v6.txt
  HTTP 200, total 0.478514s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_i2p.txt
  HTTP 200, total 0.320348s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_yggdrasil.txt
  HTTP 200, total 0.202864s
[INFO] Repo: Pmwiu/Tracker-List, Max: 25
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/ngosang/trackerslist/master/blacklist.txt (391 URLs)
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/blacklist.txt (20 URLs)
[INFO] URL blacklist: 390 URLs (dynamic + remote sources)

[INFO] trackers_ngosang_best.txt (ngosang-best)
[OK]   20 unique

[INFO] trackers_ngosang_best_ip.txt (ngosang-best-ip)
[OK]   20 unique

[INFO] trackers_cf_best.txt (cf-best)
  [INFO] Skipped 10 dynamic-blacklisted lines
[OK]   60 unique

[INFO] trackers_adysec_best.txt (adysec-best)
  [INFO] Skipped 71 dynamic-blacklisted lines
[OK]   249 unique

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
  [INFO] Skipped 10 dynamic-blacklisted lines
[OK]   63 unique

[INFO] trackers_opentracker.txt (opentracker)
  [INFO] Skipped 8 dynamic-blacklisted lines
[OK]   27 unique

[INFO] trackers_run_ws.txt (trackersrun-ws)
  [INFO] Skipped 2 dynamic-blacklisted lines
[OK]   46 unique

[INFO] trackers_ngosang_i2p.txt (ngosang-i2p)
[OK]   17 unique

[INFO] trackers_ngosang_yggdrasil.txt (ngosang-yggdrasil)
  [INFO] Skipped 1 dynamic-blacklisted lines
[WARN] trackers_ngosang_yggdrasil.txt failed (No valid trackers found in response); using backup (1 trackers)
[OK]   1 unique

[INFO] all 合并贡献: ngosang-best=20, ngosang-best-ip=20, cf-best=32, adysec-best=46, gonghailink-best=6, pandamen-best=7, gspu-best=3, linuxjin-best=1, alphacatmeow-best=3, pexcn-best=1, opentracker=14, trackersrun-ws=29, ngosang-i2p=17, ngosang-yggdrasil=1
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
  trackers_adysec_best.txt: 249
  trackers_gonghailink_best.txt: 17
  trackers_pandamen_best.txt: 18
  trackers_gspu_best.txt: 19
  trackers_linuxjin_best.txt: 20
  trackers_alphacatmeow_best.txt: 15
  trackers_pexcn_best.txt: 63
  trackers_opentracker.txt: 27
  trackers_run_ws.txt: 46
  trackers_ngosang_i2p.txt: 17
  trackers_ngosang_yggdrasil.txt: 1
  trackers_merged.txt: 200
  alive capped at 25 after test+sort
===================
[INFO] Testing 200 candidates (all-pool=200, timeout=10s, workers=30)
[INFO] Max alive trackers after scoring: 25
  [ALIVE] (3/200) http://207.241.226.111:6969/announce 7ms — announce with peers
  [ALIVE] (4/200) http://207.241.231.226:6969/announce 10ms — announce with peers
  [ALIVE] (5/200) http://216.144.239.90:6969/announce 60ms — announce with peers
  [ALIVE] (6/200) http://34.66.57.33:2701/announce 97ms — announce with peers
  [ALIVE] (7/200) http://140.235.237.23:6969/announce 174ms — announce with peers
  [ALIVE] (9/200) http://1337.abcvg.info:80/announce 258ms — announce with peers
  [ALIVE] (10/200) http://211.75.205.188:6969/announce 276ms — announce with peers
  [ALIVE] (11/200) http://211.75.205.188:80/announce 276ms — announce with peers
  [ALIVE] (12/200) http://211.75.205.187:6969/announce 278ms — announce with peers
  [ALIVE] (13/200) http://211.75.205.187:80/announce 279ms — announce with peers
  [ALIVE] (14/200) http://185.126.65.92:6969/announce 280ms — announce with peers
  [ALIVE] (15/200) http://211.75.210.221:80/announce 278ms — announce with peers
  [ALIVE] (16/200) http://211.75.210.221:6969/announce 278ms — announce with peers
  [ALIVE] (17/200) http://004430.xyz:80/announce 51ms — announce with peers
  [ALIVE] (18/200) http://138.186.10.167:1337/announce 295ms — announce without peers
  [ALIVE] (19/200) http://94.23.207.177:6969/announce 293ms — announce with peers
  [ALIVE] (20/200) http://43.250.54.126:6969/announce 295ms — announce with peers
  [ALIVE] (21/200) http://107.189.2.131:1337/announce 306ms — announce with peers
  [ALIVE] (22/200) http://135.125.198.235:2710/announce 304ms — announce with peers
  [ALIVE] (23/200) http://135.125.198.235:80/announce 304ms — announce with peers
  [ALIVE] (24/200) http://93.158.213.92:1337/announce 298ms — announce with peers
  [DEAD]  (25/200) http://bittorrent.kali.org:80/announce — restricted (failure reason)
  [ALIVE] (26/200) http://31.38.161.123:6969/announce 323ms — announce with peers
  [ALIVE] (28/200) http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 356ms — announce with peers
  [ALIVE] (29/200) http://share.hkg-fansub.info:80/announce 93ms — announce with peers
  [ALIVE] (37/200) http://tracker.004430.xyz:1337/announce 25ms — announce with peers
  [ALIVE] (38/200) http://t-backup.213891.xyz:80/announce 195ms — announce with peers
  [ALIVE] (39/200) http://open.demonii.si:80/announce 339ms — announce with peers
  [ALIVE] (40/200) http://tracker.bittor.pw:1337/announce 92ms — announce with peers
  [ALIVE] (41/200) http://tr.nyacat.pw:80/announce 174ms — announce with peers
  [ALIVE] (42/200) http://torrentsmd.me:8080/announce 210ms — announce with peers
  [ALIVE] (43/200) http://t.nyaatracker.com:80/announce 349ms — announce with peers
  [ALIVE] (45/200) http://tracker.coppersurfer.site:2710/announce 304ms — announce with peers
  [ALIVE] (46/200) http://retracker01-msk-virt.corbina.net:80/announce 377ms — announce with peers
  [ALIVE] (47/200) http://announce.sktorrent.eu:6969/announce 733ms — announce with peers
  [ALIVE] (48/200) http://tracker-zhuqiy.dgj055.icu:80/announce 349ms — announce with peers
  [ALIVE] (49/200) http://tracker.dhitechnical.com:6969/announce 256ms — announce with peers
  [ALIVE] (50/200) http://tracker.auctor.tv:6969/announce 287ms — announce with peers
  [ALIVE] (51/200) http://tracker.dler.org:6969/announce 289ms — announce with peers
  [ALIVE] (52/200) http://ipv4announce.sktorrent.eu:6969/announce 284ms — announce with peers
  [ALIVE] (53/200) http://tracker.nyaa.vc:6969/announce 280ms — announce with peers
  [ALIVE] (54/200) http://t.overflow.biz:6969/announce 420ms — announce with peers
  [ALIVE] (55/200) http://tracker.qu.ax:6969/announce 303ms — announce with peers
  [ALIVE] (56/200) http://tracker.k.vu:6969/announce 385ms — announce with peers
  [ALIVE] (58/200) http://tracker.mywaifu.best:6969/announce 311ms — announce with peers
  [ALIVE] (59/200) http://tracker.renfei.net:8080/announce 186ms — announce with peers
  [ALIVE] (60/200) http://tracker.waaa.moe:6969/announce 73ms — announce with peers
  [ALIVE] (61/200) http://tracker2.dler.org:80/announce 451ms — announce with peers
  [ALIVE] (62/200) http://tracker.opentrackr.org:1337/announce 441ms — announce with peers
  [ALIVE] (63/200) https://004430.xyz:443/announce 314ms — announce with peers
  [ALIVE] (64/200) https://1.tracker.eu.org:443/announce 23ms — announce with peers
  [ALIVE] (65/200) http://tracker.novaopcj.eu.org:6969/announce 281ms — announce with peers
  [ALIVE] (66/200) https://3.tracker.eu.org:443/announce 20ms — announce with peers
  [ALIVE] (67/200) http://tracker.dler.com:6969/announce 434ms — announce with peers
  [ALIVE] (68/200) http://opentracker.xyz:80/announce 1034ms — announce with peers
  [ALIVE] (69/200) https://4.tracker.eu.org:443/announce 17ms — announce with peers
  [ALIVE] (71/200) https://t.213891.xyz:443/announce 229ms — announce with peers
  [ALIVE] (73/200) https://tr.nyacat.pw:443/announce 299ms — announce with peers
  [ALIVE] (74/200) https://337hhh.xyz:443/announce 459ms — announce with peers
  [SKIP]   (75/200) http://btrackrqkjp6kgelov5a3uxisis77ofxqt5nvy5hvvtoybjpmq4q.b32.i2p:80/announce — I2P network required
  [ALIVE] (76/200) https://tracker.7471.top:443/announce 333ms — announce with peers
  [ALIVE] (77/200) https://2.tracker.eu.org:443/announce 28ms — announce with peers
  [ALIVE] (78/200) http://open.tracker.cl:1337/announce 859ms — announce without peers
  [ALIVE] (80/200) udp://132.226.6.145:6969/announce 105ms — valid connect + announce
  [ALIVE] (83/200) https://tracker.foreverpirates.co:443/announce 473ms — announce with peers
  [ALIVE] (85/200) udp://109.201.134.183:80/announce 153ms — valid connect + announce
  [ALIVE] (88/200) udp://23.157.120.14:6969/announce 28ms — valid connect + announce
  [ALIVE] (90/200) https://tracker.midnightprogrammer.net:443/announce 468ms — announce with peers
  [ALIVE] (92/200) udp://193.148.251.93:6969/announce 58ms — valid connect + announce
  [ALIVE] (93/200) https://tracker.nekomi.cn:443/announce 66ms — announce with peers
  [ALIVE] (96/200) udp://51.81.222.188:6969/announce 15ms — valid connect + announce
  [ALIVE] (97/200) udp://135.125.198.235:1984/announce 152ms — valid connect + announce
  [ALIVE] (99/200) udp://34.66.57.33:1337/announce 47ms — valid connect + announce
  [ALIVE] (100/200) udp://34.66.57.33:80/announce 49ms — valid connect + announce
  [ALIVE] (101/200) udp://151.242.104.187:80/announce 151ms — valid connect + announce
  [ALIVE] (102/200) udp://185.121.168.96:1337/announce 148ms — valid connect + announce
  [ALIVE] (104/200) udp://211.75.205.187:6969/announce 139ms — valid connect + announce
  [ALIVE] (105/200) udp://211.75.205.187:80/announce 138ms — valid connect + announce
  [ALIVE] (108/200) udp://193.34.92.5:80/announce 182ms — valid connect + announce
  [ALIVE] (109/200) udp://31.38.161.123:6969/announce 161ms — valid connect + announce
  [ALIVE] (110/200) udp://43.154.112.29:17272/announce 146ms — valid connect + announce
  [ALIVE] (111/200) udp://43.250.54.126:6969/announce 148ms — valid connect + announce
  [ALIVE] (112/200) udp://45.137.199.107:6969/announce 148ms — valid connect + announce
  [ALIVE] (114/200) udp://31.56.179.159:6969/announce 169ms — valid connect + announce
  [ALIVE] (115/200) udp://51.15.41.46:6969/announce 151ms — valid connect + announce
  [ALIVE] (116/200) udp://explodie.org:6969/announce 23ms — valid connect + announce
  [ALIVE] (117/200) udp://93.158.213.92:1337/announce 139ms — valid connect + announce
  [ALIVE] (118/200) udp://89.234.156.205:451/announce 148ms — valid connect + announce
  [ALIVE] (119/200) udp://93.158.213.92:6969/announce 145ms — valid connect + announce
  [ALIVE] (120/200) udp://65.109.28.17:6969/announce 167ms — valid connect + announce
  [ALIVE] (121/200) udp://65.109.28.33:6969/announce 170ms — valid connect + announce
  [ALIVE] (122/200) udp://83.102.180.21:80/announce 190ms — valid connect + announce
  [ALIVE] (123/200) udp://exodus.desync.com:6969/announce 3ms — valid connect + announce
  [ALIVE] (125/200) udp://95.217.80.20:6969/announce 172ms — valid connect + announce
  [ALIVE] (126/200) udp://open.ftorrent.com:443/announce 28ms — valid connect + announce
  [ALIVE] (129/200) udp://evan.im:6969/announce 69ms — valid connect + announce
  [ALIVE] (130/200) udp://95.217.80.22:6969/announce 174ms — valid connect + announce
  [ALIVE] (131/200) udp://ipv4announce.sktorrent.eu:6969/announce 143ms — valid connect + announce
  [ALIVE] (133/200) udp://mail.segso.net:6969/announce 172ms — valid connect + announce
  [ALIVE] (134/200) udp://tracker.004430.xyz:1337/announce 9ms — valid connect + announce
  [ALIVE] (135/200) udp://open.demonii.com:1337/announce 147ms — valid connect + announce
  [ALIVE] (136/200) udp://open.stealth.si:80/announce 163ms — valid connect + announce
  [ALIVE] (137/200) udp://martin-gebhardt.eu:25/announce 148ms — valid connect + announce
  [ALIVE] (139/200) udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 267ms — valid connect + announce
  [ALIVE] (140/200) udp://tracker.bittor.pw:1337/announce 49ms — valid connect + announce
  [ALIVE] (141/200) udp://t.overflow.biz:6969/announce 168ms — valid connect + announce
  [ALIVE] (143/200) udp://retracker01-msk-virt.corbina.net:80/announce 185ms — valid connect + announce
  [ALIVE] (144/200) udp://tr4ck3r.duckdns.org:6969/announce 67ms — valid connect + announce
  [ALIVE] (145/200) udp://tracker.corpscorp.online:80/announce 47ms — valid connect + announce
  [ALIVE] (146/200) udp://tracker-udp.gbitt.info:80/announce 149ms — valid connect + announce
  [ALIVE] (147/200) udp://tracker.dler.org:6969/announce 138ms — valid connect + announce
  [ALIVE] (148/200) udp://tracker.cn.nyaa.net:6969/announce 146ms — valid connect + announce
  [ALIVE] (149/200) udp://opentracker.lain.moscow:6969/announce 158ms — valid connect + announce
  [ALIVE] (150/200) udp://tracker.ducks.party:1984/announce 153ms — valid connect + announce
  [ALIVE] (151/200) udp://tracker.gmi.gd:6969/announce 109ms — valid connect + announce
  [ALIVE] (152/200) udp://tracker.farted.net:6969/announce 164ms — valid connect + announce
  [ALIVE] (153/200) udp://tracker.filemail.com:6969/announce 150ms — valid connect + announce
  [ALIVE] (154/200) udp://tracker.nyaa.vc:6969/announce 141ms — valid connect + announce
  [ALIVE] (155/200) udp://tracker.opentrackr.org:1337/announce 143ms — valid connect + announce
  [ALIVE] (156/200) udp://tracker.nyaa.net:6969/announce 187ms — valid connect + announce
  [ALIVE] (157/200) udp://tracker.ilibr.org:6969/announce 172ms — valid connect + announce
  [ALIVE] (158/200) udp://tracker.qu.ax:6969/announce 151ms — valid connect + announce
  [ALIVE] (159/200) udp://tracker.aruku.ovh:8081/announce 167ms — valid connect + announce
  [ALIVE] (160/200) udp://tracker.opentrackr.com:6969/announce 171ms — valid connect + announce
  [ALIVE] (161/200) udp://tracker.peerfect.org:6969/announce 172ms — valid connect + announce
  [ALIVE] (162/200) udp://tracker.skynetcloud.site:6969/announce 138ms — valid connect + announce
  [ALIVE] (163/200) udp://tracker.wildkat.net:6969/announce 48ms — valid connect + announce
  [ALIVE] (165/200) udp://tracker2.dler.org:80/announce 138ms — valid connect + announce
  [ALIVE] (166/200) udp://tracker.willy.pro:6969/announce 231ms — valid connect + announce
  [ALIVE] (167/200) udp://tracker.torrent.eu.org:451/announce 151ms — valid connect + announce
  [ALIVE] (171/200) wss://spacetradersapi-chatbox.herokuapp.com:443/announce 264ms — TLS reachable
  [ALIVE] (173/200) wss://tracker.openwebtorrent.com:443/announce 160ms — TLS reachable
  [ALIVE] (174/200) wss://tracker.files.fm:7073/announce 377ms — TLS reachable
  [ALIVE] (175/200) wss://tracker.magnetoo.io:443/announce 263ms — TLS reachable
  [ALIVE] (176/200) http://retracker.x2k.ru:80/announce 5085ms — announce with peers
  [ALIVE] (177/200) udp://52.58.128.163:6969/announce 165ms — valid connect + announce
  [DEAD]  (200/200) udp://wepzone.net:6969/announce — no connect response

[INFO] First pass done in 14.7s
[INFO] Second pass: re-testing top 100 alive trackers...
[INFO] Second pass done, refined 96 trackers
[INFO] Low-speed filtered (>5s): 1 trackers
[INFO] Same-subnet(/24) dedup removed 70 slower tracker(s)
[INFO] Dynamic blacklist: 1 consistently-dead trackers

===== Test Summary =====
  Total tested:   200
  Alive (raw):    63
  Alive (final):  25 (top 25 by composite score)
  Non-UDP kept:   7 (quota >= 4)
  Classic kept:   3 (quota >= 4)
  Score-capped:   38
  Unsafe filtered:3
  Low-speed:      1 (>5s excluded)
  Same-subnet dedup:  70 (kept faster)
  Dead final:     154
  Time:           23.6s
=== 协议分布统计 ===
  HTTP  : 53 个
  HTTPS : 12 个
  UDP   : 65 个
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
 Round 1 - 2026-10-13 02:31:54
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 60 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 249 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 17 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 18 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 19 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 63 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 27 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 46 trackers
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
  [PASS] Plain text: /adysec_best.txt: 249 trackers
  [PASS] Plain text: /gonghailink_best.txt: 17 trackers
  [PASS] Plain text: /pandamen_best.txt: 18 trackers
  [PASS] Plain text: /gspu_best.txt: 19 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 15 trackers
  [PASS] Plain text: /pexcn_best.txt: 63 trackers
  [PASS] Plain text: /opentracker.txt: 27 trackers
  [PASS] Plain text: /run_ws.txt: 46 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 91 trackers
  [PASS] Plain text: /http.txt: 84 trackers
  [PASS] Plain text: /https.txt: 20 trackers
  [PASS] Plain text: /wss.txt: 5 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset-of-all check: all 25 best trackers present in all (59)
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
 Round 1 - 2026-10-13 02:32:06
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 60 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 249 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 17 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 18 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 19 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 63 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 27 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 46 trackers
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
  [PASS] Plain text: /adysec_best.txt: 249 trackers
  [PASS] Plain text: /gonghailink_best.txt: 17 trackers
  [PASS] Plain text: /pandamen_best.txt: 18 trackers
  [PASS] Plain text: /gspu_best.txt: 19 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 15 trackers
  [PASS] Plain text: /pexcn_best.txt: 63 trackers
  [PASS] Plain text: /opentracker.txt: 27 trackers
  [PASS] Plain text: /run_ws.txt: 46 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 91 trackers
  [PASS] Plain text: /http.txt: 84 trackers
  [PASS] Plain text: /https.txt: 20 trackers
  [PASS] Plain text: /wss.txt: 5 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset-of-all check: all 25 best trackers present in all (59)
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
  [PASS] Worker best 加速: HTTP 200, 25 trackers
  [PASS] Worker all 加速: HTTP 200, 59 trackers
------------------------------------------------------------
  Result: 82 passed, 0 warnings, 0 failed
============================================================

============================================================
 Round 2 - 2026-10-13 02:32:13
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 60 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 249 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 17 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 18 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 19 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 63 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 27 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 46 trackers
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
  [PASS] Plain text: /adysec_best.txt: 249 trackers
  [PASS] Plain text: /gonghailink_best.txt: 17 trackers
  [PASS] Plain text: /pandamen_best.txt: 18 trackers
  [PASS] Plain text: /gspu_best.txt: 19 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 15 trackers
  [PASS] Plain text: /pexcn_best.txt: 63 trackers
  [PASS] Plain text: /opentracker.txt: 27 trackers
  [PASS] Plain text: /run_ws.txt: 46 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 91 trackers
  [PASS] Plain text: /http.txt: 84 trackers
  [PASS] Plain text: /https.txt: 20 trackers
  [PASS] Plain text: /wss.txt: 5 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset-of-all check: all 25 best trackers present in all (59)
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
  [PASS] Worker best 加速: HTTP 200, 25 trackers
  [PASS] Worker all 加速: HTTP 200, 59 trackers
------------------------------------------------------------
  Result: 82 passed, 0 warnings, 0 failed
============================================================

============================================================
 Round 3 - 2026-10-13 02:32:20
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 60 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 249 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 17 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 18 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 19 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 63 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 27 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 46 trackers
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
  [PASS] Plain text: /adysec_best.txt: 249 trackers
  [PASS] Plain text: /gonghailink_best.txt: 17 trackers
  [PASS] Plain text: /pandamen_best.txt: 18 trackers
  [PASS] Plain text: /gspu_best.txt: 19 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 15 trackers
  [PASS] Plain text: /pexcn_best.txt: 63 trackers
  [PASS] Plain text: /opentracker.txt: 27 trackers
  [PASS] Plain text: /run_ws.txt: 46 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 91 trackers
  [PASS] Plain text: /http.txt: 84 trackers
  [PASS] Plain text: /https.txt: 20 trackers
  [PASS] Plain text: /wss.txt: 5 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset-of-all check: all 25 best trackers present in all (59)
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
  [PASS] Worker best 加速: HTTP 200, 25 trackers
  [PASS] Worker all 加速: HTTP 200, 59 trackers
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
=== End of diagnostics (Tue Oct 13 02:32:20 UTC 2026) ===
