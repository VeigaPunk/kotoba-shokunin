# R75Attack24 — attack on R75Facet24

## Verdict: finding does not survive; control-gap claim is unsupported

**Axes:** factual accuracy; materiality/actionability; scope; operability.

The attacked report's central claim is that `SKILL.md:193` offers uniqueness/non-integral threshold×runs as sufficient safeguards but lacks a guard checking the actual configuration, so the recommendation's continued applicability is not counter-enforced. The source bytes show a bounded authoring recommendation, not an enforced invariant or a promise of automated validation: `SKILL.md:193` explicitly identifies the guide advice level and points to the reference implementation and its knowledge entry. A missing automated guard is not a demonstrated defect in prose advice, and the report supplies no requirement that this recommendation be automatically checked. Its proposed committed control matrix is optional validation, not evidence that the current statement is materially wrong.

**Independent source check:** the pinned S211 snapshot is recorded at `corpus/knowledge/skill-eval-artefacts-round70.md:3` (tree `dbd4588f9e1033efb41dad4bef2f7947c8993d44`). In `.ufo/waves/round-70/snapshots/S211-run_eval.py.txt`, lines 201 and 213–229 show repeated submissions and aggregation by query string, with rate `sum(triggers) / len(triggers)`; lines 232–234 implement `>=` for should-trigger and `<` for should-not-trigger; lines 266–267 set default runs=3 and threshold=0.5. This confirms the report's underlying comparator/denominator facts, rather than refuting them.

**Cheap control arithmetic (same pinned behavior):** unique query, 3 runs, 1 trigger gives 1/3: both `> 0.5` and `>= 0.5` fail; 2/3 passes both. Duplicate identical query entries each run 3 times and are aggregated as one string across six observations (snapshot lines 200–229); 3/6 gives strict-guide fail and implementation pass. Unique query, 2 runs, 1 trigger likewise gives the equality disagreement. For an arbitrary threshold `t`, unique strings and `runs × t` non-integral rule out equality on that denominator; duplicates can change the denominator, hence the additional uniqueness clause in `SKILL.md` is relevant. These examples support, rather than falsify, the scoped advice. I did not execute live `run_eval.py`: it launches `claude -p` and performs external model calls (snapshot lines 70–90), so the deterministic arithmetic check against pinned source is the safe cheap check.

**Scope/evidence qualification:** the report's own cited knowledge entry says these are guide recommendations, not universal rules (R75Facet24's cited lines 11–21); the source itself calls them “guide advice level.” It correctly notes that the recommendation is prose, but infers a control obligation without an applicable requirement. The facts are about the named upstream implementation, and `SKILL.md:193` scopes its comparator statement to that reference implementation; no broader runtime claim is needed.

**LSP:** no `lsp` device is mounted in this environment (the `xd://lsp` request returned “No such tool” and listed mounted devices). Used literal source reads/snapshot instead; no semantic-search claim is made.

## Residual risk / verification gaps

No live fetch or external execution was performed. The report's concrete comparator and duplicate-query observations are corroborated by the recorded pinned snapshot; its proposed automated control may be useful as future assurance, but no evidence establishes it as required or as a current actionable defect.

## Report trailer

- Target: `.ufo/waves/round-75/w1/R75Facet24.md`.
- Evidence: `SKILL.md:193`; `corpus/knowledge/skill-eval-artefacts-round70.md:3,11-21,33-34,56-72`; `.ufo/waves/round-70/snapshots/S211-run_eval.py.txt:200-234,266-267`.
- No lane changes; report only.
