# ScoutSibKaidokuKakeR74 — C2 re-read: kaidoku, kake

**Verdict:** proposals do NOT differ from r49 for either lane (kaidoku `none`, kake `adjacent`); both sibling files changed (kaidoku +447/-2, kake +955/-5) but neither now names kotoba. Freeze blobs match (`git rev-parse <head>:SKILL.md <head>:PROVINCE.md` equals the freeze row for both). Not run: `check_sibling_census.py` on the proposed rows (the entry file does not exist yet; unobserved). Only committed bytes at the frozen heads were read.

Files: `.ufo/waves/round-74/w1/build/ScoutSibKaidokuKakeR74/kaidoku.json`, `kake.json` (full text pasted below).

## kaidoku — head 3b1ab3c9d248b7afbf7fc5e5507d76cd87e26c3c, `none`
- Clause: `none`. kotoba hits (whole word) in SKILL.md 0, PROVINCE.md 0, corpus/README.md 0 (`git show <head>:<f> | grep -n -w -i kotoba | wc -l`). Tree-wide `git grep -n -w -i kotoba <head> -- . ':!LOG.md' ':!.ufo'` → `EXAMPLE.kama.md:32`, `:51` only: a copy of kama's MINT.md listing kotoba as kama's neighbour (`kotoba | prompt & skill craft | instruction surfaces, not services`), a kama/kotoba split, not kaidoku's.
- Delta: `git diff --shortstat 08c7a72… <head> -- SKILL.md PROVINCE.md` → `2 files changed, 447 insertions(+), 2 deletions(-)`; `rev-list --count` → 121.
- Quote `SKILL.md:3`: `sed -n 3p | grep -c '<quote>'` → 1 (quote is the first 14 words after `description: `, trailing text dropped).
- Open sibling item unchanged: kaidoku/revenger boundary (`SKILL.md:677` "remains an open L0 question").
- Boundary: kaidoku owns reverse engineering of shipped artifacts with REA (SKILL.md:3); kotoba owns prompt and skill craft; kaidoku's only open split is with revenger (SKILL.md:677), not kotoba, and no kaidoku scope file names kotoba.

## kake — head 20217f23eca15862febe14545523832e21584106, `adjacent`
- Clause 2 (kotoba side): kotoba description at base `1e03d19` SKILL.md:10-11 "own their own SKILL.md content — this skill audits and reports" names kake. kake's own scope surfaces (SKILL.md, PROVINCE.md § Adjacent lines 32-41: tabi, chousa, kagi, kama) do not name kotoba; basis is kotoba-only, matching kotoba's base PROVINCE row (basis kotoba). Sibling-side corroboration only in a kotoba-filed mirror lesson, line 5: "Aggregator-owned file; the owning lane corrects `SKILL.md`." (r49 cited `:4-5`; still lines 4-5, a note that the r50 "basis both" and the PROVINCE "basis kotoba" statements disagree — recorded, not ruled).
- kotoba hits: SKILL.md 0, PROVINCE.md 0, corpus/README.md 0; tree-wide only `corpus/lessons/round-5-aggregator-mirror-pathless-cli-invocation.md:4` and `:6`.
- Delta: `2 files changed, 955 insertions(+), 5 deletions(-)`; `rev-list --count` 248.
- Not contested: `grep -c -i 'prompt|AGENTS\.md|frontmatter'` SKILL.md 1 (`:372`, mission prompts of another repo), PROVINCE.md 0; the 23 `SKILL.md` hits in kake SKILL.md are kake's own property-map audit rows.
- Live drift after freeze: `refs/heads/master` is 1 commit past the freeze head; `diff --shortstat head..master -- SKILL.md PROVINCE.md` empty. kaidoku `main` equals the freeze head.
- Boundary: kake owns web properties and Pages publishing (SKILL.md:3); kotoba audits and reports kake's SKILL.md wording while kake corrects it (kotoba SKILL.md:10-11 at 1e03d19); no kake scope file names kotoba (0 hits).

## JSON
```json
{
 "lane": "kaidoku",
 "head40": "3b1ab3c9d248b7afbf7fc5e5507d76cd87e26c3c",
 "r49_classification": "none",
 "r49_pin": "08c7a7299ed61c3fdc30ddb0adfe4e812d5eac76",
 "proposed_classification": "none",
 "decision": "`none` clause: neither of the two other arms fires. No contested claim: the scope surfaces name no SKILL.md/prompt/AGENTS.md authoring (SKILL.md:3 and PROVINCE.md:3 are reverse engineering only). No adjacent split: whole-word kotoba count is 0 in SKILL.md, PROVINCE.md and corpus/README.md at the head; kotoba's description at base 1e03d19 SKILL.md:10-12 does not name kaidoku. Deciding sibling sentence (SKILL.md:3): 'Anti-trigger: ordinary source repositories — use normal repo tools, never run REA on available source.' names no craft area. The only tree-wide whole-word hits are EXAMPLE.kama.md:32,51, a verbatim copy of kama's MINT.md (a kama/kotoba split, not kaidoku's).",
 "changed": "Classification: no. Bytes: yes — `git diff --shortstat 08c7a72 3b1ab3c -- SKILL.md PROVINCE.md` = 2 files changed, 447 insertions(+), 2 deletions(-) (121 commits); the additions are REA 6.5.0-6.7.0 pins, Ghidra/JDK reverification, new Core rows and queue-drain craft, none naming kotoba (0 hits both pins and head). The r49 pin did not show the extra scope words 'managed assemblies, firmware images and recorded crashes' in the description; they do not touch kotoba's ground.",
 "skill_file": "SKILL.md",
 "quote": "Domain specialist — reverse engineering of shipped artifacts with REA on this Linux host",
 "quote_path_line": "SKILL.md:3",
 "kotoba_mentions": [],
 "kotoba_mentions_other_files": [
  {
   "path": "EXAMPLE.kama.md:32",
   "kind": "citation"
  },
  {
   "path": "EXAMPLE.kama.md:51",
   "kind": "citation"
  }
 ],
 "boundary": "kaidoku owns reverse engineering of shipped artifacts with REA (SKILL.md:3); kotoba owns prompt and skill craft; kaidoku's only open split is with revenger (SKILL.md:677), not kotoba, and no kaidoku scope file names kotoba.",
 "sweep": [
  "git -C kaidoku-shokunin cat-file -t 3b1ab3c9d248b7afbf7fc5e5507d76cd87e26c3c -> commit",
  "git -C kaidoku-shokunin rev-parse <head>:SKILL.md <head>:PROVINCE.md -> aa46a42b3c7d4ca8c36a1302662f0277bf92dd63 d453a29ddeb6e6a48bc59ccb863d7fff24c08f6f (equal to the freeze row)",
  "git -C kaidoku-shokunin show <head>:SKILL.md | grep -n -w -i kotoba | wc -l -> 0",
  "git -C kaidoku-shokunin show <head>:PROVINCE.md | grep -n -w -i kotoba | wc -l -> 0",
  "git -C kaidoku-shokunin show <head>:corpus/README.md | grep -n -w -i kotoba -> (empty)",
  "git -C kaidoku-shokunin grep -n -w -i kotoba <head> -- . ':!LOG.md' ':!.ufo' -> EXAMPLE.kama.md:32 and :51 only",
  "grep -c -i -E 'prompt|AGENTS\\.md|frontmatter' on head SKILL.md and PROVINCE.md -> 0 each; 'SKILL.md' hits are the lane's own line cites and the REA package skill (PROVINCE.md:336,349,351 are about REA tools)",
  "git -C kaidoku-shokunin grep -n -i -E 'prompt craft|skill craft|write a skill|audit.*SKILL|owns.*SKILL\\.md' <head> -- . ':!LOG.md' ':!.ufo' -> no scope-surface hit (only EXAMPLE.kama.md:51 'kotoba | prompt & skill craft', SOURCES/knowledge lines unrelated)",
  "git -C kaidoku-shokunin merge-base --is-ancestor 08c7a72 <head> -> yes; git rev-list --count 08c7a72..<head> -> 121",
  "git -C kaidoku-shokunin diff --shortstat 08c7a7299ed61c3fdc30ddb0adfe4e812d5eac76 <head> -- SKILL.md PROVINCE.md -> 2 files changed, 447 insertions(+), 2 deletions(-)",
  "git -C kaidoku-shokunin show <head>:SKILL.md | sed -n 3p | grep -c 'Domain specialist — reverse engineering of shipped artifacts with REA on this Linux host' -> 1",
  "description sibling-name sweep (grep -o -w -i over the lane list on SKILL.md:3) -> none (arbitration cell: no)"
 ]
}
```
```json
{
 "lane": "kake",
 "head40": "20217f23eca15862febe14545523832e21584106",
 "r49_classification": "adjacent",
 "r49_pin": "e73d48bbf20759fc7758afaebf841fa02e5cfbbf",
 "proposed_classification": "adjacent",
 "decision": "`adjacent` clause 2 of the r49 rule, kotoba side: kotoba's own description (base 1e03d19 SKILL.md:10-11) states 'kagi, kake, kasegi, kengaku and kumitate own their own SKILL.md content — this skill audits and reports'. Not `contested`: kake's scope surfaces (SKILL.md:3, PROVINCE.md:3,5,12-18) claim no SKILL.md/prompt/AGENTS.md authoring of other lanes; the 23 'SKILL.md' hits in kake SKILL.md are the lane's own property-map audit rows. Not `none`: the split is stated by kotoba and kake's PROVINCE.md § Adjacent (lines 32-41) names tabi, chousa, kagi, kama but not kotoba, so basis is kotoba only, as kotoba's base PROVINCE row says. Kake-side sentence at head (lesson line 5): 'Aggregator-owned file; the owning lane corrects `SKILL.md`.' is in a kotoba-filed mirror, corroboration only.",
 "changed": "Classification: no; basis: no change (kotoba-side; sibling surfaces still silent on kotoba). Bytes: yes — `git diff --shortstat e73d48b 20217f2 -- SKILL.md PROVINCE.md` = 2 files changed, 955 insertions(+), 5 deletions(-) (248 commits): kake gained PROVINCE.md Core/Frontier/Adjacent/Surfaces sections (lines 10-60) naming tabi, chousa, kagi, kama as split partners, and a SKILL.md registry-audit block; none names kotoba. Line move: the r49 lesson cite ':4-5' now reads lines 4 (Filed by kotoba) and 5 (owning lane corrects SKILL.md); unchanged text.",
 "skill_file": "SKILL.md",
 "quote": "Domain specialist — web properties & publishing — scopes ds4cc.com, kimi.page/pro mirrors, Pages deploys.",
 "quote_path_line": "SKILL.md:3",
 "kotoba_mentions": [],
 "kotoba_mentions_other_files": [
  {
   "path": "corpus/lessons/round-5-aggregator-mirror-pathless-cli-invocation.md:4",
   "kind": "citation"
  },
  {
   "path": "corpus/lessons/round-5-aggregator-mirror-pathless-cli-invocation.md:6",
   "kind": "citation"
  }
 ],
 "boundary": "kake owns web properties and Pages publishing (SKILL.md:3); kotoba audits and reports kake's SKILL.md wording while kake corrects it (kotoba SKILL.md:10-11 at 1e03d19); no kake scope file names kotoba (0 hits).",
 "sweep": [
  "git -C kake-shokunin cat-file -t 20217f23eca15862febe14545523832e21584106 -> commit",
  "git -C kake-shokunin rev-parse <head>:SKILL.md <head>:PROVINCE.md -> 35626e09cec6e2dad189a8e3ddc3e79977b865cf 175fdab38832d9d79a390063e4b76ecf438706ec (equal to the freeze row)",
  "git -C kake-shokunin show <head>:SKILL.md | grep -n -w -i kotoba | wc -l -> 0; same for :PROVINCE.md -> 0; :corpus/README.md -> 0",
  "git -C kake-shokunin grep -n -w -i kotoba <head> -- . ':!LOG.md' ':!.ufo' -> corpus/lessons/round-5-aggregator-mirror-pathless-cli-invocation.md:4 and :6 only",
  "git -C kake-shokunin grep -n -i -E 'owning lane corrects|owns? (its|their) own SKILL|prompt craft|skill craft|route.*(to|findings to) kotoba' <head> -- . ':!LOG.md' ':!.ufo' -> lesson line 5 only",
  "grep -c -i -E 'prompt|AGENTS\\.md|frontmatter' on head SKILL.md -> 1 ('prompt' at :372, mission prompts under ufofsdbeta), PROVINCE.md -> 0",
  "description sibling-name sweep (grep -o -w -i over lane list on SKILL.md:3) -> none (arbitration cell: no)",
  "git -C kake-shokunin merge-base --is-ancestor e73d48b <head> -> yes; rev-list --count e73d48b..<head> -> 248",
  "git -C kake-shokunin diff --shortstat e73d48bbf20759fc7758afaebf841fa02e5cfbbf <head> -- SKILL.md PROVINCE.md -> 2 files changed, 955 insertions(+), 5 deletions(-)",
  "git -C kake-shokunin show <head>:SKILL.md | sed -n 3p -> 'description: Domain specialist — web properties & publishing — scopes ds4cc.com, kimi.page/pro mirrors, Pages deploys. Rank: shonen.'",
  "git -C kotoba-shokunin show 1e03d19:SKILL.md | grep -n 'own their own SKILL' -> 11: own their own SKILL.md content — this skill audits and reports; fixes route",
  "live branch after freeze: refs/heads/master is 1 commit ahead of the freeze head; diff --shortstat head..master -- SKILL.md PROVINCE.md -> empty (no scope change)"
 ]
}
```
