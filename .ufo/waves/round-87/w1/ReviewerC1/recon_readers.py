#!/usr/bin/env python3
"""ReviewerC1: own per-root reader-quote candidates + min header offset."""
import bisect
import mmap
import re
from array import array

ELF = "/home/vgpnk/.local/bin/omp"
JOIN_RE = re.compile(rb"join\(|\.join\(|resolve\(|path\.join")
HDR_RE = re.compile(rb"//[ \t]*packages/[A-Za-z0-9_./@-]+")
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
    s = starts[i]
    e = starts[i + 1] - 1 if i + 1 < len(starts) else n
    return s, e

def has_join(off):
    s, e = bounds(off)
    return JOIN_RE.search(mm, s, e) is not None

hdrs = {}
for m in HDR_RE.finditer(mm):
    name = m.group(0)[m.group(0).find(b"/") + 1:].lstrip()
    hdrs.setdefault(name, []).append(m.start())
print(f"min header offset: {min(o[0] for o in hdrs.values())} "
      f"(doc string-table first occurrence @114486488)")

MODULES = {
    "builtin.ts": b"// packages/coding-agent/src/discovery/builtin.ts",
    "agents.ts": b"// packages/coding-agent/src/discovery/agents.ts",
    "codex.ts": b"// packages/coding-agent/src/discovery/codex.ts",
    "opencode.ts": b"// packages/coding-agent/src/discovery/opencode.ts",
    "github.ts": b"// packages/coding-agent/src/discovery/github.ts",
    "claude.ts": b"// packages/coding-agent/src/discovery/claude.ts",
    "omp-plugins.ts": b"// packages/coding-agent/src/discovery/omp-plugins.ts",
    "managed-skills.ts": b"// packages/coding-agent/src/autolearn/managed-skills.ts",
}
for label, h in MODULES.items():
    offs, i = [], mm.find(h)
    while i != -1:
        offs.append(i)
        i = mm.find(h, i + 1)
    lo = max(offs)
    nxt = mm.find(b"\n// packages/", lo + 10)
    body_end = nxt if nxt != -1 else lo + 20000
    print(f"\n== {label} body [{lo}, {body_end}) — join lines mentioning skills/.omp/:")
    shown, pos = 0, lo
    while pos < body_end and shown < 14:
        s, e = bounds(pos)
        line = mm[s:min(e, body_end)]
        if JOIN_RE.search(line) and (b"skill" in line or b".omp" in line
                                     or b"agent" in line or b"codex" in line
                                     or b"opencode" in line or b"github" in line
                                     or b"claude" in line or b"plugin" in line):
            print(f"  @{s:>10} {line.decode('utf-8', 'replace')[:150]!r}")
            shown += 1
        pos = e + 1
