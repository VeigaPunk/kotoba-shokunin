ROW | kasegi | master | 1fafde8f11454f3b0b98ab7f2b2e640aaf7f399a | SKILL.md | none | no | no | PROVINCE.md:3 | "bounty & security research — scopes ~/Projects/bounties, program rules, claim packages"

# Round 49 C1 — sibling-overlap census: kasegi-shokunin

Date 2026-10-22. Seat KotobaR49.CensusKasegi (leaf, no dispatch). kotoba-shokunin read-only except
this file; kasegi-shokunin read-only throughout via `git -C … show/ls-tree/rev-parse/grep/log`.
No jj, no git write, no pacman/uv install, no web fetch this session. Repo HEAD is detached at
`1fafde8`; `rev-parse master` succeeded with the same 40-hex, so the row's branch is `master`.

## Findings

1. **Classification `none`.** At the pin, kasegi's owned surface is bounty and security research
   content (program rules, scopes, claim packages); nothing in its pinned docs claims skill,
   prompt or always-on craft, and its only kotoba references are citations of kotoba as auditor
   (finding 5). Sweep over the three pinned docs for the plan pattern: **5 lines, all in
   `SKILL.md`, none an ownership claim** (see Evidence). Case-insensitive sweep is also 5.
2. **Not `contested`.** No cross-lane writing or auditing of `SKILL.md` / prompts / `AGENTS.md`.
   Its `AGENTS.md` is five self-scoped lines (`AGENTS.md:3`, "Work only within this repo and its
   PROVINCE.md scope"). Its lane-local instruments — `corpus/instruments/density.py`,
   `anchorcheck.py`, `resolve.py`, and the round-21 frozen skill guard — measure its own
   `SKILL.md` citation survival and block density as its `depth:density` / `depth:verifiability`
   axes; they publish no skill-craft rule and verify no other lane. Craft-ownership phrase sweep
   over `corpus/` (`frontmatter|prompt craft|skill craft|trigger fidelity|dispatch prompt|
   AGENTS\.md-class|always-on`) returns **1 line**, an unrelated "always-on alarm" sentence in
   `corpus/lessons/round-11.md:33`.
3. **Not `adjacent` at this pin — and kotoba's existing clause is unsourced.**
   `PROVINCE.md` § Adjacent (lines 40–47) names chousa, kagi, kake, kengaku only; **kotoba is
   absent from every revision of that file** (`git log -S kotoba -- PROVINCE.md` → no commits,
   exit 0). The phrase `prompt[- ]injection` has **zero matches in the whole kasegi tree**
   (`git grep -qiE` → exit 1), so kotoba's current § Adjacent line "kasegi — security research
   incl. prompt-injection exploits" is not attested by the sibling. Its source,
   kotoba `.ufo/round-46/scouts/w2-connector.md:22`, cites `../kasegi-shokunin/PROVINCE.md:3-4`;
   that line at the round-46-time commit `c8b719d` is byte-identical to the pin and carries no
   such clause. The nearest agent-toolchain item is a CWE-78 command-injection VDP on an
   Anthropic plugin dev test hook (`SKILL.md:739–747`, `:783–788`) — a runtime vulnerability, not
   instruction-surface craft.
4. **Closest real contact is dispatch runtime, not dispatch wording.** kasegi documents the
   bounty fleet's `.ufo/prompts/` layout and mission-prompt inventory
   (`corpus/knowledge/ufo-workspaces.md:33,97,112,146`); that is runtime/workspace description,
   kumitate's half under kotoba's own split, and kasegi does not author or audit prompt wording.
5. **Direction of the only recorded relation is kotoba → kasegi.** Tree-wide `kotoba` = 6 lines
   in 4 files: `LOG.md:400` (a kotoba inventory finding parks a kasegi argument),
   `corpus/lessons/round-5-aggregator-mirror-ambiguous-citation-base.md:4,6,18` (kotoba round-5
   fleet skill audit filed defects against kasegi's `SKILL.md`; "kasegi L86"), and two
   citation-survival TSVs (`corpus/instruments/citation-survival.tsv:1025`,
   `.ufo/rounds/round-21/frozen-head-citation-survival.tsv:1041`) recording the kotoba audit file
   as `GONE`. kasegi records the audit and claims nothing back.
6. **Frontmatter description: no kotoba, no arbitration clause.** `SKILL.md:3` verbatim:
   "description: Domain specialist — bounty & security research — scopes ~/Projects/bounties,
   program rules, claim packages. Rank: shonen." `grep -c kotoba` on it → 0. Arbitration-phrase
   sweep (`arbitrat|contested|owns |refuses`) over the three pinned docs → 5 lines, none an
   arbitration clause: `PROVINCE.md:25` (generic refusal), `SKILL.md:167,313,321,368` (ops-code
   behaviour, "owns the deep bijection").
7. **Census consequence.** Kotoba's § Adjacent should drop the kasegi row or restate it as
   no-overlap, e.g. "kasegi — none at `1fafde8`: bounty/security province names
   chousa/kagi/kake/kengaku, never kotoba; zero kotoba in SKILL.md/PROVINCE.md/AGENTS.md;
   `prompt injection` absent (git grep exit 1)." If the L1 wants to keep a frontier contact, the
   only evidence-backed one is agent-toolchain security (plugin command-injection, CWE-78) vs
   kotoba's MCP/plugin instruction surfaces — explicitly not a Core boundary.
8. **Method note for the entry's `recheck:`.** The `none` sweep needs its control arm and must
   cover `corpus/`, not only the top-level docs (same lesson as CensusKagi finding 6). This row's
   recheck should re-read `PROVINCE.md:3` and rerun the two grep sweeps plus the
   `prompt[- ]injection` negative at the pinned commit.

## Scope quote (step 6, first)

`PROVINCE.md:3` at `1fafde8` — verbatim, one physical line, 11 words:
"bounty & security research — scopes ~/Projects/bounties, program rules, claim packages".
`git show 1fafde8:PROVINCE.md | grep -cF '<that line>'` → `1`, exit 0 (full line in Evidence).
Alternate, `SKILL.md:6`: "# kasegi-shokunin — bounty & security research craft", `grep -cF` → `1`.

## Overlap quote (step 6, second)

Not applicable: classification is `none`, so the assigned form asks for the negative sweep instead
of an overlap quote. The negative's best located evidence: `PROVINCE.md:40-47` § Adjacent names
four siblings and no kotoba, and `git grep -qiE 'prompt[- ]injection' 1fafde8` → exit 1.

## Evidence

Pin (step 1):
- `git -C /home/vgpnk/Projects/shokunin/kasegi-shokunin rev-parse master` → exit 0,
  `1fafde8f11454f3b0b98ab7f2b2e640aaf7f399a`.
- `git … symbolic-ref -q HEAD` → empty (detached); `git … rev-parse HEAD` → same 40-hex, exit 0.
- `git … log -1 --format='%H %ci %an %s' 1fafde8` → `2026-10-21 08:19:01 -0300 João Pedro Veiga
  considerthese: 2026-10-21 daily reflection`.
- `git … status --porcelain -- SKILL.md PROVINCE.md AGENTS.md` → empty, exit 0 (pinned docs clean).

Skill files (step 2):
- `git … ls-tree --name-only 1fafde8` → 12 entries: `.gitignore .ufo AGENTS.md LOG.md PROVINCE.md
  README.md SCORECARD.md SHONEN.md SKILL.md considerthese corpus plans`.
- `git … ls-tree -r --name-only 1fafde8 | grep -E '^(skills?/[^/]+/)?SKILL\.md$'` → `SKILL.md`
  (exit 0, exactly one; `ls-tree -r | wc -l` → `172`).

Frontmatter and province (steps 3, 5):
- `git show 1fafde8:SKILL.md` lines 1–4: `--- / name: kasegi-shokunin / description: Domain
  specialist — bounty & security research — scopes ~/Projects/bounties, program rules, claim
  packages. Rank: shonen. / ---`.
- `git show 1fafde8:PROVINCE.md` line 3 full: `**Domain:** bounty & security research — scopes
  ~/Projects/bounties, program rules, claim packages`; `grep -cF` of the unemphasised quote →
  `1`, exit 0. `Core` (lines 29–33) = program rules, scopes, claim packages, triage/claim gates,
  submission/disclosure packaging.
- Per-file `kotoba`: `SKILL.md` 0, `PROVINCE.md` 0, `AGENTS.md` 0, `README.md` 0
  (`git show 1fafde8:$f | grep -c kotoba`, exits 0/1/1/1).

Sweep (step 4, `none` coverage):
- Three pinned docs, plan pattern: `{ git show 1fafde8:SKILL.md; git show 1fafde8:PROVINCE.md;
  git show 1fafde8:AGENTS.md; } | grep -cE 'SKILL\.md|prompt|AGENTS\.md|frontmatter|trigger|
  description|kotoba'` → `5`, exit 0. Per pattern: `SKILL\.md` 2, `prompt` 1, `AGENTS\.md` 0,
  `frontmatter` 0, `trigger` 1, `description` 1, `kotoba` 0. Case-insensitive variant → `5`.
  Located: `SKILL.md:3` (own description), `:50` ("the L1 judge prompt"), `:973` and `:976`
  (references to its own `SKILL.md` citation set), `:1020` (ordinary word "trigger" in the
  disclosure table). None asserts craft ownership.
- Control arm (Q05/Q18): the same three docs `grep -ci bounty` → `SKILL.md` 42, `PROVINCE.md` 4,
  `AGENTS.md` 0, so the pipeline matches when the term is present.
- Corpus-wide plan pattern (`-- corpus`) → `312` lines (per pattern: `SKILL\.md` 270, `prompt` 10,
  `trigger` 16, `description` 16, `kotoba` 4, `AGENTS\.md` 0, `frontmatter` 0); the 270 are
  self-citations of its own skill file, and all 10 `prompt` lines are bounty-fleet runtime
  references (`ufo-workspaces.md:33,97,112,146`; lessons round-1/5/12; two TSV rows).
- Craft-ownership phrases over `corpus/` → `1` line (`corpus/lessons/round-11.md:33`), unrelated.
- `git grep -qiE 'prompt[- ]injection' 1fafde8` → exit `1` (no match anywhere).
- Tree-wide `kotoba` → `6` lines / `4` files (`git grep -n kotoba 1fafde8`), all citations of
  kotoba's audit, listed in finding 5.
- `git log -S kotoba -- PROVINCE.md` → empty, exit 0; `-S injection` and `-S prompt` → empty,
  exit 0; PROVINCE.md history is 4 commits (seed `aeddcd2` … `c8b719d`).
- `diff <(git show c8b719d:PROVINCE.md | awk 'NR==3') <(git show 1fafde8:PROVINCE.md | awk
  'NR==3')` → identical (exit 0), which falsifies the round-46 scout's citation at
  `kotoba .ufo/round-46/scouts/w2-connector.md:22`.

Hashes of the pinned docs (`git show <pin>:<path> | sha256sum`):
- `SKILL.md` `f74a9f3334688f8ef62b233c1173f5583f7edf3d03e8159be0787320677324af`
- `PROVINCE.md` `bfea62f21a4a54118fb82c1c3a0801b87d0ece37f6332f57ec3e803b581226e8`
- `AGENTS.md` `a7ad6e6e5957bffcfc04f7af75db9217e8023d049271fecb16738c83fdea5e9f`

Not run (not this seat's assignment): no lane verifier, no kotoba test, no network fetch. No tool
installed or upgraded.

## Remaining unknowns

- Only the three pinned docs were confirmed clean in the kasegi working tree; other corpus files
  may be dirty. The classification rests on the pinned commit, so this does not move the row, but
  a census recheck should re-run at the pin, not the worktree.
- The 312 corpus-wide pattern lines were characterized by per-pattern breakdown and the separate
  craft-phrase sweep, not read line by line; a line-by-line reading could surface a phrasing the
  two sweeps miss.
- Whether kotoba's round-46 scout mis-cited or read a different (uncommitted) sibling PROVINCE is
  not resolvable from kasegi's history; every committed revision lacks the clause.
