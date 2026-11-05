# ReviewerRepairs — r90-w1 review (floors bump + index row)

Reviewer seat, read-only. Every path below is under /home/vgpnk/Projects/shokunin/kotoba-shokunin unless
noted. Scratch `/fast/scratch/hyaku/kotoba-r90/ReviewerRepairs` used for all clone work; deleted before this
yield. Evidence receipts copied to .ufo/waves/round-90/w1/ReviewerRepairs/ (see § Copies). No git/jj write was
made anywhere — all clone worlds were were created by `git clone -q --shared` from the lane and verified with
`git rev-parse --show-toplevel` == the clone path before any command inside them; no commit was made in them.

## Repair 1 — floors half-bump completion (verdict: SOUND)

Verified from committed bytes: `git diff 6af71591e7232a7eebbaff78e7db653a70c7218b --
verifiers/floors-registry.json verifiers/check_assertion_floors.py` → 6 hunks: docstring floor list +
registration note (2 adjacent), `EXPECTED_INSTRUMENTS` `+ "freeze_gate": 30`, `INSTRUMENTS` `+
"freeze_gate": ("verifiers/check_freeze_gate.py", 30, r"(?m)^(\d+) failure\(s\) over (\d+)
assertions$", 2, 1)`, F6 swap literal `18`→`19` (line 866) + comment paren (line 863). Nothing else.

Row-for-row agreement (my own check, executed): AST-parsing all three artifacts:
- `AST literal_eval` INSTRUMENTS/EXPECTED vs floors-registry.json: `mismatches: []`, `extra rows in tables: []`,
  `total entries len matches instrument_total: True`.
- Semantic registry diff vs base: only `instrument_total` 18→19 (structural JSON sort_keys diff: one line).
- BUT: the base registry already held the freeze_gate row (the r89 half-bump row), so `instrument_total` 19
  vs 19 entries reads as the registry "matching" on payload with the bump expressed only through the
  instrument_total field + tables; the r89 bump's COVERING (row exists) shape means `+freeze_gate` tables
  rows are load-bearing for REACH, not for consistency. My half-bump rebuild probe (own clone, worktree
  equal to base bytes for the guard — `worktree guard == base bytes: True`, base guard sha16
  `81624ad87b7869c4`) confirms: reverting the table rows only (OPTION-B) → rc=2,
  `FAIL registry size drift: instrument_total=18 but 19 entries in verifiers/floors-registry.json` alone;
  at the unmodified base state (tables absent + registry 18-with-row) → rc=2 with BOTH base-floors.txt lines
  byte-identical (`FAIL registry size drift: ...18 but 19...`; `FAIL registry row vanish: freeze_gate
  (listed in verifiers/floors-registry.json, absent from both guard tables)`) — both FAIL lines return.
- F6 sweep: `grep -n '"instrument_total": 18' verifiers/check_assertion_floors.py` → gone (exit 1); only
  one F6 literal at line 866 now reads 19. The literal is consistent with the r89 half-bump state because
  the harness compares the mutated-file literal against the registry inline in the same file's
  stub_registry/registry text, not against the integer 18 semantically (verified by execution: F6's own
  count-check still bites, 165 assertions total, `0 failure(s) over 165 assertions`, rc=0).
- Registry row floor: `json: floors-registry.json instruments.freeze_gate = {"floor": 30,
  "path": "verifiers/check_freeze_gate.py"}`; guard live reads it `PASS freeze_gate observed=30 floor=30`

Live run (bare, at my seat scratch copy of current tree): 19/19 PASS, `PASS freeze_gate observed=30
floor=30`, rc=0 (wall 182.16 s; copied to Copies/live-guard-after.txt). Current guard sha256 ==
FLOORS_READY (`7120c7d6c8412bf6e61826f3940f40b83e2e2b26d58d2bcf7175c99a83cfbadb`).

FINDING R1-a (MEDIUM, pre-existing, not introduced by the bump): `verify_harness_independent.py
--self-test` now takes ~167 s standalone on this host; the guard's child-cap base 120 s stands in the
round-56 class in reverse (idle host → 1-min loadavg < 1.4 → cap 129.8 s < real 167 s → false rc=2
`self-test timed out`). At high load or with a parallel sibling the factors hide it; my own full-run needed
180+ s and read the cap doubling. The `SELF_TEST_TIMEOUT_S = 120` base is load-scaled only
(`child_timeout_s(base, load)`), not wall-clock measured, so fixture growth (~3x since round 56 per
ExecFloorsBump Finding 1, consistent with my observation) can deterministically false-red every future
idle-host bare walk. Routed to the L1 (this is a floors-guard instrumentation limit, not my repair's
introduction).

## Repair 2 — index row (verdict: SOUND)

Verified from committed bytes: `git diff <base> -- corpus/README.md` → exactly one line added at line 186
(`| Round-89 verifier spot-check (indexed round 90) | lessons/round-89-verifier-spotcheck.md | ...`);
format mirrors r87/r88 sibling rows (lines 181–182: same 4-cell table shape, `lessons/<file>.md` column-2
token). Gate (my own run):
`python3 -B verifiers/verify_corpus_integrity.py --json` → `unindexed 0`, `unindexed_detail: []`
(index_patterns 198→199), rc=1 dominated by pre-existing stale *equal* checks: verified base-integrity.json
was already DRIFT on the same five checks (`corpus.index.tracked_files` 181, `pointers.report_total` 146,
`pointers.commit_total` 62, `pointers.commit_unresolvable` 1, `index.unindexed` 1→0 now). My no-row
scratch world (fresh clone, row removed, pristine committed README) returns `unindexed 1`
`['corpus/lessons/round-89-verifier-spotcheck.md']` rc=1, row removed → row present gives the exact
0↔1 flip. `index-regression.txt` (seat receipt) shows the same two readings; copies in § Copies.

## Repair 3 — battery command 1 and 2 reruns vs base receipts (verdict: SOUND, no new red)

`check_assertion_floors.py` (base battery cmd 1): base rc=2 with the two FAIL lines (base-floors.txt);
now rc=0, 19/19 PASS including freeze_gate 30/30 (no regression).
`verify_corpus_integrity.py --json` (base battery cmd 2): base rc=1 with DRIFT on 5 checks
(base-integrity.json); now rc=1 with the SAME DRIFT set (unindexed now PASS; no check that was PASS moved
to FAIL). Both my runs agree with the base receipts' classes; nothing new red from either repair.

## Reviewer-of-reviewer notes (new evidence-driven, cross-seat)

- ExecFloorsBump Finding 1 (child-cap drift) is confirmed by my own live walk timing (182 s wall vs
  round-56 docstring's 59 s claim) — the frozen docstring's round-56 arithmetic is now stale
  in the same direction (child runtime far larger than the flat base suggests); the repair completes the
  registry row without re-measuring that. Not a rescue target for this bump.
- ExecIndexRow Finding 1 (exit 0 unreachable for the gate without L1 baseline re-record) confirmed by my
  own full-run: rc=1 is unchanged from base, `unindexed` is the only check that moved red→green. The
  predicate line the seat spec named ("unindexed 0") is achieved; the exit code is dominated by the
  stale-frozen-baseline class. This matches the round's declared carried-red doctrine.

## Copies (evidence, byte-level, my seat dir)

- .ufo/waves/round-90/w1/ReviewerRepairs/live-guard-after.txt — my own full live bare run, 19/19 PASS.
- .ufo/waves/round-90/w1/ReviewerRepairs/index-no-row-world.json — my own no-row scratch world integrity
  reading (`unindexed 1`, row-named detail).
- .ufo/waves/round-90/w1/ReviewerRepairs/floors-base-vs-current.md — full diff text of the two files at
  base vs current (all 6 hunks).

No install, no pacman, no kernel/host change, no secret read, no scratch trail left
(fast/scratch/hyaku/kotoba-r90/ReviewerRepairs/ ≥ empty at yield; receipts above persisted first).
