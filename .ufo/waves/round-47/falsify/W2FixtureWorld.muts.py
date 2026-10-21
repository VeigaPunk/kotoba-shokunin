#!/usr/bin/env python3
"""Mutation tests against the round-47 surfaces fixtures.

Each mutation is applied to a COPY of the clean fixture in a scratch dir; the
verifier is pointed at the mutated copies.  We record the FULL per-check status
so we can see whether a mutation is (a) caught by the check that owns it,
(b) caught only incidentally, or (c) NOT caught at all (escape).
"""
import json, os, re, shutil, subprocess, sys

REPO = sys.argv[1]
OUT = sys.argv[2]
FX = os.path.join(REPO, "verifiers/fixtures/surfaces")
V = os.path.join(REPO, "verifiers/verify_surfaces.py")
WORK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mutwork")
shutil.rmtree(WORK, ignore_errors=True)
os.makedirs(WORK)

CHECKS = ["surfaces.literal_present", "surfaces.no_uncovered_class",
          "surfaces.opencode_extract", "surfaces.table_parity",
          "surfaces.literal_parity", "surfaces.kind_parity",
          "surfaces.excluded_reason"]


def load(p):
    return open(os.path.join(FX, p)).read()


def run(baseline, inventory, omp=None, oc=None):
    args = [sys.executable, V, "--repo", FX,
            "--omp-strings", omp or os.path.join(FX, "strings-omp-clean.txt"),
            "--opencode-strings", oc or os.path.join(FX, "strings-opencode-clean.txt"),
            "--baseline", baseline, "--inventory", inventory, "--json"]
    p = subprocess.run(args, capture_output=True, text=True)
    try:
        d = json.loads(p.stdout)
    except Exception:
        return {"exit": p.returncode, "err": p.stdout + p.stderr}
    return {"exit": p.returncode,
            "statuses": {c["id"]: c["status"] for c in d["checks"]},
            "details": {c["id"]: c["detail"] for c in d["checks"]}}


results = {}


def record(name, expectation, baseline, inventory, **kw):
    r = run(baseline, inventory, **kw)
    fails = [k for k, v in r.get("statuses", {}).items() if v == "FAIL"]
    results[name] = {"expectation": expectation, "exit": r.get("exit"), "fails": fails,
                     "statuses": r.get("statuses"), "details": r.get("details")}
    verdict = "OK " if set(fails) == set(expectation.get("fails", [])) else "MISS"
    print("%s %-26s exit=%s fails=%s  (expected %s)" %
          (verdict, name, r.get("exit"), fails or "none", expectation.get("fails") or "none"))
    for k in fails:
        print("        %s: %s" % (k, r["details"][k][:300]))


# ---------------------------------------------------------------- inventory mutations
inv = load("inventory-clean.md")
base = load("baseline-clean.json")

# M1: literal drift on a round-47 NEW opencode row (https:// -> http://)
m = inv.replace("| `opencode:config/instructions-remote` | https:// |",
                "| `opencode:config/instructions-remote` | http:// |")
assert m != inv
p1 = os.path.join(WORK, "m1.md"); open(p1, "w").write(m)
record("M1 literal-drift new-row",
       {"fails": ["surfaces.literal_parity"]}, os.path.join(FX, "baseline-clean.json"), p1)

# M2: kind drift on a round-47 NEW opencode row
m = inv.replace("| `opencode:read-hook/instructions` | <system-reminder> | loader-literal |",
                "| `opencode:read-hook/instructions` | <system-reminder> | loader-config |")
assert m != inv
p2 = os.path.join(WORK, "m2.md"); open(p2, "w").write(m)
record("M2 kind-drift new-row",
       {"fails": ["surfaces.kind_parity"]}, os.path.join(FX, "baseline-clean.json"), p2)

# M3: missing census row for a round-47 NEW opencode row
m = "\n".join(l for l in inv.splitlines()
              if not l.startswith("| `opencode:instructions/CONTEXT.md` |"))
assert m != inv
p3 = os.path.join(WORK, "m3.md"); open(p3, "w").write(m)
record("M3 missing-row new-row",
       {"fails": ["surfaces.table_parity"]}, os.path.join(FX, "baseline-clean.json"), p3)

# M4: extra census row
m = inv.replace("## Method notes",
                "| `opencode:instructions/GUIDE.md` | GUIDE.md | loader-literal | governed | injected |\n\n## Method notes")
assert m != inv
p4 = os.path.join(WORK, "m4.md"); open(p4, "w").write(m)
record("M4 extra-row new-id",
       {"fails": ["surfaces.table_parity"]}, os.path.join(FX, "baseline-clean.json"), p4)

# M5: VERDICT cell drift on a census row (no check compares census verdict to baseline)
m = inv.replace("| `opencode:config/instructions` | instructions | loader-config | governed |",
                "| `opencode:config/instructions` | instructions | loader-config | excluded |")
assert m != inv
p5 = os.path.join(WORK, "m5.md"); open(p5, "w").write(m)
record("M5 verdict-cell drift",
       {"fails": []}, os.path.join(FX, "baseline-clean.json"), p5)

# M6: single-row id-not-first (only one opencode row)
m = inv.replace("| `opencode:instructions/CONTEXT.md` | CONTEXT.md | loader-literal | governed | last priority list element |",
                "| CONTEXT.md | `opencode:instructions/CONTEXT.md` | loader-literal | governed | last priority list element |")
assert m != inv
p6 = os.path.join(WORK, "m6.md"); open(p6, "w").write(m)
record("M6 id-not-first one row",
       {"fails": ["surfaces.literal_parity"]}, os.path.join(FX, "baseline-clean.json"), p6)

# ---------------------------------------------------------------- joint baseline+census rekind
# M7: LAUNDERING ESCAPE — re-kind a round-47 NEW opencode row to `doc` in BOTH the
#     baseline fixture and the census fixture.
b = json.loads(base)
for e in b["classes"]:
    if e["class_id"] == "opencode:instructions/AGENTS.md":
        e["context_kind"] = "doc"
pb = os.path.join(WORK, "m7-base.json"); json.dump(b, open(pb, "w"), indent=2)
m = inv.replace("| `opencode:instructions/AGENTS.md` | AGENTS.md | loader-literal | governed |",
                "| `opencode:instructions/AGENTS.md` | AGENTS.md | doc | governed |")
assert m != inv
p7 = os.path.join(WORK, "m7.md"); open(p7, "w").write(m)
record("M7 joint rekind opencode->doc",
       {"fails": ["surfaces.no_uncovered_class"]}, pb, p7)

# M8: control — same joint rekind on an omp row (the covered case)
b = json.loads(base)
for e in b["classes"]:
    if e["class_id"] == "omp:cursor/rules":
        e["context_kind"] = "doc"
pb = os.path.join(WORK, "m8-base.json"); json.dump(b, open(pb, "w"), indent=2)
m = inv.replace("| `omp:cursor/rules` | rules | loader-literal | governed |",
                "| `omp:cursor/rules` | rules | doc | governed |")
assert m != inv
p8 = os.path.join(WORK, "m8.md"); open(p8, "w").write(m)
record("M8 joint rekind omp->doc",
       {"fails": ["surfaces.no_uncovered_class"]}, pb, p8)

# M9: baseline-only rekind of a NEW opencode row (census left alone)
b = json.loads(base)
for e in b["classes"]:
    if e["class_id"] == "opencode:instructions/AGENTS.md":
        e["context_kind"] = "doc"
pb = os.path.join(WORK, "m9-base.json"); json.dump(b, open(pb, "w"), indent=2)
record("M9 baseline-only rekind oc",
       {"fails": ["surfaces.kind_parity"]}, pb, os.path.join(FX, "inventory-clean.md"))

# M10: excluded row dropped from the census but a NEW excluded row added to the
#      baseline -> excluded_reason must name the NEW excluded id
b = json.loads(base)
b["classes"].append({"class_id": "opencode:config/instructions-remote",
                      "harness": "opencode", "literal": "https://",
                      "context_kind": "loader-config", "verdict": "excluded",
                      "reason": ""})
pb = os.path.join(WORK, "m10-base.json"); json.dump(b, open(pb, "w"), indent=2)
m = "\n".join(l for l in inv.splitlines()
              if not l.startswith("| `opencode:config/instructions-remote` |"))
p10 = os.path.join(WORK, "m10.md"); open(p10, "w").write(m)
record("M10 new excluded id missing",
       {"fails": ["surfaces.table_parity", "surfaces.excluded_reason"]}, pb, p10)

# M11: the census cell for <system-reminder> backticked (rendering fidelity)
m = inv.replace("| `opencode:read-hook/instructions` | <system-reminder> |",
                "| `opencode:read-hook/instructions` | `<system-reminder>` |")
assert m != inv
p11 = os.path.join(WORK, "m11.md"); open(p11, "w").write(m)
record("M11 backticked literal cell",
       {"fails": []}, os.path.join(FX, "baseline-clean.json"), p11)

json.dump(results, open(OUT, "w"), indent=2, sort_keys=True)
print("wrote", OUT)
