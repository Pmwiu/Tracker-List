=== Diagnostics Tue Oct 13 08:45:45 UTC 2026 ===
Python: Python 3.12.15
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_best.txt
  HTTP 200, total 0.071797s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_best_ip.txt
  HTTP 200, total 0.067345s
>>> https://cf.trackerslist.com/best.txt
  HTTP 200, total 0.230579s
>>> https://tracker.adysec.com/trackers_best.txt
  HTTP 200, total 0.227326s
>>> https://raw.githubusercontent.com/gonghailink/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.119039s
>>> https://raw.githubusercontent.com/panda-men/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.116309s
>>> https://raw.githubusercontent.com/gspu/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.141334s
>>> https://raw.githubusercontent.com/linux-jin/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.280055s
>>> https://raw.githubusercontent.com/AlphaCatMeow/trackerslist/master/trackers_best.txt
  HTTP 200, total 0.139741s
>>> https://raw.githubusercontent.com/pexcn/daily/gh-pages/trackerlist/trackerlist-best.txt
  HTTP 200, total 0.150264s
>>> https://raw.githubusercontent.com/1265578519/OpenTracker/refs/heads/master/tracker.txt
  HTTP 200, total 0.140910s
>>> https://trackers.run/s/rw_ws_up_hp_hs_v4_v6.txt
  HTTP 200, total 0.671155s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_i2p.txt
  HTTP 200, total 0.084412s
>>> https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_yggdrasil.txt
  HTTP 200, total 0.071017s
[INFO] public list https://cf.trackerslist.com/all.txt: 121 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all.txt: 74 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ip.txt: 53 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_udp.txt: 46 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_http.txt: 17 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_https.txt: 11 urls
[INFO] public list https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ws.txt: 3 urls
[OK]   1336 new candidates -> candidates_20261013.txt
[OK]   1336 new candidates
[INFO] Repo: Pmwiu/Tracker-List, Max: 25
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/ngosang/trackerslist/master/blacklist.txt (391 URLs)
[INFO] Blacklist source loaded: https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/blacklist.txt (20 URLs)
[INFO] URL blacklist: 390 URLs (dynamic + remote sources)
Traceback (most recent call last):
  File "/home/runner/work/Tracker-List/Tracker-List/scripts/update_trackers.py", line 1238, in <module>
    main()
  File "/home/runner/work/Tracker-List/Tracker-List/scripts/update_trackers.py", line 1090, in main
    discovered_sources = load_discovered_candidates(
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Tracker-List/Tracker-List/scripts/update_trackers.py", line 632, in load_discovered_candidates
    host = (urllib.parse.urlparse(normalized).hostname or "").lower()
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/urllib/parse.py", line 395, in urlparse
    splitresult = urlsplit(url, scheme, allow_fragments)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/urllib/parse.py", line 514, in urlsplit
    raise ValueError("Invalid IPv6 URL")
ValueError: Invalid IPv6 URL
=== End of diagnostics (Tue Oct 13 08:45:55 UTC 2026) ===
