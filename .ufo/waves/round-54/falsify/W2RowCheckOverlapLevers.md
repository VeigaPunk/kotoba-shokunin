Result: HOLDS — every cell of the `check_overlap_levers.py` registry row is accurate as landed at bf65974c (row text byte-identical at tip 58db81c); two minor findings and one residual risk, none of which falsifies a cell, so no corrected row text is proposed.

Seat: KotobaR54.W2RowCheckOverlapLevers · 2026-10-22 · sandbox clone `/fast/scratch/hyaku/kotoba-r54/W2RowCheckOverlapLevers` at 58db81c4465b0e9b07ef2485b87d8970683afac6. Installs: none (nothing needed). No lane file written; git writes only inside the sandbox clone.

## The row under attack

`bf65974c:SKILL.md:451`, unchanged at tip `SKILL.md:465` (line moved because C1 content grew the file above it; cell text identical, verified by `git show <rev>:SKILL.md | grep -F`):

```
| `verifiers/check_overlap_levers.py` | gate | `python3 -B verifiers/check_overlap_levers.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | self-test temp repo (removed); `--fetch` reads the network | kotoba |
```

Source line numbers below are `verifiers/check_overlap_levers.py` at 58db81c (1,358 lines).

## Per-cell verdicts

| Cell | Verdict | Evidence |
|---|---|---|
| Name `verifiers/check_overlap_levers.py` | HOLDS | Blob exists at tip; frozen counter lists it `OK` (see counter run below). |
| Kind `gate` | HOLDS | PROTOCOL.md:390-392: a gate "reads surfaces, compares them against expected values persisted in its own repo, and returns a verdict". This script reads four surfaces via `git show` (526-531, 579-582), compares against expectations persisted in-file (89-201), returns 0/1/2 (598, 617). It can fail: measured exit 1 (below) and 19+ self-test mutants each asserted to lower the count (732-955). Not a probe. |
| Entry command | HOLDS | Measured: `python3 -B verifiers/check_overlap_levers.py --rev 58db81c…` → 7 `BACKED …` lines, last line `overlap levers backed 7 of 7 clients`, **exit 0**. |
| Verdict map `0=clean, 1=failed, 2=could-not-evaluate` | HOLDS | All three codes produced with the declared meaning (runs below). Ladder matches the script's own docstring (60-62) and code: `rc = 0 if k == len(CLIENTS) else 1` (598), fetch downgrade to 1 (616), IO error → 2 (583-585), root error → 2 (568-570), argparse usage error → 2. No fourth code produced in any exercised path. Finding F1 qualifies the *cause→code* mapping, not the map itself. |
| Self-test `--self-test` | HOLDS | Flag is real: argparse (548), dispatch `return self_test()` (556-558). Measured: `python3 -B verifiers/check_overlap_levers.py --self-test` → **exit 0**, stdout exactly 2 lines: `0 failures`, `51 assertions`. This is genuinely the script's own suite: it calls `evaluate()`/`main()` in-process on in-memory fixtures; no nested invocation of the entry command (the only subprocess calls are `git` inside the m18 arm, 1148-1196) and no usage text. PROTOCOL.md:398-402 satisfied: it asserts exit codes (m18: `rc1 == 1 and rc2 == 0`, 1190-1195), stable expected outcomes for control world + 19+ mutants (956-1350), and re-pins its own literals (982-1040). |
| Pinned values `in-file` | HOLDS | The script reads no pinned-value file: grep for `open(|.json|read_text|mkdtemp` shows only the graded surfaces (579-582) and the network read (496). All expected values are literals in the file: `CLIENTS` (89), `MAX_QUOTE_WORDS` (121), vocab/tier (123-127), `CLIENT_URL_PREFIXES` (132), `REVIEWED_LEVERS` (162), entry/lesson paths (99, 101). The four graded files are surfaces, not pins. |
| Write scope `self-test temp repo (removed); --fetch reads the network` | HOLDS | Entry run leaves the worktree clean (`git status --porcelain` after all runs: only `?? selftest.out`, my own shell-redirect artifact; `-B` suppresses bytecode). The self-test's only disk write is a real temp git repo built inside `tempfile.TemporaryDirectory()` (1154-1196), removed by the context manager — measured: `/tmp` `tmp*` entry count 56 → 56 across a self-test run. `--fetch` reads the network: `urllib.request.urlopen` (496), `fetch_probe` (504-514); not executed this session (see gaps). |
| Owner `kotoba` | HOLDS | Lane owner; counter prints the row `OK`. |

## Corroborating frozen-counter run (sandbox, read-only)

`python3 -B verifiers/check_gate_registry.py --rev 58db81c…` → row line `verifiers/check_overlap_levers.py    OK`, summary `gate registry rows conformant 24 of 24 lane verifiers; phantom 0`, **exit 0**.

## Findings (by severity)

**F1 — minor (no row change; script fix as text).** A nonexistent revision grades as `failed` (1) instead of `could-not-evaluate` (2). Measured: `python3 -B verifiers/check_overlap_levers.py --rev 0123456789abcdef0123456789abcdef01234567` → `overlap levers backed 0 of 7 clients`, **exit 1**. Cause: `git_show` maps any failing `git show` to `None` (526-531) and the reader does `read_path(…) or ""` (579-582), so "rev unreadable" is indistinguishable from "file absent at rev". The docstring ladder (60-62) declares exactly this behavior and the row mirrors the script, so the verdict-map cell is not false — but a typo'd hash reads as a red gate. Proposed fix (not applied; lane files untouched): in `--rev` mode, resolve the revision first (`git cat-file -e <rev>^{commit}`) and on failure print `ERROR rev <rev> not readable` and return 2, before reading any file. Registry row stays as landed.

**F2 — observation.** The module docstring (68) says "the only writes are the self-test's stdout and the network reads made by --fetch", under-describing the m18 temp git repo (1154-1196). The registry cell is the more accurate of the two; if the docstring is ever touched, align it. No row change.

**F3 — residual risk (lane-wide, not exercised).** An uncaught exception exits with Python's traceback code 1, which the declared map reads as `failed`; PROTOCOL.md:393-395 reads only *undeclared* nonzero codes as could-not-evaluate, and 1 is declared. Not exercised (would need fault injection); shared by every Python gate row in this registry, not specific to this row.

## Verification gaps

- `--fetch` was not executed (it would hit seven vendor pages; unnecessary to judge the cell — the network read is evident at 487-514). Its failure-downgrade path (`found < k` → `rc = 1`, 616) is therefore unexercised this session.
- Exit behavior under uncaught exceptions not exercised (F3).
- "Removed" for the self-test temp repo rests on the `TemporaryDirectory` context manager (code) plus the unchanged `/tmp` census (measurement); no pathological-interrupt test was run.
