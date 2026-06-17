"""Lightweight test runner fallback when pytest isn't available."""
import runpy
import glob
import sys


def run_test_file(path):
    try:
        runpy.run_path(path, run_name="__main__")
        return True, ""
    except AssertionError as e:
        return False, f"AssertionError: {e}"
    except SystemExit as e:
        # some tests call subprocess and may exit; treat non-zero as failure
        if getattr(e, 'code', 0) == 0:
            return True, ""
        return False, f"SystemExit: {e}"
    except Exception as e:
        return False, str(e)


def main():
    tests = glob.glob('tests/test_*.py')
    total = len(tests)
    passed = 0
    for t in tests:
        ok, msg = run_test_file(t)
        if ok:
            print(f"PASS: {t}")
            passed += 1
        else:
            print(f"FAIL: {t} -> {msg}")

    print(f"\n{passed}/{total} tests passed")
    return 0 if passed == total else 2


if __name__ == '__main__':
    raise SystemExit(main())
