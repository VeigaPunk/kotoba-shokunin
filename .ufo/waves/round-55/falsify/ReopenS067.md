Result: HOLDS — S067 re-opened byte-identical (same sha256/bytes); every S067 cell (lesson Gate quote, SOURCES row, entry reading, SKILL.md table row) is byte-exact or a faithful, no-wider reading of the live page.

Seat: KotobaR55.ReopenS067 (wave-2 FALSIFY, kotoba round 55). Read-only on the lane; tip f0e6b695b746775823b65a8c45de7d50ea33e84f. Fetched bytes kept at /fast/scratch/hyaku/kotoba-r55/ReopenS067/vscode-agent-skills.md.

## 1. Re-open of the row URL

- Row: corpus/SOURCES.md:80 — S067, Visual Studio Code — Use Agent Skills in VS Code, https://code.visualstudio.com/docs/agent-customization/agent-skills.md, docs, tier A, mined, opened 2026-10-22.
- Fetch record (mine): `date -u` → `Fri 23 Oct 2026 12:09:13 AM UTC`; `curl -sS -o … https://code.visualstudio.com/docs/agent-customization/agent-skills.md` → HTTP 200, 23,082 bytes, sha256 `26973567be23eb5756eb6db62afacf055455fbe6f427d40b45659aacb44d361a`.
- Matches the row's recorded fetch (SOURCES.md:80: HTTP 200, 23,082 B, sha256 `26973567…361a`, fetched 2026-10-22T23:13:16Z) exactly. The live page is byte-identical to the page the row was mined from, so byte-exact checks below transfer to the recorded fetch. Host `code.visualstudio.com` is the counter's first pinned host for VS Code (verifiers/check_explicit_invocation.py:129).

## 2. Lesson Gate quote — HOLDS

- corpus/lessons/round-55.md:16 records for S067: quote "You can add extra context after the slash command. For example, `/webapp-testing for the login page` or `/github-actions-debugging PR #42`." at `agent-skills.md:287`, 23,082 B, sha256 `26973567…`.
- Fetched bytes line 287 (`grep -n -F`, exit 0): byte-exact, including the page's backticks — exactly as the quote note at corpus/lessons/round-55.md:22 states ("S067's quote keeps the page's backticks"). No normalisation needed.
- Surrounding anchors also exact: `## Use skills as slash commands` at fetched line 283 (SOURCES anchor `agent-skills.md:283-287`), and the invoked/context sentence at 285.
- 20 words — within the 25-word quote cap.

## 3. SOURCES row cells — HOLDS

- teaches (SOURCES.md:80): "VS Code gives `/webapp-testing` as a skill slash-command example and says extra context may follow the command" — 17 words (≤25). Page support: fetched 287 gives `/webapp-testing` as the example of a skill slash command with extra context after it. Says no more than the page; no over-wide phrase found.
- Anchor cell: `agent-skills.md:283-287` (section span) and `disable-model-invocation` field `:151` — both verified on the fetched bytes (283 header; 151 is the field row: "Set to `true` to require manual invocation through the `/` slash command only."). No over-wide phrase found.
- Q30-sweep precondition not triggered: the row does not claim the client is silent about anything.

## 4. Entry row (corpus/knowledge/explicit-invocation-round55.md:24) — HOLDS

- quote cell: byte-identical to fetched line 287 (same string as §2). location cell `agent-skills.md:287`: correct.
- reading cell: "Selecting or typing the skill's slash command invokes it (`:285`); extra task context may follow the command." Fetched line 285: "Type `/` in the chat input field to see a list of available skills and prompts, and select a skill to invoke it." — both the typing and the selecting readings are on the line; `:285` correct; the context claim is line 287. Says no more than the page.
- Other S067 uses in the entry check out: source line 1 (`agent-skills.md:287`), findings 1 (`/` sigil for VS Code) and 3 (`disable-model-invocation: true` (S067 `:151`) — fetched line 151 confirms the field, default `false`, `true` = manual only).

## 5. SKILL.md § Explicit invocation by client, VS Code row (SKILL.md:201) — HOLDS

- form: `` `/<skill-name>`, e.g. `/webapp-testing` `` — backticked token `/webapp-testing` occurs verbatim on fetched line 287; the slash-command mechanism is documented at 283-287.
- what it does: "Invokes the named skill as a slash command, with optional context after it; `disable-model-invocation: true` makes this the only way (`:151`)" — invoke at 285, optional context at 287, "only way" at 151 plus the fetched line-295 configuration row (`disable-model-invocation: true` → slash command Yes, auto-loaded No). Each clause is on the page; `:151` correct.
- action: "Set the turn aside as explicit when its user text starts with the skill's `/name`, even when task text follows" — grounded in the page's only example, which shows command-first ordering with task text after (`/webapp-testing for the login page`, fetched 287); the page nowhere shows context preceding the command. The entry discloses this as a measure choice, not a page quote (entry findings 1, lines 32-35: "'starts with `/name`' and 'holds `/name`' differ: the action cells say which"), so it is not an over-wide record of the page. Recorded as an interpretive dependency in Residual risk, not a defect.
- Non-counted status consistent: the S067 quote contains no standalone word `skill`, and both the entry Limits section and corpus/lessons/round-55.md:34 record that the v2 counter therefore does not count the VS Code row (admitted, kept on the reading) per erratum 1. Not a new finding.

## Verdict per cell

| Cell | Verdict |
|---|---|
| URL re-open (status/bytes/sha256) | HOLDS — byte-identical to recorded fetch |
| Lesson Gate quote + location (lessons/round-55.md:16) | HOLDS — byte-exact at fetched :287, backticks kept as noted |
| SOURCES teaches (≤25 words, ≤ page) | HOLDS — 17 words, no over-wide phrase |
| SOURCES anchors (:283-287, :151) | HOLDS |
| Entry quote/location/reading (explicit-invocation-round55.md:24) | HOLDS |
| SKILL.md:201 form / what it does / action | HOLDS |
| v2-counter non-counted routing (lessons:34, entry Limits) | HOLDS — consistent with erratum 1 |

## Residual risk and verification gaps

- My fetch is ~1 h after the recorded one (2026-10-23T00:09:13Z vs 2026-10-22T23:13:16Z); identical bytes today, but the page can drift later — the row's recheck is 90d.
- The action cell's "starts with" rests on the page's single example ordering; VS Code's page does not explicitly state message-initial placement. The entry discloses this as a choice; a future measure inheriting "starts with" inherits that interpretation.
- Client behaviour was not run or measured (paid model calls forbidden); all verdicts are documentation-text checks, as the entry itself states.
- No installs or upgrades were performed (no tooling need arose; pacman guard respected trivially).
