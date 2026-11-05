# ReviewerD5Gate — independent review of the instance-level D5 gate (C2, round 89 wave 1)

Seat: ReviewerD5Gate (attack seat). Date 2026-11-05. Gate under review:
`verifiers/check_r86_routed_repairs_v3.py`, sha256 `1c110fb1fd9c7722d40e20d9dbe16b25f4bc1e00cfa41c889fe0a4e8924610f0`
(byte-identical at review start and end; confirmed by sha256sum before and after every probe).
Reviewer scratch: `/fast/scratch/hyaku/kotoba-r89/ReviewerD5Gate/` (lane never written except this
review dir). All worlds built from a shared clone of the lane at the plan-draft revision
`43fc7840202d542bcd1f5d7fab6e6f3dbb7f19b3`; every world asserted
`git rev-parse --show-toplevel` == that world dir before any commit.

## 1. Re-derived control polarities

Receipt source: `.ufo/waves/round-89/receipts/ctl-*.txt` (ExecCtlWorlds). Each receipt's command,
output and exit were re-executed in the reviewer's own clones; the receipts do NOT name their
clones inside the file (shell level), so the reviewer re-ran the same gate bytes (`1c110fb1…`) with
`--base-receipt` written by the reviewer's own `--write-base-receipt` in a pristine clone.

- **w_added_instance** — world rebuilt from the committed delta (one line appended to
  `corpus/lessons/round-88-verifier-spotcheck.md` citing 40-hex unresolvable
  `0123456789abcdef0123456789abcdef01234567`; confirmable byte-for-byte against
  `worlds/w_added_instance/.git` index blob d62bc7c. Own clone run:
  `python3 -B verifiers/check_r86_routed_repairs_v3.py --base-receipt base-receipt.json --root worlds/w_added_instance`
  → `FAIL d5iii instance growth under: ['corpus.pointers.commit_total 62>61', 'corpus.pointers.commit_unresolvable 2>1']`,
  `r86 routed defects closed 4 of 5`, `instance drift 2`, **exit 1**.
  Receipt `ctl-w_added_instance.txt` declares exactly this (d5iii, drift 2, closed 4 of 5). MATCH.
- **w_healed** — reviewer's clone of ExecCtlWorlds' world (commit `bbae42f`, one line of
  `corpus/lessons/round-81.md` re-pointed to the resolvable base commit). Own run: `closed 5 of 5`,
  `instance drift 0`, **exit 0**. Receipt matches. `commit_unresolvable` DRIFT row is REMOVED from
  the world's DRIFT list (heal), `d5ii` reads subset → PASS. MATCH.
- w_silenced / w_rerecorded / w_tip / equivalence / v2-blindness receipts read; polarity shapes
  agree with receipt lines; these three were additionally exercised through the forged-world probes
  below (same mechanisms, stricter worlds) and never contradicted.

All six ExecCtlWorlds receipts carry both halves of their declared output (`closed N of 5`,
`instance drift K`) plus the full 8-leg PASS/FAIL list, so "declared vs observed" is checkable
line-by-line; reviewer found no receipt whose declared exit or body line disagrees with its command.

## 2. Forged worlds beyond the declared controls (all from the pristine base clone; gate bytes pinned 1c110fb1, sha256-verified before and after)

| world | forge | gate result | verdict |
|---|---|---|---|
| f_renamed | red check `corpus.pointers.commit_total` renamed to `…commit_count_renamed` in the world's copy of `verify_corpus_integrity.py` CHECKS (counts unchanged) | exit 1, `FAIL d5i` (missing/extra names) + `FAIL d5ii` (new DRIFT name) + `FAIL d5iii` (`commit_count_renamed (no receipt value)`) + `FAIL snapshot_tampered` | refused, no escape hatch |
| f_shrink_plus_newred | `report_total` shrunk 141→140 under an already-red name + new red name `commit_nonhash_new` (same measured output key, renamed check id) | exit 1, d5i/d5ii/d5iii/snapshot_tampered all FAIL | refused |
| f_added_green | one new finding under a formerly GREEN name, integrity script untouched (`commit_nonhash` 0→1 honest) | exit 1, `FAIL d5ii new DRIFT names ['corpus.pointers.commit_nonhash']`, `FAIL d5iii commit_nonhash 1>0`, `drift 1` | refused, never exit 0 |
| f_tamper_digest | receipt `baseline_sha256` replaced with `0`×64, measured world pristine | exit 1, `FAIL snapshot_tampered pinned digests differ (… baseline 000000000000 vs 6fdabfac8189)` | gate names declared-vs-observed, refuses |
| f_truncated_obs | receipt observation dict truncated (9→8 rows, `commit_unresolvable` row removed, digests intact) measured against an honest pristine world | exit 1; `FAIL d5i check names differ … extra ['corpus.pointers.commit_unresolvable']`; `FAIL d5ii`; `FAIL d5iii (no receipt value)` | **fails closed** — a missing receipt name is GROWTH, never treated as zero |
| f_truncate_both | both sides truncated the same name (world script edited, receipt truncated to match) | names 8 = 8 BUT `FAIL snapshot_tampered` (the world's script edit moves the pinned integrity digest) → exit 1 | digest pin closes the bilateral-truncation hole |
| f_two_deltas | one red healed (`commit_unresolvable` re-pointed to a resolvable commit) + a second simultaneous GROWTH (`report_total` 141→142, `report_dead` 1→2) | exit 1, names exactly the growth legs `['corpus.pointers.report_dead 2>1', 'corpus.pointers.report_total 142>141']`, heal leg is not punished (`d5ii` reads subset PASS) | refused, growth named |

**No forged world reads exit 0 while being worse than the receipt — except Finding F1 below, which
is an attack on the receipt itself, not on the world, and which the gate cannot see.**

## 3. Source-level escape-hatch audit

- Comparison directions: `growth_names` uses strict `>`; heals (value decreases) are allowed —
  matches the plan ("a healed red passes"). No `>=`-reversed reads found.
- `drift_subset` uses `set <= set` (strict direction correct: new red names fail, heals pass).
- `names_equal` compares sorted full name lists (case-sensitive Python string ordering; nothing
  coerces case). No `.lower()` on any name path; the only `.lower()` in the file is a decision-cell
  reader in D3 — unchanged from r87 and not part of D5.
- Missing-as-zero: absent receipt values make `growth_names` report the name (fail-closed); absent
  measured names make `names_equal` fail. Never treated as zero.
- Digest checks are hard FAILs, not warns: `snapshot_tampered` FAIL immediately drives the exit
  ladder to 1; no "warn and continue" path exists for any leg.
- Values come from the row's own `observed` key (`row.get("observed")`); no cross-key read.
- Non-int values (including bools) are rejected as could-not-evaluate, not coerced.
- The `finally: shutil.rmtree(work)` cleanup writes only under the caller-supplied `--work`/TMPDIR;
  the gate never writes outside the receipt path.

## 4. D1–D4 drift from frozen v2/r87 semantics

The v3 file reimplements D1–D4. Comment-stripped op-level diffs against the frozen
`verifiers/check_r86_routed_repairs.py`: `check_d1` 0 hunks, `check_d2` 0, `check_d3` 0,
`check_d4` 0 (the 10 removed lines after `check_d4` are r87's old `check_d5` constants — the
instance-level D5 replaces exactly that function; there is no carried meaning drift). All shared
constants byte-identical: `LANDING_REV`, `CATALOGUE_LINE`, `REGISTRY_LINE`, `INSTRUMENTS`,
`PLAN`, `LESSON`, `KILL_BOUNDARY`, `MIN_READER`, `MIN_REASON_WORDS`. Self-test
(`0 failure(s) over 33 assertions`, exit 0) covers every D5 leg plus carried D1–D4 positives and
must-fail arms, each naming the arm it guards.

## 5. Findings

### F1 (HIGH) — receipt-value laundering reads exit 0; nothing re-derives the receipt from the snapshot digests
Reproduction, byte-identical `w_added_instance` world (`ce992ad14c4cc…`; lesson blob diff vs the
lane's warm state == one added line, verified `WORLD-IDENTICAL` by `git show HEAD:…` diff == empty):
  base receipt values `commit_total` 61 → 999 and `commit_unresolvable` 1 → 999 edited in place
  (schema, digest FORMAT, and the two snapshot file digests untouched);
  `python3 -B verifiers/check_r86_routed_repairs_v3.py --base-receipt receipt-inflated2.json --root <that world>`
  → `PASS` on every leg, `closed 5 of 5`, `instance drift 0`, **exit 0**.
`snapshot_tampered` pins only `verifiers/verify_corpus_integrity.py` and
`verifiers/corpus-baseline.json`; `load_receipt` validates format, never provenance. A receipt is
data, and the gate treats its observation as ground truth. In this wave's flow the exposure is
narrow but real: the gate author (ExecD5Gate) and the receipt author (ExecCtlWorlds) are
different seats and the freeze commit lands both, but the frozen landing-receipt diff
(`git diff <freeze> <landing> -- verifiers verifiers/fixtures plans corpus`) does NOT cover
`.ufo/waves/round-89/receipts/d5v3-base-receipt.json`, so a post-score receipt edit is outside the
very receipt-command that is supposed to prove no post-score byte change. Recommendation (not
applied — finding only): have `--write-base-receipt` also pin `receipt_sha256` = sha256 of the
receipt body minus that field, print it, and have `compare()` refuse (snapshot-class) when a
caller-supplied `--receipt-sha256` disagrees; alternatively pin the observation dict sha and make
the L1's landing-receipt command include the receipts/ path of the base receipt.

### F2 (MEDIUM) — location flip produces exit-1 false refusal where the plan requires could-not-evaluate; no flip detector
Measured: a lane-shaped receipt (`report_dead` PASS 0) vs a bare-clone-measured world
(`report_dead` DRIFT 1) → `FAIL d5iii report_dead 1>0`, `closed 4 of 5`, **exit 1** (a REFUSAL
naming a leg, not exit 2). plans/round-89.md §C2 Location discipline (Q79) says a location-flipped
verdict "is could-not-evaluate for that world, never a silent verdict" — exit 1 is an affirmative
verdict, so this leg of Q79 is not met by the gate itself. ExecCtlWorlds' ctl-equivalence.txt
records the same hazard (their finding, unrepaired by that seat); this review confirms it with an
independent measurement. Mitigation for the freeze: the L1 must keep receipt-root location class ==
measured-root location class (the receipt's `root` field is the hook) or measure worlds in a
lane-shaped scaffold; a clone-measured world against the freeze-hour LANE receipt must not be
presented as a scored reading.

### F3 (LOW) — the Wonderland receipts-vs-world harness never reads the receipt's `root` field
`compare()` never asserts receipt root vs measured root relationship. A caller may pair any
receipt with any directory (I ran a CLONE-written receipt against the LANE itself: `closed 5 of 5`,
exit 0, full pass at 09:0x). This is the operational half of F2; it is not exploitable beyond the
location flip unless combined with F1, but it belongs in the flip detector.

### Non-findings
- Leg ordering matches the plan (d1…d4, then d5i, d5ii, d5iii, snapshot_tampered; exit 1 names the
  FIRST failing leg; "closed N of 5" uses the d5-block single point plus per-leg d1..d4 count).
- `w_added_instance` grew two names (commit_total AND commit_unresolvable) — this is the correct
  honest reading (the citation adds one to both counters); drift 2 is not a miscount.
- ExecCtlWorlds supplied six receipts (five polarities + equivalence + v2-blindness = 7 files);
  the two extras are additive evidence, both grounded, and do not widen the frozen predicate.

## 6. Residual risk and verification gaps

- The reviewer did NOT re-execute w_silenced / w_rerecorded / w_tip / equivalence as dedicated
  world runs (budget): polarity shapes verified by receipt reading plus the stricter forged-world
  probes (sections 2 and 5), not by re-running those exact worlds. The three receipt bodies are
  internally consistent (leg list, closed-N, drift-K all agree).
- Whether the L1's freeze-hour receipt will be lane-shaped or clone-shaped is not yet fixed in the
  record; F2 makes this a freeze-blocker to resolve before the freeze commit lands.
- F1's fix (receipt self-digest) is a pre-score amendment if adopted: it does not widen the
  predicate, but it changes gate bytes — per the kill rules it must land BEFORE the first candidate
  score or ride an addendum, exactly as C2's own rule requires.
