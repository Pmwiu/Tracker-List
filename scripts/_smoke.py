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
