=== Diagnostics Thu Oct  8 04:34:11 UTC 2026 ===
Python: Python 3.12.15
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://cf.trackerslist.com/best.txt
  HTTP 200, total 0.122363s
>>> https://trackers.run/s/rw_up_hp_hs_v4_v6.txt
  HTTP 200, total 0.629235s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.115672s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best_ip.txt
  HTTP 200, total 0.128645s
>>> https://raw.githubusercontent.com/1265578519/OpenTracker/refs/heads/master/tracker.txt
  HTTP 200, total 0.309930s
[INFO] Repo: Pmwiu/Tracker-List, Max: 20

[INFO] trackers_cf_best.txt (cf-best)
[OK]   71 unique

[INFO] trackers_run_best.txt (trackersrun-best)
[OK]   52 unique

[INFO] trackers_ngosang_best.txt (ngosang-best)
[OK]   20 unique

[INFO] trackers_ngosang_best_ip.txt (ngosang-best-ip)
[OK]   20 unique

[INFO] trackers_opentracker.txt (opentracker)
[OK]   38 unique

[INFO] all 合并贡献: cf-best=49, trackersrun-best=11, ngosang-best=10, ngosang-best-ip=19, opentracker=11
[INFO] all 协议分布: http=36, https=16, udp=47, wss=1, ws=0

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
  trackers_run_best.txt: 52
  trackers_ngosang_best.txt: 20
  trackers_ngosang_best_ip.txt: 20
  trackers_opentracker.txt: 38
  trackers_merged.txt: 100
  alive capped at 20 after test+sort
===================
[INFO] Testing 100 candidates (all-pool=100, timeout=10s, workers=30)
[INFO] Max alive trackers after scoring: 20
  [ALIVE] (3/100) http://207.241.226.111:6969/announce 39ms — valid announce response
  [ALIVE] (4/100) http://207.241.231.226:6969/announce 44ms — valid announce response
  [ALIVE] (6/100) http://bt1.archive.org:6969/announce 57ms — valid announce response
  [ALIVE] (8/100) http://tracker.waaa.moe:6969/announce 124ms — valid announce response
  [ALIVE] (9/100) https://004430.xyz:443/announce 42ms — valid announce response
  [ALIVE] (10/100) http://tracker.dhitechnical.com:6969/announce 205ms — valid announce response
  [ALIVE] (11/100) http://211.75.210.221:80/announce 281ms — valid announce response
  [ALIVE] (12/100) http://1337.abcvg.info:80/announce 253ms — valid announce response
  [ALIVE] (13/100) http://211.75.205.187:6969/announce 288ms — valid announce response
  [ALIVE] (14/100) http://211.75.205.188:80/announce 288ms — valid announce response
  [ALIVE] (15/100) http://211.75.210.221:6969/announce 287ms — valid announce response
  [ALIVE] (16/100) http://94.23.207.177:6969/announce 288ms — valid announce response
  [ALIVE] (17/100) http://ipv4announce.sktorrent.eu:6969/announce 289ms — valid announce response
  [ALIVE] (18/100) https://t.213891.xyz:443/announce 42ms — valid announce response
  [ALIVE] (19/100) http://tracker.mywaifu.best:6969/announce 307ms — valid announce response
  [ALIVE] (20/100) http://107.189.2.131:1337/announce 369ms — valid announce response
  [ALIVE] (23/100) http://announce.sktorrent.eu:6969/announce 347ms — valid announce response
  [ALIVE] (25/100) https://1337.abcvg.info:443/announce 279ms — valid announce response
  [ALIVE] (26/100) https://tr.nyacat.pw:443/announce 181ms — valid announce response
  [ALIVE] (27/100) http://tracker.dler.org:6969/announce 286ms — valid announce response
  [ALIVE] (28/100) http://tracker.qu.ax:6969/announce 298ms — valid announce response
  [ALIVE] (29/100) https://tracker.foreverpirates.co:443/announce 227ms — valid announce response
  [ALIVE] (30/100) https://tracker.7471.top:443/announce 193ms — valid announce response
  [ALIVE] (31/100) udp://209.141.59.25:6969/announce 17ms — valid connect + announce
  [ALIVE] (32/100) http://tracker.auctor.tv:6969/announce 274ms — valid announce response
  [ALIVE] (33/100) udp://208.83.20.20:6969/announce 31ms — valid connect + announce
  [ALIVE] (34/100) udp://23.157.120.14:6969/announce 28ms — valid connect + announce
  [ALIVE] (36/100) http://nyaa.tracker.wf:7777/announce 466ms — valid announce response
  [ALIVE] (37/100) http://tracker.opentrackr.org:1337/announce 483ms — valid announce response
  [ALIVE] (38/100) https://tracker.qingwapt.org:443/announce 240ms — online (failure reason)
  [ALIVE] (39/100) https://tracker.midnightprogrammer.net:443/announce 300ms — valid announce response
  [ALIVE] (40/100) udp://109.201.134.183:80/announce 137ms — valid connect + announce
  [ALIVE] (41/100) udp://34.66.57.33:80/announce 50ms — valid connect + announce
  [ALIVE] (42/100) udp://34.66.57.33:1337/announce 55ms — valid connect + announce
  [ALIVE] (43/100) http://tracker.nyaa.vc:6969/announce 299ms — valid announce response
  [ALIVE] (45/100) udp://135.125.198.235:1984/announce 151ms — valid connect + announce
  [ALIVE] (46/100) udp://185.121.168.96:1337/announce 134ms — valid connect + announce
  [ALIVE] (47/100) http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 739ms — valid announce response
  [ALIVE] (48/100) udp://151.242.104.187:80/announce 153ms — valid connect + announce
  [ALIVE] (49/100) http://tracker.dler.com:6969/announce 532ms — valid announce response
  [ALIVE] (50/100) https://1.tracker.eu.org:443/announce 50ms — valid announce response
  [ALIVE] (51/100) udp://211.75.210.221:80/announce 143ms — valid connect + announce
  [ALIVE] (52/100) http://retracker01-msk-virt.corbina.net:80/announce 647ms — valid announce response
  [ALIVE] (54/100) http://tracker.renfei.net:8080/announce 179ms — valid announce response
  [ALIVE] (55/100) udp://31.56.179.159:6969/announce 161ms — valid connect + announce
  [ALIVE] (56/100) udp://exodus.desync.com:6969/announce 31ms — valid connect + announce
  [ALIVE] (57/100) udp://explodie.org:6969/announce 25ms — valid connect + announce
  [ALIVE] (58/100) udp://evan.im:6969/announce 51ms — valid connect + announce
  [ALIVE] (59/100) udp://65.109.28.17:6969/announce 163ms — valid connect + announce
  [ALIVE] (61/100) udp://open.ftorrent.com:443/announce 41ms — valid connect + announce
  [ALIVE] (62/100) udp://83.102.180.21:80/announce 176ms — valid connect + announce
  [ALIVE] (63/100) http://bt2.archive.org:6969/announce 211ms — valid announce response
  [ALIVE] (64/100) udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 147ms — valid connect + announce
  [ALIVE] (65/100) udp://open.demonii.com:1337/announce 139ms — valid connect + announce
  [ALIVE] (66/100) https://tracker.nekomi.cn:443/announce 49ms — valid announce response
  [ALIVE] (67/100) udp://kolankoalastree.newtrackon.co.nz:1337/announce 168ms — valid connect + announce
  [ALIVE] (68/100) udp://mail.segso.net:6969/announce 165ms — valid connect + announce
  [ALIVE] (69/100) udp://tracker.bittor.pw:1337/announce 50ms — valid connect + announce
  [ALIVE] (70/100) udp://tracker.gmi.gd:6969/announce 12ms — valid connect + announce
  [ALIVE] (72/100) udp://retracker01-msk-virt.corbina.net:80/announce 183ms — valid connect + announce
  [ALIVE] (73/100) udp://tr4ck3r.duckdns.org:6969/announce 72ms — valid connect + announce
  [ALIVE] (74/100) udp://43.250.54.126:6969/announce 382ms — valid connect + announce
  [ALIVE] (75/100) wss://tracker.openwebtorrent.com:443/announce 25ms — TLS reachable
  [ALIVE] (77/100) udp://89.234.156.205:451/announce 378ms — valid connect + announce
  [ALIVE] (78/100) udp://45.137.199.107:6969/announce 404ms — valid connect + announce
  [ALIVE] (79/100) udp://open.stealth.si:80/announce 282ms — valid connect + announce
  [ALIVE] (80/100) udp://tracker.opentrackr.org:1337/announce 153ms — valid connect + announce
  [ALIVE] (81/100) udp://tracker.ducks.party:1984/announce 160ms — valid connect + announce
  [ALIVE] (82/100) udp://t.overflow.biz:6969/announce 167ms — valid connect + announce
  [ALIVE] (83/100) udp://tracker.corpscorp.online:80/announce 56ms — valid connect + announce
  [ALIVE] (84/100) udp://martin-gebhardt.eu:25/announce 357ms — valid connect + announce
  [ALIVE] (85/100) udp://93.158.213.92:1337/announce 443ms — valid connect + announce
  [ALIVE] (86/100) udp://tracker.qu.ax:6969/announce 273ms — valid connect + announce
  [ALIVE] (87/100) udp://tracker.nyaa.vc:6969/announce 335ms — valid connect + announce
  [ALIVE] (88/100) udp://torrent.tracker.durukanbal.com:6969/announce 266ms — valid connect + announce
  [ALIVE] (89/100) udp://opentracker.lain.moscow:6969/announce 342ms — valid connect + announce
  [ALIVE] (90/100) udp://tracker.skynetcloud.site:6969/announce 331ms — valid connect + announce
  [ALIVE] (91/100) udp://tracker.torrent.eu.org:451/announce 424ms — valid connect + announce
  [ALIVE] (92/100) udp://tracker-udp.gbitt.info:80/announce 430ms — valid connect (announce not confirmed)
  [ALIVE] (93/100) udp://tracker.tryhackx.org:6969/announce 380ms — valid connect (announce not confirmed)
  [DEAD]  (100/100) https://tr.abir.ga:443/announce — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>

[INFO] First pass done in 12.6s
[INFO] Second pass: re-testing top 80 alive trackers...
[INFO] Second pass done, refined 79 trackers
[INFO] Same-IP dedup removed 32 slower tracker(s)

===== Test Summary =====
  Total tested:   100
  Alive (raw):    48
  Alive (final):  20 (top 20 by composite score)
  Non-UDP kept:   4 (quota >= 4)
  Score-capped:   28
  Unsafe filtered:0
  Low-speed:      0 (>5s excluded)
  Same-IP dedup:  32 (kept faster)
  Dead final:     78
  Time:           20.6s
=== 协议分布统计 ===
  HTTP  : 26 个
  HTTPS : 10 个
  UDP   : 43 个
  WSS   : 1 个
  WS    : 0 个
  总计: 80 个（存活）
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
 Round 1 - 2026-10-08 04:34:34
============================================================
  [PASS] Local tracker: trackers_cf_best.txt: 71 trackers
  [PASS] Local tracker: trackers_run_best.txt: 52 trackers
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
  [PASS] Plain text: /run_best.txt: 52 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /opentracker.txt: 38 trackers
  [PASS] Plain text: /udp.txt: 47 trackers
  [PASS] Plain text: /http.txt: 36 trackers
  [PASS] Plain text: /https.txt: 16 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
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
 Round 1 - 2026-10-08 04:34:42
============================================================
  [PASS] Local tracker: trackers_cf_best.txt: 71 trackers
  [PASS] Local tracker: trackers_run_best.txt: 52 trackers
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
  [PASS] Plain text: /run_best.txt: 52 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /opentracker.txt: 38 trackers
  [PASS] Plain text: /udp.txt: 47 trackers
  [PASS] Plain text: /http.txt: 36 trackers
  [PASS] Plain text: /https.txt: 16 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
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
 Round 2 - 2026-10-08 04:34:48
============================================================
  [PASS] Local tracker: trackers_cf_best.txt: 71 trackers
  [PASS] Local tracker: trackers_run_best.txt: 52 trackers
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
  [PASS] Plain text: /run_best.txt: 52 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /opentracker.txt: 38 trackers
  [PASS] Plain text: /udp.txt: 47 trackers
  [PASS] Plain text: /http.txt: 36 trackers
  [PASS] Plain text: /https.txt: 16 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
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
 Round 3 - 2026-10-08 04:34:54
============================================================
  [PASS] Local tracker: trackers_cf_best.txt: 71 trackers
  [PASS] Local tracker: trackers_run_best.txt: 52 trackers
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
  [PASS] Plain text: /run_best.txt: 52 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /opentracker.txt: 38 trackers
  [PASS] Plain text: /udp.txt: 47 trackers
  [PASS] Plain text: /http.txt: 36 trackers
  [PASS] Plain text: /https.txt: 16 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
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
=== End of diagnostics (Thu Oct  8 04:34:54 UTC 2026) ===
