#!/usr/bin/env python3
"""reduce.py <roots> <ledger> <out-roots> <out-ledger>: one alias per real directory
(the one with the fewest path components; ties -> lexicographic), original order kept."""
import os, sys
from pathlib import Path
roots = [r for r in Path(sys.argv[1]).read_text().splitlines() if r]
led = Path(sys.argv[2]).read_text().splitlines()
q = {l.split("\t")[0]: l for l in led[1:]}
best = {}
for r in roots:
    k = os.path.realpath(r)
    if k not in best or (r.count("/"), r) < (best[k].count("/"), best[k]):
        best[k] = r
keep = set(best.values())
out = [r for r in roots if r in keep]
Path(sys.argv[3]).write_text("\n".join(out) + "\n")
Path(sys.argv[4]).write_text("\n".join([led[0]] + [q["~/" + r[len("/home/vgpnk/"):]] for r in out]) + "\n")
print(f"{len(roots)} -> {len(out)} roots")
