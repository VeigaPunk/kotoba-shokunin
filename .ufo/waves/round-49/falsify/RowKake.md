# RowKake: falsify report (round 49, C1 census row `kake`)

Verdict: FAILS on the classification. The census row `kake` says `none`. Under the census's own rule (either side's committed scope surfaces state a split, which makes the row `adjacent`), it should say `adjacent`. Applies to census row `kake` in `corpus/knowledge/sibling-overlap-census-round49.md` and to `PROVINCE.md:43`, judged at kotoba c48793dbe5eb30cd661f42ecad7399ae94e3d7ad. HOLDS for the pin, the branch cell (as ancestry only), the scope quote, and both mechanical columns.

Attacked: the kake census row and its PROVINCE.md row (pin, branch, quote, classification, mechanical columns, boundary note); the C1 content guard as far as it covers this row; `.ufo/waves/round-49/build/CensusKake.md`.

## Findings (by severity)

### F1 — High: classification `none` breaks the stated rule
Rule (census § Classification rule): "`adjacent`: either side's committed scope surfaces (SKILL.md, PROVINCE.md, corpus files) state a split of one artifact, function or trigger area between the sibling and kotoba." `none` is "neither of the above".

- Kotoba's committed SKILL.md, lines 10-12 (E6): "Sibling boundary: the five `*-shokunin` domain skills (kagi, kake, kasegi, kengaku, kumitate) own their own SKILL.md content — this skill audits and reports; fixes route to the owning lane." That is a published split of one artifact (kake's SKILL.md content) between kake (owner) and kotoba (auditor). It sits on the "either side" surface the rule names.
- The census already counts kotoba-side text as adjacency evidence. `chousa` is adjacent on kotoba's own PROVINCE row (`corpus/QUALITY.md`), and `kagi` on kotoba's PROVINCE.md:41. So SKILL.md:10-12 counts for kake.
- More kotoba-side evidence of the same split, none cited by the census: `corpus/knowledge/sibling-citation-routing-round16.md:101` (`r16adj-route-kake`, "prepared; owner decision pending"); `corpus/knowledge/sibling-citation-routing-round21.md:22` ("route r16adj-route-kake still unacknowledged"); `corpus/knowledge/sibling-description-rewrites-round8.md:186-216` (§3.2: kotoba's replacement description for kake's frontmatter, with its own "Sibling boundary" sentence). Exit codes of these reads were not captured; the lines were read in full (E11, E12).
- The `none` sweep was one-sided. CensusKake.md Evidence sweeps kake's files only (`git show <c>:SKILL.md …`, `grep -n kake <lane>/PROVINCE.md`). The rule says "either side"; the build seat did not sweep kotoba's committed surfaces for kake.
- Same defect on a sibling row, same basis: `kasegi` is `none`, yet SKILL.md:10-12 names it in the same sentence. I did not sweep kasegi's own surfaces.
- Consequence (hand arithmetic on the census § Counts, `7 adjacent, 13 none, 0 contested`; the census awk was not re-run): kake alone gives 8 adjacent and 12 none; kake and kasegi together give 9 and 11.
- Counter-reading: SKILL.md:10-12 is a generic boundary sentence. Rebuttal: the census treats "X owns Y" statements as splits (kengaku and kumitate are adjacent on sibling-side "kotoba owns …" text; chousa on kotoba-side text). SKILL.md:10-12 has the same form and names an artifact. If the census meant to exclude it, the rule text must change first; the row stays `adjacent` under the text as written.

### F2 — Medium: the content guard cannot fail on F1, and does not check the mechanical columns
- Guard run in a scratch clone at c48793db: `rows 20 verified 20`, `province rows 20 matched 20`, exit 0 (E10).
- Classification is checked only for membership in (contested, adjacent, none) (`verifiers/check_sibling_census.py:393-396`) and for equality with the PROVINCE row (`:532-536`). No rule is applied.
- `names kotoba` and `arbitration` are read only for the non-empty check (`:383`). The guard never re-derives them from a sibling file (its only sibling read is `git_show` for the quote, `:425`). The census says these two columns are not judgment; the guard does not enforce that.
- The guard does check the quote at `path:line` ±2 (`locate_quote`, `LINE_TOLERANCE = 2`, `:103`, `:434`). Scope-quote location is machine-checked.

### F3 — Medium: the PROVINCE.md boundary note for kake is incomplete and uncited
Row (PROVINCE.md:43): `| kake | none | e73d48bbf20759fc7758afaebf841fa02e5cfbbf | web properties and publishing; no claim on kotoba ground |`

Statement by statement:
- (a) "web properties and publishing": HOLDS. kake PROVINCE.md:3 reads "web properties & publishing" (E3).
- (b) "no claim on kotoba ground": HOLDS for kake's own pinned bytes. `git grep -c -i kotoba` at e73d48b excluding `.ufo` (E13) lists only LOG.md (2 hits, relays of a kotoba r14 complaint) and `corpus/lessons/round-5-aggregator-mirror-pathless-cli-invocation.md` (2 hits; the build seat reads them as a filer note at line 4). kake's SKILL.md, PROVINCE.md, README.md, AGENTS.md, SHONEN.md and SCORECARD.md contain no `kotoba`. But the note omits the split kotoba itself states (F1), so a reader of PROVINCE.md alone sees no boundary.
- (c) "cited line": none. The row has no `path:line`. Other rows carry one: kagi `corpus/README.md:97`, kengaku `SKILL.md:3`, kumitate `PROVINCE.md:27`, kama `corpus/knowledge/cross-lane-scope.md:29`. The guard checks this row only against the census, so the note cannot be checked from PROVINCE.md alone.

### F4 — Low: the pin is an ancestor of master, not master's tip
- Pin is an ancestor of master (E2). `git branch --contains` lists `master` and a detached HEAD (exit not captured).
- master = 7697990cbca20291f3b0367b8ff4220e93b38b03 (E9), eight commits after the pin (E8), including `36b6b21` (round-28) and `7697990` (round-29).
- Blob changes since the pin: SKILL.md `7df5219…` → `4ed26d6…`; PROVINCE.md `a222e4e…` → `51b6919…`. README.md (`fa0c1b3…`) and AGENTS.md (`d982324…`) unchanged.
- The tip PROVINCE.md diff touches lines 26-30 only (base-path tooling entry). Neither tip file mentions kotoba (grep of the tip SKILL.md and PROVINCE.md copies, E14). The F1 defect is therefore not a tip-only effect.
- The branch cell `master` is right as ancestry, but a reader takes it as the current tip. The census "Pins move" note covers this. Low.

### F5 — Low: build seat report is stale on the PROVINCE row
- CensusKake.md Finding 7 says kotoba's PROVINCE.md has "zero kake mentions" (`grep -n kake PROVINCE.md` exit 1). At judged c48793db the row is at PROVINCE.md:43 (E7). The build seat read an earlier checkout. Its proposed `no overlap observed` line already exists in another form. The defect is the classification (F1), not a missing row.

## Verified (holds)
1. Commit and branch cell. `rev-parse --verify -q e73d…^{commit}` exit 0 (E1). Ancestor of master, exit 0 (E2). Commit 2026-10-22 06:41:20 -0300, "round-28: C1 follow-up …".
2. Scope quote. `grep -nF` of the census quote in `git show e73d…:PROVINCE.md` → `3:**Domain:** web properties & publishing — scopes ds4cc.com, kimi.page/pro mirrors, Pages deploys`, exit 0 (E3). Exactly line 3, no trailing space (`cat -A`). SKILL.md:3 matches exactly as well.
3. Contested (none found). Sibling-side sweeps:
   - `scripts/`: only `freshness-sweep.mjs` matches the skill-craft term set (18 lines, mostly `trigger` in its own comments, e.g. :302). `citing_set.py` "sibling" means its own selftest runner. No script reads another lane's SKILL.md, AGENTS.md or prompts.
   - AGENTS.md (5 lines): "Work only within this repo and its PROVINCE.md scope."
   - SHONEN.md:5: kake's own promotion checklist ("SKILL.md contains real decision tables, error patterns, checklists, cited sources"). Self-scoped; consistent with kotoba's SKILL.md:10-12.
   - SKILL.md:371 "wz0/wz1 mission prompts": a path listing of ufofsdbeta's own `.ufo`.
   - `corpus/` and `plans/` dispatch hits: kake's own wave runs (`corpus/README.md:93,101`; `plans/wwkd-round-20-citation-locality.md:5-42`).
   Conclusion: no `contested` claim. The `contested` half of the `none` call holds; the `adjacent` half does not (F1).
4. Mechanical columns, re-derived from `git show e73d…:SKILL.md` line 3:
   - names kotoba: E4, exit 1, 0 hits → `no`. Holds.
   - arbitration: E5, exit 1, 0 hits over the 20 sibling names (whole token, case-insensitive) → `no`. Holds.
   - Sibling set: 21 `*-shokunin` directories (E-count below) = 20 siblings + kotoba. Holds.

## Evidence (commands and exit codes verbatim; Q = the census quote)
- E1 `git -C kake rev-parse --verify -q "e73d…^{commit}"` → exit 0
- E2 `git -C kake merge-base --is-ancestor e73d… master` → exit 0
- E3 `git -C kake show e73d…:PROVINCE.md | grep -nF -- "$Q"` → exit 0 (line 3)
- E4 `printf '%s\n' "$DESC" | grep -ioEw kotoba` → exit 1 (no output)
- E5 `printf '%s\n' "$DESC" | grep -ioEw -e audio -e chousa -e game-dev-2d -e game-dev-3d -e kagi -e kaidoku -e kake -e kama -e kasegi -e kengaku -e kotodama -e kumitate -e lore -e mado -e mori -e revenger -e souji -e tabi -e tameshi -e tsukuroi` → exit 1 (no output)
- E6 `git -C kotoba show c48793db…:SKILL.md | sed -n 10,12p` → exit 0 (the split sentence, lines 10-12)
- E7 `git -C kotoba show c48793db…:PROVINCE.md | grep -n '^| kake |'` → exit 0, line 43
- E8 `git -C kake log --oneline e73d…..master | wc -l` → 8, exit 0
- E9 `git -C kake rev-parse master` → 7697990cbca20291f3b0367b8ff4220e93b38b03, exit 0
- E10 guard in scratch clone `/fast/scratch/hyaku/kotoba-r49/falsify/RowKake/kotoba` (checkout c48793db): `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` → `rows 20 verified 20`, `province rows 20 matched 20`, exit 0
- E11 `git -C kotoba show c48793db…:corpus/knowledge/sibling-description-rewrites-round8.md | sed -n 186,216p` (read; exit not captured)
- E12 `git -C kotoba grep -n kake c48793db… -- corpus/knowledge/sibling-citation-routing-round16.md corpus/knowledge/sibling-citation-routing-round21.md` → lines 101 and 22 (exit not captured)
- E13 `git -C kake grep -c -i kotoba e73d… -- . ':!.ufo'` → LOG.md:2, corpus/lessons/round-5-aggregator-mirror-pathless-cli-invocation.md:2 (exit not captured)
- E14 kake tip copies (`git show master:SKILL.md`, `git show master:PROVINCE.md`): `grep -niE 'kotoba|AGENTS\.md|triage|sibling|prompt|frontmatter|description'` on the tip SKILL.md printed no kotoba line; the pin-vs-tip PROVINCE diff (shell `diff`) changes lines 26-30 only, and none of those lines contains kotoba (exit not captured).
- E-count `ls -d /home/vgpnk/Projects/shokunin/*-shokunin | wc -l` → 21 (exit not captured)
- Guard source reads: `grep -nE 'values\[' verifiers/check_sibling_census.py` → `:383` (non-empty check), `:393-396`, `:404`, `:415` (exit 0); no comparison of `names kotoba` or `arbitration` cells to a sibling file.

Tooling: nothing installed or upgraded. Git calls on sibling and lane repos were read-only (rev-parse, show, log, grep, cat-file, merge-base, branch --contains). The one `git clone` read the lane; the `git checkout` ran inside my scratch clone only. Nothing in the lane, the fleet root, or any sibling repo was written. Pin and tip extracts were moved into `/fast/scratch/hyaku/kotoba-r49/falsify/RowKake/`.

## Residual risk and verification gaps
- Not swept: kasegi's own surfaces; every other census row (other seats own them); the mutation arms of the guard.
- Not run: the census awk counts, and any lane-side check. Counts above are hand arithmetic and are labelled as such.
- If the census authors meant "either side" to exclude a generic boundary sentence like SKILL.md:10-12, F1 becomes a rule-text defect; the kake row still needs the rule amended before `none` can stand.
- kake's master is eight commits ahead of the pin and its SKILL.md and PROVINCE.md changed. The row is correct for its pin only.
- No web sources were opened. No procedure in this report depends on one.
