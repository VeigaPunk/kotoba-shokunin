# Kb80R05FleetGrammar — seat report (scout, round 80 w1)

Assignment: fleet grammar precedent for the r80 external-commit grammar class. Does any gate
under `/home/vgpnk/Projects/shokunin/*/verifiers/` already classify `owner/repo@<hex>` (or
third-repository) commit citations? Verdict: novel ground or re-derivation? Publish findings
with file:line evidence.

## What I ran (read-only; no lane files touched, no scratch needed)

- Lane inventory: only `kotoba-shokunin` has a `verifiers/` directory in the fleet
  (`for d in {FLEET}/*/; do [ -d "$d/verifiers" ] && echo …` → 1 hit, 61 top-level `.py`).
  Revenger has 12 gate-like `.py` under `corpus/`; kake has `scripts/citation_lint.py`;
  kama has `tools/round54-cited-path-check.py`. No other lane has gate files (fleet-wide
  `find … -name 'check_*.py' -o -name 'verify_*.py'`, plus `grep -rln cat-file …`).
- Directory-scoped grammar grep over kotoba's 61 verifiers
  (`owner/repo|@<hex>|commit_external|foreign|@hex|third.?repo|external.?commit`): zero hits
  for any external/third-repo commit grammar; "foreign" hits are only the SKILL.md
  client-marker guard.
- Fleet-wide `.py` sweep for `owner/repo|@<hex>|commit_external|third.repo|external.commit|
  external.repo` + inspection of every commit-resolving gate found.
- History: M102/M103 (corpus/lessons/round-66.md:18,32), Q61 (corpus/QUALITY.md:76),
  r53 D2 (.ufo/waves/round-53/falsify/W2CriticDrift.md:117), M45 (round-54.md:13),
  r54 spot-check (round-54-verifier-spotcheck.md:37,146-148), r55 carried row (round-55.md:57),
  r80 plan (plans/round-80.md:11,24).

Note on method: the seat prompt's one-line glob grep (`{FLEET}/*/verifiers/*.py`) returned
nothing on the first pass — a tool glob-expansion miss, not evidence. All verdicts below rest
on the directory-scoped greps and file inventory, which are reproducible.

## Findings (full evidence in the build file)

1. **No fleet gate classifies `owner/repo@<hex>` citations.** Kotoba's two corpus gates define
   the resolution set as {lane repo, fleet root} only (`verify_corpus_integrity.py:600-612`;
   `verify_corpus_independent.py:493-499`) and the token model as bare 7-40 hex
   (`verify_corpus_integrity.py:151-153`). No `commit_external` symbol exists in any of the 61
   verifier files.
2. **The class is a re-derivation of recorded ground.** M102 (round 66) named "foreign-
   repository commit misclassified as unresolved"; r53's D2 critic note proposed the exact
   instrument fix ("classify `cfb894a5` as an external-repository commit in the instrument,
   with a self-test arm, or quote it"). Rounds 53–55 took the "or quote it" evasions (in-place
   edit = M45; `cae8f2ea` rewording); r66 fixed only the fleet-object half (bare-hex fleet
   citations now resolve). The third-repo half stayed unresolved-by-construction and is now the
   C1 blocker.
3. **Nearest fleet neighbors are different mechanisms:** kake's `EXTERNAL_RE`
   (`kake-shokunin/scripts/citation_lint.py:45-47,167-168`) suppresses dead-citation
   violations on lines naming a fixed keyword list of external repos + a manual adjudication
   ledger — line-keyword suppression, not token grammar, and exclusion without a named INFO
   class. Kama's upstream class (`kama-shokunin/tools/round54-cited-path-check.py:529-556`)
   requires evidence URLs to equal ONE frozen owner/repo pin (fails closed otherwise).
   Revenger SM5 resolves lane-only with an erratum escape (`revenger-shokunin/corpus/
   self_assessment_check.py`). None detects `owner/repo@<hex>` by grammar or counts it INFO.

## Answer to the seat question

The r80 grammar-class fix is **a re-derivation of an existing, recorded class (M102/r53-D2)
but novel as a gate mechanism**: no gate under the fleet root tokenizes `owner/repo@<hex>` or
holds a named external-commit INFO class. E05/Q75 may claim the mechanism as new work; they
must cite M102 and the r53 D2 proposal as the class's lineage, and must not claim the
underlying lesson (external-repo citations ≠ unresolvable defects) as newly discovered.

## Deliverable

Published: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80R05FleetGrammar.md`
(same content, evidence-first layout). Peer Kb80E10Battery notified this is a verdict memo,
not a stack patch. No scratch dir was created; nothing to remove.

VERDICT: Re-derivation of the M102/r53-D2 class, NOVEL as a mechanism — zero fleet gates classify `owner/repo@<hex>` third-repo commit citations (nearest: kake keyword-line suppression, kama frozen upstream pin, revenger lane-only); kotoba's corpus gates resolve lane→fleet only and have no `commit_external` symbol.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80R05FleetGrammar.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80R05FleetGrammar.md
