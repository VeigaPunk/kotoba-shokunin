# harness-independent agreement report — round 37/38 (C1, seats P4/P1)

Driver: `verifiers/compare_harness_independent.py` (embeds no expected value; joins both
instruments' outputs only). Source-blindness rule honoured while building it: no harness
source, no `baseline.json` harness rows and no doc quoting them were read.

Agreement predicate follows the round-37 C1 adjudication protocol §2 (frozen surface):
`equal` -> value equality; `zero` -> both readings empty; `positive` -> numeric direction.
Strict value equality is reported alongside; rows where it fails but the predicate holds
are adjudicated and named, never smoothed.

Round-38 C1 closure: rows the independent instrument scopes out (status `SCOPED_OUT`,
blocker named by that instrument) leave the join by name and are listed below with their
blockers. The headline is stated over the joined scope, so a scope-out can only narrow
the claim, never add to the numerator.

- HEAD scanned: `055d3b9`
- live command: `file:/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/round-46/evidence/x3/injected-live.json` (exit 0)
- independent command: `file:/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/round-46/evidence/x3/injected-independent.json` (exit 0)
- **agreement: 1/1** (mode-aware protocol headline over the joined scope; 1 live checks, 0 scoped out) — protocol 1/1, strict 1/1 — all checks agree, both instruments green

| # | check | mode | live observed | independent expected | ind status | protocol | strict |
|---|-------|------|---------------|----------------------|------------|----------|--------|
| 1 | `probe.anchor
| 2 | counterfeit | equal | 999 | 999 | DERIVED | yes | yes |` | equal | `1` | `1` | DERIVED | yes | yes |

## Scoped out by the independent instrument (blocker named — not a disagreement, not agreement)

- none

## Provisional rows (agreement resting on unlanded derivations — named, not counted)

- none

## Adjudicated rows (strict unequal, protocol agreed — recorded, not smoothed)

- none

## Disagreements (named)

- none

## Instrument states quoted (both instruments' own outputs)

- live verdicts: 1 PASS, 0 non-PASS
- secondary join (independent expected vs live expected): 0/1
- driver exit: 0 — all checks agree, both instruments green

