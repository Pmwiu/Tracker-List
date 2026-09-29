=== Diagnostics Tue Sep 29 06:28:33 UTC 2026 ===
Python: Python 3.12.14
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://cf.trackerslist.com/all.txt
  HTTP 200, total 0.133707s
>>> https://raw.githubusercontent.com/adysec/tracker/main/trackers_all.txt
  HTTP 200, total 0.105552s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt
  HTTP 200, total 0.025498s
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
  [ALIVE] (1/500) http://004430.xyz:80/announce 97ms — valid announce response
  [ALIVE] (2/500) http://tr.nyacat.pw:80/announce 111ms — valid announce response
  [ALIVE] (3/500) https://004430.xyz:443/announce 62ms — valid announce response
  [ALIVE] (5/500) http://207.241.226.111:6969/announce 197ms — valid announce response
  [ALIVE] (6/500) http://207.241.231.226:6969/announce 196ms — valid announce response
  [ALIVE] (7/500) https://t.213891.xyz:443/announce 15ms — valid announce response
  [ALIVE] (8/500) http://1337.abcvg.info:80/announce 240ms — valid announce response
  [ALIVE] (9/500) http://tracker.mywaifu.best:6969/announce 239ms — valid announce response
  [ALIVE] (10/500) http://tracker.zhuqiy.dgj055.icu:80/announce 231ms — valid announce response
  [ALIVE] (11/500) http://tracker.qu.ax:6969/announce 164ms — valid announce response
  [ALIVE] (12/500) http://tracker.opentorrent.top:6969/announce 229ms — valid announce response
  [ALIVE] (13/500) http://bt2.archive.org:6969/announce 135ms — valid announce response
  [ALIVE] (14/500) http://bt1.archive.org:6969/announce 198ms — valid announce response
  [ALIVE] (15/500) https://1337.abcvg.info:443/announce 191ms — valid announce response
  [ALIVE] (16/500) http://nyaa.tracker.wf:7777/announce 274ms — valid announce response
  [ALIVE] (17/500) https://tr.nyacat.pw:443/announce 114ms — valid announce response
  [ALIVE] (18/500) http://ipv4announce.sktorrent.eu:6969/announce 183ms — valid announce response
  [ALIVE] (19/500) https://1.tracker.eu.org:443/announce 33ms — valid announce response
  [ALIVE] (20/500) https://tracker.foreverpirates.co:443/announce 121ms — valid announce response
  [ALIVE] (21/500) http://tracker.xn--djrq4gl4hvoi.top:80/announce 274ms — valid announce response
  [DEAD]  (25/500) https://tracker.pmman.tech:443/announce — HTTPError: HTTP Error 404: Not Found
  [ALIVE] (26/500) https://tracker.7471.top:443/announce 121ms — valid announce response
  [ALIVE] (29/500) http://tracker2.dler.org:80/announce 378ms — valid announce response
  [ALIVE] (30/500) http://tracker.dler.com:6969/announce 399ms — valid announce response
  [ALIVE] (31/500) http://tracker.renfei.net:8080/announce 16ms — valid announce response
  [ALIVE] (32/500) udp://evan.im:6969/announce 2ms — valid connect + announce
  [ALIVE] (33/500) http://tracker.opentrackr.org:1337/announce 383ms — valid announce response
  [ALIVE] (34/500) http://announce.sktorrent.eu:6969/announce 381ms — valid announce response
  [ALIVE] (35/500) udp://93.158.213.92:6969/announce 83ms — valid connect + announce
  [ALIVE] (37/500) https://open.ftorrent.com:443/announce 150ms — valid announce response
  [ALIVE] (38/500) udp://ns575949.ip-51-222-82.net:6969/announce 15ms — valid connect + announce
  [ALIVE] (39/500) http://retracker01-msk-virt.corbina.net:80/announce 455ms — valid announce response
  [ALIVE] (40/500) https://tracker.qingwapt.org:443/announce 141ms — online (failure reason)
  [ALIVE] (41/500) udp://ipv4announce.sktorrent.eu:6969/announce 86ms — valid connect + announce
  [ALIVE] (42/500) http://tracker1.itzmx.com:8080/announce 428ms — valid announce response
  [ALIVE] (43/500) udp://open.ftorrent.com:443/announce 48ms — valid connect + announce
  [ALIVE] (44/500) http://tracker.dler.org:6969/announce 519ms — valid announce response
  [ALIVE] (45/500) https://tracker.nekomi.cn:443/announce 65ms — valid announce response
  [ALIVE] (46/500) http://107.189.2.131:1337/announce 790ms — valid announce response
  [ALIVE] (47/500) udp://mail.segso.net:6969/announce 115ms — valid connect + announce
  [ALIVE] (48/500) udp://explodie.org:6969/announce 80ms — valid connect + announce
  [ALIVE] (49/500) udp://martin-gebhardt.eu:25/announce 92ms — valid connect + announce
  [DEAD]  (50/500) udp://ipv6.govt.hu:6969/announce — no connect response
  [ALIVE] (52/500) udp://rekcart.duckdns.org:15480/announce 94ms — valid connect + announce
  [ALIVE] (53/500) udp://exodus.desync.com:6969/announce 73ms — valid connect + announce
  [ALIVE] (54/500) udp://open.stealth.si:80/announce 101ms — valid connect + announce
  [ALIVE] (55/500) udp://tracker.004430.xyz:1337/announce 21ms — valid connect + announce
  [ALIVE] (56/500) udp://seedpeer.net:6969/announce 76ms — valid connect + announce
  [ALIVE] (57/500) udp://retracker01-msk-virt.corbina.net:80/announce 132ms — valid connect + announce
  [ALIVE] (58/500) udp://tr3.ysagin.top:2715/announce 94ms — valid connect + announce
  [ALIVE] (59/500) https://tracker.zhuqiy.com:443/announce 208ms — valid announce response
  [ALIVE] (60/500) udp://tr4ck3r.duckdns.org:6969/announce 15ms — valid connect + announce
  [ALIVE] (61/500) udp://opentracker.lain.moscow:6969/announce 101ms — valid connect + announce
  [ALIVE] (62/500) udp://tracker.bittor.pw:1337/announce 27ms — valid connect + announce
  [ALIVE] (63/500) udp://tracker-udp.gbitt.info:80/announce 88ms — valid connect + announce
  [ALIVE] (64/500) udp://tracker.corpscorp.online:80/announce 26ms — valid connect + announce
  [ALIVE] (65/500) https://tracker.midnightprogrammer.net:443/announce 739ms — valid announce response
  [ALIVE] (66/500) udp://open.demonii.com:1337/announce 208ms — valid connect + announce
  [ALIVE] (67/500) udp://torrent.tracker.durukanbal.com:6969/announce 84ms — valid connect + announce
  [ALIVE] (68/500) udp://kolankoalastree.newtrackon.co.nz:1337/announce 210ms — valid connect + announce
  [ALIVE] (70/500) udp://tracker.ddunlimited.net:6969/announce 100ms — valid connect + announce
  [ALIVE] (71/500) udp://anime-tracker.aruku.kro.kr:8081/announce 184ms — valid connect + announce
  [ALIVE] (72/500) udp://tracker.ilibr.org:6969/announce 115ms — valid connect + announce
  [ALIVE] (73/500) udp://tracker.dler.com:6969/announce 188ms — valid connect + announce
  [ALIVE] (74/500) udp://tracker.opentrackr.org:1337/announce 85ms — valid connect + announce
  [ALIVE] (75/500) udp://tracker.dler.org:6969/announce 188ms — valid connect + announce
  [ALIVE] (76/500) udp://tracker.cn.nyaa.net:6969/announce 199ms — valid connect + announce
  [ALIVE] (77/500) udp://tracker.ducks.party:1984/announce 91ms — valid connect + announce
  [ALIVE] (78/500) udp://tracker.farted.net:6969/announce 106ms — valid connect + announce
  [ALIVE] (79/500) udp://tracker.qu.ax:6969/announce 84ms — valid connect + announce
  [ALIVE] (80/500) udp://tracker.nyaa.net:6969/announce 122ms — valid connect + announce
  [ALIVE] (81/500) udp://tracker.opentrackr.com:6969/announce 116ms — valid connect + announce
  [ALIVE] (82/500) udp://tracker.wildkat.net:6969/announce 18ms — valid connect + announce
  [ALIVE] (83/500) udp://tracker.gmi.gd:6969/announce 62ms — valid connect + announce
  [ALIVE] (84/500) http://tracker.waaa.moe:6969/announce 1541ms — valid announce response
  [ALIVE] (85/500) udp://tracker.peerfect.org:6969/announce 115ms — valid connect + announce
  [ALIVE] (86/500) udp://tracker.teambelgium.net:6969/announce 87ms — valid connect + announce
  [ALIVE] (87/500) udp://tracker.skynetcloud.site:6969/announce 88ms — valid connect + announce
  [ALIVE] (88/500) udp://tracker.aruku.ovh:8081/announce 236ms — valid connect + announce
  [ALIVE] (89/500) udp://tracker.torrents.observer:80/announce 90ms — valid connect + announce
  [ALIVE] (90/500) wss://tracker.openwebtorrent.com:443/announce 9ms — TLS reachable
  [ALIVE] (91/500) udp://tracker.playground.ru:6969/announce 126ms — valid connect + announce
  [ALIVE] (93/500) udp://tracker.k.vu:6969/announce 105ms — valid connect + announce
  [ALIVE] (94/500) udp://tracker.nyaa.vc:6969/announce 84ms — valid connect + announce
  [ALIVE] (96/500) udp://tracker2.dler.org:80/announce 188ms — valid connect + announce
  [ALIVE] (98/500) udp://tracker.willy.pro:6969/announce 251ms — valid connect + announce
  [DEAD]  (100/500) udp://tracker.yume-hatsuyuki.moe:6969/announce — no connect response
  [ALIVE] (102/500) udp://yuptracker-eu.gaijinent.com:27022/announce 72ms — valid connect + announce
  [ALIVE] (103/500) udp://t.overflow.biz:6969/announce 115ms — valid connect + announce
  [ALIVE] (105/500) http://t.overflow.biz:6969/announce 257ms — valid announce response
  [ALIVE] (107/500) udp://v2.iperson.xyz:6969/announce 256ms — valid connect + announce
  [ALIVE] (110/500) udp://tracker.torrent.eu.org:451/announce 94ms — valid connect + announce
  [ALIVE] (111/500) http://tracker.dhitechnical.com:6969/announce 4216ms — valid announce response
  [ALIVE] (113/500) http://bittorrent-tracker.e-n-c-r-y-p-t.net:1337/announce 467ms — valid announce response
  [DEAD]  (125/500) udp://tracker3.itzmx.com:6961/announce — no connect response
  [DEAD]  (150/500) http://109.71.253.37:1096/announce — URLError: <urlopen error timed out>
  [ALIVE] (152/500) https://pybittrack.retiolus.net:443/announce 14151ms — valid announce response
  [DEAD]  (175/500) http://113.17.153.206:6969/announce — URLError: <urlopen error timed out>
  [DEAD]  (200/500) http://116.8.90.235:6969/announce — URLError: <urlopen error timed out>
  [DEAD]  (225/500) http://116.9.207.121:6969/announce — URLError: <urlopen error timed out>
  [ALIVE] (236/500) http://135.125.198.235:2710/announce 183ms — valid announce response
  [ALIVE] (242/500) http://135.125.198.235:80/announce 181ms — valid announce response
  [DEAD]  (250/500) http://123.245.62.105:6969/announce — URLError: <urlopen error timed out>
  [ALIVE] (251/500) http://140.235.237.23:6969/announce 53ms — valid announce response
  [DEAD]  (275/500) http://13.115.115.32:6969/announce — URLError: <urlopen error timed out>
  [DEAD]  (300/500) http://167.235.245.209:80/announce — HTTPError: HTTP Error 404: Not Found
  [DEAD]  (325/500) http://152.249.214.74:6969/announce — URLError: <urlopen error timed out>
  [DEAD]  (350/500) http://177.112.215.4:6969/announce — URLError: <urlopen error timed out>
  [ALIVE] (358/500) http://177.188.141.75:6969/announce 230ms — valid announce response
  [DEAD]  (375/500) http://177.172.63.135:6969/announce — URLError: <urlopen error timed out>
  [ALIVE] (400/500) http://185.126.65.92:6969/announce 183ms — valid announce response
  [DEAD]  (425/500) http://187.11.72.188:6969/announce — URLError: <urlopen error [Errno 111] Connection refused>
  [DEAD]  (450/500) http://186.10.170.58:1337/announce — URLError: <urlopen error timed out>
  [DEAD]  (475/500) http://187.57.131.55:6969/announce — URLError: <urlopen error timed out>
  [DEAD]  (500/500) http://189.18.96.56:6969/announce — URLError: <urlopen error timed out>

[INFO] First pass done in 111.8s
[INFO] Second pass: re-testing top 97 alive trackers...
[INFO] Second pass done, refined 96 trackers

===== Test Summary =====
  Total tested:   500
  Alive (raw):    97
  Alive (final):  25 (top 25 by composite score)
  Score-capped:   72
  Unsafe filtered:0
  Dead final:     475
  Time:           127.0s
  Protocols:      {'http': 32, 'https': 13, 'udp': 51, 'wss': 1}
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
 Round 1 - 2026-09-29 06:30:40
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
  [PASS] Alive count check: 25 <= 25
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
 Round 1 - 2026-09-29 06:30:47
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
  [PASS] Alive count check: 25 <= 25
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
 Round 2 - 2026-09-29 06:30:52
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
  [PASS] Alive count check: 25 <= 25
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
 Round 3 - 2026-09-29 06:30:57
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
  [PASS] Alive count check: 25 <= 25
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
=== End of diagnostics (Tue Sep 29 06:30:57 UTC 2026) ===
