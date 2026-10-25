# ConnectorSiblingScan — round 69 wave 1 (kotoba, hyaku run 6, attempt 2)

Seat: leaf connector. Scope: read-only scan of the 20 sibling lane repos for anything on this
round's ground — (a) same-named skill precedence, (b) per-client rule-file/trust maps, (c) a
sibling claiming part of C1/C2/C3. No sibling file was written. Nothing in the lane was modified;
the one proposed text change was tested in a `/tmp` `git clone --shared` sandbox (below).

Lane tip at scan: `a238989a96cb0d2b939679126b832d75b861ca6e` (plan + counters + base controls),
with the C1 entry draft and its S203–S207 rows uncommitted in the working tree.

## Method (commands, all read-only)

- Sibling heads: `for d in *-shokunin; do git -C "$d" rev-parse HEAD; done`.
- Scope-surface sweep for precedence: `grep -nE 'precedence|same[- ]named|name collision|shadow'
  "$d/SKILL.md" "$d/PROVINCE.md"` over all 20 lanes; then the same pattern plus `skill` over
  `corpus/knowledge`, `corpus/lessons`, `corpus/README.md`, `MINT.md`, `SCORECARD.md`.
- C1 client tokens: `grep -rniE 'junie|roo[- ]?code|deepcode|deep code|ampcode'` over every
  sibling's `SKILL.md`, `PROVINCE.md`, `corpus/knowledge`, `corpus/lessons`, `corpus/SOURCES.md`.
- r68 client tokens: `grep -rniE 'vt code|vtcode|parallel works|pw code|kilo code|kilocode|
  mistral vibe|agent framework|model spec'` over the 14 lanes with a corpus.
- command-vs-skill collision: `(slash[- ]command|command)[^\n]{0,50}(same[- ]name|collision)` plus
  the reverse form.
- Per-client/path maps: `trust (map|gate|tier|model)|rule[- ]file|consumer registry|cascade` over
  scope files; direct reads of kagi `corpus/adjacency.tsv`, kama `corpus/knowledge/consumer-registry.md`
  and `cross-lane-scope.md`, kumitate `corpus/README.md`, `SKILL.md`, `corpus/knowledge/kimi-*`,
  `omp-task-contract.md`.
- Plan claim: `grep -rlniE 'skill[- ]name|skill precedence|name collision' */plans */considerthese`
  → kotoba only (`plans/round-69.md`, `considerthese/2026-10-23.md`).

All pins below were re-read at the sibling's current head; where a file is dirty in that sibling's
working tree, the line was re-checked with `git show <head>:<path>`.

## F1 — kumitate holds a same-named skill precedence rule for Kimi Code (the one sibling hit)

- Sibling: **kumitate** (`be4a820c344d4eb2f94b999c3b5d649e76ab70f1`, 2026-10-25; census pin was
  `fac39171ac28c606e90da75fc2ba2ed3df52f4ea`).
- `SKILL.md:554-556` — "**Resolution precedence** (verified): User skills > Extra (managed
  plugins) > Built-in; user skills under `~/.kimi-code/skills/` are **symlinks** into
  `~/Projects/myskills` and `~/.agents/skills`". Same line at the census pin (checked with
  `git show fac39171:SKILL.md`), so the census row is not falsified — but the census records
  none of this.
- `corpus/knowledge/kimi-skills-plugins.md:423-428` quotes the governing text verbatim **from a
  rendered skill listing**: "When multiple scopes define a skill with the same name, the more
  specific scope takes precedence: Project overrides User overrides Extra overrides Built-in"
  (23 words).
- Same file `:300-312` records a **real** collision: two `SKILL.md:2` files both declare
  `name: kimi-webbridge` (User copy 2.0.26 vs Extra/plugin copy 1.11.3); the user copy wins by the
  quoted rule, labelled "INFERENCE, not measured" (no listing captured for that collision).
- `corpus/README.md:71` indexes the precedence fact; `corpus/lessons/round-18.md:20` (K3) records
  "precedence User > Extra > Built-in verified against the session listing".
- Boundary that crosses kotoba's: kumitate `PROVINCE.md:27` "Prompt and skill craft → kotoba", and
  kumitate `SCORECARD.md:1713-1719` (K-block boundary clause, `FLEET-ADJACENCY-ERRATA-V1`
  clause A) routes "`skills/*` craft and trigger discipline to **kotoba**" while keeping the
  `~/.kimi-code` census. So the split is sibling-stated: kumitate owns the Kimi substrate census
  (including its observed precedence), kotoba owns skill craft.
- Finding: **no client-set overlap** — C1's five clients (Roo Code, Amp, Deep Code, Junie,
  opencode) exclude Kimi — but Kimi is the one client for which a sibling holds *both* a
  name-keyed precedence rule *and* an observed instance, i.e. exactly C1's surface at a stronger
  evidence grade than C1's (documentary only). C1 must not be read as fleet-complete, and must not
  import Kimi without entering kumitate's Core.

## F2 — kumitate holds agent-file discovery precedence (adjacent class, different artifact)

- `corpus/knowledge/omp-task-contract.md:156-168` — "Agent discovery precedence": nearest project
  `.omp/agents` → user agent dir → extension package roots → Claude marketplace plugin roots →
  bundled; "Discovery uses first-wins de-duplication by exact `agent.name` … name comparison is
  case-sensitive."
- kumitate `PROVINCE.md:19` (Frontier) names "OMP harness contract (task batch, agent hub, agent
  discovery)" as its ground; the entry has S003 anchors.
- Finding: a same-name first-wins rule again, but over **agent-definition files**, not skills, and
  held as the harness contract. Kotoba's r56/r67 hold where agent files live and at whose
  authority level, not their discovery de-dupe. C1 must stay skill-scoped; generalising to agents
  would cross kumitate's Frontier.

## F3 — kagi's path-ownership map reads the same opencode tree as C1's opencode row

- Sibling: **kagi** (`69b61db46be4ed955994f6f1d1cba522bc5f4e97`, 2026-10-25),
  `corpus/adjacency.tsv:81` — `$HOME/.config/opencode | integrator | unresolved | declared |
  SCORECARD.md:54 | opencode | …` with "kotoba owns the instruction/agent surface and the provider
  declaration is operator-owned … this domain owns only credential/request hygiene on those
  children. Owners found by search: kotoba 24 files, kama 14, kengaku 9, kumitate 2".
- `:84` — `$HOME/.agents/AGENTS.md | kotoba | shared-read | declared | … kotoba is the sole fleet
  claimant of the file's checklist/shape reading`.
- Finding: a per-path ownership map whose subject is the opencode config tree C1's opencode row
  cites (skills live under `~/.config/opencode/`). It names kotoba as the instruction-surface
  claimant and claims **only** credential/request hygiene — no precedence, no skill-name rule. Not
  contested; the opencode config ownership question remains the integrator's (`unresolved`).

## F4 — kama inventories the opencode skills/agent/command dirs, for a different question

- Sibling: **kama** (`873c5d7774b97e7c633052456f13595a2ea5775f`, 2026-10-24).
  `corpus/knowledge/consumer-registry.md:325` runs an endpoint-pin grep over
  `~/.config/opencode/skills/`, `tools/`, `plugin/`, `agent/`, `command/` (no matches); `:56-57`
  records `~/.config/opencode/agents/` among the files "Deleted since round 2"; rows `:91-92`
  name `kotoba [INFERENCE]` in the owner column for the agent-instruction surface.
- `corpus/knowledge/cross-lane-scope.md:29` — "**Kotoba** owns the instruction/agent surface and
  its model/fallback wording; **kama** owns independent verification of the target endpoint."
- Finding: the same directory tree appears, read as an endpoint-pin inventory, under kama's own
  split that assigns wording to kotoba. No skill-name rule, no trust map for skill bodies.

## F5 — negatives (searched, not found)

- **No sibling states a same-named-skill precedence rule for any of C1's five clients.** The C1
  client-token sweep returns only kotoba's own working-tree files
  (`corpus/knowledge/skill-name-precedence-round69.md`, `corpus/SOURCES.md`, `plans/round-69.md`).
- **No sibling holds a per-client skill trust map** for r68's five clients (VT Code, Parallel
  Works/pw code, Kilo Code, Microsoft Agent Framework, Mistral AI Vibe). kumitate
  `corpus/SOURCES.md:264` lists "Microsoft Agent Framework primary docs … not opened" — a non-row
  pointer, not a claim. C3's r68 Core area is unclaimed elsewhere.
- **No sibling states precedence between a command and a same-named skill** (the round-58 unheld
  item). The only statements are kotoba's own `SKILL.md:108` and `:115` ("a same-named skill
  wins" / "commands rank below same-named skills", Copilot CLI).
- **No sibling lane plan names this round's surface**: the plans/considerthese sweep returns only
  kotoba's `plans/round-69.md` and `considerthese/2026-10-23.md`.
- Other `precedence` hits on sibling scope surfaces are unrelated senses: kama model-id resolution
  (`SKILL.md:147,156,1248`), kagi `op-ref` (`PROVINCE.md:49`), kaidoku instrument precedence
  (`SKILL.md:1136,1155`), mado Hyprland include order (`SKILL.md:50`), game-dev-3d's owed P/C
  label ruling (`SKILL.md:122-138`).

## Cross-check on kotoba's own draft (exposed by the scan; not a sibling claim)

Three findings in `corpus/knowledge/skill-name-precedence-round69.md` that the sibling/census
cross-read made visible (X1, X2 contradictions; X3 a prior holding the draft does not name).
Reported, not edited; `corpus/` is out of bounds for this seat.

- **X1 — the pinned-seven bullet is false as written.** `:45-46` reads "Five clients, none of them
  the lane's pinned seven; a pinned client's collision rule is not claimed here." opencode is
  pinned in both lists the lane uses: `verifiers/check_agent_definitions.py:134-135`
  (Claude Code, Codex, VS Code, Copilot CLI, Gemini CLI, Cursor, opencode) and
  `verifiers/check_overlap_levers.py:89-97` (GitHub Copilot SDK, Copilot CLI, VS Code, Claude Code,
  opencode, Gemini CLI, Codex). The sentence was inherited from the round-68 entry
  (`client-trust-gates-round68.md:56-57`), where it was true. Side note: the lane carries **two
  different "pinned seven" lists** (Cursor vs Copilot SDK); any correction must name which one.
- **X2 — the r50 novelty claim is too strong.** `:14-15` says the round-50 entry "only covers how
  clients choose between *differently named* skills". Its table already has a "which one wins rule
  documented" column carrying same-name rules for six client pages including opencode's exact S207
  quote (`corpus/knowledge/skill-selection-rules-round50.md:18-27`; coverage-map row at
  `corpus/README.md:72`). C1's real delta is **four new clients** (Roo Code, Amp, Deep Code,
  Junie) **plus opencode restated** as a collision rule.
- **X3 — a mined source the lane already owns states a collision rule.** S002
  (`corpus/SOURCES.md:15`, `agentskills.io/client-implementation/adding-skills-support`, status
  `mined`) carries a "§ Handling name collisions" section: "The universal convention across
  existing implementations: **project-level skills override user-level skills.**" and "either
  first-found or last-found is acceptable — pick one and be consistent" (verbatim in the round-47
  fetch at `.ufo/waves/round-47/build/KnowDescriptionRule.s002-adding-skills-support.md:83-89`).
  S002 is registered for the YAML/lenient-validation claim only; no entry uses the collision
  section. Wave artifact, so not a scope surface — but it means the surface is prior-held at
  source level, and the "universal convention" sentence is already contradicted by two of C1's
  own clients (Amp orders by *source*, Deep Code by *root*, neither by project/user). Do not add
  S002 to this round's frozen five; record it as the next entry's first candidate.

## Proposed move (one, tested)

Fold F1 + X1 + X2 into one Limits/Scope correction in
`corpus/knowledge/skill-name-precedence-round69.md` (L1's pen; no sibling edit):

1. intro: name the r50 same-name column as the prior holding and state the delta — four new
   clients, opencode restated;
2. Limits: replace the pinned-seven sentence with "four of them are not among the lane's pinned
   seven as the round-68 entry lists it; opencode is pinned in every list the lane uses
   (`check_overlap_levers.py:89-97`, `check_agent_definitions.py:134`), and its row here restates
   the round-50 uniqueness rule (S024)";
3. Limits: add the sibling boundary — "Kimi Code's skill resolution (User > Extra/Built-in) is
   kumitate's Core fact at `../kumitate-shokunin/SKILL.md:554-556` (head `be4a820c`), derived in
   kumitate `corpus/knowledge/kimi-skills-plugins.md:305,423-428`; cited, not re-derived, and Kimi
   is not counted among the five."

Tested in `/tmp/kotoba-r69-conn` (`git clone --shared` of the lane, draft files copied, committed
in the sandbox only):

```
# draft as it stands (sandbox rev 664b2f9)
python3 -B verifiers/check_skill_precedence.py --rev 664b2f9  ->  skill precedence backed 5 of 5, exit 0
# after the three text changes above (sandbox rev 3419eed)
python3 -B verifiers/check_skill_precedence.py --rev 3419eed  ->  skill precedence backed 5 of 5, exit 0
```

No S-id is added, so the counter's exact-five `source:` rule is untouched; the per-client table,
quotes and coverage-map index are unchanged, so checks 2–8 see identical inputs. Sandbox removed.

**Axes.** `depth` up: the entry's novelty statement becomes true and it distinguishes documentary
from observed evidence. `adjacency` up: the kumitate boundary is stated on kotoba's side with a
pinned sibling commit, no sibling touched. `consistency` up: X1 is an internal contradiction the
lane's own counters cannot see. `coverage` unchanged; no band move claimed.

## Risks

- Adding **Kimi as a sixth client** breaks the frozen five (counter → `0 of 5`). Cite only.
- A sibling head can advance: pin `be4a820c` and note the fact also holds at the census pin
  `fac39171`; do not cite a branch.
- The Kimi rule text names `Project` as the highest scope while kumitate's applied order
  (`SKILL.md:554`) has no project tier (no project-scoped Kimi skills observed). If quoted, quote
  the rule and state the applied order separately.
- X1's correction must not enumerate one "pinned seven" without saying which list; the two lists
  disagree (Cursor vs Copilot SDK) and that disagreement is itself a follow-up for the next census
  append, not something to settle here.
- X3 (S002's collision section) stays out of this round: adding it would break the frozen five and
  the counter's exact-five `source:` rule. It belongs in the next round's declaration.

## Verification

Evidence is tool output above: `git -C … rev-parse HEAD` for every pin; `sed`/`git show` line reads
for each quote; the two counter runs at sandbox revs `664b2f9` and `3419eed`. Sibling working trees
were left untouched. Tool installs: none. No pacman, no network fetch performed by this seat.
