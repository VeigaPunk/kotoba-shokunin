verdict: `corpus/README.md` takes the four rows cleanly after BASE line 62 (three new files + the round-46 spot-check file that is unindexed at BASE), and the tested patch makes both corpus instruments exit 0 — but the row edit alone leaves `corpus.index.tracked_files` DRIFT until `verifiers/corpus-baseline.json` `expect` 58 → post-landing count is refreshed, and two present-tense README claims were already false at BASE (Frontier `omp 18.12.3 … surfaces 5/7 … pins 1/3` at `corpus/README.md:74`; `29 heads` at `corpus/README.md:85`, measured 28).

# ScoutReadmeIndex — corpus/README.md index map, insertion points, stale counts

BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (`git rev-parse HEAD`, exit 0). All production reads were at BASE; all writing/experiments were in `/fast/scratch/kotoba-r47/ScoutReadmeIndex/`. No production file was modified. No tools were installed or upgraded (none needed).

Artifacts (both under `.ufo/waves/round-47/build/`):

- `ScoutReadmeIndex.md` — this report.
- `ScoutReadmeIndex.patch` — README edits + the one baseline `expect` line, 72 lines, `git diff <BASE>`; `git apply --check` and `git apply` both exit 0 on a fresh BASE clone, and the resulting tree passes both corpus instruments (evidence in §7).

## 1. Structure of `corpus/README.md` at BASE

| Region | Lines | Shape and gate relevance |
|---|---|---|
| H1 + domain | 1–3 | no table |
| `## Coverage map` | 5 | heading starts the only section the integrity census harvests |
| header / separator | 7 / 8 | `| Area | File | Basis |` |
| coverage rows | 9–62 (54 rows) | column 2 backticked tokens are the index claims (76 tokens at BASE) |
| blank | 63 | insertion seam for round-47 rows |
| `## Frontier` | 64 | ends the coverage-map section (`verify_corpus_integrity.py:355-360` only harvests inside it) |
| Frontier intro | 66 | says "appended round 46" |
| Frontier header / sep / rows | 68 / 69 / 70–75 (6 rows) | 3-column table; **not** harvested by the integrity gate |
| `## Known gaps` | 77 | bullet list, 79–116; **not** harvested |

Row format: one physical line, `| Area | \`corpus-relative path\` [ + \`more\`] | basis |`, exactly four `|` characters (no pipes in cell text unless escaped `\|`). All four rows I propose have 4 pipes (checked with `gsub(/\|/,"|")`, one row per line).

Gate mechanics that constrain the text (read from `verifiers/verify_corpus_integrity.py:313-446`; the independent witness at `verifiers/verify_corpus_independent.py:254-356` reads the same column):

- Only column 2 of rows inside `## Coverage map` is harvested (`file_column_tokens`), every backticked token, **corpus-relative** (`lessons/round-47.md`, not `corpus/lessons/round-47.md`).
- Fenced lines are opaque (`fenced_lines`); a row inside a fence is an example, not a promise.
- Every non-glob token must exist on disk relative to `corpus/` (`missing_paths`), and every corpus-internal token must match `git ls-files corpus/` (`stale_patterns`); no-match or absent file each DRIFT.
- `corpus.index.unindexed` is the set difference `git ls-files corpus/` minus README.md minus covered tokens.
- `tracked_files`, `report_total`, `commit_total` are `equal`-mode baseline pins in `verifiers/corpus-baseline.json`; the rest are zero-mode.
- `commit \`x\`` is checked as a git commit (`<x>^{commit}`, 7–40 hex); a placeholder fires `commit_nonhash`. A report pointer `/home/vgpnk/Projects/shokunin/.ufo/reports/round-47/kotoba.md` fires `report_dead` until the file exists.

## 2. Insertion points (exact, at BASE)

1. **Coverage map — after line 62**, before the blank line 63. The four rows become new lines 63–66; positions 64–75 shift by +4. (If the integrator wants a different intra-round order, only the four lines move; nothing else depends on order.)
2. **Line 62** (round-46 row) — append a note inside the existing cell (no line added).
3. **Lines 39 and 40** (round-14 extraction row, round-13 census row) — append a note inside each existing cell (no line added).
4. **Line 58** (round-23 substrate-pin guard row) — append a note inside the existing cell (no line added).
5. **Line 66** — Frontier intro "appended round 46" → "appended rounds 46–47" (1:1 line swap).
6. **Line 74** — replace the stale `Loader-rule freshness` row (1:1 line swap).
7. **Line 85** — `29 heads` correction; the bullet grows from 1 line to 4 (+3 lines).
8. **`verifiers/corpus-baseline.json:13-15`** — `"expect": 58` → the landing count (62 in the tested configuration); append a `notes.round47_readme_index` entry (template in §6). This is required for C3's "0 DRIFT"; the row edit alone flips `unindexed` to 0 but leaves `tracked_files` DRIFT (`observed 59/62 vs expected 58`, §7).

Net effect: `corpus/README.md` 116 → 123 lines.

## 3. Row text — copy verbatim (4 lines, insert after BASE line 62)

```text
| Round-46 verifier spot-check (non-author) | `lessons/round-46-verifier-spotcheck.md` | integrator-written record of the post-landing non-author verification at `04192c252`: the LEARNING.md admit/reject sample — S003 (Anthropic skill structure) and S006 admitted, S011 kept tier C/rejected against S002's "Lenient validation: warn, load anyway", the reviewers re-opening S002/S003/S004/S011 and the open Agent Skills spec (the "cannot contain XML tags" rule recorded as vendor-specific) — plus the ADMITTED adjudication of the r46 WIP `36ab0d3` (depth improved, operability and calibration improved-bounded, consistency/coverage/freshness/adjacency unchanged; q.v. `lessons/round-46.md`); indexed in round 47, closing the "spot-check pending non-author" clause on the round-46 row |
| Round-47 lessons | `lessons/round-47.md` | LOG.md round-47 entries; artifacts: the substrate re-derive/re-pin (`knowledge/substrate-recensus-round47.md`), the `description` XML-tag rule as an executed checklist-instrument check (`knowledge/description-xml-tag-rule-round47.md`), and the pinned fail-closed erratum registry for the governance citation gate; `## Mistakes` carries each class with pointer, captured-by criterion and fix |
| Substrate recensus (round 47) | `knowledge/substrate-recensus-round47.md` + `../verifiers/verify_surfaces.py` + `../verifiers/check_substrate_pins.py` | C1 freshness: the omp 18.12.5 and opencode-npx 1.19.3 substrate re-derived from the shipped binaries rather than copied — every omp loader class either re-extracted or re-verdicted with its sweep, OC-1/OC-4/OC-6 re-verdicted against 1.19.3 — then re-pinned: `verify_surfaces.py` 7/7 exit 0 and `check_substrate_pins.py` 3/3 exit 0 at the default resolution |
| Description XML-tag rule (round 47) | `knowledge/description-xml-tag-rule-round47.md` + `../verifiers/verify_skill_checklist.py` + `../verifiers/fixtures/checklist/` | C2 operability: the portability-floor rule "`description` carries no XML tag" (S003, re-opened this round and recorded vendor-specific in `SOURCES.md`) becomes an executed fail-closed check — a planted-tag fixture fails, tag-free controls stay green, `--self-test` carries the discrimination — and `SKILL.md`'s own description loses its `<skills>` token; the round-46 Frontier debt closes |
```

Facts in row 1 were read from `corpus/lessons/round-46-verifier-spotcheck.md:5` (`04192c252`), `:12` (admit S003+S006), `:13` (reject S011), `:17` (ADMITTED, per-axis sentence). `04192c252` and `36ab0d3` both resolve as commits at BASE (`git cat-file -e <c>^{commit}` → exit 0 each); written without the word `commit` immediately before them, so they add **zero** `commit_total` counts — deliberate, because the round-47 landing commit does not exist yet and a `commit \`<placeholder>\`` would fire `commit_nonhash` (the round-11 debt class, `corpus/lessons/round-11.md`).

Caveats the integrator must check before landing these rows:

- The rows name `lessons/round-47.md`, `knowledge/substrate-recensus-round47.md`, `knowledge/description-xml-tag-rule-round47.md` exactly. If C1/C2 land under different names, rename in the rows; the gate does not fuzzy-match. A missing file = `stale_patterns` + `missing_paths` (proved, §7).
- Row 3 asserts `7/7` and `3/3` at the default resolution — the plan's after-target. Those are the instruments' fixed check counts, but the passes themselves are C1's to land; if the landed verdicts differ, edit the basis (the index gate will not catch the false claim; calibration will).
- Row 4 asserts the check lands in `verify_skill_checklist.py` with a planted-tag fixture under `verifiers/fixtures/checklist/`. No such check exists at BASE (`grep -rn errata verifiers/` exit 1; the checklist has 10 checks, §5), so this row must not land before C2.
- Any *additional* corpus file landed by C2/C3 (e.g. a third knowledge file for the erratum registry) needs its own row and changes the `tracked_files` count; the 62 in the patch assumes exactly the three new files.

## 4. In-place edits to existing rows (round-27 errata style)

The style at `corpus/README.md:15-16` is an inline bold `**round-27 note:** …` appended inside the cell, preserving the original claim. The same shape for round 47:

- **Line 62** — replace `spot-check pending non-author) |` with:
  `spot-check pending non-author); **round-47 note:** the pending clause is closed by \`lessons/round-46-verifier-spotcheck.md\`, indexed this round |`
- **Line 39** (round-14 OC rules) — append before the trailing ` |`:
  `; **round-47 note:** OC-1/OC-4/OC-6 match nothing in opencode 1.19.3 and are re-verdicted there (q.v. \`knowledge/substrate-recensus-round47.md\`)`
- **Line 40** (round-13 census) — append before the trailing ` |`:
  `; **round-47 note:** the omp sweep is re-derived against 18.12.5, and the class set with its counts lives in \`knowledge/substrate-recensus-round47.md\``
- **Line 58** (round-23 pin guard) — append before the trailing ` |`:
  `; **round-47 note:** re-pinned for the 18.12.5 / 1.19.3 substrate (q.v. \`knowledge/substrate-recensus-round47.md\`), \`OK 3/3 pins hold\` at the default resolution`
  (the round-23 text itself stays: "at landing: live exit 0 (`OK 3/3 pins hold`)" is historical and true; the note is what makes the present tense honest).
- **Line 66** — `appended round 46` → `appended rounds 46–47`.
- **Line 74** — replace the whole row:
  ```text
  | Substrate re-pin trigger | the 18.12.5 / 1.19.3 pins are current (round 47), but nothing re-derives the class inventory when a harness moves — the guard only hashes the binaries, so a moved loader fails after the fact, not at install time | a move-probe: point `../verifiers/verify_surfaces.py` at a scratch-root binary pair (`--omp-binary` / `--opencode-binary`) and record which classes sweep vs die before re-pinning |
  ```
  Rationale: the old row's whole content is exactly what round 47 closes (drift, the 5/7 and 1/3 numbers, and the unchecked tag rule), so keeping it as "Frontier" would re-state a solved item. The replacement keeps the residual that is still true: re-pinning is manual and there is no pre-install probe. Deleting the row instead is also defensible; either way do not leave the stale row.

## 5. Stale counts in present-tense README text

Measured at BASE unless noted.

| Site | Claim | State at BASE | Evidence |
|---|---|---|---|
| `corpus/README.md:74` | "omp 18.12.3 drift leaves surfaces 5/7 and pins 1/3; the frontmatter `description` XML-token rule is unchecked" | **stale on all four counts.** Substrate is omp 18.12.5 + opencode 1.19.3; default surfaces exit 2, explicit 4/7; pins 0/3 pass; tag rule still unchecked | `.ufo/waves/round-47/before/SUMMARY.md:5-9`; `check_substrate_pins.py --json` exit 2 `pass 0 / fail 3` (omp sha DRIFT, omp mtime DRIFT `delta_ns 140082506863270`, opencode `UNREADABLE`); `verify_surfaces.py --json` exit 2 `opencode binary not found`; with the frozen dumps, exit 1, 4 PASS / 3 FAIL |
| `corpus/README.md:85` | "`verifiers/checklist-command-vocabulary.json`, 29 heads" | **wrong; 28.** The file has 28 `commands` entries and 28 distinct heads, and has held 28 since round 15 — this is a counting error, not drift | `python3` count over `commands` → 28; `sha256sum` = `76d16a9c…e02b` = `git show 0089974:…` and `git show 0089974:… \| python3` → 28. The same "29" is in `corpus/knowledge/checklist-execution-round15.md:214` — **append-only, do not edit there**; correct the README and name the lesson's error |
| `corpus/README.md:62` | "spot-check pending non-author" | **closed at BASE** — the spot-check file is tracked (`git ls-files` lists it) and cites its landing at `04192c252` | `corpus/lessons/round-46-verifier-spotcheck.md:5`; `git log --oneline -1 -- corpus/lessons/round-46-verifier-spotcheck.md` → `c61a973 round-46 verifier spot-check …` |
| `corpus/README.md:58` | "at landing: live exit 0 (`OK 3/3 pins hold`, mtime `delta 0 ns`)" | true at round-23 landing, but the guard now exits 2 with 0/3 — a reader can mistake it for current state | `check_substrate_pins.py --json` exit 2; see note in §4 |
| `corpus/README.md:39-40` | OC-1…OC-6 two-way parity; omp "8 machine-extracted `.md` registrations" | round-13/14 scoped, but at 1.19.3 OC-1/OC-4/OC-6 match nothing and the omp dump yields 0 classes — needs the round-47 note, and the "8" must be re-stated in the recensus (I did not re-derive the class count; C1 owns it) | explicit surfaces run: `8 loader literal(s) not verifiable` (vacuity 0/8), `OC-1 / OC-4 / OC-6` produce nothing |
| `corpus/README.md:70` and `:79-80` | "33 of 41 boxes remain lane-attested", "8 executed / 0 delegated / 33 unexecuted" | **accurate at BASE** | live `verify_skill_checklist.py --json` exit 1; `checklist.box_map_complete` PASS detail "41 boxes mapped (8 executed, 0 delegated, 33 unexecuted)" |
| `corpus/README.md:15-16, :44-45, :112-116` | round-27 notes; historical check counts (9 checks, tenth check); 17-skill render cliff | dated/historical and already scoped; not re-measured this round — left alone | — |

Conditional counts if C2 changes the box map (do not apply blindly):

- New instrument check, not disposed to a box (the likely shape): README counts stay `41 / 8 / 33`; the checklist JSON goes 10 → 11 checks. No README edit.
- New check disposed to an existing box in `checklist-baseline.json`: `:79` "33 of the 41" → "32 of the 41", `:80` "8 executed / … / 33 unexecuted" → "9 executed / … / 32 unexecuted", `:70` "33 of 41" → "32 of 41".
- A new 42nd box: `41` → `42`, executed +1, unexecuted `42 − executed`.
Verify with the live checklist JSON after C2; the box-map check prints the numbers.

Adjacent, not README (flagging so the C2 owner does not miss them): `SKILL.md:151` says "This file's own description still carries `<skills>`; the repair is planned" — false once C2 lands; `SKILL.md:185` says "Eight of the fifteen boxes" while the file has 41 (`SKILL.md:126`, baseline detail) — stale and inside C2's file.

## 6. Baseline refresh (required for 0 DRIFT)

At BASE `verify_corpus_integrity.py --json` exits 1 with exactly two DRIFTs: `corpus.index.tracked_files` `observed 59, expected 58` and `corpus.index.unindexed` `observed 1` (`corpus/lessons/round-46-verifier-spotcheck.md`). The row set in §3 drives both to pass, but `tracked_files` is `equal`-mode, so:

1. After the three new files are tracked and indexed, set `verifiers/corpus-baseline.json` `checks["corpus.index.tracked_files"].expect` to `git ls-files corpus/ | wc -l` (62 in the tested configuration: 59 + `round-47.md` + the two knowledge files).
2. Append a `notes.round47_readme_index` entry in the file's existing per-round note style (last is `round46_landing`). Template, with the numbers I measured for the README rows alone:
   `"round47_readme_index": "Measured with python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json against a staged clone of c61a973b. tracked_files 59 -> 62: corpus/lessons/round-47.md, corpus/knowledge/substrate-recensus-round47.md and corpus/knowledge/description-xml-tag-rule-round47.md, each indexed in corpus/README.md (the round-46-verifier-spotcheck row closes the 59-vs-58 unindexed DRIFT first); index_tokens 76 -> 84. report_total 40 and commit_total 29 unchanged only because the four README rows add no report pointer and no commit citation — re-observe after the corpus docs are authored, since any pointer they carry moves report_total. All zero-defect expectations observed zero; both corpus instruments exit 0."`
3. Do **not** rewrite `measured_against` (`head` is `d85982d`, round 17): the file's convention is to retain it as the historical record and append notes (see the `round16_redispatch` note's last sentence).

If the new corpus docs cite the round-47 fleet report before it exists, `report_dead` DRIFT; if they cite a commit, `commit_total` must be re-recorded. Both are `equal`/zero pins, not automatic.

## 7. Verification evidence (scratch only)

Commands and exit codes; the green runs are in `/fast/scratch/kotoba-r47/ScoutReadmeIndex/{lane,verify,verify2}` with the three new corpus files present (stubs) and tracked.

| Command | Exit | Key output |
|---|---|---|
| `git rev-parse HEAD` (lane) | 0 | `c61a973b2e02e1ded169703ddcb06466f4edd8bd` |
| `verify_corpus_integrity.py --json` (live BASE) | 1 | `tracked_files 59 vs 58`, `unindexed 1` |
| `verify_corpus_independent.py --json` (live BASE) | 1 | `unindexed 1`, same file |
| `verify_skill_checklist.py --json` (live BASE) | 1 | 9 PASS / 1 FAIL; FAIL `governance.citation_resolves`: `LOG.md:2111: '.ufo/round-45/drafts/v10/post-r44-hunt.py' does not resolve`; box map "41 boxes mapped (8 executed, 0 delegated, 33 unexecuted)" |
| `check_substrate_pins.py --json` (live BASE) | 2 | `pass 0`, `fail 3` (omp sha DRIFT, omp mtime DRIFT, opencode UNREADABLE) |
| `verify_surfaces.py --json` (live BASE) | 2 | `opencode binary not found: /home/vgpnk/.opencode/bin/opencode` |
| `verify_surfaces.py --omp-strings <snapshot> --opencode-strings <snapshot> --json` | 1 | `pass 4 / fail 3`; vacuity 0/8, OC-1/OC-4/OC-6 empty |
| clone, rows + 3 files + baseline `expect: 62`, `verify_corpus_integrity.py --json` | 0 | 9/9 PASS |
| same clone, `verify_corpus_independent.py --json` | 0 | all 9 PASS/INFO |
| counterexample: row token `corpus/lessons/round-47.md` instead of `lessons/round-47.md` | 1 | `unindexed 1`, `stale_patterns 1`, `missing_paths 1` — three DRIFTs for one wrong prefix |
| counterexample: row present, file deleted from disk+index | 1 | `stale_patterns 1`, `missing_paths 1` (`corpus/README.md:65: knowledge/substrate-recensus-round47.md -> …`) |
| `git apply --check ScoutReadmeIndex.patch` / `git apply` (fresh BASE clone) | 0 / 0 | clean |
| fresh clone + patch + 3 files, both corpus verifiers | 0 / 0 | `9/9 checks pass`, independent `exit 0`; README 123 lines |

The README rows add **8** harvested tokens (76 → 84: row 1 = 1, row 2 = 1, row 3 = 3, row 4 = 3) and **zero** report/commit citations; with the patch applied, `report_total 40` and `commit_total 29` are unchanged. The Frontier replacement drops the old row's column-2 `` `description` `` token, so the independent witness's INFO counter `index_tokens_outside_coverage_map` goes 1 → 0 (it is not a gate; the integrity gate never reads outside the coverage map).

Note on clone use: `verify_skill_checklist.py` is positional and **must** run in the lane. In a clone it fails spuriously — `trigger.name_directory` FAILs when the directory is not `kotoba-shokunin`, and `trigger.citation_resolves` FAILs on `../.ufo/...` that only exists at the lane root. My clone runs of that verifier are therefore not evidence and are not used.

## 8. What I did NOT check

- Whether C1 actually lands 7/7 and 3/3: I only measured the instruments' current failures. Rows 3's target numbers are the plan's, not observed.
- The C1 class count / re-verdiction outcome: the README's "8 machine-extracted `.md` registrations" needs C1's re-derivation; I did not re-derive it, and I deliberately kept "8" out of the new rows.
- C2's actual check id, fixture names and whether the box map moves; §5 gives the conditional arithmetic, not a verdict.
- C3's erratum registry implementation: nothing named `errata`/`erratum` exists under `verifiers/` at BASE (`grep -rn` exit 1), so I could not index or verify it; if it lands as a corpus file it needs a row.
- `verify_harness_claims.py` (21/28 at BASE per the plan) and `verify_harness_independent.py` (row 38's "live 24/24"): not re-run; no README edit proposed there.
- The round-27 opencode telemetry note (`corpus/README.md:15-16`) against the 1.19.3 DB: not re-measured, so not called stale.
- The end-to-end landing with the real authored corpus docs: I tested with stubs, so the docs' own report/commit citations (which move `report_total`/`commit_total`) are unmeasured.
- The live checklist gate after C2: not run against a modified tree (production read-only; clone invalid, §7).
