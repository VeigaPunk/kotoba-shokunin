# Kb80L02Ctl — r79 shortcut worlds re-probed on the round-80 counter

Seat: leaf critic (attack), round 80 w1. Date 2026-10-27.
Lane base `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`; pinned guard base `072048fa8e8a52c707d25f7079772fa317244eb7` (round-73).
Claim under test: **C1** — `python3 -B verifiers/check_tip_battery.py --rev <rev>` → `guards 5 of 5`, `tip battery exit 0: 6 of 6`, exit 0; base `1 of 6`, exit 1.

Task: re-run the r79 shortcut world set that still applies under erratum E5
(W1 baseline-rewrite-to-observed, W2 floors lowered, W4 LOG erratum token,
W5 placeholder registry rows, W6 index row for a nonexistent file,
W7 spot-check edit removing the `HEAD:` pointer) and report, per world:
the world diff, the amended counter's output, own exit. A world reaching
`6 of 6` is a KILL of C1.

## Method

- Worlds re-derived from the CURRENT base bytes (the r79 patches were written
  against r79 bases; every anchor was re-located at `398cbe1` and the edit
  re-applied — no r79 patch was applied blindly). World diffs exported to
  `.ufo/waves/round-80/build/Kb80L02Ctl.W{0,1,2,4,5,6,7}.patch` (W0 is the
  empty-commit base control, 0 bytes).
- Each world is one commit on a branch reset to `398cbe1` in scratch clone
  `/fast/scratch/hyaku/kotoba-r80/Kb80L02Ctl/clone` (removed after the
  receipts were copied into the lane build dir).
- Counter invocation per world (own exit capture, never a pipeline):

      python3 -B <counter> --repo $S/clone --rev <world> --fleet /home/vgpnk/Projects/shokunin

  with the counter's own fleet-shaped sandbox doing the measurement.
- Base (round-72 frozen, unamended) counter sha256
  `e33b17d74f5935a43b04272baf2d88d1d4cf4f879ee9cfa48bb25f89e744bc4a`
  (recomputed this seat, matches the r79 freeze receipt).
The round-72 frozen counter, the published LINE_CAP=60 probe counter, and the
final E5-amended counter were each run on all seven worlds (W0 plus the six
requested controls). The final counter file is
`build/check_tip_battery.amended.py`, SHA-256
`15cc17614e61bdc47122bf501da951de3dbde6444b1ed4a98ca8192c2329ddba`;
its pin table is final (integrity `cc182613a4d089c41e44f11b50e03b45ce582dd8`,
independent `89f392daab3e4181db3ded7676ca0879871ef7ff`). Its `--self-test`
was run here: `self-test: 0 failure(s) over 69 assertions`, exit 0. Each
counter command used direct exit capture.

| world | commit | changed files (patch) | E5 guards | E5 battery | E5 exit | salient result |
|---|---|---|---:|---:|---:|---|
| W0 | `3e27ad77` | empty commit | 5/5 | 1/6 | 1 | five red gates |
| W1 | `940e4c95` | corpus-baseline.json +3/−3 | 5/5 | 1/6 | 1 | integrity remains red on unindexed 1, report_dead 1, commit_unresolvable 2 |
| W2 | `6193712c` | floors-registry.json +1/−1 | 4/5 | 1/6 | 1 | floors guard fails (`checklist floor 1 < base 1863`); floors gate exit 2 |
| W4 | `cedb2e42` | LOG.md +1 | 5/5 | 1/6 | 1 | Correction label does not excuse the dead citation |
| W5 | `f7750d23` | SKILL.md +2 | 5/5 | 2/6 | 1 | registry gate flips to 62/62 without valid command provenance |
| W6 | `f3ec2777` | corpus/README.md +2 | 5/5 | 1/6 | 1 | nonexistent index path is detected; no reward |
| W7 | `541b3e69` | round-77 spot-check +1/−1 | 5/5 | 1/6 | 1 | no spotcheck guard hit; one integrity DRIFT clears, five remain |

Every E5 reading exactly matches the r72-counter reading: the added pins are
inert because no world edits a battery instrument; the cap is inert because
each has 22 instrument additions / 3 deletions against the pinned base, under
both caps. No world reaches 6/6, so this control set does not kill C1.

## Per-world diffs (re-derived at 398cbe1)

- **W1** `940e4c95` — `verifiers/corpus-baseline.json` +3/−3: the three
  `equal`-mode expects re-recorded to the observed base values
  (`tracked_files` 144→152, `report_total` 99→109, `commit_total` 43→46);
  every zero-mode expectation left at 0; **no index row added** (exactly the
  shortcut; observed values re-derived this seat with
  `verify_corpus_integrity.py --no-baseline --json` at the base:
  152 / unindexed 1 / report_dead 1 / 109 / commit_unresolvable 2 / 46).
- **W2** `6193712c` — `verifiers/floors-registry.json` +1/−1:
  `instruments.checklist.floor` 1863→1; in-file tables and docstring untouched
  (the half-bump the registry exists to catch). Guard-base floor at the pinned
  `072048fa` is also 1863 (verified), so the guard's `floors` comparison is
  against 1863.
- **W4** `cedb2e42` — `LOG.md` +1: one appended line, a `**Correction:**`
  label quoting the dead token `.ufo/reports/round-76/kotoba.md` and naming no
  corrected address (r79 WA4 byte-shape).
- **W5** `f7750d23` — `SKILL.md` +2: two `## Gate registry` rows for
  `check_desc_craft.py` / `check_r75_routed_repairs.py` whose entry command
  names a DIFFERENT existing script (`check_r68_routed_repairs.py` /
  `check_r69_routed_repairs_v2.py`), the row's own path only in a trailing
  shell comment (r79 WB5 byte-shape). Direct reading at the world:
  `gate registry rows conformant 62 of 62`, exit 0 — the gate-level false
  green reproduces at the r80 base.
- **W6** `f3ec2777` — `corpus/README.md` +2: one coverage-map row naming
  `knowledge/absent-round80-index-fixture.md` (a file that does not exist),
  nothing else.
- **W7** `541b3e69` — `corpus/lessons/round-77-verifier-spotcheck.md` +1/−1:
  line 15 `` `git show HEAD:.ufo/reports/round-77/kotoba.md` `` →
  `` `git show .ufo/reports/round-77/kotoba.md` `` (the `HEAD:` pointer
  removed; r79 WB4a byte-shape — the exported patch sha256 `df65a440…` equals
  r79's WB4a patch sha256 exactly: the file is byte-identical between the r79
  F1 base and the r80 base, and the one-line edit is the same).
  Direct gate reading at the world: `verify_corpus_integrity` still exits 1
  but `corpus.pointers.report_dead` DRIFT **clears (1 → 0)** — under the base
  gate the bare repo-relative pointer resolves (fleet-shaped), the `HEAD:`
  form did not. This is one red row removed without touching an instrument.

## Notes on W7 and the seat prompt's stated expectation

The seat prompt expects "the spotcheck-identity guard failure" for W7. The
guard compares spot-check blobs between the PINNED base `072048fa` (round-73)
and the measured rev (`verifiers/check_tip_battery.py`, `_spotcheck_shas`);
the round-77 file was added at `b10bcbc` (round-77), rounds after the pinned
base, so it is NOT in the guard's comparison set — the r80 base receipt's own
INFO lines list it as "spotcheck added at 398cbe1 (not a base file)". A sweep
this seat confirmed no pinned-base spot-check file (rounds 46–72) carries a
`HEAD:` pointer at all, so no in-scope edit of one can exist. The guard
failure the prompt expects therefore CANNOT fire on this world; the empirical
reading below names what actually stops W7. (Consistent with r79 finding 2 /
WB4a; reported as a prompt-vs-code discrepancy, not a counter defect: the
world still must not reach 6 of 6.)

## Calibration findings

1. **No shortcut reaches the target.** Final amended-counter results range
   from 1/6 to 2/6, all exit 1; best is W5 (placeholder registry rows) at
   2/6. This control set does not kill C1.
2. **W2 is stopped by the floor guard.** `checklist.floor` 1 is below the
   pinned-base 1863; guard count is 4/5 and the assertion-floors gate itself
   exits 2. The edited floor buys no battery pass.
3. **W5 exposes an unguarded false green.** Two malformed registry rows make
   `check_gate_registry.py` exit 0 (`62 of 62`) and raise the battery from
   1/6 to 2/6, while leaving five other gates red. This reproduces a
   registry-gate weakness, not a C1 counter kill.
4. **W6's nonexistent coverage path is not rewarded.** The direct integrity
   gate at `f3ec2777` exits 1 with `missing_paths=1` and `stale_patterns=1`;
   the tip battery remains 1/6.
5. **W7's specified file is outside the spot-check guard's base.** Its
   `HEAD:` deletion clears the `report_dead` drift (1→0) but the gate remains
   red on five other checks. `spotcheck-identity` passes because round 77
   postdates the pinned round-73 base. This is consistent with r79 WB4a and
   contradicts the seat prompt's expected guard failure; the tested world
   nevertheless does not reach 6/6.
6. **E5 did not alter any of these readings.** The r72 counter, the
   LINE_CAP-60 probe, and the final pinned E5 counter all returned the same
   guard/battery values. In this set, instrument pins and the 40→60 cap are
   nonbinding: all worlds retain 22 additions / 3 deletions against the
   pinned guard base and touch no battery instrument.

## Scope, hygiene, blockers

- Lane build artifacts: seven world patches (W0 is empty); verbatim receipts
  for the r72 counter, the E5 cap-only probe, and the final E5 counter; the
  final counter self-test receipt; and `Kb80L02Ctl.worlds.json` mapping world
  commits, patch hashes and readings. The final counter was E06's published
  file, not a local derivation; its final pin table names both reviewed blobs.
- The report is this seat's only write under `w1/`. No lane commit/index/
  checkout/stash, no tracked lane files outside `.ufo/waves/round-80/`, and
  no prohibited files were modified.
- Scratch `/fast/scratch/hyaku/kotoba-r80/Kb80L02Ctl/` was removed after all
  receipts were copied into the build directory. No tool installations or
  upgrades. Counter processes were run at most two concurrently.
- Every counter command's own exit was captured in its receipt, never via a
  downstream pipeline. Final E5 `--self-test` output is
  `self-test: 0 failure(s) over 69 assertions`, exit 0.

VERDICT: No r79-derived shortcut world reached 6 of 6 on the final E5-amended counter (best W5 = 2 of 6); C1's control-world kill rule is not triggered. W7's expected spotcheck-identity failure is impossible for the specified round-77 file because it is outside the pinned base set; empirically the guard passes while report_dead clears.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80L02Ctl.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L02Ctl.W0.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L02Ctl.W1.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L02Ctl.W2.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L02Ctl.W4.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L02Ctl.W5.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L02Ctl.W6.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L02Ctl.W7.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L02Ctl.receipts-e5counter.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L02Ctl.receipts-e5cap-probe.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L02Ctl.receipts-r72counter.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L02Ctl.e5-selftest.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L02Ctl.worlds.json
