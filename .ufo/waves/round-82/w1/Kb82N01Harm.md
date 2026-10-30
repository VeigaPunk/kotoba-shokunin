# Kb82N01Harm — sentinel no-harm surface hunt (round 82, w1)

Lane: /home/vgpnk/Projects/shokunin/kotoba-shokunin. HEAD 006a834cee4339ede8620e10c3995d5226141c0a (freeze commit); base 47dbe8781657de563ff867caca6244d28e3db504. Host measured 2026-10-30T15:18:53Z. Read-only: no lane, ~/.local/bin, or fleet file was modified. Receipts: `build/Kb82N01Harm-sweep.txt`, `build/Kb82N01Harm-host.txt`.

## Host state (C1 input)

| item | value |
|---|---|
| `~/.local/bin/omp.real` | absent (`test -e` exit 1) |
| `~/.local/bin/omp` | ELF, 276,244,656 B, sha256 `e7dd2b606c4ebe9d1a7bcfad1b8820db968cd6b05409fed1c6bc8db0b6a95a8f`, mtime_ns `1793326786168359786` = `2026-10-29T23:19:46.168359786-03:00` (exact), `omp/18.14.0` |
| `~/.opencode/bin/opencode` | sha256 `ca9b3ee2…d2e7` = `baseline.json` opencode pin (holds) |
| `OMP_REAL` env | unset; no lane reader of it |

Pinned omp values at HEAD (`verifiers/baseline.json` measured_against): sha `85d9daf3…` and mtime `2026-10-21T20:37:24.615549837-03:00`, both belonging to the now-absent `omp.real`. They must move with the path.

## 1. Default-path callsites (active code)

The omp path is held by **four independent literals, one per file**. There is no shared constant:

| file:line | constant | base value |
|---|---|---|
| verifiers/check_substrate_pins.py:68 | `BINARIES["omp"]` (argparse :311 derives) | `~/.local/bin/omp.real` |
| verifiers/verify_surfaces.py:169 | `DEFAULT_BINARIES["omp"]` (argparse :2432 derives) | `~/.local/bin/omp.real` |
| verifiers/verify_harness_claims.py:53 | `OMP_BIN` (argparse :629 derives) | `~/.local/bin/omp.real` |
| verifiers/verify_harness_independent.py:124 | `DEFAULT_OMP_BINARY` (argparse :1716 derives) | `~/.local/bin/omp.real` |

- Inside each file the default derives from one constant: no second literal there.
- Across files there is one literal per file, so a partial move is possible. The round-72 history shows this exact risk ("Default paths moved … together"). Any move must touch all four in one change.
- `verifiers/check_substrate_repin_v2.py` has no omp literal. Its P and S conjuncts run `check_substrate_pins.py` and `verify_surfaces.py` with no path flags, so they inherit whatever the tree's defaults are. Its only hard-coded host path is `HOST_OPENCODE` (:127), which is correct.
- `verifiers/compare_harness_independent.py` was not re-read in this seat. The round-72 scout record says it has no binary path default.
- Base status: all four resolve to the absent `omp.real`. This matches `receipts/before-pins.txt` (exit 2) and `before-c1-counter.txt`.
- HEAD vs base: `git diff --name-only 47dbe878..HEAD -- verifiers corpus SKILL.md PROVINCE.md` is empty. The four literals are unchanged since base.

**Candidate move (other seat's artifact, read only, not applied):** `build/Kb82E01Paths-c1-paths.patch` changes exactly those four literals to `~/.local/bin/omp` and rewrites the adjacent comments. After it is applied, the count of executable `omp.real` literals is **0**. The patch alone does not clean up the docstring items in §2.

## 2. Stale present-tense text (not default sources)

1. **verifiers/check_substrate_repin_v2.py:12–15 (docstring).** Says "path move onto `~/.local/bin/omp.real`". After C1 this is false. The E01 patch does not touch it. Editing it changes the frozen counter's bytes (sha `629487a1…`), so the plan's SHA-checked gate-blob rule applies. The predicate reads no path, so behaviour is unaffected. **L1 decision:** edit under the counter's blob freeze, or leave and record it as a named docstring-only residual.
2. **verifiers/verify_harness_claims.py:14–19 (docstring).** The omp line is correct for `~/.local/bin/omp`. The opencode line still names the npm `opencode-ai` npx-cache `.../opencode.exe` path, which is the round-47 lineage. The line is labelled historical but is in the present-tense header. Doc-only.
3. **PROVINCE.md:30 (Core).** "omp.real and opencode v2.1.4 re-derived and re-pinned (round 72)." This is a dated round-72 claim inside protected Core. Core is no-harm-guarded, so the decision belongs to L1. A round-82 re-pin needs a dated note or an append, not an in-place rewrite of the round-72 claim.
4. **SKILL.md:560.** "`~/.local/bin/omp` embedded JS." This is **true again** for the 18.14.0 ELF at that path. No edit needed.
5. **corpus/knowledge/claude-md-surface.md:8–11.** Undated counts against `~/.local/bin/omp` (17 CLAUDE.md, 37 AGENTS.md). Pre-existing, not a default source. The binary has changed several times since.
6. **corpus/knowledge/skill-activation-telemetry.md:18.** ELF offset `283082932` is already dead on every binary measured since round 21. Pre-existing.
7. **verifiers/check_report_pointers.py:80, 658, 772.** `omp.real` appears as a dotted non-pointer fixture token. It is not a path and needs no action.

## 3. Historical records (append-only, keep)

- `verifiers/baseline.json` `omp_round51_note`, `omp_round72_note`, and the opencode round-53/72 notes.
- `LOG.md:2777` (round 72), `SCORECARD.md:32` (round 51), `plans/round-51.md:12–80`, `plans/round-72.md:33–46, 111–138`.
- `corpus/lessons/round-72-verifier-spotcheck.md:67–71`; `corpus/knowledge/instruction-surface-census-round13.md` (dated).
- `.ufo/waves/round-21..76` receipts and round-82 build receipts. Together these hold the before-state evidence.

## 4. Hidden second default source check

- `OMP_REAL` env: 0 lane readers (the wrapper that honoured it is gone).
- `shutil.which("omp")`: not used by any omp-facing verifier.
- `~/.local/bin/opencode` shim (round-21 record, sha `b240efa9…`): not referenced by any default. opencode defaults correctly use `~/.opencode/bin/opencode`.
- Fleet `scripts/`, `tools/`, `m-rev-vs-rev.py`: 0 hits for `omp.real` or `local/bin/omp`.
- Lane-wide sweep excluding `.ufo` and `.git`: 24 files. Executable hits are the four in §1. The rest are docs and records in §2–§3.

**Result: no hidden second default source.** The only source risk is the four-literal split in §1, and it is closed only if all four move together.

## 5. Recommendations (report, not implemented)

1. Apply the four-literal move as one change (E01 covers it). Re-pin `baseline.json` `omp_binary_sha256` to `e7dd2b60…` and `omp_binary_mtime` to `2026-10-29T23:19:46.168359786-03:00` (ns `1793326786168359786`). Keep the round-72 notes as they are.
2. After the move, re-run the existing sweep and confirm 0 executable `omp.real` literals. That check is cheap and should be run by L1 once.
3. Decide the §2 items 1 and 3 explicitly. Do not silently widen the change to docstrings.

## 6. Limits and evidence gaps

- `omp --version` was run once without its exit code captured. The version string is `omp/18.14.0`.
- `compare_harness_independent.py` was not re-read.
- I did not run any verifier. The before-state receipts are the existing `.ufo/waves/round-82/receipts/*` files and other seats' builds, which I read but did not re-execute.
- No edits, commits, or pushes. The only files I wrote are this report and the two build receipts.
- Installs or upgrades: none by this seat.

VERDICT: no hidden second omp default source found; four per-file omp.real literals remain at HEAD (base-identical), all absent on host; a four-file move is required for C1 with the frozen counter docstring and PROVINCE Core text left as explicit L1 decisions.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82N01Harm.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82N01Harm-sweep.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82N01Harm-host.txt
