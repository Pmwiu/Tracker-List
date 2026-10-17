=== Diagnostics Sat Oct 17 11:00:11 UTC 2026 ===
Python: Python 3.12.15
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt
  HTTP 200, total 0.027328s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ip.txt
  HTTP 200, total 0.027985s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_yggdrasil_ip.txt
  HTTP 200, total 0.068569s
>>> https://cf.trackerslist.com/all.txt
  HTTP 200, total 0.121788s
>>> https://tracker.adysec.com/trackers_all.txt
  HTTP 200, total 0.131348s
>>> https://raw.githubusercontent.com/kris3713/UltimateBTTrackersList/refs/heads/master/ultimate_trackers.txt
  HTTP 200, total 0.076898s
>>> https://raw.githubusercontent.com/entr0pia/TrackersListCollection-S/refs/heads/master/https.txt
  HTTP 200, total 0.098784s
[INFO] public list https://cf.trackerslist.com/all.txt: 122 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all.txt: 75 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ip.txt: 53 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_udp.txt: 48 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_http.txt: 17 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_https.txt: 10 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ws.txt: 3 urls
[OK]   1295 new candidates -> candidates_20261017.txt
[OK]   1295 new candidates
[ERROR] No valid trackers found in response
[INFO] Repo: Pmwiu/Tracker-List, Max: 59
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/ngosang/trackerslist/master/blacklist.txt (391 URLs)
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/blacklist.txt (20 URLs)
[INFO] URL blacklist: 389 URLs (dynamic + remote sources)
[INFO] Protected hosts (防误杀): 99
[INFO] discovered candidates: 1077 URLs in 1 file(s)

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
[OK]   discovered_set.json (1077)

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
  [ALIVE] (5/320) http://004430.xyz:80/announce 146ms — announce with peers:1
  [ALIVE] (6/320) http://107.189.2.131:1337/announce 197ms — announce with peers:1
  [ALIVE] (19/320) http://138.186.10.167:1337/announce 231ms — announce with peers:1
  [ALIVE] (20/320) http://1337.abcvg.info:80/announce 172ms — announce with peers:1
  [ALIVE] (21/320) http://140.235.237.23:6969/announce 505ms — announce with peers:1
  [DEAD]  (25/320) http://109.121.134.121:1337/announce — URLError: <urlopen error timed out>
  [ALIVE] (48/320) http://185.126.65.92:6969/announce 191ms — announce without peers
  [DEAD]  (50/320) http://113.13.7.90:6969/announce — URLError: <urlopen error timed out>
  [ALIVE] (57/320) http://207.241.226.111:6969/announce 129ms — announce with peers:1
  [ALIVE] (58/320) http://207.241.231.226:6969/announce 133ms — announce with peers:1
  [ALIVE] (65/320) http://211.75.205.187:6969/announce 378ms — announce with peers:1
  [ALIVE] (66/320) http://211.75.205.187:80/announce 379ms — announce with peers:1
  [ALIVE] (67/320) http://211.75.205.188:6969/announce 378ms — announce with peers:1
  [ALIVE] (69/320) http://211.75.205.188:80/announce 378ms — announce with peers:1
  [ALIVE] (70/320) http://211.75.210.221:6969/announce 378ms — announce with peers:1
  [ALIVE] (71/320) http://211.75.210.221:80/announce 376ms — announce with peers:1
  [ALIVE] (72/320) http://43.250.54.126:6969/announce 165ms — announce with peers:1
  [ALIVE] (73/320) http://216.144.239.90:6969/announce 243ms — announce with peers:1
  [ALIVE] (74/320) http://93.158.213.92:1337/announce 166ms — announce with peers:1
  [ALIVE] (75/320) http://94.23.207.177:6969/announce 171ms — announce with peers:1
  [ALIVE] (76/320) http://announce.sktorrent.eu:6969/announce 214ms — announce with peers:1
  [ALIVE] (77/320) http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 195ms — announce with peers:1
  [ALIVE] (78/320) http://ipv4announce.sktorrent.eu:6969/announce 186ms — announce with peers:1
  [ALIVE] (79/320) http://open.tracker.cl:1337/announce 371ms — announce with peers:1
  [ALIVE] (80/320) http://retracker01-msk-virt.corbina.net:80/announce 466ms — announce with peers:1
  [ALIVE] (81/320) http://t.overflow.biz:6969/announce 249ms — announce with peers:1
  [ALIVE] (82/320) http://tr.nyacat.pw:80/announce 205ms — announce without peers
  [DEAD]  (100/320) http://200.232.254.1:6969/announce — URLError: <urlopen error timed out>
  [ALIVE] (102/320) https://t.213891.xyz:443/announce 38ms — announce without peers
  [ALIVE] (103/320) https://004430.xyz:443/announce 151ms — announce with peers:1
  [ALIVE] (106/320) http://tracker.waaa.moe:6969/announce 342ms — announce with peers:1
  [ALIVE] (109/320) https://tr.nyacat.pw:443/announce 116ms — announce without peers
  [ALIVE] (110/320) http://tracker.qu.ax:6969/announce 164ms — announce with peers:1
  [ALIVE] (111/320) https://tracker.7471.top:443/announce 130ms — announce without peers
  [ALIVE] (114/320) https://1.tracker.eu.org:443/announce 46ms — announce without peers
  [ALIVE] (115/320) http://tracker.zhuqiy.dgj055.icu:80/announce 228ms — announce without peers
  [ALIVE] (118/320) http://tracker.mywaifu.best:6969/announce 390ms — announce without peers
  [ALIVE] (119/320) http://tracker.dler.org:6969/announce 383ms — announce with peers:1
  [ALIVE] (120/320) http://tracker.dler.com:6969/announce 382ms — announce with peers:1
  [ALIVE] (122/320) http://tracker.renfei.net:8080/announce 19ms — announce with peers:1
  [ALIVE] (123/320) udp://164.152.110.70:6969/announce 17ms — valid connect + announce (v4)
  [ALIVE] (124/320) https://open.ftorrent.com:443/announce 152ms — announce without peers
  [ALIVE] (125/320) udp://149.106.106.25:443/announce 46ms — valid connect + announce (v4)
  [ALIVE] (127/320) http://tracker2.dler.org:80/announce 383ms — announce with peers:1
  [ALIVE] (128/320) udp://109.201.134.183:80/announce 84ms — valid connect + announce (v4)
  [ALIVE] (129/320) udp://192.99.100.68:6969/announce 14ms — valid connect + announce (v4)
  [ALIVE] (130/320) udp://135.125.198.235:1984/announce 92ms — valid connect + announce (v4)
  [ALIVE] (131/320) http://tracker.opentrackr.org:1337/announce 369ms — announce with peers:1
  [ALIVE] (132/320) https://tracker.zhuqiy.com:443/announce 73ms — announce with peers:1
  [ALIVE] (133/320) https://tracker.foreverpirates.co:443/announce 341ms — announce without peers
  [ALIVE] (135/320) udp://151.242.104.187:80/announce 99ms — valid connect + announce (v4)
  [ALIVE] (136/320) udp://180.131.145.175:6969/announce 69ms — valid connect + announce (v4)
  [ALIVE] (137/320) udp://178.239.19.29:80/announce 91ms — valid connect + announce (v4)
  [ALIVE] (138/320) udp://34.66.57.33:1337/announce 27ms — valid connect + announce (v4)
  [ALIVE] (139/320) udp://34.66.57.33:80/announce 26ms — valid connect + announce (v4)
  [ALIVE] (140/320) udp://185.216.179.62:25/announce 93ms — valid connect + announce (v4)
  [ALIVE] (141/320) udp://159.146.99.45:6969/announce 125ms — valid connect + announce (v4)
  [ALIVE] (142/320) udp://23.157.120.14:6969/announce 70ms — valid connect + announce (v4)
  [ALIVE] (143/320) udp://23.94.174.203:1337/announce 61ms — valid connect + announce (v4)
  [ALIVE] (144/320) udp://51.222.82.36:6969/announce 15ms — valid connect + announce (v4)
  [ALIVE] (145/320) udp://193.187.90.12:6969/announce 100ms — valid connect + announce (v4)
  [ALIVE] (146/320) udp://38.180.157.12:2715/announce 89ms — valid connect + announce (v4)
  [ALIVE] (147/320) udp://74.119.149.136:6969/announce 1ms — valid connect + announce (v4)
  [ALIVE] (148/320) udp://43.250.54.126:6969/announce 88ms — valid connect + announce (v4)
  [ALIVE] (149/320) udp://31.56.179.159:6969/announce 110ms — valid connect + announce (v4)
  [ALIVE] (150/320) udp://212.42.38.197:6969/announce 133ms — valid connect + announce (v4)
  [ALIVE] (151/320) udp://15.235.207.99:8081/announce 224ms — valid connect + announce (v4)
  [ALIVE] (152/320) udp://185.121.168.96:1337/announce 186ms — valid connect + announce (v4)
  [ALIVE] (153/320) udp://45.38.170.167:6969/announce 109ms — valid connect + announce (v4)
  [ALIVE] (154/320) udp://107.189.2.131:1337/announce 285ms — valid connect + announce (v4)
  [ALIVE] (155/320) udp://160.30.240.158:1337/announce 218ms — valid connect + announce (v4)
  [ALIVE] (156/320) https://tracker.nekomi.cn:443/announce 150ms — announce with peers:1
  [ALIVE] (158/320) udp://211.75.205.187:6969/announce 189ms — valid connect + announce (v4)
  [ALIVE] (159/320) udp://211.75.205.187:80/announce 189ms — valid connect + announce (v4)
  [ALIVE] (160/320) udp://65.109.28.17:6969/announce 114ms — valid connect + announce (v4)
  [ALIVE] (161/320) udp://65.109.28.33:6969/announce 115ms — valid connect + announce (v4)
  [ALIVE] (162/320) udp://93.158.213.92:6969/announce 83ms — valid connect + announce (v4)
  [ALIVE] (163/320) udp://evan.im:6969/announce 2ms — valid connect + announce (v4)
  [ALIVE] (164/320) udp://ns575949.ip-51-222-82.net:6969/announce 15ms — valid connect + announce (v4)
  [ALIVE] (165/320) udp://47.76.201.250:6969/announce 199ms — valid connect + announce (v4)
  [ALIVE] (166/320) udp://ipv4announce.sktorrent.eu:6969/announce 86ms — valid connect + announce (v4)
  [ALIVE] (167/320) udp://74.81.245.60:2010/announce 152ms — valid connect + announce (v4)
  [ALIVE] (168/320) udp://open.ftorrent.com:443/announce 52ms — valid connect + announce (v4)
  [ALIVE] (169/320) https://tracker.midnightprogrammer.net:443/announce 804ms — announce without peers
  [ALIVE] (170/320) udp://bt-tracker.de:6969/announce 84ms — valid connect + announce (v4)
  [ALIVE] (171/320) udp://mail.segso.net:6969/announce 119ms — valid connect + announce (v4)
  [ALIVE] (173/320) udp://explodie.org:6969/announce 70ms — valid connect + announce (v4)
  [ALIVE] (174/320) udp://open.stealth.si:80/announce 95ms — valid connect + announce (v4)
  [ALIVE] (175/320) udp://seedpeer.net:6969/announce 64ms — valid connect + announce (v4)
  [ALIVE] (176/320) udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 265ms — valid connect + announce (v4)
  [ALIVE] (177/320) udp://tr4ck3r.duckdns.org:6969/announce 15ms — valid connect + announce (v4)
  [ALIVE] (178/320) udp://60.172.236.18:6969/announce 283ms — valid connect + announce (v4)
  [ALIVE] (179/320) udp://t.overflow.biz:6969/announce 115ms — valid connect + announce (v4)
  [ALIVE] (180/320) udp://retracker01-msk-virt.corbina.net:80/announce 135ms — valid connect + announce (v4)
  [ALIVE] (181/320) udp://kolankoalastree.newtrackon.co.nz:1337/announce 198ms — valid connect + announce (v4)
  [ALIVE] (182/320) udp://tr.btube3.com:2010/announce 131ms — valid connect + announce (v4)
  [ALIVE] (184/320) udp://tr3.ysagin.top:2715/announce 91ms — valid connect + announce (v4)
  [ALIVE] (185/320) udp://open.demonii.com:1337/announce 186ms — valid connect + announce (v4)
  [ALIVE] (186/320) udp://martin-gebhardt.eu:25/announce 98ms — valid connect + announce (v4)
  [ALIVE] (188/320) http://t.nyaatracker.com:80/announce 227ms — announce without peers
  [DEAD]  (200/320) http://tk.greedland.net:80/announce — URLError: <urlopen error [Errno -2] Name or service not known>
  [ALIVE] (202/320) http://tracker.dhitechnical.com:6969/announce 3825ms — announce with peers:1
  [ALIVE] (206/320) udp://exodus.desync.com:6969/announce 71ms — valid connect + announce (v4)
  [ALIVE] (212/320) http://tracker.coppersurfer.site:2710/announce 181ms — announce without peers
  [DEAD]  (225/320) http://tracker.dutchtracking.nl:80/announce — URLError: <urlopen error [Errno -2] Name or service not known>
  [ALIVE] (247/320) http://tracker.novaopcj.eu.org:6969/announce 166ms — announce with peers:1
  [DEAD]  (250/320) http://tracker.kicks-ass.net:80/announce — URLError: <urlopen error [Errno -2] Name or service not known>
  [DEAD]  (275/320) http://tracker.files.fm:6969/announce — URLError: <urlopen error timed out>
  [DEAD]  (300/320) http://tracker3.ctix.cn:2095/announce — URLError: <urlopen error [Errno -2] Name or service not known>

[INFO] First pass done in 91.7s
[INFO] Multi-sample: 3 samples on top 50 alive trackers...
[INFO] Multi-sample refined 48 trackers (median + jitter penalty)
[INFO] Same-subnet(/24) dedup removed 46 slower tracker(s)
[INFO] scrape probe: 20 http/https alive trackers
[INFO] scrape: 4 responded, 2 with seeders
[INFO] discovered candidates excluded from all: 1077

===== Test Summary =====
  Total tested:   320
  Alive (raw):    55
  All (final):    53 (top 59 by composite score)
  Unsafe filtered:3
  Low-speed:      0 (>5s excluded)
  Same-subnet dedup:  46 (kept faster)
  Dead final:     263
  Time:           100.4s
=== 协议分布统计 ===
  HTTP  : 38 个
  HTTPS : 10 个
  UDP   : 53 个
  WSS   : 0 个
  WS    : 0 个
  总计: 101 个（存活）
=========================

============================================================
 Round 1 - 2026-10-17 11:02:00
============================================================
  [PASS] Local tracker: trackers_ngosang_all.txt: 75 trackers
  [PASS] Local tracker: trackers_ngosang_all_ip.txt: 51 trackers
  [FAIL] Local tracker: trackers_ngosang_yggdrasil_ip.txt: missing
  [PASS] Local tracker: trackers_cf_all.txt: 106 trackers
  [PASS] Local tracker: trackers_adysec_all.txt: 3285 trackers
  [PASS] Local tracker: trackers_kris3713_ultimate.txt: 162 trackers
  [PASS] Local tracker: trackers_entr0pia_https.txt: 16 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_all.txt: 53 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Discovery output: 1295 candidates in 1 file(s)
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
 Round 1 - 2026-10-17 11:02:07
============================================================
  [PASS] Local tracker: trackers_ngosang_all.txt: 75 trackers
  [PASS] Local tracker: trackers_ngosang_all_ip.txt: 51 trackers
  [FAIL] Local tracker: trackers_ngosang_yggdrasil_ip.txt: missing
  [PASS] Local tracker: trackers_cf_all.txt: 106 trackers
  [PASS] Local tracker: trackers_adysec_all.txt: 3285 trackers
  [PASS] Local tracker: trackers_kris3713_ultimate.txt: 162 trackers
  [PASS] Local tracker: trackers_entr0pia_https.txt: 16 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_all.txt: 53 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Discovery output: 1295 candidates in 1 file(s)
  [PASS] Merged dedup check: 200 unique
  [PASS] URL format check: all 200 valid
------------------------------------------------------------
  Result: 14 passed, 0 warnings, 1 failed
============================================================

============================================================
 Round 2 - 2026-10-17 11:02:12
============================================================
  [PASS] Local tracker: trackers_ngosang_all.txt: 75 trackers
  [PASS] Local tracker: trackers_ngosang_all_ip.txt: 51 trackers
  [FAIL] Local tracker: trackers_ngosang_yggdrasil_ip.txt: missing
  [PASS] Local tracker: trackers_cf_all.txt: 106 trackers
  [PASS] Local tracker: trackers_adysec_all.txt: 3285 trackers
  [PASS] Local tracker: trackers_kris3713_ultimate.txt: 162 trackers
  [PASS] Local tracker: trackers_entr0pia_https.txt: 16 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_all.txt: 53 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Discovery output: 1295 candidates in 1 file(s)
  [PASS] Merged dedup check: 200 unique
  [PASS] URL format check: all 200 valid
------------------------------------------------------------
  Result: 14 passed, 0 warnings, 1 failed
============================================================

============================================================
 Round 3 - 2026-10-17 11:02:17
============================================================
  [PASS] Local tracker: trackers_ngosang_all.txt: 75 trackers
  [PASS] Local tracker: trackers_ngosang_all_ip.txt: 51 trackers
  [FAIL] Local tracker: trackers_ngosang_yggdrasil_ip.txt: missing
  [PASS] Local tracker: trackers_cf_all.txt: 106 trackers
  [PASS] Local tracker: trackers_adysec_all.txt: 3285 trackers
  [PASS] Local tracker: trackers_kris3713_ultimate.txt: 162 trackers
  [PASS] Local tracker: trackers_entr0pia_https.txt: 16 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_all.txt: 53 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Discovery output: 1295 candidates in 1 file(s)
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
=== End of diagnostics (Sat Oct 17 11:02:17 UTC 2026) ===
