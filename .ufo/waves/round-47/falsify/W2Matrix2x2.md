verdict: HOLDS — frozen-dump 2×2 rejects all three stale/crossed combinations; only tip code × tip baseline+census passes

## Scope and axes

Reviewed C1's **“re-derived, not copied”** claim through the assigned code/data cross-product. Axes: **freshness** (old-generation data must fail), **operability** (current code and data work on frozen bytes), **calibration** (do not mistake consistency checks for independent semantic provenance). This is lane-authored review, not admission or closure.

BASE: `c61a973b2e02e1ded169703ddcb06466f4edd8bd`; tip: `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`. Work ran in `/fast/scratch/kotoba-r47/w2/W2Matrix2x2/`, with canonical-layout clone `kotoba-shokunin/` and extracted matrix inputs in `m/base/` and `m/tip/`. Production files were not mutated.

## Four-cell attack: result

Every cell used the same frozen `omp-18.12.5.strings` and `opencode-1.19.3.strings`; “data” means baseline JSON **and** census from the same revision. All seven checks ran, without `--check` filtering.

| Code | Baseline+census | Exit | Key observed output |
|---|---|---:|---|
| BASE | BASE | **1** | FAIL `literal_present` (8 OMP loader literals); FAIL `no_uncovered_class` (0 extracted vs 8 declared; explicit vacuity); FAIL `opencode_extract` (old project/read-hook/API classes lack matching rules). Four inventory checks PASS, 38 IDs. |
| BASE | tip | **1** | Same two OMP failures; FAIL `opencode_extract` (seven current classes produced by no rule; OC-1/OC-4/OC-6 unmatched). Four inventory checks PASS, 42 IDs. |
| tip | BASE | **1** | OMP checks PASS; FAIL `opencode_extract`: three obsolete IDs produced by no rule and seven current IDs undeclared in baseline. Four inventory checks PASS, 38 IDs. |
| tip | tip | **0** | **7/7 PASS**: 42 loader-kind entries; all 8 extracted OMP classes declared; opencode **9/9 classes from 7/7 rules**; inventory/literal/kind parity 42 IDs; 8 excluded entries reasoned. |

The strongest requested counterexample—tip extractor with the internally consistent BASE baseline+census—is rejected **for substrate-derived opencode identity differences**, not because BASE baseline and BASE census disagree. Exact rejection:

```text
FAIL surfaces.opencode_extract: declared opencode class(es) produced by no rule: opencode:api-entries/instructions, opencode:project/AGENTS.md, opencode:read-hook/AGENTS.md; extracted opencode class(es) undeclared in baseline: opencode:claude-home/CLAUDE.md, opencode:config/instructions-remote, opencode:instruction-context/AGENTS.md, opencode:instructions/AGENTS.md, opencode:instructions/CLAUDE.md, opencode:instructions/CONTEXT.md, opencode:read-hook/instructions
```

### Commands and reproduction

Inputs were extracted using `git show` from the canonical-layout scratch clone. For each `(revision, destination)` pair `(c61a973b2e02e1ded169703ddcb06466f4edd8bd, base)` and `(7ad7fadfc09354b74fb66605dfb0c1182c115a2f, tip)`:

```sh
git -C kotoba-shokunin show "$revision:verifiers/verify_surfaces.py" > "m/$destination/verify_surfaces.py"
git -C kotoba-shokunin show "$revision:verifiers/surfaces-baseline.json" > "m/$destination/surfaces-baseline.json"
git -C kotoba-shokunin show "$revision:corpus/knowledge/instruction-surface-census-round13.md" > "m/$destination/census.md"
```

Extraction completed successfully. Each matrix invocation had this argument set, substituting the four `code`/`data` pairs in the table:

```sh
python3 "m/$code/verify_surfaces.py" \
  --repo "$PWD/kotoba-shokunin" \
  --omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings \
  --opencode-strings /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings \
  --baseline "m/$data/surfaces-baseline.json" \
  --inventory "m/$data/census.md"
```

Captured complete cell outputs, including `exit=`, remain at scratch paths `m/cell-base-base.txt`, `m/cell-base-tip.txt`, `m/cell-tip-base.txt`, `m/cell-tip-tip.txt`. Matrix exits in that order: **1, 1, 1, 0**.

`sha256sum -c SHA256SUMS` in `/fast/scratch/kotoba-r47/shared/` exited **0**, all four files OK. Re-dumping both frozen binaries with GNU `strings -n 4` (GNU Binutils 2.47) produced hashes equal to the frozen dumps:

```text
omp strings:      33df0aeffc4565967bc1a3b42621f8eade0e6e4c2ae8733319fcd484902fb301
opencode strings: f4d8f34ae02a2411eb5e30203421b6fcdfa81b83e96b768bbcf404504a297bc3
omp binary:       fdbc8136084c9a10439569157b2af62312e2b0d801cab54c73e89476da798e7e
opencode binary:  179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9
```

## Evidence at tip and additional probes

All following source references are at `7ad7fad`:

- `verifiers/verify_surfaces.py:354-364` explicitly separates the 1.19.3 generation from retired v2.0.26 anchors. `:447-475` derives priority-list names and config/home paths and checks local/remote instruction consumers; `:479-498` covers read hook, resolution switch, and instruction-context subsystem.
- `verifiers/surfaces-baseline.json:245-305` declares the nine current opencode identities. The decisive renamed/returned identities are not merely a timestamp update: `:245`, `:252`, `:259`, `:273`, `:287`, `:294`, `:301` correspond to the seven undeclared IDs emitted against BASE data.
- `corpus/knowledge/instruction-surface-census-round13.md:212-257` presents current substrate and nine inventory rows; `:289-305` segregates obsolete rows outside the machine-counted inventory and introduces the historical identity ledger.

Additional attacks already exercised:

1. **tip code + tip baseline + BASE census:** exit **1**, `table_parity` names missing current and extra obsolete rows, even though the three dump-based checks pass.
2. **tip code + BASE baseline + tip census:** exit **1**, both `opencode_extract` and `table_parity` fail.
3. **tip code + BASE data, only `literal_present` and `no_uncovered_class`:** exit **0**. This is not a full-gate bypass: the unchanged eight OMP class identities legitimately remain accepted after extractor refresh; the full run rejects opencode identity drift. Do not cite this two-check subset as proof of opencode freshness.
4. **tip script in canonical scratch clone, default resolution:** exit **0**, seven checks pass. Observed default binary hashes matched the frozen binaries. The opencode wrapper was not executed.
5. **Relocated extracted script `m/tip/verify_surfaces.py --self-test`:** exit **1**, 98 failures/99 assertions because it resolves fixtures under `m/tip/fixtures/surfaces/`, which were not copied (errors include missing `baseline-clean.json`). This was an invalid fixture-location probe, **not evidence of a product self-test regression**. No successful canonical-location self-test is claimed.

## Counterexample disposition and smallest safe correction

**No counterexample broke the assigned matrix criterion.** Freshness and operability survive this scoped attack. No code correction is warranted from these results.

Calibration boundary: this experiment demonstrates that both extractor and data changes are necessary on these frozen dumps, and that stale self-consistent data is rejected. It does **not**, by itself, prove independent human re-derivation of every semantic claim, runtime loading behavior, or absence of copy-forward inside matching rows. The smallest safe reporting correction, if a broader conclusion is proposed, is to state precisely this matrix result rather than equate 7/7 with full provenance or semantic equivalence.

## Not checked

No C2 XML/checklist mutation tests, C3 corpus/fault-harness tests, substrate-pin verifier, canonical-location self-test, live sessions, upstream source validation, full census count-command audit, independent reverse engineering of each loader's semantics, or exhaustive mutations of the new regex gates. No installations or upgrades. No SHONEN marks, integrations, production commits, or changes to runtime routing.
