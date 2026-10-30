#!/usr/bin/env python3
"""Kb82E11Loader — C1 independent extraction probe for group `gemini`.

Independent re-derivation of the documented verify_surfaces.py loader-call
extraction grammar (docstring §1 + OMP_GENERIC_CALL_RE / ASSIGN_RE /
MODULE_MARKER_RE / PARAM_HEADER_RE semantics), implemented from the
DOCUMENTED shapes only — verify_surfaces.py is NOT imported.

Inputs (read-only):
  --binary   host omp ELF (default /home/vgpnk/.local/bin/omp); sha256 taken
             before and after the analysis pass to prove no mutation.
  --dump     strings -n 4 dump of that binary (default: generated with
             `strings -n 4 <binary>`, exactly the verifier's command).
  --baseline surfaces-baseline.json taken at base rev
             47dbe8781657de563ff867caca6244d28e3db504 (fetched read-only via
             `git show` by the driver; passed as a plain file).

Outputs (JSON, --out):
  * every call matching the documented shape, with module-scoped identifier
    resolution provenance and source anchors (dump line, module source-path
    comment, callee, resolution class);
  * the distinct (group, file) pairs for group == "gemini", compared against
    the base baseline's declared omp loader-group pairs (set difference both
    ways), under BOTH the raw shape rule and the round-52 callee-admission
    rule (a callee is admitted iff one of its call sites registers a
    baseline-declared omp pair; every pair of an admitted callee extracts);
  * literal-presence census for the gemini literals (occurrence counts,
    how many occurrences sit inside a matched call shape);
  * full-group pattern sweep (distinct groups observed, observed-absence
    recorded as a valid result);
  * binary sha256 before/after, dump sha256/size/lines;
  * a synthetic decoy-fixture run proving false-match discrimination
    (prompt prose, template lists, bare assignments, two-arg calls,
    unquoted file args, non-.md files, alias callees, module-scope
    resolution, function-parameter shadowing).

Read-only: the probe never opens the binary for writing and never mutates
the lane repo.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

# --- documented grammar (re-implemented, not imported) ---------------------

# Registration-call shape, any callee (round-52 generic shape):
#   CALLEE(<v>, <group>, "<file>.md") followed by comma or close-paren.
CALL_SHAPE_RE = re.compile(
    r"(?<![A-Za-z0-9_$.])([A-Za-z_$][A-Za-z0-9_$]*)\(\s*[^\s,()]+\s*,\s*"
    r"(?:\"([a-z0-9_-]+)\"|([A-Za-z_$][A-Za-z0-9_$]*))\s*,\s*"
    r"\"([A-Za-z0-9_./-]+\.md)\"(?=\s*[,)])"
)
# Identifier -> string constant bindings (var/let/const or plain assignment,
# including second declarators). Same limits as the documented ASSIGN_RE.
BIND_RE = re.compile(
    r"(?<![A-Za-z0-9_$.])([A-Za-z_$][A-Za-z0-9_$]*)\s*=\s*\"([^\"\\\n]{1,80})\""
)
# Module-scope markers: a line that is only a source-path comment
# (// packages/.../foo.ts). A dump without markers is ONE scope.
MODULE_MARK_RE = re.compile(r"^//[ \t]*\S+\.(?:[cm]?[jt]sx?)[ \t]*$", re.M)
# Function headers whose parameter lists can shadow an identifier.
FUNC_HEADER_RE = re.compile(
    r"(?:async\s+)?function\s*[\w$]*\s*\(([^()]*)\)"
    r"|(?:\(([^()]*)\)|([A-Za-z_$][\w$]*))\s*=>"
)
CLASS_ID_RE = re.compile(r"^(omp|opencode):([a-z0-9_-]+)/([A-Za-z0-9_./-]+)$")


def sha256_file(path: Path, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        while True:
            b = fh.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def first_seen_table(text: str) -> dict[str, str]:
    """First-seen name->string table; a conflicting rebind drops the name."""
    table: dict[str, str] = {}
    conflicts: set[str] = set()
    for name, value in BIND_RE.findall(text):
        if name in conflicts:
            continue
        if name in table and table[name] != value:
            conflicts.add(name)
            del table[name]
        else:
            table.setdefault(name, value)
    return table


def module_spans(text: str) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    start = 0
    for m in MODULE_MARK_RE.finditer(text):
        spans.append((start, m.start()))
        start = m.end()
    spans.append((start, len(text)))
    return spans


def span_of(spans: list[tuple[int, int]], pos: int) -> tuple[int, int]:
    lo, hi = 0, len(spans) - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if spans[mid][0] <= pos:
            lo = mid
        else:
            hi = mid - 1
    return spans[lo]


def scope_table(text: str, spans: list[tuple[int, int]], pos: int) -> dict[str, str]:
    start, end = span_of(spans, pos)
    if start == 0 and end == len(text):
        return {}  # one-scope dump: the dump-wide table IS its scope table
    return first_seen_table(text[start:end])


def is_param_shadowed(text: str, spans: list[tuple[int, int]], pos: int,
                      ident: str) -> bool:
    start, _ = span_of(spans, pos)
    params: set[str] = set()
    for m in FUNC_HEADER_RE.finditer(text[start:pos]):
        if m.group(3) is not None:
            params = {m.group(3)}
        else:
            plist = m.group(1) or m.group(2)
            params = {p.strip() for p in plist.split(",") if p.strip()} \
                if plist else set()
    return ident in params


def line_no(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def scope_label(text: str, spans: list[tuple[int, int]], pos: int) -> str:
    """The source-path comment line that opens the scope containing pos,
    or '<whole-dump single scope>' when the dump has no markers."""
    start, end = span_of(spans, pos)
    if start == 0 and end == len(text):
        return "<whole-dump single scope>"
    # the marker that ENDS the previous span opens this one
    upto = text[:start]
    marks = list(MODULE_MARK_RE.finditer(upto))
    return marks[-1].group(0).strip() if marks else "<none>"


def extract_calls(dump: str) -> list[dict]:
    """Every call matching the documented shape, module-scoped resolution."""
    global_table = first_seen_table(dump)
    spans = module_spans(dump)
    out: list[dict] = []
    for m in CALL_SHAPE_RE.finditer(dump):
        callee, quoted, ident, filename = m.groups()
        if quoted:
            group, prov, shadowed = quoted, "quoted-literal", False
        else:
            consts = {**scope_table(dump, spans, m.start()), **global_table}
            shadowed = is_param_shadowed(dump, spans, m.start(), ident)
            if ident in consts and not shadowed:
                group, prov = consts[ident], "const-table"
                # provenance detail: did the own-scope table have it?
                if ident not in scope_table(dump, spans, m.start()):
                    prov = "dump-wide-table"
                else:
                    prov = "own-module-scope"
            else:
                group, prov = "<unresolved-var:%s>" % ident, \
                    "param-shadowed" if shadowed else "unresolvable"
        out.append({
            "callee": callee,
            "group": group,
            "file": filename,
            "dump_line": line_no(dump, m.start()),
            "module_scope": scope_label(dump, spans, m.start()),
            "resolution": prov,
            "quoted_group": bool(quoted),
            "group_ident": ident,
        })
    return out


def admit_by_declared(calls: list[dict], declared: set[tuple[str, str]]) -> set[tuple[str, str]]:
    """Round-52 admission: a callee is admitted when one of its call sites
    registers a declared pair (or its group stays unresolved while its file
    is a declared file); every pair of an admitted callee extracts."""
    declared_files = {f for _, f in declared}
    admitted = {c["callee"] for c in calls
                if (c["group"], c["file"]) in declared
                or (c["group"].startswith("<unresolved-var:") and c["file"] in declared_files)}
    return {(c["group"], c["file"]) for c in calls if c["callee"] in admitted}


# --- decoy fixture (false-match discrimination) ----------------------------

DECOY_DUMP = """\
// packages/demo/src/real.ts
var real = "gemini";
function reg(u){ return Zz(u, real, "GEMINI.md"), Qq(u, real, "system.md"); }
// packages/demo/src/prose.ts
const tips = "read gemini GEMINI.md first";
const list = ["gemini", "GEMINI.md", "notes"];
var lonely = "gemini";
function two(u){ return Only(u, "gemini"); }
function unq(u){ return Unq(u, "gemini", GEMINI_MD); }
function json(u){ return Js(u, "gemini", "settings.json"); }
function alias(u){ return Alias(u, "gemini", "FAKE.md"); }
// packages/demo/src/shadow.ts
var e = "gemini";
function q(e){ return Sh(u, e, "GEMINI.md"); }
// packages/demo/src/other.ts
var g = "gemini";
var other = "title";
function use(u){ return Use(u, g, "SYSTEM_TEMPLATE.md"); }
// packages/demo/src/title.ts
var g = "title";
function diff(u){ return Diff(u, g, "GEMINI.md"); }
"""


def run_decoys() -> dict:
    calls = extract_calls(DECOY_DUMP)
    pairs = {(c["group"], c["file"]) for c in calls}
    # Expected under the documented grammar:
    #   (gemini, GEMINI.md)  Zz, own-module resolution
    #   (gemini, system.md)  Qq
    #   (gemini, SYSTEM_TEMPLATE.md) Use — own module binds g="gemini"
    #   ("title", GEMINI.md) Diff — own module binds g="title" (module scope!)
    #   ("gemini", FAKE.md) alias callee — raw rule extracts, admission drops
    # NOT expected: prose, list, lonely, two/Only (2-arg call, no file arg),
    #   unq, json (.json file), Sh shadowed e (param shadowed -> unresolved)
    gemini_pairs = sorted([list(p) for p in pairs if p[0] == "gemini"])
    documented = [["gemini", "GEMINI.md"], ["gemini", "system.md"],
                  ["gemini", "SYSTEM_TEMPLATE.md"]]
    return {
        "fixture_text_lines": DECOY_DUMP.count("\n"),
        "raw_pairs": sorted([list(p) for p in pairs]),
        "gemini_pairs": gemini_pairs,
        "gemini_raw_equals_documented_plus_alias_decoy":
            gemini_pairs == sorted(documented + [["gemini", "FAKE.md"]]),
        "module_scope_resolved_title_not_gemini":
            ["title", "GEMINI.md"] in [list(p) for p in pairs],
        "param_shadow_blocked": ("<unresolved-var:e>", "GEMINI.md") in pairs,
        "alias_decoy_fake_present_raw": ("gemini", "FAKE.md") in pairs,
        "admission_drops_alias_decoy": sorted(
            [list(p) for p in admit_by_declared(
                calls, {("gemini", "GEMINI.md"), ("gemini", "system.md"),
                        ("gemini", "SYSTEM_TEMPLATE.md"), ("title", "GEMINI.md")})
             if p[0] == "gemini"]) == sorted(documented),
        "non_md_file_rejected": not any(f.endswith(".json") for _, f in pairs),
        "two_arg_call_rejected": not any(c["callee"] == "Only" for c in calls),
        "unquoted_file_rejected": not any(c["callee"] == "Unq" for c in calls),
        "prose_and_list_rejected": not any(
            c["file"] in ("GEMINI.md",) and c["callee"] in ("tips", "list", "lonely")
            for c in calls),
        "calls": calls,
    }


# --- main -------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--binary", default="/home/vgpnk/.local/bin/omp")
    ap.add_argument("--dump", default=None)
    ap.add_argument("--baseline", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    binary = Path(args.binary)
    sha_before = sha256_file(binary)
    size_before = binary.stat().st_size

    if args.dump:
        dump_path = Path(args.dump)
        dump = dump_path.read_text(encoding="utf-8", errors="replace")
        dump_sha = sha256_file(dump_path)
        strings_cmd = "supplied:%s" % dump_path
    else:
        proc = subprocess.run(["strings", "-n", "4", str(binary)],
                              capture_output=True)
        if proc.returncode != 0:
            print("strings failed: %d" % proc.returncode, file=sys.stderr)
            return 2
        dump = proc.stdout.decode("utf-8", "replace")
        dump_sha = hashlib.sha256(proc.stdout).hexdigest()
        strings_cmd = "strings -n 4 %s" % binary

    sha_after = sha256_file(binary)
    size_after = binary.stat().st_size

    baseline = json.loads(Path(args.baseline).read_text())
    classes = baseline["classes"]
    base_gemini = sorted(
        c["class_id"] for c in classes
        if c.get("harness") == "omp" and "gemini" in c.get("class_id", ""))
    declared_omp_pairs = sorted({
        (CLASS_ID_RE.match(c["class_id"]).group(2),
         CLASS_ID_RE.match(c["class_id"]).group(3))
        for c in classes
        if c.get("harness") == "omp"
        and CLASS_ID_RE.match(c.get("class_id", ""))
    })
    declared_loader_pairs = sorted({
        (CLASS_ID_RE.match(c["class_id"]).group(2),
         CLASS_ID_RE.match(c["class_id"]).group(3))
        for c in classes
        if c.get("harness") == "omp" and c.get("context_kind") == "loader-group"
        and CLASS_ID_RE.match(c.get("class_id", ""))
    })

    calls = extract_calls(dump)
    raw_pairs = {(c["group"], c["file"]) for c in calls}
    gemini_calls = [c for c in calls if c["group"] == "gemini"]
    gemini_pairs = sorted({(c["group"], c["file"]) for c in gemini_calls})
    gemini_pairs_admitted = sorted(
        p for p in admit_by_declared(calls, set(declared_omp_pairs))
        if p[0] == "gemini")

    groups_seen = sorted({g for g, _ in raw_pairs if not g.startswith("<")})
    unresolved_groups = sorted({g for g, _ in raw_pairs if g.startswith("<")})

    # literal census for the declared gemini literals
    literals = sorted({c["literal"] for c in classes
                       if c.get("harness") == "omp" and "gemini" in c["class_id"]})
    call_lines = {c["dump_line"] for c in gemini_calls}
    literal_census = {}
    lines = dump.split("\n")
    for lit in literals:
        occ = [i + 1 for i, l in enumerate(lines) if lit in l]
        in_call = sum(1 for i in occ if i in call_lines)
        literal_census[lit] = {
            "occurrences": len(occ),
            "occurrence_lines_bounded_first10": occ[:10],
            "inside_extracted_gemini_call_line": in_call,
        }

    declared_gemini_pairs = sorted(
        (g, f) for g, f in declared_loader_pairs if g == "gemini")

    report = {
        "seat": "Kb82E11Loader",
        "claim_scope": "C1 independent extraction probe for group gemini",
        "binary": {
            "path": str(binary),
            "size_before": size_before,
            "size_after": size_after,
            "sha256_before": sha_before,
            "sha256_after": sha_after,
            "unchanged": sha_before == sha_after and size_before == size_after,
        },
        "dump": {
            "produced_by": strings_cmd,
            "sha256": dump_sha,
            "bytes": len(dump.encode("utf-8", "replace")),
            "lines": dump.count("\n") + 1,
            "module_marker_lines": len(MODULE_MARK_RE.findall(dump)),
        },
        "grammar_source": "verify_surfaces.py documented extraction grammar "
                          "(docstring sec.1; OMP_GENERIC_CALL_RE / ASSIGN_RE / "
                          "MODULE_MARKER_RE / PARAM_HEADER_RE semantics), "
                          "re-implemented without importing the verifier",
        "baseline": {
            "path": args.baseline,
            "sha256": sha256_file(Path(args.baseline)),
            "base_rev": "47dbe8781657de563ff867caca6244d28e3db504",
            "omp_declared_pairs_all_kinds": [list(p) for p in declared_omp_pairs],
            "omp_declared_pairs_loader_group": [list(p) for p in declared_loader_pairs],
            "gemini_class_ids": base_gemini,
        },
        "sweep": {
            "total_shape_calls": len(calls),
            "distinct_groups_seen": groups_seen,
            "unresolved_group_tokens": unresolved_groups[:40],
            "unresolved_group_token_count": len(unresolved_groups),
            "distinct_pairs_raw": sorted([list(p) for p in raw_pairs]),
        },
        "gemini": {
            "declared_loader_pairs": [list(p) for p in declared_gemini_pairs],
            "extracted_pairs_raw": [list(p) for p in gemini_pairs],
            "extracted_pairs_callee_admitted": [list(p) for p in gemini_pairs_admitted],
            "pairs_found_not_declared":
                [list(p) for p in gemini_pairs if list(p) not in [list(d) for d in declared_gemini_pairs]],
            "pairs_declared_not_found":
                [list(p) for p in declared_gemini_pairs if list(p) not in [list(p) for p in gemini_pairs]],
            "declared_found_intersection":
                [list(p) for p in gemini_pairs if list(p) in [list(d) for d in declared_gemini_pairs]],
            "calls": gemini_calls,
            "literal_census": literal_census,
        },
        "decoy_fixture": run_decoys(),
    }
    Path(args.out).write_text(json.dumps(report, indent=2, sort_keys=True))
    print("wrote %s" % args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
