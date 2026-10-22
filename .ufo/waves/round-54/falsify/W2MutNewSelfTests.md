Result: MIXED — all four self-tests killed at least one judgment mutant, but 8 of 16 mutants survived.

## Method and baseline

Used the isolated clone `/fast/scratch/hyaku/kotoba-r54/W2MutNewSelfTests` at `58db81c4465b0e9b07ef2485b87d8970683afac6`. `git show --format= --stat b55550b9bf3916e5d11a8b596ac92f0dbce9e681` confirmed the four named verifier files were changed by that commit. Each of the 16 mutants below changed one point in judgment code; no self-test code was mutated. For each, I ran its named `--self-test`, then restored the source and reran the same detector. A mutant was killed when the self-test exited nonzero; otherwise it survived.

Pristine self-test command for each file was `python3 -B verifiers/<file> --self-test`; all returned exit 0:

- `box_proof_case_deletion.py`: `self-test: 0 failure(s) over 10 assertions`
- `check_alwayson_boxes.py`: `self-test PASS: counted box exit 0; missing delegate exit 1`
- `check_callee_rename.py`: `PASS self-test robust case: strings-omp-clean.txt exit=0 finding=omp:rnplant/RNPLANT.md`; `PASS self-test non-robust case: strings-omp-clean.txt exit=1 finding=self-test injected suppression`; `self-test: 0 failure(s) over 2 assertions`
- `check_opencode_repin.py`: `0 failure(s) over 2 assertions`

`Expected detector` for every row is that same per-file `--self-test` exits 1 on the introduced judging defect. Outputs below are actual stdout and exit codes; each mutation hash is the hash of the modified script at detector time.

## `box_proof_case_deletion.py` — killed 3/4

Pristine/restored SHA-256: `d85eb20e63b1d394b7f080ca16b2dbe974d8c8c226e7c82256c30f9b32959447`.

| Mutant (judging location) | Mutant SHA-256 | Detector output / exit | Verdict |
|---|---|---|---|
| At `verifiers/box_proof_case_deletion.py:202`, classify exit 0 as `killed` instead of `survived`. | `ae0f54a7da79daec499010f14d1a5efea818428ad8704dc87f8438876976a6f6` | `FAIL surviving control finding is stable: got False, expected True`; `FAIL incomplete fixture returns failed: got 0, expected 1`; `FAIL surviving deletion finding is stable: got False, expected True`; `FAIL incomplete fixture summary: got 'killed 6 of 6', expected 'killed 5 of 6'`; `self-test: 4 failure(s) over 10 assertions`; exit 1. | Killed |
| At `...:204`, classify a non-1 exit as `survived` rather than `error`. | `53f12ef7ae1da0d1b5d650b043c2cfdb68bd21b2784ffe3ce981d126e2745897` | `self-test: 0 failure(s) over 10 assertions`; exit 0. | **Survived** — fixture cases produce only exit 0 or 1, so this branch is not exercised. |
| At `...:205-206`, force the `proven` test false. | `0536a44b6561027dd8f540133ada83ec8614a60997adbf4c2a9a69c37e297f90` | `FAIL complete fixture returns clean: got 1, expected 0`; `FAIL killed finding is stable: got False, expected True`; `FAIL complete fixture summary: got 'killed 0 of 6', expected 'killed 6 of 6'`; `FAIL another deletion is still killed: got False, expected True`; `FAIL incomplete fixture summary: got 'killed 0 of 6', expected 'killed 5 of 6'`; `self-test: 5 failure(s) over 10 assertions`; exit 1. | Killed |
| At `...:207`, force the named-diagnostic test false. | `360d12cd9617c6851c68acfa5f028aa295ba94c7ee51e396e62d174b08b98f51` | Same five failure lines and summary as the preceding mutant; exit 1. | Killed |

## `check_alwayson_boxes.py` — killed 3/4

Pristine/restored SHA-256: `7d989ed4ae85375ffd3c5786543b810b93820e823132ec1da104f18e8eb19f47`.

| Mutant (judging location) | Mutant SHA-256 | Detector output / exit | Verdict |
|---|---|---|---|
| At `verifiers/check_alwayson_boxes.py:196`, drop the subprocess exit-code comparison and judge only the JSON status. | `707cae80728b14c47daaf08c14127c0c6441b427b263d0afa061606d193ace85` | `self-test PASS: counted box exit 0; missing delegate exit 1`; exit 0. | **Survived** — tested delegates return the expected status and code together; there is no status/code disagreement case. |
| At `...:239`, invert the `if bad` branch. | `7cf1cd67b14bbf0eed6663acd138977659dd659896c697ea598fc15274f546e4` | `self-test failed: counted`; `always-on boxes executed and discriminating 0 of 2`; both boxes say `not counted (0 of 6 cases wrong: )`; exit 1. | Killed |
| At `...:243`, do not increment the counted-box total. | `b986fbe2ea054807f7b554fc2b34db51e62e46a0e747d1667cdecb50f04120f3` | `self-test failed: counted`; summary says `discriminating 0 of 2`; both boxes still say `counted (6 of 6 cases as pinned)`; exit 1. | Killed |
| At `...:250`, invert the final exit-code decision. | `d0f12d84ca38b9095f0c728a696b8381397f9d0bbb09bdf81cfa451aaabaa17a` | `self-test failed: counted`; output says `discriminating 2 of 2` and both boxes counted; exit 1. | Killed |

## `check_callee_rename.py` — killed 1/4

Pristine/restored SHA-256: `30a17b8f83fa2fb716655e6b32aabe8d94b44ef4c2ca700ce7340ccae955f962`.

| Mutant (judging location) | Mutant SHA-256 | Detector output / exit | Verdict |
|---|---|---|---|
| At `verifiers/check_callee_rename.py:142`, let `both_pass` check only exit code 0, not the required PASS lines. | `ab2fe40e555cfe0a6175cc1d8507c68d8d7ef45acd3c6ce906a9e52807cb2ab2` | Both self-test cases printed `PASS`; `self-test: 0 failure(s) over 2 assertions`; exit 0. | **Survived** — no case has exit 0 with a missing required PASS line. |
| At `...:267-268`, judge the planted run by exit 1 alone. | `d4a410cc907890f811055af16f4388cd82d5ab58cd24aba757c907bb63a4412e` | Both self-test cases printed `PASS`; `self-test: 0 failure(s) over 2 assertions`; exit 0. | **Survived** — the injected suppression returns exit 0, while the normal planted run has the expected finding. |
| At `...:268`, remove the required `PLANT_ID` test from the planted-run judgment. | `58210083786cd8ec68123a3da6325e1a42bb09aa66422761fc1de6b1654c72c0` | Both self-test cases printed `PASS`; `self-test: 0 failure(s) over 2 assertions`; exit 0. | **Survived** — the robust fixture separately contains the expected ID, and the suppression fixture has exit 0. |
| At `...:272`, compute robustness without `ok_b`. | `5ac1ba488070e7fb445b9f4f0f1f75228365c3c3a66729b01e1bb83bcb53b6ae` | `PASS self-test robust case: strings-omp-clean.txt exit=0 finding=omp:rnplant/RNPLANT.md`; `FAIL self-test non-robust case: strings-omp-clean.txt exit=0 finding=self-test injected suppression`; `self-test: 1 failure(s) over 2 assertions`; exit 1. | Killed |

## `check_opencode_repin.py` — killed 1/4

Pristine/restored SHA-256: `5cff0fedd41f05698edbb38866fd556718bd6ad1f67c08b5f313d38d0d1bec1b`.

| Mutant (judging location) | Mutant SHA-256 | Detector output / exit | Verdict |
|---|---|---|---|
| At `verifiers/check_opencode_repin.py:81`, accept every class, not just `harness == "opencode"`. | `0441aba9a2d10d9d8cc962d6a10c572c8724155f9f5304430c90afad8b2867a2` | `0 failure(s) over 2 assertions`; exit 0. | **Survived** — the fixture contains only an opencode class. |
| At `...:83`, omit `verdict` from the extracted class tuple. | `44abe5c4befa17b97c677426d67861284a06e99f5f4d1b0db00dac7db392b16e` | `0 failure(s) over 2 assertions`; exit 0. | **Survived** — both base and revision are parsed by the same weakened projection. |
| At `...:231`, count any present class ID as kept without comparing its fields. | `f2b7bac3f3d21165d12462ee4e4aebf29f348340a0b623a6d8dd0ad407ddb1df` | `0 failure(s) over 2 assertions`; exit 0. | **Survived** — the retirement fixture removes the class rather than keeping it with changed fields. |
| At `...:253`, invert the final exit-code result. | `c2535859f96e562f085df2a688db74ee26cfc48821b28c5ea5de32098e188796` | `FAIL retained class is clean: (1, 'opencode re-pin: surfaces pass 7 of 7 (opencode_extract PASS); pins OK 3/3; opencode classes kept 1 of 1; self-test 0 failure(s) over 129 assertions…')`; `FAIL retired class is failed with stable finding: (0, 'opencode re-pin: surfaces pass 6 of 7 (opencode_extract FAIL); pins OK 3/3; opencode classes kept 0 of 1; self-test 0 failure(s) over 129 assertions…')`; `2 failure(s) over 2 assertions`; exit 1. | Killed |

## Restoration evidence

After **each** mutation, the source was restored and that file's `--self-test` rerun. Every restored run returned exit 0 with the same pristine output listed above. SHA-256 before mutation and after restoration matched for all four files: `box_proof_case_deletion.py` `d85eb20e63b1d394b7f080ca16b2dbe974d8c8c226e7c82256c30f9b32959447`; `check_alwayson_boxes.py` `7d989ed4ae85375ffd3c5786543b810b93820e823132ec1da104f18e8eb19f47`; `check_callee_rename.py` `30a17b8f83fa2fb716655e6b32aabe8d94b44ef4c2ca700ce7340ccae955f962`; `check_opencode_repin.py` `5cff0fedd41f05698edbb38866fd556718bd6ad1f67c08b5f313d38d0d1bec1b`. Thus the scratch sources were byte-identical to their pristine state at completion.

Each self-test killed at least one mutant, so none was hollow by the stated zero-kills criterion. The survivors show specific untested judging boundaries, most notably only 1/4 mutants killed by each of the callee-rename and opencode-repin self-tests.