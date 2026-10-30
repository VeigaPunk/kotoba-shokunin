#!/usr/bin/env python3
"""Kb82V01Loader independent loader-pair derivation on omp 18.14.0 dump.

Method (deliberately different from verify_surfaces.extract_classes):
per-line scan for registration-call shapes `CALLEE(ARG1, GROUP, "FILE.md")`,
capturing line numbers and resolving identifier GROUP args through
same-line `IDENT = "value"` bindings only (no dump-wide constant table,
no callee admission logic). Class assignment uses the baseline's class_id
vocabulary read independently from surfaces-baseline.json.
"""
import json
import re
import sys
from pathlib import Path

DUMP = Path(sys.argv[1])
BASELINE = Path(sys.argv[2])

# My own shape (spaces tolerated, lookahead on , or )).
CALL = re.compile(
    r'([A-Za-z_$][A-Za-z0-9_$]*)\(\s*[^,()\s]+\s*,\s*'
    r'(?:"([a-z0-9_-]+)"|([A-Za-z_$][A-Za-z0-9_$]*))\s*,\s*'
    r'"([A-Za-z0-9_./-]+\.md)"(?=\s*[,)])'
)
BIND = re.compile(r'(?<![A-Za-z0-9_$.])([A-Za-z_$][A-Za-z0-9_$]*)\s*=\s*"([^"\\\n]{1,80})"')

baseline = json.loads(BASELINE.read_text())
declared = {}
for e in baseline["classes"]:
    if e["harness"] == "omp" and e["context_kind"] == "loader-group":
        gid = e["class_id"].split("/", 1)[0].split(":", 1)[1]
        declared[(gid, e["literal"])] = e["class_id"]

# Dump-wide unique bindings: an identifier bound to exactly one string value
# anywhere in the dump resolves; multiply-bound identifiers stay unresolved.
GLOBAL_BIND = re.compile(r'(?<![A-Za-z0-9_$.])([A-Za-z_$][A-Za-z0-9_$]*)\s*=\s*"([^"\\\n]{1,80})"')
gb = {}
with DUMP.open("r", encoding="utf-8", errors="replace") as fh:
    for line in fh:
        if '"' not in line or '=' not in line:
            continue
        for k, v in GLOBAL_BIND.findall(line):
            gb.setdefault(k, set()).add(v)
gb_unique = {k: next(iter(v)) for k, v in gb.items() if len(v) == 1}

hits = []  # (line, callee, group, filename, group_src)
with DUMP.open("r", encoding="utf-8", errors="replace") as fh:
    for ln, line in enumerate(fh, 1):
        if ".md" not in line:
            continue
        for m in CALL.finditer(line):
            callee, quoted, ident, fname = m.groups()
            if quoted:
                group, gsrc = quoted, "literal"
            else:
                binds = dict(BIND.findall(line))
                if ident in binds:
                    group, gsrc = binds[ident], f"same-line-bind:{ident}"
                elif ident in gb_unique:
                    group, gsrc = gb_unique[ident], f"dump-unique-bind:{ident}"
                else:
                    group, gsrc = f"<unresolved:{ident}>", "unresolved"
            hits.append((ln, callee, group, fname, gsrc))

pairs = {}
for ln, callee, group, fname, gsrc in hits:
    pairs.setdefault((group, fname), []).append((ln, callee, gsrc))

print(f"raw call-shape hits: {len(hits)}; distinct (group,file): {len(pairs)}")
print("--- all distinct (group,file) with call sites ---")
for (g, f), sites in sorted(pairs.items()):
    callees = sorted({c for _, c, _ in sites})
    print(f"  {g!r:24} {f!r:32} sites={len(sites)} callees={callees}")

print("--- declared loader-group pair presence ---")
ok = True
for pair in sorted(declared):
    sites = pairs.get(pair)
    if sites:
        callees = sorted({c for _, c, _ in sites})
        print(f"  PRESENT  {pair[0]}/{pair[1]}  sites={len(sites)} callees={callees}")
    else:
        ok = False
        print(f"  MISSING  {pair[0]}/{pair[1]}")

extra = {p: s for p, s in pairs.items() if p not in declared}
print(f"--- pairs NOT in declared loader-group set: {len(extra)} ---")
for (g, f), sites in sorted(extra.items()):
    callees = sorted({c for _, c, _ in sites})
    print(f"  EXTRA  {g!r}/{f!r} sites={len(sites)} callees={callees}")

print("DERIVATION-MATCH" if ok and not extra else "DERIVATION-DIVERGENT")
