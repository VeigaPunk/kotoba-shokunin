source: S022 (https://code.claude.com/docs/en/skills, § Frontmatter reference `description` row, § Resolve skills that share a name, § Troubleshooting → Skill triggers too often), S023 (https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview, § Level 1: Metadata (always loaded)), S018 (https://agentskills.io/specification, § `description` field); sibling bytes: the 20 sibling lane repos under /home/vgpnk/Projects/shokunin/*-shokunin at the commits pinned in the table below
verified-at: 2026-10-22
recheck: python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md  # exit 0 and "rows 20 verified 20" on 2026-10-22; exit 1 names the row whose quote, commit, classification or PROVINCE row no longer matches

# Fleet sibling-overlap census (round 49)

Frontier area: sibling arbitration (`corpus/README.md` § Known gaps: "0/5 descriptions carry an
arbitration clause", measured at round 7 over five lanes). The fleet now has 20 sibling lanes, and
kotoba's `PROVINCE.md` § Adjacent named 10 of them at `a5adc146`. This entry classifies all 20
against kotoba's province, from each sibling's own committed bytes at a pinned commit, and records
what each sibling's skill description says about its neighbours. It reports sibling scope; it
does not absorb it, and it does not edit any sibling (adjacency axis, `../AXES.md`).

## What decides between overlapping skills (sources opened 2026-10-22)

- The description is the matching input. Claude Code: "What the skill does and when to use it.
  Claude uses this to decide when to apply the skill." (S022, `skills.md:389`). Anthropic's overview:
  "Claude loads this metadata at startup and includes it in the system prompt." (S023,
  `overview.md:59`), and the description "is what Claude matches your request against when
  determining whether to trigger the Skill" (S023, same section).
  The open specification says the same of the field: it "Should describe both what the skill does and
  when to use it" (S018, `specification.md:102`; a recommendation, not a `Must`), and it states no rule
  for overlapping skills (`grep -cinE 'overlap|ambiguit|precedence|disambiguat|tie[- ]?break|arbitrat|multiple skills'`
  over the fetched 7,608 B file → 0; seat `SrcSpecDescriptionField.md`).
- Neither page states a tie-break rule for two descriptions that both match. Sweeps over the fetched
  markdown: S022 `arbitrat`, `tie-?break`, `ambigu`, `overlap` → 0 each; S023 nine patterns
  (`tie[- ]break`, `overlap`, `ambigu`, `multiple skills`, `one skill`, `arbitrat`, `conflict`,
  `both skills`, `select`) → 0 each (seat reports `SrcClaudeCodeSkills.md`, `SrcAgentSkillsOverview.md`
  under `../.ufo/waves/round-49/build/`).
- What S022 does give: a name clash is settled by origin ("When two skills share a directory or file
  name, where each one came from decides which one `/name` runs.", `skills.md:198`), and a skill that
  fires where it should not is fixed by a more specific description or `disable-model-invocation: true`
  (§ Troubleshooting, `skills.md:1190-1195`).
- Consequence for craft: with no documented tie-break, the only arbitration a skill author controls is
  the text of each description. A description that names its neighbour and says who owns what is the
  whole mechanism. That is why kotoba's trigger-fidelity box `trigger.05` asks for a concrete sibling
  arbitration rule in the description (`../SKILL.md` § Trigger-fidelity checklist).
- Limit on this host: the shokunin lane `SKILL.md` files are not in an omp skill discovery root
  (kotoba's own description says so, `../SKILL.md:12-15`; critic seat `CriticC1Sizing.md` found no lane
  `SKILL.md` in the ten discovery roots it checked). So the arbitration columns below are audit-side
  facts about the files, not observed router behaviour.

## Classification rule

- `contested`: the sibling's committed scope surfaces claim part of kotoba's core (writing or auditing
  other lanes' SKILL.md, prompts or AGENTS.md-class files, or the instruments over them).
- `adjacent`: either side's committed scope surfaces (SKILL.md, PROVINCE.md, corpus files) state a split
  of one artifact, function or trigger area between the sibling and kotoba.
- `none`: neither of the above; the seat report carries the sweep that found no claim (Q14).
- `names kotoba` and `arbitration` are mechanical: whether the frontmatter `description` at the pin
  contains the token `kotoba`, and which sibling lane names (case-insensitive, whole token) it contains.
  `no SKILL.md` means the lane has no skill file at the pin.

One override of a seat's call: kotodama's seat chose `none`; this entry records `adjacent`, because
kotodama's description refuses kotoba's craft by name ("NOT prompt/skill craft (kotoba-shokunin)",
kotodama `SKILL.md:3`) and its `MINT.md:20` records the name collision ("kotoba owns prompt/skill craft
despite its name"). That is a published split of a trigger area.

## Census (20 rows; quotes verbatim at the pinned commit, whitespace collapsed)

| lane | branch | commit | skill file | classification | names kotoba | arbitration | scope quote at | scope quote |
|---|---|---|---|---|---|---|---|---|
| audio | main | 7a2fcd4f08831154686e4e323031f41fffdb077f | NONE | none | no SKILL.md | no SKILL.md | PROVINCE.md:3 | "Owns: game audio production — SFX (UI, impacts, movement, ambience) and soundtrack (motifs, loops, stems, adaptive layers)" |
| chousa | master | 6c5eb1466f2b8abbd3de576389037f435016d07b | SKILL.md | adjacent | no | yes: kasegi, kengaku | PROVINCE.md:3 | "**Domain:** deep-research method (調査) — the reusable craft of source research." |
| game-dev-2d | main | 7753d49b16674e122ed134403e7a9b301f2cbf7e | NONE | none | no SKILL.md | no SKILL.md | PROVINCE.md:3 | "Owns: 2D game production verified by executable headless fixtures — loop, input, physics, scenes, camera, UI, levels, juice, export readiness." |
| game-dev-3d | main | 89dd182b70943a20ae9aa6c1ed0e3c9b6e79c080 | SKILL.md | none | no | yes: game-dev-2d, revenger | PROVINCE.md:3 | "Owns: 3D game production verified by executable headless fixtures — 3D movement and collision, spatial queries, camera projection and frustum behavior" |
| kagi | master | 899c50b42634a3a4ad0b28ab7509786315e2fc2b | SKILL.md | adjacent | no | no | PROVINCE.md:3 | "secrets & vault ops — the-janitor flows, credential hygiene evidence" |
| kaidoku | main | 08c7a7299ed61c3fdc30ddb0adfe4e812d5eac76 | SKILL.md | none | no | no | SKILL.md:3 | "Domain specialist — reverse engineering of shipped artifacts with REA on this Linux host" |
| kake | master | e73d48bbf20759fc7758afaebf841fa02e5cfbbf | SKILL.md | none | no | no | PROVINCE.md:3 | "**Domain:** web properties & publishing — scopes ds4cc.com, kimi.page/pro mirrors, Pages deploys" |
| kama | master | c808ba07f09c4be55413d3d6516c542ab69b64f8 | SKILL.md | adjacent | no | no | SKILL.md:8 | "Local model serving & endpoint health. This lane answers exactly one question:" |
| kasegi | master | 1fafde8f11454f3b0b98ab7f2b2e640aaf7f399a | SKILL.md | none | no | no | PROVINCE.md:3 | "bounty & security research — scopes ~/Projects/bounties, program rules, claim packages" |
| kengaku | master | 1f3b0f1ec41ec297130e8944ff97968d32324632 | SKILL.md | adjacent | yes | yes: chousa, kama, kotoba, kumitate, tameshi | SKILL.md:3 | "Domain specialist — LLM/model research & evaluation — eval design, benchmark selection, offline replay grading, blind shim-cascade leg attribution and interval-calibrated verdicts" |
| kotodama | main | 35f0d49f96f1d51f8b006136a8e1d0e8d0919a7a | SKILL.md | adjacent | yes | yes: chousa, kotoba, lore | SKILL.md:8 | "Domain: the generative craft that connects languages, cultures, myths, symbolisms, and eras to their linguistics and costumes for a fictional world" |
| kumitate | master | fac39171ac28c606e90da75fc2ba2ed3df52f4ea | SKILL.md | adjacent | no | no | PROVINCE.md:3 | "**Domain:** orchestration & tooling — scopes OMP task/hub, ufo-fsd scripts & runtime" |
| lore | main | 380ef3abc7c7af11d7f23e9f9c82bb1937e1f695 | SKILL.md | none | no | yes: chousa, game-dev-2d | PROVINCE.md:3 | "Owns: fictional-world records — entities (characters, places, factions, items), relations, timeline events — with consistency verification and sourced inspiration." |
| mado | master | e33ea30461f6e9bbeee40beef19770a953f7a105 | SKILL.md | none | no | no | SKILL.md:8 | "desktop & compositor craft playbook — the Hyprland/waybar/walker/terminal config plane" |
| mori | master | 28b79d3d1b76824f0c825aabe6cb6c5dc49961bf | SKILL.md | none | no | yes: kama, kumitate, tsukuroi | PROVINCE.md:3 | "fleet & host observability (森) — whether the fleet, its waves and its host are alive and progressing." |
| revenger | main | 876630dbb4d630e016d7d8c32a19ea04c646cbae | NONE | none | no SKILL.md | no SKILL.md | PROVINCE.md:3 | "Owns: reverse engineering of shipped artifacts — native binaries, managed assemblies, Electron/JavaScript packages, Android APKs, archives, firmware, browser/Electron runtime evidence" |
| souji | master | 4edb25dfe262515d0da63224bbba71e02e36cba5 | SKILL.md | none | no | yes: kagi | PROVINCE.md:3 | "**Domain:** fleet repository & workspace hygiene (掃除) — receipt-gated removal of stale, duplicate, and already-preserved artifacts." |
| tabi | master | e3cf4e0d30bb835532ff44b118c5ad52e09eb76d | SKILL.md | none | no | no | PROVINCE.md:3 | "browser & web-interaction craft (旅, journey) — driving real browsers against real sites with evidence discipline." |
| tameshi | master | 3b20f073c7305a582562cd323982991464c324f3 | SKILL.md | adjacent | no | yes: kama | PROVINCE.md:3 | "**Domain:** verification-fixture craft — the reusable method of honest checks: hermetic suites, mutation testing, fail-closed arms, verdict-line discipline, no-permissiveness audits, before/after proof." |
| tsukuroi | master | 22fd1642e7fa4dfbdfba4419a443f06ffbb0b6c0 | SKILL.md | none | no | no | PROVINCE.md:3 | "**Domain:** host operability & system repair (繕, mending) — the OS substrate itself: package state, systemd, drivers/firmware, boot health." |

Per-row evidence (pin commands, sweeps, overlap quotes): `../.ufo/waves/round-49/build/Census<Lane>.md`.

## Counts (each with its command, 2026-10-22)

Every command reads only table rows (the regex `^\| [a-z0-9-]+ \| (main|master) \| [0-9a-f]{40} \|`);
`F` is this file, `corpus/knowledge/sibling-overlap-census-round49.md`, run from the lane root.
Fields under `awk -F' \\| '`: `$4` skill file, `$5` classification, `$6` names kotoba, `$7` arbitration.

- 20 rows — `grep -cE '^\| [a-z0-9-]+ \| (main|master) \| [0-9a-f]{40} \|' F`
- 7 adjacent, 13 none, 0 contested — `awk -F' \\| ' '/^\| [a-z0-9-]+ \| (main|master) \| [0-9a-f]{40} \|/{print $5}' F | sort | uniq -c`.
  Adjacent: chousa, kagi, kama, kengaku, kotodama, kumitate, tameshi.
- 17 of 20 lanes have a skill file at the pin — `awk -F' \\| ' '/^\| [a-z0-9-]+ \| (main|master) \| [0-9a-f]{40} \|/{print $4}' F | sort | uniq -c`
  (17 `SKILL.md`, 3 `NONE`); audio, game-dev-2d and revenger have none (seed-form lanes).
- 2 of 17 descriptions name kotoba (kengaku, kotodama) — `awk -F' \\| ' '/^\| [a-z0-9-]+ \| (main|master) \| [0-9a-f]{40} \|/ && $6=="yes"' F | wc -l`
- 8 of 17 descriptions name at least one sibling — `awk -F' \\| ' '/^\| [a-z0-9-]+ \| (main|master) \| [0-9a-f]{40} \|/ && $7 ~ /^yes/' F | wc -l`.
  This supersedes the round-7 figure "0/5 arbitration clauses" (`alwayson-checklist-round7.md:56-57`)
  as a fleet measure; for the same five lanes (kagi, kake, kasegi, kengaku, kumitate) it is now 1/5
  (kengaku).

## Findings that change kotoba's records

1. **kasegi was classified on an unsourced clause.** Base `PROVINCE.md` § Adjacent said "kasegi —
   security research incl. prompt-injection exploits". `git -C ../kasegi-shokunin grep -qiE
   'prompt[- ]injection' 1fafde8f11454f3b0b98ab7f2b2e640aaf7f399a` exits 1 (no match), and kasegi's
   `PROVINCE.md` never contained `prompt` or `injection` (`git log -S` empty; seat `CensusKasegi.md`).
   The row is now `none`.
2. **kotodama → kotoba is not reciprocal.** kotodama's description routes prompt and skill craft to
   kotoba; kotoba's description names five siblings (kagi, kake, kasegi, kengaku, kumitate) and not
   kotodama (`sed -n 1,16p SKILL.md | grep -c kotodama` → 0 at `a5adc146`). The two lane names are near
   homonyms (言葉 and 言霊), so a request that says "kotoba" or "words" can reach either. The fix is a
   description edit; this round's drift guard keeps the SKILL.md frontmatter unchanged, so it is carried
   to the next round's plan.
3. **kotoba's two surfaces disagree.** The description names 5 of 20 siblings; § Adjacent named 10, with
   kagi and kake only in the description (seat `ConnectSiblingOverlap.md` § c). After this round
   § Adjacent names all 20 and the description still names 5: the gap is recorded, not closed.
4. **Sibling-to-sibling items seen, reported, not ruled on:** kaidoku and revenger both state "reverse
   engineering of shipped artifacts" as their domain (kaidoku `SKILL.md:3`, revenger `PROVINCE.md:3`),
   and kaidoku records that arbitration as open; kagi records `$HOME/.config/opencode` as
   `owner=integrator, status=unresolved` (kagi `corpus/adjacency.tsv:81`). Both belong to the integrator.
5. **Only one sibling pair arbitrates in both descriptions** (chousa and kengaku); seat
   `ConnectSiblingOverlap.md` § b lists 17 directed pairs across 8 descriptions.

## Limits

- Pins move: kake, kama and tameshi advanced during the census. Every claim is about the pinned commit;
  the recheck reads pinned bytes, never a branch tip.
- The classification is a judgment under the rule above; the two mechanical columns are not.
- `none` rows rest on each seat's sweep over the sibling's top-level scope files and a tree-wide token
  search; a claim stated only in an unread wave report would be missed (kagi's split lives in `corpus/`,
  which its seat read; a top-level-only sweep would have called kagi `none`).
