# R75Facet17 — trigger-query design and validation as a description-audit candidate

## Finding

**Observed (high confidence; committed bytes).** The r70 entry's source declarations identify S210/S213 as the Agent Skills description-optimization *guide*, pin the snapshot and upstream revision, and explicitly date its historical `ground:` sweep to `7d51253f` (`corpus/knowledge/skill-eval-artefacts-round70.md:2,6-9`). Its authority note says the advice is non-normative (`:13-16`). The same entry describes trigger query construction, repetition, and a held-out split; it warns that the guide and skill-creator runner differ at the threshold, and disclaims native-client execution (`:48-54,58-72,76-82`). The r74 spotcheck reports a separate C1 sourced-coverage claim, with re-measured page fidelity and counter outputs, and calls its verdict `improved` (`corpus/lessons/round-74-verifier-spotcheck.md:46-64,100-105`); it does not turn the r70 entry into a current r75 claim.

The pinned S210 snapshot provides a particularly concrete, falsifiable test-design rule: positive queries should vary phrasing, explicitness, detail and complexity; useful negatives are near-misses with keyword overlap, not obviously irrelevant prompts (`.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md:41-66`). It says hold out a fixed, mixed 40% validation split, never use validation failures to guide edits, select the best iteration by validation pass rate, and try fresh queries after selection (`:136-163,171-175`). The entry summarizes part of this method, but its compact `SKILL.md` description-audit guidance is not itself evidence that any particular query set follows these design safeguards (`SKILL.md:193`).

**Assessment / inference.** This is a suitable r75 *candidate rule* for a sourced-depth/calibration audit, not a finding that the current description has failed. An audit that merely counts labelled queries or reports a trigger percentage can miss the source's key construct-validity guard: plausible near-miss negatives and varied positives. A query set of easy unrelated negatives could yield a reassuring false-trigger rate without testing the description's boundary. Likewise, if held-out examples influenced edits, the claimed validation score is no longer held out. The documentary source supports recommendations about test design; it does not establish a universal benchmark, prove that a prompt population is representative, or show runtime behavior for any client.

## Concrete check / control

For a read-only committed-byte audit, bind the claim to one explicit description revision and inspect the exact frozen query set plus its train/validation assignment and edit history. For each query, require a `should_trigger` label and record which declared dimension it exercises (positive: phrasing / explicitness / detail / complexity; negative: overlapping-keyword near-miss). Check that both labels occur in each split, the split is fixed, and validation queries/results are absent from the evidence used to choose or revise descriptions. Treat a negative set consisting only of irrelevant prompts as insufficient coverage, not a passing precision control. Recompute reported counts/rates from the committed query and outcome rows; retain fresh, previously unused queries as a separately reported generalization check. Cite S210/S213 as guide advice, not a normative specification or client guarantee.

This control can fail observably: a duplicated/missing label, one-class split, absent near-miss negatives, validation item appearing in an edit rationale, or a reported rate not reproducible from frozen outcomes falsifies the corresponding audit claim. Source: `.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md:41-66,136-163,171-175`; source-row scope: `corpus/SOURCES.md:151,153`.

## Evidence limits

- The inspected repo tip is `65a5c7a663249e0522cc49e4a148424200d9ddfe`; `git rev-parse HEAD:<path>` confirmed committed objects for `SKILL.md` (`d612f22…`), the r70 knowledge entry (`c103d82…`), r74 lesson (`9f3e7b3…`), `QUALITY.md` (`6ed3a9a…`), r74 plan (`d3fa9ba…`), and S210 snapshot (`8bc4cc4…`).
- No live fetch, model/runtime experiment, or verifier execution was done. The snapshot establishes what the guide said at its pinned historical revision, not what any current client implements.
- This is a bounded audit design opportunity; it does not claim the r75 description or any particular query corpus is defective.
- No edits outside this report; no install.

## Evidence paths

All paths are relative to `kotoba-shokunin`:
- `SKILL.md:193`
- `corpus/knowledge/skill-eval-artefacts-round70.md:2,6-9,13-16,48-54,58-82`
- `.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md:41-66,136-163,171-175`
- `corpus/SOURCES.md:151,153`
- `corpus/lessons/round-74-verifier-spotcheck.md:46-64,100-105`
- `corpus/QUALITY.md:36-37` (Q25-Q26 require falsifiable counter arms and headlines bounded to what the counter/guard measures)
- `plans/round-74.md:47-58,98-99` (historical claim identity/bound distinction; not a frozen r75 plan)
