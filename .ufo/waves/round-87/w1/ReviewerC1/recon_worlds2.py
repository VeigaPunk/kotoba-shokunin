#!/usr/bin/env python3
"""Attack specimens v2: header occurrence lists, window-only join lines, quote counts."""
import mmap
import re

ELF = "/home/vgpnk/.local/bin/omp"
JOIN_RE = re.compile(rb"join\(|\.join\(|resolve\(|path\.join")
fh = open(ELF, "rb")
mm = mmap.mmap(fh.fileno(), 0, access=mmap.ACCESS_READ)


def count(q):
    c, i = 0, mm.find(q)
    while i != -1:
        c += 1
        i = mm.find(q, i + 1)
    return c


print("header occurrence lists:")
for h in [b"// packages/coding-agent/src/discovery/builtin.ts",
          b"// packages/coding-agent/src/discovery/codex.ts",
          b"// packages/coding-agent/src/discovery/claude.ts",
          b"// packages/coding-agent/src/discovery/agents.ts",
          b"// packages/coding-agent/src/discovery/opencode.ts",
          b"// packages/coding-agent/src/discovery/github.ts",
          b"// packages/coding-agent/src/discovery/omp-plugins.ts",
          b"// packages/coding-agent/src/autolearn/managed-skills.ts"]:
    offs, i = [], mm.find(h)
    while i != -1:
        offs.append(i)
        i = mm.find(h, i + 1)
    print(f"  {h.decode():<58} n={len(offs)} first@{offs[0] if offs else -1} "
          f"last@{offs[-1] if offs else -1}")

print("\noccurrence counts of candidate reader quotes:")
for q in [b'dir: fr.join(we(), "skills"),',
          b'dir: fr.join(k, Ou.projectDir, "skills"),',
          b'dir: Zo.join(R.path, "skills"),',
          b'dir: Fr.join(k, eh, "skills"),',
          b'const k = Xr.join(R, "skills");',
          b'return Zm.join(u, "managed-skills");',
          b'Native OMP configuration from ~/.omp and .omp/']:
    print(f"  count={count(q):>3} first@{mm.find(q):>10}  {q.decode()!r}")

print("\nfabricated-quote check (must be absent from ELF):")
for q in [b'dir: Zo.join(R.path, "plugins", "skills"),',
          b'const R = yo.join(u, "plugins", "node_modules", "skills");',
          b'return pi.join(u, "managed-skills");']:
    print(f"  count={count(q)} {q.decode()!r}")

# W1a: unique lines with no join token on the line but one within +-200B,
# inside the builtin.ts module body (between its later header and the next header)
hdr = b"// packages/coding-agent/src/discovery/builtin.ts"
h0 = 173814223
nxt = mm.find(b"\n// packages/", h0 + 10)
print(f"\nW1a scan in builtin.ts body [{h0}, {nxt}):")
shown = 0
pos = h0
while pos < nxt and shown < 10:
    ls = mm.rfind(b"\n", 0, pos) + 1
    le = mm.find(b"\n", pos)
    le = min(le, nxt) if le != -1 else nxt
    line = mm[ls:le]
    if (len(line) >= 14 and not JOIN_RE.search(line) and line.strip()
            and b"skills" not in line.lower() and b"{" not in line
            and b"}" not in line and count(line) == 1):
        w = mm[max(0, ls - 200):le + 200]
        if JOIN_RE.search(w):
            print(f"  @{ls} len={len(line)} occ=1 {line.decode()!r}")
            shown += 1
    pos = le + 1
