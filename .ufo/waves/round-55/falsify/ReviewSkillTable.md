Result: MIXED — the seven forms and most "starts with"/"holds" anchors match the cited documentation, but both ScoutPlanWalk notes are unreflected (no raw-text ordering clause anywhere; opencode's action cell contradicts itself on turn granularity), the intro's "who chose" clause misstates the limit, and two minor cell defects remain.

Scope: `SKILL.md:193-205` at `f0e6b695b746775823b65a8c45de7d50ea33e84f` (heading, intro `SKILL.md:195`, header `:197-198`, seven rows `:199-205`). Read-only review; nothing executed, no lane file edited. Cross-read: `corpus/knowledge/explicit-invocation-round55.md`, `corpus/knowledge/trigger-miss-proxy-round6.md:10-19`, `corpus/README.md:98,129-133,152`, `verifiers/check_explicit_invocation.py` docstring + ERRATUM v2, SOURCES S065–S071 (`corpus/SOURCES.md:78-84`), seat reports `Src*.md`, `.ufo/waves/round-55/build/ScoutPlanWalk.md` (the dispatch target).

## Findings by severity

### F1 (medium) — ScoutPlanWalk note B unreflected: "the turn" is the wrong set-aside unit, and the opencode row contradicts itself

Evidence: walk `ScoutPlanWalk.md:123-128` (note B) records live session `ses_ed42d6c31ffejc2Q8Hp3GMCzn7`: user row seq 629 carries `@tower` plus a `skills[]` attach; assistant row seq 630 — same turn — calls the `skill` tool for `shokunin`, a model-chosen load. The precise set-aside is the named skill's activation, not the turn.

Landed cells: six of seven say "Set the turn aside as explicit" (`SKILL.md:199-202,204-205`). The opencode cell is the live contradiction: `SKILL.md:205` says set the turn aside when the prompt holds `@` plus a skill ID, then says "the model's own `skill` tool calls are the implicit ones" — in the observed session both occurred in one turn, so the cell tells the measurer to both exclude the turn and count that `shokunin` call implicit. Unactionable as written. Claude Code `:199` half-covers it ("count only the other activations as implicit") but still discards the whole turn. The intro `SKILL.md:195` and `corpus/README.md:130-131` also say "turns". Gemini CLI `:203` is the only row already at activation granularity.

### F2 (medium) — ScoutPlanWalk note A unreflected: no "match on raw text before cleaning" clause in intro, entry, or any cell

Evidence: the lane's only implicit-trigger recipe cleans user text before matching — `trigger-miss-proxy-round6.md:13-15` strips slash-command tokens (`/skill:godspeed`, `/ufo`, "these are invocation verbs, not router intent") and injected directive blobs. The walk (`ScoutPlanWalk.md:116-121`, note A; restated `:110-112`) observed that neither the table intro nor the entry says the form match must run on raw text; a measurer reusing the recipe verbatim deletes every `/name` marker first, and slash-invoked turns fall into the implicit complement — exactly the contamination the table exists to remove. Landed cells say "its user text" / "its prompt" / "the message" (`:199-205`); none says raw or ordering. `$` and `@` forms survive that cleaning (walk `:62`), so the defect bites the four `/`-form rows: Claude Code, VS Code, Copilot CLI, Cursor.

### F3 (medium) — Intro misstates the who-chose limit

`SKILL.md:195`: "it says nothing about who chose the skill unless the user typed it." Two readings, both wrong: (a) "unless the user typed it" implies a typed form does establish who chose it — falsified on the lane's own store: the walk's 8-file sample of omp sessions found fleet dispatches injecting `/skill:godspeed` into user-role text (`ScoutPlanWalk.md:61,66-73`); entry finding 4 and README `:131-133` both record "who typed the form" as still-not-held; (b) as tautology ("typed by the user = user chose") it adds nothing. Fix below.

### F4 (low) — "starts with" vs "holds": five rows verified, Cursor vague

- Claude Code `:199` "starts with" — defensible: S065 documents typing `/skill-name` as a leading command form (`skills.md:547`).
- VS Code `:201` "starts with … even when task text follows" — correct: the picker inserts the command at position 0; S067's example shows trailing context (`agent-skills.md:287`).
- Codex `:200` "holds `$` plus name" — correct: `$setup-demo-app` sits mid-sentence in the S066 prompt (`eval-skills.md:148`).
- Copilot CLI `:202` "holds `/` plus name" — correct: `/frontend-design` is mid-sentence (`add-skills.md:128`).
- opencode `:205` "holds `@` plus ID" — correct: a mention anywhere (`skills.mdx:201`).
- Cursor `:204` "when the message used the skill's `/name`" — "used" is not a match operator; the docs show a picker entry that "attaches once when you press Enter" (`SrcCursor.md:5,10`, `cursor-skills.md:29`), i.e. an embedded form, so "holds" fits the documentation better than either the vague "used" or "starts with".
- Gemini CLI `:203` correctly refuses a user-typed form (none documented; `activate_skill` is a model call).

### F5 (low) — opencode metadata key misnamed in the "What it does" cell

`SKILL.md:205` says `` `autoinvoke: false` ``; the documented key is `opencode/autoinvoke: false` — entry `:28`, S071 quote "`opencode/autoinvoke: false` only hides the skill from the model's available list" (`skills.mdx:142`, seat `Srcopencode.md:9`), and the held round-51 entry `skill-overlap-levers-round51.md:24` (`metadata["opencode/autoinvoke"]`).

### F6 (low) — Walk note C's corroborating signal not folded into the opencode row

The v2 store records the same explicit act in the user row's attached `skills[]` array (`ScoutPlanWalk.md:146-152`) — a second, harder-to-strip signal. Optional strengthening; the assignment asked for A and B, and C is noted for completeness.

## Actionability check (SKILL.md alone)

Every cell except opencode's names a concrete match plus a disposition and is executable without the sources (Codex's "installed skill name" needs no external table). opencode fails actionability via the F1 contradiction; Cursor is weakly actionable ("used" undefined). All seven cells remain non-empty under the counter's rule, so none of the rewrites below affects the frozen predicate.

## Draft replacement text (all single-line edits; SKILL.md stays 598 lines ≤ 600)

`SKILL.md:195` (intro):
```
An implicit-trigger measure (Frontier *Implicit-intent fidelity*) must first set aside activations where a skill was invoked by name, matching the form on the raw user text before the join recipe strips slash tokens and directive blobs (`trigger-miss-proxy-round6.md`). The form is what the user typed, or the model's load call, as each client documents it; it records that the skill was named, not who named it. Basis: `corpus/knowledge/explicit-invocation-round55.md` (S065–S071), checked by `verifiers/check_explicit_invocation.py`.
```

`:199` Claude Code — action cell → `Set the skill's activation aside as explicit when the raw user text starts with its `/name`; count the turn's other activations as implicit`

`:200` Codex — action cell → `Set the skill's activation aside as explicit when the raw user text holds `$` plus an installed skill name; only the rest can test description routing`

`:201` VS Code — action cell → `Set the skill's activation aside as explicit when the raw user text starts with its `/name`, even when task text follows`

`:202` Copilot CLI — action cell → `Set the skill's activation aside as explicit when the raw prompt holds `/` plus a skill name; the rest are the description-routed turns`

`:203` Gemini CLI — unchanged (already activation-granular and correct).

`:204` Cursor — action cell → `Set the skill's activation aside as explicit when the raw message holds `/` plus a skill name; a flagged skill can only appear in such turns`

`:205` opencode — what cell: `` `autoinvoke: false` `` → `` `opencode/autoinvoke: false` ``; action cell → `Set only the named skill's activation aside as explicit when the raw prompt holds `@` plus a skill ID (the user row's `skills[]` attach record corroborates it); the model's other `skill` tool calls stay implicit`

(Note A is fully covered by the intro rewrite; the per-row "raw" reinforcements above keep each cell self-contained.)

## Residual risk and gaps

- I did not refetch any client page; "documented form" judgements cite the lane's landed rows and seat reports, not my own fetches — sufficient for reviewing cell-vs-entry consistency, not for re-verifying the pages.
- The counter is untouched by all proposed edits (action-cell wording is unjudged beyond non-empty); no counter run was needed or performed for this review.
- F6's `skills[]` signal and the walk's live-store finding (round-6 SQL dead on the opencode v2 schema) are beyond this table's remit; recorded here as routed context, not defects of the rows.
- If the L1 prefers minimal churn, F1+F2 alone repair the measurer-facing defect; F3–F6 are precision fixes on already-acceptable cells.

Report: .ufo/waves/round-55/falsify/ReviewSkillTable.md
