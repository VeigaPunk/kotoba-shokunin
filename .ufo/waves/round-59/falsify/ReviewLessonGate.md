Result: HOLDS — The round-59 lesson `## Gate` at `c63ccc6823e1f6a8577acbb43d19551eadbbee9a` is accurate: all seven admitted rows match their seat reports and snapshots byte-for-byte, every rejection carries a reason with evidence in the named reports, and the "Rows touched" claim matches the SOURCES diff.

Seat: `KotobaR59.ReviewLessonGate` (leaf, no subagent dispatch). Lane read-only; all checks read-only `git show`/`git diff` or ordinary curls. No tools installed (none needed). No lane/fleet writes except this report.

## 1. Admitted rows: URL / access time / status / bytes / sha prefix / file:line / quote

Snapshot artifacts (lane `.ufo/waves/round-59/snapshots/`) — `sha256sum` + `wc -c` observed (exit 0):

| Snapshot | bytes | sha256 (full) | matches lesson prefix |
|---|---|---|---|
| S096.page | 274129 | c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8 | `c6ef9d21…` |
| S097.page | 47133 | 57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92 | `57166ef0…` |
| S098.page | 15152 | 98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08 | `98c5be6b…` |
| S099.page | 8428 | 23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4 | `23370e09…` |
| S100.page | 17650 | fb44fbcfaccc3cdb7895d989f3808bed66cfa6516411535c4c4d9077d242e7bc | `fb44fbcf…` |
| S101.page | 69145 | 8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d | `8436af76…` |

- S096 — seat `build/SrcClaudeCode.md:11` records `Fri 23 Oct 2026 09:34:52 AM UTC`, HTTP 200, 274129 B, sha `c6ef9d21…`; quote `hooks.md:910` verified byte-exact in S096.page line 910: "This `PreToolUse` hook in `.claude/settings.json` runs a project script before each Bash command, and blocks the command if the script fails:". ✓
- S097 — seat `build/SrcCodex.md:14-15,100` records `Fri Oct 23 09:35:05 AM UTC 2026`, HTTP 200, 47133 bytes, sha `57166ef03e705973`; folded quote `hooks.md:38-44` verified against S097.page raw lines 38-44 (a default `hooks/hooks.json` … - `~/.codex/hooks.json`; newlines→spaces, link/list markers kept). ✓
- S098 — seat `build/SrcVSCode.md:17,55` records `Fri Oct 23 09:35:04 AM UTC 2026`, HTTP 200, 15152 B, sha `98c5be6b693a19cc`; quote `hooks.md:59-60` verified against S098.page lines 59-60 (pipe delimiters written `&#124;`, line break folded). ✓
- S099 — seat `build/SrcCopilotCLI.md:42,31` records `Fri Oct 23 09:34:55 AM UTC 2026`, HTTP 200, 8428 B, sha `23370e092d2e`; quote `hooks.md:28` verified byte-exact substring in S099.page line 28. ✓
- S100 — seat `build/SrcGeminiCLI.md:13,113` records `Fri Oct 23 09:34:48 AM UTC 2026`, HTTP 200, 17650 B, sha `fb44fbcf…`; quote `best-practices.md:413` verified byte-exact in S100.page line 413. ✓
- S101 — seat `build/SrcCursor.md:17,79` records `Fri 23 Oct 2026 09:35:23 AM UTC`, HTTP 200, 69145 B, sha `8436af76…`; quote `hooks:50` verified byte-exact substring in S101.page line 50. ✓
- S102 — seat `build/ScribeR4Note.md:20,37` records `Fri Oct 23 09:34:33 AM UTC 2026`, HTTP 200, 114542 B, sha `6b070e87…` (S089-identical). No snapshot file exists for S102 (not claimed). Independent live re-fetch at 2026-10-23T09:53:39Z: `curl -sSL` `https://code.claude.com/docs/en/slash-commands.md` → HTTP 200, 114542 bytes, sha256 `6b070e872dea28905a7ea7f45c4d5960f5bdf28cc73ac808799af6d50435ffbd` (exit 0); line 152 = `## Choose where skills load`. The "identical to S089" identity claim holds against the live page. ✓

Census cross-check: each row's sha/bytes match its census fetch (`w0/CensusClaudeCode.md:17`, `CensusCodex.md:11-20`, `CensusVSCode.md:13-14`, `CensusCopilotCLI.md:13`, `CensusGeminiCLI.md:14`, `CensusCursor.md:10`). SKILL-intro quotes also verified on the snapshots: S099 `hooks.md:15` ("Unlike custom instructions, hooks run code rather than asking the model to follow a rule.") and S098 `hooks.md:6` ("…without relying on the model to request the action.").

## 2. Rejections: reason + evidence present

1. opencode `.opencode/plugins/` — `w0/Censusopencode.md:7,19,100` (`/docs/hooks.md` and `/docs/hooks` both HTTP 404; segment `plugins` banned) and `build/SrcOpencodeNegative.md:7,13` (hook code is a plugin module; no backticked token; counter rejects as not well-formed per `controls/CtlFabEvents.md:39`). ✓
2. VS Code `.github/hooks/audit.json` — S098.page:77 "Create `.github/hooks/audit.json`:" (example file), vs documented folder pattern at S098.page:59; `build/CriticCensus.md:21` (VS-1: tutorial filename). ✓
3. Copilot CLI `.github/hooks/*.json` as lead — `w0/CensusVSCode.md:85` ("A Copilot CLI row that leads with it disqualifies both rows"); `build/CriticCensus.md:34-38` (E5-1). ✓
4. Codex `~/.codex/config.toml` — `w0/CensusCodex.md:84` ("General config file, not the dedicated hook file"). ✓
5. Codex quote spanning `<repo>/.codex/hooks.json` — `controls/CtlFabEvents.md:133-136` (tag-shaped text stripped by `norm_page_case`; quote fails frozen check and stops at token). ✓
6. Gemini CLI hooks-overview quote — `w0/CensusGeminiCLI.md:50` (29 whitespace-separated words > 25 cap; legal quote is best-practices). ✓
7. `https://cursor.com/docs/hooks.md` as S101 URL — `controls/CtlFabEvents.md:118,122-124` (404, 389 B, counter header set at 09:21:27Z; non-`.md` route serves byte-identical markdown sha `8436af76…`) and `build/ScoutHookSecurity.md:34,168`. ✓
8. Claude `best-practices`/`features-overview` "deterministic" lines — `build/ScoutInstructionVsHook.md:49-64,101-103` (on other pages; not opened as rows this round; intro rests on S099:15 and S098:6). ✓
9. In-place S089 anchor edit — `build/ScribeR4Note.md:32,42`; contract verified at `SOURCES-CONTRACT-v1.md:49-51` and `CORPUS.md:113-118`: only `status`/`recheck`/`used-by` change in place; a correction is a new row whose `teaches` opens `supersedes S0NN —`. ✓

## 3. Rows touched accuracy

`git --no-optional-locks diff --numstat a975cbbf00534443c49bf02e29c813a3db0bf0f8 c63ccc6823e1f6a8577acbb43d19551eadbbee9a -- corpus/SOURCES.md` → `7 0 corpus/SOURCES.md` (exit 0): exactly seven added lines, zero modifications/deletions. The only added rows are S096–S102 (grep of `^[-+]` lines outside S096–S102 yields only the diff header). S089 line is byte-identical at base and data (`git show` row 102 both sides). S085 tail is byte-identical at base and data (used-by remains `corpus/knowledge/plugin-manifests-round57.md`; `git diff` contains no S085 line). S102's `teaches` opens `supersedes S089 —` (`corpus/SOURCES.md` data row, S102). SKILL.md at data commit line 133 cites S085/S087 for the opencode hook cell ("§ Plugin manifests by client; S085, S087"), matching the lesson's "S085 is cited by the new SKILL opencode row" claim. "None in place. S089 is byte-identical" therefore holds.

## Residual risk / verification gaps

- S102 has no committed snapshot; its byte identity was verified by a live re-fetch at 09:53:39Z (not the recorded 09:34:33Z fetch). If the site mutates between the two, the recorded fetch itself cannot be re-audited from lane artifacts — but the recorded sha equals the recorded S089 sha, which is stable across both records.
- Quote folding for S097/S098 is as described ("line breaks folded", `&#124;`), verified against the snapshot lines; byte-exactness refers to the folded form, which the risk and frozen counter unescape before matching (CtlFabEvents).
- No finding contradicts the Gate; all checks were run once and exit 0.
