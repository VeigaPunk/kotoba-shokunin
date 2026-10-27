# S04Assimilation — assimilation decision, kotoba r77 w1

Assimilation: none

Reason (three independent blockers, each observed in committed/staged bytes):
1. Id-space collision: 23 staged ids (S203..S225) are already taken in the lane by different sources; the package was staged against a lane of 128 rows ("first staged id is S203", MERGE-REPORT.md:9), the lane now holds 151 (S001..S225). Appending SOURCES.append.md verbatim would create 23 duplicate ids with conflicting rows; the staged entries cite those ids, so a renumber rewrites entries and is a new, unfrozen claim.
2. The only theme that maps onto C1 is not admissible under the frozen counter (see below).
3. Every other theme is either already held by the lane (round 7/67/68/74 entries), outside PROVINCE.md scope (registry/aggregator census), or would need an unfrozen counter. r77 claims are frozen (plans/round-77.md § Frozen counters); nothing may be widened.

## Id-collision guard (scratch only, A=/fast/scratch/hyaku/kotoba-r77/S04Assimilation)
- grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md  -> 151 ids (S001..S225, no duplicates)
- same on SOURCES.append.md -> 188 ids (S203..S390, no duplicates)
- sort | comm -12 -> collision count = 23 (S203..S225, every id from S203 to S225)
- Collisions are different sources, not same-source: e.g. lane S203 Roo Code skills vs staged S203 OpenAI Model Spec; lane S213 agentskills optimizing-descriptions vs staged S213 Mitsubishi Electric article.
- URL overlap (sorted-unique, strings of http(s)://): 26 URLs appear in both registries (agentskills.io best-practices/evaluating-skills/optimizing-descriptions/quickstart/using-scripts, Roo, Amp, Junie, Deep Code, Factory, TRAE, CodeBuddy IDE+CLI, Kimi, Zhipu, Claude Code skills, MS Agent Framework, pi-mono, Hermes, …). The lane already independently opened them (r74/r75). Free ids in the staged span: S226..S390 do not collide (165 ids), but rows S203..S225 would need renumbering.
- The staged S231 (optimizing-descriptions) and S232 (best-practices) are duplicates of lane S213 and S223.
- MERGE-REPORT.md:9 baseline (128 rows) is stale by 23 rows; its "rows whose source the lane already holds" table is keyed to old ids (S204→S124 etc.) and is not reliable for the current lane.

## Themes (88 knowledge entries, 188 rows; MERGE-REPORT.md § Knowledge files)
| theme | staged entries (examples) | PROVINCE.md scope | lane already holds | r77 verdict |
|---|---|---|---|---|
| T1 description / trigger craft, eval design, invocation bottleneck | description-writing-and-trigger-testing, spec-description-trigger-discipline, skill-invocation-is-the-bottleneck, spec-eval-file-format, skill-measurement-protocols | in scope (trigger fidelity, line 3) | S213/S223 + spec-skill-creation-craft-round74 (guide-advice level) | maps onto C1 only for the S213 half; refused (below) |
| T2 authority ladder, body placement, tool-mediated conflict | instruction-authority-ladder, skill-body-authority-*, tool-mediated-conflict-is-the-hard-case | in scope | instruction-authority-ladder-round67.md | duplicate of held entry |
| T3 trust gates, injection surface | client-trust-gates-round7, untrusted-project-skill-gate-amendment, skills-are-an-injection-surface | in scope (PROVINCE.md:29) | client-trust-gates-round68.md | duplicate; verify-by-counter exists |
| T4 client skill surfaces / Chinese vendors (Qwen, TRAE, CodeBuddy, Kimi, Zhipu) | client-surface-census-extension, chinese-client-skill-surfaces, trae-*, kimi-*, translation-drift | partly (client surface maps) | rows S217-S222 already in lane for same URLs | would need renumber + new counter |
| T5 precedence / paths / loading models / skill-vs-always-on | skill-paths-and-precedence, skill-source-precedence-round7, client-loading-and-distribution-models, skill-vs-always-on-boundary, context-rot | in scope | r49/r53/r67 entries cover same ground | needs dedup, no counter |
| T6 Japanese layer (rounds 3,6,8-16, ~12 entries) | japanese-* | adjacent research, not craft | none | out of frozen claims |
| T7 registry / aggregator / health-score / catalogue census (rounds 7-16, ~30 entries) | registry-*, catalogue-figures-*, leaderboard-count-*, owner-enumeration-*, aggregator-edit-state-*, health-score-metric-*, aaif-project-home-* | NOT in scope (not prompt/skill craft; refuses "anything outside this domain") | none | decline |

## Does any theme map onto C1?
Only T1's spec-description-trigger-discipline.md (source: S231 = the S213 page, "fetched as .md 13 403 B on 2026-10-23"). It cannot serve C1:
- C1 conjunct (a)/(b)/(f) are bound to corpus/knowledge/description-craft-round76.md, the r76 snapshot set (.ufo/waves/round-76/snapshots/, digest 7cc54fbb…bd837) and located quotes verified against those bytes. The staged entry carries no snapshot bytes and no digest (package holds only knowledge/*.md); its quotes are unverifiable against the pinned page.
- Its claims go beyond C1: it asserts the 20-query / 8-10 eval-design guidance and a three-way negative-trigger "tension" with TRAE and Chiba; plans/round-76.md § C1 explicitly holds the eval-fidelity claims out. Its "specification is the normative guide" framing and the S231 id are stale/duplicate.
- r76 already decided: plans/round-76.md:12 refused it as a staged artifact and re-grounded in-round (CORPUS.md rule 1). Nothing has changed that.

## If L1 nonetheless wanted one theme (not proposed)
Candidate = T1 only, as in-round re-grounding, never staged text: (1) re-open S213 and S223 in-round (already a C1 task: two independent seats); (2) rewrite the staged entry's source: lines S231->S213, S232->S223 and re-quote against the pinned snapshots; (3) drop the eval-design and TRAE/Chiba paragraphs (held / separate claims); (4) leave SOURCES.append.md unappended (23 id collisions). That adds no conjunct to the frozen six and no counter would measure it, so it would be an unmeasured extra; recommend against.

Tools installed: none. Scratch removed on exit (trap).
