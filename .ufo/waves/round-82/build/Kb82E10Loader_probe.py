#!/usr/bin/env python3
"""Kb82E10Loader independent extraction probe -- group claude-md (omp 18.14.0).

Seat Kb82E10Loader, Kotoba round 82, C1 freshness outside-guard.  This probe is
an INDEPENDENT implementation of the extraction grammar documented in
verifiers/verify_surfaces.py (module docstring lines 20-60, 189-248, 444-604):
written from the documentation, not by importing the gate.  It extracts the
`.md` registration-call shapes from a `strings -n 4` dump of the CURRENT host
ELF and reports the pairs/literals/anchors for group `claude-md`, then compares
the distinct pairs against verifiers/surfaces-baseline.json at base
47dbe8781657de563ff867caca6244d28e3db504.

Documented grammar (as implemented here, independently):
  call shape : <callee-ident>( <v>, <group>, "<file>.md" ) followed by , or )
               callee = ANY identifier (round-52 generic mode);
               group  = quoted [a-z0-9_-]+ literal OR identifier;
               file   = quoted [A-Za-z0-9_./-]+ ending .md.
  bindings   : var|let|const declarators and plain assignments
               <ident> = "<string>" (<=80 chars, no escapes) anywhere in dump.
  resolution : dump-wide first-seen table, drop-on-conflict (a name bound to
               two different strings dump-wide is unsettled there); a name the
               dump-wide table cannot settle is resolved from the binding
               table of the call's OWN module scope (spans delimited by
               source-path comment lines `// <path>.<ext>`); the dump-wide
               table wins wherever it has an entry.
  shadowing  : a group identifier that is a parameter of the nearest preceding
               function header in the call's own module span never resolves.
  unresolved : surface as <unresolved-var:NAME> -- never guessed.

Usage: probe.py DUMP BASELINE_JSON OUT_JSON [--cross-check EXTRACTOR_JSON]

Exit codes: 0 always (findings are data); malformed inputs exit 2.
"""
import argparse
import bisect
import json
import re
import sys
from collections import defaultdict

# --- grammar (independent restatement of the documented shapes) --------------
CALL_SHAPE = re.compile(
    r"(?<![A-Za-z0-9_$.])([A-Za-z_$][A-Za-z0-9_$]*)"   # callee
    r"\(\s*[^\s,()]+\s*,\s*"                           # first arg <v>
    r"(?:\"([a-z0-9_-]+)\"|([A-Za-z_$][A-Za-z0-9_$]*))"  # group: quoted|ident
    r"\s*,\s*"
    r"\"([A-Za-z0-9_./-]+\.md)\"(?=\s*[,)])"           # file literal
)
ASSIGN = re.compile(
    r"(?<![A-Za-z0-9_$.])([A-Za-z_$][A-Za-z0-9_$]*)\s*=\s*\"([^\"\\\n]{1,80})\""
)
MODULE_MARKER = re.compile(r"^//[ \t]*\S+\.(?:[cm]?[jt]sx?)[ \t]*$", re.M)
PARAM_HEADER = re.compile(
    r"(?:async\s+)?function\s*[\w$]*\s*\(([^()]*)\)"
    r"|(?:\(([^()]*)\)|([A-Za-z_$][\w$]*))\s*=>"
)
CLASS_ID = re.compile(r"^(omp|opencode):([a-z0-9_-]+)/([A-Za-z0-9_./-]+)$")
GROUP_OF_INTEREST = "claude-md"
LITERAL_OF_INTEREST = "CLAUDE.md"


def line_index(text):
    offs = [0]
    for i, ch in enumerate(text):
        if ch == "\n":
            offs.append(i + 1)
    return offs


def lineno(offs, pos):
    return bisect.bisect_right(offs, pos)


def module_anchor(dump, spans, pos):
    """Nearest preceding source-path comment (module anchor) for pos."""
    best = None
    for m in MODULE_MARKER.finditer(dump):
        if m.start() > pos:
            break
        best = m
    if best is None:
        return {"module": "<dump-head:no-marker-before>", "marker_offset": None}
    return {"module": best.group(0).strip(), "marker_offset": best.start()}


def module_span_of(spans, pos):
    for i, (s, e) in enumerate(spans):
        if s <= pos < e or (i == len(spans) - 1 and pos >= s):
            return i, (s, e)
    return len(spans) - 1, spans[-1]


def constant_table(text):
    """First-seen wins; conflicting rebind dropped (unsettled)."""
    table, conflicts = {}, set()
    for name, val in ASSIGN.findall(text):
        if name in conflicts:
            continue
        if name in table and table[name] != val:
            conflicts.add(name)
            del table[name]
        else:
            table.setdefault(name, val)
    return table, conflicts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dump")
    ap.add_argument("baseline")
    ap.add_argument("out")
    ap.add_argument("--cross-check", default=None,
                    help="JSON from the gate's own extract_classes run")
    a = ap.parse_args()

    dump = open(a.dump, encoding="utf-8", errors="replace").read()
    offs = line_index(dump)
    base = json.load(open(a.baseline))
    entries = base["classes"]
    declared_pairs = set()
    baseline_claude = []
    for e in entries:
        m = CLASS_ID.match(e["class_id"])
        if m and e["harness"] == "omp":
            declared_pairs.add((m.group(2), m.group(3)))
        if m and e["harness"] == "omp" and m.group(2) == GROUP_OF_INTEREST:
            baseline_claude.append(e)
    baseline_claude_pairs = {(m.group(2), m.group(3))
                             for e in baseline_claude
                             for m in [CLASS_ID.match(e["class_id"])]}

    # module scopes
    spans = []
    start = 0
    for m in MODULE_MARKER.finditer(dump):
        spans.append((start, m.start()))
        start = m.end()
    spans.append((start, len(dump)))
    whole_dump_one_scope = len(spans) == 1

    global_table, global_conflicts = constant_table(dump)
    scope_tables = {}
    scope_conflicts = {}
    for i, (s, e) in enumerate(spans):
        t, c = constant_table(dump[s:e])
        scope_tables[i] = t
        scope_conflicts[i] = c

    calls = []
    for m in CALL_SHAPE.finditer(dump):
        callee, quoted, ident, filename = m.groups()
        span_i, (ss, se) = module_span_of(spans, m.start())
        shadowed = False
        params = set()
        if ident:
            for hm in PARAM_HEADER.finditer(dump[ss:m.start()]):
                if hm.group(3) is not None:
                    params = {hm.group(3)}
                else:
                    plist = hm.group(1) or hm.group(2)
                    params = {p.strip() for p in plist.split(",") if p.strip()} \
                        if plist else set()
            shadowed = ident in params
        resolution = None
        binding_ev = None
        if quoted:
            group, resolution = quoted, "quoted-literal"
        elif ident is None:
            group, resolution = "<parse-error>", "parse-error"
        else:
            if ident in global_conflicts or ident not in global_table:
                # dump-wide unsettled -> own module scope decides
                st = scope_tables[span_i]
                if ident in st and ident not in scope_conflicts[span_i]:
                    group, resolution = st[ident], "module-scope"
                    for bm in ASSIGN.finditer(dump[ss:se]):
                        if bm.group(1) == ident:
                            binding_ev = {
                                "name": ident, "value": bm.group(2),
                                "rel_offset": bm.start(),
                                "abs_offset": ss + bm.start(),
                                "line": lineno(offs, ss + bm.start()),
                                "scope_span": [ss, se],
                            }
                            break
                else:
                    group = "<unresolved-var:%s>" % ident
                    resolution = "unresolved"
            else:
                group, resolution = global_table[ident], "dump-wide"
            if shadowed and not group.startswith("<"):
                group = "<unresolved-var:%s>" % ident
                resolution = "param-shadowed"
        anchor = module_anchor(dump, spans, m.start())
        calls.append({
            "callee": callee, "group": group, "file": filename,
            "offset": m.start(), "line": lineno(offs, m.start()),
            "resolution": resolution,
            "param_shadowed": shadowed,
            "module": anchor["module"],
            "marker_offset": anchor["marker_offset"],
            "span_index": span_i,
            "binding": binding_ev,
        })

    all_pairs = sorted({(c["group"], c["file"]) for c in calls})
    claude_calls = [c for c in calls if c["group"] == GROUP_OF_INTEREST]
    claude_pairs = sorted({(c["group"], c["file"]) for c in claude_calls})
    unresolved_claude_files = sorted({c["file"] for c in calls
                                      if c["group"].startswith("<unresolved-var:")
                                      and c["file"] == LITERAL_OF_INTEREST})

    # literal anchors
    def literal_anchors(lit):
        pat = re.compile(re.escape('"' + lit + '"'))
        out = []
        for m in pat.finditer(dump):
            a2 = module_anchor(dump, spans, m.start())
            out.append({"line": lineno(offs, m.start()), "offset": m.start(),
                        "module": a2["module"]})
        return out

    claude_md_strings = literal_anchors(GROUP_OF_INTEREST)
    claude_file_strings = literal_anchors(LITERAL_OF_INTEREST)

    # decoys ---------------------------------------------------------------
    callees_claude = sorted({c["callee"] for c in claude_calls})
    callee_pair_map = defaultdict(set)
    for c in calls:
        callee_pair_map[c["callee"]].add((c["group"], c["file"]))
    claude_callee_other = {cal: sorted(callee_pair_map[cal] - {(GROUP_OF_INTEREST, p) for p in {c["file"] for c in claude_calls}})
                           for cal in callees_claude}
    # alias decoys: <ident> = <callee-ident> assignments for involved callees
    alias_hits = []
    for cal in callees_claude:
        for am in re.finditer(r"(?<![A-Za-z0-9_$.])([A-Za-z_$][A-Za-z0-9_$]*)\s*=\s*"
                              + re.escape(cal) + r"(?![A-Za-z0-9_$])", dump):
            alias_hits.append({"alias": am.group(1), "callee": cal,
                               "line": lineno(offs, am.start()),
                               "offset": am.start()})
    two_char_callees = sorted({c["callee"] for c in calls
                               if len(c["callee"]) <= 2})
    two_char_pairs = {tc: sorted(callee_pair_map[tc]) for tc in two_char_callees}
    # near-miss shapes mentioning the group but failing the grammar
    near_miss = []
    for m in re.finditer(re.escape('"' + GROUP_OF_INTEREST + '"'), dump):
        ctx = dump[max(0, m.start() - 160):m.end() + 160]
        if CALL_SHAPE.search(ctx) is None:
            a2 = module_anchor(dump, spans, m.start())
            near_miss.append({"line": lineno(offs, m.start()),
                              "offset": m.start(), "module": a2["module"],
                              "context": ctx.replace("\n", " ")[:200]})
    case_decoys = {}
    for variant in ("Claude-md", "CLAUDE-MD", "claude_md", "Claude-MD"):
        case_decoys[variant] = len(re.findall(re.escape(variant), dump))
    # non-.md claude-md call shapes (deliberately out of grammar)
    non_md = []
    for m in re.finditer(r"(?<![A-Za-z0-9_$.])([A-Za-z_$][A-Za-z0-9_$]*)\(\s*[^\s,()]+\s*,\s*\""
                         + GROUP_OF_INTEREST + r"\"\s*,\s*\"([^\"]+)\"(?=\s*[,)])", dump):
        if not m.group(2).endswith(".md"):
            non_md.append({"callee": m.group(1), "file": m.group(2),
                           "line": lineno(offs, m.start())})

    cross = None
    if a.cross_check:
        cross = json.load(open(a.cross_check))

    report = {
        "seat": "Kb82E10Loader",
        "dump": a.dump,
        "dump_bytes": len(dump),
        "dump_lines": len(offs),
        "module_markers": len(spans) - (0 if whole_dump_one_scope else 0),
        "whole_dump_one_scope": whole_dump_one_scope,
        "grammar": {
            "call_shape": CALL_SHAPE.pattern,
            "assign": ASSIGN.pattern,
            "module_marker": MODULE_MARKER.pattern,
        },
        "total_call_shapes": len(calls),
        "all_distinct_pairs_count": len(all_pairs),
        "all_distinct_pairs": all_pairs,
        "baseline_omp_declared_pairs": sorted(declared_pairs),
        "group_of_interest": GROUP_OF_INTEREST,
        "baseline_claude_rows": baseline_claude,
        "baseline_claude_pairs": sorted(baseline_claude_pairs),
        "claude_md_call_count": len(claude_calls),
        "claude_md_calls": claude_calls,
        "claude_md_distinct_pairs": claude_pairs,
        "claude_md_pairs_vs_baseline": {
            "extracted_minus_baseline": sorted(set(claude_pairs) - baseline_claude_pairs),
            "baseline_minus_extracted": sorted(baseline_claude_pairs - set(claude_pairs)),
            "match": set(claude_pairs) == baseline_claude_pairs,
        },
        "unresolved_var_calls_with_CLAUDE_md_file": [
            c for c in calls
            if c["group"].startswith("<unresolved-var:") and c["file"] == LITERAL_OF_INTEREST
        ],
        "literal_anchors": {
            GROUP_OF_INTEREST: claude_md_strings,
            LITERAL_OF_INTEREST: claude_file_strings,
        },
        "decoys": {
            "callees_registering_claude_md": callees_claude,
            "claude_callee_other_pairs": claude_callee_other,
            "alias_assignments_to_those_callees": alias_hits,
            "two_char_callees": two_char_callees,
            "two_char_callee_pairs": two_char_pairs,
            "near_miss_group_literals_outside_grammar": near_miss,
            "case_variant_counts": case_decoys,
            "non_md_claude_md_call_shapes": non_md,
        },
        "extracted_pairs_minus_baseline_declared": sorted(
            (g, f) for g, f in all_pairs
            if (g, f) not in declared_pairs and not g.startswith("<")),
        "cross_check": cross,
        "conflicts_dump_wide": sorted(global_conflicts),
    }
    with open(a.out, "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=1, sort_keys=False)
    # bounded console summary
    print("dump_lines=%d module_markers=%d one_scope=%s" %
          (len(offs), report["module_markers"], whole_dump_one_scope))
    print("total_call_shapes=%d distinct_pairs=%d" %
          (len(calls), len(all_pairs)))
    print("claude_md_calls=%d distinct_pairs=%s" %
          (len(claude_calls), claude_pairs))
    print("vs_baseline=%s" % report["claude_md_pairs_vs_baseline"])
    print("unresolved_with_CLAUDE.md=%d" %
          len(report["unresolved_var_calls_with_CLAUDE_md_file"]))
    print("callees=%s" % callees_claude)
    print("wrote %s" % a.out)


if __name__ == "__main__":
    sys.exit(main())
