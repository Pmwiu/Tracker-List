# 转正建议（自动发现候选，人工 review 后加入 SOURCES）

达标线：连续存活 ≥ 5 轮。以下候选通过探活且稳定，建议评估转正。

更新时间：2026-10-16 04:46 UTC

| tracker | 连续存活轮数 | 最近评分 | 首次发现 |
|---|---|---|---|
| `udp://tr4ck3r.duckdns.org:6969/announce` | 6 | 65.6 | 2026-10-13 |
| `http://t.nyaatracker.com:80/announce` | 5 | 50.9 | 2026-10-13 |
| `http://t.overflow.biz:6969/announce` | 5 | 49.8 | 2026-10-13 |

转正方式：把选定 tracker 加入 `scripts/update_trackers.py` 的 SOURCES。
