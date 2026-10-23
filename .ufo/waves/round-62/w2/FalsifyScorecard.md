# FalsifyScorecard — round-62 SCORECARD annotations attack (wave 2)

Seat: `L1kotoba62.FalsifyScorecard` (reviewer, leaf; no subagents). Date: 2026-10-23.
Scope: SCORECARD.md round-62 additions at lane tip `e6da78bbe420722dd18a13182a7c4b64ce02f005` —
the axes-annotation paragraph (line 36), the "**Round 62 completed**" block (line 369), and
"**Next: round 63**" (line 371). Checks: pointer resolution at tip, held scores vs axes table,
band-move absence, capabilities-row absence, and the Next block's supportability.
Lane untouched except this file. Installs: none (RULES.md read; `git`/`sha256sum`/`python3` suffice).
Method note: the working tree is dirty (wave 2 in flight); every verdict below is against the
**committed** tip blob (`git show e6da78b:SCORECARD.md`), and counting commands were re-run on a
sandbox clone `/tmp/r62tip-check` at `e6da78b`, never on the dirty worktree.

## Findings

### M1 — Unfilled template placeholders in the "completed" block (SCORECARD.md:369, committed bytes)

Committed line 369 ends: `wave 1 39 (34 reports, 5 dead), build-completion call 5, wave 2
{W2_COUNT} attack seats; total {TOTAL}.` — literal `{W2_COUNT}`/`{TOTAL}` placeholders ship in the
committed annotation while the sentence calls the round "completed." LOG.md:2565 carries the real
numbers the scribe never pasted back: wave 2 = 39 spawn (17 reviewer / 10 critic / 5 scout /
3 mutation-tester / 2 sentinel / 1 revenger / 1 connector), "Round total 83 seats." A claim-bearing
line with uncomputed placeholders fails this lane's own evidence discipline (every number carries
the command that produced it); a reader cannot re-derive `{W2_COUNT}` or `{TOTAL}` from anything on
the page. (`git show e6da78b:SCORECARD.md | sed -n '369p' | grep -o 'wave 2 {W2_COUNT} attack
seats; total {TOTAL}'` → exact match.)

### M2 — Dead report pointer (SCORECARD.md:369)

`Report `.ufo/reports/round-62/kotoba.md`` does not resolve at tip:
`git cat-file -e e6da78b:.ufo/reports/round-62/kotoba.md` fails; `ls .ufo/reports/` has no
round-62 dir (lane reports stop at round-45; since ~round 46 the convention is the fleet root —
the file exists at `../.ufo/reports/round-62/kotoba.md`, outside the lane, written by
`scripts/hyaku/fleet-commit.sh`). Two defects stack: (a) the path is the dead lane-relative shape —
the r60 annotation in this same file already carries the same dead `reports/round-60/kotoba.md`
shape while r58/r59 rows use `../.ufo/reports/`; (b) even the fleet copy is the last commit-order
item (plan step 8) and lands after this tree, so the pointer is doubly unresolvable at `e6da78b`.
(The dirty worktree's line 369 already reads `../.ufo/reports/round-62/kotoba.md` — the fix in
flight confirms the defect.)

### M3 — "before 0 of 5 committed arm-level receipts" overstates under the control's own criterion (SCORECARD.md:36 and :369)

Both lines assert `before: 0 of 5 committed arm-level receipts`, citing
`controls/absorption-before.txt`. That control's own stated criterion (lines 15–16): a receipt
"(a) names the landed counter sha 5a5adc94 AND (b) records a reject/accept verdict for an instance
of one of the five erratum classes." Verified directly on committed r61 bytes
(`git show a745411c:.ufo/waves/round-61/receipts/C1-worlds.txt`, lines 14–16): the receipt names
sha `5a5adc945e…` and records `world W1 … reject=True arm=A4 … declares no supersedes` (an E2c
conjunct-iv instance) and `world W2 … reject=True arm=A3 … rendering alias` (an E2b A3(b)
instance). Under (a)∧(b) the before-state is 2 of 5 classes with one committed arm-level reject
each, not 0 of 5; the control's exclusion sentence "none runs an instance of E2/E2b/E2c/E2e/E2f"
is false as written. The narrower honest claims survive: no seat attack table was re-scored on the
landed bytes (0 sha-mentions in all five Mut* reports), and no r61 receipt runs the
disabling/guard-mutation direction — but the annotation and control state the broader claim.
(Independent confirmation: sibling seat `FalsifyBeforeState`, same finding, same evidence.)
Impact is bounded — the matrix delta "no two-direction arm-level receipt existed" still holds —
but the SCORECARD carries the false 0 verbatim twice. (The in-flight worktree edit already rewrites
line 36's before-clause to "2 of 5 classes with one committed synthetic arm-level reject … 0 of 5
with both directions" — correct fix; line 369's `before 0 of 5 committed arm-level receipts` was
still unedited in the worktree hunk shown by `git diff`.)

### L1 — "the six surviving errata classes" miscounts and mislabels (SCORECARD.md:371, Next block)

The Next block offers "(1) depth: the six surviving errata classes (E2c condition 5/6, E2e
negation/commented/equals forms, E2f G7) as live-row fixes once the closure upholds the frozen
matrix; the W8 escape class and A2's F6 compound-purpose bound (G9) stay the named residuals."
Two problems against the round's own receipts:

- Off-by-one: the matrix (`C1-absorb-measure.txt:11-17`) leaves **6 survivor instances**, of which
  the v3.1 successor closes **5** and `e2f-compound-purpose-outside-citation` (the G9 bound)
  remains — `C1-v31-successor.txt`: `survivors closed 5 of 6`. The six enumerated items are the
  five closable survivors, not six; and the same sentence names G9 the residual, so "the six … as
  live-row fixes" claims one survivor the round itself proved still survives. SKILL.md:490 (same
  commit) states it correctly: "closes five of the six measured survivor instances (E2c ×2, E2e
  ×2, E2f G7); G9 compound-purpose stays a declared bound."
- Wrong unit: three of five erratum classes survive (E2c, E2e, E2f); the six items are conditions/
  instances, not "classes." The E2e enumeration "negation/commented/equals forms" also names three
  forms across two measured survivors (`e2e-negated-path-key`, `e2e-commented-equals-key`) — fine
  as design intent, imprecise as the count basis.

Not an unsupported ambition — v3.1 demonstrates the class is repairable — but the forward claim
states six fixable survivors where the receipts support five.

### L2 — "both new instruments are registered gates" is underinclusive (SCORECARD.md:36)

Four new `gate` rows landed this round in SKILL.md (tip lines 488–491):
`check_erratum_absorption.py`, `check_routed_repairs_v2.py`, `check_scoped_rules_v31.py`, and
`check_seat_counts.py` (the routed-defect seat-count guard). "Both" refers only to the two
counted-predicate instruments; harmless for the no-capabilities claim (verified below) but
imprecise against the file's own registry.

## Verified clean (re-run, not trusted)

- **Held scores match the axes table.** Axes table (lines 28–29): `depth | 9 | … | owned | 60`,
  `consistency (calibration sub-axis) | 10 | … | owned | 15`. Annotations: "score held 9" (L36/369),
  "consistency row held 10" (L369). Match, and both annotations phrase the hold identically
  ("band move waits on the non-author closure").
- **No band move claimed.** The only verdict words are "held"; L36 explicitly "No band move is
  claimed … (r60 E2 exploratory ruling unchanged)."
- **No capabilities row added; plan declares none.** `git diff a745411c..e6da78b -- SCORECARD.md`
  touches only lines 33–36 (axis annotations) and 366–371 (completed + Next); the Capabilities
  table (307–320) is untouched. L36's "No capabilities row: both new instruments are registered
  gates, not repertoire (AXES.md § Capabilities)" matches plan:228–229.
- **Both counting commands reproduce verbatim at tip** (sandbox clone `/tmp/r62tip-check` @
  `e6da78b`): `python3 -B verifiers/check_erratum_absorption.py --self-test` → prints the quoted
  `errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2`, all six named survivors,
  exit 0; `python3 -B verifiers/check_routed_repairs_v2.py --self-test` → prints the quoted
  `successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6`, exit 0.
  Committed blob shas at tip match the receipts: absorption `afb4ff74…`, v2 `de5e3471…`, frozen
  counter `5a5adc94…` (byte-identical claim holds: `sha256sum verifiers/check_scoped_rules.py` =
  `5a5adc945e…` at tip).
- **Receipt pointers resolve and match.** `C1-absorb-measure.txt` (receipt_rev `3e7aed9b`, the
  quoted line, exit=0) and `C2-successor-measure.txt` (base `f3246d14` `0 of 6` exit 1 → `3e7aed9b`
  `6 of 6` exit 0, lines 31–49) exist at tip with the quoted content. Controls
  `absorption-before.txt`, `absorption-hollow.txt` (hollow exit 1 / label exit 1 / real exit 0 —
  matches L36), `frozen-repairs-dishonest.txt` (frozen scores `[6,6,6,6,6,6,4]` — D1–D6 6 of 6,
  H1 4 of 6 — matches L36), `seat-counts-r61.txt` (65 of 68, missing `RevCounterHistory` named —
  matches L369), `seat-counts-r62.txt` (committed blob: 34 of 39 at rev `3e7aed9b`, five missing
  named — matches "wave 1 39 (34 reports, 5 dead)"; the in-flight worktree receipt's later
  35-of-39/completion-call revision is consistent with "build-completion call 5").
- **Frontier claims.** `grep -c '^| S' corpus/SOURCES.md`: 116 at tip, 115 at `a745411c` — "115 →
  116" holds; S118 row lands with "re-opens S103" text (S103's own row unchanged between
  revisions, so "re-opens" is S118's lineage claim, not an S103 edit — correct as stated). Census:
  `grep -c W04` = 15 in `census-before.txt`, 16 in `census-after.txt` (the +1 is S118's own
  duplicate-url warning), both receipts exit 0 — "census 15 → 16 W04 exit 0" holds. M93 exists
  (`corpus/lessons/round-62.md:25`), Q57 exists (`corpus/QUALITY.md:68`). The v3.1 successor is
  correctly marked "NOT part of C1's counted predicate" (`C1-v31-successor.txt:1`) — consistent
  with erratum E1 item 3.
- **r61 routed-defect claims.** Stray-`n` repair verified: `writing-revision-calibration-round61.md`
  now opens `source:` (LOG.md:2562 item 2). Seat counts per receipts above. C2 freeze sha
  `95ade9be…` matches `sha256sum verifiers/check_routed_repairs.py`. No-harm arm count and Gate
  reject sample are named in LOG.md:2562 items 4–5 (18 PASS = 15+3, not 16+3). W8 escape class has
  committed referents (`MutFixtureEscape.md`, `ExecSelftestArms.md` at r61 tip). "attempt 1
  OOM-killed mid-wave" per LOG.md:2545.

## Residual risk / gaps

- The dirty worktree already contains convergent fixes for M1's wording-adjacent text, M2's path
  (`../.ufo/reports/…`) and M3's before-state on line 36; whether M3's twin at line 369 and the
  `{W2_COUNT}`/`{TOTAL}` placeholders get fixed before the final tree is the L1's open edit. My
  verdicts stand on the committed tip regardless.
- Line 371's other clause — "(2) calibration: the v2 successor's first exercise on fresh routed
  defects (the G-a count against a new round's build subtree), not a rewrite of the frozen six" —
  is a supportable candidate statement (mirrors the r61 Next block and C2's declared scope); no
  defect filed. "Standing debt" items carry over verbatim from the r61 block, minus the dropped
  "(op origin unverifiable from op log alone)" qualifier on helper-invocation receipts — cosmetic.
- Not in scope: mutation coverage of the two gates, S118 re-open verdict, sibling seat reports —
  owned by peer wave-2 seats.

## Verdict

Two actionable calibration defects in the committed annotations — dead `{W2_COUNT}`/`{TOTAL}`
placeholders plus a dead lane-relative report pointer in the "completed" block (M1/M2), and the
overstated `0 of 5` before-state carried twice (M3) — plus an off-by-one in the round-63 candidate
worn by the Next block (L1). Scores, band posture, capabilities posture, and every re-runnable
count verify clean.
