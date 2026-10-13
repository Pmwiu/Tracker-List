#!/usr/bin/env python3
"""私有冒烟测试（断言式，无 pytest 依赖）。

用法：
  python scripts/_smoke.py

其他脚本通过 @test 装饰器注册测试函数。退出码：0 全部通过，1 有失败。
"""

import os
import sys

import update_trackers as ut

TESTS = []


def test(fn):
    """注册一个测试函数。"""
    TESTS.append((fn.__name__, fn))
    return fn


@test
def test_source_counts_shape():
    import json
    p = ut.SOURCE_COUNTS_FILE
    if not os.path.exists(p):
        return  # standalone 运行且尚未跑过 update_trackers 时跳过
    with open(p, encoding="utf-8") as f:
        data = json.load(f)
    assert isinstance(data, dict) and data
    for url, count in data.items():
        assert isinstance(url, str) and ut.is_valid_tracker(url)
        assert isinstance(count, int) and 1 <= count <= 20


@test
def test_last_outcomes_roundtrip():
    import json
    import shutil
    import test_trackers as tt
    state_path = os.path.join(ut.OUTPUT_DIR, "test_state.json")
    backup = None
    if os.path.exists(state_path):
        backup = state_path + ".smokebak"
        shutil.copy2(state_path, backup)
    try:
        # 全新一轮：1 alive + 1 dead + 1 未观察
        tt.save_history(
            alive_trackers=["udp://alive.example/announce"],
            dead_trackers=["udp://dead.example/announce"],
            candidates=["udp://alive.example/announce", "udp://dead.example/announce"],
        )
        st = tt.load_history()
        assert "last_outcomes" in st
        assert st["last_outcomes"]["udp://alive.example/announce"][-1] == 1
        assert st["last_outcomes"]["udp://dead.example/announce"][-1] == 0
        # 长度限制 10：连续调 12 次，alive 那条应 <=10
        for _ in range(12):
            tt.save_history(
                alive_trackers=["udp://alive.example/announce"],
                dead_trackers=[],
                candidates=["udp://alive.example/announce"],
            )
        st = tt.load_history()
        assert len(st["last_outcomes"]["udp://alive.example/announce"]) <= 10
        # candidates 裁剪：换 candidates 后，旧 url 应被剔除
        tt.save_history(
            alive_trackers=["udp://other.example/announce"],
            dead_trackers=[],
            candidates=["udp://other.example/announce"],
        )
        st = tt.load_history()
        assert "udp://alive.example/announce" not in st["last_outcomes"]
    finally:
        if backup:
            shutil.move(backup, state_path)


@test
def test_compute_score_dimensions():
    import test_trackers as tt
    # 0-维度基线（旧行为）
    base = tt.compute_score("udp://a", 50.0, 0.5, "valid connect + announce")
    # 3 源一致 + 近期全活：无反退化
    high = tt.compute_score("udp://a", 50.0, 0.5, "valid connect + announce",
                            source_agreement=3, recent_success_rate=1.0,
                            recent_outcomes=[1, 1, 1])
    # 3 源一致 + 近期全死：触发反退化 -5
    degraded = tt.compute_score("udp://a", 50.0, 0.5, "valid connect + announce",
                                source_agreement=3, recent_success_rate=0.0,
                                recent_outcomes=[0, 0, 0])
    # 关键性质：多源 + 近期健康的 tracker 显著高于其他场景
    assert high > base
    assert high > degraded
    # 反退化降低分数（与全活同源数对比）
    fully_alive = tt.compute_score("udp://a", 50.0, 0.5, "valid connect + announce",
                                   source_agreement=3, recent_success_rate=1.0,
                                   recent_outcomes=[1, 1, 1])
    assert degraded < fully_alive
    # 权重和 = 1.0
    w = (tt.SCORE_SPEED_WEIGHT + tt.SCORE_STABILITY_WEIGHT
         + tt.SCORE_QUALITY_WEIGHT + tt.SCORE_SOURCE_AGREEMENT_WEIGHT
         + tt.SCORE_RECENT_SUCCESS_WEIGHT)
    assert abs(w - 1.0) < 1e-6


@test
def test_source_agreement_mapping():
    import test_trackers as tt
    assert tt.source_agreement_to_score(1) == 0
    assert tt.source_agreement_to_score(2) == 30
    assert tt.source_agreement_to_score(3) == 70
    assert tt.source_agreement_to_score(4) == 100
    assert tt.source_agreement_to_score(10) == 100


@test
def test_jitter_penalty():
    import statistics
    import test_trackers as tt
    # 中位 + 抖动 → 期望 effective speed
    samples = [50, 100, 150]
    median = statistics.median(samples)
    assert median == 100
    # 抖动=100，median=100 → penalty = 1 - 100/100*0.3 = 0.7
    eff, pen = tt.multi_sample_refine(samples)
    assert pen == 0.7
    assert eff == 100 * 0.7
    # 抖动=0 → penalty=1.0
    eff, pen = tt.multi_sample_refine([80, 80, 80])
    assert pen == 1.0
    assert eff == 80
    # 样本不足时退回原值
    eff, pen = tt.multi_sample_refine([42])
    assert pen == 1.0
    assert eff == 42


@test
def test_detect_dual_stack():
    import test_trackers as tt
    # dns.google 同时有 A 和 AAAA 记录
    v4, v6 = tt.detect_dual_stack("dns.google")
    assert v4 is True
    assert isinstance(v6, bool)
    # 不存在的域名：两条都应为 False（不抛异常）
    v4n, v6n = tt.detect_dual_stack("definitely-does-not-exist-987654.invalid")
    assert v4n is False and v6n is False


@test
def test_ip_to_prefix():
    import test_trackers as tt
    # /24 for IPv4
    assert tt._ip_to_prefix("192.0.2.5") == "192.0.2.0/24"
    assert tt._ip_to_prefix("10.1.2.3") == "10.1.2.0/24"
    # /48 for IPv6
    assert tt._ip_to_prefix("2001:db8:1234:5678::1") == "2001:db8:1234::/48"
    # 无法解析的字符串原样返回
    assert tt._ip_to_prefix("not-an-ip") == "not-an-ip"


@test
def test_diversity_demote_basic():
    import test_trackers as tt
    # 4 个同 /24 + 1 个不同 /24：demote 后同 /24 至多 3
    cache = {
        "h1": "10.0.0.0/24", "h2": "10.0.0.0/24", "h3": "10.0.0.0/24", "h4": "10.0.0.0/24",
        "h5": "192.168.0.0/24",
    }
    picked = ["h1", "h2", "h3", "h4", "h5"]
    out = tt._enforce_asn_diversity(picked, cache, max_per_prefix=3)
    assert "h4" not in out
    assert out.count("h1") == 1 and out.count("h2") == 1 and out.count("h3") == 1
    assert "h5" in out
    assert len(out) == 4


@test
def test_cold_seed_bias_prefers_high_uptime():
    import test_trackers as tt
    # 3 个非 UDP，quota 至少 2；high-uptime 的 c 应当被选
    scored = [
        ("udp://a", 90, 10, 0.5, "valid connect + announce"),
        ("udp://b", 95, 10, 0.9, "valid connect + announce"),
        ("http://c", 80, 10, 0.95, "announce with peers"),
        ("https://d", 70, 10, 0.3, "announce with peers"),
        ("ws://e", 60, 10, 0.2, "TCP reachable"),
    ]
    picked, _ = tt.select_top_with_quotas(
        scored, max_total=5, min_non_udp=2, min_classic=0
    )
    urls = [t for t, *_ in picked]
    assert "http://c" in urls
    assert sum(1 for t in urls if not t.startswith("udp://")) >= 2


@test
def test_extract_tracker_urls():
    import discover_trackers as dt
    text = (
        "udp://tracker.opentrackr.org:1337/announce\n"
        "http://tracker.example.com:80/announce\n"
        "not a url\n"
        "udp://broken host/announce\n"  # 含空格，不应匹配
    )
    urls = dt.extract_tracker_urls(text)
    assert "udp://tracker.opentrackr.org:1337/announce" in urls
    assert "http://tracker.example.com:80/announce" in urls
    assert "not a url" not in urls
    # 重复应去重
    text2 = "udp://x/announce\nudp://x/announce\nudp://y/announce\n"
    urls2 = dt.extract_tracker_urls(text2)
    assert len(urls2) == 2


@test
def test_dedup_against_known():
    import discover_trackers as dt
    known = {"udp://known.example/announce"}
    fresh = {"udp://known.example/announce", "udp://new.example/announce"}
    out = dt.filter_known(fresh, known)
    assert out == {"udp://new.example/announce"}


@test
def test_load_discovered_caps_age():
    import shutil
    import tempfile
    import time as _time
    import update_trackers as ut
    tmp = tempfile.mkdtemp(prefix="discovered_test_")
    try:
        old_path = os.path.join(tmp, "candidates_20200101.txt")
        new_path = os.path.join(tmp, "candidates_20261013.txt")
        with open(old_path, "w", encoding="utf-8") as f:
            f.write("udp://old.example/announce\n")
        with open(new_path, "w", encoding="utf-8") as f:
            f.write("udp://new.example/announce\n")
        # 把 old 文件 mtime 设为 100 天前
        old_mtime = _time.time() - 100 * 86400
        os.utime(old_path, (old_mtime, old_mtime))
        results = ut.load_discovered_candidates(out_dir=tmp, max_age_days=7)
        new_urls = [u for _, urls in results for u in urls]
        # 100 天前的应被剔除
        assert not any("udp://old.example/announce" == u for u in new_urls)
        # 当天的应保留
        assert any("udp://new.example/announce" == u for u in new_urls)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


@test
def test_select_discovered_to_test():
    import test_trackers as tt
    merged = ["udp://in-merged.example/announce"]
    discovered = {
        "http://160.1.2.3:6969/announce",   # IP literal -> deprioritized
        "udp://good-domain.example.com/announce",  # domain -> prioritized
        "udp://in-merged.example/announce",        # already in merged -> excluded
        "http://8.8.8.8/announce",                 # IP literal
    }
    out = tt.select_discovered_to_test(discovered, merged, cap=2)
    # 域名优先，且 merged 内的被排除
    assert out[0] == "udp://good-domain.example.com/announce"
    assert "udp://in-merged.example/announce" not in out
    assert len(out) == 2  # cap
    # 空 discovered -> 空
    assert tt.select_discovered_to_test(set(), merged) == []


@test
def test_update_promote_queue():
    import test_trackers as tt
    now = "2026-10-14T00:00:00+00:00"
    q = {}
    # 首轮：2 个 discovered alive
    q = tt.update_promote_queue(q, {"udp://r1/announce": 88.5, "udp://r2/announce": 70.0},
                                set(), now)
    assert q["udp://r1/announce"]["alive_runs"] == 1
    assert q["udp://r1/announce"]["last_score"] == 88.5
    assert q["udp://r1/announce"]["first_seen"] == now
    # 第二轮：r1 继续活（runs=2），r2 死一次（dead_streak=1，保留）
    now2 = "2026-10-14T06:00:00+00:00"
    q = tt.update_promote_queue(q, {"udp://r1/announce": 90.0}, {"udp://r2/announce"}, now2)
    assert q["udp://r1/announce"]["alive_runs"] == 2
    assert q["udp://r2/announce"]["dead_streak"] == 1
    # 连续死 3 次 -> 剔除
    for i in range(3):
        q = tt.update_promote_queue(q, {}, {"udp://r2/announce"}, now2)
    assert "udp://r2/announce" not in q
    # 存活即清零 dead_streak
    q = tt.update_promote_queue(q, {"udp://r1/announce": 91.0}, set(), now2)
    assert q["udp://r1/announce"]["dead_streak"] == 0


@test
def test_render_promote_md():
    import test_trackers as tt
    q = {
        "udp://a/announce": {"alive_runs": 6, "last_score": 95.0,
                             "first_seen": "x", "last_seen": "y", "dead_streak": 0},
        "udp://b/announce": {"alive_runs": 2, "last_score": 99.0,
                             "first_seen": "x", "last_seen": "y", "dead_streak": 0},
    }
    md = tt.render_promote_md(q, threshold=5)
    assert "udp://a/announce" in md   # 达标
    assert "udp://b/announce" not in md  # 未达 5 轮
    # 按分数排序：a 在 b 之前（b 被过滤，只剩 a）
    assert md.index("udp://a/announce") < md.index("转正方式") or "udp://a" in md


@test
def test_fetch_public_lists_parses():
    import discover_trackers as dt
    fixture = {
        "https://a/all.txt": "udp://t1.example.com:6969/announce\n# comment\nhttp://t2.example.com/announce\n",
        "https://b/all.txt": "udp://t1.example.com:6969/announce\nnot a url\n",
    }
    orig = dt._http_get_text
    dt._http_get_text = lambda url, **kw: fixture[url]
    try:
        out = dt.fetch_public_lists(urls=list(fixture.keys()))
        # 去重 + 过滤非法 + normalize（http 补默认端口 80）
        assert out == {"udp://t1.example.com:6969/announce",
                       "http://t2.example.com:80/announce"}
    finally:
        dt._http_get_text = orig


@test
def test_fetch_public_lists_all_fail_graceful():
    import discover_trackers as dt
    orig = dt._http_get_text
    def boom(url, **kw):
        raise RuntimeError("network down")
    dt._http_get_text = boom
    try:
        out = dt.fetch_public_lists(urls=["https://x/all.txt", "https://y/all.txt"])
        assert out == set()  # 全部失败也不抛异常
    finally:
        dt._http_get_text = orig


@test
def test_select_reserve():
    import test_trackers as tt
    # discovered alive 按评分降序取前 cap；白名单条目绝不进备选
    pool = [
        ("udp://d1/announce", 90.0, 10.0, 0.9, "valid connect + announce"),
        ("udp://w1/announce", 95.0, 10.0, 0.9, "valid connect + announce"),  # whitelist
        ("udp://d2/announce", 80.0, 10.0, 0.9, "valid connect + announce"),
        ("udp://d3/announce", 70.0, 10.0, 0.9, "valid connect + announce"),
    ]
    discovered = {"udp://d1/announce", "udp://d2/announce", "udp://d3/announce"}
    out = tt.select_reserve(pool, discovered, cap=2)
    assert out == ["udp://d1/announce", "udp://d2/announce"]
    # discovered 为空 -> 空备选
    assert tt.select_reserve(pool, set(), cap=2) == []


@test
def test_build_reserve_from_alive_discovered():
    import test_trackers as tt
    # results 含 discovered：1 alive 但慢(6s)，1 alive 快，1 dead；whitelist 一条
    results = [
        ("udp://slow-disc/announce", "alive", "valid connect + announce", 6000.0),
        ("udp://fast-disc/announce", "alive", "valid connect + announce", 100.0),
        ("udp://dead-disc/announce", "dead", "timeout", 0.0),
        ("udp://whitelist/announce", "alive", "valid connect + announce", 90.0),
    ]
    discovered = {"udp://slow-disc/announce", "udp://fast-disc/announce",
                  "udp://dead-disc/announce"}
    out = tt.build_reserve(results, discovered, {}, {}, {}, cap=20)
    # alive discovered 都进备选（含慢的，备选库不套用 best/all 的低速淘汰）
    assert "udp://fast-disc/announce" in out
    assert "udp://slow-disc/announce" in out
    assert "udp://dead-disc/announce" not in out
    assert "udp://whitelist/announce" not in out
    # 评分降序：快的在前
    assert out[0] == "udp://fast-disc/announce"


@test
def test_dedup_same_host():
    import test_trackers as tt
    # host key：小写 + 去 www. 前缀
    assert tt._host_key("udp://WWW.Example.COM:1337/announce") == "example.com"
    assert tt._host_key("not a url") is None
    # 同域名（跨端口/跨协议）只保留最快
    entries = [
        ("udp://a.example.com:1337/announce", "d", 50.0),
        ("udp://a.example.com:6969/announce", "d", 80.0),
        ("http://www.a.example.com/announce", "d", 60.0),
        ("udp://b.other.com/announce", "d", 70.0),
    ]
    removed = tt.dedup_by_groups(entries, tt._host_key)
    assert removed == {"udp://a.example.com:6969/announce",
                       "http://www.a.example.com/announce"}


@test
def test_peers_and_scrape_signals():
    import test_trackers as tt
    # announce peers 计数（compact IPv4 6 字节/peer，IPv6 18 字节/peer）
    decoded = {b'peers': b'x' * 24, b'peers6': b'y' * 36, b'interval': 1800}
    assert tt.count_announce_peers(decoded) == 4 + 2
    assert tt.count_announce_peers({b'peers': b''}) == 0
    # scrape 种子数解析（bencoded files dict，容忍截断流）
    data = (b'd5:filesd20:' + b'0' * 20 + b'd8:completei123e10:downloadedi9e'
            b'10:incompletei5eeee' + b'8:completei77e')
    assert tt.parse_scrape_seeders(data) == 123 + 77
    assert tt.parse_scrape_seeders(b'd8:intervali60ee') == 0
    # quality：scrape 高热度可拉满
    assert tt.quality_score('announce without peers') == 90
    assert tt.quality_score('announce with peers:1') == 95
    assert tt.quality_score('announce with peers:5') == 100
    assert tt.quality_score('announce without peers', scrape_seeders=150) == 100
    assert tt.quality_score('announce without peers', scrape_seeders=5) == 95
    assert tt.quality_score('valid connect + announce', scrape_seeders=0) == 100
    # compute_score 接受 scrape kwarg
    s_hi = tt.compute_score("udp://a", 50.0, 0.5, "announce without peers",
                            scrape_seeders=200)
    s_lo = tt.compute_score("udp://a", 50.0, 0.5, "announce without peers")
    assert s_hi > s_lo


@test
def test_append_discovered_sources_no_nameerror():
    import update_trackers as ut
    per_source = [("ngosang-best", ["udp://a/announce"])]
    results = [("trackers_ngosang_best.txt", 1)]
    contribution = {}
    disc = [("discovered-abcd1234", ["udp://new1/announce", "udp://a/announce"])]
    ut.append_discovered_sources(per_source, results, contribution, disc)
    assert ("discovered-abcd1234", ["udp://new1/announce", "udp://a/announce"]) in per_source
    assert contribution["discovered-abcd1234"] == 2
    # 不污染首页统计（results 不追加 discovered 行）
    assert len(results) == 1


@test
def test_discovered_excluded_from_best():
    import test_trackers as tt
    scored = [
        ("udp://whitelist/ann", 100.0, 10.0, 1.0, "valid connect + announce"),
        ("udp://discovered/ann", 110.0, 10.0, 1.0, "valid connect + announce"),
    ]
    picked, capped = tt.select_top_with_quotas(
        scored, 25, 4, 4, whitelist_only_set={"udp://whitelist/ann"})
    urls = [t for t, *_ in picked]
    assert "udp://discovered/ann" not in urls
    assert "udp://whitelist/ann" in urls
    # capped 里应含被排除的 discovered
    capped_urls = [t for t, *_ in capped]
    assert "udp://discovered/ann" in capped_urls


def main():
    failed = 0
    for name, fn in TESTS:
        try:
            fn()
        except Exception as e:  # 断言失败与意外异常都算 FAIL，逐条继续
            print(f"FAIL {name}: {type(e).__name__}: {e}")
            failed += 1
        else:
            print(f"OK   {name}")
    total = len(TESTS)
    if failed:
        print(f"{failed}/{total} failed")
        return 1
    print(f"{total} tests, all OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
