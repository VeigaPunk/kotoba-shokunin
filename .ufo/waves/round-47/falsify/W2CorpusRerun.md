verdict: HOLDS — attacked both corpus instruments at 7ad7fad (9/9 + exit 0 at tip, exit 1 at BASE c61a973), mutation-tested the two new corpus/README.md index rows and the re-recorded baseline; both new rows name real tracked files; two LOW calibration defects found, neither flips a verdict.

Lane: `KotobaR47-2.W2CorpusRerun-2` (leaf, no dispatch). Scope: `verifiers/verify_corpus_integrity.py` + `verifiers/verify_corpus_independent.py` re-run, the `corpus/README.md` index rows added in round 47, and the `verifiers/corpus-baseline.json` re-record.

Scratch clone: `/fast/scratch/kotoba-r47/w2/W2CorpusRerun/kotoba-shokunin` @ `7ad7fadfc09354b74fb66605dfb0c1182c115a2f` (detached). Production repo `/home/vgpnk/Projects/shokunin/kotoba-shokunin` was read-only (HEAD is also `7ad7fad`; only untracked `.ufo/waves/round-47/*` entries present). All mutations were done in the scratch clone and reverted (`git diff --stat` empty afterwards). Command log: `.ufo/waves/round-47/falsify/W2CorpusRerun.commands.txt`. Artifacts: `W2CorpusRerun.integrity.json`, `W2CorpusRerun.integrity.selftest.txt`, `W2CorpusRerun.independent.json`, `W2CorpusRerun.independent.txt`, `W2CorpusRerun.independent.selftest.txt`, `W2CorpusRerun.commands.txt`.

---

## 1. Counting claims re-derived (freshness / operability)

### 1.1 Tip = `7ad7fad`

| command (cwd = scratch clone @7ad7fad) | exit | key output |
|---|---|---|
| `python3 verifiers/verify_corpus_integrity.py --json` | **0** | `corpus.index.tracked_files` observed **60** expected **60** PASS; 9 results, all PASS. observed: `tracked_files 60, index_patterns 78, index_tokens_total 78, index_tokens_fenced 0, index_tokens_excluded 0, index_tokens_classified {directory: 2}, unindexed 0, stale_patterns 0, missing_paths 0, report_total 40, report_dead 0, commit_total 29, commit_unresolvable 0, commit_nonhash 0, report_pointers_excluded 8, commit_quoted_excluded 2, report_pointer_shapes {relative 1, absolute 38, tilde 1, bare 0}, corpus_md_files 59` |
| `python3 verifiers/verify_corpus_integrity.py --self-test` | **0** | `self-test: 0 failure(s) over 150 assertions` |
| `python3 verifiers/verify_corpus_independent.py` | **0** | `index tracked_files=60 index_tokens=78 (outside coverage map=2) unindexed=0 stale=0 missing=0`; `points candidates=48 checked=40 excluded=8 quoted=0 dead=0 shapes={'absolute': 38, 'tilde': 1, 'relative': 1, 'bare': 0}`; `commits candidates=31 citations=29 hex=29 quoted=2 nonhash=0 unresolvable=0`; `exit 0` |
| `python3 verifiers/verify_corpus_independent.py --json` | **0** | same numbers as the text run (independent re-derivation, not a copy) |
| `python3 verifiers/verify_corpus_independent.py --self-test` | **0** | `self-test: 91 assertions, 0 failures` |

`python3 verifiers/verify_corpus_integrity.py --no-baseline --json` → exit 0, `tracked_files 60, index_tokens_total 78, report_total 40, commit_total 29` — i.e. the baseline-free observation and the baseline-compared observation agree; `expect: 60` is not hiding a different observed value.

Re-run in the **production** repo (read-only): integrity exit **0** (`9/9 checks pass`), independent exit **0** (`exit 0`), both `--self-test` exit **0**. The verdict is identical in the scratch clone and in the lane repo, so it is not a clone artifact.

**The acceptance numbers hold exactly:** `tracked_files 60 == expect 60`, 9/9 checks pass, exit 0; `report_total 40` and `commit_total 29` unchanged; both instruments' self-tests green (150 and 91 assertions).

### 1.2 Before = `c61a973` (BASE) — the "exit 1 → 0" transition is real, not a rewritten baseline

```
git checkout --detach c61a973b2e02e1ded169703ddcb06466f4edd8bd
python3 verifiers/verify_corpus_integrity.py     # EXIT=1
   corpus.index  tracked=59 unindexed=1 stale=0 missing=0  (76 FILE-column patterns over 58 md files)
   unindexed: corpus/lessons/round-46-verifier-spotcheck.md
   DRIFT corpus.index.tracked_files: observed=59 expected=58
   DRIFT corpus.index.unindexed: observed=1 expected=0 / empty
   7/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed
python3 verifiers/verify_corpus_independent.py   # EXIT=1
   index tracked_files=59 index_tokens=76 (outside coverage map=1) unindexed=1 stale=0 missing=0
   points ... report_total 40 dead=0 ; commits ... commit_total 29 nonhash=0 unresolvable=0
```

Parent of BASE `04192c2` → `python3 verifiers/verify_corpus_integrity.py` exit **0** (`9/9 checks pass`). This confirms the round-47 M21 story end to end: the integrator's closure commit `c61a973` added `corpus/lessons/round-46-verifier-spotcheck.md` (`git show --stat c61a973` → 1 file changed) without an index row and left the gate red at BASE; round 47 closed it.

The committed before-receipts agree with my independent re-measurement byte-for-byte on the decisive fields: `.ufo/waves/round-47/before/SUMMARY.md` line `corpus integrity: exit=1 DRIFT tracked_files 59!=58, unindexed 1` and `corpus independent: exit=1 DRIFT unindexed`; `.ufo/waves/round-47/before/verify_corpus_integrity.py.out` (`tracked_files 59`, `unindexed_detail ["corpus/lessons/round-46-verifier-spotcheck.md"]`); `.ufo/waves/round-47/before/verify_corpus_independent.py.out` (`index_tokens 76`, `index_tokens_outside_coverage_map 1`).

### 1.3 The baseline re-record is a real count, not a fitted denominator

`git diff c61a973 7ad7fad -- verifiers/corpus-baseline.json` → one substantive change: `checks.corpus.index.tracked_files.expect` **58 → 60** (`verifiers/corpus-baseline.json:15`), plus a new `notes.round47` string (`:58`). Every other `expect` is untouched; `report_total` expect stays 40, `commit_total` expect stays 29.

Independent count at 7ad7fad: `git ls-files corpus/ | wc -l` → **60** (59 `.md` + 1 `.json`: `corpus/knowledge/sibling-citation-routing-round16.json`). The instrument's own `tracked_files` is 60 and `unindexed` is 0, so every one of the 60 tracked corpus files is covered by a coverage-map row. The expectation equals the real population.

### 1.4 The two new index rows name real files

`corpus/README.md:63` — `| Round-46 non-author spot-check (integrator) | `lessons/round-46-verifier-spotcheck.md` | …`
`corpus/README.md:64` — `| Round-47 lessons | `lessons/round-47.md` | …`

Both column-2 tokens are inside the `## Coverage map` section (`corpus/README.md:5`, next `## ` heading at `:66`) and both name real tracked files:

```
git ls-files corpus/lessons/ | grep -E 'round-4[67]'
corpus/lessons/round-46-verifier-spotcheck.md
corpus/lessons/round-46.md
corpus/lessons/round-47.md
ls -la corpus/lessons/round-46-verifier-spotcheck.md corpus/lessons/round-47.md
-rw-r--r-- 2221 … corpus/lessons/round-46-verifier-spotcheck.md
-rw-r--r-- 6476 … corpus/lessons/round-47.md
```

Content spot-check of the file the row calls "written by the kaika integrator, not the lane": `corpus/lessons/round-46-verifier-spotcheck.md` is a real spot-check (admit row for S003/S006, reject row for S011, both "agree"; `## Adjudication` → `ADMITTED`), its two cited fleet reports exist (`/home/vgpnk/Projects/shokunin/.ufo/waves/kaika-w3/kotoba-review.md`, `kotoba-critic.md`), and `git show --stat c61a973` shows it was added by the integrator commit — the row's "landed at `c61a973` without an index row, indexed round 47" is literally true. `corpus/lessons/round-47.md` is a real lesson file with `## Mistakes` (M20/M21/M22) and `## Gate` (S012–S015 + the C1 class ledger pointer), matching the row's summary.

**No backticked path in either new corpus file is dead** (checked every backticked token containing `/`, resolving repo-relative, corpus-relative, and the `/fast/scratch/kotoba-r47/shared` base): all 20 path-shaped tokens in `corpus/lessons/round-47.md` and the one in `round-46-verifier-spotcheck.md` resolve. The S015 substrate receipt also re-verifies: `cd /fast/scratch/kotoba-r47/shared && sha256sum -c SHA256SUMS` → exit **0**, 4/4 OK, and the quoted prefixes `fdbc8136…` / `179ca421…` match `bin/omp-18.12.5` / `bin/opencode-1.19.3`.

---

## 2. Mutation tests (non-vacuity of the new rows and the re-recorded baseline)

All four mutations were applied to the scratch clone only and reverted; `git diff --stat` was empty afterwards.

| id | mutation | expected | observed |
|---|---|---|---|
| MUT-1 | delete the `\| Round-47 lessons \|` row from `corpus/README.md` | unindexed DRIFT | integrity **exit 1** — `DRIFT corpus.index.unindexed: observed=1`, `unindexed: corpus/lessons/round-47.md` (8/9 pass) |
| MUT-2 | change that row's token to `lessons/round-47x.md` | stale + missing + unindexed DRIFT | integrity **exit 1** — `unindexed=1 stale=1 missing=1`, `missing_paths: corpus/README.md:64: lessons/round-47x.md -> lessons/round-47x.md`; independent **exit 1** — same three DRIFT lines |
| MUT-3 | `verifiers/corpus-baseline.json` `expect` 60 → 61 | tracked_files DRIFT | integrity **exit 1** — `DRIFT corpus.index.tracked_files: observed=60 expected=61` |
| MUT-4 | delete the `\| Round-46 non-author spot-check \|` row | unindexed DRIFT | integrity **exit 1** — `unindexed: corpus/lessons/round-46-verifier-spotcheck.md` |

Both instruments fire on the same class of damage and neither is vacuous: the index rows are load-bearing, the `expect: 60` is a live gate, and the M21 defect the round set out to close is *detectable* by the very gate that was red at BASE.

Operability of the CLI: `--json`, `--self-test`, `--no-baseline`, `--repo <path>` and `--baseline <path>` all work. `--repo /home/vgpnk/Projects/shokunin/kotoba-shokunin` → 9/9 pass exit 0; `--repo <scratch clone>` → 9/9 pass exit 0. The script's default repo is its own grandparent, so it is cwd-independent.

---

## 3. Findings (severity order)

### LOW-1 — the primary instrument's own docstring states an invariant that the round-47 README edit made observably false, and it has no counter for the class

`verifiers/verify_corpus_integrity.py:354-361` (docstring of `file_column_tokens`):

> "No README table outside the section carries a column-2 token today (`index_tokens_outside_coverage_map` was 0 when the independent instrument measured it), so this changes no live number — it makes the claim true and the failure mode impossible."

Three problems at 7ad7fad:

1. **The parenthetical is false.** The independent instrument exposes `index_tokens_outside_coverage_map` (`verifiers/verify_corpus_independent.py:356`) and it is **2** at 7ad7fad — not 0. It was already **1** at BASE `c61a973` (the token `description` on `corpus/README.md:74`). The value 1 is even committed in the round's own receipt: `.ufo/waves/round-47/before/verify_corpus_independent.py.out` → `"index_tokens_outside_coverage_map": 1`.
2. **Round 47 grew the class 1 → 2.** The new `## Frontier` row `corpus/README.md:76` (the "Loader-rule freshness" row rewritten in this round) carries two backticked column-2 tokens *outside* the coverage map: `trigger.no_xml_tag` and `lessons/round-47.md`. Repro:

   ```
   python3 - <<'EOF'   # import verify_corpus_independent.coverage_cells, print outside cells
   ...  # -> line 76 tokens ['trigger.no_xml_tag', 'lessons/round-47.md']
   EOF
   ```
   BASE gives `line 74 -> ['description']`.
3. **The primary instrument silently drops this class.** `file_column_tokens` (`verifiers/verify_corpus_integrity.py:351`, harvest loop at `:363-372`) harvests only rows inside the `## Coverage map` section and the instrument publishes **no** `index_tokens_outside_coverage_map` counter — the `--json` observed block has `index_tokens_fenced` and `index_tokens_excluded` (both named classes) but nothing for "outside". That contradicts the instrument's own stated round-33 rule at `verifiers/verify_corpus_integrity.py:378-382`: "the census harvests EVERY backticked column-2 token and classifies it in `index_findings`; the exclusion is a named class with a counter, never a silent drop at harvest time."

**Impact on verdicts: none.** Outside tokens never contribute to `covered` in either implementation (`verifiers/verify_corpus_independent.py:311-320` builds `outside_tokens` separately and never adds them to `denoted`), so they cannot mask an unindexed file or fake a coverage hit; `unindexed=0` stands on the coverage-map harvest alone. This is a **calibration / audit-gap** defect, not a false-green: the primary instrument's docstring asserts a live invariant ("no table outside the section carries a column-2 token … the failure mode impossible") that the round's own content falsified, and the class it fails to name is the exact class its own rule says must never be dropped silently.

**Repro (one-liner, tip):**
```
cd /fast/scratch/kotoba-r47/w2/W2CorpusRerun/kotoba-shokunin
python3 verifiers/verify_corpus_integrity.py --json | python3 -c "import json,sys;print(sorted(json.load(sys.stdin)['observed']['corpus']))"
# -> no 'index_tokens_outside_coverage_map' key
python3 verifiers/verify_corpus_independent.py --json | python3 -c "import json,sys;print(json.load(sys.stdin)['observed']['index']['index_tokens_outside_coverage_map'])"
# -> 2
```
Suggested fix (not applied — read-only lane): give the integrity instrument the same named counter, and correct the round-12 docstring's factual parenthetical. If the intent is that no README table outside the coverage map may carry a backticked path token, then `corpus/README.md:76` violates that intent and should drop the backticks around `lessons/round-47.md` (or the row moves into the coverage map).

### LOW-2 — the round-47 baseline note uses a different arrow convention from every prior note in the same field, and reads as a false count

`verifiers/corpus-baseline.json:58` (`notes.round47`):

> "corpus.index.tracked_files **58 -> 60**: corpus/lessons/round-46-verifier-spotcheck.md (landed by the integrator at c61a973 without an index row, the round-47 M21 class) and corpus/lessons/round-47.md, both indexed in corpus/README.md. … Expectation refresh for two real indexed files, not a fitted denominator."

Prior notes in the same `notes` object use **observed → observed** ("round37_harness_independent": "tracked_files 53 -> 54"; "round23_capability": "tracked_files 52 -> 53"; "round46_landing": "tracked_files 55 -> 58"). This entry instead uses **expectation → expectation** (58 was the BASE *expectation*, 60 the new one). The observed movement was **59 → 60**, i.e. round 47 added exactly **one** new tracked corpus file (`corpus/lessons/round-47.md`); `corpus/lessons/round-46-verifier-spotcheck.md` was already tracked at BASE — `git diff --stat c61a973 7ad7fad -- corpus/` lists only `QUALITY.md`, `README.md`, `SOURCES.md`, `knowledge/instruction-surface-census-round13.md`, `lessons/round-47.md` (5 files, +169/−10).

The note's substance is right (both files are indexed; it is a real refresh, not a fitted denominator), and a careful reader can reconstruct the history from the parenthetical. But a reader applying the file's established convention reads "two new tracked files" where only one was added by this round. Calibration nit; the same sentence's other numbers (`report_total 40`, `commit_total 29`, the six zero classes) are exactly what I measured.

### LOW-3 (pre-existing, not introduced by round 47) — the baseline's freshness header still names a round-16 tree

`verifiers/corpus-baseline.json` `as_of` = `2026-09-29T01:30:35-03:00`, `measured_against.head` = `d85982d` ("round-16: planner rank-1 discharged …"), `measured_against.git_status` = "round-17 staged working tree …". The round-47 refresh updated `expect` and added `notes.round47` but left the header pointing at a round-16/17 tree. No machine consumer reads it — `evaluate()` (`verifiers/verify_corpus_integrity.py:654`) reads only `baseline["checks"][id]["expect"]` — so this is a human-facing freshness claim only, and it was already flagged by an earlier round (`.ufo/round-21/scouts/F2.md:63` records the same observation). Low severity; noted because a reader taking `as_of`/`measured_against` at face value would read a false "as of" for a file whose expectations are now round-47.

---

## 4. What survived the attack (findings too)

- **C3's corpus half holds.** The re-record is correct, minimal and reproducible: one `expect` changed (58→60), no zero-class expectation touched, and both instruments independently re-derive 60 tracked / 0 unindexed / 0 stale / 0 missing / 40 report pointers / 29 commit citations.
- **The M21 closure is genuine, not a baseline edit.** The gate was genuinely red at BASE (`tracked_files 59≠58`, `unindexed 1`) and the fix is a real index row, not a loosened expectation — MUT-3 shows the `expect` is a live gate, and MUT-1/MUT-4 show both new rows are load-bearing.
- **Both instruments agree without sharing code.** The independent implementation reaches the same 60/0/0/0 and 40/29 from its own tokenizers (`POINTER_RE`/`COMMIT_RE`/`coverage_cells`) — the agreement is a real cross-check, and the two self-tests (150 and 91 assertions) are green.
- **The new corpus content's own citations resolve.** Every backticked path in `corpus/lessons/round-47.md` and `corpus/lessons/round-46-verifier-spotcheck.md` points at a file that exists, and the S015 substrate receipt re-verifies (`sha256sum -c SHA256SUMS` → 4/4 OK).

## 5. What I did NOT check

- I did **not** verify the *substance* of the round-47 lesson's M20/M21/M22 rows beyond their pointer existence and the M21 instrument reproduction (the M20 stale-premise re-derivation and M22's `SCORECARD.md` line drift are other lanes' scope); I only re-ran M21's stated commands.
- I did **not** audit `corpus/knowledge/instruction-surface-census-round13.md` (§ B′) or `corpus/SOURCES.md` S012–S015 / `corpus/QUALITY.md` Q19 content, nor the C1 surface/pin re-derivation (omp 18.12.5 / opencode 1.19.3) — out of this lane's scope. I only re-verified the shared-substrate SHA256SUMS receipt that S015 cites.
- I did **not** re-derive the 38 host-absolute report pointers individually; I relied on the instruments' `report_dead=0` plus my own confirmation that the pointer class is unchanged between BASE (38 absolute / 1 relative / 1 tilde) and tip (identical shapes) and that `report_total` is 40 at both.
- I did **not** check the `corpus/README.md` `## Frontier` / `## Known gaps` tables for path tokens other than the one class identified in LOW-1 (no other table row outside the coverage map carries a backticked column-2 token; that IS the LOW-1 census).
- I did **not** test the corpus instruments against a *dirty* working tree (untracked/modified corpus files) or against a repo with a corrupted git index; my runs are on clean detached checkouts of `7ad7fad`, `c61a973` and `04192c2`.
- I did **not** re-run the fault harness (`verifiers/` harness claims), the checklist gate, the surfaces verifier or the pins guard — other lanes' scope. I did read `.ufo/waves/round-47/before/SUMMARY.md` and `before/verify_corpus_*.py.out` and found them consistent with my independent measurements.
- No tool was installed, upgraded or removed by this lane (python3 + git from the base image sufficed); no pacman transaction was attempted.

## 6. Recommendation

**Accept** the round-47 corpus landing (C3 corpus half) — the gate is green on substance, the baseline is honest, the two new index rows name real files, and the gate is demonstrably non-vacuous. **Fold in LOW-1** (name the outside-coverage-map class in the primary instrument and correct the falsified round-12 parenthetical at `verifiers/verify_corpus_integrity.py:354-361`), and fold LOW-2's wording fix into the next append-only baseline note. LOW-3 is a pre-existing debt, not a round-47 blocker.
