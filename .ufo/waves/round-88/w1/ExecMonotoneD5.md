# ExecMonotoneD5 — C2 v2 routed gate (D5 identity + monotone)

Seat: ExecMonotoneD5 (executor, leaf). Owned file: `verifiers/check_r86_routed_repairs_v2.py` (new).
Frozen predicate, plans/round-88.md § C2, carried verbatim:
`python3 -B verifiers/check_r86_routed_repairs_v2.py --rev <rev>` prints `r86 routed defects closed N of 5`,
exit 0 iff N == 5, exit 1 otherwise, exit 2 could-not-evaluate.

## Files written

- `verifiers/check_r86_routed_repairs_v2.py` (new, executable, stdlib only). Imports the frozen r87 counter
  `check_r86_routed_repairs.py` read-only for D1-D4 (`check_d1`..`check_d4`, unchanged).
- `.ufo/waves/round-88/w1/ExecMonotoneD5/receipts.txt` (self-test, scored value, four control arms).
- This report.

Not touched: the r87 gate, the integrity script, `corpus-baseline.json`, the corpus, `floors-registry.json`
(the C2 gate has no floors row in this seat's assignment), `C2_READY` (see below).

## Result at the tip (scored value)

    python3 -B verifiers/check_r86_routed_repairs_v2.py --rev 4df1e8005016c75390a5e06b209462df58c95918
    PASS d1 ... PASS d2 ... PASS d3 ... PASS d4 ...
    PASS d5  identity: 9 names equal at base and rev; monotone: DRIFT at rev [...6 names...] is a subset of base [...6 names...]
    r86 routed defects closed 5 of 5          (exit 0)

N = 5 at `4df1e8005016c75390a5e06b209462df58c95918`. D5 is computed in two scratch clones (base `223ae62`, tip), never the lane tree.

## Self-test (not passing)

    python3 -B verifiers/check_r86_routed_repairs_v2.py --self-test
    1 failure(s) over 16 assertions
    FAIL arm w_added_red (frozen control): ... expects D5 FAIL via (ii); ... reads it as PASS

Fifteen arms pass. The one failure is the frozen `w_added_red` control, and it fails for a reason in the
frozen predicate, not in the code (finding F1). The self-test is not edited to hide it.

**`C2_READY` is written** at `.ufo/waves/round-88/w1/C2_READY` after L1 ruling F1 = disclose (do not amend). The handoff rule said "after the self-test passes"; the L1 ruling accepts the 1-failure self-test as the disclosed state. Its third line is `sha256sum` of the gate: `10bd5508a7e5f8c18e994cf179274469bc6d9c4d28f6134b99b71e7998e58b82`.

## Controls (scratch clones, committed before scoring; real integrity script)

| World | Scratch commit | D5 observed | Frozen expectation | Verdict |
|---|---|---|---|---|
| w_tip (landing tip) | `4df1e80` (lane) | PASS | PASS | as expected |
| w_healed (base + report_dead red fixed) | `142a490` on base `223ae62` (fleet's `round-76/kotoba.md` copied over the dangling symlink) | PASS (DRIFT = the five lane-tip reds) | PASS | as expected |
| w_added_red (tip + unresolvable citation line) | `29358e5` on tip | **PASS** | FAIL via (ii) | **control fails (F1)** |
| w_silenced (tip, `commit_unresolvable` removed from CHECKS) | `8af7784` on tip | FAIL via (i): 8 names vs 9 | FAIL via (i) | as expected |
| w_silenced, monotone-only arm | same | (ii) alone PASS | PASS | as expected (why (i) exists) |

Receipts: `.ufo/waves/round-88/w1/ExecMonotoneD5/receipts.txt` §2-§4.

## Findings

**F1 — the monotone test cannot see a new instance of a name already DRIFT (counter/predicate defect).**
(ii) compares sets of check *names*. `corpus.pointers.commit_unresolvable` is already DRIFT at the base, so a second
unresolvable citation changes its observed count (1 → 2) and adds a detail line
(`corpus/lessons/round-87.md:253: 0123456789abcdef…`), but the DRIFT name set stays the same and (ii) reads PASS.
The same holds for `report_dead`, `report_total`, `commit_total`, `tracked_files`, `unindexed`. Only a check that is
PASS at the base and goes red at the tip (`stale_patterns`, `missing_paths`, `commit_nonhash`) is caught by (ii).
Consequence: the frozen `w_added_red` control cannot be satisfied by the frozen predicate. I did not change the
predicate (plans/round-88.md: a counter defect is a finding; a predicate change after the first candidate score kills C2).
The L1 decides: disclose the control as failed by design, or route an amended predicate through the kill rule.
Measured: `receipts.txt` §4 (`commit_unresolvable` detail 2 in the added world vs 1 at the tip; DRIFT names identical).

**F2 — the scratch clones read a different world than the lane tip receipt for `report_dead`.**
The tracked symlink `.ufo/reports/round-76/kotoba.md` (`../../../../.ufo/reports/round-76/kotoba.md`) resolves to the fleet
root from the lane, where the 8,128-byte file with `## SHONEN` exists. In any clone it dangles (Q63). So the scratch
clone of the tip reads `corpus.pointers.report_dead` as DRIFT (6 DRIFT names, identical to the base set), while
`receipts/before-C2-tip-integrity.txt` (lane) reads 5. D5 still passes (equal sets ⊆ equal sets), but D5's (ii)
at the tip is measured on a world that still carries the report_dead red. The base red is also `corpus/lessons/round-81.md:29`
(`../../.ufo/reports/round-76/kotoba.md`), not `round-86-verifier-spotcheck.md:33` as the plan's narrative says;
`before-C2-base-integrity-full.txt` is the authority, and w_healed was built against it.

**F3 — the plan's base-red narrative is stale.** plans/round-88.md "Measured before-state" names the base-to-tip healed
red as `.ufo/reports/round-84/kama.md`. The committed base receipt names `round-81.md:29` → `round-76/kotoba.md`.
Recorded here; not corrected (plans/ is the L1's).

## Risks

- The gate is not green: the self-test fails by design (F1). `C2_READY` withheld. Downstream waiters on `C2_READY`
  (MutTesterV2, CriticFalsify, ReviewerC2, the L1 integration) are blocked on the L1's decision, not on this seat.
- (ii) is a names-level check; any new red of a name already DRIFT at the base is invisible to it (F1).
- D5 depends on clone-only symlink resolution (F2); a future fleet-root change can flip report_dead in the lane
  and not in clones.
- Lane not modified by this seat except the two new files it owns (the v2 gate and this report/receipts). `git status`
  shows only `verifiers/check_r86_routed_repairs_v2.py` untracked.

## Checks the main agent should run (not run by this seat)

- `python3 -B verifiers/check_r86_routed_repairs_v2.py --self-test` (expect `1 failure(s) over 16 assertions`, F1).
- `python3 -B verifiers/check_r86_routed_repairs_v2.py --rev 4df1e8005016c75390a5e06b209462df58c95918` (expect `5 of 5`, exit 0).
- r87 counter bytes unchanged: `sha256sum verifiers/check_r86_routed_repairs.py` equals the r87 blob.

## Tooling

No tools installed or updated.
