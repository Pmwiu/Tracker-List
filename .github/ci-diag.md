=== Diagnostics Sat Oct 17 04:43:21 UTC 2026 ===
Python: Python 3.12.15
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt
  HTTP 200, total 0.089831s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ip.txt
  HTTP 200, total 0.118023s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_yggdrasil_ip.txt
  HTTP 200, total 0.121595s
>>> https://cf.trackerslist.com/all.txt
  HTTP 200, total 0.194698s
>>> https://tracker.adysec.com/trackers_all.txt
  HTTP 200, total 0.211515s
>>> https://raw.githubusercontent.com/kris3713/UltimateBTTrackersList/refs/heads/master/ultimate_trackers.txt
  HTTP 200, total 0.099943s
>>> https://raw.githubusercontent.com/entr0pia/TrackersListCollection-S/refs/heads/master/https.txt
  HTTP 200, total 0.119150s
[INFO] public list https://cf.trackerslist.com/all.txt: 122 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all.txt: 75 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ip.txt: 53 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_udp.txt: 45 urls
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
[INFO] Protected hosts (防误杀): 134
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
  [ALIVE] (5/320) http://004430.xyz:80/announce 136ms — announce with peers:1
  [ALIVE] (7/320) http://107.189.2.131:1337/announce 265ms — announce with peers:1
  [DEAD]  (25/320) http://106.55.172.54:6969/announce — URLError: <urlopen error timed out>
  [ALIVE] (36/320) http://140.235.237.23:6969/announce 131ms — announce with peers:1
  [ALIVE] (42/320) http://1337.abcvg.info:80/announce 224ms — announce with peers:1
  [ALIVE] (43/320) http://138.186.10.167:1337/announce 269ms — announce with peers:1
  [DEAD]  (50/320) http://167.235.245.209:80/announce — HTTPError: HTTP Error 404: Not Found
  [ALIVE] (64/320) http://185.126.65.92:6969/announce 226ms — announce without peers
  [DEAD]  (75/320) http://116.9.207.198:6969/announce — URLError: <urlopen error timed out>
  [ALIVE] (77/320) http://207.241.226.111:6969/announce 77ms — announce with peers:1
  [ALIVE] (78/320) http://207.241.231.226:6969/announce 94ms — announce with peers:1
  [ALIVE] (79/320) http://216.144.239.90:6969/announce 103ms — announce with peers:1
  [ALIVE] (83/320) http://43.250.54.126:6969/announce 212ms — announce with peers:1
  [ALIVE] (84/320) http://93.158.213.92:1337/announce 229ms — announce with peers:1
  [ALIVE] (85/320) http://94.23.207.177:6969/announce 231ms — announce with peers:1
  [ALIVE] (87/320) http://announce.sktorrent.eu:6969/announce 234ms — announce with peers:1
  [ALIVE] (91/320) http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 300ms — announce with peers:1
  [ALIVE] (92/320) http://211.75.205.188:6969/announce 334ms — announce with peers:1
  [ALIVE] (93/320) http://211.75.205.187:80/announce 334ms — announce with peers:1
  [ALIVE] (94/320) http://211.75.205.187:6969/announce 335ms — announce with peers:1
  [ALIVE] (95/320) http://ipv4announce.sktorrent.eu:6969/announce 230ms — announce with peers:1
  [ALIVE] (97/320) http://tr.nyacat.pw:80/announce 139ms — announce without peers
  [ALIVE] (98/320) http://tracker.dhitechnical.com:6969/announce 163ms — announce with peers:1
  [ALIVE] (100/320) https://004430.xyz:443/announce 161ms — announce with peers:1
  [ALIVE] (101/320) http://tracker.mywaifu.best:6969/announce 271ms — announce without peers
  [ALIVE] (102/320) https://t.213891.xyz:443/announce 61ms — announce without peers
  [ALIVE] (104/320) http://tracker.renfei.net:8080/announce 110ms — announce with peers:1
  [ALIVE] (105/320) https://open.ftorrent.com:443/announce 66ms — announce without peers
  [ALIVE] (106/320) http://tracker.zhuqiy.dgj055.icu:80/announce 288ms — announce without peers
  [ALIVE] (108/320) http://tracker.qu.ax:6969/announce 219ms — announce with peers:1
  [ALIVE] (110/320) http://tracker2.dler.org:80/announce 342ms — announce with peers:1
  [ALIVE] (111/320) http://tracker.dler.org:6969/announce 419ms — announce with peers:1
  [ALIVE] (112/320) http://retracker01-msk-virt.corbina.net:80/announce 506ms — announce with peers:1
  [ALIVE] (113/320) http://tracker.dler.com:6969/announce 369ms — announce with peers:1
  [ALIVE] (114/320) https://1.tracker.eu.org:443/announce 46ms — announce without peers
  [ALIVE] (116/320) http://tracker.opentrackr.org:1337/announce 358ms — announce with peers:1
  [ALIVE] (118/320) http://open.tracker.cl:1337/announce 335ms — announce with peers:1
  [ALIVE] (119/320) https://tr.nyacat.pw:443/announce 245ms — announce without peers
  [ALIVE] (120/320) http://tracker.waaa.moe:6969/announce 415ms — announce with peers:1
  [ALIVE] (121/320) udp://149.106.106.25:443/announce 21ms — valid connect + announce (v4)
  [ALIVE] (122/320) udp://164.152.110.70:6969/announce 12ms — valid connect + announce (v4)
  [ALIVE] (123/320) https://tracker.7471.top:443/announce 186ms — announce without peers
  [ALIVE] (124/320) https://tracker.foreverpirates.co:443/announce 192ms — announce without peers
  [DEAD]  (125/320) https://tracker.pmman.tech:443/announce — HTTPError: HTTP Error 404: Not Found
  [ALIVE] (127/320) https://tracker.zhuqiy.com:443/announce 78ms — announce with peers:1
  [ALIVE] (128/320) udp://109.201.134.183:80/announce 111ms — valid connect + announce (v4)
  [ALIVE] (129/320) udp://180.131.145.175:6969/announce 77ms — valid connect + announce (v4)
  [ALIVE] (130/320) udp://192.99.100.68:6969/announce 45ms — valid connect + announce (v4)
  [ALIVE] (131/320) udp://135.125.198.235:1984/announce 129ms — valid connect + announce (v4)
  [ALIVE] (132/320) udp://151.242.104.187:80/announce 124ms — valid connect + announce (v4)
  [ALIVE] (133/320) https://tracker.midnightprogrammer.net:443/announce 350ms — announce without peers
  [ALIVE] (134/320) udp://178.239.19.29:80/announce 117ms — valid connect + announce (v4)
  [ALIVE] (135/320) udp://107.189.2.131:1337/announce 149ms — valid connect + announce (v4)
  [ALIVE] (136/320) udp://34.66.57.33:1337/announce 24ms — valid connect + announce (v4)
  [ALIVE] (137/320) udp://23.94.174.203:1337/announce 42ms — valid connect + announce (v4)
  [ALIVE] (138/320) udp://23.157.120.14:6969/announce 64ms — valid connect + announce (v4)
  [ALIVE] (139/320) udp://185.216.179.62:25/announce 126ms — valid connect + announce (v4)
  [ALIVE] (140/320) udp://34.66.57.33:80/announce 33ms — valid connect + announce (v4)
  [ALIVE] (141/320) udp://160.30.240.158:1337/announce 189ms — valid connect + announce (v4)
  [ALIVE] (142/320) udp://193.187.90.12:6969/announce 127ms — valid connect + announce (v4)
  [ALIVE] (143/320) udp://15.235.207.99:8081/announce 212ms — valid connect + announce (v4)
  [ALIVE] (144/320) udp://185.121.168.96:1337/announce 185ms — valid connect + announce (v4)
  [ALIVE] (145/320) udp://51.222.82.36:6969/announce 49ms — valid connect + announce (v4)
  [ALIVE] (146/320) udp://211.75.205.187:6969/announce 168ms — valid connect + announce (v4)
  [ALIVE] (147/320) udp://211.75.205.187:80/announce 173ms — valid connect + announce (v4)
  [ALIVE] (148/320) udp://31.56.179.159:6969/announce 137ms — valid connect + announce (v4)
  [ALIVE] (149/320) udp://212.42.38.197:6969/announce 156ms — valid connect + announce (v4)
  [ALIVE] (150/320) https://tracker.nekomi.cn:443/announce 177ms — announce with peers:1
  [ALIVE] (151/320) udp://43.250.54.126:6969/announce 108ms — valid connect + announce (v4)
  [ALIVE] (152/320) udp://38.180.157.12:2715/announce 118ms — valid connect + announce (v4)
  [ALIVE] (153/320) udp://74.119.149.136:6969/announce 36ms — valid connect + announce (v4)
  [ALIVE] (155/320) udp://45.38.170.167:6969/announce 132ms — valid connect + announce (v4)
  [ALIVE] (156/320) udp://52.58.128.163:6969/announce 114ms — valid connect + announce (v4)
  [ALIVE] (159/320) udp://74.81.245.60:2010/announce 97ms — valid connect + announce (v4)
  [ALIVE] (160/320) udp://47.76.201.250:6969/announce 177ms — valid connect + announce (v4)
  [ALIVE] (161/320) udp://65.109.28.17:6969/announce 136ms — valid connect + announce (v4)
  [ALIVE] (162/320) udp://65.109.28.33:6969/announce 137ms — valid connect + announce (v4)
  [ALIVE] (163/320) udp://93.158.213.92:6969/announce 115ms — valid connect + announce (v4)
  [ALIVE] (164/320) udp://evan.im:6969/announce 36ms — valid connect + announce (v4)
  [ALIVE] (165/320) udp://open.ftorrent.com:443/announce 25ms — valid connect + announce (v4)
  [ALIVE] (166/320) udp://explodie.org:6969/announce 68ms — valid connect + announce (v4)
  [ALIVE] (167/320) udp://exodus.desync.com:6969/announce 48ms — valid connect + announce (v4)
  [ALIVE] (168/320) udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 137ms — valid connect + announce (v4)
  [ALIVE] (169/320) udp://ipv4announce.sktorrent.eu:6969/announce 115ms — valid connect + announce (v4)
  [ALIVE] (170/320) udp://ns575949.ip-51-222-82.net:6969/announce 45ms — valid connect + announce (v4)
  [ALIVE] (171/320) udp://60.172.236.18:6969/announce 241ms — valid connect + announce (v4)
  [ALIVE] (173/320) udp://bt-tracker.de:6969/announce 124ms — valid connect + announce (v4)
  [ALIVE] (174/320) udp://seedpeer.net:6969/announce 81ms — valid connect + announce (v4)
  [ALIVE] (175/320) udp://tr.btube3.com:2010/announce 76ms — valid connect + announce (v4)
  [ALIVE] (176/320) udp://martin-gebhardt.eu:25/announce 129ms — valid connect + announce (v4)
  [ALIVE] (177/320) udp://mail.segso.net:6969/announce 144ms — valid connect + announce (v4)
  [ALIVE] (178/320) udp://kolankoalastree.newtrackon.co.nz:1337/announce 195ms — valid connect + announce (v4)
  [ALIVE] (179/320) udp://retracker01-msk-virt.corbina.net:80/announce 157ms — valid connect + announce (v4)
  [ALIVE] (180/320) udp://admin.52ywp.com:6969/announce 261ms — valid connect + announce (v4)
  [ALIVE] (182/320) udp://open.stealth.si:80/announce 119ms — valid connect + announce (v4)
  [ALIVE] (183/320) udp://t.overflow.biz:6969/announce 150ms — valid connect + announce (v4)
  [ALIVE] (184/320) udp://open.demonii.com:1337/announce 163ms — valid connect + announce (v4)
  [ALIVE] (186/320) udp://tr3.ysagin.top:2715/announce 117ms — valid connect + announce (v4)
  [ALIVE] (187/320) udp://tr4ck3r.duckdns.org:6969/announce 30ms — valid connect + announce (v4)
  [ALIVE] (190/320) http://t.overflow.biz:6969/announce 1920ms — announce with peers:1
  [DEAD]  (200/320) http://bt.ktkj.com:8080/announce — URLError: <urlopen error [Errno -2] Name or service not known>
  [DEAD]  (225/320) http://fe.dealclub.de:6969/announce — URLError: <urlopen error [Errno -5] No address associated with hostname>
  [DEAD]  (250/320) http://chihaya.de:80/announce — URLError: <urlopen error timed out>
  [ALIVE] (275/320) http://opentracker.xyz:80/announce 740ms — announce with peers:1
  [DEAD]  (300/320) http://shogiroom.com:6969/announce — URLError: <urlopen error [Errno -2] Name or service not known>

[INFO] First pass done in 93.5s
[INFO] Multi-sample: 3 samples on top 50 alive trackers...
[INFO] Multi-sample refined 49 trackers (median + jitter penalty)
[INFO] Same-subnet(/24) dedup removed 42 slower tracker(s)
[INFO] scrape probe: 19 http/https alive trackers
[INFO] scrape: 3 responded, 1 with seeders
[INFO] discovered candidates excluded from all: 1077

===== Test Summary =====
  Total tested:   320
  Alive (raw):    55
  All (final):    55 (top 59 by composite score)
  Unsafe filtered:5
  Low-speed:      0 (>5s excluded)
  Same-subnet dedup:  42 (kept faster)
  Dead final:     254
  Time:           101.8s
=== 协议分布统计 ===
  HTTP  : 33 个
  HTTPS : 10 个
  UDP   : 54 个
  WSS   : 0 个
  WS    : 0 个
  总计: 97 个（存活）
=========================

============================================================
 Round 1 - 2026-10-17 04:45:15
============================================================
  [PASS] Local tracker: trackers_ngosang_all.txt: 75 trackers
  [PASS] Local tracker: trackers_ngosang_all_ip.txt: 51 trackers
  [FAIL] Local tracker: trackers_ngosang_yggdrasil_ip.txt: missing
  [PASS] Local tracker: trackers_cf_all.txt: 106 trackers
  [PASS] Local tracker: trackers_adysec_all.txt: 3285 trackers
  [PASS] Local tracker: trackers_kris3713_ultimate.txt: 162 trackers
  [PASS] Local tracker: trackers_entr0pia_https.txt: 16 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_all.txt: 55 trackers
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
 Round 1 - 2026-10-17 04:45:21
============================================================
  [PASS] Local tracker: trackers_ngosang_all.txt: 75 trackers
  [PASS] Local tracker: trackers_ngosang_all_ip.txt: 51 trackers
  [FAIL] Local tracker: trackers_ngosang_yggdrasil_ip.txt: missing
  [PASS] Local tracker: trackers_cf_all.txt: 106 trackers
  [PASS] Local tracker: trackers_adysec_all.txt: 3285 trackers
  [PASS] Local tracker: trackers_kris3713_ultimate.txt: 162 trackers
  [PASS] Local tracker: trackers_entr0pia_https.txt: 16 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_all.txt: 55 trackers
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
 Round 2 - 2026-10-17 04:45:26
============================================================
  [PASS] Local tracker: trackers_ngosang_all.txt: 75 trackers
  [PASS] Local tracker: trackers_ngosang_all_ip.txt: 51 trackers
  [FAIL] Local tracker: trackers_ngosang_yggdrasil_ip.txt: missing
  [PASS] Local tracker: trackers_cf_all.txt: 106 trackers
  [PASS] Local tracker: trackers_adysec_all.txt: 3285 trackers
  [PASS] Local tracker: trackers_kris3713_ultimate.txt: 162 trackers
  [PASS] Local tracker: trackers_entr0pia_https.txt: 16 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_all.txt: 55 trackers
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
 Round 3 - 2026-10-17 04:45:31
============================================================
  [PASS] Local tracker: trackers_ngosang_all.txt: 75 trackers
  [PASS] Local tracker: trackers_ngosang_all_ip.txt: 51 trackers
  [FAIL] Local tracker: trackers_ngosang_yggdrasil_ip.txt: missing
  [PASS] Local tracker: trackers_cf_all.txt: 106 trackers
  [PASS] Local tracker: trackers_adysec_all.txt: 3285 trackers
  [PASS] Local tracker: trackers_kris3713_ultimate.txt: 162 trackers
  [PASS] Local tracker: trackers_entr0pia_https.txt: 16 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_all.txt: 55 trackers
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
=== End of diagnostics (Sat Oct 17 04:45:31 UTC 2026) ===
