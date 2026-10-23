Result: HOLDS — `SKILL.md` § Hook files by client at `c63ccc6823e1f6a8577acbb43d19551eadbbee9a` sits correctly under § Instruction surfaces, stays inside the 600-line budget (596→587), carries tokens byte-identical to the entry, every cited line resolves byte-exact on the six committed snapshots (and the opencode row's cites resolve on the S085 pin, verified live), and backtick discipline matches the frozen rule exactly.

Reviewer: KotobaR59.ReviewSkillSection, 2026-10-23. Lane read-only throughout; every lane git call read-only. All file reads done against a sandbox clone at the pinned revision: `/fast/scratch/hyaku/kotoba-r59/ReviewSkillSection` (`git checkout -q c63ccc6823e1f6a8577acbb43d19551eadbbee9a`); the only write in the lane is this report. No lane code executed; the counter was not re-run (other seats' item). Tools installed or updated: none (pacman paused host-wide; nothing needed).

## 1. Placement — PASS

`git show c63ccc6:SKILL.md` puts `### Hook files by client` at SKILL.md:121–133, inside `## Instruction surfaces — pick the file before the fix` (SKILL.md:60), immediately after `### Custom command files by client` (:107, table ends :119) and before `## Router model` (:135). Heading text is exactly `### Hook files by client` and the table header is exactly `| Client | Hook config | Events | Action |` (plan §35 contract; `plans/round-59.md:35-37`). The plan's "beside § Custom command files by client" requirement is met literally.

## 2. Line budget — PASS

```
$ git --no-optional-locks show a975cbbf00534443c49bf02e29c813a3db0bf0f8:SKILL.md | wc -l   → 596
$ git --no-optional-locks show c63ccc6823e1f6a8577acbb43d19551eadbbee9a:SKILL.md | wc -l   → 587
$ git --no-optional-locks show d64d945b3435e2532203c505ad64ecf5d91b780e:SKILL.md | wc -l   → 587
```

596 (base) → 587 (data commit and tip), both under the 600 budget; the base value matches the R5-mandated figure (596). Net −9 despite the new 14-line section because the same commit moved the § Sources production-skill bullets verbatim to `corpus/knowledge/anatomy-and-compression.md` § "Moved from SKILL.md § Sources — production skill files (round 59)" (confirmed at anatomy-and-compression.md:142-159; SKILL.md diff also shows +1 Gate-registry row for `check_hook_files.py` at the § Gate registry table).

## 3. Backtick discipline in Hook config cells — PASS

Mechanical scan of SKILL.md:127-133 (column 2 = Hook config):

```
Claude Code cell spans: ['.claude/settings.json']
Codex cell spans:       ['~/.codex/hooks.json']
VS Code cell spans:     ['.github/hooks/*.json']
Copilot CLI cell spans: ['~/.copilot/hooks/*.json']
Gemini CLI cell spans:  ['.gemini/settings.json']
Cursor cell spans:      ['.cursor/hooks.json']
opencode cell spans:    []   (cell = "no hook file: hook code is a plugin module (§ Plugin manifests by client; S085, S087)")
```

Each client cell holds exactly one backticked span and it is the token; the opencode negative row holds zero — matching the build spec ("NO backticked path in the Hook config cell") and SrcOpencodeNegative's advice. Line refs are never backticked anywhere in the table (`S096 :243-245`, `S085 index.mdx :1738, :1746` are plain). Events cells hold only event-name spans (`PreToolUse`, `SessionStart`, …, `execute.before`, `execute.after` — each matches the frozen `^[A-Za-z][A-Za-z0-9_.:-]*$` pattern, ≥2 distinct per cell).

## 4. Table ↔ entry consistency (tokens, sources) — PASS

Tokens: SKILL.md:127-133 column 2 spans are byte-identical to `corpus/knowledge/hook-files-round59.md` table column 2 (entry :21-27) for all six eligible clients; the opencode negative row is intentionally absent from the entry table — the counter's own reject line confirms this is the designed shape (`.ufo/waves/round-59/C1-measure.txt:9`: "reject opencode: SKILL.md hook config cell holds no backticked token; no entry row names the client"; eligible-rows-only precedent from round 57).

Sources: entry frontmatter `source:` URLs equal `corpus/SOURCES.md` rows S096–S101 (SOURCES.md:108-113): `code.claude.com/docs/en/hooks.md`, `learn.chatgpt.com/docs/hooks.md`, `code.visualstudio.com/docs/agent-customization/hooks.md`, `docs.github.com/en/copilot/concepts/customizations/hooks.md`, `geminicli.com/docs/hooks/best-practices.md`, `cursor.com/docs/hooks`. All six are `docs`/`A`/`mined`/`opened 2026-10-23`/`used-by corpus/knowledge/hook-files-round59.md`. The claim's "+ S102" is a Claude Code command-file correction row (SOURCES.md:114, "supersedes S089 — S089 anchor correction", R4 re-open), correctly outside the hook entry — the claim's parenthetical is accurate (S102, not the S103 the scribe draft assumed; see M3).

Snapshot↔SOURCES hash binding (`sha256sum` over committed `.page` files vs the sha256 printed in each row):

```
S096 c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8  = row ✓
S097 57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92  = row ✓
S098 98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08  = row ✓
S099 23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4  = row ✓
S100 fb44fbcfaccc3cdb7895d989f3808bed66cfa6516411535c4c4d9077d242e7bc  = row ✓
S101 8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d  = row ✓
```

The entry's claim "each sha256 equals its SOURCES row" holds verbatim. Events cells and parenthetical cites match the entry's per-client notes everywhere they overlap (:33/:37/:40/:65 S096; :19/:25/:27/:30-46 S097; :4/:58-62/:128/:130/:202 S098; :28/:34/:37 S099; :31/:413/:442 S100; :27/:50/:67/:88/:102/:1340 S101).

## 5. Every cited line exists on the snapshot — PASS

`grep -n` over the committed `.page` files (all line numbers are file lines, no shaping):

- S096 (4219 lines): `:33` `| SessionStart | When a session begins or resumes |`, `:37` `| PreToolUse | Before a tool call executes. Can block it |` (entry adds `:40` PostToolUse, `:65` SessionEnd — all present); `:243-245` = user `~/.claude/settings.json` / project `.claude/settings.json` / local `.claude/settings.local.json` rows; `:4146` = the WARNING line "Command hooks execute shell commands with your full user permissions… Review and test all hook commands before adding them".
- S097 (1130 lines): `:19` non-managed review/trust line, `:25` PreToolUse row, `:27` SessionStart row, `:30-46` "Where Codex looks for hooks" + `hooks.json`/`config.toml` forms + four locations incl. `~/.codex/hooks.json` (:44).
- S098 (214 lines): `:4` title with "(Preview)", `:6` "without relying on the model to request the action" (intro quote byte-exact substring), `:58-62` personal/repository/settings-map/plugin/agent-scoped rows (`.github/hooks/*.json` on :59), `:128` sessionStart row, `:130` preToolUse row, `:202` "Hook configuration and scripts are executable code. Review them before use".
- S099 (165 lines): `:15` "Unlike custom instructions, hooks run code rather than asking the model to follow a rule." (intro quote byte-exact prefix), `:26` "Do not assume that the same events, input, or output work unchanged across surfaces.", `:28` repository `.github/hooks/*.json` + personal `~/.copilot/hooks/*.json`, `:34` sessionStart, `:37` preToolUse.
- S100 (709 lines): `:31` "(like `BeforeTool` or `AfterModel`)." (both event names on the cited line), `:413` "When you open a project with hooks defined in `.gemini/settings.json`:", `:442` "**Verify the source** of any project hooks or extensions before enabling them.".
- S101 (1507 lines): `:27` `preToolUse`/`postToolUse`/`postToolUseFailure` bullet, `:50` cloud-agents quote (entry row), `:67` `| postToolUse | Yes |`, `:88` `| sessionStart | Deferred while cloud agents… |`, `:102` "User-level hooks (`~/.cursor/hooks.json`) are not available in cloud agents.", `:649` "Project hooks run in any trusted workspace", `:781` "Require the workspace to be trusted to run", `:1340` sessionStart section (entry-internal cite).
- S085 (opencode Events cell, `index.mdx :1738, :1746`): no committed snapshot for this pre-existing round-57 pin; verified live instead. Fetch record: `Fri 23 Oct 2026 10:01:50 AM UTC`, `curl -sS https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/build/plugins/index.mdx` → HTTP 200, 60,780 bytes, sha256 `e505931a59faa9a6685be195ccf42fcd8e3ddb9bb1d9e52f95d3b6c862cb83a5` — byte-identical to the sha256 the S085 SOURCES row records (`60,780 B`, `e505931a…83a5`). On those exact bytes: `:1738` `await ctx.tool.hook("execute.before", (event) => {`, `:1746` `await ctx.tool.hook("execute.after", (event) => {` — the cited event names are printed at the cited lines.

## 6. Counter coherence — PASS

Committed counter at the data revision: `sha256sum verifiers/check_hook_files.py` = `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71` (frozen value). `check_hook_files.py:253-254` → `TARGET = 4`, `NEW_TARGET = 5`. L1 receipt `.ufo/waves/round-59/C1-measure.txt`: `--fetch` exit 0, "6 of 6; 6 of 6; new ground 6" → F=6≥4, G=6≥5, predicate MET; no-`--fetch` run exits 1 with G=0 as designed (no live evidence). Coherent.

## Findings

None breaking in scope. Minor observations (not verdict-affecting):

- **M1 — cite-style inconsistency (cosmetic).** The new hook table uses plain `S096 :243-245` line refs; sibling tables (§ Custom command files, § Plugin manifests) backtick theirs (``S089 `:450` ``). Uniform inside the new table and consistent with the build spec's "do not backtick the line refs" instruction for the opencode Events cell — reads as the new convention applied table-wide, not a defect.
- **M2 — opencode Events line refs unverifiable from the entry alone.** SKILL.md:133 cites `S085 index.mdx :1738, :1746`; the entry's opencode note records only `S085, S087` with no line refs, and the S085 row's anchor names Hooks `:1335-1418` (the ToolHooks block actually sits at 1733-1758). The cited lines do exist on the pinned bytes (verified live, §5); a reader can't confirm them from the entry without refetching.
- **M3 — S102 supersede landed without caller migration (adjacent section).** SOURCES.md:114 S102 "supersedes S089", but `corpus/knowledge/command-files-round58.md:2` (and :43, :52) still names S089; the scribe draft assumed migration to S103 which became S102 and no caller was moved. Outside this section (likely deliberate to keep `check_command_files.py` scoring stable); noted for the L1 and ReviewMistakes.

## Residual risk / verification gaps

- Event *semantics* (whether each printed identifier is truly an event per the vendor page) is the addendum's named limit: routed to per-client `Cells<Client>` seats; this seat verified printing + placement only.
- Live-page equivalence of S096-S101 (`found 6 of 6`) was confirmed via the L1 receipt, not a re-fetch on my seat.
- The `--self-test` path and mutated-world behaviour of the counter are the mutators'/controls' items, not re-run here.

Report: .ufo/waves/round-59/falsify/ReviewSkillSection.md
