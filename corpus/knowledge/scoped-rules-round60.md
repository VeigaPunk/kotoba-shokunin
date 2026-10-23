---
source: S103–S109; S103, S106 and S108 re-open round-53 rows S043, S048 and S049 for the scope keys those rows never recorded (URLs and full sha256 values are recorded in `corpus/SOURCES.md`)
verified-at: 2026-10-23
recheck: python3 -B verifiers/check_scoped_rules.py --rev <rev> --fetch
---

# Scoped rule files by client (round 60)

Scope: Vendor documentation read 2026-10-23; not a runtime test.

Choose a scoped rule when the documented goal is to load it only for matching files: Claude Code says a `paths` rule loads only when Claude works with matching files [S103 :168]; VS Code automatically attaches an `applyTo` instruction when its pattern matches files being changed [S105 :105]; Copilot CLI includes a path-specific instruction only when `applyTo` matches a file it is working with [S106 :32]; Cursor auto-attaches a `globs` rule when a matching file is in context [S108 :68]. Do not treat every rule in those folders as scoped: Claude Code says rules without `paths` load at launch, while Cursor documents always-apply, description-selected, and manual rule types alongside path-scoped rules [S103 :188; S108 :65-70]. The other surveyed systems describe directory placement rather than a matching-path key: Codex walks instruction files by directory [S104 :12], Gemini describes a user-home default plus workspace/ancestor and just-in-time directory discovery [S107 :20-35,38-40], and opencode describes project-directory rules and a global file [S109 :64,68]. Keep project-wide and user-level sources distinct from scoped rules: VS Code's `.github/copilot-instructions.md` is project-wide [S105 :64], Copilot CLI distinguishes its repository-wide file from matching-path instructions [S106 :17,32], and Claude also documents a user-level `~/.claude/rules/` path for rules [S103 :273,640].

| Client | Rule files | Source | Quote |
|---|---|---|---|
| Claude Code | `.claude/rules/` | S103 | For larger projects, you can organize instructions into multiple files using the `.claude/rules/` directory. |
| VS Code | `.github/instructions/**/*.instructions.md` | S105 | Targeted instructions can use `.github/instructions/**/*.instructions.md` or Markdown files in `.claude/rules`. |
| Copilot CLI | `.github/instructions/**/*.instructions.md` | S106 | `.github/instructions/**/*.instructions.md`              &#124; Modular repository instructions, discovered in the standard locations |
| Cursor | `.cursor/rules` | S108 | Project rules live in `.cursor/rules` as `.mdc` files and are version-controlled. |

## Per-client notes

- **Claude Code (S103).** Project rule files are in `.claude/rules/`; YAML frontmatter `paths` takes the matching file patterns [S103 :168,194,198-199]. A rule in that directory without `paths` loads at launch [S103 :188]. The docs also name `~/.claude/rules/` as a user-level rules directory and state that path-scoped rules can be in either `.claude/rules/` or `~/.claude/rules/` [S103 :273,640]. `.claude/CLAUDE.md` is a separate, launch-loaded file, not the matching-file rule [S103 :188].
- **VS Code (S105).** The targeted file pattern is `.github/instructions/**/*.instructions.md`; `applyTo` selects files, and the docs also describe loading an instruction on demand when its `description` matches the task [S105 :27,105,164]. The census does not state the default for a file lacking `applyTo`, so this entry does not infer one. The page distinguishes project-wide `.github/copilot-instructions.md` and `AGENTS.md` from the targeted files; its Local-harness note also lists `CLAUDE.md` [S105 :24,32,64]. The census report does not establish a VS Code user-home rule folder; this is a limit of the evidence recorded here, not a claim that such a folder cannot exist [CensusVSCode.md:133-139].
- **Copilot CLI (S106).** The path-scoped rule files are `.github/instructions/**/*.instructions.md`; `applyTo` makes them conditional on the file Copilot CLI is working with [S106 :18,32,66]. The census page does not settle what a modular file does when `applyTo` is absent. Its repository-wide `.github/copilot-instructions.md` is a separate scope [S106 :17]. A separate Copilot CLI configuration-directory fetch recorded personal `~/.copilot/instructions/` as applying to every session, not as the matching-path row (re-census report: `RecensusCopilotCLI.md:115`; the assigned S106 snapshot is the add-custom-instructions page).
- **Cursor (S108).** Project rules are in `.cursor/rules`; `globs` supplies a path pattern, and matching files are auto-attached when in context [S108 :32,68,85]. The same folder also documents always-apply, description-selected, and manual rule types [S108 :65-70]. The census does not establish the default for a file without `globs`, and its report does not identify a user-level rules folder; neither default nor absence is inferred here [CensusCursor.md:20,65-76].

## Directory-scoped negatives

- **Codex (S104).** The census documents `AGENTS.override.md`, `AGENTS.md`, and fallback names discovered along the directory walk, with at most one file included per directory; this is placement-based, not a file-path glob rule [S104 :12,46]. `~/.codex/rules/` is a separate experimental command execpolicy; its `pattern` matches command prefixes, not instruction-file paths [S104 :48-61,91]. The census also rejects `AGENTS.md` as a counted token because it is one segment and not dot-led [CensusCodex.md:95-100].
- **Gemini CLI (S107).** The default `GEMINI.md` context file is discovered by directory hierarchy and JIT access, not a matching-path frontmatter rule [S107 :20-35]. The user-level `~/.gemini/GEMINI.md` provides defaults for all projects [S107 :38-40]. The `fileName` setting names context filenames; the census found no path-pattern key and no action line for attaching such a pattern [S107 :66-79].
- **opencode (S109).** The project `AGENTS.md` applies in its directory and subdirectories; the global `~/.config/opencode/AGENTS.md` applies across sessions [S109 :64,68]. Its `instructions` array adds extra files to load alongside discovered `AGENTS.md`; the census says those globs choose instruction files, not paths of files the agent is working on [Censusopencode.md:73-86]. This is not the matching-file rule class.

## Quote shaping (per row; each written from the committed snapshot line)

- **S103:** contiguous prefix of `S103.page:168` through `directory.`; backticks kept; no bytes removed (`SrcClaudeCode`).
- **S105:** contiguous slice of `S105.page:32` (the second sentence of the line); backticks kept; no bytes removed (`SrcVSCode`).
- **S106:** contiguous slice of the table row `S106.page:18` from the token's opening backtick through `locations`; the source's run of spaces is kept and its one table pipe is written `&#124;` so the entry table keeps four columns (the counter unescapes it); no other bytes changed (`SrcCopilotCLI`).
- **S108:** contiguous prefix of `S108.page:32` through `version-controlled.`; backticks kept; no bytes removed (`SrcCursor`).

## Not held

- Runtime behavior: no client was run; attachment, parsing, timing, and matching behavior are vendor documentation claims, not observed runtime results.
- The default behavior of a candidate rule file without `paths`, `applyTo`, or `globs` is not asserted where the census page does not state it.
- Cross-client equivalence of glob syntax, matching rules, precedence, ordering, or conflict resolution is not established. Only behavior explicitly stated on each cited page is recorded.
- User-level rule folders are named only where the census evidence records them; no claim is made that a location omitted from a report does not exist.
- Undocumented loaders or behavior outside the fetched vendor-documentation pages and cited census searches are not held.
