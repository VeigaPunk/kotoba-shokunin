verdict: PARTIAL — the two new coverage-map rows and the rewritten Frontier row are path-correct, load-bearing and (for the Frontier row) factually true, but the round-47 lessons row overstates its own lesson's re-open set (`S001–S008 re-opened` vs the lesson's "S006, S007 not re-opened"), the adjacent round-46 lessons row still says "spot-check pending non-author" two lines below a row that indexes the landed spot-check, and the known-false "29 heads" count in the same file that the wave-1 scout measured at 28 and proposed fixing was dropped at landing.

# W2ReadmeIndex — falsify of `corpus/README.md` at 7ad7fad

**Target:** `/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/README.md` @ `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`
**Scope:** the coverage-map rows added in round 47, the rewritten Frontier row, "paths resolve", "descriptions true", "no other row edited".
**Lane:** leaf member, no subagents. Scratch clone `/fast/scratch/kotoba-r47/w2/W2ReadmeIndex/kotoba-shokunin` (canonical layout, symlinks to `/home/vgpnk/Projects/shokunin/*`), detached at 7ad7fad; all mutations committed there only and reverted (`git reset --hard 7ad7fad`). No production file was written by this lane. No tool was installed or upgraded (system `git`, `python3 -B`, `grep`/`sed` only).

---

## 1. What the round actually changed in the file

```
$ cd /fast/scratch/kotoba-r47/w2/W2ReadmeIndex/kotoba-shokunin
$ git diff c61a973b2e02e1ded169703ddcb06466f4edd8bd 7ad7fadfc09354b74fb66605dfb0c1182c115a2f -- corpus/README.md
 corpus/README.md | 4 +++-
 1 file changed, 3 insertions(+), 1 deletion(-)
```

Whole-file opcode diff (python `difflib.SequenceMatcher`, base vs head, every line):

```
insert base[63:63] head[63:65]
  + | Round-46 non-author spot-check (integrator) | `lessons/round-46-verifier-spotcheck.md` | …
  + | Round-47 lessons | `lessons/round-47.md` | …
replace base[74:75] head[76:77]
  - | Loader-rule freshness | omp 18.12.3 drift leaves surfaces 5/7 and pins 1/3; the frontmatter `description` XML-token rule is unchecked by the lane's own gate | …
  + | Loader-rule freshness | round 47: omp 18.12.5 and opencode 1.19.3 (npm channel, round-14 loader lineage) re-derived and re-pinned — surfaces 7/7, pins 3/3 at default resolution; …
```

**"no other row edited" — HOLDS.** Section-scoped row extraction (coverage-map table rows: base 56 → head 58; Frontier table rows: base 8 → head 8) shows exactly two insertions and one in-place replacement; every other coverage-map row and every other Frontier row is byte-identical between `c61a973` and `7ad7fad`. The root `README.md` was not touched (`git diff --stat c61a973 7ad7fad -- README.md` → empty). Only `corpus/README.md` changed in the corpus tree besides `QUALITY.md`, `SOURCES.md`, the census and `lessons/round-47.md`.

---

## 2. Findings

### F1 — MEDIUM — `corpus/README.md:64` claims a wider re-open set than the lesson it indexes

The new row says:

```
corpus/README.md:64  … `## Gate` (source rows S012–S015 with access records, S001–S008 re-opened, the C1 class ledger pointer)
```

The row it indexes says the opposite for two of the eight:

```
corpus/lessons/round-47.md:46  **Existing rows re-opened (no status change):** S001 content still holds, but its anchor
corpus/lessons/round-47.md:47  label "§ Skill metadata table" names no heading on the live page (`SrcS001.md`); contract
corpus/lessons/round-47.md:48  rule 2 forbids an in-place anchor edit, so the defect is recorded here and a superseding
corpus/lessons/round-47.md:49  row waits for the next round that cites S001. S002, S003, S004, S005, S008 still hold
corpus/lessons/round-47.md:50  (`SrcS002.md` … `SrcS008.md`). S006, S007 not re-opened.
```

Corroborated independently by the registry and by the wave-1 seat inventory:

```
corpus/SOURCES.md:81   already carries, no upload rejection). Re-opened S001–S005 and S008 (no status change;
$ ls .ufo/waves/round-47/build/ | grep -E "SrcS00[67]"
(no output — no SrcS006.md / SrcS007.md seat report exists; the set is SrcS001, SrcS002, SrcS003, SrcS004, SrcS005, SrcS008)
```

So the re-opened set is **6 of 8 rows (S001–S005, S008)**; the coverage-map row asserts the full range **S001–S008**. The range notation reads as a complete predicate over the range — and the sibling clause in the same sentence ("source rows S012–S015 with access records") is likewise a complete claim (4 new rows, all 4 present). A reader taking row 64 at face value believes S006 (RFC 8259) and S007 (Python `json`) were re-verified in round 47; `corpus/SOURCES.md:19-20` still carries both with `status=queued`, `opened=2026-10-19`, and `git diff c61a973 7ad7fad -- corpus/SOURCES.md | grep -cE "^[+-]\| S00[1-8] "` → **0** (no S001–S008 row was touched at all this round, so the two not-re-opened rows carry round-46 open dates).

**Repro:**
```bash
grep -n "S001–S008 re-opened" corpus/README.md
grep -n "S006, S007 not re-opened" corpus/lessons/round-47.md
grep -n "Re-opened S001" corpus/SOURCES.md
ls .ufo/waves/round-47/build/ | grep -E "SrcS00[67]"   # empty
```

**Why no gate catches it:** both corpus instruments harvest only **column 2** (the File column) of coverage-map rows inside the `## Coverage map` section — `verifiers/verify_corpus_integrity.py:351` (`file_column_tokens`) and `:365-370` (section gate), `verifiers/verify_corpus_independent.py:254-283` (`coverage_cells`). Column 3 prose is never read by either instrument, so an over-stated count in the Basis column is structurally invisible.

**Class:** this is the round's own M20/M22 class ("a lesson's own evidence pointers stale at landing" / a carried figure quoted wider than measured) landing inside the row that indexes the lesson recording the class. Suggested repair (one clause, in the lane's own edit): `S001–S005 and S008 re-opened (S006, S007 not re-opened)`.

### F2 — MEDIUM — `corpus/README.md:62` still says the spot-check is "pending", contradicting `:63` two lines below

```
corpus/README.md:62  | Round-46 lessons | `lessons/round-46.md` | … `## Gate` (no knowledge admitted this round; source rows; spot-check pending non-author) |
corpus/README.md:63  | Round-46 non-author spot-check (integrator) | `lessons/round-46-verifier-spotcheck.md` | … landed at `c61a973` without an index row, indexed round 47 |
```

The spot-check is not pending: it landed at `c61a973` and was adjudicated `ADMITTED` with per-axis verdicts (`corpus/lessons/round-46-verifier-spotcheck.md:17`, "ADMITTED: … Open residuals (carried): …"). The wave-1 seat that surveyed this file had already spotted the contradiction and shipped the fix inside its patch — it was not taken at landing:

```
.ufo/waves/round-47/build/ScoutReadmeIndex.patch:
-| Round-46 lessons | … spot-check pending non-author) |
+| Round-46 lessons | … spot-check pending non-author); **round-47 note:** the pending clause is closed by `lessons/round-46-verifier-spotcheck.md`, indexed this round |
```

Note the constraint: `corpus/lessons/round-46.md` is append-only for this lane (the contract: "LOG.md, lessons and historical receipts are append-only"), and `corpus/lessons/round-46.md:81` still reads "pending — non-author verification by the orchestrator after landing; agree/disagree recorded here by a later append" — so the *row* is the only place a correction can live, and the lane left it uncorrected. Net effect: the coverage map asserts, in adjacent rows, that the round-46 spot-check is both pending and adjudicated.

### F3 — MEDIUM (adjacent; outside the two named rows but in the same file) — `corpus/README.md:87` "29 heads" is false, was measured in-wave at 28, and the fix was dropped

```
corpus/README.md:85  - The command check's extraction set is declared
corpus/README.md:86    (`verifiers/checklist-command-vocabulary.json`, 29 heads) plus
corpus/README.md:87    shell-tagged/info-less fenced blocks — a command outside it is invisible, and an
```

Measured:
```
$ python3 -B -c "import json;d=json.load(open('verifiers/checklist-command-vocabulary.json'));print(len(d['commands']))"
28
$ sha256sum verifiers/checklist-command-vocabulary.json
76d16a9cb53e43db25ec4549465fd00bf1f11551384350c7761328a935eeb02b
$ git show c61a973:verifiers/checklist-command-vocabulary.json | sha256sum
76d16a9cb53e43db25ec4549465fd00bf1f11551384350c7761328a935eeb02b   # identical → 28 at BASE too
```
The file has held 28 `commands` entries since round 15, so the "29" is a counting error, not drift. The wave-1 scout recorded exactly this and put the corrected text in its patch (`.ufo/waves/round-47/build/ScoutReadmeIndex.md:95`, and the `ScoutReadmeIndex.patch` hunk that grows the bullet to 4 lines with "28 heads — measured at round 47"). The landing kept "29 heads". Because the round's own brief was "coverage-map rows + Frontier row", one can argue this line was out of scope; but the false present-tense count was in the round's own seat evidence, the corrected wording was written and ready, and the count is one a reader of this file uses to reason about the gate's blind spot. This is the same "descriptions true" axis as the two rows in scope.

### F4 — LOW — the Frontier row's file pointers are outside every corpus gate (mutation-confirmed invisible)

The rewritten Frontier row (`corpus/README.md:76`) cites `` `lessons/round-47.md` `` (M20) and `` `knowledge/instruction-surface-census-round13.md` `` (§ B′) in column 2 of a **Frontier** table row — outside the `## Coverage map` section, so neither instrument path-checks it.

Mutation (in the scratch clone, committed then reverted):
```bash
# replace `lessons/round-47.md` M20) with `lessons/round-47X.md` M20) in the Frontier row
$ python3 -B verifiers/verify_corpus_integrity.py   # → 9/9 checks pass
$ echo $?                                          # → 0
$ python3 -B verifiers/verify_corpus_independent.py | head -3
index   tracked_files=60 index_tokens=78 (outside coverage map=2) unindexed=0 stale=0 missing=0
$ echo $?                                          # → 0
```
A typo in the Frontier row's path is invisible to both instruments (`index_tokens_outside_coverage_map` is an INFO counter, not a gate — `verifiers/verify_corpus_independent.py:311-317, 356`). I verified both pointers **manually** and they are correct at 7ad7fad: `corpus/lessons/round-47.md` exists and its M20 row is at `:19`; `corpus/knowledge/instruction-surface-census-round13.md` exists and `### B′.` is at `:212`; `corpus/knowledge/instruction-surface-census-round13.md:287` is the "Superseded class rows and the round-47 opencode ledger" section the row's § B′ pointer relies on. So the description is true — but nothing enforces it. (Note the head Frontier row carries *two* outside-section tokens vs one at base, so the ungated surface grew.)

### F5 — LOW — `corpus/README.md:63` cites the commit `c61a973` outside the `commit `-grammar, so no instrument verifies it

`verifiers/verify_corpus_integrity.py:146`:
```python
COMMIT_RE = re.compile(r"(?<![A-Za-z0-9_-])commit[ \t]+`([^`\n]+)`")
```
Only `commit `<hex>`` is harvested. The new row writes "landed at `c61a973`" (no `commit` word), so it contributes 0 to `commit_total` and is never checked for resolvability. Mutation-confirmed:
```bash
# landded at `c61a97X` (bogus 7-hex) in corpus/README.md:63
$ python3 -B verifiers/verify_corpus_integrity.py | head -2
corpus.index    tracked=60 unindexed=0 stale=0 missing=0  (78 FILE-column patterns over 59 md files)
corpus.pointers report_dead=0/40 commit_total=29 unresolvable=0 nonhash=0 …
$ python3 -B verifiers/verify_corpus_integrity.py >/dev/null 2>&1; echo $?   # → 0
$ python3 -B verifiers/verify_corpus_independent.py >/dev/null 2>&1; echo $?  # → 0
```
The claim is **true today** — `git cat-file -e c61a973^{commit}` → exit 0, and it is the BASE commit — so this is a gate blind spot, not a false statement. The same bare-hash shape already exists in rows 29/35/37/42/50 (`778310d`, `d49dfa5`, `0f658ff`, `63ceba7`, `683d147`), so it is a pre-existing file convention, not a round-47 regression; the wave-1 scout flagged the grammar avoidance as deliberate (`.ufo/waves/round-47/build/ScoutReadmeIndex.md:59`) to keep `commit_total` at 29. Consequence to note: the round-47 landing's own commit is still uncitable in the checked grammar, so a future edit to that token would be silently wrong.

---

## 3. Claims that survived my attack (findings too)

**S1 — the two new coverage-map rows are real, path-resolving, and load-bearing.**
- `corpus/lessons/round-46-verifier-spotcheck.md` and `corpus/lessons/round-47.md` both exist and are tracked at 7ad7fad (`git ls-files corpus/` → 60 entries; `git ls-tree -r --name-only 7ad7fad corpus/ | grep -E "round-46-verifier-spotcheck|round-47.md"` → both).
- Column-2 tokens are path-checked by both instruments; `missing_paths=0`, `unindexed=0`, `stale_patterns=0` at head (`python3 -B verifiers/verify_corpus_integrity.py --json` → all PASS, exit 0; `verify_corpus_independent.py` → exit 0).
- **Mutation: drop the round-47 row** → `unindexed_detail = ['corpus/lessons/round-47.md']`, integrity exit **1**, independent exit **1**.
- **Mutation: drop the spot-check row** → `unindexed_detail = ['corpus/lessons/round-46-verifier-spotcheck.md']`, integrity exit **1**, independent exit **1**.
- **Mutation: typo the path** (`lessons/round-47.md` → `lessons/round-47x.md`) → `missing_paths = ['corpus/README.md:64: lessons/round-47x.md -> lessons/round-47x.md']` + `unindexed 1`, integrity exit **1**.
  Both rows are therefore *load-bearing*, not decorative: the corpus gate genuinely fails if either is removed or misspelled.

**S2 — every factual assertion in the rewritten Frontier row is true at 7ad7fad.** Re-derived, not read off:
- "omp 18.12.5 … opencode 1.19.3 (npm channel, round-14 loader lineage)": `omp --version` → `omp/18.12.5`; `corpus/knowledge/instruction-surface-census-round13.md:212-218` — "npm `opencode-ai` 1.19.3 … the bytes the `~/.local/bin/opencode` npx wrapper executes … a different distribution channel from v2.0.26 … not its successor" and "the round-13/14 one recorded as historical"; `verifiers/baseline.json` `round47_note` carries the same lineage claim. `sha256sum` of the live default binaries equals the frozen snapshot: `fdbc8136…` (omp) and `179ca421…` (opencode) vs `/fast/scratch/kotoba-r47/shared/SHA256SUMS`.
- "surfaces 7/7, pins 3/3 at default resolution": `python3 -B verifiers/verify_surfaces.py` → 7 `PASS` lines, exit **0**; `python3 -B verifiers/check_substrate_pins.py` → `OK 3/3 pins hold`, exit **0** — both with the default `DEFAULT_BINARIES`/`BINARIES` paths, i.e. no override.
- "the XML-token rule moved to Core (`trigger.no_xml_tag`)": `PROVINCE.md:15` — "Frontmatter XML-tag rule (round 47, moved from Frontier)"; the check exists at `verifiers/verify_skill_checklist.py:97, 310, 1294` and PASSes live (`verify_skill_checklist.py --json` → `trigger.no_xml_tag PASS`, exit 0).
- "the omp extractor is a callee-name allowlist, so the next minifier rename is a red gate": `verifiers/verify_surfaces.py:138-146` — "a callee allowlist of the minified names … the callee name is minification-volatile — the FIRST thing to re-pin on a binary bump"; `OMP_CALL_RE` at `:157` is exactly that allowlist.
- "the round-46 'omp 18.12.3 … 5/7 … 1/3' figures were a stale copy, `lessons/round-47.md` M20": `git show c61a973:SCORECARD.md | grep -c "installed omp 18.12.3"` → **1** (the stale plan row); the before-run measured `surfaces default: exit=2` and `pins: exit=2 DRIFT 3/3` (`.ufo/waves/round-47/before/SUMMARY.md`), so 5/7·1/3 were carried figures, not measurements; `corpus/lessons/round-47.md:19` M20 names the class and the copied before-column. The row's correction is accurate.
- "§ B′" pointer resolves (`census:212`), and the row's remaining "not held" reason (rename robustness) is honest rather than a re-claim of a held item.

**S3 — the two new rows' descriptions match their sources on every claim I could check.** Row 63: "written by the kaika integrator, not the lane (outside review; never edited here)" — `git log --oneline -- corpus/lessons/round-46-verifier-spotcheck.md` → only `c61a973`; `git diff --stat c61a973 7ad7fad -- corpus/lessons/round-46-verifier-spotcheck.md` → empty (never edited here ✓). "S003/S006 admit, S011 reject — both agree" — spot-check `:12-13`, result column "agree" for both ✓. "the adjudication ADMITTED with per-axis verdicts and the carried open residuals" — `:17` "ADMITTED: … Per-axis: depth improved … Open residuals (carried): …" ✓. "landed at `c61a973` without an index row" — `git show --stat c61a973` shows one file, 17 insertions, no other; `git show c61a973:corpus/README.md | grep -c spotcheck` → **0** ✓ (and the file was genuinely unindexed at BASE: `verify_corpus_integrity.py --json` at BASE → `tracked_files 59≠58` DRIFT, `unindexed 1`, exit 1).
Row 64: "LOG.md round-47 entry" — `LOG.md:2317` "## 2026-10-21 — Round 47 landing …" ✓; "`## Mistakes` (stale planned premise M20, unindexed closure landing M21, stale lesson pointers M22)" — the three M-rows' titles are exactly "Stale planned premise (before-values copied, not re-measured)" / "Corpus file landed without its index row (closure commit)" / "A lesson's own evidence pointers stale at landing" ✓; "source rows S012–S015 with access records" — the lesson's Gate table has all four with `accessed`, a ≤25-word quote and a seat record ✓; "the C1 class ledger pointer" — `corpus/lessons/round-47.md:56` ✓. **The only untrue clause in either row is F1's "S001–S008 re-opened".**

**S4 — the corpus-baseline expectation the rows sit on is honest.** `verifiers/corpus-baseline.json` `notes.round47` states "tracked_files 58 -> 60: corpus/lessons/round-46-verifier-spotcheck.md (landed by the integrator at c61a973 without an index row, the round-47 M21 class) and corpus/lessons/round-47.md, both indexed in corpus/README.md … Expectation refresh for two real indexed files, not a fitted denominator." Verified: expectation 58→60, observed tracked files 59 at `c61a973` → 60 at 7ad7fad (`git ls-tree -r --name-only <c> corpus/ | wc -l`), and the delta is exactly those two files. `report_total 40` / `commit_total 29` unchanged, both zero-class checks 0.

**S5 — full gate battery green at 7ad7fad in a clean canonical clone** (exit codes as run):
```
python3 -B verifiers/verify_corpus_integrity.py     → 0   (9/9 checks pass)
python3 -B verifiers/verify_corpus_independent.py   → 0   (tracked_files=60 index_tokens=78 unindexed=0 stale=0 missing=0)
python3 -B verifiers/verify_surfaces.py             → 0   (7 PASS)
python3 -B verifiers/check_substrate_pins.py         → 0   (OK 3/3 pins hold)
python3 -B verifiers/verify_skill_checklist.py      → 0   (11 PASS, 0 FAIL)
bash   verifiers/fault_injection_corpus.sh          → 0   (verdict: ALL PASS)
```
matching `.ufo/waves/round-47/after/SUMMARY.md` (surfaces 0, pins 0, checklist 0, corpus integrity 0, independent 0, fault harness 0; harness claims 1 — pre-existing 21/28, not claimed this round).

---

## 4. Residual risk

- **No instrument reads column 3 prose.** F1 and F3 are in the Basis column; both corpus instruments harvest column 2 only. Any over-stated count in a Basis cell is structurally invisible — the only defence is a human or a future non-author reading the row against its source. `corpus/knowledge/claim-census-round12.md` is the lane's historical countermeasure (a per-claim census), but it is a document, not an instrument, and it was not re-run this round.
- **The Frontier table is outside the corpus census by construction** (`verifiers/verify_corpus_integrity.py:350-361` documents this as a round-12 fix). Round 47 put two path-shaped tokens into that region (F4), so the ungated surface grew by one; the pointers are correct today only because I checked them by hand.
- **`git diff` shows 273 files / +46,865 lines in the round-47 landing** (mostly `.ufo/waves/round-47/build/**` evidence). I reviewed the corpus/README.md diff in full; I did not review the 260+ other changed files.
- The lesson-side correction for F1 may be landable as an append-only erratum inside `corpus/lessons/round-47.md` if the lane prefers the lesson to carry it rather than the README row; I did not test that route (the lesson's own `## Gate` is append-only, and I did not check whether a new `## Mistakes`/erratum block would re-trigger `corpus.index` checks).

## 5. What I did NOT check

- I did not verify the *content* of `corpus/lessons/round-47.md` M20/M21/M22 evidence commands beyond reading them (their re-derivation is the `W2LessonM20/M21/M22` lanes' scope).
- I did not re-derive the C1 surface/pin numbers from the binaries myself — I re-ran the two shipped gates at default resolution (7/7, 3/3, exit 0/0) and confirmed the pinned sha256 values equal `/fast/scratch/kotoba-r47/shared/SHA256SUMS`; the extraction rules themselves (OC-1..OC-6, the omp call-shape regex) are the C1/census lanes' scope.
- I did not audit `verifiers/verify_skill_checklist.py`'s `trigger.no_xml_tag` semantics or its four fixtures (C2 lanes' scope); I confirmed the check exists, is wired, and PASSes, and that the frontmatter `<skills>` count went 1 → 0 (`git show c61a973:SKILL.md` frontmatter count 1 vs head 0).
- I did not check `corpus/SOURCES.md` rows S012–S015 for source accuracy (only their presence, their `recheck`/`status` cells, and that no S001–S008 row was modified).
- I did not verify `PROVINCE.md`, `SCORECARD.md`, `LOG.md` round-47 prose beyond the specific claims quoted above (PROVINCE carries its own stale `omp 18.12.3 … surfaces 5/7, pins 1/3` string at `:22`; that file is another lane's scope).
- I did not execute the `~/.local/bin/opencode` wrapper (contract-prohibited) and did not copy any binary or strings dump into the lane repo; all substrate checks read the frozen snapshot and the default paths only.
- I did not check the `index_tokens_outside_coverage_map` INFO counter's self-test expectations (`verify_corpus_independent.py:718` asserts 1 on a fixture), only that the head value is 2 and ungated.

---

### Reproduction summary (all commands run in `/fast/scratch/kotoba-r47/w2/W2ReadmeIndex/kotoba-shokunin`)

| # | command | exit | outcome |
|---|---|---|---|
| 1 | `git diff c61a973 7ad7fad -- corpus/README.md` | 0 | 3 insertions, 1 deletion; only rows 63/64/76 touched |
| 2 | `python3 -B verifiers/verify_corpus_integrity.py --json` | 0 | tracked 60, unindexed 0, missing 0, 9/9 PASS |
| 3 | `python3 -B verifiers/verify_corpus_independent.py` | 0 | tracked 60, tokens 78, unindexed 0 |
| 4 | mutate: drop `Round-47 lessons` row | 1 | `unindexed=['corpus/lessons/round-47.md']` |
| 5 | mutate: drop `Round-46 non-author spot-check` row | 1 | `unindexed=['corpus/lessons/round-46-verifier-spotcheck.md']` |
| 6 | mutate: `lessons/round-47.md` → `lessons/round-47x.md` (coverage row) | 1 | `missing_paths=1` + `unindexed=1` |
| 7 | mutate: `lessons/round-47.md` → `lessons/round-47X.md` (Frontier row) | **0** | **not detected** (F4) |
| 8 | mutate: `c61a973` → `c61a97X` (row 63 commit cite) | **0** | **not detected** (F5) |
| 9 | `python3 -B verifiers/verify_surfaces.py` | 0 | 7 PASS (omp 18.12.5 / opencode 1.19.3 at default paths) |
| 10 | `python3 -B verifiers/check_substrate_pins.py` | 0 | OK 3/3 pins hold |
| 11 | `python3 -B verifiers/verify_skill_checklist.py --json` | 0 | 11 PASS / 0 FAIL |
| 12 | `bash verifiers/fault_injection_corpus.sh` | 0 | verdict: ALL PASS |
| 13 | `sha256sum` live omp/opencode vs `/fast/scratch/kotoba-r47/shared/SHA256SUMS` | 0 | `fdbc8136…` / `179ca421…` both match |
| 14 | `git cat-file -e c61a973^{commit}` | 0 | resolves |
