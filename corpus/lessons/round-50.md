# Lessons — round 50

Round: 50 (hyaku campaign, attempt 1). Lane base `f30464660c675d1c1e2851a3bf0366a3aaffe5a8`. Claims:
C1 adjacency — kotoba's `SKILL.md` frontmatter `description` names the census lanes classed non-`none`,
each in a clause with an ownership or routing word (guard line 5 of 9 → 9 of 9); C2 operability —
deleting any one of the 6 must-fail cases from `verifiers/fixtures/dispatch-prompts/manifest.json`
makes `--box-proof` exit 1 (0 of 6 → 6 of 6). Plan: `plans/round-50.md` (with its re-sizing notes).
Wave evidence: `.ufo/waves/round-50/build/`.

## Mistakes

`captured-by` names the criterion or instrument that should have caught the class;
`none → Qnn` means nothing caught it and this round adds the criterion.

|class|evidence pointer (command → output)|captured-by|fix|
|---|---|---|---|
| M31 A claim's headline asserted properties its counter never measured (twice in round 49: the adjacency row's "from their own bytes … 0 contested" and the operability headline's "executed") | `git show 374ecf98:PROVINCE.md \| awk '/^## Adjacent/{f=1;next} /^## /{f=0} f' \| grep -cE '^\| (audio\|chousa\|…\|tsukuroi) \| (contested\|adjacent\|none) \| [0-9a-f]{40} \|'` → 20, exit 0 — one integer, no classification; the census's own `names kotoba` column reads `no` for 7 of the 9 `adjacent` rows, so "from their own bytes" is false on the census's own table; on a clone at `374ecf98` with kake reclassified `contested` in both the census and `PROVINCE.md` the same counter still prints 20 and the cited guard `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` still exits 0 (`rows 20 verified 20`, `province rows 20 matched 20`) while the split reads 8 adjacent / 1 contested / 11 none (seat `.ufo/waves/round-50/build/MineMistake.md`, 2026-10-22). C2: `python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json` → `boxes proven 2`, exit 0, while the headline says "dispatch-prompt boxes executed" and `plans/round-49.md` says "The full `dispatch.08` box is executed, state clause included"; the proof covers six named conjuncts with one fixture each and `LOG.md:2382` names four box clauses with no fixture (unsubstituted variable before the report path, non-digit round folder, `≤` equality boundary, legacy-state arm; `SKILL.md:131-133` names three, `SCORECARD.md:255` two), and deleting a must-fail case leaves `boxes proven 2`, exit 0 (`.ufo/waves/round-49/falsify/ReplayC2BoxProof.md` M1/M2/M3/M5/M6; reproduced 2026-10-22: six of six removals → exit 0, `boxes proven 2`, `killed 0 of 6`) | none → Q26 (Q25 was met in form: each counter was shown able to fail and a content guard was cited; Q13, Q14 and Q19 were met too — they bind form, not the statement) | Q26. The round-49 headlines are re-stated with their bounds (SCORECARD append; the `box_proof` docstring stops saying "every conjunct" — routed D2/D4), and both round-50 statements are written as exactly what their counters print (`plans/round-50.md` C1/C2: the frontmatter name count, and `killed K of 6` over the manifest's must-fail cases). |
| M32 Misroot sweep run before the last seat returned | `git -C /home/vgpnk/Projects/shokunin status --porcelain` at round-50 start → `?? .ufo/waves/round-49/`; the file `.ufo/waves/round-49/falsify/RowGameDev2d.md` (13,630 B, sha256 `37aaa836…`, mtime 2026-10-22T11:38:25Z) is a round-49 kotoba falsify seat report written into the fleet root, after the round-49 report's sweep line ("shows no file from this round's seats") was filed at fleet `8bf9073`; the lane had no copy (`cmp` → no such file) | the addendum's misroot sweep (§6 item 3), run once at filing while 12 seats were still running | the sweep runs again after the last seat returns and before the last addendum; this round copied the file byte-exact into `.ufo/waves/round-49/falsify/RowGameDev2d.md` (`cmp` equal), deleted the fleet copy, and the round-50 report's sweep line is written after every seat has returned |

Q26 is shown able to fail: applied to the two round-49 claim statements it fails both, and applied to
the two round-50 statements as re-sized before landing it passes both (seat
`.ufo/waves/round-50/build/MineMistake.md`). This round's first plan repeated the class before landing:
its C1 statement said "frontmatter names" while the counter read every frontmatter line and folded no
case (a bare or capitalised list printed 9; seat `CriticC1Sizing.md` F1-F3), and its C2 milestone said
"enforces its case coverage" while a manifest hash pin also printed 6 of 6 (`CriticC2Sizing.md` F1). Both
were re-sized in `plans/round-50.md` before any landing.

## Gate

**Admitted:**
- Knowledge: an appended round-50 section of `corpus/knowledge/sibling-overlap-census-round49.md`
  (no tie-break between overlapping descriptions on six more client pages; every documented
  "which one wins" rule is keyed on the skill name), citing S024-S029, S022 and S019. Candidates 1,
  admitted 1.
- Criterion Q26 (`corpus/QUALITY.md`), grounded in M31.
- Source rows S024-S029 (new, `mined`); S019 and S022 re-opened byte-identical.

**Rejected, with reasons:**
- The first C1 counter (case-sensitive name count over the whole frontmatter): a capitalised repeat and
  a YAML comment each printed 9 with fewer lanes in the description (`CriticC1Sizing.md` F1-F2).
- The first C2 counter design (a FAIL count taken from the measured revision's own manifest, any exit 1
  counted as a kill): a hash pin and a traceback both scored 6 of 6 (`CriticC2Sizing.md` F1, F5, F6).
- Three drafted rows not written: the Copilot concept page (it carries no description role and no rule;
  the how-to page S027 carries the role), the Copilot SDK skills page (provider catalogs, not
  SKILL.md routing), and the Gemini CLI source-code row (S029's docs page carries the name-keyed rule;
  the code confirms it but no claim needs it). Seat reports `SrcCopilotSkills.md`, `SrcGeminiCliSkills.md`.
- The opencode docs row's draft status `queued`: written as `mined` because the census section cites it;
  its scope cell keeps the bound that the page describes opencode's current release, not v1.19.3
  (rounds 47-48 excluded it on that ground; S016 stays the authority for v1.19.3 behaviour).
- `DescDraft` seat output not used; the L1 wrote the description from the critic constraints (1,024-
  character cap, first 99 characters unchanged, admitted side of each split only) and the guard.

**Rows written this round** (each opened on 2026-10-22 by a build-wave seat; the seat report holds the
full fetch record):

| row | URL | accessed (UTC) | quote, at most 25 words (location) |
|---|---|---|---|
| S024 | https://opencode.ai/docs/skills.md | 2026-10-22T12:31:20Z | "OpenCode lists available skills in the `skill` tool description." (§ Recognize tool description, `skills.md:110`) — seat `.ufo/waves/round-50/build/SrcOpencodeDocs.md` |
| S025 | https://code.visualstudio.com/docs/agent-customization/agent-skills | 2026-10-22T12:29:33Z | "Copilot reads the skill's `name` and `description` from the YAML frontmatter." (§ How Copilot uses skills, step 1 Discovery, `agent-skills.md:302`) — seat `.ufo/waves/round-50/build/SrcVSCodeSkills.md` |
| S026 | https://code.claude.com/docs/en/sub-agents | 2026-10-22T12:28:30Z | "When Claude encounters a task that matches a subagent's description, it delegates to that subagent, which works independently and returns results." (§ Create custom subagents, `sub-agents.md:11`) — seat `.ufo/waves/round-50/build/SrcClaudeSubagents.md` |
| S027 | https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills | 2026-10-22T12:30:10Z | "**description** (required): A description of what the skill does, and when Copilot should use it." (frontmatter field list, `add-skills.md:33`) — seat `.ufo/waves/round-50/build/SrcCopilotSkills.md` |
| S028 | https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference | 2026-10-22T12:31:51Z | "**Agents and skills** use first-found-wins precedence." (§ Loading order and precedence, `cli-plugin-reference.md:415`) — seat `.ufo/waves/round-50/build/SrcCopilotSkills.md` |
| S029 | https://geminicli.com/docs/cli/skills/ | 2026-10-22T12:28:45Z | "If multiple skills share the same name, the version from the higher-precedence location is used." (§ Precedence and aliases, `skills.md:51-52`) — seat `.ufo/waves/round-50/build/SrcGeminiCliSkills.md` |

**Existing row re-opened:** S019 (Claude Docs — Agent Skills best practices), `https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md`, fetched 2026-10-22T12:28:47Z: 200, 42,169 B, sha256 `f0a5d61b…`, byte-identical to the bytes the row records. Quote: "Your description must provide enough detail for Claude to determine when to select this Skill" (§ Writing effective descriptions, `best-practices.md:215`). Status `mined` → `mined`; recheck `90d` → `90d`; `used-by` `SKILL.md, corpus/knowledge/frontmatter-rule-authorities-round48.md` → `SKILL.md, corpus/knowledge/frontmatter-rule-authorities-round48.md, corpus/knowledge/sibling-overlap-census-round49.md, corpus/lessons/round-50.md` (seat `.ufo/waves/round-50/build/SrcReopenS019.md`).

**Existing row re-opened:** S022 (Claude Code — Extend Claude with skills), `https://code.claude.com/docs/en/skills.md`,
fetched 2026-10-22T12:28:45Z and again at 13:04:07Z: 200, 111,557 B, sha256 `cdfcb0df…`, byte-identical to the
bytes the row records and to the round-48 fetch of the same route. Quote: "the combined `description` and
`when_to_use` text is truncated at 1,536 characters in the skill listing to reduce context usage"
(§ Frontmatter reference, `skills.md:389`). Status `mined` → `mined`; recheck `90d` → `90d`; `used-by`
`corpus/knowledge/sibling-overlap-census-round49.md` → `corpus/knowledge/sibling-overlap-census-round49.md,
corpus/lessons/round-50.md` (seat `.ufo/waves/round-50/build/SrcReopenS022.md`).

Status changes logged old→new: S024-S029 created as `mined` (used-by: the census entry and this lesson);
S019 `used-by` gains the census entry and this lesson; S022 `used-by` gains this lesson; S019 and S022
also gain anchor, scope and teaches text for the round-50 facts (seat reports carry each old→new cell).
No other row moved. Rows 23 → 29 (`grep -c '^| S0' corpus/SOURCES.md`).

### Erratum: the round-49 Gate recorded "rejected 0" (routed defect D5)

`corpus/lessons/round-49.md:21-24` reads "candidates 1, admitted 1, rejected 0". That line scoped
itself to knowledge entries, where "rejected 0" is literally true. As the round's gate record it is
false: round 49 rejected the items below, and a rejection is evidence of taste
(`corpus/QUALITY.md:38-39`). The round-49 lesson is append-only and owned by its round, so the
erratum lives here. Each item names what was rejected, the reason, and an evidence pointer.

| # | rejected | reason | evidence |
|---|---|---|---|
| 1 | the kasegi "prompt-injection exploits" clause | kasegi's tree never held it (`git grep` exit 1; `git log -S` empty) | `corpus/knowledge/sibling-overlap-census-round49.md:111-115`; `.ufo/waves/round-49/build/CensusKasegi.md:26-31` |
| 2 | kengaku's "route telemetry" clause | the sibling marks that surface ABSENT since 2026-10-15; the note copied the stale half | `.ufo/waves/round-49/falsify/RowKengaku.md:11-15` |
| 3 | mado's "no claim on kotoba ground" | mado surveys the omarchy skill file's frontmatter as its own surface | `.ufo/waves/round-49/falsify/RowMado.md:17` |
| 4 | kama's misquoted split | the quote dropped "agent" and "fallback" | `.ufo/waves/round-49/falsify/RowKama.md:29` |
| 5 | chousa's MINT.md "Rejected recipients" reading | the stated reason ("none is a scope surface") is wrong; MINT.md is a committed boundary record | `.ufo/waves/round-49/falsify/RowChousa.md:37` |
| 6 | kotodama's seat call `none` | overridden to `adjacent`: its description refuses kotoba's craft by name and `MINT.md:20` records the name collision | `corpus/knowledge/sibling-overlap-census-round49.md:60-63`; `.ufo/waves/round-49/build/CensusKotodama.md:19,30` |
| 7 | kake and kasegi's first-landing `none` | the rule's "either side" arm: kotoba's own description states the split (7 → 9 adjacent) | `corpus/knowledge/sibling-overlap-census-round49.md:143-149`; `.ufo/waves/round-49/falsify/CriticC1Landed.md:19,32` |
| 8 | tameshi's cited basis | the citation pointed at a wave report, an excluded surface; the row was re-based | `.ufo/waves/round-49/falsify/CriticC1Landed.md:26`; `.ufo/waves/round-49/falsify/RowTameshi.md:16` |
| 9 | tabi's `adjacent` | the split appears only in wave drafts; the row stays `none` | `corpus/knowledge/sibling-overlap-census-round49.md:54-55,171-176`; `.ufo/waves/round-49/falsify/RowTabi.md:23-26` |
| 10 | C1's name-count counter (10 → 20) | content-blind (CE1–CE4: a bare 20-name list also prints 20); re-sized to a classified, pinned row count | `plans/round-49.md:27-30,35-43`; `.ufo/waves/round-49/build/CriticC1Sizing.md:12,21-27`; `.ufo/waves/round-49/build/MineMistake.md:88-91` |
| 11 | C2's disposition-count counter (0 → 2) | content-blind (an unrelated instrument or a 10-byte stub still prints 2); re-sized to `boxes proven 2` | `plans/round-49.md:58-61,63-72`; `.ufo/waves/round-49/build/CriticC2Sizing.md:9-21`; `.ufo/waves/round-49/build/MineMistake.md:88-91` |
| 12 | M30's "the round-46 source does not carry the clause either" | false: that line carries the clause and mis-cites kasegi `PROVINCE.md:3-4`; the class and fix stand | `corpus/lessons/round-49.md:98-101`; `.ufo/waves/round-49/falsify/ReviewLessonQ25.md:12-19` |
| 13 | C2's "every per-conjunct mutant fails on its named conjunct" | the proof does not enforce its own coverage: removing the `d04-stem` case still prints `boxes proven 2` | `corpus/lessons/round-49.md:102-104`; `.ufo/waves/round-49/falsify/ReviewLessonQ25.md:20-29` |
| 14 | S022's "description alone" teaches cell | the page supports less than the cell claims; the cell was corrected | `.ufo/waves/round-49/falsify/ReopenS022.md:11-12` |
| 15 | the declared `dispatch.08` commitment ("executed … its live failures are findings") | the box was re-worded to a different authority before landing (`.round` → `.report-baseline`) and the plan never declared it; the old authority failed 166 of 289 prompts | `plans/round-49.md:76`; `.ufo/waves/round-49/falsify/CriticBoxReword.md:36`; `.ufo/waves/round-49/build/DispatchIndependent.md:25` |
| 16 | the round-48 entry's line 56 sweep and line 32 "24 probe fixtures" | the printed command gives 1 hit, not 0; no run list for 24 (21 of 23 reproduce) | `.ufo/waves/round-49/build/R4CountProvenance.md:14-21` |

Round 49 wrote no rejected source row: S022 and S023 were admitted and S018 stayed `mined`
(`corpus/lessons/round-49.md:39-40`); the registry's only `status=rejected` row is S011, rejected
2026-10-19. Carried, not rejected: the census guard's duplicate-row gap
(`corpus/lessons/round-49.md:105-106`), R5's unfrozen v2 oracle, R1's no-name fallback.
```


## Routed defects from the round-49 spot-check

- **D1 (report record):** the round-50 report keeps its filed header; every later lane head goes inside an
  appended addendum block at the end (seat `ReviewD1D5Facts.md` confirmed the round-49 pattern: one
  line-4 rewrite per addendum, nothing else removed).
- **D2 (calibration):** the `box_proof` docstring and `--box-proof` help now name the six conjuncts, the
  observed-status coverage rule, and the clauses without fixtures; the SCORECARD operability row carries
  the six-conjunct bound. Decision: `--box-proof` now enforces its own case coverage (C2) and runs from
  the checklist gate: `verifiers/verify_skill_checklist.py` check `checklist.box_map_complete` runs each
  delegated instrument's `--box-proof` and fails on a non-zero exit (seat `BoxProofGate.md`).
- **D3 (classification rule):** see the census entry's round-50 precedence section; the guard now rejects a repeated
  lane in either table (seat `CensusGuard.md`; the round-49 mutants M1, M2, M7, M8 from
  `MutCensusGuardBase.md` are the before-column), and `check_sibling_census.py` is registered in
  `verifiers/floors-registry.json` at 68 assertions.
- **D4 (calibration):** the SCORECARD adjacency row now says that kake and kasegi are `adjacent` because
  of kotoba's own description, not their own bytes, and that the round-49 "0 contested" had no
  precedence rule behind it.
- **D5 (gate record):** the erratum above and the separate admit and reject lists in this Gate.
- **D6 (carried):** R4 is carried because its two unprovenanced counts sit in a table no round-50
  counter reads; R5 because a v2 oracle must be frozen and pre-registered before measurement; R1's
  no-name fallback because it needs an identity-contract decision and a floor bump. All three are
  still open at `f3046466` (seat `CarryD6.md`, with commands).

## Falsify-wave corrections and additions (before the report)

Seat reports under `.ufo/waves/round-50/falsify/`. Recorded here, not rewritten above.

- **New admitted knowledge entry** `corpus/knowledge/skill-selection-rules-round50.md` (after
  `CriticLearningBar.md` found the census appendix could not meet Q12: the entry's `source:` line is
  round-49 and its recheck cannot fail on the round-50 text). The new entry's `source:` names S024-S029,
  S022 and S019, and its recheck re-fetches eight pages and prints `DRIFT <url>` for any page whose
  sha256 prefix moved (prints nothing at 13:36Z). Gate: candidates 1, admitted 1. A `SKILL.md`
  § Anti-patterns error-pattern paragraph now cites it. Knowledge files 36 → 37.
- **Gate line for the census precedence section:** admitted as a correction to an admitted entry
  (routed defect D3), then corrected again by `CriticPrecedenceLanded.md` (one definition of
  `contested`; kake and kasegi basis `kotoba`); the rule and the three closures are sent to the
  integrator (fleet `.ufo/l0-questions.md`, kotoba round-50 line, fleet-repository commit 8d56eb1).
- **Rejected:** the census sentence "every documented rule is keyed on the name" as written (S026
  `sub-agents.md:77` is a fit-based default, `CriticFrontierSweep.md`); "the only arbitration an author
  controls is the description" (S022 documents `when_to_use`, `disable-model-invocation`, `paths`,
  `CriticC1Landed.md`); the census list of the four added lanes (kengaku for kotodama); the kengaku
  clause "measured effects of prompt format" (now "measured capability effects of prompt format",
  1,019 of 1,024 characters; the guard still prints 9 of 9).
- **M31 fix cell:** it calls the C1 counter "the frontmatter name count"; the counter that landed is the
  guard line `skill description names K of N non-none lanes` (`plans/round-50.md` re-sizing notes).
- **Plan promise not kept as written:** the plan said the description edit would cite a new source row;
  source ids were kept out of the description (they cost characters and do nothing for triggering).
  The new `SKILL.md` § Anti-patterns paragraph cites the round-50 entry, which cites S024-S029.
- **C2 wording** (`CriticC2Landed.md`): "enforces its own case coverage" (D2 bullet above) is wider than the
  counter; the counter shows deletion of any one of the six labelled must-fail cases is caught. The
  driver can be laundered by a duplicate-id twin or an unlabelled twin (it then reports 6 of 6 while a
  single deletion passes), and its kill test accepts any stderr that contains the conjunct name
  (`ReviewDriver.md` F1); an unknown revision or a malformed manifest ends in a traceback, not exit 2
  (F2, F3). The landed manifest has unique ids and one labelled case per conjunct, so the measured
  6 of 6 holds for the committed bytes. Carried to round 51: reject duplicate ids, match the
  instrument's own coverage line, catch the two crash paths. `SKILL.md` § Run the verifier now lists
  the four clauses without a fixture (it listed three).
- **Gate gate-code survivors** (`MutBoxProofGate.md`): 4 of 12 mutants of the new checklist gate code
  survive its self-test (the `--map` argument dropped, help read from stdout only, the summary from
  stderr, the working directory); the live gate behaves correctly. Carried.
- **Calibration count** (`CalibrationRecords.md`): 5 mismatches of 51 round-50 statements at `956ee16`;
  fixed after: the two SCORECARD qualifiers sat inside older shell commands (moved to the end of each
  evidence cell), the `Round 50 completed` line said "D4 qualifiers" for both, the LOG named two of
  the four build seats that left no usable report, and the lesson's D4 bullet disagreed with the
  census basis column (the census basis is now `kotoba`, matching the lesson).
- **D1 bullet corrected** (`.ufo/waves/round-50/falsify/ReviewD1ReportPattern.md` F1-F3): the line-4
  rewrite it cites is the defect, not a pattern to follow. The rule the round-50 report follows: the
  filing commit's lines are frozen (line 4 included); each addendum is one block appended at the end,
  naming the lane head it describes by the helper's `landed <hash>`; a correction is a new sentence in
  the block. Check per addendum commit <c> (with <n> = the line count of the report at <c>^, and
  <report> = the round-50 kotoba report path in the fleet repository's reports directory):
  `git -C <fleet> diff -U0 <c>^ <c> -- <report> | awk -v n=<n> 'f && /^-/{r++} /^@@/{f=1; h++; if ($0 ~ "^@@ -" n ",0 [+]") e++} END{print "removed", r+0, "non_EOF", h-e+0}'`
  must print `removed 0 non_EOF 0`; on the four round-49 addenda it prints `removed 1 non_EOF 1` each.
- **Three in-place edits of this lesson's own lines before filing, disclosed:** the D3 bullet's pointer
  (it named a heading that does not exist; now the census precedence section); a backticked fleet
  commit token in the Gate addition (the corpus integrity gate read it as an unresolvable lane commit;
  now written without backticks); and the D1 check command above (its literal report path and commit
  letter read as a dead report pointer and a non-hash commit; now placeholders). All three changed only
  this round's own text.
