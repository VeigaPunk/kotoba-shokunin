# kotoba-shokunin

Prompt and skill craft — trigger fidelity, decision density, and claims
that say only what they can support.

A `SKILL.md` here is a loader contract. The frontmatter `description` is
the part a router actually ingests. Kotoba audits that contract, the
decision tables under it, and the citations that keep the tables honest.
Sibling lanes own the content of their own skills. This lane audits and
reports; the fix routes home.

Rank: **shonen**. `SHONEN.md` is still here. Registered in the fleet
`MANIFEST.json` roster since 2026-09-28.

## Province

**Owns.** `SKILL.md` / `AGENTS.md` quality and trigger fidelity for the
skills in scope. The knowledge, playbooks, error patterns, and checklists
of that craft.

**Hands off.** Anything outside prompt and skill craft. The province file
is short on purpose; the surfaces are in `SKILL.md` and `corpus/`.

The scorecard records an axis-name reconciliation: `MISSION.md` assigns
this lane "depth + consistency", and `AXES.md` has no `consistency` axis.
Kotoba treats consistency as a sub-axis of calibration and marks the
mismatch as routed to the protocol lane. Read that note before comparing
this card with another lane's.

## Start here

1. `SKILL.md` — the craft, including how the two harnesses render a
   description.
2. `corpus/README.md` — the coverage map. The integrity verifier treats
   this index as a claim.
3. `verifiers/` — executable checks over the corpus and the skill.
4. `SCORECARD.md` — fractional scores, each with a counting command.
5. `LOG.md` — append-only. Errata point at the text they correct.

## Check the corpus

The verifiers live in `verifiers/`. Open the module docstring before you
treat a run as a verdict; each file names its check ids and what a failure
means.

```
verifiers/verify_corpus_integrity.py
verifiers/verify_corpus_independent.py
verifiers/verify_skill_checklist.py
verifiers/verify_harness_claims.py
verifiers/verify_surfaces.py
verifiers/fault_injection_corpus.sh
```

`verify_corpus_integrity.py` pins the index: tracked corpus files the
coverage map does not mention, map patterns that match nothing, and
pointers that do not resolve.

## The tree

| Path | What it is |
|---|---|
| `SKILL.md` | The craft contract |
| `corpus/knowledge/` | Admitted notes |
| `corpus/lessons/` | Per-round lessons |
| `verifiers/` | The checks above |
| `plans/` | Round plans |

## Fleet

Minted under [shokunin](https://github.com/VeigaPunk/shokunin).
