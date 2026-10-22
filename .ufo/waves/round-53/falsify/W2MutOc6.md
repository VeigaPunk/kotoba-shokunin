Result: MIXED — Three OC-6 weakenings are killed; the exact `targets:["AGENTS.md"]` requirement can be removed without either frozen detector noticing.

## Baseline and detector

Scratch clone: `/fast/scratch/hyaku/kotoba-r53/w2/W2MutOc6`, checked out at `c775d6823bfca8f0de8c0874032a954438b38edc`. Target: `verifiers/verify_surfaces.py`. Pristine SHA-256: `f84d423ad3eddd4b2f594306212aec5d72093ef60ebcf3b7d4d541c1b5c4c37b`.

On pristine bytes:

- `python3 -B <scratch>/verifiers/verify_surfaces.py --self-test` → exit 0, `0 failure(s) over 155 assertions` (expected negative-fixture ERROR lines are part of the self-test).
- `python3 -B <scratch>/verifiers/verify_surfaces.py --json --repo <scratch>` → exit 0, `pass: 7`, `fail: 0`, `surfaces.opencode_extract: PASS`; measured opencode SHA-256 `538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7`.
- Target-mismatch probe (a scratch copy of the 1.19.4 anchors with line 31 changed to `targets:["OTHER.md"]`): same JSON gate → exit 1; `surfaces.opencode_extract: FAIL`, OC-6 unmatched.

Each mutation was applied and restored separately. `before SHA → mutant SHA → restored SHA`:

| Mutant | SHA-256 | Result and evidence |
|---|---|---|
| Drop registered-layer dependency check: replace the `builtins_re.search(...)` guard in `opencode_context_layer_matches` with unconditional acceptance after the instruction-context instance is found (`verify_surfaces.py:739-746`). | `f84d423a…c37b` → `6a13620109a3ea9aaee1e0be06ee5a8ab72f4046afb03c76f7efcea3d001d4d5` → `f84d423a…c37b` | **KILLED / HOLDS.** Self-test exit 1: `3 failure(s) over 155 assertions`; `strings-opencode-1.19.4-decoy-oc6.txt` was expected to exit 1 but got 0, and the “only OC-6 unmatched” assertion failed. The full live gate still exited 0, pass 7/7. Running the gate on that dependency-decoy fixture also exited 0, pass 7/7, exposing the weakened rule which the self-test catches. |
| Accept the `"core/instructions"` literal alone: add an early return before the structural checks (`verify_surfaces.py:711-715`). | `f84d423a…c37b` → `ebf908c159a101855797c8628fc17edac76a5b16a6bcd0ba59f8fdd01146e907` → `f84d423a…c37b` | **KILLED / HOLDS.** Self-test exit 1: `3 failure(s) over 155 assertions`; the OC-6 dependency-decoy expected exit 1 but got 0. Full live gate exited 0, pass 7/7; the same decoy gate exited 0, pass 7/7. |
| Accept `Key.make` only, rejecting 1.19.4's `Wr.make` (`verify_surfaces.py:630-633`). | `f84d423a…c37b` → `5e1031b2e57075c5fe9128350cdb80aaea20644bf983f44180a0ce9ea53d567e` → `f84d423a…c37b` | **KILLED / HOLDS.** Self-test exit 1: `3 failure(s) over 155 assertions`, including `oc-1.19.4 anchors: exit 0: got 1`. The full live gate exited 1, `pass: 6`, `fail: 1`, with `surfaces.opencode_extract: FAIL` because OC-6 no longer matched. The 1.19.4 anchor-fixture gate likewise exited 1 with OC-6 FAIL. |
| Drop the exact target requirement by weakening `OC_V2_TARGETS_RE` to match only `.up({` (`verify_surfaces.py:641-643`). | `f84d423a…c37b` → `992f3b6f0c5f169fa19cb89e5631d85e95e6979b8b4c9d1ce5f91790595f5191` → `f84d423a…c37b` | **SURVIVED / BREAKS. Severity: moderate coverage gap.** Self-test exit 0, `0 failure(s) over 155 assertions`; full live gate exit 0, pass 7/7. The wrong-target probe also changed from pristine exit 1 / OC-6 FAIL to mutant exit 0 / pass 7/7. This is a false-positive path if the target matcher is weakened: neither the frozen self-test nor host gate detects it. The self-test currently checks dropped OC-6 anchors and the dependency decoy (`verify_surfaces.py:1596-1635`), but has no wrong-target OC-6 negative case.

## Restoration

After every mutation, the self-test, full host gate, and corresponding probe returned to their pristine results. Final target SHA-256 and the preserved pristine copy both equal `f84d423ad3eddd4b2f594306212aec5d72093ef60ebcf3b7d4d541c1b5c4c37b`. The final wrong-target probe again exited 1 with OC-6 unmatched. All mutated and diagnostic bytes stayed inside the assigned scratch clone; the lane target was not edited.