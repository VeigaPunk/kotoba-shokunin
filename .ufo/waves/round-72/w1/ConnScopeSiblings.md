# ConnScopeSiblings — round-72 wave 1: PROVINCE scope check of the assimilation theme

Seat: ConnScopeSiblings (leaf; no subagent dispatch). Verdicts on the two staged entries
of the round-72 assimilation (`plans/round-72.md` § Assimilation: one theme — resident-index
versus on-demand rung; two entries). Read-only; no lane/sibling/merge file touched; no tool
installed; no web fetch performed.

## Verdicts (first)

| staged entry | sources | verdict | ground |
|---|---|---|---|
| `knowledge/corpus/knowledge/skill-vs-always-on-boundary.md` | S261–S264 | **admit-as-craft** | substance = vendor-stated decision-boundary rules for authors (kotoba craft); one Vercel-number paragraph (L27–31) is kengaku measured-capability ground — excluded from the SKILL.md rule text, kept only as historical provenance pointer |
| `knowledge/corpus/knowledge/context-rot-and-always-on-context.md` | S248, S254, S255, S256 | **admit-as-craft (surgical)** — flip from expected refusal | the craft rule survives without the measured figures: `always-resident surface = index, not payload; on-demand small enough`. The Chroma degradation curve and the Vercel percentages are kengaku measured-capability ground → refuse-sibling-scope for exactly those passages; S255/S256 spec budgets are tier-A format facts (kotoba craft ground) |

For every entry: the surviving craft rule is independent of the measured figures; the figures
are the part kengaku's adjacent ground owns. Neither entry is chousa/kumitate/kama scope.

## 1. Where the staged inputs come from (observed)

Commands (read-only):
- `read /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-72/assimilation/`
  → `reg-ids` (S001–S213), `staged-ids` (S203–S390), `collisions` (S203–S213),
  `quarantine-slice-full.txt` (13 kotoba rows), `guard-proof/`.
- `read /home/vgpnk/Projects/shokuknow/merge/kotoba/MERGE-REPORT.md` → "proposed knowledge
  entries: 88"; both staged files are in the package's knowledge list (skill-vs-always-on-
  boundary.md round6; context-rot-and-always-on-context.md round5).
- `read` of both staged files (full) and `read SOURCES.append.md:51-68:raw` for rows
  S248/S254/S255/S256/S261–S264.

## 2. Entry 1 — skill-vs-always-on-boundary.md

Content: what belongs in a skill versus an always-on file versus a one-off prompt (the three-
rung instruction ladder). This is the lane's own Core surface (`PROVINCE.md` Core: "Agent-
definition, always-on (AGENTS.md-class) and dispatch-prompt craft"; the A4 rung rule of C1).

Vendor-stated boundary sentences (byte-exact from `sed -n` of the staged file; dropped bytes:
none — lines quoted whole):

- Factory (S262), L17–19: `Use skills when instructions are too specific for always-on AGENTS.md` (9 words).
- pi (S263), L20–22: `Use a skill when a workflow needs more context than a prompt template but does not need a new executable integration point.` (22 words).
- Hermes (S264), L33–35: `house authoring standards (≤60-char description, the standard section order, Hermes-tool framing, no invented commands)` (14 words).
- Letta (S261), L42–43: `Skills are portable across Letta, Codex, Claude Code, Hermes Agent, OpenClaw, and other compatible agents.` (15 words).
- The ladder rule as written, L49–53: `a skill is for instructions that are too specific to sit in an always-on file and too shaped to be a one-off prompt, and that do not need to be executable integrations. Below that line, use a prompt. Above it, use AGENTS.md and accept the cost.`

Measured passage, L27–31 (excluded from craft text): `Round 5's Vercel eval put numbers on the comparison the ladder implies: a compressed always-on index reached 100% where a skill reached 53% without an instruction to use it and 79% with one.` — capability measurement, kengaku ground (see §4); already held by the lane as its round-5 finding (`corpus/SOURCES.md` L241/L283: "Vercel — AGENTS.md outperforms skills in our agent evals (56% non-invocation; compressed index at 100%)"), so it is a historical provenance pointer, not new owned evidence.

Surviving craft rules without the figures: the ladder rule (L49–53); Hermes house-standard clauses (≤60-char description cap against spec 1024; "no invented commands" safety clause, L33–39); Letta portability claim (L41–46).

Registry rows S261–S264 (`SOURCES.append.md` L65–68): all `docs` tier B, status `mined`, quote cells are boundary/standard statements (no measurements); used-by includes `skill-vs-always-on-boundary.md` for all four. No scope objection.

## 3. Entry 2 — context-rot-and-always-on-context.md

Measured content (kengaku ground, refused as kotoba-owned evidence):
- Chroma (S254), L11–13: `model performance degrades as input length increases, often in surprising and non-uniform ways` (13 words) — measured degradation curve.
- Vercel (S248), row L52: `In 56% of eval cases, the skill was never invoked.` (11 words); `A compressed 8KB docs index embedded directly in AGENTS.md achieved a 100% pass rate, while skills maxed out at 79%` (21 words).
- Entry L30–31: `an on-demand skill that the agent may never invoke (56% in Vercel's eval)`.

Craft content that survives without any figure:
- Spec budgets: S255 (one-pager), entry L28–29: `only the name and description of each skill (~50-100 tokens per skill)` (12 words); S256 (client-implementation guide), entry L29–30: catalog ~50–100 tokens per skill, instructions under 5000 tokens on activation, resources only when referenced.
- The synthesis, L32–36: `the always-resident surface should be an index, not a payload, and the on-demand surface should be small enough that a failed invocation costs little.` (24 words); L41–43: `keep a pointer resident and the payload retrievable.`

These sentences state what a skill author should ship (resident index, retrievable payload) —
kotoba craft; they do not require Chroma's or Vercel's numbers. The plan's expected refusal
(measured degradation curve = kengaku's adjacent ground) therefore flips to admit-as-craft for
the rule sentences, with the measured passages refused as sibling scope.

Row notes: S254 is tier B `mined`, used-by `context-rot-and-always-on-context.md`; S255/S256
are tier A `mined`, format facts (agentskills.io spec pages; S256 same page as held S002 but a
listed section). No scope objection to the rows themselves; only the measurement passages must
not enter kotoba's SKILL.md rule text as kotoba-owned evidence.

## 4. Sibling boundaries (located quotes, byte-exact from `sed -n`)

kengaku (measured capability effects stay; craft implications route to kotoba):
- `sed -n '138p' /home/vgpnk/Projects/shokunin/kengaku-shokunin/PROVINCE.md`:
  `kotoba | prompt- and skill-craft rules — measured capability effects of prompt format stay here; reusable craft implications route out (r7 tools-without-system, r11/r12 ack-intent findings)` (14 words).
- `sed -n '3p' .../kengaku-shokunin/SKILL.md` (arbitration clause; dropped bytes: rest of the line after the clause):
  `kotoba owns prompt and skill craft (kengaku keeps only measured capability effects)` (14 words).
- `sed -n '59p' .../kotoba-shokunin/PROVINCE.md` (kengaku row, snippet; dropped: rest of row):
  `kengaku keeps measured capability effects of prompt format, kotoba owns the craft rules` (14 words).

kumitate (routes prompt/skill craft to kotoba):
- `sed -n '28p' .../kumitate-shokunin/PROVINCE.md`:
  `Local model serving and endpoints → kama. Prompt and skill craft → kotoba. Research method → chousa.`

chousa (owns the research method, not findings or claims):
- `sed -n '3p' .../chousa-shokunin/PROVINCE.md`: `deep-research method (調査) — the reusable craft of source research.`
- `sed -n '10,12p' .../chousa-shokunin/PROVINCE.md`: `model-quality or evaluation claims (→ kengaku)`.

kama (serving-plane identity/health only):
- `sed -n '29p' .../kama-shokunin/corpus/knowledge/cross-lane-scope.md`:
  `Kotoba owns the instruction/agent surface and its model/fallback wording; kama owns independent verification of the target endpoint.` (17 words).

Neither staged entry touches kama's endpoints, kumitate's dispatch runtime, or chousa's research
method; both are instruction-surface craft with a measurement component that kengaku's split
claims.

## 5. Non-scope flags surfaced for the L1/counter seats

- C1 predicate (b): every cited S### must have `used-by` naming the A4 entry path
  (`corpus/knowledge/resident-index-and-rungs-round72.md`). Current registry cells:
  S248 used-by = {skill-invocation-is-the-bottleneck.md, context-rot-and-always-on-context.md};
  S254 used-by = {context-rot-and-always-on-context.md}; S255/S256 used-by do **not** list
  context-rot-and-always-on-context.md nor any resident-index entry. If the A4 entry cites
  these ids, the used-by cells must be updated at landing or C1(b) fails (registration
  mechanics, not scope).
- Quarantine cross-reference: S168 (same Vercel URL as staged S248) was refused round 68 as
  `payload-absent` (`corpus/lessons/round-68.md` L103: "refused — the quoted span was not
  located on the page this round fetched"). Staged S248 carries a different quote cell
  ("In 56% of eval cases, the skill was never invoked."); A4(d) will require that quote
  word-bounded in a committed snapshot — verifier/counter seat, not scope.

## 6. Process compliance

Read-only seat: lane `read`/`grep`/`sed -n`/directory listings; no edits anywhere, no git/jj
mutation, no installs (no tooling directive triggered), no web fetch (snapshots not verified —
not this seat's gate). `[INFERENCE]` none: every claim above is quoted from fetched local bytes
or observed file listings.
