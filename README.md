# kotoba-shokunin — prompt and skill craft

The question this lane answers is whether a `SKILL.md` or `AGENTS.md` says what it does: trigger fidelity, checklist fidelity, and the citation that backs a rule (`PROVINCE.md`, `SKILL.md`).

**Rank:** `SHONEN.md` boxes are `[~]`. Round 13 records that earlier `[x]` marks rested on subagents this lane dispatched, which `PROTOCOL.md` does not count as a non-author verifier, so the marks reverted. That is not a promotion.

## Owns / refuses

Owns the domain knowledge, playbooks, error patterns, and checklists for prompt and skill craft: `SKILL.md` / `AGENTS.md` quality and trigger fidelity (`PROVINCE.md`).

Refuses anything outside that domain. Cross-domain evidence is reported, not absorbed.

## Start here

`verifiers/verify_skill_checklist.py` is the machine check that every live checklist box in `SKILL.md` is executed, delegated, or recorded `unexecuted:<reason>`, against `verifiers/checklist-baseline.json` (`kotoba-checklist-v1`). The CLI is `build_parser()` in that file: default target is this repo's `SKILL.md`; `--self-test` asserts the checks on fixtures only and its exit code is not comparable to a live run; `--json` is machine-readable.

```sh
python3 verifiers/verify_skill_checklist.py
python3 verifiers/verify_skill_checklist.py --self-test
```

`verifiers/verify_harness_claims.py` documents a separate live-host check (`python3 verifiers/verify_harness_claims.py`, plus `--json` and `--self-test`). `verifiers/fault_injection_corpus.sh` documents `fault_injection_corpus.sh [--repo DIR] [--keep-worlds] [--self-test]`. Read the header: some faults are recorded blind spots, not must-fire cases.

## How to read the corpus

`corpus/README.md` is the index. Knowledge notes cite it by line (`corpus/README.md:35`, `:38`, `:40`, `:42` among others), so it was not reflowed. `corpus/knowledge/` holds the worked tables `SHONEN.md` says moved out of `SKILL.md` in round 15. `corpus/lessons/` holds round lessons. `verifiers/` holds the instruments and their baselines.

## Map

| Path | What it is |
|---|---|
| `PROVINCE.md` | Domain boundary |
| `SKILL.md` | Decision surface and checklists |
| `SHONEN.md` | Checklist, `[~]` after the author-attestation revert |
| `LOG.md` | Append-only record |
| `SCORECARD.md` | Axis verdicts |
| `AGENTS.md` | Operating rules |
| `corpus/` | Knowledge, lessons, index |
| `verifiers/` | Checklist, harness, corpus, and surface checkers |
| `plans/` | Round plans |
| `.ufo/` | Round machinery |

## Neighbors

kengaku keeps measured effects of prompt format and hands the reusable craft here (`kengaku-shokunin/PROVINCE.md` records that handoff). This lane does not absorb model-quality claims.

Fleet protocol: [VeigaPunk/shokunin](https://github.com/VeigaPunk/shokunin).
