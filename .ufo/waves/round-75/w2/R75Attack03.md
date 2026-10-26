# R75Attack03 — attack on R75Facet03

## Verdict

**Finding substantially survives, with one calibration limit.** The source discrepancy is real and correctly cited. The actionable concern is also supported: `SKILL.md:193` publishes “Keep runs × threshold non-integral and query strings unique” as unqualified imperative advice, while the source entry explicitly delimits the cases and presents alternatives. However, the facet report itself already recognizes those limits, so this is not a newly discovered factual error and its stated risk is reader interpretation, not a demonstrated failure of the quote checker.

## Independent evidence

At measured `HEAD` `65a5c7a663249e0522cc49e4a148424200d9ddfe`, reopened `corpus/knowledge/skill-eval-artefacts-round70.md:58-72`. It says the guide uses “above,” implementation uses `>=`, and the disagreement is only should-trigger equality; at default 3 runs/query and threshold 0.5, equality is impossible for one unique query. It explicitly notes duplicate query strings can create a 3/6 equality and other thresholds can create equality at 3 runs. The specific action at lines 71-72 offers three alternatives, including stating which rule applies.

Reopened `SKILL.md:193`: it keeps comparator reporting but follows it with the categorical “Keep runs × threshold non-integral and query strings unique.” This is a faithful concern in R75Facet03: the standalone recommendation loses the source entry's conditional framing / alternatives. The report's arithmetic is consistent: at threshold 0.5, three runs cannot yield exact equality for a single query scored over those three runs; two runs and one fire can.

Reopened `verifiers/check_skill_evals.py:149-161`: the cited path checks quote length, required terms, pinned snapshot availability, and normalized quote inclusion. It does not evaluate thresholds, per-query fire rates, or run counts. The self-test at `:292` mutates the F8 quote's operator from `>=` to `<` and expects a source-quote verification failure (`:295-303`); it does not test threshold semantics. Therefore it cannot substantiate or enforce the operational advice, as the facet says.

## Cheap check / scope

No runtime or network check was needed: the truth-table cases follow directly from the audited denominator and comparator, and running the verifier would not test the behavior in dispute. A better scoped control would assert the comparison on declared per-query counts and separately exercise duplicate-query aggregation; the proposed control is non-vacuous, but would verify the numeric claim, not overall skill-description quality. No end-to-end behavior or downstream harm is demonstrated by the evidence.

No `lsp` device/status endpoint was available in the mounted tool inventory; evidence was checked by reopening the exact cited source lines. No source changes made.

## Residual risk and gaps

The wording risk survives because the guide sentence reads as a general rule despite the underlying entry's explicit qualifications. The claim should not be inflated into proof that odd run counts are generally required: the report correctly notes it only avoids equality for threshold 0.5 with a unique query. No diagnostics or broader caller analysis was performed; none is necessary to establish this narrowly textual/source claim.
