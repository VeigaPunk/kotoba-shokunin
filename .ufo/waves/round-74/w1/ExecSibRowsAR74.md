# ExecSibRowsAR74 — C2 mechanical row cells for five lanes (round 74, wave 1)

**Verdict: 5 of 5 assigned lanes derived mechanically at the frozen fleet heads, and the same
script re-derives the round-49 pins' cells identically to the committed r49 rows for all five
(`REDERIVE_ALL_MATCH=yes`).** No committed lane file was touched. The five rows, with the sibling
scouts' proposed quotes filled, pass the base checker's own row checks —
`rows 5 verified 5` — with the fleet lane-set as the only failure (15 lanes are other seats').
Two L1 actions follow from the derivation: `PROVINCE.md` § Adjacent commit cells for **chousa** and
**kagi** still read the r49 pins and must be bumped to the freeze heads, and **kagi must not be
classified `none`** (its pinned `SKILL.md:297` names kotoba).

Base checker used for every derivation (Q33: measured revision supplies bytes, not code):

```
$ git -C kotoba-shokunin show 1e03d1991bc02281b00a5b7a5e00c9d5d5d72908:verifiers/check_sibling_census.py > check_sibling_census.py
$ sha256sum check_sibling_census.py && wc -l check_sibling_census.py
2f9d8a88b1d3dd8562455006d5ea89ec02546a1ecb9d023f327d88e5502eedc7  check_sibling_census.py
1518 check_sibling_census.py
```

Derivation uses the checker's own `description_of`, `token_in`, `fleet_lanes`, `git_show`,
`mechanical_findings`, `split_path_line`, `locate_quote`, `normalize_lane`, `select_province_table`,
`select_census_table` — nothing is re-implemented.

## Deliverables

`.ufo/waves/round-74/w1/build/ExecSibRowsAR74/`:

| file | sha256 | what |
|---|---|---|
| `rows.tsv` | `25f5d98fa95d23fec560999351049abb45f22ae735a97d00550b91185d7a9e19` | merge-seat schema, 8 cols: `lane branch commit skill_file names_kotoba arbitration quote_at quote`; quote cells copied from the sibling scouts' JSON (provenance below), every other cell my derivation |
| `rows-full.tsv` | `9001edefe39d13380ea65cee7332dfb87f2b7997aa95b5ac7768a8edfcbb5dbd` | my derivation, 16 cols: `lane branch commit40 r49_pin skill_file names_kotoba arbitration delta delta_files kotoba_hits_skillmd kotoba_hits_province skill_scope_candidates province_scope_candidates path_line quote classification`; `path_line`/`quote`/`classification` left empty (scouts own them, merge joins) |
| `derive_rows.py` | `607ea313bc7980acf8f719b4e00a30713c4165ef54f27f201abd226cea72d3a4` | the derivation script; also emits `rows.tsv` |
| `validate_rows.py` | `fb15db27b102b7cd6e4059ae25d79c09d6e16cfb5d99d246f2c760983df07339` | runs the base checker over the five rows in a scratch census |

Reproduce (`check_sibling_census.py` = the base copy, any path):

```
python3 -B derive_rows.py check_sibling_census.py rows-full.tsv
python3 -B validate_rows.py check_sibling_census.py rows-full.tsv <w1/build>          # row checks
python3 -B validate_rows.py check_sibling_census.py rows-full.tsv <w1/build> --province
```

`rows.tsv` quote provenance (scouts' proposals, verbatim): `ScoutSibAudioGamedev2dR74/audio.json`,
`ScoutSibAudioGamedev2dR74/game-dev-2d.json`, `ScoutSibChousaKagiR74/chousa.json`,
`ScoutSibChousaKagiR74/kagi.json`, `ScoutSibGamedev3dLoreR74/game-dev-3d.json`. No `|` and no tab
in any cell of either file (`pipe-lines []` for both). My lane set is **5 of the freeze file's 20** —
the other 15 are ExecSibRowsB/C/D (their build dirs exist); the merge seat was told.

## The cells

| lane | branch | commit40 (freeze head) | r49 pin | skill_file | names kotoba | arbitration | delta | kotoba hits |
|---|---|---|---|---|---|---|---|---|
| audio | main | `7a2fcd4f08831154686e4e323031f41fffdb077f` | same | `NONE` | `no SKILL.md` | `no SKILL.md` | `none` | — |
| chousa | master | `00f8c7f5272a1d98b6d34913985fa4537e00aaf9` | `6c5eb1466f2b8abbd3de576389037f435016d07b` | `SKILL.md` | `no` | `yes: kasegi, kengaku` | `+187/-20` | — |
| game-dev-2d | main | `7753d49b16674e122ed134403e7a9b301f2cbf7e` | same | `NONE` | `no SKILL.md` | `no SKILL.md` | `none` | — |
| game-dev-3d | main | `89dd182b70943a20ae9aa6c1ed0e3c9b6e79c080` | same | `SKILL.md` | `no` | `yes: game-dev-2d, revenger` | `none` | — |
| kagi | master | `69b61db46be4ed955994f6f1d1cba522bc5f4e97` | `899c50b42634a3a4ad0b28ab7509786315e2fc2b` | `SKILL.md` | `no` | `no` | `none` | `SKILL.md:297` |

`delta_files` (per-file decomposition of the summed `delta`): chousa `SKILL.md:+187/-20;;PROVINCE.md:none`;
the other four `SKILL.md:none;;PROVINCE.md:none`.

Candidate scope-statement lines (in `rows-full.tsv`, `;;`-separated, `N:line`):
audio `PROVINCE.md:3-5`; chousa `SKILL.md:3` (description) + `PROVINCE.md:3,5-8`;
game-dev-2d `PROVINCE.md:3`; game-dev-3d `SKILL.md:3` + `PROVINCE.md:3-12`;
kagi `SKILL.md:3` + `PROVINCE.md:3,5-6`.

## Findings

**F1 — Freeze row confirmed against live refs and blobs (all five).**
`git -C <lane>-shokunin rev-parse refs/heads/{main|master}` equals the freeze `head40` for all five;
`git rev-parse <head>:SKILL.md <head>:PROVINCE.md` equals the freeze blob columns for all five:

```
audio        -        27f53c7b18c5e55fd549d73f7c407ee7083d5c9b
chousa       ec1f0c1f5865fcc823c688fe8be34c7d8cdf53ae  0f94a0c4f73cec2e36d587b199d7c43716ceae8c
game-dev-2d  -        d753cc009ed90658e3bfed65fc80a74931924d6c
game-dev-3d  bbed9b7b9a18ce318bd6f4c3de5e9e4f532eeff9  7430773c4dcc9de44e0991f1c3b70888eaa95c0e
kagi         716f0169832cfc8f28ed28ab3b1dae350853e975  2bbd4daae8a117bc62a0761e828f5004c6617a5a
```

The sibling working trees the scouts read are clean for the two files (`git status --porcelain -- SKILL.md PROVINCE.md`
empty for all five), so a textual read and a `git show` read give the same bytes.

**F2 — The five cells are the checker's own derivation, not mine.**
`mechanical_findings(repo, head, values, lane, fleet_all, "adjacent")` returns no problem for any of
the five (`audio: OK`, `chousa: OK`, `game-dev-2d: OK`, `game-dev-3d: OK`, `kagi: OK`). This is the
same function that decides whether a census row's skill/names/arbitration cells are legal.

**F3 — Re-derivation of the r49 pins reproduces the committed r49 rows exactly (the required check).**
Same script, `cells_at(chk, lane, repo, <r49 pin>, fleet_all)` vs the
`git show 1e03d19:corpus/knowledge/sibling-overlap-census-round49.md` rows, comparing
`path`/`names kotoba`/`arbitration`/`commit`/`branch`/classification (from the base `PROVINCE.md` row):

```
audio: match          chousa: match        game-dev-2d: match
game-dev-3d: match    kagi: match
REDERIVE_ALL_MATCH=yes
```

So the checker's derivation has **not** changed since round 49 and none of the five r49 rows was
wrong on its mechanical cells. No discrepancy to report.

**F4 — `delta`, with the trap named.** `git -C <lane>-shokunin diff --shortstat <r49 pin> <head> -- SKILL.md PROVINCE.md`:

```
audio       (7a2fcd4f0883 -> 7a2fcd4f0883): (empty)          -> none
chousa      (6c5eb1466f2b -> 00f8c7f5272a): 1 file changed, 187 insertions(+), 20 deletions(-)  -> +187/-20
game-dev-2d (7753d49b1667 -> 7753d49b1667): (empty)          -> none
game-dev-3d (89dd182b7094 -> 89dd182b7094): (empty)          -> none
kagi        (899c50b42634 -> 69b61db46be4): (empty)          -> none
```

**kagi reads `none` although its commit cell is 6 commits behind the head** — the two files are
byte-equal across those commits, which I verified myself rather than taking from the scout:
`git -C kagi-shokunin log --oneline 899c50b4..69b61db4 -- SKILL.md PROVINCE.md | wc -l` → `0`;
`rev-parse` of both blobs at pin and head identical (`716f0169…`, `2bbd4daa…`). chousa moved 213
commits, 40 touching `SKILL.md`, 0 touching `PROVINCE.md`
(`git log --oneline 6c5eb146..00f8c7f5 -- PROVINCE.md | wc -l` → `0`).
*Operability note for the entry:* the `delta` column cannot distinguish "pin == head" from "commit
moved, both files byte-identical"; the r74 entry should say which case each `none` is, or a reader
will read kagi's `none` as "nothing happened".

**F5 — The `none` rule fires for kagi only, in my five.** `mechanical_findings(..., "none")`:
`audio: clear, chousa: clear, game-dev-2d: clear, game-dev-3d: clear, kagi: fire`. kagi's hit:

```
$ git -C kagi-shokunin show HEAD:SKILL.md | sed -n '297p'
  four committed defects: two `local://` scratch URIs, one kotoba path wearing
```

(11 words, the whole line — `awk '{print NF}'` → `11`; nothing dropped but the leading two spaces,
and the sentence's continuation on the next line.) `token_in("kotoba", …)` finds exactly one line in kagi's `SKILL.md` and none in its
`PROVINCE.md`; no other lane of my five has a hit in either file. **C2 (e) therefore forbids a
`none` row for kagi**; its r49 class `adjacent` is compatible. The audio/`game-dev-2d` rows have no
`SKILL.md` at all, so only `PROVINCE.md` can trip rule (e) and it does not.

**F6 — The r49 quotes still relocate at the freeze heads (measured, not asserted).** Running the
checker's `locate_quote` with each r49 row's own `path:line` and quote at the freeze head:

```
audio (PROVINCE.md:3): r49 quote relocates at PROVINCE.md:3
chousa (PROVINCE.md:3): r49 quote relocates at PROVINCE.md:3
game-dev-2d (PROVINCE.md:3): r49 quote relocates at PROVINCE.md:3
game-dev-3d (PROVINCE.md:3): r49 quote relocates at PROVINCE.md:3
kagi (PROVINCE.md:3): r49 quote relocates at PROVINCE.md:3
```

This is the plan's "carry-forward" shortcut world, and **for these five lanes it is mechanically
indistinguishable from an honest re-read on the quote arm** — the bytes are the same bytes. What
separates it are the `delta` cell (chousa `+187/-20` vs a carried r49 row's stale `none`) and the
class/evidence columns. That is a real bound of the C2 counter as frozen for this lane subset; it
should be stated in the entry, not glossed.

**F7 — The five rows pass the base checker's row checks end to end.** Scratch census of the five
rows (my cells + the scouts' proposed quotes/classes), base `check_census`:

```
rows 5 verified 5  province_rows 0 matched 0
failures 1
  - lane set: 15 sibling lane(s) never surveyed: kaidoku, kake, ..., tsukuroi
```

Nothing else fires: quote length ≥6 words, non-heading, commit 40-hex, cell completeness,
skill/names/arbitration derivation, `none` rule. The single failure is the fleet-wide lane set,
which the other three row seats and the merge complete.

**F8 — `PROVINCE.md` § Adjacent (rule d): two commit cells must be bumped.** Same scratch run with
`province_path` = base `PROVINCE.md`: `province_rows 20 matched 3`, and the two failures for my lanes
are exactly

```
  - province row 2 (line 14): lane chousa commit 6c5eb1466f2b does not match the census 00f8c7f5272a
  - province row 5 (line 17): lane kagi commit 899c50b42634 does not match the census 69b61db46be4
```

audio, game-dev-2d and game-dev-3d already match (their pins equal their freeze heads). The
classification cells must then be set equal to the entry's (r49 classes: audio `none`, chousa
`adjacent`, game-dev-2d `none`, game-dev-3d `none`, kagi `adjacent`).

## Cross-check against the sibling scouts (agreement, independently reached)

The scouts' JSONs, read after my derivation, agree on every cell I derive: `skill_file`, `delta`
(audio/`none`, game-dev-2d/`none`, game-dev-3d/`none`, chousa `1 file changed, 187 insertions(+),
20 deletions(-)`, kagi/`none`), and kagi's single `SKILL.md:297` kotoba hit. Their proposed
classifications are `none, adjacent, none, none, adjacent` for
audio, chousa, game-dev-2d, game-dev-3d, kagi — no conflict with my computed `none` rule (F5) and
no `none` claim for kagi. I recorded this as agreement only; every number above was produced by my
own command, not copied.

## Risks / blockers for the L1

1. **`PROVINCE.md` bump (F8)** — without it C2 (d) fails on chousa and kagi even with perfect rows.
2. **kagi class** — a `none` row for kagi fails C2 (e) deterministically; `adjacent` is what r49 and
   the scout both propose.
3. **`none` ambiguity in the delta column (F4)** — 4 of my 5 lanes read `none`; for kagi that is
   "6 commits moved, both files byte-identical", for the others "pin == head". The entry should say
   so, or the freshness claim reads weaker than the fact.
4. **Carry-forward bound (F6)** — on this lane subset the counter cannot tell a re-pin-plus-recomputed-delta
   from a carried row on the quote arm alone. Report it as the measured bound; do not claim the
   counter sees more.
5. **`no SKILL.md` cells are verbatim** — the checker compares lowercased, so `NONE` is legal in the
   skill-file cell while names/arbitration must read `no SKILL.md` exactly.
6. No blockers hit; nothing in the assignment was unreachable.

## Tooling and cleanup

No tool was installed or upgraded (none needed; `python3` + `git` only). Scratch directory
`/tmp/k74w1-ExecSibRowsAR74.YM59` held the base checker copy, the scratch census and the raw run
output, and was deleted before this report was returned; the scripts it produced are the two files
in the build directory listed above. No lane file, sibling repo, fleet repo, jj state or git index
was written.
