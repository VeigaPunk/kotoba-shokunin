# DispatchInstrument — C2 operability: dispatch-prompt box execution (kotoba round 49)

Seat: `KotobaR49.DispatchInstrument`. Lane base `a5adc146a2995dcc5a95a6d8db6e5674f75191ac`.
Private clone: `/fast/scratch/hyaku/kotoba-r49/seats/DispatchInstrument/clone` (read-only to the lane;
no lane file was edited except this report). Deliverables: `c2.patch`
(sha256 `634a9b8c50533bca1771d8f4f0d7e4ad69a2b778fbf893a2aaaade67319b7b78`), `live.json`
(sha256 `f183a0bc02fc881414450183a8c1faaa1bf4e5ed84ab25978204bb636162b51e`).

## Findings first

1. **C2's two boxes are now executed, not attested.** `verifiers/verify_dispatch_prompts.py`
   (new, 620 lines, stdlib only) runs `dispatch.04` and `dispatch.08` over a prompts
   directory. Both map entries moved from `unexecuted:` to
   `delegated:verifiers/verify_dispatch_prompts.py`; the live map reads **8 executed /
   2 delegated / 31 unexecuted** (was 8 / 0 / 33).
2. **The plan's jq counter is content-blind and the critic's objection stands.** I did not
   rely on it. `--box-proof` proves the claim instead: it reads the map, requires both boxes
   to be `delegated:verifiers/verify_dispatch_prompts.py` **and** their `text_sha256` to
   equal a constant pinned in the instrument **and** the live `SKILL.md` box to hash to that
   same constant, then runs the committed fixture corpus and requires every control to
   pass and every mutant to fail on its named conjunct. It prints exactly `boxes proven N`
   and exits 0 only at N == 2.
3. **dispatch.08's state clause needed the L1's authority amendment, and I applied it.**
   `.ufo/state/<id>.round` is frozen since 2026-10-15 (mtimes 2026-10-15T01:45:42 /
   01:50:57, 21 files); the hyaku driver writes `<id>.report-baseline`, whose first
   whitespace field is the lane's latest dispatched round. The `SKILL.md` dispatch.08 box
   text now reads that authority, keeping the other words of the box; its `text_sha256`
   changed `c1e80da8…` -> `f5c37baa…` and was re-pinned in both the map and the
   instrument's `PINNED_BOX_SHA`. **The instrument's own box extractor was cross-checked
   against `verify_skill_checklist.extract_boxes`**: all nine dispatch box hashes agree,
   so the re-pin cannot be a normalisation drift.
4. **Live findings (not hidden).** `dispatch.04` **FAILs on 6 real prompt defects**;
   `dispatch.08` PASSes. Details in §Live results.
5. **The floors guard now runs 10 instruments, all PASS** at exact floors; the new row
   `dispatch_prompts` has floor 32 = the instrument's observed self-test count.

## The instrument

`verifiers/verify_dispatch_prompts.py`, exit 0 pass / 1 check failure / 2 usage-substrate,
`--json`, `--self-test`, `--box-proof`; options `--prompts` (default
`/home/vgpnk/Projects/shokunin/.ufo/prompts`), `--state-dir` (default `…/.ufo/state`),
`--fleet` (default `/home/vgpnk/Projects/shokunin`), `--check` (repeatable).

**Scope.** Non-recursive scan of the prompts root; `closure/` is a subdirectory and is
never descended. A prompt file's lane id is the stem prefix of `<lane>-round-<N>.md` /
`<lane>-L1.md`; any other name is out of scope with a reason. `*-round-1-continuation-*.md`
and `*-L1.md` are out of scope for dispatch.08 with a reason (the box's round token is
read from the file name).

**dispatch.04** conjuncts: `report_path_literal` (only the *report path* is scanned — an
L0 `<lane> | round-<N>` template or a command template elsewhere in the body does not
trip it), `report_stem_is_lane_id` (report file stem == lane id), `lane_identity_known`
(the lane id names a lane this fleet knows: a `<fleet>/<id>-shokunin` repository or a
`<state-dir>/<id>.round` / `.report-baseline` state file — the lane id is never taken on
the prompt's own word). A non-lane role (the aggregator and the protocol lane, which own
no per-lane repository) is **listed out of scope with that reason**, not silently excepted;
its report artefact is fleet-level, so the stem conjunct does not apply to it.

**dispatch.08** conjuncts: `filename_role_round_equal`, `filename_report_dir_round_equal`,
`round_le_latest_dispatched` (N <= the lane's latest dispatched round = first field of
`<state-dir>/<lane>.report-baseline`). A lane with only the legacy `<lane>.round` is
reported **`state-stale`, not compared**; a lane with neither is **N/A**. A missing state
source is never a pass. Role-line forms are derived from the population, not assumed:
`You are the <lane> L1, round <N>.` / `round <N> of up to <M>.` / `<lane>-shokunin L1,
round <N> of up to <M>.` / `shokunin <lane> L1 (model …), round <N> of up to <M>.`; the
round token is the first `round <digits>` on line 1, so the `of up to 1024` cap is never
captured.

**Verdict rule.** Per conjunct PASS/FAIL/N-A; a file FAILs if any conjunct FAILs, else
N/A if any is N/A, else PASS. A check FAILs if any file FAILs, else N/A if no file PASSes,
else PASS. Every check prints `evaluated N`; `N == 0` is never a PASS (self-tested).

## Live results (fleet prompts, `live.json`)

Command: `python3 -B verifiers/verify_dispatch_prompts.py --json` (clone), exit **1**.

| check | status | evaluated | PASS | FAIL | N/A | out of scope |
|---|---|---|---|---|---|---|
| dispatch.04 | FAIL | 287 | 259 | 6 | 22 | 28 |
| dispatch.08 | PASS | 279 | 250 | 0 | 29 | 13 |

**dispatch.04 failures — 6 real defects, all `<lane>` placeholders in the report path of
an L1 prompt** (the class the box names: "a `<lane>` placeholder cost two lanes their
canonical round-1 report names"):

- `kake-L1.md` — `.ufo/reports/round-1/<lane>.md`; `report_path_literal` FAIL +
  `report_stem_is_lane_id` FAIL (stem `<lane>` != `kake`).
- `kasegi-L1.md` — same shape, lane `kasegi`.
- `kengaku-L1.md` — same shape, lane `kengaku`.
- `kotoba-L1.md` — same shape, lane `kotoba`.
- `kumitate-L1.md` — same shape, lane `kumitate`.
- `protocol-L1.md` — `.ufo/reports/round-1/<lane>.md`; `report_path_literal` FAIL. Its
  stem conjunct is N/A: the protocol lane owns no `protocol-shokunin` repository, so it is
  a fleet-root role and its report artefact is fleet-level (out of scope with that reason,
  listed in `out_of_scope`).

Sweep that produced the "6 FAIL / 22 N/A" split: 287 files evaluated = 279
`<lane>-round-<N>.md` + 8 `<lane>-L1.md`; the 22 N/A are the 21 fleet-root-role files
(aggregator 9 + protocol 12 round files, plus `protocol-L1.md`) whose stem conjunct does
not apply; 28 out of scope = 4 `*-continuation-kaika.md` + `.gitkeep` + 23 files whose
stem conjunct does not apply. `grep -cE '^[a-z0-9-]+-round-[0-9]+\.md$'` over the prompts
root = 279, `grep -cE '^[a-z0-9-]+-L1\.md$'` = 8.

**dispatch.08: 0 FAIL.** 250 PASS; 29 N/A are the `state-stale` lanes (only the legacy
`<id>.round`, frozen since 2026-10-15, not compared) — 20 audio/game-dev-2d/game-dev-3d/
lore-family files plus the 9 aggregator files. 13 out of scope = 4 continuation files +
`.gitkeep` + 8 `<lane>-L1.md` spawn files.

**The dispatch.08 identity conjuncts hold across the whole population**: 0 role-line round
mismatches and 0 report-dir round mismatches (measured by the instrument itself, and
independently by my own probe before the instrument existed). The state clause, measured
against the *amended* authority (`.report-baseline`), is satisfied by every file that has
a baseline; the 29 N/A are the state-stale lanes, and no file is a false pass.

**Live failures are findings, not instrument bugs** — the L1's instruction. They are
reported, not suppressed. `kotoba-round-49.md` is a PASS under the amended authority
(`kotoba.report-baseline` = 49, file round 49); under the frozen legacy `.round` (16) it
would have been a false FAIL, which is why the box text was amended rather than the
check weakened.

## Box proof (the content-tested after-value)

`python3 -B verifiers/verify_dispatch_prompts.py --box-proof` -> `boxes proven 2`, exit **0**.

Committed fixture corpus `verifiers/fixtures/dispatch-prompts/` (26 files + `manifest.json`):
one must-pass control and one must-fail mutant per conjunct of each box —
`report_path_literal`, `report_stem_is_lane_id`, `lane_identity_known`,
`filename_role_round_equal`, `filename_report_dir_round_equal`,
`round_le_latest_dispatched` (above state), and the missing-state case (N/A, never a
pass). The `d04-control` fixture body carries an L0 `<lane> | round-<N>` template and must
still PASS — the control arm that the whole-file-placeholder reading would fail.

**Both must-fail demonstrations, run and observed:**

1. Remap `dispatch.04` to `delegated:verifiers/verify_harness_independent.py` in the map
   -> `boxes proven 1`, exit 1, stderr names
   `dispatch.04: map disposition is 'delegated:verifiers/verify_harness_independent.py',
   not 'delegated:verifiers/verify_dispatch_prompts.py'`. (This is the critic's exact
   attack: an unrelated instrument, a real box-map PASS, and the content-blind counter
   would still read 2.)
2. Edit the `d04-placeholder` mutant fixture into a passing file (report path
   `/round-7/<lane>.md` -> `/round-7/kote.md`) -> `boxes proven 1`, exit 1, stderr names
   `dispatch.04/d04-placeholder: kote-round-7.md verdict 'PASS', expected 'FAIL'`.

Both were reverted; the tree re-verified at `boxes proven 2`.

## Other edits (in the clone, in the patch)

- `verifiers/checklist-baseline.json` — `dispatch.04` and `dispatch.08` dispositions ->
  `delegated:verifiers/verify_dispatch_prompts.py`; `dispatch.08` `text_sha256` re-pinned to
  the re-worded box.
- `SKILL.md` — the dispatch.08 box text re-worded to the `.report-baseline` authority
  (body only; **frontmatter untouched**); the live-count prose updated to
  "8 executed, 2 delegated, 31 unexecuted" and names the delegating instrument.
- `corpus/README.md` — the Known-gaps bullet updated to "31 of the 41" and the same
  live counts.
- `verifiers/floors-registry.json` — new row `dispatch_prompts` (floor 32, path
  `verifiers/verify_dispatch_prompts.py`); `instrument_total` 9 -> 10.
- `verifiers/check_assertion_floors.py` — **BUMP-IN-STEP**: the new row added to BOTH
  in-file tables (`EXPECTED_INSTRUMENTS` and `INSTRUMENTS`), the guard docstring's floor
  vector updated, and the F6 fixture's live-total literal moved 9 -> 10 in-step (it is
  anchored to the live registry's declared total, so a half-edit would have named a
  stale count).

## Verification (all in the clone; commands and exit codes)

| command | exit | result |
|---|---|---|
| `python3 -B verifiers/verify_dispatch_prompts.py --self-test` | 0 | `0 failure(s) over 32 assertions` |
| `python3 -B verifiers/verify_dispatch_prompts.py --box-proof` | 0 | `boxes proven 2` |
| `python3 -B verifiers/verify_dispatch_prompts.py --json` (live fleet prompts) | 1 | dispatch.04 FAIL / dispatch.08 PASS (`live.json`) |
| `python3 -B verifiers/verify_skill_checklist.py --json` (clone) | 1 | `checklist.box_map_complete` **PASS** — `41 boxes mapped (8 executed, 2 delegated, 31 unexecuted)`; 3 other FAILs, all pre-existing clone-location artifacts (see below) |
| `python3 -B verifiers/verify_skill_checklist.py --self-test` | 0 | `0 failure(s) over 1845 assertions` |
| `python3 -B verifiers/check_assertion_floors.py` | 0 | 10/10 PASS: `10/150/91/99/1845/62/116/330/150/32`; 33.5 s wall (not slow under load) |
| `python3 -B verifiers/check_assertion_floors.py --self-test` | 0 | `0 failure(s) over 150 assertions` |
| `python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json` (clone) | 1 | observed block **byte-identical** to the base clone's (the pre-existing unindexed `corpus/lessons/round-48-verifier-spotcheck.md` and 2 dead report pointers are base state, unchanged by this patch) |

**The 3 clone-only checklist FAILs are artifacts of the clone's location, not of this
patch.** Verified by running the same verifier on an unmodified clone of the base commit
(`clone-base`): it reports the same three FAILs — `trigger.name_directory` (name
`kotoba-shokunin` != directory `clone-base`) and two `../.ufo/reports/…` citation
resolutions that escape the clone tree. In the real lane checkout the same command exits
**0** with 11 PASS / 0 FAIL, `checklist.box_map_complete` PASS included.

## What is NOT done

- **No `SCORECARD.md` capabilities-table row.** The plan's C2 text mentions entering the
  SCORECARD capabilities table with the output; the L1's scoping messages did not include
  it, and the time bound hit before it. The row's evidence is this report: the command,
  the exit codes and `live.json`. The L1 owns that edit.
- **No `LOG.md` entry and no `corpus/knowledge/` or `corpus/lessons/` entry.** The L1's
  scope additions named only SKILL.md, corpus/README.md, the map, the registry and the
  guard; I did not widen into the corpus admission path (Q12/Q13 recheck machinery) I was
  not asked to build.
- **`corpus/README.md`'s coverage-map table is untouched** — only the Known-gaps bullet's
  prose changed, so `corpus.index.*` counts are unaffected (verified: the corpus
  instrument's observed block is identical to the base clone's).
- **The plan's jq counter was not adopted as the after-value.** It reads 2 (both boxes
  delegated) but it cannot distinguish the remap and stub attacks; `--box-proof` is the
  content-tested after-value and it is the one that prints 2.
- **Not verified in the real lane checkout**: the instrument, the fixtures and the map
  edit exist only in the clone. The lane checkout is read-only for this seat, and the
  L1 integrates the patch.
- The live run reads a **moving population** (the fleet dispatches during the round). The
  counts above are the 2026-10-22T11:1xZ snapshot; re-running the command reproduces the
  method, not necessarily the exact numbers.
