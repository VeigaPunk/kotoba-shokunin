ROW | kumitate | master (detached HEAD, same commit) | fac39171ac28c606e90da75fc2ba2ed3df52f4ea | SKILL.md | adjacent | no | yes | PROVINCE.md:3 | "**Domain:** orchestration & tooling — scopes OMP task/hub, ufo-fsd scripts & runtime"

# Round 49 C1 — sibling-overlap census: kumitate-shokunin

Date 2026-10-22. Seat KotobaR49.CensusKumitate (leaf, no dispatch). Lane kotoba-shokunin
read-only except this file; kumitate-shokunin read-only throughout via
`git -C … show/ls-tree/rev-parse/grep`. No jj, no git write, no pacman.

## Findings

1. **Classification `adjacent`** — dispatch runtime versus dispatch and skill wording.
   kumitate owns the dispatch *machinery*: the three dispatch shapes, swarm wave
   producer/consumer, sighting lifecycle, native-trial launch sequence, plus a
   *file-level census* of the Kimi substrate. kotoba owns *craft*: SKILL.md frontmatter
   and trigger discipline, prompt wording, the fidelity checklists over
   `.ufo/prompts/*.md` (dispatch.04, dispatch.08) and AGENTS.md-class files.
2. **Reciprocal, not contested.** kumitate's own PROVINCE.md:27 cedes "Prompt and skill
   craft → kotoba"; its SCORECARD.md:1616 cedes "`skills/*` craft and trigger discipline
   to **kotoba**". kotoba's PROVINCE.md:30 says the mirror image: "kumitate —
   orchestration/dispatch runtime and swarm lifecycle; kotoba owns the prompt wording,
   not the runtime." Both sides name the same split, so no claim is in dispute.
3. **Frontmatter description does not name kotoba** — `git show <c>:SKILL.md | grep -c
   kotoba` → `0`. It carries no sibling arbitration clause either; the arbitration lives
   in PROVINCE.md:27 and SCORECARD.md:1616, both of which name kotoba.
4. **No cross-lane skill/prompt auditing** in kumitate's surface. Its fifteen-item
   Verifiable checklist (SKILL.md:617-647) gates *its own* citation/proxy/census/anchor
   truth; nothing there audits another lane's SKILL.md, prompts or AGENTS.md. Its
   instruments are `scripts/*.mjs` over its own corpus and over the origin tree.
5. **Where kumitate touches skill files it stays descriptive.** `corpus/knowledge/
   kimi-skills-plugins.md` inventories frontmatter of five installed skills
   ("Frontmatter (L1–8)", lines 39, 49, 60, 80, 131, 161, 179, 286) and closes with a
   section titled "Cross-domain findings — report, do not absorb" (line 369). Census,
   not craft.
6. **Boundary risk to watch (inference, not a defect).** kumitate's Anti-patterns
   (SKILL.md:475-495) constrain the *content* of an emitted dispatch payload — distinct
   `{{item}}` expansions, "never a generic-`task` wave", "never carry `role`/`agent` on a
   resume lane", one `task` call per wave. Those are mechanically checkable properties of
   the tasks array; kotoba's dispatch.04/.08 check the wording fidelity of the prompt
   files themselves. Same artifact, different halves — this is the exact seam to state in
   PROVINCE.md § Adjacent.
7. **kumitate ran this same census in round 35** and its row for kotoba reads
   `.ufo/waves/round-35/build/ConnectorSiblingOverlap.md:23`: "…consumes
   `scripts/ufo-swarm-wave.mjs` behaviour… Absorb; validation ≠ dispatch; re-run at new pin
   not guaranteed." Its boundary verdict matches mine (runtime vs validation), taken at an
   older pin.

## Evidence

Pin (step 1):
- `git -C /home/vgpnk/Projects/shokunin/kumitate-shokunin rev-parse master` → exit 0,
  `fac39171ac28c606e90da75fc2ba2ed3df52f4ea`.
- `git … symbolic-ref -q HEAD` → exit 1 (no output): HEAD is **detached**;
  `git rev-parse HEAD` → same 40-hex; `git branch --show-current` → empty;
  `git describe --all` → `heads/master`; `git branch` → `* (no branch)` plus `master`.
  So the pin is master's tip, checked out detached.

Skill files (step 2):
- `git … ls-tree --name-only fac3917` → `.gitignore .ufo AGENTS.md LOG.md PROVINCE.md
  README.md SCORECARD.md SHONEN.md SKILL.md considerthese corpus scripts` (exit 0).
- `git … ls-tree -r --name-only fac3917 | grep -E '^(skills?/[^/]+/)?SKILL\.md$'` → `SKILL.md`
  (exit 0, exactly one; no `skills/` or `.agents/` directory tracked —
  `git ls-tree -r --name-only fac3917 | grep -E '^(skills?|\.agents)/'` → zero rows,
  exit 1; `… | grep -cE` → `0`, exit 1).
- File sizes at pin: SKILL.md 842 lines; sha256 `708ebc91e2c6390b49b1397317f38e43fa4c73240824465c0f3a72ec6d4d7879`;
  PROVINCE.md sha256 `fcd69667a1027d5edd07a8ff0390a716a467aff92719071e33cb6157673b665f`;
  AGENTS.md sha256 `0d619d4b74c47897320e0c0c99821a30be8afc2f88628de4f6aee7e41cfc8d12`.

Frontmatter (step 3), `git show fac3917:SKILL.md` lines 1-4 verbatim:
```
---
name: kumitate-shokunin
description: Domain specialist — orchestration & tooling — scopes OMP task/hub dispatch, ufo-fsd scripts, crates/ufo-core-runtime. Rank: shonen.
---
```

PROVINCE.md key lines (`git show fac3917:PROVINCE.md`, sha256 above):
- L3 `**Domain:** orchestration & tooling — scopes OMP task/hub, ufo-fsd scripts & runtime` (12 words)
- L5 `**Owns:** the domain knowledge, playbooks, error patterns, and checklists above.`
- L6 `**Refuses:** anything outside this domain; report cross-domain evidence back to the orchestrator rather than absorbing it.`
- L12-15 Core: origin script layer S1–S8, origin runtime layer R1–R11, Kimi substrate K1–K5, "the lane's own instruments `scripts/*.mjs`".
- L19-22 Frontier: OMP harness contract, MCP protocol revisions, isolation substrates, durable execution.
- L24-28 Adjacent: `MCP/OAuth security practice … → kasegi / kagi.` / `Local model serving and endpoints → kama. Prompt and skill craft → kotoba. Research method → chousa.` / `Upstream defects in /home/vgpnk/Projects/ufo-fsd-alpha → filed in lane reports for the operator; never patched from here.`

Counts (step 5, commands verbatim, all at `fac3917`):
- `git show fac3917:SKILL.md | grep -c kotoba` → `0`
- `git show fac3917:PROVINCE.md | grep -c kotoba` → `1` (line 27)
- `git show fac3917:SCORECARD.md | grep -c kotoba` → `1` (line 1616)
- `git show fac3917:AGENTS.md | grep -c kotoba` → `0`; same for README.md → `0`
- `git show fac3917:SKILL.md | grep -Ec 'SKILL\.md|prompt|AGENTS\.md|frontmatter|trigger|description|kotoba'` → `13`
- `git show fac3917:PROVINCE.md | grep -Ec '<same pattern>'` → `2` (L15, L27)
- `git grep -l -i kotoba fac3917` → 6 paths: `.ufo/rounds/round-33/owned-metadata.patch`,
  `.ufo/waves/round-35/build/ConnectorSiblingOverlap.md`, `LOG.md`, `PROVINCE.md`,
  `SCORECARD.md`, `corpus/lessons/round-14.md`. Reports and lessons only — no instrument.

Arbitration clause (step 5), SCORECARD.md:1612-1618:
> **K-block boundary clause (fleet audit, `FLEET-ADJACENCY-ERRATA-V1` clause A).** The
> K-block registry is an enumerable CENSUS of `~/.kimi-code` filesystem members, not
> exclusive ownership of their domains: … `skills/*` craft and trigger discipline to
> **kotoba**, and secret-bearing paths (`credentials/`, `oauth/`, `server.token`) to
> **kagi** discipline.

Quotes (step 6):
1. Scope — `PROVINCE.md:3`, 12 words, sha256 of the containing file above:
   "**Domain:** orchestration & tooling — scopes OMP task/hub, ufo-fsd scripts & runtime"
2. Overlap — `PROVINCE.md:27`, 18 words:
   "Local model serving and endpoints → kama. Prompt and skill craft → kotoba. Research method → chousa."
   Counts: `git show fac3917:PROVINCE.md | sed -n '27p' | wc -w` → `18` (exit 0);
   `… | sed -n '27p' | wc -c` → `109` (exit 0). Line 3: `wc -w` → `12`, `wc -c` → `87`.

## Confirmations and gaps

- Confirmed: no `skills/` tree, no cross-lane SKILL.md or prompt instrument (`git grep -n
  -E "audit(s|ing)? .*SKILL\.md|SKILL\.md .*audit"` returns only its own round reports and
  lessons rows, no script). Frontmatter appears in kumitate only inside its own corpus
  notes about `~/.kimi-code` (descriptive rows, `kimi-skills-plugins.md`).
- Unresolved: whether kumitate's `scripts/render-seat-tables.mjs` (`TARGETS` includes
  `AGENTS.md`, seen at `.ufo/waves/round-35/falsify/SecRenderSeatTables.md:62`) writes
  into AGENTS.md-class files *inside its own repo* or reaches other lanes. Its falsify
  report describes `TARGETS = Object.freeze(["AGENTS.md", …])` locally; I did not read the
  script body at the pin, so "no cross-lane write" is inference from the grep sweep, not
  read proof. A reader wanting certainty should check
  `git show fac3917:scripts/render-seat-tables.mjs` for path roots outside the repo.
- Not run by design: no builds, no linters, no lane verifiers (main agent's job).

Tooling: none installed or upgraded this seat (pacman transactions host-wide paused; no
`uv`/`npx` install needed). Tools used: git (system), GNU grep/sed/wc/sha256sum, python3
(read-only JSON parse of the lane baseline).
