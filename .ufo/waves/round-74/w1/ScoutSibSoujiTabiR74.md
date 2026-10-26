# ScoutSibSoujiTabiR74 — C2 sibling re-read: souji, tabi

**Verdict: the proposal equals r49 for both lanes (souji `none`, tabi `none`); no classification changes. One plan defect found: C2 clause (e) as written rejects the tabi `none` row, which the base checker accepts (below). Both heads read from committed bytes only (`git -C <lane>-shokunin show <head40>:<file>`); the freeze blobs were re-derived and equal.**

Method: plan `plans/round-74.md` § C2 and `corpus/knowledge/sibling-overlap-census-round49.md` § Classification rule (lines 43-58) plus the round-50 precedence section (lines 246-295) read first. Heads from `.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv`: souji `b8cb4b31…`, tabi `856fa9e1…`. No sibling or lane file was written; scratch `/tmp/k74w1-ScoutSibSoujiTabiR74.gRUI` was created and deleted. Nothing was installed.

## Finding 1 — plan clause (e) vs the base checker (tabi)  [disagreement, recorded for the L1]
- `git -C tabi-shokunin show 856fa9e1…:SKILL.md | grep -n -w -i kotoba` → `1313:  \`LANES="protocol aggregator kasegi kengaku kake kumitate kotoba kagi kama"\`` and `1450:` (the same string). 2 hits in SKILL.md, 0 in PROVINCE.md, 0 in the description.
- Plan C2 (e): "no `none` row exists for a lane whose pinned `SKILL.md` or `PROVINCE.md` contains the whole word `kotoba`". Applied literally the tabi row cannot be `none`.
- The base checker's none rule (`verifiers/check_sibling_census.py:595-601`) reads only the description and `PROVINCE.md` (`token_in(SELF_LANE, description) or … province_text`). Run on my row: `mechanical_findings(tabi, head, {path:SKILL.md, names kotoba:no, arbitration:no}, 'tabi', 20 lanes, 'none')` → `[]`; control arbitration `yes: kagi` → `["arbitration cell 'yes: kagi' but the pinned description gives 'no'"]`.
- The 2 hits are a citation of a fleet watchdog roster string (tabi records that tabi is absent from it), not a split. The pin e3cf4e0d already had the same 2 (`git -C tabi-shokunin grep -c -w -i kotoba e3cf4e0d… -- SKILL.md PROVINCE.md` → `…:SKILL.md:2`), so r49's `none` was under the same bytes. An `adjacent` call has no sentence to rest on (rule: a split stated by a scope surface). Options for the L1, before data (Q28): narrow (e) to the description and `PROVINCE.md` (the base checker's reading), or keep (e) and accept that tabi cannot score; I propose the first. The kind labels for tabi's 2 hits are `citation`, not `split` or `claim`.

## Finding 2 — souji: `none`, unchanged
- Deciding clause: `none` (third bullet). No scope surface states a split with kotoba: 0 whole-word kotoba in SKILL.md, PROVINCE.md, corpus/README.md. souji's own split is with kagi (`SKILL.md:2` description: "NEVER credentials/secrets handling (kagi-shokunin owns credential hygiene)").
- Changed since pin 4edb25df: `git diff --shortstat 4edb25df b8cb4b31 -- SKILL.md PROVINCE.md` → `1 file changed, 2 insertions(+), 2 deletions(-)` (SKILL.md only; line 37 `launch-*.json`→`launch-<id>.json`, line 224 blank→a `souji-pre-report-gate` row); PROVINCE.md blob is the same. The description is byte-equal to the pin's.
- The branch moved after the freeze: `git -C souji-shokunin rev-parse refs/heads/master` → `b8620071…`, 2 commits past `b8cb4b31`. The row is valid at the frozen head, not the tip.
- The 202 whole-word hits in the tree are census/ (135), tests/ (65), results/ (2), lane directory names in data; 0 under corpus/, tools/, plans/.

## Finding 3 — tabi: `none`, unchanged
- Deciding clause: `none` with the rule's wave-report exclusion. Tabi's round-16 draft still states the split at the head (`.ufo/waves/round-16/drafts/DraftAdjacency.md:39`, "kotoba owns the craft of such text"; grep line 13, 25, 26 too), and `.ufo` is excluded by bullet 4 exactly as in r49 `RowTabi`. No head-committed scope surface (SKILL.md, PROVINCE.md, corpus/) carries it: the 8 non-SKILL hits outside `.ufo` are all the `LANES` string. The r49 note "a later round should ask tabi whether to land it" is still open at the head (re-checked, not resolved).
- Changed since pin e3cf4e0d: `1 file changed, 89 insertions(+)` (SKILL.md: append-only errata + round-24 gate-registry table from line 2442); PROVINCE.md same blob. 52 commits. The additions hold no kotoba and no split.

## JSON objects (also saved at `.ufo/waves/round-74/w1/build/ScoutSibSoujiTabiR74/{souji,tabi}.json`)

### souji.json
```json
{
 "lane": "souji",
 "head40": "b8cb4b31ce80e2e3314b88e85d40ea9873180804",
 "r49_classification": "none",
 "r49_pin": "4edb25dfe262515d0da63224bbba71e02e36cba5",
 "proposed_classification": "none",
 "clause": "`none` (r49 § Classification rule, third bullet): no sibling-side or kotoba-side committed scope surface states a split of a kotoba artifact/function/trigger area. Deciding sibling sentence (souji SKILL.md:2, description): \"NEVER credentials/secrets handling (kagi-shokunin owns credential hygiene)\" - a split with kagi, not kotoba. Kotoba side: base SKILL.md has 0 whole-word souji/tabi hits; base PROVINCE.md names souji only in its own Adjacent row (line 68) which states 'no split'.",
 "changed": "Classification unchanged (none). Bytes changed since the r49 pin 4edb25df: SKILL.md 2 insertions/2 deletions (line 37 `launch-*.json` -> `launch-<id>.json` in the `stale` row; line 224 blank -> a `souji-pre-report-gate` gate row); PROVINCE.md byte-identical (blob 57b657f2 both sides, empty diff); the description (line 2) is byte-equal to the pin. Nothing in the diff mentions kotoba, prompt or skill authoring.",
 "skill_file": "SKILL.md",
 "quote": "fleet repository & workspace hygiene (掃除) — receipt-gated removal of stale, duplicate, and already-preserved artifacts.",
 "quote_path_line": "PROVINCE.md:3",
 "kotoba_mentions": [],
 "kotoba_mentions_note": "0 whole-word kotoba hits in SKILL.md, PROVINCE.md and corpus/README.md at the head. The only whole-word hits in the tree (git grep, .ufo and LOG.md excluded) are 202 lines in 3 data directories: census/ 135, tests/ 65, results/ 2 - kotoba as a lane directory name or file name in census rows and vault fixtures, never in a scope statement; 0 hits under corpus/, tools/, plans/, README.md, SHONEN.md, SCORECARD.md, MINT.md.",
 "boundary": "souji owns receipt-gated removal of stale or duplicate artifacts (PROVINCE.md:3-4) and routes credential findings to kagi (SKILL.md:2); it states no claim over SKILL.md or prompt text, so no split with kotoba.",
 "sweep": [
  {
   "cmd": "git -C souji-shokunin cat-file -t b8cb4b31ce80e2e3314b88e85d40ea9873180804; git -C souji-shokunin rev-parse b8cb4b31ce80e2e3314b88e85d40ea9873180804:SKILL.md b8cb4b31ce80e2e3314b88e85d40ea9873180804:PROVINCE.md",
   "out": "commit; 516738853d917b3c55c08c93d0463bea12b212f5; 57b657f28976fb496de939874563f3c89d48d779 (equal to the freeze row)"
  },
  {
   "cmd": "for f in SKILL.md PROVINCE.md corpus/README.md; do git -C souji-shokunin show b8cb4b31ce80e2e3314b88e85d40ea9873180804:$f | grep -c -w -i kotoba; done",
   "out": "0 0 0"
  },
  {
   "cmd": "git -C souji-shokunin grep -l -w -i kotoba b8cb4b31ce80e2e3314b88e85d40ea9873180804 -- . ':!LOG.md' ':!.ufo' | sed 's/^b8cb4b31ce80e2e3314b88e85d40ea9873180804://' | awk -F/ '{print $1}' | sort | uniq -c",
   "out": "135 census / 65 tests / 2 results (lines: grep -n gives 202)"
  },
  {
   "cmd": "git -C souji-shokunin grep -c -w -i kotoba b8cb4b31ce80e2e3314b88e85d40ea9873180804 -- corpus SKILL.md PROVINCE.md README.md SHONEN.md SCORECARD.md tools plans MINT.md; echo rc=$?",
   "out": "rc=1 (no hit)"
  },
  {
   "cmd": "git -C souji-shokunin show b8cb4b31ce80e2e3314b88e85d40ea9873180804:SKILL.md | sed -n 2p | grep -o -i -w -E '<19 other lane names>' | sort -u",
   "out": "kagi"
  },
  {
   "cmd": "git -C souji-shokunin show b8cb4b31ce80e2e3314b88e85d40ea9873180804:SKILL.md | grep -n -i -E 'SKILL\\.md|AGENTS\\.md|prompt|frontmatter|description'; same on PROVINCE.md and corpus/README.md",
   "out": "SKILL.md: line 2 only (the description itself); PROVINCE.md: no hit; corpus/README.md: 38 (`core (SKILL.md, tools/)` - souji's own file) and 153 (its own historical descriptions). No claim over another lane's SKILL.md, prompt or AGENTS.md."
  },
  {
   "cmd": "git -C souji-shokunin diff --shortstat 4edb25dfe262515d0da63224bbba71e02e36cba5 b8cb4b31ce80e2e3314b88e85d40ea9873180804 -- SKILL.md PROVINCE.md; git -C souji-shokunin rev-list --count 4edb25df..b8cb4b31ce80e2e3314b88e85d40ea9873180804; merge-base --is-ancestor",
   "out": "1 file changed, 2 insertions(+), 2 deletions(-); 85 commits; pin is an ancestor (rc=0)"
  },
  {
   "cmd": "git -C kotoba-shokunin show 1e03d19:SKILL.md | grep -c -w -i -E 'souji|tabi'",
   "out": "0 (kotoba's side names neither); PROVINCE.md hits only the two Adjacent rows at lines 68-69"
  },
  {
   "cmd": "python3 -B (import verifiers/check_sibling_census.py).mechanical_findings(souji repo, head, {path:SKILL.md, names kotoba:no, arbitration:'yes: kagi'}, 'souji', 20 lanes, 'none')",
   "out": "[] ; control with arbitration 'no' -> [\"arbitration cell 'no' but the pinned description gives 'yes: kagi'\"]"
  },
  {
   "cmd": "git -C souji-shokunin rev-parse refs/heads/master (info)",
   "out": "b86200714069022954a3b498cf697d894119b45e - the branch moved 2 commits past the freeze head b8cb4b31 during wave 1; the row is valid at the frozen head, not the tip"
  }
 ]
}
```

### tabi.json
```json
{
 "lane": "tabi",
 "head40": "856fa9e1202179f5cfbd28c1f0efdd4eb1f426bb",
 "r49_classification": "none",
 "r49_pin": "e3cf4e0d30bb835532ff44b118c5ad52e09eb76d",
 "proposed_classification": "none",
 "clause": "`none` (r49 § Classification rule, third bullet, with its wave-report exclusion): tabi's scope surfaces (SKILL.md, PROVINCE.md, corpus/) state no split with kotoba; the only committed split is in .ufo/waves/round-16/drafts/DraftAdjacency.md:39, a wave draft the rule excludes. Deciding sibling sentence (tabi PROVINCE.md:15-17): \"Refuses: reverse engineering as forensics (→ revenger/kaidoku), web *publishing* (→ kake), secrets (→ kagi\" - splits with other lanes, none with kotoba.",
 "changed": "Classification unchanged (none). Bytes changed since the r49 pin e3cf4e0d: SKILL.md +89 lines, 0 deletions (an append-only block from line 2442: 'Errata - round22 axis and encoding', 'Round 24 - gate registry conformance' and a gate table); PROVINCE.md byte-identical (blob c2222b16 both sides, empty diff). The description (SKILL.md:3) is unchanged. The +89 lines contain no whole-word kotoba. PLAN CONFLICT: tabi SKILL.md carries whole-word kotoba at 1313 and 1450 (a quoted fleet watchdog LANES string), the same 2 hits the r49 pin e3cf4e0d already had; plan C2 clause (e) (SKILL.md or PROVINCE.md contains kotoba -> no `none`) would reject this row, while the base checker's none rule reads only the description and PROVINCE.md and passes it.",
 "skill_file": "SKILL.md",
 "quote": "browser & web-interaction craft (旅, journey) — driving real browsers against real sites with evidence discipline.",
 "quote_path_line": "PROVINCE.md:3",
 "kotoba_mentions": [
  {
   "path_line": "SKILL.md:1313",
   "kind": "citation",
   "text": "LANES=\"protocol aggregator kasegi kengaku kake kumitate kotoba kagi kama\" (fleet watchdog roster string; tabi's point is that tabi is absent from it)"
  },
  {
   "path_line": "SKILL.md:1450",
   "kind": "citation",
   "text": "same LANES string, repeated in an append-only note"
  }
 ],
 "kotoba_mentions_note": "PROVINCE.md 0, corpus/README.md 0, description 0. Besides SKILL.md the git grep (.ufo and LOG.md excluded) finds 8 more files, all LANES-roster citations (corpus/evidence/w11-b11-1/w11-b11-1-fleet.txt:22, w11-ver-b11-poll/pins_recon.txt:20, corpus/knowledge/closeout-r11.md:141, plans/round-{6,7,8,9,10}-record-draft.md). Under .ufo (excluded by the rule): round-16/drafts/DraftAdjacency.md:13,25,26,39 states 'kotoba owns the craft of such text' (draft, still at head).",
 "boundary": "tabi owns browser-session and web-interaction evidence (PROVINCE.md:6-13) and refuses forensics, publishing and secrets to revenger, kaidoku, kake and kagi (PROVINCE.md:15-17); it states no split with kotoba on its scope surfaces.",
 "sweep": [
  {
   "cmd": "git -C tabi-shokunin rev-parse 856fa9e1202179f5cfbd28c1f0efdd4eb1f426bb:SKILL.md 856fa9e1202179f5cfbd28c1f0efdd4eb1f426bb:PROVINCE.md",
   "out": "e335eb36ac53b20a224198635f478869fd06fe02; c2222b16b3b18ce2c2058fb3a50d690c6e5735ae (equal to the freeze row)"
  },
  {
   "cmd": "for f in SKILL.md PROVINCE.md corpus/README.md; do git -C tabi-shokunin show 856fa9e1202179f5cfbd28c1f0efdd4eb1f426bb:$f | grep -c -w -i kotoba; done",
   "out": "2 0 0"
  },
  {
   "cmd": "git -C tabi-shokunin show 856fa9e1202179f5cfbd28c1f0efdd4eb1f426bb:SKILL.md | grep -n -w -i kotoba",
   "out": "1313:  `LANES=\"protocol aggregator kasegi kengaku kake kumitate kotoba kagi kama\"` ; 1450:  `LANES=\"... same ...\"`."
  },
  {
   "cmd": "git -C tabi-shokunin grep -n -w -i kotoba 856fa9e1202179f5cfbd28c1f0efdd4eb1f426bb -- . ':!LOG.md' ':!.ufo'",
   "out": "9 files: SKILL.md:1313,1450; corpus/evidence/w11-b11-1/w11-b11-1-fleet.txt:22; corpus/evidence/w11-ver-b11-poll/pins_recon.txt:20; corpus/knowledge/closeout-r11.md:141; plans/round-{6,7,8,9,10}-record-draft.md - every line is the watchdog `LANES` string; none states a split"
  },
  {
   "cmd": "git -C tabi-shokunin grep -n -w -i kotoba 856fa9e1202179f5cfbd28c1f0efdd4eb1f426bb -- .ufo | cut -c1-260",
   "out": "DraftAdjacency.md:13,25,26,39 and w1/ConnSiblings.md:9,55,77,78,85 under .ufo/waves/round-16 - wave drafts and reports, excluded by the rule's fourth bullet (same as r49 RowTabi)"
  },
  {
   "cmd": "git -C tabi-shokunin show 856fa9e1202179f5cfbd28c1f0efdd4eb1f426bb:PROVINCE.md | grep -n -i -E 'SKILL\\.md|AGENTS\\.md|prompt|frontmatter|tool description|agent-facing|schema'; same on corpus/README.md",
   "out": "PROVINCE.md: no hit; corpus/README.md: lines 19,20,71,90,155,393,407,426,458,562,564,583,591 - about tabi's own SKILL.md/webmcp inputSchema evidence, none a claim over another lane's SKILL.md or prompts"
  },
  {
   "cmd": "git -C tabi-shokunin show 856fa9e1202179f5cfbd28c1f0efdd4eb1f426bb:SKILL.md | sed -n 1,5p | grep -c -i -w kotoba; description lane names",
   "out": "0; description (line 3) names no lane"
  },
  {
   "cmd": "git -C tabi-shokunin diff --shortstat e3cf4e0d30bb835532ff44b118c5ad52e09eb76d 856fa9e1202179f5cfbd28c1f0efdd4eb1f426bb -- SKILL.md PROVINCE.md; rev-list --count",
   "out": "1 file changed, 89 insertions(+); 52 commits; pin is an ancestor (rc=0)"
  },
  {
   "cmd": "git -C tabi-shokunin grep -c -w -i kotoba e3cf4e0d -- SKILL.md PROVINCE.md",
   "out": "e3cf4e0d...:SKILL.md:2 - the pin already had both hits, so clause (e) conflicts with r49's none already"
  },
  {
   "cmd": "python3 -B mechanical_findings(tabi repo, head, {path:SKILL.md, names kotoba:no, arbitration:'no'}, 'tabi', 20 lanes, 'none')",
   "out": "[] ; control arbitration 'yes: kagi' -> [\"arbitration cell 'yes: kagi' but the pinned description gives 'no'\"]"
  },
  {
   "cmd": "git -C tabi-shokunin rev-parse refs/heads/master (info)",
   "out": "856fa9e1... = freeze head (not moved)"
  }
 ]
}
```

## Unobserved
- The non-author semantic check of the two classifications is wave 2's. I did not run the full 20-row census checker (this seat owns 2 rows). I did not read souji's or tabi's working trees. Quotes are copied from `sed -n 3,4p` of the blob (whitespace-collapsed join of two lines; no words dropped).
