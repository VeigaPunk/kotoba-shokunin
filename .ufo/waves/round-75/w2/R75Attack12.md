# R75Attack12 — falsification of R75Facet12

**Verdict: survived attack; no actionable defect demonstrated.** The cited source claim is accurate at measured lane revision `65a5c7a663249e0522cc49e4a148424200d9ddfe`. The report's proposed control is non-vacuous for the stated comparator disagreement. Its caveat about representativeness/stability is a scope limit, not a finding against the documented rule.

**Independent evidence:** `git show 65a5c7a663249e0522cc49e4a148424200d9ddfe:SKILL.md` line 193 explicitly calls the material Agent Skills guides' artefacts/advice, says the guide threshold is above while `run_eval.py` uses `>=`, and recommends non-integral runs×threshold and unique query strings. At that revision, `corpus/knowledge/skill-eval-artefacts-round70.md:13-16` says the guides are not normative; `:58-72` explains the equality mismatch, repeated-string aggregation and control; `:76-82` disclaims native client execution. The pinned runner snapshot `.ufo/waves/round-70/snapshots/S211-run_eval.py.txt:213-234,266-267` independently confirms aggregation per query string, `>=` for should-trigger, `<` for should-not-trigger, and the default three runs.

**Control exercised:** read-only exact-rational calculation at threshold 1/2 produced:

| Case | Rate | Guide `>` | Runner `>=` |
|---|---:|---:|---:|
| Unique query, 3 runs, 2 triggers | 2/3 | pass | pass |
| Even-run boundary, 2 runs, 1 trigger | 1/2 | fail | pass |
| Duplicate query aggregated across 6 runs, 3 triggers | 1/2 | fail | pass |

This confirms the predicted one-way distinction and that the odd-run unique case avoids equality. No live client fetch or execution was needed. I did not run the evaluator itself; the source snapshot and arithmetic suffice for this boundary check.

**Finding assessment:** The report does not claim that its documentation proves query-set representativeness or stable activation propensity; it explicitly says those broader claims would require separate evidence and limits the control to the comparator counterexample. Therefore that caveat does not falsify the factual claim or establish a source change. The proposed test is specified with cases, expected verdict columns and recorded inputs, and is not a vacuous carry-forward score.

**Verification gaps / residual risk:** No LSP device is mounted (`xd://lsp/status` returned no doc topics; `xd://lsp` reported no such tool), so semantic references/diagnostics were unavailable. No live client behavior or real-world query-set quality was tested, consistently with the facet's stated scope. No actionable defect remains in this facet's scope.

**Evidence provenance:** measured revision confirmed by `git rev-parse HEAD`; exact source was read with `git show <revision>:...`; repository worktree also had pre-existing modifications to `SKILL.md` and `corpus/knowledge/skill-eval-artefacts-round70.md`, so conclusions above refer specifically to committed bytes where stated. No source files changed; no installs.