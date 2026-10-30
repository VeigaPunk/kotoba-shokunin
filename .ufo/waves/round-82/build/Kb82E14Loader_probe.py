#!/usr/bin/env python3
"""Kb82E14Loader_probe.py — seat Kb82E14Loader, Kotoba round 82 (C1 freshness).

Independent extraction probe for ONE loader group ("windsurf", harness omp)
against the current host ELF ~/.local/bin/omp (omp 18.14.0), starting from the
documented extraction grammar of verifiers/verify_surfaces.py at base
47dbe8781657de563ff867caca6244d28e3db504 and a `strings -n 4` dump of the ELF.

The probe RE-IMPLEMENTS the documented grammar on its own (it does not import
the reference for its own result) and only then cross-checks its output against
the reference implementation's functions, so the two extraction paths stay
independent.  Everything is bounded: one dump file, precompiled patterns, one
process, stdlib only.  Per-module scope tables and nearest-preceding-header
lookups are precomputed once per dump (same semantics as the reference, which
recomputes them per call).

Documented grammar (base verify_surfaces.py, round-52 "declared" mode):
  dump        `strings -n 4 <binary>`
  scopes      module spans opened by `//<path>.[cm]?[jt]sx?` comment lines
  bindings    identifier -> string, first-seen wins, conflicting rebinds
              dropped (dump-wide table); per-module scope table as fallback;
              dump-wide table wins on overlap
  shadowing   a group identifier that is a parameter of the nearest preceding
              function header in the call's own module span never resolves
  call shape  <callee>(<v>, <group>, "<file>.md") — <group> quoted lowercase
              [a-z0-9_-]+ or identifier; lookahead `[,)]`; ANY callee, but a
              callee is ADMITTED only if one of its sites registers a pair the
              baseline declares for omp (any kind, class-id parsed); every pair
              of an admitted callee is extracted.  Unresolved-var groups can
              admit via a declared FILE.
Extension (clearly labeled, group-scoped): the same shape with a non-.md quoted
file arg, to witness non-md registrations of THIS group (the documented
extractor is .md-only by construction).

Outputs JSON: extraction result, baseline comparison, per-call anchors,
false-match decoy census, and the reference cross-check diff.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import sys
from bisect import bisect_right
from pathlib import Path

# --- documented grammar (semantics restated from base verify_surfaces.py) ----
MODULE_MARKER_RE = re.compile(r"^//[ \t]*\S+\.(?:[cm]?[jt]sx?)[ \t]*$", re.M)
ASSIGN_RE = re.compile(
    r'(?<![A-Za-z0-9_$.])([A-Za-z_$][A-Za-z0-9_$]*)\s*=\s*"([^"\\\n]{1,80})"'
)
PARAM_HEADER_RE = re.compile(
    r"(?:async\s+)?function\s*[\w$]*\s*\(([^()]*)\)"
    r"|(?:\(([^()]*)\)|([A-Za-z_$][\w$]*))\s*=>"
)
GENERIC_CALL_RE = re.compile(
    r"(?<![A-Za-z0-9_$.])([A-Za-z_$][A-Za-z0-9_$]*)\(\s*[^\s,()]+\s*,\s*"
    r'(?:"([a-z0-9_-]+)"|([A-Za-z_$][A-Za-z0-9_$]*))\s*,\s*'
    r'"([A-Za-z0-9_./-]+\.md)"(?=\s*[,)])'
)
# bounded group extension: same shape, any quoted file literal (not .md-only)
EXTENDED_CALL_RE = re.compile(
    r"(?<![A-Za-z0-9_$.])([A-Za-z_$][A-Za-z0-9_$]*)\(\s*[^\s,()]+\s*,\s*"
    r'(?:"([a-z0-9_-]+)"|([A-Za-z_$][A-Za-z0-9_$]*))\s*,\s*'
    r'"([A-Za-z0-9_./-]+)"(?=\s*[,)])'
)
CLASS_ID_RE = re.compile(r"^(omp|opencode):([a-z0-9_-]+)/([A-Za-z0-9_./-]+)$")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


class DumpCtx:
    """One-pass precomputation over the dump (same semantics as the reference
    implementation, which recomputes these per call)."""

    def __init__(self, dump: str) -> None:
        self.dump = dump
        self.global_table = self._constant_table(dump)
        self.spans = self._module_scopes(dump)
        self.markers = [(m.start(), m.group(0).strip())
                        for m in MODULE_MARKER_RE.finditer(dump)]
        self.marker_pos = [m[0] for m in self.markers]
        self.starts = [0] + [m.end() for m in re.finditer("\n", dump)]
        # nearest-preceding-header lookup: (header_start, params)
        self.header_pos: list[int] = []
        self.header_params: list[frozenset] = []
        for m in PARAM_HEADER_RE.finditer(dump):
            if m.group(3) is not None:
                params = frozenset({m.group(3)})
            else:
                plist = m.group(1) or m.group(2)
                params = frozenset(p.strip() for p in plist.split(",")
                                   if p.strip()) if plist else frozenset()
            self.header_pos.append(m.start())
            self.header_params.append(params)
        self._scope_cache: dict[int, dict] = {}

    @staticmethod
    def _constant_table(text: str) -> dict[str, str]:
        table: dict[str, str] = {}
        conflicts: set[str] = set()
        for name, value in ASSIGN_RE.findall(text):
            if name in conflicts:
                continue
            if name in table and table[name] != value:
                conflicts.add(name)
                del table[name]
            else:
                table.setdefault(name, value)
        return table

    @staticmethod
    def _module_scopes(dump: str) -> list[tuple[int, int]]:
        spans: list[tuple[int, int]] = []
        start = 0
        for m in MODULE_MARKER_RE.finditer(dump):
            spans.append((start, m.start()))
            start = m.end()
        spans.append((start, len(dump)))
        return spans

    def scope_index(self, pos: int) -> int:
        lo, hi = 0, len(self.spans) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if self.spans[mid][0] <= pos:
                lo = mid
            else:
                hi = mid - 1
        return lo

    def scope_table(self, idx: int) -> dict:
        if idx not in self._scope_cache:
            start, end = self.spans[idx]
            self._scope_cache[idx] = {} if (start == 0 and end == len(self.dump)) \
                else self._constant_table(self.dump[start:end])
        return self._scope_cache[idx]

    def param_shadowed(self, pos: int, ident: str) -> bool:
        idx = self.scope_index(pos)
        module_start = self.spans[idx][0]
        # nearest preceding header at or before pos, at or after module start;
        # the reference keeps ONLY the last header's params per call site
        i = bisect_right(self.header_pos, pos) - 1
        if i < 0 or self.header_pos[i] < module_start:
            return False
        return ident in self.header_params[i]

    def line_no(self, pos: int) -> int:
        return bisect_right(self.starts, pos)

    def module_anchor(self, pos: int) -> str:
        if not self.markers:
            return "<no module marker: whole-dump scope>"
        idx = bisect_right(self.marker_pos, pos) - 1
        return self.markers[idx][1] if idx >= 0 else \
            "<no module marker: whole-dump scope>"


def extract_all(ctx: DumpCtx, declared: set[tuple[str, str]],
                pattern: "re.Pattern[str]") -> dict:
    """The documented round-52 admission rule over the WHOLE dump (all groups),
    implemented independently."""
    dump = ctx.dump
    calls: list[dict] = []
    raw: list[tuple[str, str, str, str]] = []
    for m in pattern.finditer(dump):
        callee, quoted, ident, filename = m.groups()
        idx = ctx.scope_index(m.start())
        consts = {**ctx.scope_table(idx), **ctx.global_table}
        shadowed = False
        if quoted:
            group, how = quoted, "quoted"
        elif ident in consts and not ctx.param_shadowed(m.start(), ident):
            group, how = consts[ident], "identifier-resolved"
        else:
            shadowed = ident in consts  # bound, but shadowed by a parameter
            group, how = "<unresolved-var:%s>" % ident, "unresolved"
        raw.append((callee, group, filename))
        calls.append({
            "callee": callee,
            "group": group,
            "file": filename,
            "how": how,
            "shadowed_binding": shadowed,
            "line": ctx.line_no(m.start()),
            "offset": m.start(),
            "module": ctx.module_anchor(m.start()),
        })
    declared_files = {f for _, f in declared}
    admitted = {c for c, g, f in raw
                if (g, f) in declared
                or (g.startswith("<unresolved-var:") and f in declared_files)}
    extracted = {(g, f) for c, g, f in raw if c in admitted}
    return {
        "calls": calls,
        "admitted_callees": sorted(admitted),
        "extracted_pairs": sorted(extracted),
        "declared_pairs_used_for_admission": sorted(declared),
    }


def declared_pairs(entries: list[dict], harness: str) -> set[tuple[str, str]]:
    out: set[tuple[str, str]] = set()
    for e in entries:
        if e.get("harness") != harness:
            continue
        m = CLASS_ID_RE.match(e.get("class_id", ""))
        if m:
            out.add((m.group(2), m.group(3)))
    return out


DECOY_RULES = [
    ("registration-call-shape",
     re.compile(r'\(\s*[^\s,()]+\s*,\s*("windsurf"|[A-Za-z_$][\w$]*)\s*,\s*"')),
    ("description-string", re.compile(r'description:\s*"[^"]*[Ww]indsurf')),
    ("env-or-telemetry-ident", re.compile(r'WINDSURF_|hasUsedWindsurf|'
                                          r'windsurfProTrialEndTime')),
    ("enum-mapping", re.compile(r'\[\["?WINDSURF')),
    ("chunk-path", re.compile(r'windsurf-cpgn0s20\.js|/\$bunfs/root/chunks/')),
    ("module-map-key", re.compile(r'@oh-my-pi/pi-coding-agent/discovery/windsurf')),
    ("module-marker", re.compile(r'^//\s*\S*windsurf\.ts\s*$')),
    ("identifier-binding", re.compile(r'=\s*"[Ww]indsurf"')),
    ("provider-set-literal", re.compile(r'^\s*windsurf:\s*')),
    ("prose-mention", re.compile(r'[Ww]indsurf')),
]


def decoy_census(dump: str, group: str) -> dict:
    hits: list[dict] = []
    other: list[int] = []
    for i, line in enumerate(dump.splitlines(), 1):
        if group.lower() not in line.lower():
            continue
        for label, rx in DECOY_RULES:
            if rx.search(line):
                hits.append({"line": i, "class": label, "text": line[:160]})
                break
        else:
            other.append(i)
            hits.append({"line": i, "class": "other", "text": line[:160]})
    counts: dict[str, int] = {}
    for h in hits:
        counts[h["class"]] = counts.get(h["class"], 0) + 1
    return {"total_lines_with_group_token": len(hits),
            "counts_by_class": dict(sorted(counts.items())),
            "hits": hits,
            "unclassified_lines": other}


def reference_crosscheck(ref_path: Path, baseline_path: Path, dump: str,
                         mine: set[tuple[str, str]]) -> dict:
    spec = importlib.util.spec_from_file_location("verify_surfaces_base", ref_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    baseline_entries = mod.load_baseline(baseline_path)
    declared = mod.declared_loader_pairs(baseline_entries, "omp")
    ref_pairs = mod.extract_classes(dump, "omp", declared=declared)
    out = {
        "reference_baseline_entries": len(baseline_entries),
        "reference_declared_omp_pairs": len(declared),
        "reference_extract_matches_probe": set(ref_pairs) == set(mine),
        "reference_extracted_count": len(ref_pairs),
        "probe_extracted_count": len(mine),
        "only_in_reference": sorted(set(ref_pairs) - set(mine)),
        "only_in_probe": sorted(set(mine) - set(ref_pairs)),
        "windsurf_pairs_in_reference": sorted(p for p in ref_pairs
                                              if p[0] == "windsurf"),
    }
    # bounded literal_present for the windsurf entries only
    ws_entries = [e for e in baseline_entries
                  if e["class_id"].startswith("omp:windsurf")]
    ok, detail = mod.check_literal_present(ws_entries, {"omp": dump},
                                           {"omp": set(ref_pairs)})
    out["reference_literal_present_windsurf_ok"] = ok
    out["reference_literal_present_windsurf_detail"] = detail
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dump", required=True)
    ap.add_argument("--baseline", required=True)
    ap.add_argument("--group", default="windsurf")
    ap.add_argument("--reference", required=True,
                    help="path to a copy of base verify_surfaces.py")
    ap.add_argument("--out", required=True)
    args = ap.parse_args(argv)

    dump_path = Path(args.dump)
    dump = dump_path.read_text(encoding="utf-8", errors="replace")
    baseline = json.loads(Path(args.baseline).read_text(encoding="utf-8"))
    entries = baseline["classes"]

    omp_declared = declared_pairs(entries, "omp")
    group_declared = sorted(p for p in omp_declared if p[0] == args.group)

    ctx = DumpCtx(dump)

    # Pass A: documented grammar (.md call shapes), admission over whole dump
    full_a = extract_all(ctx, omp_declared, GENERIC_CALL_RE)
    group_pairs_a = sorted(p for p in full_a["extracted_pairs"] if p[0] == args.group)
    group_calls_a = [c for c in full_a["calls"]
                     if c["group"] == args.group and c["callee"] in
                     set(full_a["admitted_callees"])]

    # Pass B: bounded extension (any quoted file literal), group-scoped
    full_b = extract_all(ctx, omp_declared, EXTENDED_CALL_RE)
    group_pairs_b = sorted(p for p in full_b["extracted_pairs"] if p[0] == args.group)
    group_calls_b = [c for c in full_b["calls"]
                     if c["group"] == args.group and c["callee"] in
                     set(full_b["admitted_callees"])]

    decoys = decoy_census(dump, args.group)
    cross = reference_crosscheck(Path(args.reference), Path(args.baseline),
                                 dump, set(full_a["extracted_pairs"]))

    # baseline literal presence for the group's declared classes
    literal_probe = {}
    for e in entries:
        if e["harness"] == "omp" and e["class_id"].split(":")[1] \
                .split("/")[0] == args.group:
            literal_probe[e["class_id"]] = {
                "literal": e["literal"],
                "context_kind": e["context_kind"],
                "occurrences_in_dump": dump.count(e["literal"]),
            }

    result = {
        "seat": "Kb82E14Loader",
        "round": 82,
        "group": args.group,
        "harness": "omp",
        "inputs": {
            "dump_path": str(dump_path),
            "dump_sha256": sha256_file(dump_path),
            "dump_lines": dump.count("\n") + 1,
            "baseline_path": str(Path(args.baseline).resolve()),
            "baseline_classes": len(entries),
            "reference_grammar_path": str(Path(args.reference).resolve()),
        },
        "declared_pairs_for_group": group_declared,
        "documented_pass": {
            "extracted_pairs_for_group": group_pairs_a,
            "extracted_pairs_all_groups": full_a["extracted_pairs"],
            "admitted_callees_all_groups": full_a["admitted_callees"],
            "calls_for_group": group_calls_a,
            "distinct_pairs_only_in_extraction":
                sorted(p for p in group_pairs_a if p not in set(group_declared)),
            "distinct_pairs_only_in_baseline":
                sorted(p for p in group_declared if p not in set(group_pairs_a)),
        },
        "extended_pass_non_md": {
            "note": "beyond the documented .md-only grammar; group-scoped "
                    "witness of non-md registrations",
            "extracted_pairs_for_group": group_pairs_b,
            "calls_for_group": group_calls_b,
        },
        "baseline_literal_probe": literal_probe,
        "decoy_census": decoys,
        "reference_crosscheck": cross,
    }
    out_path = Path(args.out)
    out_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n",
                        encoding="utf-8")

    print("group:", args.group)
    print("declared pairs:", group_declared)
    print("extracted (.md, documented):", group_pairs_a)
    print("extracted (extended, non-.md):", group_pairs_b)
    print("admitted callees (all groups):", full_a["admitted_callees"])
    print("only in extraction:", result["documented_pass"]
          ["distinct_pairs_only_in_extraction"])
    print("only in baseline:", result["documented_pass"]
          ["distinct_pairs_only_in_baseline"])
    print("reference cross-check:", cross["reference_extract_matches_probe"],
          "|", cross["reference_literal_present_windsurf_detail"])
    print("decoy counts:", decoys["counts_by_class"])
    print("json ->", out_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
