# Falsify RowKumitate — C1 census row `kumitate` (round 49)

Verdict: **HOLDS** — the census row `kumitate` (corpus/knowledge/sibling-overlap-census-round49.md),
its PROVINCE.md § Adjacent row, and the boundary note survive every attack I ran. No finding
reaches the classification, the quote, the pin, or either mechanical column. Two minor defects
noted, neither in judged bytes.

Attacked at: kotoba branch master c48793db (base a5adc146); sibling pin
fac39171ac28c606e90da75fc2ba2ed3df52f4ea in /home/vgpnk/Projects/shokunin/kumitate-shokunin
(read-only). Leaf seat, no subagents. Nothing installed or upgraded (pacman paused; no need arose).

## Findings

1. MINOR (build artifact, not judged bytes) — `.ufo/waves/round-49/build/CensusKumitate.md` ROW
   header line lists the arbitration cell as `yes`, contradicting the seat's own finding 3
   ("carries no sibling arbitration clause either") and the census's mechanical definition
   (sibling tokens in the frontmatter description). The census table's `no` is the correct value;
   the guard re-derives it from pinned bytes and passes. The judged artifact is right; the build
   report's ROW line is internally inconsistent.
2. MINOR (guard gap, latent) — `verifiers/check_sibling_census.py` validates the quote, commit,
   classification, skill-file, names-kotoba and arbitration cells, but nothing asserts the branch
   cell. It is correct today (pin reachable from master), but a branch rename or history rewrite
   would rot the cell silently while the guard stays green.
3. Observation, not a defect — kumitate master has advanced 3 commits past the pin since the
   census (round-39 candidates, tip dfa159d5). The entry's Limits section covers pin movement and
   the recheck reads pinned bytes, so no row value is invalidated.

## Attack results (claim-by-claim)

(1) Pin and branch cell — HOLDS. Commit exists (log -1 → "considerthese: 2026-10-21 daily
reflection", exit 0) and is reachable from master (`git log --format=%H master | grep -c
'^fac39171…'` → 1). Build seat measured master == fac3917 at pin time (detached HEAD, same
commit); since then master moved +3. Branch cell "master" remains true.

(2) Scope quote — HOLDS. `git show fac3917:PROVINCE.md` line 3 (±2: L1 title, L2 blank, L4 blank)
is byte-identical to the census quote, em-dash U+2014 included (cat -A: `M-bM-^@M-^T`):
`**Domain:** orchestration & tooling — scopes OMP task/hub, ufo-fsd scripts & runtime`.
Guard, re-run by me in a fresh scratch clone at c48793db: `rows 20 verified 20 / province rows 20
matched 20`, exit 0 — the kumitate row's quote, commit, classification and both mechanical cells
all re-verify against pinned bytes.

(3) Classification `adjacent` — HOLDS; contested and none both fail.
- adjacent is satisfied by the sibling's own committed split statements: kumitate
  `PROVINCE.md:27` "- Local model serving and endpoints → kama. Prompt and skill craft →
  kotoba. Research method → chousa." (18 words) and `SCORECARD.md:1616` "`skills/*` craft and
  trigger discipline to **kotoba**, and secret-bearing paths…" (K-block boundary clause, lines
  1612-1618). Both cited lines verified at the pin.
- contested fails on a full committed-surface sweep, including the one file the build seat left
  unread: `scripts/render-seat-tables.mjs` (its AGENTS.md TARGETS worry) was **never committed**
  at any revision (`git log --all -- '*render-seat-tables*'` → empty, exit 0; at the pin only two
  round-35 wave reports mention it). All eight committed scripts are self-scoped: cite-check
  `SELF_DOCS = {SKILL.md, LOG.md, SCORECARD.md, PROVINCE.md, SHONEN.md, AGENTS.md}` (its own
  docs), surface-probe "parse this repo's `SKILL.md`", no `/home/` or sibling paths in any script.
  SKILL.md's 13 prompt/SKILL/frontmatter lines are all dispatch-runtime mechanics over its own
  payloads. `.ufo/rounds/round-33/owned-metadata.patch` touches only its own LOG.md/SCORECARD.md
  and is the commit that *introduces* the cession clause. `corpus/knowledge/kimi-skills-plugins.md`
  inventories `~/.kimi-code` skills descriptively under "Cross-domain findings — report, do not
  absorb", routing the `.omp/skills` layout to the host-plane lane and endpoints to kama.
  kumitate's own round-35 connector (`.ufo/waves/round-35/build/ConnectorSiblingOverlap.md`,
  kotoba row) reads kotoba's SCORECARD claim on `ufo-swarm-wave.mjs` behaviour and disposes
  "Absorb; validation ≠ dispatch" — substrate membership of its own script, kotoba's validation
  explicitly not absorbed. No surface claims any part of kotoba's core.
- none fails because the split is explicitly stated by the sibling — exactly the rule's adjacent
  arm. One kotodama-style override is not needed here; the seat's call matches the rule.

(4) Mechanical columns — HOLDS. Re-derived from `git show fac3917:SKILL.md` line 3
("Domain specialist — orchestration & tooling — scopes OMP task/hub dispatch, ufo-fsd scripts,
crates/ufo-core-runtime. Rank: shonen."): sibling/kotoba whole-token case-insensitive sweep →
0 tokens; `grep -c kotoba` over the whole SKILL.md → 0. Census cells `no | no` are correct.

(5) PROVINCE.md boundary note — HOLDS. "orchestration and dispatch runtime and swarm lifecycle":
kumitate PROVINCE.md:3 ("orchestration & tooling — scopes OMP task/hub, ufo-fsd scripts &
runtime") and SKILL.md description cover the first half; SKILL.md line 18 (Swarm wave table row),
line 37 ("`scripts/ufo-swarm-wave.mjs` — wave producer") and 20 swarm matches cover "swarm
lifecycle". "kotoba owns the prompt wording, not the runtime" is kotoba's own position, mirrored
by kumitate's cession and its round-35 "validation ≠ dispatch". Citation "(kumitate
`PROVINCE.md:27`)" is the right line — the cession sentence sits on line 27. Commit cell
fac39171… and classification adjacent match the census row.

## Residual risk and verification gaps

- The branch cell is unguarded (finding 2); everything else in the row is guard-checked.
- The PROVINCE boundary free text is not guard-checked (guard joins classification and commit
  only); my check of it is manual this round.
- I did not sweep kumitate's full corpus/ file-by-file (24 tracked files beyond top level); the
  contested arm rests on the token sweep (`git grep -l -i kotoba fac3917` → 6 paths, all read:
  2 wave/round reports, LOG, PROVINCE, SCORECARD, lessons/round-14 — every one cessions or
  description) plus the scripts sweep. An unread corpus file claiming prompt-craft ownership
  would have to avoid the token `kotoba` and every sibling token to slip past.

## Evidence (commands and exit codes)

All sibling reads via `git -C /home/vgpnk/Projects/shokunin/kumitate-shokunin <show|log|ls-tree|rev-parse>` at fac39171ac28c606e90da75fc2ba2ed3df52f4ea; kotoba reads read-only.

- `git rev-parse master` → dfa159d5152ff8449ce04c7e5e7021fa3cce6d30 (rc 0); `git log -1 --format='%H%d %ci %s' fac39171…` → rc 0; `git log --format=%H master | grep -c '^fac39171…'` → 1.
- `git show fac3917:PROVINCE.md | sed -n '1,8p' | cat -A` → L3 verbatim incl. U+2014 (rc 0); `sed -n '27p' | wc -w` → 18 (rc 0).
- `git show fac3917:SCORECARD.md | sed -n '1610,1620p'` → cession clause, line 1616 (rc 0).
- `git show fac3917:.ufo/rounds/round-33/owned-metadata.patch | head -80` → own LOG/SCORECARD only (rc 0).
- `git ls-tree --name-only fac3917:scripts` → 8 .mjs, no render-seat-tables (rc 0); `git log --all --oneline -- '*render-seat-tables*'` → empty (rc 0).
- Per-script `grep -nE '/home/|shokunin|SKILL\.md|AGENTS'` → self-doc/self-repo hits only (rc 0).
- `git show fac3917:SKILL.md | sed -n '3p' | grep -ioE '\b(…20 sibling tokens…|kotoba)\b' | wc -l` → 0; `… | grep -ic kotoba` → 0; `grep -icE 'swarm'` → 20; `grep -inE 'swarm' | head` → lines 18/25/27/32/37/40 (rc 0).
- `git show fac3917:corpus/knowledge/kimi-skills-plugins.md | sed -n '360,378p'` → "report, do not absorb" (rc 0).
- Guard in scratch clone: `git clone -q <lane> /fast/scratch/hyaku/kotoba-r49/falsify/RowKumitate/clone && git checkout -q c48793db && python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` → `rows 20 verified 20 / province rows 20 matched 20`, **guard_rc=0**.
