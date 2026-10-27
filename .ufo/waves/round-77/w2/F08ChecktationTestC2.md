# F08 — C2 R1/R3/R4 mutation probe

Scope: `verifiers/check_r75_routed_repairs.py` R1, R3, and R4. Frozen counter SHA-256 at lane HEAD: `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63`, matching `plans/round-77.md`. Lane HEAD checked before and after probe: `6523aced1ee0ebe07dca996213bdc645a6acbd1e` (freeze); the planned claim data is not committed there. Specifically, `corpus/lessons/round-75.md` has no appended correction; the R1 receipt, R2 no-harm receipt, and R3 note are absent; LOG lacks the R2/R3 citations and R4 settlement. Therefore no landed claim data was treated as verified.

## Detector / pristine baseline

Isolated scratch clone: `/fast/scratch/hyaku/kotoba-r77/F08Mutation-TestC2/clone`, cloned shared from lane HEAD, configured as `scratch-r77 <scratch@example.invalid>`, and top-level check matched the expected clone path before any scratch fixture commits.

Pristine detector command:

`timeout 120 python3 -B verifiers/check_r75_routed_repairs.py --self-test --repo "$S/clone" --work "$S/work"`

Output: `PASS honest world: closed 4 of 4`; all listed broken worlds rejected; `PASS real-git arm: honest fixture closes 4 of 4`; `PASS real-git arm: token-dump fixture rejected (exit 1)`; `self-test: 0 failure(s) over 27 assertions`. Process exit `0`. Pristine counter hash: `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63`.

Frozen-base gate command:

`timeout 120 python3 -B verifiers/check_r75_routed_repairs.py --repo "$S/clone" --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e --work "$S/work-base"`

Output: `measured-rev: 6523aced1ee0ebe07dca996213bdc645a6acbd1e`; `R1: open`, `R2: open`, `R3: open`, `R4: open`; `r75 routed repairs closed 0 of 4`; process exit `1` (expected pre-data red). This independently confirms data is not landed at the tested revision.

## Mutants

Each mutant changed only the scratch clone's counter source; the same `--self-test` detector ran at each mutant. No lane files were changed.

- **R1 mutant (survived / coverage finding):** changed `if "M75-1" not in appended:` to `if False:` in `r1_correction`. Mutant SHA-256: `d62cd40070131f6e54ddf71296a4993e09a37cf9f8385d144c711e7273ca2d21`. Command: `timeout 120 python3 -B verifiers/check_r75_routed_repairs.py --self-test --repo "$S/clone" --work "$S/work-r1"`. Output ended `self-test: 0 failure(s) over 27 assertions`; exit `0`. The detector did not notice that the required M75-1 name check had been disabled. Minimal repair: add an isolated must-fail fixture removing only `M75-1` from the correction while preserving its quoted source text and other required facts. This improves R1 test depth without changing the C2 contract or another axis.
- **R3 mutant (survived / coverage finding):** changed `if "R75Attack28" not in note:` to `if False:` in `r3_note`. Mutant SHA-256: `962cd013767c13733789924a22b8233658bea2be129d15c8222b73c511829d03`. Command: `timeout 120 python3 -B verifiers/check_r75_routed_repairs.py --self-test --repo "$S/clone" --work "$S/work-r3"`. Output ended `self-test: 0 failure(s) over 27 assertions`; exit `0`. Inspection of the existing “R3 note names no seat” fixture shows its global replacement also changes `w2/R75Attack28.md`, so the independent missing-report-path check rejects that world; the seat-name predicate is not isolated. Minimal repair: remove only the seat name in the note prose while retaining the required report path and all other evidence. This improves R3 test specificity without changing the contract or another axis.
- **R4 mutant (killed):** inserted `return []` at the start of `r4_log_closing`, bypassing the R4 gate. Mutant SHA-256: `ec1c282e04f07034277fb6058cd53c3d865434fc4c4596ef4ee8675e7909af9e`. Command: `timeout 120 python3 -B verifiers/check_r75_routed_repairs.py --self-test --repo "$S/clone" --work "$S/work-r4"`. Output included `FAIL broken world survived: R4 closing line absent -> closed 4` and `FAIL broken world survived: R4 closing line precedes the pending text -> closed 4`, ending `self-test: 2 failure(s) over 27 assertions`; process exit `1`. The detector killed this mutant.

## Restoration

After restoring all mutated source lines, the counter hash returned to `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63`; `cmp` against the lane's committed counter returned exit `0`. The same restored `--self-test` returned `self-test: 0 failure(s) over 27 assertions`, exit `0`. Scratch directory removed and absence confirmed (`scratch_removed=yes`). No installs. Verification covered only the commands and results recorded above.

VERDICT: C2 claim data is not landed at HEAD 6523aced; R4 mutant killed, while R1 and R3 counter-guard mutants survived the self-test, exposing isolated-test coverage gaps.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w2/F08ChecktationTestC2.md