# Critic: frozen-predicate shortcut worlds

Axes attacked: C1 depth; C2 freshness. Base: `1c8f37edf2e5ac0fb3c2be1c88e32406313fe47b`; specification: `f822dd113fe9f58661dd642dc207669581a4ab57:plans/round-85.md` and claims.json. No production files edited; no git writes; no tools installed.

## Construction and commands

Scratch root S was `/fast/scratch/hyaku/kotoba-r85/Critic`. W0 was extracted with:

```
mkdir -p "$S/W0"
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin archive 1c8f37edf2e5ac0fb3c2be1c88e32406313fe47b | tar -x -C "$S/W0"
```

W1–W7 were separate copies of W0, modified by the retained `build_worlds.py`. Candidate description matches the plan's complete payload, 876 parsed characters. Exact payload artifacts are retained under `fixtures/`. World numbers below follow this seat's assignment, NOT the different W1/W2 control definitions in the plan.

For every world W, cwd was `$S/W`, TMPDIR was `$S`, and these three commands ran:

```
python3 -B "$S/c1_oracle.py" --repo "$S/W"
python3 -B "$S/W/verifiers/check_substrate_pins.py" --repo "$S/W"
python3 -B "$S/W/verifiers/verify_surfaces.py" --repo "$S/W" --json
```

Every exact argv, cwd, stdout, stderr and exit is retained in `Wn-c1.json`, `Wn-pins.json`, `Wn-surfaces.json`; aggregate: `results.json`. No `--omp-binary` override or strings-dump bypass was used.

The production C1 counter did not exist when the worlds were constructed. `c1_oracle.py` independently implements the eight frozen labels. R5 invokes the base-tree sibling guard with the round-74 census, `--province PROVINCE.md --skill SKILL.md`. R6 extracts quoted declared trigger phrases and uses case-insensitive substring membership; near-miss words are lowercased ASCII alphanumeric tokens of length >=4. R8 requires S213, date, recheck, nonempty locator and a 1–25-word quote. These are oracle interpretations, not authority over the production counter. Base reproduces the expected 4/8. The oracle includes the terminal period in R1's first sentence (151 base characters versus the plan's 150); the threshold outcome is unchanged.

## Observed world table

Cells give score/output and exit code. All rows ran all three commands above.

| World | Delta from W0 | C1 score; exit | Pins; exit | Surfaces pass/fail; exit | C2 conjunction |
|---|---|---|---|---|---|
| W0 | none | 4/8; 1 | UNREADABLE 2/3; 2 | 0/0 + missing omp.real error; 2 | false |
| W1 | candidate description only | 6/8; 1 | UNREADABLE 2/3; 2 | 0/0 + missing omp.real error; 2 | false |
| W2 | candidate description + token-dump eval | 6/8; 1 | UNREADABLE 2/3; 2 | 0/0 + missing omp.real error; 2 | false |
| W3 | conforming eval + entry; base description | 6/8; 1 | UNREADABLE 2/3; 2 | 0/0 + missing omp.real error; 2 | false |
| W4 | four omp path constants only | 4/8; 1 | DRIFT 2/3; 1 | 7/0; 0 | false |
| W5 | candidate omp pin values only | 4/8; 1 | UNREADABLE 2/3; 2 | 0/0 + missing omp.real error; 2 | false |
| W6 (additional witness) | two predicate-relevant constants + candidate pin values | 4/8; 1 | OK 3/3 pins hold; 0 | 7/0; 0 | true |
| W7 (additional witness) | candidate description + conforming eval + entry | 8/8; 0 | UNREADABLE 2/3; 2 | 0/0 + missing omp.real error; 2 | false |

W0/W4/W5 missing R1,R4,R6,R8. W1/W2 missing R6,R8. W2's token-dump eval has 8 positives and 8 negatives but zero indirect positives. W3 is missing R1,R4. W7's conforming eval has six indirect positives and eight shared-word negatives. W3/W7 entries are synthetic fixtures, not evidence of a live source reopening: their quote and location come from existing S213 registry evidence.

Pins failures name `omp_binary_sha256, omp_binary_mtime`. W4 reads the new ELF but compares old values; W5 records new values but still reads missing omp.real. W4/W6 surfaces independently report 42-id inventory parity and all eight extracted loader classes declared.

## Required answers

(a) None of the six required shortcut worlds reaches C1 8/8 under the independent frozen-plan oracle. Description-only and token-dump worlds stop at 6/8; omitting the description rewrite also stops at 6/8.

(b) Neither W4 nor W5 reaches C2. W4 surfaces succeeds but pins exits 1; W5 both tools exit 2.

(c) Cheapest observed successful combinations: W7 for C1 (description + shape-conforming eval + sourced-entry structure), and W6 for C2 (the two constants read by the predicate + two omp pin values). W7 contains all three claimed artifact types, but does NOT establish behavioral trigger quality or live source verification. W6 contains the claimed host re-point/re-pin work and genuine extraction, but omits two of the four owned path-constant migrations.

## Strongest counterexample, risk, smallest safe correction

**C2 coverage gap:** W6 reaches the exact C2 target while leaving `verify_harness_claims.py` OMP_BIN and `verify_harness_independent.py` DEFAULT_OMP_BINARY pointing at absent omp.real. The frozen conjunction does not observe those callers. Impact: freshness/integration consistency; the target is not proof of four-caller migration. Smallest safe correction: keep the frozen predicates unchanged, complete all four owned constant migrations, and explicitly inspect the two unmeasured constants before integration. This is a fixable scope/coverage gap, not a request to change claim authority or reject the valid observed conjunction.

**C1 provenance/behavior limitation:** W7 reaches 8/8 using a fixture entry with an asserted date and a registry-derived quote, without reopening S213; its negative queries satisfy lexical overlap without demonstrating routing behavior. R6/R8 freeze structural checks, not a model evaluation or source-fetch verifier. Smallest safe correction: restrict reporting to render/eval-set shape and bind the real entry to the source seat's live receipt; do not call this a behavioral trigger-rate improvement. Do not add ninth rules or silently strengthen R8 after measurement.

The production C1 counter remains an integration prerequisite: these receipts use the explicitly permitted independent oracle and are not a production-counter `--rev` result. No judgment/admission decision is made here.

## Self-review

Accuracy 4/5: raw receipts support all observed scores; R8 syntax and period counting are disclosed oracle interpretations. Completeness 4/5: all six required and two witness worlds ran, but production-counter parity is not measured because the counter was unavailable. Clarity 4/5: table separates axis results from provenance limitations. Actionability 4/5: exact receipts and fixture bytes retained; integrate four constants and compare the production oracle. Conciseness 4/5: extra witness rows are necessary to ground the cheapest-world answers. Overall 4.0/5. Highest-value improvement is production-counter comparison by the integrator, without changing the frozen labels. Would the user agree: likely, provided independent-oracle limits remain explicit.
