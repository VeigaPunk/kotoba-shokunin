# FixtureFaithful: round-51 falsify of verifiers/fixtures/surfaces/strings-omp-18.12.6.txt

Verdict: FAILS (narrow). Three unlabelled fixture lines (lines 9, 15, 33) are not dump bytes, so the claim that every unlabelled line comes verbatim from the 18.12.6 dump is false. The S$ order holds, the 30 dump-backed lines are verbatim, and no extraction result changes.

Scope: fixture honesty, judged on freshness and calibration. Lane HEAD is 59903b2637689739a5b9901956301da72d0effe1. The fixture was last changed in commit e032030 (C1). Its working-copy sha equals its HEAD sha (53aef789…). The binary pin holds: sha256 of /home/vgpnk/.local/bin/omp is 85d9daf3…ccfa4. Tools installed or upgraded: none.

## Findings

### 1. MEDIUM. Three unlabelled lines are not dump bytes (provenance claim)
- Lines 9 and 15 are `}`. `strings -n 4` cannot emit them: the dump's shortest line is 4 characters, there are 0 lines shorter than 4, and 0 exact `}` lines (Python over omp-strings.txt, exit 0).
- Line 33 is `// packages/coding-agent/src/session/session-summary.ts`. The substring `session-summary` occurs 0 times in 2,444,467 dump lines (Python, exit 0). The fixture labels only the block below it (line 34), not this line.
- No gate catches this. The self-test takes fixtures as inputs and never checks them against a dump. A regex search of the clone's verifiers/ for verbatim, provenance, byte substring, and exact dump found no fixture-to-dump check.
- Sibling fixtures state their provenance. The strings-opencode-*.txt headers say every non-comment line is an exact byte substring of a named dump at a named line, with synthetic exceptions listed. baseline-18.12.5.json has a $comment naming its dump. The 18.12.6 fixture has no header and no dump line numbers.

### 2. LOW. Omissions are not marked (excerpt presented as a block)
- All 30 dump-backed lines embed in dump order (greedy in-order embedding, out-of-order list empty), and each sits under its own module marker (30 of 30 match).
- But 14 of the 27 fixture-adjacent pairs of dump-backed lines are not adjacent in the dump, and the fixture marks no omissions. Examples: line 3 to line 4 jumps from dump line 843424 to 895592; line 16 to line 17 jumps from 899267 to 899323.
- The file reads as a contiguous block. It is an in-order excerpt.

### 3. PASS (calibration). The decoy does what its comment says
- Probes in a private clone, monkeypatching constant_table and scope_table, fixture text only:
  - current module-scope rule: ('claude-md', 'CLAUDE.md')
  - dump-wide last-wins: ('later', 'CLAUDE.md')
  - dump-wide first-wins: ('title', 'CLAUDE.md')
  - dump-wide conflict-drop: ('<unresolved-var:S$>', 'CLAUDE.md')
- Self-test block (b2h), verify_surfaces.py:1097-1118, already covers the dump-wide alternatives on an inline three-module example. Reading its assertions (not executed) shows they reject first-wins and last-wins. So the decoy is a second, fixture-level check.
- [INFERENCE] Without line 36, the last S$ binding is line 11 (claude-md), so a last-wins regression would still pass the fixture. This follows from the same probe logic and was not run separately.
- Dropping line 11 turns the claude-md row into ('<unresolved-var:S$>', 'CLAUDE.md'), so the rule is not vacuous.

### 4. RESIDUAL (INFERENCE). The module-scope premise is not provable from this dump
- The rule treats each `// <path>` marker as a new JS scope. The dump has 0 `__esm(` wrappers, module bodies are not indented, and `strings -n 4` drops every line that is only `}`. So the dump cannot show that the two column-0 `var S$` declarations (dump lines 843423 and 895604) sit in separate scopes.
- If they share one scope, the runtime value of S$ is the last top-level assignment, which in dump order is "claude-md". The live answer is unchanged either way.
- But the decoy's expected answer ("claude-md" over "later") holds only under the module-scope reading. A top-level `var S$ = "later"` in one shared scope would make the runtime value "later". The decoy's calibration rests on an unproven premise.

### 5. PASS (freshness)
- Full dump (2,444,467 lines) through extract_classes(…, "omp"): 8 pairs. Fixture: 8 pairs. Fixture pairs missing from the live dump: 0. Live pairs missing from the fixture: 0. Live `<unresolved-var:…>` rows: 0.
- The string "18.12.6" occurs 9 times in the dump, for example dump line 644426, `var p0 = "18.12.6";` (Python count, exit 0).

## S$ bindings versus the bq call: HOLDS
- Dump order: `var S$ = "title";` at 843423, then `var S$ = "claude-md";` at 895604, then `return bq(u, S$, "CLAUDE.md");` at 895607. This is the only one of the 9 `bq(` lines in the dump that names S$.
- Fixture order: line 2, then line 11, then line 14. Same order. Dump 843423-843424 equals fixture lines 2-3. Dump 895603-895607 equals fixture lines 10-14, verbatim and contiguous.
- Standalone `S$` tokens later in the dump (2145452 `S$=#ue`, 2399954 ` S$=n`) sit inside binary runs. Dump lines 2145446-2145463 and 2399945-2399965 are random-byte lines, not JS bindings.
- The synthetic `later` binding (line 36) sits after the bq call and has no dump counterpart. It is labelled synthetic.

## Synthetic lines: who labels them

| fixture line | text | labelled in fixture | labelled in self-test | in dump | effect on extraction |
|---|---|---|---|---|---|
| 9 | `}` | no | no | cannot be (strings -n 4) | none; dropping it gives the same 8 pairs |
| 15 | `}` | no | no | cannot be | none |
| 33 | session-summary.ts header | no | no | 0 hits | none; dropping it gives the same 8 pairs |
| 34 | comment "synthetic line (not in the live dump)" | yes | no | 0 | none |
| 35 | comment, continues line 34 | yes | no | 0 | none |
| 36 | `var S$ = "later";` | yes, via line 34 | no; self-test calls it "a LATER S$ binding" (verify_surfaces.py:1013-1014) | 0 | decoy; changes the outcome only under dump-wide last-wins |

## Evidence (commands and exit codes; scratch is /fast/scratch/hyaku/kotoba-r51/falsify/FixtureFaithful)
1. `sha256sum /home/vgpnk/.local/bin/omp` gives 85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4. Exit 0.
2. `strings -n 4 /home/vgpnk/.local/bin/omp > omp-strings.txt` gives 2,444,467 lines, 48,148,449 bytes, sha256 953b19dffc4d51bd877330b90f0e994db38e90ee5f80575f08a31f3b73e7d96f. Exit 0.
3. Literal `grep -Fxc -- <line> omp-strings.txt` for all 36 fixture lines, run through a Python subprocess: 30 lines count 1 with exit 0. Lines 9, 15, 33, 34, 35, 36 count 0 with exit 1. A Python set test gives the same split.
4. Fixture: 1467 bytes, 36 lines, LF-terminated, 0 CR, 0 NUL, 0 non-ASCII (Python, exit 0).
5. `git clone -q <lane> <scratch>/lane` then `git -C <scratch>/lane checkout -q 59903b26…`: exit 0. `git show HEAD:verifiers/fixtures/surfaces/strings-omp-18.12.6.txt | sha256sum` gives 53aef789…, equal to the lane working copy. `git log -- <fixture>` lists only e032030.
6. `python3 -B verifiers/verify_surfaces.py --self-test` in the private clone at HEAD: exit 0, "0 failure(s) over 115 assertions".
7. Variant probes with extract_classes on fixture text: dropping line 33 gives the same 8 pairs; dropping lines 9 and 15 gives the same; dropping lines 33-36 gives the same; dropping line 2 leaves claude-md unchanged; dropping line 11 gives ('<unresolved-var:S$>', 'CLAUDE.md').
8. Dump line lengths (Python, exit 0): minimum 4; lines shorter than 4: 0; exact `}` lines: 0.
9. Python, exit 0: `session-summary` hits 0; `bq(` lines 9; `18.12.6` occurrences 9; `__esm(` occurrences 0.

## Recommendations (no edits made)
1. Delete lines 9, 15 and 33, or label them. Add a provenance header with the dump sha (953b19dffc…), the binary sha (85d9daf3…), and "in-order excerpt; omitted lines are not marked", or insert omission markers.
2. Add a gate: every unlabelled fixture line must be an exact line of `strings -n 4` of the pinned binary. Report SKIP, not PASS, when the binary is absent.
3. Settle the module-scope premise (finding 4) by inspecting the bundle's scope in a non-stripped build, or label the decoy's expected value as depending on that premise.

## Residual risk and gaps
- I did not run the C1 `verify_surfaces.py --json` live gate. I ran extract_classes over the full dump instead.
- I did not execute omp. Finding 4 is untested.
- The `strings` version was not recorded (GNU binutils from the system).
- Lane untouched: this report is the only file written. All runs were in scratch. No git write commands, no jj commands, no messages sent.
