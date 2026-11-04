# MutTester mutation battery — round 85 / w1

## Scope and detector
C1 production counter was absent at seat start; the explicitly permitted frozen-spec fallback is used. These are reference-spec kills, NOT evidence that the production C1 counter kills these inputs. `reference_scorer.py` transcribes the eight frozen labels and invokes the actual round-74 sibling census for R5. Parser anchored to lane baseline: description 1021 characters, first sentence 150.

C2 uses a byte-frozen copy of the existing pin checker and a host-matching candidate baseline (explicit binary paths). No runtime binaries were invoked. Detector sha256: `3f222b1abc18572b4449334401d141f51a02aeb48b8c2fcafa687417307fb311`. Every receipt records exact commands, pristine/mutated/restored output and SHA256 hashes. `fixture-inputs.json` preserves construction bytes; knowledge quote is a synthetic shape fixture, not a source quotation claim.

## Results

| Mutant | Expected red | Observed red | Verdict |
|---|---|---|---|
| M01-R1 | R1 | R1 | killed |
| M02-R2 | R2 | R2 | killed |
| M03-R3 | R3 | R3,R5 | killed (coupled) |
| M04-R4 | R4 | R4 | killed |
| M05-R5 | R5 | R5 | killed |
| M06-R6 | R6 | R6 | killed |
| M07-R7 | R7 | R7 | killed |
| M08-R8 | R8 | R8 | killed |
| L01-trigger-laundering | R1 | R1 | killed |
| L02-negative-laundering | R6 | R6 | killed |

All C1 pristine/restored runs: exit 0, `description render rules met 8 of 8`; all mutants exit 1. Nine mutants read 7 of 8. M03 reads 6 of 8: violating R3 with >1024 characters also violates R5 because the census enforces the same ceiling. Thus the requested strictly R3-only witness cannot exist under literal R5; do not count this as isolated load-bearing evidence. L01 has declared trigger-list quotes only after offset 99: R2 passes while R1 fails. L02 negatives share `kubernetes cluster manifest` with one another but no qualifying description word: R6 fails.

### C2 actual outputs

- **C2-wrong-sha**: expected rejection; observed exit 1; **killed**.
```text
FAIL omp_binary_sha256: sha256 drift: expect=0000000000000000000000000000000000000000000000000000000000000000 got=6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f
PASS omp_binary_mtime: delta 0 ns (tolerance 0 ns)
PASS opencode_binary_sha256: ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7
DRIFT 1/3 pins failed: omp_binary_sha256
```

- **C2-missing-path**: expected rejection; observed exit 2; **killed**.
```text
FAIL omp_binary_sha256: UNREADABLE: [Errno 2] No such file or directory: '/fast/scratch/hyaku/kotoba-r85/MutTester/missing-omp'
FAIL omp_binary_mtime: UNREADABLE: [Errno 2] No such file or directory: '/fast/scratch/hyaku/kotoba-r85/MutTester/missing-omp'
PASS opencode_binary_sha256: ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7
UNREADABLE 2/3 pins failed: omp_binary_sha256, omp_binary_mtime
```

- **C2-non-ns-mtime**: expected rejection; observed exit 0; **survived**.
```text
PASS omp_binary_sha256: 6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f
PASS omp_binary_mtime: delta 804 ns (tolerance 999 ns)
PASS opencode_binary_sha256: ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7
OK 3/3 pins hold
```

## Bounds, not contract changes
The microsecond mtime mutant is a surviving ns-exactness coverage probe: `delta 804 ns (tolerance 999 ns)` still prints `OK 3/3 pins hold`. Existing checker deliberately tolerates the precision stated by a pin; this does not invalidate the actual 9-digit candidate pin. KotobaR85 directed preservation of the frozen predicate and reporting this as a bound, not a refusal requirement or authorization to strengthen the checker. Wrong sha and missing path are killed. No C1 production-counter defect is inferred from the independent reference scorer.

## Restoration
Every mutant restored identical pristine bytes and then reran the same detector successfully. Before/mutated/after hashes are recorded in each receipt. Missing-path mutation changes only the argv, and restoration reruns pristine argv. Production files were never edited. Scratch removed after persisting receipts and fixtures. No tools installed or upgraded.

## Self-evaluation
Accuracy 4: C1 is clearly limited to independent frozen-spec scoring. Completeness 4: 13 requested probes run; isolated R3 impossible due to R5 coupling. Clarity 4: raw outputs in separate receipts. Actionability 4: fixture bytes and frozen detector retained, but scratch paths require reconstruction. Conciseness 4: one table plus actual C2 lines. Overall 4.0. Improvements: compare production C1 detector only under a separately assigned probe; preserve the distinction between coarse-pin bounds and actual ns-exact pins. User agreement expected because limitations are explicit.
