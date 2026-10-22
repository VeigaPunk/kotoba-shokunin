Result: MIXED — every routed stale mention was corrected in place at c8407a45 except `PROVINCE.md:26`, a Frontier bullet that still asserts the superseded `7 of 7` client count with no declared-result qualifier.

# ReviewMoreStale — remaining stale round-51 mentions at c8407a453788df964df5a7b835dd0ce1360de882

Scope: every lane file except `LOG.md` and `.ufo/`, searched at the judged revision with
`git grep <rev>` plus pathspec excludes (10,934 files at rev). Also swept the uncommitted
`SCORECARD.md` working-tree diff (the attempt-1 leftover, a named attack target) and the
safety-net strings `overlap levers backed`, `rows are new`, `of 7 clients`. Commands were
read-only `git grep`/`git show`/`git diff` in the lane; no lane mutation, no installs.

## Findings

### Still needs a correction

1. **`PROVINCE.md:26` (LOW; arguably HOLDS).** The Frontier bullet still reads "round 51: the
   per-client overlap levers moved to Core — 7 of 7 clients document a non-wording removal
   lever, and none of them is a tie-break". The same file's Core bullet (`PROVINCE.md:17`)
   carried the identical claim as the counter output `overlap levers backed 7 of 7 clients`
   and got the round-52 correction appended at `:18`; the README note (`corpus/README.md:153`)
   and index row (`:75`) and `SCORECARD.md:28` all got the declared-result qualifier. This
   bullet alone still states the 7-of-7 fact unqualified. Mitigating: it does not print the
   counter string, and the count is factually supported — the surviving head counter's
   `LEVER_IDS` still covers all 7 clients and the same bullet's "none is a tie-break" holds.
   Verdict: residual stale mention by the lane's own correction convention (M36: a block
   stating the superseded result must also hold the declared one); a one-clause qualifier
   ("on the falsify-hardened counter; declared 4 of 7") would close it. The M36 registry in
   `verifiers/check_correction_sweep.py:31-37` can never catch this class — its `stale`
   pattern is the literal counter string `overlap levers backed 7 of 7 clients`, which
   `PROVINCE.md:26` does not contain (informational registry gap, not a defect in the fix).

### Corrected (append-only corrections present, per lane convention "corrections in place of record")

- `corpus/README.md:147-157` — pre-falsify lever set (`ignoredSkillsLocations`,
  `disable-model-invocation: true`, opencode `deny`) and unqualified `overlap levers backed
  7 of 7 clients` retained as record; the correction at `:158-167` gives the declared 4 of 7
  and the falsify-corrected lever list. FIXED per convention.
- `corpus/README.md:75` — index row still says "(removed everywhere, or automatic choice
  off)" and cites S031; the appended correction names `removed in a scope` and the declared
  count "4 of 7 on the plan-commit counter `7c81a787` (7 of 7 only on the widened counter,
  Q28)". FIXED per convention.
- `PROVINCE.md:17` — `overlap levers backed 7 of 7 clients` retained; correction at `:18`
  gives declared 4 of 7 and points at `SKILL.md` § Anti-patterns. FIXED.
- `SCORECARD.md:28` (committed) — depth lead now opens "declared result … `4 of 7`, exit 1
  on the landed content"; the widened `7 of 7` @ `34cfffbb` is labelled "Second measurement,
  never the declared one (Q28)"; "six rows are new" gone — the cell now says "four counted
  rows are new … (the 'six' first written here was the pre-falsify count)". FIXED.
- `corpus/SOURCES.md:44` (S031) — the false `disabledSkills` claim remains in the `teaches`
  cell by rule (contract v1 rule 2 forbids in-place edits, recorded at
  `corpus/lessons/round-51.md:188-191`); superseded by S038 (`corpus/SOURCES.md:51`), whose
  teaches cell states "it does not contain `disabledSkills` (0 occurrences), which S031
  named". FIXED by supersession. Residual nit: S031's own row carries no
  "superseded by S038" marker in the fetched/teaches cells (the S038 row points back, not
  the reverse); readers of the index row `corpus/README.md:75` still see S031 cited, and
  `check_overlap_levers.py:695` `LEVER_IDS` pins `S031`, so the S031 citation in
  `SKILL.md:412` is counter-required, not stale. Severity: none.
- `corpus/knowledge/skill-overlap-levers-round51.md` — the `deny`, `ignoredSkillsLocations`,
  `disable-model-invocation: true` and `"removed everywhere"` mentions at `:30,34,94-95,115,
  118-119,130,136` are all inside the corrected counted table or the "Other levers … not
  counted" / "Falsify-wave corrections" records (`:112-140`). FIXED/corrected state.

### Historical record (lessons, plans, spot-checks, older entries — no correction owed)

- `corpus/lessons/round-51.md` `:5,7,146,150-165,188-190` — the round's own lesson and M35
  record; names `ignoredSkillsLocations`, `disable-model-invocation: true`, `deny`,
  `disabledSkills` as what was widened/replaced. Record.
- `corpus/lessons/round-51-verifier-spotcheck.md` `:19,37,60,64-66,70,77,81,108-109,120-128,
  161-165,171` — the closure's own record; it is the document that routed the corrections.
  Record.
- `corpus/lessons/round-52.md` `:10,38-39,73` — M36 and S038 records quoting the stale text
  to document the fix. Record.
- `plans/round-51.md` `:14,32,37,81,108-111` — the plan's frozen statement plus its own
  `34cfffbb`-widening disclosure (`:110` already states the plan-commit counter counts 4 of
  7). Record.
- `plans/round-52.md` `:66-74` — quotes the defects verbatim to route them. Record.
- `corpus/knowledge/sibling-overlap-census-round49.md` `:32,310,463-465`,
  `corpus/knowledge/skill-selection-rules-round50.md:55,97`, `corpus/lessons/round-50*.md`,
  `corpus/knowledge/harness-router-models-round9.md:126`,
  `corpus/knowledge/harness-verifier-round10.md:130`, `corpus/lessons/round-8.md:90` —
  older-round records where `disable-model-invocation: true` and per-skill `deny` are
  documented facts of their rounds, not the superseded count or lever claim. Record.
- `considerthese/2026-10-19.md:29` ("artefact denylist"), `corpus/SOURCES.md:121` (search-term
  list) — unrelated `deny` usages. Not stale.

### Structural (verifier internals, not corpus statements)

- `verifiers/check_correction_sweep.py` `:6-7,32-36,107-111` — stale phrases are the
  detection registry and self-test fixtures; correct by construction.
- `verifiers/check_overlap_levers.py` `:31,55,124,159,163-171,596,661-680,778-779,814,830,
  868,884,910,923,932,979,991-999,1082,1193-1250,1301-1310` — `ALLOWED_EFFECTS` still lists
  `removed everywhere` as a legal value (no landed row uses it; keeping the value is
  harmless), `LEVER_IDS` pins S031 (see above), and the deny/`7 of 7` hits are self-test
  worlds. Correct.

### `SCORECARD.md` uncommitted leftover diff (attack target)

`git diff -- SCORECARD.md` (8 insertions, 2 deletions): replaces the coverage and freshness
leads with round-52 C2/C1 records, adds the "Round 52 completed" block and two claim-log
rows. The added text contains none of the seven stale patterns — its counts are `5 of 7`
(mcp instructions), `4 of 4` (callee rename) and `pass 7`/`self-test 119 → 129`, all with
`frozen 4c003a4b` labels. The stale `7 of 7`/`removed in a scope` hits in the diff are
context lines of the untouched depth row (`:28`). One content nit (not a stale mention): the
added "Round 52 completed" block says "S038 supersedes S031" and routes the still-carried
items to "Next: round 53" — accurate per `corpus/lessons/round-52.md:73-76`. Clean.

## Severity summary

- LOW: `PROVINCE.md:26` unqualified `7 of 7` restatement (the only hit matching the
  superseded-claim shape that lacks a declared-result qualifier anywhere in its block).
- Informational: the M36 sweep registry matches only the literal counter string, so prose
  restatements like `PROVINCE.md:26` are permanently outside its net; S031's row bears no
  back-pointer to S038 (convention-consistent, single direction).

## Verification gaps / bounds

- No `lsp` server answers these Markdown/Python files' semantics here; hits were classified
  by direct line reads, which is the level this task needs.
- `PROVINCE.md:26` is a judgment call: it is factually supported by the surviving counter,
  so HOLDS is defensible; flagged because the lane's own M36 convention (a block stating
  the superseded result must also hold the declared one) would qualify it.
- All greps were `git grep` at `c8407a45` with `:(exclude)LOG.md` `:(exclude).ufo`; the
  `.ufo/` exclusion covers wave reports including attempt-1 leftovers.

Report: .ufo/waves/round-52/falsify-a2/ReviewMoreStale.md
