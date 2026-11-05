# MutTesterBattery — r91-w1 attack on the C1 battery runner

Seat: MutTesterBattery (mutation-tester, attack). Target: `verifiers/check_mutation_battery.py` as built by
ExecBatteryArms (`ExecBatteryArms/ExecBatteryArms.patch`, READY `N=25 rc=0`). Freeze base
`9af1a7af2adf0ab07cfd53f92affc1ed8d992262`. Candidate committed in my scratch clone as
`9a776745d72800cc0ad32776108d2f8bb0822cc1` (scratch identity; patch not modified, no lane writes).

## Control (candidate, unmutated)
- `python3 -B verifiers/check_mutation_battery.py --self-test` → `0 failure(s) over 25 assertions`, rc 0.
- `python3 -B verifiers/check_mutation_battery.py --rev 9a776745d728… --work <scratch>` → rc 0; G1 PASS, G2 PASS
  (23 mutant copies, 3 revision copies), G3 PASS; line exactly
  `mutation battery killed 17 of 17 kill-set; equivalents survived 6 of 6; disclosed survivors 0 of 0`.
  Receipt: `predicate-clean.txt`, `selftest-clean.txt`.

## Mutants (one at a time, each from the committed candidate bytes)

| id | mutation | self-test rc | first failing arm | predicate rc | verdict |
|---|---|---|---|---|---|
| m1 | G1 commit check disabled | 1 (1 of 25 fails) | `G1 commit check: the refusal says the revision is not a commit` | 0 (exact line) | KILLED |
| m2 | G1 clean-tree guard disabled | 1 (2 of 25) | `G1 clean-tree guard: a dirtied scratch clone exits 2` | 0 (exact line) | KILLED |
| m3 | restore read-back removed | 1 (2 of 25) | `G2 restore read-back: a tampered revision restore after a mutant exits 2` | 0 (exact line) | KILLED |
| m4 | third PROBES entry removed | 1 (14 of 25) | fixture world `could-not-evaluate: target ... has no probe set` | 2 (`manifest mb-m2-…: target has no probe set`) | KILLED |
| m5 | comment-insert generator broken (bare `(` line) | 1 (12 of 25) | `satisfying world (clean)` → `d5-self-test output changed` | 2 (`eq-comment-insert-freeze-gate: mutant does not compile`) | KILLED |
| m6 | manifest row `mb-m15` dropped (committed, separate clone, rev `c8ec9464e604`) | 0 (0 of 25) | none | 0 with `… killed 16 of 16 …` | SURVIVED |
| m7 | new G1 commit-check arm inverted (`rc == 2` → `rc != 2`) | 1 (1 of 25) | `G1 commit check: a full-hex --rev that is not a commit exits 2` | 0 (exact line) | KILLED |

Tally: 6 KILLED, 1 SURVIVED. Restoration: after each mutant the single file was `git checkout`-restored in
the scratch clone and its sha256 was checked against `HEAD:` before the next mutant. Raw outputs:
`selftest-<id>.txt`, `predicate-<id>.txt`, `m6-selftest.txt`, machine record `summary.json`, rows `mutants.tsv`.

## Findings

1. **m6 survives the exit rule (routed finding, not repaired).** Dropping one of the 17 kill rows leaves the
   battery's self-test green (`0 failure(s) over 25 assertions`) and the public run exits 0 with
   `killed 16 of 16`. The instrument's exit condition (`K == M and M >= 8 …`) never pins the kill-set size to 17;
   only the literal line in the frozen predicate sentence distinguishes it. The C1 predicate ("prints exactly …
   17 of 17 … exits 0") is therefore enforced by the reader comparing text, not by the exit code. Suggested
   routing for the L1: either a self-test arm pinning the real manifest's kill count, or the predicate
   receipt compares the line. Not edited by this seat.

2. **m1 and m7 are guarded only by message text in one arm each.** Under m1 (commit check off) the non-commit
   `--rev` still exits 2, because the failure is re-raised by `git show` as `G1: git show … failed`; only the
   arm `the refusal says the revision is not a commit` detects the loss. The rc arm alone passes. This is a
   kill, but it depends on the exact wording of the refusal text. Same class of coupling as the self-test
   arms in general; noted as a risk, not a defect.

3. **m4/m5 are caught by the predicate too**, through a could-not-evaluate (rc 2) rather than a content fail.
   Both match the "expect could-not-evaluate" expectation.

4. **Guards m1, m2, m3, m7 are invisible to the public predicate.** The predicate run with a guard disabled still
   prints the exact 17 of 17 line and exits 0 (the guards cannot be reached by a valid committed --rev on a
   clean scratch clone). The G1/G2 arms of the self-test are therefore the only kill channel for those
   four rows, as the plan states; the predicate reading does not independently re-test them.

5. **Resource note.** The public predicate run: `time` reported 38 s wall and about 22 CPU-minutes of user
   time on this 32-core host (the freeze-gate and d5 probes parallelise internally). Each predicate run
   was run sequentially, one at a time, by this seat; no other probes were started.

## Risks
- The mutant anchors bind to the candidate bytes; a later landing edit to `check_mutation_battery.py` or to
  the manifest row recipes (`mb-m2`, `mb-m15`, `mb-m16`) would invalidate the m1/m2/m3 anchor mapping.
- m6 was measured on a separate commit (`c8ec9464e604`) that exists only in the scratch clone.

## Tools
No installs. No pacman, no sysctl, no host setting touched. Scratch
`/fast/scratch/hyaku/kotoba-r91/MutTesterBattery` deleted at yield; no lane, fleet, or sibling write.
