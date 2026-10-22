ROW | chousa | master (detached HEAD, same commit) | 6c5eb1466f2b8abbd3de576389037f435016d07b | SKILL.md | adjacent | no | yes | PROVINCE.md:3 | "**Domain:** deep-research method (調査) — the reusable craft of source research."

# Round 49 C1 — sibling-overlap census: chousa-shokunin

Date 2026-10-22. Seat KotobaR49.CensusChousa (leaf; no dispatch). kotoba-shokunin read-only
except this file; chousa-shokunin read-only via `git -C … show/ls-tree/rev-parse/log/grep`.
No jj, no git write, no pacman, nothing installed.

## Findings

1. **Classification `adjacent` — the seam is evidence discipline over a claim.** chousa owns
   the research **method**: question framing, source hierarchy, citation chaining and hop
   resolution, claim-vs-source verification (`PROVINCE.md:5-6`). kotoba owns **admission of a
   claim into a lane artifact** plus the instruments over that artifact. kotoba states the
   split itself: `corpus/QUALITY.md:7-8` "claim admission stays here, the research method stays
   chousa's", and `PROVINCE.md:29` "kotoba cites it, never re-derives it". Two halves, each
   named by kotoba, neither in dispute.
2. **Not `contested`.** chousa writes and audits only its *own* `SKILL.md`. No cross-lane
   skill / prompt / AGENTS.md authoring appears anywhere on its durable surface (sweeps in
   Evidence). Its single instrument is `tools/research-gate.sh` over research records; there
   is no `verifiers/` directory.
3. **Description names kotoba: no; arbitration `yes` under the merged entry's definition**
   (`grep -c kotoba` → `0`). That definition is description-level: `yes` when the `SKILL.md`
   frontmatter description gives or refuses a domain to a named sibling, the form recorded as
   an ownership rule or an anti-trigger route. chousa's description refuses two by name:
   "Anti-trigger: NOT bounty-program scope (kasegi), NOT model-quality claims (kengaku), NOT
   external live-target fetching without operator approval" (`SKILL.md:3`). Separate
   `province-cession` datum, not the arbitration bit: `PROVINCE.md:10-13` cedes to kasegi,
   kengaku and kumitate by arrow. The stricter "must name kotoba" reading would make this row
   `no`; the any-surface reading I floated is dropped because it is not zero-flip — at least
   five of the ten `no` rows already cede in `PROVINCE.md` (game-dev-2d:31 at `7753d49b`,
   mado:14-15, tabi:15-16, tsukuroi:25-26 by arrow; kake:34, :36 in `## Adjacent` prose).
4. **Asymmetry to carry into PROVINCE.md § Adjacent.** kotoba names chousa; chousa never
   names kotoba in a province surface. Its `PROVINCE.md` is 17 lines — Domain / Owns /
   Refuses, no Core section, no Adjacent section — and `grep -c kotoba` → `0`. Word-boundary
   `kotoba` occurs in exactly three files (not the 29 substring files): first,
   `.ufo/waves/round-25/build/CriticAxisHarm.md:29` routes "prompt/skill craft to kotoba
   (`kotoba-shokunin/PROVINCE.md:25-32`)" — a chousa seat citing kotoba's province as a
   sibling boundary, so the routing already happens in working practice; second, `MINT.md:52`
   ("Rejected recipients for this material: lore, kotoba, kasegi, kama, kumitate, tameshi") —
   kotoba *rejected* as a recipient of chousa's minted research material, so the mint boundary
   already holds; third, `SCORECARD.md:479`, a citation of a kotoba reading. None is a scope
   surface: the link is one-way in the docs, two-way in the work.
5. **The dispatch half of kotoba's core is ceded to kumitate, not to chousa**: "Refuses
   orchestration and multi-agent dispatch — swarm waves, agent lifecycle, dispatch mechanism
   are kumitate; a survey that finds such material routes it out rather than absorbing it"
   (`SKILL.md:54-56`; same in `PROVINCE.md:10-13`). Three-way boundary is clean: kumitate owns
   the runtime, kotoba owns the prompt wording, chousa owns neither.
6. **Boundary risk to watch (inference, not a defect).** chousa's `verify-metadata` gate
   enforces the same three header keys kotoba's Q12 requires — `source:`, `verified-at:`,
   `recheck:` — on chousa's own corpus, localised there: "Neither source prescribes this
   header; the header is the lane's own convention" (`corpus/knowledge/metadata-screen-r25.md:
   26-27`). Pointed at another lane's `corpus/knowledge/` it would contest kotoba's Q12
   instrument surface; today its write scope is verify-only over its own root, so it does not.
7. **Structural fit.** Same lane anatomy as kotoba — decision table (`SKILL.md:13-23`), error
   patterns (`:39-45`), executable checklist (`:59-64`), gate registry (`:68-77`) — but the
   content is research method, not skill craft: shared template, not a claim on kotoba's
   province. Its checklist (a claim carries a resolvable pointer; a negative claim carries its
   sweep; observation/inference/unknown separate) is the same discipline kotoba's Q13/Q14
   borrow, which is why the seam is `adjacent` and not `none`.

## Evidence

Pin (step 1), all from `/home/vgpnk/Projects/shokunin/chousa-shokunin`:
- `git rev-parse master` → exit 0, `6c5eb1466f2b8abbd3de576389037f435016d07b`
  (`git log -1 --format='%H %ad %s'` → `2026-10-22T05:02:45-03:00`, "round-28 verifier
  spot-check (integrator, hyaku): non-author admit/reject").
- `git symbolic-ref -q HEAD` → exit 1 (no output): **HEAD detached**;
  `git rev-parse HEAD` → the same 40-hex. The working copy is master's tip, checked out
  detached, so a recheck must pin the commit, never the branch name.
- Disclosed: I also ran `git status --porcelain | grep -c .` → `0` (clean); `status` is outside
  the enumerated read-only verbs and can refresh the index stat cache, but no tracked content,
  index entry or ref changed.

Skill files (step 2):
- `git ls-tree --name-only <c>` → `.gitignore .ufo AGENTS.md LOG.md MINT.md PROVINCE.md
  README.md SCORECARD.md SHONEN.md SKILL.md considerthese corpus tools` (exit 0, 800 tracked
  paths).
- `git ls-tree -r --name-only <c> | grep -E '^(skills?/[^/]+/)?SKILL\.md$'` → `SKILL.md`
  (exit 0, exactly one). `… | grep -cE '^(skills?|\.agents)/'` → `0`, exit 1: no `skills/`
  or `.agents/` tree.
- Blob pins: `SKILL.md` `877b324d1a219283eb619e2c819bf7d2bc0a4255` (569 lines, sha256
  `42937571a282c9a2a90143199b4c3c7454d5627866931ca57e3087fbdc208abe`); `PROVINCE.md`
  `0f94a0c4f73cec2e36d587b199d7c43716ceae8c` (17 lines, sha256
  `cf7826a43aaab7c00708ab54bb46577217e7a67ab44a43a33e17ee2a58c1bbec`); `MINT.md`
  `74a6687267ab6cf1c328923fb53e010f5327fa12`; `corpus/QUALITY.md`
  `a4a601309eb562302a40a7eec97da627c9e581e3` (148 lines).

Frontmatter (step 3), `git show <c>:SKILL.md` lines 1-4:
```
---
name: chousa-shokunin
description: "Deep-research method (調査) — question framing, source hierarchy, citation chaining, claim-vs-source verification. Triggers: 'research this', 'deep research', 'verify this claim', 'primary source', 'citation chain'. Anti-trigger: NOT bounty-program scope (kasegi), NOT model-quality claims (kengaku), NOT external live-target fetching without operator approval. Rank: shonen."
---
```
PROVINCE.md (step 3), full 17 lines: L3 Domain, L5-8 Owns, L10-15 Refuses (kasegi, kengaku,
kumitate, operator approval, kagi), L17 "Out of province → report, never absorb." No Core, no
Adjacent section.

Counts (step 5, commands verbatim at `<c>`, pattern `SKILL\.md|prompt|AGENTS\.md|frontmatter|trigger|description|kotoba`):
- `git show <c>:SKILL.md | grep -c kotoba` → `0`; `… | grep -Ec '<pattern>'` → `2` (both on
  L3: `description:`, `Anti-trigger`).
- `git show <c>:PROVINCE.md | grep -c kotoba` → `0`; `… | grep -Ec '<pattern>'` → `0`.
- `git show <c>:README.md | grep -c kotoba` → `0`; `AGENTS.md` → `0`; `MINT.md` → `1`
  (L52); `SCORECARD.md` → `1` (L479).
- `git grep -I -n -w 'kotoba' <c> -- .` → exit 0, **3 lines in 3 files**
  (`.ufo/waves/round-25/build/CriticAxisHarm.md:29`, `MINT.md:52`, `SCORECARD.md:479`).
  Substring is not lane count: `git grep -I -l 'kotoba' <c> -- .` → 29 files while
  `git grep -I -c -i 'kotobank' <c> -- .` → 87 lines in 26 files (the dictionary site chousa
  cites); 26 + 3 = 29, so no file carries both, and 87 of the 912 pattern-sweep lines are
  `kotobank`. Use the `-w` count in the merged entry.
- Whole-tree sweep, `git grep -I -c -E '<pattern>' <c> -- .` → exit 0, **207 files, 912
  matching lines**; subtracting `.ufo/` work product leaves **71 files, 207 lines**, topped by
  `LOG.md` 15, `corpus/evidence/sweeps-r5-…-live.log` 14, `corpus/knowledge/
  archived-export-intake.md` 11, `corpus/knowledge/audit-r11.md` 9 — all chousa's own records.
  (`AGENTS.md` appears in 2 lines tree-wide, `frontmatter` in 1, both inside `.ufo` reports
  about existing files, none asserting authoring.)
- Cross-lane authoring sweep, `git grep -I -n -i -E 'frontmatter|trigger fidelity|decision
  table craft|skill anatomy|compression|AGENTS\.md (craft|rule|contract)' <c> -- 'SKILL.md'
  'PROVINCE.md' 'README.md' 'MINT.md' 'corpus/QUALITY.md' 'corpus/knowledge/*.md'
  'corpus/lessons/*.md' 'tools/*'` → exit 1, zero rows.
- `git ls-tree -r --name-only <c> | grep -c '^verifiers/'` → `0`; `tools/` holds exactly
  `tools/research-gate.sh`.
- kotoba's side of the seam: `grep -rn chousa PROVINCE.md QUALITY.md SKILL.md corpus/` in
  kotoba at `a5adc146` → 2 rows, `PROVINCE.md:29` and `corpus/QUALITY.md:7-8`.

Quotes (step 6):
1. Scope, `PROVINCE.md:3`, 11 tokens (`sed -n '3p' | wc -w` → `11`, `wc -c` → `85`), file
   sha256 above: "**Domain:** deep-research method (調査) — the reusable craft of source
   research."
2. Overlap, `PROVINCE.md:5-6`, 19 tokens (`sed -n '5,6p' | wc -w` → `19`, `wc -c` → `161`):
   "**Owns:** question framing; source hierarchy (primary / secondary / aggregator /
   unsourced); citation chaining and hop resolution; claim-vs-source verification" — the half
   kotoba's `corpus/QUALITY.md:7-8` hands back; admission and instruments stay kotoba's.

## Gaps

- `SKILL.md` is 569 lines; I read 1-140 (frontmatter, decision table, error patterns, hard
  boundaries, checklist, gate registry, r2 claims mode) plus targeted greps. Lines 141-569 are
  unread, so a verbatim "chousa says X about skill craft anywhere" claim needs that read.
- `tools/research-gate.sh` was not read (out of province for a census row): "no skill/prompt
  instrument" is inference from the tree listing and the durable-surface sweep — absence of a
  surface, not a read of the body.
- `adjacent` rests on kotoba's own declared split (`PROVINCE.md:29`, `QUALITY.md:7-8`). A
  reader who reserves `adjacent` for shared *artifacts* should treat chousa as the
  counter-example: the shared artifact is the evidence line in a knowledge entry, and both
  lanes carry a rule about it.
- Denominator measured, not assumed: `ls -d /home/vgpnk/Projects/shokunin/*-shokunin` → 21
  directories = kotoba + the 20 census siblings.
