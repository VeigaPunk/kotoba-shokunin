# F16 — predicate sentence identity review

Axes: depth, consistency, calibration, freshness, operability. Scope: scorecard predicate identity on the only observed lane HEAD; no claim data was committed at that revision.

## Finding: no landed r77 scorecard predicate to compare

Read `plans/round-77.md` at HEAD `6523aced1ee0ebe07dca996213bdc645a6acbd1e`. Its C1 sentence is the exact r77 command + `description craft backed K of 6` + exit-0-at-all-six + base `2f675548eaad2a037a899d39247c1fd7a88aaf48` red condition (plan lines 24–27). C2 similarly specifies `r75 routed repairs closed 4 of 4` and the same r77 base red result (lines 36–40). But the measured tree is the declared freeze/base, not a landed data tip: `corpus/knowledge/description-craft-round76.md` is absent; the C1 gate independently confirms lesson, entry, SKILL row and S213 used-by are absent. The SCORECARD at this tip has the Round 76 honest-stop annotation at line 469 and no Round 77 row. Thus an r77 SCORECARD sentence cannot yet be identity-checked as a landed artifact.

## Predicate identity mismatch in frozen counter docstrings

The unchanged frozen C1 docstring (lines 10–15) quotes the operational shape but binds its red condition to the prior r76 base `b7f13f4b39cbd43076a85568adca763a6f674e7a`; the plan's r77 predicate binds it to `2f675548eaad2a037a899d39247c1fd7a88aaf48`. C2 has the same mismatch (docstring lines 6–12). This is a disclosed historical-base difference because counter bytes were frozen unchanged, not evidence the frozen counters were edited. It does mean the frozen docstring sentence is not verbatim-identical to the current round's canonical sentence. Build draft `C02CritPredicate.proposed-addendum.md` independently flags this distinction and recommends recording the complete operational sentence verbatim in round-77 receipts and SCORECARD. I did not treat that draft as landed evidence.

## Runs and bytes

At revision `6523aced1ee0ebe07dca996213bdc645a6acbd1e`:

- `python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_desc_craft.py --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e` → `description craft backed 0 of 6`, exit 1. All six conjuncts fail; output says the lesson and entry are not committed, no cited Body craft row, no audit entry, no S213 used-by and no provenance entry.
- `python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_r75_routed_repairs.py --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e --work /fast/scratch/hyaku/kotoba-r77/F16CheckScorecard/c2work` → `r75 routed repairs closed 0 of 4`, exit 1. R1–R4 are open; required lesson/receipts/note/LOG records are absent.
- `sha256sum verifiers/check_desc_craft.py verifiers/check_r75_routed_repairs.py` → `cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e` and `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63`, matching the plan pins.

The cwd lane was clean in the tracked/index sense, but had untracked wave build/receipt artifacts; HEAD remained the freeze hash above. The scratch output files were transient and are not cited as deliverables. No tools installed.

## Counterexample, axes, smallest safe correction

Counterexample: the round-77 plan and unchanged r76 counter docstrings have different base-revision clauses, while the measured SCORECARD has no C1/C2 r77 row at all. Therefore a scorecard-row identity claim for the landed round is currently unsupported. This affects calibration/consistency (predicate provenance), depth (no landed C1 claim evidence), freshness (r77 result absent), and operability (a reader cannot reproduce a purported after-value from the observed tip). It is a fixable record mismatch, not evidence that counter logic changed.

Smallest safe correction: after data is actually committed and L1 announces the landed measured revision, put the full plan-canonical C1/C2 predicate sentences verbatim into the relevant receipts and SCORECARD rows, with measured revision, output and direct exit status; retain the frozen counter bytes and explicitly identify their r76-base docstring as historical. Re-run both counters at that measured revision. Do not write or score an after-row before that landing. This improves identity/operability without harming any axis. Current blocker: there is no landed claim-data tip to review.

VERDICT: blocked—only freeze/base HEAD is present; both frozen gates are red and no r77 SCORECARD predicate row is landed, so predicate identity of the claimed after-state is not established.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w2/F16CheckScorecard.md