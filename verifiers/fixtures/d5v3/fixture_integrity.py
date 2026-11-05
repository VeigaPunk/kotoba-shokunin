#!/usr/bin/env python3
"""Fixture integrity gate for check_r86_routed_repairs_v3's --self-test.

Committed fixture (plans/round-89.md § C2 keeps the fixture definitions under
verifiers/fixtures/d5v3/).  The v3 self-test copies this file to
verifiers/verify_corpus_integrity.py inside a throwaway world repository under
the process TMPDIR and commits a MODE file at the repo root; MODE selects the
world this script reports, emitted in the --json shape of the real
verifiers/verify_corpus_integrity.py ({"observed": ..., "results": [...]}
with one PASS/DRIFT row per check):

  base            nine names; DRIFT on the five baseline reds (receipt world)
  healed          report_dead healed to 0/PASS (a healed red passes D5)
  added           commit_unresolvable 1->2 and commit_total 3->4: an added
                  integrity finding under already-red names (leg d5iii, the
                  r88 blindness v2 could not see)
  silenced        commit_unresolvable removed from the name list (leg d5i)
  renamed         commit_nonhash renamed corpus.pointers.renamed (leg d5i)
  newred          commit_nonhash PASS->DRIFT at 1 (a new red name; leg d5ii)
  rerecorded      the re-recorded-baseline world: every verdict PASS at the
                  same values; the world also commits altered
                  corpus-baseline.json bytes, which only the snapshot leg
                  may catch
  brokenselftest  valid base JSON, but --self-test exits 1 (the d5i conjunct)
  garbage         stdout is not JSON (could-not-evaluate)

Read-only: no writes, no network, no lane reads.
"""
from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MODE = "base"
_mode_file = ROOT / "MODE"
if _mode_file.is_file():
    MODE = _mode_file.read_text(encoding="utf-8").strip() or "base"

# name -> (value, mode, expected); the five baseline reds carry DRIFT.
TABLE = {
    "corpus.index.tracked_files": (7, "equal", 4),
    "corpus.index.unindexed": (0, "zero", "0 / empty"),
    "corpus.index.stale_patterns": (0, "zero", "0 / empty"),
    "corpus.index.missing_paths": (0, "zero", "0 / empty"),
    "corpus.pointers.report_total": (3, "equal", 1),
    "corpus.pointers.report_dead": (1, "zero", "0 / empty"),
    "corpus.pointers.commit_total": (3, "equal", 1),
    "corpus.pointers.commit_unresolvable": (1, "zero", "0 / empty"),
    "corpus.pointers.commit_nonhash": (0, "zero", "0 / empty"),
}
RED = {
    "corpus.index.tracked_files",
    "corpus.pointers.report_total",
    "corpus.pointers.report_dead",
    "corpus.pointers.commit_total",
    "corpus.pointers.commit_unresolvable",
}


def rows() -> list[dict]:
    out: list[dict] = []
    for name, (value, mode, expected) in TABLE.items():
        observed = value
        verdict = "DRIFT" if name in RED else "PASS"
        if MODE == "healed" and name == "corpus.pointers.report_dead":
            observed, verdict = 0, "PASS"
        elif MODE == "added" and name == "corpus.pointers.commit_unresolvable":
            observed = 2
        elif MODE == "added" and name == "corpus.pointers.commit_total":
            observed = 4
        elif MODE == "newred" and name == "corpus.pointers.commit_nonhash":
            observed, verdict = 1, "DRIFT"
        elif MODE == "rerecorded":
            verdict = "PASS"
            if mode == "equal":
                expected = observed
        out.append({"check": name, "mode": mode, "observed": observed,
                    "expected": expected, "verdict": verdict})
    if MODE == "silenced":
        out = [r for r in out
               if r["check"] != "corpus.pointers.commit_unresolvable"]
    if MODE == "renamed":
        for row in out:
            if row["check"] == "corpus.pointers.commit_nonhash":
                row["check"] = "corpus.pointers.renamed"
    return out


def main() -> int:
    if MODE == "garbage":
        print("integrity noise, definitely not json")
        return 0
    if "--self-test" in sys.argv[1:]:
        print("%s fixture: self-test %s"
              % (MODE, "fails by declaration" if MODE == "brokenselftest"
                 else "holds"))
        return 1 if MODE == "brokenselftest" else 0
    doc = {"observed": {"corpus": {"fixture_mode": MODE}},
           "results": rows()}
    print(json.dumps(doc, indent=2))
    return 1 if any(r["verdict"] == "DRIFT" for r in doc["results"]) else 0


if __name__ == "__main__":
    sys.exit(main())
