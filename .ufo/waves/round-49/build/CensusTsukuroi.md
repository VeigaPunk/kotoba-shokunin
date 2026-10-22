ROW | tsukuroi | master (detached HEAD, same commit) | 22fd1642e7fa4dfbdfba4419a443f06ffbb0b6c0 | SKILL.md | none | no | no | PROVINCE.md:3 | "**Domain:** host operability & system repair (繕, mending) — the OS substrate itself: package state, systemd, drivers/firmware, boot health."

# Round 49 C1 — sibling-overlap census: tsukuroi-shokunin

Date 2026-10-22. Seat KotobaR49.CensusTsukuroi (leaf, no dispatch). Lane kotoba-shokunin
read-only except this file; tsukuroi-shokunin read-only throughout via
`git -C … show/ls-tree/rev-parse/grep/log`. No jj, no git write, no pacman, no tool installed.

## Findings

1. **Classification `none`.** tsukuroi's whole declared surface is OS state and health:
   package state, systemd user units, journal/boot triage, driver/firmware, update-safety
   (PROVINCE.md:3-14). None of kotoba's Core surfaces (SKILL.md trigger/frontmatter craft,
   anatomy and compression, decision tables, the four fidelity checklists; agent-definition,
   always-on and dispatch-prompt craft; the executable instruments over them) appears as an
   owned or refused object. The word `kotoba` appears **0** times in both SKILL.md and
   PROVINCE.md at the pin.
2. **No cross-lane craft rule and no arbitration against kotoba.** Its Refuses line routes
   endpoint health → kama, secrets → kagi, binary RE → kaidoku/revenger (PROVINCE.md:25-28).
   Its seven-row handoff table (ADJ-01..07, PROVINCE.md:44-52) names kama, kagi, mado, mori,
   kumitate, "protocol integrator — kaidoku/revenger", tameshi. kotoba is in neither list,
   and the only arbitration text (PROVINCE.md:79-80) is kaidoku-versus-revenger, deferred.
3. **Frontmatter is four lines and bare.** `name: tsukuroi-shokunin`; `description: Domain
   specialist — host operability & system repair. Rank: shonen (probation).` No lane named, no
   trigger clause, no sibling arbitration rule, so the ROW's arbitration field is `no`.
4. **No instrument over kotoba's surfaces.** `tools/` holds 26 files; 0 match
   `prompt|skill|frontmatter` and 0 match `agent|dispatch`. The nearest structural tool,
   `tools/check-appended-notices.py`, verifies append boundaries and notice sections of
   *its own* `SKILL.md` blob (`tools/check-appended-notices.py:83`, `:397`) against an
   immutable Git baseline; it enforces no
   frontmatter, trigger, anatomy or fidelity rule, so it is self-ledger discipline, not craft.
5. **Three nearest touches, all consumption or lane-local policy — none is a claim:**
   (a) SKILL.md:207-209 names `kama-shokunin/SKILL.md` as a "Shape model … decision table +
   checklist + cited sources" and cites the fleet `PROTOCOL.md` file contract;
   (b) R22 seat boundary (`corpus/knowledge/seat-boundary-r22.md:22`: "A prompt-level binding
   fixes exact read/write paths and empty command/fetch lists before dispatch") constrains
   *its own* dispatch prompts, states the limit in `tools/check-boundary-contract.py:25`
   ("Prompt policy and post-hoc request classification only") and cedes enforcement at
   SKILL.md:2165 ("Full native enforcement belongs to kumitate/operator runtime authority");
   (c) `corpus/knowledge/executor-test-sufficiency.md:187` mentions kotoba only inside a
   list of other lanes' historical logs. None of the three writes, audits or arbitrates a
   SKILL.md, prompt or AGENTS.md belonging to another lane.
6. **Tree-wide `kotoba` mentions exist but are incidental (10 files).** They are lane-report
   citations (`.ufo/waves/round-19/build/ConnWritersMori.md`,
   `.ufo/waves/round-19/build/InClass013.md`,
   `.ufo/waves/round-19/falsify/FxInRes02.md` citing
   `kotoba-shokunin c61a973b…:.ufo/round-22/scouts/A6.md:47`), the round-19 pointer JSONs
   (`.ufo/waves/round-19/l1-capture/adjacency-pointers-r19.json` and `.v1.json`), a captured
   sibling PROVINCE that names kotoba
   (`.ufo/waves/round-19/l1-capture/siblings/kumitate/1770305fae20/PROVINCE.md:27`,
   "Prompt and skill craft → kotoba" — a quoted sibling cession, not tsukuroi's rule), the
   IN-021
   pointer rows (`corpus/knowledge/adjacency-anchors-r19.md:116`, `.json:570`), one corpus
   note list (`corpus/knowledge/executor-test-sufficiency.md:187`, see 5(c)), and a fleet
   misroot sweep line (`.ufo/waves/round-22/measure/fleet-misroot-sweep.txt:7`). No ownership
   statement in any of the ten.
7. **Census implication for C1 (fact, not this row's judgment).** At kotoba `a5adc146`,
   `PROVINCE.md` § Adjacent has 6 bullets naming 10 of the 20 sibling lanes; tsukuroi is not
   among them. This row supplies the missing tsukuroi entry with classification `none`.
8. **Reclassification falsifier.** If the census counts lane-local policy over a lane's own
   dispatch-prompt scope as a shared prompt surface, this row flips to `adjacent` (kotoba:
   wording; tsukuroi: own-seat scope bindings) — a taxonomy ruling, not an evidence gap. Any
   future tsukuroi tool validating frontmatter, trigger text or SKILL.md anatomy would move
   it to `contested`.

## Evidence

Pin (working tree is detached at the same commit as master):

```
$ git -C /home/vgpnk/Projects/shokunin/tsukuroi-shokunin rev-parse master
22fd1642e7fa4dfbdfba4419a443f06ffbb0b6c0            exit 0
$ git -C … symbolic-ref -q HEAD                     exit 1  (detached)
$ git -C … rev-parse HEAD                           exit 0  → 22fd1642…b6c0
$ git -C … branch --contains 22fd1642…              → "* (no branch)" and master
$ git -C … log -1 --format='%H %ci %s' 22fd1642…
22fd1642e7fa4dfbdfba4419a443f06ffbb0b6c0 2026-10-22 05:59:42 -0300 round-24: land C1 hardened per-cause report, C2 pause-lift gate entry with 17 sources, criteria 54-56, SKILL table and registry, wave-1 evidence
```

Tree at the pin:

```
$ git -C … ls-tree --name-only 22fd1642…   exit 0
.gitignore .ufo AGENTS.md LOG.md MINT.md PROVINCE.md SCORECARD.md SHONEN.md SKILL.md
considerthese corpus plans reports tools
$ git -C … ls-tree -r --name-only 22fd1642… | grep -E '^(skills?/[^/]+/)?SKILL\.md$'
SKILL.md                                     exit 0  (exactly one; no skills/ directory)
```

Pinned bytes:

```
$ git -C … rev-parse 22fd1642…:SKILL.md      58e1c119ccc4574820f19d8f3b7934f1ef3d2138
$ git -C … rev-parse 22fd1642…:PROVINCE.md   e1787e38f83e4c6d6232256fe2b28df1aa4f3bca
$ git show 22fd1642…:SKILL.md    | wc -lc    2285 / 261104
$ git show 22fd1642…:PROVINCE.md | wc -lc     152  / 16727
$ git show 22fd1642…:SKILL.md    | sha256sum 679235a1472810b13a03206f7b7f32dd6f5bd8bd44ceee6e75544f64c40a0317
$ git show 22fd1642…:PROVINCE.md | sha256sum a296da872e83731f7f7a7737662988558ebb97e4399681a1099fab4a259b7a79
```

Counts (every number carries its command):

```
$ git show 22fd1642…:SKILL.md    | grep -c kotoba     0   exit 1
$ git show 22fd1642…:PROVINCE.md | grep -c kotoba     0   exit 1
$ git grep -l kotoba 22fd1642…  | wc -l              10   exit 0
$ git -C … log --all --oneline --grep=kotoba | wc -l  0   exit 0
$ git -C … ls-tree -r --name-only 22fd1642… tools | wc -l                        26 exit 0
$ git -C … ls-tree -r --name-only 22fd1642… tools | grep -icE 'prompt|skill|frontmatter'  0 exit 1
$ git -C … ls-tree -r --name-only 22fd1642… tools | grep -iE 'prompt|skill|frontmatter|agent|dispatch'  no output, exit 1
$ git -C … ls-tree -r --name-only 22fd1642… | grep -ic protocol                         0 exit 1
```

Negative sweep behind finding 1/5 (`none` requires it) — combined pattern over the seven
top-level markdown files at the pin:

```
$ for f in SKILL.md PROVINCE.md AGENTS.md MINT.md SHONEN.md SCORECARD.md LOG.md; do
    git show 22fd1642…:$f; done | grep -cE 'SKILL\.md|prompt|AGENTS\.md|frontmatter|trigger|description|kotoba'
81                                            exit 0   (per file: 27 / 2 / 0 / 0 / 2 / 23 / 27)
```

All 81 were read line by line: self-references to its own `SKILL.md` (`SKILL.md:118`,
`SKILL.md:217-220`, `SCORECARD.md:25-27` history, `LOG.md:9,54,75,201`), host-plane wording
("boundary trigger" `PROVINCE.md:44`, "Record the trigger" `PROVINCE.md:56`, unit
`LastTrigger`), dispatch-scope accounting ("prompt scope", "prompt bindings",
`invalid_prompt`: `SCORECARD.md:672-722`, `LOG.md:968`), `SHONEN.md:5-6` rank criteria over
its own file, and its own description line. Zero name kotoba, and none states a craft rule
binding another lane's SKILL.md, prompt or AGENTS.md. The `SHONEN.md:5` line ("SKILL.md
contains real decision tables, error patterns, checklists, cited sources") is a self-promotion
criterion, not an audit of anyone else's file.

Scope quote (19 words; `git show 22fd1642…:PROVINCE.md | sed -n '3,4p' | tr '\n' ' ' | wc -w`
→ 19), verbatim across PROVINCE.md:3-4, start locus `PROVINCE.md:3`:

> **Domain:** host operability & system repair (繕, mending) — the OS substrate itself: package state, systemd, drivers/firmware, boot health.

Nearest-touch quote (not an overlap; consumption of the file contract), SKILL.md:207-208:

> - Shape model: `kama-shokunin/SKILL.md` (sibling lane, distilled form: decision table + checklist + cited sources). Fleet conventions: PROTOCOL.md file contract (`SKILL.md` = craft + cited sources; …

## Remaining unknowns

- Whether the fleet `PROTOCOL.md` named at SKILL.md:208 assigns SKILL.md craft to any lane:
  PROTOCOL.md is not in this repo's tree at the pin (`ls-tree` above), so that question needs
  the fleet-root copy and is outside this row.
- Kotoba-side `PROVINCE.md` § Adjacent currently names 10 of 20 siblings; the 10 missing
  lanes are other seats' rows, not adjudicated here.
