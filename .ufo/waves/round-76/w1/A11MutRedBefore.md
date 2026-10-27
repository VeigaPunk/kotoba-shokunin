# A11MutRedBefore — red-before findings

The prescribed `--shared` worktree creation was rejected (`git worktree add: unknown option 'shared'`, exit 129). Used the permitted shared clone instead at `/fast/scratch/hyaku/kotoba-r76/A11MutRedBefore`, detached at base `b7f13f4b39cbd43076a85568adca763a6f674e7a`; removed scratch afterward.

Executed exact requested counters at both revisions:

- `python3 -B verifiers/check_desc_craft.py --rev b7f13f4b39cbd43076a85568adca763a6f674e7a` — output: `python3: can't open file '/fast/scratch/hyaku/kotoba-r76/A11MutRedBefore/verifiers/check_desc_craft.py': [Errno 2] No such file or directory`; exit 2.
- `python3 -B verifiers/check_r75_routed_repairs.py --rev b7f13f4b39cbd43076a85568adca763a6f674e7a` — same missing-file error for that path; exit 2.
- `python3 -B verifiers/check_desc_craft.py --rev abd8e5cfd45ea3863b344ac58a187b0c5de620d0` — same missing-file error; exit 2.
- `python3 -B verifiers/check_r75_routed_repairs.py --rev abd8e5cfd45ea3863b344ac58a187b0c5de620d0` — same missing-file error; exit 2.

Verdict: **INCONCLUSIVE**. Neither counter exists at the designated base checkout, so the expected `0 of 6` / `0 of 4`, exit 1 red-before observations could not be made. No mutation was performed; byte hashes/restoration are not applicable. No tool installed.