# kotoba-shokunin — Scorecard

Axes owned by this lane: **depth + consistency** (`../MISSION.md`, § Fleet shape).
All six AXES.md axes are scored because the contract asks for the full table;
only depth and consistency are worked as moves. Scores are the state after the
round named in the last column. Every score carries a pointer; no pointer, no score.

## axes

| Axis | Score 0–10 | Evidence pointer | Last-change round |
|---|---:|---|---|
| depth | 8 | `SKILL.md` — anatomy, decision-table, four fidelity checklists, anti-pattern table, Sources; `corpus/knowledge/render-mechanism-round7.md` + `knowledge/opencode-offer-trace-round8.md` mechanism sections. Not 10: checklist execution is still lane-attested (no external verifier) | 9 |
| consistency | 7 | `SKILL.md` — `## Router model — which harness, which gate` (omp vs opencode tag/render/gate/failure) + harness-qualified intro, frontmatter-craft opener, rule 8, rules 9, anti-pattern rows; `corpus/README.md` coverage map now indexes both round-8 artifacts and both lesson files; `corpus/lessons/round-8.md` written. Was 5 at the start of round 9 (`UNSCOPED=9 UNSUPPORTED=7` over 31 claim units, baseline table in `corpus/knowledge/claim-scope-audit-round9.md`) | 9 |
| coverage | 7 | `PROVINCE.md`; `SKILL.md` § Instruction surfaces (7 classes); `corpus/README.md` § Coverage map + Known gaps. Below exhaustive: implicit-intent fidelity unmeasured; no MCP/plugin surface exists on this host | 9 |
| operability | 6.5 | `SKILL.md` four checklists (13/9/12/8 items) applied to real files (round-5/6/7 audits); both harness Verify command blocks in `knowledge/harness-router-models-round9.md`. Ceiling: promotion evidence remains lane-asserted (`SHONEN.md` all `[~]`) | 9 |
| freshness | 7.5 | `LOG.md` round-9 drift re-measure: omp cache 5/17 → 17 rows with 17/17 keys reproduced (`sqlite3 -readonly ~/.omp/agent/skill-descriptions.db "select count(*) from skill_descriptions;"` → 17; style-aware salt recipe in `knowledge/harness-router-models-round9.md`); warns 10681 → 10925 (`grep -rh 'Skill description compression failed' ~/.omp/logs/ | wc -l`); session_init 3911 → ~4032–4116 (`grep -rh '"type":"session_init"' ~/.omp/agent/sessions/ | wc -l`); opencode.db 415/216 and opencode.log 471 permission lines unchanged. Round-9 corpus rows re-labelled truncation-era | 9 |
| calibration | 6 | `SHONEN.md` regenerated to the canonical 4-box seed with one evidence line per box (round-8 audit had flagged kotoba's prose variant); all marks `[~]` with pointers — no `[x]` is claimed anywhere. Ceiling: no non-author verifier has run the checklists | 9 |
| adjacency | 7 | Cross-domain defects audited and routed, never fixed: sibling description rewrites remain proposals (`knowledge/sibling-description-rewrites-round8.md`); round-9 connector lane swept the five sibling `SKILL.md` files for the same unscoped harness claims and found none (`grep -n 'cliff\|<skills>\|<available_skills>\|slice(0,99)\|router\|opencode\|omp'` per file → no harness-unscoped skill-router claim), so no handover was owed for this axis-move | 9 |

## planned

Round 10 — **depth**: convert the round-9 harness model into an executable
verifier (a committed script that recomputes the omp cache-key coverage and the
opencode `init count` reconstruction and exits non-zero on drift), so the two
harness claim sets stop depending on hand-run recipes.

## retired

None yet. No saturation or wrong-fit evidence (`../AXES.md`, § Working an axis).