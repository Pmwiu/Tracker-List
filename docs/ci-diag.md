=== Diagnostics Thu Oct  8 03:39:23 UTC 2026 ===
Python: Python 3.12.15
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://cf.trackerslist.com/best.txt
  HTTP 200, total 0.213826s
>>> https://trackers.run/s/rw_up_hp_hs_v4_v6.txt
  HTTP 200, total 0.746602s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.029186s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best_ip.txt
  HTTP 200, total 0.069032s
>>> https://raw.githubusercontent.com/1265578519/OpenTracker/refs/heads/master/tracker.txt
  HTTP 200, total 0.076778s
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
  [ALIVE] (1/100) https://t.213891.xyz:443/announce 26ms — valid announce response
  [ALIVE] (2/100) http://207.241.226.111:6969/announce 98ms — valid announce response
  [ALIVE] (3/100) http://207.241.231.226:6969/announce 106ms — valid announce response
  [ALIVE] (5/100) https://004430.xyz:443/announce 129ms — valid announce response
  [ALIVE] (6/100) http://tracker.dhitechnical.com:6969/announce 111ms — valid announce response
  [ALIVE] (7/100) http://tracker.waaa.moe:6969/announce 107ms — valid announce response
  [ALIVE] (8/100) http://tracker.nyaa.vc:6969/announce 189ms — valid announce response
  [ALIVE] (10/100) http://ipv4announce.sktorrent.eu:6969/announce 206ms — valid announce response
  [ALIVE] (11/100) https://tr.nyacat.pw:443/announce 114ms — valid announce response
  [ALIVE] (12/100) http://tracker.mywaifu.best:6969/announce 244ms — valid announce response
  [ALIVE] (13/100) http://bt1.archive.org:6969/announce 147ms — valid announce response
  [ALIVE] (15/100) http://bt2.archive.org:6969/announce 153ms — valid announce response
  [ALIVE] (16/100) http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 223ms — valid announce response
  [ALIVE] (17/100) https://tracker.7471.top:443/announce 136ms — valid announce response
  [ALIVE] (18/100) http://211.75.210.221:80/announce 359ms — valid announce response
  [ALIVE] (19/100) udp://193.148.251.93:6969/announce 19ms — valid connect + announce
  [ALIVE] (20/100) http://211.75.205.187:6969/announce 364ms — valid announce response
  [ALIVE] (21/100) http://211.75.210.221:6969/announce 363ms — valid announce response
  [ALIVE] (22/100) http://211.75.205.188:80/announce 365ms — valid announce response
  [ALIVE] (24/100) http://tracker.qu.ax:6969/announce 208ms — valid announce response
  [ALIVE] (25/100) http://tracker.auctor.tv:6969/announce 208ms — valid announce response
  [ALIVE] (26/100) udp://51.81.222.188:6969/announce 48ms — valid connect + announce
  [ALIVE] (27/100) https://1337.abcvg.info:443/announce 409ms — valid announce response
  [ALIVE] (28/100) http://1337.abcvg.info:80/announce 439ms — valid announce response
  [ALIVE] (29/100) udp://109.201.134.183:80/announce 108ms — valid connect + announce
  [ALIVE] (30/100) http://nyaa.tracker.wf:7777/announce 375ms — valid announce response
  [ALIVE] (31/100) udp://135.125.198.235:1984/announce 106ms — valid connect + announce
  [ALIVE] (32/100) udp://51.15.41.46:6969/announce 101ms — valid connect + announce
  [ALIVE] (33/100) udp://89.234.156.205:451/announce 104ms — valid connect + announce
  [ALIVE] (34/100) udp://132.226.6.145:6969/announce 143ms — valid connect + announce
  [ALIVE] (36/100) udp://31.38.161.123:6969/announce 114ms — valid connect + announce
  [ALIVE] (38/100) udp://evan.im:6969/announce 16ms — valid connect + announce
  [ALIVE] (39/100) https://tracker.foreverpirates.co:443/announce 395ms — valid announce response
  [ALIVE] (40/100) udp://explodie.org:6969/announce 49ms — valid connect + announce
  [ALIVE] (41/100) http://tracker.dler.org:6969/announce 476ms — valid announce response
  [ALIVE] (42/100) udp://193.34.92.5:80/announce 138ms — valid connect + announce
  [ALIVE] (43/100) http://tracker.renfei.net:8080/announce 68ms — valid announce response
  [ALIVE] (45/100) http://tracker.dler.com:6969/announce 376ms — valid announce response
  [ALIVE] (46/100) udp://ipv4announce.sktorrent.eu:6969/announce 103ms — valid connect + announce
  [ALIVE] (47/100) udp://tr4ck3r.duckdns.org:6969/announce 23ms — valid connect + announce
  [ALIVE] (48/100) udp://43.154.112.29:17272/announce 182ms — valid connect + announce
  [ALIVE] (49/100) udp://martin-gebhardt.eu:25/announce 105ms — valid connect + announce
  [ALIVE] (50/100) https://1.tracker.eu.org:443/announce 35ms — valid announce response
  [ALIVE] (51/100) udp://tracker.bittor.pw:1337/announce 11ms — valid connect + announce
  [ALIVE] (52/100) udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 222ms — valid connect + announce
  [ALIVE] (53/100) udp://open.ftorrent.com:443/announce 27ms — valid connect + announce
  [ALIVE] (54/100) udp://exodus.desync.com:6969/announce 52ms — valid connect + announce
  [ALIVE] (55/100) https://tracker.nekomi.cn:443/announce 124ms — valid announce response
  [ALIVE] (56/100) udp://mail.segso.net:6969/announce 124ms — valid connect + announce
  [ALIVE] (57/100) udp://tracker.corpscorp.online:80/announce 12ms — valid connect + announce
  [ALIVE] (58/100) udp://tracker-udp.gbitt.info:80/announce 100ms — valid connect + announce
  [ALIVE] (59/100) udp://t.overflow.biz:6969/announce 138ms — valid connect + announce
  [ALIVE] (60/100) udp://kolankoalastree.newtrackon.co.nz:1337/announce 204ms — valid connect + announce
  [ALIVE] (62/100) https://tracker.qingwapt.org:443/announce 604ms — online (failure reason)
  [ALIVE] (64/100) udp://admin.52ywp.com:6969/announce 255ms — valid connect + announce
  [ALIVE] (65/100) udp://tracker.nyaa.vc:6969/announce 98ms — valid connect + announce
  [ALIVE] (66/100) udp://open.demonii.com:1337/announce 181ms — valid connect + announce
  [ALIVE] (67/100) udp://tracker.wildkat.net:6969/announce 2ms — valid connect + announce
  [ALIVE] (68/100) udp://tracker.cn.nyaa.net:6969/announce 186ms — valid connect + announce
  [ALIVE] (69/100) udp://tracker.dler.com:6969/announce 180ms — valid connect + announce
  [ALIVE] (70/100) udp://tracker.dler.org:6969/announce 182ms — valid connect + announce
  [ALIVE] (72/100) udp://retracker01-msk-virt.corbina.net:80/announce 142ms — valid connect + announce
  [ALIVE] (73/100) udp://tracker.qu.ax:6969/announce 102ms — valid connect + announce
  [ALIVE] (74/100) udp://tracker.gmi.gd:6969/announce 53ms — valid connect + announce
  [ALIVE] (75/100) udp://tracker.ilibr.org:6969/announce 127ms — valid connect + announce
  [ALIVE] (76/100) https://tracker.midnightprogrammer.net:443/announce 864ms — valid announce response
  [ALIVE] (77/100) udp://torrent.tracker.durukanbal.com:6969/announce 100ms — valid connect + announce
  [ALIVE] (78/100) udp://tracker.opentrackr.org:1337/announce 104ms — valid connect + announce
  [ALIVE] (79/100) udp://open.stealth.si:80/announce 105ms — valid connect + announce
  [ALIVE] (80/100) udp://tracker.nyaa.net:6969/announce 135ms — valid connect + announce
  [ALIVE] (81/100) udp://tracker.opentrackr.com:6969/announce 128ms — valid connect + announce
  [ALIVE] (82/100) wss://tracker.openwebtorrent.com:443/announce 38ms — TLS reachable
  [ALIVE] (83/100) udp://tracker.ducks.party:1984/announce 109ms — valid connect + announce
  [ALIVE] (84/100) udp://tracker.peerfect.org:6969/announce 127ms — valid connect + announce
  [ALIVE] (85/100) udp://opentracker.lain.moscow:6969/announce 108ms — valid connect + announce
  [ALIVE] (86/100) udp://tracker.skynetcloud.site:6969/announce 105ms — valid connect + announce
  [ALIVE] (87/100) udp://tracker.willy.pro:6969/announce 228ms — valid connect + announce
  [ALIVE] (88/100) udp://v2.iperson.xyz:6969/announce 229ms — valid connect + announce
  [ALIVE] (89/100) udp://tracker.aruku.ovh:8081/announce 208ms — valid connect + announce
  [ALIVE] (90/100) udp://tracker2.dler.org:80/announce 174ms — valid connect + announce
  [ALIVE] (91/100) http://tracker.xn--djrq4gl4hvoi.top:80/announce 1592ms — valid announce response
  [ALIVE] (92/100) udp://tracker.torrent.eu.org:451/announce 107ms — valid connect + announce
  [ALIVE] (93/100) udp://tracker.torrents.observer:80/announce 101ms — valid connect + announce
  [DEAD]  (100/100) udp://wegkxfcivgx.ydns.eu:80/announce — no connect response

[INFO] First pass done in 11.4s
[INFO] Second pass: re-testing top 83 alive trackers...
[INFO] Second pass done, refined 82 trackers
[INFO] Same-IP dedup removed 19 slower tracker(s)

===== Test Summary =====
  Total tested:   100
  Alive (raw):    64
  Alive (final):  20 (top 20 by composite score)
  Non-UDP kept:   4 (quota >= 4)
  Score-capped:   44
  Unsafe filtered:0
  Low-speed:      0 (>5s excluded)
  Same-IP dedup:  19 (kept faster)
  Dead final:     80
  Time:           19.4s
=== 协议分布统计 ===
  HTTP  : 22 个
  HTTPS : 10 个
  UDP   : 50 个
  WSS   : 1 个
  WS    : 0 个
  总计: 83 个（存活）
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
 Round 1 - 2026-10-08 03:39:47
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
  [PASS] Plain text: /udp.txt: 57 trackers
  [PASS] Plain text: /http.txt: 26 trackers
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
 Round 1 - 2026-10-08 03:39:53
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
  [PASS] Plain text: /udp.txt: 57 trackers
  [PASS] Plain text: /http.txt: 26 trackers
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
------------------------------------------------------------
  Result: 47 passed, 0 warnings, 0 failed
============================================================

============================================================
 Round 2 - 2026-10-08 03:39:58
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
  [PASS] Plain text: /udp.txt: 57 trackers
  [PASS] Plain text: /http.txt: 26 trackers
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
------------------------------------------------------------
  Result: 47 passed, 0 warnings, 0 failed
============================================================

============================================================
 Round 3 - 2026-10-08 03:40:04
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
  [PASS] Plain text: /udp.txt: 57 trackers
  [PASS] Plain text: /http.txt: 26 trackers
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
------------------------------------------------------------
  Result: 47 passed, 0 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 3 rounds completed
   Total PASS: 141
   Total WARN: 0
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################
=== End of diagnostics (Thu Oct  8 03:40:04 UTC 2026) ===
