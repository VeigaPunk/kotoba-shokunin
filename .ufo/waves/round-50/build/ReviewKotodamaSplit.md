# ReviewKotodamaSplit — attack the kotodama facts behind C1 (round 50 build)

HOLDS-BOUNDED — the census's kotodama `none` → `adjacent` override survives every attack I could
mount under the census rule's text; the verbatim quotes check out at pin and tip. Bounded by three
citation-hygiene nits (N1-N3), none of which moves the row: C1's 9-of-9 target keeps kotodama.

Lane repo for facts: /home/vgpnk/Projects/shokunin/kotodama-shokunin, read-only via
`git rev-parse`/`show` only. Pin 35f0d49f96f1d51f8b006136a8e1d0e8d0919a7a (branch `main`;
`rev-parse main` = same hash, reported by the round-49 seat and consistent with the census row).
Tip at read time: HEAD = 5b7ecfb600b10f37f76a84a68c384e33a0755fb9 (advanced since the round-49
seat saw HEAD = pin, detached).

## 1. Quotes, verbatim (identical bytes at pin and tip)

Blob identity, `git -C <kotodama> rev-parse <pin>:SKILL.md HEAD:SKILL.md <pin>:MINT.md HEAD:MINT.md`
→ `14b6524e39d24038d508d1f7b4610933e3973178` / `14b6524e…` (equal) and
`355d49d559661c7f2750aea1ca05bd46a99e1a29` / `355d49d5…` (equal). So every quote below holds
verbatim at pin 35f0d49f AND at tip 5b7ecfb6, same line numbers.

**kotodama SKILL.md:3 (frontmatter `description`, full line):**

> description: "Linguistic-cultural worldbuilding (言霊) — conlang craft, myth & symbol systems,
> era staging, costume/material-culture lexicon, and the coupling between them, feeding the world
> bible. Triggers: 'design a language', 'conlang', 'culture for this world', 'mythology of',
> 'symbolism of', 'naming system', 'costume/dress terms', 'era language stages', 'word for this
> concept'. Anti-trigger: NOT world-bible canon recording or consistency verification
> (lore-shokunin), NOT prompt/skill craft (kotoba-shokunin), NOT general source-research method
> (chousa-shokunin), NOT real-world rights/attribution rulings. Rank: shonen."

The clause C1 rests on: `NOT prompt/skill craft (kotoba-shokunin)` — one occurrence of `kotoba`
in the whole file (`grep -c kotoba` → 1, line 3).

**kotodama MINT.md:20-21 (name-collision note; the census cites ":20", the quote ends on :21):**

> provinces name lore explicitly); kotoba owns prompt/skill craft despite
> its name.

Quoted text: "kotoba owns prompt/skill craft despite its name" (spans lines 20-21).

**Corroborating enumerated surface, kotodama PROVINCE.md:20 (Refuses list):** "…web publishing
(kake); prompt/skill craft (kotoba)." — the census's override sentence cites SKILL.md:3 and
MINT.md:20 but not this line; it should (see A1).

## 2. Reciprocal clause kotoba's description must carry (20 words)

> NOT linguistic-cultural worldbuilding (kotodama-shokunin): kotodama owns conlang, myth, era and
> costume systems; kotoba owns prompt/skill-craft wording despite the similar name.

Accuracy check of the three required elements: (a) what kotodama owns — conlang, myth/symbol,
era-staging, costume lexicon (its SKILL.md:3 description and PROVINCE.md § Owns); (b) what kotoba
owns — prompt/skill craft, the exact area kotodama's anti-trigger and PROVINCE.md:20 cede, and the
area MINT.md:20-21 assigns to kotoba outright; (c) the name collision — both lane names named
adjacent, plus "similar name" (kotoba 言葉 / kotodama 言霊, both word-names; MINT.md:20-21 "despite
its name" implies it; the round-49 seat CensusKotodama.md finding 4 states it explicitly).
The census's own finding 2 says the fix is a description edit — this clause is that edit.

## 3. Attack on the override (seat call `none` → census `adjacent`) under the rule's text

Rule (census § Classification rule): `adjacent` = "either side's committed scope surfaces
(SKILL.md including its frontmatter description, PROVINCE.md, corpus files) state a split of one
artifact, function or trigger area between the sibling and kotoba."
Override sentence: "One override of a seat's call: kotodama's seat chose `none`; this entry records
`adjacent`, because kotodama's description refuses kotoba's craft by name … and its `MINT.md:20`
records the name collision … That is a published split of a trigger area."

- **A1 Surface enumeration.** MINT.md is not among the rule's named surfaces (SKILL.md incl.
  frontmatter description, PROVINCE.md, corpus files); a strict reading makes the MINT citation
  out of scope. Disposition: the override survives — SKILL.md:3 is enumerated and states the
  cession with the owner named, and kotodama PROVINCE.md:20 (also enumerated) repeats it as an
  explicit routing. MINT.md is corroboration only. Cleaner citation: swap MINT.md:20 for
  PROVINCE.md:20 in the override sentence.
- **A2 Exclusion vs split.** "NOT prompt/skill craft (kotoba-shokunin)" could be read as a bare
  exclusion, not a two-sided split. Disposition: the anti-trigger names kotoba in the owner slot
  and PROVINCE.md's Refuses list routes each refused area to a named lane; "trigger area" is one
  of the rule's enumerated split objects, and an anti-trigger is literally a statement about a
  trigger area. The seat's contrary reading (its finding 2: kotodama holds "an *instance* of
  SKILL.md, not a half of its governance"; "the overlap set is empty") imports a shared-governance
  requirement the rule's text does not contain. The seat's own report is internally split —
  findings 3-4 record the arbitration clause naming kotoba and recommend keeping kotodama in
  § Adjacent "on that ground" — which is exactly the tension the census resolved.
- **A3 "Override" framing.** The rule's arms are functions of committed bytes; the rule contains
  no override clause and takes no seat call as input. Under the rule's text the census
  re-applied an arm the seat misapplied — a correction, not an override. The word "override" has
  no textual anchor. Wording finding only; no effect on the classification.
- **A4 Forced moves elsewhere.** The same reading does not move lore or chousa: the arm requires
  a split "between the sibling and kotoba", and kotodama's refusals split kotodama–lore and
  kotodama–chousa, not lore–kotoba or chousa–kotoba. Chousa is adjacent on kotoba-side grounds;
  lore stays `none`. No other row depends on this override.
- **A5 Mechanical cells reproduced.** names kotoba = yes; arbitration = yes: chousa, kotoba, lore
  — all three `-shokunin` tokens are in the description bytes; scope quote SKILL.md:8-10 matches
  the census cell; SKILL.md present at the pin.
- **A6 Pin currency.** SKILL.md and MINT.md blobs are identical at pin and current tip, so C1's
  reliance is stable as of 2026-10-22. The census's own limit ("pins move; every claim is about
  the pinned commit") still applies to future reads.

## 4. Nits (diagnostics; no row movement)

- N1: the census cites "MINT.md:20" for a quote whose last word is on line 21; cite MINT.md:20-21.
- N2: "records the name collision" overstates line 20-21, which records the ownership ruling
  ("… despite its name"); the collision itself (both names are word-names) is implied context,
  stated explicitly only in `.ufo/waves/round-49/build/CensusKotodama.md` finding 4. Suggest
  "implies the name collision (kotoba 言葉 / kotodama 言霊)" or add the seat citation.
- N3: at base f3046466 the guard has no `--skill` arm (exit 2, "unrecognized arguments") — correct
  base state; the `--skill SKILL.md` invocation in the plan is the round-50 C1 deliverable, so its
  absence at base is not a defect, just a fact a falsifier should not misread.

## 5. Impact on C1

Kotodama stays one of the 9 non-`none` census lanes (chousa, kagi, kake, kama, kasegi, kengaku,
kotodama, kumitate, tameshi); the override stands on enumerated-surface text, so the C1 statement
"5 of 9 → 9 of 9" needs no re-declaration under the plan's D3 clause.

## 6. Evidence (commands and exit codes, 2026-10-22)

- `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin rev-parse HEAD` →
  `5b7ecfb600b10f37f76a84a68c384e33a0755fb9`, exit 0.
- `git -C … rev-parse 35f0d49f…:SKILL.md HEAD:SKILL.md 35f0d49f…:MINT.md HEAD:MINT.md` → blob ids
  above, exit 0 (pin = tip for both files).
- `git -C … show 35f0d49f…:SKILL.md` (full; description on line 3) and `… show HEAD:SKILL.md |
  awk 'NR<=5'` → identical frontmatter, exit 0.
- `git -C … show 35f0d49f…:MINT.md | awk 'NR>=14&&NR<=22'` and same at HEAD → identical, exit 0.
- `git -C … show 35f0d49f…:PROVINCE.md | awk 'NR>=16&&NR<=21'` → Refuses line 20, exit 0.
- `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md
  --province PROVINCE.md` (from the kotoba lane root) → "rows 20 verified 20 / province rows 20
  matched 20", exit 0.
- Same with `--skill SKILL.md` → exit 2 "unrecognized arguments" (see N3).
- Bounds: kotodama accessed read-only via `git rev-parse`/`show` only; no jj; no git writes
  anywhere; only this report file written in the lane. Tooling: nothing installed or upgraded
  (pacman host-wide paused; no need arose).

## 7. Residual risk and verification gaps

- I relied on the round-49 seat's sweep for the tools/-negative claims (no kotoba-craft instrument
  in kotodama `tools/`); I did not re-sweep all 68 kotoba-mentioning paths myself. Nothing in my
  scope (description, MINT, PROVINCE, classification rule) depends on it.
- Tip is a moving target (it advanced during round 51 work between the round-49 seat and now);
  blob identity is verified as of this seat's reads, not permanently.
- I did not run kotoba's C1 counter command or edit any description — that is the C1 executor's
  deliverable; my scope was the facts and the override's textual footing.
