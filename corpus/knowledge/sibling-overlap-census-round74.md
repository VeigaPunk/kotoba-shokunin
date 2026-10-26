source: S022 (https://code.claude.com/docs/en/skills, § Frontmatter reference `description` row, § Troubleshooting → Skill triggers too often), S023 (https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview, § Level 1: Metadata (always loaded)), S018 (https://agentskills.io/specification, § `description` field) — cited from the round-49 entry, not re-opened this round; sibling bytes: the 20 sibling lane repos under /home/vgpnk/Projects/shokunin/*-shokunin at the heads frozen in `.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv`
verified-at: 2026-10-25
recheck: `python3 -B verifiers/check_sibling_reread.py --rev <rev>` (exit 0 and `sibling rows re-pinned, re-located and re-diffed at the frozen fleet heads 20 of 20`) and `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md --province PROVINCE.md` (exit 0, `rows 20 verified 20` and `province rows 20 matched 20`); exit 1 names the row whose commit, quote, cell, delta or evidence no longer matches

# Fleet sibling-overlap census, re-read at frozen heads (round 74)

This entry is a re-pin of the round-49 census (`corpus/knowledge/sibling-overlap-census-round49.md`), not a new
method: the classification rule (`:43-64`), its round-50 precedence section (`:246-295`) and the round-51 status of
that rule (`:416-458`) are applied unchanged to the same 20 sibling lanes, each read at the head commit frozen in
`.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv` (written by the L1 before any wave-1 seat ran). It reports
sibling scope; it does not absorb it and edits no sibling (adjacency boundary, `../AXES.md`).

## Why a re-pin

- **15 of 20 siblings' `SKILL.md` or `PROVINCE.md` differed between the round-49 pin and the round-74 head, 5 did
  not** (audio, game-dev-2d, game-dev-3d, kagi, lore): per `## Adjacent` row of `PROVINCE.md` at `1e03d19`,
  `git -C ../<lane>-shokunin diff --shortstat <pin> <freeze head> -- SKILL.md PROVINCE.md` (receipt
  `.ufo/waves/round-74/receipts/sibling-staleness-base.tsv`, line 3: 15 differ). The 15 pins sat 50–312 commits behind
  (`git rev-list --count <pin>..<branch>`: kasegi 50, mori 312); kagi moved 6 commits with both files byte-equal, so a
  commit count alone does not mark a row stale — the `delta` cell below is the test.
- **18 of 20 lanes have a `SKILL.md` at the frozen head, 2 do not** (audio, game-dev-2d): `awk -F'\t' '!/^#/ && NF>=5
  {print ($4=="-"?"NONE":"SKILL.md")}' .ufo/waves/round-74/receipts/sibling-heads-freeze.tsv | sort | uniq -c` →
  `2 NONE`, `18 SKILL.md`. The round-49 entry had 17 and 3: revenger's `SKILL.md` was added after its pin
  (`git -C ../revenger-shokunin log --diff-filter=A --format='%h %ad' --date=short -- SKILL.md` → `cab8085 2026-10-24`),
  and the row's three cells (skill file, names kotoba, arbitration) are recomputed from the file that now exists.
- **Classes now: 10 adjacent, 10 none, 0 contested** — `awk -F' \| ' '/^\| [a-z0-9-]+ \| (main|master) \| [0-9a-f]{40} \|/ {print $5}'
  corpus/knowledge/sibling-overlap-census-round74.md | sort | uniq -c` (the first table below); round 49 had 9 adjacent and 11 none.

## One class changes: tsukuroi `none` → `adjacent` (basis kotoba)

tsukuroi's own bytes did not move toward kotoba (0 whole-word `kotoba` hits in its `SKILL.md` and `PROVINCE.md` at the pin
and at the head: `git -C ../tsukuroi-shokunin grep -n -w -i kotoba <commit> -- SKILL.md PROVINCE.md` prints nothing at
`22fd1642` and at `8bd001f5`). The change is on kotoba's side: this lane's own `SKILL.md` says "host package/initramfs
hooks are tsukuroi's" (§ Hook files by client) and `corpus/knowledge/hook-files-round59.md:20` says "Host package and
initramfs hooks are tsukuroi's", both written after the round-49 pin, while `PROVINCE.md` at `1e03d19` still carried "no
split with kotoba on its scope surfaces" for tsukuroi. The round-49 rule counts a split stated on either side's committed
scope surfaces, corpus files included, and the round-50 precedence section lets a split stated only by kotoba make a
no-claim row `adjacent` — the same footing as kake and kasegi, whose basis is kotoba's own description. The round-59
closure left adjacency unchanged (`corpus/lessons/round-59-verifier-spotcheck.md:156`, "FITS (tsukuroi host hooks kept
apart)") without reading the corpus sentence as a split; the two kotoba records disagreed and this entry resolves them.
A non-`none` class makes `check_sibling_census.py --skill SKILL.md` demand that kotoba's description names the lane in an
ownership clause, so the description now carries "tsukuroi owns host package and initramfs hooks" (this round; the
`Note:` clause was shortened to hold the 1,024-character cap). Whether kotoba-side-only splits should make a row
adjacent is the open provisional-rule question of `.ufo/l0-questions.md` line 105; this entry applies the rule as it
stands and does not extend it.

## Census, round-49 nine cells (what `check_sibling_census.py` reads)

Quotes verbatim at each row's frozen head, whitespace collapsed; `scope quote at` is `path:line` of the frozen blob.

| lane | branch | commit | skill file | classification | names kotoba | arbitration | scope quote at | scope quote |
|---|---|---|---|---|---|---|---|---|
| audio | main | 7a2fcd4f08831154686e4e323031f41fffdb077f | NONE | none | no SKILL.md | no SKILL.md | PROVINCE.md:3 | "Owns: game audio production — SFX (UI, impacts, movement, ambience) and soundtrack (motifs, loops, stems, adaptive layers)" |
| chousa | master | 00f8c7f5272a1d98b6d34913985fa4537e00aaf9 | SKILL.md | adjacent | no | yes: kasegi, kengaku | PROVINCE.md:3 | "deep-research method (調査) — the reusable craft of source research." |
| game-dev-2d | main | 7753d49b16674e122ed134403e7a9b301f2cbf7e | NONE | none | no SKILL.md | no SKILL.md | PROVINCE.md:3 | "Owns: 2D game production verified by executable headless fixtures — loop, input, physics, scenes, camera, UI, levels, juice, export readiness." |
| game-dev-3d | main | 89dd182b70943a20ae9aa6c1ed0e3c9b6e79c080 | SKILL.md | none | no | yes: game-dev-2d, revenger | PROVINCE.md:3 | "Owns: 3D game production verified by executable headless fixtures — 3D movement and collision, spatial queries, camera projection and frustum" |
| kagi | master | 69b61db46be4ed955994f6f1d1cba522bc5f4e97 | SKILL.md | adjacent | no | no | SKILL.md:3 | "secrets & vault ops — the-janitor flows, credential hygiene evidence, vault lifecycle." |
| kaidoku | main | 3b1ab3c9d248b7afbf7fc5e5507d76cd87e26c3c | SKILL.md | none | no | no | SKILL.md:3 | "Domain specialist — reverse engineering of shipped artifacts with REA on this Linux host" |
| kake | master | 20217f23eca15862febe14545523832e21584106 | SKILL.md | adjacent | no | no | SKILL.md:3 | "Domain specialist — web properties & publishing — scopes ds4cc.com, kimi.page/pro mirrors, Pages deploys." |
| kama | master | 3e6fdbe9e0ca1ca5b633d0b312d5561301e924c4 | SKILL.md | adjacent | no | no | SKILL.md:3 | "local model serving & endpoint health — scopes local LLM endpoints, baseURL drift, model-id reconciliation" |
| kasegi | master | a155310d1ee9aacc07c3ce62328105a46c0392b4 | SKILL.md | adjacent | no | no | SKILL.md:3 | "bounty & security research — scopes ~/Projects/bounties, program rules, claim packages" |
| kengaku | master | f9efce3beb0705ec2e04ba3f8f449d10d64cc1dd | SKILL.md | adjacent | yes | yes: chousa, kama, kotoba, kumitate, tameshi | SKILL.md:3 | "Domain specialist — LLM/model research & evaluation — eval design, benchmark selection, offline replay grading, blind shim-cascade leg attribution and interval-calibrated verdicts" |
| kotodama | main | f7104cbce186bc2e1522abf0cfd619cc834628bb | SKILL.md | adjacent | yes | yes: chousa, kotoba, lore | SKILL.md:3 | "Linguistic-cultural worldbuilding (言霊) — conlang craft, myth & symbol systems, era staging, costume/material-culture lexicon, and the coupling between them, feeding the world bible." |
| kumitate | master | 2ca91a0c81542cad5f731049aa55dd2f99ade98d | SKILL.md | adjacent | no | no | PROVINCE.md:3 | "orchestration & tooling — scopes OMP task/hub, ufo-fsd scripts & runtime" |
| lore | main | 380ef3abc7c7af11d7f23e9f9c82bb1937e1f695 | SKILL.md | none | no | yes: chousa, game-dev-2d | PROVINCE.md:3 | "Owns: fictional-world records — entities (characters, places, factions, items), relations, timeline events — with consistency verification and sourced inspiration." |
| mado | master | 62dd798bb08401a8697383552edcc36f109344fa | SKILL.md | none | no | no | SKILL.md:8 | "desktop & compositor craft playbook — the Hyprland/waybar/walker/terminal config plane" |
| mori | master | 24ebc7991e9081348d1aa4f558f994b1f4feccab | SKILL.md | none | no | yes: kama, kumitate, tsukuroi | PROVINCE.md:3 | "fleet & host observability (森) — whether the fleet, its waves and its host are alive and progressing." |
| revenger | main | 6da884c6708fa25a7af013b6fc6802492e3264fa | SKILL.md | none | no | no | PROVINCE.md:3 | "Owns: reverse engineering of shipped artifacts — native binaries, managed assemblies, Electron/JavaScript packages, Android APKs, archives, firmware" |
| souji | master | b8cb4b31ce80e2e3314b88e85d40ea9873180804 | SKILL.md | none | no | yes: kagi | PROVINCE.md:3 | "fleet repository & workspace hygiene (掃除) — receipt-gated removal of stale, duplicate, and already-preserved artifacts." |
| tabi | master | 856fa9e1202179f5cfbd28c1f0efdd4eb1f426bb | SKILL.md | none | no | no | PROVINCE.md:3 | "browser & web-interaction craft (旅, journey) — driving real browsers against real sites with evidence discipline." |
| tameshi | master | a944eb55d64a2e0a77e3561c44bf89faadf04bb9 | SKILL.md | adjacent | no | yes: kama | SKILL.md:3 | "Verification-fixture craft for 'hermetic suites', 'mutation testing', and 'gate fixtures'." |
| tsukuroi | master | 8bd001f58bfda29c92d90d2a7a413825c0ca9fcb | SKILL.md | adjacent | no | no | SKILL.md:3 | "Domain specialist — host operability & system repair." |

## Census with `delta` and `evidence` (what `check_sibling_reread.py` reads)

The same 20 rows plus two cells the counter recomputes. `delta` is `+insertions/-deletions` summed over
`git diff --shortstat <round-49 pin> <frozen head> -- SKILL.md PROVINCE.md` (`none` when empty). `evidence` is
`<path>:<line> <changed|unchanged> "<quote>"`: the line of the committed file that decides the row — the sibling's own file at the
frozen head, or behind `kotoba/` this lane's file at the measured revision — with the flag recomputed against the round-49 pin
(or against the base revision for a `kotoba/` file).

| lane | branch | commit | skill file | classification | names kotoba | arbitration | scope quote at | scope quote | delta | evidence |
|---|---|---|---|---|---|---|---|---|---|---|
| audio | main | 7a2fcd4f08831154686e4e323031f41fffdb077f | NONE | none | no SKILL.md | no SKILL.md | PROVINCE.md:3 | "Owns: game audio production — SFX (UI, impacts, movement, ambience) and soundtrack (motifs, loops, stems, adaptive layers)" | none | PROVINCE.md:3 unchanged "Owns: game audio production — SFX (UI, impacts, movement, ambience) and soundtrack (motifs, loops, stems, adaptive layers)" |
| chousa | master | 00f8c7f5272a1d98b6d34913985fa4537e00aaf9 | SKILL.md | adjacent | no | yes: kasegi, kengaku | PROVINCE.md:3 | "deep-research method (調査) — the reusable craft of source research." | +187/-20 | kotoba/SKILL.md:12 changed "chousa owns the research method; kama owns endpoint verification" |
| game-dev-2d | main | 7753d49b16674e122ed134403e7a9b301f2cbf7e | NONE | none | no SKILL.md | no SKILL.md | PROVINCE.md:3 | "Owns: 2D game production verified by executable headless fixtures — loop, input, physics, scenes, camera, UI, levels, juice, export readiness." | none | PROVINCE.md:3 unchanged "Owns: 2D game production verified by executable headless fixtures — loop, input, physics, scenes, camera, UI, levels, juice, export readiness." |
| game-dev-3d | main | 89dd182b70943a20ae9aa6c1ed0e3c9b6e79c080 | SKILL.md | none | no | yes: game-dev-2d, revenger | PROVINCE.md:3 | "Owns: 3D game production verified by executable headless fixtures — 3D movement and collision, spatial queries, camera projection and frustum" | none | PROVINCE.md:3 unchanged "Owns: 3D game production verified by executable headless fixtures — 3D movement and collision, spatial queries, camera projection and frustum" |
| kagi | master | 69b61db46be4ed955994f6f1d1cba522bc5f4e97 | SKILL.md | adjacent | no | no | SKILL.md:3 | "secrets & vault ops — the-janitor flows, credential hygiene evidence, vault lifecycle." | none | corpus/README.md:97 unchanged "kagi pins its bytes; kotoba owns the checklist/shape reading — no adjudication needed, both are read-only" |
| kaidoku | main | 3b1ab3c9d248b7afbf7fc5e5507d76cd87e26c3c | SKILL.md | none | no | no | SKILL.md:3 | "Domain specialist — reverse engineering of shipped artifacts with REA on this Linux host" | +447/-2 | SKILL.md:3 changed "Domain specialist — reverse engineering of shipped artifacts with REA on this Linux host" |
| kake | master | 20217f23eca15862febe14545523832e21584106 | SKILL.md | adjacent | no | no | SKILL.md:3 | "Domain specialist — web properties & publishing — scopes ds4cc.com, kimi.page/pro mirrors, Pages deploys." | +955/-5 | kotoba/SKILL.md:10 changed "kagi, kake, kasegi, kengaku and kumitate own their own SKILL.md content — this skill audits and reports" |
| kama | master | 3e6fdbe9e0ca1ca5b633d0b312d5561301e924c4 | SKILL.md | adjacent | no | no | SKILL.md:3 | "local model serving & endpoint health — scopes local LLM endpoints, baseURL drift, model-id reconciliation" | +417/-8 | corpus/knowledge/cross-lane-scope.md:29 unchanged "**Kotoba** owns the instruction/agent surface and its model/fallback wording; **kama** owns independent verification of the target endpoint." |
| kasegi | master | a155310d1ee9aacc07c3ce62328105a46c0392b4 | SKILL.md | adjacent | no | no | SKILL.md:3 | "bounty & security research — scopes ~/Projects/bounties, program rules, claim packages" | +72/-1 | kotoba/SKILL.md:10 changed "kagi, kake, kasegi, kengaku and kumitate own their own SKILL.md content — this skill audits and reports" |
| kengaku | master | f9efce3beb0705ec2e04ba3f8f449d10d64cc1dd | SKILL.md | adjacent | yes | yes: chousa, kama, kotoba, kumitate, tameshi | SKILL.md:3 | "Domain specialist — LLM/model research & evaluation — eval design, benchmark selection, offline replay grading, blind shim-cascade leg attribution and interval-calibrated verdicts" | +30/-0 | SKILL.md:3 changed "Sibling arbitration: kotoba owns prompt and skill craft (kengaku keeps only measured capability effects)" |
| kotodama | main | f7104cbce186bc2e1522abf0cfd619cc834628bb | SKILL.md | adjacent | yes | yes: chousa, kotoba, lore | SKILL.md:3 | "Linguistic-cultural worldbuilding (言霊) — conlang craft, myth & symbol systems, era staging, costume/material-culture lexicon, and the coupling between them, feeding the world bible." | +85/-0 | SKILL.md:3 changed "NOT prompt/skill craft (kotoba-shokunin), NOT general source-research method (chousa-shokunin)" |
| kumitate | master | 2ca91a0c81542cad5f731049aa55dd2f99ade98d | SKILL.md | adjacent | no | no | PROVINCE.md:3 | "orchestration & tooling — scopes OMP task/hub, ufo-fsd scripts & runtime" | +106/-12 | PROVINCE.md:28 changed "Local model serving and endpoints → kama. Prompt and skill craft → kotoba. Research method → chousa." |
| lore | main | 380ef3abc7c7af11d7f23e9f9c82bb1937e1f695 | SKILL.md | none | no | yes: chousa, game-dev-2d | PROVINCE.md:3 | "Owns: fictional-world records — entities (characters, places, factions, items), relations, timeline events — with consistency verification and sourced inspiration." | none | PROVINCE.md:3 unchanged "Owns: fictional-world records — entities (characters, places, factions, items), relations, timeline events — with consistency verification and sourced inspiration." |
| mado | master | 62dd798bb08401a8697383552edcc36f109344fa | SKILL.md | none | no | no | SKILL.md:8 | "desktop & compositor craft playbook — the Hyprland/waybar/walker/terminal config plane" | +118/-0 | SKILL.md:8 changed "desktop & compositor craft playbook — the Hyprland/waybar/walker/terminal config plane" |
| mori | master | 24ebc7991e9081348d1aa4f558f994b1f4feccab | SKILL.md | none | no | yes: kama, kumitate, tsukuroi | PROVINCE.md:3 | "fleet & host observability (森) — whether the fleet, its waves and its host are alive and progressing." | +462/-15 | PROVINCE.md:3 changed "fleet & host observability (森) — whether the fleet, its waves and its host are alive and progressing." |
| revenger | main | 6da884c6708fa25a7af013b6fc6802492e3264fa | SKILL.md | none | no | no | PROVINCE.md:3 | "Owns: reverse engineering of shipped artifacts — native binaries, managed assemblies, Electron/JavaScript packages, Android APKs, archives, firmware" | +618/-0 | PROVINCE.md:3 unchanged "Owns: reverse engineering of shipped artifacts — native binaries, managed assemblies, Electron/JavaScript packages, Android APKs, archives, firmware" |
| souji | master | b8cb4b31ce80e2e3314b88e85d40ea9873180804 | SKILL.md | none | no | yes: kagi | PROVINCE.md:3 | "fleet repository & workspace hygiene (掃除) — receipt-gated removal of stale, duplicate, and already-preserved artifacts." | +2/-2 | PROVINCE.md:3 unchanged "fleet repository & workspace hygiene (掃除) — receipt-gated removal of stale, duplicate, and already-preserved artifacts." |
| tabi | master | 856fa9e1202179f5cfbd28c1f0efdd4eb1f426bb | SKILL.md | none | no | no | PROVINCE.md:3 | "browser & web-interaction craft (旅, journey) — driving real browsers against real sites with evidence discipline." | +89/-0 | PROVINCE.md:3 unchanged "browser & web-interaction craft (旅, journey) — driving real browsers against real sites with evidence discipline." |
| tameshi | master | a944eb55d64a2e0a77e3561c44bf89faadf04bb9 | SKILL.md | adjacent | no | yes: kama | SKILL.md:3 | "Verification-fixture craft for 'hermetic suites', 'mutation testing', and 'gate fixtures'." | +108/-43 | corpus/knowledge/fleet-kill-rate-ledger.md:127 unchanged "kotoba `verifiers/*` — file existence is O, their gate-ness is U until a survey admits them" |
| tsukuroi | master | 8bd001f58bfda29c92d90d2a7a413825c0ca9fcb | SKILL.md | adjacent | no | no | SKILL.md:3 | "Domain specialist — host operability & system repair." | +872/-0 | kotoba/SKILL.md:127 changed "writing or running hook code is out of scope (round-13 census), and host package/initramfs hooks are tsukuroi's" |

## What changed since round 49, per lane

| lane | r49 pin | r74 head | delta (SKILL.md, PROVINCE.md) | class r49 → r74 |
|---|---|---|---|---|
| audio | `7a2fcd4f` | `7a2fcd4f` | none | none → none |
| chousa | `6c5eb146` | `00f8c7f5` | +187/-20 | adjacent → adjacent |
| game-dev-2d | `7753d49b` | `7753d49b` | none | none → none |
| game-dev-3d | `89dd182b` | `89dd182b` | none | none → none |
| kagi | `899c50b4` | `69b61db4` | none | adjacent → adjacent |
| kaidoku | `08c7a729` | `3b1ab3c9` | +447/-2 | none → none |
| kake | `e73d48bb` | `20217f23` | +955/-5 | adjacent → adjacent |
| kama | `c808ba07` | `3e6fdbe9` | +417/-8 | adjacent → adjacent |
| kasegi | `1fafde8f` | `a155310d` | +72/-1 | adjacent → adjacent |
| kengaku | `1f3b0f1e` | `f9efce3b` | +30/-0 | adjacent → adjacent |
| kotodama | `35f0d49f` | `f7104cbc` | +85/-0 | adjacent → adjacent |
| kumitate | `fac39171` | `2ca91a0c` | +106/-12 | adjacent → adjacent |
| lore | `380ef3ab` | `380ef3ab` | none | none → none |
| mado | `e33ea304` | `62dd798b` | +118/-0 | none → none |
| mori | `28b79d3d` | `24ebc799` | +462/-15 | none → none |
| revenger | `876630db` | `6da884c6` | +618/-0 | none → none |
| souji | `4edb25df` | `b8cb4b31` | +2/-2 | none → none |
| tabi | `e3cf4e0d` | `856fa9e1` | +89/-0 | none → none |
| tameshi | `3b20f073` | `a944eb55` | +108/-43 | adjacent → adjacent |
| tsukuroi | `22fd1642` | `8bd001f5` | +872/-0 | none → adjacent |

Boundary sentences for the 20 lanes are in `PROVINCE.md` § Adjacent, each from the lane's scout record
(`.ufo/waves/round-74/w1/build/ScoutSib*R74/<lane>.json`, field `boundary`). Two of them correct a round-49 wording rather than
move a class: game-dev-3d's row said its frontmatter audits cover only its own and vendored skill files, which no sentence of its
`SKILL.md`, `PROVINCE.md` or `corpus/README.md` at the head carries (`git -C ../game-dev-3d-shokunin grep -n -i frontmatter <head> --
SKILL.md PROVINCE.md corpus/README.md` hits only a vendored analysis, `ScoutSibGamedev3dLoreR74`); revenger's row said "no skill file
at the pin", true at `876630db` and false at the head.

## Limits

- **The counter measures pins, cells, quotes, deltas and evidence lines; it does not measure judgement.** Whether `adjacent`,
  `contested` or `none` is the right class, and whether a boundary sentence reads correctly, is assigned to the wave-2
  reviewers, whose reviews are cited in the round report and not counted here. A mechanical re-pin with recomputed cells reaches a
  high count by itself; the round report states the measured figure.
- **Siblings keep moving after the freeze.** Rows are valid at their commit cells, not at the round end:
  `git -C ../<lane>-shokunin rev-list --count <commit>..refs/heads/<branch>` per row (4 of 20 branches had moved when this
  entry was first drafted: kake, kasegi, kotodama, souji).
- **Documentary evidence about sibling files, not router behaviour.** The lane `SKILL.md` files sit outside the omp skill
  discovery roots (kotoba's description, line 18 of `SKILL.md`), so `arbitration` and `names kotoba` are audit-side facts about
  committed bytes; a description that names a neighbour is not an observation that a request routes to it.
- **The mechanical `none` rule is the base checker's:** a `none` row is refused when the sibling's frontmatter `description` or
  `PROVINCE.md` names kotoba (`verifiers/check_sibling_census.py:595-604`). tabi's frozen `SKILL.md` body carries the whole word
  twice inside one watchdog roster string (`git -C ../tabi-shokunin show 856fa9e1:SKILL.md | grep -n -w -i kotoba` → lines 1313
  and 1450, the same two at the round-49 pin): a citation, not a split, so tabi stays `none`; the counter prints such lanes and
  does not count them.
- **Quote shape.** Six words or more and found within two lines of `path:line` (base rule); a quote that stops mid-sentence
  where the physical line wraps (mori, game-dev-3d, revenger) is the first 25 words of two collapsed lines, stated here so it
  is not read as a sentence.

## Recheck

1. `python3 -B verifiers/check_sibling_reread.py --rev <rev>` — one row per frozen lane, commit cell equal to the freeze head and
   an ancestor of the lane's branch, `delta` and `evidence` recomputed, `PROVINCE.md` § Adjacent equal; exit 0 only at 20 of 20.
2. `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md --province PROVINCE.md` — the
   base checker over the nine-cell table and `PROVINCE.md` § Adjacent (`rows 20 verified 20`, `province rows 20 matched 20`).
3. A failure names the row; first check that the lane still resolves the commit (`git -C ../<lane>-shokunin cat-file -t <commit>`).
