Result: DONE — Drafted a 12-line SKILL.md section and mapped its factual clauses to the W0 census reports.

## Section text (verbatim; 12 lines)
```markdown
### Custom command files by client
When you meet a custom command or prompt, open a file in the client-specific location below.
Basis: `corpus/knowledge/command-files-round58.md`; source rows and quotations are in `corpus/lessons/round-58.md` § Gate.
| Client | Command files | What a file sets | Action |
|---|---|---|---|
| Claude Code | `.claude/commands/` | Markdown file creates a custom slash command | Prefer a skill for new work |
| Codex | `~/.codex/prompts/` | Top-level Markdown files are reusable slash-command prompts | Use skills for new reusable prompts; custom prompts are deprecated |
| VS Code | `.github/prompts` | Reusable Markdown prompt invoked as a slash command | Local harness sessions only |
| Copilot CLI | No distinct eligible path (shared with Claude Code) | Individual Markdown command file; command name comes from filename | Use Claude Code's row for the shared location |
| Gemini CLI | `~/.gemini/commands/` | TOML command file; `prompt` is required | Store user command files here |
| Cursor | `.cursor/commands` | Markdown file defines a focused workflow or action | Invoke with `/` in Agent chat |
| opencode | `.opencode/commands/` (project); `~/.config/opencode/commands/` (global) | Markdown `.md` files turn prompts into slash commands | Use `commands/` for new files, not legacy singular `command/` |
```

## Facts and census-report pointers
- Lead: the listed client-specific locations tell a reader which file location to inspect (editorial instruction). Its Basis references follow the existing SKILL.md house style; the referenced knowledge and lesson files were not present at the time of this read (see limits).
- Claude Code: `.claude/commands/` contains Markdown command files; a file and a same-named skill can both create a slash command — `CensusClaudeCode.md:20-22,41`. Commands are an older format; the page prefers skills for new work — `CensusClaudeCode.md:57-62`.
- Codex: `~/.codex/prompts/` contains top-level Markdown files that are scanned as reusable slash-command prompts — `CensusCodex.md:21-25,42`. Custom prompts are deprecated and the docs direct users to skills for reusable prompts — `CensusCodex.md:56-64`.
- VS Code: `.github/prompts` is the workspace prompt-file location; a prompt file is reusable Markdown invoked as a slash command — `CensusVSCode.md:20-22,44`. Prompt files run only in Local harness sessions — `CensusVSCode.md:70-74`.
- Copilot CLI: its docs call individual `.md` files in the Claude Code command location an alternative to skills; the command name comes from the filename. That normalized location is Claude Code's eligible row, so Copilot CLI has no distinct eligible path — `CensusCopilotCLI.md:7,17-28,40-43`. This table row contains no backticked path.
- Gemini CLI: `~/.gemini/commands/` is the global user-command location; command files are TOML and require `prompt` — `CensusGeminiCLI.md:21-27,45-46`.
- Cursor: `.cursor/commands` is where custom commands are defined; commands are Markdown files defining a focused workflow or action and invoked with `/` in Agent chat — `CensusCursor.md:15,19-21,42`.
- opencode: `.opencode/commands/` is the project location and `~/.config/opencode/commands/` the global location; only `.md` files are discovered and a file turns a prompt into a slash command — `Censusopencode.md:22-26,43`. The page directs users to plural `commands/` for new files and labels singular `command/` legacy — `Censusopencode.md:61-66`.

## Provenance, gates, and touched surfaces
- This seat used the seven read-only W0 reports as its source; no network fetch, lane command, counter, build, test, or verifier was run here. No tools were installed or updated.
- W0 fetch provenance recorded by the seats (not independently re-run): Claude Code used `curl -sSL -o <body> -w "%{http_code} %{url_effective}"`, exit 0 / HTTP 200 / 114542 bytes / sha256 `6b070e872dea28905a7ea7f45c4d5960f5bdf28cc73ac808799af6d50435ffbd` (`CensusClaudeCode.md:7-13`); Codex used `curl -sSL -D headers -o custom-prompts.md`, exit 0 / HTTP 200 / 3357 bytes / sha256 `d6f7cf8dd9f31d2faf5604ef3a6f8322132a7b66fa50823109cb681e372a0fa9` (`CensusCodex.md:7-13`); VS Code used `curl -sSL -D prompt-files.md.hdr -o prompt-files.md`, exit 0 / HTTP 200 / 13729 bytes / sha256 `4ad1b2bcaf78c9166b1609610f354d9cb8b1ff9c9e7cf643c443fad04dac6685` (`CensusVSCode.md:7-14`).
- Further W0 fetch provenance: Gemini CLI used `date -u` then `curl -sSL` for the `.md` page, exit 0 / HTTP 200 / 12129 bytes / sha256 `8f3295e8ca502b0c70bb3bf672f0dc0130ecb868fad4a88d5cac0f36ac6f3872` (`CensusGeminiCLI.md:7-19`); Cursor used `curl -sSL -D <headers> -o <body> -w "%{http_code} %{size_download} %{url_effective}"`, exit 0 / HTTP 200 / 5972 bytes / sha256 `7ceb657892bdfa5d7a32f1168411fcaeb63c2f6ab41a5f0c45116a0a3f3a6bf4` (`CensusCursor.md:7-13`); opencode used `curl -sSL -H 'Accept: text/markdown'`, exit 0 / HTTP 200 / 7220 bytes / sha256 `c3dc75fc48071613c359126e7d84e2298afd10c4b83aac83383e94a1489a23dc` (`Censusopencode.md:7-13`).
- Copilot CLI used `curl -sSL -o <body> -w "%{http_code} %{size_download}"`, exit 0 / HTTP 200 / 461944 bytes / sha256 `c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9` (`CensusCopilotCLI.md:11-17`).
- Lane surfaces read: `SKILL.md:97-124` and `.ufo/waves/round-58/w0/Census{ClaudeCode,Codex,VSCode,GeminiCLI,Cursor,opencode,CopilotCLI}.md`; no product files were edited. The only written file is `.ufo/waves/round-58/build/ScribeSkillSection.md`.
- Read attempts for `corpus/knowledge/command-files-round58.md` and `corpus/lessons/round-58.md` returned “not found”; the Basis line is the frozen intended reference, not a claim that those files were present. Source seats may correct cells, as assigned; this is a draft, not an integrated SKILL.md change.
- Out of scope: source fetching, counter execution, section integration, and checks. No gate result is claimed.

Artifact: `.ufo/waves/round-58/build/ScribeSkillSection.md`
