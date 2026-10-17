=== Diagnostics Sat Oct 17 04:10:35 UTC 2026 ===
Python: Python 3.12.15
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt
  HTTP 200, total 0.037615s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ip.txt
  HTTP 200, total 0.088292s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_yggdrasil_ip.txt
  HTTP 200, total 0.125767s
>>> https://cf.trackerslist.com/all.txt
  HTTP 200, total 0.128614s
>>> https://tracker.adysec.com/trackers_all.txt
  HTTP 200, total 0.228068s
>>> https://raw.githubusercontent.com/kris3713/UltimateBTTrackersList/refs/heads/master/ultimate_trackers.txt
  HTTP 200, total 0.111046s
>>> https://raw.githubusercontent.com/entr0pia/TrackersListCollection-S/refs/heads/master/https.txt
  HTTP 200, total 0.111471s
[INFO] public list https://cf.trackerslist.com/all.txt: 122 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all.txt: 72 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ip.txt: 53 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_udp.txt: 45 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_http.txt: 17 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_https.txt: 10 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ws.txt: 3 urls
[WARN] github topic search failed (bt-tracker): HTTP Error 403: rate limit exceeded
[WARN] github topic search failed (public-tracker): HTTP Error 403: rate limit exceeded
[WARN] github topic search failed (tracker-list): HTTP Error 403: rate limit exceeded
[OK]   75 new candidates -> candidates_20261017.txt
[OK]   75 new candidates
[ERROR] No valid trackers found in response
[INFO] Repo: Pmwiu/Tracker-List, Max: 59
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/ngosang/trackerslist/master/blacklist.txt (391 URLs)
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/blacklist.txt (20 URLs)
[INFO] URL blacklist: 389 URLs (dynamic + remote sources)
[INFO] Protected hosts (防误杀): 14
[INFO] discovered candidates: 59 URLs in 1 file(s)

[INFO] trackers_ngosang_all.txt (ngosang-all)
[OK]   75 unique

[INFO] trackers_ngosang_all_ip.txt (ngosang-all-ip)
[OK]   51 unique

[INFO] trackers_ngosang_yggdrasil_ip.txt (ngosang-yggdrasil-ip)
  [INFO] Skipped 4 invalid lines

[INFO] trackers_cf_all.txt (cf-all)
  [INFO] Skipped 2 invalid lines
  [INFO] Skipped 16 dynamic-blacklisted lines
[OK]   106 unique

[INFO] trackers_adysec_all.txt (adysec-all)
  [INFO] Skipped 6 invalid lines
  [INFO] Skipped 258 dynamic-blacklisted lines
[OK]   3285 unique

[INFO] trackers_kris3713_ultimate.txt (kris3713-ultimate)
  [INFO] Skipped 2 invalid lines
  [INFO] Skipped 16 dynamic-blacklisted lines
[OK]   162 unique

[INFO] trackers_entr0pia_https.txt (entr0pia-https)
  [INFO] Skipped 3 dynamic-blacklisted lines
[OK]   16 unique

[WARN] 1 source(s) failed:
  - ngosang-yggdrasil-ip: No valid trackers found in response

[INFO] all 合并贡献: ngosang-all=47, ngosang-all-ip=44, ngosang-yggdrasil-ip=0, cf-all=15, adysec-all=43, kris3713-ultimate=5, entr0pia-https=2
[INFO] all 协议分布: http=81, https=18, udp=100, wss=1, ws=0

[OK]   merged: 200
[OK]   source_counts.json (200)
[OK]   discovered_set.json (59)

===== Summary =====
  trackers_ngosang_all.txt: 75
  trackers_ngosang_all_ip.txt: 51
  trackers_cf_all.txt: 106
  trackers_adysec_all.txt: 3285
  trackers_kris3713_ultimate.txt: 162
  trackers_entr0pia_https.txt: 16
  trackers_merged.txt: 200
  FAILED SOURCES: 1
===================
[INFO] discovery: +15 discovered candidates for liveness test (rotation, cap 120)
[INFO] Testing 215 candidates (all-pool=200, timeout=10s, workers=30)
  [ALIVE] (2/215) http://004430.xyz:80/announce 27ms — announce with peers:1
  [ALIVE] (9/215) http://107.189.2.131:1337/announce 287ms — announce with peers:1
  [ALIVE] (20/215) http://140.235.237.23:6969/announce 139ms — announce with peers:1
  [ALIVE] (21/215) http://138.186.10.167:1337/announce 270ms — announce with peers:1
  [ALIVE] (22/215) http://185.126.65.92:6969/announce 263ms — announce without peers
  [ALIVE] (23/215) http://207.241.226.111:6969/announce 35ms — announce with peers:1
  [ALIVE] (24/215) http://207.241.231.226:6969/announce 42ms — announce with peers:1
  [ALIVE] (25/215) http://211.75.205.187:80/announce 373ms — announce with peers:1
  [ALIVE] (26/215) http://211.75.205.187:6969/announce 384ms — announce with peers:1
  [ALIVE] (27/215) http://1337.abcvg.info:80/announce 255ms — announce with peers:1
  [ALIVE] (28/215) http://211.75.210.221:80/announce 384ms — announce with peers:1
  [ALIVE] (29/215) http://211.75.205.188:6969/announce 391ms — announce with peers:1
  [ALIVE] (30/215) http://216.144.239.90:6969/announce 69ms — announce with peers:1
  [ALIVE] (31/215) http://43.250.54.126:6969/announce 261ms — announce with peers:1
  [ALIVE] (32/215) http://93.158.213.92:1337/announce 262ms — announce with peers:1
  [ALIVE] (33/215) http://94.23.207.177:6969/announce 288ms — announce with peers:1
  [ALIVE] (34/215) http://announce.sktorrent.eu:6969/announce 321ms — announce with peers:1
  [ALIVE] (35/215) http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 284ms — announce with peers:1
  [ALIVE] (36/215) http://ipv4announce.sktorrent.eu:6969/announce 287ms — announce with peers:1
  [ALIVE] (37/215) http://retracker01-msk-virt.corbina.net:80/announce 608ms — announce with peers:1
  [ALIVE] (38/215) http://open.tracker.cl:1337/announce 273ms — announce with peers:1
  [ALIVE] (39/215) http://tr.nyacat.pw:80/announce 177ms — announce without peers
  [ALIVE] (40/215) http://t.overflow.biz:6969/announce 374ms — announce with peers:1
  [DEAD]  (50/215) http://106.14.254.164:6969/announce — URLError: <urlopen error timed out>
  [ALIVE] (56/215) https://004430.xyz:443/announce 41ms — announce with peers:1
  [ALIVE] (58/215) https://t.213891.xyz:443/announce 40ms — announce without peers
  [ALIVE] (62/215) https://open.ftorrent.com:443/announce 111ms — announce without peers
  [ALIVE] (65/215) http://tracker.dhitechnical.com:6969/announce 206ms — announce with peers:1
  [ALIVE] (69/215) https://1.tracker.eu.org:443/announce 45ms — announce without peers
  [ALIVE] (70/215) https://tr.nyacat.pw:443/announce 194ms — announce without peers
  [ALIVE] (71/215) http://tracker.renfei.net:8080/announce 177ms — announce with peers:1
  [ALIVE] (74/215) https://tracker.7471.top:443/announce 188ms — announce without peers
  [ALIVE] (75/215) udp://149.106.106.25:443/announce 35ms — valid connect + announce (v4)
  [ALIVE] (76/215) http://tracker.qu.ax:6969/announce 260ms — announce with peers:1
  [ALIVE] (77/215) http://tracker.waaa.moe:6969/announce 84ms — announce with peers:1
  [ALIVE] (80/215) https://tracker.foreverpirates.co:443/announce 242ms — announce without peers
  [ALIVE] (82/215) https://tracker.zhuqiy.com:443/announce 130ms — announce with peers:1
  [ALIVE] (83/215) http://tracker.zhuqiy.dgj055.icu:80/announce 319ms — announce without peers
  [ALIVE] (84/215) udp://180.131.145.175:6969/announce 32ms — valid connect + announce (v4)
  [ALIVE] (85/215) udp://109.201.134.183:80/announce 131ms — valid connect + announce (v4)
  [ALIVE] (86/215) http://tracker.dler.com:6969/announce 387ms — announce with peers:1
  [ALIVE] (87/215) udp://164.152.110.70:6969/announce 56ms — valid connect + announce (v4)
  [ALIVE] (88/215) udp://107.189.2.131:1337/announce 143ms — valid connect + announce (v4)
  [ALIVE] (89/215) http://tracker.dler.org:6969/announce 395ms — announce with peers:1
  [ALIVE] (90/215) http://tracker2.dler.org:80/announce 398ms — announce with peers:1
  [ALIVE] (91/215) udp://135.125.198.235:1984/announce 154ms — valid connect + announce (v4)
  [ALIVE] (92/215) udp://209.141.59.25:6969/announce 15ms — valid connect + announce (v4)
  [ALIVE] (93/215) https://tracker.midnightprogrammer.net:443/announce 324ms — announce without peers
  [ALIVE] (94/215) udp://23.94.174.203:1337/announce 8ms — valid connect + announce (v4)
  [ALIVE] (95/215) http://tracker.mywaifu.best:6969/announce 537ms — announce without peers
  [ALIVE] (96/215) udp://151.242.104.187:80/announce 142ms — valid connect + announce (v4)
  [ALIVE] (97/215) udp://192.99.100.68:6969/announce 70ms — valid connect + announce (v4)
  [ALIVE] (98/215) https://tracker.nekomi.cn:443/announce 43ms — announce with peers:1
  [ALIVE] (99/215) udp://15.235.207.99:8081/announce 179ms — valid connect + announce (v4)
  [ALIVE] (100/215) udp://160.30.240.158:1337/announce 143ms — valid connect + announce (v4)
  [ALIVE] (101/215) udp://178.239.19.29:80/announce 133ms — valid connect + announce (v4)
  [ALIVE] (102/215) http://tracker.opentrackr.org:1337/announce 402ms — announce with peers:1
  [ALIVE] (103/215) udp://34.66.57.33:1337/announce 52ms — valid connect + announce (v4)
  [ALIVE] (104/215) udp://185.216.179.62:25/announce 138ms — valid connect + announce (v4)
  [ALIVE] (105/215) udp://34.66.57.33:80/announce 53ms — valid connect + announce (v4)
  [ALIVE] (106/215) udp://185.121.168.96:1337/announce 150ms — valid connect + announce (v4)
  [ALIVE] (107/215) udp://193.187.90.12:6969/announce 148ms — valid connect + announce (v4)
  [ALIVE] (108/215) udp://51.222.82.36:6969/announce 71ms — valid connect + announce (v4)
  [ALIVE] (109/215) udp://212.42.38.197:6969/announce 170ms — valid connect + announce (v4)
  [ALIVE] (110/215) udp://31.56.179.159:6969/announce 151ms — valid connect + announce (v4)
  [ALIVE] (111/215) udp://211.75.205.187:6969/announce 187ms — valid connect + announce (v4)
  [ALIVE] (112/215) udp://211.75.210.221:80/announce 186ms — valid connect + announce (v4)
  [ALIVE] (113/215) udp://211.75.205.187:80/announce 195ms — valid connect + announce (v4)
  [ALIVE] (114/215) udp://211.75.205.188:6969/announce 194ms — valid connect + announce (v4)
  [ALIVE] (115/215) udp://43.250.54.126:6969/announce 129ms — valid connect + announce (v4)
  [ALIVE] (117/215) udp://38.180.157.12:2715/announce 151ms — valid connect + announce (v4)
  [ALIVE] (118/215) udp://45.137.199.107:6969/announce 140ms — valid connect + announce (v4)
  [ALIVE] (119/215) udp://74.119.149.136:6969/announce 50ms — valid connect + announce (v4)
  [ALIVE] (120/215) udp://45.38.170.167:6969/announce 158ms — valid connect + announce (v4)
  [ALIVE] (121/215) udp://52.58.128.163:6969/announce 138ms — valid connect + announce (v4)
  [ALIVE] (122/215) udp://47.76.201.250:6969/announce 153ms — valid connect + announce (v4)
  [ALIVE] (123/215) udp://74.81.245.60:2010/announce 79ms — valid connect + announce (v4)
  [ALIVE] (125/215) udp://65.109.28.17:6969/announce 158ms — valid connect + announce (v4)
  [ALIVE] (126/215) udp://65.109.28.33:6969/announce 159ms — valid connect + announce (v4)
  [ALIVE] (127/215) udp://89.234.156.205:451/announce 135ms — valid connect + announce (v4)
  [ALIVE] (128/215) udp://60.172.236.18:6969/announce 223ms — valid connect + announce (v4)
  [ALIVE] (129/215) udp://93.158.213.92:1337/announce 132ms — valid connect + announce (v4)
  [ALIVE] (130/215) udp://93.158.213.92:6969/announce 131ms — valid connect + announce (v4)
  [ALIVE] (131/215) udp://94.23.207.177:6969/announce 142ms — valid connect + announce (v4)
  [ALIVE] (132/215) udp://95.217.80.20:6969/announce 159ms — valid connect + announce (v4)
  [ALIVE] (133/215) udp://83.102.180.21:80/announce 176ms — valid connect + announce (v4)
  [ALIVE] (134/215) udp://evan.im:6969/announce 50ms — valid connect + announce (v4)
  [ALIVE] (135/215) udp://95.217.80.22:6969/announce 158ms — valid connect + announce (v4)
  [ALIVE] (136/215) udp://open.ftorrent.com:443/announce 36ms — valid connect + announce (v4)
  [ALIVE] (137/215) udp://ipv4announce.sktorrent.eu:6969/announce 143ms — valid connect + announce (v4)
  [ALIVE] (138/215) udp://admin.52ywp.com:6969/announce 217ms — valid connect + announce (v4)
  [ALIVE] (140/215) udp://bt-tracker.de:6969/announce 123ms — valid connect + announce (v4)
  [ALIVE] (141/215) udp://martin-gebhardt.eu:25/announce 136ms — valid connect + announce (v4)
  [ALIVE] (142/215) udp://explodie.org:6969/announce 121ms — valid connect + announce (v4)
  [ALIVE] (143/215) udp://open.demonii.com:1337/announce 149ms — valid connect + announce (v4)
  [ALIVE] (144/215) udp://kolankoalastree.newtrackon.co.nz:1337/announce 161ms — valid connect + announce (v4)
  [ALIVE] (145/215) udp://mail.segso.net:6969/announce 162ms — valid connect + announce (v4)
  [ALIVE] (146/215) udp://open.stealth.si:80/announce 142ms — valid connect + announce (v4)
  [ALIVE] (147/215) udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 351ms — valid connect + announce (v4)
  [ALIVE] (148/215) udp://seedpeer.net:6969/announce 32ms — valid connect + announce (v4)
  [ALIVE] (149/215) udp://tracker.004430.xyz:1337/announce 8ms — valid connect + announce (v4)
  [ALIVE] (150/215) udp://tr.btube3.com:2010/announce 63ms — valid connect + announce (v4)
  [ALIVE] (151/215) udp://tracker.bittor.pw:1337/announce 50ms — valid connect + announce (v4)
  [ALIVE] (152/215) udp://ns575949.ip-51-222-82.net:6969/announce 70ms — valid connect + announce (v4)
  [ALIVE] (153/215) udp://tr4ck3r.duckdns.org:6969/announce 74ms — valid connect + announce (v4)
  [ALIVE] (156/215) udp://retracker01-msk-virt.corbina.net:80/announce 177ms — valid connect + announce (v4)
  [ALIVE] (157/215) udp://t.overflow.biz:6969/announce 154ms — valid connect + announce (v4)
  [ALIVE] (158/215) udp://tracker-udp.gbitt.info:80/announce 131ms — valid connect + announce (v4)
  [ALIVE] (159/215) udp://tr3.ysagin.top:2715/announce 159ms — valid connect + announce (v4)
  [ALIVE] (160/215) udp://opentracker.lain.moscow:6969/announce 142ms — valid connect + announce (v4)
  [ALIVE] (161/215) udp://tracker.cn.nyaa.net:6969/announce 152ms — valid connect + announce (v4)
  [ALIVE] (162/215) udp://tracker.corpscorp.online:80/announce 52ms — valid connect + announce (v4)
  [ALIVE] (163/215) udp://tracker.ddunlimited.net:6969/announce 148ms — valid connect + announce (v4)
  [ALIVE] (164/215) udp://tracker.dler.org:6969/announce 186ms — valid connect + announce (v4)
  [ALIVE] (165/215) udp://tracker.farted.net:6969/announce 154ms — valid connect + announce (v4)
  [ALIVE] (166/215) udp://tracker.gmi.gd:6969/announce 13ms — valid connect + announce (v4)
  [ALIVE] (168/215) udp://tracker.aruku.ovh:8081/announce 180ms — valid connect + announce (v4)
  [ALIVE] (169/215) udp://tracker.okade.pro:1337/announce 139ms — valid connect + announce (v4)
  [ALIVE] (170/215) udp://tracker.nyaa.vc:6969/announce 140ms — valid connect + announce (v4)
  [ALIVE] (171/215) udp://tracker.ducks.party:1984/announce 144ms — valid connect + announce (v4)
  [ALIVE] (172/215) udp://tracker.opentrackr.org:1337/announce 131ms — valid connect + announce (v4)
  [ALIVE] (175/215) udp://tracker.k.vu:6969/announce 158ms — valid connect + announce (v4)
  [ALIVE] (176/215) udp://tracker.opentrackr.com:6969/announce 162ms — valid connect + announce (v4)
  [ALIVE] (177/215) udp://tracker.ilibr.org:6969/announce 162ms — valid connect + announce (v4)
  [ALIVE] (178/215) udp://tracker.qu.ax:6969/announce 130ms — valid connect + announce (v4)
  [ALIVE] (180/215) udp://tracker.wildkat.net:6969/announce 55ms — valid connect + announce (v4)
  [ALIVE] (182/215) udp://tracker.peerfect.org:6969/announce 162ms — valid connect + announce (v4)
  [ALIVE] (183/215) udp://tracker.skynetcloud.site:6969/announce 129ms — valid connect + announce (v4)
  [ALIVE] (185/215) udp://tracker.willy.pro:6969/announce 228ms — valid connect + announce (v4)
  [ALIVE] (186/215) udp://tracker2.dler.org:80/announce 188ms — valid connect + announce (v4)
  [ALIVE] (188/215) udp://tracker.torrents.observer:80/announce 133ms — valid connect + announce (v4)
  [ALIVE] (189/215) udp://v2.iperson.xyz:6969/announce 197ms — valid connect + announce (v4)
  [ALIVE] (190/215) udp://tracker.tryhackx.org:6969/announce 155ms — valid connect + announce (v4)
  [ALIVE] (191/215) udp://tracker.playground.ru:6969/announce 170ms — valid connect + announce (v4)
  [ALIVE] (195/215) udp://exodus.desync.com:6969/announce 24ms — valid connect + announce (v4)
  [ALIVE] (196/215) udp://tracker.fnix.net:6969/announce 153ms — valid connect + announce (v4)
  [DEAD]  (200/215) udp://159.146.99.45:6969/announce — no connect response

[INFO] First pass done in 30.3s
[INFO] Multi-sample: 3 samples on top 50 alive trackers...
[INFO] Multi-sample refined 48 trackers (median + jitter penalty)
[INFO] Same-subnet(/24) dedup removed 70 slower tracker(s)
[INFO] scrape probe: 18 http/https alive trackers
[INFO] scrape: 4 responded, 2 with seeders
[INFO] discovered candidates excluded from all: 59

===== Test Summary =====
  Total tested:   215
  Alive (raw):    65
  All (final):    45 (top 59 by composite score)
  Unsafe filtered:0
  Low-speed:      0 (>5s excluded)
  Same-subnet dedup:  70 (kept faster)
  Dead final:     150
  Time:           39.2s
=== 协议分布统计 ===
  HTTP  : 33 个
  HTTPS : 10 个
  UDP   : 92 个
  WSS   : 0 个
  WS    : 0 个
  总计: 135 个（存活）
=========================

============================================================
 Round 1 - 2026-10-17 04:11:20
============================================================
  [PASS] Local tracker: trackers_ngosang_all.txt: 75 trackers
  [PASS] Local tracker: trackers_ngosang_all_ip.txt: 51 trackers
  [FAIL] Local tracker: trackers_ngosang_yggdrasil_ip.txt: missing
  [PASS] Local tracker: trackers_cf_all.txt: 106 trackers
  [PASS] Local tracker: trackers_adysec_all.txt: 3285 trackers
  [PASS] Local tracker: trackers_kris3713_ultimate.txt: 162 trackers
  [PASS] Local tracker: trackers_entr0pia_https.txt: 16 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_all.txt: 45 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Discovery output: 75 candidates in 1 file(s)
  [PASS] Merged dedup check: 200 unique
  [PASS] URL format check: all 200 valid
------------------------------------------------------------
  Result: 14 passed, 0 warnings, 1 failed
============================================================

############################################################
 FINAL REPORT: 1 rounds completed
   Total PASS: 14
   Total WARN: 0
   Total FAIL: 1
   STATUS: ISSUES DETECTED
############################################################

============================================================
 Round 1 - 2026-10-17 04:11:27
============================================================
  [PASS] Local tracker: trackers_ngosang_all.txt: 75 trackers
  [PASS] Local tracker: trackers_ngosang_all_ip.txt: 51 trackers
  [FAIL] Local tracker: trackers_ngosang_yggdrasil_ip.txt: missing
  [PASS] Local tracker: trackers_cf_all.txt: 106 trackers
  [PASS] Local tracker: trackers_adysec_all.txt: 3285 trackers
  [PASS] Local tracker: trackers_kris3713_ultimate.txt: 162 trackers
  [PASS] Local tracker: trackers_entr0pia_https.txt: 16 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_all.txt: 45 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Discovery output: 75 candidates in 1 file(s)
  [PASS] Merged dedup check: 200 unique
  [PASS] URL format check: all 200 valid
------------------------------------------------------------
  Result: 14 passed, 0 warnings, 1 failed
============================================================

============================================================
 Round 2 - 2026-10-17 04:11:32
============================================================
  [PASS] Local tracker: trackers_ngosang_all.txt: 75 trackers
  [PASS] Local tracker: trackers_ngosang_all_ip.txt: 51 trackers
  [FAIL] Local tracker: trackers_ngosang_yggdrasil_ip.txt: missing
  [PASS] Local tracker: trackers_cf_all.txt: 106 trackers
  [PASS] Local tracker: trackers_adysec_all.txt: 3285 trackers
  [PASS] Local tracker: trackers_kris3713_ultimate.txt: 162 trackers
  [PASS] Local tracker: trackers_entr0pia_https.txt: 16 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_all.txt: 45 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Discovery output: 75 candidates in 1 file(s)
  [PASS] Merged dedup check: 200 unique
  [PASS] URL format check: all 200 valid
------------------------------------------------------------
  Result: 14 passed, 0 warnings, 1 failed
============================================================

============================================================
 Round 3 - 2026-10-17 04:11:37
============================================================
  [PASS] Local tracker: trackers_ngosang_all.txt: 75 trackers
  [PASS] Local tracker: trackers_ngosang_all_ip.txt: 51 trackers
  [FAIL] Local tracker: trackers_ngosang_yggdrasil_ip.txt: missing
  [PASS] Local tracker: trackers_cf_all.txt: 106 trackers
  [PASS] Local tracker: trackers_adysec_all.txt: 3285 trackers
  [PASS] Local tracker: trackers_kris3713_ultimate.txt: 162 trackers
  [PASS] Local tracker: trackers_entr0pia_https.txt: 16 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_all.txt: 45 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Discovery output: 75 candidates in 1 file(s)
  [PASS] Merged dedup check: 200 unique
  [PASS] URL format check: all 200 valid
------------------------------------------------------------
  Result: 14 passed, 0 warnings, 1 failed
============================================================

############################################################
 FINAL REPORT: 3 rounds completed
   Total PASS: 42
   Total WARN: 0
   Total FAIL: 3
   STATUS: ISSUES DETECTED
############################################################
=== End of diagnostics (Sat Oct 17 04:11:37 UTC 2026) ===
