FAILS for routed defect D3 as framed ("add a precedence rule"): on the pinned bytes no choice of precedence moves any row between `none` and non-`none`. The open items come from the contested arm's object wording, from one false citation, and from a wrong premise about kake and kasegi. HOLDS-BOUNDED for the round-49 classes of kama, kengaku, tameshi (`adjacent`) and mado (`none`) under the rule proposed below.

Seat: KotobaR50.CriticPrecedence (critic, leaf). Judged bytes: kotoba `f30464660c675d1c1e2851a3bf0366a3aaffe5a8`; siblings at the census pins. Axis: adjacency (calibration is touched through the D4 wording). I did not read the drafting seat's output.

## 1. Proposed rule (two parts)

**Part A. Anchor the contested arm to one authority.** The census arm (census:45-46) restates kotoba's core in its own words ("…or the instruments over them"). That restatement is wider than kotoba's `PROVINCE.md` § Core, which lists craft functions (trigger and frontmatter craft, anatomy, fidelity checklists, agent, AGENTS.md-class and dispatch-prompt craft) and kotoba's own named `verifiers/*`. Two definitions of "core" is the root of D3. Rule: a claim is contested only if the sibling's scope surfaces claim a § Core element over text the sibling does not own. Reading or verifying a non-craft fact held in such text does not count: an endpoint value, a credential checklist item, or the kill rate of the owner's gate.

**Part B. Precedence: the claim comes first, and a sibling-stated split is the only exit.** If the arm fires, the row is `contested`. It becomes `adjacent` only if the sibling's own scope surfaces state a split that assigns the claimed element. A split stated only on kotoba's side never neutralises a sibling's claim.

Why: the classes exist to surface conflicts to the integrator. Calling a real claim `adjacent` hides it. Calling something `contested` by mistake costs only a review. Requiring the split on the claimant's side stops kotoba from relabelling a sibling's claim with its own text (see section 2).

## 2. Strongest argument for the opposite: the split wins, from either side

- The census's own source finding: with no documented tie-break, "A description that names its neighbour and says who owns what is the whole mechanism" (census:34-37). On that reading, a stated split *is* the arbitration, and `contested` should mean "claim with no arbitration". Counting a resolved overlap as contested adds noise.
- Fleet practice matches it. kengaku's own corpus labels kotoba "**Contested** — prompt format is a treatment in kengaku experiments, while prompt construction is kotoba's province" (`corpus/evidence/round9-fleet/sibling-overlap.md:12` at `1f3b0f1e`), then resolves that to a split in ruling (a) (`:21`). The sibling's own record goes contested, then split, then settled.
- `adjacent` versus `contested` does not change C1: both are non-`none`, so the 9-lane target does not move either way.

Where it breaks: (1) Under "either side", kotoba could turn any contested row `adjacent` by adding one sentence to its own description. (2) Stale splits still count. kama's split names agent files that kama's own `PROVINCE.md:11` and `corpus/README.md:51-55` record as deleted on 2026-10-14. The live cross-lane touch, `consumer-registry.md:111-112` (a verdict on kengaku `SKILL.md:322-323`), is covered only by kama's function rule at `cross-lane-scope.md:32`, not by the split at `:29`. Part B keeps the useful half of this argument, because a sibling-stated split still resolves the row.

## 3. Rows under each precedence

Readings: **R-lit** is the arm as written: scope surfaces only, `.ufo/` excluded (the same exclusion that keeps tabi and mado `none`), object "other lanes' SKILL.md, prompts or AGENTS.md-class files, or the instruments over them". **R-core** is Part A. **Pc** = the claim always wins. **Ps** = the split wins (the opposite). **Pm** = Part B.

| row | arm under R-lit (pinned evidence) | split on the sibling's side | Pc | Ps | Pm | under R-core |
|---|---|---|---|---|---|---|
| kama | fires: `consumer-registry.md:91-92` audits agent prompt text (janitor "there is no fallback"); `:111-112` records a verdict on kengaku `SKILL.md:322-323`; `SKILL.md:20-21` scopes baseURLs in "agent frontmatter" | `cross-lane-scope.md:29` ("**Kotoba** owns the instruction/agent surface and its model/fallback wording; **kama** owns independent verification…"); `:32` function rule; `MINT.md:42` ("instruction surfaces, not services") | **contested** (moves) | adjacent | adjacent | arm does not fire (endpoint truth is not craft): adjacent |
| kengaku | does **not** fire. `plans/round25_census.sh` reads only the `SKILL.md` in its working directory (`:37-38` require a lane root; `:112-172` read `SKILL.md`). Its scope surfaces claim only its own use: header `:2` "run from the lane root"; `corpus/README.md:192` "…frontmatter triggers…". The audit of 19 lanes and the predicted runs in kotoba live only in `.ufo/waves/round-25/` (RowKengaku F2), which the rule excludes | description `SKILL.md:3` "kotoba owns prompt and skill craft (kengaku keeps only measured capability effects)"; `PROVINCE.md:30-32, :138` | adjacent | adjacent | adjacent | adjacent |
| tameshi | fires: Core `PROVINCE.md:31-32` names kagi `corpus/checklist-run.sh`, which reads kagi's `SKILL.md` checklist (kagi `checklist-run.sh:4`) | `PROVINCE.md:14-17` "every lane's gate remains its own; tameshi owns only the reusable craft … Never edits a sibling's gate code"; `fleet-kill-rate-ledger.md:125-128` names kotoba `verifiers/*` as adjacent machinery, "not queued" | **contested** (moves) | adjacent | adjacent | arm does not fire (kagi's instrument is not kotoba's § Core): adjacent |
| mado (`none`) | does not fire: the omarchy skill belongs to no lane | none: 0 files in mado `SKILL.md`, `PROVINCE.md` or `corpus/` name kotoba | none | none | none | none (consumer reading plus a host-drift check, not a craft judgment) |

Rows that move:
- Pc moves kama and tameshi from `adjacent` to `contested`. The census counts go from 9 adjacent / 0 contested to 7 / 2. The SCORECARD "0 contested" wording changes; C1 does not.
- Ps and Pm move nothing.
- The object wording, not precedence, decides mado. If the arm is read as "any SKILL.md" (kotoba's description says "audits … SKILL.md" with no "other lanes'"), mado fires. `corpus/knowledge/terminals-and-omarchy.md:115-151` maps the omarchy frontmatter and judges its hook listing "illustrative/older than the shipped layout". With no split on any scope surface, mado would move from `none` to `contested` under **every** precedence, and the C1 target would move from 9 to 10, re-declared before landing (plan line 20). Part A keeps it `none`.
- kengaku would turn `contested` under Pc and Pm only if `.ufo/` counted. That would also move tabi (its round-16 draft split) and break the rule's own exclusion, so I reject that reading.

## 4. Defects found while testing (fixable; not tradeoffs)

**F1. False citation in the kengaku boundary note.** Kotoba `PROVINCE.md` (kengaku row): "kengaku's round-25 census script counts trigger strings in other lanes' SKILL.md files, including kotoba's (kengaku `corpus/README.md:192`)". At the pin, README:192 reads "Round-25 counting script (SOURCES census, new rows, mistakes rows, SHONEN form, frontmatter triggers, both instruments' summaries)". It says nothing about other lanes, and the script reads only its own working directory. Correction: cite the `.ufo/waves/round-25/` reports and state that the rule excludes them, or drop the clause. The kengaku item recorded as "open" then closes under the rule as written.

**F2. The rule overstates kotoba's base `PROVINCE.md`.** Census:51-52 says kotoba's base § Adjacent lines "state a split (chousa, kumitate, kengaku, tameshi)". At `a5adc146`, only chousa ("kotoba cites it, never re-derives it") and kumitate ("kotoba owns the prompt wording, not the runtime") name kotoba's half. kengaku ("LLM/model evaluation and route telemetry.") and tameshi ("verification-fixture craft and mutation testing.") name only the sibling's ground. The same base block says "kama (model serving) — no overlap observed", and the rule ignores that kotoba-side statement while counting others. tameshi's `adjacent` therefore needs its tameshi-side basis cited (`PROVINCE.md:14-17` and ledger `:125-128`), not kotoba's base line.

**F3. The kake and kasegi premise is false (affects D4 and the census finding).** Both siblings' own committed corpus states the split, in lessons the aggregator mirrored into their trees:
- kake `corpus/lessons/round-5-aggregator-mirror-pathless-cli-invocation.md:4-5` at `e73d48bb`: "**Filed by:** kotoba round-5 report …" and "Aggregator-owned file; the owning lane corrects `SKILL.md`."
- kasegi `corpus/lessons/round-5-aggregator-mirror-ambiguous-citation-base.md:4-5` at `1fafde8f`: the same two lines.

That is the same split as kotoba's description ("kotoba audits and reports; the owning lane fixes"), stated in the sibling's tree, which the rule lists as a scope surface ("corpus files"). The round-49 seats missed it. The guard checks only the description and `PROVINCE.md`, so it could not have caught it. D4's planned qualifier "kake and kasegi rest on kotoba's own description" would be wrong if appended as written. Correct basis: kotoba's description, plus aggregator-authored lessons in the sibling's corpus.

## 5. Should a split stated only on kotoba's side count the same?

No, not the same, though the question no longer decides kake or kasegi (F3). Counterexamples:
1. The sentence is universal. "Own their own SKILL.md content — this skill audits and reports" is true of all 17 lanes that have a skill file. Naming 5 of them is a selection inherited from round 7's five-lane sample, not an observed overlap. If the description had named audio in that sentence, audio would be `adjacent` under the current rule.
2. Kotoba's own text is used one way only. Kotoba-side "split" lines count, but kotoba-side "no overlap observed" lines (kama and mado at `a5adc146`) are ignored.
3. It would let kotoba relabel claims (section 2).

Ruling I recommend: a split stated only on kotoba's side may establish `adjacent` for a row that has no claim, because it is a routing commitment kotoba must honour. But it must name an element specific to that lane, it never overrides a sibling's claim (Part B), and the row records a basis value: `sibling`, `kotoba`, `both` or `third-party`. Under that ruling, kake and kasegi get `both` (kotoba's description plus aggregator-mirrored lessons); neither moves.

Sweep of the 11 `none` rows for kotoba mentions on scope surfaces: 0 files each for audio, game-dev-2d, game-dev-3d, kaidoku, lore, mado, revenger and souji. mori has 23 files (observability logs such as "SURFACE lane.kotoba: progressing"), tabi 4 (the watchdog `LANES=` roster line) and tsukuroi 3 (pointer-census rows). None states a split, so no `none` row moves.

## 6. Smallest safe correction (append-only)

1. Append to the census § Classification rule. Suggested text: "Contested means the sibling's scope surfaces claim an element of kotoba's `PROVINCE.md` § Core over text the sibling does not own; reading or verifying a non-craft fact in such text is not a claim. Precedence: a claim makes the row `contested` unless the sibling's own scope surfaces state a split that assigns the claimed element; a split stated only by kotoba never overrides a claim. Each non-`none` row records its basis: sibling, kotoba, both, third-party."
2. Rulings under that text: kama `adjacent` (basis `sibling`: cross-lane-scope `:29`, `:32`); kengaku `adjacent` (`both`; F1 corrected); tameshi `adjacent` (`sibling`: `PROVINCE.md:14-17`, ledger `:125-128`); mado `none`; kake and kasegi `adjacent` (`both`, F3).
3. D4's qualifier cites F3 instead of "kotoba's own description".
4. C1 lane list: unchanged at 9. Re-declare only if the rule is read as "any SKILL.md" (mado).

Tradeoff left to the judge: Pm versus Pc is a policy choice. Pc catches more conflicts at the cost of noisier labels, and it changes the census count from 0 to 2 contested. F1 to F3 are plain defects either way.

## Evidence (all read-only; every command exited 0 unless stated)

- Sibling bytes: `git -C <lane>-shokunin show <pin>:<path> | sed -n <range>p` for kengaku (`SKILL.md:1-12`, `PROVINCE.md:28-40,130-140`, `corpus/README.md:180-200`, `plans/round25_census.sh:1-60,100-175`, `corpus/evidence/round9-fleet/sibling-overlap.md:10-22`); tameshi (`PROVINCE.md:1-50`, ledger `:120-130`); kama (`SKILL.md:1-24`, `MINT.md:36-44`, `cross-lane-scope.md:20-40`, `consumer-registry.md:85-115,320-330`); mado (`SKILL.md:1-20,365-400`, `PROVINCE.md`, `MINT.md:1-20`, `terminals-and-omarchy.md:112-160`); kagi `checklist-run.sh:1-25`; the kake and kasegi lessons (`:1-30`, `:1-16`).
- kengaku other-lane claim on scope surfaces: `git -C kengaku-shokunin grep -nE 'round25_census|FrontmatterScout|frontmatter trigger|19 lanes|skill_frontmatter' 1f3b0f1e -- SKILL.md PROVINCE.md corpus` gave 7 lines: README:192 and kengaku's own receipts and spot-check. None claims a run in another lane.
- kake and kasegi: `git -C <lane>-shokunin grep -il kotoba <pin> -- SKILL.md PROVINCE.md corpus | wc -l` gave kake 1 and kasegi 2. All hits are the round-5 aggregator-mirror lessons (kasegi's second hit is `corpus/instruments/citation-survival.tsv:1025`).
- `none` sweep: an awk loop over the census rows with `$5=="none"`, running `git -C <lane>-shokunin grep -il kotoba <pin> -- SKILL.md PROVINCE.md corpus | wc -l`, gave the counts in section 5.
- Kotoba base: `git show a5adc146:PROVINCE.md | awk '/^## Adjacent/{f=1;next} /^## /{f=0} f'` gave the six base lines quoted in F2. `git rev-parse HEAD` in the lane gave `f30464660c675d1c1e2851a3bf0366a3aaffe5a8`.
- Not run: the census guard and any mutant. This seat is attack-only and changes no code, so there is no `patch.diff`. Scratch directory `/fast/scratch/hyaku/kotoba-r50/build/CriticPrecedence/` was created and is empty.

Tooling: nothing installed or upgraded. Used git, awk, grep and sed (read-only). No web sources. No jj commands. The only lane write is this report.
