# MutBoxProofCode — round-50 falsify, C2 operability (kotoba, judged 956ee167)

VERDICT: HOLDS-BOUNDED — applies to claim C2 (`plans/round-50.md`, re-sized before landing): the statement "deleting any one of the 6 must-fail cases from `verifiers/fixtures/dispatch-prompts/manifest.json` makes `--box-proof` exit 1: 0 of 6 → 6 of 6" is enforced by the landed code, not merely asserted: the mutation probe below breaks it in 10 of 17 single-point mutants (driver prints 5 of 6, 4 of 6, 1 of 6, 0 of 6, 0 of 6, or aborts with exit 2). The bound: the C2 counter (`verifiers/box_proof_case_deletion.py`) gates its exit code on the six conjuncts only — it also deletes the must-pass controls and the N/A case and prints `controls killed 0 of 2` / `na killed 0 of 1`, but those lines do not affect its exit code, so 7 of 17 mutants survive the C2 counter with `killed 6 of 6` and exit 0; the instrument's own `--self-test` catches 16 of the 17.

## Scope and method

- Judged bytes: `master` at `956ee1676e4c18480bce8ac3993541462be76e11`. Private clone `/fast/scratch/hyaku/kotoba-r50/falsify/MutBoxProofCode/lane` (`git clone -q` of the lane + `git checkout -q 956ee167…`); `git -C lane rev-parse HEAD` → `956ee167…e76e11`.
- Mutated file: `verifiers/verify_dispatch_prompts.py` only (box-proof coverage code: observed-status check, `ALLOWED_CO_FAIL`, control requirement, N/A requirement, `EnvError` handling, `CONJUNCTS` use). 17 single-point mutants, one exact-string substitution each, applied by `harness.py` (scratch dir) with an assertion that each substitution matched once.
- Per mutant: `git -C lane commit -qam "mut: <id>"` inside the clone, then `python3 -B verifiers/verify_dispatch_prompts.py --self-test` and `python3 -B verifiers/box_proof_case_deletion.py --rev HEAD --repo <clone>`; then `git -C lane reset --hard 956ee167…`.
- Baseline (pristine, same clone): `--self-test` → `0 failure(s) over 56 assertions`, exit 0; driver → `killed 6 of 6`, `controls killed 2 of 2`, `na killed 1 of 1`, exit 0; driver at the round-49 base `f3046466…` → `killed 0 of 6`, exit 1 (C2's before-value).
- Tools: python3 3.14.8, git (system); no package installed or upgraded. Lane writes: none except this report; no git write command and no jj command in the lane, the fleet repo or a sibling lane. No subagent dispatch (leaf seat).

## Mutant table

`self-test` = failures over 56 assertions (exit 1 = at least one failure). `driver` = the `killed K of 6` line the C2 driver prints; `abort` = the driver exits 2 with `ERROR the intact box proof at HEAD does not exit 0; case coverage is not measurable` and prints no kill count. Pristine baseline: 0 failures / 6 of 6 / exit 0.

| id | locus (one-line mutation) | self-test | driver | verdict |
|---|---|---|---|---|
| M01 | coverage-isolation: drop the isolation test (`any(n in fails)`) | 3 failures, exit 1 | 5 of 6, exit 1 | killed by both |
| M02 | coverage-verdict: the coverage problem line no longer sets `ok = False` | 8 failures, exit 1 | 0 of 6, exit 1 | killed by both |
| M03 | conjunct-source: the conjunct list is derived from the manifest labels | 11 failures, exit 1 | 1 of 6, exit 1 | killed by both |
| M04 | conjunct-constant: `CONJUNCTS` drops `lane_identity_known` | 3 failures, exit 1 | 5 of 6, exit 1 | killed by both |
| M05 | conjunct-use: only the first two conjuncts per box are checked | 4 failures, exit 1 | 4 of 6, exit 1 | killed by both |
| M06 | allowed-co-fail: `ALLOWED_CO_FAIL` emptied | 3 failures, exit 1 | abort, exit 2 | killed by both |
| M07 | allowed-co-fail: reverse pairing added (stem → path) | 3 failures, exit 1 | 5 of 6, exit 1 | killed by both |
| M08 | allowed-co-fail: the pinned co-failure is ignored (`allowed = frozenset()`) | 3 failures, exit 1 | abort, exit 2 | killed by both |
| M09 | control-requirement: the must-pass control requirement is dropped | 2 failures, exit 1 | 6 of 6, exit 0 | survived by driver, killed by self-test |
| M10 | na-requirement: the N/A arm requirement is dropped | 1 failure, exit 1 | 6 of 6, exit 0 | survived by driver, killed by self-test |
| M11 | na-requirement: the N/A arm is recognised on an observed PASS | 3 failures, exit 1 | abort, exit 2 | killed by both |
| M12 | env-error: `except (EnvError, OSError)` → `except OSError` | 0 failures, exit 0 | 6 of 6, exit 0 | survived by both (F3) |
| M13 | env-error: a substrate error no longer sets `substrate_error` | 1 failure, exit 1 | 6 of 6, exit 0 | survived by driver, killed by self-test |
| M14 | observed-status: coverage reads the case's `expect_conjunct` label | 1 failure, exit 1 | 6 of 6, exit 0 | survived by driver, killed by self-test |
| M15 | exit-code: one proven box is enough (`proven >= 1`) | 11 failures, exit 1 | 0 of 6, exit 1 | killed by both |
| M16 | observed-status: the named conjunct's expected status is not checked | 1 failure, exit 1 | 6 of 6, exit 0 | survived by driver, killed by self-test |
| M17 | case-selection: the `check` id is ignored, every case is scored for every box | 2 failures, exit 1 | 6 of 6, exit 0 | survived by driver, killed by self-test |

## Findings

**F1 — the C2 counter's exit code does not gate the control and N/A deletions it performs.** The driver deletes the must-pass controls (`d04-control`, `d08-control`) and the N/A case (`d08-missing-state`) and prints `controls killed C of 2` / `na killed A of 1`, but its exit code is `0 if killed == 6 else 1` plus the run-error counter; those counts are never read. M09 (control requirement dropped) → `controls killed 0 of 2`, `killed 6 of 6`, exit 0; M10 (N/A requirement dropped) → `na killed 0 of 1`, `killed 6 of 6`, exit 0; M17 (per-box case selection dropped) → `controls killed 0 of 2`, `killed 6 of 6`, exit 0. C2's statement names only the six must-fail cases, so this is not a false statement; it is a coverage limit of the counter, and the two lines it prints while exiting 0 can be misread as failures. The instrument's self-test covers all three.

**F2 — the C2 counter cannot see the observation rule the plan's re-sizing note names.** The plan says "Coverage is checked on observed conjunct statuses (with one pinned co-failure: the placeholder sits inside the stem)". M14 replaces the observed failing set with the case's `expect_conjunct` label and M16 stops checking the named conjunct's observed status; both still print `killed 6 of 6`, exit 0, because the committed corpus's labels are correct. Only the self-test arms "a relabelled placeholder copy cannot cover the stem" and "a must-fail case naming an unnamed conjunct is rejected" catch them. The deletion counter measures the deletion behaviour, not the observation rule; C2's wording does not claim the latter, so the statement still holds, but the counter alone is not a witness for "observed conjunct statuses".

**F3 — the `EnvError` arm is exercised by neither detector.** M12 (`except (EnvError, OSError)` → `except OSError`) passes `--self-test` (0 failures) and the C2 driver (6 of 6, exit 0). It is not an equivalent mutant: with one fixture prompt file made unreadable (`chmod 000`), the pristine instrument prints `boxes proven 1` plus `box-proof: dispatch.04/d04-placeholder: … Permission denied (prompt file)` and exits 2 with no traceback, while M12 raises an uncaught `EnvError` and exits 1 with a traceback — the behaviour the `box_proof` docstring forbids. Neither detector creates an unreadable fixture file, so neither can see it.

**F4 — the C2 counter reports an abort, not a kill count, when the base proof itself breaks.** M06, M08 and M11 leave the intact proof failing (`boxes proven 1`, exit 1); the driver exits 2 with `ERROR the intact box proof at HEAD does not exit 0; case coverage is not measurable` and prints no `killed K of 6` line. The regression is detected, but a consumer reading only the last output line sees no count.

**F5 — the six-case enforcement is real.** 10 of 17 mutants break it (M01 5 of 6, M02 0 of 6, M03 1 of 6, M04 5 of 6, M05 4 of 6, M06 abort, M07 5 of 6, M08 abort, M11 abort, M15 0 of 6), against the pristine 6 of 6 and the round-49 base's 0 of 6. The coverage rule fails when the code that enforces it is broken.

## Evidence (commands, exit codes)

    git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin <scratch>/lane
    git -C <scratch>/lane checkout -q 956ee1676e4c18480bce8ac3993541462be76e11
    python3 -B verifiers/verify_dispatch_prompts.py --self-test  → "0 failure(s) over 56 assertions", exit 0
    python3 -B verifiers/box_proof_case_deletion.py --rev HEAD --repo <scratch>/lane
        → control: exit 0 boxes proven 2 / killed 6 of 6 / controls killed 2 of 2 / na killed 1 of 1, exit 0
    python3 -B verifiers/box_proof_case_deletion.py --rev f30464660c675d1c1e2851a3bf0366a3aaffe5a8 --repo <scratch>/lane
        → six cases "exit 0 survived" / controls killed 0 of 2 / na killed 0 of 1 / killed 0 of 6, exit 1
    # per mutant (17x), inside the clone only
    git -C <scratch>/lane commit -qam "mut: <id>"
    python3 -B verifiers/verify_dispatch_prompts.py --self-test  → failure counts in the table, exit 0/1
    python3 -B verifiers/box_proof_case_deletion.py --rev HEAD --repo <scratch>/lane  → "killed K of 6" (or abort, exit 2)
    # supplementary probe for F3 (scratch copy, one fixture prompt file chmod 000)
    python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json
        pristine → "boxes proven 1" + "box-proof: dispatch.04/d04-placeholder: … Permission denied (prompt file)", exit 2
        M12      → uncaught EnvError traceback, exit 1
    # restoration (bytes restored after every mutant; final state)
    sha256sum <scratch>/lane/verifiers/verify_dispatch_prompts.py → de9602710a67a3a54ca7ede0e64fcc8047410071b5df8f853e5cb401cc4adc2b
    sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/verify_dispatch_prompts.py → the same digest
    git -C <scratch>/lane rev-parse HEAD → 956ee1676e4c18480bce8ac3993541462be76e11
    git -C <scratch>/lane status --porcelain → (empty)
    Harness and raw run logs: /fast/scratch/hyaku/kotoba-r50/falsify/MutBoxProofCode/ (harness.py, run4.json).
