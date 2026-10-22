HOLDS-BOUNDED: every C1 number reproduces exactly from private clones with no override flags; the strength of the 7 of 7 is bounded (F1, F3).

# ReplayC1Counter: round 51 falsify, C1 freshness numbers

Scope: C1 counters only (verify_surfaces.py, check_substrate_pins.py, the baseline.json diff, default inputs). HEAD 59903b2637689739a5b9901956301da72d0effe1 against BASE 43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10. Leaf seat, no delegation. Tools installed or updated: none (used git, python3, GNU strings 2.47, omp). Lane writes: this file only. Scratch: /fast/scratch/hyaku/kotoba-r51/falsify/ReplayC1Counter/.

## Binary identity
- 2026-10-22T15:14:30Z: `omp --version` = `omp/18.12.6`; `sha256sum /home/vgpnk/.local/bin/omp` = 85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4.
- Same hash after the BASE and HEAD runs (15:16:06Z), at 15:21:46Z and at 15:22:52Z (last). The binary did not move; the claim is reproducible today.

## Numbers: `python3 -B verifiers/verify_surfaces.py --json`, no override flags
| run | exit | pass | fail | failing checks | stderr bytes |
|---|---|---|---|---|---|
| BASE (clone at 43ca0bfb) | 1 | 5 | 2 | surfaces.literal_present, surfaces.no_uncovered_class | 0 |
| HEAD (clone at 59903b26) | 0 | 7 | 0 | none | 0 |

- HEAD `substrate.omp`: path /home/vgpnk/.local/bin/omp, bytes 256702432, sha256 85d9daf3... (equals the binary hash), mtime 1792625844.6155498, source binary.
- HEAD run repeated: `cmp` of the two outputs, exit 0 (identical).
- The five checks that pass at BASE (opencode_extract, table_parity, literal_parity, kind_parity, excluded_reason) have detail strings identical to HEAD: 5 of 5.
- BASE failure text: literal_present lists 8 omp loader literals with no call shape; no_uncovered_class says "vacuity: 0 loader class(es) extracted from the omp dump while the baseline declares 8".
- C1 commit e032030 alone (own clone, checkout): gate exit 0, pass 7, fail 0. `git merge-base --is-ancestor e032030 59903b26` exit 0. In BASE..HEAD the only commit touching verify_surfaces.py, baseline.json, verifiers/fixtures or surfaces-baseline.json is e032030; `git diff --numstat e032030 59903b26` for those paths prints nothing.

## Pins: `python3 -B verifiers/check_substrate_pins.py`
- BASE: exit 1; `FAIL omp_binary_sha256` (expect fdbc8136..., got 85d9daf3...); `FAIL omp_binary_mtime`; `PASS opencode_binary_sha256`; `DRIFT 2/3 pins failed: omp_binary_sha256, omp_binary_mtime`.
- HEAD and C1 commit: exit 0; `PASS omp_binary_mtime: delta 0 ns (tolerance 0 ns)`; `OK 3/3 pins hold`.

## baseline.json diff
`git -C <clone> --no-pager diff 43ca0bfb... 59903b26... -- verifiers/baseline.json`: one hunk `@@ -2,10 +2,11 @@`; numstat 3 insertions, 2 deletions. All changes sit inside `measured_against`: value of omp_binary_sha256, value of omp_binary_mtime (2026-10-21T03:30:38.135013187-03:00 to 2026-10-21T20:37:24.615549837-03:00), and one new key omp_round51_note. Top-level as_of, host, checks and notes are unchanged (json load of the HEAD file).

## Default inputs of verify_surfaces.py (HEAD source lines)
- verifiers/surfaces-baseline.json (default baseline, main() lines 1419-1420): sha256 6b23c3d1c8766e4effea9f5502b638de7b22cd0d61be20426ba99482c7d1260b in both clones; not in the BASE..HEAD stat.
- corpus/knowledge/instruction-surface-census-round13.md (DEFAULT_INVENTORY, line 162): sha256 6c7958fb6997adb45a1c026fdcec1332feb083a996ee8752356adeb84d760486 in both; not in the stat.
- omp binary through `strings -n 4` (DEFAULT_BINARIES lines 158-159; dump_via_strings lines 264-276).
- opencode binary through `strings -n 4` (lines 160-161): /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe, sha256 179ca421... (equals the pin).
- Fixtures are read only by --self-test. verifiers/baseline.json is read only by check_substrate_pins.py (line 319).
So the baseline check rows and the surfaces inventory are byte-unchanged. The gate code did change: verify_surfaces.py +268 -13.

## Self-test and floors
- `python3 -B verifiers/verify_surfaces.py --self-test`: HEAD exit 0, "0 failure(s) over 115 assertions"; BASE exit 0, "0 failure(s) over 99 assertions".
- `python3 -B verifiers/check_assertion_floors.py` at HEAD: exit 0; 12 of 12 PASS, including surfaces observed=115 floor=115 and overlap_levers observed=22 floor=22.

## Attack A: does the 7 of 7 need the new rule? (scratch copy only)
- Scratch copy of HEAD verifiers with `scope_table` made to return {} (edit tool, scratch file only). Live run: `python3 -B verifiers/verify_surfaces.py --repo <laneH> --json` gives exit 1, pass 5, fail 2. FAIL literal_present names omp:claude-md/CLAUDE.md; FAIL no_uncovered_class names `omp:<unresolved-var:S$>/CLAUDE.md`.
- The same copy's `--self-test`: exit 1, "7 failure(s) over 115 assertions". The self-test does catch the rule's removal.

## Attack B: independent extraction (scratch script `out/extract_omp.py`, exit 0, output in `out/extract_omp.out`; the dump is `strings -n 4` of the binary, `wc -l` 2,444,467 lines, 3,239 source-path comment lines)
- Round-50 callee list: 0 `.md` registration shapes in the 18.12.6 dump.
- Round-51 list (adds Kl, Ho, bq): 11 shapes (bq 2, Kl 5, Ho 4), all between dump lines 895596 and 900706.
- Module-scope resolution: 8 (group, file) pairs, equal to the 8 declared omp loader-group rows; 0 undeclared; 0 unresolved.
- Dump-wide table only: 1 unresolved pair (S$).
- The two var-bound sites: line 895593 `var v$ = "agents-md";`, line 895596 `return bq(u, v$, "AGENTS.md");` inside `async function zBt(u)`; line 895604 `var S$ = "claude-md";` (under marker line 895603, `// .../discovery/claude-md.ts`), line 895607 `return bq(u, S$, "CLAUDE.md");` inside `async function XBt(u)`. Neither enclosing function takes S$ or v$ as a parameter. The module then registers `Le(Tl.id, { id: S$, ...` (lines 895608-895609).
- The other S$ string binding, line 843423 `var S$ = "title";`, sits under `session/session-entries.ts`. Two non-string S$ assignments in the mnemopi module are ignored by both policies.
- Definitions: `function bq(e, t, n)` at line 863364; `function Kl(e, t, n)` at line 863058, followed by `function Ho(e, t, n)`. Each takes (context, group, file) in the same order as the call sites.

## Findings, by severity
F1 (Medium; bounds what "7 of 7" measures). Of the 33 omp loader-kind rows, only the 8 loader-group rows get a registration call-shape test. The other 25 (21 loader-literal, 4 loader-config) pass when their literal occurs anywhere in the strings dump of the 256 MB binary (verify_surfaces.py line 684; rule text at lines 84-97). Each literal occurs many times (str.count in out/extract_omp.out: `rules` 416, `prompts` 491, `skills` 492, `plugins` 562, `commands` 758, `instructions` 434; lowest is `enabledProviders` 3). Round 51 did not change this: no diff hunk touches check_literal_present (lines 675-704). Plain reading: the omp freshness claim rests on 8 strict rows.

F2 (Low; wording). "The two omp checks" are check IDs that cover both harnesses. check_no_uncovered_class loops over HARNESS_IDS (lines 729-733); check_literal_present takes every loader-kind row, 9 of them opencode. Their BASE failure text names omp rows only. The count 0 of 2 to 2 of 2 is right; "omp checks" describes the failing content, not a separate check class.

F3 (Medium; mechanism, not a defect). The 7 of 7 needs the module-scope rule for S$: Attack A shows the gate fails live without it. Attack B shows the rule resolves every call it touches correctly, at the two sites checked in full. The rule depends on `// <path>.ts` marker lines (3,239 found). If a future bundle drops them, the dump becomes one scope and the gate fails closed (documented limit in the module docstring), not silently.

F4 (Low; record). omp_round51_note gives version, sha256 and mtime, as Q09 asks. It does not mention the callee or module-scope change. That change is recorded in verify_surfaces.py (header comment at line 175, docstring) and in plans/round-51.md. Add a pointer in the note if the record should stand alone.

F5 (Nit). baseline.json as_of still reads 2026-10-14T09:58:47.702772-03:00 while the pins moved on 2026-10-22. No reader checks it.

F6 (Nit). Fixture verifiers/fixtures/surfaces/strings-omp-18.12.6.txt: 36 non-empty lines, 32 verbatim in the live dump (Python `line in dump`). The four that are not: `// .../session/session-summary.ts`, two synthetic comment lines, and `var S$ = "later";`. The synthetic comments label the block; the marker line itself is not labelled.

F7 (Info). The pins pass because the pins were re-taken from this binary. Epoch check: 2026-10-21T20:37:24.615549837-03:00 equals 1792625844615549837 ns, the value the BASE pins run printed for the binary. The pin drifts on the next rebuild, by design.

F8 (Info; no-harm for C1). The five unchanged checks give identical details (5 of 5). Floors guard exit 0. Among readers of measured_against, only check_substrate_pins.py reads the pins (grep); the new key does not match its `<substrate>_binary_<kind>` pattern.

## Verdicts on the declared numbers
- pass 5 of 7 to 7 of 7, exit 1 to 0: HOLDS (BASE, HEAD and the C1 commit all reproduce).
- 0 of 2 to 2 of 2 (surfaces.literal_present, surfaces.no_uncovered_class): HOLDS as counts; bounded by F1 and F2.
- Companion pins DRIFT 2/3 to OK 3/3, exit 1 to 0: HOLDS.
- Overall: HOLDS-BOUNDED.

## Residual risk and gaps
- Evidence is static: `strings` output only. Nothing runs omp, so runtime loading is unmeasured (same caveat as the round-51 re-sizing note).
- My extraction and resolution policy are my own code. Module-scope resolution was checked at two full sites plus the set-level result, not at every S$ use in the dump.
- Verified only at binary sha 85d9daf3...; the 18.12.6 rule is tuned to that build.
- Not checked here: the C2 counter, the routed defects, the other no-harm gates, fixture faithfulness beyond the line check (other seats).

## Commands and exit codes (all run from scratch clones or the scratch copy)
- `omp --version; sha256sum /home/vgpnk/.local/bin/omp` (first, 15:14:30Z): exit 0.
- `git clone -q <lane> laneB`, `laneH`, `laneC1`; `git checkout -q` to 43ca0bfb, 59903b26, e032030: exit 0 each.
- `cd laneB && python3 -B verifiers/verify_surfaces.py --json`: exit 1. `cd laneH && ...`: exit 0. Repeat on laneH, `cmp`: exit 0.
- `python3 -B verifiers/check_substrate_pins.py`: BASE exit 1, HEAD exit 0, C1 exit 0.
- `git -C <clone> --no-pager diff 43ca0bfb... 59903b26... -- verifiers/baseline.json`: exit 0; `--numstat` 3 2.
- `sha256sum` of surfaces-baseline.json and the round-13 inventory in both clones: equal pairs (see above).
- `python3 -B verifiers/verify_surfaces.py --self-test`: HEAD exit 0, BASE exit 0.
- `python3 -B verifiers/check_assertion_floors.py` (HEAD): exit 0.
- `python3 -B extract_omp.py > extract_omp.out` (scratch `out/`): exit 0. Prints 11 shapes (bq 2, Kl 5, Ho 4), 8 module-scope pairs, 0 undeclared, 0 declared-but-not-extracted, 1 unresolved under dump-wide-only, 0 zero-count probe rows.
- Attack A: scratch copy live run exit 1; scratch copy `--self-test` exit 1.
- `git merge-base --is-ancestor e032030 59903b26`: exit 0. Gate and pins at e032030: exit 0 and exit 0.
- One lane git attempt (`git --no-pager diff` in the lane) stopped at a shell redirect error before git ran (exit 1). Nothing else touched the lane; all git runs used clones.
- Final `omp --version; sha256sum`: unchanged (see identity).
