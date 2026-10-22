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
- `adjacent`: either side's committed scope surfaces (SKILL.md including its frontmatter description,
  PROVINCE.md, corpus files) state a split of one artifact, function or trigger area between the sibling
  and kotoba. On kotoba's side this includes its own description at the base commit, which names kagi,
  kake, kasegi, kengaku and kumitate as owning their own SKILL.md content while kotoba audits and reports
  (`SKILL.md:10-12` at `a5adc146`), and its base `PROVINCE.md` § Adjacent lines that state a split
  (chousa, kumitate, kengaku, tameshi).
- `none`: neither of the above; the seat report carries the sweep that found no claim (Q14).
- Wave reports and run logs (`.ufo/`, `reports/`) are not scope surfaces: a split stated only there does
  not make a row `adjacent` (mado's round-18 wave report is the case in point; seat `RowMado.md`).
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
| kake | master | e73d48bbf20759fc7758afaebf841fa02e5cfbbf | SKILL.md | adjacent | no | no | PROVINCE.md:3 | "**Domain:** web properties & publishing — scopes ds4cc.com, kimi.page/pro mirrors, Pages deploys" |
| kama | master | c808ba07f09c4be55413d3d6516c542ab69b64f8 | SKILL.md | adjacent | no | no | SKILL.md:8 | "Local model serving & endpoint health. This lane answers exactly one question:" |
| kasegi | master | 1fafde8f11454f3b0b98ab7f2b2e640aaf7f399a | SKILL.md | adjacent | no | no | PROVINCE.md:3 | "bounty & security research — scopes ~/Projects/bounties, program rules, claim packages" |
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
- 9 adjacent, 11 none, 0 contested — `awk -F' \\| ' '/^\| [a-z0-9-]+ \| (main|master) \| [0-9a-f]{40} \|/{print $5}' F | sort | uniq -c`.
  Adjacent: chousa, kagi, kake, kama, kasegi, kengaku, kotodama, kumitate, tameshi.
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
   kotodama (`sed -n 1,16p SKILL.md | grep -c kotodama` → 0 at `a5adc146`). The two lane names collide
   (kotodama `MINT.md:20`), so a request that says "kotoba" or "words" can reach either. The fix is a
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

## Falsify-wave corrections (round 49, before the report)

- **Classification rule applied consistently** (seat `../.ufo/waves/round-49/falsify/CriticC1Landed.md`): the
  first landing counted a one-sided published split for kotodama but not kotoba's own description, which
  names kake and kasegi as owning their SKILL.md content while kotoba audits. kake and kasegi are now
  `adjacent` (7 → 9 adjacent, 13 → 11 none). kasegi's adjacency rests on that description, not on the
  withdrawn "prompt-injection" clause. tameshi's basis is kotoba's base `PROVINCE.md` line ("tameshi —
  verification-fixture craft and mutation testing", sibling-owned ground), with tameshi's own wave report
  as corroboration only.
- **The guard re-derives what it can** (same seat showed an all-`none` pair passed): the skill-file,
  names-kotoba and arbitration cells are now recomputed from the pinned `SKILL.md`; a `none` row whose
  sibling description or `PROVINCE.md` names kotoba fails; a quote under six words fails. Still not
  machine-checked: an `adjacent` call that rests on a kotoba-side or corpus-side statement.
- **S022 says more than "description alone"** (seat `ReopenS022.md`): Claude Code also lists
  `when_to_use`, always lists names, and under a 1% context budget drops descriptions of the least-used
  skills first (`skills.md:1207-1213`). That is listing priority, not a tie-break between two matching
  descriptions, so the "no documented tie-break" finding stands; the S022 `teaches` cell is corrected.
- **Routing:** the kaidoku and revenger overlap is already an open operator question
  (`/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` line 42, tsukuroi round 1); this round does not
  re-file it. The opencode config item is not sibling-to-sibling: kotoba is a wording claimant there
  (kama `corpus/knowledge/cross-lane-scope.md:29`), and this round filed it as an operator question.
- **kengaku** (seat `RowKengaku.md`): kotoba's base `PROVINCE.md` line carried "route telemetry", which
  kengaku marks absent since 2026-10-15; the boundary note is corrected. kengaku's round-25 census script
  counts trigger strings in other lanes' SKILL.md files, kotoba's included, and kengaku's `corpus/README.md`
  describes it as its own: a possible `contested` element, recorded for the integrator; the row stays
  `adjacent`. The `arbitration` column lists every fleet lane name the description contains other than the
  row's own lane, kotoba included.
- **mado** (seat `RowMado.md`): `none` holds under the rule, but the boundary note "no claim on kotoba
  ground" overstated it: mado surveys the omarchy skill file's frontmatter as its own documentation
  surface. The `none` notes in `PROVINCE.md` now say "no split with kotoba on its scope surfaces".
- **tabi** (seat `RowTabi.md`): tabi's round-16 wave drafts state a split with kotoba ("kotoba owns the
  craft of such text … Route craft findings to kotoba", tabi `.ufo/waves/round-16/drafts/DraftAdjacency.md:39`
  at the pin) over tool names, descriptions and schemas as agent-facing text. It never reached tabi's scope
  surfaces, so the row stays `none` under the rule's wave-report exclusion (stated after the first landing,
  above); a later round should ask tabi whether to land it. The build seat's sweep sentence "zero of those
  state a rule over skill/prompt authoring for another lane" was wrong for that draft.
- **tameshi** (seat `RowTameshi.md`): the boundary note cited a wave report and generalised "the
  SKILL-checklist instrument" to "its own checklist instruments"; corrected to tameshi's corpus ledger. Open:
  tameshi's Core names kagi's `corpus/checklist-run.sh`, which reads kagi's SKILL.md checklist section; read
  literally, "instruments over them" could make that `contested`. Recorded, not ruled; the row stays
  `adjacent`.
- **kama** (seat `RowKama.md`): the boundary note misquoted kama's split (dropped "agent" and "fallback");
  corrected verbatim. The split names agent files kama deleted on 2026-10-14. kama's
  `consumer-registry.md:91-92, 111-112, 325-326` audits agent prompt text and records a verdict on a sibling
  SKILL.md: read literally, a possible `contested` element. The rule gives no precedence between the
  `contested` and `adjacent` arms; recorded for the integrator, row stays `adjacent`. Seats `RowSouji`,
  `RowLore`, `RowGameDev2d` returned HOLDS or HOLDS-BOUNDED; RowLore notes the arbitration cell leaves out
  the row's own lane name, which the rule does not yet state.

## Round 50: six more client pages, and kotoba's own description

Appended round 50 (append-only; the sections above are unchanged). Seat reports are under
`../.ufo/waves/round-50/build/`.

- **No tie-break between overlapping descriptions, now on nine pages.** Round 49 swept S022, S023 and
  S018. Round 50 opened six more client pages (rows S024-S029, all opened 2026-10-22; fetch records in
  the seat reports and in `corpus/lessons/round-50.md` § Gate) and swept each with
  `grep -ciE` for `overlap`, `ambigu`, `precedence`, `tie[- ]?break`, `conflict`, `multiple skills`,
  `same name`, `prioriti`, `1024`, `truncat`. No page states a rule for two skills with different
  names whose descriptions both match. Every non-zero hit is located in the seat report and is about
  something else (a same-name collision, a length cap, site chrome or an unrelated sense):
  - S024 opencode docs (`skills.md`, 5,365 B): every arbitration term 0; `1024` 1 (the description cap,
    `skills.md:72`). The model sees all skills in the `skill` tool description (`skills.md:110`).
    Seat `SrcOpencodeDocs.md`.
  - S025 VS Code agent skills (`agent-skills.md`, 22,871 B): `precedence` 1, `same name` 1 and
    `multiple skills` 1, all about duplicate names; `overlap`, `ambigu`, `tie[- ]?break`, `conflict` 0.
    "Copilot reads the skill's `name` and `description` from the YAML frontmatter." (`agent-skills.md:302`).
    Seat `SrcVSCodeSkills.md`.
  - S026 Claude Code subagents (`sub-agents.md`, 110,784 B): delegation follows the `description`
    (`sub-agents.md:839`); the only arbitration is between same-name subagents, and even there the page
    says one is "chosen by filesystem read order rather than a documented precedence" (`sub-agents.md:176`).
    Its remedy for overlap is craft: "Make each description specific enough to route to the right
    subagent" (`sub-agents.md:1293`). Seat `SrcClaudeSubagents.md`.
  - S027 GitHub Copilot, adding agent skills (`add-skills.md`): "Copilot will decide when to use your
    skills based on your prompt and the skill's description" (`add-skills.md:233`); no overlap rule.
    S028 GitHub Copilot CLI plugin reference: "**Agents and skills** use first-found-wins precedence."
    (`cli-plugin-reference.md:415`), a name-keyed rule. Seat `SrcCopilotSkills.md`.
  - S029 Gemini CLI skills (`skills.md`, 5,763 B): "If multiple skills share the same name, the version
    from the higher-precedence location is used." (`skills.md:51-52`) — again name-keyed; `overlap`,
    `ambigu`, `tie[- ]?break`, `conflict` 0. Seat `SrcGeminiCliSkills.md`.
  - Re-opened, byte-identical to their recorded bytes: S022 (adds the 1,536-character listing cap on
    `description` plus `when_to_use`, `skills.md:389`) and S019 ("Maximum 1,024 characters",
    `best-practices.md:161`; "Always write in third person", `:206`). Seats `SrcReopenS022.md`,
    `SrcReopenS019.md`.
- **What this changes for craft.** Every documented "which one wins" rule found so far is keyed on the
  skill *name* (origin, location tier, first found). None compares descriptions. So the round-49
  consequence stands with more support: the only arbitration an author controls between two skills
  with different names is the text of each description. The round-49 sweep pattern `tie[- ]break`
  (above) missed the unhyphenated spelling; the round-50 pattern is `tie[- ]?break`.
- **kotoba's description now names the 9 lanes classed `adjacent`.** Finding 2 (kotodama is not named)
  and finding 3 (the description named 5 of 20) are acted on: the description at the round-50 landing
  names chousa, kagi, kake, kama, kasegi, kengaku, kotodama, kumitate and tameshi, each in a clause with
  an ownership or routing word, and keeps to the 1,024-character cap (1,008 characters). Checked by
  `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md`
  → `skill description names 9 of 9 non-none lanes`, exit 0 (5 of 9, exit 1, on the description at
  `f3046466`). The clause test is lexical: a clause that names a lane next to a false ownership word
  still passes (seat `CensusGuard.md`, mutant m9). For the four lanes added this round the description
  states only the side the census already admits (chousa's research method, kama's endpoint
  verification, kengaku's measured effects of prompt format, tameshi's fixture and mutation method).
  kake and kasegi are named because kotoba's own description already named them at the base; their own
  descriptions carry none of kotoba's trigger words (seat `CriticC1Sizing.md` F4), so naming them adds
  no measured trigger precision.
- **Line pins.** The citation `../SKILL.md:12-15` in § What decides refers to the description at
  `f3046466` (and at `a5adc146`); the round-50 description moved that note to lines 15-17.

## Round 50: precedence between `contested` and a stated split (routed defect D3)

Appended round 50 (append-only). Basis: critic seat `../.ufo/waves/round-50/build/CriticPrecedence.md`
and fact seats `RuleKama.md`, `RuleKengaku.md`, `RuleTameshi.md` (all read the pinned sibling bytes).
No vendor page decides this: the six pages opened this round document only name-keyed rules (section
above), so the precedence below is kotoba's own rule.

- **What `contested` means.** The sibling's scope surfaces claim an element of kotoba's `PROVINCE.md`
  § Core over text the sibling does not own. Reading or verifying a non-craft fact held in such text is
  not a claim: an endpoint value, a credential checklist item, or the kill rate of the owner's gate.
- **Precedence.** A claim makes the row `contested` unless the sibling's own scope surfaces state a
  split that assigns the claimed element. A split stated only by kotoba never overrides a sibling's
  claim, because kotoba could otherwise relabel any claim with one sentence of its own. A split stated
  only by kotoba may still make a row with no claim `adjacent`; it is a routing commitment kotoba must
  honour.
- **Basis of each `adjacent` row at `f3046466`** (sibling, kotoba, both), before this round's description
  edit adds kotoba's side for chousa, kama, kotodama and tameshi: chousa kotoba (no chousa-side split
  was cited; recorded, not re-swept this round); kagi both; kake both; kama sibling; kasegi both;
  kengaku both; kotodama sibling; kumitate both; tameshi sibling.
- **Rulings.** No row moves; the counts stay 9 adjacent, 11 none, 0 contested.
  - kama: the arm does not fire. kama's registry rows (`consumer-registry.md:91-92, 111-112, 325-326`
    at `c808ba07`) verify endpoint values and absences in instruction files; they judge no wording.
    kama's own split assigns the wording to kotoba ("**Kotoba** owns the instruction/agent surface and
    its model/fallback wording; **kama** owns independent verification of the target endpoint",
    `cross-lane-scope.md:29`). `adjacent`, basis sibling.
  - kengaku: the arm does not fire. Its round-25 census script reads only the `SKILL.md` of the lane it
    runs in (`plans/round25_census.sh` requires a lane root; seat `RuleKengaku.md`), and kengaku's
    `corpus/README.md:192` says only "frontmatter triggers". The round-49 boundary note that the script
    counts trigger strings in other lanes' files rested on kengaku's round-25 wave reports, which this
    rule excludes. `adjacent`, basis both (kengaku `SKILL.md:3`: "kotoba owns prompt and skill craft
    (kengaku keeps only measured capability effects)").
  - tameshi: the arm fires literally (its Core names kagi's `corpus/checklist-run.sh`, which reads
    kagi's `SKILL.md` checklist), but that instrument is kagi's, not an element of kotoba's § Core, and
    tameshi measures its kill rate read-only. tameshi's own split: "every lane's gate remains its own"
    and it "Never edits a sibling's gate code" (`PROVINCE.md:14-17` at `3b20f073`). `adjacent`, basis
    sibling.
  - mado stays `none`: the omarchy skill file it surveys belongs to no lane, so no § Core element over
    another lane's text is claimed.
- **Correction to the falsify-wave note above on kake and kasegi.** Their `adjacent` class does not rest
  on kotoba's description alone. Both siblings' corpora carry an aggregator-mirrored lesson that states
  the same split: "Aggregator-owned file; the owning lane corrects `SKILL.md`." (kake
  `corpus/lessons/round-5-aggregator-mirror-pathless-cli-invocation.md:4-5` at `e73d48bb`; kasegi
  `corpus/lessons/round-5-aggregator-mirror-ambiguous-citation-base.md:4-5` at `1fafde8f`; seat
  `CriticPrecedence.md` F3). Basis both.
- **Correction to § Classification rule.** Its sentence that kotoba's base `PROVINCE.md` lines "state a
  split (chousa, kumitate, kengaku, tameshi)" holds only for chousa and kumitate; the kengaku and
  tameshi lines named only the sibling's ground (`CriticPrecedence.md` F2). Both rows rest on the
  sibling-side splits cited above.
- **Guard.** `../verifiers/check_sibling_census.py` now fails a lane that appears in more than one row of
  either table (round 50), and it does not machine-check the basis column above.

## Round 50: falsify-wave corrections (before the report)

Appended round 50 (append-only). Seat reports under `../.ufo/waves/round-50/falsify/`.

- **"Every documented rule is keyed on the name" is too wide** (`CriticFrontierSweep.md`): Claude Code
  uses its built-in `claude` agent "When a task doesn't fit a more specialized agent." (S026
  `sub-agents.md:77`), a fit-based preference of any specialized agent over a built-in catch-all. The
  sentences above ("the only arbitration is between same-name subagents"; "Every documented 'which one
  wins' rule found so far is keyed on the skill *name*") hold for rules between two author-written
  skills or subagents, not for that built-in default. The ten-pattern sweep had no choice words
  (`choose`, `select`, `more speciali`); the wider sweep found only that line. The full account is
  `skill-selection-rules-round50.md`.
- **"The only arbitration an author controls ... is the text of each description" is false for Claude
  Code** (`CriticC1Landed.md`): S022 also documents `when_to_use`, `disable-model-invocation` and
  `paths` (`skills.md:390, 393, 403`). The description is the one lever every client here reads.
- **Wrong lane list:** "For the four lanes added this round" names chousa, kama, kengaku and tameshi;
  the four added were chousa, kama, kotodama and tameshi (guard at `f3046466`: missing chousa, kama,
  kotodama, tameshi). The kengaku clause was also widened in the landed text ("measured effects of
  prompt format"); kengaku keeps "only measured capability effects" (kengaku `SKILL.md:3`), so the
  description now reads "measured capability effects of prompt format" (1,019 of 1,024 characters).
- **"Ownership or routing word" is wider in the guard:** its marker list also accepts `see above`,
  `as above` and `see also` (`CriticC1Landed.md`), so a clause such as "chousa: see above" passes.
- **Precedence section, two definitions** (`CriticPrecedenceLanded.md`): the round-50 definition of
  `contested` supersedes the round-49 bullet in § Classification rule, and it is limited to text owned by
  another fleet lane (another lane's `SKILL.md`, prompts or AGENTS.md-class files, or kotoba's own
  instruments). Read that way, mado's survey of the omarchy skill and game-dev-3d's judgments on
  vendored upstream skills (`adaptation-kimi.md:330-331`) concern files no fleet lane owns, so both
  stay `none`. A split counts only when it assigns the element to someone other than the claimant.
- **kake and kasegi basis is `kotoba`, not `both`:** the sibling-corpus lessons cited above say "Filed by:
  kotoba round-5 report" and "Aggregator-owned file"; they relay kotoba's own finding and are not a
  sibling-stated split. No row moves.
- **Kotoba ruled on its own boundary.** The three round-49 open items (kama, kengaku, tameshi) are
  closed here by kotoba's own rule; that rule and those closures are sent to the integrator as an
  operator question (fleet `.ufo/l0-questions.md`, kotoba round-50 line) and stand as kotoba's reading
  until answered.
- **S025 bullet** (`ReopenS025.md`): `multiple skills` 1 is not about duplicate names; it is "Combine
  multiple skills to build complex workflows" (`agent-skills.md:15`). The page also has `1024` 1 (the
  description cap, `:148`), and its one `precedence` line (`:64`) sits inside an experimental
  Codex-integration note. The no-tie-break reading of S025 is unchanged.
- **kama ruling, corrected reasoning** (`RowKamaR50.md`): "they judge no wording" is false. kama's
  `consumer-registry.md:91-92` ("only consumer with no fallback", "cascade-protected") judges fallback
  statements in agent files; the registry's own errata mark those rows historical and the files no
  longer exist. Rows 111-112 concern kengaku's file, not kotoba's. So the claim arm fires on kama, and the
  row is `adjacent` because kama's own split assigns that wording to kotoba (`cross-lane-scope.md:29`),
  which is the precedence rule's sibling-split exit. Under a claim-always-wins precedence it would be
  `contested`; the class does not change the C1 count (both are non-`none`).
- **§ intro "from each sibling's own committed bytes"** holds for the quotes and the mechanical columns;
  for chousa, kake and kasegi the `adjacent` class rests on kotoba's side (basis `kotoba`).
- **tameshi ruling, corrected reasoning** (`ReviewProvinceRows.md` M2): "tameshi measures it read-only"
  is not supported (its ledger lists kagi's `checklist-run` as unmeasured by sweep), and the earlier
  boundary text "kotoba owns the SKILL-checklist instrument" had no split behind it. The claim arm fires
  literally; the row is `adjacent` through tameshi's own split ("every lane's gate remains its own",
  `PROVINCE.md:14-17`), the precedence rule's sibling-split exit.
- **tameshi, second reading** (`RowTameshiR50.md`): tameshi's only measurement of kagi's
  `checklist-run.sh` is its self-test kill rate (`corpus/knowledge/mutation-case-kagi-checklist.md:47-52`
  at `3b20f073`), which the round-50 definition excludes ("the kill rate of the owner's gate"), so under
  that definition no claim exists; under the literal round-49 wording the arm fires and tameshi's own
  split clears it (`PROVINCE.md:14-18`). `adjacent` either way. The basis labels in the precedence
  section are the basis at `f3046466`; kotoba's round-50 description adds kotoba's side for chousa,
  kama, kotodama and tameshi, so those rows read `both` from round 50 (chousa stays `kotoba` plus its
  own domain line). The guard checks neither definition nor basis.
- **kengaku ruling, corrected premise** (`RowKengakuR50.md`): the round-25 script does not read "only the
  `SKILL.md` of the lane it runs in"; it reads the lane root it is run from (87 paths in a traced run),
  and pointed at a directory holding kotoba's `SKILL.md` it prints `skill_frontmatter_triggers=8`. The
  row's "no claim" rests on the scope-surface rule: the script's cross-lane runs are recorded only in
  kengaku's wave reports, which § Classification rule excludes. kengaku's corpus also carries connector
  reports that read kotoba instruments (`r10-connector.md`, `r11-connector.md`) as design evidence, and
  `corpus/evidence/round9-fleet/sibling-overlap.md:12` labels the relation "Contested" before resolving
  it to the split in its own ruling; neither is an audit claim, and both are recorded for the integrator
  with the round-50 L0 line.
