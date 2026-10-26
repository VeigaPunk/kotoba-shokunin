# ScoutSibChousaKagiR74 — C2 sibling re-read: chousa, kagi

**Verdict: no proposal differs from r49.** chousa stays `adjacent` (basis kotoba side only), kagi stays `adjacent` (basis both). Only chousa's bytes moved (SKILL.md +187/-20, PROVINCE.md byte-equal); kagi's SKILL.md and PROVINCE.md are byte-equal to the r49 pin. Neither lane's SKILL.md or PROVINCE.md at the head gained the word `kotoba` (kagi has the one r49-era citation at SKILL.md:297). Everything below read committed objects only (`git show <head40>:path`, `git grep <head40>`); no working tree, no edits, no scratch dir created. Unobserved: the base `check_sibling_census.py` was not run on these rows (the L1/counter does that); descriptions here are unconfirmed against any router (no discovery root on this host, r49 § What decides).

Seat files: `.ufo/waves/round-74/w1/build/ScoutSibChousaKagiR74/chousa.json`, `.../kagi.json` (the same objects are pasted below).

## Common facts (commands run from /home/vgpnk/Projects/shokunin)
- Rule read: `corpus/knowledge/sibling-overlap-census-round49.md:43-58` (three classes; wave reports excluded) plus round-50 precedence (`:246-295`, `:301-357`): a claim makes `contested` unless the sibling's own surfaces assign the element elsewhere; a kotoba-only split may still make a no-claim row `adjacent`.
- Freeze rows: `cat .../receipts/sibling-heads-freeze.tsv` -> chousa master 00f8c7f5…a9 blobs ec1f0c1f…/0f94a0c4…; kagi master 69b61db4…97 blobs 716f0169…/2bbd4daa….
- `git -C chousa-shokunin rev-parse 00f8c7f5…:SKILL.md 00f8c7f5…:PROVINCE.md` -> `ec1f0c1f5865fcc823c688fe8be34c7d8cdf53ae`, `0f94a0c4f73cec2e36d587b199d7c43716ceae8c` (match). kagi -> `716f0169832cfc8f28ed28ab3b1dae350853e975`, `2bbd4daae8a117bc62a0761e828f5004c6617a5a` (match).
- `git -C <lane>-shokunin merge-base --is-ancestor <head40> refs/heads/master && echo anc` -> `chousa-anc`, `kagi-anc`.
- r49 pins read from kotoba base PROVINCE.md: `git -C kotoba-shokunin show 1e03d199…:PROVINCE.md | sed -n '53p;56p'` -> chousa `6c5eb1466f2b8abbd3de576389037f435016d07b`, kagi `899c50b42634a3a4ad0b28ab7509786315e2fc2b`; both `adjacent`.
- Kotoba's own side at base: `git -C kotoba-shokunin show 1e03d199…:SKILL.md | sed -n 10,13p` -> "own their own SKILL.md content — this skill audits and reports; fixes route / to the owning lane. chousa owns the research method; kama owns endpoint" (kagi named at :10, chousa at :12).

## chousa
- Delta: `git -C chousa-shokunin diff --shortstat 6c5eb146… 00f8c7f5… -- SKILL.md PROVINCE.md` -> ` 1 file changed, 187 insertions(+), 20 deletions(-)`; with `-- PROVINCE.md` alone -> empty; `rev-list --count` r49pin..head -> 213; `log --oneline … -- SKILL.md PROVINCE.md | wc -l` -> 40. Added table rows (`git diff … -- SKILL.md | grep -E '^\+\| '`) are all chousa's own tools/gates (quote-reopen, research-gate, round-29…51 counters, parent-lifetime, tag-count, etc.). Description line 3: `diff <(show 6c5eb146:SKILL.md | sed -n 3p) <(show 00f8c7f5:SKILL.md | sed -n 3p)` -> equal. SKILL.md is 736 lines at head (`wc -l`).
- kotoba mentions in SKILL.md/PROVINCE.md: `git show <head>:SKILL.md | grep -n -w -i kotoba` -> no output; PROVINCE.md -> no output; at the r49 pin both exit 1. Tree sweep `git grep -n -w -i kotoba <head> -- . ':!LOG.md' ':!.ufo'` -> `MINT.md:52: - Rejected recipients for this material: lore, kotoba, kasegi, kama, kumitate,` and `SCORECARD.md:479` (citation of `../SCORECARD.md:172-174`). MINT.md:45-53 is a rule for an exported research dump (rejects recipients of that material); not a trigger-area split with kotoba and not in the rule's scope surfaces (SKILL.md, PROVINCE.md, corpus files). Recorded, not counted. `corpus/README.md` has no hit.
- Claim arm: `git grep -n -i -E 'prompt/skill craft|skill craft|AGENTS\.md|audit(s|ing)? (other|another|sibling|every) lane' <head> -- . ':!LOG.md' ':!.ufo' ':!SCORECARD.md'` -> no output. chousa's scope (PROVINCE.md:3-8) is research method, source hierarchy, citation chains, claim-vs-source verification, own corpus/gates. Not contested.
- Adjacent clause: only kotoba-side. Deciding sentence: kotoba base SKILL.md:12 "chousa owns the research method;" and base PROVINCE.md:53 "deep-research method; kotoba cites it, never re-derives it". chousa's own side names kasegi/kengaku in the description (arbitration cell `kasegi, kengaku`, `sed -n 3p | grep -o -i -w -E <lane names>`), kumitate and kagi in PROVINCE.md:10-15 Refuses; it never names kotoba. Same as r49 (basis kotoba).
- Mechanical cells recomputed: skill file `SKILL.md`; names kotoba `no`; arbitration `yes: kasegi, kengaku` (description line 3 equals the r49 line).

```json
{
 "lane": "chousa",
 "head40": "00f8c7f5272a1d98b6d34913985fa4537e00aaf9",
 "r49_classification": "adjacent",
 "r49_pin": "6c5eb1466f2b8abbd3de576389037f435016d07b",
 "proposed_classification": "adjacent -- decided by the second clause of the r49 rule (a split stated on kotoba's side, base SKILL.md description, and kotoba's base PROVINCE.md:53 row); no sibling-side split and no claim over kotoba's core; deciding sentence (kotoba base SKILL.md:12): \"chousa owns the research method;\"",
 "changed": "No. Classification and basis (kotoba side only) are unchanged. What moved: chousa SKILL.md grew (git diff --shortstat r49pin..head -- SKILL.md PROVINCE.md: ' 1 file changed, 187 insertions(+), 20 deletions(-)'; PROVINCE.md byte-equal; the 187 added lines are rows for chousa's own tools/gates r29-r51, description line 3 byte-equal to the pin). Neither SKILL.md nor PROVINCE.md at the head contains the word kotoba, so no sibling-side split or claim appeared.",
 "skill_file": "SKILL.md",
 "quote": "deep-research method (調査) — the reusable craft of source research.",
 "quote_path_line": "PROVINCE.md:3",
 "kotoba_mentions": [],
 "boundary": "chousa owns the research method, its tools and gates (PROVINCE.md:3-8 at the head); kotoba cites it and never re-derives it (kotoba base PROVINCE.md:53, SKILL.md:12); chousa's scope surfaces name no kotoba.",
 "sweep": [
  "git -C chousa-shokunin merge-base --is-ancestor 00f8c7f5 refs/heads/master -> exit 0 (ancestor)",
  "git -C chousa-shokunin rev-parse 00f8c7f5:SKILL.md 00f8c7f5:PROVINCE.md -> ec1f0c1f5865fcc823c688fe8be34c7d8cdf53ae / 0f94a0c4f73cec2e36d587b199d7c43716ceae8c (equal to freeze row)",
  "git -C chousa-shokunin diff --shortstat 6c5eb146 00f8c7f5 -- SKILL.md PROVINCE.md -> ' 1 file changed, 187 insertions(+), 20 deletions(-)'; same for -- PROVINCE.md alone -> empty",
  "git -C chousa-shokunin show <head>:SKILL.md | grep -n -w -i kotoba -> no output; same on PROVINCE.md -> no output; same at r49 pin -> exit 1 both",
  "git -C chousa-shokunin grep -n -w -i kotoba 00f8c7f5 -- . ':!LOG.md' ':!.ufo' -> MINT.md:52 'Rejected recipients for this material: lore, kotoba, kasegi, kama, kumitate,' (mint record on an export dump, not a trigger-area split) and SCORECARD.md:479 (citation of kotoba's scorecard); corpus/README.md has no hit",
  "git -C chousa-shokunin grep -n -i -E 'prompt/skill craft|skill craft|AGENTS\\.md|audit(s|ing)? (other|another|sibling|every) lane' 00f8c7f5 -- . ':!LOG.md' ':!.ufo' ':!SCORECARD.md' -> no output (no claim over kotoba's core)",
  "git -C chousa-shokunin show <head>:SKILL.md | sed -n 3p | grep -o -i -w -E '<20 lane names>' -> kasegi, kengaku (arbitration cell: kasegi, kengaku); PROVINCE Refuses also names kumitate and kagi (PROVINCE.md:10-15)",
  "git -C kotoba-shokunin show 1e03d199:SKILL.md | sed -n 10,13p -> 'chousa owns the research method;' (SKILL.md:12); git -C kotoba-shokunin show 1e03d199:PROVINCE.md | sed -n 53p -> row 'chousa | adjacent | 6c5eb146...'"
 ]
}```

## kagi
- Delta: `git -C kagi-shokunin diff --shortstat 899c50b4… 69b61db4… -- SKILL.md PROVINCE.md` -> empty (0 bytes); `rev-list --count 899c50b4..69b61db4` -> 6; `git log --oneline 899c50b4..69b61db4 -- SKILL.md PROVINCE.md | wc -l` -> 0. Row `delta` = `none`.
- kotoba mentions: SKILL.md `grep -n -w -i kotoba` -> `297:  four committed defects: two `local://` scratch URIs, one kotoba path wearing` (a historical citation of a defect; the same single hit at the r49 pin); PROVINCE.md -> none. Tree: `corpus/README.md:96-97`, `corpus/adjacency.tsv:57,81,84`, `corpus/knowledge/adjacency-scope.md`, `claim-ledger.md`, `drift-gate.md`, lessons, `scope-gate.sh:98,756,852,866`, `surface-census.tsv:55`, SCORECARD.md.
- Split text: `corpus/README.md:97` -> "| `$HOME/.agents/AGENTS.md` | kotoba (…alwayson-checklist-round7.md:30) audits the same file … | kagi pins its bytes; kotoba owns the checklist/shape reading — no adjudication needed, both are read-only |"; `corpus/adjacency.tsv:84` `$HOME/.agents/AGENTS.md	kotoba	shared-read	declared`. That is a sibling-stated split of one artifact (an AGENTS.md-class file, kotoba core) assigning the reading to kotoba, so the claim arm (kagi pins bytes only) is cleared by kagi's own assignment; the class is `adjacent` by clause 2, not `contested`. Also `corpus/README.md:96` (`$HOME/.config/opencode`): kagi claims credential/request hygiene on four children only; ruling owed to the integrator (unresolved, unchanged since r49).
- Claim arm sweep: `git grep -n -i -E 'skill craft|prompt craft|audit(s|ing)? (other|another|sibling) lane|writes? (other|another) lane' <head> -- . ':!LOG.md' ':!.ufo' ':!SCORECARD.md'` -> exit 1. The `corpus/checklist-run.sh` (PROVINCE.md:50) reads kagi's own SKILL.md checklist: own text, not another lane's.
- Mechanical cells: description `Domain specialist — secrets & vault ops — the-janitor flows, credential hygiene evidence, vault lifecycle. Rank: shonen.` (SKILL.md:3) names kotoba `no` (no lane name at all: `grep -o -i -w -E <lane names>` exit 1), arbitration `no`, skill file `SKILL.md`. PROVINCE.md:3 `**Domain:** secrets & vault ops — the-janitor flows, credential hygiene evidence`. PROVINCE.md:67 (Adjacent) names chousa, kasegi, kumitate, kama, kaidoku, tsukuroi, kake but not kotoba.

```json
{
 "lane": "kagi",
 "head40": "69b61db46be4ed955994f6f1d1cba522bc5f4e97",
 "r49_classification": "adjacent",
 "r49_pin": "899c50b42634a3a4ad0b28ab7509786315e2fc2b",
 "proposed_classification": "adjacent -- decided by the second clause of the r49 rule on both sides: kagi's own corpus states the split (kagi corpus/README.md:97 \"kagi pins its bytes; kotoba owns the checklist/shape reading\") and kotoba's base description says \"kagi, kake, kasegi, kengaku and kumitate own their own SKILL.md content\" (SKILL.md:10-11); the contested arm is cleared by kagi's own assignment of the AGENTS.md reading to kotoba",
 "changed": "No. Classification unchanged, basis both unchanged. Delta: git diff --shortstat r49pin..head -- SKILL.md PROVINCE.md prints nothing (both files byte-equal; 6 commits in between touch neither, git log --oneline r49pin..head -- SKILL.md PROVINCE.md | wc -l -> 0). Row delta = none. The head's bytes say nothing the r49 pin did not.",
 "skill_file": "SKILL.md",
 "quote": "secrets & vault ops — the-janitor flows, credential hygiene evidence, vault lifecycle.",
 "quote_path_line": "SKILL.md:3",
 "kotoba_mentions": [
  {
   "path_line": "SKILL.md:297",
   "kind": "citation"
  }
 ],
 "boundary": "kagi owns secrets and vault ops, credential custody and hygiene evidence (SKILL.md:3, PROVINCE.md:3); kotoba owns the checklist and shape reading of the shared $HOME/.agents/AGENTS.md, which kagi only byte-pins (kagi corpus/README.md:97).",
 "sweep": [
  "git -C kagi-shokunin merge-base --is-ancestor 69b61db4 refs/heads/master -> exit 0 (ancestor)",
  "git -C kagi-shokunin rev-parse 69b61db4:SKILL.md 69b61db4:PROVINCE.md -> 716f0169832cfc8f28ed28ab3b1dae350853e975 / 2bbd4daae8a117bc62a0761e828f5004c6617a5a (equal to freeze row)",
  "git -C kagi-shokunin diff --shortstat 899c50b4 69b61db4 -- SKILL.md PROVINCE.md -> empty (0 bytes); git rev-list --count 899c50b4..69b61db4 -> 6; git log --oneline 899c50b4..69b61db4 -- SKILL.md PROVINCE.md | wc -l -> 0",
  "git -C kagi-shokunin show <head>:SKILL.md | grep -n -w -i kotoba -> 297:  four committed defects: two `local://` scratch URIs, one kotoba path wearing; PROVINCE.md -> no output (r49 pin identical: SKILL.md 297 only)",
  "git -C kagi-shokunin show <head>:SKILL.md | sed -n 3p | grep -o -i -w -E '<20 lane names>' -> no output, exit 1 (description names no lane)",
  "git -C kagi-shokunin grep -n -w -i kotoba 69b61db4 -- . ':!LOG.md' ':!.ufo' -> corpus/README.md:96-97, corpus/adjacency.tsv:57,81,84, corpus/knowledge/adjacency-scope.md:27,50,66,76,124,197, claim-ledger.md:112,283, drift-gate.md:96, lessons round-1/11/13/14/15/16/5, scope-gate.sh:98,756,852,866, surface-census.tsv:55, SKILL.md:297, SCORECARD.md (many)",
  "sed -n 97p of corpus/README.md at head -> '| `$HOME/.agents/AGENTS.md` | kotoba (...alwayson-checklist-round7.md:30) audits the same file ... | kagi pins its bytes; kotoba owns the checklist/shape reading — no adjudication needed, both are read-only |'; adjacency.tsv:84 owner kotoba shared-read",
  "git -C kagi-shokunin grep -n -i -E 'skill craft|prompt craft|audit(s|ing)? (other|another|sibling) lane|writes? (other|another) lane' 69b61db4 -- . ':!LOG.md' ':!.ufo' ':!SCORECARD.md' -> exit 1 (no kagi claim over writing other lanes' SKILL.md or prompts)"
 ]
}```

## Notes for the L1
- Quote lines verified: `git -C chousa-shokunin show 00f8c7f5…:PROVINCE.md | sed -n 3p` -> `**Domain:** deep-research method (調査) — the reusable craft of source research.`; `git -C kagi-shokunin show 69b61db4…:SKILL.md | sed -n 3p` -> `description: Domain specialist — secrets & vault ops — the-janitor flows, credential hygiene evidence, vault lifecycle. Rank: shonen.` (quote is a substring of each line; dropped: the `**Domain:**` markup / the `description: Domain specialist — ` prefix and ` Rank: shonen.`; quote-equal after dropping those bytes, not byte-exact line equality). Word counts: chousa 10, kagi 12, boundaries 30 each.
- r49's kagi quote used `PROVINCE.md:3`; mine uses `SKILL.md:3` (frontmatter) — both exist at the head.
- chousa `names kotoba = no` and kagi `names kotoba = no` hold; whole-word `kotoba` appears in no description and in neither PROVINCE.md, so counter clause (e) does not force a non-`none` row; both rows are `adjacent` on other grounds above.
