Result: DONE — the frozen C2 counter is delivered as `.ufo/waves/round-58/w0/check_sweep_mutants.py` (sha256 `f7664401…`), with the 16-row table embedded as a literal; in the sandbox its `--self-test` exits 0 over 20 assertions and `--rev f56f6e19…` prints `sweep mutants killed 4 of 11; equivalents survived 5 of 5`, exit 1, exactly the expected base result.

# Delivered artifact

| item | value |
|---|---|
| delivered file | `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-58/w0/check_sweep_mutants.py` |
| integrate as | `verifiers/check_sweep_mutants.py` (the lane keeps `verifiers/*.py` at mode 755; the delivered file is 755) |
| sha256 | `f7664401095948fd84889de1767e4fa6a32b7dc25cb50f49de2c981543d3241f` |
| bytes | 18599 |
| table sha256 (`json.dumps(TABLE, sort_keys=True)`) | `6ccb40faa2f85d5abe8682fd71b9c2cf42b727609906882c81cf92d3dbc0c30c` |
| frozen source `.ufo/waves/round-58/sweep-mutants.json` | sha256 `cf2fa97a7a385a00aab60e52a58211982e80c7194d6ddd3de751e2f144d6bfbf` (5534 B) |
| base blob `f56f6e19…:verifiers/check_correction_sweep.py` | 14831 B, sha256 `799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18` |

No tool was installed or upgraded; no channel was used. Nothing outside the two assigned files was written in the lane.

# What the counter does

- `TABLE` is a Python literal (16 rows, fields `id, kind, desc, old, new`) generated from the frozen JSON by `repr()` per value, so the strings are byte-exact. The counter never opens the tree for it; the freeze is enforced by comparing `hashlib.sha256(json.dumps(TABLE, sort_keys=True))` against the constant `TABLE_SHA256` inside `--self-test`.
- `--rev REV` reads `git -C <lane> show REV:verifiers/check_correction_sweep.py`, where `<lane> = Path(__file__).resolve().parent.parent`. `--file PATH` reads that file instead (controls).
- Per pristine copy and per applied row: a fresh `tempfile.TemporaryDirectory()` (honours `TMPDIR`), `git init -q` inside it with `GIT_DIR/GIT_WORK_TREE/GIT_INDEX_FILE` stripped from the child environment, the target written to `verifiers/check_correction_sweep.py`, then `[sys.executable, '-B', 'verifiers/check_correction_sweep.py', '--self-test']` with `cwd=<tmp>` and a 120 s cap; output is captured, never echoed.
- Applicability: `source.count(old) == 1`, replacement made once. Mutant → `killed` iff exit ≠ 0 (a timeout counts as killed and prints `exit=timeout`). Equivalent → `survived` iff exit 0. A non-applying row prints `not-applicable` with `exit=na` and counts against its predicate.
- Pristine ≠ 0 prints `could-not-evaluate: pristine self-test exit N` to stderr and exits 2, as do an unknown rev, a failing git (`git show`/`git init`), an unreadable `--file`, and an unusable scratch copy (OSError is mapped to exit 2 rather than a traceback).
- Output: `<id> <kind> killed|survived|not-applicable exit=<n>` per row, then exactly `sweep mutants killed K of 11; equivalents survived E of 5`; exit 0 iff K == 11 and E == 5.

# Evidence (pasted runs; sandbox clone `/fast/scratch/hyaku/kotoba-r58/ExecC2Counter`, `git rev-parse HEAD` = `f56f6e191762c27c1aa2af11a204db9e2ca4edec`)

## 1. Sandbox `--self-test` (final bytes)

```
$ date -u
Fri 23 Oct 2026 07:44:26 AM UTC
$ sha256sum verifiers/check_sweep_mutants.py
f7664401095948fd84889de1767e4fa6a32b7dc25cb50f49de2c981543d3241f  verifiers/check_sweep_mutants.py
$ timeout 900 python3 -B verifiers/check_sweep_mutants.py --self-test
table sha256 6ccb40faa2f85d5abe8682fd71b9c2cf42b727609906882c81cf92d3dbc0c30c
0 failure(s) over 20 assertions
EXIT=0
```

The 20 assertions are: table sha (1), table shape 16 rows / 11 mutants / 5 equivalents (1), one `old`-occurs-exactly-once assertion per row against the base blob (16), and the two synthetic exit-code mappings (2).

## 2. Sandbox `--rev` at base (final bytes)

```
$ date -u
Fri 23 Oct 2026 07:44:26 AM UTC
$ timeout 900 python3 -B verifiers/check_sweep_mutants.py --rev f56f6e191762c27c1aa2af11a204db9e2ca4edec
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

This is the expected base result. The seven survivors on base are M04, M05, M06 (weakened `declared` literals) and M08–M11 (deleted self-test cases). The reason for the declared-literal survivors is visible in the target itself: `grep -n "Round-57\|migrate-v1" verifiers/check_correction_sweep.py` returns only lines 75, 77 (the declared literals), 228 (`Round-57 correction (R2)`) and 233 (`migrate-v1.mdx:486`) — every fixture occurrence is already the full correction form, so no fixture tells `Round-57` from `Round-57 correction` or `migrate-v1\.mdx` from `migrate-v1\.mdx:486`. The deleted-case survivors follow directly: a deleted `case(...)` removes the only assertion over that row.

## 3. Delivered copy run from its staged path (cwd `/tmp`, lane read-only)

```
$ date -u
Fri 23 Oct 2026 07:44:54 AM UTC
$ D=/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-58/w0/check_sweep_mutants.py
$ timeout 900 python3 -B "$D" --self-test
table sha256 6ccb40faa2f85d5abe8682fd71b9c2cf42b727609906882c81cf92d3dbc0c30c
0 failure(s) over 20 assertions
EXIT=0
$ timeout 900 python3 -B "$D" --rev f56f6e191762c27c1aa2af11a204db9e2ca4edec | tail -2
E5 equivalent survived exit=0
sweep mutants killed 4 of 11; equivalents survived 5 of 5
EXIT=1
```

`cp` + `cmp` confirmed the delivered bytes are identical to the tested sandbox bytes (`IDENTICAL`).

## 4. Controls (`--file`)

Synthetic full-kill fixture written in memory by the counter's own self-test (`synthetic_full_kill()`), exercised through the real CLI:

```
$ timeout 900 python3 -B verifiers/check_sweep_mutants.py --file scratch/full_kill.py
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
```

Same fixture with E5's `old` comment replaced by an inert comment (self-test still green, row no longer applies):

```
$ timeout 900 python3 -B verifiers/check_sweep_mutants.py --file scratch/na_control.py
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
E5 equivalent not-applicable exit=na
sweep mutants killed 11 of 11; equivalents survived 4 of 5
EXIT=1
```

The fixture carries all 16 `old` texts byte-exactly and probes them semantically: registry ids as a multiset (E1's row swap survives), `declared` patterns by behaviour on a "records the correction" text and a weaker "names the round" text (E2 `[.]`, E3 `[ ]` survive; M04/M05/M06 start matching the weak text and die), `SEEDED` membership (M07 dies), case blocks parsed by name and wanted ids (E4's swap survives, M08–M11 die), and a comment line that carries no meaning (E5 survives). `--self-test` asserts this file maps to exit 0 and that a second fixture whose self-test always fails maps to exit 2.

## 5. Failure paths

```
$ timeout 300 python3 -B verifiers/check_sweep_mutants.py --rev 0000000000000000000000000000000000000000
could-not-evaluate: git show 0000000000000000000000000000000000000000:verifiers/check_correction_sweep.py failed in /fast/scratch/hyaku/kotoba-r58/ExecC2Counter (exit 128): fatal: path 'verifiers/check_correction_sweep.py' exists on disk, but not in '0000000000000000000000000000000000000000'
EXIT=2

$ timeout 300 python3 -B verifiers/check_sweep_mutants.py --file /fast/scratch/hyaku/kotoba-r58/ExecC2Counter/nope.py
could-not-evaluate: cannot read /fast/scratch/hyaku/kotoba-r58/ExecC2Counter/nope.py: [Errno 2] No such file or directory: '/fast/scratch/hyaku/kotoba-r58/ExecC2Counter/nope.py'
EXIT=2
```

Control `scratch/no_s076.py` = base bytes with the S076 registry row deleted:
`could-not-evaluate: pristine self-test exit 1`, `EXIT=2` — i.e. any control that removes a live row breaks the pristine run before any row is judged, which is why the not-applicable control in §4 uses a behaviour-free comment.

## 6. `TMPDIR` is honoured

The 17 evaluations (pristine + 16 rows) each build their scratch copy under `TMPDIR`:

```
$ TMPDIR=/fast/scratch/hyaku/kotoba-r58/ExecC2Counter/scratch/tmpok timeout 900 python3 -B verifiers/check_sweep_mutants.py --file scratch/full_kill.py
sweep mutants killed 11 of 11; equivalents survived 5 of 5   (EXIT=0)
[sampling os.listdir(TMPDIR) every 5 ms during the run]
max concurrent temp entries in TMPDIR: 1 | distinct names: 17
leftovers now: []
```

A read-only `TMPDIR` was observed to be skipped, not fatal (`tempfile.gettempdir()` falls back to the next candidate), so that run still exited 0; an unusable scratch copy in general is mapped to `could-not-evaluate` and exit 2 by the `OSError` guard in `run_self_test`.

# Notes

- Sandbox: `/fast/scratch/hyaku/kotoba-r58/ExecC2Counter`, cloned from the lane and checked out at `f56f6e191762c27c1aa2af11a204db9e2ca4edec`; every execution happened there (or, for §3, on the delivered copy with `cwd=/tmp`). The lane was touched read-only (`git --no-optional-locks show/status`), and jj was not invoked at all.
- Lane `git --no-optional-locks status --porcelain -- .ufo/waves/round-58 verifiers` shows only `?? .ufo/waves/round-58/sweep-mutants.json`, `?? .ufo/waves/round-58/w0-call.json`, `?? .ufo/waves/round-58/w0/` — nothing under `verifiers/`.
- `LANE` is `Path(__file__).resolve().parent.parent`. Staged at `.ufo/waves/round-58/w0/` the counter therefore resolves `LANE` to `.ufo/waves/round-58`, which still reads the correct repository because `git -C <subdir>` walks up; after integration at `verifiers/check_sweep_mutants.py` it resolves to the lane root, as specified. §3 exercises the staged path end to end.

# Risks

- The base measurement is 4 of 11 killed, 5 of 5 equivalents surviving. The counter is a measuring instrument only; it does not change the target, and the round's claim must be built on this measured number (7 mutants survive base).
- `not-applicable` is reported as `exit=na` and `timeout` as `exit=timeout`; both are outside the numeric `<n>` form. Neither occurred in any run against the frozen table and base revision; both are documented in the module docstring so a reader is not surprised.
- The table sha is frozen by an embedded constant. Editing `.ufo/waves/round-58/sweep-mutants.json` without regenerating that constant makes `--self-test` fail by design — that is the freeze, not a defect.
- Environment recorded: Python 3.14.8, git 2.56.0, Linux; no dependency beyond the standard library.

# Blockers

None.
