# R75Attack07 — independent falsification

## Verdict

**Central factual claim survives, with a material qualification to the proposed control.** At measured `HEAD` `65a5c7a663249e0522cc49e4a148424200d9ddfe`, `SKILL.md:193` describes the guide's should-trigger pass as strictly above threshold and `run_eval.py` as `>=`, and recommends non-integral runs × threshold. The cited source snapshot independently confirms those semantics: `S210-optimizing-descriptions.md:92` says “above”; `.ufo/waves/round-70/snapshots/S211-run_eval.py.txt:230-234` implements `>=` for positive and `<` for negative cases. At equality the positive-case classifications differ; e.g. 1/2 runs at threshold 0.5. The report appropriately limits this to documentary protocol and does not claim a description was tested or that scores predict general routing.

## Attack on the proposed control

The suggested validation control is not an untouched final generalization check if it is also used to select the best iteration. The source guidance explicitly directs selection “by its validation pass rate” (`S210-optimizing-descriptions.md:160-163`), while the report says to prohibit validation use “in choosing wording” and also freeze the iteration-selection rule (`R75Facet07.md:19`). Freeze prevents changing the rule after seeing scores, but selecting the winning wording/iteration by validation still makes the validation set part of model selection. The guide itself supplies the remedy the control omits: after selection, evaluate on fresh 5–10 queries never used during optimization (`S210-optimizing-descriptions.md:171-175`). Therefore the report's “held-out” result should be described as validation-set selection/performance, not an independent estimate of generalization; retain a fresh test set if it intends that stronger reading.

The proposed deliberately-overfit control is also not a deterministic negative control as phrased: inserting training-query wording does not guarantee no held-out improvement (queries may share that concept, and finite samples vary). Define a specific mutant and expected outcomes from frozen query labels, or treat its observed score as diagnostic rather than a guaranteed non-improvement.

## Scope / check limits

The comparator check is a safe source-level check, not an execution of the model-trigger experiment. No r75 query set, candidate scores, or execution receipt are claimed here; running a live client/model test would exceed the cited evidence and was not necessary to falsify the control language. No lane files were changed.

## Evidence paths

All paths relative to `kotoba-shokunin`: `SKILL.md:193`; `.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md:92, 136-163, 171-175`; `.ufo/waves/round-70/snapshots/S211-run_eval.py.txt:229-234`; `.ufo/waves/round-75/w1/R75Facet07.md:15,19,23`.
