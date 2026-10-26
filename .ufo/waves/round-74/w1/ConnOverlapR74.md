# ConnOverlapR74 — cross-claim contention map, round 74 (kotoba lane)

Seat: `ConnOverlapR74` (connector, wave 1, leaf member — no subagents dispatched).
Scope: every shared file, number and ordering constraint the two frozen claims (C1 depth/coverage
spec-craft, C2 freshness sibling re-pin) touch; the landing order that keeps each claim verifiable
alone; the numbers that must be re-recorded.

**Verdict.** The two claims do **not** collide on prose, and their corpus surfaces are disjoint
(C1 → `corpus/knowledge/spec-skill-creation-craft-round74.md` + `corpus/SOURCES.md`; C2 →
`corpus/knowledge/sibling-overlap-census-round74.md`). They collide on **three shared artefacts and
three shared numbers**, and the lane is currently **red on two battery gates** because of how the
freeze-2 commit ordered them:

1. **Both new gate-registry rows were committed (`d919179`) ahead of the paths they cite.** The
   checklist gate's `trigger.citation_resolves` therefore fails at `HEAD` (the two rows' verdict-map
   cells name `corpus/knowledge/spec-skill-creation-craft-round74.md`,
   `corpus/knowledge/sibling-overlap-census-round74.md` and
   `.ufo/waves/round-74/snapshots/MANIFEST.sha256`, none of which exist at `HEAD`).
2. **Both new registry rows fail their own pinned-values cells** → the registry gate reads
   `58 of 60`, exit 1.
3. The **SKILL.md frontmatter `description` has 5 characters of headroom** to the S018 1024 cap at
   base; C2's `tsukuroi none→adjacent` judgement forces a ~48-character clause into it. C2 alone
   cannot fit — it needs a matching compression elsewhere in the same frontmatter.

Recommended landing order (below) clears (1) and (2) in **one** commit before either claim is
measured, then lands C2 and C1 as separate measurable commits with the shared numbers re-recorded
per commit.

---

## A. Shared artefacts — who edits, and the collision

| artefact | C1 edits | C2 edits | collision? | who lands it |
|---|---|---|---|---|
| `SKILL.md` § Gate registry | 1 row (`check_spec_craft.py`) | 1 row (`check_sibling_reread.py`) | **shared block**, but the two rows are independent cells | L1 (both rows already landed in `d919179`) |
| `SKILL.md` § Compression rules | new `### Body craft — the specification's skill-creation guides` subsection (+ frame sentence at the `two harnesses here` text) | — | no | C1's commit |
| `SKILL.md` frontmatter `description` | — | `tsukuroi owns host package and initramfs hooks` clause | **shared numeric budget** (1024 cap), not shared text | C2's commit |
| `PROVINCE.md` § Core | 1 bullet naming the C1 entry | — | no | C1's commit |
| `PROVINCE.md` § Adjacent | — | 20 rows re-pinned to the freeze heads (commit + classification) | **no textual collision with C1**, but breaks `check_province_core.py`'s byte-identity conjunct | C2's commit |
| `corpus/knowledge/spec-skill-creation-craft-round74.md` | new | — | no | C1's commit |
| `corpus/knowledge/sibling-overlap-census-round74.md` | — | new (11-cell rows) | no | C2's commit |
| `corpus/SOURCES.md` | 3 rows (S223–S225) | — | no | C1's commit |
| `corpus/README.md` coverage map | 1 row (C1 entry) | 1 row (C2 entry) | shared file, disjoint rows | each claim's commit |
| `verifiers/corpus-baseline.json` | `tracked_files` +1 | `tracked_files` +1 | **shared counter, order-dependent** | each claim's commit (E1.3) |
| `verifiers/floors-registry.json` | — | — | **no row** (E1.3; adding one alone breaks the gate — § D2) | nobody |
| `verifiers/checklist-baseline.json` | 45 boxes, unchanged (table rows, not checkboxes — § D3) | — | no | nobody |
| `verifiers/census-removals.json` | — | — | not touched by either claim | nobody |
| `SCORECARD.md` / `LOG.md` | depth/coverage row | freshness row | shared files, separate rows | L1 at closure |

---

## B. The ordered landing sequence

### Step 0 — already landed (not mine, recorded for provenance)
- `329e7d9` plan + base receipts + r73-closure index row + id scratch.
- `d919179` **freeze 2**: both counters, both registry rows, `plans/round-74-addendum-1.md`, control
  self-test receipts.
- `d5aebcf` orchestrator in-flight snapshot (not a landing).

### Step 1 — **unblock commit** (L1; must land before any claim is measured)
One commit carrying:
1. `.ufo/waves/round-74/snapshots/` — `MANIFEST.sha256`, `FETCH-LOG.tsv`, `best-practices.md`,
   `using-scripts.md`, `quickstart.md` (**currently untracked**: `git status --porcelain` shows
   `?? .ufo/waves/round-74/snapshots/`).
2. `corpus/knowledge/spec-skill-creation-craft-round74.md` (**currently untracked**) and
   `corpus/knowledge/sibling-overlap-census-round74.md`.
3. `corpus/README.md` coverage-map rows for both entries.
4. `verifiers/corpus-baseline.json` re-recorded to the new `tracked_files` count.
5. **Correction of the two registry rows' pinned-values cells** (the exact defect in § C1/C2 below):
   drop the backticked `PAGE_SHA` token from `check_spec_craft.py`'s cell, and correct
   `check_sibling_reread.py`'s cell to `.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv`.

Rationale, all measured: without (1)+(2) the checklist gate is red at every rev; without (4) the
corpus gate is red; without (5) the registry gate is red. One commit clears all three because the
three gates read the same tree.

### Step 2 — **C2's commit** (measured alone at its own rev)
`corpus/knowledge/sibling-overlap-census-round74.md` (11-cell rows) **+ `PROVINCE.md` § Adjacent
re-pin** **+ `SKILL.md` description `tsukuroi` clause** **+ `corpus/README.md` row** **+
`corpus-baseline.json` bump** — all in the same commit, because predicate (d) requires PROVINCE's
row to carry the same commit and classification as the entry, and the base checker's `--province`
cross-check fails otherwise (§ C3).

The description clause must be net ≤ 1024 characters with the clause's lane named in a clause
carrying an ownership marker; measure before landing (§ D1).

### Step 3 — **C1's commit** (measured alone at its own rev)
`corpus/SOURCES.md` S223–S225 **+ `SKILL.md` § Compression rules subsection + frame sentence**
**+ `PROVINCE.md` § Core bullet** **+ `corpus/README.md` row** **+ `corpus-baseline.json` bump**.

### Step 4 — closure
`SCORECARD.md` / `LOG.md` rows, the tip battery in both invocation forms, the lesson.

**Separability caveat (E1.3 says each counter is measured at a sandbox revision holding only its own
claim's files on the base).** The registry rows for both counters landed in one commit (`d919179`),
so a revision "holding only C1's files" still carries C2's registry row. That is harmless for the
registry gate (rows are per-verifier, not per-claim) but it does mean the *literal* separability the
addendum describes is no longer reachable without rewriting `SKILL.md` history. The `sandbox`
measurement with a claim-scoped clone is still available and still the honest reading; the
*committed* revision carries both rows.

---

## C. Evidence — every finding, with its command and observed output

### C1 — the registry gate is red at `HEAD`: 58 of 60, exit 1

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
$ python3 -B verifiers/check_gate_registry.py --rev HEAD
verifiers/check_sibling_reread.py            no pinned path receipts/sibling-heads-freeze.tsv does not exist
verifiers/check_spec_craft.py                no pinned path PAGE_SHA does not exist; pinned path .ufo/waves/round-74/snapshots/MANIFEST.sha256 does not exist
gate registry rows conformant 58 of 60 lane verifiers; phantom 0
EXIT=1
```

Cause, from the guard's own code (`verifiers/check_gate_registry.py:judge_row`, pinned-values cell):
every **backticked** token in the pinned-values cell is treated as a repo-relative path and must
exist at the measured revision (`git cat-file -e <rev>:<path>`). Two tokens fail:

- `receipts/sibling-heads-freeze.tsv` — the real path is
  `.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv`. The freeze file **is** committed:
  `git cat-file -e HEAD:.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv` → exit 0.
- `PAGE_SHA` — a Python constant in `verifiers/check_spec_craft.py:203`, not a path. The row must
  name it without backticks (or as `in-file`).
- `.ufo/waves/round-74/snapshots/MANIFEST.sha256` — exists on disk, **not committed**:
  `git status --porcelain` → `?? .ufo/waves/round-74/snapshots/`.

Both counters are in the registry, so the **universe is 58 → 60** and both rows are required;
`phantom 0` confirms the row names are correct — only the pinned-values cells are wrong.

### C2 — the checklist gate is red at `HEAD` because the rows cite uncommitted paths

```
$ TMPDIR=/home/vgpnk/.scratch/k74conn python3 -B verifiers/check_tip_battery.py --rev HEAD
gate verifiers/check_gate_registry.py exit 1 wall 0.8s
gate verifiers/check_assertion_floors.py exit 0 wall 88.8s
gate verifiers/verify_skill_checklist.py exit 1 wall 2.2s
gate verifiers/verify_corpus_integrity.py exit 0 wall 0.3s
gate verifiers/verify_corpus_independent.py exit 0 wall 0.9s
gate verifiers/check_correction_sweep.py exit 0 wall 0.1s
fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery exit 0: 4 of 6
EXIT=1
```

and, in a fleet-shaped clone at `HEAD`:

```
$ python3 -B verifiers/verify_skill_checklist.py
FAIL trigger.citation_resolves: evaluated 193 — line 493: '../.ufo/reports/round-7/kotoba.md' does not resolve ...
```

The `../` noise is an artefact of the throwaway clone name (the same clone reports
`FAIL trigger.name_directory: name 'kotoba-shokunin' != directory 'hc'`); the lane-specific
failures are the three registry-row paths. On the **live tree** the same gate reports only the
unrelated routed-item-5 token:

```
$ python3 -B verifiers/verify_skill_checklist.py   # live worktree
FAIL trigger.citation_resolves: evaluated 203 — line 81: 'corpus/knowledge/chinese-vendor-skill-surfaces-round73.md:26,35-36' does not resolve ...
EXIT=1
```

That is a **separate live defect** (a `path:line,line-line` token in the routed `.agents/skills/`
decision row) and is C1/routed-item-5's to fix, not C2's — see § D4.

### C3 — C2's § Adjacent re-pin breaks two readers; both must be handled at landing

**(a) `check_province_core.py`'s no-harm conjunct.** Its `## Frontier` and `## Adjacent` sections
must be **byte-identical to its pinned base `a5f7459f99bb27bf697e9438362e75ac5833eca8`**
(`verifiers/check_province_core.py:87-92`). Today they are:

```
$ python3 - <<'PY'   # compare base a5f7459 vs tip 1e03d19
Frontier identical: True len base 2125 len tip 2125
Adjacent identical: True len base 8321 len tip 8321
```

Re-pinning one Adjacent commit cell breaks it (measured in a throwaway clone):

```
$ python3 -B verifiers/check_province_core.py --rev HEAD --repo "$D/lane"
measured-rev: 252c8689a02a817b76480d4333d5beb2ebcf3d20
province core rows 0 of 2
  - § Adjacent differs from the base
EXIT=1
```

`check_province_core.py` is **not** in the tip battery's six (BATTERY = gate_registry,
assertion_floors, skill_checklist, corpus_integrity, corpus_independent, correction_sweep), so this
does not break the battery — but the lane's own scorecard cites the counter's tip result
(`SCORECARD.md:435` "province core rows 2 of 2"). C2's landing therefore needs a decision: re-pin
that counter's `BASE` to the round-74 base (a frozen-counter change — Q28), or record the red gate
with its disposition. **Not in the plan's no-harm battery; not in the addendum.**

**(b) The base census checker's `--province` cross-check.** It compares PROVINCE's § Adjacent commit
cells with the census file's commit cells. Re-pinning PROVINCE alone (without the r74 census entry)
fails:

```
$ python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province "$D/PROVINCE.md"
FAIL province row 7 (line 19): lane kake commit 20217f23eca1 does not match the census e73d48bbf207
rows 20 verified 20
province rows 20 matched 19
EXIT=1
```

E1.3 already handles this (r49 entry checked **without** `--province`; r74 entry with `--province`).
The consequence to carry into the landing order: **PROVINCE § Adjacent and the r74 census entry must
land in the same commit.**

**(c) The r74 census table must be 9 columns for the base checker.** The base checker selects a
9-cell table (`CENSUS_COLUMNS = 9`). A 10-cell census table is refused outright:

```
$ python3 -B verifiers/check_sibling_census.py /tmp/k74conn-census10.md
FAIL census table not found: no 9-column markdown table with a separator row in /tmp/k74conn-census10.md
rows 0 verified 0
EXIT=1
```

A 9-cell census table **plus a separate** delta table passes (`rows 20 verified 20`, exit 0) — which
is why E1.2 (a) has the counter build the **9-cell projection** of the 11-cell row and run the base
checker on the projection. The registry row for `check_sibling_reread.py` says "11-cell row" and the
addendum says "10-cell entry row" in (a) and "eleventh `evidence` cell" in (f) — **11 cells
total** (9 projected + `delta` + `evidence`). These three numbers must be made to agree in one place
before the row is scored; today they read 10, 11 and 11.

### C4 — the base checker's `none` rule and the `tsukuroi` judgement

The base `none` rule reads the frontmatter **description** and `PROVINCE.md` only
(`verifiers/check_sibling_census.py:595-604`), which is why the plan's whole-file `grep -w kotoba`
clause was withdrawn (E1.2 (e)). Verified against the freeze heads in
`.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv`:

```
$ while read lane branch head skill prov; do ... git -C "$lane-shokunin" show "$head:SKILL.md" | grep -ciw kotoba ...; done < .ufo/waves/round-74/receipts/sibling-heads-freeze.tsv
audio 0/0   chousa 0/0   game-dev-2d 0/0   game-dev-3d 0/0   kagi 1/0
kaidoku 0/0   kake 0/0   kama 0/0   kasegi 0/0   kengaku 1/5
kotodama 1/1   kumitate 0/1   lore 0/0   mado 0/0   mori 0/0
revenger 0/0   souji 0/0   tabi 2/0   tameshi 0/0   tsukuroi 0/0
```

(SKILL.md / PROVINCE.md occurrences of the whole word `kotoba` at each lane's frozen head.)

- The sibling lane named **tabi** names kotoba twice in its `SKILL.md` — at lines 1313 and 1450,
  inside a `LANES="protocol aggregator kasegi kengaku kake kumitate kotoba kagi kama"` roster
  string. Its frontmatter `description` is `Domain specialist — browser & web-interaction craft.
  Rank: shonen (probation).` and its `PROVINCE.md` has 0 occurrences → the base rule keeps it
  `none`. **E1.2 (e)'s withdrawal is correct on the evidence.**
- **tsukuroi** at its frozen head: 0 occurrences in `SKILL.md`, 0 in `PROVINCE.md`. Its
  `none→adjacent` judgement therefore rests on **kotoba's own corpus**
  (`corpus/knowledge/hook-files-round59.md:19-20`), not on the sibling's bytes. That is exactly what
  E1.2 (f)'s `kotoba/`-prefixed evidence cell is for. **The judgement is sound, but its consequence is
  a SKILL.md frontmatter edit (below), and it is the one place where C2 reaches a C1-adjacent file.**

### C5 — the SKILL.md `description` has 5 characters of headroom, and C2 needs ~48

```
$ python3 - <<'PY'   # base SKILL.md description
description chars: 1019
headroom to 1024: 5
```

The cap is enforced by the base census checker's G4 rule (`SKILL_DESCRIPTION_MAX = 1024`,
`check_sibling_census.py:522-527`), and the lane's own census arm fails when it is crossed:

```
$ python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --skill SKILL.md
FAIL skill description length 1027 is outside 1-1024 characters (S018: the description field must be 1-1024 characters)
rows 20 verified 20
skill description names 9 of 9 non-none lanes
skill description length 1027 of 1024
EXIT=1
```

That 1027 reading was the **live worktree** mid-edit; the tree now reads **1021** (re-measured
after the L1's follow-up edit). So C2's clause has already been paid for by a compression of the
existing frontmatter. **The number to carry: base 1019 → the landed value must be ≤ 1024, and the
`tsukuroi` clause must sit in a clause carrying an ownership marker** (`owns/own/owned/route/
routes/routing/NOT/see above/see also` — `check_sibling_census.py:OWNERSHIP_MARKERS`).

This is the one **shared numeric budget** between the claims' SKILL.md edits: C1's frame sentence
lives in the body (`SKILL.md:24`), C2's clause in the frontmatter — different text, but the
frontmatter is a single 1024-char budget that only C2 spends and only C2 can overflow.

---

## D. The numbers that must be re-recorded, and the shared-number arithmetic

### D1 — SKILL.md frontmatter description: base 1019 → ≤ 1024
Owner: C2. Re-measure before landing:
`python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md --skill SKILL.md`
must print `skill description names 10 of 10 non-none lanes` and `skill description length N of 1024`
with N ≤ 1024, exit 0. Note the lane count rises **9 → 10** (tsukuroi) — the `names N of M` figure
in the no-harm receipt changes shape.

### D2 — floors registry: **15 rows, unchanged. Do NOT add a row.**
E1.3 declines the row on r73 precedent, and the precedent holds — `check_cn_vendor_surfaces.py` and
`check_report_pointers.py` carry no row. Adding one **alone** turns the floors gate to
could-not-evaluate:

```
$ (temp copy) add {"spec_craft": {"floor": 10, "path": "verifiers/check_spec_craft.py"}} to verifiers/floors-registry.json
$ python3 -B verifiers/check_assertion_floors.py --repo <copy>
exit 2
FAIL registry row vanish: spec_craft (listed in verifiers/floors-registry.json, absent from both guard tables)
FAIL registry path absent: spec_craft verifiers/check_spec_craft.py (declared in verifiers/floors-registry.json, not a non-empty file under <copy>)
```

The registry row would also have to be mirrored into the guard's two in-file tables
(`EXPECTED_INSTRUMENTS` + `INSTRUMENTS`) — and `check_assertion_floors.py` is one of the six
battery instruments whose blob is pinned (`INSTRUMENT_PINS`, `verifiers/check_tip_battery.py`), so
editing it trips the `instrument-pin` guard unless the pin list is amended too. **Answer: no floors
row; the two self-tests are unfloored and the lesson records the gap (as E1.3 says).**

### D3 — `verifiers/checklist-baseline.json`: **45 boxes, unchanged.**
`python3 -c "import json;print(len(json.load(open('verifiers/checklist-baseline.json'))['boxes']))"` → `45`.
The live tree's checklist gate still reports `45 — 45 boxes mapped`. C1's § Compression-rules
landing uses a **table**, not checkboxes, so no box is added and the baseline is untouched. A
checkbox would break it — measured:

```
$ (add a "- [ ]" box to SKILL.md)
FAIL checklist.box_map_complete: evaluated 46 — unmapped box at line 209 (section "Body craft — the specification's skill-creation guides", sha256 3b4d0710bdcb…)
EXIT=1
```

Every box is pinned by `text_sha256`, so any reworded box also needs a baseline re-record.

### D4 — `corpus-baseline.json`: `tracked_files` **139 → 141** (+1 more if a lesson file lands).
Current expectations, from the committed file:
`{'corpus.index.tracked_files': 139, 'corpus.index.unindexed': 0, 'corpus.index.stale_patterns': 0,
'corpus.index.missing_paths': 0, 'corpus.pointers.report_total': 97, 'corpus.pointers.report_dead': 0,
'corpus.pointers.commit_total': 41, 'corpus.pointers.commit_unresolvable': 0,
'corpus.pointers.commit_nonhash': 0}` — and the live tree matches them
(`python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json` → `tracked_files 139,
unindexed 0, report_total 97, report_dead 0, commit_total 41, commit_unresolvable 0`).

Each claim adds **one** tracked corpus file, so the count is **order-dependent**: C2 first → 140
then 141; C1 first → 140 then 141; both in one commit → 141 in one bump. E1.3 requires the bump in
the commit that adds the tracked file. Measured consequence of forgetting it:

```
$ (add an unindexed corpus/knowledge file)
corpus.index    tracked=139 unindexed=1 stale=0 missing=0
DRIFT   corpus.index.tracked_files: observed=139 expected=138
DRIFT   corpus.index.unindexed: observed=1 expected=0 / empty
6/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed, corpus.pointers.report_total
EXIT=1
```

Both claims' entries also need a **`corpus/README.md` coverage-map row** (column-2 token
`` `knowledge/<file>` ``) or they count as unindexed.

`report_total` / `commit_total` move with the new entries' citations (the r74 report and the
freeze-head commits) — re-record from the `--no-baseline --json` output, not by hand.

### D5 — gate-registry universe: **58 → 60**, and the count must read **60 of 60**.
`python3 -B verifiers/check_gate_registry.py --rev <tip>` — currently `58 of 60`, exit 1 (§ C1).
The registry row shape the two new rows must satisfy (from `judge_row`): exactly one row per
verifier; `kind` ∈ {gate, probe}; entry-command cell contains the verifier path; a `gate` declares
`0=clean` and `1=failed`; the self-test cell names a backticked flag that is an **exact active
`add_argument` handler** in the file (`--self-test` in both new counters — present);
pinned-values cell ≠ `none` for a gate and every backticked path in it must exist at the rev;
write scope non-empty; owner `kotoba`.

### D6 — `verifiers/census-removals.json`: **untouched by both claims.** It is the opencode-census
excuse ledger (`schema kotoba census-removals v1 (round 72)`); neither claim moves an opencode
surface. No re-record.

### D7 — SKILL.md line budget: **570 → 590** measured live, cap **600**.
```
$ wc -lc SKILL.md     # live worktree
590 lines
```
Budget stated in the plan/E1.3: 570 + 14 (C1 subsection) + 2 (registry rows) + 4 (routed item 5)
= 590. The checklist gate binds the cap from the file's own box (`File ≤ 600 lines`, line 267 at
base) and reports `PASS trigger.line_budget: evaluated 590 — 590 lines within budget 600 (from box
at line 285)`. **10 lines of slack.** Any further SKILL.md growth must be counted against it.

### D8 — tip battery: **6 of 6** is the target; **4 of 6** is the measured state at `HEAD`.
Full battery output at `HEAD` (fleet-shaped sandbox, base `072048fa8e8a52c707d25f7079772fa317244eb7`):
guards 5 of 5 (no-deletions, floors, instrument-size, instrument-pin, spotcheck-identity all PASS);
gates: gate_registry **1**, assertion_floors 0, skill_checklist **1**, corpus_integrity 0,
corpus_independent 0, correction_sweep 0 → `tip battery exit 0: 4 of 6`, exit 1. The two reds are
§ C1 and § C2 and both clear in the Step-1 commit.

### D9 — the `instrument-size` cap: **what it measures, and against which base.**
Read from the guard (`verifiers/check_tip_battery.py`): `BATTERY` is a **frozen six-script tuple**
(gate_registry, assertion_floors, skill_checklist, corpus_integrity, corpus_independent,
correction_sweep); `LINE_CAP = 40` is applied to the added and deleted lines of **those six scripts
only**, between `BASE = 072048fa8e8a52c707d25f7079772fa317244eb7` (**the round-73 base**, not the
round-74 base) and the measured rev, via `git diff --numstat`. **Two new counters of several hundred
lines do NOT trip it** — they are not in the tuple. Measured at `HEAD`, with both counters present:

```
guarded paths 586, deleted 0; floors 15 rows; instruments added 0 / deleted 0 lines (cap 40); spotcheck base files 27
guard instrument-size PASS
guard instrument-pin PASS
```

What *does* bind the new counters is the **gate-registry universe** (58 → 60, § D5), the
**floors registry** (§ D2), and the **`no-deletions` guard** — which fires only for base paths absent
at the rev, so additions are safe (`deleted 0`).

---

## E. Cross-claim risks not visible in either plan or addendum

1. **`check_province_core.py` is a silent casualty of C2** (§ C3a). It is not in the battery, so
   nothing in the round's no-harm list will catch it, yet `SCORECARD.md:435` cites its tip result.
2. **The registry row cells cite `PAGE_SHA` and a wrong freeze path** (§ C1). The addendum's E1.1
   names the constant correctly in prose (`a CONSTANT pinned in this file (PAGE_SHA)`); the registry
   row mis-transcribed it as a path.
3. **The 11-cell / 10-cell / 11-cell row-shape disagreement** (§ C3c) must be settled in one place
   before either counter is scored.
4. **Live defect in the routed `.agents/skills/` decision row**: the token
   `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md:26,35-36` does not resolve
   (`trigger.citation_resolves` FAIL, live tree). It is a `path:line,line-line` token that the
   citation resolver treats as a literal path. Fix by splitting the reference into a resolvable path
   plus a separate line citation. Owner: routed item 5 / C1's SKILL.md edit — **not** C2's.
5. **`corpus/SOURCES.md` id spaces.** The lane registry is S001–S222 (148 rows); the staged package
   is S203–S390 with 20 collisions on S203–S222; the campaign's per-round register uses S236/S237
   for `skills.sh/docs` and `skills.sh/audits`, which are **not** the package's S236/S237
   (agentskills.io using-scripts / quickstart). The live C1 rows take **S223 best-practices,
   S224 quickstart, S225 using-scripts** — so a reader who knows the package numbering will look for
   using-scripts at S236 and quickstart at S237 and find S225/S224. Bind page↔id by **URL path**
   (predicate (b′)) and **anchor digest** (c′), never by id number; the SOURCES rows' `used-by`
   must name the C1 entry so the link is closed from the other side.
6. **The r73-closure search-log damage in `corpus/SOURCES.md`** (lines ~210–220: truncated log
   notes and two stray `## Leads (unopened)` headings at 220 and 223) is a **pre-existing** defect
   (r73 lesson item 4) and is not caused by this round. The fleet census still passes it:
   `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → exit 0, 20
   `W04` duplicate-URL warnings, no `E##` findings. C1's three rows append after S222 and are
   appends, not protected-cell rewrites: `check_sources_append_only.py --rev HEAD` reports
   `18 change(s) in 8 of 44 commits` and the **same** command at the round base reports
   `18 change(s) in 8 of 43 commits` — the breach count is unchanged from base, i.e. pre-existing.
   C1 must not add a breach; it does not need to fix the old ones.
7. **`check_sibling_census.py --skill` on the r74 entry changes the lane count** 9 → 10 (tsukuroi).
   Any receipt that quotes `names 9 of 9` from the r49 entry stays true for the r49 entry; the r74
   entry quotes `10 of 10`. Two different numbers in one report must not be conflated.

---

## F. Verification I performed (all read-only; no lane file modified)

| command | observed |
|---|---|
| `python3 -B verifiers/check_gate_registry.py --rev HEAD` | `58 of 60 … phantom 0`, exit 1; two pinned-path failures named |
| `python3 -B verifiers/check_gate_registry.py --rev d919179` | `58 of 60`, exit 1 (same two failures) |
| `python3 -B verifiers/check_tip_battery.py --rev HEAD` (fleet-shaped sandbox, `TMPDIR` on `/home`) | guards 5 of 5; `tip battery exit 0: 4 of 6`, exit 1; wall 108.8 s |
| `python3 -B verifiers/check_tip_battery.py --rev 329e7d9` | guards 5 of 5; `6 of 6`, exit 0; wall 96.4 s — **the 4 of 6 is new since the plan commit** |
| `python3 -B verifiers/check_spec_craft.py --rev HEAD` | `spec craft pages backed 0 of 3`, `held at base: 0`, exit 1; names the absent entry and the absent § Core bullet |
| `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` | `rows 20 verified 20`, `province rows 20 matched 20`, exit 0 |
| `python3 -B verifiers/check_sibling_census.py … --skill SKILL.md` | `names 9 of 9`; `length 1027 of 1024` FAIL at the 1027 reading; exit 1 |
| `python3 -B verifiers/check_province_core.py --rev HEAD` | `province core rows 2 of 2`, exit 0 |
| `python3 -B verifiers/check_province_core.py --rev <repin>` (clone) | `0 of 2`, `§ Adjacent differs from the base`, exit 1 |
| `python3 -B verifiers/check_sibling_census.py <10-col table>` | `census table not found: no 9-column markdown table`, exit 1 |
| `python3 -B verifiers/check_sibling_census.py <9-col + separate delta table>` | `rows 20 verified 20`, exit 0 |
| `python3 -B verifiers/check_cn_vendor_surfaces.py --rev HEAD` (clone with a C1 § Core bullet) | `vendor skill surfaces backed 4 of 4`, `province surfaces named 4 of 4`, exit 0 — **C1's Core bullet does not break it** |
| `python3 -B verifiers/check_author_rules.py --rev HEAD` | `author-facing rules in SKILL.md 4 of 4`, exit 0 |
| `python3 -B verifiers/check_correction_sweep.py --root .` | `correction sweep: 0 stale block(s)`, exit 0 |
| `python3 -B verifiers/check_sources_append_only.py --rev HEAD` / `--rev 1e03d19` | `18 change(s) in 8 of 44 commits` / `… of 43 commits` — unchanged from base, pre-existing |
| `python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json` | `tracked_files 139, unindexed 0, report_total 97, report_dead 0, commit_total 41, commit_unresolvable 0` |
| `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` | exit 0; 20 `W04`; no `E##` |
| `git ls-tree -z <rev> verifiers/` | 58 `.py`/`.sh` blobs at base; 60 after the two counters |
| `wc -lc SKILL.md` (live) | 590 lines |
| `git status --porcelain` | ` M SKILL.md`, ` M corpus/SOURCES.md`, `?? .ufo/waves/round-74/snapshots/`, `?? corpus/knowledge/spec-skill-creation-craft-round74.md` |

**Not observed / not verified here:** the C1 counter's own page-unique-token, fetch-log and
9-cell-projection behaviour on data worlds (wave-2's job); the C2 counter's score on the r74 entry;
whether the tsukuroi classification is the reviewers' judgement (wave-2's job, ≥ 10 lanes per E1.2).

**Environment note:** `/tmp` was at 100 % (245 MB free) from other lanes' scratch during this seat's
run — `check_tip_battery.py` failed `exit 2` with `cannot create directory at '.ufo/round-45/evidence/x2':
No space left on device`. Runs above were re-done with `TMPDIR=/home/vgpnk/.scratch/k74conn`, which
has 567 GB free. Other seats should do the same; my scratch was deleted before returning.

**Lane-mutation statement:** this seat wrote no lane file. Scratch under
`/home/vgpnk/.scratch/k74conn/` (deleted on return); two throwaway clones under the same scratch
root; no fleet-repo, sibling-lane, `shokuknow` or lane-Git-index write; no `jj` mutation; no network
fetch.
