#!/usr/bin/env python3
"""Kb82E12Loader-probe.py — Round 82 C1 independent extraction probe, github group.

Seat Kb82E12Loader (leaf). Independent outside-guard for the C1 freshness
re-derivation: extracts the omp loader-group registration-call pairs for the
GROUP "github" from the CURRENT host ELF /home/vgpnk/.local/bin/omp (18.14.0)
via `strings -n 4`, using the extraction grammar DOCUMENTED in the lane's
verifiers/verify_surfaces.py docstrings (re-implemented here independently;
no import of the lane module for the primary path).  Also:

  * records sha256/mtime/size of the binary BEFORE and AFTER (read-only);
  * resolves identifier group args through dump-wide + module-scope constant
    tables with the documented conflict-drop and function-parameter shadow
    guard;
  * records source anchors (module-path comment lines) per call;
  * compares distinct extracted github pairs against the github-group pairs
    declared by verifiers/surface-baseline.json at base 47dbe878;
  * witnesses the github loader-literal classes ("instructions", "prompts",
    "copilot-instructions.md") by literal occurrence counts;
  * runs a false-match decoy battery on synthetic dumps (alias callee,
    param shadow, conflicting rebind, cross-module binding, non-.md file,
    token-without-loader-role);
  * cross-checks the independent result against the lane's own
    verify_surfaces.extract_classes() run on the same dump.

Output: JSON report to Kb82E12Loader-probe-report.json beside this file
(or --out path), human summary on stdout.  Read-only w.r.t. the host binary.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

HOST_OMP = Path("/home/vgpnk/.local/bin/omp")
BASE_REV = "47dbe8781657de563ff867caca6244d28e3db504"

# --- documented grammar (verify_surfaces.py docstrings, re-implemented) ------
# Registration-call shape with ANY identifier callee (round-52 documented
# grammar): callee(<v>, <quoted group> | <ident group>, "<file>.md") followed
# by comma or close paren.  The file literal MUST carry the .md suffix.
GENERIC_CALL_RE = re.compile(
    r"(?<![A-Za-z0-9_$.])([A-Za-z_$][A-Za-z0-9_$]*)\(\s*[^\s,()]+\s*,\s*"
    r'(?:"([a-z0-9_-]+)"|([A-Za-z_$][A-Za-z0-9_$]*))\s*,\s*'
    r'"([A-Za-z0-9_./-]+\.md)"(?=\s*[,)])'
)
# Identifier -> string binding, first declarator/second declarator/plain
# assignment forms; values up to 80 chars, no escapes/newlines.
ASSIGN_RE = re.compile(
    r'(?<![A-Za-z0-9_$.])([A-Za-z_$][A-Za-z0-9_$]*)\s*=\s*"([^"\\\n]{1,80})"'
)
# Module scopes: a line that is exactly a source-path comment opens a module.
MODULE_MARKER_RE = re.compile(r"^//[ \t]*\S+\.(?:[cm]?[jt]sx?)[ \t]*$", re.M)
# Function-parameter shadow guard: nearest preceding function header in the
# call's own module span; a header whose parameter list contains the ident
# disqualifies a constant-table resolution (fail-closed).
PARAM_HEADER_RE = re.compile(
    r"(?:async\s+)?function\s*[\w$]*\s*\(([^()]*)\)"
    r"|(?:\(([^()]*)\)|([A-Za-z_$][\w$]*))\s*=>"
)
CLASS_ID_RE = re.compile(r"^(omp|opencode):([a-z0-9_-]+)/([A-Za-z0-9_./-]+)$")


def sha256_file(path: Path) -> tuple[str | None, int | None]:
    if not path.is_file():
        return None, None
    h = hashlib.sha256()
    size = 0
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
            size += len(chunk)
    return h.hexdigest(), size


def binary_stat(path: Path) -> dict:
    digest, size = sha256_file(path)
    st = path.stat() if path.is_file() else None
    return {
        "path": str(path),
        "sha256": digest,
        "size": size,
        "mtime_epoch": st.st_mtime if st else None,
        "mtime_iso": time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime(st.st_mtime)) if st else None,
    }


def constant_table(dump: str) -> dict[str, str]:
    """First-seen ident -> string; conflicting rebinds drop the name."""
    table: dict[str, str] = {}
    conflicts: set[str] = set()
    for name, value in ASSIGN_RE.findall(dump):
        if name in conflicts:
            continue
        if name in table and table[name] != value:
            conflicts.add(name)
            table.pop(name, None)
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


def scope_anchor(dump: str, spans: list[tuple[int, int]], pos: int) -> str | None:
    """The module-marker comment line of the scope that contains pos."""
    start, _ = scope_of(spans, pos)
    if start == 0:
        return None
    # spans[i] starts at the END of marker i-1's text (the newline sits at
    # `start`), so recover the marker line by scanning back to its line start.
    line_start = dump.rfind("\n", 0, start - 1) + 1 if start > 1 else 0
    line = dump[line_start:start].strip()
    return line or None


def param_shadowed(dump: str, spans: list[tuple[int, int]], pos: int, ident: str) -> bool:
    start, _ = scope_of(spans, pos)
    params: set[str] = set()
    for m in PARAM_HEADER_RE.finditer(dump[start:pos]):
        if m.group(3) is not None:
            params = {m.group(3)}
        else:
            plist = m.group(1) or m.group(2)
            params = {p.strip() for p in plist.split(",") if p.strip()} if plist else set()
    return ident in params


def extract_all(dump: str, declared: set[tuple[str, str]]) -> tuple[list[dict], set[tuple[str, str]]]:
    """The documented round-52 admission sweep: any callee whose call sites
    register at least one declared (group, file) pair is admitted, and every
    pair an admitted callee registers is extracted.  Identifier groups resolve
    via scope-then-global constant tables with the param-shadow guard.
    Returns (per-call detail rows, extracted pair set)."""
    global_table = constant_table(dump)
    spans = module_scopes(dump)
    calls: list[dict] = []
    for m in GENERIC_CALL_RE.finditer(dump):
        callee, quoted, ident, filename = m.groups()
        local = scope_table(dump, spans, m.start())
        consts = {**local, **global_table}
        resolution = "quoted"
        if quoted:
            group = quoted
        elif ident in consts and not param_shadowed(dump, spans, m.start(), ident):
            group = consts[ident]
            resolution = "const-table"
        else:
            group = "<unresolved-var:%s>" % ident
            resolution = "unresolved(param-shadow)" if ident in consts else "unresolved(no-binding)"
        calls.append({
            "callee": callee,
            "group": group,
            "file": filename,
            "pair": [group, filename],
            "resolution": resolution,
            "offset": m.start(),
            "anchor": scope_anchor(dump, spans, m.start()),
            "context": dump[max(0, m.start() - 60):m.end() + 20].replace("\n", "\\n"),
        })
    declared_files = {f for _, f in declared}
    admitted = {c["callee"] for c in calls
                if tuple(c["pair"]) in declared
                or (c["group"].startswith("<unresolved-var:") and c["file"] in declared_files)}
    for c in calls:
        c["admitted"] = c["callee"] in admitted
    extracted = {tuple(c["pair"]) for c in calls if c["admitted"]}
    return calls, extracted


def declared_loader_pairs(entries: list[dict], harness: str) -> set[tuple[str, str]]:
    out: set[tuple[str, str]] = set()
    for e in entries:
        if e.get("harness") != harness:
            continue
        m = CLASS_ID_RE.match(e.get("class_id", ""))
        if m:
            out.add((m.group(2), m.group(3)))
    return out


# --------------------------------------------------------------------------
# false-match decoy battery (synthetic dumps; expected outcomes asserted)
# --------------------------------------------------------------------------

DECOY_DECLARED = {("github", "copilot-instructions.md")}


def run_decoys() -> list[dict]:
    results = []
    mod_github = "// packages/coding-agent/src/discovery/github.ts\n"

    def check(name: str, dump: str, expect_pairs: set[tuple[str, str]],
              expect_groups: set[str] | None = None,
              expect_unresolved: int = 0) -> dict:
        calls, extracted = extract_all(dump, DECOY_DECLARED)
        unresolved = sum(1 for c in calls if c["group"].startswith("<unresolved-var:"))
        groups = {c["group"] for c in calls}
        ok = extracted == expect_pairs and unresolved == expect_unresolved \
            and (expect_groups is None or groups == expect_groups)
        results.append({
            "decoy": name, "ok": ok,
            "extracted": sorted([list(p) for p in extracted]),
            "expected": sorted([list(p) for p in expect_pairs]),
            "unresolved_calls": unresolved,
            "groups_seen": sorted(groups),
        })
        return results[-1]

    # 1. alias decoy: a callee with NO declared pair must never be admitted.
    check("alias-decoy-callee",
          mod_github + 'var q = (a, b, c) => a;\nq(u, "evil", "EVIL.md");\n'
          'var ts = (a, b, c) => a;\nts(u, "github", "copilot-instructions.md");\n',
          {("github", "copilot-instructions.md")})
    # 2. param shadow: module binds Ko="github" but the call's function takes
    #    Ko as a parameter -> must NOT resolve to the "github" pair; the call
    #    surfaces as <unresolved-var:Ko> (documented fail-loud behaviour).
    check("param-shadowed-ident",
          mod_github + 'var Ko = "github";\n'
          'async function f(Ko) { return ts(u, Ko, "copilot-instructions.md"); }\n',
          {("<unresolved-var:Ko>", "copilot-instructions.md")}, expect_unresolved=1)
    # 3. conflicting rebind inside one module -> name dropped -> unresolved.
    check("conflicting-rebind",
          mod_github + 'var Ko = "github";\nvar Ko = "other";\n'
          'ts(u, Ko, "copilot-instructions.md");\n',
          {("<unresolved-var:Ko>", "copilot-instructions.md")}, expect_unresolved=1)
    # 4. cross-module: call in module B uses a binding made in module A (no
    #    conflict) -> dump-wide table resolves it.
    other_mod = "// packages/coding-agent/src/discovery/other.ts\n"
    check("cross-module-binding",
          mod_github + 'var Ko = "github";\n' + other_mod +
          'ts(u, Ko, "copilot-instructions.md");\n',
          {("github", "copilot-instructions.md")})
    # 5. non-.md file: `ts(u, "github", "instructions")` is NOT a registration
    #    shape under the grammar (file literal must end .md).
    check("non-md-file",
          mod_github + 'ts(u, "github", "instructions");\nts(u, "github", "prompts");\n',
          set())
    # 6. token-without-loader-role: enable-gate call and prose carrying the
    #    tokens must not extract.
    check("token-without-role",
          mod_github + 'if (ji("github", u)) { }\n'
          'description: "Load copilot-instructions.md from .github/ and ~/.copilot/"\n',
          set())
    # 7. unresolved group with a declared file: callee admitted, pair surfaces
    #    as unresolved (the documented CriticC1Escape behaviour).
    check("unresolved-declared-file",
          mod_github + 'ts(u, Zz, "copilot-instructions.md");\n',
          {("<unresolved-var:Zz>", "copilot-instructions.md")}, expect_unresolved=1)
    return results


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--binary", default=str(HOST_OMP))
    ap.add_argument("--dump", default=None, help="pre-made strings dump path")
    ap.add_argument("--clone", default="/fast/scratch/hyaku/kotoba-r82/Kb82E12Loader/clone")
    ap.add_argument("--group", default="github")
    ap.add_argument("--out", default=None)
    ap.add_argument("--lane-verifier", default=None,
                    help="optional path to lane verify_surfaces.py for cross-check")
    args = ap.parse_args(argv)

    binary = Path(args.binary)
    before = binary_stat(binary)

    # --- dump via strings -n 4 (documented harness) or reuse a given dump ---
    dump_path = Path(args.dump) if args.dump else None
    if dump_path is None:
        dump_path = Path(__file__).resolve().parent / "Kb82E12Loader-omp-strings.txt"
        proc = subprocess.run(["strings", "-n", "4", str(binary)],
                              capture_output=True, timeout=600)
        if proc.returncode != 0:
            print("strings failed rc=%d" % proc.returncode, file=sys.stderr)
            return 2
        dump_path.write_bytes(proc.stdout)
    dump = dump_path.read_text(encoding="utf-8", errors="replace")
    dump_sha, dump_size = sha256_file(dump_path)

    after = binary_stat(binary)
    binary_unchanged = before["sha256"] == after["sha256"]

    # --- baseline at base -------------------------------------------------
    baseline_file = Path(args.clone) / "verifiers" / "surfaces-baseline.json"
    entries = json.loads(baseline_file.read_text())["classes"]
    omp_declared = declared_loader_pairs(entries, "omp")
    group_entries = [e for e in entries
                     if e.get("harness") == "omp"
                     and CLASS_ID_RE.match(e.get("class_id", ""))
                     and CLASS_ID_RE.match(e["class_id"]).group(2) == args.group]
    baseline_group_pairs = {(CLASS_ID_RE.match(e["class_id"]).group(2),
                             CLASS_ID_RE.match(e["class_id"]).group(3))
                            for e in group_entries}
    baseline_loader_group_pairs = {p for p in baseline_group_pairs
                                   if any(e["context_kind"] == "loader-group"
                                          and CLASS_ID_RE.match(e["class_id"]).group(2) == p[0]
                                          and CLASS_ID_RE.match(e["class_id"]).group(3) == p[1]
                                          for e in group_entries)}

    # --- extraction ---------------------------------------------------------
    calls, extracted = extract_all(dump, omp_declared)
    group_calls = [c for c in calls if c["group"] == args.group]
    group_pairs = {tuple(c["pair"]) for c in group_calls if c["admitted"]}
    group_pairs_all_callees = {tuple(c["pair"]) for c in group_calls}  # incl. unadmitted

    # --- literal witnesses (loader-literal classes of this group) -----------
    literals = {}
    for e in group_entries:
        lit = e["literal"]
        occurrences = dump.count(lit)
        first = dump.find(lit)
        line = dump.count("\n", 0, first) + 1 if first != -1 else None
        literals[e["class_id"]] = {
            "literal": lit,
            "context_kind": e["context_kind"],
            "occurrences": occurrences,
            "first_line": line,
        }

    # --- set comparison vs baseline -----------------------------------------
    missing = sorted([list(p) for p in baseline_loader_group_pairs - group_pairs])
    extra = sorted([list(p) for p in group_pairs - baseline_loader_group_pairs])

    # --- cross-check vs lane verifier (independent agreement) ---------------
    crosscheck = None
    if args.lane_verifier:
        import importlib.util
        spec = importlib.util.spec_from_file_location("verify_surfaces", args.lane_verifier)
        vs = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(vs)
        lane_pairs = vs.extract_classes(dump, "omp", declared=omp_declared)
        crosscheck = {
            "lane_extract_classes_github_pairs": sorted([list(p) for p in lane_pairs
                                                         if p[0] == args.group]),
            "matches_independent": {p for p in lane_pairs if p[0] == args.group} == group_pairs,
        }

    report = {
        "seat": "Kb82E12Loader",
        "base_rev": BASE_REV,
        "binary_before": before,
        "binary_after": after,
        "binary_unchanged": binary_unchanged,
        "dump": {"path": str(dump_path), "sha256": dump_sha, "size": dump_size,
                 "lines": dump.count("\n") + 1},
        "group": args.group,
        "baseline_group_entries": group_entries,
        "baseline_group_pairs_all_kinds": sorted([list(p) for p in baseline_group_pairs]),
        "baseline_loader_group_pairs": sorted([list(p) for p in baseline_loader_group_pairs]),
        "extracted_group_pairs_admitted": sorted([list(p) for p in group_pairs]),
        "extracted_group_pairs_any_callee": sorted([list(p) for p in group_pairs_all_callees]),
        "missing_vs_baseline": missing,
        "extra_vs_baseline": extra,
        "full_sweep_total_calls": len(calls),
        "full_sweep_total_pairs": len(extracted),
        "full_sweep_extracted_pairs": sorted([list(p) for p in extracted]),
        "group_calls": group_calls,
        "group_literal_witnesses": literals,
        "decoys": run_decoys(),
        "crosscheck_lane_verify_surfaces": crosscheck,
        "generated_by": os.path.basename(__file__),
    }

    out = Path(args.out) if args.out else Path(__file__).resolve().parent / "Kb82E12Loader-probe-report.json"
    out.write_text(json.dumps(report, indent=2, sort_keys=True))
    print("binary sha before : %s" % before["sha256"])
    print("binary sha after  : %s" % after["sha256"])
    print("binary unchanged  : %s" % binary_unchanged)
    print("dump sha256       : %s (%d bytes)" % (dump_sha, dump_size))
    print("group             : %s" % args.group)
    print("baseline lg pairs : %s" % sorted(baseline_loader_group_pairs))
    print("extracted pairs   : %s" % sorted(group_pairs))
    print("missing vs base   : %s" % missing)
    print("extra vs base     : %s" % extra)
    print("literal witnesses : %s" % json.dumps(literals, sort_keys=True))
    print("full sweep pairs  : %d pairs over %d calls" % (len(extracted), len(calls)))
    for d in report["decoys"]:
        print("decoy %-26s ok=%s extracted=%s" % (d["decoy"], d["ok"], d["extracted"]))
    if crosscheck:
        print("lane cross-check  : matches_independent=%s" % crosscheck["matches_independent"])
    print("report written    : %s" % out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
