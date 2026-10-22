# ReviewD5D6 — attack the D5 and D6 edits (round-51 falsify, hyaku 2026-10-22)

Verdict: **HOLDS-BOUNDED** — D5 and D6 repairs hold at HEAD `59903b2`; two minor citation-precision
defects found (M1 stale self-citation, M2 loose "append-only" label), neither breaks a claim.

Scope: `git diff 43ca0bf 59903b2 -- PROVINCE.md corpus/knowledge/sibling-overlap-census-round49.md`
(90 insertions, 1 deletion; the single `-` line is the D5 kama row replacement). Sibling quotes verified
by `git show` against kama `c808ba07` and kengaku `1f3b0f1e`. All work in scratch clone
`/fast/scratch/hyaku/kotoba-r51/falsify/ReviewD5D6/lane` at HEAD; lane untouched.

## Findings

### M1 LOW (census, D5 kama entry): stale self-citation "PROVINCE.md:44 now carries"
The appended D5 kama entry says the BASE row "quoted kama's split" at `PROVINCE.md:44` (true at BASE,
verified) and that "`PROVINCE.md:44` now carries that full sentence". At HEAD the kama row is at
`PROVINCE.md:46`: the D6 status paragraph inserted at line 34 in the same round pushed it down by 2.
Past-tense `:44` is correct; present-tense "now carries" resolves to the wrong line. The census guard
does not catch this (it checks lane set, classification and commit only). Fix is a one-token citation
update in the append-only entry (`:44` → `:46` for the "now" clause, or note the D6 shift).

### M2 LOW (PROVINCE.md:34, D6 paragraph): "Round 51 (append-only)" over-claims for this file
The paragraph labels round 51 "(append-only)" and adds "No row and no classification changes". The same
round's diff rewrites the kama row in place (the diff's only `-` line): boundary text changed (quote
completed, deletion citations bounded). Classification, commit `c808ba07…` and the row's ruling tail
are byte-identical BASE→HEAD, and the appended census D6 section is genuinely append-only (0 `-`
lines) — but the PROVINCE edit is not. The census D5 entry states it precisely ("the classification,
the commit and the basis of the kama row are unchanged"); the PROVINCE label does not. Calibration
blemish only; no claim depends on it.

## Verified (no defect)

- **D5 kama quote verbatim.** kama `c808ba07` `corpus/knowledge/cross-lane-scope.md:29` second cell:
  "**Kotoba** owns the instruction/agent surface and its model/fallback wording; **kama** owns
  independent verification of the target endpoint." The PROVINCE row and census line 400 quote it
  character-for-character including the bold markers (final period outside the quotes); census line 269
  already carried the same full sentence ("at the line above" claim true).
- **D5 deletion citations bounded and accurate.** `consumer-registry.md:56-57` = "Most consumer files
  are gone. Deleted since round 2:" with `~/.config/opencode/agents/` on 57. `cross-lane-scope.md:57,59`
  = round-10 corrections A26/A27, each of `janitor.md`/`distiller.md` absent "shape-only, no body read".
  `corpus/README.md:51-55` names only `janitor.md` (:52) and says "2026-10-14 re-census all three files
  are deleted or emptied" (:54) — "a re-census date … not a deletion day" is a fair reading.
- **D5 kengaku quote verbatim.** kengaku `1f3b0f1e` `corpus/README.md:192` is the `plans/round25_census.sh`
  table row; the census quote matches verbatim; the parenthetical lists six outputs and "frontmatter
  triggers" is the fifth. Top-level `README.md` at that pin is 14 lines ("a bare `README.md:192` does not
  resolve" true). `plans/round25_census.sh:11-27` documents exactly the 14 keys the entry lists. The
  round-50 withdrawal it relies on exists above the append (census ~357-360, seat `RowKengakuR50.md`);
  the false premise stays at census line 273, corrected append-only — consistent with the file's rule.
- **D5 moves no classification.** Kama row keeps `adjacent` / `c808ba07…` / identical ruling tail;
  kengaku row untouched by the diff; counts restated 9 adjacent, 11 none, 0 contested.
- **D6 pure append.** Census hunk `@@ -368,3 +368,90 @@` — zero `-` lines anywhere in the census diff.
  PROVINCE: one 2-line insertion at :34 (D6) plus the D5 row replacement; no other `-` line exists.
- **D6 adds no ruling.** The appended section only (a) marks the rule provisional until the operator
  answers fleet `.ufo/l0-questions.md:105` — verified: kotoba round-50 line, ends "Accept, or rule
  otherwise?", no answer; the file's two `L0 ANSWER` markers are exactly lines 52-53 (kama r11, tsukuroi
  r12, other lanes); (b) records the written-after-the-rows ordering; (c) bounds the generic-refusal
  exit, marking tameshi as the generic-refusal-cleared row (consistent with census :347-349 and
  RowTameshiR50 F4); (d) states round 51 neither extends nor relies on the rule. No clause amended, no
  row measured under the rule beyond the three already decided.
- **D6 cross-references all resolve.** Census lines 165 (kengaku), 180 (tameshi), 185-186 (kama) are the
  three round-49 "possible `contested`" items. Rule+rulings landed in one commit `956ee16` ("round-50:
  D3 precedence rule and rulings (no row moves)"). `corpus/lessons/round-50-verifier-spotcheck.md:207-213`
  says the rule "was written after the rows were known" and its "exit clause clears exactly those three".
  `../.ufo/waves/round-50/falsify/RowTameshiR50.md:37` = F4 (two definitions of contested), and its
  section 3 is "Would claim-always-wins change the row?" — matches "the same finding, section 3".
  `RowKamaR50.md:33-43` spans F4 (:33, excuse not premise) and F5 (:39-43, claim-always-wins flip).
  mado stays `none` with no sibling split (census :82, `no | no`), i.e. on the classification rule alone.
- **Verifier at HEAD (scratch clone):** `python3 -B verifiers/check_sibling_census.py
  corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md` →
  `rows 20 verified 20` / `province rows 20 matched 20` / `skill description names 9 of 9 non-none
  lanes` / `skill description length 1019 of 1024`, exit 0.

## Residual risk and verification gaps

- The kengaku entry's claim that a run of `plans/round25_census.sh` at the pin prints 14 keys
  (`sources_rows=76`, `skill_frontmatter_triggers=6`, …) is a build-seat claim; I verified the header
  documents the 14 keys but did not re-run the script.
- `.ufo/l0-questions.md` is a live fleet file; line 105 verified today (2026-10-22); it can move after
  an operator answer, which would make the "provisional" note's citation stale by design.
- M1/M2 are text-precision defects in append-only media; repairing them means a further appended
  erratum, not an in-place rewrite.

## Evidence (commands, exit codes)

- `git clone -q <lane> scratch/lane && git checkout -q 59903b2` → exit 0; `git log --oneline -3` shows
  `59903b2` (baseline re-record) atop `e621902` (D1), `34cfffb` (C2/D1-D7).
- `git diff 43ca0bf 59903b2 -- PROVINCE.md corpus/knowledge/sibling-overlap-census-round49.md` →
  `4 ++-, 87 ++`, total "90 insertions(+), 1 deletion(-)"; sole `-` line = BASE kama row.
- `git -C kama-shokunin show c808ba07:corpus/knowledge/cross-lane-scope.md` (line 29, 57, 59);
  `…/consumer-registry.md` (56-57); `…/corpus/README.md` (51-55) → exit 0, contents as above.
- `git -C kengaku-shokunin show 1f3b0f1e:corpus/README.md | sed -n 188,196p` → line 192 as quoted;
  `show 1f3b0f1e:README.md | wc -l` → `14`; `show 1f3b0f1e:plans/round25_census.sh | sed -n 11,27p` →
  the 14 documented keys, exit 0.
- `grep -n 'kama | adjacent' PROVINCE.md` → line 46 at HEAD; `git show 43ca0bf:PROVINCE.md | sed -n 44p`
  → kama row (BASE). `grep -c '^-'` on the two-file diff → 1 (kama row only).
- `sed -n 105p .ufo/l0-questions.md` (fleet) → kotoba round-50 line, "Accept, or rule otherwise?";
  `grep -n 'L0 ANSWER'` → lines 52, 53 only.
- Verifier run quoted above, exit 0. No tools installed (python3 present; nothing upgraded).
