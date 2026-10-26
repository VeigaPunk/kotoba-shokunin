# R75Facet33 — sourced depth / calibration facet

**Scope:** `SKILL.md` line 193, the compact “Testing a skill” instruction. Read-only inspection of committed lane revision `65a5c7a663249e0522cc49e4a148424200d9ddfe` (identified by `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD`). No edits or live fetches.

## Finding

**Observation — adequate support, but a material operability omission.** `SKILL.md:193` says trigger sets label about 20 queries and run about three times, then warns about guide-vs-implementation threshold equality and duplicate strings. The cited knowledge entry is explicit that this is guide advice rather than a normative spec rule (`corpus/knowledge/skill-eval-artefacts-round70.md:13-16`), and distinguishes trigger testing from output-quality evaluation (`:18-21`). Its trigger protocol further specifies ~40% held-out validation, that this set never guides edits, and selecting the best iteration on validation pass rate (`:48-54`). Those controls are absent from the compact skill instruction. This is a sourced-depth opportunity: the skill conveys sampling and threshold mechanics but not the overfitting control that makes iteration results interpretable.

**Calibration:** the warning in `SKILL.md:193` is well-scoped to the cited artifacts, not client behavior. The entry identifies F7 as guide wording (“above”) and F8 as `run_eval.py`'s `>=` (`corpus/knowledge/skill-eval-artefacts-round70.md:33-35`), and carefully refuses a claim that clients natively run the artifact (`:74-82`). Do not upgrade the advice to a universal runtime guarantee.

## Concrete check / control

For a future description-audit candidate using this guidance, preserve the committed guide snapshot and test query set as inputs; freeze a disjoint validation subset before edits; prohibit validation queries from influencing wording changes; compare candidate iterations on validation pass rate; report train and validation results separately. Include a boundary arm with a unique query at exactly threshold × runs = integer (e.g. 1/2 at 2 runs) and require the report to state which comparator it follows. These checks directly cover the omission and the equality discrepancy; they do not establish any client runtime behavior.

## Evidence and limits

- `SKILL.md:193` — compact trigger-evaluation guidance and equality/unique-query warning.
- `corpus/knowledge/skill-eval-artefacts-round70.md:48-54` — repeated trigger runs, held-out validation, best-iteration selection, and its explicit note that the protocol is stated twice rather than independently corroborated.
- `corpus/knowledge/skill-eval-artefacts-round70.md:56-72` — equality disagreement and conditions producing it.
- `corpus/knowledge/skill-eval-artefacts-round70.md:74-82` — scope/refusal of native client-execution claims.

**Inference:** omitting the held-out-selection clause from the skill line weakens its standalone ability to prevent overfit during description tuning. The evidence does not show that any current evaluation actually leaked validation data or that clients execute these files natively. No source-row semantic review was performed in this facet; support assessment is bounded to the committed knowledge entry and its cited rows as represented there.