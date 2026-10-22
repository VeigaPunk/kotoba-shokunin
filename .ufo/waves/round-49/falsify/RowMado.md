# Round 49 FALSIFY — C1 census row `mado` (seat KotobaR49.RowMado, leaf)

Pin: mado-shokunin `e33ea30461f6e9bbeee40beef19770a953f7a105`. Judged kotoba bytes: `c48793dbe5eb30cd661f42ecad7399ae94e3d7ad`. Scratch: `/fast/scratch/hyaku/kotoba-r49/falsify/RowMado/` (private kotoba clone at c48793db, pinned mado files, mutants).

**VERDICT: HOLDS-BOUNDED** for census row `mado` (corpus/knowledge/sibling-overlap-census-round49.md:76): commit, branch cell, scope quote, both mechanical columns, and `none` under the letter of § Classification rule. **FAILS** for the PROVINCE.md:50 boundary sentence "no claim on kotoba ground", which mado's own committed omarchy-skill text contradicts.

## Per-item verdicts

1. **Commit and branch cell — HOLDS.** `e33ea304…` exists (`cat-file -t` = commit). `master` contains it (`merge-base --is-ancestor`, exit 0). HEAD is detached (`git branch --show-current` printed nothing). `master` is 3 commits ahead (tip `4de44647`); those commits add 26 files, all under `.ufo/waves/round-23/`, so no scope surface changed after the pin.
2. **Scope quote at SKILL.md:8 — HOLDS.** Line 8 equals the census quote byte for byte (`desktop & compositor craft playbook — the Hyprland/waybar/walker/terminal config plane`; em dash U+2014). It also sits inside the ±2 window. Line 9 continues "and display behavior on this host."
3. **Classification `none` — HOLDS-BOUNDED.** Contested test: no committed mado surface claims writing or auditing another lane's SKILL.md, prompts, or AGENTS.md-class files (F6). Adjacent test: no enumerated surface (SKILL.md, PROVINCE.md, corpus/) contains the token `kotoba` (0 in all three). The only committed mado statement that splits the omarchy skill with kotoba sits in `.ufo/` (F1, F2).
4. **Mechanical columns — HOLDS (`no` / `no`), but no instrument checks them** (F3). Re-derived in Python from `git show e33ea30…:SKILL.md`: the frontmatter has one `description:` line (SKILL.md:3). `kotoba` token: False. Sibling-lane tokens in the description: none.
5. **PROVINCE.md:50 boundary note — FAILS in part.** "desktop and compositor config" is accurate as a paraphrase but narrows the sibling's own word "craft" (F5). "no claim on kotoba ground" is contradicted (F1).

## Findings (by severity)

**F1 (medium): "no claim on kotoba ground" is false as written; the omarchy skill is a shared artifact.**
- mado `PROVINCE.md:10-11` (pin, under "Owns (surfaces)"): "The omarchy skill (`~/.agents/skills/omarchy/`) is documentation surface, read-only." So mado claims a SKILL.md as its own surface.
- mado `SKILL.md:371-375`: that file "is the domain's instruction authority for end-user customization."
- mado `corpus/knowledge/terminals-and-omarchy.md:115-151` ("omarchy skill anatomy"): frontmatter and body section map of that SKILL.md (`:120-132`). `:138-146` judges its hook listing "illustrative/older than the shipped layout". This contradicts the build seat's claim that the section is read "not to judge the document" (`CensusMado.md`, Finding 5).
- mado `.ufo/waves/round-18/w1/reports/SiblingOverlap18.md:81` assigns "omarchy skill as a document instance (frontmatter/anatomy survey)" to kotoba. The same row adds "(one survey datum; no province clause)". The build seat's quote drops that qualifier, which makes a one-sided assignment look settled.
- kotoba side, at c48793db: `corpus/knowledge/frontmatter-trigger-surface.md:18-19,97-98` and `anatomy-and-compression.md:21-22,86-87` analyse the same omarchy frontmatter and anatomy. `SKILL.md:404` lists it as an observed file. None of these names mado. So the artifact overlap is two-sided, the split statement is one-sided, and the kotoba side is silent.
- Fix: the mado row or its boundary note should disclose the omarchy document-instance overlap (mado owns the read-only documentation surface and the host drift; the frontmatter/anatomy survey is shared).

**F2 (medium): `none` rests on an exclusion the rule does not state.** § Classification rule lists the surfaces as "SKILL.md, PROVINCE.md, corpus files". `.ufo/` is not listed, yet § Limits says "a claim stated only in an unread wave report would be missed". The build seat did read `SiblingOverlap18.md` and recorded the split as "descriptive" without a rule basis. Under the letter, `none` holds. Under the rule's intent (a split of one artifact between sibling and kotoba), `adjacent` is arguable. Either the rule should say `.ufo/` is excluded, or mado should be `adjacent`. Currently the text supports both.

**F3 (medium): the guard cannot falsify the mado row's classification or mechanical cells.** `verifiers/check_sibling_census.py` reads `names kotoba` and `arbitration` but checks only that they are non-empty (lines 383-386). It checks `classification` only for membership in the allowed set (393-398). It does not read the boundary prose. Mutants run in scratch (census copies, PROVINCE copies at `…/RowMado/mut/`):
- M1, census only, mado `names kotoba` `no`→`yes`: exit 0.
- M2, census and PROVINCE both `none`→`adjacent`: exit 0.
- M3, census only `none`→`adjacent`: exit 1 ("FAIL province row 14 (line 24)…").
So the recheck catches cross-file drift only. The census entry's claim that the mechanical columns are checked is not backed by the instrument.

**F4 (low): build-seat slips in the Q14 and Finding evidence.**
- `CensusMado.md` per-token line gives `SKILL.md` 58. Recount over the eight files with `grep -o 'SKILL\.md'`: 68 (SKILL.md 25, README 1, MINT 1, SHONEN 1, SCORECARD 18, LOG 22; PROVINCE and AGENTS 0). The line-count table (28/0/1/0/1/1/13/30 = 74) reproduces. The per-token line gives no command.
- "all inside `.ufo/waves/**` and `corpus/`": `git grep -ic kotoba e33ea30 -- corpus` gives 0. All 34 files are under `.ufo/waves`.
- "PROVINCE.md:34 … kotoba's current line": that is the base a5adc146 file. At c48793db line 34 is blank; the row is now PROVINCE.md:50.
- "SKILL.md:181 … one severity table row": line 181 is prose ("same triggers before they enter any register.").

**F5 (low): paraphrase narrows the sibling's own domain word.** The PROVINCE note says "config". mado's PROVINCE.md:3, SKILL.md:3 and SKILL.md:8 all say "craft", and "craft" is the word that overlaps kotoba's "prompt & skill craft". Suggested wording: "desktop & compositor craft (Hyprland/waybar/walker/terminal config plane); omarchy skill document instance shared, see F1".

**F6 (info): instrument reach and pin drift.**
- `tools/mado-assessment.py` takes `--check PATH` and `--root` (argparse lines 211-215). Its promotion item 1 (`SUBJECTS`, line 21) is a SKILL.md craft check that accepts any path. "Applied to no other lane" is a usage claim, not a code restriction. No committed claim makes it contested under the rule as written.
- `tools/mado-verify.sh:3684-3748` uses the omarchy leaf for link and `readlink` checks (`:3716-3734`) and `sha256sum` (`:3742`). Lines 3749-3962 were not read. Fixture copies at `:664-1063` are test roots.
- Pin drift is only in `.ufo/`; the census keeps the pin, which is correct.

## Evidence (commands, exit codes; all read-only on sibling and lane)

- `git -C mado-shokunin rev-parse master` → `4de44647…`, exit 0. `git cat-file -t e33ea30…` → commit, exit 0. `merge-base --is-ancestor e33ea30 master` → exit 0. `rev-list --count e33ea30..master` → 3, exit 0. `diff --name-status e33ea30 master` → 26 lines, all `A .ufo/waves/round-23/…`, exit 0.
- `git -C mado-shokunin show e33ea30:{SKILL,PROVINCE,MINT,SHONEN,README,AGENTS,SCORECARD,LOG}.md` → sha256 SKILL `f8f856c5…` (1985 L, 169,402 B), PROVINCE `1b25bb1e…` (20 L, 1,950 B); exit 0 each.
- Quote check (Python, scratch copy): `line8 == quote` True; quote inside lines 6-10 True; non-ASCII code points `[0x2014]`.
- Mechanical columns (Python): `description` lines 1; `kotoba` token False; sibling-lane tokens `[]`.
- Q14 recount: `grep -Ec` per file → 28/0/1/0/1/1/13/30, sum 74. Per-token `grep -o`: SKILL.md 68, prompt 7, AGENTS.md 1, frontmatter 0, trigger 2, description 7, kotoba 0.
- `git grep -il kotoba e33ea30 -- .` → 34 files; `git grep -in kotoba` → 226 lines; outside `.ufo`/`corpus` → none, exit 1; `-- corpus` → 0.
- Guard, private clone at c48793db: `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --fleet /home/vgpnk/Projects/shokunin --province PROVINCE.md` → `rows 20 verified 20`, `province rows 20 matched 20`, exit 0.
- Mutants M1 exit 0, M2 exit 0, M3 exit 1 (F3).
- Kotoba-side token search (`_grep`, `(?i)mado|omarchy|hyprland|waybar|walker`, over SKILL.md, PROVINCE.md, AGENTS.md, README.md, corpus/, plans/ at c48793db): `mado` appears only at PROVINCE.md:50, the census row, and plans/round-49.md:30,43.

## Residual risk and verification gaps

- Did not read all of mado's SKILL.md (1985 lines), `tools/mado-verify.sh` beyond :3748, or `tools/mado-tripwire.py`. The "no instrument reads another lane's SKILL.md" finding rests on token searches (`skills/|shokunin|SKILL\.md|AGENTS|glob|os.walk|find`) and the omarchy-leaf reads. A read through a computed path would be missed.
- Did not read `SCORECARD.md` beyond the 18 matching lines, the full rubric, or `LOG.md:771`.
- Did not read `_check_province` (guard lines 478-560) in full; its behavior is inferred from M1-M3.
- `SiblingOverlap18.md` is round 18 (scan 2026-10-20). Its §3.1 split may have been revised later; I checked only that it stays in the pinned tree.
- No web sources were used for this item.

## Tooling record

No installs or updates. Tools used: git (read-only on sibling and lane; `git clone` and `git checkout` only in scratch), python3 (scratch-only reads and mutants), the census guard already in the lane. No jj command ran. No write touched the lane except this report.
