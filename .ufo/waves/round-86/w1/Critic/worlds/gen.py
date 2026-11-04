#!/usr/bin/env python3
"""Critic shortcut-world generator (round 86). Never reads omp's discovery source.

gen.py roots <skillmd-list> <names> <order> <out-roots>   order: find|alpha|cover
gen.py module <base-module> <roots-file> <out-module>
gen.py ledger <roots-file> <mode> <out-tsv>                mode: fragment|wildcard
"""
import re, sys
from pathlib import Path

GENERIC = ": archive has no SKILL.md"           # an error string; says nothing about discovery
FRAG = [(".agents/skills", "skills from .agent/skills and .agents/skills"),
        (".claude/skills", "Load skills from .claude/skills/*/SKILL.md"),
        (".codex/skills", "om ~/.codex/skills and .codex/skills/")]


def roots(listing, names_file, order, out):
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
    if order == "alpha":
        first = sorted(first)
    elif order == "cover":
        first = sorted(first, key=lambda r: (-len(cover[r]), r))
    Path(out).write_text("\n".join(first) + "\n")
    print(f"{len(first)} roots, {len(set().union(*cover.values()))} of {len(names)} names covered")


def module(base, roots_file, out):
    src = Path(base).read_text()
    rs = [r for r in Path(roots_file).read_text().splitlines() if r]
    body = "USER_ROOTS = [\n" + "".join(f"    Path({r!r}),\n" for r in rs) + "]\n"
    new, n = re.subn(r"^USER_ROOTS = \[\n(?:    .*\n)*?\]\n", body, src, count=1, flags=re.M)
    assert n == 1
    Path(out).write_text(new)


def ledger(roots_file, mode, out):
    rows = ["root_pattern\tbinary_quote"]
    if mode == "wildcard":
        rows.append(f"*\t{GENERIC}")
    else:
        for r in (x for x in Path(roots_file).read_text().splitlines() if x):
            q = next((q for frag, q in FRAG if frag in r), GENERIC)
            rows.append(f"{r}\t{q}")
    Path(out).write_text("\n".join(rows) + "\n")


if __name__ == "__main__":
    {"roots": roots, "module": module, "ledger": ledger}[sys.argv[1]](*sys.argv[2:])
