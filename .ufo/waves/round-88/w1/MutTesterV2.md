# MutTesterV2 — scoped findings (round 88, wave 1)

Full report: `.ufo/waves/round-88/w1/MutTesterV2/report.md`. Verdict table: `MutTesterV2/mutants.tsv`.

- C2 `check_r86_routed_repairs_v2.py`: 6 of 6 mutants KILLED (n1 drop (i), n2 drop (ii), n3 subset→superset, n4 exit 0 on D5 FAIL, n5 hardcoded D5 PASS, n6 integrity script from the worktree). No survivor. n4 and n5 are caught only by controls outside the committed self-test.
- C1 `check_omp_root_semantics_v2.py`: 0 of 7 scored. `C1_READY` never appeared by the 45-minute cap. The counter's self-test raises `UnboundLocalError` at line 335 (`reader_grounded`, `last_absent` unassigned), so no mutant has a named-arm verdict. Owner: ExecLiveBound.
- The C2 self-test is red at the handoff: `1 failure(s) over 16 assertions` (`arm w_added_red`, the frozen control expects D5 FAIL via (ii); v2 reads PASS). `C2_READY` says it passes.

Scratch removed. Writes: `.ufo/waves/round-88/w1/MutTesterV2/` (report.md, mutants.tsv, c2_mutate.py, c2-rows.json, c1-selftest-baseline.txt) and this file.
