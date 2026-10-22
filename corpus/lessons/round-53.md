# Round 53 — lessons (kotoba, hyaku campaign, attempt 1)

Base `e78dff667237fba2e3cf9eccb802eff5bc9ea302`; plan `3bb0a7a33e6eb585a83a1a55dee30b26079b1e36` (both counters
frozen); plan erratum `5e5336c42a013f21f22df5bae2196eea7a3e2f9a`. Claims: C1 freshness (opencode 1.19.4
re-derivation and re-pin), C2 operability (always-on boxes `alwayson.04` and `alwayson.07` executed; the sourced
claim). Seat reports: `.ufo/waves/round-53/build/` (34 seats), `.ufo/waves/round-53/falsify/` (36 seats).

## Mistakes

| id | class | evidence | captured-by | fix |
|---|---|---|---|---|
| M41 | `stale-baseline` | Round 52 left `verifiers/corpus-baseline.json` un-re-recorded after its own files landed. Each revision's own gate: `c8579a4c` 5/9 pass (DRIFT `tracked_files`, `unindexed`, `report_total`, `report_dead`); `0c9180a6` 5/9 pass with `unindexed` fixed and `commit_total` 31/30 new. Same pass count, changed finding set; the round's no-harm test compared exit codes and counts only (`.ufo/waves/round-52/falsify-a2/ExecGateMatrix.md`), so the new finding reached the outside closure only (`corpus/lessons/round-52-verifier-spotcheck.md` § 2, routed defect 2). Mined by seat `ScribeMistake` (`.ufo/waves/round-53/build/ScribeMistake.md`). | none — no rule compared a red gate's finding set between base and head | `verifiers/check_gate_finding_delta.py` (adopted byte-exact from the seat's sandbox, sha256 `1c41414e…`): runs each revision's own corpus-integrity gate and exits 1 when head has a DRIFT id base lacked. Shown able to fail: `--base c8579a4c… --head 0c9180a6…` → `new: corpus.pointers.commit_total`, exit 1; control `--base e78dff66… --head e78dff66…` → exit 0; `--self-test` 0 failures over 9 assertions (L1 runs, 2026-10-22). Scope: corpus-integrity only; it cannot see a dishonest re-record. |
| M42 | `loose-match` | The round-52 MCP counter matched a host pin by string prefix and a quote by substring: mutants M12 (`github.com/modelcontextprotocol-evil/…` admitted under the `github.com/modelcontextprotocol` pin) and M16 (a fragment of the recorded quote) both survived, count 5 of 7 unchanged (`.ufo/waves/round-52/falsify-a2/MutMcpCounter.md`; spot-check routed defect 4). | none — Q25 asks that a counter can fail on removed content, not that its matching is exact | `verifiers/check_mcp_instructions.py` now requires the exact host and a whole path-segment prefix, and a quote equal to a Gate quote recorded for that row (`.ufo/waves/round-53/build/ExecMcpTighten.md`): its self-test kills M12 and M16 (each 7/7 → 6/7 on the mutated data), and the declared round-52 results re-measure unchanged with the tightened script (`c8579a4c` 0 of 7, `c8407a45` 5 of 7, `e78dff66` 7 of 7; L1 runs). QUALITY Q32. The round-52 record's frozen bytes stay `4c003a4b:verifiers/check_mcp_instructions.py`. |
| M43 | `overclaim` | The round-53 plan (`3bb0a7a3`) said more than its counters print: C1's statement named omp 18.12.6 and its sha and the version 1.19.4, which the counter does not print; "retiring or re-kinding a class to clear the gate is not kept" holds only for the baseline file (a retirement inside the gate printed the target line, `CriticC1Sizing.md` patch B); C2's FAIL cases were called "dated/transient" though all four contain a date (`CriticC2Sizing.md`); "C2 works a different frontier area" overstated (round 49's C2 named the same Frontier row, `CriticDrift.md`). The drift-sentinel class (rounds 50–52) recurred in plan prose. | Q26 and Q31 — caught by the wave-1 critics before any C1 or C2 content landed | Plan erratum `5e5336c4` (append-only, landed before the C1 and C2 commits): statements bounded to the printed line, the counters' trust boundary named, three C1 guards and one C2 guard added outside the frozen counters, the frontier sentence narrowed. QUALITY Q33. Shown able to fail: the wave-2 seat `W2CriticDrift` checks commit order and every statement against its counter. |
| M44 | `process` | The L1 integrated the C1 seat patch with `git apply --3way`, which writes the lane Git index (round prompt § 6.4 forbids `git add` and lane index mutation); the index was then reset by the helper's next jj mutation and the landed commit `6dd31164` holds exactly the patch's paths. | the round prompt's commit-order rule (§ 6.4) | Apply seat patches with plain `git apply` (working tree only); the falsify-wave context now names `apply --index/--3way` among forbidden lane writes. Not shown able to fail mechanically: a procedural fix, recorded as such. |

## Gate

### Admitted (rows opened this round; full fetch records in the seat reports named)

| row | URL | opened (UTC) | bytes, sha256 | quote (≤25 words) | location | seat |
|---|---|---|---|---|---|---|
| S043 | https://code.claude.com/docs/en/memory.md | 2026-10-22T20:04Z | 51,971 B, `971d75bf…` | "An `AGENTS.md` and a `CLAUDE.md` or `CLAUDE.local.md` in your working directory or above it" → "Your `CLAUDE.md` files only" | `memory.md:357` | L1 (19:5xZ), ScribeClaudeCode, CriticC2Sizing, ScoutClaudeBehaviour |
| S044 | https://learn.chatgpt.com/docs/agent-configuration/agents-md.md | 2026-10-22T20:08:31Z | 9,149 B, `9d1f87a2…` | "In each directory along the path, it checks for `AGENTS.override.md`, then `AGENTS.md`, then any fallback names in `project_doc_fallback_filenames`." | `agents-md.md:12` | ScribeCodex |
| S045 | https://opencode.ai/docs/rules (served `.md` and HTML) | 2026-10-22T20:04:44Z | 6,684 B, `dfb242d9…` | "The first matching file wins in each category. For example, if you have both `AGENTS.md` and `CLAUDE.md`, only `AGENTS.md` is used." | `rules.mdx:103` | ScribeOpencode, ScoutLaneCorpusAlwaysOn |
| S046 | google-gemini/gemini-cli `docs/cli/gemini-md.md` at `451a02ff` (raw) | 2026-10-22T20:10:20Z | 3,807 B, `d00eeaef…` | `"fileName": ["AGENTS.md", "CONTEXT.md", "GEMINI.md"]` | `gemini-md.md:105` | ScribeGemini |
| S047 | https://code.visualstudio.com/docs/copilot/customization/custom-instructions (source `microsoft/vscode-docs@fd64d648`) | 2026-10-22T20:10:54Z | 25,213 B, `eb2be087…` | "Do not depend on a file order or precedence rule to resolve conflicts" | `custom-instructions.md:315` | ScribeVSCode |
| S048 | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md | 2026-10-22T20:05:13Z | 8,730 B, `00e45ea5…` | "When multiple applicable user-level and repository instruction files exist, Copilot CLI combines their instructions." | `copilot-cli-custom-instructions.md:30` | ScribeCopilotCli |
| S049 | https://cursor.com/docs/rules.md | 2026-10-22T20:09:33Z | 17,403 B, `884c67ca…` | "Cursor supports AGENTS.md in the project root and subdirectories." | `rules.md:321` | ScribeCursor |
| S050 | https://zed.dev/docs/ai/instructions.md | 2026-10-22T20:05:08Z | 3,169 B, `7c63efe0…` | "Project instruction files apply to the current project. Zed uses the first matching file in this list:" | `instructions.md:25` | ScribeZed |
| S052 | https://cursor.com/help/customization/rules.md | 2026-10-22T20:09:33Z (re-opened 20:36Z by W2ReopenS049) | 6,285 B, `c6d2b069…` | the § How does CLAUDE.md work in Cursor? answer, quoted in `ScribeCursor.md` § Gate record | `rules.md:97-99` | ScribeCursor; added after falsify seat W2ReopenS049 found the entry's Cursor `CLAUDE.md` cell had no row behind it |
| S051 | https://github.com/anomalyco/opencode/compare/v1.19.3...v1.19.4.diff and `releases.atom` | 2026-10-22 (fetch log in the seat report) | diff 48 entries, `a6a680ae…` | "Upgraded the bundled Bun runtime to 1.4.4, which includes security fixes for Brotli, TLS, HTTP/1.1, HTTP/2, HTTP/3, WebSocket, and fetch" | `releases.atom:27` | ScoutOcRelease |

### Rows touched (old → new)

- S004 (agents.md): `status` queued → mined; `used-by` — → `corpus/knowledge/alwayson-rule-files-round53.md`. Re-opened by
  ScribeAgentsMdSpec, 2026-10-22T20:04:34Z, 81,690 B, `06b65de9…` (the round-46 record carries `e3a5b9a4…`; the
  bytes changed, the quoted sentence did not): "The closest AGENTS.md to the edited file wins; explicit user chat
  prompts override everything." (`FAQSection.tsx:20`).
- S019 (Anthropic skills best practices): `used-by` gains `corpus/knowledge/alwayson-rule-files-round53.md`.
  Re-opened by ScribeDatedAuthority (byte-identical to the S019 record): `### Avoid time-sensitive information`
  (`best-practices.md:574`).
- S050 (Zed, written this round at `55973a20`): `anchor` cell reworded in place before the report,
  "at commit `cfb894a5`" → "at zed-industries/zed@`cfb894a5`", because the corpus gate reads the words
  "commit `<hex>`" as a lane commit pointer and flagged the upstream Zed commit `commit_unresolvable`. Same source,
  same commit, no change of meaning. This edits a cell the contract keeps append-only (rule 2 allows only
  `status`, `recheck`, `used-by`); it is disclosed here rather than carried as a red gate or a duplicate row.

### Rejected (opened, not admitted as rows)

Each seat report lists its rejections with reasons (`Scribe*.md` §§ Rejected); none is promoted to a row. Not admitted
although opened: the further pages each scribe drafted (Codex config sample, config advanced, customization overview,
import, app server, `agents_md.rs`; Gemini CLI configuration reference, memory import processor, tutorial, loader
source; VS Code settings reference and four release notes; GitHub concepts, repository instructions, support matrix,
reusable, custom-agents pages; Cursor help, CLI, CLI changelog, Bugbot; Zed loader source and release notes; the
agents.md site source; the Claude Code changelog; opencode V2 instructions source, `instruction.ts`, changelog,
release atom) — one row per client is enough for the entry's claims; their quotes stay in the seat reports and the
entry cites the seat report where it uses one.

### Q30 sweeps

Every client negative in the entry ("no `@` import", "no size limit", "no dated-text rule", "`GEMINI.md` not read")
carries the three legs in its seat report: changelog or release notes, current docs source tree, lane-corpus grep.
Where a leg could not be run (Claude Code publishes no docs source tree: the `llms-full.txt` export was used; agents.md
page component 404), the seat says so and the client is recorded `not checked` for that point.

## Routed defects from the round-52 spot-check

1. opencode 1.19.4 re-pin — C1 (`6dd31164`).
2. Corpus-integrity baseline — the five dead fleet-report pointers now resolve against the fleet root (both corpus
   instruments, self-test arms 150 → 152 and 91 → 93) and the spot-check file is indexed (`aeed0890`); the baseline is
   re-recorded last, in the closing commit, after every round file has landed; M41's check runs on that commit.
3. Self-test arms for the two round-52 attempt-2 C1 fixes — `aeed0890` (`ExecSurfArms.md`: each arm fails with its
   fix reverted, 2 failures each).
4. The MCP counter's prefix pin and substring quote — M42, Q32, `aeed0890`.
5. Drift sentinel — M43; C2 works the always-on half of the "executed checklist coverage" row (plan § Erratum 4;
   the operator rules whether that satisfies the sentinel).
6. Q30 — applied to every client negative (§ Q30 sweeps above).

Carried with reasons (unchanged this round): the omp MCP `instructions` question and plugin surfaces (Frontier;
not this round's area), the C1 limits found by the round-52 falsify wave (member-call loaders, a new callee with
only an undeclared pair, decoy stand-ins), R5 v2 configured-root oracle, R1 no-name fallback, the D7 items, D2
F1–F5 (`corpus/lessons/round-52.md:114-115`).
