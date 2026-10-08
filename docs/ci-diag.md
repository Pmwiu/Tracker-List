=== Diagnostics Thu Oct  8 06:25:31 UTC 2026 ===
Python: Python 3.12.14
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_best.txt
  HTTP 200, total 0.333963s
>>> https://cf.trackerslist.com/best.txt
  HTTP 200, total 0.106916s
>>> https://raw.githubusercontent.com/gonghailink/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.137374s
>>> https://raw.githubusercontent.com/panda-men/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.132854s
>>> https://raw.githubusercontent.com/gspu/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.107194s
>>> https://raw.githubusercontent.com/linux-jin/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.119718s
>>> https://raw.githubusercontent.com/AlphaCatMeow/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.114304s
>>> https://raw.githubusercontent.com/pexcn/daily/gh-pages/trackerlist/trackerlist-best.txt
  HTTP 200, total 0.121641s
[INFO] Repo: Pmwiu/Tracker-List, Max: 20

[INFO] trackers_ngosang_best.txt (ngosang-best)
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

[INFO] all 合并贡献: ngosang-best=20, cf-best=49, gonghailink-best=11, pandamen-best=6, gspu-best=5, linuxjin-best=1, alphacatmeow-best=3, pexcn-best=0
[INFO] all 协议分布: http=14, https=19, udp=61, wss=1, ws=0

[OK]   merged: 95
[OK]   MIRRORS.txt
[OK]   /s/alive
[OK]   /s/all
[OK]   index.html
[OK]   docs/alive.txt
[OK]   docs/merged.txt
[OK]   docs/ngosang_best.txt
[OK]   docs/cf_best.txt
[OK]   docs/gonghailink_best.txt
[OK]   docs/pandamen_best.txt
[OK]   docs/gspu_best.txt
[OK]   docs/linuxjin_best.txt
[OK]   docs/alphacatmeow_best.txt
[OK]   docs/pexcn_best.txt
[OK]   docs/udp.txt
[OK]   docs/http.txt
[OK]   docs/https.txt
[OK]   docs/wss.txt
[OK]   docs/ws.txt

===== Summary =====
  trackers_ngosang_best.txt: 20
  trackers_cf_best.txt: 71
  trackers_gonghailink_best.txt: 20
  trackers_pandamen_best.txt: 20
  trackers_gspu_best.txt: 20
  trackers_linuxjin_best.txt: 20
  trackers_alphacatmeow_best.txt: 20
  trackers_pexcn_best.txt: 73
  trackers_merged.txt: 95
  alive capped at 20 after test+sort
===================
[INFO] Testing 95 candidates (all-pool=95, timeout=10s, workers=30)
[INFO] Max alive trackers after scoring: 20
  [ALIVE] (2/95) https://t.213891.xyz:443/announce 36ms — valid announce response
  [ALIVE] (3/95) http://bt1.archive.org:6969/announce 64ms — valid announce response
  [ALIVE] (4/95) https://004430.xyz:443/announce 98ms — valid announce response
  [ALIVE] (5/95) http://bt2.archive.org:6969/announce 60ms — valid announce response
  [ALIVE] (7/95) https://tracker.foreverpirates.co:443/announce 195ms — valid announce response
  [ALIVE] (9/95) http://tracker.dhitechnical.com:6969/announce 211ms — valid announce response
  [ALIVE] (10/95) https://tracker.7471.top:443/announce 203ms — valid announce response
  [ALIVE] (11/95) http://tracker.renfei.net:8080/announce 129ms — valid announce response
  [ALIVE] (12/95) http://ipv4announce.sktorrent.eu:6969/announce 299ms — valid announce response
  [ALIVE] (13/95) https://tracker.midnightprogrammer.net:443/announce 292ms — valid announce response
  [ALIVE] (14/95) https://1337.abcvg.info:443/announce 320ms — valid announce response
  [ALIVE] (15/95) http://1337.abcvg.info:80/announce 321ms — valid announce response
  [ALIVE] (18/95) https://1.tracker.eu.org:443/announce 38ms — valid announce response
  [ALIVE] (20/95) https://tracker.nekomi.cn:443/announce 98ms — valid announce response
  [ALIVE] (21/95) udp://evan.im:6969/announce 61ms — valid connect + announce
  [ALIVE] (22/95) udp://leet-tracker.moe:1337/announce 51ms — valid connect + announce
  [ALIVE] (23/95) https://tracker.zhuqiy.com:443/announce 327ms — valid announce response
  [ALIVE] (24/95) https://tracker.qingwapt.org:443/announce 205ms — online (failure reason)
  [ALIVE] (25/95) udp://open.ftorrent.com:443/announce 28ms — valid connect + announce
  [ALIVE] (27/95) http://tracker.dler.org:6969/announce 532ms — valid announce response
  [ALIVE] (28/95) http://nyaa.tracker.wf:7777/announce 406ms — valid announce response
  [ALIVE] (29/95) http://tracker.mywaifu.best:6969/announce 342ms — valid announce response
  [ALIVE] (30/95) udp://open.demonii.com:1337/announce 135ms — valid connect + announce
  [ALIVE] (31/95) udp://explodie.org:6969/announce 60ms — valid connect + announce
  [ALIVE] (32/95) udp://martin-gebhardt.eu:25/announce 158ms — valid connect + announce
  [ALIVE] (33/95) udp://open.stealth.si:80/announce 155ms — valid connect + announce
  [ALIVE] (34/95) udp://tracker.004430.xyz:1337/announce 31ms — valid connect + announce
  [ALIVE] (35/95) udp://mail.segso.net:6969/announce 172ms — valid connect + announce
  [ALIVE] (36/95) udp://kolankoalastree.newtrackon.co.nz:1337/announce 171ms — valid connect + announce
  [ALIVE] (37/95) http://tracker.dler.com:6969/announce 516ms — valid announce response
  [ALIVE] (38/95) udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 361ms — valid connect + announce
  [ALIVE] (39/95) udp://torrent.tracker.durukanbal.com:6969/announce 149ms — valid connect + announce
  [ALIVE] (40/95) udp://tracker-udp.gbitt.info:80/announce 149ms — valid connect + announce
  [ALIVE] (41/95) udp://tracker.bittor.pw:1337/announce 54ms — valid connect + announce
  [ALIVE] (42/95) udp://tr4ck3r.duckdns.org:6969/announce 68ms — valid connect + announce
  [ALIVE] (43/95) http://tracker.waaa.moe:6969/announce 682ms — valid announce response
  [ALIVE] (44/95) udp://tracker.cn.nyaa.net:6969/announce 149ms — valid connect + announce
  [ALIVE] (45/95) udp://tracker.dler.com:6969/announce 132ms — valid connect + announce
  [ALIVE] (46/95) udp://tracker.dler.org:6969/announce 132ms — valid connect + announce
  [ALIVE] (47/95) udp://opentracker.lain.moscow:6969/announce 156ms — valid connect + announce
  [ALIVE] (48/95) udp://tracker.corpscorp.online:80/announce 58ms — valid connect + announce
  [ALIVE] (49/95) http://tracker.opentrackr.org:1337/announce 720ms — valid announce response
  [DEAD]  (50/95) http://www.wareztorrent.com:80/announce — RemoteDisconnected: Remote end closed connection without response
  [ALIVE] (51/95) udp://tracker.ducks.party:1984/announce 154ms — valid connect + announce
  [ALIVE] (52/95) udp://retracker01-msk-virt.corbina.net:80/announce 191ms — valid connect + announce
  [ALIVE] (53/95) udp://tracker.auctor.tv:6969/announce 153ms — valid connect + announce
  [ALIVE] (54/95) udp://tracker.farted.net:6969/announce 178ms — valid connect + announce
  [ALIVE] (55/95) udp://tracker.aruku.ovh:8081/announce 162ms — valid connect + announce
  [ALIVE] (56/95) udp://tracker.theoks.net:6969/announce 47ms — valid connect + announce
  [ALIVE] (57/95) udp://tracker.nyaa.vc:6969/announce 143ms — valid connect + announce
  [ALIVE] (58/95) udp://tracker.opentrackr.org:1337/announce 154ms — valid connect + announce
  [ALIVE] (59/95) udp://tracker.qu.ax:6969/announce 151ms — valid connect + announce
  [ALIVE] (60/95) udp://tracker.gmi.gd:6969/announce 40ms — valid connect + announce
  [ALIVE] (61/95) udp://tracker.nyaa.net:6969/announce 181ms — valid connect + announce
  [ALIVE] (62/95) udp://tracker.opentrackr.com:6969/announce 174ms — valid connect + announce
  [ALIVE] (63/95) udp://t.overflow.biz:6969/announce 176ms — valid connect + announce
  [ALIVE] (64/95) udp://tracker.wildkat.net:6969/announce 47ms — valid connect + announce
  [ALIVE] (65/95) udp://tracker.ilibr.org:6969/announce 176ms — valid connect + announce
  [ALIVE] (66/95) wss://tracker.openwebtorrent.com:443/announce 19ms — TLS reachable
  [ALIVE] (67/95) udp://tracker.skynetcloud.site:6969/announce 156ms — valid connect + announce
  [ALIVE] (68/95) udp://tracker.peerfect.org:6969/announce 176ms — valid connect + announce
  [ALIVE] (69/95) udp://tracker2.dler.org:80/announce 132ms — valid connect + announce
  [ALIVE] (70/95) udp://tracker.willy.pro:6969/announce 223ms — valid connect + announce
  [ALIVE] (71/95) udp://v2.iperson.xyz:6969/announce 203ms — valid connect + announce
  [ALIVE] (74/95) udp://tracker.torrent.eu.org:451/announce 169ms — valid connect + announce
  [ALIVE] (75/95) udp://zer0day.ch:1337/announce 157ms — valid connect + announce
  [ALIVE] (78/95) udp://tracker.filemail.com:6969/announce 150ms — valid connect (announce not confirmed)

[INFO] First pass done in 12.0s
[INFO] Second pass: re-testing top 66 alive trackers...
[INFO] Second pass done, refined 66 trackers
[INFO] Same-IP dedup removed 9 slower tracker(s)

===== Test Summary =====
  Total tested:   95
  Alive (raw):    57
  Alive (final):  20 (top 20 by composite score)
  Non-UDP kept:   4 (quota >= 4)
  Score-capped:   37
  Unsafe filtered:1
  Low-speed:      0 (>5s excluded)
  Same-IP dedup:  9 (kept faster)
  Dead final:     75
  Time:           15.3s
=== 协议分布统计 ===
  HTTP  : 12 个
  HTTPS : 10 个
  UDP   : 43 个
  WSS   : 1 个
  WS    : 0 个
  总计: 66 个（存活）
=========================
[OK]   /s/alive
[OK]   /s/all
[OK]   index.html
[OK] Pages regenerated with alive statistics.
[OK]   docs/alive.txt
[OK]   docs/merged.txt
[OK]   docs/ngosang_best.txt
[OK]   docs/cf_best.txt
[OK]   docs/gonghailink_best.txt
[OK]   docs/pandamen_best.txt
[OK]   docs/gspu_best.txt
[OK]   docs/linuxjin_best.txt
[OK]   docs/alphacatmeow_best.txt
[OK]   docs/pexcn_best.txt
[OK]   docs/udp.txt
[OK]   docs/http.txt
[OK]   docs/https.txt
[OK]   docs/wss.txt
[OK]   docs/ws.txt
[OK] Plain-text files synced to docs/.

============================================================
 Round 1 - 2026-10-08 06:25:50
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 71 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 20 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 20 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 20 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 20 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 73 trackers
  [PASS] Local tracker: trackers_merged.txt: 95 trackers
  [PASS] Local tracker: trackers_alive.txt: 20 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 20 trackers
  [PASS] Plain text: /merged.txt: 95 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 71 trackers
  [PASS] Plain text: /gonghailink_best.txt: 20 trackers
  [PASS] Plain text: /pandamen_best.txt: 20 trackers
  [PASS] Plain text: /gspu_best.txt: 20 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 20 trackers
  [PASS] Plain text: /pexcn_best.txt: 73 trackers
  [PASS] Plain text: /udp.txt: 61 trackers
  [PASS] Plain text: /http.txt: 14 trackers
  [PASS] Plain text: /https.txt: 19 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 20 in [0, 20]
  [PASS] Merged dedup check: 95 unique
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_ngosang_best.txt vs ngosang_best.txt: identical
  [PASS] Consistency: trackers_cf_best.txt vs cf_best.txt: identical
  [PASS] Consistency: trackers_gonghailink_best.txt vs gonghailink_best.txt: identical
  [PASS] Consistency: trackers_pandamen_best.txt vs pandamen_best.txt: identical
  [PASS] Consistency: trackers_gspu_best.txt vs gspu_best.txt: identical
  [PASS] Consistency: trackers_linuxjin_best.txt vs linuxjin_best.txt: identical
  [PASS] Consistency: trackers_alphacatmeow_best.txt vs alphacatmeow_best.txt: identical
  [PASS] Consistency: trackers_pexcn_best.txt vs pexcn_best.txt: identical
  [PASS] Consistency: trackers_udp.txt vs udp.txt: identical
  [PASS] Consistency: trackers_http.txt vs http.txt: identical
  [PASS] Consistency: trackers_https.txt vs https.txt: identical
  [PASS] Consistency: trackers_wss.txt vs wss.txt: identical
  [PASS] Consistency: trackers_ws.txt vs ws.txt: identical
  [PASS] URL format check: all 95 valid
------------------------------------------------------------
  Result: 50 passed, 0 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 1 rounds completed
   Total PASS: 50
   Total WARN: 0
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################

============================================================
 Round 1 - 2026-10-08 06:25:57
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 71 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 20 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 20 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 20 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 20 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 73 trackers
  [PASS] Local tracker: trackers_merged.txt: 95 trackers
  [PASS] Local tracker: trackers_alive.txt: 20 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 20 trackers
  [PASS] Plain text: /merged.txt: 95 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 71 trackers
  [PASS] Plain text: /gonghailink_best.txt: 20 trackers
  [PASS] Plain text: /pandamen_best.txt: 20 trackers
  [PASS] Plain text: /gspu_best.txt: 20 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 20 trackers
  [PASS] Plain text: /pexcn_best.txt: 73 trackers
  [PASS] Plain text: /udp.txt: 61 trackers
  [PASS] Plain text: /http.txt: 14 trackers
  [PASS] Plain text: /https.txt: 19 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 20 in [0, 20]
  [PASS] Merged dedup check: 95 unique
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_ngosang_best.txt vs ngosang_best.txt: identical
  [PASS] Consistency: trackers_cf_best.txt vs cf_best.txt: identical
  [PASS] Consistency: trackers_gonghailink_best.txt vs gonghailink_best.txt: identical
  [PASS] Consistency: trackers_pandamen_best.txt vs pandamen_best.txt: identical
  [PASS] Consistency: trackers_gspu_best.txt vs gspu_best.txt: identical
  [PASS] Consistency: trackers_linuxjin_best.txt vs linuxjin_best.txt: identical
  [PASS] Consistency: trackers_alphacatmeow_best.txt vs alphacatmeow_best.txt: identical
  [PASS] Consistency: trackers_pexcn_best.txt vs pexcn_best.txt: identical
  [PASS] Consistency: trackers_udp.txt vs udp.txt: identical
  [PASS] Consistency: trackers_http.txt vs http.txt: identical
  [PASS] Consistency: trackers_https.txt vs https.txt: identical
  [PASS] Consistency: trackers_wss.txt vs wss.txt: identical
  [PASS] Consistency: trackers_ws.txt vs ws.txt: identical
  [PASS] URL format check: all 95 valid
  [PASS] Raw: alive (Raw): HTTP 200, 20 trackers
  [PASS] Raw: merged (Raw): HTTP 200, 95 trackers
  [PASS] Pages: /alive.txt: HTTP 200, 20 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 95 trackers
  [PASS] Pages short: /s/alive: HTTP 200, redirect OK
  [PASS] Pages short: /s/all: HTTP 200, redirect OK
  [PASS] Worker best 短链: HTTP 200, 20 trackers
  [PASS] Worker all 短链: HTTP 200, 95 trackers
  [PASS] Worker best 加速: HTTP 200, 20 trackers
  [PASS] Worker all 加速: HTTP 200, 100 trackers
------------------------------------------------------------
  Result: 60 passed, 0 warnings, 0 failed
============================================================

============================================================
 Round 2 - 2026-10-08 06:26:03
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 71 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 20 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 20 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 20 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 20 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 73 trackers
  [PASS] Local tracker: trackers_merged.txt: 95 trackers
  [PASS] Local tracker: trackers_alive.txt: 20 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 20 trackers
  [PASS] Plain text: /merged.txt: 95 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 71 trackers
  [PASS] Plain text: /gonghailink_best.txt: 20 trackers
  [PASS] Plain text: /pandamen_best.txt: 20 trackers
  [PASS] Plain text: /gspu_best.txt: 20 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 20 trackers
  [PASS] Plain text: /pexcn_best.txt: 73 trackers
  [PASS] Plain text: /udp.txt: 61 trackers
  [PASS] Plain text: /http.txt: 14 trackers
  [PASS] Plain text: /https.txt: 19 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 20 in [0, 20]
  [PASS] Merged dedup check: 95 unique
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_ngosang_best.txt vs ngosang_best.txt: identical
  [PASS] Consistency: trackers_cf_best.txt vs cf_best.txt: identical
  [PASS] Consistency: trackers_gonghailink_best.txt vs gonghailink_best.txt: identical
  [PASS] Consistency: trackers_pandamen_best.txt vs pandamen_best.txt: identical
  [PASS] Consistency: trackers_gspu_best.txt vs gspu_best.txt: identical
  [PASS] Consistency: trackers_linuxjin_best.txt vs linuxjin_best.txt: identical
  [PASS] Consistency: trackers_alphacatmeow_best.txt vs alphacatmeow_best.txt: identical
  [PASS] Consistency: trackers_pexcn_best.txt vs pexcn_best.txt: identical
  [PASS] Consistency: trackers_udp.txt vs udp.txt: identical
  [PASS] Consistency: trackers_http.txt vs http.txt: identical
  [PASS] Consistency: trackers_https.txt vs https.txt: identical
  [PASS] Consistency: trackers_wss.txt vs wss.txt: identical
  [PASS] Consistency: trackers_ws.txt vs ws.txt: identical
  [PASS] URL format check: all 95 valid
  [PASS] Raw: alive (Raw): HTTP 200, 20 trackers
  [PASS] Raw: merged (Raw): HTTP 200, 95 trackers
  [PASS] Pages: /alive.txt: HTTP 200, 20 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 95 trackers
  [PASS] Pages short: /s/alive: HTTP 200, redirect OK
  [PASS] Pages short: /s/all: HTTP 200, redirect OK
  [PASS] Worker best 短链: HTTP 200, 20 trackers
  [PASS] Worker all 短链: HTTP 200, 95 trackers
  [PASS] Worker best 加速: HTTP 200, 20 trackers
  [PASS] Worker all 加速: HTTP 200, 100 trackers
------------------------------------------------------------
  Result: 60 passed, 0 warnings, 0 failed
============================================================

============================================================
 Round 3 - 2026-10-08 06:26:08
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 71 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 20 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 20 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 20 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 20 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 73 trackers
  [PASS] Local tracker: trackers_merged.txt: 95 trackers
  [PASS] Local tracker: trackers_alive.txt: 20 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 20 trackers
  [PASS] Plain text: /merged.txt: 95 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 71 trackers
  [PASS] Plain text: /gonghailink_best.txt: 20 trackers
  [PASS] Plain text: /pandamen_best.txt: 20 trackers
  [PASS] Plain text: /gspu_best.txt: 20 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 20 trackers
  [PASS] Plain text: /pexcn_best.txt: 73 trackers
  [PASS] Plain text: /udp.txt: 61 trackers
  [PASS] Plain text: /http.txt: 14 trackers
  [PASS] Plain text: /https.txt: 19 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 20 in [0, 20]
  [PASS] Merged dedup check: 95 unique
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_ngosang_best.txt vs ngosang_best.txt: identical
  [PASS] Consistency: trackers_cf_best.txt vs cf_best.txt: identical
  [PASS] Consistency: trackers_gonghailink_best.txt vs gonghailink_best.txt: identical
  [PASS] Consistency: trackers_pandamen_best.txt vs pandamen_best.txt: identical
  [PASS] Consistency: trackers_gspu_best.txt vs gspu_best.txt: identical
  [PASS] Consistency: trackers_linuxjin_best.txt vs linuxjin_best.txt: identical
  [PASS] Consistency: trackers_alphacatmeow_best.txt vs alphacatmeow_best.txt: identical
  [PASS] Consistency: trackers_pexcn_best.txt vs pexcn_best.txt: identical
  [PASS] Consistency: trackers_udp.txt vs udp.txt: identical
  [PASS] Consistency: trackers_http.txt vs http.txt: identical
  [PASS] Consistency: trackers_https.txt vs https.txt: identical
  [PASS] Consistency: trackers_wss.txt vs wss.txt: identical
  [PASS] Consistency: trackers_ws.txt vs ws.txt: identical
  [PASS] URL format check: all 95 valid
  [PASS] Raw: alive (Raw): HTTP 200, 20 trackers
  [PASS] Raw: merged (Raw): HTTP 200, 95 trackers
  [PASS] Pages: /alive.txt: HTTP 200, 20 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 95 trackers
  [PASS] Pages short: /s/alive: HTTP 200, redirect OK
  [PASS] Pages short: /s/all: HTTP 200, redirect OK
  [PASS] Worker best 短链: HTTP 200, 20 trackers
  [PASS] Worker all 短链: HTTP 200, 95 trackers
  [PASS] Worker best 加速: HTTP 200, 20 trackers
  [PASS] Worker all 加速: HTTP 200, 100 trackers
------------------------------------------------------------
  Result: 60 passed, 0 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 3 rounds completed
   Total PASS: 180
   Total WARN: 0
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################
=== End of diagnostics (Thu Oct  8 06:26:08 UTC 2026) ===
