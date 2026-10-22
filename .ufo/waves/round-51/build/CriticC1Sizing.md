# CriticC1Sizing — attack on the sizing of claim C1 (freshness), round 51 build

**Result: HOLDS-BOUNDED.** This applies to C1's statement "the gate passes 5 of 7 checks → 7 of 7 against omp 18.12.6". The arithmetic reproduces. But the statement is wider than the counter. Only 2 of the 7 checks read the omp binary. Four cheap paths print `pass 7, exit 0` without a true re-derivation, and the `--json` counter catches none of them. The claim holds only with the extra conditions in § Re-sized statement.

## Findings

F1. **Only 2 of the 7 checks measure omp, so the freshness delta is "0 of 2 → 2 of 2" (Q26).**
- `surfaces.literal_present` and `surfaces.no_uncovered_class` read the omp dump.
- `surfaces.opencode_extract` reads the opencode 1.19.3 binary in the npx cache (sha `179ca421…`), not omp.
- `table_parity`, `literal_parity`, `kind_parity` and `excluded_reason` read only repo files: `surfaces-baseline.json` and the census `## Class inventory`.
- All five already PASS at base, so "7 of 7" adds no freshness evidence beyond the two omp checks.
- The 7 of 7 also depends on the opencode binary still being in the npx cache, which the statement does not name.
- Of the 42 omp loader-kind entries, `literal_present` gives call-shape evidence for only the 8 `loader-group` rows. The other 34 are substring tests on a 48 MB dump (`"AGENTS.md" in dump`).

F2. **Adding the three new callee names alone does not reach 7 of 7. The real change is the `S$` resolution rule.**
- The live 18.12.6 dump registers the 8 pairs through `bq`, `Kl` and `Ho` (11 call shapes, all mapping to the 8 declared pairs).
- `S$` is bound twice: `var S$ = "title";` at dump line 843423, and `var S$ = "claude-md";` at line 895604, three lines before `return bq(u, S$, "CLAUDE.md");` at 895607 inside `// packages/coding-agent/src/discovery/claude-md.ts`.
- `constant_table` drops conflicting names (by design), so mutant m0 (allowlist plus `bq|Kl|Ho` only) stays at `pass 5`, exit 1. It names `omp:<unresolved-var:S$>/CLAUDE.md`.
- So "extraction rule change" (Q09) must mean a stated binding-resolution rule, not only callee names.

F3. **Cheap paths to the after-value. For each: is it caught by the 7-check `--json` counter, and by `--self-test`?**

| Path | Live `--json` | `--self-test` | Caught by |
|---|---|---|---|
| m1: allow any callee + last binding wins | pass 7, exit 0 | exit 1 (7 of 99 fail) | self-test only |
| m2a: allowlist + last binding wins (a guess) | pass 7, exit 0 | exit 0 | nothing |
| m2b: allowlist + hardcoded `table['S$']='claude-md'` | pass 7, exit 0 | exit 0 | nothing |
| m2c: allowlist + nearest preceding binding (the defensible rule) | pass 7, exit 0 | exit 0 | — (honest) |
| m3 + rekind: allow only `Kl|Ho`, re-kind the two `bq` rows to `loader-literal` in baseline and census | pass 7, exit 0, "all 6 extracted", 42 ids | n/a | nothing; ids unchanged |
| m3 + drop: allow only `Kl|Ho`, delete the two `bq` rows from baseline and census | pass 7, exit 0, "all 6 extracted", 40 ids | n/a | nothing |
| unmodified script, `--omp-strings` = live dump + 13 lines of `strings-omp-18.12.5.txt` | pass 7, exit 0, "all 8 extracted" | n/a | nothing |

Notes on the table:
- In the m1 row, the self-test failure comes from the clean fixture's decoy: `clean: exit 0: got 1`, then `new-callees: exit 0: got 1`.
- In the rekind and drop rows, the no-flag counter is reached by editing the lane's `surfaces-baseline.json` and census. I simulated this with `--baseline`/`--inventory` flags pointing at the edited copies.
- The re-kind path beats the round-28 laundering arm because that arm only inspects ids the extractor finds, and with `bq` absent those two are never found.
- In the last row (planted dump), the JSON prints no binary path or sha. Editing `DEFAULT_BINARIES["omp"]` is the same class [INFERENCE, not run].

F4. **A thin 18.12.6 fixture is a fixture-only pass while the live dump fails (this attacks the plan's Q25 arm).**
- The arm "fails with the round-50 allowlist, passes with the new one" is satisfiable by a fixture that leaves out the earlier `var S$ = "title"`.
- On such a fixture (`fx-thin`), m0 exits 0, while m0 on the live binary is `pass 5`, exit 1.
- Three fixture arms separate the honest rule from each guess (exit codes from `--check literal_present --check no_uncovered_class` on `baseline-18.12.5.json`):

| Fixture | m0 allowlist only | m2a last wins | m2b hardcode | m2c nearest preceding |
|---|---|---|---|---|
| fx-thin (no conflict) | 0 | 0 | 0 | 0 |
| fx-conflict-before (`S$="title"` first) | 1 | 0 | 0 | 0 |
| fx-conflict-both (+ later `S$="later"`) | 1 | 1 | 0 | 0 |
| fx-renamed-var (conflict on `T$`) | 1 | 0 | 1 | 0 |

F5. **The provenance clause "against omp 18.12.6 (path, sha256)" is not turned on by the counter (Q26).**
- `verify_surfaces.py --json` prints no binary path, no sha256, and nothing about whether `--omp-strings` was used.
- `check_substrate_pins.py` turns on "the binary at the path has sha `85d9daf3…`". It does not bind the surfaces run to that binary.
- The pins companion is satisfied by any re-pin to whatever is installed. It proves currency, not that the extraction was re-derived.

F6. **Unmeasured stale evidence.**
- Census rows 73–74 still cite `jDe(e,Pqr,"AGENTS.md")` / `Pqr = "agents-md"` (the 2026-09-28 generation) in the fifth cell.
- No check reads cells 4–5, so 7 of 7 passes with stale evidence text.
- The Q09 record (version, sha, mtime, rule change) is a documentation requirement that the counter does not verify. Score it separately, not as counter evidence.

F7. **The before-values reproduce (Q19).**
- `{'exit_code': 1, 'fail': 2, 'pass': 5}` with the same two FAIL ids.
- Pins: `DRIFT 2/3 pins failed: omp_binary_sha256, omp_binary_mtime`, exit 1.
- `omp --version` gives `omp/18.12.6`. sha256 `85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4`, mtime `2026-10-21 20:37:24.615549837 -0300`.

## Re-sized statement (the smallest safe correction; no new claim)

> C1: on `/home/vgpnk/.local/bin/omp` 18.12.6 (sha256 `85d9daf3…`, shown by `check_substrate_pins.py` `OK 3/3` in the same session), the two omp-dump checks of `verify_surfaces.py` go 0 of 2 → 2 of 2. The whole gate goes 5 of 7 → 7 of 7, exit 0. This is with opencode 1.19.3 (sha `179ca421…`) unchanged.

The claim must also state these conditions, each checkable by command or diff:
1. The command is exactly `python3 -B verifiers/verify_surfaces.py --json`, with no `--omp-strings`, `--omp-binary`, `--baseline`, `--inventory` or `--repo`. The diff leaves `DEFAULT_BINARIES` unchanged. (Closes the planted-dump path.)
2. The detail strings read `all 8 extracted loader class(es) declared` and `42 loader-kind entries verified against the dumps`. The `class_id`, `context_kind`, `literal` and `verdict` of every `surfaces-baseline.json` entry, and cells 1–3 of the census Class inventory rows, are byte-unchanged from `43ca0bfb`. Counting ids is not enough: the re-kind path keeps 42 ids. (Closes the drop and re-kind paths.)
3. The omp allowlist grows by exactly `bq|Kl|Ho`. No wildcard callee. `CALL_RE` for opencode is unchanged. (Closes m1.)
4. The resolver is a stated rule that reads only the dump: never the baseline, and no per-identifier table. `--self-test` exits 0 and carries the three arms fx-conflict-before, fx-conflict-both and fx-renamed-var. They must use the real `var S$ = "title"` prior binding, and they fail under m0, m2a and m2b respectively. (Closes m2a, m2b and the F4 thin fixture.) The m2c rule (nearest preceding binding) passes all three plus the live dump. It is one admissible rule, not a prescription.
5. The census evidence cells for the 8 loader-group rows cite the 18.12.6 shapes with dump lines (for example `bq(u, S$, "CLAUDE.md")` at 895607, `S$` at 895604). This is recorded as Q09 documentation, not counted by the gate.
6. Optional code hardening, the smallest change: `emit_json` adds the dumped omp path and sha256, or `"omp_strings_override": true`. Then the provenance clause is turned on by the counter itself (Q26).

## Evidence (commands run in `/fast/scratch/hyaku/kotoba-r51/build/CriticC1Sizing/`, clone at `43ca0bfb`)

- Clone and checkout:
  - `git clone -q … lane && git -C lane checkout -q 43ca0bfb… && git -C lane rev-parse HEAD` → `43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10`, exit 0.
- Base counter:
  - `python3 -B verifiers/verify_surfaces.py --json` → `pass 5`, `fail 2`, `exit_code 1`; shell exit 1.
  - The FAILs are `literal_present` ("8 loader literal(s) not verifiable") and `no_uncovered_class` ("vacuity: 0 loader class(es) extracted…").
- Base companion and self-test:
  - `python3 -B verifiers/check_substrate_pins.py` → `DRIFT 2/3 pins failed: omp_binary_sha256, omp_binary_mtime`, exit 1.
  - `python3 -B verifiers/verify_surfaces.py --self-test` → `0 failure(s) over 99 assertions`, exit 0.
- Binary identity:
  - `sha256sum /home/vgpnk/.local/bin/omp` → `85d9daf3…07ccfa4`.
  - `omp --version` → `omp/18.12.6`.
- Live dump census:
  - `strings -n 4 omp > omp-18.12.6.strings` gives 48148449 bytes, sha256 `953b19df…d96f`.
  - The any-callee census regex (callee length 1–4) → `Counter({'Kl': 5, 'Ho': 4, 'bq': 2})`, 11 shapes mapping to the 8 declared pairs.
  - `constant_table`: `v$='agents-md'`, `S$=None`; `S$` bindings `{'title','claude-md'}` at lines 843423 and 895604.
  - Alias `q=Kl` at line 1747113 is binary noise with no call shape.
- Mutants:
  - Run with `python3 -B mutants.py` (generator in scratch, sha256 `f39aed00…e4`, mutant files `lane/verifiers/_m*.py` in the clone only), exit 0.
  - Each mutant's live and self-test results are as tabled in F3. m0 live is `exit=1 pass=5`; m3 live alone is `exit=1 pass=6`.
- Re-kind and drop variants:
  - `_m3_allow_Kl_Ho_only.py --json --baseline baseline-{rekind2,drop2}.json --inventory inventory-{rekind2,drop2}.md` → exit 0, pass 7 for both (detail as in F3).
- Planted dump:
  - Unmodified script, `--json --omp-strings omp-18.12.6-plus-18.12.5-fixture.strings` → exit 0, pass 7.
- Fixture discrimination:
  - Exit codes as tabled in F4. A first fx-renamed-var attempt was a no-op substitution (the `S$` text was unchanged). It was regenerated with Python and rerun; only the rerun values are reported.

No lane files were written except this report. No patch was produced (critic seat). The `skill://godspeed` file was not found on this host (`find / -xdev -type d -iname godspeed` printed nothing). Tooling: no installs or updates.
