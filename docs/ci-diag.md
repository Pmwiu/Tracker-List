=== Diagnostics Tue Oct 13 10:35:43 UTC 2026 ===
Python: Python 3.12.15
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_best.txt
  HTTP 200, total 0.053541s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_best_ip.txt
  HTTP 200, total 0.038073s
>>> https://cf.trackerslist.com/best.txt
  HTTP 200, total 0.185392s
>>> https://tracker.adysec.com/trackers_best.txt
  HTTP 200, total 0.182750s
>>> https://raw.githubusercontent.com/gonghailink/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.116241s
>>> https://raw.githubusercontent.com/panda-men/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.106392s
>>> https://raw.githubusercontent.com/gspu/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.100161s
>>> https://raw.githubusercontent.com/linux-jin/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.107988s
>>> https://raw.githubusercontent.com/AlphaCatMeow/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.102563s
>>> https://raw.githubusercontent.com/pexcn/daily/gh-pages/trackerlist/trackerlist-best.txt
  HTTP 200, total 0.103702s
>>> https://raw.githubusercontent.com/1265578519/OpenTracker/refs/heads/master/tracker.txt
  HTTP 200, total 0.103741s
>>> https://trackers.run/s/rw_ws_up_hp_hs_v4_v6.txt
  HTTP 200, total 0.675962s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_i2p.txt
  HTTP 200, total 0.048469s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_yggdrasil.txt
  HTTP 200, total 0.058193s
[INFO] public list https://cf.trackerslist.com/all.txt: 119 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all.txt: 74 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ip.txt: 53 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_udp.txt: 46 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_http.txt: 17 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_https.txt: 11 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ws.txt: 3 urls
[OK]   1284 new candidates -> candidates_20261013.txt
[OK]   1284 new candidates
[INFO] Repo: Pmwiu/Tracker-List, Max: 25
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/ngosang/trackerslist/master/blacklist.txt (391 URLs)
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/blacklist.txt (20 URLs)
[INFO] URL blacklist: 401 URLs (dynamic + remote sources)
[INFO] discovered candidates: 1066 URLs in 1 file(s)

[INFO] trackers_ngosang_best.txt (ngosang-best)
[OK]   20 unique

[INFO] trackers_ngosang_best_ip.txt (ngosang-best-ip)
[OK]   20 unique

[INFO] trackers_cf_best.txt (cf-best)
  [INFO] Skipped 15 dynamic-blacklisted lines
[OK]   55 unique

[INFO] trackers_adysec_best.txt (adysec-best)
  [INFO] Skipped 72 dynamic-blacklisted lines
[OK]   248 unique

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
  [INFO] Skipped 7 dynamic-blacklisted lines
[OK]   13 unique

[INFO] trackers_pexcn_best.txt (pexcn-best)
  [INFO] Skipped 15 dynamic-blacklisted lines
[OK]   58 unique

[INFO] trackers_opentracker.txt (opentracker)
  [INFO] Skipped 4 invalid lines
  [INFO] Skipped 8 dynamic-blacklisted lines
[OK]   23 unique

[INFO] trackers_run_ws.txt (trackersrun-ws)
  [INFO] Skipped 3 dynamic-blacklisted lines
[OK]   47 unique

[INFO] trackers_ngosang_i2p.txt (ngosang-i2p)
[OK]   17 unique

[INFO] trackers_ngosang_yggdrasil.txt (ngosang-yggdrasil)
  [INFO] Skipped 1 dynamic-blacklisted lines
[WARN] trackers_ngosang_yggdrasil.txt failed (No valid trackers found in response); using backup (1 trackers)
[OK]   1 unique

[INFO] all 合并贡献: ngosang-best=20, ngosang-best-ip=20, cf-best=25, adysec-best=37, gonghailink-best=4, pandamen-best=4, gspu-best=3, linuxjin-best=1, alphacatmeow-best=1, pexcn-best=1, opentracker=10, trackersrun-ws=19, ngosang-i2p=17, ngosang-yggdrasil=1
[INFO] all 协议分布: http=105, https=18, udp=76, wss=1, ws=0

[OK]   merged: 200
[OK]   source_counts.json (200)
[OK]   discovered_set.json (1066)
[OK]   MIRRORS.txt
[OK]   /s/alive
[OK]   /s/all
[OK]   index.html
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

===== Summary =====
  trackers_ngosang_best.txt: 20
  trackers_ngosang_best_ip.txt: 20
  trackers_cf_best.txt: 55
  trackers_adysec_best.txt: 248
  trackers_gonghailink_best.txt: 15
  trackers_pandamen_best.txt: 15
  trackers_gspu_best.txt: 16
  trackers_linuxjin_best.txt: 20
  trackers_alphacatmeow_best.txt: 13
  trackers_pexcn_best.txt: 58
  trackers_opentracker.txt: 23
  trackers_run_ws.txt: 47
  trackers_ngosang_i2p.txt: 17
  trackers_ngosang_yggdrasil.txt: 1
  trackers_merged.txt: 200
  alive capped at 25 after test+sort
===================
[INFO] reserve: +120 discovered candidates for liveness test (rotation, cap 120)
[INFO] Testing 320 candidates (all-pool=200, timeout=10s, workers=30)
[INFO] Max alive trackers after scoring: 25
  [ALIVE] (4/320) http://135.125.198.235:2710/announce 192ms — announce without peers
  [ALIVE] (5/320) http://135.125.198.235:80/announce 189ms — announce without peers
  [ALIVE] (6/320) http://004430.xyz:80/announce 169ms — announce with peers:1
  [ALIVE] (7/320) http://107.189.2.131:1337/announce 241ms — announce with peers:1
  [ALIVE] (8/320) http://138.186.10.167:1337/announce 271ms — announce with peers:1
  [ALIVE] (9/320) http://1337.abcvg.info:80/announce 400ms — announce with peers:1
  [ALIVE] (10/320) http://140.235.237.23:6969/announce 324ms — announce with peers:1
  [ALIVE] (12/320) http://185.126.65.92:6969/announce 176ms — announce without peers
  [DEAD]  (25/320) http://116.252.176.125:6969/announce — URLError: <urlopen error timed out>
  [ALIVE] (35/320) http://207.241.231.226:6969/announce 139ms — announce with peers:1
  [ALIVE] (36/320) http://207.241.226.111:6969/announce 140ms — announce with peers:1
  [ALIVE] (37/320) http://43.250.54.126:6969/announce 171ms — announce with peers:1
  [ALIVE] (38/320) http://94.23.207.177:6969/announce 174ms — announce with peers:1
  [ALIVE] (39/320) http://93.158.213.92:1337/announce 174ms — announce with peers:1
  [ALIVE] (44/320) http://31.38.161.123:6969/announce 204ms — announce with peers:1
  [ALIVE] (47/320) http://announce.sktorrent.eu:6969/announce 228ms — announce with peers:1
  [ALIVE] (50/320) http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 218ms — announce with peers:1
  [ALIVE] (51/320) http://211.75.205.187:6969/announce 392ms — announce with peers:1
  [ALIVE] (52/320) http://211.75.210.221:80/announce 392ms — announce with peers:1
  [ALIVE] (53/320) http://211.75.205.187:80/announce 393ms — announce with peers:1
  [ALIVE] (54/320) http://211.75.210.221:6969/announce 393ms — announce with peers:1
  [ALIVE] (55/320) http://211.75.205.188:6969/announce 394ms — announce with peers:1
  [ALIVE] (56/320) http://211.75.205.188:80/announce 396ms — announce with peers:1
  [ALIVE] (66/320) http://ipv4announce.sktorrent.eu:6969/announce 174ms — announce with peers:1
  [ALIVE] (68/320) http://open.demonii.si:80/announce 237ms — announce without peers
  [ALIVE] (69/320) http://tracker.dhitechnical.com:6969/announce 142ms — announce with peers:1
  [ALIVE] (70/320) http://tracker.nyaa.vc:6969/announce 181ms — announce without peers
  [ALIVE] (72/320) http://tracker.mywaifu.best:6969/announce 326ms — announce without peers
  [ALIVE] (73/320) http://tracker.auctor.tv:6969/announce 172ms — announce with peers:1
  [ALIVE] (75/320) http://tracker.opentrackr.org:1337/announce 175ms — announce with peers:1
  [ALIVE] (76/320) http://retracker01-msk-virt.corbina.net:80/announce 409ms — announce with peers:1
  [ALIVE] (78/320) http://tracker.renfei.net:8080/announce 106ms — announce with peers:1
  [ALIVE] (79/320) http://tracker.qu.ax:6969/announce 171ms — announce with peers:1
  [ALIVE] (80/320) http://tracker.dler.com:6969/announce 435ms — announce with peers:1
  [ALIVE] (81/320) http://tracker.dler.org:6969/announce 403ms — announce with peers:1
  [ALIVE] (82/320) https://004430.xyz:443/announce 180ms — announce with peers:1
  [ALIVE] (83/320) https://2.tracker.eu.org:443/announce 29ms — announce without peers
  [ALIVE] (84/320) https://4.tracker.eu.org:443/announce 27ms — announce without peers
  [ALIVE] (85/320) http://tracker2.dler.org:80/announce 395ms — announce with peers:1
  [ALIVE] (86/320) https://1.tracker.eu.org:443/announce 28ms — announce without peers
  [ALIVE] (87/320) https://3.tracker.eu.org:443/announce 26ms — announce without peers
  [ALIVE] (88/320) https://t.213891.xyz:443/announce 26ms — announce without peers
  [ALIVE] (89/320) http://opentracker.xyz:80/announce 533ms — announce with peers:1
  [ALIVE] (90/320) https://5.tracker.eu.org:443/announce 25ms — announce without peers
  [ALIVE] (91/320) https://337hhh.xyz:443/announce 288ms — announce without peers
  [ALIVE] (92/320) http://tracker.waaa.moe:6969/announce 663ms — announce with peers:1
  [ALIVE] (93/320) https://tr.nyacat.pw:443/announce 107ms — announce without peers
  [ALIVE] (94/320) https://tracker.7471.top:443/announce 124ms — announce without peers
  [ALIVE] (95/320) https://open.ftorrent.com:443/announce 154ms — announce without peers
  [ALIVE] (96/320) http://open.tracker.cl:1337/announce 414ms — announce with peers:1
  [ALIVE] (97/320) https://tracker.foreverpirates.co:443/announce 158ms — announce without peers
  [ALIVE] (99/320) https://retracker.x2k.ru:443/announce 372ms — announce with peers:1
  [ALIVE] (100/320) udp://109.201.134.183:80/announce 87ms — valid connect + announce (v4)
  [ALIVE] (101/320) udp://193.148.251.93:6969/announce 42ms — valid connect + announce (v4)
  [ALIVE] (102/320) udp://135.125.198.235:1984/announce 94ms — valid connect + announce (v4)
  [ALIVE] (103/320) udp://151.242.104.187:80/announce 101ms — valid connect + announce (v4)
  [ALIVE] (104/320) udp://132.226.6.145:6969/announce 164ms — valid connect + announce (v4)
  [ALIVE] (105/320) udp://193.34.92.5:80/announce 125ms — valid connect + announce (v4)
  [ALIVE] (106/320) udp://209.141.59.25:6969/announce 141ms — valid connect + announce (v4)
  [ALIVE] (107/320) udp://185.121.168.96:1337/announce 190ms — valid connect + announce (v4)
  [ALIVE] (108/320) udp://23.157.120.14:6969/announce 79ms — valid connect + announce (v4)
  [ALIVE] (109/320) udp://34.66.57.33:1337/announce 34ms — valid connect + announce (v4)
  [ALIVE] (110/320) udp://34.66.57.33:80/announce 34ms — valid connect + announce (v4)
  [ALIVE] (113/320) udp://31.38.161.123:6969/announce 102ms — valid connect + announce (v4)
  [ALIVE] (114/320) udp://211.75.205.187:6969/announce 197ms — valid connect + announce (v4)
  [ALIVE] (115/320) udp://31.56.179.159:6969/announce 109ms — valid connect + announce (v4)
  [ALIVE] (116/320) https://tracker.nekomi.cn:443/announce 178ms — announce with peers:1
  [ALIVE] (117/320) udp://211.75.205.187:80/announce 197ms — valid connect + announce (v4)
  [ALIVE] (121/320) udp://43.250.54.126:6969/announce 86ms — valid connect + announce (v4)
  [ALIVE] (123/320) udp://51.15.41.46:6969/announce 87ms — valid connect + announce (v4)
  [SKIP]   (125/320) http://opentracker.simp.i2p:80/a — I2P network required
  [ALIVE] (127/320) udp://45.137.199.107:6969/announce 94ms — valid connect + announce (v4)
  [ALIVE] (129/320) udp://51.81.222.188:6969/announce 69ms — valid connect + announce (v4)
  [ALIVE] (134/320) udp://93.158.213.92:1337/announce 86ms — valid connect + announce (v4)
  [ALIVE] (135/320) udp://89.234.156.205:451/announce 95ms — valid connect + announce (v4)
  [ALIVE] (136/320) udp://evan.im:6969/announce 26ms — valid connect + announce (v4)
  [ALIVE] (137/320) udp://93.158.213.92:6969/announce 87ms — valid connect + announce (v4)
  [ALIVE] (138/320) udp://65.109.28.17:6969/announce 120ms — valid connect + announce (v4)
  [ALIVE] (139/320) udp://65.109.28.33:6969/announce 120ms — valid connect + announce (v4)
  [ALIVE] (140/320) udp://ipv4announce.sktorrent.eu:6969/announce 86ms — valid connect + announce (v4)
  [ALIVE] (141/320) udp://43.154.112.29:17272/announce 204ms — valid connect + announce (v4)
  [ALIVE] (143/320) udp://83.102.180.21:80/announce 134ms — valid connect + announce (v4)
  [ALIVE] (144/320) udp://open.ftorrent.com:443/announce 50ms — valid connect + announce (v4)
  [ALIVE] (146/320) udp://95.217.80.20:6969/announce 120ms — valid connect + announce (v4)
  [ALIVE] (147/320) udp://95.217.80.22:6969/announce 118ms — valid connect + announce (v4)
  [ALIVE] (148/320) udp://explodie.org:6969/announce 77ms — valid connect + announce (v4)
  [ALIVE] (149/320) udp://martin-gebhardt.eu:25/announce 94ms — valid connect + announce (v4)
  [ALIVE] (150/320) udp://mail.segso.net:6969/announce 118ms — valid connect + announce (v4)
  [ALIVE] (151/320) udp://tr4ck3r.duckdns.org:6969/announce 16ms — valid connect + announce (v4)
  [ALIVE] (152/320) udp://tracker.004430.xyz:1337/announce 81ms — valid connect + announce (v4)
  [ALIVE] (153/320) udp://kolankoalastree.newtrackon.co.nz:1337/announce 202ms — valid connect + announce (v4)
  [ALIVE] (154/320) udp://retracker01-msk-virt.corbina.net:80/announce 137ms — valid connect + announce (v4)
  [ALIVE] (155/320) udp://tracker-udp.gbitt.info:80/announce 87ms — valid connect + announce (v4)
  [ALIVE] (156/320) udp://tracker.bittor.pw:1337/announce 34ms — valid connect + announce (v4)
  [ALIVE] (157/320) udp://opentracker.lain.moscow:6969/announce 103ms — valid connect + announce (v4)
  [ALIVE] (158/320) udp://tracker.corpscorp.online:80/announce 35ms — valid connect + announce (v4)
  [ALIVE] (159/320) udp://open.demonii.com:1337/announce 193ms — valid connect + announce (v4)
  [ALIVE] (161/320) udp://tracker.ducks.party:1984/announce 94ms — valid connect + announce (v4)
  [ALIVE] (162/320) udp://tracker.nyaa.vc:6969/announce 91ms — valid connect + announce (v4)
  [ALIVE] (163/320) udp://tracker.opentrackr.org:1337/announce 87ms — valid connect + announce (v4)
  [ALIVE] (164/320) udp://tracker.qu.ax:6969/announce 89ms — valid connect + announce (v4)
  [ALIVE] (165/320) udp://tracker.dler.org:6969/announce 196ms — valid connect + announce (v4)
  [ALIVE] (166/320) udp://tracker.cn.nyaa.net:6969/announce 204ms — valid connect + announce (v4)
  [ALIVE] (167/320) udp://tracker.farted.net:6969/announce 111ms — valid connect + announce (v4)
  [ALIVE] (168/320) udp://open.stealth.si:80/announce 101ms — valid connect + announce (v4)
  [ALIVE] (169/320) udp://tracker.aruku.ovh:8081/announce 223ms — valid connect + announce (v4)
  [ALIVE] (170/320) udp://tracker.peerfect.org:6969/announce 118ms — valid connect + announce (v4)
  [ALIVE] (171/320) udp://tracker.gmi.gd:6969/announce 167ms — valid connect + announce (v4)
  [ALIVE] (173/320) udp://tracker.skynetcloud.site:6969/announce 86ms — valid connect + announce (v4)
  [ALIVE] (174/320) udp://tracker.torrent.eu.org:451/announce 96ms — valid connect + announce (v4)
  [ALIVE] (175/320) udp://tracker2.dler.org:80/announce 196ms — valid connect + announce (v4)
  [ALIVE] (182/320) http://216.144.239.90:6969/announce 5064ms — announce with peers:1
  [ALIVE] (183/320) udp://t.overflow.biz:6969/announce 126ms — valid connect + announce (v4)
  [ALIVE] (186/320) udp://tracker.filemail.com:6969/announce 92ms — valid connect + announce (v4)
  [ALIVE] (188/320) udp://tracker.tryhackx.org:6969/announce 111ms — valid connect + announce (v4)
  [DEAD]  (200/320) http://cn.pcfreetime.com:6969/announce — URLError: <urlopen error [Errno 111] Connection refused>
  [BLOCK] (225/320) http://ipv4.tracker.harry.lu:80/announce — resolves to private IP: 127.0.0.1
  [DEAD]  (250/320) http://open.nyap2p.com:8080/announce — URLError: <urlopen error [Errno -2] Name or service not known>
  [DEAD]  (275/320) http://siambit.org:80/announce.php — HTTPError: HTTP Error 404: Not Found
  [ALIVE] (282/320) http://t.overflow.biz:6969/announce 257ms — announce with peers:1
  [ALIVE] (284/320) http://t.nyaatracker.com:80/announce 238ms — announce without peers
  [DEAD]  (300/320) http://torrent.nwps.ws:80/announce — URLError: <urlopen error [Errno -2] Name or service not known>

[INFO] First pass done in 86.8s
[INFO] Multi-sample: 3 samples on top 50 alive trackers...
[INFO] Multi-sample refined 50 trackers (median + jitter penalty)
[INFO] Low-speed filtered (>5s): 1 trackers
[INFO] Same-subnet(/24) dedup removed 65 slower tracker(s)
[INFO] scrape probe: 12 http/https alive trackers
[INFO] scrape: 3 responded, 2 with seeders
[INFO] discovered candidates excluded from best/all: 1066
[INFO] reserve pool: 9 discovered candidates -> trackers_reserve.txt
[INFO] promote queue: 13 tracked, 0 ready to promote
[INFO] Dynamic blacklist: 1 consistently-dead trackers

===== Test Summary =====
  Total tested:   320
  Alive (raw):    49
  Alive (final):  25 (top 25 by composite score)
  Non-UDP kept:   8 (quota >= 4)
  Classic kept:   0 (quota >= 4)
  Score-capped:   24
  Unsafe filtered:6
  Low-speed:      1 (>5s excluded)
  Same-subnet dedup:  65 (kept faster)
  Dead final:     278
  Time:           94.8s
=== 协议分布统计 ===
  HTTP  : 41 个
  HTTPS : 14 个
  UDP   : 60 个
  WSS   : 0 个
  WS    : 0 个
  总计: 115 个（存活）
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
 Round 1 - 2026-10-13 10:37:33
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 55 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 248 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 15 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 16 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 13 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 58 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 23 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 47 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_all.txt: 46 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1284 candidates in 1 file(s)
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /all.txt: 46 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 55 trackers
  [PASS] Plain text: /adysec_best.txt: 248 trackers
  [PASS] Plain text: /gonghailink_best.txt: 15 trackers
  [PASS] Plain text: /pandamen_best.txt: 15 trackers
  [PASS] Plain text: /gspu_best.txt: 16 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 13 trackers
  [PASS] Plain text: /pexcn_best.txt: 58 trackers
  [PASS] Plain text: /opentracker.txt: 23 trackers
  [PASS] Plain text: /run_ws.txt: 47 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 76 trackers
  [PASS] Plain text: /http.txt: 105 trackers
  [PASS] Plain text: /https.txt: 18 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset-of-all check: all 25 best trackers present in all (46)
  [PASS] Reserve pool check: 9 candidates, disjoint
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
 Round 1 - 2026-10-13 10:37:41
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 55 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 248 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 15 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 16 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 13 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 58 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 23 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 47 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_all.txt: 46 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1284 candidates in 1 file(s)
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /all.txt: 46 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 55 trackers
  [PASS] Plain text: /adysec_best.txt: 248 trackers
  [PASS] Plain text: /gonghailink_best.txt: 15 trackers
  [PASS] Plain text: /pandamen_best.txt: 15 trackers
  [PASS] Plain text: /gspu_best.txt: 16 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 13 trackers
  [PASS] Plain text: /pexcn_best.txt: 58 trackers
  [PASS] Plain text: /opentracker.txt: 23 trackers
  [PASS] Plain text: /run_ws.txt: 47 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 76 trackers
  [PASS] Plain text: /http.txt: 105 trackers
  [PASS] Plain text: /https.txt: 18 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset-of-all check: all 25 best trackers present in all (46)
  [PASS] Reserve pool check: 9 candidates, disjoint
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
  [PASS] Worker all 短链: HTTP 200, 46 trackers
  [PASS] Worker best 加速: HTTP 200, 25 trackers
  [PASS] Worker all 加速: HTTP 200, 59 trackers
------------------------------------------------------------
  Result: 85 passed, 0 warnings, 0 failed
============================================================

============================================================
 Round 2 - 2026-10-13 10:37:46
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 55 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 248 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 15 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 16 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 13 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 58 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 23 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 47 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_all.txt: 46 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1284 candidates in 1 file(s)
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /all.txt: 46 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 55 trackers
  [PASS] Plain text: /adysec_best.txt: 248 trackers
  [PASS] Plain text: /gonghailink_best.txt: 15 trackers
  [PASS] Plain text: /pandamen_best.txt: 15 trackers
  [PASS] Plain text: /gspu_best.txt: 16 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 13 trackers
  [PASS] Plain text: /pexcn_best.txt: 58 trackers
  [PASS] Plain text: /opentracker.txt: 23 trackers
  [PASS] Plain text: /run_ws.txt: 47 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 76 trackers
  [PASS] Plain text: /http.txt: 105 trackers
  [PASS] Plain text: /https.txt: 18 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset-of-all check: all 25 best trackers present in all (46)
  [PASS] Reserve pool check: 9 candidates, disjoint
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
  [PASS] Worker all 短链: HTTP 200, 46 trackers
  [PASS] Worker best 加速: HTTP 200, 25 trackers
  [PASS] Worker all 加速: HTTP 200, 59 trackers
------------------------------------------------------------
  Result: 85 passed, 0 warnings, 0 failed
============================================================

============================================================
 Round 3 - 2026-10-13 10:37:51
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 55 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 248 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 15 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 16 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 13 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 58 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 23 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 47 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_all.txt: 46 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1284 candidates in 1 file(s)
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /all.txt: 46 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 55 trackers
  [PASS] Plain text: /adysec_best.txt: 248 trackers
  [PASS] Plain text: /gonghailink_best.txt: 15 trackers
  [PASS] Plain text: /pandamen_best.txt: 15 trackers
  [PASS] Plain text: /gspu_best.txt: 16 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 13 trackers
  [PASS] Plain text: /pexcn_best.txt: 58 trackers
  [PASS] Plain text: /opentracker.txt: 23 trackers
  [PASS] Plain text: /run_ws.txt: 47 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 76 trackers
  [PASS] Plain text: /http.txt: 105 trackers
  [PASS] Plain text: /https.txt: 18 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset-of-all check: all 25 best trackers present in all (46)
  [PASS] Reserve pool check: 9 candidates, disjoint
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
  [PASS] Worker all 短链: HTTP 200, 46 trackers
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
=== End of diagnostics (Tue Oct 13 10:37:51 UTC 2026) ===
