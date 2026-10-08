=== Diagnostics Thu Oct  8 13:51:06 UTC 2026 ===
Python: Python 3.12.15
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_best.txt
  HTTP 200, total 0.034550s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_best_ip.txt
  HTTP 200, total 0.145403s
>>> https://cf.trackerslist.com/best.txt
  HTTP 200, total 0.162983s
>>> https://tracker.adysec.com/trackers_best.txt
  HTTP 200, total 0.256244s
>>> https://raw.githubusercontent.com/gonghailink/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.103541s
>>> https://raw.githubusercontent.com/panda-men/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.132403s
>>> https://raw.githubusercontent.com/gspu/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.231664s
>>> https://raw.githubusercontent.com/linux-jin/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.131500s
>>> https://raw.githubusercontent.com/AlphaCatMeow/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.111670s
>>> https://raw.githubusercontent.com/pexcn/daily/gh-pages/trackerlist/trackerlist-best.txt
  HTTP 200, total 0.255194s
>>> https://raw.githubusercontent.com/1265578519/OpenTracker/refs/heads/master/tracker.txt
  HTTP 200, total 0.105685s
>>> https://trackers.run/s/rw_ws_up_hp_hs_v4_v6.txt
  HTTP 200, total 1.051856s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_i2p.txt
  HTTP 200, total 0.046237s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_yggdrasil.txt
  HTTP 200, total 0.037444s
[INFO] Repo: Pmwiu/Tracker-List, Max: 20
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/ngosang/trackerslist/master/blacklist.txt (391 URLs)
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/blacklist.txt (20 URLs)
[INFO] URL blacklist: 402 URLs (dynamic + remote sources)

[INFO] trackers_ngosang_best.txt (ngosang-best)
[OK]   20 unique

[INFO] trackers_ngosang_best_ip.txt (ngosang-best-ip)
[OK]   20 unique

[INFO] trackers_cf_best.txt (cf-best)
  [INFO] Skipped 15 dynamic-blacklisted lines
[OK]   56 unique

[INFO] trackers_adysec_best.txt (adysec-best)
  [INFO] Skipped 68 dynamic-blacklisted lines
[OK]   242 unique

[INFO] trackers_gonghailink_best.txt (gonghailink-best)
  [INFO] Skipped 5 dynamic-blacklisted lines
[OK]   15 unique

[INFO] trackers_pandamen_best.txt (pandamen-best)
  [INFO] Skipped 5 dynamic-blacklisted lines
[OK]   15 unique

[INFO] trackers_gspu_best.txt (gspu-best)
  [INFO] Skipped 4 dynamic-blacklisted lines
[OK]   16 unique

[INFO] trackers_linuxjin_best.txt (linuxjin-best)
[OK]   20 unique

[INFO] trackers_alphacatmeow_best.txt (alphacatmeow-best)
  [INFO] Skipped 8 dynamic-blacklisted lines
[OK]   12 unique

[INFO] trackers_pexcn_best.txt (pexcn-best)
  [INFO] Skipped 15 dynamic-blacklisted lines
[OK]   58 unique

[INFO] trackers_opentracker.txt (opentracker)
  [INFO] Skipped 8 dynamic-blacklisted lines
[OK]   30 unique

[INFO] trackers_run_ws.txt (trackersrun-ws)
  [INFO] Skipped 5 dynamic-blacklisted lines
[OK]   45 unique

[INFO] trackers_ngosang_i2p.txt (ngosang-i2p)
[OK]   17 unique

[INFO] trackers_ngosang_yggdrasil.txt (ngosang-yggdrasil)
[OK]   1 unique

[INFO] all 合并贡献: ngosang-best=20, ngosang-best-ip=13, cf-best=13, adysec-best=16, gonghailink-best=5, pandamen-best=2, gspu-best=2, linuxjin-best=0, alphacatmeow-best=0, pexcn-best=0, opentracker=7, trackersrun-ws=9, ngosang-i2p=12, ngosang-yggdrasil=1
[INFO] all 协议分布: http=48, https=16, udp=35, wss=1, ws=0

[OK]   merged: 100
[OK]   MIRRORS.txt
[OK]   /s/alive
[OK]   /s/all
[OK]   index.html
[OK]   docs/alive.txt
[OK]   docs/all.txt
[OK]   docs/merged.txt
[OK]   docs/ngosang_best.txt
[OK]   docs/ngosang_best_ip.txt
[OK]   docs/cf_best.txt
[OK]   docs/adysec_best.txt
[OK]   docs/gonghailink_best.txt
[OK]   docs/pandamen_best.txt
[OK]   docs/gspu_best.txt
[OK]   docs/linuxjin_best.txt
[OK]   docs/alphacatmeow_best.txt
[OK]   docs/pexcn_best.txt
[OK]   docs/opentracker.txt
[OK]   docs/run_ws.txt
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
  trackers_cf_best.txt: 56
  trackers_adysec_best.txt: 242
  trackers_gonghailink_best.txt: 15
  trackers_pandamen_best.txt: 15
  trackers_gspu_best.txt: 16
  trackers_linuxjin_best.txt: 20
  trackers_alphacatmeow_best.txt: 12
  trackers_pexcn_best.txt: 58
  trackers_opentracker.txt: 30
  trackers_run_ws.txt: 45
  trackers_ngosang_i2p.txt: 17
  trackers_ngosang_yggdrasil.txt: 1
  trackers_merged.txt: 100
  alive capped at 20 after test+sort
===================
[INFO] Testing 100 candidates (all-pool=100, timeout=10s, workers=30)
[INFO] Max alive trackers after scoring: 20
  [ALIVE] (3/100) http://207.241.226.111:6969/announce 82ms — announce with peers
  [ALIVE] (4/100) http://207.241.231.226:6969/announce 95ms — announce with peers
  [ALIVE] (5/100) http://004430.xyz:80/announce 153ms — announce with peers
  [ALIVE] (6/100) http://185.126.65.92:6969/announce 219ms — announce with peers
  [ALIVE] (8/100) http://94.23.207.177:6969/announce 224ms — announce with peers
  [ALIVE] (9/100) http://135.125.198.235:80/announce 243ms — announce with peers
  [ALIVE] (10/100) http://107.189.2.131:1337/announce 252ms — announce with peers
  [ALIVE] (11/100) http://135.125.198.235:2710/announce 253ms — announce with peers
  [ALIVE] (12/100) http://announce.sktorrent.eu:6969/announce 230ms — announce with peers
  [ALIVE] (13/100) http://ipv4announce.sktorrent.eu:6969/announce 212ms — announce with peers
  [ALIVE] (14/100) http://138.186.10.167:1337/announce 273ms — announce without peers
  [ALIVE] (15/100) http://152.249.214.196:6969/announce 288ms — announce with peers
  [ALIVE] (16/100) http://211.75.205.187:6969/announce 333ms — announce with peers
  [ALIVE] (17/100) http://211.75.210.221:80/announce 333ms — announce with peers
  [ALIVE] (18/100) http://211.75.210.221:6969/announce 338ms — announce with peers
  [ALIVE] (19/100) http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 273ms — announce with peers
  [ALIVE] (20/100) http://1337.abcvg.info:80/announce 394ms — announce with peers
  [ALIVE] (21/100) http://tracker.nyaa.vc:6969/announce 233ms — announce with peers
  [ALIVE] (24/100) https://004430.xyz:443/announce 221ms — announce with peers
  [ALIVE] (25/100) http://tracker.mywaifu.best:6969/announce 233ms — announce with peers
  [ALIVE] (26/100) http://tracker.dler.org:6969/announce 376ms — announce with peers
  [ALIVE] (27/100) http://tracker.qu.ax:6969/announce 227ms — announce with peers
  [ALIVE] (28/100) http://tracker.dler.com:6969/announce 353ms — announce with peers
  [ALIVE] (29/100) http://tracker.auctor.tv:6969/announce 210ms — announce with peers
  [ALIVE] (30/100) http://tracker.opentrackr.org:1337/announce 358ms — announce with peers
  [ALIVE] (31/100) https://2.tracker.eu.org:443/announce 89ms — announce with peers
  [ALIVE] (32/100) http://tracker.renfei.net:8080/announce 122ms — announce with peers
  [ALIVE] (33/100) https://open.ftorrent.com:443/announce 66ms — announce with peers
  [ALIVE] (34/100) https://3.tracker.eu.org:443/announce 81ms — announce with peers
  [ALIVE] (35/100) https://1.tracker.eu.org:443/announce 136ms — announce with peers
  [ALIVE] (36/100) https://4.tracker.eu.org:443/announce 110ms — announce with peers
  [ALIVE] (37/100) http://140.235.237.23:6969/announce 921ms — announce with peers
  [ALIVE] (38/100) https://t.213891.xyz:443/announce 133ms — announce with peers
  [ALIVE] (39/100) https://5.tracker.eu.org:443/announce 88ms — announce with peers
  [ALIVE] (40/100) https://337hhh.xyz:443/announce 353ms — announce with peers
  [ALIVE] (41/100) http://retracker01-msk-virt.corbina.net:80/announce 457ms — announce with peers
  [ALIVE] (42/100) udp://208.83.20.20:6969/announce 49ms — valid connect + announce
  [ALIVE] (43/100) udp://109.201.134.183:80/announce 114ms — valid connect + announce
  [ALIVE] (44/100) https://tracker.7471.top:443/announce 245ms — announce with peers
  [ALIVE] (45/100) udp://209.141.59.25:6969/announce 53ms — valid connect + announce
  [ALIVE] (46/100) udp://34.66.57.33:1337/announce 22ms — valid connect + announce
  [ALIVE] (47/100) udp://34.66.57.33:80/announce 28ms — valid connect + announce
  [ALIVE] (48/100) udp://135.125.198.235:1984/announce 125ms — valid connect + announce
  [ALIVE] (49/100) udp://151.242.104.187:80/announce 124ms — valid connect + announce
  [ALIVE] (50/100) udp://23.157.120.14:6969/announce 77ms — valid connect + announce
  [ALIVE] (51/100) http://211.75.205.187:80/announce 1236ms — announce with peers
  [ALIVE] (52/100) udp://185.121.168.96:1337/announce 165ms — valid connect + announce
  [ALIVE] (53/100) http://tracker.dhitechnical.com:6969/announce 921ms — announce with peers
  [ALIVE] (54/100) udp://exodus.desync.com:6969/announce 52ms — valid connect + announce
  [ALIVE] (55/100) https://retracker.x2k.ru:443/announce 510ms — announce with peers
  [ALIVE] (56/100) udp://explodie.org:6969/announce 73ms — valid connect + announce
  [ALIVE] (57/100) http://211.75.205.188:80/announce 1357ms — announce with peers
  [ALIVE] (58/100) udp://211.75.210.221:80/announce 170ms — valid connect + announce
  [ALIVE] (59/100) udp://31.56.179.159:6969/announce 142ms — valid connect + announce
  [ALIVE] (60/100) https://tracker.zhuqiy.com:443/announce 323ms — announce with peers
  [ALIVE] (61/100) udp://tracker.bittor.pw:1337/announce 20ms — valid connect + announce
  [ALIVE] (62/100) udp://tracker.corpscorp.online:80/announce 20ms — valid connect + announce
  [ALIVE] (63/100) udp://tracker.004430.xyz:1337/announce 48ms — valid connect + announce
  [ALIVE] (64/100) https://tracker.nekomi.cn:443/announce 156ms — announce with peers
  [ALIVE] (65/100) https://tracker.foreverpirates.co:443/announce 670ms — announce with peers
  [ALIVE] (66/100) udp://open.stealth.si:80/announce 121ms — valid connect + announce
  [ALIVE] (67/100) udp://retracker01-msk-virt.corbina.net:80/announce 154ms — valid connect + announce
  [ALIVE] (68/100) udp://tracker-udp.gbitt.info:80/announce 112ms — valid connect + announce
  [ALIVE] (69/100) udp://open.demonii.com:1337/announce 180ms — valid connect + announce
  [ALIVE] (70/100) udp://tracker.filemail.com:6969/announce 117ms — valid connect + announce
  [ALIVE] (71/100) udp://tracker.nyaa.vc:6969/announce 108ms — valid connect + announce
  [ALIVE] (72/100) udp://t.overflow.biz:6969/announce 145ms — valid connect + announce
  [ALIVE] (73/100) udp://tracker.opentrackr.org:1337/announce 120ms — valid connect + announce
  [ALIVE] (74/100) udp://tracker.gmi.gd:6969/announce 58ms — valid connect + announce
  [ALIVE] (75/100) udp://tracker.dler.org:6969/announce 182ms — valid connect + announce
  [ALIVE] (76/100) udp://tracker.qu.ax:6969/announce 115ms — valid connect + announce
  [ALIVE] (77/100) https://tracker.midnightprogrammer.net:443/announce 827ms — announce with peers
  [ALIVE] (78/100) udp://tracker.peerfect.org:6969/announce 136ms — valid connect + announce
  [ALIVE] (79/100) udp://tracker.ducks.party:1984/announce 118ms — valid connect + announce
  [ALIVE] (80/100) wss://tracker.openwebtorrent.com:443/announce 51ms — TLS reachable
  [ALIVE] (88/100) udp://tracker.skynetcloud.site:6969/announce 109ms — valid connect + announce
  [ALIVE] (90/100) udp://tracker2.dler.org:80/announce 168ms — valid connect + announce
  [ALIVE] (91/100) http://tracker.waaa.moe:6969/announce 1628ms — announce with peers
  [ALIVE] (96/100) udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 796ms — valid connect + announce
  [ALIVE] (98/100) udp://tracker.torrent.eu.org:451/announce 130ms — valid connect + announce
  [DEAD]  (100/100) udp://tracker.tryhackx.org:6969/announce — no connect response

[INFO] First pass done in 11.7s
[INFO] Second pass: re-testing top 80 alive trackers...
[INFO] Second pass done, refined 78 trackers
[INFO] Same-subnet(/24) dedup removed 39 slower tracker(s)

===== Test Summary =====
  Total tested:   100
  Alive (raw):    41
  Alive (final):  20 (top 20 by composite score)
  Non-UDP kept:   5 (quota >= 4)
  Classic kept:   3 (quota >= 4)
  Score-capped:   21
  Unsafe filtered:1
  Low-speed:      0 (>5s excluded)
  Same-subnet dedup:  39 (kept faster)
  Dead final:     66
  Time:           19.8s
=== 协议分布统计 ===
  HTTP  : 31 个
  HTTPS : 15 个
  UDP   : 33 个
  WSS   : 1 个
  WS    : 0 个
  总计: 80 个（存活）
=========================
[OK]   /s/alive
[OK]   /s/all
[OK]   index.html
[OK] Pages regenerated with alive statistics.
[OK]   docs/alive.txt
[OK]   docs/all.txt
[OK]   docs/merged.txt
[OK]   docs/ngosang_best.txt
[OK]   docs/ngosang_best_ip.txt
[OK]   docs/cf_best.txt
[OK]   docs/adysec_best.txt
[OK]   docs/gonghailink_best.txt
[OK]   docs/pandamen_best.txt
[OK]   docs/gspu_best.txt
[OK]   docs/linuxjin_best.txt
[OK]   docs/alphacatmeow_best.txt
[OK]   docs/pexcn_best.txt
[OK]   docs/opentracker.txt
[OK]   docs/run_ws.txt
[OK]   docs/ngosang_i2p.txt
[OK]   docs/ngosang_yggdrasil.txt
[OK]   docs/udp.txt
[OK]   docs/http.txt
[OK]   docs/https.txt
[OK]   docs/wss.txt
[OK]   docs/ws.txt
[OK] Plain-text files synced to docs/.

============================================================
 Round 1 - 2026-10-08 13:51:31
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 56 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 242 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 15 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 16 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 12 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 58 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 30 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 45 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 100 trackers
  [PASS] Local tracker: trackers_alive.txt: 20 trackers
  [PASS] Local tracker: trackers_all.txt: 41 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 20 trackers
  [PASS] Plain text: /all.txt: 41 trackers
  [PASS] Plain text: /merged.txt: 100 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 56 trackers
  [PASS] Plain text: /adysec_best.txt: 242 trackers
  [PASS] Plain text: /gonghailink_best.txt: 15 trackers
  [PASS] Plain text: /pandamen_best.txt: 15 trackers
  [PASS] Plain text: /gspu_best.txt: 16 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 12 trackers
  [PASS] Plain text: /pexcn_best.txt: 58 trackers
  [PASS] Plain text: /opentracker.txt: 30 trackers
  [PASS] Plain text: /run_ws.txt: 45 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 35 trackers
  [PASS] Plain text: /http.txt: 48 trackers
  [PASS] Plain text: /https.txt: 16 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 20 in [0, 20]
  [PASS] Merged dedup check: 100 unique
  [PASS] Alive subset check: best is subset of all
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_all.txt vs all.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_ngosang_best.txt vs ngosang_best.txt: identical
  [PASS] Consistency: trackers_ngosang_best_ip.txt vs ngosang_best_ip.txt: identical
  [PASS] Consistency: trackers_cf_best.txt vs cf_best.txt: identical
  [PASS] Consistency: trackers_adysec_best.txt vs adysec_best.txt: identical
  [PASS] Consistency: trackers_gonghailink_best.txt vs gonghailink_best.txt: identical
  [PASS] Consistency: trackers_pandamen_best.txt vs pandamen_best.txt: identical
  [PASS] Consistency: trackers_gspu_best.txt vs gspu_best.txt: identical
  [PASS] Consistency: trackers_linuxjin_best.txt vs linuxjin_best.txt: identical
  [PASS] Consistency: trackers_alphacatmeow_best.txt vs alphacatmeow_best.txt: identical
  [PASS] Consistency: trackers_pexcn_best.txt vs pexcn_best.txt: identical
  [PASS] Consistency: trackers_opentracker.txt vs opentracker.txt: identical
  [PASS] Consistency: trackers_run_ws.txt vs run_ws.txt: identical
  [PASS] Consistency: trackers_ngosang_i2p.txt vs ngosang_i2p.txt: identical
  [PASS] Consistency: trackers_ngosang_yggdrasil.txt vs ngosang_yggdrasil.txt: identical
  [PASS] Consistency: trackers_udp.txt vs udp.txt: identical
  [PASS] Consistency: trackers_http.txt vs http.txt: identical
  [PASS] Consistency: trackers_https.txt vs https.txt: identical
  [PASS] Consistency: trackers_wss.txt vs wss.txt: identical
  [PASS] Consistency: trackers_ws.txt vs ws.txt: identical
  [PASS] URL format check: all 100 valid
------------------------------------------------------------
  Result: 72 passed, 0 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 1 rounds completed
   Total PASS: 72
   Total WARN: 0
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################

============================================================
 Round 1 - 2026-10-08 13:51:41
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 56 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 242 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 15 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 16 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 12 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 58 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 30 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 45 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 100 trackers
  [PASS] Local tracker: trackers_alive.txt: 20 trackers
  [PASS] Local tracker: trackers_all.txt: 41 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 20 trackers
  [PASS] Plain text: /all.txt: 41 trackers
  [PASS] Plain text: /merged.txt: 100 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 56 trackers
  [PASS] Plain text: /adysec_best.txt: 242 trackers
  [PASS] Plain text: /gonghailink_best.txt: 15 trackers
  [PASS] Plain text: /pandamen_best.txt: 15 trackers
  [PASS] Plain text: /gspu_best.txt: 16 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 12 trackers
  [PASS] Plain text: /pexcn_best.txt: 58 trackers
  [PASS] Plain text: /opentracker.txt: 30 trackers
  [PASS] Plain text: /run_ws.txt: 45 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 35 trackers
  [PASS] Plain text: /http.txt: 48 trackers
  [PASS] Plain text: /https.txt: 16 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 20 in [0, 20]
  [PASS] Merged dedup check: 100 unique
  [PASS] Alive subset check: best is subset of all
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_all.txt vs all.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_ngosang_best.txt vs ngosang_best.txt: identical
  [PASS] Consistency: trackers_ngosang_best_ip.txt vs ngosang_best_ip.txt: identical
  [PASS] Consistency: trackers_cf_best.txt vs cf_best.txt: identical
  [PASS] Consistency: trackers_adysec_best.txt vs adysec_best.txt: identical
  [PASS] Consistency: trackers_gonghailink_best.txt vs gonghailink_best.txt: identical
  [PASS] Consistency: trackers_pandamen_best.txt vs pandamen_best.txt: identical
  [PASS] Consistency: trackers_gspu_best.txt vs gspu_best.txt: identical
  [PASS] Consistency: trackers_linuxjin_best.txt vs linuxjin_best.txt: identical
  [PASS] Consistency: trackers_alphacatmeow_best.txt vs alphacatmeow_best.txt: identical
  [PASS] Consistency: trackers_pexcn_best.txt vs pexcn_best.txt: identical
  [PASS] Consistency: trackers_opentracker.txt vs opentracker.txt: identical
  [PASS] Consistency: trackers_run_ws.txt vs run_ws.txt: identical
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
  [PASS] Worker all 短链: HTTP 200, 41 trackers
  [PASS] Worker best 加速: HTTP 200, 20 trackers
  [PASS] Worker all 加速: HTTP 200, 36 trackers
------------------------------------------------------------
  Result: 82 passed, 0 warnings, 0 failed
============================================================

============================================================
 Round 2 - 2026-10-08 13:51:47
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 56 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 242 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 15 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 16 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 12 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 58 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 30 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 45 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 100 trackers
  [PASS] Local tracker: trackers_alive.txt: 20 trackers
  [PASS] Local tracker: trackers_all.txt: 41 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 20 trackers
  [PASS] Plain text: /all.txt: 41 trackers
  [PASS] Plain text: /merged.txt: 100 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 56 trackers
  [PASS] Plain text: /adysec_best.txt: 242 trackers
  [PASS] Plain text: /gonghailink_best.txt: 15 trackers
  [PASS] Plain text: /pandamen_best.txt: 15 trackers
  [PASS] Plain text: /gspu_best.txt: 16 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 12 trackers
  [PASS] Plain text: /pexcn_best.txt: 58 trackers
  [PASS] Plain text: /opentracker.txt: 30 trackers
  [PASS] Plain text: /run_ws.txt: 45 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 35 trackers
  [PASS] Plain text: /http.txt: 48 trackers
  [PASS] Plain text: /https.txt: 16 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 20 in [0, 20]
  [PASS] Merged dedup check: 100 unique
  [PASS] Alive subset check: best is subset of all
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_all.txt vs all.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_ngosang_best.txt vs ngosang_best.txt: identical
  [PASS] Consistency: trackers_ngosang_best_ip.txt vs ngosang_best_ip.txt: identical
  [PASS] Consistency: trackers_cf_best.txt vs cf_best.txt: identical
  [PASS] Consistency: trackers_adysec_best.txt vs adysec_best.txt: identical
  [PASS] Consistency: trackers_gonghailink_best.txt vs gonghailink_best.txt: identical
  [PASS] Consistency: trackers_pandamen_best.txt vs pandamen_best.txt: identical
  [PASS] Consistency: trackers_gspu_best.txt vs gspu_best.txt: identical
  [PASS] Consistency: trackers_linuxjin_best.txt vs linuxjin_best.txt: identical
  [PASS] Consistency: trackers_alphacatmeow_best.txt vs alphacatmeow_best.txt: identical
  [PASS] Consistency: trackers_pexcn_best.txt vs pexcn_best.txt: identical
  [PASS] Consistency: trackers_opentracker.txt vs opentracker.txt: identical
  [PASS] Consistency: trackers_run_ws.txt vs run_ws.txt: identical
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
  [PASS] Worker all 短链: HTTP 200, 41 trackers
  [PASS] Worker best 加速: HTTP 200, 20 trackers
  [PASS] Worker all 加速: HTTP 200, 36 trackers
------------------------------------------------------------
  Result: 82 passed, 0 warnings, 0 failed
============================================================

============================================================
 Round 3 - 2026-10-08 13:51:53
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 56 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 242 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 15 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 16 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 12 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 58 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 30 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 45 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 100 trackers
  [PASS] Local tracker: trackers_alive.txt: 20 trackers
  [PASS] Local tracker: trackers_all.txt: 41 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 20 trackers
  [PASS] Plain text: /all.txt: 41 trackers
  [PASS] Plain text: /merged.txt: 100 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 56 trackers
  [PASS] Plain text: /adysec_best.txt: 242 trackers
  [PASS] Plain text: /gonghailink_best.txt: 15 trackers
  [PASS] Plain text: /pandamen_best.txt: 15 trackers
  [PASS] Plain text: /gspu_best.txt: 16 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 12 trackers
  [PASS] Plain text: /pexcn_best.txt: 58 trackers
  [PASS] Plain text: /opentracker.txt: 30 trackers
  [PASS] Plain text: /run_ws.txt: 45 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 35 trackers
  [PASS] Plain text: /http.txt: 48 trackers
  [PASS] Plain text: /https.txt: 16 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 20 in [0, 20]
  [PASS] Merged dedup check: 100 unique
  [PASS] Alive subset check: best is subset of all
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_all.txt vs all.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_ngosang_best.txt vs ngosang_best.txt: identical
  [PASS] Consistency: trackers_ngosang_best_ip.txt vs ngosang_best_ip.txt: identical
  [PASS] Consistency: trackers_cf_best.txt vs cf_best.txt: identical
  [PASS] Consistency: trackers_adysec_best.txt vs adysec_best.txt: identical
  [PASS] Consistency: trackers_gonghailink_best.txt vs gonghailink_best.txt: identical
  [PASS] Consistency: trackers_pandamen_best.txt vs pandamen_best.txt: identical
  [PASS] Consistency: trackers_gspu_best.txt vs gspu_best.txt: identical
  [PASS] Consistency: trackers_linuxjin_best.txt vs linuxjin_best.txt: identical
  [PASS] Consistency: trackers_alphacatmeow_best.txt vs alphacatmeow_best.txt: identical
  [PASS] Consistency: trackers_pexcn_best.txt vs pexcn_best.txt: identical
  [PASS] Consistency: trackers_opentracker.txt vs opentracker.txt: identical
  [PASS] Consistency: trackers_run_ws.txt vs run_ws.txt: identical
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
  [PASS] Worker all 短链: HTTP 200, 41 trackers
  [PASS] Worker best 加速: HTTP 200, 20 trackers
  [PASS] Worker all 加速: HTTP 200, 36 trackers
------------------------------------------------------------
  Result: 82 passed, 0 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 3 rounds completed
   Total PASS: 246
   Total WARN: 0
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################
=== End of diagnostics (Thu Oct  8 13:51:53 UTC 2026) ===
