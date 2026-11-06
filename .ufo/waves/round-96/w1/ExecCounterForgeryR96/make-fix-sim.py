#!/usr/bin/env python3
"""make-fix-sim.py -- build a scratch copy of the frozen v4 counter with two proposed v5 rules,
to measure whether the fix recommendations close the forgery worlds found in r96-w1.

This is a SIMULATION in /fast/scratch only. The frozen counter in the lane is never edited.

Rules added:
  R-honest-final  run the honest self-test once more at the very end; both honest runs must be CLEAN
                  (defeats a world that is CLEAN on the first run and fakes failures afterwards).
  R-mirror        run every target and the positive a second time with the mutant text on disk as
                  well as in memory; the mirror run must also be a REPORTED-FAILURE
                  (defeats a recompile-compare world: it is CLEAN when disk == executed text).
"""
from __future__ import annotations

import sys
from pathlib import Path

SRC = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/fixtures/round-96/selftest-kills.py")
OUT = Path("/fast/scratch/hyaku/kotoba-r96/ExecCounterForgeryR96/counter-fix-sim.py")


def main() -> int:
    text = SRC.read_text(encoding="utf-8")
    reps = [
        ("        killed = errors = 0\n",
         "        killed = errors = 0\n        mirror = 0\n"),
        ('            print("mutant %s rc %d %s: %s" % (name, rc, verdict, last_line(out)))\n',
         '            print("mutant %s rc %d %s: %s" % (name, rc, verdict, last_line(out)))\n'
         '            mtext = mutant_text(name, a, c, w)\n'
         '            rc_m, out_m, cls_m = run_text(mtext, "mirror " + name, mtext)\n'
         '            mirror += cls_m == "REPORTED-FAILURE"\n'
         '            print("mirror %s rc %d %s: %s" % (name, rc_m, '
         '"KILLED" if cls_m == "REPORTED-FAILURE" else cls_m, last_line(out_m)))\n'),
        ('        pos = 1 if cls == "REPORTED-FAILURE" else 0\n'
         '        print("positive %s rc %d %s: %s" % (pname, rc, "KILLED" if pos else cls, last_line(out)))\n',
         '        pos = 1 if cls == "REPORTED-FAILURE" else 0\n'
         '        print("positive %s rc %d %s: %s" % (pname, rc, "KILLED" if pos else cls, last_line(out)))\n'
         '        mtext = mutant_text(pname, pa, pc, pw)\n'
         '        rc, out, cls = run_text(mtext, "mirror " + pname, mtext)\n'
         '        pos_mirror = 1 if cls == "REPORTED-FAILURE" else 0\n'
         '        print("mirror %s rc %d %s: %s" % (pname, rc, '
         '"KILLED" if pos_mirror else cls, last_line(out)))\n'),
        ('        if path.read_text(encoding="utf-8") != original:\n',
         '        rc_h2, out_h2, cls_h2 = run_text(original, "honest-final", original)\n'
         '        print("honest-final rc %d %s: %s" % (rc_h2, cls_h2, last_line(out_h2)))\n'
         '        if path.read_text(encoding="utf-8") != original:\n'),
        ('        met = cls_h == "CLEAN" and killed == n and pos == 1 and held_comment == n and held_code == n\n',
         '        met = cls_h == "CLEAN" and cls_h2 == "CLEAN" and killed == n and mirror == n \\\n'
         '            and pos == 1 and pos_mirror == 1 and held_comment == n and held_code == n\n'),
        ('        print("%s targets killed %d of %d (run errors %d); positive killed %d of 1; honest %s; "\n',
         '        print("mirror targets killed %d of %d; mirror positive killed %d of 1"\n'
         '              % (mirror, n, pos_mirror))\n'
         '        print("%s targets killed %d of %d (run errors %d); positive killed %d of 1; honest %s; "\n'),
    ]
    for old, new in reps:
        if text.count(old) != 1:
            print("snippet miss (%d): %r" % (text.count(old), old[:70]), file=sys.stderr)
            return 2
        text = text.replace(old, new)
    compile(text, str(OUT), "exec", dont_inherit=True)
    OUT.write_text(text, encoding="utf-8")
    print("wrote", OUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
