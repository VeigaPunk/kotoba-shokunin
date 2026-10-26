# R75Attack36 — independent falsification

## Axes
Consistency, calibration, operability.

## Verdict
**Central comparator finding survives, but the proposed check is only a minimal arithmetic illustration, not a test of the cited runner or actual trigger behavior.** The report correctly scopes the disagreement to a reference implementation versus guide wording, and it correctly warns against universalizing it. Its material actionable risk is under-stated: the exact equality condition is not reached with the default 3 runs for a unique query, but the committed entry itself identifies duplicate query-string aggregation and non-default thresholds that do make equality reachable.

## Evidence

- Reopened the target `R75Facet36.md`: it says the `>=` vs “above” discrepancy is evidence of boundary disagreement, acknowledges that this is not a universal format/client rule, and proposes an equality-boundary test.
- At measured master `65a5c7a663249e0522cc49e4a148424200d9ddfe`, independently reopened committed `corpus/knowledge/skill-eval-artefacts-round70.md` lines 33–34: F7 quotes S213 “above a threshold”; F8 quotes S211 `did_pass = trigger_rate >= trigger_threshold`. Lines 58–72 specify the exact disagreement and its reachability limits: 3 unique-query runs produce no 0.5 rate, while duplicate query strings aggregate to six results and configurable thresholds can produce equality. Snapshot SHA256 matches the recorded S211 prefix `43e3b8f8…`; the cited expression is present at snapshot line 232.
- The local Python boundary check at rate = threshold = 0.5 returns implementation `True`, strict-wording `False`. This confirms the arithmetic only; it does not execute `run_eval.py`, invoke Claude, or establish any observed trigger behavior.
- The checked-out knowledge file is modified relative to master (its SHA256 differs from `git show 65a5c7a:...`); thus current working-copy bytes are not a valid substitute for the requested measured-revision evidence. The committed master version was used above. Target report itself is not present in that master tree (it is wave-owned untracked evidence), so its contents were independently reopened from its lane path.
- The cited round-74 spot-check lines 76–77 concern a description length/name check and unrelated counter; they do not independently bear on the trigger comparator.

## Smallest safe correction

Keep the scoped implementation-vs-guide claim. Phrase the suggested check as an explicit branch/arithmetic regression against the pinned S211 source (or say it is only a comparator illustration); do not imply it measures trigger effectiveness. Preserve the reachability qualification: default 3 runs with distinct query strings avoid the boundary, but other supported inputs can reach it. No lane-source changes made.

## Report

- `.ufo/waves/round-75/w2/R75Attack36.md`
