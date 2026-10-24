# Round 56 — lessons (kotoba, hyaku campaign, attempt 1)

Base `b0b7140b5a7cf8a50f13989ee6285fc8ee245c41`; plan and frozen counters `0f58a469b0e3c4fcefaa11d2a01648b2e88cb257`;
errata 1–3 (C2 withdrawn before data; C1 counter v1.3) `e02f5f5d2f37427e8a77b1c3efb45f84b78c67c8`. Claim: C1 depth
(agent-definition files by client; the learning and sourced claim). Seat reports: `.ufo/waves/round-56/w0/`,
`.ufo/waves/round-56/controls/`, `.ufo/waves/round-56/build/`.

## Gate

### Admitted (rows opened this round; fetch records in the seat reports named)

| row | URL | opened (UTC) | bytes, sha256 | quote (≤25 words) | location | seat |
|---|---|---|---|---|---|---|
| S072 | https://code.claude.com/docs/en/agent-sdk/subagents.md | 2026-10-23T02:48:46Z | 41,461 B, sha256 `5b7aa6c6…` | "**Filesystem-based**: define agents as markdown files in `.claude/agents/` directories." | `sdk-subagents.md:17` | SrcClaudeCode |
| S073 | https://developers.openai.com/codex/subagents.md | 2026-10-23T02:47:05Z | 22,907 B, sha256 `e7469d41`… | "To define your own custom agents, add standalone TOML files under `~/.codex/agents/` for personal agents or `.codex/agents/` for project-scoped agents." | `subagents.md:341-343` | SrcCodex |
| S074 | https://code.visualstudio.com/docs/agent-customization/custom-agents.md | 2026-10-23T02:47:52Z | 15,714 B, sha256 `8643b098`… | "For example, save this planning agent as `.github/agents/planner.agent.md`. It uses read-only tools to research a task and return a plan:" | `custom-agents.md:63` | SrcVSCode |
| S075 | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli.md | 2026-10-23T02:47:19Z | 8,379 B, sha256 `506783b4…` | "Choose between the options to create the custom agent in the repository or in your home directory: Project (`.github/agents/`)" | create-custom-agents-for-cli.md:23-25 | SrcCopilotCLI |
| S076 | https://geminicli.com/docs/core/subagents.md | 2026-10-23T02:47:06Z | 23614 B, sha256 `4b9baa88…` | "2.  **User-level:** `~/.gemini/agents/*.md` (Personal agents)" | `subagents.md:324` | SrcGeminiCLI |
| S077 | https://cursor.com/docs/subagents.md | 2026-10-23T02:47:16Z | 27660 B, sha256 `264b4b00…` | "You can also create subagents manually by adding markdown files to `.cursor/agents/` (project) or `~/.cursor/agents/` (user)." | `subagents.md:427` | SrcCursor |
| S078 | https://raw.githubusercontent.com/anomalyco/opencode/4e0bc52216d91c3a8d10035837b1b6f9b82fd1d3/services/www/src/docs/content/agents.mdx | 2026-10-23T02:50:41Z | 8,779 B, sha256 `6cca5b0a…` | "A nested path becomes part of the agent ID: text .opencode/agents/team/reviewer.md → team/reviewer" | `agents.mdx:41-44` | Srcopencode |

Quote notes: S073's URL redirects to `learn.chatgpt.com/docs/agent-configuration/subagents.md` and its quote folds two
line breaks (`:341-343`) into spaces; S075's quote folds lines 23–25 and strips the list and bold markers on `* **Project**`; S076's quote is the
user-level line (the project line `:323` holds no agent word); S078's quote is a fenced example whose info string
`text` stays and whose fence markers were removed. Detail in `corpus/knowledge/agent-definition-files-round56.md`.

### Rejected (opened or built this round, not admitted)

| item | when | reason | flip |
|---|---|---|---|
| C2 claim (agent-definition boxes executed, counter `check_agentdef_boxes.py` at `0f58a469`) | 2026-10-23T02:31Z–02:38Z | two pre-freeze controls met the frozen predicate without implementing a box: `CtlC2Heuristics` (`40c2b5eb`, `5 of 9`, exit 0) and `CtlC2GeneratorKeyed` (`41c2f484`, case order leaked through the work directory, `5 of 9` on 10 of 10 seeds) | a counter with shuffled order, per-case isolation and a hard negative per heuristic class, re-controlled before data (`build/C2RedesignCounter.md`) |
| C1 counter v1 and v1.1 as the claim's rule | 02:31Z–02:45Z | `CtlC1RealNoForm` met v1.1 with real issue-tracker text naming other clients' or proposed folders (`7639deba`, `5 of 5; new ground 2`, exit 0); `CtlC1HeldVariant` re-cited base URLs through aliases and redirects | v1.3 (errata 1–3), re-scored: `controls/C1-v12-rescore.txt`, `C1-v13-rescore.txt` |
| `check_explicit_invocation.py` v3 patch (`build/ExecInvocationNewGround.patch`, routed defect 2) | 03:00Z | it counts the literal template `$<name>` against base text, so Codex `$` scores as new although `$skill` is held at base (`skill-overlap-levers-round51.md:26`); the right number (2) with the wrong forms | a form match that reads every sigil-prefixed skill token at base, not a template string |
| SKILL.md row tokens chosen to raise new ground (Copilot CLI `~/.copilot/agents/` first, suggested by `ScoutAgentSpec`) | 03:00Z | each row leads with the client's project folder by one rule; picking the user folder to make G 3 instead of counting `.github/agents` once would tune the cell to the counter | none |
| Cursor Action "Apply checklist to Cursor subagents" (`SrcCursor`) | 03:02Z | the checklist is opencode's: it demands `name` = stem and roster enrolment, while Cursor makes `name` optional (`CriticC1Rows`) | replaced by a client-specific Action |
| `agent-plugins.org/specification.md` as a SOURCES row (`ScoutAgentSpec`) | 02:50:43Z | not a pinned client host and states a negative only ("too client-specific for a stable portable contract"); kept as seat evidence | an official cross-client agent-file spec |

### Rows touched (old → new)

None. S072–S078 are new rows. Census W04 for S065 (shared URL with S053, `code.claude.com/docs/en/skills.md`, different
scopes): a scope merge would rewrite a protected cell, so it is reported only (`build/ScribeS065.md`).

## Mistakes

- **M52 `example-name-new-ground`** · round-55 C1 counter v2 printed `new ground 4` where two forms were new
  (`round-55-verifier-spotcheck.md:69-73`, routed defect 2) · captured-by: the outside spot-check; Q38 from this
  round · fix: the round-56 C1 counter counts distinct normalised locations against the whole base tree outside
  `.ufo/`; shown able to fail: `CtlC1HeldVariant-v12.md` world `opencode-held-new-page` (`49ba2ca0`) is found on the
  live page and scores `new ground 0` (`controls/C1-v13-rescore.txt`).
- **M53 `cancelled-seat-output-untracked`** (repeat of M34) · `.ufo/waves/round-55/falsify/ReviewLessonMistakes.md`,
  mtime 2026-10-23T00:26:10Z — after the ~00:21Z settle cancellation and after the round-55 report (00:22:10Z) —
  left untracked · captured-by: Q27, applied only to returned seats · fix: committed `3d8efd7c`; Q40.
- **M54 `counter-checks-presence-not-ownership`** · the round-56 C1 counter v1/v1.1 checked host and text presence:
  issue pages naming other clients' folders met it (`controls/CtlC1RealNoForm.md`, `7639deba`) · captured-by: the
  phase-4 pre-freeze control wave · fix: erratum 2 (docs kind, no tracker URLs, own configuration root); shown able
  to fail: the same world prints `0 of 5`, exit 1 (`controls/C1-v12-rescore.txt`).
- **M55 `generated-cases-leak-order`** · the C2 counter's fixed case order was visible to the delegate through its
  work directory; a delegate that never opened a file met it (`controls/CtlC2GeneratorKeyed.md`) · captured-by: the
  pre-freeze control wave · fix: C2 withdrawn; redesign input `build/C2RedesignCounter.md`. Not shown able to fail
  in this round (no redesigned counter is committed).
- **M56 `seat-killed-sibling-processes`** · seat `ExecFloorsTimeout` ran `pkill -f 'fast/scratch/hyaku/kotoba-r56'`,
  which matched the shared scratch root and killed three runs of seat `ExecCneShortcuts` at ~03:06Z, and its contention test (24 slow runs plus 48 CPU
  workers, 02:57:41Z–03:04:05Z) drove the shared host to load 96 (both disclosed by the seat) · captured-by: none (the bound says "kill any process tree you started", not how) · fix: wave contexts
  say kill by PID of the processes you started, never by a pattern over a shared path.
- **M57 `context-mislabels-counter-version`** · the build-wave context called the C1 counter "v1.1" while the
  commit it named held v1.3 (`CriticAxisFit`, `ScribeC1Frame`, `ReviewPlanCounters`) · captured-by: three seats ·
  fix: the context names the counter by commit and sha256, not by a version label.

## Corrections to round 55

- **M51 bound wording.** `corpus/lessons/round-55.md:48` attributes the incident to "never any git in the fleet
  repo"; the recorded wave contexts say "Never mutate the fleet repo" (`ScribeLessonCorrections`).
- **M50 chronology.** No committed record timestamps when the Fix seats scored their patches; "after seats had
  scored their patches" is [INFERENCE]. `CriticC2Landed.md:17,62` also reads P as "the claimed work in its cheapest
  form", not a shortcut; that disagreement stands unresolved.
- **Routed defect 6 wording.** `451a02ff` is not resolvable in the lane repository; upstream fetches returned 200.
- **Report accounting.** `ReviewLessonMistakes` did write a report (M53); the round-55 report's "without reports"
  is wrong for that seat. The fleet report is not edited; this note is the correction.

## Routed defects from the round-55 spot-check

1. Untracked report: committed (`3d8efd7c`), M53.
2. Example-name new ground: rule applied in the round-56 C1 counter (M52); the v3 patch to the round-55 counter is
   rejected (Gate).
3. C2 counter shortcuts D/P/S: `build/ExecCneShortcuts.md` (see the LOG entry for what landed).
4. Floors nested timeout and 5b preflight returncode: `build/ExecFloorsTimeout.md` (see the LOG entry).
5. 5a misattributed revision message: fixed in seven gates (`250e3026`, `ExecDiagRevMsg`).
6. S065 W04: report-only (Rows touched above).
7. Cross-domain evidence: in the round-56 report (`build/ConnSiblingOverlap.md`).
