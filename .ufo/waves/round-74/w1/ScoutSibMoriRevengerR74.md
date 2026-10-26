# ScoutSibMoriRevengerR74 — C2 sibling re-read: mori, revenger

**Verdict: both proposed classifications equal r49 (`none` → `none` for mori and for revenger). No classification differs from r49.** What changed for revenger is the derived cells, not the class: r49 pinned `876630db` with no skill file; at the frozen head `6da884c6` a `SKILL.md` exists (added by `cab8085`, round 64), so the row's skill-file cell becomes `SKILL.md`, names-kotoba `no`, arbitration `no`. mori's row is unchanged in every cell (new pin, same bytes of scope).

Only committed bytes at the heads in `.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv` were read (`git -C … show/grep/diff <head40>`); no working tree, no sibling edit. Heads/blobs re-checked: mori `24ebc799…` SKILL `a32d8013…` PROVINCE `b8480258…`; revenger `6da884c6…` SKILL `082af19c…` PROVINCE `797f67fe…` — equal to the freeze file (`git rev-parse <head>:SKILL.md <head>:PROVINCE.md`). Both pins are ancestors of the head (`merge-base --is-ancestor` → anc; mori 312 commits, revenger 66).

Mechanical verification: the base `check_sibling_census.py` (copy of `git show 1e03d19:verifiers/check_sibling_census.py`, sha256 `2f9d8a88b1d3dd8562455006d5ea89ec02546a1ecb9d023f327d88e5502eedc7`, equal to the committed blob's hash) run on a 2-row census against a scratch 20-symlink fleet → `rows 2 verified 2` for the two proposed rows (only the 18 unsurveyed lanes fail the lane-set check). Controls: the r49-shaped revenger row (NONE / no SKILL.md) → 3 FAILs, `rows 2 verified 1`; quote at wrong line `PROVINCE.md:9` → `quote not found … (+/-2 lines)`; mori as `adjacent` still `verified 2` (the checker cannot reject a wrong class — Bound). Scratch dir deleted.

## Findings (command → observed)

1. mori: `git -C mori-shokunin grep -n -w -i kotoba 24ebc799… -- SKILL.md PROVINCE.md | wc -l` → `0`; whole tree minus LOG.md/.ufo → 38 lines, 25 files, all roster ids or ledger citations (e.g. `tools/mori-census.sh:527` `roster_ids=(… kotoba …)`, `corpus/lessons/round-39.md:82`). No split, no SKILL.md/prompt claim. Same count `rc=1` at the r49 pin.
2. mori: description line 3 is byte-identical at `28b79d3d` and `24ebc799` (both printed with `sed -n 3p`); `git diff --shortstat 28b79d3d 24ebc799 -- SKILL.md PROVINCE.md` → `2 files changed, 462 insertions(+), 15 deletions(-)` — gate rows and OOM/PSI/job-runway Core notes, none about kotoba's ground.
3. revenger: `git cat-file -e 876630db:SKILL.md` → `fatal: path 'SKILL.md' exists on disk, but not in '876630db…'`; `git log --diff-filter=A -- SKILL.md` → `cab8085 2026-10-24 … round-64: C1 admission … SKILL.md landed`; `git diff --shortstat 876630db 6da884c6 -- SKILL.md PROVINCE.md` → `1 file changed, 618 insertions(+)`, and `git diff … -- PROVINCE.md` is empty (PROVINCE.md byte-identical).
4. revenger: new SKILL.md has no frontmatter (`grep -n -E '^---$|^description:'` → no output), so the checker derives description `''` (names kotoba `no`, arbitration `no`). Its scope (SKILL.md:10-20) is its own entries, verifiers and frozen probe; sole `instruction file` hit is `SKILL.md:3` "applied to this instruction file". Whole-word kotoba: 0 in SKILL.md/PROVINCE.md; 1 in tree at `corpus/lessons/round-69.md:217` (citation: misroot report, no split).
5. Open (reported, not ruled): kaidoku/revenger overlap stays an operator question; neither revenger file states it (sweep for `kaidoku` in SKILL.md/PROVINCE.md → no hit). A frontmatter-less SKILL.md means the base checker's `--skill`/description machinery sees an empty description for revenger; if kotoba later wants an arbitration clause for revenger, there is no description to carry it. Unobserved: the elided middle of mori's `PROVINCE.md` Adjacent appendix was read via grep sweeps and the Adjacent table (lines 59-68), not every appended line.

Extra key `clause_decided` in each JSON gives the deciding rule clause; `quote` is from `PROVINCE.md:3` (quote-equal after dropping the `**Domain:** ` prefix for mori; dropped nothing after the quoted words — the line wraps).

## mori.json
```json
{
  "lane": "mori",
  "head40": "24ebc7991e9081348d1aa4f558f994b1f4feccab",
  "r49_classification": "none",
  "r49_pin": "28b79d3d1b76824f0c825aabe6cb6c5dc49961bf",
  "proposed_classification": "none",
  "clause_decided": "`none` arm of the r49 rule (neither contested nor adjacent). contested needs a sibling claim on writing/auditing other lanes' SKILL.md, prompts or AGENTS.md-class files; adjacent needs a stated split of one artifact/function/trigger area with kotoba. Deciding sibling sentence (PROVINCE.md:12-13): 'Refuses: dispatch and orchestration mechanism (→ kumitate); OS package, systemd unit, driver/firmware and boot state (→ tsukuroi)' — it names kumitate/tsukuroi/kama/kagi and never kotoba; whole-word kotoba count in SKILL.md+PROVINCE.md at the head is 0.",
  "changed": "no (none -> none, same arbitration cell 'yes: kama, kumitate, tsukuroi'). The pin moved 312 commits (28b79d3d -> 24ebc799; `git diff --shortstat` 2 files changed, 462 insertions(+), 15 deletions(-)), but the frontmatter description is byte-identical at both commits (line 3 printed equal) and the added bytes are gate rows, Core/Frontier notes and Round-N appends about OOM/PSI/job-runway probes, none naming kotoba or a SKILL.md/prompt-craft claim.",
  "skill_file": "SKILL.md",
  "quote": "fleet & host observability (森) — whether the fleet, its waves and",
  "quote_path_line": "PROVINCE.md:3",
  "kotoba_mentions": [],
  "boundary": "mori owns read-only fleet and host liveness, wave-settlement and kill/OOM reporting (PROVINCE.md:3-10) and routes dispatch, OS state and endpoint health to kumitate, tsukuroi and kama (SKILL.md:3); it states no split with kotoba.",
  "sweep": [
    "git -C mori-shokunin grep -n -w -i kotoba 24ebc799… -- SKILL.md PROVINCE.md | wc -l -> 0",
    "git -C mori-shokunin grep -n -w -i kotoba 24ebc799… -- . ':!LOG.md' ':!.ufo' | wc -l -> 38 lines in 25 files; every hit is a lane-roster id or ledger citation (corpus/evidence/*.log SURFACE lane.kotoba rows, corpus/knowledge/roster-truth-r12.md:9-10 roster id lists, observability-surfaces-r2.md:78,299, progressing-weak-r2.md:144-165, tools/mori-census.sh:527 roster_ids array, corpus/lessons/round-39.md:82 'do not import kotoba's `--no-merges`'); none states a split or a claim over SKILL.md/prompt craft",
    "git -C mori-shokunin grep -n -i -E 'SKILL\\.md|AGENTS\\.md|prompt|frontmatter|description' 24ebc799… -- SKILL.md PROVINCE.md -> every hit is mori's own SKILL.md (gate rows, own-file pointers) or the kagi row's own `SKILL.md:374-393`; no hit about another lane's SKILL.md or prompt text",
    "git -C mori-shokunin grep -n -E '[a-z]+-shokunin/SKILL\\.md' 24ebc799… -- SKILL.md PROVINCE.md corpus/README.md -> no output",
    "git -C mori-shokunin show 28b79d3d…:SKILL.md | sed -n 3p  vs  git -C mori-shokunin show 24ebc799…:SKILL.md | sed -n 3p -> identical description line (Anti-trigger: NOT dispatch/orchestration (kumitate), NOT OS package/systemd/driver state (tsukuroi), NOT endpoint health (kama))",
    "git -C mori-shokunin grep -c -w -i kotoba 28b79d3d… -- SKILL.md PROVINCE.md -> no output, rc 1 at the r49 pin as well",
    "base checker (1e03d19 copy, sha256 2f9d8a88…eedc7, identical to `git show 1e03d19:verifiers/check_sibling_census.py | sha256sum`) on the proposed row with a 20-symlink scratch fleet -> row verified (`rows 2 verified 2` for the mori+revenger pair; only the 18 unsurveyed lanes fail the lane-set check)",
    "kotoba side: kotoba's own description (master:SKILL.md frontmatter) names kagi, kake, kasegi, kengaku, kumitate, chousa, kama, tameshi, kotodama and neither mori nor revenger (sed -n 1,25p of master:SKILL.md)"
  ]
}
```

## revenger.json
```json
{
  "lane": "revenger",
  "head40": "6da884c6708fa25a7af013b6fc6802492e3264fa",
  "r49_classification": "none",
  "r49_pin": "876630dbb4d630e016d7d8c32a19ea04c646cbae",
  "proposed_classification": "none",
  "clause_decided": "`none` arm of the r49 rule. SKILL.md now exists (lines 1-20 scope: 'process instruction ... governs three narrow acts in this lane': entries under corpus/knowledge/, its own corpus/ verifier family, its frozen counting probe) — a claim over its own files only, so not contested (no other lane's SKILL.md/prompt/AGENTS.md); no kotoba-side or revenger-side split sentence exists (whole-word kotoba count in SKILL.md+PROVINCE.md = 0; kotoba's description names neither). Deciding PROVINCE.md:19-23 'Refuses: ... harness/evidence auditing (harness-integrity, gate-evidence, rlm-dispatch); game mechanics verification (game-dev-2d); narrative canon (lore).' names no kotoba.",
  "changed": "classification no (none -> none); skill-file/cell derivation YES: r49 row said NONE / 'no SKILL.md' / 'no SKILL.md', but the pin moved 66 commits and SKILL.md was added by cab8085 (git log --diff-filter=A, 2026-10-24, round-64); `git diff --shortstat 876630db 6da884c6 -- SKILL.md PROVINCE.md` -> 1 file changed, 618 insertions(+) (PROVINCE.md byte-identical: diff empty). The new SKILL.md has no frontmatter, so the checker derives description '' -> names kotoba 'no', arbitration 'no'. The r49-shaped cells (NONE) now FAIL the base checker (3 failures, control below).",
  "skill_file": "SKILL.md",
  "quote": "Owns: reverse engineering of shipped artifacts — native binaries, managed",
  "quote_path_line": "PROVINCE.md:3",
  "kotoba_mentions": [],
  "boundary": "revenger owns reverse engineering of shipped artifacts (PROVINCE.md:3-7) and, since SKILL.md landed (git log --diff-filter=A, cab8085), a checklist over its own saved-ledger verifiers (SKILL.md:10-20); neither file names kotoba.",
  "sweep": [
    "git -C revenger-shokunin grep -n -w -i kotoba 6da884c6… -- SKILL.md PROVINCE.md | wc -l -> 0",
    "git -C revenger-shokunin grep -n -w -i kotoba 6da884c6… -- . ':!LOG.md' ':!.ufo' -> 1 hit: corpus/lessons/round-69.md:217 '.ufo/waves/round-24/w2/RevUnlandedResolution.md sit at the fleet root — kotoba's and tabi's seats' (kind citation: a misroot report, no split, no SKILL.md claim)",
    "git -C revenger-shokunin grep -n -i -E 'instruction file|other lanes|sibling lane|another lane|\\.\\./[a-z0-9-]+-shokunin' 6da884c6… -- SKILL.md PROVINCE.md corpus/README.md -> one hit, SKILL.md:3 'applied to this instruction file' (its own file)",
    "git -C revenger-shokunin grep -n -i -E 'SKILL\\.md|AGENTS\\.md|prompt|frontmatter|sibling|kagi|kake|kama|kumitate|kengaku|tameshi|chousa|kaidoku|mori|tsukuroi' 6da884c6… -- SKILL.md PROVINCE.md -> PROVINCE.md:10 (REA skill source path), :28 'sibling repositories remain read-only', SKILL.md:19 'their siblings' (its own verifiers), :295 self_assessment_check input list; no other lane named, kaidoku overlap not stated in either file",
    "git -C revenger-shokunin show 6da884c6…:SKILL.md | grep -n -E '^---$|^description:' -> no output (no frontmatter, no description)",
    "git -C revenger-shokunin cat-file -e 876630db…:SKILL.md -> fatal: path 'SKILL.md' exists on disk, but not in '876630db…' (confirms r49 'no SKILL.md')",
    "base checker (1e03d19 copy) on the proposed row (SKILL.md | none | no | no, PROVINCE.md:3) -> verified; on the r49-shaped row (NONE | no SKILL.md | no SKILL.md) -> 'FAIL ... SKILL.md exists at the pin but the skill cell says NONE' + names-kotoba + arbitration mismatches, `rows 2 verified 1`",
    "quote-line control: same row with PROVINCE.md:9 -> 'quote not found at PROVINCE.md:9 (+/-2 lines)'",
    "mori control: mori row with `adjacent` instead of `none` still passes the base checker (rows 2 verified 2): the classification is a judgement the checker cannot reject, as the plan's Bound says"
  ]
}
```
