# NoHarmGates — round-50 falsify, no-harm check

**Verdict: HOLDS-BOUNDED.** Applies to head 956ee1676e4c18480bce8ac3993541462be76e11 measured against base f30464660c675d1c1e2851a3bf0366a3aaffe5a8. Across the 15 lane gates in the assignment, zero gates are green at base and red at head. Bounds: three gates are red at both revisions from host state; the census `--skill` arm does not exist at base (exit 2, so that row is "absent", not "green"); and the fleet root `.git` changed at 13:34:06Z during my run, which I could not attribute (finding 3).

Run window: 13:33:47Z to about 13:37Z, 2026-10-22. Scratch root: `/fast/scratch/hyaku/kotoba-r50/falsify/NoHarmGates` (`base/`, `head/`, `logs/<rev>/<gate>.log`, `summary.json`). Python 3.14.8 as shipped. No tool installed or upgraded. No web source opened. No git or jj write in the lane, the fleet root, or any sibling repo.

## Setup

- Two private clones made with `git clone` from the lane, then `git checkout -q`: `base/fleet/kotoba-shokunin` at f3046466, `head/fleet/kotoba-shokunin` at 956ee167. `rev-parse HEAD` confirmed both.
- Fleet shape: `.ufo` and `PROTOCOL.md` were copied into each `fleet/` directory, not linked, so verifier writes stay in scratch. The other fleet entries are symlinks. `check_sibling_census` reads the live sibling repos at `/home/vgpnk/Projects/shokunin` (its default `--fleet`) through `git show` only.
- Each gate ran from its own revision's clone with that revision's verifiers, using `python3 -B` from the clone root.

## Table: command, base exit and summary, head exit and summary

Summary is the last line of the log, or the named line where it says so. Logs are in `logs/base/` and `logs/head/`.

| # | command | base rc / summary | head rc / summary | verdict |
|---|---|---|---|---|
| 1 | `verifiers/verify_skill_checklist.py --json` | 0 / pass 11 fail 0 na 0 | 0 / pass 11 fail 0 na 0 | green to green |
| 2 | `verifiers/verify_skill_checklist.py --self-test` | 0 / 0 failure(s) over 1845 assertions | 0 / 0 failure(s) over 1851 assertions | green to green |
| 3 | `verifiers/verify_corpus_integrity.py --json` | 1 / 4 DRIFT: tracked_files 67 vs 66, unindexed 1, report_total 44 vs 43, report_dead 2 | 1 / 1 DRIFT: report_dead 2 | red to red, improved |
| 4 | `verifiers/verify_corpus_independent.py` | 1 / DRIFT unindexed=1, DRIFT report_dead=2, exit 1 | 1 / DRIFT report_dead=2, exit 1 | red to red, improved |
| 5 | `verifiers/check_assertion_floors.py` | 0 / 10 PASS lines (checklist 1845, dispatch 32, others unchanged) | 0 / 11 PASS lines (checklist 1851, dispatch 56, sibling_census 68=68 added) | green to green |
| 6 | `verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` | 0 / province rows 20 matched 20 | 0 / identical output | green to green |
| 7 | same command plus `--skill SKILL.md` | 2 / argparse: unrecognized arguments: --skill | 0 / skill description names 9 of 9 non-none lanes; length 1008 of 1024 | absent to green (no arm at base; not harm) |
| 8 | `verifiers/check_sibling_census.py --self-test` | 0 / 44 assertions | 0 / 68 assertions | green to green |
| 9 | `verifiers/verify_dispatch_prompts.py --self-test` | 0 / 32 assertions | 0 / 56 assertions | green to green |
| 10 | `verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json` | 0 / boxes proven 2 | 0 / boxes proven 2 (identical log) | green to green |
| 11 | `verifiers/verify_harness_independent.py --self-test` | 0 / 123 assertions | 0 / 123 assertions | green to green |
| 12 | `verifiers/compare_harness_independent.py --self-test` | 0 / 330 assertions | 0 / 330 assertions | green to green |
| 13 | `verifiers/verify_surfaces.py --json` | 1 / pass 5 fail 2 (loader literals not verifiable; vacuity) | 1 / pass 5 fail 2 (identical log) | red to red, identical |
| 14 | `verifiers/verify_harness_claims.py` | 1 / 21/28 checks pass; DRIFT omp.db.rows, omp.offered.skills, omp.cache.misses, omp.catalogue | 1 / identical log | red to red, identical |
| 15 | `verifiers/check_substrate_pins.py` | 1 / DRIFT 2/3 pins failed: omp_binary_sha256, omp_binary_mtime | 1 / identical log | red to red, identical |

## Counters (C1 and C2 as named in the plan)

- C2, run from the head clone: `verifiers/box_proof_case_deletion.py --rev f30464660c675d1c1e2851a3bf0366a3aaffe5a8` gives rc 1, `killed 0 of 6`. With `--rev 542f515672306e1baefcb69ba79f1d4c18b6450e` it gives rc 0, `killed 6 of 6`. With `--rev 956ee1676e4c18480bce8ac3993541462be76e11` it gives rc 0, `killed 6 of 6`.
- C2, my own deletion probe at 956ee167, run in the scratch head clone. I edited `verifiers/fixtures/dispatch-prompts/manifest.json` and restored it byte for byte; `git status --porcelain` was empty afterwards. Unmodified `--box-proof`: rc 0, `boxes proven 2`. Deleting each of `d04-placeholder`, `d04-stem`, `d04-unknown-lane`, `d08-role-round`, `d08-report-dir-round`, `d08-above-state` gives rc 1 each, with `no isolated must-fail case for conjunct ...`. Deleting the all-PASS control `d04-control` gives rc 1, `no all-PASS control case`. That is 6 of 6 killed, and the control also fails.
- C1, the head census script run on the base SKILL.md (`--skill <base>/SKILL.md`): rc 1, `skill description names 5 of 9 non-none lanes`. The FAIL lines name chousa, kama, kotodama and tameshi. At head (row 7): rc 0, `9 of 9`, description 1008 characters against a 1024 budget.
- I did not run the C1 counter at 542f515.

## Findings

1. **No harm (none found).** No gate is green at base and red at head. Rows 1 to 12 are green at both revisions. Rows 3 and 4 are red at both but fewer DRIFTs at head. Rows 13 to 15 are red at both with identical logs.
2. **Low, operability: the C2 counter is unregistered.** `box_proof_case_deletion.py` appears in `verifiers/floors-registry.json` nowhere, and no other verifier imports or runs it. Grep finds it only in `LOG.md`, `SCORECARD.md` and itself. The enforcement is live: finding-level probe above shows `verify_dispatch_prompts.py --box-proof` exits 1 on each deletion. But the counter that prints "6 of 6" is not guarded, so a broken counter would fail no gate.
3. **Bounded, unattributed: fleet root `.git` changed during my run.** `find /home/vgpnk/Projects/shokunin/.git -maxdepth 1 -newer logs/marker` lists `index`, `COMMIT_EDITMSG`, `MERGE_RR` and `objects`, all stamped 13:34:06Z, about 19 seconds after my marker (13:33:47Z), which fell inside the 35-second `check_assertion_floors` run. `.ufo/waves/hyaku/PHASE3.md` also changed after the marker. My code-path check: the census calls against real sibling repos are read-only `git show` (`verifiers/check_sibling_census.py:316`); its `_git` init, add and commit calls at lines 986 to 996 are in a fixture builder whose root I did not check; the other gates' `git -C` calls (`verify_corpus_integrity.py:527`, `verify_corpus_independent.py:64`, `compare_harness_independent.py:2400`, `box_proof_case_deletion.py:128`) ran on the scratch clones. I did not audit processes, so I cannot prove my runs did not write there. Fleet owner should check. Also: a stray fleet-root entry named `bash: ` predates my first command; I left it alone.
4. **Info, calibration: baseline expectations moved in this change.** `verifiers/corpus-baseline.json` changes `corpus.index.tracked_files` from 66 to 68 and `corpus.pointers.report_total` from 43 to 44. The head observed values are 68 and 44, and the gate reads them as real. This is a refresh for two newly indexed files, not a loosening, but it is an exact-equality expectation moved in the same change. Command: `git diff f30464660c675d1c1e2851a3bf0366a3aaffe5a8 956ee1676e4c18480bce8ac3993541462be76e11 -- verifiers/corpus-baseline.json`.
5. **Info, operability: description headroom is 16 characters.** The description is 1008 of 1024 characters (base 814). I did not test what happens above 1024.
6. **Info: floors moved in step, none lowered.** `floors-registry.json` `instrument_total` 10 to 11; checklist 1845 to 1851; dispatch_prompts 32 to 56; sibling_census added at 68. All 11 instruments PASS with observed equal to floor at head.

## Residual risk and verification gaps

- Rows 13 to 15 are red at both revisions from host state (omp dump and omp binary). They neither show harm nor clear it. I did not investigate their causes.
- The census reads live sibling repos at run time (13:33Z to 13:37Z). A sibling commit landing in that window could move rows 6 to 8. Logs at both revisions are identical for row 6, so none was visible.
- Out of scope for this seat: D1 to D6 repairs, S024 to S029 and re-opened S019 and S022, Q26, M31, the adjacency semantics of the nine lanes, and the C1 counter at 542f515. Other seats own those.
- Unrun checks are not passes. Every check in the assignment ran at both revisions; none was skipped.
