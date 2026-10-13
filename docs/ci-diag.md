=== Diagnostics Tue Oct 13 05:18:28 UTC 2026 ===
Python: Python 3.12.15
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_best.txt
  HTTP 200, total 0.097168s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_best_ip.txt
  HTTP 200, total 0.058758s
>>> https://cf.trackerslist.com/best.txt
  HTTP 200, total 0.166257s
>>> https://tracker.adysec.com/trackers_best.txt
  HTTP 200, total 0.145308s
>>> https://raw.githubusercontent.com/gonghailink/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.139573s
>>> https://raw.githubusercontent.com/panda-men/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.119053s
>>> https://raw.githubusercontent.com/gspu/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.136050s
>>> https://raw.githubusercontent.com/linux-jin/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.149134s
>>> https://raw.githubusercontent.com/AlphaCatMeow/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.136120s
>>> https://raw.githubusercontent.com/pexcn/daily/gh-pages/trackerlist/trackerlist-best.txt
  HTTP 200, total 0.109734s
>>> https://raw.githubusercontent.com/1265578519/OpenTracker/refs/heads/master/tracker.txt
  HTTP 200, total 0.151476s
>>> https://trackers.run/s/rw_ws_up_hp_hs_v4_v6.txt
  HTTP 200, total 2.689529s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_i2p.txt
  HTTP 200, total 0.088131s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_yggdrasil.txt
  HTTP 200, total 0.119768s
[OK]   1347 new candidates -> candidates_20261013.txt
[OK]   1347 new candidates
[INFO] Repo: Pmwiu/Tracker-List, Max: 25
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/ngosang/trackerslist/master/blacklist.txt (391 URLs)
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/blacklist.txt (20 URLs)
[INFO] URL blacklist: 390 URLs (dynamic + remote sources)
[INFO] discovered candidates: 1347 URLs in 1 file(s)

[INFO] trackers_ngosang_best.txt (ngosang-best)
[OK]   20 unique

[INFO] trackers_ngosang_best_ip.txt (ngosang-best-ip)
[OK]   20 unique

[INFO] trackers_cf_best.txt (cf-best)
  [INFO] Skipped 10 dynamic-blacklisted lines
[OK]   60 unique

[INFO] trackers_adysec_best.txt (adysec-best)
  [INFO] Skipped 71 dynamic-blacklisted lines
[OK]   249 unique

[INFO] trackers_gonghailink_best.txt (gonghailink-best)
  [INFO] Skipped 3 dynamic-blacklisted lines
[OK]   17 unique

[INFO] trackers_pandamen_best.txt (pandamen-best)
  [INFO] Skipped 2 dynamic-blacklisted lines
[OK]   18 unique

[INFO] trackers_gspu_best.txt (gspu-best)
  [INFO] Skipped 1 dynamic-blacklisted lines
[OK]   19 unique

[INFO] trackers_linuxjin_best.txt (linuxjin-best)
[OK]   20 unique

[INFO] trackers_alphacatmeow_best.txt (alphacatmeow-best)
  [INFO] Skipped 5 dynamic-blacklisted lines
[OK]   15 unique

[INFO] trackers_pexcn_best.txt (pexcn-best)
  [INFO] Skipped 10 dynamic-blacklisted lines
[OK]   63 unique

[INFO] trackers_opentracker.txt (opentracker)
  [INFO] Skipped 8 dynamic-blacklisted lines
[OK]   27 unique

[INFO] trackers_run_ws.txt (trackersrun-ws)
  [INFO] Skipped 2 dynamic-blacklisted lines
[OK]   44 unique

[INFO] trackers_ngosang_i2p.txt (ngosang-i2p)
[OK]   17 unique

[INFO] trackers_ngosang_yggdrasil.txt (ngosang-yggdrasil)
  [INFO] Skipped 1 dynamic-blacklisted lines
[WARN] trackers_ngosang_yggdrasil.txt failed (No valid trackers found in response); using backup (1 trackers)
[OK]   1 unique

[INFO] all 合并贡献: ngosang-best=20, ngosang-best-ip=20, cf-best=26, adysec-best=29, gonghailink-best=6, pandamen-best=7, gspu-best=3, linuxjin-best=1, alphacatmeow-best=3, pexcn-best=1, opentracker=14, trackersrun-ws=20, ngosang-i2p=17, ngosang-yggdrasil=1
[INFO] all 协议分布: http=99, https=20, udp=80, wss=1, ws=0

[OK]   merged: 200
[OK]   source_counts.json (200)
[OK]   discovered_set.json (1347)
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
  trackers_cf_best.txt: 60
  trackers_adysec_best.txt: 249
  trackers_gonghailink_best.txt: 17
  trackers_pandamen_best.txt: 18
  trackers_gspu_best.txt: 19
  trackers_linuxjin_best.txt: 20
  trackers_alphacatmeow_best.txt: 15
  trackers_pexcn_best.txt: 63
  trackers_opentracker.txt: 27
  trackers_run_ws.txt: 44
  trackers_ngosang_i2p.txt: 17
  trackers_ngosang_yggdrasil.txt: 1
  trackers_merged.txt: 200
  alive capped at 25 after test+sort
===================
[INFO] Testing 200 candidates (all-pool=200, timeout=10s, workers=30)
[INFO] Max alive trackers after scoring: 25
  [ALIVE] (4/200) http://004430.xyz:80/announce 97ms — announce with peers
  [ALIVE] (5/200) http://135.125.198.235:2710/announce 245ms — announce with peers
  [ALIVE] (6/200) http://135.125.198.235:80/announce 246ms — announce with peers
  [ALIVE] (7/200) http://1337.abcvg.info:80/announce 295ms — announce with peers
  [ALIVE] (8/200) http://138.186.10.167:1337/announce 238ms — announce without peers
  [ALIVE] (9/200) http://107.189.2.131:1337/announce 1342ms — announce with peers
  [ALIVE] (12/200) http://207.241.226.111:6969/announce 69ms — announce with peers
  [ALIVE] (13/200) http://207.241.231.226:6969/announce 104ms — announce with peers
  [ALIVE] (14/200) http://185.126.65.92:6969/announce 238ms — announce with peers
  [ALIVE] (15/200) http://211.75.205.187:6969/announce 328ms — announce with peers
  [ALIVE] (16/200) http://211.75.205.187:80/announce 332ms — announce with peers
  [ALIVE] (17/200) http://211.75.205.188:80/announce 316ms — announce with peers
  [ALIVE] (18/200) http://211.75.205.188:6969/announce 332ms — announce with peers
  [ALIVE] (19/200) http://211.75.210.221:6969/announce 315ms — announce with peers
  [ALIVE] (20/200) http://211.75.210.221:80/announce 316ms — announce with peers
  [ALIVE] (21/200) http://216.144.239.90:6969/announce 71ms — announce with peers
  [ALIVE] (22/200) http://31.38.161.123:6969/announce 253ms — announce with peers
  [ALIVE] (23/200) http://140.235.237.23:6969/announce 5116ms — announce with peers
  [DEAD]  (25/200) http://119.28.71.45:8080/announce — URLError: <urlopen error timed out>
  [ALIVE] (49/200) http://43.250.54.126:6969/announce 234ms — announce with peers
  [ALIVE] (50/200) http://93.158.213.92:1337/announce 235ms — announce with peers
  [ALIVE] (51/200) http://94.23.207.177:6969/announce 238ms — announce with peers
  [ALIVE] (53/200) http://announce.sktorrent.eu:6969/announce 260ms — announce with peers
  [ALIVE] (54/200) http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 265ms — announce with peers
  [ALIVE] (59/200) http://ipv4announce.sktorrent.eu:6969/announce 233ms — announce with peers
  [ALIVE] (61/200) http://tracker.auctor.tv:6969/announce 228ms — announce with peers
  [ALIVE] (62/200) http://tracker.mywaifu.best:6969/announce 281ms — announce with peers
  [ALIVE] (63/200) http://retracker01-msk-virt.corbina.net:80/announce 585ms — announce with peers
  [ALIVE] (64/200) http://tracker.qu.ax:6969/announce 231ms — announce with peers
  [ALIVE] (66/200) http://tracker.waaa.moe:6969/announce 170ms — announce with peers
  [ALIVE] (67/200) http://tracker.renfei.net:8080/announce 97ms — announce with peers
  [ALIVE] (74/200) https://004430.xyz:443/announce 119ms — announce with peers
  [SKIP]   (75/200) http://opentracker.eeptorrent.i2p:80/a — I2P network required
  [ALIVE] (80/200) https://1.tracker.eu.org:443/announce 64ms — announce with peers
  [ALIVE] (81/200) https://t.213891.xyz:443/announce 53ms — announce with peers
  [ALIVE] (83/200) https://4.tracker.eu.org:443/announce 72ms — announce with peers
  [ALIVE] (85/200) https://3.tracker.eu.org:443/announce 63ms — announce with peers
  [ALIVE] (87/200) https://337hhh.xyz:443/announce 363ms — announce with peers
  [ALIVE] (88/200) https://2.tracker.eu.org:443/announce 68ms — announce with peers
  [ALIVE] (90/200) https://tracker.7471.top:443/announce 187ms — announce with peers
  [ALIVE] (92/200) https://tracker.foreverpirates.co:443/announce 218ms — announce with peers
  [ALIVE] (93/200) https://tr.nyacat.pw:443/announce 291ms — announce with peers
  [ALIVE] (95/200) udp://109.201.134.183:80/announce 118ms — valid connect + announce (v4)
  [ALIVE] (96/200) udp://135.125.198.235:1984/announce 127ms — valid connect + announce (v4)
  [ALIVE] (97/200) udp://132.226.6.145:6969/announce 131ms — valid connect + announce (v4)
  [ALIVE] (98/200) udp://193.148.251.93:6969/announce 52ms — valid connect + announce (v4)
  [ALIVE] (99/200) udp://151.242.104.187:80/announce 130ms — valid connect + announce (v4)
  [ALIVE] (100/200) udp://209.141.59.25:6969/announce 69ms — valid connect + announce (v4)
  [ALIVE] (101/200) http://tracker.dhitechnical.com:6969/announce 2728ms — announce with peers
  [ALIVE] (102/200) udp://185.121.168.96:1337/announce 150ms — valid connect + announce (v4)
  [ALIVE] (103/200) https://tracker.nekomi.cn:443/announce 120ms — announce with peers
  [ALIVE] (104/200) udp://34.66.57.33:1337/announce 32ms — valid connect + announce (v4)
  [ALIVE] (105/200) udp://34.66.57.33:80/announce 36ms — valid connect + announce (v4)
  [ALIVE] (106/200) udp://23.157.120.14:6969/announce 85ms — valid connect + announce (v4)
  [ALIVE] (107/200) udp://193.34.92.5:80/announce 153ms — valid connect + announce (v4)
  [ALIVE] (108/200) udp://211.75.205.187:6969/announce 159ms — valid connect + announce (v4)
  [ALIVE] (109/200) udp://211.75.205.187:80/announce 160ms — valid connect + announce (v4)
  [ALIVE] (110/200) udp://51.81.222.188:6969/announce 55ms — valid connect + announce (v4)
  [ALIVE] (111/200) udp://31.56.179.159:6969/announce 140ms — valid connect + announce (v4)
  [ALIVE] (113/200) udp://43.250.54.126:6969/announce 113ms — valid connect + announce (v4)
  [ALIVE] (114/200) udp://51.15.41.46:6969/announce 120ms — valid connect + announce (v4)
  [ALIVE] (115/200) udp://45.137.199.107:6969/announce 121ms — valid connect + announce (v4)
  [ALIVE] (116/200) udp://43.154.112.29:17272/announce 170ms — valid connect + announce (v4)
  [ALIVE] (117/200) https://tracker.midnightprogrammer.net:443/announce 932ms — announce with peers
  [ALIVE] (119/200) udp://65.109.28.33:6969/announce 147ms — valid connect + announce (v4)
  [ALIVE] (122/200) udp://65.109.28.17:6969/announce 150ms — valid connect + announce (v4)
  [ALIVE] (123/200) udp://93.158.213.92:1337/announce 117ms — valid connect + announce (v4)
  [ALIVE] (124/200) udp://89.234.156.205:451/announce 123ms — valid connect + announce (v4)
  [ALIVE] (125/200) udp://83.102.180.21:80/announce 167ms — valid connect + announce (v4)
  [ALIVE] (126/200) udp://93.158.213.92:6969/announce 125ms — valid connect + announce (v4)
  [ALIVE] (128/200) udp://95.217.80.20:6969/announce 146ms — valid connect + announce (v4)
  [ALIVE] (129/200) udp://evan.im:6969/announce 32ms — valid connect + announce (v4)
  [ALIVE] (130/200) udp://95.217.80.22:6969/announce 151ms — valid connect + announce (v4)
  [ALIVE] (131/200) udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 132ms — valid connect + announce (v4)
  [ALIVE] (133/200) udp://ipv4announce.sktorrent.eu:6969/announce 121ms — valid connect + announce (v4)
  [ALIVE] (134/200) udp://explodie.org:6969/announce 87ms — valid connect + announce (v4)
  [ALIVE] (135/200) udp://mail.segso.net:6969/announce 153ms — valid connect + announce (v4)
  [ALIVE] (143/200) udp://open.stealth.si:80/announce 138ms — valid connect + announce (v4)
  [ALIVE] (144/200) udp://open.demonii.com:1337/announce 151ms — valid connect + announce (v4)
  [ALIVE] (145/200) udp://kolankoalastree.newtrackon.co.nz:1337/announce 179ms — valid connect + announce (v4)
  [ALIVE] (146/200) udp://retracker01-msk-virt.corbina.net:80/announce 167ms — valid connect + announce (v4)
  [ALIVE] (147/200) udp://martin-gebhardt.eu:25/announce 133ms — valid connect + announce (v4)
  [ALIVE] (148/200) udp://t.overflow.biz:6969/announce 140ms — valid connect + announce (v4)
  [ALIVE] (149/200) udp://opentracker.lain.moscow:6969/announce 129ms — valid connect + announce (v4)
  [ALIVE] (150/200) udp://tracker.004430.xyz:1337/announce 36ms — valid connect + announce (v4)
  [ALIVE] (151/200) udp://tracker.bittor.pw:1337/announce 35ms — valid connect + announce (v4)
  [ALIVE] (152/200) udp://tracker.corpscorp.online:80/announce 39ms — valid connect + announce (v4)
  [ALIVE] (153/200) http://tracker.nyaa.vc:6969/announce 243ms — announce with peers
  [ALIVE] (154/200) udp://tracker.dler.org:6969/announce 160ms — valid connect + announce (v4)
  [ALIVE] (156/200) udp://tracker.farted.net:6969/announce 137ms — valid connect + announce (v4)
  [ALIVE] (157/200) udp://tracker.ducks.party:1984/announce 134ms — valid connect + announce (v4)
  [ALIVE] (158/200) udp://tracker.nyaa.vc:6969/announce 123ms — valid connect + announce (v4)
  [ALIVE] (160/200) udp://tracker.opentrackr.org:1337/announce 123ms — valid connect + announce (v4)
  [ALIVE] (162/200) udp://tracker.qu.ax:6969/announce 121ms — valid connect + announce (v4)
  [ALIVE] (163/200) udp://tracker.skynetcloud.site:6969/announce 114ms — valid connect + announce (v4)
  [ALIVE] (166/200) udp://tracker.tryhackx.org:6969/announce 132ms — valid connect + announce (v4)
  [ALIVE] (167/200) udp://52.58.128.163:6969/announce 129ms — valid connect + announce (v4)
  [ALIVE] (168/200) udp://tracker.torrent.eu.org:451/announce 144ms — valid connect + announce (v4)
  [ALIVE] (169/200) udp://tr4ck3r.duckdns.org:6969/announce 53ms — valid connect + announce (v4)
  [ALIVE] (170/200) http://tracker.opentrackr.org:1337/announce 2535ms — announce with peers
  [ALIVE] (172/200) udp://open.ftorrent.com:443/announce 23ms — valid connect + announce (v4)
  [ALIVE] (175/200) http://tracker.dler.org:6969/announce 4238ms — announce with peers
  [ALIVE] (176/200) udp://tracker2.dler.org:80/announce 160ms — valid connect + announce (v4)
  [ALIVE] (177/200) http://tracker.dler.com:6969/announce 3890ms — announce with peers
  [ALIVE] (178/200) udp://tracker-udp.gbitt.info:80/announce 117ms — valid connect + announce (v4)
  [ALIVE] (179/200) udp://tracker.gmi.gd:6969/announce 42ms — valid connect + announce (v4)
  [ALIVE] (180/200) udp://tracker.peerfect.org:6969/announce 148ms — valid connect + announce (v4)
  [ALIVE] (184/200) http://tracker2.dler.org:80/announce 3687ms — announce with peers
  [ALIVE] (189/200) udp://exodus.desync.com:6969/announce 49ms — valid connect + announce
  [ALIVE] (190/200) udp://tracker.filemail.com:6969/announce 121ms — valid connect + announce
  [DEAD]  (200/200) udp://opentor.org:2710/announce — no connect response

[INFO] First pass done in 38.1s
[INFO] Multi-sample: 3 samples on top 50 alive trackers...
[INFO] Multi-sample refined 50 trackers (median + jitter penalty)
[INFO] Low-speed filtered (>5s): 1 trackers
[INFO] Same-subnet(/24) dedup removed 53 slower tracker(s)
[INFO] discovered candidates excluded from best/all: 1347
[INFO] Dynamic blacklist: 1 consistently-dead trackers

===== Test Summary =====
  Total tested:   200
  Alive (raw):    54
  Alive (final):  25 (top 25 by composite score)
  Non-UDP kept:   8 (quota >= 4)
  Classic kept:   4 (quota >= 4)
  Score-capped:   29
  Unsafe filtered:2
  Low-speed:      1 (>5s excluded)
  Same-subnet dedup:  53 (kept faster)
  Dead final:     154
  Time:           55.4s
=== 协议分布统计 ===
  HTTP  : 36 个
  HTTPS : 12 个
  UDP   : 60 个
  WSS   : 0 个
  WS    : 0 个
  总计: 108 个（存活）
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
 Round 1 - 2026-10-13 05:19:37
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 60 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 249 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 17 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 18 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 19 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 63 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 27 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 44 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_all.txt: 54 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1347 candidates in 1 file(s)
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /all.txt: 54 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 60 trackers
  [PASS] Plain text: /adysec_best.txt: 249 trackers
  [PASS] Plain text: /gonghailink_best.txt: 17 trackers
  [PASS] Plain text: /pandamen_best.txt: 18 trackers
  [PASS] Plain text: /gspu_best.txt: 19 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 15 trackers
  [PASS] Plain text: /pexcn_best.txt: 63 trackers
  [PASS] Plain text: /opentracker.txt: 27 trackers
  [PASS] Plain text: /run_ws.txt: 44 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 80 trackers
  [PASS] Plain text: /http.txt: 99 trackers
  [PASS] Plain text: /https.txt: 20 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset-of-all check: all 25 best trackers present in all (54)
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
  [PASS] URL format check: all 200 valid
------------------------------------------------------------
  Result: 73 passed, 0 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 1 rounds completed
   Total PASS: 73
   Total WARN: 0
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################

============================================================
 Round 1 - 2026-10-13 05:19:46
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 60 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 249 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 17 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 18 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 19 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 63 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 27 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 44 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_all.txt: 54 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1347 candidates in 1 file(s)
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /all.txt: 54 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 60 trackers
  [PASS] Plain text: /adysec_best.txt: 249 trackers
  [PASS] Plain text: /gonghailink_best.txt: 17 trackers
  [PASS] Plain text: /pandamen_best.txt: 18 trackers
  [PASS] Plain text: /gspu_best.txt: 19 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 15 trackers
  [PASS] Plain text: /pexcn_best.txt: 63 trackers
  [PASS] Plain text: /opentracker.txt: 27 trackers
  [PASS] Plain text: /run_ws.txt: 44 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 80 trackers
  [PASS] Plain text: /http.txt: 99 trackers
  [PASS] Plain text: /https.txt: 20 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset-of-all check: all 25 best trackers present in all (54)
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
  [PASS] URL format check: all 200 valid
  [PASS] Raw: alive (Raw): HTTP 200, 25 trackers
  [PASS] Raw: merged (Raw): HTTP 200, 200 trackers
  [PASS] Pages: /alive.txt: HTTP 200, 25 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 200 trackers
  [PASS] Pages short: /s/alive: HTTP 200, redirect OK
  [PASS] Pages short: /s/all: HTTP 200, redirect OK
  [PASS] Worker best 短链: HTTP 200, 25 trackers
  [PASS] Worker all 短链: HTTP 200, 54 trackers
  [PASS] Worker best 加速: HTTP 200, 25 trackers
  [PASS] Worker all 加速: HTTP 200, 59 trackers
------------------------------------------------------------
  Result: 83 passed, 0 warnings, 0 failed
============================================================

============================================================
 Round 2 - 2026-10-13 05:19:51
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 60 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 249 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 17 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 18 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 19 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 63 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 27 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 44 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_all.txt: 54 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1347 candidates in 1 file(s)
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /all.txt: 54 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 60 trackers
  [PASS] Plain text: /adysec_best.txt: 249 trackers
  [PASS] Plain text: /gonghailink_best.txt: 17 trackers
  [PASS] Plain text: /pandamen_best.txt: 18 trackers
  [PASS] Plain text: /gspu_best.txt: 19 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 15 trackers
  [PASS] Plain text: /pexcn_best.txt: 63 trackers
  [PASS] Plain text: /opentracker.txt: 27 trackers
  [PASS] Plain text: /run_ws.txt: 44 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 80 trackers
  [PASS] Plain text: /http.txt: 99 trackers
  [PASS] Plain text: /https.txt: 20 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset-of-all check: all 25 best trackers present in all (54)
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
  [PASS] URL format check: all 200 valid
  [PASS] Raw: alive (Raw): HTTP 200, 25 trackers
  [PASS] Raw: merged (Raw): HTTP 200, 200 trackers
  [PASS] Pages: /alive.txt: HTTP 200, 25 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 200 trackers
  [PASS] Pages short: /s/alive: HTTP 200, redirect OK
  [PASS] Pages short: /s/all: HTTP 200, redirect OK
  [PASS] Worker best 短链: HTTP 200, 25 trackers
  [PASS] Worker all 短链: HTTP 200, 54 trackers
  [PASS] Worker best 加速: HTTP 200, 25 trackers
  [PASS] Worker all 加速: HTTP 200, 59 trackers
------------------------------------------------------------
  Result: 83 passed, 0 warnings, 0 failed
============================================================

============================================================
 Round 3 - 2026-10-13 05:19:57
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 60 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 249 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 17 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 18 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 19 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 63 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 27 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 44 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_all.txt: 54 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1347 candidates in 1 file(s)
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /all.txt: 54 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 60 trackers
  [PASS] Plain text: /adysec_best.txt: 249 trackers
  [PASS] Plain text: /gonghailink_best.txt: 17 trackers
  [PASS] Plain text: /pandamen_best.txt: 18 trackers
  [PASS] Plain text: /gspu_best.txt: 19 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 15 trackers
  [PASS] Plain text: /pexcn_best.txt: 63 trackers
  [PASS] Plain text: /opentracker.txt: 27 trackers
  [PASS] Plain text: /run_ws.txt: 44 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 80 trackers
  [PASS] Plain text: /http.txt: 99 trackers
  [PASS] Plain text: /https.txt: 20 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset-of-all check: all 25 best trackers present in all (54)
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
  [PASS] URL format check: all 200 valid
  [PASS] Raw: alive (Raw): HTTP 200, 25 trackers
  [PASS] Raw: merged (Raw): HTTP 200, 200 trackers
  [PASS] Pages: /alive.txt: HTTP 200, 25 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 200 trackers
  [PASS] Pages short: /s/alive: HTTP 200, redirect OK
  [PASS] Pages short: /s/all: HTTP 200, redirect OK
  [PASS] Worker best 短链: HTTP 200, 25 trackers
  [PASS] Worker all 短链: HTTP 200, 54 trackers
  [PASS] Worker best 加速: HTTP 200, 25 trackers
  [PASS] Worker all 加速: HTTP 200, 59 trackers
------------------------------------------------------------
  Result: 83 passed, 0 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 3 rounds completed
   Total PASS: 249
   Total WARN: 0
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################
=== End of diagnostics (Tue Oct 13 05:19:57 UTC 2026) ===
