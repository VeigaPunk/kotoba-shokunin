#!/usr/bin/env python3
"""Kb82E09Loader — independent loader extraction probe for group `agents-md`.

Seat: Kotoba round 82, C1 freshness outside guard.  This probe re-implements
the documented extraction grammar of verifiers/verify_surfaces.py (round-51
module-scope resolution, round-52 callee-admission, round-51 param-shadow
guard) from its docstring and regex specs, WITHOUT importing the verifier, and
applies it to a `strings -n 4` dump of the current host omp ELF (18.14.0).

Outputs (JSON, stdout):
  binary           path/sha256/mtime/size of the measured ELF
  dump             dump path, sha256, line count, module-marker count
  baseline         base-revision surfaces-baseline.json sha256 + class count
  declared_pairs   omp (group, file) pairs declared at base
  sweep            every call matching the generic registration shape
                   (callee, group-resolved-or-<unresolved-var:...>, file,
                   dump line, module anchor, resolution path) — admission-free
  extracted        pairs after round-52 admission against declared pairs
  agents_md        per-call audit for the agents-md group
  diff             extracted vs declared, both directions
  literal_present  agents-md literals observed in the dump

The probe is read-only on the binary (it only runs sha256sum/stat/strings).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

# --- documented grammar (verbatim semantics from verify_surfaces.py) ---------

# Registration-call shape, ANY callee (round 52, OMP_GENERIC_CALL_RE):
#   <callee>(<v>, <quoted-group>|<ident-group>, "<file>.md")  followed by , or )
GENERIC_CALL_RE = re.compile(
    r"(?<![A-Za-z0-9_$.])([A-Za-z_$][A-Za-z0-9_$]*)\(\s*[^\s,()]+\s*,\s*"
    r'(?:"([a-z0-9_-]+)"|([A-Za-z_$][A-Za-z0-9_$]*))\s*,\s*'
    r'"([A-Za-z0-9_./-]+\.md)"(?=\s*[,)])'
)
# Module scope: a line that is exactly a source-path comment (round 51).
MODULE_MARKER_RE = re.compile(r"^//[ \t]*\S+\.(?:[cm]?[jt]sx?)[ \t]*$", re.M)
# Identifier -> string binding, first-seen wins, conflicting rebinds dropped.
ASSIGN_RE = re.compile(
    r'(?<![A-Za-z0-9_$.])([A-Za-z_$][A-Za-z0-9_$]*)\s*=\s*"([^"\\\n]{1,80})"'
)
# Function-parameter shadowing (round 51 falsify probe 09).
PARAM_HEADER_RE = re.compile(
    r"(?:async\s+)?function\s*[\w$]*\s*\(([^()]*)\)"
    r"|(?:\(([^()]*)\)|([A-Za-z_$][\w$]*))\s*=>"
)
CLASS_ID_RE = re.compile(r"^(omp|opencode):([a-z0-9_-]+)/([A-Za-z0-9_./-]+)$")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def constant_table(dump: str) -> dict[str, str]:
    """Dump-wide first-seen table; conflicting rebinds dropped (unresolvable)."""
    table: dict[str, str] = {}
    conflicts: set[str] = set()
    for name, value in ASSIGN_RE.findall(dump):
        if name in conflicts:
            continue
        if name in table and table[name] != value:
            conflicts.add(name)
            del table[name]
        else:
            table.setdefault(name, value)
    return table


def module_scopes(dump: str) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    start = 0
    for m in MODULE_MARKER_RE.finditer(dump):
        spans.append((start, m.start()))
        start = m.end()
    spans.append((start, len(dump)))
    return spans


def scope_of(spans, pos: int) -> tuple[int, int]:
    lo, hi = 0, len(spans) - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if spans[mid][0] <= pos:
            lo = mid
        else:
            hi = mid - 1
    return spans[lo]


def scope_table(dump: str, spans, pos: int) -> dict[str, str]:
    start, end = scope_of(spans, pos)
    if start == 0 and end == len(dump):
        return {}
    return constant_table(dump[start:end])


def scope_anchor(dump: str, spans, pos: int) -> str:
    """The source-path comment line that opens the scope containing pos."""
    start, _ = scope_of(spans, pos)
    line_start = dump.rfind("\n", 0, start) + 1
    line_end = dump.find("\n", start)
    marker = dump[line_start:line_end if line_end != -1 else len(dump)]
    return marker.strip()


def param_shadowed(dump: str, spans, pos: int, ident: str) -> bool:
    start, _ = scope_of(spans, pos)
    params: set[str] = set()
    for m in PARAM_HEADER_RE.finditer(dump[start:pos]):
        if m.group(3) is not None:
            params = {m.group(3)}
        else:
            plist = m.group(1) or m.group(2)
            params = {p.strip() for p in plist.split(",") if p.strip()} \
                if plist else set()
    return ident in params


def extract(dump: str):
    """Full pattern sweep + admission.  Returns (calls, extracted, tables)."""
    global_table = constant_table(dump)
    spans = module_scopes(dump)
    calls = []
    for m in GENERIC_CALL_RE.finditer(dump):
        callee, quoted, ident, filename = m.groups()
        scope_tbl = scope_table(dump, spans, m.start())
        consts = {**scope_tbl, **global_table}
        if quoted:
            group, how = quoted, "quoted-literal"
        elif ident in consts and not param_shadowed(dump, spans, m.start(), ident):
            group, how = consts[ident], (
                "dump-wide-table" if ident in global_table else "module-scope-table"
            )
        else:
            group, how = "<unresolved-var:%s>" % ident, (
                "param-shadowed" if ident in consts and
                param_shadowed(dump, spans, m.start(), ident)
                else "unresolvable"
            )
        line = dump.count("\n", 0, m.start()) + 1
        calls.append({
            "callee": callee,
            "group": group,
            "file": filename,
            "line": line,
            "module_anchor": scope_anchor(dump, spans, m.start()),
            "resolution": how,
            "ident": ident or "",
        })
    return calls, global_table, spans


def admit(calls, declared: set[tuple[str, str]]):
    """Round-52 admission: a callee is admitted when at least one call site
    registers a declared pair; unresolved groups admit only on a declared
    file.  Every pair of an admitted callee is extracted."""
    declared_files = {f for _, f in declared}
    admitted = {c["callee"] for c in calls
                if (c["group"], c["file"]) in declared
                or (c["group"].startswith("<unresolved-var:") and c["file"] in declared_files)}
    return {c["callee"]: None for c in calls if c["callee"] in admitted}, admitted


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--binary", required=True)
    ap.add_argument("--dump", required=True)
    ap.add_argument("--baseline", required=True)
    args = ap.parse_args()

    binary = Path(args.binary)
    dump_path = Path(args.dump)
    baseline_path = Path(args.baseline)

    bin_sha = sha256_file(binary)
    st = binary.stat()
    dump_text = dump_path.read_text(encoding="utf-8", errors="replace")
    dump_sha = sha256_file(dump_path)
    base_text = baseline_path.read_text(encoding="utf-8")
    base_sha = sha256_file(baseline_path)
    base = json.loads(base_text)

    declared = set()
    for e in base["classes"]:
        if e.get("harness") != "omp":
            continue
        m = CLASS_ID_RE.match(e.get("class_id", ""))
        if m:
            declared.add((m.group(2), m.group(3)))

    calls, global_table, spans = extract(dump_text)
    extracted_pairs = {(c["group"], c["file"]) for c in calls}
    _, admitted_callees = admit(calls, declared)

    # admission-restricted extraction (round-52 semantics)
    admitted_extracted = {
        (c["group"], c["file"]) for c in calls if c["callee"] in admitted_callees
    }

    agents_md_calls = [c for c in calls if c["group"] == "agents-md"]

    marker_count = len(MODULE_MARKER_RE.findall(dump_text))
    out = {
        "binary": {
            "path": str(binary),
            "sha256": bin_sha,
            "mtime_epoch": st.st_mtime,
            "size": st.st_size,
        },
        "dump": {
            "path": str(dump_path),
            "sha256": dump_sha,
            "lines": dump_text.count("\n") + 1,
            "module_markers": marker_count,
        },
        "baseline": {
            "path": str(baseline_path),
            "sha256": base_sha,
            "classes": len(base["classes"]),
        },
        "declared_pairs_omp": sorted([list(p) for p in declared]),
        "sweep": {
            "shape_calls": len(calls),
            "distinct_callees": sorted({c["callee"] for c in calls}),
            "calls": calls,
        },
        "admitted_callees": sorted(admitted_callees),
        "extracted_admitted_pairs": sorted([list(p) for p in admitted_extracted]),
        "extracted_all_pairs_unfiltered": sorted([list(p) for p in extracted_pairs]),
        "agents_md": {
            "calls": agents_md_calls,
            "pairs": sorted({(c["group"], c["file"]) for c in agents_md_calls}),
        },
        "diff_vs_declared": {
            "declared_not_extracted": sorted(
                [list(p) for p in declared - admitted_extracted]),
            "extracted_not_declared": sorted(
                [list(p) for p in admitted_extracted - declared]),
        },
        "literal_present": {
            "agents-md": "agents-md" in dump_text,
            "AGENTS.md": "AGENTS.md" in dump_text,
        },
    }
    json.dump(out, sys.stdout, indent=1, sort_keys=True)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
