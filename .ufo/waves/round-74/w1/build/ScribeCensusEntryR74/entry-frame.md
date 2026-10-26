source: S022 (https://code.claude.com/docs/en/skills, § Frontmatter reference `description` row, § Resolve skills that share a name, § Troubleshooting → Skill triggers too often), S023 (https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview, § Level 1: Metadata (always loaded)), S018 (https://agentskills.io/specification, § `description` field); sibling bytes: the 20 sibling lane repos at the heads frozen in .ufo/waves/round-74/receipts/sibling-heads-freeze.tsv
verified-at: 2026-10-25
recheck: python3 -B verifiers/check_sibling_reread.py --rev <rev>  # prints "sibling rows re-pinned and re-read N of 20", exit 0 when N == 20; then python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md --province PROVINCE.md  # the base checker's row checks: exits 0 only when every row's nine cells and its PROVINCE.md § Adjacent row match the bytes at the row's own commit

# Fleet sibling-overlap census (round 74)

This entry is a re-read at new pins, not a new method. It applies the round-49
classification rule to the same 20 sibling lanes, read at the heads frozen in
`.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv` (that file's line 1:
"sibling heads frozen 2026-10-26T01:25:43Z by the L1 before any wave-1 seat ran"; the
quote stops at "ran" — after it the line defines the branch ref).
The round-49 entry and `PROVINCE.md` § Adjacent carried the round-49 pins until this
round; this entry replaces them, lane by lane, with the commit each row was read at.

What changed since round 49, measured before this entry's rows were written:

- **15 of 20 siblings' `SKILL.md` or `PROVINCE.md` differ between the round-49 pin and
  the frozen head**, and 5 are byte-equal (audio, game-dev-2d, game-dev-3d, kagi, lore).
  Command, once per `## Adjacent` row of `PROVINCE.md` at base `1e03d199`:
  `git -C ../<lane>-shokunin diff --shortstat <pin> <frozen head> -- SKILL.md PROVINCE.md`
  — 15 rows print a shortstat, 5 print nothing. The base receipt states the same:
  `.ufo/waves/round-74/receipts/sibling-staleness-base.tsv:3` ("rows 20; rows whose
  SKILL.md or PROVINCE.md differs between pin and branch head: 15").
- **The 15 moved pins sit 50 to 312 commits behind their frozen heads**
  (`git -C ../<lane>-shokunin rev-list --count <pin>..<frozen head>`: kasegi 50 … mori 312).
  kagi's branch moved 6 commits with both files byte-identical, so commit count alone does
  not mark a row as moved; the shortstat above is the test the `delta` cell carries.
- **18 of the 20 lanes have a `SKILL.md` at the frozen head, 2 do not** (audio,
  game-dev-2d) — `awk -F'\t' '!/^#/ && NF>=4 {print ($4=="-"?"NONE":"SKILL.md")}'
  .ufo/waves/round-74/receipts/sibling-heads-freeze.tsv | sort | uniq -c` → `2 NONE`,
  `18 SKILL.md`. The round-49 census had 17 and 3: revenger's `SKILL.md` was added after
  its round-49 pin (finding 1 below).
- **One row's classification is proposed to change, and the change is on kotoba's side.**
  tsukuroi was `none` at `22fd1642`; kotoba's own corpus file written after that pin states
  a split — the sentence "Host package and initramfs hooks are tsukuroi's" at
  `corpus/knowledge/hook-files-round59.md:20` (line tail; the bytes before it close a
  previous sentence) — while the `PROVINCE.md` row at the round-49 pin says "no split with
  kotoba on its scope surfaces" (`PROVINCE.md:71` at `1e03d199`; the cell continues with a
  parenthetical about the seat sweep). A split stated only by
  kotoba may make a no-claim row `adjacent`
  (`corpus/knowledge/sibling-overlap-census-round49.md:246-295`, the round-50 precedence
  section), and the round-59 spot-check left tsukuroi's adjacency unchanged
  (`corpus/lessons/round-59-verifier-spotcheck.md:156`, "FITS (tsukuroi host hooks kept
  apart)"). The row's class is in the table below; the sentence above is why the two
  kotoba records disagree.
- **The rule the rows are decided under is provisional, and this entry does not extend it.**
  `PROVINCE.md:48`: the precedence rule "is provisional until the operator answers the fleet
  `.ufo/l0-questions.md` line 105"; its status and the bound on its generic-refusal exit are
  `corpus/knowledge/sibling-overlap-census-round49.md:416-458`.

## What decides between overlapping skills (unchanged; S022, S023, S018 cited from round 49)

Not re-opened this round. The reasoning stands as recorded at
`corpus/knowledge/sibling-overlap-census-round49.md:14-42`: the frontmatter `description`
is the matching input on each page, and none of the three pages states a tie-break between
two descriptions that both match, so the only arbitration a skill author controls is the
text of each description. The three source rows are cited above for that reason and for the
`arbitration` column's meaning; this entry opens no page and re-mines no row.

## Classification rule

Unchanged, and restated only by pointer: `corpus/knowledge/sibling-overlap-census-round49.md:43-64`
defines `contested`, `adjacent` and `none`, and its fourth bullet excludes wave reports and
run logs (`.ufo/`, `reports/`) as scope surfaces. The round-50 precedence section
(`:246-295`, `contested` against a stated split, and the definition of `contested` limited to
text another fleet lane owns) and the round-51 status of that rule (`:416-458`) are part of
the rule as applied here. No clause is redefined in this entry, and no classification in it
rests on a clause that section does not contain. `names kotoba` and `arbitration` are the
mechanical columns the rule defines; they are recomputed from the description at the row's
commit, not from the round-49 description.

## Census (20 rows; quotes verbatim at each row's frozen head, whitespace collapsed)

<!-- merge_census.py (ExecSibMergeR74) writes the 20-row table here: its `census` shape is the
     nine round-49 cells plus a trailing `delta` cell (shape question in § Limits), one row per
     frozen lane, sorted by lane as in round 49.
     Cells: the scout record's quote, quote_path_line, boundary and proposed classification;
     the commit is the freeze head; `delta` is the merge tool's shortstat recomputation
     (its rendering is one of the two documented ones, § Limits).
     Per-lane evidence (pin commands, sweeps, overlap quotes):
     .ufo/waves/round-74/w1/build/ScoutSib*R74/<lane>.json; rows TSVs in the four
     ExecSibRows{A,B,C,D}R74 directories. -->

Per-row evidence (pin commands, sweeps, overlap quotes): `../.ufo/waves/round-74/w1/build/ScoutSib*R74/<lane>.json`.

## What changed since round 49

One row per lane, 20 in all, in the census table's lane order. Each cell is filled from
that lane's scout record (`../.ufo/waves/round-74/w1/build/ScoutSib*R74/<lane>.json`:
`r49_pin`, `head40`, `r49_classification`, `proposed_classification`, and the `changed`
prose, which the `why` cell condenses); `delta` is the merge tool's recomputation of
`git diff --shortstat <r49 pin> <r74 head> -- SKILL.md PROVINCE.md`, not a scout value, and
the reread counter recomputes the same quantity independently. Values are placeholders until
the merge tool runs.

| lane | r49 pin | r74 head | delta | classification r49 → r74 | why |
|---|---|---|---|---|---|
| <<lane>> | <<r49_pin>> | <<head40>> | <<delta>> | <<r49_classification>> → <<proposed_classification>> | <<changed>> |

## Counts (each with its command, 2026-10-25 local; quoted receipt stamps are UTC)

`F` is this file, `corpus/knowledge/sibling-overlap-census-round74.md`, run from the lane
root; `R` is the round-49 entry, `corpus/knowledge/sibling-overlap-census-round49.md`.
Row regex: `^\| [a-z0-9-]+ \| (main|master) \| [0-9a-f]{40} \|`; fields under
`awk -F' \| '`: `$4` skill file, `$5` classification.

- The table carries 20 rows, one per frozen lane — `grep -cE '^\| [a-z0-9-]+ \| (main|master) \| [0-9a-f]{40} \|' F`; the lane set is the freeze file's
  (`awk -F'\t' '!/^#/ && NF>=5 {print $1}' .ufo/waves/round-74/receipts/sibling-heads-freeze.tsv | wc -l` → 20),
  and the counter refuses a missing or an extra lane.
- 15 of 20 lanes changed bytes since the round-49 pin, 5 did not — per-lane
  `git diff --shortstat <pin> <frozen head> -- SKILL.md PROVINCE.md` (see § intro); the
  before-receipt is `receipts/sibling-staleness-base.tsv:3`.
- **Before, at the round-49 entry** (unchanged since round 49, re-counted here): 20 rows —
  `grep -cE '^\| [a-z0-9-]+ \| (main|master) \| [0-9a-f]{40} \|' R`; 9 adjacent, 11 none,
  0 contested (that output has no `contested` line) —
  `awk -F' \| ' '/^\| [a-z0-9-]+ \| (main|master) \| [0-9a-f]{40} \|/{print $5}' R | sort | uniq -c`;
  17 `SKILL.md`, 3 `NONE` in `$4` — `awk -F' \| ' '/^\| [a-z0-9-]+ \| (main|master) \| [0-9a-f]{40} \|/{print $4}' R | sort | uniq -c`.
- **At the frozen heads**: 18 `SKILL.md`, 2 `NONE` (audio, game-dev-2d), counted from the
  freeze file's fourth column by the `awk` in § intro.
- The fresh count of this entry's own classes and its `N of 20` are the counter's output,
  not a second prose figure: `python3 -B verifiers/check_sibling_reread.py --rev <rev>`
  prints `sibling rows re-pinned and re-read N of 20` (`check_sibling_reread.py:745`).

## Findings that change kotoba's records

1. **revenger's round-49 row cells no longer describe the lane.** At the round-49 pin
   `876630db` revenger has no `SKILL.md`: `git -C ../revenger-shokunin cat-file -e 876630db:SKILL.md`
   → `fatal: path 'SKILL.md' exists on disk, but not in '876630db…'` (rc 128). At the frozen
   head `6da884c6` it has one: `cat-file -e 6da884c6:SKILL.md` → rc 0, and
   `git log --diff-filter=A --format='%h %ad %s' --date=short 876630db..6da884c6 -- SKILL.md`
   → `cab8085 2026-10-24 round-64: C1 admission … SKILL.md landed …`. Three cells of the row
   move, not one: the skill-file cell reads `SKILL.md`, and `names kotoba` and `arbitration`
   are recomputed from a file that now exists and carries no frontmatter — the base checker's
   own `description_of` over `git show 6da884c6:SKILL.md` returns `''` (0 characters) and
   `token_in("kotoba", '')` is `False`, so both read `no` where the round-49 row read
   `no SKILL.md`. That is a file addition, not
   a scope change: the claim sweep
   `git -C ../revenger-shokunin grep -n -i -E "prompt[- ]?(craft|engineering|text)|skill craft|AGENTS\.md|frontmatter|description (craft|wording)|another lane|sibling'?s? SKILL|other lanes' SKILL" 6da884c6 -- SKILL.md PROVINCE.md`
   prints nothing (exit 1), and the file's own § Scope governs three acts inside revenger.
2. **Two kotoba surfaces disagree on tsukuroi.** `PROVINCE.md:71` at the base commit
   `1e03d199` said "no split with kotoba on its scope surfaces";
   `corpus/knowledge/hook-files-round59.md:20` states the
   hook-file split quoted in § intro, written in round 59, after the round-49 pin. The
   round-59 spot-check kept adjacency unchanged (`corpus/lessons/round-59-verifier-spotcheck.md:156`
   carries "tsukuroi host hooks kept apart"). That corpus sentence is the basis the row's
   class rests on; the class cell itself is the table's, and the `PROVINCE.md` boundary text
   is the surface that went stale — it is the integration owner's to rewrite.

## Limits

- **Siblings keep moving after the freeze.** The rows are valid at their commit cells, not
  at the round end. Checked when this text was written (2026-10-26T01:45:41Z,
  `git -C ../<lane>-shokunin rev-parse refs/heads/<branch>` against the freeze row): 4 of
  20 branches had already moved — kake, kasegi, kotodama, souji. A row is read at its pin:
  `git -C ../<lane>-shokunin show <commit>:<path>`.
- **The counter measures pins, cells and quotes, not judgement.** It checks one commit cell
  against the freeze file, one `delta` cell against its own recomputation, the row shape,
  the located quote, the § Adjacent commit and class, and one mechanical `none` rule. It
  does not measure whether `adjacent`/`contested`/`none` is the right classification, nor
  whether a boundary sentence reads correctly; that judgement is assigned to named non-author
  wave-2 seats and their reviews are cited in the round report, not counted here.
- **Documentary evidence about sibling files, not router behaviour.** The lane `SKILL.md`
  files are not in an omp skill discovery root (`SKILL.md:16-18` at base `1e03d199`: "shokunin
  files sit outside the omp skill discovery roots, so this text never reaches the omp router —
  craft here is audit-side"; round 49's critic seat is recorded as having found no lane
  `SKILL.md` in the ten roots it checked, `…census-round49.md:38-41`), so the `arbitration` and `names kotoba` columns
  are audit-side facts about committed bytes. A description that names a neighbour is not an
  observation that a request routes to it.
- **The mechanical `none` guard is a token test, not a reading.** It fires on the whole word
  `kotoba` anywhere in the lane's `SKILL.md` or `PROVINCE.md`. tabi's frozen `SKILL.md`
  carries it twice — `git -C ../tabi-shokunin show 856fa9e1:SKILL.md | grep -n -w -i kotoba`
  → ``1313:  `LANES="protocol aggregator kasegi kengaku kake kumitate kotoba kagi kama"` ``
  and the same string at `1450`, both a quotation of a fleet watchdog roster — and the
  round-49 pin carried the same two (`git -C ../tabi-shokunin grep -c -w -i kotoba e3cf4e0d -- SKILL.md PROVINCE.md`
  → `…:SKILL.md:2`). The token therefore fires on a citation. Of the ten rows the scouts
  propose as `none`, tabi is the only one whose frozen `SKILL.md` or `PROVINCE.md` carries
  the token at all (the other nine carry it in neither file: `token_in` over the blob at the
  row's commit). The word is not drift: the same two hits are at the round-49 pin
  (`…:SKILL.md:2`) and at the frozen head, and `PROVINCE.md` carries none at either, so
  re-pinning cannot remove them. The base checker's own `none` rule reads only the
  description and `PROVINCE.md` (`verifiers/check_sibling_census.py:595-601`), which tabi's
  row passes; the counter's clause (e) reads both files, so as drafted it cannot score tabi's
  `none` row. A mechanical 20 of 20 and tabi's `none` row — the class the rule gives it —
  cannot both hold; this entry reports both readings rather than pick one.
- **The two recheck instruments want different table shapes.** The base census checker
  selects a nine-column census table only (`verifiers/check_sibling_census.py:143, 214-234`;
  observed: `_select_table` over a ten-column header returns `None`, over the same table with
  nine columns returns the table). The reread counter requires a tenth `delta` cell
  (`check_sibling_reread.py:132, 424-445`) and strips it before handing the nine cells to the
  base checker. The census table is the merge tool's output; which shape the landing carries
  decides which of the two recheck commands reads this entry, and that is the integration
  owner's call, not a measurement this entry makes.
- **The `delta` cell: one quantity, two renderings, and the landing must declare one.** The
  plan names only the command (`plans/round-74.md:129-131`); the counter renders it
  `+<insertions>/-<deletions>` (`check_sibling_reread.py:215-225`), and the merge tool's
  default is the collapsed `git diff --shortstat` text (`merge_census.py:49-52, 417-445`).
  The two strings differ for every non-empty diff — observed: `'+955/-5'` from
  `render_delta(" 2 files changed, 955 insertions(+), 5 deletions(-)")` against
  `'2 files changed, 955 insertions(+), 5 deletions(-)'`; equal only at `none`. The merge tool
  also offers the counter's form as `--delta-format plusminus` (`merge_census.py:631-636`),
  and with that flag its cells equal the counter's for all 20 frozen lanes (observed: 0
  mismatches). A landing that passes the flag satisfies the counter's clause (c); one that
  leaves the default fails (c) on the 15 moved lanes. The census table is the merge tool's
  output, so the rendering is a landing choice, recorded in the round report.

## Recheck

1. `python3 -B verifiers/check_sibling_reread.py --rev <rev>` → `sibling rows re-pinned and re-read N of 20`,
   exit 0 when N == 20. Per lane it reads this entry's row at `--rev`, demands exactly one
   row per frozen lane, a commit cell equal to the freeze head and an ancestor of the lane's
   branch head, a `delta` cell equal to its own recomputation from the round-49 pin, the
   matching `PROVINCE.md` § Adjacent row at `--rev`, and no `none` row over bytes carrying
   the whole word `kotoba`. Nothing is measured over the network; every byte comes from a
   sibling repository at a named commit.
2. `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md --province PROVINCE.md`
   → the base checker's own row checks over this entry: every cell non-empty; the quote at
   least six words and found at its `path:line` within ±2 lines (`verifiers/check_sibling_census.py:145`);
   the skill-file, `names kotoba` and `arbitration` cells recomputed from the pinned
   `SKILL.md`; a `none` row whose description or `PROVINCE.md` names kotoba refused; and, with
   `--province`, the lane set, class and commit of `PROVINCE.md` § Adjacent matched to the
   table.
3. Read the pins, not the branch tips. A failure names the row; the first thing to check is
   that the lane's repository still resolves the row's commit
   (`git -C ../<lane>-shokunin cat-file -t <commit>` → `commit`), because a row is a statement
   about that commit.
