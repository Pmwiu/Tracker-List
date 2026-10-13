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
    import os
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
