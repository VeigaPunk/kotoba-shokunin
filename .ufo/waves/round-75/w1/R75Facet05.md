# R75Facet05 — trigger-threshold boundary as a sourced-depth audit candidate

## Observed evidence

- `corpus/knowledge/skill-eval-artefacts-round70.md:13-16` explicitly limits its authority: S209/S210 are guides, not the specification, and their values are advice rather than normative rules. Lines 33-34 distinguish the guide's “above” threshold wording (F7) from the reference implementation's `>=` behavior (F8); lines 58-72 spell out the discrepancy and suggested mitigations. This is a carefully bounded statement, not an unqualified claim that the guide and implementation agree.
- The committed snapshots support the boundary: `.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md:88-93` says 3 runs is a reasonable starting point, should-trigger rates pass when above threshold (0.5 a reasonable default), and should-not-trigger rates pass below. `.ufo/waves/round-70/snapshots/S211-run_eval.py.txt:227-234` groups results by query string, computes rate over that group's collected outcomes, then uses `>=` for should-trigger and `<` for should-not-trigger. Its defaults are 3 runs and threshold 0.5 (`:264-267`). The key is query-string identity (`:213-225`), so repeated identical strings aggregate in one group.
- `corpus/knowledge/skill-eval-artefacts-round70.md:61-70` correctly notes a one-way disagreement at exact threshold, and that a unique query at the defaults cannot have rate exactly 0.5 (three trials yield 0, 1/3, 2/3, or 1). The duplicate-query caveat is grounded in the implementation's grouping by query string: two copies at three runs each can produce 3/6. This caveat matters; a naïve “three runs eliminate the boundary” summary would be false for duplicated queries.
- `corpus/lessons/round-74-verifier-spotcheck.md:15-19` says gates were not executed and distinguishes receipt verification from re-measurement/re-opening. This is an appropriate evidence-status warning when using the r70 knowledge artifact; the lesson does not independently re-evaluate its threshold facts.

## Assessment / inference

This is a strong, narrow candidate for a sourced-depth and calibration audit: the source distinction, exact comparator, defaults, and edge case are all falsifiable from pinned committed bytes. The artifact is calibrated about authority and scope (`skill-eval-artefacts-round70.md:13-16, 74-82`), and the threshold example has more depth than merely repeating a recommendation because it derives a concrete disagreement boundary (`:56-72`). It is historical committed evidence, not evidence that a current client executes this evaluator or that current descriptions behave the same way. In particular, the entry expressly declines to claim native client support (`:76-82`).

## Concrete check/control

For a read-only audit, reproduce the boundary from the pinned snapshots: verify S210's “above” wording at lines 90-92; verify S211's default arguments and comparator/grouping at the lines above; then check the entry's stated examples against rates. Minimal truth table: unique 3-run query at threshold .5 has no equality case; two identical query rows totaling 6 runs can have 3/6 equality, where S211 passes should-trigger and the guide's strict “above” would not. Require the report to state whether rates are grouped per distinct query string and preserve the authority label “guide” versus “reference implementation.” No model run, live fetch, or current-client claim is needed.

**Confidence:** High for the wording/comparator/defaults, directly located in committed snapshots; moderate for using this as a prospective audit target, since the artifact dates to round 70 and this report does not establish current round-75 implementation or behavior.

**Remaining unknowns:** Whether the referenced upstream pages/code remain unchanged since the snapshots; whether any current consumer adopts this evaluator or its exact semantics. Neither is established by these committed files, and neither is necessary to state the bounded historical finding.

## Evidence paths

All paths are relative to `kotoba-shokunin`:
- `corpus/knowledge/skill-eval-artefacts-round70.md:13-16,33-34,56-82`
- `.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md:88-93`
- `.ufo/waves/round-70/snapshots/S211-run_eval.py.txt:213-234,264-267`
- `corpus/lessons/round-74-verifier-spotcheck.md:15-19`
