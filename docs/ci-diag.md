=== Diagnostics Tue Oct 13 06:34:14 UTC 2026 ===
Python: Python 3.12.15
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_best.txt
  HTTP 200, total 0.039590s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_best_ip.txt
  HTTP 200, total 0.034146s
>>> https://cf.trackerslist.com/best.txt
  HTTP 200, total 0.172947s
>>> https://tracker.adysec.com/trackers_best.txt
  HTTP 200, total 0.137931s
>>> https://raw.githubusercontent.com/gonghailink/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.099630s
>>> https://raw.githubusercontent.com/panda-men/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.098165s
>>> https://raw.githubusercontent.com/gspu/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.098839s
>>> https://raw.githubusercontent.com/linux-jin/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.115864s
>>> https://raw.githubusercontent.com/AlphaCatMeow/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.121279s
>>> https://raw.githubusercontent.com/pexcn/daily/gh-pages/trackerlist/trackerlist-best.txt
  HTTP 200, total 0.099667s
>>> https://raw.githubusercontent.com/1265578519/OpenTracker/refs/heads/master/tracker.txt
  HTTP 200, total 0.102362s
>>> https://trackers.run/s/rw_ws_up_hp_hs_v4_v6.txt
  HTTP 200, total 0.443815s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_i2p.txt
  HTTP 200, total 0.063946s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_yggdrasil.txt
  HTTP 200, total 0.073910s
[INFO] public list https://cf.trackerslist.com/all.txt: 121 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all.txt: 74 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ip.txt: 53 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_udp.txt: 45 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_http.txt: 17 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_https.txt: 11 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ws.txt: 3 urls
[WARN] public list fetch failed https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_wss.txt: HTTP Error 404: Not Found
[OK]   1335 new candidates -> candidates_20261013.txt
[OK]   1335 new candidates
[INFO] Repo: Pmwiu/Tracker-List, Max: 25
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/ngosang/trackerslist/master/blacklist.txt (391 URLs)
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/blacklist.txt (20 URLs)
[INFO] URL blacklist: 390 URLs (dynamic + remote sources)
[INFO] discovered candidates: 1335 URLs in 1 file(s)

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
[OK]   46 unique

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
[OK]   discovered_set.json (1335)
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
  trackers_run_ws.txt: 46
  trackers_ngosang_i2p.txt: 17
  trackers_ngosang_yggdrasil.txt: 1
  trackers_merged.txt: 200
  alive capped at 25 after test+sort
===================
[INFO] Testing 200 candidates (all-pool=200, timeout=10s, workers=30)
[INFO] Max alive trackers after scoring: 25
  [ALIVE] (2/200) http://140.235.237.23:6969/announce 85ms — announce with peers:1
  [ALIVE] (4/200) http://004430.xyz:80/announce 114ms — announce with peers:1
  [ALIVE] (6/200) http://135.125.198.235:2710/announce 226ms — announce without peers
  [ALIVE] (7/200) http://135.125.198.235:80/announce 228ms — announce without peers
  [ALIVE] (8/200) http://107.189.2.131:1337/announce 231ms — announce with peers:1
  [ALIVE] (11/200) http://138.186.10.167:1337/announce 243ms — announce with peers:1
  [ALIVE] (19/200) http://207.241.231.226:6969/announce 102ms — announce with peers:1
  [ALIVE] (20/200) http://185.126.65.92:6969/announce 196ms — announce without peers
  [ALIVE] (21/200) http://216.144.239.90:6969/announce 113ms — announce with peers:1
  [ALIVE] (22/200) http://31.38.161.123:6969/announce 246ms — announce with peers:1
  [ALIVE] (23/200) http://211.75.205.187:6969/announce 439ms — announce with peers:1
  [ALIVE] (24/200) http://211.75.205.187:80/announce 435ms — announce with peers:1
  [ALIVE] (25/200) http://211.75.205.188:6969/announce 435ms — announce with peers:1
  [ALIVE] (26/200) http://211.75.210.221:6969/announce 444ms — announce with peers:1
  [ALIVE] (27/200) http://211.75.205.188:80/announce 446ms — announce with peers:1
  [ALIVE] (28/200) http://207.241.226.111:6969/announce 479ms — announce with peers:1
  [ALIVE] (31/200) http://211.75.210.221:80/announce 451ms — announce with peers:1
  [ALIVE] (32/200) http://43.250.54.126:6969/announce 202ms — announce with peers:1
  [ALIVE] (33/200) http://93.158.213.92:1337/announce 194ms — announce with peers:1
  [ALIVE] (34/200) http://94.23.207.177:6969/announce 207ms — announce with peers:1
  [ALIVE] (35/200) http://1337.abcvg.info:80/announce 400ms — announce with peers:1
  [ALIVE] (36/200) http://announce.sktorrent.eu:6969/announce 238ms — announce with peers:1
  [ALIVE] (37/200) http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 234ms — announce with peers:1
  [ALIVE] (46/200) http://ipv4announce.sktorrent.eu:6969/announce 201ms — announce with peers:1
  [SKIP]   (50/200) http://freetracker.i2p:7331/announce — I2P network required
  [ALIVE] (55/200) http://tracker.auctor.tv:6969/announce 207ms — announce with peers:1
  [ALIVE] (56/200) http://tracker.dhitechnical.com:6969/announce 135ms — announce with peers:1
  [ALIVE] (57/200) http://retracker01-msk-virt.corbina.net:80/announce 540ms — announce with peers:1
  [ALIVE] (60/200) http://tracker.dler.org:6969/announce 435ms — announce with peers:1
  [ALIVE] (61/200) http://tracker.dler.com:6969/announce 641ms — announce with peers:1
  [ALIVE] (62/200) http://tracker.nyaa.vc:6969/announce 216ms — announce without peers
  [ALIVE] (65/200) http://tracker.mywaifu.best:6969/announce 470ms — announce without peers
  [ALIVE] (66/200) http://tracker.qu.ax:6969/announce 208ms — announce with peers:1
  [ALIVE] (67/200) http://tracker.renfei.net:8080/announce 55ms — announce with peers:1
  [ALIVE] (69/200) http://tracker.waaa.moe:6969/announce 157ms — announce with peers:1
  [ALIVE] (70/200) http://tracker.opentrackr.org:1337/announce 309ms — announce with peers:1
  [ALIVE] (72/200) https://004430.xyz:443/announce 142ms — announce with peers:1
  [ALIVE] (73/200) http://tracker2.dler.org:80/announce 446ms — announce with peers:1
  [ALIVE] (74/200) https://1.tracker.eu.org:443/announce 35ms — announce without peers
  [ALIVE] (75/200) https://2.tracker.eu.org:443/announce 57ms — announce without peers
  [ALIVE] (76/200) https://3.tracker.eu.org:443/announce 24ms — announce without peers
  [ALIVE] (78/200) https://t.213891.xyz:443/announce 17ms — announce without peers
  [ALIVE] (80/200) https://4.tracker.eu.org:443/announce 47ms — announce without peers
  [ALIVE] (83/200) https://337hhh.xyz:443/announce 337ms — announce without peers
  [ALIVE] (84/200) https://tracker.7471.top:443/announce 135ms — announce without peers
  [ALIVE] (85/200) https://tr.nyacat.pw:443/announce 216ms — announce without peers
  [ALIVE] (88/200) https://tracker.foreverpirates.co:443/announce 437ms — announce without peers
  [ALIVE] (92/200) udp://109.201.134.183:80/announce 101ms — valid connect + announce (v4)
  [ALIVE] (93/200) udp://135.125.198.235:1984/announce 107ms — valid connect + announce (v4)
  [ALIVE] (94/200) https://tracker.nekomi.cn:443/announce 127ms — announce with peers:1
  [ALIVE] (95/200) udp://132.226.6.145:6969/announce 148ms — valid connect + announce (v4)
  [ALIVE] (96/200) udp://193.148.251.93:6969/announce 21ms — valid connect + announce (v4)
  [ALIVE] (98/200) udp://151.242.104.187:80/announce 110ms — valid connect + announce (v4)
  [ALIVE] (99/200) udp://193.34.92.5:80/announce 132ms — valid connect + announce (v4)
  [ALIVE] (100/200) udp://209.141.59.25:6969/announce 129ms — valid connect + announce (v4)
  [ALIVE] (101/200) udp://185.121.168.96:1337/announce 189ms — valid connect + announce (v4)
  [ALIVE] (102/200) udp://23.157.120.14:6969/announce 83ms — valid connect + announce (v4)
  [ALIVE] (103/200) udp://31.38.161.123:6969/announce 115ms — valid connect + announce (v4)
  [ALIVE] (104/200) udp://34.66.57.33:1337/announce 11ms — valid connect + announce (v4)
  [ALIVE] (105/200) udp://211.75.205.187:6969/announce 222ms — valid connect + announce (v4)
  [ALIVE] (106/200) udp://34.66.57.33:80/announce 12ms — valid connect + announce (v4)
  [ALIVE] (107/200) udp://31.56.179.159:6969/announce 124ms — valid connect + announce (v4)
  [ALIVE] (108/200) udp://211.75.205.187:80/announce 225ms — valid connect + announce (v4)
  [ALIVE] (109/200) udp://43.250.54.126:6969/announce 105ms — valid connect + announce (v4)
  [ALIVE] (110/200) udp://45.137.199.107:6969/announce 100ms — valid connect + announce (v4)
  [ALIVE] (111/200) udp://51.81.222.188:6969/announce 51ms — valid connect + announce (v4)
  [ALIVE] (112/200) udp://51.15.41.46:6969/announce 104ms — valid connect + announce (v4)
  [ALIVE] (113/200) udp://43.154.112.29:17272/announce 183ms — valid connect + announce (v4)
  [ALIVE] (114/200) udp://52.58.128.163:6969/announce 109ms — valid connect + announce (v4)
  [ALIVE] (115/200) udp://65.109.28.17:6969/announce 128ms — valid connect + announce (v4)
  [ALIVE] (116/200) udp://65.109.28.33:6969/announce 130ms — valid connect + announce (v4)
  [ALIVE] (117/200) udp://93.158.213.92:1337/announce 101ms — valid connect + announce (v4)
  [ALIVE] (118/200) udp://89.234.156.205:451/announce 108ms — valid connect + announce (v4)
  [ALIVE] (119/200) udp://83.102.180.21:80/announce 148ms — valid connect + announce (v4)
  [ALIVE] (120/200) udp://93.158.213.92:6969/announce 101ms — valid connect + announce (v4)
  [ALIVE] (123/200) udp://95.217.80.20:6969/announce 128ms — valid connect + announce (v4)
  [ALIVE] (124/200) udp://95.217.80.22:6969/announce 128ms — valid connect + announce (v4)
  [ALIVE] (125/200) udp://evan.im:6969/announce 22ms — valid connect + announce (v4)
  [ALIVE] (143/200) udp://exodus.desync.com:6969/announce 50ms — valid connect + announce (v4)
  [ALIVE] (146/200) udp://explodie.org:6969/announce 84ms — valid connect + announce (v4)
  [ALIVE] (147/200) udp://open.ftorrent.com:443/announce 29ms — valid connect + announce (v4)
  [ALIVE] (148/200) udp://ipv4announce.sktorrent.eu:6969/announce 100ms — valid connect + announce (v4)
  [DEAD]  (150/200) http://178.175.143.27:80/announce — URLError: <urlopen error timed out>
  [ALIVE] (152/200) udp://martin-gebhardt.eu:25/announce 109ms — valid connect + announce (v4)
  [ALIVE] (153/200) udp://tracker.corpscorp.online:80/announce 12ms — valid connect + announce (v4)
  [ALIVE] (154/200) udp://tracker.bittor.pw:1337/announce 13ms — valid connect + announce (v4)
  [ALIVE] (155/200) udp://tracker.004430.xyz:1337/announce 46ms — valid connect + announce (v4)
  [ALIVE] (156/200) udp://mail.segso.net:6969/announce 130ms — valid connect + announce (v4)
  [ALIVE] (157/200) udp://retracker01-msk-virt.corbina.net:80/announce 146ms — valid connect + announce (v4)
  [ALIVE] (158/200) udp://open.demonii.com:1337/announce 188ms — valid connect + announce (v4)
  [ALIVE] (159/200) udp://t.overflow.biz:6969/announce 129ms — valid connect + announce (v4)
  [ALIVE] (160/200) udp://opentracker.lain.moscow:6969/announce 107ms — valid connect + announce (v4)
  [ALIVE] (161/200) udp://tracker-udp.gbitt.info:80/announce 105ms — valid connect + announce (v4)
  [ALIVE] (162/200) udp://open.stealth.si:80/announce 110ms — valid connect + announce (v4)
  [ALIVE] (163/200) udp://tracker.nyaa.vc:6969/announce 96ms — valid connect + announce (v4)
  [ALIVE] (164/200) udp://kolankoalastree.newtrackon.co.nz:1337/announce 198ms — valid connect + announce (v4)
  [ALIVE] (165/200) udp://tracker.opentrackr.org:1337/announce 106ms — valid connect + announce (v4)
  [ALIVE] (166/200) udp://tracker.farted.net:6969/announce 129ms — valid connect + announce (v4)
  [ALIVE] (167/200) udp://tracker.qu.ax:6969/announce 103ms — valid connect + announce (v4)
  [ALIVE] (168/200) udp://tracker.dler.org:6969/announce 219ms — valid connect + announce (v4)
  [ALIVE] (171/200) udp://tracker.ducks.party:1984/announce 111ms — valid connect + announce (v4)
  [ALIVE] (172/200) udp://tracker.gmi.gd:6969/announce 130ms — valid connect + announce (v4)
  [ALIVE] (174/200) udp://tracker.skynetcloud.site:6969/announce 94ms — valid connect + announce (v4)
  [ALIVE] (175/200) udp://tracker.peerfect.org:6969/announce 124ms — valid connect + announce (v4)
  [ALIVE] (176/200) udp://tracker2.dler.org:80/announce 222ms — valid connect + announce (v4)
  [ALIVE] (177/200) udp://tracker.torrent.eu.org:451/announce 142ms — valid connect + announce (v4)
  [ALIVE] (181/200) udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 1542ms — valid connect + announce (v4)
  [DEAD]  (200/200) udp://wepzone.net:6969/announce — no connect response

[INFO] First pass done in 31.1s
[INFO] Multi-sample: 3 samples on top 50 alive trackers...
[INFO] Multi-sample refined 50 trackers (median + jitter penalty)
[INFO] Same-subnet(/24) dedup removed 53 slower tracker(s)
[INFO] scrape probe: 18 http/https alive trackers
[INFO] scrape: 5 responded, 3 with seeders
[INFO] discovered candidates excluded from best/all: 1335
[INFO] promote queue: 0 tracked, 0 ready to promote
[INFO] Dynamic blacklist: 1 consistently-dead trackers

===== Test Summary =====
  Total tested:   200
  Alive (raw):    52
  Alive (final):  25 (top 25 by composite score)
  Non-UDP kept:   8 (quota >= 4)
  Classic kept:   5 (quota >= 4)
  Score-capped:   27
  Unsafe filtered:2
  Low-speed:      0 (>5s excluded)
  Same-subnet dedup:  53 (kept faster)
  Dead final:     154
  Time:           47.2s
=== 协议分布统计 ===
  HTTP  : 36 个
  HTTPS : 11 个
  UDP   : 58 个
  WSS   : 0 个
  WS    : 0 个
  总计: 105 个（存活）
=========================
[OK]   /s/alive
[OK]   /s/all
[OK]   index.html
[OK] Pages regenerated with alive statistics.
[OK]   docs/alive.txt
[OK]   docs/all.txt
[OK]   docs/reserve.txt
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
 Round 1 - 2026-10-13 06:35:12
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
  [PASS] Local tracker: trackers_run_ws.txt: 46 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_all.txt: 52 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1335 candidates in 1 file(s)
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /all.txt: 52 trackers
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
  [PASS] Plain text: /run_ws.txt: 46 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 80 trackers
  [PASS] Plain text: /http.txt: 99 trackers
  [PASS] Plain text: /https.txt: 20 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset-of-all check: all 25 best trackers present in all (52)
  [PASS] Reserve pool check: 0 candidates, disjoint
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_all.txt vs all.txt: identical
  [PASS] Consistency: trackers_reserve.txt vs reserve.txt: identical
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
  Result: 75 passed, 0 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 1 rounds completed
   Total PASS: 75
   Total WARN: 0
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################

============================================================
 Round 1 - 2026-10-13 06:35:19
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
  [PASS] Local tracker: trackers_run_ws.txt: 46 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_all.txt: 52 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1335 candidates in 1 file(s)
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /all.txt: 52 trackers
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
  [PASS] Plain text: /run_ws.txt: 46 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 80 trackers
  [PASS] Plain text: /http.txt: 99 trackers
  [PASS] Plain text: /https.txt: 20 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset-of-all check: all 25 best trackers present in all (52)
  [PASS] Reserve pool check: 0 candidates, disjoint
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_all.txt vs all.txt: identical
  [PASS] Consistency: trackers_reserve.txt vs reserve.txt: identical
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
  [PASS] Worker all 短链: HTTP 200, 52 trackers
  [PASS] Worker best 加速: HTTP 200, 25 trackers
  [PASS] Worker all 加速: HTTP 200, 59 trackers
------------------------------------------------------------
  Result: 85 passed, 0 warnings, 0 failed
============================================================

============================================================
 Round 2 - 2026-10-13 06:35:25
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
  [PASS] Local tracker: trackers_run_ws.txt: 46 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_all.txt: 52 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1335 candidates in 1 file(s)
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /all.txt: 52 trackers
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
  [PASS] Plain text: /run_ws.txt: 46 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 80 trackers
  [PASS] Plain text: /http.txt: 99 trackers
  [PASS] Plain text: /https.txt: 20 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset-of-all check: all 25 best trackers present in all (52)
  [PASS] Reserve pool check: 0 candidates, disjoint
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_all.txt vs all.txt: identical
  [PASS] Consistency: trackers_reserve.txt vs reserve.txt: identical
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
  [PASS] Worker all 短链: HTTP 200, 52 trackers
  [PASS] Worker best 加速: HTTP 200, 25 trackers
  [PASS] Worker all 加速: HTTP 200, 59 trackers
------------------------------------------------------------
  Result: 85 passed, 0 warnings, 0 failed
============================================================

============================================================
 Round 3 - 2026-10-13 06:35:30
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
  [PASS] Local tracker: trackers_run_ws.txt: 46 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_all.txt: 52 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1335 candidates in 1 file(s)
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /all.txt: 52 trackers
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
  [PASS] Plain text: /run_ws.txt: 46 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 80 trackers
  [PASS] Plain text: /http.txt: 99 trackers
  [PASS] Plain text: /https.txt: 20 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset-of-all check: all 25 best trackers present in all (52)
  [PASS] Reserve pool check: 0 candidates, disjoint
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_all.txt vs all.txt: identical
  [PASS] Consistency: trackers_reserve.txt vs reserve.txt: identical
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
  [PASS] Worker all 短链: HTTP 200, 52 trackers
  [PASS] Worker best 加速: HTTP 200, 25 trackers
  [PASS] Worker all 加速: HTTP 200, 59 trackers
------------------------------------------------------------
  Result: 85 passed, 0 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 3 rounds completed
   Total PASS: 255
   Total WARN: 0
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################
=== End of diagnostics (Tue Oct 13 06:35:30 UTC 2026) ===
