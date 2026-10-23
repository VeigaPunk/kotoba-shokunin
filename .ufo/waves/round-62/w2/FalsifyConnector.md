# FalsifyConnector — round-62 wave-2 sibling-overlap re-scan (the two new surfaces only)

Seat: FalsifyConnector (leaf; no dispatch, no background jobs, no model calls). Date 2026-10-23.
Read-only: every path outside this file was opened read-only (`read`, `grep`, `git -C <lane>
rev-parse|log|diff|ls-files` only); no lane, sibling, fleet, `.ufo/state`, MANIFEST or index file
was written. Installs: none. Blockers: none.

Scope (assignment): re-scan sibling overlap on the two new round-62 surfaces only —

- **Shape A — erratum-absorption audit**: frozen attack instances scored through a landed
  counter's own arm functions; *absorbed* = rejected under the committed counter AND accepted
  when only that erratum's guard is disabled in-process; seeded absorbed/surviving controls;
  sha256-pinned subject counter, exit 2 on byte drift (`verifiers/check_erratum_absorption.py`).
- **Shape B — honest-pass counter hardening**: a successor counter whose counted predicate
  carries BOTH legs — dishonest rejected 6 of 6 AND honest passed 2 of 2, computed from input
  blobs — plus a self-derived count (G-a `git ls-tree` census) (`verifiers/check_routed_repairs_v2.py`).

Answers: **(1) no sibling now holds an instrument of either shape** (wave-1 conclusion upheld at
instrument level, with two nearest-evidence corrections below); **(2) yes — the absorption
criterion borrows technique classes that no landed round-62 artifact cites**, exactly the four
credits wave 1 committed to the lesson/registry rows and routed items.

Kotoba bytes audited: named landed tip `e6da78bbe420722dd18a13182a7c4b64ce02f005` (corpus +
registry + successor, 2026-10-23T18:27:58-03:00); working HEAD at scan time
`e424f2a4a2d65011ba3697de1aaeb2e3665863a4` (wave-2 falsification + C2 hardening, 18:43:02-03:00).
Command: `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin log --format='%cI %h %s' -6`.

## Scan basis and commands

1. Index lines of all 20 sibling `corpus/README.md` (current bytes), shape-vocabulary sweep
   `grep -ciE 'honest|dishonest|erratum|mutation|mutant|guard|hollow|survivor'` per file →
   audio 0, chousa 29, game-dev-2d 1, game-dev-3d 1, kagi 7, kaidoku 20, kake 6, kama 11,
   kasegi 5, kengaku 17, kotodama 14, kumitate 28, lore 2, mado 6, mori 13, revenger 0,
   souji 5, tabi 8, tameshi 54, tsukuroi 6. Every matched index line was read (representative
   lines quoted below). No index row in any sibling names an instrument of shape A or shape B.
2. Body-level corpus sweep (goes one step past wave 1's index-lines-only bound, which wave 1
   itself flagged): `grep -rli 'absorb' <sibling>/corpus/` → game-dev-2d 542, game-dev-3d 327,
   kotodama 45, kengaku 38, tsukuroi 33, tabi 28, tameshi 24, kagi 22, kumitate 21, chousa 20,
   mori 15, audio 12, kaidoku 11, kama 11, mado 12, kasegi 8, kake 7, revenger 4, souji 2,
   lore 0 files. Classified by mechanism (context extract `grep -rhoiE '.{28}absorb[a-z]*.{28}'`):
   disposition/vocabulary ("report, never absorb" adjacency boilerplate; linguistics in kotodama;
   "recorded, not absorbed" in tabi/tsukuroi), argument-parsing ("absorbed by a want=[] arm",
   audio), locator probing ("not absorbed by the javascript locator", kengaku) — and **one
   measured mechanism**: game-dev-2d (below).
3. Sibling movement since the wave-1 pins (`ConnSibling.md:32-38`), command
   `git -C <lane> rev-list --count <pin>..HEAD` + `git -C <lane> diff --numstat <pin>..HEAD --
   corpus/README.md`: audio 0/0+0, **chousa +3 commits** (README 0+0), game-dev-2d 0, game-dev-3d 0,
   kagi 0, kaidoku 0, **kake +1** (README 0+0), **kama +4** (README +23), kasegi 0, kengaku 0,
   kotodama 0, kumitate 0, lore 0, mado 0, **mori +2** (README +9), revenger 0, souji 0, tabi 0,
   **tameshi +8** (README +13), tsukuroi 0. All new index rows and new files since the pins were
   inspected (diffs shown per lane below); none is either shape.
4. The two routed siblings read in full: chousa round-35 erratum handling
   (`chousa-shokunin/corpus/lessons/round-35.md`) plus its landed successor round 36
   (`lessons/round-36.md`, the +3 commits); kumitate round-48 freeze-before-data
   (`kumitate-shokunin/corpus/lessons/round-48.md` +
   `corpus/knowledge/counter-amendment-discipline.md`, admitted round 49, rule D49
   `probe/doctrine49-probe.mjs`).

## (1) Does any sibling now hold an instrument of either shape?

**Shape A — no.** No sibling index row, and no sibling corpus body found by the sweeps, names an
instrument that re-runs frozen attack instances through a *landed* counter's own arm functions
under a sha256 pin with a guard-disable flip direction. Nearest neighbours, all mechanism-distinct:

- **tameshi** (method owner, unchanged in kind by its +8 commits): `guard-kill-closure.md` §1 —
  "a guard G is covered … only when (a) pristine green … (b) kill: the selftest exits nonzero
  when G's single-occurrence guard text is removed (the mutant applied to a copy)"; plus the
  meta-cheat/incidental-kill exclusions (`knowledge/guard-kill-closure.md:14-29`). Tameshi mutates
  a *copy of the tool's text* and requires a *selftest* to fail; kotoba replaces a *guard function
  in-process* and requires the *instance verdicts to flip to accept* against a sha-pinned landed
  counter. Same two-legged attribution family, different object, different direction, no erratum
  classes, no absorption predicate. The +8 commits are a round-35 index repair (three lagging
  entries: `runner-tally-audit-v2`, `survivor-fixture-minimization`, `witness-equivalence-rule`)
  and `tools/tally-audit-v3.py` — mutation-witness/tally work, not shape A.
- **game-dev-2d** (new finding, missed by wave 1's index-only bound): `corpus/live/r66-scribe`,
  `r67-*`, `r68-*` carry a *measured* absorption mechanism — an allowlist entry **absorbs** a
  forged `ERROR:` line (verdict-inert), a foreign entry does **not** absorb, a second `ERROR:`
  (count==2) defeats absorption (`corpus/live/r66-scribe/observations.md:33-41`,
  `r67-critic/matrix_results.json`, `r68-boundary/drive_landed.py:124-132`). Mechanism: classifier
  line-allowlisting. Not shape A (no erratum classes vs a landed counter, no guard-flip
  attribution, no sha pin), and it lives in live scratch the lane's own index calls "ignored and
  disposable" (`corpus/README.md:22,24`). **Vocabulary collision #2** — see (2).
- chousa r35/r36, kumitate r41–43 `gate-mutants`, kengaku/kama/mori mutation arms: input- or
  gate-byte mutants with kill rules; none scores errata against landed counter arms.

**Shape B — no sibling holds the positive honest-pass arm; wave 1's nearest-evidence row is
corrected twice.** The distinguishing kotoba leg is *honest input must PASS inside the counted
predicate* (`honest passed 2 of 2` in the frozen line). What siblings hold:

- **kumitate round-40** (predates the wave-1 pin; index rows `kumitate-shokunin/corpus/README.md:117,119`):
  `scripts/anchor-truth.mjs --open REV` — declared before `attacks_accepted=20/26` with
  `benign_clean=10/10`; after `attacks_accepted=0/26` with `benign_clean=10/10`
  (`corpus/lessons/round-40.md:26-29`). A two-sided attack/benign hardening predicate — the
  closest sibling instrument to shape B. Wave 1's row (b) said "no sibling index shows a hardened
  counter with an honest-pass arm; siblings recorded honest stops instead" and cited only the
  failure family (kaidoku r32, kake r26/27): its surface-b sweep (`self-derived|self-count|honest`)
  cannot see "benign". Correction: kumitate's index *does* show a hardened probe with a
  benign-clean arm. Distinction that keeps shape B kotoba's: `benign_clean` is a no-harm leg
  (benign edits must not trip), not a positive pass leg (honest trees must score 6 of 6); and the
  object is review-record anchors, not repair receipts. Stated as a ruling, not smoothed.
- **kumitate round-48 A48** (the routed freeze-before-data sibling): control MutSummaryForge M2 —
  a round-gate selftest failing one case while printing a self-consistent `62/62` summary and
  exit 0 — read `ROUTED_HELD` 3/3; A48 (per-case line corroboration) kills the forgery at RG742
  "without disturbing honest suites" (`A48-stab-r47-f00cf278.txt` 5/5)
  (`corpus/lessons/round-48.md` Mistake 3; `counter-amendment-discipline.md` C4–C7). Forgery-kill
  + honest-undisturbed — again a no-harm leg outside the frozen predicate, not an honest-pass arm
  inside it.
- **chousa round-36** (landed after the wave-1 pin, +3 commits): engine-swap canary 10/14 → 14/14;
  per-record argv witness 2/5 → 5/5 "with the renamed matcher passing" (`lessons/round-36.md:9-15`)
  — a benign-invariance leg ("renamed passes"), not a dishonest+honest pair predicate. Its r35
  pre-data controls (`c1-base 0/9`, `c1-hardcoded 3/9`, `c2-stub-pass 0/2`, `c2-stub-fail`)
  (`lessons/round-35.md:19-22`) are the stub/label control class, not honest-pass hardening.
- Other moved lanes: kama +4 (r31 chat-adapter; C1 honest non-admission — "a do-nothing registry
  of twelve duplicate rows also meets it" — a hollow-control finding, not a hardened arm); mori +2
  (r38 content anchors, "a named-row arm killed by its own mutation"); kake +1 (r43 spot-check
  only). None is shape B.

**Net: wave 1's "all three surfaces are kotoba-owned and landable" survives the re-scan** at
instrument level, on both current bytes and everything that moved since the pins. Two
nearest-evidence corrections (kumitate r40/r48; game-dev-2d vocabulary) do not transfer ownership.

## (2) Does kotoba's absorption criterion borrow a technique it does not cite? — yes

What the landed criterion implements, and where each technique class is held:

| technique in the r62 instruments | held by | sibling evidence (read this round) |
|---|---|---|
| guard-disabled flip arm + hollow/label kill controls + isolation arm | tameshi (method; kotoba `SKILL.md:14` itself says "tameshi owns the fixture and mutation method") | `tameshi-shokunin/corpus/knowledge/guard-kill-closure.md:14-29` (pristine-green + removal-kill rule, meta-cheat, incidental kill); fleet kill-rate ledger rows (`corpus/README.md` round-35 index repair confirms the set) |
| controls-before-data, control-forced named pre-data amendment, re-scored controls | kumitate | `counter-amendment-discipline.md` C1/C4–C7 (D49 `probe/doctrine49-probe.mjs`); r48 A48 receipts |
| "absorbed" vocabulary distinction | chousa (r16 disposition) **and game-dev-2d** (r65–r68 allowlist absorption) | `chousa-shokunin/corpus/knowledge/verification-r16.md`; `game-dev-2d-shokunin/corpus/live/r66-scribe/observations.md:33-41` |
| self-derived count (C2 G-a) | kagi | `kagi-shokunin/corpus/self-counts.py` + `self-counts.tsv`, index rows `corpus/README.md:172-175,219-222` (wave-1 row b; re-confirmed, kagi unmoved) |
| two-sided hardening (nearest practice for C2's honest-pass leg) | kumitate r40/r48 | `lessons/round-40.md:26-29`; `lessons/round-48.md` Mistake 3 |

Where the credits are **absent** — command
`grep -rniE 'tameshi|kumitate|chousa|kengaku|mado|sibling' <files>` over the landed round-62
artifacts (output filtered to non-boilerplate; run at HEAD `e424f2a4`, corpus files landed at
`e6da78b`):

- `corpus/knowledge/erratum-absorption-round62.md` — frontmatter sources S112–S115, S117, S118
  only; body carries no method credit and no chousa/game-dev-2d vocabulary sentence.
- `corpus/lessons/round-62.md` — Gate/Mistakes/Status changes/Falsify corrections (F1–F12):
  zero sibling mentions.
- `SKILL.md` registry rows 488–490 (the three new gates) — plain gate rows, no method credit
  (line 14's province sentence is the standing boundary, not a round-62 citation).
- `corpus/QUALITY.md` Q57 — grounded-in cites only M93 and the lane's own controls
  (`absorption-hollow.txt:16-27`); the criterion codifies the tameshi-shaped two-leg rule
  ("rejected by the landed instrument and disabling that erratum's guard in-process admits that
  same instance") with no technique provenance.
- `corpus/README.md` round-62 rows (109–110), `LOG.md` § Round 62 (2545–2565),
  `SCORECARD.md` round-62 annotations (36, 369) — zero sibling mentions.
- `plans/round-62.md` § Routed r61 items — internal items only.

Wave 1 already adjudicated this debt and assigned the landing places:
`ConnSibling.md:91-108` — tameshi method credit "in the C1 lesson and registry rows"; the kumitate
M90↔discipline correspondence "in the routed items"; the kagi class scoping; the chousa vocabulary
sentence "in the entry/lesson". None of those four landed. The lane has an established mechanism
for citing borrowed sibling practice — S117 is a kama row ("practice-level borrowing from sibling
source S117", r61) — so the omission is a deviation from the lane's own precedent, and it sits one
level above the round's own mined mistake M93 ("erratum recorded as absorbed without an arm-level
receipt"): the criterion's *method provenance* is recorded without a receipt, in the same round
that created Q57 to forbid exactly that shape of unreceipted claim.

## Contradictions, stated

- *Is kumitate r40's `benign_clean` an honest-pass arm?* Ruling: no (no-harm vs positive pass),
  which is what keeps shape B kotoba's; but the wave-1 sentence "no sibling index shows a hardened
  counter with an honest-pass arm" is only as strong as that ruling, and its nearest-evidence
  column should have named r40/r48 rather than only the honest-stop family.
- *Is game-dev-2d's absorption a "hold"?* It is measured, through the lane's real verifier
  machinery, with foreign/count-2 controls — but it lives in live scratch the lane's index marks
  disposable. Reported as vocabulary-level, body-level, index-invisible; calling it an instrument
  would overstate, ignoring it (wave 1's state) leaves the term register incomplete.

## Affected axes and proposed move (one, bounded)

- **Adjacency** (judged axis): wave-1 ownership verdict upheld; nearest-evidence rows corrected
  (kumitate r40/r48 for shape B; game-dev-2d vocabulary for shape A's word).
- **Calibration/consistency**: the four owed technique credits are missing from every landed
  round-62 artifact — a citable defect while the round's report (commit-order step 8) is still
  pending.

**Move:** land the four credits in the round-62 report's routed-items section, and — only where
append-only-safe — one sentence each in `corpus/lessons/round-62.md` § Falsify corrections or a
Q57 `grounded-in` addendum: (i) tameshi holds the guard-disable/kill-control method class the C1
matrix applies in-lane (fleet D-series; `SKILL.md:14` already concedes ownership); (ii) M90 is an
instance of kumitate's `counter-amendment-discipline` freeze-before-data clause class, and kumitate
r40/r48 are the nearest two-sided-hardening practice behind C2's honest-pass arm; (iii) C2 G-a's
self-derived count is the kagi `self-counts` technique class, so C2's novelty stays scoped to the
routed-repairs surface; (iv) "absorbed" in Q57/entry prose is distinct from chousa r16's
record-correction "absorb" and from game-dev-2d's allowlist line-absorption. No sibling tree
writes; no frozen bytes touched (`check_scoped_rules.py` `5a5adc94…`,
`check_routed_repairs.py` `95ade9be…` stay byte-identical); nothing is ceded — all three surfaces
remain kotoba's.

**Risks:** the report is the L1's vehicle; if its routed-items section is already drafted, this
file is the wave-2 evidence that must reach it. Overstating kumitate r40 as "same shape" would
concede novelty it does not claim; understating repeats wave 1's sweep-keyword blind spot
(`honest` missing `benign`). A vocabulary register naming only chousa repeats the same blind spot
against game-dev-2d.

**Verification (re-run):** the three sweep commands in § Scan basis; the movement census
(`rev-list --count` + README numstat vs the `ConnSibling.md:32-38` pins); the absence grep over
the nine landed r62 artifacts; and, after the report lands, the same absence grep returning the
four credits. Every number above carries the command that produced it; nothing here was run
against sibling working trees with write access, and no check was claimed that was not executed.
