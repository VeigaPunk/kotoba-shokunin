# Round 59 — lessons (kotoba, hyaku campaign, attempt 1)

Plan `plans/round-59.md` (draft `a3e70a30`, freeze `4b2125c9`, addendum `67b68e0f`; controls `283124cd`). C1 (depth): hook
files by client. Seat reports: `.ufo/waves/round-59/{w0,controls,build,falsify}/`.

## Gate

### Admitted (rows opened this round; fetch records in the seat reports named; snapshots `.ufo/waves/round-59/snapshots/`)

- **S096 Claude Code** — https://code.claude.com/docs/en/hooks.md — accessed 2026-10-23T09:34:52Z (HTTP 200, 274,129 B, sha256 `c6ef9d21…`; seat `SrcClaudeCode`, census `CensusClaudeCode`) — `hooks.md:910`: "This `PreToolUse` hook in `.claude/settings.json` runs a project script before each Bash command, and blocks the command if the script fails:"
- **S097 Codex** — https://learn.chatgpt.com/docs/hooks.md — accessed 2026-10-23T09:35:05Z (HTTP 200, 47,133 B, sha256 `57166ef0…`; seat `SrcCodex`, census `CensusCodex`) — `hooks.md:38-44` (line breaks folded; link and list marker kept): "a default `hooks/hooks.json` file. See [Build plugins](https://developers.openai.com/plugins/build/plugins#bundled-mcp-servers-and-lifecycle-hooks) for the plugin packaging rules. In practice, the four most useful locations are: - `~/.codex/hooks.json`"
- **S098 VS Code** — https://code.visualstudio.com/docs/agent-customization/hooks.md — accessed 2026-10-23T09:35:04Z (HTTP 200, 15,152 B, sha256 `98c5be6b…`; seat `SrcVSCode`, census `CensusVSCode`) — `hooks.md:59-60` (pipes written `&#124;`, line break folded): "Automation shared with a repository &#124; `.github/hooks/*.json` at the repository root &#124; &#124; Hooks"
- **S099 Copilot CLI** — https://docs.github.com/en/copilot/concepts/customizations/hooks.md — accessed 2026-10-23T09:34:55Z (HTTP 200, 8,428 B, sha256 `23370e09…`; seat `SrcCopilotCLI`, census `CensusCopilotCLI`) — `hooks.md:28`: "Copilot CLI also supports personal hooks in `~/.copilot/hooks/*.json`."
- **S100 Gemini CLI** — https://geminicli.com/docs/hooks/best-practices.md — accessed 2026-10-23T09:34:48Z (HTTP 200, 17,650 B, sha256 `fb44fbcf…`; seat `SrcGeminiCLI`, census `CensusGeminiCLI`) — `best-practices.md:413`: "When you open a project with hooks defined in `.gemini/settings.json`:"
- **S101 Cursor** — https://cursor.com/docs/hooks — accessed 2026-10-23T09:35:23Z (HTTP 200, 69,145 B, sha256 `8436af76…`; seat `SrcCursor`, census `CensusCursor`) — `hooks:50`: "If you have hooks defined in `.cursor/hooks.json` at the root of your project, cloud agents pick them up and run them during their work."
- **S102 Claude Code (S089 anchor correction, routed R4)** — https://code.claude.com/docs/en/slash-commands.md — accessed 2026-10-23T09:34:33Z (HTTP 200, 114,542 B, sha256 `6b070e87…`, identical to S089; seat `ScribeR4Note`) — `slash-commands.md:152`: "Choose where skills load"

SKILL intro quotes (on admitted rows' pages; seat `ScoutInstructionVsHook`): S099 `hooks.md:15` "Unlike custom instructions, hooks run code rather than asking the model to follow a rule."; S098 `hooks.md:6` "…without relying on the model to request the action."

### Rejected (opened or built this round, not admitted)

- **opencode `.opencode/plugins/` as a hook-file token** — reject: hook code is a plugin module; the token carries the banned word `plugins` and `opencode.ai/docs/hooks.md` is HTTP 404 (`Censusopencode`, `SrcOpencodeNegative`); the SKILL row says so in plain words.
- **VS Code `.github/hooks/audit.json` as the lead token** — reject: an example file the page asks you to create (`hooks.md:77`), not the documented location; the row leads with the folder pattern `.github/hooks/*.json` (`hooks.md:59`), scored True by `SrcVSCode` through the frozen counter's checks.
- **Copilot CLI `.github/hooks/*.json` as its lead token** — reject: it is the VS Code row's token, and E5 would disqualify both rows; the Copilot row leads with its own personal path and names the shared folder in plain words (`CensusCopilotCLI`, `CriticCensus`).
- **Codex `~/.codex/config.toml` as the lead token** — reject: general config that may hold inline `[hooks]` tables, not the dedicated hook file (`CensusCodex`).
- **Codex quote spanning `<repo>/.codex/hooks.json`** — reject: tag-shaped text is stripped on the page side only, so the frozen quote check fails (`CtlFabEvents`); the admitted quote stops at `~/.codex/hooks.json`.
- **Gemini CLI hooks-overview quote** — reject: 29 words, above the 25-word cap (`CensusGeminiCLI`); the best-practices page carries a 10-word quote.
- **`https://cursor.com/docs/hooks.md` as the S101 URL** — reject: HTTP 404 (389 B) to the counter's curl header set at 09:2xZ (`CtlFabEvents`, `ScoutHookSecurity`); `https://cursor.com/docs/hooks` serves the same markdown (sha256 `8436af76…`).
- **Claude Code `best-practices` / `features-overview` "hooks are deterministic" lines as SKILL intro basis** — not opened as rows this round (`ScoutInstructionVsHook`); the intro rests on S098 and S099 instead.
- **In-place edit of S089's anchor cell (R4)** — reject: the SOURCES contract allows in-place changes only to `status`, `recheck`, `used-by`; a correction is a new row (`ScribeR4Note`); S102 appended.

### Rows touched (old → new)

None in place. S089 is byte-identical; S102 supersedes its anchor. S085 is cited by the new SKILL opencode row; its `used-by` is unchanged (the SKILL file is not a `used-by` path in this registry).

## Mistakes

M79–M83 are the round-58 spot-check routes R1, R2, R3, R5 and R4, drafted by seat `ScribeMistakes`
(`.ufo/waves/round-59/build/ScribeMistakes.md`) and checked by the L1; M84 is this round's own (the mined mistake).

- **M79 `misrooted-seat-report-and-premature-sweep`** · `ReviewBudgetMove` wrote its report to the fleet root, not the lane, it was omitted from seat accounting, and the misroot sweep snapshot preceded the later report write (`corpus/lessons/round-58-verifier-spotcheck.md:243-252`; `.ufo/waves/round-58/falsify/ReviewBudgetMove.provenance.md:3-10`; `.ufo/waves/round-58/falsify/ScoutMisroot.md:3-27`) · captured-by: the round-58 non-author spot-check, routed defect R1 · fix: pin the output directory in `.ufo/waves/round-59/bounds.md` and rerun the sweep after the last seat settles · shown able to fail: `timeout 5 ls /home/vgpnk/Projects/shokunin/.ufo/waves/round-58/falsify/ReviewBudgetMove.md` → exit 0, stdout `/home/vgpnk/Projects/shokunin/.ufo/waves/round-58/falsify/ReviewBudgetMove.md`.

- **M80 `final-tip-receipts-asserted-not-committed`** · the final-tip checklist success and `4 DRIFT` count were asserted without receipts naming `ed44e0c4`; available tip-named receipts instead record earlier revisions, including `noharm-tip.txt` at `46b4a706` and `C1-remeasure-tip.txt` at `6de8e2eb` where the checklist fails (`corpus/lessons/round-58-verifier-spotcheck.md:253-257`; `.ufo/waves/round-58/noharm-tip.txt:1-8,38-39`; `.ufo/waves/round-58/C1-remeasure-tip.txt:1-25`) · captured-by: the round-58 non-author spot-check, routed defect R2 · fix: commit receipts naming the exact final tip and recording the checks run there · shown able to fail: `timeout 10 git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin ls-tree -r --name-only ed44e0c4807b92d99417eaff04a0fd2122f981b4 -- .ufo/waves/round-58 | grep -E 'verify_skill_checklist|checklist.*tip'` → exit 1, no output (no matching receipt path).

- **M81 `counter-blind-fields-and-ua-sensitive-fetch`** · the frozen C1 counter reads the token and action cells but not `What a file sets`; replacing all seven field cells with `x` left its output unchanged, while Cursor's Python-urllib request returned HTTP 403 where curl returned HTTP 200, moving G to its floor (`.ufo/waves/round-58/falsify/MutC1Content.md:146-161`; `.ufo/waves/round-58/falsify/ReopenS094.md:46-48`; `corpus/lessons/round-58-verifier-spotcheck.md:258-262`; frozen source `.ufo/waves/round-58/w0/check_command_files.py:762-783`) · captured-by: round-58 counter falsification and non-author spot-check, routed defect R3 · fix: for future counters, cover field cells or name the seat that checks them, and preserve a committed `--fetch` snapshot run; do not alter the frozen round-58 rule or targets · shown able to fail: the prior falsify-seat command `timeout 600s python3 -B verifiers/check_command_files.py --rev "$REV" --fetch` on mutant (f), which replaced all seven field cells with `x`, printed `custom command files found on the live page 6 of 6; new ground 4` and `exit 0` (`MutC1Content.md:146-161`; sandbox commit `b8e7d8aa99cb903d1b89d5b82696b2db3a337d9b` at `/fast/scratch/hyaku/kotoba-r58/MutC1Content`). This is the earlier seat's recorded run, not a run by me.

- **M82 `budget-delta-started-at-freeze-not-base`** · “600 → 596” used the freeze as its start, although the round's base had 598 lines; future budget lines should name the base (`corpus/lessons/round-58-verifier-spotcheck.md:265-266`) · captured-by: the round-58 non-author spot-check, routed defect R5 · fix: state the base revision and its line count when reporting the round delta · shown able to fail: `timeout 20 bash -o pipefail -c 'for r in f56f6e191762c27c1aa2af11a204db9e2ca4edec 3de87aad29e960c95ed35840442f424c48c29729 ed44e0c4807b92d99417eaff04a0fd2122f981b4; do printf "%s SKILL.md lines: " "$r"; git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show "$r:SKILL.md" | wc -l; done'` → exit 0; output `f56f6e191762c27c1aa2af11a204db9e2ca4edec SKILL.md lines: 598`, `3de87aad29e960c95ed35840442f424c48c29729 SKILL.md lines: 600`, `ed44e0c4807b92d99417eaff04a0fd2122f981b4 SKILL.md lines: 596`.

- **M83 `source-anchor-label-not-page-heading`** · SOURCES row S089 anchors the quote with `§ Where skills live`, but fetched `slash-commands.md` has the page heading `## Choose where skills load` (`corpus/lessons/round-58-verifier-spotcheck.md:263-264`; `corpus/SOURCES.md:102` at `ed44e0c4`; `.ufo/waves/round-58/build/SrcClaudeCode.md:40-41`; fetched page `.ufo`-external snapshot `/fast/scratch/hyaku/kotoba-r58/SrcClaudeCode/claude-slash-commands.md:152`) · captured-by: the round-58 non-author spot-check, routed defect R4 · fix: the SOURCES contract allows no in-place anchor edit (`CORPUS.md:112-118`, `build/ScribeR4Note.md`), so correction row S102 (`supersedes S089 —`, anchor `§ Choose where skills load` at `slash-commands.md:152`) is appended and S089 stays byte-identical · shown able to fail: `timeout 10 git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -n -o -F '§ Where skills live' ed44e0c4807b92d99417eaff04a0fd2122f981b4 -- corpus/SOURCES.md` → exit 0, stdout `ed44e0c4807b92d99417eaff04a0fd2122f981b4:corpus/SOURCES.md:102:§ Where skills live`; the cited fetched page line 152 reads `## Choose where skills load`.

- **M84 `census-token-substituted-without-rescore`** (the mined mistake) · the L1 wrote the VS Code lead token in the frozen
  census table as `.github/hooks/*.json` (`plans/round-59.md` census row, freeze `4b2125c9`) while the census seat had
  scored `.github/hooks/audit.json` ELIGIBLE and called the wildcard E5-rejected on the premise that Copilot CLI would
  lead with it (`w0/CensusVSCode.md`); the build context then repeated the substituted token as "the census" ·
  captured-by: `SentinelContexts` (build) and `ScribeEntry` (both flagged the mismatch) · fix: the census table cell
  states the substitution and its reason in-cell, `SrcVSCode` scored the substituted token through the frozen counter's
  quote and event checks on the snapshot and live (all True), and the Copilot row leads with its own path so E5 does
  not fire; rule for next rounds: a census token the L1 changes is re-scored by a seat before the freeze, never after ·
  shown able to fail: `grep -c 'audit.json' .ufo/waves/round-59/w0/CensusVSCode.md` prints ≥ 1 while the freeze plan's
  VS Code row leads with `.github/hooks/*.json`.
