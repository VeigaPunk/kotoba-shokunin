# R75Attack56 — independent attack on R75Facet56

## Scope and revision

Target: `.ufo/waves/round-75/w1/R75Facet56.md`. Lane HEAD observed as `65a5c7a663249e0522cc49e4a148424200d9ddfe`; the target's cited sentence and table were independently reopened at `SKILL.md:166,168-176`. I ran only the proposed bounded detector, `python3 -B verifiers/check_description_thresholds.py --root .`, without `--fetch`; no live fetch was performed.

## Result

**F1: survived, narrowly confirmed.** A plausible contradictory rewrite of the claimed summary sentence does not affect the counter: its output remains `description thresholds backed 7 of 7 clients`, exit 0. This confirms the counter does not validate the summary sentence's classification/payload claims. It does not independently establish that the prose attribution is substantively false: the report itself cites the counter docstring explicitly limiting its scope, so the factual wording “checked by” can reasonably mean that the associated table is checked, not that every summary clause is computed. The substantive concern is the sentence's compressed claim attribution, not proof that its table is unchecked.

The proposed F2 three-column sweep control is not demonstrated by the report's read-only evidence as a necessary acceptance criterion. Its Q30 reading supports calling the negative insufficiently evidenced; but no execution here establishes that the suggested columns or specific grep would give meaningful coverage rather than populated-but-ineffective cells. Mark this as a calibration concern, not a falsified factual statement.

F3 has direct support at the cited bytes: the sentence says unqualified “omp cuts at 99,” while the cited entry says “unless a cached one-liner exists” (`skill-listing-thresholds-round54.md:32-34`); the table likewise describes that branch distinction in the moved router material cited by the facet. No counterevidence found. F4's population distinction is real in the bytes opened: the table has a Cursor 1,024 row (`SKILL.md:175`) while the round-68 lesson's stated list omits Cursor, as cited by the target report. This is a scope/calibration discrepancy, not proof the current count of four is wrong. F5 is a weak/inconclusive control criticism: listed source IDs S062-S064 are cited in the backing entry, and the counter is explicitly a per-client-row counter, not a general basis-pointer validator. Their lack of separate checking alone does not establish a material defect in this sentence.

## Mutation probe (scratch only)

Mutant: replaced only `SKILL.md:166` in an isolated scratch copy with the contradictory text: “A documented maximum is a render cut: every client states 1,024 and all document a cut there, Claude Code and Codex do not cut or budget the listing, omp never cuts …”. Table, entry, and verifier were unchanged.

Detector on pristine bytes: output listed all seven clients `BACKED`, then `description thresholds backed 7 of 7 clients`; exit 0.

Detector on mutant bytes: identical seven `BACKED` rows and `description thresholds backed 7 of 7 clients`; exit 0. **Verdict: survived** (the detector did not kill the summary-prose mutant). This is a valid non-vacuity challenge for a claim that the counter checks the summary text, not a failure of its declared table/source-row contract.

Restoration: restored scratch `SKILL.md` byte-for-byte from lane source; SHA-256 before/baseline and after/restored: `7b1263b5ccbe2ba8b6ffd5d0f4c87ffc5ab3292c9ce792aeee96de283a06464a`. Mutant SHA-256: `78c6dd164134363adc3daa3b643c51fddecbb93cacdde4f8e7895b9f50dce6c1`. Restored detector again returned seven `BACKED`, `7 of 7`, exit 0. Scratch directory was removed.

## Overall verdict

**Partially confirmed; no grounds to accept all five findings as equally material.** Strongest actionable evidence is the counter's intentional scope boundary (docstring lines 19-48) together with the surviving sentence-only mutant, and the missing cache-miss qualifier in the summary sentence. The target report overreaches if it treats that mutation result alone as proof that the summary is false or that every proposed successor control is non-vacuous. No lane source was changed; this report is the only persistent output.

Report: `.ufo/waves/round-75/w2/R75Attack56.md`
