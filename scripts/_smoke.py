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
def test_dynamic_blacklist_skips_protected():
    import os
    import tempfile
    import test_trackers as tt
    dead = {"udp://tracker.opentrackr.org:1337/announce": 25,   # 经典受保护
            "udp://random-bad.example.com:6969/announce": 25,   # 普通坏 tracker
            "udp://lone.example.com:6969/announce": 3}          # 未达阈值
    tmp = os.path.join(tempfile.mkdtemp(), "bl.txt")
    urls = tt.write_dynamic_blacklist(dead, threshold=20, path=tmp)
    assert "udp://tracker.opentrackr.org:1337/announce" not in urls  # 防误杀
    assert "udp://random-bad.example.com:6969/announce" in urls
    assert "udp://lone.example.com:6969/announce" not in urls        # 未达阈值


@test
def test_is_blacklisted_protected():
    import update_trackers as ut
    domain = {"evil.com", "tracker.opentrackr.org"}   # 某经典主机也在域名黑名单里（测防误杀）
    urls = {"udp://urlbad.example.com:6969/announce"}
    protected = {"tracker.opentrackr.org"}
    # 域名命中但受保护 -> 不杀
    assert not ut.is_blacklisted("udp://tracker.opentrackr.org:1337/announce",
                                 domain, urls, protected)
    # 域名命中且不受保护 -> 杀
    assert ut.is_blacklisted("udp://evil.com:6969/announce", domain, urls, protected)
    # URL 级精确命中 -> 即便主机受保护也杀
    assert ut.is_blacklisted("udp://urlbad.example.com:6969/announce", domain, urls, protected)
    # 正常 -> 不杀
    assert not ut.is_blacklisted("udp://good.example.com:6969/announce", domain, urls, protected)
    # 畸形 IPv6（urlparse 抛错）-> 不崩、不误杀
    assert not ut.is_blacklisted("udp://[::1:6969/announce", domain, urls, protected)


@test
def test_build_blacklists_dedup_and_protected():
    import update_trackers as ut
    orig = (ut.load_blacklist, ut.load_url_blacklist, ut.fetch_remote_blacklist)
    ut.load_blacklist = lambda: {"evil.com", "tracker.opentrackr.org"}
    ut.load_url_blacklist = lambda: {"udp://dyn.example.com:6969/announce"}
    ut.fetch_remote_blacklist = lambda: {"udp://dyn.example.com:6969/announce",
                                         "udp://rem.example.com/announce"}
    try:
        source_counts = {"udp://popular.example.com/announce": 4,
                         "udp://lone.example.com/announce": 1}
        domain, urls, protected = ut.build_blacklists(source_counts)
        assert domain == {"evil.com", "tracker.opentrackr.org"}
        # 动态+远程重叠的 URL 去重
        assert urls == {"udp://dyn.example.com:6969/announce", "udp://rem.example.com/announce"}
        # 保护集 = 经典主机 ∪ 跨源一致性>=3
        assert "tracker.opentrackr.org" in protected   # 经典
        assert "popular.example.com" in protected       # agreement 4
        assert "lone.example.com" not in protected      # agreement 1
    finally:
        (ut.load_blacklist, ut.load_url_blacklist,
         ut.fetch_remote_blacklist) = orig


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
        # 纯形状校验（不与演进中的严格 validator 绑定，避免旧 artifact 误报）
        assert isinstance(url, str) and "://" in url
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
    text2 = "udp://a.example.com/announce\nudp://a.example.com/announce\nudp://b.example.com/announce\n"
    urls2 = dt.extract_tracker_urls(text2)
    assert len(urls2) == 2
    # 畸形 IPv6（[ 无匹配 ]）被拒绝，不写入候选
    text3 = "udp://[::1:6969/announce\nudp://good.example.com:6969/announce\n"
    urls3 = dt.extract_tracker_urls(text3)
    assert urls3 == {"udp://good.example.com:6969/announce"}, urls3


@test
def test_dedup_against_known():
    import discover_trackers as dt
    known = {"udp://known.example/announce"}
    fresh = {"udp://known.example/announce", "udp://new.example/announce"}
    out = dt.filter_known(fresh, known)
    assert out == {"udp://new.example/announce"}


@test
def test_is_well_formed_tracker_rejects_odd():
    import update_trackers as ut
    # 合法但"写法奇特"的形态必须被拒（当前宽松正则会放过）
    odd = [
        "udp://[::1]:6969/announce",                       # IPv6 字面量
        "http://[2605:6400:30::1]:1337/announce",          # IPv6 字面量
        "udp://1.2.3.4:6969/announce?key=1",               # query
        "http://tracker.example.com/announce#frag",        # fragment
        "http://tracker.example.com/a%20b",                # 百分号编码
        "UDP://tracker.example.com/announce",              # 大写 scheme
        "http://tracker.example.com//announce",            # 双斜杠
        "http://tracker:80/announce",                      # 单标签无点
        "http://tracker.example.com:99999/announce",       # 端口越界
    ]
    for u in odd:
        assert not ut.is_well_formed_tracker(u), f"should reject: {u}"
    # 正常形态必须保留
    ok = [
        "udp://tracker.example.com:6969/announce",
        "http://1.2.3.4:80/announce",                      # IPv4 字面量常见，保留
        "wss://tracker.example.com/announce",
        "https://tracker.example.com:443/announce",
        "udp://open.stealth.si:80/announce",
    ]
    for u in ok:
        assert ut.is_well_formed_tracker(u), f"should accept: {u}"
    # is_valid_tracker 现在必须与严格校验一致（拒绝畸形 IPv6）
    assert not ut.is_valid_tracker("udp://[::1:6969/announce")


@test
def test_load_discovered_handles_malformed_ipv6():
    import os, shutil, tempfile
    import update_trackers as ut
    tmp = tempfile.mkdtemp(prefix="disc_v6_")
    try:
        p = os.path.join(tmp, "candidates_20261013.txt")
        # 畸形 IPv6（[ 无匹配 ]）能过 is_valid_tracker 正则，但 urlparse 会抛 ValueError
        with open(p, "w", encoding="utf-8") as f:
            f.write("udp://[::1:6969/announce\n"
                    "udp://good.example.com:6969/announce\n")
        # 不应抛异常；坏行被跳过，好行保留
        res = ut.load_discovered_candidates(out_dir=tmp, blacklist=set(), url_blacklist=set())
        urls = [u for _, us in res for u in us]
        assert urls == ["udp://good.example.com:6969/announce"], urls
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


@test
def test_load_discovered_filters_blacklist():
    import os, shutil, tempfile
    import update_trackers as ut
    tmp = tempfile.mkdtemp(prefix="disc_bl_")
    try:
        p = os.path.join(tmp, "candidates_20261013.txt")
        with open(p, "w", encoding="utf-8") as f:
            f.write("udp://good.example.com:6969/announce\n"
                    "udp://evil.example.net:6969/announce\n"
                    "http://urlbl.example.org/announce\n")
        # evil.example.net 域名黑名单；urlbl URL 精确黑名单（normalize 后带 :80）
        res = ut.load_discovered_candidates(
            out_dir=tmp,
            blacklist={"evil.example.net"},
            url_blacklist={"http://urlbl.example.org:80/announce"})
        urls = [u for _, us in res for u in us]
        assert urls == ["udp://good.example.com:6969/announce"], urls
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


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
def test_select_discovered_rotation():
    import test_trackers as tt
    # 轮换：最近测过的应排后，优先测最久未测/从未测的
    discovered = {"udp://a.example.com/announce",
                  "udp://b.example.com/announce",
                  "udp://c.example.com/announce"}
    merged = []
    tested_state = {
        "udp://a.example.com/announce": "2026-10-13T00:00:00+00:00",  # 刚测过
        "udp://b.example.com/announce": "2026-10-10T00:00:00+00:00",  # 很久前
        # c 从未测过
    }
    out = tt.select_discovered_to_test(discovered, merged, cap=2,
                                       tested_state=tested_state)
    # 从未测的 c 最优先，其次最久未测的 b；刚测过的 a 排最后（被 cap 截断）
    assert out[0] == "udp://c.example.com/announce", out
    assert out[1] == "udp://b.example.com/announce", out
    assert "udp://a.example.com/announce" not in out
    # 无 tested_state 时退回域名优先（向后兼容旧测试）
    out2 = tt.select_discovered_to_test(discovered, merged, cap=3)
    assert len(out2) == 3


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
def test_dual_stack_no_redundant_fallback():
    import socket
    import test_trackers as tt
    # v4-only dead udp tracker must be probed exactly once (no double-test fallback)
    calls = {"udp": 0}
    orig = (tt.is_safe_tracker, tt.detect_dual_stack, tt.cached_getaddrinfo, tt.test_udp)
    def fake_safe(t): return True, "safe"
    def fake_dual(host): return True, False  # v4 only
    def fake_gai(host, port): return [(socket.AF_INET, 1, 6, '', ('1.2.3.4', 0))]
    def fake_udp(ip, port, timeout, **kw):
        calls["udp"] += 1
        return False, 1.0, 'no connect response'
    tt.is_safe_tracker = fake_safe
    tt.detect_dual_stack = fake_dual
    tt.cached_getaddrinfo = fake_gai
    tt.test_udp = fake_udp
    try:
        tracker, status, detail, _ = tt.test_one("udp://x.example.org:6969/announce", 5)
        assert status == 'dead', status
        assert calls["udp"] == 1, f"test_udp called {calls['udp']}x (expected 1)"
    finally:
        (tt.is_safe_tracker, tt.detect_dual_stack,
         tt.cached_getaddrinfo, tt.test_udp) = orig


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
    scored = tt.build_reserve(results, discovered, {}, {}, {})
    # 返回 [(tracker, score)]，含所有 alive discovered（慢的也在）
    pairs = dict(scored)
    assert "udp://fast-disc/announce" in pairs
    assert "udp://slow-disc/announce" in pairs   # 备选库不套用 best/all 的低速淘汰
    assert "udp://dead-disc/announce" not in pairs
    assert "udp://whitelist/announce" not in pairs
    # 评分降序：快的在前
    assert scored[0][0] == "udp://fast-disc/announce"
    # reserve 列表与 promote 分数同源：截断只影响列表，不影响分数全集
    reserve_list = [t for t, _ in scored[:1]]
    assert reserve_list == ["udp://fast-disc/announce"]
    assert set(pairs.keys()) >= set(reserve_list)


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
