# ScribeEntry — scoped findings (round-88 w1)

Seat: ScribeEntry (scribe, leaf). Owned output: `corpus/knowledge/omp-root-semantics-round88.md` (new, untracked; not committed).
Detail: `.ufo/waves/round-88/w1/ScribeEntry/summary.md`.

## Status

- Knowledge entry written: 150 lines, body 147 (budget 160). Provenance trio present (`source:` S257 + ELF sha256; `verified-at:` 4df1e80 + date; `recheck:` both v2 commands). No `[x]`.
- **C1 is not admitted.** The v2 root counter gave no verdict on my run (counter sha `506a2ba9…`: `UnboundLocalError`); the file was then edited to sha `892404e3…`, which does not parse (`SyntaxError`, line 984). Forged-world record stays at round 87: 0 of 4 rejected.
- **C2** reads `closed 5 of 5` at the tip; its self-test is `1 failure(s) over 16 assertions` (disclosed, lead ruling F1).
- Handoffs: `SOURCE_READY`, `ELF_MAP_READY`, `C2_READY` present. `C1_READY` and `FORGERY_READY` absent (45-minute window: 22 polls x 120 s, `bg_3342`; I did not wait further). `ExecForgeryWorlds` later wrote `matrix.tsv` (before column measured, after column `NOT_RUN`); `ExecLiveBound` has no report file in w1.

## Evidence (commands and observed lines)

1. `python3 -B verifiers/check_omp_root_semantics_v2.py --rev 4df1e8005016c75390a5e06b209462df58c95918` (counter sha `506a2ba9…`) → `binding sets frozen sha256 PENDING_FREEZE`; guards S2, S5 PASS; `row 1 FAIL '{cwd}/.omp/skills': binary_quote not located in the omp ELF` (rows 2–12 identical); then `UnboundLocalError: cannot access local variable 'last_absent'`, `exit=1`.
2. Same counter `--self-test` → same `UnboundLocalError` (lines 914 and 335).
3. Independent `mmap` find of all 12 ledger `binary_quote`s in the ELF → all present (rows 1–8, 10–12: 2 occurrences; row 9: 1). The counter's conjunct 5 reports them absent: a counter defect.
4. `grep -n "PENDING" verifiers/check_omp_root_semantics_v2.py` → line 186 `BINDING_BLOCK_SHA256 = "PENDING"`: binding sets not frozen.
5. `python3 -B -c "import ast; ast.parse(open('verifiers/check_omp_root_semantics_v2.py').read())"` on sha `892404e3…` → `SyntaxError: unmatched ')'` (matches ExecForgeryWorlds' line 984 report).
6. `python3 -B verifiers/check_r86_routed_repairs_v2.py --rev 4df1e80…` → `PASS d5 …` and `r86 routed defects closed 5 of 5`.
7. `ExecMonotoneD5/receipts.txt` line 8 → `1 failure(s) over 16 assertions` (arm `w_added_red`).
8. `sha256sum /home/vgpnk/.local/bin/omp` → `6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f`.
9. `sha256sum ELF_MAP.tsv` = `ELF_MAP_READY` content `21e3c518…4897`.
10. `grep -n "of 12\|exit" .ufo/waves/round-87/w3/CriticSemanticsR87/forgery-worlds.txt` → `grounded 12 of 12` / `exit=0` on the four worlds (lines 15, 31, 47, 63): before M = 0. `ExecForgeryWorlds/receipts.txt` § 2 reproduces it, including the honest tip.
11. Cross-check (ReviewerC1, not the frozen counter, `receipts/indep_C1_worlds_A14.txt`): `grounded 10, 10, 9, 9 of 12`.
12. `sha256sum verifiers/check_omp_root_semantics.py` = `6e826f3bf8d4585340ddcc9b7a546e4b7d8b9774a2794c4f45b3cf13e7798922` (matches the plan's pin). Other frozen files hashed; no pin recorded in the plan to compare against; this seat did not edit them.
13. Census before the entry: `bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → `E11 S257 missing used-by corpus/knowledge/omp-root-semantics-round88.md`, 33 `W04`, exit 1. After: 0 `E`, 33 `W04`, exit 0.
14. `git show 4df1e80:verifiers/omp-skill-roots-semantics.tsv | wc -l` → 13 (header + 12 rows).

## Findings

- **F1 (blocking, C1).** `check_omp_root_semantics_v2.py` raises `UnboundLocalError` (`last_absent`, `reader_grounded`, line 335) at sha `506a2ba9…`, and at sha `892404e3…` it does not parse. No N or M is printed. Sentinel F1 agrees.
- **F2 (blocking, C1).** `binary_grounded` (line 681) reports every honest row's binary quote absent; an independent mmap find says all 12 are present. Result: blanket refusal. The positive control fails; M == 4 cannot be credited.
- **F3 (blocking, C1).** Binding token sets unfrozen (`PENDING`). The plan's kill rule applies to any revision after the first score.
- **F4 (C1 record).** `matrix.tsv` exists: before column measured (0 of 4 rejected); after column `NOT_RUN` on every row. `FORGERY_READY` never written.
- **F5 (C2, disclosed).** v2 gate self-test fails `w_added_red` (1 of 16): the monotone test counts names, so new instances of an already-red name pass. `C2_READY` was written over that red by lead ruling.
- **F6 (C2).** `report_dead` reads DRIFT in scratch clones (dangling symlink to the fleet root), not at the lane tip. Recorded, not repaired.
- **F7 (registry).** `verifiers/floors-registry.json` has no `omp_root_semantics_v2` row (`grep omp_root … → empty` at 4df1e80).
- **F8 (upstream, sound).** S257 bound verified in ScoutUpstream receipts (line 149 quote, blob `2e41428b…`, tag commit `3fedf8d5…`); ELF counterpart offsets re-found by me (173865771, 173865668, 173864226).

## Risks

- The entry's §1 result block is from counter sha `506a2ba9…`; the current file (`892404e3…`) does not parse. The entry says so; a future revision must re-measure.
- Census exit 0 is sequencing (the entry exists at its `used-by` path), not a verdict.
- The 6 unledgered joins come from the scout's map; no upstream open covers them.

## Not done

- No edit to the v2 counters, gates, ledger, floors row, plan, SOURCES, README, QUALITY, LOG, SCORECARD or SKILL (not owned).
- Nothing committed (git writes forbidden to this seat).
- The C1 after column: not measurable until the v2 counter parses and runs.

## Tooling

No tool installed or upgraded. Used: `python3` (stdlib `mmap`, `re`, `ast`, `subprocess`), `sha256sum`, `grep`, read-only `git show`, the lane's `sources-census.sh validate`. PACMAN not touched.
