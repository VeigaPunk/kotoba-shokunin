# Kb80E05GrammarFix — C1 repair 5: the external-commit grammar class (executor, leaf)

Base `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`. Deliverable form: patches + receipts under
`.ufo/waves/round-80/build/`, no lane edit (freeze discipline). Consumed peer bytes read-only:
`Kb80E04DeadPointer.patch`, `Kb80E02Symlink.patch`, `Kb80E03IndexBaseline.patch`,
`Kb80L01Grammar.md` (scout map), `Kb80S01Lesson.md`, `allowed-tools-surfaces-round80.md`,
`Kb80E13FixtureGuard-REFERENCE-grammar-class.diff`. I dispatched no labrat (a leaf; the grammar map
already existed from the scout seat).

## What the class is (and what it is not)

`commit_external` is a counted, named **INFO** class in BOTH corpus gates, computed independently:

1. **Grammar arm (preventive).** A backticked commit token that itself carries an `owner/repo@`
   binding (`commit `owner/repo@<hex>`` — the plan's named grammar, and the
   `owner/repo@`-immediately-prefixed backticked-hex shape, whose captured token ends in `@`) is
   `commit_external`, never `commit_nonhash`. Interception happens **before** the not-hex branch.
2. **Line-scope arm (the live repair).** A bare hex token that fails resolution in the lane repo
   **and** in the declared fleet root (Q61 precondition — the divert sits *inside* the existing
   `if not commit_resolves(...)` branch, so lane-only and fleet-only tokens keep their exact current
   resolution and the fleet hop is untouched) and whose **citing line** explicitly names a third
   repository (a `github.com` / `raw.githubusercontent.com` repository URL, or an `owner/repo@`
   binding) is `commit_external`.

The Q61 quote / code-span exclusion runs first and is unchanged. Why line scope and not a
token-bound rule: `corpus/SOURCES.md:172` (S231) names `mistralai/mistral-vibe` only in the row URL
and title — no in-line owner/repo — so no token-level rule can reach it (scout finding 3,
`Kb80L01Grammar.md`; plan Addendum 2).

Neither gate gains a CHECKS/CHECK_IDS row, so the class can never be a drift class and needs no
baseline entry (precedent: `commit_truncated`, `commit_quoted_excluded`). It is observable as
`observed.corpus.commit_external` (+`_detail` sites) and `observed.commits.commit_external`
(+`_detail`) in `--json`.

## Line accounting (hard bound)

| stack element | added | deleted |
|---|---|---|
| base, `check_assertion_floors.py` | 22 | 3 |
| E04, `verify_corpus_integrity.py` | 17 | 0 |
| **E05** `verify_corpus_integrity.py` (+11/−2) + `verify_corpus_independent.py` (+10/−3) | **21** | **5** |
| **six-instrument total vs `072048fa`** | **60 = LINE_CAP (E5)** | 8 ≤ 60 |

Exactly at the cap: **zero added-line headroom remains** — any further line in the six instruments
busts `instrument-size`. Flagged for the L1 rather than pre-spent.

## Evidence (command → own exit status, no pipelines; receipts in `build/`)

| what | result |
|---|---|
| patched self-tests (`verify_corpus_integrity.py --self-test`) | **exit 0**, 165 assertions, 0 failures; new arm `cites/commit-external` = (2,1,0) |
| patched self-tests (`verify_corpus_independent.py --self-test`) | **exit 0**, 106 assertions, 0 failures; `ok 91 - commits: external is INFO` |
| red-before: **unpatched** gates over the base tree | exit 1 / exit 1; `commit_total 46, unresolvable 2, nonhash 0`, `commit_external` **absent**; sites `SOURCES.md:171`, `:172` |
| class live over the base corpus (base + E05 only) | both gates `46 / unresolvable 0 / nonhash 0 / external 2`; remaining reds are not this repair's (`corpus.index.unindexed 1`, `corpus.pointers.report_dead 1`) → exit 1 |
| composed C1 stack (E02 + E03 + E04 + E05 + peer drafts `corpus/lessons/round-80.md`, `corpus/knowledge/allowed-tools-surfaces-round80.md`), commit `87ef90b`, baseline refreshed (`refresh-corpus-baseline.py` exit 0; 144→154 tracked, 99→109 report_total, 43→46 commit_total) | **integrity exit 0, independent exit 0**, 0 DRIFT rows each; `46 / 0 / 0 / 2` |
| resolution-precedence probe (lane sha + fleet sha on third-repo lines; absent hash without marker; `commit `o/r@bbbbbbbb``; the live token) | both gates agree: lane and fleet tokens **resolve** (neither external nor unresolvable), absent-unmarked stays `commit_unresolvable`, grammar token is `commit_external` (not nonhash), live token is `commit_external` |
| mutation M1 (line-scope divert removed) | both self-tests exit 1 (`got (1,2) want (2,1)`), live `external 0 / unresolvable 2` |
| mutation M2 (grammar divert removed) | both self-tests exit 1 (`got (1,1) want (2,1)`) |
| application order | E04→E05 and E05→E04 both apply cleanly; composed integrity blob identical |
| marker blast radius | of 55 corpus citation lines, 4 carry a third-repository marker; 2 of those are quote-excluded upstream of the class (`round-53.md:44`, `round-54.md:13`), 2 are the live sites |

Blobs for `INSTRUMENT_PINS` (published in `Kb80E05GrammarFix.blobs`):
`verifiers/verify_corpus_integrity.py 68ccce1c152c915e16893a5157c9d5878df779fb` (E04+E05),
`verifiers/verify_corpus_independent.py e887de71892ecfc6be5b3f47e362ce8a766c5c89` (E05);
E05-alone-on-base integrity blob `678a0d500361229f1b9eda54771d102146f3998d`.
Patch sha256 `a4345d34d3a8e35d7697b5abc05d077c2bb43e49e636edd6937590b1b223a2d3`.

## Residuals — named, not repaired (calibration)

- **R1 (class width, C01's point).** Line scope is spoofable by construction: a fabricated hash
  placed on a line that already names a third repository is classified `commit_external` instead of
  `commit_unresolvable`. Measured live blast radius today: exactly the 2 blockers (4 marker lines,
  2 quote-excluded upstream). Narrowing to token-bound attribution would fail Addendum 2's S231 case
  (no in-line repo) — this is the L1's declared trade, and the arm is pinned both ways in self-test.
- **R2 (provenance, N01/V04's point).** The class cannot detect a *false* attribution: S230
  (`SOURCES.md:171`) attributes mistral-vibe's commit `7bb48f21…` to `badlogic/pi-mono`. M45 forbids
  rewriting the row; the lesson draft already records it (`corpus/lessons/round-80.md:44`, M80-3).
  The class count of 2 is a resolution-class statement, not a provenance endorsement of `:171`.
- **R3.** Zero added-line headroom (60 = cap after E5).
- **R4.** The grammar arm is preventive only: the corpus has **0** `commit `owner/repo@<hex>``
  citations today (the 27 `owner/repo@` occurrences are prose outside the backticks and invisible to
  `COMMIT_RE`); the probe pins its behaviour so it cannot silently rot into `commit_nonhash`.
- **R5.** Both self-test assertion totals move (+1 each: 165 / 106); any harness pinning the old
  totals must be updated.

VERDICT: The external-commit grammar class lands in both corpus gates as counted INFO `commit_external` (live: `commit_unresolvable` 2→0, `commit_external` 2 = `SOURCES.md:171-172`, `commit_total` 46 unchanged, `commit_nonhash` 0), with lane/fleet resolution and the Q61 quote exclusion byte-for-byte preserved, both self-tests green with red-before arms that fail under M1/M2, and the composed C1 stack green on both gates (exit 0) at exactly 60/60 capped added lines (21 for E05).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E05GrammarFix.patch; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E05GrammarFix.blobs; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E05GrammarFix.receipts.txt
