Result: HOLDS — at 2026-10-23 06:45 UTC the same two Cursor-cache packages still ship `.claude-plugin`, `.codex-plugin` and `.cursor-plugin` as sibling directories, each with a non-empty `plugin.json`. No entry text change.

# Question

Re-derive, on this host today, the host-observation sentence in `corpus/knowledge/plugin-manifests-round57.md` § Findings at `07c33d73ddce769d9cea2846a6313164401b5478` (lane `HEAD` is that commit; `git --no-optional-locks show` of those lines matches the worktree):

> One package can serve several clients at once: VS Code reads Claude's format (S081 `:103`), and the host inventory found plugins shipping `.claude-plugin`, `.codex-plugin` and `.cursor-plugin` side by side (`.ufo/waves/round-57/build/ScoutPluginSweep.md`, host observation, not a documented rule).

File lines 55–57. The sentence cites `ScoutPluginSweep.md` §3.6, which names:

- `~/.cursor/plugins/cache/cursor-public/aws-agents/d00d03ae…/`
- `~/.cursor/plugins/cache/cursor-public/elevenlabs/1c5f1de1…/`

and the cache counts "14 carry `.cursor-plugin/`, 3 carry `.claude-plugin/`, 2 carry `.codex-plugin/`".

This is a filesystem re-derivation of that inventory. It does not re-open vendor docs and does not re-check which binaries read which path.

# Commands and output

`date -u` before the finds: `Fri 23 Oct 2026 06:45:51 AM UTC`.

All six roots exist (`/home/vgpnk/.claude`, `.codex`, `.cursor`, `.config/opencode`, `.gemini`, `.copilot`). No `/fast/scratch` path. `/usr/bin/find` default (no `-L`), so directory symlinks were not followed. Every hit below printed `%y` = `d` (real directory, not a symlink). No tool installed.

## `~/.cursor`, maxdepth 10 (exit 0)

```
timeout 120 /usr/bin/find /home/vgpnk/.cursor -maxdepth 10 \
  \( -name '.claude-plugin' -o -name '.codex-plugin' -o -name '.cursor-plugin' \) \
  -type d -printf '%y %p\n' | sort
```

```
d /home/vgpnk/.cursor/plugins/cache/cursor-public/1password/857bf89a2c3583c40ff1eea7c4c6dd30cc1156cd/.cursor-plugin
d /home/vgpnk/.cursor/plugins/cache/cursor-public/agent-compatibility/9b93e81fb2921b9263d9463c15bafeabfe3903aa/.cursor-plugin
d /home/vgpnk/.cursor/plugins/cache/cursor-public/aws-agents/d00d03ae6e4872b9f35a2b2ca86d0cbdbaa81684/.claude-plugin
d /home/vgpnk/.cursor/plugins/cache/cursor-public/aws-agents/d00d03ae6e4872b9f35a2b2ca86d0cbdbaa81684/.codex-plugin
d /home/vgpnk/.cursor/plugins/cache/cursor-public/aws-agents/d00d03ae6e4872b9f35a2b2ca86d0cbdbaa81684/.cursor-plugin
d /home/vgpnk/.cursor/plugins/cache/cursor-public/browser-use/4749bcbfe456e5384b98281a8a66119352197f59/.cursor-plugin
d /home/vgpnk/.cursor/plugins/cache/cursor-public/elevenlabs/1c5f1de18e1d28a3c84a9aa2146a6a5e9484488c/.claude-plugin
d /home/vgpnk/.cursor/plugins/cache/cursor-public/elevenlabs/1c5f1de18e1d28a3c84a9aa2146a6a5e9484488c/.codex-plugin
d /home/vgpnk/.cursor/plugins/cache/cursor-public/elevenlabs/1c5f1de18e1d28a3c84a9aa2146a6a5e9484488c/.cursor-plugin
d /home/vgpnk/.cursor/plugins/cache/cursor-public/exa/0c6bb4c04067971681f5777606acb60a71ed7270/.cursor-plugin
d /home/vgpnk/.cursor/plugins/cache/cursor-public/github/9b93e81fb2921b9263d9463c15bafeabfe3903aa/.cursor-plugin
d /home/vgpnk/.cursor/plugins/cache/cursor-public/gmail/9b93e81fb2921b9263d9463c15bafeabfe3903aa/.cursor-plugin
d /home/vgpnk/.cursor/plugins/cache/cursor-public/google-drive/9b93e81fb2921b9263d9463c15bafeabfe3903aa/.cursor-plugin
d /home/vgpnk/.cursor/plugins/cache/cursor-public/link/d0b502744a798f7fb8c1835532464193f5034d4c/.cursor-plugin
d /home/vgpnk/.cursor/plugins/cache/cursor-public/parallel/b0fd7db38cf7398d46bc68dd631af9ec285bc55f/.cursor-plugin
d /home/vgpnk/.cursor/plugins/cache/cursor-public/pstack/9b93e81fb2921b9263d9463c15bafeabfe3903aa/.cursor-plugin
d /home/vgpnk/.cursor/plugins/cache/cursor-public/vercel/3b472643cbb1a42479d99b0c9a1d27b8bc84aaa7/.claude-plugin
d /home/vgpnk/.cursor/plugins/cache/cursor-public/vercel/3b472643cbb1a42479d99b0c9a1d27b8bc84aaa7/.cursor-plugin
d /home/vgpnk/.cursor/plugins/cache/cursor-public/x/9b93e81fb2921b9263d9463c15bafeabfe3903aa/.cursor-plugin
```

Cache tally, same shape as `ScoutPluginSweep.md:95`: 14 `.cursor-plugin`, 3 `.claude-plugin` (aws-agents, elevenlabs, vercel), 2 `.codex-plugin` (aws-agents, elevenlabs). The two hash prefixes in §3.6 are unchanged: `d00d03ae6e4872b9f35a2b2ca86d0cbdbaa81684`, `1c5f1de18e1d28a3c84a9aa2146a6a5e9484488c`.

## `~/.claude`, maxdepth 10 (exit 0)

```
timeout 120 /usr/bin/find /home/vgpnk/.claude -maxdepth 10 \
  \( -name '.claude-plugin' -o -name '.codex-plugin' -o -name '.cursor-plugin' \) \
  -type d -printf '%y %p\n' | sort
```

42 directories, every one `.claude-plugin`, no `.codex-plugin` and no `.cursor-plugin`. Deepest hit is depth 5 (`plugins/marketplaces/claude-plugins-official/external_plugins/<name>/.claude-plugin`). Full list:

```
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/external_plugins/asana/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/external_plugins/context7/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/external_plugins/discord/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/external_plugins/fakechat/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/external_plugins/firebase/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/external_plugins/github/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/external_plugins/gitlab/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/external_plugins/imessage/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/external_plugins/laravel-boost/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/external_plugins/linear/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/external_plugins/playwright/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/external_plugins/serena/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/external_plugins/telegram/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/external_plugins/terraform/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/plugins/agent-sdk-dev/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/plugins/claude-code-setup/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/plugins/claude-md-management/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/plugins/claude-security/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/plugins/code-modernization/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/plugins/code-review/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/plugins/code-simplifier/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/plugins/commit-commands/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/plugins/cwc-makers/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/plugins/example-plugin/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/plugins/explanatory-output-style/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/plugins/feature-dev/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/plugins/frontend-design/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/plugins/hookify/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/plugins/learning-output-style/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/plugins/math-olympiad/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/plugins/math-proof/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/plugins/mcp-server-dev/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/plugins/mcp-tunnels/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/plugins/playground/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/plugins/plugin-dev/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/plugins/project-artifact/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/plugins/pr-review-toolkit/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/plugins/ralph-loop/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/plugins/security-guidance/.claude-plugin
d /home/vgpnk/.claude/plugins/marketplaces/claude-plugins-official/plugins/skill-creator/.claude-plugin
d /home/vgpnk/.claude/plugins/synced/ce424f13-ba19-43c2-9454-94728c447ee4_1c4d9ed3-dfe7-4c05-b09a-ccad07f0d4fc/cowork-plugin-management/.claude-plugin
```

The sweep's "41" was `plugin.json` files under `.claude-plugin`, not directory count. This pass did not re-count those `plugin.json` files. The marketplace catalog directory above is the extra directory (it holds `marketplace.json` per the sweep, not re-opened here).

## `~/.codex`, maxdepth 10 (exit 0, empty)

```
timeout 120 /usr/bin/find /home/vgpnk/.codex -maxdepth 10 \
  \( -name '.claude-plugin' -o -name '.codex-plugin' -o -name '.cursor-plugin' \) \
  -type d -printf '%y %p\n' | sort
```

No output. No side-by-side package under `~/.codex` within this bound.

## `~/.config/opencode`, `~/.gemini`, `~/.copilot`, maxdepth 10 (exit 0, empty)

```
timeout 120 /usr/bin/find /home/vgpnk/.config/opencode /home/vgpnk/.gemini /home/vgpnk/.copilot \
  -maxdepth 10 \
  \( -name '.claude-plugin' -o -name '.codex-plugin' -o -name '.cursor-plugin' \) \
  -type d -printf '%y %p\n' | sort
```

No output. The sweep did not search `~/.copilot`; this pass did. Still no hit.

## Parents that have all three, maxdepth 16 (find exit 0)

`date -u`: `Fri 23 Oct 2026 06:46:15 AM UTC`.

```
timeout 120 /usr/bin/find /home/vgpnk/.claude /home/vgpnk/.codex /home/vgpnk/.cursor \
  /home/vgpnk/.config/opencode /home/vgpnk/.gemini /home/vgpnk/.copilot \
  -maxdepth 16 \
  \( -name '.claude-plugin' -o -name '.codex-plugin' -o -name '.cursor-plugin' \) \
  -type d -printf '%p\n' | awk -F/ '{
  p=$0; sub(/\/[^/]+$/,"",p); kind=$NF; parents[p]=parents[p] " " kind; n[kind]++
}
END {
  print "COUNTS"
  for (k in n) print k, n[k]
  print "TRIPLES"
  for (p in parents) if (parents[p] ~ /\.claude-plugin/ && parents[p] ~ /\.codex-plugin/ && parents[p] ~ /\.cursor-plugin/) print p, parents[p]
}'
```

```
COUNTS
.codex-plugin 2
.cursor-plugin 14
.claude-plugin 45
TRIPLES
/home/vgpnk/.cursor/plugins/cache/cursor-public/aws-agents/d00d03ae6e4872b9f35a2b2ca86d0cbdbaa81684  .cursor-plugin .codex-plugin .claude-plugin
/home/vgpnk/.cursor/plugins/cache/cursor-public/elevenlabs/1c5f1de18e1d28a3c84a9aa2146a6a5e9484488c  .cursor-plugin .codex-plugin .claude-plugin
```

`.claude-plugin` 45 = the 42 under `~/.claude` plus the 3 under `~/.cursor`. Nothing new between depth 11 and 16. Exactly two parents hold all three names.

## Sibling check (not nested inside each other), exit 0

`timeout 30 /usr/bin/find <pkg> -maxdepth 1 -printf '%y %f\n'` and `timeout 30 /usr/bin/find <pkg> -maxdepth 2 -name plugin.json -printf '%s %p\n'`.

aws-agents depth-1 includes, as siblings: `.claude-plugin`, `.codex-plugin`, `.cursor-plugin`, `skills`, root `plugin.json`, `mcp.json`, `.mcp.json`. Its four `plugin.json` files:

```
1102 .../aws-agents/d00d03ae6e4872b9f35a2b2ca86d0cbdbaa81684/plugin.json
1304 .../aws-agents/d00d03ae6e4872b9f35a2b2ca86d0cbdbaa81684/.claude-plugin/plugin.json
1419 .../aws-agents/d00d03ae6e4872b9f35a2b2ca86d0cbdbaa81684/.cursor-plugin/plugin.json
2487 .../aws-agents/d00d03ae6e4872b9f35a2b2ca86d0cbdbaa81684/.codex-plugin/plugin.json
```

elevenlabs depth-1 includes, as siblings: `.claude-plugin`, `.codex-plugin`, `.cursor-plugin`, `skills`, `architect`, `mcp.json`, `server.json`. No root `plugin.json` at depth 2. The three manifests:

```
736  .../elevenlabs/1c5f1de18e1d28a3c84a9aa2146a6a5e9484488c/.cursor-plugin/plugin.json
861  .../elevenlabs/1c5f1de18e1d28a3c84a9aa2146a6a5e9484488c/.claude-plugin/plugin.json
964  .../elevenlabs/1c5f1de18e1d28a3c84a9aa2146a6a5e9484488c/.codex-plugin/plugin.json
```

Opened heads (bytes, not a doc quote). aws-agents `.codex-plugin/plugin.json:2-3` is `"name": "aws-agents"` / `"version": "1.0.0"`, matching the sweep's `:99` snippet. elevenlabs `.claude-plugin/plugin.json:2-3` is `"$schema": "https://json.schemastore.org/claude-code-plugin-manifest.json"` / `"name": "elevenlabs"`. The other four heads are the same two names (`aws-agents`, `elevenlabs`) at version `1.0.0` and `0.4.0`.

# What holds, and what the citation over-says

The entry sentence holds. Two installed packages, the same two the sweep named, each contain `.claude-plugin`, `.codex-plugin` and `.cursor-plugin` as siblings, and each of those six directories contains a non-empty `plugin.json`. They are the only such parents under the six roots through depth 16.

`ScoutPluginSweep.md:95` "both multi-client ones carry all three" does not match the third `.claude-plugin` package, which the 14/3/2 count already implied and which is on disk today:

`~/.cursor/plugins/cache/cursor-public/vercel/3b472643cbb1a42479d99b0c9a1d27b8bc84aaa7/`

Depth-1 siblings there include `.claude-plugin` and `.cursor-plugin`, and do not include `.codex-plugin`. Also present, outside this claim: `.kimi-plugin`, `.plugin`. Vercel's `plugin.json` files were not opened. [INFERENCE] vercel is the unnamed third `.claude-plugin` from the sweep, because today's 14/3/2 counts and the two named hashes match §3.6 and the sweep never named the third. That inference is not needed for the entry sentence, which says the inventory found such plugins, not that every multi-manifest package has all three.

# Entry text

No old→new. Lines 55–57 stay. The sentence is a host observation, and the host still shows it. Do not tighten it into "both multi-client packages" — that stronger wording is the sweep's, and vercel falsifies it.

# Limits

- Not searched: depth greater than 16; any path outside the six named roots; symlink targets (`-L` not passed).
- Not re-done: Claude `plugin.json` recount (41), binary strings, which client loads which directory. Out of the sentence under test.
- Point in time only (`2026-10-23 06:45:51 UTC` through `06:46:15 UTC`). A later cache refresh can add or drop a package.
- No tools installed. No lane git/jj write. Read-only `git --no-optional-locks show` / `rev-parse` only.

Confidence: high for the two packages and the six-root bound through depth 16. The vercel-was-already-the-third inference is marked above and is not load-bearing.
