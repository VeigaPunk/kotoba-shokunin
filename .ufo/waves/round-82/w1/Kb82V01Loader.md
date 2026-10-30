# Kb82V01Loader — review of E01 path/extractor patch (C1 freshness, host loader re-pin)

Seat: Kb82V01Loader (leaf, reviewer; no subagents). Base: `47dbe8781657de563ff867caca6244d28e3db504`.
Reviewed artifact: `.ufo/waves/round-82/build/Kb82E01Paths-c1-paths.patch` (sha256 `24be1b0c5bdc0a1abe5aadf9f2ae96f8978f46d2267498f69e6813d1b2236770`).
Scratch: `/fast/scratch/hyaku/kotoba-r82/Kb82V01Loader/` (clone toplevel asserted; fixture-only commit `9abad59` in scratch clone; no lane mutation; deleted on exit).

## 1. Host facts — independently measured from the live binary

| fact | observed by this seat | E01 claim | match |
|---|---|---|---|
| path exists / `omp.real` absent | `/home/vgpnk/.local/bin/omp` present; `omp.real` → ENOENT | same | yes |
| ELF magic | `7f 45 4c 46`; `file`: ELF 64-bit x86-64, not stripped | same | yes |
| version | `omp/18.14.0`, exit 0 | same | yes |
| bytes | 276244656 | same | yes |
| sha256 | `e7dd2b606c4ebe9d1a7bcfad1b8820db968cd6b05409fed1c6bc8db0b6a95a8f` | same | yes |
| mtime_ns | 1793326786168359786 (2026-10-29 23:19:46.168359786 -0300) | same | yes |
| strings dump | `strings -a -n 4` → sha256 `81277d35…8319` | same | yes |

Matches L1 `receipts/host-open.json` on path, sha, bytes, mtime_ns, version, elf=true.

## 2. Loader-pair derivation — independent method, not a rerun

E01 ran the committed generic extractor (`verify_surfaces.extract_classes`, callee-admission rule). That is the gate's own code, so I did not re-run it as a second derivation. I wrote a separate line-based scanner (`Kb82V01Loader-derive-pairs.py`) with no callee-admission logic and no dump-wide constant table in the matching path. It matches `CALLEE(ARG, GROUP, "FILE.md")` per line, resolves the group from (a) a literal, (b) a same-line binding, or (c) a dump-wide binding that is unique, and otherwise marks it unresolved. Class membership is read from `verifiers/surfaces-baseline.json` at base.

Result (`build/Kb82V01Loader-derivation.txt`): 11 raw call-shape hits, 8 distinct (group, file) pairs, all 8 declared `loader-group` pairs PRESENT, **0 undeclared pairs**. `DERIVATION-MATCH`.

Call sites (grep-verified in the dump; line numbers from `tmp/omp-strings.txt`):

| pair | callee | sites |
|---|---|---|
| agents-md/AGENTS.md | `F9` (group `nD`, `var nD = "agents-md"` at line 972667) | `return F9(u, nD, "AGENTS.md")` line 972670 |
| claude-md/CLAUDE.md | `F9` (group `rD`, `var rD = "claude-md"` at line 972678) | line 972681 |
| gemini/GEMINI.md, gemini/system.md, gemini/SYSTEM_TEMPLATE.md | `ts`, `Ac` | lines 976407, 976418, 976543–976546 |
| github/copilot-instructions.md | `ts` | line 976880 |
| opencode/AGENTS.md | `Ac` | line 976641 |
| windsurf/memories/global_rules.md | `Ac` | line 977791 |

**Finding F1 (documentation, not a gate defect):** E01's note in `Kb82E01Paths-loader-pairs-18.14.0.txt` and §2 of its report says the active registration callees are `ts, Ac`. The independent derivation shows the active set is `{ts, Ac, F9}`. `F9` carries two of the eight classes (agents-md, claude-md) through identifier-bound groups. The 8-class outcome is still correct, but the stated callee list is incomplete. Fix in E02's pinned note or the builder's report; it is not a patch hunk.

## 3. Hunk-by-hunk disposition (patch applied in scratch with `git apply`, exit 0, 4 files, 17+/13-)

| file | hunk | disposition | reason |
|---|---|---|---|
| `verifiers/check_substrate_pins.py` | `BINARIES["omp"]` → `~/.local/bin/omp`; comment rewritten | **LAND** | Path is the live ELF (verified §1). Comment states the round-82 fact; the split sha across two comment lines (`…fed1c` / `6bc8…`) is cosmetic, not a defect. |
| `verifiers/verify_surfaces.py` | `DEFAULT_BINARIES["omp"]` → `~/.local/bin/omp`; comment | **LAND** | Same binary; default-path gate now resolves. Verified 7/7 with patched default (§4). |
| `verifiers/verify_harness_claims.py` | `OMP_BIN` → `~/.local/bin/omp` | **LAND** | Same binary. Its live run was not executed by this seat (see §5). |
| `verifiers/verify_harness_independent.py` | `DEFAULT_OMP_BINARY` → `~/.local/bin/omp`; comment | **LAND** | Same binary. |
| (none) `check_substrate_repin_v2.py`, `surfaces-baseline.json`, `baseline.json`, census, ledger | not touched | **N/A — correctly out of scope** | Frozen counter unchanged; expected values are E02's re-pin. Confirmed by `git diff --stat` (only the four verifier files). |

Refused hunks: **none.** The patch is path-only, adds no expected-value change, and mutates no census class, ledger row, or counter bytes.

Residual `omp.real` mentions in the four files are historical narrative inside comments only (grep: lines 66, 165, 124). They are harmless; they are not live defaults. Not a refusal reason.

## 4. Gate runs (scratch clone, patched tree at fixture commit `9abad59`)

| command | exit | observed |
|---|---|---|
| `python3 -B verifiers/check_substrate_pins.py --self-test` | 0 | `0 failure(s) over 62 assertions` |
| `python3 -B verifiers/verify_harness_claims.py --self-test` | 0 | `self-test: 0 failure(s) over 10 assertions` |
| `python3 -B verifiers/verify_harness_independent.py --self-test` | 0 | `0 failure(s) over 123 assertions` (elapsed 126.06 s; see §5) |
| `python3 -B verifiers/verify_surfaces.py --self-test` | 0 | `0 failure(s) over 218 assertions` (2 `ERROR` lines are expected negative-arm fixtures) |
| `python3 -B verifiers/verify_surfaces.py --json` (live host, patched default) | 0 | pass 7 / fail 0; checks: literal_present, no_uncovered_class, opencode_extract (6/6 classes, 3 ledgered removals, 7/7 rules), table_parity 42, literal_parity 42, kind_parity 42, excluded_reason 8 |
| `python3 -B verifiers/check_substrate_pins.py --json` (live host, patched default) | 1 | omp_binary_sha256 DRIFT (observed `e7dd2b60…`, expect `85d9daf3…`); omp_binary_mtime DRIFT (observed `1793326786168359786`, expect `2026-10-21…`, delta 700941552809949 ns); opencode PASS. pass 1 / fail 2. Receipt: `build/Kb82V01Loader-pins-patched.txt`. |
| `check_substrate_repin_v2.py --rev 47dbe87…` (base, unpatched tree) | 2 | `cannot evaluate: … omp binary not found: /home/vgpnk/.local/bin/omp.real` (the before state; matches the committed before receipt's failure mode). |
| `check_substrate_repin_v2.py --rev 9abad59…` (patched fixture rev) | 1 | `host substrate re-derived: pins OK 1/3; surfaces pass 7 of 7; removal ledger 3 of 3 verified` / `FAIL pins: 1 of 3 row(s) hold`. Expected: the two omp pins fail until E02 re-pins `baseline.json`. This is an intermediate state, **not a C1 score**. |

Pins DRIFT on `omp` is the expected handoff to E02: E01's report explicitly leaves expected values to E02. The patch makes the omp pins *resolve* (they were UNREADABLE at base) — that is the defect it fixes.

## 5. Limits, timing, and what was not observed

- `verify_harness_independent --self-test` takes ~126 s, above the 120 s contention cap; my first run was killed at my tool deadline (exit 124, no result). The rerun with a 600 s deadline exited 0 with 0 failures over 123 assertions. Elapsed is recorded here; no other heavy process was started by this seat.
- I did not run `verify_harness_claims.py` or `compare_harness_independent.py` against the live host. Those are the omp-facing live instruments; E01 did not run them either. Unobserved, not claimed.
- I did not run the frozen counter at a fixture rev that also re-pins `baseline.json`. That is E02's work; no C1 after-value is claimed here.
- The frozen counter at base ran from my scratch clone; its `--rev` extraction uses `git archive`, so the counter reads committed bytes, not the working tree. I confirmed this by reading `extract()` in `check_substrate_repin_v2.py`.

## 6. Tooling record

No installs or upgrades. Only pre-existing coreutils (`sha256sum`, `stat`, `file`, `od`, `awk`, `sed`), binutils `strings`, and the host `python3`. pacman untouched (paused).

## 7. Mistakes (own)

| # | what happened | fix |
|---|---|---|
| M1 | First scanner resolved identifiers only on the same line, so `nD`/`rD` came out unresolved and the derivation read DIVERGENT. | Added dump-wide unique bindings; fixed the prefilter (`'="' in line` missed `= "`). Re-run gave DERIVATION-MATCH. The DIVERGENT verdict was a scanner bug, not a finding against E01. |
| M2 | `verify_harness_independent --self-test` backgrounded at the tool deadline (exit 124). | Re-ran with a longer deadline; recorded the 126 s elapsed above. |
| M3 | The frozen counter's `--rev` path reads committed bytes via `git archive`, so the patch had to be committed in scratch to be measured at a rev. I made fixture-only commit `9abad59` in the scratch clone (scratch identity, toplevel asserted). | Commit lives only in `/fast/scratch/hyaku/kotoba-r82/Kb82V01Loader/clone`; no lane git index, branch, or jj state touched; base remains `47dbe87`. |

## 8. Verdict on E01

- **Land** all four hunks (`check_substrate_pins.py`, `verify_surfaces.py`, `verify_harness_claims.py`, `verify_harness_independent.py`).
- **Do not re-run the extractor fix**: the unchanged round-52 generic extractor derives all 8 declared loader pairs from the live dump. The only extractor-side issue is the incomplete callee note (F1), which is documentation.
- E02 owns the pin values (`baseline.json`); the observed live values for E02 are: omp sha `e7dd2b606c4ebe9d1a7bcfad1b8820db968cd6b05409fed1c6bc8db0b6a95a8f`, omp mtime_ns `1793326786168359786`.

## Residual risk

- F1: E01's documentation of the callee set is incomplete (`F9`). Low, since the gate's outcome is correct.
- Pins remain DRIFT until E02 lands; C1 is not met by this patch alone.
- The omp mtime pin is ns-exact with tolerance 0. Any reinstall of the binary between measurement and pin would break it again.

VERDICT: LAND — all four E01 hunks land as path-only changes; live ELF identity (18.14.0, sha `e7dd2b60…`, mtime_ns `1793326786168359786`) independently re-measured; 8/8 loader pairs re-derived by an independent scanner with 0 undeclared; self-tests 62/10/123/218 all exit 0; surfaces 7/7 exit 0 live. Documentation finding F1 (callee set omits `F9`). C1 not satisfied by this patch alone (pins DRIFT pending E02's re-pin).

DELIVERABLES:
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82V01Loader.md
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82V01Loader-derive-pairs.py
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82V01Loader-derivation.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82V01Loader-applied-patch-verify.diff
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82V01Loader-pins-patched.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82V01Loader-counter-base.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82V01Loader-counter-patched.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82V01Loader-sha256.txt
