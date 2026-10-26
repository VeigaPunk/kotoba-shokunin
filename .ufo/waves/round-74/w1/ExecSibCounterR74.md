# ExecSibCounterR74 — C2 frozen counter built and first-falsified (round 74, wave 1)

**Verdict: built and green.** `check_sibling_reread.py` implements the round-74 plan § C2 predicate
(`sibling rows re-pinned and re-read N of 20`, exit 0 iff N == 20) on committed bytes, with the
round-49 row checks run by the **base** copy of `check_sibling_census.py` (sha256-pinned, bytes
fetched at `BASE_REV`), the frozen heads sha256-pinned, and one red arm per conjunct. Self-test:
**`self-test: 0 failure(s) over 34 assertions`, exit 0** (3.4 s). Do-nothing control at the base
revision: **`sibling rows re-pinned and re-read 0 of 20`, exit 1**, in the live tree and in a
fleet-shaped sandbox checked out at base. The one calibration fact the L1 must carry into the claim:
a **purely mechanical carry-forward scores 19 of 20**, and the only lane separating it from a real
re-read is `tabi` — via conjunct (e). Details in § Calibration.

Deliverables (drafts; the L1 lands the counter):

| path | bytes | sha256 |
|---|---|---|
| `.ufo/waves/round-74/w1/build/ExecSibCounterR74/check_sibling_reread.py` | 68,232 (1,558 lines) | `0042cb42d7ef92b51e0f376a144dfbed9dd47355b656be0ac52b466bd5042074` |
| `.ufo/waves/round-74/w1/build/ExecSibCounterR74/carry_forward_measure.py` | 9,338 | `8d67d6d7c1624af6145313dedd2af2778d24d6ac0b2e572a74ff9cf86b83027f` |
| `.ufo/waves/round-74/w1/build/ExecSibCounterR74/README.md` | 6,976 | replay commands, pins, entry row shape, `--repo` warning, tabi decision point, integration |

No lane file was modified; no commit, no jj call, no sibling write. Scratch (`/tmp/k74w1-…`,
`/tmp/k74fleet-…`, `/tmp/k74carry-…`) created and deleted. No tool installed or upgraded.

## Pins (constants in the counter; no CLI flag sets them)

| pin | value | how verified this session |
|---|---|---|
| `BASE_REV` | `1e03d1991bc02281b00a5b7a5e00c9d5d5d72908` | `git rev-parse HEAD` at round start |
| `BASE_CHECKER_SHA256` | `2f9d8a88b1d3dd8562455006d5ea89ec02546a1ecb9d023f327d88e5502eedc7` | below, F1 |
| `FREEZE_SHA256` | `6e6012fc800d0f8da9666a2c1ad42934c6de4c0225d97391ae72c97ecdee195d` | below, F2 |
| `FREEZE_LANES` | `20` | `grep -vc '^#'` of the freeze file |

**F1 — the base checker bytes are the pin's.** `git show 1e03d199…:verifiers/check_sibling_census.py | sha256sum`
and `sha256sum verifiers/check_sibling_census.py` both print `2f9d8a88b1d3dd8562455006d5ea89ec02546a1ecb9d023f327d88e5502eedc7`
(1,518 lines). The file is unchanged between base and tip today, so the pin costs nothing yet and
refuses a measured revision that swaps the checker (M6, base-sha arm). The counter imports those
bytes from a temp copy; the measured tree supplies no code (Q33).

**F2 — the freeze file.** `sha256sum .ufo/waves/round-74/receipts/sibling-heads-freeze.tsv` →
`6e6012fc…dee195d`, 22 lines, 20 lane rows, 5 tab-separated cells each; `git log --oneline -1 -- <that path>`
→ `329e7d9 round-74: plan, base receipts, index r73 closure file, id scratch, sibling freeze heads`.
The freeze is **not** in the base tree (`git ls-tree -r --name-only 1e03d19 | grep -c '^\.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv$'` → `0`),
so the counter reads the pinned file from the worktree, and when the worktree has it not (a sandbox
checked out at base) from the newest commit that carries it (`git rev-list --all --max-count=1 -- <path>`).
Both routes are sha-pinned; a tampered copy is exit 2 either way (M6).

**Freeze cells re-derived, not trusted.** For all 20 lanes
`git -C <lane>-shokunin rev-parse --verify --quiet <head>:SKILL.md` (and `:PROVINCE.md`) equals the
freeze's blob cell, with `-` for the two lanes that have no `SKILL.md` at their head (audio,
game-dev-2d). The counter re-runs this per lane and fails the lane when a blob column does not
describe the head it names.

## How the five conjuncts are implemented

| conjunct | code | note |
|---|---|---|
| (a) row passes the **base** checker | `parse_entry` (base's `parse_blocks`/`split_row`) → `build_base_census` writes the nine-cell projection → `base.check_census(projection, fleet, None)` | one base run; each base failure labelled `row <i> (census line <n>)` is mapped back to the lane by the projection index. The tenth `delta` cell is stripped; the base file's bytes are never edited (its translate: `\|` re-escaped on re-emit so the base's `split_row` unescapes identically). The base's census-wide lane-set and duplicate-row refusals are its own and must come back clean. |
| (b) commit cell == frozen head, exact | string compare of the lower-cased 40-hex cell; then `git -C <lane> merge-base --is-ancestor <head> refs/heads/<branch>` (branch from the freeze row, ref verified first) | no prefix accepted (arm in the self-test, Q32) |
| (c) `delta` cell == recomputation | `git -C <lane> diff --shortstat <r49 pin> <head> -- SKILL.md PROVINCE.md` → `+<ins>/-<del>`, `none` when empty | the r49 pin is read from `PROVINCE.md` at `BASE_REV` (header-mapped `## Adjacent` parse), never from the measured revision |
| (d) PROVINCE `## Adjacent` row agrees | `province_rows` at `--rev`, indexed by **header name** (`lane`, `classification`, `commit`) so an added column cannot shift cells | exactly one row per lane; commit and classification must equal the entry's |
| (e) no false `none` | base's `token_in("kotoba", …)` over `SKILL.md` and `PROVINCE.md` at the frozen head | wider than the base's own `none` rule, which reads only the frontmatter description and PROVINCE.md |

Stdout: `repo/rev/base`, `freeze …`, `fleet …`, `base census: rows R verified V`,
`FAIL census-wide …`, one `lane <L>: ok|FAIL <reasons>` line per lane, then the summary line as the
**last** line. Exit 2 (could-not-evaluate) only for: bad arguments, not the lane repository, the
fleet root equal to the lane (M127), the base checker absent or sha-mismatched, the freeze absent /
sha-mismatched / not 20 lanes.

## Measurements (command → observed output)

**M1 — do-nothing control, live tree.**
```
cd …/kotoba-shokunin/.ufo/waves/round-74/w1/build/ExecSibCounterR74
python3 -B check_sibling_reread.py --rev 1e03d1991bc02281b00a5b7a5e00c9d5d5d72908
```
→ `freeze … (pinned, 20 lanes, sha256 6e6012fc…)`, `base census: rows 0 verified 0`, `note entry
absent at the measured revision`, `FAIL census-wide census table not found in
corpus/knowledge/sibling-overlap-census-round74.md at 1e03d1991bc0 (no ten-cell row)`, 20 × `lane
<L>: FAIL entry has no row for <L>`, `sibling rows re-pinned and re-read 0 of 20`, **exit 1**.

**M2 — the same verdict in a fleet-shaped sandbox at base** (the L1's battery form: symlink every
fleet entry except the lane, `git clone --shared -q --no-checkout`, checkout base, counter copied to
`verifiers/`):
```
python3 -B verifiers/check_sibling_reread.py --rev 1e03d199…   # cwd = $P/kotoba-shokunin
```
→ `freeze …/.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv (pinned, object store at
329e7d91d7d7), 20 lanes, sha256 6e6012fc…`, `sibling rows re-pinned and re-read 0 of 20`, **exit 1**
(2.8 s). Without the object-store fallback this would have been exit 2 for a missing freeze file —
the plan's control says exit 1, so the fallback is required, not polish.

**M3 — the plan-commit tip.** `python3 -B verifiers/check_sibling_reread.py --rev HEAD --fleet "$P"`
(sandbox at `329e7d9`, **symlinked** fleet root) → `freeze … (pinned, worktree) …`, `fleet "$P"`,
`sibling rows re-pinned and re-read 0 of 20`, **exit 1**. Same in the live tree at `329e7d9`.

**M4 — self-test.**
```
python3 -B check_sibling_reread.py --self-test
self-test: 0 failure(s) over 34 assertions
EXIT=0                                   # real 3.4 s
```
34 assertions (Q48): a satisfying fixture fleet of 20 tiny sibling repos plus a lane repo drives
`main()` to exit 0 and the exact line `sibling rows re-pinned and re-read 20 of 20`; then one broken
world per conjunct, each exit 1 with `19 of 20` — (a) a quote absent at the pin, (b) the r49 pin as
the commit cell, (b/Q32) a 12-hex prefix, (c) a wrong `delta`, (d) a stale PROVINCE commit, (e) a
`none` row whose SKILL.md **body** (outside the description) names kotoba — plus a missing row, a
duplicated row, freeze-sha mismatch (exit 2), freeze of 19 lanes (exit 2), base-checker sha mismatch
(exit 2), no `--rev` (exit 2), `--self-test` with `--rev` (exit 2), the Q66 relative `--repo .` arm
(exit 0, exact line), and an assertion that no CLI flag can set a pin.

**M5 — the real base checker, not only the stand-in.** The self-test's fixture carries a stand-in
checker (the 1,518 base bytes are not shippable inside the counter). I therefore measured the same
fixture with the **real** base bytes: `git show 1e03d19…:verifiers/check_sibling_census.py` → 68,473
bytes, sha256 `2f9d8a88…` = the pin, injected as the fixture lane's base commit and used through
`Pins(base_rev=<fixture base>)`:
- green: `base census: rows 20 verified 20 (delta cell stripped, base-row checks)`,
  `sibling rows re-pinned and re-read 20 of 20`, **exit 0**;
- `delta` world: `lane lane01: FAIL delta cell '+9/-9' but the recomputation gives '+2/-0' …`,
  `19 of 20`, **exit 1**;
- quote world: `lane lane04: FAIL base row check: row 4 (census line 8) (lane lane04): quote not
  found at PROVINCE.md:5 (+/-2 lines)`, `19 of 20`, **exit 1** — the base's own message, attributed
  to the right lane by the projection index.

**M6 — attacks I ran that are not in the self-test** (ad-hoc worlds on the fixture, same driver):
empty `delta` cell → `19 of 20`, reason `delta cell '' but the recomputation gives 'none'`; a
11-cell row → `19 of 20`, `row at entry line 12 has 11 cells, expected 10`; `## Adjacent` removed →
`0 of 20`; header's last cell renamed `change` → `0 of 20` (no ten-cell table; the rows are then
unsurveyed, exit 1 — a malformed entry never becomes a pass); a quote pointing at `PROVINCE.md:1` →
`19 of 20`, base refuses `at PROVINCE.md:1 (+/-2 lines)`; `--fleet` = the lane → `exit 2`,
`the fleet root is the lane itself … pass the directory that holds the lane` (M127).

**M7 — the base instrument still passes on real data** (my dependency, re-run, not inherited):
`python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md`
→ `rows 20 verified 20` / `province rows 20 matched 20`, exit 0.

**M8 — the `delta` recomputation against the L1's receipt.** `--emit-cells` prints, for the 20 frozen
heads: 15 non-`none` deltas and 5 `none` (audio, game-dev-2d, game-dev-3d, kagi, lore), all 20
identical to `receipts/sibling-staleness-base.tsv` (chousa `+187/-20`, kaidoku `+447/-2`, kake
`+955/-5`, kama `+417/-8`, kasegi `+72/-1`, kengaku `+30/-0`, kotodama `+85/-0`, kumitate `+106/-12`,
mado `+118/-0`, mori `+462/-15`, revenger `+618/-0`, souji `+2/-2`, tabi `+89/-0`, tameshi
`+108/-43`, tsukuroi `+872/-0`). The mechanical columns (skill file, names-kotoba, arbitration) equal
the round-49 census cells for **19 of 20** lanes; the exception is `revenger`, whose r49 row says
`no SKILL.md` and whose frozen head has one. Revenger's stale row fails on **three** cells, not one —
`base.mechanical_findings(repo, 6da884c6708f…, {path: NONE, names: no SKILL.md, arbitration: no
SKILL.md}, …)` returns exactly: `SKILL.md exists at the pin but the skill cell says NONE`;
`names-kotoba cell 'no SKILL.md' but the pinned description gives 'no'`; `arbitration cell 'no
SKILL.md' but the pinned description gives 'no'` — so an entry author who sets only the skill cell to
`SKILL.md` still fails the row.

**M9 — conjunct (e) is load-bearing on real bytes.** At the frozen heads the whole word `kotoba`
appears in `SKILL.md` for kagi, kengaku, kotodama, tabi; in `PROVINCE.md` for kengaku, kotodama,
kumitate. For **tabi** it is in the body only, so the base's `none` rule (description + PROVINCE.md)
does not see it: `git -C …/tabi-shokunin show 856fa9e12021…:SKILL.md | grep -n kotoba` →
`` 1313:  `LANES="protocol aggregator kasegi kengaku kake kumitate kotoba kagi kama"` `` and the same
string at `1450` (that output is the whole line, nothing dropped). `--emit-cells` gives tabi
`names kotoba = no`, so a carry-forward `none` row for tabi passes every base row check and is
refused only by (e).

**M10 — gate universe.** At base `verifiers/` holds **58** `.py`/`.sh` blobs (no recursion) and
`SKILL.md`'s `## Gate registry` holds **58** rows; two new verifier files plus two rows give the
plan's `60 of 60`. My counter adds one file and one row.

## Calibration — the carry-forward world the plan says to measure

`carry_forward_measure.py` (replayable, real fleet, throwaway `--shared` clone; the lane is read
only) builds three worlds and reports what the counter scores. Observed, exit 0 of the driver:

```
W_d  (entry recomputed, PROVINCE unchanged): exit 1 | sibling rows re-pinned and re-read 4 of 20
     ok lanes: audio, game-dev-2d, game-dev-3d, lore
W_v1 (round-49 cells, delta none, PROVINCE bumped): exit 1 | … 5 of 20
     ok lanes: audio, game-dev-2d, game-dev-3d, kagi, lore
W_cf (entry and PROVINCE recomputed): exit 1 | … 19 of 20
     ok lanes: audio, chousa, game-dev-2d, game-dev-3d, kagi, kaidoku, kake, kama, kasegi, kengaku,
               kotodama, kumitate, lore, mado, mori, revenger, souji, tameshi, tsukuroi
     FAIL: lane tabi: classified none, but SKILL.md at the frozen head 856fa9e12021 names kotoba whole-word
```

Three findings for the claim, each measured:

1. **The plan's expectation about the first shortcut world is false as written.** The plan says the
   bumped-commit copy dies because "quotes die at moved lines for the changed lanes". They do not:
   nearly every r49 quote sits on `PROVINCE.md:3` / `SKILL.md:3` / `SKILL.md:8` — the domain line at
   the top of the file — so the quote is still within ±2 lines after `+955/-5` (kake) or `+872/-0`
   (tsukuroi). A bumped commit cell alone is caught by (b); a bumped commit cell **plus recomputed
   delta and mechanical cells** scores **19 of 20**.
2. **The whole mechanical/mechanical-plus-delta re-pin is worth 4–5 of 20, not 0.** (c) blocks 15
   lanes over a claimed `none`; (a) blocks revenger over the stale `no SKILL.md`; (d) blocks the 16
   non-byte-equal lanes while PROVINCE is stale.
3. **The only lane separating a mechanical re-pin from a re-read is tabi, through (e).** The C2
   claim's value at 20 of 20 therefore rests on one mechanical judgement plus whatever the wave-2
   reviewers decide about the classification and the boundary sentences — exactly the bound the plan
   already states (Q26/Q51), now with a number. **Route to 20:** tabi must be classified
   non-`none` in the entry and in § Adjacent (the counter accepts any of the three classes; the
   plan's (e) only forbids `none` over bytes that name kotoba), or (e) is amended **before any
   data** to ignore fenced code. Both are the L1's decisions; the counter implements the plan as
   written and says which lane blocks.

## Cross-seat check (seat `ExecSibControlsR74`, same draft sha256 `0042cb42…`)

Their nine control worlds scored `0/18/17/17/17/17/4/17/17` (all below 20, each isolating a
conjunct) and their carry-forward world 18→19 — consistent with my numbers, and an independent
confirmation of the delta/cell arithmetic. Their 19 and mine are **two constructions of one row
content**, not two worlds: their diag-2b recomputes only revenger's three entry cells on top of the
world-2 overlay (PROVINCE already re-pinned), while my W_cf recomputes the mechanical cells and delta
for all 20 rows — and M8 shows recomputation changes exactly one lane (revenger), so the 19 row
contents coincide. That coincidence is a second measurement of the same fact (a mechanical re-pin is
worth 19 of 20), not a duplicated score; their 4 (world-2 entry against the base PROVINCE) is the
same conjunction with (d) left to decide, matching my W_d. The premise is now measured twice, from
different code: my M8 comparison and their `lanes.json` sweep over all 20 lanes both find 19 of 20
round-49 mechanical cell sets already equal to the head derivation, with revenger the only lane that
moves (`NONE | no SKILL.md | no SKILL.md` → `SKILL.md | no | no`). Their scores were run against the
draft path, since `verifiers/` does not hold the counter yet. Three of their statements, checked
against my own measurements:

- `resolve_repo()` uses the counter file's directory, not the cwd: **confirmed**, same behaviour;
  their "any sandbox replay must pass `--repo`" is a warning about draft copies, and it is now in the
  README (§ Replay). My M2/M3 sandbox runs copied the counter inside the sandbox, so the default was
  already the sandbox.
- tabi: **confirmed**, including that the base's `none` rule passes it and (e) refuses it (my M9),
  and that the mention sits in a shell snippet at lines 1313 and 1450. Their inference "the real
  entry cannot reach 20" holds only if tabi must be `none`; N == 20 is reachable by a non-`none`
  tabi classification, or by a pre-data amendment — see Calibration point 3.
- revenger: **confirmed** — its r49 cells say `no SKILL.md`, its frozen head has one
  (`git -C …/revenger-shokunin show 876630db:SKILL.md` exit 128, `6da884c6:SKILL.md` exit 0), so its
  r49 mechanical cells fail the base row check and recomputing them lifts the carry-forward world to
  19, matching my W_cf.

## Pre-data conflicts raised by other seats

**P1 — the `delta` cell spelling (seat `ScribeCensusEntryR74`; the finding is real, the fix is a
producer/consumer choice).** `merge_census.py`
(`.ufo/waves/round-74/w1/build/ExecSibMergeR74/merge_census.py`, `shortstat_delta()` at line 417)
emits the whitespace-collapsed shortstat — `2 files changed, 955 insertions(+), 5 deletions(-)` — and
says in its own comment that it "owns the cell and emits the plan's C2 (c) shortstat string"; my
counter renders `+955/-5`. Plan (c) (`plans/round-74.md:129-131`) fixes the **source** — "the row's
`delta` cell equals the counter's recomputation of `git diff --shortstat …`; an unchanged lane reads
`none`" — but **not the spelling**; my seat assignment is what fixed the spelling as `+<ins>/-<del>`
summed over both files, and that is what the draft implements. As the two drafts stand, (c) refuses
all 15 moved lanes, so one form must be chosen **before data**:

- **form A** (`+955/-5`, this draft): the merge tool's formatter changes (one return statement), and
  the rows seats' `mechanics.tsv` already uses that form;
- **form B** (collapsed shortstat): this counter changes `render_delta` (one function), the
  self-test's delta arm, and the README. The numbers are identical either way; only the spelling
  differs, and `none` stays `none`.

The counter deliberately accepts **one** spelling, not both: two accepted renderings would make the
frozen record inconsistent across lanes without adding a single check. Either way the failure message
prints the expected value, so a wrong cell is named per lane. The two renderers agree **by
construction**, not only by report: `merge_census.py:75-77` and this counter's `SHORTSTAT`
(`check_sibling_reread.py:138-140`) are the same three-part regex, the `plusminus` branch
(`merge_census.py:433-438`) is the same `"+%d/-%d" % (group(2) or 0, group(3) or 0)` expression with the
same `none` for empty output, and my own deltas already equal the L1's receipt on 20 of 20 (M8).
**L1 ruling needed on which spelling the landed entry carries; it is free now and costly after the
first scored world (Q28).**

**P2 — "(e) conflicts with (a) for tabi": not a conflict.** Plan (a) (`plans/round-74.md:124`)
quotes the **base checker's** `none` rule — "a `none` row names no `kotoba` in the sibling's
description or `PROVINCE.md`"; plan (e) (`plans/round-74.md:133`) is a separate, wider rule over the
whole file — "no `none` row exists for a lane whose pinned `SKILL.md` or `PROVINCE.md` contains the
whole word `kotoba`". Both are implemented as written: (a) delegates to the pinned base copy, (e)
recomputes over the whole file. tabi is the only lane where the two differ.

Extra measured fact for the L1's decision: the roster mention is **not drift**. `git -C
…/tabi-shokunin show <rev>:SKILL.md | grep -c kotoba` → `2` at the r49 pin `e3cf4e0d` and `2` at the
frozen head `856fa9e1`; `PROVINCE.md` → `0` at both. Re-pinning cannot remove it, so N == 20 requires
tabi classified non-`none` (with § Adjacent agreeing) or a pre-data amendment of (e) that ignores
fenced code/shell snippets — the same decision recorded in § Calibration point 3.

**P3 — the entry generator cannot currently emit a row set (verified; blocks the first 20-of-20
measurement).** `merge_census.py:501,514` reads each scout JSON's `proposed_classification` and
refuses any value outside `contested/adjacent/none`. Measured over the 20 committed scout JSONs in
`.ufo/waves/round-74/w1/build/*/`, 18 carry a bare enum and **2 carry prose**: `chousa
"adjacent -- decided by the second clause of the r49 rule (a …"` and `kagi "adjacent -- decided by
the second clause of the r49 rule on …"` (both files under `ScoutSibChousaKagiR74/`). The root cause
is a scout-schema split: `kumitate.json` puts the reason in `proposed_classification_clause` beside a
bare value, the two chousa/kagi files put it inside the value. The generator therefore exits 2 before
writing any entry, so no measurement of mine can reach N > 0 until it is fixed. Two edits, both
outside this seat: normalise the two JSON values (keeping the prose in the clause field), or let the
generator accept a leading enum token. This is a producer-side blocker, not a counter defect — the
counter never reads scout JSON.

## Integration for the L1

0. **Three items before the first scored world (Q28):** the `delta` cell spelling (§ P1 — form A keeps
   this counter and is already what `merge_census.py --delta-format plusminus` emits), tabi/(e)
   (§ P2 — classify tabi non-`none`, or amend (e) pre-data to ignore fenced code), and the generator
   refusal (§ P3 — normalise the two prose `proposed_classification` values or accept a leading enum
   token). All three are free now and block any N > 0 if left open.
1. `cp .ufo/waves/round-74/w1/build/ExecSibCounterR74/check_sibling_reread.py verifiers/`
   (landed copy must be byte-identical: sha256 `0042cb42…42074`).
2. One `## Gate registry` row (kind `gate`, verdict map `0=clean, 1=failed, 2=could-not-evaluate`,
   self-test `--self-test`, pinned values `verifiers/check_sibling_census.py` and
   `.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv` — both exist at the measured revision —
   write scope read-only, owner `kotoba`); full row text in the README.
3. Optional `check_assertion_floors.py` `INSTRUMENTS` row with floor **34** (the self-test prints the
   lane-convention summary line), so silent arm deletion becomes a floors FAIL.
4. Commit order the counter enforces: the **PROVINCE § Adjacent re-pin and the entry must land
   together** (W_d shows a 4-of-20 result otherwise), and the C2 commit must be measured at its own
   revision before C1 lands (`PROVINCE.md` § Core is not read by this counter).
5. Do not re-freeze without updating `FREEZE_SHA256`; that is a deliberate constant edit, and a
   stale pin fails closed as exit 2.

## Risks / limits (unobserved or unmeasurable here)

- **R1 (calibration, not a defect):** 19 of 20 is reachable by a mechanical re-pin (M10/W_cf). Any
  wave-2 seat comparing "20 of 20" with "the entry is a real re-read" must read § Calibration.
- **R2:** the counter does not judge whether `adjacent`/`contested`/`none` is right, nor whether a
  boundary sentence reads correctly, nor whether a quote is the *best* quote for the scope — only
  that it is located at the pinned commit, ≥6 words, off a heading, within ±2 lines.
- **R3:** the self-test's base checker is a stand-in that mirrors the base's row-check contract; the
  real bytes were exercised separately (M5) but not inside `--self-test`. A future change to the
  base checker's own rules changes the real verdict without touching the self-test.
- **R4:** `--emit-cells` is a convenience for the entry author; it recomputes the mechanical columns
  with the base's helpers, and the counter never accepts its output as a verdict. Whether a seat
  copies those cells without reading the sibling files is not something a counter can see.
- **R5:** the sibling lanes keep moving after the freeze; rows are valid at their frozen heads, and
  the counter says so in its docstring and in every `freeze …` line.
- No blocker. The only unreachable thing this session was a *real* 20-of-20 measurement, which
  requires the entry the L1 has not written yet; the fixture measure with the real base bytes (M5)
  covers the mechanism.
