"""Command-line interface for practice_project."""
import argparse
import sys
from . import math_ops


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="practice_project")
    sub = parser.add_subparsers(dest="cmd")

    p_add = sub.add_parser("add", help="Add two numbers")
    p_add.add_argument("a")
    p_add.add_argument("b")

    p_div = sub.add_parser("div", help="Divide two numbers")
    p_div.add_argument("a")
    p_div.add_argument("b")

    p_fib = sub.add_parser("fib", help="First n Fibonacci numbers")
    p_fib.add_argument("n", type=int)

    return parser


def main(argv=None) -> int:
    argv = argv or sys.argv[1:]
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.cmd == "add":
        a, b = float(args.a), float(args.b)
        print(math_ops.add(a, b))
        return 0
    if args.cmd == "div":
        a, b = float(args.a), float(args.b)
        try:
            print(math_ops.divide(a, b))
        except ZeroDivisionError as e:
            print(e)
            return 2
        return 0
    if args.cmd == "fib":
        seq = math_ops.fibonacci(args.n)
        print(" ".join(map(str, seq)))
        return 0

    parser.print_help()
    return 1
