#!/usr/bin/env python3
"""Kb82E09Loader — control-world cross-check: frozen verifier vs independent probe.

Runs verify_surfaces.extract_classes (imported read-only from the scratch
clone at base 47dbe878) on the live 18.14.0 strings dump and compares against
the independent probe's admitted extraction.  This is a control-world
agreement check, not a production after-score: no production file is read or
written, and the fleet tree is untouched.
"""
from __future__ import annotations

import json
import sys

sys.path.insert(0, "/fast/scratch/hyaku/kotoba-r82/Kb82E09Loader/clone/verifiers")
import verify_surfaces as vs  # noqa: E402

DUMP = "/fast/scratch/hyaku/kotoba-r82/Kb82E09Loader/build/omp-18.14.0.strings.txt"
BASE = "/fast/scratch/hyaku/kotoba-r82/Kb82E09Loader/build/surfaces-baseline.base.json"
PROBE = "/fast/scratch/hyaku/kotoba-r82/Kb82E09Loader/receipts/probe-output.json"


def main() -> int:
    dump = open(DUMP, encoding="utf-8", errors="replace").read()
    base = json.load(open(BASE))
    entries = [{
        "class_id": e["class_id"], "harness": e["harness"],
        "literal": e["literal"], "context_kind": e["context_kind"],
        "verdict": e["verdict"], "reason": e.get("reason") or "",
    } for e in base["classes"]]
    declared = vs.declared_loader_pairs(entries, "omp")
    got = vs.extract_classes(dump, "omp", declared=declared)
    mine = {tuple(p) for p in json.load(open(PROBE))["extracted_admitted_pairs"]}
    report = {
        "verifier_pairs": sorted([list(p) for p in got]),
        "probe_pairs": sorted([list(p) for p in mine]),
        "agree": got == mine,
        "agents_md_present": ("agents-md", "AGENTS.md") in got,
        "verifier_module": vs.__file__,
    }
    json.dump(report, sys.stdout, indent=1)
    print()
    return 0 if got == mine else 1


if __name__ == "__main__":
    sys.exit(main())
