# Round 74 C2 shortcut worlds (seat `ExecSibControlsR74`)

Nine committed shortcut worlds for the frozen C2 predicate of
`plans/round-74.md` § C2, plus one diagnostic bundle. Every world is an
overlay over a fresh `--shared` clone of the lane at
`1e03d1991bc02281b00a5b7a5e00c9d5d5d72908`: `corpus/knowledge/sibling-overlap-census-round74.md`,
`PROVINCE.md`, and the freeze receipt
`.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv` (copied unchanged; the base
tree does not carry it, and the counter falls back to the object store at
`329e7d91` when the worktree lacks it — measured: same 18 of 20 both ways — so
the copy only keeps the sandbox self-contained). Nothing here is merged into the lane — the L1 is the only integration
owner.

Row shape (the counter's, `check_sibling_reread.py` `parse_entry`): the
round-49 nine cells plus a tenth `delta` cell, rendered `+<insertions>/-<deletions>`
summed over `SKILL.md` and `PROVINCE.md`, `none` when the diff is empty.
World 1 is the plan's literal "copy with the commit cells bumped and nothing
else", so it keeps the nine-cell round-49 shape and carries no `delta` cell.

## Measured scores

Command (counter = `ExecSibCounterR74/check_sibling_reread.py`, the draft
intended for `verifiers/check_sibling_reread.py`; it resolves the lane from its
own path, so `score_worlds.sh` passes `--repo <sandbox> --rev HEAD`):

```
.ufo/waves/round-74/w1/build/ExecSibControlsR74/score_worlds.sh \
  .ufo/waves/round-74/w1/build/ExecSibCounterR74/check_sibling_reread.py \
  /home/vgpnk/Projects/shokunin --diag
```

| world | what it varies | measured | must be |
|---|---|---|---|
| world-1-bump-only | r49 entry, commit cells bumped, nothing else | 0 of 20 | < 20 |
| world-2-carry-forward | world 1 + script `delta` cells + script quote re-location | **18 of 20** | measured, not asserted |
| world-3-missing-row | `lore` row dropped from entry and PROVINCE | 17 of 20 | < 20 |
| world-4-duplicate-row | `lore` row duplicated in the entry | 17 of 20 | < 20 |
| world-5-not-freeze-head | `kumitate` left at its r49 pin | 17 of 20 | < 20 |
| world-6-quote-absent | `kagi` quote replaced by a kama sentence | 17 of 20 | < 20 |
| world-7-province-unchanged | world 2's entry, base PROVINCE § Adjacent | 4 of 20 | < 20 |
| world-8-none-names-kotoba | `kagi` classified `none` (its SKILL.md names kotoba) | 17 of 20 | < 20 |
| world-9-delta-wrong-numbers | `kake` delta `+954/-5` for `+955/-5` | 17 of 20 | < 20 |
| diag-2b-recomputed | world 2 + `revenger`'s three mechanical cells recomputed | 19 of 20 | diagnostic |

The kill rule ("any non-carry-forward world scoring 20 means the counter is
wrong") is not triggered: every control sits below 20, and each isolates its
own conjunct — the only constant failures across worlds 2-9 are `revenger`
(stale mechanical cells) and `tabi` (the `none` rule).

`./score_worlds.sh --emulate` reproduces the same nine numbers from
`emulate_reread.py`, which applies the plan's conjuncts with the base copy of
`check_sibling_census.py`. The agreement is why the emulated numbers were
trustworthy before the counter landed.

## What the worlds measured

1. **No quote dies.** All 20 round-49 quote cells are still located, at the
   *same* line numbers, at the freeze heads (`world-1-bump-only.base-census.log`:
   `rows 20 verified 19`, the one failure being `revenger`'s mechanical cells).
   The plan's prediction that "quotes die at moved lines for the changed lanes"
   did not hold at these heads. World 1 scores 0 for a different reason: its
   nine-cell table has no `delta` cell, so the counter refuses the table shape
   (`logs/world-1-bump-only.log`: "entry has no census table with 10 cells and
   a trailing `delta` cell").
2. **The carry-forward is 18 of 20, one mechanical cell set from 19.** Two rows
   cost it: `revenger` (the lane gained a `SKILL.md` at its freeze head; the
   round-49 row says `NONE`) and `tabi` (`none` row whose pinned `SKILL.md`
   contains `kotoba` at line 1313 inside a shell `LANES=` list). Recomputation
   of `revenger`'s cells lifts the same overlay to 19 (`diag-2b-recomputed`).
3. **Conjunct (e) as frozen is fired by a body-only mention.** `tabi`'s honest
   `none` row — the classification the round-49 census and its falsify wave
   both support — fails (e) for a `kotoba` token inside a shell snippet, not a
   scope statement. The base checker's own `none` rule (frontmatter
   description + `PROVINCE.md`) passes it. See the seat report § Finding 3.
4. **`PROVINCE.md` is load-bearing.** With the entry complete and PROVINCE left
   at the round-49 pins, only the four lanes whose pin already equals the head
   pass (`audio`, `game-dev-2d`, `game-dev-3d`, `lore`): 4 of 20.

## Files

| path | role |
|---|---|
| `build_worlds.py` | generates every `world-*/overlay/` and README from the r49 entry + freeze file |
| `analyze.py`, `lanes.json` | per-lane facts at the freeze heads: pin, quote re-location line, stale/current mechanical cells, delta, `kotoba` hits |
| `emulate_reread.py` | expected-score emulator (base checker's functions, plan conjuncts) |
| `collect_expected.py` | writes `expected.json` from the emulator |
| `record_measured.py` | writes `expected.json` from `logs/*.log` (measured run) |
| `score_worlds.sh` | runs one counter (or `--emulate`) over every world: `<world> <N of 20> <exit>` |
| `check_sibling_census_base.py` | `git show 1e03d199:verifiers/check_sibling_census.py`, sha256 `2f9d8a88…` (the base bytes the emulator and the counter both use) |
| `logs/` | one log per world from the measured run, plus `world-1-bump-only.base-census.log` |
| `logs-emulated/` | the `--emulate` run, kept apart so it never overwrites measured evidence |

## Bound

These worlds test one counter, not the census. They say nothing about whether
any classification is the right call, whether a boundary sentence reads
correctly, or whether the freeze heads are still the siblings' heads. A row is
valid at its frozen head, not at the round end.
