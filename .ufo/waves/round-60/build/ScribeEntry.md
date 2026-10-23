Result: DONE — drafted the complete scoped-rules knowledge entry with the four requested quote placeholders and evidence-bounded client notes.

## Behavior

The full file text below follows the round-59 house shape: source/date/recheck metadata, title and scope line, a four-sentence sourced scoped-versus-always-on decision, the required entry-table header, per-client notes, per-row quote-shaping notes, directory-scoped negatives, and a Not held list. The four eligible rows are Claude Code (S103), VS Code (S105), Copilot CLI (S106), and Cursor (S108). Their Quote cells are explicitly placeholders for the assigned source seats; no vendor quote is invented here.

Citations in the draft use the source-page line numbers recorded in the census reports. The evidence read for this draft is `corpus/knowledge/hook-files-round59.md:1-81`, `plans/round-60.md:21-37,47-65,99-153`, `verifiers/check_scoped_rules.py:1-226,289-342`, and the W0/W0b census reports named in the draft and below. The planned S103-S109 URL/SHA records belong to `corpus/SOURCES.md`; this seat did not fetch or re-hash vendor pages.

## Draft file text

```markdown
---
source: S103–S109 (URLs and full sha256 values are recorded in `corpus/SOURCES.md`)
verified-at: 2026-10-23
recheck: python3 -B verifiers/check_scoped_rules.py --rev <rev> --fetch
---

# Scoped rule files by client (round 60)

Scope: Vendor documentation read 2026-10-23; not a runtime test.

Choose a scoped rule when the documented goal is to load it only for matching files: Claude Code says a `paths` rule loads only when Claude works with matching files [S103 :168]; VS Code automatically attaches an `applyTo` instruction when its pattern matches files being changed [S105 :105]; Copilot CLI includes a path-specific instruction only when `applyTo` matches a file it is working with [S106 :32]; Cursor auto-attaches a `globs` rule when a matching file is in context [S108 :68]. Do not treat every rule in those folders as scoped: Claude Code says rules without `paths` load at launch, while Cursor documents always-apply, description-selected, and manual rule types alongside path-scoped rules [S103 :188; S108 :65-70]. The other surveyed systems describe directory placement rather than a matching-path key: Codex walks instruction files by directory [S104 :12], Gemini describes a user-home default plus workspace/ancestor and just-in-time directory discovery [S107 :20-35,38-40], and opencode describes project-directory rules and a global file [S109 :64,68]. Keep project-wide and user-level sources distinct from scoped rules: VS Code's `.github/copilot-instructions.md` is project-wide [S105 :64], Copilot CLI distinguishes its repository-wide file from matching-path instructions [S106 :17,32], and Claude also documents a user-level `~/.claude/rules/` path for rules [S103 :273,640].

| Client | Rule files | Source | Quote |
|---|---|---|---|
| Claude Code | `.claude/rules/` | S103 | [SrcClaudeCode: paste the exact quote from the saved S103 snapshot] |
| VS Code | `.github/instructions/**/*.instructions.md` | S105 | [SrcVSCode: paste the exact quote from the saved S105 snapshot] |
| Copilot CLI | `.github/instructions/**/*.instructions.md` | S106 | [SrcCopilotCLI: paste the exact quote from the saved S106 snapshot] |
| Cursor | `.cursor/rules` | S108 | [SrcCursor: paste the exact quote from the saved S108 snapshot] |

## Per-client notes

- **Claude Code (S103).** Project rule files are in `.claude/rules/`; YAML frontmatter `paths` takes the matching file patterns [S103 :168,194,198-199]. A rule in that directory without `paths` loads at launch [S103 :188]. The docs also name `~/.claude/rules/` as a user-level rules directory and state that path-scoped rules can be in either `.claude/rules/` or `~/.claude/rules/` [S103 :273,640]. `.claude/CLAUDE.md` is a separate, launch-loaded file, not the matching-file rule [S103 :188].
- **VS Code (S105).** The targeted file pattern is `.github/instructions/**/*.instructions.md`; `applyTo` selects files, and the docs also describe loading an instruction on demand when its `description` matches the task [S105 :27,105,164]. The census does not state the default for a file lacking `applyTo`, so this entry does not infer one. The page distinguishes project-wide `.github/copilot-instructions.md` and `AGENTS.md` from the targeted files; its Local-harness note also lists `CLAUDE.md` [S105 :24,32,64]. The census report does not establish a VS Code user-home rule folder; this is a limit of the evidence recorded here, not a claim that such a folder cannot exist [CensusVSCode.md:133-139].
- **Copilot CLI (S106).** The path-scoped rule files are `.github/instructions/**/*.instructions.md`; `applyTo` makes them conditional on the file Copilot CLI is working with [S106 :18,32,66]. The census page does not settle what a modular file does when `applyTo` is absent. Its repository-wide `.github/copilot-instructions.md` is a separate scope [S106 :17]. A separate Copilot CLI configuration-directory fetch recorded personal `~/.copilot/instructions/` as applying to every session, not as the matching-path row (re-census report: `RecensusCopilotCLI.md:115`; the assigned S106 snapshot is the add-custom-instructions page).
- **Cursor (S108).** Project rules are in `.cursor/rules`; `globs` supplies a path pattern, and matching files are auto-attached when in context [S108 :32,68,85]. The same folder also documents always-apply, description-selected, and manual rule types [S108 :65-70]. The census does not establish the default for a file without `globs`, and its report does not identify a user-level rules folder; neither default nor absence is inferred here [CensusCursor.md:20,65-76].

## Directory-scoped negatives

- **Codex (S104).** The census documents `AGENTS.override.md`, `AGENTS.md`, and fallback names discovered along the directory walk, with at most one file included per directory; this is placement-based, not a file-path glob rule [S104 :12,46]. `~/.codex/rules/` is a separate experimental command execpolicy; its `pattern` matches command prefixes, not instruction-file paths [S104 :48-61,91]. The census also rejects `AGENTS.md` as a counted token because it is one segment and not dot-led [CensusCodex.md:95-100].
- **Gemini CLI (S107).** The default `GEMINI.md` context file is discovered by directory hierarchy and JIT access, not a matching-path frontmatter rule [S107 :20-35]. The user-level `~/.gemini/GEMINI.md` provides defaults for all projects [S107 :38-40]. The `fileName` setting names context filenames; the census found no path-pattern key and no action line for attaching such a pattern [S107 :66-79].
- **opencode (S109).** The project `AGENTS.md` applies in its directory and subdirectories; the global `~/.config/opencode/AGENTS.md` applies across sessions [S109 :64,68]. Its `instructions` array adds extra files to load alongside discovered `AGENTS.md`; the census says those globs choose instruction files, not paths of files the agent is working on [Censusopencode.md:73-86]. This is not the matching-file rule class.

## Quote shaping (per row)

- **S103:** The census candidate is a contiguous prefix of fetched `memory.md:168`, ending at `directory.`; it retains its printed backticks and removes no bytes [CensusClaudeCode.md:33-39]. The table placeholder remains until SrcClaudeCode supplies the quote from the committed S103 snapshot.
- **S105:** The census quote is a contiguous slice of fetched `agent-custom-instructions.md:32`; the report says no Markdown bytes were stripped [CensusVSCode.md:29-43]. Keep the exact fetched-byte slice; the placeholder awaits SrcVSCode's saved snapshot.
- **S106:** The census quote candidate is a contiguous slice of fetched `add-custom-instructions.md:18`, from the opening backtick through `locations`; it retains the source table's literal pipe and surrounding spaces, with no bytes stripped [CensusCopilotCLI.md:31-52]. The row remains a placeholder so SrcCopilotCLI can provide its final exact quote and document any table-safe representation it uses.
- **S108:** The census quote is a contiguous prefix of fetched `rules.md:32` through `version-controlled.`; backticks are retained and no bytes are stripped [CensusCursor.md:39-47]. The placeholder awaits SrcCursor's quote from the saved S108 snapshot.

## Not held

- Runtime behavior: no client was run; attachment, parsing, timing, and matching behavior are vendor documentation claims, not observed runtime results.
- The default behavior of a candidate rule file without `paths`, `applyTo`, or `globs` is not asserted where the census page does not state it.
- Cross-client equivalence of glob syntax, matching rules, precedence, ordering, or conflict resolution is not established. Only behavior explicitly stated on each cited page is recorded.
- User-level rule folders are named only where the census evidence records them; no claim is made that a location omitted from a report does not exist.
- Undocumented loaders or behavior outside the fetched vendor-documentation pages and cited census searches are not held.
```

## Gates

- Counter specification was read before drafting: `verifiers/check_scoped_rules.py:1-226` states the frozen C1 contract and A1 semantic conjuncts; `TARGET = 3` is at `:249`. This seat did not run the counter.
- No source fetch, `wc -w`, snapshot hash check, test, build, lint, or runtime probe was run by this seat. The quoted shaping details are taken from the existing census reports, not independently re-fetched bytes. No tool was installed or updated.
- The placeholder quote cells are intentional per assignment and are not a counter receipt or evidence of a completed source quote. The draft must be integrated only after the source seats provide their exact rows/snapshots/quotes.

## Touched surfaces

Only `.ufo/waves/round-60/build/ScribeEntry.md` was written. No product, corpus, verifier, source registry, lesson, snapshot, or `SKILL.md` file was changed.

## Known census/freeze tension

The W0b reports contain headlines that conflict with the frozen E1 source-seat assignment. Verbatim:

- `RecensusClaudeCode.md:1` headline, verbatim: Result: DONE — Claude Code: ELIGIBLE https://code.claude.com/docs/de/memory.md token `.claude/rules/` key `paths` line 198. The freeze says the locale copy is rejected and the source seat must re-open base S043 at the English URL (`plans/round-60.md:136,146`; build-spec `SrcClaudeCode` prompt).
- `RecensusCopilotCLI.md:1` headline, verbatim: Result: DONE — Copilot CLI: ELIGIBLE https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md token `.github/instructions/**/*.instructions.md` key `applyTo` line 66. The freeze rejects versioned aliases and directs S106 to re-open base S048 (`plans/round-60.md:137,146`; build-spec `SrcCopilotCLI` prompt).
- `RecensusCursor.md:1`: `Result: DONE — Cursor: NOT ELIGIBLE (no non-base page on a pinned host has `.cursor/rules` and `globs` in A1 key form; the only `globs:` site's final URL is the base rules page)`. The freeze's E1 re-open rule makes Cursor eligible as re-opened S049 (`plans/round-60.md:138,146`; build-spec `SrcCursor` prompt).

The draft follows the frozen v2/E1 assignment for its four rows and does not use the locale/versioned aliases. The report headlines are preserved here rather than silently rewritten.

## Artifact path

`.ufo/waves/round-60/build/ScribeEntry.md`
