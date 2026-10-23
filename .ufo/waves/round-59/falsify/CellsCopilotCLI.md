Result: HOLDS — both Copilot CLI Events spans are actual lifecycle events, and every scoped Hook config, Action, entry-note claim and line reference is supported by the frozen source bytes.

## Scope and axes

Attacked: `SKILL.md:130` and `corpus/knowledge/hook-files-round59.md:26,44-46` at `c63ccc6823e1f6a8577acbb43d19551eadbbee9a`. Primary axis: depth (correct configuration scope, event identity, actionable caveat). Calibration is relevant to distinguishing documentation from runtime evidence. This is a scoped semantic review, not C1 admission, a six-client verdict, or a saturation claim.

The frozen addendum explicitly separates printed identifiers from event semantics (`plans/round-59.md:93-98`). I applied that semantic route without changing the counter, rule, targets, or row identity.

## Source opened and provenance

Opened the existing committed snapshot `.ufo/waves/round-59/snapshots/S099.page`, including the surrounding surface distinction, event heading/list, and configuration examples. URL: https://docs.github.com/en/copilot/concepts/customizations/hooks.md . No new network fetch was needed or performed.

Original capture provenance, not a fetch claimed by this seat: `corpus/SOURCES.md:111` and `.ufo/waves/round-59/build/SrcCopilotCLI.md:38-44` record HTTP 200, 8,428 bytes, SHA-256 `23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4`, and this original `date -u` output:

```text
Fri Oct 23 09:34:55 AM UTC 2026
```

Independent local reads below reproduced the byte count and full digest. The reviewed working-tree files matched the assigned data revision in the path-limited read-only diffs recorded below.

## Exact page text

Each quotation is an unchanged contiguous excerpt of at most 25 words. Markdown bytes are preserved; nothing was stripped or folded.

Q1 — S099 snapshot line 28, repository location:

```text
For Copilot CLI and Copilot cloud agent, you can define repository hooks in `.github/hooks/*.json`.
```

Q2 — S099 snapshot line 28, personal location and the entry's complete quotation:

```text
Copilot CLI also supports personal hooks in `~/.copilot/hooks/*.json`.
```

Q3 — S099 snapshot line 32, what the following names represent:

```text
These are examples of Copilot CLI hook events. Copilot cloud agent supports a subset:
```

Q4 — S099 snapshot line 34:

```text
* **sessionStart**: Executed when a new agent session begins or when resuming an existing session.
```

Q5 — S099 snapshot line 37:

```text
* **preToolUse**: Executed before the agent uses any tool (such as `bash`, `edit`, `view`).
```

Q6 — S099 snapshot line 26, Action caveat:

```text
Do not assume that the same events, input, or output work unchanged across surfaces.
```

Q7 — S099 snapshot line 26, scope of that caveat:

```text
The configuration and examples below describe hooks for Copilot CLI and Copilot cloud agent.
```

## Every Events-cell span

`SKILL.md:130` has exactly two backticked Events spans; neither is an incidental identifier or a tool name.

| Span, in row order | Ruling | Evidence and reference check |
|---|---|---|
| `preToolUse` | event | Q3 expressly introduces Copilot CLI hook events; Q5 defines this one as execution before tool use. Parenthetical `S099 :37` resolves exactly. It also appears as a hook-definition key at snapshot line 106. |
| `sessionStart` | event | Q3 plus Q4 explicitly identify the lifecycle event and its start/resume behavior. Parenthetical `S099 :34` resolves exactly. It also appears under the JSON `hooks` object at snapshot lines 52-53. |

Unruled spans: none. Spans ruled `not an event`: none. The prose list, rather than mere occurrence in a JSON example, is the decisive semantic support.

## Every field claim and parenthetical reference

| Attacked claim | Ruling | Exact support / reference resolution |
|---|---|---|
| SKILL Hook config: `~/.copilot/hooks/*.json` is personal Copilot CLI configuration | supported | Q2 says precisely this. `S099 :28` is correct; it is not a cloud-agent personal-path claim. |
| SKILL Hook config: repository hooks share the VS Code row's folder pattern | supported | Q1 supplies `.github/hooks/*.json`; the adjacent `SKILL.md:129` uses that exact pattern. Independently, `.ufo/waves/round-59/snapshots/S098.page:59` prints the same repository-root pattern. The S099 `:28` reference supports the Copilot side of the comparison. |
| SKILL Action: check event support on each surface before relying on it | supported | This is the direct operational consequence of Q6, scoped by Q7. The row does not claim the CLI list works unchanged in cloud agent or VS Code. `S099 :26` resolves exactly. |
| Entry table `:26`: personal path and quotation | supported | Hook token matches Q2 exactly; the entire quoted sentence is byte-identical to the second sentence of S099 line 28. No quote shaping is needed. |
| Entry note `:44-45`: repository and personal paths | supported | Q1 and Q2 establish both locations. Parenthetical `hooks.md:28` resolves to the committed S099 snapshot line 28. |
| Entry note `:45-46`: personal path leads because the repository pattern is the VS Code row's token; E5 rationale | supported as an internal selection explanation, not vendor provenance | `SKILL.md:129-130` demonstrates the chosen tokens; `plans/round-59.md:37,42,70` defines first-token selection, shared-token disqualification, and this exact frozen choice. This sentence does not assert that GitHub ranks personal hooks above repository hooks. |
| Entry note `:46`: events include `sessionStart` and `preToolUse` | supported | Q3-Q5. Parenthetical `:34,37` maps in the entry's stated order, exactly. |

Unsupported claims: none in the assigned cells/note. Overstated claims: none found in this slice. Every page-line parenthetical in the assigned row and entry note resolves to the content claimed.

## Strongest local counterexample attempted

Candidate attack: the page is titled for GitHub Copilot generally, so its event names or personal hook path might belong only to another surface, making the CLI row false despite textual counter matches.

The local evidence defeats this attack: Q3 explicitly calls these Copilot CLI hook events; Q2 explicitly assigns personal hooks to Copilot CLI; Q1 separately assigns repository hooks to CLI and cloud agent. Q3 warns that cloud agent supports only a subset, and Q6 supplies the cross-surface warning that the Action cell preserves. Thus neither event identity nor personal scope was inferred from a shared product name.

A second reading attack is that choosing the personal token to avoid E5 silently removes repository support. It does not: the Hook config cell retains repository scope by reference to the adjacent row, and the entry note prints both paths. The rule-driven choice is disclosed as such, not attributed to GitHub as precedence.

Smallest safe correction: none to the assigned row or entry note. Keep the existing cross-surface caveat and explicit documentation-only limit. No semantic correction needs to be routed into the lesson from this seat. This conclusion does not establish hook runtime behavior or the full round's no-harm judgment.

## Commands, observed output, and limits

Read-only identity command (exit 0; no output):

```text
timeout 20s git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin diff --no-ext-diff c63ccc6823e1f6a8577acbb43d19551eadbbee9a -- SKILL.md corpus/knowledge/hook-files-round59.md .ufo/waves/round-59/snapshots/S099.page plans/round-59.md verifiers/check_hook_files.py
```

Supplemental source-registry/adjacent-pattern identity command (exit 0; no output):

```text
timeout 20s git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin diff --no-ext-diff c63ccc6823e1f6a8577acbb43d19551eadbbee9a -- corpus/SOURCES.md .ufo/waves/round-59/snapshots/S098.page
```

Local provenance command (exit 0):

```text
timeout 10s sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/snapshots/S099.page && timeout 10s wc -lc /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/snapshots/S099.page && timeout 10s date -u
```

Observed output:

```text
23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4  /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/snapshots/S099.page
 165 8428 /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/snapshots/S099.page
Fri 23 Oct 2026 09:52:30 AM UTC
```

No counter, self-test, hook, client CLI, mutation, sandbox runtime, or canonical judge was executed by this seat. No tools were installed or updated. Only this report was written; no lane content, Git index, jj state, fleet file, or sibling file was changed.

Report: .ufo/waves/round-59/falsify/CellsCopilotCLI.md
