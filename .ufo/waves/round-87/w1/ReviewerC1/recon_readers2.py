#!/usr/bin/env python3
"""All join-lines in agents/opencode/github bodies + ELF-wide opencode/github join lines."""
import bisect
import mmap
import re
from array import array

ELF = "/home/vgpnk/.local/bin/omp"
JOIN_RE = re.compile(rb"join\(|\.join\(|resolve\(|path\.join")
fh = open(ELF, "rb")
mm = mmap.mmap(fh.fileno(), 0, access=mmap.ACCESS_READ)
n = len(mm)
starts = array("q", [0])
p = mm.find(b"\n")
while p != -1:
    starts.append(p + 1)
    p = mm.find(b"\n", p + 1)

def bounds(off):
    i = bisect.bisect_right(starts, off) - 1
    return starts[i], (starts[i + 1] - 1 if i + 1 < len(starts) else n)

def count(q):
    c, i = 0, mm.find(q)
    while i != -1:
        c += 1
        i = mm.find(q, i + 1)
    return c

BODIES = {
    "agents.ts": (173864077, 173869755),
    "opencode.ts": (173898271, 173906255),
    "github.ts": (173906256, 173911448),
}
for label, (lo, hi) in BODIES.items():
    print(f"== ALL join lines in {label} body [{lo}, {hi}):")
    pos, shown = lo, 0
    while pos < hi and shown < 20:
        s, e = bounds(pos)
        line = mm[s:min(e, hi)]
        if JOIN_RE.search(line):
            print(f"  @{s:>10} {line.decode('utf-8', 'replace')[:150]!r}")
            shown += 1
        pos = e + 1

print("\nELF-wide join lines containing b'opencode' (first 12):")
shown, pos = 0, 166000000
while shown < 12:
    i = mm.find(b"opencode", pos)
    if i == -1:
        break
    s, e = bounds(i)
    if JOIN_RE.search(mm, s, e):
        print(f"  @{s:>10} {mm[s:e].decode('utf-8', 'replace')[:150]!r}")
        shown += 1
    pos = e + 1

print("\nELF-wide join lines containing b'github' and b'skills' (first 12):")
shown, pos = 0, 166000000
while shown < 12:
    i = mm.find(b"github", pos)
    if i == -1:
        break
    s, e = bounds(i)
    seg = mm[s:e]
    if b"skills" in seg and JOIN_RE.search(seg):
        print(f"  @{s:>10} {seg.decode('utf-8', 'replace')[:150]!r}")
        shown += 1
    pos = e + 1

for q in [b'return Wne(u).flatMap((x) => y1.map((R) => Rs.join(x, R, ...p)));',
          b'const c = d.join(s, S.name, "SKILL.md");']:
    print(f"\ncount={count(q)} first@{mm.find(q)} {q.decode()!r}")
