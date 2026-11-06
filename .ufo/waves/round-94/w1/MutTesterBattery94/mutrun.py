#!/usr/bin/env python3
"""MutTesterBattery94 scratch harness (never committed).

Usage: mutrun.py <clone> [--only NAME,...] [--timeout S]
Applies each mutant (literal substitutions, counts checked) to <clone>/verifiers/check_mutation_battery.py,
runs `python3 -B verifiers/check_mutation_battery.py --self-test` in <clone>, records rc and the FAIL lines,
restores the exact original bytes, and prints one line per mutant.
"""
import os
import subprocess
import sys
import json
import py_compile
from pathlib import Path

INSTR = "verifiers/check_mutation_battery.py"

ANCHOR_PIN = "ok_pin, pin_detail = kill_set_check(committed, pinned)"
ORDER_BLOCK = ('    ok_pin, pin_detail = kill_set_check(committed, pinned)\n'
               '    if not ok_pin:\n'
               '        raise CouldNotEvaluate("arm kill-set-size: manifest at %s has %s"\n'
               '                               % (rev[:12], pin_detail))\n')

MUTANTS = [
    # control: byte-equivalent rewrite, must SURVIVE (equivalence)
    ("N13-equiv-control", [("return n == want, \"observed", 1, "return not (n != want), \"observed")]),
    # N1: committed manifest read at HEAD instead of --rev (rev != HEAD never exercised)
    ("N1-rev-head", [('committed = git_show(lane, rev, MANIFEST).decode("utf-8")', 1,
                      'committed = git_show(lane, "HEAD", MANIFEST).decode("utf-8")')]),
    # N2: off-by-one pin
    ("N2-off-by-one", [("return n == want, \"observed", 1, "return n == want + 1, \"observed")]),
    # N3: kill count also counts equivalent rows
    ("N3-count-equiv", [('return sum(1 for row in parse_manifest(text) if row.cls == "kill")', 1,
                         'return sum(1 for row in parse_manifest(text) if row.cls in ("kill", "equivalent"))')]),
    # N4: pin check moved after the probe loop (before results)
    ("N4-check-after-probes", [(ORDER_BLOCK, 1, ""), ("    results = []\n", 1, ORDER_BLOCK + "    results = []\n")]),
    # N5: label only the target-set refusal on the rev path as kill-set-size
    ("N5-label-targets-cne", [('raise CouldNotEvaluate("manifest must name exactly the targets %s"', 1,
                               'raise CouldNotEvaluate("arm kill-set-size: manifest must name exactly the targets %s"')]),
    # N6: pinned argument ignored
    ("N6-ignore-pinned", [("want = KILL_SET_PINNED if pinned is None else pinned", 1,
                           "want = KILL_SET_PINNED")]),
    # N7: accept fewer rows (drop direction, <= instead of ==)
    ("N7-accept-fewer", [("return n == want, \"observed", 1, "return n <= want, \"observed")]),
    # N8: malformed manifest accepted by the pin
    ("N8-malformed-accept", [('return False, "manifest malformed: %s" % exc', 1,
                              'return True, "manifest malformed: %s" % exc')]),
    # N9: rev path never refuses on the pin
    ("N9-rev-pin-disabled", [("    if not ok_pin:\n", 1, "    if ok_pin and False:\n")]),
    # N10: accept exactly one added row
    ("N10-accept-plus-one", [("return n == want, \"observed", 1,
                              "return (n == want or n == want + 1), \"observed")]),
    # N11: accept exactly two added rows
    ("N11-accept-plus-two", [("return n == want, \"observed", 1,
                              "return (n == want or n == want + 2), \"observed")]),
    # N12: AST-level inversion of the None test (pinned=None path refused)
    ("N12-ast-none-inversion", [("want = KILL_SET_PINNED if pinned is None else pinned", 1,
                                 "want = KILL_SET_PINNED if pinned is not None else pinned")]),
]


def main(argv):
    clone = Path(argv[1]).resolve()
    only = None
    timeout = 600
    if "--only" in argv:
        only = set(argv[argv.index("--only") + 1].split(","))
    if "--timeout" in argv:
        timeout = int(argv[argv.index("--timeout") + 1])
    path = clone / INSTR
    original = path.read_bytes()
    text0 = original.decode("utf-8")
    tmp = Path(os.environ["TMPDIR"])
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")

    def run():
        p = subprocess.run([sys.executable, "-B", INSTR, "--self-test"], cwd=clone, env=env,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=timeout)
        out = p.stdout.decode("utf-8", "replace")
        return p.returncode, out

    try:
        rc, out = run()
        fails = [ln for ln in out.splitlines() if ln.startswith("FAIL ")]
        last = [ln for ln in out.splitlines() if ln.strip()][-1:]
        print("HONEST rc=%d last=%r fails=%d" % (rc, last, len(fails)), flush=True)
        for name, subs in MUTANTS:
            if only and name not in only:
                continue
            text = text0
            ok = True
            for anchor, count, repl in subs:
                found = text.count(anchor)
                if found != count:
                    print("%s NOT-EVALUATED anchor count %d != %d" % (name, found, count), flush=True)
                    ok = False
                    break
                text = text.replace(anchor, repl)
            if not ok:
                continue
            tmpf = tmp / "mut.py"
            tmpf.write_text(text, encoding="utf-8")
            try:
                py_compile.compile(str(tmpf), cfile=str(tmp / "c.pyc"), doraise=True)
            except py_compile.PyCompileError as exc:
                print("%s NOT-EVALUATED does not compile: %s" % (name, exc.msg.splitlines()[-1]), flush=True)
                continue
            path.write_bytes(text.encode("utf-8"))
            try:
                rc, out = run()
            except subprocess.TimeoutExpired:
                rc, out = -999, "timeout"
            finally:
                path.write_bytes(original)
            fails = [ln for ln in out.splitlines() if ln.startswith("FAIL ")]
            last = [ln for ln in out.splitlines() if ln.strip()][-1:]
            verdict = "KILLED" if rc != 0 else "SURVIVED"
            print("%s rc=%d %s last=%r" % (name, rc, verdict, last), flush=True)
            for f in fails[:4]:
                print("    " + f[:220], flush=True)
    finally:
        path.write_bytes(original)
    after = path.read_bytes()
    print("RESTORED identical=%s" % (after == original), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
