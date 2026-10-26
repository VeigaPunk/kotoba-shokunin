# R75Attack39 — falsification of Facet 39

**Axes:** calibration, freshness, operability.

## Verdict

The narrow historical comparison and proposed boundary fixture survive: the pinned guide snapshot says “above,” while the pinned reference runner uses `>=` for should-trigger and `<` for should-not-trigger. This is not evidence of a defect in a current audit or client. The report’s claim that the *knowledge entry* records the discrepancy is stale against the working tree at the measured commit: that entry has an uncommitted edit adding an explicit Round 75 equality clarification. Do not mistake that working-tree text for committed evidence. The recommended tests are only partially discriminating: “just below” is a shared negative control, not a comparator discriminator; equality is the actual differentiating case.

## Independent evidence

- `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD` returned `65a5c7a663249e0522cc49e4a148424200d9ddfe`.
- `git status --porcelain -- corpus/knowledge/skill-eval-artefacts-round70.md ...` returned ` M corpus/knowledge/skill-eval-artefacts-round70.md`. Thus the committed-vs-working-tree distinction matters. Current working tree lines 86–88 add a Round 75 clarification pointing to Facet02; that addition is not part of HEAD and cannot validate Facet39’s committed-source citation.
- The assigned Facet39 report cites knowledge lines 27–34 and says they record the discrepancy. In committed snapshot, the given rows indeed say F7 “above” (line 33) and F8 `>=` (line 34); lines 58–72 explain that equality is where they disagree and list mitigations. Committed entry lines 76–77 restrict scope to the guides and one implementation.
- Re-opened `.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md:90-92`: guide wording is “above a threshold” for should-trigger and “below” for should-not-trigger.
- Re-opened `.ufo/waves/round-70/snapshots/S211-run_eval.py.txt:227-234`: rates are computed per query; branch uses `>=` for should-trigger and `<` for should-not-trigger. A cheap literal check against `git show HEAD:<snapshot>` confirmed both predicates are present. No runtime execution is needed to test this boolean boundary.
- `corpus/QUALITY.md:36-37` supports content-sensitive falsification controls for claims, but does not establish an existing description-audit counter or defect.

## Counterexample / control assessment

A direct equality test (rate exactly equal to threshold) distinguishes strict `>` from inclusive `>=`; a just-below test fails under both predicates and therefore cannot by itself falsify the comparator claim. The report’s stated test of equality plus just-below is sound as a positive boundary case plus sanity control, provided the chosen comparator is named. At default 3 runs and threshold 0.5, equality cannot occur for one unique query (rates are multiples of 1/3); use an even run count, or another threshold/run combination with integral product, to make that fixture reachable. This is consistent with committed entry lines 62–70. Same threshold/query set is useful for comparisons but not itself a control for comparator correctness.

**Impacted axes:** freshness (working-tree entry is modified while revision is named); calibration (historical observation does not imply present audit misclassification); operability (below-threshold arm is nondiscriminating for strict-vs-inclusive behavior).

**Smallest safe correction:** retain the narrowly historical finding, cite immutable `HEAD` snapshot bytes for it, explicitly state that no current counter defect was tested, and make the equality arm the comparator assertion; keep below-threshold only as a sanity arm. Do not attribute the uncommitted entry clarification to revision `65a5c7a`.

## Report trailer

- `.ufo/waves/round-75/w1/R75Facet39.md:3-11`
- `.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md:90-92`
- `.ufo/waves/round-70/snapshots/S211-run_eval.py.txt:227-234`
- `corpus/knowledge/skill-eval-artefacts-round70.md:33-34,58-72,76-77` (working tree modified; source wording here is committed at HEAD except new lines 86-88)
- `corpus/QUALITY.md:36-37`
