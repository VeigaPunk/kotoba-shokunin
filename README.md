# kotoba-shokunin — prompt & skill craft

**A `SKILL.md` is a loader contract.** The frontmatter `description` is
what the router sees. The body is what a cold agent can execute without
oral context. This lane audits trigger fidelity and decision density —
and reports; it does not silently rewrite a sibling's skill.

This is a [shokunin](https://github.com/VeigaPunk/shokunin) lane. Rank:
shonen. Kotoba owns skill-file craft. It does not own the domain
content inside another lane's skill (that lane does), and it does not
own the measured effect of prompt format on model capability (that is
[kengaku](https://github.com/VeigaPunk/kengaku-shokunin)).

## Province

**Owns:** `SKILL.md` / `AGENTS.md` / dispatch-prompt / system-prompt
quality; trigger fidelity; checklist density; the verifiers that prove
those claims against pinned baselines.

**Refuses:** anything outside prompt & skill craft. Sibling `*-shokunin`
skills own their own content — this lane audits and reports; fixes
route to the owning lane. Note recorded in `SKILL.md`: the shokunin
files are not in an OMP skill-discovery root, so their descriptions
never reach the `<skills>` router. Craft here is audit-side, not
router-visible.

Full boundary: [`PROVINCE.md`](PROVINCE.md).

## Start here

1. [`SKILL.md`](SKILL.md) — loader-contract rules, trigger craft, anti-patterns.
2. [`PROVINCE.md`](PROVINCE.md) — owned domain and refusals.
3. [`verifiers/`](verifiers/) — machine checks against pinned baselines.

## Verifiers

```
python3 verifiers/verify_skill_checklist.py
python3 verifiers/verify_surfaces.py
python3 verifiers/verify_corpus_integrity.py
python3 verifiers/verify_corpus_independent.py
python3 verifiers/verify_harness_claims.py
bash verifiers/fault_injection_corpus.sh
```

`verify_skill_checklist.py` extracts every `- [ ]` box under checklist
sections and requires `verifiers/checklist-baseline.json`
(`kotoba-checklist-v1`) to cover each live box exactly once, pinned by
the sha256 of normalised box text. A reworded, added, or removed box
fails the run. Disposition is *executed*, *delegated* to a named
instrument, or `unexecuted:<reason>`.

These verifiers grade this lane's own skill and corpus. They are not a
license to edit a sibling.

## What's in the repo

```
kotoba-shokunin/
├── SKILL.md          loader-contract craft
├── PROVINCE.md       domain boundary
├── SHONEN.md         promotion checklist
├── LOG.md            append-only audit trail
├── SCORECARD.md      axis verdicts
├── AGENTS.md         operating rules
├── verifiers/        checklist / surfaces / corpus / harness gates
├── plans/            round plans
└── corpus/           knowledge/, lessons/, QUALITY.md
```

Protocol: append-only corpus; every claim separates observation /
inference / unknown; rounds are non-author-verified. See the fleet
[README](https://github.com/VeigaPunk/shokunin#readme) for how a lane
learns.
