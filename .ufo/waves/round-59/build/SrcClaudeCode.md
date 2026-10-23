Result: MIXED — S096’s fetched source, snapshot, quote and live/snapshot quote-event checks are complete; the requested entry-cell scope note conflicts with the frozen exact-token check, so the entry draft below keeps its config cell exact and records scope beside it.

## Evidence and gates

- Read the frozen counter’s specification and rules before drafting: `verifiers/check_hook_files.py` (frozen sha256 per the round-59 control receipts: `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71`; `TARGET=4`, `NEW_TARGET=5`, lines 253–254). The assigned freeze revision is `67b68e0f9a0c48e5aa5ced63e6117cfca69da491`.
- Sandbox only: `unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE && timeout 900 git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r59/SrcClaudeCode && timeout 900 git -C /fast/scratch/hyaku/kotoba-r59/SrcClaudeCode checkout -q 67b68e0f9a0c48e5aa5ced63e6117cfca69da491` — completed with no output (exit 0); no sandbox commit.
- Exact source fetch command:
  ```sh
  date -u; timeout 45 curl -sSL --max-time 30 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -o /fast/scratch/hyaku/kotoba-r59/SrcClaudeCode/S096-live.page -w '%{http_code} %{url_effective} %{size_download}\n' https://code.claude.com/docs/en/hooks.md; rc=$?; printf 'curl_exit=%s\n' "$rc"; sha256sum /fast/scratch/hyaku/kotoba-r59/SrcClaudeCode/S096-live.page; wc -c /fast/scratch/hyaku/kotoba-r59/SrcClaudeCode/S096-live.page
  ```
  Observed output: `Fri 23 Oct 2026 09:34:52 AM UTC`; `200 https://code.claude.com/docs/en/hooks.md 274129`; `curl_exit=0`; sha256 `c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8`; `274129` bytes. The snapshot was copied byte-for-byte to `.ufo/waves/round-59/snapshots/S096.page`; `cmp -s` exit 0; its `sha256sum` and `wc -c` returned the same hash and 274129 bytes. No bytes were stripped.
- Source evidence in `.ufo/waves/round-59/snapshots/S096.page`: the quote is line 910; `SessionStart` is line 33 and `PreToolUse` line 37 in the Hook events table (their descriptions say session begins/resumes and before a tool call, respectively). `PostToolUse` is line 40 and `SessionEnd` line 65. Hook JSON configuration/event/matcher/handler structure is lines 225–229; user, project, local, policy, plugin, skill and subagent locations/scopes are lines 237–249. Agent hooks, specifically, are marked experimental at line 396; this is not a claim that all hooks or the settings-file scopes are experimental.
- In the sandbox clone, imported `verifiers/check_hook_files.py`, read the copied snapshot bytes, and called its `found_on_page`, `event_on_page`, and `page_why` functions on those bytes and on `m.fetch(URL, pins=m.HOSTS["Claude Code"])` (the counter fetch path uses `run_curl`). The exact checks returned:
  ```text
  fresh_live_fetch=through counter.fetch/run_curl; chars=274119
  snapshot quote_check=True\nsnapshot PreToolUse=True\nsnapshot SessionStart=True\nsnapshot events_check=True\nsnapshot page_why=[]
  live quote_check=True\nlive PreToolUse=True\nlive SessionStart=True\nlive events_check=True\nlive page_why=[]
  ```
  The invocation exited 0. The first inline invocation had a quoting SyntaxError before checks ran (exit 1); it made no file changes, and the successful invocation above reran the requested checks. The `\\n` separators shown above were literal separators in the successful invocation’s printed output.

## Draft rows

SOURCES row (columns in S089–S095 order; hash is the full fetched-body sha256):

```markdown
| S096 | Claude Code Docs — Hooks — https://code.claude.com/docs/en/hooks.md | docs | A | Claude Code hook configuration locations, JSON event/matcher/handler structure, and documented lifecycle events (vendor documentation; not a runtime test) | Hook configuration (`hooks.md:225-229`); § Hook locations (`:237-249`); § Hook events (`:31-65`); project Bash hook example (`:910`); fetched 2026-10-23T09:34:52Z, HTTP 200, 274,129 B, sha256 `c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8` (seat SrcClaudeCode) | Claude Code documents JSON hook settings, lifecycle events, matchers and handlers, with user/project/local settings scopes and event-specific behavior | mined | 2026-10-23 | 90d | corpus/knowledge/hook-files-round59.md |
```

Entry row (counter-compatible form):

```markdown
| Claude Code | `.claude/settings.json` | S096 | This `PreToolUse` hook in `.claude/settings.json` runs a project script before each Bash command, and blocks the command if the script fails: |
```

Scope note for this source/entry: `.claude/settings.json` is project-scoped and shareable; `~/.claude/settings.json` is user-wide, and `.claude/settings.local.json` is project-local (snapshot lines 243–245). This note is kept outside the entry Hook config cell because the frozen check requires that cell to equal the token.

SKILL row draft (short cells; alternative scope plain words and line references included):

```markdown
| Claude Code | `.claude/settings.json` (project; user `~/.claude/settings.json` and local `.claude/settings.local.json`, lines 243–245) | `PreToolUse`, `SessionStart`; also `PostToolUse`, `SessionEnd`; Agent hooks experimental (lines 33, 37, 40, 65, 396) | Move lifecycle handlers here; review event matchers first |
```

Lesson `## Gate` line draft (quote verbatim; `sha256` is the requested prefix):

```markdown
- S096 — https://code.claude.com/docs/en/hooks.md — fetched 2026-10-23T09:34:52Z; HTTP 200; 274129 B; sha256 `c6ef9d211e8c`; `hooks.md:910`: “This `PreToolUse` hook in `.claude/settings.json` runs a project script before each Bash command, and blocks the command if the script fails:”
```

## Frozen-contract conflict

The requested entry-row shape is `| Claude Code | \`.claude/settings.json\` (scope note) | S096 | <quote> |`. The frozen counter’s `hook_cell_matches` requires `cell.replace("`", "").strip() in (token, normalise(token))` (`verifiers/check_hook_files.py:768-771`); its entry check rejects any appended scope note. Thus the requested note cannot be inside that cell while remaining counter-compatible. The scope note is supplied beside the entry row, while the SKILL row carries it in plain words as requested. No counter/rule change is proposed. The requested checks establish only the quote/token and event-presence conjuncts for snapshot and live content; no full-row judge or `--fetch` counter run was performed for this single-seat draft.

## Surfaces, bounds, and artifacts

- Lane files written: `.ufo/waves/round-59/snapshots/S096.page` (required exact fetched bytes) and this report only. `corpus/SOURCES.md`, `corpus/knowledge/hook-files-round59.md`, `corpus/lessons/round-59.md`, and `SKILL.md` were not edited; their S096 rows/line are drafts above.
- Scratch clone and fetch copy: `/fast/scratch/hyaku/kotoba-r59/SrcClaudeCode` only. No lane Git/jj writes, commits, tools installed/updated, paid model calls, browser use, or other checks. The evidence is vendor documentation and counter text matching, not a runtime execution of Claude Code hooks.
- Artifacts: `.ufo/waves/round-59/snapshots/S096.page`; `.ufo/waves/round-59/build/SrcClaudeCode.md`.
