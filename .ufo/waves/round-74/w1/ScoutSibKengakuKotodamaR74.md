# ScoutSibKengakuKotodamaR74 — C2 sibling re-read: kengaku, kotodama

**Verdict:** both proposals equal r49 (`adjacent`, `adjacent`); no classification differs from the round-49 census rows. Pins move: kengaku `1f3b0f1e` -> `f9efce3beb0705ec2e04ba3f8f449d10d64cc1dd` (delta `2 files changed, 30 insertions(+)`), kotodama `35f0d49f` -> `f7104cbce186bc2e1522abf0cfd619cc834628bb` (delta `1 file changed, 85 insertions(+)`). Bytes read only via `git -C <lane>-shokunin show|grep <head40>`; blobs equal the freeze TSV (`git rev-parse <head>:SKILL.md <head>:PROVINCE.md`: kengaku fb88848f.../93be7bd9..., kotodama b6dc54ca.../313b182f...). Both heads are ancestors of the lane branch (`merge-base --is-ancestor` exit 0). Unobserved: wave reports under `.ufo/` (excluded by the r49 rule); I did not run `check_sibling_census.py` on these rows (not asked; JSON quotes verified with `sed -n 3p | grep -c -F` -> 1 each).

Deciding rule: r49 § Classification rule, `adjacent` clause (a split of a trigger area stated on scope surfaces). `contested` negative sweeps below: no scope surface of either lane claims writing or auditing other lanes' SKILL.md, prompts or AGENTS.md.

Findings that were not in the r49 row text: (1) kengaku PROVINCE gained two frontier-admission paragraphs and SKILL.md one gate row since the pin; none mentions kotoba. (2) kotodama's pin delta is SKILL.md only (7 commits, round 69-73 registry rows); PROVINCE.md byte-unchanged. (3) kotoba's own description at base `1e03d19` still names both lanes (`git -C kotoba-shokunin show 1e03d19:SKILL.md | sed -n 1,25p | grep -n -o -i -E 'kotodama[^;.]{0,90}|kengaku[^;.]{0,90}'` -> lines 10, 13, 14, 15).

Commands and observed output are in the `sweep` arrays below (copied from the saved JSON files). Saved: `.ufo/waves/round-74/w1/build/ScoutSibKengakuKotodamaR74/{kengaku,kotodama}.json`.

## kengaku.json
```json
{
 "lane": "kengaku",
 "head40": "f9efce3beb0705ec2e04ba3f8f449d10d64cc1dd",
 "r49_classification": "adjacent",
 "r49_pin": "1f3b0f1ec41ec297130e8944ff97968d32324632",
 "proposed_classification": "adjacent",
 "decided_by": "adjacent clause 2 (a split of one trigger area stated on the sibling's own scope surfaces); contested clause does not fire. Deciding sentence, kengaku SKILL.md:3: \"Sibling arbitration: kotoba owns prompt and skill craft (kengaku keeps only measured capability effects)\"; corroborated by PROVINCE.md:30-32 and :138. Basis: both (kotoba's own description at base 1e03d19 SKILL.md:13 also states 'kengaku owns measured capability effects of prompt format').",
 "changed": "No. Classification, skill file, names-kotoba (yes) and the five kotoba hit lines (SKILL.md:3; PROVINCE.md:30,35,62,83,138) are identical at the r49 pin 1f3b0f1e and the head f9efce3b. What changed in bytes: 79 commits since the pin, 3 touch SKILL.md/PROVINCE.md; delta '2 files changed, 30 insertions(+)': PROVINCE.md +rounds 29-attempt-2 and 35 frontier-admission paragraphs (task-validity checklist, TB2 grader probe, sources_adopt.py) and SKILL.md +1 gate-registry row (`sources-adopt`). None names kotoba or craft over another lane's text; the r49 scope quote at SKILL.md:3 is unmoved.",
 "skill_file": "SKILL.md",
 "quote": "Domain specialist — LLM/model research & evaluation — eval design, benchmark selection, offline replay grading, blind shim-cascade leg attribution and interval-calibrated verdicts",
 "quote_path_line": "SKILL.md:3",
 "kotoba_mentions": [
  {
   "loc": "SKILL.md:3",
   "kind": "split",
   "note": "description: 'Sibling arbitration: kotoba owns prompt and skill craft (kengaku keeps only measured capability effects)'"
  },
  {
   "loc": "PROVINCE.md:30",
   "kind": "split",
   "note": "'kotoba: prompt- and skill-craft rules, render/trigger behaviour' (refusals list, :30-32)"
  },
  {
   "loc": "PROVINCE.md:35",
   "kind": "citation",
   "note": "report-out to kotoba (output-contract system prompt evidence), evidence sent not absorbed"
  },
  {
   "loc": "PROVINCE.md:62",
   "kind": "citation",
   "note": "round-11 report-out (ack compliance), prompt-craft evidence for benchmark authors"
  },
  {
   "loc": "PROVINCE.md:83",
   "kind": "citation",
   "note": "round-12/14 report-out (ack-intent derivation)"
  },
  {
   "loc": "PROVINCE.md:138",
   "kind": "split",
   "note": "## Adjacent table row: measured capability effects of prompt format stay here; reusable craft implications route out"
  }
 ],
 "boundary": "kengaku owns measured capability effects of prompt format and hands reusable craft out; kotoba owns the prompt/skill craft rules (kengaku SKILL.md:3, PROVINCE.md:30-32,138); kengaku's census script reads only its own lane root (plans/round25_census.sh:37-38).",
 "sweep": [
  "git -C kengaku-shokunin cat-file -t f9efce3b... -> commit; rev-parse f9efce3b:SKILL.md fb88848f2549f75641639e0c4e39cbf9ae1153cd, :PROVINCE.md 93be7bd9594793006980fa9cb0b085d18a6cc841 (both equal the freeze TSV blobs)",
  "git -C kengaku-shokunin merge-base --is-ancestor f9efce3b master -> exit 0 ('kengaku head ancestor of master')",
  "for f in SKILL.md PROVINCE.md: git show f9efce3b:$f | grep -n -w -i kotoba -> SKILL.md:3 ; PROVINCE.md:30 35 62 83 138 (same lines at 1f3b0f1e)",
  "git -C kengaku-shokunin grep -c -w -i kotoba f9efce3b -- . ':!LOG.md' ':!.ufo' -> 27 files, 99 hit lines (corpus/evidence/ and SCORECARD.md mostly; scope surfaces: SKILL.md 1, PROVINCE.md 5; corpus/README.md not listed = 0)",
  "git -C kengaku-shokunin diff --shortstat 1f3b0f1e f9efce3b -- SKILL.md PROVINCE.md -> 2 files changed, 30 insertions(+)",
  "git -C kengaku-shokunin log --oneline 1f3b0f1e..f9efce3b -- SKILL.md PROVINCE.md -> 4fe72a9 round-35, bcd2a6c round-32, 8cf7b60 round-29",
  "contested negative sweep: git -C kengaku-shokunin grep -n -i -E 'skill[- ]craft|prompt[- ]craft|SKILL\\.md quality|trigger fidelity|AGENTS\\.md' f9efce3b -- SKILL.md PROVINCE.md corpus/README.md -> only SKILL.md:3 (kotoba split) and PROVINCE.md:30,65,138 (split/report-out); no AGENTS.md hit, no claim to write or audit another lane's SKILL.md",
  "git show f9efce3b:plans/round25_census.sh | grep -n -E 'SKILL|lane root' -> :37-38 'if [ ! -f SKILL.md ] || [ ! -d corpus ]' exits 2 unless cwd is a lane root; :115-172 awk runs on ./SKILL.md only; corpus/README.md:206 describes it as 'frontmatter triggers' of this lane",
  "git grep -n -E '\\.\\./[a-z0-9-]*-shokunin|\\*-shokunin|kotoba-shokunin' f9efce3b -- plans ':!.ufo' -> one hit, plans/attrib-r21-frozen.md:20 (mori boundary note); no cross-lane SKILL.md reader",
  "quote check: git show f9efce3b:SKILL.md | sed -n 3p | grep -c -F '<quote>' -> 1"
 ]
}
```

## kotodama.json
```json
{
 "lane": "kotodama",
 "head40": "f7104cbce186bc2e1522abf0cfd619cc834628bb",
 "r49_classification": "adjacent",
 "r49_pin": "35f0d49f96f1d51f8b006136a8e1d0e8d0919a7a",
 "proposed_classification": "adjacent",
 "decided_by": "adjacent clause 2 (published split of a trigger area on the sibling's own scope surfaces); contested does not fire. Deciding sentence, kotodama SKILL.md:3: \"NOT prompt/skill craft (kotoba-shokunin)\", repeated at PROVINCE.md:19-20 ('prompt/skill craft (kotoba)') and MINT.md:20 ('kotoba owns prompt/skill craft despite its name'). Basis: sibling (and kotoba's own description at base 1e03d19 SKILL.md:14-15 names kotodama as owning naming and language for fictional worlds).",
 "changed": "No. Classification, skill file, names-kotoba (yes) and the kotoba hit lines (SKILL.md:3; PROVINCE.md:20) are identical at the r49 pin 35f0d49f and the head f7104cbc. What changed in bytes: 241 commits since the pin, 7 touch SKILL.md/PROVINCE.md; delta '1 file changed, 85 insertions(+)': SKILL.md only (registry-correction-chain decision table and error signatures, gate-registry rows, r73 rows); PROVINCE.md byte-unchanged; no new kotoba mention, no claim on prompt/skill text. The r49 quote lines (SKILL.md:8 area) did not move.",
 "skill_file": "SKILL.md",
 "quote": "Linguistic-cultural worldbuilding (言霊) — conlang craft, myth & symbol systems, era staging, costume/material-culture lexicon, and the coupling between them, feeding the world bible.",
 "quote_path_line": "SKILL.md:3",
 "kotoba_mentions": [
  {
   "loc": "SKILL.md:3",
   "kind": "split",
   "note": "description anti-trigger: 'NOT prompt/skill craft (kotoba-shokunin)'"
  },
  {
   "loc": "PROVINCE.md:20",
   "kind": "split",
   "note": "Refuses list: '(kake); prompt/skill craft (kotoba).'"
  }
 ],
 "boundary": "kotodama owns generative linguistic-cultural worldbuilding for fictional worlds and refuses prompt/skill craft by name (SKILL.md:3, PROVINCE.md:19-20); kotoba owns that craft; the lane-name collision is recorded in kotodama MINT.md:20.",
 "sweep": [
  "git -C kotodama-shokunin cat-file -t f7104cbc... -> commit; rev-parse f7104cbc:SKILL.md b6dc54ca41cbe0745e42030c74d515086ba63c10, :PROVINCE.md 313b182f251564b7997b06996b4f063370778f11 (both equal the freeze TSV blobs)",
  "git -C kotodama-shokunin merge-base --is-ancestor f7104cbc main -> exit 0 ('kotodama head ancestor of main')",
  "for f in SKILL.md PROVINCE.md: git show f7104cbc:$f | grep -n -w -i kotoba -> SKILL.md:3 ; PROVINCE.md:20 (same lines at 35f0d49f)",
  "git -C kotodama-shokunin grep -c -w -i kotoba f7104cbc -- . ':!LOG.md' ':!.ufo' -> 57 files, 105 hit lines: scope surfaces MINT.md 2, PROVINCE.md 1, README.md 1, SKILL.md 1; the rest are reports/ (historical) and 3 Japanese-word homonyms in corpus/knowledge/linguistics/ (orality-formulaic-language.md:59,77 'makura-kotoba', sociolinguistics-registers.md:104 'Onna-kotoba') and corpus/lessons/round-69.md:29 (a citation of 'kotoba r67'); corpus/README.md has 0 (git show ...:corpus/README.md | grep -c -w -i kotoba)",
  "git -C kotodama-shokunin diff --shortstat 35f0d49f f7104cbc -- SKILL.md PROVINCE.md -> 1 file changed, 85 insertions(+)",
  "git -C kotodama-shokunin log --oneline 35f0d49f..f7104cbc -- SKILL.md PROVINCE.md -> 7 commits (2d1cd91, 7aa8f99, 3537899, e62d731, acc2d61, 975e8f2, e86ed3e), all round-69..73 SKILL.md rows",
  "contested negative sweep: git -C kotodama-shokunin grep -n -i -E 'skill[- ]craft|prompt[- ]craft|SKILL\\.md quality|trigger fidelity|AGENTS\\.md' f7104cbc -- SKILL.md PROVINCE.md README.md MINT.md corpus/README.md -> only MINT.md:20,30, PROVINCE.md:20, README.md:6, SKILL.md:3, all refusals/echoes of the split; SKILL.md has no AGENTS.md or trigger-fidelity text; SKILL.md:556 'a sibling repo' only, no cross-lane SKILL.md claim",
  "diff +lines grep for 'kotoba|prompt|skill craft|SKILL.md|trigger|frontmatter|AGENTS' over git diff 35f0d49f f7104cbc -- SKILL.md -> only the '+++ b/SKILL.md' header line matched (no added line touches those words)",
  "quote check: git show f7104cbc:SKILL.md | sed -n 3p | grep -c -F '<quote>' -> 1"
 ]
}
```
