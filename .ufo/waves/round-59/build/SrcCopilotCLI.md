Result: DONE — Copilot CLI S099 bytes were reopened and the frozen counter’s quote and event checks returned True on both the snapshot and a fresh live fetch.

## Axes and findings

- **Depth:** `~/.copilot/hooks/*.json` is specifically personal Copilot CLI configuration; `.github/hooks/*.json` is the repository-level location (snapshot lines 26–28). The page warns not to assume the same event/input/output support across surfaces (line 26).
- **Quote (Q42):** 8 words, unshaped, no bytes stripped: `Copilot CLI also supports personal hooks in `~/.copilot/hooks/*.json`.` It is on snapshot line 28; `hooks` is outside the token.
- **Events:** `sessionStart` (line 34) and `preToolUse` (line 37), both printed as Copilot CLI hook-event examples under line 32. Other events are `sessionEnd` (35), `userPromptSubmitted` (36), `postToolUse` (38), `agentStop` (39), `subagentStop` (40), and `errorOccurred` (41). Only Visual Studio Code is explicitly labeled public preview (line 24); the page does not label Copilot CLI preview/experimental.
- **Fetch provenance:** `date -u` printed `Fri Oct 23 09:34:55 AM UTC 2026`; HTTP 200; 8,428 bytes; sha256 `23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4`. The saved bytes match the census fetch at `.ufo/waves/round-59/w0/CensusCopilotCLI.md:13`.

## Draft SOURCES row (column order S089–S095)

```markdown
| S099 | GitHub Docs — Hooks for GitHub Copilot — https://docs.github.com/en/copilot/concepts/customizations/hooks.md | docs | A | Copilot CLI hook-file locations and documented events; distinguish CLI from cloud-agent and VS Code scope | § Where you can use hooks (`hooks.md:21-28`); § Types of hooks (`:32-43`); fetched 2026-10-23T09:34:55Z (HTTP 200, 8,428 B, sha256 `23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4`) | Copilot CLI documents repository hooks at `.github/hooks/*.json` and personal hooks at `~/.copilot/hooks/*.json`; `sessionStart` and `preToolUse` are named hook events, with a warning not to assume event support across surfaces | mined | 2026-10-23 | 90d | corpus/knowledge/hook-files-round59.md |
```

`mined` and `used-by` above are draft values for the paired entry; neither row has been integrated into lane corpus files by this seat.

## Draft entry and SKILL rows

```markdown
| Copilot CLI | `~/.copilot/hooks/*.json` (personal scope) | S099 | Copilot CLI also supports personal hooks in `~/.copilot/hooks/*.json`. |
```

```markdown
| Copilot CLI | `~/.copilot/hooks/*.json` (personal; repo hooks also at `.github/hooks/*.json`, hooks.md:28) | `sessionStart`, `preToolUse` (also `sessionEnd`, `userPromptSubmitted`, `postToolUse`, `agentStop`, `subagentStop`, `errorOccurred`; lines 34–41; only VS Code is labeled public preview, line 24) | Move reusable hook guidance here; review path scope first |
```

## Draft `## Gate` line

```markdown
- S099 — https://docs.github.com/en/copilot/concepts/customizations/hooks.md; opened 2026-10-23T09:34:55Z (date -u: Fri Oct 23 09:34:55 AM UTC 2026); HTTP 200; 8,428 B; sha256 prefix `23370e092d2e`; `.ufo/waves/round-59/snapshots/S099.page:28`: "Copilot CLI also supports personal hooks in `~/.copilot/hooks/*.json`."
```

## Counter acceptance evidence

The freeze clone was made at `/fast/scratch/hyaku/kotoba-r59/SrcCopilotCLI` and checked out at `67b68e0f9a0c48e5aa5ced63e6117cfca69da491`; clone/checkout command exited 0 with no output. The imported counter reports sha256 `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71`. `quote_why` and `event_on_page` are the counter’s quote/event checks (`verifiers/check_hook_files.py:1022-1055`); `run_curl` is its curl fetcher (`:1058-1082`).

Direct source-save command (exit 0):

```text
timeout 120 bash -c 'mkdir -p /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/snapshots && date -u && curl -sSL --max-time 30 -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -H "Accept: text/markdown, text/plain;q=0.9, */*;q=0.8" -o /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/snapshots/S099.page -w "%{http_code} %{url_effective} %{size_download}\n" https://docs.github.com/en/copilot/concepts/customizations/hooks.md && sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/snapshots/S099.page'
Fri Oct 23 09:34:55 AM UTC 2026
200 https://docs.github.com/en/copilot/concepts/customizations/hooks.md 8428
23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4  /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/snapshots/S099.page
```

Sandbox command, run from `/fast/scratch/hyaku/kotoba-r59/SrcCopilotCLI` (exit 0):

```text
timeout 120 python3 -B -c 'import importlib.util; from pathlib import Path; p=Path("verifiers/check_hook_files.py"); spec=importlib.util.spec_from_file_location("check_hook_files", p); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); url="https://docs.github.com/en/copilot/concepts/customizations/hooks.md"; quote="Copilot CLI also supports personal hooks in `~/.copilot/hooks/*.json`."; token="~/.copilot/hooks/*.json"; events=("sessionStart", "preToolUse"); snapshot=Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/snapshots/S099.page").read_bytes().decode("utf-8", errors="replace"); status, effective, live_bytes=m.run_curl(url); live=live_bytes.decode("utf-8", errors="replace"); print(f"counter sha256={m.self_sha()}"); print(f"live fetch status={status} effective={effective} bytes={len(live_bytes)}"); print(f"snapshot quote={not m.quote_why(snapshot, quote, token)}"); print(f"snapshot event sessionStart={m.event_on_page(snapshot, events[0])}"); print(f"snapshot event preToolUse={m.event_on_page(snapshot, events[1])}"); print(f"snapshot events={all(m.event_on_page(snapshot, e) for e in events)}"); print(f"live quote={not m.quote_why(live, quote, token)}"); print(f"live event sessionStart={m.event_on_page(live, events[0])}"); print(f"live event preToolUse={m.event_on_page(live, events[1])}"); print(f"live events={all(m.event_on_page(live, e) for e in events)}")'
counter sha256=f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71
live fetch status=200 effective=https://docs.github.com/en/copilot/concepts/customizations/hooks.md bytes=8428
snapshot quote=True
snapshot event sessionStart=True
snapshot event preToolUse=True
snapshot events=True
live quote=True
live event sessionStart=True
live event preToolUse=True
live events=True
```

Two invocation/path errors were corrected, not counter failures: the first curl could not save because the snapshots directory did not exist (curl exit 23; HTTP 200 but 0 bytes written), then the successful command above created the requested directory and saved the page. The first sandbox check looked for the uncommitted S099 snapshot under the freeze clone and exited 1 with `FileNotFoundError`; the successful check above read the saved snapshot by its lane path and fetched the live page through `m.run_curl`.

## Touched surfaces, limits, and scope

- Lane files written: `.ufo/waves/round-59/snapshots/S099.page` (exact fetched bytes) and this report only. The SOURCES, knowledge entry, SKILL, and lesson rows above are drafts; no corpus/SKILL files were edited.
- Sandbox: clone at the assigned freeze in `/fast/scratch/hyaku/kotoba-r59/SrcCopilotCLI`; no sandbox commit or counter modification. No tool installed or updated.
- The helper quote/event checks passed for snapshot and fresh live bytes. The full round C1 `check_hook_files.py --rev ... --fetch` predicate, integration, and hook runtime behavior were not tested by this item. No canonical judge, commit, push, or deploy was run.

Report: .ufo/waves/round-59/build/SrcCopilotCLI.md
