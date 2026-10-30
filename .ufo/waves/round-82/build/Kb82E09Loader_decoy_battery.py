#!/usr/bin/env python3
"""Kb82E09Loader — false-match decoy battery for the agents-md loader probe.

Each decoy is a synthetic strings-dump fragment fed through the SAME
extract()/admit() implementation as the live probe (build/loader_probe.py).
Expected results encode the documented grammar's discrimination contract.
"""
from __future__ import annotations

import importlib.util
import json
import sys

spec = importlib.util.spec_from_file_location(
    "loader_probe", "/fast/scratch/hyaku/kotoba-r82/Kb82E09Loader/build/loader_probe.py")
lp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lp)

DECLARED = {("agents-md", "AGENTS.md"), ("claude-md", "CLAUDE.md")}

DECOYS = {
    "d1_alias_callee_no_declared_pair": {
        "dump": '// mod/x.ts\nvar nD = "agents-md";\nq(u, "evil", "EVIL.md");\nF9(u, nD, "AGENTS.md");\n',
        "expect": {
            "sweep_pairs": [["agents-md", "AGENTS.md"], ["evil", "EVIL.md"]],
            "extracted": [["agents-md", "AGENTS.md"]],
            "admitted": ["F9"],
            "why": "alias decoy callee q registers no declared pair -> never admitted",
        },
    },
    "d2_param_shadowed_group": {
        "dump": '// mod/x.ts\nvar nD = "agents-md";\nfunction load(u, nD) { return F9(u, nD, "AGENTS.md"); }\n',
        "expect": {
            "sweep_pairs_raw": [["<unresolved-var:nD>", "AGENTS.md"]],
            "extracted": [["<unresolved-var:nD>", "AGENTS.md"]],
            "admitted": ["F9"],
            "why": "group ident is a function parameter -> fail-closed unresolved, "
                   "surfaces via declared-file admission; NEVER resolves to agents-md",
        },
    },
    "d3_cross_module_rebind": {
        "dump": '// mod/a.ts\nvar nD = "agents-md";\n// mod/b.ts\nvar nD = "title";\nF9(u, nD, "AGENTS.md");\n',
        "expect": {
            "sweep_pairs": [["title", "AGENTS.md"]],
            "extracted": [],
            "admitted": [],
            "why": "call sits in b.ts whose own module binds nD='title'; "
                   "dump-wide table drops the conflict; module scope wins -> "
                   "no false agents-md match, no admission (pair undeclared)",
        },
    },
    "d4_non_md_file": {
        "dump": '// mod/x.ts\nvar nD = "agents-md";\nF9(u, nD, "rules");\n',
        "expect": {
            "sweep_pairs": [],
            "extracted": [],
            "admitted": [],
            "why": "file arg lacks .md suffix -> outside the documented set "
                   "(the cursor/rules class is declared by hand, never extracted)",
        },
    },
    "d5_quoted_group_positive": {
        "dump": '// mod/x.ts\nF9(u, "agents-md", "AGENTS.md");\n',
        "expect": {
            "sweep_pairs": [["agents-md", "AGENTS.md"]],
            "extracted": [["agents-md", "AGENTS.md"]],
            "admitted": ["F9"],
            "why": "positive control: quoted group literal matches directly",
        },
    },
    "d6_no_module_markers_conflict": {
        "dump": 'var nD = "agents-md";\nvar nD = "title";\nF9(u, nD, "AGENTS.md");\n',
        "expect": {
            "sweep_pairs_raw": [["<unresolved-var:nD>", "AGENTS.md"]],
            "extracted": [["<unresolved-var:nD>", "AGENTS.md"]],
            "admitted": ["F9"],
            "why": "no source-path comments -> whole dump one scope -> conflicting "
                   "rebind stays unresolved (conservative fail, never guessed)",
        },
    },
    "d7_wrapped_call_shape": {
        "dump": '// mod/x.ts\nvar nD = "agents-md";\ns(F9(u, nD, "AGENTS.md"), "project", "text");\n',
        "expect": {
            "sweep_pairs": [["agents-md", "AGENTS.md"]],
            "extracted": [["agents-md", "AGENTS.md"]],
            "admitted": ["F9"],
            "why": "wrapped registration (the bundle norm) still matches the shape",
        },
    },
    "d8_property_lookup_not_call": {
        "dump": '// mod/x.ts\nvar nD = "agents-md";\nconst c = { reg: F9 };\nc.reg(u, nD, "AGENTS.md");\n',
        "expect": {
            "sweep_pairs": [],
            "extracted": [],
            "admitted": [],
            "why": "member-expression callee (c.reg) is rejected by the "
                   "(?<![A-Za-z0-9_$.]) lookbehind: the grammar admits bare "
                   "identifier callees only, so an alias property never feeds "
                   "the extractor",
        },
    },
}


def run():
    results = []
    failed = 0
    for name, case in DECOYS.items():
        calls, _, _ = lp.extract(case["dump"])
        _, admitted = lp.admit(calls, DECLARED)
        extracted = sorted([list(p) for p in {
            (c["group"], c["file"]) for c in calls if c["callee"] in admitted}])
        sweep = sorted([list(p) for p in {(c["group"], c["file"]) for c in calls}])
        exp = case["expect"]
        exp_sweep = exp.get("sweep_pairs", exp.get("sweep_pairs_raw"))
        checks = {
            "sweep_pairs": sweep == exp_sweep,
            "extracted": extracted == exp["extracted"],
            "admitted": sorted(admitted) == exp["admitted"],
        }
        ok = all(checks.values())
        failed += 0 if ok else 1
        results.append({
            "decoy": name, "ok": ok, "checks": checks,
            "observed": {"sweep": sweep, "extracted": extracted,
                         "admitted": sorted(admitted)},
            "expect": exp,
        })
    out = {"decoys": len(DECOYS), "failed": failed, "results": results}
    json.dump(out, sys.stdout, indent=1)
    print()
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(run())
