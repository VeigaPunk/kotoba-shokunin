verdict: renamed-to-X — OC-4's read-tool channel survives in opencode 1.19.3, but with no `ReadTool.Plugin` and no `SessionInstructions.load`: `ReadTool.execute` calls the `@opencode/Instruction` service inline (`e.resolve(g.messages, filepath, messageID)`), publishes `metadata.loaded`, and appends `Instructions from: <path>` entries to the read output inside a `<system-reminder>`. All four BASE anchors are 0; a 20-token rename sweep is 0/20; the behaviour is proven present at five exact dump lines.

Seat: C1WitnessOC4-9. Base `c61a973b2e02e1ded169703ddcb06466f4edd8bd`. Read-only production lane; all code experiments in `/fast/scratch/kotoba-r47/MoriR22R.C1WitnessOC4-9/lane`.

## 1. BASE state of rule OC-4

- `verifiers/verify_surfaces.py:374-381` — comment + four constants:
  - `OC_READ_FN = "ReadTool.Plugin"` (:378)
  - `OC_READ_TARGETS = 'targets:[a$]'` (:379)
  - `OC_READ_CONST = 'a$="AGENTS.md"'` (:380)
  - `OC_SESSION_LOAD = 'SessionInstructions.load'` (:381)
- `verifiers/verify_surfaces.py:428-433` — rule `OC-4`, owns class `opencode:read-hook/AGENTS.md`, matched only if all four literals are substrings of the opencode dump; fail-closed reporting names the anchors otherwise.
- Comment claims: `ReadTool.Plugin` "walks up from every read file to the project root for AGENTS.md … and calls `SessionInstructions.load`, which renders `Instructions from: <path>` synthetic entries."

Gate confirmation at BASE (scratch clone, frozen dump, only this check):
```
python3 -B verifiers/verify_surfaces.py --omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings \
  --opencode-strings /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings \
  --check surfaces.opencode_extract --json
→ exit 1; detail: "… rule(s) matched nothing: OC-1 (…); OC-4 (owns opencode:read-hook/AGENTS.md;
   missing ReadTool.Plugin + targets:[a$] + a$=\"AGENTS.md\" + SessionInstructions.load); OC-6 (…)"
```

## 2. Frozen snapshot integrity

`cd /fast/scratch/kotoba-r47/shared && sha256sum -c SHA256SUMS` → exit 0:
`bin/omp-18.12.5: OK`, `bin/opencode-1.19.3: OK`, `omp-18.12.5.strings: OK`, `opencode-1.19.3.strings: OK`.
Dump: 67,839,091 bytes, 750,049 lines. `bin/opencode-1.19.3 --version` → `1.19.3`, exit 0; dump contains `2.0.26` 0 times.

## 3. The four BASE anchors: absent

| anchor | count in dump | grep -n lines |
|---|---:|---|
| `ReadTool.Plugin` | 0 | — |
| `targets:[a$]` | 0 | — |
| `a$="AGENTS.md"` | 0 | — |
| `SessionInstructions.load` | 0 | — |

`SessionInstructions` (bare) is also 0, as are `SessionInstruction`, `ReadTool.plugin`, `ReadPlugin`. The `ReadTool` namespace itself is alive under different ids: `"ReadTool.execute"` 1 @ dump line 444228, `"ReadTool.read"` @ 445540, plus `ReadTool.inspect/list/warm/miss/…`.

## 4. Rename sweep (falsification attempt)

20 plausible renamed tokens, each `grep -cF` = 0 (loop exit 1 because the last count is zero):

`ReadTool.Plugin`, `ReadTool.plugin`, `ReadPlugin`, `readHook`, `afterRead`, `postRead`, `beforeRead`, `onFileRead`, `fileReadHook`, `instructions.load`, `Instruction.load`, `SessionInstructions`, `SessionInstruction`, `Instructions.load`, `instructionContext.load`, `read.instruction`, `readInstructions`, `hook.read`, `hooks.read`, `plugin.read`.

Generic event names that do exist are unrelated: `file.read` 6 hits are a CLI debug route (`Cli.debug.file.read`), a file-content annotation id, Node stream internals, and `client.file.read` UI calls; `onRead` hits are Node stream/undici/HTML-parser/tar internals. No plugin-style read hook exists under any of the swept names, and the `yield*y(h)` call in the read result path is `ReadTool.warm` (file-cache touch), not a hook.

## 5. Behaviour found: renamed-to-X (relocated inline)

All line numbers are `grep -n` lines in `/fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings`; all five sites live in one Bun chunk file, `chunk-2h6vy674.js` (dump file headers: line 443991 `/$bunfs/root/chunk-2h6vy674.js`, next header line 444404 `chunk-652ecseb.js`).

1. **Service identity + read-metadata consumer** — dump 443993:
   - `class Co extends ao.Service()("@opencode/Instruction")`
   - `var Wo={};so(Wo,{node:()=>bi,loaded:()=>ai,Service:()=>Co,Instruction:()=>Wo})`
   - `function qe(o){ … t.tool==="read" … let i=t.state.metadata?.loaded; … }` — collects the `loaded` file paths that the read tool publishes, per completed read part, skipping compacted parts.
   - name list used by the resolver: `y=["AGENTS.md",...!t.disableClaudeCodePrompt?["CLAUDE.md"]:[],"CONTEXT.md"]`
2. **Resolver definition** — dump 443995:
   - `h=s.fn("Instruction.find")(function*(T){for(let d of y){let w=X.resolve(X.join(T,d)); if(yield*e.existsSafe(w))return w} return})`
   - `b=s.fn("Instruction.resolve")(function*(T,d,w){ … N=X.resolve(yield*J.directory), K=X.resolve(d), G=X.dirname(K); while(G.startsWith(N)&&G!==N){ … } … q.push({filepath:W,content:`Instructions from: ${W}\n${k}`}); … } return q})`
   - exclusions: `W===K` (the file being read itself), `O.has(W)` (system paths), `U.has(W)` (`qe` claims from read metadata), plus `R.claims.get(w)` keyed by message id (dedupe across steps).
3. **Read tool executes the call** — dump 444225/444228/444233:
   - `ut=j("read",s.gen(function*(){let o=yield*V.Service,e=yield*Wo.Service, … }` (444225) — `e` is `Wo.Service`, the same-file `@opencode/Instruction` service (no import of `Wo` inside the file: `\bas Wo\b` = 0; namespace declared once at 443993; one `Wo.Service` use at the read factory).
   - `$=s.fn("ReadTool.execute")(function*(a,g){ … }` (444228)
   - `let d=yield*e.resolve(g.messages,h,g.messageID)` (444233)
   - image branch metadata: `metadata:{preview:I,truncated:!1,loaded:d.map((k)=>k.filepath)}` (444233)
   - text branch metadata: `…)`,truncated:G,loaded:d.map((W)=>W.filepath),display:{…}` (444244)
4. **Publication into the read result** — dump 444240-444243:
   - ``if(R+=`</content>`,yield*y(h),d.length>0)R+=` `` / `<system-reminder>` / `${d.map((W)=>W.content).join(\`\n\`)}` / `</system-reminder>`;`
   - each `W.content` starts with `Instructions from: ${W}` from step 2, so the synthetic entries are appended to the read tool's own output.
5. **Second, context-registry channel (not OC-4's witness)** — dump 445482: `InstructionContext.observe` loads project-walk-up `up({targets:["AGENTS.md"],start:S,stop:$})` plus `resolve(jX(L.config,"AGENTS.md"))` under `Key.make("core/instructions")`; `XP` renders `Instructions from: ${L.path}`. This is where OC-1's `targets:["AGENTS.md"]` literal lives; it is a different channel (context registration at step boundary), and should not be used to satisfy OC-4.

Counts: `Instruction.resolve` 1, `fn("Instruction.resolve")` 1, `.resolve(g.messages,` 1, `loaded:d.map(` 2, `metadata?.loaded` 1, `Instructions from: ${` 4, `@opencode/Instruction` 1.

Classification: **renamed-to-X**, specifically *relocated/inlined*: the plugin indirection was replaced by an inline service call in the read tool, the `targets:[a$]`/`a$` constants were replaced by the `Instruction.find` name list, and `SessionInstructions.load` became `Instruction.resolve`. The class id `opencode:read-hook/AGENTS.md` still names a real, live channel.

## 6. Minimum discriminating anchor set for opencode 1.19.3

Four literals, all read-tool/instruction-specific (not shared with OC-1/OC-2/OC-3/OC-6 anchors):

| # | anchor | count:lines | why it is in the minimum |
|---|---|---|---|
| 1 | `.resolve(g.messages,` | 1 @ 444233 | proves the read tool calls the resolver per read (only occurrence of this call shape) |
| 2 | `loaded:d.map(` | 2 @ 444233, 444244 | proves the read tool publishes resolved instruction paths in its metadata |
| 3 | `Instruction.resolve` | 1 @ 443995 | names the resolver that performs the walk-up and builds `Instructions from:` entries |
| 4 | `` `Instructions from: ${ `` | 4 @ 443993, 443994, 443995, 445482 | pins the rendered synthetic-entry format |

Optional corroboration (not needed for discrimination): `@opencode/Instruction` (1 @ 443993, service identity) and `metadata?.loaded` (1 @ 443993, the consumer of anchor 2).

Fail-closed tests actually run:

- Python drop-one on the full dump: rule = all four anchors; `True` on the real dump; each single anchor removed → `False`; both read-tool anchors removed → `False`. Exit 0.
- Gate level: patched OC-4 in the scratch clone (`C1WitnessOC4.patch`), reran `--check surfaces.opencode_extract` against the frozen dump → exit 1 still (OC-1/OC-6 remain) but the detail no longer lists `opencode:read-hook/AGENTS.md` or OC-4, i.e. the rule now matches and produces its class.
- Gate level mutation: dump copy with `.resolve(g.messages,` renamed to `.resolve(g.messagesX,` → exit 1 and OC-4 reappears in the FAIL detail with all four new anchors listed. Proves the re-pinned rule fails closed rather than silently shrinking.
- Cross-harness: all five candidate literals count 0 in `omp-18.12.5.strings` (0/5), so the set does not leak into the other harness if a dump is crossed.

Caveat the integrator should keep: anchors 1/2 contain minified locals (`g`, `d`, `W`); they are exact for 1.19.3 and must be re-derived at every substrate bump (that is what the fail-closed report is for). Round-14's older pair `fn("Instruction.resolve")` + `<system-reminder>` also matches this dump, but `<system-reminder>` is generic (18 hits, mostly prompt text), so I do not recommend it as the second anchor.

## 7. Semantic drift from the OC-4 comment (comment must be rewritten)

- Walk-up stop is the **session directory**, not the project root: `N=X.resolve(yield*J.directory)`; loop condition `while(G.startsWith(N)&&G!==N)` also excludes the session directory itself (dump 443995). OC-1's project walk-up uses `project.directory` separately.
- Name list is **not AGENTS.md-only**: `["AGENTS.md", "CLAUDE.md" (unless `disableClaudeCodePrompt`), "CONTEXT.md"]` (443993).
- Exclusions are four-fold: the read file itself, system paths, paths already published by prior reads (`metadata.loaded`), and per-message claims.
- Publication is dual: appended to the read output in a `<system-reminder>` **and** recorded as `metadata.loaded` on the tool result.
- Class-id history: round-14 declared `opencode:read-hook/instructions`; the current census row (`corpus/knowledge/instruction-surface-census-round13.md:208`) declares `opencode:read-hook/AGENTS.md`. Keeping the current id avoids inventory/baseline/table-parity churn; the comment should state that the channel also loads CLAUDE.md/CONTEXT.md.

## 8. Calibration notes (honest counterexamples)

- The verifier's failure detail says "missing" but prints **all** anchors on a mismatch, not only the absent ones: OC-1's BASE detail lists `targets:["AGENTS.md"]` as missing although it is present once (dump 445482). This can mislead the next re-derivation; reporting only absent anchors would be more truthful.
- The dump contains a **second read-tool copy** in `chunk-81ykj5bc.js` (dump 445357-445586): `ReadTool.list` exists there, but `ReadTool.execute`, `.resolve(`, `loaded:`, `metadata:{preview` are all absent. A dump-wide substring match can therefore be satisfied by a module copy that does not carry the channel. The chosen anchors 1/2 occur only in the executing copy (`chunk-2h6vy674.js`).
- Substrate release-line drift: 1.19.3 has the pre-2.0.26 instruction shape (`Instruction.resolve`, `InstructionContext.observe`, `system-context-builtins` present; `ConfigInstructionPlugin` and all `2.0.26` strings absent). The BASE OC-4 anchors describe the 2.0.26 shape recorded in round 44, not this build. [INFERENCE] 1.19.3 is an older release line than 2.0.26; the observed binary version is `1.19.3` and the dump contains no `2.0.26`. This affects the other opencode rules too (OC-1's function anchor is absent, OC-6's API anchors are absent), i.e. it is a substrate-level freshness issue, not only an OC-4 issue.
- `InstructionContext.observe`/`core/instructions` is live in 1.19.3 (dump 445482); whichever rule owns the context channel must not be credited by OC-4's anchors, and vice versa.

## 9. Commands run (exit codes, key output)

| command | exit | key output |
|---|---:|---|
| `sha256sum -c SHA256SUMS` (shared snapshot) | 0 | 4/4 OK |
| `grep -cF` per old anchor (loop) | 1 | 0,0,0,0 |
| rename sweep, 20 tokens (loop) | 1 | all 0 |
| Python old/new anchor rule test + drop-one | 0 | old `False`; new `True`; each removal `False` |
| `verify_surfaces.py --check surfaces.opencode_extract --json` (clone at BASE, frozen dump) | 1 | OC-4 listed unmatched with 4 old anchors |
| same, after OC-4 patch in clone | 1 | OC-4 absent from detail; OC-1/OC-6 remain |
| same, mutated dump without `.resolve(g.messages,` | 1 | OC-4 relisted with all four new anchors |
| `bin/opencode-1.19.3 --version` | 0 | `1.19.3` |
| omp dump cross-check (5 anchors) | 1 | 0/5 |

## 10. What I did NOT check

- Full 7-check `verify_surfaces.py` at default resolution, and `verifiers/check_substrate_pins.py` — not run; only `surfaces.opencode_extract` in the scratch clone.
- omp-side rules and OC-1/OC-2/OC-3/OC-5/OC-6 re-derivations; only anchor counts incident to discrimination were measured (OC-1 and OC-6 remain failing at BASE).
- Inventory/baseline/table-parity consequences of the new anchor set; no edits to `corpus/knowledge/instruction-surface-census-round13.md` or `verifiers/surfaces-baseline.json`.
- Runtime verification: no opencode session was launched; the read path executing this code is [INFERENCE] from static bundle structure (a `j("read",…)` tool factory wiring `ReadTool.execute`).
- Upstream TypeScript source or source maps: none present/read; all identifiers are from the minified bundle.
- Corpus-wide historical anchor audit beyond `corpus/knowledge/opencode-extraction-round14.md:45` and the round-44 frozen inventory; other rounds' OC-4 notes were not read.
- No tool installs or upgrades were made.

## 11. Artifacts written

- `.ufo/waves/round-47/build/C1WitnessOC4.md` (this report)
- `.ufo/waves/round-47/build/C1WitnessOC4.anchors.json` (counts, dump line numbers, binding chain, fail-closed results)
- `.ufo/waves/round-47/build/C1WitnessOC4.patch` (scratch-clone OC-4 re-pin only: constants + rule + comment; not applied to production; L1 is sole integrator)
