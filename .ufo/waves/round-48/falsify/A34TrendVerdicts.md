# A34TrendVerdicts — round 48 trend verdicts (expansion, quality, discernment)

**Verdict: DEFECT (medium).** The honest trend verdicts are **expansion improved (bounded, +1 entry)**,
**quality improved (bounded)** and **discernment improved (bounded)**. Each is still falsifiable as
landed, so none should be recorded unqualified. The landed entry fails part of the bar it claims
(Q14, and Q23 since `d28b16b`). Unless that is fixed, LEARNING.md's harmed clause for expansion
("an admitted entry fails the bar it was admitted under") is in play.
Targets: `d1ae458` (C2), `887b6af` (C1), `84b9c9b` (records). The lane moved to `d28b16b` (falsify
corrections) during this review, and every finding below was re-checked there.

## Proposed verdicts

| trend | proposed verdict | what would make "improved" false |
|---|---|---|
| expansion | improved, bounded: 34 → 35 Markdown entries; 1 entry on ground the coverage map did not hold | (E1) the entry is ruled to fail its admission bar; (E2) the ground is ruled to be held already by `SKILL.md:151` plus Core `trigger.no_xml_tag` |
| quality | improved, bounded: 4 mis-credited source rows superseded by re-opened rows; `SKILL.md:151` corrected; 2 stale live-24/24 claims marked | (Q-a) stale entries ruled unmarked, because the mark exists only in the README index row; (Q-b) C2's new exit 2 on an unreadable root ruled a new false red (Q05/Q18); (Q-c) the new entry's form defects ruled a failed re-check |
| discernment | improved, bounded: round-47 outside disagreements became lessons with grounded criteria (M24 → Q20/Q23, M26 → Q21, M28 → Q22) | (D1) Q23 landed in the same commit that edited the entry, yet the entry still fails Q23; (D2) round 48 has no non-author spot-check of its own gate yet |

## Evidence

**Counts (my runs, lane read-only):** `git ls-tree -r --name-only <rev> corpus/knowledge | grep -c '\.md$'`
gives 34 at `75f671b`, 35 at `887b6af`, 35 at `84b9c9b` (all exit 0).

**Rule 4 (expansion counts admitted entries citing a `mined` row on uncovered ground):**
- The entry's `source:` line cites S018, S017, S019, S012, S021 and S020, and all six are `mined` in the registry.
- Base knowledge held none of this ground.
  `git grep -n -i -E '1024|1,024|64 char|xml tag|no_xml_tag|quick_validate|packager|agentskills|S001|S003|S012|reserved word|third person|consecutive hyphen' 75f671b -- corpus/knowledge`
  returned 2 unrelated hits (`harness-system-prompt.md:28`, `render-mechanism-round7.md:24`).
- The base coverage map has no validity-by-authority row. Its one `authorit` hit is the
  "Frontmatter trigger surfaces" row, which covers description trigger content.
- Partial prior hold, which E2 attacks: base `SKILL.md:151` already stated name ≤64 equal to the directory,
  description ≤1024, no XML tags, and "packager is stricter". The README Frontier says the XML-token rule
  "moved to Core". Ground new at base: consecutive hyphens, reserved words, third person, unknown
  fields, the skills-ref and Codex columns, the Unicode-name split and the run counterexamples.
  Most of the table is therefore new ground, so E2 fails as a refutation but bounds the claim.
- Axis label: the lane filed this entry under freshness, while 34 → 35 is the expansion observable.
  A09 rates that a medium defect, and the lesson records the disagreement without retargeting.

**E1: the entry fails its own stated bar (still true at `d28b16b`).**
1. *Mislocated quote (CORPUS "a quote names its location"; Q23 "located quote").* Entry line 58 cites
   "the frontmatter table (spec.md:27)". Re-fetched `https://agentskills.io/specification.md`
   (2026-10-22T08:53:15Z, 7608 B, sha256 `9a67de89…`, the same bytes as S018): line 27 is blank, and the quote is
   at line 30, "Max 64 characters. Lowercase letters, numbers, and hyphens only." Line 27 is the coordinate in
   `docs/specification.mdx@69ef37e9`, which I re-fetched (same time, line 27 matches). This is the
   same class as the S001 anchor defect this round superseded. The entry's other cites (spec.md:63, 64, 66, 67, 101, 237) all match.
2. *Negative claims without sweeps (Q14).* Entry lines 11-12 say "every 'not stated' cell names
   the search that found nothing (Q14)". Three cells carry no sweep: third person / skills-ref,
   body length / skills-ref, and body length / packager. The claims themselves are true. I swept the
   re-fetched `validator.py@69ef37e9` (sha256 `b5ee3d85…`, matching the entry) and
   `quick_validate.py@dbd4588` (sha256 `67cf5703…`, matching) with
   `grep -n -i -E 'third|person|500|lines|reserved|claude|anthropic'`. The only hits are the 500-character
   `compatibility` limits (validator.py:12, qv.py:91-92), with no third-person, reserved-word or line rule.
   So this is a form defect, not false content.
3. *Admission not recorded.* The round-48 `## Gate` lists source rows and search-log exclusions, but has
   no entry for knowledge candidates considered, admitted or rejected (LEARNING § Files: "candidates
   considered, admitted, rejected … spot-check result").
4. *Provenance incomplete (contract rule 2 permits a logged change).* S012's `used-by` is still `SKILL.md` only
   at `d28b16b`, while the entry's `source:` cites S012. This does not break rule 4.

**Quality evidence.**
- Supersession is byte-verified: the spec, skills-ref and packager hashes I re-fetched equal the entry's pins.
- The entry's `recheck:` runs: `curl -fsSL https://agentskills.io/specification.md | grep -c 'Must match the parent directory name'` returns 1, exit 0.
- Q-a: `rg -n -i 'round-48|round 48|qualif' corpus/knowledge/harness-independent-round37.md corpus/knowledge/harness-independent-round41-census.md`
  returns 0 hits. Both bodies still assert 24/24 (for example round37.md:177 "**24/24 over the landed scope**"). The
  round-48 stale mark lives only in the README index rows.
- Q-b: `A24UnreadableRoot.md` reports that C2 exits 2 (a caught `SUBSTRATE` error) on an unreadable
  `--oc-config/skills`, where base exited 0. The lesson records this as an open question, not a fix. I did not re-run it.
- C2 semantics versus the round's own source. I re-opened
  `raw.githubusercontent.com/anomalyco/opencode/v1.19.3/packages/opencode/src/skill/index.ts`
  (08:52:24Z, sha256 `91dce57f…`). Line 24 reads `const OPENCODE_SKILL_PATTERN = "{skill,skills}/**/SKILL.md"`, and
  line 134 reads `state.skills[md.data.name] = {`, so identity is the frontmatter name.
  The C2 arm asserts "a nested skill is not a name (direct children only)" and counts
  `entry.name`, which is the directory name. The depth row discloses "Not claimed: recursive … parity (upstream
  S016 is recursive) … frontmatter-name identity". It still calls the closer-to-upstream enumeration a "recursive
  mutant", so the next round's parity fix must break this arm and the 115 floor.
  The live row is unchanged because both roots are absent on this host. The gain is synthetic: ruler 5 → 0.
- No-harm runs, in private clones under `/fast/scratch/hyaku/kotoba-r48-a2/seats2/A34TrendVerdicts/`:
  - At `84b9c9b`: `check_assertion_floors.py` exit 0 (harness_independent 115/115); `verify_harness_independent.py --self-test` exit 0, "0 failure(s) over 115 assertions"; `verify_corpus_integrity.py --json` exit 0; `verify_corpus_independent.py` exit 0.
  - `verify_skill_checklist.py` exits 1 at `75f671b`, `d1ae458`, `887b6af` and `84b9c9b` alike: name equals directory, plus `../` sibling-lane cites that only exist on the host.
  - In a host-shaped clone (`.ufo` symlinked), the governance dead-cite set is identical at `75f671b` and `84b9c9b` (LOG.md lines 311, 824, 1203; evaluated 872 → 901). The 29 new LOG and SCORECARD citations add no dead cite.
  - At `d28b16b`: checklist `--self-test` exit 0, "0 failure(s) over 1845 assertions"; floors exit 0.

**Discernment evidence.**
- The round-47 spot-check (`lessons/round-47-verifier-spotcheck.md:49-52, 62-74`) agreed with the S012 admit and the pointer reject, and routed items 1-5.
- At `d28b16b`, every new criterion has a lesson row: Q20 ← M24, Q21 ← M26, Q22 ← M28, Q23 ← M24 (supersedes Q20). Item 5 takes no criterion, with a stated reason. No criterion lacks a lesson, so the harmed clause is not met.
- D1: Q23 requires "a located quote from that authority plus the sweep". The same commit (`d28b16b`) edited the entry and left both E1.1 and E1.2 in place.
- D2: the lesson labels wave 2 "lane-dispatched — not a non-author spot-check". Round 48's own admit and reject decisions (at least 1 of each) are unsampled, and the Gate has no `rejected` row. Rejects exist only as 5 search-log exclusions.

## Impacted axes

Freshness (C1's entry and its label), depth (C2 semantics and A24), calibration (Q23 not applied to the round's own admit), and records (SCORECARD freshness row "knowledge on uncovered ground" under the freshness axis).

## Smallest safe correction (lane to apply; I edited nothing)

1. Entry line 58: change `spec.md:27` to `spec.md:30`, or cite `specification.mdx:27 @69ef37e9`. Append the three sweeps above,
   or narrow line 12's "every" claim. After this, E1 and D1 no longer hold.
2. Round-48 `## Gate`: add the knowledge admission line (the entry admitted, the criteria checked) and name an
   admit and a reject for the non-author spot-check to sample, for example S017 and the excluded opencode docs.
3. Change S012 `used-by` from `SKILL.md` to `SKILL.md, corpus/knowledge/frontmatter-rule-authorities-round48.md`, logged
   old → new.
4. Append a dated round-48 qualification line inside `harness-independent-round37.md` and
   `harness-independent-round41-census.md` (closes Q-a).
5. Report C2 as improved-bounded and synthetic-only, and name the A24 exit-2 tradeoff. If the judge upholds Q-b
   under Q18, quality is a trade, not improved.

Tools installed or updated: none. Fetched code was hashed and grepped, never executed.
