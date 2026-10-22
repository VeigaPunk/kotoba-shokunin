Result: HOLDS — every cell of the `verifiers/check_substrate_pins.py` registry row at `bf65974c` matches the script's real behavior; no corrected row needed.

# Scope

Row under attack (`SKILL.md` § Gate registry, `bf65974c7845a06d7ef621ad998c6378ff735cd5`, line 454; identical at tip `58db81c4`):

```
| `verifiers/check_substrate_pins.py` | gate | `python3 -B verifiers/check_substrate_pins.py` | 0=clean, 1=failed, 2=could-not-evaluate, 3=could-not-evaluate | `--self-test` | `verifiers/baseline.json` | self-test files under `$TMPDIR` | kotoba |
```

Sandbox: `git clone /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r54/W2RowCheckSubstratePins`, checkout `58db81c4465b0e9b07ef2485b87d8970683afac6`. The script is byte-identical at base `422ffd10`, landed `bf65974c`, and tip (md5 `04ac2948207000e68b43a585aa705e6d`, 576 lines), so running the tip copy tests the landed bytes. Line numbers below are the file at tip = landed commit.

# (1) Runs

Entry command (read-only check: it opens `baseline.json` and the two host binaries for reading only — `open(path, "rb")` line 135, `read_text()` line 323, `.stat()` line 249; no writes, no network, 0.26 s):

```
$ python3 -B verifiers/check_substrate_pins.py        # in sandbox clone
PASS omp_binary_sha256: 85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4
PASS omp_binary_mtime: delta 0 ns (tolerance 0 ns)
PASS opencode_binary_sha256: 538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7
OK 3/3 pins hold
ENTRY_EXIT=0
```

Declared self-test flag (the script's own `self_test()`, lines 315–316 dispatch → 349–567; exercises the real `main()` in-process via `run_capture` lines 342–346/392–394 over fixture baselines + a fixture binary, asserting exit codes 0/1/2/3 and `--json`/`exit_code` agreement — not a nested call to another tool, not usage text):

```
$ python3 -B verifiers/check_substrate_pins.py --self-test
0 failure(s) over 62 assertions
SELFTEST_EXIT=0
```

# (2) Cell-by-cell

- **Name** `verifiers/check_substrate_pins.py` — HOLDS. Blob exists at `bf65974c` (`git cat-file -e` on the row's pinned path; script md5 matches across base/landed/tip).
- **Kind** `gate` — HOLDS. PROTOCOL.md § Gate standard: a gate reads surfaces and compares against expected values persisted in its own repo and can fail. This script compares live substrate sha256/mtime against committed pins in `verifiers/baseline.json` and exits 1 on DRIFT/PIN_ABSENT/VACUOUS (`VERDICT_CODE` lines 116–125; `code_of` 128–130).
- **Entry command** — HOLDS. Ran green above; contains `verifiers/check_substrate_pins.py` literally. Host-anchored reads of `/home/vgpnk/.local/bin/omp` and the npx `opencode.exe` (lines 64–67, 40–46) are reads, not writes — inside the stated skip rule.
- **Verdict map** `0=clean, 1=failed, 2=could-not-evaluate, 3=could-not-evaluate` — HOLDS. Every code the script produces is declared: `sys.exit(main())` (575–576) returns `code_of(results)` ∈ {0,1,2,3} (VERDICT_CODE 116–125) or `return 3` on baseline IO/parse failure (322–329); `self_test()` returns 0/1 (567). `0=clean` = all PASS; `1=failed` = DRIFT/PIN_ABSENT/VACUOUS; `2=could-not-evaluate` = UNREADABLE/UNSUPPORTED (binary not readable, unresolvable or non-canonical pin key — the pin cannot be evaluated, docstring 16–20); `3=could-not-evaluate` = NO_BASELINE/BAD_PIN (21–23). Gate requirement `0=clean`+`1=failed` met. No produced code missing: argparse's usage-error exit is also 2 (declared class). No undeclared code reachable.
- **Self-test** `` `--self-test` `` — HOLDS. Literal flag at line 311 (`ap.add_argument("--self-test", ...)`); runs `self_test()` which asserts exit codes and stable finding strings over `tempfile` fixtures — satisfies the standard's isolated-fixture clause; real flag, not `none`.
- **Pinned values** `` `verifiers/baseline.json` `` — HOLDS. Path exists at `bf65974c` (`git cat-file -e bf65974c:verifiers/baseline.json` OK). Read at line 318–319 (`<repo>/verifiers/baseline.json` default) and parsed line 323; its `measured_against` block carries the expected pin values (`omp_binary_sha256`, `omp_binary_mtime`, `opencode_binary_sha256` — observed in the file) compared as `expect` at lines 217–258.
- **Write scope** `self-test files under $TMPDIR` — HOLDS. All writes live inside `self_test()` under `tempfile.TemporaryDirectory(prefix="pins-selftest-")` (line 361): `mini.write_bytes` 364, fixture `write_text` 380, `os_utime` 419/422 (helper 570–572) on the fixture only, `symlink_to` 505, `write_bytes`/`chmod` 509–513. Normal path writes nothing. `$TMPDIR` is tempfile's honored env root. Scope cell accurate.
- **Owner** `kotoba` — HOLDS (lane-owned; counter-required literal).

# Residual risk / gaps

- UNSUPPORTED mapped to `could-not-evaluate` rather than `failed` is a lane-owned judgment: a mis-cased/whitespace-padded/unknown-substrate pin key is a malformed baseline *input* the gate declines to resolve. Declared in the row and the docstring (16–20); honest, not a defect.
- The self-test asserts exit codes and substrings but the "stable expected finding-id" is per-pin naming (`FAIL <pin>: <VERDICT>`), which is this gate's finding vocabulary — adequate.
- Not exercised: a live DRIFT on the real host binaries (would need mutating `/home/vgpnk/.local/bin/omp` or the baseline — out of bounds). Fixture coverage of DRIFT exists in the self-test (lines 407–421).

Attack verdict: HOLDS on all eight cells. No patch proposed.
