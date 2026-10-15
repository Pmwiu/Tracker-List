=== Diagnostics Thu Oct 15 11:47:09 UTC 2026 ===
Python: Python 3.12.15
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_best.txt
  HTTP 200, total 0.044429s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_best_ip.txt
  HTTP 200, total 0.235830s
>>> https://cf.trackerslist.com/best.txt
  HTTP 200, total 0.122072s
>>> https://tracker.adysec.com/trackers_best.txt
  HTTP 200, total 0.256565s
>>> https://raw.githubusercontent.com/gonghailink/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.133096s
>>> https://raw.githubusercontent.com/panda-men/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.137051s
>>> https://raw.githubusercontent.com/gspu/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.143507s
>>> https://raw.githubusercontent.com/linux-jin/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.121719s
>>> https://raw.githubusercontent.com/AlphaCatMeow/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.147841s
>>> https://raw.githubusercontent.com/pexcn/daily/gh-pages/trackerlist/trackerlist-best.txt
  HTTP 200, total 0.126525s
>>> https://raw.githubusercontent.com/1265578519/OpenTracker/refs/heads/master/tracker.txt
  HTTP 200, total 0.135371s
>>> https://trackers.run/s/rw_ws_up_hp_hs_v4_v6.txt
  HTTP 200, total 0.564493s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_i2p.txt
  HTTP 200, total 0.534280s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_yggdrasil.txt
  HTTP 200, total 1.287534s
[INFO] public list https://cf.trackerslist.com/all.txt: 122 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all.txt: 76 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ip.txt: 52 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_udp.txt: 48 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_http.txt: 18 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_https.txt: 10 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ws.txt: 3 urls
[OK]   1278 new candidates -> candidates_20261015.txt
[OK]   1278 new candidates
[INFO] Repo: Pmwiu/Tracker-List, Max: 25
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/ngosang/trackerslist/master/blacklist.txt (391 URLs)
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/blacklist.txt (20 URLs)
[INFO] URL blacklist: 390 URLs (dynamic + remote sources)
[INFO] Protected hosts (防误杀): 59
[INFO] discovered candidates: 1060 URLs in 1 file(s)

[INFO] trackers_ngosang_best.txt (ngosang-best)
[OK]   20 unique

[INFO] trackers_ngosang_best_ip.txt (ngosang-best-ip)
[OK]   20 unique

[INFO] trackers_cf_best.txt (cf-best)
  [INFO] Skipped 10 dynamic-blacklisted lines
[OK]   61 unique

[INFO] trackers_adysec_best.txt (adysec-best)
  [INFO] Skipped 64 dynamic-blacklisted lines
[OK]   246 unique

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
[OK]   58 unique

[INFO] trackers_opentracker.txt (opentracker)
  [INFO] Skipped 4 invalid lines
  [INFO] Skipped 8 dynamic-blacklisted lines
[OK]   23 unique

[INFO] trackers_run_ws.txt (trackersrun-ws)
  [INFO] Skipped 2 dynamic-blacklisted lines
[OK]   51 unique

[INFO] trackers_ngosang_i2p.txt (ngosang-i2p)
[OK]   17 unique

[INFO] trackers_ngosang_yggdrasil.txt (ngosang-yggdrasil)
  [INFO] Skipped 1 dynamic-blacklisted lines
[WARN] trackers_ngosang_yggdrasil.txt failed (No valid trackers found in response); using backup (1 trackers)
[OK]   1 unique

[INFO] all 合并贡献: ngosang-best=20, ngosang-best-ip=20, cf-best=18, adysec-best=29, gonghailink-best=6, pandamen-best=6, gspu-best=3, linuxjin-best=4, alphacatmeow-best=3, pexcn-best=11, opentracker=9, trackersrun-ws=19, ngosang-i2p=17, ngosang-yggdrasil=1
[INFO] all 协议分布: http=100, https=19, udp=80, wss=1, ws=0

[OK]   merged: 200
[OK]   source_counts.json (200)
[OK]   discovered_set.json (1060)
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
  trackers_cf_best.txt: 61
  trackers_adysec_best.txt: 246
  trackers_gonghailink_best.txt: 17
  trackers_pandamen_best.txt: 18
  trackers_gspu_best.txt: 19
  trackers_linuxjin_best.txt: 20
  trackers_alphacatmeow_best.txt: 15
  trackers_pexcn_best.txt: 58
  trackers_opentracker.txt: 23
  trackers_run_ws.txt: 51
  trackers_ngosang_i2p.txt: 17
  trackers_ngosang_yggdrasil.txt: 1
  trackers_merged.txt: 200
  alive capped at 25 after test+sort
===================
[INFO] reserve: +120 discovered candidates for liveness test (rotation, cap 120)
[INFO] Testing 320 candidates (all-pool=200, timeout=10s, workers=30)
[INFO] Max alive trackers after scoring: 25
  [ALIVE] (4/320) http://004430.xyz:80/announce 132ms — announce with peers:1
  [ALIVE] (5/320) http://107.189.2.131:1337/announce 225ms — announce with peers:1
  [ALIVE] (6/320) http://135.125.198.235:2710/announce 224ms — announce without peers
  [ALIVE] (7/320) http://135.125.198.235:80/announce 224ms — announce without peers
  [ALIVE] (8/320) http://138.186.10.167:1337/announce 240ms — announce with peers:1
  [ALIVE] (9/320) http://1337.abcvg.info:80/announce 341ms — announce with peers:1
  [ALIVE] (10/320) http://140.235.237.23:6969/announce 640ms — announce with peers:1
  [ALIVE] (13/320) http://185.126.65.92:6969/announce 195ms — announce without peers
  [ALIVE] (15/320) http://189.18.97.208:6969/announce 261ms — announce with peers:1
  [ALIVE] (16/320) http://207.241.226.111:6969/announce 102ms — announce with peers:1
  [ALIVE] (17/320) http://207.241.231.226:6969/announce 97ms — announce with peers:1
  [ALIVE] (18/320) http://211.75.205.187:6969/announce 453ms — announce with peers:1
  [ALIVE] (19/320) http://211.75.205.187:80/announce 436ms — announce with peers:1
  [ALIVE] (20/320) http://211.75.205.188:6969/announce 438ms — announce with peers:1
  [ALIVE] (21/320) http://211.75.205.188:80/announce 437ms — announce with peers:1
  [ALIVE] (22/320) http://211.75.210.221:6969/announce 437ms — announce with peers:1
  [ALIVE] (23/320) http://211.75.210.221:80/announce 439ms — announce with peers:1
  [ALIVE] (24/320) http://216.144.239.90:6969/announce 108ms — announce with peers:1
  [ALIVE] (25/320) http://31.38.161.123:6969/announce 226ms — announce with peers:1
  [ALIVE] (26/320) http://43.250.54.126:6969/announce 209ms — announce with peers:1
  [ALIVE] (27/320) http://93.158.213.92:1337/announce 206ms — announce with peers:1
  [ALIVE] (28/320) http://94.23.207.177:6969/announce 201ms — announce with peers:1
  [ALIVE] (29/320) http://announce.sktorrent.eu:6969/announce 207ms — announce with peers:1
  [ALIVE] (30/320) http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 281ms — announce with peers:1
  [DEAD]  (50/320) http://116.9.207.198:6969/announce — URLError: <urlopen error timed out>
  [ALIVE] (66/320) http://tracker.dhitechnical.com:6969/announce 227ms — announce with peers:1
  [ALIVE] (67/320) http://tracker.auctor.tv:6969/announce 189ms — announce with peers:1
  [ALIVE] (69/320) http://ipv4announce.sktorrent.eu:6969/announce 203ms — announce with peers:1
  [ALIVE] (70/320) http://tracker.nyaa.vc:6969/announce 203ms — announce without peers
  [ALIVE] (71/320) http://open.demonii.si:80/announce 256ms — announce without peers
  [ALIVE] (72/320) http://tracker.qu.ax:6969/announce 211ms — announce with peers:1
  [ALIVE] (73/320) http://tracker.waaa.moe:6969/announce 134ms — announce with peers:1
  [ALIVE] (75/320) https://004430.xyz:443/announce 125ms — announce with peers:1
  [ALIVE] (77/320) http://tracker.renfei.net:8080/announce 68ms — announce with peers:1
  [ALIVE] (78/320) http://tracker.mywaifu.best:6969/announce 331ms — announce without peers
  [ALIVE] (79/320) http://tracker.opentrackr.org:1337/announce 311ms — announce with peers:1
  [ALIVE] (80/320) https://t.213891.xyz:443/announce 28ms — announce without peers
  [ALIVE] (81/320) https://1.tracker.eu.org:443/announce 36ms — announce without peers
  [ALIVE] (83/320) http://tracker.dler.com:6969/announce 463ms — announce with peers:1
  [ALIVE] (84/320) http://tracker.dler.org:6969/announce 472ms — announce with peers:1
  [ALIVE] (85/320) https://3.tracker.eu.org:443/announce 38ms — announce without peers
  [ALIVE] (86/320) https://2.tracker.eu.org:443/announce 47ms — announce without peers
  [ALIVE] (89/320) http://open.tracker.cl:1337/announce 281ms — announce with peers:1
  [ALIVE] (90/320) http://retracker01-msk-virt.corbina.net:80/announce 498ms — announce with peers:1
  [ALIVE] (91/320) https://tracker.7471.top:443/announce 136ms — announce without peers
  [ALIVE] (92/320) https://337hhh.xyz:443/announce 345ms — announce without peers
  [ALIVE] (94/320) https://tr.nyacat.pw:443/announce 113ms — announce without peers
  [ALIVE] (95/320) https://tracker.foreverpirates.co:443/announce 171ms — announce without peers
  [ALIVE] (97/320) udp://193.148.251.93:6969/announce 21ms — valid connect + announce (v4)
  [ALIVE] (98/320) http://tracker2.dler.org:80/announce 637ms — announce with peers:1
  [ALIVE] (99/320) udp://109.201.134.183:80/announce 104ms — valid connect + announce (v4)
  [ALIVE] (100/320) https://tracker.zhuqiy.com:443/announce 57ms — announce with peers:1
  [ALIVE] (101/320) udp://151.242.104.187:80/announce 106ms — valid connect + announce (v4)
  [ALIVE] (102/320) udp://135.125.198.235:1984/announce 112ms — valid connect + announce (v4)
  [ALIVE] (103/320) https://tracker.midnightprogrammer.net:443/announce 304ms — announce without peers
  [ALIVE] (104/320) http://opentracker.xyz:80/announce 812ms — announce with peers:1
  [ALIVE] (105/320) udp://23.157.120.14:6969/announce 61ms — valid connect + announce (v4)
  [ALIVE] (106/320) udp://132.226.6.145:6969/announce 144ms — valid connect + announce (v4)
  [ALIVE] (107/320) udp://34.66.57.33:1337/announce 11ms — valid connect + announce (v4)
  [ALIVE] (108/320) udp://34.66.57.33:80/announce 12ms — valid connect + announce (v4)
  [ALIVE] (109/320) udp://189.18.97.208:6969/announce 130ms — valid connect + announce (v4)
  [ALIVE] (110/320) udp://193.34.92.5:80/announce 141ms — valid connect + announce (v4)
  [ALIVE] (111/320) udp://51.81.222.188:6969/announce 52ms — valid connect + announce (v4)
  [ALIVE] (112/320) udp://185.121.168.96:1337/announce 192ms — valid connect + announce (v4)
  [ALIVE] (113/320) udp://31.38.161.123:6969/announce 119ms — valid connect + announce (v4)
  [ALIVE] (114/320) https://tracker.nekomi.cn:443/announce 119ms — announce with peers:1
  [ALIVE] (115/320) udp://43.250.54.126:6969/announce 106ms — valid connect + announce (v4)
  [ALIVE] (116/320) udp://51.15.41.46:6969/announce 106ms — valid connect + announce (v4)
  [ALIVE] (117/320) udp://31.56.179.159:6969/announce 135ms — valid connect + announce (v4)
  [ALIVE] (118/320) udp://45.137.199.107:6969/announce 130ms — valid connect + announce (v4)
  [ALIVE] (119/320) udp://211.75.205.188:80/announce 219ms — valid connect + announce (v4)
  [ALIVE] (120/320) udp://211.75.205.188:6969/announce 232ms — valid connect + announce (v4)
  [ALIVE] (121/320) udp://43.154.112.29:17272/announce 184ms — valid connect + announce (v4)
  [ALIVE] (122/320) udp://65.109.28.17:6969/announce 129ms — valid connect + announce (v4)
  [ALIVE] (123/320) udp://65.109.28.33:6969/announce 128ms — valid connect + announce (v4)
  [ALIVE] (124/320) udp://93.158.213.92:1337/announce 104ms — valid connect + announce (v4)
  [ALIVE] (125/320) udp://89.234.156.205:451/announce 112ms — valid connect + announce (v4)
  [ALIVE] (126/320) udp://93.158.213.92:6969/announce 106ms — valid connect + announce (v4)
  [ALIVE] (127/320) udp://83.102.180.21:80/announce 151ms — valid connect + announce (v4)
  [ALIVE] (128/320) udp://95.217.80.20:6969/announce 132ms — valid connect + announce (v4)
  [ALIVE] (129/320) udp://evan.im:6969/announce 29ms — valid connect + announce (v4)
  [ALIVE] (130/320) udp://95.217.80.22:6969/announce 128ms — valid connect + announce (v4)
  [ALIVE] (131/320) udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 111ms — valid connect + announce (v4)
  [ALIVE] (134/320) udp://ipv4announce.sktorrent.eu:6969/announce 101ms — valid connect + announce (v4)
  [ALIVE] (139/320) udp://exodus.desync.com:6969/announce 52ms — valid connect + announce (v4)
  [ALIVE] (141/320) udp://mail.segso.net:6969/announce 124ms — valid connect + announce (v4)
  [ALIVE] (142/320) udp://explodie.org:6969/announce 56ms — valid connect + announce (v4)
  [ALIVE] (146/320) udp://open.ftorrent.com:443/announce 31ms — valid connect + announce (v4)
  [ALIVE] (148/320) udp://martin-gebhardt.eu:25/announce 109ms — valid connect + announce (v4)
  [ALIVE] (150/320) udp://open.stealth.si:80/announce 104ms — valid connect + announce (v4)
  [ALIVE] (152/320) udp://kolankoalastree.newtrackon.co.nz:1337/announce 203ms — valid connect + announce (v4)
  [ALIVE] (153/320) udp://tracker.bittor.pw:1337/announce 11ms — valid connect + announce (v4)
  [ALIVE] (154/320) udp://tracker.004430.xyz:1337/announce 46ms — valid connect + announce (v4)
  [ALIVE] (155/320) udp://tracker.corpscorp.online:80/announce 12ms — valid connect + announce (v4)
  [ALIVE] (156/320) udp://open.demonii.com:1337/announce 190ms — valid connect + announce (v4)
  [ALIVE] (158/320) udp://tracker-udp.gbitt.info:80/announce 99ms — valid connect + announce (v4)
  [ALIVE] (160/320) udp://retracker01-msk-virt.corbina.net:80/announce 144ms — valid connect + announce (v4)
  [ALIVE] (162/320) udp://tracker.nyaa.vc:6969/announce 121ms — valid connect + announce (v4)
  [ALIVE] (163/320) udp://tracker.opentrackr.org:1337/announce 102ms — valid connect + announce (v4)
  [ALIVE] (164/320) udp://opentracker.lain.moscow:6969/announce 114ms — valid connect + announce (v4)
  [ALIVE] (165/320) udp://tracker.gmi.gd:6969/announce 76ms — valid connect + announce (v4)
  [ALIVE] (166/320) udp://tracker.qu.ax:6969/announce 98ms — valid connect + announce (v4)
  [ALIVE] (167/320) udp://tracker.opentrackr.com:6969/announce 128ms — valid connect + announce (v4)
  [ALIVE] (168/320) udp://tracker.dler.org:6969/announce 217ms — valid connect + announce (v4)
  [ALIVE] (169/320) udp://t.overflow.biz:6969/announce 141ms — valid connect + announce (v4)
  [ALIVE] (170/320) udp://tracker.farted.net:6969/announce 130ms — valid connect + announce (v4)
  [ALIVE] (171/320) udp://tracker.ducks.party:1984/announce 109ms — valid connect + announce (v4)
  [ALIVE] (172/320) udp://tracker.peerfect.org:6969/announce 130ms — valid connect + announce (v4)
  [ALIVE] (174/320) udp://tracker.skynetcloud.site:6969/announce 100ms — valid connect + announce (v4)
  [ALIVE] (175/320) udp://tracker2.dler.org:80/announce 220ms — valid connect + announce (v4)
  [ALIVE] (176/320) udp://tracker.torrent.eu.org:451/announce 110ms — valid connect + announce (v4)
  [ALIVE] (181/320) udp://52.58.128.163:6969/announce 112ms — valid connect + announce (v4)
  [ALIVE] (182/320) udp://tracker.theoks.net:6969/announce 59ms — valid connect + announce (v4)
  [ALIVE] (183/320) udp://tracker.tryhackx.org:6969/announce 116ms — valid connect + announce (v4)
  [DEAD]  (200/320) udp://open.tracker.ink:6969/announce — no connect response
  [ALIVE] (218/320) udp://obey.torrentonline.cc:42069/announce 2508ms — valid connect + announce (v4)
  [DEAD]  (225/320) udp://open.4ever.tk:6969/announce — no connect response
  [DEAD]  (250/320) udp://rep-art.ynh.fr:6969/announce — no connect response
  [ALIVE] (251/320) udp://tr4ck3r.duckdns.org:6969/announce 25ms — valid connect + announce (v4)
  [ALIVE] (268/320) udp://tracker.aruku.ovh:8081/announce 206ms — valid connect + announce (v4)
  [ALIVE] (270/320) udp://tracker.cn.nyaa.net:6969/announce 189ms — valid connect + announce (v4)
  [ALIVE] (273/320) udp://tracker.cyberia.is:6969/announce 139ms — valid connect + announce (v4)
  [DEAD]  (275/320) udp://static.54.161.216.95.clients.your-server.de:6969/announce — no connect response
  [ALIVE] (288/320) udp://tracker.ilibr.org:6969/announce 131ms — valid connect + announce (v4)
  [ALIVE] (289/320) udp://tracker.ilibr.org:80/announce 128ms — valid connect + announce (v4)
  [DEAD]  (300/320) udp://tracker.4.babico.name.tr:3131/announce — no connect response

[INFO] First pass done in 92.0s
[INFO] Multi-sample: 3 samples on top 50 alive trackers...
[INFO] Multi-sample refined 48 trackers (median + jitter penalty)
[INFO] Same-subnet(/24) dedup removed 60 slower tracker(s)
[INFO] scrape probe: 20 http/https alive trackers
[INFO] scrape: 4 responded, 2 with seeders
[INFO] discovered candidates excluded from best/all: 1060
[INFO] reserve pool: 9 discovered candidates -> trackers_reserve.txt
[INFO] promote queue: 72 tracked, 3 ready to promote
[INFO] Dynamic blacklist: 1 consistently-dead trackers

===== Test Summary =====
  Total tested:   320
  Alive (raw):    60
  Alive (final):  25 (top 25 by composite score)
  Non-UDP kept:   12 (quota >= 4)
  Classic kept:   3 (quota >= 4)
  Score-capped:   35
  Unsafe filtered:5
  Low-speed:      0 (>5s excluded)
  Same-subnet dedup:  60 (kept faster)
  Dead final:     278
  Time:           101.1s
=== 协议分布统计 ===
  HTTP  : 40 个
  HTTPS : 12 个
  UDP   : 68 个
  WSS   : 0 个
  WS    : 0 个
  总计: 120 个（存活）
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
 Round 1 - 2026-10-15 11:49:05
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 61 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 246 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 17 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 18 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 19 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 58 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 23 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 51 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_all.txt: 55 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1278 candidates in 1 file(s)
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /all.txt: 55 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 61 trackers
  [PASS] Plain text: /adysec_best.txt: 246 trackers
  [PASS] Plain text: /gonghailink_best.txt: 17 trackers
  [PASS] Plain text: /pandamen_best.txt: 18 trackers
  [PASS] Plain text: /gspu_best.txt: 19 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 15 trackers
  [PASS] Plain text: /pexcn_best.txt: 58 trackers
  [PASS] Plain text: /opentracker.txt: 23 trackers
  [PASS] Plain text: /run_ws.txt: 51 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 80 trackers
  [PASS] Plain text: /http.txt: 100 trackers
  [PASS] Plain text: /https.txt: 19 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset-of-all check: all 25 best trackers present in all (55)
  [PASS] Reserve pool check: 9 candidates, disjoint
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
  [WARN] Source freshness: linuxjin-best unchanged 7d
  [WARN] Source freshness: ngosang-i2p unchanged 7d
  [WARN] Source freshness: ngosang-yggdrasil unchanged 7d
------------------------------------------------------------
  Result: 75 passed, 3 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 1 rounds completed
   Total PASS: 75
   Total WARN: 3
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################

============================================================
 Round 1 - 2026-10-15 11:49:13
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 61 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 246 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 17 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 18 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 19 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 58 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 23 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 51 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_all.txt: 55 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1278 candidates in 1 file(s)
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /all.txt: 55 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 61 trackers
  [PASS] Plain text: /adysec_best.txt: 246 trackers
  [PASS] Plain text: /gonghailink_best.txt: 17 trackers
  [PASS] Plain text: /pandamen_best.txt: 18 trackers
  [PASS] Plain text: /gspu_best.txt: 19 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 15 trackers
  [PASS] Plain text: /pexcn_best.txt: 58 trackers
  [PASS] Plain text: /opentracker.txt: 23 trackers
  [PASS] Plain text: /run_ws.txt: 51 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 80 trackers
  [PASS] Plain text: /http.txt: 100 trackers
  [PASS] Plain text: /https.txt: 19 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset-of-all check: all 25 best trackers present in all (55)
  [PASS] Reserve pool check: 9 candidates, disjoint
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
  [PASS] Worker all 短链: HTTP 200, 55 trackers
  [PASS] Worker best 加速: HTTP 200, 25 trackers
  [PASS] Worker all 加速: HTTP 200, 52 trackers
  [WARN] Source freshness: linuxjin-best unchanged 7d
  [WARN] Source freshness: ngosang-i2p unchanged 7d
  [WARN] Source freshness: ngosang-yggdrasil unchanged 7d
------------------------------------------------------------
  Result: 85 passed, 3 warnings, 0 failed
============================================================

============================================================
 Round 2 - 2026-10-15 11:49:19
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 61 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 246 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 17 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 18 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 19 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 58 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 23 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 51 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_all.txt: 55 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1278 candidates in 1 file(s)
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /all.txt: 55 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 61 trackers
  [PASS] Plain text: /adysec_best.txt: 246 trackers
  [PASS] Plain text: /gonghailink_best.txt: 17 trackers
  [PASS] Plain text: /pandamen_best.txt: 18 trackers
  [PASS] Plain text: /gspu_best.txt: 19 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 15 trackers
  [PASS] Plain text: /pexcn_best.txt: 58 trackers
  [PASS] Plain text: /opentracker.txt: 23 trackers
  [PASS] Plain text: /run_ws.txt: 51 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 80 trackers
  [PASS] Plain text: /http.txt: 100 trackers
  [PASS] Plain text: /https.txt: 19 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset-of-all check: all 25 best trackers present in all (55)
  [PASS] Reserve pool check: 9 candidates, disjoint
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
  [PASS] Worker all 短链: HTTP 200, 55 trackers
  [PASS] Worker best 加速: HTTP 200, 25 trackers
  [PASS] Worker all 加速: HTTP 200, 52 trackers
  [WARN] Source freshness: linuxjin-best unchanged 7d
  [WARN] Source freshness: ngosang-i2p unchanged 7d
  [WARN] Source freshness: ngosang-yggdrasil unchanged 7d
------------------------------------------------------------
  Result: 85 passed, 3 warnings, 0 failed
============================================================

============================================================
 Round 3 - 2026-10-15 11:49:28
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 61 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 246 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 17 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 18 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 19 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 58 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 23 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 51 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_all.txt: 55 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1278 candidates in 1 file(s)
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /all.txt: 55 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 61 trackers
  [PASS] Plain text: /adysec_best.txt: 246 trackers
  [PASS] Plain text: /gonghailink_best.txt: 17 trackers
  [PASS] Plain text: /pandamen_best.txt: 18 trackers
  [PASS] Plain text: /gspu_best.txt: 19 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 15 trackers
  [PASS] Plain text: /pexcn_best.txt: 58 trackers
  [PASS] Plain text: /opentracker.txt: 23 trackers
  [PASS] Plain text: /run_ws.txt: 51 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 80 trackers
  [PASS] Plain text: /http.txt: 100 trackers
  [PASS] Plain text: /https.txt: 19 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset-of-all check: all 25 best trackers present in all (55)
  [PASS] Reserve pool check: 9 candidates, disjoint
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
  [PASS] Worker all 短链: HTTP 200, 55 trackers
  [PASS] Worker best 加速: HTTP 200, 25 trackers
  [PASS] Worker all 加速: HTTP 200, 52 trackers
  [WARN] Source freshness: linuxjin-best unchanged 7d
  [WARN] Source freshness: ngosang-i2p unchanged 7d
  [WARN] Source freshness: ngosang-yggdrasil unchanged 7d
------------------------------------------------------------
  Result: 85 passed, 3 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 3 rounds completed
   Total PASS: 255
   Total WARN: 9
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################
=== End of diagnostics (Thu Oct 15 11:49:28 UTC 2026) ===
