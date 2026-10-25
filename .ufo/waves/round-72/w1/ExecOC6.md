# ExecOC6 — round 72 wave 1 (build): OC-6 re-derived on opencode v2.1.4

**Verdict.** OC-6 is honestly re-derivable on the live opencode v2.1.4 bytes; the behaviour it was
written to witness is present under new names, so the census disposition is **class kept — no
`census-removals.json` entry for `opencode:instruction-context/AGENTS.md`**. The committed rule
matches nothing because it pins three literals that no longer exist
(`InstructionContext.observe`, `system-context-builtins`, `Key.make`/`Wr.make("core/instructions")`).
The replacement is a **new v2.1.4 branch** in `opencode_context_layer_matches` that requires the whole
observed chain (key → instruction-layer render → discovery service storing `InstructionDiscovery.File`
values → its own `Ct({service,layer,deps})` registration → the `@opencode/SessionContext` layer carrying
both the builtins layer and the discovery layer → the `opencode.config.instruction` plugin feeding that
service from the all-match `AGENTS.md` walk). It matches the live dump, rejects four token-preserving
decoys and all four committed negative fixtures, and leaves the committed self-test at
`0 failure(s) over 175 assertions`. Nothing was loosened: the new branch is strictly additional
conjuncts on the same token set, and the two older generation branches stay as fixture-only regressions.

Provenance: lane `master` at `e61fd29` (wave-1 spec commit; descendant of plan freeze `7b229a1`,
base `c69711e`); `verifiers/verify_surfaces.py` is unmodified at HEAD (sha256
`4f13e3bd9d7c43b9e9d3b153b02e8f6ebb2ba57fcf66ac8ae82b9a053e809c21`, `git diff --stat HEAD --
verifiers/verify_surfaces.py` empty). Shared dump `/tmp/k72-oc-strings.txt`: sha256
`020fb25393e5ce881ac2da70222acedebc5cef2d3810d07e4625b2cde885b089`, 28,835,401 bytes, 1,237,844 lines
(== the value named in the seat item; copied once into my scratch dir so the line numbers below are
stable). Binary `~/.opencode/bin/opencode` sha256
`ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7` (the v2.1.4 value the plan records).

---

## 1. The rule as committed, on the v2.1.4 bytes: it matches nothing

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && python3 -B -c "
import sys; sys.path.insert(0,'verifiers')
import verify_surfaces as V
dump=open('/tmp/k72-oc-strings.txt',encoding='utf-8',errors='replace').read()
ids,rep=V.extract_opencode_classes(dump)
for r in rep: print(r['rule_id'], 'matched=',r['matched'], 'owns=',r['owns'], 'missing=',r['missing'])
print('IDS:', sorted(ids))"
OC-1 matched= False owns= ['opencode:instructions/AGENTS.md', 'opencode:instructions/CLAUDE.md', 'opencode:instructions/CONTEXT.md'] missing= ['["AGENTS.md" … "CONTEXT.md"]', 'disableClaudeCodePrompt']
OC-2 matched= False owns= ['opencode:config/AGENTS.md', 'opencode:claude-home/CLAUDE.md'] missing= ['X.join(<v>.config,"AGENTS.md")', 'X.join(<v>.home,".claude","CLAUDE.md")']
OC-3a matched= False owns= ['opencode:config/instructions'] missing= ['for(let <v> of <v>.instructions)']
OC-3b matched= False owns= ['opencode:config/instructions-remote'] missing= ['.instructions….filter((q)=>q.startsWith("https://")||q.startsWith("http://"))', 'Instructions from: ']
OC-4 matched= False owns= ['opencode:read-hook/instructions'] missing= ['Instruction.resolve exported as .resolve', 'ReadTool.execute calls .resolve(messages, path, id)', '<system-reminder> wraps the resolved content']
OC-5 matched= False owns= [] missing= ['OPENCODE_DISABLE_PROJECT_CONFIG', 'globUp(<v>.directory,<v>.worktree)', 'globUp(<v>.config,<v>.config)']
OC-6 matched= False owns= ['opencode:instruction-context/AGENTS.md'] missing= ['core/instructions key + InstructionContext.observe AGENTS.md walk', 'instruction-context layer registered under system-context-builtins']
IDS: []
```

Whole-gate view of the same run (committed file, both dumps supplied so the omp side is not re-dumped):

```
$ python3 -B verifiers/verify_surfaces.py --opencode-strings /tmp/k72-oc-strings.txt --omp-strings /tmp/k72-omp-strings.txt
FAIL surfaces.literal_present: 1 loader literal(s) not verifiable: opencode:instructions/CONTEXT.md (literal 'CONTEXT.md' absent from opencode dump)
PASS surfaces.no_uncovered_class: all 8 extracted loader class(es) declared
FAIL surfaces.opencode_extract: vacuity: extraction produced 0 class(es) from 7 rule(s); … rule(s) matched nothing: OC-1 (owns …); OC-2 … 
PASS surfaces.table_parity: inventory id set == baseline id set (42 ids)
PASS surfaces.literal_parity: 42 inventory row literal(s) match the baseline per id
PASS surfaces.kind_parity: 42 inventory row kind(s) match the baseline per id
PASS surfaces.excluded_reason: 8 excluded entries, all reasoned and listed in the inventory
EXIT=1        real 0m13.392s
```

(`pass 5 fail 2` — the same shape the plan's base table records, so nothing changed under me.)

Absence sweep for every literal the committed OC-6 pins (all from `/tmp/k72-oc-strings.txt`):

```
$ for s in 'InstructionContext.observe' 'system-context-builtins' 'instruction-context' 'Key.make("core/instructions")' 'Wr.make("core/instructions")' 'InstructionDiscovery.observe'; do printf '%-34s %s\n' "$s" "$(grep -c -F "$s" /tmp/k72-oc-strings.txt)"; done
InstructionContext.observe         0
system-context-builtins            0
instruction-context                0
Key.make("core/instructions")      0
Wr.make("core/instructions")       0
InstructionDiscovery.observe       0
```

---

## 2. The v2.1.4 form of what OC-6 witnessed

Every quote below is the literal `sed -n '<L>p' /tmp/k72-oc-strings.txt | grep -o '<pattern>'`
output, pasted unchanged; the rest of that dump line (each cited line is a whole minified bundle
chunk, 10^5–10^6 bytes) is dropped and is **not** part of the quote. `[INFERENCE]` marks a reading,
not a quoted byte.

| # | shape (v2.1.4) | dump line | located quote (≤25 words) |
|---|---|---|---|
| a | key factory, now bare `sA.make` | 708288 | `__=sA.make("core/instructions")` |
| b | the key rendered as an **instruction** layer (its `removed` message is the instruction one) | 708288 | `removed:()=>"Previously loaded instructions no longer apply."` |
| c | the service class — subsystem renamed `InstructionContext` → `InstructionDiscovery` | 708288 | `class WT extends U()("@opencode/InstructionDiscovery")` |
| d | the service's editor stores `InstructionDiscovery.File` values | 708288 | `add:(D)=>a.files.set(D.path,new p2(D))` |
| e | its own registered layer: wrapped factory + `var M6=_J()` | 708288 | `function _J(H){return Ct({service:WT,layer:P_(H),deps:[ti]})}var M6=_J()` |
| f | the builtins layer (`system-context-builtins` successor half) | 708294 / 708297 | `class fI extends U()("@opencode/InstructionBuiltIns")` / `Sue=Ct({service:fI,layer:S_,deps:[ls,_f]})` |
| g | the composition point: `system-context-builtins` is gone; the SessionContext layer carries both | 708343 | `class JT extends U()("@opencode/SessionContext")` / `FJ=Ct({service:JT,layer:g8,deps:[VT,yP,DA,Sue,M6` |
| h | the all-match AGENTS.md walk, now in the config-instruction plugin | 708687 | `up({targets:["AGENTS.md"],start:T,stop:V,type:"file"})` |
| i | that plugin consumes the discovery service and pushes the walk's hits into it | 708687 | `var CM=tt({id:"opencode.config.instruction"` / `new p2({path:we,content:Ae})` / `we.add(Ae)` |

Reading (`[INFERENCE]`, each clause backed by the quotes above): the **second instruction subsystem
survives intact** — key, its own layer, its own registered service, and a composition edge with the
builtins layer — but (i) the layer/composition names moved (`instruction-context` →
`instruction-discovery`, `system-context-builtins` → the `@opencode/SessionContext` layer's dep list),
and (ii) the subsystem no longer walks itself: the walk lives in the `opencode.config.instruction`
plugin, whose results are `InstructionDiscovery.File` objects pushed into the discovery state
(`we.add(Ae)`). So the old conjunction "own walk + own layer + builtins composition" split into
"own layer + builtins composition" (the subsystem) and "the walk" (its feeder); the re-derived rule
requires the feeder edge explicitly instead of pretending the walk is still internal.

---

## 3. The replacement rule (scratch copy + diff)

Deliverables (drafts; the L1 integrates):

- `.ufo/waves/round-72/w1/build/ExecOC6/verify_surfaces.py` — base file + the v2.1.4 branch
  (sha256 `f3f0b7771415c6cd71864b7fc5e577c30ce1cc64a142deb37e736605147b3264`).
- `.ufo/waves/round-72/w1/build/ExecOC6/rule.diff` — `diff -u` against the base file, 216 lines,
  179 added / 3 removed (sha256 `ade28f3b90a9283a2a9a21056402cba2f3db8fe4a1fccdeb5764f63b3398ad00`).
- `.ufo/waves/round-72/w1/build/ExecOC6/decoys.py` — regenerates every decoy from the shared dump and
  prints the rule's verdict (one command, no other dependency).

Patch applies cleanly to the committed file:

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && python3 -B -c "import ast; ast.parse(open('.ufo/waves/round-72/w1/build/ExecOC6/verify_surfaces.py').read()); print('syntax OK')"
syntax OK
$ patch -p0 --dry-run --forward < .ufo/waves/round-72/w1/build/ExecOC6/rule.diff
checking file verifiers/verify_surfaces.py
```

What the new branch (`opencode_context_layer_v214_matches`) requires, all simultaneously:

1. `class <FC> extends …("InstructionDiscovery.File")` and `class <S> extends U()("@opencode/InstructionDiscovery")`;
2. `<K>=…make("core/instructions")` in the same 60 k window as
   `GA({key:<K>,codec:…(…),read:…(…),render:{initial:…,changed:…,removed:()=>"Previously loaded instructions no longer apply."}})`
   — the **instruction** render, which is what separates it from `core/codemode`'s layer on the same
   `GA({key:…})` shape;
3. the service's editor `add:(p)=>….files.set(p.path,new <FC>(p))` and the labels
   `c("InstructionDiscovery.list")` + `c("InstructionDiscovery.load")` in that window;
4. a registration binding the service to its own layer — both shapes covered
   (`V=Ct({service,layer:L,deps:[…]})` and `function F(…){return Ct({service,layer:G(…),deps:[…]})}var V=F()`);
5. a `Ct({service:<SessionContext class>,layer:…,deps:[…]})` whose dep tokens contain **both** that
   discovery layer and the layer bound to the `@opencode/InstructionBuiltIns` service;
6. the `opencode.config.instruction` plugin window contains `yield*<service>`, the all-match
   `AGENTS.md` walk, `new <FC>({path:`, `instanceof <FC>` and a `transform((v)=>{…v.add(`.

Any single conjunct missing → the rule reports unmatched (fail-closed, with the anchor names in
`missing`). Nothing is OR-ed into acceptance except the two **retained generation branches** (1.19.4
and the 1.19.3 fixture fallback), which the live dump cannot satisfy (sweep in §1).

### Decoy: same tokens, no instruction-loading role

Primary decoy (`decoy-codemode-layer`): the live bytes with the instruction layer's render replaced by
the `core/codemode` layer's render while `__=sA.make("core/instructions")` stays bound — i.e. the
instruction key wearing the Code Mode role:

```
$ cd .ufo/waves/round-72/w1/build/ExecOC6 && python3 -B decoys.py /tmp/k72-oc-strings.txt "$S/decoys"
dump /tmp/k72-oc-strings.txt sha256 020fb25393e5ce881ac2da70222acedebc5cef2d3810d07e4625b2cde885b089 bytes 28835401
live dump                  MATCH
decoy-codemode-layer       NO-MATCH  (/tmp/…/decoys/decoy-codemode-layer.txt)
decoy-no-compose           NO-MATCH  (/tmp/…/decoys/decoy-no-compose.txt)
decoy-no-walk              NO-MATCH  (/tmp/…/decoys/decoy-no-walk.txt)
decoy-service-renamed      NO-MATCH  (/tmp/…/decoys/decoy-service-renamed.txt)
0 decoy/decoys accepted (must be 0)
EXIT=0        real 0m35.213s
```

The other three decoys keep every token and break one conjunct each: the `SessionContext` deps drop
`M6` (`decoy-no-compose`), the config plugin walks `CLAUDE.md` instead of `AGENTS.md`
(`decoy-no-walk`), and the service label is renamed while `InstructionDiscovery.File` stays
(`decoy-service-renamed`). Each one is named as unmatched by the gate itself:

```
$ for d in decoy-codemode-layer decoy-no-compose decoy-no-walk decoy-service-renamed; do python3 -B verify_surfaces.py --repo <lane> --opencode-strings "$S/$d.txt" --omp-strings /tmp/k72-omp-strings.txt --check surfaces.opencode_extract | grep -o 'OC-6 (owns[^;]*'; done
OC-6 (owns opencode:instruction-context/AGENTS.md        # ×4
```

### Branch matrix (who accepts what)

```
dump                                        committed   v2.1.4-branch   scratch-total
live-v2.1.4                                 False       True            True
strings-opencode-clean.txt (1.19.3)         True        False           True
strings-opencode-1.19.4-anchors.txt         True        False           True
strings-opencode-1.19.4-decoy-oc6.txt       False       False           False
strings-opencode-1.19.4-decoy-oc6-target.txt False      False           False
strings-opencode-drop-oc6.txt               False       False           False
strings-opencode-v2.0.26.txt                False       False           False
decoy-codemode-layer                        False       False           False
decoy-no-compose                            False       False           False
decoy-no-walk                               False       False           False
decoy-service-renamed                       False       False           False
```

Two facts this pins: (i) acceptance of the live dump comes **only** from the new branch (committed
rule on the live dump is `False`); (ii) the new branch does not swallow any committed negative fixture.
Committed self-test over the fixtures still green:

```
$ cd .ufo/waves/round-72/w1/build/ExecOC6 && python3 -B verify_surfaces.py --self-test
0 failure(s) over 175 assertions
EXIT=0        real 0m0.084s        (base file, same command: 0 failure(s) over 175 assertions)
```

(`fixtures` in the scratch dir is a symlink to `verifiers/fixtures`, because `FIXTURES` is
`Path(__file__).resolve().parent / "fixtures" / "surfaces"`.)

---

## 4. Scratch copy run with the prescribed flags — per-check result

```
$ cd .ufo/waves/round-72/w1/build/ExecOC6 && time python3 -B verify_surfaces.py \
    --repo /home/vgpnk/Projects/shokunin/kotoba-shokunin \
    --opencode-strings /tmp/k72-oc-strings.txt --omp-binary /home/vgpnk/.local/bin/omp.real
FAIL surfaces.literal_present: 1 loader literal(s) not verifiable: opencode:instructions/CONTEXT.md (literal 'CONTEXT.md' absent from opencode dump)
PASS surfaces.no_uncovered_class: all 8 extracted loader class(es) declared
FAIL surfaces.opencode_extract: declared opencode class(es) produced by no rule: opencode:claude-home/CLAUDE.md, opencode:config/AGENTS.md, opencode:config/instructions, opencode:config/instructions-remote, opencode:instructions/AGENTS.md, opencode:instructions/CLAUDE.md, opencode:instructions/CONTEXT.md, opencode:read-hook/instructions; rule(s) matched nothing: OC-1 (…); OC-2 (…); OC-3a (…); OC-3b (…); OC-4 (…); OC-5 (…)
PASS surfaces.table_parity: inventory id set == baseline id set (42 ids)
PASS surfaces.literal_parity: 42 inventory row literal(s) match the baseline per id
PASS surfaces.kind_parity: 42 inventory row kind(s) match the baseline per id
PASS surfaces.excluded_reason: 8 excluded entries, all reasoned and listed in the inventory
EXIT=1        real 0m22.216s
```

Extracted from that same output (the tool truncates long lines, so these are `grep`/`sed` over the
captured file, not retyped):

```
unmatched rule ids:                 OC-1 OC-2 OC-3a OC-3b OC-4 OC-5
OC-6 named as unmatched:            0
declared ids produced by no rule:   8 (opencode:instructions/AGENTS.md, …/CLAUDE.md, …/CONTEXT.md,
                                    opencode:config/AGENTS.md, opencode:config/instructions,
                                    opencode:config/instructions-remote,
                                    opencode:claude-home/CLAUDE.md, opencode:read-hook/instructions)
"instruction-context" in that list: 0
```

So the scratch gate is `pass 5 fail 2`, the same two failing checks as at base, but the
`opencode_extract` failure no longer names `opencode:instruction-context/AGENTS.md` or `OC-6`: **OC-6
is the one of the seven opencode checks that honest re-derivation recovers on these bytes.** The other
six (OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5) remain unmatched and belong to the sibling seats.

Note on the command: `--repo <lane root>` is required for the scratch copy because `DEFAULT_REPO` is
`Path(__file__).resolve().parent.parent` (line 160), which for a script in the build dir is the build
dir, not the lane; without it the baseline/inventory reads leave the tree. No path flag changes what
the OC-6 rule reads — it is fed the dump on the command line.

---

## 5. Census disposition

- **Keep the class.** `opencode:instruction-context/AGENTS.md`, literal `AGENTS.md`, kind
  `loader-literal`, verdict `governed` — no `verifiers/census-removals.json` entry, so the C2 ledger
  conjunct (base class kept with same `class_id`/`literal`/`context_kind`/`verdict`) is satisfiable
  for this row.
- The class **id** keeps the census's subsystem name (`instruction-context`) although v2.1.4 names the
  layer `instruction-discovery`: the id names the subsystem's role in the census, not the layer
  literal, and the id's literal `AGENTS.md` is still the walk target that feeds it. Renaming the id
  would force a census-row edit, a baseline edit and a ledger entry for no derivation gain. If the L1
  prefers the new name, that is a separate, self-consistent move (census row + baseline + ledger
  together) — it is **not** required for honesty.
- No removal ledger entry is proposed: the behaviour is witnessed (§2), so a "class removed" reason
  would be false.

---

## 6. Limits and risks

- The v2.1.4 branch pins the **composition layer name** (`@opencode/SessionContext`) and the service
  label. That is the point (a rename is drift and must go red), but it means each opencode lineage
  change costs one re-derivation of this rule — the same cost the 1.19.x → 2.1.4 move just paid.
- `_oc_v214_registrations` reads minified variable names dump-wide; a second module reusing the same
  minified pair could in principle fabricate the composition edge. Mitigations in the rule: the
  composing registration's service var must be the class tagged `@opencode/SessionContext`, the dep
  tokens must match layers bound to the `@opencode/InstructionDiscovery` and
  `@opencode/InstructionBuiltIns` service classes, and the feed conjunct is separate. Residual risk is
  recorded, not eliminated — the same limit the committed 1.19.4 branch already carried.
- The walk anchor `targets:["AGENTS.md"]` occurs exactly once in the dump (`grep -c -F` → 1) and that
  one occurrence is now the **config plugin's**, i.e. the feeder, not the subsystem. A future bundle
  that keeps the walk but drops the discovery service is rejected by conjunct 1–5 — demonstrated by
  `decoy-no-walk` (rejected) and by the live `ConfigInstructionPlugin` bytes alone being insufficient.
- The two retained older branches are kept only because the committed fixtures
  (`strings-opencode-clean.txt`, `strings-opencode-1.19.4-anchors.txt`) are still must-PASS worlds for
  this rule. If the L1 later regenerates those fixtures for v2.1.4, the older branches can be deleted
  in the same change; deleting them now would turn the committed self-test red.
- I did not run any lane gate from a bare clone and did not build a fleet sandbox: this item's evidence
  is dump-level (rule in / rule out), and the only gate-shaped runs were `verify_surfaces.py` in place
  and its self-test, both read-only over committed bytes and fixtures.

## 7. Commands, wall times, process discipline

| command | wall | note |
|---|---|---|
| committed `verify_surfaces.py` on both dumps | 13.4 s | single process |
| committed per-rule report (in-process) | 10.5 s | single process |
| scratch `--self-test` | 0.08 s | in-process fixtures |
| scratch gate, prescribed flags (dumps omp each run) | 22.2 s | single process |
| branch matrix over 11 dumps | 111.6 s | backgrounded once (job bg_12036, 127 s wall) |
| `decoys.py` (5 × 28 MB scans) | 35.2 s | single process |
| decoy gate runs (4 × 28 MB) | 74.2 s | backgrounded once (job bg_11892) |

No tool installed or upgraded (no need; python3 3.14 stdlib only). No pacman, no jj, no git write, no
fleet/sibling/lane-tree mutation: the only writes are the three draft files in
`.ufo/waves/round-72/w1/build/ExecOC6/`, this report, and a `mktemp -d /tmp/k72w1-ExecOC6.XXXX`
scratch dir (deleted before returning). The 4 decoy dumps (115 MB) were removed from scratch after
their runs; `decoys.py` regenerates them on demand.

## 8. Files written

- `.ufo/waves/round-72/w1/ExecOC6.md` (this report)
- `.ufo/waves/round-72/w1/build/ExecOC6/verify_surfaces.py` (patched scratch copy)
- `.ufo/waves/round-72/w1/build/ExecOC6/rule.diff` (unified diff against the committed file)
- `.ufo/waves/round-72/w1/build/ExecOC6/decoys.py` (decoy regenerator + verdict printer)
- `.ufo/waves/round-72/w1/build/ExecOC6/fixtures` → symlink to `verifiers/fixtures` (self-test only)

For the L1: apply `rule.diff` to `verifiers/verify_surfaces.py`, then the checks to run are
`python3 -B verifiers/verify_surfaces.py --self-test` and
`python3 -B verifiers/verify_surfaces.py --opencode-strings <v2.1.4 dump> --omp-strings <omp dump>`
(expect `pass 5 fail 2` with OC-6 absent from the unmatched rules and class list, as in §4).
