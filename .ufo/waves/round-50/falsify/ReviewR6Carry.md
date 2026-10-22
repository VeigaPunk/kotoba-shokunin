HOLDS-BOUNDED — D6 carry sentences for R4, R5 and R1 at 956ee1676e4c18480bce8ac3993541462be76e11: all three items are still open; R5 holds; R4 holds with two bounds; R1 holds except its clause "needs a floor bump", which fails as a necessity.

# ReviewR6Carry — routed defect D6 (carried items), round 50 falsify

Seat: KotobaR50.ReviewR6Carry (leaf). Scope: D6 only. C1, C2, D1–D5, S024–S029 and Q26 belong to other seats.
Sources checked: `corpus/lessons/round-50.md` lines 132–135 (D6) and the carry text in `.ufo/waves/round-50/build/CarryD6.md` (R4 at lines 40–42, R5 at 67–69, R1 at 111–113, umbrella at 115–118).
Judged bytes: private clone at 956ee16 under `/fast/scratch/hyaku/kotoba-r50/falsify/ReviewR6Carry/lane`. HEAD and master both 956ee16. The lane was read, never edited.
Tools: none installed or upgraded. I used the existing curl, git, jq, sha256sum and python3 (3.14.8). No pacman transaction.

## Verdict per item

| Item | Still open at 956ee16? | Carry reason | Verdict |
|---|---|---|---|
| R4: two count rows without a reproducing command | Yes | True for file contents; bounded by findings 2 and 3 | HOLDS-BOUNDED |
| R5: v2 configured-root oracle not frozen | Yes | True | HOLDS |
| R1: no-name fallback counts a skill opencode skips | Yes | Identity decision and "neither C1 nor C2 depends" are true; "needs a floor bump" fails as a necessity (finding 1) | HOLDS-BOUNDED |

## Findings, by severity

1. MEDIUM (R1; Q26). The clause "needs … an assertion-floor bump" says more than its guard measures. The guard passes when observed is at least the floor: `verifiers/check_assertion_floors.py:525` is `ok = match is not None and assertions >= floor and failures == 0 and proc.returncode == 0`. Its docstring (:6–7) says it fails only when the observed count is below the floor. Observed is 123 and the floor is 123 (`floors-registry.json:30`). A second nameless skill (124 assertions, CarryD6 closing step 3) passes with no bump. Step 1 (keep the fallback and label it) is docstring and SCORECARD text only. A bump is the repo's ratchet convention. The registry's BUMP-IN-STEP RULE makes it a three-site edit: registry, both in-file tables, and the docstring. Round 50 already edits `check_assertion_floors.py` (sibling_census 68 added to both tables and the docstring; `git diff f30464 956ee16`), so a bump collides with two files, not only the registry as the carry says. Fix the wording to: "a bump follows the ratchet convention if the count rises; the guard passes at observed ≥ floor."

2. LOW (R4). "No round-50 counter reads" is exact for file contents, not for the path. SKILL.md:159 cites `corpus/knowledge/frontmatter-rule-authorities-round48.md` by path. The checklist's citation box resolves that token with `(base / …).exists()` (`verify_skill_checklist.py:1483–1504`). Renaming or deleting the file would fail that box, and so the checklist gate that D2 changed, although no counter reads its rows. Restating rows 32 and 56 would not move it. Fix: say "reads its rows" and name the path dependency.

3. LOW (R4). Two recorded statuses. The D5 erratum table (lesson row 16) lists the round-48 entry's lines 32 and 56 as items round 49 rejected. The round-49 "Carried, not rejected" list (lesson lines 109–110) names R5 and R1 but not R4. D6 carries R4. Fix: record the transition once.

4. LOW (R5). Line cite. `R5Disposition.md:82` cites `index.ts:277-278` for the built-in marker comment. In the pinned file (opencode tag v1.19.3, commit e3c4eb24) the comment is lines 276–277, and line 278 starts the assignment. CarryD6's R5 section repeats 277–278. Fix: cite 276–278.

5. NOTE (R5). CarryD6 calls the v1 pin surface "intact". That holds at base revision 197b5a4 only. The instrument's consumer sha `872993f8` is `verifiers/verify_harness_independent.py` at 197b5a4 (`git show 197b5a4:verifiers/verify_harness_independent.py | sha256sum` → 872993f8…). The live module is `54f9c95b`. Not a defect in the carry sentence.

6. NOTE (D6 wording). "Still open at f3046466" is also true at 956ee16 (verified below). Suggest "at f30464, unchanged at 956ee16".

## R4 evidence

- `git grep -n -E '24 not reproducible|printed command cannot produce 0|partly addressed' 956ee16 -- corpus/knowledge/frontmatter-rule-authorities-round48.md` → lines 149, 157, 185; exit 0.
- `git diff --quiet f30464 956ee16 -- <same file>` → exit 0 (byte-unchanged). sha256 `23479c76…`; 186 lines.
- 23 count rows (lines 144–166); two "**no**" verdicts (rows 32 and 56); line 168: "21 of 23 reproduce".
- `git ls-tree -r --name-only 956ee16 | grep -c -E 'p_alias|probes/'` → 0, exit 1. No fixture tree is tracked.
- Copied `/fast/scratch/hyaku/kotoba-r49/seats/R4CountProvenance` to scratch `r4/`. `python3 -B counts.py` → `sources_with_https 5`, `rule_rows 10`, `probe_files 36 probe_dirs 36 probe_distinct 29`; exit 0. The script reads a round-48 scratch glob and the live lane path, so its output depends on uncommitted bytes. That is the open defect.
- Printed row-56 command in the copy: `grep -niE 'third person|reserved|max_lines|line_count|500' validator.py parser.py models.py` → `validator.py:12:MAX_COMPATIBILITY_LENGTH = 500`, exit 0. Executed command: no output, exit 1.
- Readers of the table at 956ee16 (`git grep -n 'frontmatter-rule-authorities-round48'`): `verify_skill_checklist.py:112` (docstring) and `:1431` (detail string); `SKILL.md:159` (citation); `verifiers/corpus-baseline.json:60` (note). No C1 or C2 file opens it. `check_sibling_census.py` opens only its three command-line files (`read_text` at :530, :616, :797: skill, census, province). `box_proof_case_deletion.py` reads a `git archive` tree. `verify_dispatch_prompts.py` reads the box map, SKILL.md and manifest (:1027–1045). The checklist's governance check reads only LOG.md and SCORECARD.md (:386).
- "Closing it would not move either counter": supported by those reads. [INFERENCE: no mutation run.]

## R5 evidence

- `git grep -l 'configured-root-oracle-v2' 956ee16` → only `.ufo/waves/round-49/build/R5Disposition.md` and `.ufo/waves/round-50/build/CarryD6.md`; exit 0. `ls .ufo/round-50/oracle` → No such file; exit 2.
- `git show 956ee16:.ufo/round-48/oracle/config-root-cases.json | sha256sum` → `1d09a38c…`. `jq -r '.schema, (.cases|length)'` → `kotoba-configured-root-oracle-v1` and `13`. base_revision `197b5a4`.
- instrument.json `instruments[1].sha256` = `1d09a38c…`. `git grep -l 1d09a38c 956ee16 -- .ufo/round-48/verification/` → 4 files.
- Ruler `.ufo/round-48/tools/config-root-ruler.py`: lines 161–163 (oracle hash), 165–166 (schema), 179–181 (baseline receipt revision and oracle hash), 184–185 (non-BASE revision needs the receipt). All as CarryD6 states.
- Pre-registration: instrument.json keys include `immutable_before_receipt`, `literal_parent_base_argv` and `pre_I_amendment`.
- `git show a5adc146:verifiers/verify_harness_independent.py | sha256sum` → `f576c23f…`, the BASE consumer hash CarryD6 names for v2.

## R1 evidence

- `git show 956ee16:verifiers/verify_harness_independent.py | sha256sum` → `54f9c95b…`. Unchanged from f30464 to 956ee16 (diff exit 0).
- `python3 -B verifiers/verify_harness_independent.py --self-test` in the clone → `0 failure(s) over 123 assertions`; exit 0.
- `floors-registry.json:30` `"floor": 123`; `instrument_total` 11 (line 3).
- `skill_identity` at :291, return at :311–312. Derive comment :670–673 ("the case the agents root has always fallen back to"). Fallback arm :1661–1663 expects 3.
- Six-shape probe on the landed module, my own fixtures in scratch `r1probe/` (build seat's `fx/` not re-run); exit 0:
  - no name → `{'description': …}` → `'no-name'` (dir)
  - `name: ""` → `{'name': ''}` → `'empty-name'` (dir)
  - `name: 123` → `{'name': '123'}` → `'123'`
  - `name: x # note` → `{'name': 'x # note'}` → `'x # note'`
  - `"name": x` → `{}` → `'quoted-key'` (dir)
  - unreadable → `{}` → `'unreadable'` (dir)
  The landed-module column of CarryD6 matches.
- Opencode, pinned `packages/opencode/src/skill/index.ts` (tag v1.19.3, commit e3c4eb24…): fetched 2026-10-22T13:36:49Z; HTTP 200; 11,843 B; sha256 `91dce57f…` (same as R5Disposition). Quotes: :56 `typeof data.name === "string" &&`; :121 `if (!md) return`; :123 `if (!isSkillFrontmatter(md.data)) return`; :134 `state.skills[md.data.name] = {`. All match CarryD6.
- Parser: `ConfigMarkdown` → `packages/core/src/config/markdown.ts` (fetched 13:38:48Z; 1,220 B; sha256 `add3093b…`) → `matter` from gray-matter. The two YAML rows (`x # note` → x; `"name": x` → key name) follow from YAML rules. [INFERENCE: gray-matter source read, parser not executed.] The catch block at :110–118 was not read in full, so the unreadable row rests on :121 alone.
- Carry reason, clause by clause:
  - "needs an identity-contract decision": TRUE.
  - "neither C1 nor C2 depends on that operator": TRUE. `git grep -l harness_independent 956ee16 -- verifiers/check_sibling_census.py verifiers/box_proof_case_deletion.py verifiers/verify_dispatch_prompts.py verifiers/verify_skill_checklist.py` → no match; exit 1.
  - "round 50's D3 registration is already editing" the registry: TRUE (sibling_census 68 added; instrument_total 10 → 11).
  - "needs … an assertion-floor bump": FAILS as a necessity (finding 1).

## Commands and exit codes

- `git clone` of the lane, then `git checkout -q 956ee16` → 0. `git rev-parse HEAD master` in the clone → 956ee16 for both. Lane master, read-only → 956ee16.
- `git diff --stat f30464 956ee16` → 50 files. The R1 module, the round-48 table and `.ufo/round-48/` are not in the list.
- `curl -sSL` on the three opencode files → HTTP 200 each; exit 0.
- `python3 -B counts.py` (copy) → 0. Printed and executed row-56 greps → 0 and 1.
- `python3 -B verifiers/verify_harness_independent.py --self-test` → 0.
- `python3 -B verifiers/check_assertion_floors.py` ran as a background job. Only part of its output came back (PASS lines for harness, corpus_integrity, corpus_independent, surfaces, checklist 1851, pins). Its final exit code was not captured, so I used nothing from it.

## Residual risk and gaps

- "Closing does not move C1 or C2" rests on code reads and `git grep`, not a mutation run.
- The gray-matter parse was not executed; two R1 table cells are inference.
- `trigger.citation_resolves` was not run. The C1 and C2 counters were not run here; other seats own them.
- The floor guard's final exit code was not captured.

Scratch: `/fast/scratch/hyaku/kotoba-r50/falsify/ReviewR6Carry/` (lane clone at 956ee16, `src/` fetched sources, `r4/` copy, `r1probe/` fixtures).
