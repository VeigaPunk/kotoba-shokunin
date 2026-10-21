verdict: HOLDS — attacked `verifiers/corpus-baseline.json` `corpus.index.tracked_files` 58→60 as a fitted denominator (population, index coverage, committed unindexed-file and missing-file plants)

Role: critic (W2CorpusBaselineFit), lane-authored review only, not non-author closure. Every check below was run in the scratch clone `/fast/scratch/kotoba-r47/w2/W2CorpusBaselineFit/kotoba-shokunin` at `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`, with fleet symlinks in the canonical layout. Plants were committed in per-plant worktrees of that clone. Nothing was written to production files.

## Findings

**F1: 60 is exactly the tracked corpus population at the tip, not a fitted value. (Survives.)**
- `verifiers/corpus-baseline.json:15` sets `"expect": 60`. The instrument counts rows of `git ls-files corpus/` (`verifiers/verify_corpus_integrity.py:6`, `:547-552`, `:571`) and compares them with `equal` mode (`:630`).
- `git ls-files corpus | wc -l` gives 60 at the tip and 59 at BASE `c61a973`. The integrity JSON at the tip reports `tracked_files: 60`, and the independent instrument also reports `tracked_files: 60`, derived by its own code path (`verifiers/verify_corpus_independent.py:354`).
- The +2 decomposes into two real files:
  - `git diff --name-status c61a973 7ad7fad -- corpus` shows exactly one `A`, `corpus/lessons/round-47.md`. The other changes are four `M` lines (QUALITY, README, SOURCES, census13).
  - The second file, `corpus/lessons/round-46-verifier-spotcheck.md`, was added by `c61a973` itself (`git log --diff-filter=A`).
- At BASE, integrity exits 1 with `tracked_files` 59≠58 `DRIFT` and `unindexed` 1 (`corpus/lessons/round-46-verifier-spotcheck.md`), and independent also exits 1. This reproduces the M21 premise (`corpus/lessons/round-47.md:20`) and the round-47 note's account (`verifiers/corpus-baseline.json:58`).

**F2: Each new file is indexed by its own explicit coverage-map row; no glob or incidental coverage. (Survives.)**
- I recomputed coverage with the instrument's own `file_column_tokens` and `expand_pattern`:
  - The coverage map contains zero glob tokens.
  - `lessons/round-46-verifier-spotcheck.md` is covered only by `corpus/README.md:63`.
  - `lessons/round-47.md` is covered only by `corpus/README.md:64`.
  - The only uncovered tracked file is `README.md` itself, which is exempt by design.
- Removing coverage turns the gate red: plant P9 fences the `:64` row in a code block, and both instruments report `unindexed=['corpus/lessons/round-47.md']` with exit 1. So the rows are load-bearing, not decorative.
- The row claims hold:
  - `round-47.md` has `## Mistakes` (`:12`) with 3 M20–M22 rows and `## Gate` (`:27`) with 4 S012–S015 rows.
  - The spot-check file carries S003/S006 admit and S011 reject, both marked "agree" (`corpus/lessons/round-46-verifier-spotcheck.md:12-13`), and `ADMITTED` (`:17`).
  - All 11 `.ufo/waves/round-47/...` paths cited from the lesson and README resolve in the `7ad7fad` tree (`git cat-file -e`).

**F3: The note's "report_total 40 / commit_total 29 unchanged" holds.**
- BASE gives `report_total` 40, `commit_total` 29, `index_patterns` 76. The tip gives 40, 29, 78.
- The new `c61a973` and `36ab0d3` mentions don't count as commit tokens because `COMMIT_RE` matches only ``commit `hex` `` (`verifiers/verify_corpus_integrity.py:146`), and the new text never uses that form. That is consistent with the instrument's grammar, not an evasion.

**F4: Required plants. Both red, in both instruments.**
- **P1: a committed, tracked corpus file with no index row** (`corpus/knowledge/w2cbf-unindexed.md`, plant commit `3fce0ee`). Integrity exits 1 with `tracked_files=61 DRIFT` and `unindexed=1 DRIFT`. Independent exits 1 with `unindexed=1`.
- **P2: a committed coverage-map row for a missing file** (`` `knowledge/w2cbf-gone.md` `` at README:65, plant commit `fcb4885`). Both instruments exit 1 with `stale_patterns=1` and `missing_paths=1`.

**F5: Count-neutral attacks on the equality denominator. The zero-mode checks catch what equality cannot.**
- **P3, swap:** `git rm` of `lessons/round-47.md` with its row kept, plus a new unindexed file, committed. `tracked_files` stays 60 and equality PASSes. Both instruments still exit 1 on `unindexed=1`, `stale_patterns=1` and `missing_paths=1`.
- **P4, honest rename:** the file is moved and its row repointed. Both instruments exit 0, which is correct.
- **P5, honest growth:** a new file with a row. Integrity exits 1 on `tracked_files=61 DRIFT` alone; independent exits 0. This is the intended forcing function for an explicit baseline refresh, as round 47 did.

**F6: Pre-existing blind spots, not introduced by round 47.** Both verifier files are byte-unchanged BASE..tip; the diff `--stat c61a973 7ad7fad -- verifiers/` does not list either one.
- **P6, unbackticked row:** a coverage-map row naming a missing file without backticks (`| W2CBF plant P6 | knowledge/w2cbf-gone-plain.md | … |`). Both instruments exit 0. Both harvest only backticked column-2 tokens (`verify_corpus_integrity.py:378`, `verify_corpus_independent.py:309`). The lane's index grammar is "backticked column-2 token", so this is a grammar boundary, not a gate defect. It is low severity and not listed in `corpus/README.md` § Known gaps (`:79-118`).
- **P7, the instruments disagree:** a missing-file row whose token carries a placeholder mark (`` `knowledge/w2cbf-gone-<lane>.md` ``). Integrity exits 0 because the token is a named, counted exclusion (`verify_corpus_integrity.py:214-217`; it counts toward `index_tokens_excluded`, which no check gates). Independent exits 1 with `stale_patterns=1` and `missing_paths=1`, because it has no placeholder exclusion for index tokens (`verify_corpus_independent.py:320-346`).
  - The combined battery still goes red.
  - The divergence is undocumented in Known gaps.
  - Smallest safe correction (for the integrator, not this round's claim): name it in § Known gaps, or gate `index_tokens_excluded` with `equal` mode, currently 0.
- **P8, untracked file:** a file on disk in `corpus/` that was never `git add`ed. Both instruments exit 0. The population is defined as tracked files, so this is the stated design, not a defect.

**F7: Calibration nit (pre-existing pattern).**
- The top-level `measured_against` block still names `head: d85982d` and the round-16 tree (`verifiers/corpus-baseline.json:5-11`), while `expect` values now reflect `7ad7fad`.
- The `round47` note (`:58`) says "the round-47 integration tree" without naming a commit or tree hash. The round-46 note named `78ee57e`.
- The values are reproducible at `7ad7fad` (F1), so this affects provenance precision only, not the number.

## Commands run (exit codes)
- `python3 -B verifiers/verify_corpus_integrity.py --json` at the tip: exit 0, 9/9 PASS, `tracked_files` 60, `unindexed` 0.
- `python3 -B verifiers/verify_corpus_independent.py --json` at the tip: exit 0, `tracked_files` 60 (INFO), `unindexed` 0.
- The same two commands at BASE `c61a973` (worktree): exit 1 and exit 1 (`tracked_files` 59≠58, `unindexed` 1).
- `python3 -B verifiers/verify_corpus_integrity.py --self-test`: exit 0, "0 failure(s) over 150 assertions".
- `python3 -B verifiers/verify_corpus_independent.py --self-test`: exit 0, "91 assertions, 0 failures".
- `bash verifiers/fault_injection_corpus.sh --repo .` at the tip: exit 0, `verdict: ALL PASS`.
  - Faults a–e fire on the expected class in both instruments.
  - Fault f is a documented blind spot (control 40, plant 39, baseline-mode exit 1).
  - Faults g and h do not fire.
  - The round-47 planter fix (rows inserted inside `## Coverage map`, `verifiers/fault_injection_corpus.sh:117-119`) is what keeps d1/d2 rows inside the map now that a `## Frontier` table follows it.
- `bash plants.sh` (P0–P9), output in `W2CorpusBaselineFit.plants-out.txt`.

## Repro
Run `bash .ufo/waves/round-47/falsify/W2CorpusBaselineFit.plants.sh.txt`. It is self-contained: it creates worktrees under `/fast/scratch/kotoba-r47/w2/W2CorpusBaselineFit/worlds/<id>` from the scratch clone at `7ad7fad`, plants and commits, then runs both gates. To use it elsewhere, edit `ROOT`/`SRC`.

## Artifacts
- `.ufo/waves/round-47/falsify/W2CorpusBaselineFit.plants.sh.txt`: the plant script.
- `.ufo/waves/round-47/falsify/W2CorpusBaselineFit.plants-out.txt`: the observed output for P0–P9.

## Not checked
- The C1/C2 claims (surfaces, pins, `trigger.no_xml_tag`), GOVERNANCE_ERRATA, LOG/SCORECARD/PROVINCE records, and S012–S015 source re-opens are outside this assignment.
- Whether the other 58 README rows' column-3 prose is accurate; I checked only rows 63–64.
- `jj` state of the lane repo.
- Timing: self-tests took about 300 s wall-clock under host load. No other observations.

Tooling installs/updates: none.
