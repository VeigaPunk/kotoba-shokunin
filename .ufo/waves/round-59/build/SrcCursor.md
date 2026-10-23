Result: PARTIAL — Cursor source evidence and draft rows are complete, but the requested entry-cell scope note conflicts with frozen E4, so the counter-compliant entry row keeps the exact token.

## Findings

- I read the frozen counter and the required `CtlFabEvents.md` and `CtlFabSnapshot.md` controls before drafting. The counter's frozen source hash is `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71`; `TARGET = 4`, `NEW_TARGET = 5` are at `verifiers/check_hook_files.py:253-254`. The source row and snapshot are prepared for S101 on `https://cursor.com/docs/hooks` (the URL returned 200 and exact same page bytes as the census lead).
- The best quote is the unshaped sentence at fetched page line 50, 24 words with the Markdown backticks retained. It contains `.cursor/hooks.json` and `hooks` outside the token. **Bytes stripped: none.** The `preToolUse` event is explicitly called before tool execution (`S101.page:860-862`); `sessionStart` is called when a new composer conversation is created (`:1338-1340`). They are hook events, not merely coincidental identifiers. Other documented events include `postToolUse` (`:897-899`) and `sessionEnd` (`:1372`). The Cursor census reports no experimental/preview/deprecated/beta/alpha markers (`w0/CensusCursor.md:84`).
- The user-requested `(scope note)` suffix cannot be added to the entry `Hook config` cell and still pass the frozen counter. `hook_cell_matches` strips backticks and then requires the cell to equal the token or its normalized form (`verifiers/check_hook_files.py:768-771`); the entry check applies that rule (`:797-800`). I therefore place the project/cloud-agent scope note outside the counter-compliant entry cell. The requested expanded form is shown below as **rejected**, not as a passing row.

## Fetch provenance and snapshot

Successful source fetch command (ordinary curl, browser User-Agent, counter `Accept` header):

```text
date -u && timeout 60 curl -sSL -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -o /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/snapshots/S101.page -w 'HTTP_STATUS=%{http_code}\nSIZE_DOWNLOAD=%{size_download}\nURL_EFFECTIVE=%{url_effective}\n' 'https://cursor.com/docs/hooks' && wc -c /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/snapshots/S101.page && sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/snapshots/S101.page
```

Observed output, exit 0: `Fri 23 Oct 2026 09:35:23 AM UTC`; `HTTP_STATUS=200`; `SIZE_DOWNLOAD=69145`; `URL_EFFECTIVE=https://cursor.com/docs/hooks`; `69145 .../S101.page`; sha256 `8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d`. The byte count and digest match the census page (`w0/CensusCursor.md:10,12`) and the prior control's alternate-URL capture (`controls/CtlFabSnapshot.md:162`).

Fetch-path failures/limits observed before selecting the source URL:

- At `Fri 23 Oct 2026 09:34:22 AM UTC`, the first `https://cursor.com/docs/hooks.md` write failed because the snapshots directory did not yet exist: curl exit 23, `HTTP_STATUS=200`, `SIZE_DOWNLOAD=0`, `curl: (23) client returned ERROR on write of 5921 bytes`. No usable response body was captured by that attempt.
- After creating the required snapshots directory, a retry of `https://cursor.com/docs/hooks.md` with the same browser UA and Accept header returned HTTP 404, 389 bytes, sha256 `4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1` (`Fri 23 Oct 2026 09:34:48 AM UTC`). That 404 body was overwritten by the successful `/docs/hooks` response. The cited source URL is therefore `/docs/hooks`, not the failing `.md` route.

## Frozen quote and event checks

Sandbox used: `/fast/scratch/hyaku/kotoba-r59/SrcCursor`, checked out at `67b68e0f9a0c48e5aa5ced63e6117cfca69da491`. Clone command completed with `CLONE_OK`; `git rev-parse HEAD` returned that revision, and clone `verifiers/check_hook_files.py` hashed to the frozen counter digest above. The following Python was run through `functions.eval`; it imported only the cloned counter and read the saved snapshot bytes:

```python
import hashlib, importlib.util
from pathlib import Path
clone = Path('/fast/scratch/hyaku/kotoba-r59/SrcCursor')
spec = importlib.util.spec_from_file_location('check_hook_files_r59', clone / 'verifiers/check_hook_files.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
quote = 'If you have hooks defined in `.cursor/hooks.json` at the root of your project, cloud agents pick them up and run them during their work.'
token = '.cursor/hooks.json'
events = ('preToolUse', 'sessionStart')
snapshot_bytes = Path('/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/snapshots/S101.page').read_bytes()
snapshot = snapshot_bytes.decode('utf-8', errors='replace')
status, effective, live_bytes = mod.run_curl('https://cursor.com/docs/hooks')
live = live_bytes.decode('utf-8', errors='replace')
# For each page: quote check is `not quote_why(page, quote, token)`;
# each event check is `event_on_page(page, event)`.
```

Observed results: counter hash `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71`; snapshot 69,145 bytes, SHA256 `8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d`; **snapshot quote=True; snapshot `preToolUse`=True; snapshot `sessionStart`=True**. The fresh frozen `run_curl` fetch returned HTTP 200, URL `https://cursor.com/docs/hooks`, 69,145 bytes, same SHA256; **live quote=True; live `preToolUse`=True; live `sessionStart`=True**. Both `page_why` checks returned `[]`; word count was 24. These are quote/event checks, not a full C1 run or a predicate result.

## Drafts for integration

SOURCES row (S089-S095 column order; full snapshot digest):

```text
| S101 | Cursor Docs — Hooks — https://cursor.com/docs/hooks | docs | A | Cursor's project hook-config path, hook events, and execution scopes (vendor documentation; not runtime behavior) | Project cloud-agent hooks (`hooks:50`); `preToolUse` (`:860-862`), `postToolUse` (`:897-899`), `sessionStart` (`:1338-1340`), `sessionEnd` (`:1372`); user-level config unavailable to cloud agents (`:102`); fetched 2026-10-23T09:35:23Z, HTTP 200, 69,145 B, sha256 `8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d` (seat SrcCursor) | Cursor documents `.cursor/hooks.json` for project cloud-agent hooks; user-level hooks are unavailable to cloud agents, and the page defines hook lifecycle events | mined | 2026-10-23 | 90d | corpus/knowledge/hook-files-round59.md, corpus/lessons/round-59.md |
```

Counter-compliant entry row (exact config token; scope note is adjacent rather than in the checked cell):

```text
| Cursor | `.cursor/hooks.json` | S101 | If you have hooks defined in `.cursor/hooks.json` at the root of your project, cloud agents pick them up and run them during their work. |
```

Scope note: project cloud-agent hook configuration (line 50); user-level `~/.cursor/hooks.json` is unavailable to cloud agents (line 102).

Requested expanded entry form, **rejected by frozen E4** because its config cell is not exactly the token after backtick removal:

```text
| Cursor | `.cursor/hooks.json` (project cloud agents) | S101 | If you have hooks defined in `.cursor/hooks.json` at the root of your project, cloud agents pick them up and run them during their work. |
```

SKILL row draft (four real event names; compact scope note and action):

```text
| Cursor | `.cursor/hooks.json` (project cloud hooks; scripts are in `.cursor/hooks/` (127, 157); user `~/.cursor/hooks.json` unavailable to cloud agents (102)) | `preToolUse` (860), `sessionStart` (1338); also `postToolUse` (897), `sessionEnd` (1372); no preview/experimental marker | Move always-on rules from prompts to hooks; review event scope first. |
```

Lesson `## Gate` line draft:

```text
- S101 — https://cursor.com/docs/hooks; fetched 2026-10-23T09:35:23Z, HTTP 200, 69,145 B, sha256 `8436af76…`; `.ufo/waves/round-59/snapshots/S101.page:50`: "If you have hooks defined in `.cursor/hooks.json` at the root of your project, cloud agents pick them up and run them during their work."
```

## Touched surfaces, gates, and limits

- Wrote the exact successful fetch body only to `.ufo/waves/round-59/snapshots/S101.page`; wrote this report to `.ufo/waves/round-59/build/SrcCursor.md`. No product file, SOURCES row, knowledge entry, lesson, SKILL section, or counter was edited. No package/tool was installed or updated.
- Source gates observed: pinned host `cursor.com` per counter spec; `/docs/hooks` HTTP 200; full digest is available; quote is 24 words with no stripped bytes; `hook` appears outside the token; two preferred events are printed and have documented triggers; snapshot and fresh-fetch quote/events checks are all true. The `.md` route gave HTTP 404, so it is not used.
- Out of scope: integrating these drafts, checking the full table/entry/SOURCES/Gate judge or running `python3 -B verifiers/check_hook_files.py --rev ... --fetch`; this report makes no claim that S101 is backed by a committed snapshot or that the C1 predicate passes. Only the required snapshot file is currently saved in the lane working tree.

Report: .ufo/waves/round-59/build/SrcCursor.md
