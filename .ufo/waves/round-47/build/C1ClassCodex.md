verdict: both `omp:codex` baseline rows still exist in omp 18.12.5 as live capability registrations (`codex.ts`, dump 897978–898676); `loader-literal` remains the correct kind for both, but the C1 verifier's omp callee allowlist is stale on this substrate — 0 call shapes extract, so `surfaces.literal_present` and `surfaces.no_uncovered_class` both FAIL on the frozen dump. Exact re-pin candidate set is `lq|Xl|Fo`, which simulates to 8/8 baseline loader-group pairs, 0 extra, both checks PASS.

# C1 per-class witness — omp loader family `codex`

BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (verified `git rev-parse HEAD`, exit 0).
Substrate snapshot `/fast/scratch/kotoba-r47/shared/` — `sha256sum -c SHA256SUMS` exit 0, all 4 artifacts `OK` (both binaries + both dumps); `~/.local/bin/omp --version` → `omp/18.12.5` exit 0. All dump line numbers below are lines of `omp-18.12.5.strings`, which is `strings -n 4` output: lines shorter than 4 bytes (e.g. lone `}`) do not exist in the dump, so brace-only closes are absent, not missing code.

## 1. Baseline rows in scope (exhaustive)

`jq -r '.classes[] | select(.class_id|startswith("omp:codex"))'` on `verifiers/surfaces-baseline.json` returns exactly two of 38 entries (`"class_id": "omp:codex` grep → lines 132, 167; only 2 hits):

| class_id | literal | kind | verdict | baseline lines | census row |
|---|---|---|---|---|---|
| `omp:codex/AGENTS.md` | `AGENTS.md` | `loader-literal` | governed | `verifiers/surfaces-baseline.json:132-136` | `corpus/knowledge/instruction-surface-census-round13.md:98` |
| `omp:codex/prompts` | `prompts` | `loader-literal` | governed | `verifiers/surfaces-baseline.json:167-171` | `corpus/knowledge/instruction-surface-census-round13.md:103` |

No other baseline id starts `omp:codex`. Family-adjacent codex surfaces are carried by excluded generic rows: `omp:discovery/mcp-configs` (:181), `omp:discovery/settings` (:189), `omp:discovery/extensions` (:197, reason text names `.codex/tools`), `omp:discovery/commands` (:213), `omp:discovery/skills-roots` (:221, reason text names `~/.codex/skills`).

## 2. Per-class witness

### 2.1 `omp:codex/AGENTS.md` — PRESENT, `loader-literal` correct

Module boundary: `// packages/coding-agent/src/discovery/codex.ts` at dump 897978 and 898295; the module runs to the `cursor.ts` marker at 898677. Group constants at **898296-898298**: `var ti = "codex"; var la = "OpenAI Codex"; var da = 70;`.

Registration call (**898600-898605**) — a real registration, not a literal hit:

```
Le(Al.id, {
  id: ti,
  displayName: la,
  description: "Load context files from ~/.codex/AGENTS.md (user-level only)",
  priority: da,
  load: Pte
```

Call shape around the literal: the `(group, file)` pair is **not** a 3-arg registration call. `Le` is `registerProvider(capabilityId, def)` — definition at **861904-861921**: looks up `I.get(e)`, throws on unknown capability, records display name/description, then inserts the provider into `n.providers` sorted by `priority`. `Al` is the capability `context-files` (**892076-892077** `var Al = Jo({ id: "context-files", ...`) whose `Jo` factory is at 861898-861903.

Literal site is inside the loader `Pte` (**898310-898325**):

```
898313  const T = ua(u);
898316  const M = Yr.join(T, "AGENTS.md");
898317  const I = await Ue(M);
898322      level: "user",
```

and `ua` (**898301-898304**) gates the user path:

```
898301 function ua(u, p = false) {
898302   if (!p && !Ii("codex", u))
898303     return null;
898304   return Yr.join(u.home, fO.codex.userBase);
```

with `fO.codex = { userBase: ".codex", userAgent: ".codex", projectDir: ".codex" }` at **862459-862461**. `Ii` is the provider gate (**862059-862073**: disabled set, `ge[n] !== true` pass-through, explicit providers, enabled set with `*`/`all`, `CLAUDE_CONFIG_DIR` special-case); `ge.codex: true` at **861882** so codex user paths require opt-in exactly as the census's provider-gate row claims.

User-level-only confirmed by sweep: `grep -nE '(Xl|Fo|lq)\(u, "codex"' omp-18.12.5.strings` → 0 hits, and the only other `AGENTS.md` codex mention is the description/UI text (557981, 898603). The separate AGENTS.md path at 896692-896704 belongs to the omp-native discovery module (`discovery/builtin.ts`, 895896-896721), not codex. Second, independent witness: the human-readable discovery list at **557980-557981** (`OpenAI Codex<` / `Load context files from ~/.codex/AGENTS.md (user-level only):`).

Conclusion: class exists; registration and literal both live; `loader-literal` is the right kind (there is no `(group, "<file>.md")` call — only `join(user-dir, "AGENTS.md")`).

### 2.2 `omp:codex/prompts` — PRESENT, `loader-literal` correct

Registration call (**898630-898635**):

```
Le(fR.id, {
  id: ti,
  displayName: la,
  description: "Load prompts from ~/.codex/prompts and .codex/prompts/",
  priority: da,
  load: Ite
```

`fR` is the capability `prompts` (**892184-892185** `var fR = Jo({ id: "prompts", ...`).

Loader `Ite` (**898484-898512**) resolves both levels and reads `.md` files under the group `ti`:

```
898485  const p = ua(u);
898486  const R = p ? Yr.join(p, "prompts") : null;
898487  const T = nl(u);
898488  const M = Yr.join(T, "prompts");
898501    R ? Nn(u, R, ti, "user", {
898502      extensions: ["md"],
898505    Nn(u, M, ti, "project", {
```

with `nl(u) = Yr.join(u.cwd, ".codex")` (**898299-898300**). Project prompts are ungated (`Nn(... "project")` has no `Ii` call), user prompts are gated through `ua`; consistent with the provider-gate row's "project-level paths are never gated".

Conclusion: class exists; literal is a directory name consumed by a directory reader with `extensions: ["md"]`, so no `.md`-suffixed registration shape exists — `loader-literal` is the right kind.

## 3. Family extent in 18.12.5 (freshness)

Ten `Le(...)` registrations inside `discovery/codex.ts` (897978-898676), all with `id: ti`, `displayName: la`, `priority: da` (70):

| dump lines | capability constant | description | baseline treatment |
|---|---|---|---|
| 898600-898605 | `Al` context-files | `~/.codex/AGENTS.md` (user-level only) | governed `omp:codex/AGENTS.md` |
| 898606-898611 | `fa` mcps | `config.toml [mcp_servers.*]` | `omp:discovery/mcp-configs` excluded |
| 898612-898617 | `Tl` skills | `~/.codex/skills` + `.codex/skills/` | `omp:discovery/skills-roots` excluded |
| 898618-898623 | `dw` extension-modules | `~/.codex/extensions` + `.codex/extensions/` | `omp:discovery/extensions` excluded |
| 898624-898629 | `gd` slash-commands | `~/.codex/commands` + `.codex/commands/` | `omp:discovery/commands` excluded |
| 898630-898635 | `fR` prompts | `~/.codex/prompts` + `.codex/prompts/` | governed `omp:codex/prompts` |
| 898636-898641 | `hh` hooks | `~/.codex/hooks` + `.codex/hooks/` | only inside `discovery/extensions` reason text |
| 898642-898647 | `uw` hooks→custom tools | `~/.codex/tools` + `.codex/tools/` | only inside `discovery/extensions` reason text |
| 898648-898653 | `vy` settings | `config.toml` | `omp:discovery/settings` (literal `settings.json`) |
| 898671-898676 | SYSTEM loader `Nte` (898654-898670) | `SYSTEM.md`/`SYSTEM_TEMPLATE.md` from `.codex` cwd+home | `omp:agent-system-prompt/SYSTEM.md` (one id for the family) |

Everything the census claims about codex is still true on 18.12.5; nothing was removed or renamed. Two calibration gaps, stated as observations not as a required round-47 change: (a) codex settings and MCP both resolve to `config.toml`, while the excluded `omp:discovery/settings` literal is `settings.json` — the codex spelling is not itself witnessed by any baseline literal; (b) `~/.codex/hooks` and `~/.codex/tools` are covered only by prose inside `omp:discovery/extensions`'s reason, whose literal is `extensions`.

## 4. Counterexamples / discriminating power

### 4.1 The two codex rows' verifier check is non-discriminating

`check_literal_present` treats `loader-literal` as "literal occurs in the dump" (`verifiers/verify_surfaces.py:60-64, 508-533`). Literal counts in the dump: `AGENTS.md` 37, `prompts` 491. Counterfactual run: removing both codex description strings from an in-memory copy of the dump and running `check_literal_present` on the two codex entries still returns `True | 2 loader-kind entries verified against the dumps` (scrubbed dump retained `AGENTS.md` 35, `prompts` 485). So these rows cannot detect removal of the codex registration; existence rests on the manual witnesses in §2, which is exactly what this seat supplies.

### 4.2 C1 verifier is currently red on the frozen 18.12.5 dump (callee allowlist stale)

Read-only run:

```
python3 verifiers/verify_surfaces.py \
  --omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings \
  --opencode-strings /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings \
  --check surfaces.literal_present --check surfaces.no_uncovered_class
```

exit **1**:

- `FAIL surfaces.literal_present`: 8 loader literals unverifiable — every omp `loader-group` row (`agents-md/AGENTS.md`, `claude-md/CLAUDE.md`, `opencode/AGENTS.md`, `gemini/GEMINI.md`, `gemini/system.md`, `gemini/SYSTEM_TEMPLATE.md`, `github/copilot-instructions.md`, `windsurf/memories/global_rules.md`) has "no call shape".
- `FAIL surfaces.no_uncovered_class`: "vacuity: 0 loader class(es) extracted from the omp dump while the baseline declares 8 loader-group class(es)"; plus the "extractor blind" arm listing declared literals (the codex rows appear in that list as collateral — the arm enumerates every declared literal present when extraction is zero, and is skipped once pairs extract; it is not a codex-specific defect).

Cause: `OMP_CALL_RE` at `verifiers/verify_surfaces.py:155-159` allows callees `Id|Cl|jD[ef]|Tl|dr|GW|Co|Dl|Hj|I5|Gl|Mo` (last pinned 18.12.2 `I5/Gl/Mo`, comment at :142-143). 18.12.5's actual `(group, "<file>.md")` helpers are:

- `lq(e,t,n)` at **862812** (walk-up reader; `lq(u, f$, "AGENTS.md")` 895129, `lq(u, m$, "CLAUDE.md")` 895140; `f$ = "agents-md"` 895126, `m$ = "claude-md"` 895137)
- `Xl(e,t,n)` at **862506** (gated user path via `nLe`/`Ii`)
- `Fo(e,t,n)` at **862510** (ungated project path, `fO[t].projectDir`)

Observed shape sites: `Xl(u,"opencode","AGENTS.md")` 899090; `Xl(u,"gemini","GEMINI.md")` 898856; `Fo(u,"gemini","system.md")` 898993; `Xl/Fo(u,"gemini","SYSTEM_TEMPLATE.md")` 898992/898994; `Fo(u,"github","copilot-instructions.md")` 899328; `Xl(u,"windsurf","memories/global_rules.md")` 900239.

Advisory re-pin simulation (in-process monkeypatch only; no production file touched): adding `lq|Xl|Fo` to `OMP_CALL_RE` yields exactly the 8 baseline pairs, **missing: []**, **extra: []**, and both checks pass — `literal_present ALL: True (38 loader-kind entries verified)`, `no_uncovered ALL: True (all 8 extracted loader classes declared)`. Machine-readable record: `.ufo/waves/round-47/build/C1ClassCodex.repin-sim.json`. Caveat: `lq(u, rb, X)` at 895850 is not extracted (third arg is an identifier, not a quoted `*.md`) and `rb` has conflicting bindings (`8192` at 688715, `"custom-context"` at 895819) so the constant table drops it — no codex impact.

## 5. Commands run (all read-only against lane + frozen snapshot)

| command | exit | key output |
|---|---|---|
| `git rev-parse HEAD` | 0 | `c61a973b2e02e1ded169703ddcb06466f4edd8bd` |
| `sha256sum -c SHA256SUMS` (snapshot dir) | 0 | 4× `OK` |
| `wc -l omp-18.12.5.strings` | 0 | 2,443,339 lines |
| `~/.local/bin/omp --version` | 0 | `omp/18.12.5` |
| `jq -r '.classes[] \| select(.class_id\|startswith("omp:codex"))'` | 0 | 2 rows |
| `grep -n 'description: "Load …' omp-18.12.5.strings` | 0 | codex rows at 898603/898615/898621/898627/898633/898639/898645/898651/898674 |
| `grep -n -F '.codex' omp-18.12.5.strings` | 0 | 61 hits (registry 898…, provider table 862459-862461, history path 802613, session store 542602) |
| `python3 verifiers/verify_surfaces.py --omp-strings … --opencode-strings … --check surfaces.literal_present --check surfaces.no_uncovered_class` | **1** | both checks FAIL (see §4.2) |
| in-process re-pin simulation (`C1ClassCodex.repin-sim.json`) | 0 | 8/8 pairs, 0 missing, 0 extra, both checks PASS |
| in-process counterfactual scrub of codex strings | 0 | codex rows still PASS literal presence |

No tools installed or upgraded. No production files modified.

## 6. What I did NOT check

- Did not run `verify_skill_checklist.py`, `check_substrate_pins.py`, the full `verify_surfaces.py` check set, or `--self-test` — outside this seat.
- Did not execute the codex loaders at runtime (no omp session launch; contract forbids) — "exists in the binary" is proven, "fires in a real session" is not.
- Did not inspect the binary directly beyond the hash-verified `strings -n 4` dump; no disassembly, so `Pte`/`Ite`/`Le` bodies are read from the embedded/minified JS text, and dump-local line numbers are not file offsets.
- Did not resolve the identity of `Nn` (directory reader used by `Ite`) — minified name is reused in at least three other chunks, and its own definition is not needed to establish the codex literal site.
- Did not check whether the census's `omp:codex/AGENTS.md` "user-level only" note is also true on Windows/platform variants; only the Linux x64 snapshot was examined.
- Did not verify the excluded rows' reasons against codex beyond naming them; assessing census exclusion adequacy is not this seat's question.
