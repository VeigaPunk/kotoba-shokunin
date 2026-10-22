# Round 55 — lessons (kotoba, hyaku campaign, attempt 1)

Base `f0e5de820a60ec44ff7e5b7c88ac8c8d463dde0c`; plan and frozen counters `a10240c0940f770a5f2a5f32a7e3c363dd5d40c0`;
erratum 1 (C1 counter v2, before any C1 content) `b04a9005c494d14e4667b201b723857005effb0d`. Claims: C1 depth (explicit
invocation by client; the learning and sourced claim), C2 operability (could-not-evaluate paths of 13 gates). Seat
reports: `.ufo/waves/round-55/build/` and `.ufo/waves/round-55/falsify/`.

## Gate

### Admitted (rows opened this round; fetch records in the seat reports named)

| row | URL | opened (UTC) | bytes, sha256 | quote (≤25 words) | location | seat |
|---|---|---|---|---|---|---|
| S065 | https://code.claude.com/docs/en/skills.md | 2026-10-22T23:12:23Z | 112,748 B, sha256 `909dd50a…` | "You can type `/skill-name` to invoke it directly, and Claude can load it automatically when relevant to your conversation." | `skills.md:547` | SrcClaudeCode |
| S066 | https://developers.openai.com/blog/eval-skills.md | 2026-10-22T23:13:16Z | 19,356 B, sha256 `6cf414bb…` | "Use the $setup-demo-app skill to create the project in this directory." | `eval-skills.md:148` (inside a `codex exec` prompt string) | SrcCodex |
| S067 | https://code.visualstudio.com/docs/agent-customization/agent-skills.md | 2026-10-22T23:13:16Z | 23,082 B, sha256 `26973567…` | "You can add extra context after the slash command. For example, `/webapp-testing for the login page` or `/github-actions-debugging PR #42`." | `agent-skills.md:287` | SrcVSCode |
| S068 | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills.md | 2026-10-22T23:12:41Z | 10,057 B, sha256 `989af498…` | "Use the /frontend-design skill to create a responsive navigation bar in React." | `add-skills.md:128` (body of a fenced example; direction at `:125`) | SrcCopilotCLI, ScoutCopilotMoved |
| S069 | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/tutorials/skills-getting-started.md | 2026-10-22T23:15:25Z | 5,855 B, sha256 `111e8bfa…` | "description and calls the `activate_skill` tool." | `skills-getting-started.md:127-129` | SrcGeminiCLI |
| S070 | https://cursor.com/docs/skills.md | 2026-10-22T23:12:21Z | 18,477 B, sha256 `a642fa96…` | "When `true`, the skill is only included when explicitly invoked via `/skill-name`. The agent will not automatically apply it based on context." | `cursor-skills.md:175` | SrcCursor |
| S071 | https://raw.githubusercontent.com/anomalyco/opencode/3d213123cdf574e55f88711554edfe6fd66a95ad/services/www/src/docs/content/skills.mdx | 2026-10-22T23:12:55Z | 9,187 B, sha256 `931b5425…` | "To load a skill yourself, mention it in your prompt as @skill-id." | `skills.mdx:201` (the source wraps `@skill-id` in backticks; stripped here as the counter's page normalisation does) | Srcopencode |

Quote notes: S067's quote keeps the page's backticks; S071's quote drops the source's inline backticks around
`@skill-id` (the counter's page normalisation drops them too); S069's quote is a clause from a numbered step;
S068's quote is the body of a fenced example. S069 (Gemini CLI) is a model-side tool call and is not counted by the
v2 counter (erratum 1).
