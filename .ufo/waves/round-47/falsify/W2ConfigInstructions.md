verdict: HOLDS — `opencode:config/instructions`'s excluded→governed re-verdict is supported: the declared-list loop globs local entries into `Instruction.systemPaths`, `Instruction.system` consumes that set, and `Instruction.system`'s output is spliced into the `system:` array of the model call inside `SessionPrompt.run`; the gate that certifies it (OC-3a) is weaker than the prose, and two mutations escape it.

# Substrate

- `/fast/scratch/kotoba-r47/shared/SHA256SUMS` recomputed: `bin/opencode-1.19.3` `179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9`, `opencode-1.19.3.strings` `f4d8f34ae02a2411eb5e30203421b6fcdfa81b83e96b768bbcf404504a297bc3` — both match the frozen manifest (`sha256sum` exit 0). All line numbers below are `opencode-1.19.3.strings` dump lines; `@N` is the character offset inside that dump line (the convention the round's C1 reports use).
- Scratch clone at `7ad7fadfc09354b74fb66605dfb0c1182c115a2f` (`/fast/scratch/kotoba-r47/w2/KotobaR47-2.W2ConfigInstructions-2/kotoba-shokunin`, `rev-parse HEAD` = 7ad7fad). Production files untouched; no tool installs, no pacman; no opencode/omp session executed.

# Finding 1 — the loop is a real local-file reader (confirmed)

`Instruction.systemPaths` (`g`) at dump 443993@7717. Three `w.add(X.resolve(...))` sites, one per source class:

| source | line@offset | code |
|---|---|---|
| config/home candidates | 443993@6801, @7811, @7852 | `n=[X.join(r.config,"AGENTS.md"),...!t.disableClaudeCodePrompt?[X.join(r.home,".claude","CLAUDE.md")]:[]]`; `for(let O of n)if(yield*e.existsSafe(O)){w.add(X.resolve(O));break}` |
| project walk (`AGENTS.md`/`CLAUDE.md`/`CONTEXT.md`) | 443993@6906, @7917, @7947, @8028 | `y=["AGENTS.md",...!t.disableClaudeCodePrompt?["CLAUDE.md"]:[],"CONTEXT.md"]`; `for(let O of y){let U=yield*e.findUp(O,d.directory,d.worktree)...;if(U.length>0){U.forEach((q)=>w.add(X.resolve(q)));break}}` |
| **config `instructions` (the attacked class)** | 443993@8071, @8241, @8325, @8378 | `if(T.instructions)for(let O of T.instructions){if(O.startsWith("https://")||O.startsWith("http://"))continue;let U=O.startsWith("~/")?X.join(r.home,O.slice(2)):O;(yield*(X.isAbsolute(U)?e.glob(X.basename(U),{cwd:X.dirname(U),absolute:!0,include:"file"}):m(U)).pipe(...)).forEach((R)=>w.add(X.resolve(R)))}` |

`m(U)` is `globUp(U, d.directory, d.worktree)` when project config is enabled, else `globUp(U, r.config, r.config)` (443993@7057–7242). `FileSystem.globUp` (447206) globs the pattern at `cwd` then walks to the stop directory: `ww=B.fn("FileSystem.globUp")(function*(Q,U,Y){let g=[],L=U;while(!0){let jx=yield*$y(Q,{cwd:L,absolute:!0,include:"file",dot:!0})...;if(g.push(...jx),Y===L)break;...L=Cx}return g})`. So an absolute `instructions` entry is globbed by basename in its own directory; a relative entry is a glob pattern applied up the project (or config) tree; every match is resolved and added. `w.add` is real consumption, not discovery-only.

# Finding 2 — `Instruction.system` consumes `systemPaths` (confirmed)

`c=s.fn("Instruction.system")` at 443993@8410; its first reads are `let T=yield*o.get(),d=yield*g()` (@8471), where `g` is systemPaths (single binding at @7717, single `g=` in the line — no shadowing; `c=` likewise single at @8410). It then reads every path in `d` with `l` (`readFileString`, concurrency 8) and renders `Instructions from: <path>` blocks (443993@8705, continued 443994); remote entries are re-filtered out of `T.instructions` (`w=(T.instructions??[]).filter(...)`, 443993@8483) and fetched by `$` with `s.timeout(5000)`, concurrency 4. Local `instructions` matches therefore flow into the returned system text.

# Finding 3 — reachable from prompt assembly (confirmed statically)

Chunk wiring, each step at a dump line:

1. The Instruction module is inside `chunk-2h6vy674.js` (filename at 443991, `// @bun` at 443992, source 443993–444402). Its namespace `Wo` is built at 443993@6206: `so(Wo,{node:()=>bi,loaded:()=>ai,Service:()=>Co,Instruction:()=>Wo})`, and its service table is 443996: `return Co.of({clear:a,systemPaths:g,system:c,find:h,resolve:b})`; class tag `Co extends ao.Service()("@opencode/Instruction")`.
2. That chunk's export map (444403) is `export{S as mo,Qr as no,eo as oo,Wo as po,Te as qo,lo as ro,tr as so,Pr as to,$o as uo,ie as vo};` — the Instruction namespace is public as `po`.
3. `chunk-cd3gkc3x.js` imports it at 443143: `import{oo as ua,po as ln,ro as eh,so as za,to as ls,vo as Co}from"/$bunfs/root/chunk-2h6vy674.js"` — so in the SessionPrompt module `ln` **is** the Instruction namespace.
4. The SessionPrompt layer (`443983@704`, `class Yl extends Ae.Service()("@opencode/SessionPrompt")`) binds `K=yield*ln.Service` at 443983@1124 (`z=yield*fo.Service` at @1200 is the same-chunk `SystemPrompt` namespace, defined at 443145@14170 as `var fo={};S(fo,{provider:…,SystemPrompt:()=>fo,Service:()=>tl})`).
5. Inside `SessionPrompt.run` (def 443988@10495), dump 443988@13714: `let[he,qe,Ue,bo,ns]=yield*s.all([z.skills(Y),z.environment(Z),K.system().pipe(s.orDie),z.mcp(Y,Q.permission),Me.toModelMessagesEffect(C,Z)])`, then @13852 `uo=[...qe,...Ue,...bo?[bo]:[],...he?[he]:[]]`, then @13976 `yield*ee.process({...,system:uo,messages:[...ns,...]})`. The third element (`Ue`) is `Instruction.system()`'s return; it is spliced into the `system` array handed to the LLM processor. `K.clear(ee.message.id)` at 443988@3156 also resolves to `Instruction.clear` (same service table), independently confirming the binding.
6. Chain inside the same module: `SessionPrompt.prompt` (def 443988@9836) calls `yield*Ao({sessionID:t.sessionID})` (@10216); `Ao=s.fn("SessionPrompt.loop")` (def 443988@15236) runs `Ke(t.sessionID)` (443988@15336); `Ke=s.fn("SessionPrompt.run")` (def 443988@10495). `SessionPrompt.command` calls `yield*we({...})` (443989@1469); `SessionPrompt.ops` exposes `prompt:(t)=>we(t)...` (443983@1413). So command/ops → prompt → loop → run → `Instruction.system` → `system:uo` → `ee.process`.

Therefore the class's recorded evidence ("consumer proven: `for(let O of T.instructions)` inside `Instruction.systemPaths` globs each local entry") is true, and is stronger than written: the collected set reaches the model's system prompt through `SessionPrompt.run`. Liveness is static-bundle evidence only (no process executed) — [INFERENCE] for actual firing in a session.

# Finding 4 — the landed re-verdict is real and consistent

- `verifiers/surfaces-baseline.json:279-285`: `opencode:config/instructions`, literal `instructions`, kind `loader-config`, verdict `governed`; the old `excluded` entry and its reason ("no loader consumer proven") are gone in the BASE→HEAD diff; `$comment`'s `assembled` note adds the round-47 channel move.
- Census: `corpus/knowledge/instruction-surface-census-round13.md:254` (governed row + evidence), `:240` (prose "proven consumer"), `:314` (ledger `excluded → re-verdicted governed`, anchor count 1). The retired v2.0.26 row survives only in the "Superseded class rows" section at `:303`, clearly historical — no live contradiction.
- Fixture: `verifiers/fixtures/surfaces/inventory-clean.md:17` carries `governed | declared list loop`, so `literal_parity`/`kind_parity` compare against a governed row.
- Commands re-run in the clone: `python3 verifiers/verify_surfaces.py` → 7 PASS lines (incl. `surfaces.opencode_extract: 9/9 declared class(es) from 7/7 rules`), **exit 0**; `python3 verifiers/check_substrate_pins.py` → 3/3 PASS, **exit 0**; `python3 verifiers/verify_surfaces.py --self-test` → `0 failure(s) over 99 assertions`, **exit 0**. These match `.ufo/waves/round-47/after/SUMMARY.md` (surfaces 0, pins 0) and are better than the before-file `.ufo/waves/round-47/before/SUMMARY.md` (surfaces default exit 2 — binary path gone; pins exit 2 DRIFT 3/3).
- Ledger anchor counts re-run over the frozen dump with the ledger's own command: `for(let O of T.instructions)` 1, `Instruction.systemPaths` 1, `Instructions from: ` 4, `X.join(r.config,"AGENTS.md")` 1, `X.join(r.home,".claude","CLAUDE.md")` 1, `disableClaudeCodePrompt` 3, `CONTEXT.md` 1, `fn("Instruction.resolve")` 1, `fn("ReadTool.execute")` 1, `InstructionContext.observe` 1, `system-context-builtins` 1, `ConfigInstructionPlugin` 0, `SessionInstructions` 0, `InstructionDiscovery` 0 — all equal the census ledger rows.

# Finding 5 — calibration: OC-3a certifies the loop header, not the read; two mutations escape

`verifiers/verify_surfaces.py:392-394` defines `OC_DECLARED_RE` on the `for(...of....instructions)` header alone; `:470-472` sets `declared = OC_DECLARED_RE.search(dump) is not None` and attaches `opencode:config/instructions` to it. No check references `w.add`, `e.glob`, `globUp`, or `d=yield*g()` for this class. Mutation tests against the real dump (mutant copies in my scratch, never the frozen substrate), full verifier with `--opencode-strings <mutant>`:

| mutant | change | full run | `--check surfaces.opencode_extract` |
|---|---|---|---|
| M1 | keep the `for` loop, delete `).forEach((R)=>w.add(X.resolve(R)))` so glob matches are discarded | **exit 0** | PASS `9/9 … 7/7 rules` |
| M2 | delete the whole `if(T.instructions)for(...)…` branch | **exit 1** | FAIL: `declared opencode class(es) produced by no rule: opencode:config/instructions; rule(s) matched nothing: OC-3a` |
| M3 | in `Instruction.system`, replace `d=yield*g()` with `d=new Set` (sever the systemPaths→system link) | **exit 0** | PASS `9/9 … 7/7 rules` |

Repro (from the clone; mutant files are `/fast/scratch/kotoba-r47/w2/KotobaR47-2.W2ConfigInstructions-2/work/mut{1,2,3}-*.strings`, sha256 `df24fdcd…`, `ccb36dbd…`, `c2b3d7c7…`): `python3 verifiers/verify_surfaces.py --opencode-strings work/mut1-no-add.strings --check surfaces.opencode_extract` → exit 0.

Consequences, honestly scoped:

- The re-verdict is **not false**: the unmutated code does glob and add local entries, and `Instruction.system` does consume the set. But the census sentence "consumer proven: … globs each local entry" is enforced only as "a loop over `.instructions` exists"; M1 keeps the sentence's verb (globs) while breaking its object (each local entry used). A future regression that silently drops the collected matches, or that stops `Instruction.system` from consuming `systemPaths`, passes all 7 checks. If the class is to stay governed on "consumer proven", OC-3a needs a second required anchor (e.g. `w.add(X.resolve(` within the same `T.instructions` branch, and `d=yield*g()` in `Instruction.system`); otherwise the gate's claim ceiling should be stated as "declaration loop present".
- Minor: the ledger's `opencode:config/instructions-remote` anchor `Instructions from: ` 4 is real but non-discriminating on its own — the 4 hits are the local render (443993), the remote render (443994), the read hook (443995), and `InstructionContext` (445482). OC-3b's `.filter(...)` regex is what discriminates; the count column alone would not.

# What I did NOT check

- No runtime: the opencode ELF and the `~/.local/bin/opencode` wrapper were never executed; no session, no config file with an `instructions` entry, no observation that `SessionPrompt.run` fires. Liveness is a static call/splice chain (`ee.process` is the LLM request prep), marked [INFERENCE] for firing.
- No check of the plugin hook `experimental.chat.system.transform` (443887) mutating the assembled `system` array, nor of `ee.process` beyond its `system:uo` argument.
- `config/instructions`'s *remote* half (`instructions-remote`) and the other 8 opencode ids were checked only for the anchor counts above; not each one's full consumer chain.
- C1's omp half (callees/lq/Xl/Fo), C2 (`trigger.no_xml_tag`, SKILL.md description), C3 (GOVERNANCE_ERRATA LOG.md:2111 pin, corpus baseline 58→60, fault harness planters), and frontier S012–S015 / Q19 / M20–M22 were not attacked here; only the after-battery values that overlap this lane (surfaces, pins, self-test) were re-run.
- `verifiers/verify_harness_claims.py` (after SUMMARY says exit 1) not examined; `corpus` gates not re-run.
