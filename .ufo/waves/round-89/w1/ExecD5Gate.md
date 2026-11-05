# ExecD5Gate — r89-w1 seat report

Seat: ExecD5Gate (C2 instrument — instance-level D5 successor gate). No lane-identity
heading; files and headings carry this seat name only.

## Files written

- `verifiers/check_r86_routed_repairs_v3.py` (new, 1166 lines, Python stdlib only,
  `python3 -B`). sha256
  `1c110fb1fd9c7722d40e20d9dbe16b25f4bc1e00cfa41c889fe0a4e8924610f0`.
- `verifiers/fixtures/d5v3/fixture_integrity.py` (new, committed fixture template;
  MODE-driven worlds: base / healed / added / silenced / renamed / newred /
  rerecorded / brokenselftest / garbage). sha256
  `9e1abf00b63ba5e0168978c66292ee0aa0e17cf928d575df6a76b0325793e9a9`.
- `.ufo/waves/round-89/w1/ExecD5Gate/self-test.txt` (self-test receipt).
- `.ufo/waves/round-89/w1/D5_READY` (content: the gate sha256 above).

Frozen instruments untouched: `check_r86_routed_repairs_v2.py`,
`verify_corpus_integrity.py`, `corpus-baseline.json` — no byte changed
(`git diff --stat a5b3b15c..HEAD -- verifiers/` empty at seat start; only this seat's
two new files added since). The lane's base receipt was NOT written (L1 owns it).

## Behavior (frozen predicate, plans/round-89.md § C2)

- `--write-base-receipt <path>`: measures the lane with cwd = the lane root, pins
  lane HEAD revision, working-tree sha256 of `verify_corpus_integrity.py` +
  `corpus-baseline.json`, and the full `--json` observation dict (nine checks with
  live values). Refuses to pin anything but nine names (v2:54 NAME_COUNT anchor).
- `--base-receipt <receipt> [--root <dir>] [--print-observation]`: re-measures with
  cwd = the measured root; legs d1–d4 (carried from r87:322/350/379/401 via the v2:172
  binding, reimplemented, each cites its v2/r87 line; rev = the measured root's HEAD,
  committed bytes via `git show` only) then d5i (name-list equality AND the root's own
  integrity `--self-test` exit 0), d5ii (measured DRIFT set ⊆ receipt's), d5iii
  (per-name observed ≤ receipt value; `instance drift K` counts growths), snapshot
  (both pinned digests match working-tree bytes). Exit 1 names the FIRST failing leg
  in the fixed order d1, d2, d3, d4, d5i, d5ii, d5iii, snapshot_tampered; exit 2 for
  anything unevaluable (malformed receipt, integrity exit 2/3, non-JSON, duplicate
  names, unreadable digests). Prints `r86 routed defects closed N of 5` and
  `instance drift K`.

## Evidence (all commands run this session)

1. `python3 -B verifiers/check_r86_routed_repairs_v3.py --self-test` (TMPDIR =
   /fast/scratch/hyaku/kotoba-r89/ExecD5Gate) →
   `0 failure(s) over 33 assertions`, exit 0. Arms: 9 pure d5i/d5ii/d5iii arms on
   micro observation dicts, 3 synthetic-receipt-file arms (load round-trip,
   wrong-schema refused, malformed digest refused) under the process TMPDIR, 9
   end-to-end world arms (w_tip exit 0; w_healed exit 0; w_added_instance exit 1
   naming d5iii with drift 2 and d5ii PASS — the r88-blindness discriminator;
   w_silenced exit 1 d5i; w_renamed exit 1 d5i; w_newred exit 1 d5ii; w_rerecorded
   exit 1 snapshot_tampered with d5i/ii/iii PASS; w_brokenselftest exit 1 d5i;
   w_garbage exit 2), and 11 carried D1–D4 arms (positive + ≥1 must-fail per check).
2. Real-lane smoke at HEAD `0f2b86689c2914bad8ba73a89698e6c37258709d`:
   `--write-base-receipt <scratch>/smoke-base-receipt.json` exit 0 (9 names, 5 DRIFT);
   `--base-receipt <same> --work <scratch>` exit 0, all eight legs PASS,
   `r86 routed defects closed 5 of 5`, `instance drift 0`; the measured DRIFT set is
   exactly the plan's honest-bound five (`index.tracked_files`, `index.unindexed`,
   `pointers.report_total`, `pointers.commit_total`, `pointers.commit_unresolvable`);
   d1 carried receipts verified against `04647b0f..0f2b8668`; d2 validator read
   (10 roles, no planner). `--print-observation` smoke: exit 0, emits
   `{observed, results}` with 9 checks.
3. Zero temp-path literals in the gate source (grep `/tmp` → no hits).

## Findings

1. **Exit-code harmonization for the d5i self-test conjunct (decision, documented in
   the gate docstring).** The plan's D5(i) sentence makes "integrity --self-test exits
   0 at the measured root" a d5i conjunct, while the Q79 discipline sentence says a
   root whose self-test fails is could-not-evaluate. Reading adopted: a self-test that
   RUNS and exits nonzero is a NAMED d5i failure (exit 1, detail "names equal but
   integrity --self-test nonzero at the root"); only a self-test that cannot run at
   all (OSError/timeout) is exit 2. This is the only reading under which the frozen
   w_silenced control (exit 1 naming d5i) holds for every way of silencing a check.
2. **L1 freeze command shape.** At the freeze the L1 should run
   `python3 -B verifiers/check_r86_routed_repairs_v3.py --write-base-receipt
   .ufo/waves/round-89/receipts/d5v3-base-receipt.json` (cwd = the lane root, clean
   tree at the freeze revision). The receipt pins the lane HEAD + the two digests +
   the full observation dict; comparison worlds then run
   `--base-receipt <receipt> --root <world-checkout>`.
3. **v2 blindness reconfirmed from my fixture arm, not by editing v2.** The
   added-instance world class that v2's frozen name-set gate reads as PASS is exactly
   the class my d5iii leg names (w_added_instance arm); v2 stayed byte-identical and
   its own self-test still prints its known `1 failure(s) over 16 assertions`
   (before-state receipt) — untouched this seat.
4. **World construction constraint (already in the bounds, restated for ExecCtlWorlds):**
   worlds must be `git clone -q --shared` checkouts of the lane with one world commit
   on top — D1–D4 read the world HEAD's committed bytes (round-86 receipts, D2/D4
   carriers, instrument blobs), so a world without lane history would name d1 as the
   first failing leg instead of the intended D5 leg.

## Risks

- None observed. No tool installs (operator 2026-10-19 rule: nothing installed, pacman
  untouched). Scratch `/fast/scratch/hyaku/kotoba-r89/ExecD5Gate` deleted at seat end;
  nothing written outside the four owned paths above.
