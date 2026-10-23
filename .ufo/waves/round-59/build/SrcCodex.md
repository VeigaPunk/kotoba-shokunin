Result: DONE — Codex S097 snapshot and row drafts are ready; the frozen counter's quote and event checks passed on both snapshot and fresh live bytes.

## Behavior and source evidence

Opened `https://learn.chatgpt.com/docs/hooks.md` with ordinary curl and the counter's browser User-Agent. Exact command, exit 0:

```sh
timeout 45 bash -c 'date -u; curl -sSL --max-time 30 -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -H "Accept: text/markdown, text/plain;q=0.9, */*;q=0.8" -o /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/snapshots/S097.page -w "HTTP %{http_code} %{url_effective}\n" https://learn.chatgpt.com/docs/hooks.md; rc=$?; printf "curl_exit=%s\n" "$rc"; wc -c /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/snapshots/S097.page; sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/snapshots/S097.page; exit "$rc"'
```

Observed output:

```text
Fri Oct 23 09:35:05 AM UTC 2026
HTTP 200 https://learn.chatgpt.com/docs/hooks.md
curl_exit=0
47133 /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/snapshots/S097.page
57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92  /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/snapshots/S097.page
```

The fetched bytes say `# Hooks`; Codex hooks run scripts or MCP tools during the agentic loop (`S097.page:1,5-6`). The printed locations say “In practice, the four most useful locations are:” and list `~/.codex/hooks.json` first (`S097.page:42-45`). This is the census lead. Other scopes: project-local hooks require a trusted `.codex/` layer; user and system hooks remain loaded in untrusted projects (`:58-60`); managed sources include system, MDM, cloud and `requirements.toml` (`:73-74`); user, project, session and plugin sources are also named (`:371-378`). Non-managed definitions must be reviewed and trusted before they run (`:64-71`). Hooks are stated to be enabled by default (`:314`); I do not infer a broader Preview/experimental status.

### Quote and events

Best available quote containing the lead token and a separate whole “hooks” word, without HTML-shaped text, is the contiguous source excerpt below (`S097.page:38-44`). No source bytes were stripped; original Markdown line breaks are shown here. The excerpt starts at “a default” within line 38 and ends at the first location bullet, before the `<repo>` bullets.

```text
a default `hooks/hooks.json` file. See [Build
plugins](https://developers.openai.com/plugins/build/plugins#bundled-mcp-servers-and-lifecycle-hooks) for the
plugin packaging rules.

In practice, the four most useful locations are:

- `~/.codex/hooks.json`
```

The pre-tool event `PreToolUse` is printed at line 25; session-start event `SessionStart` at line 27, under the page's “Hooks run at different points in a conversation” table (`:21-28`). The table prints ten other distinct event names on lines 25-28. The quote is 22 counter words after backticks are removed. For a one-line table cell below, only source newlines/whitespace are folded to spaces; no text bytes are deleted or substituted.

## Frozen counter probe

Created the required isolated clone and checked out the freeze; command exit 0, no output:

```sh
timeout 300 bash -c 'unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r59/SrcCodex && git -C /fast/scratch/hyaku/kotoba-r59/SrcCodex checkout -q 67b68e0f9a0c48e5aa5ced63e6117cfca69da491'
```

The following command imported `verifiers/check_hook_files.py` from that clone, loaded the saved snapshot bytes, and made a fresh fetch using the module's `fetch()` (which invokes its `run_curl`) with the Codex host pin. Exit 0:

```sh
timeout 120 python3 -c 'import hashlib, importlib.util, pathlib; spec=importlib.util.spec_from_file_location("counter", "verifiers/check_hook_files.py"); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); q="a default `hooks/hooks.json` file. See [Build\nplugins](https://developers.openai.com/plugins/build/plugins#bundled-mcp-servers-and-lifecycle-hooks) for the\nplugin packaging rules.\n\nIn practice, the four most useful locations are:\n\n- `~/.codex/hooks.json`"; token="~/.codex/hooks.json"; events=["PreToolUse","SessionStart"]; sp=pathlib.Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/snapshots/S097.page"); snap=sp.read_bytes().decode("utf-8", errors="replace"); live=m.fetch("https://learn.chatgpt.com/docs/hooks.md", pins=m.HOSTS["Codex"]); qplain=q.replace("`", ""); span=m.token_span(qplain, token); print("snapshot_sha256", hashlib.sha256(sp.read_bytes()).hexdigest()); print("live_utf8_bytes", len(live.encode("utf-8"))); print("live_sha256", hashlib.sha256(live.encode("utf-8")).hexdigest()); checks=lambda label,page: [(label,"quote_word_count",len(qplain.split())),(label,"quote_and_token",not m.quote_why(page,q,token)),(label,"hook_word_outside_token",span is not None and m.hook_word_outside(qplain,span[0],span[1])),(label,"events_cell_valid",not m.events_cell_why(events))]+[(label,"event_"+name,m.event_on_page(page,name)) for name in events]+[(label,"all_page_checks",not m.page_why(page,q,token,events))]; [print(*row) for row in checks("snapshot",snap)+checks("live",live)]'
```

Observed output (the snapshot and fresh live fetch have identical 47,133-byte UTF-8 content and SHA-256):

```text
snapshot_sha256 57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92
live_utf8_bytes 47133
live_sha256 57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92
snapshot quote_word_count 22
snapshot quote_and_token True
snapshot hook_word_outside_token True
snapshot events_cell_valid True
snapshot event_PreToolUse True
snapshot event_SessionStart True
snapshot all_page_checks True
live quote_word_count 22
live quote_and_token True
live hook_word_outside_token True
live events_cell_valid True
live event_PreToolUse True
live event_SessionStart True
live all_page_checks True
```

These are the requested page-level counter checks, not a full `check_hook_files.py --rev ... --fetch` run or C1 predicate verdict. The counter event check verifies case-sensitive event-name presence; the vendor page's event table and labels ground these as lifecycle events.

## Drafts for L1 integration

SOURCES row (column order copied from S089-S095):

```text
| S097 | OpenAI Learn — Hooks — https://learn.chatgpt.com/docs/hooks.md | docs | A | Codex hook configuration locations, lifecycle events, and trust review (vendor documentation, not a runtime test) | § Hooks run at different points in a conversation (`hooks.md:21-28`); § Where Codex looks for hooks (`:30-60`); § Review and trust hooks (`:62-74`); fetched 2026-10-23T09:35:05Z (HTTP 200, 47,133 B, sha256 `57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92`) | Codex documents a user hook file and lifecycle events; non-managed hook definitions must be reviewed and trusted before they run | mined | 2026-10-23 | 90d | corpus/knowledge/hook-files-round59.md |
```

Knowledge entry row:

```text
| Codex | `~/.codex/hooks.json` | S097 | a default `hooks/hooks.json` file. See [Build plugins](https://developers.openai.com/plugins/build/plugins#bundled-mcp-servers-and-lifecycle-hooks) for the plugin packaging rules. In practice, the four most useful locations are: - `~/.codex/hooks.json` |
```

SKILL row (compact cells; the hook token is the first backticked span of Hook config):

```text
| Codex | `~/.codex/hooks.json` (user; project needs trust; system/managed/session/plugin scopes, lines 58–60, 73–74, 371–378) | `PreToolUse`, `SessionStart` (10 other events: lines 25–28; enabled by default: line 314) | Move always-on rules into hooks; review trust and scope first. |
```

`## Gate` lesson line (full URL, exact access time, status, bytes, SHA-256 prefix, snapshot file:lines and quote):

```text
- S097 — https://learn.chatgpt.com/docs/hooks.md; accessed Fri Oct 23 09:35:05 AM UTC 2026; HTTP 200; 47,133 bytes; sha256 `57166ef03e705973`; `.ufo/waves/round-59/snapshots/S097.page:38-44`: "a default `hooks/hooks.json` file. See [Build plugins](https://developers.openai.com/plugins/build/plugins#bundled-mcp-servers-and-lifecycle-hooks) for the plugin packaging rules. In practice, the four most useful locations are: - `~/.codex/hooks.json`"
```

## Touched surfaces, scope, and limits

- Wrote the exact fetched page bytes only to `.ufo/waves/round-59/snapshots/S097.page`; wrote this report to `.ufo/waves/round-59/build/SrcCodex.md`. The four SOURCES/entry/SKILL/Gate snippets above are drafts for the integrator; no product corpus or SKILL file was edited by this seat.
- Counter implementation used: frozen clone at `/fast/scratch/hyaku/kotoba-r59/SrcCodex`, requested revision `67b68e0f9a0c48e5aa5ced63e6117cfca69da491`. No tool installed or updated. No paid client/model calls, browser, challenge bypass, lane Git/jj writes, or full predicate run.
- The page-level checks establish quote/token and printed-event presence on the saved and freshly fetched page. The full row-backed counter and downstream C1 predicate remain for integration; source documentation is not a runtime test.

Report: .ufo/waves/round-59/build/SrcCodex.md
