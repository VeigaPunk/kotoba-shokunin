Result: MIXED — All listed component kinds are supported, but the candidate leaves both Codex cells unchanged and omits manifest prompt metadata and the scaffold's optional/initial-empty qualifier.

## Scope and axes

Reviewed only the Codex shipment cells at `07c33d73ddce769d9cea2846a6313164401b5478`: `SKILL.md:118` and `corpus/knowledge/plugin-manifests-round57.md:43`, plus their appearances in `.ufo/waves/round-57/a3/a2-candidate.patch:16,98` and its S086 claim at line 37. The patch is an untrusted review target, not vendor evidence.

Impacted axis: **depth**, specifically instruction-location completeness and exact configuration qualifiers. Freshness is supported by the new fetch; calibration requires distinguishing documented examples from automatic loading. These are fixable documentation details, not a demonstrated runtime regression or a judgment of C1.

## Commands and live-source receipt

Read-only lane comparison, exit 0, no output:

```text
timeout 30 git --no-optional-locks diff 07c33d73ddce769d9cea2846a6313164401b5478 -- SKILL.md corpus/knowledge/plugin-manifests-round57.md corpus/SOURCES.md
```

Isolated clone/check-out command, exit 0, no output:

```text
env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE timeout 120 git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r57a3/A3ShipCodex && env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE timeout 30 git -C /fast/scratch/hyaku/kotoba-r57a3/A3ShipCodex checkout -q 07c33d73ddce769d9cea2846a6313164401b5478
```

S080 and proposed S086 cite the same URL: https://developers.openai.com/plugins/build/plugins.md . I fetched it myself with this command, exit 0:

```text
timeout 5 date -u && timeout 75 curl --location --fail --silent --show-error --max-time 60 --output /fast/scratch/hyaku/kotoba-r57a3/A3ShipCodex/openai-plugins.md --write-out 'HTTP %{http_code}\nBytes %{size_download}\nURL %{url_effective}\n' https://developers.openai.com/plugins/build/plugins.md && timeout 5 wc -c /fast/scratch/hyaku/kotoba-r57a3/A3ShipCodex/openai-plugins.md && timeout 5 sha256sum /fast/scratch/hyaku/kotoba-r57a3/A3ShipCodex/openai-plugins.md
```

Observed output:

```text
Fri 23 Oct 2026 06:46:15 AM UTC
HTTP 200
Bytes 38036
URL https://developers.openai.com/plugins/build/plugins.md
38036 /fast/scratch/hyaku/kotoba-r57a3/A3ShipCodex/openai-plugins.md
c37e330df8f040df8ee2f48035992b37c6a7decf6c3f5640822ca0907118c4e1  /fast/scratch/hyaku/kotoba-r57a3/A3ShipCodex/openai-plugins.md
```

Below, `F` means those fetched bytes, `/fast/scratch/hyaku/kotoba-r57a3/A3ShipCodex/openai-plugins.md`. This is the same byte count and digest recorded for S080 and claimed for S086. That verifies current content equality, not the candidate's historical access times.

## Findings and strongest counterexample

### 1. The candidate does not replace either Codex cell

Patch lines 16 and 98 are unchanged context lines, not additions or deletions. S086 changes the source registry's teaching about scaffold contents; it does not change the Codex inventory. There is no candidate Codex replacement to prefer over the tip.

### 2. Manifest-embedded prompt strings are omitted

The fetched OpenAI manifest example places literal prompt strings under `extensions.com.openai.interface.defaultPrompt` (`F:608-631`; nesting at `614-618`, field and values at `628-631`). Byte-exact excerpt, `F:628-630`:

```text
        "defaultPrompt": [
          "Use My Plugin to summarize new CRM notes.",
          "Use My Plugin to triage new customer follow-ups."
```

This is the strongest counterexample: the cited page itself contains prompt-bearing text inside the manifest, whereas both inventories enumerate only skills, MCP servers, hooks and assets. [INFERENCE] A reader treating that enumeration as exhaustive could omit the manifest's own prompt strings from an instruction audit. Treat this as prompt-bearing presentation metadata, not evidence of always-on or automatic invocation.

The onboarding skill is also worth locating explicitly: `F:650-657,667,673-676` documents a packaged setup skill selected by `extensions.com.openai.onboardingSkill`. Invocation occurs when users run setup (`F:650-653`), not merely because installation happened. This is a specialization already covered by “skills,” not an additional independent component kind.

### 3. Preserve the scaffold distinction without inventing generated hook files

`F:61-89` supports the compatibility scaffold, including optional `.mcp.json`, `.app.json`, and directories. But `F:76-80` says only the manifest is always created and identifies initially empty objects. Byte-exact `F:77`:

```text
directories are optional. `.mcp.json` starts with an empty `mcpServers` object,
```

Thus the entry's parenthetical “the scaffold writes `.mcp.json`” loses a material optional/initial-empty qualifier. Do not change this to an assertion that `.mcp.json` is a portable filename: `F:86-89` explicitly distinguishes portable `mcp.json`, its schema, and its per-server transport `type`.

The candidate S086 correction is supported in substance by `F:76-84`: requested hooks create an empty directory, not a hook configuration or executable script. `.mcp.json` and `.app.json` are not empty files; their `mcpServers` and `apps` objects start empty. Do not reintroduce an assertion that the creator generates populated hook files or runnable scripts.

## Evidence for every part

| Cell part | Live fetched lines | Reading |
|---|---|---|
| Skills under `skills/` | `F:18,70,79-80`; concrete skill path `242-245` | Supported by the original cited ranges. |
| Portable MCP configuration in `mcp.json` | `F:19,86-89` | Supported; distinct from compatibility `.mcp.json`. |
| Compatibility scaffold `.mcp.json` | `F:61-78` | Supported, but optional and initially containing an empty `mcpServers` object. |
| Registered-server mappings in `.app.json` | `F:24-26,68-79,614-616,697-698` | Explicitly documented; these are mappings, not another instruction-file format. |
| Lifecycle hooks for manually installed Codex desktop plugins | `F:21-22,82-84,703-705` | Supported, including the original desktop/manual restriction. |
| Assets | `F:20,73`; visual examples `633-635,695-696` | Supported as package contents; the page's concrete examples are visual assets, not instructions. |
| Onboarding skill and user-run setup | `F:650-657,667,673-676` | Supported specialization of skills, not a new independent kind or automatic installation-time instruction. |
| Manifest example's `extensions.com.openai.interface.defaultPrompt` strings | `F:608-631`, particularly `614-618,628-631` | Explicit example content; do not infer automatic loading. |
| Portable root `plugin.json` | `F:14-15,86-88` | Supported by the original cited ranges. |
| `.codex-plugin/plugin.json` compatibility fallback | `F:24-26,54,61-67`; precise selection rule `642-646` | Supported. The root OpenAI object replaces the overlay; they are not merged. |

The existing entry citation `S080 build-plugins.md:14-30,52-89` really contains evidence for every component it currently lists and its layout statements. **No currently listed component is fabricated, and no original cited range misses its claimed text.** Its deficiencies are omitted detail and qualification, not broken line numbers. The additional fields require additional cited ranges.

Hook discovery (`F:911-912`), explicit replacement rather than addition (`F:932-935`), and hook trust (`F:907-909`) further explain the already listed lifecycle-hook category. They do not justify inventing a separate command/agent/rule package type. Likewise, a `scripts/` directory in the scaffold is not evidence for an independently loaded instruction surface.

## Exact smallest safe correction

Use my own replacements below. Keep the manifest and Action cells unchanged. Keep one source authority: these additions are on S080's already cited page, not independent corroboration from a second source merely because S086 has a new ID.

### `SKILL.md:118` — only the `What a plugin can ship` cell

Old:

```text
skills, MCP servers via `mcp.json`, lifecycle hooks for manually installed desktop plugins, assets
```

New:

```text
skills (including setup via `extensions.com.openai.onboardingSkill`), MCP servers via `mcp.json` (compatibility scaffold: optional `.mcp.json` with an initially empty `mcpServers` object) and registered-server mappings via `.app.json`, lifecycle hooks for manually installed Codex desktop plugins, assets; the manifest presentation example also includes `extensions.com.openai.interface.defaultPrompt` prompt strings
```

### `corpus/knowledge/plugin-manifests-round57.md:43` — only the shipment cell

Old:

```text
skills under `skills/`, MCP servers through `mcp.json` (the scaffold writes `.mcp.json`), lifecycle hooks for manually installed desktop plugins, assets; portable packages put `plugin.json` at the root and `.codex-plugin/plugin.json` stays supported as a compatibility fallback
```

New:

```text
skills under `skills/` (including optional onboarding skills selected by `extensions.com.openai.onboardingSkill` when users run setup), MCP servers through `mcp.json` (compatibility scaffold: optional `.mcp.json` with an initially empty `mcpServers` object) and registered-server mappings through `.app.json`, lifecycle hooks for manually installed Codex desktop plugins, assets; the OpenAI manifest presentation example includes `extensions.com.openai.interface.defaultPrompt` prompt strings; portable packages put `plugin.json` at the root and `.codex-plugin/plugin.json` stays supported as a compatibility fallback
```

Matching Source lines cell, old → new:

```text
S080 `build-plugins.md:14-30,52-89`
```

→

```text
S080 `build-plugins.md:14-30,61-89,608-631,650-676,695-705`
```

This preserves all supported existing components and the portable/compatibility distinction, adds the manifest's actual prompt-bearing example without a loading claim, and fixes the scaffold qualifier. It does not change a manifest token, the frozen counter, or the declared miss.

No lane code, counter, client runtime, build, test, or judge was run. No lane files were changed except this assigned report. No tools were installed or updated.
