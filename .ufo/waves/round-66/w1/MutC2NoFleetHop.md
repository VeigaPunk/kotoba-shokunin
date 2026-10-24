# MutC2NoFleetHop — C2 routed-mutation probe (round 66)

Read-only mutation seat. No claim, counter, threshold, baseline, plan or receipt was changed;
no production edit was made. Only this report was written in the lane tree.

## Revisions (pinned base vs measured tip)

- Pinned round-66 base: `11385e04e368c1e94ab1a5a89d7439033eb1f855` (plan / controls).
- Observed lane tip (scratch clone base): `2a8eba56b3f9321b70c569fa2816d42237ca49a2`
  (`round-66 verifier spot-check (integrator, hyaku): non-author admit/reject`).
- Clean-green receipt revision used for isolation: `fc1b71e56fda86fefe672f2cae90a62318d34449`
  (`round-66: align independent integrity resolver`), where the C2 receipt records 9/9 and
  `commit_unresolvable=0`.
- Temporary sandboxes (disposable, no lane jj/Git index touched):
  - `/tmp/mutc2-nofleethop.3Yyq/pristine` — clone at `2a8eba5`, mutation committed locally as
    `3089e87316aefa000af3aa3bf200e71a804b06ee` (scratch history only).
  - `/tmp/mutc2-nofleethop.3Yyq/fc` — clone checked out at `fc1b71e`, mutation left uncommitted,
    then restored.

Baseline detector hashes (pristine, both clones and the lane tree):

```
febfa57e64896a37cea740ee080ccd1ea0f994980ade0856fc2dc080c1386534  verifiers/verify_corpus_integrity.py
3129c0d7016467d93a3ea45a626dd1237bc92bd20d79bc09499c53c503293141  verifiers/check_r66_routed_repairs.py
0944ae98cbe52dfcc9b7836b68710be8758ad177a3bb8abe1dc476671c827d15  verifiers/corpus-baseline.json
```

## Mutant

Smallest behavior-bearing point: the fleet-root fallback branch of
`commit_resolves(hex_id, repo, fleet_root=FLEET_ROOT)` in `verifiers/verify_corpus_integrity.py`.
Lane lookup is kept; the fallback is removed; the `COMMIT_HOP_MARKER` literal and docstring are
left untouched (they are source claims, not the behavior).

```diff
     if git_ok(repo, "cat-file", "-e", commit_peel_arg(hex_id)):
         return True
-    if not fleet_root.is_dir():
-        return False
-    return git_ok(fleet_root, "cat-file", "-e", commit_peel_arg(hex_id))
+    return False
```

Mutant hash: `376597f636ff8296e47ca0bf54e4b8a1cbf006120facb7a431dad751a5de69d4`.

Expected detector: `verify_corpus_integrity.py --self-test` assertion
`commit-hop/fleet-fallback` (fleet-only commit must resolve), plus the gate's
`corpus.pointers.commit_unresolvable`; and the r66 routed counter's D2 check.

## Detector outputs — pristine `fc1b71e` sandbox (clean green baseline)

```
$ python3 -B verifiers/verify_corpus_integrity.py
corpus.index    tracked=118 unindexed=0 stale=0 missing=0  (136 FILE-column patterns over 117 md files)
corpus.pointers report_dead=0/79 commit_total=37 unresolvable=0 nonhash=0 (...)
9/9 checks pass
exit=0

$ python3 -B verifiers/verify_corpus_integrity.py --self-test
self-test: 0 failure(s) over 161 assertions
exit=0

$ python3 -B verifiers/check_r66_routed_repairs.py --rev fc1b71e56fda86fefe672f2cae90a62318d34449
control at 11385e04: 0 of 2
D1-r65-registries-committed: PASS
D2-corpus-integrity-reconciled: PASS
r66 routed defects closed 2 of 2
exit=0
```

## Detector outputs — mutant (same `fc1b71e` tree, fallback removed)

```
$ sha256sum verifiers/verify_corpus_integrity.py
376597f636ff8296e47ca0bf54e4b8a1cbf006120facb7a431dad751a5de69d4

$ python3 -B verifiers/verify_corpus_integrity.py --self-test
FAIL commit-hop/fleet-fallback: got False want True
self-test: 1 failure(s) over 161 assertions
exit=1

$ python3 -B verifiers/verify_corpus_integrity.py
corpus.index    tracked=118 unindexed=0 stale=0 missing=0  (136 FILE-column patterns over 117 md files)
corpus.pointers report_dead=0/79 commit_total=37 unresolvable=2 nonhash=0 (...)
           commit_unresolvable: corpus/lessons/round-62-verifier-spotcheck.md:13: def4b9fffbf59e9e121b89ef73fbeb89426bd614
           commit_unresolvable: corpus/lessons/round-65-verifier-spotcheck.md:11: 7b370d54bd0e74eef4aa90b2e8b2fc9736b3d39f
DRIFT   corpus.pointers.commit_unresolvable: observed=2 expected=0 / empty
8/9 checks pass; DRIFT: corpus.pointers.commit_unresolvable
exit=1

$ python3 -B verifiers/check_r66_routed_repairs.py --self-test
self-test: 0 failure(s) over 14 assertions
exit=0
```

The fleet-only citations stay red: with the hop removed, the two fleet-only spot-check commits
(`def4b9ff…`, `7b370d54…`) are reported `commit_unresolvable`, turning the receipt-clean 9/9 tree
into 8/9, exit 1. The behavioral detectors kill the mutant.

## Detector outputs — r66 routed counter world (mutant committed bytes)

At the observed tip `2a8eba5`, the mutation was committed in the scratch clone
(`3089e87316aefa000af3aa3bf200e71a804b06ee`) and the counter was run against those committed bytes:

```
$ python3 -B verifiers/check_r66_routed_repairs.py --rev 3089e87316aefa000af3aa3bf200e71a804b06ee
control at 11385e04: 0 of 2
D1-r65-registries-committed: PASS
D2-corpus-integrity-reconciled: PASS
r66 routed defects closed 2 of 2
exit=0
```

Pristine tip for comparison: same 2 of 2, exit 0. The counter is byte-scoped to `--rev` (a
worktree-only mutation leaves it at 2 of 2), so the committed-mutant run is the meaningful one.

Gate at the observed tip (pristine, same clone) is **already red for independent reasons**:

```
corpus.index    tracked=119 unindexed=1 stale=0 missing=0  (136 FILE-column patterns over 118 md files)
corpus.pointers report_dead=0/82 commit_total=38 unresolvable=0 nonhash=0 (...)
           unindexed: corpus/lessons/round-66-verifier-spotcheck.md
DRIFT   corpus.index.tracked_files: observed=119 expected=118
DRIFT   corpus.index.unindexed: observed=1 expected=0 / empty
DRIFT   corpus.pointers.report_total: observed=82 expected=79
DRIFT   corpus.pointers.commit_total: observed=38 expected=37
5/9 checks pass; exit=1
```

On the same tip tree the mutant adds `commit_unresolvable: observed=3` (the third is
`corpus/lessons/round-66-verifier-spotcheck.md:11: 1154d57a…`) and drops to 4/9, exit 1. Because
the tip baseline is red, this tip gate delta is corroborating, not the kill; the clean kill is the
`fc1b71e` run above.

## Verdict

- **Integrity behavioral detectors: KILLED.** `commit-hop/fleet-fallback` fails (1/161 vs 0/161
  pristine) and the gate reports the fleet-only citations as unresolvable (9/9 → 8/9 at
  `fc1b71e`; 5/9 → 4/9 at the measured tip).
- **r66 routed counter D2: SURVIVED.** `check_r66_routed_repairs.py --rev 3089e87…` scores
  `D2-corpus-integrity-reconciled: PASS`, `2 of 2`, exit 0, although `commit_resolves` no longer
  implements the fleet hop. D2's committed-byte predicate pins the `COMMIT_HOP_MARKER` literal and
  the symbol names (`def commit_resolves(`, `inside_code_span`, `commit_resolves(hex_id`); it never
  executes the resolver, so a lane-only resolver carrying the marker is accepted.
- **Counter self-test world: SURVIVED (coverage finding).** The self-test's `kill/D2-no-fleet-hop`
  is a self-contained fixture that omits the marker; it does not exercise the real verifier, so
  `0 failure(s) over 14 assertions` is unchanged by the mutant. The routed counter cannot by itself
  distinguish "fix landed" from "marker retained, behavior removed".

So the frozen pair is asymmetric: the counter's 2-of-2 is necessary but not sufficient evidence for
D2; the integrity gate/self-test is the behavior-bearing detector. Under this mutant, D2 can still
score true, while the gate and self-test stay red exactly as the claim requires.

## Restoration evidence

Both scratch copies were restored to the exact pristine bytes and re-measured:

```
fc1b71e sandbox:      febfa57e64896a37cea740ee080ccd1ea0f994980ade0856fc2dc080c1386534  (git status clean)
2a8eba5 sandbox:      febfa57e64896a37cea740ee080ccd1ea0f994980ade0856fc2dc080c1386534  (diff vs 2a8eba5 empty)
lane verifier:        febfa57e64896a37cea740ee080ccd1ea0f994980ade0856fc2dc080c1386534  (unchanged)
restored self-test:   self-test: 0 failure(s) over 161 assertions, exit 0 (both sandboxes)
```

The scratch mutant commit `3089e87` exists only in `/tmp/mutc2-nofleethop.3Yyq/pristine`; it is not
in the lane repository. No tool was installed or upgraded for this probe. No subagent was
dispatched.
