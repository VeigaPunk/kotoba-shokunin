Result: BREAKS — The tip omits citation ranges for tools and hooks; the candidate repairs those ranges but retains ambiguous agent-registration wording and an unnecessarily universal manifest claim.

## Scope and axes

Reviewed the opencode ship cells at lane tip `07c33d73ddce769d9cea2846a6313164401b5478`, plus the corresponding claims in `.ufo/waves/round-57/a3/a2-candidate.patch`. The patch is proposal data, not evidence. Primary impacted axis: **depth**; secondary risks are consistency and calibration of what the cited page actually establishes. These are fixable documentation defects, not a proposed change to the frozen counter or an admission judgment.

Read-only review. No lane code, counter, client runtime, paid model call, or test was executed. No lane files were changed except this report. No tools were installed or updated. No sandbox commits were created. This seat did not rerun C1; its assignment is the opencode ship-cell source review.

## Independently fetched evidence

All evidence below is newly fetched by this seat, not inherited from earlier-attempt scratch files. The sandbox checkout command exited 0 with no output:

```sh
timeout 120s env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r57a3/A3Shipopencode && timeout 60s env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /fast/scratch/hyaku/kotoba-r57a3/A3Shipopencode checkout -q 07c33d73ddce769d9cea2846a6313164401b5478
```

Fetch working directory: `/fast/scratch/hyaku/kotoba-r57a3/A3Shipopencode`. Each command exited 0. Headers and original response bodies remain there.

### S085 build guide

```sh
timeout 5s date -u && timeout 90s curl --location --max-time 75 --connect-timeout 15 --silent --show-error --dump-header fetch-S085.headers --output fetch-S085-index.mdx --write-out 'HTTP %{http_code}\nURL %{url_effective}\nBytes %{size_download}\n' https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/build/plugins/index.mdx && timeout 5s wc -c fetch-S085-index.mdx && timeout 5s sha256sum fetch-S085-index.mdx
```

Observed output:

```text
Fri 23 Oct 2026 06:45:57 AM UTC
HTTP 200
URL https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/build/plugins/index.mdx
Bytes 60780
60780 fetch-S085-index.mdx
e505931a59faa9a6685be195ccf42fcd8e3ddb9bb1d9e52f95d3b6c862cb83a5  fetch-S085-index.mdx
```

### Candidate S087 discovery page

```sh
timeout 5s date -u && timeout 90s curl --location --max-time 75 --connect-timeout 15 --silent --show-error --dump-header fetch-S087.headers --output fetch-S087-plugins.mdx --write-out 'HTTP %{http_code}\nURL %{url_effective}\nBytes %{size_download}\n' https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/plugins.mdx && timeout 5s wc -c fetch-S087-plugins.mdx && timeout 5s sha256sum fetch-S087-plugins.mdx
```

Observed output:

```text
Fri 23 Oct 2026 06:45:57 AM UTC
HTTP 200
URL https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/plugins.mdx
Bytes 4371
4371 fetch-S087-plugins.mdx
39afa29948069c9e8d95ba812ee1701535912a7e5ce3ed7fef5d4ba6d7521fd3  fetch-S087-plugins.mdx
```

Both hashes match the respective hashes claimed in the lane source record / candidate, but the fetched bytes above are the evidence. In the remainder, `B` means `/fast/scratch/hyaku/kotoba-r57a3/A3Shipopencode/fetch-S085-index.mdx`; `D` means `/fast/scratch/hyaku/kotoba-r57a3/A3Shipopencode/fetch-S087-plugins.mdx`. Line numbers refer to these unmodified fetched bytes. Quotes are contiguous, byte-exact substrings, no markdown stripped and no line breaks folded; each quote is at most 25 words.

## Findings and strongest counterexamples

### 1. Tip source ranges do not cover two listed parts; candidate fixes this

At tip, `corpus/knowledge/plugin-manifests-round57.md:48` lists tools and runtime hooks but cites only:

```text
S085 `index.mdx:10-22,214-235,414-445,610-627,865-892,1768-1786`
```

The actual Tools section begins at `B:961`; Hooks begins at `B:1335`. Neither is inside that source-lines cell. This is a citation-completeness defect, not evidence that tools/hooks are invented: the live page does document them. `corpus/SOURCES.md:98` already points to both sections, but that does not make the narrower entry-row range hold their text.

Candidate patch `:107` adds `961-996,1335-1418`, correctly repairing this omission. Its other range extensions close code examples: agent `235→236`, MCP `627→631`, skills `892→894`. The original shorter ranges still contain their substantive prose/examples; these extensions are not repairs for changed live line numbers. The independently fetched S085 bytes have the recorded hash.

Impacted axis: depth/evidence traceability. Smallest correction: retain the candidate's tools/hooks citations, adding the new ranges identified below only for newly explicit claims.

### 2. “Registers agents” is stronger than this page's agent contract

Tip `SKILL.md:123` groups agents with things “registered in code”; tip entry `:48` and candidate patch `:107` say the module “registers agents”. The source instead documents transforms over existing agents. `B:223` says:

```text
Register a transform to inspect, update, remove, or select the default agent.
```

The complete displayed `AgentEditor` interface at `B:256-262` has `list`, `get`, `default`, `update`, and `remove`, with no `add`; the example updates `build`, selects its default, and removes `legacy` (`B:226-235`). Contrast the explicit additions for commands (`B:426`), skills (`B:881`) and tools (`B:980`).

Strongest local counterexample: a reader taking “registers agents” as permission to create an agent with `editor.add` will find no such operation in the cited agent editor. This is an ambiguity/unsupported creation implication; I did not execute the API and do not claim that every other possible way of adding agents is impossible.

Impacted axis: depth. Smallest safe correction: distinguish **transforms of existing agents (update/remove/default selection)** from registration of commands, skills and tools.

### 3. Candidate's global folder is supported; its “only file its docs call a manifest” is overbroad

Candidate patch `:25` correctly adds `~/.config/opencode/plugins/`. `D:57` says:

```text
Global plugins use the same discovery layout under the OpenCode config directory.
```

The literal path is at `D:60`. The candidate's `D:44-60` range therefore holds this claim. Keep this discovery fact in the location prose (candidate `:54-55`) rather than treating it as an instruction-bearing part.

`B:1770-1773` explicitly labels `package.json` as a minimal manifest. This supports the candidate entry's bounded wording, but not the SKILL cell's universal “the only file its docs call a manifest”. A search of the two fetched pages finds the manifest label in this publishing section; that is not a sweep of all OpenCode documentation. No client-wide absence claim is made here.

There is also a direct contradiction within the proposed SKILL row: its unchanged manifest cell says “no JSON manifest” and its unchanged action says “there is no manifest to read”, while its new ship cell names the documented JSON manifest. Restricting the noun to a plugin-specific schema could be a defensible distinction, but the smallest evidence-positive correction avoids the negative claim altogether (exact text below).

Impacted axes: depth and consistency/calibration. Preserve the observed package-manifest fact; delete the universal and categorical negatives.

### 4. Direct session text submission is absent from both lists

`B:810-816` documents another code-mediated instruction path, separate from registering a command or installing a runtime hook. `B:810` says:

```text
Send user prompts, transient generation requests, commands, or synthetic messages.
```

The following examples submit text through `session.prompt`, `session.generate` and `session.synthetic`. Neither the tip's nor candidate's entry-row citations include this section. A plugin can therefore contribute model-facing text without that text arriving as a skill/agent/command artifact or a registered hook. The recommended wording explicitly includes these calls, without claiming they create another on-disk instruction-file format.

The existing “runtime hooks” category already covers prompt and system-instruction mutation, so these are not invented additional packaged components. Naming them makes the instruction path explicit: prompt edits and attachments at `B:1354-1375`; outgoing system instructions at `B:1394-1409`. In particular, the source example adds a policy-file attachment (`B:1360`) and pushes a text system part (`B:1409`).

I did not classify the page's provider, storage, VCS, worktree or local/Git reference APIs (`B:681-725`) as automatically loaded instructions. Their existence alone does not establish that claim. This review is not an assertion that the entire client documents no other instruction surface.

Impacted axis: depth. Smallest safe addition: identify session text submission and spell out the instruction-bearing hooks, without inventing a rules/context-file package schema.

## Exact cells to land — my own wording

Use the following **identical ship-cell text in both tables**. This removes the agent-creation implication, includes the directly documented text-submission path, and bounds the package-manifest statement. The global discovery fact remains valid in the candidate's location prose, not in this cell.

```text
JavaScript/TypeScript code can register commands, MCP server configuration, skills and tools; transform existing agents (update/remove/default selection); send session prompts, transient generation requests and synthetic messages; and install runtime hooks that edit incoming prompts and outgoing system instructions; published packages use `package.json` as a minimal manifest
```

### Exact old → new substitutions

1. `SKILL.md:123`, tip ship cell — OLD:

```text
agents, commands, MCP configuration, skills, tools and runtime hooks, registered in code
```

→ NEW: the shared ship-cell text above.

2. Candidate patch `:25`, SKILL ship cell — OLD:

```text
agents, commands, MCP configuration, skills, tools and runtime hooks, registered in code; global folder `~/.config/opencode/plugins/`; a published package's `package.json` is the only file its docs call a manifest
```

→ NEW: the shared ship-cell text above.

3. `corpus/knowledge/plugin-manifests-round57.md:48`, tip ship cell — OLD:

```text
a JavaScript/TypeScript module that registers agents, commands, MCP configuration, skills, tools and runtime hooks in code; a published package carries a `package.json`
```

→ NEW: the shared ship-cell text above.

4. Candidate patch `:107`, entry ship cell — OLD:

```text
a JavaScript/TypeScript module that registers agents, commands, MCP configuration, skills, tools and runtime hooks in code; a published package carries a `package.json`, which the build guide calls a minimal manifest
```

→ NEW: the shared ship-cell text above.

5. Tip entry `:48`, source-lines cell — OLD:

```text
S085 `index.mdx:10-22,214-235,414-445,610-627,865-892,1768-1786`
```

Candidate patch `:107`, source-lines cell — OLD:

```text
S085 `index.mdx:10-22,214-236,414-445,610-631,865-894,961-996,1335-1418,1768-1786`; S087 `plugins.mdx:44-60`
```

→ NEW for either starting point:

```text
S085 `index.mdx:10-22,223-236,256-262,414-445,618-631,810-816,873-894,971-996,1335-1418,1770-1786`; S087 `plugins.mdx:44-60`
```

### Evidence for every part of the recommended cell

| Part | Evidence in newly fetched bytes |
|---|---|
| JavaScript/TypeScript code | `B:10-18` shows the TypeScript module and default plugin export; `D:46-47` explicitly documents discovery of direct `.ts` and `.js` files and immediate plugin-package directories. |
| Commands | `B:422`: “Register commands with a transform. The executor receives the session, prompt attachments, and requested delivery mode.” The added command and submitted prompt text appear at `B:425-438`. |
| MCP server configuration | `B:618`: “Plugins manage MCP servers only through transforms.” Configuration addition/replacement/update/removal is documented at `B:618-631`. This does not assert that arbitrary bundled MCP instructions load independently of the configured server. |
| Skills | `B:873`: “Register a transform to inspect, add, update, or remove skills.” `B:881-886` includes a name, description, path and instruction-bearing `content` string. |
| Tools | `B:971`: “Register, update, and remove tools with a synchronous transform, including in Promise plugins.” `B:975-995` supplies namespace/description, tool description, schema and executor. |
| Existing-agent transforms | `B:223-235` describes and demonstrates updates/removal/default selection; complete editor contract at `B:256-262`. Wording does not claim creation of new agents. |
| Session prompts / transient generation / synthetic messages | `B:810-816` explicitly documents and demonstrates each path. These are runtime submissions from code, not separately packaged file types. |
| Runtime hooks / incoming prompts | `B:1335-1346` registers hooks; `B:1354-1375` changes incoming prompt text, files and selected skills. |
| Outgoing system instructions | `B:1396`: “Modify assembled system instructions, messages, tools, or request options immediately before model dispatch.” The system-text addition is at `B:1409`. `B:1420-1421` limits these edits to the outgoing model call, not persisted history/configuration. |
| Published package / minimal manifest | `B:1770-1773` uses the minimal-manifest label and names `package.json`; JSON body at `B:1774-1785`. The statement does not claim every local module needs this file. |

### Necessary adjacent wording consistency

These two exact substitutions keep the SKILL row from contradicting the documented manifest fact. They leave the first manifest token `.opencode/plugins/` unchanged and do not propose changing frozen counting rules.

Manifest cell, OLD (tip and candidate):

```text
`.opencode/plugins/` (no JSON manifest: a plugin is a JavaScript/TypeScript module)
```

→ NEW:

```text
`.opencode/plugins/` (global: `~/.config/opencode/plugins/`; published packages carry `package.json`)
```

Action cell, OLD (tip and candidate):

```text
Review the module code; there is no manifest to read
```

→ NEW:

```text
Review the module code and, for published packages, `package.json`
```

Evidence: `B:10-22,1770-1786`; `D:44-60`. The candidate's entry-level change from “no JSON manifest” to a distinction about a plugin-specific manifest is directionally better, but this seat has not independently performed a docs-tree/changelog/corpus absence sweep and does not certify that negative claim. Its positive package-manifest statement is independently verified above.

## Disposition

Do not land the candidate SKILL ship cell verbatim. Keep its repaired tools/hooks ranges and independently supported discovery/package facts; narrow agent wording and manifest scope, and add the omitted direct session-text path. This report makes no claim that the frozen C1 predicate improves: its stated limits exclude ship-cell completeness (`plans/round-57.md:42-43`; entry `:73-74`). No runtime behavior or no-harm test is reported as passed.
