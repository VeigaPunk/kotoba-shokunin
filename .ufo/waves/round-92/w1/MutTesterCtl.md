# MutTesterCtl — round-92 w1 findings

Candidate: freeze `e073723` + ExecCtlWorlds.patch + ExecKillPin.patch = scratch commit `52dc61ea4e33047ce1a9776c3a5fa92ff9fcc6fa`.
Full detail, diffs and rc evidence: `.ufo/waves/round-92/w1/MutTesterCtl/MutTesterCtl.md` (receipts in `.ufo/waves/round-92/w1/MutTesterCtl/receipts/`).

Baseline (unmutated): frozen counting `round-92 controls: shortcuts refused 2 of 2; honest held 2 of 2` rc 0 (438 s); battery self-test `0 failure(s) over 28 assertions` rc 0.

| mutant | attack | frozen counting on candidate | discriminating probe | verdict |
|---|---|---|---|---|
| m1 | counting accepts refused world rc 0 | `2 of 2` rc 0 (same as base) | stub refused-rc-0 world: candidate `1 of 2` rc 1, m1 `2 of 2` rc 0 | SURVIVED (F1) |
| m2 | ctl-c2 drops tip battery, cap-only | `refused 1 of 2` rc 1 | shortcut world: m2 ACCEPTED rc 0, candidate REFUSED rc 1 | KILLED |
| m3 | ctl-c1 passes base rev | `refused 1 of 2` rc 1 | manifest-only world: m3 ACCEPTED rc 0 | KILLED |
| m4 | kill-set-size arm removed | `2 of 2` rc 0 | dropped-row self-test: m4 rc 0 (N=25); candidate rc 1 naming kill-set-size | SURVIVED on frozen counting (F2); caught only by the plan's C2(a) after-readings |
| m5 | ctl-c1-honest drops exit-0 rc | `2 of 2` rc 0 (no rev passed) | G3-failing rev: m5 `C1-PREDICATE-MET` rc 0; candidate `UNMET` rc 1 | SURVIVED on frozen counting (F3); KILLED by rev probe |

Equivalents green: frozen counting rc 0 with 2 of 2 and 2 of 2 unmutated; battery self-test rc 0 with 28 assertions.

Findings (short; detail in the MutTesterCtl.md):
- F1: no consumer pins a refused world's exit code (m1 survives the frozen predicate).
- F2: C2(a) has no executable frozen control; the pin reads the instrument's working-tree manifest, not the measured revision's committed manifest.
- F3: the honest control's rc-0 conjunct is only exercised with a revision argument, which the counting never passes.
- F4: `ctl-c1-honest.sh` prints "without the frozen predicate line" on a case where the line is printed (message only).
- F5: the frozen counting takes ~411–453 s; above the 120 s per-probe guidance.

ReviewerCtl had not published probes when checked; if its probes cover m1, m4 or m5, those SURVIVED lines change.
