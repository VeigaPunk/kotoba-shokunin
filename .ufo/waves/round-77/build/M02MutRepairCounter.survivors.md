# M02MutRepairCounter — C2 mutation findings

Scope: mutation-test disclosure only. Frozen target: `verifiers/check_r75_routed_repairs.py`; no counter or lane source edits. Original SHA-256 before probes: `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63`.

Method: isolated shared scratch clone at `/fast/scratch/hyaku/kotoba-r77/M02MutRepairCounter/clone`, based on lane HEAD `6523aced1ee0ebe07dca996213bdc645a6acbd1e`; each single-point mutant replaced only the scratch verifier, ran `python3 -B .../check_r75_routed_repairs.py --repo .../clone --work .../work --self-test`, then restored the pristine copy before the next probe. 36 distinct mutants were run to completion (corrected two harness anchor misses before running those cases). Self-test success means the mutant survived; nonzero means killed by the detector.

## Survivors (22/36)

Each listed mutant returned exit 0 and `self-test: 0 failure(s) over 27 assertions`. These are coverage findings, not contract changes.

| Mutant | Source line | Reason it survived |
|---|---:|---|
| M01 allow any ancestor instead of exact R75 tip | 397 | The stale-ancestor fake fixture does not include `BASE` (or another non-R75 ancestor) in `FakeRepo.ancestors`; removing exact-tip equality still passes because the fake ancestry check rejects the tested stale value. |
| M04 omit recomputed stripped-value check | 369 | No self-test supplies a committed description whose stripped render differs from the required 1021. |
| M05 omit recomputed clip-value check | 366 | No self-test supplies committed SKILL bytes with a wrong clip render while the receipt still claims the target. |
| M06 omit R1 measured-revision ancestry check | 358 | No R1 fixture uses a non-ancestor measured revision. |
| M10 omit recomputed block-line-range check | 379 | No self-test shifts the description block away from lines 4–18. |
| M14 omit rejection of `DRIFT` in receipt transcript | 421 | No self-test injects a transcript containing `DRIFT` while otherwise matching live stdout. |
| M15 omit green-verdict wording check | 423 | No self-test removes the verdict token while retaining transcript stdout and exit 0. |
| M16 omit live gate exit validation | 433 | The forged-green fixture already fails the unchanged live-output `DRIFT` arm, so it does not isolate the exit-code arm. |
| M17 omit live gate `DRIFT` validation | 435 | The forged-green fixture already fails the unchanged live-exit arm, so it does not isolate the output arm. |
| M18 allow empty normalized stdout through | 439 | No self-test gives the fake gate an empty stdout with a transcript block present. |
| M20 omit R3 excerpt check | 476 | No fixture removes just the excerpt while retaining the absent-report pathname; the existing edit helper removes both. |
| M21 omit R3 absent-report pathname check | 479 | The excerpt-removal helper also removes the pathname, so no test isolates this check. |
| M23 omit R3 explicit absence statement | 486 | No self-test removes only the absence wording while preserving excerpt, path, count, and citation. |
| M25 omit R4 dead-seat count check | 533 | No self-test removes or forges only the `0 dead` count. |
| M26 omit R4 recomputed report/seat pair check | 530 | No self-test forges or removes only the report/seat pair. |
| M27 omit R4 R75Attack28 settlement check | 536 | No self-test removes only the seat settlement while retaining the other closing facts. |
| M28 omit R4 settlement proximity check | 543 | No self-test separates the closing facts by more than three lines. |
| M32 omit M75 quoted-window check | 317 | No fixture retains required tokens but removes the verbatim excerpt window. |
| M33 omit Gate quoted-window check | 335 | No fixture retains required Gate tokens but removes the verbatim excerpt window. |
| M34 omit missing first-line R2 revision failure | 394 | The missing-tip-revision fixture still fails the independent live transcript matching arm; it does not isolate the missing-revision finding. |
| M35 omit R4 pending-text anchor check | 507 | No self-test removes `w2 falsify results pending` while retaining the settlement tail. |
| M36 omit R1 correction line-range claim check | 340 | No self-test removes only `4–18` from the correction while preserving all other R1 evidence. |

## Killed mutants (14/36)

For each, the command exited 1. Exact detector diagnostics (stderr):

- M02 skip normalized-stdout comparison — `FAIL broken world survived: R2 copied green stdout does not match the sandbox rerun -> closed 4`.
- M03 compare clip render against 1021 — honest fixture failed R1 (`recomputed folded render ... is 1022, not 1022 (stripped 1021)`); self-test exited 1 with 2 failures / 27 assertions.
- M07 omit receipt clip-number requirement — `FAIL broken world survived: R1 receipt prints no render length -> closed 4`.
- M08 omit receipt stripped-number requirement — `FAIL broken world survived: R1 receipt prints no stripped variant -> closed 4`.
- M09 omit receipt convention requirement — `FAIL broken world survived: R1 receipt names no convention -> closed 4`.
- M11 omit correction render-number requirement — `FAIL broken world survived: R1 correction asserts no render length -> closed 4`.
- M12 omit correction citation requirement — `FAIL broken world survived: R1 correction cites no spot-check -> closed 4`.
- M13 omit receipt exit-code requirement — `FAIL broken world survived: R2 receipt carries no exit code -> closed 4`.
- M19 make R2 LOG citation unconditional pass — `FAIL broken world survived: R2 LOG does not cite the receipt -> closed 4`.
- M22 omit R3 count-pair requirement — `FAIL broken world survived: R3 note records no counts -> closed 4`.
- M24 make R3 LOG citation unconditional pass — `FAIL broken world survived: R3 LOG does not cite the note -> closed 4`.
- M29 replace recomputed report count with literal 1021 — honest fixture reports no `1021 of 64` pair; real-git arm also rejected the honest fixture.
- M30 take R3 excerpt from arbitrary first result — honest fixture failed R3: `the note carries no machine-checkable excerpt (>=20-character verbatim window) of the R75Attack28 results entry`.
- M31 omit append-only lesson check — `FAIL broken world survived: R1 lesson rewritten (not appended) -> closed 4`.

## Verification and restoration

- Pristine baseline command: `python3 -B /fast/scratch/hyaku/kotoba-r77/M02MutRepairCounter/clone/verifiers/check_r75_routed_repairs.py --repo /fast/scratch/hyaku/kotoba-r77/M02MutRepairCounter/clone --work /fast/scratch/hyaku/kotoba-r77/M02MutRepairCounter/work --self-test`; exit 0, `self-test: 0 failure(s) over 27 assertions`.
- Restored-byte self-test: same command; exit 0, `self-test: 0 failure(s) over 27 assertions`.
- After all probes, `sha256sum` of lane source, pristine backup and restored scratch verifier was identical: `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63`. `cmp` of pristine backup and scratch verifier succeeded. Scratch clone HEAD remained `6523aced1ee0ebe07dca996213bdc645a6acbd1e`.
- No tools installed.
