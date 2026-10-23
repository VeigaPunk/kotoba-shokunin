Result: DONE — no sibling lane's corpus states a fact about a client's scoped rule folder or scope key that contradicts the round-60 census; census stands (Claude Code, VS Code, Copilot CLI, Cursor eligible; Codex, Gemini CLI, opencode not eligible).

# Sibling-lane contradiction scan — C1 scoped rule files by client

Scan date (UTC): 2026-10-23 (this seat). Lane root: `/home/vgpnk/Projects/shokunin`. Scope: every `/home/vgpnk/Projects/shokunin/*-shokunin` except `kotoba-shokunin` (20 lanes), read-only, no lane content written. Commits (lane HEAD, read-only `git rev-parse HEAD`) are recorded per lane below.

## Census under test (frozen, erratum E1)
Eligible: Claude Code (`.claude/rules/`, `paths`), VS Code (`.github/instructions/**/*.instructions.md`, `applyTo`), Copilot CLI (same token, `applyTo`), Cursor (`.cursor/rules`, `globs`). Not eligible: Codex (nested `AGENTS.md`/`AGENTS.override.md` by directory), Gemini CLI (directory-scoped `GEMINI.md`), opencode (nested `AGENTS.md` by directory; `instructions` adds files, does not scope).

## Method
For each sibling lane I searched its `SKILL.md`, `PROVINCE.md` and `corpus/` (excluding `.git/`, `.ufo/`, `live/`, `mut/`, vendored fixtures) for the scoped-rule surface tokens named in the census and in the task: `applyTo`, `globs`, `paths` as a frontmatter key, `.cursor/rules`, `.claude/rules`, `.github/instructions`, plus the broader phrases "scoped rule", "rule files by client", and each client name combined with "rule"/"instruction"/"scope". Incidental hits (e.g. Python `paths` variables, `dead-globs`, game audio "backend-scoped rule", cannon-es `applyTorque`) were excluded; none is a statement about a client's scoped rule folder or scope key. I also read the prior sibling-overlap scan `w0/ConnSiblingScoped.md`, which reached the same "no lane owns the surface (FITS)" conclusion and recorded the same commit hashes for the lanes it covered.

## Findings
None. No sibling lane's corpus states a fact about any client's scoped rule folder or scope key. In particular, no sibling contradicts the census's eligibility split or the recorded scope keys (`paths` for Claude Code, `applyTo` for VS Code/Copilot CLI, `globs` for Cursor) or the "not eligible" classification of Codex, Gemini CLI and opencode.

## Per-lane verdict
| lane | commit | verdict | evidence |
|---|---|---|---|
| audio | `7a2fcd4f08831154686e4e323031f41fffdb077f` | no scoped-rule fact | grep of `corpus/` for the census tokens returned only `paths` as Python iteration variables and audio-path prose |
| chousa | `f20aeaa7980cb3a94c6b483c10e6dac1fb2b0989` | no scoped-rule fact | hits are research-gate `paths`/`globs` terminology, not client rule folders |
| game-dev-2d | `7753d49b16674e122ed134403e7a9b301f2cbf7e` | no scoped-rule fact | only game-engine "Cursor" symbol and binary strings |
| game-dev-3d | `89dd182b70943a20ae9aa6c1ed0e3c9b6e79c080` | no scoped-rule fact | `.claude/skills/` appears only as Claude Code harness-skill location, not a scoped rule folder |
| kagi | `899c50b42634a3a4ad0b28ab7509786315e2fc2b` | no scoped-rule fact | only opencode config adjacency; no client scoped-rule folder |
| kaidoku | `f432c8e3bc58934887c83f1db2b26f9910a9d87f` | no scoped-rule fact | Codex mention is about MCP approvals, not scoped rules |
| kake | `b061585ac68ac7f1cba7c4789f8de7f7ec5550fd` | no scoped-rule fact | no scoped-rule-folder statement |
| kama | `513eba3ba51a142c9936553e3a85918345eb5c4c` | no scoped-rule fact | no scoped-rule-folder statement |
| kasegi | `1fafde8f11454f3b0b98ab7f2b2e640aaf7f399a` | no scoped-rule fact | `dead-globs` only |
| kengaku | `1f3b0f1ec41ec297130e8944ff97968d32324632` | no scoped-rule fact | client names occur only in provider/model context |
| kotodama | `25b44b8a24c37f31c50021c785cd3abb6196b071` | no scoped-rule fact | no client scoped-rule folder statement |
| kumitate | `fe3d45bf929246915c8c0de5f7f8682b5015b22c` | no scoped-rule fact | no scoped-rule-folder statement |
| lore | `380ef3abc7c7af11d7f23e9f9c82bb1937e1f695` | no scoped-rule fact | no scoped-rule-folder statement |
| mado | `8e72db74e6d0f9af9b290b407d9a3787683d09a2` | no scoped-rule fact | no scoped-rule-folder statement |
| mori | `5842dc045bb3d3b7aa2bdaaf462dcff536358444` | no scoped-rule fact | no scoped-rule-folder statement |
| revenger | `876630dbb4d630e016d7d8c32a19ea04c646cbae` | no scoped-rule fact | no scoped-rule-folder statement |
| souji | `4edb25dfe262515d0da63224bbba71e02e36cba5` | no scoped-rule fact | no scoped-rule-folder statement |
| tabi | `e3cf4e0d30bb835532ff44b118c5ad52e09eb76d` | no scoped-rule fact | no scoped-rule-folder statement |
| tameshi | `24a5a5bb598ae919546715267d76f814efaf8912` | no scoped-rule fact | no scoped-rule-folder statement |
| tsukuroi | `199beb97d0c30507d732a0ebb4dba69adb973596` | no scoped-rule fact | no scoped-rule-folder statement |

## Conclusion
No contradiction found. The census's eligibility and scope-key assignments are not challenged by any sibling lane's corpus. Adjacent lanes defer the instruction surface to kotoba (per `w0/ConnSiblingScoped.md`), and none documents a competing scoped-rule folder or scope key.

Report: .ufo/waves/round-60/build/ConnSiblingContradict.md