# kotoba-shokunin — Province

**Domain:** prompt & skill craft — scopes SKILL.md/AGENTS.md quality, trigger fidelity

**Owns:** the domain knowledge, playbooks, error patterns, and checklists above.
**Refuses:** anything outside this domain; report cross-domain evidence back to the orchestrator rather than absorbing it.

## Core

Appended round 46 (LEARNING.md § Province is a frontier); surfaces the lane governs now:

- `SKILL.md` — trigger/frontmatter craft, anatomy and compression, decision tables, the four fidelity checklists (backed by `corpus/knowledge/frontmatter-trigger-surface.md`, `corpus/knowledge/anatomy-and-compression.md`, `corpus/knowledge/fail-closed-and-anti-patterns.md`).
- Agent-definition, always-on (AGENTS.md-class) and dispatch-prompt craft — `corpus/knowledge/agent-defs-commands-and-round-prompts.md`, `corpus/knowledge/agents-md-and-dispatch-surfaces.md`, `corpus/knowledge/dispatch-prompt-audit-round7.md`.
- Executable instruments over those surfaces — `verifiers/verify_skill_checklist.py`, `verifiers/verify_surfaces.py`, `verifiers/verify_harness_claims.py`, `verifiers/compare_harness_independent.py`, `verifiers/verify_corpus_integrity.py`, `verifiers/verify_corpus_independent.py`, `verifiers/check_substrate_pins.py`, `verifiers/check_assertion_floors.py`.
- Frontmatter XML-tag rule (round 47, moved from Frontier): S003's Anthropic rule (`corpus/SOURCES.md`; superseded as a row by S019 in round 48) is approximated lexically on the unparsed `name` and `description` text by `verifiers/verify_skill_checklist.py` check `trigger.no_xml_tag`, with four discriminating fixtures (code-span, folded split, YAML escape, arrow/comparison control); it is not the packager's parsed-value rule (round 48 entry below); this file's description is tag-free.
- Frontmatter rule authorities (round 48): which authority imposes which SKILL.md frontmatter rule — open spec (S018), its reference validator skills-ref (S017), Anthropic docs (S019), Anthropic's packager (S012), Codex docs (S021) — and what the lane's lexical `trigger.no_xml_tag` actually executes (S020), with run counterexamples: `corpus/knowledge/frontmatter-rule-authorities-round48.md`.
- Sibling arbitration (round 49, moved from Frontier): which sibling lanes share a boundary with kotoba and what each sibling's description says about its neighbours, read at pinned sibling commits, with the primary-source finding that no documented tie-break exists between overlapping descriptions (S022, S023, S018) — `corpus/knowledge/sibling-overlap-census-round49.md`, checked by `verifiers/check_sibling_census.py`. Round 50: kotoba's own description names the 9 lanes classed `adjacent`, each in a clause with an ownership or routing word (`verifiers/check_sibling_census.py --skill SKILL.md`), and the census entry adds the precedence between `contested` and a stated split.

## Frontier

Explored, not held — the live list is `corpus/README.md` § Frontier:

- Executed checklist coverage (33 of 41 boxes still lane-attested prose at round 46; 31 at round 49), command extraction outside the declared vocabulary, implicit-intent trigger fidelity, MCP/plugin instruction surfaces, sibling arbitration clauses (round 49: the census moved to Core; round 50: kotoba's own description names the 9 `adjacent` lanes; open: whether naming a lane improves routing is unmeasured on any harness), per-render skill consumption.
- Loader-rule freshness: the omp 18.12.3 substrate drift (surfaces 5/7, pins 1/3) and the frontmatter `description` XML-token rule — `corpus/lessons/round-46.md` § Mistakes, `corpus/SOURCES.md`. **Round 47:** the XML-token half moved to Core; the round-46 figures above are historical (they were the round-44 before-column, `corpus/lessons/round-47.md` M20). omp 18.12.5 and opencode 1.19.3 were re-derived and re-pinned (surfaces 7/7, pins 3/3 at default resolution). Still not held: re-derivation after a rebuild is manual — the omp extractor is a callee-name allowlist and opencode changed lineage under the same path family.

## Adjacent

Sibling-owned ground (report, don't absorb). Rewritten round 49 from the fleet census
`corpus/knowledge/sibling-overlap-census-round49.md` (classification rule, quotes and sweeps there;
per-lane seat reports under `.ufo/waves/round-49/build/`). The commit is the sibling commit the
classification was read at; `verifiers/check_sibling_census.py --province PROVINCE.md` checks that
these rows match the census on lane set, classification and commit (the boundary text is not checked). The round-46 list this replaces came from
`.ufo/round-46/scouts/w2-connector.md`.

| lane | classification | commit | boundary |
|---|---|---|---|
| audio | none | 7a2fcd4f08831154686e4e323031f41fffdb077f | game audio production; no skill file at the pin (seed form); no split with kotoba on its scope surfaces (seat sweep in the census row's report) |
| chousa | adjacent | 6c5eb1466f2b8abbd3de576389037f435016d07b | deep-research method; kotoba cites it, never re-derives it (`corpus/QUALITY.md`: claim admission stays here, the research method stays chousa's) |
| game-dev-2d | none | 7753d49b16674e122ed134403e7a9b301f2cbf7e | 2D game production; no skill file at the pin (seed form); no split with kotoba on its scope surfaces (seat sweep in the census row's report) |
| game-dev-3d | none | 89dd182b70943a20ae9aa6c1ed0e3c9b6e79c080 | 3D game production; its frontmatter audits cover only its own and vendored skill files |
| kagi | adjacent | 899c50b42634a3a4ad0b28ab7509786315e2fc2b | secrets and vault ops; shared read of `$HOME/.agents/AGENTS.md` — kagi pins the bytes, kotoba owns the checklist and shape reading (kagi `corpus/README.md:97`); the opencode config group owner is unresolved and stays with the integrator |
| kaidoku | none | 08c7a7299ed61c3fdc30ddb0adfe4e812d5eac76 | reverse engineering of shipped artifacts with REA; its domain overlaps revenger's (an open operator question, `.ufo/l0-questions.md` line 42 in the fleet repository; not kotoba's to rule) |
| kake | adjacent | e73d48bbf20759fc7758afaebf841fa02e5cfbbf | web properties and publishing; kotoba's description names kake among the lanes that own their own SKILL.md content while kotoba audits and reports (`SKILL.md:10-12` at `f3046466`); kake's corpus carries the same sentence only in a kotoba-filed, aggregator-owned lesson (kake `corpus/lessons/round-5-aggregator-mirror-pathless-cli-invocation.md:4-5`), which is not a sibling-stated split; basis kotoba |
| kama | adjacent | c808ba07f09c4be55413d3d6516c542ab69b64f8 | local model serving and endpoint health; kama's split reads "Kotoba owns the instruction/agent surface and its model/fallback wording; kama owns independent verification" (kama `corpus/knowledge/cross-lane-scope.md:29`; the agent files it names were deleted 2026-10-14 per kama `corpus/README.md:51-55`); kotoba's round-50 ruling, sent to the integrator (fleet `.ufo/l0-questions.md`, kotoba round-50 line; census entry, precedence sections): kama's `corpus/knowledge/consumer-registry.md:91-92` does judge fallback statements in agent files (rows its own errata mark historical; the files are gone), so the claim arm fires, and kama's own split assigns that wording to kotoba (`corpus/knowledge/cross-lane-scope.md:29`), so the row is `adjacent` by the precedence rule; basis sibling |
| kasegi | adjacent | 1fafde8f11454f3b0b98ab7f2b2e640aaf7f399a | bounty and security research; kotoba's description names kasegi among the lanes that own their own SKILL.md content while kotoba audits and reports (`SKILL.md:10-12` at `f3046466`); kasegi's corpus carries the same sentence only in a kotoba-filed, aggregator-owned lesson (kasegi `corpus/lessons/round-5-aggregator-mirror-ambiguous-citation-base.md:4-5`), which is not a sibling-stated split; basis kotoba; the earlier "prompt-injection exploits" clause had no source in kasegi's tree and is withdrawn |
| kengaku | adjacent | 1f3b0f1ec41ec297130e8944ff97968d32324632 | LLM and model research and evaluation (route telemetry is marked absent since 2026-10-15 in kengaku's own `SKILL.md:3`); kengaku keeps measured capability effects of prompt format, kotoba owns the craft rules (kengaku description, `SKILL.md:3`); kotoba's round-50 ruling, sent to the integrator: kengaku's round-25 census script reads only the SKILL.md of the lane it runs in (`plans/round25_census.sh`), so it is no claim on kotoba's Core; the round-49 note that it counts other lanes' files rested on excluded wave reports; basis both |
| kotodama | adjacent | 35f0d49f96f1d51f8b006136a8e1d0e8d0919a7a | worldbuilding and naming; its description refuses prompt and skill craft by naming kotoba (name collision recorded in kotodama `MINT.md:20`); kotoba's description names kotodama since round 50 |
| kumitate | adjacent | fac39171ac28c606e90da75fc2ba2ed3df52f4ea | orchestration and dispatch runtime and swarm lifecycle; kumitate routes "Prompt and skill craft → kotoba" (kumitate `PROVINCE.md:27`); kotoba owns the prompt wording, not the runtime (kotoba base `PROVINCE.md` § Adjacent) |
| lore | none | 380ef3abc7c7af11d7f23e9f9c82bb1937e1f695 | fictional-world records; no split with kotoba on its scope surfaces (seat sweep in the census row's report) |
| mado | none | e33ea30461f6e9bbeee40beef19770a953f7a105 | desktop and compositor craft; mado surveys the omarchy skill file's frontmatter as its own documentation surface (mado `PROVINCE.md:10-11`), and a mado wave report assigns that facet to kotoba with no province clause; no split on its scope surfaces, so `none` under the rule |
| mori | none | 28b79d3d1b76824f0c825aabe6cb6c5dc49961bf | fleet and host observability; no split with kotoba on its scope surfaces (seat sweep in the census row's report) |
| revenger | none | 876630dbb4d630e016d7d8c32a19ea04c646cbae | reverse engineering of shipped artifacts; no skill file at the pin; overlaps kaidoku (an open operator question, `.ufo/l0-questions.md` line 42 in the fleet repository; not kotoba's to rule) |
| souji | none | 4edb25dfe262515d0da63224bbba71e02e36cba5 | fleet repository hygiene; no split with kotoba on its scope surfaces (seat sweep in the census row's report) |
| tabi | none | e3cf4e0d30bb835532ff44b118c5ad52e09eb76d | browser and web-interaction craft; no split with kotoba on its scope surfaces (seat sweep in the census row's report) |
| tameshi | adjacent | 3b20f073c7305a582562cd323982991464c324f3 | verification-fixture craft and mutation testing; tameshi owns the fixture and mutation method (tameshi `PROVINCE.md` Domain line); kotoba's round-50 ruling, sent to the integrator: tameshi's Core names kagi's `corpus/checklist-run.sh`, which reads kagi's SKILL.md checklist (an instrument over another lane's SKILL.md, so the claim arm fires literally; the ledger lists it as unmeasured), and tameshi's own split keeps every gate with its owner (`PROVINCE.md:14-17`: every lane's gate remains its own), so the row is `adjacent` by the precedence rule; basis sibling |
| tsukuroi | none | 22fd1642e7fa4dfbdfba4419a443f06ffbb0b6c0 | host operability and system repair; no split with kotoba on its scope surfaces (seat sweep in the census row's report) |
