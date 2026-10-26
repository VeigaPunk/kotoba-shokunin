# R75Attack01 — attack on R75Facet01

## Axes
Depth and calibration, matching the target. Verdict: **survives, with a material current-revision qualification**. The semantic blind spot is directly established; the suggested independent review is a meaningful, non-vacuous control, though it does not itself supply a reproducible adjudication procedure beyond requiring row-by-row evidence.

## Independent evidence
- At measured `65a5c7a663249e0522cc49e4a148424200d9ddfe`, `verifiers/check_skill_evals.py:125-175` checks quote/key-term/snapshot and source-row linkage plus the presence of the entry path in SKILL.md; it never compares fact prose or the SKILL sentence's meaning against the quoted source. Its own contract at lines 23-26 explicitly says those checks do not prove faithful interpretation and that the half is settled by a non-author spot-check. This supports the facet's central observation.
- `corpus/lessons/round-70.md:238-244,270-278` independently records the 11/13 junk-world result and the exact weakness; it also states the historical depth content rests on a non-author spot-check, not the counter. This is not evidence that the current candidate has itself been semantically adjudicated.
- Re-ran the safe, read-only command `python3 -B verifiers/check_skill_evals.py --rev 65a5c7a663249e0522cc49e4a148424200d9ddfe`: it reported `skill eval facts backed 1 of 8`, exit 1, with F1–F7 saying S212/S213 have no pinned snapshot. Current `corpus/knowledge/skill-eval-artefacts-round70.md:27-34` cites S212/S213, whereas the verifier's `SNAPSHOTS` map at `verifiers/check_skill_evals.py:46-56` only maps S209–S211. Thus do not describe the current run as an 8/8 result; the 8/8 figure is historical r70 evidence, as the facet correctly labels it.
- `SKILL.md:193` states the guidance and points to the entry, but this observation alone cannot settle whether its paraphrases are source-faithful; the proposed source-line-by-source-line non-author check addresses exactly that gap. Its rule to keep counter and semantic review separate is a useful control, not a claim that the checker proves semantics.

## Verdict and residual risk
No counterexample falsifies the central claim. The report is well-scoped in distinguishing historical weakness from the present result and does not allege an unsupported client-native runtime. Its proposed human control is non-vacuous because it requires per-fact and per-SKILL-sentence evidence at exact supported scope, but reviewer calibration/consistency is not assured by that prose alone. Current verifier's pinned-source-ID mismatch is a separate observable gate limitation, not a reason to treat a failed run as semantic evidence.

## Verification gaps
No LSP device/server is mounted in this environment; caller/definition/diagnostics requests were unavailable, so evidence was checked by direct file reads, not semantic grep. No live fetch or model run was performed. The verifier command above was run locally and failed as stated.

Report path: `.ufo/waves/round-75/w2/R75Attack01.md`
