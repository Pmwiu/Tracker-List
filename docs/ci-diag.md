=== Diagnostics Thu Oct  8 02:02:55 UTC 2026 ===
Python: Python 3.12.15
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://cf.trackerslist.com/best.txt
  HTTP 200, total 0.215033s
>>> https://trackers.run/s/rw_up_hp_hs_v4_v6.txt
  HTTP 200, total 0.529203s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.039035s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best_ip.txt
  HTTP 200, total 0.149587s
>>> https://raw.githubusercontent.com/1265578519/OpenTracker/refs/heads/master/tracker.txt
  HTTP 200, total 0.168001s
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
  [ALIVE] (1/100) http://207.241.226.111:6969/announce 85ms — valid announce response
  [ALIVE] (2/100) http://207.241.231.226:6969/announce 92ms — valid announce response
  [ALIVE] (3/100) http://bt1.archive.org:6969/announce 97ms — valid announce response
  [ALIVE] (5/100) https://t.213891.xyz:443/announce 87ms — valid announce response
  [ALIVE] (7/100) http://tracker.dhitechnical.com:6969/announce 129ms — valid announce response
  [ALIVE] (8/100) https://004430.xyz:443/announce 187ms — valid announce response
  [ALIVE] (10/100) http://bt2.archive.org:6969/announce 123ms — valid announce response
  [ALIVE] (11/100) http://tracker.nyaa.vc:6969/announce 217ms — valid announce response
  [ALIVE] (12/100) http://211.75.205.188:80/announce 337ms — valid announce response
  [ALIVE] (13/100) http://211.75.210.221:80/announce 340ms — valid announce response
  [ALIVE] (14/100) http://211.75.210.221:6969/announce 345ms — valid announce response
  [ALIVE] (15/100) http://211.75.205.187:6969/announce 347ms — valid announce response
  [ALIVE] (16/100) https://1.tracker.eu.org:443/announce 69ms — valid announce response
  [ALIVE] (18/100) http://1337.abcvg.info:80/announce 229ms — valid announce response
  [ALIVE] (19/100) udp://193.148.251.93:6969/announce 21ms — valid connect + announce
  [ALIVE] (20/100) https://1337.abcvg.info:443/announce 248ms — valid announce response
  [ALIVE] (21/100) http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 276ms — valid announce response
  [ALIVE] (22/100) http://ipv4announce.sktorrent.eu:6969/announce 221ms — valid announce response
  [ALIVE] (23/100) http://tracker.dler.org:6969/announce 380ms — valid announce response
  [ALIVE] (24/100) https://tracker.7471.top:443/announce 205ms — valid announce response
  [ALIVE] (25/100) https://tracker.foreverpirates.co:443/announce 219ms — valid announce response
  [ALIVE] (26/100) http://nyaa.tracker.wf:7777/announce 310ms — valid announce response
  [ALIVE] (27/100) http://tracker.renfei.net:8080/announce 119ms — valid announce response
  [ALIVE] (28/100) udp://51.81.222.188:6969/announce 53ms — valid connect + announce
  [ALIVE] (29/100) http://tracker.qu.ax:6969/announce 230ms — valid announce response
  [ALIVE] (30/100) http://tracker.auctor.tv:6969/announce 243ms — valid announce response
  [ALIVE] (31/100) http://tracker.mywaifu.best:6969/announce 380ms — valid announce response
  [ALIVE] (33/100) udp://109.201.134.183:80/announce 120ms — valid connect + announce
  [ALIVE] (34/100) http://tracker.dler.com:6969/announce 376ms — valid announce response
  [ALIVE] (36/100) udp://135.125.198.235:1984/announce 124ms — valid connect + announce
  [ALIVE] (37/100) http://tracker.waaa.moe:6969/announce 436ms — valid announce response
  [ALIVE] (38/100) udp://132.226.6.145:6969/announce 135ms — valid connect + announce
  [ALIVE] (39/100) udp://51.15.41.46:6969/announce 109ms — valid connect + announce
  [ALIVE] (40/100) udp://31.38.161.123:6969/announce 124ms — valid connect + announce
  [ALIVE] (41/100) udp://evan.im:6969/announce 28ms — valid connect + announce
  [ALIVE] (42/100) udp://89.234.156.205:451/announce 120ms — valid connect + announce
  [ALIVE] (43/100) udp://193.34.92.5:80/announce 151ms — valid connect + announce
  [ALIVE] (44/100) udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 135ms — valid connect + announce
  [ALIVE] (45/100) https://tr.nyacat.pw:443/announce 331ms — valid announce response
  [ALIVE] (47/100) https://tracker.midnightprogrammer.net:443/announce 396ms — valid announce response
  [ALIVE] (48/100) udp://ipv4announce.sktorrent.eu:6969/announce 111ms — valid connect + announce
  [ALIVE] (49/100) udp://43.154.112.29:17272/announce 181ms — valid connect + announce
  [ALIVE] (50/100) udp://open.ftorrent.com:443/announce 22ms — valid connect + announce
  [ALIVE] (51/100) udp://tr4ck3r.duckdns.org:6969/announce 31ms — valid connect + announce
  [ALIVE] (52/100) udp://tracker.corpscorp.online:80/announce 21ms — valid connect + announce
  [ALIVE] (53/100) udp://martin-gebhardt.eu:25/announce 120ms — valid connect + announce
  [ALIVE] (54/100) https://tracker.nekomi.cn:443/announce 142ms — valid announce response
  [ALIVE] (55/100) udp://exodus.desync.com:6969/announce 50ms — valid connect + announce
  [ALIVE] (56/100) udp://tracker.bittor.pw:1337/announce 30ms — valid connect + announce
  [ALIVE] (57/100) udp://open.stealth.si:80/announce 129ms — valid connect + announce
  [ALIVE] (58/100) udp://admin.52ywp.com:6969/announce 205ms — valid connect + announce
  [ALIVE] (59/100) udp://mail.segso.net:6969/announce 143ms — valid connect + announce
  [ALIVE] (60/100) udp://open.demonii.com:1337/announce 172ms — valid connect + announce
  [ALIVE] (61/100) udp://tracker.ducks.party:1984/announce 117ms — valid connect + announce
  [ALIVE] (62/100) udp://tracker-udp.gbitt.info:80/announce 116ms — valid connect + announce
  [ALIVE] (63/100) udp://kolankoalastree.newtrackon.co.nz:1337/announce 171ms — valid connect + announce
  [ALIVE] (64/100) https://tracker.qingwapt.org:443/announce 608ms — online (failure reason)
  [ALIVE] (65/100) udp://tracker.dler.com:6969/announce 179ms — valid connect + announce
  [ALIVE] (66/100) udp://tracker.dler.org:6969/announce 169ms — valid connect + announce
  [ALIVE] (67/100) udp://tracker.cn.nyaa.net:6969/announce 178ms — valid connect + announce
  [ALIVE] (68/100) udp://tracker.qu.ax:6969/announce 112ms — valid connect + announce
  [ALIVE] (69/100) udp://tracker.nyaa.vc:6969/announce 145ms — valid connect + announce
  [ALIVE] (70/100) udp://tracker.wildkat.net:6969/announce 18ms — valid connect + announce
  [ALIVE] (71/100) udp://tracker.opentrackr.com:6969/announce 142ms — valid connect + announce
  [ALIVE] (72/100) udp://tracker.peerfect.org:6969/announce 136ms — valid connect + announce
  [ALIVE] (73/100) udp://t.overflow.biz:6969/announce 149ms — valid connect + announce
  [ALIVE] (74/100) udp://torrent.tracker.durukanbal.com:6969/announce 118ms — valid connect + announce
  [ALIVE] (75/100) udp://retracker01-msk-virt.corbina.net:80/announce 150ms — valid connect + announce
  [ALIVE] (76/100) udp://tracker.aruku.ovh:8081/announce 202ms — valid connect + announce
  [ALIVE] (77/100) udp://tracker.gmi.gd:6969/announce 53ms — valid connect + announce
  [ALIVE] (78/100) udp://tracker.ilibr.org:6969/announce 143ms — valid connect + announce
  [ALIVE] (79/100) udp://opentracker.lain.moscow:6969/announce 140ms — valid connect + announce
  [ALIVE] (80/100) wss://tracker.openwebtorrent.com:443/announce 46ms — TLS reachable
  [ALIVE] (81/100) udp://tracker.opentrackr.org:1337/announce 112ms — valid connect + announce
  [ALIVE] (82/100) udp://tracker.skynetcloud.site:6969/announce 120ms — valid connect + announce
  [ALIVE] (83/100) udp://v2.iperson.xyz:6969/announce 220ms — valid connect + announce
  [ALIVE] (84/100) udp://tracker2.dler.org:80/announce 168ms — valid connect + announce
  [ALIVE] (85/100) udp://tracker.willy.pro:6969/announce 227ms — valid connect + announce
  [ALIVE] (87/100) udp://tracker.torrents.observer:80/announce 118ms — valid connect + announce
  [ALIVE] (88/100) udp://tracker.torrent.eu.org:451/announce 121ms — valid connect + announce
  [ALIVE] (89/100) http://tracker.xn--djrq4gl4hvoi.top:80/announce 1277ms — valid announce response
  [ALIVE] (90/100) udp://tracker.tryhackx.org:6969/announce 127ms — valid connect (announce not confirmed)
  [DEAD]  (100/100) https://tr.abir.ga:443/announce — URLError: <urlopen error _ssl.c:993: The handshake operation timed out>

[INFO] First pass done in 17.4s
[INFO] Second pass: re-testing top 82 alive trackers...
[INFO] Second pass done, refined 81 trackers
[INFO] Same-IP dedup removed 19 slower tracker(s)

===== Test Summary =====
  Total tested:   100
  Alive (raw):    63
  Alive (final):  20 (top 20 by composite score)
  Score-capped:   43
  Unsafe filtered:0
  Low-speed:      0 (>5s excluded)
  Same-IP dedup:  19 (kept faster)
  Dead final:     80
  Time:           25.6s
=== 协议分布统计 ===
  HTTP  : 22 个
  HTTPS : 10 个
  UDP   : 49 个
  WSS   : 1 个
  WS    : 0 个
  总计: 82 个（存活）
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
 Round 1 - 2026-10-08 02:03:23
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
 Round 1 - 2026-10-08 02:03:30
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
 Round 2 - 2026-10-08 02:03:35
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
 Round 3 - 2026-10-08 02:03:40
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
=== End of diagnostics (Thu Oct  8 02:03:40 UTC 2026) ===
