# Falsify — C1 census row `game-dev-3d` (seat RowGameDev3d, 2026-10-22)

HOLDS — applies to census row `game-dev-3d` (sibling-overlap-census-round49.md:66) and
PROVINCE.md § Adjacent row (PROVINCE.md:40): classification `none`, both mechanical columns,
branch/commit/skill-file cells, scope quote, and every factual statement in the boundary note
survive attack. One minor wording imprecision recorded; it does not flip any cell.

## Findings

**F1 (minor, wording): the boundary note "its frontmatter audits cover only its own and vendored
skill files" is imprecise about what the sibling's committed audit reads.**
`reports/round-104/skill/bleed.md` at the pin is titled "frontmatter accuracy, cross-domain bleed,
PROVINCE consistency" (subject: its own `SKILL.md`), but its §1.5 "the Rank convention" runs
`for f in /home/vgpnk/Projects/shokunin/*-shokunin/SKILL.md; do … grep -c 'Rank: shonen' $f; done`
(bleed.md:129-130, repeated :524-525), reading all 18 lane SKILL.md files — `kotoba-shokunin 1`
(bleed.md:139). The match in kotoba's file is body prose, `Rank: shonen.` at kotoba
`SKILL.md:45` (frontmatter is lines 1-16 at c48793d), so the sweep reads sibling body bytes, not
frontmatter keys. Why it does not flip anything: bleed.md is under `reports/`, which the census
classification rule does not count as a scope surface (rule names "SKILL.md, PROVINCE.md, corpus
files"; census Limits concedes wave reports can be missed); the loop asserts no craft claim — it
explicitly records "a majority convention rather than a rule… a consistency note, not a defect"
(bleed.md:151-154); and the note stays true for the audit *subjects* (its own SKILL.md per
bleed.md:4-5; the 3 vendored upstream SKILL.md per `reports/round-101/probes/skill-frontmatter.md:1-4`).

**F2 (observation, guard gap): the machine guard cannot catch F1-class prose drift.**
`python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md
--province PROVINCE.md` → `rows 20 verified 20` / `province rows 20 matched 20`, rc 0 at judged
bytes c48793d (run in private clone /fast/scratch/hyaku/kotoba-r49/falsify/RowGameDev3d/lane).
It checks census↔PROVINCE row agreement and pinned-byte quotes; boundary-note prose like the
"only its own and vendored" clause is unguarded. No action required this round; noted for the
guard's future scope.

**F3 (attack failed, recorded): corpus files the build seat's top-level sweep did not enumerate
contain no kotoba claim or kotoba split.** The build seat's craft-pattern sweep covered 8
top-level files; I swept `corpus/` (excluding vendored `unreal-mcp/upstream` and `fixtures/`)
at the pin for `SKILL\.md|frontmatter|AGENTS\.md|dispatch prompt|prompt craft|trigger` and
separately `arbitrat|sibling|craft`. Every hit is own-file receipt (`corpus/knowledge/engines.md:157`,
`godot-floor-angle-threshold.md:38`, lessons), chousa deference (`corpus/QUALITY.md:5`,
`corpus/SOURCES.md:3`), or a sibling↔sibling split that does not involve kotoba
(`corpus/SOURCES.md:3`: 3D/2D registry split with game-dev-2d; `corpus/README.md:170-175`
adjacency table: game-dev-2d, mado, kumitate, kengaku, revenger — no kotoba row, no
skill/prompt-craft row). Under the rule (`adjacent` needs a split *with kotoba*) these leave `none`.

**F4 (attack failed): the two kotoba-mentioning files in the whole tree are deference, not claims.**
Tree-wide `git grep -l -i kotoba <pin>` → exactly `reports/round-101/r101-scout-roster.md` and
`reports/round-104/skill/bleed.md`. The roster's kotoba row (row 2 of its rejected-fit table,
~line 106) *rejects a demand away from kotoba* by quoting kotoba's own anti-trigger
(`SKILL.md:8-9`) and body refusal (`SKILL.md:447-448`) — the opposite of absorbing kotoba ground.
bleed.md's kotoba line is the F1 convention count. Neither is a scope surface; neither claims or
splits anything.

## Verified cells (each with the command that fixes it)

- **Commit/branch:** `git -C game-dev-3d-shokunin rev-parse --verify 89dd182b…^{commit}` rc 0;
  `git log -1 --format='%H %d'` → `89dd182b… (HEAD -> main, origin/main, origin/HEAD)`;
  `git branch -a --contains` → `main` only. Census cell `main` right; build report's "master does
  not exist" right.
- **Skill file cell:** root `SKILL.md` exists at pin (frontmatter `name: game-dev-3d-shokunin`,
  25,541 B, sha256 `f52b988afaa03bf4…`); 7 `SKILL.md` paths tree-wide (root + 3 vendored + 3
  scratch copies), matching the build report.
- **Scope quote:** `git show <pin>:PROVINCE.md | head -12` — the quote is verbatim (whitespace
  collapsed) across lines 3-5, starting at `PROVINCE.md:3` as the row records; guard rc 0.
- **names kotoba = no; arbitration = yes: game-dev-2d, revenger** — re-derived from
  `git show <pin>:SKILL.md | sed -n 3p` with
  `grep -oiE '\b(kotoba|audio|chousa|game-dev-2d|…|tsukuroi)\b' | sort | uniq -c` →
  `1 game-dev-2d`, `1 revenger`, no third token, case-insensitive whole token. Exact cell match.
- **classification none:** whole-tree keyword sweep
  (`git grep -inE 'SKILL\.md|frontmatter|trigger|AGENTS\.md|dispatch|prompt' <pin> -- .`):
  scope-surface hits are own-file only (sibling `SKILL.md:3` description, `:49` row-D
  "structural description"; `README.md:12`; `PROVINCE.md` 0 kotoba, `grep -ci kotoba` → 0;
  sibling `## Adjacent` at PROVINCE.md:72-78 names exactly game-dev-2d, mado, kumitate, kengaku,
  revenger — build report's five-lane claim correct). No tools/ or verifiers/ dir at the pin
  (`ls-tree --name-only`: AGENTS.md LOG.md PROVINCE.md README.md SCORECARD.md SHONEN.md SKILL.md
  considerthese corpus reports). Under § Classification rule: no contested claim (nothing audits
  other lanes' SKILL.md/prompt/AGENTS.md craft as a scope surface), no kotoba split → `none`.
- **Boundary note facts:** "3D game production" = PROVINCE.md:3 verbatim; frontmatter-audit claim
  holds for audit subjects (own: bleed.md:4-5; vendored: skill-frontmatter.md:1-4), see F1 for the
  imprecision. The note cites no line numbers; nothing else in it to check.
- **Build report numbers reproduce:** 23,564 tracked files (`ls-tree -r | wc -l`); SKILL.md 25,541 B
  / PROVINCE.md 7,467 B / AGENTS.md 3,925 B; SKILL.md sha256 `f52b988a…`; kotoba-file count 2; its
  roster characterization (row 2, rejection quoting kotoba's boundary) verified.

## Residual risk and verification gaps

- Classification rests on keyword sweeps over committed bytes; a claim phrased with none of the
  swept tokens and no lane name would be missed — the same limit the census records in Limits.
- No `lsp` server applies (read-only Markdown/byte checks on a sibling repo); all evidence is
  git-object reads, grep used for counts and token sets only.
- The 3 `reports/round-104/gate/scratch/c85a816/**/SKILL.md` copies were not hash-compared to the
  vendored files byte-for-byte (build seat's size match accepted; they are scratch copies in
  `reports/`, not scope surfaces, so load-bearing for nothing here).
- `considerthese/2026-10-20.md` craft-pattern count 0 taken from `grep -c` (rc 1 = zero matches),
  not a full read; the file carries no kotoba or craft tokens.

## Evidence index (all read-only; sibling repo read-only git; lane untouched except this file)

1. Pin identity/branch — rev-parse/log/branch-contains, rc 0, `main` only.
2. Guard — clone at c48793d, `python3 -B verifiers/check_sibling_census.py … --province
   PROVINCE.md` → `rows 20 verified 20` / `province rows 20 matched 20`, rc 0.
3. Description token sweep — `sed -n 3p` + 21-lane alternation, rc 0, {game-dev-2d, revenger}.
4. Tree sweeps — kotoba `-l` (2 files), craft keywords per-file counts, corpus-only passes, rc 0/1
   as noted; sibling PROVINCE heading list (`## Adjacent` at :72), bullets :74-78.
5. kotoba `SKILL.md` at c48793d — `grep -n Rank` → `45:Rank: shonen.`; frontmatter `^---$` at 1,16.
6. Tool installs/upgrades: none performed; none needed.
