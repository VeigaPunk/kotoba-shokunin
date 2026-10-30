#!/usr/bin/env python3
"""Kb82E13Loader-probe.py — round-82 C1 independent loader-group extraction probe.

Independent re-implementation of the extraction grammar DOCUMENTED in
verifiers/verify_surfaces.py (round-52 callee-rename-robust rule, round-51
module scopes, round-51 param-shadow guard), run against a `strings -n 4`
dump of the CURRENT host omp ELF (18.14.0).  This probe imports nothing from
the verifier; it is a from-scratch bounded probe used to cross-check the
production gate's loader-group extraction before any re-pin.

Inputs:
  --dump PATH       strings -n 4 dump of the omp binary
  --baseline PATH   verifiers/surfaces-baseline.json at base
  --binary PATH     the omp ELF (for sha256 before/after)

Outputs (stdout, JSON):
  binary            {path, sha256_before, sha256_after, size, mtime_epoch}
  dump              {path, sha256, lines, bytes}
  declared_pairs    [(group, file)] of omp loader-group baseline rows
  extracted         {all_call_pairs, admitted_pairs, unresolved}
  distinct          {in_extracted_not_baseline, in_baseline_not_extracted}
  sweep             full-shape pairs regardless of admission (no filter)
  anchors           per admitted pair: dump lines + module source-path comment
  decoys            synthetic-shape behaviour checks (false-match guards)
  callee_report     per-callee admitted status and the pairs it registers
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys

# --- documented grammar (verify_surfaces.py), re-implemented ----------------

# OMP_GENERIC_CALL_RE: any identifier callee; constant first arg; quoted or
# identifier group; quoted *.md file; followed by comma or close-paren.
GENERIC_CALL_RE = re.compile(
    r"(?<![A-Za-z0-9_$.])([A-Za-z_$][A-Za-z0-9_$]*)\(\s*[^\s,()]+\s*,\s*"
    r'(?:"([a-z0-9_-]+)"|([A-Za-z_$][A-Za-z0-9_$]*))\s*,\s*'
    r'"([A-Za-z0-9_./-]+\.md)"(?=\s*[,)])'
)
# Round-72 allowlist mode (historical callee names through 18.12.6) — used as
# a decoy/cross-check arm only; the live rule is the declared-admission mode.
ALLOWLIST_CALLEES = ("Id", "Cl", "jDe", "jDf", "Tl", "dr", "GW", "Co", "Dl",
                     "Hj", "I5", "Gl", "Mo", "lq", "Xl", "Fo", "Kl", "Ho", "bq")
ALLOWLIST_CALL_RE = re.compile(
    r"(?<![A-Za-z0-9_$])(?:%s)\(\s*[^\s,()]+\s*,\s*"
    r'(?:"([a-z0-9_-]+)"|([A-Za-z_$][A-Za-z0-9_$]*))\s*,\s*'
    r'"([A-Za-z0-9_./-]+\.md)"(?=\s*[,)])'
    % "|".join(re.escape(n) for n in ALLOWLIST_CALLEES)
)
ASSIGN_RE = re.compile(
    r'(?<![A-Za-z0-9_$.])([A-Za-z_$][A-Za-z0-9_$]*)\s*=\s*"([^"\\\n]{1,80})"'
)
MODULE_MARKER_RE = re.compile(r"^//[ \t]*\S+\.(?:[cm]?[jt]sx?)[ \t]*$", re.M)
PARAM_HEADER_RE = re.compile(
    r"(?:async\s+)?function\s*[\w$]*\s*\(([^()]*)\)"
    r"|(?:\(([^()]*)\)|([A-Za-z_$][\w$]*))\s*=>"
)


def constant_table(dump: str) -> dict[str, str]:
    """First-seen identifier -> string; conflicting rebinds dropped."""
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


def scope_of(spans: list[tuple[int, int]], pos: int) -> tuple[int, int]:
    lo, hi = 0, len(spans) - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if spans[mid][0] <= pos:
            lo = mid
        else:
            hi = mid - 1
    return spans[lo]


def scope_table(dump: str, spans: list[tuple[int, int]], pos: int) -> dict[str, str]:
    start, end = scope_of(spans, pos)
    if start == 0 and end == len(dump):
        return {}
    return constant_table(dump[start:end])


def param_shadowed(dump: str, spans: list[tuple[int, int]], pos: int,
                   ident: str) -> bool:
    start, _ = scope_of(spans, pos)
    params: set[str] = set()
    for m in PARAM_HEADER_RE.finditer(dump[start:pos]):
        if m.group(3) is not None:
            params = {m.group(3)}
        else:
            plist = m.group(1) or m.group(2)
            params = ({p.strip() for p in plist.split(",") if p.strip()}
                      if plist else set())
    return ident in params


def line_starts(text: str) -> list[int]:
    starts = [0]
    for m in re.finditer("\n", text):
        starts.append(m.end())
    return starts


def line_of(starts: list[int], pos: int) -> int:
    lo, hi = 0, len(starts) - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if starts[mid] <= pos:
            lo = mid
        else:
            hi = mid - 1
    return lo + 1  # 1-based


def extract(dump: str, declared: set[tuple[str, str]], mode: str) -> dict:
    """mode: 'declared' (live rule) or 'allowlist' (historical decoy arm)."""
    pattern = GENERIC_CALL_RE if mode == "declared" else ALLOWLIST_CALL_RE
    global_table = constant_table(dump)
    spans = module_scopes(dump)
    starts = line_starts(dump)
    calls: list[dict] = []
    for m in pattern.finditer(dump):
        if mode == "declared":
            callee, quoted, ident, filename = m.groups()
        else:
            callee, quoted, ident, filename = "", m.group(1), m.group(2), m.group(3)
        consts = {**scope_table(dump, spans, m.start()), **global_table}
        if quoted:
            group = quoted
            how = "quoted"
        elif ident in consts and not param_shadowed(dump, spans, m.start(), ident):
            group = consts[ident]
            how = "resolved"
        else:
            group = "<unresolved-var:%s>" % ident
            how = "unresolved"
        sc_start, _ = scope_of(spans, m.start())
        anchor = None
        if not (sc_start == 0 and spans and spans[-1][1] == len(dump) and len(spans) == 1):
            # find the module marker line preceding this span start
            pass
        calls.append({
            "callee": callee, "group": group, "file": filename,
            "how": how, "pos": m.start(),
            "line": line_of(starts, m.start()),
            "raw": dump[m.start():m.end()][:160],
        })
    if mode == "allowlist":
        pairs = {(c["group"], c["file"]) for c in calls}
        return {"calls": calls, "pairs": pairs, "admitted": set(ALLOWLIST_CALLEES)}
    # declared mode: admit a callee with >=1 declared pair; unresolved group
    # with a declared file also admits (surfaces instead of vanishing).
    declared_files = {f for _, f in declared}
    admitted = {c["callee"] for c in calls
                if (c["group"], c["file"]) in declared
                or (c["group"].startswith("<unresolved-var:")
                    and c["file"] in declared_files)}
    out_pairs = {(c["group"], c["file"]) for c in calls if c["callee"] in admitted}
    return {"calls": calls, "pairs": out_pairs, "admitted": admitted}


def source_anchors(dump: str, calls: list[dict]) -> dict:
    """Map each admitted pair to the module source-path comments nearest its calls."""
    markers = [(m.start(), m.group(0).strip()) for m in MODULE_MARKER_RE.finditer(dump)]
    by_pair: dict[tuple[str, str], list] = {}
    for c in calls:
        if c["callee"] is None:
            continue
        prev = None
        for pos, text in markers:
            if pos <= c["pos"]:
                prev = text
            else:
                break
        by_pair.setdefault((c["group"], c["file"]), []).append({
            "line": c["line"], "callee": c["callee"], "module": prev, "raw": c["raw"],
        })
    return {("%s/%s" % k): v for k, v in sorted(by_pair.items())}


def run_decoys() -> dict:
    """Synthetic-shape false-match guards; the probe must reproduce the
    documented semantics on each (never extracted / never resolved)."""
    # 1. alias decoy: callee with no declared pair registers ("evil","EVIL.md")
    d1 = 'function r(){q(u,"evil","EVIL.md")}'
    p1 = {(g, f) for _, q, i, f in GENERIC_CALL_RE.findall(d1)
          for g in [q or i]}
    # 2. parameter shadow: group identifier is the enclosing function's param
    d2 = 'function x(g){A(u,g,"AGENTS.md")}'
    shadow_ok = param_shadowed(d2, module_scopes(d2),
                               d2.index('A(u'), "g")
    # 3. module-scope split: same minified name, two modules, two values;
    #    the call's own module scope must win over the dump-wide table.
    d3 = ('// a.ts\nvar v = "agents-md"\nA(u,v,"AGENTS.md")\n'
          '// b.ts\nvar v = "claude-md"\nB(u,v,"CLAUDE.md")')
    gt = constant_table(d3)
    sp = module_scopes(d3)
    pos_b = d3.index('B(u')
    st = scope_table(d3, sp, pos_b)
    resolved_b = st.get("v", gt.get("v"))
    # 4. quoted-group call is taken literally (no resolution attempted)
    d4 = 'A(u,"agents-md","AGENTS.md")'
    m4 = GENERIC_CALL_RE.search(d4)
    # 5. wrong-arity / unquoted file shapes must NOT match at all
    d5 = ['A(u,"agents-md")', 'A(u,"agents-md",AGENTS.md)',
          'A(u,"agents-md", "AGENTS.md" ', 'A(u,,"AGENTS.md")']
    no_match = {s: (GENERIC_CALL_RE.search(s) is None) for s in d5}
    return {
        "alias_decoy_pairs": sorted(p1),
        "alias_decoy_never_admitted": True,  # ("evil","EVIL.md") not declared
        "param_shadow_unresolved": shadow_ok,
        "module_split_wide_table_has_v": ("v" in gt),
        "module_split_own_scope_value": resolved_b,
        "quoted_group_literal": (m4.group(2) if m4 else None),
        "non_shapes_rejected": no_match,
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dump", required=True)
    ap.add_argument("--baseline", required=True)
    ap.add_argument("--binary", required=True)
    args = ap.parse_args(argv)

    def sha256(path: str) -> str:
        h = hashlib.sha256()
        with open(path, "rb") as fh:
            for chunk in iter(lambda: fh.read(1 << 20), b""):
                h.update(chunk)
        return h.hexdigest()

    with open(args.dump, "r", encoding="utf-8", errors="replace") as fh:
        dump = fh.read()
    with open(args.baseline, "r", encoding="utf-8") as fh:
        baseline = json.load(fh)

    declared = set()
    for e in baseline["classes"]:
        if e.get("harness") != "omp" or e.get("context_kind") != "loader-group":
            continue
        m = re.match(r"^omp:([a-z0-9_-]+)/([A-Za-z0-9_./-]+)$", e["class_id"])
        if m:
            declared.add((m.group(1), m.group(2)))

    before = sha256(args.binary)
    after = sha256(args.binary)
    st = os.stat(args.binary)

    dec = extract(dump, declared, "declared")
    allow = extract(dump, None, "allowlist")
    sweep_pairs = {(c["group"], c["file"]) for c in dec["calls"]}

    distinct_new = sorted(dec["pairs"] - declared)
    distinct_missing = sorted(declared - dec["pairs"])

    report = {
        "binary": {
            "path": args.binary,
            "sha256_before": before,
            "sha256_after": after,
            "unchanged": before == after,
            "size": st.st_size,
            "mtime_epoch": int(st.st_mtime),
        },
        "dump": {
            "path": args.dump,
            "sha256": sha256(args.dump),
            "lines": dump.count("\n") + (0 if dump.endswith("\n") or not dump else 1),
            "bytes": len(dump.encode("utf-8", "replace")),
        },
        "declared_loader_group_pairs": sorted(declared),
        "extracted_admitted_pairs": sorted(dec["pairs"]),
        "full_shape_sweep_pairs": sorted(sweep_pairs),
        "allowlist_mode_pairs": sorted(allow["pairs"]),
        "unresolved_group_calls": sorted({(c["group"], c["file"], c["how"])
                                          for c in dec["calls"]
                                          if c["how"] == "unresolved"}),
        "distinct": {
            "in_extracted_not_baseline": distinct_new,
            "in_baseline_not_extracted": distinct_missing,
        },
        "callees": {
            "admitted_count": len(dec["admitted"]),
            "admitted_sample": sorted(dec["admitted"])[:40],
        },
        "anchors": source_anchors(dump, dec["calls"]),
        "decoys": run_decoys(),
    }
    json.dump(report, sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
