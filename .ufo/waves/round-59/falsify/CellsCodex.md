Result: MIXED — Both Codex Events spans and the hook-location claims hold; the Action and entry note overstate the documented default trust gate as an unconditional guarantee.

## Scope and evidence identity

- Seat: CellsCodex; impacted axis: **depth**. This is a source-level semantic review, not a runtime test or a canonical judgment.
- Reviewed `SKILL.md:128` and `corpus/knowledge/hook-files-round59.md:24,36-39,62` at data revision `c63ccc6823e1f6a8577acbb43d19551eadbbee9a`.
- Applied the frozen semantic-seat requirement in `plans/round-59.md:93-98`: rule every Events span, without changing the counter, row rule, or targets.
- Opened the committed S097 snapshot, `.ufo/waves/round-59/snapshots/S097.page`. All source line numbers below refer to those exact bytes. Source URL: https://learn.chatgpt.com/docs/hooks.md.
- No fresh HTTP fetch was needed: the assignment expressly permits the pinned snapshot. The original fetch receipt is `.ufo/waves/round-59/build/SrcCodex.md:5-18`, not a fetch performed by this seat:

```text
Fri Oct 23 09:35:05 AM UTC 2026
HTTP 200 https://learn.chatgpt.com/docs/hooks.md
curl_exit=0
47133 /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/snapshots/S097.page
57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92  /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/snapshots/S097.page
```

My read-only snapshot identity command, exit 0:

```sh
timeout 30s sha256sum .ufo/waves/round-59/snapshots/S097.page
```

```text
57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92  .ufo/waves/round-59/snapshots/S097.page
```

This equals `corpus/SOURCES.md:109`. My separate read-only pinning command, exit 0:

```sh
timeout 30s bash -c 'date -u; wc -c .ufo/waves/round-59/snapshots/S097.page; git --no-optional-locks diff --exit-code c63ccc6823e1f6a8577acbb43d19551eadbbee9a -- SKILL.md corpus/knowledge/hook-files-round59.md corpus/SOURCES.md plans/round-59.md .ufo/waves/round-59/snapshots/S097.page .ufo/waves/round-59/build/SrcCodex.md; rc=$?; printf "reviewed_files_diff_exit=%s\n" "$rc"; exit "$rc"'
```

```text
Fri Oct 23 09:52:44 AM UTC 2026
47133 .ufo/waves/round-59/snapshots/S097.page
reviewed_files_diff_exit=0
```

## Events: every backticked span ruled

There are exactly two backticked spans in the Codex Events cell at `SKILL.md:128`.

| Span | Ruling | Exact page text and context |
|---|---|---|
| `PreToolUse` | **event** | `S097.page:21` says `Hooks run at different points in a conversation:`. Line 23 labels the second column `Hooks`; line 25 puts `PreToolUse` in that column for `During a turn`. Line 751 is `### PreToolUse`; lines 753-755 describe its tool interception behavior. This is a named lifecycle event, not merely an identifier appearing elsewhere. |
| `SessionStart` | **event** | The same Hooks table, line 27, places `SessionStart` under `When a session or subagent starts`. Line 648 is `### SessionStart`; line 650 says: `` `matcher` is applied to `source` for this event. `` Line 669 uses `"hookEventName": "SessionStart"`. |

The parenthetical `(S097 :25, :27)` is **supported**, in the stated order. The entry note's `(:25,27)` at `corpus/knowledge/hook-files-round59.md:38` is also **supported**. No event-name correction is needed.

## Hook config: every claim and citation

| Claim | Ruling | Exact page text |
|---|---|---|
| `~/.codex/hooks.json` is a Codex hook configuration location | **supported** | Line 30: `## Where Codex looks for hooks`; line 44: ``- `~/.codex/hooks.json` ``. |
| The lead path is user-scoped | **supported** | Line 44 prints the home-directory path; lines 58-60 distinguish project-local hooks from user and system hooks. No claim that this is the sole hook source is made. |
| Repository layers are also supported | **supported** | Line 32: `Codex discovers hooks next to active config layers in either of these forms:`; line 46: ``- `<repo>/.codex/hooks.json` ``. |
| Inline `config.toml` tables are also supported | **supported** | Line 35: ``- inline `[hooks]` tables inside `config.toml` ``; line 45 prints the user `config.toml` location. Line 47 additionally prints the repository `config.toml` location. |
| Entry: hooks live next to active config layers, as `hooks.json` or inline `[hooks]` tables | **supported** | Line 32 above; line 34: ``- `hooks.json` ``; line 35 above. |
| Entry: the page lists `~/.codex/hooks.json` first among the four most useful locations | **supported** | Line 42: `In practice, the four most useful locations are:`; line 44 is the first bullet. |

Both location references — `(S097 :30-46)` in `SKILL.md:128` and `(hooks.md:30-46)` in the entry at line 37 — support the actual claims made. The fourth location is on page line 47, outside that range, but neither reviewed sentence claims to enumerate all four; this is not an unsupported citation.

The entry table quote at line 24 is **supported**. It is the continuous excerpt from page lines 38-44, starting at `a default` within line 38 and ending at the first location bullet. As disclosed at entry line 62, source line breaks and blank lines are folded to spaces; no non-whitespace bytes are removed. The exact resulting 22-word excerpt is:

> a default `hooks/hooks.json` file. See [Build plugins](https://developers.openai.com/plugins/build/plugins#bundled-mcp-servers-and-lifecycle-hooks) for the plugin packaging rules. In practice, the four most useful locations are: - `~/.codex/hooks.json`

The opening fragment concerns plugin packaging; the subsequent locations heading and bullet independently support the user-file claim. It does not establish that the user file is itself a plugin bundle, and the entry does not make that claim.

## Action: default supported, unconditional guarantee overstated

### What holds

`Put the hook here` is **supported** as routing advice by the documented location at page line 44. It does not say putting a file there is sufficient to enable an unmatched, disabled, or untrusted hook.

The line-19 citation is textually accurate. Exact page line 19:

> - Non-managed hooks must be reviewed and trusted before they run.

Thus `(S097 :19)` in `SKILL.md:128` and `(:19)` in the entry at line 39 genuinely support the **normal review/trust workflow**. The reference is not fabricated or misnumbered.

### Concrete source-level counterexample

The Action says a non-managed hook runs **only after** review and trust; the entry repeats that non-managed hooks **must** be reviewed and trusted before running, without qualifying the invocation or workflow.

But the same pinned page expressly documents this exception at lines 76-78, quoted verbatim with original line breaks and no shaping (24 words):

```text
For one-off automation that already vets hook sources outside Codex, pass
`--dangerously-bypass-hook-trust` to run enabled hooks without requiring
persisted hook trust for that invocation.
```

Consequently, an invocation using that documented automation path does not require persisted Codex hook trust. The row's unconditional wording cannot safely be read as an invariant that Codex always enforces its review/trust gate. This is **overstated**, not wholly unsupported.

Important limit: this is a documentation counterexample, not an executed bypass. It does **not** establish that the page recommends unvetted hooks; the page explicitly describes external vetting. Nor does it establish that no review or trust of any kind occurred outside Codex. It establishes that the unconditional in-client gate implication needs a default-workflow qualification.

The same unqualified sentence is propagated in `corpus/SOURCES.md:109`'s `teaches` cell. That is the same issue, not an independent finding.

### Smallest safe correction

Have the integrator qualify the existing statements; do not alter paths, event names, evidence bytes, counter logic, row rule, or targets:

- `SKILL.md:128`, Action: **Put the hook here; by default, non-managed hooks require review and trust before running (S097 :19, :64-78).**
- Entry lines 38-39: **By default, non-managed hooks must be reviewed and trusted before they run (`:19,64-78`).**
- If carrying the teaching forward, qualify the identical SOURCES teaching under the registry's append-only correction convention, rather than leaving two conflicting strengths of claim.

No need to teach users how to invoke the exception in the compact SKILL row. Making the default explicit is sufficient; the extended citation exposes its documented boundary.

## Impact and no-harm boundary

- **Depth:** real configuration and event grounding survives. The defect is an absolute trust-enforcement implication unsupported by the full cited page, not fabricated hook knowledge.
- This is a fixable wording defect, not a reason to redesign the frozen counter or claim a different target. Canonical acceptance remains outside this seat.
- [INFERENCE] The proposed qualification preserves routing advice and the review recommendation while avoiding a false unconditional guarantee. It leaves both Events spans and all source identities unchanged; it adds no second authority or runtime dependency.
- No lane code executed, no verifier or mutation run, no other runtime invoked, and no lane Git/jj writes. Only this report was written. No tool installed or updated.
