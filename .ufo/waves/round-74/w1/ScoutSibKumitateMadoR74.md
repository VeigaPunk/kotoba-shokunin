# ScoutSibKumitateMadoR74 — C2 sibling re-read: kumitate, mado

**Verdict:** both proposals EQUAL r49 — kumitate `adjacent`, mado `none`. No classification differs from r49; what moved is bytes (kumitate +106/-12, mado +118 lines at the frozen heads), not the deciding sentences.

Method: only committed bytes at the freeze heads (`git -C /home/vgpnk/Projects/shokunin/<lane>-shokunin show <head40>:<path>`); never the working tree. Heads and blob ids were checked against `receipts/sibling-heads-freeze.tsv` (rev-parse output equals the freeze row for both lanes, and `master` tip equals the head today). Deliverables: `.ufo/waves/round-74/w1/build/ScoutSibKumitateMadoR74/{kumitate,mado}.json` (pasted below). No sibling edited; no network; no tools installed.

## kumitate (head 2ca91a0c…, r49 pin fac39171…)

Deciding clause: `adjacent` — a sibling-side committed scope surface states a split of a trigger area. `git show 2ca91a0c:PROVINCE.md | sed -n 28p` → `- Local model serving and endpoints → kama. Prompt and skill craft → kotoba. Research method → chousa.` The `contested` arm does not fire: kumitate claims no authoring/audit of other lanes' SKILL.md/prompts (sweeps in JSON). Kotoba-side: base SKILL.md:10-11 names kumitate as owning its own SKILL.md content.

Observed:
- `git diff --shortstat fac39171… 2ca91a0c… -- SKILL.md PROVINCE.md` → `2 files changed, 106 insertions(+), 12 deletions(-)`; pin is ancestor (`merge-base --is-ancestor` yes); 225 commits between.
- whole-word kotoba at head, `git grep -n -w -i kotoba 2ca91a0c -- . ':!LOG.md' ':!.ufo'` → 4 hits: PROVINCE.md:28 (split), SCORECARD.md:1722 (split: K-block clause "`skills/*` craft and trigger discipline to **kotoba**"; was :1616 at the pin), corpus/knowledge/kimi-skills-plugins.md:324 (citation), corpus/lessons/round-14.md:77 (citation). SKILL.md: 0 hits.
- Quote line: `sed -n 3p` of PROVINCE.md → `**Domain:** orchestration & tooling — scopes OMP task/hub, ufo-fsd scripts & runtime` (quote drops the leading `**Domain:** `).
- Note: kumitate's SKILL.md description line 3 is `description: Domain specialist — orchestration & tooling — scopes OMP task/hub dispatch, ufo-fsd scripts, crates/ufo-core-runtime. Rank: shonen.`; it names no sibling lane and not kotoba (names kotoba: no; arbitration: no).
- Unobserved: I did not read all 225 commits; the delta was read via diff of SKILL.md/PROVINCE.md only.

## mado (head 62dd798b…, r49 pin e33ea304…)

Deciding clause: `none` — neither clause fires. `git grep -n -w -i kotoba 62dd798b -- . ':!LOG.md' ':!.ufo'` → empty; `git show 62dd798b:SKILL.md | grep -n -w -i kotoba` and the same on PROVINCE.md → empty; `git grep -n -i kotoba 62dd798b -- . ':!.ufo' | wc -l` → 0. Hits exist only under `.ufo/waves/**` wave reports (excluded by the r49 rule). Closest sentence, not a split with kotoba: PROVINCE.md:10 `The omarchy skill (`~/.agents/skills/omarchy/`) is documentation surface,` and SKILL.md `## Omarchy boundary` (read-only; "Editing the skill … never"). The omarchy skill belongs to no fleet lane. Kotoba's base description names no mado (`grep -c -i mado` over lines 1-25 → 0).

Observed:
- `git diff --shortstat e33ea304… 62dd798b… -- SKILL.md PROVINCE.md` → `2 files changed, 118 insertions(+)` (pure additions: PROVINCE round-23…36 refinements + tool table; SKILL.md +42); pin is ancestor; 229 commits between.
- Quote line: `sed -n 8p` of SKILL.md → `desktop & compositor craft playbook — the Hyprland/waybar/walker/terminal config plane`. (Same line and words as the r49 quote; re-located at head, not copied from r49; it is the same sibling bytes.) Frontmatter line 3: `description: Domain specialist — desktop & compositor craft. Rank: shonen (probation).` names no lane.
- Prompt/AGENTS sweep: only SKILL.md:1024 `(AGENTS.md:3)` (LOG-owner note), corpus/README.md 0 hits.

## JSON — kumitate.json
```json
{
 "lane": "kumitate",
 "head40": "2ca91a0c81542cad5f731049aa55dd2f99ade98d",
 "r49_classification": "adjacent",
 "r49_pin": "fac39171ac28c606e90da75fc2ba2ed3df52f4ea",
 "proposed_classification": "adjacent",
 "proposed_classification_clause": "`adjacent` clause (either side's committed scope surfaces state a split of a trigger area): sibling-side sentence at kumitate PROVINCE.md:28 \"Prompt and skill craft → kotoba.\" (head blob). The `contested` clause does not fire: kumitate states no claim to write or audit other lanes' SKILL.md/prompts/AGENTS.md (negative sweeps below). Kotoba-side corroboration: kotoba base SKILL.md:10-11 \"kagi, kake, kasegi, kengaku and kumitate own their own SKILL.md content\".",
 "changed": "No: classification and class-deciding sentence are unchanged. The sentence moved line 27 -> 28 (PROVINCE.md delta at the pin: four frontier bullets gained first-entry text; `git diff --shortstat fac39171 2ca91a0c -- SKILL.md PROVINCE.md` -> `2 files changed, 106 insertions(+), 12 deletions(-)`); SKILL.md delta adds gate-registry rows, none naming kotoba. SCORECARD.md:1722 (was :1616 at the pin) still carries the K-block clause assigning `skills/*` craft and trigger discipline to kotoba.",
 "skill_file": "SKILL.md",
 "quote": "orchestration & tooling — scopes OMP task/hub, ufo-fsd scripts & runtime",
 "quote_path_line": "PROVINCE.md:3",
 "kotoba_mentions": [
  {
   "path_line": "PROVINCE.md:28",
   "kind": "split"
  },
  {
   "path_line": "SKILL.md",
   "kind": "none (0 hits)"
  },
  {
   "path_line": "SCORECARD.md:1722",
   "kind": "split (outside SKILL/PROVINCE; clause A of the K-block boundary)"
  },
  {
   "path_line": "corpus/knowledge/kimi-skills-plugins.md:324",
   "kind": "citation"
  },
  {
   "path_line": "corpus/lessons/round-14.md:77",
   "kind": "citation"
  }
 ],
 "boundary": "kumitate owns dispatch/orchestration tooling and routes \"Prompt and skill craft → kotoba\" (kumitate `PROVINCE.md:28`); kotoba owns the wording, kumitate the runtime, and neither edits the other's SKILL.md.",
 "sweep": [
  "git -C kumitate-shokunin rev-parse 2ca91a0c81542cad5f731049aa55dd2f99ade98d:SKILL.md 2ca91a0c81542cad5f731049aa55dd2f99ade98d:PROVINCE.md -> 533632196114c399b7a5790855a78b41adb351aa / 6a94f01c50a63837dc5a409e4b2d3d446b3745e8 (equal to freeze row); rev-parse master -> head40",
  "git -C kumitate-shokunin diff --shortstat fac39171ac28c606e90da75fc2ba2ed3df52f4ea 2ca91a0c81542cad5f731049aa55dd2f99ade98d -- SKILL.md PROVINCE.md -> 2 files changed, 106 insertions(+), 12 deletions(-); merge-base --is-ancestor pin head -> yes; git log --oneline pin..head | wc -l -> 225",
  "git show <head>:SKILL.md | grep -n -w -i kotoba -> (empty); git show <head>:PROVINCE.md | grep -n -w -i kotoba -> 28:- Local model serving and endpoints → kama. Prompt and skill craft → kotoba. Research method → chousa.",
  "git grep -n -w -i kotoba <head> -- . ':!LOG.md' ':!.ufo' -> 4 hits: PROVINCE.md:28, SCORECARD.md:1722, corpus/knowledge/kimi-skills-plugins.md:324, corpus/lessons/round-14.md:77",
  "git show <head>:PROVINCE.md | sed -n 3p -> **Domain:** orchestration & tooling — scopes OMP task/hub, ufo-fsd scripts & runtime",
  "git show <head>:SKILL.md | sed -n 3p -> description: Domain specialist — orchestration & tooling — scopes OMP task/hub dispatch, ufo-fsd scripts, crates/ufo-core-runtime. Rank: shonen.",
  "contested negative sweep: git show <head>:SKILL.md | grep -n -i prompt -> 9 hits, all dispatch mechanics (item `prompt`, `promptPath`, session prompt, 12 KiB prompt bound), none an authoring/audit claim; PROVINCE.md prompt hits 1 (the :28 split); git grep -i -E 'skill (authoring|craft)|craft of (prompts|skills)|rewrite.*SKILL' <head> -- corpus/README.md SKILL.md PROVINCE.md -> only PROVINCE.md:28; SKILL.md delta added lines naming kotoba|other lane|skill craft -> 0",
  "kumitate's skills/ work audits ~/.kimi-code/skills (corpus/README.md rows kimi-skills-plugins, kimi-modes-machinery), not another lane's SKILL.md; SCORECARD.md:1722 assigns `skills/*` craft to kotoba, a sibling-stated split.",
  "kotoba side: git show 1e03d19:SKILL.md | sed -n 10,11p -> 'Sibling boundary: kagi, kake, kasegi, kengaku and kumitate / own their own SKILL.md content'"
 ]
}```

## JSON — mado.json
```json
{
 "lane": "mado",
 "head40": "62dd798bb08401a8697383552edcc36f109344fa",
 "r49_classification": "none",
 "r49_pin": "e33ea30461f6e9bbeee40beef19770a953f7a105",
 "proposed_classification": "none",
 "proposed_classification_clause": "`none` clause (neither adjacent nor contested): no sibling-side or kotoba-side committed scope surface states a split between mado and kotoba. mado scope files hold 0 whole-word `kotoba` hits and kotoba's description names no mado (`git show 1e03d19:SKILL.md | sed -n 1,25p | grep -c -i mado` -> 0). Closest sentence, not a split with kotoba: PROVINCE.md:10 \"The omarchy skill (`~/.agents/skills/omarchy/`) is documentation surface,\" (read-only, belongs to no fleet lane).",
 "changed": "No: classification unchanged. The delta at the pin is 118 pure insertions (`git diff --shortstat e33ea304 62dd798b -- SKILL.md PROVINCE.md` -> `2 files changed, 118 insertions(+)`): PROVINCE.md round-23..36 refinements and a tool-inventory table; SKILL.md +42 lines (an omarchy boundary section, gate rows). None names kotoba or claims prompt/skill authoring over a lane-owned file.",
 "skill_file": "SKILL.md",
 "quote": "desktop & compositor craft playbook — the Hyprland/waybar/walker/terminal config plane",
 "quote_path_line": "SKILL.md:8",
 "kotoba_mentions": [],
 "boundary": "mado owns the Hyprland/waybar/walker/terminal config plane and display behavior read-only; it states no split with kotoba and treats the omarchy skill as read-only documentation (mado `PROVINCE.md:10`), claiming no lane SKILL.md.",
 "sweep": [
  "git -C mado-shokunin rev-parse 62dd798bb08401a8697383552edcc36f109344fa:SKILL.md 62dd798bb08401a8697383552edcc36f109344fa:PROVINCE.md -> 6c44244575184b08977f1b44b9ccf4a1f68b556d / 22835321ae7fa7e8cc58ef1e887f0a9bbee985df (equal to freeze row); rev-parse master -> head40",
  "git -C mado-shokunin diff --shortstat e33ea30461f6e9bbeee40beef19770a953f7a105 62dd798bb08401a8697383552edcc36f109344fa -- SKILL.md PROVINCE.md -> 2 files changed, 118 insertions(+); merge-base --is-ancestor pin head -> yes; git log --oneline pin..head | wc -l -> 229",
  "git show <head>:SKILL.md | grep -n -w -i kotoba -> (empty); git show <head>:PROVINCE.md | grep -n -w -i kotoba -> (empty)",
  "git grep -n -w -i kotoba <head> -- . ':!LOG.md' ':!.ufo' -> (empty); git grep -n -i kotoba <head> -- . ':!.ufo' | wc -l -> 0 (hits exist only under .ufo/waves wave reports, which the r49 rule excludes)",
  "git show <head>:PROVINCE.md | sed -n 3,4p -> **Domain:** desktop & compositor craft — the Hyprland/waybar/walker / configuration plane and display behavior on this host.",
  "git show <head>:SKILL.md | sed -n 8p -> desktop & compositor craft playbook — the Hyprland/waybar/walker/terminal config plane; sed -n 3p -> description: Domain specialist — desktop & compositor craft. Rank: shonen (probation).",
  "claim sweep: git show <head>:{SKILL,PROVINCE}.md | grep -i -E 'prompt|AGENTS|kotoba' -> only SKILL.md:1024 '(AGENTS.md:3)' (a LOG-owner note) ; corpus/README.md prompt|AGENTS.md -> 0; SKILL.md:~400 `## Omarchy boundary` says skill is 'read-only documentation' and 'never' edited",
  "names no sibling in description (frontmatter has none) so arbitration = none; SKILL.md names tameshi at :624 (harness path) only"
 ]
}```
