"""Utility helpers for the practice project."""
from typing import Tuple


def parse_floats(args: Tuple[str, ...]) -> Tuple[float, ...]:
    return tuple(float(x) for x in args)


def safe_divide(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        return float('inf')
