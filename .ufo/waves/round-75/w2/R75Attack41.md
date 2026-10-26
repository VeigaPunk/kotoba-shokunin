# R75Attack41 — Falsification of R75Facet41

## Axes
Factual calibration; provenance; operational scope; falsifiability.

## Verdict
**Facet survives in its narrow central conclusion, but its confidence in the pinpointed committed evidence needs a working-tree caveat.** The cited recommendation is present in the measured committed revision's S210 snapshot, while the knowledge entry currently has an uncommitted modification. This matters because the facet reports committed wording as observed without proving its worktree matched HEAD. No evidence here establishes a specific description's measured quality, and the report correctly avoids that inference.

## Independent evidence
- `git rev-parse HEAD` in `kotoba-shokunin` returned `65a5c7a663249e0522cc49e4a148424200d9ddfe`.
- `git show HEAD:.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md | wc -c` returned `13403`, matching the S210 source row's captured byte count. The pinned snapshot at lines 90-94 says model behavior is nondeterministic, suggests multiple runs and trigger rate, gives 0.5 as a reasonable default, and outlines 20 queries / 3 runs. The knowledge entry at `corpus/knowledge/skill-eval-artefacts-round70.md:48-54` accurately summarizes labelled positives/negatives, repeated runs, held-out validation, and selecting by validation rate. Snapshot section `Avoiding overfitting with train/validation splits` and `The optimization loop` are identified at lines 136 onward; these support the entry's held-out/iteration description.
- The source row `corpus/SOURCES.md:151` scopes S210 to its trigger-evaluation protocol, calls it guidance, and records the snapshot size/date and pinned upstream revision. The entry at lines 13-16 explicitly distinguishes guidance from specification. Its scope caveat at `:76-82` expressly does not assert native client execution.
- Counterevidence to the facet's assumption of committed/worktree identity: `git status --porcelain -- corpus/knowledge/skill-eval-artefacts-round70.md .ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md` returned ` M corpus/knowledge/skill-eval-artefacts-round70.md`. Thus the currently displayed entry bytes are not demonstrated to equal the measured commit. The pinned snapshot itself was not modified according to this path-scoped status, and HEAD's snapshot can be read independently.

## Attack on the proposed control
The proposed freeze/held-out/repeated-run control is non-vacuous in design: it would expose tuning-set leakage and permit before/after comparison. But it is a protocol, not a cheap check of an existing description; it requires choosing a target, representative labelled queries, a client/runtime, and repeated invocations. Query labels and client-specific observability are themselves judgment-sensitive, as S210:79-81 says behavior/registration and detection vary by client. Therefore the control must not be presented as a direct objective quality score or proof of generalized routing quality. Its strongest valid claim is empirical performance on the frozen fixture, under the named client and measurement procedure.

The report's proposed additional requirement to re-open pinned S210 is useful provenance hygiene, but the local snapshot/source row already allows the historical recommendation to be checked without live fetch. A live re-fetch is unnecessary for the historical claim and would test freshness instead. No evaluator command is specified in the facet report, so there was no concrete command to execute safely; no experiment was run.

## Smallest safe correction
Retain the narrow conclusion and control, but state that the measured revision's committed snapshot supports the historical recommendation, and that the knowledge entry's present working-tree bytes are dirty relative to HEAD. Qualify any resulting metric as fixture- and client-specific, not a universal or intrinsic description-quality score. Do not infer a defect in any target description.

## Evidence trailer
Measured revision: `65a5c7a663249e0522cc49e4a148424200d9ddfe`. Read-only checks only; no source edits, live fetches, or installs. Report written at `.ufo/waves/round-75/w2/R75Attack41.md`.
