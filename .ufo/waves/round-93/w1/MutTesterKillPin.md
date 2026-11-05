# MutTesterKillPin — round 93 C1 mutation probe

Seat: MutTesterKillPin (mutation-tester). Scope: mutate the ExecKillPinRev C1 candidate; does the frozen counter
`verifiers/fixtures/round-93/c1-killpin-rev.sh` or the battery `--self-test` kill each mutant?

## Candidate
- Base: `6d7eee0570912d9f3b9d3e3d0137f3c755451233` (freeze). Patch: `ExecKillPinRev.patch`, sha256
  `c88bd6aaddadab2fcb1321628fbb273f2c84033c564bd5d1f27047a2e1705f20` (matches the READY-referenced patch).
- Built in scratch clone `/fast/scratch/hyaku/kotoba-r93/MutTesterKillPin/repo` as commit
  `75213bd92a8e7c9fc8e433a4915f5f70f1e1ac16` (scratch identity; `rev-parse --show-toplevel` checked = clone).
- Candidate baseline:
  - `python3 -B verifiers/check_mutation_battery.py --self-test` → `0 failure(s) over 31 assertions` (rc 0)
  - `c1-killpin-rev.sh 75213bd9… <repo>` → `C1-PREDICATE-MET` (drop world rc 2 names `kill-set-size`: yes;
    other world rc 2 names: no; honest rc 0 names: no). Exit 0.
  - Added-kill-row world (18 kill rows, all with probe targets, committed): rc 2 with
    `could-not-evaluate: arm kill-set-size: manifest at a715b3586bb0 has observed 18 kill rows, pinned 17`. **Refused, naming the arm.**
  - Dirty working tree, committed manifest honest, one kill row dropped only in the working tree: rc 0 (committed bytes govern).
  - Round-92 `controls-run.sh` at candidate: `round-92 controls: shortcuts refused 2 of 2; honest held 2 of 2` (rc 0).

## Mutants (each committed in scratch on top of the candidate, restored to candidate after; mutant diffs in `receipts/<m>.diff`)

| id | mutation (exact diff) | frozen counter `c1-killpin-rev.sh` | self-test | verdict |
|---|---|---|---|---|
| m1 | new check block deleted (4 lines) | UNMET: drop world rc 2 *no* name; honest rc 2 (clone's bat-self-test baseline fails) | `1 failure(s) over 31` (dropped-row arm) | KILLED (counter and self-test) |
| m2 | pin comparison inverted: `return n == want` → `return n < want` (literal reading of `!=`→`<`; refuses honest world too) | UNMET: honest rc 2 *names* `kill-set-size` (17 < 17 refused) | `18 failure(s) over 31` | KILLED |
| m2b | faithful "only drops refused": `return not (n < want)` (so 18 kill rows is accepted by the check) | UNMET: honest rc 2 names no (clone bat-self-test baseline fails); drop world names yes | `1 failure(s) over 31` (live arm: 16 kill rows not refused) | KILLED — but via the honest conjunct and the self-test; see F2 |
| m3 | the new check reads the WORKING-TREE manifest: `kill_set_check((lane / MANIFEST).read_text(…))` instead of `committed` | **MET** (`C1-PREDICATE-MET`): all three worlds are committed and clean, so the working tree equals the committed bytes | `0 failure(s) over 31` | **SURVIVED** the frozen counter and the self-test. KILLED only by my dirty-tree probe (rc 2 naming `kill-set-size`, 16 of 17) |
| m4 | arm name dropped from the refusal: `arm kill-set-size: manifest at` → `manifest at` | UNMET: drop world rc 2 names no | `1 failure(s) over 31` | KILLED |
| m5 | kill check moved before the target-set check (block reordered) | **MET**; round-92 `controls-run.sh` still `shortcuts refused 2 of 2; honest held 2 of 2` | `0 failure(s) over 31` | **SURVIVED** (equivalent on every observable the frozen instruments read); see F3 |
| m6 | every `could-not-evaluate:` line prefixed `kill-set-size:` (3 print sites; the forgery shape) | UNMET: other world rc 2 *names* `kill-set-size` (`baseline fg-self-test` line prefixed) | `0 failure(s) over 31` | KILLED by the counter only; self-test survives; see F4 |

Mutant rows: 7 mutants; 5 killed by the frozen counter, m3 and m5 survived it. Self-test killed m1, m2, m2b, m4 and survived m3, m5, m6.
(Counter MET/UNMET tally is over the frozen predicate, not a manifest kill-set count; the battery's own 17-row kill-set is
unchanged on every mutant except where it was broken by the mutant.)

## Round-92 controls on m5
`controls-run.sh` at m5: `shortcuts refused 2 of 2; honest held 2 of 2`. The C1 shortcut is still refused because
`parse_manifest` runs before both checks and already raises `could-not-evaluate: manifest mb-c1-shortcut-kill: target … has no probe set`,
which the controls grep. So the moved check never executes on that world.

## Findings
- **F1 (counter gap, m3).** The frozen counter builds only committed, clean worlds, so it cannot distinguish reading the
  committed manifest from reading the working tree. The self-test's `poison` fixture dirties only the freeze-gate target, not the manifest.
  The required behaviour (committed bytes govern under a dirty tree) is observed only by my extra probe (`receipts/dirty-cand.txt` rc 0,
  `receipts/dirty-m3.txt` rc 2). Recommend a frozen dirty-tree arm in a future addendum; not amended here.
- **F2 (no added-row arm in the counter or self-test).** The 18-row refusal is observed only on the candidate (`receipts/added18.txt`).
  The frozen counter has no added-row world, so an acceptance-only regression (m2b) is not caught by the counter's drop/other/honest worlds.
  Under m2b, the 18-row world is refused by the clone's bat-self-test baseline (`receipts/m2b-added18.txt`), not by the arm, so that
  run does not isolate the arm's acceptance logic. The candidate's own self-test has no add-row assertion.
- **F3 (order-insensitive kill check, m5).** Before/after placement of the kill check changes no observable on the frozen instruments.
  The round-92 C1 shortcut is refused by `parse_manifest` first either way. Benign for C1 (not a kill-set leak), but it means the
  frozen instruments cannot tell an earlier from a later check.
- **F4 (self-test does not isolate the forgery shape, m6).** The counter's `other` world is the only frozen reader that catches a
  CNE line whose prefix names `kill-set-size` while the cause is a baseline failure. The self-test's "unrelated baseline failure" arm takes the
  rc 1 path, not the CNE path, so it never reads the CNE prefix. The counter kills m6 (`receipts/m6-counter.txt`).
- **F5 (self-test mutation of module global).** Candidate's self-test assigns `KILL_SET_PINNED` in a try/finally, so an
  exception mid-arm would leave the global set to 9 or 10 for the rest of that process. Not observed; noted as the builder did.

## Restoration
- Scratch clone restored to `75213bd9…` after every mutant (`git checkout -q -f`). Lane untouched (read-only `git show` / counters run from lane path with REPO = scratch).
- No lane writes, no fleet-root writes, no git write in the lane. No kernel or host setting changed. No package installed.
- Processes: all started by this seat; each counter and self-test ran serially (one counter at a time); none still running.

## Receipts
`/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-93/w1/MutTesterKillPin/receipts/` (counter, self-test, dirty, added-row,
controls outputs; `<m>.diff` per mutant; `mut.py`, `mut2b.py`, `drive.sh` harness). Pre-data receipts copied: `redbefore-c1-base.txt`, `forgery-c1-run.txt`.

## Verdict
C1 candidate passes its own counter and self-test and refuses the added-row and drop worlds. The frozen instruments kill 5 of 7 mutants.
Gaps: the frozen counter cannot see a working-tree read (F1) or an added-row acceptance (F2), and the self-test does not catch the forgery naming (F4).
Recommend an L1 addendum adding a dirty-tree arm and an added-row world before C1 is scored, or record these as disclosed limits.
