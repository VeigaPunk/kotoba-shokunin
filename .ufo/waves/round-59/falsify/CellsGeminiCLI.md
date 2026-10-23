Result: HOLDS — Both Gemini CLI Events spans are lifecycle events used as such on S100, and the scoped Hook config, Action, and entry-note claims are supported.

## Scope and evidence identity

Attacked: `SKILL.md:131` and `corpus/knowledge/hook-files-round59.md:27,47-49` at data commit `c63ccc6823e1f6a8577acbb43d19551eadbbee9a`. This is a semantic source review on **depth**, not a C1 predicate, admission, or axis-score judgment. The freeze addendum (`plans/round-59.md:93-98`) leaves the counter unchanged and assigns actual event meaning to this seat.

Primary page: https://geminicli.com/docs/hooks/best-practices.md, reopened as committed `.ufo/waves/round-59/snapshots/S100.page`. No fresh HTTP request was made by this seat. Original fetch provenance is recorded in `build/SrcGeminiCLI.md:7-19` under the same round directory: `Fri Oct 23 09:34:48 AM UTC 2026`; HTTP 200; 17,650 bytes; SHA256 `fb44fbcfaccc3cdb7895d989f3808bed66cfa6516411535c4c4d9077d242e7bc`. Those HTTP details are the existing receipt, not a new observation. The source registry independently records them at `corpus/SOURCES.md:112`.

Read-only command, exit 0, no output:

```sh
timeout 30s git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin diff c63ccc6823e1f6a8577acbb43d19551eadbbee9a -- SKILL.md corpus/knowledge/hook-files-round59.md corpus/SOURCES.md plans/round-59.md .ufo/waves/round-59/snapshots/S100.page
```

Thus the inspected content matches the assigned revision for these paths. Independent byte measurements, combined command exit 0:

```sh
timeout 30s sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/snapshots/S100.page && timeout 30s wc -c /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/snapshots/S100.page && timeout 30s date -u '+%Y-%m-%dT%H:%M:%SZ'
```

Observed output:

```text
fb44fbcfaccc3cdb7895d989f3808bed66cfa6516411535c4c4d9077d242e7bc  /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/snapshots/S100.page
17650 /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/snapshots/S100.page
2026-10-23T09:52:33Z
```

## Every Events span

There are exactly two backticked spans in the Gemini Events cell; its `S100 :31` reference is plain text, not another span.

| Span | Ruling | Evidence of use as an event, not merely a printed identifier |
|---|---|---|
| `BeforeTool` | **event** | S100 `:31` explicitly calls it a frequently run hook; `:178` uses it as the value of `hook_event_name`; `:306-307` places it under the `hooks` configuration map. |
| `AfterModel` | **event** | S100 `:31` explicitly calls it a frequently run hook; the “Use appropriate events” section (`:70-77`) explicitly describes when it fires. |

Exact page text follows. Each source quote is at most 25 words; these are complete source lines, preserving Markdown, indentation, and physical newlines. No bytes were stripped.

S100 `:31`:

```text
hooks that run frequently (like `BeforeTool` or `AfterModel`).
```

S100 `:178`:

```text
  "hook_event_name": "BeforeTool",
```

S100 `:72`:

```text
Choose hook events that match your use case to avoid unnecessary execution.
```

S100 `:76-77`:

```text
- **`AfterModel`**: Fires after **every chunk** of LLM output. Use this for
  real-time redaction, PII filtering, or monitoring output as it streams.
```

The page need not contain an exhaustive event catalog to support these two events. Neither row nor note claims that `AfterModel` is once-per-turn, a session-start event, or interchangeable with `AfterAgent`.

## Every field claim and parenthetical reference

| Location / claim or reference | Ruling | Exact support |
|---|---|---|
| `SKILL.md:131`, Hook config `.gemini/settings.json` | **supported** | S100 `:413` names that exact file as containing hooks. |
| Same cell, project scope and `(project, S100 :413)` | **supported** | The same source line explicitly says “a project”; no user/system scope is inferred. |
| Same row, Events `(S100 :31)` | **supported** | Both names occur together in the hook context quoted above. Additional semantic evidence is `:72,76-77,178`. |
| Same row, Action: verify the source of project hooks before enabling them; `(S100 :442)` | **supported** | The source gives that recommendation verbatim, including “before enabling them.” The row does not claim a technical approval gate. |
| Entry table `:27`, config token and quote | **supported** | Its quote is the complete, unchanged S100 `:413` line below. |
| Entry note `:47`, project path and `(best-practices.md:413)` | **supported** | Same exact path and project scope at S100 `:413`. |
| Entry note `:48`, page prints both events and `(:31)` | **supported** | Both are printed and used as hooks at S100 `:31`; they are not arbitrary code symbols. |
| Entry note `:48-49`, source-verification recommendation and `(:442)` | **supported** | S100 `:442` explicitly supplies it. |
| Entry note `:49`, session events are on a separate hooks page, which is not a row | **supported with separate-page evidence, not attributed to S100** | Existing fetched `https://geminicli.com/docs/hooks.md` bytes, independently reopened below, list `SessionStart` and `SessionEnd` at `:40-41`. An exact-URL search of `corpus/SOURCES.md` returned `No matches found`; S100 is the best-practices URL. |

S100 `:413`:

```text
When you open a project with hooks defined in `.gemini/settings.json`:
```

S100 `:442`:

```text
**Verify the source** of any project hooks or extensions before enabling them.
```

For the entry note's separate-page statement, opened `/fast/scratch/hyaku/kotoba-r59/CensusGeminiCLI/geminicli.com_docs_hooks.md.body:30-52`. Existing fetch provenance: `w0/CensusGeminiCLI.md:36`, `Fri 23 Oct 2026 09:02:48 AM UTC`, HTTP 200, 8,341 bytes, SHA256 `a06a92438d3110690e875d61feef49a850d82eda618bb837146a1a7ff7a4c8d9`. No fresh fetch claimed. Source `:36` says:

```text
Hooks are triggered by specific events in Gemini CLI's lifecycle.
```

Source `:40`, complete line, unchanged:

```text
| `SessionStart`        | When a session begins (startup, resume, clear) | Inject Context         | Initialize resources, load context           |
```

Source `:41`, complete line, unchanged:

```text
| `SessionEnd`          | When a session ends (exit, clear)              | Advisory               | Clean up, save state                         |
```

Independent supporting-cache measurement, exit 0:

```sh
timeout 10s date -u && timeout 10s sha256sum /fast/scratch/hyaku/kotoba-r59/CensusGeminiCLI/geminicli.com_docs_hooks.md.body && timeout 10s wc -c /fast/scratch/hyaku/kotoba-r59/CensusGeminiCLI/geminicli.com_docs_hooks.md.body
```

Observed output:

```text
Fri 23 Oct 2026 09:53:26 AM UTC
a06a92438d3110690e875d61feef49a850d82eda618bb837146a1a7ff7a4c8d9  /fast/scratch/hyaku/kotoba-r59/CensusGeminiCLI/geminicli.com_docs_hooks.md.body
8341 /fast/scratch/hyaku/kotoba-r59/CensusGeminiCLI/geminicli.com_docs_hooks.md.body
```

This is a page/registry distinction, not a claim that the client documents nothing about a topic.

## Strongest counterexample considered

**Attack:** Could “before enabling” falsely imply that project hooks cannot execute until manually approved? S100's own execution sequence contradicts that stronger interpretation: a new identity generates a warning (`:418-419`), then execution (`:420-421`), then trusted marking (`:422`). Exact `:420-421`:

```text
4. **Execution**: The hook is executed (unless specific security settings block
   it).
```

This does **not** break the landed row: its Action is the source's explicit safety recommendation, not an assertion that verification is enforced by the client. The note also makes no per-hook approval or unconditional-execution guarantee. Promoting the recommendation into a runtime trust gate would be an unsupported depth/safety-calibration regression; it has not happened here.

## Smallest safe correction and no-harm

**No correction required to these assigned cells or note.** Preserve the narrow project scope, exact event spellings, and recommendation wording. The separate catalog corroborates only the note's navigation statement; it is not substituted for S100 in either event ruling. No frozen counter, rule, targets, source identities, or population changes are proposed. No unavoidable tradeoff is presented for canonical judgment.

After-column: depth's source/field semantics survive this attack; runtime execution, whole-C1 scoring, and other-axis no-harm are not asserted by this seat. No lane code, counter, test, client CLI, or other judgment runtime was executed; no sandbox was needed. No tools installed or updated. Only this report was written.

Report: .ufo/waves/round-59/falsify/CellsGeminiCLI.md
