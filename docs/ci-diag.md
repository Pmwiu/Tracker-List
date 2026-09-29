=== Diagnostics Tue Sep 29 04:55:02 UTC 2026 ===
Python: Python 3.12.14
PWD: /home/runner/work/Tracker-List/Tracker-List
--- Test file lock (fcntl) ---
lock OK
--- Test source connectivity ---
>>> https://cf.trackerslist.com/all.txt
  HTTP 200, total 0.233361s
>>> https://raw.githubusercontent.com/adysec/tracker/main/trackers_all.txt
  HTTP 200, total 0.190261s
>>> https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt
  HTTP 200, total 0.039040s
  File "/home/runner/work/Tracker-List/Tracker-List/scripts/update_trackers.py", line 371
    return " &middot;
           ^
SyntaxError: unterminated string literal (detected at line 371)
=== End of diagnostics (Tue Sep 29 04:55:03 UTC 2026) ===
