# A20 FloorsGuard — falsify findings (Round-48 attempt 2)

Verdicts: **(a) CONFIRMED** — deleting the configured-root arm drops `harness_independent`
below its floor, 115, and the guard FAILs. **(b) CONFIRMED** — the guard notices a registry
floor lowered to 104 while both guard tables stay at 115: it fails loudly, exit 2, before any
self-test runs. **(c)** guard `--self-test` exits: pristine 0, under mutant A 0, under mutant B 0.

## Setup

- Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin` @ `84b9c9b` (read-only, untouched; no
  git/jj writes anywhere — all writes confined to the private clone).
- Private clone (gate work only): `/fast/scratch/hyaku/kotoba-r48-a2/seats2/KotobaR48.A20FloorsGuard/lane`
- Baseline hashes (pristine clone, sha256):
  - `verifiers/check_assertion_floors.py` = `5264fa2ee358b372b5dbbbee793b48b606a79a3b5a708a97de0449a7bb297a3c` (never modified)
  - `verifiers/verify_harness_independent.py` = `d67b1b6e9ba0e614f643adda2686c9db8d57c31741de01780be3fcb06c4f7937`
  - `verifiers/floors-registry.json` = `3bb49e967fd3ebfd2ff734f2d53dd6f7133e35f42c8bc707a90ce89f2618be65`

## Baseline (pristine)

- `python3 -B verifiers/check_assertion_floors.py` → `PASS harness_independent observed=115 floor=115`, exit **0**.
- `python3 -B verifiers/verify_harness_independent.py --self-test` → `0 failure(s) over 115 assertions`, exit **0**.

## (a) Delete the configured-root arm

Mutant: in the clone only, cut the entire round-48 (C1) configured-root self-test arm from
`verify_harness_independent.py` (comment block through the last `logsame` expectation, 99 lines).
The derive() enumeration is left in place — smallest behavior-bearing point that moves the count.

- Mutant hash (verify_harness_independent.py) = `bd9e571ffec5414919baeff9c028b1cc297398bfc029fe6e28bfa51cfaa0949c`
- `python3 -B verifiers/check_assertion_floors.py` →
  `FAIL harness_independent observed=104 floor=115` (all other instruments still PASS), exit **1**. KILLED.
- `python3 -B verifiers/verify_harness_independent.py --self-test` → `0 failure(s) over 104 assertions`, exit 0
  (arm gone cleanly; the count loss is exactly the ratchet's signal).
- Restoration: `git checkout -- verifiers/verify_harness_independent.py` in the clone →
  hash back to `d67b1b6e9ba0e614f643adda2686c9db8d57c31741de01780be3fcb06c4f7937`.

## (b) Lower floors-registry.json harness_independent to 104, tables stay 115

Mutant: clone's `floors-registry.json` `instruments.harness_independent.floor` 115 → 104; guard
tables (`EXPECTED_INSTRUMENTS`, `INSTRUMENTS`) untouched at 115.

- Mutant hash (floors-registry.json) = `0cecb95dba0183f02fe2fb6fcd9bd898ec2d4641f5a172eaa7b5caf933359049`
- `python3 -B verifiers/check_assertion_floors.py` →
  `FAIL registry floor drift: harness_independent registry=104 expected=115 row=115`, exit **2**.
  The guard notices (anchor cross-check fires before any instrument runs; no `PASS` line printed).
- Restoration: `git checkout -- verifiers/floors-registry.json` → hash back to `3bb49e96...`.

## (c) Guard --self-test exits

- Pristine (restored bytes): `0 failure(s) over 150 assertions`, exit **0**.
- Under mutant A (arm deleted): exit **0** (guard self-test is hermetic; doesn't read the target file).
- Under mutant B (registry 104): exit **0** (fixtures tolerate the half-bump; the live run still fails, exit 2).

## Conclusion

The landed ratchet holds against both probes: deleting the C1 configured-root arm is caught by the
count floor (104 < 115, exit 1), and a registry-only floor downgrade is caught by the anchor
cross-check (exit 2, named). The guard's own `--self-test` passes in every state tested.

Final clone state: `git status --short` empty; lane checkout untouched.
