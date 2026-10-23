Result: DONE — Drafted Q34 and Q35 in the requested QUALITY table shape without editing product files.

## Proposed rows

| id | criterion | applies to | grounded in | supersedes |
|---|---|---|---|---|
| Q34 | Whenever append-only compliance is claimed for `corpus/SOURCES.md`, `verifiers/check_sources_append_only.py` is run over the claimed range and returns 1 for a protected-cell rewrite or removed row and 0 for permitted-cell-only changes, with the `anchor in place` self-test arm and routed red run on `e792607e` recorded as evidence it can fail. | `corpus/SOURCES.md` history and append-only claims | M45 `append-only-breach` (`corpus/lessons/round-54.md` § Mistakes) | — |
| Q35 | Every verifier is represented by exactly one matching `SKILL.md` § Gate registry row, each `gate` row declares a non-`none` backticked self-test flag present in that file, and `verifiers/check_gate_registry.py` is shown rejecting `none` with its `gate with self-test none` arm and the round-54 pre-patch 19-of-23 result. | verifier inventory and gate-registry self-test declarations | M47 `unregistered-gate` (`corpus/lessons/round-54.md` § Mistakes) | — |

## Evidence and scope

- M45: `corpus/lessons/round-54.md:13` records the protected-cell rewrites, identifies no prior criterion, and records `check_sources_append_only.py` returning exit 1 for the routed S050 anchor rewrite on `e792607e`; it also records the `anchor in place` self-test arm. `verifiers/check_sources_append_only.py:9-19,121-159,181-190` defines protected-cell/removal failures, the self-test arms, and exit codes.
- M47: `corpus/lessons/round-54.md:15` records the four gates lacking self-tests, no prior criterion, the registry gate's `gate with self-test none` arm, and the honest pre-patch registry result of 19/23. `verifiers/check_gate_registry.py:20-36,185-200,229-241,295-307` defines one-row-per-verifier conformance, the gate self-test requirement, its must-reject arm, and the failing exit condition.
- QUALITY table shape and existing sequential IDs: `corpus/QUALITY.md:10-11,43-44`; no Q34 or Q35 rows were added there.
- Touched surface: this report only, `.ufo/waves/round-55/build/ScribeQuality.md`. No product files were edited. No commands, tests, probes, or installs were run; this deliverable is a text-only draft.