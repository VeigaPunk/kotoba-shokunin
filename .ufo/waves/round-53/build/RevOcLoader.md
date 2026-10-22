Result: DONE — both OC-4 and OC-6 semantics are fully preserved in opencode 1.19.4; the counter's two failing rules are broken only by a whole-bundle minified-identifier re-roll (`s.fn(`/`fn(` → `l(`, `Key.make` → `Wr.make`, `join as jX` → `join as Wy`), and a byte-identical 1.19.3 binary was recovered from the host's npm cacache so the diff is real, not from the recorded shape alone.

# Substrate provenance

- 1.19.4 binary (the measured one): `/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe`, sha256 `538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7`, mtime 2026-10-22 14:50:30 -0300 (= 17:50:30Z, the repin moment). File mtime and hash match the plan.
- L1 dump `/fast/scratch/hyaku/kotoba-r53/oc-1.19.4.strings` (993,160 lines): verified byte-identical to a fresh `strings -n 4` run — my own run at `/fast/scratch/hyaku/kotoba-r53/RevOcLoader/oc-1.19.4.mine.strings` has the same sha256 `2d72d83f8c90b15c4ba12037c305a838fefe03401e0762c90efdfe04f5a4bd98`.
- 1.19.3 binary RECOVERED on the host: npm cacache index entry `make-fetch-happen:request-cache:https://registry.npmjs.org/opencode-linux-x64/-/opencode-linux-x64-1.19.3.tgz` (index `/home/vgpnk/.npm/_cacache/index-v5/20/cf/12dff…`, integrity `sha512-wz+kXi7Z…`, registry fetch recorded 2026-10-22, tgz 60,356,012 B). Inner `package/bin/opencode` sha256 `179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9` — byte-identical to the substrate the census § B′ recorded for 1.19.3. Copies in my scratch: `RevOcLoader/oc-1.19.3.tgz`, `RevOcLoader/oc1193/package/bin/opencode`, `RevOcLoader/oc-1.19.3.strings` (750,049 lines, sha256 `f4d8f34ae02a2411eb5e30203421b6fcdfa81b83e96b768bbcf404504a297bc3`) — free for the L1/ExecOcRederive to reuse. No other 1.19.3 binary or dump exists on the host (npx caches checked, `~/.cache/opencode/bin` empty, `~/.opencode` empty, lane `.ufo` has no dumps, `/fast/scratch/kotoba-r47/shared/` is gone).
- Method: static `strings` extraction + pattern matching only, no execution; no network, no model calls, no installs.

# (1) What changed in each shape — real 1.19.3 ↔ 1.19.4 diff

Every OC-4/OC-6 change is a renamed minified identifier; the code shape is identical. The whole bundle was re-rolled (`l("FileSystem.up")`, `l("Instruction.find")`, `l("Instruction.system")` renamed identically), not these functions refactored. 1.19.3 line numbers below are my regenerated dump, which lands on the same lines the census recorded (443995/444228/445481-445487).

**OC-4 — read-hook channel (class `opencode:read-hook/instructions`)**

| Anchor | 1.19.3 | 1.19.4 | Verdict |
|---|---|---|---|
| hook def | `fn("Instruction.resolve")` L443995 | `l("Instruction.resolve")` L598311 | wrapper renamed only |
| caller def | `fn("ReadTool.execute")` L444228 | `l("ReadTool.execute")` L598484 | wrapper renamed only |
| call edge | `e.resolve(g.messages,h,g.messageID)` L444233 | `r.resolve(F.messages,I,F.messageID)` L598489 | identical arg shape (messages, path, messageID) |
| resolve body | `while(G.startsWith(N)&&G!==N)` (walk inside instance dir, `I(Q)` = find per dir, `R.claims.get(w)` dedup per message) L443995 | `while(Q.startsWith(q)&&Q!==q)`, `I(Q)` find, `_.claims.get(b)` L598311 | identical walk semantics; signature `(T,d,w)` → `(C,y,b)` |
| in-hook delivery | `\n<system-reminder>\n${d.map((W)=>W.content).join(\`\n` L444240, `loaded:d.map((W)=>W.filepath)` L444244 | `\n<system-reminder>\n${y.map((B)=>B.content).join(\`\n` L598496-598499, `loaded:y.map((B)=>B.filepath)` L598500 | identical template |

1.19.4 excerpts (each ≤300 chars; `\n` = real newline in the dump):

- hook def, oc-1.19.4.strings:598311: `l("Instruction.resolve")(function*(C,y,b){let E=yield*F(),U=fr(C),L=[],_=yield*ht(d),q=pe.resolve(yield*Ku),te=pe.resolve(y),Q=pe.dirname(te);while(Q.startsWith(q)&&Q!==q){let B=yield*I(Q);if(!B||B===te||E.has(B)||U.has(B)){Q=pe.dirname(Q);continue}let ie=_.claims.get(b);`
- caller def, oc-1.19.4.strings:598484: `A=l("ReadTool.execute")(function*(T,F){let v=yield*Ht,I=T.filePath;if(!ye.isAbsolute(I))I=ye.resolve(v.directory,I);let k=ye.relative(v.worktree,I)`
- call edge, oc-1.19.4.strings:598489: `let y=yield*r.resolve(F.messages,I,F.messageID),b=yield*d(I,Number(C.size),Is),E=h5(b,O.mimeType(I))`
- delivery, oc-1.19.4.strings:598496-598500 joined: `</content>\`,yield*f(I),y.length>0)_+=\`\n<system-reminder>\n${y.map((B)=>B.content).join(\`\n</system-reminder>\`;return{title:k,output:_,metadata:{…loaded:y.map((B)=>B.filepath)`

**OC-6 — InstructionContext subsystem (class `opencode:instruction-context/AGENTS.md`)**

| Anchor | 1.19.3 | 1.19.4 | Verdict |
|---|---|---|---|
| registry key | `Key.make("core/instructions")` L445481 | `Wr.make("core/instructions")` L597822 | constructor renamed only |
| observe def | `InstructionContext.observe` L445482 | same literal L597823 | unchanged |
| all-match walk | `e.up({targets:["AGENTS.md"],start:S,stop:$})` | `e.up({targets:["AGENTS.md"],start:u,stop:f})` L597823 | identical; `FileSystem.up` = exists()-loop walk, both dumps (1.19.3 L447206, 1.19.4 L596418) |
| env gate | `_.OPENCODE_DISABLE_PROJECT_CONFIG||!h?[]:` | `he.OPENCODE_DISABLE_PROJECT_CONFIG||!I?[]:` | identical condition (env disable OR cwd outside project → no walk) |
| config candidate | `jX(L.config,"AGENTS.md")` | `Wy(t.config,"AGENTS.md")` — `import{…,join as Wy}from"path"` L597822 | same ungated join; identifier renamed |
| layer + composition | `name:"instruction-context",layer:uX,deps:[SH.node,DE.node,cH.node,TL.node]`; builtins `layer:tX,deps:[cH.node,TL.node,a_.node,SH.node,DE.node]` L445482/445487 | `name:"instruction-context",layer:eD,deps:[O.node,hs,Ac,lH]`; builtins `layer:HD,deps:[Ac,lH,iD,O.node,hs]` L597823/597828 | instruction-context layer is still composed as a dep of system-context-builtins |

1.19.4 excerpts (≤300 chars):

- key, oc-1.19.4.strings:597822: `import{isAbsolute as Zy,join as Wy,relative as jy,sep as Qy}from"path";class oc extends Fe("InstructionContext.File")…var Yy=M(oc),UE=Wr.make("core/instructions"),eD=ia(m(function*(){`
- observe body, oc-1.19.4.strings:597823: `s=l("InstructionContext.observe")(function*(){let u=yield*e.resolve(n.directory),f=yield*e.resolve(n.project.directory),L=jy(f,u),I=L===""||L!==".."&&!L.startsWith(\`..${Qy}\`)&&!Zy(L),_=new Set(yield*_e(he.OPENCODE_DISABLE_PROJECT_CONFIG||!I?[]:yield*e.up({targets:["AGENTS.md"],start:u,stop:f}),e.resolve)),T=K8([yield*e.resolve(Wy(t.config,"AGENTS.md")),..._])`
- layer + registration, oc-1.19.4.strings:597823 and 597828: `iD=Re({name:"instruction-context",layer:eD,deps:[O.node,hs,Ac,lH]})` / `sD=Re({name:"system-context-builtins",layer:HD,deps:[Ac,lH,iD,O.node,hs]})`

Corroboration for the rest of the opencode rules (explains the counter's "only OC-4/OC-6 fail"): OC-1 array `f=["AGENTS.md",...!i.disableClaudeCodePrompt?["CLAUDE.md"]:[],"CONTEXT.md"]`, OC-2 `pe.join(n.config,"AGENTS.md")` / `pe.join(n.home,".claude","CLAUDE.md")`, OC-3a `if(C.instructions)for(let E of C.instructions)`, OC-3b `(C.instructions??[]).filter((L)=>L.startsWith("https://")||L.startsWith("http://"))` + `{concurrency:4}` + `Instructions from: `, OC-5 `he.OPENCODE_DISABLE_PROJECT_CONFIG` + `globUp(C,y.directory,y.worktree)` + `globUp(C,n.config,n.config)` — all present on oc-1.19.4.strings:598309-598310 (each verified, 1 match each).

# (2) Semantics verdicts

**OC-4 — YES.** `ReadTool.execute` (L598484) still calls `yield*r.resolve(F.messages,I,F.messageID)` (L598489) — `r` is the Instruction service (`@opencode/Instruction`, service def L598309-598312). `resolve` still walks strict ancestors of the read path's directory while inside the instance root (`while(Q.startsWith(q)&&Q!==q)` — same unseparated string-prefix boundary as 1.19.3), takes the first instruction file per directory by name-priority (`find` over `["AGENTS.md","CLAUDE.md","CONTEXT.md"]`), dedupes by system paths and per-message claims, and returns `{filepath,content:"Instructions from: <path>\n<content>"}` blocks. The text-file branch still appends them inside `<system-reminder>` to the tool result and reports `loaded:` filepaths (image/PDF branch sets `loaded:` only; directory branch `loaded:[]`). Identical chain in 1.19.3 (L444228→L444233→L443995→L444240→L444244).

**OC-6 — YES.** `InstructionContext.observe` still loads `AGENTS.md` under its own condition: an all-match exact-name walk `e.up({targets:["AGENTS.md"],start:<cwd>,stop:<project>})` — `FileSystem.up` tests `exists` at every level (no globbing), gated by `OPENCODE_DISABLE_PROJECT_CONFIG` OR cwd-outside-project-root — PLUS an ungated `join(config,"AGENTS.md")` global candidate. That is a different load condition than OC-1/OC-5's globUp first-match, so the separate class id is still justified. The result still registers under key `core/instructions` with baseline `Instructions from: <path>` and update text `These instructions replace all previously loaded ambient instructions.`, and the layer named `"instruction-context"` is still composed as a dependency of `system-context-builtins`, not registered as it.

# (3) Narrowest regexes I would accept

Each pattern below is validated unique-1 against BOTH dumps (so the rule would have matched 1.19.3 as well — no silent re-pin break next bump). Identifier-agnostic where the minifier renamed; name-string-locked where the literal is stable (string literals survive re-rolls; `Key`/`fn`/`jX`/`iD` do not).

**OC-4 (must require the call edge and the in-hook token — the two gaps the round-47 LIMITS note names):**

1. `OC_READ_DEFS = [A-Za-z_$][A-Za-z0-9_$]*\("Instruction\.resolve"\)` and same for `"ReadTool\.execute"` — wrapper-tolerant, call-shape required, unique-1 on both.
2. Call edge, windowed to the tool body (gap measured 1010/1008 chars): `OC_READ_EDGE = \("ReadTool\.execute"\).{0,1200}?[A-Za-z_$][A-Za-z0-9_$]*\.resolve\(\s*[A-Za-z_$][A-Za-z0-9_$]*\.messages\s*,\s*[A-Za-z_$][A-Za-z0-9_$]*\s*,\s*[A-Za-z_$][A-Za-z0-9_$]*\.messageID\s*\)` with `re.S`. The `.messages,…,.messageID` argument triple is unique to this edge (1 match per dump). Do NOT accept the bare `fn("ReadTool.execute")` + bare `<system-reminder>` pair again — that is what failed.
3. In-hook token bound to instruction-content delivery (bare `<system-reminder>` = 18 hits on 1.19.3, 16 on 1.19.4 — the decoy surface): `OC_READ_TOKEN = \n<system-reminder>\n\$\{[A-Za-z_$][A-Za-z0-9_$]*\.map\(\([A-Za-z_$][A-Za-z0-9_$]*\)=>[A-Za-z_$][A-Za-z0-9_$]*\.content\)\.join\(` — unique-1 on both (the other `\n<system-reminder>\n` openers, 3 in 1.19.4, carry plan-mode text, not a `.content` map). Optional second delivery witness: `loaded:[A-Za-z_$][A-Za-z0-9_$]*\.map\(\([A-Za-z_$][A-Za-z0-9_$]*\)=>[A-Za-z_$][A-Za-z0-9_$]*\.filepath\)` (2 hits each dump, both inside ReadTool).

**OC-6 (must require its own load condition — env gate and config candidate were the unwitnessed edges):**

1. `OC_V2_KEY = [A-Za-z_$][A-Za-z0-9_$]*\.make\("core/instructions"\)` — constructor-agnostic, key-string exact, unique-1 both dumps. (`Key.make(` itself survives elsewhere as `e.Key={make:t=>t}` Solid.js code, L849128 — so pinning the constructor name was wrong anyway.)
2. Load-condition composite (one regex, `re.S`, matches only the observe body): `OC_V2_COND = InstructionContext\.observe.{0,300}?OPENCODE_DISABLE_PROJECT_CONFIG.{0,140}?\.up\(\{targets:\["AGENTS\.md"\],start:[A-Za-z_$][A-Za-z0-9_$]*,stop:[A-Za-z_$][A-Za-z0-9_$]*\}\).{0,240}?[A-Za-z_$][A-Za-z0-9_$]*\([A-Za-z_$][A-Za-z0-9_$]*\.config,"AGENTS\.md"\)` — binds observe → env gate → all-match walk → ungated config candidate; unique-1 on both dumps (observe→config-candidate gap: 342 chars 1.19.3, 328 1.19.4).
3. Registration/composition (stable name strings, not identifiers): `OC_V2_LAYER = name:"instruction-context",layer:[A-Za-z_$][A-Za-z0-9_$]*,deps:\[[^\]]*\]` and `OC_V2_REG = system-context-builtins",layer:[A-Za-z_$][A-Za-z0-9_$]*,deps:\[[^\]]*\]` — unique-1 on both; tighter than the bare `system-context-builtins` substring at almost the same width. Keep `targets:["AGENTS.md"]` only inside the composite, never alone (it is generic — e.g. `targets:[".opencode"]` at L596579 proves the `targets:` shape recurs).

# Divergences and confidence

- Confident (observed, two-dump diff): every anchor change is an identifier rename; OC-4/OC-6 semantics preserved; proposed regexes are empirically unique-1 on both dumps. `[INFERENCE]` that `l(` is 1.19.4's instrumentation wrapper (the renamed `fn(`) and `Wr` the key constructor — positional/unique evidence only; `Wy` is proven `join` by the import line.
- Not established: runtime firing of either channel (static evidence only — the census's own honest ceiling, unchanged); whether the `claims`/`loaded` dedup produces the same user-visible order (code shape says yes, not run).
- Handoff to ExecOcRederive: only two anchors are actually broken — the `fn(` pair in OC-4 and `Key.make` in OC-6. The 1.19.3 binary + dump in `RevOcLoader/` are free for cross-checking any new rule against both substrates.
