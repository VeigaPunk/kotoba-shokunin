#!/usr/bin/env python3
"""dotfilter.py <skillmd-list> <names> <order> <out-roots> <out-ledger>

Mechanical attack on addendum-1 G4: keep only brute roots whose every dot
segment ('.x') can be quoted from SOME >= 12-char printable ELF window that
contains all of them (any context; meaning ignored), order roots
(cover|alpha|find), and emit a per-root ledger `~/<rel>\t<window>`.
Reads the omp ELF as an opaque string pool, never its discovery code.
"""
import mmap, re, sys
from pathlib import Path

listing, names_file, order, out_roots, out_led = sys.argv[1:6]
HOME = "/home/vgpnk/"
names = set(Path(names_file).read_text().split())
first, cover = [], {}
for line in Path(listing).read_text().splitlines():
    p = Path(line)
    if p.parent.name not in names:
        continue
    r = str(p.parent.parent)
    if r not in cover:
        first.append(r); cover[r] = set()
    cover[r].add(p.parent.name)

f = open("/home/vgpnk/.local/bin/omp", "rb")
elf = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
PRINT = re.compile(rb"[\x20-\x7e]{12,}")
memo = {}


def quote_for(dots: tuple) -> str | None:
    if dots in memo:
        return memo[dots]
    q = None
    anchor = dots[0].encode()
    for mo in re.finditer(re.escape(anchor), elf):
        s, e = mo.start(), mo.end()
        while s > 0 and 0x20 <= elf[s - 1] <= 0x7e and mo.start() - s < 200:
            s -= 1
        while e < len(elf) and 0x20 <= elf[e] <= 0x7e and e - mo.end() < 200:
            e += 1
        run = elf[s:e]
        if len(run) >= 12 and all(d.encode() in run for d in dots) and b"\t" not in run:
            q = run.decode("ascii").strip()
            if len(q) >= 12:
                break
            q = None
    memo[dots] = q
    return q


kept, rows, dropped = [], ["root_pattern\tbinary_quote"], []
for r in first:
    if not r.startswith(HOME):
        dropped.append(r); continue
    rel = r[len(HOME):]
    dots = tuple(dict.fromkeys(s for s in rel.split("/") if s.startswith(".")))
    if not dots:
        dropped.append(r); continue
    q = quote_for(dots)
    if q is None:
        dropped.append(r); continue
    kept.append(r)
    rows.append(f"~/{rel}\t{q}")
if order == "alpha":
    kept.sort()
elif order == "cover":
    kept.sort(key=lambda r: (-len(cover[r]), r))
Path(out_roots).write_text("\n".join(kept) + "\n")
Path(out_led).write_text("\n".join(rows) + "\n")
cov = set().union(*(cover[r] for r in kept)) if kept else set()
print(f"{len(first)} roots -> kept {len(kept)}, dropped {len(dropped)}; kept cover {len(cov)} of {len(names)}")
