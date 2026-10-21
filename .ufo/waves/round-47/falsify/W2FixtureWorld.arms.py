#!/usr/bin/env python3
"""Run every fixture-driven self-test arm of verify_surfaces.py and report the
PER-CHECK status for each, so we can see whether an arm fails ONLY for the
reason its comment states or also for incidental co-failures."""
import json, subprocess, sys, os

REPO = sys.argv[1]
FX = os.path.join(REPO, "verifiers/fixtures/surfaces")
V = os.path.join(REPO, "verifiers/verify_surfaces.py")

CLEAN = dict(
    omp=os.path.join(FX, "strings-omp-clean.txt"),
    oc=os.path.join(FX, "strings-opencode-clean.txt"),
    base=os.path.join(FX, "baseline-clean.json"),
    inv=os.path.join(FX, "inventory-clean.md"),
)

ARMS = [
    # (arm, comment-in-verifier, overrides)
    ("clean", "(a) clean fixture set -> exit 0, all checks PASS", {}),
    ("literal-drift", "(d2b) census row literal drifted -> exit 1, literal_parity",
     {"inv": "inventory-literal-drift.md"}),
    ("id-not-first", "(d2d) declared id outside first cell -> exit 1, literal_parity; table_parity PASS",
     {"inv": "inventory-id-not-first.md"}),
    ("missing-row", "(d) inventory drops a governed class-id row -> exit 1, table_parity",
     {"inv": "inventory-missing-row.md"}),
    ("extra-row", "(d2) inventory carries an extra class-id row -> exit 1, table_parity",
     {"inv": "inventory-extra-row.md"}),
    ("no-literal-cell", "(d2c) declared id whose row has no literal cell -> exit 1, literal_parity",
     {"inv": "inventory-no-literal-cell.md"}),
    ("missing-excluded-row", "(e2) excluded id absent from the inventory -> exit 1, excluded_reason",
     {"inv": "inventory-missing-excluded-row.md"}),
    ("rekind-doc", "(b4) baseline re-kinds omp loader-group rows to doc -> exit 1, no_uncovered_class",
     {"base": "baseline-rekind-doc.json", "inv": "inventory-rekind-doc.md"}),
    ("rekind-partial", "(b4) partial rekind -> exit 1, no_uncovered_class",
     {"base": "baseline-rekind-partial.json", "inv": "inventory-rekind-partial.md"}),
    ("excluded-noreason", "(e) excluded entry with empty reason -> exit 1, excluded_reason",
     {"base": "baseline-excluded-noreason.json"}),
    ("kind-drift-orphan", "NOT REFERENCED by the self-test (orphan fixture)",
     {"inv": "inventory-kind-drift.md"}),
]


def run(cfg, checks=None):
    args = [sys.executable, V, "--repo", FX,
            "--omp-strings", cfg["omp"], "--opencode-strings", cfg["oc"],
            "--baseline", cfg["base"], "--inventory", cfg["inv"], "--json"]
    for c in (checks or []):
        args += ["--check", c]
    p = subprocess.run(args, capture_output=True, text=True)
    try:
        data = json.loads(p.stdout)
    except Exception:
        return {"_exit": p.returncode, "_stdout": p.stdout, "_stderr": p.stderr}
    data["_exit"] = p.returncode
    return data


out = {}
for arm, comment, ov in ARMS:
    cfg = dict(CLEAN)
    for k, v in ov.items():
        cfg[k] = os.path.join(FX, v)
    data = run(cfg)
    statuses = {c["id"]: c["status"] for c in data.get("checks", [])}
    details = {c["id"]: c["detail"] for c in data.get("checks", [])}
    out[arm] = {"comment": comment, "exit": data.get("_exit"), "statuses": statuses,
                "details": details, "raw": data}
    fails = [k for k, v in statuses.items() if v == "FAIL"]
    print("ARM %-22s exit=%s  FAILS=%s" % (arm, data.get("_exit"), fails or "none"))
    for k in fails:
        print("      %s -> %s" % (k, details[k][:400]))

json.dump(out, open(sys.argv[2], "w"), indent=2, sort_keys=True)
print("wrote", sys.argv[2])
