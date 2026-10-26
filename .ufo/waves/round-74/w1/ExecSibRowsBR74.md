# ExecSibRowsBR74 — C2 mechanical row cells (kaidoku, kake, kama, kasegi, kengaku)

**Verdict: DELIVERED, no blocker.** Five lanes' mechanical cells derived from the frozen heads with
the base checker's own functions, verified by re-deriving the round-49 pins (5 of 5 match) and by
running the base checker over the committed round-49 entry (`rows 20 verified 20`, exit 0). Three
deliverables under `.ufo/waves/round-74/w1/build/ExecSibRowsBR74/`; no committed lane file touched;
no tool installed; no network used.

Two findings the L1 must act on before the C2 counter is measured (F6, F7): the plan's C2 predicate
(c) names a `delta` **row cell** while (a) demands the base checker's 9-cell row checks — a 10-cell
census table is rejected by that checker, proved (F6); and the plan's stated reason the bump-only
shortcut control fails is false for all five of my lanes — their round-49 quotes still re-locate
verbatim at the freeze heads (F7), so `delta` is the discriminator that contradiction forbids.

## Deliverables

| file | sha256 | bytes |
|---|---|---|
| `.ufo/waves/round-74/w1/build/ExecSibRowsBR74/rows.tsv` | `1bb107a32839676ef7913753a174712ff46a3ba8a9f8912d2e4f4605fdb8eac5` | 4374 |
| `.ufo/waves/round-74/w1/build/ExecSibRowsBR74/derive_rows.py` | `0b990b84ceabfb3aef08574dfe59ce1411db2379a8cd981f176c14e3cf176707` | 18145 |
| `.ufo/waves/round-74/w1/build/ExecSibRowsBR74/scope-candidates.tsv` | `fbf112baa8f015f5598b0163efd69987a4fc9260bbc7909494d8b969c5ff8209` | 3285 |

`rows.tsv` header (18 columns, one row per lane, 6 lines total):

```
lane	branch	commit	r49_pin	skill_file	classification	names_kotoba	arbitration	quote_at	path_line	quote	delta	kotoba_hits_skill_md	kotoba_hits_province_md	scope_skill_md	scope_province_md	scope_skill_text	scope_province_text
```

Column names follow the ones the other row seats already wrote — ExecSibRowsA/D (`skill_file`,
`names_kotoba`, `arbitration`, `quote_at`, `quote`) and ExecSibRowsC (`r49_pin`, `delta`,
`kotoba_hits_*`, `scope_*`) — so the merge seat joins one shape. `classification`, `quote_at`,
`path_line` and `quote` are deliberately **empty**: the scouts `ScoutSib*` own them.

Cells (from `cat rows.tsv`; text columns elided with `…` where long, full text is in the file):

| lane | branch | commit | skill_file | names_kotoba | arbitration | delta | kotoba hits SKILL.md | kotoba hits PROVINCE.md | scope lines |
|---|---|---|---|---|---|---|---|---|---|
| kaidoku | main | 3b1ab3c9d248b7afbf7fc5e5507d76cd87e26c3c | SKILL.md | no | no | +447/-2 | - | - | SKILL.md:3; PROVINCE.md:3,4,5,6 |
| kake | master | 20217f23eca15862febe14545523832e21584106 | SKILL.md | no | no | +955/-5 | - | - | SKILL.md:3; PROVINCE.md:3,5 |
| kama | master | 3e6fdbe9e0ca1ca5b633d0b312d5561301e924c4 | SKILL.md | no | no | +417/-8 | - | - | SKILL.md:3; PROVINCE.md:3,4 |
| kasegi | master | a155310d1ee9aacc07c3ce62328105a46c0392b4 | SKILL.md | no | no | +72/-1 | - | - | SKILL.md:3; PROVINCE.md:3,24 |
| kengaku | master | f9efce3beb0705ec2e04ba3f8f449d10d64cc1dd | SKILL.md | yes | yes: chousa, kama, kotoba, kumitate, tameshi | +30/-0 | SKILL.md:3 | PROVINCE.md:30,35,62,83,138 | SKILL.md:3; PROVINCE.md:3,5 |

`r49_pin` per lane: kaidoku `08c7a7299ed61c3fdc30ddb0adfe4e812d5eac76`, kake
`e73d48bbf20759fc7758afaebf841fa02e5cfbbf`, kama `c808ba07f09c4be55413d3d6516c542ab69b64f8`,
kasegi `1fafde8f11454f3b0b98ab7f2b2e640aaf7f399a`, kengaku
`1f3b0f1ec41ec297130e8944ff97968d32324632`.

`scope-candidates.tsv` (17 candidate lines, `lane/file/line/text`) carries the full collapsed text of
each description line and each PROVINCE `Domain`/`Owns` label plus continuation, so a scout can quote
without re-deriving where the statement starts.

## Derivation (F1) — base checker functions, not a second convention

Command:

```
cd .ufo/waves/round-74/w1/build/ExecSibRowsBR74 && PYTHONDONTWRITEBYTECODE=1 python3 -B derive_rows.py --verify-r49 --out rows.tsv --candidates scope-candidates.tsv
```

Observed:

```
checker: 1e03d1991bc0:verifiers/check_sibling_census.py sha256=2f9d8a88b1d3dd8562455006d5ea89ec02546a1ecb9d023f327d88e5502eedc7
fleet lanes: 20; freeze lanes: 20
kaidoku: branch head 3b1ab3c9d248; freeze head 3b1ab3c9d248 equal
kake: branch head 7ff637929c93; freeze head 20217f23eca1 ancestor
kama: branch head 3e6fdbe9e0ca; freeze head 3e6fdbe9e0ca equal
kasegi: branch head 43c364d06ccf; freeze head a155310d1ee9 ancestor
kengaku: branch head f9efce3beb07; freeze head f9efce3beb07 equal
wrote rows.tsv (5 rows) and scope-candidates.tsv (17 candidate lines)
r49 re-derivation: 5 of 5 lanes match on branch, commit, skill file, names kotoba, arbitration
```

The script `git show`s `1e03d199…:verifiers/check_sibling_census.py` into its own temp dir and imports
it; every cell comes from `description_of`, `token_in`, `fleet_lanes`, `git_show`,
`extract_adjacent_section`, `parse_blocks`, `select_province_table`, `collapse`, `split_path_line`.
Nothing is re-implemented; the measured revision supplies bytes only (Q33). `arbitration` is derived
over the base's own `all_lanes` set (`fleet_lanes(fleet_root) | {"kotoba"}`), and the run asserts that
set equals the freeze file's lane set (`fleet lanes: 20; freeze lanes: 20`), so a lane added or removed
after the freeze would stop the derivation instead of silently changing a cell.

## F2 — verification of the derivation against the committed round-49 entry: 5 of 5

Two independent paths, both green.

(a) Same script at the r49 pins (pins read from the base-revision `PROVINCE.md` `## Adjacent` table via
the checker's own `extract_adjacent_section`/`select_province_table`):

```
r49 re-derivation: 5 of 5 lanes match on branch, commit, skill file, names kotoba, arbitration
```

(b) The base checker itself over the committed entry at the live fleet:

```
git -C kotoba-shokunin show 1e03d1991bc0:verifiers/check_sibling_census.py > $D/base_checker.py
python3 -B $D/base_checker.py corpus/knowledge/sibling-overlap-census-round49.md --fleet /home/vgpnk/Projects/shokunin --province PROVINCE.md
--> rows 20 verified 20 / province rows 20 matched 20 / EXIT=0
```

So the checker's derivation did not change between round 49 and the base, and the round-49 rows for my
five lanes are not wrong.

## F3 — `delta` recomputed independently, and it matches the committed base receipt

```
git -C kaidoku-shokunin diff --shortstat 08c7a7299ed6… 3b1ab3c9d248… -- SKILL.md PROVINCE.md
 2 files changed, 447 insertions(+), 2 deletions(-)
git -C kake-shokunin    diff --shortstat e73d48bbf207… 20217f23eca1… -- SKILL.md PROVINCE.md
 2 files changed, 955 insertions(+), 5 deletions(-)
git -C kama-shokunin    diff --shortstat c808ba07f09c… 3e6fdbe9e0ca… -- SKILL.md PROVINCE.md
 2 files changed, 417 insertions(+), 8 deletions(-)
git -C kasegi-shokunin  diff --shortstat 1fafde8f1145… a155310d1ee9… -- SKILL.md PROVINCE.md
 2 files changed, 72 insertions(+), 1 deletion(-)
git -C kengaku-shokunin diff --shortstat 1f3b0f1ec41e… f9efce3beb07… -- SKILL.md PROVINCE.md
 2 files changed, 30 insertions(+)
```

The five `+ins/-del` sums equal `.ufo/waves/round-74/receipts/sibling-staleness-base.tsv` lines 9–13
(`+447/-2`, `+955/-5`, `+417/-8`, `+72/-1`, `+30/-0`). Note the last one: a diff with no deletions reads
`+30/-0` (the field is summed, not copied from the shortstat text).

## F4 — freeze integrity: blobs match the bytes read; two lanes moved after the freeze

For each lane the script asserts `git rev-parse <freeze head>:SKILL.md` equals the freeze file's
`skill_md_blob` and likewise for `PROVINCE.md`. Observed (12-hex prefixes):

```
kaidoku skill=match prov=match | SKILLblob=aa46a42b3c7d PROVblob=d453a29ddeb6 | HEAD=3b1ab3c9d248 branchhead=3b1ab3c9d248
kake    skill=match prov=match | SKILLblob=35626e09cec6 PROVblob=175fdab38832 | HEAD=7ff637929c93 branchhead=7ff637929c93
kama    skill=match prov=match | SKILLblob=d87d6f743f12 PROVblob=d55183990675 | HEAD=873c5d7774b9 branchhead=3e6fdbe9e0ca
kasegi  skill=match prov=match | SKILLblob=0e1b60d5db5d PROVblob=adf701525640 | HEAD=43c364d06ccf branchhead=43c364d06ccf
kengaku skill=match prov=match | SKILLblob=fb88848f2549 PROVblob=93be7bd95947 | HEAD=f9efce3beb07 branchhead=f9efce3beb07
```

Three observations for the counter author:

1. **kake** `refs/heads/master` is `7ff637929c93` (`round-57 verifier spot-check (integrator, hyaku)`),
   one commit past the freeze head `20217f23…`, which the script proved an ancestor
   (`merge-base --is-ancestor` → 0). Predicate (b) holds, but only if the counter measures
   `refs/heads/<branch>` and not the freeze head as "current".
2. **kasegi** `refs/heads/master` moved **during this seat's run**: `a155310d1ee9` at 22:34 -03 and
   `43c364d06ccf` at 22:40 -03 (`2026-10-25T22:40:29-03:00`). Its freeze head is still an ancestor. A
   counter that asserts equality with the live head instead of ancestry would flip red while the entry
   is correct.
3. **kama** has a **detached `HEAD` at `873c5d7774b9`**, a sandbox mutation commit (`mut4: corrupt
   cited blob hash in R35-WORDS row (sandbox only)`), while `refs/heads/master` is the freeze head
   `3e6fdbe9e0ca`. Any seat that reads `HEAD` in a sibling repo reads mutants: the freeze file's
   `branch` column is the reason it exists, and the counter must use it.

## F5 — the `none` guard (predicate e) is decidable from these cells

`kotoba_hits_*` are the base's `token_in("kotoba", line)` over every line of the two files at the frozen
head. Cross-checked with a second tool (`grep -nw kotoba` over `git show <head>:<file>`), which produced
the same line sets: kengaku `SKILL.md:3` and `PROVINCE.md:30,35,62,83,138`; the other four lanes no
hits in either file. Consequence for the scouts' classification:

- **kengaku** cannot be `none` — its pinned bytes name kotoba six times (predicate (e) refuses it).
- kaidoku, kake, kama, kasegi: `none` is mechanically admissible; whether it is *right* is the scouts'
  judgement, not a counter's (plan bound, `plans/round-74.md:146-148`).

kaidoku's round-49 row was `none` and its bytes at the freeze head still contain no whole-word kotoba,
so no mechanical drift forced a reclassification; the `+447/-2` drift is invisible to the row checks.

## F6 — plan attack: predicate (c)'s `delta` cell cannot live in a row that passes the base row checks

- `plans/round-74.md:121-122` (predicate a): "has exactly one row for `L` in the round-49 row shape and
  that row passes the **base's** `check_sibling_census.py` row checks" (20 words; the parenthetical that
  follows, "(every cell non-empty; quote ≥ 6 words …)", is dropped here).
- `plans/round-74.md:129` (predicate c): "the row's `delta` cell equals the counter's recomputation of
  `git diff --shortstat <r49 pin> <freeze head>" (16 words; further bytes on that line are dropped).
- The base checker fixes the row width: `verifiers/check_sibling_census.py:143` `CENSUS_COLUMNS = 9`,
  and `:664` fails any row whose cell count differs, and `:626` fails the whole file when no 9-column
  table is found.

Proved with a committed-bytes variant in scratch (round-49 entry + a `delta` cell appended to header,
separator and all 20 rows), run through the same base copy:

```
FAIL census table not found: no 9-column markdown table with a separator row in /tmp/…/census-10col.md
rows 0 verified 0        (exit 1)
```

So (a) and (c) are mutually exclusive inside one table: the counter must read `delta` from a **second
lane-keyed table** (or the L1 amends the predicate before data, Q28 — no rule change after a seat scores
data). `rows.tsv` keeps `delta` as a separate column precisely so either resolution works; the counter
needs one of (i) a second table `| lane | delta |` in the entry, or (ii) the plan addendum that says so.
An entry built by copying the 9-cell row and adding a 10th cell scores **0 of 20** on (a) — a silent
false negative that looks like a stale census.

## F7 — plan attack: the bump-only shortcut's stated kill does not happen for these five lanes

`plans/round-74.md:137-138` expects the world "the r49 entry copied with every commit cell bumped to the
freeze heads and nothing else" to fail because the "quotes die at moved lines for the changed lanes"
(9 words, that fragment). For my five lanes they do not die. Round-49 quote located at the freeze head
with the base checker's own `locate_quote` (same `path:line`, ±2 lines):

```
kaidoku  SKILL.md:3    at 3b1ab3c9 found=True matched_line=3 heading=False anywhere=[3] words=14
kake     PROVINCE.md:3 at 20217f23 found=True matched_line=3 heading=False anywhere=[3] words=12
kama     SKILL.md:8    at 3e6fdbe9 found=True matched_line=8 heading=False anywhere=[8] words=12
kasegi   PROVINCE.md:3 at a155310d found=True matched_line=3 heading=False anywhere=[3] words=11
kengaku  SKILL.md:3    at f9efce3b found=True matched_line=3 heading=False anywhere=[3] words=22
```

And the committed cells still re-derive identically (F2a), so the whole row passes. Running that world
(a copy of the round-49 entry with only my five commit cells bumped) through the base checker:

```
FAIL lane set: 15 sibling lane(s) never surveyed: audio, chousa, …, tsukuroi
rows 5 verified 5        (exit 1; the only failure is the deliberate 5-row slice)
```

Consequences the L1 should carry into the counter's control set:

1. The bump-only world is caught by (d) (PROVINCE unchanged ⇒ commit mismatch) and by (c) (no `delta`
   cell at all) — **not** by the quotes, for at least 5 of 20 lanes. If a future world also bumps
   `PROVINCE.md`'s `## Adjacent` commits consistently, then for these lanes the **only** discriminator
   left is the `delta` cell — the very cell F6 shows the 9-cell shape forbids. Those two findings are
   coupled; resolving one without the other leaves the shortcut control with no kill for ≤ 5/20 lanes.
2. The plan's wording should be corrected (a measured premise, not an assertion): quote survival must be
   *measured per lane* in the shortcut-control receipt, not asserted for "the changed lanes".
3. The pure carry-forward world (recomputed `delta`, quotes re-located) is, per the plan, measured and
   reported rather than asserted below 20 — that is consistent with what I observe here: my five lanes
   are exactly such a carry-forward, and their row cells are honest at the freeze heads.

## Candidates for the scouts (F8)

`scope_skill_md` for every one of my lanes is `SKILL.md:3` — the frontmatter description is a single
physical line in all five. `scope_province_md` is the `Domain` label plus its non-blank continuation
lines (kaidoku 3–6, kake 3+5, kama 3–4, kasegi 3+24, kengaku 3+5); label-only lines would have been
quoteable but would cut mid-statement, so the continuations are included and marked with their own
line numbers. kengaku's description is long (902 B on one physical line, `SKILL.md:3`; measured with
`git -C kengaku-shokunin show f9efce3beb07…:SKILL.md | sed -n '3p' | wc -c`) and contains a
literal `Sibling arbitration:` clause naming kotoba, kumitate, chousa, kama and tameshi — a scout
quoting the first 22 words of that line reproduces the round-49 quote exactly (F7).

## Risks / not observed

- **Not mine, not measured:** the other 15 lanes' rows, every `classification`, every `quote_at`/`quote`,
  and the `PROVINCE.md` § Adjacent edit. `PROVINCE.md` at base is unchanged by me.
- **Sibling motion:** kasegi's `master` advanced mid-run and kake's is one commit past the freeze. Rows
  are valid at the freeze heads; the counter must recompute ancestry (b) at measurement time.
- **`check_sibling_reread.py` does not exist yet** (`ls verifiers/ | grep -i sibling` → only
  `check_sibling_census.py`), so the frozen counter command at `plans/round-74.md:114` is unbuilt and F6
  could not be tested against it — only against the base row checks the predicate names.
- No `pacman`, no `uv tool`, no `npx` install was made; no network fetch. Scratch
  `/tmp/k74w1-ExecSibRowsBR74.KFLo` was created and will be deleted before this seat returns.
