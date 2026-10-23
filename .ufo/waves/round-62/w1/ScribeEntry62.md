# ScribeEntry62 — round-62 C1 absorption map

## Behavior and evidence

Wrote `corpus/knowledge/erratum-absorption-round62.md` at the S118 `used-by` path. It records each erratum class, its frozen IDs/arms and matrix observations, the E2f G7 gap and v3.1 successor boundary, declared bounds, the S118 `paths` quote, and the instrument limits. The successor source is present and its self-test source re-scores the frozen survivors while retaining G9/F6 as a bound; its self-test was not run in this scribe assignment, so no successor result is claimed.

Provenance: S112–S115 are the per-client scope-key sources, S117 is writing-time calibration context, S118 is the Claude Code memory page, and the r61 arm/bounds reference is `corpus/knowledge/scoped-rules-counter-round61.md`. S118's fetch record is named at `corpus/lessons/round-62.md` § Gate; the page snapshot is `.ufo/waves/round-62/snapshots/S118.page`.

## Commands and outcomes

- `python3 -B verifiers/check_erratum_absorption.py --self-test` — exit 0, also recorded in `.ufo/waves/round-62/C1-absorb-measure.txt` (`receipt_rev=3e7aed9b61bbfd83e0c800213b6dfc6da6191f85`): `errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2`; `guard flips: E2 2; E2b 2; E2c 0; E2e 0; E2f 0`.
- `python3 -B verifiers/verify_corpus_integrity.py` — exit 1 at this pre-integration tree: `2/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed, corpus.index.stale_patterns, corpus.index.missing_paths, corpus.pointers.report_total, corpus.pointers.commit_total, corpus.pointers.commit_unresolvable`. The same run reports stale/missing README patterns for the knowledge entry and `corpus/lessons/round-62.md`. The parent confirmed these were mid-landing; the integrator will rerun at the final tree. No index or lesson file was written by this seat.

## Touched surfaces, bounds, and handoff

- **Written by this seat:** `corpus/knowledge/erratum-absorption-round62.md`; `.ufo/waves/round-62/w1/ScribeEntry62.md`.
- **Read for evidence:** round-62 plan/E1 addenda, r61 knowledge entry, QUALITY Q34–Q56, absorption instrument and matrix receipt, v3.1 successor source, S118 source row/snapshot, and the hollow-control receipt.
- **Out of scope:** verifier/counter and successor implementation, S118 fetch/registry, lesson/index/baseline changes, other lanes/fleet state, Git/jj mutation, build/lint/format, and canonical judgment. No tools installed.
- **Limits:** the matrix is arm-level; it does not measure world-level semantics, reviewer entailment judgment, network freshness, or independent provenance of the embedded counter pin. The successor is separate evidence; G9/F6 remains a named bound.

Findings: E2 and E2b are absorbed; E2c, E2e, and E2f survive. S118 supports only the cited `paths` fact. The entry does not claim a successor result or closure of the G9/F6 bound.

## Final entry counts

- `wc -w corpus/knowledge/erratum-absorption-round62.md && wc -l corpus/knowledge/erratum-absorption-round62.md` → `713 corpus/knowledge/erratum-absorption-round62.md`.
- `wc -w corpus/knowledge/erratum-absorption-round62.md && wc -l corpus/knowledge/erratum-absorption-round62.md` → `50 corpus/knowledge/erratum-absorption-round62.md`.

Report: .ufo/waves/round-62/w1/ScribeEntry62.md
