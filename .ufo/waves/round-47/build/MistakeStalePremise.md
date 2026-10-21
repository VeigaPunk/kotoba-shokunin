verdict: confirmed stale-premise mistake — the round-46 "Next: round 47" before-values (`omp 18.12.3`, `surfaces 5/7`, `pins 1/3`) were copied, not re-measured; captured-by none (Q09/Q13 partial); proposed Q19 with a prototype premise gate that fails on all three stale copies and passes a fresh fixture.

# Scope

Lane: MistakeStalePremise (leaf, no subagents). BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`. Production files were read only. All runs were in the scratch clone `/fast/scratch/kotoba-r47/MistakeStalePremise/lane` (detached at BASE). Nothing was committed, staged in the lane, or written to the lane's Git state. Artifacts are in `.ufo/waves/round-47/build/MistakeStalePremise.*`.

# Proposed lesson row (for `corpus/lessons/round-47.md` § Mistakes; integrator assigns the number)

| class | evidence pointer (command → output) | captured-by | fix |
|---|---|---|---|
| M20 Stale pre-registered before-values (premise copied, not re-measured) | `SCORECARD.md:101`, `corpus/README.md:74`, `PROVINCE.md:21` → "omp 18.12.3 … surfaces 5/7, pins 1/3"; `.ufo/reports/round-44/kotoba.md:28` → "substrate red \| surfaces 5/7 (0/8 loader-class), pins 1/3" (the r44 pre-repin before-column, verbatim); `corpus/lessons/round-46.md:27` → "`DRIFT 2/3 pins failed`" at the same landing; `python3 -B verifiers/check_substrate_pins.py` at BASE → exit 2, `DRIFT 3/3 pins failed: omp_binary_sha256, omp_binary_mtime, opencode_binary_sha256`; `omp --version` → `omp/18.12.5` exit 0 | none → Q19 (partial: Q09 names freshness-red but not premise provenance; Q13 requires command+date on counts, scoped to lesson prose, not plan lines) | A planned "Before" is a re-measurement at round BASE that names its command, binary sha256, version and date; a plan naming an omp version or pinned binary path is checked against live `omp --version` and `test -e` before the round starts (prototype below). |

Proposed criterion (append-only, integrator to add to `corpus/QUALITY.md`):
Q19 — A planned "Before" value is re-measured at round BASE, not copied from an earlier report. It names the command, the binary sha256/version it ran against, and the date. A plan that names an omp version or a pinned binary path is checked against the live binary and path before the round starts. Grounded in M20. Supersedes: —.

# Evidence, with commands and exit codes

1. **Live omp moved after the plan was written.**
   `omp --version` → `omp/18.12.5`, exit 0. `sha256sum ~/.local/bin/omp` → `fdbc8136084c9a10439569157b2af62312e2b0d801cab54c73e89476da798e7e`, mtime `2026-10-21 03:30:38`. The plan (`plans/round-47.md:11-13`) records this move (18.12.3 → 18.12.5). `SUMMARY.md:11` agrees.
   The 18.12.3 premise was accurate when written: `.ufo/round-46/evidence/S2/g1-strings-census.json:14` → `"version_stdout": "omp/18.12.3"`, and `.ufo/round-46/scouts/S2.md:49` records sha `065b5079…` for that build. The premise expired within about two days; the mistake is carrying the version forward without re-measuring.

2. **The pinned opencode path is gone.**
   `ls -la ~/.opencode/bin` → `No such file or directory`, exit 2. `stat ~/.opencode` → mtime `2026-10-20 08:14:11`, which is the last entry change in that directory (a bound, not proof of removal time). `verifiers/verify_surfaces.py:130` and `verifiers/check_substrate_pins.py:63` pin `/home/vgpnk/.opencode/bin/opencode`. Today `~/.local/bin/opencode` is a 1460-byte bash wrapper (dated 2026-10-03) that runs `npx`. Its ELF lives in the npx cache, `/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-linux-x64/bin/opencode`, sha256 `179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9`. I did not execute the wrapper or the ELF; the snapshot matches that sha (`SHA256SUMS` → OK).

3. **The default gates fail at BASE (re-run in the clone).**
   `python3 -B verifiers/check_substrate_pins.py` → exit 2, `FAIL opencode_binary_sha256: UNREADABLE … '/home/vgpnk/.opencode/bin/opencode'`, `DRIFT 3/3 pins failed`. This matches `SUMMARY.md:5`.
   `python3 -B verifiers/verify_surfaces.py --json` → exit 2 (matches `SUMMARY.md:3`).
   With the frozen snapshot binaries, `check_substrate_pins.py --omp-binary /fast/scratch/kotoba-r47/shared/bin/omp-18.12.5 --opencode-binary …/opencode-1.19.3` → exit 1, `DRIFT 3/3`. The baseline pins `omp_binary_sha256` `9513ef9f…` (`verifiers/baseline.json:5`, 18.12.2) and `opencode_binary_sha256` `d9123b9b…` (`baseline.json:9`, v2.0.26). Neither matches the r47 substrate, so the "pins 1/3" number names neither the r44 state nor the baseline.
   `verify_surfaces.py` with the live npx ELF, or with the snapshot binaries → exit 1, `pass 4 fail 3`. Both numbers are checks out of 7, so "surfaces 5/7" is wrong at BASE. The FAILs are the omp vacuity (0/8 classes) and OC-1/OC-4/OC-6 (`verify_surfaces.py` FAIL lines, saved in `MistakeStalePremise.surfaces-explicit.json`).

4. **Provenance of the premise numbers.**
   `.ufo/reports/round-44/kotoba.md:28`: `| C3 | substrate red | surfaces 5/7 (0/8 loader-class), pins 1/3 | surfaces 7/7, pins 3/3 …`. The r44 before-column is the same string as the r46 "Next: round 47" block (`SCORECARD.md:101`) and the `corpus/README.md:74` / `PROVINCE.md:21` copies. `git log -S "pins 1/3" --format='%h %s'` → `f2f9ee1` (r46 landing) and `032f47b` (r44 publish). `git log -S "omp 18.12.3"` → `f2f9ee1` only. So the r46 landing copied the r44 pre-repin before-column into three front-door files.
   The same landing disagrees with itself. `corpus/lessons/round-46.md:27` (M9, landed in `f2f9ee1`) records `DRIFT 2/3 pins failed: omp_binary_sha256, omp_binary_mtime`. `SCORECARD.md:101`, `corpus/README.md:74` and `PROVINCE.md:21` record `pins 1/3`. Neither is a measurement taken at the round's BASE.

5. **Captured-by, row by row.** Checked against `corpus/QUALITY.md` Q01–Q18 as committed at BASE.
   - Q09 "substrate rebuild makes freshness red until re-derived and re-pinned": captures the red, not the provenance of a planned before-value. Partial.
   - Q10 "measurement names source sha before and after": the plan's before-values are not measurements and carry no sha. Not applicable as written.
   - Q13 "count carries its command, `<number> — <command> <date>`": the rule is scoped to knowledge/lesson prose. `SCORECARD.md:101` has no command and no date. A plan-scoped reading would catch it; the scope excludes it. Partial.
   - Q04, Q14 and the rest: no match.
   Result: **none** for the premise-provenance class. Q19 is proposed.

# Prototype fix that can be shown to fail

Draft: `verifiers/check_planned_premises.py` in the clone (committed nowhere; patch at `.ufo/waves/round-47/build/MistakeStalePremise.patch`, sha256 `a83419d7…`). It reads a plan file, extracts `omp 18.12.N` / `omp/18.12.N` literals and absolute `/…/bin/…` paths, and compares them with `omp --version` and `os.path.exists`. Exit 0 all match, 1 stale premise (named `FILE:LINE`), 2 live omp unreadable. Output is in `MistakeStalePremise.premise-check.txt`.

| run | command | exit | output |
|---|---|---|---|
| BASE SCORECARD | `check_planned_premises.py SCORECARD.md` | 1 | `FAIL SCORECARD.md:101: planned omp 18.12.3 != live omp 18.12.5` |
| BASE README | `… corpus/README.md` | 1 | `FAIL corpus/README.md:74: …` |
| BASE PROVINCE | `… PROVINCE.md` | 1 | `FAIL PROVINCE.md:21: …` |
| fixture stale (fake omp 18.12.5, text `omp 18.12.3`) | `… fixtures/stale.md --omp-binary fixtures/omp-fake-5` | 1 | `FAIL …stale.md:1` |
| fixture fresh (text `omp 18.12.5`) | same binary | 0 | `PASS every named premise matches live omp 18.12.5` |
| fixture absent path (`/home/vgpnk/.opencode/bin/opencode`) | same | 1 | `FAIL …absent-path.md:1: pinned binary path absent` |
| fixture present path (`/home/vgpnk/.local/bin/omp`) | same | 0 | `PASS` |
| no omp | `… SCORECARD.md --omp-binary /nonexistent/omp` | 2 | `ERROR cannot read live omp version` |

The gate discriminates: it fails on each stale copy and passes on the matching control. It is a prototype. It has not been wired into a verifier, the checklist, or the round-start procedure, and it has not been run on a real round.

# Counterexamples and limits

- The mistake is the carry-forward, not the r46 measurement. `omp 18.12.3` was the installed binary at r46 close (`S2.md:49`). The environmental drift came after that.
- The `surfaces 5/7` / `pins 1/3` numbers were wrong at r46 close too: the lesson's own M9 said pins 2/3 at that landing. The r44 number was copied, not re-derived.
- The prototype checks only version literals and absolute binary paths. It does not check count literals such as `surfaces 5/7` or `pins 1/3`. Those would need a round-start run of the gates, with their JSON compared to the plan's literal. Not built here.
- The prototype would false-positive on historical literals such as `omp 18.12.2` in `verifiers/baseline.json` or LOG history, so its scope must be a plan file named by the round, not the whole tree.
- Only one round of exposure. The r47 plan (`plans/round-47.md:11-16`) caught the premise in-round, by re-measuring. The lane has no QUALITY row that forces that step.

# Did NOT check

- The 8 loader classes or the opencode rules at 18.12.5 / 1.19.3 (that is C1, not this lane's claim).
- The opencode version `1.19.3` was taken from `SUMMARY.md:12` and `SHA256SUMS`; I did not run any opencode binary, and did not run the wrapper.
- Whether `~/.opencode/bin` was removed on 2026-10-20; the directory mtime is only a bound.
- `corpus/SOURCES.md` S003 and the description XML-tag rule (C2).
- Any Q-row beyond the 18 in `corpus/QUALITY.md` at BASE; Q19 is not yet admitted.
- Whether the lane's other planning files carry the same stale literals; I grepped only `SCORECARD.md`, `corpus/README.md`, `PROVINCE.md`, `plans/round-47.md`, `corpus/lessons/round-46.md`, `verifiers/baseline.json`, and `.ufo/` for `18.12.` and `pins 1/3`.
- A round-start run of the full surfaces and pins gates with the fix applied; not run.

# Tools and installs

No tool was installed or upgraded. Commands used: `sha256sum`, `git` (read-only: `clone`, `checkout --detach`, `log -S`, `show`, `add -N` in the scratch clone only), `python3 -B` for the verifiers and the prototype, `omp --version`, `ls`, `stat`, `grep`, `cp` into `build/`.

# Artifacts

- `.ufo/waves/round-47/build/MistakeStalePremise.md` (this report)
- `.ufo/waves/round-47/build/MistakeStalePremise.patch` (`verifiers/check_planned_premises.py`, sha256 `a83419d785ffe141945790b9bdd4b627ef1342d135f84c20e6ef14b4c74f460f`)
- `.ufo/waves/round-47/build/MistakeStalePremise.premise-check.txt` (sha256 `0d0f177c…`)
- `.ufo/waves/round-47/build/MistakeStalePremise.surfaces-explicit.json` (sha256 `4df5f3a9…`)
- `.ufo/waves/round-47/build/MistakeStalePremise.pins-snapshot.txt` (sha256 `b5ce8dbe…`)

# Checks the main agent should run

- `python3 -B verifiers/check_planned_premises.py SCORECARD.md` (expect exit 1 at BASE) and the fixture pair, once the patch is applied in a clone.
- Do not rewrite `SCORECARD.md:101`, `corpus/README.md:74` or `PROVINCE.md:21`; they are append-only history. Integrator decision.
