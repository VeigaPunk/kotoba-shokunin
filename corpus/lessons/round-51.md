# Lessons — round 51

Round: 51 (hyaku campaign, attempt 1). Lane base `43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10`. Claims:
C1 freshness — run against the installed omp 18.12.6, `verifiers/verify_surfaces.py --json` passes
5 of 7 → 7 of 7 (the two omp checks 0 of 2 → 2 of 2); C2 depth — `SKILL.md` § Anti-patterns names,
for K of 7 pinned clients, a reviewed removal-lever key term backed by a quote in
`corpus/knowledge/skill-overlap-levers-round51.md` and a `mined` row (0 of 7 → 7 of 7). Plan and
re-sizing: `plans/round-51.md`. Wave evidence: `.ufo/waves/round-51/build/`, `.ufo/waves/round-51/falsify/`.

## Mistakes

`captured-by` names the criterion or instrument that should have caught the class;
`none → Qnn` means nothing caught it and this round adds the criterion.

|class|evidence pointer (command → output)|captured-by|fix|
|---|---|---|---|
| M33 A gate rejection reason characterized a source page's content with no line behind it, and the page contradicted the reason | `corpus/lessons/round-50.md:44-45` reads "the Copilot SDK skills page (provider catalogs, not SKILL.md routing)"; the page, fetched 2026-10-22T14:19:50Z (HTTP 200, 35,455 B, sha256 `64856ff44e5481f3ccb16defbc80180874e463862ac12309ef23b18802d4b9f3`, byte-identical to the round-50 closure's fetch) reads at line 11 "A skill is a named directory containing a `SKILL.md` file", at line 289 "**`description`**: A short description of what the skill does." and at lines 805-810 § Skill conflicts: "Use `disabledSkills` to exclude conflicting skills" / "Reorganize skill directories to avoid overlaps" — file-based `SKILL.md` skills, the `description` field and a remedy for overlapping skills, so the reason is false on the page's own bytes | Q23 (a rule attributed to an authority carries a located quote from that authority; violated, and not applied in-lane) and Q14 (the same reason is a negative claim about the page's content with no sweep behind it); caught only by the non-author closure (`corpus/lessons/round-50-verifier-spotcheck.md:189,260-262`) | every Gate reject reason names the located line of the rejected source that decides it, or the sweep command that produced the absence; a reason may not characterize a page without a line. Round 51 appends the correction to the round-50 Gate and writes the page as a source row, because C2 cites it (`plans/round-51.md` D4). |
| M34 A seat recorded as cancelled wrote its report after the round report was filed, and the leftover sweep was gated on seat return, not on seat write | `/home/vgpnk/Projects/shokunin/.ufo/reports/round-50/kotoba.md:96-97` reads "0 died; 2 cancelled by the L1 after an hour without a report (`DescDraft`, `D2D4Wording`; their work was done by the L1)" and line 112 reads "Misroot sweep (run after every seat returned): one round-49 kotoba seat report found in the fleet root, moved into the lane byte-exact and removed (lesson M32); nothing from round-50 seats"; the report was filed at fleet `cc7d642` (2026-10-22T10:52:09-03:00); `.ufo/waves/round-50/build/D2D4Wording.md` (18,592 B, sha256 `bb7679ad…`) was written 10:51:16-03:00 and is committed in the lane tree at the round-51 base (`git ls-tree 43ca0bfb .ufo/waves/round-50/build/D2D4Wording.md` → blob `c26b2465…`), and `.ufo/waves/round-50/build/DescDraft.md` (10,079 B, sha256 `0181a459…`) was written 10:52:19-03:00 — 10 s after the filing and 30 s before the driver completion (`/home/vgpnk/Projects/shokunin/.ufo/watchdog.log:705`, 10:52:49-03:00) — and is still untracked at the round-51 base (`git status --porcelain` → `?? .ufo/waves/round-50/build/DescDraft.md`); M32's own fix cell (`corpus/lessons/round-50.md:18`) gates the sweep on "the last seat returns", which is the gate the round-50 record used | none → Q27 (Q06's denominator was right: 33 declared build seats in `.ufo/waves/round-50/build-spec.json`, and the report's "33" matches it; Q05 in form: M32's fix shipped no arm that could fail on a seat writing after the sweep) | the seat record counts a seat that wrote as written whatever its status, and the leftover sweep runs after the last seat write, over every directory a seat can write to, with its command printed. Round 51 commits `DescDraft.md` byte-exact with a disposition line, corrects the seat accounting in the lesson and the LOG, and runs the sweep after the last seat write (`plans/round-51.md` D1). |

Q27 (added to `corpus/QUALITY.md` this round) is shown able to fail: applied literally to the round-50
record it fails on the report's seat line ("2 cancelled … `DescDraft`, `D2D4Wording`") and its sweep
line ("run after every seat returned … nothing from round-50 seats"), because both seats wrote files
after that point (seat `.ufo/waves/round-51/build/MineMistake.md` § Q27 shown able to fail). M33 is
caught by Q23 and Q14 as written; the round-50 Gate violated them and only the non-author closure
caught it, so no new criterion is added for M33: this round's Gate gives a page line for every
reject reason.

## Gate

### Admitted

- **Entry `corpus/knowledge/skill-overlap-levers-round51.md`** (C2): supersedes finding 4 of
  `skill-selection-rules-round50.md`. Clears Q12 (source rows, `verified-at`, a recheck that runs),
  Q14 (the negative "none decides between two remaining candidates" carries the seven seats' sweeps,
  each pasted in its `Src*.md` report), Q23 (each lever quoted from its own vendor page) and Q26 (the
  claim statement was re-sized to the counter before landing, `plans/round-51.md`).
- **S030 (new row)** — GitHub Docs, Copilot SDK custom skills —
  https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills (fetched as `.md`), opened
  2026-10-22T14:19:11Z by seat `SrcCopilotSdk`, HTTP 200, 35,455 B, sha256 `64856ff4…`, byte-identical
  to the round-50 fetch; re-fetched by the L1 at 15:08Z, same hash. Quote: "Use `disabledSkills` to
  exclude conflicting skills" (`skills.md:809`). Tier A, `docs`, `mined`, `used-by` the new entry,
  this lesson and `skill-selection-rules-round50.md` (whose falsify-wave correction already cites
  the page). Writing this row answers routed defect D4's "decide whether to write the row".
- **S031 (new row)** — GitHub Docs, Copilot CLI command reference —
  https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference (fetched
  as `.md`), opened 2026-10-22T14:19:21Z by seat `SrcCopilotCli`, HTTP 200, 461,944 B, sha256
  `c61997ef…`. Quote: "Use the `ignoredSkillsLocations` setting to exclude specific directories
  (and their descendants) from discovery, regardless of which location above would otherwise
  surface them." (`cli-command-reference.md:1300`, 22 words). Tier A, `docs`, `mined`, `used-by` the
  new entry. S028 (the plugin reference) was not used: it does not carry this lever.
- **S021, S022, S024, S025, S029 re-opened** (seats `SrcCodex`, `SrcClaudeCode`, `SrcOpencode`,
  `SrcVSCode`, `SrcGemini`; the L1 re-fetched each quoted page at 15:08Z): each page was
  byte-identical to the hash already recorded (`ed6e324f…`, `cdfcb0df…`, `f10ced73…`, `de5ba34f…`,
  `8e1b4cbe…`). Quotes as in the entry's table: S021 `build-skills.md:218`, S022 `skills.md:886`,
  S024 `skills.md:230`, S025 `agent-skills.md:289`, S029 `skills.md:94`.
- **Q27 (new criterion)**, grounded in M34.

`used-by` changes (old → new; the only in-place cell changes, contract v1 rule 2):

- S021: `corpus/knowledge/frontmatter-rule-authorities-round48.md` → `corpus/knowledge/frontmatter-rule-authorities-round48.md, corpus/knowledge/skill-overlap-levers-round51.md`
- S022, S024, S025, S029: `corpus/knowledge/sibling-overlap-census-round49.md, corpus/lessons/round-50.md, corpus/knowledge/skill-selection-rules-round50.md` → the same plus `, corpus/knowledge/skill-overlap-levers-round51.md`

No `status` or `recheck` cell changed. S024's `teaches` cell names only name uniqueness and
`opencode/autoinvoke` as collision controls; the page also documents the permission `deny`
(`skills.md:133-156, 230`). Contract v1 rule 2 forbids editing `teaches` in place, and a superseding
row with the same URL would add a W04 duplicate-URL warning, so the narrower cell stays and the
entry carries the fuller reading (seat `SrcOpencode.md`, decision recorded here).

### Rejected

- **S024 superseding row** (drafted by `SrcOpencode` as "supersedes S024 —"): not written; reason
  above.
- **Copilot CLI quote at `cli-command-reference.md:1278`** (the `disable-model-invocation` table
  row): its cells are separated by `|`, which cannot sit inside a markdown table cell; the prose
  sentence at `:1300` was used instead, and the per-directory bound is in the entry's Limits.
- **Gemini CLI quote at `skills.md:75`** ("`/skills disable` and `/skills enable` default to the
  `user` scope."): it states a scope default, not what the command does; `:94` states the effect.
- **VS Code `user-invocable`** as a lever: the page says it hides the skill from the `/` menu "while
  still allowing the agent to load it automatically" (`agent-skills.md:150`), the opposite effect.
- **Claude Code `when_to_use`** as a lever: the page says it is "Appended to `description` in the
  skill listing" (`skills.md:390`), so it is description wording (seat `ReviewOverlapRows.md`).
- **Secondary pages as rows** (seat `LeverOtherPages.md`): VS Code `manage-ai-settings.md:294`, Gemini
  CLI settings reference `:189`, Codex `config-reference.md:381-393`, Claude Code `permissions.md:138`:
  each either duplicates the skills page or offers only an all-or-nothing switch.
- **omp's shipped docs as a row** (`LeverOmp.md`): `omp://skills.md` is read through the harness, not
  a URL a recheck can fetch; the entry keeps omp in a separate, uncounted paragraph.

### Erratum: the round-50 reject reason for the Copilot SDK page (routed defect D4)

`corpus/lessons/round-50.md:44-45` rejected the Copilot SDK skills page as "provider catalogs, not
SKILL.md routing". That reason is wrong. The page documents file-based `SKILL.md` skills ("A skill
is a named directory containing a `SKILL.md` file", `skills.md:11`), the `description` field
(`:289`) and a § Skill conflicts section whose remedies are "Use `disabledSkills` to exclude
conflicting skills" and "Reorganize skill directories to avoid overlaps" (`:809-810`). The
accurate reason at the time would have been "no claim needed the row". The row is now written as
S030. This erratum is appended here; the round-50 lesson is a record and is not edited.

## Routed defects from the round-50 spot-check

- **D1 (record).** `.ufo/waves/round-50/build/DescDraft.md` (10,079 B, sha256 `0181a459…`, mtime
  2026-10-22 10:52:19 -03:00, 57 s after `2abd290`) is committed byte-exact this round as round-50
  wave evidence. It is not claim-bearing: it recommends keeping the landed description, and it
  misdates that landing as `956ee167` (the description landed at `542f515`; `956ee167` does not
  touch `SKILL.md`). Seat accounting correction for the round-50 record (seat `D1Disposition.md`):
  the report's "2 cancelled by the L1 after an hour without a report (`DescDraft`, `D2D4Wording`)" is
  wrong. Both seats wrote reports: `D2D4Wording.md` at 10:51:16 -03:00 (committed in `2abd290`, 6 s
  later) and `DescDraft.md` at 10:52:19. Corrected count: 71 of 71 round-50 seats wrote a report;
  0 cancelled; 0 died; 70 of 71 reports were committed in round 50 and the 71st now. The round-50
  report is a filed record and is not edited; this paragraph and LOG.md carry the correction. This
  round's leftover and misroot sweep runs after the last seat write (Q27); its command and output
  are in the round-51 report.
- **D2 (calibration).** The checklist-gate sentence is bounded in `SKILL.md` and in an appended
  qualifier at the end of the `SCORECARD.md` operability cell (see LOG.md, round 51). The fixes for
  findings F3–F5 (a false red on a relative `--map` run from another directory, a crash on non-UTF-8
  help output) and the four `MutBoxProofGate` survivors stay carried, not fixed.
- **D3 (corrections sweep).** Seat `D3Sweep.md` found exactly the two routed sites. `SKILL.md`
  (the round-50 error pattern) now carries the eight-page bound and no "documented remedy" clause;
  `corpus/README.md:72`'s index row is corrected; the round-50 entry gets an appended note that
  finding 4 is superseded.
- **D4 (gate record).** Erratum above; S030 written.
- **D5 (rows).** `PROVINCE.md` kama row: the quote is now the full sentence and the deletion
  citation is bounded to the passages that each carry one half; census entry: appended section
  "Round 51: corrections to the round-50 rulings" quotes what kengaku `corpus/README.md:192` lists
  (six outputs, not only "frontmatter triggers"). No row moved (seat `D5Rows.md`).
- **D6 (rule).** Census entry: appended section "Round 51 status of the precedence rule (routed
  D6)": the rule is provisional until the operator's L0 answer, it was written after the three rows
  were known, the generic-refusal exit is bounded (a row cleared only by a generic refusal is marked
  so; tameshi's is), and round 51 neither extends nor relies on the rule (no new ruling, no row
  moved, no claim counter reads it). `PROVINCE.md` § Adjacent carries a one-line pointer.
- **D7 (carried).** Re-confirmed open at base by seat `CarryD7.md`: the C2 driver launders through
  duplicate-id and unlabelled twins; its kill test is a stderr substring; three crash paths (unknown
  revision, malformed manifest, an existing work directory), not two; 7 of 17 instrument mutants and
  11 of 28 census-guard mutants survive; `box_proof_case_deletion.py` has no `--self-test`, so it
  cannot enter `verifiers/floors-registry.json` yet; the four `FloorsRegister` arms F30–F33 are
  unapplied (the patch still applies cleanly). Reason for carrying: this round's claims are freshness
  and depth; each item needs its own fixture work. The new counter `check_overlap_levers.py` is
  floored this round (instrument total 11 → 12), so the "counter not registered" class does not
  repeat.
