# S07FrontierLeads — round 77 w1 seat report

Task: propose up to 3 frontier ground leads (round 78+), opened now, quote ≤25 words, not-covered sweep, PROVINCE scope check.

Read: corpus/README.md § Frontier (rows: checklist coverage, command extraction, implicit-intent, MCP/plugin, loader freshness, per-render consumption + round 52–74 notes), PROVINCE.md § Frontier/Core/Adjacent (20 sibling lanes),
corpus/SOURCES.md registry S001–S225 and § Leads (unopened) (anthropics/skills, Anthropic Engineering context engineering, Vercel, arXiv items, ...).

Result (full evidence in the deliverable): 
1. L1 Claude Code skills.md § Skill content lifecycle — "keeping the first 5,000 tokens of each" / 25,000 combined after auto-compaction. sha256 0fdcb266…968ad286, fetched 2026-10-27T19:45:04Z, HTTP 200. Sweeps for compaction/re-attach/25,000 over corpus/knowledge + SKILL.md: 0 lines. IN scope (body craft); refuse compaction measurement → kengaku.
2. L2 agentskills.io adding-skills-support.md § Protect skill content from context compaction — S002's page but S002 anchors only malformed-YAML/lenient-validation; sweeps: 0 lines. sha256 07511caa…0dfb586. IN scope as author guidance; harness-implementation text refused (nearest sibling kumitate, [INFERENCE]).
3. L3 Anthropic effective-context-engineering "right altitude" — sha256 ec0eb251…f5b961, 308→/research/ then 200; sweep 0 lines; overlaps S223 fragility grading, so weakest; compaction/memory sections refused.
Refused: Vercel AGENTS.md-vs-skills (page now carries "56% of eval cases" quote, but it is capability measurement = kengaku, the lane's r72 refusal stands).

Checks run: curl fetches (all HTTP 200 after redirects), verbatim quote presence via a python check (L1 20 words, L1b 9, L2 19, L3 12: all found), grep sweeps (exit codes in deliverable). No tool installs. Scratch /fast/scratch/hyaku/kotoba-r77/S07FrontierLeads removed at the end. No lane file outside .ufo/waves/round-77/ was edited; no git writes.
Calibration: all claims are documentary (vendor/spec page text), not client runs; the kumitate sibling assignment is inference.

VERDICT: 3 leads delivered (L1/L2 sound, L3 weak) plus 1 refused (Vercel); ground is "what a skill body keeps after compaction", uncovered at base 6523aced.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/S07FrontierLeads.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/S07FrontierLeads.md
