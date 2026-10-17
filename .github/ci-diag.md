=== Diagnostics Sat Oct 17 15:45:25 UTC 2026 ===
Python: Python 3.12.15
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt
  HTTP 200, total 0.064423s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ip.txt
  HTTP 200, total 0.027127s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_yggdrasil_ip.txt
  HTTP 200, total 0.064844s
>>> https://cf.trackerslist.com/all.txt
  HTTP 200, total 0.089325s
>>> https://tracker.adysec.com/trackers_all.txt
  HTTP 200, total 0.134630s
>>> https://raw.githubusercontent.com/kris3713/UltimateBTTrackersList/refs/heads/master/ultimate_trackers.txt
  HTTP 200, total 0.069997s
>>> https://raw.githubusercontent.com/entr0pia/TrackersListCollection-S/refs/heads/master/https.txt
  HTTP 200, total 0.107335s
[INFO] public list https://cf.trackerslist.com/all.txt: 122 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all.txt: 75 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ip.txt: 51 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_udp.txt: 48 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_http.txt: 17 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_https.txt: 10 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ws.txt: 3 urls
[OK]   1291 new candidates -> candidates_20261017.txt
[OK]   1291 new candidates
[ERROR] No valid trackers found in response
[INFO] Repo: Pmwiu/Tracker-List, Max: 59
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/ngosang/trackerslist/master/blacklist.txt (391 URLs)
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/blacklist.txt (20 URLs)
[INFO] URL blacklist: 389 URLs (dynamic + remote sources)
[INFO] Protected hosts (防误杀): 99
[INFO] discovered candidates: 1073 URLs in 1 file(s)

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
[INFO] all 协议分布: http=124, https=18, udp=57, wss=1, ws=0

[OK]   merged: 200
[OK]   source_counts.json (200)
[OK]   discovered_set.json (1073)

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
[INFO] discovery: +120 discovered candidates for liveness test (rotation, cap 120)
[INFO] Testing 320 candidates (all-pool=200, timeout=10s, workers=30)
  [ALIVE] (5/320) http://004430.xyz:80/announce 145ms — announce with peers:1
  [ALIVE] (6/320) http://107.189.2.131:1337/announce 195ms — announce with peers:1
  [DEAD]  (25/320) http://107.150.14.110:6969/announce — URLError: <urlopen error timed out>
  [ALIVE] (40/320) http://138.186.10.167:1337/announce 236ms — announce with peers:1
  [ALIVE] (49/320) http://1337.abcvg.info:80/announce 424ms — announce with peers:1
  [DEAD]  (50/320) http://167.235.245.209:80/announce — HTTPError: HTTP Error 404: Not Found
  [ALIVE] (61/320) http://140.235.237.23:6969/announce 2644ms — announce with peers:1
  [ALIVE] (64/320) http://185.126.65.92:6969/announce 167ms — announce without peers
  [DEAD]  (75/320) http://141.144.224.250:6969/announce — URLError: <urlopen error timed out>
  [ALIVE] (77/320) http://207.241.231.226:6969/announce 131ms — announce with peers:1
  [ALIVE] (78/320) http://207.241.226.111:6969/announce 131ms — announce with peers:1
  [ALIVE] (79/320) http://216.144.239.90:6969/announce 140ms — announce with peers:1
  [ALIVE] (81/320) http://43.250.54.126:6969/announce 165ms — announce with peers:1
  [ALIVE] (82/320) http://93.158.213.92:1337/announce 166ms — announce with peers:1
  [ALIVE] (83/320) http://94.23.207.177:6969/announce 169ms — announce with peers:1
  [ALIVE] (86/320) http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 196ms — announce with peers:1
  [ALIVE] (91/320) http://ipv4announce.sktorrent.eu:6969/announce 173ms — announce with peers:1
  [ALIVE] (92/320) http://211.75.205.187:6969/announce 380ms — announce with peers:1
  [ALIVE] (93/320) http://211.75.205.187:80/announce 379ms — announce with peers:1
  [ALIVE] (94/320) http://211.75.205.188:6969/announce 378ms — announce with peers:1
  [ALIVE] (96/320) http://tr.nyacat.pw:80/announce 220ms — announce without peers
  [ALIVE] (97/320) http://announce.sktorrent.eu:6969/announce 178ms — announce with peers:1
  [ALIVE] (98/320) http://t.overflow.biz:6969/announce 250ms — announce with peers:1
  [ALIVE] (99/320) http://tracker.mywaifu.best:6969/announce 179ms — announce without peers
  [DEAD]  (100/320) http://167.253.78.20:8080/announce — URLError: <urlopen error timed out>
  [ALIVE] (102/320) https://t.213891.xyz:443/announce 24ms — announce without peers
  [ALIVE] (103/320) https://004430.xyz:443/announce 172ms — announce with peers:1
  [ALIVE] (105/320) http://tracker.renfei.net:8080/announce 57ms — announce with peers:1
  [ALIVE] (106/320) http://tracker.zhuqiy.dgj055.icu:80/announce 229ms — announce without peers
  [ALIVE] (107/320) http://tracker.qu.ax:6969/announce 165ms — announce with peers:1
  [ALIVE] (109/320) https://1.tracker.eu.org:443/announce 52ms — announce without peers
  [ALIVE] (110/320) http://tracker.waaa.moe:6969/announce 157ms — announce with peers:1
  [ALIVE] (111/320) https://tracker.7471.top:443/announce 129ms — announce without peers
  [ALIVE] (112/320) https://open.ftorrent.com:443/announce 171ms — announce without peers
  [ALIVE] (114/320) http://open.tracker.cl:1337/announce 253ms — announce with peers:1
  [ALIVE] (116/320) http://retracker01-msk-virt.corbina.net:80/announce 449ms — announce with peers:1
  [ALIVE] (117/320) https://tr.nyacat.pw:443/announce 228ms — announce without peers
  [ALIVE] (119/320) udp://149.106.106.25:443/announce 52ms — valid connect + announce (v4)
  [ALIVE] (120/320) http://tracker.dler.org:6969/announce 555ms — announce with peers:1
  [ALIVE] (121/320) udp://109.201.134.183:80/announce 89ms — valid connect + announce (v4)
  [ALIVE] (122/320) udp://135.125.198.235:1984/announce 90ms — valid connect + announce (v4)
  [ALIVE] (123/320) udp://164.152.110.70:6969/announce 17ms — valid connect + announce (v4)
  [ALIVE] (124/320) http://tracker.opentrackr.org:1337/announce 415ms — announce with peers:1
  [ALIVE] (125/320) udp://151.242.104.187:80/announce 92ms — valid connect + announce (v4)
  [ALIVE] (127/320) https://tracker.foreverpirates.co:443/announce 396ms — announce without peers
  [ALIVE] (128/320) udp://107.189.2.131:1337/announce 218ms — valid connect + announce (v4)
  [ALIVE] (129/320) http://tracker.dler.com:6969/announce 542ms — announce with peers:1
  [ALIVE] (130/320) http://tracker2.dler.org:80/announce 530ms — announce with peers:1
  [ALIVE] (131/320) udp://192.99.100.68:6969/announce 14ms — valid connect + announce (v4)
  [ALIVE] (133/320) udp://180.131.145.175:6969/announce 67ms — valid connect + announce (v4)
  [ALIVE] (134/320) udp://178.239.19.29:80/announce 87ms — valid connect + announce (v4)
  [ALIVE] (135/320) https://tracker.zhuqiy.com:443/announce 95ms — announce with peers:1
  [ALIVE] (136/320) udp://34.66.57.33:1337/announce 26ms — valid connect + announce (v4)
  [ALIVE] (137/320) udp://34.66.57.33:80/announce 30ms — valid connect + announce (v4)
  [ALIVE] (138/320) udp://185.216.179.62:25/announce 95ms — valid connect + announce (v4)
  [ALIVE] (139/320) udp://23.94.174.203:1337/announce 63ms — valid connect + announce (v4)
  [ALIVE] (140/320) udp://15.235.207.99:8081/announce 227ms — valid connect + announce (v4)
  [ALIVE] (141/320) udp://193.187.90.12:6969/announce 102ms — valid connect + announce (v4)
  [ALIVE] (142/320) udp://51.222.82.36:6969/announce 15ms — valid connect + announce (v4)
  [ALIVE] (143/320) udp://23.157.120.14:6969/announce 103ms — valid connect + announce (v4)
  [ALIVE] (144/320) udp://160.30.240.158:1337/announce 199ms — valid connect + announce (v4)
  [ALIVE] (145/320) udp://212.42.38.197:6969/announce 139ms — valid connect + announce (v4)
  [ALIVE] (146/320) udp://185.121.168.96:1337/announce 186ms — valid connect + announce (v4)
  [ALIVE] (147/320) udp://74.119.149.136:6969/announce 2ms — valid connect + announce (v4)
  [ALIVE] (148/320) udp://43.250.54.126:6969/announce 84ms — valid connect + announce (v4)
  [ALIVE] (149/320) https://tracker.nekomi.cn:443/announce 158ms — announce with peers:1
  [ALIVE] (150/320) udp://45.38.170.167:6969/announce 103ms — valid connect + announce (v4)
  [ALIVE] (151/320) udp://211.75.205.187:6969/announce 190ms — valid connect + announce (v4)
  [ALIVE] (152/320) udp://211.75.205.187:80/announce 189ms — valid connect + announce (v4)
  [ALIVE] (154/320) udp://74.81.245.60:2010/announce 95ms — valid connect + announce (v4)
  [ALIVE] (155/320) udp://93.158.213.92:6969/announce 83ms — valid connect + announce (v4)
  [ALIVE] (156/320) udp://65.109.28.17:6969/announce 115ms — valid connect + announce (v4)
  [ALIVE] (157/320) udp://65.109.28.33:6969/announce 113ms — valid connect + announce (v4)
  [ALIVE] (158/320) udp://evan.im:6969/announce 1ms — valid connect + announce (v4)
  [ALIVE] (159/320) udp://47.76.201.250:6969/announce 199ms — valid connect + announce (v4)
  [ALIVE] (160/320) http://tracker.dhitechnical.com:6969/announce 1438ms — announce with peers:1
  [ALIVE] (161/320) udp://ns575949.ip-51-222-82.net:6969/announce 15ms — valid connect + announce (v4)
  [ALIVE] (162/320) udp://ipv4announce.sktorrent.eu:6969/announce 85ms — valid connect + announce (v4)
  [ALIVE] (163/320) udp://60.172.236.18:6969/announce 218ms — valid connect + announce (v4)
  [ALIVE] (165/320) udp://bt-tracker.de:6969/announce 90ms — valid connect + announce (v4)
  [ALIVE] (166/320) udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 230ms — valid connect + announce (v4)
  [ALIVE] (167/320) udp://open.ftorrent.com:443/announce 51ms — valid connect + announce (v4)
  [ALIVE] (168/320) udp://exodus.desync.com:6969/announce 70ms — valid connect + announce (v4)
  [ALIVE] (169/320) udp://mail.segso.net:6969/announce 114ms — valid connect + announce (v4)
  [ALIVE] (170/320) udp://martin-gebhardt.eu:25/announce 90ms — valid connect + announce (v4)
  [ALIVE] (171/320) udp://tr4ck3r.duckdns.org:6969/announce 15ms — valid connect + announce (v4)
  [ALIVE] (172/320) udp://open.stealth.si:80/announce 92ms — valid connect + announce (v4)
  [DEAD]  (175/320) http://171.104.111.201:6969/announce — URLError: <urlopen error timed out>
  [ALIVE] (176/320) udp://seedpeer.net:6969/announce 70ms — valid connect + announce (v4)
  [ALIVE] (177/320) udp://kolankoalastree.newtrackon.co.nz:1337/announce 202ms — valid connect + announce (v4)
  [ALIVE] (178/320) udp://retracker01-msk-virt.corbina.net:80/announce 131ms — valid connect + announce (v4)
  [ALIVE] (179/320) udp://t.overflow.biz:6969/announce 115ms — valid connect + announce (v4)
  [ALIVE] (180/320) udp://tr.btube3.com:2010/announce 75ms — valid connect + announce (v4)
  [ALIVE] (181/320) udp://explodie.org:6969/announce 110ms — valid connect + announce (v4)
  [ALIVE] (182/320) udp://open.demonii.com:1337/announce 206ms — valid connect + announce (v4)
  [ALIVE] (184/320) udp://tr3.ysagin.top:2715/announce 91ms — valid connect + announce (v4)
  [ALIVE] (196/320) https://337hhh.xyz:443/announce 293ms — announce without peers
  [DEAD]  (200/320) https://api.ipv4online.uk:443/announce — URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)>
  [ALIVE] (216/320) udp://admin.52ywp.com:6969/announce 240ms — valid connect + announce (v4)
  [DEAD]  (225/320) https://github.com:443/BiglySoftware/BiglyBT — HTTPError: HTTP Error 400: Bad Request
  [DEAD]  (250/320) https://github.com:443/simeon-vanov/cortiq-public/releases/latest — HTTPError: HTTP Error 400: Bad Request
  [DEAD]  (275/320) https://ngosang.github.io:443/trackerslist/trackers_all_udp.txt — invalid bencoded response
  [DEAD]  (300/320) http://asiatorrent.giize.com:51413/announce — URLError: <urlopen error timed out>

[INFO] First pass done in 42.1s
[INFO] Multi-sample: 3 samples on top 50 alive trackers...
[INFO] Multi-sample refined 47 trackers (median + jitter penalty)
[INFO] Same-subnet(/24) dedup removed 43 slower tracker(s)
[INFO] scrape probe: 17 http/https alive trackers
[INFO] scrape: 2 responded, 1 with seeders
[INFO] discovered candidates excluded from all: 1073

===== Test Summary =====
  Total tested:   320
  Alive (raw):    50
  All (final):    50 (top 59 by composite score)
  Unsafe filtered:3
  Low-speed:      0 (>5s excluded)
  Same-subnet dedup:  43 (kept faster)
  Dead final:     269
  Time:           50.2s
=== 协议分布统计 ===
  HTTP  : 32 个
  HTTPS : 10 个
  UDP   : 51 个
  WSS   : 0 个
  WS    : 0 个
  总计: 93 个（存活）
=========================

============================================================
 Round 1 - 2026-10-17 15:46:23
============================================================
  [PASS] Local tracker: trackers_ngosang_all.txt: 75 trackers
  [PASS] Local tracker: trackers_ngosang_all_ip.txt: 51 trackers
  [FAIL] Local tracker: trackers_ngosang_yggdrasil_ip.txt: missing
  [PASS] Local tracker: trackers_cf_all.txt: 106 trackers
  [PASS] Local tracker: trackers_adysec_all.txt: 3285 trackers
  [PASS] Local tracker: trackers_kris3713_ultimate.txt: 162 trackers
  [PASS] Local tracker: trackers_entr0pia_https.txt: 16 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_all.txt: 50 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Discovery output: 1291 candidates in 1 file(s)
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
 Round 1 - 2026-10-17 15:46:30
============================================================
  [PASS] Local tracker: trackers_ngosang_all.txt: 75 trackers
  [PASS] Local tracker: trackers_ngosang_all_ip.txt: 51 trackers
  [FAIL] Local tracker: trackers_ngosang_yggdrasil_ip.txt: missing
  [PASS] Local tracker: trackers_cf_all.txt: 106 trackers
  [PASS] Local tracker: trackers_adysec_all.txt: 3285 trackers
  [PASS] Local tracker: trackers_kris3713_ultimate.txt: 162 trackers
  [PASS] Local tracker: trackers_entr0pia_https.txt: 16 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_all.txt: 50 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Discovery output: 1291 candidates in 1 file(s)
  [PASS] Merged dedup check: 200 unique
  [PASS] URL format check: all 200 valid
------------------------------------------------------------
  Result: 14 passed, 0 warnings, 1 failed
============================================================

============================================================
 Round 2 - 2026-10-17 15:46:35
============================================================
  [PASS] Local tracker: trackers_ngosang_all.txt: 75 trackers
  [PASS] Local tracker: trackers_ngosang_all_ip.txt: 51 trackers
  [FAIL] Local tracker: trackers_ngosang_yggdrasil_ip.txt: missing
  [PASS] Local tracker: trackers_cf_all.txt: 106 trackers
  [PASS] Local tracker: trackers_adysec_all.txt: 3285 trackers
  [PASS] Local tracker: trackers_kris3713_ultimate.txt: 162 trackers
  [PASS] Local tracker: trackers_entr0pia_https.txt: 16 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_all.txt: 50 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Discovery output: 1291 candidates in 1 file(s)
  [PASS] Merged dedup check: 200 unique
  [PASS] URL format check: all 200 valid
------------------------------------------------------------
  Result: 14 passed, 0 warnings, 1 failed
============================================================

============================================================
 Round 3 - 2026-10-17 15:46:40
============================================================
  [PASS] Local tracker: trackers_ngosang_all.txt: 75 trackers
  [PASS] Local tracker: trackers_ngosang_all_ip.txt: 51 trackers
  [FAIL] Local tracker: trackers_ngosang_yggdrasil_ip.txt: missing
  [PASS] Local tracker: trackers_cf_all.txt: 106 trackers
  [PASS] Local tracker: trackers_adysec_all.txt: 3285 trackers
  [PASS] Local tracker: trackers_kris3713_ultimate.txt: 162 trackers
  [PASS] Local tracker: trackers_entr0pia_https.txt: 16 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_all.txt: 50 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Discovery output: 1291 candidates in 1 file(s)
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
=== End of diagnostics (Sat Oct 17 15:46:40 UTC 2026) ===
