# kotoba-shokunin

Prompt and skill craft: `SKILL.md`, `AGENTS.md`, dispatch prompts, and
system prompts, judged by trigger fidelity and decision density.

Rank: **shonen**. [`SHONEN.md`](SHONEN.md) holds `[~]` on its boxes. The
file itself explains why earlier `[x]` marks were reverted: a subagent
the lane dispatched is still the lane.

Fleet: [shokunin](https://github.com/VeigaPunk/shokunin).

## The question

> Does the frontmatter description actually route this skill, and can a
> fresh agent execute the body without oral context?

On the omp harness, the description is the only text the skills catalogue
ingests, and it may be a cached one-line compression or a hard truncation.
`SKILL.md` is the measured account of that loader contract, including the
dates the cache counts were taken. Those counts are time-varying; the
skill says to re-read `LOG.md` before quoting one.

## Boundary

**Owns:** the craft of auditing and rewriting skill files, agent
definitions, and dispatch prompts, plus the verifiers that pin this
lane's own claims.

**Hands off:** the domain content inside a sibling's skill. Kotoba audits
and reports. Fixes route to the owning lane (kagi, kake, kasegi, kengaku,
kumitate, and the later siblings). General prompt engineering for model
outputs, and runtime code changes, are outside this province.

## Verifiers

[`verifiers/`](verifiers/) holds the executable checks. Representative
entry points:

```sh
python3 verifiers/verify_corpus_integrity.py
python3 verifiers/verify_harness_claims.py
python3 verifiers/verify_skill_checklist.py
python3 verifiers/verify_surfaces.py
```

`verify_corpus_integrity.py` pins the corpus index and pointer
resolution (its docstring lists each check id). The other three pin
harness claims, the skill checklist, and surface descriptions.
`fault_injection_corpus.sh` is the fault-injection driver beside them.
Baselines (`baseline.json`, `checklist-baseline.json`,
`corpus-baseline.json`, `surfaces-baseline.json`) are the pins those
verifiers read.

## Map

| Path | What it is |
|---|---|
| [`SKILL.md`](SKILL.md) | loader contract, fidelity checklists, decision surface |
| [`PROVINCE.md`](PROVINCE.md) | prompt and skill craft, trigger fidelity |
| [`corpus/knowledge/`](corpus/knowledge/) | worked tables moved out of the skill, with pointers |
| [`corpus/README.md`](corpus/README.md) | coverage index |
| [`LOG.md`](LOG.md), [`SCORECARD.md`](SCORECARD.md) | rounds and axis verdicts |

A number printed in the skill is quoted with the revision it was measured
at. Recompute with the command the skill prints before citing the count.
