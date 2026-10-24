# MutW2Counter — mutation battery on `verifiers/check_r64_routed_repairs.py` @ c019919c

Seat: kotoba-r64.MutW2Counter-2 (wave 2, falsify). Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Measured tip: `c019919c97ab5fe98e87a7754b4449ea4e699c99`. Base: `078eec4a1f6a41c64ff8806f58b46a67cd413bfc`.

## Method

Landed bytes extracted read-only from git and mutated **only in /tmp copies**:

```
$ git show c019919c:verifiers/check_r64_routed_repairs.py > /tmp/mutw2c/pristine/check_r64_routed_repairs.py
$ sha256sum /tmp/mutw2c/pristine/check_r64_routed_repairs.py
8f5b9f915abe6ae42bf84c4c8842ed341c1e03afc184ca23351f33545e5294bf
```

Two bounded detectors on every copy, same arguments:

- **D1 (certification):** `python3 -B <copy> --root <lane> --rev c019919c…` — the frozen predicate's positive arm.
- **D2 (self-test):** `python3 -B <copy> --self-test` — the 32-assertion constructed-world suite.

Baseline on pristine bytes, both directions (before any mutation):

```
PASS seat-edit-committed    marker=True added-marker=True added-lines=82 (need >=60)
PASS control-revs-named     round-64 LOG line names committed controls 8c4cefa8 + cbbee56e and base 35d44b4b
PASS lowest-axis-corrected  round-64 LOG suffix names depth 9 < consistency 10 as lowest
PASS assertion-count-named  runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23; added patch line names 23 assertions
r63 routed defects closed 4 of 4
exit=0

FAIL seat-edit-committed    marker=False added-marker=False added-lines=0 (need >=60)
FAIL control-revs-named     no round-64 LOG line names both committed control basenames, computed revisions, and computed base
FAIL lowest-axis-corrected  round-64 LOG suffix lacks lowest/depth/consistency and both computed scores
FAIL assertion-count-named  runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23; no BASE_REV-added patch line names 23 assertions
r63 routed defects closed 0 of 4
the pinned do-nothing control at 078eec4a… is never a certification
exit=1

self-test: 0 failure(s) over 32 assertions   exit=0
```

## Mutants, detectors, verdicts

| # | Mutation (one point each) | before sha256 | after sha256 | D1 | D2 | verdict |
|---|---|---|---|---|---|---|
| M1 | `BASE_REV = BASE_REV_LITERAL` → `BASE_REV = "c019919c…"` | 8f5b9f91 | 587d72ec | rc=1, refuse (3 of 4 at repointed base) | 6 failures /32, rc=1 | **killed** (D1 + repointed arm) |
| M2 | check 2 scans whole LOG: `for line in _r64_suffix_lines(root, rev)` → `for line in (show(root, rev, LOG) or "").splitlines()` | 8f5b9f91 | e6c8c5e1 | rc=0, 4 of 4 (**blind**) | 1 failure /32, rc=1 | **killed by D2** (`Round-64b` arm only); the ticket's stated base-1-of-4 kill does **not** reproduce — see F1 |
| M3 | check 1 floor `added_count >= 60` → `>= 90` | 8f5b9f91 | 202c5d73 | rc=1, 3 of 4 | 7 failures /32, rc=1 | **killed** |
| M4 | static cross-check removed (`if runtime_count != static_count: return None, …`) | 8f5b9f91 | e6aba6d2 | rc=0, 4 of 4 | **0 failures /32, rc=0** | **SURVIVED both** → arm delivered below |
| M5 | heading anchor reverted to `stripped == ROUND64_HEADER` | 8f5b9f91 | 8c2322e7 | rc=1, 2 of 4 | 1 failure /32, rc=1 | **killed** |
| M6 | refuse rule `if base_closed != 0:` → `if base_closed >= total:` (r63 green-control form) | 8f5b9f91 | 12c49032 | rc=0, 4 of 4 (**blind**, real base is 0 of 4) | 2 failures /32, rc=1 | **killed by D2** (partial + repointed arms) |

### M1 — repointed BASE_REV

```
base arm failed: pinned do-nothing control at c019919c97ab5fe98e87a7754b4449ea4e699c99 closed 3 of 4; refusing to certify any revision unless the base is exactly 0 of 4
exit=1
FAIL counter arm: honest counter passes label-only worlds: got False, expected True
FAIL counter arm: honest counter passes fingerprint worlds: got False, expected True
FAIL counter arm: honest counter passes worktree-read worlds: got False, expected True
FAIL base arm: partial pinned control refuses certification: got False, expected True
FAIL base arm: repointed green BASE_REV refuses certification: got False, expected True
FAIL counter arm: hardcoded assertion tally is rejected: got True, expected False
self-test: 6 failure(s) over 32 assertions
exit=1
```

The named arm `base arm: repointed green BASE_REV refuses certification` fails as predicted. Note the real run refuses at **3** of 4, not 4: with `BASE_REV == rev` the check-4 receipt diff `BASE_REV..rev` is empty, so check 4 can never pass at a repointed base; checks 1–3 do. The refusal is therefore one check short of "green" yet still refuses, i.e. the `!= 0` form is the load-bearing one (relevant to M6).

### M2 — check 2 matcher relaxed to whole-LOG

```
PASS seat-edit-committed    … added-lines=82 (need >=60)
PASS control-revs-named     round-64 LOG line names committed controls 8c4cefa8 + cbbee56e and base 35d44b4b
PASS lowest-axis-corrected  …
PASS assertion-count-named  …
r63 routed defects closed 4 of 4
exit=0

FAIL heading: a Round-64b sibling heading does not anchor the suffix: got True, expected False
self-test: 1 failure(s) over 32 assertions
exit=1
```

D1 is **blind**: the base control stays 0 of 4, so certification proceeds and the tip scores 4 of 4. The only killer is the `Round-64b` sibling arm, because whole-LOG makes the pre-heading (and 64b-heading) region visible. There is exactly one matching line at the tip and it is post-heading:

```
r64 heading at line 2599
m2 whole-LOG matches at tip: [2604] -> all post-heading: True
```

### M3 — check 1 floor 60→90

```
FAIL seat-edit-committed    marker=True added-marker=True added-lines=82 (need >=60)
PASS control-revs-named     …
PASS lowest-axis-corrected  …
PASS assertion-count-named  …
r63 routed defects closed 3 of 4
exit=1
```

```
FAIL target: all four computed checks pass: got {... 'seat-edit-committed': False ...}, expected {... True ...}
FAIL target: all four checks close: got 3, expected 4
FAIL heading: a parenthetical round heading still anchors the suffix: got {... 'seat-edit-committed': False ...}
FAIL counter arm: honest counter passes label-only worlds: got False, expected True
FAIL counter arm: honest counter passes fingerprint worlds: got False, expected True
FAIL counter arm: honest counter passes worktree-read worlds: got False, expected True
FAIL counter arm: hardcoded assertion tally is rejected: got True, expected False
self-test: 7 failure(s) over 32 assertions
```

The landed 82-line edit fails at the mutated floor in both the real lane and the constructed target (the arm's target uses the same 82-line `_seat_edit_text()`). Killed.

### M4 — static cross-check removed — **SURVIVOR**

Mutated bytes (one deletion, everything else intact):

```python
    if runtime_count != static_count:
        return None, "runtime %d disagrees with static %d (%s)" % (
            runtime_count, static_count, static_detail)
```
deleted; the `EXPECTED_ASSERTIONS` / `EXPECTED_STATIC_SHAPE` gate is left in place.

```
PASS seat-edit-committed    …
PASS control-revs-named     …
PASS lowest-axis-corrected  …
PASS assertion-count-named  runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23; added patch line names 23 assertions
r63 routed defects closed 4 of 4
exit=0

self-test: 0 failure(s) over 32 assertions
exit=0
```

Both detectors are blind. Why: every constructed r63 fixture is *honest about its own tally* — `_r63_fixture_source()` prints the counter it actually accumulated, so runtime always equals static (23 at `fixed_calls=17`, 24 at `fixed_calls=18`). The `fixed_calls=18` substitution arm is caught by the `EXPECTED_ASSERTIONS` gate, not by the cross-check, so no assertion exercises the cross-check. The cross-check is therefore untested by the landed 32 assertions.

**Delivered killing arm** (insert inside `self_test()`'s `try:`, immediately before the `# Historical base LOG contains the old control citations.` block; it turns the suite into 33 assertions):

```python
            # The static reconstruction must be cross-checked against the
            # runtime tally: a self-test that keeps the 23-site literal shape
            # but skips one call behind a guard prints 22, and even a receipt
            # naming 22 must not credit check 4 while static says 23.
            guarded = _r63_fixture_source().replace(
                "    for arm in (0, 1, 2):\n"
                "        check('reject', True, True)\n",
                "    for arm in (0, 1, 2):\n"
                "        if arm != 2:\n"
                "            check('reject', True, True)\n")
            _write(root, R63_COUNTER, guarded)
            _write(root, PATCH_RECEIPT,
                   "C2 patch tally measured by runtime and static reconstruction: 22 assertions\n")
            skewed_rev = _commit(root, "guard-skewed r63 self-test tally")
            check("assertion tally: runtime 22 against static 23 is refused",
                  check_assertion_count(root, skewed_rev)[0], False)
```

Why it targets the cross-check and nothing else: the guarded fixture keeps the literal loop shape `for arm in (0, 1, 2):` with two `check(...)` call sites inside it, so `_static_assertion_count` still computes `(17, 2, 3) = 23` and passes the `EXPECTED_*` gates; the `if arm != 2` guard makes the *runtime* tally 22. The receipt names 22, so with the cross-check removed `count=22` matches the added receipt line and check 4 wrongly returns True; with the cross-check present (`22 != 23`) `_materialized_tally` returns None and the check returns False.

Validated on both byte sets (arm copy = pristine + arm, and = M4 + arm):

```
##### arm_pristine (sha cc7f8334) #####
self-test: 0 failure(s) over 33 assertions
exit=0
##### arm_m4 (sha 373fec25) #####
FAIL assertion tally: runtime 22 against static 23 is refused: got True, expected False
self-test: 1 failure(s) over 33 assertions
exit=1
```

The arm is green on landed bytes and red exactly on the M4 mutant. [INFERENCE] Landing it changes the suite tally from 32 to 33 assertions; any prose/commit that freezes "32-assertion self-test" (round-64 commit message, LOG entry, docstring) must be updated in the same change.

### M5 — heading anchor reverted to exact equality

```
PASS seat-edit-committed    …
FAIL control-revs-named     no round-64 LOG line names both committed control basenames, computed revisions, and computed base
FAIL lowest-axis-corrected  round-64 LOG suffix lacks lowest/depth/consistency and both computed scores
PASS assertion-count-named  …
r63 routed defects closed 2 of 4
exit=1

FAIL heading: a parenthetical round heading still anchors the suffix: got {... 'control-revs-named': False, 'lowest-axis-corrected': False ...}, expected {... True ...}
self-test: 1 failure(s) over 32 assertions
exit=1
```

The real heading `## 2026-10-24 — Round 64 (hyaku run 5, attempt 1; …)` (LOG.md:2599) is parenthetical, so the exact-equality anchor empties the suffix and both suffix-scoped checks fail. Killed.

### M6 — refuse rule weakened to r63's green-control form

```
PASS seat-edit-committed    …
PASS control-revs-named     …
PASS lowest-axis-corrected  …
PASS assertion-count-named  …
r63 routed defects closed 4 of 4
exit=0

FAIL base arm: partial pinned control refuses certification: got False, expected True
FAIL base arm: repointed green BASE_REV refuses certification: got False, expected True
self-test: 2 failure(s) over 32 assertions
exit=1
```

D1 is blind by construction: the real pinned base is *exactly* 0 of 4, so `>= total` and `!= 0` agree on the real repo. The partial-world arm (`partial_base_source`, base repointed to `wrong_rev`, which closes 3 of 4) is the killer, plus the repointed-green arm. Both attacks on the refusal rule (M1 and M6) are visible **only** through constructed worlds — the self-test is the sole defense here.

## Findings beyond the six

**F1 — premise check: the `LOG.md:2576` leak does not make the base score 1 of 4 under a whole-LOG scan.** At BASE_REV the scan still returns 0 of 4, and the base LOG contains no line naming both control basenames:

```
pristine/m2 check2 @ 078eec4a = False :: no round-64 LOG line names both committed control basenames, computed revisions, and computed base
base LOG lines naming BOTH basenames: []
```

Line 2576 is one conjunct away, not a leak on its own:

```
commits: ['8c4cefa8e1b751d5f93dbcc65349b8e985b102d8', 'cbbee56e9a3589b0b46736ad36f1b77701def80e'] pinned: 35d44b4b4dcdda234b5dbff7af37e432fec55f05
line2576 hash-prefix conjuncts: [True, True] True
line2576 has 'committed': True
line2576 basenames: [False, False]
base LOG lines satisfying every conjunct EXCEPT the basename check: [2576]
```

So the load-bearing conjunct for this leak class is `all(name in line for name in basenames)`, not the suffix scope. Proof by supplementary mutant **M2c** (whole-LOG **and** basename conjunct dropped, sha `57cbbbb7`):

```
base arm failed: pinned do-nothing control at 078eec4a1f6a41c64ff8806f58b46a67cd413bfc closed 1 of 4; refusing to certify any revision unless the base is exactly 0 of 4
exit=1
FAIL heading: a Round-64b sibling heading does not anchor the suffix: got True, expected False
FAIL control citation: missing exact basenames fails: got True, expected False
self-test: 2 failure(s) over 32 assertions
exit=1
```

i.e. the base ledger catches this class only after the basename conjunct is gone, and in that case two self-test arms also catch it. The ticket's stated detector for M2 (`LOG.md:2576 → base 1 of 4 → refuse`) is therefore mis-stated: at `c019919c` it cannot fire with the conjuncts intact. M2 is still killed, by the `Round-64b` arm.

**F2 — the counter's own certification run is structurally blind to three of the six mutants** (M2, M4, M6). The self-test is the only detector for M2 and M6, and for M4 there is no detector at all. [INFERENCE] Any future claim that "the counter refuses dishonest worlds" overstates D1: it verifies the tip and the pinned base, not the refusal rule's partial-base behavior.

**F3 — the self-test's constructed "leak" line is strawman-shaped.** Its base LOG bait is `- historical references 8c4cefa8 cbbee56e 35d44b4b.` — no basenames and no `committed`, so it does not satisfy the citation conjuncts even after relaxing scope or dropping the basename check. That is why M2c's base-1-of-4 leak is only caught by the citation-arm, never by the "baseline LOG leak" arm.

## Restoration evidence

No lane source byte was written at any point; every mutation lived in `/tmp/mutw2c/<copy>/`. After the battery:

```
$ sha256sum /tmp/mutw2c/pristine/check_r64_routed_repairs.py \
            /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_r64_routed_repairs.py
8f5b9f915abe6ae42bf84c4c8842ed341c1e03afc184ca23351f33545e5294bf  /tmp/mutw2c/pristine/check_r64_routed_repairs.py
8f5b9f915abe6ae42bf84c4c8842ed341c1e03afc184ca23351f33545e5294bf  verifiers/check_r64_routed_repairs.py
$ git -C <lane> status --porcelain -- verifiers/check_r64_routed_repairs.py   # (empty, exit 0)
$ python3 -B pristine/… --root <lane> --rev c019919c…
r63 routed defects closed 4 of 4          restored_target_exit=0
$ python3 -B pristine/… --self-test
self-test: 0 failure(s) over 32 assertions    restored_selftest_exit=0
```

Detectors are deterministic across the whole run: pristine D1 4 of 4 / rc 0 and D2 32-assertion green both before and after the battery; base direction 0 of 4 / rc 1 both times.

## Tooling

None installed or upgraded; no pacman transaction attempted (host pause respected). Python 3 / git already present.

## Disposition

- M1, M3, M5: killed by both detectors — the landed assertions are load-bearing.
- M2: killed, but the ticket's stated detector is wrong (F1); the real killer is `heading: a Round-64b sibling heading does not anchor the suffix`.
- M6: killed by the self-test only (partial-world + repointed arms); D1 is blind (F2).
- M4: **survives the landed 32-assertion suite and the certification run** → coverage finding; exact killing arm delivered above, validated green-on-pristine / red-on-M4.
