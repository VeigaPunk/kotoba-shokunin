# Round 57 — lessons (kotoba, hyaku campaign, attempt 1)

Base `47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a`; plan and frozen counters `ee50d8fa7b5d260fff8bc332f4a90513bee518ff`;
erratum 1 (C1 counter v2, C2 withdrawn before data) `01312a77e36317feb6e961aba77841ddab1225ca`; v2 re-control receipts
`27af04a7ed8cee74291fd8237f5c73c43243ce02`. Claim: C1 depth (plugin manifests by client; the learning and sourced
claim). Seat reports: `.ufo/waves/round-57/w0/`, `.ufo/waves/round-57/controls/`, `.ufo/waves/round-57/build/`.

## Gate

### Admitted (rows opened this round; fetch records in the seat reports named)

| row | URL | opened (UTC) | bytes, sha256 | quote (≤25 words) | location | seat |
|---|---|---|---|---|---|---|
| S079 | https://code.claude.com/docs/en/plugins-reference.md | 2026-10-23T04:46:45Z | 42,124 B, sha256 `f2910dd6…` | "Save the manifest at `.claude-plugin/plugin.json` under the plugin root." | `plugins-reference.md:34` | SrcClaudeCode |
| S080 | https://developers.openai.com/plugins/build/plugins.md | 2026-10-23T04:47:08Z | 38,036 B, sha256 `c37e330d…` | "The plugin-creator skill will create the plugin folder, create a supported `.codex-plugin/plugin.json` compatibility manifest, and add MCP server wiring for the plugin." | `build-plugins.md:135-137` | SrcCodex |
| S081 | https://code.visualstudio.com/docs/agents/reference/agent-plugin-reference.md | 2026-10-23T04:47:13Z | 21,972 B, sha256 `d6e10328…` | "A root `plugin.json` that declares the canonical Agent Plugins `$schema` uses Agent Plugins semantics." | `agent-plugin-reference.md:97` | SrcVSCode |
| S082 | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating.md | 2026-10-23T04:47:14Z | 7,711 B, sha256 `c0642867…` | "Choose a plugin format, then add a `plugin.json` manifest file to the root of the directory." | `plugins-creating.md:27` | SrcCopilotCLI |
| S083 | https://geminicli.com/docs/extensions/reference.md | 2026-10-23T04:46:46Z | 12,022 B, sha256 `8b9eecb2…` | "Each extension must have a `gemini-extension.json` file in its root directory." | `extensions-reference.md:106-107` | SrcGeminiCLI |
| S084 | https://cursor.com/docs/plugins.md | 2026-10-23T04:46:52Z | 20,323 B, sha256 `74387ff9…` | "plugins with a `.cursor-plugin/plugin.json` manifest, which add rules, agents, commands, hooks, and" | `plugins.md:28` | SrcCursor |
| S085 | https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/build/plugins/index.mdx | 2026-10-23T04:47:59Z | 60,780 B, sha256 `e505931a…` | "Plugins under `.opencode/plugins/` are loaded automatically, like the local example above." | `index.mdx:21` | Srcopencode |

Quote notes (each re-opened against the seat's fetched bytes by the L1, Q42): S079, S081, S084 and S085 are one line
each and unshaped (S084 is a contiguous substring: the list marker and bold label before it and the link after it are
not quoted); S080 folds two line breaks (`:135-137`); S082 omits the list number `2. ` before it; S083 folds one line
break (`:106-107`).

### Rejected (opened or built this round, not admitted)

| item | when | reason | flip |
|---|---|---|---|
| C2 claim (info-less fence line classes, counter `check_infoless_fences.py` at `ee50d8fa`) | 04:20Z–04:45Z | four pre-freeze controls met the frozen predicate without the claimed work: a fence-blind patch keyed on case-directory names and the fixed real command lines (`CtlC2GeneratorKeyed`, 120 of 120 on six seeds), a patch keyed on the extraction path (`CtlC2DoNothingJunk`, 120 of 120 with the instrument self-test green and the live run byte-identical), character skips with an echo fallback (`CtlC2CharShortcuts`, 120 of 120), and a 50-line stub replacing the gate (`MutC2Counter`) | a counter that also requires the measured instrument's own self-test at its base assertion count, drives its scoring end to end in its self-test, and draws every token, name and command line from one distribution (`build/ExecC2CounterV3.md`, redesign input) |
| C1 counter v1 as the claim's rule (`ee50d8fa`) | 04:20Z–04:40Z | `CtlC1RealNoForm` (`5 of 7; new ground 4`), `CtlC1HeldVariant` (`5 of 5; new ground 3`), `CtlC1DoNothingJunk` world C and `CtlC1Fabricated` W5 (`7 of 7; new ground 3`) met it with bare words, nav text, a changelog line and case variants of held words | v2 (erratum 1), re-scored by the same five seats: best hollow world `found 1 of 7` (`controls/CtlC1*.md` § v2 re-score) |
| VS Code row token `.plugin/plugin.json` (Legacy OpenPlugin, `SrcVSCode` draft) | 05:05Z | VS Code's default manifest is the root `plugin.json` (`agent-plugin-reference.md:97`); leading with a legacy third-party format's path would pass the counter and say less than the truth (`CriticC1Rows`) | VS Code documents a VS Code-named manifest path |
| opencode `package.json` as the row token (`Srcopencode` draft) | 05:05Z | a published package's metadata file, not a plugin manifest; the row names the plugin folder and says there is no JSON manifest | none |
| GitHub Flavored Markdown spec as a new row for C2 (`ScoutC2Source`) | 04:55Z | C2 was withdrawn, and the CommonMark spec is already row S005; neither spec states that an info-less fence declares no language (the claim would rest on [INFERENCE]) | a C2 redesign that needs the source |
| Copilot CLI legacy manifest paths (`.github/plugin/plugin.json`, `.plugin/plugin.json`) | 05:05Z | they are listed on the CLI plugin reference, base row S028; re-citing a base URL for a counted row is barred, and the creation guide S082 names only the root `plugin.json` | none |

### Rows touched (old → new)

None. S079–S085 are new rows; S005 and S028 are unchanged.

## Corrections to round 56 (R2 — quote provenance)

- **S076 (Gemini CLI).** The quote recorded in `corpus/lessons/round-56.md:18` and
  `corpus/knowledge/agent-definition-files-round56.md:25` is the user-level location at `subagents.md:324`; it states
  `~/.gemini/agents/*.md` and supports the project token `.gemini/agents/*.md` only through substring matching. The
  project location is at `:323`, and the 24-word span `:320-323` witnesses it without shaping. The quote cells are
  unchanged; the entry carries the correction in its quote-notes paragraph, registered in
  `verifiers/check_correction_sweep.py` (row `r57-r2-s076-note`).
- **S078 (opencode).** The recorded quote joins prose at `agents.mdx:41`, the fence info string `text` at `:43` and the
  example body at `:44`, with backticks stripped and whitespace folded; `text` is a fence label, not prose. Registered
  as `r57-r2-s078-note`.
- **`SKILL.md:109` clause.** "singular `agent/` still loads per a 2026-01-17 docs commit" had no SOURCES basis
  (`ReopenS078` F3); it now cites the pinned migration page `migrate-v1.mdx:486` (re-opened in round 56, HTTP 200,
  20,805 B, sha256 `f3d42b36…`, `.ufo/waves/round-56/falsify/ReopenS078.md:138-142`), which is not a SOURCES row.
  Registered as `r57-r2-skill-singular-agent`.
- **Round-56 report line 14.** `40c2b5eb`, `41c2f484` and `7639deba` are sandbox commits in
  `/fast/scratch/hyaku/kotoba-r56/` clones (their receipts: `controls/CtlC2Heuristics.md:5`,
  `CtlC2GeneratorKeyed.md:140`, `CtlC1RealNoForm.txt:27` in `.ufo/waves/round-56/`). The fleet report is not edited.
