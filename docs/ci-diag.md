=== Diagnostics Tue Sep 29 08:22:38 UTC 2026 ===
Python: Python 3.12.14
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://cf.trackerslist.com/all.txt
  HTTP 200, total 0.075564s
>>> https://raw.githubusercontent.com/adysec/tracker/main/trackers_all.txt
  HTTP 200, total 0.140375s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt
  HTTP 200, total 0.025626s
[INFO] Repo: Pmwiu/Tracker-List, Max: 25

[INFO] trackers_cf.txt (cf-all)
[OK]   117 unique

[INFO] trackers_adysec.txt (adysec-all)
[OK]   3535 unique

[INFO] trackers_ngosang.txt (ngosang-all)
[OK]   72 unique

[OK]   merged: 3539
[OK]   MIRRORS.txt
[OK]   /s/alive
[OK]   /s/cf
[OK]   /s/adysec
[OK]   /s/ngosang
[OK]   /s/all
[OK]   index.html
[OK]   docs/alive.txt
[OK]   docs/merged.txt
[OK]   docs/cf.txt
[OK]   docs/ngosang.txt
[OK]   docs/adysec.txt

===== Summary =====
  trackers_cf.txt: 117
  trackers_adysec.txt: 3535
  trackers_ngosang.txt: 72
  trackers_merged.txt: 3539
  alive capped at 25 after test+sort
===================
[INFO] Testing 500 of 3539 candidates (timeout=10s, workers=30, priority sources first)
[INFO] Max alive trackers after scoring: 25
  [ALIVE] (1/500) http://207.241.231.226:6969/announce 117ms — valid announce response
  [ALIVE] (2/500) http://207.241.226.111:6969/announce 130ms — valid announce response
  [ALIVE] (4/500) http://bt2.archive.org:6969/announce 145ms — valid announce response
  [ALIVE] (5/500) http://bt1.archive.org:6969/announce 160ms — valid announce response
  [ALIVE] (6/500) http://004430.xyz:80/announce 190ms — valid announce response
  [ALIVE] (7/500) https://004430.xyz:443/announce 100ms — valid announce response
  [ALIVE] (8/500) https://t.213891.xyz:443/announce 15ms — valid announce response
  [ALIVE] (9/500) http://tracker.dhitechnical.com:6969/announce 195ms — valid announce response
  [ALIVE] (10/500) http://tr.nyacat.pw:80/announce 245ms — valid announce response
  [ALIVE] (11/500) https://1.tracker.eu.org:443/announce 17ms — valid announce response
  [ALIVE] (12/500) https://open.ftorrent.com:443/announce 89ms — valid announce response
  [ALIVE] (13/500) https://1337.abcvg.info:443/announce 242ms — valid announce response
  [ALIVE] (14/500) http://1337.abcvg.info:80/announce 378ms — valid announce response
  [ALIVE] (16/500) http://tracker.waaa.moe:6969/announce 49ms — valid announce response
  [ALIVE] (17/500) https://tr.nyacat.pw:443/announce 157ms — valid announce response
  [ALIVE] (18/500) http://ipv4announce.sktorrent.eu:6969/announce 415ms — valid announce response
  [ALIVE] (19/500) http://announce.sktorrent.eu:6969/announce 428ms — valid announce response
  [ALIVE] (20/500) http://nyaa.tracker.wf:7777/announce 335ms — valid announce response
  [ALIVE] (21/500) http://tracker.zhuqiy.dgj055.icu:80/announce 356ms — valid announce response
  [ALIVE] (24/500) http://107.189.2.131:1337/announce 482ms — valid announce response
  [ALIVE] (25/500) http://tracker.renfei.net:8080/announce 158ms — valid announce response
  [ALIVE] (26/500) http://tracker.dler.org:6969/announce 455ms — valid announce response
  [ALIVE] (27/500) http://tracker2.dler.org:80/announce 280ms — valid announce response
  [ALIVE] (28/500) http://tracker.dler.com:6969/announce 279ms — valid announce response
  [ALIVE] (29/500) http://tracker.qu.ax:6969/announce 290ms — valid announce response
  [ALIVE] (30/500) http://tracker.xn--djrq4gl4hvoi.top:80/announce 218ms — valid announce response
  [ALIVE] (31/500) https://tracker.foreverpirates.co:443/announce 193ms — valid announce response
  [ALIVE] (32/500) http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 523ms — valid announce response
  [ALIVE] (33/500) http://tracker1.itzmx.com:8080/announce 243ms — valid announce response
  [ALIVE] (34/500) udp://explodie.org:6969/announce 29ms — valid connect + announce
  [ALIVE] (35/500) udp://exodus.desync.com:6969/announce 3ms — valid connect + announce
  [ALIVE] (36/500) http://t.overflow.biz:6969/announce 419ms — valid announce response
  [ALIVE] (38/500) http://tracker.mywaifu.best:6969/announce 334ms — valid announce response
  [ALIVE] (39/500) udp://open.ftorrent.com:443/announce 28ms — valid connect + announce
  [ALIVE] (41/500) https://tracker.7471.top:443/announce 178ms — valid announce response
  [ALIVE] (42/500) https://tracker.midnightprogrammer.net:443/announce 272ms — valid announce response
  [ALIVE] (45/500) udp://93.158.213.92:6969/announce 142ms — valid connect + announce
  [ALIVE] (46/500) udp://evan.im:6969/announce 58ms — valid connect + announce
  [ALIVE] (47/500) https://tracker.zhuqiy.com:443/announce 321ms — valid announce response
  [ALIVE] (48/500) https://tracker.qingwapt.org:443/announce 202ms — online (failure reason)
  [ALIVE] (49/500) udp://ns575949.ip-51-222-82.net:6969/announce 67ms — valid connect + announce
  [ALIVE] (50/500) http://tracker.opentrackr.org:1337/announce 581ms — valid announce response
  [ALIVE] (51/500) udp://ipv4announce.sktorrent.eu:6969/announce 144ms — valid connect + announce
  [ALIVE] (52/500) http://retracker01-msk-virt.corbina.net:80/announce 568ms — valid announce response
  [ALIVE] (53/500) udp://seedpeer.net:6969/announce 65ms — valid connect + announce
  [ALIVE] (54/500) udp://martin-gebhardt.eu:25/announce 153ms — valid connect + announce
  [ALIVE] (55/500) udp://anime-tracker.aruku.kro.kr:8081/announce 135ms — valid connect + announce
  [ALIVE] (56/500) udp://tracker.004430.xyz:1337/announce 49ms — valid connect + announce
  [ALIVE] (57/500) https://tracker.nekomi.cn:443/announce 79ms — valid announce response
  [ALIVE] (59/500) udp://open.demonii.com:1337/announce 154ms — valid connect + announce
  [ALIVE] (60/500) udp://open.stealth.si:80/announce 172ms — valid connect + announce
  [ALIVE] (61/500) udp://mail.segso.net:6969/announce 171ms — valid connect + announce
  [ALIVE] (63/500) udp://tr4ck3r.duckdns.org:6969/announce 66ms — valid connect + announce
  [ALIVE] (64/500) udp://tracker.bittor.pw:1337/announce 50ms — valid connect + announce
  [ALIVE] (65/500) udp://kolankoalastree.newtrackon.co.nz:1337/announce 177ms — valid connect + announce
  [ALIVE] (66/500) udp://tracker.corpscorp.online:80/announce 49ms — valid connect + announce
  [ALIVE] (67/500) udp://retracker01-msk-virt.corbina.net:80/announce 187ms — valid connect + announce
  [ALIVE] (68/500) udp://t.overflow.biz:6969/announce 168ms — valid connect + announce
  [ALIVE] (70/500) udp://tracker.dler.com:6969/announce 139ms — valid connect + announce
  [ALIVE] (71/500) udp://tracker.dler.org:6969/announce 141ms — valid connect + announce
  [ALIVE] (72/500) udp://opentracker.lain.moscow:6969/announce 155ms — valid connect + announce
  [ALIVE] (73/500) udp://tracker.cn.nyaa.net:6969/announce 149ms — valid connect + announce
  [ALIVE] (74/500) udp://rekcart.duckdns.org:15480/announce 163ms — valid connect + announce
  [ALIVE] (75/500) udp://tracker.ddunlimited.net:6969/announce 156ms — valid connect + announce
  [ALIVE] (76/500) udp://tracker-udp.gbitt.info:80/announce 148ms — valid connect + announce
  [ALIVE] (77/500) udp://tracker.farted.net:6969/announce 165ms — valid connect + announce
  [ALIVE] (78/500) udp://tr3.ysagin.top:2715/announce 159ms — valid connect + announce
  [ALIVE] (79/500) udp://tracker.opentrackr.org:1337/announce 143ms — valid connect + announce
  [ALIVE] (80/500) udp://torrent.tracker.durukanbal.com:6969/announce 147ms — valid connect + announce
  [ALIVE] (81/500) udp://tracker.nyaa.vc:6969/announce 152ms — valid connect + announce
  [ALIVE] (82/500) udp://tracker.k.vu:6969/announce 167ms — valid connect + announce
  [ALIVE] (83/500) udp://tracker.wildkat.net:6969/announce 47ms — valid connect + announce
  [ALIVE] (84/500) udp://tracker.nyaa.net:6969/announce 181ms — valid connect + announce
  [ALIVE] (85/500) udp://tracker.ducks.party:1984/announce 157ms — valid connect + announce
  [ALIVE] (86/500) udp://tracker.opentrackr.com:6969/announce 170ms — valid connect + announce
  [ALIVE] (87/500) udp://tracker.qu.ax:6969/announce 150ms — valid connect + announce
  [ALIVE] (88/500) udp://tracker.ilibr.org:6969/announce 172ms — valid connect + announce
  [ALIVE] (89/500) udp://tracker.aruku.ovh:8081/announce 168ms — valid connect + announce
  [ALIVE] (90/500) udp://tracker.peerfect.org:6969/announce 171ms — valid connect + announce
  [ALIVE] (92/500) wss://tracker.openwebtorrent.com:443/announce 7ms — TLS reachable
  [ALIVE] (93/500) udp://tracker.teambelgium.net:6969/announce 148ms — valid connect + announce
  [ALIVE] (94/500) udp://tracker2.dler.org:80/announce 139ms — valid connect + announce
  [ALIVE] (98/500) udp://tracker.skynetcloud.site:6969/announce 153ms — valid connect + announce
  [ALIVE] (99/500) udp://yuptracker-eu.gaijinent.com:27022/announce 130ms — valid connect + announce
  [ALIVE] (100/500) udp://v2.iperson.xyz:6969/announce 175ms — valid connect + announce
  [ALIVE] (104/500) udp://tracker.torrents.observer:80/announce 144ms — valid connect + announce
  [ALIVE] (105/500) udp://tracker.willy.pro:6969/announce 298ms — valid connect + announce
  [ALIVE] (109/500) udp://tracker.playground.ru:6969/announce 187ms — valid connect + announce
  [ALIVE] (111/500) http://tracker.opentorrent.top:6969/announce 3684ms — valid announce response
  [ALIVE] (113/500) https://pybittrack.retiolus.net:443/announce 8995ms — valid announce response
  [DEAD]  (125/500) http://113.13.7.215:6969/announce — URLError: <urlopen error [Errno 111] Connection refused>
  [DEAD]  (150/500) http://109.71.253.37:1096/announce — URLError: <urlopen error timed out>
  [DEAD]  (175/500) http://113.17.152.30:6969/announce — URLError: <urlopen error timed out>
  [DEAD]  (200/500) http://116.8.90.235:6969/announce — URLError: <urlopen error timed out>
  [DEAD]  (225/500) http://123.245.62.84:6969/announce — URLError: <urlopen error [Errno 111] Connection refused>
  [ALIVE] (236/500) http://135.125.198.235:2710/announce 314ms — valid announce response
  [ALIVE] (243/500) http://135.125.198.235:80/announce 317ms — valid announce response
  [DEAD]  (250/500) http://123.245.62.105:6969/announce — URLError: <urlopen error timed out>
  [ALIVE] (269/500) http://140.235.237.23:6969/announce 1187ms — valid announce response
  [DEAD]  (275/500) http://13.115.115.32:6969/announce — URLError: <urlopen error timed out>
  [DEAD]  (300/500) http://15.204.239.175:6969/announce — URLError: <urlopen error timed out>
  [DEAD]  (325/500) http://152.249.214.74:6969/announce — URLError: <urlopen error timed out>
  [DEAD]  (350/500) http://177.112.215.4:6969/announce — URLError: <urlopen error timed out>
  [ALIVE] (360/500) http://177.188.141.75:6969/announce 336ms — valid announce response
  [DEAD]  (375/500) http://177.172.63.135:6969/announce — URLError: <urlopen error timed out>
  [ALIVE] (400/500) http://185.126.65.92:6969/announce 292ms — valid announce response
  [DEAD]  (425/500) http://179.98.51.66:6969/announce — URLError: <urlopen error timed out>
  [DEAD]  (450/500) http://186.10.170.58:1337/announce — URLError: <urlopen error timed out>
  [DEAD]  (475/500) http://187.57.131.55:6969/announce — URLError: <urlopen error timed out>
  [DEAD]  (500/500) http://189.18.96.56:6969/announce — URLError: <urlopen error timed out>

[INFO] First pass done in 111.7s
[INFO] Second pass: re-testing top 95 alive trackers...
[INFO] Second pass done, refined 93 trackers
[INFO] Low-speed filtered (>5s): 1 trackers
[INFO] Same-IP dedup removed 26 slower tracker(s)

===== Test Summary =====
  Total tested:   500
  Alive (raw):    68
  Alive (final):  25 (top 25 by composite score)
  Score-capped:   43
  Unsafe filtered:0
  Low-speed:      1 (>5s excluded)
  Same-IP dedup:  26 (kept faster)
  Dead final:     475
  Time:           123.9s
  Protocols:      {'http': 32, 'https': 13, 'udp': 49, 'wss': 1}
=========================
[OK]   /s/alive
[OK]   /s/cf
[OK]   /s/adysec
[OK]   /s/ngosang
[OK]   /s/all
[OK]   index.html
[OK] Pages regenerated with alive statistics.
[OK]   docs/alive.txt
[OK]   docs/merged.txt
[OK]   docs/cf.txt
[OK]   docs/ngosang.txt
[OK]   docs/adysec.txt
[OK] Plain-text files synced to docs/.

============================================================
 Round 1 - 2026-09-29 08:24:43
============================================================
  [PASS] Local tracker: trackers_cf.txt: 117 trackers
  [PASS] Local tracker: trackers_adysec.txt: 3535 trackers
  [PASS] Local tracker: trackers_ngosang.txt: 72 trackers
  [PASS] Local tracker: trackers_merged.txt: 3539 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/cf: valid redirect
  [PASS] Local short page: /s/adysec: valid redirect
  [PASS] Local short page: /s/ngosang: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /merged.txt: 3539 trackers
  [PASS] Plain text: /cf.txt: 117 trackers
  [PASS] Plain text: /ngosang.txt: 72 trackers
  [PASS] Plain text: /adysec.txt: 3535 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 3539 unique
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_cf.txt vs cf.txt: identical
  [PASS] Consistency: trackers_ngosang.txt vs ngosang.txt: identical
  [PASS] Consistency: trackers_adysec.txt vs adysec.txt: identical
  [PASS] URL format check: all 3539 valid
------------------------------------------------------------
  Result: 28 passed, 0 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 1 rounds completed
   Total PASS: 28
   Total WARN: 0
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################

============================================================
 Round 1 - 2026-09-29 08:24:51
============================================================
  [PASS] Local tracker: trackers_cf.txt: 117 trackers
  [PASS] Local tracker: trackers_adysec.txt: 3535 trackers
  [PASS] Local tracker: trackers_ngosang.txt: 72 trackers
  [PASS] Local tracker: trackers_merged.txt: 3539 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/cf: valid redirect
  [PASS] Local short page: /s/adysec: valid redirect
  [PASS] Local short page: /s/ngosang: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /merged.txt: 3539 trackers
  [PASS] Plain text: /cf.txt: 117 trackers
  [PASS] Plain text: /ngosang.txt: 72 trackers
  [PASS] Plain text: /adysec.txt: 3535 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 3539 unique
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_cf.txt vs cf.txt: identical
  [PASS] Consistency: trackers_ngosang.txt vs ngosang.txt: identical
  [PASS] Consistency: trackers_adysec.txt vs adysec.txt: identical
  [PASS] URL format check: all 3539 valid
  [PASS] Raw: alive (Raw): HTTP 200, 25 trackers
  [PASS] Raw: merged (Raw): HTTP 200, 3539 trackers
  [PASS] Pages: /alive.txt: HTTP 200, 25 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 3539 trackers
  [PASS] Pages short: /s/alive: HTTP 200, redirect OK
  [PASS] Pages short: /s/cf: HTTP 200, redirect OK
------------------------------------------------------------
  Result: 34 passed, 0 warnings, 0 failed
============================================================

============================================================
 Round 2 - 2026-09-29 08:24:56
============================================================
  [PASS] Local tracker: trackers_cf.txt: 117 trackers
  [PASS] Local tracker: trackers_adysec.txt: 3535 trackers
  [PASS] Local tracker: trackers_ngosang.txt: 72 trackers
  [PASS] Local tracker: trackers_merged.txt: 3539 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/cf: valid redirect
  [PASS] Local short page: /s/adysec: valid redirect
  [PASS] Local short page: /s/ngosang: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /merged.txt: 3539 trackers
  [PASS] Plain text: /cf.txt: 117 trackers
  [PASS] Plain text: /ngosang.txt: 72 trackers
  [PASS] Plain text: /adysec.txt: 3535 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 3539 unique
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_cf.txt vs cf.txt: identical
  [PASS] Consistency: trackers_ngosang.txt vs ngosang.txt: identical
  [PASS] Consistency: trackers_adysec.txt vs adysec.txt: identical
  [PASS] URL format check: all 3539 valid
  [PASS] Raw: alive (Raw): HTTP 200, 25 trackers
  [PASS] Raw: merged (Raw): HTTP 200, 3539 trackers
  [PASS] Pages: /alive.txt: HTTP 200, 25 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 3539 trackers
  [PASS] Pages short: /s/alive: HTTP 200, redirect OK
  [PASS] Pages short: /s/cf: HTTP 200, redirect OK
------------------------------------------------------------
  Result: 34 passed, 0 warnings, 0 failed
============================================================

============================================================
 Round 3 - 2026-09-29 08:25:01
============================================================
  [PASS] Local tracker: trackers_cf.txt: 117 trackers
  [PASS] Local tracker: trackers_adysec.txt: 3535 trackers
  [PASS] Local tracker: trackers_ngosang.txt: 72 trackers
  [PASS] Local tracker: trackers_merged.txt: 3539 trackers
  [PASS] Local tracker: trackers_alive.txt: 25 trackers
  [PASS] Local tracker: trackers_dead.txt: exists
  [PASS] Local MIRRORS.txt: exists
  [PASS] Local test_report.md: exists
  [PASS] Local test_state.json: exists
  [PASS] Local Pages index.html: exists
  [PASS] Local short page: /s/alive: valid redirect
  [PASS] Local short page: /s/cf: valid redirect
  [PASS] Local short page: /s/adysec: valid redirect
  [PASS] Local short page: /s/ngosang: valid redirect
  [PASS] Local short page: /s/all: valid redirect
  [PASS] Plain text: /alive.txt: 25 trackers
  [PASS] Plain text: /merged.txt: 3539 trackers
  [PASS] Plain text: /cf.txt: 117 trackers
  [PASS] Plain text: /ngosang.txt: 72 trackers
  [PASS] Plain text: /adysec.txt: 3535 trackers
  [PASS] Alive count check: 25 in [0, 25]
  [PASS] Merged dedup check: 3539 unique
  [PASS] Consistency: trackers_alive.txt vs alive.txt: identical
  [PASS] Consistency: trackers_merged.txt vs merged.txt: identical
  [PASS] Consistency: trackers_cf.txt vs cf.txt: identical
  [PASS] Consistency: trackers_ngosang.txt vs ngosang.txt: identical
  [PASS] Consistency: trackers_adysec.txt vs adysec.txt: identical
  [PASS] URL format check: all 3539 valid
  [PASS] Raw: alive (Raw): HTTP 200, 25 trackers
  [PASS] Raw: merged (Raw): HTTP 200, 3539 trackers
  [PASS] Pages: /alive.txt: HTTP 200, 25 trackers
  [PASS] Pages: /merged.txt: HTTP 200, 3539 trackers
  [PASS] Pages short: /s/alive: HTTP 200, redirect OK
  [PASS] Pages short: /s/cf: HTTP 200, redirect OK
------------------------------------------------------------
  Result: 34 passed, 0 warnings, 0 failed
============================================================

############################################################
 FINAL REPORT: 3 rounds completed
   Total PASS: 102
   Total WARN: 0
   Total FAIL: 0
   STATUS: ALL ROUNDS HEALTHY (warnings may be network-related)
############################################################
=== End of diagnostics (Tue Sep 29 08:25:01 UTC 2026) ===
