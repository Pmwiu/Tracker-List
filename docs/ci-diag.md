=== Diagnostics Thu Oct  8 04:20:58 UTC 2026 ===
Python: Python 3.12.15
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://cf.trackerslist.com/best.txt
  HTTP 200, total 0.090971s
>>> https://trackers.run/s/rw_up_hp_hs_v4_v6.txt
  HTTP 200, total 0.426036s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.040541s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best_ip.txt
  HTTP 200, total 0.088439s
>>> https://raw.githubusercontent.com/1265578519/OpenTracker/refs/heads/master/tracker.txt
  HTTP 200, total 0.070198s
[INFO] Repo: Pmwiu/Tracker-List, Max: 20

[INFO] trackers_cf_best.txt (cf-best)
[OK]   71 unique

[INFO] trackers_run_best.txt (trackersrun-best)
[OK]   53 unique

[INFO] trackers_ngosang_best.txt (ngosang-best)
[OK]   20 unique

[INFO] trackers_ngosang_best_ip.txt (ngosang-best-ip)
[OK]   20 unique

[INFO] trackers_opentracker.txt (opentracker)
[OK]   38 unique

[INFO] all 合并贡献: cf-best=17, trackersrun-best=25, ngosang-best=20, ngosang-best-ip=20, opentracker=18

[OK]   merged: 100
[OK]   MIRRORS.txt
[OK]   /s/alive
[OK]   /s/all
[OK]   index.html
[OK]   docs/alive.txt
[OK]   docs/merged.txt
[OK]   docs/cf_best.txt
[OK]   docs/run_best.txt
[OK]   docs/ngosang_best.txt
[OK]   docs/ngosang_best_ip.txt
[OK]   docs/opentracker.txt
[OK]   docs/udp.txt
[OK]   docs/http.txt
[OK]   docs/https.txt
[OK]   docs/wss.txt
[OK]   docs/ws.txt

===== Summary =====
  trackers_cf_best.txt: 71
  trackers_run_best.txt: 53
  trackers_ngosang_best.txt: 20
  trackers_ngosang_best_ip.txt: 20
  trackers_opentracker.txt: 38
  trackers_merged.txt: 100
  alive capped at 20 after test+sort
===================
[INFO] Testing 100 candidates (all-pool=100, timeout=10s, workers=30)
[INFO] Max alive trackers after scoring: 20
  [ALIVE] (4/100) http://207.241.226.111:6969/announce 127ms — valid announce response
  [ALIVE] (5/100) http://207.241.231.226:6969/announce 139ms — valid announce response
  [ALIVE] (6/100) http://tracker.dhitechnical.com:6969/announce 146ms — valid announce response
  [ALIVE] (7/100) http://94.23.207.177:6969/announce 185ms — valid announce response
  [ALIVE] (8/100) http://107.189.2.131:1337/announce 207ms — valid announce response
  [ALIVE] (9/100) http://tracker.nyaa.vc:6969/announce 177ms — valid announce response
  [ALIVE] (11/100) http://ipv4announce.sktorrent.eu:6969/announce 180ms — valid announce response
  [ALIVE] (13/100) http://nyaa.tracker.wf:7777/announce 207ms — valid announce response
  [ALIVE] (14/100) http://announce.sktorrent.eu:6969/announce 191ms — valid announce response
  [ALIVE] (15/100) http://bt1.archive.org:6969/announce 128ms — valid announce response
  [ALIVE] (16/100) http://tracker.renfei.net:8080/announce 28ms — valid announce response
  [ALIVE] (17/100) http://1337.abcvg.info:80/announce 192ms — valid announce response
  [ALIVE] (19/100) http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 211ms — valid announce response
  [ALIVE] (20/100) https://t.213891.xyz:443/announce 52ms — valid announce response
  [ALIVE] (21/100) http://tracker.qu.ax:6969/announce 185ms — valid announce response
  [ALIVE] (23/100) http://tracker.auctor.tv:6969/announce 183ms — valid announce response
  [ALIVE] (24/100) http://211.75.205.187:6969/announce 373ms — valid announce response
  [ALIVE] (25/100) http://211.75.205.188:80/announce 373ms — valid announce response
  [ALIVE] (26/100) http://211.75.210.221:6969/announce 374ms — valid announce response
  [ALIVE] (27/100) http://211.75.210.221:80/announce 380ms — valid announce response
  [ALIVE] (28/100) http://bt2.archive.org:6969/announce 201ms — valid announce response
  [ALIVE] (29/100) https://004430.xyz:443/announce 159ms — valid announce response
  [ALIVE] (30/100) http://tracker.mywaifu.best:6969/announce 242ms — valid announce response
  [ALIVE] (31/100) https://1337.abcvg.info:443/announce 206ms — valid announce response
  [ALIVE] (32/100) https://tracker.7471.top:443/announce 140ms — valid announce response
  [ALIVE] (33/100) https://tr.nyacat.pw:443/announce 128ms — valid announce response
  [ALIVE] (34/100) https://tracker.foreverpirates.co:443/announce 160ms — valid announce response
  [ALIVE] (36/100) https://tracker.qingwapt.org:443/announce 163ms — online (failure reason)
  [ALIVE] (37/100) http://tracker.waaa.moe:6969/announce 240ms — valid announce response
  [ALIVE] (38/100) udp://109.201.134.183:80/announce 89ms — valid connect + announce
  [ALIVE] (39/100) https://1.tracker.eu.org:443/announce 59ms — valid announce response
  [ALIVE] (40/100) http://tracker.opentrackr.org:1337/announce 280ms — valid announce response
  [ALIVE] (41/100) udp://193.148.251.93:6969/announce 47ms — valid connect + announce
  [ALIVE] (42/100) udp://135.125.198.235:1984/announce 93ms — valid connect + announce
  [ALIVE] (43/100) http://tracker.dler.org:6969/announce 382ms — valid announce response
  [ALIVE] (44/100) http://tracker.dler.com:6969/announce 389ms — valid announce response
  [ALIVE] (45/100) http://retracker01-msk-virt.corbina.net:80/announce 406ms — valid announce response
  [ALIVE] (47/100) udp://151.242.104.187:80/announce 97ms — valid connect + announce
  [ALIVE] (48/100) udp://34.66.57.33:1337/announce 31ms — valid connect + announce
  [ALIVE] (49/100) udp://34.66.57.33:80/announce 31ms — valid connect + announce
  [DEAD]  (50/100) https://tracker1.520.jp:443/announce — HTTPError: HTTP Error 521: <none>
  [ALIVE] (51/100) udp://209.141.59.25:6969/announce 62ms — valid connect + announce
  [ALIVE] (52/100) https://tracker.zhuqiy.com:443/announce 232ms — valid announce response
  [ALIVE] (53/100) udp://132.226.6.145:6969/announce 152ms — valid connect + announce
  [ALIVE] (55/100) http://tracker2.dler.org:80/announce 490ms — valid announce response
  [ALIVE] (56/100) udp://193.34.92.5:80/announce 129ms — valid connect + announce
  [ALIVE] (57/100) https://tracker.nekomi.cn:443/announce 161ms — valid announce response
  [ALIVE] (58/100) udp://31.38.161.123:6969/announce 103ms — valid connect + announce
  [ALIVE] (59/100) http://tracker1.itzmx.com:8080/announce 403ms — valid announce response
  [ALIVE] (60/100) udp://185.121.168.96:1337/announce 174ms — valid connect + announce
  [ALIVE] (61/100) udp://43.250.54.126:6969/announce 89ms — valid connect + announce
  [ALIVE] (62/100) udp://45.137.199.107:6969/announce 88ms — valid connect + announce
  [ALIVE] (64/100) udp://31.56.179.159:6969/announce 117ms — valid connect + announce
  [ALIVE] (65/100) udp://93.158.213.92:1337/announce 91ms — valid connect + announce
  [ALIVE] (66/100) udp://93.158.213.92:6969/announce 89ms — valid connect + announce
  [ALIVE] (67/100) udp://89.234.156.205:451/announce 99ms — valid connect + announce
  [ALIVE] (68/100) udp://65.109.28.17:6969/announce 118ms — valid connect + announce
  [ALIVE] (70/100) udp://tracker.corpscorp.online:80/announce 31ms — valid connect + announce
  [ALIVE] (71/100) udp://tracker.bittor.pw:1337/announce 31ms — valid connect + announce
  [ALIVE] (72/100) udp://95.217.80.20:6969/announce 121ms — valid connect + announce
  [ALIVE] (73/100) udp://211.75.210.221:80/announce 187ms — valid connect + announce
  [ALIVE] (74/100) udp://83.102.180.21:80/announce 135ms — valid connect + announce
  [ALIVE] (75/100) udp://open.stealth.si:80/announce 97ms — valid connect + announce
  [ALIVE] (76/100) udp://tracker.nyaa.vc:6969/announce 90ms — valid connect + announce
  [ALIVE] (77/100) udp://tracker.ducks.party:1984/announce 92ms — valid connect + announce
  [ALIVE] (78/100) udp://tracker-udp.gbitt.info:80/announce 90ms — valid connect + announce
  [ALIVE] (79/100) udp://tracker.qu.ax:6969/announce 88ms — valid connect + announce
  [ALIVE] (80/100) udp://tracker.opentrackr.org:1337/announce 89ms — valid connect + announce
  [ALIVE] (81/100) udp://exodus.desync.com:6969/announce 70ms — valid connect + announce
  [ALIVE] (82/100) udp://retracker01-msk-virt.corbina.net:80/announce 134ms — valid connect + announce
  [ALIVE] (83/100) udp://tracker.gmi.gd:6969/announce 62ms — valid connect + announce
  [ALIVE] (84/100) udp://explodie.org:6969/announce 106ms — valid connect + announce
  [ALIVE] (85/100) https://tracker.midnightprogrammer.net:443/announce 831ms — valid announce response
  [ALIVE] (86/100) udp://open.demonii.com:1337/announce 174ms — valid connect + announce
  [ALIVE] (87/100) udp://tracker.skynetcloud.site:6969/announce 92ms — valid connect + announce
  [ALIVE] (88/100) udp://tracker2.dler.org:80/announce 184ms — valid connect + announce
  [ALIVE] (90/100) udp://tracker.torrent.eu.org:451/announce 113ms — valid connect + announce
  [ALIVE] (91/100) udp://23.157.120.14:6969/announce 107ms — valid connect (announce not confirmed)
  [DEAD]  (100/100) udp://tracker.tryhackx.org:6969/announce — no connect response

[INFO] First pass done in 11.0s
[INFO] Second pass: re-testing top 77 alive trackers...
[INFO] Second pass done, refined 77 trackers
[INFO] Same-IP dedup removed 32 slower tracker(s)

===== Test Summary =====
  Total tested:   100
  Alive (raw):    45
  Alive (final):  20 (top 20 by composite score)
  Non-UDP kept:   4 (quota >= 4)
  Score-capped:   25
  Unsafe filtered:0
  Low-speed:      0 (>5s excluded)
  Same-IP dedup:  32 (kept faster)
  Dead final:     77
  Time:           14.4s
=== 协议分布统计 ===
  HTTP  : 28 个
  HTTPS : 11 个
  UDP   : 38 个
  WSS   : 0 个
  WS    : 0 个
  总计: 77 个（存活）
=========================
[OK]   /s/alive
[OK]   /s/all
[OK]   index.html
[OK] Pages regenerated with alive statistics.
[OK]   docs/alive.txt
[OK]   docs/merged.txt
[OK]   docs/cf_best.txt
[OK]   docs/run_best.txt
[OK]   docs/ngosang_best.txt
[OK]   docs/ngosang_best_ip.txt
[OK]   docs/opentracker.txt
[OK]   docs/udp.txt
[OK]   docs/http.txt
[OK]   docs/https.txt
[OK]   docs/wss.txt
[OK]   docs/ws.txt
[OK] Plain-text files synced to docs/.

============================================================
 Round 1 - 2026-10-08 04:21:15
============================================================
  [PASS] Local tracker: trackers_cf_best.txt: 71 trackers
  [PASS] Local tracker: trackers_run_best.txt: 53 trackers
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 38 trackers
  [PASS] Local tracker: trackers_merged.txt: 100 trackers
  [PASS] Local tracker: trackers_alive.txt: 20 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 20 trackers
  [PASS] Plain text: /merged.txt: 100 trackers
  [PASS] Plain text: /cf_best.txt: 71 trackers
  [PASS] Plain text: /run_best.txt: 53 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /opentracker.txt: 38 trackers
  [PASS] Plain text: /udp.txt: 42 trackers
  [PASS] Plain text: /http.txt: 41 trackers
  [PASS] Plain text: /https.txt: 17 trackers
  [PASS] Plain text: /wss.txt: 0 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 20 in [0, 20]
  [PASS] Merged dedup check: 100 unique
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_cf_best.txt vs cf_best.txt: identical
  [PASS] Consistency: trackers_run_best.txt vs run_best.txt: identical
  [PASS] Consistency: trackers_ngosang_best.txt vs ngosang_best.txt: identical
  [PASS] Consistency: trackers_ngosang_best_ip.txt vs ngosang_best_ip.txt: identical
  [PASS] Consistency: trackers_opentracker.txt vs opentracker.txt: identical
  [PASS] Consistency: trackers_udp.txt vs udp.txt: identical
  [PASS] Consistency: trackers_http.txt vs http.txt: identical
  [PASS] Consistency: trackers_https.txt vs https.txt: identical
  [PASS] Consistency: trackers_wss.txt vs wss.txt: identical
  [PASS] Consistency: trackers_ws.txt vs ws.txt: identical
  [PASS] URL format check: all 100 valid
------------------------------------------------------------
  Result: 41 passed, 0 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 1 rounds completed
   Total PASS: 41
   Total WARN: 0
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################

============================================================
 Round 1 - 2026-10-08 04:21:22
============================================================
  [PASS] Local tracker: trackers_cf_best.txt: 71 trackers
  [PASS] Local tracker: trackers_run_best.txt: 53 trackers
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 38 trackers
  [PASS] Local tracker: trackers_merged.txt: 100 trackers
  [PASS] Local tracker: trackers_alive.txt: 20 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 20 trackers
  [PASS] Plain text: /merged.txt: 100 trackers
  [PASS] Plain text: /cf_best.txt: 71 trackers
  [PASS] Plain text: /run_best.txt: 53 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /opentracker.txt: 38 trackers
  [PASS] Plain text: /udp.txt: 42 trackers
  [PASS] Plain text: /http.txt: 41 trackers
  [PASS] Plain text: /https.txt: 17 trackers
  [PASS] Plain text: /wss.txt: 0 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 20 in [0, 20]
  [PASS] Merged dedup check: 100 unique
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_cf_best.txt vs cf_best.txt: identical
  [PASS] Consistency: trackers_run_best.txt vs run_best.txt: identical
  [PASS] Consistency: trackers_ngosang_best.txt vs ngosang_best.txt: identical
  [PASS] Consistency: trackers_ngosang_best_ip.txt vs ngosang_best_ip.txt: identical
  [PASS] Consistency: trackers_opentracker.txt vs opentracker.txt: identical
  [PASS] Consistency: trackers_udp.txt vs udp.txt: identical
  [PASS] Consistency: trackers_http.txt vs http.txt: identical
  [PASS] Consistency: trackers_https.txt vs https.txt: identical
  [PASS] Consistency: trackers_wss.txt vs wss.txt: identical
  [PASS] Consistency: trackers_ws.txt vs ws.txt: identical
  [PASS] URL format check: all 100 valid
  [PASS] Raw: alive (Raw): HTTP 200, 20 trackers
  [PASS] Raw: merged (Raw): HTTP 200, 100 trackers
  [PASS] Pages: /alive.txt: HTTP 200, 20 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 100 trackers
  [PASS] Pages short: /s/alive: HTTP 200, redirect OK
  [PASS] Pages short: /s/all: HTTP 200, redirect OK
  [PASS] Worker best 短链: HTTP 200, 20 trackers
  [PASS] Worker all 短链: HTTP 200, 100 trackers
  [PASS] Worker best 加速: HTTP 200, 20 trackers
  [PASS] Worker all 加速: HTTP 200, 100 trackers
------------------------------------------------------------
  Result: 51 passed, 0 warnings, 0 failed
============================================================

============================================================
 Round 2 - 2026-10-08 04:21:27
============================================================
  [PASS] Local tracker: trackers_cf_best.txt: 71 trackers
  [PASS] Local tracker: trackers_run_best.txt: 53 trackers
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 38 trackers
  [PASS] Local tracker: trackers_merged.txt: 100 trackers
  [PASS] Local tracker: trackers_alive.txt: 20 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 20 trackers
  [PASS] Plain text: /merged.txt: 100 trackers
  [PASS] Plain text: /cf_best.txt: 71 trackers
  [PASS] Plain text: /run_best.txt: 53 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /opentracker.txt: 38 trackers
  [PASS] Plain text: /udp.txt: 42 trackers
  [PASS] Plain text: /http.txt: 41 trackers
  [PASS] Plain text: /https.txt: 17 trackers
  [PASS] Plain text: /wss.txt: 0 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 20 in [0, 20]
  [PASS] Merged dedup check: 100 unique
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_cf_best.txt vs cf_best.txt: identical
  [PASS] Consistency: trackers_run_best.txt vs run_best.txt: identical
  [PASS] Consistency: trackers_ngosang_best.txt vs ngosang_best.txt: identical
  [PASS] Consistency: trackers_ngosang_best_ip.txt vs ngosang_best_ip.txt: identical
  [PASS] Consistency: trackers_opentracker.txt vs opentracker.txt: identical
  [PASS] Consistency: trackers_udp.txt vs udp.txt: identical
  [PASS] Consistency: trackers_http.txt vs http.txt: identical
  [PASS] Consistency: trackers_https.txt vs https.txt: identical
  [PASS] Consistency: trackers_wss.txt vs wss.txt: identical
  [PASS] Consistency: trackers_ws.txt vs ws.txt: identical
  [PASS] URL format check: all 100 valid
  [PASS] Raw: alive (Raw): HTTP 200, 20 trackers
  [PASS] Raw: merged (Raw): HTTP 200, 100 trackers
  [PASS] Pages: /alive.txt: HTTP 200, 20 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 100 trackers
  [PASS] Pages short: /s/alive: HTTP 200, redirect OK
  [PASS] Pages short: /s/all: HTTP 200, redirect OK
  [PASS] Worker best 短链: HTTP 200, 20 trackers
  [PASS] Worker all 短链: HTTP 200, 100 trackers
  [PASS] Worker best 加速: HTTP 200, 20 trackers
  [PASS] Worker all 加速: HTTP 200, 100 trackers
------------------------------------------------------------
  Result: 51 passed, 0 warnings, 0 failed
============================================================

============================================================
 Round 3 - 2026-10-08 04:21:32
============================================================
  [PASS] Local tracker: trackers_cf_best.txt: 71 trackers
  [PASS] Local tracker: trackers_run_best.txt: 53 trackers
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 38 trackers
  [PASS] Local tracker: trackers_merged.txt: 100 trackers
  [PASS] Local tracker: trackers_alive.txt: 20 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 20 trackers
  [PASS] Plain text: /merged.txt: 100 trackers
  [PASS] Plain text: /cf_best.txt: 71 trackers
  [PASS] Plain text: /run_best.txt: 53 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /opentracker.txt: 38 trackers
  [PASS] Plain text: /udp.txt: 42 trackers
  [PASS] Plain text: /http.txt: 41 trackers
  [PASS] Plain text: /https.txt: 17 trackers
  [PASS] Plain text: /wss.txt: 0 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 20 in [0, 20]
  [PASS] Merged dedup check: 100 unique
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_cf_best.txt vs cf_best.txt: identical
  [PASS] Consistency: trackers_run_best.txt vs run_best.txt: identical
  [PASS] Consistency: trackers_ngosang_best.txt vs ngosang_best.txt: identical
  [PASS] Consistency: trackers_ngosang_best_ip.txt vs ngosang_best_ip.txt: identical
  [PASS] Consistency: trackers_opentracker.txt vs opentracker.txt: identical
  [PASS] Consistency: trackers_udp.txt vs udp.txt: identical
  [PASS] Consistency: trackers_http.txt vs http.txt: identical
  [PASS] Consistency: trackers_https.txt vs https.txt: identical
  [PASS] Consistency: trackers_wss.txt vs wss.txt: identical
  [PASS] Consistency: trackers_ws.txt vs ws.txt: identical
  [PASS] URL format check: all 100 valid
  [PASS] Raw: alive (Raw): HTTP 200, 20 trackers
  [PASS] Raw: merged (Raw): HTTP 200, 100 trackers
  [PASS] Pages: /alive.txt: HTTP 200, 20 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 100 trackers
  [PASS] Pages short: /s/alive: HTTP 200, redirect OK
  [PASS] Pages short: /s/all: HTTP 200, redirect OK
  [PASS] Worker best 短链: HTTP 200, 20 trackers
  [PASS] Worker all 短链: HTTP 200, 100 trackers
  [PASS] Worker best 加速: HTTP 200, 20 trackers
  [PASS] Worker all 加速: HTTP 200, 100 trackers
------------------------------------------------------------
  Result: 51 passed, 0 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 3 rounds completed
   Total PASS: 153
   Total WARN: 0
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################
=== End of diagnostics (Thu Oct  8 04:21:32 UTC 2026) ===
