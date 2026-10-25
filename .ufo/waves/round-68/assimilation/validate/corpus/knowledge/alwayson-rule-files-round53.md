source: S043 (https://code.claude.com/docs/en/memory.md, `memory.md:354-358, 368-378, 440-461`), S044 (https://learn.chatgpt.com/docs/agent-configuration/agents-md.md, `agents-md.md:9-15, 145-159`), S045 (https://opencode.ai/docs/rules, `rules.mdx:77-103, 135-137, 182`), S046 (google-gemini/gemini-cli `docs/cli/gemini-md.md` at `451a02ff`, `:71-106`), S047 (https://code.visualstudio.com/docs/copilot/customization/custom-instructions, source `custom-instructions.md:45, 229-257, 315-319` at `fd64d648`), S048 (https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md, `:11-32, 48-50`), S049 (https://cursor.com/docs/rules.md, `rules.md:127, 317-357`), S052 (https://cursor.com/help/customization/rules.md, `rules.md:95-99`), S050 (https://zed.dev/docs/ai/instructions.md, `instructions.md:23-37`), S004 (https://agents.md/, `FAQSection.tsx:18-21`, `:31-48`), S019 (Anthropic Agent Skills best practices, `best-practices.md:574-582`, § Avoid time-sensitive information)
verified-at: 2026-10-22
recheck: python3 -B verifiers/verify_alwayson.py --self-test && python3 -B verifiers/check_alwayson_boxes.py --rev master

# Always-on rule files: which name each client reads, and what counts as a redirect (round 53)

Frontier area: executed checklist coverage, always-on half (`corpus/README.md` § Frontier, first row).
The `SKILL.md` § Always-on constraint-file checklist box "One canonical rule-file name per repo
(AGENTS.md **or** CLAUDE.md, or an explicit redirect)" was lane-attested prose from round 7 to round 52:
the lane recorded no client's rule for which name it reads (`.ufo/waves/round-53/build/ScoutLaneCorpusAlwaysOn.md`,
Q30 third leg: no per-client statement for Claude Code, Codex or Gemini CLI in the corpus). This entry
records what nine authorities document, so the box and its instrument (`verifiers/verify_alwayson.py`) rest
on sources rather than on the box's own wording.

Every page was opened on 2026-10-22 by a round-53 seat (fetch time, status, bytes, sha256 and the full
quote set in each seat report under `.ufo/waves/round-53/build/`, summarised in
`corpus/lessons/round-53.md` § Gate). These are documentation statements, not measured client
behaviour; two facts were measured (§ Limits), the first the installed Claude Code's Project instructions setting
(`ScoutClaudeBehaviour.md`: 2.1.304, default `claude-md-or-agents-md`, read without a model call).

## Per-client record

| client | row | names read (always-on, project level) | both AGENTS.md and CLAUDE.md in one directory | redirect forms the client documents |
|---|---|---|---|---|
| Claude Code | S043 | `CLAUDE.md`, `.claude/CLAUDE.md`, `CLAUDE.local.md`; `AGENTS.md` and `.claude/AGENTS.md` only when none of those exists (`memory.md:356, 368-375`) | reads "Your `CLAUDE.md` files only" (`:357`) | a `CLAUDE.md` with an `@AGENTS.md` import (`:442-445`) or a `CLAUDE.md` symlink to `AGENTS.md` (`:452-455`); a prose mention is not one (`:436`); imports inside code are ignored (`:112`) |
| OpenAI Codex | S044 | `AGENTS.override.md`, then `AGENTS.md`, then `project_doc_fallback_filenames` (`agents-md.md:12, 145-159`); the list's default `[]` is on the config sample page (`config-sample.md:286`, opened by ScribeCodex and re-opened by W2ReopenS044, no SOURCES row) | reads `AGENTS.md`; `CLAUDE.md` is not on the default list, and "Filenames not on this list are ignored for instruction discovery" (`:159`); "Codex includes at most one file per directory" (`:12`) | the fallback-name list in config; no `@` import (0 hits over 191 pages, `ScribeCodex.md` § 4) |
| opencode 1.19.x | S045 | `AGENTS.md`, with `CLAUDE.md` as a Claude Code compatibility fallback (`rules.mdx:77-91`); the loader also keeps a deprecated third name, `CONTEXT.md` (`instruction.ts:64-68` at v1.19.4, not on the page) | reads `AGENTS.md` only; precedence is per name, first name with any hit wins (`rules.mdx:95-103`; loader `instruction.ts:122-130` at v1.19.4) | the `instructions` config array (additive, `:107-131`); symlinks are named only as a way to share rules (`:182`), and the symlink redirect effect is this round's measurement (§ Limits); `@` references in a rule file are not parsed (`:135-137`). The vendor's V2 docs tree says V2 reads `AGENTS.md` only (`ScribeOpencode.md`); the installed 1.19.4 is V1 |
| Gemini CLI | S046 | `GEMINI.md` by default; `context.fileName` takes a name or a list, e.g. `["AGENTS.md", "CONTEXT.md", "GEMINI.md"]` (`gemini-md.md:94-106`) | a `context.fileName` value adds names, and the pinned loader keeps `GEMINI.md` in the list (`memoryTool.ts:22-49`, W2ReopenS046; the S046 row's "replaces" wording is wrong); every listed name present loads (`memoryDiscovery.ts:470, 485-500`) | `context.fileName`; `@file.md` imports (`gemini-md.md:71-92`); a symlink redirect is not documented |
| VS Code (Copilot Chat, Local harness) | S047 | `.github/copilot-instructions.md`, root `AGENTS.md`, `CLAUDE.md` in four locations, each behind a setting (`custom-instructions.md:45, 79, 229-257`); the page states the default only for `chat.useAgentsMdFile` (on, `:232`) and nested `AGENTS.md` (needs both settings, `:239`) | reads both [INFERENCE from the general sentence, no line names the pair]: "Applicable instruction sources are additive. Do not depend on a file order or precedence rule" (`:315`) | Markdown links behind a setting; no `@` import, no symlink rule documented |
| GitHub Copilot CLI | S048 | `AGENTS.md`, `CLAUDE.md` (also `.claude/CLAUDE.md`), `GEMINI.md`, `.github/copilot-instructions.md` and others (`:11-22`) | "Copilot CLI combines their instructions" with no precedence order (`:30`) | `@` plus a relative path in `AGENTS.md`, `CLAUDE.md` or `copilot-instructions.md` (`:48`); not in `GEMINI.md` (`:50`) |
| Cursor | S049 | `AGENTS.md` at the root and in subdirectories (`rules.md:317-357`); `CLAUDE.md` "the same way", always applied (S052, `help/customization/rules.md:97-99`) | reads both; no page orders them | none: an `@file` mention is a lazy tool read whose contents "are not inlined" (`rules.md:127`) |
| Zed | S050 | the first match of a nine-name list: `.rules`, `.cursorrules`, `.windsurfrules`, `.clinerules`, `.github/copilot-instructions.md`, `AGENT.md`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` (`instructions.md:25-35`) | reads `AGENTS.md`; `CLAUDE.md` is not loaded, with no warning found ([INFERENCE] from the absence of one) | none documented; `@AGENTS.md` is literal text ([INFERENCE] from code reading at `cfb894a5`, not executed, `ScribeZed.md`) |
| agents.md convention | S004 | `AGENTS.md`; "The closest AGENTS.md to the edited file wins" (`FAQSection.tsx:20`) | not addressed | a symlink from an old name to `AGENTS.md` (`:31-48`), Aider `read:`, Gemini CLI `context.fileName` |
| omp 18.12.6 (kotoba's own host; no SOURCES row — read from the installed binary's strings, sha256 `85d9daf3…`, and the shipped `omp://context-files.md`) | — | ten providers by priority: `.omp/AGENTS.md` 100, `.claude/CLAUDE.md` 80, `.agent(s)/AGENTS.md` 70, `GEMINI.md` 60, standalone `AGENTS.md` 10, standalone `CLAUDE.md` 10, and others (`ScoutOmpAlwaysOn.md`) | standalone `AGENTS.md` and `CLAUDE.md` tie at priority 10 and `AGENTS.md` takes the slot by registration order ([INFERENCE] from the bundle order; no session was run) | `@path` imports are expanded in every context file (depth 5, code spans untouched) and symlinks are followed (code reading) |

## What follows for the craft

1. **Two independent rule files are not one rule set.** With an `AGENTS.md` and an unrelated `CLAUDE.md`
   in one directory, Claude Code reads only `CLAUDE.md` (S043), Codex, opencode and Zed read only
   `AGENTS.md` (S044, S045, S050), and VS Code, Copilot CLI and Cursor read both (S047–S049). The same
   repository gives three clients three different instruction sets. This is the documented basis of the
   box's FAIL branch; the box text alone did not carry it.
2. **The two redirect forms the instrument accepts are portable in effect.** A `CLAUDE.md` symlink to
   `AGENTS.md` gives every client that reads either name the same bytes (S043 `:455`; opencode measured, § Limits; S004 documents the
   same mechanism for an old `AGENT.md` name, not for `CLAUDE.md`). A `CLAUDE.md` whose redirect line is `@AGENTS.md` is expanded by Claude Code
   (S043) and, by [INFERENCE] from its generic `@` relative-path form (`:48`), Copilot CLI (S048); the clients that do not expand it read `AGENTS.md` first or as well
   (Codex, opencode, Zed: `AGENTS.md` wins; VS Code, Cursor: both load, and the `CLAUDE.md` then contributes
   only its own lines plus the inert `@AGENTS.md` text — [INFERENCE] from the per-client rows, not a documented
   statement of any client). So the import form is a Claude Code redirect whose failure mode elsewhere reads,
   by that inference, as harmless, not a universal import (S045 `:135-137`, S049 `:127`).
3. **A prose mention is not a redirect.** S043 `:436`: "Claude sees `AGENTS.md` only if it decides to open the
   file"; a `CLAUDE.md` that only mentions `AGENTS.md` in prose leaves Claude Code reading a file without the rules.
4. **`GEMINI.md` and `.github/copilot-instructions.md` are further names** a repository may need to cover
   (S046, S047, S048, S050). The round-53 instrument checks only the `AGENTS.md`/`CLAUDE.md` pair; a
   repository with a third independent name is outside its check.
5. **Dated text (box `alwayson.04`) has no vendor rule for always-on files.** The one authority that states
   the rule states it for skills: Anthropic's Agent Skills best practices, § "Avoid time-sensitive
   information" (S019, `best-practices.md:574-582`, re-opened this round, `ScribeDatedAuthority.md` § 2.1),
   whose bad example is "If you're doing this before August 2025, use the old API." No authority opened
   this round was found to say it for `AGENTS.md`/`CLAUDE.md` (the Gemini CLI and Cursor dating sweeps are
   partial, W2ReviewEntry M2, so those two are `not checked` on this point); the nearest is advice to remove outdated instructions
   (S043 `:90`; Gemini CLI `memory-management.md:117-118`). The box is a lane extension of the skills rule,
   grounded in the round-7 evidence (`alwayson-checklist-round7.md`), and the instrument's docstring must say
   so (Q23). Its detector flags dates and a fixed list of date-free cue words (`currently`, `temporarily`, `for now`,
   `at present`, `right now`, `until further notice`); other undated transient text is not detected, a cue word can
   fire on a durable rule, and the skills page's own example ("before August 2025": a month and year, no day)
   passes it (held-out run, `.ufo/waves/round-53/falsify/W2CriticHeldOut.md`).
6. **Size limits differ by client and are not the box's rule.** Claude Code: a 200-line target and a
   4 MiB skip (S043 `:88, :619`); Codex: 32 KiB combined by default (S044 `:15`); Cursor: "Keep rules under
   500 lines" (S049 `:155`); opencode, VS Code, Copilot CLI: no rule-file size limit documented (full Q30
   sweeps); Gemini CLI and Zed: not checked (partial size sweeps, W2ReviewEntry M1, L3). Recorded for box `alwayson.08`, which stays unexecuted.

## Limits

- Documentation only, except two measurements. Claude Code's setting value (above). opencode 1.19.4's read
  channel, measured without a model (`opencode debug agent build --tool read`, also under `unshare -rn`):
  `AGENTS.md` only → `AGENTS.md`; `CLAUDE.md` only → `CLAUDE.md`; both → `AGENTS.md` only; a `CLAUDE.md`
  symlink to `AGENTS.md` → `AGENTS.md` once; a literal `@AGENTS.md` line is inert text
  (`.ufo/waves/round-53/build/ScoutOpencodeBehaviour.md`). opencode's system-prompt set and every other
  client were not run (model calls were out of bounds).
- The table's "names read" column is project level; user-level files (`~/.claude/CLAUDE.md`,
  `~/.codex/AGENTS.md`, Zed's `~/.config/zed/AGENTS.md`) are in the seat reports, not here.
- Claude Code reads `AGENTS.md` directly only from v2.1.277 (S043 `:364`); older or restricted sessions
  read `CLAUDE.md` only, so there the redirect is required, not optional.
- Copilot cloud agent differs from Copilot CLI: "the nearest `AGENTS.md` file in the directory tree will
  take precedence" (`ScribeCopilotCli.md` § 2.2); not separately rowed.
- What the instrument checks is stated in its docstring; what it does not check (other names, nested
  directories, transient text outside its cue-word list) is reviewer judgment there (Q31).
