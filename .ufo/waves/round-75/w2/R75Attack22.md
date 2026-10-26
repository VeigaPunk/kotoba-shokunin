# R75Attack22 — falsifying R75Facet22

## Verdict

**Partly survives; bounded textual discrepancy is real, but the report overstates the guide's comparator as settled strict semantics and is duplicative.** The committed guide says “above a threshold”; the reference runner uses `>=`. That supports a literal wording-versus-implementation observation, not proof that the guide defines a strict `>` predicate or that an actual client/evaluation outcome is wrong. No production/client claim is established, and the facet itself properly disclaims those broader claims.

## Independent evidence at measured revision

`git rev-parse HEAD` returned `65a5c7a663249e0522cc49e4a148424200d9ddfe`, matching the facet. Working tree is not clean: `corpus/knowledge/skill-eval-artefacts-round70.md` is modified, so I checked the committed bytes with `git show HEAD:<path>`, not the current working copy.

- Committed knowledge file `corpus/knowledge/skill-eval-artefacts-round70.md:33-34` states F7 as “above” and F8 as runner `>=`; the excerpt is correctly located. Its lines 58-72 bound the claim and give the proposed action.
- Committed S210 snapshot ` .ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md:92` says a should-trigger query passes if its rate “is above a threshold”; that same sentence calls 0.5 “a reasonable default.” It does not say “strictly above,” mention equality, or give an equality example. Thus the source's exact wording is verified, but strict `>` is an interpretation of ordinary prose, not an explicit comparator declaration.
- Committed S211 snapshot `.ufo/waves/round-70/snapshots/S211-run_eval.py.txt:229-234` computes `sum(triggers) / len(triggers)`, uses `>=` for should-trigger and `<` for should-not-trigger. Lines 266-267 give defaults of 3 runs and 0.5. These implementation claims and the cited locations are accurate.
- The guide's S210 example at line 94 uses 3 runs, where a single query's possible rates are 0, 1/3, 2/3, 1; equality at 0.5 is unreachable. The proposed 2-run / duplicated-query 6-run examples are mathematically sound. I independently evaluated equality for 3, 2, and 6 runs: at rate 0.5, `>=` passes and a strict `>` interpretation fails; equality is reachable only for the latter two. At threshold 1/3 and 3 runs, it is likewise reachable (one hit).
- The proposed comparator mutation is non-vacuous for the **runner comparator**: an equality fixture distinguishes `>=` from `>`, and a should-not equality fixture distinguishes `<` from a changed branch. It does not establish that the guide intended strict semantics: a grep/assertion for the phrase “above” would still only test words, not their intended interpretation. No runner/model experiment or live fetch was needed or run.

## Actionable attack

1. **Interpretation boundary:** revise any statement of a “strict above threshold” *rule* as “the guide's wording says ‘above’ and leaves equality unstated; on a strict reading it differs from this runner's `>=`.” The target report's limits and suggested “state which rule the report applies” action already move in this direction, so this is a calibration weakness rather than a false source quotation.
2. **Duplicate:** current wave-1 `R75Facet02.md:12,17-22` identifies the same knowledge-entry paragraph (`:56-72`), same F7/F8 rows, same S210/S211 snapshots, and the same equality question. That report's focus is whether the guide settles the comparator; R75Facet22 frames the same mismatch as an audit candidate. This is not an independent second discrepancy and should not be counted as novel evidence.

## Severity and residual risk

No actionable factual error in the committed source citations, runner branches, default values, or arithmetic. Residual risk is semantic: “above” may be read strictly, but the source never resolves equality. Live-source freshness remains unverified as both reports state; this does not invalidate the dated, committed-snapshot comparison. No lane files were edited.