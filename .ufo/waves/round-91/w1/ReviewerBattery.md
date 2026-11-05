# ReviewerBattery r91-w1 — C1 attack report (battery arms, guards disabled in turn)

Candidate: 9af1a7af2adf0ab07cfd53f92affc1ed8d992262 + ExecBatteryArms.patch only (scratch clone
commit 5edb26f83988bef98d4f41a60a465ec82078f881). Patch unchanged. Full evidence with commands and
observed lines: .ufo/waves/round-91/w1/ReviewerBattery/review.md (receipts alongside).

- (a) PASS — `git apply --check` on a fresh base clone rc 0 ("APPLY --CHECK OK"); manifest parses:
  23 rows (kill 17, equivalent 6, survivor 0), three mb rows present, targets == PROBES keys
  (FG, D5, BAT), every anchor matches exactly once on candidate bytes, every mutant compiles.
- (b) PASS — candidate `--self-test`: `0 failure(s) over 25 assertions`, rc 0 (base 19 → 25; ≥ 22).
  Frozen predicate run at the candidate: `mutation battery killed 17 of 17 kill-set; equivalents
  survived 6 of 6; disclosed survivors 0 of 0`, G1/G2/G3 PASS, rc 0.
- (c) PASS — manifest-recipe replays (json.loads + anchored regex, findall==1): mb-m2 → rc 1
  (`1 failure(s) over 25 assertions`, FAIL names the G1 commit-check arm); mb-m15 → rc 1 (2
  failures, G1 clean-tree arm); mb-m16 → rc 1 (2 failures, G2 restore read-back arm). Each flips
  red for its own arm; none stays green.
- (d) PASS — G1 independence: added arm code contains no file reads (no open/read_bytes/read_text);
  behavioral proof — sabotaged working tree (garbage manifest + appended battery line) leaves the
  candidate run at 17/17 rc 0, targets byte-identical after runs (cmp vs `git show rev:path`).

Findings: (1) method hazard for mutation-tester seats — in an unstaged-patch clone, `git checkout
-- <path>` restores the INDEX (base) bytes; a first replay round then "went green over 19
assertions" because it tested the base instrument, not the candidate (artifact, not a defect);
keep pristine copies outside git. (2) mb-m15/mb-m16 anchors also match base bytes (shared text;
kill channel is the candidate-only arms). (3) Calibration headroom only: battery run 26 s → 39 s
with the third probe target, well inside PROBE_TIMEOUT.

No C1 defect found in ExecBatteryArms.patch. No tool installs performed.
