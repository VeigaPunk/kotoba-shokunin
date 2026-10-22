ROW | kagi | master (detached HEAD, same commit) | 899c50b42634a3a4ad0b28ab7509786315e2fc2b | SKILL.md | adjacent | no | no | PROVINCE.md:3 | "secrets & vault ops — the-janitor flows, credential hygiene evidence"

# Round 49 C1 — sibling-overlap census: kagi-shokunin

Date 2026-10-22. Seat KotobaR49.CensusKagi (leaf, no dispatch). kotoba-shokunin read-only
except this file; kagi-shokunin read-only throughout through `git -C … show/ls-tree/
rev-parse/grep/log`. No jj, no git write, no pacman install, no web fetch this session.

## Findings

1. **Classification `adjacent`** — the always-on (`AGENTS.md`-class) surface and the
   `~/.config/opencode` instruction/agent surface are the shared boundary, and each lane
   owns a different half. kagi's half: byte pins, mode/shape census, credential and
   request hygiene on the handler-reaching children. kotoba's half: the checklist/shape
   reading and the instruction/agent surface content.
2. **Not `contested`, because the split is declared on kagi's side and machine-checked.**
   `corpus/adjacency.tsv:84` gives `$HOME/.agents/AGENTS.md` `owner=kotoba`,
   `status=shared-read`: "byte-pinned here; kotoba is the sole fleet claimant of the
   file's checklist/shape reading (read-only for both lanes)"; `corpus/README.md:97`
   states the same split in prose. kagi does not claim to write or audit SKILL.md,
   prompts or AGENTS.md for any other lane.
3. **The one group kagi leaves open names kotoba too, and kagi narrows itself out of
   kotoba's half.** `corpus/README.md:96` / `corpus/adjacency.tsv:81`:
   `$HOME/.config/opencode` is `owner=integrator, status=unresolved`; the note says
   "kotoba owns the instruction/agent surface … kagi claims credential/request hygiene on
   those children only" (4 of the group's 20 children reach the handler). Adjacent with a
   real unsettled ownership question beside it; the census entry must not restate that
   group as settled.
4. **Frontmatter description carries neither kotoba nor an arbitration clause.**
   `git show 899c50b:SKILL.md | sed -n '3p' | grep -cE 'kotoba|arbitrat|sibling'` → `0`,
   exit 1. The description is "Domain specialist — secrets & vault ops — the-janitor
   flows, credential hygiene evidence, vault lifecycle. Rank: shonen."
5. **`PROVINCE.md` does not name kotoba**: `git show 899c50b:PROVINCE.md | grep -c
   kotoba` → `0`, exit 1. Its § Adjacent names chousa, kasegi, kumitate, kama, kaidoku,
   tsukuroi, kake; its contested row is the musketeer profile against kake, not kotoba.
   So the kotoba boundary is recorded in kagi's corpus, not in its province or frontmatter.
6. **A top-level-only sweep would misclassify kagi as `none`; the corpus is where the
   arbitration lives.** Over the four pinned top-level docs (SKILL.md, PROVINCE.md,
   AGENTS.md, README.md) the plan's sweep matches 15 lines and `kotoba` exactly 1 line
   (`SKILL.md:297`, a citation-defect description: "one kotoba path wearing this repo's
   anchor"). Tree-wide, `kotoba` appears in 17 files (`:(exclude).ufo`). Census consequence:
   the entry's `recheck:` for a `none` row must cover `corpus/`, otherwise the negative is
   unsound — record this as a method rule, not just a kagi fact.
7. **kagi's agent-frontmatter statements are runtime precedence, not craft.**
   `corpus/knowledge/config-layering.md:21` and `corpus/lessons/round-6.md:38` record that
   `agents/janitor.md` frontmatter wins `agent.janitor` wholesale and beats JSON `agent.*`
   blocks. That is substrate behaviour inside kagi's handler trust boundary, not guidance
   on how to author an agent definition; it is the nearest thing to kotoba's core and it
   stays on kagi's side of the line.
8. **Shared vocabulary is not shared ownership.** `README.md:12` describes its own
   `SKILL.md` as "the distilled expertise: decision tables, error patterns, checklists".
   Same anatomy words as kotoba's Core, applied to its own repo layout; no claim over
   skill craft as a discipline.
9. **Seam to state in kotoba's PROVINCE.md § Adjacent:** "kagi — secrets & vault ops;
   adjacent on the always-on surface: kagi byte-pins `~/.agents/AGENTS.md` and owns
   credential/request hygiene on the 4 handler-reaching `~/.config/opencode` children,
   kotoba owns the checklist/shape reading and the instruction/agent surface; the
   opencode group's single-owner ruling stays with the integrator."

## Scope quote (step 6, first)

`PROVINCE.md:3` at `899c50b` — verbatim, one physical line, 11 words: "**Domain:** secrets & vault ops — the-janitor flows, credential hygiene evidence". `grep -cF` of that whole line against the pinned file → `1`, exit 0. The ROW field quotes the same line minus the markdown emphasis, "secrets & vault ops — the-janitor flows, credential hygiene evidence" (10 words), also `grep -cF` → `1`.

## Overlap quote (step 6, second, classification adjacent)

`corpus/README.md:97` at `899c50b` — verbatim, one physical line, 16 words: "kagi pins its bytes; kotoba owns the checklist/shape reading — no adjudication needed, both are read-only". `grep -cF` against the pinned file → `1`, exit 0; located by `grep -nF 'kagi pins its bytes'` → line 97.

## Evidence

Pin (step 1):
- `git -C /home/vgpnk/Projects/shokunin/kagi-shokunin rev-parse master` → exit 0,
  `899c50b42634a3a4ad0b28ab7509786315e2fc2b`.
- `git … symbolic-ref -q HEAD` → exit 1, `fatal: ref HEAD is not a symbolic ref`;
  `git … rev-parse HEAD` → the same 40-hex (exit 0); `git … branch --show-current` →
  empty. Pin is master's tip, checked out detached. `git log -1 --format='%ci %an %s'` →
  `2026-10-21 15:23:29 -0300 kagi-shokunin round-28: measured outcomes, strict receipt
  audit and honest frozen-fixture conformance`.

Skill files (step 2):
- `git … ls-tree --name-only 899c50b` → `.gitignore .ufo AGENTS.md LOG.md PROVINCE.md
  README.md SCORECARD.md SHONEN.md SKILL.md considerthese corpus plans` (12 rows, exit 0;
  note: `plans`, not `scripts`).
- `git … ls-tree -r --name-only 899c50b | grep -E '^(skills?/[^/]+/)?SKILL\.md$'` →
  `SKILL.md` (exit 0, exactly one). Recursive `grep -E 'SKILL\.md$'` also returns five
  sandbox copies under `.ufo/waves/round-27/sandboxes/*/base/SKILL.md`; the canonical
  skill path is the top-level one.
- `git … ls-tree -r --name-only 899c50b | wc -l` → `3189` (exit 0).

Sweep (step 4, run because the row must carry its negative/positive coverage):
- Four pinned docs, plan pattern: `for f in SKILL.md PROVINCE.md AGENTS.md README.md; do
  git … show 899c50b:$f; done | grep -cE 'SKILL\.md|prompt|AGENTS\.md|frontmatter|trigger|
  description|kotoba'` → `15` (exit 0). Per pattern: `SKILL\.md` 5, `prompt` 4,
  `AGENTS\.md` 1, `frontmatter` 2, `trigger` 0, `description` 2, `kotoba` 1.
- Control arm (pipeline can match, Q05/Q18): the same four files `grep -c vault` → `26`;
  tree-wide `git … grep -c vault 899c50b -- . ':(exclude).ufo'` summed → `323`.
- Tree-wide, pattern `:(exclude).ufo` summed → `367` lines in `86` files; `kotoba` alone →
  `17` files. With `.ufo` included the pattern sums to `7246` lines (sandbox trees).
- Per-file `kotoba`: `SKILL.md` 1, `PROVINCE.md` 0, `AGENTS.md` 0, `README.md` 0
  (`git show 899c50b:$f | grep -c kotoba`, exits 0/1/1/1).

Boundary rows read at the pin:
- `git show 899c50b:corpus/adjacency.tsv | sed -n '81p'` (opencode group, integrator,
  unresolved) and `'84p'` (`$HOME/.agents/AGENTS.md`, kotoba, shared-read).
- `git show 899c50b:corpus/README.md | sed -n '94,98p'` (overlap table), same at
  `corpus/knowledge/adjacency-scope.md:60-80` (group table) and `corpus/surface-census.tsv:55`
  ("shared with kotoba (always-on checklist surface); bytes pinned here").
- `git show 899c50b:LOG.md | sed -n '181p'` — the same seam reported to the integrator:
  "`~/.agents/AGENTS.md` is also audited by kotoba" (adjacency, not absorbed).

Hashes of the pinned docs (`git show 899c50b:$f | sha256sum`):
- `SKILL.md` f1c59e552f4ed48ad5a16cd530a048b6590f320a9c33330a08ca4ff5e52e31d2
- `PROVINCE.md` 5edd4f1b134d1cf3b4434239478e168bcc535e02fcfa31bc354dabec4650bb02
- `AGENTS.md` c62ffaf4e92d50e4abb75227f068455c77597d23d723ef814e180fedbe029891
- `README.md` add2a5169e472b33d147610963a6ea052d6a4f6aa8b398e75000fd5942f68733

Not run (not this seat's assignment): no lane verifier, no kotoba test, no network fetch.
No tool installed or upgraded.

## Remaining unknowns

- The `$HOME/.config/opencode` single-owner ruling is owed to the integrator at kagi's
  side; whether kotoba's PROVINCE § Adjacent should carry that group as `unresolved`
  rather than as a plain adjacent split is for the L1 (I recommend "adjacent on the
  AGENTS.md half; opencode group unresolved, integrator owes the ruling").
- Whether kagi's `scope-gate.sh` still passes at this pin was not exercised (host-surface
  and credential gates; out of this seat's scope and partly host-state dependent).
- The census entry's `recheck:` script must read `corpus/README.md:97` and
  `corpus/adjacency.tsv:84`; a recheck limited to the four top-level docs cannot
  reproduce this classification (finding 6).
