Result: HOLDS — all seven hunks are OC-4/OC-6 rule documentation/logic or self-test arms, including the two attributed round-52 repair arms; the pin script is unchanged.

## Hunk classification

| Hunk | Final `verify_surfaces.py` lines | Classification | Evidence |
|---|---:|---|---|
| 1 | 572–576 | OC-4/OC-6 comment | Updates the carried-limit note: OC-4 now binds export, call, and result; OC-6 binds its layer dependency. The same comment explicitly retains prior OC-1..OC-3/OC-5 limitations; this is comment-only. |
| 2 | 622–755 | OC-4/OC-6 constants, conditions, and comments | Adds OC-6 key/layer/observe/walk patterns and `opencode_context_layer_matches`; adds OC-4 entry/call patterns and `opencode_read_hook_matches`. |
| 3 | 805–810 | OC-4 condition/comment | Replaces the OC-4 literal-presence predicate with `opencode_read_hook_matches(dump)` and updates its explanatory anchors. |
| 4 | 821–825 | OC-6 condition/comment | Replaces the OC-6 all-literals predicate with `opencode_context_layer_matches(dump)` and updates its explanatory anchors. |
| 5 | 1428–1441 | Round-52-fix arm (aeed0890) | Adds the unresolved-group-admission self-test, checking that the unresolved class is surfaced. |
| 6 | 1575–1587 | Round-52-fix arm (aeed0890) | Adds the empty-baseline fallback self-test, checking that extracted omp classes remain visible. |
| 7 | 1611–1634 | Self-test arm/fixture (C1) | Tests the 1.19.4 anchor fixture and literal-preserving OC-4/OC-6 decoys. |

No hunk is OTHER. The changed hunks do not enter loader implementations, `check_opencode_extract`, substrate identity/reporting, `main`, or JSON emission. The OC rule helpers are used by `extract_opencode_classes`; its caller and the downstream check/reporting paths are outside the changed ranges.

## Evidence

- `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin diff 3bb0a7a33e6eb585a83a1a55dee30b26079b1e36 6dd311644f987cef62a40f0c028ea2be2fc6ff67 -- verifiers/verify_surfaces.py verifiers/check_substrate_pins.py` — exit 0; seven `verify_surfaces.py` hunks at old/new starts `569/569`, `619/619`, `689/802`, `704/818`, `1310/1424`, `1442/1572`, `1464/1608`; no `check_substrate_pins.py` diff.
- `git diff --stat` for that range and those paths — exit 0; output: `verifiers/verify_surfaces.py | 227 ...`; `1 file changed, 198 insertions(+), 29 deletions(-)`.
- `git diff --exit-code 3bb0a7a33e6eb585a83a1a55dee30b26079b1e36 6dd311644f987cef62a40f0c028ea2be2fc6ff67 -- verifiers/check_substrate_pins.py` — exit 0; no diff (`PIN_DIFF_EXIT=0`).
- `git log --format='%h %s' 3bb0a7a33e6eb585a83a1a55dee30b26079b1e36..6dd311644f987cef62a40f0c028ea2be2fc6ff67 -- verifiers/verify_surfaces.py verifiers/check_substrate_pins.py` — output names `6dd3116` C1 and `aeed089` routed repairs. `git show aeed0890efb7cb62ef1364ce7d7ba5566ef3fed6 -- verifiers/verify_surfaces.py` shows exactly two hunks (`@@ -1310,6 +1310,22` and `@@ -1442,6 +1458,20`), corresponding to rows 5 and 6.
- Final source evidence: `verifiers/verify_surfaces.py:673-755` contains the two OC matchers; `:805-825` applies them; `:1054-1088` is `check_opencode_extract`; `:1740-1815` contains substrate reporting/JSON/main code, outside changed hunks.

## Residual risk and verification gaps

- The LSP device is unavailable: `read xd://lsp` returned `No such tool: xd://lsp` (mounted devices listed: `ast_edit`, `debug`). No LSP status, references, definition, or diagnostics could be requested. Function and hunk mapping above comes from the diff and source text; it is not claimed as LSP semantic proof.
- No tests or runtime checks were run; this report is limited to guard (a)'s diff-scope classification.