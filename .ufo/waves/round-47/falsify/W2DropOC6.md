verdict: PARTIAL — OC-6 gate (verifiers/verify_surfaces.py:494-498) mutation-probed on the real opencode-1.19.3 dump: anchor loss killed 8/8, spelling renames false-red 4/4, load-condition drift and self-test quantifier gaps survive

# W2DropOC6 — OC-6 mutation probe (round-47 falsify, wave 2)

Tree: `/fast/scratch/kotoba-r47/w2/W2DropOC6/kotoba-shokunin`, detached at `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`. `git status --short` empty after all runs. Production tree not written, no git run in production.

## Setup and provenance

- `verifiers/verify_surfaces.py` sha256 `e44bf34b1a52c0e5e4cd320b8f90a20c10c0a997bc225e9b36bf90ccf173be4e`; `verifiers/surfaces-baseline.json` sha256 `6b23c3d1c8766e4effea9f5502b638de7b22cd0d61be20426ba99482c7d1260b`.
- `cd /fast/scratch/kotoba-r47/shared && sha256sum -c SHA256SUMS` → `opencode-1.19.3.strings: OK`, `omp-18.12.5.strings: OK` (plus both binaries), exit 0. Dump: sha256 `f4d8f34ae02a2411eb5e30203421b6fcdfa81b83e96b768bbcf404504a297bc3`, 67,839,091 bytes.
- Mutants live in `/fast/scratch/kotoba-r47/w2/W2DropOC6/mutants/` (1.1 GiB, scratch only; nothing copied into production).
- Installs/updates: none. Tools: system `python3`, GNU `grep`, `sha256sum`. The opencode wrapper, the default opencode binary path and the opencode binary were never executed. Every non-self-test verifier run passed `--opencode-strings` and `--omp-strings` explicitly. No labrat dispatched.

## 1. Counting commands re-run (real dump, 7ad7fad verifier)

| command | result | exit |
|---|---|---|
| `grep -a -c -F` per OC-6 anchor (lines) | 1 / 1 / 1 / 1 | 0 |
| `grep -a -o -F … \| wc -l` (occurrences) | `Key.make("core/instructions")`=1, `targets:["AGENTS.md"]`=1, `InstructionContext.observe`=1, `system-context-builtins`=1 | 0 |
| `grep -a -n -F` (dump line) | Key→445481; observe→445482; targets→445482; system-context-builtins→445487 | 0 |
| byte offsets (python `bytes.index`) | Key 12865679; observe 12866071; targets 12866329; registration 12867917 | — |
| `InstructionContext` / `AGENTS.md` / `jX(L.config,"AGENTS.md")` / `H.up(` | 3 / 30 / 1 / 1 | 0 |
| `verify_surfaces.py --opencode-strings <real> --omp-strings <real>` | 7/7 PASS; `surfaces.opencode_extract: opencode extraction 9/9 declared class(es) from 7/7 rules (OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6)` | 0 |
| same with `--check surfaces.opencode_extract` | PASS | 0 |
| `verify_surfaces.py --self-test` | `0 failure(s) over 99 assertions` | 0 |

Freshness of the OC-6 anchors (C1 part) holds: 4/4 present, each exactly once, at the dump lines the comment cites (`verify_surfaces.py:410-412`, "dump 445481-445487").

## 2. Anchor mutations on the real dump (16 mutants)

Each mutant is one byte-exact replacement, `count == 1` asserted, applied to a copy of `opencode-1.19.3.strings`. Two runs each: full checks (`full rc`) and `--check surfaces.opencode_extract` (`check rc`). Repro in §8.

| # | mutant | edit (old → new) | dump line / byte | full rc | check rc | result |
|---|---|---|---|---|---|---|
| 1 | OBS-remove | `InstructionContext.observe` → ∅ | 445482 / 12866071 | 1 | 1 | killed |
| 2 | OBS-corrupt | `…observe` → `…obzerve` | 445482 / 12866071 | 1 | 1 | killed |
| 3 | KEY-remove | `Key.make("core/instructions")` → ∅ | 445481 / 12865679 | 1 | 1 | killed |
| 4 | KEY-corrupt | `core/instructions` → `core/instruction` | 445481 / 12865679 | 1 | 1 | killed |
| 5 | TGT-remove | `targets:["AGENTS.md"]` → ∅ | 445482 / 12866329 | 1 | 1 | killed |
| 6 | TGT-corrupt | `"AGENTS.md"` → `"AGENTS.Md"` | 445482 / 12866329 | 1 | 1 | killed |
| 7 | REG-remove | `system-context-builtins` → ∅ | 445487 / 12867917 | 1 | 1 | killed |
| 8 | REG-corrupt | `system-context-builtins` → `system-context-builtin` | 445487 / 12867917 | 1 | 1 | killed |
| 9 | EQ-label | `InstructionContext.observe` → `instruction-context.observe` | 445482 / 12866071 | 1 | 1 | false red (§4) |
| 10 | EQ-quote-tgt | `targets:["AGENTS.md"]` → `targets:['AGENTS.md']` | 445482 / 12866329 | 1 | 1 | false red (§4) |
| 11 | EQ-quote-key | `Key.make("core/instructions")` → `Key.make('core/instructions')` | 445481 / 12865679 | 1 | 1 | false red (§4) |
| 12 | EQ-layer | `system-context-builtins` → `system_context_builtins` | 445487 / 12867917 | 1 | 1 | false red (§4) |
| 13 | W-config | `jX(L.config,"AGENTS.md")` → `jX(L.config,"CLAUDE.md")` | 445482 / 12866409 | 0 | 0 | **SURVIVES** (§3a) |
| 14 | W-walk-stop | `…start:S,stop:$}` → `…start:S,stop:S}` | 445482 / 12866329 | 0 | 0 | **SURVIVES** (§3b) |
| 15 | W-gate | `qE.OPENCODE_DISABLE_PROJECT_CONFIG\|\|!h?[]:yield*H.up(` → `yield*H.up(` | 445482 / 12866275 | 0 | 0 | **SURVIVES** (§3c) |
| 16 | D1-decoy | four real anchors deleted; the same four literals re-planted in one trailing dead line | 445481–445487 deleted; new last line | 0 | 0 | **SURVIVES** (§3d) |

Kill output, identical in all 12 red rows (rows 1–12):

```
FAIL surfaces.opencode_extract: declared opencode class(es) produced by no rule: opencode:instruction-context/AGENTS.md; rule(s) matched nothing: OC-6 (owns opencode:instruction-context/AGENTS.md; missing InstructionContext.observe + Key.make("core/instructions") + targets:["AGENTS.md"] + system-context-builtins)
```

The owned class and the rule are both named, so the kill criterion holds. But the `missing` list names all four anchors in every red row, including the single-anchor removals (rows 1, 3, 5, 7): `rule()` sets `missing = list(anchors)` on any non-match (`verifiers/verify_surfaces.py:441`). The comment at `:344-346` promises an absent anchor is "reported by name". It is not. See §6.

## 3. Survivors (exit 0) with diffs

Full diffs of the dump windows are in `.ufo/waves/round-47/falsify/W2DropOC6.patch`; the code-level diffs are unified diffs of `verify_surfaces.py`.

### 3a. W-config — ungated config-dir candidate reads CLAUDE.md (exit 0, all PASS, 9/9 classes)

```
-…H.resolve)),F=yP.dedupe([yield*H.resolve(jX(L.config,"AGENTS.md")),...U]),y=yield*M.forEach(F,…
+…H.resolve)),F=yP.dedupe([yield*H.resolve(jX(L.config,"CLAUDE.md")),...U]),y=yield*M.forEach(F,…
```

The comment at `verify_surfaces.py:412-415` says this candidate is why the class carries its own id: "keeps an ungated config-dir candidate (`jX(L.config,"AGENTS.md")`) — a different load condition … which is why it carries its own class id." Nothing witnesses it. OC-2's pattern (`:376-378`) requires a `.join(` call; the real dump matches only `.join(r.config,"AGENTS.md"` there, and the OC-6 candidate is a bare `jX(` (alias of `path.join`, import on dump line 445481). `CALL_RE` (`:151`) has no `jX` shape.

### 3b. W-walk-stop — all-match walk bounded at cwd (exit 0)

```
-…targets:["AGENTS.md"],start:S,stop:$}…
+…targets:["AGENTS.md"],start:S,stop:S}…
```

Only the target literal witnesses the walk. Its bounds (`stop:$`, the project directory from the same function's `E.project.directory`) are not witnessed. The comment at `:410-412` claims the walk goes "up from cwd to the project root".

### 3c. W-gate — project-walk gate removed (exit 0)

```
-…U=new Set(yield*M.forEach(qE.OPENCODE_DISABLE_PROJECT_CONFIG||!h?[]:yield*H.up({targets:…
+…U=new Set(yield*M.forEach(yield*H.up({targets:…
```

OC-5 witnesses the env name only globally (`:406`, rule at `:485-490`), not this gate on OC-6's walk.

### 3d. D1-decoy — presence is placement-blind (exit 0)

Deleted: the four real literals in their loader positions (dump lines 445481–445487). Appended as the final dump line: `DEAD: InstructionContext.observe Key.make("core/instructions") targets:["AGENTS.md"] system-context-builtins`. The rule is `all(literal in dump)` (`:495-496`), so a dead string satisfies it. Realistic analogues are rows 13–15; this row proves the mechanism.

### 3e. Code-level survivors (working copy of `verifiers/` in scratch, never committed)

Control (unmutated copy): `--self-test` rc 0, `0 failure(s) over 99 assertions`.

| mutant | edit in `verify_surfaces.py` | self-test | real-dump kill | result |
|---|---|---|---|---|
| K1 | `v2 = all(a in dump` → `v2 = any(a in dump` (`:495`) | rc 0, 0 failures | rows OBS/KEY/TGT/REG-remove → rc 0 each | SURVIVES ×4 |
| K2 | drop `OC_V2_OBSERVE,` from the tuple (`:495`) | rc 0, 0 failures | OBS-remove → rc 0 | SURVIVES |
| K3 | drop `OC_V2_TARGETS,` | rc 0, 0 failures | TGT-remove → rc 0 | SURVIVES |
| K4 | drop `OC_V2_KEY,` | rc 0, 0 failures | KEY-remove → rc 0 | SURVIVES |
| K5 | drop `OC_V2_REGISTRATION` | rc 0, 0 failures | REG-remove → rc 0 | SURVIVES |

Why the self-test misses them. The OC loop (`verify_surfaces.py:1035-1048`) has one OC-6 fixture, `verifiers/fixtures/surfaces/strings-opencode-drop-oc6.txt` (`:1043`). It removes all four anchors together (each count 0). No fixture holds a partial OC-6 anchor set:
- `strings-opencode-extra.txt`, `strings-opencode-drop-oc1` … `oc5`, `strings-opencode-planted-name.txt` each contain all four.
- `strings-opencode-v2.0.26.txt` contains only `targets:["AGENTS.md"]` (line 7: `i.up({targets:["AGENTS.md"],start:_,stop:P,type:"file"})`). Its assertion (`:1059-1063`) checks only OC-1 unmatched.

### 3f. Cross-generation consequence of K1 (`W2DropOC6.crossgen.txt`)

On the retired v2.0.26 fixture, the unmutated verifier lists `opencode:instruction-context/AGENTS.md` under "produced by no rule" (exit 1). Under K1, the same fixture still exits 1 (other rules unmatched), but that class drops out of the list. The 1.19.3 OC-6 class would be claimed from a retired-generation dump. The comment at `:1056-1058` says exactly this must not happen ("a rule set that OR-ed both generations' anchors would … launder the re-derive"). The self-test asserts it only for OC-1 (`:1063`).

## 4. Renamed-but-equivalent anchors: too narrow (false red)

| mutant | edit | result |
|---|---|---|
| EQ-label | `InstructionContext.observe` → `instruction-context.observe` | exit 1, false red |
| EQ-quote-tgt | `"AGENTS.md"` → `'AGENTS.md'` (same JS literal) | exit 1, false red |
| EQ-quote-key | `"core/instructions"` → `'core/instructions'` (same JS literal) | exit 1, false red |
| EQ-layer | `system-context-builtins` → `system_context_builtins` | exit 1, false red |

Verdict: too narrow. The rule is `all(literal in dump)` over byte-exact literals (`:495-496`). Two literals are names rather than dispatch keys:
- `InstructionContext.observe` is the first argument of `M.fn(...)` at dump line 445482. It has the same `fn("X.y")` shape as the OC-4 name `s.fn("Instruction.resolve")` (`:423`).
- `system-context-builtins` is the `name:` of layer `kX` at dump line 445487.

Each occurs exactly once in the dump, so no other string-keyed lookup references them. That is count-verified; their runtime role is `[INFERENCE]`. The quote variants are JS-equivalent. The fail-closed design (`:344-346`) accepts a red on drift, but these reds are cosmetic and the message (§2) points at all four anchors.

## 5. Split verdict: narrow on spelling, wide on load condition

- Narrow: spelling and label changes go red (§4).
- Wide: four present strings do not witness the load condition the class id encodes (`:410-415`). Anchor loss is killed (8/8, §2). Load-condition drift is not (3/3 plus the decoy, §3a–d).
- No second gate catches the survivors. `literal_present` checks the baseline literal `AGENTS.md` (`verifiers/surfaces-baseline.json:303`), which occurs 30 times in the dump. The only OC-6 gate is `opencode_extract`.

## 6. Diagnostic defect (calibration and operability)

- `verifiers/verify_surfaces.py:440-441`: `missing = [] if matched else list(anchors)`. Every red OC-6 row lists all four anchors, even when only one literal is absent. Row 1 removes only `InstructionContext.observe`, yet the message also reports `Key.make("core/instructions")`, `targets:["AGENTS.md"]` and `system-context-builtins` as missing.
- The comment at `:344-346` promises an absent anchor is reported by name. The same helper serves OC-1…OC-5 (rule calls at `:447-497`). I inspected that path but did not mutate those rules.
- Suggested, not applied: compute per-anchor absence inside `extract_opencode_classes`, where `dump` is in scope.

## 7. Candidate witnesses (regex level in scratch; not applied to the verifier)

| witness | real dump matches | target survivor matches |
|---|---|---|
| `\bjX\(\s*[A-Za-z_$][A-Za-z0-9_$]*\.config\s*,\s*"AGENTS\.md"\)` | 1 | W-config: 0 |
| `H\.up\(\{targets:\["AGENTS\.md"\],start:[A-Za-z_$][A-Za-z0-9_$]*,stop:\$\}\)` | 1 | W-walk-stop: 0 |
| `qE\.OPENCODE_DISABLE_PROJECT_CONFIG\|\|!h\?\[\]:yield\*H\.up\(` | 1 | W-gate: 0 |
| co-located (re.S): `InstructionContext\.observe"\)\(function\*\(\)\{.{0,900}?H\.up\(\{targets:\["AGENTS\.md"\],start:[A-Za-z_$][A-Za-z0-9_$]*,stop:\$\}\).{0,900}?jX\(\s*[A-Za-z_$][A-Za-z0-9_$]*\.config\s*,\s*"AGENTS\.md"\)` | 1 | W-config 0, W-walk-stop 0, D1-decoy 0, OBS-remove 0; W-gate still 1 |

These depend on minified identifiers (`jX`, `qE`, `h`) and inherit the §4 rename fragility. Their false-red rate on renamed builds is untested.

## 8. Repro

```
cd /fast/scratch/kotoba-r47/w2/W2DropOC6/kotoba-shokunin
python3 verifiers/verify_surfaces.py --opencode-strings /fast/scratch/kotoba-r47/w2/W2DropOC6/mutants/W-config.strings --omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings; echo "exit=$?"     # exit=0 (survivor)
python3 verifiers/verify_surfaces.py --opencode-strings /fast/scratch/kotoba-r47/w2/W2DropOC6/mutants/OBS-remove.strings --omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings; echo "exit=$?"  # exit=1 (killed)
python3 verifiers/verify_surfaces.py --self-test; echo "exit=$?"                                                                                                                # exit=0, 99 assertions
```

Mutant recipe: replace `old` with `new` exactly once in `opencode-1.19.3.strings`. The old/new bytes, offsets and both outputs are in `W2DropOC6.mutants.json`.

## 9. Recommended integrator actions (not applied)

1. Make `rule()` list only absent anchors (`:440-441`).
2. Add per-anchor and quantifier fixtures for OC-6 (K1–K5 survive today), and an OC-6 "unmatched on v2.0.26" assertion (`:1059-1063` covers OC-1 only).
3. Either witness the load condition (§7 candidates) and decide the rename trade-off explicitly, or narrow the class claim in the `:410-415` comment to what the four literals prove.

## 10. What I did NOT check

- No runtime behaviour of opencode 1.19.3 was observed. The load-condition claims (all-match walk, ungated candidate, gate) are read from dump text and the rule comments only.
- Effect `M.fn` and layer `name:` semantics are `[INFERENCE]` from dump shape, not verified against library source.
- OC-1…OC-5 were not mutated per anchor. The per-anchor self-test gap is likely shared but is unmeasured.
- The default `strings -n 4` extraction path was not exercised. The `:341` risk (a non-printable byte splitting an anchor) is untested.
- `--json` output and the other `--check` subsets were not run against mutants.
- The omp side was not mutated. Corpus gates, the fault harness, the C2 checklist and the C3 frontier were not attacked; they are outside this assignment.
- The census doc and round-47 ledger OC-6 rows were not re-read.
- The production working tree was not diffed against 7ad7fad. Everything ran on the scratch clone's committed state.
- No fix was applied, and no verifier or fixture was committed. §7 witnesses are regex checks in Python, not verifier runs.
- The labrat probe was not dispatched.

## Artifacts (`.ufo/waves/round-47/falsify/`, lane-owned)

- `W2DropOC6.md` — this report
- `W2DropOC6.mutants.json` — 16 dump mutants: old/new bytes, offsets, full and check outputs
- `W2DropOC6.code-mutants.json` — control plus K1–K5: self-test and real-dump rc
- `W2DropOC6.crossgen.txt` — v2.0.26 fixture, unmutated vs K1
- `W2DropOC6.patch` — survivor diffs (dump windows; unified diffs of `verify_surfaces.py` for K1–K5)
