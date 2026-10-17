# kotoba-shokunin — 言葉

**Prompt and skill craft.** A `SKILL.md` is a loader contract. The
frontmatter `description` is the only part most routers ingest. Kotoba
audits, writes, and rewrites skills, `AGENTS.md`, dispatch prompts, and
system prompts for trigger fidelity and decision density.

This is a **shokunin lane** of the [shokunin fleet](https://github.com/VeigaPunk/shokunin).
Rank: **shonen**.

## The craft

- Frontmatter `description` is the trigger surface. Body tables are for
  the agent that already loaded; they do not reach the `<skills>`
  catalogue.
- On omp, the catalogue render is `cache.get(key) ?? slice(0, 99)…`
  (`SKILL.md`). Cache rows are keyed by `(name, description-as-loaded)`
  and never pruned — a count is not a coverage meter.
- Sibling `*-shokunin` skills own their own `SKILL.md` *content*. This
  lane audits and reports; fixes route to the owning lane.
- The shokunin files are not in an omp skill-discovery root, so their
  descriptions never reach the router. Craft here is audit-side, not
  router-visible.

Anti-triggers (from the skill frontmatter): general prompt engineering
for model outputs that are not skill files; runtime code changes; domain
content inside a skill's `reference/` tree.

## Province

Owns: `SKILL.md` / `AGENTS.md` quality, trigger fidelity, dispatch-prompt
and system-prompt craft.

**Refuses:** absorbing another lane's domain content "to fix the skill"
(report the audit; the owner lands the fix), model-quality claims
(kengaku), serving identity (kama). Out of province → report, never
absorb.

See [`PROVINCE.md`](PROVINCE.md).

## What's in this repository

```
kotoba-shokunin/
├── SKILL.md              loader-contract playbook, harness differences, checklists
├── PROVINCE.md
├── SHONEN.md             promotion checklist (marks here are author-asserted until a named non-author)
├── LOG.md
├── SCORECARD.md
├── AGENTS.md
├── plans/
├── verifiers/
│   ├── verify_skill_checklist.py
│   ├── verify_surfaces.py
│   ├── verify_corpus_integrity.py
│   ├── verify_corpus_independent.py
│   ├── verify_harness_claims.py
│   ├── fault_injection_corpus.sh
│   └── fixtures/ + *-baseline.json
└── corpus/
    ├── knowledge/
    └── lessons/
```

## Start here

```sh
python3 verifiers/verify_skill_checklist.py
python3 verifiers/verify_surfaces.py
python3 verifiers/verify_corpus_integrity.py
python3 verifiers/verify_harness_claims.py
```

These verifiers pin claims in *this* repo's skill and corpus. They do
not rewrite a sibling's `SKILL.md`. Read [`SKILL.md`](SKILL.md) before
auditing anyone else's.

## How a round works

One axis-move, typically depth + consistency. Lane identity:
`kotoba-shokunin <kotoba@shokunin.local>`.

## Fleet

[VeigaPunk/shokunin](https://github.com/VeigaPunk/shokunin) ·
[kimi-shokunin](https://github.com/VeigaPunk/kimi-shokunin)
