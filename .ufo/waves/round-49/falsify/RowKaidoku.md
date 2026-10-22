# Falsify: C1 census row `kaidoku` — seat KotobaR49.RowKaidoku

**HOLDS** — the kaidoku census row (`corpus/knowledge/sibling-overlap-census-round49.md:68`), its
PROVINCE.md § Adjacent row (line 42), and the build report `CensusKaidoku.md` survived every attack
tried. No defect found in scope. Leaf seat; no dispatch; read-only except this file. No tools
installed (none needed).

## Attack 1 — commit exists and branch cell
- `git -C kaidoku-shokunin rev-parse 08c7a7299ed61c3fdc30ddb0adfe4e812d5eac76^{commit}` → the
  object, exit 0. Exists.
- Branch cell `main` is right: `git branch -a --contains <pin>` lists `main` (plus detached-HEAD
  marker); `git rev-parse refs/heads/main` = `dc31f9c441528cfff1070c0574eea9669fd47e64` and
  `git merge-base --is-ancestor <pin> refs/heads/main` → exit 0 ("ancestor: yes"). At census time
  the pin was main's tip (build report: `for-each-ref refs/heads` → `main 08c7a729` only).
- Post-census drift is real but pre-declared: main advanced to `dc31f9c4` (round-25 EVM work); of
  the top-level scope surfaces only `SCORECARD.md` changed pin→tip (`git diff --name-only <pin>
  refs/heads/main -- SKILL.md PROVINCE.md README.md AGENTS.md MINT.md SHONEN.md SCORECARD.md` →
  `SCORECARD.md`). The census Limits section declares pin-anchored reads, and the guard re-reads
  pinned bytes. Not a defect.

## Attack 2 — scope quote verbatim at SKILL.md:3
- `git show <pin>:SKILL.md` line 3 sha256 `d6fd799dbb7bdc43e404ef7e5f709b930fe932c4e9c21f8f8c155df653b04b4d`
  — identical to the build seat's recorded hash.
- `grep -c 'Domain specialist — reverse engineering of shipped artifacts with REA on this Linux host'`
  over line 3 → 1. Verbatim, at the stated line (±0, tolerance 2). ✓

## Attack 3 — classification `none` under § Classification rule
Rule: contested = claims part of kotoba's core ("writing or auditing other lanes' SKILL.md, prompts
or AGENTS.md-class files, or the instruments over them"); adjacent = either side's committed scope
surfaces (SKILL.md, PROVINCE.md, corpus files) state a split between sibling and kotoba.
- kaidoku side, repo-wide at the pin, excluding `.ufo`:
  `git grep -inE 'kotoba|skill[- ]?craft|prompt[- ]?craft|AGENTS\.md' <pin> -- . ':!.ufo'` → exactly
  3 hits: `EXAMPLE.kama.md:32,51` (a verbatim evidence copy of kama's MINT.md table — a kama→kotoba
  row, not a kaidoku claim, and it affirms kotoba owns "prompt & skill craft") and
  `corpus/lessons/round-13.md:11` (fleet-root AGENTS.md protocol lesson, no ownership claim).
  `prompt`, `AGENTS.md`, `frontmatter`, `kotoba` have 0 matches in the six governance files
  (independently reproduced from the build seat's counts).
- Sibling tokens in kaidoku SKILL.md + PROVINCE.md at the pin: only `revenger` ×8
  (`git grep -ioE '\b(<20 lane names)\b' <pin> -- SKILL.md PROVINCE.md | uniq -c`), all recording
  the kaidoku/revenger arbitration as open — a sibling-to-sibling clause, not a kotoba clause.
- Nearest approach, read and rejected: `corpus/knowledge/2026-10-13-rea-skill-contract.md` curates
  RE-domain candidates of the **host** skill `~/.agents/skills/reverse-engineer-anything/`
  (SKILL.md v37). A hostile reading calls this "auditing a SKILL.md"; the rule's own words limit
  contested to **other lanes'** SKILL.md/prompts/AGENTS.md. REA is a host package, not a lane; the
  verdicts are RE-content admissions ("suggested: admit — top-level scope gate…"), not skill craft
  (no trigger/frontmatter/anatomy claims). Correctly `none` under the stated rule.
- kotoba side ("either side"): base `PROVINCE.md:34` at `a5adc146` assigns "shipped-artifact RE" to
  **revenger** and never names kaidoku; `corpus/knowledge/sibling-citation-routing-round21.md:52`
  credits kaidoku `citation-drift-probe.py` as prior art (a credit, not a split statement); current
  kotoba bytes name kaidoku only in the census entry and the two § Adjacent rows.
- kaidoku's own committed overlap census (`.ufo/waves/round-14/w1/SiblingOverlap.md:21`) says
  "Zero overlap. … kotoba owns meta-skill craft" — the sibling's own verdict agrees with `none`.

## Attack 4 — mechanical columns re-derived two ways
From `git show <pin>:SKILL.md` line 3 only: (a) whitespace tokenization with punctuation stripped,
lowercased; (b) `grep -oiw` word-boundary on the raw line. For `kotoba` and all 20 sibling lane
names (audio … tsukuroi): **0 matches each, both methods**. Row cells `no | no` are correct. The
description's only boundary clause is the generic anti-trigger ("ordinary source repositories…");
`Rank: shonen` and `REA` are not lane names.

## Attack 5 — PROVINCE.md § Adjacent boundary note (line 42), fact by fact
- "reverse engineering of shipped artifacts with REA" ✓ — kaidoku SKILL.md:3 and § Domain at pin.
- "its domain overlaps revenger's" ✓ — revenger PROVINCE.md:3 at its pin `876630db`: "Owns: reverse
  engineering of shipped artifacts — native binaries, managed…" (same claimed domain, verbatim stem).
- "open arbitration between those two" ✓ — kaidoku SKILL.md:677 "The kaidoku/revenger
  dynamic-analysis boundary remains an open L0 question."; kaidoku PROVINCE.md:240 ("kaidoku/revenger
  arbitration is still open"), :272–273, :303 — all at the pin.
- "reported to the integrator" ✓ — census finding 4 records the kaidoku/revenger item for the
  integrator; the PROVINCE row reports without resolving, matching the entry's own practice.
- Commit and classification cells match the census row exactly; the committed guard joins them.

## Guard run (exercises this row)
`python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md
--province PROVINCE.md` → `rows 20 verified 20` / `province rows 20 matched 20`, **exit 0**.

## Residual risk / verification gaps
1. The pin has advanced (`main` → `dc31f9c4`); the row's truth is pinned to `08c7a729` by design.
   If the round is re-read at a moving tip, SCORECARD.md drift exists but SKILL.md/PROVINCE.md do
   not (checked).
2. kaidoku's 30 `.ufo/waves/**` files named `SKILL.md` (RE attack fixtures) were not semantically
   audited; the classification rule's surfaces do not include wave fixtures, and the census Limits
   section declares this limit. 20 committed `.ufo` files mention kotoba — the sampled ones are
   session transcripts and the round-14 "Zero overlap" verdict; none asserts skill-craft ownership.
3. `none` is a judgment; the only judgment-adjacent fact (REA skill contract) is resolved by the
   rule's "other lanes'" wording, recorded here so an appeals reader sees the hinge.

## Evidence index (commands → exit codes)
- rev-parse pin → exit 0; branch -a --contains → main; merge-base --is-ancestor → 0.
- quote grep -c → 1; line-3 sha256 matches build report.
- non-.ufo kotoba/craft grep → 3 lines, exit 0; sibling-token uniq → `8 revenger` only.
- token recount (two methods) → all 0; guard → exit 0 (`rows 20 verified 20`).
- All reads via `git -C /home/vgpnk/Projects/shokunin/kaidoku-shokunin show|grep|ls-tree` (read-only);
  no jj commands; no pacman; no writes outside this report and /tmp scratch.
