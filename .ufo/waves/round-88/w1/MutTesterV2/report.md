# MutTesterV2 — round 88 mutation report

Seat: MutTesterV2 (attack seat). Scope: mutants of the two v2 instruments, scored in scratch copies only.
Lane HEAD during the run: `89579c7` (plan freeze). Frozen tip used for all controls: `4df1e8005016c75390a5e06b209462df58c95918`.

## Verdicts

| Instrument | Mutants | KILLED | SURVIVED | NOT_SCORED |
|---|---|---|---|---|
| C2 `verifiers/check_r86_routed_repairs_v2.py` (sha256 `10bd5508…8b82`) | n1–n6 | **6** | 0 | 0 |
| C1 `verifiers/check_omp_root_semantics_v2.py` (sha256 `506a2ba9…4beb`) | m1–m7 | 0 | 0 | **7** |

Kill count: **6 of 13** mutants killed; 7 not scored (C1 instrument not ready, see F4).

## Method

- Each mutant is a copy of the v2 file with one exact, uniqueness-checked string replacement, placed in a scratch `verifiers/` with a copy of the byte-frozen r87 counter it imports (`c2_mutate.py`, committed beside this report).
- Signature per copy: `--self-test` output, controls C-a…C-d (`check_d5` on the four frozen worlds built with the copy's own fixture helpers), driver exits (`main` with D1–D4 stubbed True and the real D5) on the silenced and tip worlds, and the real CLI at the frozen tip.
- KILLED iff the signature differs from the unmutated baseline's signature; the differing items name the catching arm or control.
- Caveat: the baseline is not a green instrument. It already fails its own self-test (1 failure) and its frozen control C-a. KILLED here means "an observable change", and the table in `mutants.tsv` names the arm.

## C2 results

| Mutant | Mutation | Verdict | Catching arm / control |
|---|---|---|---|
| n1 drop (i) | `identity_holds` → True | KILLED | self-test: `arm (i) identity: a silenced check … fails`, `a renamed check … fails`, `arm w_silenced … via (i)`; control C-b reads PASS (expected FAIL) |
| n2 drop (ii) | `monotone_holds` → True | KILLED | self-test: `arm (ii) monotone: a new DRIFT name fails`, `arm w_newname … via (ii)` |
| n3 subset → superset | `base <= rev` | KILLED | self-test: `arm (ii) strict subset`, `arm w_healed`, `new DRIFT name`, `w_newname`, `w_silenced monotone-only`; control C-c (healed) reads FAIL (expected PASS) |
| n4 exit 0 on D5 FAIL | `main` returns 0 when D5 fails | KILLED | **not** the self-test (no new failing arm). Driver control `drv_silenced`: exit 0, expected 1 |
| n5 hardcode D5 PASS | `check_d5` returns True | KILLED | **not** the self-test. Control C-b: `check_d5` on silenced reads PASS, expected FAIL |
| n6 integrity from worktree | integrity script read from lane path, not the `<rev>` scratch tree | KILLED | self-test: `arm w_silenced … via (i)`, `arm w_garbage`, `arm w_newname`, `arm w_added_red` detail; control C-b |

No C2 survivor. Two kills (n4, n5) are caught only by controls outside the committed self-test. See F2.

## C1 results

Not scored. The v2 counter's own `--self-test` raises `UnboundLocalError` (see F3 and `c1-selftest-baseline.txt`), so no mutant can produce a named-arm verdict. A crash is not a kill, so I did not count one. Mutants m1–m7 are listed as `NOT_SCORED` with the reason.

## Findings

- **F1 (C2 handoff contract).** `C2_READY` says the v2 gate's self-test passes. The baseline self-test prints `1 failure(s) over 16 assertions`, with `FAIL arm w_added_red (frozen control)`. The frozen control C-a expects D5 FAIL via (ii). v2 reads PASS on that world because (ii) compares names, and an added instance of a name already DRIFT is invisible to it (the counter's own docstring says so). The executor disclosed this as "F1". The frozen control is not met by the counter. The plan's kill rule and predicate are for the integrator and the attack seats to rule on; I did not rescue them.
- **F2 (C2 self-test coverage gap).** The committed self-test asserts (i) and (ii) as pure functions, and `check_d5` only on `w_tip`. It has no arm for `check_d5` on `w_silenced` or `w_added_red`, and no arm for the driver's exit code. So a hardcoded D5 PASS (n5) and an exit 0 on D5 FAIL (n4) both leave the self-test at `1 failure(s) over 16 assertions`, unchanged. The frozen controls catch them, but the self-test cannot gate them.
- **F3 (C1 counter crash, blocking).** `check_omp_root_semantics_v2.py:335` (`reader_grounded`) uses `last_absent` in the refusal message, but it is assigned only inside the loop after the join-token `continue`. When every occurrence of a reader quote lacks a join token, the function raises `UnboundLocalError` rather than returning a refusal. The crash reaches `self_test` (line 914, via `world` and `score`, line 829/631) and the tip run (line 1074). An unhandled exception exits 1, which is outside the frozen exit ladder (0 pass / 1 content fail / 2 could-not-evaluate). Owner: ExecLiveBound.
- **F4 (C1 handoff never written).** `C1_READY` did not appear by the 45-minute cap (about 06:43 local). The v2 file did exist (1129 lines), but F3 means its self-test is red. I did not run C1 mutants against it.
- **F5 (lane HEAD).** `git -C` the lane shows HEAD `89579c7` (plan freeze), with tip `4df1e80` one commit behind. Controls used `4df1e80` explicitly.

## Risks

- C1 has no verdict. Until ExecLiveBound fixes F3 and writes `C1_READY`, m1–m7 are unscored.
- The C2 kill count is "observable change vs baseline", not "correct verdict", because the baseline already fails C-a. A reviewer who reads C-a as a gate should not read the kill count as a pass.
- Only C2's committed self-test is shown to be red. The C2 controls (C-b, and the driver exit) are my own harness, built from the frozen fixture worlds in the self-test. They are not in the committed file.

## Evidence

- `c2_mutate.py` (harness), `c2-rows.json` (per-mutant signatures), `mutants.tsv` (verdict table), `c1-selftest-baseline.txt` (C1 traceback, `exit=1`).
- Baseline C2 self-test: `1 failure(s) over 16 assertions`; baseline C2 CLI at `4df1e80`: `r86 routed defects closed 5 of 5`, exit 0.
- Baseline C2 controls: C-a PASS (want FAIL), C-b FAIL (want FAIL), C-c PASS, C-d PASS; driver `drv_silenced` exit 1 (`4 of 5`), `drv_tip` exit 0 (`5 of 5`).
- Tools installed: none.
