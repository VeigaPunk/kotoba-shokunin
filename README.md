# kotoba-shokunin

Prompt and skill craft: auditing, writing, and rewriting `SKILL.md`,
`AGENTS.md`, dispatch prompts, and system prompts so the trigger fires
on the work it names and stays quiet on the work it does not.

The lane audits a skill and reports. It does not take ownership of
another lane's domain content. A fix to kagi's, kake's, kasegi's,
kengaku's, or kumitate's `SKILL.md` is routed to that lane. General
prompt engineering for model outputs, runtime code changes, and the
insides of a skill's `reference/` tree are outside the trigger.

## The job

`PROVINCE.md` scopes the lane to `SKILL.md` / `AGENTS.md` quality and
trigger fidelity. `SKILL.md` is the playbook: when a description is doing
its job, how a decision table should be shaped, and which failures are
recurring. The instruments that check those claims live in `verifiers/`.

`verifiers/verify_skill_checklist.py` is the machine check for checklist
fidelity. Its docstring states the claim under test: every checkbox in a
`SKILL.md` is executed by the instrument, delegated to a named instrument,
or recorded `unexecuted:<reason>`, and `verifiers/checklist-baseline.json`
covers every live box once, pinned by the sha256 of the box text. A
reworded, added, or removed box fails the run. Read the docstring for the
arguments; the baseline file is the map.

Sibling verifiers in the same directory check corpus integrity, harness
claims, and surface pins (`verify_corpus_integrity.py`,
`verify_corpus_independent.py`, `verify_harness_claims.py`,
`verify_surfaces.py`). Fixtures and baselines sit beside them.

## Read this first

1. [`PROVINCE.md`](PROVINCE.md) — the boundary in one paragraph.
2. [`SKILL.md`](SKILL.md) — triggers, anti-triggers, and the craft rules.
3. [`corpus/README.md`](corpus/README.md) — what has been admitted.
4. [`verifiers/verify_skill_checklist.py`](verifiers/verify_skill_checklist.py) — the checklist contract, in the module docstring.

## On disk

| Path | Role |
|---|---|
| `SKILL.md` | The craft manual, including its own frontmatter description. |
| `PROVINCE.md` | Domain and refusal. |
| `verifiers/` | Checklist, corpus, harness, and surface instruments, plus their baselines. |
| `corpus/` | Knowledge and lessons. |
| `plans/` | Round plans. |
| `SHONEN.md` | Promotion checklist. Rank is shonen. |
| `LOG.md`, `SCORECARD.md` | Audit trail and axis verdicts. |

## Fleet

Protocol and roster: [shokunin](https://github.com/VeigaPunk/shokunin).
Roster id `kotoba`, rank **shonen**.
