verdict: C3 index row + corpus-baseline re-record (tracked_files 58→59) make both corpus instruments green in the scratch clone (integrity 9/9 exit 0, independent exit 0, both `--self-test` 0 failures) and the patch reproduces that on a fresh BASE clone; the fault harness still exits 1 from a pre-existing defect introduced at f2f9ee1 (planted index rows land outside the coverage map), routed with a verified sketch and NOT included in this patch.

# C3 corpus index — round-47 build (lane C3CorpusIndex)

BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`. Scratch clone `/fast/scratch/kotoba-r47/C3CorpusIndex/lane`, committed locally as `0335341` (scratch only; the harness clones committed HEAD). The production tree was not written. It was read only: the scratch clone was made from it with `git clone` as a read-source, and no git command ran in its working tree.

Axes: freshness — the baseline now matches the committed tree; operability — both instruments exit 0 and the patch reapplies cleanly; calibration — the row is path-checked, both edits are individually necessary (§5), and the harness defect is named.

## 0. Deliverables
- `C3CorpusIndex.patch` (`git diff c61a973 0335341`, 2 files, +4/−2):
  - `corpus/README.md`: one coverage-map row inserted after `:62` (after-patch `:63`): `Round-46 verifier spot-check` | `` `lessons/round-46-verifier-spotcheck.md` `` | integrator-written non-author spot-check (one admit, one reject, both `agree`) and the r46 WIP adjudication.
  - `verifiers/corpus-baseline.json`: `:15` `corpus.index.tracked_files` `expect` 58→59; `:57` gains a trailing comma; new `notes.round47_c3_index` at `:58`.
- `C3CorpusIndex.fault-harness-sketch.patch`: NOT part of C3. Scratch-only verified fix for §5.2.
- Evidence (JSON/TXT) beside it; list in §9.

## 1. Red state at BASE and its cause
- `corpus/lessons/round-46-verifier-spotcheck.md` (17 lines) entered the tree in `c61a973` alone (`git show --stat c61a973`: 1 file, 17 insertions) without a coverage-map row. The coverage map runs `corpus/README.md:5`–`:63`; its last row is `:62`; `## Frontier` starts at `:64`.
- Integrity (BASE): `DRIFT corpus.index.tracked_files observed=59 expected=58`, `DRIFT corpus.index.unindexed observed=1` (exit 1, 7/9). Independent (BASE): `unindexed=1` (exit 1). Matches SUMMARY.md before-values.
- The 58→59 delta is exactly that file: `git ls-tree -r --name-only 04192c2 corpus/` = 58; `git diff --name-status 04192c2 c61a973 -- corpus verifiers` = one `A` line. This is a real new tracked file, not a fitted denominator.

## 2. Why the row satisfies the instruments
- Column-2 harvest reads only the `## Coverage map` section: `verifiers/verify_corpus_integrity.py:351-384` (section gate `:365-370`); independent `verifiers/verify_corpus_independent.py:254-283`. The token is matched exactly against the tracked set: `verify_corpus_integrity.py:421-434`; independent `:328-335` (match) and `:348-351` (unindexed). A typo would flip `stale_patterns`/`missing_paths` (§5.2 exercises both classes).
- The Basis column carries no `.ufo/reports/round-N/` pointer and no `` commit `<token>` ``. Both shapes are scanned over every tracked md, README included: `verify_corpus_integrity.py:141-146`; independent `:100-103`. Hence `report_total` 40 and `commit_total` 29 are unchanged (observed, §4).
- Basis text checked against the lesson (`corpus/lessons/round-46-verifier-spotcheck.md:1-17`): admit S003/S006 agree, reject S011 agree (table at `:10-13`), adjudication at `:17`.

## 3. Baseline re-record — only one expectation moves
- `checks.corpus.index.tracked_files.expect` 58→59 (`verifiers/corpus-baseline.json:15`). Other pins are unchanged: `report_total` 40, `commit_total` 29, all zero-mode checks (the instrument confirms, §4).
- `notes.round47_c3_index` appended after `round46_landing` (`:57`), matching the earlier re-records: round-23 (`LOG.md:1233`, "corpus-baseline re-record (observed 52→53 tracked …)") and round-46 (`LOG.md:2310`, notes `round46_landing`).
- `as_of` (`:2`) and `measured_against` (`:4-10`) untouched. They have been stale since round 16–17 and every later re-record left them alone (carried, §6).
- Read-only semantic diff vs BASE baseline (python): only `checks.corpus.index.tracked_files` differs; `notes` gains exactly `round47_c3_index`; existing notes unchanged; `measured_against`/`as_of` equal.

## 4. Commands and exit codes (cwd = lane; BASE then after-edit)
| stage | command | exit | key output |
|---|---|---|---|
| BASE | `python3 -B verifiers/verify_corpus_integrity.py --json` | 1 | DRIFT tracked_files 59≠58; DRIFT unindexed 1 |
| BASE | `python3 -B verifiers/verify_corpus_integrity.py` | 1 | `tracked=59 unindexed=1 stale=0 missing=0 (76 FILE-column patterns over 58 md files)`; `report_dead=0/40 commit_total=29 unresolvable=0 nonhash=0`; `7/9 checks pass` |
| BASE | `python3 -B verifiers/verify_corpus_integrity.py --self-test` | 0 | `0 failure(s) over 150 assertions` |
| BASE | `python3 -B verifiers/verify_corpus_independent.py --json` | 1 | unindexed 1 |
| BASE | `python3 -B verifiers/verify_corpus_independent.py` | 1 | `tracked_files=59 index_tokens=76 (outside coverage map=1) unindexed=1`; `citations=29 nonhash=0 unresolvable=0` |
| BASE | `python3 -B verifiers/verify_corpus_independent.py --self-test` | 0 | `91 assertions, 0 failures` |
| edit | baseline `:15`/`:57`/`:58`; `python3 -m json.tool verifiers/corpus-baseline.json` | 0 | valid JSON |
| E2 | integrity with new baseline, BASE README | 1 | DRIFT unindexed 1 only; `8/9` |
| edit | README row inserted after `:62` | — | — |
| AFTER | `python3 -B verifiers/verify_corpus_integrity.py --json` | 0 | `9/9 checks pass` |
| AFTER | `python3 -B verifiers/verify_corpus_integrity.py` | 0 | `tracked=59 unindexed=0 stale=0 missing=0 (77 FILE-column patterns over 58 md files)`; `report_dead=0/40 commit_total=29 unresolvable=0 nonhash=0` |
| AFTER | `python3 -B verifiers/verify_corpus_integrity.py --self-test` | 0 | `0 failure(s) over 150 assertions` |
| AFTER | `python3 -B verifiers/verify_corpus_independent.py --json` | 0 | all zero classes 0; `tracked_files=59` |
| AFTER | `python3 -B verifiers/verify_corpus_independent.py` | 0 | `tracked_files=59 index_tokens=77 (outside coverage map=1) unindexed=0 stale=0 missing=0`; `citations=29 nonhash=0 unresolvable=0` |
| AFTER | `python3 -B verifiers/verify_corpus_independent.py --self-test` | 0 | `91 assertions, 0 failures` |
| E1 | integrity `--baseline` = BASE baseline (row present, no re-record) | 1 | DRIFT tracked_files 59≠58 only; `8/9` |
| apply | fresh BASE clone: `git apply --check`, `git apply C3CorpusIndex.patch` | 0, 0 | then integrity `--json` 0 (9/9), independent `--json` 0, both self-tests 0 failures |
| commit | scratch commit `0335341` (needed for the harness) | 0 | `2 files changed, 4 insertions(+), 2 deletions(-)` |
| fault | `TMPDIR=/tmp bash verifiers/fault_injection_corpus.sh --repo "$PWD"` on `0335341` | 1 | `FAILURES PRESENT`: every row PASS except `fault-d1` and `fault-d2` (MISS) |
| fault | same harness `--self-test` on `0335341` | 0 | `self-test: OK` |
| fault (pre) | same harness, HEAD = BASE (red) | 1 | `fault-0-control` FAIL-control-dirty; self-test T3 FAIL → BROKEN |
| prehist | same harness at `78ee57e` (pre-f2f9ee1) | 0 | `verdict: ALL PASS`; d1 → stale+missing, d2 → stale |
| sketch | scoped insert (§5.2), scratch copy only | 0 | `verdict: ALL PASS`; self-test `OK` |

No tool was installed or upgraded. Used system `git`, `python3 -B` and the verifiers' own CLIs.

## 5. Counterexamples and falsifiers
1. **Both edits are necessary.** Row without re-record → E1 exit 1, only `tracked_files` DRIFTs. Re-record without row → E2 exit 1, only `unindexed` DRIFTs.
2. **Fault-harness `d1`/`d2` MISS is pre-existing, not caused by C3.**
   - `verifiers/fault_injection_corpus.sh:111-121` (`insert_index_row`) plants after the last `|` line of the whole README (`:117`). At BASE that line is `corpus/README.md:75`, which sits in `## Frontier` (`:64`), outside the coverage map. The planted rows are never counted: in the BASE-state run d1 fired only `unindexed` (expected `missing_paths`) and d2 only `unindexed` (expected `stale_patterns`).
   - `## Frontier` first appears in `f2f9ee1` (`git log -S'## Frontier'`). At `78ee57e` the same harness is `ALL PASS`, exit 0.
   - Scratch-only sketch (`C3CorpusIndex.fault-harness-sketch.patch`): scope the insert to the `## Coverage map` section (replace the one `idx = max(…)` line with a start/end-bounded `idx`, update the helper comment). Result `ALL PASS`, exit 0; self-test `OK`. Routed for the L1 to decide; not in C3.
3. **Harness sequencing.** `new_world` clones committed HEAD only (`verifiers/fault_injection_corpus.sh:73-80`), so the fault-0 control and self-test T3 need a green committed HEAD. At BASE HEAD they fail for that reason. Run the harness on the landed tree, not on BASE.

## 6. Carried, not changed here
- `corpus/README.md:62` still says "spot-check pending non-author". Now superseded by the new row at `:63`. Left as the historical description (append-only convention); the L1 may annotate it.
- `verifiers/corpus-baseline.json:2` `as_of` 2026-09-29 and `:4-10` `measured_against.head` `d85982d` are stale, as in every round since 16.
- The independent instrument's `outside coverage map=1` is the backticked `description` in the Frontier row (`corpus/README.md:74` at BASE). It is counted, not checked, and is not a path.

## 7. Integration notes
- Any other seat that lands a new `corpus/*.md` must re-record `verifiers/corpus-baseline.json:15` again, since `equal` pins fail on every new file. That line is the likely merge conflict point. [INFERENCE: other C-lanes may add such a file; not verified.]
- The patch touches README between `:62`–`:63` and baseline `:15`, `:57`–`:58`. Other hunks should not conflict.
- Under jj the lesson is already in the BASE commit, so the tracked set (`git ls-files corpus/`, 59) does not need a `git add`. README and baseline are working-tree edits read directly by the instruments. [INFERENCE: the production jj working copy was not measured.]

## 8. What I did NOT check
- Production tree: no git command ran there. BASE identity comes from the clone, and the before-values match SUMMARY.md. [INFERENCE: production == BASE.]
- Governance erratum registry half of C3 (`LOG.md:2111` / `governance.citation_resolves`). Outside this item; `verify_skill_checklist.py` was not run.
- Not run: `verify_harness_claims.py`, `verify_surfaces.py`, `check_substrate_pins.py`, `verify_skill_checklist.py`. A grep for `README` under `verifiers/` found the two corpus instruments, the fault harness, and checklist fixtures/docstrings; I did not read `verify_skill_checklist.py`'s code paths in full.
- A repo-wide grep for live counts (`tracked=5x`, `tracked_files`, `index rows`) returned 143+ files, mostly `.ufo` history. I did not confirm that no live non-history doc cites the old count.
- jj-colocated production behavior was not exercised.
- Labrat not dispatched.

## 9. Artifacts (`.ufo/waves/round-47/build/`)
- `C3CorpusIndex.patch`; `C3CorpusIndex.fault-harness-sketch.patch`
- `C3CorpusIndex.integrity-before.json`, `C3CorpusIndex.integrity-after.json`
- `C3CorpusIndex.independent-before.json`, `C3CorpusIndex.independent-after.json`
- `C3CorpusIndex.falsify-baseline-only.json` (E2), `C3CorpusIndex.falsify-row-only.txt` (E1)
- `C3CorpusIndex.fault-harness-committed.txt` (`0335341`, exit 1), `C3CorpusIndex.fault-harness-sketch-run.txt` (ALL PASS), `C3CorpusIndex.fault-harness-78ee57e.txt` (ALL PASS)

Reproduce: `git clone --no-hardlinks <repo> x && git -C x checkout --detach c61a973 && git -C x apply <path>/C3CorpusIndex.patch && python3 -B x/verifiers/verify_corpus_integrity.py && python3 -B x/verifiers/verify_corpus_independent.py` → both exit 0.
