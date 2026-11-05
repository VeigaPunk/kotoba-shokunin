# ReviewerKillPin — review of ExecKillPinRev C1 patch (round 93)

Scope: `.ufo/waves/round-93/w1/ExecKillPinRev/ExecKillPinRev.patch` against plans/round-93.md § C1.
Patch sha256 `c88bd6aaddadab2fcb1321628fbb273f2c84033c564bd5d1f27047a2e1705f20` (matches READY).
Candidate: scratch clone `/fast/scratch/hyaku/kotoba-r93/ReviewerKillPin/repo`, freeze `6d7eee0570912d9f3b9d3e3d0137f3c755451233` + builder patch, committed as `9bf0090ee80c001bcd69d895ee304c1051f68086` (scratch identity). Scratch removed before yield.

## Verdict

C1 is met on the candidate: the frozen counter reads `C1-PREDICATE-MET`, and the committed-revision kill-set check is correctly placed and names `kill-set-size` only on the intended path. One self-test arm is vacuous under the module-state leak (finding 1, blocking for that arm). Fix it before landing; the frozen counter is unaffected.

## Findings

### 1. BLOCKING (self-test arm) — the dropped-row arm compares against a leaked pin, not 17

`verifiers/check_mutation_battery.py:800` reads `dropped_ok, dropped_detail = kill_set_check(dropped_text)` with no explicit pin. The default is the module global `KILL_SET_PINNED`, and the self-test sets it to 9 at line 767 and never restores it. So the arm checks "16 kill rows vs 9", not "16 kill rows vs 17". It passes for the wrong reason: the refusal happens because 16 != 9, so any pin other than 16 would pass it.

Evidence (defect sims in scratch, candidate otherwise unchanged):

    $ python3 -B verifiers/check_mutation_battery.py --self-test        # as shipped
    0 failure(s) over 31 assertions
    # instrumented: print KILL_SET_PINNED just before line 800
    PIN-AT-DROPPED-ARM 9
    # sim C: force the pin to 16 at line 800 (committed-minus-one count)
    FAIL arm kill-set-size: a manifest with one kill row dropped is refused by the pin :: observed 16 kill rows, pinned 16
    1 failure(s) over 31 assertions
    # sim C': the same call with an explicit 17
    0 failure(s) over 31 assertions

The arm does not test the pin it names. Fix: `kill_set_check(dropped_text, 17)`, matching the explicit `kill_set_check(live_text, 17)` on line 795. The frozen counter is not affected (it runs the CLI in a fresh process).

### 2. Non-blocking — the rev-path check is the only place that names `kill-set-size`

Verified: `grep -n kill-set-size` in the candidate shows the new raise at line 372, `arm kill-set-size: manifest at %s has %s`, as the only could-not-evaluate path that names it. `kill_set_check`'s "manifest malformed" branch cannot fire from `evaluate()`, because `parse_manifest(committed)` at line 367 raises first with its own message. No other path names the arm.

### 3. Verified — placement and pin

- The check sits after `parse_manifest` and the target-set check (line 369) and before `materialize`, the baseline probes and the G3 read: lines 367–373 of the candidate. Matches § C1 "placement after the target-set check".
- The bytes come from `git show <rev>:<manifest>` (line 366: `committed = git_show(lane, rev, MANIFEST)`), not the working tree.
- `KILL_SET_PINNED = 17` is unchanged at line 87. Only self-test fixture arms assign it, inside the self-test process.
- Anchor check on candidate bytes (`anchor_scan.py` over every manifest row): all 17 kill rows' anchors (18 edit lines across fg/d5/mb targets) match exactly once. The three `mb-*` anchors (mb-m2, mb-m15, mb-m16) each match once.

### 4. Verified — defect sim B (new check deleted): the arm fails on the defect

    # candidate with the rev-path check block removed (python replace), self-test:
    FAIL kill-set-size rev path: a committed manifest dropping a kill row exits 2 naming kill-set-size :: on identity PASS: ...
    1 failure(s) over 31 assertions

Only the dropped-row arm fails; the matching-pin arm and the unrelated-baseline arm still pass, as they should.

### 5. Verified — defect sim A (fixture pin mismatch): the rev path is live

Changing the `broken` fixture pin from 10 to 17 (line 685) gives 2 failures over 31, both on the "broken conjunct" arm:

    FAIL broken conjunct K == M: ... could-not-evaluate: arm kill-set-size: manifest at 1ffe286f72e9 has observed 10 kill rows, pinned 17
    FAIL broken conjunct K == M: the line reads killed 9 of 10 :: ...

Repeated in a second process: identical failure, so no cross-process leak.

### 6. Verified — frozen C1 counter at the candidate

Command: `bash verifiers/fixtures/round-93/c1-killpin-rev.sh 9bf0090ee80c001bcd69d895ee304c1051f68086 /fast/scratch/hyaku/kotoba-r93/ReviewerKillPin/repo` (exit 0):

    honest last: mutation battery killed 17 of 17 kill-set; equivalents survived 6 of 6; disclosed survivors 0 of 0
    drop last: could-not-evaluate: arm kill-set-size: manifest at d7418e4333d5 has observed 16 kill rows, pinned 17
    other last: could-not-evaluate: baseline fg-self-test exit 1, declared 0: the revision does not hold the frozen baseline
    drop world d7418e4333d57af7cb6cb0de372eaedca04bc8d3 rc 2 names kill-set-size yes: yes
    other world 5608faacd0201b98d52ca4cc9b56a1c9f423164a rc 2 names kill-set-size no: yes
    honest world 9bf0090ee80c001bcd69d895ee304c1051f68086 rc 0 names kill-set-size no: yes
    C1-PREDICATE-MET

The pre-data receipt `receipts/redbefore-c1-base.txt` shows `C1-PREDICATE-UNMET` at base 5549fa9e (drop world named nothing). The forgery control `receipts/forgery-c1-run.txt` names `kill-set-size` on the other world and reads UNMET, as designed.

### 7. Verified — round-92 C1 honest control from my clone (measures the candidate)

    $ bash <clone>/verifiers/fixtures/round-92/ctl-c1-honest.sh 9bf0090ee80c001bcd69d895ee304c1051f68086
    G3 registry presence PASS: 1 SKILL.md line(s) name check_mutation_battery.py
    mutation battery killed 17 of 17 kill-set; equivalents survived 6 of 6; disclosed survivors 0 of 0
    C1-PREDICATE-MET   (rc 0)

Note: the round-92 C1 shortcut control (`ctl-c1-manifest-only-v2.sh`) hard-codes freeze `e073723` and builds its own world, so it does not exercise the candidate. Its output (`C1-SHORTCUT-REFUSED`, rc 2 naming `mb-c1-shortcut-kill`) was observed against the lane history only. The candidate refuses it by the same earlier target-set check, by reading the code (line 369 precedes the new check). That is inference, not a measurement on the candidate.

### 8. Non-blocking — patch header prefixes

The builder patch uses mnemonic prefixes (`c/`, `w/`) where `git diff --binary` uses `a/`, `b/`. `git apply --check` succeeds on a fresh clone at `6d7eee0`, and the resulting `verifiers/check_mutation_battery.py` has the same sha256 as the candidate (`810219993763c6e01014da540c8ac53337171d9cd7d0c2c1852b04c9248a2e7e`). Harmless; note only because the plan asks for `git diff --binary` patches.

### 9. Non-blocking — process and evidence gaps

- The builder's `controls-run.sh` did not complete in its seat (300 s tool cap, timed out twice). I did not run it end to end either. Its C2 steps need the C2 patch, which is not in this candidate, so C2 controls are out of scope for this review.
- Two of my own background C2 controls (bg_9545, bg_9546) read the lane tip, not the candidate. I cancelled them as out of scope before they reported.
- Two of my tool calls were malformed (a `path` argument where `command` was required). I also submitted an incremental `type: section` yield that was not a terminal result. No state was affected.
- One IRC reply to ConnectorScope-23 failed (`not logged in`). No content was lost.

## Residual risk and verification gaps

- Finding 1 must be fixed before the arm can be trusted. Re-run `--self-test` after the fix; expect 0 failures over 31.
- The frozen shortcut control and the full round-92 `controls-run.sh` were not run end to end on the candidate (see 7, 9).
- Pin leakage: the self-test's module-global mutation is restored only by process exit. Harmless to the counter, but the cause of finding 1.
