---
author: kotoba L1 (round 65, hyaku run 5)
date: 2026-10-24
round: 65
lane: kotoba
---

# Round 65 — lesson (kotoba, hyaku run 5)

All seat work this round was executed by the L1 directly (accepted host
mapping: this seat holds no dispatch tool; the two L2 waves are prepared under
`.ufo/waves/round-65/` and itemized in the report — the orchestrator dispatches
them between rounds). Self-caught defects below are mined with their red-before
receipts; nothing was found by an external falsifier this round, and the claims
rest on frozen counters + kill batteries committed as receipts.

## Gate

- **S121 — Overcoming the Equivalent Mutant Problem: A Systematic Literature
  Review and a Comparative Experiment of Second Order Mutation** (Madeyski,
  Orzeszyna, Torkar, Józala — IEEE TSE 40(1):23-42, Jan 2014) —
  https://madeyski.e-informatyka.pl/download/Madeyski13TSE.pdf — accessed
  2026-10-24 (HTTP 200, 1,126,684 B, `application/pdf`, sha256
  `bad1b681b1d6d6cea09f0c1e4701618b88dc175b713689c2a6ac43aba07418a3`) —
  snapshot `.ufo/waves/round-65/snapshots/S121.pdf` + extracted text
  `S121.txt` (committed this round).
  - Gate quote (abstract, PDF text line 64; whitespace-normalized substring
    count 1 against the snapshot): "The experiment indicated that SOM in
    general and JudyDiffOp strategy in particular provide the best results"
    (16 words ≤ 25). The abstract sentence wraps two extracted lines
    (64-65) — the row records the normalized form (Q42/Q54 discipline).
  - Support quote (PDF text lines 1174-1176): "Empirical results suggest
    that applying SOMs reduced the number of mutants by approximately 50%,
    without much decrease in the quality of the test suite." (24 words).
  - Identity (read from the opened bytes): authors Madeyski, Orzeszyna,
    Torkar, Józala; venue IEEE TSE vol. 40 no. 1 Jan 2014 p. 23; DOI
    10.1109/TSE.2013.44 (PDF header line 90). The artifact is the
    author-hosted preprint v.2; the publisher record was not opened.
  - **First candidate REJECTED before the plan froze:** arXiv:1309.4818,
    opened the same way (HTTP 200, 40,082 B), is Carlson's "_1-relation on
    the class of epsilon numbers" — a mathematics paper, not the mutation
    work. The rejection and the opened replacement are recorded here (M97
    discipline; see M101 below).
- **Census (before → after).** Before: `.ufo/waves/round-65/census-before.txt`
  — exit 0, 16 W04, 118 rows. After: run at round end (appended below when
  run; the report carries it).

## Mistakes

- **M99 — class: fixture-hermeticity leak (a new test battery inherited the
  live table defaults).** Evidence: the first corrections-battery run FAILed
  three arms — the fixture worlds called `check_governance_citations` without
  pinning `errata=()`, so the REAL `GOVERNANCE_ERRATA` row (LOG.md:2111) leaked
  into 3-line fixture worlds ("past horizon"), and one fixture built a 2-line
  SCORECARD while the correction row named line 9 ("names no live red
  subject"). Captured-by: none — caught by the checker's own fail-closed arms
  surfacing as self-test FAILs (the battery was fixed before landing; the
  landed self-test is green at 1862 assertions). Fix: every fixture-world call
  pins `errata=()` / `corrections=` explicitly, and the mechanism's default is
  `corrections=()` with the live table passed only by `main()` — shown able to
  fail: `.ufo/waves/round-65/receipts/M99-fixture-leak.txt` regenerates both
  bug shapes (status=FAIL, named classes) in a sandbox world.
- **M100 — class: self-referential citation (the correction text re-imports
  the disease).** Evidence: the first appended correction notices wrote the
  stale and corrected tokens in BACKTICKS; the scanner reads backtick spans,
  so each notice line itself became a new dead subject (live run FAILed on
  LOG.md:2619-2621 — the notices' own tokens). Captured-by: none — the live
  gate named the lines immediately. Fix: the notices quote the tokens in
  double quotes (not a scanned span), and the correction row's byte-pin makes
  any re-wording drift fail closed; shown able to fail:
  `.ufo/waves/round-65/receipts/C2-selfreference-redbefore.txt` — backticked
  notice: status=FAIL (the notice token named); quoted notice: status=PASS.
- **M101 — class: stale-premise candidate frozen from memory (M97 recurrence,
  caught before data).** Evidence: the round plan's first S121 candidate was
  arXiv:1309.4818, recalled as the second-order-mutation preprint; opened
  2026-10-24 it is a math paper (title "[1309.4818] Carlson's _1-relation on
  the class of epsilon numbers"), rejected in the Gate above, and the plan
  froze only the opened replacement. Captured-by: M97's own rule (a plan
  candidate is a lead, opened before it is named — `corpus/lessons/round-64.md`
  M97). Fix: held — the rule caught it at planning time, before any seat or
  receipt spent work on the wrong identifier; the row cites the artifact
  actually opened (S121).

## Status changes

- S121: new row this round, status `mined` at landing (used-by the C1
  knowledge entry and this lesson; both paths committed in the same commit —
  the E11 landing-order gate stays green at the after-census).
- No other registry row changed (append-only; no in-place cell edits this
  round — the r64 S120 breach form is not repeated).

## Method provenance

- The closing-package arms: `RevC1Predicate` §3 (wave 1, round 64), counts
  re-measured by `MutW2M7M22` §4 (wave 2, round 64) — the quoted package shas
  did not reproduce and were dropped; the landed bytes recompute the pin.
- The four new arms' lanes: `MutW2M7M22` §5 (M20), §8a (SPAN_FIRST/SPAN_LAST),
  §8b (M11 exact-case), all measured at judge level on the round-64 landed
  bytes.
- The governance-corrections shape: the checker's own `GOVERNANCE_ERRATA`
  precedent (round 47) — same horizon/byte-pin/fail-closed discipline,
  extended from recorded-absence to recorded-correction.
