verdict: `omp:opencode/AGENTS.md` still EXISTS in omp 18.12.5 — but its 18.12.5 registration callee is `Xl` (`omp-18.12.5.strings:899090`), which the pinned allowlist at `verifiers/verify_surfaces.py:155-159` does not contain; extraction is 0/8 loader-group pairs and the verifier FAILs. Adding `Xl|Fo|lq` reproduces EXACTLY the 8 declared pairs (no extras, no misses) — the re-pin is a callee-name change, not a hash bump.

BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (`git rev-parse HEAD` exit 0). Snapshot `/fast/scratch/kotoba-r47/shared/` — `sha256sum -c SHA256SUMS` exit 0, 4/4 OK (`omp-18.12.5.strings` = `33df0aeffc45…b301`).

## 1. The baseline entry under witness

`verifiers/surfaces-baseline.json:19-25`:

```
"class_id": "omp:opencode/AGENTS.md"   (:20)
"harness": "omp"                       (:21)
"literal": "AGENTS.md"                 (:22)
"context_kind": "loader-group"         (:23)
"verdict": "governed"                  (:24)
```

It is the ONLY `omp:opencode*` entry (39 `class_id` lines total; `opencode:*` rows at :245-280 are the separate opencode-harness family, out of this slice). Provenance: `corpus/knowledge/instruction-surface-census-round13.md:75` cites the witness as `` `Id(e,"opencode","AGENTS.md")` `` — a callee that does not exist in 18.12.5 (sweep below). The baseline header at `verifiers/surfaces-baseline.json:3` says only the *opencode-harness* classes were re-derived at round 18; the omp:opencode row kept the round-13 callee name, which is exactly the drift.

## 2. Class still exists — witness chain in 18.12.5

Dump line numbers below are `/fast/scratch/kotoba-r47/shared/omp-18.12.5.strings` (2,443,339 lines, 48,115,461 bytes; `strings -n 4 bin/omp-18.12.5 | sha256sum` exit 0 reproduces the pinned dump digest exactly, so the dump is faithful to the pinned binary `fdbc8136084c…e7e`).

- **Loader body** — `async function qte(u) {` (:899087), first statement:
  `:899090:  const T = Xl(u, "opencode", "AGENTS.md");`
  then `const M = await Ue(T)` (:899092) and push `{ path: T, content: M, level: "user", _source: Ze(ho, T, "user") }` (:899094-899099). Return `{ items: p, warnings: R }` (:899101). So the literal is consumed as a user-level context file, not merely declared.
- **Registration** — `:899284-899289`:
  `Le(Al.id, { id: ho, displayName: Au, description: "Load AGENTS.md from ~/.config/opencode/", priority: _u, load: qte })`
  with `ho = "opencode"` (:899025), `Au = "OpenCode"` (:899026), `_u = 55` (:899027), and `Al` = the `Jo({ id: "context-files", displayName: "Context Files", … })` extension point (:892076-892079).
- **Family is alive, 6 registered loaders under the same group**: `id: ho` at :899285 (AGENTS.md, `load: qte` :899289), :899291 (MCP, `Qte`), :899297 (skills, `ene`), :899303 (plugins, `tne`), :899309 (commands, `rne`), :899315 (settings, `ine`). The group literal `"opencode"` appears in 6 call sites — :899077/:899083 (config `opencode.json`/`.jsonc` loop over `fk`, :899028), :899090 (AGENTS.md), :899201/:899202 (skills), :899221/:899222 (plugins), :899239/:899240 (commands) — and the whole file has 113 lines containing `opencode` and 13 containing `.config/opencode`.
- **Call shape resolves to the discovery helpers** — `fO.opencode = { userBase: ".config/opencode", userAgent: ".config/opencode", projectDir: ".opencode" }` (:862468-862471); `nLe` (:862497-862505) joins `home/userAgent/name`; `Xl(e,t,n)` = gate `Ii(t,e)` then `nLe` (:862506-862509); `Fo(e,t,n)` = `cwd/projectDir/name` (:862510-862514). Hence `Xl(u,"opencode","AGENTS.md")` is `~/.config/opencode/AGENTS.md`, gated by provider enablement `Ii` (:862059-862074). [INFERENCE] The chunk at :899021 imports only `os`/`path`, so the dump's name scoping (not an import list) is the binding evidence: `nLe` appears ONLY at its definition :862497, inside `Xl` :862509, and at :899239 in this same discovery chunk, which shows the discovery chunks share the helpers' top-level names. Note `Xl` is a reused minified name across unrelated chunks (:676246, :686325, :739666 as a judgment mapper, :1147554 as a timeout predicate, :1262170 as a lazy import) — the binding at :899090 to the discovery helper is inference from that shared-scope evidence, not a byte-level proof.

**Counterexample / semantic bound:** only the USER-level copy is loaded by this plugin. `Fo(u, "opencode", "AGENTS.md")` has 0 hits (`grep -c -F` exit 1), i.e. project `.opencode/AGENTS.md` is not produced by the `opencode` group here; the registry description ("Load AGENTS.md from `~/.config/opencode/`") agrees. Whether some other plugin covers project `.opencode/AGENTS.md` was NOT traced in this slice.

## 3. The pinned extraction does not see it — observed, not inferred

`OMP_CALL_RE` (`verifiers/verify_surfaces.py:155-159`) alternation is `Id|Cl|jD[ef]|Tl|dr|GW|Co|Dl|Hj|I5|Gl|Mo` (generation ledger :138-148; last pin 18.12.2 at :143). `Xl`, `Fo`, `lq` are absent.

- Verifier against the snapshot (script copied to my scratch, read-only inputs):
  `python3 verify_surfaces.py --repo <lane> --omp-strings …/omp-18.12.5.strings --opencode-strings …/opencode-1.19.3.strings --baseline <lane>/verifiers/surfaces-baseline.json --inventory <lane>/corpus/knowledge/instruction-surface-census-round13.md --check surfaces.literal_present --check surfaces.no_uncovered_class`
  → **exit 1**, `FAIL surfaces.literal_present: 8 loader literal(s) not verifiable: … omp:opencode/AGENTS.md (no (Id|Cl|…|Mo)(<v>, <group>, "<file>.md") call shape for (opencode, AGENTS.md) in omp dump) …`
  and `FAIL surfaces.no_uncovered_class: vacuity: 0 loader class(es) extracted … while the baseline declares 8 loader-group class(es) …; extractor blind: 33 declared literal(s) present …` (`--json` form same statuses, exit 1).
- Old-callee sweeps, all 0 hits (exit 1): `Id(e,"opencode","AGENTS.md")`; also `jDe(e,Pqr,"AGENTS.md")`, `Cl(e,"gemini","GEMINI.md")`, `Id(e,"gemini","GEMINI.md")`, `Cl(e,"github","copilot-instructions.md")`, `Id(e,"windsurf","memories/global_rules.md")`.
- Unspaced form `"opencode","AGENTS.md"` = 0 (exit 1); the live line has a space, which the regex tolerates. Broad sweep `, *"opencode", *"<...\.(md|json|jsonc|skills|plugins|commands)"` returns exactly one line: :899090.
- Literal presence alone is not witness: `"AGENTS.md"` occurs on 14 lines of the omp dump, so `literal_present`'s first arm passes and only the loader-group arm fails — the FAIL text above proves the verifier distinguishes them.

## 4. Re-pin slice (exact, calibrated)

Extending the omp alternation to `…|I5|Gl|Mo|Xl|Fo|lq` and replaying the verifier's own constant-table resolution over the dump yields 11 `.md` call shapes (:895129, :895140, :898856, :898867, :898992, :898993, :898994, :898995, :899090, :899328, :900239) → exactly 8 unique `(group,file)` pairs, and set equality with the baseline's 8 omp `loader-group` ids is **True** (no `only declared`, no `only extracted`). `lq` is required for `agents-md`/`claude-md` because the group arrives through the constant table (`f$ = "agents-md"` :895126 → `lq(u, f$, "AGENTS.md")` :895129; `m$ = "claude-md"` :895137 → :895140).

Operability notes for the integrator:
- `CALLEE_SHAPES` (`verifiers/verify_surfaces.py:160-163`) is user-facing FAIL text; update it with the alternation or the message misdescribes the live shape.
- The self-test fixture `verifiers/fixtures/surfaces/strings-omp-newcallees.txt` carries only `Co/Dl/Hj/I5/Gl/Mo`; it has ZERO `Xl(`, `Fo(`, `lq(` lines (same for every file under `verifiers/fixtures/surfaces/`), so a fixture generation for 18.12.5 is needed to keep the re-pin falsifiable (`verify_surfaces.py:816-820` is the current new-callee case).
- `Xl`/`Fo` are generic path helpers: a group arriving as an identifier absent from the constant table degrades to `<unresolved-var:…>` by design, so a re-pin must be checked against the whole dump (done here: all 11 shapes resolve; 8 pairs, no unresolved group).
- No production file was edited; this is advice, not a patch.

## 5. Commands run (exit codes)

| command | exit | key output |
|---|---|---|
| `sha256sum -c SHA256SUMS` (snapshot) | 0 | 4/4 OK |
| `strings -n 4 bin/omp-18.12.5 \| sha256sum` | 0 | `33df0aeffc45…b301` == pinned dump |
| `grep -n -F 'Xl(u, "opencode", "AGENTS.md")' omp-18.12.5.strings` | 0 | `899090:  const T = Xl(u, "opencode", "AGENTS.md");` |
| `grep -n -F 'async function qte(u)' …` / `'load: qte' …` | 0 | `899087`, `899289` |
| `grep -n -F 'id: ho,' …` | 0 | 6 lines :899285-:899315 |
| `grep -c -F '"opencode","AGENTS.md"' …` | 1 | 0 |
| `grep -c -F 'Id(e,"opencode","AGENTS.md")' …` | 1 | 0 |
| `grep -c -F 'Fo(u, "opencode", "AGENTS.md")' …` | 1 | 0 |
| `grep -n -E ', *"opencode", *"[A-Za-z0-9_./-]+\.(md\|json\|jsonc\|skills\|plugins\|commands)"' …` | 0 | only `899090` |
| `python3 verify_surfaces.py --check surfaces.literal_present --check surfaces.no_uncovered_class` (scratch copy, snapshot dumps) | 1 | both FAIL, `omp:opencode/AGENTS.md` named |
| same with `--json` | 1 | `status: FAIL` for both ids |
| extended-allowlist replay (`Xl\|Fo\|lq`) in Python | 0 | 11 shapes → 8 pairs; `got == declared: True` |

No tools installed or upgraded. No writes outside `.ufo/waves/round-47/build/`. No `omp` session launched (contract); only `strings`/`grep`/`sha256sum` and the verifier copy were executed.

## 6. What I did NOT check

- No runtime/session confirmation that the `opencode` discovery plugin is enabled and its items reach the system prompt; the activation gate `Ii` (:862059-862074) depends on `F()`/`ge`/`X()` data structures I did not recover (opt-out map contents unknown) — registration and consumption are static evidence only.
- Did not re-derive or verify the opencode-harness (`opencode:*`) classes, the `verify_surfaces` OC-1..OC-6 rules against `opencode-1.19.3.strings`, or `check_substrate_pins.py` — separate C1 slices; the dump digest check here covers only the omp dump.
- Did not apply the allowlist edit, extend fixtures, or run `--self-test` after such an edit (production files read-only; a self-test against fixtures without the new generation would not prove the re-pin).
- Did not prove the cross-chunk binding of the minified `Xl` at :899090 byte-for-byte (name-scoping inference stated above).
- Did not trace whether any other omp plugin loads project-level `.opencode/AGENTS.md`, nor the 33 non-loader literals named by the extractor-blind arm (their kinds are config/doc, not this class).
