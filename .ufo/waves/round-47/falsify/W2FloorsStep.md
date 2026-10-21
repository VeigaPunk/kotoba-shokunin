verdict: PARTIAL — all three bump-in-step mutants fail loudly; restored-byte controls later time out, preventing an unqualified three-kill result.

# W2FloorsStep — scoped mutation probe

Lane-authored review by `KotobaR47-2.W2FloorsStep-2`; not integration or non-author closure.

## Scope and axes

- Revision: `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`.
- Scratch: `/fast/scratch/kotoba-r47/w2/W2FloorsStep-2/kotoba-shokunin`, with fleet siblings symlinked beside the clone to preserve canonical layout.
- **Freshness:** re-measure the landed surfaces/checklist assertion counts rather than reuse a receipt.
- **Operability:** execute the default detector and its 150-assertion self-test; preserve failures as well as passes.
- **Calibration:** distinguish named registry rejection from a timeout, and prove exact-byte restoration without treating a failed clean control as a killed mutant.
- Production source files were read only. Mutations were confined to this scratch clone. No subagents, package installs/updates, substrate sessions, or opencode wrapper executions occurred.

## Pinned source anchors

All path:line citations in this report refer to the revision above:

- `verifiers/floors-registry.json:2` states the bump-in-step rule and documents the coordinated-all-channels trust boundary; `:3` declares nine instruments, `:6` pins checklist at 1845, and `:38` pins surfaces at 99.
- `verifiers/check_assertion_floors.py:122-123` carries those floors in `EXPECTED_INSTRUMENTS`; `:142-145` carries them in `INSTRUMENTS`.
- `verifiers/check_assertion_floors.py:274-275` names disagreement between the in-file tables; `:352-354` names either table's disagreement with the external registry. `:443-452` runs these checks and returns 2 before the instrument walk.
- `verifiers/check_assertion_floors.py:129` sets the per-instrument timeout to 120 seconds; `:501-507` handles its expiration and `:517-519` returns 2 for that run error. Registry rejection and timeout therefore share an exit code but not a finding.

## Commands and controls actually run

Setup commands, both exit 0:

```sh
git clone -q --no-hardlinks /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/kotoba-r47/w2/W2FloorsStep-2/kotoba-shokunin
git -C /fast/scratch/kotoba-r47/w2/W2FloorsStep-2/kotoba-shokunin checkout -q --detach 7ad7fadfc09354b74fb66605dfb0c1182c115a2f
```

Every detector invocation used exactly the following argv from the scratch repo root, with an outer `subprocess.run(..., timeout=300)` bound and the detector's unchanged default 120-second per-instrument bound. No timeout was raised by the outer runner.

```sh
python3 -B verifiers/check_assertion_floors.py
```

| State, in execution order | Exit | Actual result | Elapsed seconds |
|---|---:|---|---:|
| Pristine tip | 0 | 9 PASS, surfaces 99, checklist 1845 | 115.814 |
| M1: registry-only surfaces bump | 2 | Named surfaces registry floor drift | 0.039 |
| Restored after M1 | 0 | Same 9 PASS as pristine | 118.142 |
| M2: checklist bump in one in-file table | 2 | Two named checklist floor-drift lines | 0.043 |
| Restored after M2 | 2 | 8 PASS; harness_independent self-test timeout | 125.749 |
| M3: surfaces lowered in both in-file tables | 2 | Named surfaces registry floor drift | 0.041 |
| Restored after M3 | 2 | 8 PASS; harness_independent self-test timeout | 125.665 |

Actual stdout of both clean runs (pristine and restored after M1):

```text
PASS harness observed=10 floor=10
PASS corpus_integrity observed=150 floor=150
PASS corpus_independent observed=91 floor=91
PASS surfaces observed=99 floor=99
PASS checklist observed=1845 floor=1845
PASS pins observed=62 floor=62
PASS harness_independent observed=104 floor=104
PASS compare_harness_independent observed=330 floor=330
PASS floors_guard observed=150 floor=150
```

The separate requested self-test command was run on pristine bytes and again after the final restoration, exits 0 and 0 respectively (1.115 s and 1.354 s):

```sh
python3 -B verifiers/check_assertion_floors.py --self-test
```

Both actual outputs:

```text
0 failure(s) over 150 assertions
```

All reported detector/self-test invocations had empty stderr.

## Mutants, expected detector, actual outputs, verdicts

Apply each listed change independently to the pinned scratch checkout, run the same default command above, then undo only that change. The original values and exact paths below are the reproduction recipe; the table and outputs above are observed, not predicted.

### M1 — registry only: surfaces 99 → 100

Smallest change: `verifiers/floors-registry.json:38`, change `"floor": 99` to `"floor": 100`; leave both in-file tables and all instrument implementations unchanged.

Expected: external-anchor disagreement, `FAIL registry floor drift: surfaces`, exit 2, not a self-test shortfall.

Actual stdout, exit 2:

```text
FAIL registry floor drift: surfaces registry=100 expected=99 row=99
```

**Verdict: KILLED.** Clean before and clean after; exact hashes restored. This is a complete pristine/mutant/restored sandwich.

### M2 — one in-file table only: checklist 1845 → 1846

Smallest change: `verifiers/check_assertion_floors.py:144`, change only the `INSTRUMENTS` checklist tuple's floor to 1846. Leave `EXPECTED_INSTRUMENTS["checklist"]` and the registry at 1845.

Expected: internal-table disagreement plus external-anchor disagreement, both naming checklist, exit 2.

Actual stdout, exit 2:

```text
FAIL registry floor drift: checklist floor=1846 expected=1845
FAIL registry floor drift: checklist registry=1845 expected=1845 row=1846
```

**Named rejection observed; conservative full-trial verdict: INCONCLUSIVE.** The preceding pristine-byte control passed, and the mutant was rejected for exactly the expected registry reasons. However, the restored-byte run did not return clean: it timed out in `harness_independent`. Do not upgrade that incomplete clean/mutant/clean result to an unqualified kill.

### M3 — lower a floor while keeping both in-file tables consistent: surfaces 99 → 98

One conceptual floor-lowering defect applied to `verifiers/check_assertion_floors.py:122` and `:142`: set the surfaces floor to 98 in both `EXPECTED_INSTRUMENTS` and `INSTRUMENTS`. Leave `verifiers/floors-registry.json:38` at 99. This exercises the external anchor rather than relying on the two tables disagreeing.

Expected: `FAIL registry floor drift: surfaces registry=99 expected=98 row=98`, exit 2.

Actual stdout, exit 2:

```text
FAIL registry floor drift: surfaces registry=99 expected=98 row=98
```

**Verdict: INCONCLUSIVE as a fully controlled kill.** The common initial pristine baseline passed, and the mutant produced the exact expected named rejection. But its immediately preceding pristine-byte control and its restored-byte control both timed out. A failed baseline is not a killed mutant. No silent-green survivor was observed.

## Additional finding: default detector not consistently green on unchanged bytes

After M2 and M3, the exact restored inputs produced the following identical stdout, exit 2:

```text
PASS harness observed=10 floor=10
PASS corpus_integrity observed=150 floor=150
PASS corpus_independent observed=91 floor=91
PASS surfaces observed=99 floor=99
PASS checklist observed=1845 floor=1845
PASS pins observed=62 floor=62
FAIL harness_independent self-test timed out after 120s (hung?)
PASS compare_harness_independent observed=330 floor=330
PASS floors_guard observed=150 floor=150
```

This is an operational limitation of the observed default-resolution runs, not an extra registry mutant and not evidence that a floor mismatch survived. Cause was not established. The two earlier clean runs, the later timeouts, and the unchanged hashes are all retained here; no increased-timeout retry was substituted for the requested command.

## Before / mutated / restored SHA-256 evidence

The following command was run seven times: pristine, each of the three mutated states, and after each of the three restorations. Every checksum command exited 0 with empty stderr.

```sh
sha256sum verifiers/check_assertion_floors.py verifiers/floors-registry.json
```

Pristine hashes, also observed after **every** restoration:

```text
40fe8788f37a5c30ebb854fc2805dad203e806c7bc989e513ad63645a5c60182  verifiers/check_assertion_floors.py
6b0595967999353469fb79edd3fcc6d0f979589b1191a6486c6db61d07493b2b  verifiers/floors-registry.json
```

Mutated hashes:

| State | check_assertion_floors.py SHA-256 | floors-registry.json SHA-256 |
|---|---|---|
| M1 registry only | `40fe8788f37a5c30ebb854fc2805dad203e806c7bc989e513ad63645a5c60182` | `6823094989310229ce466ebdffdd359e0727c1c131783a57824db3130d6d8586` |
| M2 one table only | `e4b5bd54f13d5c6895fbeb032654fc6dfb26459d1550e193f64714bcf70ffd97` | `6b0595967999353469fb79edd3fcc6d0f979589b1191a6486c6db61d07493b2b` |
| M3 both in-file floors lowered | `1af69ea031cbdebe50d791381d991765cebb9f7cdd068b52fec900b5ee689488` | `6b0595967999353469fb79edd3fcc6d0f979589b1191a6486c6db61d07493b2b` |

Both target files ended at their exact pristine hashes even though two restored behavioral runs failed. No mutation remains in those scratch files.

## Not checked

- Did not re-derive live omp/opencode binary surfaces, pin freshness, XML trigger semantics, governance errata, corpus integrity verdicts, source rows, or the fault harness as separate acceptance checks. The floor detector invoked its registered instruments' self-tests only.
- Did not test coordinated edits to all three floor channels, docstring-only drift, instrument deletion/repointing, fake assertion summaries, or overrides; these are outside this assigned three-mutation probe.
- Did not diagnose the `harness_independent` timeout or increase its limit, change a floor to accommodate it, rerun a failed control merely to obtain green, or alter the invariant.
- No integration, shipping, lane Git/jj mutation, or SHONEN marking was performed. No tools were installed or updated.
