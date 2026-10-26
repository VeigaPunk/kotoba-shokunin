# ExecSibMergeR74 — the round-74 sibling merge tool (wave 1, build)

## Verdict

**Built, tested on fixtures, and run on the real wave-1 inputs. The join works: 20 of 20 lanes
join, both tables emit, and the emitted 9-column table passes the base census checker
`rows 20 verified 20` with `province rows 20 matched 20`, exit 0.** The real run is refused
(exit 2, by design) on exactly two scout cells: `chousa` and `kagi` put a prose sentence in
`proposed_classification` where the schema wants one of `contested`/`adjacent`/`none`.

Two defects that are **not** mine to fix, both with evidence below, block C2 as frozen:

- **F1** — the assigned `delta` cell makes the census table 10 columns, and the base
  `check_sibling_census.py` (which plan C2 (a) names as the row check) selects a table only at
  exactly 9 columns: on the 10-column table it prints `census table not found`, exit 1. The tool
  therefore emits two shapes; the 9-column one is byte-identical in form to the r49 table and
  passes today.
- **F2** — plan C2 clause (e) ("no `none` row exists for a lane whose pinned `SKILL.md` or
  `PROVINCE.md` contains the whole word `kotoba`") is unsatisfiable for `tabi`: `tabi` is `none`
  and its `SKILL.md` at the freeze head contains `kotoba` twice (a quoted `LANES=` string). The
  base checker's `none` rule reads the description and `PROVINCE.md` only, and it passes the row.

## Deliverables

All under `.ufo/waves/round-74/w1/build/ExecSibMergeR74/`; nothing else was written, no tracked
lane file was touched (`git status --porcelain -- SKILL.md PROVINCE.md corpus verifiers plans
LOG.md SCORECARD.md SHONEN.md README.md` → empty, tip `329e7d9`).

| file | sha256 | what |
|---|---|---|
| `merge_census.py` (656 lines, stdlib only) | `317ac86d3a6ae422f2f4e26d5ed2242186331e30bb7bb701046b5eb37f59dac8` | the tool |
| `roundtrip_test.py` (364 lines) | `770c9690518c4d49f3f976952c856f4021c7a09c1f8f3bf400046d87d933b0fe` | fixture round-trip + 11 refusal cases + a positive delta case |
| `roundtrip-test.log` | — | the full 15-check run (`RESULT PASS`, exit 0) |
| `roundtrip-r49-regenerated.md` | `c7029dc185ce4de51e1f9cca24e0d0c2bbcebc677fea0b58140e2ee422a07f2c` | regenerated r49 table |
| `roundtrip-province-regenerated.md`, `roundtrip-census-delta.md` | — | regenerated PROVINCE rows; the 10-column shape |
| `draft-real-census-enumnormalised.md` | `274c130d3cb91a9ccbb43f271c47612d603e35b946b703a8aa91572ef2739bd4` | **draft only**: the real inputs with the two prose classification cells reduced to their first word in a scratch copy (`classification_note` keeps the prose) |
| `draft-real-census9-enumnormalised.md`, `draft-real-province-enumnormalised.md` | — | the same, 9-column and PROVINCE shapes |
| `draft-real-census-plusminus-enumnormalised.md` | — | the 10-column draft with the counter's `+ins/-del` delta cell (20/20 equal to `check_sibling_reread.render_delta`) |
| `real-refusals-unfixed.txt` | — | the real run's two refusals |

CLI: `merge_census.py --inputs-root DIR | --rows PATH… --scouts PATH… --freeze PATH --shape
{census,census-r49,province} [--out PATH] [--base-rev REV] [--lane-root PATH] [--fleet-root PATH]
[--r49-pins PATH]`. Exit 0 on success, 2 on any refusal (all refusals printed, one per line,
`REFUSE <lane|path>: …`, nothing written).

## Round-trip proof (the assigned falsifier)

Fixtures were built **from the r49 entry itself**: the 20 rows of the 9-column table at
`corpus/knowledge/sibling-overlap-census-round49.md:67` were split into the four rows TSVs
(5 lanes each, `ExecSibRows{A..D}R74/rows.tsv`) and the ten scout JSONs (2 lanes each,
`ScoutSibFix01..10R74/<lane>.json`), with `boundary` taken from the base `PROVINCE.md` § Adjacent
row and `head40` = the r49 commit; a fixture freeze file was generated from the same rows.

```
python3 -B .ufo/waves/round-74/w1/build/ExecSibMergeR74/roundtrip_test.py \
  --lane /home/vgpnk/Projects/shokunin/kotoba-shokunin \
  --base 1e03d1991bc02281b00a5b7a5e00c9d5d5d72908 --work /tmp/k74w1-ExecSibMergeR74.XXXX
```

observed (log lines, verbatim):

```
PASS census-r49 round-trip against the r49 table: 22 line(s), diff empty
PASS province round-trip against base PROVINCE.md: 22 line(s), diff empty
PASS census shape: 20 rows, 10 columns, deltas ['none']
PASS delta-nonzero: exit 0, cell '2 files changed, 955 insertions(+), 5 deletions(-)', direct shortstat '2 files changed, 955 insertions(+), 5 deletions(-)'
RESULT PASS
```

- The census round-trip compares header + separator + all 20 rows against the r49 table block: a
  literal line diff, **empty**. The PROVINCE round-trip compares against the § Adjacent table of
  `git show 1e03d19:PROVINCE.md`: **empty**.
- `delta-nonzero` is the positive control for the delta cell: the `kake` freeze head was set to
  the live `kake-shokunin` head, so the recomputation must produce a real shortstat. The cell
  equals the direct `git diff --shortstat <pin> <head> -- SKILL.md PROVINCE.md` byte for byte —
  the tool computes the cell, it does not hardcode `none`.
- Two runs of the real census shape give one sha256 (`274c130d…` twice): the output is
  deterministic.

## Refusals exercised (11 cases, each exit 2 with the lane or path named)

`missing-rows-file`, `duplicate-lane`, `head40-vs-rows`, `head40-vs-freeze`, `empty-quote`,
`bad-classification`, `pipe-in-cell`, `lane-set-short`, `lane-set-extra`,
`changed-contradicts-delta`, `rows-quote-disagrees` — all PASS. Two examples, verbatim:

```
REFUSE kagi: head40 1111111111111111111111111111111111111111 differs from the freeze head 899c50b42634a3a4ad0b28ab7509786315e2fc2b in …/freeze.tsv
REFUSE tabi: boundary cell contains a `|` ('browser craft | not ours'); escaping is the author's job, this tool refuses
```

Beyond the assigned list the tool also refuses (each naming the lane): a rows row without a scout
record and the reverse; a rows `commit` disagreeing with the scout `head40`; a branch disagreeing
with the freeze branch; a non-40-hex commit; an empty required field; a `quote_path_line` that is
not `PATH:LINE`; a rows quote/`quote_at` disagreeing with the scout's; and `changed` contradicting
the recomputed delta. A lane named twice inside one file is refused by the same two-file path.

## Real-input run

Inputs as found at 22:43: all four `ExecSibRows{A,B,C,D}R74/rows.tsv` and all 20
`ScoutSib*R74/<lane>.json` (ten directories), freeze
`.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv`.

```
python3 -B …/merge_census.py --inputs-root .ufo/waves/round-74/w1/build \
  --freeze .ufo/waves/round-74/receipts/sibling-heads-freeze.tsv --shape census --out …
→ exit 2, 2 refusals:
REFUSE chousa: proposed classification 'adjacent -- decided by the second clause of the r49 rule (a split stated on kotoba's side, …' is not one of contested/adjacent/none
REFUSE kagi: proposed classification 'adjacent -- decided by the second clause of the r49 rule on both sides: …' is not one of contested/adjacent/none
```

Those are the only two. With those two cells reduced to their first word **in a scratch copy**
(`classification_note` keeps the prose; the lane's own reasoning is not lost), both shapes emit,
20 rows each, exit 0:

```
python3 -B …/merge_census.py --inputs-root /tmp/…/real --freeze …/sibling-heads-freeze.tsv --shape census
→ exit 0, 20 rows, 10 columns, 10 adjacent / 10 none / 0 contested
```

and the output is consumable by the base checker — this is the C2 (a) row check, run by me on the
projection, not by the counter seat:

```
python3 -B verifiers/check_sibling_census.py …/census9.md --province …/PROVINCE.md --fleet /home/vgpnk/Projects/shokunin
rows 20 verified 20
province rows 20 matched 20
checker_rc=0
```

(`PROVINCE.md` there is a scratch copy of `git show 1e03d19:PROVINCE.md` whose § Adjacent rows
were replaced by the generated ones; the checker needs the `## Adjacent` heading, which the tool
does not emit — the L1 pastes the rows under the existing heading.)

## Findings

**F1 — the `delta` cell and the base checker's 9-column selection conflict (plan C2 (a)).**
`verifiers/check_sibling_census.py:143` is `CENSUS_COLUMNS = 9` and `_select_table` (line 233)
keeps only blocks whose header has exactly that many cells. The 10-column table the item assigns
is therefore invisible to the checker plan C2 (a) names:

```
python3 -B verifiers/check_sibling_census.py …/census.md --fleet /home/vgpnk/Projects/shokunin
FAIL census table not found: no 9-column markdown table with a separator row in …/census.md
rows 0 verified 0      (exit 1)
```

Options for the L1, all supported by the tool: (i) land `--shape census-r49` as the entry's table
and have the C2 counter project/parse the 9 columns (the counter draft
`ExecSibCounterR74/check_sibling_reread.py:132` is `CENSUS_COLUMNS = 10`, so it cannot read that
table as written); (ii) land `--shape census` and make the counter project the 9 columns before
calling the base checker; (iii) amend plan C2 (a) to say the counter uses its own row parse. No
single table is readable by both tools — that is measured, not inferred: 10 columns → the base
checker prints `census table not found`; 9 columns → the counter's `len(header) != CENSUS_COLUMNS`
gate (line 436) fails. This is a plan-vs-checker conflict, not a tool bug: I changed neither.

**F2 — plan C2 (e) rejects a row the base rule accepts (`tabi`).** Plan (e): "no `none` row exists
for a lane whose pinned `SKILL.md` or `PROVINCE.md` contains the whole word `kotoba`". Measured at
the freeze heads with `git -C <lane>-shokunin grep -c -w -i kotoba <head> -- SKILL.md PROVINCE.md`:
`tabi SKILL=2 PROVINCE=0`, the two hits being a quoted fleet variable list —

```
856fa9e1…:SKILL.md:1313:  `LANES="protocol aggregator kasegi kengaku kake kumitate kotoba kagi kama"`
```

`tabi`'s class is `none`, so (e) as written caps N at 19 no matter what the scouts do; the base
checker's `none` rule (description + `PROVINCE.md`) passes the row, which is why `20 verified 20`
holds. Needs an addendum before data (Q28) or a counter that reads the description/PROVINCE rule.
Other lanes with hits are all non-`none` (kagi 1, kengaku 1+5, kotodama 1+1, kumitate 0+1).

**F3 — the delta cells reproduce the plan's before-values exactly.** From the real run:
`kake 2 files changed, 955 insertions(+), 5 deletions(-)`, `mori 462/15`, `tsukuroi 872`,
`revenger 618`, `tameshi 108/43`, `chousa 187/20`, `kaidoku 447/2`, `kama 417/8`, `kasegi 72/1`,
`kengaku 30`, `kotodama 85`, `kumitate 106/12`, `mado 118`, `souji 2/2`, `tabi 89`; `none` for
audio, game-dev-2d, game-dev-3d, kagi, lore. The plan's table said "kake +955, tsukuroi +872,
revenger +618, mori +462" — the pins in base `PROVINCE.md` § Adjacent are the right pins.

**F4 — `revenger`'s skill-file cell is now `SKILL.md`, not `NONE`.** Seat `ExecSibRowsDR74` derived
it at the freeze head (`cab8085` added the file, 2026-10-24); the tool copies the cell verbatim and
the base checker verified the row, so the r74 entry will differ from r49 here. A freshness change
the entry should show, not a merge decision.

**F5 — the classification counts are the scouts' judgement, and they move one row.** Real run:
10 `adjacent`, 10 `none`, 0 `contested` (r49: 9/11/0). The moved lane is `tsukuroi`
(`none` → `adjacent`), on a kotoba-side corpus entry landed at round 59 — its scout flags the call
as wave-2's. The merge does not judge a classification; it refuses a non-enum value and copies the
word.

**F6 — the first real run refused 42 problems; the parser was widened on evidence, not on a hunch.**
`ExecSibRowsBR74` and `ExecSibRowsCR74` pack evidence columns beside the join columns
(`r49_pin`, `path`, `path_line`, `scope_*`, `kotoba_hits_*`, `selfcheck`, their own `delta`), and 18
scouts write `changed` as prose or as `{"differs": false, "why": "…"}`. A join tool must not refuse
evidence: unknown header columns are now ignored (`path`→`skill_file`, `path_line`→`quote_at`), and
`changed` drives the delta cross-check only when it is a boolean or an object's boolean `differs`.
The strict refusals (enum, pipe, empty quote, head/freeze, lane set) were not relaxed — the same
run still refuses chousa and kagi.

**F7 — the delta cell has one owner, and it can be emitted in the counter's own form.**
`ExecSibRowsDR74/mechanics.tsv` formats delta as `+ins/-del`, and the C2 counter draft
(`.ufo/waves/round-74/w1/build/ExecSibCounterR74/check_sibling_reread.py:215-225`) compares the
cell to `render_delta(shortstat)` → `+<ins>/-<del>`, `none` when empty — while plan C2 (c) writes
the cell as the `git diff --shortstat` text. The tool now has `--delta-format
{shortstat,plusminus}` (default `shortstat`, the plan-literal string; `plusminus` for the counter).
With `--delta-format plusminus` on the real inputs, **all 20 cells equal the counter's own
`render_delta` applied to the same shortstat** (counter module imported from its draft, per lane:
`audio none/none … kake +955/-5/+955/-5 … tsukuroi +872/-0/+872/-0`; `mismatches: 0 of 20`). So the
format conflict the scribe seat recorded is closable from this side; the width conflict (F1) is
not, because the counter requires 10 columns (`CENSUS_COLUMNS = 10`, line 132) and the base
checker requires 9 — one table cannot be read by both. Evidence:
`draft-real-census-plusminus-enumnormalised.md`. A rows `delta` column is still ignored, so the
L1 pastes the tool's cell, never mechanics.tsv's.

**F8 — the tool is the only writer, and it writes nothing but `--out`.** No lane gate was run here
(the L1 owns post-integration gates); the base checker runs above were read-only over sibling
repos. No tool was installed or upgraded. Scratch dirs were deleted
(`ls -d /tmp/k74w1-ExecSibMergeR74.*` → none).

## Risks and blockers

- **Blocker for the L1's landing (2 cells):** `ScoutSibChousaKagiR74/{chousa,kagi}.json` must carry
  a bare `adjacent` in `proposed_classification`; their sentences belong in `boundary` (or a note
  key). Until then the real run is exit 2 by design. I did not edit another seat's file.
- **C2 cannot reach 20 under plan (e) as written** (F2), and cannot pass plan (a) with a 10-column
  table (F1). Both need a plan addendum before any data is scored, or a counter that reads the
  shapes this tool emits.
- The classification/boundary text is not verified by this tool (no `|`, non-empty, enum only);
  whether `adjacent`/`none` is right is the wave-2 seats' judgement, as the plan's Q26 bound says.
- Siblings keep moving after the freeze; the rows are valid at the frozen heads only.
