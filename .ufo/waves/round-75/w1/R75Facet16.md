# R75Facet16 — description-evaluation threshold rule

## Finding (observed)
A distinct, concrete calibration candidate is `SKILL.md:193`: its trigger-evaluation advice says to keep `runs × threshold` non-integral and query strings unique, citing the round-70 artefact. The cited knowledge entry explicitly labels its facts as non-normative guide advice (`corpus/knowledge/skill-eval-artefacts-round70.md:15-16`) and locates the exact discrepancy: guide says should-trigger passes *above* threshold, while the reference code uses `>=` (`:33-34`, `:58-70`). The entry further says default 3 runs at 0.5 cannot equal the threshold for one query string, but duplicate strings aggregate to 6 runs and can reach 3/6 (`:62-70`).

This supports a narrow, falsifiable claim about the two specified sources and the described counting behavior; it does not support general claims about all clients or native execution. The entry itself correctly refuses the latter at `:76-82`.

## Control / concrete check
At a pinned commit, independently inspect the committed knowledge entry, its cited committed snapshot hashes, and the exact guide/reference lines; then hand-calculate or run a tiny local truth table for unique versus duplicate query strings and threshold × run counts (including the equality case) against each stated predicate. A useful control pair is one should-trigger query at an even run count with exactly half triggers: expected disagreement (`>` fails, `>=` passes); and odd 3 runs at threshold 0.5, where equality is unreachable. Keep this as source-rule calibration, not a description-quality outcome claim. No live fetch or execution was performed for this report.

## Evidence and limits
- `kotoba-shokunin/SKILL.md:193` — downstream advice/citation.
- `kotoba-shokunin/corpus/knowledge/skill-eval-artefacts-round70.md:1-8` — source identities, snapshot pins and recheck contract.
- `kotoba-shokunin/corpus/knowledge/skill-eval-artefacts-round70.md:33-34,58-72` — located rule discrepancy and derived conditions.
- `kotoba-shokunin/corpus/knowledge/skill-eval-artefacts-round70.md:76-82` — explicit scope/refusal.

Confidence: high that the committed text makes this bounded, testable claim; no independent reproduction of the source snapshot contents in this seat. Remaining unknown: whether the current committed verifier still exercises the duplicate-query/equality cases; this report did not inspect or run it.

Report trailer: `kotoba-shokunin/.ufo/waves/round-75/w1/R75Facet16.md`