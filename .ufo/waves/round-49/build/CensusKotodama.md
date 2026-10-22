ROW | kotodama | detached (no branch; main same commit) | 35f0d49f96f1d51f8b006136a8e1d0e8d0919a7a | SKILL.md | none | yes | yes | SKILL.md:8-10 | "Domain: the generative craft that connects languages, cultures, myths, symbolisms, and eras to their linguistics and costumes for a fictional world"

# Round 49 C1 — sibling-overlap census: kotodama-shokunin

Date 2026-10-22. Seat KotobaR49.CensusKotodama (leaf, no dispatch). Lane
kotoba-shokunin read-only except this file; kotodama-shokunin read-only throughout via
`git -C … rev-parse/ls-tree/show/grep/log`, no working-tree reads, no jj, no git writes.

## Findings

1. **Classification `none`** against kotoba's province Core (`PROVINCE.md:12-14`:
   SKILL.md trigger/frontmatter craft, anatomy and compression, decision tables, the four
   fidelity checklists; agent-definition, AGENTS.md-class and dispatch-prompt craft;
   instruments over those surfaces). kotodama claims only the linguistic-cultural
   generative craft and its own records (`PROVINCE.md:9-11`) and refuses the whole kotoba
   surface by name (`PROVINCE.md:20`, `SKILL.md:3`). It owns no function on any kotoba
   surface: no cross-lane skill, prompt or AGENTS.md authoring, no auditor of another
   lane's skill file, no instrument over those surfaces.
2. **Why not `adjacent`.** The only shared artifact class is `SKILL.md` itself, and
   kotodama holds an *instance* of it, not a half of its governance. The sibling draws
   that line itself: "Lane-operating craft rules ≠ kotoba's cross-lane skill craft"
   (`reports/round-33/adj/A01-province.md:75`). Compare kumitate (`adjacent`): it owns a
   distinct function — the dispatch runtime — on the same artifact as kotoba's wording.
   kotodama owns no such function, so the overlap set is empty.
3. **Arbitration clause: yes, and it names kotoba.** The frontmatter description carries
   four anti-triggers naming three siblings: `lore-shokunin` (canon recording and
   consistency verification), `kotoba-shokunin` (prompt/skill craft), `chousa-shokunin`
   (general source-research method); the fourth refusal (real-world rights/attribution)
   names no lane. `PROVINCE.md:20` repeats the cession: "prompt/skill craft (kotoba)".
4. **This is the name-collision row.** kotoba (言葉) and kotodama (言霊) are both
   "word/language" names; the sibling's mint record arbitrates it explicitly: "kotoba owns
   prompt/skill craft despite its name" (`MINT.md:20`). So the routing risk exists even
   though the province risk does not — keep the lane in § Adjacent on that ground, as
   kotoba's current line already does ("no overlap observed", `PROVINCE.md:34`).
5. **No cross-lane instrument.** `tools/` holds 16 scripts plus `gates/` and `harness/`;
   the only `tools/*.py` string `SKILL.md` is a docstring spec citation
   (`tools/gates/argot-derivation-gate.py:4`), and no tool opens, parses or writes a skill
   file or prompt: `git grep -lci 'frontmatter' <c> -- tools/` → no paths, exit 1.
   Its own prompt templates (`reports/round-5/…`, `-6/…`, `-7/prompt-template.txt`) and
   `templates/round-runner-template.py` bind its own seats only; `round-7/prompt-template.txt:13`
   quotes the fleet contract (`fleet templates/round-prompt.md`) rather than authoring one.
6. **In-lane gaps the census should not overstate** (both checked, both negative):
   the hard-boundary list `SKILL.md:509-520` omits kotoba entirely — the refusal lives only
   in the frontmatter and PROVINCE.md; and `AGENTS.md` (40 lines) names no sibling
   (`git show <c>:AGENTS.md | grep -c kotoba` → 0). Neither weakens the classification;
   both are places a later drift could hide a claim.
7. **Reciprocity check.** kotoba's `PROVINCE.md:34` already files kotodama as
   "no overlap observed" in a five-lane lump. This row confirms that line at a pin, with a
   sweep, and supplies the arbitration quote the lump lacks.

## Evidence

Pin (step 1, `C=35f0d49f96f1d51f8b006136a8e1d0e8d0919a7a`):
- `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin rev-parse master` → **exit 128**,
  `fatal: ambiguous argument 'master': unknown revision or path not in the working tree`
  (the repo has no `master`; `git branch -a` lists `main` and hyaku/* only).
- `git … symbolic-ref -q HEAD` → **exit 1, no output**: HEAD is detached.
- `git … rev-parse HEAD` → `35f0d49f96f1d51f8b006136a8e1d0e8d0919a7a`; `git … rev-parse main`
  → same 40-hex, so the pin is main's tip checked out detached. `git branch` → `* (no branch)`,
  `main`. `git log -1` → `35f0d49… 2026-10-22 06:33:02 -0300 round-51: claim D — pastoralism
  section-2 boundary table 11 -> 15 rows …`. Working tree carries one untracked path,
  `.ufo/waves/round-51/` (not read).

Skill files (step 2), all exit 0:
- `git … ls-tree --name-only <c>` → `.gitignore .ufo AGENTS.md LOG.md MINT.md PROVINCE.md
  README.md REGIMEN.md SCORECARD.md SHONEN.md SKILL.md corpus examples reports templates tools`
- `git … ls-tree -r --name-only <c> | grep -E '^(skills?/[^/]+/)?SKILL\.md$'` → `SKILL.md`
  (exactly one; no `skills/` or `.agents/` tree — that pipeline returns no rows for
  `^(skills?|\.agents)/`, exit 1). 3670 tracked files total.

Frontmatter (step 3), `git show <c>:SKILL.md` lines 1-4 verbatim:
```
---
name: kotodama-shokunin
description: "Linguistic-cultural worldbuilding (言霊) — conlang craft, myth & symbol systems, era staging, costume/material-culture lexicon, and the coupling between them, feeding the world bible. Triggers: 'design a language', 'conlang', 'culture for this world', 'mythology of', 'symbolism of', 'naming system', 'costume/dress terms', 'era language stages', 'word for this concept'. Anti-trigger: NOT world-bible canon recording or consistency verification (lore-shokunin), NOT prompt/skill craft (kotoba-shokunin), NOT general source-research method (chousa-shokunin), NOT real-world rights/attribution rulings. Rank: shonen."
---
```
SKILL.md 734 lines / 88426 bytes, sha256 `1b4efe0f83fafe57c208076a23c9a42b111e2c1de4688c342215938c9fe8fd53`.
PROVINCE.md 31 lines / 1636 bytes, sha256 `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6`.

PROVINCE.md sections at the pin: L3-7 **Domain** (linguistic-cultural worldbuilding),
L9-14 **Owns** ("the generative/coupling craft and its records in this repo … they do not
expand ownership into general research method, fleet protocol, historical truth
certification or lore's canon"), L16-20 **Refuses** (canon → lore; real-world
rights/attribution; game mechanics → game-dev-2d/3d; research method → chousa; web
publishing → kake; prompt/skill craft → kotoba), L22-25 adjacent contract (lore, load-bearing,
`corpus/knowledge/synthesis/worldbible-integration-contract.md`), L27-29 write scope
("Only writes this standalone lane repository … Sibling repositories … read-only").
There is **no `## Core` section** and no per-sibling Adjacent list; kotoba appears once, in
Refuses.

Counts (step 5, commands verbatim, at `<c>`):
- `git show <c>:SKILL.md | grep -c kotoba` → `1` (line 3, anti-trigger); occurrence count
  `grep -o kotoba | wc -l` → `1`.
- `git show <c>:PROVINCE.md | grep -c kotoba` → `1` (line 20).
- `git show <c>:README.md | grep -c kotoba` → `1` (line 6, same description text);
  `AGENTS.md` → `0`; `MINT.md` → `2` (lines 20, 30); `SCORECARD.md` → `0`.
- `git grep -l -i kotoba <c>` → **68** paths: 6 top-level docs (SKILL, PROVINCE, README,
  MINT, LOG, corpus/README), 1 round-50 build note, ~45 reports (adjacency/scope/drift),
  ~10 corpus knowledge/lesson rows, rest `.ufo`/recheck JSON. No `tools/` or `verifiers/` path.

Sweep for `none` (step 4), required pattern:
- `for f in SKILL.md PROVINCE.md; do git show <c>:$f | grep -Eic 'SKILL\.md|prompt|AGENTS\.md|frontmatter|trigger|description'; done`
  → SKILL.md **6**, PROVINCE.md **1**, combined pipeline **7**.
  The seven lines, read in full: SKILL.md:3 (its own description), :149 and :183 (internal
  citations `SKILL.md:47` of its own rules), :161 ("not its trigger" — typed-label routing
  in a culture packet), :645 ("register-triggered use" — register overlap in its own
  corpus), :729 ("the actual prompt's non-verbatim step-6 defect" — its own native-request
  evidence binding); PROVINCE.md:20 (the kotoba refusal). Adding `|kotoba` to the pattern
  leaves the same 7 lines. Not one of them asserts authority over another lane's skill,
  prompt or AGENTS.md.
- Supporting negatives: `git grep -lci 'frontmatter' <c> -- tools/` → no paths, exit 1;
  `git grep -n 'SKILL\.md' <c> -- 'tools/*.py'` → one hit, `tools/gates/argot-derivation-gate.py:4`
  (docstring: "Spec: `SKILL.md` \"Derivation replay …\""); `git show <c>:SKILL.md | sed -n
  '509,521p' | grep -c kotoba` → `0` (hard-boundary section omits kotoba).

Quotes (step 6):
1. Scope — `SKILL.md:8-10`, 21 words, line breaks collapsed, bytes as shown by `cat -A`
   (lines end `myths,` / `fictional` / `world —`):
   "Domain: the generative craft that connects languages, cultures, myths, symbolisms, and
   eras to their linguistics and costumes for a fictional world"
   Word count: `git show <c>:SKILL.md | sed -n '8,10p' | tr '\n' ' ' | sed 's/ — .*//' | awk '{print NF}'` → 21.
2. Boundary (not required for `none`, recorded for § Adjacent) —
   `reports/round-33/adj/A01-province.md:75`, 8 words:
   "Lane-operating craft rules ≠ kotoba's cross-lane skill craft"
   (file sha256 `e22f2d03ce5b59d3b8faa9173dfc2410e24e322598e51541bd55c502e87cfcce`, last touched
   `da68a6d705e41f369f21e8607bfaab5b54077f84`, 2026-10-19T03:52:53-03:00).
   Its companion line in `MINT.md:20`, 9 words: "kotoba owns prompt/skill craft despite its
   name".

## Confirmations and gaps

- Confirmed by read: frontmatter, Domain/Owns/Refuses/write-scope, hard boundaries,
  checklist, the 7 sweep lines, the 68 kotoba paths, the absence of a skill/prompt
  instrument in `tools/`.
- Inference (marked): "no cross-lane claim" rests on the sweep plus the write-scope clause
  plus the absence of a `tools/` skill reader; I did not read all 1857 report files. A
  falsifier wanting read proof should sweep `reports/*/adj*` (I read rounds 11, 19, 25, 26,
  33 only — the five that mention kotoba).
- Not established: whether kotodama's round prompts ever drifted toward kotoba-style
  fidelity boxes (its `tools/check-gate-battery.py`, `check-claim-separability.py`,
  `check-readme-heading.py` gate its *own* round protocol and README index, which kotoba's
  Core does not claim). Left open rather than asserted.
- Not run by design: no builds, no linters, no lane verifiers.

Tooling: nothing installed or upgraded this seat (pacman host-wide paused; no `uv`/`npx`
needed). Tools used: git (system), GNU grep/sed/cat/awk/wc/sha256sum.
