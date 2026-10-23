Result: MIXED — The committed Cursor inventory is supported; the candidate knowledge cell loses the root-skill exclusion and leaves Cursor-only discovery insufficiently scoped.

## Scope and evidence identity

Review only: depth is the assigned axis. No admission, integration, counter modification, client execution, or runtime judgment was performed. This seat did not rerun C1. No tool was installed or updated.

The reviewed committed bytes are from `07c33d73ddce769d9cea2846a6313164401b5478`, checked out in `/fast/scratch/hyaku/kotoba-r57a3/A3ShipCursor`. No sandbox commit was made. The lane was read-only except for this report.

Preparation commands, both exit 0:

```text
timeout 90s env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r57a3/A3ShipCursor
timeout 30s env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /fast/scratch/hyaku/kotoba-r57a3/A3ShipCursor checkout -q 07c33d73ddce769d9cea2846a6313164401b5478
```

Observed output: none, success.

Committed targets: `SKILL.md:122`; `corpus/knowledge/plugin-manifests-round57.md:47`. Candidate claims: `.ufo/waves/round-57/a3/a2-candidate.patch:24,106`; the proposed S088 row is at `:39`. The candidate was treated only as proposed text, never as source evidence. No earlier-attempt receipt or scratch artifact was used as evidence.

## Fresh source receipts

All source line numbers below refer to the unmodified downloaded bytes. S084's cited basename `plugins.md` is saved here as `cursor-plugins.md`; S088 is saved as `reference-plugins.md`. All source quotations below are contiguous, byte-exact substrings; no Markdown was stripped and no line breaks were folded.

### S084 — https://cursor.com/docs/plugins.md

Command chain, exit 0, cwd `/fast/scratch/hyaku/kotoba-r57a3/A3ShipCursor`:

```text
timeout 5s date -u && timeout 55s curl --location --max-time 45 --connect-timeout 10 --silent --show-error --dump-header cursor-plugins.headers --output cursor-plugins.md --write-out 'URL %{url_effective}\nHTTP %{http_code}\nDownloaded %{size_download} bytes\n' https://cursor.com/docs/plugins.md && timeout 5s sha256sum cursor-plugins.md && timeout 5s wc -c cursor-plugins.md
```

Observed output:

```text
Fri 23 Oct 2026 06:46:07 AM UTC
URL https://cursor.com/docs/plugins.md
HTTP 200
Downloaded 20323 bytes
74387ff95205965ca3060fac4d12966fea7b1525cc0e972e6f265bbee591cb62  cursor-plugins.md
20323 cursor-plugins.md
```

### S088 candidate source — https://cursor.com/docs/reference/plugins.md

Command chain, exit 0, same cwd:

```text
timeout 5s date -u && timeout 55s curl --location --max-time 45 --connect-timeout 10 --silent --show-error --dump-header reference-plugins.headers --output reference-plugins.md --write-out 'URL %{url_effective}\nHTTP %{http_code}\nDownloaded %{size_download} bytes\n' https://cursor.com/docs/reference/plugins.md && timeout 5s sha256sum reference-plugins.md && timeout 5s wc -c reference-plugins.md
```

Observed output:

```text
Fri 23 Oct 2026 06:46:07 AM UTC
URL https://cursor.com/docs/reference/plugins.md
HTTP 200
Downloaded 30324 bytes
3bbf36f3320382adb68509aa758e2e764fd31c5de5f5c70c6af1683497b11204  reference-plugins.md
30324 reference-plugins.md
```

Both source hashes independently match the hashes claimed for those pages. This corroborates the page bytes, not the candidate's interpretation or its claimed earlier access history.

## Findings

### 1. Fixable defect: the candidate knowledge cell omits a necessary root-skill condition

Candidate `:106` says that without manifest paths Cursor discovers the component folders “and reads a root `SKILL.md` as a single-skill plugin.” Its cited S088 range does contain the relevant row, but its text drops a condition actually present in that row.

Authoritative evidence, `/fast/scratch/hyaku/kotoba-r57a3/A3ShipCursor/reference-plugins.md:164`:

> Treated as a single-skill plugin (only if no `skills/` dir and no manifest `skills` field)

Strongest counterexample, a documented-rule deduction, not an executed Cursor test:

```text
my-plugin/
  .cursor-plugin/plugin.json  containing {"name":"example"}
  SKILL.md
  skills/
    code-reviewer/
      SKILL.md
```

[INFERENCE] This package has no manifest component paths, so the candidate knowledge sentence's premise holds. Nevertheless, the root `SKILL.md` does not qualify for the documented single-skill fallback because `skills/` exists. The source explicitly excludes this case. Even an empty `skills/` directory is not excluded from that guard by the documentation.

The candidate SKILL cell's word “alone” can be read as shorthand for the exclusion, so I do not claim it is necessarily false. It is weaker than spelling out both tests and does not limit this fallback to Cursor Plugins. Also, `reference-plugins.md:65` requires a Cursor Plugin manifest; “alone” must not imply that a manifest-free directory is sufficient.

Impacted axes: depth directly; calibration if the shortened statement is presented as fully source-checked. This is a repairable wording defect, not an unavoidable axis tradeoff.

### 2. Discovery must be per component and Cursor-Plugin-specific

`reference-plugins.md:152` titles the section “Cursor Plugin component discovery”; `:16` says the rest of the reference documents the Cursor plugin format. Candidate `:106` says only “Cursor discovers,” after discussing both formats. Do not export these discovery rules to Agent Plugins on this evidence.

`reference-plugins.md:154,158-164` provides the defaults. At `:166`:

> If a manifest field **is** specified (e.g., `"skills": "./my-skills/"`), it **replaces** folder discovery for that component.

The next sentence on the same line is:

> The default folder is not also scanned.

Thus an explicit field for one component does not disable discovery for every other component, and the explicit field is not additive. The candidate range `:152-165` stops immediately before this replacement rule. The existing default paths are correctly cited; the safe replacement must extend the citation to `:166` and state per-component scope.

### 3. The tip's six instruction-bearing component classes all hold; variables need a configuration qualifier

No listed component in either committed cell is unsupported by S084 `plugins.md:9-30`. The per-part evidence is below. No additional instruction-bearing component class is enumerated in that range beyond those six.

The tip omits the additional documented `variables` feature at S084 `:28`. The candidate is right to notice it, but the reference defines a schema for user configuration, not a new instruction-file format. S088 `reference-plugins.md:94,114-118` is the relevant source, outside the candidate cell's S088 `:152-165` citation. At `:114`:

> The plugin only defines the schema; it does not include the secret values themselves.

Use “a user-configuration `variables` schema,” rather than implying the package ships user values. The candidate knowledge parenthesis “not instruction-bearing” is a classification, not an explicit assertion by the page; the replacement below avoids needing that stronger negative claim.

The overview additionally describes canvases at S084 `:34-41` as “shared setup templates your team can open and reuse.” That passage does not establish another AI-instruction-file class. I would not add canvases to an instruction-bearing inventory on that evidence. Assets, logos, and marketplace distribution metadata likewise are not additional named instruction-file classes in these pages.

### 4. Local development claim holds, but not in the component citation range

The candidate SKILL cell's `~/.cursor/plugins/local` claim is supported by S084 `plugins.md:211` and `:313-326`, not by `:9-30`. The candidate knowledge introduction separately cites `:211`, correctly. The statement is about a development location, not unconditional automatic loading: `:325-326` conditions discovery on local imports being allowed, and `:328-334` gives Enterprise and same-name precedence qualifications. The proposed cell below retains only the location claim.

## Line evidence for every retained part

Paths in this table are under `/fast/scratch/hyaku/kotoba-r57a3/A3ShipCursor/`.

| Part | Fresh line evidence | What it establishes |
|---|---|---|
| Cursor Plugin rules | `cursor-plugins.md:13`; `reference-plugins.md:14,159,170` | Cursor-only component; persistent guidance; default `rules/` |
| Skills in both formats | `cursor-plugins.md:14`; `reference-plugins.md:13-14,158,196` | Both formats; default Cursor Plugin `skills/`; `SKILL.md` files |
| Cursor Plugin agents | `cursor-plugins.md:15`; `reference-plugins.md:14,160,236` | Configurations and prompts; default `agents/` |
| Cursor Plugin commands | `cursor-plugins.md:16`; `reference-plugins.md:14,161,268-270` | Agent-executable files; default `commands/` |
| MCP servers in both formats | `cursor-plugins.md:17,27`; `reference-plugins.md:13-14,163,330-332` | Both formats; `mcp.json`; Cursor default discovery |
| Cursor Plugin hooks | `cursor-plugins.md:18`; `reference-plugins.md:14,162,295` | Event-triggered scripts; default `hooks/hooks.json` |
| Cursor Plugin variables schema | `cursor-plugins.md:28`; `reference-plugins.md:14,94,112-118` | Names/types/descriptions for user configuration; schema, not secret values |
| Agent Plugin root `plugin.json` | `cursor-plugins.md:27`; `reference-plugins.md:13` | Format and location, with skills/MCP contents |
| Either format's local development location | `cursor-plugins.md:211,313-326` | `~/.cursor/plugins/local`; the replacement does not claim unconditional loading |
| Cursor-only, per-component discovery | `reference-plugins.md:16,152-166` | Defaults apply to a component without a specified manifest field; a specified field replaces that discovery |
| Root `SKILL.md` fallback | `reference-plugins.md:164`; manifest requirement `:65` | Single skill only when neither `skills/` nor manifest `skills` exists; not a manifest-free plugin |

## Exact cells to land: my corrected candidate

No manifest cell or action cell change is proposed. These are editorial recommendations for L1, not landed edits.

### SKILL.md — What a plugin can ship

Exact tip old text (`SKILL.md:122`):

```text
Cursor Plugins: rules, skills, agents, commands, MCP servers, hooks; Agent Plugins: skills and MCP servers
```

Exact candidate old text (`a2-candidate.patch:24`):

```text
Cursor Plugins: rules, skills, agents, commands, MCP servers, hooks, variables; Agent Plugins: skills and MCP servers; local development from `~/.cursor/plugins/local`; a root `SKILL.md` alone is a single-skill plugin
```

Either old text → this exact new cell:

```text
Cursor Plugins: rules, skills, agents, commands, MCP servers, hooks, and a user-configuration `variables` schema; Agent Plugins: skills and MCP servers; local development from `~/.cursor/plugins/local`; for Cursor Plugins, a root `SKILL.md` is a single-skill fallback only if neither a `skills/` directory nor a manifest `skills` field exists
```

### corpus/knowledge/plugin-manifests-round57.md — Instruction-bearing parts a plugin can ship

Exact tip old text (`:47`):

```text
Cursor Plugins: rules, skills, agents, commands, MCP servers, hooks; Agent Plugins (root `plugin.json`): skills and MCP servers
```

Exact candidate old text (`a2-candidate.patch:106`):

```text
Cursor Plugins: rules, skills, agents, commands, MCP servers, hooks, `variables` (user-config placeholders, not instruction-bearing); Agent Plugins (root `plugin.json`): skills and MCP servers; without manifest paths Cursor discovers `skills/`, `rules/`, `agents/`, `commands/`, `hooks/hooks.json`, `mcp.json`, and reads a root `SKILL.md` as a single-skill plugin
```

Either old text → this exact new cell:

```text
Cursor Plugins: rules, skills, agents, commands, MCP servers, hooks, and a `variables` schema for user configuration; Agent Plugins (root `plugin.json`): skills and MCP servers; Cursor Plugins discover `skills/`, `rules/`, `agents/`, `commands/`, `hooks/hooks.json`, and `mcp.json` per component only when its manifest field is absent; a root `SKILL.md` is a single-skill fallback only if neither a `skills/` directory nor a manifest `skills` field exists
```

Exact tip source-lines old text:

```text
S084 `plugins.md:9-30`
```

Exact candidate source-lines old text:

```text
S084 `plugins.md:9-30`; S088 `reference-plugins.md:152-165`
```

Either old text → this exact new source-lines cell (also supplies the SKILL local-development location):

```text
S084 `plugins.md:9-30,211`; S088 `reference-plugins.md:13-16,65,88-94,112-118,152-166`
```

Prerequisite for citing S088: L1 must integrate its independently verified source record and include its URL in the knowledge entry's source metadata; this report does not integrate or admit that row. The source receipt above is fresh evidence for its page, not approval of every statement in the untrusted candidate.

## Smallest safe correction

Keep all six supported component classes and both format identities. Replace the candidate's unqualified root-skill clause with the explicit two-part exclusion, limit discovery to Cursor Plugins and to each component, and extend citations to the variable schema and replacement rule. No counter change or runtime behavior change is needed. This review does not turn the declared C1 miss into a hit.
