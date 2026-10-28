#!/usr/bin/env python3
# Kb81S17ReceiptIndex-check.py -- presence gate for the round-81 w1 receipt index.
#
# Authority: plans/round-81.md (C1, C2, Frontier, Round shape, Receipt discipline,
# No-harm battery) and the 64 seat prompts in .ufo/waves/round-81/w1-spec.json.
# The canonical prose index is .ufo/waves/round-81/build/Kb81S17ReceiptIndex.md;
# this script only answers "does the named file exist yet", never "is it right".
#
# Run from the lane root:
#   python3 -B .ufo/waves/round-81/build/Kb81S17ReceiptIndex-check.py
#
# Exit status
#   0  every fixed-path blocking receipt and every proposed subject is present
#   1  at least one fixed-path blocking receipt is missing
#   2  fixed paths complete, but at least one proposed subject is missing
#   3  environment error (not run from the lane root / spec unreadable)
#
# Blocks in this file are lane-relative. A row may be a glob; a glob row is
# present iff at least one match exists. Presence is not correctness: a file
# that exists with wrong bytes passes this gate and fails its own counter.

import glob
import json
import os
import sys

LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
SPEC = ".ufo/waves/round-81/w1-spec.json"

# (path, blocking, group) -- concrete names the plan or a seat prompt pins.
FIXED = [
    # --- C1 before-values -------------------------------------------------
    (".ufo/waves/round-81/receipts/tipbattery-base-dot.txt", True, "C1"),
    (".ufo/waves/round-81/build/base-battery/01-tip-battery-dot.txt", True, "C1"),
    (".ufo/waves/round-81/build/base-battery/02-tip-battery-abs.txt", True, "C1"),
    (".ufo/waves/round-81/build/base-battery/03-gate-registry.txt", True, "C1"),
    (".ufo/waves/round-81/build/base-battery/04-assertion-floors.txt", True, "C1"),
    (".ufo/waves/round-81/build/base-battery/05-skill-checklist.txt", True, "C1"),
    (".ufo/waves/round-81/build/base-battery/06-corpus-integrity.txt", True, "C1"),
    (".ufo/waves/round-81/build/base-battery/07-corpus-independent.txt", True, "C1"),
    (".ufo/waves/round-81/build/base-battery/08-correction-sweep.txt", True, "C1"),
    (".ufo/waves/round-81/build/base-battery/09-census.txt", True, "C1"),
    (".ufo/waves/round-81/build/base-battery/index.txt", False, "C1"),
    (".ufo/waves/round-81/build/Kb81E10Battery.md", True, "C1"),
    (".ufo/waves/round-81/build/Kb81E11Receipts.txt", True, "C1"),
    # --- C1 instruments, manifest, erratum --------------------------------
    (".ufo/waves/round-81/build/Kb81E01Integrity.patch", True, "C1"),
    (".ufo/waves/round-81/build/Kb81E01Integrity.blob", True, "C1"),
    (".ufo/waves/round-81/build/Kb81E02Independent.patch", True, "C1"),
    (".ufo/waves/round-81/build/Kb81E03ExtManifest.json", True, "C1"),
    (".ufo/waves/round-81/build/Kb81E03ExtManifest-fetch.txt", True, "C1"),
    (".ufo/waves/round-81/build/Kb81E04Baseline.patch", True, "C1"),
    (".ufo/waves/round-81/build/Kb81E04Baseline.md", False, "C1"),
    (".ufo/waves/round-81/build/refresh-corpus-baseline.py", True, "C1"),
    (".ufo/waves/round-81/build/Kb81E05Erratum.patch", True, "C1"),
    (".ufo/waves/round-81/build/Kb81E05Erratum.sha256", True, "C1"),
    (".ufo/waves/round-81/build/Kb81E14PinAudit.md", True, "C1"),
    (".ufo/waves/round-81/build/Kb81E14PinAudit-base.txt", False, "C1"),
    (".ufo/waves/round-81/build/Kb81E15Order.md", False, "C1"),
    (".ufo/waves/round-81/build/Kb81E13FixtureGuard.md", False, "C1"),
    # --- C1 controls ------------------------------------------------------
    (".ufo/waves/round-81/build/c1_controls.py", False, "C1"),
    (".ufo/waves/round-81/build/c1_controls.txt", True, "C1"),
    (".ufo/waves/round-81/build/Kb81C01C1-*.txt", True, "C1"),
    (".ufo/waves/round-81/build/Kb81M01Instruments-*.txt", False, "C1"),
    (".ufo/waves/round-81/build/Kb81M02Battery-*.txt", False, "C1"),
    # --- C2 ---------------------------------------------------------------
    (".ufo/waves/round-81/snapshots/S249.md", True, "C2"),
    (".ufo/waves/round-81/snapshots/S249.fetch.json", True, "C2"),
    (".ufo/waves/round-81/build/Kb81R03Reopen-fetch.json", False, "C2"),
    (".ufo/waves/round-81/build/allowed-tools-sdk-round81.md", True, "C2"),
    (".ufo/waves/round-81/build/check_sdk_allowed_tools.py", True, "C2"),
    (".ufo/waves/round-81/build/Kb81E09C2Counter-selftest.txt", True, "C2"),
    (".ufo/waves/round-81/build/Kb81E09C2Counter-base.txt", True, "C2"),
    (".ufo/waves/round-81/build/c2_controls.py", False, "C2"),
    (".ufo/waves/round-81/build/c2_controls.txt", True, "C2"),
    (".ufo/waves/round-81/build/Kb81C02C2-*.txt", True, "C2"),
    (".ufo/waves/round-81/build/Kb81S05SourcesEdits.md", True, "C2"),
    (".ufo/waves/round-81/build/Kb81S11GateQuotes.md", True, "C2"),
    (".ufo/waves/round-81/build/Kb81S08ReadmeRows.md", True, "C2"),
    (".ufo/waves/round-81/build/Kb81S09SkillRule.md", True, "C2"),
    (".ufo/waves/round-81/build/Kb81S10Province.md", True, "C2"),
    (".ufo/waves/round-81/build/Kb81M03C2-*.txt", False, "C2"),
    # --- frontier ---------------------------------------------------------
    (".ufo/waves/round-81/receipts/census-before.txt", True, "frontier"),
    (".ufo/waves/round-81/build/Kb81E12Census.txt", True, "frontier"),
    (".ufo/waves/round-81/build/Kb81S16CensusLog.md", True, "frontier"),
    (".ufo/waves/round-81/build/Kb81E16Shokuknow-slice.txt", True, "frontier"),
    (".ufo/waves/round-81/build/Kb81E16Shokuknow-collisions.txt", True, "frontier"),
    (".ufo/waves/round-81/build/Kb81S12AssimDisp.md", True, "frontier"),
    (".ufo/waves/round-81/build/Kb81R01NegSweep.md", False, "frontier"),
    # --- freeze / dispositions -------------------------------------------
    (".ufo/waves/round-81/build/Kb81S15FreezeShas.md", True, "freeze"),
    (".ufo/waves/round-81/receipts/freeze-shas.txt", True, "freeze"),
    (".ufo/waves/round-81/dispositions/wapes.txt", True, "freeze"),
    # --- report / lesson drafts ------------------------------------------
    (".ufo/waves/round-81/build/Kb81S01Lesson.md", True, "report"),
    (".ufo/waves/round-81/build/Kb81S02Log.md", True, "report"),
    (".ufo/waves/round-81/build/Kb81S03Scorecard.md", True, "report"),
    (".ufo/waves/round-81/build/Kb81S04Report.md", True, "report"),
    (".ufo/waves/round-81/build/Kb81S06Shonen.md", True, "report"),
    (".ufo/waves/round-81/build/Kb81S07Quality.md", False, "report"),
    (".ufo/waves/round-81/build/Kb81S13L0.md", False, "report"),
    (".ufo/waves/round-81/build/Kb81S14WaveRegistry.md", True, "report"),
    (".ufo/waves/round-81/build/Kb81S17ReceiptIndex.md", True, "report"),
    (".ufo/waves/round-81/w1-results.json", True, "report"),
]

# Required receipts whose filenames the plan/seat prompts do NOT pin. The L1
# fixes the name at integration; until then the index proposes these.
SUBJECTS = [
    (".ufo/waves/round-81/build/Kb81E02Independent.blob", True,
     "composed git-blob sha of the E02-patched verify_corpus_independent.py (E6 pin input)"),
    (".ufo/waves/round-81/build/Kb81E05Erratum-counter.sha256", True,
     "sha256 of the amended verifiers/check_tip_battery.py (the freeze's claim bytes)"),
    (".ufo/waves/round-81/receipts/after-final-dot.txt", True,
     "tip battery --repo . at the landed tip (expect guards 5 of 5; 6 of 6; exit 0)"),
    (".ufo/waves/round-81/receipts/after-final-abs.txt", True,
     "tip battery absolute --repo <lane> at the landed tip (same expectation)"),
    (".ufo/waves/round-81/receipts/after-final-c2.txt", True,
     "sdk counter at the landed tip (expect documented 1 of 1, exit 0)"),
    (".ufo/waves/round-81/receipts/census-after.txt", True,
     "census after the SOURCES edits, with own exit and row count on the receipt"),
    (".ufo/waves/round-81/receipts/baseline-refresh.txt", True,
     "refresh-corpus-baseline.py run at the final pre-report commit + its JSON diff"),
    (".ufo/waves/round-81/receipts/sibling-census.txt", True,
     "check_sibling_census.py --skill SKILL.md (plan no-harm battery; not in run-battery.sh)"),
    (".ufo/waves/round-81/receipts/report-pointers.txt", True,
     "check_report_pointers.py --report .ufo/reports/round-81/kotoba.md at the report commit"),
]


def present(row):
    path = os.path.join(LANE, row)
    if "*" in row or "?" in row or "[" in row:
        return len(glob.glob(path)) > 0
    return os.path.isfile(path)


def main():
    if not os.path.isdir(LANE):
        print("check: lane root missing: %s" % LANE)
        return 3
    if not os.path.isfile(os.path.join(LANE, SPEC)):
        print("check: wave spec missing: %s" % SPEC)
        return 3
    try:
        spec = json.load(open(os.path.join(LANE, SPEC)))
        seats = [i["name"] for i in spec["items"]]
    except Exception as exc:  # noqa: BLE001 - report, never crash the wave
        print("check: cannot read %s: %s" % (SPEC, exc))
        return 3

    blocking_missing = []
    fixed_missing = 0
    for path, blocking, group in FIXED:
        ok = present(path)
        if not ok:
            fixed_missing += 1
            if blocking:
                blocking_missing.append((group, path))

    subject_missing = [
        (desc, path) for path, blocking, desc in SUBJECTS
        if blocking and not present(path)
    ]

    seat_missing = [n for n in seats
                    if not os.path.isfile(os.path.join(
                        LANE, ".ufo/waves/round-81/w1", n + ".md"))]

    print("check: lane=%s" % LANE)
    print("check: fixed rows=%d blocking=%d" % (
        len(FIXED), sum(1 for _, b, _ in FIXED if b)))
    print("check: fixed missing=%d blocking missing=%d" % (
        fixed_missing, len(blocking_missing)))
    for group, path in blocking_missing:
        print("MISSING[%s] %s" % (group, path))
    print("check: subjects=%d missing=%d" % (len(SUBJECTS), len(subject_missing)))
    for desc, path in subject_missing:
        print("SUBJECT %s -- %s" % (path, desc))
    print("check: seat reports %d/%d" % (len(seats) - len(seat_missing), len(seats)))

    if blocking_missing:
        return 1
    if subject_missing:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
