verdict: PARTIAL — attacked `opencode:instruction-context/AGENTS.md` on the frozen opencode 1.19.3 dump: the all-match walk, the ungated config candidate, the `core/instructions` key and the walk's `OPENCODE_DISABLE_PROJECT_CONFIG` gate all match the bytes, but the row's "registered as `system-context-builtins`" is a misattribution — the subsystem registers itself as its own layer `instruction-context`; `system-context-builtins` is a separate layer that depends on it and registers `core/builtins`.

Revision under attack: `7ad7fadfc09354b74fb66605dfb0c1182c115a2f` (scratch clone `/fast/scratch/kotoba-r47/w2/KotobaR47-2.W2InstrContext-2/kotoba-shokunin`, clean at that commit).
Substrate: `/fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings` (sha256 `f4d8f34a…`, regenerable: `strings -n 4 bin/opencode-1.19.3 | sha256sum` reproduces it, exit 0); `sha256sum -c SHA256SUMS` → 4/4 OK, exit 0. Binary path/sha (`179ca421…`) matches the default `verify_surfaces.py:128-131` path; `check_substrate_pins.py` → `OK 3/3 pins hold`, exit 0.

## Commands run

```
cd <scratch clone>
python3 verifiers/verify_surfaces.py
  → 7 PASS, exit 0 (incl. "opencode extraction 9/9 declared class(es) from 7/7 rules (OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6)")
python3 verifiers/verify_surfaces.py --self-test
  → "0 failure(s) over 99 assertions", exit 0
python3 verifiers/verify_surfaces.py --opencode-strings <frozen dump> --check surfaces.opencode_extract --json
  → PASS, exit 0
python3 verifiers/check_substrate_pins.py
  → OK 3/3 pins hold, exit 0
```
Mutant runs: M1–M8, exits in the table below (repro sheet `W2InstrContext.mutants.txt`, machine counts `W2InstrContext.probes.json`).

## Claim by claim (dump lines are `opencode-1.19.3.strings` lines)

### 1. All-match walk — CONFIRMED
- Call site, dump `:445482`: `U=new Set(yield*M.forEach(qE.OPENCODE_DISABLE_PROJECT_CONFIG||!h?[]:yield*H.up({targets:["AGENTS.md"],start:S,stop:$}),H.resolve))`.
- `H.up` is `FileSystem.up`, body at dump `:447206`:
  `kw=B.fn("FileSystem.up")(function*(Q){let U=[],Y=Q.start;while(!0){for(let L of Q.targets){let jx=yy(Y,L);if(yield*A.exists(jx))U.push(jx)}if(Q.stop===Y)break;let g=UW(Y);if(g===Y)break;Y=g}return U})`
  — it accumulates **every** existing target at **every** ancestor, `stop` inclusive; the caller wraps it in a `Set` (dedupe, not first-match). "All-match" is accurate.
- `S=resolve(E.directory)`, `$=resolve(E.project.directory)`; the environment renderer at dump `:445484` names these `Working directory:` and `Workspace root folder:`, so "cwd to the project root" is supported.

### 2. Ungated config candidate — CONFIRMED (with scope)
- Dump `:445482`: `F=yP.dedupe([yield*H.resolve(jX(L.config,"AGENTS.md")),...U])`; `jX` is `path.join` (`import{isAbsolute as qX,join as jX,relative as OX,sep as pX}from"path"`, dump `:445481`).
- `L=yield*DE.Service` is the `@opencode/Global` service (dump `:447217`, `class j extends t.Service()("@opencode/Global")`); its `.config` is `e.OPENCODE_CONFIG_DIR??G.config` (same line), i.e. the global config directory.
- The candidate is outside the env ternary, so `OPENCODE_DISABLE_PROJECT_CONFIG` does **not** gate it; a missing file is dropped by `readFileStringSafe`. The census's attachment of "ungated" to this candidate (`census:257`) is correct.
- Caveat: the candidate can be relocated by `OPENCODE_CONFIG_DIR`, but there is no disable gate on it.

### 3. `core/instructions` key — CONFIRMED
- `BP=XH.Key.make("core/instructions")`, dump `:445481`; registered once: `yield*I.register({key:BP,load:A().pipe(...)})`, dump `:445482` (`register({key:BP` count 1).
- `I=yield*TL.Service`; `TL` is `@opencode/v2/SystemContextRegistry` (dump `:445402`), so this is a system-context key, as claimed.

### 4. `system-context-builtins` registration — **MISMATCH**
- The subsystem's own layer is `instruction-context`:
  dump `:445482` `gX=i({name:"instruction-context",layer:uX,deps:[SH.node,DE.node,cH.node,TL.node]})` (`name:"instruction-context"` count 1).
- `system-context-builtins` is a **separate** layer:
  dump `:445487` `kX=i({name:"system-context-builtins",layer:tX,deps:[cH.node,TL.node,a_.node,SH.node,DE.node]})`.
  Its layer `tX` registers only `core/builtins` (combining `core/environment` + `core/date`, dump `:445487`) — it never calls `register({key:BP})`.
- The only relation is composition: `a_.node` is the instruction-context module node (count 1), so `system-context-builtins` builds the instruction-context layer as a dependency. The boot group includes `s_.node` (dump `:445585`), which is `kX`.
- Therefore "`instruction-context`, registered as the `system-context-builtins` context" is false as written; the true statements are "registered as the layer/plugin `instruction-context`" and "composed under `system-context-builtins` as a dependency". The key `core/instructions` is registered by the former, not the latter.
- Claim sites to correct: `corpus/knowledge/instruction-surface-census-round13.md:257` ("registered as `system-context-builtins`"), `verifiers/verify_surfaces.py:410-411` (same), `:419` (`OC_V2_REGISTRATION = "system-context-builtins"`), inherited from `corpus/knowledge/opencode-extraction-round14.md:47` and `:55`. The round's own wave-1 witness already read the layer correctly — `.ufo/waves/round-47/build/C1WitnessOC1.md:51` records `gX=i({name:"instruction-context",layer:uX,…})` — so the landed prose was not reconciled with the witness byte evidence it cites.
- The class id, `literal` (`AGENTS.md`), `context_kind` (`loader-literal`) and `governed` verdict are unaffected (`verifiers/surfaces-baseline.json:301-306`; parity checks pass). The baseline provenance (`verifiers/surfaces-baseline.json:3`) says the round-14 ids were "re-derived anchor by anchor" on 1.19.3; that is true for the four OC-6 anchors, but the registration sentence was carried over from `opencode-extraction-round14.md:55` without re-reading the two layer definitions.

### 5. `OPENCODE_DISABLE_PROJECT_CONFIG` gating — walk gated, candidate not
- The walk is gated: `qE.OPENCODE_DISABLE_PROJECT_CONFIG||!h?[]:yield*H.up(...)` (dump `:445482`). `qE` is the env-accessor object (`import{…,aD as qE}from"…/chunk-6rc9yyzv.js"`, dump `:445359`; the object defines `get OPENCODE_DISABLE_PROJECT_CONFIG(){return j("OPENCODE_DISABLE_PROJECT_CONFIG")}`, dump `:447235`).
- There is a second gate: `h` (the containment predicate computed from `relative(project, directory)`), so a cwd outside the project also empties `U`.
- The config candidate is outside both gates (§2). The census's "ungated" qualifier is correctly scoped; the row omits that the *walk* is env-gated, which is an incompleteness rather than a contradiction.

## Mutants / counterexamples

| mutant | change | exit | meaning |
|---|---|---|---|
| M1 | `system-context-builtins` → `system-context-X` | 1 | OC-6 fails, names the class |
| M2 | `Key.make("core/instructions")` → `Key.make("core/X")` | 1 | fails |
| M3 | `InstructionContext.observe` → `…X` | 1 | fails |
| M4 | `targets:["AGENTS.md"]` → `["X.md"]` | 1 | fails |
| M5 | remove `a_.node` from `system-context-builtins` deps (subsystem no longer built; `a_.node` count 1) | **0** | PASS — gate blind to wiring |
| M6 | remove the env gate from the walk | **0** | PASS — gate blind to gating |
| M7 | rename the actual layer `name:"instruction-context"` | **0** | PASS — gate blind to the real layer name |
| M8 | remove `jX(L.config,"AGENTS.md")` entirely | **0** | PASS — gate blind to the config candidate |

Repro: `python3 verifiers/verify_surfaces.py --opencode-strings <mutant>.strings --check surfaces.opencode_extract`; each mutant is one `str.replace(old,new,1)` on the frozen dump (exact strings in `W2InstrContext.mutants.txt`).

Reading: M1–M4 confirm the fail-closed anchor behaviour. M5–M8 show OC-6 is a four-string witness: it does not pin the row's behavioural claims (config candidate, env gating) and it cannot witness the registration relation — M7 passes although the layer that registers `core/instructions` has been renamed, and M5 passes although the subsystem is no longer reachable from the boot group. This is consistent with the verifier's documented "witness, not completeness" limit (`verify_surfaces.py:348-353`), but it means the "registered as `system-context-builtins`" claim is not load-bearing in the gate that is supposed to pin it.

## Adjacent calibration (not my row; not counted in the verdict)

- `census:249` (OC-1) says "first-match per directory via `globUp(T,d.directory,d.worktree)`". At 1.19.3 the name-priority walk in `Instruction.systemPaths` (dump `:443993`) uses `findUp` for the name list: `for(let O of y){let U=yield*e.findUp(O,d.directory,d.worktree); if(U.length>0){U.forEach(q=>w.add(X.resolve(q))); break}}` — i.e. first **name** with any match, then **all** ancestor matches; `FileSystem.findUp` itself accumulates all matches (dump `:447206`). `globUp` is used by `m(T)` for the declared `T.instructions` entries, not the name list. Consequently the OC-6 contrast sentence "a different load condition … than OC-1/OC-2's first-match walk" (`verify_surfaces.py:410-415`; also round14 `:47`) is not supported: v1's project walk is also `OPENCODE_DISABLE_PROJECT_CONFIG`-gated (`if(!Jr.OPENCODE_DISABLE_PROJECT_CONFIG)`, dump `:443993`) and also all-match for the winning name. The genuine differences are name priority/fallback vs AGENTS-only, the always-on config/AGENTS.md candidate, and the separate service/key. This does not change the instruction-context row's asserted facts.

## What I did NOT check

- Runtime behaviour/liveness: I never executed opencode (strings-only, per bounds). Boot-group composition (`CK … s_.node`, dump `:445585`) is static evidence that the layer is built; that the resulting `core/instructions` context reaches a model prompt is [INFERENCE], not observed.
- Whether `E.directory` is literally the process cwd; the only evidence is the "Working directory" renderer at dump `:445484`.
- The removed round-14 binary, so whether the "system-context-builtins" attribution was true on that generation is unverifiable ([INFERENCE] it was the same wrapper-layer shape, but no bytes remain).
- `OPENCODE_CONFIG_PROJECT_DISABLE` / config-level `project:false` behaviour for this subsystem (the 1.19.3 strings path shows only the env gate), and the omp side of C1.
- Other opencode rules' semantics beyond the adjacent OC-1 contrast above; C2/C3 surfaces; the fault harness and corpus gates.

No tools were installed or updated for this lane; all checks ran with the host's `python3` (3.14.8) against the frozen substrate.
