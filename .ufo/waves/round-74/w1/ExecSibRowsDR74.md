# ExecSibRowsDR74 — C2 mechanical row cells, five lanes (revenger, souji, tabi, tameshi, tsukuroi)

**Verdict: 5 of 5 lanes derived, 0 discrepancies against the round-49 cells, 0 freeze-integrity
mismatches, 2 findings the merge/counter seats must read before they join.**

Every cell below is derived with the **base** checker's own functions (`description_of`,
`token_in`, `git_show`, `repo_dir_for`, `fleet_lanes`, `NO_SKILL`, `extract_adjacent_section`,
`select_province_table`, `parse_blocks`, `select_census_table`, `mechanical_findings`) imported
from `git show 1e03d1991bc02281b00a5b7a5e00c9d5d5d72908:verifiers/check_sibling_census.py`
(sha256 `2f9d8a88b1d3dd8562455006d5ea89ec02546a1ecb9d023f327d88e5502eedc7`). Nothing about the
row shape, the description parse, the whole-word rule or the arbitration rule is re-implemented.
The base copy is byte-identical to the measured revision's file:

```
$ git diff 1e03d1991bc02281b00a5b7a5e00c9d5d5d72908 329e7d91d7d750031c35d264f0e34af1d0ce8385 -- verifiers/check_sibling_census.py
(empty; exit 0)
```

## Deliverables

All under `.ufo/waves/round-74/w1/build/ExecSibRowsDR74/`; no committed lane file touched
(`git status --porcelain` shows only untracked `.ufo/waves/round-74/...` paths).

| file | bytes | sha256 | content |
|---|---|---|---|
| `derive_rows.py` | 18833 | `220b35decbf749da2b4b537235767d86e1929babe366dc9b9f27f554b9d7c34a` | the derivation; self-contained (materialises the base checker from git, removes its temp dir) |
| `rows.tsv` | 444 | `019a7caeab3b3faee48869cf1cb95fdb018bbb2e9e4fbe972ceabf9eacc50aa1` | the merge seat's exact schema, `quote_at`/`quote` empty |
| `mechanics.tsv` | 1016 | `16aec0f1acc1fccd4e96423bf0e68ebb0ff6c171a09dafbfb2a850828d11f31d` | same rows + every mechanical cell (empty `classification`; `delta`; hit lines; scope spans; both none rules; per-file deltas) |
| `scopelines.tsv` | 5161 | `72091466b9f940970409223916c2f20eadc10f296c1748ecc0b368ffca905109` | every candidate scope-statement line, with `heading` yes/no so no scout quotes a heading (the row check refuses those) |
| `r49-recheck.tsv` | 1253 | `f137418eb962545a4a87b4b9e43a9e21b70ecc77cde7827f3e7e044919c1b34a` | the same derivation at the r49 pin vs the r49 census cells |
| `freeze-check.tsv` | 1706 | `1f94ab26d35520555e0b45c2bb5863464a03872f47b83ca66b82d15f28abf7cf` | frozen head/blob triples vs today's sibling git, plus branch-head drift |

`derive_rows.py` re-run command and result (byte-identical outputs on the second run — the hashes
above are from the self-contained run, after the `--base` argument was removed):

```
$ python3 -B derive_rows.py revenger souji tabi tameshi tsukuroi
… --- r49 recheck mismatches: 0
    --- freeze mismatches: 0        (exit 0; no /tmp residue: script removes its own dir)
```

`rows.tsv` verbatim (`cat -A` shows `^I` tabs; no cell contains `|` — asserted in the script):

```
lane	branch	commit	skill_file	names_kotoba	arbitration	quote_at	quote
revenger	main	6da884c6708fa25a7af013b6fc6802492e3264fa	SKILL.md	no	no		
souji	master	b8cb4b31ce80e2e3314b88e85d40ea9873180804	SKILL.md	no	yes: kagi		
tabi	master	856fa9e1202179f5cfbd28c1f0efdd4eb1f426bb	SKILL.md	no	no		
tameshi	master	a944eb55d64a2e0a77e3561c44bf89faadf04bb9	SKILL.md	no	yes: kama		
tsukuroi	master	8bd001f58bfda29c92d90d2a7a413825c0ca9fcb	SKILL.md	no	no		
```

Schema handshake: `ExecSibMergeR74` messaged this seat mid-run with its parser contract (8 columns,
header starting `lane`, 40-hex commit equal to the freeze head, `no SKILL.md` sentinel verbatim,
no `|`, one trailing newline) and said it refuses a lane set that is not the freeze file's 20
"across the four files". I answered with the schema confirmation and the lane-set note: this seat
is assigned **5 of 20** lanes (a sibling-seat partition; the four sibling-row seats' files together
are the 20). `classification` is not in the merge schema, so it lives in `mechanics.tsv` (empty,
scout-owned) together with the `delta` cell the C2 entry needs.

## The rows (mechanical cells)

`mechanics.tsv`:

| lane | branch | commit40 | skill_file | names_kotoba | arbitration | delta | delta SKILL.md | delta PROVINCE.md | kotoba hits SKILL.md | kotoba hits PROVINCE.md | scope spans |
|---|---|---|---|---|---|---|---|---|---|---|---|
| revenger | main | `6da884c6708fa25a7af013b6fc6802492e3264fa` | SKILL.md | no | no | +618/-0 | +618/-0 | none | — | — | PROVINCE.md:3-7 |
| souji | master | `b8cb4b31ce80e2e3314b88e85d40ea9873180804` | SKILL.md | no | yes: kagi | +2/-2 | +2/-2 | none | — | — | SKILL.md:2-2; PROVINCE.md:3-4,6-17 |
| tabi | master | `856fa9e1202179f5cfbd28c1f0efdd4eb1f426bb` | SKILL.md | no | no | +89/-0 | +89/-0 | none | SKILL.md:1313; SKILL.md:1450 | — | SKILL.md:3-3; PROVINCE.md:3-4,6-13 |
| tameshi | master | `a944eb55d64a2e0a77e3561c44bf89faadf04bb9` | SKILL.md | no | yes: kama | +108/-43 | +95/-43 | +13/-0 | — | — | SKILL.md:3-3; PROVINCE.md:3-5,7-12 |
| tsukuroi | master | `8bd001f58bfda29c92d90d2a7a413825c0ca9fcb` | SKILL.md | no | no | +872/-0 | +827/-0 | +45/-0 | — | — | SKILL.md:3-3; PROVINCE.md:3-4,8-14 |

`delta` = `git diff --shortstat <r49 pin> <freeze head> -- SKILL.md PROVINCE.md`, insertions and
deletions summed; the r49 pins are the base revision's `PROVINCE.md` § Adjacent commits
(revenger `876630db…`, souji `4edb25df…`, tabi `e3cf4e0d…`, tameshi `3b20f073…`, tsukuroi
`22fd1642…`), each an ancestor of its freeze head (`git merge-base --is-ancestor` exit 0 for all
five). Independently reproduced by hand, one example:

```
$ git -C tsukuroi-shokunin diff --shortstat 22fd1642e7fa4dfbdfba4419a443f06ffbb0b6c0 8bd001f58bfda29c92d90d2a7a413825c0ca9fcb -- SKILL.md PROVINCE.md
 2 files changed, 872 insertions(+)
$ git -C tameshi-shokunin diff --shortstat 3b20f073c7305a582562cd323982991464c324f3 a944eb55d64a2e0a77e3561c44bf89faadf04bb9 -- SKILL.md PROVINCE.md
 2 files changed, 108 insertions(+), 43 deletions(-)
```

(The plan's before-values cite `tsukuroi +872` and `revenger +618`; both reproduce.)

## Verification 1 — the r49 self-falsification (assignment requirement)

Re-derived the **round-49 pin** cells with the same script and compared to the r49 entry
(`corpus/knowledge/sibling-overlap-census-round49.md` rows 84–88): path, names-kotoba,
arbitration, commit, classification — 25 of 25 match, 0 mismatches (`r49-recheck.tsv`).

```
$ grep -c yes r49-recheck.tsv ; grep -c NO r49-recheck.tsv
25
0
```

The comparison is not vacuous: the no-skill branch is the one that would have failed. My first
draft derived `no`/`no` at revenger's r49 pin (no SKILL.md there) instead of the base sentinel, and
the re-check reported exactly those two cells as `NO`; switching to the base's own `NO_SKILL`
constant (`"no skill.md"`) turned them to `yes`. That is the discrepancy the assignment asked me
to look for — it was **my** derivation, not the checker and not the r49 row:

```
revenger	names kotoba	no SKILL.md	no	NO      (first draft)
revenger	arbitration	no SKILL.md	no	NO      (first draft)
```

## Verification 2 — freeze integrity and branch drift

`freeze-check.tsv`: 10 of 10 frozen `SKILL.md`/`PROVINCE.md` blob ids equal (5 lanes x 2 files; the file's other 5 rows are the branch-head drift rows)
`git -C <lane> rev-parse <head>:<path>` (0 mismatches) — the freeze file is a true statement about
the sibling repos. Branch drift since the freeze (freshness, for the wave-2 seats):

```
revenger	main	same        souji	master	ahead (freeze b8cb4b3…, branch now b862007…)
tabi	master	same            tameshi	master	same
tsukuroi	master	same
```

souji moved after the freeze but the freeze head is still an ancestor (`merge-base --is-ancestor`
exit 0), which is what C2 clause (b) requires; the row is valid at its pin, not at the round end.

## Verification 3 — the base checker's own verdict on these cells

`mechanical_findings` (the base function that re-derives the three cells from the pinned bytes and
applies the sibling-side `none` condition) accepts every derived row; and three negative controls
show it is not vacuous on these very bytes:

```
ACCEPT revenger problems=0 []      ACCEPT souji problems=0 []     ACCEPT tabi problems=0 []
ACCEPT tameshi  problems=0 []      ACCEPT tsukuroi problems=0 []
CONTROL-A (souji, names=yes / arbitration=no)
  ["names-kotoba cell 'yes' but the pinned description gives 'no'",
   "arbitration cell 'no' but the pinned description gives 'yes: kagi'"]
CONTROL-B (revenger, the r49 sentinels at the freeze head)
  ['SKILL.md exists at the pin but the skill cell says NONE',
   "names-kotoba cell 'no SKILL.md' but the pinned description gives 'no'",
   "arbitration cell 'no SKILL.md' but the pinned description gives 'no'"]
CONTROL-C token_in('kotoba', 'kotoba-shokunin kotobas xkotoba') -> True (whole-word rule is
  boundary-based: the hyphen is a boundary, so a lane-qualified mention counts)
```

The description spans are also self-checked in the script (the collapsed span text must equal
`description_of`'s value); no `SPAN MISMATCH` was printed on the final run.

## Finding 1 — revenger's `SKILL.md` has no YAML frontmatter, so its cells flip from the sentinel to `no`/`no`

At the r49 pin revenger had no `SKILL.md` (row: `NONE | no SKILL.md | no SKILL.md`). At the freeze
head the file exists (blob `082af19c…`) but line 1 is `# SKILL — revenger saved-ledger evidence
craft`, so `description_of` returns `''` and the mechanical cells are `SKILL.md`, `no`, `no` —
*not* `no SKILL.md`. Consequence for the scouts: revenger has **no description line to quote**;
its only candidate scope statements are PROVINCE lines 3–7:

```
$ git -C revenger-shokunin show 6da884c6708fa25a7af013b6fc6802492e3264fa:PROVINCE.md | sed -n '3,5p'
Owns: reverse engineering of shipped artifacts — native binaries, managed
assemblies, Electron/JavaScript packages, Android APKs, archives, firmware,
browser/Electron runtime evidence — using the REA skill and its toolset,
```

Quote taken from line 3 (10 words, line pasted above; lines 4–5 dropped):
"Owns: reverse engineering of shipped artifacts — native binaries, managed".

## Finding 2 — tabi: the base `none` rule and the plan's literal clause (e) disagree on the same bytes

tabi's whole `SKILL.md` at the freeze head contains the whole word `kotoba` on two body lines:

```
$ git -C tabi-shokunin show 856fa9e1…:SKILL.md | sed -n '1313p;1450p'
  `LANES="protocol aggregator kasegi kengaku kake kumitate kotoba kagi kama"`
  `LANES="protocol aggregator kasegi kengaku kake kumitate kotoba kagi kama"`.
```

Both are prose bullets quoting the fleet watchdog's `LANES` roster (context lines 1310–1315 and
1448–1452: "tabi is still absent from the watchdog `LANES` roster — `scripts/shokunin-watchdog.sh:14` →").
They are **not** a scope statement and not in the description or `PROVINCE.md` (hit cell `—` for
both there). So:

- the **base** none rule (`mechanical_findings`: description + whole `PROVINCE.md`) passes:
  `tabi none_rule_base = ok for none`;
- the **plan's** literal clause (e) wording ("whose pinned `SKILL.md` or `PROVINCE.md` contains the
  whole word `kotoba`") fails: `tabi none_rule_plan_e = blocked: kotoba named`.

Both readings are in `mechanics.tsv` per lane. If the C2 counter (`check_sibling_reread.py`, not
yet in `verifiers/` at this write) implements (e) literally, a `none` row for tabi is refused and
the entry must either reclassify tabi or the counter must adopt the base's rule — a decision for
the L1 and the counter seat, not for this one. Under the base rule the r49 `none` classification
is reproducible at the freeze head. The same two mentions sit at the **same line numbers** at the
r49 pin, and the r49 census row for tabi is `none` and passed the base checker:

```
$ git -C tabi-shokunin show e3cf4e0d30bb835532ff44b118c5ad52e09eb76d:SKILL.md | grep -inw kotoba
1313:  `LANES="protocol aggregator kasegi kengaku kake kumitate kotoba kagi kama"`
1450:  `LANES="protocol aggregator kasegi kengaku kake kumitate kotoba kagi kama"`.
$ git -C tabi-shokunin show <head>:SKILL.md | wc -l ; git -C tabi-shokunin show <r49 pin>:SKILL.md | wc -l
2530
2441
```

So the base rule, not the literal (e) wording, is the rule the r49 census actually met; a counter
that adopts (e) literally would retroactively fail the r49 entry's tabi row.

## Candidate scope-statement lines (for the ScoutSib* seats; `scopelines.tsv`)

Per lane, the description's physical lines with line numbers (description quoted only where a
frontmatter description exists) and every PROVINCE `Domain`/`Owns` block including its wrapped
continuation lines, each with `heading` yes/no:

- revenger: no description; `PROVINCE.md:3-7` (`Owns:` block).
- souji: `SKILL.md:2` (description, single 547-char physical line); `PROVINCE.md:3-4`
  (`**Domain:**`), `PROVINCE.md:6-17` (`## Owns` heading + its bullet list; the heading line is
  flagged `heading=yes` because a heading quote is refused by the row check).
- tabi: `SKILL.md:3`; `PROVINCE.md:3-4`, `PROVINCE.md:6-13` (`**Owns (surfaces):**` block).
- tameshi: `SKILL.md:3`; `PROVINCE.md:3-5`, `PROVINCE.md:7-12` (`**Owns:**` block).
- tsukuroi: `SKILL.md:3`; `PROVINCE.md:3-4`, `PROVINCE.md:8-14`
  (`**Owns (surfaces, all read-only probes):**` block).

Description lengths (`len(description_of)`, S018 cap 1024): revenger 0, souji 547, tabi 78,
tameshi 198, tsukuroi 79 — all inside the cap; no discrimination there.

## Risks / blockers

1. **tabi's `none` cell is a two-reading cell** (Finding 2). Until the counter seat decides, a scout
   writing `none` for tabi is correct under the base rule and refused under (e). Recorded, not
   resolved here.
2. **revenger's `quote_at` cannot be `SKILL.md`**: no frontmatter description, so a scout quoting a
   description line would be inventing one. Its r49 quote (`PROVINCE.md:3`) still re-locates
   byte-equal (`PROVINCE.md` unchanged since the pin, `delta PROVINCE.md = none`).
3. **Quote re-location risk by lane** (`delta SKILL.md` / `delta PROVINCE.md`): only tameshi and
   tsukuroi moved `PROVINCE.md` (+13/-0, +45/-0), so r49 PROVINCE quotes for those two are the only
   ones at risk; souji/tabi/revenger PROVINCE quotes re-locate if the target lines survived their
   `SKILL.md`-only deltas.
4. **Lane set is 5 of 20 by assignment** (merge-seat refusal rule noted above); the other 15 rows
   are the sibling-row seats' and the merge joins all four files.
5. No build/lint/gate was run: wave 1 is in flight and the parent owns the post-integration gates.
   No tool was installed or upgraded. No committed lane file was edited; no jj mutation; no
   write to any sibling repo or to `/home/vgpnk/Projects/shokuknow`.

Q69: this seat's name ends `R74`, every path above is in `kotoba-shokunin`, and no other lane's
round is named as this result.
