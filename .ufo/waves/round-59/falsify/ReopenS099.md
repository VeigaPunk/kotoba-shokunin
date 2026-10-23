Result: HOLDS — S099’s row, committed snapshot, and entry/Gate quote survive reopening; all cited anchors support the row’s teaching claims.

## Evidence

- The S099 registry row at `corpus/SOURCES.md:111` (at `c63ccc6823e1f6a8577acbb43d19551eadbbee9a`) gives `https://docs.github.com/en/copilot/concepts/customizations/hooks.md`, anchors `hooks.md:21-28` and `:32-43`, and SHA-256 `23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4`.
- Reopened with `curl -sSL -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'`: `date -u` → `Fri 23 Oct 2026 09:52:37 AM UTC`; HTTP 200; 8,428 bytes; SHA-256 `23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4`.
- Fetched bytes compared with `.ufo/waves/round-59/snapshots/S099.page`: `cmp` exit 0. I also extracted the committed blob at `c63ccc6823e1f6a8577acbb43d19551eadbbee9a:.ufo/waves/round-59/snapshots/S099.page` into my scratch directory and compared it with the fetch: `cmp` exit 0; committed-blob SHA-256 is `23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4`, equal to the SOURCES row hash. The snapshot’s line 28 exactly reads: “For Copilot CLI and Copilot cloud agent, you can define repository hooks in `.github/hooks/*.json`. Copilot CLI also supports personal hooks in `~/.copilot/hooks/*.json`. For execution environments, additional locations, and event support, see [GitHub Copilot hooks reference](/en/copilot/reference/hooks-reference).” This contains the entry quote recorded in `corpus/knowledge/hook-files-round59.md:26` and the Gate quote in `corpus/lessons/round-59.md:13`; both quote the personal-hook sentence accurately.
- The cited `hooks.md:21-28` distinguishes the CLI from the app, cloud agent, and VS Code, warns not to assume events/input/output transfer unchanged across surfaces (line 26), and states the repository and CLI-personal hook locations (line 28). The cited `hooks.md:32-43` identifies these as example CLI hook events and says cloud agent supports a subset (line 32), names `sessionStart` (line 34) and `preToolUse` (line 37), and points to the cloud-agent availability reference (line 43). These anchors support the S099 `teaches` cell without claiming runtime behavior.

## Findings (by severity)

- None.

## Residual risk

- This re-open verifies the cited source bytes, not hook runtime behavior; the knowledge entry explicitly leaves runtime behavior unheld.

## Verification gaps

- None within this assignment’s source/row/snapshot/quote checks; no runtime test was requested or performed.

No tool was installed or updated.