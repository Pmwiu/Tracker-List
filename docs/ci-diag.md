=== Diagnostics Thu Oct  8 11:05:02 UTC 2026 ===
Python: Python 3.12.15
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_best.txt
  HTTP 200, total 0.026503s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_best_ip.txt
  HTTP 200, total 0.034982s
>>> https://cf.trackerslist.com/best.txt
  HTTP 200, total 0.071622s
>>> https://raw.githubusercontent.com/gonghailink/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.119942s
>>> https://raw.githubusercontent.com/panda-men/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.113462s
>>> https://raw.githubusercontent.com/gspu/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.113359s
>>> https://raw.githubusercontent.com/linux-jin/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.158967s
>>> https://raw.githubusercontent.com/AlphaCatMeow/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.131139s
>>> https://raw.githubusercontent.com/pexcn/daily/gh-pages/trackerlist/trackerlist-best.txt
  HTTP 200, total 0.135228s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_i2p.txt
  HTTP 200, total 0.062559s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_yggdrasil.txt
  HTTP 200, total 0.059170s
[INFO] Repo: Pmwiu/Tracker-List, Max: 20

[INFO] trackers_ngosang_best.txt (ngosang-best)
[OK]   20 unique

[INFO] trackers_ngosang_best_ip.txt (ngosang-best-ip)
[OK]   20 unique

[INFO] trackers_cf_best.txt (cf-best)
[OK]   71 unique

[INFO] trackers_gonghailink_best.txt (gonghailink-best)
[OK]   20 unique

[INFO] trackers_pandamen_best.txt (pandamen-best)
[OK]   20 unique

[INFO] trackers_gspu_best.txt (gspu-best)
[OK]   20 unique

[INFO] trackers_linuxjin_best.txt (linuxjin-best)
[OK]   20 unique

[INFO] trackers_alphacatmeow_best.txt (alphacatmeow-best)
[OK]   20 unique

[INFO] trackers_pexcn_best.txt (pexcn-best)
[OK]   73 unique

[INFO] trackers_ngosang_i2p.txt (ngosang-i2p)
[OK]   17 unique

[INFO] trackers_ngosang_yggdrasil.txt (ngosang-yggdrasil)
[OK]   1 unique

[INFO] all 合并贡献: ngosang-best=20, ngosang-best-ip=16, cf-best=26, gonghailink-best=9, pandamen-best=6, gspu-best=3, linuxjin-best=1, alphacatmeow-best=2, pexcn-best=0, ngosang-i2p=16, ngosang-yggdrasil=1
[INFO] all 协议分布: http=30, https=19, udp=50, wss=1, ws=0

[OK]   merged: 100
[OK]   MIRRORS.txt
[OK]   /s/alive
[OK]   /s/all
[OK]   index.html
[OK]   docs/alive.txt
[OK]   docs/merged.txt
[OK]   docs/ngosang_best.txt
[OK]   docs/ngosang_best_ip.txt
[OK]   docs/cf_best.txt
[OK]   docs/gonghailink_best.txt
[OK]   docs/pandamen_best.txt
[OK]   docs/gspu_best.txt
[OK]   docs/linuxjin_best.txt
[OK]   docs/alphacatmeow_best.txt
[OK]   docs/pexcn_best.txt
[OK]   docs/ngosang_i2p.txt
[OK]   docs/ngosang_yggdrasil.txt
[OK]   docs/udp.txt
[OK]   docs/http.txt
[OK]   docs/https.txt
[OK]   docs/wss.txt
[OK]   docs/ws.txt

===== Summary =====
  trackers_ngosang_best.txt: 20
  trackers_ngosang_best_ip.txt: 20
  trackers_cf_best.txt: 71
  trackers_gonghailink_best.txt: 20
  trackers_pandamen_best.txt: 20
  trackers_gspu_best.txt: 20
  trackers_linuxjin_best.txt: 20
  trackers_alphacatmeow_best.txt: 20
  trackers_pexcn_best.txt: 73
  trackers_ngosang_i2p.txt: 17
  trackers_ngosang_yggdrasil.txt: 1
  trackers_merged.txt: 100
  alive capped at 20 after test+sort
===================
[INFO] Testing 100 candidates (all-pool=100, timeout=10s, workers=30)
[INFO] Max alive trackers after scoring: 20
  [ALIVE] (1/100) http://bt1.archive.org:6969/announce 11ms — announce with peers
  [ALIVE] (2/100) http://bt2.archive.org:6969/announce 13ms — announce with peers
  [ALIVE] (3/100) https://004430.xyz:443/announce 45ms — announce with peers
  [ALIVE] (5/100) http://tracker.dhitechnical.com:6969/announce 196ms — announce with peers
  [ALIVE] (6/100) http://1337.abcvg.info:80/announce 238ms — announce with peers
  [ALIVE] (7/100) https://t.213891.xyz:443/announce 15ms — announce with peers
  [ALIVE] (8/100) http://211.75.205.187:6969/announce 282ms — announce with peers
  [ALIVE] (9/100) http://ipv4announce.sktorrent.eu:6969/announce 289ms — announce with peers
  [ALIVE] (10/100) http://tracker.dler.org:6969/announce 292ms — announce with peers
  [ALIVE] (11/100) http://tracker.dler.com:6969/announce 292ms — announce with peers
  [ALIVE] (12/100) http://tracker.renfei.net:8080/announce 161ms — announce with peers
  [ALIVE] (13/100) https://1337.abcvg.info:443/announce 239ms — announce with peers
  [ALIVE] (14/100) https://1.tracker.eu.org:443/announce 27ms — announce with peers
  [ALIVE] (16/100) http://nyaa.tracker.wf:7777/announce 330ms — announce with peers
  [ALIVE] (18/100) http://tracker.mywaifu.best:6969/announce 311ms — announce with peers
  [ALIVE] (19/100) https://tracker.7471.top:443/announce 174ms — announce with peers
  [ALIVE] (20/100) https://tracker.foreverpirates.co:443/announce 225ms — announce with peers
  [ALIVE] (24/100) https://tracker.zhuqiy.com:443/announce 335ms — announce with peers
  [ALIVE] (25/100) https://tracker.nekomi.cn:443/announce 42ms — announce with peers
  [ALIVE] (27/100) http://tracker.opentrackr.org:1337/announce 473ms — announce with peers
  [ALIVE] (28/100) udp://109.201.134.183:80/announce 153ms — valid connect + announce
  [ALIVE] (29/100) udp://209.141.59.25:6969/announce 18ms — valid connect + announce
  [ALIVE] (30/100) udp://135.125.198.235:1984/announce 155ms — valid connect + announce
  [ALIVE] (31/100) https://tracker.qingwapt.org:443/announce 191ms — online (failure reason)
  [ALIVE] (32/100) udp://23.157.120.14:6969/announce 30ms — valid connect + announce
  [ALIVE] (33/100) http://tracker.waaa.moe:6969/announce 956ms — announce with peers
  [ALIVE] (34/100) udp://34.66.57.33:1337/announce 45ms — valid connect + announce
  [ALIVE] (35/100) udp://151.242.104.187:80/announce 156ms — valid connect + announce
  [ALIVE] (36/100) udp://34.66.57.33:80/announce 46ms — valid connect + announce
  [ALIVE] (37/100) udp://211.75.205.188:6969/announce 138ms — valid connect + announce
  [ALIVE] (38/100) udp://211.75.205.188:80/announce 138ms — valid connect + announce
  [ALIVE] (39/100) udp://185.121.168.96:1337/announce 147ms — valid connect + announce
  [ALIVE] (40/100) https://tracker.midnightprogrammer.net:443/announce 736ms — announce with peers
  [ALIVE] (41/100) udp://45.137.199.107:6969/announce 143ms — valid connect + announce
  [ALIVE] (42/100) udp://31.56.179.159:6969/announce 171ms — valid connect + announce
  [ALIVE] (43/100) udp://43.250.54.126:6969/announce 148ms — valid connect + announce
  [ALIVE] (46/100) udp://65.109.28.17:6969/announce 170ms — valid connect + announce
  [ALIVE] (47/100) udp://83.102.180.21:80/announce 195ms — valid connect + announce
  [ALIVE] (48/100) udp://open.demonii.com:1337/announce 137ms — valid connect + announce
  [ALIVE] (49/100) udp://open.stealth.si:80/announce 154ms — valid connect + announce
  [ALIVE] (50/100) udp://explodie.org:6969/announce 3ms — valid connect + announce
  [ALIVE] (51/100) udp://tracker.004430.xyz:1337/announce 8ms — valid connect + announce
  [ALIVE] (52/100) udp://leet-tracker.moe:1337/announce 46ms — valid connect + announce
  [ALIVE] (53/100) udp://retracker01-msk-virt.corbina.net:80/announce 186ms — valid connect + announce
  [ALIVE] (55/100) udp://tracker-udp.gbitt.info:80/announce 152ms — valid connect + announce
  [ALIVE] (56/100) udp://t.overflow.biz:6969/announce 170ms — valid connect + announce
  [ALIVE] (65/100) udp://tracker.bittor.pw:1337/announce 45ms — valid connect + announce
  [ALIVE] (67/100) udp://tracker.corpscorp.online:80/announce 45ms — valid connect + announce
  [ALIVE] (71/100) udp://tracker.gmi.gd:6969/announce 18ms — valid connect + announce
  [ALIVE] (72/100) wss://tracker.openwebtorrent.com:443/announce 7ms — TLS reachable
  [ALIVE] (74/100) udp://tracker.dler.org:6969/announce 143ms — valid connect + announce
  [ALIVE] (75/100) udp://tracker.auctor.tv:6969/announce 151ms — valid connect + announce
  [ALIVE] (76/100) udp://tracker.nyaa.vc:6969/announce 149ms — valid connect + announce
  [ALIVE] (77/100) udp://tracker.opentrackr.org:1337/announce 150ms — valid connect + announce
  [ALIVE] (78/100) udp://tracker.qu.ax:6969/announce 147ms — valid connect + announce
  [ALIVE] (79/100) udp://tracker.farted.net:6969/announce 171ms — valid connect + announce
  [ALIVE] (80/100) udp://tracker.ducks.party:1984/announce 158ms — valid connect + announce
  [ALIVE] (81/100) udp://tracker2.dler.org:80/announce 139ms — valid connect + announce
  [ALIVE] (82/100) udp://tracker.tryhackx.org:6969/announce 215ms — valid connect + announce
  [ALIVE] (83/100) udp://tracker.peerfect.org:6969/announce 176ms — valid connect + announce
  [ALIVE] (84/100) udp://tracker.skynetcloud.site:6969/announce 152ms — valid connect + announce
  [ALIVE] (85/100) udp://tracker.torrent.eu.org:451/announce 161ms — valid connect + announce
  [ALIVE] (88/100) udp://exodus.desync.com:6969/announce 4ms — valid connect (announce not confirmed)
  [ALIVE] (89/100) udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 1999ms — valid connect + announce
  [DEAD]  (100/100) udp://tracker.publictracker.xyz:6969/announce — no connect response

[INFO] First pass done in 12.0s
[INFO] Second pass: re-testing top 64 alive trackers...
[INFO] Second pass done, refined 64 trackers
[INFO] Same-subnet(/24) dedup removed 25 slower tracker(s)

===== Test Summary =====
  Total tested:   100
  Alive (raw):    39
  Alive (final):  20 (top 20 by composite score)
  Non-UDP kept:   4 (quota >= 4)
  Score-capped:   19
  Unsafe filtered:2
  Low-speed:      0 (>5s excluded)
  Same-subnet dedup:  25 (kept faster)
  Dead final:     64
  Time:           14.3s
=== 协议分布统计 ===
  HTTP  : 13 个
  HTTPS : 10 个
  UDP   : 40 个
  WSS   : 1 个
  WS    : 0 个
  总计: 64 个（存活）
=========================
[OK]   /s/alive
[OK]   /s/all
[OK]   index.html
[OK] Pages regenerated with alive statistics.
[OK]   docs/alive.txt
[OK]   docs/merged.txt
[OK]   docs/ngosang_best.txt
[OK]   docs/ngosang_best_ip.txt
[OK]   docs/cf_best.txt
[OK]   docs/gonghailink_best.txt
[OK]   docs/pandamen_best.txt
[OK]   docs/gspu_best.txt
[OK]   docs/linuxjin_best.txt
[OK]   docs/alphacatmeow_best.txt
[OK]   docs/pexcn_best.txt
[OK]   docs/ngosang_i2p.txt
[OK]   docs/ngosang_yggdrasil.txt
[OK]   docs/udp.txt
[OK]   docs/http.txt
[OK]   docs/https.txt
[OK]   docs/wss.txt
[OK]   docs/ws.txt
[OK] Plain-text files synced to docs/.

============================================================
 Round 1 - 2026-10-08 11:05:18
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 71 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 20 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 20 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 20 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 20 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 73 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
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
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 71 trackers
  [PASS] Plain text: /gonghailink_best.txt: 20 trackers
  [PASS] Plain text: /pandamen_best.txt: 20 trackers
  [PASS] Plain text: /gspu_best.txt: 20 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 20 trackers
  [PASS] Plain text: /pexcn_best.txt: 73 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 50 trackers
  [PASS] Plain text: /http.txt: 30 trackers
  [PASS] Plain text: /https.txt: 19 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 20 in [0, 20]
  [PASS] Merged dedup check: 100 unique
  [PASS] Alive subset check: best is subset of all
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_ngosang_best.txt vs ngosang_best.txt: identical
  [PASS] Consistency: trackers_ngosang_best_ip.txt vs ngosang_best_ip.txt: identical
  [PASS] Consistency: trackers_cf_best.txt vs cf_best.txt: identical
  [PASS] Consistency: trackers_gonghailink_best.txt vs gonghailink_best.txt: identical
  [PASS] Consistency: trackers_pandamen_best.txt vs pandamen_best.txt: identical
  [PASS] Consistency: trackers_gspu_best.txt vs gspu_best.txt: identical
  [PASS] Consistency: trackers_linuxjin_best.txt vs linuxjin_best.txt: identical
  [PASS] Consistency: trackers_alphacatmeow_best.txt vs alphacatmeow_best.txt: identical
  [PASS] Consistency: trackers_pexcn_best.txt vs pexcn_best.txt: identical
  [PASS] Consistency: trackers_ngosang_i2p.txt vs ngosang_i2p.txt: identical
  [PASS] Consistency: trackers_ngosang_yggdrasil.txt vs ngosang_yggdrasil.txt: identical
  [PASS] Consistency: trackers_udp.txt vs udp.txt: identical
  [PASS] Consistency: trackers_http.txt vs http.txt: identical
  [PASS] Consistency: trackers_https.txt vs https.txt: identical
  [PASS] Consistency: trackers_wss.txt vs wss.txt: identical
  [PASS] Consistency: trackers_ws.txt vs ws.txt: identical
  [PASS] URL format check: all 100 valid
------------------------------------------------------------
  Result: 60 passed, 0 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 1 rounds completed
   Total PASS: 60
   Total WARN: 0
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################

============================================================
 Round 1 - 2026-10-08 11:05:26
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 71 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 20 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 20 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 20 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 20 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 73 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
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
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 71 trackers
  [PASS] Plain text: /gonghailink_best.txt: 20 trackers
  [PASS] Plain text: /pandamen_best.txt: 20 trackers
  [PASS] Plain text: /gspu_best.txt: 20 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 20 trackers
  [PASS] Plain text: /pexcn_best.txt: 73 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 50 trackers
  [PASS] Plain text: /http.txt: 30 trackers
  [PASS] Plain text: /https.txt: 19 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 20 in [0, 20]
  [PASS] Merged dedup check: 100 unique
  [PASS] Alive subset check: best is subset of all
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_ngosang_best.txt vs ngosang_best.txt: identical
  [PASS] Consistency: trackers_ngosang_best_ip.txt vs ngosang_best_ip.txt: identical
  [PASS] Consistency: trackers_cf_best.txt vs cf_best.txt: identical
  [PASS] Consistency: trackers_gonghailink_best.txt vs gonghailink_best.txt: identical
  [PASS] Consistency: trackers_pandamen_best.txt vs pandamen_best.txt: identical
  [PASS] Consistency: trackers_gspu_best.txt vs gspu_best.txt: identical
  [PASS] Consistency: trackers_linuxjin_best.txt vs linuxjin_best.txt: identical
  [PASS] Consistency: trackers_alphacatmeow_best.txt vs alphacatmeow_best.txt: identical
  [PASS] Consistency: trackers_pexcn_best.txt vs pexcn_best.txt: identical
  [PASS] Consistency: trackers_ngosang_i2p.txt vs ngosang_i2p.txt: identical
  [PASS] Consistency: trackers_ngosang_yggdrasil.txt vs ngosang_yggdrasil.txt: identical
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
  Result: 70 passed, 0 warnings, 0 failed
============================================================

============================================================
 Round 2 - 2026-10-08 11:05:31
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 71 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 20 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 20 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 20 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 20 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 73 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
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
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 71 trackers
  [PASS] Plain text: /gonghailink_best.txt: 20 trackers
  [PASS] Plain text: /pandamen_best.txt: 20 trackers
  [PASS] Plain text: /gspu_best.txt: 20 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 20 trackers
  [PASS] Plain text: /pexcn_best.txt: 73 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 50 trackers
  [PASS] Plain text: /http.txt: 30 trackers
  [PASS] Plain text: /https.txt: 19 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 20 in [0, 20]
  [PASS] Merged dedup check: 100 unique
  [PASS] Alive subset check: best is subset of all
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_ngosang_best.txt vs ngosang_best.txt: identical
  [PASS] Consistency: trackers_ngosang_best_ip.txt vs ngosang_best_ip.txt: identical
  [PASS] Consistency: trackers_cf_best.txt vs cf_best.txt: identical
  [PASS] Consistency: trackers_gonghailink_best.txt vs gonghailink_best.txt: identical
  [PASS] Consistency: trackers_pandamen_best.txt vs pandamen_best.txt: identical
  [PASS] Consistency: trackers_gspu_best.txt vs gspu_best.txt: identical
  [PASS] Consistency: trackers_linuxjin_best.txt vs linuxjin_best.txt: identical
  [PASS] Consistency: trackers_alphacatmeow_best.txt vs alphacatmeow_best.txt: identical
  [PASS] Consistency: trackers_pexcn_best.txt vs pexcn_best.txt: identical
  [PASS] Consistency: trackers_ngosang_i2p.txt vs ngosang_i2p.txt: identical
  [PASS] Consistency: trackers_ngosang_yggdrasil.txt vs ngosang_yggdrasil.txt: identical
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
  Result: 70 passed, 0 warnings, 0 failed
============================================================

============================================================
 Round 3 - 2026-10-08 11:05:37
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 71 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 20 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 20 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 20 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 20 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 73 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
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
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 71 trackers
  [PASS] Plain text: /gonghailink_best.txt: 20 trackers
  [PASS] Plain text: /pandamen_best.txt: 20 trackers
  [PASS] Plain text: /gspu_best.txt: 20 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 20 trackers
  [PASS] Plain text: /pexcn_best.txt: 73 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 50 trackers
  [PASS] Plain text: /http.txt: 30 trackers
  [PASS] Plain text: /https.txt: 19 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 20 in [0, 20]
  [PASS] Merged dedup check: 100 unique
  [PASS] Alive subset check: best is subset of all
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_ngosang_best.txt vs ngosang_best.txt: identical
  [PASS] Consistency: trackers_ngosang_best_ip.txt vs ngosang_best_ip.txt: identical
  [PASS] Consistency: trackers_cf_best.txt vs cf_best.txt: identical
  [PASS] Consistency: trackers_gonghailink_best.txt vs gonghailink_best.txt: identical
  [PASS] Consistency: trackers_pandamen_best.txt vs pandamen_best.txt: identical
  [PASS] Consistency: trackers_gspu_best.txt vs gspu_best.txt: identical
  [PASS] Consistency: trackers_linuxjin_best.txt vs linuxjin_best.txt: identical
  [PASS] Consistency: trackers_alphacatmeow_best.txt vs alphacatmeow_best.txt: identical
  [PASS] Consistency: trackers_pexcn_best.txt vs pexcn_best.txt: identical
  [PASS] Consistency: trackers_ngosang_i2p.txt vs ngosang_i2p.txt: identical
  [PASS] Consistency: trackers_ngosang_yggdrasil.txt vs ngosang_yggdrasil.txt: identical
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
  Result: 70 passed, 0 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 3 rounds completed
   Total PASS: 210
   Total WARN: 0
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################
=== End of diagnostics (Thu Oct  8 11:05:37 UTC 2026) ===
