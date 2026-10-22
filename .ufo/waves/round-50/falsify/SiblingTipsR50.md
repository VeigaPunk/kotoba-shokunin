# SiblingTipsR50 — do moved sibling tips contradict a clause of kotoba's description at 956ee167?

Verdict: **HOLDS-BOUNDED** — for the six lanes named in kotoba's round-50 description
(chousa, kake, kama, kasegi, kotodama, tameshi), no change between the round-49 census pin and
the live branch tip contradicts any description clause. Bounded because four of the six tips
moved (files under `corpus/`, plus `SKILL.md`/`PROVINCE.md` in kake, kama, tameshi), every
frontmatter `description` is byte-identical pin-to-tip, and two tips advanced *during* this read —
so a tip-level claim must name its revision.

Scope. Judged kotoba bytes: `git show 956ee1676e4c18480bce8ac3993541462be76e11:SKILL.md`
lines 1-19. Clauses tested, verbatim: (a) "kagi, kake, kasegi, kengaku and kumitate own their
own SKILL.md content — this skill audits and reports; fixes route to the owning lane";
(b) "chousa owns the research method"; (c) "kama owns endpoint verification"; (d) "kengaku owns
measured effects of prompt format"; (e) "tameshi owns the fixture and mutation method";
(f) "NOT kotodama-shokunin: kotodama owns naming and language for fictional worlds".

## Per lane

| Lane | Census pin | Branch tip (2026-10-22T13:33:58Z) | Changed since pin | Clause | Contradiction |
|---|---|---|---|---|---|
| chousa | `6c5eb146` (master) | `6c5eb146` (master) | none — `diff --stat` empty | b | none |
| kake | `e73d48bb` (master) | `91b60bd4` (master) | 14 files, +1529/−56; `SKILL.md` 113, `PROVINCE.md` 35 | a | none |
| kama | `c808ba07` (master) | `1560e4d8` (master) | 8 files, +666/−9; `SKILL.md` 34; `PROVINCE.md` none | c | none |
| kasegi | `1fafde8f` (master) | `1fafde8f` (master) | none — `diff --stat` empty | a | none |
| kotodama | `35f0d49f` (main) | `6524184e` (main) | 11 files, +1178/−19; no `SKILL.md`/`PROVINCE.md` | f | none |
| tameshi | `3b20f073` (master) | `b1cc95e1` (master) | 13 files, +1174/−42; `SKILL.md` 114, `PROVINCE.md` 13 | e | none |
| kengaku (control) | `1f3b0f1e` (master) | `1f3b0f1e` (master) | none — `diff --stat` empty | d | none |

- **chousa.** Master is the pinned commit: nothing changed. Clause (b) holds, but its only basis
  is kotoba's own text — the census itself records "no chousa-side split was cited" and the
  recheck reads pinned bytes. Unchanged tip therefore adds no lane-side support either.
- **kake.** Tip has a new `PROVINCE.md` § "Round-29 base-path frontier step" and a base-path
  audit gate (`scripts/base_path_audit.py`); `PROVINCE.md:3` still reads "**Domain:** web
  properties & publishing — scopes ds4cc.com, kimi.page/pro mirrors, Pages deploys". The
  aggregator lesson the census uses for the split ("Aggregator-owned file; the owning lane
  corrects `SKILL.md`", `corpus/lessons/round-5-aggregator-mirror-pathless-cli-invocation.md:4-5`)
  is untouched at the tip. Clause (a) holds; kake still owns its own skill-file content.
- **kama.** The 34 changed `SKILL.md` lines add § "Round-25 decision rows: declared versus
  served context capacity" — `/props`, `/slots`, `/v1/models`, verbose startup log. That is
  endpoint verification exactly, so clause (c) is strengthened. kama's own split
  (`corpus/knowledge/cross-lane-scope.md:29`: "**Kotoba** owns the instruction/agent surface and
  its model/fallback wording; **kama** owns independent verification of the target endpoint") is
  unchanged. Its mutation-experiment registry rows also changed counts, but those rows existed at
  the pin and describe kama's own report-audit probes, not ownership of the mutation method, so
  clause (e) is not touched.
- **kasegi.** Master is the pinned commit: nothing changed. Clause (a) holds; kasegi's aggregator
  lesson (its half of the split) is at that same revision.
- **kotodama.** Only `corpus/` moved: `corpus/knowledge/linguistics/sign-languages-manual-modality.md`,
  `.../speech-surrogates-whistled-drummed.md`, a pasture/husbandry revision, SOURCES/README and
  round-51/52 lessons. `SKILL.md` is byte-identical, including the refusal "NOT prompt/skill craft
  (kotoba-shokunin)" — clause (f) holds and the non-reciprocal name collision is unchanged.
  This branch advanced from `c3297ff9` to `6524184e` between two polls of this read; the delta
  touched no `SKILL.md` or `PROVINCE.md`.
- **tameshi.** `PROVINCE.md` gained a round-26 Core append at line 103+ (mutation legs now nine;
  the ninth is kumitate `scripts/cite-check.mjs`). Lines 14-17 — "every lane's gate remains its
  own … Never edits a sibling's gate code" — are unchanged, so clause (e) holds and its
  read-only posture survives. Note for the D3 record, not a contradiction: tameshi keeps adding
  sibling instruments to its own ledger, which is the sibling-to-sibling item the census already
  ruled on, not a claim on kotoba's ground.
- **kengaku (control, not newly named).** Pin equals tip, and its frontmatter still names kotoba,
  so the census "names kotoba: yes" cell is stable. Clause (d) holds.

## What the bounded part means

- All four moved lanes keep their frontmatter `description` byte-identical
  (`diff` of the extracted frontmatter block → no output). The clauses kotoba's description
  makes are about sibling *scope ownership*, and the scope sentences have not drifted; the
  growth is corpus and self-scoped SKILL rows.
- No added line in any moved lane's `SKILL.md`, `PROVINCE.md` or `corpus/` names kotoba
  (`grep -cE '^\+.*kotoba'` → 0, exit 1, for kake, kama, tameshi, kotodama). So no lane has
  published a new split or a new claim over kotoba's ground since the pins.
- Residual gap: because `check_sibling_census.py` rechecks pinned bytes and never a branch tip,
  a future sibling edit that removed a clause's basis would not be caught by the guard. This
  round's tips do not do that; nothing in the instrument would notice if they did.

## Evidence (commands, exit codes)

Working directory `/home/vgpnk/Projects/shokunin`; `TIP` read 2026-10-22T13:33:58Z.

1. Tips: `git -C <lane>-shokunin rev-parse master|main` → chousa `6c5eb1466f2b8abbd3de576389037f435016d07b`,
   kake `91b60bd40c07de351c54ebdc366502f33dc19412`, kama `1560e4d83f42b04f40336357de6f9637eafa0f4b`,
   kasegi `1fafde8f11454f3b0b98ab7f2b2e640aaf7f399a`, kotodama `6524184e9c55665b84884a25ec240c695cacb64e`,
   tameshi `b1cc95e1fb62532646d74e2863770c4fed0851cc`, kengaku `1f3b0f1ec41ec297130e8944ff97968d32324632`. Exit 0.
   (First poll at 13:31Z showed kake `f80bd8fa`, kotodama `c3297ff9`; both advanced.)
2. `git -C <lane>-shokunin diff --stat <PIN> <TIP> -- SKILL.md PROVINCE.md corpus` → the per-lane
   counts in the table. Empty output with exit 0 for chousa, kasegi, kengaku (pin == tip).
3. Frontmatter identity: `diff <(git show PIN:SKILL.md | awk frontmatter) <(git show TIP:SKILL.md | awk frontmatter)`
   → `IDENTICAL` for kake, kama, tameshi, kotodama. Exit 0.
4. Census quotes still resolve at tips: `git -C <lane>-shokunin grep -cF '<quote>' <TIP> -- <file>`
   prints a matching-line count — chousa 1, kake 1, kama 1, kasegi 2, kotodama 1, tameshi 1,
   kengaku 1, exit 0. The quoted rows were read directly and sit where the census says: chousa
   `PROVINCE.md:3`, kake `PROVINCE.md:3`, kama `SKILL.md:8`, kasegi `PROVINCE.md:3` (its second
   match is a body restatement at line 9), tameshi `PROVINCE.md:3` (`git show <TIP>:<file> |
   sed -n '3p'`), kotodama `SKILL.md:8` and kengaku `SKILL.md:3` (frontmatter read). Exit 0.
5. Split lines at tips: `git show <TIP>:PROVINCE.md | sed -n '14,17p'` (tameshi) and
   `git show <TIP>:corpus/knowledge/cross-lane-scope.md | sed -n '29p'` (kama) → quoted text present.
   Aggregator lessons: `git show <TIP>:corpus/lessons/round-5-aggregator-mirror-*.md | sed -n '4,5p'`
   → present for kake and kasegi. Exit 0.
6. New kotoba/prompt-craft claims: `git diff PIN TIP -- SKILL.md PROVINCE.md corpus | grep -cE '^\+.*kotoba'`
   → 0, exit 1 (no match) for all four moved lanes. Adjacent greps for `prompt|frontmatter|trigger word`
   in added lines return only the lanes' own round-prompt template-compliance rows in their lessons.
7. Newest kake/kotodama deltas (`f80bd8fa..91b60bd4`, `c3297ff9..6524184e`) restricted to
   `SKILL.md PROVINCE.md` → empty output, exit 0.

## Unknowns

- Tooling: none installed or upgraded this seat; every command above used git, grep, sed, awk, diff.
- The tips are live lanes mid-round; this report judges the revisions in evidence item 1 only.
- kumitate and kagi were outside this ticket's lane list; their pins were not compared to tips.
- All six clauses are lexical statements about ownership; a semantic widening of a sibling's scope
  that keeps the words would not be caught here. None of the observed diffs does that.
