Result: HOLDS — every cell of the `verifiers/check_opencode_repin.py` registry row (SKILL.md:464, landed bf65974c) matches observed behavior of the script at 58db81c4 in a sandbox clone; no defect found, no corrected row needed.

Seat: KotobaR54.W2RowCheckOpencodeRepin, 2026-10-22. Sandbox: `/fast/scratch/hyaku/kotoba-r54/KotobaR54.W2RowCheckOpencodeRepin` cloned from the lane, checked out at `58db81c4465b0e9b07ef2485b87d8970683afac6`. Row under attack: SKILL.md:464 under `## Gate registry` (SKILL.md:447, header SKILL.md:453). No installs were needed; no lane file was touched by any check (all runs in the sandbox clone).

Context re-run (frozen C2 counter, read-only): `python3 -B verifiers/check_gate_registry.py --rev 58db81c4...` → `gate registry rows conformant 24 of 24 lane verifiers; phantom 0`, exit 0, with `verifiers/check_opencode_repin.py  OK`. So the row is counter-conformant as landed; what follows attacks what the counter does not measure (plans/round-54.md:49-51).

## Cell-by-cell

**1. Name `verifiers/check_opencode_repin.py` — HOLDS.** Blob exists directly under `verifiers/` at the revision; the counter lists it in the 24-file universe.

**2. Kind `gate` — HOLDS.** It is the frozen counter for the round-53 C1 (freshness) claim (`verifiers/check_opencode_repin.py:3-5`), with a hard pass/fail predicate over measured values: exit 0 iff surfaces pass 7/7 with opencode_extract PASS, pins OK 3/3, all opencode classes kept, self-test 0 failures at ≥129 assertions; else 1 (`:35-36`, `:251-253`). Plan erratum 2 names it among the four scripts that must carry kind `gate` plus a working declared self-test for C2 to be claimed (plans/round-54.md:88-93); the self-test landed in b55550b9 (`git log 422ffd10..58db81c4 -- verifiers/check_opencode_repin.py` → exactly one commit, b55550b "own --self-test modes for four gates that had none … check_opencode_repin"). Not a probe: it decides a claim, it does not merely report.

**3. Entry `python3 -B verifiers/check_opencode_repin.py --rev <rev>` — HOLDS.** Run verbatim in the sandbox from the repo root:

```
$ python3 -B verifiers/check_opencode_repin.py --rev 58db81c4465b0e9b07ef2485b87d8970683afac6
opencode re-pin: surfaces pass 7 of 7 (opencode_extract PASS); pins OK 3/3; opencode classes kept 9 of 9; self-test 0 failure(s) over 175 assertions
substrate opencode: /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe sha256 538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7 bytes 214522032
EXIT=0   (14.6 s real)
```

No network used; the only host contact is read-only opens of the installed binaries, which the docstring declares as the measurement substrate (`:38-40`). Args match argparse (`--rev` required unless `--self-test`, `:199-205`); `--repo` defaults to the script's own lane (`:63`, `:201`), so the cell needs no extra argument.

**4. Verdict map `0=clean, 1=failed, 2=could-not-evaluate` — HOLDS.** All three produced with the declared meanings, none missing:
- 0 = clean: `:253` `return 0 if ok else 1` behind the full predicate `:251-252`; observed exit 0 above on a passing world.
- 1 = failed: same line on a failing predicate. Empirical even without a broken lane: the script's own self-test drives `main()` over a retired-class world and asserts `code == 1` (`:177-184`, check `retired class is failed with stable finding`), and that self-test passed (see cell 5).
- 2 = could-not-evaluate: `:215-216` (gate or pin script missing in the extracted tree, printing `cannot evaluate: …`) and `:244-246` (catch of `CalledProcessError, JSONDecodeError, KeyError, ValueError, OSError, TarError`, printing `cannot evaluate: …`). Demonstrated: `python3 -B verifiers/check_opencode_repin.py --rev 0123456789abcdef0123456789abcdef01234567` → stderr `cannot evaluate: Command '['git', … 'archive' …]' returned non-zero exit status 128.`, EXIT=2.
- No undeclared code is reachable: the only exits are `sys.exit(main())` (`:257`), the three returns above, and argparse usage failure which also exits 2 (`ap.error`, `:204-205`; observed: bare run → `check_opencode_repin.py: error: --rev is required unless --self-test is selected`, exit 2 — same declared code, so no gap; the SKILL.md preamble already reads undeclared nonzero as could-not-evaluate anyway).
- Edge semantics noted, not a defect: a revision whose `verifiers/baseline.json` is unreadable makes the pins step yield 0 holding of 1 row → exit 1 (failed), not 2; that is the frozen docstring contract ("1 otherwise", `:35-36`) and the row states the script's contract faithfully.

**5. Self-test `--self-test` — HOLDS; it is the script's own self-test.** Flag is a real argparse option dispatching to `self_test()` (`:201-203`), which builds an isolated throwaway git repo under a `TemporaryDirectory` (`:101-116`), writes stub `verify_surfaces.py` / `check_substrate_pins.py` into it (`:129-150`), swaps the module-global `BASE_REV` to the fixture commit and restores it afterwards (`:154-155`, `:186-187`), then calls its own `main()` twice over redirected stdout/stderr (`:157-162`) asserting the clean world exits 0 with the exact clean line and the retired-class world exits 1 with the exact failed line (`:165-184`). It reads no host binaries (`:45`) and ran in 0.12 s:

```
$ python3 -B verifiers/check_opencode_repin.py --self-test
0 failure(s) over 2 assertions
EXIT=0
```

Not usage text, not a foreign script's self-test (the recursive `main()` call is the script exercising itself — that is the definition of the declared flag).

**6. Pinned values `verifiers/surfaces-baseline.json`, `verifiers/baseline.json` — HOLDS.** Both paths exist at the revision (`git cat-file -e 58db81c4…:verifiers/surfaces-baseline.json` and `…:verifiers/baseline.json` both succeed) and both are actually consumed as expected values by the entry command:
- `verifiers/surfaces-baseline.json` is read directly twice: at BASE_REV via `git show {BASE_REV}:verifiers/surfaces-baseline.json` (`:208`) and at the measured revision from the extracted tree (`:230`), and its class tuples are compared as the expected values (`:231`).
- `verifiers/baseline.json` is consumed mediated through the revision's own pin checker: the entry runs the tree's `check_substrate_pins.py --json --repo <tree>` (`:224-225`), whose default baseline path is `<repo>/verifiers/baseline.json` (`verifiers/check_substrate_pins.py:318-319`) and which reads it there (`:323`); the gate consumes its per-pin PASS verdicts (`:228-229`) in the exit predicate `k == n == PINS_TOTAL` with `PINS_TOTAL = 3` in-file (`:61`, `:251`). The pins the claim is about are exactly this file's `measured_against` values at the measured revision. [INFERENCE on intent, evidence on mechanism: the cell is honest under the row's meaning — every declared path's values reach the verdict; no over-wide record.] Strict-reader caveat for a later round: `check_opencode_repin.py` never opens `verifiers/baseline.json` with its own file handle; if the registry ever moves to open()-level strictness, this cell would need a delegation note. As landed, the counter's existence rule and the observed data flow both support the cell.

**7. Write scope `temp trees under $TMPDIR (removed)` — HOLDS.** Entry mode writes exactly one tree, `TemporaryDirectory(prefix="oc-repin-")` filled by `git archive … | tar extractall` (`:209-211`, `:70-74`), removed by the context manager. Self-test mode writes exactly one tree, `TemporaryDirectory(prefix="oc-repin-self-test-")` including its throwaway git repo (`:101-116`), also removed. Both child invocations and the top-level run use `-B` (`:217`, `:224`, `:232`; entry command cell), so no `__pycache__` is written anywhere; the invoked children are read-only in the modes used (`check_substrate_pins.py:34-36` "opens the baseline and the binaries for reading only"; `verify_surfaces.py` writes only inside its own `--self-test` fixture section, and it is called with `--json`/`--self-test --repo <tree>` here). Empirical residue check after all runs: `git status --porcelain` in the sandbox → 0 lines; `ls -d /tmp/oc-repin*` → no matches. Nothing is written outside `$TMPDIR`.

**8. Owner `kotoba` — HOLDS.** Matches the lane (kotoba-shokunin) and the counter's pinned owner constant; enforced by the passing counter re-run above.

## Gate vs probe

Gate, correctly labeled: it is a frozen claim counter with a declared verdict ladder and a working self-test; its result gates the round-53 C1 claim, and round-54 erratum 2 (plans/round-54.md:88-93) requires exactly this shape — `gate` plus a declared flag that exits 0 in a sandbox clone at the measured revision. Both halves observed (entry 0, self-test 0). The write-scope and pinned-values cells are honest; the verdict map is complete.

## Residual risk and verification gaps

- The entry command's verdict is substrate-dependent by design (it names the measured binaries on line 2, `:38-40`): a rebuilt host binary flips a future re-run to exit 1 without any row defect. Recorded, not attacked — no freshness work this round (drift rule).
- Exit 1 was exercised via the self-test's retired-class world rather than a broken real lane; the retired-world assertion (`:177-184`) is the script's own proof of the 1=failed mapping and it passed, but I did not construct an independent broken-lane run.
- The 2=could-not-evaluate demonstration used a bogus rev (git archive failure path, `:244-246`); the `:215-216` missing-script branch is source-verified only.
- `verifiers/floors-registry.json` is cited only in a comment (`:62`, `SELFTEST_FLOOR = 129` pinned in-file); the row correctly does not declare it, and I did not check the comment's accuracy against that file — out of row scope.
- Tooling: none installed or upgraded; existing python3/git sufficed.
