verdict: OC-1's behaviour is PRESENT in opencode 1.19.3 but its first anchor is RENAMED — `ConfigInstructionPlugin.projectSource` has 0 hits in both the reproducible strings dump and the raw binary; the project-source walk-up is now `InstructionContext.observe` (layer `instruction-context`, registration key `core/instructions`), while `targets:["AGENTS.md"]` is still present verbatim (1 hit). Re-pin anchor 1 only; the tested 8-file patch is `C1WitnessOC1.patch`.

# C1 per-rule witness — OC-1 (opencode 1.19.3)

BASE: `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (`git rev-parse HEAD` in the lane repo, exit 0).
Snapshot: `/fast/scratch/kotoba-r47/shared/{bin/opencode-1.19.3, opencode-1.19.3.strings}`.

## 1. What OC-1 asserts at BASE

- `verifiers/verify_surfaces.py:353-360` — comment + the two constants:
  - `:359` `OC_PROJECT_FN = "ConfigInstructionPlugin.projectSource"`
  - `:360` `OC_PROJECT_TARGETS = 'targets:["AGENTS.md"]'`
- `verifiers/verify_surfaces.py:413-415` — `project = OC_PROJECT_FN in dump and OC_PROJECT_TARGETS in dump`; on true it owns `opencode:project/AGENTS.md`, on false the rule is reported unmatched.
- `verifiers/verify_surfaces.py:406` — `missing = [] if matched else list(anchors)` (see counterexample in §5).
- `verifiers/surfaces-baseline.json:245-249` — `opencode:project/AGENTS.md`, literal `AGENTS.md`, `loader-literal`, `governed`. OC-1 is its only producer.
- Census witness text: `corpus/knowledge/instruction-surface-census-round13.md:206`.
- Pre-build state: `.ufo/waves/round-47/before/SUMMARY.md:4` — `surfaces --opencode-binary <npx 1.19.3>: 4 PASS / 3 FAIL (... opencode_extract OC-1/OC-4/OC-6)`; the npx ELF sha `179ca421…` there equals the snapshot binary sha, so this is the same artifact.

## 2. Substrate freshness (checked before grepping)

- `sha256sum -c SHA256SUMS` in `/fast/scratch/kotoba-r47/shared` → exit 0, four `OK` lines (both binaries, both dumps).
- `strings -n 4 bin/opencode-1.19.3 | sha256sum` → `f4d8f34ae02a2411eb5e30203421b6fcdfa81b83e96b768bbcf404504a297bc3`, byte-identical to `opencode-1.19.3.strings`; the dump is exactly what `verify_surfaces.py:214` would generate (`strings -n 4`). Pipeline exit 0.

## 3. State of OC-1 in 1.19.3: renamed-to-X, behaviour present

### Anchor 1 — ABSENT as written, renamed

| token | dump hits | raw-binary hits | `grep -q` exit |
|---|---|---|---|
| `ConfigInstructionPlugin.projectSource` | 0 | 0 | 1 |
| `ConfigInstructionPlugin` | 0 | 0 | 1 |
| `InstructionContext.observe` | 1 | 1 | 0 |
| `core/instructions` | 1 | 1 | 0 |
| `instruction-context` | 1 | — | 0 |

Rename sweep, all 0 hits in the dump (several plausible spellings): `ConfigInstruction`, `config.instruction`, `config.instruction.plugin`, `opencode.config`, `opencode.config.instruction`, `Plugin.project`, `InstructionPlugin`, `InstructionService`, `InstructionsContext`, `InstructionContextPlugin`, `ProjectSource`, `project_source`, `instructionPlugin`, `projectInstructions`.

Live evidence, dump line 445482 (`grep -n -o -F 'InstructionContext.observe'` → `445482:InstructionContext.observe`), byte 12866070:

```
...,BP=XH.Key.make("core/instructions"),uX=... M.gen(function*(){...
A=M.fn("InstructionContext.observe")(function*(){
  let S=yield*H.resolve(E.directory),$=yield*H.resolve(E.project.directory),P=OX($,S),
  h=P===""||P!==".."&&!P.startsWith(`..${pX}`)&&!qX(P),
  U=new Set(yield*M.forEach(qE.OPENCODE_DISABLE_PROJECT_CONFIG||!h?[]:
      yield*H.up({targets:["AGENTS.md"],start:S,stop:$}),H.resolve)),
  F=yP.dedupe([yield*H.resolve(jX(L.config,"AGENTS.md")),...U]), ...
yield*I.register({key:BP,load:A().pipe(...)})
```

Layer identity: `gX=i({name:"instruction-context",layer:uX,deps:[SH.node,DE.node,cH.node,TL.node]})`, byte 12866890, dump line 445482. Service class `InstructionContext.File` and key `core/instructions` are at dump line 445481/445482.

### Anchor 2 — STILL PRESENT

`targets:["AGENTS.md"]`: exactly 1 dump hit and 1 binary hit (`grep -q` exit 0), dump line 445482, byte 12866329, inside `H.up({targets:["AGENTS.md"],start:S,stop:$})` (byte 12866325). It is 259 bytes downstream of `InstructionContext.observe` in the same strings chunk.

### Behaviour — present, same semantics

Resolve cwd (`E.directory`) and `E.project.directory`, containment guard, gate on `OPENCODE_DISABLE_PROJECT_CONFIG` (the literal is co-located on dump line 445482, 1 of its 9 dump hits), all-match walk-up (`up` → `forEach` → `Set`), dedupe against the config-dir `AGENTS.md`, read every file, register the result under `core/instructions`. That is OC-1's "project walk-up, all-match AGENTS.md".

Two details of the BASE comment are stale even though the check does not test them:
- `verifiers/verify_surfaces.py:358` shows `type:"file"` in the call; the live call is `{targets:["AGENTS.md"],start:S,stop:$}` with no `type`. `type:"file"` occurs 182× elsewhere, so it proves nothing.
- `:353` names a plugin `opencode.config.instruction`; that literal has 0 hits in 1.19.3.

## 4. Minimum discriminating anchor set for 1.19.3

**`{"InstructionContext.observe", "targets:[\"AGENTS.md\"]"}`** — both are code literals, each occurs exactly once in the dump, 259 bytes apart on the same strings line. Uniqueness makes plain `in dump` exact: there is no second occurrence that could satisfy one anchor in an unrelated subsystem.

Recommended optional third anchor: `core/instructions` (1 hit, byte 12865688) to tie the loader to the instruction-service registration. Not required for discrimination now, and it widens the failure surface if the key is renamed, so the minimal patch below keeps two.

Rejected candidates (measured):
- `projectSource` — 2 hits, both message-pagination code (`projectSource:!0`, `G.projectSource&&ke`) at bytes 49762799 / 49765326. The bare token is a false friend; never anchor on it.
- `OPENCODE_DISABLE_PROJECT_CONFIG` — 9 hits on 7 dump lines; discriminating only in conjunction with the `up()` shape, and OC-5 already owns it.
- `type:"file"` — 182 hits. `AGENTS.md` — 25 hits.

Second AGENTS.md channel, deliberately not matched: the legacy `@opencode/Instruction` service at dump line 443993 carries the name-priority array `["AGENTS.md",...!t.disableClaudeCodePrompt?["CLAUDE.md"]:[],"CONTEXT.md"]` and `X.join(r.config,"AGENTS.md")`, with `findUp`, not `up({targets:["AGENTS.md"]})`. Neither OC-1 anchor occurs there, so the minimum set above does not conflate the two channels.

## 5. Counterexample: the `missing` list is not per-anchor

`verifiers/verify_surfaces.py:406` reports **every** anchor as missing when the rule is unmatched. Observed output on 1.19.3:

```
OC-1 (owns opencode:project/AGENTS.md; missing ConfigInstructionPlugin.projectSource + targets:["AGENTS.md"])
```

but `targets:["AGENTS.md"]` is present (byte 12866329). Any re-pin workflow that trusts `missing` would "re-pin" a live anchor. The function is fail-closed as designed, but the message is wrong for one of the two anchors; making the report carry per-anchor presence (a parallel machine-anchor list, since OC-3/OC-5 anchors are prose labels) would remove the trap.

## 6. Collateral calibration (outside OC-1, relevant to C1)

- **OC-2 currently passes on the legacy chunk.** Its regex matches `join(r.config,"AGENTS.md")` in `@opencode/Instruction` at dump line 443993 — not the live `instruction-context` chunk, whose global join is `jX(L.config,"AGENTS.md")` (byte 12866409, dump line 445482) and does not match the `r.config` shape. Textual consumer probes for the legacy layer return 0 (`bi.Service`, `bi.node`, `systemPaths()`), so it is plausible that OC-2 is green on code this bundle never wires. [INFERENCE] — liveness is not proven either way; this needs its own witness before the C1 re-pin is called done.
- **Baseline provenance contradicts 1.19.3.** `verifiers/surfaces-baseline.json:3` says the classes were re-derived for a 2.x binary and that "the instruction-context subsystem [is] gone". 1.19.3 has a layer literally named `instruction-context` plus the `InstructionContext` service. Either that note describes another build or the subsystem returned; the note must not be read as current for this substrate.
- **OC-4 / OC-6 remain absent.** OC-4: 0/4 anchors (`ReadTool.Plugin`, `targets:[a$]`, `a$="AGENTS.md"`, `SessionInstructions.load`); OC-6: 0/2 (`/instructions/entries`, `session.instructions.entry.put`). Reproduces the before FAIL set. Not my item; flagged so OC-1's green is not mistaken for opencode_extract green.

## 7. Re-pin patch (scratch-tested, advice only)

`C1WitnessOC1.patch` (8 files, prefixes `i/`/`w/` — apply with `git apply -p1`), generated from a scratch clone at BASE:

- `verifiers/verify_surfaces.py`: `OC_PROJECT_FN = "InstructionContext.observe"`; comment rewritten to the live identity and to say the legacy `@opencode/Instruction` array is a different service; notes that `type:` is gone.
- 7 fixtures (`strings-opencode-{clean,extra,drop-oc2..oc6}.txt`): replace the embedded old token with `InstructionContext.observe`. This coupling is mandatory: the fixtures at `verifiers/fixtures/surfaces/strings-opencode-clean.txt:6` and siblings embed the old anchor, and the self-test asserts `clean: exit 0`. `strings-opencode-drop-oc1.txt` correctly contains neither anchor and was left untouched. Four baseline fixture `$comment` prose strings still mention the old token; cosmetic only, not read by any check.

Observed after the patch, against the snapshot dump + production baseline:

- `extract_opencode_classes` → `OC-1 True`; ids now include `opencode:project/AGENTS.md` (plus `config/AGENTS.md`, `config/instructions`).
- `check_opencode_extract` → still `False`, but the OC-1 clause is gone; remaining: `OC-4`, `OC-6`.
- Full CLI on the snapshot dumps: `exit=1`, `surfaces.opencode_extract` no longer names OC-1 / `opencode:project/AGENTS.md`. Remaining FAILs: omp-side `literal_present` / `no_uncovered_class` (other C1 seat) and OC-4/OC-6.
- `python3 verifiers/verify_surfaces.py --self-test` → exit 0, `0 failure(s) over 87 assertions` (without the fixture edits the clean fixture loses OC-1 and that assertion cannot hold).

## 8. Commands run (exit codes)

| command | exit | key output |
|---|---|---|
| `git rev-parse HEAD` (lane repo, read-only) | 0 | `c61a973b2e02e1ded169703ddcb06466f4edd8bd` |
| `sha256sum -c SHA256SUMS` (shared snapshot dir) | 0 | 4× OK |
| `strings -n 4 bin/opencode-1.19.3 \| sha256sum` | 0 | `f4d8f34a…` = dump sha |
| `grep -q -F 'ConfigInstructionPlugin' opencode-1.19.3.strings` | 1 | absent |
| `grep -q -F 'targets:["AGENTS.md"]' …` | 0 | present |
| `grep -q -F 'InstructionContext.observe' …` | 0 | present |
| `grep -q -F 'core/instructions' …` | 0 | present |
| `grep -a -o -F 'ConfigInstructionPlugin' bin/opencode-1.19.3 \| wc -l` | 0 (wc) | `0` |
| `grep -a -o -F 'targets:["AGENTS.md"]' bin/opencode-1.19.3 \| wc -l` | 0 (wc) | `1` |
| python: `extract_opencode_classes(baseline)` on snapshot dump | 0 | OC-1/OC-4/OC-6 unmatched; OC-2/3/5 matched |
| python: `check_opencode_extract(production baseline)` | 0 | `ok: False`, names OC-1/OC-4/OC-6 |
| `python3 verifiers/verify_surfaces.py --self-test` (patched scratch clone) | 0 | 87 assertions, 0 failures |
| full CLI with snapshot `--omp-strings`/`--opencode-strings` (patched clone) | 1 | opencode_extract now OC-4/OC-6 only |
| `git apply -R --check C1WitnessOC1.patch` (scratch clone) | 0 | patch reverses cleanly |

No tools were installed or upgraded. No network used.

## 9. What I did NOT check

- No end-to-end run of `verify_surfaces.py` in the production tree (production is read-only to me); the patch was exercised in `/fast/scratch/kotoba-r47/C1WitnessOC1/lane` only.
- No older opencode binary is available, so I cannot date when `ConfigInstructionPlugin.projectSource` disappeared or confirm the anchor's last-good substrate; `.ufo/waves/round-47/before/SUMMARY.md:4` only shows 1.19.3 already failed it.
- Liveness of the legacy `@opencode/Instruction` service is unresolved: I only counted textual consumers (`bi.Service` = 0, `bi.node` = 0, `systemPaths()` = 0). Static minified bundles can wire it under another alias; this needs a runtime or graph witness.
- I did not inspect the `up()` implementation to confirm what `targets` accepts now (only the call shape).
- I did not check the omp 18.12.5 side of `literal_present`/`no_uncovered_class`, OC-2/OC-4/OC-6 re-pins, the description XML-tag check, or the erratum registry — other C1/C2/C3 seats.
- No JSON/schema validation of `surfaces-baseline.json` beyond `json.load` in the check helpers.
