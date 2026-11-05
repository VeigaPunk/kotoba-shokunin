# ReviewerRepairs — r90-w1 seat report (floors bump + index row attack)

Full evidence: `.ufo/waves/round-90/w1/ReviewerRepairs/review.md` (plus live-guard-after.txt,
floors-base-vs-current.md, index-no-row-world.json in the same dir). Read-only seat; scratch
`/fast/scratch/hyaku/kotoba-r90/ReviewerRepairs` removed before this yield.

## Verdicts

1. **Floors half-bump completion — SOUND.** `git diff 6af71591e...f33 -- verifiers/floors-registry.json
   verifiers/check_assertion_floors.py` → 6 hunks exactly as the seat reported: docstring list + note,
   `EXPECTED_INSTRUMENTS["freeze_gate"] = 30`, `INSTRUMENTS["freeze_gate"]` row, F6 literal `18`→`19`
   (line 866) + comment paren. Row-for-row: AST read-back of both tables vs `floors-registry.json` shows
   zero mismatches, zero extra rows; the registry's only semantic change vs base is
   `instrument_total` 18→19 (structural JSON diff, one line). Guard live (my own run): 19/19 PASS,
   `PASS freeze_gate observed=30 floor=30`, rc=0.
   My own built worlds (never the seat's): unmodified-base clone reproduces BOTH `base-floors.txt` lines
   byte-identical at rc=2 (`FAIL registry size drift: instrument_total=18 but 19 entries...`;
   `FAIL registry row vanish: freeze_gate (listed in ..., absent from both guard tables)`);
   tables-reverted/full-bump half-bump shapes never read silent-green (rc=2 size drift in every variant).
2. **Index row — SOUND.** One line at `corpus/README.md:186`, sibling format matched (4-cell row,
   `lessons/...` token). My own runs: with-row `unindexed 0` (`unindexed_detail: []`), no-row scratch
   world (fresh shared clone, pristine README) `unindexed 1` naming the file — the 0↔1 flip is the sole
   cause. rc stays 1 in both, dominated by the same five DRIFT checks as base-integrity.json
   (verified identical DRIFT set).
3. **No new red** from either repair on battery commands 1–2: floors rc 2→0 with all PASS;
   integrity DRIFT set unchanged except `corpus.index.unindexed` DRIFT→PASS.

## Findings (for the L1)

- **Finding 1 (MEDIUM, pre-existing, not introduced by this round):** floors-guard child-cap drift —
  `verify_harness_independent.py --self-test` takes ~167 s standalone; `SELF_TEST_TIMEOUT_S = 120` scales
  only with load, so an idle-host bare guard walk false-reds rc=2 (`self-test timed out`), cap 129.8 s
  vs real 167 s. Confirms ExecFloorsBump Finding 1; noted, not rescued.
- **Finding 2 (INFO):** ExecIndexRow Finding 1 confirmed — the seat-spec "exit 0" for the integrity gate is
  unreachable without an L1 re-record of the frozen `corpus-baseline.json` equal-expectations; the named
  line (`unindexed 0`) is achieved, residual rc=1 is the declared stale-equal + carried
  `commit_unresolvable` classes.
- **Finding 3 (INFO, cross-seat observation for K1 context):** the r89 registry row `freeze_gate` was
  already carried in the registry at the base (covering shape) with `instrument_total` 18 countable only
  against 19 entries; the r89 half-bump red pins both size and vanish arms, and the r90 change is the
  minimal, one-commit-completing form.

## Bounds compliance
No git/jj write anywhere (read-only git and shared scratch clones only, toplevel asserted); no fleet-root
tracked file written; no pacman, no install, no kernel/sysctl change; no secret read. Writes: this file,
`.ufo/waves/round-90/w1/ReviewerRepairs/` records only.
