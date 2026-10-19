# harness-independent agreement report — round 37 (C1, seat P4)

Driver: `verifiers/compare_harness_independent.py` (embeds no expected value; joins both
instruments' outputs only). Source-blindness rule honoured while building it: no harness
source, no `baseline.json` harness rows and no doc quoting them were read.

Agreement predicate follows the round-37 C1 adjudication protocol §2 (frozen surface):
`equal` -> value equality; `zero` -> both readings empty; `positive` -> numeric direction.
Strict value equality is reported alongside; rows where it fails but the predicate holds
are adjudicated and named, never smoothed.

- HEAD scanned: `041f6ba`
- stamp: FINAL P4 snapshot; instrument sha256 in drafts/p4/hashes-at-measure.txt; join stable across e8ea8d8c/e5f92f74/942d5fc5
- live command: `/usr/bin/python3 verifiers/verify_harness_claims.py --json` (exit 0)
- independent command: `/usr/bin/python3 /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/verify_harness_independent.py --json` (exit 0)
- **agreement: 23/28** (mode-aware protocol headline) — protocol 23/28, strict 17/28 — disagreements: oc.dup.roots_both_sided (mode=equal: expected 3, observed 0), oc.log.skills_tag_hits (mode=zero: expected 13, observed 0), omp.catalogue.found (mode=equal: expected None, observed True), omp.catalogue.matched (mode=equal: expected None, observed 7), omp.catalogue.total (mode=equal: expected None, observed 7)

| # | check | mode | live observed | independent expected | ind status | protocol | strict |
|---|-------|------|---------------|----------------------|------------|----------|--------|
| 1 | `oc.dup.onesided_roots` | zero | `[]` | `0` | DERIVED | yes | no |
| 2 | `oc.dup.roots_both_sided` | equal | `0` | `3` | DERIVED | NO | no |
| 3 | `oc.log.available_skills_hits` | zero | `0` | `0` | DERIVED | yes | yes |
| 4 | `oc.log.init_count_max` | equal | `0` | `0` | DERIVED | yes | yes |
| 5 | `oc.log.init_count_monotone` | zero | `[]` | `0` | DERIVED | yes | no |
| 6 | `oc.log.skills_rescan_max` | equal | `3` | `3` | DERIVED | yes | yes |
| 7 | `oc.log.skills_tag_hits` | zero | `0` | `13` | DERIVED | NO | no |
| 8 | `oc.permission.skill_allow` | equal | `0` | `0` | DERIVED | yes | yes |
| 9 | `oc.permission.skill_lines` | equal | `0` | `0` | DERIVED | yes | yes |
| 10 | `oc.roots.names_plus_builtin` | equal | `7` | `7` | DERIVED | yes | yes |
| 11 | `oc.roots.plugins_cache` | zero | `False` | `0` | DERIVED | yes | no |
| 12 | `omp.cache.keys_reproduced` | equal | `7` | `7` | DERIVED | yes | yes |
| 13 | `omp.cache.misses` | zero | `0` | `0` | DERIVED | yes | yes |
| 14 | `omp.cache.verified_skills` | equal | `7` | `7` | DERIVED | yes | yes |
| 15 | `omp.catalogue.found` | equal | `True` | `None` | UNLANDED | NO | no |
| 16 | `omp.catalogue.matched` | equal | `7` | `None` | UNLANDED | NO | no |
| 17 | `omp.catalogue.missing_names` | zero | `[]` | `None` | UNLANDED | yes | no |
| 18 | `omp.catalogue.total` | equal | `7` | `None` | UNLANDED | NO | no |
| 19 | `omp.db.rows` | equal | `14` | `14` | DERIVED | yes | yes |
| 20 | `omp.db.rows_wellformed` | equal | `14` | `14` | DERIVED | yes | yes |
| 21 | `omp.descriptions.missing` | zero | `[]` | `0` | DERIVED | yes | no |
| 22 | `omp.descriptions.over_cliff` | positive | `7` | `7` | DERIVED | yes | yes |
| 23 | `omp.descriptions.unmodelled` | zero | `0` | `0` | DERIVED | yes | yes |
| 24 | `omp.elf.template_bytes` | equal | `273` | `273` | DERIVED | yes | yes |
| 25 | `omp.elf.template_sha256` | equal | `'c1f03c8e248eb40ec7735baab67f686fc2f254e00d2a0241ff220628461bdb51'` | `'c1f03c8e248eb40ec7735baab67f686fc2f254e00d2a0241ff220628461bdb51'` | DERIVED | yes | yes |
| 26 | `omp.names.mismatches` | zero | `[]` | `0` | DERIVED | yes | no |
| 27 | `omp.offered.dangling` | equal | `0` | `0` | DERIVED | yes | yes |
| 28 | `omp.offered.skills` | equal | `7` | `7` | DERIVED | yes | yes |

## Provisional rows (agreement resting on unlanded derivations — named, not counted)

- `omp.catalogue.missing_names` (status=UNLANDED): live observed `[]` vs independent expected `None`

## Adjudicated rows (strict unequal, protocol agreed — recorded, not smoothed)

- `oc.dup.onesided_roots` (mode=zero): live observed `[]` vs independent expected `0`
- `oc.log.init_count_monotone` (mode=zero): live observed `[]` vs independent expected `0`
- `oc.roots.plugins_cache` (mode=zero): live observed `False` vs independent expected `0`
- `omp.catalogue.missing_names` (mode=zero): live observed `[]` vs independent expected `None`
- `omp.descriptions.missing` (mode=zero): live observed `[]` vs independent expected `0`
- `omp.names.mismatches` (mode=zero): live observed `[]` vs independent expected `0`

## Disagreements (named)

- `oc.dup.roots_both_sided` (mode=equal): live observed `0` != independent expected `3`
- `oc.log.skills_tag_hits` (mode=zero): live observed `0` != independent expected `13`
- `omp.catalogue.found` (mode=equal): live observed `True` != independent expected `None`
- `omp.catalogue.matched` (mode=equal): live observed `7` != independent expected `None`
- `omp.catalogue.total` (mode=equal): live observed `7` != independent expected `None`

## Instrument states quoted (both instruments' own outputs)

- live verdicts: 28 PASS, 0 non-PASS
- secondary join (independent expected vs live expected): 17/28
- driver exit: 1 — disagreements: oc.dup.roots_both_sided (mode=equal: expected 3, observed 0), oc.log.skills_tag_hits (mode=zero: expected 13, observed 0), omp.catalogue.found (mode=equal: expected None, observed True), omp.catalogue.matched (mode=equal: expected None, observed 7), omp.catalogue.total (mode=equal: expected None, observed 7)

