#!/usr/bin/env python3
"""Kb80S17ReceiptIndex-check — presence gate for every receipt the round-80 report and lesson cite.

Run from the lane root:
    cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
    python3 -B .ufo/waves/round-80/build/Kb80S17ReceiptIndex-check.py

Exit codes:
  0  every fixed-path blocking receipt AND every mandatory-subject receipt exists
  1  a fixed-path blocking receipt is missing (plan/prompt fix the path)
  2  fixed paths are complete, but a mandatory-subject receipt is missing under the
     canonical name proposed by Kb80S17ReceiptIndex.md (the L1 may write it under another
     name — then cite that name in the report and update this list; the subject itself is
     not optional)

The authority for a produced file's name is the producing seat's report in
.ufo/waves/round-80/w1/; this list is the canonical set the report/lesson may cite.
"""
import os
import sys

B = ".ufo/waves/round-80/build/"
R = ".ufo/waves/round-80/receipts/"
W = ".ufo/waves/round-80/w1/"

# Fixed paths: the plan or the producing seat's prompt names the file. Blocking = True
# means the report/lesson value it grounds has no other receipt.
REQUIRED = [
    # ---- base receipts (pre-freeze; committed at c2f69d4) ----
    ("B01", R + "tipbattery-base-dot.txt", True, "C1-base"),
    ("B02", R + "tipbattery-base-abs.txt", True, "C1-base"),
    ("B03", R + "census-before.txt", True, "FR-census"),
    ("B04", R + "census-after.txt", True, "FR-census"),
    ("B05", R + "census-final.txt", False, "FR-census"),
    ("B06", R + "m80-1-pipe-vs-direct.txt", True, "MISTAKE"),
    ("B07", R + "freeze-shas.txt", True, "C1+C2-freeze"),
    # ---- C1 repair/instrument artifacts ----
    ("C1p01", B + "Kb80E01Registry.patch", True, "C1-repair1"),
    ("C1p02", B + "Kb80E02Symlink.patch", True, "C1-repair2"),
    ("C1p03", B + "Kb80E03IndexBaseline.patch", True, "C1-repair3"),
    ("C1p04", B + "Kb80E04DeadPointer.patch", True, "C1-repair4"),
    ("C1p05", B + "Kb80E04DeadPointer.blob", True, "C1-pin"),
    ("C1p06", B + "Kb80E06CounterErratum.patch", True, "C1-erratum"),
    ("C1p07", B + "Kb80E06CounterErratum.sha256", True, "C1-freeze"),
    ("C1p08", B + "Kb80E05GrammarFix.blobs", True, "C1-pin"),
    ("C1p09", B + "run-battery.sh", True, "C1-runner"),
    ("C1p10", B + "Kb80E14C1Worlds.txt", True, "C1-controls"),
    ("C1p11", B + "Kb80E16PinAudit.txt", True, "C1-freeze"),
    ("C1p12", B + "Kb80E15BaselineOrder.md", True, "C1-integration"),
    ("C1p13", W + "Kb80E10Battery.md", False, "C1-stackworld"),
    # ---- C2 ----
    ("C2p01", B + "check_allowed_tools.py", True, "C2-counter"),
    ("C2p02", B + "allowed-tools-surfaces-round80.md", True, "C2-entry"),
    ("C2p03", B + "c2_controls.py", True, "C2-controls"),
    ("C2p04", B + "Kb80R03ReopenSix-S226.fetch.json", True, "C2-reopen"),
    ("C2p05", B + "Kb80R03ReopenSix-S227.fetch.json", True, "C2-reopen"),
    ("C2p06", B + "Kb80R03ReopenSix-S228.fetch.json", True, "C2-reopen"),
    ("C2p07", B + "Kb80R03ReopenSix-S229.fetch.json", True, "C2-reopen"),
    ("C2p08", B + "Kb80R03ReopenSix-S230.fetch.json", True, "C2-reopen"),
    ("C2p09", B + "Kb80R03ReopenSix-S231.fetch.json", True, "C2-reopen"),
    ("C2p10", W + "Kb80R03ReopenSix.md", True, "C2-reopen"),
    ("C2p11", ".ufo/waves/round-79/snapshots", True, "C2-pins"),
    ("C2p12", W + "Kb80E08C2Entry.md", False, "C2-entry-verify"),
    ("C2p13", W + "Kb80E07C2Counter.md", False, "C2-counter-verify"),
    # ---- frontier / assimilation / census ----
    ("FR01", B + "Kb80R01NegSweep.md", True, "FR-neg"),
    ("FR02", B + "Kb80R01NegSweep-admit.md", False, "FR-neg"),
    ("FR03", B + "Kb80S05SourcesEdits.md", True, "FR-edits"),
    ("FR04", B + "Kb80S11GateQuotes.md", True, "FR-quotes"),
    ("FR05", B + "Kb80S16CensusLog.md", True, "FR-edits"),
    ("FR06", B + "Kb80E12Census.txt", True, "FR-census"),
    ("FR07", B + "Kb80R06ShokuknowSlice.md", True, "FR-assim"),
    ("FR08", B + "Kb80K03Considerthese.md", True, "FR-assim"),
    ("FR09", B + "Kb80R07ClosureScan.md", True, "LC-routed"),
    ("FR10", B + "Kb80R05FleetGrammar.md", False, "FR-q75"),
    ("FR11", B + "Kb80R04SiblingScan.md", False, "FR-adjacency"),
    ("FR12", B + "Kb80R02TipRecon", True, "NOHARM-base"),
    ("FR13", B + "Kb80E11Receipts.txt", True, "NOHARM-base"),
    # ---- drafts that become the report/lesson/log/scorecard/corpus text ----
    ("S01", B + "Kb80S01Lesson.md", True, "LESSON"),
    ("S02", B + "Kb80S02Log.md", True, "LOG"),
    ("S03", B + "Kb80S03Scorecard.md", True, "SCORECARD"),
    ("S04", B + "Kb80S04Report.md", True, "REPORT"),
    ("S06", B + "Kb80S06Shonen.md", True, "REPORT-shonen"),
    ("S07", B + "Kb80S07Quality.md", True, "Q75"),
    ("S08", B + "Kb80S08ReadmeRows.md", True, "COVERAGE"),
    ("S09", B + "Kb80S09SkillRule.md", True, "SKILL-RULE"),
    ("S10", B + "Kb80S10Province.md", True, "PROVINCE"),
    ("S12", B + "Kb80S12AssimDisp.md", True, "LESSON-gate"),
    ("S13", B + "Kb80S13L0.md", True, "REPORT-l0"),
    ("S15", B + "Kb80S15FreezeShas.md", True, "FREEZE-draft"),
    ("S14", B + "Kb80S14WaveRegistry.md", False, "INDEX"),
    ("E13", B + "Kb80E13FixtureGuard.md", False, "HYGIENE"),
]

# Mandatory subjects: the evidence is required. Tip receipt NAMES are fixed by the committed
# build/run-battery.sh; only the out-dir (receipts/tip/) is proposed here. The EXT names are
# proposed by this index. If the L1 chooses another name or out-dir, cite it in the report and
# update this list.
SUBJECTS = [
    # canonical tip receipt set: produced by build/run-battery.sh (receipt names fixed
    # IN THE COMMITTED RUNNER, lines 190-232). Canonical out-dir proposed: receipts/tip/
    ("TIP01", R + "tip/index.txt", "runner index: rev/repo/fleet/utc + per-receipt exit"),
    ("TIP02", R + "tip/01-tip-battery-dot.txt", "C1 frozen predicate form 1 (--repo .)"),
    ("TIP03", R + "tip/02-tip-battery-abs.txt", "C1 frozen predicate form 2 (absolute --repo)"),
    ("TIP04", R + "tip/03-gate-registry.txt", "Q72 gate at tip"),
    ("TIP05", R + "tip/04-assertion-floors.txt", "Q72 gate at tip (~100 s)"),
    ("TIP06", R + "tip/05-skill-checklist.txt", "Q72 gate at tip"),
    ("TIP07", R + "tip/06-corpus-integrity.txt", "Q72 gate + C1 DRIFT classes"),
    ("TIP08", R + "tip/07-corpus-independent.txt", "Q72 gate + C1 DRIFT classes"),
    ("TIP09", R + "tip/08-correction-sweep.txt", "Q72 gate at tip"),
    ("TIP10", R + "tip/09-census.txt", "Q72 census at final tip"),
    ("TIP11", R + "tip/15-report-pointers.txt", "Q72/Q68 report pointers at report commit"),
    # not covered by the committed runner -- the L1 must run these separately
    ("EXT01", R + "tip-extra-sibling-census.txt", "Q72 check_sibling_census at tip"),
    ("EXT02", R + "c2-base.txt", "C2 base: documented 0 of 6, exit 1"),
    ("EXT03", R + "c2-tip.txt", "C2 tip: documented 6 of 6 + generator world line"),
    ("EXT04", R + "c2-selftest.txt", "C2 counter --self-test"),
    ("EXT05", R + "c2-controls.txt", "C2 controls C0-C8 on the frozen counter"),
]

# Seat reports: every dispatched seat + the plan's C2 reopen receipt name.
SEATS = """Kb80E01Registry Kb80E02Symlink Kb80E03IndexBaseline Kb80E04DeadPointer Kb80E05GrammarFix
Kb80E06CounterErratum Kb80E07C2Counter Kb80E08C2Entry Kb80E09C2Worlds Kb80E10Battery
Kb80E11Receipts Kb80E12Census Kb80E13FixtureGuard Kb80E14C1Worlds Kb80E15BaselineOrder
Kb80E16PinAudit Kb80S01Lesson Kb80S02Log Kb80S03Scorecard Kb80S04Report Kb80S05SourcesEdits
Kb80S06Shonen Kb80S07Quality Kb80S08ReadmeRows Kb80S09SkillRule Kb80S10Province
Kb80S11GateQuotes Kb80S12AssimDisp Kb80S13L0 Kb80S14WaveRegistry Kb80S15FreezeShas
Kb80S16CensusLog Kb80S17ReceiptIndex Kb80R01NegSweep Kb80R02TipRecon Kb80R03ReopenSix
Kb80R04SiblingScan Kb80R05FleetGrammar Kb80R06ShokuknowSlice Kb80R07ClosureScan
Kb80K01Overlap Kb80K02Patterns Kb80K03Considerthese Kb80C01C1 Kb80C02C2 Kb80C03Residual
Kb80C04Honesty Kb80C05Closure Kb80V01C1 Kb80V02C2 Kb80V03Instruments Kb80V04Gates
Kb80V05Report Kb80M01Instruments Kb80M02Battery Kb80M03C2 Kb80M04Registry Kb80Z01Sec
Kb80N01Sentinel Kb80Y01Simplify Kb80G01Revenge Kb80L01Grammar Kb80L02Ctl Kb80L03Symlink
Kb80ReopenSix""".split()


def main() -> int:
    print("# lane root: %s" % os.getcwd())
    print("# id    blocking  status   family          path")
    missing_fixed = []
    for rid, rel, blocking, family in REQUIRED:
        ok = os.path.exists(rel)
        print("%-7s %-9s %-8s %-15s %s" % (rid, "Y" if blocking else "N",
                                           "EXISTS" if ok else "MISSING", family, rel))
        if blocking and not ok:
            missing_fixed.append(rel)

    print("\n# mandatory subjects (tip names from build/run-battery.sh; out-dir/EXT names proposed)")
    missing_subj = []
    for sid, rel, why in SUBJECTS:
        ok = os.path.exists(rel)
        print("%-5s %-8s %-52s %s" % (sid, "EXISTS" if ok else "MISSING", rel, why))
        if not ok:
            missing_subj.append(rel)

    print("\n# seat reports (non-blocking; absence at this instant is expected mid-wave)")
    seat_missing = [s for s in SEATS if not os.path.exists(W + s + ".md")]
    print("# %d/%d present; missing: %s" % (len(SEATS) - len(seat_missing), len(SEATS),
                                            " ".join(seat_missing) if seat_missing else "-"))

    print("\n# own-exit capture audit: .ufo/waves/round-80/receipts/*.txt")
    if os.path.isdir(R):
        for name in sorted(os.listdir(R)):
            if not name.endswith(".txt"):
                continue
            with open(os.path.join(R, name), "rb") as fh:
                text = fh.read().decode("utf-8", "replace")
            lines = text.splitlines()
            has_exit = any(ln.startswith("exit=") for ln in lines)
            has_rc = any(ln.startswith(("pipe-rc=", "direct-rc=")) for ln in lines)
            print("%-46s %s" % (name, "own-exit=yes" if has_exit else
                                ("rc-lines=yes" if has_rc else "own-exit=NO")))

    print("\nfixed-path blocking missing: %d" % len(missing_fixed))
    for rel in missing_fixed:
        print("  MISSING %s" % rel)
    print("mandatory-subject missing (proposed names): %d" % len(missing_subj))
    for rel in missing_subj:
        print("  MISSING %s" % rel)
    if missing_fixed:
        return 1
    if missing_subj:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
