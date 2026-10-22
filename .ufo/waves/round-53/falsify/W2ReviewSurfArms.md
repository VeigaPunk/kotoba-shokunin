Result: HOLDS — both round-52 attempt-2 fix arms at aeed0890 fail when only their named fix reverts, and each arm pins the named fix's observable rather than an incidental path.

# Scope and method

Target: the two self-test arms added to `verifiers/verify_surfaces.py` at aeed0890efb7cb62ef1364ce7d7ba5566ef3fed6 (routed defect 3, plan § Claims repairs item 3), guarding the two round-52 attempt-2 C1 fixes that landed in a44196d. Judged tree c775d6823bfca8f0de8c0874032a954438b38edc. Attacks ran in my sandbox clone `/fast/scratch/hyaku/kotoba-r53/w2/KotobaR53.W2ReviewSurfArms` (cloned from the lane, checked out at c775d68; ends the run with `git status --porcelain` → 0 dirty entries). No tool installs or updates were made (operator directive: nothing was needed). No lane file other than this report was written; no lane git/jj state touched; no model calls; no web fetches.

Identify the fixes under test (both present at c775d68, both landed in a44196d — verified via `git show a44196d -- verifiers/verify_surfaces.py | grep …`, matched at lines 16, 19, 28 of that diff):

- Fix A — unresolved-file admission: `verifiers/verify_surfaces.py:515-522`. The revert target is the `or (g.startswith("<unresolved-var:") and f in declared_files)` clause of the callee-admission set (hunk comment: "round 52 falsify, CriticC1Escape P4").
- Fix B — empty-baseline fallback: `verifiers/verify_surfaces.py:483-487`. The revert target is the `bool(declared)` conjunct of `generic` (hunk comment: "round 52 falsify, ReviewC1Diff").

The arms under test, both added at aeed0890 and unchanged through c775d68 (`git diff aeed0890 c775d68 -- verifiers/verify_surfaces.py verifiers/fixtures/surfaces/strings-omp-unresolved-group.txt verifiers/fixtures/surfaces/baseline-empty.json` → empty; the C1 commit 6dd3116 added 22 unrelated OC assertions only):

- Arm 1 (b2j, "unresolved-group-admission"): `verifiers/verify_surfaces.py:1428-1441`, fixture `verifiers/fixtures/surfaces/strings-omp-unresolved-group.txt`. Asserts exit 1 and a FAIL detail naming `omp:<unresolved-var:S$>/CLAUDE.md`.
- Arm 2 (h2, "empty-baseline fallback"): `verifiers/verify_surfaces.py:1575-1587`, using the existing clean omp fixture against `baseline-empty.json` (`"classes": []`) and `inventory-empty.md`. Asserts exit 1 and FAIL naming `omp:claude-md/CLAUDE.md` and `omp:gemini/GEMINI.md`.

# Attack results

All runs: `python3 -B verifiers/verify_surfaces.py --self-test` in the sandbox (grep `-v "^ERROR"` applied only to hide the expected missing-path negative-fixture ERROR lines, which appear identically in the untouched base run).

0. Base, both fixes present:
   `0 failure(s) over 155 assertions`, exit 0.
1. Revert Fix A alone (drop only the `or (g.startswith("<unresolved-var:") and f in declared_files)` clause; Fix B intact):
   exit 1.
   ```
   self-test FAIL: unresolved-group-admission: exit 1: got 0
   self-test FAIL: unresolved-group-admission: names unresolved class: got 'PASS surfaces.no_uncovered_class: all 2 extracted loader class(es) declared\n'
   2 failure(s) over 155 assertions
   ```
2. Revert Fix B alone (drop only `bool(declared) and `; Fix A intact):
   exit 1.
   ```
   self-test FAIL: empty-baseline fallback: exit 1: got 0
   self-test FAIL: empty-baseline fallback: names extracted omp classes: got 'PASS surfaces.no_uncovered_class: all 0 extracted loader class(es) declared\n'
   2 failure(s) over 155 assertions
   ```
3. Both fixes reverted together:
   exit 1, `4 failure(s) over 155 assertions` — exactly the two arms' four assertions, no other assertion failed.
4. Restored both fixes: `0 failure(s) over 155 assertions`, exit 0; sandbox byte-identical to c775d68.

Every arm fails when its named fix alone reverts, and only then. Severity: no defect found in either arm.

# Is each arm testing the fix it names?

Arm 1 → Fix A: HOLDS, with a discriminating-fixture argument I verified empirically.

- On revert, the got-line is `PASS surfaces.no_uncovered_class: all 2 extracted loader class(es) declared` — the bq call (unresolved `S$` group, declared file CLAUDE.md) vanished, while the two Kl control pairs still extract and match the baseline. That is precisely the P4e escape the fix closes (an unresolved group vanishing instead of surfacing), and it is not vacuity (extraction is non-empty) and not kind-laundering.
- Why the Kl control pairs matter: I built a bq-only fixture (Kl removed) in the sandbox and ran the CLI with Fix A present, then with Fix A reverted. Present: `FAIL surfaces.no_uncovered_class: 1 loader class(es) undeclared in baseline: omp:<unresolved-var:S$>/CLAUDE.md`, exit 1. Reverted: exit 1 anyway, but via `vacuity: 0 loader class(es) extracted from the omp dump while the baseline declares 8 loader-group class(es)` plus `extractor blind: … (omp:claude-md/CLAUDE.md)` — the unresolved class is never named. So an exit-code-only arm on a bq-only fixture would survive the fix's revert (incidental discrimination through the round-21 vacuity guard). The landed fixture's two Kl pairs convert the revert into a clean exit-0 PASS, which the arm's two assertions (exit code AND the named unresolved class) both catch. The landed design is the tight one, and it asserts the fix's observable, not a side effect.
- Fixture and its baseline (`baseline-18.12.5.json`) are unchanged since aeed0890 (see diff check above), so the arm still exercises the committed 18.12.5 declared set, not a locally mutated one.

Arm 2 → Fix B: HOLDS.

- On revert the got-line is `PASS surfaces.no_uncovered_class: all 0 extracted loader class(es) declared` — the exact 0==0 vacuous pass the fix exists to kill. The vacuity guard stays silent on this path because `baseline-empty.json` declares no loader-group entries (`check_no_uncovered_class` vacuity arm requires declared loader-group classes, `verifiers/verify_surfaces.py:946-954`), so the only way the arm's expected exit 1 + named classes appear is the fallback firing. Mechanism check: `declared_loader_pairs` initializes `out: set()` (`verifiers/verify_surfaces.py:532`) and returns that empty set — not None — for an empty classes array, so `declared is not None` remains true and `bool(declared)` is the operative conjunct. Confirmed by the observed revert behaviour, not just by reading.
- The arm reuses the existing clean omp fixture (real 8-pair extraction) rather than a crafted dump, so the FAIL names the two genuinely extracted classes; asserting the class ids (not just exit 1) is what makes the revert detectable, since a revert produces exit 0.

Independence: single-revert runs each produced exactly 2 failures confined to their own arm's assertions; the combined revert produced exactly 4. Neither arm reacts to the other fix's state, so there is no incidental coupling between the arms, and the base run shows both arms pass with both fixes present.

# Findings

No BREAKS. Both arms: HOLDS.

# Residual risk and verification gaps

1. Both arms guard the observable of `--check surfaces.no_uncovered_class` only. A weakening of `check_no_uncovered_class` itself (rather than of `extract_classes`) would also trip these arms — still on-target for the invariant, but the arm cannot distinguish "fix reverted" from "check weakened". The erratum's scope guard (a) on this file is the compensating control; not my seat to run (GuardScopeC1).
2. Arm 2 depends on `declared_loader_pairs` returning an empty set rather than None for an empty classes array. If that helper's contract ever changed to return None on zero entries, the fallback would trigger via `declared is not None` and the arm would pass regardless of `bool(declared)`. Current code returns `set()` (verified), and no observed defect — noted as a latent dependency, not a finding.
3. Revert testing proves discrimination for the exact landed fix text; a behaviour-preserving refactor that moves the condition elsewhere is not covered by this method. Standard limitation, mitigated by the scope guard above.
4. I did not run the full C1 counter (`verifiers/check_opencode_repin.py`) or the floors checker; the in-context freshness results (exit 0 at 6dd3116) are quoted from the assignment context and were not re-executed by me. Covered by RerunC1/GuardRowsC1 seats.
