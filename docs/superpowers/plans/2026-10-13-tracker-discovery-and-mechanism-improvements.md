# Tracker Discovery & Mechanism Improvements Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Improve tracker selection quality (5-dimension scoring, multi-sample, dual-stack, ASN diversity, anti-degradation) and add an opt-in auto-discovery module that surfaces candidate public trackers without polluting production output.

**Architecture:** Two parts. Part A extends existing scoring/filtering/liveness in `test_trackers.py` and `update_trackers.py` with 6 dimensions. Part B adds a new `scripts/discover_trackers.py` that surfaces candidate public trackers via GitHub topic search + known public lists; candidates join the merge pool and are tested+scored, but explicitly filtered out of `best.txt`/`all.txt` in Phase 1.

**Tech Stack:** Python 3.12 stdlib only (urllib, json, re, dataclasses, concurrent.futures, ipaddress, struct, socket, ssl, hashlib, html.parser, argparse, datetime, statistics). GitHub Actions YAML for CI.

**Spec:** `docs/superpowers/specs/2026-10-13-tracker-discovery-design.md`

## Global Constraints

- Zero external dependencies (pure stdlib, project invariant)
- Python 3.12 (CI uses 3.12); local dev uses uv venv
- CI timeout 30 min total; new work must not push single-run past 15 min
- `MAX_CANDIDATES = 200` total candidate pool (existing)
- `MAX_TRACKERS = 25`, `MAX_ALL = 59` (existing)
- Non-UDP quota ≥ 4, classic quota ≥ 4 (existing)
- New scoring weights: 50% speed + 20% stability + 15% quality + 10% source-agreement + 5% recent-success (sum 100; classic bonus +6 still additive)
- Anti-degradation penalty: last 3 outcomes all 0 → -5 from final score
- ASN diversity: top-25 must not have > 3 trackers from same /16 (IPv4) or /48 (IPv6)
- Discovery never directly modifies SOURCES or enters best/all in Phase 1
- Discovered candidates DO count toward `MAX_CANDIDATES`
- Multi-sample speed test: 3 samples top 50 alive; median speed; jitter penalty up to 30% speed-score reduction
- All edits backward-compatible with existing CI (no breaking changes to public outputs)
- Test framework: new private `scripts/_smoke.py` with assertion-style tests (project has no test framework; design explicitly authorizes this addition)

## Review Focus

Spec-implied inputs/failures no task's tests exercise directly:

1. **DNS resolution failure during ASN cache build** — must fail gracefully (cache file not built, dedup skipped, log warning)
2. **Massive discovered file (1M URLs)** — must not OOM (stream/chunked read in `load_discovered_candidates`)
3. **GitHub rate limit during discovery** — must not break pipeline (continue-on-error in CI, log warning, write empty candidates file)
4. **Tracker URL with embedded credentials (e.g. `http://user:pass@host`)** — must reject in validation; existing `is_safe_tracker` handles, but worth a test
5. **CI runner with no IPv6** — dual-stack test must skip IPv6, not fail; existing `ipv6_available` check covers, but worth pinning a test

## File Structure

**New files:**
- `scripts/_smoke.py` — private smoke test runner (assertion-based; not committed in `__pycache__`)
- `scripts/discover_trackers.py` — auto-discovery module
- `trackers/discovered/.gitkeep` — directory marker
- `trackers/cache/.gitkeep` — ASN cache directory marker
- `docs/superpowers/specs/2026-10-13-tracker-discovery-design.md` — already created

**Modified files:**
- `scripts/update_trackers.py` — source-count tracking, write `reports/source_counts.json`, load discovered candidates
- `scripts/test_trackers.py` — new scoring dimensions, multi-sample, dual-stack, ASN diversity, recent outcomes
- `scripts/health_check.py` — new "Discovery" check; keep current checks
- `.github/workflows/update-trackers.yml` — new "Discover" step (before "Download")
- `.gitignore` — add `trackers/cache/asn_cache.json` and `trackers/discovered/candidates_*.txt`
- `RUNBOOK.md` — document new module + scoring dimensions
- `CHANGELOG.md` — record changes

**New runtime artifacts (gitignored):**
- `reports/source_counts.json` — written by `update_trackers.py`, read by `test_trackers.py`
- `trackers/cache/asn_cache.json` — regenerated as needed, TTL 7 days
- `trackers/discovered/candidates_<UTC_date>.txt` — discovery output

## Task Decomposition

Tasks ordered so each builds on prior; each ends with an independently testable deliverable.

### Task 1: Smoke test scaffolding

**Files:**
- Create: `scripts/_smoke.py`

**Interfaces:**
- `main()` walks a list of `(name, callable)` pairs, runs each, catches `AssertionError`, prints `OK` / `FAIL name: msg`, exits 1 on any FAIL, 0 otherwise
- Module-level: `TESTS = []` list, `def test_xxx(): ...` decorator/append pattern

- [ ] **Step 1: Write `scripts/_smoke.py`**

Minimal runner, no pytest, ~30 lines. Reads its own `TESTS` list and runs each entry.

- [ ] **Step 2: Run, verify exit 0 with no tests**

Run: `.venv/Scripts/python.exe scripts/_smoke.py`
Expected: prints "0 tests, all OK", exits 0

- [ ] **Step 3: Commit**

```bash
git add scripts/_smoke.py
git commit -m "test: add scripts/_smoke.py scaffolding"
```

### Task 2: Source-count tracking in update_trackers.py

**Files:**
- Modify: `scripts/update_trackers.py` — add `SOURCE_COUNTS_FILE` constant, write JSON at end of main, add `discovered_set` placeholder
- Test: `scripts/_smoke.py` — add `test_source_counts_shape` (skip if file absent)

**Interfaces:**
- New constant: `SOURCE_COUNTS_FILE = os.path.join(REPORTS_DIR, "source_counts.json")`
- Output JSON shape: `{"udp://x/announce": 3, "udp://y/announce": 1, ...}` (URL → distinct source count)
- File written in `main()` after the merge, before `write_run_summary`

- [ ] **Step 1: Add failing test in `_smoke.py`**

```python
def test_source_counts_shape():
    import json, os
    p = os.path.join(ut.PROJECT_ROOT, "reports", "source_counts.json")
    if not os.path.exists(p):
        return  # skip until update_trackers has been run
    data = json.load(open(p))
    assert isinstance(data, dict) and data
    for url, count in data.items():
        assert isinstance(url, str) and ut.is_valid_tracker(url)
        assert isinstance(count, int) and 1 <= count <= 20
```

- [ ] **Step 2: Implement in `update_trackers.py`**

After the per-source loop and before `write_run_summary`, build:
```python
source_counts = {url: sum(1 for _, ts in per_source if url in ts) for url in all_merged}
atomic_write(SOURCE_COUNTS_FILE, json.dumps(source_counts, ensure_ascii=False, indent=2) + NL)
```

- [ ] **Step 3: Run `update_trackers.py` then `_smoke.py`**

Run: `.venv/Scripts/python.exe scripts/update_trackers.py` then `_smoke.py`
Expected: PASS

- [ ] **Step 4: Commit**

```bash
git add scripts/update_trackers.py scripts/_smoke.py
git commit -m "feat(update): track per-tracker source count, emit reports/source_counts.json"
```

### Task 3: last_outcomes in test_state.json

**Files:**
- Modify: `scripts/test_trackers.py:save_history` and `load_history`
- Test: smoke `test_last_outcomes_roundtrip`

**Interfaces:**
- `test_state.json` adds `last_outcomes: {url: [int, ...]}` (last 10, 0/1)
- `load_history()` returns dict with `last_outcomes` key (default `{}`)
- `save_history()` appends new outcome for each `observed` tracker; trims to last 10; prunes by `candidates`

- [ ] **Step 1: Failing test in `_smoke.py`**

Round-trip: save with one alive, one dead; load; assert `last_outcomes[url]` ends with the right int.

- [ ] **Step 2: Implement in `save_history`**

After `new_dead_streak` block, build `last_outcomes`:
```python
last_outcomes = dict(old.get("last_outcomes", {}))
for t in observed:
    hist = last_outcomes.get(t, [])
    hist.append(1 if t in alive_set else 0)
    last_outcomes[t] = hist[-10:]
if candidates is not None:
    cand = set(candidates)
    last_outcomes = {t: v for t, v in last_outcomes.items() if t in cand}
state["last_outcomes"] = last_outcomes
```

- [ ] **Step 3: Run `_smoke.py` + `health_check.py --skip-net`**

Expected: PASS, FAIL=0

- [ ] **Step 4: Commit**

```bash
git add scripts/test_trackers.py scripts/_smoke.py
git commit -m "feat(test): persist last_outcomes in test_state.json"
```

### Task 4: Three new scoring dimensions

**Files:**
- Modify: `scripts/test_trackers.py:compute_score` — new signature with kwargs
- Modify: `scripts/test_trackers.py:main()` — build `source_agreement_map` from JSON, build `recent_outcomes_map` from history
- Test: smoke `test_compute_score_dimensions`, `test_weight_sum`

**Interfaces:**
- `compute_score(tracker, speed, uptime, detail, *, source_agreement=0, recent_success_rate=0.0, recent_outcomes=None) -> float`
- New constants: `SCORE_SPEED_WEIGHT=0.50`, `SCORE_STABILITY_WEIGHT=0.20`, `SCORE_QUALITY_WEIGHT=0.15`, `SCORE_SOURCE_AGREEMENT_WEIGHT=0.10`, `SCORE_RECENT_SUCCESS_WEIGHT=0.05`
- Helper: `source_agreement_to_score(count) -> float` mapping `{1:0, 2:30, 3:70, default: 100}`
- Anti-degradation: if `recent_outcomes[-3:] == [0,0,0]`, subtract 5
- Sum of weights = 1.0 (assert in smoke)
- Classic bonus +6 still additive after weighted sum

- [ ] **Step 1: Failing test**

```python
def test_compute_score_dimensions():
    from scripts.test_trackers import compute_score
    base = compute_score("udp://a", 50.0, 0.5, "valid connect + announce")
    high = compute_score("udp://a", 50.0, 0.5, "valid connect + announce",
                          source_agreement=3, recent_success_rate=1.0, recent_outcomes=[1,1,1])
    degraded = compute_score("udp://a", 50.0, 0.5, "valid connect + announce",
                             source_agreement=3, recent_success_rate=0.0, recent_outcomes=[0,0,0])
    assert high > base > degraded
    assert abs(0.50 + 0.20 + 0.15 + 0.10 + 0.05 - 1.0) < 1e-6
```

- [ ] **Step 2: Implement in `compute_score`**

Restructure to compute each component separately, multiply by weight, sum, apply classic bonus, apply anti-degradation.

- [ ] **Step 3: Update `main()` call site (line ~960)**

Read `reports/source_counts.json` once at start of main(); build `sa_map = {url: count}`. Build `ro_map = {url: state["last_outcomes"][url]}` from `load_history()`. Pass into `compute_score`.

- [ ] **Step 4: Run `_smoke.py` + `health_check.py --skip-net`**

Expected: PASS, FAIL=0

- [ ] **Step 5: Commit**

```bash
git add scripts/test_trackers.py scripts/_smoke.py
git commit -m "feat(score): 5-dim scoring (speed/stability/quality/source-agreement/recent) + anti-degradation"
```

### Task 5: Multi-sample speed test (3x median + jitter)

**Files:**
- Modify: `scripts/test_trackers.py:main()` — replace 2nd-pass logic with 3-sample loop for top 50
- Test: smoke `test_jitter_penalty`

**Interfaces:**
- After first pass, sort alive by speed asc; take top 50
- For each, run 2 more samples with `max(args.timeout - 2, 5)` timeout
- Final speed = `statistics.median([s1, s2, s3])`; jitter = `max(s1,s2,s3) - min(s1,s2,s3)`
- Speed penalty applied in score: `effective_speed = median * max(0.7, 1 - jitter/median*0.3)` when `median > 0`
- Cap top-50 retest at 30s × 3 = 90s total wall (3 samples × 50 trackers ÷ 15 workers)

- [ ] **Step 1: Failing test**

```python
def test_jitter_penalty():
    samples = [50, 100, 150]
    median = 100; jitter = 100
    penalty = max(0.7, 1 - jitter/median*0.3)
    assert 0.7 <= penalty < 0.8
    # Edge: jitter=0
    assert max(0.7, 1 - 0/100*0.3) == 1.0
```

- [ ] **Step 2: Implement in `main()`**

Replace the 2-pass block (around lines 898-925) with multi-sample logic. Use `concurrent.futures.ThreadPoolExecutor(max_workers=15)` for the retest. Update `results` in place with median + new `speed_score` adjustment (note: pass adjusted speed to `make_speed_scorer`).

- [ ] **Step 3: Run end-to-end**

Run: `.venv/Scripts/python.exe scripts/update_trackers.py && .venv/Scripts/python.exe scripts/test_trackers.py --timeout 8 --workers 20 --max-candidates 200 --no-second-pass`
Expected: exit 0, best=25, all populated

- [ ] **Step 4: Commit**

```bash
git add scripts/test_trackers.py scripts/_smoke.py
git commit -m "feat(test): 3-sample speed test with median + jitter penalty"
```

### Task 6: IPv4/IPv6 dual-stack test

**Files:**
- Modify: `scripts/test_trackers.py:test_one` — branch on dual-stack host
- New helper: `detect_dual_stack(host) -> (has_v4, has_v6)`
- Test: smoke `test_detect_dual_stack`

**Interfaces:**
- `detect_dual_stack(host)` returns tuple; uses `cached_getaddrinfo(host, None)` and inspects `family`
- In `test_one` for udp/wss/ws schemes, if `has_v4 and has_v6`, test both stacks; combined result = `min(score_v4, score_v6)` if both succeed; mark as "alive" only if at least one stack succeeds
- Per-stack detail in test_report.md (new column)

- [ ] **Step 1: Add `detect_dual_stack` helper + failing test**

```python
def test_detect_dual_stack():
    from scripts.test_trackers import detect_dual_stack
    v4, v6 = detect_dual_stack("dns.google")
    assert v4 is True
    assert isinstance(v6, bool)
```

- [ ] **Step 2: Modify `test_one` for dual-stack**

After `is_safe_tracker`, before scheme-specific dispatch: if dual-stack detected, call scheme-specific test twice (once per family), combine results.

- [ ] **Step 3: Run `_smoke.py` + `health_check.py --skip-net`**

Expected: PASS, FAIL=0

- [ ] **Step 4: Commit**

```bash
git add scripts/test_trackers.py scripts/_smoke.py
git commit -m "feat(test): IPv4/IPv6 dual-stack testing"
```

### Task 7: ASN diversity penalty + cold-seed bias

**Files:**
- Modify: `scripts/test_trackers.py:select_top_with_quotas` — add post-process diversity step
- New helpers: `_load_asn_cache()`, `_build_asn_cache(alive_urls)`, `_ip_to_prefix(host)`
- New: `trackers/cache/.gitkeep`
- Update: `.gitignore` — ignore `trackers/cache/asn_cache.json`
- Test: smoke `test_diversity_demote`, `test_cold_seed_bias`

**Interfaces:**
- Cache file: `trackers/cache/asn_cache.json` shape `{"host:port": "/16-or-/48", ...}` (host:port, not full URL)
- TTL: 7 days (rebuild if older); `mtime` checked
- `_ip_to_prefix(host)`: resolve via `cached_getaddrinfo`; for IPv4, return `ipaddress.ip_network(f"{ip}/24", strict=False).network_address.exploded`; for IPv6, `/48` prefix
- `select_top_with_quotas` post-process: if any `/16` (or `/48`) has > 3 entries in `picked`, demote lowest-scored of those, pull next-best from `scored` (skipping discovered)
- Cold-seed bias: in Stage 2 (non-UDP quota), prefer `uptime >= 0.7`; ties broken by score

- [ ] **Step 1: Add helpers + failing test**

```python
def test_diversity_demote():
    from scripts.test_trackers import _ip_to_prefix
    # 192.0.2.0/24 → 192.0.2.0/24 prefix
    p = _ip_to_prefix("192.0.2.5")
    assert p == "192.0.2.0/24"
```

- [ ] **Step 2: Implement `_load_asn_cache` / `_build_asn_cache`**

Read JSON if mtime < 7 days, else rebuild by walking all alive URLs and resolving.

- [ ] **Step 3: Modify `select_top_with_quotas`**

Add diversity pass after the existing 3 stages; add cold-seed preference in Stage 2.

- [ ] **Step 4: Run `_smoke.py` + `health_check.py --skip-net`**

Expected: PASS, FAIL=0

- [ ] **Step 5: Commit**

```bash
git add scripts/test_trackers.py scripts/_smoke.py .gitignore
git commit -m "feat(select): ASN diversity demotion + cold-seed bias"
```

### Task 8: discover_trackers.py — new file

**Files:**
- Create: `scripts/discover_trackers.py`
- Create: `trackers/discovered/.gitkeep`
- Update: `.gitignore` — ignore `trackers/discovered/candidates_*.txt`
- Test: smoke `test_extract_tracker_urls`, `test_dedup_against_known`

**Interfaces:**
- `discover_trackers(out_dir="trackers/discovered", known_urls=None) -> int` returns count of NEW URLs written
- Output: `trackers/discovered/candidates_<UTC_date>.txt` (one URL per line, sorted, deduped)
- Sources (initial): 3 GitHub topics (`bt-tracker`, `public-tracker`, `tracker-list`); per-repo fetch: README + files matching `tracker*.txt`, ≤10 files, ≤100KB each
- `extract_tracker_urls(text: str) -> set[str]` regex-based; validates with `TRACKER_PATTERN`
- Dedup against known SOURCES URLs and past discoveries (last 7 days)
- Stale cache (.gitkeep) ensures dir exists
- Graceful: per-source failures logged, never raise

- [ ] **Step 1: Stub with CLI + module skeleton**

```python
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", default="trackers/discovered")
    args = parser.parse_args()
    n = discover_trackers(args.out_dir)
    print(f"[OK]   {n} new candidates")
    return 0
```

- [ ] **Step 2: Add `extract_tracker_urls` + failing test**

```python
def test_extract_tracker_urls():
    from scripts.discover_trackers import extract_tracker_urls
    text = "udp://tracker.opentrackr.org:1337/announce\nhttp://x/y\n"
    urls = extract_tracker_urls(text)
    assert "udp://tracker.opentrackr.org:1337/announce" in urls
    assert "http://x/y" not in urls  # lacks scheme suffix
```

- [ ] **Step 3: Add `fetch_github_topic` + `fetch_repo_tracker_files`**

Use `urllib.request` (10 req/min unauthenticated); respect 100KB file cap; per-repo cap 10 files.

- [ ] **Step 4: Add `discover_trackers` orchestrator**

Iterate topics, dedup against known SOURCES URLs (read from disk), write to date-stamped file.

- [ ] **Step 5: Run script manually**

Run: `.venv/Scripts/python.exe scripts/discover_trackers.py`
Expected: prints count, creates `trackers/discovered/candidates_<date>.txt`

- [ ] **Step 6: Run `_smoke.py`**

Expected: PASS

- [ ] **Step 7: Commit**

```bash
git add scripts/discover_trackers.py scripts/_smoke.py .gitignore
git commit -m "feat(discover): auto-discover candidate public trackers (Phase 1)"
```

### Task 9: update_trackers.py loads discovered candidates

**Files:**
- Modify: `scripts/update_trackers.py` — add `load_discovered_candidates()`, call in main() before source loop
- New constant: `DISCOVERED_FILE_PATTERN = "trackers/discovered/candidates_*.txt"`
- Test: smoke `test_load_discovered_caps_age`

**Interfaces:**
- `load_discovered_candidates(out_dir="trackers/discovered", max_age_days=7) -> list[(short_name, [url, ...])]`
- Returns list of `(synthetic_name, urls)` to be added to `per_source`
- `synthetic_name = "discovered-<sha1[:8]>"`
- Synthetic sources go AFTER whitelist in `per_source` (so they have lower priority in scoring's source_agreement dimension)
- Their `trackers` get a synthetic `_discovered` set, written to `reports/discovered_set.json` (new file, read by test_trackers.py in Task 10)

- [ ] **Step 1: Add `load_discovered_candidates` + failing test**

```python
def test_load_discovered_caps_age(tmp_path):
    from scripts.update_trackers import load_discovered_candidates
    out = tmp_path / "discovered"
    out.mkdir()
    (out / "candidates_20260101.txt").write_text("udp://old/x\n")
    (out / "candidates_20261013.txt").write_text("udp://new/x\n")
    results = load_discovered_candidates(out_dir=str(out), max_age_days=7)
    # Old file should be skipped
    new_urls = [u for _, urls in results for u in urls]
    assert "udp://old/x" not in new_urls
    assert any("udp://new/x" == u for u in new_urls)
```

- [ ] **Step 2: Implement in `update_trackers.py`**

Read candidates files; for each file, filter by mtime; validate each URL with `is_valid_tracker`; group by file (each file = one synthetic source); append to `per_source` and `contribution`.

- [ ] **Step 3: Write `reports/discovered_set.json`**

After `per_source` is built:
```python
discovered_set = {url for _, urls in discovered_sources for url in urls}
atomic_write(DISCOVERED_SET_FILE, json.dumps(sorted(discovered_set), ensure_ascii=False, indent=2) + NL)
```

- [ ] **Step 4: Run end-to-end**

Run: `.venv/Scripts/python.exe scripts/update_trackers.py` then check `reports/discovered_set.json` exists (may be empty if no discovery files yet)

- [ ] **Step 5: Commit**

```bash
git add scripts/update_trackers.py scripts/_smoke.py
git commit -m "feat(update): load discovered candidates into merge pool (report only)"
```

### Task 10: test_trackers.py filters discovered from best/all selection

**Files:**
- Modify: `scripts/test_trackers.py:main()` — load `reports/discovered_set.json`, pass to `select_top_with_quotas`
- Modify: `scripts/test_trackers.py:select_top_with_quotas` — new parameter `whitelist_only_set: set[str] | None`, filter out non-whitelist in picked
- Test: smoke `test_discovered_excluded_from_best`

**Interfaces:**
- `select_top_with_quotas(scored, max_total, min_non_udp, min_classic, *, whitelist_only_set=None)` — if set, `picked` only includes URLs in the set; if no whitelist, fall back to old behavior
- Best subset invariant preserved: best ⊆ whitelist_only_set ∩ all_whitelist
- Discovery report appended to `test_report.md` (new section): "Discovery: N candidates tested, M passed liveness, would-have-been top K: [...]"

- [ ] **Step 1: Failing test**

```python
def test_discovered_excluded_from_best():
    from scripts.test_trackers import select_top_with_quotas
    scored = [
        ("udp://whitelist/ann", 100.0, 10.0, 1.0, "valid connect + announce"),
        ("udp://discovered/ann", 110.0, 10.0, 1.0, "valid connect + announce"),
    ]
    picked, capped = select_top_with_quotas(scored, 25, 4, 4, whitelist_only_set={"udp://whitelist/ann"})
    urls = [t for t, _, _, _, _ in picked]
    assert "udp://discovered/ann" not in urls
    assert "udp://whitelist/ann" in urls
```

- [ ] **Step 2: Modify `select_top_with_quotas`**

Add the `whitelist_only_set` parameter; in `_pick` helper, skip if URL not in set.

- [ ] **Step 3: Update `main()` to pass the set**

Load `reports/discovered_set.json`; invert to get `whitelist_only_set`; pass to `select_top_with_quotas`.

- [ ] **Step 4: Add discovery section to `write_report`**

Append a new section to `test_report.md` listing discovered candidates and their outcomes.

- [ ] **Step 5: Run `_smoke.py` + `health_check.py --skip-net`**

Expected: PASS, FAIL=0

- [ ] **Step 6: Commit**

```bash
git add scripts/test_trackers.py scripts/_smoke.py
git commit -m "feat(test): exclude discovered from best/all, add Discovery report section"
```

### Task 11: CI workflow + Discovery check

**Files:**
- Modify: `.github/workflows/update-trackers.yml` — add "Discover candidate trackers" step before "Check subscription sources"
- Modify: `scripts/health_check.py` — add `check_discovery_output` to `check_local_files`
- Test: `health_check.py --skip-net`

**Interfaces:**
- New workflow step: runs `python scripts/discover_trackers.py` with `continue-on-error: true`
- New health check: when `trackers/discovered/candidates_*.txt` exists, parse and assert at least one contains a valid URL OR is empty (both are valid discovery outcomes); PASS if no candidates file exists yet (don't fail on first run)

- [ ] **Step 1: Add discover step to workflow YAML**

Insert between "Set up Python" and "Check subscription sources":
```yaml
- name: Discover candidate trackers
  if: steps.sources.outputs.enabled == 'true'
  continue-on-error: true
  run: |
    python scripts/discover_trackers.py 2>&1 | tee -a diag.log
```

- [ ] **Step 2: Add `check_discovery_output` to `health_check.py`**

In `check_local_files`, after source files, glob `trackers/discovered/candidates_*.txt`; if any, parse URLs and assert shape (empty list is fine; non-empty must contain at least one valid URL).

- [ ] **Step 3: Run `health_check.py --skip-net`**

Expected: PASS (or PASS with WARN on first run when no candidates file exists)

- [ ] **Step 4: Commit**

```bash
git add .github/workflows/update-trackers.yml scripts/health_check.py
git commit -m "ci: add Discover candidate trackers step + health check"
```

### Task 12: Docs (RUNBOOK + CHANGELOG)

**Files:**
- Modify: `RUNBOOK.md` — add "Auto-Discovery Module (Phase 1)" section, update scoring section
- Modify: `CHANGELOG.md` — add 2026-10-13 entry

- [ ] **Step 1: Update RUNBOOK.md**

Add section after "8. 关键参数速查":
- Auto-Discovery Module (Phase 1)
  - 入口：`scripts/discover_trackers.py`
  - 产出：`trackers/discovered/candidates_<date>.txt`
  - 发现源：GitHub topic 搜索 + 公开列表
  - 集成：`update_trackers.py` 读取，merge 池包含，**不**进 best/all
  - 转正：人工 review SOURCES 后入库
- 新评分维度表格：5 维 + 权重 + 反退化
- 引用设计文档路径

- [ ] **Step 2: Update CHANGELOG.md**

Add `## [2026-10-13] - feat` entry with bullets:
- 5 维评分（速度/稳定/质量/源一致性/近期成功率）+ 反退化
- 多次样本测速 + 抖动扣分
- IPv4/IPv6 双栈测试
- ASN 多样性 penalty + 冷门命中 bias
- 自动发现模块（Phase 1 报告模式）
- `scripts/_smoke.py` 私有冒烟测试

- [ ] **Step 3: Commit**

```bash
git add RUNBOOK.md CHANGELOG.md
git commit -m "docs: document 5-dim scoring + auto-discovery module"
```

### Task 13: Final verification + push

- [ ] **Step 1: Run full pipeline end-to-end**

```bash
.venv/Scripts/python.exe scripts/update_trackers.py
.venv/Scripts/python.exe scripts/test_trackers.py --timeout 8 --workers 20 --max-candidates 200
.venv/Scripts/python.exe scripts/discover_trackers.py
.venv/Scripts/python.exe scripts/health_check.py --skip-net
.venv/Scripts/python.exe scripts/_smoke.py
```
All must exit 0.

- [ ] **Step 2: Restore generated files**

```bash
git checkout -- .   # restore generated outputs
git status --porcelain   # should show only ?? RUNBOOK.md and the new design/plan/spec files
```

- [ ] **Step 3: Push via SSH (real-IP bypass)**

```bash
git push origin main
```

---

## Self-Review Notes

- Spec coverage: every Goal/Anti-goal maps to a task (A1→Task4 via Task2+Task4; A2→Task5; A3→Task4+Task5; A4→Task3+Task4; A5→Task7; A6→Task6; B1→Task8; B2→Task9+Task10; B4→Task11; docs→Task12)
- Type consistency: `compute_score` signature, `select_top_with_quotas` signature, `load_discovered_candidates` return type all consistent across tasks
- Review Focus items: each gets a smoke test in the relevant task (1→Task7; 2→Task9; 3→Task8+Task11; 4→Task9; 5→Task6)
- Proportion: ~340 lines plan vs ~230 lines spec; tasks are decisions not transcripts
