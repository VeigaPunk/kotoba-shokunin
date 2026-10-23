Result: HOLDS — The round-59 PROVINCE.md Core bullet and the corpus/README.md round-59 frontier note are each supported by the entry/SKILL/counter at `c63ccc68`, both state the hook-code scope boundary, and neither claims runtime behaviour.

Reviewed at: `c63ccc6823e1f6a8577acbb43d19551eadbbee9a` (read-only git in the lane). No web sources opened; no lane code executed; no tools installed. UTC: 2026-10-23 09:53Z.

## The two documents (scope)

- `PROVINCE.md:24` — round-59 Core bullet (diff base→rev adds exactly this line).
- `corpus/README.md:177` — round-59 Frontier append-only note; `corpus/README.md:99` — the same round's coverage-map row (adjacent, same commit).

## 1. Every statement is supported by the entry / SKILL / counter

| Statement | Support (path:line at c63ccc68) |
|---|---|
| six clients (Claude Code, Codex, VS Code, Copilot CLI, Gemini CLI, Cursor) document hook-configuration locations and lifecycle events | entry table + per-client notes, `corpus/knowledge/hook-files-round59.md:11-38`; rows S096–S101 in `corpus/SOURCES.md:108-113` (kind docs, tier A, status mined, opened 2026-10-23); SKILL § Hook files by client table `SKILL.md:121-133` |
| "where to route a check that must run at an event instead of writing it into a prompt" | entry intro `hook-files-round59.md:5-7` ("A rule written into a prompt, skill or always-on file is text the model reads; a hook is run by the client at the event … route a must-run check to the right file"); SKILL Action cells `SKILL.md:126-132` |
| scope boundary "(writing or running hook code stays outside the lane, round-13 census)" | entry § Scope boundary `hook-files-round59.md:16-18`, citing the census quote verbatim: "executable surfaces, out of prompt-craft province" at `corpus/knowledge/instruction-surface-census-round13.md:265` (§ C Excluded loader-derived classes) |
| (S096–S101) | rows exist at rev; each opened 2026-10-23; entry frontmatter `source:` list matches |
| "counted by `verifiers/check_hook_files.py --rev <rev> --fetch`" | counter exists at rev; its own sha256 at rev = `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71` (git show + sha256sum), equals the pinned counter sha in the assignment and in the L1 receipt; TARGET/NEW_TARGET at committed lines 253-254 = 4/5; receipt `.ufo/waves/round-59/C1-measure.txt` at `d64d945` records the exact command at rev c63ccc68 → `hook files backed on committed snapshots 6 of 6; found on the live page 6 of 6; new ground 6`, exit 0 (F 6≥4, G 6≥5) |
| "This is documentary evidence, not observed runtime behaviour" | entry frontmatter "(vendor pages, not a runtime test)" `hook-files-round59.md:6`; entry § Not held `:54-55` ("no hook was run; … is the pages' word") |
| "opencode hook code is a plugin surface, not a hook-file row" | entry opencode note `hook-files-round59.md:39-41` (plugin module in `.opencode/plugins/` / `~/.config/opencode/plugins/`); SKILL opencode row `SKILL.md:132`; lesson rejection (opencode `.opencode/plugins/` token) `corpus/lessons/round-59.md` § Rejected; counter's own reject line: `reject opencode: SKILL.md hook config cell holds no backticked token; no entry row names the client` |
| frontier note: counter "checks the cited event identifiers on committed snapshots and live pages, not observed execution" | counter spec: snapshot must carry the quote, the token and every Events span (`check_hook_files.py` SNAPSHOT rule); with `--fetch`, live page must carry quote/token/events; nothing executes hooks — matches plan freeze addendum limit (`plans/round-59.md` at `67b68e0f` lines 93-97: the Events conjunct proves a name is printed, not that a printed identifier is a hook event) |
| frontier note: "Still not held: client runtime behaviour"; "opencode hooks are code in plugin folders" | entry § Not held + opencode note (above) |

Independent spot-checks run by this seat (all pass):
- All six snapshots exist at rev (`.ufo/waves/round-59/snapshots/S096.page`–`S101.page`, git ls-tree) and each sha256 equals its SOURCES row pin (S096 `c6ef9d21…`, S097 `57166ef03…`, S098 `98c5be6b…`, S099 `23370e09…`, S100 `fb44fbcf…`, S101 `8436af76…` — git show | sha256sum vs rows in `corpus/SOURCES.md:108-113`).
- Lesson `## Gate` (round-59.md) records the six quotes verbatim, matching the entry's Quote cells byte-for-byte (incl. S098's `&#124;` shaping).
- Counter sha256 at rev matches the pinned `f695d59e…` (git show | sha256sum → `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71`).

## 2. Scope boundary stated

- PROVINCE.md:24: "(writing or running hook code stays outside the lane, round-13 census)" ✓
- corpus/README.md:177: "writing or running hook code stays outside the lane" ✓
- Entry states it independently and ties it to the census quote (verified verbatim above) ✓

## 3. Nothing claims runtime behaviour

- PROVINCE.md:24 ends "This is documentary evidence, not observed runtime behaviour"; the note's counter description is "…on committed snapshots and live pages, not observed execution" and adds "Still not held: client runtime behaviour." Both scope events to what the pages name rather than observed firing. ✓

## Findings (severity order)

1. **Minor (wording)** — `corpus/README.md:99` coverage-map row: "and the events each hook fires on". The bullet and the frontier note carefully use "lifecycle events [the pages name]"; this row's "fires on" is assertoric about behavior. It is supported only as documented identifiers (plan freeze addendum, `plans/round-59.md:93-97`; entry § Not held: "which events fire … is the pages' word"), and it sits in the same file one line-context away from the more careful phrasing. No observed behavior is claimed anywhere; suggest rewording to "the events the pages name" for consistency with the round's own anti-overclaim rule.
2. **Info (citation label)** — entry § Scope boundary cites the census as "§ excluded surfaces"; the actual section heading is "### C. Excluded loader-derived classes" (`instruction-surface-census-round13.md:264`). The quoted text ("executable surfaces, out of prompt-craft province") is present verbatim at `:265`, so the substance is exact; only the section label is loose. Not a defect in the reviewed bullet/note.

## Residual risk and verification gaps

- This seat did not re-run the counter nor fetch live pages (the L1 receipt at `d64d945` documents exit 0 / 6 of 6 at rev `c63ccc68`, and the counter sha256 was verified against the pinned value). The statements reviewed rely on that receipt plus frozen source inspection.
- The plan's declared Events limit stands: the counter proves each event identifier is printed on the cited page, not that it is a hook event; nothing in the two reviewed documents asserts more.
- The frontier note's "the table routes a check … to the client's hook file" is a fair characterization of the SKILL Action column (Claude Code/Codex/Cursor cells actively route; VS Code/Copilot CLI/Gemini CLI cells state review conditions); if finer precision is wanted, the routing wording applies most directly to three rows.

## Reporting

Report: .ufo/waves/round-59/falsify/ReviewProvince.md
