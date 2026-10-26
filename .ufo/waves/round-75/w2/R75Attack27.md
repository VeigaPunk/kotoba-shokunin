# R75Attack27 — independent falsification of R75Facet27

**Verdict: survives this attack; no actionable defect found in the asserted boundary advice.** The candidate correctly identifies the SKILL line's unique-query boundary: its adjacent conditions jointly avoid equality; uniqueness alone would not suffice. The report labels this only an audit candidate and proposes re-opening pinned bytes plus a truth-table, rather than alleging a defect.

## Independent evidence

Measured repository revision: `65a5c7a663249e0522cc49e4a148424200d9ddfe`. Working tree contains concurrent edits in SKILL/entry and round-75 artifacts, so I used `git show`/tracked revision as the measured basis, not those live working-tree bytes. The exact committed claim at `SKILL.md:193` is also confirmed by `git grep` against `65a5c7a`: it says keep runs × threshold non-integral **and** query strings unique.

- At the pinned `S210-optimizing-descriptions.md:90-94`, query runs are repeated and rates are fractions; should-trigger passes “above” threshold, while should-not-trigger passes below. Thus equality is a disagreement only on should-trigger.
- At `S211-run_eval.py.txt:213-229`, runs are accumulated by query string and rate is `sum(triggers)/len(triggers)`; lines 231-234 implement `>=` for should-trigger and `<` for should-not-trigger. Lines 266-267 set CLI defaults to 3 runs and threshold 0.5.
- I ran a small local arithmetic check: 3×0.5 has no integer success count; 2×0.5 gives equality at one success; 4×0.5 at two; and 3×(1/3 or 2/3) at one or two. Duplicate query text at default 3 runs aggregates to six samples; three successes gives equality. Therefore the uniqueness condition handles exactly the duplication caveat, while the non-integral product condition handles equality for each distinct query's actual collected run count.

The “run count” wording is shorthand: due to duplicate-string aggregation, it means the number of collected trials for the query string, not necessarily the CLI option's nominal per-row count. The advice's explicit uniqueness condition resolves that qualification for its recommended setup; it is not a material misstatement. No client-execution claim is inferred.

## Check limitations / residual risk

No LSP device is mounted (`read xd://lsp` returned “No such tool”), so no semantic references/definition/diagnostics were available; this was a self-contained documentation/source audit, not a caller change. I did not live-fetch upstream. The proposed isolated runner invocation was not necessary to validate the arithmetic; source aggregation logic and the arithmetic check independently establish the stated control. No source or lane files were changed.

Report trailer paths (relative to `kotoba-shokunin`): `.ufo/waves/round-75/w1/R75Facet27.md`