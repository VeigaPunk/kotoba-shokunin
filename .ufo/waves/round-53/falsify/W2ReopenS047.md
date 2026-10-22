# W2ReopenS047 — re-open of SOURCES row S047 (VS Code custom instructions)

Result: MIXED — the S047 row re-opens byte-identically and every line it cites says what the row says, but the knowledge row that cites S047 attributes two defaults ("each behind a setting that defaults on", "Markdown links … defaults off") and one joint-reading claim to a page that does not state them, and the page that does state them (`ai-settings.md`, opened and pinned by the wave-1 seat) has no SOURCES row.

Seat: `KotobaR53.W2ReopenS047` (leaf). Lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin` at judged revision `c775d6823bfca8f0de8c0874032a954438b38edc`. Sandbox clone `/fast/scratch/hyaku/kotoba-r53/w2/KotobaR53.W2ReopenS047/clone` — `git rev-parse HEAD` → `c775d682…` and `git status --porcelain | wc -l` → `0`, both exit 0. No lane file was edited; no tool installed or upgraded; no model call; no lane git/jj write.

## 1. Re-open receipt (S047 URL)

| attempt (UTC) | command shape | status | bytes | sha256 |
|---|---|---|---|---|
| 2026-10-22T20:36:35Z | `curl -sS` on the row's URL, no `-L` | 301 | 79 | `df1d4d50837a085ef04724c57a301256917cf27f73496aedad125a193879d1b9` |
| 2026-10-22T20:36:46Z | `curl -sSL` on the row's URL | 200 (final `/docs/agent-customization/custom-instructions`) | 162,008 | `dc87f7c2a0c19e731bb2902306f505740bef05dc78df1214a1fbc67a374b7ab0` |
| 2026-10-22T20:38:14Z | `curl -sSI -A curl/8` (headers) + `curl -sSL` new route | 301 `location: /docs/agent-customization/custom-instructions`; new route 200 | 162,008 | `dc87f7c2…` |

Recorded in the row: "rendered page fetched 2026-10-22T20:04:53Z (200, 162,008 B, sha256 `dc87f7c2…`)" (`corpus/SOURCES.md:60`). **Bytes and sha256 reproduce exactly; the recorded 200 is only reachable by following a 301** (the historical 20:04:53Z fetch itself cannot be replayed).

Pinned source, `https://raw.githubusercontent.com/microsoft/vscode-docs/fd64d64891a2e660bcc0d32ea402da905adfef7f/docs/agent-customization/custom-instructions.md`, fetched 2026-10-22T20:37:04Z: **200, 25,213 B, sha256 `eb2be0877a6241a520bdd41cf26346ec2ba9c8a0576f855cb09f0d2b4ce34d6b`** — the row's "(25,213 B, sha256 `eb2be087…`)" reproduces exactly (HOLDS). `docs/copilot/customization/custom-instructions.md` at the same commit: 404, 14 B. `main` on 2026-10-22T20:38:25Z: 25,213 B, sha256 `eb2be087…`; `diff -q` against the pin → exit 0, so no source drift since `fd64d648`.

Rendered page and pinned source agree for every cited claim: each of `Project instructions can use`, `The nested-file setting is disabled by default`, `CLAUDE.local.md`, `is enabled by default`, `no general precedence order`, `Do not depend on a file order or precedence rule`, `includeReferencedInstructions`, `Markdown links` occurs exactly once in the 162,008 B render.

## 2. Per-cited-line verdicts (pinned `custom-instructions.md`, 378 lines)

| line | cited as | what the line says (quote ≤25 words) | verdict |
|---|---|---|---|
| 45 | § Types of instruction files | "Project instructions can use `.github/copilot-instructions.md`, `AGENTS.md`, or `CLAUDE.md`." + "The Local harness-specific settings in the sections below control discovery." | HOLDS (heading is line 30; :45 is the Local-harness NOTE inside the section, matching the file's body-line citation convention) |
| 79 | § Use a `.github/copilot-instructions.md` file | "The Local harness also discovers this workspace file when `setting(github.copilot.chat.codeGeneration.useInstructionFiles)` is enabled." | HOLDS |
| 89 | same section | "For personal, always-on instructions … use `~/.copilot/copilot-instructions.md`." | HOLDS |
| 229 | § Use an `AGENTS.md` file | "Avoid conflicting guidance because there is no general precedence order between these files." | HOLDS |
| 232 | same section | "`setting(chat.useAgentsMdFile)` … is enabled by default." | HOLDS |
| 236 | same section (nested subsection) | "Use nested `AGENTS.md` files when different folders need different guidance." | HOLDS |
| 239 | same section (nested subsection) | "Set both … to `true`" / "The nested-file setting is disabled by default." | HOLDS |
| 248-257 | § Use a `CLAUDE.md` file | "searches for Claude instructions in these locations when `setting(chat.useClaudeMdFile)` is enabled"; four-row table (workspace root, `.claude`, user home, `CLAUDE.local.md`) | HOLDS |
| 315-319 | § Resolve conflicting instructions | "Applicable instruction sources are additive. Do not depend on a file order or precedence rule" | HOLDS (verbatim; 16-word quote matches) |
| 332 | § Tips for writing effective instructions | "Keep your instructions short and self-contained." | HOLDS |

Knowledge-file pointers: `source custom-instructions.md:45, 229-257, 315-319 at fd64d648` (`corpus/knowledge/alwayson-rule-files-round53.md:1`) — all three ranges exist at the pin and cover the file-name, AGENTS/nested, CLAUDE-location and additivity statements. `:315` quote at line 29 is a verbatim substring. Those pointers HOLDS.

## 3. Defects

**D1 — MEDIUM (citation / provenance). Knowledge row asserts defaults and link gating that S047 does not state, and the source that does state them has no SOURCES row.**
`corpus/knowledge/alwayson-rule-files-round53.md:29` says the three always-on families are "each behind a setting that defaults on (`custom-instructions.md:45, 229-257`)". At the pin, the page states a default exactly twice: `useAgentsMdFile` "is enabled by default" (:232) and "The nested-file setting is disabled by default" (:239). For `github.copilot.chat.codeGeneration.useInstructionFiles` (:79) and `chat.useClaudeMdFile` (:248, :257) the page only gates ("when … is enabled"), never states the default. The same cell's "Markdown links behind a setting that defaults off" has no pointer at all; S047:73 only says "use Markdown links" and :360 lists `chat.includeReferencedInstructions` among settings to check are enabled.
The facts are true, but from a different page: `https://raw.githubusercontent.com/microsoft/vscode-docs/fd64d64891a2e660bcc0d32ea402da905adfef7f/docs/agents/reference/ai-settings.md` (fetched 2026-10-22T20:39:16Z, 200, 67,275 B, sha256 `6157cfd8b7d7439d88891c96454b6087f3d764588c57d85efa84139b2d270bb2`) — `:343` copilot-instructions `true`, `:351` `chat.useAgentsMdFile` `true`, `:352` `chat.useClaudeMdFile` `true`, `:353` `chat.useNestedAgentsMdFiles` `false`, `:342` `chat.includeReferencedInstructions` `false`.
That page was opened and pinned by the wave-1 seat, which drafted a row for it (`.ufo/waves/round-53/build/ScribeVSCode.md:145`, 67,275 B, `6157cfd8…`), but it landed nowhere: `grep -c 'ai-settings' corpus/SOURCES.md` → `0`, exit 1; S-rows total 51 (`grep -c '^| S0'` → 51, S051 last); the knowledge header (line 1) lists S043–S050, S004, S019 and no such row. So the knowledge cell's defaults are supported by an unpinned, unrowed page. Fix: land the ai-settings row and point the cell at it, or strike "defaults on"/"defaults off" from the cell. Note the plan's own Frontier line required rows "for every always-on source opened this round".

**D2 — LOW (unmarked inference). "reads both" is presented as documented; the seat recorded it as [INFERENCE].**
`alwayson-rule-files-round53.md:29` states the joint outcome for AGENTS.md + CLAUDE.md in one directory as "reads both" backed by the additive sentence at `:315`. `:315` is general ("Applicable instruction sources are additive") and no line on the page states the pair outcome; the seat wrote exactly that: "That composition is `[INFERENCE]`: no sentence names the `AGENTS.md` + `CLAUDE.md` pair." (`.ufo/waves/round-53/build/ScribeVSCode.md:58`). § Limits (`corpus/knowledge/alwayson-rule-files-round53.md:69-84`) does not disclose it, and line 40 then uses it as a mechanical claim ("the `CLAUDE.md` then adds only its client-specific lines"). Fix: mark the cell and line 47-48 `[INFERENCE]`.

**D3 — LOW (imprecision). The row's nested-AGENTS parenthetical omits the required second setting.**
`corpus/SOURCES.md:60` says "nested files when `chat.useNestedAgentsMdFiles` is on". The cited line it summarises, `:239`, says "Set both `setting(chat.useAgentsMdFile)` and `setting(chat.useNestedAgentsMdFiles)` to `true`", and ai-settings `:353` says "Requires `setting(chat.useAgentsMdFile)` to be enabled." A reader who turns on only the nested setting gets no nested discovery. Fix: "nested files when both `chat.useAgentsMdFile` and `chat.useNestedAgentsMdFiles` are on".

**D4 — LOW (URL hygiene). The row's URL cell is now a 301.**
`corpus/SOURCES.md:60` and `corpus/lessons/round-53.md:27` both record `https://code.visualstudio.com/docs/copilot/customization/custom-instructions`; on re-open it answers 301 with `location: /docs/agent-customization/custom-instructions` (2026-10-22T20:38:14Z, HTTP/2 301, 79 B, sha256 `df1d4d50…`). The redirect target is byte-identical (162,008 B, `dc87f7c2…`), and the source pin already lives under `docs/agent-customization/`, so content is unaffected; only reproducibility is. Fix: record the canonical route and note the 301, as S051's row already does for sst/opencode.

## 4. What HOLDS (attacked and not broken)

- Row S047's bytes, sizes and sha256 for both the rendered page and the pinned source: exact on re-open; `main` still byte-identical to the pin (no drift since `fd64d648`).
- Every line S047 cites exists, is inside the section it names, and says what the row attributes to it (§2 table); the rendered page carries every cited sentence.
- The negative sweep the knowledge row rests on: `grep -c -i symlink custom-instructions.md` → `0`, exit 1; `grep -c '`@'` → `0`, exit 1. No `@` import and no symlink rule is documented for these files on this page.
- The lessons row's quote and receipt for S047 (`corpus/lessons/round-53.md:27`: 25,213 B, `eb2be087…`, quote at `:315`) reproduce; the quote is a verbatim substring.
- The row's own scope line — "(vendor documentation for VS Code; not a measurement of the editor)" — is satisfied: no editor binary was run, and nothing in the row claims a measurement.

## 5. Remaining unknowns

- The commit date of `fd64d648…` and whether it was `main` tip on 2026-10-22: `GET https://api.github.com/repos/microsoft/vscode-docs/commits/fd64d648…` returned 403, `{"message":"API rate limit exceeded for 179.218.13.209…"}` (2026-10-22T20:38:25Z and 20:38:29Z, both with a UA). Only content equality of `main` at 20:38:25Z could be checked.
- Whether the recorded 20:04:53Z render differed from today's: not replayable; today's is byte-identical to what the row records, so the record is consistent.
- Whether any other lane file leans on the "defaults on" wording; `grep -rn S047` over `verifiers/` and `corpus/` finds only prose uses (knowledge lines 1, 29, 40, 53; lessons line 27), none machine-read, so D1/D2 are documentation defects with no counter behaviour attached.
