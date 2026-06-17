import sys
import os
import subprocess

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


def run_cmd(args):
    cmd = [sys.executable, "-m", "practice_project"] + args
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return p


def test_cli_add():
    p = run_cmd(["add", "2", "3"])
    assert p.returncode == 0
    assert p.stdout.strip() == "5.0"


def test_cli_fib():
    p = run_cmd(["fib", "6"])
    assert p.returncode == 0
    assert p.stdout.strip().startswith("0")
