# A09ClaimSizingC1 — critic, claim C1 sizing and axis (round 48, attempt 2, falsify wave)

Seat: `KotobaR48.A09ClaimSizingC1`, read-only on the lane. Writing gates ran only in the private clone
`/fast/scratch/hyaku/kotoba-r48-a2/seats2/A09ClaimSizingC1/clone`. Tools installed or updated: none.

## Verdict

**DEFECT, medium.** The count is CONFIRMED as declared (34 → 35, and the 35th file is the entry). The
axis label is defective: 34 → 35 is the expansion observable, and AXES.md maps expansion to coverage
and adjacency, not to freshness. The counter also cannot fail on an empty file. The round does contain
real freshness work (four stale rows superseded, `SKILL.md:151` corrected, a live recheck that still
returns 1), but C1's declared before → after does not measure it.
C1 does qualify as a learning (expansion) claim under the session bar. Second finding, **LOW**: the
round left two stale `used-by` cells (S001, S003) that the contract allowed it to fix.

## Evidence (lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, commands exit 0 unless stated)

1. Count at each revision, `git ls-tree -r --name-only <rev> corpus/knowledge | grep -c '\.md$'`:
   `75f671b` → 34; `887b6af5…` → 35; `84b9c9b` (records) → 35.
2. `git diff --stat 75f671b 887b6af5… -- corpus/knowledge` → one file,
   `frontmatter-rule-authorities-round48.md`, 104 insertions, exit 0. `--name-status` → `A` only.
   No other knowledge file changed. `887b6af..84b9c9b` changes nothing under `corpus/knowledge`.
3. The entry's `source:` line cites S017, S018, S019, S020, S021, all added this round, and all
   `status=mined` in `corpus/SOURCES.md`. So the plan's second clause ("citing at least one SOURCES row
   added this round") holds, but only by inspection: the declared command does not test it.
4. Live recheck, 2026-10-22T08:50:37Z UTC: `curl -fsSL https://agentskills.io/specification.md` exit 0,
   7,608 B, sha256 `9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16`. That matches
   the entry's byte count and hash prefix. `grep -c 'Must match the parent directory name'` → 1.
   Located quote (spec.md:67): "Must match the parent directory name".

## Counterexample 1 — the counter is blind to content and to axis (medium)

- Private clone at `75f671b`: commit an empty `corpus/knowledge/zz-empty.md` → the declared command
  prints **35**. An empty entry meets the declared after-value exactly.
- Same clone at `887b6af`: rename an older entry from `.md` to `.markdown` → **34**. Renames and
  extensions move the count without any knowledge change.
- `../AXES.md` § The learning path: "Expansion ↔ `coverage` + `adjacency`; quality ↔ `depth` +
  `freshness` + `operability`". `../LEARNING.md` defines the expansion observable as "admitted
  `knowledge/` entries on ground the coverage map did not hold". An entry count is that observable.
  So the declared number measures coverage (expansion), not freshness.
- AXES.md defines freshness as "skill claims re-verified against live surfaces; stale items flagged or
  fixed". The landed bytes do support a freshness count; the claim just never uses it:
  `grep -c 'supersedes S0' corpus/SOURCES.md` is 0 at `75f671b` and 4 at `887b6af` (S018 supersedes
  S001, S019 supersedes S003, S020 supersedes S010, S021 supersedes S013). `SKILL.md` S-refs moved
  from S001/S003 to S018/S019 (now 0 hits for S001/S003). Line 151's "stricter" sentence was corrected.
- Impacted axes: freshness (false provenance — the axis credit rests on a number that does not
  measure it); coverage (an expansion move is credited to another axis instead of being declared).
  The SCORECARD round-48 freshness row (before "34 knowledge entries…", after "35 entries @ `887b6af`")
  repeats the mismatch, but its prose also lists the real freshness evidence.
- Fixable defect, not a tradeoff: no axis is harmed. The fix is to re-measure or re-label.

## Is freshness the honest axis?

Partly. The content is freshness work. Six authorities were opened on 2026-10-22, and S018 is
byte-identical to the round-47 fetch. S019 has copy edits only, with every rule line unchanged. The
S012 pin is still `main` HEAD. Four stale or mis-credited rows were superseded and `SKILL.md:151` was
fixed. The measurement is not freshness. The axis choice (freshness at 8, tied with adjacency 8.0 for
the lowest score) is defensible. Only the declared instrument is wrong for it.

## Is it a learning claim (admitted knowledge on uncovered ground)?

Yes, on the expansion trend, with a qualification:
- It is admitted knowledge, and `source:` cites mined rows (S017–S021). Its coverage-map row is
  `corpus/README.md:66`.
- The ground is uncovered in `corpus/knowledge/`. At the base, `git grep -i -E
  'agentskills|skills-ref|quick_validate'` over `corpus/knowledge` finds nothing (exit 1).
  `frontmatter-trigger-surface.md` covers trigger craft, not validity rules.
- It is not uncovered in the lane overall. At the base, `SKILL.md:151` already stated per-authority
  rules. The lesson discloses this (round-48 M25, from `build/C2UncoveredSweep.md`), and the plan's
  name-only sweep missed it. The new ground beyond line 151 is real: the skills-ref column, the
  NFKC/Unicode charset contradiction, the three angle-bracket regimes, the observed lane-checker
  column, and the round-47 counterexamples actually run.
- Note: under AXES.md this learning credit belongs to coverage/expansion. Freshness credit has to come
  from the re-verification and supersession evidence, measured as such.

## Finding 2 — stale `used-by` cells left in place (low)

- S001 and S003 are `status=mined` with `used-by=SKILL.md`. At `887b6af`, `SKILL.md` cites neither
  (0 hits; it now cites S018 and S019). The new rows S018 and S019 list only the entry in `used-by`.
- Round-48 lesson lines 25–26: "No existing row's `status`, `recheck` or `used-by` changed; S001,
  S003 … stay as written (contract rule 2)". But `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md` rule 2
  says: "Only `status`, `recheck` and `used-by` change in place, and each change is logged old→new".
  Rule 2 is exactly what permits the fix; it does not forbid it. The fleet copy and all four
  scratch copies of the contract have the same sha256 prefix, `6c674a2281af`, so no other version
  reads differently.
- The contract's census line ("mined rows whose used-by paths do not exist") prints nothing at both
  revisions, because the path exists. Only the claim it carries is stale. This is a stale item the
  freshness round itself created and neither fixed nor flagged as stale.

## Smallest safe corrections

1. Keep C1 on freshness, but declare a measure that is actually freshness, from landed bytes:
   `grep -c 'supersedes S0' corpus/SOURCES.md` 0 → 4 (`75f671b` → `887b6af`), plus the recheck line
   (count 1, fails closed at 0). Report 34 → 35 separately as the expansion (learning) trend
   observable, not as the freshness number.
2. If 34 → 35 stays a counted claim anywhere, make it able to fail on an empty or uncited file, e.g.
   `git show <rev>:corpus/knowledge/frontmatter-rule-authorities-round48.md | head -1 | grep -cE 'S0(1[6-9]|2[01])'`
   → must be ≥ 1.
3. Update the S001 and S003 `used-by` cells (and the S018/S019 `used-by` cells to include `SKILL.md`,
   to match the S001 convention), logging old → new in `corpus/lessons/round-48.md` per rule 2.
   Correct the lesson's misreading of rule 2.

## Checks not run

- I did not re-run the lane checker, packager or skills-ref fixtures behind the table cells (other
  seats own those columns). I did not re-fetch S017, S019, S021 or S012.
