---
author: kotoba L1 (round 64, hyaku run 5)
date: 2026-10-24
round: 64
lane: kotoba
---

# Round 64 — lesson (kotoba, hyaku run 5)

Wave-1 seat drafts by `ScribeLesson` (skeleton, M96 row), `RevSourcesGate` (Gate text,
S120 row review), `ScribeQ60` (Q60), `ScoutS120`/`ScoutS049` (measured digests),
`ScribeLOGCorr`/`ScribeSCORECARD` (LOG/SCORECARD material); integrated and measured by
the L1. Errata E1–E3 (`plans/round-64.md`, committed pre-data at `5613392d`) record the
wave-1 falsifications that shaped the instruments before any after-measurement.

## Gate

- **S120 — Practical Mutation Testing at Scale: A view from Google** (Petrović, Ivanković,
  Fraser, Just) — https://arxiv.org/html/2102.11378 — accessed 2026-10-24 (HTTP 200,
  571,600 B, `text/html; charset=utf-8`, sha256
  `15963c3e67b577182fb40318960ca654d70951ddc8827529de82d7f563cc79e8`) — snapshot
  `.ufo/waves/round-64/snapshots/S120.page` (committed this round).
  - `#abstract1.1` (snapshot lines 283-284) — "Mutation analysis assesses a test suite's
    adequacy by measuring its ability to detect small artificial faults, systematically
    seeded into the tested program" (22 words) — the gate quote grounding `teaches`.
    Substring check (Q54): `grep -c` with the whitespace-normalized form → 1 against the
    snapshot; `wc -w` → 22.
  - Support quotes (the round-63 S119 two-quote precedent): `#S1.p1.1` line 324 — "However,
    code coverage alone might be misleading, in particular when program statements are
    covered but the expected program outcome is not asserted upon" (23 words); `#S3.SS2.SSS2.p1.1`
    lines 780-782 — "Equivalent mutants, which are semantically equivalent to the mutated
    program, are a plague in mutation testing and cannot generally be detected
    automatically" (22 words).
  - Identity correction (three seats agree; the plan's candidate was wrong on three
    fields): the authors are Petrović, Ivanković, Fraser & Just — no "Ernst"; the venue is
    IEEE TSE 48(10):3900-3912 (Oct 2022) per Crossref metadata (`10.1109/TSE.2021.3107634`),
    not "ICSE 2021" (that venue belongs to a different paper by the same four authors);
    the preprint is arXiv:2102.11378v2, not 2103.02722 (a Markov-process paper). The row
    cites the opened arXiv HTML artifact; the journal record is Crossref metadata only.
    Version trap measured (`RevSourcesGate`): the arXiv HTML, the arXiv PDF and the IEEE
    PDF word the key sentence differently — the row hashes the artifact it quotes.
- **S049 live context — re-probe appended (`ScoutS049`, 2026-10-24T03:35:37Z).** Default
  `Accept`: HTTP 200, 17,252 B, sha256 `dae9d3ecd7e389fc94ee57d87911fe8d54bae1f00ce451d44303616648247ce0`
  — reproduces the 2026-10-23 receipt byte-for-byte (Vercel cache HIT). `Accept: text/markdown`:
  HTTP 404, 389 B, sha256 `4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1`
  — the request-profile-dependent 404 still reproduces. Control `…/rules` (no `.md`): HTTP
  200, 540,892 B HTML, sha256 `35ff98b0fca637195a670ca8907d32b52642cb311d5455717aedfbc2d91e6ee2`.
  The 2026-10-22 receipt (17,403 B, `884c67ca…`) does not reproduce under either profile.
  Appended to `corpus/SOURCES.md` § Search log; the row and the r63 errata stand unwritten.
- **Census (before → after).** Before: `.ufo/waves/round-64/census-before.txt` —
  `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` exit 0,
  16 W04 (117 rows). After: `.ufo/waves/round-64/census-after.txt` (round end; appended
  below when run).

## Mistakes

- **M96 — class: reference-drift (M95-class recurrence, in the report itself).**
  Evidence: `corpus/lessons/round-63-verifier-spotcheck.md` defect 2 — the round-63
  report cites the two controls "@ `35d44b4b`" while `C1-do-nothing-v31.txt` committed at
  `8c4cefa` and `C2-before-r62tip.txt` at `cbbee56` (each pins base `35d44b4b`
  internally; `git cat-file -e 35d44b4b:<path>` exits 128 for both). M95 mined the class
  from r62 artifacts but named no citation-shape rule, so the r63 report repeated it.
  Captured-by: none at r63 — now **Q60**. Fix: C2 check 2 `control-revs-named` + the LOG
  corrections block (one round-64-suffix line naming both committing revs, the base, both
  basenames, `committed`), shown able to fail: the counter prints `0 of 4` at base
  `078eec4` and the wave-1 seats demonstrated the suffix anchor is load-bearing
  (`LOG.md:2576` already co-located the three tokens).
- **M97 — class: stale-premise (a frozen plan citing identifiers no seat had opened).**
  Evidence: `plans/round-64.md` § Sources named arXiv:2103.02722 / DOI
  10.1109/ICSE43902.2021.00068 / author "Ernst" — three fields, each belonging to a
  different paper; `ScoutS120`, `ScribeSOURCESRow` and `RevSourcesGate` each measured the
  mismatch before any row was minted (the row cites the artifact actually opened).
  Captured-by: none — the plan froze a candidate from memory. Fix: a SOURCES-row candidate
  in a plan is a lead, not a citation; the row is written only from the opened bytes
  (contract rule 1 already says this for rows; the plan now records it for candidates,
  and the Gate above carries the identity correction verbatim).
- **M98 — class: number-drift in a non-author record (recorded, not repaired by us).**
  Evidence: the r63 spot-check's defect 1 quotes the inherited working-tree edit as
  "41+/13-"; every numstat variant measures 82+/29- (`ScoutQualityDebt`,
  `RevSpotcheckCrosswalk` F7). The spot-check file is non-author — never edited; the true
  numbers stand in this round's evidence. Captured-by: none applicable to a non-author
  file. Fix: none by this lane; the routing (commit the edit) stands and is executed
  under C2 check 1.

## Falsify corrections (wave 1)

| # | distinct attack | source seat(s) | disposition as landed |
|---|---|---|---|
| a | check 2 false-green at base via `LOG.md:2576` token co-location | `ScoutQualityDebt` hazard; `RevC2Checks`; `ScribeLesson`; `MutR64Counter` M2 | **fixed pre-data (E1.1/E2)** — round-64-suffix anchor; the pre-named-baseline-LOG self-test arm |
| b | check 4 literal `check(` count unsatisfiable (20 tokens / 19 sites / runtime 23) | `ScribeReportSkeleton` F1; `RevC2Checks`; `ScribeLesson`; `MutR64Counter` | **fixed pre-data (E1.2/E2.4)** — materialized self-test tally + static cross-check |
| c | dishonest counter prints the C1 lines with zero pinning (tautology arms; SM1 still admits) | `RevC1Predicate` Q1 | **fixed pre-data (E3.1)** — kill conjunct + `(sha256, 223)` pin pair in the receipt |
| d | arm 4 maskable at the wrapper (out-of-span `mode` dies on A2's page gate first) | `MutSpanArms` A2; `CriticC1Bound` 3 | **fixed pre-data (E3.2)** — hardened cell; wrapper-level ADMIT/REJECT discrimination measured on the landed bytes |
| e | SM5 "component-only" premise false — judge-reachable witness exists | `RevC1Predicate` Q4 | **E1.3 withdrawn (E3.3)** — the hardened arm 4 pins SM5 through `action_conjunct` too; the deferred wrapper arm moves to the M7–M22 package |
| f | six verdict-flipping lanes beyond SM1–SM6 (M7–M22; M8/M12 admission-flipping) | `RevC1Predicate` Q3 | **debt-recorded** — measured closing package (229/230 assertions, shas `f3c82574…`/`b614e8b1…`) deferred to round 65, named in the SCORECARD Next line |
| g | control rule admits vacuous token scans (1-of-4 at base + 4-of-4 at target) | `RevC2Checks` control-rule; `CriticC2Bound` 1 | **fixed pre-data (E2.5)** — refuse unless `base_closed == 0`; partial-world arm |
| h | BASE_REV relocation guard only blocks green controls, not moved constants | `CriticC2Bound` 2 | **bound-recorded** — tamper-evidence rests on the frozen predicate sentence naming `078eec4…` + the sha256-pinned counter bytes at the measured rev (Q28 freeze discipline) |
| i | M95 class census: 15 absence instances (10 unique pairs), check 2 covers the 2 routed | `ScoutReceiptSweep` | **class repair + bound** — the 8 uncovered pairs named with their committing revs in the LOG census line; the counted bound stays the two routed instances |
| j | SCORECARD r63 annotation cites receipt bytes stale at the cited rev (`C1-g9-measure.txt` at `849a546e` names the 205-assertion wave-1 receipt; the 219-assertion refresh committed at `2ba4547f`) | `ScribeQ60` F2 | **fixed** — round-64 SCORECARD erratum line naming `2ba4547f`; recorded, not headline-counted (E1 disposition) |
| k | token-only matchers green-light inverted statements; one line can serve checks 2+3 | `RevSpotcheckCrosswalk` F5/F6 | **fixed pre-data, then hardened post-data (row n)** — ordered, content-shaped matchers; wave 2 showed the landed matcher still green-lit inverted prose; the hardened matcher is the landed one |
| l | SHONEN box-3 anchor falsified ("B1/B2 both fixed in round 13" — the record says the recipe gap stands) | `ScribeSHONEN` F1 | **fixed** — the refreshed line withdraws the claim, stays `[~]` |
| k' | census grammar trap (adjacency vs reversed forms over/under-flag ~10×) | `ScribeQ60` F5 | **fixed in Q60** — the criterion binds the path-claim form only |

| m | both counting commands re-run independently at tip and base; predicates reproduce byte-exact (`RevW2C1Count`, `RevW2C2Count`, `ScribeW2Dispositions`) | **verified** — C1 223/exit 0 @ `c019919c`, 219 @ base, sha pair reproduced; C2 4 of 4/exit 0 @ tip, 0 of 4/exit 1 @ base, refuse mechanism demonstrated on a 1-of-4 base world |
| n | inverted/swapped/negated/bundled prose certifies (checks 2/3 presence-only); marker+filler credits check 1; note-deletion + cell rewrite credits check 4 (`MutW2ReceiptSubs` M1/M2/M3b/M5c, `RevW2Lesson`, `RevW2Crosswalk2` F2) | **fixed post-data (hardening; predicate unchanged)** — pairing-, direction-, negation-, distinctness-, signature-, and note-marker-aware matchers; one self-test arm per demonstrated shortcut; honest world still 4 of 4, base still 0 of 4 on the hardened bytes; C2's measured pin moves to the close commit with both pins recorded (Q28 second measurement) |
| o | three self-test shortcuts survived the 32-assertion suite (`CriticW2C2Dishonest`; `MutW2Counter` M4; `RevW2C2Count` F1; `RevW2Intent` F2) | **fixed** — hardcoded-axis, dirty-scorecard, missing-rev, guard-skewed tally, substituted control-base, and base-threshold arms added (43 assertions) |
| p | M7–M22 re-derived at judge level: only M8 is judge-reachable admission; M20 also flips; closing package VERIFIED at 229 (`56fb9b3a…`)/230 (`a198aa50…`) shas — wave-1's `f3c82574…`/`b614e8b1…` do not reproduce; M20 survives the package (`MutW2M7M22`) | **debt-recorded with corrected package** — round-65 candidates: M8, M20, the wrapper SM5 arm, and a floors row; E1.3 stands (SM5 not judge-discriminable; the round-64 E3.3 withdrawal is itself corrected here) |
| q | paperwork defects: S120 blank-line table split + §III-B2 caveat mis-cite + notes under Leads; LOG receipts bullet cites absent `noharm-base.txt`; C2 receipts lacked rev/command/exit; noharm FAIL receipt overwritten (`CriticW2Frontier`, `RevW2S120Reopen`, `RevW2Receipts` H1/H2, `RevW2PredWording` F4/F6) | **fixed** — SOURCES table/caveat/placement repaired (old→new logged here: caveat §III-B2 → §VI Related Work `#S6.p3.1` lines 1911-1916); receipts rewritten with command/rev/exit; the failing c019919c no-harm receipt preserved as `receipts/noharm-c019919c-FAIL.txt`, the green b99fb79c run as `receipts/noharm-b99fb79c-OK.txt`; census-after committed |
| r | Sentinel HIGH: the counter materializes and executes `<rev>` code unsandboxed; git calls unbounded (`SentW2Scope`) | **debt-recorded** — lane-internal gate (revs are lane-authored); sandbox + timeouts named for round 65; the predicate's evidence does not rest on hostile revs |


## Routed-input handling

1. G7 `span_missing` pinning arms (measured, 223 assertions, row (t)) → **C1**, landed
   with the hardened arm 4 (E3.2); wrapper-level SM5 discrimination measured on the
   landed bytes.
2. M95 citation-class defect (report controls "@ `35d44b4b`", committed `8c4cefa` /
   `cbbee56`) → **C2** checks 1–2, M96, Q60, and the LOG corrections block; the class
   census (`ScoutReceiptSweep`) rides the same block.
3. S049 request-profile errata → live context: re-probe measured (`ScoutS049`), appended
   to the search log; no row field rewritten.
4. The r63 spot-check's four routed defects map one-to-one onto C2 checks 1–4
   (`RevSpotcheckCrosswalk` bijection); items 5 (C1's deferred arms) and 6 (operator-owned
   SHONEN) are outside the counted predicate by name.

## Status changes

- S120 teaches-cell citation repair (this lesson, wave 2): the productive-equivalent-mutant caveat's section moved `§III-B2` → `§VI Related Work #S6.p3.1, snapshot lines 1911-1916` (old → new logged here per contract rule 2's spirit); the row's other cells stand.
- S120: new row this round, status `mined` at landing (used-by the C1 entry and this
  lesson; both paths committed in the same commit — the E11 landing-order gate stays
  green at the after-census).
- S049: status `mined` unchanged, `recheck 90d` unchanged; the search log gains the
  2026-10-24 re-probe note (append-only; the row's own cells are untouched).
- No other registry row changed.

## Method provenance

- The pinning-arms method: `MutW2V32` §11 (round 63 post-close seat measurement) —
  the SM battery, the four arms, the 20 000-cell equivalent-mutant note; hardened by
  `MutSpanArms` §6 (this round); wrapper-level witness by `RevC1Predicate` Q4 + L1
  measurement on the landed bytes.
- The routed-repairs counter shape: `verifiers/check_r63_routed_repairs.py` (r63,
  errata E2 hardening) — the computed-checks discipline, the pinned-base refuse rule
  (strengthened to `base_closed == 0` per E2.5), the process-arm self-test.
- The citation-class census: `ScoutReceiptSweep` (this round), method = `git cat-file -e`
  per cited pair, committing revs from `git log -1 --diff-filter=A` on master (not
  `--all`; jj keep-refs duplicate adds).
- Sibling method credit: kotodama's R64-M9 lesson (mutant-leg exclusivity) shapes the
  kill-conjunct attribution rule (`ConnSibling`).

## Bounds

- **C1**: the four arms pin SM1–SM6 exactly; the M7–M22 lanes (six verdict-flipping +
  diagnostic) are recorded surviving debt with the seat's measured closing package
  deferred to round 65; SM4/SM6 kills are pre-existing `eligible world` arms, not new-arm
  pins (attribution per the R64-M9 rule); honest padding past 223 assertions is a second
  measurement under Q28, never the declared one.
- **C2**: the counter binds the r63 spot-check's four routed lane-side defects; the other
  13 census instances are repaired by the LOG census line + Q60 but not headline-counted;
  a new self-assessment mismatch class is outside the bound.
- **Carried gate debt**: `check_scoped_rules_v32.py` has no `floors-registry.json` row
  (r62 F17, re-found by `RevC1Predicate` Q2) — the arms could later be deleted with every
  gate green; the round-65 candidate list names it.
- **Quality debt** (`ScoutQualityDebt` dispositions): SentBounds baseline, helper receipts,
  M93 wording, the `LOG.md:2549` clock, the r62 no-harm sentence, the r61 R-b list —
  open; carried to the round-65 Next line with evidence pointers.
