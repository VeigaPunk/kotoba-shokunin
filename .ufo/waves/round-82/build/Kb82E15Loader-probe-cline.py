#!/usr/bin/env python3
"""Kb82E15Loader — C1 independent extraction probe for group ``cline``.

Seat: Kb82E15Loader (kotoba round 82, wave 1). Scope: extraction probe only,
no production edit. Host substrate: /home/vgpnk/.local/bin/omp (omp 18.14.0,
ELF). Baseline: verifiers/surfaces-baseline.json @ base 47dbe8781657de563ff867caca6244d28e3db504.

The probe re-implements the documented extraction grammar of
verifiers/verify_surfaces.py (callee-rename-robust "declared" mode, round 52)
verbatim, with source anchors, and additionally:

  A. extracts every registration-shape call from the host strings dump and
     reports those whose resolved group is exactly ``cline`` (module-scoped
     resolution + source anchors);
  B. full pattern sweep: every extracted (group, file) pair whose group
     contains the substring ``cline`` (decoy family, e.g. clinerules);
  C. binding sweep: every identifier->string binding (dump-wide and per
     module scope) whose value contains ``cline``;
  D. raw token sweep: every whitespace-delimited dump token containing
     ``cline``, classified exact-vs-substring, with counts and a line anchor;
  E. distinct-pair comparison of the cline family vs surfaces-baseline.json
     at base (both directions, plus the clinerules decoy context row);
  F. six synthetic decoy fixtures proving the probe discriminates quoted
     groups, substring decoys, module-scoped identifier resolution,
     function-parameter shadowing (fail-closed), callee admission, and
     unresolved-variable surfacing.

Observed absence is a valid result: if no call resolves to group ``cline``,
sections A/B/C say so explicitly rather than guessing.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Documented grammar — verbatim from verifiers/verify_surfaces.py @ base
# 47dbe8781657de563ff867caca6244d28e3db504 (source anchors cited per rule).
# ---------------------------------------------------------------------------

# verify_surfaces.py:239 — OMP_GENERIC_CALL_RE (round 52 callee-rename-robust
# registration-call shape; any identifier callee; first arg a value; second arg
# quoted group OR identifier group; third arg a quoted *.md file; followed by
# `,` or `)`).
OMP_GENERIC_CALL_RE = re.compile(
    r"(?<![A-Za-z0-9_$])([A-Za-z_$][A-Za-z0-9_$]*)\(\s*[^\s,()]+\s*,\s*"
    r'(?:"([a-z0-9_-]+)"|([A-Za-z_$][A-Za-z0-9_$]*))\s*,\s*'
    r'"([A-Za-z0-9_./-]+\.md)"(?=\s*[,)])'
)
# verify_surfaces.py:248 — module scope markers (`//<path>.js|ts|jsx|...`).
MODULE_MARKER_RE = re.compile(r"^//[ \t]*\S+\.(?:[cm]?[jt]sx?)[ \t]*$", re.M)
# verify_surfaces.py:251 — identifier -> string bindings anywhere in the dump.
ASSIGN_RE = re.compile(
    r'(?<![A-Za-z0-9_$.])([A-Za-z_$][A-Za-z0-9_$]*)\s*=\s*"([^"\\\n]{1,80})"'
)
# verify_surfaces.py:254 — class id shape (baseline rows).
CLASS_ID_RE = re.compile(r"^(omp|opencode):([a-z0-9_-]+)/([A-Za-z0-9_./-]+)$")
# verify_surfaces.py:510 — function-parameter shadowing header shape.
PARAM_HEADER_RE = re.compile(
    r"(?:async\s+)?function\s*[\w$]*\s*\(([^()]*)\)"
    r"|(?:\(([^()]*)\)|([A-Za-z_$][\w$]*))\s*=>"
)

GROUP = "cline"


def constant_table(dump: str) -> dict[str, str]:
    """verify_surfaces.py:443 verbatim — first-seen binding wins; a name
    re-bound to a different value anywhere in the dump is dropped (marked
    unresolvable), never guessed."""
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
    """verify_surfaces.py:459 verbatim — each source-path comment opens a new
    module; a dump with no marker is a single whole-dump scope."""
    spans: list[tuple[int, int]] = []
    start = 0
    for m in MODULE_MARKER_RE.finditer(dump):
        spans.append((start, m.start()))
        start = m.end()
    spans.append((start, len(dump)))
    return spans


def scope_anchors(dump: str, spans: list[tuple[int, int]]) -> list[str | None]:
    """The source-path comment that OPENED each span: span 0 (the dump
    prefix before the first marker) has None; span i>=1 has markers[i-1].
    This is the per-extraction source anchor the seat report requires."""
    markers = [m.group(0).strip() for m in MODULE_MARKER_RE.finditer(dump)]
    anchors: list[str | None] = [None]
    anchors.extend(markers)
    return anchors[:len(spans)]


def anchor_for(span_starts: list[int],
               anchors: list[str | None], pos: int) -> str:
    lo, hi = 0, len(span_starts) - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if span_starts[mid] <= pos:
            lo = mid
        else:
            hi = mid - 1
    a = anchors[lo]
    return a if a else "<no-module-marker;whole-dump-scope>"


def scope_of(spans: list[tuple[int, int]], pos: int) -> tuple[int, int]:
    """verify_surfaces.py:474 verbatim."""
    lo, hi = 0, len(spans) - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if spans[mid][0] <= pos:
            lo = mid
        else:
            hi = mid - 1
    return spans[lo]


def scope_table(dump: str, spans: list[tuple[int, int]], pos: int) -> dict[str, str]:
    """verify_surfaces.py:480 verbatim — the constant table of the call's own
    module scope; whole-dump scope degenerates to {} (the global table is then
    the only table, per the original)."""
    start, end = scope_of(spans, pos)
    if start == 0 and end == len(dump):
        return {}
    return constant_table(dump[start:end])


def param_shadowed(dump: str, spans: list[tuple[int, int]], pos: int,
                   ident: str) -> bool:
    """verify_surfaces.py:517 verbatim — fail-closed: an identifier that is a
    parameter of the nearest preceding function header in the call's own
    module never resolves through a module/global binding."""
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


def extract_calls(dump: str) -> list[dict]:
    """Every registration-shape call in the dump, resolved per the documented
    grammar (global table first, own-module scope as fallback, parameter
    shadowing fail-closed, unresolved identifiers surfaced verbatim), each
    with its source anchor (the module's source-path comment)."""
    global_table = constant_table(dump)
    spans = module_scopes(dump)
    anchors = scope_anchors(dump, spans)
    span_starts = [s for s, _ in spans]
    out: list[dict] = []
    for m in OMP_GENERIC_CALL_RE.finditer(dump):
        callee, quoted, ident, filename = m.groups()
        scope_tab = scope_table(dump, spans, m.start())
        consts = {**scope_tab, **global_table}
        if quoted:
            group, how = quoted, "quoted"
        elif ident in consts and not param_shadowed(dump, spans, m.start(), ident):
            group, how = consts[ident], "ident:%s" % (
                "global" if ident in global_table else "module-scope")
        else:
            group, how = "<unresolved-var:%s>" % ident, "unresolved"
        out.append({
            "callee": callee, "group": group, "file": filename,
            "how": how, "offset": m.start(),
            "line": dump.count("\n", 0, m.start()) + 1,
            "module": anchor_for(span_starts, anchors, m.start()),
            "shadowed": bool(ident and ident in consts
                             and param_shadowed(dump, spans, m.start(), ident)),
        })
    return out


def declared_pairs(entries: list[dict], harness: str) -> set[tuple[str, str]]:
    """verify_surfaces.py:587 (declared_loader_pairs) verbatim semantics: the
    (group, file) pairs of every baseline class id for one harness, whatever
    its declared kind — admission must not depend on kind."""
    out: set[tuple[str, str]] = set()
    for e in entries:
        if e.get("harness") != harness:
            continue
        m = CLASS_ID_RE.match(e.get("class_id", ""))
        if m:
            out.add((m.group(2), m.group(3)))
    return out


# ---------------------------------------------------------------------------
# F. Synthetic decoy fixtures (bounded, inline) proving discrimination.
# ---------------------------------------------------------------------------

def run_decoys() -> list[dict]:
    results = []

    # F1: a real quoted "cline" registration must be extracted.
    d1 = 'X(a, "cline", "OK.md"),'
    got = [(c["group"], c["file"]) for c in extract_calls(d1)]
    results.append({"decoy": "F1-quoted-cline-call",
                    "expect": [("cline", "OK.md")], "got": got,
                    "pass": ("cline", "OK.md") in got})

    # F2: the substring decoy — a "clinerules" registration must NOT be
    # reported as a cline pair.
    d2 = 'X(a, "clinerules", "RULES.md"),'
    got = [(c["group"], c["file"]) for c in extract_calls(d2)]
    results.append({"decoy": "F2-substring-clinerules-not-cline",
                    "expect_not_group": GROUP, "got": got,
                    "pass": ("cline", "RULES.md") not in got
                    and ("clinerules", "RULES.md") in got})

    # F3: module-scoped identifier resolution (round 51): one minified name,
    # two modules, two bindings; each call resolves in its OWN module.
    d3 = ("//src/a.ts\nvar v = \"cline\"\nK(x, v, \"A.md\"),\n"
          "//src/b.ts\nvar v = \"other\"\nK(y, v, \"B.md\"),\n")
    got = {(c["group"], c["file"], c["module"]) for c in extract_calls(d3)}
    results.append({"decoy": "F3-module-scoped-identifier-resolution",
                    "expect": sorted([("cline", "A.md", "//src/a.ts"),
                                      ("other", "B.md", "//src/b.ts")]),
                    "got": sorted(got),
                    "pass": ("cline", "A.md", "//src/a.ts") in got
                    and ("other", "B.md", "//src/b.ts") in got})

    # F4: function-parameter shadowing is fail-closed: an identifier bound to
    # "cline" at module scope but passed as a parameter must NOT resolve.
    d4 = ("//src/c.ts\nvar w = \"cline\"\n"
          "function f(w) { return Q(u, w, \"P.md\"); }\n")
    calls = extract_calls(d4)
    got = [(c["group"], c["file"], c["shadowed"]) for c in calls]
    results.append({"decoy": "F4-param-shadow-fail-closed",
                    "expect_group": "<unresolved-var:w>",
                    "got": got,
                    "pass": any(c["group"] == "<unresolved-var:w>"
                                and c["file"] == "P.md" and c["shadowed"]
                                for c in calls)})

    # F5: callee admission (round 52): with a declared set naming only
    # ("cline","OK.md"), an alias callee registering an undeclared pair is not
    # admitted; every pair of an admitted callee IS extracted.
    d5 = ('X(a, "cline", "OK.md"),\n'
          'q(u, "evil", "EVIL.md"),\n'
          'X(b, "cline", "EXTRA.md"),\n')
    calls = extract_calls(d5)
    declared = {("cline", "OK.md")}
    admitted = {c["callee"] for c in calls
                if (c["group"], c["file"]) in declared
                or (c["group"].startswith("<unresolved-var:")
                    and c["file"] in {f for _, f in declared})}
    extracted = {(c["group"], c["file"]) for c in calls if c["callee"] in admitted}
    results.append({"decoy": "F5-callee-admission-alias-rejected",
                    "admitted_callees": sorted(admitted),
                    "extracted": sorted(extracted),
                    "pass": "q" not in admitted
                    and ("cline", "EXTRA.md") in extracted
                    and ("evil", "EVIL.md") not in extracted})

    # F6: an identifier with no binding anywhere surfaces as unresolved
    # (never guessed, never dropped).
    d6 = "//src/d.ts\nZ(t, nope, \"N.md\"),\n"
    calls = extract_calls(d6)
    results.append({"decoy": "F6-unresolved-var-surfaces",
                    "expect_group": "<unresolved-var:nope>",
                    "got": [(c["group"], c["file"]) for c in calls],
                    "pass": any(c["group"] == "<unresolved-var:nope>"
                                for c in calls)})
    return results


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dump", required=True, help="host strings dump path")
    ap.add_argument("--binary", required=True, help="host binary (sha evidence)")
    ap.add_argument("--baseline", required=True, help="surfaces-baseline.json")
    ap.add_argument("--out", required=True, help="JSON report output path")
    args = ap.parse_args(argv)

    dump_path = Path(args.dump)
    bin_path = Path(args.binary)
    dump = dump_path.read_text(encoding="utf-8", errors="replace")

    binary_sha_before = hashlib.sha256(bin_path.read_bytes()).hexdigest()
    dump_sha = hashlib.sha256(dump_path.read_bytes()).hexdigest()

    baseline = json.loads(Path(args.baseline).read_text(encoding="utf-8"))
    entries = baseline["classes"] if isinstance(baseline, dict) \
        and "classes" in baseline else baseline

    # -- A/B: full extraction + cline family sweep -----------------------------
    calls = extract_calls(dump)
    all_pairs = {(c["group"], c["file"]) for c in calls}
    cline_exact = [c for c in calls if c["group"] == GROUP]
    cline_family = sorted({(g, f) for g, f in all_pairs if GROUP in g})
    family_calls = [c for c in calls if GROUP in c["group"]]

    # -- C: binding sweep -------------------------------------------------------
    global_table = constant_table(dump)
    spans = module_scopes(dump)
    binding_hits: list[dict] = []
    for name, value in global_table.items():
        if GROUP in value:
            binding_hits.append({"scope": "dump-wide", "ident": name,
                                 "value": value})
    # per-module bindings containing cline (only modules where the global
    # table could not settle a name — the documented fallback path)
    anchors = scope_anchors(dump, spans)
    for idx, (start, end) in enumerate(spans):
        if start == 0 and end == len(dump):
            continue
        module_text = dump[start:end]
        anchor = anchors[idx] or "<no-module-marker>"
        for name, value in constant_table(module_text).items():
            if GROUP in value and global_table.get(name) != value:
                binding_hits.append({"scope": "module", "module": anchor,
                                     "ident": name, "value": value})

    # -- D: raw token sweep -----------------------------------------------------
    token_hits: dict[str, dict] = {}
    tok_re = re.compile(r"[A-Za-z0-9_./$-]*" + re.escape(GROUP) + r"[A-Za-z0-9_./$-]*")
    for lineno, line in enumerate(dump.splitlines(), 1):
        for tok in tok_re.findall(line):
            rec = token_hits.setdefault(tok, {"count": 0, "first_line": lineno})
            rec["count"] += 1
    token_report = [
        {"token": tok, "occurrences": r["count"], "first_line": r["first_line"],
         "kind": "exact-token" if tok == GROUP else "substring-of-longer-token"}
        for tok, r in sorted(token_hits.items(), key=lambda kv: (-kv[1]["count"], kv[0]))
    ]

    # -- E: baseline comparison -------------------------------------------------
    omp_declared = declared_pairs(entries, "omp")
    base_cline_exact = sorted(p for p in omp_declared if p[0] == GROUP)
    base_cline_family = sorted(p for p in omp_declared if GROUP in p[0])
    extracted_cline_exact = sorted({(c["group"], c["file"]) for c in cline_exact})
    comparison = {
        "baseline_omp_pairs_total": len(omp_declared),
        "baseline_cline_exact_pairs": base_cline_exact,
        "baseline_cline_substring_pairs": base_cline_family,
        "extracted_cline_exact_pairs": extracted_cline_exact,
        "extracted_cline_substring_pairs": cline_family,
        "distinct_extracted_minus_baseline_cline_family":
            sorted(set(cline_family) - set(base_cline_family)),
        "distinct_baseline_minus_extracted_cline_family":
            sorted(set(base_cline_family) - set(cline_family)),
        "decoy_context_row": [e for e in entries
                              if e.get("class_id") == "omp:clinerules/.clinerules"],
    }

    decoys = run_decoys()

    binary_sha_after = hashlib.sha256(bin_path.read_bytes()).hexdigest()

    report = {
        "probe": "Kb82E15Loader-cline-extraction-probe",
        "group": GROUP,
        "base_rev": "47dbe8781657de563ff867caca6244d28e3db504",
        "grammar_source": "verifiers/verify_surfaces.py @ base "
                          "(OMP_GENERIC_CALL_RE:239, MODULE_MARKER_RE:248, "
                          "ASSIGN_RE:251, PARAM_HEADER_RE:510, "
                          "constant_table:443, module_scopes:459, "
                          "scope_of:474, scope_table:480, "
                          "param_shadowed:517, declared_loader_pairs:587)",
        "host": {
            "binary": str(bin_path),
            "binary_sha256_before": binary_sha_before,
            "binary_sha256_after": binary_sha_after,
            "binary_unchanged": binary_sha_before == binary_sha_after,
            "dump": str(dump_path),
            "dump_sha256": dump_sha,
            "dump_lines": dump.count("\n") + 1,
            "module_scope_count": len(spans),
            "registration_shape_calls_total": len(calls),
            "distinct_pairs_total": len(all_pairs),
        },
        "A_cline_exact_extractions": cline_exact,
        "B_cline_substring_pair_sweep": cline_family,
        "B_cline_family_calls": family_calls,
        "C_binding_sweep": binding_hits,
        "D_token_sweep": token_report,
        "E_baseline_comparison": comparison,
        "F_decoys": decoys,
    }
    Path(args.out).write_text(json.dumps(report, indent=2, sort_keys=True) + "\n",
                              encoding="utf-8")

    print("cline exact extractions: %d" % len(cline_exact))
    print("cline substring pair sweep: %s" % (cline_family or "[]"))
    print("binding sweep hits: %d" % len(binding_hits))
    print("distinct cline tokens: %d" % len(token_report))
    print("baseline cline exact pairs: %s" % (base_cline_exact or "[]"))
    print("decoys: %d/%d pass" % (sum(1 for d in decoys if d["pass"]), len(decoys)))
    print("binary unchanged: %s" % (binary_sha_before == binary_sha_after))
    return 0


if __name__ == "__main__":
    sys.exit(main())
