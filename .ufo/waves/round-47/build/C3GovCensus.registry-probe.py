#!/usr/bin/env python3
"""C3 governance erratum registry probe — ADVICE ARTIFACT, not a lane gate.

Demonstrates the failure modes a pinned, fail-closed erratum registry must
survive, using the production verifier's own extractor (no reimplementation):

  A. a registry keyed on (file, token, occurrence-ordinal, sha256 of the exact
     line text) binds across line drift (LOG.md 2112 -> 2111 across the r46
     merge) and still fails closed when the recorded absence stops being true;
  B. the governance gate is location-dependent: 24 of its 805 live subjects are
     `../` tokens that resolve only because the lane lives inside the fleet.

Usage:
  python3 -B C3GovCensus.registry-probe.py --repo <repo> [--json]
Exit 0 iff every dead subject is registered with a binding pin and no pin is
stale; 1 otherwise (fail-closed by construction).
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

FILES = ("LOG.md", "SCORECARD.md")

# The one erratum this probe pins. line_sha256 is derived, never hand-copied.
REGISTRY = [
    {
        "file": "LOG.md",
        "token": ".ufo/round-45/drafts/v10/post-r44-hunt.py",
        "ordinal": 1,
        # sha256 of the exact 873-char line; identical at 36ab0d3:2112 and
        # BASE:2111 (the r46 merge shifted the line number, not the text).
        "line_sha256":
            "7dcbf123313d46c469cab9f5dac2daa7567e54ac1ddf7cffdd1fd38c74200135",
        "reason": "round-45 replay runner was an untracked draft (sha256 "
                  "3a70d405… V10.md), pruned; line records its own absence",
    },
]


def load_verifier(repo: Path):
    spec = importlib.util.spec_from_file_location(
        "vsc", repo / "verifiers" / "verify_skill_checklist.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def line_sha(text: str) -> str:
    return hashlib.sha256(text.rstrip().encode("utf-8")).hexdigest()


def collect(repo: Path, mod) -> list[dict]:
    subjects: list[dict] = []
    for name in FILES:
        lines = (repo / name).read_text(encoding="utf-8").splitlines()
        found, _ = mod.citation_subjects(
            lines, source=name, exclude_quoted=True, exclude_schematic=True)
        for row in found:
            row["line_sha256"] = line_sha(lines[row["line"] - 1])
        subjects.extend(found)
    seen: dict[tuple[str, str], int] = {}
    for row in subjects:
        key = (row["source"], row["token"])
        seen[key] = seen.get(key, 0) + 1
        row["ordinal"] = seen[key]
    for row in subjects:
        row["resolves"] = mod.citation_resolve(row["token"], repo)
    return subjects


def evaluate(subjects: list[dict]) -> dict:
    dead = [s for s in subjects if not s["resolves"]]
    problems: list[str] = []
    for s in dead:
        cands = [e for e in REGISTRY
                 if e["file"] == s["source"] and e["token"] == s["token"]
                 and e["ordinal"] == s["ordinal"]]
        if not cands:
            problems.append("UNREGISTERED %s:%d %r"
                            % (s["source"], s["line"], s["token"]))
            continue
        if cands[0]["line_sha256"] != s["line_sha256"]:
            problems.append("PIN LOSES BINDING (line text changed): %s:%d %r"
                            % (s["source"], s["line"], s["token"]))
    for entry in REGISTRY:
        keys = {(s["source"], s["token"], s["ordinal"]): s for s in subjects}
        s = keys.get((entry["file"], entry["token"], entry["ordinal"]))
        if s is None:
            problems.append("ORPHAN entry (owner subject absent): %s %r#%d"
                            % (entry["file"], entry["token"], entry["ordinal"]))
        elif s["resolves"]:
            problems.append("STALE ERRATUM (path resolves again): %s:%d %r"
                            % (s["source"], s["line"], s["token"]))
    return {
        "live_subjects": len(subjects),
        "dead_subjects": [
            {"file": s["source"], "line": s["line"], "token": s["token"],
             "ordinal": s["ordinal"], "line_sha256": s["line_sha256"],
             "parent_relative": s["token"].startswith("../")}
            for s in dead],
        "problems": problems,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    repo = Path(args.repo).resolve()
    mod = load_verifier(repo)
    result = evaluate(collect(repo, mod))
    result["repo"] = str(repo)
    result["registry"] = REGISTRY
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print("live=%d dead=%d problems=%d"
              % (result["live_subjects"], len(result["dead_subjects"]),
                 len(result["problems"])))
        for p in result["problems"]:
            print("  " + p)
    return 0 if not result["problems"] else 1


if __name__ == "__main__":
    sys.exit(main())
