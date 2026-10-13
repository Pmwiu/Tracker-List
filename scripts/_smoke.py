#!/usr/bin/env python3
"""私有冒烟测试（断言式，无 pytest 依赖）。

用法：
  python scripts/_smoke.py

其他脚本通过 @test 装饰器注册测试函数。退出码：0 全部通过，1 有失败。
"""

import sys

TESTS = []


def test(fn):
    """注册一个测试函数。"""
    TESTS.append((fn.__name__, fn))
    return fn


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
