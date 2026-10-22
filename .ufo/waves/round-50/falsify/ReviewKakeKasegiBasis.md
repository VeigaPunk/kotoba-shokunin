# Review: kake and kasegi basis (round 50 falsify, adjacency)

FAILS — applies to the D4 qualifier in `SCORECARD.md` (adjacency row, judged line 34) and to the census basis label `both` for kake and kasegi (census lines 284-289). The verbatim quote HOLDS. The `adjacent` class for kake and kasegi HOLDS-BOUNDED: it stands on kotoba's own description alone (F4).

Judged bytes: kotoba `956ee1676e4c18480bce8ac3993541462be76e11`. Pins: kake `e73d48bb…`, kasegi `1fafde8f…`. Base: `f30464660c675d1c1e2851a3bf0366a3aaffe5a8`. Read-only (`git show`, `git grep`, `git log`, `merge-base`). No writes outside this report. No subagents.

## Answers

1. **Is the quote verbatim?** Yes. The census string "Aggregator-owned file; the owning lane corrects `SKILL.md`." occurs exactly once in each lesson, on line 5 (the `Mirrored by` line). Line 4 is `Filed by: kotoba round-5 report`. The census's gloss is not verbatim: it says the lessons "state the same split", but the quoted sentence names no kotoba side (F1). (E1)
2. **Is an aggregator-authored file in the sibling's corpus a "sibling-stated" split?** No. Corpus files are scope surfaces by location, but the census's own test asks who states the split, and this text is the aggregator's routing record (F1).
3. **Is the D4 qualifier accurate?** No. Part of its history is right. "Found only in round 50" is false for the files, it states no current basis, it splices into the round-49 counter command, and it omits tameshi (F2).

## Findings

**F1 (high). The mirror lines are not a sibling-stated split.**
- The file declares itself aggregator work. Line 5 reads "Mirrored by: aggregator round-5 (main-repo lane, `m_qwen`) … Aggregator-owned file; the owning lane corrects `SKILL.md`." The fleet protocol treats such mirrors as routing records: `PROTOCOL.md:243-246` (fleet working copy, read 2026-10-22; the 2026-09-28 text was not checked) says the aggregator "mirrors each routed defect into the owning repo's `corpus/lessons/`" and that "routing is integrator work and must exist in an artifact" (E12).
- kake: the commit that added the file, `1395393` (an ancestor of the pin, E2), is titled "corpus: round-5 aggregator audit lesson (independent re-verification, L1-adjudicated)". By its own title it is an aggregator commit (E3).
- kasegi: the file came in with a kasegi commit titled "round-9" (ancestor, E2; six files, E4). A lane commit does not make an aggregator-owned sentence the lane's own statement. The text still says "Aggregator-owned".
- No sibling text states a kotoba split. Whole-tree `grep -i kotoba` at each pin (E5, E6): kake's hits are LOG.md, one `.ufo/` file, and the mirror. kasegi's are LOG.md, one `.ufo/rounds/` file, one survival-check row naming a kotoba file (`corpus/instruments/citation-survival.tsv:1025`), and the mirror. Neither pin's `SKILL.md` nor `PROVINCE.md` names kotoba. LOG.md is not a listed scope surface; I did not read those hits (see gaps).
- Line 4 is provenance only. Round-49 seats read it the same way: `falsify/RowKake.md:31` ("the build seat reads them as a filer note at line 4"); `falsify/RowKasegi.md:28` ("Not a split").
- The census's test is "the sibling's own scope surfaces" (census lines 256-257), with basis values sibling, kotoba and both. The round-50 critic proposed a fourth value, `third-party` (`CriticPrecedence.md` §5 and §6.1). An aggregator-authored file is third-party under that scheme. The census did not adopt the value and still labels kake and kasegi `both` (F3).
- Conclusion: the sibling-side arm is empty for kake and kasegi. The correct basis label is `kotoba`.

**F2 (high). The D4 qualifier (SCORECARD judged line 34) is inaccurate.**
- (a) "Found only in round 50" is false for the files. Kotoba cited them in round 22 (`.ufo/round-22/scouts/A2.md:59`, `A3.md:39`), round 23 (`.ufo/round-23/scouts/A3.md:43`, `A4.md:56`) and round 49 (`.ufo/waves/round-49/build/CensusKake.md:105`, `CensusKasegi.md:43`; `falsify/CriticC1Landed.md:23`; `RowKake.md:31,72`; `RowKasegi.md:28,65`) (E9). Round-49 `falsify/CriticC1Landed.md:21-23` even counted them as corroboration ("Both sides corroborate the split"). What is new in round 50 is the line-5 sentence. "Owning lane corrects" is absent from the base tree (E10, rc 1) and first appears at the judged commit.
- (b) It states no current basis, and the records disagree. SCORECARD: kake and kasegi "were classed `adjacent` from kotoba's own description, with an aggregator-mirrored lesson … found only in round 50." The lesson's D4 entry (read from the working copy) says the SCORECARD now says "because of kotoba's own description, not their own bytes". The SCORECARD does not say "not their own bytes". Census lines 284-289 say "Basis both". On F1 the census is wrong, and the lesson's reading is closer.
- (c) It splices into the round-49 record. The D4 text sits inside the round-49 counter command, between `PROVINCE.md` and `| grep -cE '^\| (<20 lane names>) …` (E8). The recorded round-49 counter can no longer be read as written. The round's D1 rule (append; rewrite nothing) is the pattern to follow.
- (d) It is incomplete. The census falsify note (census lines 147-149) says tameshi's round-49 basis was kotoba's base `PROVINCE.md` line, and `CriticPrecedence.md` F2 says that line named only tameshi's ground. The qualifier names only kake and kasegi. The D3 section re-based tameshi to its own `PROVINCE.md:14-17`, so the current row stands; the history in the qualifier does not.
- What holds: "'from their own bytes' overstated" for kake and kasegi (the round-49 row says "from their own bytes", E8); "classed `adjacent` from kotoba's own description" (census lines 143-149); "no precedence rule until round 50" (census D3 section).

**F3 (medium). The round-50 critic's premise is half true.** `CriticPrecedence.md` F3 says "the round-49 seats missed it." They read the files and quoted line 4 (F2a). They did not quote line 5. The census then adopted F3's "basis both" without F3's own value scheme (F1). F3 also counts "aggregator-authored lessons" toward the sibling side, which its §5 scheme labels third-party.

**F4 (residual risk; the class holds).** The kake and kasegi `adjacent` rows now rest on one kotoba-side sentence. The critic calls that sentence universal (`CriticPrecedence.md` §5, counterexample 1: true of all 17 lanes with a skill file). The census adopts "a split stated only by kotoba may make a no-claim row `adjacent`", but not the critic's added requirement that the element be specific to that lane. As written, the class holds. If the stricter test is adopted, kake and kasegi need another basis or move.

**F5 (checked; holds).** The judged frontmatter `description` value is 1,008 characters (E7), matching the SCORECARD's "1,008". Not part of D4.

## Recommended corrections (not run)
- Census: change kake and kasegi basis from `both` to `kotoba`, and say the mirror lines are aggregator routing records, not sibling statements.
- SCORECARD: append a corrected D4 line that names the basis `kotoba`, drops "found only in round 50", names tameshi's round-49 basis, and leaves the round-49 counter text as recorded.
- Lesson D4 entry: align it with the corrected SCORECARD text.

## Evidence (exit codes verbatim)
- E1 `git -C kake-shokunin show e73d48bb…:corpus/lessons/round-5-aggregator-mirror-pathless-cli-invocation.md` rc 0 (2,480 B). Kasegi `git -C kasegi-shokunin show 1fafde8f…:corpus/lessons/round-5-aggregator-mirror-ambiguous-citation-base.md` rc 0 (2,760 B). Census `git -C kotoba-shokunin show 956ee16…:corpus/knowledge/sibling-overlap-census-round49.md` rc 0 (28,348 B). Python exact-substring test: census holds the quoted string, with quotes, once; kake quote lines [5], total 1; kasegi quote lines [5], total 1.
- E2 `git -C kake-shokunin merge-base --is-ancestor 1395393 e73d48bb…` rc 0; `git -C kasegi-shokunin merge-base --is-ancestor c80c2a1 1fafde8f…` rc 0.
- E3 `git -C kake-shokunin show --stat 1395393`: two files, `round-5-aggregator-audit.md` (+76) and the mirror (+26).
- E4 `git -C kasegi-shokunin show --stat c80c2a1`: six files, including `SKILL.md` (48 lines), `corpus/README.md` (9), `corpus/lessons/round-9.md` (63) and the mirror (27).
- E5 `git -C kake-shokunin grep -n -i kotoba e73d48bb…` rc 0: `LOG.md:190`, `LOG.md:284`, `.ufo/waves/round-27/misroot-sweep.txt:12`, mirror `:4`, `:6`.
- E6 `git -C kasegi-shokunin grep -n -i kotoba 1fafde8f…` rc 0: `LOG.md:400`, `LOG.md:501`, `.ufo/rounds/round-21/frozen-head-citation-survival.tsv:1041`, `corpus/instruments/citation-survival.tsv:1025`, mirror `:4`, `:6`, `:18`.
- E7 Frontmatter `description` value at `956ee16` (Python; folded lines joined with spaces): 1,008 characters.
- E8 `git -C kotoba-shokunin show f30464660c…:SCORECARD.md` rc 0 (128,553 B); `show 956ee16…:SCORECARD.md` rc 0. Adjacency row: base 4,727 characters, judged 6,138. Two inserts: the round-50 prefix, and the D4 qualifier inside the round-49 awk text. (A first attempt with a mistyped base SHA gave rc 128; re-run with the correct SHA.)
- E9 `git -C kotoba-shokunin grep -n round-5-aggregator-mirror f30464660c…` rc 0, 11 hits (listed in F2a).
- E10 `git -C kotoba-shokunin grep -c -F 'owning lane corrects' f30464660c…` rc 1 (no hits). At `956ee16` the same command gives rc 0, hits in `CriticPrecedence.md` and the census.
- E11 Base round-49 adjacency text: "all 20 sibling lanes classified at pinned sibling commits from their own bytes".
- E12 Fleet `PROTOCOL.md` lines 243-246 (grep, working copy, 2026-10-22).
- E13 Census lines 47-48, 143-149, 256-260, 284-289, 294-295; `CriticC1Landed.md:21-23`; `CriticPrecedence.md` F2, F3, §5, §6.1 (working tree, `.ufo/waves/round-50/build/`).

## Gaps (not checked)
- Kake `LOG.md:190, 284` and kasegi `LOG.md:400, 501`: LOG.md is not a listed scope surface. I did not read them.
- The lesson and plan were read from the working copy, not `956ee16`.
- Fleet `PROTOCOL.md` was read at the working copy, not the 2026-09-28 version.
- The census guard was not run. It does not check the basis column (census lines 294-295).

Tooling: nothing installed or upgraded.
