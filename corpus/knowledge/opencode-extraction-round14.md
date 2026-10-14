# opencode instruction-class extraction — round 14

> **2026-10-14 errata (round 18, append-only).** The opencode substrate moved:
> the v1 OC-1…OC-5 rule set no longer has anchors in the live binary (dump
> `d9123b9b…`, opencode v2.0.26), and `InstructionContext.observe` /
> `system-context-builtins` / `core/instructions` are gone. The subsystems
> described below are **historical**: they were true of the round-14 binary and
> are preserved verbatim as the round's evidence. The current rule set —
> OC-1…OC-6 over `ConfigInstructionPlugin.projectSource`, `ReadTool.Plugin`,
> the API-managed instruction entries and an env-gate — is the round-18
> re-derivation recorded in `instruction-surface-census-round13.md` § B
> (errata block) and `verifiers/verify_surfaces.py`.

**Claim (the round's axis move, coverage 8.0 → 8.5).** The instruction-surface
inventory's machine check is no longer vacuous for the **opencode** harness:
opencode's instruction classes are now **derived from code shapes in its shipped
bundle** by seven named, fail-closed rules, and the check refuses both directions of
vacuity. Round 13 landed the inventory and its checker but recorded the gap
verbatim — *"For opencode the check is vacuous by construction — its loaders are
arrays/join/findUp/globUp, so `surfaces.no_uncovered_class` extracts zero pairs
there and cannot fail"* (`instruction-surface-census-round13.md` § Honest
ceiling). This file is the closing evidence for that sentence.

**Scope of the claim (stated first, because it is narrower than it sounds).** The
check proves that a **documented extraction rule set** reproduces the declared
opencode class set and that every rule's anchors are present — never existential
completeness of opencode's instruction surfaces. Rules key on the shapes below; a
loader minified differently, or reached through a variable the dump resolves
differently, stays outside the set. What changed is that "outside the set" is now
a *named* boundary with a drop-one matrix, not an admitted hole in the check.

## The rules (instrument: `verifiers/verify_surfaces.py`, `extract_opencode_classes`)

Anchors are quoted as **shapes** (`<v>` for the minified variable the dump
resolves), never as offsets or `strings` line numbers. "Derives" means the rule
reads the class identity out of the shape; "witness" means the shape is the
loader's fingerprint and the id is the census's name for it.

| Rule | Anchor shape (verbatim literals) | Class ids | Kind |
|---|---|---|---|
| OC-1 | `["AGENTS.md"` … `"CONTEXT.md"]` (name-priority array), gated element `disableClaudeCodePrompt?["CLAUDE.md"]` | `opencode:instructions/{AGENTS,CLAUDE,CONTEXT}.md` | derives: every `*.md` literal in the array becomes an id |
| OC-2 | `X.join(<v>.config,"AGENTS.md")`; `X.join(<v>.home,".claude","CLAUDE.md")` | `opencode:config/AGENTS.md`, `opencode:claude-home/CLAUDE.md` | derives: group from the join path (`config`; `.claude` → `<dir>-home`), file from the literal |
| OC-3a | `for(let <v> of <v>.instructions)` | `opencode:config/instructions` | witness |
| OC-3b | `.instructions`…`startsWith("https://")`…`startsWith("http://")` **and** `` `Instructions from: ${…}` `` | `opencode:config/instructions-remote` | witness (two anchors, both required) |
| OC-4 | `fn("Instruction.resolve")` **and** `<system-reminder>` | `opencode:read-hook/instructions` | witness (both anchors required) |
| OC-5 | `OPENCODE_DISABLE_PROJECT_CONFIG` **and** `globUp(<v>.directory,<v>.worktree)` **and** `globUp(<v>.config,<v>.config)` | — (shape witness, owns no id) | witness: losing the project-vs-config switch FAILs rather than silently re-scoping where the ids are read from |
| OC-6 | `InstructionContext.observe` **and** `Key.make("core/instructions")` **and** `targets:["AGENTS.md"]` **and** `system-context-builtins` | `opencode:instruction-context/AGENTS.md` | witness: the **second** instruction subsystem — all-match ambient walk plus an ungated config-dir candidate, a different load condition for the same file class as OC-1, hence its own id |

### Why OC-6 exists (a gap the blind witness found)

The round's blind second witness (L2 lane `R14OcShapes`, seat scout, **never** read
the census or any other lane's scratch; binary re-hashed, dump reused with its
sha256 verified) enumerated opencode's instruction surfaces from the bytes and
found **two parallel subsystems**: v1 `@opencode/Instruction` (the target of
OC-1…OC-5) and v2 `instruction-context`, registered as the
`system-context-builtins` context under key `core/instructions`, walking
AGENTS.md **all-match** from cwd to the project root and keeping an **ungated**
`<config>/AGENTS.md` candidate. Round 13 described this split in § B **prose** but
gave it no class id, so the inventory's own claim ("every loader-derived class is
governed by a craft row or excluded with a reason") was overstated by one class.
Round 14 declares `opencode:instruction-context/AGENTS.md` as the ninth opencode
class, adds the census row, and pins it with OC-6. Live proof that the pin is
load-bearing: with OC-6 present but the id undeclared, the check FAILed on the
live tree with `extracted opencode class(es) undeclared in baseline:
opencode:instruction-context/AGENTS.md` (exit 1) — the fail-closed direction
working on real bytes.

The witness also confirmed the mechanical reason round 13 saw zero extracted
pairs: "opencode is NOT vacuous by construction for a rule that accepts
`join()`/`targets`/`glob` shapes, but IS vacuous for a rule restricted to omp's
array-group shape" (`local://round14-oc-shapes-scout.md`). Rule numbering differs
between lanes (the planner's OC-3 = the globUp switch, its OC-4 = the declared
list); the landed numbering above is authoritative and every cross-lane drop file
maps to it **by anchor, not by number** — recorded so a reader is not misled.

Rule registered as `surfaces.opencode_extract`, check id `surfaces.opencode_extract`
(the check is named for the harness, not for a rule; the rules are numbered
inside its detail line).

## What the check refuses (the anti-vacuity contract)

| Direction | Behaviour |
|---|---|
| Baseline declares an opencode id no rule produces | FAIL, naming the id and the rule(s) that own it |
| A rule produces an id the baseline does not declare | FAIL, naming the id |
| Any rule matches nothing | FAIL, naming the rule and the anchors it is missing |
| Extraction produces **0 classes at all** | FAIL with `vacuity:` — opencode is a target harness of this lane, so zero extracted classes is a broken rule set or a broken dump, never a pass |
| Section/inventory missing while ids are declared | handled by `surfaces.table_parity` / `surfaces.literal_parity` / `surfaces.kind_parity` |

Consequence: an **empty baseline** produces a FAIL that names every extracted
opencode class, and a **vanished anchor** produces a FAIL that names the class it
used to produce. Neither can pass on `0 == 0`.

## Falsifiers, run on the landed tree (2026-09-28)

Binary `sha256 f9dab32248695e9ebd56b16a1921798fd85112cf5a69c7dfd0cabc1e17be4a11`
(equal to `verifiers/baseline.json` `measured_against.opencode_binary_sha256`);
dump `strings -n 4` of `/home/vgpnk/.opencode/bin/opencode`,
`sha256 a7db30951351f16b821822e07c19cd55cb6ba300f6640f64dbb5b4c10eb7ac59`.
Non-author freshness re-check (L2 lane `R14CensusFresh`, reviewer seat):
18 census fragments re-derived against a fresh dump, both binary hashes exact
match — record `local://round14-census-freshness.md`.

| Case | Command | Result |
|---|---|---|
| live tree | `python3 verifiers/verify_surfaces.py` | **7/7 PASS, exit 0** (≈13 s); opencode detail `9/9 declared class(es) from 7/7 rules (OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6)` |
| fixtures | `python3 verifiers/verify_surfaces.py --self-test` | **0 failure(s) over 75 assertions**, exit 0 |
| empty baseline, live dumps | `--baseline verifiers/fixtures/surfaces/baseline-oc-empty.json` | exit 1; `FAIL surfaces.opencode_extract: extracted opencode class(es) undeclared in baseline: opencode:claude-home/CLAUDE.md, opencode:config/AGENTS.md, opencode:config/instructions, opencode:config/instructions-remote, opencode:instructions/AGENTS.md, opencode:instructions/CLAUDE.md, opencode:instructions/CONTEXT.md, opencode:read-hook/instructions, opencode:instruction-context/AGENTS.md` |
| OC-1 anchor deleted from a live dump copy | `--opencode-strings <copy> --check surfaces.opencode_extract` | exit 1; `declared opencode class(es) produced by no rule: …` |
| anchor-less dump | `--opencode-strings verifiers/fixtures/surfaces/strings-empty.txt --check surfaces.opencode_extract` | exit 1; `vacuity: extraction produced 0 class(es) from 6 rule(s) …` |
| anchor-bearing dump, empty baseline | `--baseline …/baseline-oc-empty.json`, fixture run in `--self-test` | exit 1; names 8 ids |

Drop-one coverage is complete in the fixtures: `strings-opencode-clean.txt`
carries all five anchor families, and `strings-opencode-drop-oc{1,2,3a,3b,4,5,6}.txt`
each remove exactly one rule's anchors. A second, independent drop-one matrix was
produced by L2 lane `R14DropOne` (labrat seat) with its own throwaway
fail-closed extractor over line-level dump copies: **9 runs, all 8 candidate
anchors load-bearing, no class survived removal of its anchor**, empty dump →
exit 1 naming all 8 (`local://round14-dropone.md`; recorded in the round report).

## Row-column parity: three of five census columns are now machine-checked

Round 13's mutation lane planted 13 faults, caught 11, and named two escapes: a
census row's **literal** cell or **evidence** cell rewritten still exited 0.
`surfaces.literal_parity` (round 14) closes the literal escape and
`surfaces.kind_parity` closes the same escape in the **kind** column — both have
exact machine counterparts in `verifiers/surfaces-baseline.json` and both are
compared per id:

| Case | Command | Result |
|---|---|---|
| census literal rewritten to `WRONG.md` | `--inventory <mutated copy> --check surfaces.literal_parity --check surfaces.table_parity` | exit 1; `FAIL surfaces.literal_parity: … omp:agents-md/AGENTS.md (line 47: census literal 'WRONG.md' != baseline literal 'AGENTS.md')`; `table_parity` still PASS — the new check is what catches it |
| census kind rewritten to another *legitimate* kind | `--inventory <mutated copy> --check surfaces.literal_parity --check surfaces.kind_parity --check surfaces.table_parity` | exit 1; `FAIL surfaces.kind_parity: … census kind 'loader-literal' != baseline context_kind 'loader-group'` |
| a declared id moved out of the row's first cell | fixture `inventory-id-not-first.md` | exit 1; `FAIL surfaces.literal_parity: line 9 carries class id(s) … outside the first cell — the literal comparison cannot be anchored` |

The two remaining columns (`governed by`, `evidence`) are **prose with no machine
counterpart** — the baseline carries no equivalent field, so a rewrite there is
caught by a reader, not by the checker. That residual is named, not smoothed
over: it is the boundary the round-14 mutation matrix reports (L2 lane
`R14MutationsPre`: 11 mutations, 3 escaped — evidence/kind/governed-by column
rewrites; `kind` was closed after that run by `surfaces.kind_parity`, so the
standing residual is the two prose columns).

## Ceilings (what this file does not claim)

- **Extraction, not injection.** A rule matching proves the loader **shape** ships
  in the binary; it is not proof that any file reached a prompt this session.
  Round 13's partial wire probe (§ A3 of the census) remains the only injection
  evidence, for one host state.
- **Extraction-set completeness.** The six rules are a documented set. Nothing
  here proves no other opencode instruction surface exists — only that every
  *declared* class has a load-bearing code-shape witness and that a rule which
  stops matching FAILs.
- **Derive-vs-witness.** OC-1 and OC-2 derive ids from the shape; OC-3a/b, OC-4,
  OC-5 and OC-6 witness a fingerprint and take the census's name for it. The
  distinction is stated per rule above rather than hidden in a single number.
- **Binaries move.** Every rule is anchored on this binary's bytes; a bundle
  rebuild that renames a minified variable breaks the *shape* (OC-1/OC-2 patterns
  use `[\w$]` wildcards where the live dump has `r`/`t`), but a rebuild that
  removes a loader is expected to FAIL, which is the point.
- **Host existence, provider priority, the two-subsystem split** — unchanged from
  the round-13 ceiling; not re-measured here.