#!/usr/bin/env python3
"""Kb82C04FalseRed attack harness.

Attacks verify_surfaces.py (base 47dbe878) parser/input narrowing across six
axes: quoted-vs-variable groups, repeated module vars, unresolved vars,
renamed callees, non-md registrations, decoys. Each case runs the REAL gate
functions imported from the base clone. A case is a GATE DEFECT when observed
behavior diverges from the gate's own documented semantics (module docstring
lines 20-60, code comments at extract_classes/constant_table/scope_table/
param_shadowed, self-test arms).

Expectation tags:
  LOUD   - gate fails loudly (documented or acceptable)
  TRADE  - documented limit / accepted tradeoff, evidence recorded
  HOLE   - fail-open divergence: documented semantics say the input must
           surface, and it silently vanishes (or a non-registration is
           admitted as provenance)
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

CLONE = Path("/fast/scratch/hyaku/kotoba-r82/Kb82C04FalseRed/corrected_pkg")
LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
DUMP = LANE / ".ufo/waves/round-82/build/Kb82E12Loader-omp-18.14.0-strings.txt"

spec = importlib.util.spec_from_file_location(
    "verify_surfaces", CLONE / "verify_surfaces.py")
vs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vs)

baseline = vs.load_baseline(CLONE / "surfaces-baseline.json")
DECLARED = vs.declared_loader_pairs(baseline, "omp")
LOADER_GROUP_PAIRS = {(e["group"], e["file"]) for e in baseline
                      if e["harness"] == "omp" and e["context_kind"] == "loader-group"}

results = []

def rec(axis, case, expect, observed, verdict, detail=""):
    results.append({
        "axis": axis, "case": case, "expectation": expect,
        "verdict": verdict,  # LOUD | TRADE | HOLE | OK
        "observed": observed, "detail": detail,
    })

def extract(dump_text, declared=None):
    return vs.extract_classes(dump_text, "omp",
                              DECLARED if declared is None else declared)

# ---------------------------------------------------------------- axis 1
# 1a. quoted group + variable group from the same admitted callee both extract
t1a = ('// m1.ts\nvar nD = "agents-md";\n'
       'F9(u, nD, "AGENTS.md");\n'
       'F9(u, "claude-md", "CLAUDE.md");\n')
p1a = extract(t1a)
rec("quoted-vs-variable", "same callee mixes var group and quoted group",
    "LOUD", sorted(p1a), "OK" if p1a == {("agents-md", "AGENTS.md"), ("claude-md", "CLAUDE.md")} else "HOLE",
    "both pair forms extract from an admitted callee")

# 1b. dump-wide single binding (different value) overrides own-module binding
t1b = ('// other.ts\nvar nD = "agents-md-walkup";\n'
       '// m1.ts\nvar nD = "agents-md";\n'
       'F9(u, nD, "AGENTS.md");\n')
p1b = extract(t1b)
# dump-wide wins -> ("agents-md-walkup","AGENTS.md") which IS declared -> the
# real pair ("agents-md","AGENTS.md") goes missing. check_literal_present
# names it -> loud. Extraction level: pair replaced, not silent.
missed_real = ("agents-md", "AGENTS.md") not in p1b
wrong_declared = ("agents-md-walkup", "AGENTS.md") in p1b
rec("quoted-vs-variable", "cross-module different value cannot override own-module binding",
    "LOUD", sorted(p1b),
    "OK" if (not missed_real and not wrong_declared) else "HOLE",
    "drop-on-conflict fires dump-wide, so the global merge entry exists only "
    "when ALL dump bindings agree; own-module value then necessarily matches -- "
    "the docstring's 'dump-wide wins wherever it has an entry' is defensive-only")

# 1c. forward reference: binding AFTER the call inside one module
t1c = ('// m1.ts\nF9(u, nD, "AGENTS.md");\nvar nD = "agents-md";\n')
p1c = extract(t1c)
rec("quoted-vs-variable", "var bound after the call in same module (hoisting)",
    "LOUD", sorted(p1c),
    "OK" if ("agents-md", "AGENTS.md") in p1c else "HOLE",
    "constant table is order-independent within the scope")

# 1d. commented-out binding shadows real binding (comment line feeds ASSIGN_RE)
t1d = ('// m1.ts\n// var nD = "agents-md-walkup";\n'
       'var nD = "agents-md";\nF9(u, nD, "AGENTS.md");\n')
p1d = extract(t1d)
rec("quoted-vs-variable", "comment-line binding collides with real binding (same module)",
    "LOUD", sorted(p1d),
    "OK" if ("<unresolved-var:nD>", "AGENTS.md") in p1d else "HOLE",
    "comment binding + real binding in one module = scope conflict -> unresolved "
    "(loud); comment pollution can only over-conservatize, never mis-resolve")

# ---------------------------------------------------------------- axis 2
# 2a. one var, two calls, same module
t2a = ('// m1.ts\nvar nD = "agents-md";\n'
       'F9(u, nD, "AGENTS.md");\nAc(u, nD, "AGENTS.md");\n')
p2a = extract(t2a)
rec("repeated-module-vars", "same module var reused by two callees",
    "LOUD", sorted(p2a), "OK" if p2a == {("agents-md", "AGENTS.md")} else "HOLE")

# 2b. same var twice SAME value in one module -> no conflict
t2b = ('// m1.ts\nvar nD = "agents-md";\nvar nD = "agents-md";\n'
       'F9(u, nD, "AGENTS.md");\n')
p2b = extract(t2b)
rec("repeated-module-vars", "identical rebind in one module is not a conflict",
    "LOUD", sorted(p2b), "OK" if ("agents-md", "AGENTS.md") in p2b else "HOLE")

# 2c. same var, different values, different modules -> each call own-module
t2c = ('// a.ts\nvar Q$ = "one";\n// b.ts\nvar Q$ = "agents-md";\n'
       'F9(u, Q$, "AGENTS.md");\n')
# note: module marker repeats; spans split per marker, so 'var Q$ = "two"' and
# the call end up in the same span.
p2c = extract(t2c)
rec("repeated-module-vars", "own-module binding settles call despite other-module conflict",
    "LOUD", sorted(p2c),
    "OK" if ("agents-md", "AGENTS.md") in p2c else "HOLE",
    "b2h-settled semantics; a repeated marker between binding and call splits "
    "scopes and the call falls back to the (conflicted) global table -> "
    "unresolved, also loud")

# ---------------------------------------------------------------- axis 3
# 3a. unresolved var + DECLARED file -> must surface (b2j arm semantics)
t3a = ('// a.ts\nvar Z$ = "one";\n// b.ts\nvar Z$ = "two";\n'
       '// c.ts\nfunction f(u) { return Q(u, Z$, "CLAUDE.md"); }\n')
p3a = extract(t3a)
rec("unresolved-vars", "unresolved group + declared file surfaces",
    "LOUD", sorted(p3a),
    "OK" if ("<unresolved-var:Z$>", "CLAUDE.md") in p3a else "HOLE",
    "P4 admission: unresolved + declared_file admits the callee")

# 3b. HOLE candidate: unresolved var + UNDECLARED file + no declared sibling
t3b = ('// a.ts\nvar Z$ = "one";\n// b.ts\nvar Z$ = "two";\n'
       '// c.ts\nfunction f(u) { return Q(u, Z$, "BRANDNEW.md"); }\n')
p3b = extract(t3b)
rec("unresolved-vars", "unresolved group + NEW file + unadmitted callee VANISHES",
    "LOUD", sorted(p3b),
    "HOLE" if p3b == set() else "OK",
    "a genuinely new loader class with an unsettled group var and no admitted "
    "sibling call silently disappears: no_uncovered_class sees nothing, "
    "vacuity guard silent (other 8 pairs still extract), literal_present only "
    "covers declared rows")

# 3c. unresolved var + undeclared file + callee WITH declared sibling -> loud
t3c = ('// a.ts\nvar Z$ = "one";\n// b.ts\nvar Z$ = "two";\n'
       '// c.ts\nQ(u, "gemini", "GEMINI.md");\nQ(u, Z$, "BRANDNEW.md");\n')
p3c = extract(t3c)
rec("unresolved-vars", "unresolved+new file but callee has declared sibling",
    "LOUD", sorted(p3c),
    "OK" if ("<unresolved-var:Z$>", "BRANDNEW.md") in p3c else "HOLE",
    "admitted callee's unresolved pair extracts -> uncovered FAIL")

# ---------------------------------------------------------------- axis 4
# 4a. ASCII callee with $
t4a = 'd$(u, "agents-md", "AGENTS.md");\n'
p4a = extract(t4a)
rec("renamed-callees", "dollar-suffixed callee",
    "LOUD", sorted(p4a), "OK" if ("agents-md", "AGENTS.md") in p4a else "HOLE")

# 4b. non-ASCII (ES2015+) callee identifier
t4b = 'éc(u, "gemini", "GEMINI.md");\n'
p4b = extract(t4b)
rec("renamed-callees", "non-ASCII callee identifier",
    "LOUD", sorted(p4b),
    "TRADE" if p4b == set() else "OK",
    "OMP_GENERIC_CALL_RE identifier class is ASCII-only; alone it trips vacuity, "
    "alongside ASCII callees its pairs go missing -> literal_present loud; "
    "charset assumption not written into the documented grammar")

# 4c. keyword-shaped decoy text 'function(...)' matches as callee
t4c = 'function(u, "gemini", "GEMINI.md");\n'
p4c = extract(t4c)
rec("renamed-callees", "keyword decoy 'function(u,\"gemini\",\"GEMINI.md\")'",
    "LOUD", sorted(p4c),
    "TRADE" if ("gemini", "GEMINI.md") in p4c else "OK",
    "any-identifier admission has no reserved-word filter; a docs/test string "
    "with this text would mint provenance; not present in live dump (11 shapes)")

# ---------------------------------------------------------------- axis 5
# 5a. uppercase .MD file arg
t5a = 'ts(u, "github", "CONTRIBUTING.MD");\n'
p5a = extract(t5a)
rec("non-md-registrations", "uppercase .MD file arg",
    "LOUD", sorted(p5a),
    "TRADE" if p5a == set() else "OK",
    "file regex is lowercase-.md-only; case-insensitive-platform registration "
    "would be invisible; documented limit says '.md-suffixed' without case note")

# 5b. same shape, non-md file (the documented outside-set case)
t5b = 'Ac(u, "cursor", "rules");\nAc(u, "gemini", "settings.json");\n'
p5b = extract(t5b)
rec("non-md-registrations", "same-shape non-md registrations invisible",
    "LOUD", sorted(p5b),
    "TRADE" if p5b == set() else "OK",
    "by-design outside set; census hand-declares them; absence on a new binary "
    "must be documented, never silently dropped")

# ---------------------------------------------------------------- axis 6
# 6a. member call excluded (Q18)
p6a = extract('o.x(u, "agents-md", "AGENTS.md");\n')
rec("decoys", "member call o.x(...) excluded",
    "LOUD", sorted(p6a), "OK" if p6a == set() else "HOLE")

# 6b. alias decoy with undeclared pair
p6b = extract('q(u, "evil", "EVIL.md");\n')
rec("decoys", "undeclared alias decoy excluded",
    "LOUD", sorted(p6b), "OK" if p6b == set() else "HOLE")

# 6c. HOLE candidate: commented-out call of an admitted callee -> provenance
# from a comment line (real registration removed, comment remains)
t6c = ('// m1.ts\n// F9(u, "claude-md", "CLAUDE.md");\n')
p6c = extract(t6c)
# F9 not admitted (comment pair does extract as a shape? the regex matches the
# text after '// '), so the shape DOES match; callee F9 admitted via the
# commented pair -> pair extracts -> literal_present would PASS on a binary
# whose real registration was deleted but a comment line remains.
rec("decoys", "comment-line call shape of admitted callee extracts",
    "LOUD", sorted(p6c),
    "HOLE" if ("claude-md", "CLAUDE.md") in p6c else "OK",
    "regex is not line-anchored; a bundler-retained comment carrying the call "
    "text witnesses a loader that need not exist -> false provenance PASS")

# 6d. string-literal-embedded shape (quote-terminated decoy)
t6d = 'var s = "F9(u, \\"claude-md\\", \\"CLAUDE.md\\");";\n'
p6d = extract(t6d)
rec("decoys", "escaped-string-embedded shape",
    "LOUD", sorted(p6d),
    "OK" if ("claude-md", "CLAUDE.md") not in p6d else "TRADE",
    "escaped quotes break the shape; if matched it would be decoy provenance")

# ================================================================ live data
dump_text = DUMP.read_text(encoding="utf-8", errors="replace")
lines = dump_text.split("\n")

# L1: every OMP_GENERIC_CALL_RE shape: line, callee, module, comment?
shapes = []
cur_marker = None
line_offsets = []
off = 0
for ln, line in enumerate(lines, 1):
    line_offsets.append(off)
    off += len(line) + 1
for m in vs.OMP_GENERIC_CALL_RE.finditer(dump_text):
    ln = None
    import bisect
    ln = bisect.bisect_right(line_offsets, m.start())
    line_txt = lines[ln - 1] if ln else ""
    shapes.append({
        "line": ln, "callee": m.group(1), "group_var": m.group(3),
        "file": m.group(4), "line_is_comment": line_txt.lstrip().startswith("//"),
        "line_text": line_txt.strip()[:120],
    })
rec("live-dump", "all generic call shapes on frozen 18.14.0 dump",
    "11 shapes, none on comment lines, all in src/discovery",
    shapes,
    "OK" if (len(shapes) == 11 and not any(s["line_is_comment"] for s in shapes)) else "HOLE",
    "frozen dump sha256 81277d3572277febcaf0853f10cf8778c64920f58a13fba98ef0accbb70a8319")

# L2: callees observed
callees = {}
for s in shapes:
    callees.setdefault(s["callee"], 0)
    callees[s["callee"]] += 1
rec("live-dump", "callee census on frozen dump",
    "Ac/F9/ts expected; E01 artifact claims only ts,Ac",
    callees, "OK", "E01 loader-pairs parenthetical omits F9, the var-group callee")

# L3: loosened shape: any quoted third arg (find non-md invisible registrations)
LOOSE = re.compile(
    r"(?<![A-Za-z0-9_$.])([A-Za-z_$][A-Za-z0-9_$]*)\(\s*[^\s,()]+\s*,\s*"
    r'(?:"([a-z0-9_-]+)"|([A-Za-z_$][A-Za-z0-9_$]*))\s*,\s*"([^"\n]+)"(?=\s*[,)])')
loose_hits = []
for m in LOOSE.finditer(dump_text):
    third = m.group(4)
    if not third.endswith(".md"):
        ln = bisect.bisect_right(line_offsets, m.start())
        loose_hits.append({"line": ln, "callee": m.group(1),
                           "group": m.group(2) or m.group(3), "file": third,
                           "line_text": lines[ln - 1].strip()[:120]})
rec("live-dump", "non-md third-arg shapes (invisible set)",
    "data", loose_hits[:40], "OK", "count=%d" % len(loose_hits))

# L4: near-miss file args (.MD uppercase, spaces) anywhere as third-arg strings
near_md = re.compile(r'"[A-Za-z0-9_./ -]*\.MD"|"[A-Za-z0-9_./ -]+ [A-Za-z0-9_./ -]*\.md"')
nm = [bisect.bisect_right(line_offsets, m.start()) for m in near_md.finditer(dump_text)]
rec("live-dump", "case/space near-miss file literals",
    "data", nm[:20], "OK", "count=%d" % len(nm))

# L5: comment-line ASSIGN_RE matches (binding pollution vector)
comment_bindings = []
for m in vs.ASSIGN_RE.finditer(dump_text):
    ln = bisect.bisect_right(line_offsets, m.start())
    if lines[ln - 1].lstrip().startswith("//"):
        comment_bindings.append({"line": ln, "name": m.group(1),
                                 "value": m.group(2)[:60]})
rec("live-dump", "ASSIGN_RE matches on // comment lines",
    "data", comment_bindings[:30], "OK", "count=%d" % len(comment_bindings))

# L6: unresolved-var call shapes anywhere on the dump (all files)
unres = [s for s in shapes if s["group_var"]]
# resolve each like the gate does
spans = vs.module_scopes(dump_text)
gtab = vs.constant_table(dump_text)
unres_report = []
for s in shapes:
    if not s["group_var"]:
        continue
    pos = line_offsets[s["line"] - 1] + lines[s["line"] - 1].find(s["group_var"])
    consts = {**vs.scope_table(dump_text, spans, pos), **gtab}
    ident = s["group_var"]
    if ident in consts and not vs.param_shadowed(dump_text, spans, pos, ident):
        unres_report.append({"line": s["line"], "var": ident,
                             "resolved": consts[ident]})
    else:
        unres_report.append({"line": s["line"], "var": ident, "resolved": None})
rec("live-dump", "var-group shapes resolution on frozen dump",
    "nD,rD resolve", unres_report, "OK", "")

# L7: historical allowlist callee names at .md registration sites (frozen dump)
hist = vs.OMP_CALL_RE.findall(dump_text)
rec("live-dump", "historical allowlist callees at .md shapes (frozen dump)",
    "0 (renamed)", len(hist), "OK" if len(hist) == 0 else "HOLE", "")

out = {
    "declared_pair_count": len(DECLARED),
    "loader_group_pair_count": len(LOADER_GROUP_PAIRS),
    "results": results,
}
Path(sys.argv[1]).write_text(json.dumps(out, indent=1), encoding="utf-8")
holes = [r for r in results if r["verdict"] == "HOLE"]
trades = [r for r in results if r["verdict"] == "TRADE"]
print("cases=%d HOLE=%d TRADE=%d OK=%d" % (
    len(results), len(holes), len(trades),
    len(results) - len(holes) - len(trades)))
for h in holes:
    print("HOLE:", h["axis"], "-", h["case"])
print("wrote", sys.argv[1])
