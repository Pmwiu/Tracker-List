=== Diagnostics Sat Oct 17 00:21:05 UTC 2026 ===
Python: Python 3.12.15
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_best.txt
  HTTP 200, total 0.059825s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_best_ip.txt
  HTTP 200, total 0.046146s
>>> https://cf.trackerslist.com/best.txt
  HTTP 200, total 0.236788s
>>> https://tracker.adysec.com/trackers_best.txt
  HTTP 200, total 0.288047s
>>> https://raw.githubusercontent.com/gonghailink/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.189647s
>>> https://raw.githubusercontent.com/panda-men/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.140845s
>>> https://raw.githubusercontent.com/gspu/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.183017s
>>> https://raw.githubusercontent.com/linux-jin/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.359254s
>>> https://raw.githubusercontent.com/AlphaCatMeow/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.672284s
>>> https://raw.githubusercontent.com/pexcn/daily/gh-pages/trackerlist/trackerlist-best.txt
  HTTP 200, total 0.147119s
>>> https://raw.githubusercontent.com/1265578519/OpenTracker/refs/heads/master/tracker.txt
  HTTP 200, total 0.126745s
>>> https://trackers.run/s/rw_ws_up_hp_hs_v4_v6.txt
  HTTP 200, total 1.251768s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_i2p.txt
  HTTP 200, total 0.048083s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_yggdrasil.txt
  HTTP 200, total 0.051269s
[INFO] public list https://cf.trackerslist.com/all.txt: 122 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all.txt: 72 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ip.txt: 53 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_udp.txt: 45 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_http.txt: 17 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_https.txt: 10 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ws.txt: 3 urls
[OK]   1286 new candidates -> candidates_20261017.txt
[OK]   1286 new candidates
[INFO] Repo: Pmwiu/Tracker-List, Max: 59
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/ngosang/trackerslist/master/blacklist.txt (391 URLs)
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/blacklist.txt (20 URLs)
[INFO] URL blacklist: 390 URLs (dynamic + remote sources)
[INFO] Protected hosts (防误杀): 59
[INFO] discovered candidates: 1068 URLs in 1 file(s)

[INFO] trackers_ngosang_best.txt (ngosang-best)
[OK]   20 unique

[INFO] trackers_ngosang_best_ip.txt (ngosang-best-ip)
[OK]   20 unique

[INFO] trackers_cf_best.txt (cf-best)
  [INFO] Skipped 10 dynamic-blacklisted lines
[OK]   62 unique

[INFO] trackers_adysec_best.txt (adysec-best)
  [INFO] Skipped 68 dynamic-blacklisted lines
[OK]   241 unique

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
[OK]   61 unique

[INFO] trackers_opentracker.txt (opentracker)
  [INFO] Skipped 4 invalid lines
  [INFO] Skipped 8 dynamic-blacklisted lines
[OK]   23 unique

[INFO] trackers_run_ws.txt (trackersrun-ws)
  [INFO] Skipped 2 dynamic-blacklisted lines
[OK]   52 unique

[INFO] trackers_ngosang_i2p.txt (ngosang-i2p)
[OK]   17 unique

[INFO] trackers_ngosang_yggdrasil.txt (ngosang-yggdrasil)
  [INFO] Skipped 1 dynamic-blacklisted lines
[WARN] trackers_ngosang_yggdrasil.txt failed (No valid trackers found in response); using backup (1 trackers)
[OK]   1 unique

[INFO] all 合并贡献: ngosang-best=20, ngosang-best-ip=20, cf-best=20, adysec-best=29, gonghailink-best=7, pandamen-best=8, gspu-best=3, linuxjin-best=1, alphacatmeow-best=3, pexcn-best=9, opentracker=10, trackersrun-ws=17, ngosang-i2p=17, ngosang-yggdrasil=1
[INFO] all 协议分布: http=102, https=19, udp=78, wss=1, ws=0

[OK]   merged: 200
[OK]   source_counts.json (200)
[OK]   discovered_set.json (1068)
[OK]   MIRRORS.txt
[OK]   /s/all
[OK]   index.html
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
  trackers_cf_best.txt: 62
  trackers_adysec_best.txt: 241
  trackers_gonghailink_best.txt: 17
  trackers_pandamen_best.txt: 18
  trackers_gspu_best.txt: 19
  trackers_linuxjin_best.txt: 20
  trackers_alphacatmeow_best.txt: 15
  trackers_pexcn_best.txt: 61
  trackers_opentracker.txt: 23
  trackers_run_ws.txt: 52
  trackers_ngosang_i2p.txt: 17
  trackers_ngosang_yggdrasil.txt: 1
  trackers_merged.txt: 200
===================
[INFO] discovery: +120 discovered candidates for liveness test (rotation, cap 120)
[INFO] Testing 320 candidates (all-pool=200, timeout=10s, workers=30)
  [ALIVE] (1/320) http://004430.xyz:80/announce 25ms — announce with peers:1
  [ALIVE] (5/320) http://1337.abcvg.info:80/announce 257ms — announce with peers:1
  [ALIVE] (6/320) http://135.125.198.235:2710/announce 289ms — announce without peers
  [ALIVE] (7/320) http://107.189.2.131:1337/announce 296ms — announce with peers:1
  [ALIVE] (8/320) http://135.125.198.235:80/announce 291ms — announce without peers
  [ALIVE] (9/320) http://138.186.10.167:1337/announce 269ms — announce with peers:1
  [ALIVE] (10/320) http://140.235.237.23:6969/announce 1143ms — announce with peers:1
  [ALIVE] (14/320) http://185.126.65.92:6969/announce 262ms — announce without peers
  [ALIVE] (15/320) http://207.241.226.111:6969/announce 34ms — announce with peers:1
  [ALIVE] (16/320) http://207.241.231.226:6969/announce 36ms — announce with peers:1
  [ALIVE] (18/320) http://211.75.205.187:6969/announce 294ms — announce with peers:1
  [ALIVE] (19/320) http://211.75.205.187:80/announce 281ms — announce with peers:1
  [ALIVE] (20/320) http://211.75.205.188:6969/announce 280ms — announce with peers:1
  [ALIVE] (21/320) http://211.75.205.188:80/announce 293ms — announce with peers:1
  [ALIVE] (22/320) http://211.75.210.221:6969/announce 292ms — announce with peers:1
  [ALIVE] (23/320) http://216.144.239.90:6969/announce 25ms — announce with peers:1
  [ALIVE] (24/320) http://211.75.210.221:80/announce 280ms — announce with peers:1
  [ALIVE] (25/320) http://43.250.54.126:6969/announce 259ms — announce with peers:1
  [ALIVE] (26/320) http://31.38.161.123:6969/announce 293ms — announce with peers:1
  [ALIVE] (27/320) http://93.158.213.92:1337/announce 261ms — announce with peers:1
  [ALIVE] (29/320) http://94.23.207.177:6969/announce 286ms — announce with peers:1
  [ALIVE] (30/320) http://announce.sktorrent.eu:6969/announce 304ms — announce with peers:1
  [ALIVE] (31/320) http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 285ms — announce with peers:1
  [DEAD]  (50/320) http://116.9.207.164:6969/announce — URLError: <urlopen error timed out>
  [ALIVE] (66/320) http://ipv4announce.sktorrent.eu:6969/announce 287ms — announce with peers:1
  [ALIVE] (69/320) http://open.demonii.si:80/announce 320ms — announce without peers
  [ALIVE] (71/320) http://tracker.dler.org:6969/announce 291ms — announce with peers:1
  [ALIVE] (72/320) http://tracker.nyaa.vc:6969/announce 273ms — announce without peers
  [ALIVE] (73/320) http://tracker.auctor.tv:6969/announce 260ms — announce with peers:1
  [ALIVE] (74/320) https://004430.xyz:443/announce 43ms — announce with peers:1
  [ALIVE] (75/320) http://tracker.renfei.net:8080/announce 173ms — announce with peers:1
  [ALIVE] (76/320) http://tracker.qu.ax:6969/announce 261ms — announce with peers:1
  [ALIVE] (77/320) http://tracker.opentrackr.org:1337/announce 407ms — announce with peers:1
  [ALIVE] (78/320) http://retracker01-msk-virt.corbina.net:80/announce 581ms — announce with peers:1
  [ALIVE] (80/320) http://tracker2.dler.org:80/announce 314ms — announce with peers:1
  [ALIVE] (81/320) https://4.tracker.eu.org:443/announce 48ms — announce without peers
  [ALIVE] (82/320) http://tracker.dler.com:6969/announce 535ms — announce with peers:1
  [ALIVE] (83/320) http://tracker.mywaifu.best:6969/announce 446ms — announce without peers
  [ALIVE] (84/320) http://retracker.x2k.ru:80/announce 788ms — announce with peers:1
  [ALIVE] (85/320) http://tracker.waaa.moe:6969/announce 231ms — announce with peers:1
  [ALIVE] (86/320) https://t.213891.xyz:443/announce 36ms — announce without peers
  [ALIVE] (87/320) https://1.tracker.eu.org:443/announce 44ms — announce without peers
  [ALIVE] (88/320) https://2.tracker.eu.org:443/announce 42ms — announce without peers
  [ALIVE] (89/320) https://3.tracker.eu.org:443/announce 41ms — announce without peers
  [ALIVE] (90/320) https://tr.nyacat.pw:443/announce 193ms — announce without peers
  [ALIVE] (91/320) http://open.tracker.cl:1337/announce 266ms — announce with peers:1
  [ALIVE] (94/320) https://tracker.foreverpirates.co:443/announce 228ms — announce without peers
  [ALIVE] (95/320) https://tracker.7471.top:443/announce 190ms — announce without peers
  [ALIVE] (97/320) https://337hhh.xyz:443/announce 439ms — announce without peers
  [ALIVE] (98/320) https://tracker.midnightprogrammer.net:443/announce 263ms — announce without peers
  [DEAD]  (100/320) https://tracker.pmman.tech:443/announce — HTTPError: HTTP Error 404: Not Found
  [ALIVE] (101/320) https://tracker.zhuqiy.com:443/announce 129ms — announce with peers:1
  [ALIVE] (102/320) udp://132.226.6.145:6969/announce 108ms — valid connect + announce (v4)
  [ALIVE] (103/320) udp://209.141.59.25:6969/announce 32ms — valid connect + announce (v4)
  [ALIVE] (104/320) udp://109.201.134.183:80/announce 131ms — valid connect + announce (v4)
  [ALIVE] (105/320) udp://193.148.251.93:6969/announce 88ms — valid connect + announce (v4)
  [ALIVE] (106/320) udp://23.157.120.14:6969/announce 48ms — valid connect + announce (v4)
  [ALIVE] (107/320) udp://135.125.198.235:1984/announce 148ms — valid connect + announce (v4)
  [ALIVE] (108/320) https://tracker.nekomi.cn:443/announce 41ms — announce with peers:1
  [ALIVE] (109/320) udp://151.242.104.187:80/announce 149ms — valid connect + announce (v4)
  [ALIVE] (110/320) udp://185.121.168.96:1337/announce 130ms — valid connect + announce (v4)
  [ALIVE] (111/320) udp://34.66.57.33:1337/announce 53ms — valid connect + announce (v4)
  [ALIVE] (113/320) udp://34.66.57.33:80/announce 52ms — valid connect + announce (v4)
  [ALIVE] (114/320) udp://51.81.222.188:6969/announce 30ms — valid connect + announce (v4)
  [ALIVE] (115/320) udp://211.75.205.188:6969/announce 146ms — valid connect + announce (v4)
  [ALIVE] (116/320) udp://211.75.210.221:80/announce 140ms — valid connect + announce (v4)
  [ALIVE] (117/320) udp://193.34.92.5:80/announce 169ms — valid connect + announce (v4)
  [ALIVE] (118/320) udp://31.38.161.123:6969/announce 143ms — valid connect + announce (v4)
  [ALIVE] (119/320) udp://31.56.179.159:6969/announce 160ms — valid connect + announce (v4)
  [ALIVE] (120/320) udp://43.250.54.126:6969/announce 130ms — valid connect + announce (v4)
  [ALIVE] (121/320) udp://51.15.41.46:6969/announce 131ms — valid connect + announce (v4)
  [ALIVE] (123/320) udp://43.154.112.29:17272/announce 153ms — valid connect + announce (v4)
  [ALIVE] (125/320) udp://45.137.199.107:6969/announce 164ms — valid connect + announce (v4)
  [ALIVE] (129/320) http://opentracker.xyz:80/announce 1618ms — announce with peers:1
  [ALIVE] (133/320) udp://93.158.213.92:1337/announce 131ms — valid connect + announce (v4)
  [ALIVE] (135/320) udp://89.234.156.205:451/announce 139ms — valid connect + announce (v4)
  [ALIVE] (136/320) udp://65.109.28.17:6969/announce 161ms — valid connect + announce (v4)
  [ALIVE] (137/320) udp://93.158.213.92:6969/announce 130ms — valid connect + announce (v4)
  [ALIVE] (140/320) udp://open.ftorrent.com:443/announce 35ms — valid connect + announce (v4)
  [ALIVE] (142/320) udp://95.217.80.20:6969/announce 162ms — valid connect + announce (v4)
  [ALIVE] (143/320) udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 149ms — valid connect + announce (v4)
  [ALIVE] (144/320) udp://95.217.80.22:6969/announce 159ms — valid connect + announce (v4)
  [ALIVE] (146/320) udp://explodie.org:6969/announce 21ms — valid connect + announce (v4)
  [ALIVE] (147/320) udp://evan.im:6969/announce 53ms — valid connect + announce (v4)
  [ALIVE] (148/320) udp://ipv4announce.sktorrent.eu:6969/announce 143ms — valid connect + announce (v4)
  [ALIVE] (149/320) udp://tracker.004430.xyz:1337/announce 8ms — valid connect + announce (v4)
  [SKIP]   (150/320) http://tracker.nyaa2p.i2p:80/announce — I2P network required
  [ALIVE] (151/320) udp://martin-gebhardt.eu:25/announce 136ms — valid connect + announce (v4)
  [ALIVE] (152/320) udp://open.demonii.com:1337/announce 130ms — valid connect + announce (v4)
  [ALIVE] (153/320) udp://mail.segso.net:6969/announce 159ms — valid connect + announce (v4)
  [ALIVE] (154/320) udp://open.stealth.si:80/announce 163ms — valid connect + announce (v4)
  [ALIVE] (155/320) udp://tr4ck3r.duckdns.org:6969/announce 69ms — valid connect + announce (v4)
  [ALIVE] (156/320) udp://kolankoalastree.newtrackon.co.nz:1337/announce 142ms — valid connect + announce (v4)
  [ALIVE] (157/320) udp://bt-tracker.de:6969/announce 127ms — valid connect + announce (v4)
  [ALIVE] (158/320) udp://tracker.bittor.pw:1337/announce 53ms — valid connect + announce (v4)
  [ALIVE] (160/320) udp://tracker-udp.gbitt.info:80/announce 130ms — valid connect + announce (v4)
  [ALIVE] (161/320) udp://retracker01-msk-virt.corbina.net:80/announce 183ms — valid connect + announce (v4)
  [ALIVE] (162/320) udp://tracker.corpscorp.online:80/announce 53ms — valid connect + announce (v4)
  [ALIVE] (163/320) udp://tracker.dler.org:6969/announce 147ms — valid connect + announce (v4)
  [ALIVE] (164/320) udp://tracker.opentrackr.org:1337/announce 131ms — valid connect + announce (v4)
  [ALIVE] (165/320) udp://tracker.filemail.com:6969/announce 135ms — valid connect + announce (v4)
  [ALIVE] (166/320) udp://opentracker.lain.moscow:6969/announce 148ms — valid connect + announce (v4)
  [ALIVE] (167/320) udp://tracker.farted.net:6969/announce 160ms — valid connect + announce (v4)
  [ALIVE] (168/320) udp://tracker.qu.ax:6969/announce 130ms — valid connect + announce (v4)
  [ALIVE] (169/320) udp://tracker.nyaa.vc:6969/announce 173ms — valid connect + announce (v4)
  [ALIVE] (170/320) udp://tracker.gmi.gd:6969/announce 43ms — valid connect + announce (v4)
  [ALIVE] (171/320) udp://tracker.ducks.party:1984/announce 148ms — valid connect + announce (v4)
  [ALIVE] (172/320) udp://tracker.peerfect.org:6969/announce 161ms — valid connect + announce (v4)
  [ALIVE] (174/320) udp://tracker.skynetcloud.site:6969/announce 130ms — valid connect + announce (v4)
  [ALIVE] (175/320) udp://tracker2.dler.org:80/announce 147ms — valid connect + announce (v4)
  [ALIVE] (176/320) http://tracker.dhitechnical.com:6969/announce 2980ms — announce with peers:1
  [ALIVE] (180/320) udp://tracker.aruku.ovh:8081/announce 177ms — valid connect + announce (v4)
  [ALIVE] (185/320) udp://t.overflow.biz:6969/announce 154ms — valid connect + announce (v4)
  [ALIVE] (188/320) udp://tracker.torrent.eu.org:451/announce 134ms — valid connect + announce (v4)
  [ALIVE] (190/320) udp://52.58.128.163:6969/announce 140ms — valid connect + announce (v4)
  [DEAD]  (200/320) udp://torrents.tmtime.dev:6969/announce — no connect response
  [DEAD]  (225/320) udp://1c.premierzal.ru:6969/announce — no connect response
  [DEAD]  (250/320) udp://bt1.archive.org:6969/announce — no connect response
  [DEAD]  (275/320) udp://laestrygonian.ooguy.com:9001/announce — no connect response
  [DEAD]  (300/320) udp://moonburrow.club:6969/announce — no connect response

[INFO] First pass done in 55.3s
[INFO] Multi-sample: 3 samples on top 50 alive trackers...
[INFO] Multi-sample refined 48 trackers (median + jitter penalty)
[INFO] Same-subnet(/24) dedup removed 55 slower tracker(s)
[INFO] scrape probe: 20 http/https alive trackers
[INFO] scrape: 3 responded, 1 with seeders
[INFO] discovered candidates excluded from all: 1068
[INFO] Dynamic blacklist: 3 consistently-dead trackers

===== Test Summary =====
  Total tested:   320
  Alive (raw):    57
  All (final):    55 (top 59 by composite score)
  Unsafe filtered:5
  Low-speed:      0 (>5s excluded)
  Same-subnet dedup:  55 (kept faster)
  Dead final:     246
  Time:           64.3s
=== 协议分布统计 ===
  HTTP  : 40 个
  HTTPS : 13 个
  UDP   : 59 个
  WSS   : 0 个
  WS    : 0 个
  总计: 112 个（存活）
=========================
[OK]   /s/all
[OK]   index.html
[OK] Pages regenerated with all statistics.
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
 Round 1 - 2026-10-17 00:22:30
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 62 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 241 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 17 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 18 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 19 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 61 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 23 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 52 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_all.txt: 55 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1286 candidates in 1 file(s)
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /all.txt: 55 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 62 trackers
  [PASS] Plain text: /adysec_best.txt: 241 trackers
  [PASS] Plain text: /gonghailink_best.txt: 17 trackers
  [PASS] Plain text: /pandamen_best.txt: 18 trackers
  [PASS] Plain text: /gspu_best.txt: 19 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 15 trackers
  [PASS] Plain text: /pexcn_best.txt: 61 trackers
  [PASS] Plain text: /opentracker.txt: 23 trackers
  [PASS] Plain text: /run_ws.txt: 52 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 78 trackers
  [PASS] Plain text: /http.txt: 102 trackers
  [PASS] Plain text: /https.txt: 19 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Merged dedup check: 200 unique
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
  [WARN] Source freshness: linuxjin-best unchanged 8d
  [WARN] Source freshness: ngosang-i2p unchanged 8d
  [WARN] Source freshness: ngosang-yggdrasil unchanged 8d
------------------------------------------------------------
  Result: 67 passed, 3 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 1 rounds completed
   Total PASS: 67
   Total WARN: 3
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################

============================================================
 Round 1 - 2026-10-17 00:22:38
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 62 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 241 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 17 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 18 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 19 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 61 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 23 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 52 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_all.txt: 55 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1286 candidates in 1 file(s)
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /all.txt: 55 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 62 trackers
  [PASS] Plain text: /adysec_best.txt: 241 trackers
  [PASS] Plain text: /gonghailink_best.txt: 17 trackers
  [PASS] Plain text: /pandamen_best.txt: 18 trackers
  [PASS] Plain text: /gspu_best.txt: 19 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 15 trackers
  [PASS] Plain text: /pexcn_best.txt: 61 trackers
  [PASS] Plain text: /opentracker.txt: 23 trackers
  [PASS] Plain text: /run_ws.txt: 52 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 78 trackers
  [PASS] Plain text: /http.txt: 102 trackers
  [PASS] Plain text: /https.txt: 19 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Merged dedup check: 200 unique
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
  [PASS] Raw: merged (Raw): HTTP 200, 200 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 200 trackers
  [PASS] Pages short: /s/all: HTTP 200, redirect OK
  [PASS] Worker all 短链: HTTP 200, 55 trackers
  [PASS] Worker all 加速: HTTP 200, 55 trackers
  [WARN] Source freshness: linuxjin-best unchanged 8d
  [WARN] Source freshness: ngosang-i2p unchanged 8d
  [WARN] Source freshness: ngosang-yggdrasil unchanged 8d
------------------------------------------------------------
  Result: 72 passed, 3 warnings, 0 failed
============================================================

============================================================
 Round 2 - 2026-10-17 00:22:44
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 62 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 241 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 17 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 18 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 19 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 61 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 23 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 52 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_all.txt: 55 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1286 candidates in 1 file(s)
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /all.txt: 55 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 62 trackers
  [PASS] Plain text: /adysec_best.txt: 241 trackers
  [PASS] Plain text: /gonghailink_best.txt: 17 trackers
  [PASS] Plain text: /pandamen_best.txt: 18 trackers
  [PASS] Plain text: /gspu_best.txt: 19 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 15 trackers
  [PASS] Plain text: /pexcn_best.txt: 61 trackers
  [PASS] Plain text: /opentracker.txt: 23 trackers
  [PASS] Plain text: /run_ws.txt: 52 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 78 trackers
  [PASS] Plain text: /http.txt: 102 trackers
  [PASS] Plain text: /https.txt: 19 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Merged dedup check: 200 unique
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
  [PASS] Raw: merged (Raw): HTTP 200, 200 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 200 trackers
  [PASS] Pages short: /s/all: HTTP 200, redirect OK
  [PASS] Worker all 短链: HTTP 200, 55 trackers
  [PASS] Worker all 加速: HTTP 200, 55 trackers
  [WARN] Source freshness: linuxjin-best unchanged 8d
  [WARN] Source freshness: ngosang-i2p unchanged 8d
  [WARN] Source freshness: ngosang-yggdrasil unchanged 8d
------------------------------------------------------------
  Result: 72 passed, 3 warnings, 0 failed
============================================================

============================================================
 Round 3 - 2026-10-17 00:22:49
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 62 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 241 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 17 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 18 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 19 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 61 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 23 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 52 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_all.txt: 55 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1286 candidates in 1 file(s)
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /all.txt: 55 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 62 trackers
  [PASS] Plain text: /adysec_best.txt: 241 trackers
  [PASS] Plain text: /gonghailink_best.txt: 17 trackers
  [PASS] Plain text: /pandamen_best.txt: 18 trackers
  [PASS] Plain text: /gspu_best.txt: 19 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 15 trackers
  [PASS] Plain text: /pexcn_best.txt: 61 trackers
  [PASS] Plain text: /opentracker.txt: 23 trackers
  [PASS] Plain text: /run_ws.txt: 52 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 78 trackers
  [PASS] Plain text: /http.txt: 102 trackers
  [PASS] Plain text: /https.txt: 19 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Merged dedup check: 200 unique
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
  [PASS] Raw: merged (Raw): HTTP 200, 200 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 200 trackers
  [PASS] Pages short: /s/all: HTTP 200, redirect OK
  [PASS] Worker all 短链: HTTP 200, 55 trackers
  [PASS] Worker all 加速: HTTP 200, 55 trackers
  [WARN] Source freshness: linuxjin-best unchanged 8d
  [WARN] Source freshness: ngosang-i2p unchanged 8d
  [WARN] Source freshness: ngosang-yggdrasil unchanged 8d
------------------------------------------------------------
  Result: 72 passed, 3 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 3 rounds completed
   Total PASS: 216
   Total WARN: 9
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################
=== End of diagnostics (Sat Oct 17 00:22:49 UTC 2026) ===
