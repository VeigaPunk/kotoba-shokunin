#!/usr/bin/env python3
"""Context dump: declared variables near each join site + unledgered offset classification."""
import mmap, re, hashlib

ELF = "/home/vgpnk/.local/bin/omp"

h = open(ELF, "rb")
blob = mmap.mmap(h.fileno(), 0, access=mmap.ACCESS_READ)

def ctx(offset, before=2500, after=1200):
    lo = max(0, offset - before); hi = min(blob.size(), offset + after)
    return blob[lo:hi].decode("utf-8", "replace")

def line_at(offset):
    start = blob.rfind(b"\n", max(0, offset - 8192), offset)
    start = 0 if start < 0 else start + 1
    end = blob.find(b"\n", offset, offset + 8192)
    end = blob.size() if end < 0 else end
    return blob[start:end].decode("utf-8", "replace")

def has_join(line):
    return any(t in line for t in (b"join(", b".join(", b"resolve(", b"path.join"))

SITES = [
    (1, "{cwd}/.omp/skills", 173819979),
    (2, "{cwd}/.claude/skills", 173840364),
    (3, "{cwd}/.agent/skills", 173865724),
    (5, "{cwd}/.codex/skills", 173879095),
    (6, "{cwd}/.opencode/skills", 172785704),
    (7, "{cwd}/.github/skills", 172785704),
    (8, "~/.omp/agent/skills", 173820135),
    (9, "~/.omp/plugins/node_modules/*/skills", 173914936),
    (10, "~/.agent/skills", 173865523),
    (12, "~/.omp/agent/managed-skills", 173809938),
]

for num, pat, off in SITES:
    print("=" * 110)
    print(f"ROW {num} {pat} @ {off}")
    print("--- line:", repr(line_at(off)))
    print("--- context before:")
    print(ctx(off, 2200, 60))
    print("--- context after:")
    print(ctx(off, 40, 1400))

print("#" * 110)
print("UNLEDGERED OFFSETS (round-87 w3/ScoutPatternsR87/derived-roots.txt section C)")
UNL = [
    ("~/.claude/skills", 173840218),
    ("~/.codex/skills", 173882129),
    ("~/.config/opencode/skills", 172785499),
    ("<agent-plugin>/skills", 173778070),
    ("<claude-plugin>/skills", 173851107),
    ("~/.omp/plugins/node_modules/*", 166892485),
]
for name, off in UNL:
    ln = line_at(off)
    print("=" * 110)
    print(f"{name} @ {off}  join_token_on_line={has_join(ln.encode())}")
    print("  line:", repr(ln))
    print("  context before:")
    print(ctx(off, 1800, 60))
    print("  context after:")
    print(ctx(off, 40, 1200))
