Result: HOLDS — every cell of the C2 registry row for `verifiers/verify_surfaces.py` survives attack at 58db81c; two minor observations and two notes, no cell breaks, no corrected row needed.

Seat: KotobaR54.W2RowVerifySurfaces (leaf; no subagents spawned). Date: 2026-10-22.
Row under attack (SKILL.md:478 at 58db81c4465b0e9b07ef2485b87d8970683afac6; identical text at bf65974c7845a06d7ef621ad998c6378ff735cd5:464 — `git diff bf65974..58db81c -- SKILL.md` contains no `verify_surfaces` line):

| `verifiers/verify_surfaces.py` | gate | `python3 -B verifiers/verify_surfaces.py` | 0=clean, 1=failed, 2=could-not-evaluate, 3=could-not-evaluate | `--self-test` | `verifiers/surfaces-baseline.json` | self-test temp files | kotoba |

Sandbox: fresh clone of the lane checked out at 58db81c4465b0e9b07ef2485b87d8970683afac6 at /fast/scratch/hyaku/kotoba-r54/KotobaR54W2RowVerifySurfaces (seat name de-dotted for the filesystem; same identity). All commands below ran there, from the clone root. The lane repo was only read; `git status --porcelain` in the sandbox returns 0 lines after every run below, so nothing in the tree was written by any invocation.

## Cell-by-cell

### Name — HOLDS
`verifiers/verify_surfaces.py` is a blob directly under `verifiers/` at 58db81c; the frozen counter lists it and prints `gate registry rows conformant 24 of 24 lane verifiers; phantom 0`, exit 0 (run in the sandbox against the tip).

### Kind: gate — HOLDS
It is a gate, not a probe: it reads surfaces (the two harness binaries via `strings`, the census artifact, the baseline) and compares them against expected values persisted in its own repo (`verifiers/surfaces-baseline.json`, 42 class entries; source line 1787-1790 default path, `load_baseline` at 316). It can fail: a mutated baseline produces exit 1 with a FAIL verdict (probe below). PROTOCOL.md § Gate standard line 390-392 requires exactly this and forbids registering a can-fail tool as a probe.

### Entry command: `python3 -B verifiers/verify_surfaces.py` — HOLDS
Ran from the clone root, no arguments:
- exit code 0, wall time 14 s (well under the 10-minute skip bar).
- last lines: `PASS surfaces.opencode_extract: opencode extraction 9/9 declared class(es) from 7/7 rules (OC-1, ...)`, `PASS surfaces.table_parity: inventory id set == baseline id set (42 ids)`, `PASS surfaces.literal_parity: 42 inventory row literal(s) match the baseline per id`, `PASS surfaces.kind_parity: 42 inventory row kind(s) match the baseline per id`, `PASS surfaces.excluded_reason: 8 excluded entries, all reasoned and listed in the inventory`.
- read-only: the only subprocess is `strings -n 4 <binary>` with `capture_output=True` (line 292-296) — output is captured in memory, never written; no write site exists before the self-test region (see Write scope). No network access anywhere in the script.
- The command has no `--rev`: it grades the live tree and the host binaries (`/home/vgpnk/.local/bin/omp`, the npx opencode binary, lines 163-166). The SKILL.md preamble's `<rev>` sentence (line 450) constrains rows that take `--rev`; this row takes none, and the script's own docstring declares the contract honestly: "Read-only; deterministic for a fixed host" (line 143) with per-binary sha256/mtime/size reported in `--json` substrate output (lines 1748-1763). See NOTE-2 for the residual.

### Verdict map: `0=clean, 1=failed, 2=could-not-evaluate, 3=could-not-evaluate` — HOLDS
Every declared code is produced with exactly its declared meaning, exercised live in the sandbox:

| Code | Probe | Exit | Last line |
|---|---|---|---|
| 0=clean | `python3 -B verifiers/verify_surfaces.py` (entry run) | 0 | 7× `PASS surfaces.*` |
| 1=failed | `--baseline /tmp/R54-empty.json` (`{"classes": []}`) `--check surfaces.table_parity` | 1 | `FAIL surfaces.table_parity: extra row(s) not in baseline: omp:agent-system-prompt/SYSTEM.md, ...` |
| 2=could-not-evaluate | `--check surfaces.literal_present --omp-strings /tmp/R54-nope.txt` | 2 | `ERROR omp strings dump not found: /tmp/R54-nope.txt` |
| 2 (second cause) | `--check surfaces.table_parity --inventory /tmp/R54-nope.md` | 2 | `ERROR inventory file not found: /tmp/R54-nope.md` |
| 2 (third cause) | `env PATH=/tmp/R54-emptybin /usr/bin/python3 -B verifiers/verify_surfaces.py --omp-binary verifiers/surfaces-baseline.json` | 2 | `ERROR \`strings\` tool unavailable on this host` |
| 3=could-not-evaluate | `--baseline /tmp/R54-nope.json` | 3 | `ERROR baseline not found: /tmp/R54-nope.json` |

Source agreement: main() returns only 0/1 (line 1855), 2 on `EnvError` (line 1827: missing binary, missing/unrunnable `strings` tool at 288-299, missing inventory file via `read_text` at 278-284, OS-level baseline read error at 321-322), 3 on `BaselineError` (line 1800: baseline not found / unparseable, 316-332). The docstring states the same map (lines 138-140). No produced code is missing from the declared map: the only other `SystemExit` is argparse's usage error, which also exits 2 (probe: `--no-such-flag` → exit 2, `verify_surfaces.py: error: unrecognized arguments: --no-such-flag`) — NOTE-1.

### Self-test: `--self-test` — HOLDS
It is the script's own self-test, not a nested call and not usage text:
- the flag exists (`--self-test`, line 1729-1731, help "assert all checks and exit codes on fixtures only") and dispatches to `self_test()` defined in the same file (line 1785-1786 → line 1161);
- `self_test()` calls `main(argv)` in-process with redirected stdout (`run_capture`, lines 1155-1159) over committed fixtures in `verifiers/fixtures/surfaces/` (clean dumps, baseline-clean.json, inventory-clean.md, plus per-generation omp/opencode dumps), i.e. PROTOCOL § Self-test's "self-invocation mode over isolated fixtures";
- run: exit 0 in <1 s, last line `0 failure(s) over 175 assertions`;
- it asserts both exit codes and stable expected finding ids: `rec("clean: exit 0", ...)` (1187), `rec("extra-class: exit 1", ...)` naming `omp:foo/FOO.md` (1193-1195), `rec("missing dump: exit 2", ...)` (1594), `rec("missing inventory: exit 2", ...)` (1690), `rec("missing baseline: exit 3", ...)` (1697), plus ~25 further exit-1 arms each naming its exact FAIL string (`missing-row`, `literal-drift`, `vacuous-parity`, `<unresolved-var:S$>` arms at 1368-1372, 1400-1404). Expected verdicts are hardcoded in the committed script, independent of the recomputation, per PROTOCOL § Self-test;
- no live-tree write: all self-test writes go into `tempfile.TemporaryDirectory()` blocks (see Write scope); no network (fixtures only, <1 s).

### Pinned values: `verifiers/surfaces-baseline.json` — HOLDS
- Exists at the revision: `git cat-file -e 58db81c...:verifiers/surfaces-baseline.json` and `git cat-file -e bf65974...:verifiers/surfaces-baseline.json` both succeed.
- Actually read as expected values: default path resolved at lines 1787-1790 (`repo / "verifiers" / "surfaces-baseline.json"`), parsed by `load_baseline` (316-333) into 42 class entries; those entries feed all seven checks (lines 1815-1848) and, for omp, the declared loader-group pairs feed extraction itself (`declared_loader_pairs(entries, h)` at line 1816).
- Load-bearing, not decorative: pointing `--baseline` at an emptied baseline flips the verdict to exit 1 with `FAIL surfaces.table_parity: extra row(s) not in baseline:` naming every one of the 42 inventory ids (probe above) — the baseline is the comparator the verdict depends on.

### Write scope: `self-test temp files` — HOLDS
- No write site exists outside the self-test region: every `write_text`/`TemporaryDirectory` occurrence sits at line ≥ 1293, i.e. inside `self_test()` (which starts at 1161); lines before 1161 contain no `write_text`, no `mkdir`, no write-mode `open`, no `NamedTemporaryFile` (checked by line-filtered scan of the whole file).
- The normal-mode entry command writes nothing (strings output captured in memory, line 292-296); empirically `git status --porcelain` = 0 lines after the entry run, the self-test, and all six probes.
- Inside the self-test, every write is into a `tempfile.TemporaryDirectory()` context that removes its own files: fixture dump writes at 1293-1299 (`p6`, `p5`, `pp` under `tmp`), 1339-1341 (`strings-omp-renamed.txt`), 1367-1369 (`strings-omp-ambiguous.txt`), 1415-1417 (`strings-omp-param-shadow.txt`). "self-test temp files" is an exact description.

### Owner: `kotoba` — HOLDS
Lane owner; the frozen counter accepts it and prints 24 of 24.

## Findings by severity

No major or minor-breaking findings. No cell breaks; no corrected row text is proposed.

- MINOR (protocol-letter gap, non-actionable this round): PROTOCOL.md § Gate standard, "Two evidences" (line ~407-410) says a frozen baseline's expected.json MUST pin the digest of every snapshot input file and the gate verifies those digests before comparing ("an edited snapshot is `snapshot_tampered` (could-not-evaluate) ... a baseline without digests is reported `unpinned (legacy)`"). The snapshot-run expected values here — `verifiers/fixtures/surfaces/baseline-clean.json` and `baseline-18.12.5.json` — contain zero sha256 keys (`grep -c sha256` = 0 in both), and the script never reports `snapshot_tampered` or `unpinned (legacy)`. The clause predates the round (present since kimi-shokunin e737d2e, 2026-10-19), so its letter was in force when the row landed. It does not break a declared cell (the pinned-values cell names the live baseline, which is read as expected values — that attack question holds), and the round's binding drift rule ("no change to verifiers/verify_surfaces.py") makes the only honest fix a later-round item. Proposed fix text for a later round, for the L1 to weigh: add a `fixtures` digest pin (sha256 of each `strings-*.txt` fixture) to the fixture baselines, verify the digests before comparing, exit 2 with `snapshot_tampered: <file>` on mismatch and print `unpinned (legacy)` for a digest-less baseline.
- NOTE-1 (benign overload): argparse usage errors exit 2 (`SystemExit(2)`), the same number declared as could-not-evaluate. A bad invocation genuinely is could-not-evaluate, so the declared map absorbs the collision; for the same reason `--help` exits 0 without any measurement. Shared with every argparse-based gate in the lane; no action proposed.
- NOTE-2 (residual semantics smear): an uncaught exception exits with the interpreter's code 1, which the declared map reads as "failed" although no check FAILed; and the live verdict grades the moving host binaries plus worktree. The script mitigates attribution by printing per-binary sha256/mtime/size in `--json` substrate output (lines 1748-1763), but nothing pins those digests. Residual risk shared across the lane's Python gates; the counter's docstring already declares produced-code and kind questions reviewer territory (Q31).

## Verification gaps

None material. All four declared exit codes, all three distinct exit-2 causes, the exit-1 fail path, the exit-3 baseline path, the self-test run, and the no-write claim were exercised or proven from source, at 58db81c, in the sandbox. The only arm asserted from source rather than triggered live is nothing — every `EnvError`/`BaselineError` arm listed in the docstring was hit by a probe (missing dump, missing inventory, missing strings tool, missing baseline) or by the self-test's own arms (exit 2 at 1594/1690, exit 3 at 1697). Runtime observed: entry 14 s, self-test <1 s.

Tooling record: no package installed or upgraded for this seat (nothing needed; no pacman, uv, or binary installs).

Commands and exit codes cited above were run in /fast/scratch/hyaku/kotoba-r54/KotobaR54W2RowVerifySurfaces at 58db81c4465b0e9b07ef2485b87d8970683afac6 on 2026-10-22; the lane repo was not written and lane jj/git state untouched.
