# Plan — round 53 (hyaku campaign, attempt 1)

Base: branch `master` at `e78dff667237fba2e3cf9eccb802eff5bc9ea302` (round 52 admitted after the round-51
rejection; spot-check `corpus/lessons/round-52-verifier-spotcheck.md`). Shape: default, two v1 waves (build,
then falsify). The L1 holds the planner seat; no swarm planner item. Every before-value below was measured
by the L1 at round start, 2026-10-22T19:50–19:54Z, on the lane checkout at `e78dff66` (Q19). Both counters
are committed in this plan commit, before any content they score (Q28); their cases, tables and targets are
frozen here and never widened this round.

Axis scores at base (`SCORECARD.md` § axes @ `e78dff66`): depth 9, consistency 10, coverage 8.5,
operability 8.5, freshness 8, calibration 8.5, adjacency 8.0. Lowest non-retired: freshness and adjacency,
tied at 8. C1 works freshness.

Drift sentinel (orchestrator note; `SCORECARD.md` `Next: round 53`): rounds 50–52 each recorded more than
was verified, and rounds 51–52 worked sibling overlap and MCP instruction surfaces. C2 works a different
frontier area: executed checklist coverage of the always-on (AGENTS.md-class) constraint-file checklist,
which has no executed or delegated box (`corpus/README.md` § Frontier, first row). Each statement below is
the counter's printed line and nothing more (Q26).

## Claims (each statement is exactly what its counter prints)

**C1 — freshness (lowest non-retired axis, 8).**
Statement: `python3 -B verifiers/check_opencode_repin.py --rev <rev>` prints `surfaces pass 7 of 7
(opencode_extract PASS); pins OK 3/3; opencode classes kept 9 of 9; self-test 0 failure(s)` and exits 0,
measured on the host opencode 1.19.4 (sha256 `538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7`)
and omp 18.12.6 (sha256 `85d9daf3…`).
Before at `e78dff66` (2026-10-22T19:53Z): `opencode re-pin: surfaces pass 6 of 7 (opencode_extract FAIL);
pins OK 2/3; opencode classes kept 9 of 9; self-test 0 failure(s) over 129 assertions`, exit 1.
Counter: frozen here. It extracts the revision's `verifiers/` and `corpus/` with `git archive`, runs that
revision's `verify_surfaces.py --json` and `check_substrate_pins.py --json` against the installed binaries,
compares the revision's declared opencode classes with those at `e78dff66` (same `class_id`, `literal`,
`context_kind`, `verdict`; retiring or re-kinding a class to clear the gate is not kept), and runs the
revision's `verify_surfaces.py --self-test` (floor 129). The second output line names the measured opencode
binary; a later host rebuild is a different measurement.
What the counter does not measure: whether the re-derived OC-4/OC-6 rules match the loader code they name
rather than an unrelated string. That is reviewer and mutation-tester work in wave 2 and is not claimed.

**C2 — operability (advisory, 8.5; the sourced claim).**
Statement: `python3 -B verifiers/check_alwayson_boxes.py --rev <rev>` prints `always-on boxes executed and
discriminating 2 of 8` and exits 0.
Before at `e78dff66` (2026-10-22T19:54Z): `always-on boxes executed and discriminating 0 of 8`, exit 1
(`alwayson.04` and `alwayson.07` both `unexecuted`).
Counter: frozen here. A box counts only when the revision's box map delegates it to an instrument in the
revision and that instrument, run as `--check <box> --target <dir> --json`, returns the pinned status and
exit code on each of the 6 cases the counter pins for that box (alwayson.04: 2 PASS controls including a
version number, 4 dated/transient FAIL cases; alwayson.07: 4 PASS cases including the `@AGENTS.md` import
and the symlink redirect, 2 FAIL cases including a prose mention that is not an import).
Source basis: the redirect forms and the both-files behaviour come from Claude Code's current memory
documentation (`https://code.claude.com/docs/en/memory.md`, opened 2026-10-22 by the L1; a SOURCES row is
written after a wave-1 seat re-opens it, with the Gate quote). Other clients' AGENTS.md / CLAUDE.md
resolution (Codex, opencode, Gemini CLI, Copilot, Cursor, agents.md, omp) is opened in wave 1; any client
recorded as silent carries the Q30 three-part sweep or is recorded `not checked`.
What the counter does not measure: the instrument's behaviour on the live always-on population, and the 6
other boxes. A live run is reported as an observation, not as the claim.

Causal separability: C1 changes `verifiers/verify_surfaces.py`, `verifiers/baseline.json`, surfaces
fixtures, the census entry if a rule's anchor text changes, and the `surfaces` floor; its counter reads no C2
file. C2 adds an always-on instrument, its fixtures, map dispositions for `alwayson.04`/`alwayson.07`, the
SOURCES rows and a knowledge entry; its counter reads only `verifiers/`. Each verifies without the other.

No-harm guards (not part of either statement): `verify_skill_checklist.py --json` stays exit 0 with
`box_map_complete` PASS; `check_assertion_floors.py` exit 0 with no floor lowered; `check_sibling_census.py`,
`check_correction_sweep.py` and the frozen round-52 counters unchanged in exit code.

## Routed defects from the round-52 spot-check (repairs, not claims)

1. Re-derive and re-pin opencode 1.19.4 — this is C1.
2. Re-record the `verify_corpus_integrity` baseline: at base the gate reads 4 of 9 (DRIFT `tracked_files`
   76/72, `unindexed` 1 = the round-52 spot-check file, `report_total` 49/46, `report_dead` 5 = fleet report
   paths cited in closure-authored spot-check files, `commit_total` 31/30). Index the spot-check file; resolve
   or classify the 5 fleet-report pointers in the instrument with a self-test arm (closure files are never
   edited); re-record the baseline last, after every round file has landed.
3. Self-test arms for the two attempt-2 C1 fixes in `verify_surfaces.py` (unresolved-group admission; the
   empty-baseline fallback), each shown able to fail by reverting its fix.
4. The C2-counter class (`MutMcpCounter` M12 host-prefix pin, M16 quote-substring): a QUALITY criterion
   grounded in a round-53 lesson row, and `verifiers/check_mcp_instructions.py` tightened so both mutants are
   killed, with self-test arms; the round-52 declared results re-measured on the plan-commit counter to show
   the round-52 record is untouched.
5. Drift sentinel — handled by C2's choice of frontier (above) and by Q26 statements.
6. Q30 already landed in round 52 (`corpus/QUALITY.md:41`); this round applies it to every client negative.

## Frontier step

- SOURCES: rows for every always-on source opened this round (Claude Code memory docs first). Census before at
  `e78dff66`: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → exit 0
  (W04 S018, S019, S021; `kotoba ok`), 42 rows.
- Mistake to mine: the round-52 corpus-integrity baseline was not re-recorded after the round's own files
  landed (`commit_total` DRIFT new at head; routed defect 2), or a better-evidenced one a seat finds; the fix
  is shown able to fail.
- Sourced claim: C2.

## Waves

- Wave 1 build (v1, 32–40 seats): C1 re-derivation in a sandbox clone; routed-defect repairs in sandbox
  clones; the always-on instrument in a sandbox clone; source opening per client; live always-on population;
  counter attacks; sibling-overlap scan; critics on both claims.
- Wave 2 falsify (v1, 32–40 seats) only if wave 1 yields at least 32 distinct attack items; otherwise one
  residual call of at most 8 reviewer and critic seats.
