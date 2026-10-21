verdict: PARTIAL — the OC-4 read-hook mechanism is real at 7ad7fad, but the § B′ sentence's "nearest instruction file" is false (the loop attaches one file per ancestor directory), its "inside the instance directory" is a string-prefix test rather than path containment, and the OC-4 gate passes dumps with the call site deleted and with the read-tool injection deleted.

Lane: KotobaR47-2.W2ReadHook-2. Target: `opencode:read-hook/instructions` / OC-4 in
`corpus/knowledge/instruction-surface-census-round13.md:256` (and the identity bullet at
`:236-239`), plus the rule in `verifiers/verify_surfaces.py:421-429,479-484`.
All line refs below are at 7ad7fadfc09354b74fb66605dfb0c1182c115a2f unless prefixed
`dump:` (= `/fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings:<line>`,
sha256 `f4d8f34ae02a2411eb5e30203421b6fcdfa81b83e96b768bbcf404504a297bc3`, verified).

## Source facts (observed)

`fn("Instruction.resolve")` occurs once, exactly at `dump:443995`; `fn("ReadTool.execute")`
once, exactly at `dump:444228`; the call `e.resolve(g.messages,h,g.messageID)` exactly at
`dump:444233`. Both functions are in the same embedded module, chunk-2h6vy674.js
(`dump:443991` marker, next marker `dump:444404`), so there is no cross-chunk alias doubt:
the chunk locally declares `var Wo={}` / `so(Wo,{node:…,Service:()=>Co,Instruction:()=>Wo})`
at `dump:443993`, and the `read` tool registration (`ut=j("read", …)` at `dump:444228`)
resolves `e=yield*Wo.Service`, which therefore binds to the
`@opencode/Instruction` service whose object is `Co.of({…,resolve:b})` — `e.resolve` is the
`fn("Instruction.resolve")` body. The census evidence citation `(dump 443995)` for the
definition and `(dump 444228)` for the `ReadTool.execute` marker is exact; the verifier's
range `444228-444233` is exact for the call site.

`Instruction.resolve` body (`dump:443995`, verbatim):

```
b=s.fn("Instruction.resolve")(function*(T,d,w){
 let O=yield*g(),                 // Instruction.systemPaths() Set
 U=qe(T),                         // files already listed in prior read results' metadata.loaded
 q=[], R=yield*J.get(u),          // {claims: Map}
 N=X.resolve(yield*J.directory),  // InstanceRef.directory
 K=X.resolve(d), G=X.dirname(K);
 while(G.startsWith(N)&&G!==N){
  let W=yield*h(G);               // Instruction.find: first existing of y=[AGENTS.md, (CLAUDE.md), CONTEXT.md]
  if(!W||W===K||O.has(W)||U.has(W)){G=X.dirname(G);continue}
  let I=R.claims.get(w); if(!I)I=new Set,R.claims.set(w,I);
  if(I.has(W)){G=X.dirname(G);continue}
  I.add(W);
  let k=yield*l(W);
  if(k)q.push({filepath:W,content:`Instructions from: ${W}\n${k}`});
  G=X.dirname(G)}}             // no break, no early return
 return q});
```

`qe` (`dump:443993`) walks `T`'s message parts for `type:"tool"&&tool==="read"&&
state.status==="completed"` and collects `state.metadata?.loaded`; the call passes
`g.messages` (`dump:444233`), so the dedupe set is "files already attached in this
conversation".

`J` is `InstanceRef`: chunk-qz01fgzt exports `R as Lu`, and `R` is
`{…directory:()=>KW,…context:()=>vW,…get:()=>SW,…make:()=>K_,InstanceState:()=>R}` with
`KW=Q.map(vW,($)=>$.directory)` (`dump:446377`). So `N` is the instance directory, as the
census says.

Delivery (text branch `dump:444240-444243`; the resolve call is at `dump:444233`):

```
if(R+=`\n</content>`,yield*y(h),d.length>0)R+=`
<system-reminder>
${d.map((W)=>W.content).join(`
</system-reminder>`;return{title:b,output:R,metadata:{preview:…,loaded:d.map((W)=>W.filepath),…}}
```

## Part-by-part verdict on the § B′ sentence

| clause | verdict |
|---|---|
| `fn("Instruction.resolve")` (443995) called from `fn("ReadTool.execute")` (444228) | CONFIRMED |
| walks up *inside* the instance directory (`while(G.startsWith(N)&&G!==N)`) | CONFIRMED for genuine descendants; OVER-STRONG as a containment claim (string prefix, see C2) |
| attaches **the nearest** instruction file | REFUTED as written (see C1) |
| to the read's tool result in a `<system-reminder>` | CONFIRMED |

### C1 — "the nearest instruction file" is singular but the code accumulates (refutation)

The loop pushes at every ancestor level and never breaks; `h(G)` resolves at most one
priority file per directory. Therefore a read of `N/a/b/c.txt` with instruction files at
both `N/a/` and `N/a/b/` attaches **two** entries (nearest-first ordering), not one.
The same singular wording is repeated at `verifiers/verify_surfaces.py:421`
("the nearest ancestor instruction file").

Repro (transliteration of the exact loop, script in `W2ReadHook.repro.txt`; run with
node 24.21.0): tree `instance/AGENTS.md`, `instance/a/AGENTS.md`, `instance/a/b/AGENTS.md`,
read `instance/a/b/c.txt` →

```
CASE A (nested read): attached=2
  /tmp/rh-probe/instance/a/b/AGENTS.md
  /tmp/rh-probe/instance/a/AGENTS.md
CASE A root AGENTS.md attached: false
```

This is a simulation of the transcribed control flow, not execution of opencode; the
control flow itself is plain in `dump:443995` (no `break`, `q.push` inside the `while`).

Also omitted by the sentence, not false but scope-relevant: the read file itself
(`W===K`), `Instruction.systemPaths()` members (`O`), files already in prior read
`metadata.loaded` (`U`), and per-`messageID` claims (`claims.get(w)`, `w=g.messageID`)
are all skipped; an empty instruction file is skipped by `if(k)`. So a second read of the
same subtree attaches nothing.

### C2 — "inside the instance directory" is a string prefix, not containment (narrow refutation)

`G.startsWith(N)` where `N` has no trailing separator. A read of an absolute path under a
sibling directory whose name starts with the instance directory's name enters the loop.
Repro (same script): instance dir `/tmp/rh-probe/instance`, read
`/tmp/rh-probe/instance-other/x.txt` →

```
CASE B (prefix-sibling read): attached=1
  /tmp/rh-probe/instance-other/AGENTS.md
CASE B attached file inside N: false
```

The attached file is outside the instance directory. Absolute read paths are admitted
(`if(!z.isAbsolute(h))h=z.resolve(c.directory,h)` at `dump:444228`), so the case is
reachable subject to the read permission ask; the ordinary descendant case is
exactly as the census describes, and the loop still stops at `N` (`G!==N`), so the
instance root's own file is never attached by this hook. But "walks up inside the
instance directory" is stronger than the check: it is a prefix test on resolved path
strings, not a path-component containment test.

### Confirmed delivery detail

The resolve result is appended to the read tool's `output` string inside a single
`<system-reminder>` block (`dump:444241-444243`), content is
`Instructions from: <path>` + file text; filepaths are recorded in `metadata.loaded`,
which feeds the `qe()` dedupe. Directory reads return before `e.resolve` is reached, and
image/PDF reads call resolve for `metadata.loaded` but return an `Image/PDF read
successfully` output with no instruction text. Neither is claimed otherwise by the census.

## Gate calibration (mutation matrix)

OC-4 is a pure three-substring presence check (`verifiers/verify_surfaces.py:479-484`):
`fn("Instruction.resolve")` and `fn("ReadTool.execute")` and `<system-reminder>`, anywhere
in the dump. `<system-reminder>` has 18 occurrences on 15 lines (census `:231` says "18
hits" — re-measured exactly), and the first is prompt text explaining the tag
(`dump:443193`), not the read-tool injection (`dump:444241`).

Mutations run against copies of the frozen dump (hashes in `W2ReadHook.mutants.json`):

| mutation | result | meaning |
|---|---|---|
| M1 delete `fn("ReadTool.execute")` marker | exit 1, `FAIL … no rule: opencode:read-hook/instructions` | marker loss is caught |
| M2 keep both `fn(...)` markers, change `e.resolve(...)` to `e.notresolve(...)` | **exit 0, 7/7 PASS** | gate cannot see the caller relation its comment at `:421-425` asserts |
| M3 delete the read-tool `<system-reminder>`/`</system-reminder>` injection at `dump:444241-444243`, leave 17 other occurrences | **exit 0, 7/7 PASS** | gate cannot see that the injection site was removed |

M2/M3 are calibration gaps, not refutations of the source claim: in the frozen 1.19.3
bytes the call and the injection are present, as quoted above. But the verifier comment
("called from … `e.resolve(g.messages,h,…)`, delivered inside `<system-reminder>`")
describes semantic relations the rule does not test; `verifiers/fixtures/surfaces/
strings-opencode-extra.txt:16-19` already demonstrates the same gap — it is a synthetic
dump of three unconnected lines that the self-test expects to pass OC-4.

Two smaller gate defects observed:
- `verifiers/verify_surfaces.py:441` sets `missing = list(anchors)` whenever a rule is
  unmatched, so M1's failure message names **all three** anchors as missing even though
  only `fn("ReadTool.execute")` was removed — drift reports misdirect.
- `verifiers/fixtures/surfaces/strings-opencode-extra.txt:16` and
  `strings-opencode-drop-oc4.txt:16` cite the injected token as "443193"; that line is
  the system-prompt explanation of `<system-reminder>` tags, not the read-hook injection
  at `dump:444241`. The fixture still functions (token anywhere), which is precisely the
  weakness above; the citation is wrong as a provenance note.

Ledger row `corpus/knowledge/instruction-surface-census-round13.md:320` claims
`fn("Instruction.resolve")` 1, `fn("ReadTool.execute")` 1 — re-measured: 1 and 1. Baseline
pin `verifiers/surfaces-baseline.json:294` carries the class id.

## Commands run (exit codes)

- `sha256sum -c /fast/scratch/kotoba-r47/shared/SHA256SUMS` → 0 (4/4 OK).
- `grep -n -o 'fn("Instruction\.resolve")\|fn("ReadTool\.execute")' <dump>` → 0;
  hits at 443995 and 444228; `grep -o '<system-reminder>' | wc -l` → 18 (15 lines).
- `python3 verifiers/verify_surfaces.py --repo . --opencode-strings <frozen> --omp-strings <frozen>`
  → 0; 7/7 PASS, `opencode extraction 9/9 declared class(es) from 7/7 rules`.
- `python3 verifiers/verify_surfaces.py --self-test` → 0; `0 failure(s) over 99 assertions`.
- M1 → 1; M2 → 0; M3 → 0 (three verifier runs, same baseline/inventory).
- `node /tmp/rh-probe/repro2.mjs` → 0; output quoted above (artifact `W2ReadHook.repro.txt`).

No tools installed or upgraded.

## What I did NOT check

- The tool framework's mapping of the read tool's `output` string into the model-visible
  tool-result message is [INFERENCE]; I traced `Instruction.resolve` and the read tool's
  `output` assembly, not the tool dispatcher.
- Runtime firing: everything here is static strings-dump evidence; no opencode session was
  launched (consistent with the census's own "Honest ceiling"). The dump is a printable-run
  extraction, not decompiled bytecode; the source statements are read from those runs.
- Whether `t.disableClaudeCodePrompt` is set in practice (the read hook's `find` shares the
  gated `CLAUDE.md` priority list; the gate is visible, its runtime default is not).
- `Instruction.clear` callers / compaction behaviour, which could re-enable re-attachment.
- Other `<system-reminder>` producers among the 14 remaining lines (e.g. `dump:444800`) and
  whether any other consumer calls the Instruction service's `resolve`.
- The `systemPaths` walk in the `OPENCODE_DISABLE_PROJECT_CONFIG` branch beyond the
  `globUp(...config, config)` shape already anchored by OC-5.
- Frontier rows S012–S015, Q19, M20–M22, and the rest of C1/C2/C3 — outside this lane.
