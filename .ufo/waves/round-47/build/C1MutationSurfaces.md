verdict: BASE self-test killed 6/10 extraction mutants (60%); 4 survived, none inconclusive; all ten exact-byte restorations returned the detector to 87/87.

# C1 baseline mutation probe

Lane-authored mutation evidence only; no integration, claim-admission decision, or promotion mark.

- **BASE:** `c61a973b2e02e1ded169703ddcb06466f4edd8bd`.
- **Target:** `verifiers/verify_surfaces.py`, exclusively in `/fast/scratch/kotoba-r47/C1MutationSurfaces/lane`.
- **Axes:** freshness (frozen-BASE reference for the C1 re-derivation), operability (the existing bounded CLI detector actually executes), calibration (survivors remain coverage findings, not passes for the changed behavior).
- **Raw evidence:** `.ufo/waves/round-47/build/C1MutationSurfaces.results.json` — 62,095 bytes, all 30 subprocess stdout/stderr streams and exit codes, per-run before/after hashes, mutation replacements scoped to BASE lines, and verdicts. No binary or strings-dump bytes are copied into the lane.

## Method and commands

Read `plans/round-47.md` first and the before summary. Created the isolated clone with:

```sh
git clone -q --no-hardlinks /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/kotoba-r47/C1MutationSurfaces/lane && git -C /fast/scratch/kotoba-r47/C1MutationSurfaces/lane checkout -q --detach c61a973b2e02e1ded169703ddcb06466f4edd8bd
```

Exit **0**, no output. Production source, index/refs, jj state, sibling scratch trees, logs, and shared substrate snapshots were not modified.

From that scratch clone, the **same detector** was run on pristine, independently mutated, and restored source for every row below:

```sh
python3 -B verifiers/verify_surfaces.py --self-test
```

Each invocation used a 30-second subprocess timeout. Ten pristine + ten mutated + ten restored invocations completed without timeout. Every pristine/restored invocation exited **0**, stdout exactly `0 failure(s) over 87 assertions\n`. Expected stderr from the self-test's negative fixtures named missing `NO-SUCH.txt`, `NO-SUCH.md`, and `NO-SUCH.json`; those diagnostics are retained, not suppressed. The test intentionally asserts these environment-error paths at `verifiers/verify_surfaces.py:956-961,1001-1013`.

```sh
python3 --version
# exit 0: Python 3.14.8
sha256sum verifiers/verify_surfaces.py
# exit 0 before and after each of the 30 detector invocations
```

Applied only one behavior-bearing mutant at a time with a surgical edit; reversed it before the next pristine run. Fixtures, assertions, check IDs, and expected values were unchanged. A reporting-only metadata cell initially had a Python SyntaxError before execution; the corrected cell produced the evidence JSON. That was not a detector run or a source mutation.

## Mutant → caught? → assertion

All source/fixture line references in this report refer to **BASE** above. Each listed assertion is an existing `rec(...)` assertion, not a new test.

| Mutant | Smallest changed point | Caught? / mutated output | Detecting assertion(s) |
|---|---|---|---|
| **M01** | `verifiers/verify_surfaces.py:156`: remove `Id` from OMP callee allowlist | **Killed**, exit **1**; `7 failure(s) over 87 assertions` | `clean: exit 0`, `clean: PASS surfaces.literal_present` at :804-806; additionally extra-class naming/check, rekind naming/control, and `oc-extra: exit 0` (full list below). |
| **M02** | `verifiers/verify_surfaces.py:156`: remove `Mo` from OMP allowlist | **Survived**, exit **0**; `0 failure(s) over 87 assertions` | None. `new-callees: exit 0` / literal-present / uncovered-class assertions at :818-822 remain satisfied. |
| **M03** | `verifiers/verify_surfaces.py:156`: replace allowlist with any JS identifier, `(?:[A-Za-z_$][A-Za-z0-9_$]*)` | **Killed**, exit **1**; `5 failure(s) over 87 assertions` | `clean: PASS surfaces.no_uncovered_class` at :806; clean/new-callees/oc-extra controls also fail. Actual finding: `omp:evil/EVIL.md` undeclared. |
| **M04** | `verifiers/verify_surfaces.py:158`: remove required `\.md` file suffix | **Killed**, exit **1**; `5 failure(s) over 87 assertions` | Same five controls as M03. Actual finding: `omp:cursor/rules->loader-literal`, kind reassignment is not a bypass. |
| **M05** | `verifiers/verify_surfaces.py:567`: `loader_group_declared and not pairs` → `loader_group_declared and pairs` | **Killed**, exit **1**; `7 failure(s) over 87 assertions` | `extract-vacuity: FAIL no_uncovered_class names vacuity` at :828-829 and `blind-dead-dump: vacuity named` at :874; five positive controls also fail. |
| **M06** | `verifiers/verify_surfaces.py:1114`: replace `check_opencode_extract(...)` dispatch with `True, "opencode extraction skipped"` | **Killed**, exit **1**; `21 failure(s) over 87 assertions` | Six OC drop-rule triples at :963-975, `oc-empty-baseline: FAIL opencode_extract` at :987-988, and zero-extraction finding/vacuity assertions at :997-999. |
| **M07** | `verifiers/verify_surfaces.py:413`: OC-1 requires either anchor (`and` → `or`) | **Survived**, exit **0**; `0 failure(s) over 87 assertions` | None; the OC-1 drop fixture removes both anchors together. |
| **M08** | `verifiers/verify_surfaces.py:430-431`: OC-4 requires any of four anchors (all three `and` → `or`) | **Killed**, exit **1**; `3 failure(s) over 87 assertions` | `strings-opencode-drop-oc4.txt: exit 1`, `...: FAIL opencode_extract`, `...: names opencode:read-hook/AGENTS.md`, generated at :972-975. |
| **M09** | `verifiers/verify_surfaces.py:307`: conflicting-rebind comparison `!=` → `==` | **Survived**, exit **0**; `0 failure(s) over 87 assertions` | None. The committed detector does not distinguish this inverted binding-conflict behavior. |
| **M10** | `verifiers/verify_surfaces.py:330`: unresolved-group marker assignment → `continue` | **Survived**, exit **0**; `0 failure(s) over 87 assertions` | None. The detector stays green while unresolved registrations are silently discarded. |

**Measured kill-rate:** `6 / 10 = 60%`, counted from the mutated exit codes in the evidence JSON. No baseline/restoration failure or timeout was counted as a kill. This is a rate for these ten defined mutants, not a percentage of loader completeness.

### Complete failed-assertion names

- **M01 (7):** `clean: exit 0`; `clean: PASS surfaces.literal_present`; `extra-class: FAIL no_uncovered_class`; `extra-class: names omp:foo/FOO.md`; `rekind-doc: names omp:gemini/GEMINI.md->doc`; `rekind-partial: gemini row untouched (no gemini->doc, literal_present green)`; `oc-extra: exit 0`.
- **M03 and M04 (5 each):** `clean: exit 0`; `clean: PASS surfaces.no_uncovered_class`; `new-callees: exit 0`; `new-callees: PASS no_uncovered_class`; `oc-extra: exit 0`.
- **M05 (7):** `clean: exit 0`; `clean: PASS surfaces.no_uncovered_class`; `new-callees: exit 0`; `new-callees: PASS no_uncovered_class`; `extract-vacuity: FAIL no_uncovered_class names vacuity`; `blind-dead-dump: vacuity named`; `oc-extra: exit 0`.
- **M06 (21):** For each `N=1..6`, all three `strings-opencode-drop-ocN.txt: exit 1`, `strings-opencode-drop-ocN.txt: FAIL opencode_extract`, and `strings-opencode-drop-ocN.txt: names <owned-class-or-witness>` fail. In order, the named values are `opencode:project/AGENTS.md`, `opencode:config/AGENTS.md`, `opencode:config/instructions`, `opencode:read-hook/AGENTS.md`, `OC-5`, `opencode:api-entries/instructions`. The remaining three are `oc-empty-baseline: FAIL opencode_extract`; `oc-zero-extraction: FAIL opencode_extract`; `oc-zero-extraction: says vacuity`. The complete verbatim names and captured actual values are also in the JSON.
- **M08 (3):** `strings-opencode-drop-oc4.txt: exit 1`; `strings-opencode-drop-oc4.txt: FAIL opencode_extract`; `strings-opencode-drop-oc4.txt: names opencode:read-hook/AGENTS.md`.

## Counterexamples and calibration limits

The four surviving mutants are **observed counterexamples to treating green BASE self-test as proof of each extraction invariant**. They do not authorize weakening the contract.

1. **Per-callee coverage is not independent (M02).** `verifiers/fixtures/surfaces/strings-omp-newcallees.txt:8-10` registers the same `gemini/GEMINI.md` pair via `Co`, `Gl`, and `Mo`; `extract_classes` deduplicates pairs at `verifiers/verify_surfaces.py:323-331`. Removing `Mo` leaves all 87 assertions green. This does not show `Mo` is obsolete; it shows the positive fixture cannot independently enforce it.
2. **OC-1 conjunction is unprotected (M07).** The anchor conjunction is at `verifiers/verify_surfaces.py:413-415`. `verifiers/fixtures/surfaces/strings-opencode-drop-oc1.txt:1-2,5-13` removes the function and targets anchors together. Replacing the conjunction with disjunction still satisfies the whole existing detector. [INFERENCE, not separately executed] A dump containing only `ConfigInstructionPlugin.projectSource` would distinguish those implementations.
3. **Binding ambiguity is unprotected (M09).** The first-seen/conflicting-rebind contract is explicit at `verifiers/verify_surfaces.py:299-312`, but changing the comparison to equality is not caught. [INFERENCE, not separately executed] `P="gemini"; P="other"; Id(e,P,"GEMINI.md")` would distinguish fail-closed ambiguity handling from the mutant's retained first binding.
4. **Unresolved-group visibility is unprotected (M10).** The declared fail-closed marker contract is at `verifiers/verify_surfaces.py:315-330`. Suppressing the pair entirely survives. [INFERENCE, not separately executed] A valid declared registration plus `Id(e,Unknown,"EXTRA.md")` would distinguish retaining the unresolved pair from silently omitting it without triggering a zero-pairs guard.
5. **OC-4's kill has a fixture-text dependency (M08).** Although its drop fixture says anchors are gone, the comment at `verifiers/fixtures/surfaces/strings-opencode-drop-oc4.txt:2` still literally contains `ReadTool.Plugin`, `targets:[a$]`, and `SessionInstructions.load`; only `a$="AGENTS.md"` is absent. The extractor scans the whole dump, comments included. The OR mutant therefore makes this fixture pass every surface check, causing the three expected-failure assertions to fail. This is an observed kill, but not evidence that every independent OC-4 conjunct is protected.

For a comparable C1 after-measurement, preserve these six detected defect classes and compare mutant identities, not only an aggregate ratio; four existing blind spots are explicitly not claimed fixed here. No candidate C1 implementation was measured by this probe.

## Hashes and restoration evidence

`H0` (pristine and every restored source):

```text
9fa10d44848a9ff7e9d516125beafe501d62d3df7dbcb777dd13fef074d69657
```

| Mutant | Mutated source SHA-256 | Restored SHA-256 / detector |
|---|---|---|
| M01 | `d995f44bd43a1ff852bbe1db573ccde91768cd7eee8ac4fdff23db2f06621e4f` | H0 / exit 0, 87/87 |
| M02 | `cae42f4a09935014ce036c619faae562ac1fa69e63e964b9fece4a19091bb337` | H0 / exit 0, 87/87 |
| M03 | `7ed3a0bb964e50637bdfeaa46daea6b26019fed3e2518148691cb3c740310a43` | H0 / exit 0, 87/87 |
| M04 | `fe866c983f5a9381370e79adae6c5f1743d99777576b38e30f50884b9d04b875` | H0 / exit 0, 87/87 |
| M05 | `f8eb92c57f23dd8412b473c8e2e81010247e8023998e93b5047aaae30fdceaac` | H0 / exit 0, 87/87 |
| M06 | `39ed2a68255bd41c44d09db48d9e7063f6d37c6d4909b8939b0253094da3e0fe` | H0 / exit 0, 87/87 |
| M07 | `d3aab7de2797314d5e4bb2c0b32966c746ae2d09a025f0ea964957b8e3d36acb` | H0 / exit 0, 87/87 |
| M08 | `9a87f87c65446932f6fe9ed3133c2d658e6ab78dfb089f13f1d9f13a2db4672d` | H0 / exit 0, 87/87 |
| M09 | `4b275fe52f59dfe8c4065965f55c8e881aa91cc9a8072733ba27a05a96389f86` | H0 / exit 0, 87/87 |
| M10 | `af998a715cc534744c9344947512210baff0c21b3de1e708dcd5cabc21114083` | H0 / exit 0, 87/87 |

For each run, the before/after detector hashes are equal. For each mutation triplet, pristine/restored hashes equal H0, while the mutated hash differs. The last restored run is exit **0**, `0 failure(s) over 87 assertions`, SHA-256 **H0**. No mutant patch remains applied in the scratch target, and no production source patch is proposed.

## Not checked

- No revised C1 candidate, final integration, live default binary resolution, frozen omp/opencode dumps, substrate pin verifier, or real loader execution. The self-test is fixture-only by construction (`verifiers/verify_surfaces.py:789-800`).
- No C2 description/XML checks, C3 erratum registry, corpus gates, lane-wide gates, build, linter, or formatter.
- No exhaustive callee deletion matrix, OC-rule operator matrix, mutant combinations, existential completeness proof, or execution of the illustrative partial-anchor/conflict/unresolved inputs above.
- No independent judgment or round closure. No subagents or other agent runtimes launched. No tools installed or updated.
