Result: DONE — `verifiers/check_correction_sweep.py` gains four behavioural probes and one dropped-case guard; the frozen counter now kills 11 of 11 mutants with all 5 equivalents surviving (exit 0), delivered as an insertion-only patch.

# R3 repair — behavioural sweep self-test arms (C2 withdrawn; record only)

C2 was withdrawn before data (plan erratum 1): no claim rests on this work. It is defect work
measured by the frozen counter as a record, never as a claim.

## Deliverables

- Patch: `.ufo/waves/round-58/build/ExecC2Arms.patch`
  - sha256 `3fe7fc6eb72baaf682fbeda03cb3baf900a68db208fdc246ee32a668b3d0fecf`, 81 lines.
  - `git diff --stat`: `1 file changed, 51 insertions(+)` — zero deletions, zero reordered
    lines, so every frozen `old` text still occurs exactly once (the counter shows no `na` row).
  - Applies cleanly to the lane file: `git apply --check -p1` on a pristine copy of
    `verifiers/check_correction_sweep.py` → `APPLY_CHECK=ok`; applied result sha256
    `f54cff1791b67b87384e8479e7b6481ad706b41a29374f777d503d02f8d2d3c6`, identical to the
    patched sandbox file.
- Sandbox: `/fast/scratch/hyaku/kotoba-r58/ExecC2Arms` at
  `3de87aad29e960c95ed35840442f424c48c29729`; patched tree committed as
  sandbox `310ab2481bd18ad7541819cfb99ebf6906528eac`.
- Pre-image: lane working tree, lane `a39942c`, freeze `3de87aa` and base `f56f6e19` all hold
  the same `verifiers/check_correction_sweep.py` (sha256
  `799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18`), so the patch's context
  matches the lane.

## What the arms do (behaviour, not text)

Three changes, all insertions (three diff hunks); nothing existing was edited or reordered.

1. `ran: list[str] = []` in `self_test()` and `ran.append(name)` in the inner `case()`: every
   case records itself as it runs. (`check_correction_sweep.py:170,176` patched lines.)
2. Four red probes call `sweep(reader(None, tmpdir))` on fixtures that state the stale claim
   beside the weaker text a shortened `declared` pattern would accept:
   - `r58 s076 bare round red`: fixture `S076's project line holds no agent word; a Round-57 note follows.`
     must be reported for `r57-r2-s076-note`. True `declared` (`Round-57 correction`) does not
     match a bare `Round-57`; the shortened `Round-57` (M04) does, so the probe turns green and
     the case fails.
   - `r58 s078 bare round red`: same shape for `r57-r2-s078-note` (M05).
   - `r58 singular bare path red`: fixture
     `` | opencode | `.opencode/agents` (singular `agent/` still loads; see `migrate-v1.mdx`) | ``
     must be reported for `r57-r2-skill-singular-agent`. True `declared` (`migrate-v1\.mdx:486`)
     needs the line number; the shortened `migrate-v1\.mdx` (M06) matches, so the case fails.
   - `r58 singular wrong line red`: fixture with `migrate-v1.mdx:999` must be reported for the
     same row; only the exact `:486` satisfies the true `declared`, while M06's shortened
     pattern accepts any line number.
3. Dropped-case guard: `expected_cases` lists the 19 case names; at the end of `self_test()`
   `sorted(ran) != sorted(expected_cases)` appends a failure (and increments `n`). A dropped or
   renamed case fails the run while the remaining cases pass; a pure reorder keeps the same name
   set and survives (E4), as does an inserted comment (E5).

No hash, snapshot or grep of the file's own source, and no reference to the mutant catalogue
(control `CtlC2Snapshot` / `CtlC2SourceGrep` avoided). The arms encode the semantic rule the
round-57 rows exist to enforce.

Self-test assertion count: **18 before → 23 after** (4 new cases + 1 guard assertion).
`check_sweep_mutants.py --self-test` is unchanged at 20 assertions.

## Evidence

Sandbox `/fast/scratch/hyaku/kotoba-r58/ExecC2Arms`, 2026-10-23T08:12:25Z (`date -u`).

Before the patch (unpatched `3de87aa`, 2026-10-23T08:09:40Z):

```
$ timeout 300 python3 -B verifiers/check_correction_sweep.py --self-test
0 failure(s) over 18 assertions
EXIT=0

$ timeout 900 python3 -B verifiers/check_sweep_mutants.py --file verifiers/check_correction_sweep.py
M01 mutant killed exit=1
M02 mutant killed exit=1
M03 mutant killed exit=1
M04 mutant survived exit=0
M05 mutant survived exit=0
M06 mutant survived exit=0
M07 mutant killed exit=1
M08 mutant survived exit=0
M09 mutant survived exit=0
M10 mutant survived exit=0
M11 mutant survived exit=0
E1 equivalent survived exit=0
E2 equivalent survived exit=0
E3 equivalent survived exit=0
E4 equivalent survived exit=0
E5 equivalent survived exit=0
sweep mutants killed 4 of 11; equivalents survived 5 of 5
EXIT=1
```

After the patch:

```
$ timeout 300 python3 -B verifiers/check_correction_sweep.py --self-test
0 failure(s) over 23 assertions
EXIT=0

$ timeout 900 python3 -B verifiers/check_sweep_mutants.py --file verifiers/check_correction_sweep.py
M01 mutant killed exit=1
M02 mutant killed exit=1
M03 mutant killed exit=1
M04 mutant killed exit=1
M05 mutant killed exit=1
M06 mutant killed exit=1
M07 mutant killed exit=1
M08 mutant killed exit=1
M09 mutant killed exit=1
M10 mutant killed exit=1
M11 mutant killed exit=1
E1 equivalent survived exit=0
E2 equivalent survived exit=0
E3 equivalent survived exit=0
E4 equivalent survived exit=0
E5 equivalent survived exit=0
sweep mutants killed 11 of 11; equivalents survived 5 of 5
EXIT=0

$ timeout 900 python3 -B verifiers/check_sweep_mutants.py --self-test
table sha256 6ccb40faa2f85d5abe8682fd71b9c2cf42b727609906882c81cf92d3dbc0c30c
0 failure(s) over 20 assertions
EXIT=0

$ timeout 300 python3 -B verifiers/check_correction_sweep.py --rev 3de87aad29e960c95ed35840442f424c48c29729
correction sweep: 0 stale block(s)
EXIT=0
```

Per-mutant kill reason, observed by applying each row's `old`→`new` to the patched source and
running the mutated `--self-test` in a temp `git init` repo (same procedure as the counter's
`run_self_test`, stdout/stderr captured):

| mutant | exit | observed failure line(s) |
|---|---|---|
| M04 | 1 | `FAIL r58 s076 bare round red: got []` |
| M05 | 1 | `FAIL r58 s078 bare round red: got []` |
| M06 | 1 | `FAIL r58 singular bare path red: got []`; `FAIL r58 singular wrong line red: got []` |
| M08 | 1 | guard: `cases run [...]`, `expected [...]`; missing `r57 quote notes red` |
| M09 | 1 | guard; missing `r57 quote notes green` |
| M10 | 1 | guard; missing `r57 singular agent clause red` |
| M11 | 1 | guard; missing `r57 singular agent clause green` |

M01–M03 stay killed (their registry-row deletion now also fires the matching new probe), M07
stays killed (dropped `SEEDED` entry → `RuntimeError: missing
corpus/knowledge/agent-definition-files-round56.md`). The equivalents exit 0 with no failures.

## Risks

- `expected_cases` is a fixed name set: adding or renaming a case in a later round requires
  updating it. That is the guard's contract (a silent drop is what it exists to catch), but it
  is a maintenance coupling, stated in the in-file comment.
- The probes bind the semantic distinction the three round-57 rows rely on (a bare round label
  is not the declared correction; a path without its exact line number is not the declared
  citation). A future row that legitimately declares only `Round-57` or a bare path would trip
  them.
- The withdrawal reason still stands: a fixed, published equivalent set can be special-cased by
  a text-keyed self-test. These arms are behavioural and pass the frozen counter, but they do
  not give the counter a way to tell behavioural arms from a catalogue-keyed self-test — that
  is the `CriticC2Redesign` input, out of scope here. No claim is made.
- The patch touches no registry row, no `SEEDED` entry and no existing line; the `--rev` sweep
  at the freeze rev still reports 0 stale blocks.

## Blockers

None. No tool installs or upgrades; no model calls, no client CLI invocation; all runs
`timeout`-capped (≤ 900 s) inside the sandbox clone; no lane writes beyond this report and the
patch.
