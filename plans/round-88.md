# kotoba round 88 — plan and freeze

Host: Linux `7.2.11-arch1-1`, omp 18.15.0 (ELF `/home/vgpnk/.local/bin/omp`, sha256
`6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f`).
Lane repo `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, branch `master`.
**Tip at freeze:** `4df1e8005016c75390a5e06b209462df58c95918` (round-87 closure commit).
**Base for C1:** the same tip (the r87 counter is measured there, before-receipts committed with this file).
**Reference base for C2's red-set test:** `223ae62424f8ab1eb365d733eb648d6228ddd7e8` (the round-87 base; its
integrity red set is six names, receipt `.ufo/waves/round-88/receipts/before-C2-base-integrity-full.txt`).
**Freeze:** this file and `.ufo/waves/round-88/receipts/before-*.txt`, committed before any candidate data.

## Fresh-start reading (run-15 authorization, 2026-11-05 "Authorize all")

Read before declaring: `corpus/lessons/round-85-verifier-spotcheck.md` (C1 unprovable: vacuous worlds
satisfied the frozen predicate; C2 improved), `corpus/lessons/round-86-verifier-spotcheck.md`
(admitted; the kill-rule ruling and the planner-citation finding), `corpus/lessons/round-87-verifier-spotcheck.md`
(**rejected-honest-stop**: C1 depth 12/12 reached by four forged ledgers; C2 at the tip 4 of 5 because
D5(iii) fails on a healed external red; record defects R87-D1..D8). Each rejection is answered by a
concrete change below: C1 adds forgery rejection as its predicate; C2 replaces the exact-set red test with a
monotone-plus-identity test whose controls are committed before scoring.

## Measured before-state (committed receipts, this file's freeze)

| Measurement | Command | Observed | Receipt |
|---|---|---|---|
| C1 honest, r87 counter, tip | `python3 -B verifiers/check_omp_root_semantics.py --rev <tip>` | `12 of 12`, exit 0 | `receipts/before-C1-r87counter-honest.txt` |
| C1 forged worlds, r87 counter | `w3/CriticSemanticsR87/forgery-worlds.txt` (r87 attack seat) | `12 of 12` exit 0 on all four worlds `w_cross_row7`, `w_subdir_row9`, `w_misattr_row12`, `w_renderline_row6` | `.ufo/waves/round-87/w3/CriticSemanticsR87/forgery-worlds.txt` |
| C2 r87 counter, tip | `python3 -B verifiers/check_r86_routed_repairs.py --rev <tip>` | `r86 routed defects closed 4 of 5`, exit 1 (D5 FAIL) | `receipts/before-C2-tip.txt` |
| Integrity red set, base `223ae62` | `verify_corpus_integrity.py` in a scratch clone at base | `3/9`; reds `index.tracked_files`, `index.unindexed`, `pointers.report_total`, `pointers.report_dead`, `pointers.commit_total`, `pointers.commit_unresolvable` | `receipts/before-C2-base-integrity-full.txt` |
| Integrity red set, tip | same command in the lane | `4/9`; reds `index.tracked_files`, `index.unindexed`, `pointers.report_total`, `pointers.commit_total`, `pointers.commit_unresolvable` | `receipts/before-C2-tip-integrity.txt` |

Tip red set ⊂ base red set (5 ⊂ 6). `pointers.report_dead` healed (its target, `.ufo/reports/round-84/kama.md`,
landed on the fleet repo). The check count is 9 at both revisions.

---

## C1 — depth (score 9, owned lowest): forged root grounding is rejected

**Surface changed.** The lane's counter for *which code grounds each omp skill root*. The r87 counter
(`verifiers/check_omp_root_semantics.py`, sha256 `6e826f3b…8922`) is **not edited**; it stays the
do-nothing control and the frozen record. The new counter is `verifiers/check_omp_root_semantics_v2.py`.
Its ledger is the r87 ledger `verifiers/omp-skill-roots-semantics.tsv` read unchanged at `<rev>`.

**Frozen predicate** (the same sentence here, in the v2 counter's docstring, and in every receipt):

    python3 -B verifiers/check_omp_root_semantics_v2.py --rev <rev>
        -> prints "omp root semantics grounded N of 12" and "forgeries rejected M of 4",
           exit 0 iff N == 12 AND M == 4 AND guards S1-S5 PASS; exit 1 otherwise; exit 2 = could-not-evaluate.

- **N** counts rows grounded under the v2 conjuncts (below) on the honest ledger at `<rev>`.
- **M** counts the four forged worlds of the r87 critic (`w_cross_row7`, `w_subdir_row9`,
  `w_misattr_row12`, `w_renderline_row6`) that the v2 counter **rejects** (exit nonzero or N < 12 on that world).
  The four worlds are re-created as scratch commits from the r87 receipts; their ledger diffs are the
  committed `forgery-ledger-diffs.txt` of round 87.

**Row grounded** (all conjuncts, v2):

1. **pattern** — as r87 (equal to the round-86 ledger's pattern at `<rev>`; no `..`; no wildcard in the first segment).
2. **reader** — `reader_quote` (>= 12 chars) occurs verbatim in the ELF on a line carrying a join token; **and**
   the line also carries the row's **binding token set**: a per-row token set frozen in the v2 counter's source
   **in the first commit that adds the file**, before any honest or forged world is scored. For each row the set
   names at least one token that the row's root literal or its declared reader variable produces; an empty set
   is refused. Sets are written into the counter's header comment with their sha256 before the first forged or
   honest score; a set revised after that score kills C1 (kill rule below), it is never amended.
3. **module** — as r87 (the `// packages/<module>` header precedes the reader quote's first occurrence).
4. **bound (live)** — the v2 counter **computes** the expansion set for a `{cwd}/` row from a frozen
   probe cwd `/home/u/proj/sub` with `HOME=/home/u` (session cwd and ancestors **strictly below** `$HOME`:
   `/home/u/proj/sub`, `/home/u/proj`), joins the row pattern to each element, normalizes, and refuses any
   candidate that (a) escapes the expansion set or (b) contains a `..` segment. A row whose pattern is `~/`
   must produce only `$HOME`-rooted candidates. The computed set is compared with the set the row's module
   code visibly walks (the module quote's walk-up loop, or its single join for a non-walking row); a mismatch
   fails the row. This replaces the r87 conjunct 4, which the r87 closure found inert at scoring.
5. **binary** — the row's `binary_quote` occurs verbatim in the ELF (the r87 counter never matched it).

Guards: **S1** the ledger is read from `<rev>`'s committed bytes (`git show`); **S2** the ELF sha256 equals the
pinned value (else exit 2); **S3** the ledger's `root_pattern` column equals the round-86 ledger's at `<rev>`;
**S4** the counter's `--self-test` prints `0 failure(s) over N assertions` with N >= the frozen floor recorded in
`verifiers/floors-registry.json` (added row); **S5** the counter opens the ELF read-only (mmap) and never execs it.

**Target:** `N == 12` and `M == 4`, exit 0 at the landing revision.

**Before (measured, do-nothing control):** r87 counter on the honest tip `12 of 12` (exit 0) and on the four
forged worlds `12 of 12` each (`forgeries rejected 0 of 4` under the v2 reading). The r87 counter therefore
meets N but **fails M**: it is the do-nothing control and must read `M == 0`.

**Positive control (blanket refusal is not a gain):** the v2 counter must read `N == 12` on the honest ledger, so a
counter that refuses everything cannot satisfy the predicate.

**Kill rule (C1):** the v2 counter, its binding token sets, its floors row or its ledger changed **after the first
candidate or forged score** kills C1. A pre-score amendment is an addendum that ships its own re-run controls and
may not widen the target or change the predicate sentence.

**Sourced (§2b).** C1's knowledge entry cites a `corpus/SOURCES.md` row **opened this round**: the upstream
omp v18.15.0 walk-up module `packages/coding-agent/src/discovery/agents.ts`, re-opened from
`raw.githubusercontent.com` with access date, sha256 and a located ≤25-word quote (the bound conjunct's
upstream ground). It becomes row S257 (the next unused id; S256 is the last row).

---

## C2 — consistency (calibration sub-axis, score 10): the routed D5 gate reads honest state

**Surface changed.** The lane's own routed-repair gate `check_r86_routed_repairs.py` (r87). Its D5 demanded that
the integrity gate's red set equal exactly two names, which healed external red falsifies (closure R87-D8, r87
`D5(iii)`). The r87 counter is **not edited**; the new counter is `verifiers/check_r86_routed_repairs_v2.py`.

**Frozen predicate:**

    python3 -B verifiers/check_r86_routed_repairs_v2.py --rev <rev>
        -> prints "r86 routed defects closed N of 5", exit 0 iff N == 5; exit 1 otherwise; exit 2 = could-not-evaluate.

Items D1–D4 are the r87 items, unchanged in meaning (receipts for the r86 tip instruments; the planner citation;
the reject row in `corpus/lessons/round-87.md` `## Gate`; the boundary wording in `plans/round-87.md`).
**D5 (v2)** holds iff **both**:

- **(i) identity:** `python3 -B verifiers/verify_corpus_integrity.py --json` at `<rev>` and at the reference base
  `223ae62` lists the **same set of check names** (nine names at both revisions). A silenced or removed check fails (i).
- **(ii) monotone:** the set of names whose verdict is `DRIFT` at `<rev>` is a **subset** of the set at `223ae62`.
  A new red fails (ii); a healed red passes (ii).

**Target:** 5 of 5, exit 0 at the landing revision.

**Do-nothing control:** the r87 counter at the tip reads `4 of 5`, exit 1 (D5 FAIL). **Discrimination controls
(committed before scoring, each a scratch clone):**

- `w_added_red` — the tip plus a pointer to an unresolvable commit in a new lesson line → v2 D5 FAIL (ii).
- `w_silenced` — the tip with one integrity check removed from the script → v2 D5 FAIL (i) (**a monotone-only
  variant passes this world**; that is why (i) exists; the monotone-only variant is reported as the control's arm).
- `w_healed` — the base `223ae62` with `report_dead` absent (a fixture that resolves its one red) → v2 D5 PASS.
- `w_tip` — the landing tip → v2 D5 PASS (the honest state).

**Kill rule (C2):** the v2 counter, its fixtures or the integrity script changed after the first candidate score kills
C2. The integrity script is **not** edited by this round; a red that the lane's own records introduced is measured,
disclosed and routed, not repaired by re-recording expected counts (that is how r86 M-class defects started).

**Honest bound, stated before data:** C2 measures the gate, not the corpus. The tip keeps five integrity reds, all
inherited from base; C2 does not claim them repaired. Expected counts (`corpus-baseline.json`) are not re-recorded.

---

## Record correction (mined mistake, not a claim)

R87-D7 (closure § 6): `LOG.md` round-87 says C2 "verified, `5 of 5`" (line 3315) while the tip reads `4 of 5`.
Captured-by: none (no check compares a record's verdict with the tip reading). Fix: an appended correction entry
naming line 3315's text and the tip reading, plus a sweep that is red before (the stale line unannotated) and
green after (annotated). The sweep is committed as `receipts/mistake-sweep-before.txt` and `…-after.txt`.

## Frontier step (§2b, CORPUS.md contract v1)

- `corpus/SOURCES.md`: one new row S257 (opened this round; Gate records URL, access date, sha256, located quote);
  status changes old→new logged in the lesson (none expected).
- Census before and after: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`
  (before: exit 0, 33 W04; recorded at round start).
- One mistake mined (R87-D7, above). The fix is shown able to fail (red before, green after).
- Sourced claim: C1 rests on S257.
- `considerthese/2026-10-26.md` proposal 4 ("don't close a round before its falsify wave runs") mined: a QUALITY
  criterion (Q80) that a round with no attack seat closes provisional. Proposal 1 was mined in round 87.
  Proposal 3 (description audit against S213) is carried, not landed this round.
- Assimilation: `none` — `/home/vgpnk/Projects/shokuknow/merge/kotoba/` exists (MERGE-REPORT.md, 188 rows) but its
  id space collides with S256 and no staged theme matches the C1/C2 ground this round; no adoption starts here.

## Round shape (hyaku run 15, band 8–16)

ONE v1 wave, 14 seats, under `scripts/hyaku/ufo-wave-policy.json` (`waveMinLanes` 8, `waveMaxLanes` 16):
scout 2, executor 3, scribe 3, connector 1, reviewer 2, critic 1, mutation-tester 1, sentinel 1 (the validated
counts are in `.ufo/waves/round-88/r88-w1-plan.txt`). Attack set (reviewer, critic, mutation-tester)
= 4 of 14 = 28.6 % >= 25 %; connector seats 1 (<= 2). The §3 planner seat is held by the L1 (the validator's
`SWARM_ROLES` excludes `planner`; `~/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs` carries the frozen-topology
sentence). The planning data-walk rides the scouts and the connector.

## Touch list

`plans/round-88.md` (this file), `verifiers/check_omp_root_semantics_v2.py` (new),
`verifiers/check_r86_routed_repairs_v2.py` (new), `verifiers/floors-registry.json` (one row; if it exists — check),
`corpus/knowledge/omp-root-semantics-round88.md` (new), `corpus/SOURCES.md` (one row S257), `corpus/README.md`
(index row + § Frontier note), `corpus/QUALITY.md` (Q80), `corpus/lessons/round-88.md` (new),
`LOG.md` (append), `SCORECARD.md` (append), `SKILL.md` (registry rows within the 600-line budget, only if a new
gate must be registered), `.ufo/waves/round-88/**`.

## Admission

Both claims verify on their frozen v2 counters at the landed revision, with their controls reading as stated.
No axis is harmed (the no-harm battery: base and post-state runs of the integrity gate, the gate registry and the
sibling census, committed as receipts). Non-author closure rules. Number alone is not C1's evidence: the forged
worlds and the blanket-refusal positive control are part of the predicate, not commentary.

---

## Errata (appended after wave-1 data; no predicate, target or control changed)

**E1 — the base red citation.** The plan's measured-state paragraph names the healed red as
`.ufo/reports/round-84/kama.md` (copied from the round-87 closure). The committed base receipt
`receipts/before-C2-base-integrity-full.txt` names the base red as `report_dead` at
`corpus/lessons/round-81.md:29`, pointing at `.ufo/reports/round-76/kotoba.md`. In the lane tree that
path is a tracked symlink to the fleet root, where the file exists, so the lane reads it as healed; in a
fresh clone it dangles and reads red (ExecMonotoneD5 `F2`). The tip-reading `4 of 5` for the r87 gate and
the set arithmetic in this plan are unchanged; the location-dependence is the r87 closure's R87-D8 again.

**E2 — the frozen control `w_added_red` fails under the frozen predicate (F1, measured after data).** Clause
D5(ii) is a set of check NAMES. `corpus.pointers.commit_unresolvable` is already DRIFT at the base, so a second
unresolvable citation changes its instance count and adds a detail line, but the name set is unchanged; (ii)
reads PASS. The frozen control expected FAIL via (ii). Measured at `scratch` by ExecMonotoneD5
(`.ufo/waves/round-88/w1/ExecMonotoneD5/receipts.txt` §2–§4): self-test `1 failure(s) over 16 assertions`,
the failing arm is `w_added_red`. The plan's control expectation was wrong: the predicate cannot satisfy it.
**Disposition (L1, this round):** the predicate is NOT amended. The kill rule forbids a counter change after the
first candidate score, and the tip reading was scored in this round. C2 is therefore **not verified** this round:
the frozen discrimination control fails, and an instance-level successor is routed to round 89 (its predicate and
its controls to be frozen and EXECUTED before the freeze commit). The F1 failure is recorded as the round's
mined mistake: a frozen control was written but not executed before the freeze commit.

**E3 — what the round does not claim.** Nothing in this errata changes C1's frozen predicate. C1's verdict depends
on its own control matrix (`ExecForgeryWorlds/matrix.tsv`) and on the v2 counter's self-test, as frozen.
