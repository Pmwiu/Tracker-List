=== Diagnostics Sat Oct 17 03:21:39 UTC 2026 ===
Python: Python 3.12.15
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt
  HTTP 200, total 0.277429s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ip.txt
  HTTP 200, total 0.268306s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_yggdrasil_ip.txt
  HTTP 200, total 0.297945s
>>> https://cf.trackerslist.com/all.txt
  HTTP 200, total 0.128820s
>>> https://tracker.adysec.com/trackers_all.txt
  HTTP 200, total 0.138896s
>>> https://raw.githubusercontent.com/kris3713/UltimateBTTrackersList/refs/heads/master/ultimate_trackers.txt
  HTTP 200, total 0.145431s
>>> https://raw.githubusercontent.com/entr0pia/TrackersListCollection-S/refs/heads/master/https.txt
  HTTP 200, total 0.148159s
[INFO] public list https://cf.trackerslist.com/all.txt: 122 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all.txt: 72 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ip.txt: 53 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_udp.txt: 45 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_http.txt: 17 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_https.txt: 10 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ws.txt: 3 urls
[OK]   1301 new candidates -> candidates_20261017.txt
[OK]   1301 new candidates
[ERROR] No valid trackers found in response
[INFO] Repo: Pmwiu/Tracker-List, Max: 59
[CLEAN] trackers/trackers_adysec_all.txt
[CLEAN] trackers/trackers_ngosang_all_ip.txt
[CLEAN] trackers/trackers_ngosang_all.txt
[CLEAN] trackers/trackers_cf_all.txt
[CLEAN] docs/adysec_all.txt
[CLEAN] docs/ngosang_all_ip.txt
[CLEAN] docs/ngosang_all.txt
[CLEAN] docs/cf_all.txt
[OK]   Cleaned 8 legacy files.
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/ngosang/trackerslist/master/blacklist.txt (391 URLs)
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/blacklist.txt (20 URLs)
[INFO] URL blacklist: 389 URLs (dynamic + remote sources)
[INFO] Protected hosts (防误杀): 114
[INFO] discovered candidates: 1083 URLs in 1 file(s)

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
[OK]   discovered_set.json (1083)
[OK]   MIRRORS.txt
[OK]   /s/all
[OK]   index.html
[OK]   docs/all.txt
[OK]   docs/merged.txt
[OK]   docs/ngosang_all.txt
[OK]   docs/ngosang_all_ip.txt
[OK]   docs/cf_all.txt
[OK]   docs/adysec_all.txt
[OK]   docs/kris3713_ultimate.txt
[OK]   docs/entr0pia_https.txt
[OK]   docs/udp.txt
[OK]   docs/http.txt
[OK]   docs/https.txt
[OK]   docs/wss.txt
[OK]   docs/ws.txt

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
  [ALIVE] (3/320) http://004430.xyz:80/announce 27ms — announce with peers:1
  [ALIVE] (8/320) http://107.189.2.131:1337/announce 283ms — announce with peers:1
  [ALIVE] (20/320) http://138.186.10.167:1337/announce 266ms — announce with peers:1
  [ALIVE] (22/320) http://1337.abcvg.info:80/announce 257ms — announce with peers:1
  [ALIVE] (25/320) http://140.235.237.23:6969/announce 2260ms — announce with peers:1
  [DEAD]  (50/320) http://113.16.152.171:6969/announce — URLError: <urlopen error timed out>
  [ALIVE] (51/320) http://185.126.65.92:6969/announce 265ms — announce without peers
  [ALIVE] (66/320) http://207.241.226.111:6969/announce 35ms — announce with peers:1
  [ALIVE] (67/320) http://207.241.231.226:6969/announce 37ms — announce with peers:1
  [ALIVE] (69/320) http://211.75.205.187:6969/announce 307ms — announce with peers:1
  [ALIVE] (70/320) http://211.75.205.187:80/announce 281ms — announce with peers:1
  [ALIVE] (71/320) http://216.144.239.90:6969/announce 18ms — announce with peers:1
  [ALIVE] (72/320) http://211.75.205.188:6969/announce 294ms — announce with peers:1
  [ALIVE] (73/320) http://43.250.54.126:6969/announce 259ms — announce with peers:1
  [ALIVE] (74/320) http://93.158.213.92:1337/announce 262ms — announce with peers:1
  [ALIVE] (75/320) http://94.23.207.177:6969/announce 288ms — announce with peers:1
  [ALIVE] (76/320) http://announce.sktorrent.eu:6969/announce 306ms — announce with peers:1
  [ALIVE] (77/320) http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 372ms — announce with peers:1
  [ALIVE] (78/320) http://ipv4announce.sktorrent.eu:6969/announce 287ms — announce with peers:1
  [ALIVE] (80/320) http://retracker01-msk-virt.corbina.net:80/announce 585ms — announce with peers:1
  [ALIVE] (81/320) http://open.tracker.cl:1337/announce 347ms — announce with peers:1
  [ALIVE] (82/320) http://tr.nyacat.pw:80/announce 181ms — announce without peers
  [ALIVE] (83/320) http://t.overflow.biz:6969/announce 391ms — announce with peers:1
  [ALIVE] (84/320) http://tracker.bittor.pw:1337/announce 102ms — announce with peers:1
  [ALIVE] (85/320) http://tracker.dhitechnical.com:6969/announce 146ms — announce with peers:1
  [ALIVE] (86/320) http://tracker.dler.com:6969/announce 318ms — announce with peers:1
  [ALIVE] (87/320) http://tracker.dler.org:6969/announce 314ms — announce with peers:1
  [ALIVE] (88/320) http://tracker.mywaifu.best:6969/announce 301ms — announce without peers
  [DEAD]  (100/320) http://180.97.219.76:8070/announce — URLError: <urlopen error timed out>
  [ALIVE] (101/320) https://004430.xyz:443/announce 51ms — announce with peers:1
  [ALIVE] (102/320) https://t.213891.xyz:443/announce 38ms — announce without peers
  [ALIVE] (103/320) https://open.ftorrent.com:443/announce 112ms — announce without peers
  [ALIVE] (113/320) http://tracker.renfei.net:8080/announce 174ms — announce with peers:1
  [ALIVE] (116/320) https://tr.nyacat.pw:443/announce 186ms — announce without peers
  [ALIVE] (119/320) udp://149.106.106.25:443/announce 35ms — valid connect + announce (v4)
  [ALIVE] (120/320) http://tracker.qu.ax:6969/announce 261ms — announce with peers:1
  [ALIVE] (122/320) https://1.tracker.eu.org:443/announce 44ms — announce without peers
  [ALIVE] (123/320) https://tracker.foreverpirates.co:443/announce 236ms — announce without peers
  [DEAD]  (125/320) https://tracker.pmman.tech:443/announce — HTTPError: HTTP Error 404: Not Found
  [ALIVE] (126/320) http://tracker2.dler.org:80/announce 283ms — announce with peers:1
  [ALIVE] (127/320) udp://180.131.145.175:6969/announce 31ms — valid connect + announce (v4)
  [ALIVE] (128/320) http://tracker.opentrackr.org:1337/announce 396ms — announce with peers:1
  [ALIVE] (130/320) https://tracker.midnightprogrammer.net:443/announce 288ms — announce without peers
  [ALIVE] (131/320) udp://164.152.110.70:6969/announce 56ms — valid connect + announce (v4)
  [ALIVE] (132/320) udp://109.201.134.183:80/announce 131ms — valid connect + announce (v4)
  [ALIVE] (133/320) https://tracker.7471.top:443/announce 195ms — announce without peers
  [ALIVE] (134/320) udp://23.94.174.203:1337/announce 8ms — valid connect + announce (v4)
  [ALIVE] (135/320) https://tracker.zhuqiy.com:443/announce 122ms — announce with peers:1
  [ALIVE] (136/320) udp://23.157.120.14:6969/announce 32ms — valid connect + announce (v4)
  [ALIVE] (137/320) udp://135.125.198.235:1984/announce 145ms — valid connect + announce (v4)
  [ALIVE] (138/320) udp://192.99.100.68:6969/announce 70ms — valid connect + announce (v4)
  [ALIVE] (139/320) http://tracker.zhuqiy.dgj055.icu:80/announce 323ms — announce without peers
  [ALIVE] (140/320) udp://151.242.104.187:80/announce 142ms — valid connect + announce (v4)
  [ALIVE] (141/320) udp://15.235.207.99:8081/announce 175ms — valid connect + announce (v4)
  [ALIVE] (142/320) udp://34.66.57.33:1337/announce 53ms — valid connect + announce (v4)
  [ALIVE] (143/320) udp://34.66.57.33:80/announce 49ms — valid connect + announce (v4)
  [ALIVE] (144/320) udp://178.239.19.29:80/announce 133ms — valid connect + announce (v4)
  [ALIVE] (145/320) udp://160.30.240.158:1337/announce 143ms — valid connect + announce (v4)
  [ALIVE] (146/320) https://tracker.nekomi.cn:443/announce 45ms — announce with peers:1
  [ALIVE] (147/320) udp://185.121.168.96:1337/announce 130ms — valid connect + announce (v4)
  [ALIVE] (148/320) udp://159.146.99.45:6969/announce 168ms — valid connect + announce (v4)
  [ALIVE] (150/320) udp://185.216.179.62:25/announce 136ms — valid connect + announce (v4)
  [ALIVE] (151/320) udp://211.75.205.187:80/announce 140ms — valid connect + announce (v4)
  [ALIVE] (152/320) udp://193.187.90.12:6969/announce 148ms — valid connect + announce (v4)
  [ALIVE] (153/320) udp://211.75.205.187:6969/announce 153ms — valid connect + announce (v4)
  [ALIVE] (154/320) udp://74.119.149.136:6969/announce 49ms — valid connect + announce (v4)
  [ALIVE] (155/320) udp://51.222.82.36:6969/announce 70ms — valid connect + announce (v4)
  [ALIVE] (156/320) udp://43.250.54.126:6969/announce 130ms — valid connect + announce (v4)
  [ALIVE] (157/320) udp://212.42.38.197:6969/announce 171ms — valid connect + announce (v4)
  [ALIVE] (158/320) udp://31.56.179.159:6969/announce 151ms — valid connect + announce (v4)
  [ALIVE] (159/320) udp://74.81.245.60:2010/announce 76ms — valid connect + announce (v4)
  [ALIVE] (160/320) udp://explodie.org:6969/announce 23ms — valid connect + announce (v4)
  [ALIVE] (161/320) udp://38.180.157.12:2715/announce 159ms — valid connect + announce (v4)
  [ALIVE] (162/320) udp://45.38.170.167:6969/announce 153ms — valid connect + announce (v4)
  [ALIVE] (163/320) udp://47.76.201.250:6969/announce 153ms — valid connect + announce (v4)
  [ALIVE] (164/320) udp://93.158.213.92:6969/announce 131ms — valid connect + announce (v4)
  [ALIVE] (165/320) udp://open.ftorrent.com:443/announce 35ms — valid connect + announce (v4)
  [ALIVE] (166/320) udp://65.109.28.17:6969/announce 161ms — valid connect + announce (v4)
  [ALIVE] (168/320) udp://65.109.28.33:6969/announce 159ms — valid connect + announce (v4)
  [ALIVE] (169/320) udp://evan.im:6969/announce 49ms — valid connect + announce (v4)
  [ALIVE] (170/320) udp://seedpeer.net:6969/announce 30ms — valid connect + announce (v4)
  [ALIVE] (171/320) udp://60.172.236.18:6969/announce 207ms — valid connect + announce (v4)
  [ALIVE] (172/320) udp://ipv4announce.sktorrent.eu:6969/announce 145ms — valid connect + announce (v4)
  [ALIVE] (174/320) udp://martin-gebhardt.eu:25/announce 136ms — valid connect + announce (v4)
  [ALIVE] (175/320) udp://edgev.duckdns.org:6969/announce 171ms — valid connect + announce (v4)
  [ALIVE] (176/320) udp://open.demonii.com:1337/announce 130ms — valid connect + announce (v4)
  [ALIVE] (177/320) udp://mail.segso.net:6969/announce 157ms — valid connect + announce (v4)
  [ALIVE] (178/320) udp://admin.52ywp.com:6969/announce 225ms — valid connect + announce (v4)
  [ALIVE] (179/320) udp://tr.btube3.com:2010/announce 70ms — valid connect + announce (v4)
  [ALIVE] (180/320) udp://tr4ck3r.duckdns.org:6969/announce 70ms — valid connect + announce (v4)
  [ALIVE] (181/320) udp://kolankoalastree.newtrackon.co.nz:1337/announce 143ms — valid connect + announce (v4)
  [ALIVE] (183/320) udp://bt-tracker.de:6969/announce 124ms — valid connect + announce (v4)
  [ALIVE] (184/320) udp://t.overflow.biz:6969/announce 153ms — valid connect + announce (v4)
  [ALIVE] (185/320) udp://retracker01-msk-virt.corbina.net:80/announce 171ms — valid connect + announce (v4)
  [ALIVE] (186/320) udp://107.189.2.131:1337/announce 557ms — valid connect + announce (v4)
  [ALIVE] (187/320) udp://tr3.ysagin.top:2715/announce 154ms — valid connect + announce (v4)
  [ALIVE] (188/320) udp://ns575949.ip-51-222-82.net:6969/announce 70ms — valid connect + announce (v4)
  [ALIVE] (189/320) udp://open.stealth.si:80/announce 142ms — valid connect + announce (v4)
  [ALIVE] (192/320) http://t.nyaatracker.com:80/announce 318ms — announce without peers
  [ALIVE] (199/320) udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 323ms — valid connect + announce (v4)
  [ALIVE] (200/320) http://tracker.waaa.moe:6969/announce 2038ms — announce with peers:1
  [ALIVE] (211/320) udp://exodus.desync.com:6969/announce 23ms — valid connect + announce (v4)
  [ALIVE] (215/320) http://tracker.coppersurfer.site:2710/announce 289ms — announce without peers
  [DEAD]  (225/320) https://tracker.adgk.net:443/announce — HTTPError: HTTP Error 522: Connection Timeout with Origin Server
  [ALIVE] (235/320) http://tracker.iro.moe:80/announce 115ms — announce with peers:1
  [ALIVE] (246/320) http://tracker.nucozer-tracker.ml:2710/announce 159ms — announce with peers:1
  [ALIVE] (247/320) http://tracker.novaopcj.eu.org:6969/announce 262ms — announce with peers:1
  [DEAD]  (250/320) http://siwserver.duckdns.org:9900/announce — URLError: <urlopen error timed out>
  [DEAD]  (275/320) http://tracker.files.fm:6969/announce — URLError: <urlopen error timed out>
  [DEAD]  (300/320) http://tracker.peckservers.com:9000/announce — URLError: <urlopen error [Errno 101] Network is unreachable>

[INFO] First pass done in 89.4s
[INFO] Multi-sample: 3 samples on top 50 alive trackers...
[INFO] Multi-sample refined 48 trackers (median + jitter penalty)
[INFO] Same-subnet(/24) dedup removed 49 slower tracker(s)
[INFO] scrape probe: 19 http/https alive trackers
[INFO] scrape: 5 responded, 4 with seeders
[INFO] discovered candidates excluded from all: 1083

===== Test Summary =====
  Total tested:   320
  Alive (raw):    54
  All (final):    53 (top 59 by composite score)
  Unsafe filtered:3
  Low-speed:      0 (>5s excluded)
  Same-subnet dedup:  49 (kept faster)
  Dead final:     264
  Time:           99.8s
=== 协议分布统计 ===
  HTTP  : 38 个
  HTTPS : 10 个
  UDP   : 55 个
  WSS   : 0 个
  WS    : 0 个
  总计: 103 个（存活）
=========================
[OK]   /s/all
[OK]   index.html
[OK] Pages regenerated with all statistics.
[OK]   docs/all.txt
[OK]   docs/merged.txt
[OK]   docs/ngosang_all.txt
[OK]   docs/ngosang_all_ip.txt
[OK]   docs/cf_all.txt
[OK]   docs/adysec_all.txt
[OK]   docs/kris3713_ultimate.txt
[OK]   docs/entr0pia_https.txt
[OK]   docs/udp.txt
[OK]   docs/http.txt
[OK]   docs/https.txt
[OK]   docs/wss.txt
[OK]   docs/ws.txt
[OK] Plain-text files synced to docs/.

============================================================
 Round 1 - 2026-10-17 03:23:37
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
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1301 candidates in 1 file(s)
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /all.txt: 53 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_all.txt: 75 trackers
  [PASS] Plain text: /ngosang_all_ip.txt: 51 trackers
  [FAIL] Plain text: /ngosang_yggdrasil_ip.txt: missing
  [PASS] Plain text: /cf_all.txt: 106 trackers
  [PASS] Plain text: /adysec_all.txt: 3285 trackers
  [PASS] Plain text: /kris3713_ultimate.txt: 162 trackers
  [PASS] Plain text: /entr0pia_https.txt: 16 trackers
  [PASS] Plain text: /udp.txt: 57 trackers
  [PASS] Plain text: /http.txt: 124 trackers
  [PASS] Plain text: /https.txt: 18 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Merged dedup check: 200 unique
  [PASS] Consistency: trackers_all.txt vs all.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_ngosang_all.txt vs ngosang_all.txt: identical
  [PASS] Consistency: trackers_ngosang_all_ip.txt vs ngosang_all_ip.txt: identical
  [WARN] Consistency: trackers_ngosang_yggdrasil_ip.txt vs ngosang_yggdrasil_ip.txt: one side missing
  [PASS] Consistency: trackers_cf_all.txt vs cf_all.txt: identical
  [PASS] Consistency: trackers_adysec_all.txt vs adysec_all.txt: identical
  [PASS] Consistency: trackers_kris3713_ultimate.txt vs kris3713_ultimate.txt: identical
  [PASS] Consistency: trackers_entr0pia_https.txt vs entr0pia_https.txt: identical
  [PASS] Consistency: trackers_udp.txt vs udp.txt: identical
  [PASS] Consistency: trackers_http.txt vs http.txt: identical
  [PASS] Consistency: trackers_https.txt vs https.txt: identical
  [PASS] Consistency: trackers_wss.txt vs wss.txt: identical
  [PASS] Consistency: trackers_ws.txt vs ws.txt: identical
  [PASS] URL format check: all 200 valid
------------------------------------------------------------
  Result: 43 passed, 1 warnings, 2 failed
============================================================

############################################################
 FINAL REPORT: 1 rounds completed
   Total PASS: 43
   Total WARN: 1
   Total FAIL: 2
   STATUS: ISSUES DETECTED
############################################################

============================================================
 Round 1 - 2026-10-17 03:23:45
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
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1301 candidates in 1 file(s)
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /all.txt: 53 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_all.txt: 75 trackers
  [PASS] Plain text: /ngosang_all_ip.txt: 51 trackers
  [FAIL] Plain text: /ngosang_yggdrasil_ip.txt: missing
  [PASS] Plain text: /cf_all.txt: 106 trackers
  [PASS] Plain text: /adysec_all.txt: 3285 trackers
  [PASS] Plain text: /kris3713_ultimate.txt: 162 trackers
  [PASS] Plain text: /entr0pia_https.txt: 16 trackers
  [PASS] Plain text: /udp.txt: 57 trackers
  [PASS] Plain text: /http.txt: 124 trackers
  [PASS] Plain text: /https.txt: 18 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Merged dedup check: 200 unique
  [PASS] Consistency: trackers_all.txt vs all.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_ngosang_all.txt vs ngosang_all.txt: identical
  [PASS] Consistency: trackers_ngosang_all_ip.txt vs ngosang_all_ip.txt: identical
  [WARN] Consistency: trackers_ngosang_yggdrasil_ip.txt vs ngosang_yggdrasil_ip.txt: one side missing
  [PASS] Consistency: trackers_cf_all.txt vs cf_all.txt: identical
  [PASS] Consistency: trackers_adysec_all.txt vs adysec_all.txt: identical
  [PASS] Consistency: trackers_kris3713_ultimate.txt vs kris3713_ultimate.txt: identical
  [PASS] Consistency: trackers_entr0pia_https.txt vs entr0pia_https.txt: identical
  [PASS] Consistency: trackers_udp.txt vs udp.txt: identical
  [PASS] Consistency: trackers_http.txt vs http.txt: identical
  [PASS] Consistency: trackers_https.txt vs https.txt: identical
  [PASS] Consistency: trackers_wss.txt vs wss.txt: identical
  [PASS] Consistency: trackers_ws.txt vs ws.txt: identical
  [PASS] URL format check: all 200 valid
  [PASS] Raw: merged (Raw): HTTP 200, 200 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 200 trackers
  [PASS] Pages short: /s/all: HTTP 200, redirect OK
------------------------------------------------------------
  Result: 46 passed, 1 warnings, 2 failed
============================================================

============================================================
 Round 2 - 2026-10-17 03:23:50
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
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1301 candidates in 1 file(s)
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /all.txt: 53 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_all.txt: 75 trackers
  [PASS] Plain text: /ngosang_all_ip.txt: 51 trackers
  [FAIL] Plain text: /ngosang_yggdrasil_ip.txt: missing
  [PASS] Plain text: /cf_all.txt: 106 trackers
  [PASS] Plain text: /adysec_all.txt: 3285 trackers
  [PASS] Plain text: /kris3713_ultimate.txt: 162 trackers
  [PASS] Plain text: /entr0pia_https.txt: 16 trackers
  [PASS] Plain text: /udp.txt: 57 trackers
  [PASS] Plain text: /http.txt: 124 trackers
  [PASS] Plain text: /https.txt: 18 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Merged dedup check: 200 unique
  [PASS] Consistency: trackers_all.txt vs all.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_ngosang_all.txt vs ngosang_all.txt: identical
  [PASS] Consistency: trackers_ngosang_all_ip.txt vs ngosang_all_ip.txt: identical
  [WARN] Consistency: trackers_ngosang_yggdrasil_ip.txt vs ngosang_yggdrasil_ip.txt: one side missing
  [PASS] Consistency: trackers_cf_all.txt vs cf_all.txt: identical
  [PASS] Consistency: trackers_adysec_all.txt vs adysec_all.txt: identical
  [PASS] Consistency: trackers_kris3713_ultimate.txt vs kris3713_ultimate.txt: identical
  [PASS] Consistency: trackers_entr0pia_https.txt vs entr0pia_https.txt: identical
  [PASS] Consistency: trackers_udp.txt vs udp.txt: identical
  [PASS] Consistency: trackers_http.txt vs http.txt: identical
  [PASS] Consistency: trackers_https.txt vs https.txt: identical
  [PASS] Consistency: trackers_wss.txt vs wss.txt: identical
  [PASS] Consistency: trackers_ws.txt vs ws.txt: identical
  [PASS] URL format check: all 200 valid
  [PASS] Raw: merged (Raw): HTTP 200, 200 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 200 trackers
  [PASS] Pages short: /s/all: HTTP 200, redirect OK
------------------------------------------------------------
  Result: 46 passed, 1 warnings, 2 failed
============================================================

============================================================
 Round 3 - 2026-10-17 03:23:55
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
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1301 candidates in 1 file(s)
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /all.txt: 53 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_all.txt: 75 trackers
  [PASS] Plain text: /ngosang_all_ip.txt: 51 trackers
  [FAIL] Plain text: /ngosang_yggdrasil_ip.txt: missing
  [PASS] Plain text: /cf_all.txt: 106 trackers
  [PASS] Plain text: /adysec_all.txt: 3285 trackers
  [PASS] Plain text: /kris3713_ultimate.txt: 162 trackers
  [PASS] Plain text: /entr0pia_https.txt: 16 trackers
  [PASS] Plain text: /udp.txt: 57 trackers
  [PASS] Plain text: /http.txt: 124 trackers
  [PASS] Plain text: /https.txt: 18 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Merged dedup check: 200 unique
  [PASS] Consistency: trackers_all.txt vs all.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_ngosang_all.txt vs ngosang_all.txt: identical
  [PASS] Consistency: trackers_ngosang_all_ip.txt vs ngosang_all_ip.txt: identical
  [WARN] Consistency: trackers_ngosang_yggdrasil_ip.txt vs ngosang_yggdrasil_ip.txt: one side missing
  [PASS] Consistency: trackers_cf_all.txt vs cf_all.txt: identical
  [PASS] Consistency: trackers_adysec_all.txt vs adysec_all.txt: identical
  [PASS] Consistency: trackers_kris3713_ultimate.txt vs kris3713_ultimate.txt: identical
  [PASS] Consistency: trackers_entr0pia_https.txt vs entr0pia_https.txt: identical
  [PASS] Consistency: trackers_udp.txt vs udp.txt: identical
  [PASS] Consistency: trackers_http.txt vs http.txt: identical
  [PASS] Consistency: trackers_https.txt vs https.txt: identical
  [PASS] Consistency: trackers_wss.txt vs wss.txt: identical
  [PASS] Consistency: trackers_ws.txt vs ws.txt: identical
  [PASS] URL format check: all 200 valid
  [PASS] Raw: merged (Raw): HTTP 200, 200 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 200 trackers
  [PASS] Pages short: /s/all: HTTP 200, redirect OK
------------------------------------------------------------
  Result: 46 passed, 1 warnings, 2 failed
============================================================

############################################################
 FINAL REPORT: 3 rounds completed
   Total PASS: 138
   Total WARN: 3
   Total FAIL: 6
   STATUS: ISSUES DETECTED
############################################################
=== End of diagnostics (Sat Oct 17 03:23:55 UTC 2026) ===
