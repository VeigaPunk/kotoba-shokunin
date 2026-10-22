ROW | kaidoku | main (detached HEAD) | 08c7a7299ed61c3fdc30ddb0adfe4e812d5eac76 | SKILL.md | none | no | no | SKILL.md:3 | "Domain specialist — reverse engineering of shipped artifacts with REA on this Linux host"

# Round 49 C1 — sibling-overlap census: kaidoku-shokunin

Date 2026-10-22. Seat KotobaR49.CensusKaidoku (leaf, no dispatch). Surface
`/home/vgpnk/Projects/shokunin/kaidoku-shokunin`, read-only through
`git -C … rev-parse/symbolic-ref/ls-tree/show/grep/for-each-ref`. No edit, no jj, no git write,
no pacman transaction, no tool install (nothing was needed).

## Findings

1. **Pin.** `master` does not exist in kaidoku. HEAD is detached at
   `08c7a7299ed61c3fdc30ddb0adfe4e812d5eac76`, which is the tip of its only live branch `main`.
   The working tree is dirty from a different seat (`M corpus/lessons/round-25.md`,
   `?? .ufo/waves/round-25/a3/`), so every read below is a committed blob at the pin, never the
   working tree.
2. **Skill file.** Exactly one real lane skill: `SKILL.md` at the repo root (832 lines, blob
   `118f11cf…`). The recursive SKILL.md regex matches only that path; the 31 tracked paths named
   `SKILL.md` include 30 under `.ufo/waves/**` (RE attack fixtures and patch trees), not lane
   skills. There is no `skills/` directory.
3. **Own scope.** PROVINCE.md Domain (lines 3–6) and its Core table (19 surface rows,
   `git show 08c7a729:PROVINCE.md | sed -n '44,62p' | grep -c '^|'` → 19) scope the lane to
   reverse engineering of shipped artifacts with the `rea` MCP/CLI and the Ghidra 12.1.4
   provider: ELF/PE, Electron/ASAR/JavaScript, APK, archives, firmware, managed assemblies,
   recorded crashes, WASM, pcap. Its § Adjacent refusals are malware triage at scale, non-REA
   dynamic analysis (gdb/strace/Frida), source-available reconstruction of ordinary repos,
   engine/config installation, and quality/safety verdicts. No prompt, skill-file or
   AGENTS.md-authoring surface appears anywhere in the province.
4. **Classification `none` against kotoba's Core.** The sweep required for a `none` row returns
   7 matches over the six governance files, and not one of them claims prompt/skill/AGENTS.md
   craft: SKILL.md:3 is its own `description:` frontmatter line; SKILL.md:736–737 are REA verb
   names (`round23-signal-description`, `round23-dart-description`); PROVINCE.md:107 is "anti-trigger"
   referring to *its own* frontmatter scope gate; README.md:12 is repo layout ("`SKILL.md` — the
   distilled expertise"); SHONEN.md:5–6 is its own promotion checklist citing its own SKILL.md.
   The terms `prompt`, `AGENTS.md`, `frontmatter` and `kotoba` have **0** matches in those six
   files.
5. **Nearest approach, still `none`.** kaidoku curates RE method *out of* a shipped skill
   package: `corpus/knowledge/2026-10-13-rea-skill-contract.md` studies
   `~/.agents/skills/reverse-engineer-anything/` (SKILL.md v37 plus six references) and admits
   or rejects RE candidates from it. That is domain content inside a skill, which kotoba
   explicitly refuses ("kotoba refuses domain content inside other skills"); it touches no
   kotoba Core surface (trigger craft, anatomy/compression, decision tables, fidelity
   checklists, AGENTS.md or dispatch-prompt craft, the instruments over those).
6. **Reciprocal classification, recorded by the sibling itself.** kaidoku's own overlap census
   `.ufo/waves/round-14/w1/SiblingOverlap.md:21` classifies kotoba as "Zero overlap. `kaidoku`
   owns its domain Go decision table addendum; `kotoba` owns meta-skill craft", and
   `.ufo/waves/round-18/w1/ConnSiblingOverlap.md:50` records kotoba routing shipped-artifact RE
   to revenger. Two independent seats, opposite directions, same verdict.
7. **Description: no kotoba, no arbitration rule.** The frontmatter description names no sibling;
   its only boundary clause is a generic anti-trigger ("ordinary source repositories — use
   normal repo tools, never run REA on available source"). The lane body does carry a *named but
   explicitly open* arbitration against **revenger** (SKILL.md:677, SKILL.md:722,
   PROVINCE.md:240, :272–273, :303) — a cross-row note for the revenger row, not a kotoba clause.
   The only place kaidoku's repo writes kotoba's name in its own material is
   `EXAMPLE.kama.md:51`, a verbatim evidence copy of kama's MINT.md table row
   "| kotoba | prompt & skill craft | instruction surfaces, not services |".
8. **Cross-row flag for the census (report, do not adjudicate).** kaidoku's PROVINCE.md:3 claims
   "reverse engineering of shipped artifacts" in the same words kotoba's `PROVINCE.md:34` today
   assigns to revenger. Once kaidoku's row is added, kotoba's § Adjacent phrase "shipped-artifact
   RE" names two live lanes whose own arbitration is open (kaidoku SKILL.md:677: "The
   kaidoku/revenger dynamic-analysis boundary remains an open L0 question"). kotoba should
   record both classifications and point at that open question rather than resolve it.

## Evidence

Pinning (cwd `/home/vgpnk/Projects/shokunin/kaidoku-shokunin`):

- `git rev-parse master` → `fatal: ambiguous argument 'master'` , exit 128.
- `git symbolic-ref -q HEAD` → no output, exit 1 (detached).
- `git rev-parse HEAD` → `08c7a7299ed61c3fdc30ddb0adfe4e812d5eac76`, exit 0.
- `git for-each-ref --format='%(refname:short) %(objectname:short)' refs/heads` → `main 08c7a729`
  as the only branch at that object; exit 0.
- `git status -sb` → `## HEAD (no branch)`, ` M corpus/lessons/round-25.md`, `?? .ufo/waves/round-25/a3/`.

Skill files:

- `git ls-tree --name-only 08c7a729` → `AGENTS.md EXAMPLE.kama.md LOG.md MINT.md PROVINCE.md
  README.md SCORECARD.md SHONEN.md SKILL.md corpus evidence tools` (plus `.gitignore`, `.ufo`); exit 0.
- `git ls-tree -r --name-only 08c7a729 | grep -E '^(skills?/[^/]+/)?SKILL\.md$'` → `SKILL.md` only; exit 0.
- `git ls-tree -r --name-only 08c7a729 | grep -c 'SKILL\.md'` → 31 (30 under `.ufo/`); exit 0.
- Blobs at the pin: `git rev-parse 08c7a729:SKILL.md 08c7a729:PROVINCE.md 08c7a729:README.md` →
  `118f11cfac77f930ba5630ff4d8e01c8bef2165b`, `306e35912ff3d129aa5ec15956fb6a5dafd683a0`,
  `b21d9946221e2ed2a9aee6ff80cf282f4577bdb9`; exit 0. Line counts 832 and 303.
- Frontmatter: `git show 08c7a729:SKILL.md | sed -n '2p'` → `name: kaidoku-shokunin`; line 3 is
  the description, 624 bytes, sha256 `d6fd799dbb7bdc43e404ef7e5f709b930fe932c4e9c21f8f8c155df653b04b4d`.
  The row quote is a verbatim prefix of that line (`… | grep -c '<quote>'` → 1, exit 0), 13 words.

Sweep for the `none` row (exact command, count):

- `git grep -E 'SKILL\.md|prompt|AGENTS\.md|frontmatter|trigger|description|kotoba' 08c7a729 -- SKILL.md PROVINCE.md AGENTS.md README.md MINT.md SHONEN.md | wc -l`
  → **7**, exit 0. Per file (`git grep -cE …`): `PROVINCE.md:1`, `README.md:1`, `SHONEN.md:2`,
  `SKILL.md:3`, `MINT.md` and `AGENTS.md` absent from the output (0 each).
- Per term over the same six files (`git grep -E '<term>' … | wc -l`): `SKILL\.md` 3, `prompt` 0,
  `AGENTS\.md` 0, `frontmatter` 0, `trigger` 2, `description` 3, `kotoba` 0.
- Breadth variant: same pattern over the whole tracked tree minus `.ufo/`
  (`git grep -nE '…' 08c7a729 -- . ':!.ufo' | wc -l`) → 273, exit 0; the hits are corpus lessons,
  `corpus/QUALITY.md`, source rows and RE knowledge files, none asserting skill-craft ownership.
- `kotoba` occurrences repo-wide: `git grep -l kotoba 08c7a729 | wc -l` → 21 files, of which 20
  are `.ufo/**` wave reports; outside `.ufo` only `EXAMPLE.kama.md:32,51` (verbatim kama MINT
  copy). Written-doc count: `git show 08c7a729:SKILL.md | grep -c kotoba` → 0;
  `git show 08c7a729:PROVINCE.md | grep -c kotoba` → 0.

Quotes used above:

- SKILL.md:677 → `The kaidoku/revenger dynamic-analysis boundary remains an open L0 question.`
- README.md:12 → ``- `SKILL.md` — the distilled expertise: decision tables, error patterns,``
- PROVINCE.md:107 → `  anti-trigger `(unowned)`.`
- `.ufo/waves/round-14/w1/SiblingOverlap.md:21` (kotoba row, verbatim tail): "Zero overlap.
  `kaidoku` owns its domain Go decision table addendum; `kotoba` owns meta-skill craft."

## Unknowns

- The pin is a blob pin, not a head claim: another seat is actively committing in kaidoku
  (round-25 dirty tree), so `main` may advance past `08c7a729`. This row is valid at the pin only.
- Whether the 30 `.ufo` SKILL.md attack/patch trees encode any reusable skill-craft lesson is not
  assessed; they are RE test fixtures and outside this row's question.
