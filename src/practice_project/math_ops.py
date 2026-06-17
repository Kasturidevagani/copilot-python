"""Simple math operations for practice."""
from typing import List


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def fibonacci(n: int) -> List[int]:
    """Return first n Fibonacci numbers (n >= 0)."""
    if n <= 0:
        return []
    seq = [0]
    if n == 1:
        return seq
    seq.append(1)
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq
