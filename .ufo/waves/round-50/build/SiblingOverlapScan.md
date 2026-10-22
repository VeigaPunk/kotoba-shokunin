HOLDS — the round-49 census classification and its names-kotoba and arbitration columns still match every sibling's branch tip (scanned 2026-10-22T12:28:40Z–12:30:01Z): 9 of 20 lanes moved, and none of the movers changed its SKILL.md frontmatter or added a scope-surface line that names kotoba, states a split with kotoba, or claims kotoba-core ground.

Seat: KotobaR50.SiblingOverlapScan (scout, leaf). Lane base: kotoba `master` = `f30464660c675d1c1e2851a3bf0366a3aaffe5a8` (unchanged during the scan). Read-only; no edits outside this report. Tools installed or updated: none.

## Findings

1. **Movers (9 of 20), all fast-forward from the census pin.** Measured with `git rev-parse <branch>`, `rev-list --count pin..tip` and `merge-base --is-ancestor`. Same at tip (11): audio, chousa, game-dev-2d, game-dev-3d, kagi, kasegi, kengaku, lore, revenger, souji, tabi.

| lane | pin | tip | commits | frontmatter | PROVINCE.md | scope-surface lines naming kotoba (added or removed) |
|---|---|---|---|---|---|---|
| kaidoku | 08c7a729 | c27f445e | 6 | byte-identical | unchanged | 0 |
| kake | e73d48bb | 04637bdd | 14 | byte-identical | changed (own Pages base-path frontier) | 0 |
| kama | c808ba07 | 1560e4d8 | 7 | byte-identical | unchanged | 0 |
| kotodama | 35f0d49f | 5b7ecfb6 | 10 | byte-identical | unchanged | 0 |
| kumitate | fac39171 | f69817ed | 9 | byte-identical | unchanged | 0 |
| mado | e33ea304 | 8e5d9369 | 11 | byte-identical | changed (own tools inventory) | 0 |
| mori | 28b79d3d | 248408f5 | 45 | byte-identical | changed (job-runway probe; names kumitate as owner) | 0 |
| tameshi | 3b20f073 | 2227d833 | 13 | byte-identical | changed (ninth mutation leg, kumitate `cite-check.mjs`) | 0 |
| tsukuroi | 22fd1642 | 157ee255 | 10 | byte-identical | unchanged | 0 |

   Full tips: kaidoku c27f445e70cedbaf5300b2fd0a53e821d9b659a9, kake 04637bdd1ac1c76517b764f48bdc83279edd7266, kama 1560e4d83f42b04f40336357de6f9637eafa0f4b, kotodama 5b7ecfb600b10f37f76a84a68c384e33a0755fb9, kumitate f69817edf687c8ce4f87ed7953a353399232f69e, mado 8e5d93691e2f7baa3d4a0a61c9428e5acb5d2122, mori 248408f5b6610a85bcbdebe7ac0b4fa7ed51422a, tameshi 2227d8338c02aa9a5fd7d95c1a41b76865ad7647, tsukuroi 157ee2556a75bf4d1ae4893d4a06c020ae531ac0.
   kotodama's tip moved during the scan (dea5ece6 at 12:28:40Z, then 5b7ecfb6 from 12:29Z). The figures above are for 5b7ecfb6, and other tips may keep moving.

2. **No mover touches the classification.** "Scope surfaces" here means SKILL.md, PROVINCE.md, MINT.md, AGENTS.md and `corpus/` minus `corpus/evidence/`. Across all nine pin-to-tip diffs of those surfaces, 0 added or removed lines contain the whole token `kotoba`. The same diffs contain no sibling, adjacency or ownership line about prompt craft, skill craft, SKILL.md or AGENTS.md authoring, or trigger and frontmatter craft for another lane. The terms that do match are each lane's own round-prompt conformance rows and its own `SKILL.md` registry pointers. The new ownership statements are all between other siblings: mori and tameshi name kumitate as owner, kotodama names the unowned WCAG 1.2.6 scope, and tsukuroi cites mori's PSI note.
   Every census scope quote line (`scope quote at`) is byte-identical at the tip for all 9 movers.

3. **Open "possible contested" elements from round 49 did not move.** kama `corpus/knowledge/consumer-registry.md` and `cross-lane-scope.md` have an empty pin-to-tip diff. tameshi's only `checklist-run` change in SKILL.md is the leg count (`N=8 since round 18` becomes `N=8 since round 18, N=9 since round 26`), with no new reading of kagi's SKILL.md checklist. kengaku did not move, so its round-25 census script is unchanged.

4. **Wave-report mentions of kotoba exist in every mover but are outside the rule.** The census excludes `.ufo/` and `reports/` from scope surfaces. They cover fleet misroot sweeps (the kotoba round-49 `RowGameDev2d.md` landing in the fleet root, `.ufo/state/kotoba.report-baseline`), lane-wide token scans that count kotoba as noise, and connector tables citing kotoba `PROVINCE.md:34` non-claims (kama, kotodama). One item is worth carrying forward, the same kind as the round-49 tabi case: mado `.ufo/waves/round-23/w1/reports/ConnSibling.md` records that mado's tripwire reads the same record type as kotoba's skill-activation telemetry (OMP session JSONL `toolCall` arguments), citing `kotoba-shokunin/corpus/knowledge/skill-activation-telemetry.md:23,66`, with the note "Same record type, telemetry only." It is not a split on mado's scope surfaces, so the mado row stays `none`.

5. **kotodama at its tip still routes prompt and skill craft to kotoba.** At 5b7ecfb6, `SKILL.md:2`, inside the frontmatter `description`, reads "Anti-trigger: NOT world-bible canon recording or consistency verification (lore-shokunin), NOT prompt/skill craft (kotoba-shokunin), NOT general source-research method (chousa-shokunin)". The frontmatter is byte-identical to the pin. `MINT.md:20` still reads "kotoba owns prompt/skill craft despite", and `PROVINCE.md:20` reads "prompt/skill craft (kotoba)." Note: the census cites kotodama's anti-trigger as `SKILL.md:3`, but at both pin and tip the `description` key is on file line 2 (frontmatter body line 1). The quoted text is the same, so this locator is cosmetic.

6. **Reciprocity, at kotoba `f3046466` and each sibling's tip.** The "kotoba names X" column comes from kotoba's frontmatter (the C1 counter's awk extraction). The "X names kotoba" column comes from X's frontmatter `description`. The last column counts whole-token `kotoba` lines on X's other scope surfaces, for context only.

| X | kotoba names X | X names kotoba | reciprocal | X's other surfaces naming kotoba (lines) |
|---|---|---|---|---|
| chousa | no | no | neither side | 0 |
| kagi | yes | no | one-way (kotoba → kagi) | SKILL.md body 1 (`:297`, a defect note about a kotoba path) |
| kake | yes | no | one-way (kotoba → kake) | 0 |
| kama | no | no | neither side | 0 |
| kasegi | yes | no | one-way (kotoba → kasegi) | 0 |
| kengaku | yes | yes | **both** | PROVINCE.md 5 (`:30,35,62,83,138`) |
| kotodama | no | yes | one-way (kotodama → kotoba) | PROVINCE.md 1 (`:20`); MINT.md `:20` |
| kumitate | yes | no | one-way (kotoba → kumitate) | PROVINCE.md 1 (`:27` "Prompt and skill craft → kotoba.") |
| tameshi | no | no | neither side | 0 |

   Totals: kotoba names 5 of 9 (kagi, kake, kasegi, kengaku, kumitate), the C1 "before" value. 2 of 9 name kotoba (kengaku, kotodama). 1 of 9 is reciprocal (kengaku). If C1 lands 9 of 9, kotodama becomes reciprocal, and chousa, kama and tameshi become one-way from kotoba. That leaves 7 one-way pairs, which only sibling-owned description edits could close (out of kotoba's write scope).

## Consequences for C1 (adjacency)

- The C1 lane list (the 9 non-`none` rows) is unaffected by sibling movement: no row's basis changed at the tip.
- kumitate's PROVINCE.md routes prompt and skill craft to kotoba, but its description does not. That is the same surface gap kotoba had (description versus § Adjacent). It is reportable to kumitate, not fixable here.
- Every census claim is pinned. The guard still reads pinned bytes and passes. That is correct for the census, but it means the guard cannot detect tip drift. This scan is the tip-side check for 2026-10-22T12:30Z only.

## Evidence (commands run from `/home/vgpnk/Projects/shokunin/kotoba-shokunin` unless noted; all read-only)

- Pin vs tip, 20 rows: loop over the census rows (`grep -E '^\| [a-z0-9-]+ \| (main|master) \| [0-9a-f]{40} \|' F`) running `git -C ../<lane>-shokunin rev-parse <branch>`, `rev-list --count`, `merge-base --is-ancestor`. Exit 0. Result: 11 SAME, 9 MOVED, all `ff`.
- Frontmatter compare: sha256 of `git show <rev>:SKILL.md | awk 'NR==1&&/^---$/{f=1;next} f&&/^---$/{exit} f'` at pin and tip, plus the `description:` line alone. 20 of 20 identical; rerun at 12:30:01Z with the same result. Exit 0.
- Scope diff: `git -C <lane> diff -U0 <pin> <tip> -- SKILL.md PROVINCE.md MINT.md AGENTS.md corpus ':(exclude)corpus/evidence'`, then a count of `^[+-]` lines (excluding file headers) matching `grep -ciw kotoba`. Result: 0 for each of the 9 movers. Exit 0.
- Whole-tree diff kotoba lines (including `.ufo/`): kaidoku 5, kake 5, kama 8, kotodama 5, kumitate 5, mado 10, mori 15, tameshi 21, tsukuroi 12. All matching lines are under `.ufo/` (files listed by an awk filter on `+++` headers). Exit 0.
- Scope-quote lines: `git show <pin|tip>:<file> | sed -n <line>p | sha256sum` for the 9 movers. 9 of 9 identical. Exit 0.
- kama contested files: `git -C ../kama-shokunin diff --stat c808ba07… <tip> -- corpus/knowledge/consumer-registry.md corpus/knowledge/cross-lane-scope.md` printed nothing. Exit 0.
- kotodama tip: `git -C ../kotodama-shokunin show 5b7ecfb6:SKILL.md | awk '<frontmatter>' | grep -n -E 'kotoba|description'` gives line 2 (quoted above); `show …:MINT.md | sed -n 20p`; `show …:PROVINCE.md | grep -n -i kotoba` gives `20`.
- Reciprocity: per lane, `grep -ciw kotoba` on the frontmatter, PROVINCE.md and SKILL.md body at the tip, and `grep -ciw <lane>` on kotoba's frontmatter at f3046466. Counts as in the table. Exit 0.
- Census guard (pinned bytes): `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` printed `rows 20 verified 20` and `province rows 20 matched 20`. Exit 0.

Scratch: diff captures were written to `/tmp/sos-<lane>.diff` (outside the lane) and removed after the scan.
