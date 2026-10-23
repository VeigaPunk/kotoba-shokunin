Result: HOLDS — S101 (Cursor) row, snapshot, and quote all verified against a live re-fetch; the committed snapshot is byte-identical to today's page under the documented header set, and every row-cited anchor line says what the `teaches` cell claims.

## Attack surface and method

Assigned item: S101 row in `corpus/SOURCES.md` at `c63ccc6823e1f6a8577acbb43d19551eadbbee9a` (URL `https://cursor.com/docs/hooks`, fetched 2026-10-23T09:35:23Z, HTTP 200, 69,145 B, sha256 `8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d`, seat SrcCursor); snapshot `.ufo/waves/round-59/snapshots/S101.page`; entry quote (hook-files-round59.md table row, line 28) and lesson Gate quote (`corpus/lessons/round-59.md:15`). Review only; no lane file edited. Scratch: `/fast/scratch/hyaku/kotoba-r59/ReopenS101`. No tool installed/updated (nothing needed).

## Live re-fetch (provenance)

Command (ordinary curl, browser UA, the seat's documented `Accept` set from `.ufo/waves/round-59/build/SrcCursor.md`):

```
cd /fast/scratch/hyaku/kotoba-r59/ReopenS101 && date -u && timeout 60 curl -sSL \
  -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' \
  -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' \
  -o S101.live -w 'HTTP_STATUS=%{http_code}\nSIZE_DOWNLOAD=%{size_download}\nURL_EFFECTIVE=%{url_effective}\n' \
  'https://cursor.com/docs/hooks'; echo curl_exit=$?; wc -c S101.live; sha256sum S101.live
```

Observed (exit 0): `Fri 23 Oct 2026 09:52:58 AM UTC`; `HTTP_STATUS=200`; `SIZE_DOWNLOAD=69145`; `URL_EFFECTIVE=https://cursor.com/docs/hooks`; `69145 S101.live`; sha256 `8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d`.

## Findings (all HOLDS)

1. **Snapshot == live page.** Extracted the committed blob (`git --no-optional-locks show c63ccc6823e1f6a8577acbb43d19551eadbbee9a:.ufo/waves/round-59/snapshots/S101.page > S101.snapshot`): 69,145 B, sha256 `8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d`. `cmp S101.snapshot S101.live` → exit 0, no output (identical). The page has not drifted since the 09:35Z capture.
2. **Row sha256/bytes match.** Row claims 69,145 B / `8436af76…`; snapshot and live fetch both reproduce exactly. URL effective ( no redirects; HTTP 200.
3. **Gate/entry quote at `hooks:50`.** Line 50 (verbatim):
   `Cloud agents run command-based hooks from your repository. If you have hooks defined in `.cursor/hooks.json` at the root of your project, cloud agents pick them up and run them during their work.`
   The quoted sentence matches the lesson Gate (`round-59.md:15`) and the entry table row byte-for-byte, 24 words, backticks retained, no bytes stripped (line is 32 words; the quote is the sentence starting at "If you have hooks…"). Word count check: `awk 'NR==50' S101.live | wc -w` → 32; `wc -w` on the quoted sentence → 24.
4. **Every SOURCES-row anchor line says what `teaches` claims.** `teaches`: "Cursor documents `.cursor/hooks.json` for project cloud-agent hooks; user-level hooks are unavailable to cloud agents, and the page defines hook lifecycle events."
   - `hooks:50` — project `.cursor/hooks.json` picked up and run by cloud agents: confirmed (also `:98` "Project hooks (`.cursor/hooks.json` in your repo): Loaded and run during cloud agent work").
   - `hooks:102` — "User-level hooks (`~/.cursor/hooks.json`) are not available in cloud agents. Cloud agent VMs don't have access to your local home directory configuration." Confirms the "unavailable to cloud agents" clause.
   - `hooks:860-862` — `#### preToolUse` at 860; definition at 861 ("Called before any tool execution. This is a generic hook that fires for all tool types…").
   - `hooks:897-899` — `#### postToolUse` at 897; definition at 898 ("Called after successful tool execution. Useful for auditing, analytics, and injecting context.").
   - `hooks:1338-1340` — `#### sessionStart` at 1338; definition at 1340 ("Called when a new composer conversation is created…").
   - `hooks:1372` — `#### sessionEnd` at 1372; definition at 1373 ("Called when a composer conversation ends…").
   Page defines the hook lifecycle events as claimed (also `sessionEnd`/`preCompact`/`workspaceOpen` etc. in the same section).
5. **Entry-file side cites also check out.** `hook-files-round59.md:50-52` cites events at `:27` (line 27 lists `preToolUse` / `postToolUse` / `postToolUseFailure` as generic tool-use hooks) and `:67` (`| postToolUse | Yes |` in the cloud-agent-run table), `sessionStart` deferred for cloud agents at `:88` (table row: "Deferred while cloud agents can still start in a read-only environment…"), and user-level unavailability at `:102` — all confirmed on the live page.

## Residual notes (no break)

- **Content negotiation.** Same URL with browser UA only (curl default `Accept: */*`) returns HTML — 1,307,361 B, sha256 `380c5a72c14ca5d72cfbc91f90bf7d285c2d2f1652588c4aa7dfcfe5dcdc8bd3`, still HTTP 200. The markdown form (the snapshot) depends on the `Accept: text/markdown…` header set, which the build report `SrcCursor.md` documents verbatim, and the lesson already records UA/header sensitivity (M81 note, `round-59.md:45`). Not a falsification of the row/snapshot.
- Entry reader: the project-script path `Create your hook script at <project>/.cursor/hooks/format.sh` sits at line 156, not 157 (line 157 is the following ```bash fence); the SOURCES row does not cite 157, so no row defect — flagging only so the SKILL-row drafts that cite `(127, 157)` get a last-mile look before integration.
- No paid model calls; no bot challenges encountered; ordinary curl only.

## Verification gaps

None within scope. The C1 counter run itself (`check_hook_files.py --rev … --fetch`), the SKILL.md section, and the other rows (S096–S100, S102) are other seats' items.

Report: .ufo/waves/round-59/falsify/ReopenS101.md
