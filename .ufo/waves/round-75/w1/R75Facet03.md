# R75Facet03 — description-audit source claim

Axes: sourced depth, calibration, operability.

## Finding (observation)

The most concrete weakness in this facet is the round-70 entry's exact-threshold prescription, not its descriptive count of the guide's advice. `corpus/knowledge/skill-eval-artefacts-round70.md:58-72` observes a mismatch between the guide's “above” and `run_eval.py`'s `>=`, then recommends “keep threshold × runs non-integral (an odd run count at 0.5), de-duplicate query strings, or state which rule the report applies.” Yet the audited predicate at `verifiers/check_skill_evals.py:149-161` accepts a quote by normalized substring inclusion inside the pinned snapshot; it verifies quoted evidence but does not measure, simulate, or use the trigger-rate predicate. Its self-test's `F8 inverted operator` arm at `:292` only checks that a quote with `>=` changed to `<` stops matching that source quote. It does not test threshold equality behavior.

Thus the report can safely treat the implementation discrepancy as a source fact, but the operational mitigation is not supported by this counter's measurement and is potentially too broad: any odd run count avoids exactly 0.5 only at threshold 0.5 for a unique query; the entry itself qualifies this in `:67-70`, and notes duplicate queries and non-default thresholds. `SKILL.md:193` compresses the recommendation into “keep runs × threshold non-integral and query strings unique,” which is advice, not a demonstrated requirement for a description audit.

Committed-byte identity check (command): `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD` → `65a5c7a663249e0522cc49e4a148424200d9ddfe`; `git show HEAD:corpus/knowledge/skill-eval-artefacts-round70.md | sha256sum` → `598655365e46cfc4aa27d235c3196f157855c3e6ed92b7a495241441ba946293`; snapshot `git show HEAD:.ufo/waves/round-70/snapshots/S211-run_eval.py.txt | sha256sum` → `43e3b8f80dbf69c343967ba77e268fae991d9fa3ed68b32a0ff02532cd48657f` (matches the entry's cited S211 digest prefix at line 3). No live fetch or model run performed.

## Control / falsifiability

A cheap, falsifiable description-audit control is a tiny truth table on the *declared* `(threshold, run-count, per-query observed fires)` using the source implementation's exact comparison: test below/equal/above threshold, with both should-trigger and should-not-trigger labels; include duplicate query strings as separate and unique cases. Record the source rule and guide wording independently, and flag only equal-threshold should-trigger cases as the disagreement. In particular, `threshold=.5`, 2 runs, 1 fire should pass under `>=` and fail under strict `>`; `threshold=.5`, 3 runs cannot produce equality for one unique query. This tests the described edge directly without implying an end-to-end skill-description quality result.

Smallest safe correction candidate: retain the sourced discrepancy and narrow the advice to “for this implementation, equality passes; report the threshold comparator and the per-query run denominator; if avoiding the discrepancy at 0.5, use an odd run count per unique query.” Do not claim that `check_skill_evals.py` controls this behavior; it currently does not. If advice is meant to be normative for the audit, add the truth-table control to a future counter and its mutation/self-test, with separate cases for duplicate strings and non-default thresholds.

## Impact and risk

- **Sourced depth:** strong on the limited claim: two guides plus one pinned implementation and quotes are distinguished; lines 13-16 disclaim normative status. The numerical prescription is less deeply verified than the underlying source mismatch.
- **Calibration:** moderate risk of readers interpreting the compressed `SKILL.md:193` sentence as a general threshold rule, despite line 70's conditional scope.
- **Operability:** actionable but not presently enforced by the cited quote checker; a future audit could unknowingly report pass while equality handling differs.

No edits made. The working tree already showed the round-75 wave directory untracked when inspected; no change was made outside this report.
