verdict: PARTIAL — the machine-checked C1 after-count survives every attack (default and frozen-dump runs both exit 0, 7/7 PASS, byte-identical verdict payloads; the default opencode path IS the npx ELF at the pinned sha256 and the run's dumps are byte-identical to the frozen dumps), but the census-side record of the **omp** half of the round-47 re-derivation never landed: `corpus/knowledge/instruction-surface-census-round13.md` still cites call shapes that do not exist in omp 18.12.5 and still names the 2026-09-28 binary pair (F1), and its moved "superseded" rows carry a present-tense claim round 47 falsified (F2).

Lane: `KotobaR47-2.W2SurfacesRerun-2` (leaf, no subagents). Target: `verifiers/verify_surfaces.py` at
`7ad7fadfc09354b74fb66605dfb0c1182c115a2f`. Scratch clone: `/fast/scratch/kotoba-r47/w2/W2SurfacesRerun/kotoba-shokunin`
(+ `base` worktree at `c61a973`, + `mut` worktree at `7ad7fad`). All mutations happened in the scratch clone only; the
production tree was written nowhere except this report and `W2SurfacesRerun.{default,frozen}.json` under
`.ufo/waves/round-47/falsify/`.

---

## 0. What I attacked

1. The two required runs (default resolution; frozen dumps) — exit codes, PASS count, **byte-identical** verdict details.
2. The identity chain: default opencode path → npx ELF → sha256 = `SHA256SUMS` line → the bytes the run actually dumps.
3. Non-vacuity: is the 7/7 green load-bearing on the round-47 changes, or would it stay green without them?
4. Freshness/exhaustiveness of the omp extraction set on 18.12.5 (is a class hiding under an unallowlisted callee?).
5. Calibration of the corpus record the C1 claim names (`§ B′`, the round-47 ledger, the omp `§ A`).

---

## 1. FINDINGS

### F1 — MEDIUM (calibration): the census records no omp 18.12.5 provenance; its omp evidence cells cite shapes that do not exist in the current binary

**Where (path:line at `7ad7fad`):**
`corpus/knowledge/instruction-surface-census-round13.md`

- `:53-54` — "Binaries (2026-09-28): omp `sha256 55016ef5317af556…`, opencode `sha256 f9dab32248695e9e…`,
  **identical to the binary hashes `verifiers/baseline.json` records in `measured_against`**". That present-tense
  equality is now **false**: `verifiers/baseline.json:5` records `omp_binary_sha256 = fdbc8136…` and
  `verifiers/baseline.json:9` records `opencode_binary_sha256 = 179ca421…`.
- `:22` — the round-18 errata names the *previous* pair (omp `ff59fc1b48…` 2026-10-14 / opencode `d9123b9bcd…`);
  `:14` names that round's callee set (`Tl|dr|GW`, "allowlist re-pinned in the verifier").
- `:73-80` — every `§ A` (omp machine-extracted registrations) row cites a **dead** call shape:
  `jDe(e,Pqr,"AGENTS.md")`, `jDe(e,BWr,"CLAUDE.md")`, `Id(e,"opencode","AGENTS.md")`, `Id(e,"gemini","GEMINI.md")`,
  `Id(e,"gemini","system.md")`, `Cl(e,"gemini","GEMINI.md")`, `Cl(e,"gemini","SYSTEM_TEMPLATE.md")`,
  `Cl(e,"github","copilot-instructions.md")`, `Id(e,"windsurf","memories/global_rules.md")`.
  **None of these strings exists in the 18.12.5 dump.** The live shapes are
  `lq(u,f$,"AGENTS.md")`, `lq(u,m$,"CLAUDE.md")`, `Xl(u,"gemini",…)`, `Fo(u,"github",…)`, with
  `f$ = "agents-md"`, `m$ = "claude-md"`.
- `:146` and `:439` — the same dead `jDe(e,Pqr,"AGENTS.md")` / `Cl(e,"gemini","GEMINI.md")` shapes in § A3 and in the
  absorbed SKILL.md table row.
- `:365` — the Honest ceiling still says the call-shape regex misses "group names passed as variables other than the
  two resolved (`Pqr`, `BWr`)". The resolved variables on 18.12.5 are `f$`/`m$`; `Pqr` survives in the dump only as an
  incidental substring of random bytes.
- `jDe` is no longer a registration callee at all: in the 18.12.5 dump it is `function jDe(e, t, g, B = $9)`, a
  JSON-stringify helper with a different arity — a reader grepping the census for `jDe` would be looking for a function
  that has nothing to do with the loader.

**Repro (all read-only):**
```bash
cd /fast/scratch/kotoba-r47/w2/W2SurfacesRerun/kotoba-shokunin
grep -c '18\.12' corpus/knowledge/instruction-surface-census-round13.md          # -> 0
grep -c 'lq'      corpus/knowledge/instruction-surface-census-round13.md          # -> 0
grep -c 'fdbc8136' corpus/knowledge/instruction-surface-census-round13.md       # -> 0
grep -n 'jDe(e,Pqr' corpus/knowledge/instruction-surface-census-round13.md       # -> line 73
python3 -c "d=open('/fast/scratch/kotoba-r47/shared/omp-18.12.5.strings',errors='replace').read();\
print(d.count('jDe(e,Pqr,\"AGENTS.md\")'), d.count('Id(e,\"opencode\",\"AGENTS.md\")'), d.count('f$ = \"agents-md\"'))"
# -> 0 0 1     (the census's three cited shapes are absent; the live binding is f$)
```

**Callee-set arithmetic (the census's own last recorded remedy is two rebuilds stale).** Matching the
`(callee, <v>, <group>, "<file>.md")` shape over the whole 48 MB 18.12.5 dump:

| callee set | source | raw `.md` matches on omp 18.12.5 |
|---|---|---|
| `Id\|Cl\|jDe\|jDf\|n4\|o4\|CTt` | census `:47` (§ Method row 1) | **0** |
| `Id\|Cl\|jD[ef]\|Tl\|dr\|GW` | census `:14` (round-18 errata) | **0** |
| `Id\|Cl\|jD[ef]\|Tl\|dr\|GW\|Co\|Dl\|Hj\|I5\|Gl\|Mo` | round-44 (18.12.2) | **0** |
| `…\|Mo\|lq\|Xl\|Fo` | round-47 (18.12.5), `verifiers/verify_surfaces.py:156` | **11** → 8 distinct (group,file) pairs |

The census errata's sentence "§ A stays live — the same `.md` registration shapes persist under renamed callees
(`Id|Cl|jD[ef]` → `Tl|dr|GW`, allowlist re-pinned in the verifier)" is true in substance (the 8 class ids, literals,
kinds and verdicts are all still correct and are re-proved by the machine gate on the live binary) and false in its
cited detail: the callee set it names extracts **0** of the 8 on the current binary.

**Impact.** The gate is green and *correct*: `surfaces.literal_present` re-probes every `(group,file)` pair against the
live 18.12.5 dump, and I independently confirmed the 8 pairs are exactly the 8 `loader-group` rows. What is broken is the
**human-readable derivation record** the C1 claim names: the census's omp half is the *round-13* derivation with the
round-18 errata, re-anchored to binaries that no longer exist. A reader re-deriving the omp half by hand on the pinned
18.12.5 binary finds none of the shapes the census cites, and would have to rediscover `lq`/`Xl`/`Fo` and the `f$`/`m$`
bindings unaided.

**Honest scoping of the claim.** `LOG.md:2321` and `SCORECARD.md:32` scope the *census* claim to the **opencode** half
("census § B′ plus the ledger section"); the omp re-derivation is logged as a *verifier* change
(`LOG.md:2321`: "omp 18.12.5 callees `lq`/`Xl`/`Fo` appended to the allowlist with an 18.12.5 fixture"). The brief I was
handed phrases C1 as "omp 18.12.5 … **and** opencode 1.19.3 … re-derived in verify_surfaces.py + surfaces-baseline.json +
corpus/knowledge/instruction-surface-census-round13.md (§ B′ and the round-47 ledger section)". Under that phrasing the
census half of the **omp** re-derivation is missing. Under the LOG's own phrasing it is not. F1 is therefore a gap between
the brief's phrasing and the artifact, not a false logged claim — but it is a real gap in the corpus, and the corpus is
what a future round reads first.

### F2 — LOW-MEDIUM (calibration): the moved "superseded" rows carry a present-tense claim that round 47 falsified

`corpus/knowledge/instruction-surface-census-round13.md:289-303`

The section is titled "**Superseded** class rows and the round-47 opencode ledger (not inventory)" and its preamble says
"**Moved here in round 47, bytes unchanged**, from § B (four rows) and § C (one row): the v2.0.26 opencode classes."
But two of the five moved rows are **live** ids in the 42-id inventory and in `verifiers/surfaces-baseline.json`:

- `:297` `opencode:config/AGENTS.md` — live (inventory row `:252`; ledger `:311` "retained, re-anchored").
- `:303` `opencode:config/instructions` — live, and the moved row's reason reads "**no loader consumer proven** in the
  binary — only the read-hook publishes file contents (round-18 re-derivation, OC-3 witness only)". Round 47's own
  ledger row `:314` says "re-verdicted governed" with anchor `for(let O of T.instructions)` 1, and the live inventory row
  `:254` says "consumer proven: `for(let O of T.instructions)` inside `Instruction.systemPaths` globs each local entry".
  I re-counted the anchor on the frozen dump: `for(let O of T.instructions)` = **1**.

So the section that a reader reaches for "what is dead" states, in the present tense, the exact claim round 47
falsified. "Bytes unchanged" is the tell: the rows were relocated without re-anchoring their content. The corrected
verdicts are present in the ledger table below (`:310-320`), so the information is not lost — but the placement contradicts
it, and the gate cannot see it (both tables sit outside `## Class inventory`, so `verify_surfaces.py` does not count them;
`surfaces.table_parity` = "inventory id set == baseline id set (42 ids)").

**Repro:** read `:289-303` and `:310-314` side by side; or
`grep -n "opencode:config/instructions" corpus/knowledge/instruction-surface-census-round13.md` → `:254` (live, consumer
proven) vs `:303` (superseded table, "no loader consumer proven").

### F3 — LOW (calibration): two provenance timestamps in the re-pinned artifacts were not moved

- `verifiers/baseline.json:2` — `"as_of": "2026-10-14T09:58:47.702772-03:00"`, although `measured_against` was re-pinned
  on 2026-10-21 (`:12` `round47_note`, `:6` omp mtime `2026-10-21T03:30:38.135013187-03:00`). `as_of` is read by no gate
  (`grep -rn "as_of" verifiers/*.py` → 0 hits), so it is inert metadata, but the file's declared measurement instant
  contradicts its own contents by seven days.
- `verifiers/surfaces-baseline.json` — the `assembled` note ends with the **opencode** round-47 sentence and never mentions
  the omp 18.12.5 re-derivation (`lq`/`Xl`/`Fo`, the `f$`/`m$` var-bound groups, the 18.12.5 fixture); its header still
  reads "assembled: 2026-09-28T21:02". The baseline file that is the checked source of the 8 omp `loader-group` rows
  therefore carries no note that its omp rows were re-derived against a new binary.

### F4 — LOW (calibration, pre-existing): stale counts in the census's own Honest ceiling

`corpus/knowledge/instruction-surface-census-round13.md:370-371` — "six code-shape rules (OC-1…OC-6, anchors and
derive-vs-witness stated per rule) that must reproduce all **5** declared opencode class ids". The live rule set reports
**7** rule ids (OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6 — see the `opencode_extract` detail string) and there are **9**
declared opencode ids. Not introduced by round 47, but it sits inside the artifact the C1 claim names, and it is the
paragraph a reader consults for the ceiling.

---

## 2. CLAIMS THAT SURVIVED (findings in their own right)

### S1 — The two required runs: exit 0, 7/7 PASS, byte-identical verdicts ✔

```bash
cd /fast/scratch/kotoba-r47/w2/W2SurfacesRerun/kotoba-shokunin
python3 -B verifiers/verify_surfaces.py --json
# exit 0; pass 7, fail 0
python3 -B verifiers/verify_surfaces.py --json \
  --omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings \
  --opencode-strings /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings
# exit 0; pass 7, fail 0
```
Verdict payloads are **equal objects**, not merely equal counts:
`python3 -c "import json;a=json.load(open('W2SurfacesRerun.default.json'));b=json.load(open('W2SurfacesRerun.frozen.json'));print(a==b)"`
→ `True`. Identical detail strings, including `"opencode extraction 9/9 declared class(es) from 7/7 rules (OC-1, OC-2,
OC-3a, OC-3b, OC-4, OC-5, OC-6)"`, `"42 loader-kind entries verified against the dumps"`, `"all 8 extracted loader class(es)
declared"`, `"inventory id set == baseline id set (42 ids)"`, `"42 inventory row literal(s) match the baseline per id"`,
`"42 inventory row kind(s) match the baseline per id"`, `"8 excluded entries, all reasoned and listed in the inventory"`.
Both payloads archived as `W2SurfacesRerun.default.json` / `W2SurfacesRerun.frozen.json`.
The run is cwd-independent (`cd /` → pass 7, fail 0, exit 0): `DEFAULT_REPO` is script-relative (`verifiers/verify_surfaces.py:125`).

### S2 — The default opencode path IS the npx ELF, at the pinned sha256 ✔

```bash
file /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe
# ELF 64-bit LSB executable, x86-64, dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2,
# BuildID[sha1]=c30f169b1bef81fa57467cd091ba53aab5235468, not stripped
sha256sum …/opencode.exe
# 179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9
grep  opencode-1.19.3 /fast/scratch/kotoba-r47/shared/SHA256SUMS
# 179ca421…  bin/opencode-1.19.3          <-- identical
grep opencode_binary_sha256 verifiers/baseline.json   # 179ca421…  (verifiers/baseline.json:9)
```
It is the file the `~/.local/bin/opencode` npx wrapper executes: the wrapper is a bash script that runs
`npx --yes --prefer-online --package opencode-ai -- which opencode-ai`, and
`~/.npm/_npx/e2094862b59aac7b/node_modules/.bin/opencode -> ../opencode-ai/bin/opencode.exe`
(`node_modules/opencode-ai/package.json` → `"bin": {"opencode": "./bin/opencode.exe"}`, `"version": "1.19.3"`).
I did **not** execute the wrapper (contract).
The path recorded in the round's own before-summary
(`.ufo/waves/round-47/before/SUMMARY.md`: `…/opencode-linux-x64/bin/opencode`) is the **same inode**:
`stat -c '%i %h %n'` → `43795736 2` for both paths, same sha256. The landed path choice is therefore sound.
`~/.local/bin/omp`: `file` → ELF 64-bit x86-64, BuildID `a9ea3707…`; sha256 `fdbc8136084c9a10439569157b2af62312e2b0d801cab54c73e89476da798e7e`
= `SHA256SUMS` `bin/omp-18.12.5` = `verifiers/baseline.json:5` `omp_binary_sha256`; live mtime
`2026-10-21 03:30:38.135013187 -0300` = the pin at `verifiers/baseline.json:6`.

### S3 — The run dumps exactly the bytes the pins name ✔

```bash
strings -n 4 /home/vgpnk/.local/bin/omp                                  | sha256sum
# 33df0aeffc4565967bc1a3b42621f8eade0e6e4c2ae8733319fcd484902fb301
strings -n 4 …/opencode-ai/bin/opencode.exe                              | sha256sum
# f4d8f34ae02a2411eb5e30203421b6fcdfa81b83e96b768bbcf404504a297bc3
cmp … (both) /fast/scratch/kotoba-r47/shared/{omp-18.12.5,opencode-1.19.3}.strings   # identical
```
Both equal the `SHA256SUMS` dump lines (`33df0aef…`, `f4d8f34a…`) — i.e. the default-resolution run and the frozen-dump
run read the same bytes. The dump tool is GNU binutils **strings 2.47**; the frozen dumps were made with the same
version on this host (byte-identical output proves it).

### S4 — The "before" numbers reproduce exactly ✔
At `c61a973` (BASE) in the `base` worktree:
- default resolution → **exit 2**, `error: "opencode binary not found: /home/vgpnk/.opencode/bin/opencode"`
  (BASE's `verifiers/verify_surfaces.py:128-131` still points at the removed `~/.opencode/bin/opencode`);
- with the frozen 1.19.3 dumps → **exit 1**, 4 PASS / 3 FAIL (`literal_present`, `no_uncovered_class` vacuity 0/8,
  `opencode_extract` OC-1/OC-4/OC-6) — matching `.ufo/waves/round-47/before/SUMMARY.md` line for line.

### S5 — The discriminating cell holds (the gate is not merely "the substrate moved") ✔
AFTER code (tip) × BASE baseline + BASE census, frozen dumps → **exit 1**:
`surfaces.opencode_extract FAIL declared opencode class(es) produced by no rule: opencode:api-entries/instructions,
opencode:project/AGENTS.md, opencode:read-hook/AGENTS.md`.

### S6 — The round-47 allowlist extension is load-bearing (non-vacuous) ✔
Mutation in the `mut` worktree: drop `lq|Xl|Fo` from `OMP_CALL_RE` (`verifiers/verify_surfaces.py:156`) → **exit 1**:
`literal_present FAIL 8 loader literal(s) not verifiable: … no (Id|Cl|jD[ef]|Tl|dr|GW|Co|Dl|Hj|I5|Gl|Mo)(<v>, <group>,
"<file>.md") call shape …` and `no_uncovered_class FAIL vacuity: 0 loader class(es) extracted from the omp dump while the
baseline declares 8 loader-group class(es) for it …; extractor blind: 33 declared literal(s) present in the omp dump but no
registration shape extracts`. The 7/7 green is therefore produced *by* the round-47 change, not in spite of it.

### S7 — The two round-47 opencode gate tightenings are load-bearing ✔ (mutated dumps, `/tmp`, not the repo)
| mutation | result |
|---|---|
| `.filter(` → `.map(` in the OC-3b remote half | **exit 1** — `opencode_extract FAIL … rule(s) matched nothing: OC-3b (owns opencode:config/instructions-remote; missing .instructions….filter((q)=>q.startsWith("https://")||q.startsWith("http://")) + Instructions from: )` |
| `fn("ReadTool.execute")` → `fn("ReadTool.executeX")` | **exit 1** — `… rule(s) matched nothing: OC-4 (owns opencode:read-hook/instructions; missing fn("Instruction.resolve") + fn("ReadTool.execute") + <system-reminder>)` |
| plant `"PLANTED.md"` into the OC-1 priority array | **exit 1** — `… extracted opencode class(es) undeclared in baseline: opencode:instructions/PLANTED.md` (OC-1 **derives**, it does not witness) |

### S8 — The omp extraction set is EXHAUSTIVE on 18.12.5, not just sufficient ✔
A **callee-agnostic** scan of the whole 48 MB dump for the 3-argument registration shape
`(?<![A-Za-z0-9_$.])([A-Za-z_$][A-Za-z0-9_$]*)\(\s*[^\s,()]+\s*,\s*(?:"([a-z0-9_-]+)"|([A-Za-z_$][A-Za-z0-9_$]*))\s*,\s*"([A-Za-z0-9_./-]+\.md)"(?=\s*[,)])`
returns exactly **3 distinct callees**: `Xl` (5), `Fo` (4), `lq` (2) — the same 11 raw matches the round-47 allowlist
yields, resolving to the same 8 `(group,file)` pairs:
`agents-md/AGENTS.md`, `claude-md/CLAUDE.md`, `gemini/GEMINI.md`, `gemini/SYSTEM_TEMPLATE.md`, `gemini/system.md`,
`github/copilot-instructions.md`, `opencode/AGENTS.md`, `windsurf/memories/global_rules.md`.
**No `.md` registration shape hides under an unallowlisted callee**, so the 12 dead names in the allowlist are inert on
this binary and no class is missing from the census's omp half. (The allowlist's 15 names are a growing historical set:
3 live, 12 dead — harmless today because an allowlisted callee that matches a *new* shape would yield an **undeclared**
class → FAIL, i.e. fail-closed.)
Same probe on the opencode 1.19.3 dump: **0** generic `.md` call shapes — consistent with the census's
"opencode's loaders are not `(group, literal)`-shaped calls" and with the OC-rule design.

### S9 — Every census § B′ / ledger anchor and dump-line citation reproduces on the frozen dump ✔
Counted with the census's own documented command
(`python3 -c 'import sys;d=open(sys.argv[1],errors="replace").read();print(d.count(sys.argv[2]))' <dump> '<anchor>'`):

| anchor | census says | measured |
|---|---|---|
| `ConfigInstructionPlugin` / `ReadTool.Plugin` / `SessionInstructions` / `session.instructions.entry.put` / `j5(r.config,"AGENTS.md")` / `InstructionDiscovery` | 0 | **0, 0, 0, 0, 0, 0** |
| `X.join(r.config,"AGENTS.md")` | 1 | **1** |
| `instructions:{entry:{list:` | 1 | **1** |
| `for(let O of T.instructions)` | 1 | **1** |
| priority array `["AGENTS.md",…,"CONTEXT.md"]` | 1 | **1** (full literal) |
| `disableClaudeCodePrompt` | 3 | **3** |
| `CONTEXT.md` | 1 | **1** |
| `X.join(r.home,".claude","CLAUDE.md")` | 1 | **1** |
| `Instructions from: ` | 4 | **4** |
| `fn("Instruction.resolve")` / `fn("ReadTool.execute")` | 1 / 1 | **1 / 1** |
| `InstructionContext.observe` / `system-context-builtins` | 1 / 1 | **1 / 1** |
| `<system-reminder>` | 18 | **18** |
| `var n="1.19.3"` / `2.0.26` | present / absent | **1 / 0** |

Dump-line citations also land exactly: `["AGENTS.md",` → **443993**; `fn("Instruction.resolve")` → **443995**;
`fn("ReadTool.execute")` → **444228**; `Key.make("core/instructions")` → **445481**;
`InstructionContext.observe` → **445482** (census: "445481-445487"). OC-5's switch polarity is confirmed verbatim at
L443993: `if(!Jr.OPENCODE_DISABLE_PROJECT_CONFIG) return yield*e.globUp(T,d.directory,d.worktree); return
yield*e.globUp(T,r.config,r.config)` — project walk-up unless the env var is set, exactly as `verifiers/verify_surfaces.py:407-408`
describes. § D's "byte-identical at two sites" claim holds: `.cursorrules` (2) and `copilot-instructions.md` (2) occur
only at L444608 and L445789 (the `/init` template), and a sweep of all 30 `AGENTS.md` occurrences in the opencode dump
shows only prompt text plus the two modeled loader sites (L443993 priority array + config join; L445482 OC-6
`targets:["AGENTS.md"]` / `jX(L.config,"AGENTS.md")`) — no third, unmodeled loader site.

### S10 — The 18.12.5 fixture is faithful to the real binary ✔
`verifiers/fixtures/surfaces/strings-omp-18.12.5.txt` (14 lines): **13 of 14 are verbatim substrings of the real
`omp-18.12.5.strings`**; the 14th is the declared synthetic decoy
(`const q = Xl; var decoy = q(u, "evil", "EVIL.md");`). The fixture therefore does not certify a fiction.

### S11 — Fail-closed environment handling ✔
`--opencode-binary /nonexistent/opencode` → **exit 2** (`error: "opencode binary not found: …"`, not a pass);
the retired v2.0.26 generation fixture (`verifiers/fixtures/surfaces/strings-opencode-v2.0.26.txt`) → **exit 1**
(5 `literal_present` failures + `opencode_extract FAIL vacuity: extraction produced 0 class(es) from 7 rule(s)`).

### S12 — Self-test intact ✔
`python3 -B verifiers/verify_surfaces.py --self-test` → **exit 0**, "0 failure(s) over **99** assertions" (the round-47
count; the 18.12.5-callees arm "18.12.5-callees: exit 0" is one of them).

---

## 3. Residual risk (no gate impact, recorded not smoothed)

- **R1 — `strings` version is unpinned.** The frozen dumps are binutils 2.47 output; a host with a different binutils
  could produce a different dump, so the default run's verdict could differ from the frozen-dump verdict. On this host they
  are byte-identical, so the "identical verdict details" claim holds *here* only.
- **R2 — the default opencode path points into a mutable npx cache.** `npx --prefer-online --package opencode-ai` can
  re-resolve `^1.19.3` to a newer 1.19.x **in the same cache dir**; the pinned path would then hold different bytes →
  pins DRIFT + surfaces extraction changes. This fails closed (never a silent green), but the *default resolution* is
  inherently volatile. Today the cache also carries `opencode-linux-x64-baseline` (the postinstall's non-AVX2 variant) —
  same version 1.19.3 and the **same sha256** `179ca421…`, so no decoy today; on a non-AVX2 host the *executed* binary
  could be the `-baseline` copy while the pin names `opencode-ai/bin/opencode.exe` (same bytes here, but the pin would
  name a path the host does not execute).
- **R3 — the omp allowlist is a 15-name historical set with 3 live names.** It is complete for the shape on 18.12.5
  (S8), but the next minifier rename requires another hand re-pin — already recorded as the standing debt in
  `corpus/README.md:76` and in the verifier's own comment block (`verifiers/verify_surfaces.py:139-144`).
- **R4 — `verifiers/baseline.json`'s `as_of`** (F3) is read by no gate, so nothing detects it drifting again.

---

## 4. What I did NOT check

- I did **not** run `verifiers/check_substrate_pins.py` (that is the pins lane, `KotobaR47-2.W2PinsRerun-2`); I compared
  the pin *values* in `verifiers/baseline.json` against `SHA256SUMS` and the live binaries by hand only.
- I did not audit C2 (`trigger.no_xml_tag` in `verifiers/verify_skill_checklist.py`, the SKILL.md `<skills>` frontmatter
  change) or C3 (the `GOVERNANCE_ERRATA` row, `LOG.md:2111` line sha256, the corpus README index, `tracked_files` 58→60,
  the fault-harness planter) — out of this lane's scope.
- I did not verify the census's SKILL.md table body hash (`census:411-412`) or the round-47 lesson/quality rows.
- I did not re-derive the 25 hand-declared omp `loader-literal` rows (§ A's second table, `omp:cursor/rules` …
  `omp:agents/skills`): by design they are probed by `literal_present` only (literal-in-dump), so a hand audit of their
  registry descriptions is still open.
- I did not re-derive the § C exclusion *reasons* (8 rows) on the live binary; the gate only proves a reason exists
  (the census's own "Reason truth" ceiling). I did verify the § D false-friend rows (`.cursorrules`,
  `copilot-instructions.md`) and the opencode loader classes.
- No runtime/wire evidence: I never executed the `~/.local/bin/opencode` wrapper (contract) and ran no live harness
  session, so "the loader fires" remains undecided (the census's own ceiling).
- I did not test on a host with a different binutils or a non-AVX2 CPU (R1/R2 are reasoned from the postinstall source
  and the cache layout, not executed).
- I did not run the corpus gates, the fault harness, or the floors verifier.

---

## 5. Tooling

No installs, no upgrades, no pacman transactions. Pre-existing tools used: `python3` 3.14.8, `git` 2.56.0,
GNU `strings` (binutils) 2.47, `file`, `sha256sum`, `cmp`, `stat`, `grep`/`sed` for read-only inspection.
Artifacts written by this lane: `.ufo/waves/round-47/falsify/W2SurfacesRerun.md` (this file),
`W2SurfacesRerun.default.json`, `W2SurfacesRerun.frozen.json` (both 1132 B). All mutations were confined to
`/fast/scratch/kotoba-r47/w2/W2SurfacesRerun/{kotoba-shokunin,base,mut}` (scratch clone + git worktrees); the production
tree and the lane's git/jj state were untouched.
