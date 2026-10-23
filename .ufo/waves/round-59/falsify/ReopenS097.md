Result: HOLDS — S097 row, snapshot and quote survive re-opening: live fetch at 2026-10-23T09:52:34Z is byte-identical to the committed snapshot and matches the row's sha256, and every anchor line supports the teaches cell.

Seat `ReopenS097` (leaf, round-59 falsify). Attacks: (1) the SOURCES row S097, (2) the committed snapshot, (3) the quote (entry and Gate). Locale: lane read-only; all counter executions in sandbox clone `/fast/scratch/hyaku/kotoba-r59/ReopenS097/lane` at `c63ccc6823e1f6a8577acbb43d19551eadbbee9a`. No tools installed (git/curl/python3 preinstalled; no pacman/uv/npm transactions).

## 1. Row (corpus/SOURCES.md:109 at c63ccc)

Row: `| S097 | OpenAI Learn — Hooks — https://learn.chatgpt.com/docs/hooks.md | docs | A | ... |` — cells: desc (4) "Codex hook configuration locations, lifecycle events, and trust review (vendor documentation, not a runtime test)"; anchor+fetch (5) "§ Hooks run at different points in a conversation (`hooks.md:21-28`); § Where Codex looks for hooks (`:30-60`); § Review and trust hooks (`:62-74`); fetched 2026-10-23T09:35:05Z (HTTP 200, 47,133 B, sha256 `57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92`)"; teaches (6) "Codex documents a user hook file and lifecycle events; non-managed hook definitions must be reviewed and trusted before they run"; status mined, opened 2026-10-23, 90d, used-by `corpus/knowledge/hook-files-round59.md`.

Fetch record (ordinary curl -sSL, browser UA, no headless browser):
- `date -u` → `Fri 23 Oct 2026 09:52:34 AM UTC`
- `curl -sSL -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36" -o S097.live -w "HTTP %{http_code} | bytes %{size_download} | url %{url_effective}\n" https://learn.chatgpt.com/docs/hooks.md` → `HTTP 200 | bytes 47133 | url https://learn.chatgpt.com/docs/hooks.md` (no redirect; effective URL unchanged)
- `sha256sum S097.live` → `57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92` — equals the row's declared sha256 exactly.

Anchor lines in the fetched page (1-based, raw markdown bytes) and what they say:
- `hooks.md:21-28` — heading "Hooks run at different points in a conversation:" and the When/Hooks table: During a turn (PreToolUse, PermissionRequest, PostToolUse, PreCompact, PostCompact, UserPromptSubmit, SubagentStop, Stop), interrupt (Interrupt), session/subagent start (SessionStart, SubagentStart), main thread ends (SessionEnd). Supports the teaches' "lifecycle events".
- `hooks.md:30-60` — heading "Where Codex looks for hooks": Codex discovers hooks next to active config layers as `hooks.json` or inline `[hooks]` tables (34-35); four most useful locations include `~/.codex/hooks.json` (44) and `<repo>/.codex/hooks.json` (46); plugin-bundled hooks (54-56); project-local hooks load only when the project `.codex/` layer is trusted and user/system hooks load from their own layers in untrusted projects (58-60). Supports the teaches' "a user hook file" (user path listed first; user/system terminology at 59).
- `hooks.md:62-74` — heading "Review and trust hooks": Codex lists configured hooks before deciding which can run; a non-managed hook requires review and trust of the exact hook definition, keyed to the hook's current hash (64-67); `/hooks` CLI (69-71); managed hooks from system/MDM/cloud/`requirements.toml` are trusted by policy (73-74). Supports "non-managed hook definitions must be reviewed and trusted before they run"; line 19 restates the same gate: "Non-managed hooks must be reviewed and trusted before they run."

SKILL.md:128 cross-check: token `~/.codex/hooks.json` (user; repo layers and inline config.toml tables too, S097 :30-46); events `PreToolUse`, `SessionStart` (S097 :25, :27); action "Put the hook here; a non-managed hook runs only after it is reviewed and trusted (S097 :19)". All three citations verified at those exact lines of the fetched page (PreToolUse at 25, SessionStart at 27, the gate sentence at 19).

## 2. Snapshot (`.ufo/waves/round-59/snapshots/S097.page` at c63ccc)

- Blob `1b16bbbc9d8efe426b9b743d9b92c325f61dfc29` (git ls-tree -r c63ccc), 47,133 bytes.
- `git show c63ccc:.ufo/waves/round-59/snapshots/S097.page > S097.committed` then `cmp S097.live S097.committed` → identical (exit 0); `sha256sum S097.committed` → `57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92`. No drift between the row's 09:35:05Z fetch and my 09:52:34Z refetch.

## 3. Quote (entry == Gate)

- Entry quote cell, `corpus/knowledge/hook-files-round59.md:24`: `a default `hooks/hooks.json` file. See [Build plugins](https://developers.openai.com/plugins/build/plugins#bundled-mcp-servers-and-lifecycle-hooks) for the plugin packaging rules. In practice, the four most useful locations are: - `~/.codex/hooks.json``
- Gate admitted quote, `corpus/lessons/round-59.md:11`: byte-identical string (asserted equal in script).
- Reconstruction from source lines 38-44 (blank lines dropped, folded to single spaces; link and list marker kept, per the shaping note at knowledge-file line 62): fold = `manifest or a default ... are: - `~/.codex/hooks.json``; the quote cell equals the fold starting at "a default" (mid-line 38) and ending at `~/.codex/hooks.json` (line 44) — consistent with the documented shaping.
- Page checks (mirroring the frozen counter's normalisation): `norm(quote) in norm_page(page)` → True; token `~/.codex/hooks.json` found at boundary (index 1952 in the plain page text) → True; quote length 22 words (E6 range 6-25) → True; events `PreToolUse` (line 25) and `SessionStart` (line 27) at identifier boundaries → True.

## Counter runs (sandbox clone at c63ccc)

- `timeout 900 python3 -B verifiers/check_hook_files.py --rev c63ccc6823e1f6a8577acbb43d19551eadbbee9a` → `hook files backed on committed snapshots 6 of 6; live not run; new ground 0`; `counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71`; exit 1 (only rejection: opencode, which is outside the 6-client claim).
- `timeout 900 python3 -B verifiers/check_hook_files.py --rev c63ccc6823e1f6a8577acbb43d19551eadbbee9a --fetch` → `hook files backed on committed snapshots 6 of 6; found on the live page 6 of 6; new ground 6`; exit 0. Reproduces the L1 receipt `.ufo/waves/round-59/C1-measure.txt` exactly.

## Findings

No actionable defect in scope. The row (URL, sha256, byte count, kind/tier/status, teaches), the snapshot (byte-identical to the live page at refetch), and the quote (entry == Gate, verbatim on page, token/events at boundaries) all hold.

## Residual risk / verification gaps

- The teaches cell's word "user" for `~/.codex/hooks.json` is an inference: the page lists the path first among "the four most useful locations" (line 44) and separately speaks of "user and system hooks" (lines 59-60); the page never literally labels that path "user". Low severity; SKILL.md:128 already glosses it "(user;...)". [INFERENCE] for the label, not for the path.
- Drift after 2026-10-23T09:52:34Z is unobserved; the committed snapshot remains the frozen artifact.
- No bot challenges or access controls were encountered; no headless browser used.
