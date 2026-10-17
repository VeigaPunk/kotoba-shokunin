# kotoba-shokunin — 言葉

**Prompt and skill craft.** A `SKILL.md` is a loader contract. The
frontmatter `description` is the only part most routers ingest; the body
is the operating manual a fresh agent must be able to execute without
oral context.

A **shokunin lane**: an expert agent for one domain, minted and trained
under the [shokunin skill](https://github.com/VeigaPunk/shokunin).
Rank: **shonen**. Promotion is a named non-author review of
[`SHONEN.md`](SHONEN.md), never self-attestation.

This lane answers: *will this skill fire when it should, stay silent
when it shouldn't, and can every checklist box be executed, delegated,
or honestly marked unexecuted?*

## Domain

From [`PROVINCE.md`](PROVINCE.md): `SKILL.md` / `AGENTS.md` quality,
trigger fidelity, dispatch prompts, system prompts. Sibling domain
lanes own their own `SKILL.md` *content* — this lane audits and
reports; fixes route to the owner.

Not general prompt-engineering for model outputs. Not runtime code
changes. Not the domain material inside a skill's `reference/` tree.

## What's here

| Path | Role |
|---|---|
| [`SKILL.md`](SKILL.md) | trigger-fidelity craft, harness differences (omp truncator vs compressor), checklists |
| [`PROVINCE.md`](PROVINCE.md) | domain boundary |
| [`verifiers/`](verifiers/) | machine checks for checklist fidelity, surfaces, corpus integrity |
| [`corpus/`](corpus/) | knowledge and lessons |
| [`SCORECARD.md`](SCORECARD.md) · [`LOG.md`](LOG.md) · [`SHONEN.md`](SHONEN.md) | axes, trail, promotion |

## The gate

```sh
python3 verifiers/verify_skill_checklist.py
python3 verifiers/verify_skill_checklist.py --self-test
python3 verifiers/verify_surfaces.py
python3 verifiers/verify_corpus_integrity.py
```

Checklist boxes in `SKILL.md` are pinned by sha256 of normalised text
in `verifiers/checklist-baseline.json`. A reworded, added, or removed
box fails the run. That is the point.

## How a lane learns

Append-only corpus; every claim separates observation / inference /
unknown; rounds are non-author-verified. See the fleet
[README](https://github.com/VeigaPunk/shokunin#readme).
