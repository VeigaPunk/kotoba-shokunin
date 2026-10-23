Result: HOLDS — `check_sweep_mutants.py` at `3de87aad29e960c95ed35840442f424c48c29729` matches plan § C2 and the frozen JSON on every scored element; two cosmetic nits, no defect.

# Scope

Review of `verifiers/check_sweep_mutants.py` at `3de87aad29e960c95ed35840442f424c48c29729`
against `plans/round-58.md` § C2 (lines 75–84) and `.ufo/waves/round-58/sweep-mutants.json`.
Sandbox: `/fast/scratch/hyaku/kotoba-r58/ReviewC2Counter` (clone of the lane, checkout
`3de87aad`; read-only against the lane). Lane working-copy bytes verified identical to the
freeze-commit bytes for both files under review:

```
$ git --no-optional-locks show 3de87aad...:verifiers/check_sweep_mutants.py | sha256sum
f7664401095948fd84889de1767e4fa6a32b7dc25cb50f49de2c981543d3241f
$ sha256sum verifiers/check_sweep_mutants.py          # same
$ git --no-optional-locks show 3de87aad...:.ufo/waves/round-58/sweep-mutants.json | sha256sum
cf2fa97a7a385a00aab60e52a58211982e80c7194d6ddd3de751e2f144d6bfbf
$ sha256sum .ufo/waves/round-58/sweep-mutants.json    # same
```

# Element checklist (plan § C2 → counter)

| Spec element | Plan line | Counter | Verdict |
|---|---|---|---|
| Embedded table equals JSON | — | `TABLE` literal `check_sweep_mutants.py:47-112`; sha constant `:43`; re-check `:320-324` | HOLDS — see sha block below |
| Applies-exactly-once rule | plan:80-81 "old text occurs exactly once" | `:266` `source.count(old) != 1` → `not-applicable`; `:269` `replace(old, new, 1)` | HOLDS |
| Kill/survive mapping | plan:80-81 | `:270-273` mutant killed iff exit≠"0"; equivalent survived iff exit=="0" | HOLDS (timeout counts as killed — docstring `:17-18`; wording nit F2) |
| Not-applicable counted against | plan:82 predicate over all 11/5 | `:267` verdict `na`; denominators `:280,:282` count TABLE rows, so `na` rows fail the `:399` predicate | HOLDS |
| Pristine precondition | plan:81 "pristine self-test must exit 0 (else exit 2)" | `:260-262` raises `CouldNotEvaluate` → `:391-393` exit 2 | HOLDS |
| Temp repo env hygiene | plan:79 "in a temp git repo" | `:238-255` TemporaryDirectory + `git init -q` (`:242`); `child_env` drops GIT_DIR/GIT_WORK_TREE/GIT_INDEX_FILE (`:207-210`); `sys.executable -B`, `cwd=t`, `timeout=120` (`:248-250`) | HOLDS |
| Print format | plan:82 | `:397-398` `sweep mutants killed %d of %d; equivalents survived %d of %d` | HOLDS |
| Predicate | plan:82 "exit 0 iff K = 11 and E = 5" | `:399` `0 if killed == mutants and survived == equivalents` (denominators are the TABLE counts) | HOLDS |
| Expected base | plan:83 "K = 4, E = 5, exit 1" | observed run below: `killed 4 of 11; equivalents survived 5 of 5`, exit 1 | HOLDS |
| 16 rows = 11 mutants + 5 equivalents | plan:78-79 | `:329-330` shape assertion in `--self-test`; ids M01–M11, E1–E5 in both orderings | HOLDS |

# Table equality (both shas computed)

```
embedded TABLE sha256 : 6ccb40faa2f85d5abe8682fd71b9c2cf42b727609906882c81cf92d3dbc0c30c
sweep-mutants.json sha: 6ccb40faa2f85d5abe8682fd71b9c2cf42b727609906882c81cf92d3dbc0c30c
TABLE_SHA256 literal  : 6ccb40faa2f85d5abe8682fd71b9c2cf42b727609906882c81cf92d3dbc0c30c
emb==literal: True | doc==literal: True
row order emb/doc identical: M01..M11, E1..E5
keys identical: desc, id, kind, new, old
structures equal: True
```

Canonical form is `json.dumps(TABLE, sort_keys=True)` (declared `:46`, computed `:320`),
not the file bytes — whitespace-insensitive, appropriate since the JSON is pretty-printed.

# Required runs (pasted; sandbox clone at 3de87aad)

```
$ timeout 600 python3 -B verifiers/check_sweep_mutants.py --self-test
table sha256 6ccb40faa2f85d5abe8682fd71b9c2cf42b727609906882c81cf92d3dbc0c30c
0 failure(s) over 20 assertions
EXIT=0
```

```
$ timeout 600 python3 -B verifiers/check_sweep_mutants.py --rev f56f6e191762c27c1aa2af11a204db9e2ca4edec
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

Base run reproduces the plan's expected `K = 4, E = 5, exit 1` (plan:83; matches the
assignment's record). Wall time ~2.1 s — well inside the 120 s/child cap.

# Findings

**F1 (LOW, cosmetic).** `check_sweep_mutants.py:4-5` docstring: "frozen by round-58 W0
(plan draft 8db20702, `plans/round-58.md` section C1)". The mutant sweep is specified in
**section C2** (`plans/round-58.md:75-84`); C1 is the command-files claim. Wrong section
name in a comment only — no behaviour, no predicate impact.

**F2 (LOW, wording divergence).** Mutant-kill mapping counts a self-test **timeout** as
killed (`:251-252` returns `"timeout"`; `:271` `code != "0"` → killed; docstring `:17-18`
declares this). Plan § C2 (plan:80-81) says killed iff "exits non-zero". A hanging mutant
therefore scores as killed, not could-not-evaluate. Direction is safe (a >120 s hang is a
defect signal), and the equivalents' side is strict (`code == "0"` only). Disclosed in the
counter's own docstring, so not a hidden rule change — noted for the record since the plan
sentence is the frozen wording.

**F3 (cosmetic).** `self_test()` counts `n += 1` once when `git show BASE_REV` fails
(`:339-340`) but would have run 16 row checks — assertion tally under-reports on that
failure path. Never triggered at base (observed: `0 failure(s) over 20 assertions` =
1 sha + 1 shape + 16 occurrence + 2 fixture checks).

# Residual risk / gaps

- `child_env` (`:207-210`) drops exactly the three git pointers the docstring names; other
  `GIT_*` vars (e.g. `GIT_OBJECT_DIRECTORY`, `GIT_CEILING_DIRECTORIES`) pass through. Spec
  names only the three; exotic environments could still steer the child's `git init`.
- The counter is source-blind by design: `git show rev:TARGET` then text `count`/`replace`
  on bytes. A self-test keyed on the published mutant `old` texts (the CtlC2SourceGrep
  shortcut, plan erratum 1) passes it — that is why C2 is withdrawn; it is a property of
  the fixed published table, not a defect in this file. This file faithfully executes the
  frozen contract.
- `CouldNotEvaluate` exit-2 path verified only via the `always_fail` fixture inside
  `--self-test` (`:362-371`); no live `--rev` exit-2 run performed (not required by the item).

# No findings on

Row-order, key sets, mutant-vs-equivalent per-row verdicts, `na` handling, exit-2 plumbing
(`:216-222,:244-246,:253-254,:229-231`), argparse shape (`:380-385`, mutually exclusive
`--rev`/`--file`/`--self-test`), and the `--file` control hook (`:383,:389`) — all conform.
