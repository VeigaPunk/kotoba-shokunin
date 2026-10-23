# ExecInstancesA2 — frozen E2f instances

## Scope and files

Lane write: this report only, `.ufo/waves/round-62/w1/ExecInstancesA2.md`. Scratch runner: `/fast/scratch/hyaku/kotoba-r62/ExecInstancesA2/probe_instances.py` (not lane evidence). No counter, lane product, fleet, sibling, `.ufo/state`, or jj/git-index file was changed.

## Committed `action_conjunct` behavior established before probing

Read `verifiers/check_scoped_rules.py:972-1040`; the source digest measured immediately before execution was `5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91`, matching the round-62 frozen pin.

- `content_words` removes backticked spans before tokenizing (`check_scoped_rules.py:972-977`). `page_words` scans the whole page with backticks included (`:990-996`).
- `action_conjunct` calculates the cited-line forward threshold as `ceil(2|W|/3)` (minimum 2), checks page-word support, then requires `ceil(|L|/3)` reverse support (minimum 1) (`:980-987`, `:1010-1040`).
- This function has no raw-tokenizer load/event-claim check and no compound-purpose/section check. Its signature also has no scope-key argument; G5 key-on-line is not implemented inside this function. Both fixtures use the otherwise-eligible Claude Code/S103 row; the event claim cites line 194 and passes its support fractions, while W6-sib cites line 209 and is rejected by the reverse fraction. Each raw cited line contains the row's canonical backticked `paths` key.

The line used as the eligible Claude Code action/key line is S103:194: `Rules can be scoped to specific files using YAML frontmatter with the `paths` field. These conditional rules only apply when Claude is working with files matching the specified patterns.`

## Frozen Python input literals

These are the exact `action_conjunct(lines, cell, line, page_text)` inputs used. The W6-sib-style instance is the published MutA2 cell on the otherwise-eligible Claude Code/S103 row, citing its line 209.

```python
CASES = [
    (
        "E2f-event-token-backticked",
        ".ufo/waves/round-60/snapshots/S103.page",
        194,
        "The `InstructionsLoaded` event loads rules only when Claude works with specific matching files and specified patterns. (S103 :194)",
    ),
    (
        "E2f-W6-sib-style",
        ".ufo/waves/round-60/snapshots/S103.page",
        209,
        "Create the rule file in the project and add frontmatter so it loads only for the matching files. (S103 :209)",
    ),
    (
        "F6-compound-purpose-bound",
        ".ufo/waves/round-60/snapshots/S106.page",
        60,
        "Create instructions files with glob syntax and organize the copies in the project directory. (S106 :60)",
    ),
    (
        "eligible-Claude-S103",
        ".ufo/waves/round-60/snapshots/S103.page",
        194,
        "Scope rules to specific files using YAML frontmatter; apply only when matching specified patterns. (S103 :194)",
    ),
    (
        "eligible-VS-Code-S105",
        ".ufo/waves/round-60/snapshots/S105.page",
        329,
        "Use multiple instruction files per topic and apply them selectively (S105 :329)",
    ),
    (
        "eligible-Copilot-S106",
        ".ufo/waves/round-60/snapshots/S106.page",
        60,
        "Create a path-specific instruction file with an applyTo glob; use glob syntax to specify the files or directories the instructions apply to (S106 :60)",
    ),
    (
        "eligible-Cursor-S108",
        ".ufo/waves/round-60/snapshots/S108.page",
        131,
        "Use globs to scope a rule to specific files or directories. Separate multiple patterns with commas. (S108 :131)",
    ),
]
```

The first fixture's raw backticked `InstructionsLoaded` token is absent from the counter's `content_words` output; the remaining words clear both support fractions. It is a raw event/load claim, so the proposed G7 must reject it. The published W6-sib-style fixture is rejected by the committed counter's reverse-support fraction (8/34; need 12), not by a G7 implementation. F6 is the compound-purpose control/bound. The four eligible cell literals are the Action cells at `SKILL.md:141,143-144,146` with their original citation lines.

## Exact run and retained output

Counter command was executed from `/home/vgpnk/Projects/shokunin/kotoba-shokunin`; `date -u` and command:

```sh
date -u && python3 -B /fast/scratch/hyaku/kotoba-r62/ExecInstancesA2/probe_instances.py; rc=$?; printf 'exit=%s\n' "$rc"; exit "$rc"
```

Exact stdout and exit:

```text
Fri 23 Oct 2026 08:55:19 PM UTC
counter sha256 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91
== E2f-event-token-backticked .ufo/waves/round-60/snapshots/S103.page:194
cell='The `InstructionsLoaded` event loads rules only when Claude works with specific matching files and specified patterns. (S103 :194)'
content_words=['claude', 'event', 'files', 'loads', 'matching', 'patterns', 'rules', 'specific', 'specified', 'works']
forward=8/10 need=7; reverse=8/15 need=5
verdict=ACCEPTED; reasons=[]
== E2f-W6-sib-style .ufo/waves/round-60/snapshots/S103.page:209
cell='Create the rule file in the project and add frontmatter so it loads only for the matching files. (S103 :209)'
content_words=['create', 'file', 'files', 'frontmatter', 'loads', 'matching', 'project', 'rule']
forward=6/8 need=6; reverse=8/34 need=12
verdict=REJECTED; reasons=["A2: the cited line's 34 content word(s) are supported 8 time(s) by the action cell at line 209 (need >= 12): the line does not state the claim"]
== F6-compound-purpose-bound .ufo/waves/round-60/snapshots/S106.page:60
cell='Create instructions files with glob syntax and organize the copies in the project directory. (S106 :60)'
content_words=['copies', 'create', 'directory', 'files', 'glob', 'instructions', 'organize', 'project', 'syntax']
forward=6/9 need=6; reverse=7/14 need=5
verdict=ACCEPTED; reasons=[]
== eligible-Claude-S103 .ufo/waves/round-60/snapshots/S103.page:194
cell='Scope rules to specific files using YAML frontmatter; apply only when matching specified patterns. (S103 :194)'
content_words=['apply', 'files', 'frontmatter', 'matching', 'patterns', 'rules', 'scope', 'specific', 'specified', 'using', 'yaml']
forward=11/11 need=8; reverse=11/15 need=5
verdict=ACCEPTED; reasons=[]
== eligible-VS-Code-S105 .ufo/waves/round-60/snapshots/S105.page:329
cell='Use multiple instruction files per topic and apply them selectively (S105 :329)'
content_words=['apply', 'files', 'instruction', 'multiple', 'selectively', 'topic']
forward=6/6 need=4; reverse=6/11 need=4
verdict=ACCEPTED; reasons=[]
== eligible-Copilot-S106 .ufo/waves/round-60/snapshots/S106.page:60
cell='Create a path-specific instruction file with an applyTo glob; use glob syntax to specify the files or directories the instructions apply to (S106 :60)'
content_words=['apply', 'applyto', 'create', 'directories', 'file', 'files', 'glob', 'instruction', 'instructions', 'path', 'specific', 'specify', 'syntax']
forward=12/13 need=9; reverse=9/14 need=5
verdict=ACCEPTED; reasons=[]
== eligible-Cursor-S108 .ufo/waves/round-60/snapshots/S108.page:131
cell='Use globs to scope a rule to specific files or directories. Separate multiple patterns with commas. (S108 :131)'
content_words=['commas', 'directories', 'files', 'globs', 'multiple', 'patterns', 'rule', 'scope', 'separate', 'specific']
forward=9/10 need=7; reverse=9/9 need=3
verdict=ACCEPTED; reasons=[]
exit=0
```

**Observed verdict:** the committed counter accepts the backticked event attack, which is the one surviving E2f instance, and rejects the published W6-sib instance on its existing reverse-support fraction (not G7). Thus this pair yields the plan's expected single survivor. F6 is accepted and remains the declared compound-purpose bound. All four distinct eligible Action cells are accepted.

## Successor predicate wording and boundary

The r62 successor form in `plans/round-62.md:73-85` is G5 key-on-line **and** G7 raw-tokenizer event-claim checking; it explicitly leaves F6/G9 as a declared surviving bound. The measured MutA2 proposal (`.ufo/waves/round-61/wave/MutA2.md:360-368`) gives the exact guard wording:

- **G7 claim-span:** “if the cell contains a raw load/attach/fire/read or event token, every content word of the cell occurs on one page line (raw tokenizer).” This must inspect raw bytes so the backticked `InstructionsLoaded` event is not erased before claim detection.
- **G9 clause-span (the proposed fuller guard, not part of the r62 successor's frozen G5+G7 form):** “every clause (split on `;`, `.`, ` and `) with ≥2 content words has all its content words present in the cited line's section (nearest heading through the next heading of the same or higher level), plural/`-ed`/`-ing` tolerant.” This would reject F6; the r62 successor must instead declare F6 as surviving if it does not implement G9.

The eligible-cell measurements support keeping the successor's forward/reverse fractions rather than demanding every non-claim Action word on one line, consistent with `plans/round-61.md:241-254` and MutA2's positive controls.

## Limits, risks, blockers

This is an arm-level measurement of the committed `action_conjunct`, not a full CLI, matrix, or successor run. I did not run `--self-test`; those gates belong to integration. LSP access was not exposed in this seat's tools; symbol behavior was established by reading the implementation and importing/calling the exact committed function. No tool was installed or updated.

installs: no installs.
blockers: none.
Attacked: E2f backticked event survivor and W6-sib rejection via reverse support; retained F6 bound and four eligible Action positives.
