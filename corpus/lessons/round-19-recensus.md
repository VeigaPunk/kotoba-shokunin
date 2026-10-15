# round-19 re-census — vacuous permission comparator tightened; live harness excluded

2026-10-14. Steered round 19. Advisory inventories:
`../.ufo/waves/shokunin12h-20261014-p1-repair/members/Kotoba*.md`.

## Landed change (one file, 2 lines)

`verifiers/verify_harness_claims.py`: `oc.permission.skill_lines` and
`oc.permission.skill_allow` move from `at_least` to `equal` in `CHECKS`.
`expect` stays `0`. With `at_least` and expect 0 any non-negative count passed —
a vacuous assertion. The baseline JSON's documentary `"mode"` string is not
read by `evaluate()` (the comparator mode comes from `CHECKS[cid][0]`), so the
runtime fix is authoritative; the stale metadata string is recorded here rather
than edited.

## Verdict lines (measured)

- `python3 verifiers/verify_corpus_integrity.py` → exit 0, `9/9 checks pass`.
- `python3 verifiers/verify_surfaces.py` → exit 0 (7/7 checks).
- `python3 verifiers/verify_corpus_independent.py` → exit 0.
- `bash verifiers/fault_injection_corpus.sh --self-test` → OK.
- `python3 verifiers/verify_harness_claims.py --self-test` → 0 failures over 10
  assertions. The **live** run is excluded: it reads real `~/.omp` session JSONL.

## Named debt

- `verify_skill_checklist.py` → exit 1, `FAIL trigger.line_budget: evaluated
  601 — 601 lines exceed budget 600`. **Pre-existing on HEAD** (SKILL.md is not
  touched by this wave); do not raise the budget to go green.
- `SKILL.md` still teaches the v1 opencode model; lowercase
  `/home/vgpnk/projects/...` cites remain; harness-verifier count prose is stale.

## Independent audit erratum (appended 2026-10-14)

Independent audit: integrity 9/9, independent exit 0, fault-injection self-test OK after the index row and tracked-file pin refresh; the live harness verifier was excluded (reads real `~/.omp` sessions). Identity/pathspec/record confirmed. The audit DISAGREED with the parent pre-integration numbers because the round lesson was itself unindexed at that moment — fixed here (`corpus/README.md` row + `corpus.index.tracked_files` 47→48 with a recorded rationale). Remaining red: `trigger.line_budget` 601>600 (pre-existing; do not raise the budget). Named debt: stale v1 opencode prose, lowercase path cites, baseline documentary mode strings.
