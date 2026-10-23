Result: HOLDS — S096's row, snapshot and quotes all survive re-opening byte-for-byte against the live page; one LOW label-precision defect in the anchors cell (§ name), no field cell affected.

Seat: KotobaR59.ReopenS096, 2026-10-23. All commit refs at c63ccc6823e1f6a8577acbb43d19551eadbbee9a unless stated. No tool installs were made. All work read-only in the lane; fetched bytes in my scratch /fast/scratch/hyaku/kotoba-r59/ReopenS096/.

## 1. Live re-fetch (attack: the snapshot)

- Command: `curl -sSL -A "Mozilla/5.0 (X11; Linux x86_64) … Chrome/131.0.0.0 Safari/537.36" -o S096.live -w "HTTP %{http_code} downloaded %{size_download} bytes url=%{url_effective}\n" "https://code.claude.com/docs/en/hooks.md"`; exit 0.
- `date -u` before: `Fri 23 Oct 2026 09:53:09 AM UTC`; after: `Fri 23 Oct 2026 09:53:10 AM UTC`.
- Observed: `HTTP 200 downloaded 274129 bytes url=https://code.claude.com/docs/en/hooks.md`; `sha256sum S096.live` → `c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8`; 4219 lines.
- Row (corpus/SOURCES.md:108) records HTTP 200, 274,129 B, sha256 `c6ef9d21…862d8` — both match exactly.
- `cmp S096.live .ufo/waves/round-59/snapshots/S096.page` → identical; `cmp` of the committed blob (`git show c63ccc68:.ufo/waves/round-59/snapshots/S096.page`) vs the worktree snapshot → identical. Snapshot is the verbatim fetched markdown (starts `# Hooks reference`, line 5).
- Claim files unchanged through tip d64d945: `git diff --stat c63ccc68..d64d945 -- SKILL.md corpus/SOURCES.md corpus/knowledge/hook-files-round59.md .ufo/waves/round-59/snapshots/S096.page` is empty, and the tip's S096.page re-hashes to `c6ef9d21…862d8`.
- Timestamp coherence: host local time is UTC-3 (`date` = 06:57:43-03, `date -u` = 09:57:43Z); snapshot mtime 2026-10-23 06:35:06 -0300 = 09:35:06Z, consistent with the row's fetch stamp 09:34:52Z; data commit c63ccc68 stamped 2026-10-23T06:48:15-03:00 = 09:48:15Z, after the fetch. No chronology defect.

## 2. Entry quote (attack: the quote)

- Entry `corpus/knowledge/hook-files-round59.md`, Quote cell (Claude Code row): "This `PreToolUse` hook in `.claude/settings.json` runs a project script before each Bash command, and blocks the command if the script fails:"
- Snapshot line 910 is byte-identical: extracted the cell (stripping the table scaffolding `| Claude Code | … | S096 | ` and trailing ` |` only), `cmp` vs `sed -n '910p'` → `QUOTE BYTE-EXACT vs snapshot:910`. The entry's own shaping note ("S096, S099, S100, S101: one source line, bytes unchanged") is true for S096.
- C1 row-rule preconditions hold on this quote: 21 words (cap 6-25); token `.claude/settings.json` present case-sensitively, backtick-delimited (path-segment boundaries); the word `hook` appears outside the token span; the page prints many distinct event identifiers (table at :31-65). Counter constants TARGET=4, NEW_TARGET=5 at verifiers/check_hook_files.py:253-254; the L1 receipt "hook files backed on committed snapshots 6 of 6; found on the live page 6 of 6; new ground 6" clears both (counter re-execution itself is other seats' assignment).
- Lesson `corpus/lessons/round-59.md:10` repeats the same `hooks.md:910` quote with the same digest prefix `c6ef9d21…` — consistent.

## 3. Gate quote at the stated line (attack: the SKILL Action cell)

- SKILL.md § Hook files by client spans lines 121-133 at c63ccc68 (heading :121, Claude Code row :127) — matches the claim's citation.
- SKILL.md:127 Action: "review and test each command first, it runs with your user permissions (S096 :4146)". Snapshot :4146 (the page's own WARNING under § Security considerations → § Disclaimer, heading at :4140, :4142) reads: "> Command hooks execute shell commands with your full user permissions. They can modify, delete, or access any files your user account can access. Review and test all hook commands before adding them to your configuration."
- Exact line: :4146 is that bullet. Both the SKILL Action cell and the entry's per-client note (":4146") are faithful compressions of it. (The SKILL intro's two gate quotes cite S098 :6 / S099 :15 — other seats' scope.)

## 4. Every anchor line vs the teaches cell (attack: the row)

teaches: "Claude Code hook configuration locations, JSON event/matcher/handler structure, and documented lifecycle events (vendor documentation; not a runtime test)".

- `hooks.md:225-229` "Hook configuration": :225 "Hooks are defined in JSON settings files. The configuration has three levels of nesting:" + :227-229 event → matcher group → hook handlers. Grounds "JSON event/matcher/handler structure". Exact.
- `:237-249` "§ Hook locations": heading "### Hook locations" at :237; table :241-249; :243 `~/.claude/settings.json`, :244 `.claude/settings.json`, :245 `.claude/settings.local.json` — grounds the row's file choice and the SKILL cell "(project; user and local settings files too, S096 :243-245)" and the entry note ":243-245". Exact.
- `:31-65` event table: :31 header, :33 `SessionStart`, :37 `PreToolUse`, :40 `PostToolUse`, :65 `SessionEnd` — all five line cites (row, SKILL, entry) verified line-exact by grep. Grounds "documented lifecycle events". Content exact; see the LOW finding on the section label.
- `:910` project Bash hook example: the sentence introducing the PreToolUse/Bash `onFailure: block` settings example (JSON block follows at :912-927). Exact.
- Scope honesty: the row's "(vendor documentation; not a runtime test)" and the entry's "Not held" section (no hook was run; no cross-client event-semantics claim) match what was actually done. No overclaim found.

## Findings by severity

- LOW (row-label precision, corpus/SOURCES.md:108 anchors cell): "§ Hook events (`:31-65`)" mislabels the section name. Lines 31-65 are the event summary table inside "## Hook lifecycle" (heading at :17); the page's section actually titled "## Hook events" starts at :1219 (per-event input schema), and the page itself distinguishes them at :28: "The table below summarizes when each event fires. The [Hook events](#hook-events) section documents the full input schema…". The row's sibling label "§ Hook locations (`:237-249`)" is heading-exact, so this one label breaks the row's own § convention. Content is unaffected: every cited line says what teaches says, and no downstream consumer (counter, SKILL.md, entry, lesson) reads the section name. Correction if the L1 wants it: relabel to "event summary table (`hooks.md:31-65`, § Hook lifecycle)" or extend the span to `:28-65` to carry the provenance sentence.
- No MEDIUM or HIGH findings.

## Residual risk

- The row's fetch timestamp (2026-10-23T09:34:52Z) is a historical record and cannot be re-observed; it is coherent with the snapshot mtime (09:35:06Z) and the data commit (09:48:15Z), but the exact second is unverified.
- The live page could drift at any later moment; my re-fetch pins equality only at 09:53:09Z. Nothing in the claim needs more.
- The entry's "user and local settings files also hold hooks" reading rests on the locations table naming those files as hook locations (:243-245); the page's config grammar (:225-229) is consistent with that reading. Not independently tested at runtime (honestly declared in "Not held").

## Verification gaps

- I did not execute the counter (assigned to RerunC1Counter / ResC1Remeasure seats); I verified the S096-specific quote/token/event/span preconditions by hand from the committed bytes.
- Single live fetch (one curl at 09:53:09Z), no retry needed — first attempt returned the pinned bytes.
