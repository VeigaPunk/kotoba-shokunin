#!/usr/bin/env python3
"""ReviewerC1 ELF recon: module headers, doc-quote join proximity, reader lines."""
import mmap
import os
import re
import sys

ELF = "/home/vgpnk/.local/bin/omp"
JOIN_RE = re.compile(rb"join\(|\.join\(|resolve\(|path\.join")
HDR_RE = re.compile(rb"//[ \t]*packages/[A-Za-z0-9_./@-]+")

fh = open(ELF, "rb")
mm = mmap.mmap(fh.fileno(), 0, access=mmap.ACCESS_READ)
n = len(mm)

print(f"ELF bytes {n}")
hdrs = {}
for m in HDR_RE.finditer(mm):
    name = m.group(0)
    hdrs.setdefault(name, []).append(m.start())
print(f"distinct `// packages/...` headers: {len(hdrs)}")
for name in sorted(hdrs):
    offs = hdrs[name]
    print(f"  {name.decode():<64} n={len(offs):>3} first@{offs[0]:>10} last@{offs[-1]:>10}")

DOC = [
    b"Native OMP configuration from ~/.omp and .omp/",
    b"Load skills from .claude/skills/*/SKILL.md",
    b"Load skills from .agent/skills and .agents/skills (project walk-up + user home)",
    b"Load skills from ~/.codex/skills and .codex/skills/",
    b"Load skills from ~/.config/opencode/skills/ and .opencode/skills/",
    b"Auto-generated managed skills from ~/.omp/agent/managed-skills",
    b"var Gh = \".omp\";",
]
print("\ndoc/string-table quotes: join-token proximity (attack-1 survey)")
for q in DOC:
    offs, i = [], mm.find(q)
    while i != -1 and len(offs) < 6:
        offs.append(i)
        i = mm.find(q, i + 1)
    print(f"  {q.decode()[:60]!r} occurrences={len(offs)}")
    for off in offs:
        s, e = max(0, off - 200), min(n, off + 200)
        win = mm[s:e]
        j = JOIN_RE.search(win)
        # which line does the quote sit on, does THAT line carry a token?
        ls = mm.rfind(b"\n", 0, off) + 1
        le = mm.find(b"\n", off)
        le = n if le == -1 else le
        on_line = JOIN_RE.search(mm, ls, le) is not None
        print(f"    @{off:>10} token_in_window={'YES' if j else 'no '} "
              f"token_on_same_line={'YES' if on_line else 'no '}"
              + (f" win_token@{s + j.start() - off:+d}" if j else ""))

READERS = [
    b'dir: fr.join(we(), "skills"),',
    b'dir: fr.join(k, Ou.projectDir, "skills"),',
    b'dir: Zo.join(R.path, "skills"),',
    b'dir: Fr.join(k, eh, "skills"),',
    b'const k = Xr.join(R, "skills");',
    b'return Zm.join(u, "managed-skills");',
    b'const x = z9(u, "skills").map((k) => Ba(u, { dir: k, providerId: Yo, level: "user" }));',
    b'const p = V9(u, "skills").map((k) => Ba(u, { dir: k, providerId: Yo, level: "project" }));',
    b'const x = os(u, "opencode", "skills");',
    b'const p = os(u, "github", "skills");',
    b'const p = Ac(u, "opencode", "skills");',
]
print("\nknown code readers: same-line join token check (my conjunct-2 sanity)")
for q in READERS:
    off = mm.find(q)
    if off == -1:
        print(f"  NOT FOUND: {q.decode()[:70]!r}")
        continue
    ls = mm.rfind(b"\n", 0, off) + 1
    le = mm.find(b"\n", off)
    le = n if le == -1 else le
    on_line = JOIN_RE.search(mm, ls, le) is not None
    print(f"  @{off:>10} on_join_line={on_line} {q.decode()[:80]!r}")

# nearby preceding header for each reader (conjunct-3 geometry)
print("\nreader -> nearest preceding `// packages/` header")
for q in READERS:
    off = mm.find(q)
    if off == -1:
        continue
    best = None
    for name, offs in hdrs.items():
        for ho in offs:
            if ho < off and (best is None or ho > best[1]):
                best = (name, ho)
    if best:
        print(f"  {q.decode()[:56]!r} @{off} <- {best[0].decode()} @{best[1]} "
              f"(delta {off - best[1]})")
