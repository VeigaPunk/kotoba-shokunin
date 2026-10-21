verdict: OC-3's anchor is STILL PRESENT on the opencode 1.19.3 substrate (schema annotation at dump line 447094), and the class's recorded exclusion premise ("no loader consumer proven") is FALSIFIED on this substrate — `Instruction.systemPaths`/`Instruction.system` read the config `instructions` field and the prompt pipeline calls `Instruction.system`; the current anchor is non-discriminating (2 hits, one unrelated), so the minimum faithful anchor for 1.19.3 is the full annotated field literal (1 hit), optionally plus the consumer loop (1 hit) if the class is re-verdicted governed.

# C1 per-rule witness — opencode OC-3 vs opencode-1.19.3.strings

BASE: `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (verified `git -C <scratch clone> rev-parse HEAD` → that sha, exit 0).
Substrate: `/fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings`
sha256 `f4d8f34ae02a2411eb5e30203421b6fcdfa81b83e96b768bbcf404504a297bc3` (matches `SHA256SUMS` line 4);
binary `bin/opencode-1.19.3` sha256 `179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9` (matches). Dump embeds version literal `var n="1.19.3"` at `opencode-1.19.3.strings:447186`.
Line numbers below are `grep -n` line numbers of that dump; `@N` is the byte offset inside the (single, very long) string line.

## 1. What OC-3 says at BASE

- `verifiers/verify_surfaces.py:369-371` (comment): "OC-3: the config `instructions` field — schema-declared ("Additional paths or URLs supplying ambient instructions"). The field is declared; a loader consumer is NOT proven on this binary (round-18 excluded class)."
- `verifiers/verify_surfaces.py:372`: `OC_AMBIENT_SCHEMA = 'ambient instructions'`
- `verifiers/verify_surfaces.py:422-426`: `ambient = OC_AMBIENT_SCHEMA in dump`; `rule("OC-3", ["opencode:config/instructions"], ambient, ['"ambient instructions" schema annotation'])`
- Declaration side: `verifiers/surfaces-baseline.json:273-279` — `class_id opencode:config/instructions`, `context_kind loader-config`, `verdict excluded`, `reason` at :278: "schema-declared ambient-instructions list; no loader consumer proven in the 2.x binary — only the read-hook publishes file contents (round-18 re-derivation)". Census row: `verifiers/fixtures/surfaces/inventory-clean.md:16` ("excluded | schema-declared, consumer unproven").
- Fixture: `verifiers/fixtures/surfaces/strings-opencode-drop-oc3.txt:1-4` — synthetic dump with "The ambient-instructions schema annotation is gone; the rest stays", expected to make OC-3 report unmatched.

Doc nit in scope of this rule: `verifiers/verify_surfaces.py:343` says "OC-3's two entries" but the rule at :425 owns a single class id, and `opencode:config/instructions-remote` does not appear anywhere in `verifiers/surfaces-baseline.json` (`grep -c instructions-remote` → 0). The "two entries" phrasing is stale from the round-14 OC-3a/OC-3b pair.

## 2. Observed on 1.19.3 — anchor present (schema declaration)

`grep -n -o -E '.{0,200}ambient instructions.{0,200}' opencode-1.19.3.strings` (exit 0) returns exactly two lines:

1. `opencode-1.19.3.strings:447094@18712` — inside the config schema annotation:
   `...commands:e.Record(e.String,h.Info)...instructions:e.String.pipe(e.Array,e.optional).annotate({description:"Additional paths or URLs supplying ambient instructions"}),references:...`
   The exact discriminating shape starts at `447094@18607`:
   `instructions:e.String.pipe(e.Array,e.optional).annotate({description:"Additional paths or URLs supplying ambient instructions"})`
   (the surrounding line also carries `compaction`/`skills`/`commands`/`references`/`plugins`/`mcp_timeout`/`policies` config fields; `identifier:"Config"` closes the struct at `447178@67409`).
2. `opencode-1.19.3.strings:445481@9118` — UNRELATED session-baseline text near the end of a 9139-byte line:
   `update:($,P)=>\`These instructions replace all previously loaded ambient instructions.`

Counts: `ambient instructions` = 2; `"Additional paths or URLs supplying ambient instructions"` = 1; the full `instructions:e.String.pipe(...)...})` shape = 1.

So: **anchor-still-present**, not renamed. But the anchor is not unique and not tied to the schema field.

## 3. Observed — the behaviour is present AND its consumer is proven on 1.19.3

`Instruction` module (layer `@opencode/Instruction`), `opencode-1.19.3.strings:443993` (8728-byte line, imports at @0; module export `var Wo={...Service:()=>Co,Instruction:()=>Wo}` @6196):

- declaration consumer, local paths: `443993@7717` `g=s.fn("Instruction.systemPaths")(function*(){let T=yield*o.get(),...` and `443993@8071`:
  `if(T.instructions)for(let O of T.instructions){if(O.startsWith("https://")||O.startsWith("http://"))continue;let U=O.startsWith("~/")?X.join(r.home,O.slice(2)):O;(yield*(X.isAbsolute(U)?e.glob(X.basename(U),{cwd:X.dirname(U),absolute:!0,include:"file"}):m(U))...`
  → local path/glob entries of config `instructions` are resolved and merged into the instruction set.
- declaration consumer, URLs: `443993@8410` `c=s.fn("Instruction.system")(function*(){let T=yield*o.get(),d=yield*g(),w=(T.instructions??[]).filter((q)=>q.startsWith("https://")||q.startsWith("http://")),O=yield*s.forEach(Array.from(d),l,{concurrency:8}),U=yield*s.forEach(w,$,{concurrency:4});return[...Array.from(d).flatMap((q,R)=>O[R]?[\`Instructions from: ${q}` (continues `443994:${O[R]}`...])` — http(s) entries are fetched (`$` = HttpClient/execute path with a 5000 ms timeout, defined at `443993@7401`) and rendered as `Instructions from: <url>`.
- service method table: `443996` `return Co.of({clear:a,systemPaths:g,system:c,find:h,resolve:b})`.
- wiring into prompt assembly: `443988@13773` `let[he,qe,Ue,bo,ns]=yield*s.all([z.skills(Y),z.environment(Z),K.system().pipe(s.orDie),z.mcp(Y,Q.permission),Me.toModelMessagesEffect(C,Z)]),uo=[...qe,...Ue,...bo?[bo]:[],...he?[he]:[]]`; `z` is the `SystemPrompt` service (`"SystemPrompt.skills"`/`"SystemPrompt.environment"`/`"SystemPrompt.mcp"` each 1 hit), `K` is acquired at `443983@1123` `K=yield*ln.Service`.

Identity of the config object read by `o.get()` (so the consumer is provably the config `instructions` field, not a same-named other surface):
- `443993@6677` `let o=yield*no.Service` inside the `@opencode/Instruction` effect; import at `443993@977`: `import{Lu as J,Nu as xo,Su as no}from"/$bunfs/root/chunk-qz01fgzt.js"`.
- `446381` (178-byte export list) maps `Y2 as Su`; this is the ONLY export of the short name `Su` in the dump (`grep -o -E '[A-Za-z0-9_$.]+ as Su[},]'` → `Y2 as Su}`; `export{[^}]*[,{]Su[,}]` → 0), so the imported `Su` is `Y2`.
- `446377@1459` `var Y2={};p(Y2,{use:()=>j0,node:()=>V0,Service:()=>g$,Config:()=>Y2})`; `446378@22186` `class g$ extends a.Service()("@opencode/Config"){}`; `446380@5095` `K$=Q.fn("Config.get")(function*(){return yield*R.use(h,(B)=>B.config)})` and `446380` service object `g$.of({get:K$,getGlobal:w,getConsoleState:AW,update:xW,updateGlobal:z,invalidate:U,directories:m$,waitForDependencies:qW})`.
- Chain: `no` = `Su` = `Y2` = Config namespace → `no.Service` = `@opencode/Config` tag → `yield*` instance `o` → `o.get()` = `Config.get` → config object → `T.instructions`.
- [INFERENCE] The export statement line does not carry its chunk filename in a `strings -n 4` dump (file boundaries are lost), so `Y2 as Su` → `chunk-qz01fgzt.js` rests on the unique-export-name argument above, not on a preserved file header.
- [INFERENCE] 1.19.3 is the pre-2.x line: the dump still carries the round-13 "name-priority array" `n=[X.join(r.config,"AGENTS.md"),...!t.disableClaudeCodePrompt?[X.join(r.home,".claude","CLAUDE.md")]:[]],y=["AGENTS.md",...!t.disableClaudeCodePrompt?["CLAUDE.md"]:[],"CONTEXT.md"]` at `443993@6801`, which the round-18 baseline note (`surfaces-baseline.json:3`) says is gone in the 2.x binary; `2.0.26` has 0 hits in this dump and the embedded version is `1.19.3`.

Conclusion for OC-3 on 1.19.3: **behaviour present**, and stronger than the rule states — the class is not "schema-declared only". The BASE comment at `verify_surfaces.py:370` says "NOT proven on this binary" WITHOUT the "2.x" qualifier that the baseline reason keeps (`surfaces-baseline.json:278`); against the pinned 1.19.3 substrate the unqualified comment and the `excluded` verdict's consumer rationale do not hold.

## 4. Counterexample — the current anchor can pass with the schema field gone

In-process (module loaded from the BASE clone, then `extract_opencode_classes(dump)`):

- real dump → `OC-3` report `{"matched": true, "owns": ["opencode:config/instructions"], "missing": []}`; extracted ids = `['opencode:config/AGENTS.md', 'opencode:config/instructions']`.
- mutate the real dump by replacing ONLY the schema shape `instructions:e.String.pipe(e.Array,e.optional).annotate({description:"Additional paths or URLs supplying ambient instructions"})` with `instructions:e.String.pipe(e.Array,e.optional)` (description literal now 0 occurrences; `ambient instructions` still 1 occurrence, the unrelated message at 445481):
  → OC-3 still reports `{"matched": true, ...}`; extracted ids unchanged.
- The drop fixture (`strings-opencode-drop-oc3.txt`) cannot catch this because its synthetic dump contains no second `ambient instructions` occurrence; the real substrate does.

That is a live false-pass path on the pinned dump: delete/rename the declared field and OC-3 still lights up. The symmetric brittleness is that if the session-baseline message is reworded the rule FAILs while the field still exists.

## 5. Minimum discriminating anchor set for 1.19.3

Schema-only witness (keeps the current "declared field" intent):
- `instructions:e.String.pipe(e.Array,e.optional).annotate({description:"Additional paths or URLs supplying ambient instructions"})` — 1 hit at `447094@18607`; 0 after the mutation above. This binds field name + type shape + description, so a rename/retype/redescribe fails closed.
- Acceptable weaker form: the full description literal `"Additional paths or URLs supplying ambient instructions"` — 1 hit, still discriminates from the session text, but no longer binds it to the `instructions:` field.
- Do NOT keep `ambient instructions` alone: 2 hits, one unrelated.

If C1 re-verdicts the class `governed` for 1.19.3 (consumer proven, per §3), the minimum witness is the field shape plus one consumer anchor:
- `if(T.instructions)for(let O of T.instructions)` — 1 hit at `443993@8071` (local-path consumer, the round-14 OC-3a shape), or
- `w=(T.instructions??[]).filter(` — 1 hit at `443993@8483` (URL consumer).
`Instructions from: ` alone is NOT discriminating (4 hits: 443993, 443994, 443995, 445482).

Recommendation for the C1 lane: either keep the class excluded and scope the reason to the 2.x binary while tightening `OC_AMBIENT_SCHEMA`, or re-verdict it governed on 1.19.3 and witness declaration+consumer. Either way add a regression fixture whose dump contains the session message `These instructions replace all previously loaded ambient instructions.` with the schema annotation removed, and assert OC-3 unmatches.

## 6. Cross-rule context observed while running the named verifier (not my closure)

`python3 verifiers/verify_surfaces.py --repo . --omp-strings /fast/.../omp-18.12.5.strings --opencode-strings /fast/.../opencode-1.19.3.strings --check surfaces.opencode_extract --json` (run in scratch clone) → exit 1 (detail abridged with `...`; full string in the JSON artifact):

```
declared opencode class(es) produced by no rule: opencode:api-entries/instructions,
opencode:project/AGENTS.md, opencode:read-hook/AGENTS.md;
rule(s) matched nothing: OC-1 (... missing ConfigInstructionPlugin.projectSource + targets:["AGENTS.md"]);
OC-4 (... missing ReadTool.Plugin + targets:[a$] + a$="AGENTS.md" + SessionInstructions.load);
OC-6 (... missing /instructions/entries + session.instructions.entry.put)
```

This reproduces the round-47 before value (`before/SUMMARY.md`: "4 PASS / 3 FAIL ... OC-1/OC-4/OC-6 match nothing"). Raw grep counts on the same dump (exit codes: 0 when the last grep found ≥1, 1 when 0):

| anchor | hits | note |
|---|---|---|
| `ConfigInstructionPlugin.projectSource` | 0 | OC-1 |
| `targets:["AGENTS.md"]` | 1 | at 445482@340, shape `H.up({targets:["AGENTS.md"],start:S,stop:$})` — behaviour exists pre-rewrite, anchor pair does not |
| `ReadTool.Plugin` / `targets:[a$]` / `a$="AGENTS.md"` / `SessionInstructions.load` | 0 / 0 / 0 / 0 | OC-4 |
| `OPENCODE_DISABLE_PROJECT_CONFIG` / `OPENCODE_CONFIG_PROJECT_DISABLE` | 7 / 0 | OC-5 matched (OR) |
| `/instructions/entries` | 1 | 606940@5400, client methods `instructions:{entry:{list,put,remove}}`; OC-6's literal `session.instructions.entry.put` is 0 → rule FAILs |
| `X.join(r.config,"AGENTS.md")` | 1 | 443993@6804, OC-2 matched |

So the whole OC rule set is keyed to the 2.x shapes while the pinned dump is 1.19.3; OC-3's schema anchor happens to survive, OC-1/OC-4/OC-6 do not. C1 re-derivation decides the other rules; this report only closes OC-3.

## 7. Commands run (exit codes) and artifacts

- `git clone -q --no-hardlinks … /fast/scratch/kotoba-r47/C1WitnessOC3/lane && git checkout --detach c61a973…` → exit 0; `git rev-parse HEAD` → `c61a973b2e02e1ded169703ddcb06466f4edd8bd`, exit 0.
- `sha256sum opencode-1.19.3.strings bin/opencode-1.19.3` → `f4d8f34a…` / `179ca421…`, exit 0, equal to `SHA256SUMS`.
- Token sweep loop over 12 candidate tokens (counts in §2/§6); shell exit 1 only because the last token had 0 hits.
- `grep -n -o -E '.{0,200}ambient instructions.{0,200}'` → 445481, 447094, exit 0.
- `python3 verifiers/verify_surfaces.py … --check surfaces.opencode_extract --json` (scratch clone) → exit 1, detail quoted in §6.
- In-process Python: load BASE `verifiers/verify_surfaces.py`, run `extract_opencode_classes` on the real dump and on the schema-removed in-memory copy; exit 0. Machine copy: `.ufo/waves/round-47/build/C1WitnessOC3.extract.json`.
- No tools installed (nothing needed); no pacman/uv/npx actions.
- No production file written; only this report and the JSON artifact under `.ufo/waves/round-47/build/`.

## 8. What I did NOT check

- The 2.x binary (sha `d9123b9b…`) — I cannot confirm or refute its `excluded` reason here; all findings are scoped to the 1.19.3 dump.
- Runtime behaviour of `Instruction.system`/`systemPaths` (static strings only; no execution, no session run).
- Exhaustive consumer enumeration: `.system()` appears once in the dump and the prompt call site at 443988 is the one I traced; a destructured `system:c` passed around elsewhere would not show as `.system()` and was not chased.
- The omp dump; OC-3 is opencode-only.
- `verifiers/check_substrate_pins.py` and the other six surfaces checks (out of my item; C1 lane runs the gate).
- File-scope linkage of `Y2 as Su` to `chunk-qz01fgzt.js` (dump loses file boundaries) — unique-export-name argument only, marked [INFERENCE].
- Whether re-verdicting OC-3 to governed is the intended C1 decision — that is the L1's call; I supply the evidence that the current exclusion rationale is false for 1.19.3.
