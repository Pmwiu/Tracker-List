# Design — Tracker Mechanism Optimization & Auto-Discovery

Date: 2026-10-13
Status: DRAFT (pending review)

## Intent and why

Tracker-List aggregates 14 whitelisted public BitTorrent tracker sources, performs
protocol-level liveness testing, scores by speed+stability+quality, and publishes
`best.txt` (25) / `all.txt` (59). The pipeline works but has gaps the user wants
closed in this change:

- **Filtering** is purely blacklist-based; doesn't reward cross-source agreement
- **Speed testing** is 2 samples per tracker; doesn't measure jitter
- **Liveness** only checks announce handshake; doesn't validate returned peer counts
- **Scoring** is single-dimension with 3 components; no degradation or trend signals
- **Selection** is single-objective sort; doesn't optimize for diversity
- **Discovery** is purely passive (curated SOURCES list); no active public-tracker finding

This change makes selection more discerning and adds an opt-in discovery pipeline that
surfaces candidate public trackers without polluting production.

## Goals

- Better signal: scoring reflects real-world reliability, not just handshake speed
- Diversity: best list covers protocols / ASNs / cold-seed scenarios, not just fastest 25
- New-tracker discovery: automatically find public trackers in the wild, surfaced for review
- **Zero new external dependencies** (project invariant — pure stdlib)
- **No behavior regression** for already-working trackers

## Non-goals (explicit out of scope)

- Active DHT crawling (BEP 5 Kademlia) — needs long-running process; deferred
- BitTorrent client emulation / real download speed — needs private seed; deferred
- Geographic / regional filtering — needs GeoIP DB; deferred
- Per-BT-client tuning — needs client config knowledge; deferred
- Changing public URLs / output file format

## Anti-goals (things that would be a failure even if technically working)

- Discovered trackers polluting `best.txt` / `all.txt` without human review
- Adding runtime overhead that breaks the 30-minute CI budget
- New trackers causing false alarms (failure issue spam)
- Breaking the existing `best ⊆ all` invariant or the `best ≤ 25 / all ≤ 59` caps

## Constraints

- Pure Python stdlib (no `requests`, no `bs4`, no `lxml`)
- CI timeout 30 min (current run uses ~1-2 min; new work must not push past 15 min)
- Candidate pool ≤ `MAX_CANDIDATES = 200`
- best ≤ `MAX_TRACKERS = 25`, all ≤ `MAX_ALL = 59`
- Non-UDP quota ≥ 4, classic quota ≥ 4
- Schedule: every 6h + manual + push-to-scripts trigger
- Windows / Linux / macOS runnable (pure stdlib implies this; confirm urllib behaves)

## What gets built

### Part A — existing mechanism optimizations

All changes are backward-compatible: existing files / public output unchanged unless
described below. Each item is independently revertible.

**A1. Cross-source agreement (filter + score)**
- During merge, count how many distinct sources each tracker appears in
- Pass counts to scoring via `reports/source_counts.json` (new file, gitignored-able
  but committed — it's small and useful for diagnostics)
- Add scoring dimension: `source_agreement_score` (0/30/70/100 for 1/2/3/4+ sources)
- Weight 10% of total score

**A2. Multi-sample speed test (测速)**
- Change from 2-pass top-100 to 3-sample median across top 50 (limit CI budget)
- Each sample = existing probe
- Final speed = median(samples); jitter = max - min
- Penalty: `speed_score *= max(0.7, 1 - jitter/median*0.3)` (caps at 30% reduction)

**A3. Peer count parsing (测活)**
- HTTP/HTTPS bencoded response: parse `peers` field byte-length → count (compact format)
- New quality dimension `peers_returned_score`: 0→60, 1-5→80, 6+→100
- For UDP: action 1 response body contains peer list; parse similarly
- Extends existing `QUALITY_SCORES` dict (not a new dimension — replaces "with peers" boolean)

**A4. Recent-run outcome rate (评分)**
- `test_state.json` already tracks `uptime_ema`; add `last_outcomes` (list of last 10 results)
- Each run appends the new outcome; trim to last 10
- New score dimension: `recent_success_rate = sum(last_outcomes) / len(last_outcomes) * 100`
- Weight 10% (steals from stability's 25%, not additive)
- Anti-degradation bonus: if last 3 outcomes are all 0, apply -5 to final score

**A5. Pareto / multi-objective selection (测优)**
- Score is already weighted multi-dim — keep that
- Add **ASN diversity penalty** in final selection: precompute per-tracker /16 (IPv4) or
  /48 (IPv6) via `socket.getaddrinfo` (cached). If top-25 has >3 from same /16,
  demote the lowest-scored one (push out of `picked` set)
- Add **cold-seed bias** in quota selection: in `select_top_with_quotas`, when
  picking classic/non-UDP quotas, prefer trackers with `uptime_ema >= 0.7` even if
  their composite score is lower than a faster but flakier alternative
- ASN cache: `trackers/cache/asn_cache.json` (gitignored, regenerated on demand by
  `dedup_same_asn` walking all live IPs; small, ~few KB)

**A6. IPv4/IPv6 dual-stack test (测活, optional)**
- In `test_one`: if hostname has both A and AAAA records, test both stacks
- Combined score = min(ipv4_score, ipv6_score) when both present; either single
- Output per-stack detail in `test_report.md`

### Part B — auto-discovery module

**B1. New script `scripts/discover_trackers.py`**
- Inputs: a list of "discovery sources" — URLs, GitHub topics, known public lists
- Outputs: `trackers/discovered/candidates_<UTC_date>.txt` (one URL per line, deduped
  against the 14 whitelisted sources and against past discoveries)
- No liveness test in this script — that's B2's job
- Stdlib only: `urllib`, `re`, `json`, `html.parser` for simple HTML extraction

**B2. Validation integration**
- `update_trackers.py` gets a new function: `load_discovered_candidates()` reads
  `trackers/discovered/candidates_*.txt` (latest 7 days), validates each URL
  (TRACKER_PATTERN + is_safe_tracker equivalent), merges into a synthetic
  `DISCOVERED_SOURCES` list
- These candidates join the merge pool (after whitelist sources) — they get tested
  alongside whitelisted ones
- They are scored identically and reported in `test_report.md` Discovery section,
  **but they do NOT enter `best.txt` / `all.txt` in Phase 1** — see anti-goals.
  Selection (`select_top_with_quotas`) only considers whitelisted-source trackers.
  Discovered trackers surface in the report only as "would-have-been-ranked-X"
  diagnostics, not as live subscriptions.
- The 200-candidate cap (existing `MAX_CANDIDATES`) protects against runaway growth

**B3. Promotion mechanism (option B: half-auto, require human review)**
- New file `trackers/discovered/promote_queue.json` tracks candidates that have
  survived N consecutive runs (default N=5)
- On each run, surviving candidates are appended to
  `trackers/discovered/PROMOTE.md` with their stats (alive count, avg score, sources)
- A separate workflow `monthly-check.yml` adds a step to open a GitHub Issue with
  PROMOTEs for the maintainer's review (similar to the existing auto-alert pattern)
- The auto-discovery **never directly modifies SOURCES** — promotion is human-driven

**B4. CI integration**
- New step in `.github/workflows/update-trackers.yml`: "Discover candidate trackers"
- Runs **before** `update_trackers.py` (so the same run's merge can include them)
- Catches failures with `continue-on-error: true` so a broken discovery doesn't break
  the main pipeline
- New diagnostic section appended to `docs/ci-diag.md` "Discovery" section

**B5. Discovery sources (initial)**
- GitHub topic search: `bt-tracker`, `public-tracker`, `tracker-list`
  (via `https://api.github.com/search/repositories?q=topic:bt-tracker&sort=updated`)
  - Per-repo fetch: `README.md` (default branch) + files whose name contains
    `tracker` and ends in `.txt` (e.g. `trackers.txt`, `trackers_best.txt`).
    Skip files > 100 KB to avoid pulling huge datasets. Per-repo cap: 10 files.
    Unauthenticated `api.github.com/search` is 10 req/min — fine for periodic runs.
- Known public lists' "all" files (currently NOT in SOURCES — wider net):
  ngosang/trackers_all_ip.txt, ngosang/trackers_all.txt,
  trackerslist.com/all.txt, etc.
- "Newly discovered" aggregator pages (manual list to start, can grow)
- Each source: a tuple in `DISCOVERY_SOURCES` (similar to `SOURCES`), whitelist-checked

## Key decisions (builder's call)

- Use `dataclasses` (Python 3.7+, stdlib) for the score-result struct
- `source_counts.json` lives in `reports/`, written by `update_trackers.py`,
  read by `test_trackers.py` — clean module boundary, no signature changes
- Discovery module uses `urllib.request` + a tiny HTML stripper (no bs4)
- ASN /16 cache: simplest possible — read once, regenerate when stale (>7 days)
- New scoring weights: 50% speed + 20% stability + 15% quality + 10% source-agreement
  + 5% recent-success (sum to 100, classic bonus +6 still additive).
  Anti-degradation penalty: if last 3 outcomes are all 0, apply -5 to final score
  (separate from the weighted sum).
- Discovery candidates default to a 7-day retention; older ones archived/moved

## What the builder has to figure out (in scope, but your call)

- Exact regex for "discovering" tracker URLs in free text (avoid URL fragments,
  markdown link syntax, etc.) — start permissive, validate with TRACKER_PATTERN
- Specific weighting constants in the new score formula (above are starting values)
- Whether to add ASN diversity as a score *dimension* or a *post-selection demotion*
  — design above says demotion; could be inverted if demotion is too aggressive
- Discovery source initial list (the user can curate over time)

## What the human partner has to decide (TBD)

- N for promotion queue (default 5)
- Whether discovered candidates that survive to best/all should be visibly marked
  in the output (e.g. comment line `# discovered by ...`) — **NO in Phase 1; they
  don't enter best/all at all**
- Daily-discovery vs. every-6h-discovery cadence (decision: every-6h, runs as part
  of the existing CI flow)

## Test strategy

- Project has no existing test framework — keep it that way per project convention
- Add a `scripts/_smoke.py` (private, not committed by default) with assert-heavy
  smoke tests for the new scoring functions
- The `health_check.py` pipeline remains the integration regression test
- New "Discovery" check added to `health_check.py`: when discovery ran, the
  candidates file is non-empty and well-formed
- All A1-A6 changes must keep existing checks PASS

## Out-of-scope reminders

- Don't change public URLs (`tracker.pmwiu.com/best.txt` etc.)
- Don't add third-party deps
- Don't add to SOURCES without explicit whitelist expansion
- Don't let discovered trackers directly enter best/all
- Don't break the `best ⊆ all` invariant (the new Alive-subset-of-all check is now real)

## Phasing

- **Phase 1 (this session):** All of Part A + Part B1/B2/B4 (core discovery).
  Skips B3 (promotion queue + monthly Issue) and B5 (curated discovery sources
  beyond GitHub topic search). Estimate: substantial; will commit by feature.
- **Phase 2 (future):** B3 promotion automation + expanded B5 source list.
- **Phase 3 (further future):** Active DHT crawler (BEP 5 Kademlia).

## Files to be added / changed

- `scripts/update_trackers.py` — cross-source count tracking, write `reports/source_counts.json`
- `scripts/test_trackers.py` — new score dimensions, multi-sample, peer count, dual-stack
- `scripts/health_check.py` — new "Discovery" check (if Part B enabled)
- `scripts/discover_trackers.py` — new file
- `.github/workflows/update-trackers.yml` — new "Discover" step
- `trackers/cache/asn_cache.json` — new file, gitignored, regenerated
- `trackers/discovered/` — new directory (gitkeep)
- `RUNBOOK.md` — update with new module, new scoring dimensions
- `CHANGELOG.md` — record the changes

## Open questions for builder

1. Should the score formula change be a single atomic edit, or staged (each
   dimension added independently and tested)? Staged is safer but slower.
2. Should the discovery module's URL extraction be permissive (catch all
   `udp://...`, `http://...` etc.) or strict (only well-formed)?
3. Should the discovered-candidates file be committed to the repo (so audit
   trail is visible) or gitignored (so it doesn't bloat history)?
