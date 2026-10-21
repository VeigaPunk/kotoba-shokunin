verdict: BASE recorded at c61a973 (integrity DRIFT 2: tracked_files observed 59 vs expected 58, and round-46 unindexed; independent DRIFT 1); the simulated pair re-records tracked_files 58->61 (+ report_total 40->42 and commit_total 29->31 if it cites a pointer and a commit each); NOT yet no-harm: independent --self-test exits 1 under /tmp pressure, and the two instruments disagree on ellipsis/glued/bracket pointers and spaced commit tokens, so a re-recorded baseline can pass with three dead pointers.

# ExecCorpusBaseline: corpus verifier no-harm baseline at BASE c61a973

Scope: `verifiers/verify_corpus_integrity.py` and `verifiers/verify_corpus_independent.py` at BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`. Every run used scratch clones (`/fast/scratch/kotoba-r47/ExecCorpusBaseline/{lane,simA,simB,simC,simU}`, detached at BASE). The production repo was read, never written, and no git or verifier command ran in it. Installs: none. `sudo` was used only for `mount -t tmpfs` / `umount` of 24 KiB scratch test mounts; all were unmounted and removed (verified: 0 mounts left). Environment: `/usr/bin/python3` 3.14.8, git 2.56.0. Path citations are at BASE unless marked.

## 1. BASE record

### 1.1 Commands, exits, runtimes, heads

| command (cwd = lane) | exits (3 runs) | runtime s | head printed |
|---|---|---|---|
| `python3 -B verifiers/verify_corpus_integrity.py --self-test` | 0,0,0 | 0.045 / 0.043 / 0.039 | none; `self-test: 0 failure(s) over 150 assertions` |
| `python3 -B verifiers/verify_corpus_integrity.py --json` | 1,1,1 | 0.100 / 0.099 / 0.096 | none (JSON holds `observed.corpus` and `results`) |
| `python3 -B verifiers/verify_corpus_integrity.py` (text) | 1,1,1 | 0.097 / 0.116 / 0.113 | none |
| `python3 -B verifiers/verify_corpus_independent.py --self-test` | 0,1,0 (flake, F1) | 0.208 / 0.086 / 0.222 | none |
| `python3 -B verifiers/verify_corpus_independent.py --json` | 1,1,1 | 0.212 / 0.203 / 0.228 | `"head": "c61a973"` |
| `python3 -B verifiers/verify_corpus_independent.py` (text) | 1,1,1 | 0.237 / 0.226 / 0.227 | `HEAD c61a973` (render, `verify_corpus_independent.py:512`) |

- Outputs were byte-identical across the three runs for every command except the independent self-test, which failed once.
- Exit controls: integrity `--no-baseline` exit 1 (`8/9 checks pass; DRIFT: corpus.index.unindexed`); integrity `--baseline /nonexistent --json` exit 3 (F6); integrity `--repo <non-git dir>` exit 2; independent `--repo <non-git dir>` exit 2 (`environment unreadable: not a git repository`).
- `git status --porcelain` in the lane was empty before and after the run batch. Both verifiers write nothing (`-B` also avoids `__pycache__`).
- The BASE numbers match the before-values in `plans/round-47.md:37-38` and `.ufo/waves/round-47/before/SUMMARY.md:7-8`.

### 1.2 Integrity gate at BASE (`--json`, baseline `verifiers/corpus-baseline.json`)

| check | mode | expect (baseline) | observed | verdict |
|---|---|---|---|---|
| corpus.index.tracked_files | equal | 58 (`corpus-baseline.json:15`) | 59 | DRIFT |
| corpus.index.unindexed | zero | 0 | 1 (`corpus/lessons/round-46-verifier-spotcheck.md`) | DRIFT |
| corpus.index.stale_patterns | zero | 0 | 0 | PASS |
| corpus.index.missing_paths | zero | 0 | 0 | PASS |
| corpus.pointers.report_total | equal | 40 (`:31`) | 40 | PASS |
| corpus.pointers.report_dead | zero | 0 | 0 | PASS |
| corpus.pointers.commit_total | equal | 29 (`:39`) | 29 | PASS |
| corpus.pointers.commit_unresolvable | zero | 0 | 0 | PASS |
| corpus.pointers.commit_nonhash | zero | 0 | 0 | PASS |

Auxiliary observed values: tracked 59 (`git ls-files corpus/`), corpus md 58, FILE-column patterns 76, report pointers shapes relative 1 / absolute 38 / tilde 1 / bare 0, excluded 8 (all `<lane>` / `<repo>` placeholders), quoted 0; commit citations 29 (all hex, all resolvable), quoted-excluded 2 (`corpus/knowledge/claim-census-round12.md:95`, `corpus/lessons/round-6-aggregator-audit.md:45`).

### 1.3 Independent instrument at BASE (`--json`; no baseline, zero-mode gates only)

| check | mode | observed | verdict |
|---|---|---|---|
| corpus.index.tracked_files | observe | 59 | INFO |
| corpus.index.unindexed | zero | 1 | DRIFT |
| corpus.index.stale_patterns | zero | 0 | PASS |
| corpus.index.missing_paths | zero | 0 | PASS |
| corpus.pointers.report_total | observe | 40 (candidates 48, excluded 8, quoted 0, dead 0) | INFO |
| corpus.pointers.report_dead | zero | 0 | PASS |
| corpus.pointers.commit_total | observe (`commit_hex_total`) | 29 (citations 29, quoted 2) | INFO |
| corpus.pointers.commit_unresolvable | zero | 0 | PASS |
| corpus.pointers.commit_nonhash | zero | 0 | PASS |

Index tokens 76 (the same as integrity); one backticked token outside the coverage map (`corpus/README.md:74`, `description`), which only the independent instrument counts. On all nine values the two instruments agree at BASE.

### 1.4 Why BASE drifts

Commit `c61a973` changed only `corpus/lessons/round-46-verifier-spotcheck.md` (+17 lines, `git show --stat`). It added no README row and no baseline re-record. The last re-record is the round-46 note at `verifiers/corpus-baseline.json:57`. The plan's before-values are therefore correct, and this is the C3 index-row and re-record debt.

## 2. Simulation: two new files plus README rows (git add in the clone)

The assignment's state is B1. Each state below is cumulative from BASE in clone `simB` unless noted. New tracked files were `git add`-staged (the gate reads the index); the B4 target and the B5 file were deliberately left untracked. Full JSON: `ExecCorpusBaseline.sim.json`.

| state | integrity exit | integrity DRIFT (expect != observed) | I tracked / unindexed / report_total (dead) / commit_total (nonhash) | independent exit | N tracked / unindexed / checked (dead) / citations (nonhash) |
|---|---|---|---|---|---|
| A: BASE + round-46 index row only (clone simA) | 1 | tracked (expect 58, got 59) | 59 / 0 / 40 (0) / 29 (0) | 0 | 59 / 0 / 40 (0) / 29 (0) |
| B0: BASE | 1 | tracked, unindexed | 59 / 1 / 40 (0) / 29 (0) | 1 | 59 / 1 / 40 (0) / 29 (0) |
| B1: + `knowledge/x.md`, `lessons/round-47.md`, 2 rows (assignment) | 1 | tracked (expect 58, got 61), unindexed | 61 / 1 / 40 (0) / 29 (0) | 1 | 61 / 1 / 40 (0) / 29 (0) |
| B2: B1 + round-46 row | 1 | tracked (expect 58, got 61) | 61 / 0 / 40 (0) / 29 (0) | 0 | 61 / 0 / 40 (0) / 29 (0) |
| B3: both new files cite `../../.ufo/reports/round-47/kotoba.md` (absent) and `commit c61a973b...` | 1 | tracked, report_total, report_dead, commit_total | 61 / 0 / 42 (2) / 31 (0) | 1 | 61 / 0 / 42 (2) / 31 (0) |
| B4: the pointer target now exists, untracked | 1 | tracked, report_total, commit_total | 61 / 0 / 42 (0) / 31 (0) | 0 | 61 / 0 / 42 (0) / 31 (0) |
| B4r: B4 with expect 61 / 42 / 31 (`--baseline`) | 0 | none | 61 / 0 / 42 (0) / 31 (0) | 0 | same |
| B5: + unstaged `corpus/knowledge/untracked-y.md` with a dead pointer | 1 | tracked, report_total, commit_total | 61 / 0 / 42 (0) / 31 (0) | 0 | 61 / 0 / 42 (0) / 31 (0) |
| B6: + `commit `round-47`` and `commit `round 47`` and capital `Commit `<sha>`` | 1 | + commit_nonhash | 61 / 0 / 42 (0) / 31 (2) | 1 | 61 / 0 / 42 (0) / 32 (nonhash 1; hex 31) |
| B7: + ellipsis, glued and bracket-link pointers, targets absent | 1 | tracked, report_total, commit_total | 61 / 0 / 42 (0) / 31 (0); excluded 11 | 1 | 61 / 0 / 45 (3) / 31 (0); excluded 8 |
| C: B7 with expect 61 / 42 / 31 (clone simC) | **0** | none | as B7 | **1** | as B7 (report_dead 3) |
| B8: staged then deleted from the worktree | 2 | n/a | INCONCLUSIVE | 2 | environment unreadable |

Observed in B1: `corpus/README.md` rows at lines 63-64 are inserted after the round-46 row (`corpus/README.md:62`). Both new files are covered (`unindexed` stays 1 from the round-46 file alone).

### 2.1 Which baseline numbers must be re-recorded

1. `corpus.index.tracked_files`: 58 -> 59 at BASE, which is owed now. Verified: state A plus expect 59 gives integrity exit 0 with all nine PASS, and independent exit 0 (`ExecCorpusBaseline.c3-row-rerecord59.json`). With the simulated pair it goes 58 -> 61 (B1, and B4r).
2. `corpus.pointers.report_total`: 40 -> 42 and `corpus.pointers.commit_total`: 29 -> 31, but only if the two files carry the usual `.ufo/reports/...` pointer and a `commit <hex>` citation each (B3, B4r). With no citations (B1) both stay 40 / 29.
3. Zero-mode expectations are not re-recorded; they must stay 0. The pair adds no `unindexed` because its two rows cover both files. Any dead pointer makes `report_dead` nonzero with exit 1 whatever the baseline says (B3).
4. Observation-only numbers that the baseline notes historically recorded but no gate reads: `index_patterns` 76 -> 78 for the pair (79 with the round-46 row) and corpus md files 58 -> 60.
5. Documentation: `verifiers/corpus-baseline.json:2` (`as_of` 2026-09-29) and `:4-10` (`measured_against.head` d85982d) are stale. No verifier reads them for the corpus (the only corpus readers are `verify_corpus_integrity.py:666`, which reads `checks[*].expect`, and `fault_injection_corpus.sh:81-82`, which copies the file). Add a round-47 note under the existing convention.

## 3. Findings

**F1: independent `--self-test` exits 1 with an uncaught traceback when temp space runs out (operability; reproduced).**
- Mechanism. `_git` (`verify_corpus_independent.py:62-65`) returns the CompletedProcess unchecked. `_git_init` (`:571-574`) ignores the rc of `git init` and `git add`. Under ENOSPC, `git init` exits 128 and leaves a partial `.git` (measured: `error: copy-fd: write returned: No space left on device`; `.git/hooks` only, no HEAD). The next `corpus_markdown` call then raises `EnvError` from `tracked_paths` (`:84-85`), which has no handler inside `self_test` (call site `:848-849`). `main` calls `self_test()` outside its `try` (`:984-985`, versus `:986-990`), so Python exits 1. The contract at `:29` says 2 means an unreadable environment.
- Evidence. A 12-run loop produced `1,1,0,1,1,1,1,1,1,1,1,1`. Each of the 11 failures printed `EnvError: git ls-files failed: fatal: not a git repository (or any parent up to mount point /)` at line 849. `df -h /tmp` read 2.0M available (100%) during that window. The 3-run set at the start gave `0,1,0`. In a 24 KiB tmpfs with the directory empty, the self-test exits 1 with the same traceback (reproduced twice). The integrity self-test on the same tmpfs exits 0 with 150 assertions, because it creates no fixtures on disk. Runs with `TMPDIR` on `/fast` (763,679 MiB free) gave 10/10 exit 0, and runs with `/tmp` at about 16.9 GiB free gave 10/10 exit 0.
- Tempfile routing. With the tmpfs filled to 0 bytes, `tempfile.gettempdir()` returns `/tmp`, because the candidate write test fails with ENOSPC. The self-test then passes. The failure therefore depends on which candidate directory has free bytes at that instant (`ExecCorpusBaseline.tmpfs-fallback.json`).
- Footprint. A self-test run makes 12 `git init` calls, 62 `_git` calls and 13 `add` calls (measured by wrapping `_git` in-process). Each `.git` is 84 KiB. That puts the transient at about 1 MiB per run [INFERENCE from those two measurements].
- Count. 14 of 41 self-test invocations at BASE exited 1: 11 in the 12-run loop, 1 in the first set, and 2 of the 4 tmpfs runs. None failed in the 20 runs made with at least 16.9 GiB free.
- Context. `/tmp` had a directory link count of 6,142 (about 6,140 subdirectories) at the time. I did not identify the writer and deleted nothing.

**F2: non-ASCII corpus filenames give false red in both instruments (operability; reproduced in clone simU).**
- `git ls-files` C-quotes `café.md` as `"corpus/knowledge/caf\303\251.md"`. Neither instrument strips the prefix from the quoted name (integrity `tracked_corpus_files` `:547-552`; independent `tracked_paths` `:81-86`, `corpus_markdown` `:89-90`, `analyse_index` `:317`). The result with a correct README row is integrity: tracked 61, unindexed 2 (one detail reads `corpus/"corpus/knowledge/caf\303\251.md"`), stale 1 (`corpus/README.md:64`), exit 1. Independent: stale 1, unindexed 1, exit 1.
- BASE is unaffected (`git ls-files corpus | grep -c '"'` = 0). The fix is `git ls-files -z` (or `core.quotePath=false`, which still quotes tabs and quotes); see recommendations.

**F3: ellipsis, glued-prose and bracket-link pointers are read differently by the two instruments (calibration; reproduced in state C).**
- Integrity: `is_excluded_pointer` (`verify_corpus_integrity.py:267-279`) excludes any token whose path segment contains `..` as a substring (`:279`), so `corpus/.../` and `x../` are exempt, as its own docstring intends (`:76-79`). `has_glob` (`:199-200`) treats `[` as a glob character (`GLOB_CHARS`, `:126`), so `[link](.ufo/...)` is exempt as a "glob".
- Independent: `has_dotdot_after_hops` (`verify_corpus_independent.py:174-178`) matches the segment `..` exactly, so `...` and `x..` are checked promises. `pointer_exclusion` (`:181-191`) has no bracket rule.
- Result. In state C, with the baseline re-recorded to 61/42/31, integrity reports `report_dead` 0 and `report_pointers_excluded` 11 and exits 0. Independent reports `report_dead` 3 (`corpus/lessons/round-47.md:5`) and exits 1. The corpus is identical in both runs.
- BASE has no live instance (both excluded counts are 8, all placeholders), so this is latent. It is still a gate-relevant gap: a dead pointer written in a schematic-looking form passes the primary once the counts are re-recorded. Which reading is intended is a decision for the lane, not something this check can settle.

**F4: spaced commit tokens are counted by one instrument only (calibration; probe and state B6).**
- `commit `round 47`` is a nonhash citation for integrity (`COMMIT_RE`, `verify_corpus_integrity.py:146`, `[^`\n]+`), so it trips `commit_nonhash` and exits 1. Independent's `COMMIT_RE` (`verify_corpus_independent.py:103`, `[^`\s]+`) does not match it at all. B6 shows integrity `commit_nonhash` 2 against independent 1.

**F5: `commit_total` means different things in the two instruments (calibration; naming trap).**
- Integrity counts hex citations only: nonhash citations `continue` at `:491-493`, before `commit_total += 1` at `:494`. Independent counts every citation in `commit_total`: `citations.append` at `:421`, `"commit_total": len(citations)` at `:430`. B6 gives 31 against 32. The comparable independent field is `commit_hex_total`. Anyone diffing the two JSON files by key name will see a false disagreement, or miss a real one.

**F6: a missing baseline file hides zero-mode violations behind exit 3 (calibration).**
- `if baseline is None and not args.no_baseline: ... return 3` (`verify_corpus_integrity.py:1315-1318`) runs before `return 1 if drift else 0` (`:1325`). `--baseline /nonexistent --json` exits 3 with `corpus.index.unindexed` observed 1 and verdict DRIFT (`ExecCorpusBaseline.exit-controls.json`). The docstring at `:91-92` says a zero violation "still exits 1". That holds with `--no-baseline` but not with a missing file.

**F7: the tracked set is the index, not the working tree (calibration; docstring).**
- Both instruments take the tracked set from `git ls-files` (integrity `:547-552`; independent `:81-86`). Integrity's docstring says "Both families are read from the working tree, not from HEAD" (`verify_corpus_integrity.py:45-46`). That is true only for file contents.
- B5: an unstaged corpus file with a dead pointer is invisible to both (`report_dead` 0, tracked unchanged). Deleting a staged file from the worktree (B8) gives exit 2 in both, which is correct fail-closed behaviour.

**F8: pointer targets resolve against the working tree (calibration).**
- B4: a pointer whose target exists only untracked passes (`report_dead` 0). A committed pointer to an uncommitted report is therefore green locally. Nothing in the gate proves the target is committed.

**F9: the baseline is stale by one at BASE, and its metadata is stale too (freshness).**
- `expect` 58 against 59 tracked (`corpus-baseline.json:15`, F1 of section 2). Header `as_of` 2026-09-29 (`:2`) and `measured_against.head` d85982d (`:6`) describe round 16 / 17. The notes block (`:50-57`) is the only current record.

**F10: capitalised `Commit `<sha>`` escapes both commit gates (shared blind spot).**
- Both regexes are case-sensitive (integrity `:146`, independent `:103`). In the differential, `Commit `c61a973`` gives 0 citations from both instruments (`ExecCorpusBaseline.differential.json`, row `Commit-capital`).

**F11: whitespace-bearing pointers are seen by one instrument only (observation, not gated).**
- Integrity's `UFO_POINTER_RE` (`verify_corpus_integrity.py:141-143`) cannot match across whitespace, so such tokens are never seen. Independent counts them as `whitespace` exclusions (`verify_corpus_independent.py:187-188`). Only the excluded count differs (differential rows `ptr-space-in-name`, `ptr-space-middle-dir`).

**Differential summary.** 30 probe lines were run through both instruments' tokenizers, using real `git cat-file` for resolution (`ExecCorpusBaseline.differential.json`). There were 6 disagreements: `commit `round 47``, the ellipsis, the glued prose, the spaced pointer names (two rows) and the markdown link. The two instruments agree on all other shapes, including quoted context, placeholders, globs, uppercase hex and the 7/40-hex boundary.

**Positive controls that held.** Exit 0 and exit 1 match the documented codes. Exit 2 appears in both (B8, and `--repo` on a non-git directory). The integrity self-test is deterministic and independent of disk state.

## 4. Freshness, operability, calibration

- Freshness: the baseline is one file behind at BASE (F9). Its metadata is stale. The plan's before-values are right, and the C3 index row plus re-record clears both DRIFTs (A+59 gives exit 0).
- Operability: the independent self-test flakes on /tmp pressure with an exit code that means something else (F1). Non-ASCII filenames cause false red (F2). The missing-baseline path returns 3 even when a zero-mode violation exists (F6).
- Calibration: the instruments disagree on six probe shapes (F3, F4, F5, F11). A re-recorded baseline can pass dead pointers the independent instrument catches (F3, state C). Unstaged files and capitalised citations are invisible in both (F7, F10).

## 5. Recommendations (not implemented here; for the integrator)

1. `verify_corpus_independent.py`: make `_git` / `_git_init` raise `EnvError` on rc != 0, and have `self_test` return 2 on `EnvError`. This mirrors integrity's fail-closed `git()` (`verify_corpus_integrity.py:523-536`). Also give the self-test a private, checked temp dir (F1).
2. Reconcile pointer exclusion in both instruments: one shared rule for ellipsis, glued and bracket shapes, with counters and a fixture in each. Decide "promise or schematic" explicitly (F3).
3. Give both commit regexes one rule for internal whitespace and for case (F4, F10). Rename the independent JSON `commit_total` to `commit_citations`, and compare `commit_hex_total` for parity (F5).
4. Return 1 when a zero-mode DRIFT is present even with no baseline, or change the docstring at `:91-92` to say exit 3 masks it (F6).
5. Use `git ls-files -z` in both instruments and parse NUL-separated names (F2).
6. Correct the docstring at `verify_corpus_integrity.py:45-46`: the tracked set is the index (F7).
7. Refresh or drop `as_of` and `measured_against` in `corpus-baseline.json`, and add a round-47 note when re-recording (F9).
8. C3: add an index row for `corpus/lessons/round-46-verifier-spotcheck.md` after `corpus/README.md:62`, and re-record `tracked_files` to 59. Verified: exit 0 for both instruments.
9. For the simulated pair: re-record `tracked_files` 58 -> 61 (59 -> 61 if C3 lands first). Re-record `report_total` 40 -> 42 and `commit_total` 29 -> 31 only if the files carry those citations, and make sure the cited targets are committed.

## 6. What I did NOT check

- The production working tree and HEAD. No git or verifier command ran there, so I cannot say whether production has moved past BASE.
- Other gates: `verify_harness_claims.py`, `verify_surfaces.py`, `check_substrate_pins.py`, `verify_skill_checklist.py`, and `fault_injection_corpus.sh` (which copies `corpus-baseline.json` into its workspace, `:81-82`, and was not run).
- The source and timeline of the /tmp fill. I took only `df` and `shutil.disk_usage` snapshots and no per-run free-space trace. The root cause of F1 is established by the ENOSPC replays and the failing window, not by a captured fill event.
- Symlinks, CRLF line endings, submodules, file modes, non-default `core.quotePath`, and `-z` parsing (the proposed fix is untested).
- jj-colocated state. The clones are plain `git clone --no-hardlinks` copies, so the git object set and the index behaviour are assumed to match production. The integrity gate found 0 unresolvable commits in the clone.
- Whether the ellipsis, glued and bracket shapes are intended promises. That is a lane decision.
- Concurrent writes during a run, and Python versions other than 3.14.8.
- The optional labrat probe. It was not needed and not spawned.

## 7. Artifacts (all under `.ufo/waves/round-47/build/`)

- `ExecCorpusBaseline.md`: this report.
- `ExecCorpusBaseline.base-integrity.json` (3,522 B) and `.base-independent.json` (3,313 B): the BASE `--json` outputs.
- `ExecCorpusBaseline.base-runs.json` (2,938 B): the run matrix, the flake sequences and the /tmp readings.
- `ExecCorpusBaseline.selftest-git-count.json` (147 B): 12 `init`, 62 `_git`, 13 `add` per self-test.
- `ExecCorpusBaseline.flake.json` (564 B) and `.tmpfs-fallback.json` (227 B): the 24 KiB tmpfs replays and the `gettempdir` fallback.
- `ExecCorpusBaseline.sim-B1.patch` (1,695 B): the assignment's simulation, two new files plus two README rows.
- `ExecCorpusBaseline.sim.json` (12,890 B): `B_states` lists every measured state, A first, then B0 to B8; `C_ellipsis_glued_link` holds state C.
- `ExecCorpusBaseline.c3-row-rerecord59.json`: the state A plus expect-59 check.
- `ExecCorpusBaseline.differential.json` (18,954 B): 30 probe shapes, 6 disagreements.
- `ExecCorpusBaseline.unicode-probe.json` (903 B): F2.
- `ExecCorpusBaseline.exit-controls.json` (1,264 B): exits 2 and 3 controls, and F6.
