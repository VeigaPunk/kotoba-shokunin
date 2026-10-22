ROW | kake | master | e73d48bbf20759fc7758afaebf841fa02e5cfbbf | SKILL.md | none | no | no | PROVINCE.md:3 | "**Domain:** web properties & publishing — scopes ds4cc.com, kimi.page/pro mirrors, Pages deploys"

# kake census — kotoba round 49, C1 adjacency

Scout: `KotobaR49.CensusKake`. Surface: `/home/vgpnk/Projects/shokunin/kake-shokunin`, read-only
(`git show`/`ls-tree`/`rev-parse` only). Classification: **none**. Description names kotoba: **no**
(0 hits). Arbitration clause naming a kotoba-core sibling: **no**. No tools installed or upgraded.

## Findings

1. **Pin, and the repo moved under me.** First `rev-parse master` gave
   `8ecbefe31b81462239c572fbe23d21404442a177` (exit 0); later reads gave
   `5a83d13` then `e73d48bbf20759fc7758afaebf841fa02e5cfbbf`. kake is mid-round-28 integration
   (`log 8ecbefe..e73d48b` = two commits: `5a83d13`, `e73d48b`). Final pin recorded above is
   `e73d48b`, stable across three consecutive reads (`rev-parse master` = `rev-parse HEAD`,
   `symbolic-ref -q HEAD` exit 1 → detached HEAD at the same commit). The move does **not** affect
   this census: the four prose blobs are byte-identical at `8ecbefe` and `e73d48b`
   (`rev-parse <c>:SKILL.md …` identical, `diff --stat 8ecbefe e73d48b -- SKILL.md PROVINCE.md
   README.md AGENTS.md` exit 0, empty). Working tree is dirty (`status --porcelain`: ` M
   corpus/QUALITY.md`, ` M corpus/lessons/round-28.md`, many `??` under `.ufo/waves/round-2{6,8}/`).

2. **Skill file inventory.** Root `SKILL.md` is the only skill file
   (`ls-tree -r --name-only <c> | grep -E '^(skills?/[^/]+/)?SKILL\.md$'` → `SKILL.md`, exit 0;
   1 match in 1,708 tracked files). No `skills/` tree. Frontmatter (SKILL.md:1-4):
   `name: kake-shokunin`, `description: Domain specialist — web properties & publishing — scopes
   ds4cc.com, kimi.page/pro mirrors, Pages deploys. Rank: shonen.`

3. **What kake owns.** Web properties and publishing: Pages fronts, kimi.page/pro mirrors,
   sitemaps, publish gating. Its eight scripts are domain instruments —
   `accessibility_packet.py`, `canonical_audit.py`, `citing_set.py`, `corpus-contract.mjs`,
   `freshness-sweep.mjs`, `live_snapshot.py`, `probe-delta.mjs`, `receipt_replay.py` — none parses
   SKILL.md frontmatter, decision-table anatomy, AGENTS.md or dispatch prompts. `corpus-contract.mjs`
   is a structural census of kake's own `corpus/` entries; `citing_set.py` parses citation ranges in
   kake's own knowledge files. `corpus/QUALITY.md` (324 lines) is a publishing-evidence bar
   ("Citation-local absence", "Replayable claim", "Platform mechanism"), not a skill-craft bar.

4. **kotoba-core contact is by instance, not by claim.** kake uses decision tables for its own gate
   rows (SKILL.md:387 `corpus-contract`, :411 `canonical-audit`, :555 `accessibility-packet`) and
   `README.md:12` describes `SKILL.md` as "the distilled expertise: decision tables, error
   patterns, checklists". That is consumption of the form; no file claims authority to write or
   audit those surfaces for another lane. `frontmatter` occurs 5× in the whole tree, 0× outside
   `.ufo/` (all five in `.ufo` fixtures/wave notes).

5. **kotoba named?** 0 in `SKILL.md`, `PROVINCE.md`, `README.md`, `AGENTS.md` (also 0 in `SHONEN.md`,
   `SCORECARD.md`). Tree-wide 7 hits in 3 files, all incidental: `LOG.md:190` and `:284` relay
   kotoba r14 as the *filer* of a `probe-delta.mjs` complaint; `corpus/lessons/round-5-aggregator-
   mirror-pathless-cli-invocation.md:4` reads "**Filed by:** kotoba round-5 report … §'Cross-domain
   observations to relay'"; a `.ufo` sweep line. Direction of flow is kotoba → kake evidence, which
   matches kotoba's report-don't-absorb refusal; no craft delegation either way.

6. **Arbitration.** The frontmatter description names no sibling at all, so it cannot carry an
   arbitration rule. `PROVINCE.md` § Adjacent (:30-39) does arbitrate four *domain* siblings —
   `tabi` (browser/client-side crawler vs publisher-side placement), `chousa` (research method vs
   domain findings), `kagi` (credentials vs no secret values), `kama` (local serving vs remote
   properties) — none touching kotoba's core. `arbitrat*` appears twice tree-wide, both inside kake
   `.ufo` round-22 wave notes about its own decision, not about lanes.

7. **C1 consequence (for the census owner, not fixed here).** kotoba's own `PROVINCE.md` § Adjacent
   has **zero** `kake` mentions (`grep -n kake PROVINCE.md` exit 1). It names 10 of the 20 sibling
   lanes; `kake` is among the 10 unnamed (`audio game-dev-2d game-dev-3d kagi kaidoku kake lore
   souji tabi tsukuroi`). So the C1 claim "PROVINCE.md § Adjacent naming all 20 sibling lanes" does
   not hold at this checkout for this row. Because the classification here is `none`, the honest
   repair is a `no overlap observed` line for kake (kotoba's existing phrasing for kotodama/mado/
   revenger/mori/kama), not a shared-boundary clause.

8. **Confidence:** high for the pinned blobs. Remaining unknown: whether kake's in-flight round-28
   wave lands prose changes to these four files; re-check the row against the next `master` tip.

## Evidence

```
git -C <R> rev-parse master                      # 8ecbefe… then e73d48b… ; final: e73d48bbf20759fc7758afaebf841fa02e5cfbbf  exit 0
git -C <R> rev-parse HEAD master                 # both e73d48bbf20759fc7758afaebf841fa02e5cfbbf  exit 0
git -C <R> symbolic-ref -q HEAD                  # no output, exit 1 (detached)
git -C <R> ls-tree --name-only <c>               # .gitignore .ufo AGENTS.md LOG.md PROVINCE.md README.md SCORECARD.md SHONEN.md SKILL.md considerthese corpus plans scripts
git -C <R> ls-tree -r --name-only <c> | grep -E '^(skills?/[^/]+/)?SKILL\.md$'   # SKILL.md  exit 0
git -C <R> ls-tree -r --name-only <c> | wc -l    # 1708
git -C <R> show <c>:SKILL.md | wc -lc            # 697 77943
git -C <R> show <c>:PROVINCE.md | wc -lc         # 80 5060
git -C <R> show <c>:README.md | wc -l            # 14
git -C <R> rev-parse <c>:SKILL.md <c>:PROVINCE.md <c>:README.md <c>:AGENTS.md
                                                 # 7df5219403aa43ed7f170b8bff0590ab375bf368 a222e4ecda638c8316521db60853218db062696b fa0c1b318ec85a2b51cd61a7ae342d3ed6e980b1 d9823243a1f80f51580377ab13a67db7e581afda
git -C <R> diff --stat 8ecbefe 8ecbefe…e73d48b -- SKILL.md PROVINCE.md README.md AGENTS.md  # empty, exit 0
git -C <R> log --oneline 8ecbefe..e73d48b        # 5a83d13, e73d48b
```

Required `none` sweep (pinned prose surfaces; 30 matching lines, 31 occurrences, exit 0):

```
git -C <R> show <c>:SKILL.md <c>:PROVINCE.md <c>:README.md <c>:AGENTS.md \
  | grep -cE 'SKILL\.md|prompt|AGENTS\.md|frontmatter|trigger|description|kotoba'
                                                 # 30  exit 0
  … | grep -oE '<same pattern>' | sort | uniq -c  # SKILL.md 24, description 4, trigger 2, prompt 1, kotoba 0, AGENTS.md 0, frontmatter 0
```

Every hit is self-reference or domain vocabulary, none a craft claim:
`SKILL.md` 24× = kake citing its own file (22 in SKILL.md, `Surface: …/kake-shokunin/SKILL.md` and
`… SKILL.md:16` re-census lines; 1 in PROVINCE.md:43 `Present:` list; 1 in README.md:12);
`description` 4× = frontmatter key (SKILL.md:3),
`fire-description timestamp` (:328), `612B SPA-shell description` (:471), `description is not the
total` (:659); `trigger` 2× = `Pages workflows triggered on push` (:422) and `push trigger` (:453);
`prompt` 1× = a path listing `wz0/wz1 mission prompts` (:371).

```
git -C <R> grep -lE 'kotoba' <c> -- .             # .ufo/waves/round-27/misroot-sweep.txt, LOG.md, corpus/lessons/round-5-aggregator-mirror-pathless-cli-invocation.md
git -C <R> show <c>:SKILL.md | grep -c kotoba     # 0
git -C <R> show <c>:PROVINCE.md | grep -c kotoba  # 0
git -C <R> show <c>:README.md | grep -c kotoba    # 0
git -C <R> show <c>:AGENTS.md | grep -c kotoba    # 0
git -C <R> grep -lE 'frontmatter' <c> -- . ':!.ufo'   # no output, exit 1
grep -n 'kake' <lane>/PROVINCE.md                 # no output, exit 1 (kotoba names no kake row)
sed -n '29,34p' <lane>/PROVINCE.md | grep -oE '\b(chousa|…|kama|kake)\b' | sort -u | wc -l   # 10
ls -d /home/vgpnk/Projects/shokunin/*-shokunin | wc -l                                        # 21 (20 siblings + kotoba)
comm -23 /tmp/all.txt /tmp/named.txt                                                          # unnamed: audio game-dev-2d game-dev-3d kagi kaidoku kake lore souji tabi tsukuroi
```

**Scope quote (SKILL.md:3, verbatim):** `description: Domain specialist — web properties &
publishing — scopes ds4cc.com, kimi.page/pro mirrors, Pages deploys. Rank: shonen.`
**Second located quote (PROVINCE.md:3, verbatim):** `**Domain:** web properties & publishing —
scopes ds4cc.com, kimi.page/pro mirrors, Pages deploys`
**Nearest arbitration quote (PROVINCE.md:32-33, line wrap joined with `⏎`):**
``tabi` drives browsers and owns client-side crawler discipline; kake owns⏎ publisher-side placement
(robots/sitemap at the host it serves).`
