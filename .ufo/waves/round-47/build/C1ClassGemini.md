verdict: the `omp:gemini/*` family still exists in omp 18.12.5 — all three baseline rows have live registration records and exact `(v, "gemini", "<file>")` call shapes (`Xl`/`Fo`, dump lines 898856/898867 and 898992–898995) — but `verify_surfaces.py` extracts **0** shapes from the 18.12.5 dump because its pinned callee allowlist predates this generation; adding the measured `lq|Xl|Fo` generation to the allowlist restores exact 8/8 loader-group parity, so **no gemini row needs re-verdicting or dropping**.

# C1 per-class witness — `omp:gemini` family vs omp 18.12.5

BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (confirmed: `git rev-parse HEAD` exit 0). Production files read-only; no lane file touched except this report and its JSON artifact.

## 1. Baseline rows under test (BASE)

`verifiers/surfaces-baseline.json`:

| class_id | entry lines | literal | kind | verdict |
|---|---|---|---|---|
| `omp:gemini/GEMINI.md` | 26–32 (`class_id` :27) | `GEMINI.md` | loader-group | governed |
| `omp:gemini/system.md` | 33–39 (`:34`) | `system.md` | loader-group | governed |
| `omp:gemini/SYSTEM_TEMPLATE.md` | 40–46 (`:41`) | `SYSTEM_TEMPLATE.md` | loader-group | governed |

That is the whole `omp:gemini` prefix set (verified by loading the JSON: `[e['class_id'] for e in classes if startswith('omp:gemini')]` → exactly the 3). Baseline has 38 classes, of which **8** are `loader-group` — the family is 3 of those 8.

Family-adjacent loader rows (different class prefix, but their loader evidence is the gemini module) — both **excluded**, so no re-verdict is at stake:
- `omp:discovery/settings` (:188–195, reason :194 "Settings discovery (cursor/gemini/…)") — evidence `Xl/Fo(u, "gemini", "settings.json")` at 898937/898953 (loader `Gte`, :898934) and 898808/898814 (MCP settings reader).
- `omp:discovery/extensions` (:196–203, reason :202) — evidence 898885/898891 (`Hte`, :898882), 898926/898927 (`Wte`), manifest `gemini-extension.json` at 898903 (`YO`, :898898).

## 2. Substrate identity

`sha256sum -c SHA256SUMS` in `/fast/scratch/kotoba-r47/shared` → exit 0, all four OK: `bin/omp-18.12.5` (`fdbc8136…`), `bin/opencode-1.19.3` (`179ca421…`), `omp-18.12.5.strings` (`33df0aef…`), `opencode-1.19.3.strings` (`f4d8f34a…`). This matches the round-47 before-summary. Dump line numbers below are **`strings -n 4` dump-relative**, not binary offsets.

The default resolution uses the same bytes: `sha256sum /home/vgpnk/.local/bin/omp` → `fdbc8136…`, `omp --version` → `omp/18.12.5`, and `strings -n 4 /home/vgpnk/.local/bin/omp | sha256sum` → `33df0aef…` (exit 0), i.e. the snapshot dump is byte-identical to what `verify_surfaces.py` generates at default resolution on this host. The line numbers quoted here therefore apply unchanged to the default run.

## 3. Per-class witness (dump `omp-18.12.5.strings`)

The gemini discovery module is intact and contiguous. Provenance comment `// packages/coding-agent/src/discovery/gemini.ts` at :898800; provider id `var mo = "gemini"` at :898802. The registration callee is the capability registry `Le`: `GEMINI.md` binds `Al` = capability `context-files` (`var Al = Jo({ id: "context-files", … })` :892076–892079, "Persistent instruction files (CLAUDE.md, AGENTS.md, etc.)"), while `system.md`/`SYSTEM_TEMPLATE.md` bind `xy` = `system-prompt` (:892242–892245). So the three rows are live registrations in the same prompt-bearing capability objects the other families use, not orphaned literals.

### 3.1 `omp:gemini/GEMINI.md` — exists, governed stands
- Loader `Bte` at :898853. Registration record :898976–898981:
  `Le(Al.id, { id: mo, displayName: Mu, description: "Load GEMINI.md context files", priority: Eu, load: Bte })` (description :898979; the same string also appears as a standalone literal at :557997).
- Call shapes (wrapped in the loader, no further indirection):
  - :898856 `const T = Xl(u, "gemini", "GEMINI.md");` → user level (`level: "user"`, `_source: Ze(mo, …)`).
  - :898867 `const M = Fo(u, "gemini", "GEMINI.md");` → project level, with depth at :898871 `const B = Fo(u, "gemini", "");` (empty filename, not a class).
- Both are exactly the `(v, group, "<file>.md")` shape the verifier models.

### 3.2 `omp:gemini/system.md` and `omp:gemini/SYSTEM_TEMPLATE.md` — exist, governed stands
- One loader `zte` at :898982; registration :898997–899002:
  `Le(xy.id, { id: mo, …, description: "Load system.md custom system prompt files", …, load: zte })` (description :899000).
- Calls (a local `R(path, level, kind)` wrapper, :898984–898991):
  - :898992 `await R(Fo(u, "gemini", "SYSTEM_TEMPLATE.md"), "project", "template");`
  - :898993 `await R(Fo(u, "gemini", "system.md"), "project", "text");`
  - :898994 `await R(Xl(u, "gemini", "SYSTEM_TEMPLATE.md"), "user", "template");`
  - :898995 `await R(Xl(u, "gemini", "system.md"), "user", "text");`
- `system.md` appears in the dump **only** at these two lines (`grep -F '"system.md"'` → 898993, 898995); `"gemini", "GEMINI.md"` only at 898856/898867; `"gemini", "SYSTEM_TEMPLATE.md"` only at 898992/898994. No competing gemini call site.

### 3.3 Why the shape is the gemini family (call-shape semantics)
- Provider dir table `var fO = {` at :862443; `gemini: { userBase: ".gemini", userAgent: ".gemini", projectDir: ".gemini" }` at :862463–862466.
- `function Fo(e, t, n)` at :862510: `r = fO[t]; if (!r.projectDir) return null; return join(e.cwd, r.projectDir, n)` → `<cwd>/.gemini/<file>`.
- `function Xl(e, t, n)` at :862506: `if (!Ii(t, e)) return null; return nLe(e, t, n)`; `nLe` at :862497 joins `home + fO[t].userAgent + n` → `~/.gemini/<file>`. `Ii` at :862059 is the provider opt-out/enable gate (`F()` disabled set, `ge` default-off table, explicit providers, `X()` enabled set, `CLAUDE_CONFIG_DIR` special case).
- `lq(e, t, n)` at :862812 is the walk-up standalone-file loader used by `agents-md`/`claude-md`, **not** by gemini (do not mistake it for the gemini shape).

## 4. What the verifier currently does (freshness defect, measured)

```
python3 -B verifiers/verify_surfaces.py \
  --omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings \
  --opencode-strings /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings --json
→ exit 1; 4 PASS / 3 FAIL
```
- `surfaces.literal_present` FAIL names all 8 loader-group rows including `omp:gemini/GEMINI.md`, `omp:gemini/system.md`, `omp:gemini/SYSTEM_TEMPLATE.md`, each as `no (Id|Cl|jD[ef]|Tl|dr|GW|Co|Dl|Hj|I5|Gl|Mo)(<v>, <group>, "<file>.md") call shape for (gemini, …)`. Note the diagnostics: the **literal test passed** (`e["literal"] in dump`, `verifiers/verify_surfaces.py:517`) — only the call-shape test failed (`:523-529`).
- `surfaces.no_uncovered_class` FAIL: `vacuity: 0 loader class(es) extracted … while the baseline declares 8` plus `extractor blind: 33 declared literal(s) present`.
- Direct measurement of the pinned regex (`OMP_CALL_RE`, `verifiers/verify_surfaces.py:155-160`) over the whole 18.12.5 dump: **0 matches** (CALL_RE also 0). The allowlist's names (`Id, Cl, jDe/jDf, Tl, dr, GW, Co, Dl, Hj, I5, Gl, Mo`) still exist as unrelated minified functions — e.g. `function jDf(` = 0, `function Id(` = 5 — but none carries the `(v, <group>, "<file>.md")` shape in this build. This is the "minification-volatile, FIRST thing to re-pin" case the code comment at `:138-149` describes, now two generations on.

## 5. Re-pin evidence (the 18.12.5 generation)

An all-callee sweep for the exact `(v, <group>, "<file>.md")` shape over the dump finds **11 call sites with exactly 3 callees**:

| callee | sites | lines |
|---|---|---|
| `lq` | 2 | 895129 (`agents-md`/`AGENTS.md`), 895140 (`claude-md`/`CLAUDE.md`) |
| `Xl` | 5 | 898856, 898994, 898995, 899090 (`opencode`), 900239 (`windsurf`) |
| `Fo` | 4 | 898867, 898992, 898993, 899328 (`github`) |

Resolving identifier groups through the existing constant table (`f$ = "agents-md"` :895126, `m$ = "claude-md"` :895137; `constant_table`, `:299-312`) yields **8 unique pairs, exactly equal to the 8 declared loader-group rows, with no undeclared pair**:

```
('agents-md','AGENTS.md') ('claude-md','CLAUDE.md') ('gemini','GEMINI.md')
('gemini','SYSTEM_TEMPLATE.md') ('gemini','system.md') ('github','copilot-instructions.md')
('opencode','AGENTS.md') ('windsurf','memories/global_rules.md')
```

Two-way parity 8 == 8 (both `no_uncovered_class` directions and all 8 `literal_present` shapes). So the C1 surfaces re-pin is: extend `OMP_CALL_RE` + `CALLEE_SHAPES["omp"]` with `lq|Xl|Fo` and record the 2026-10-21 generation in the comment block. This is a pin update, not a class change — every gemini row stays `governed` with its existing literal.

## 6. Counterexamples and calibration notes

- **Name ≠ identity.** `Xl(` occurs 29× with 3 function definitions; `Fo(` 54× with 7 definitions. The name alone proves nothing; the anchor is the 3-argument `.md` shape plus `fO[t].userAgent`/`fO[t].projectDir` in the callee bodies (:862497, :862510). If the integrator wants a fail-closed derivation rather than a name pin, witness those definitions alongside the allowlist.
- **No aliased-callee over-match in this dump.** All 11 shape sites call the callee directly; the shape does not match `const y = Xl; y(v, "g", "x.md")`. The self-test's decoy arm (`strings-omp-clean.txt`/`strings-omp-newcallees.txt`: `const xSomeId = …; xSomeId(e, "evil", "EVIL.md")`) is preserved by the shape regex.
- **Self-test fixture is one generation stale (operability gap).** `verifiers/fixtures/surfaces/strings-omp-newcallees.txt` covers only `Co/Dl/Hj` (2026-10-16) and `I5/Gl/Mo` (2026-10-18); the self-test arm `verifiers/verify_surfaces.py:815-822` therefore stays green on the old pin while the live dump extracts 0. Any re-pin must extend that fixture with the `lq/Xl/Fo` generation, else the fixture stops guarding exactly the defect this round fixes.
- **Other `SYSTEM_TEMPLATE.md` loaders are other families.** :896216/:896218 (`Pr`, `SYSTEM.md`+template, agent-system-prompt), :897967/:897969 (`jo`, `.agent/.agents` walk-up), :898666/:898668 (`ti`, another provider) — none carries `"gemini"`, so there is no second gemini call site and no hidden `omp:gemini/*` class.
- **Adjacent excluded rows are unaffected.** `settings.json`/`extensions` evidence is live (:898937/:898953, :898885/:898891, :898926/:898927), literals already pass `literal_present`; their `excluded` verdicts rest on kind, not on the omp shape extractor.

## 7. Commands run (all read-only; cwd `/fast/scratch/kotoba-r47/shared` unless noted)

| command | exit | key output |
|---|---|---|
| `sha256sum -c SHA256SUMS` | 0 | 4/4 `OK` |
| `grep -n -F '"gemini", "GEMINI.md"' omp-18.12.5.strings` | 0 | 898856, 898867 |
| `grep -n -F '"gemini", "system.md"' omp-18.12.5.strings` | 0 | 898993, 898995 |
| `grep -n -F '"gemini", "SYSTEM_TEMPLATE.md"' omp-18.12.5.strings` | 0 | 898992, 898994 |
| `grep -n -F 'Load GEMINI.md context files' omp-18.12.5.strings` | 0 | 557997, 898979 |
| `grep -n -F 'Load system.md custom system prompt files' omp-18.12.5.strings` | 0 | 557998, 899000 |
| `grep -n '^function Xl(e, t, n)\|^function Fo(e, t, n)\|^function nLe(e, t, n)\|^async function lq(e, t, n)' omp-18.12.5.strings` | 0 | 862497, 862506, 862510, 862812 |
| `awk 'NR>=898974 && NR<=899003'` (registration block numbering) | 0 | see §3 |
| `python3 -B` script: `OMP_CALL_RE.findall(dump)` | 0 | 0 matches; all-callee `.md` shape sweep → 11 sites / callees `{lq:2, Xl:5, Fo:4}`; allowlist `lq|Xl|Fo` → 8 pairs equal to the 8 declared |
| `python3 -B verifiers/verify_surfaces.py --omp-strings …18.12.5.strings --opencode-strings …1.19.3.strings --json` (cwd lane repo) | 1 | 4 PASS / 3 FAIL; gemini rows in `literal_present` detail |
| `sha256sum /home/vgpnk/.local/bin/omp` | 0 | `fdbc8136…` (same as snapshot) |
| `/home/vgpnk/.local/bin/omp --version` | 0 | `omp/18.12.5` |
| `strings -n 4 /home/vgpnk/.local/bin/omp \| sha256sum` | 0 | `33df0aef…` — byte-identical to the snapshot dump |
| `python3 -B -c "json.load(verifiers/surfaces-baseline.json)…"` | 0 | 38 classes; 3 `omp:gemini/*`; 8 loader-group |
| `grep -c "function <name>("` for the pinned callees | 0 | `jDe` 1, `jDf` 0, `Id` 5, `Cl` 2, `Tl` 2, `dr` 6, `GW` 2, `Co` 7, `Dl` 3, `Hj` 1, `I5` 2, `Gl` 3, `Mo` 7 |
| `grep -n '^var Al = \|^var xy = \|^var vIe = '` + `awk` context | 0 | `Al`=context-files :892076, `xy`=system-prompt :892242, `vIe`=extensions :892094 |
| `python3 -B -m json.tool .ufo/waves/round-47/build/C1ClassGemini.extract.json` | 0 | artifact valid |

Artifact: `.ufo/waves/round-47/build/C1ClassGemini.extract.json` (6.2 KiB) — machine-readable copy of §1/§3/§5 with the same line numbers.

## 8. What I did NOT check

- `verifiers/check_substrate_pins.py` pin values and the opencode 1.19.3 side of C1 (other seats own those; I only used the dump paths).
- `verify_surfaces.py --self-test` execution after a widened allowlist — I inspected the fixture text and the arm at `:815-822` but did not mutate or run it.
- Whether `Xl|Fo|lq` stay valid for a future build; the pin is a snapshot, not a derivation (see the definition-anchor suggestion in §6).
- Non-gemini families' semantic re-derivation (github/windsurf/opencode/agents-md were only swept for shape/parity, not re-read in full).
- Binary-level (rather than strings-dump) offsets; all line numbers are dump-relative.
