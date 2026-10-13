# Tracker Reserve Pool & Discovery Enhancement (Phase 2) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: superpowers:executing-plans (inline). Steps use checkbox syntax.

**Goal:** Strengthen active/clean/stable/classic/excellent/open tracker evaluation (peers count, scrape popularity, same-domain dedup), publish an evaluated reserve pool (备选库), expand discovery sources, and add a human-review promotion queue.

**Architecture:** All changes extend the existing pipeline. Peers/scrape signals fold into the existing quality dimension (no weight changes). Reserve pool is a new output derived from discovered candidates that pass liveness+scoring. Promotion queue persists survivor stats across runs.

**Tech Stack:** Python 3.12 stdlib (urllib, bencode already present, struct for UDP scrape).

**Spec:** `docs/superpowers/specs/2026-10-13-tracker-discovery-design.md` (Phase 2 sections B3/B5 + this plan's research addendum below)

## Research Addendum (2026-10-14, from international projects)

- **ngosang/trackerslist**: "Trackers are sorted by popularity and latency"; "Trackers with the same domain or pointing to the same IP address are removed"; bot checks daily. → adopt scrape popularity + same-domain dedup.
- **XIU2/TrackersListCollection**: best=70/all=121 daily; `cf.trackerslist.com/all.txt` is a large open pool. → adopt as discovery source.
- Our repo already encodes: full-announce liveness (ngosang/XIU2 standard), low-speed cut, /24 dedup, URL blacklist.

## Global Constraints

(inherited from Phase 1 plan) pure stdlib; CI ≤30min; MAX_CANDIDATES=200; best≤25/all≤59; quotas; discovered excluded from best/all; no secrets; ASCII-safe prints for Windows console; weights unchanged (50/20/15/10/5 + classic +6).

New: reserve pool ≤ 20 entries; reserve never auto-enters best/all (promotion is human, via PROMOTE.md).

## Tasks

### Task P2-1: peers count + scrape popularity (测活/测优)

**Files:** Modify `scripts/test_trackers.py` (test_http, test_udp, new scrape_probe, quality_score); tests in `scripts/_smoke.py`.

**Interfaces:**
- `test_http` detail becomes `announce with peers:N` (N = len(peers)/6 + len(peers6)/18) or `announce without peers` when N=0.
- `scrape_probe(tracker_url, timeout) -> (ok: bool, seeders: int, elapsed_ms: float)`:
  - http/https: replace trailing `/announce` with `/scrape` (or append `/scrape` if path ends with `/`), GET, read ≤64KB, bdecode, sum `files.*.complete` over first 50 entries. 404/HTML/unparseable → (False, 0, elapsed).
  - udp: skip (announce peers signal suffices). wss/ws: skip.
- `quality_score(detail)` extended: `announce with peers:N` → N≥3:100, 1-2:95, else 90 (as today); plus new arg `scrape_seeders=None` → tier bonus folded: None→no change; 0→90; 1-9→95; 10-99→98; ≥100→100. Final quality = max(announce_tier, scrape_tier) when scrape available.
- main(): after alive determination, run scrape_probe concurrently (workers=15) for alive http/https trackers only; store `scrape_map`; pass seeders into quality via compute_score kwargs (`scrape_seeders=None` default).
- Smoke tests: `test_parse_announce_peers`, `test_scrape_tier`, `test_quality_with_scrape`.

### Task P2-2: same-domain dedup (筛选)

**Files:** Modify `scripts/test_trackers.py:dedup_same_ip` → also group by hostname (strip `www.`); keep fastest per host group AND per /24 group (union of removals).
**Smoke:** `test_dedup_same_host` with mock cache (multi-port same host → 1 kept).

### Task P2-3: reserve pool output (备选库)

**Files:** Modify `scripts/test_trackers.py:main()` (write `trackers/trackers_reserve.txt` ≤20 from discovered∩alive sorted by score); `scripts/update_trackers.py:sync_plain_text_files` (mapping reserve.txt); `cloudflare/tracker-proxy.js` (ALIASES reserve.txt); `scripts/health_check.py` (TRACKER_FILES + PLAIN_TEXT_FILES + CONSISTENCY_MAP + reserve count check ≤20); `scripts/update_trackers.py:write_mirrors_file` (block).
**Smoke:** `test_reserve_selection` (pure function `select_reserve(discovered_alive_scored, cap=20)`).

### Task P2-4: discovery sources expansion (B5)

**Files:** Modify `scripts/discover_trackers.py`: add `PUBLIC_ALL_LISTS = [urls]` fetched as plain text (cf.trackerslist.com/all.txt, ngosall via jsdelivr, trackers.run all list, adysec all if exists); cap 6 requests; failures logged+skipped.
**Smoke:** `test_public_lists_parsing` (fixture text).

### Task P2-5: promotion queue (B3)

**Files:** New `reports/promote_queue.json` written by test_trackers.py: for each reserve candidate, `{alive_runs+1 if alive else 0, last_score, first_seen, last_seen}`; `trackers/discovered/PROMOTE.md` regenerated listing alive_runs≥5 sorted by score with stats line. `.gitignore` NOT (PROMOTE.md committed; promote_queue.json committed too — small, audit trail).
**Smoke:** `test_promote_queue_update` with temp files.

### Task P2-6: docs + final verify + push

RUNBOOK (reserve pool section, promotion queue, new signals), CHANGELOG entry, full local gate (smoke + health --skip-net + test_trackers --no-second-pass e2e), push, verify CI green via run-page fetch.

## Review Focus

1. Scrape endpoint disabled/huge response on some trackers → capped read + timeout, never crash.
2. Bencode parse of malformed scrape body → caught, treated as no-signal.
3. Reserve pool must never overlap best/all (disjoint by whitelist filter).
4. Same-domain dedup must not collapse distinct hosts sharing a CDN IP beyond /24 rule (host rule is stricter but per-host only).
5. promote_queue growth bounded (prune URLs absent from candidates >30 days).
