NEGATIVE SWEEP — S249-class surfaces for the SDK `allowedTools` channel
Seat: Kb81R01NegSweep | Round 81 w1 | opened 2026-10-27 (UTC; 2026-10-28 02:34Z at write-up)
Question: which OTHER surfaces document the SDK `allowedTools` / `allowed_tools` grant
channel — the query-config pre-approve list distinct from SKILL.md `allowed-tools`
frontmatter — beyond the S249 anchor `code.claude.com/docs/en/agent-sdk/skills.md`?

Method
- Enumerated the SDK doc tree from https://code.claude.com/docs/llms.txt
  (200, 63,686 B, sha256 f9a44a89…; the index itself has 0 hits of the token).
- Fetched all 31 `agent-sdk/*.md` doc pages plus `skills.md` (S227's page, control),
  `agent-sdk/skills.md` (S249 page, control), the platform.claude.com mirror in both
  routes, both GitHub package READMEs, and the npm registry document — 39 fetched
  objects, every one HTTP 200.
- Swept raw bytes for `allowed[-_]?[Tt]ools` (catches camelCase `allowedTools`,
  snake `allowed_tools`, frontmatter `allowed-tools`). A page with hits was read at
  every hit for whether its own text documents the channel (semantic statement) or
  merely uses it (code example / link target / contrast sentence). Q62 rule kept:
  every zero-hit claim cites the grep over named bytes.
- Fetch records: `.ufo/waves/round-81/build/Kb81R01NegSweep-fetch/<file>.fetch.json`
  (url, http, bytes, sha256, token hits, redirect final-URL where applicable); the
  fetched bytes sit next to each record for byte-identical re-verification.
- Controls verified before sweeping: `agent-sdk-skills-s249ctrl.md` = 28,395 B,
  sha256 ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2 — byte-
  identical to the S249 pin in the plan and registry. `skills-s227.md` = 117,962 B,
  sha256 31623035b25ac7e6bebd8dec6234aa76e31018f0e2eb8b47da6b36cf015712f9 —
  byte-identical to S227's recorded fetch. The corpus predicate holds on both.

Named targets — answers

1. `allowedTools` query-option reference — TypeScript (`@anthropic-ai/claude-agent-sdk`)
   https://code.claude.com/docs/en/agent-sdk/typescript.md — 200, 327,318 B,
   sha256 b6a3c9c11a48e58cbadb6e1f9144b2f88ccbc0f252c35682836f8d7e5935d8f7. ADMIT.
   § `Options`, line 505, located quote (23 words): "Tools to auto-approve without
   prompting, apart from reads from network paths. This does not restrict Claude to
   only these tools." Plus the todo-tracking opt-in clause and `canUseTool` fall-through
   (same cell); `skills` option row states the Skill-tool auto-add (cf. S249).

2. `allowedTools` query-option reference — Python (`claude_agent_sdk`)
   https://code.claude.com/docs/en/agent-sdk/python.md — 200, 163,829 B,
   sha256 4977aa56160f8e04d636fea7806c42b3dc34981b79b0d66fa0d7c7eaaf398470. ADMIT.
   § `ClaudeAgentOptions`, line 875 — identical definition text to the TypeScript row
   (same sentence, `allowed_tools` spelling), so the channel's semantics are stated
   verbatim in both language references; the `skills` row repeats the Skill-tool
   auto-add. Also examples at L252, L656, L727.

3. skills.md § Pre-approve tools for a skill (S227's anchor, re-derived) —
   does it name the SDK path? NO. `skills-s227.md` carries 0 hits of `allowedTools`
   and 0 hits of `allowed_tools` (grep over the fetched 117,962 B) and § Pre-approve
   tools for a skill (L615) covers only the `allowed-tools` frontmatter: the per-turn
   grant, workspace-trust exemption, `strictPluginOnlyCustomization` hooks clause, and
   the `allowManagedPermissionRulesOnly` managed-settings lock. Its only prescriptive
   pointer for a session-wide grant is "add allow rules to those permission settings".
   SDK cross-references exist elsewhere on the page (L190 `additionalDirectories`,
   L699 first-skill-only under SDK/`-p`, L924 `skillOverrides` for SDK callers) but none
   at or inside the pre-approve section. The SDK-option document lives exclusively on
   the agent-sdk subtree — S227's anchor does NOT cover the S249 claim surface.

High-signal candidates — full sweep (31 agent-sdk pages + mirrors + package docs)

DEFINITIONAL — own text states the channel's semantics (verdict admit):
4. agent-sdk/permissions.md — 33,157 B, sha256 3397602f…. ADMIT.
   § Allow and deny rules (L83–87) + step-5 of the evaluation flow (L70):
   "`allowed_tools` and `disallowed_tools` (TypeScript: `allowedTools` /
   `disallowedTools`) add entries to the allow and deny rule lists in the evaluation
   flow above." Uniquely documents evaluation-order placement (hooks → deny → ask →
   mode → allow rules → canUseTool) and the CLAUDE_SDK_CAN_USE_TOOL_SHADOWED warning.
   Located quote (19 words): "Check `allow` rules (from `allowed_tools` and
   settings.json). If a rule matches, the tool is approved."
5. agent-sdk/agent-loop.md — 41,257 B, sha256 d98dad7e…. ADMIT.
   § Tool permissions, line 172, located quote (24 words): "`allowed_tools` /
   `allowedTools` auto-approves listed tools. A read-only agent with `["Read",
   "Glob", "Grep"]` in its allowed tools list runs those tools without prompting".
6. agent-sdk/configuration.md — 18,852 B, sha256 bc2e046b…. ADMIT.
   § Pass options to a session (L18, L65) + § Configure specific features table (L266:
   "`allowedTools` / `allowed_tools` | Which tool calls are pre-approved").
   Located quote (19 words): "`allowedTools` (TypeScript) or `allowed_tools` (Python)
   pre-approves the listed tools, so calls to them run without stopping for approval."
7. agent-sdk/claude-code-features.md — 20,799 B, sha256 853607de…. ADMIT.
   § Skills, line 128, located quote (16 words): "When `skills` is set, the SDK adds
   the Skill tool to `allowedTools` automatically." — the skills↔channel coupling rule
   on a page other than the S249 anchor; also § Choose the right feature (L288).
8. agent-sdk/custom-tools.md — 40,958 B, sha256 946948f5…. ADMIT.
   § Configure allowed tools (L374–380): availability-vs-permission two-layer split.
   Located quote (17 words): "`allowedTools` and scoped `disallowedTools` rules change
   permission" / table row "Listed tools run without a permission prompt. Other
   unlisted tools remain available". § Call a custom tool (L155) documents the
   `mcp__{server}__{tool}` naming convention inside the option.
9. anthropics/claude-agent-sdk-python README (GitHub) — code/docs, tier B.
   https://raw.githubusercontent.com/anthropics/claude-agent-sdk-python/main/README.md
   — 200, 13,250 B, sha256 c38a933bf8fef26316ea38635989b254e69a26d21d80b96bf5731cba4e88bcc6.
   main resolved to `2d485201617258867dd0f74b9e7307056f5938fe` (git ls-remote at fetch);
   re-fetch at that pinned revision returned byte-identical bytes (200, 13,250 B, same
   sha256) — revision-pinned verifiable. ADMIT.
   § Using Tools, line 59, located quote (24 words): "`allowed_tools` is a permission
   allowlist: listed tools are auto-approved, and unlisted tools fall through to
   `permission_mode` and `can_use_tool` for a decision." — same semantics stated in
   the package's own README (agent-client doc class named in the assignment).

USAGE ONLY — option appears in examples/links, page states no channel semantics
(verdict queued, evidence parked for future rows):
10. agent-sdk/quickstart.md — 15,053 B, sha256 d44e71ca…. 9 hits, all inside
    `ClaudeAgentOptions(...)`/options literals under § Customize your agent with
    inline comments "Auto-approve these tools"; no definitional sentence. QUEUED.
11. agent-sdk/subagents.md — 42,519 B, sha256 9db0458e…. 19 hits in example options;
    the `AgentDefinition` rows it documents are `tools`/`disallowedTools` (subagent
    tool sets), NOT the query option's semantics. QUEUED.
12. agent-sdk/sessions.md — 22,703 B, sha256 456f033e…. 7 hits, option literals in
    resume/fork examples only. QUEUED.
13. agent-sdk/streaming-vs-single-mode.md — 9,193 B, sha256 34ed5851…. 4 hits,
    option literals in mode examples only. QUEUED.
14. agent-sdk/mcp.md — 40,139 B, sha256 354ad14a…. 33 hits; § Allow MCP tools
    documents the wildcard use (`allowedTools: ["mcp__claude-code-docs__*"]`,
    `mcp__server__*` server-level patterns) and § Named servers (L166) the
    server-wait interaction — usage of the channel for MCP naming, semantics
    deferred to permissions.md. QUEUED.
15. agent-sdk/tool-search.md — 11,578 B, sha256 53192262…. 2 hits, wildcard example
    comments only. QUEUED.
16. agent-sdk/modifying-system-prompts.md — 36,198 B, sha256 cf93b231…. 2 hits,
    `allowedTools: ["Bash(git *)"]` in examples. QUEUED.
17. agent-sdk/user-input.md — 35,145 B, sha256 30115ac8…. 1 hit, inside the
    "callback never fires for auto-approved tools" WARNING — documents canUseTool
    precedence, mentions the option only to exclude it. QUEUED.
18. agent-sdk/todo-tracking.md — 19,097 B, sha256 2d25f3fe…. 2 hits: § Model
    availability (L31) names `allowedTools`/`allowed_tools` as one opt-in mechanism
    for the task-tracking tools — a link-through to permissions.md, not a channel
    definition. QUEUED.

ZERO-HIT — documents nothing about the channel (verdict reject; each sweep named):
19. agent-sdk/typescript-v2-preview.md — 12,462 B, sha256 85c0e2f7…. 0 hits
    (grep over fetched bytes). The removed-V2 page carries no allowedTools surface.
20. agent-sdk/plugins.md — 13,168 B, sha256 e7e675dd…. 0 hits.
21. agent-sdk/overview.md — 7,382 B, sha256 6bf994e5…. 0 hits.
22. agent-sdk/migration-guide.md — 7,093 B, sha256 68ba58d7…. 0 hits (the SDK rename
    documented here does not extend to the option).
23. agent-sdk/hosting.md — 24,489 B, sha256 6f8f7ce2…. 0 hits.
24. agent-sdk/troubleshooting.md — 13,727 B, sha256 75c8372f…. 0 hits.
25. agent-sdk/examples.md — 2,203 B, sha256 59fd222b…. 0 hits.
26. agent-sdk/session-storage.md — 23,662 B, sha256 b2a5ad49…. 0 hits.
27. agent-sdk/structured-outputs.md — 21,524 B, sha256 d85e294d…. 0 hits.
28. agent-sdk/hooks.md — 46,054 B, sha256 fd0706de…. 0 hits.
29. agent-sdk/file-checkpointing.md — 27,455 B, sha256 92184e8a…. 0 hits.
30. agent-sdk/cost-tracking.md — 27,423 B, sha256 b01f78de…. 0 hits.
31. agent-sdk/observability.md — 18,634 B, sha256 25f4d3da…. 0 hits.
32. agent-sdk/secure-deployment.md — 21,619 B, sha256 e384fdd5…. 0 hits.
33. https://platform.claude.com/docs/en/agent-sdk/skills — 200 after redirect to
    https://code.claude.com/docs/en/agent-sdk/skills (756,680 B HTML shell,
    sha256 17387d29…; 20 hits = the same page's rendered copy). REJECT as a
    distinct source: platform.claude.com is an alias of the canonical host, not a
    separate surface. S247's cited route reproduced.
34. https://platform.claude.com/docs/en/agent-sdk/skills.md — 200, 433,168 B,
    sha256 6da45f95307f63ac3eac7fead5ea27af10b0cd46839ed6e76e4143d1aa1f26cb —
    byte-identical to S247's recorded application-shell fetch. 0 token hits.
    REJECT: the `.md` suffix on the platform host redirects to bare /agent-sdk and
    serves the JS app shell; no markdown surface exists at this URL.
35. anthropics/claude-agent-sdk-typescript README — 2,502 B,
    sha256 d7f8965a…. 0 hits (pointer page to the docs site). REJECT.
36. npm registry @anthropic-ai/claude-agent-sdk — 1,127,915 B,
    sha256 5a9a4ad1…. 0 hits (registry document embeds the same pointer README).
    REJECT.

S249 control note: agent-sdk/skills.md (the S249 page) itself carries the channel at
L348–L380 (pre-approve note quoting both `allowed-tools` frontmatter and the
`allowedTools`/`allowed_tools` option) — consistent with the S248 row text and the
counter's located quote at line 348.

Net: the SDK `allowedTools`/`allowed_tools` channel is documented definitionally on
EIGHT surfaces beyond S249 (typescript.md, python.md, permissions.md, agent-loop.md,
configuration.md, claude-code-features.md, custom-tools.md, claude-agent-sdk-python
README) — all inside the same vendor docs cluster (code.claude.com agent-sdk tree +
one GitHub package README), so the coverage is deep on one authority, not spread
across vendors. skills.md (S227) does not name the SDK path in its pre-approve
section; the mirror host adds no distinct surface.

S-row candidates beyond S249 — 11-cell schema for the admittable eight
(id slots shown as next-free after the plan's S250; L1 owns the final ids)

| S251 | Claude Code — Agent SDK reference: TypeScript — https://code.claude.com/docs/en/agent-sdk/typescript.md | docs | B | The TypeScript Agent SDK `Options.allowedTools` field — its type, default, auto-approve semantics and interaction with `canUseTool`/`permissionMode`; one vendor's reference page | § `Options`, `allowedTools` row (`typescript.md:505`); fetched 2026-10-27, HTTP 200, 327318 B, sha256 b6a3c9c11a48e58cbadb6e1f9144b2f88ccbc0f252c35682836f8d7e5935d8f7; located quote "Tools to auto-approve without prompting, apart from reads from network paths. This does not restrict Claude to only these tools." | The option pre-approves listed tools without restricting the rest; unlisted tools fall through to permissionMode and canUseTool; naming a task-tracking tool also opts the session in | queued | 2026-10-27 | 90d | — |
| S252 | Claude Code — Agent SDK reference: Python — https://code.claude.com/docs/en/agent-sdk/python.md | docs | B | The Python Agent SDK `ClaudeAgentOptions.allowed_tools` field — same definition as the TypeScript option under snake_case spelling; one vendor's reference page | § `ClaudeAgentOptions`, `allowed_tools` row (`python.md:875`), `skills` row (`:915`); fetched 2026-10-27, HTTP 200, 163829 B, sha256 4977aa56160f8e04d636fea7806c42b3dc34981b79b0d66fa0d7c7eaaf398470; located quote "Tools to auto-approve without prompting, apart from reads from network paths." | The snake_case spelling carries identical semantics: auto-approve listed tools, no restriction of unlisted tools, Skill tool auto-added when `skills` is set | queued | 2026-10-27 | 90d | — |
| S253 | Claude Code — Agent SDK: Configure permissions — https://code.claude.com/docs/en/agent-sdk/permissions.md | docs | B | Where `allowed_tools`/`allowedTools` sits in the six-step permission evaluation order and the canUseTool-shadowing warning; one vendor's guide page | § How permissions are evaluated step 5 (`permissions.md:70`), § Allow and deny rules (`:83-87`); fetched 2026-10-27, HTTP 200, 33157 B, sha256 3397602f7b8540462ef7795268b02a0bc895c95c1d32413237bee92bbeb1cb3a; located quote "Check `allow` rules (from `allowed_tools` and settings.json). If a rule matches, the tool is approved." | The option's entries merge with settings.json allow rules at step 5, after hooks/deny/ask/mode; a bare-name entry shadows canUseTool and triggers CLAUDE_SDK_CAN_USE_TOOL_SHADOWED | queued | 2026-10-27 | 90d | — |
| S254 | Claude Code — Agent SDK: How the agent loop works — https://code.claude.com/docs/en/agent-sdk/agent-loop.md | docs | B | The same channel described inside the agent-loop walkthrough — read-only allowlist example and fall-through rule; one vendor's guide page | § Tool permissions (`agent-loop.md:172`), § Permission mode bypassPermissions row (`:238`); fetched 2026-10-27, HTTP 200, 41257 B, sha256 d98dad7ed94998ccf5ad8fa9e4269b12c98d4fe72d6dbc15be62bb52ff999f37; located quote "`allowed_tools` / `allowedTools` auto-approves listed tools." | Restates auto-approve + non-restriction semantics and binds both spellings in one bullet; documents the bypassPermissions interaction | queued | 2026-10-27 | 90d | — |
| S255 | Claude Code — Agent SDK: Configure your agent — https://code.claude.com/docs/en/agent-sdk/configuration.md | docs | B | The options-object framing of `allowedTools`/`allowed_tools` — presented as the pre-approve knob alongside model/maxTurns/cwd; one vendor's guide page | § Pass options to a session (`configuration.md:18,65`), § Configure specific features table row (`:266`); fetched 2026-10-27, HTTP 200, 18852 B, sha256 bc2e046b5f4129dae0aac5bb4987570eb21ece05edfadb99da0dc18b5de82c65; located quote "`allowedTools` (TypeScript) or `allowed_tools` (Python) pre-approves the listed tools, so calls to them run without stopping for approval." | Pairs both spellings in prose and states the non-restriction rule; the features table maps the option to "which tool calls are pre-approved" | queued | 2026-10-27 | 90d | — |
| S256 | Claude Code — Agent SDK: Use Claude Code features in the SDK — https://code.claude.com/docs/en/agent-sdk/claude-code-features.md | docs | B | The skills↔channel coupling on the feature-map page: setting `skills` adds the Skill tool to `allowedTools` automatically; one vendor's guide page | § Skills (`claude-code-features.md:128`), § Choose the right feature subagent row (`:288`); fetched 2026-10-27, HTTP 200, 20799 B, sha256 853607de24218eac839698efe2a3f29da889fb14b6760279dcc29e7ee0f66a70; located quote "When `skills` is set, the SDK adds the Skill tool to `allowedTools` automatically." | The `skills` option mutates `allowedTools` (Skill auto-add); an explicit `tools` list must include "Skill" itself | queued | 2026-10-27 | 90d | — |
| S257 | Claude Code — Agent SDK: Give Claude custom tools — https://code.claude.com/docs/en/agent-sdk/custom-tools.md | docs | B | The two-layer model: `allowedTools` changes permission (not availability) and the `mcp__{server}__{tool}` naming inside the option; one vendor's guide page | § Call a custom tool (`custom-tools.md:155`), § Configure allowed tools (`:374-380`); fetched 2026-10-27, HTTP 200, 40958 B, sha256 946948f5a92b2f387aafa39924dfcec651db257572d98898c07387b07366edcf; located quote "`allowedTools` and scoped `disallowedTools` rules change permission." | Availability (`tools`, bare `disallowedTools`) vs permission (`allowedTools`, scoped rules) is split explicitly; `always_ask` permission_policy beats an `allowedTools` entry | queued | 2026-10-27 | 90d | — |
| S258 | anthropics/claude-agent-sdk-python — README § Using Tools — https://raw.githubusercontent.com/anthropics/claude-agent-sdk-python/main/README.md | code | B | The Python package's own README statement of the option's semantics; revision-pinned to `2d485201617258867dd0f74b9e7307056f5938fe` (git ls-remote 2026-10-27; pinned re-fetch byte-identical) | § Using Tools (`README.md:59`); fetched 2026-10-27, HTTP 200, 13250 B, sha256 c38a933bf8fef26316ea38635989b254e69a26d21d80b96bf5731cba4e88bcc6; located quote "`allowed_tools` is a permission allowlist: listed tools are auto-approved, and unlisted tools fall through to `permission_mode` and `can_use_tool` for a decision." | The package README states the same allowlist semantics plus the "does not remove tools" clause — an authoritative non-docs-site corroboration | queued | 2026-10-27 | 90d | — |

Rejected/queued candidates get rows only if the L1 wants the negative record kept
(precedent: r80 wrote 12 rejected rows with observed facts); the evidence above is
complete for that if wanted. Zero-hit greeps are in
`.ufo/waves/round-81/build/Kb81R01NegSweep-fetch/` per file.

Reproduce: `grep -ciE 'allowed[-_]?[Tt]ools' <fetched-bytes>` per file in the build
dir; sha256 per `.fetch.json`.

VERDICT: 8 definitional surfaces admit (all one vendor cluster + one pinned GitHub README), 9 usage-only queued, 12+2 zero-hit/mirror rejects; skills.md's pre-approve section does not name the SDK path — S249's anchor is the sole skills-page statement of the channel.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81R01NegSweep.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81R01NegSweep-fetch/
