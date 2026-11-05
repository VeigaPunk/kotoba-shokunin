#!/usr/bin/env python3
"""ReviewerC1 W3 probe: the frozen counter's {cwd}/ expansion and `..` refusal.

Loads the frozen counter module (never edits it), introspects its expansion /
matcher surface, and calls it on the frozen ancestor chain
(/home/u/proj/sub -> /home/u/proj, /home/u, /home, /).

Usage: python3 -B probe_bound.py --counter <path to check_omp_root_semantics.py>
"""
import argparse
import importlib.util
import inspect
import re
import sys

HOME = "/home/u"
CWD = "/home/u/proj/sub"
CHAIN = ["/home/u/proj/sub", "/home/u/proj", "/home/u", "/home", "/"]
INTEREST = re.compile(r"expand|match|root|cwd|bound|walk|ancestor|candidate|resolve",
                      re.I)


def load(path):
    spec = importlib.util.spec_from_file_location("frozen_counter", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--counter", required=True)
    ap.add_argument("--source-grep", action="store_true")
    a = ap.parse_args()

    src = open(a.counter, encoding="utf-8", errors="replace").read()
    print(f"counter source: {len(src)} bytes")
    for lit in ["/home/u/proj/sub", "/home/u", "proj/sub", "HOME", "..",
                "JOIN_TOKENS", "join(", "resolve("]:
        hits = [m.start() for m in re.finditer(re.escape(lit), src)]
        print(f"  source literal {lit!r}: {len(hits)} hit(s)"
              + (f" first@{hits[0]}" if hits else ""))
    if a.source_grep:
        for i, line in enumerate(src.splitlines(), 1):
            if "/home/u" in line or re.search(r"\.\./|HOME", line):
                print(f"  L{i}: {line.rstrip()[:160]}")

    mod = load(a.counter)
    names = [n for n in dir(mod) if INTEREST.search(n) and not n.startswith("__")]
    print(f"\ncandidate functions/consts: {names}")
    for n in names:
        obj = getattr(mod, n)
        if callable(obj):
            try:
                print(f"  {n}{inspect.signature(obj)}")
            except (ValueError, TypeError):
                print(f"  {n} (builtin)")
        else:
            print(f"  {n} = {obj!r}"[:200])

    # try the most likely expansion calls on the frozen chain
    for n in names:
        obj = getattr(mod, n)
        if not callable(obj):
            continue
        for args in [("cwd", "{cwd}/.omp/skills"), (CWD, "{cwd}/.omp/skills"),
                     ("{cwd}/.omp/skills", CWD), (CWD,), ("{cwd}/.omp/skills",)]:
            try:
                out = obj(*args)
                print(f"CALL {n}{args!r} -> {out!r}"[:400])
            except Exception as ex:  # noqa: BLE001 — probing, honest failures only
                print(f"CALL {n}{args!r} -> raised {type(ex).__name__}: {ex}"[:200])


if __name__ == "__main__":
    sys.exit(main())
