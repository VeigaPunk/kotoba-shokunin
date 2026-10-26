# ExecSibRowsCR74 — C2 mechanical row cells, five lanes (kotodama, kumitate, lore, mado, mori)

**Verdict: complete.** All five lanes' mechanical census cells are derived at the frozen fleet heads with the
**base** checker's own functions (imported, not re-implemented), the same script re-derives all four comparable
cells of all five **round-49** rows and they match (`## r49 re-derivation: all cells match the landed round-49
rows`, exit 0), and the five derived rows are accepted by the base checker itself in a scratch fixture
(`rows 5 verified 5`). Deliverables: `.ufo/waves/round-74/w1/build/ExecSibRowsCR74/rows.tsv`
and `.ufo/waves/round-74/w1/build/ExecSibRowsCR74/derive_rows.py`. `classification`, `path:line` and `quote` are left **empty** —
the scouts own them (this seat made no classification judgement).

No committed lane file was modified (read-only `git show` / `rev-parse` / `merge-base` / `diff` only; scratch under
`/tmp/k74w1-ExecSibRowsCR74.mWJ5`, deleted at return). The only git writes were made in a throwaway `--shared`
clone under `/tmp` for the pointer measurement in §8 (`git -C <fixture> rev-parse --show-toplevel` verified equal
to the fixture root before the single commit). No network used, no tool installed.

## 1. Deliverables

| path | sha256 |
|---|---|
| `.ufo/waves/round-74/w1/build/ExecSibRowsCR74/rows.tsv` | `5a0bb4a89828c2fd698a09b64b61f3d5471ddc2edbf3a8b0a19801f832e7e6dc` |
| `.ufo/waves/round-74/w1/build/ExecSibRowsCR74/derive_rows.py` | `727db8fb4f917524738066a66669408d7ae14930ade962e4be76d1269f8eef10` |
| base checker copy used (scratch, sha-pinned) | `2f9d8a88b1d3dd8562455006d5ea89ec02546a1ecb9d023f327d88e5502eedc7` |

The nine **first** TSV columns are exactly the round-49 census cells in census order — `lane | branch | commit |
path | classification | names_kotoba | arbitration | path_line | quote` — so the merge tool can take columns 1–9
as one census row and fill `classification`, `path_line`, `quote`. Columns 10–19 are this seat's derivation
evidence (`r49_pin`, `delta`, `r49_quote_at_head`, two kotoba-hit cells, four scope-line cells, `selfcheck`).

The script is re-runnable by the L1:

```
python3 -B .ufo/waves/round-74/w1/build/ExecSibRowsCR74/derive_rows.py \
  --scratch "$(mktemp -d)" --out /tmp/rows.tsv --fixture /tmp/fixture.md
```

## 2. Method — imported, not re-implemented (Q33: measured revision supplies bytes, not code)

```
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
git show 1e03d1991bc02281b00a5b7a5e00c9d5d5d72908:verifiers/check_sibling_census.py | sha256sum
→ 2f9d8a88b1d3dd8562455006d5ea89ec02546a1ecb9d023f327d88e5502eedc7  -
sha256sum verifiers/check_sibling_census.py
→ 2f9d8a88b1d3dd8562455006d5ea89ec02546a1ecb9d023f327d88e5502eedc7  verifiers/check_sibling_census.py
```

The base copy is byte-identical to the live working-tree checker, so the derivation cannot disagree with the
counter on *which code* re-derives the cells.

`.ufo/waves/round-74/w1/build/ExecSibRowsCR74/derive_rows.py` writes that base copy into scratch and imports it; it calls the checker's `git_show`,
`description_of`, `token_in`, `fleet_lanes`, `normalize_lane`, `NO_SKILL`, `collapse`, `strip_wrapping`,
`split_path_line`, `locate_quote`, `parse_blocks`, `select_census_table`, `select_province_table`,
`PROVINCE_COLUMNS`, `CENSUS_CELL_NAMES`, `mechanical_findings`. The only thing assembled locally is the
arbitration cell's string shape (`"yes: " + ", ".join(named)`, the checker's own expression at
`verifiers/check_sibling_census.py:591`), and it is **cross-checked** by feeding it back into
`mechanical_findings`, which re-derives the same three cells from the pinned bytes and names any mismatch;
`selfcheck` is `ok` for all five rows.

**Finding F0 (land-mine for the merge tool).** The arbitration vocabulary is not `fleet_lanes()`: the call site is
`mechanical_findings(repo, commit, values, lane, expected | {SELF_LANE}, classification)`
(`verifiers/check_sibling_census.py:746-747`), so **kotoba itself is a member** of the named set. My first run
used the bare fleet set and produced kotodama `yes: chousa, lore`, which does not match the landed r49 row
`yes: chousa, kotoba, lore`:

```
- kotodama arbitration: re-derived 'yes: chousa, lore' != r49 row 'yes: chousa, kotoba, lore' (census line 79)
```

Derived with `fleet_lanes(fleet) | {SELF_LANE}`, all five match (§3). Any merge/scout tool that re-derives
arbitration from the fleet directory set alone will silently disagree with the counter on every description that
names kotoba. The live fleet lane count is 20 siblings, 21 with kotoba
(`# fleet lanes (21): audio, chousa, game-dev-2d, game-dev-3d, kagi, kaidoku, kake, kama, kasegi, kengaku,
kotoba, kotodama, kumitate, lore, mado, mori, revenger, souji, tabi, tameshi, tsukuroi`).

## 3. Round-49 re-derivation — the verification the seat was asked for

Same script, same functions, run at each lane's **r49 pin** from `PROVINCE.md` § Adjacent, compared cell-by-cell
with the landed row of `corpus/knowledge/sibling-overlap-census-round49.md`:

```
# r49 re-derivation kotodama@35f0d49f: skill_file='SKILL.md' names='yes' arb='yes: chousa, kotoba, lore' | r49 row'SKILL.md'/'yes'/'yes: chousa, kotoba, lore' (line 79)
# r49 re-derivation kumitate@fac39171: skill_file='SKILL.md' names='no' arb='no' | r49 row'SKILL.md'/'no'/'no' (line 80)
# r49 re-derivation lore@380ef3ab: skill_file='SKILL.md' names='no' arb='yes: chousa, game-dev-2d' | r49 row'SKILL.md'/'no'/'yes: chousa, game-dev-2d' (line 81)
# r49 re-derivation mado@e33ea304: skill_file='SKILL.md' names='no' arb='no' | r49 row'SKILL.md'/'no'/'no' (line 82)
# r49 re-derivation mori@28b79d3d: skill_file='SKILL.md' names='no' arb='yes: kama, kumitate, tsukuroi' | r49 row'SKILL.md'/'no'/'yes: kama, kumitate, tsukuroi' (line 83)

## r49 re-derivation: all cells match the landed round-49 rows
EXIT=0
```

20/20 comparable cells match (5 lanes × `path`, `names kotoba`, `arbitration`, `commit`). No discrepancy: the
checker's derivation has **not** changed between the r49 landing and the base, and these five r49 rows were
right. Independent confirmation that the landed entry still passes its own guard at the base:

```
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md
→ rows 20 verified 20
  province rows 20 matched 20
  EXIT=0
```

## 4. Derived rows at the frozen heads (`receipts/sibling-heads-freeze.tsv`)

| lane | branch | commit40 (freeze) | path | names_kotoba | arbitration | delta (r49 pin → head) | kotoba hits (head) |
|---|---|---|---|---|---|---|---|
| kotodama | main | `f7104cbce186bc2e1522abf0cfd619cc834628bb` | SKILL.md | yes | `yes: chousa, kotoba, lore` | `+85/-0` | SKILL.md:3, PROVINCE.md:20 |
| kumitate | master | `2ca91a0c81542cad5f731049aa55dd2f99ade98d` | SKILL.md | no | `no` | `+106/-12` | PROVINCE.md:28 |
| lore | main | `380ef3abc7c7af11d7f23e9f9c82bb1937e1f695` | SKILL.md | no | `yes: chousa, game-dev-2d` | `none` | — |
| mado | master | `62dd798bb08401a8697383552edcc36f109344fa` | SKILL.md | no | `no` | `+118/-0` | — |
| mori | master | `24ebc7991e9081348d1aa4f558f994b1f4feccab` | SKILL.md | no | `yes: kama, kumitate, tsukuroi` | `+462/-15` | — |

r49 pins (from `PROVINCE.md` § Adjacent): kotodama `35f0d49f96f1d51f8b006136a8e1d0e8d0919a7a`, kumitate
`fac39171ac28c606e90da75fc2ba2ed3df52f4ea`, lore `380ef3abc7c7af11d7f23e9f9c82bb1937e1f695` (= the freeze head),
mado `e33ea30461f6e9bbeee40beef19770a953f7a105`, mori `28b79d3d1b76824f0c825aabe6cb6c5dc49961bf`.

`delta` recomputed two ways; they agree for all five (the spec command prints, e.g. for mori,
`2 files changed, 462 insertions(+), 15 deletions(-)`; the `--numstat` sum prints `+462/-15`):

```
for spec in "..."; do git -C "$lane-shokunin" diff --numstat "$pin" "$head" -- SKILL.md PROVINCE.md \
  | awk '{i+=$1; d+=$2} END{printf "+%d/-%d", i, d}'; done
→ kotodama: +85/-0   kumitate: +106/-12   lore: none (empty numstat)   mado: +118/-0   mori: +462/-15
```

`lore` reads `none` because its r49 pin **is** its freeze head
(`git -C lore-shokunin diff --shortstat 380ef3ab 380ef3ab -- SKILL.md PROVINCE.md` prints nothing).

Candidate scope lines (TSV `scope_skill_md` / `scope_province_md`, physical lines of the frontmatter
`description` and of the column-0 `Domain`/`Owns` lines):

| lane | `scope_skill_md` | `scope_province_md` |
|---|---|---|
| kotodama | SKILL.md:3 | PROVINCE.md:3, PROVINCE.md:9 |
| kumitate | SKILL.md:3 | PROVINCE.md:3, PROVINCE.md:5 |
| lore | SKILL.md:2–11 (10 physical lines, `description: >` block scalar) | PROVINCE.md:3 |
| mado | SKILL.md:3 | PROVINCE.md:3, PROVINCE.md:6 |
| mori | SKILL.md:3 | PROVINCE.md:3, PROVINCE.md:6 |

These are the *frontmatter/domain* candidates only; body scope statements are also legal (r49 quoted kotodama
`SKILL.md:8` and mado `SKILL.md:8`), which is why the TSV carries `r49_quote_at_head` (§5, F3).

## 5. Findings

**F1 — kotodama's branch moved past the freeze head during wave 1; its bytes did not.**

```
git -C kotodama-shokunin rev-parse main                        → 3595c919…
git -C kotodama-shokunin merge-base --is-ancestor f7104cbc main → exit 0
git -C kotodama-shokunin log --oneline f7104cbc..main
→ 3595c91 round-74: re-freeze — ledger tokens normalized, LC-01 annotated, LC-09 de-pinned, Ca counter patched …
   de93d91 round-74: freeze — final claims, ledger, counters, controls inputs, inherited round-73 w2 files, …
git -C kotodama-shokunin diff --stat f7104cbc..main -- SKILL.md PROVINCE.md
→ (empty)
```

The predicate is "commit cell equals the freeze head **and** that commit is an ancestor of the branch head", so the
row stays valid; the freeze head remains the citation. Recorded because a later seat reading `main` will see a
different tip than the freeze and must not "fix" it.

**F2 — kumitate's kotoba boundary sentence moved one line since the r49 pin (27 → 28).** `PROVINCE.md` § Adjacent
still says "kumitate `PROVINCE.md:27`"; at the freeze head the line is 28:

```
git -C kumitate-shokunin show fac39171:PROVINCE.md | grep -nw kotoba   → PROVINCE.md:27:…
git -C kumitate-shokunin show 2ca91a0c:PROVINCE.md | grep -nw kotoba   → PROVINCE.md:28:…
git -C kumitate-shokunin diff -U0 fac39171 2ca91a0c -- PROVINCE.md     → @@ -20,3 +20,4 @@
```

A scout copying the r49 boundary citation lands one line off (inside the checker's ±2 window, so the row still
verifies — but the PROVINCE boundary text is a reader pointer, not a gate-checked cell, and it is now imprecise).
The whole line, pasted from `sed -n '28p'` (18 words, no shaping):
"- Local model serving and endpoints → kama. Prompt and skill craft → kotoba. Research method → chousa."

**F3 — every r49 quote for these lanes still locates at the freeze head** (`r49_quote_at_head`, computed with the
checker's own `locate_quote` and its ±2 window):

| lane | r49 `path:line` | located at head |
|---|---|---|
| kotodama | SKILL.md:8 | SKILL.md:8 |
| kumitate | PROVINCE.md:3 | PROVINCE.md:3 |
| lore | PROVINCE.md:3 | PROVINCE.md:3 |
| mado | SKILL.md:8 | SKILL.md:8 |
| mori | PROVINCE.md:3 | PROVINCE.md:3 |

Mechanical only: this says a carried quote would still verify at the freeze head, **not** that the carried
classification is right. The scouts decide `adjacent`/`none`; the plan's carry-forward world is to be *measured*,
not asserted.

**F4 — lore's block-scalar description cannot be quoted across more than five physical lines.** `LINE_TOLERANCE
= 2` gives a 5-line window; lore's description spans physical lines 2–11. Probe with the base checker:

```
lines 3-10 words: 61
locate long quote cited at line 6: (False, None, False)
locate long quote cited at line 7: (False, None, False)
locate short quote (5-7) cited at line 6: (True, 4, False)
LINE_TOLERANCE = 2 -> window width 5 lines
```

A scout that collapses lore's whole "Sibling arbitration:" clause into one quote produces a row that can never
verify, however correct it is. The quote must fit 5 consecutive physical lines (or be one line).

**F5 — the freeze receipt's blobs hold for all five lanes** (`git rev-parse <head>:<file>` vs the receipt):

```
kotodama skill=match province=match
kumitate skill=match province=match
lore     skill=match province=match
mado     skill=match province=match
mori     skill=match province=match
```

So the freeze file's `skill_md_blob` / `province_md_blob` columns describe the bytes the derivation read.

**F6 — the derived cells pass the base checker itself.** Fixture: the five derived rows with `classification`,
`path:line` and `quote` **carried** from the r49 rows (clearly labelled in the fixture header; no classification is
made by this seat):

```
python3 -B <scratch>/base_check_sibling_census.py <scratch>/fixture-five.md --fleet /home/vgpnk/Projects/shokunin
→ FAIL lane set: 15 sibling lane(s) never surveyed: audio, chousa, game-dev-2d, game-dev-3d, kagi, kaidoku,
     kake, kama, kasegi, kengaku, revenger, souji, tabi, tameshi, tsukuroi
  rows 5 verified 5
  EXIT=1
```

`rows 5 verified 5` is the row-level proof: the checker re-derived `path`, `names kotoba` and `arbitration` from
each pinned `SKILL.md`, located each quote, and accepted each `none` row's sibling-side condition. The only failure
is the fleet-wide lane set, which a five-lane fragment cannot satisfy (the other 15 lanes are other seats').

## 6. What the scouts must fill (operability)

* `quote` — 6–25 words, copied from `git -C <lane>-shokunin show <freeze head>:<path>` via `sed -n '<L>p'`; the
  located line must not be a heading; ±2 lines of the cited line (`LINE_TOLERANCE = 2`); F4's 5-line window.
* `path:line` — the located line at the freeze head, **not** the r49 line (F2 is the live example).
* `classification` — the scouts' judgement; `none` is only legal when neither the pinned `SKILL.md` description nor
  `PROVINCE.md` names kotoba. At the heads that rule is consistent for lore, mado and mori (0 whole-word hits each);
  kotodama and kumitate **do** name kotoba (F7 below), so a `none` row for either is refused by the counter.
* Row shape: 9 cells, none empty; a duplicated lane is refused (`duplicate_lane_failures`).

**F7 — whole-word `kotoba` sweep at the freeze heads** (TSV columns 13–14, cross-checked with
`grep -ciw kotoba` over both files joined):

```
kotodama: SKILL.md:3  (description: "… NOT prompt/skill craft (kotoba-shokunin) …")   PROVINCE.md:20  ("(kake); prompt/skill craft (kotoba).")
kumitate: PROVINCE.md:28  ("… Prompt and skill craft → kotoba. …")
lore: 0 lines   mado: 0 lines   mori: 0 lines
```

`grep -ciw` line counts at the heads: kotodama 2, kumitate 1, lore 0, mado 0, mori 0 — matching the derived
cells, and the sweep is case-insensitive both ways (`token_in` uses `re.I`; `-i` added to `grep` for the
cross-check, since plain `-w` would have missed a capitalised `Kotoba`).

## 7. Risks / blockers

* **kotodama is live during the wave** (F1). The citation is the freeze head, which is still an ancestor and whose
  `SKILL.md`/`PROVINCE.md` bytes are unchanged — but a scout reading the branch tip will see a different commit
  hash. Use the `commit` cell of `.ufo/waves/round-74/w1/build/ExecSibRowsCR74/rows.tsv`, never `main`.
* The mechanical cells cannot change without a change to a lane's frontmatter description or `PROVINCE.md` at the
  freeze head; **all five cells are unchanged from r49** (kotodama yes/`yes: chousa, kotoba, lore`; lore's
  `yes: chousa, game-dev-2d`; mori's `yes: kama, kumitate, tsukuroi`). The deltas (`+85`, `+106/-12`, `+118`,
  `+462/-15`) are body growth and one body edit (kumitate `SKILL.md` has deletions below line 589), not scope
  statements — except kumitate's one-line shift (F2).
* No classification, no quote and no judgement of `adjacent`/`contested`/`none` is made by this seat; the fixture in
  F6 carries its cells from r49 and exists only to prove the mechanical cells pass the counter.
* Scratch `/tmp/k74w1-ExecSibRowsCR74.mWJ5` was used for the base checker copy and the fixture and is removed at
  return (the two files at `.ufo/waves/round-74/w1/build/ExecSibRowsCR74/` regenerate both with one command).

## 8. Pointer state (Q: the r74 report is run through `check_report_pointers.py`)

The report's own pointers are all concrete lane paths; the only unresolved ones before landing are the two
deliverable files (untracked at the base):

```
python3 -B verifiers/check_report_pointers.py --report .ufo/waves/round-74/w1/ExecSibRowsCR74.md --repo . --rev master
→ report pointers resolved 17 of 24; unresolved 7
  pointer objects: blob 17, directory 0
  unresolved: .ufo/waves/round-74/w1/build/ExecSibRowsCR74/{rows.tsv,derive_rows.py} and the same dir token
  EXIT=1
```

Measured **after** landing, in a throwaway shared clone (`/tmp/k74fixture-ExecSibRowsCR74.ellG/lane`, `mkdir` +
`cp` of the two deliverables and this report + one commit under the fixture identity, `rev-parse --show-toplevel`
verified first):

```
python3 -B verifiers/check_report_pointers.py --report .ufo/waves/round-74/w1/ExecSibRowsCR74.md --repo . --rev HEAD
→ report pointers resolved 24 of 24; unresolved 0
  pointer objects: blob 23, directory 1
  EXIT=0
```

So the L1's post-landing run of this gate should read `resolved 24 of 24; unresolved 0`. If it does not, the
deliverables were not committed with the report.

The kumitate line-28 quote in F2 was pasted from
`git -C ../kumitate-shokunin show 2ca91a0c81542cad5f731049aa55dd2f99ade98d:PROVINCE.md | sed -n '28p'`
(`wc -w` → 18); nothing was dropped from the line.
