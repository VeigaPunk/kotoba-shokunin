Result: DONE — Drafted the requested 20-line knowledge-entry frame; no lane knowledge file was edited.

## Verbatim frame for L1

```markdown
---
source: S089 https://code.claude.com/docs/en/slash-commands.md; S090 https://learn.chatgpt.com/docs/custom-prompts.md; S091 https://code.visualstudio.com/docs/agent-customization/prompt-files.md; S092 https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md; S093 https://geminicli.com/docs/cli/custom-commands.md; S094 https://cursor.com/docs/reference/deeplinks.md; S095 https://opencode.ai/v2/docs/commands/; S028 https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference
verified-at: 2026-10-23
recheck: python3 -B verifiers/check_command_files.py --rev <rev> --fetch
---

# Custom command files by client (round 58)

A custom command/prompt file is a user-authored instruction file exposed by a client as a reusable slash command; a skill is a distinct instruction surface, though names, formats and migration paths vary by client. VS Code describes prompt files as “Prompt files simplify prompting for common tasks by encoding them as standalone Markdown files that you invoke as slash commands in chat.” It says “Prompt files run only in **Local** harness sessions in the Chat view. For reusable workflows in other harnesses, create an [agent skill]” (S091; `.ufo/waves/round-58/w0/CensusVSCode.md:5-7,70-74`). Claude Code says “**Custom commands have been merged into skills.**” while “Your existing `.claude/commands/` files keep working” (S089; `.ufo/waves/round-58/w0/CensusClaudeCode.md:59-62`). Codex says “Custom prompts are deprecated.” and directs users to skills for reusable instructions (S090; `.ufo/waves/round-58/w0/CensusCodex.md:58-64`). These are vendor-doc distinctions, not runtime measurements.

**Row rule (applied to every row the same way).** Count a client only when its own documentation on a pinned host names a user-authored reusable-prompt/custom-slash-command folder or file pattern and supplies a verbatim 6–25-word quote containing the case-sensitive token (or its normalized form) at a path boundary, with a command/prompt word outside that span. The token must meet the frozen grammar: after one optional leading `~/` or `./`, at least two path segments; a dot-led first segment; a final segment containing `command(s)` or `prompt(s)`; no forbidden skill/agent/rule/plugin/extension segment, foreign client marker or non-leading dot in a non-final segment; and no shared normalized token. The census admits Claude Code, Codex, VS Code, Gemini CLI, Cursor and opencode (6 of 7). Copilot CLI has no eligible path: `.claude/commands/` is Claude Code's foreign/shared path, and `com.github.copilot/commands/` fails the dot-led-first-segment and non-final-dot rules (S092, S028; `.ufo/waves/round-58/w0/CensusCopilotCLI.md:9-41,56-81`). Its SKILL.md row must carry no backticked path. (Census: `plans/round-58.md:55-68`.)

| Client | Command files | Source | Quote |
|---|---|---|---|

## Limits

- Vendor documentation only; no client was run.
- Q31: the counter reads the measured revision's `SKILL.md`, entry, `SOURCES.md` and round-58 lesson `## Gate`. It checks unique client rows; the first backticked `Command files` token, its grammar and foreign/shared-token tests; and whether `Action` has at least three words. For entry rows it checks `Client`, matching `Command files`, one new `S###` `Source`, and `Quote` length/content; for source rows it checks id/newness, `docs` kind, tier A, `mined` status, opened date, pinned host and excluded URL classes; it also requires the quote in `## Gate`. With `--fetch`, it checks the cited live page for quote and token, and scans base-revision text blobs outside `.ufo/` for held token occurrences when computing new ground (`verifiers/check_command_files.py:68-73,127-182`).
- It does not inspect the `What a file sets` cell's contents or decide whether row-rule prose correctly describes client behavior; the action cell is only word-counted. It does not test whether a client loads or runs these files. Those are reviewer judgments, not counter checks (Q31; `corpus/QUALITY.md:42`; `verifiers/check_command_files.py:782-784`).
```

## Evidence and limits

- The draft follows `corpus/knowledge/plugin-manifests-round57.md:1-5,17-30,79-99`; the C1 frozen row rule and population are in `plans/round-58.md:52-71` and `verifiers/check_command_files.py:75-88,127-182,208-218`.
- Quote evidence: Claude Code census `:59-62`; Codex census `:58-64`; VS Code census `:5-7,70-74`. Eligible/excluded census evidence is in each `.ufo/waves/round-58/w0/Census*.md` report; source URLs and Copilot's two excluded candidates are above.
- The requested table body is intentionally empty for the L1 to populate from Src seat outputs. This report is the only file written; no command, test, build, lint, client, or counter was run by this seat, and no tools were installed.
