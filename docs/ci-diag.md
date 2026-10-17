=== Diagnostics Sat Oct 17 02:20:23 UTC 2026 ===
Python: Python 3.12.15
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt
  HTTP 200, total 0.027719s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ip.txt
  HTTP 200, total 0.032782s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_yggdrasil_ip.txt
  HTTP 200, total 0.405244s
>>> https://cf.trackerslist.com/all.txt
  HTTP 200, total 0.103546s
>>> https://tracker.adysec.com/trackers_all.txt
  HTTP 200, total 0.205312s
>>> https://raw.githubusercontent.com/kris3713/UltimateBTTrackersList/refs/heads/master/ultimate_trackers.txt
  HTTP 200, total 0.115508s
>>> https://raw.githubusercontent.com/entr0pia/TrackersListCollection-S/refs/heads/master/https.txt
  HTTP 200, total 0.154161s
[INFO] public list https://cf.trackerslist.com/all.txt: 122 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all.txt: 72 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ip.txt: 53 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_udp.txt: 45 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_http.txt: 17 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_https.txt: 10 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ws.txt: 3 urls
[OK]   1466 new candidates -> candidates_20261017.txt
[OK]   1466 new candidates
[ERROR] No valid trackers found in response
[INFO] Repo: Pmwiu/Tracker-List, Max: 59
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/ngosang/trackerslist/master/blacklist.txt (391 URLs)
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/blacklist.txt (20 URLs)
[INFO] URL blacklist: 389 URLs (dynamic + remote sources)
[INFO] Protected hosts (防误杀): 14
[INFO] discovered candidates: 1248 URLs in 1 file(s)

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

[INFO] all 合并贡献: ngosang-all=50, ngosang-all-ip=49, ngosang-yggdrasil-ip=0, cf-all=15, adysec-all=35, kris3713-ultimate=5, entr0pia-https=2
[INFO] all 协议分布: http=116, https=18, udp=65, wss=1, ws=0

[OK]   merged: 200
[OK]   source_counts.json (200)
[OK]   discovered_set.json (1248)
[OK]   MIRRORS.txt
[OK]   /s/all
[OK]   index.html
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
  [ALIVE] (3/320) http://004430.xyz:80/announce 38ms — announce with peers:1
  [ALIVE] (9/320) http://107.189.2.131:1337/announce 584ms — announce with peers:1
  [DEAD]  (25/320) http://107.150.14.110:6969/announce — URLError: <urlopen error timed out>
  [ALIVE] (40/320) http://1337.abcvg.info:80/announce 233ms — announce with peers:1
  [ALIVE] (41/320) http://138.186.10.167:1337/announce 296ms — announce with peers:1
  [ALIVE] (43/320) http://140.235.237.23:6969/announce 334ms — announce with peers:1
  [DEAD]  (50/320) http://113.16.153.192:6969/announce — URLError: <urlopen error timed out>
  [ALIVE] (58/320) http://207.241.226.111:6969/announce 6ms — announce with peers:1
  [ALIVE] (59/320) http://207.241.231.226:6969/announce 9ms — announce with peers:1
  [ALIVE] (61/320) http://185.126.65.92:6969/announce 302ms — announce without peers
  [ALIVE] (62/320) http://211.75.205.187:6969/announce 283ms — announce with peers:1
  [ALIVE] (63/320) http://211.75.205.187:80/announce 278ms — announce with peers:1
  [ALIVE] (64/320) http://216.144.239.90:6969/announce 39ms — announce with peers:1
  [ALIVE] (65/320) http://211.75.205.188:6969/announce 277ms — announce with peers:1
  [ALIVE] (66/320) http://43.250.54.126:6969/announce 291ms — announce with peers:1
  [ALIVE] (67/320) http://93.158.213.92:1337/announce 293ms — announce with peers:1
  [ALIVE] (68/320) http://94.23.207.177:6969/announce 297ms — announce with peers:1
  [ALIVE] (69/320) http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 305ms — announce with peers:1
  [ALIVE] (70/320) http://announce.sktorrent.eu:6969/announce 452ms — announce with peers:1
  [ALIVE] (71/320) http://ipv4announce.sktorrent.eu:6969/announce 295ms — announce with peers:1
  [ALIVE] (72/320) http://open.tracker.cl:1337/announce 402ms — announce with peers:1
  [ALIVE] (73/320) http://retracker01-msk-virt.corbina.net:80/announce 554ms — announce with peers:1
  [ALIVE] (74/320) http://tr.nyacat.pw:80/announce 155ms — announce without peers
  [ALIVE] (75/320) http://t.overflow.biz:6969/announce 407ms — announce with peers:1
  [ALIVE] (88/320) https://004430.xyz:443/announce 47ms — announce with peers:1
  [ALIVE] (90/320) http://tracker.waaa.moe:6969/announce 38ms — announce with peers:1
  [ALIVE] (93/320) https://t.213891.xyz:443/announce 17ms — announce without peers
  [ALIVE] (96/320) http://tracker.dhitechnical.com:6969/announce 219ms — announce with peers:1
  [ALIVE] (97/320) https://open.ftorrent.com:443/announce 89ms — announce without peers
  [ALIVE] (99/320) https://1.tracker.eu.org:443/announce 24ms — announce without peers
  [DEAD]  (100/320) http://151.115.49.115:1337/announce — URLError: <urlopen error timed out>
  [ALIVE] (101/320) http://tracker.renfei.net:8080/announce 162ms — announce with peers:1
  [ALIVE] (102/320) http://tracker.dler.org:6969/announce 299ms — announce with peers:1
  [ALIVE] (105/320) http://tracker.zhuqiy.dgj055.icu:80/announce 353ms — announce without peers
  [ALIVE] (106/320) http://tracker.mywaifu.best:6969/announce 375ms — announce without peers
  [ALIVE] (107/320) https://tr.nyacat.pw:443/announce 167ms — announce without peers
  [ALIVE] (109/320) http://tracker2.dler.org:80/announce 431ms — announce with peers:1
  [ALIVE] (110/320) http://tracker.qu.ax:6969/announce 296ms — announce with peers:1
  [ALIVE] (112/320) https://tracker.7471.top:443/announce 187ms — announce without peers
  [ALIVE] (114/320) udp://149.106.106.25:443/announce 28ms — valid connect + announce (v4)
  [ALIVE] (115/320) https://tracker.zhuqiy.com:443/announce 108ms — announce with peers:1
  [ALIVE] (116/320) http://tracker.dler.com:6969/announce 306ms — announce with peers:1
  [ALIVE] (117/320) udp://180.131.145.175:6969/announce 15ms — valid connect + announce (v4)
  [ALIVE] (118/320) https://tracker.foreverpirates.co:443/announce 232ms — announce without peers
  [ALIVE] (119/320) http://tracker.opentrackr.org:1337/announce 447ms — announce with peers:1
  [ALIVE] (120/320) udp://164.152.110.70:6969/announce 48ms — valid connect + announce (v4)
  [ALIVE] (121/320) https://tracker.midnightprogrammer.net:443/announce 286ms — announce without peers
  [ALIVE] (122/320) udp://192.99.100.68:6969/announce 68ms — valid connect + announce (v4)
  [ALIVE] (123/320) udp://109.201.134.183:80/announce 146ms — valid connect + announce (v4)
  [ALIVE] (124/320) udp://23.157.120.14:6969/announce 3ms — valid connect + announce (v4)
  [ALIVE] (125/320) udp://23.94.174.203:1337/announce 8ms — valid connect + announce (v4)
  [ALIVE] (127/320) udp://135.125.198.235:1984/announce 159ms — valid connect + announce (v4)
  [ALIVE] (128/320) udp://160.30.240.158:1337/announce 143ms — valid connect + announce (v4)
  [ALIVE] (129/320) udp://151.242.104.187:80/announce 151ms — valid connect + announce (v4)
  [ALIVE] (130/320) udp://178.239.19.29:80/announce 148ms — valid connect + announce (v4)
  [ALIVE] (131/320) udp://15.235.207.99:8081/announce 173ms — valid connect + announce (v4)
  [ALIVE] (132/320) udp://185.121.168.96:1337/announce 147ms — valid connect + announce (v4)
  [ALIVE] (133/320) udp://34.66.57.33:1337/announce 47ms — valid connect + announce (v4)
  [ALIVE] (134/320) udp://34.66.57.33:80/announce 47ms — valid connect + announce (v4)
  [ALIVE] (136/320) udp://185.216.179.62:25/announce 153ms — valid connect + announce (v4)
  [ALIVE] (137/320) udp://211.75.205.187:6969/announce 138ms — valid connect + announce (v4)
  [ALIVE] (139/320) udp://107.189.2.131:1337/announce 245ms — valid connect + announce (v4)
  [ALIVE] (140/320) udp://211.75.205.187:80/announce 138ms — valid connect + announce (v4)
  [ALIVE] (141/320) udp://193.187.90.12:6969/announce 165ms — valid connect + announce (v4)
  [ALIVE] (142/320) https://tracker.nekomi.cn:443/announce 46ms — announce with peers:1
  [ALIVE] (143/320) udp://51.222.82.36:6969/announce 68ms — valid connect + announce (v4)
  [ALIVE] (145/320) udp://74.81.245.60:2010/announce 49ms — valid connect + announce (v4)
  [ALIVE] (146/320) udp://74.119.149.136:6969/announce 69ms — valid connect + announce (v4)
  [ALIVE] (148/320) udp://212.42.38.197:6969/announce 199ms — valid connect + announce (v4)
  [ALIVE] (149/320) udp://43.250.54.126:6969/announce 151ms — valid connect + announce (v4)
  [ALIVE] (150/320) udp://38.180.157.12:2715/announce 155ms — valid connect + announce (v4)
  [ALIVE] (151/320) udp://31.56.179.159:6969/announce 172ms — valid connect + announce (v4)
  [ALIVE] (152/320) udp://47.76.201.250:6969/announce 146ms — valid connect + announce (v4)
  [ALIVE] (153/320) udp://explodie.org:6969/announce 3ms — valid connect + announce (v4)
  [ALIVE] (154/320) udp://45.38.170.167:6969/announce 169ms — valid connect + announce (v4)
  [ALIVE] (155/320) udp://65.109.28.17:6969/announce 174ms — valid connect + announce (v4)
  [ALIVE] (157/320) udp://65.109.28.33:6969/announce 175ms — valid connect + announce (v4)
  [ALIVE] (158/320) udp://91.216.110.53:451/announce 157ms — valid connect + announce (v4)
  [ALIVE] (160/320) udp://93.158.213.92:1337/announce 146ms — valid connect + announce (v4)
  [ALIVE] (161/320) udp://60.172.236.18:6969/announce 199ms — valid connect + announce (v4)
  [ALIVE] (162/320) udp://93.158.213.92:6969/announce 145ms — valid connect + announce (v4)
  [ALIVE] (163/320) udp://94.23.207.177:6969/announce 148ms — valid connect + announce (v4)
  [ALIVE] (164/320) udp://open.ftorrent.com:443/announce 28ms — valid connect + announce (v4)
  [ALIVE] (165/320) udp://83.102.180.21:80/announce 199ms — valid connect + announce (v4)
  [ALIVE] (166/320) udp://seedpeer.net:6969/announce 17ms — valid connect + announce (v4)
  [ALIVE] (167/320) udp://95.217.80.20:6969/announce 169ms — valid connect + announce (v4)
  [ALIVE] (168/320) udp://evan.im:6969/announce 69ms — valid connect + announce (v4)
  [ALIVE] (169/320) udp://tracker.004430.xyz:1337/announce 8ms — valid connect + announce (v4)
  [ALIVE] (170/320) udp://ipv4announce.sktorrent.eu:6969/announce 146ms — valid connect + announce (v4)
  [ALIVE] (171/320) udp://kolankoalastree.newtrackon.co.nz:1337/announce 143ms — valid connect + announce (v4)
  [ALIVE] (172/320) udp://ns575949.ip-51-222-82.net:6969/announce 67ms — valid connect + announce (v4)
  [ALIVE] (173/320) udp://tr.btube3.com:2010/announce 58ms — valid connect + announce (v4)
  [ALIVE] (174/320) udp://open.demonii.com:1337/announce 131ms — valid connect + announce (v4)
  [DEAD]  (175/320) wss://tracker.openwebtorrent.com:443/announce — SSLError: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1010)
  [ALIVE] (176/320) udp://admin.52ywp.com:6969/announce 224ms — valid connect + announce (v4)
  [ALIVE] (177/320) udp://bt-tracker.de:6969/announce 139ms — valid connect + announce (v4)
  [ALIVE] (178/320) udp://tr4ck3r.duckdns.org:6969/announce 66ms — valid connect + announce (v4)
  [ALIVE] (179/320) udp://open.stealth.si:80/announce 153ms — valid connect + announce (v4)
  [ALIVE] (180/320) udp://mail.segso.net:6969/announce 174ms — valid connect + announce (v4)
  [ALIVE] (181/320) udp://t.overflow.biz:6969/announce 168ms — valid connect + announce (v4)
  [ALIVE] (182/320) udp://retracker01-msk-virt.corbina.net:80/announce 186ms — valid connect + announce (v4)
  [ALIVE] (183/320) udp://tracker-udp.gbitt.info:80/announce 149ms — valid connect + announce (v4)
  [ALIVE] (184/320) udp://tr3.ysagin.top:2715/announce 154ms — valid connect + announce (v4)
  [ALIVE] (185/320) udp://martin-gebhardt.eu:25/announce 156ms — valid connect + announce (v4)
  [ALIVE] (186/320) udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 463ms — valid connect + announce (v4)
  [ALIVE] (190/320) udp://tracker.aruku.ovh:8081/announce 177ms — valid connect + announce (v4)
  [DEAD]  (200/320) http://bt.3kb.xyz:80/announce — URLError: <urlopen error [Errno -2] Name or service not known>
  [ALIVE] (202/320) udp://edgev.duckdns.org:6969/announce 184ms — valid connect + announce (v4)
  [ALIVE] (224/320) http://h4.trakx.nibba.trade:80/announce 98ms — announce with peers:1
  [DEAD]  (225/320) http://highteahop.top:6960/announce — RemoteDisconnected: Remote end closed connection without response
  [DEAD]  (250/320) http://504e163a.host.njalla.net:6969/announce — URLError: <urlopen error [Errno 101] Network is unreachable>
  [SKIP]   (275/320) http://opentracker.eeptorrent.i2p:80/a — I2P network required
  [ALIVE] (282/320) http://opentracker.xyz:80/announce 885ms — announce with peers:1
  [DEAD]  (300/320) http://servandroidkino.ru:80/announce — URLError: <urlopen error [Errno -2] Name or service not known>

[INFO] First pass done in 91.9s
[INFO] Multi-sample: 3 samples on top 50 alive trackers...
[INFO] Multi-sample refined 49 trackers (median + jitter penalty)
[INFO] Same-subnet(/24) dedup removed 49 slower tracker(s)
[INFO] scrape probe: 19 http/https alive trackers
[INFO] scrape: 5 responded, 3 with seeders
[INFO] discovered candidates excluded from all: 1248

===== Test Summary =====
  Total tested:   320
  Alive (raw):    56
  All (final):    0 (top 59 by composite score)
  Unsafe filtered:5
  Low-speed:      0 (>5s excluded)
  Same-subnet dedup:  49 (kept faster)
  Dead final:     253
  Time:           107.5s
=== 协议分布统计 ===
  HTTP  : 34 个
  HTTPS : 10 个
  UDP   : 61 个
  WSS   : 0 个
  WS    : 0 个
  总计: 105 个（存活）
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
 Round 1 - 2026-10-17 02:22:22
============================================================
  [PASS] Local tracker: trackers_ngosang_all.txt: 75 trackers
  [PASS] Local tracker: trackers_ngosang_all_ip.txt: 51 trackers
  [FAIL] Local tracker: trackers_ngosang_yggdrasil_ip.txt: missing
  [PASS] Local tracker: trackers_cf_all.txt: 106 trackers
  [PASS] Local tracker: trackers_adysec_all.txt: 3285 trackers
  [PASS] Local tracker: trackers_kris3713_ultimate.txt: 162 trackers
  [PASS] Local tracker: trackers_entr0pia_https.txt: 16 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [FAIL] Local tracker: trackers_all.txt: empty
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1466 candidates in 1 file(s)
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /all.txt: 0 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_all.txt: 75 trackers
  [PASS] Plain text: /ngosang_all_ip.txt: 51 trackers
  [FAIL] Plain text: /ngosang_yggdrasil_ip.txt: missing
  [PASS] Plain text: /cf_all.txt: 106 trackers
  [PASS] Plain text: /adysec_all.txt: 3285 trackers
  [PASS] Plain text: /kris3713_ultimate.txt: 162 trackers
  [PASS] Plain text: /entr0pia_https.txt: 16 trackers
  [PASS] Plain text: /udp.txt: 65 trackers
  [PASS] Plain text: /http.txt: 116 trackers
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
  Result: 42 passed, 1 warnings, 3 failed
============================================================

############################################################
 FINAL REPORT: 1 rounds completed
   Total PASS: 42
   Total WARN: 1
   Total FAIL: 3
   STATUS: ISSUES DETECTED
############################################################

============================================================
 Round 1 - 2026-10-17 02:22:45
============================================================
  [PASS] Local tracker: trackers_ngosang_all.txt: 75 trackers
  [PASS] Local tracker: trackers_ngosang_all_ip.txt: 51 trackers
  [FAIL] Local tracker: trackers_ngosang_yggdrasil_ip.txt: missing
  [PASS] Local tracker: trackers_cf_all.txt: 106 trackers
  [PASS] Local tracker: trackers_adysec_all.txt: 3285 trackers
  [PASS] Local tracker: trackers_kris3713_ultimate.txt: 162 trackers
  [PASS] Local tracker: trackers_entr0pia_https.txt: 16 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [FAIL] Local tracker: trackers_all.txt: empty
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1466 candidates in 1 file(s)
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /all.txt: 0 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_all.txt: 75 trackers
  [PASS] Plain text: /ngosang_all_ip.txt: 51 trackers
  [FAIL] Plain text: /ngosang_yggdrasil_ip.txt: missing
  [PASS] Plain text: /cf_all.txt: 106 trackers
  [PASS] Plain text: /adysec_all.txt: 3285 trackers
  [PASS] Plain text: /kris3713_ultimate.txt: 162 trackers
  [PASS] Plain text: /entr0pia_https.txt: 16 trackers
  [PASS] Plain text: /udp.txt: 65 trackers
  [PASS] Plain text: /http.txt: 116 trackers
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
  [FAIL] Worker all 短链: 0 trackers (empty)
  [PASS] Worker all 加速: HTTP 200, 55 trackers
------------------------------------------------------------
  Result: 46 passed, 1 warnings, 4 failed
============================================================

============================================================
 Round 2 - 2026-10-17 02:22:50
============================================================
  [PASS] Local tracker: trackers_ngosang_all.txt: 75 trackers
  [PASS] Local tracker: trackers_ngosang_all_ip.txt: 51 trackers
  [FAIL] Local tracker: trackers_ngosang_yggdrasil_ip.txt: missing
  [PASS] Local tracker: trackers_cf_all.txt: 106 trackers
  [PASS] Local tracker: trackers_adysec_all.txt: 3285 trackers
  [PASS] Local tracker: trackers_kris3713_ultimate.txt: 162 trackers
  [PASS] Local tracker: trackers_entr0pia_https.txt: 16 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [FAIL] Local tracker: trackers_all.txt: empty
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1466 candidates in 1 file(s)
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /all.txt: 0 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_all.txt: 75 trackers
  [PASS] Plain text: /ngosang_all_ip.txt: 51 trackers
  [FAIL] Plain text: /ngosang_yggdrasil_ip.txt: missing
  [PASS] Plain text: /cf_all.txt: 106 trackers
  [PASS] Plain text: /adysec_all.txt: 3285 trackers
  [PASS] Plain text: /kris3713_ultimate.txt: 162 trackers
  [PASS] Plain text: /entr0pia_https.txt: 16 trackers
  [PASS] Plain text: /udp.txt: 65 trackers
  [PASS] Plain text: /http.txt: 116 trackers
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
  [FAIL] Worker all 短链: 0 trackers (empty)
  [PASS] Worker all 加速: HTTP 200, 55 trackers
------------------------------------------------------------
  Result: 46 passed, 1 warnings, 4 failed
============================================================

============================================================
 Round 3 - 2026-10-17 02:22:56
============================================================
  [PASS] Local tracker: trackers_ngosang_all.txt: 75 trackers
  [PASS] Local tracker: trackers_ngosang_all_ip.txt: 51 trackers
  [FAIL] Local tracker: trackers_ngosang_yggdrasil_ip.txt: missing
  [PASS] Local tracker: trackers_cf_all.txt: 106 trackers
  [PASS] Local tracker: trackers_adysec_all.txt: 3285 trackers
  [PASS] Local tracker: trackers_kris3713_ultimate.txt: 162 trackers
  [PASS] Local tracker: trackers_entr0pia_https.txt: 16 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [FAIL] Local tracker: trackers_all.txt: empty
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1466 candidates in 1 file(s)
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /all.txt: 0 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_all.txt: 75 trackers
  [PASS] Plain text: /ngosang_all_ip.txt: 51 trackers
  [FAIL] Plain text: /ngosang_yggdrasil_ip.txt: missing
  [PASS] Plain text: /cf_all.txt: 106 trackers
  [PASS] Plain text: /adysec_all.txt: 3285 trackers
  [PASS] Plain text: /kris3713_ultimate.txt: 162 trackers
  [PASS] Plain text: /entr0pia_https.txt: 16 trackers
  [PASS] Plain text: /udp.txt: 65 trackers
  [PASS] Plain text: /http.txt: 116 trackers
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
  [FAIL] Worker all 短链: 0 trackers (empty)
  [PASS] Worker all 加速: HTTP 200, 55 trackers
------------------------------------------------------------
  Result: 46 passed, 1 warnings, 4 failed
============================================================

############################################################
 FINAL REPORT: 3 rounds completed
   Total PASS: 138
   Total WARN: 3
   Total FAIL: 12
   STATUS: ISSUES DETECTED
############################################################
=== End of diagnostics (Sat Oct 17 02:22:56 UTC 2026) ===
