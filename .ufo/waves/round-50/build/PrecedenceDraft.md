# PrecedenceDraft — D3 precedence rule for the sibling-overlap census

**Result: HOLDS-BOUNDED.** My independently drafted precedence rule and the rule the L1 landed at
`956ee167` (basis `CriticPrecedence.md`) reach the **same class for all 20 rows** — 9 `adjacent`,
11 `none`, 0 `contested`; the three unruled rows (kengaku, tameshi, kama) all rule `adjacent`. The
two rules differ in **mechanism, not outcome**: mine tests *claim vs. split* as two ordered arms and
makes the split admissible from either side; the landed rule tests the *object* of the claim against
kotoba's `PROVINCE.md` § Core and makes a split admissible from either side too, with the extra
guard that a kotoba-side split never overrides a sibling's claim. No row is decided differently, so
C1's 9-of-9 target and the counts (9/11/0) are unaffected. Report follows; the L1's landed text is
the adopted one and mine is preserved below as the alternative draft.

## Findings

### F1 — The rule's object must be anchored, or the `contested` arm is unbounded

The round-49 rule defines `contested` by *what the sibling touches* ("writing or auditing other
lanes' SKILL.md, prompts or AGENTS.md-class files, or the instruments over them") and `adjacent` by
*what is stated*. Two different predicates: one about reach, one about statement. With no order
between them, a lane that states a split and also touches another lane's skill file is undecided —
exactly the three rows left open.

The landed rule fixes this by anchoring the claim to a fixed list: "an element of kotoba's
`PROVINCE.md` § Core over text the sibling does not own", with an explicit exclusion that reading or
verifying a *non-craft fact* held in such text is not a claim ("an endpoint value, a credential
checklist item, or the kill rate of the owner's gate"). That exclusion is what decides kama
(endpoint verdicts), tameshi (kill rate) and kengaku (a lane-local counter) to `adjacent`, and it is
the right discriminator: kotoba's core is the *craft* of skill files, not the fact values that happen
to sit in them.

My draft reaches the same three results by a different route — arm 1 asks whether the sibling
"asserts, in the sibling's own scope voice, that it writes, rewrites, or audits the craft ... or owns
the instruments over them", with the exclusion "naming, citing, reading, counting or measuring
another lane's skill file ... is not a claim". Both formulations exclude reach-without-assertion.

### F2 — The split must be admissible from either side, but must not launder a claim

Both rules let a split stated on *either* side support `adjacent` (the round-49 rule already said
"either side's committed scope surfaces"). The landed rule adds the constraint the round-49 rule
lacked: a split stated **only by kotoba** never overrides a sibling's claim, because kotoba could
otherwise relabel any claim with one sentence of its own; and it records a per-row `basis`
(`sibling` / `kotoba` / `both`) so the asymmetry is auditable rather than implicit. My draft states
the same guard in the ordering ("a boundary published by one side cannot discharge a claim asserted
by the other") but does not tabulate a basis column. The landed rule's basis column is the stronger
form: it is what makes the kake/kasegi correction (F3) checkable.

### F3 — Two of the nine `adjacent` rows do **not** rest on kotoba's description alone

The round-49 falsify note and D4's planned qualifier both say kake and kasegi are `adjacent` from
kotoba's own description. That is incomplete. Each sibling's own committed corpus carries an
aggregator-mirrored lesson stating the same division of labour, filed by kotoba round-5 and mirrored
by the aggregator: kake `corpus/lessons/round-5-aggregator-mirror-pathless-cli-invocation.md:4-5`
and kasegi `corpus/lessons/round-5-aggregator-mirror-ambiguous-citation-base.md:4-5`, both ending
"Aggregator-owned file; the owning lane corrects `SKILL.md`." So the basis is **both**, not kotoba
alone. The landed rule carries this correction; my draft did not find it.

### F4 — The kengaku contested element is unsourced at the pin

The round-49 note records that "kengaku's round-25 census script counts trigger strings in other
lanes' SKILL.md files, kotoba's included (kengaku `corpus/README.md:192`)". At the pin
`1f3b0f1e` that README line reads "| `plans/round25_census.sh` | Round-25 counting script (SOURCES
census, new rows, mistakes rows, SHONEN form, frontmatter triggers, both instruments' summaries) |"
— it names no other lane. The script is lane-local: `plans/round25_census.sh:37-40` exits 2 unless
the working directory is a lane root ("cwd is not a lane root (needs SKILL.md and corpus/)"), and it
reads only that root's `SKILL.md` (`:112`, `:172`). The only cross-lane invocation is at
`.ufo/waves/round-25/build/CensusScriptExec.md:48`, a wave report, which the census rule excludes as
a scope surface, and it is phrased as a prediction ("Predictions for L1's post-integration check,
read-only"). kengaku's own surfaces route the craft out (`SKILL.md:3` "kotoba owns prompt and skill
craft (kengaku keeps only measured capability effects)"; `PROVINCE.md:138` "reusable craft
implications route out"). So the premise of the open item does not hold; the row closes as
`adjacent` on a stated split, basis **both**.

### F5 — The round-49 rule text overstates kotoba's base `PROVINCE.md` lines

Census:51-52 says kotoba's base § Adjacent lines "state a split (chousa, kumitate, kengaku,
tameshi)". At `a5adc146` only chousa ("kotoba cites it, never re-derives it") and kumitate ("kotoba
owns the prompt wording, not the runtime") name kotoba's half; the kengaku and tameshi lines name
only the sibling's ground. The same base block also says of kama "no overlap observed", which the
rule ignores while counting other kotoba-side lines. The landed rule carries this correction; my
draft repeated the round-49 overstatement in its application table (I cited the kengaku and tameshi
base lines as their basis) and had to be corrected to their sibling-side splits.

### F6 — The D4 qualifier is still owed in the census entry, and the counts line is unqualified

D4's substance is "classified … from their own bytes … 0 contested" without a precedence rule
behind it. The landed census section (line 246 onward) states the rule and its counts, but census
line 10 still reads "from each sibling's own committed bytes" and line 99 still reads "9 adjacent,
11 none, 0 contested" with no note that round 49 had no precedence rule behind that zero. The
SCORECARD row 34 carries the round-50 qualifier, but the census entry's own two lines do not. The
D2D4 seat's variant-B text is not in the tree (`.ufo/waves/round-50/build/D2D4Wording.md` absent),
so the qualifier was not folded into the census entry as that seat asked. This is the one open item
on D4 and it does not affect any class.

## Comparison — my draft rule vs the landed rule, row by row

| lane | mine | landed | differs? |
|---|---|---|---|
| audio, game-dev-2d, game-dev-3d, kaidoku, lore, mado, mori, revenger, souji, tabi, tsukuroi (11) | `none` | `none` | no |
| chousa, kagi, kake, kama, kasegi, kengaku, kotodama, kumitate, tameshi (9) | `adjacent` | `adjacent` | no |

**No row is decided differently.** Mechanism differences only: (i) mine tests claim-vs-split as
ordered arms, the landed rule tests the claim's *object* against kotoba's § Core and lists
non-craft facts that do not count; (ii) the landed rule adds the kotoba-side split never overrides
a sibling's claim, plus a per-row `basis` column; (iii) the landed rule adds the F3 kake/kasegi
basis correction and the F5 correction to § Classification rule, which my draft lacked. Under
either rule the three unruled rows close `adjacent` and no row moves, so the counts (9/11/0), the
non-`none` set of 9 and C1's "9 of 9" target are identical.

## My draft (alternative text, preserved for the record)

### Precedence test (ordered; the first arm that matches decides the row)

0. **Surfaces.** Only the sibling's committed scope surfaces count (SKILL.md including its
   frontmatter description, PROVINCE.md, corpus files). Wave reports, run logs and one-off evidence
   reads are not scope surfaces (unchanged from the rule above).
1. **Claim -> `contested`.** The sibling's committed scope surfaces claim part of kotoba's core
   craft: they assert, in the sibling's own scope voice, that it writes, rewrites, or audits the
   craft of SKILL.md / AGENTS.md-class files or prompts, or owns the instruments over them, for other
   lanes or for the fleet. Claiming the craft is what makes a row contested. Naming, citing, reading,
   counting or measuring another lane's skill file, and publishing a boundary about it, is not a claim.
2. **Split -> `adjacent`.** Otherwise, if either side's committed scope surfaces state a split of one
   artifact, function, or trigger area between the sibling and kotoba.
3. **Otherwise -> `none`.** Neither a claim nor a split.

**Why this order.** The two arms are not equally strong. `contested` is an affirmative finding (the
sibling's own scope asserts overlapping ownership of the craft); `adjacent` is satisfied by the
weaker condition that a boundary is published, on either side, about some artifact. A boundary
published by one side cannot discharge a claim asserted by the other, so the claim is tested first: a
lane that both claims the craft and publishes a split is `contested` (the arbitration need), and a
lane that only publishes a boundary is `adjacent`. Testing the split first would let a boundary
swallow every contested row, which is what left the three rows below unruled in round 49.

**Application to all twenty rows** (arm that fired; located basis at the pin). `none` (arm 3): audio,
game-dev-2d, game-dev-3d (2D surfaces route to game-dev-2d), kaidoku (the kaidoku/revenger
overlap is between those two lanes), lore, mado (omarchy skill read-only; the wave report assigning
the facet to kotoba is not a scope surface), mori (kotoba appears only in lane-progress evidence),
revenger, souji (the sibling SKILL.md paths it names live in `census/` transcripts), tabi (the
round-16 wave draft is a wave report), tsukuroi. `adjacent` (arm 2): chousa (base `PROVINCE.md`
§ Adjacent "kotoba cites it, never re-derives it"), kagi (base `SKILL.md`:10-12 plus kagi
`corpus/README.md`:96-97 "kotoba owns the instruction/agent surface"), kake (base `SKILL.md`:10-12),
kama (`corpus/knowledge/cross-lane-scope.md`:29), kasegi (base `SKILL.md`:10-12), kengaku
(`SKILL.md`:3, `PROVINCE.md`:138), kotodama (`SKILL.md`:3 anti-trigger, `MINT.md`:20), kumitate
(`PROVINCE.md`:27), tameshi (`PROVINCE.md`:14-17, `corpus/knowledge/fleet-kill-rate-ledger.md`:127).
**Corrections to my draft, after reading the landed rule:** kake and kasegi are basis **both**, not
kotoba alone (F3); kengaku and tameshi rest on their sibling-side splits, not on the base
`PROVINCE.md` lines (F5). Both corrections change no class.

### The three open rows, ruled (mine)

- **kengaku -> `adjacent`.** The contested element is withdrawn as unsourced at the pin: the README
  row names no other lane (F4); the script is lane-local (`plans/round25_census.sh`:37-40, :112,
  :172); the cross-lane invocation sits in an excluded wave report
  (`.ufo/waves/round-25/build/CensusScriptExec.md`:48); kengaku's own split routes the craft out
  (`SKILL.md`:3, `PROVINCE.md`:138). Basis both.
- **tameshi -> `adjacent`.** The Core names kagi's `corpus/checklist-run.sh` (`PROVINCE.md`:31-32)
  among "the six recorded mutation legs' gates as read-only primary surfaces" (`:29-30`); the gate
  reads **kagi's own** file (kagi `corpus/checklist-run.sh`:66-68 resolves `ROOT` to kagi's repo
  root and sets `SKILL="$ROOT/SKILL.md"`; `:4` "`SKILL.md` §Credential-hygiene checklist holds 16
  items"), and kagi is that file's owner. tameshi claims no skill-file craft, parks kotoba's
  instruments as an unadmitted sighting (`fleet-kill-rate-ledger.md`:127) and never edits a sibling's
  gate code (`PROVINCE.md`:14-17). Basis sibling.
- **kama -> `adjacent`.** The registry rows are endpoint records, not craft claims: `:91` covers
  `~/.config/opencode/agents/janitor.md`:5, :20-21 with owning lane "`kotoba` [INFERENCE]
  (agent-instruction surface)" and verdict FOREIGN_SERVICE; `:92` covers `distiller.md`:5, :7, same
  owning lane, verdict "cascade-protected"; `:111` cites `~/projects/shokunin/kengaku-shokunin/
  SKILL.md:322-323` with owning lane **kengaku** and an endpoint verdict; `:325-326` are the
  "Absence is evidence" rows (no matches, exit 1). kama's own split assigns the wording to kotoba
  (`corpus/knowledge/cross-lane-scope.md`:29). Basis sibling.

### Replacement boundary cells for the three PROVINCE.md § Adjacent rows

- **kama** (class `adjacent`, commit `c808ba07f09c4be55413d3d6516c542ab69b64f8`): local model
  serving and endpoint health; kama's split reads "**Kotoba** owns the instruction/agent surface and
  its model/fallback wording; **kama** owns independent verification of the target endpoint" (kama
  `corpus/knowledge/cross-lane-scope.md`:29; kama `MINT.md`:42); the agent files it names were
  deleted 2026-10-14 per kama `corpus/README.md`:51-55); ruled `adjacent` under the round-50
  precedence rule: the registry rows are endpoint verdicts, not craft claims — `:91-92` name kotoba
  as the owning lane of the agent-instruction surface, `:111-112` cite kengaku's own
  `SKILL.md`:322-323 with kengaku as owner, `:325-326` are absence greps with no matches; no kama
  scope surface claims the craft; basis sibling.
- **kengaku** (class `adjacent`, commit `1f3b0f1ec41ec297130e8944ff97968d32324632`): LLM and model
  research and evaluation (route telemetry is marked absent since 2026-10-15 in kengaku's own
  `SKILL.md`:3); kengaku keeps measured capability effects of prompt format, kotoba owns the craft
  rules (kengaku description, `SKILL.md`:3 "kotoba owns prompt and skill craft (kengaku keeps only
  measured capability effects)"; kengaku `PROVINCE.md`:138 "reusable craft implications route out");
  ruled `adjacent` under the round-50 precedence rule: the recorded contested element does not hold
  at the pin — `corpus/README.md`:192 describes a lane-local counting script and
  `plans/round25_census.sh`:37-40 exits 2 unless the cwd is a lane root, so it never reads another
  lane's `SKILL.md`; the cross-lane use appears only in the wave report
  `.ufo/waves/round-25/build/CensusScriptExec.md`:48, which the rule excludes as a scope surface;
  basis both.
- **tameshi** (class `adjacent`, commit `3b20f073c7305a582562cd323982991464c324f3`): verification-
  fixture craft and mutation testing; tameshi owns the fixture method; kotoba owns the SKILL-checklist
  instrument (kotoba base `PROVINCE.md` § Adjacent; tameshi corpus `fleet-kill-rate-ledger.md`:
  125-128); ruled `adjacent` under the round-50 precedence rule: the Core-named gate is kagi's and
  reads kagi's own repo-root `SKILL.md` (kagi `corpus/checklist-run.sh`:66-68), and tameshi's ledger
  keeps kotoba's `verifiers/*` an unadmitted sighting (`:127`), so no scope surface claims the craft;
  basis sibling.

## Evidence (read-only; commands with exit codes, 2026-10-22)

Sibling bytes at the census pins (`git -C <lane>-shokunin show <pin>:<path>`), all exit 0:
- kengaku `corpus/README.md`:192 at `1f3b0f1e` -> "| `plans/round25_census.sh` | Round-25 counting
  script (SOURCES census, new rows, mistakes rows, SHONEN form, frontmatter triggers, both
  instruments' summaries) |" (no other lane named).
- kengaku `plans/round25_census.sh`:37-40 -> `if [ ! -f SKILL.md ] || [ ! -d corpus ]; then` /
  `echo "round25_census: cwd is not a lane root (needs SKILL.md and corpus/)" >&2` / `exit 2` / `fi`;
  `:112` `if [ -f SKILL.md ]; then`; `:172` `}' SKILL.md)"`.
- kengaku `SKILL.md`:3 -> "Sibling arbitration: kotoba owns prompt and skill craft (kengaku keeps
  only measured capability effects); kumitate owns OMP route resolution and fallback policy; kama
  owns local endpoint health and identity; chousa owns research method; tameshi owns
  verification-fixture craft."; `PROVINCE.md`:138 -> "| **kotoba** | prompt- and skill-craft rules —
  measured capability effects of prompt format stay here; reusable craft implications route out
  (r7 tools-without-system, r11/r12 ack-intent findings) |".
- kengaku `.ufo/waves/round-25/build/CensusScriptExec.md`:48 -> "Predictions for L1's
  post-integration check, read-only — `(cd /home/vgpnk/Projects/shokunin/<lane> && sh
  /tmp/kengaku-r25-CensusScriptExec/plans/round25_census.sh) | grep triggers`: chousa 5, mori 5,
  kotoba 8, lore 5, tameshi 0 (all five have SKILL.md + corpus/)."
- tameshi `PROVINCE.md`:14-17 at `3b20f073` -> "**Refuses:** product domains — every lane's gate
  remains its own; tameshi owns only the reusable craft (a pattern is admitted from evidence in TWO
  independent lanes before it is claimed general). Never edits a sibling's gate code (read-only
  probes; recommendations travel in round reports)."; `fleet-kill-rate-ledger.md`:127 -> "`tools/
  {kama-probe,test-snapshot}.sh`, kotoba `verifiers/*` — file existence is O, their gate-ness is U
  until a survey admits them".
- kagi `corpus/checklist-run.sh` at `fecee874` -> `:4` "# `SKILL.md` §Credential-hygiene checklist
  holds 16 items."; `:66` `ROOT=$(cd -- "$SCRIPT_DIR/.." && pwd)`; `:68` `SKILL="$ROOT/SKILL.md"`.
- kama `corpus/knowledge/cross-lane-scope.md`:29 at `c808ba07` -> "| A model/baseURL/fallback
  statement in an agent file versus truth about the service. | **Kotoba** owns the
  instruction/agent surface and its model/fallback wording; **kama** owns independent verification of
  the target endpoint. |"; `MINT.md`:42 -> "| kotoba | prompt & skill craft | instruction surfaces,
  not services |"; `corpus/knowledge/consumer-registry.md`:91 owning lane "`kotoba` [INFERENCE]
  (agent-instruction surface)", verdict FOREIGN_SERVICE; :92 owning lane `kotoba`, verdict
  "cascade-protected"; :111 owning lane **kengaku**, verdict "records FOREIGN_SERVICE on 8080 /
  MODEL_OK on 34113"; :325-326 "**no matches** (exit 1)".
- kake `corpus/lessons/round-5-aggregator-mirror-pathless-cli-invocation.md`:4-5 at `e73d48bb` and
  kasegi `corpus/lessons/round-5-aggregator-mirror-ambiguous-citation-base.md`:4-5 at `1fafde8f` ->
  "**Filed by:** kotoba round-5 report (2026-09-28), `kotoba-shokunin@4002b9f` §"Cross-domain
  observations to relay" ..." and "**Mirrored by:** aggregator round-5 (main-repo lane, `m_qwen`) per
  `PROTOCOL.md` integrator step 2. Aggregator-owned file; the owning lane corrects `SKILL.md`."
- kotoba base `PROVINCE.md` at `a5adc146`, § Adjacent lines 29-34 -> chousa "kotoba cites it, never
  re-derives it"; kumitate "kotoba owns the prompt wording, not the runtime"; kengaku "LLM/model
  evaluation and route telemetry."; tameshi "verification-fixture craft and mutation testing."; kasegi
  "security research incl. prompt-injection exploits."; "kotodama (worldbuilding/naming), mado
  (desktop config), revenger (shipped-artifact RE), mori (fleet observability), kama (model serving)
  — no overlap observed." Only chousa and kumitate name kotoba's half.
- Scope-surface sweeps for the 11 `none` lanes (`git -C <lane> grep -c -i kotoba <pin> -- SKILL.md
  PROVINCE.md corpus/`), exit 0: audio 0, game-dev-2d 0, game-dev-3d 0, kaidoku 0, lore 0, mado 0,
  revenger 0, souji 0; mori 23 (all lane-progress evidence rows), tabi 4 (the watchdog `LANES=` roster
  line), tsukuroi 3 (pointer-census rows). None states a split.
- Cross-lane reach census, complete over all 20 lanes at their pins (which lanes' committed trees
  name another lane's `SKILL.md`; `git -C <lane> grep -o -h -E "[a-z0-9-]+-shokunin/SKILL\.md"
  <pin> -- ':!.ufo'`), exit 0: audio none; chousa none; game-dev-2d chousa; game-dev-3d chousa,
  kotoba; kagi kake; kaidoku none; kake chousa; kama kengaku; kasegi none; kengaku chousa, kasegi,
  kotoba, kumitate; kotodama none; kumitate none; lore chousa; mado none; mori none; revenger none;
  souji all 19 others; tabi none; tameshi tsukuroi; tsukuroi kama, tameshi. Every reach is a
  citation of a sibling's scope, not a craft claim, and none is in a scope surface in the contested
  sense: kengaku's are connector reports and a chousa method pointer (`PROVINCE.md`:137 "method stays
  chousa's"); tameshi's cite tsukuroi's rules (`corpus/knowledge/service-optin-protocol.md`:47);
  game-dev-3d's kotoba reach is in `reports/round-101/r101-scout-roster.md` (a report, not a scope
  surface) and its chousa reach is a method pointer (`corpus/QUALITY.md`:5 "Research follows chousa's
  method"); tsukuroi's kama reach is a shape-model citation of a sibling's distilled form
  (`SKILL.md`:207) and its tameshi reach is in `plans/` (not a scope surface); souji's 68 reaches
  all sit in `census/` transcripts and `results/` (wave and run artifacts, not scope surfaces);
  kagi's kake reach and lore's, kake's, game-dev-2d's chousa reaches are likewise citations.
- Scope-surface reach check (the same census restricted to the surfaces the rule admits — SKILL.md,
  PROVINCE.md, corpus/): the only cross-lane SKILL.md reference inside a scope surface is tsukuroi's
  `SKILL.md`:207 shape-model citation of kama; every other reach above sits in a report, plan,
  transcript or results file. No lane's scope surface reaches another's skill file *as craft*.
- Guard checks, `python3 -B` (all exit 0): landed guard on landed files -> "rows 20 verified 20",
  "province rows 20 matched 20"; with `--skill SKILL.md` -> "skill description names 9 of 9 non-none
  lanes", "skill description length 1008 of 1024"; my draft census + my draft PROVINCE rows under the
  landed guard -> "rows 20 verified 20", "province rows 20 matched 20" (my boundary text keeps the
  4-cell shape and the census table is untouched).
- Counts at the landed rev: `awk -F' \\| ' '/^\| [a-z0-9-]+ \| (main|master) \| [0-9a-f]{40} \|/{print
  $5}'` -> 9 adjacent, 11 none, 0 contested; 20 rows.

Tooling: nothing installed or upgraded. No web sources. No jj commands; no git write commands in the
lane. The only lane write is this report; the scratch copies under
`/fast/scratch/hyaku/kotoba-r50/build/PrecedenceDraft/` are outside the lane.

Out of scope for this seat (other owners): the D4 qualifier text for census lines 10 and 99 (the
D2D4 seat's variant B; its report is absent from the build directory), the guard's duplicate-row
refusal and `verifiers/floors-registry.json` entry (CensusGuard seat), and the D2 docstring /
SCORECARD wording (D2D4 seat).
