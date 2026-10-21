verdict: PARTIAL — the gate computation is real and the § B′ CLAUDE.md cells quote it exactly, but no machine check can fail on it (11/11 gate mutants exit 0; gate token fully absent still 7/7 PASS), and the same census row's per-directory load clause is false for the `Instruction.systemPaths` channel.

Rev attacked: `7ad7fadfc09354b74fb66605dfb0c1182c115a2f` (clean canonical-layout clone). Substrate: `/fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings`, sha256 `f4d8f34a…f301` (`sha256sum -c SHA256SUMS` → 4/4 OK, exit 0). All dump line numbers below are lines of that `.strings` dump.

## Observed — how `disableClaudeCodePrompt` is computed

Definition (`opencode-1.19.3.strings:447067`, chunk `chunk-6gytyv5v.js`, which is what `import{bx as to}` binds at `:443993` and re-exports at `:448836`; [INFERENCE] the `bx`→`Service` alias, resting on `t.disableClaudeCodePrompt` being the only occurrence of that field in the dump):

```js
var k=(j)=>h.boolean(j).pipe(h.withDefault(!1)),
...
disableClaudeCodePrompt:h.all({
  broad:k("OPENCODE_DISABLE_CLAUDE_CODE"),
  direct:k("OPENCODE_DISABLE_CLAUDE_CODE_PROMPT")
}).pipe(h.map((j)=>j.broad||j.direct)),
```

`⇒ disableClaudeCodePrompt = OPENCODE_DISABLE_CLAUDE_CODE || OPENCODE_DISABLE_CLAUDE_CODE_PROMPT`, each parsed as a boolean and defaulting to **false**. It is a service field of `@opencode/RuntimeFlags` (`:447067`), read once into the `Instruction` service layer as `t=yield*to.Service` (`:443993`). The sibling `disableClaudeCodeSkills` (`:447067`) is the same `broad` OR `OPENCODE_DISABLE_CLAUDE_CODE_SKILLS`; the `_PROMPT` variable does not control skills (help text for `_SKILLS` at `:446359`).

Both CLAUDE.md channels are gated by that one field (`:443993`):

```js
n=[X.join(r.config,"AGENTS.md"),...!t.disableClaudeCodePrompt?[X.join(r.home,".claude","CLAUDE.md")]:[]],
y=["AGENTS.md",...!t.disableClaudeCodePrompt?["CLAUDE.md"]:[],"CONTEXT.md"],
```

Occurrence counts (reproduced with the ledger's own command): `disableClaudeCodePrompt` **3**, on 2 dump lines (`:443993` ×2, `:447067` ×1); `OPENCODE_DISABLE_CLAUDE_CODE` (exact) **2**; `..._CLAUDE_CODE_PROMPT` **1**; `..._CLAUDE_CODE_SKILLS` **2** (definition + a doc string).

## F1 — the census/ledger cells describe the gate correctly, as far as they go

- `corpus/knowledge/instruction-surface-census-round13.md:250` quotes the exact expression `...!t.disableClaudeCodePrompt?["CLAUDE.md"]:[]` and cites dump `443993` — substring verified byte-for-byte.
- `...:253` quotes `X.join(r.home,".claude","CLAUDE.md")`, gated by the same field — verified; the join occurs only inside the gated spread.
- `...:316` ledger anchor `disableClaudeCodePrompt 3` — reproduces.
- The env names appear in the corpus at `...:443` (`OPENCODE_DISABLE_CLAUDE_CODE` / `_PROMPT`) and `corpus/knowledge/instruction-surface-remeasure-round13.md:23`; both match the dump (`broad || direct`). The § B′ cells themselves do not state the env mapping — under-documented, not false.
- `verifiers/surfaces-baseline.json:252-258,273-279` carry `literal`/`context_kind` only; `verifiers/baseline.json` has **0** occurrences of the token. The gate property lives only in prose.

No claim in the two CLAUDE.md *evidence cells* is falsified by the bytes. The defects are below.

## F2 — the verifier's gate arm cannot fail (counterexample)

`verifiers/verify_surfaces.py:450`:

```python
gated = m is not None and (OC_GATE not in m.group(0) or OC_GATE in dump)
```

If `m` matched, `m.group(0)` is a substring of `dump`, so the disjunction is always true (if the token is absent from the array, the first disjunct holds; if present, the second holds because the array came from the dump). The predicate reduces to `m is not None`. `:455` still advertises `OC_GATE` as an OC-1 anchor, but `:441` sets `missing=[]` whenever a rule matched, so the gate can never be named in output. This contradicts `corpus/knowledge/instruction-surface-census-round13.md:426` (“seven named rules, all anchors load-bearing”).

Mutation matrix on the real frozen dump (artifact `W2ClaudeGate.mutants.json` has every replacement string and observed output; `m8` is the control):

| mutant | change | exit | opencode_extract |
|---|---|---|---|
| m1 | `y` CLAUDE element ungated | 0 | 9/9, 7/7 rules PASS |
| m2 | `n` home candidate ungated | 0 | PASS |
| m3 | both ungated | 0 | PASS |
| m4 | field renamed `disableClaudeMdPrompt` in def + both uses | 0 | PASS |
| m5 | envs swapped to `SOMETHING_ELSE*` | 0 | PASS |
| m6 | definition stubbed `k("UNUSED")` | 0 | PASS |
| m7 | polarity flipped in `y` | 0 | PASS |
| m9 | uses ungated + def stubbed | 0 | PASS |
| m10 | polarity flipped in both uses | 0 | PASS |
| m11 | token **fully absent** (`claudePromptGate:k("UNUSED")`, uses ungated) | 0 | PASS |
| m12 | `if(!Jr.OPENCODE_DISABLE_PROJECT_CONFIG)` guard on the `y` walk removed | 0 | PASS |
| **m8 control** | `CLAUDE.md` dropped from `y` | **1** | FAIL names `opencode:instructions/CLAUDE.md` |

m11 is the decisive counterexample: the dump contains zero `disableClaudeCodePrompt` occurrences and the census's “gated by” cell has no referent, yet all 7 checks pass (exit 0). The name list is load-bearing (m8); the gate is decoration. No self-test fixture exercises gate removal/rename/flip: every fixture that keeps the array keeps the token in clean form (`verifiers/fixtures/surfaces/strings-opencode-{clean,extra,planted-name,drop-oc2,drop-oc3a/b,drop-oc4,drop-oc5,drop-oc6}.txt`), and `drop-oc1` removes the whole array, which name parity catches.

Repro (from a clean clone; writes only to scratch):

```
python3 - <<'EOF'
import pathlib,subprocess,sys
src=pathlib.Path('/fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings').read_text(errors='replace')
Y='...!t.disableClaudeCodePrompt?["CLAUDE.md"]:[]'
N='...!t.disableClaudeCodePrompt?[X.join(r.home,".claude","CLAUDE.md")]:[]'
DEF='disableClaudeCodePrompt:h.all({broad:k("OPENCODE_DISABLE_CLAUDE_CODE"),direct:k("OPENCODE_DISABLE_CLAUDE_CODE_PROMPT")}).pipe(h.map((j)=>j.broad||j.direct))'
t=src.replace(Y,'"CLAUDE.md"').replace(N,'[X.join(r.home,".claude","CLAUDE.md")]').replace(DEF,'claudePromptGate:k("UNUSED")')
pathlib.Path('/fast/scratch/kotoba-r47/w2/m11.strings').write_text(t,errors='replace')
print(subprocess.run([sys.executable,'verifiers/verify_surfaces.py','--opencode-strings','/fast/scratch/kotoba-r47/w2/m11.strings',
 '--omp-strings','/fast/scratch/kotoba-r47/shared/omp-18.12.5.strings']).returncode)
EOF
# observed: 0  (7/7 PASS, 9/9 declared classes)
```

## F3 — the load-condition clause is true for one channel and false for the other

`corpus/knowledge/instruction-surface-census-round13.md:443` says opencode reads CLAUDE.md “only when no `AGENTS.md` exists in that directory (first name wins in `y`)”. There are two consumers of `y` with different scopes:

- Ambient path, `Instruction.systemPaths` (`:443993`): `for(let O of y){let U=yield*e.findUp(O,d.directory,d.worktree);if(U.length>0){U.forEach(...);break}}`. `FileSystem.findUp` (`:447206`) walks from start through stop and pushes **every** existing ancestor: `while(!0){...if(Y===L)break;...L=Cx}`. The `break` is after the first *name* with any hit, so priority is global over the whole ancestor chain.
- Read-hook path, `Instruction.find` (`:443995`): `for(let d of y){...if(yield*e.existsSafe(w))return w}` for a single directory; `Instruction.resolve` (`:443995`) walks directories and calls `find(G)` per directory. Here the clause is exact.

Static counterexample: worktree `/R` contains `/R/AGENTS.md`; cwd `/R/S` contains `/R/S/CLAUDE.md` and no AGENTS.md. `systemPaths`: `findUp("AGENTS.md","/R/S","/R") = ["/R/AGENTS.md"]` → non-empty → add and `break`; `y[1]`/CLAUDE.md is never visited, so `/R/S/CLAUDE.md` is not part of the ambient instruction set — the census predicts it loads. The read hook on a file in `/R/S` returns `/R/S/CLAUDE.md` and attaches it. [INFERENCE] runtime: this is static code reading; I never executed the binary or wrapper.

The same conflation is the round-47 re-measure's “agree”: `corpus/knowledge/instruction-surface-remeasure-round13.md:24` equates “first existing name per directory” with “`break` on first name with hits, all ancestor dirs of that name collected”. Those descriptions differ exactly in the counterexample above. `LOG.md:444-448` (the per-directory clause at `:447-448`) is the accurate form for the read hook — it attributes the shadowing to `Instruction.find` — but generalizes “shadowed per directory”. Also, `:443`'s `n[1]` claim omits the sibling `break` at `:443993`: `~/.claude/CLAUDE.md` is read only if `<config>/AGENTS.md` is absent.

## F4 — secondary: `:249` cites the wrong reader/function for the same walk

`instruction-surface-census-round13.md:249` says “first-match per directory via `globUp(T,d.directory,d.worktree)` (OC-1, OC-5)”. `globUp` is the local `m` and is called only for declared `instructions` entries (`X.isAbsolute(U)?e.glob(...):m(U)`, `:443993`); the name walk uses `findUp`. Correspondingly, `verify_surfaces.py`'s OC-5 comment/constants (`:402-408`, rule `:485-492`) witness `m`'s `globUp` pair, not the inline `if(!Jr.OPENCODE_DISABLE_PROJECT_CONFIG)` before `for(let O of y)`; m12 removes that guard and the verifier stays at 7/7, exit 0.

## What holds

- Frozen substrate digests 4/4 OK; clone HEAD = `7ad7fad…`.
- `python3 verifiers/verify_surfaces.py --opencode-strings /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings --omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings` → 7 PASS, exit 0 (re-ran; 9/9 declared classes, 7/7 rules).
- The exact gate expression, both joins, both consumer sites, and the ledger count `3` are as cited at 7ad7fad. The CLAUDE.md classes exist at 1.19.3 and are genuinely env-gated in the code.

## Commands run (exit codes)

1. clone + `git checkout --detach 7ad7fad…` → 0.
2. `sha256sum -c SHA256SUMS` (shared/) → 4 OK, 0.
3. `python3 verifiers/verify_surfaces.py --opencode-strings … --omp-strings …` → 0 (7 PASS).
4. Python regex count probe over the dump → `disableClaudeCodePrompt` 3 (2 lines), broad 2, PROMPT 1, SKILLS 2; 0.
5. Mutation harness (12 files: 11 gate arms + 1 control) → artifact `W2ClaudeGate.mutants.json`; all gate arms exit 0, control exit 1.
6. `grep -rln disableClaudeCodePrompt verifiers/fixtures/` → 10 fixtures contain the token; none removes, renames, or flips the gate while keeping the array intact (`drop-oc1` removes the whole `y` array); 0.
7. Predicate truth table → `gated` true for every reachable `(in_array, in_dump)` pair; 0.

No tools installed or upgraded. No writes outside this report and its artifact.

## Did not check

- Runtime behaviour: never executed `opencode`, the snapshot binary, or the `~/.local/bin/opencode` wrapper; env parsing and file I/O are static readings, marked [INFERENCE].
- Whether `Instruction.system` (the ambient `systemPaths` consumer, `:443993`) has a live caller at session start — not traced through the minified service consumers.
- omp's `claude-md` class and the omp side of the census; C1 pins (`check_substrate_pins.py`), C2/C3 batteries, and the full after-battery were not re-run (other lanes).
- The census's v2.0.26 historical claims and the `strings-opencode-v2.0.26.txt` generation fixture.
- Which real CLAUDE.md files exist/load on this host (0-captured-injection claim).
