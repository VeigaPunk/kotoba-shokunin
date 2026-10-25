# ScribeEntryRung — round 72, wave 1 (build)

## Verdict

**Draft delivered: `corpus/knowledge/resident-index-and-rungs-round72.md` (85 lines, 8 sourced facts,
16 quoted spans all matched word-bounded against committed snapshots) plus the `SKILL.md` § Instruction
surfaces pointer in two costed forms.** The entry is a re-grounding, not a copy: three of the staged
entry's quote cells would fail C1(d) as written (markdown links and one code span break contiguity),
two staged claims are wrong (Letta names **five** agents, not six; pi's page mentions neither
`AGENTS.md` nor MCP), and the strongest source for the `index` half of the A4 rule is Hermes
`S264-hermes-skills.md:610-612` — a line the staged entry never uses. Nothing committed was touched;
no gate was run by this seat.

Artifacts (lane-relative):

| file | bytes | sha256 | note |
|---|---|---|---|
| `.ufo/waves/round-72/w1/build/ScribeEntryRung/resident-index-and-rungs-round72.ENTRY.md` | 10 626 | `e58e483053d6f0150615cea2b85429bc9f02e0336bb9e1c8bcc6b74408a99b77` | the entry alone, 85 lines, ready to `cp` to `corpus/knowledge/` |
| `.ufo/waves/round-72/w1/build/ScribeEntryRung/resident-index-and-rungs-round72.md` | 15 545 | `89d85836cacf02c95721bf853ce933ab9431f6d537c5770b297a646b0d59f490` | delivery wrapper: entry block, two `SKILL.md` diff blocks, integration notes |
| `.ufo/waves/round-72/w1/ScribeEntryRung.md` | — | — | this report |

## Findings

### 1. The lane holds no rung-selection rule — the entry is genuine expansion, not a repeat

```
$ grep -rn 'middle rung\|one-off prompt\|three rungs\|three-step' --include=*.md corpus/ SKILL.md
(no output; exit 1)
$ git grep -n 'middle rung\|one-off prompt\|three rungs\|three-step' \
    c69711ee08279609374d895bb0f3c8c18ccf15c9 -- 'corpus/*.md' 'SKILL.md'
(no output)
```

The `ground:` line of the entry records the nearest held ground: the surface maps
(`corpus/knowledge/instruction-surface-census-round13.md`, `alwayson-rule-files-round53.md`,
`command-files-round58.md`) and `corpus/knowledge/anatomy-and-compression.md:76` — "One authoritative
home per fact; the skill keeps the pointer." (dropped from the line: the leading `   bailian-cli). `
fragment and the three-space indent). Those say *where* a surface is read; none says *which* surface a
piece of guidance belongs in.

### 2. Three staged quote cells fail a literal snapshot check; the replacements pass

Command (scratch, all six candidates against the committed snapshots):

```
$ python3 - <<'PY'   # re.sub(r'\s+',' ') on each snapshot, then (?<!\w)QUOTE(?!\w)
...
S262  MISS  10w  staged cell (11-word prefix)
S262  HIT   21w  entry cell (full sentence + code span)
S261  MISS  10w  staged cell (standard sentence)
S261  HIT   15w  entry cell (portability sentence)
S264  MISS  14w  staged cell (house standard)
S264  HIT   11w  entry cell (parenthetical)
PY

(The labels are the script's own; the staged Factory cell measures 10 words, and the script prints
`MISS` for it because of the code span — the label was written before the count was measured.)
```

Per-row, on the *staged* cells:

| row | staged cell | verdict against its snapshot | why |
|---|---|---|---|
| S262 | `Use skills when instructions are too specific for always-on AGENTS.md` | **fails** as a contiguous string | `S262-factory-droid-skills.md:9` carries `` `AGENTS.md` `` as a code span |
| S261 | `The Letta agent harness implements the open Agent Skills standard.` | **fails** | `S261-letta-skills.md:15` carries `[Agent Skills](https://agentskills.io)` |
| S264 | `house authoring standards (≤60-char description, …)` | **fails** | `S264-hermes-skills.md:123` carries `[house authoring standards](#skillmd-format)` |

The cells this draft uses instead all match word-bounded on the snapshots: the full 21-word Factory
sentence *with* the code span, the 15-word Letta portability sentence, and the 11-word Hermes
parenthetical. `ExecSrcHermes` reached the same conclusion independently ("C1(d) will fail on S264 as
written unless the counter normalizes markup and newlines"). **A counter that strips markdown links
and code spans before matching would accept the staged cells; one that does not must take the cells in
the entry.** This is the single highest-risk item for C1.

### 3. All four vendor quotes are live today

```
$ curl -sS -L -o p-<md5>.html -w '%{http_code} %{size_download}' <url>   # four URLs
https://docs.factory.ai/cli/configuration/skills        -> 200 341251
https://raw.githubusercontent.com/badlogic/pi-mono/...  -> 200 4793
https://hermes-agent.nousresearch.com/docs/user-guide/features/skills -> 200 206631
https://docs.letta.com/letta-code/skills/               -> 200 92885
```

and the entry's own `recheck:` one-liner, run from the extracted file:

```
$ bash recheck.sh     # the backticked command of the entry's recheck: line, verbatim
1 1 1 1 exit=0
```

Located quotes, copied from the fetched bytes (word counts 7–22; shaping named per row):

- Factory, `S262-factory-droid-skills.md:9` — "Use skills when instructions are too specific for
  always-on \`AGENTS.md\`, too structured for a one-off prompt, and useful enough to reuse."
  (21 words; the code span is the snapshot's own, nothing dropped.)
- pi, `S263-pi-skills.md:5` — "Use a skill when a workflow needs more context than a prompt template
  but does not need a new executable integration point." (22 words; dropped: the next sentence about
  bundling scripts.)
- Hermes, `S264-hermes-skills.md:610-612` — "memory stores small durable facts that should always be in
  context, while skills store longer procedures that should load only when relevant" (22 words;
  dropped: the two line breaks and the sentence's `Skills and memory work together …` prefix).
- Hermes, `S264-hermes-skills.md:636-637` — "Skills also do not restate what is already loaded every
  turn (the repo's \`AGENTS.md\`, tool schemas)." (16 words; dropped: one line break).
- Hermes, `S264-hermes-skills.md:643-644` — "They warn; they never block a write." (7 words; dropped:
  one line break).
- Letta, `S261-letta-skills.md:15` — "Skills are portable across Letta, Codex, Claude Code, Hermes
  Agent, OpenClaw, and other compatible agents." (15 words; dropped: the preceding sentence and its
  `[Agent Skills](https://agentskills.io)` link).

None of these is claimed `byte-exact` in the entry; each is a located quote matched after whitespace
collapse, and the entry says so in § Limits.

### 4. Correction — Letta names five agents, not six

```
$ sed -n '15p' .ufo/waves/round-72/snapshots/S261-letta-skills.md
The Letta agent harness implements the open [Agent Skills](https://agentskills.io) standard. Skills are portable across Letta, Codex, Claude Code, Hermes Agent, OpenClaw, and other compatible agents.
```

Named agents: Letta, Codex, Claude Code, Hermes Agent, OpenClaw — **five**, then "other compatible
agents". The staged entry (`skill-vs-always-on-boundary.md`, § Letta) says "six named agents";
`ExecSrcLetta` independently marks that claim "absent — the page names five". The entry's F8 and its
Limits both say five. This is a propagated staged error the L1 should not land.

### 5. Correction — pi supports the middle rung only, and says nothing about the always-on file

```
$ grep -c 'AGENTS.md' .ufo/waves/round-72/snapshots/S263-pi-skills.md
0
$ grep -c 'MCP' .ufo/waves/round-72/snapshots/S263-pi-skills.md
0
```

`ExecSrcPi` reports the same two zeros and adds that "executable integration point" is defined in the
sibling `docs/extensions.md`. Consequence carried into the entry: the always-on half of the boundary
rests on Factory (F1, F2) and Hermes (F5, F6), and the entry says so in § Limits rather than
attributing it to pi.

### 6. The strongest `index` source is Hermes, not the staged entry

```
$ sed -n '610,612p' .ufo/waves/round-72/snapshots/S264-hermes-skills.md
Skills and memory work together in the self-improvement loop: memory stores
small durable facts that should always be in context, while skills store longer
procedures that should load only when relevant. The background review can
$ sed -n '636,637p' .ufo/waves/round-72/snapshots/S264-hermes-skills.md
extended in place rather than accumulated one file per session. Skills also do not
restate what is already loaded every turn (the repo's `AGENTS.md`, tool schemas).
```

This is the rung rule and its non-duplication half stated by a vendor, not inferred — and it is the
one sentence that makes the A4 box's `index` token honest without touching the measured figures.
`ExecSrcHermes` flagged the same lines as "new ground for `resident-index-and-rungs-round72.md` (A4)".
pi's `S263-pi-skills.md:3` supplies the mechanism ("Pi advertises each available skill by name and
description, then loads its full instructions only when the task calls for them." — 21 words, nothing
dropped), which is the entry's F4.

### 7. Factory publishes the decision table the lane needs, in five rows

```
$ sed -n '106,114p' .ufo/waves/round-72/snapshots/S262-factory-droid-skills.md
Use a different surface when the guidance has another shape:

| Surface | Best for |
| :------ | :------- |
| `AGENTS.md` | Always-on repository instructions, commands, conventions, and safety rules. |
| Skill | Reusable workflow Droid can choose or the user can invoke. |
| Custom slash command | Simple user-invoked prompt or executable shortcut. |
| Custom droid | Specialized subagent with its own prompt, model, and tool policy. |
| MCP server | External tools and services Droid can call. |
```

The staged entry uses only the boundary sentence and never this table. The entry's F2 adds it: it names
the always-on rung's own contents ("Always-on repository instructions, commands, conventions, and
safety rules." — 8 words, nothing dropped) and the two neighbouring rungs (slash command = the prompt
rung; MCP server = pi's "executable integration point"). `ExecSrcFactory` notes the page writes no
"rung" word and enumerates more surfaces than three; the entry's rule 3 says the ladder is the lane's
name for the boundary, not the vendor's.

### 8. Entry shape and the `SKILL.md` budget arithmetic

```
$ wc -l .ufo/waves/round-72/w1/build/ScribeEntryRung/resident-index-and-rungs-round72.ENTRY.md
85 .ufo/waves/round-72/w1/build/ScribeEntryRung/resident-index-and-rungs-round72.ENTRY.md
$ wc -l -c SKILL.md
  600 72688 SKILL.md
$ awk 'NR==65{print NR": "length($0)}' SKILL.md
65: 82
```

Validation run on the extracted entry: `lines: 85 <=90: True`; header order `source: ×4 →
verified-at: → recheck: → ground:` `True`; token counts `{'prompt': 14, 'always-on': 16, 'skill': 28,
'index': 4}`; `quotes: 16 unmatched: []`; `table rows: 8`.

`SKILL.md` is exactly 600 lines, so the pointer costs what it costs: the primary form fuses into line
65 (82 characters today, wraps to two lines) = **+1 line**; the alternative three-row table =
**+6 lines**. Both are in the deliverable with their diff. The L1 must free at least the pointer's own
lines before adding the four C1 boxes, which are the larger cost.

### 9. Lane state and seat agreement

```
$ git rev-parse HEAD
e61fd294c2e1cdd16d594b57b310254183ace1e7
$ git diff --stat c69711ee08279609374d895bb0f3c8c18ccf15c9..HEAD | tail -2
 plans/round-72.md                                  | 204 +++++
 24 files changed, 2695 insertions(+)
$ git status --porcelain SKILL.md corpus/ verifiers/ | wc -l
0
```

HEAD is the wave-1 spec commit on top of the frozen plan; the diff over the plan's base touches only
`.ufo/waves/round-72/**` and `plans/round-72.md`, and no committed `SKILL.md`, `corpus/` or
`verifiers/` file is modified in the working tree. All four source-opening seats had landed when the
final draft was written and none contradicts a quote: `ExecSrcFactory` ("verbatim prefix of snapshot
`S262-factory-droid-skills.md:9`"), `ExecSrcPi` ("located verbatim"), `ExecSrcHermes` ("verbatim in
it"), `ExecSrcLetta` (portability sentence "byte-exact in raw `.md` and raw `.html`"). Two of their
findings changed the draft (findings 4 and 5 above).

## Gates

None run by this seat, by design: no C1 counter exists yet (`verifiers/check_author_rules.py` lands
with the claim), a lane gate must not run in a bare `/tmp` clone, and a scribe seat does not verify
the L1's integration. What the L1 must run after landing, from a fleet-shaped sandbox:

- `python3 -B verifiers/check_author_rules.py --rev <rev>` → must print `author-facing rules in
  SKILL.md N of 4` with `N == 4`; the base reads `0 of 4`, exit 1.
- `python3 -B verifiers/verify_skill_checklist.py --json` → the new A4 box must be mapped in
  `verifiers/checklist-baseline.json` (an unmapped box FAILs), and `trigger.line_budget` must stay
  green at 600 lines.
- `python3 -B verifiers/verify_corpus_integrity.py` / `verify_corpus_independent.py` → both are
  already red at the base (5 DRIFT); adding this file moves `tracked_files` and `report_total` again,
  so the baseline needs the same landing as the index row.

## Touched surfaces

- Wrote `.ufo/waves/round-72/w1/build/ScribeEntryRung/resident-index-and-rungs-round72.md` and
  `…/resident-index-and-rungs-round72.ENTRY.md` (both new, under the wave's `build/`).
- Wrote this report.
- Scratch `/tmp/k72w1-ScribeEntryRung.8W4U` created and **deleted** before return (four page fetches,
  four markdown exports, `entry.md`, `recheck.sh`).
- No committed lane file, no fleet file, no sibling lane, no `shokuknow` write, no git write, no jj
  command. No fixture repo was created, so the `git -C "$D"` rule never applied.
- Observed, not mine: `git status --porcelain` lists two untracked files under a committed directory —
  `verifiers/fixtures/oc2-v2.1.4-anchor.txt` and `verifiers/fixtures/oc2-v2.1.4-decoy-moved.txt`
  (the C2 counter's fixtures, from a sibling seat). The L1 decides whether they land; my writes are
  only under `.ufo/waves/round-72/w1/`.

## Out of scope

C2 (substrate re-pin), C3 (tip battery), the quarantine hand-checks, the counters and every control
world are other seats'. The measured degradation curve in the second staged entry
(`context-rot-and-always-on-context.md`) is deliberately not absorbed: it is capability measurement on
kengaku's adjacent ground, and the entry's Scope says so.

## Tooling

Nothing installed, nothing upgraded; no package manager was invoked. Every command in this report ran
under 2 s; no process exceeded the 4-process / 120 s contention cap.

## Unobserved

- No client's loading, routing or refusal behaviour was observed by this seat; the entry is
  documentary and says so.
- I did not run any lane gate, so I make no claim about the tip battery or the C1 counter's behaviour;
  the `0 of 4` base figure is the plan's, not mine.
- The four snapshots are the seats' fetches; I re-read their bytes and matched quotes against them, but
  I did not re-fetch into the snapshots directory or verify their sha256 manifests.
