HOLDS-BOUNDED — round-50 learning bar at `956ee1676e4c18480bce8ac3993541462be76e11`: met only by the appended census knowledge (the "six more client pages" section citing S024-S029) and, separately, by C2's capability run entered in SCORECARD; NOT met by C1's SKILL.md description edit on its own bytes; the appended knowledge is not admitted-clean under Q12 (its entry's `source:` and `recheck:` do not cover it), Q13 holds loosely, Q14 holds in content with an incomplete in-entry sweep, and the round-50 Search log is missing.

Seat: KotobaR50.CriticLearningBar (critic, leaf). Judged on: adjacency. Started 2026-10-22T13:30Z, written 13:40Z.
Scratch: /fast/scratch/hyaku/kotoba-r50/falsify/CriticLearningBar/ (private clone `lane/` at 956ee16; fetched pages `pages/`).
Tooling: no install or upgrade (curl, git, python3 with PyYAML, sha256sum already present).

## Findings

F1 — C1's description edit is not one of the four learning forms. The only SKILL.md change in f3046466..956ee16 is the frontmatter
`description` (`git diff f3046466 956ee16 -- SKILL.md`: lines 10-17 only). It is no decision table and no error pattern; it applies a box
that already existed at base (SKILL.md:212-216, "Overlapping sibling skills are named concretely with an arbitration rule in the
description") to kotoba's own file. It changes kotoba's own routing text, which by its own note (SKILL.md:15-17) "never reaches the
omp router", and PROVINCE Frontier (round-50 append) says "whether naming a lane improves routing is unmeasured on any harness". So it
changes neither what kotoba knows nor what it can do. It is grounded in admitted bytes (the round-49 census rows), which makes it a
sound conformance fix, not a learning claim. The plan's label "C1 ... the learning claim" (plans/round-50.md:9) overstates it.
Counterexample: revert the description to base and kotoba's knowledge and instruments are unchanged except one guard verdict.

F2 — What does meet the bar: the appended census section "Round 50: six more client pages" (census entry lines 190-244) changes what
kotoba knows in a PROVINCE Core entry (Core line "Sibling arbitration" points at this file): from "3 pages document no tie-break" to
"9 pages, and every documented which-one-wins rule is keyed on the skill name". The negative claim survives my strongest attack:
re-fetched all six routes 2026-10-22T13:33Z, sha256 prefixes equal the recorded ones (S024 f10ced73, S025 de5ba34f, S026 89aa73eb,
S027 18c361b5, S028 d0d362cc, S029 8e1b4cbe); a broader eight-term sweep (most relevant, choose, select, multiple skills, both match,
overlap, tie-break, priorit) found no rule for two differently named skills whose descriptions both match. Hits are craft advice
("Keep it specific enough for the agent to choose correctly", S024 skills.md:73) or name/location priority (S026 sub-agents.md:156).
This is depth/quality of an existing finding more than expansion: knowledge files 36 → 36 (command E3).

F3 — Q12 is met in form by the entry, not by the appended knowledge (the main gap). The entry's opening trio is byte-identical to
base (E4: md5 of lines 1-3 equal at f3046466 and 956ee16): `source:` names only S022, S023, S018 — not S024-S029 or S019; `recheck:`
is the round-49 census guard. Two mutants show that recheck cannot fail on the round-50 knowledge (E5): deleting both round-50
sections → exit 0, `rows 20 verified 20`; inverting the negative claim to "Every page states a rule ..." → exit 0. The fleet rules
make this material: "Provenance in prose ... is unreadable to a freshness sweep" (CORPUS.md:163-166), and the expansion observable
counts entries whose `source:` cites a mined row (CORPUS.md rule 4, LEARNING.md:33). As written, S024-S029 are `mined` rows whose
only knowledge citer does not name them in its header. Also: PROVINCE Core's sibling-arbitration line still cites only "(S022, S023,
S018)" for the no-tie-break finding; its round-50 append names the description and the precedence, not the six pages.

F4 — Q13 holds loosely. The section gives the sweep command shape (`grep -ciE` plus ten patterns) and the date, and the 1,008-character
figure sits beside the guard command (guard prints `skill description length 1008 of 1024`, E2; PyYAML's parsed folded value is 1,009
with the clip newline — immaterial under 1,024). Counts without a command in `<number> — <command> <date>` form: "now on nine pages"
(a tally of S018, S022, S023 plus six) and "the counts stay 9 adjacent, 11 none, 0 contested" (line 265; the census guard prints no
class split).

F5 — Q14 holds in content, with an incomplete in-entry sweep. Per-term counts are printed in the entry for S024, S025 and S029 only;
S026, S027 and S028 carry quotes and "no overlap rule" with counts only in wave seat reports. The S029 row's anchor includes
`skills-best-practices.md:8-17`, which has `overlap` = 1 ("Avoid overlap: Ensure your skill descriptions are distinct", line 16; E6),
while the entry reports S029 `overlap` 0 (true for skills.md only). The seat report (SrcGeminiCliSkills.md F3) records the hit; the
entry does not. A Copilot SDK page opened by the build wave documents manual remedies for conflicting skills ("Use `disabledSkills` to
exclude conflicting skills", SrcCopilotSkills.md:20) and was rejected as a row; the entry is silent on it. Neither hit is a tie-break,
both support the entry's craft conclusion, so this is a sweep-record gap, not a false claim.

F6 — SOURCES contract rule 5 not met: no round-50 Search log note (identified / screened / included / excluded, stop rationale) in
`corpus/SOURCES.md`; the last note is round 48 (E7; round 49 has none either). The lesson Gate names 3 drafted rows not written, but
no identified or screened counts and no stop rationale.

F7 — The Gate under-records knowledge. "Candidates 1, admitted 1" lists only the six-pages section; the second appended section
(D3 precedence rule, three rulings, two corrections to the round-49 rule and falsify note) is kotoba's own rule appended to admitted
knowledge with no admit line and no source row (it says "the precedence below is kotoba's own rule").

F8 — C2 meets the capability form, bounded. `box_proof_case_deletion.py` was run this round at both revisions (`killed 0 of 6` → `6 of
6`) and is entered in SCORECARD (operability row; Move log rows at SCORECARD.md:252-253). Bound: the `## Capabilities` table row
"dispatch-prompt box check" (SCORECARD.md:261) is unchanged since round 49, and neither `verify_dispatch_prompts.py` nor the new
`check_sibling_census.py --skill` mode appears in PROVINCE Core's instrument list (E8). C2's operability bytes were not re-run by me
(CriticC2Landed and ReplayC2Counter hold that).

F9 — Missing understanding step. The name-keyed finding was not folded into SKILL.md: the craft rule (SKILL.md:150-156, "name the
overlapping sibling and its arbitration rule") and box (212-216) cite no round-50 source and state no consequence of "no client
compares descriptions". A one-row SKILL.md rule grounded in the admitted entry would have made the "SKILL.md decision table or error
pattern grounded in admitted entries" form genuinely met.

## Impacted axes
adjacency (judged: the learning half of the round rests on F2, bounded by F3); freshness/expansion trend (F3: the six rows are
invisible to a header-reading freshness sweep); discernment record (F6, F7).

## Smallest safe correction
1. Write a new knowledge entry (corrections are new entries; the census header is append-only) for the round-50 finding, opening with
   `source:` S024-S029, S022, S019 plus URLs and anchors, `verified-at:`, and a `recheck:` that can fail on the claim — for example a
   re-fetch of the six `.md` routes compared with the recorded sha256 values, exit 1 on any change. Index it in `corpus/README.md`, add
   its path to the six rows' `used-by` (logged old→new), and cite it from PROVINCE Core's sibling-arbitration line.
2. Append the round-50 Search log note to `corpus/SOURCES.md` and put the per-page counts for S026-S028 and S029's best-practices page
   in the entry.
3. Add the D3 precedence section to the Gate as a second knowledge candidate, admitted or rejected with its reason.
4. Re-state C1 in LOG/SCORECARD as a description-conformance claim, not the round's learning claim; or add the SKILL.md craft row of
   F9 grounded in the new entry. Either C2's Capabilities row is appended, or the LOG says why not.

## Evidence (commands, exit codes)
E1 `git log --oneline f3046466..956ee16` → 2 commits (542f515, 956ee16), exit 0.
E2 (clone at 956ee16) `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md`
   → `rows 20 verified 20` / `province rows 20 matched 20` / `skill description names 9 of 9 non-none lanes` / `skill description length 1008 of 1024`, exit 0.
   Same without `--skill` (the entry's recheck) → first two lines, exit 0.
E3 `git ls-tree -r --name-only <rev> corpus/knowledge | grep -c '\.md$'` → 36 at f3046466, 36 at 956ee16, exit 0.
E4 `git show f3046466:corpus/knowledge/sibling-overlap-census-round49.md | head -3 | md5sum` and `head -3` of the file at 956ee16 → both 13462b67…, exit 0.
E5 mutant A (file truncated before `## Round 50: six more client pages`, 189 lines) → guard with `--skill` exit 0, `rows 20 verified 20`, `9 of 9`;
   mutant B (`sed` "No page states a rule" → "Every page states a rule", 1 line changed) → exit 0, same output. File restored; clone `git status --short` empty.
E6 `curl -sSL` of the six routes plus geminicli.com/docs/cli/skills-best-practices.md at 2026-10-22T13:33:08-09Z → all 200; bytes 5365, 22871, 110784,
   11790, 47200, 5763, 3257; sha256 prefixes f10ced73, de5ba34f, 89aa73eb, 18c361b5, d0d362cc, 8e1b4cbe, 612c3b83.
   `grep -ciE 'overlap' S029b.md` → 1 (line 16); `grep -ciE 'tie[- ]?break'` → 0 on all seven; `both match|matches more than` → 0 on all seven.
E7 `git show 956ee16:corpus/SOURCES.md | grep -nE '^- \*\*20'` → 5 notes, last line 102 "2026-10-22 — round-48 sources sweep", exit 0;
   `... | grep -cE '^- \*\*2026-10-2[0-9] — round-(49|50)'` → 0, exit 1.
E8 `grep -nE 'verify_dispatch_prompts|box_proof_case_deletion|check_sibling_census' PROVINCE.md` (clone) → only lines 17 and 31 (check_sibling_census), exit 0;
   `git diff f3046466 956ee16 -- SCORECARD.md` → no hunk in `## Capabilities` (hunks at lines 28-37, 117-122, 245-253).
E9 `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → `ok`, three W04 (S018, S019, S021), exit 0.
