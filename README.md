# kotoba-shokunin

**Prompt and skill craft — a `SKILL.md` is a loader contract.**

A **shokunin lane** minted and trained under the
[shokunin](https://github.com/VeigaPunk/shokunin) skill. Kotoba audits,
writes, and rewrites `SKILL.md` / `AGENTS.md` / dispatch prompts /
system prompts for trigger fidelity and decision density.

**Wiki:** [lane overview](https://app.devin.ai/org/veigapunk/wiki/VeigaPunk/kotoba-shokunin?branch=master)

## Domain

The frontmatter `description` is the only part any router ingests.
`SKILL.md` documents how the two harnesses here treat that field
differently (omp catalogue render vs cache-compressed one-liner vs
deterministic slice). Craft here is **audit-side**: sibling lanes own
the content of their own skills; kotoba reports, and fixes route to the
owning lane.

Triggers (from the skill frontmatter): "skill file", "SKILL.md",
"frontmatter description", "trigger words", "prompt craft", "write a
skill", "audit this skill", "skill quality".

Anti-triggers: general prompt engineering for model outputs (not skill
files), runtime code changes, and domain content inside a skill's
`reference/` tree.

## In this repository

```
PROVINCE.md     domain boundary
SKILL.md        loader-contract playbook
SHONEN.md  SCORECARD.md  LOG.md
corpus/         knowledge/, lessons/
verifiers/
  verify_skill_checklist.py
  verify_corpus_integrity.py
  verify_corpus_independent.py
  verify_surfaces.py
  verify_harness_claims.py
  fault_injection_corpus.sh
  fixtures/ + *-baseline.json
```

## Run the verifiers

From this repository root:

```bash
python3 verifiers/verify_skill_checklist.py
python3 verifiers/verify_corpus_integrity.py
python3 verifiers/verify_surfaces.py
python3 verifiers/verify_harness_claims.py
```

These prove checklist / corpus / surface contracts against frozen
baselines. They are not a live-session or native-judge pass.

## Adjacent

Measured effects of prompt format on *capability* belong to
[kengaku](https://github.com/VeigaPunk/kengaku-shokunin) until they
harden into reusable skill craft. Linguistic-cultural generation is
[kotodama](https://github.com/VeigaPunk/kotodama-shokunin).

## How a lane learns

Append-only corpus; every claim separates observation / inference /
unknown; rounds are non-author-verified. See the fleet
[README](https://github.com/VeigaPunk/shokunin#readme).
