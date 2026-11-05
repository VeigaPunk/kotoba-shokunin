#!/usr/bin/env python3
"""Scratch-only: m2b = the brief's m2 (refusal comparison weakened to `<`: only drops refused).

Candidate: `return n == want` (refuse when n != want). m2b: refuse only when n < want, so an added
kill row (n > want) is accepted. Usage: python3 -B mut2b.py <clone>.
"""
import pathlib
import sys

D = pathlib.Path(sys.argv[1])
p = D / "verifiers/check_mutation_battery.py"
t = p.read_text(encoding="utf-8")
old = '    return n == want, "observed %d kill rows, pinned %d" % (n, want)'
new = '    return not (n < want), "observed %d kill rows, pinned %d" % (n, want)'
if t.count(old) != 1:
    print("anchor count %d" % t.count(old), file=sys.stderr)
    raise SystemExit(3)
p.write_text(t.replace(old, new), encoding="utf-8")
print("applied m2b")
