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
- live command: `/usr/bin/python3 verifiers/verify_harness_claims.py --json` (exit 0)
- independent command: `/usr/bin/python3 /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/verify_harness_independent.py --json` (exit 0)
- **agreement: 24/24** (mode-aware protocol headline over the joined scope; 28 live checks, 4 scoped out) — protocol 24/24, strict 20/24 — all checks agree, both instruments green

| # | check | mode | live observed | independent expected | ind status | protocol | strict |
|---|-------|------|---------------|----------------------|------------|----------|--------|
| 1 | `oc.dup.onesided_roots` | zero | `[]` | `0` | DERIVED | yes | no |
| 2 | `oc.dup.roots_both_sided` | equal | `0` | `0` | DERIVED | yes | yes |
| 3 | `oc.log.available_skills_hits` | zero | `0` | `0` | DERIVED | yes | yes |
| 4 | `oc.log.init_count_max` | equal | `0` | `0` | DERIVED | yes | yes |
| 5 | `oc.log.init_count_monotone` | zero | `[]` | `[]` | DERIVED | yes | yes |
| 6 | `oc.log.skills_rescan_max` | equal | `3` | `3` | DERIVED | yes | yes |
| 7 | `oc.log.skills_tag_hits` | zero | `0` | `0` | DERIVED | yes | yes |
| 8 | `oc.permission.skill_allow` | equal | `0` | `0` | DERIVED | yes | yes |
| 9 | `oc.permission.skill_lines` | equal | `0` | `0` | DERIVED | yes | yes |
| 10 | `oc.roots.names_plus_builtin` | equal | `7` | `7` | DERIVED | yes | yes |
| 11 | `oc.roots.plugins_cache` | zero | `False` | `0` | DERIVED | yes | no |
| 12 | `omp.cache.keys_reproduced` | equal | `7` | `7` | DERIVED | yes | yes |
| 13 | `omp.cache.misses` | zero | `0` | `0` | DERIVED | yes | yes |
| 14 | `omp.cache.verified_skills` | equal | `7` | `7` | DERIVED | yes | yes |
| 15 | `omp.db.rows` | equal | `14` | `14` | DERIVED | yes | yes |
| 16 | `omp.db.rows_wellformed` | equal | `14` | `14` | DERIVED | yes | yes |
| 17 | `omp.descriptions.missing` | zero | `[]` | `0` | DERIVED | yes | no |
| 18 | `omp.descriptions.over_cliff` | positive | `7` | `7` | DERIVED | yes | yes |
| 19 | `omp.descriptions.unmodelled` | zero | `0` | `0` | DERIVED | yes | yes |
| 20 | `omp.elf.template_bytes` | equal | `273` | `273` | DERIVED | yes | yes |
| 21 | `omp.elf.template_sha256` | equal | `'c1f03c8e248eb40ec7735baab67f686fc2f254e00d2a0241ff220628461bdb51'` | `'c1f03c8e248eb40ec7735baab67f686fc2f254e00d2a0241ff220628461bdb51'` | DERIVED | yes | yes |
| 22 | `omp.names.mismatches` | zero | `[]` | `0` | DERIVED | yes | no |
| 23 | `omp.offered.dangling` | equal | `0` | `0` | DERIVED | yes | yes |
| 24 | `omp.offered.skills` | equal | `7` | `7` | DERIVED | yes | yes |

## Scoped out by the independent instrument (blocker named — not a disagreement, not agreement)

- `omp.catalogue.found`: the catalogue carrier's selection rule is inside the harness's own authored scope (the newest session-jsonl <skills> block with at least min(10, len(known)) entries, matched line-by-line against the skill cache). This instrument's substrate set is the omp binary, the skill cache, the skill roots, the opencode log and the opencode configs; none of them carries the selection rule, so re-deriving the row blind would be guessing. Named out of scope instead (r38 adjudication, source-read(author); P3's 'named UNSUPPORTED rather than guessed' idiom).
- `omp.catalogue.matched`: the catalogue carrier's selection rule is inside the harness's own authored scope (the newest session-jsonl <skills> block with at least min(10, len(known)) entries, matched line-by-line against the skill cache). This instrument's substrate set is the omp binary, the skill cache, the skill roots, the opencode log and the opencode configs; none of them carries the selection rule, so re-deriving the row blind would be guessing. Named out of scope instead (r38 adjudication, source-read(author); P3's 'named UNSUPPORTED rather than guessed' idiom).
- `omp.catalogue.missing_names`: the catalogue carrier's selection rule is inside the harness's own authored scope (the newest session-jsonl <skills> block with at least min(10, len(known)) entries, matched line-by-line against the skill cache). This instrument's substrate set is the omp binary, the skill cache, the skill roots, the opencode log and the opencode configs; none of them carries the selection rule, so re-deriving the row blind would be guessing. Named out of scope instead (r38 adjudication, source-read(author); P3's 'named UNSUPPORTED rather than guessed' idiom).
- `omp.catalogue.total`: the catalogue carrier's selection rule is inside the harness's own authored scope (the newest session-jsonl <skills> block with at least min(10, len(known)) entries, matched line-by-line against the skill cache). This instrument's substrate set is the omp binary, the skill cache, the skill roots, the opencode log and the opencode configs; none of them carries the selection rule, so re-deriving the row blind would be guessing. Named out of scope instead (r38 adjudication, source-read(author); P3's 'named UNSUPPORTED rather than guessed' idiom).

## Provisional rows (agreement resting on unlanded derivations — named, not counted)

- none

## Adjudicated rows (strict unequal, protocol agreed — recorded, not smoothed)

- `oc.dup.onesided_roots` (mode=zero): live observed `[]` vs independent expected `0`
- `oc.roots.plugins_cache` (mode=zero): live observed `False` vs independent expected `0`
- `omp.descriptions.missing` (mode=zero): live observed `[]` vs independent expected `0`
- `omp.names.mismatches` (mode=zero): live observed `[]` vs independent expected `0`

## Disagreements (named)

- none

## Instrument states quoted (both instruments' own outputs)

- live verdicts: 28 PASS, 0 non-PASS
- secondary join (independent expected vs live expected): 20/24
- driver exit: 0 — all checks agree, both instruments green

