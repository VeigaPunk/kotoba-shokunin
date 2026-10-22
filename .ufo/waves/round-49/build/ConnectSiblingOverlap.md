# ConnectSiblingOverlap — round 49 build, C1 adjacency (reverse direction and cross-lane)

Seat `KotobaR49.ConnectSiblingOverlap`, 2026-10-22T09:40Z, read-only on all 21 repos; receipts in
`/fast/scratch/hyaku/kotoba-r49/seats/ConnectSiblingOverlap/`. No tools installed; no patch. Axes: adjacency
(judged); count honesty (Q13/Q14/Q19) as the no-harm guard.

## Findings

1. **The prescribed counter miscounts.** `git -C <repo> grep -c kotoba <commit> --` is substring-blind:
   chousa's 29 files hold 26 that only say `kotobank` (85 tokens, a Japanese dictionary site); kotodama
   has 10 files of Japanese words (`kotobank` 19, `aikotoba` 9, `hanakotoba` 5, `kakekotoba` 2).
   Adding `-w` overcorrects: it drops real lane mentions escaped as `\tkotoba` / `\nkotoba` (kagi 415
   to 390 lines, souji 265 to 261). A token-exact predicate fixes both (table below). This is the
   round's M29 "content-blind counter" defect (R2) in a new place.
2. **Reverse direction: 18 of 20 siblings mention kotoba, but only 3 make a scope claim.** Scope-claim
   mentions: kengaku (description `SKILL.md:3` + `PROVINCE.md` five lines :30,:35,:62,:83,:138),
   kotodama (description `SKILL.md:3` + `PROVINCE.md:20`), kumitate (`PROVINCE.md:27`). Three more are
   in skill bodies but are not scope claims: kagi `SKILL.md:297` (defect history), tabi `SKILL.md:1313`
   and `:1450` (a `LANES=` list). All other mentions are history. kagi (112 of 161 files) and kengaku
   (257 of 326) are mostly `/sandboxes/` or `/scratch/` copies. audio and revenger: zero.
3. **Sibling-to-sibling arbitration (kotoba excluded): 17 directed pairs across 8 descriptions.**
   8 pairs carry an explicit ownership rule, and 9 are anti-trigger routes only. Only **one pair is
   reciprocal** (chousa and kengaku). Three pairs point at lanes with no `SKILL.md` at their pins
   (game-dev-3d to game-dev-2d, game-dev-3d to revenger, lore to game-dev-2d).
4. **kotoba's description names 5 of 20 siblings and omits 15**, including kotodama, whose description
   routes skill craft to kotoba. The description names kagi and kake, which § Adjacent omits; § Adjacent
   names 7 lanes the description omits; 8 lanes are on neither surface (detail in (c)).
5. **Superseded**: round 7's "0/5 arbitration clauses" is now 1/5 (same five) and 4/17 labelled fleet-wide;
   round 21's population of five is now 17 `SKILL.md` over 20 lanes; its 14 dead tokens were not re-measured.

## (a) Mentions per lane (pins in `pins.txt`; master tip, or HEAD where master is absent)

Columns: substring = `git -C <repo> grep -c kotoba <commit> --`. Token = the same command with
`-P '(?<!ai|hana|Hana|kake|makura|_makura|_kake)kotoba(?![a-z])'`. Both exit 0, except exit 1 for audio
and revenger (no match). Bucket columns use the token predicate. "copies" means paths with
`/sandboxes/` or `/scratch/`. "hist" means `.ufo/`, `reports/`, `LOG.md`, `corpus/evidence|lessons/`,
`plans/`, `census/` and `results/`.

| lane (commit) | substring files/lines | token files/lines | scope claim | hist | copies | other |
|---|---|---|---|---|---|---|
| audio (HEAD 7a2fcd4f) | 0/0 | 0/0 | - | 0 | 0 | 0 |
| chousa (6c5eb146) | 29/88 | **3/3** | - | 1 | 0 | 2 |
| game-dev-2d (HEAD 7753d49b) | 3/3 | 3/3 | - | 3 | 0 | 0 |
| game-dev-3d (HEAD 89dd182b) | 2/2 | 2/2 | - | 2 | 0 | 0 |
| kagi (899c50b4) | 161/415 | 161/415 | SKILL.md body only | 40 | 112 | 8 |
| kaidoku (HEAD 08c7a729) | 21/29 | 21/29 | - | 20 | 0 | 1 |
| kake (8ecbefe3) | 3/5 | 3/5 | - | 3 | 0 | 0 |
| kama (5ea4fc44) | 29/90 | 29/90 | - | 25 | 0 | 4 |
| kasegi (1fafde8f) | 4/6 | 4/6 | - | 3 | 0 | 1 |
| kengaku (1f3b0f1e) | 326/946 | 326/946 | description + PROVINCE ×5 | 65 | 257 | 2 |
| kotodama (HEAD 35f0d49f) | 66/128 | **56/105** | description + PROVINCE ×1 | 50 | 0 | 4 |
| kumitate (fac39171) | 6/8 | 6/8 | PROVINCE ×1 | 4 | 0 | 1 |
| lore (HEAD 380ef3ab) | 14/17 | 14/17 | - | 14 | 0 | 0 |
| mado (e33ea304) | 17/26 | 17/26 | - | 17 | 0 | 0 |
| mori (28b79d3d) | 135/244 | 135/244 | - | 131 | 0 | 4 |
| revenger (HEAD 876630db) | 0/0 | 0/0 | - | 0 | 0 | 0 |
| souji (4edb25df) | 139/265 | 139/265 | - | 74 | 0 | 65 (tests/vault fixtures) |
| tabi (e3cf4e0d) | 24/57 | 24/57 | SKILL.md body only (LANES list) | 22 | 0 | 1 |
| tameshi (3b20f073) | 75/130 | 75/130 | - | 73 | 0 | 2 |
| tsukuroi (22fd1642) | 10/14 | 10/14 | - | 7 | 0 | 3 |

Totals: 18 lanes with a mention under either predicate. Substring: 1064 files and 2473 lines (awk sum over
`kotoba-wordboundary.txt`). Token: 1028 files and 2365 lines. The first token run listed kotodama at 57/106,
because the lookbehind did not yet exclude the capitalised `Hanakotoba`. Fleet-level mention counts measure
history volume, not overlap. Kengaku alone is 946 of the 2365 lines.

## (b) Sibling-to-sibling arbitration in descriptions (located quotes, pinned commits above)

Sweep: 21-lane name regex over the 17 sibling `SKILL.md` frontmatters (`pairs.txt`, 17 lines, kotoba
excluded); audio, game-dev-2d and revenger have no `SKILL.md` (their `SHONEN.md` says so). Ownership rule (8):
- kengaku `SKILL.md:3` (4 pairs): "kumitate owns OMP route resolution and fallback policy; kama owns local endpoint health and identity; chousa owns research method; tameshi owns verification-fixture craft".
- lore `SKILL.md:8,10` (2 pairs): "Chousa owns research method (Lore consumes its evidence" and "game-dev-2d owns mechanics (PROVINCE.md:9)".
- game-dev-3d `SKILL.md:3` (1 pair): "Sibling arbitration: 2D fixture patterns are inherited, 2D product surfaces are not".
- souji `SKILL.md:2` (1 pair): "(kagi-shokunin owns credential hygiene)"; its general clause is "contested artifact ownership is reported to the integrator".

Anti-trigger route only, with no ownership rule (9):
- chousa `:3` names kasegi and kengaku: "NOT bounty-program scope (kasegi), NOT model-quality claims (kengaku)".
- game-dev-3d `:3` names revenger: "reverse engineering as an end in itself (`revenger-shokunin`)".
- kotodama `:3` names lore and chousa: "NOT world-bible canon recording ... (lore-shokunin)" and "NOT general source-research method (chousa-shokunin)".
- mori `:3` names kumitate, tsukuroi and kama: "NOT dispatch/orchestration (kumitate), NOT OS package/systemd/driver state (tsukuroi), NOT endpoint health (kama)".
- tameshi `:3` names kama: "route those to the product lane or kama".

Pattern: lanes that put "Sibling arbitration" in their description: 4 of 17 (game-dev-3d, kengaku, lore,
souji); trigger list 8 of 17; anti-trigger 9 of 17. Nine name no sibling: kaidoku plus eight one-line
`Domain specialist —` stubs (kagi, kake, kama, kasegi, kumitate, mado, tabi, tsukuroi). Only chousa↔kengaku
is reciprocal. Side observation: lore `SKILL.md` frontmatter has no `name:` field (lines 1-12).

## (c) kotoba `SKILL.md:1-16` "Sibling boundary" against the 20 lanes

Named (5): kagi, kake, kasegi, kengaku, kumitate (`sed -n 1,16p SKILL.md | grep -oE <regex> | sort -u`).
**Omitted (15)**: audio, chousa, game-dev-2d, game-dev-3d, kaidoku, kama, kotodama, lore, mado, mori,
revenger, souji, tabi, tameshi, tsukuroi. kotodama costs most: it routes prompt and skill craft to
kotoba-shokunin, which does not route back. Line 11 assumes every sibling has a SKILL.md; three do not.
§ Adjacent before-value (plan's awk|grep at `a5adc146`): **10**, matching plan Q19 (chousa kama kasegi kengaku kotodama kumitate mado mori revenger tameshi).

## (d) Earlier measures, and which figures today's counts supersede

- Round 7 (`alwayson-checklist-round7.md:56-57`): "5/5 ... `Domain specialist — scopes X` (0/5 triggers,
  0/5 anti-triggers, 0/5 arbitration clauses)". **Superseded**: same five now 3/5 `— scopes` stubs (kagi a
  stub without "scopes", kengaku rewritten); triggers, anti-triggers, arbitration each 1/5 (kengaku).
  Fleet-wide 8/17, 9/17, 4/17 (tally loop over `desc/*.fm`).
- Round 7 :44 "description now names the 5 sibling `*-shokunin` skills": **superseded**, now 5 of 20.
- Round 21 (`sibling-citation-routing-round21.md:10-27`): "five sibling `SKILL.md` files", 14 dead tokens.
  **Population superseded** (17 `SKILL.md` across 20 lanes); the 14 was not re-run, so it stays a dated
  value. All five files changed since 2026-10-19 (`git -C <lane> log --oneline --since=2026-10-19T00:00:00Z
  <pin> -- SKILL.md | wc -l`: kagi 15, kake 16, kasegi 1, kengaku 8, kumitate 6).

## Cross-check of census rows (09:43-09:50Z; 19 `ROW` lines in `Census*.md`, **kasegi row absent**)
Cited quotes for audio, kotodama, tameshi, lore and chousa reproduce at their pins; counts match (a).
kotodama↔lore is reciprocal across surfaces. chousa names kotoba on no scope surface (token 3 files: a
round-25 seat routing skill craft to kotoba, `MINT.md:52` rejecting kotoba, `SCORECARD.md:479`). The
kotoba→chousa link (`PROVINCE.md:29`, `corpus/QUALITY.md:7-8`) is one-way in docs, two-way in work.
**Pins differ by seat**: kake row `e73d48bb`, kama row `c808ba07` against this report's `8ecbefe3`/`5ea4fc44`.
kama master is now `5c95c8f1`. Token counts, frontmatter and PROVINCE are identical across all three tips, so
no figure moves, but the recheck needs one pin set. **Arbitration column** (definition, for the entry author):
- Rows' de-facto yes set = the 8 descriptions naming a sibling in (b), plus kumitate, whose description names
  no sibling (`SKILL.md:3`, stub); its warrant is PROVINCE-only (`PROVINCE.md:27`).
- Proposed "any scope surface" definition (CensusChousa, now dropped) is **not zero-flip**: PROVINCE cessions
  flip at least game-dev-2d :31, mado :14-15, tabi :15-16, tsukuroi :25-26 (arrows) and kake :34,36 (§ Adjacent
  "X owns" prose) to yes. That's 14+ of 20, too few `no` rows to discriminate. game-dev-2d `PROVINCE.md:10`
  and `:31-32` cede "asset rights/visual direction → art-east-asian-design", a **dangling target** (no fleet lane; only
  `/home/vgpnk/Projects/prymeagnt-archive/research/art-east-asian-design` exists). Its "harness/evidence audits → their owning lanes"
  is named at `:10` (harness-integrity, gate-evidence, rlm-dispatch: prymeagnt lanes, not fleet), so not a cession
  to kotoba, though it borders kotoba `PROVINCE.md:14` (`verify_harness_claims.py`, `compare_harness_independent.py`).
- Recommended: `arbitration` = frontmatter description assigns or refuses a domain to a named sibling (form:
  rule or route), matching the router-visible thesis and the round-7 baseline. Exactly one flip (kumitate to
  no); PROVINCE cessions go in a separate `province-cession` field with siblings and lines.

## Proposed move (one, bounded)

Give each census row a **direction-aware reciprocity cell** from the committed `recheck:` script with the
token predicate: sibling description / sibling PROVINCE / kotoba description / kotoba § Adjacent names the
other. Controls: must-fail on a `kotobank` / `aikotoba` line, must-pass on a `\tkotoba` escape line.
- Adjacency: "names all 20" becomes a measurable non-reciprocity count (kotodama is the live gap).
- Count honesty: closes the R2/M29 mode the plan's own counter reproduces (substring overstates chousa
  about 10×; `-w` undercounts kagi by 25 lines).
- C2 and the SKILL.md frontmatter stay untouched (drift guard); the 15 omissions route to round 50.

## Risks and contradictions (stated, not scored)

- § Adjacent at 20 with the description at 5 **widens** the gap between kotoba's two surfaces (was 12 in
  union, 2 description-only); drift guard and adjacency claim conflict, so the census must record the gap.
  The compound lookbehind list is brittle and `git grep -P` needs PCRE.
**L1 verification:** four controls on the recheck script; token rerun over `pins.txt` = 1028/2365; plan awk|grep = 20 after rewrite.

## Evidence (receipt sha256 prefixes; files in seat scratch)

`pins.txt` a5189f2c8dfb6c52; `kotoba-summary.txt` def5d9bc7c5f305b; `kotoba-wordboundary.txt` de0bc5b258f85d7c;
`kotoba-pcre.txt` 289faebdc0334ff5 (first token run); `kotoba-buckets.txt` 02dc22c6ea31c785; `pairs.txt`
fd45d6d48ef03e12; `desc/*.fm`. All Shell commands exited 0; lane HEAD a5adc146a2995dcc5a95a6d8db6e5674f75191ac.
