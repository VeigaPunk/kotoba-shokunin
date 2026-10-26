# R75Attack53 — independent attack on R75Facet53

## Axes
Calibration, depth, freshness, and evidence/provenance scope.

## Verdict
The central factual finding survives: `check_description_thresholds.py` does not verify that the quoted source supports the row's particular threshold or its `Past the threshold` assertion. The facet's two proposed falsifier results are reproducible against the pinned source module when performed as in-memory substitutions. However, its assertion that those worlds change the quote in both the entry and the round-54 Gate record is unsupported by its replay code: `old1`/`old2` are not present in `LESSON`, so `le.replace(old,n)` is a no-op. The actual test changes only the entry quote, which is stronger and appropriately self-consistent with the checker behavior. This is an evidence-description defect, not a reversal of the substantive finding.

## Independent evidence at measured revision `65a5c7a663249e0522cc49e4a148424200d9ddfe`

- `git rev-parse HEAD` reports the stated revision. The workspace has unrelated pending wave files; this check used the explicitly pinned `git show <rev>:<path>` inputs.
- Reopened `SKILL.md:164-176`: the table has columns Client, Documented threshold, Past the threshold, Action; line 166 says checked by the counter.
- Reopened `verifiers/check_description_thresholds.py:272-330`: the checker extracts numeric tokens from the threshold cell, validates the action cell only for emptiness, and tests `has_token(quote,tokens)`. The `Past the threshold` cell is not tested. `has_token` at `:245-249` accepts any matching token. At `:317-326`, quotes are checked for word-count, any threshold token, and inclusion in Gate-recorded quotes.
- Independently ran `python3 -B verifiers/check_description_thresholds.py --rev <pinned rev>`: seven clients print BACKED; summary is `description thresholds backed 7 of 7 clients`; exit 0.
- Replayed both proposed substitutions using the committed module and pinned entry/source/lesson bytes. For each, exact `old` quote was present in the entry but absent in the lesson (`W1 True False True False`; `W2 True False True False`, ordered entry-old, entry-new, lesson-old, lesson-new). The test therefore does *not* replace the Gate row as the report's prose says. Despite that, `judge()` returns all seven clients backed for both entry-only substitutions. This is direct evidence that the quote-to-number predicate is too weak; the Gate row cannot make the tested change self-consistent, and is not needed to get the false acceptance.
- The measured token lists were Claude Code `['1,536','1%','0.01']` and opencode `['1','1024','1','2']`; the substitutions are accepted because the quote matches a different extracted token (W1: `1%`; W2: `1` from `v1` in the threshold cell). Counter SHA-256 from pinned bytes: `15fdf83b30ddb0c68bf694a7d607a59dd80f685ba1d7750487f48d4b602fe186`.
- The `TARGET=4` vs seven clients observation is also borne out by implementation at `:83, :509-514`: the gate reports total count but succeeds at four backed entries. The facet's suggestion to label the result `4 of 7` or explicitly set target to 7 is a reporting/control choice; the current claim is not that the gate asserts all seven.

## Attack assessment and limits

The facet's core limitation is actionable and in scope because the skill itself attributes its table statement to this checker. Its observed missing-column and any-token behaviors are evidenced in the implementation and do not depend on stale working-tree data. Its recommended primary-token control is a plausible successor design, but this attack did not implement or test it; do not treat that proposal as a validated fix. In particular, masking version labels alone does not address arbitrary same-cell alternate thresholds (W1); primary-token matching or a more semantic row/quote association is needed. The facet's stated replay procedure should be corrected to say entry-only substitutions, unless it adds an actual Gate-row mutation with the exact applicable Gate syntax.

No source or lane files edited; no commits, fetches, installs, or scratch mutations. Report written only to `.ufo/waves/round-75/w2/R75Attack53.md`.

Report: `.ufo/waves/round-75/w2/R75Attack53.md`
