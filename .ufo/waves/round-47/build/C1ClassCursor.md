verdict: `omp:cursor/rules` still exists in omp 18.12.5 as a live, registered rules loader (`Le(qs.id,{id:"cursor",load:Fte})` + `Xl/Fo(u,"cursor","rules")`), so the family is present, the baseline row is correctly `loader-literal`, and `surfaces.literal_present` passes for it — but the verifier's docstring witness `Cl(e,"cursor","rules")` (verifiers/verify_surfaces.py:64) has 0 hits in 18.12.5, the live callees are `Xl`/`Fo`, and `extract_classes(dump,'omp')` returns 0 pairs on the pinned dump (C1 re-pin must add the live names; the cursor row's kind and witness are unaffected).

# Scope

Family = every baseline entry whose `class_id` starts `omp:cursor`, plus the cursor module's loader registrations and the two family-adjacent `discovery` rows whose `reason` names cursor.
- Baseline has exactly one `omp:cursor*` entry out of 38 class_ids: `verifiers/surfaces-baseline.json:62-67` — `class_id: omp:cursor/rules`, `literal: rules`, `context_kind: loader-literal`, `verdict: governed`. (`grep -n 'cursor' verifiers/surfaces-baseline.json` → 62, plus 186/194 inside the two discovery reasons.)
- Census row: `corpus/knowledge/instruction-surface-census-round13.md:88` (same id/literal/kind).
- No patch produced: this seat made no code change. Artifact: `.ufo/waves/round-47/build/C1ClassCursor.shapes.json` (2.6 KiB, live `.md` call shapes + callee histogram + snapshot digest).
- Substrate readings are from `/fast/scratch/kotoba-r47/shared/omp-18.12.5.strings`; I verified that file is byte-identical to `strings -n 4 bin/omp-18.12.5` (sha256 `33df0aeffc4565967bc1a3b42621f8eade0e6e4c2ae8733319fcd484902fb301`, matching `SHA256SUMS`), i.e. exactly what `verify_surfaces.py::dump_via_strings` (verifiers/verify_surfaces.py:209-227) would derive.

# Evidence — the class still exists (18.12.5)

Module header and group constant:
- `898677:// packages/coding-agent/src/discovery/cursor.ts`
- `898678:var _l = "cursor";` (group/provider id used by all three cursor loaders; `uk = "Cursor"`, `pk = 50` at 898679-898680)

Rules loader itself (`async function Fte(u)` at 898723):
- `898726:  const T = Xl(u, "cursor", "rules");` — user-level candidate path
- `898727:  const M = Fo(u, "cursor", "rules");` — project-level candidate path
- `898730:      extensions: ["mdc", "md"],` (user branch) / `898734:` (project branch)
- `898745:function JO(u, p, R, T) {` → `898746:  return Td(u, p, R, T, { stripNamePattern: /\.(mdc|md)$/ });`
- Both branches call the same directory scanner `Nn(u, dir, _l, "user"|"project", {extensions:["mdc","md"], transform: JO})` (calls at 898728-898735).

Registration (this is the "loader row" that keeps the class alive):
- `898788:Le(qs.id, {`
- `898789:  id: _l,`
- `898790:  displayName: uk,`
- `898791:  description: "Load rules from .cursor/rules/*.mdc and legacy .cursorrules",`
- `898792:  priority: pk,`
- `898793:  load: Fte`
- Sibling registrations in the same module: mcp at `898783` (`load: Dte`, paths `898705`/`898708` = `Xl(u,"cursor","mcp.json")` / `Fo(u,"cursor","mcp.json")`), settings at `898794-898799` (`load: Ute`, paths `898750`/`898753` = `Xl/Fo(u,"cursor","settings.json")`).

Name resolution (all same bundle, discovery-helpers region 862xxx):
- `862377:var qs = Jo({` / `862378:  id: "rules",` / `862379:  displayName: "Rules",` / `862380:  description: "Project-specific rules and constraints (Cursor MDC, Windsurf, Cline formats)",` → `qs.id` is the `rules` capability, so `Le(qs.id, …)` registers a rule-text provider.
- `861904:function Le(e, t) {` — capability registry insert; unknown capability throws `Unknown capability: "${e}". Define it first with defineCapability().` and providers are priority-sorted (861904-861920).
- `862506:function Xl(e, t, n) {` → `862507:  if (!Ii(t, e))` / `862508:    return null;` / `862509:  return nLe(e, t, n);` → **user-level path, gated by provider-enabled**; there is no direct `Ii("cursor"` call site because the gate is inside `Xl`.
- `862510:function Fo(e, t, n) {` → `join(e.cwd, fO[t].projectDir, n)` (862510-862514) → **project-level path, never gated**.
- `862443:var fO = {`; cursor row `862496-862499`: `cursor: { userBase: ".cursor", userAgent: ".cursor", projectDir: ".cursor" }`.
- `862059:function Ii(e, t) {` — `disabledProviders` excludes; otherwise opt-in via `enabledProviders` accepting the group, `*`, or `all` (plus the two claude special cases), 862059-862074.
- `862757:async function Nn(e, t, n, r, s) {` — glob `*.{mdc,md}` from `extensions`, `gitignore:true`, `hidden:false`, `recursive` defaults `false` and `Fte` does not override it → **top-level files only, gitignored and dot-hidden files skipped** (observed from the function body, 862757-862775).
- `862579:function Td(e, t, n, r, s) {` — frontmatter parse; `enabled === false` drops the rule (862581-862584).

Second witness (independent table, provider listing): `557975:Cursor` then `557993:Load rules from .cursor/rules/*.mdc and legacy .cursorrules` (same sentence as the registry at 898791; no other cursor rule description exists).

# Call shape around the (group, file) literal

`load_baseline` parses `omp:cursor/rules` into `group="cursor"`, `file="rules"` (verifiers/verify_surfaces.py:284-285). The literal-side call sites are `Xl(u, "cursor", "rules")` (user) and `Fo(u, "cursor", "rules")` (project) — two path-builder calls, not a registration-call dispatch; the registration is the `Le(qs.id,{…load:Fte})` block above. Per the documented contract (`verifiers/verify_surfaces.py:33-35,61-66`), a non-`.md` directory literal is outside the extractor and is hand-declared `loader-literal`; `check_literal_present` (verifiers/verify_surfaces.py:508-536) then requires only that the literal `rules` occur in the omp dump and imposes **no** call-shape requirement for this kind.

# Scoped verifier facts

Run against the pinned dump with the BASE verifier module (scratch clone at `c61a973`, helpers called in isolation, no gate run):
- `load_baseline` family = `['omp:cursor/rules']`, kind `loader-literal`, verdict `governed`.
- `check_literal_present(family, …)` → `(True, '1 loader-kind entry verified against the dumps')`.
- `check_literal_present(['omp:discovery/mcp-configs','omp:discovery/settings'], …)` → `(True, '2 loader-kind entries verified against the dumps')`; their loader rows are 898705/898708 (`mcp.json`) and 898750/898753 (`settings.json`), descriptions 898785/898797.
- `extract_classes(dump, 'omp')` → **0 (group,file) pairs**.
- Live `.md`-shaped calls in 18.12.5 use callees `Xl` (5), `Fo` (4), `lq` (2) only — none of the 11 pinned names `Id|Cl|jD[ef]|Tl|dr|GW|Co|Dl|Hj|I5|Gl|Mo` (verifiers/verify_surfaces.py:155-159). Exact hits: `895129: lq(u, f$, "AGENTS.md")`, `895140: lq(u, m$, "CLAUDE.md")`, `898856: Xl(u, "gemini", "GEMINI.md")`, `898867: Fo(u, "gemini", "GEMINI.md")`, `898992: Fo(u, "gemini", "SYSTEM_TEMPLATE.md")`, `898993: Fo(u, "gemini", "system.md")`, `898994: Xl(u, "gemini", "SYSTEM_TEMPLATE.md")`, `898995: Xl(u, "gemini", "system.md")`, `899090: Xl(u, "opencode", "AGENTS.md")`, `899328: Fo(u, "github", "copilot-instructions.md")`, `900239: Xl(u, "windsurf", "memories/global_rules.md")`.
- Consequence for C1: re-pinning the allowlist with `Xl|Fo` (and identifier-group handling for `lq`) would re-extract the `.md` neighbour rows; it would **not** change `omp:cursor/rules`, whose literal is not `.md` and can never be extracted. `[INFERENCE]` that the current 0-pair extraction trips `check_no_uncovered_class`'s vacuity arm (verifiers/verify_surfaces.py:566-575) because the baseline declares 8 `loader-group` rows for omp; I did not run the gate (see NOT checked).

# Counterexamples / negatives

1. **Docstring witness is stale.** `verifiers/verify_surfaces.py:64` cites `Cl(e,"cursor","rules")` as the explanation of this class. In 18.12.5: `grep -n -F 'Cl(e,"cursor","rules")'` → 0 hits, exit 1; `Cl(u, "cursor", "rules")` → 0 hits, exit 1; `Id(e,"cursor"` → 0 hits, exit 1; `Tl(e,"cursor"` → 0 hits, exit 1. `Cl` is still in `OMP_CALL_RE` and matches a synthetic `Cl(e,"cursor","rules")` (sanity check True), but no such call exists in this dump. The live pair is `Xl`/`Fo` (898726-898727). This is a doc/comment staleness, not a check failure: the kind is `loader-literal`, so no call shape is required.
2. **`.cursorrules` has no code path.** Only two hits in the whole dump — 557993 (listing table) and 898791 (registry description) — both prose; there is no read of a `.cursorrules` path. This confirms the census's own note at row 88 that the description overstates the class.
3. **`CURSOR_AGENT_RULE_DISABLED` (25847) is not loader evidence.** The identical triplet `CURSOR_AGENT_RULE_DISABLED / BUN_AGENT_RULE_DISABLED / CLAUDE_CODE_AGENT_RULE_DISABLED` also appears in the opencode 1.19.3 dump at 28514-28516, adjacent to a table of `ERR_*` codes, and has zero references in the bundled JS (only 3 occurrences, bare tokens). It is shared Bun-runtime string data, not an omp cursor-loader registration. `[INFERENCE]` from co-location + zero code references in both dumps.
4. The family is **not** absent, so there is no zero-hit sweep to report for `omp:cursor`; the only zero-hit results are the stale callee probes in item 1.

# Commands run (exit codes)

```
sha256sum -c SHA256SUMS                                        # 4× OK, exit 0
strings -n 4 bin/omp-18.12.5 | sha256sum                       # 33df0ae…, equals SHA256SUMS entry, exit 0
grep -n 'cursor' verifiers/surfaces-baseline.json              # 62, 186, 194; exit 0
grep -n 'class_id' verifiers/surfaces-baseline.json            # 38 class_id lines, 1 omp:cursor*; exit 0
grep -n -F 'Xl(u, "cursor", "rules")' omp-18.12.5.strings      # 898726; exit 0
grep -n -F 'Fo(u, "cursor", "rules")' omp-18.12.5.strings      # 898727; exit 0
grep -n -F 'var _l = "cursor"' omp-18.12.5.strings             # 898678; exit 0
grep -n -F 'Load rules from .cursor/rules' omp-18.12.5.strings # 557993, 898791; exit 0
grep -n -F '.cursorrules' omp-18.12.5.strings                  # 557993, 898791 only; exit 0
grep -n -F 'Le(qs.id, {' omp-18.12.5.strings                   # 9 registrations; cursor at 898788; exit 0
grep -n -F 'Cl(e,"cursor","rules")' omp-18.12.5.strings        # 0 hits; exit 1
grep -n -F 'Cl(u, "cursor", "rules")' omp-18.12.5.strings      # 0 hits; exit 1
grep -n -F 'Id(e,"cursor"' omp-18.12.5.strings                 # 0 hits; exit 1
grep -n -F 'Tl(e,"cursor"' omp-18.12.5.strings                 # 0 hits; exit 1
grep -n -F 'AGENT_RULE_DISABLED' opencode-1.19.3.strings       # 28514-28516; exit 0
python3 (scratch clone): check_literal_present(family)         # True, exit 0
python3 (scratch clone): extract_classes(dump,'omp')           # 0 pairs, exit 0
```

Scratch clone used only for the read-only helper calls: `/fast/scratch/kotoba-r47/C1ClassCursor/lane` at `c61a973b2e02e1ded169703ddcb06466f4edd8bd`, clean (`git status --porcelain` → 0 lines). No writes to the fleet repo other than this report and `C1ClassCursor.shapes.json`.

# NOT checked

- Did not run `verifiers/verify_surfaces.py` as a gate, in the fleet repo or in the clone (lane rule: only item-named read-only verifiers; none named here). The 0-pair and per-row results come from calling `load_baseline` / `check_literal_present` / `extract_classes` in isolation against the snapshot dump; the full-gate consequence in the C1 section is marked `[INFERENCE]`.
- Did not execute the omp binary or any runtime probe; a compiled-in loader shape does not prove the loader fires (the verifier's own documented limit, verifiers/verify_surfaces.py:40-42). No `omp --version` run (unnecessary: snapshot digest verified).
- Did not audit other families' loader rows; `omp:discovery/mcp-configs` and `omp:discovery/settings` were checked only as cursor-adjacent reasons, not as their own witnesses.
- Did not resolve the `lq(u, f$, "AGENTS.md")` / `lq(u, m$, "CLAUDE.md")` identifier groups (`f$`, `m$`) through `constant_table`; irrelevant to the cursor family, relevant to whoever re-pins those two shapes.
- Did not check the opencode 1.19.3 dump for cursor-family equivalents beyond the `AGENT_RULE_DISABLED` cross-check.
- No tool installs or upgrades were performed (nothing installed, no pacman transaction attempted).
