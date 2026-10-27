# C03CritSizing — round 77 claim-sizing falsifier

## Result

**C1 and C2 are distinct and causally separable at the frozen-counter level.** The C1 counter reads the round-76 snapshots, round-76 lesson, description-craft entry, `SKILL.md`, and `SOURCES.md`. C2 reads round-75 lesson/results, round-76 repair receipts/note, and `LOG.md`; its one `SKILL.md` read is for recomputing the historical description named in the R1 receipt, not the C1 measured revision. Neither counter requires the other claim's artifacts. At base both independently fail (`0 of 6`, exit 1; `0 of 4`, exit 1), as recorded in the r77 base receipts. Shared corpus-index/baseline hygiene may be needed to keep the corpus gates green, but that is not a shared predicate dependency.

The lowest-axis duty is met under the lane's declared owned scores: depth 9 < consistency 10 in `SCORECARD.md`, and C1 works depth. This conclusion is scoped to the lane's declared ownership; fleet `AXES.md` names calibration, not consistency.

## Strong counterexample: C2's headline exceeds its predicate

The strongest local counterexample is a real-git scratch-clone test of frozen `check_r75_routed_repairs.py` (the counter was not modified). I ran its own `_fixture_tree` to make an honest 4/4 world, then changed only the appended R1 correction so it said the spot-check's 1,022 measurement was wrong and both original false premises still stand. The text retained the required quoted superseded row/Gate text, `1,022`, lines 4–18, and spot-check citation. The correction then expressly denied the asserted repair. I committed that control change in the scratch clone and ran the frozen counter at the resulting revision:

- Honest fixture: `r75 routed repairs closed 4 of 4`, exit 0.
- Reaffirming/false R1 “correction”: `r75 routed repairs closed 4 of 4`, exit 0.

Exact control driver: `/fast/scratch/hyaku/kotoba-r77/C03CritSizing/ctl.py`; captured output: `/fast/scratch/hyaku/kotoba-r77/C03CritSizing/ctl.out` (temporary scratch, not a cited deliverable). The counter's R1 text arm checks for quoted token windows, required numbers/line range, and citation; it does not establish that the correction's direction is true. R1's separate receipt recomputes the historical render at the receipt's named ancestor, not whether the appended lesson accepts that measurement. R2 re-runs the two gates at the pinned r75 tip; R3/R4 recompute counts. Thus 4/4 is evidence that the specified four checks' conditions are present, not proof that all four routed defects were substantively repaired.

**Impacted axes:** consistency claim validity and calibration/trust boundary; freshness/operability are secondary because users may read “closed” as semantic closure. This is a counter/predicate limitation for the semantic headline, not evidence that the actual round-76 correction is false.

## Calibration fit (round-prompt §9)

The round prompt §9 says a calibration claim **must count mismatches between lane self-assessment (`SCORECARD`/`SHONEN`) and observed repo state**; it cannot be an assertion. C2 neither reads nor counts either self-assessment surface. The C2 read trace at the r77 base includes `corpus/lessons/round-75.md`, `LOG.md`, round-75 results, and the three r76 repair records; it has no `SCORECARD.md` or `SHONEN.md` read. R1/R3/R4 reconcile lesson/log/wave records to selected repo evidence, and R2 establishes historical gate output, but this is routed-defect closure/evidence integrity, not the §9 self-assessment mismatch count. Calling it “consistency (calibration sub-axis)” therefore overstates its calibration fit. It also does not establish an overall mismatch count; those four routed defects are a selected set, not an enumeration of all SCORECARD/SHONEN claims.

## C1 boundary / universal wording

C1's “all six conjuncts” is bounded correctly: the six are explicitly enumerated and the counter evaluates each. Its semantic boundary is separately disclosed in the r76 plan: the counter's own text calls quote/action arms floors and delegates the judgment that the page teaches the rules to non-author attacks/closure. Accordingly, “backed 6 of 6” is the frozen mechanical predicate, not by itself proof of correct or effective description craft. The r77 plan's fresh S213 re-open is also not a C1 counter conjunct; preserve its independent fetch/quote/digest receipts as separately audited sourcing evidence, not as something the 6/6 result proves.

C2's universal “all four repairs” is likewise finite in the predicate (R1–R4 are enumerated), but the observed R1 counterexample shows that the predicate does not support the semantic word “repairs closed.” Avoid broader phrases such as “all issues fixed” or “no harm anywhere”: the battery enumerates named gates; it is not an all-axis no-harm census.

## Smallest safe correction (counters remain frozen)

Keep both counters and their targets unchanged. Tighten the C2 **headline/axis wording** in the plan and any planned scorecard/report language to:

> **C2 — routed-repair evidence predicate (consistency/evidence integrity):** the frozen counter's four enumerated R1–R4 artifact/reproduction checks pass (`r75 routed repairs closed 4 of 4`). This result does not itself assert semantic truth of the R1 lesson correction and is not a §9 calibration mismatch count.

Do not call this a calibration improvement or a substantive “four repairs closed” result solely on the counter. If C2 must remain a calibration claim, add a separately re-derivable before→after count of SCORECARD/SHONEN-vs-repo mismatches (which is beyond this frozen predicate); otherwise classify/report it only as the narrower consistency/evidence-integrity claim and let the independent closure verify R1's truth. The counterexamples are a fixable headline/evidence limitation, not a reason to edit frozen bytes or silently broaden the claim.

## Evidence/commands exercised

- Read `/home/vgpnk/Projects/shokunin/kotoba-shokunin/plans/round-77.md`, `plans/round-76.md`, addenda 1–6, both counter docstrings/arms, `../AXES.md`, `../templates/round-prompt.md` §9, lane `SCORECARD.md`, r75 verifier spot-check, r76 entry draft, and r77 base receipts.
- Scratch-clone read-set and base checks: counter runs at clone HEAD `6523aced1ee0ebe07dca996213bdc645a6acbd1e`; both exit 1, output `0 of 6` and `0 of 4` respectively. Git trace showed no shared predicate inputs (C2's `SKILL.md` read is through R1 historical render recomputation).
- Reaffirming-R1 scratch control: honest fixture 4/4 exit 0; false-direction correction 4/4 exit 0 (captured in the scratch output above).
- No lane files or counters modified. No tools installed.
