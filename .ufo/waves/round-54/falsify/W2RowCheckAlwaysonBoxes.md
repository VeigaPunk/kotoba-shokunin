Result: HOLDS — every cell of the `verifiers/check_alwayson_boxes.py` registry row (SKILL.md:456) matches the script's real behavior at tip `58db81c`; no corrected row text needed.

# Scope

Row under attack (SKILL.md § Gate registry, landed `bf65974c`; identical at tip — line 442 at `bf65974c`, line 456 at `58db81c`):

`| verifiers/check_alwayson_boxes.py | gate | python3 -B verifiers/check_alwayson_boxes.py --rev <rev> | 0=clean, 1=failed, 2=could-not-evaluate | --self-test | in-file | temp archives and self-test repos (removed) | kotoba |`

`git diff bf65974c..58db81c -- verifiers/check_alwayson_boxes.py` is empty — the script is the same bytes at both revisions; `--self-test` was added by `b55550b9` (before the row). Sandbox: `/fast/scratch/hyaku/kotoba-r54/W2RowCheckAlwaysonBoxes` @ `58db81c4465b0e9b07ef2485b87d8970683afac6` (clone, verified `rev-parse HEAD`). All runs below ran there; the lane checkout was never executed or written (`git status` on the lane file: 0 lines).

# Runs

Entry command (repo root, measured rev = tip):
`python3 -B verifiers/check_alwayson_boxes.py --rev 58db81c4465b0e9b07ef2485b87d8970683afac6` → exit 0, output:
```
always-on boxes executed and discriminating 2 of 8
  alwayson.04: counted (6 of 6 cases as pinned)
  alwayson.07: counted (6 of 6 cases as pinned)
```
Writes only inside a `TemporaryDirectory(prefix="alwayson-")` (lines 214–244): `git archive --format=tar` bytes held in memory (`io.BytesIO`, lines 217–218), extracted `verifiers/` tree (line 219), planted case dirs under `td/cases` (lines 234–235). No lane/clone-tree write, no network, seconds of runtime. Delegate `verifiers/verify_alwayson.py` (invoked per case, lines 184–196) writes nothing — grep finds no `write_text`/`open(` for write/`mkdir`/`tempfile`/`subprocess`; its `os.open` calls are read-only `O_RDONLY` walks (lines 123–210).

Self-test flag:
`python3 -B verifiers/check_alwayson_boxes.py --self-test` → exit 0, output `self-test PASS: counted box exit 0; missing delegate exit 1`. It is the script's own self-test: `self_test()` (lines 96–170) builds two throwaway git repos under `TemporaryDirectory(prefix="alwayson-self-test-")` (lines 116–152), copies the real `verify_alwayson.py` in as the delegate (lines 141–143), then invokes the script itself via `subprocess` on `Path(__file__).resolve()` with `--rev`/`--repo` (lines 153–158) and asserts both exit code and output lines including the finding strings (lines 159–160). The inner call is self-invocation over isolated fixtures, not a foreign check, usage text, or a helper-only probe — satisfies PROTOCOL.md § Gate standard "Self-test" (PROTOCOL.md:398–402) and the plan Erratum-2 guard (row says `gate`, declared flag exits 0 in a sandbox clone at the measured revision: observed).

Exit-path probes (all in sandbox):
- No args / `--self-test --rev <r>`: argparse errors → exit 2 (lines 207, 210). Observed `EXIT_norev=2`, `EXIT_bothflags=2`.
- `--rev deadbeef…` (absent object): `git show` `CalledProcessError` → caught (lines 245–247), prints `cannot evaluate: …`, exit 2. Observed `EXIT_badrev=2`.
- Scratch commit flipping `alwayson.07` disposition to `unexecuted:` → prints `… 1 of 8` + `not counted (disposition unexecuted)`, exit 1 (line 250). Observed `EXIT_flip=1`.
- Scratch commit with `not json {{{` baseline → `cannot evaluate: Expecting value…`, exit 2 (JSONDecodeError, 245–247). Observed `EXIT_badjson=2`.
- Scratch commit with `{"boxes": "x"}` (parseable, wrong shape) → `AttributeError: 'str' object has no attribute 'get'` traceback at line 220 (`b.get`), uncaught → interpreter exit 1. Observed `EXIT_wrongshape=1`.

# Per-cell verdicts (line numbers in verifiers/check_alwayson_boxes.py)

- **Name** `verifiers/check_alwayson_boxes.py` — HOLDS. Exactly one row names the file (SKILL.md:456); C2 counter at tip prints `gate registry rows conformant 24 of 24 lane verifiers; phantom 0`, exit 0 (observed in sandbox).
- **Kind** `gate` — HOLDS. The script compares a revision's live surface (`checklist-baseline.json` dispositions at the measured rev, line 213; delegate behavior on 12 pinned cases, lines 223–244) against committed expected values and returns clean/failed — it can fail (observed exit 1 on the flipped-disposition commit). Not a probe (PROTOCOL.md:390–392).
- **Entry command** — HOLDS. Ran as written from repo root; `LANE` resolution (line 57) and `--repo` default (line 202) make the clone the repo; `--rev` required (lines 201, 209–210); exit 0 with the documented output shape (lines 40–43, 248–250).
- **Verdict map** `0=clean, 1=failed, 2=could-not-evaluate` — HOLDS. All declared codes are produced with the declared meanings: 0 = both pinned boxes counted (line 250); 1 = fewer counted / self-test failure (lines 164, 168, 250); 2 = git failure, unparseable/unreadable map, usage errors (lines 245–247, argparse). No produced code is undeclared: every normal path returns 0/1/2, uncaught exceptions exit 1 (already declared), and the registry preamble (SKILL.md:450–451) plus PROTOCOL.md:395 assign undeclared nonzero to could-not-evaluate anyway.
- **Self-test** `` `--self-test` `` — HOLDS. Flag literal in the file (line 203) at `bf65974c` and tip; dispatches to the script's own `self_test()` (lines 205–208); observed exit 0. Not `none`, not borrowed — the flag is parsed and acted on by this file.
- **Pinned values** `in-file` — HOLDS. True: every expected value is a literal in this file — `CASES` with expected PASS/FAIL (lines 65–88), `SECTION` (58), `TIMEOUT` (59), `RULES_A`/`RULES_B` (61–62), self-test expectations incl. count line and finding strings (97–114), instrument contract in the docstring (28–43). The files read at the measured rev — `verifiers/checklist-baseline.json` (line 213) and the archived delegate `verify_alwayson.py` (lines 217–228) — are the measured input and the graded instrument, not pinned expected values, so they correctly do not appear in this cell.
- **Write scope** `temp archives and self-test repos (removed)` — HOLDS (minor wording nit). Real writes: the per-run temp dir (extracted `verifiers/` tree + planted case dirs, lines 214–235) and the self-test's two temp git repos (lines 116–152); both `TemporaryDirectory` objects auto-remove on exit, all under `$TMPDIR`. Verified: after my runs no new `alwayson-*` dirs remained (one stale `/tmp/alwayson-8oyzswve` has mtime 2026-10-22T20:10Z, ~2 h before my runs — leftover from a killed earlier run, not mine; `TemporaryDirectory` only cleans on normal interpreter exit). "temp archives" is loose — the tarball is in-memory — but the cell's claim (only temp writes, removed) is accurate.
- **Owner** `kotoba` — HOLDS. Lane-owned verifier; the counter accepts only `kotoba` (check_gate_registry.py:56, 180–181).

# Residual risks / notes (script-level, not row defects)

1. A parseable-but-misshapen baseline (`{"boxes": "x"}`, missing keys as non-dicts) crashes with `AttributeError` → exit 1 with a traceback, i.e. a could-not-evaluate condition surfaces as `failed` (the docstring's own taxonomy, line 43, would map "unreadable map" to 2). Catch list at line 245 misses `TypeError`/`AttributeError`. Proposed script fix (not landed — report only): add `TypeError, AttributeError` to the except tuple at line 245.
2. `self_test()` returns 1 on "could not run" infrastructure failures (line 168: OSError, CalledProcessError, TimeoutExpired, TarError), where 2 would fit the taxonomy better. Cosmetic.
3. Exit-1-for-uncaught-exception is fleet-standard (every sibling row has the same property); SKILL.md:450–451 and PROTOCOL.md:395 contain it.

No installs performed or needed (system `python3`, `git`, `tarfile` sufficed).
