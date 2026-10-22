# A18RulerRerun: falsify of C2 counting command (round 48, attempt 2)

Lane: /home/vgpnk/Projects/shokunin/kotoba-shokunin. Commit under test: d1ae45830235c38320b31032b57a8323cbf90b17 (C2). Runtime: /usr/bin/python3 = Python 3.14.8, uid 1000. No web sources used.

## Verdict
- Counting command (target): CONFIRMED. Exact command exited 0. Receipt verdict `clean`: 13 of 13 cases settled, 0 target failures, 0 behavioral mismatches, 0 evaluation errors. Values and statuses match the committed after receipt on every case. The base-revision control exits 1 with the 5 expected target failures.
- DEFECT-1 (LOW): the new configured-root enumeration aborts the whole consumer (exit 2, no check rows) when an unlogged `--oc-config/skill` or `skills` directory is unreadable. Base exits 0 on the same input. Outside the 13-case oracle and the C2 arm.
- DEFECT-2 (LOW): the contract says "readable direct child SKILL.md files"; the operator is `is_file()`. A mode-000 SKILL.md is counted, as in legacy. No fixture changes.
- RISK-3 (INFO): mixed name identity (directory names on disk roots, frontmatter names on the agents root) double-counts an alias directory. Consistent with the contract; no fixture varies frontmatter name.

## 0. Hash chain (checked before the run)
| object | sha256 | check |
|---|---|---|
| tools/config-root-ruler.py (worktree) | 01af33a6724cb91ddcfd09b690fa7ba68114d799cc4552fa65d6519c3f78bd45 | equals `git show d1ae458:` copy |
| verifiers/verify_harness_independent.py @ d1ae458 | d67b1b6e9ba0e614f643adda2686c9db8d57c31741de01780be3fcb06c4f7937 | equals `--consumer-sha256` and after receipt `consumer_sha256_after` |
| oracle/config-root-cases.json | 1d09a38ce04d6c0ab9a1c4edd7f4255978a0c2b8d44ce037d10fcd37d756b883 | equals pin; only commit touching it is c0185da |
| verification/before-configured-root.json | 8bec447aa538446e84b7cb87b902c5f1021c42bd7a01f81ea14313262f7e2312 | equals pin |
| verification/after-configured-root.json | 47e41ea9be338e21f8a10b7129546b93f77f302404c96e3fc66c8170c9e1eaaa | recorded in 84b9c9b |
| consumer @ 197b5a4 and @ 75f671b | 872993f875338f4f89d5b76178c124313e9fc3368966f8a32583acd0430bdbd1 | identical; equals before-receipt consumer |

## 1. Exact command (from lane cwd)
- `EXIT=0`; stdout 263 bytes; stderr 0 bytes.
- stdout: `{"behavioral_mismatches":[],"current_unsettled":null,"evaluation_errors":[],"remaining_not_observed":[],"settled_cases":13,"target_failures":[],"verdict":"clean"}`
- Receipt: `.../A18RulerRerun/run1/receipt.json`, sha256 b7ab78555cb2a6e9f53f077a7cb1b27f87fd8f91d8411ec6bb1c9a3753918e41. It differs from committed only by recorded_at and scratch path.
- I created run1 as an empty directory and removed it before the run, because the ruler requires a new directory.

## 2. Comparison with committed after receipt
- 17 top-level keys identical: revision, consumer hashes, ruler_sha256, oracle_sha256, baseline sha, scope, verdict, target_failures, behavioral_mismatches, evaluation_errors. Only recorded_at differs.
- Per case (13 of 13): observed target, expected target, base prediction, target_met, all 28 checks, and all statuses (24 DERIVED, 4 SCOPED_OUT) are identical.
- Hash-only differences: stdout_sha256 (13 of 13) and input digests (4 log-bearing cases). Cause: the absolute scratch path appears in consumer stdout and oc.log. Evidence: committed run files still exist under /fast/scratch/hyaku/kotoba-r48-a2/ruler-landed-02; each recorded stdout hash matches its file (13 of 13); each file equals run1 after path normalization (13 of 13).
- Before to after: only oc.roots.names_plus_builtin changed value, in the 5 target cases. No status changed.

| case | expected target | before | after | expected base |
|---|---|---|---|---|
| control-agents-only | 2 | 2 | 2 | 2 |
| singular-unlogged | 3 | 2 | 3 | 2 |
| plural-unlogged | 3 | 2 | 3 | 2 |
| both-distinct-unlogged | 4 | 2 | 4 | 2 |
| configured-duplicates-agent | 2 | 2 | 2 | 2 |
| same-name-both-config-roots | 3 | 2 | 3 | 2 |
| singular-already-logged | 3 | 3 | 3 | 3 |
| plural-already-logged | 3 | 3 | 3 | 3 |
| configured-plus-other-log-root | 4 | 3 | 4 | 3 |
| non-skill-child-files | 2 | 2 | 2 | 2 |
| skill-named-directory | 2 | 2 | 2 | 2 |
| empty-config-roots | 2 | 2 | 2 | 2 |
| duplicate-log-source | 3 | 3 | 3 | 3 |

## 3. Attacks on the counting command
- A. Base control (rev 197b5a4, no baseline receipt): exit 1; verdict failed; target_failures equal the 5 expected names; 0 mismatches; 0 errors. Checks and statuses equal the committed before receipt in 13 of 13 cases.
- B. Determinism: run2 (new scratch) exit 0, verdict clean. Non-path fields equal run1. stdout and oc.log equal after path normalization (13 of 13).
- C. Oracle not tuned to outputs: I recomputed the contract rule (agents {alpha, beta}, plus direct-child SKILL.md directory names under config skill and skills, plus legacy log-named roots) for each fixture. All 13 expected_target_count and expected_base_count values match. The oracle has one commit, c0185da, which predates the before receipt (2026-10-22T01:15:33Z) and the fix (2026-10-22T08:37:34Z).
- D. Scope: `git diff --stat 197b5a4 d1ae458` shows one file, +175/-8. New enumeration at consumer lines 608-615; base at 604-610, same operator. The C2 arm in the same diff has no unreadable or permission case.
- E. Probes (uid 1000; consumer copies from git show at rev and base; inputs built by the ruler's materialize; mode changes applied after materialize):

| probe | new d1ae458 (exit, value) | base 197b5a4 (exit, value) |
|---|---|---|
| gamma in skill/, delta in skills/, unlogged, readable | 0, 4 | 0, 2 |
| gamma/SKILL.md mode 000, unlogged | 0, 4 | 0, 2 |
| gamma/SKILL.md mode 000, root logged | 0, 3 | 0, 3 |
| gamma/ dir mode 000, unlogged | 0, 2 | 0, 2 |
| gamma/ dir mode 000, root logged | 0, 2 | 0, 2 |
| skill/ root mode 000, unlogged | 2, "SUBSTRATE [Errno 13] Permission denied" | 0, 2 |
| skill/ root mode 000, skills/delta readable, unlogged | 2, same SUBSTRATE error | 0, 2 |
| skill/ root mode 000, root logged | 2, non-JSON stdout | 2, non-JSON stdout (legacy) |
| alias dir alpha-copy with frontmatter name alpha, unlogged | 0, 3 | 0, 2 |
| alias dir alpha-copy, root logged | 0, 3 | 0, 3 |

- F. Code: consumer handler at lines 1494-1497 (`except (OSError, sqlite3.Error, LookupError)`, then `return 2`). Ruler: a non-zero consumer exit becomes an error (lines 237-238), verdict `could-not-evaluate` (line 320), exit 2 (line 327). The counting command therefore fails closed on DEFECT-1, but none of its 13 fixtures reaches that path.

## 4. Findings
DEFECT-1 (LOW). Consumer rev lines 608-615 and handler 1494-1497. The change adds every unlogged `skill`/`skills` root to `iterdir()` with no guard, so an unreadable root now stops all check rows. Base never touched those roots. The failure is loud and fail-closed, on an unusual host state, and the oracle and C2 arm do not catch it. Direction: guard OSError for configured roots (skip or record a row), add a permission fixture, or narrow the claim.

DEFECT-2 (LOW). Oracle contract line 8 says "readable"; the operator at line 614 is `is_file()`, which does not test readability. A mode-000 SKILL.md is counted in base (logged) and in new alike. Legacy parity; the 13 counts do not change. Direction: reword to "existing regular file", or enforce readability on both paths.

RISK-3 (INFO). Directory-name identity on disk roots versus frontmatter identity on the agents root: the alias probe counts 3 where frontmatter identity gives 2. Legacy logged roots behave the same. Out of scope by contract.

RISK-4 (INFO). On Python 3.14.8, the unreadable child directory case (probe row 4) raises no error and counts nothing. Other interpreters may raise. Not tested.

## 5. Lane bounds and side effects
- One `git status --porcelain` in the lane at the start. Read-only intent; git may refresh the index stat cache. Later git calls were show, log, cat-file, merge-base, diff --stat, and check-ignore.
- My importlib load of the ruler wrote `.ufo/round-48/tools/__pycache__/config-root-ruler.cpython-314.pyc` at 05:56:51 -0300. It is gitignored (.gitignore:2). I removed that file and its directory. tools/ now holds only config-root-ruler.py, sha256 unchanged.
- Scratch, all under /fast/scratch/hyaku/kotoba-r48-a2/seats2/A18RulerRerun/: run1, run2, base1, attack-*, attack2-*, attack3-*, consumer-d1ae458.py, consumer-197b5a4.py, and stdout and stderr captures.
- Tools installed or updated: none.

## 6. Verification gaps
- One interpreter only (Python 3.14.8).
- Did not run the consumer `--self-test` arm (other seats own it).
- Not tested: symlinked roots, non-UTF-8 names, and frontmatter-name divergence beyond the one alias probe.
- Oracle expectations were checked by my manual rule, not by an independent implementation.
- Records and arm claims were not validated here.
