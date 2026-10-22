FAILS for the appended section "## Round 50: precedence between `contested` and a stated split" as a decidable rule with an honest basis column. It leaves two definitions of `contested` in force, and the ownership term "text the sibling does not own" decides nothing for game-dev-3d and mado. The basis `both` for kake and kasegi rests on files kotoba filed itself. HOLDS-BOUNDED for "No row moves; 9 adjacent, 11 none, 0 contested", but only under the round-49 object reading ("other lanes' text") that the mado ruling actually uses. The precedence sentence conflicts with no row's ruling.

Seat: KotobaR50.CriticPrecedenceLanded (critic, leaf). Judged bytes: kotoba `956ee1676e4c18480bce8ac3993541462be76e11`; siblings at the census pins. Axis: adjacency (calibration is touched through the basis column). Attack rules: Q25, Q26.

## Findings

**F1. Two definitions of `contested` remain in force (duplicate authority, decidability).** The round-49 § Classification rule bullet ("claim part of kotoba's core (writing or auditing other lanes' SKILL.md, prompts or AGENTS.md-class files, or the instruments over them)") is unchanged. The round-50 bullet ("claim an element of kotoba's `PROVINCE.md` § Core over text the sibling does not own") never says it supersedes the round-49 bullet; the section corrects only the kengaku/tameshi sentence of § Classification rule. The section uses both: tameshi "the arm fires literally" (round-49 object) "but that instrument is … not an element of kotoba's § Core" (round-50 object). The two definitions disagree on whose text counts: other fleet lanes' text in round 49, anything the sibling does not own in round 50.

**F2. The mado ruling rests on a different test from the rule it cites.** The ruling reads "the omarchy skill file it surveys belongs to no lane, so no § Core element over another lane's text is claimed". The rule says "text the sibling does not own". mado does not own `~/.agents/skills/omarchy/SKILL.md`: mado `PROVINCE.md:10-11` calls it a "documentation surface, read-only". mado's corpus has a section titled "## 7. omarchy skill anatomy" (`corpus/knowledge/terminals-and-omarchy.md:115-151`). That section maps the frontmatter triggers and body sections and judges the hook listing "illustrative/older than the shipped layout". kotoba § Core element 1 names "anatomy and compression". Under the rule as written, the anatomy map is a candidate claim, and only the drift finding falls inside the "non-craft fact" exclusion. No split exists on mado's side, so if the map counts, mado moves from `none` to `contested` under every precedence.

**F3. game-dev-3d is undecidable under the round-50 wording.** game-dev-3d `corpus/knowledge/unreal-mcp/adaptation-kimi.md:330-331` reads: "Port the three `SKILL.md` files as-is. Their frontmatter is `name` + `description`, which is exactly what Kimi requires for directory skills". That is a judgment about which loader requires which frontmatter fields, the kotoba § Core element "Frontmatter rule authorities (round 48)". It is made over vendored upstream skills (`corpus/knowledge/unreal-mcp/upstream/skills/*/SKILL.md`, authored upstream). Kotoba's own `PROVINCE.md` row already says "its frontmatter audits cover only its own and vendored skill files". The rule does not say whether vendored text counts as owned:
- If vendored text counts as owned, or the test is "another lane's text", game-dev-3d stays `none`.
- If not, the arm fires. game-dev-3d's surfaces state no split and contain 0 files with the token `kotoba`, so it moves from `none` to `contested`, and the C1 target moves from 9 to 10. plan line 20 required that change to be re-declared before landing.

kaidoku and revenger also read a third-party skill (`~/.agents/skills/reverse-engineer-anything/SKILL.md`), but only its version, tool count and command lines. Those are non-craft facts, so both stay `none` under either reading.

**F4. "Assigns the claimed element" does not say to whom.** As written, a sibling whose scope surfaces say "we own <a kotoba Core element>" both claim the element and state a split that assigns it. The row would then be `adjacent`, the outcome the rule exists to prevent. No pinned row exercises this today: every sibling split I read assigns craft to kotoba or keeps the sibling to a non-craft function. It is still a hole in the rule's logic.

**F5. Basis `both` for kake and kasegi is not honest.** The section's sibling-side evidence is two lessons. Each file says "**Filed by:** kotoba round-5 report" and "Aggregator-owned file; the owning lane corrects `SKILL.md`." (kake `corpus/lessons/round-5-aggregator-mirror-pathless-cli-invocation.md:4-5`, kasegi `corpus/lessons/round-5-aggregator-mirror-ambiguous-citation-base.md:4-5`). The text is kotoba's finding, mirrored by the aggregator and declared aggregator-owned. That is not "the sibling's own scope surfaces" in the precedence's own words. The section's anti-relabel reason ("kotoba could otherwise relabel any claim with one sentence of its own") is defeated by exactly this channel: a kotoba report mirrored into a sibling's tree is counted as the sibling's statement. Honest basis is `kotoba`, with the mirror noted. No row moves: neither sibling has a claim (kake and kasegi sweep below: hits are self-references only).

**F6. chousa basis `kotoba` is honest.** On chousa's scope surfaces (`SKILL.md`, `PROVINCE.md`, `MINT.md`, `corpus/`), the token `kotoba` occurs as a whole word in 1 file. The match is `MINT.md:52`: "Rejected recipients for this material: lore, kotoba, kasegi, kama, kumitate, tameshi". That is a recipient list for research-export material, not a split. chousa's Refuses list routes to kasegi, kengaku, kumitate and kagi, not kotoba. Its description's anti-triggers name kasegi and kengaku only. chousa claims no Core element: there is no prompt or skill craft on its surfaces, and "prompt" occurs only for research-export prompts at `MINT.md:49-50`. So the row is `adjacent` through kotoba's routing commitment alone, which the rule permits.

**F7. The precedence sentence conflicts with no ruling.** "A split stated only by kotoba never overrides a claim" can only move a row whose basis is kotoba-only and whose sibling claims a Core element. With honest basis, that set is chousa, kake and kasegi (F5, F6), and none of the three claims a Core element. kama, kengaku, kumitate, kotodama, tameshi and kagi each carry a sibling-authored split (quotes verified below). So these rows stay `adjacent` whether or not the arm fires, and the "arm does not fire" reasoning for kama, kengaku and tameshi is not needed for their classes.

**F8. Kotoba ruling on its own boundary (AXES.md:16: "Lane reports name contested scope; integrator arbitrates").**
- Classifying is acceptable, because naming is the lane's job. Closing items is not. Round 49 recorded kama, kengaku and tameshi as possible `contested` elements "recorded for the integrator". Round 50 closes all three by kotoba's own definition and reports "0 contested". The fleet queue `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` has no round-50 kotoba line on this rule; the last kotoba lines are round 49 (lines 100-101).
- The round-50 anchor (kotoba's own `PROVINCE.md` § Core) is editable by kotoba. Whether tameshi fires depends on § Core listing only kotoba's named verifiers. So kotoba can still relabel a claim, through its Core list rather than through a split sentence, which is the risk the precedence sentence names.
- This is a tradeoff for the judge, not a fixable defect, unless the rule and its closures are routed to the integrator.

**F9. Q25/Q26: the rule has no counter shown able to fail.** The section admits the guard does not check the basis column. I also deleted the whole section, and separately inverted "never overrides" to "always overrides" and changed chousa's basis to `both`. The guard still exits 0 and prints the same lines, so "No row moves" is backed by no counter that reads the rule.

**F10 (minor). Dangling pointer.** The lesson's D3 note (`corpus/lessons/round-50.md:123`) says "see `## D3 precedence ruling` below". The file has 0 such headings; its `##` headings are Mistakes, Gate, and Routed defects.

## All 20 rows under the rule (my application)

| row | claim on a § Core element (pinned evidence) | sibling-authored split | outcome |
|---|---|---|---|
| audio, game-dev-2d | none (0 skill-text lines on scope surfaces) | none | none, stays |
| chousa | none (F6) | none | adjacent (kotoba-only), stays |
| game-dev-3d | undecidable (F3) | none | none, or **contested** under the literal wording |
| kagi | none (pins `$HOME/.agents/AGENTS.md` bytes, a non-craft fact) | `corpus/README.md:97` "kotoba owns the checklist/shape reading" | adjacent, stays |
| kaidoku, revenger | none (third-party REA skill facts only) | none | none, stays |
| kake, kasegi | none (self-references only) | none of their own (F5) | adjacent (kotoba-only), stays; basis should be `kotoba` |
| kama | not decisive | `cross-lane-scope.md:29` "**Kotoba** owns the instruction/agent surface…" | adjacent, stays |
| kengaku | not decisive | `SKILL.md:3` "kotoba owns prompt and skill craft (kengaku keeps only measured capability effects)" | adjacent, stays |
| kotodama | none | `SKILL.md:3` anti-trigger naming kotoba | adjacent, stays |
| kumitate | not decisive | `PROVINCE.md:27` "Prompt and skill craft → kotoba." | adjacent, stays |
| lore, mori, souji, tsukuroi, tabi | none (citations of sibling line numbers, observability logs, protocol schemas; tabi's split is in `.ufo/` only) | none | none, stays |
| mado | undecidable (F2) | none | none, or **contested** under the literal wording |
| tameshi | not decisive | `PROVINCE.md:14-17` "every lane's gate remains its own" | adjacent, stays |

Rows the rule would move: none under the reading the rulings use. Under the round-50 wording read literally, game-dev-3d and mado move from `none` to `contested`, giving 9 adjacent, 9 none, 2 contested, and the C1 target becomes 11.

## Smallest safe correction (append-only)

1. State that the round-50 `contested` bullet supersedes the round-49 one, and define the object as "text owned by another fleet lane". Third-party and vendored skills are then explicitly out of scope. Rule game-dev-3d and mado under that definition, citing `adaptation-kimi.md:330-331` and `terminals-and-omarchy.md:115-151`.
2. Precedence: "a split that assigns the claimed element to a lane other than the claimant, or confines the claimant to a non-craft function". Also: "the sibling's own scope surfaces exclude aggregator-owned files and files filed by kotoba".
3. Basis for kake and kasegi: `kotoba` (aggregator-mirrored kotoba finding). No class changes.
4. File one integrator-queue line: kotoba's precedence rule, the three closures (kama, kengaku, tameshi), and the game-dev-3d/mado ownership reading, pending integrator confirmation.
5. Fix the lesson's dangling `## D3 precedence ruling` pointer.

## Evidence (read-only in the lane; mutants only in the scratch clone)

- `git show 956ee167:corpus/knowledge/sibling-overlap-census-round49.md` (exit 0): section text and the round-49 rule bullets quoted above.
- `git -C /home/vgpnk/Projects/shokunin show HEAD:AXES.md | grep -n -i integrator` → line 16, exit 0.
- chousa: `git -C chousa-shokunin grep -c -wi kotoba 6c5eb146 -- SKILL.md PROVINCE.md MINT.md corpus AGENTS.md README.md` → `MINT.md:1`, exit 0. `git show 6c5eb146:MINT.md | sed -n 40,60p` and `git show 6c5eb146:PROVINCE.md` (exit 0).
- Row sweep: a loop over the census rows, running `git -C <lane>-shokunin grep -niE "SKILL\.md|AGENTS\.md|CLAUDE\.md|frontmatter|system prompt|dispatch prompt|agent prompt" <pin> -- SKILL.md PROVINCE.md MINT.md corpus | wc -l` (exit 0). Counts: audio 0, game-dev-2d 0, lore 29, revenger 27, mori 52, souji 57, kaidoku 89, mado 146, tsukuroi 267, game-dev-3d 343, tabi 916. A narrowed pattern (foreign, fleet, vendored or third-party skill files) over the 9 `none` rows (exit 0) produced the hits cited in F2 and F3. Every other hit is a self-reference, a citation line number, or a read of third-party version facts.
- game-dev-3d: `git show 89dd182b:corpus/knowledge/unreal-mcp/adaptation-kimi.md | sed -n 322,340p` (exit 0). `git grep -ciw kotoba 89dd182b -- SKILL.md PROVINCE.md MINT.md corpus` → 0 files.
- mado: `git show e33ea304:PROVINCE.md | sed -n 1,20p` and `git show e33ea304:corpus/knowledge/terminals-and-omarchy.md | sed -n 112,152p` (exit 0).
- Split quotes: `git show <pin>:<path> | sed -n <range>p` for the kake and kasegi lessons (`:1-8`), kagi `corpus/README.md:95-99`, kama `cross-lane-scope.md:29-32`, kengaku `SKILL.md:3`, kumitate `PROVINCE.md:20-30`, tameshi `PROVINCE.md:14-17`, kotodama `SKILL.md:3` (all exit 0).
- kake and kasegi claim sweep: narrowed foreign-skill pattern over `SKILL.md PROVINCE.md MINT.md corpus` (exit 0). All hits refer to the lane's own `SKILL.md`.
- Integrator queue: `grep -n -i kotoba /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md | tail -8` (exit 0). The last kotoba entries are round 49.
- Lesson headings: `git show 956ee167:corpus/lessons/round-50.md | grep -c '^## D3 precedence ruling'` → 0. The command printed 0 and so exited 1; the shell line exited 0 because later commands followed it.
- Scratch clone `/fast/scratch/hyaku/kotoba-r50/falsify/CriticPrecedenceLanded/lane` at `956ee1676e4c18480bce8ac3993541462be76e11`:
  - `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md` → `province rows 20 matched 20`, `skill description names 9 of 9 non-none lanes`, `skill description length 1008 of 1024`, exit 0.
  - Mutant A (precedence section deleted with awk): same output, exit 0.
  - Mutant B ("never overrides" changed to "always overrides", and "chousa kotoba" to "chousa both"; each target matched once by `grep -c`): same output, exit 0.
  - The file was restored afterwards and `git status --short` was empty.

Tooling: nothing installed or upgraded. Used git, grep, awk, sed and python3 (the mutation in scratch only). No web sources opened. No jj commands. The only lane write is this report.
