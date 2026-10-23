Result: PARTIAL — The section draft and saved-byte vendor wording are ready; the assigned source/knowledge/snapshot artifacts were absent at read time, and the available Cursor recensus conflicts with the frozen eligibility.

## Exact section body

The snippet is 12 lines including its required blank line before the table. The additional separator blank before the existing `## Router model` is not included in the bounded section body; counting that separator inside the 12-line limit would make the requested layout 13 physical lines.

```markdown
### Scoped rule files by client
“For task or language-specific instructions, use multiple `*.instructions.md` files per topic and apply them selectively by using the `applyTo` property.” (S105 :329). Basis: `corpus/knowledge/scoped-rules-round60.md` (S103–S109). A scoped rule file is loaded only for matching files; durable every-session constraints belong in the always-on file (`## Always-on constraint-file checklist`), and a check that must run at an event is a hook (`### Hook files by client`), not a scoped rule (w0/ConnSiblingScoped.md:55).

| Client | Rule files | Scope key | Action |
|---|---|---|---|
| Claude Code | `.claude/rules/` (S103 :166) | `paths` (S103 :198) | Scope rules to specific files with YAML frontmatter (S103 :194) |
| Codex | — (directory-walked AGENTS.md; S104 :12) | — | — |
| VS Code | `.github/instructions/**/*.instructions.md` (S105 :27) | `applyTo` (S105 :164) | For task- or language-specific instructions, apply selectively (S105 :329) |
| Copilot CLI | `.github/instructions/**/*.instructions.md` (S106 :18) | `applyTo` (S106 :66) | Use glob syntax to specify files or directories (S106 :60) |
| Gemini CLI | — (directory/JIT GEMINI.md context; S107 :31–33) | — | — |
| Cursor | `.cursor/rules` (S108 :32) | `globs` (S108 :85) | Scope a rule to specific files or directories (S108 :131) |
| opencode | — (directory-discovered AGENTS.md; S109 :17) | — | — |
```

The file paths, keys, and action citations for the four planned eligible rows use the original base-page census lines for Claude Code (S103 re-opens S043), Copilot CLI (S106 re-opens S048), and Cursor (S108 re-opens S049), and the new VS Code page (S105). These are provisional source-ID references: at read time `corpus/SOURCES.md` ended at S102 (line 114), `corpus/knowledge/scoped-rules-round60.md` was not found, and `.ufo/waves/round-60/snapshots/` was empty. The three non-eligible rows show the directory-based alternative reported by their census, not a path-pattern rule. No source row, knowledge entry, snapshot, or SKILL.md was written by this seat.

## Vendor sentence and saved-byte count

Primary intro evidence is VS Code's vendor sentence on line 329 of the fetched Markdown page, saved at `/fast/scratch/hyaku/kotoba-r60/CensusVSCode/agent-custom-instructions.md`. The census report records its fetch as HTTP 200, 23,715 bytes, sha256 `a45c9e9f50c62949ea60711c6d657d065752c573a0c945215f32063fa56caa1f` (`.ufo/waves/round-60/w0/CensusVSCode.md:13–15`). The quote is reproduced verbatim in the draft. The read-only count command completed successfully (exit 0; tool returned without error):

```sh
timeout 15s sh -c 'date -u; sed -n "329p" /fast/scratch/hyaku/kotoba-r60/CensusVSCode/agent-custom-instructions.md; sed -n "329p" /fast/scratch/hyaku/kotoba-r60/CensusVSCode/agent-custom-instructions.md | wc -w; sed -n "131p" /fast/scratch/hyaku/kotoba-r60/CensusCursor/rules.md; sed -n "131p" /fast/scratch/hyaku/kotoba-r60/CensusCursor/rules.md | wc -w'
```

Observed output:

```text
Fri Oct 23 12:10:01 PM UTC 2026
* For task or language-specific instructions, use multiple `*.instructions.md` files per topic and apply them selectively by using the `applyTo` property.
21
Use `globs` to scope a rule to specific files or directories. Separate multiple patterns with commas.
16
```

The VS Code line is also printed from fetched bytes in `CensusVSCode.md:72–76`; the secondary Cursor line appears in `CensusCursor.md:69–74` and is cited in the frozen-plan draft, subject to the conflict below. The Cursor `wc -w` output is 16; its sentence is not the primary intro quote.

## Conflict and limits

- Frozen assignment census: eligible Claude Code (re-opens S043), VS Code, Copilot CLI (re-opens S048), Cursor (re-opens S049), F_max 4 / TARGET 3. The frozen counter's erratum E1 explicitly permits a base-key URL when the new source row re-opens the base row (`verifiers/check_scoped_rules.py:28–37`, `65–85`, `155–183`).
- The conflicting census result is verbatim: `Result: DONE — Cursor: NOT ELIGIBLE (no non-base page on a pinned host has `.cursor/rules` and `globs` in A1 key form; the only `globs:` site's final URL is the base rules page)` (`.ufo/waves/round-60/w0b/RecensusCursor.md:1`). The original base census is also verbatim: `Result: DONE — Cursor: ELIGIBLE `.cursor/rules` key `globs` line 85` (`.ufo/waves/round-60/w0/CensusCursor.md:1`). This report preserves both; draft cites S108 as the frozen re-open, not as a resolution of the conflict.
- The German-locale Claude recensus URL (`w0b/RecensusClaudeCode.md:9`) and enterprise-cloud Copilot recensus URL (`w0b/RecensusCopilotCLI.md:9`) are not used for the draft; the original English base pages support the frozen re-open references (`w0/CensusClaudeCode.md:7–12,166,194,198`; `w0/CensusCopilotCLI.md:7–12,18,60,66`). The fleet instruction rejects locale/versioned aliases.
- Insertion point is after `### Hook files by client` and before `## Router model` (`SKILL.md:121–135`). No SKILL.md edit, counter run, build, test, or tool installation was performed. Only this report is the seat's output.

## Artifact

`.ufo/waves/round-60/build/ScribeSkillSection.md`
