# R75Facet28 — description-audit candidate

**Facet:** calibration of trigger-rate threshold guidance (round-70 knowledge entry). **Axes:** source fidelity; falsifiability; freshness. Read-only inspection of committed bytes; no live fetch, installs, or experiments.

## Evidence / finding

- `corpus/knowledge/skill-eval-artefacts-round70.md:48-54` advises ~20 labeled queries, ~40% validation, and says the protocol is also held in S124; importantly it explicitly says this is one linked protocol, not independent corroboration.
- `corpus/knowledge/skill-eval-artefacts-round70.md:56-72` identifies a threshold-boundary disagreement: guide wording is “above” while implementation uses `>=`; it bounds the default 3-run, once-listed-query case and names duplicates/even runs/non-default thresholds as ways the boundary becomes observable.
- Committed snapshot `.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md:41-52,77-92` supports the query counts, variation axes, near-miss controls, repeated-run rate, and strict “above threshold” wording. The entry cites S213 as the upstream-revision-pinned replacement for S210 at `corpus/knowledge/skill-eval-artefacts-round70.md:2,6`; its documented recheck is `:8`.
- `corpus/knowledge/skill-eval-artefacts-round70.md:74-80` expressly limits scope: it does not claim clients natively run the artifact; plugin is an opt-in near-miss. This is calibrated, not evidence of client runtime behavior.

## Concrete check/control

For a description audit using this guidance, freeze and report the labeled query set and run count; include a should-trigger query whose observed rate equals the selected threshold (e.g. one trigger in two runs at 0.5), plus a should-not-trigger boundary case. Evaluate and record separately the guide's strict `>` interpretation and any implementation's `>=` result. Keep near-miss negatives sharing vocabulary with the skill (snapshot lines 54-67), and retain a held-out validation split untouched by wording edits (knowledge entry lines 48-54). This makes the boundary discrepancy falsifiable rather than collapsing it into a generic aggregate pass rate.

## Calibration and risk

Observed: cited guide snapshot directly supports the threshold and test-design advice; the entry acknowledges a shared protocol and bounds the client-runtime claim. Inference: a description-audit report that quotes only a single aggregate trigger rate could conceal threshold-boundary disagreement or overfit to explicit prompts. Unresolved: no current live-page check was performed, so freshness beyond the snapshot's recorded fetch/recheck metadata is not established; no claim is made about the behavior of a particular client or current implementation.

**Report trailer**
- Evidence paths (relative to `kotoba-shokunin`): `corpus/knowledge/skill-eval-artefacts-round70.md:2,6,8,48-72,74-80`; `.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md:41-67,77-92`.
- Checks: `read` of committed knowledge entry and committed S210 snapshot; no execution or live fetch.
