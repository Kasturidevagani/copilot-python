import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from practice_project import math_ops


def test_add():
    assert math_ops.add(1, 2) == 3


def test_divide():
    assert math_ops.divide(6, 3) == 2


def test_divide_by_zero():
    try:
        math_ops.divide(1, 0)
    except ZeroDivisionError:
        assert True
    else:
        assert False


def test_fibonacci():
    assert math_ops.fibonacci(0) == []
    assert math_ops.fibonacci(1) == [0]
    assert math_ops.fibonacci(5) == [0, 1, 1, 2, 3]
