# Kb82E01Paths — C1 code owner: host omp 18.14.0 default-path re-pin (paths only)

Seat: Kb82E01Paths (leaf, C1 code owner). Base: `47dbe8781657de563ff867caca6244d28e3db504`.
Scratch clone: `/fast/scratch/hyaku/kotoba-r82/Kb82E01Paths/clone` (shared clone, toplevel asserted before edits; no commits).

## 1. Host binary verification (precondition for any path change)

Measured independently on the live host (before touching any default):

| fact | value |
|---|---|
| path | `/home/vgpnk/.local/bin/omp` |
| ELF magic | `7f 45 4c 46` (`file`: ELF 64-bit LSB executable, x86-64, dynamically linked, not stripped) |
| version | `omp --version` → `omp/18.14.0`, exit 0 |
| size | 276244656 bytes |
| mtime | 2026-10-29 23:19:46.168359786 -0300 (ns 1793326786168359786) |
| sha256 | `e7dd2b606c4ebe9d1a7bcfad1b8820db968cd6b05409fed1c6bc8db0b6a95a8f` |

Matches L1's committed `plan006a834c` receipt (`.ufo/waves/round-82/receipts/host-open.json`) on sha, size, mtime_ns, version. `/home/vgpnk/.local/bin/omp.real` is absent; the file at `omp` IS the ELF that runs (no wrapper indirection). Strings dump: `strings -a -n 4` → 2546730 lines / 47434077 bytes, sha256 `81277d3572277febcaf0853f10cf8778c64920f58a13fba98ef0accbb70a8319` (re-derivable; scratch deleted on exit per policy).

## 2. Call-shape derivation on 18.14.0 (extractor health)

Surveyed registration-call shapes in the live dump. The `.md`-suffixed loader registrations are now emitted through callees **`ts` and `Ac`** (e.g. `ts(u, "github", "copilot-instructions.md")`, `Ac(u, "windsurf", "memories/global_rules.md")`) — the 18.12.6 names Kl/Ho/bq have minified-rotated again, as expected. Per L1 (R03 recon) and the round-52 design, the historical callee allowlist was NOT expanded.

Ran the **unchanged** round-52 declared-pair generic extractor (`verify_surfaces.extract_classes` with `declared_loader_pairs` from the unchanged `verifiers/surfaces-baseline.json`) against the live dump: all **8 loader classes** extract, zero undeclared, zero vacuity:

```
agents-md  AGENTS.md          claude-md  CLAUDE.md
gemini     GEMINI.md          gemini     SYSTEM_TEMPLATE.md
gemini     system.md          github     copilot-instructions.md
opencode   AGENTS.md          windsurf   memories/global_rules.md
```

**Extractor needs NO changes → NO second candidate patch.** (8 classes preserved; 42-class census/baseline untouched; expected values untouched — E02 owns the re-pin of `baseline.json`/`surfaces-baseline.json`.)

Full gate, unchanged code, live dumps of BOTH harnesses (opencode live dump sha `020fb253…` matches the sha already quoted in verify_surfaces.py — host opencode unchanged since round 72):

```
PASS surfaces.literal_present      39 loader-kind entries
PASS surfaces.no_uncovered_class   all 8 extracted loader class(es) declared
PASS surfaces.opencode_extract     6/6 classes, 3 ledgered removals, 7/7 rules
PASS surfaces.table_parity         42 ids
PASS surfaces.literal_parity       42 ids
PASS surfaces.kind_parity          42 ids
PASS surfaces.excluded_reason      8 excluded, reasoned
exit=0
```

Template anchor `compress-description` present (4 occurrences) — harness-claims substrate readers remain well-formed on the new ELF.

## 3. Patch 1 (only patch): default-path update, 4 files

`build/Kb82E01Paths-c1-paths.patch` (sha256 `24be1b0c5bdc0a1abe5aadf9f2ae96f8978f46d2267498f69e6813d1b2236770`). Path-only: every `omp` default `/home/vgpnk/.local/bin/omp.real` → `/home/vgpnk/.local/bin/omp`, with comments rewritten to state the round-82 fact (ELF again, 18.14.0, sha `e7dd2b60…`, wrapper/`omp.real` gone). Exactly 4 files, 21 added lines, no expected-value changes, no census/baseline/ledger changes, no counter changes:

1. `verifiers/check_substrate_pins.py` — `BINARIES["omp"]` + comment (lines 64–72)
2. `verifiers/verify_surfaces.py` — `DEFAULT_BINARIES["omp"]` + comment (lines 163–170)
3. `verifiers/verify_harness_claims.py` — `OMP_BIN` (line 53)
4. `verifiers/verify_harness_independent.py` — `DEFAULT_OMP_BINARY` + comment (lines 123–125)

`verifiers/check_substrate_repin_v2.py` (frozen round-72 counter) NOT touched — no historical counter rewrite. Remaining `omp.real` mentions in the four files are historical narrative inside comments only.

## 4. Selftests of touched gates (patched clone, scratch)

| gate | command | result |
|---|---|---|
| check_substrate_pins.py | `--self-test` | exit 0, `0 failure(s) over 62 assertions` |
| verify_surfaces.py | `--self-test` | exit 0, `0 failure(s) over 218 assertions` (2 ERROR lines are the negative-arm fixtures, expected) |
| verify_harness_claims.py | `--self-test` | exit 0, `0 failure(s) over 10 assertions` |
| verify_harness_independent.py | `--self-test` | exit 0, `0 failure(s) over 123 assertions` |

## 5. Before→patched-default pins gate (evidence for E02; not a C1 score)

`python3 -B verifiers/check_substrate_pins.py --json` with patched default on the live host (`build/pins-patched-default.json`):
before = 1 PASS / 2 UNREADABLE, exit 2 (`.ufo/waves/round-82/receipts/before-pins.txt`); after-patch-default = 1 PASS / 2 DRIFT, exit 1, with omp pins now RESOLVED:
- `omp_binary_sha256` observed `e7dd2b606c4ebe9d1a7bcfad1b8820db968cd6b05409fed1c6bc8db0b6a95a8f`
- `omp_binary_mtime` observed `1793326786168359786` (ns)
- `opencode_binary_sha256` PASS (unchanged)

These observed values are exactly what E02 needs to re-pin; expected values left for E02 per seat split.

## Risks / notes

- None blocking. Extractor is callee-rename-robust by design; verified live on 18.14.0. If a future rebuild changes the registration *shape* (not just callee names), the round-52 rule fails loud (vacuity FAIL), never silent.
- Tooling: no installs/upgrades performed (none needed; pacman paused). `strings`/`file`/`sha256sum` from existing coreutils/binutils.
- Scratch `/fast/scratch/hyaku/kotoba-r82/Kb82E01Paths/` deleted on exit; all receipts copied under build/.

VERDICT: PASS — ELF magic/version/sha independently verified (18.14.0, e7dd2b60…); unchanged extractor derives all 8 loader pairs on the live dump (new callees ts/Ac); path-only 4-file patch prepared; all four touched gates' selftests green (62+218+10+123 assertions, 0 failures); no expected-value, census, baseline, ledger, or counter mutation.

DELIVERABLES:
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E01Paths-c1-paths.patch
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E01Paths-loader-pairs-18.14.0.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/pins-patched-default.json
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/selftest-check_substrate_pins.log
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/selftest-verify_surfaces.log
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/selftest-verify_harness_claims.log
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/selftest-verify_harness_independent.log
