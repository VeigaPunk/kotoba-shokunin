# ReviewerD5Gate — round 89, wave r89-w1 (seat-scoped findings)

Gate under review: `verifiers/check_r86_routed_repairs_v3.py`
sha256 `1c110fb1fd9c7722d40e20d9dbe16b25f4bc1e00cfa41c889fe0a4e8924610f0` (unchanged across the review;
verified before and after every probe). D5_READY sha256 matched `1c110fb…`; CTL_READY content matched
the five polarity lines. Full evidence: `.ufo/waves/round-89/w1/ReviewerD5Gate/review.md` (this
directory); all probe worlds and digested receipts left in
`/fast/scratch/hyaku/kotoba-r89/ReviewerD5Gate/`.

## Control polarity re-derivation (from ExecCtlWorlds receipts)

- w_added_instance: own clone, own re-run → exit 1 naming d5iii, `instance drift 2`
  (`commit_total 62>61`, `commit_unresolvable 2>1`). MATCHES receipt.
- w_healed: own clone, own re-run → exit 0, `5 of 5`, drift 0; healed red passes. MATCHES receipt.
- w_silenced / w_rerecorded / w_tip / ctl-equivalence / ctl-v2-blindness: receipt bodies verified
  line-by-line; mechanisms additionally exercised through stricter forged worlds; no contradiction found.
- ctl-v2-blindness verified independently: frozen v2 self-test still prints
  `1 failure(s) over 16 assertions` on arm `w_added_red` (reviewer re-ran it at the lane) — the
  v3 replacement is genuinely discriminating where v2 is blind.

## Forged worlds beyond the declared controls (own clones from pristine `43fc784`)

| world | attack | gate |
|---|---|---|
| f_renamed | red check renamed | exit 1 via d5i+d5ii+d5iii+snapshot_tampered |
| f_shrink_plus_newred | one red name shrinks + one new red name | exit 1 |
| f_added_green | added finding under a GREEN name | exit 1 via d5ii+d5iii (`commit_nonhash 1>0`) — never 0 |
| f_tamper_digest | tampered receipt digest (baseline→0×64) | exit 1, snapshot_tampered |
| f_truncated_obs | receipt observation truncated (a missing name) | FAILS CLOSED: d5i+d5ii+d5iii; missing ≠ zero |
| f_truncate_both | both sides truncated the same name | exit 1 (digest pin catches the script edit) |
| f_two_deltas | heal one red + grow another simultaneously | exit 1 naming ONLY the growth legs (`report_dead 2>1`, `report_total 142>141`); heal leg unpunished |

No world where v3 exits 0 while worse than the receipt — except **F1** below.

## Findings

**F1 (HIGH) — receipt-value laundering reads exit 0.** `--write-base-receipt` output is data;
`load_receipt` validates format only, and `snapshot_tampered` pins the INTEGRITY SCRIPT and
BASELINE digests — not the receipt's own numbers. Reproduced: byte-identical `w_added_instance`
world (verified `WORLD-IDENTICAL`/committed-diff-empty) against a receipt whose `observed` values
were inflated (commit_total 61→999, commit_unresolvable 1→999; schema and both pinned digests
untouched) → every leg PASS, `closed 5 of 5`, `instance drift 0`, **exit 0**. Exposure: the
landing-receipt command `git diff <freeze> <landing> -- verifiers verifiers/fixtures plans corpus`
does not cover `.ufo/waves/round-89/receipts/d5v3-base-receipt.json`, so a post-score receipt edit
sits outside the receipt-command that is supposed to prove no post-score byte change. Fix
suggestion (pre-score, does not widen the predicate): pin a self-digest of the receipt body minus
the digest field, printed at write time and enforced as a snapshot-class failure when supplied.

**F2 (MEDIUM) — location flip yields exit-1 false refusal; plan requires exit 2.** Lane-shaped
receipt (`report_dead` PASS 0) vs bare-clone-measured world (`report_dead` DRIFT 1) →
`FAIL d5iii report_dead 1>0`, **exit 1** (an affirmative verdict naming a leg). plans/round-89.md
§C2 Q79 requires "could-not-evaluate for a flipped world"; the gate has no flip detector
(compare() never reads the receipt `root` field — F3, LOW, same mechanism). ExecCtlWorlds recorded
the same hazard in ctl-equivalence.txt (their finding, not repaired). Freeze-blocker: the L1 must
keep receipt-root and measured-root in the same location class, or measure worlds in the
lane-shaped scaffold — never a bare clone against a lane receipt.

**Non-findings:** leg ladder, first-failing-leg naming, strict `>` growth with heals allowed,
case-sensitive name handling, hard (not warn) digest failures, `observed`-key reads, bool/non-int
rejection, TMPDIR-only writes — all checked in source, no escape hatches. D1–D4 comment-stripped
bodies diff 0 hunks vs frozen r87 except the replaced D5 function itself (its removal is the
declared surface change); all carried constants byte-identical; self-test
`0 failure(s) over 33 assertions`, exit 0.

## Verification gaps

w_silenced / w_rerecorded / w_tip were verified by receipt-consistency plus stricter forged probes,
not re-run as dedicated worlds (budget cap). F1/F2 repairs, if adopted, must land before the first
candidate score per the frozen C2 kill rule.

— ReviewerD5Gate
