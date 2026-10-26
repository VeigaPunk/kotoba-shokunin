# R75Facet34 — description-audit depth/calibration facet

## Finding (observed)

The committed round-70 knowledge entry explicitly limits its scope to the Agent Skills evaluation guides and one reference implementation, and refuses a claim that clients natively run `evals/evals.json` ( `corpus/knowledge/skill-eval-artefacts-round70.md:74-82`). Its F7/F8 distinction is concrete and falsifiable: the guide says should-trigger rate is “above” threshold, while reference code accepts `>=`; the entry derives when equality can occur and recommends de-duplicating query strings or declaring the rule (`:33-34,56-72`). This supports a narrow candidate for a description audit: test whether description-trigger advice preserves its cited source's threshold semantics and distinguishes guidance from implementation. It does **not** support a claim about actual client routing behavior (`:76-82`).

A calibration weakness is the entry's advice to “keep threshold × runs non-integral” (`:69-72`): its own example says duplicate query strings are aggregated per query string and can make the default three-run setting reach 3/6 = 0.5 (`:62-70`). The proposed control itself names deduplication, but any audit counter that only checks an odd run count would miss this equality-producing duplicate case. This is a bounded internal consistency/control risk, not evidence the rest of the entry is false.

## Concrete check/control

For a description-audit candidate based on this entry, run a small committed-byte table over threshold, runs, and duplicate-query multiplicity. Include (a) default threshold 0.5, three runs, one query occurrence (no equality), (b) the same query string repeated twice (aggregate 6 runs, equality), and (c) non-default thresholds where threshold × runs is integral. Record both the guide verdict (`>` for should-trigger, per F7) and implementation verdict (`>=`, per F8) separately. A counter/control must fail if it accepts the duplicate-query equality case as agreement, and must not generalize this result to native client behavior. The source's own boundary statement is the scope guard (`:74-82`).

## Evidence / confidence

Observed lines are from the committed knowledge entry; line references above are lane-relative and were read directly. `corpus/QUALITY.md:37` (Q26) requires each headline clause to be activated by a counter or cited guard, and `:48` (Q37) calls for the cheapest real-input shortcut control; these are suitable controls for keeping a candidate's claim and counter bounded. Confidence: high for what the committed entry states; medium for the control risk as an audit design implication. No source-row quote or underlying snapshot/code was independently reopened in this facet, so source fidelity of F7/F8 and the calculated cases remain unverified here. No edits or checks run.

## Report

Report: `.ufo/waves/round-75/w1/R75Facet34.md`
