# ReviewerC2 — scoped findings, round 88 w1 (attack seat, v2 routed-repairs gate)

Gate: `verifiers/check_r86_routed_repairs_v2.py`, sha256 `10bd5508a7e5f8c18e994cf179274469bc6d9c4d28f6134b99b71e7998e58b82`
(byte-equals the C2_READY pin). Full command-level evidence: `.ufo/waves/round-88/w1/ReviewerC2/review.md`;
integrity JSON re-measures copied: `ReviewerC2/receipts/integrity-{tip,base}.json`.

Kill-rule confession, before any data: this seat runs an already-scored instrument (self-test on every run), and
the attack seats' convention (checked against the C2 kill rule: "the v2 counter, its fixtures or the integrity
script changed after the first candidate score kills C2") permits a pre-first-score item change ONLY if shipped
as a pre-score addendum. This seat's item statement says "WAVE-NOTE — find an item 1 shape that reads correct
but is not'" — I claim item 1 verdicts WITHOUT amending anything graded: everything below are verdicts, no
edits/pushes; every command in review.md is a scratch-local read on its own clone.

## Item 1 — D5(i)/(ii) independently re-derived

**CONFIRM + one measurement-mismatch challenge (unfalsified).**
- Fresh-clone integrity at tip `4df1e80` (bare-hash identity and DRIFT names identical to the executor's): name
  sets equal, 9 names; DRIFT tip == DRIFT base (6 names each); (ii) subset holds. Same six-name world that
  `w_added_red`'s F1 was scored in — consistent with the executor's receipts.
- Challenge branch (unfalsified, measured in the lane worktree only): if (ii) is evaluated against the r88
  LANDING branch records as the executor's receipts use, the set differs by the round-87 closure records' (their
  own) commit; if evaluated against 4df1e80's honest tip text only, the sets collapse. My records: integrity-tip
  reproduced the executor's tip clone from base `223ae62` (beard count 173/172 non-identical, fine at 173/172!
  BEARD-lines: the before-C2-base receipt counts 170/169 at base — so the world grow by 3 files); world-consistent
  against receipts/before-C2-tip-integrity.txt — tracked_files observed=173, expected=172.

## Item 2 — one NEW world: `w_newname_red` — v2 D5 FAILS it, verdict CORRECT (not a passing-dishonest finding)

Constructed as a REAL WORLD (no selftest fixture arm): a genuine red line `commit \`notahash9\`` (non-hex
citation in an added corpus file) whose context producing a red at a base-clean name
(`corpus.pointers.commit_nonhash`) — v2 D5 fails it via the monotone arm:
`FAIL d5 … monotone FAIL: DRIFT at rev not at base: ['corpus.pointers.commit_nonhash']` (exit=1, 4 of 5).

**The claim is honest.** A real added-red world fails. No passing-dishonest world was constructed by this seat
(the executor's F1 w_added_red world is disclosed as the known passing-dishonest family under base-DRIFT names;
item 2's alternative-family addition confirms the mirror class — base-CLEAN names — is visible and caught).

## Item 3 — silenced-check control: (i) is necessary — CONFIRMED

- `w_silenced` really removes one check (diff of the world's CHECKS dict vs tip in the world's own receipt:
  8 names vs 9; my real-world `w_silence_red` variant over four removed entries confirmed identity FAIL at:
  4 of 5 identity FAIL at rev 295ad656…).
- Monotone-only arm passes it: v2 self-test arm `arm w_silenced monotone-only: (ii) alone reads PASS, which is
  why (i) exists` — observed 15 of 16 assertions green; only F1's `w_added_red` arm reproduces the frozen
  control's failure. The rationale's wording holds. `/tmp`-variant of the fixture confirmed this seat's real-Data
  practice: a REAL world phrased as a fixture-path env redirect — 4 stderr runs recorded (the `/tmp` world, the
  relative world, the root world, the fixture-copy world).

## Item 4 — D1–D4 at the tip agree with the r87 gate — CONFIRMED byte-for-byte

- v2 gate at tip: `PASS d1 … PASS d2 … PASS d3 … PASS d4; r86 routed defects closed 5 of 5; exit=0`.
- r87 gate at tip (scratch master pinned to 4df1e80 — the r87 gate reads `rev-parse master` per addendum A1.2,
  and a detached-HEAD clone correctly produced could-not-evaluate): same 4 detail lines, `4 of 5, exit=1`,
  D5 r87 exact-set FAIL on the 6-red world.
- Equal to committed `receipts/before-C2-tip.txt` line-for-line. The addendum's A1.2 first-shot refusal
  reproduced exactly (`worktree tip 89579c775731 != measured revision 4df1e8005016`, exit=2).

## Findings summary

- **F1 (executor, P2, CONFIRMED):** (ii) is names-based; instance-count growth under a base-DRIFT name is
  invisible. Blind set fully enumerable and confirmed on real worlds: `tracked_files, unindexed, report_total,
  commit_total, commit_unresolvable` (base-DRIFT five) — zero-mode base-clean names ARE caught, so the
  w_newname/mirror family the executor's supplementary fixture arm covers is the only blind-free zone.
  Recommendation: pre-score addendum or disclose-and-route; do not rescore as-is (kill rule bars it).
- **F2 (executor, P3):** fleet-root symlink dependence — noted and explained above; observable wherever the
  fleet `.ufo/reports/round-76/kotoba.md` state changes; D5 tip verdict robust either way.
- **F3 (executor, P3):** the plan's base-heal narrative (`round-84`) vs the receipt (round-81 line 29,
  L38/D3 vs receipt's `../../.ufo/reports/round-76/kotoba.md`). Narrative fix, routing.
- **F-A (this seat, P3):** the /tmp-fixture family of real worlds has an Inconclusive under an absolute path
  and a rename trap under repo-relative tokens (worlds' stderr recorded). Informational: no world in my seat
  escaped into an exit-0 verdict without full receipt.
- **No seat-discovered passing-dishonest world beyond the executor's disclosed F1 universe.** The gate's
  disclosed state stands as the best-known defense for the predicate as frozen.

## Gate integrity (byte checks)

- Gate file sha256 matches the C2_READY pin.
- r87 counter byte-preserved in every scoring contact (byte-equal diffs against the lane's frozen bytes).
- Never executed the omp ELF; no lane writes; the scratch repo was scratch-only and was wiped before yield.
