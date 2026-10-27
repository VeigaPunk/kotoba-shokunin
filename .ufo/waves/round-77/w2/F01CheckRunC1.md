# F01CheckRunC1 — round 77 C1 depth falsification

## Scope and evidence

Attacked item: C1, sourced depth claim, the frozen description-craft conjuncts (a)–(f). The canonical r77 plan is `plans/round-77.md`; it identifies `2f675548eaad2a037a899d39247c1fd7a88aaf48` as the pre-data base and `6523aced1ee0ebe07dca996213bdc645a6acbd1e` as the freeze commit. Read the r76 contract and addenda 1–6, including the corrected conjunct (a), clip-preserving measurement convention, and C1 counter docstring.

The lane's observed HEAD is exactly `6523aced1ee0ebe07dca996213bdc645a6acbd1e`. `git status --short --untracked-files=all` reports no staged or modified tracked files and 166 untracked wave-dispatch/build artifacts; `git log --oneline --all --decorate -8` shows HEAD at the freeze and no later landed tip. Thus claim data is not committed at the observed tip. The untracked drafts are not evidence of a landed claim and were not treated as such.

Frozen counter integrity check: `sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_desc_craft.py` returned `cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e`, exactly the plan pin. The C2 counter hash was also checked and matched its plan pin, but C2 was not run in this C1 seat.

## C1 counter execution

Exact command:

```sh
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_desc_craft.py --repo /home/vgpnk/Projects/shokunin/kotoba-shokunin --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e
```

Observed output:

```text
measured-rev: 6523aced1ee0ebe07dca996213bdc645a6acbd1e
(a) snapshot chain: fail
(b) located quotes: fail
(c) act-on: fail
(d) self-audit: fail
(e) registry: fail
(f) provenance: fail
  (a) corpus/lessons/round-76.md is not committed at the measured revision
  (b) corpus/knowledge/description-craft-round76.md is not committed at the measured revision
  (c) no Body craft row cites both corpus/knowledge/description-craft-round76.md and S213
  (d) corpus/knowledge/description-craft-round76.md is not committed at the measured revision
  (e) row S213's used-by cell does not list corpus/knowledge/description-craft-round76.md
  (f) corpus/knowledge/description-craft-round76.md is not committed at the measured revision
description craft backed 0 of 6
```

Exit status: **1** (counter process exit). This is the plan's expected red result at the pre-data freeze, not a successful C1 verification. No landed r77 revision was available, so the required post-data C1 rerun and claim verification remain **blocked**. I did not run the counter against an invented or draft-derived revision, mutate claim data, or claim the gate passed.

## Conjunct report / verdict

At the measured freeze, counter conjuncts (a)–(f) all fail. The diagnostics identify the absent committed lesson and entry, absent qualifying Body craft row and S213 used-by, and absent self-audit/provenance entry. This supports only the pre-data baseline behavior. It does not determine whether the draft artifacts would satisfy the claim once integrated; reopening/reviewing those drafts is not a substitute for a run on the landed r77 tip.

Axes named for this seat: **depth** (the attacked C1 axis); consistency, calibration, freshness, and operability are not evaluated here. Since claim data is absent, there is no claim move to keep or score. Minimal next step is for the lane integrator to land the authorized claim data after freeze, then rerun this unchanged frozen counter at that committed revision. That is a prerequisite, not a proposed change to the counter or the claim; no axis-harm assessment of unlanded data is possible.

VERDICT: BLOCKED — C1 is not landed; frozen counter at freeze returns the expected 0 of 6, exit 1, and cannot verify the r77 claim.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w2/F01CheckRunC1.md