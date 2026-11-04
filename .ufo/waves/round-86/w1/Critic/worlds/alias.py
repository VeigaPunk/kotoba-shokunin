#!/usr/bin/env python3
"""alias.py <skillmd-list> <symlinks> <names> <out>: add one level of symlink aliases.

For every symlink L whose target directory T is a root or an ancestor of a root
holding a found SKILL.md P (with a fixture-name parent), emit L + P[len(T):] too.
A mechanical host search; it never reads omp.
"""
import os, sys
from collections import defaultdict
from pathlib import Path

listing, links, names_file, out = sys.argv[1:5]
names = set(Path(names_file).read_text().split())
paths = [l for l in Path(listing).read_text().splitlines() if Path(l).parent.name in names]
under = defaultdict(list)              # ancestor dir -> SKILL.md paths below it
for p in paths:
    d = os.path.dirname(os.path.dirname(p))
    while d.startswith("/home/vgpnk/"):
        under[d].append(p)
        d = os.path.dirname(d)
extra = []
for l in Path(links).read_text().splitlines():
    t = os.path.realpath(l)
    if t in under:
        extra += [l + p[len(t):] for p in under[t]]
Path(out).write_text("\n".join(paths + extra) + "\n")
print(f"{len(paths)} direct + {len(extra)} aliased SKILL.md paths")
