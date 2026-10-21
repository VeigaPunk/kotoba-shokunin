verdict: both claude-family classes still exist in omp 18.12.5 — `omp:claude-md/CLAUDE.md` (loader-group) registers `lq(u, m$, "CLAUDE.md")` with `m$ = "claude-md"` (dump 895136-895146) and `omp:claude-dir/CLAUDE.md` (loader-literal) loads `CLAUDE.md` from the Claude config dir and `<cwd>/.claude` (dump 896894-896912); the class survived, the *witness callee* was re-minified (`jDe`→`lq`), and the BASE extractor's allowlist still names the legacy `Id|Cl|jD[ef]|…` callees but not `lq`, so it extracts 0/8 omp pairs and cannot witness the loader-group pair.

# C1 per-class witness — omp `claude-md` family (BASE c61a973b2e02e1ded169703ddcb06466f4edd8bd)

## Scope: exactly two baseline entries

- `verifiers/surfaces-baseline.json:13` — `omp:claude-md/CLAUDE.md`, literal `CLAUDE.md`, `context_kind: loader-group`, `verdict: governed`.
- `verifiers/surfaces-baseline.json:125` — `omp:claude-dir/CLAUDE.md`, literal `CLAUDE.md`, `context_kind: loader-literal`, `verdict: governed`.
- No other `class_id` in the baseline contains `claude`; the remaining `claude` hits in that file (lines 3, 186, 194, 202, 226) are the `$comment` and exclusion `reason` prose, not class rows (`grep -n "claude" verifiers/surfaces-baseline.json`, exit 0).
- Census rows: `corpus/knowledge/instruction-surface-census-round13.md:74` (claude-md) and `:97` (claude-dir). Both rows' literal cell (`CLAUDE.md`) and kind cell (`loader-group` / `loader-literal`) still match the baseline, so `surfaces.literal_parity`/`kind_parity` are not the failure; only the extraction rule is stale.

## Substrate provenance

Both dumps verified against `/fast/scratch/kotoba-r47/shared/SHA256SUMS`:

```
33df0aeffc4565967bc1a3b42621f8eade0e6e4c2ae8733319fcd484902fb301  omp-18.12.5.strings
fdbc8136084c9a10439569157b2af62312e2b0d801cab54c73e89476da798e7e  bin/omp-18.12.5
```

`sha256sum` output matched both lines (exit 0); the strings dump has 2,443,339 lines. Snapshot is read-only, omp 18.12.5.

## 1. `omp:claude-md/CLAUDE.md` — PRESENT, `loader-group` correct

Exact dump lines (`awk 'NR>=895136 && NR<=895146'`, byte-for-byte):

```
895136:// packages/coding-agent/src/discovery/claude-md.ts
895137:var m$ = "claude-md";
895138:var U7 = "CLAUDE.md";
895139:async function kBt(u) {
895140:  return lq(u, m$, "CLAUDE.md");
895141:Le(Al.id, {
895142:  id: m$,
895143:  displayName: U7,
895144:  description: "Standalone CLAUDE.md files (Claude Code style)",
895145:  priority: 10,
895146:  load: kBt
```

**Call shape around the (group, file) literal.** The registration is a three-argument standalone-file load, `lq(u, m$, "CLAUDE.md")`, where:

- `lq` is the generic walk-up loader, defined exactly once in the dump: `async function lq(e, t, n)` at `omp-18.12.5.strings:862812`. Its body resolves `home`, `cwd` and `repoRoot`, walks upward joining `n` (the file name), and skips hidden directories (`if (!D.startswith("."))` guard in the loop, dump 862816-862850). The group arg `t` is carried as provenance, not used to pick a directory. This is why claude-md and agents-md share the same callee (agents-md: `return lq(u, f$, "AGENTS.md")` at dump 895129 with `var f$ = "agents-md"` at 895126).
- The group argument is the identifier `m$`; `constant_table()` resolves it to `claude-md`. The binding is unique: `\bm\$\s*=\s*"..."` occurs once in the whole dump (895137), so there is no conflicting-rebind drop.
- The file argument is the quoted literal `"CLAUDE.md"`; the call closes with `)` immediately after, satisfying the extractor's `(?=\s*[,)])` lookahead.

**Registration.** `Le(Al.id, {...})` at 895141-895146 enters the provider into the same registry object `Al` used by agents-md (895130-895135), gemini (898856-900239 region) and the other discovery providers: `id: m$` = `claude-md`, `displayName: U7` = `CLAUDE.md`, description `Standalone CLAUDE.md files (Claude Code style)`, `priority: 10`, `load: kBt`. The object's closing `});` is not visible in the dump — `strings -n 4` drops 3-character printable runs; `grep -c '^});$'` → 0 while `grep -c '^  });$'` → 1837, so read registrations as fields, not braces. [INFERENCE on the cause, supported by those two counts.]

**Module wiring (not dead code).** The provider module is lazily imported and registered in the discovery index:

- import specifier: `@oh-my-pi/pi-coding-agent/discovery/claude-md` at dump 595867;
- lazy loader: `var Ta = () => import("/$bunfs/root/chunks/claude-md-8hbgb5ec.js");` at dump 1262035;
- index entry: `"@oh-my-pi/pi-coding-agent/discovery/claude-md": Ta,` at dump 1264038;
- chunk path also listed at dump 513545 and 2440687-2440688;
- human-readable provider catalog: `claude-md` at dump 557675 immediately followed by `Standalone CLAUDE.md files (Claude Code style)` at 557676.

## 2. `omp:claude-dir/CLAUDE.md` — PRESENT, `loader-literal` correct

Registration (`awk 'NR>=897191 && NR<=897196'`):

```
897191:Le(Al.id, {
897192:  id: mi,
897193:  displayName: Qa,
897194:  description: "Load CLAUDE.md files from .claude/ directories",
897195:  priority: Za,
897196:  load: Tee
```

Provider constants for this chunk: `var mi = "claude";` (896820), `var Qa = "Claude Code";` (896821), `var Za = 80;` (896822), `var gm = ".claude";` (896823).

Loader `async function Tee(u)` at 896894 reads two concrete `join(dir, "CLAUDE.md")` sites — no `(group, "<file>.md")` call, which is why `loader-literal` is the right kind:

```
896897:  const T = el(u);
896898:  const M = T ? Ir.join(T, "CLAUDE.md") : null;
...
896907:  const B = ym(u);
896908:  const H = Ir.join(B, "CLAUDE.md");
```

- `el(u, p = false)` (896829) returns `up(u.home).configDir` only when `Ii("claude", u)` passes; `up()` is the Claude-paths resolver (`packages/coding-agent/src/config/claude-paths.ts`, 792502-792508): `CLAUDE_CONFIG_DIR` if set, else `~/.claude`. So the user-level file is `${CLAUDE_CONFIG_DIR:-~/.claude}/CLAUDE.md`.
- `ym(u)` (896832) is `Ir.join(u.cwd, gm)`, i.e. `<cwd>/.claude/CLAUDE.md` at project level. (The name `ym` is re-used by an unrelated chunk at 699180; the local definition is 896832.)

## Verifier interaction at BASE (observed; no gate run)

I imported the module's pure functions from a scratch clone at BASE (`/fast/scratch/kotoba-r47/C1ClassClaudeMd-9/lane`, HEAD `c61a973…`) and fed them the snapshot dump — no `verify_surfaces.py` invocation.

- `extract_classes(dump, 'omp')` → **0 pairs**, reproducing the before-value `no_uncovered_class vacuity 0/8` (`.ufo/waves/round-47/before/SUMMARY.md:4`). Cause: `OMP_CALL_RE` (`verifiers/verify_surfaces.py:155-158`) allowlists `Id|Cl|jD[ef]|Tl|dr|GW|Co|Dl|Hj|I5|Gl|Mo`, and 18.12.5 registers the .md loaders as `lq` (claude-md, agents-md), `Xl` (gemini ×3, opencode, windsurf) and `Fo` (gemini ×3, github).
- `check_literal_present` on just the two claude entries, empty extraction:
  `False | 1 loader literal(s) not verifiable: omp:claude-md/CLAUDE.md (no (Id|Cl|jD[ef]|…|Mo)(<v>, <group>, "<file>.md") call shape for (claude-md, CLAUDE.md) in omp dump)`.
  `omp:claude-dir/CLAUDE.md` passes the literal probe (the only failure is the loader-group pair). With the pair `("claude-md","CLAUDE.md")` supplied, the same call returns `True | 2 loader-kind entries verified against the dumps`.
- Direct regex proof on dump line 895140: an `lq`-admitting pattern captures `(None, 'm$', 'CLAUDE.md')`; the current `OMP_CALL_RE` returns `None` on that line.
- Candidate allowlist check: adding `lq|Xl|Fo` to the existing allowlist yields exactly the 8 declared `loader-group` pairs — no extra, none missing (`agents-md/AGENTS.md`, `claude-md/CLAUDE.md`, `opencode/AGENTS.md`, `gemini/{GEMINI.md,system.md,SYSTEM_TEMPLATE.md}`, `github/copilot-instructions.md`, `windsurf/memories/global_rules.md`). [For claude-md alone, admitting `lq` is sufficient; the full-set result is supporting evidence, not a patch.]

## Counterexamples and hazards

1. **Census evidence is stale, machine checks cannot see it.** `corpus/knowledge/instruction-surface-census-round13.md:74` cites `jDe(e,BWr,"CLAUDE.md")`, `BWr = "claude-md"`. In 18.12.5: `grep -c 'var BWr\|BWr ='` → 0, `grep -c 'var Pqr\|Pqr ='` → 0 (agents-md's old group var), `grep -c 'jDe([^)]*\.md'` → 0. The naive `grep 'BWr'` returns 4 hits but every one is blob/substring noise (gzip/base64 lines 561580, 1847066, 2422056; doc array 962049) and `\bPqr\b` hits only base64 at 92210. `jDe` does exist at 818391 but as an unrelated `function jDe(e, t, g, B = $9)` (4-arg, also exported as `encodeTspMessage`). So a literal-present check plus the census row both stay green while the row's *witness text* names a callee that no longer performs the registration — a human re-derive must rewrite the evidence cell, and the C1 report should say the class was re-witnessed, not copied.
2. **`lq` has a non-literal sibling call that must stay out.** `const Y = await lq(u, rb, X);` at dump 895850 (`var rb = "custom-context"` at 895819; `X` iterates runtime-configured names from `lZ()` at 895821). Because the filename is a variable, the shape regex does not and should not match it; the baseline declares no `custom-context` class (`grep -n "custom-context" verifiers/surfaces-baseline.json` → no hits, exit 1). Admitting `lq` therefore does not manufacture a new pair from this site.
3. **`Xl`/`Fo` are chunk-shadowed minifier names.** The three-argument discovery helpers are defined at 862506 (`function Xl(e, t, n)`, user-level `nLe(...)`) and 862510 (`function Fo(e, t, n)`, project-level `join(cwd, fO[t].projectDir, n)`), but the same names are defined 2- and 3-arg elsewhere (e.g. `Xl` at 739666, 1147554; `Fo` at 666858, 671511, 741212, 757626, 814808, 1305552). A name-only allowlist on them is safe only because the shape regex pins three args with a quoted group and an `.md` literal; `lq` (one definition, 862812) is the least ambiguous of the three.
4. **`strings -n 4` erases top-level closers** (`^});$` → 0 lines vs `^  });$` → 1837), so the registration object at 895141-895146 appears headless. Do not infer a missing registration from the absent `});`.
5. **`Al`/`Le` identity unresolved.** `Le(Al.id, …)` is reused by every discovery provider in the same chunk (agents-md 895130, claude-dir 897191, gemini 898856 region), which is sufficient to show the registration path, but I did not resolve `Al`'s or `Le`'s defining module.

## Commands run (exit codes and key output)

| command (cwd) | exit | key output |
|---|---|---|
| `git rev-parse HEAD` + `git status --porcelain` (lane) | 0 | `c61a973b…`; only untracked `.ufo/waves/`, `plans/round-47.md` |
| `grep -n "claude-md" verifiers/surfaces-baseline.json` (lane) | 0 | line 13 only |
| `grep -n "claude" verifiers/surfaces-baseline.json` (lane) | 0 | rows 13, 125; prose 3, 186, 194, 202, 226 |
| `cat SHA256SUMS; sha256sum omp-18.12.5.strings bin/omp-18.12.5` (snapshot) | 0 | `33df0ae…` / `fdbc8136…` match |
| `grep -n "CLAUDE.md" omp-18.12.5.strings` | 0 | 16 hits; 895136-895146 is the registration block |
| `grep -n "claude-md" omp-18.12.5.strings` | 0 | 9 hits; `"claude-md"` quoted only at 895137 |
| `grep -n 'lq(' omp-18.12.5.strings` | 0 | definition 862812; calls 895129, 895140, 895850 |
| `grep -c 'var BWr\|BWr ='` / `Pqr` / `jDe(...md` | 1 (no match) | 0 / 0 / 0 |
| `grep -c '^});$'` / `'^  });$'` | 0 / 0 | 0 / 1837 |
| python3 `v.extract_classes(dump,'omp')` (scratch clone at BASE) | 0 | 0 pairs; `m$`→`claude-md`, `U7`→`CLAUDE.md` |
| python3 `v.check_literal_present([claude rows], …)` | 0 | `False` (empty) / `True` (pair supplied), detail quoted above |
| python3 candidate allowlist `lq\|Xl\|Fo` vs declared pairs | 0 | 8 extracted = 8 declared, 0 extra, 0 missing |
| python3 `v.inventory_rows(census)` | 0 | rows 74 and 97 parsed; literal+kind cells match baseline |

No tools were installed or upgraded. Nothing was written outside this report.

## What I did NOT check

- Did **not** run `verifiers/verify_surfaces.py` or `check_substrate_pins.py` (item names no verifier; contract forbids lane-wide gates). All verifier behaviour above is from importing its pure functions in a scratch clone — not a gate pass/fail.
- Did not inspect opencode 1.19.3 or its Claude paths; this ticket is the omp family only.
- Did not verify the loader fires at runtime (static strings evidence only; a compiled-in call proves the path exists, per the verifier's own documented limit).
- Did not resolve `Al`/`Le`/`Ii` module identities, nor read `nLe` (the user-dir join behind `Xl`).
- Did not re-derive or propose a patch for `OMP_CALL_RE`; the allowlist result is evidence for C1's owner, not an edited production file.
- Did not re-check mtime or the live host binary; only the frozen snapshot hashes.
- Did not audit census rows other than 74 and 97.

## Confidence

High for existence, registration, literal, group resolution and the call shape of both claude rows (direct byte-level dump lines + unique bindings). High for the verifier failure cause on `omp:claude-md/CLAUDE.md` (reproduced against the same module code at BASE). Medium for the full 8-pair allowlist recommendation, since `Xl`/`Fo` names collide across chunks (shape regex is what keeps it sound). Unresolved: `Al`/`Le` identity and whether any runtime path bypasses `lq` for CLAUDE.md.
