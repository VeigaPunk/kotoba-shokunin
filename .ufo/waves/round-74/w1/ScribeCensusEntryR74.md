# ScribeCensusEntryR74 — prose frame for `corpus/knowledge/sibling-overlap-census-round74.md`

**Verdict: the frame is drafted and self-consistent. The C2 landing has two unresolved blockers
(census table width; the `none` guard against tabi), one rendering choice the merge tool now
supports (the `delta` form), and one build blocker on the real inputs (two scout JSONs make the
merge exit 2).** The draft is
`.ufo/waves/round-74/w1/build/ScribeCensusEntryR74/entry-frame.md` (225 lines, 17,504 B): front
matter in the round-49 form, an intro carrying the freshness measurement, the rule restated only
by pointer, the census heading with a marker for the merge tool's 20-row table, the
`## What changed since round 49` placeholder table (6 columns, `<<…>>` cells), `## Counts`,
`## Findings that change kotoba's records`, `## Limits`, `## Recheck`. No product file was
touched; no sibling file was written; no tool was installed; no network fetch was made.

Correction to this seat's first draft of this report: it called the `delta` form a counter
mismatch that capped the figure at 5 of 20. That is superseded — the merge tool now exposes
`--delta-format plusminus`, and with it the two tools' cells agree on all 20 lanes (measured
below). The item is a landing flag, not a defect in either tool.

The open items, in order of what they block:

1. **Census table width.** The base checker selects a nine-column table only; the counter
   requires the tenth `delta` cell. One table cannot be read by both; the merge tool emits both
   shapes.
2. **The `none` guard against tabi.** The counter's clause (e) refuses a `none` row whose
   `SKILL.md` or `PROVINCE.md` carries the whole word `kotoba`; tabi's frozen `SKILL.md` carries
   it twice inside a quoted watchdog roster, and carried it at the round-49 pin. A mechanical
   20 of 20 and tabi's rule-correct `none` cannot both hold.
3. **`delta` rendering.** Now a landing choice: default is the collapsed shortstat, the flag
   gives `+ins/-del`, which the counter compares.
4. **Real-input merge refusal.** `merge_census.py` exits 2 with nothing written because chousa
   and kagi put prose in `proposed_classification`.

## Deliverable

- `.ufo/waves/round-74/w1/build/ScribeCensusEntryR74/entry-frame.md`
  - line 1 `source:` — S022 / S023 / S018 with their sections, then
    `sibling bytes: the 20 sibling lane repos at the heads frozen in .ufo/waves/round-74/receipts/sibling-heads-freeze.tsv`.
  - line 2 `verified-at: 2026-10-25`.
  - line 3 `recheck:` — `python3 -B verifiers/check_sibling_reread.py --rev <rev>` and
    `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md --province PROVINCE.md`.
  - headings, in order: `# Fleet sibling-overlap census (round 74)`,
    `## What decides between overlapping skills (unchanged; S022, S023, S018 cited from round 49)`,
    `## Classification rule`, `## Census (20 rows; quotes verbatim at each row's frozen head, whitespace collapsed)`,
    `## What changed since round 49`, `## Counts (each with its command, 2026-10-25 local; quoted receipt stamps are UTC)`,
    `## Findings that change kotoba's records`, `## Limits`, `## Recheck`.
  - the changed table is
    `| lane | r49 pin | r74 head | delta | classification r49 → r74 | why |` with the single row
    `| <<lane>> | <<r49_pin>> | <<head40>> | <<delta>> | <<r49_classification>> → <<proposed_classification>> | <<changed>> |`,
    preceded by the note naming each cell's source key in the scout JSON and stating that
    `delta` is not a scout value.
  - the census table is a comment marker:
    `<!-- merge_census.py (ExecSibMergeR74) writes the 20-row table here … -->`.

Structural check of the draft, run with the base checker's own parser:

```
$ python3 -B - <<'EOF'
import importlib.util
spec=importlib.util.spec_from_file_location("b","verifiers/check_sibling_census.py")
b=importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
lines=open('.ufo/waves/round-74/w1/build/ScribeCensusEntryR74/entry-frame.md').read().splitlines()
blocks=b.parse_blocks(lines)
print([(len(x["header"]),len(x["rows"])) for x in blocks])
print(b._select_table(blocks,b.CENSUS_COLUMNS,b.CENSUS_HEADER_TOKENS) is not None)
EOF
[(6, 1)]
False
```

i.e. the changed table is six cells wide (neither parser mistakes it for the census table), and
no nine-column census table exists yet — the merge tool's insertion is mandatory, as the
assignment says.

## Facts re-measured in this seat (not taken from a scout report or the plan)

Pins were read from the base `PROVINCE.md` (`git show 1e03d199:PROVINCE.md`), heads from
`receipts/sibling-heads-freeze.tsv`; one loop re-ran the plan's C2 (c) command for every lane.

- **20 pins, 20 freeze rows, 15 moved, 5 byte-equal.** Observed, per lane
  `git -C <lane>-shokunin diff --shortstat <pin> <head> -- SKILL.md PROVINCE.md`
  (run from `/home/vgpnk/Projects/shokunin`): 15 rows print a shortstat, 5 print nothing —
  audio, game-dev-2d, game-dev-3d, kagi, lore. Aggregate line printed by the loop:
  `MOVED: 15 SAME: 5`. The base receipt agrees:
  `.ufo/waves/round-74/receipts/sibling-staleness-base.tsv:3` — "rows 20; rows whose SKILL.md
  or PROVINCE.md differs between pin and branch head: 15".
- **Commits behind: 0 to 312 over all 20; 50 to 312 over the 15 moved.**
  `git -C <lane>-shokunin rev-list --count <pin>..<head>` → kasegi 50 (smallest moved), mori
  312 (largest); kagi moved 6 commits with both files byte-identical (`delta=none`), which is
  why the entry tests the shortstat, not the commit count.
- **Skill files at the frozen heads: 18 `SKILL.md`, 2 `NONE`.**
  `awk -F'\t' '!/^#/ && NF>=4 {print ($4=="-"?"NONE":"SKILL.md")}' .ufo/waves/round-74/receipts/sibling-heads-freeze.tsv | sort | uniq -c`
  → `2 NONE` / `18 SKILL.md`. The round-49 entry has 17 / 3 (next bullet).
- **Round-49 before-values, re-counted from the entry itself** (not from PROVINCE):
  `grep -cE '^\| [a-z0-9-]+ \| (main|master) \| [0-9a-f]{40} \|' corpus/knowledge/sibling-overlap-census-round49.md`
  → `20`; `awk -F' \| ' … '{print $5}' … | sort | uniq -c` → `9 adjacent` / `11 none`;
  `… '{print $4}' …` → `17 SKILL.md` / `3 NONE`. 0 `contested`.
- **revenger's `SKILL.md` was added after the round-49 pin, and three of its row's cells move.**
  `git -C revenger-shokunin cat-file -e 876630db:SKILL.md` → `fatal: path 'SKILL.md' exists on
  disk, but not in '876630db…'` (rc 128); `cat-file -e 6da884c6:SKILL.md` → rc 0;
  `git log --diff-filter=A --format='%h %ad %s' --date=short 876630db..6da884c6 -- SKILL.md` →
  `cab8085 2026-10-24 round-64: C1 admission … SKILL.md landed …`. The base checker's
  `description_of` over `git show 6da884c6:SKILL.md` → `''` (0 characters) and
  `token_in("kotoba", '')` → `False`, so the skill-file cell reads `SKILL.md` and both
  `names kotoba` and `arbitration` read `no`, where the round-49 row read `no SKILL.md` in
  both. The claim sweep
  `git -C revenger-shokunin grep -n -i -E "prompt[- ]?(craft|engineering|text)|skill craft|AGENTS\.md|frontmatter|description (craft|wording)|another lane|sibling'?s? SKILL|other lanes' SKILL" 6da884c6 -- SKILL.md PROVINCE.md`
  → rc 1, no output. I did not re-derive the other 19 lanes' mechanical cells: the base
  checker's clause-bound derivation is the authority and runs on landing.
- **tsukuroi's split sentence is kotoba-side and post-dates the round-49 pin.**
  `git -C kotoba-shokunin show 1e03d199:corpus/knowledge/hook-files-round59.md | sed -n '19,20p'`
  → line 20 reads `surfaces, out of prompt-craft province"). Host package and initramfs hooks
  are tsukuroi's`; the quote in the entry is the second sentence. Base `PROVINCE.md:71` reads
  "host operability and system repair; no split with kotoba on its scope surfaces (seat sweep
  in the census row's report)". `corpus/lessons/round-59-verifier-spotcheck.md:156` carries
  "adjacency | unchanged | 8.0 held; `w0/ConnSiblingHooks.md` FITS (tsukuroi host hooks kept
  apart)".
- **Proposed classes: 19 rows unchanged, 1 changed.** Read from the 20 scout JSONs
  (`ScoutSib*R74/<lane>.json`, keys `r49_classification`, `proposed_classification`): every
  lane's proposal matches its round-49 class except tsukuroi (`none` → `adjacent`). This is a
  count of the merge's inputs, not a result; the table and the counter own the landing.
- **Post-freeze drift, measured once and stamped in the entry.** At 2026-10-26T01:45:41Z,
  `git -C <lane>-shokunin rev-parse refs/heads/<branch>` against the freeze row: 4 of 20 had
  moved — kake (+1), kasegi (+2), kotodama (+2), souji (+3). The entry states the four lanes,
  not the counts, and stamps the time.

## Open items for the canonical judge (recorded, not adjudicated)

Line numbers in the two wave-1 drafts are volatile. Between this seat's reads,
`check_sibling_reread.py` grew from 66,303 B to 68,232 B and `merge_census.py` from 27,403 B to
28,274 B (it gained `--delta-format`; final sha256 `317ac86d3a6ae422…`); every citation below is
from the second read. The quoted
code text is the stable anchor, the line number is not.

### 1. Census table width: nine columns (base checker) vs ten (counter) — unresolved

- Base checker, `verifiers/check_sibling_census.py:143` `CENSUS_COLUMNS = 9` and
  `select_census_table` at `:233-234`; the refusal text is at `:625-626` ("census table not
  found: no %d-column markdown table …").
- Counter, `check_sibling_reread.py:132` ``CENSUS_COLUMNS = 10          # round-49 nine + `delta` ``,
  `parse_entry` at `:424-445` selects "the first block whose header has ten cells and whose last
  header cell is `delta`".
- Observed by this seat: `_select_table` over a ten-column header returns `None`; over the same
  table with nine columns it returns the table. The counter's refusal on a nine-column table is
  `check_sibling_reread.py:436` (`if len(header) != CENSUS_COLUMNS:`).
- The merge tool emits both, `--shape census` (10 cells) and `--shape census-r49` (9 cells), and
  its docstring (`merge_census.py:22-30`) says why the second exists. Its executor reports that
  the nine-column projection passes the base checker `rows 20 verified 20` today against a
  scratch `PROVINCE.md` (`province rows 20 matched 20`, exit 0) — that run is its measurement,
  not mine; I verified only the table-selection behaviour above.
- Consequence: the `recheck:` line this seat was instructed to write names the base checker on
  this entry *and* the counter; one table cannot satisfy both. The entry's `## Limits` states
  it; the landing decides.

### 2. The `none` guard against tabi's row — unresolved, and not a plan contradiction

- Plan (a), `plans/round-74.md:124`: "a `none` row names no `kotoba` in the sibling's
  description or `PROVINCE.md`" — this is the base checker's rule
  (`verifiers/check_sibling_census.py:595-601`: `token_in(SELF_LANE, description) or … token_in(SELF_LANE, province_text)`).
  Plan (e), `:133`: "no `none` row exists for a lane whose pinned `SKILL.md` or `PROVINCE.md`
  contains the whole word `kotoba`" — a separate, wider rule, implemented by the counter
  (`check_sibling_reread.py:64-67`, `:594`, `_check_none_rule` `:710-721`). They are two rules
  over different byte sets, not two readings of one clause.
- Observed at the frozen heads, `token_in("kotoba", <blob>)` over `SKILL.md` and `PROVINCE.md`
  for the ten scout-proposed `none` rows: tabi is the only lane with a hit — `['SKILL.md']`;
  the other nine are `neither`.
- tabi's hits: `git -C tabi-shokunin show 856fa9e1:SKILL.md | grep -n -w -i kotoba` →
  ``1313:  `LANES="protocol aggregator kasegi kengaku kake kumitate kotoba kagi kama"` `` and
  `1450:` the same string; `git -C tabi-shokunin grep -c -w -i kotoba e3cf4e0d -- SKILL.md PROVINCE.md`
  → `e3cf4e0d…:SKILL.md:2`, i.e. the round-49 pin carried the same two; `PROVINCE.md` 0 at the
  pin and at the head. The text is a quotation of a fleet watchdog roster, not a claim, and
  re-pinning cannot remove it.
- Consequence: (e) refuses the class the classification rule gives tabi (`none`), so a
  mechanical 20 of 20 needs either the row reclassified against the rule (with § Adjacent
  agreeing) or a pre-data amendment of (e) — the frozen plan was committed before any wave-1
  seat scored data (Q28), so this seat only records it. The counter seat reports the same and
  costs both edits in its report; I re-derived the token counts and the pin/head equality
  myself.

### 3. `delta` rendering — closable by a landing flag

- Plan C2 (c), `plans/round-74.md:129-131`, names only the `git diff --shortstat` command, not
  a rendering.
- The counter renders `+<ins>/-<del>` (`check_sibling_reread.py:215-225`, `render_delta`); the
  L1's seat prompt to that executor says "render as `+<ins>/-<del>` summed over both files,
  `none` when empty" (`w1-spec.json`, the counter item). The merge tool's default follows the
  plan literally, the collapsed shortstat text (`merge_census.py:49-52, 420-439`), and it
  offers the counter's form as `--delta-format plusminus` (`:631-636`).
- Observed by this seat on the real inputs: calling the merge tool's `shortstat_delta` with
  `delta_format="plusminus"` and the counter's `render_delta` over the same 20
  `git diff --shortstat` outputs gives **0 mismatches** — e.g. kake `'+955/-5'` on both,
  tsukuroi `'+872/-0'` on both, and `none` on both for the five byte-equal lanes. The default
  collapses to the other string (e.g. `'2 files changed, 955 insertions(+), 5 deletions(-)'`),
  which the counter refuses.
- Consequence: passing the flag satisfies (c); leaving the default fails it on the 15 moved
  lanes. Which rendering is declared is the integration owner's call; the entry's `## Limits`
  records both and says the census table is the merge tool's output.

### 4. The merge tool refuses the real inputs as they stand

- `python3 -B .ufo/waves/round-74/w1/build/ExecSibMergeR74/merge_census.py --freeze .ufo/waves/round-74/receipts/sibling-heads-freeze.tsv --fleet-root /home/vgpnk/Projects/shokunin --inputs-root .ufo/waves/round-74/w1/build --delta-format plusminus --shape census`
  → exit 2, 0 bytes on stdout, three `REFUSE` lines on stderr, of which the two lane lines
  name chousa and kagi and say their `proposed_classification` "is not one of
  contested/adjacent/none".
- Cause, measured: 18 of the 20 scout JSONs carry a bare class word in
  `proposed_classification`; chousa and kagi carry `'adjacent -- decided by …'` prose, and the
  generator refuses at `merge_census.py:501, 514-517` (`classification = scout["proposed_classification"]…`, then `if classification not in CLASSIFICATIONS:`).
  The split is producer-side: four lanes keep the reason in a separate key beside a bare value
  (kama and kasegi as `proposed_clause`, kumitate and mado as
  `proposed_classification_clause`), so chousa and kagi are the two records that put the prose
  inside the value. It is a scout-record conformance problem, not a merge bug. The merge
  executor reports the same and used a normalised scratch copy for its own end-to-end test
  (`.ufo/waves/round-74/w1/build/ExecSibMergeR74/draft-real-census-plusminus-enumnormalised.md`);
  I did not re-run that normalised copy.
- Consequence: no census table can be built from the committed inputs until those two JSON
  files carry the bare word. That is the merge/table owner's and the L1's to resolve; the frame
  cannot fix it.

## Peer correspondence (recorded, not averaged)

- `ExecSibCounterR74` replied that the `+<ins>/-<del>` form came from the L1's seat assignment
  and not from the plan, so item 3 is a ruling to be made before data; and that (e) is a
  separate wider rule, which its counter implements — I checked both against `w1-spec.json`
  and the code above and changed items 2 and 3 accordingly. Its added measurement (2 hits at
  the pin, 2 at the head, 0 in `PROVINCE.md`) I re-derived: same numbers. It also reported
  item 4 independently, at the same counts and the same refusal site, labelling it a
  producer-side blocker; its report cites this seat's 0-mismatch run as the confirmation that
  the two delta renderers agree.
- `ExecSibMergeR74` replied that `--delta-format plusminus` reproduces the counter's cells
  (`mismatches: 0 of 20`), that the width conflict is unfixable from either tool and it emits
  both shapes, and that plan (e) is unsatisfiable with tabi `none`. I re-derived the 0
  mismatches with both tools' own functions and the token counts; the width and tabi findings
  are as recorded.

## Assignment compliance, section by section

- `source:` — S022/S023/S018 carried from the round-49 front matter with their sections, plus the
  sibling-bytes clause in the instructed wording. The entry's only citation of those rows is
  § What decides, which points at `sibling-overlap-census-round49.md:14-42` and says it is not
  reopened; no page was fetched by this seat.
- intro — the 15-of-20 measurement, the 50–312 commit distance, the 18/2 skill-file split, the
  one proposed class change (tsukuroi, kotoba-side sentence), and the provisional status of the
  precedence rule (`PROVINCE.md:48`; `sibling-overlap-census-round49.md:416-458`).
- classification rule — pointer only, to `:43-64`, plus the round-50 precedence `:246-295` and the
  round-51 status `:416-458`; the entry contains no clause text of its own except the quoted
  phrases, and no class definition.
- changed table — the instructed six columns with `<<…>>` cells; the note above it names the
  scout keys and says `delta` is recomputed. 20 rows are the merge's job (one per frozen lane;
  the counter refuses a missing or an extra lane).
- Limits — siblings move after the freeze (four lanes named, timestamped); the counter measures
  pins/cells/quotes, not classification judgement; documentary evidence not router behaviour
  (`SKILL.md:16-18` at base, quoted; round-49 `:38-41` for the ten roots); the `none` guard is a
  token test (tabi, with the pin/head equality); the two table shapes; the two `delta`
  renderings and the flag that reconciles them.
- Recheck — both instructed commands, what each measures, and the "read the pins" note.

## Not done / unobserved

- I did not run `check_sibling_reread.py` (it is a wave-1 deliverable, not committed yet; the
  default `--rev` target is a landed entry, which does not exist). I did not run the counter's
  `--self-test`; that is its executor's report.
- I did not run the do-nothing or shortcut controls; both belong to `ExecSibControlsR74` /
  `ExecSibCounterR74`.
- I did not build a landed entry or run the base checker against one; item 1 is measured on
  parser selection, not on a full row pass.
- I did not verify the semantic classification of any lane; wave 2 owns that.
- I did not re-verify the scouts' quotes against sibling bytes lane by lane; the merge tool and
  the base checker do that on landing, and my prose quotes only sentences I read myself
  (tsukuroi, tabi, the freeze header, `PROVINCE.md:71`, `SKILL.md:16-18`).
- I did not re-derive the mechanical row cells for the 19 lanes other than revenger; the base
  checker's clause-bound derivation is the authority.
- The game-dev-3d boundary-text correction proposed by `ScoutSibGamedev3dLoreR74.md` is not in
  the frame: boundary text is the merge/PROVINCE surface, and I did not re-derive it.

## Bounds, tooling, scratch

- No tool installed or upgraded; no `pacman` transaction; no network fetch (so no URL/status/
  hash records to carry).
- No `mktemp` directory was created; the only writes are this report and the draft under
  `.ufo/waves/round-74/w1/build/ScribeCensusEntryR74/`, plus two transient files under `/tmp`
  (`/tmp/k74merge.err`, `/tmp/k74merge.out`) created by the merge-refusal probe and deleted
  immediately after. No lane file, no sibling repo, no jj state, no index was touched; all git
  calls were read-only (`show`, `grep`, `cat-file`, `log`, `diff`, `rev-list`, `rev-parse`).
- Longest single command: the 20-lane staleness loop, one shell invocation against 20 read-only
  repositories; its wall time was not recorded separately, and it returned inside the tool's
  deadline. Concurrency: at most two commands in flight (the batched read-only calls), under the
  cap of four.

## Artifact paths

- Draft: `.ufo/waves/round-74/w1/build/ScribeCensusEntryR74/entry-frame.md`
- This report: `.ufo/waves/round-74/w1/ScribeCensusEntryR74.md`
- Inputs read: `plans/round-74.md`; `corpus/knowledge/sibling-overlap-census-round49.md`;
  `PROVINCE.md`; `corpus/SOURCES.md` rows S018/S022/S023;
  `.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv`,
  `.ufo/waves/round-74/receipts/sibling-staleness-base.tsv`;
  `.ufo/waves/round-74/w1-spec.json`; `.ufo/waves/round-74/w1/ScoutSib*.md` and their
  `build/*/<lane>.json`; `verifiers/check_sibling_census.py`;
  `.ufo/waves/round-74/w1/build/ExecSibCounterR74/check_sibling_reread.py`;
  `.ufo/waves/round-74/w1/build/ExecSibMergeR74/merge_census.py`;
  `corpus/knowledge/hook-files-round59.md`; `corpus/lessons/round-59-verifier-spotcheck.md`.
