#!/usr/bin/env python3
"""Count every frozen anchor of the v5 counter's c1 and r96c1 tables in a
candidate instrument.  Exit 0 iff every anchor matches exactly its expected
count; print one line per anchor."""
import importlib.util
import sys
from pathlib import Path

counter = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/"
               "fixtures/round-97/selftest-kills.py")
spec = importlib.util.spec_from_file_location("selftest_kills", counter)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

src = Path(sys.argv[1]).read_text(encoding="utf-8")
bad = 0
for claim in ("c1", "r96c1"):
    spec_c = mod.CLAIMS[claim]
    rows = list(spec_c["targets"]) + [spec_c["positive"]]
    for name, anchor, want, _repl in rows:
        got = src.count(anchor)
        ok = got == want
        bad += not ok
        print("%-5s %-34s want %d got %d %s"
              % (claim, name, want, got, "OK" if ok else "MISMATCH"))
print("anchor mismatches: %d" % bad)
sys.exit(1 if bad else 0)
