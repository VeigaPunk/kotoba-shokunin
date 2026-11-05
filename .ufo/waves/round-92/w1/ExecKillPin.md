# ExecKillPin — C2(a) build: kill-set-size pin in check_mutation_battery.py (round 92, w1)

Seat: ExecKillPin. Base: e073723ae667b64e534f8621bddb83ad12ad0e71. Owned file: verifiers/check_mutation_battery.py only.
Patch: .ufo/waves/round-92/w1/ExecKillPin/ExecKillPin.patch (68 lines, `git diff --cached --binary` from base;
`git apply --check` at base passes in a scratch clone). READY: .ufo/waves/round-92/w1/ExecKillPin_READY (`KILLPIN-READY N=28`).

## Change
- `KILL_SET_PINNED = 17` (module constant, comment names the freeze commit).
- `kill_set_size(text)` counts `kill` rows through the existing `parse_manifest` (the G1 parse path).
- `kill_set_check(text)` returns (pass, "observed X kill rows, pinned Y"); a malformed text returns a named fail, not a raise.
- Self-test: three new assertions (25 -> 28), all named `arm kill-set-size: ...`:
  1. the live manifest's kill-row count equals the pin;
  2. a manifest with the first kill row dropped is refused by the pin;
  3. an unparseable manifest is refused, not raised.
- Docstring: one sentence on the new arm. No predicate line, PROBES, manifest, or existing arm changed.
  Existing mutation anchors (mb-m2, mb-m15, mb-m16 target this file) are untouched; the --rev measurement below proves it.

## Receipts (all under .ufo/waves/round-92/w1/ExecKillPin/)
- honest-selftest.txt: `0 failure(s) over 28 assertions`, rc 0 (in a scratch clone with the patch committed).
- dropped-row-selftest.txt: `kill rows before=17 after=16`; `FAIL arm kill-set-size: the live manifest's kill-row count equals the pin :: observed 16 kill rows, pinned 17`; `1 failure(s) over 28 assertions`; self-test rc=1.
- nomanifest-rev.txt: manifest deleted at a scratch commit, `--rev <that>` -> `could-not-evaluate: G1: git show <rev>:...manifest.tsv failed`, rc 2 (no traceback).
- nonrev-rev.txt: all-zero non-commit rev -> `could-not-evaluate: G1: ... is not a commit`, rc 2.
- honest-rev-measure.txt: honest `--rev` on the patched scratch commit f7f9e266242c -> G1/G2/G3 PASS, `mutation battery killed 17 of 17 kill-set; equivalents survived 6 of 6; disclosed survivors 0 of 0`, rc 0 (all mb-* guard rows killed, the self-test probe baseline holds at 28).
- no-live-manifest-selftest.txt: a copy of the patched battery with no manifest beside it -> `FAIL arm kill-set-size ... manifest malformed: manifest header must be ...`, rc 1, no traceback.
- rp-killpin.sh: the dropped-row procedure (see deviation 3).

## Deviations from the item text (decided here, flagged for the L1)
1. **Pin is a literal, not derived at load.** A constant computed from the same bytes it is then compared against
   can never fail, so "derived at load" as a self-compare is tautological. The pin is the independently recorded freeze
   count (17 = `grep -cP '\tkill\t'` on the freeze-commit manifest, and 17 = parse_manifest kill rows). Consequence by design:
   any future kill row added or dropped must move KILL_SET_PINNED in the same commit.
2. **Arm reads the working-tree manifest, not `git show <rev>:MANIFEST`.** The red-before world (receipt
   redbefore-m6-dropped-row.txt) removes the row in the working tree only, uncommitted; a committed-rev read cannot see it
   and the arm would stay green there, which the item forbids. In the evaluate() probe context the self-test runs inside the
   scratch clone detached at --rev, where the working tree equals the rev bytes, so the rev's manifest is what gets pinned
   when the battery measures a revision (confirmed by honest-rev-measure.txt). Standalone self-test reads the lane the script lives in.
3. **rp-m6 procedure re-run against the patched file.** rp-m6-dropped-row.sh clones the lane at base and runs the base
   battery, so it cannot exercise the patch. rp-killpin.sh is the same steps (clone at base, drop the first kill row in
   the working tree, run self-test) with the patched battery copied in. The base red-before receipt is unchanged.

## Findings / risks
- Self-test count moves 25 -> 28 (N >= 26 met). Any future hand-edit of the mutation manifest's kill rows will fail
  this arm until KILL_SET_PINNED is bumped; that is the intended pin, not a regression.
- The arm does not check that the manifest's kill-row targets are the battery's own; it counts rows, as specified.
- Nothing was installed; no host, kernel, or sysctl change; no commit in the lane; no edit outside the owned file.

## Checks for the L1 (main agent) to run at integration
- `python3 -B verifiers/check_mutation_battery.py --self-test` -> `0 failure(s) over 28 assertions`, rc 0.
- `python3 -B verifiers/check_mutation_battery.py --rev <landing> --work <scratch>` -> killed 17 of 17, rc 0.
- Not verified by this seat: whether any floors-registry row or tip-battery INSTRUMENT_PINS entry pins the blob of check_mutation_battery.py. This patch adds no such admission; the L1 must check the Q73 sweep (receipt q73-sweep-raw.txt) at integration and run `check_tip_battery.py --rev <landing>` to see the pin guard.
