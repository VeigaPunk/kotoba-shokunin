verdict: anchor-still-present — OC-2's global `<config>/AGENTS.md` loader is live in opencode 1.19.3 at dump line 443993 (byte offset 10893060), producing the same class id `opencode:config/AGENTS.md`; only surrounding names were renamed (callee `j5` → `X.join`, plugin `opencode.config.instruction` → `@opencode/Instruction`), and the BASE comment's claim that the `.claude/CLAUDE.md` candidate "no longer exists" is false at 1.19.3 (it is back, gated).

Round 47, seat `MoriR22R.C1WitnessOC2-9`. BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (worktree clean apart from untracked `.ufo/waves/` and `plans/round-47.md`, so every BASE line below is the BASE blob).

# What OC-2 is at BASE

- `verifiers/verify_surfaces.py:363-365` — comment: "the GLOBAL source — `<opencode config dir>/AGENTS.md`, resolved via `j5(r.config,"AGENTS.md")` inside `opencode.config.instruction` (the `.claude/CLAUDE.md` candidate no longer exists)".
- `verifiers/verify_surfaces.py:366-367` — `OC_GLOBAL_JOIN_RE = re.compile(r'[A-Za-z_$][A-Za-z0-9_$]*\(r\.config\s*,\s*"AGENTS\.md"\)')`. Note the shape: callee name is wildcarded, the receiver is hard-coded to the minified local `r`, the second argument is the exact literal `"AGENTS.md"`.
- `verifiers/verify_surfaces.py:405-411` — `rule()` helper; on any unmatched rule it sets `missing = list(anchors)` (line 406), i.e. every anchor is echoed, not only the absent ones (see Counterexample 1).
- `verifiers/verify_surfaces.py:417-420` — `glob = OC_GLOBAL_JOIN_RE.search(dump) is not None`, then `rule("OC-2", ["opencode:config/AGENTS.md"], glob, ['X(r.config,"AGENTS.md")'])`.
- Declared class: `verifiers/surfaces-baseline.json:252-256` — `opencode:config/AGENTS.md`, literal `AGENTS.md`, kind `loader-config`, verdict `governed`.
- Census row: `corpus/knowledge/instruction-surface-census-round13.md:207` — literal-cell note cites `j5(r.config,"AGENTS.md")` (the same stale token as the code comment).
- Existing negative fixture: `verifiers/fixtures/surfaces/strings-opencode-drop-oc2.txt:1-4` (OC-2 anchor removed; must report `opencode:config/AGENTS.md`), wired at `verifiers/verify_surfaces.py:966`.

# Witness in opencode 1.19.3 (observed, not inferred)

Substrate: `/fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings`, sha256 `f4d8f34ae02a2411eb5e30203421b6fcdfa81b83e96b768bbcf404504a297bc3` (from `SHA256SUMS`; binary `179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9`). I regenerated the dump with `strings -n 4 bin/opencode-1.19.3` and `cmp` against the frozen dump: identical (750,049 lines, 67,839,091 bytes).

Exact hit:

```
$ grep -n -o -F 'X.join(r.config,"AGENTS.md")' opencode-1.19.3.strings
443993:X.join(r.config,"AGENTS.md")          # exit 0
```

The enclosing chunk (dump line 443993, offset 10893060, one physical ~5 MB line):

```js
class Co extends ao.Service()("@opencode/Instruction"){}var hi=bo.effect(Co,s.gen(function*(){
 let o=yield*no.Service,e=yield*V.Service,r=yield*Mo.Service,t=yield*to.Service, ...
 n=[X.join(r.config,"AGENTS.md"), ...!t.disableClaudeCodePrompt?[X.join(r.home,".claude","CLAUDE.md")]:[]],
 y=["AGENTS.md", ...!t.disableClaudeCodePrompt?["CLAUDE.md"]:[], "CONTEXT.md"], ...
 g=s.fn("Instruction.systemPaths")(function*(){ ... for(let O of n) if(yield*e.existsSafe(O)){w.add(X.resolve(O));break} ... })
```

Semantic reading (static): the global source is still `<config>/AGENTS.md`, resolved as the first existing candidate of a priority list (`existsSafe` + `break`), with `~/.claude/CLAUDE.md` as a second candidate gated by `disableClaudeCodePrompt`. `r` is `yield*Mo.Service` — the config service local, which is why the regex's hard-coded `r` happens to hold here.

Rule-level confirmation from the real verifier (read-only run, snapshot binaries and dumps):

```
$ python3 -B verifiers/verify_surfaces.py \
    --omp-strings .../omp-18.12.5.strings --opencode-strings .../opencode-1.19.3.strings \
    --omp-binary .../bin/omp-18.12.5 --opencode-binary .../bin/opencode-1.19.3 --json
exit=1, 4 PASS / 3 FAIL
surfaces.opencode_extract FAIL detail names ONLY:
  opencode:api-entries/instructions, opencode:project/AGENTS.md, opencode:read-hook/AGENTS.md;
  rule(s) matched nothing: OC-1 (...), OC-4 (...), OC-6 (...)
```

OC-2, OC-3 and OC-5 are therefore matched in the live extraction; the only reported class ids are `['opencode:config/AGENTS.md', 'opencode:config/instructions']`. Direct invocation of the module's own `extract_opencode_classes(dump)` returns `OC-2 matched: true, missing: []`.

# Rename table (BASE comment/census token → 1.19.3)

| BASE token (path:line) | 1.19.3 state | hits old / new |
|---|---|---|
| `j5(r.config,"AGENTS.md")` — `verify_surfaces.py:364`, census `:207` | `X.join(r.config,"AGENTS.md")`, dump line 443993 | `grep -F 'j5(r.config,"AGENTS.md")'` → 0, exit 1; new token 1 |
| `opencode.config.instruction` — `verify_surfaces.py:364` | `@opencode/Instruction` service, same chunk | `config.instruction` → 0; `@opencode/Instruction` → 1 |
| `.claude/CLAUDE.md` "no longer exists" — `verify_surfaces.py:365` | present: `X.join(r.home,".claude","CLAUDE.md")`, gated by `disableClaudeCodePrompt` | 1 join; flag 3 occurrences on 2 dump lines |
| `ConfigInstructionPlugin.projectSource` (OC-1, adjacent) | absent; the single `projectSource` hit is an unrelated pagination field (`G.projectSource` in a session-messages cursor) | 0 live / 1 unrelated |

Sweep of plausible renamed global-join tokens, all zero-hit (each `grep -c -F`, exit 1): `path.join(r.config,"AGENTS.md")`, `config.join("AGENTS.md")`, `join(config,"AGENTS.md")`, `joinSync(`, `j5(r.config`. Positive controls: `r.config,"AGENTS.md")` → 1, `join(r.config,"AGENTS.md")` → 1, `X.join(r.config` → 1.

`X`'s binding is not co-located, but the same chunk uses `X.resolve`, `X.isAbsolute`, `X.dirname`, `X.basename`, matching node:path's surface — [INFERENCE] `X` is the node:path namespace; the rename is not byte-proven.

# Minimum discriminating anchor set for 1.19.3

The current one-anchor rule is **not discriminating** and is minifier-bound. Two synthetic controls on the frozen dump (Python, same regex as line 367):

1. rename the receiver at the live site `r`→`c`: **0 matches** while the behaviour is byte-identical → false-negative on the next minification pass.
2. rename the *project* site's receiver `L`→`r` (`jX(L.config,"AGENTS.md")`, dump line 445482 → `jX(r.config,"AGENTS.md")`): **2 matches** (offsets 10893060 and 12866409) → the generic `join(<v>.config,"AGENTS.md")` shape alone cannot tell the GLOBAL source from the PROJECT source.
3. deleting the live call (`X.join(r.config,"AGENTS.md"` → garbled suffix): **0 matches** → the rule does fail closed on removal.

Recommended minimum set (all literals, ANDed, each verified unique in this dump):

- **A1** `Instruction.systemPaths` — 1 hit. Non-minified `s.fn("Instruction.systemPaths")` name; this is the function that consumes the candidate list, so it is the stable container anchor (unlike `r`).
- **A2** `X.join(r.config,"AGENTS.md")` — 1 hit at line 443993. This is the behaviour itself. If the callee prefix is to be relaxed for future minification, use `join(<v>.config,"AGENTS.md")` (1 hit here) and keep A1 as the discriminator against the project site at line 445482.

Optional third anchor, **not** to be ANDed into OC-2: `X.join(r.home,".claude","CLAUDE.md")` — 1 hit, same line. It witnesses that the 1.19.3 global source is a *two-candidate priority list*, and it is exactly the second half of the round-14 derivation (`corpus/knowledge/opencode-extraction-round14.md:42`, which derived both `opencode:config/AGENTS.md` and `opencode:claude-home/CLAUDE.md`). ANDing it would make OC-2 FAIL the day upstream drops the `.claude` candidate again (that already happened between round 14 and round 18). The correct handling is to re-derive the round-14 class `opencode:claude-home/CLAUDE.md` as its own governed row, or record it in the excluded table with a reason — currently it is neither declared (`verifiers/surfaces-baseline.json` has 5 opencode entries, none of them claude-home) nor excluded, so a faithful re-derivation of the global source will surface an undeclared class and FAIL `surfaces.opencode_extract`.

Note on the structural substitute: `@opencode/Instruction` (1 hit, non-minified package string) can replace A1 if the function name is ever minified away; it identifies the service but not the function.

# Counterexamples and traps for the C1 re-derivation

1. **`report.missing` is not a sweep list.** `verifiers/verify_surfaces.py:406` sets `missing = list(anchors)` for *any* unmatched rule. The live run reports `OC-1 ... missing ConfigInstructionPlugin.projectSource + targets:["AGENTS.md"]`, but `grep -c -F 'targets:["AGENTS.md"]'` = 1 (dump line 445482). Using `missing` as evidence of absence would retire a live anchor. Q14's "re-verdicted with its sweep" needs an independent grep per anchor.
2. **OC-3's exclusion reason is false at 1.19.3.** `verifiers/surfaces-baseline.json:273` / reason at `:278` ("no loader consumer proven in the 2.x binary") and census `:223`. In the same 1.19.3 chunk, `Instruction.systemPaths` contains `if(T.instructions)for(let O of T.instructions){ ... (X.isAbsolute(U)? e.glob(...) : m(U)) ... }` — a real loader consumer for the config `instructions` field. OC-3 now has to move from excluded to governed (or the reason must change), independent of the OC-2 witness.
3. **Comment archaeology is not safe.** `verify_surfaces.py:365` claims the `.claude/CLAUDE.md` candidate no longer exists; it exists at 1.19.3. `verify_surfaces.py:354-355` claims the "AGENTS.md/CLAUDE.md/CONTEXT.md name-priority array is gone"; at 1.19.3 the array `y=["AGENTS.md", ..."CLAUDE.md"..., "CONTEXT.md"]` is present on the same line and drives `Instruction.find`/`findUp`. Census `:173` states `CONTEXT.md`, `disableClaudeCodePrompt`, `Instruction.resolve`, `InstructionContext.observe` were all 0 in v2.0.26; in 1.19.3 they are 1, 3 (2 lines), 1, 1. [INFERENCE] the published version line is non-monotonic (or cuts a different package), so historical "superseded-revision" claims cannot be carried into the 1.19.3 re-derivation unexamined.
4. **Line numbers are a property of the dump, not the binary.** The hit lives inside one 5 MB physical line. Anchor on dump sha256 + literal, and use `grep -o -F` (the `-n` number alone is not reproducible across different `strings` builds/flags). The frozen dump is exactly `strings -n 4` output (`cmp` exit 0 against a regeneration), so the verifier's default dump path (`verify_surfaces.py:209-233`) reproduces it.
5. **Adjacent evidence for other seats (not re-derived here):** the project source survives with a different shape at dump line 445482 (`OPENCODE_DISABLE_PROJECT_CONFIG`, `H.up({targets:["AGENTS.md"],start:S,stop:$})`, `jX(L.config,"AGENTS.md")`), and the walk-up publish path is `Instruction.resolve` + `Instructions from:` (4 dump lines), not `ReadTool.Plugin`/`SessionInstructions.load` (both 0). OC-1/OC-4 will need their own witnesses; do not copy this verdict onto them.

# Commands run (all read-only)

| command | cwd | exit |
|---|---|---|
| `git rev-parse HEAD` → `c61a973b…`; `git status --porcelain` → only `?? .ufo/waves/`, `?? plans/round-47.md` | lane | 0 |
| `sha256sum -c SHA256SUMS` → 4/4 OK | `/fast/scratch/kotoba-r47/shared` | 0 |
| `strings -n 4 bin/opencode-1.19.3` → `/tmp/oc1193_regen.strings`; `cmp` vs frozen dump | shared | 0 / 0 (identical) |
| `python3 -B verifiers/verify_surfaces.py --omp-strings … --opencode-strings … --omp-binary … --opencode-binary … --json` | lane | 1 (4 PASS / 3 FAIL; OC-2 not among FAILs) |
| `python3 -B verifiers/verify_surfaces.py --self-test` | lane | 0 ("0 failure(s) over 87 assertions") |
| Python import of `extract_opencode_classes` + `extract_opencode_classes(dump)` | lane | 0 (OC-2 matched true) |
| `grep -n -o -F` for the tokens in the rename table | shared | old token exit 1 (no match); new tokens exit 0 (match) |
| Python negative controls (delete call / rename receiver / rename project receiver) | shared | 0 (results above) |

No tools installed or upgraded; nothing to record for the tooling directive. No production file was edited; this report is the only lane write.

# What I did NOT check

- **Runtime behaviour.** I never executed the snapshot binary or the `~/.local/bin/opencode` wrapper, so the "global source is read at startup, first-existing-wins" reading is derived from the bundle's static shape and the non-minified `Instruction.systemPaths` name — not from observed file I/O. The `disableClaudeCodePrompt` default (candidate active unless env set) is [INFERENCE] from the `RuntimeFlags` map, not traced through env resolution.
- **`X` binding.** Not co-located in the dump; node:path identification is [INFERENCE] from `X.resolve/isAbsolute/dirname/basename` usage.
- **Other OpenCode rules.** OC-1/OC-4/OC-5/OC-6 were only cross-checked for the counterexamples above, not re-derived (separate seats own them).
- **omp side and `check_substrate_pins.py`.** Out of scope for this OC-2 witness.
- **Upstream opencode sources/history.** Only the frozen 1.19.3 dump was read; no repo, no network.
- **Whether the verifier's `surfaces.opencode_extract` two-way parity would still pass with the recommended 3-anchor set.** The claude-home class is currently undeclared, so that set FAILs on "extracted opencode class(es) undeclared in baseline" until the integrator adds a row or an exclusion — stated above as a consequence, not tested against a patched baseline.
