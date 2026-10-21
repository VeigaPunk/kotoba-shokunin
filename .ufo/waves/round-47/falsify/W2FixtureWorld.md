verdict: PARTIAL — the surfaces-fixture diff is exactly the claimed 5→9 opencode swap (byte-verified as the round-14 row set), and every fixture arm still fires for the reason its comment states; but round 47 leaves a **stale round-18 v2.0.26 provenance comment** in the four updated `baseline-*.json` fixtures, and the **nine new opencode rows have zero kind-laundering fixture coverage** — a joint baseline+census re-kind to `doc` on any of them passes all 7 checks (exit 0).

Lane: `KotobaR47-2.W2FixtureWorld-2` (reviewer leaf). Target: `verifiers/fixtures/surfaces/baseline-*.json` + `inventory-*.md` at `7ad7fadfc09354b74fb66605dfb0c1182c115a2f` (BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`).

Scratch clone (canonical layout, detached at 7ad7fad, all mutations confined there):
`/fast/scratch/kotoba-r47/w2/KotobaR47-2.W2FixtureWorld-2/kotoba-shokunin` (+ `base-clone` detached at c61a973).
Nothing under `/home/vgpnk/Projects/shokunin/kotoba-shokunin` was modified except this report + the `W2FixtureWorld.*` artifacts. No git/jj command was run in the lane repo. No subagents. No tools installed (nothing needed beyond python3 + git already present).

---

## F-1 (HIGH, round-47-introduced, calibration) — the four updated `baseline-*.json` fixtures carry a provenance comment that round 47 falsified

`verifiers/fixtures/surfaces/baseline-clean.json:2`, `baseline-excluded-noreason.json:2`, `baseline-rekind-doc.json:2`, `baseline-rekind-partial.json:2` all still end with the sentence:

> "Round 18: opencode half re-derived for the v2.0.26 rule set (OC-1..OC-6 over ConfigInstructionPlugin/ReadTool/API anchors)."

That sentence was **true at BASE** (the fixture's opencode half was the v2.0.26 set: `project/AGENTS.md`, `config/AGENTS.md`, `read-hook/AGENTS.md`, `api-entries/instructions`, `config/instructions`). After round 47 rewrote the file's opencode half to the round-14 lineage (9 rows, `instructions/*`, `claude-home/CLAUDE.md`, `config/instructions-remote`, `read-hook/instructions`, `instruction-context/AGENTS.md`), the sentence describes anchors the file no longer uses and that the new rule set **actively rejects** — the v2.0.26 anchors are exactly the ones `fixtures/surfaces/strings-opencode-v2.0.26.txt` must FAIL against (`verifiers/verify_surfaces.py:354-372`, the GENERATION NOTE lists `ConfigInstructionPlugin`, `ReadTool.Plugin`, `SessionInstructions`, `session.instructions.entry.put`, `j5(r.config,…)`, `InstructionDiscovery` as the **retired** v2.0.26 anchors; each of those six tokens occurs exactly once in the verifier, and only inside that prose note — none is a live anchor).

Repro (grep of the live tokens in the verifier at 7ad7fad):

```
$ for t in ConfigInstructionPlugin SessionInstructions InstructionDiscovery \
           "session.instructions.entry.put" "j5(r.config" "ReadTool.Plugin"; do
    printf "%-32s %s\n" "$t" "$(grep -c -- "$t" verifiers/verify_surfaces.py)"; done
ConfigInstructionPlugin          1
SessionInstructions              1
InstructionDiscovery             1
session.instructions.entry.put  1
j5(r.config                      1
ReadTool.Plugin                  1
```
(exit 0)

Why this is a round-47 defect and not a pre-existing nit: the same commit **did** write a correct provenance comment for the new fixture — `baseline-18.12.5.json:2` reads *"Fixture baseline for strings-omp-18.12.5.txt (round 47, C1)…"*. So the omission on the four opencode-side fixtures is an inconsistency inside one commit, and the stale sentence is a self-contradicting provenance claim in a file whose whole purpose is to be the provenance anchor for the fixture set. No machine check reads `$comment`, so it is a documentation-accuracy defect, not a gate defect — but C3's calibration axis is exactly "the recorded provenance matches what was measured", and here it does not.

Suggested fix (one sentence appended to the four `$comment`s): *"Round 47 (2026-10-21): opencode half re-derived for npm opencode-ai 1.19.3 (sha 179ca421…), the round-14 loader lineage — the 9 round-13/round-14 ids (instructions/AGENTS.md, instructions/CLAUDE.md, instructions/CONTEXT.md, config/AGENTS.md, claude-home/CLAUDE.md, config/instructions, config/instructions-remote, read-hook/instructions, instruction-context/AGENTS.md); the v2.0.26 rule set survives only as the must-fail fixture strings-opencode-v2.0.26.txt."*

---

## F-2 (HIGH, coverage gap round 47 walked into) — the nine new opencode rows have no kind-laundering fixture arm, and a joint baseline+census re-kind to `doc` passes all 7 checks (exit 0)

The round-28 kind-laundering arm lives in `check_no_uncovered_class` (`verifiers/verify_surfaces.py:643-652`):

```
laundered = sorted(cid for cid in found
                   if cid in by_id
                   and by_id[cid]["context_kind"] != "loader-group")
```

`found` is built **only** from the CALL_RE registration-shape extractor (`verifiers/verify_surfaces.py:638`, `found |= {"%s:%s/%s" % (harness, g, f) for g, f in pairs}`). That extractor sees `.md` registration calls; opencode's loaders are minified JS shapes handled by the separate `extract_opencode_classes()` rule set, so **no opencode class id ever enters `found`** and the laundering arm can never reach them. `check_opencode_extract` compares **ids only**, not kinds, so a re-kind leaves it PASS too; and `check_literal_present` *skips* non-`LOADER_KINDS` rows, so a `doc` row is dropped from literal verification as well. The only backstop left is `check_kind_parity` — which compares the census kind cell to the baseline kind cell, and therefore passes when **both** are re-kinded together.

Counterexample — re-kind a round-47 opencode row to `doc` in the baseline fixture *and* in the census fixture:

```
$ python3 - <<'EOF'
import json
b=json.load(open("mutwork/../kotoba-shokunin/verifiers/fixtures/surfaces/baseline-clean.json"))
for e in b["classes"]:
    if e["class_id"]=="opencode:instructions/AGENTS.md": e["context_kind"]="doc"
json.dump(b,open("mutwork/m7-base.json","w"),indent=2)
EOF
# census side: `opencode:instructions/AGENTS.md` row kind cell loader-literal -> doc
$ python3 kotoba-shokunin/verifiers/verify_surfaces.py --repo kotoba-shokunin/verifiers/fixtures/surfaces \
    --omp-strings kotoba-shokunin/verifiers/fixtures/surfaces/strings-omp-clean.txt \
    --opencode-strings kotoba-shokunin/verifiers/fixtures/surfaces/strings-opencode-clean.txt \
    --baseline mutwork/m7-base.json --inventory mutwork/m7.md
PASS surfaces.literal_present: 11 loader-kind entries verified against the dumps
PASS surfaces.no_uncovered_class: all 2 extracted loader class(es) declared
PASS surfaces.opencode_extract: opencode extraction 9/9 declared class(es) from 7/7 rules (OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6)
PASS surfaces.table_parity: inventory id set == baseline id set (12 ids)
PASS surfaces.literal_parity: 12 inventory row literal(s) match the baseline per id
PASS surfaces.kind_parity: 12 inventory row kind(s) match the baseline per id
PASS surfaces.excluded_reason: 1 excluded entry, all reasoned and listed in the inventory
EXIT=0
```

**Exit 0 — seven of seven green** with a round-47 opencode class silently re-classified from `loader-literal` to `doc` (i.e. "this is documentation, not a loader"). The same escape exists for the fixture's third omp row, `omp:cursor/rules` (`loader-literal`, not `.md`-suffixed, hence never in `found`): re-kinding it to `doc` in baseline+census also gives exit 0 (M8 in `W2FixtureWorld.muts-head.json`).

**Classification — pre-existing, not a round-47 regression.** The identical mutation at BASE gives exit 0 as well (BASE opencode row `opencode:project/AGENTS.md` and BASE `omp:cursor/rules`):

```
BASE joint rekind opencode:project/AGENTS.md       -> exit=0 fails=[]
BASE joint rekind omp:cursor/rules                 -> exit=0 fails=[]
```

**Why it is nonetheless a round-47 finding:** round 47 *replaced* the fixture's opencode half (5 rows) with 9 rows and the *live* baseline's opencode half likewise (5 → 9), but the rekind fixture family — `verifiers/fixtures/surfaces/baseline-rekind-doc.json`, `baseline-rekind-partial.json`, `inventory-rekind-doc.md`, `inventory-rekind-partial.md`, exercised at `verifiers/verify_surfaces.py:909-925` — was **not** extended to cover any of the nine new rows. Coverage of kind laundering over the fixture baseline is therefore **2 of 12 rows** (`omp:gemini/GEMINI.md`, `omp:claude-md/CLAUDE.md`, the only `loader-group` rows); the other 10 rows (1 omp `loader-literal` + **all nine new opencode rows**) are un-covered escapes. Round 47 is the round that made those nine rows the live census, so it is the round in which the gap became load-bearing.

Minimal fix, two options, both cheap: (a) extend the laundering arm to opencode ids by unioning `extract_opencode_classes()`'s derived ids into `found` before the `laundered` computation — the opencode ids *are* machine-derived from the dump, exactly like the omp ones; or (b) add a self-test arm that re-kinds one round-47 opencode row to `doc` in baseline+census and asserts exit 1. Option (a) also closes the `omp:cursor/rules` hole only if the loader-literal omp ids are unioned too, so (b) is the cheap, honest minimum.

---

## F-3 (MEDIUM, calibration) — `surfaces.kind_parity` is the only one of the seven checks with **no** fixture arm, and round 47 silently turned the orphaned fixture into a clean single-cause arm without adopting it

`CHECK_IDS` (`verifiers/verify_surfaces.py:175-183`) has seven checks; the self-test (`verifiers/verify_surfaces.py:834-1105`) exercises six. `surfaces.kind_parity` has **zero** arms — its only fixture, `verifiers/fixtures/surfaces/inventory-kind-drift.md`, has had **0 references** in `verifiers/` since round 14 (independently reported in `.ufo/round-22/scouts/P3.md:196-207`, `.ufo/round-23/scouts/G6.md:41`, `.ufo/round-24/scouts/S4.md:161-168`, `.ufo/round-26/scouts/S7.md:19-20`). Round 47 did not touch that file (`git diff --name-status c61a973 7ad7fad -- verifiers/fixtures/surfaces/` lists 14 M/A/D fixture files; `inventory-kind-drift.md` is **not** among them).

The interesting part is what round 47 did to that orphan **by accident**. `inventory-kind-drift.md` was written at round 14 (`29c17be`) with the round-14 opencode rows, and at BASE the fixture baseline carried the *round-18 v2.0.26* rows — so the orphan was doubly broken (2 failing checks). Round 47 restored the round-14 row set, so the orphan is now a **single-cause** kind-drift arm:

```
ARM kind-drift-orphan (HEAD): exit=1 FAILS=['surfaces.kind_parity']
      surfaces.kind_parity -> 1 census row kind(s) disagree with the baseline: omp:gemini/GEMINI.md (line 9: census kind 'loader-literal' != baseline context_kind 'loader-group')
ARM kind-drift-orphan (BASE): exit=1 FAILS=['surfaces.table_parity', 'surfaces.kind_parity']
      surfaces.table_parity -> missing row(s) for baseline id(s): opencode:api-entries/instructions, opencode:project/AGENTS.md, opencode:read-hook/AGENTS.md; extra row(s) not in baseline: opencode:claude-home/CLAUDE.md, opencode:config/instructions-remote, opencode:instruction-context/AGENTS.md, opencode:instructions/AGENTS.md, opencode:instructions/CLAUDE.md, opencode:instructions/CONTEXT.md, opencode:read-hook/instructions
```

i.e. a working, single-cause `kind_parity` fixture is sitting on disk and is still never opened by the self-test. This matters more after round 47 because `kind_parity` is the **only** check that catches F-2's single-sided variant (baseline re-kinded, census not): mutation M9 (baseline-only re-kind of `opencode:instructions/AGENTS.md`) → exit 1, `FAIL surfaces.kind_parity`. Adopt the fixture as an arm (one `run(inventory=fx + "/inventory-kind-drift.md")` plus a `rec("kind-drift: FAIL kind_parity", ...)`) and the seventh check gets coverage for free.

---

## F-4 (LOW, pre-existing, honest) — the census `verdict` column is checked by nothing, and the fixture's `verdict` column does not exist in the live census layout

The fixture census uses a 5-column header `| class_id | literal | kind | verdict | evidence |` (`verifiers/fixtures/surfaces/inventory-clean.md:7`), but the live census `corpus/knowledge/instruction-surface-census-round13.md` uses `| class_id | literal | kind | governed by | evidence |` in §B (`:247`) and a 4-column `| class_id | literal | kind | reason … |` in §C (`:261-262`). `inventory_rows()` reads `cells[0]=id`, `cells[1]=literal`, `cells[2]=kind` and never looks at `cells[3]`, so the fixture's `verdict` cell is decorative and no check compares a census verdict to the baseline verdict.

Counterexample (M5): flipping the fixture census verdict cell of `opencode:config/instructions` from `governed` to `excluded` — the exact cell round 47 re-verdicted from `excluded` to `governed` in both the baseline and the census — yields **exit 0, zero failing checks**:

```
ARM/M5 verdict-cell drift   exit=0 fails=none
```

Pre-existing (the fixture header is byte-identical at BASE), but it is the reason the `excluded_reason` check can only ever be driven from the *baseline* side. It also means the round-47 re-verdict of `opencode:config/instructions` is unverified in the census column: the fixture's row says `governed` and the baseline says `governed`, but nothing would have caught a mismatch.

---

## What I checked and it HOLDS (the assignment's core claims)

### H-1 The diff is *exactly* the 5 v2.0.26 opencode rows → 9 round-14-lineage rows, and nothing else

`git diff --name-status c61a973 7ad7fad -- verifiers/fixtures/surfaces/` → 27 files; the 14 `baseline-*.json` / `inventory-*.md` files in my scope are:

```
A  verifiers/fixtures/surfaces/baseline-18.12.5.json
M  verifiers/fixtures/surfaces/baseline-clean.json
M  verifiers/fixtures/surfaces/baseline-excluded-noreason.json
M  verifiers/fixtures/surfaces/baseline-rekind-doc.json
M  verifiers/fixtures/surfaces/baseline-rekind-partial.json
M  verifiers/fixtures/surfaces/inventory-clean.md
M  verifiers/fixtures/surfaces/inventory-extra-row.md
M  verifiers/fixtures/surfaces/inventory-id-not-first.md
M  verifiers/fixtures/surfaces/inventory-literal-drift.md
M  verifiers/fixtures/surfaces/inventory-missing-excluded-row.md
M  verifiers/fixtures/surfaces/inventory-missing-row.md
M  verifiers/fixtures/surfaces/inventory-no-literal-cell.md
M  verifiers/fixtures/surfaces/inventory-rekind-doc.md
M  verifiers/fixtures/surfaces/inventory-rekind-partial.md
```
(`inventory-empty.md`, `inventory-kind-drift.md`, `baseline-empty.json`, `baseline-oc-empty.json` are **untouched** — verified.)

Row-level proof that the change is confined to the opencode block:

* `baseline-clean.json` omp rows (`:5`, `:12`, `:20`) are byte-identical OLD↔NEW (`omp:gemini/GEMINI.md` loader-group/governed; `omp:claude-md/CLAUDE.md` loader-group/excluded + reason; `omp:cursor/rules` loader-literal/governed). The opencode block went from 5 rows (BASE `baseline-clean.json:27 project/AGENTS.md`, `:34 config/AGENTS.md`, `:41 read-hook/AGENTS.md`, `:48 api-entries/instructions`, `:55 config/instructions` excluded) to 9 rows at HEAD `baseline-clean.json:27,34,41,48,55,62,69,76,83`.
* `git diff --check c61a973 7ad7fad -- verifiers/fixtures/surfaces/` → exit 0 (no whitespace damage).
* The four mutation-bearing fixtures still differ from `baseline-clean.json` by **exactly one field each**, unchanged by round 47:
  * `baseline-excluded-noreason.json` vs `baseline-clean.json` → only `"reason": ""` on `omp:claude-md/CLAUDE.md`.
  * `baseline-rekind-doc.json` → only `context_kind: loader-group → doc` on `omp:gemini/GEMINI.md` **and** `omp:claude-md/CLAUDE.md`.
  * `baseline-rekind-partial.json` → only `context_kind: loader-group → doc` on `omp:claude-md/CLAUDE.md`.
  * `inventory-*.md` → each differs from `inventory-clean.md` by exactly the one mutation (literal `WRONG.md`; id moved to cell 2; row deleted; row added; literal cell emptied; excluded row deleted; kind cell `doc`).
* The 9 new opencode rows are **byte-identical to the round-14 row set** (commit `29c17be`, `verifiers/surfaces-baseline.json`) and to the HEAD live baseline:

```
round-14 opencode rows == HEAD fixture rows : True
round-14 opencode rows == HEAD live rows    : True
counts r14=9 fx=9 live=9
```
(key = `class_id, harness, literal, context_kind, verdict`) — so "9 round-14-lineage rows" is literally true, and the live `verifiers/surfaces-baseline.json` swap is the same 5→9 with the identical keys.
* The fixture's 9 rows also match the live census §B′ rows verbatim (`corpus/knowledge/instruction-surface-census-round13.md:249-257`: literal and kind cell agree for all nine), and `baseline-clean.json`'s opencode block is an exact subset of the live baseline's opencode block (no field mismatch on any of the 9).
* `baseline-18.12.5.json`: its `$comment` claims the 8 omp loader-group rows are "copied verbatim from verifiers/surfaces-baseline.json" — **verified true**, field-for-field (class_id, harness, literal, context_kind, verdict) for all 8.

### H-2 Every fixture arm still fires for the reason its comment states

Full per-check status for every fixture-driven arm (`W2FixtureWorld.arms-head.json`; harness `W2FixtureWorld.arms.py`), HEAD vs BASE:

| arm | fixture(s) | HEAD exit / failing checks | BASE exit / failing checks | comment at `verify_surfaces.py` | reason honored? |
|---|---|---|---|---|---|
| clean | `baseline-clean.json` + `inventory-clean.md` | 0 / none | 0 / none | :859-861 | ✅ |
| literal-drift | `inventory-literal-drift.md` | 1 / `literal_parity` only | 1 / `literal_parity` only | :974-978 | ✅ |
| id-not-first | `inventory-id-not-first.md` | 1 / `literal_parity` **+ `kind_parity`** | 1 / `literal_parity` **+ `kind_parity`** | :992-998 | ✅ for the named reason (see N-1) |
| missing-row | `inventory-missing-row.md` | 1 / `table_parity` only | 1 / `table_parity` only | :958-962 | ✅ |
| extra-row | `inventory-extra-row.md` | 1 / `table_parity` only | 1 / `table_parity` only | :966-970 | ✅ |
| no-literal-cell | `inventory-no-literal-cell.md` | 1 / `literal_parity` only | 1 / `literal_parity` only | :982-988 | ✅ |
| missing-excluded-row | `inventory-missing-excluded-row.md` | 1 / `table_parity` **+ `excluded_reason`** | 1 / `table_parity` **+ `excluded_reason`** | :1010-1014 | ✅ for the named reason (see N-2) |
| rekind-doc | `baseline-rekind-doc.json` + `inventory-rekind-doc.md` | 1 / `no_uncovered_class` only | 1 / `no_uncovered_class` only | :911-918 | ✅ |
| rekind-partial | `baseline-rekind-partial.json` + `inventory-rekind-partial.md` | 1 / `no_uncovered_class` only | 1 / `no_uncovered_class` only | :921-925 | ✅ |
| excluded-noreason | `baseline-excluded-noreason.json` | 1 / `excluded_reason` only | 1 / `excluded_reason` only | :1002-1006 | ✅ |
| kind-drift (orphan) | `inventory-kind-drift.md` | 1 / `kind_parity` only | 1 / `table_parity`+`kind_parity` | not referenced | see F-3 |

No arm's failure profile changed between BASE and HEAD. The *only* profile change is the orphan (F-3), and it changed for the better.

Key output strings, re-derived (HEAD):
* literal-drift → `FAIL surfaces.literal_parity: 1 census row literal(s) disagree with the baseline: omp:gemini/GEMINI.md (line 9: census literal 'WRONG.md' != baseline literal 'GEMINI.md')`
* id-not-first → `FAIL surfaces.literal_parity: 12 census row literal(s) disagree with the baseline: line 9 carries class id(s) omp:gemini/GEMINI.md outside the first cell — the literal comparison cannot be anchored` (and `PASS surfaces.table_parity`, as the arm asserts at :997)
* missing-row → `FAIL surfaces.table_parity: missing row(s) for baseline id(s): omp:gemini/GEMINI.md`
* extra-row → `FAIL surfaces.table_parity: extra row(s) not in baseline: omp:github/prompts`
* no-literal-cell → `FAIL surfaces.literal_parity: 2 census row literal(s) disagree with the baseline: omp:gemini/GEMINI.md (line 9: row has no literal cell — expected 'GEMINI.md'); omp:cursor/rules (line 11: row has no literal cell — expected 'rules')`
* missing-excluded-row → `FAIL surfaces.excluded_reason: excluded id(s) not shown in inventory: omp:claude-md/CLAUDE.md`
* rekind-doc → `FAIL surfaces.no_uncovered_class: 2 extracted loader class(es) re-kinded in the baseline — kind reassignment is not a bypass: omp:claude-md/CLAUDE.md->doc, omp:gemini/GEMINI.md->doc`
* rekind-partial → `FAIL surfaces.no_uncovered_class: 1 extracted loader class(es) re-kinded in the baseline — kind reassignment is not a bypass: omp:claude-md/CLAUDE.md->doc` (and `omp:gemini/GEMINI.md->doc` absent, `PASS surfaces.literal_present` — exactly as the arm asserts at :924)
* excluded-noreason → `FAIL surfaces.excluded_reason: excluded without reason: omp:claude-md/CLAUDE.md`

### H-3 The new opencode rows are individually covered by the checks that own them (mutation tests, M1–M4, M9, M11)

`W2FixtureWorld.muts-head.json` (harness `W2FixtureWorld.muts.py`) — each mutation applied to a copy of the clean fixture:

| # | mutation | expected | measured |
|---|---|---|---|
| M1 | census literal of the new `opencode:config/instructions-remote` → `http://` | `literal_parity` FAIL | ✅ `FAIL surfaces.literal_parity: … opencode:config/instructions-remote (line 18: census literal 'http://' != baseline literal 'https://')` — exit 1, that check only |
| M2 | census kind of the new `opencode:read-hook/instructions` → `loader-config` | `kind_parity` FAIL | ✅ `FAIL surfaces.kind_parity: … opencode:read-hook/instructions (line 19: census kind 'loader-config' != baseline context_kind 'loader-literal')` — exit 1, that check only |
| M3 | delete the new `opencode:instructions/CONTEXT.md` census row | `table_parity` FAIL | ✅ `missing row(s) for baseline id(s): opencode:instructions/CONTEXT.md` — exit 1, that check only |
| M4 | inject a census row for an undeclared new id | `table_parity` FAIL | ✅ `extra row(s) not in baseline: opencode:instructions/GUIDE.md` — exit 1, that check only |
| M6 | move **one** new opencode id out of the first cell | `literal_parity` FAIL (and `kind_parity` must stay green) | ✅ `line 14 carries class id(s) opencode:instructions/CONTEXT.md outside the first cell` — exit 1, `literal_parity` only, `kind_parity` PASS |
| M9 | baseline-only re-kind of a new opencode row | `kind_parity` FAIL | ✅ `census kind 'loader-literal' != baseline context_kind 'doc'` — exit 1, that check only |
| M11 | backtick the `<system-reminder>` literal cell | no change (verifier strips backticks; the live census writes the cell raw, so raw is canonical) | ✅ exit 0, no FAIL |
| M10c | add a *new* excluded id to the baseline, absent from the census | `excluded_reason` FAIL naming the new id | ✅ `FAIL surfaces.excluded_reason: excluded id(s) not shown in inventory: opencode:probe/excluded` (plus `literal_present`/`opencode_extract`/`table_parity` — correct, the id is fake) |
| **M7** | **joint baseline+census re-kind of a new opencode row to `doc`** | `no_uncovered_class` FAIL | ❌ **MISS — exit 0, all 7 PASS** (F-2) |
| **M8** | **joint baseline+census re-kind of `omp:cursor/rules` to `doc`** | `no_uncovered_class` FAIL | ❌ **MISS — exit 0, all 7 PASS** (F-2) |
| **M5** | **census verdict cell drift** | — | ❌ **no check fires, exit 0** (F-4) |

### H-4 The landed claim reproduces end-to-end

```
$ cd /fast/scratch/kotoba-r47/w2/KotobaR47-2.W2FixtureWorld-2/kotoba-shokunin
$ python3 -B verifiers/verify_surfaces.py --self-test
0 failure(s) over 99 assertions        # exit 0   (BASE: 0 over 87, exit 0)
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
$ python3 -B verifiers/verify_surfaces.py --json        # default resolution
pass 7 fail 0 exit 0
  PASS surfaces.literal_present  42 loader-kind entries verified against the dumps
  PASS surfaces.no_uncovered_class all 8 extracted loader class(es) declared
  PASS surfaces.opencode_extract opencode extraction 9/9 declared class(es) from 7/7 rules (OC-1..OC-6)
  PASS surfaces.table_parity     inventory id set == baseline id set (42 ids)
  PASS surfaces.literal_parity   42 inventory row literal(s) match the baseline per id
  PASS surfaces.kind_parity      42 inventory row kind(s) match the baseline per id
  PASS surfaces.excluded_reason  8 excluded entries, all reasoned and listed in the inventory
$ python3 -B verifiers/check_substrate_pins.py
PASS omp_binary_sha256: fdbc8136…
PASS omp_binary_mtime: delta 0 ns (tolerance 0 ns)
PASS opencode_binary_sha256: 179ca421…
OK 3/3 pins hold                       # exit 0
```
The default-resolution run and the frozen-snapshot run (`--omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings --opencode-strings /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings`) agree: **7/7 PASS, exit 0**. Artifact: `W2FixtureWorld.surfaces-default-head.json`.

The live census is self-consistent with the live baseline: the stale round-18 `opencode:config/instructions` "no loader consumer proven" row now sits in `## Superseded class rows and the round-47 opencode ledger (not inventory)` (`corpus/knowledge/instruction-surface-census-round13.md:287`), i.e. **outside** the `## Class inventory` section (`:64-286`), so the verifier's `inventory_section` (`verifiers/verify_surfaces.py:507-526`, stops at the next `^## `) correctly ignores it. `table_parity` reports 42 ids == 42 baseline ids, and `literal_parity`/`kind_parity` each report 42 rows — no duplicate-id inflation.

---

## N-1 / N-2 (LOW, pre-existing) — two arms fail for a second, unnamed reason

Both are unchanged from BASE and neither breaks an assertion, but the verifier's comments name only one cause:

* **N-1** `inventory-id-not-first.md` also FAILs `surfaces.kind_parity` ("0 inventory rows carry a baseline class id — vacuous kind parity is not a pass"), because moving every id out of the first cell leaves `kind_parity`'s `checked` counter at 0. The comment at `verify_surfaces.py:991` says only "declared id carried outside the first cell -> exit 1, literal_parity"; the arm asserts `literal_parity` FAIL and `table_parity` PASS but says nothing about `kind_parity`. Note this is *not* a blank check — the single-row variant (M6) keeps `kind_parity` green, so the difference is "all ids moved" vs "one id moved", which is worth one clause in the comment.
* **N-2** `inventory-missing-excluded-row.md` also FAILs `surfaces.table_parity` (the removed id is a baseline id too). The comment at `:1009` names only `excluded_reason`. Unavoidable given the fixture's design (removing an inventory row always breaks id parity).

Neither is a round-47 regression; both are recorded for the calibration axis.

---

## What I did NOT check

* The `strings-*` fixtures (`strings-opencode-clean.txt`, `strings-opencode-drop-oc*.txt`, `strings-opencode-extra.txt`, `strings-opencode-planted-name.txt`, `strings-opencode-v2.0.26.txt`, `strings-omp-18.12.5.txt`, `strings-omp-*.txt`) beyond using them as inputs to the arms: I did **not** verify that their lines are exact byte substrings of the frozen dumps, nor that the drop-oc1/2/3a/3b/4/5/6 matrices still isolate their intended anchor (other lanes own that). `strings-opencode-drop-oc3.txt` was deleted and split into `-oc3a`/`-oc3b` in this round; I only observed that the two new arms exist and fire.
* The live corpus census text beyond the opencode rows and the section boundaries (other lanes own the census); in particular I did not re-derive the census's own §B′ anchor counts against the 1.19.3 dump.
* `verifiers/verify_skill_checklist.py` (C2, `trigger.no_xml_tag`), `verifiers/verify_corpus_integrity.py`, `verifiers/verify_corpus_independent.py`, `verifiers/fault_injection_corpus.sh`, `SKILL.md`, `LOG.md`, `SCORECARD.md`, `PROVINCE.md`, `plans/round-47.md` — all outside this lane's target.
* The `check_substrate_pins.py` default-resolution mechanics beyond running it once (exit 0, 3/3) — I did not re-derive the sha256 of the resolved opencode ELF myself (another lane owns the re-pin).
* `omp --version` / live host state; I used only the frozen snapshot strings dumps plus the committed fixtures.
* Windows/other-platform behaviour of `dump_via_strings`; only the Linux default path was exercised.
* The `.ufo/waves/round-47/after/SUMMARY.md` numbers other than the surfaces line; I reproduced the surfaces and pins gates myself.

---

## Artifacts (this lane, `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-47/falsify/`)

| file | what |
|---|---|
| `W2FixtureWorld.md` | this report |
| `W2FixtureWorld.arms.py` | per-arm harness (runs every fixture arm with `--json`, prints per-check status) |
| `W2FixtureWorld.arms-head.json` | HEAD arm results (exit code, per-check PASS/FAIL, full detail) |
| `W2FixtureWorld.arms-base.json` | same arms at BASE c61a973 (the comparison table above) |
| `W2FixtureWorld.muts.py` | 11 mutation tests (M1-M11) against copies of the clean fixtures |
| `W2FixtureWorld.muts-head.json` | mutation results with measured vs expected failing checks |
| `W2FixtureWorld.selftest-head.txt` / `.selftest-base.txt` | `--self-test` transcripts (99 / 87 assertions, 0 failures) |
| `W2FixtureWorld.surfaces-default-head.json` | default-resolution surfaces run, 7/7 PASS exit 0 |
