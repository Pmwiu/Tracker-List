=== Diagnostics Fri Oct 16 21:26:24 UTC 2026 ===
Python: Python 3.12.15
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_best.txt
  HTTP 200, total 0.063499s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_best_ip.txt
  HTTP 200, total 0.092099s
>>> https://cf.trackerslist.com/best.txt
  HTTP 200, total 0.180539s
>>> https://tracker.adysec.com/trackers_best.txt
  HTTP 200, total 0.208480s
>>> https://raw.githubusercontent.com/gonghailink/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.174073s
>>> https://raw.githubusercontent.com/panda-men/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.151212s
>>> https://raw.githubusercontent.com/gspu/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.178325s
>>> https://raw.githubusercontent.com/linux-jin/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.214571s
>>> https://raw.githubusercontent.com/AlphaCatMeow/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.148838s
>>> https://raw.githubusercontent.com/pexcn/daily/gh-pages/trackerlist/trackerlist-best.txt
  HTTP 200, total 0.164382s
>>> https://raw.githubusercontent.com/1265578519/OpenTracker/refs/heads/master/tracker.txt
  HTTP 200, total 0.116134s
>>> https://trackers.run/s/rw_ws_up_hp_hs_v4_v6.txt
  HTTP 200, total 0.563942s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_i2p.txt
  HTTP 200, total 0.084828s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_yggdrasil.txt
  HTTP 200, total 0.088733s
[INFO] public list https://cf.trackerslist.com/all.txt: 119 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all.txt: 72 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ip.txt: 53 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_udp.txt: 45 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_http.txt: 17 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_https.txt: 10 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ws.txt: 3 urls
[OK]   1279 new candidates -> candidates_20261016.txt
[OK]   1279 new candidates
[INFO] Repo: Pmwiu/Tracker-List, Max: 25
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/ngosang/trackerslist/master/blacklist.txt (391 URLs)
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/blacklist.txt (20 URLs)
[INFO] URL blacklist: 390 URLs (dynamic + remote sources)
[INFO] Protected hosts (防误杀): 60
[INFO] discovered candidates: 1061 URLs in 1 file(s)

[INFO] trackers_ngosang_best.txt (ngosang-best)
[OK]   20 unique

[INFO] trackers_ngosang_best_ip.txt (ngosang-best-ip)
[OK]   20 unique

[INFO] trackers_cf_best.txt (cf-best)
  [INFO] Skipped 10 dynamic-blacklisted lines
[OK]   61 unique

[INFO] trackers_adysec_best.txt (adysec-best)
  [INFO] Skipped 67 dynamic-blacklisted lines
[OK]   244 unique

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
[OK]   51 unique

[INFO] trackers_ngosang_i2p.txt (ngosang-i2p)
[OK]   17 unique

[INFO] trackers_ngosang_yggdrasil.txt (ngosang-yggdrasil)
  [INFO] Skipped 1 dynamic-blacklisted lines
[WARN] trackers_ngosang_yggdrasil.txt failed (No valid trackers found in response); using backup (1 trackers)
[OK]   1 unique

[INFO] all 合并贡献: ngosang-best=20, ngosang-best-ip=20, cf-best=29, adysec-best=28, gonghailink-best=7, pandamen-best=8, gspu-best=3, linuxjin-best=1, alphacatmeow-best=3, pexcn-best=0, opentracker=10, trackersrun-ws=17, ngosang-i2p=17, ngosang-yggdrasil=1
[INFO] all 协议分布: http=102, https=19, udp=78, wss=1, ws=0

[OK]   merged: 200
[OK]   source_counts.json (200)
[OK]   discovered_set.json (1061)
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
  trackers_cf_best.txt: 61
  trackers_adysec_best.txt: 244
  trackers_gonghailink_best.txt: 17
  trackers_pandamen_best.txt: 18
  trackers_gspu_best.txt: 19
  trackers_linuxjin_best.txt: 20
  trackers_alphacatmeow_best.txt: 15
  trackers_pexcn_best.txt: 61
  trackers_opentracker.txt: 23
  trackers_run_ws.txt: 51
  trackers_ngosang_i2p.txt: 17
  trackers_ngosang_yggdrasil.txt: 1
  trackers_merged.txt: 200
  alive capped at 25 after test+sort
===================
[INFO] reserve: +120 discovered candidates for liveness test (rotation, cap 120)
[INFO] Testing 320 candidates (all-pool=200, timeout=10s, workers=30)
[INFO] Max alive trackers after scoring: 25
  [ALIVE] (4/320) http://004430.xyz:80/announce 142ms — announce with peers:1
  [ALIVE] (5/320) http://140.235.237.23:6969/announce 113ms — announce with peers:1
  [ALIVE] (6/320) http://135.125.198.235:80/announce 236ms — announce without peers
  [ALIVE] (7/320) http://135.125.198.235:2710/announce 237ms — announce without peers
  [ALIVE] (8/320) http://107.189.2.131:1337/announce 267ms — announce with peers:1
  [ALIVE] (9/320) http://1337.abcvg.info:80/announce 216ms — announce with peers:1
  [ALIVE] (10/320) http://138.186.10.167:1337/announce 263ms — announce with peers:1
  [ALIVE] (13/320) http://185.126.65.92:6969/announce 208ms — announce without peers
  [ALIVE] (16/320) http://189.18.97.208:6969/announce 292ms — announce with peers:1
  [ALIVE] (17/320) http://207.241.226.111:6969/announce 87ms — announce with peers:1
  [ALIVE] (18/320) http://207.241.231.226:6969/announce 98ms — announce with peers:1
  [ALIVE] (19/320) http://211.75.205.187:6969/announce 334ms — announce with peers:1
  [ALIVE] (20/320) http://211.75.205.187:80/announce 334ms — announce with peers:1
  [ALIVE] (21/320) http://211.75.205.188:6969/announce 339ms — announce with peers:1
  [ALIVE] (22/320) http://211.75.205.188:80/announce 335ms — announce with peers:1
  [ALIVE] (23/320) http://211.75.210.221:6969/announce 334ms — announce with peers:1
  [ALIVE] (24/320) http://211.75.210.221:80/announce 334ms — announce with peers:1
  [ALIVE] (25/320) http://216.144.239.90:6969/announce 106ms — announce with peers:1
  [ALIVE] (26/320) http://31.38.161.123:6969/announce 278ms — announce with peers:1
  [ALIVE] (27/320) http://43.250.54.126:6969/announce 222ms — announce with peers:1
  [ALIVE] (28/320) http://93.158.213.92:1337/announce 208ms — announce with peers:1
  [ALIVE] (29/320) http://94.23.207.177:6969/announce 232ms — announce with peers:1
  [ALIVE] (30/320) http://announce.sktorrent.eu:6969/announce 277ms — announce with peers:1
  [ALIVE] (31/320) http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 275ms — announce with peers:1
  [DEAD]  (50/320) http://116.9.207.121:6969/announce — URLError: <urlopen error timed out>
  [ALIVE] (65/320) http://ipv4announce.sktorrent.eu:6969/announce 238ms — announce with peers:1
  [ALIVE] (68/320) http://open.demonii.si:80/announce 279ms — announce without peers
  [ALIVE] (72/320) http://tracker.auctor.tv:6969/announce 229ms — announce with peers:1
  [ALIVE] (73/320) http://tracker.dhitechnical.com:6969/announce 172ms — announce with peers:1
  [ALIVE] (74/320) http://tracker.qu.ax:6969/announce 214ms — announce with peers:1
  [ALIVE] (75/320) http://tracker.mywaifu.best:6969/announce 255ms — announce without peers
  [ALIVE] (76/320) https://004430.xyz:443/announce 167ms — announce with peers:1
  [ALIVE] (77/320) http://retracker.x2k.ru:80/announce 430ms — announce with peers:1
  [ALIVE] (78/320) http://tracker.renfei.net:8080/announce 134ms — announce with peers:1
  [ALIVE] (79/320) http://tracker.dler.com:6969/announce 380ms — announce with peers:1
  [ALIVE] (80/320) http://tracker.dler.org:6969/announce 382ms — announce with peers:1
  [ALIVE] (82/320) https://1.tracker.eu.org:443/announce 79ms — announce without peers
  [ALIVE] (83/320) http://tracker.waaa.moe:6969/announce 88ms — announce with peers:1
  [ALIVE] (84/320) http://retracker01-msk-virt.corbina.net:80/announce 557ms — announce with peers:1
  [ALIVE] (85/320) http://tracker2.dler.org:80/announce 381ms — announce with peers:1
  [ALIVE] (86/320) https://t.213891.xyz:443/announce 76ms — announce without peers
  [ALIVE] (87/320) http://tracker.opentrackr.org:1337/announce 379ms — announce with peers:1
  [ALIVE] (88/320) https://3.tracker.eu.org:443/announce 89ms — announce without peers
  [ALIVE] (89/320) https://2.tracker.eu.org:443/announce 79ms — announce without peers
  [ALIVE] (90/320) https://4.tracker.eu.org:443/announce 104ms — announce without peers
  [ALIVE] (91/320) http://open.tracker.cl:1337/announce 268ms — announce with peers:1
  [ALIVE] (93/320) https://tracker.7471.top:443/announce 190ms — announce without peers
  [ALIVE] (95/320) https://337hhh.xyz:443/announce 376ms — announce without peers
  [ALIVE] (96/320) http://opentracker.xyz:80/announce 725ms — announce with peers:1
  [ALIVE] (97/320) https://tr.nyacat.pw:443/announce 172ms — announce without peers
  [ALIVE] (99/320) udp://193.148.251.93:6969/announce 28ms — valid connect + announce (v4)
  [ALIVE] (100/320) udp://109.201.134.183:80/announce 111ms — valid connect + announce (v4)
  [ALIVE] (101/320) https://tracker.zhuqiy.com:443/announce 119ms — announce with peers:1
  [ALIVE] (102/320) udp://135.125.198.235:1984/announce 124ms — valid connect + announce (v4)
  [ALIVE] (103/320) udp://132.226.6.145:6969/announce 143ms — valid connect + announce (v4)
  [ALIVE] (104/320) udp://151.242.104.187:80/announce 125ms — valid connect + announce (v4)
  [ALIVE] (105/320) https://tracker.foreverpirates.co:443/announce 525ms — announce without peers
  [ALIVE] (106/320) udp://34.66.57.33:1337/announce 23ms — valid connect + announce (v4)
  [ALIVE] (107/320) udp://23.157.120.14:6969/announce 69ms — valid connect + announce (v4)
  [ALIVE] (109/320) udp://34.66.57.33:80/announce 30ms — valid connect + announce (v4)
  [ALIVE] (110/320) udp://185.121.168.96:1337/announce 160ms — valid connect + announce (v4)
  [ALIVE] (111/320) udp://193.34.92.5:80/announce 159ms — valid connect + announce (v4)
  [ALIVE] (112/320) https://tracker.nekomi.cn:443/announce 146ms — announce with peers:1
  [ALIVE] (113/320) udp://211.75.205.188:6969/announce 168ms — valid connect + announce (v4)
  [ALIVE] (114/320) udp://211.75.210.221:80/announce 166ms — valid connect + announce (v4)
  [ALIVE] (115/320) udp://31.56.179.159:6969/announce 137ms — valid connect + announce (v4)
  [ALIVE] (116/320) udp://31.38.161.123:6969/announce 143ms — valid connect + announce (v4)
  [ALIVE] (117/320) udp://51.81.222.188:6969/announce 52ms — valid connect + announce (v4)
  [ALIVE] (118/320) http://tracker.nyaa.vc:6969/announce 1308ms — announce without peers
  [ALIVE] (119/320) udp://43.250.54.126:6969/announce 113ms — valid connect + announce (v4)
  [ALIVE] (120/320) udp://51.15.41.46:6969/announce 113ms — valid connect + announce (v4)
  [ALIVE] (121/320) udp://45.137.199.107:6969/announce 151ms — valid connect + announce (v4)
  [ALIVE] (122/320) udp://43.154.112.29:17272/announce 181ms — valid connect + announce (v4)
  [ALIVE] (123/320) udp://93.158.213.92:1337/announce 111ms — valid connect + announce (v4)
  [ALIVE] (124/320) udp://89.234.156.205:451/announce 122ms — valid connect + announce (v4)
  [ALIVE] (125/320) udp://65.109.28.17:6969/announce 140ms — valid connect + announce (v4)
  [ALIVE] (126/320) https://tracker.midnightprogrammer.net:443/announce 891ms — announce without peers
  [ALIVE] (128/320) udp://95.217.80.20:6969/announce 144ms — valid connect + announce (v4)
  [ALIVE] (134/320) udp://95.217.80.22:6969/announce 139ms — valid connect + announce (v4)
  [ALIVE] (135/320) udp://evan.im:6969/announce 35ms — valid connect + announce (v4)
  [ALIVE] (141/320) udp://93.158.213.92:6969/announce 120ms — valid connect + announce (v4)
  [ALIVE] (143/320) udp://open.ftorrent.com:443/announce 20ms — valid connect + announce (v4)
  [ALIVE] (145/320) udp://ipv4announce.sktorrent.eu:6969/announce 113ms — valid connect + announce (v4)
  [ALIVE] (146/320) udp://explodie.org:6969/announce 69ms — valid connect + announce (v4)
  [ALIVE] (148/320) udp://tr4ck3r.duckdns.org:6969/announce 47ms — valid connect + announce (v4)
  [ALIVE] (149/320) udp://martin-gebhardt.eu:25/announce 122ms — valid connect + announce (v4)
  [ALIVE] (150/320) udp://mail.segso.net:6969/announce 141ms — valid connect + announce (v4)
  [ALIVE] (151/320) udp://kolankoalastree.newtrackon.co.nz:1337/announce 172ms — valid connect + announce (v4)
  [ALIVE] (152/320) udp://tracker.004430.xyz:1337/announce 46ms — valid connect + announce (v4)
  [ALIVE] (153/320) udp://open.stealth.si:80/announce 125ms — valid connect + announce (v4)
  [ALIVE] (154/320) udp://open.demonii.com:1337/announce 166ms — valid connect + announce (v4)
  [ALIVE] (156/320) udp://retracker01-msk-virt.corbina.net:80/announce 159ms — valid connect + announce (v4)
  [ALIVE] (157/320) udp://tracker.bittor.pw:1337/announce 30ms — valid connect + announce (v4)
  [ALIVE] (158/320) udp://tracker.corpscorp.online:80/announce 34ms — valid connect + announce (v4)
  [ALIVE] (160/320) udp://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 527ms — valid connect + announce (v4)
  [ALIVE] (162/320) udp://tracker.opentrackr.org:1337/announce 113ms — valid connect + announce (v4)
  [ALIVE] (163/320) udp://tracker.nyaa.vc:6969/announce 133ms — valid connect + announce (v4)
  [ALIVE] (164/320) udp://tracker.dler.org:6969/announce 175ms — valid connect + announce (v4)
  [ALIVE] (165/320) udp://tracker.farted.net:6969/announce 150ms — valid connect + announce (v4)
  [ALIVE] (166/320) udp://t.overflow.biz:6969/announce 152ms — valid connect + announce (v4)
  [ALIVE] (167/320) udp://tracker-udp.gbitt.info:80/announce 228ms — valid connect + announce (v4)
  [ALIVE] (168/320) udp://tracker.ducks.party:1984/announce 133ms — valid connect + announce (v4)
  [ALIVE] (169/320) udp://tracker.gmi.gd:6969/announce 76ms — valid connect + announce (v4)
  [ALIVE] (170/320) udp://tracker.peerfect.org:6969/announce 139ms — valid connect + announce (v4)
  [ALIVE] (171/320) udp://opentracker.lain.moscow:6969/announce 122ms — valid connect + announce (v4)
  [ALIVE] (173/320) udp://tracker.aruku.ovh:8081/announce 197ms — valid connect + announce (v4)
  [ALIVE] (174/320) udp://tracker.tryhackx.org:6969/announce 126ms — valid connect + announce (v4)
  [ALIVE] (175/320) udp://tracker2.dler.org:80/announce 167ms — valid connect + announce (v4)
  [ALIVE] (176/320) udp://tracker.qu.ax:6969/announce 395ms — valid connect + announce (v4)
  [ALIVE] (177/320) udp://tracker.skynetcloud.site:6969/announce 353ms — valid connect + announce (v4)
  [ALIVE] (180/320) udp://tracker.torrent.eu.org:451/announce 128ms — valid connect + announce (v4)
  [ALIVE] (185/320) udp://52.58.128.163:6969/announce 123ms — valid connect + announce (v4)
  [ALIVE] (188/320) http://tracker.novaopcj.eu.org:6969/announce 219ms — announce with peers:1
  [ALIVE] (190/320) udp://tracker.theoks.net:6969/announce 57ms — valid connect + announce (v4)
  [DEAD]  (200/320) udp://torrents.tmtime.dev:6969/announce — no connect response
  [DEAD]  (225/320) http://tracker1.torrentino.com:80/announce — invalid bencoded response
  [ALIVE] (227/320) http://tracker.zhuqiy.dgj055.icu:80/announce 277ms — announce without peers
  [DEAD]  (250/320) http://vps-dd0a0715.vps.ovh.net:6969/announce — URLError: <urlopen error [Errno -2] Name or service not known>
  [DEAD]  (275/320) https://docs.sigstore.dev:443 — invalid bencoded response
  [DEAD]  (300/320) https://dev.tracker.cf-identity-wallet.metadata.dev.cf-deployments.org:443/announce — URLError: <urlopen error [Errno -2] Name or service not known>

[INFO] First pass done in 74.4s
[INFO] Multi-sample: 3 samples on top 50 alive trackers...
[INFO] Multi-sample refined 47 trackers (median + jitter penalty)
[INFO] Same-subnet(/24) dedup removed 57 slower tracker(s)
[INFO] scrape probe: 20 http/https alive trackers
[INFO] scrape: 5 responded, 4 with seeders
[INFO] discovered candidates excluded from best/all: 1061
[INFO] reserve pool: 3 discovered candidates -> trackers_reserve.txt
[INFO] promote queue: 86 tracked, 5 ready to promote
[INFO] Dynamic blacklist: 1 consistently-dead trackers

===== Test Summary =====
  Total tested:   320
  Alive (raw):    57
  Alive (final):  25 (top 25 by composite score)
  Non-UDP kept:   9 (quota >= 4)
  Classic kept:   2 (quota >= 4)
  Score-capped:   32
  Unsafe filtered:4
  Low-speed:      0 (>5s excluded)
  Same-subnet dedup:  57 (kept faster)
  Dead final:     278
  Time:           83.2s
=== 协议分布统计 ===
  HTTP  : 43 个
  HTTPS : 13 个
  UDP   : 58 个
  WSS   : 0 个
  WS    : 0 个
  总计: 114 个（存活）
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
 Round 1 - 2026-10-16 21:28:02
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 61 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 244 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 17 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 18 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 19 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 61 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 23 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 51 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_all.txt: 55 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1279 candidates in 1 file(s)
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /all.txt: 55 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 61 trackers
  [PASS] Plain text: /adysec_best.txt: 244 trackers
  [PASS] Plain text: /gonghailink_best.txt: 17 trackers
  [PASS] Plain text: /pandamen_best.txt: 18 trackers
  [PASS] Plain text: /gspu_best.txt: 19 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 15 trackers
  [PASS] Plain text: /pexcn_best.txt: 61 trackers
  [PASS] Plain text: /opentracker.txt: 23 trackers
  [PASS] Plain text: /run_ws.txt: 51 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 78 trackers
  [PASS] Plain text: /http.txt: 102 trackers
  [PASS] Plain text: /https.txt: 19 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset-of-all check: all 25 best trackers present in all (55)
  [PASS] Reserve pool check: 3 candidates, disjoint
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
  [WARN] Source freshness: linuxjin-best unchanged 8d
  [WARN] Source freshness: ngosang-i2p unchanged 8d
  [WARN] Source freshness: ngosang-yggdrasil unchanged 8d
------------------------------------------------------------
  Result: 75 passed, 3 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 1 rounds completed
   Total PASS: 75
   Total WARN: 3
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################

============================================================
 Round 1 - 2026-10-16 21:28:12
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 61 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 244 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 17 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 18 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 19 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 61 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 23 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 51 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_all.txt: 55 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1279 candidates in 1 file(s)
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /all.txt: 55 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 61 trackers
  [PASS] Plain text: /adysec_best.txt: 244 trackers
  [PASS] Plain text: /gonghailink_best.txt: 17 trackers
  [PASS] Plain text: /pandamen_best.txt: 18 trackers
  [PASS] Plain text: /gspu_best.txt: 19 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 15 trackers
  [PASS] Plain text: /pexcn_best.txt: 61 trackers
  [PASS] Plain text: /opentracker.txt: 23 trackers
  [PASS] Plain text: /run_ws.txt: 51 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 78 trackers
  [PASS] Plain text: /http.txt: 102 trackers
  [PASS] Plain text: /https.txt: 19 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset-of-all check: all 25 best trackers present in all (55)
  [PASS] Reserve pool check: 3 candidates, disjoint
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
  [PASS] Worker all 短链: HTTP 200, 55 trackers
  [PASS] Worker best 加速: HTTP 200, 25 trackers
  [PASS] Worker all 加速: HTTP 200, 52 trackers
  [WARN] Source freshness: linuxjin-best unchanged 8d
  [WARN] Source freshness: ngosang-i2p unchanged 8d
  [WARN] Source freshness: ngosang-yggdrasil unchanged 8d
------------------------------------------------------------
  Result: 85 passed, 3 warnings, 0 failed
============================================================

============================================================
 Round 2 - 2026-10-16 21:28:17
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 61 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 244 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 17 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 18 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 19 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 61 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 23 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 51 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_all.txt: 55 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1279 candidates in 1 file(s)
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /all.txt: 55 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 61 trackers
  [PASS] Plain text: /adysec_best.txt: 244 trackers
  [PASS] Plain text: /gonghailink_best.txt: 17 trackers
  [PASS] Plain text: /pandamen_best.txt: 18 trackers
  [PASS] Plain text: /gspu_best.txt: 19 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 15 trackers
  [PASS] Plain text: /pexcn_best.txt: 61 trackers
  [PASS] Plain text: /opentracker.txt: 23 trackers
  [PASS] Plain text: /run_ws.txt: 51 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 78 trackers
  [PASS] Plain text: /http.txt: 102 trackers
  [PASS] Plain text: /https.txt: 19 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset-of-all check: all 25 best trackers present in all (55)
  [PASS] Reserve pool check: 3 candidates, disjoint
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
  [PASS] Worker all 短链: HTTP 200, 55 trackers
  [PASS] Worker best 加速: HTTP 200, 25 trackers
  [PASS] Worker all 加速: HTTP 200, 52 trackers
  [WARN] Source freshness: linuxjin-best unchanged 8d
  [WARN] Source freshness: ngosang-i2p unchanged 8d
  [WARN] Source freshness: ngosang-yggdrasil unchanged 8d
------------------------------------------------------------
  Result: 85 passed, 3 warnings, 0 failed
============================================================

============================================================
 Round 3 - 2026-10-16 21:28:23
============================================================
  [PASS] Local tracker: trackers_ngosang_best.txt: 20 trackers
  [PASS] Local tracker: trackers_ngosang_best_ip.txt: 20 trackers
  [PASS] Local tracker: trackers_cf_best.txt: 61 trackers
  [PASS] Local tracker: trackers_adysec_best.txt: 244 trackers
  [PASS] Local tracker: trackers_gonghailink_best.txt: 17 trackers
  [PASS] Local tracker: trackers_pandamen_best.txt: 18 trackers
  [PASS] Local tracker: trackers_gspu_best.txt: 19 trackers
  [PASS] Local tracker: trackers_linuxjin_best.txt: 20 trackers
  [PASS] Local tracker: trackers_alphacatmeow_best.txt: 15 trackers
  [PASS] Local tracker: trackers_pexcn_best.txt: 61 trackers
  [PASS] Local tracker: trackers_opentracker.txt: 23 trackers
  [PASS] Local tracker: trackers_run_ws.txt: 51 trackers
  [PASS] Local tracker: trackers_ngosang_i2p.txt: 17 trackers
  [PASS] Local tracker: trackers_ngosang_yggdrasil.txt: 1 trackers
  [PASS] Local tracker: trackers_merged.txt: 200 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_all.txt: 55 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Discovery output: 1279 candidates in 1 file(s)
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /all.txt: 55 trackers
  [PASS] Plain text: /merged.txt: 200 trackers
  [PASS] Plain text: /ngosang_best.txt: 20 trackers
  [PASS] Plain text: /ngosang_best_ip.txt: 20 trackers
  [PASS] Plain text: /cf_best.txt: 61 trackers
  [PASS] Plain text: /adysec_best.txt: 244 trackers
  [PASS] Plain text: /gonghailink_best.txt: 17 trackers
  [PASS] Plain text: /pandamen_best.txt: 18 trackers
  [PASS] Plain text: /gspu_best.txt: 19 trackers
  [PASS] Plain text: /linuxjin_best.txt: 20 trackers
  [PASS] Plain text: /alphacatmeow_best.txt: 15 trackers
  [PASS] Plain text: /pexcn_best.txt: 61 trackers
  [PASS] Plain text: /opentracker.txt: 23 trackers
  [PASS] Plain text: /run_ws.txt: 51 trackers
  [PASS] Plain text: /ngosang_i2p.txt: 17 trackers
  [PASS] Plain text: /ngosang_yggdrasil.txt: 1 trackers
  [PASS] Plain text: /udp.txt: 78 trackers
  [PASS] Plain text: /http.txt: 102 trackers
  [PASS] Plain text: /https.txt: 19 trackers
  [PASS] Plain text: /wss.txt: 1 trackers
  [PASS] Plain text: /ws.txt: 0 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 200 unique
  [PASS] Alive subset-of-all check: all 25 best trackers present in all (55)
  [PASS] Reserve pool check: 3 candidates, disjoint
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
  [PASS] Worker all 短链: HTTP 200, 55 trackers
  [PASS] Worker best 加速: HTTP 200, 25 trackers
  [PASS] Worker all 加速: HTTP 200, 52 trackers
  [WARN] Source freshness: linuxjin-best unchanged 8d
  [WARN] Source freshness: ngosang-i2p unchanged 8d
  [WARN] Source freshness: ngosang-yggdrasil unchanged 8d
------------------------------------------------------------
  Result: 85 passed, 3 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 3 rounds completed
   Total PASS: 255
   Total WARN: 9
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################
=== End of diagnostics (Fri Oct 16 21:28:23 UTC 2026) ===
