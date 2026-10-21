verdict: `omp:clinerules/.clinerules` still exists in omp 18.12.5 as a live, registered rules source — `Le(qs.id,{id:"cline",displayName:"Cline",priority:40,load:cte})` at dump 897779-897784 plus the loader body 897734-897778 — so the baseline row is current and correctly `loader-literal`; `surfaces.literal_present` passes for it, and no `(group,file)` `.md` call shape can exist for it (the filename is discovered by `readdir`, and the synthetic name is `Td`'s first argument), but the class_id's group token `clinerules` is not the registered source id `cline`.

# Scope and BASE row

BASE = `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (verified: `git rev-parse HEAD` → that value, exit 0; scratch clone checked out at the same commit, exit 0).

- Baseline: `verifiers/surfaces-baseline.json:82-88` is the **only** `omp:clinerules*` entry:
  - `83: "class_id": "omp:clinerules/.clinerules"`
  - `84: "harness": "omp"`
  - `85: "literal": ".clinerules"`
  - `86: "context_kind": "loader-literal"`
  - `87: "verdict": "governed"`
- There is no second loader row for the family: `grep -n -i "cline" verifiers/surfaces-baseline.json` → lines 83 and 85 only, exit 0; no excluded entry's `reason` mentions cline.
- Census row: `corpus/knowledge/instruction-surface-census-round13.md:91` — ``| `omp:clinerules/.clinerules` | .clinerules | loader-literal | Cross-tool rule files | "Load rules from `.clinerules` (single file or directory)" |``. The family is also discussed at `corpus/knowledge/instruction-surface-census-round13.md:361` (one owner per family, not per filename).
- No patch produced: this seat made no code change. Machine-checkable witness: `.ufo/waves/round-47/build/C1ClassClinerules.witness.json`.

Substrate identity (pinned snapshot, read-only):
- `/fast/scratch/kotoba-r47/shared/bin/omp-18.12.5` sha256 `fdbc8136084c9a10439569157b2af62312e2b0d801cab54c73e89476da798e7e` — matches `SHA256SUMS` and `before/SUMMARY.md`'s omp line.
- `/fast/scratch/kotoba-r47/shared/omp-18.12.5.strings` sha256 `33df0aeffc4565967bc1a3b42621f8eade0e6e4c2ae8733319fcd484902fb301` — matches `SHA256SUMS`.
- I re-derived the dump: `strings -n 4 bin/omp-18.12.5 | sha256sum` → `33df0ae…`, exit 0; `| wc -l` → `2443339`, identical to the pinned dump's line count. So the dump is exactly what `verifiers/verify_surfaces.py:214` would produce.
- `sha256sum -c SHA256SUMS` → all 4 files OK, exit 0.

# 18.12.5 witness — the class still exists

All dump line numbers below are `/fast/scratch/kotoba-r47/shared/omp-18.12.5.strings`; byte offsets are into the pinned binary.

Module header and group constants:
- `897734: // packages/coding-agent/src/discovery/cline.ts`
- `897735: import * as wm from "path";`
- `897736: var uR = "cline";` — the registered source id (binary offset 154972314 for `var uR = "cline"`)
- `897737: var ste = "Cline";`
- `897738: var ate = 40;` — priority

Finder (project walk-up, file **or** directory):
- `897739: async function lte(u) {`
- `897741: while (true) {` / `897742: const R = await El(p);` — `El` is a cached `readdir(...,{withFileTypes:true})` (definition 861585-861595)
- `897743: const T = R.find((I) => I.name === ".clinerules");` — **the `.clinerules` literal is a runtime directory-entry comparison, not a call argument**
- `897746: path: wm.resolve(p, ".clinerules"),`
- `897750-897753:` `dirname` loop with `if (M === p) return null;` — the walk is **unbounded to the filesystem root** (no home or repo-root stop; contrast `lq` at 862812-862855)

Loader:
- `897754: async function cte(u) {`
- `897757: const T = await lte(u.cwd);` — starts at cwd, **no `u.home` and no `u.repoRoot` use** (`grep` over 897734-897784 for `Ii(|.home|repoRoot|enabledProviders|disabledProviders` → 0 hits, exit 1)
- Directory branch: `897760-897767` — `Nn(u, T.path, uR, "project", { extensions: ["md"], transform: (I,B,H,z) => Td(I,B,H,z,{stripNamePattern:/\.md$/}) })`
- File branch: `897768-897777` — `const M = await Ue(T.path);` (read) → `897771: R.push(\`Failed to read .clinerules at ${T.path}\`);` on null → `897774: const I = Ze(uR, T.path, "project");` → `897775: const B = Td("clinerules.md", M, T.path, I, { ruleName: "clinerules" });`

Registration (the loader row that keeps the class alive):
- `897779: Le(qs.id, {`
- `897780:   id: uR,`
- `897781:   displayName: ste,`
- `897782:   description: "Load rules from .clinerules (single file or directory)",`
- `897783:   priority: ate,`
- `897784:   load: cte`
- The closing `});` is present in the binary but dropped from the dump (see “Dump projection caveat”): binary offset 154972321+ shows the complete source, including `});` immediately after `load: cte`.

Capability it registers into:
- `862377: var qs = Jo({` / `862378:   id: "rules",` / `862379:   displayName: "Rules",` / `862380:   description: "Project-specific rules and constraints (Cursor MDC, Windsurf, Cline formats)"` — so `qs.id` is the `rules` capability.
- `861898-861903: function Jo(e)` — `defineCapability`, throws on duplicate id.
- `861904-861921: function Le(e, t)` — provider registration into that capability; throws `Unknown capability: "${e}"` if undefined, priority-sorted insert (`r.findIndex((o) => o.priority < t.priority)`).

Second, independent copy of the same registration data (help/description listing, not the code path):
- `557968: cline` / `557969: Cline` / `557970: Load rules from .clinerules (single file or directory)` (binary offset 96055184)
- The four string constants the code uses live in the binary's string pool (offset 97804289 `.clinerules`; 97807172-97807220 `Failed to read .clinerules at `, `clinerules.md`, `clinerules`), matching dump `566319, 566390, 566391, 566392`.

Full case-insensitive sweep for the family: `grep -n -i "clinerule" <dump>` → exactly 10 hits, all accounted for: `557970, 566319, 566390, 566391, 566392, 897743, 897746, 897771, 897775, 897782` (exit 0). The broader `grep -w "cline"` → 86 hits, but the rest are provider surfaces (`cline-pass`, model catalog, `~/.cline` table, bunfs chunk names), not instruction loaders.

# Call shape around the (group, file) literal

`load_baseline` parses this id into `group="clinerules"`, `file=".clinerules"` (`verifiers/verify_surfaces.py:284-285`). In 18.12.5 the literal-bearing call sites are:

1. `El(p)` → `R.find((I) => I.name === ".clinerules")` (897742-897743): a `readdir` result comparison.
2. `wm.resolve(p, ".clinerules")` (897746): a path join.
3. `Nn(u, T.path, uR, "project", {extensions:["md"]})` (897761): the generic scanner, whose third argument is the group **identifier** `uR` and whose file pattern is derived from `extensions` — no quoted file literal at all.
4. `Td("clinerules.md", …)` (897775): `Td` is the rule factory `(name, content, path, source, opts)` (definition 862579-862583), so the synthetic file name is the **first** argument, not the third of a registration callee.

None of these matches the extracted shape `(Id|Cl|jD[ef]|Tl|dr|GW|Co|Dl|Hj|I5|Gl|Mo)(<v>, <group>, "<file>.md")` (`verifiers/verify_surfaces.py:155-159`), and by construction the family cannot: the literal has no `.md` suffix, the directory branch never names a file, and the file branch uses a file-first callee. So `loader-literal` is structurally correct, not a re-kind escape — and adding the live 18.12.5 names to the allowlist would not change this row.

Identity mismatch (observation, not a current failure): the class id's group token is `clinerules`, but the harness registers the source as `cline` (`var uR = "cline";` 897736; `id: uR` 897780). `loader-literal` never probes the group, and the laundering arm only fires for ids the extractor actually yields, so this is inert today. `[INFERENCE]` If this row were ever re-kinded to `loader-group`, its expected pair would be `("clinerules",".clinerules")`, which no call shape can produce; the truthful registered pair would be `("cline", <something>)`. Worth normalising the label or documenting it if the census is regenerated.

# Dump projection caveat (why the dump looks like broken code)

The pinned dump is `strings -n 4` output, so every 1-3 character line is dropped. Measured: 2,443,339 non-empty lines, minimum non-empty length exactly 4, zero lines of length ≤3. Consequently every lone `}`, `});`, and `  }` in the cline module is absent from the dump — e.g. 897753 `p = M;` is followed directly by 897754 `async function cte(u) {`, and 897784 `load: cte` is followed directly by 897785 `// packages/coding-agent/src/discovery/agents.ts`.

The binary shows the complete, well-formed source: reading bytes 154,972,321-154,976,021 prints `var uR = "cline";` … `async function cte(u) { … }` … `Le(qs.id, { id: uR, … load: cte });` with all braces. **Do not read the missing braces in the dump as code damage or as evidence the loader is half-registered.** This is the projection's known floor, not a 18.12.5 anomaly.

# Scoped verifier facts (BASE verifier module, pinned dump)

Run in the scratch clone at BASE (`/fast/scratch/kotoba-r47/C1ClassClinerules-9/lane`, clean), calling helpers in isolation — no gate run:

- `load_baseline(...)` family = `['omp:clinerules/.clinerules']`, kind `loader-literal`, verdict `governed`.
- `check_literal_present(family, {"omp": dump}, …)` → `(True, '1 loader-kind entry verified against the dumps')`.
- `check_literal_present(all entries, …)` → `False`, exactly the 8 `loader-group` rows fail (`omp:agents-md/AGENTS.md`, `omp:claude-md/CLAUDE.md`, `omp:opencode/AGENTS.md`, `omp:gemini/GEMINI.md`, `omp:gemini/system.md`, `omp:gemini/SYSTEM_TEMPLATE.md`, `omp:github/copilot-instructions.md`, `omp:windsurf/memories/global_rules.md`); `omp:clinerules` is **not** among them.
- `extract_classes(dump, "omp")` → **0 (group,file) pairs**; raw `OMP_CALL_RE.findall(dump)` → 0. The live 3-arg names in 18.12.5 are `lq` (895129, 895140, 895850 — not in the allowlist) plus `Xl`/`Fo`; identifier groups resolve correctly (`constant_table`: `uR→"cline"`, `f$→"agents-md"`, `D7→"AGENTS.md"`).
- `check_table_parity` → `(True, 'inventory id set == baseline id set (38 ids)')`; `check_literal_parity` → `(True, '38 inventory row literal(s) match the baseline per id')`. So the row's literal and its census cell are current.
- `extract_opencode_classes(opencode dump)` → `['opencode:config/AGENTS.md', 'opencode:config/instructions']` (just for context; opencode is out of this family's scope).

Cross-reference for the C1 re-pin seat: this 0-pair extraction is consistent with `before/SUMMARY.md` (`surfaces --opencode-binary <npx 1.19.3>: 4 PASS / 3 FAIL (literal_present, no_uncovered_class vacuity 0/8, opencode_extract …)`) and with sibling witnesses `C1ClassCursor.md` / `C1OmpCallShapes.before.json`. The clinerules row itself is unaffected by that blindness because `loader-literal` imposes no call-shape requirement (`verifiers/verify_surfaces.py:61-66, 508-536`).

# Family-adjacent behavior (observed, useful for the class's reason/notes)

- `fO.cline` exists but carries no rules path: `862483: cline: {` / `862484: userBase: ".cline",` / `862485: userAgent: ".cline",` / `862486: projectDir: null`. No call site passes `"cline"` to `Xl`/`Fo`/`nLe` (`grep` for `Xl(u, "cline"`, `Fo(u, "cline"`, `"cline", "rules"` → 0 hits, exit 1). The only Cline rule surface is the cwd ancestor walk-up.
- Provider gating: `enabledProviders` does not gate this loader — cline is absent from the opt-out default-on map `ge` (861880-861888) and `cline.ts` never calls `Ii` (862059-862074). `disabledProviders` can still remove it entirely: `Ne` filters `e.providers.filter((s) => !F().has(s.id))` (862029-862031) before `$e` dispatch (861922-861938), and `F()` reads the `disabledProviders` sets (861876-861894).
- Directory form is top-level only: `Nn` destructures `recursive = false` (862760) and passes `pattern: "*.md"`, `gitignore: true`, `hidden: false` (862762-862775) — a `.clinerules/` directory yields only non-ignored, non-hidden `*.md` at its top level.
- File form parses frontmatter: `Td` returns `null` when `enabled === false` (862579-862582), so a `.clinerules` **file** can opt itself out; fail-to-read yields a warning, not a rule (897770-897772).
- The description is exact for this family ("single file or directory", 897782) — there is no description-vs-code overstatement here, unlike the census's cursor/windsurf notes (census 88-89).

# Counterexamples / zero-hit sweeps

- `grep -n "CLINERULES" <dump>` → 0 hits, exit 1.
- `grep -n "\.clinerules/" <dump>` → 0 hits, exit 1 (no directory-literal, no trailing-slash form; the directory case is discovered by name, not by a path literal).
- `grep -n "cline/rules\|cline/rules" <dump>` → 0 hits, exit 1 (no `omp:cline/rules`-style class).
- `grep` over the cline module block (897734-897784) for `Ii(|.home|repoRoot|enabledProviders|disabledProviders` → 0 hits, exit 1.
- The family is **not** absent, so there is no family-level zero-hit sweep to report; the zero-hit results above are negatives that bound the class, not evidence of removal.
- Caveat on the “exists” claim: a compiled-in registration proves the loader is shipped, not that it fires at runtime or that its rules reach a prompt (the verifier's own documented limit, `verifiers/verify_surfaces.py:40-42`). I did not execute omp.

# Commands run (exit codes)

```
git rev-parse HEAD                                                     # c61a973…, exit 0
git clone -q --no-hardlinks … lane && git checkout --detach c61a973…   # exit 0
sha256sum -c SHA256SUMS                                                # 4× OK, exit 0
strings -n 4 bin/omp-18.12.5 | sha256sum                               # 33df0ae…, exit 0
strings -n 4 bin/omp-18.12.5 | wc -l                                   # 2443339, exit 0
grep -n "clinerules" verifiers/surfaces-baseline.json                  # 83,85, exit 0
grep -n -i "cline" verifiers/surfaces-baseline.json                    # 83,85, exit 0
grep -n "clinerules" corpus/knowledge/instruction-surface-census-round13.md corpus/README.md  # 91 (+361), 40, exit 0
grep -n -i "clinerule" <dump>                                          # 10 hits (list above), exit 0
grep -n -i "clinerule" <binary>                                        # 9 lines, exit 0
grep -c -w "cline" <dump>                                              # 86, exit 0
grep -aob "var uR = \"cline\"" <binary>                                # 154972314, exit 0
grep -aob "Load rules from .clinerules" <binary>                       # 96055184, 154973521, exit 0
grep -aob "clinerules" <binary>                                        # 11 offsets in 3 regions, exit 0
node (scratch): min non-empty dump line length                         # 4; ≤3-char lines: 0, exit 0
python3 -B (scratch clone): check_literal_present(family)              # True, exit 0
python3 -B (scratch clone): check_literal_present(all)                 # False; 8 loader-group rows, clinerules absent, exit 0
python3 -B (scratch clone): extract_classes(dump,"omp")                # 0 pairs, exit 0
python3 -B (scratch clone): table_parity / literal_parity              # True / True, exit 0
grep -n "CLINERULES" <dump>                                            # 0, exit 1
grep -n "\.clinerules/" <dump>                                         # 0, exit 1
grep -n "cline/rules" <dump>                                           # 0, exit 1
awk 897734-897784 | grep -n "Ii(\|.home\|repoRoot\|…Providers"        # 0, exit 1
```

Scratch clone: `/fast/scratch/kotoba-r47/C1ClassClinerules-9/lane` at `c61a973b2e02e1ded169703ddcb06466f4edd8bd`, no edits (`git status --porcelain` empty). No writes to the fleet repo except this report and `C1ClassClinerules.witness.json`.

# NOT checked

- Did not run `verifiers/verify_surfaces.py` as a full gate, and did not run `check_substrate_pins.py`, in the fleet repo or the clone; all verifier results above come from calling `load_baseline`, `check_literal_present`, `extract_classes`, `check_table_parity`, `check_literal_parity` in isolation. The 8-row failure list is the helper's own output, not a gate run.
- Did not execute the omp binary or any runtime probe; no proof the loader fires, no proof the rules reach a prompt.
- Did not trace the rules capability's full consumer path (TTSP/rulebook injection) beyond the `_n(qs.id, …)` call sites at 1162261/1214514/1214527; the enabled/disabledProviders statements are limited to `Ne`/`$e`/`Ii` and were not validated at runtime.
- Did not inspect any older omp build, so “still exists” is a claim about 18.12.5 only, not a diff against the round-13/18 substrate that first recorded the row.
- Did not check the opencode dump for a Cline-equivalent surface (out of family scope); the `cline-pass` / model-catalog hits were classified by name only, not audited.
- Did not verify that the help/description listing at 557968-557970 is generated from the registrations (it is an independent copy either way).
- Did not resolve why the binary embeds a full source-text blob at ~155 MB (provenance of that copy not investigated).
- No tool installs or upgrades were performed; nothing installed, no pacman transaction attempted.
