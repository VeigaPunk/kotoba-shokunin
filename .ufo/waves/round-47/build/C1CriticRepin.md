verdict: C1 as written is launderable — 7/7 + 3/3 is reachable with ZERO re-derivation (demonstrated: a constants-only verifier edit, BASE baseline+census untouched, gives surfaces 7/7 exit 0 and self-test 87/87); the after-target must add a class ledger and the discriminating probes below, and opencode 1.19.3 is a channel/generation swap (not a successor of v2.0.26) whose retired classes are back.

Seat: MoriR22R.C1CriticRepin-9 (critic, leaf). BASE c61a973b2e02e1ded169703ddcb06466f4edd8bd. Lane-authored advice, not closure.
Axes judged: freshness (primary), calibration, operability. Tools installed/updated: none.
Artifacts: `C1CriticRepin.launder-counterexample.patch` (do NOT integrate — the vacuous pass), `C1CriticRepin.probes.patch` (adds scratch `probes.py`, the falsifier), `C1CriticRepin.probes.json` (probe results on BASE / single-reanchor / dual-generation).

## Findings

### F1 — the vacuous pass exists and is cheap (freshness, calibration)
Edit only constants in `verifiers/verify_surfaces.py` (add `Xl|Fo|lq` to `OMP_CALL_RE` :155-159 / `CALLEE_SHAPES` :160-163; repoint `OC_PROJECT_FN` :359 → `InstructionContext.observe`, `OC_READ_*` :377-381 → `Instruction.resolve` / `y=["AGENTS.md"` / `"CONTEXT.md"` / `Instructions from:`, `OC_API_ID` :394 → `instructions:{entry:{list:`). No baseline, census or fixture change.
- single re-anchor: live 7 PASS exit 0; `--self-test` exit 1 (4 failures, v2.0.26 fixtures).
- dual-generation (each OC rule accepts old OR new anchors): live 7 PASS exit 0 **and** `--self-test` 0 failures / 87, exit 0.
So "surfaces 7/7 exit 0" + "self-test green" + "pins 3/3" is satisfiable while every record about opencode stays false (F2). This is the exact Q09 laundering (`corpus/QUALITY.md:20`): green without the extraction being re-derived.

### F2 — opencode 1.19.3 is not v2.0.26's successor; the retired generation is back (freshness, calibration, identity)
- Dump version literal `var n="1.19.3",t="latest"` (1 hit); `"2.0.26"` 0 hits. Baseline pinned v2.0.26 (`verifiers/baseline.json:9`, `:11` round18_move). Lower semver, different channel (npm `opencode-ai` via `~/.local/bin/opencode`, which runs `npx --yes --prefer-online --package opencode-ai` unpinned on every call).
- Census `corpus/knowledge/instruction-surface-census-round13.md:169-171` retired seven round-13/14 ids because these anchors had 0 occurrences in v2.0.26. In the frozen 1.19.3 dump: `CONTEXT.md` 1, `disableClaudeCodePrompt` 3, `Instruction.resolve` 1, `InstructionContext.observe` 1, `system-context-builtins` 1, `"@opencode/Instruction"` 1, `Instruction.systemPaths` 1. The v2.0.26 anchors the census rows cite (:206-209) are gone: `ConfigInstructionPlugin` 0, `ReadTool.Plugin` 0, `SessionInstructions` 0, `session.instructions.entry.put` 0, `j5(r.config,"AGENTS.md")` 0, `InstructionDiscovery` 0, `instructions rescanned` 0.
- Two loader generations co-reside: legacy `@opencode/Instruction` (`n=[X.join(r.config,"AGENTS.md"),...X.join(r.home,".claude","CLAUDE.md")]`, `y=["AGENTS.md",...CLAUDE.md,"CONTEXT.md"]`, `findUp` first-match, remote `https://` filter + `Fo.HttpClient`) and `instruction-context` (`InstructionContext.observe` → `H.up({targets:["AGENTS.md"],start:S,stop:$})` + `jX(L.config,"AGENTS.md")`, key `core/instructions`). Which is live is not decidable from strings [INFERENCE: both compiled in; liveness unproven, same limit as `verify_surfaces.py:40-41`].
- **Identity change, same id**: census :190-192 says the read-hook "keeps only hits *outside*" the project; 1.19.3's `Instruction.resolve` walks `while(G.startsWith(N)&&G!==N)` — *inside* the instance directory, first-match over AGENTS/CLAUDE/CONTEXT. Re-anchoring `opencode:read-hook/AGENTS.md` (`surfaces-baseline.json:259`) onto it keeps an id whose behaviour and literal set changed.
- **False exclusion reason**: `opencode:config/instructions` (`surfaces-baseline.json:273`; census :223 "**no loader consumer proven**") — 1.19.3 has the consumer `if(T.instructions)for(let O of T.instructions){...e.glob(...)...w.add(X.resolve(R))}` in `Instruction.systemPaths`. `check_excluded_reason` (`verify_surfaces.py:746-765`) only tests non-empty reason (:759), so the false reason stays PASS.
- **API class is client-only**: `opencode:api-entries/instructions` (`surfaces-baseline.json:266`) — only SDK client `instructions:{entry:{list,put,remove}}` at `/api/session/${…}/instructions/entries` (1 hit); `:sessionID/instructions` 0, `experimental/session/…instructions` 0. Re-anchoring OC-6 onto the client object (as F1 does) silently changes the class from "server route + operation id" to "client SDK method".

### F3 — OC-2 is already green-for-the-wrong-reason at BASE (calibration)
`OC_GLOBAL_JOIN_RE` (`verify_surfaces.py:366-367`) = `[A-Za-z_$][A-Za-z0-9_$]*\(r\.config\s*,\s*"AGENTS\.md"\)` matches `X.join(r.config,"AGENTS.md")` in the legacy `@opencode/Instruction` service (`join` is the identifier). Its derivation anchor `j5(r.config,"AGENTS.md")` (census :187, :207) is absent, and the instruction-context path uses `jX(L.config,…)` which it does NOT match. OC-2 passes at BASE on a different loader than the one it certifies — this is why the before-state shows only OC-1/4/6 red. A re-derivation that leaves OC-2 untouched inherits a wrong-reason pass.

### F4 — omp side: honest re-derivation is mechanical; two traps (freshness, operability)
- Wildcard-callee probe over the frozen omp dump yields exactly the 8 declared `.md` pairs via `Xl` 5, `Fo` 4, `lq` 2; `m$`→`claude-md`, `f$`→`agents-md` resolve uniquely (no conflicting rebinding); old callees (`I5|Gl|Mo` …) contribute 0. Non-`.md` `Xl/Fo` registrations stay inside declared groups (cursor, gemini, github, opencode, vscode, windsurf). `omp --version` → `omp/18.12.5`.
- Trap A (Q09 defeat): replacing the allowlist with a wildcard callee makes M3 (callee rename) go green forever — renames would stop turning freshness red. That is a tradeoff the integrator must state explicitly, not slip in. The appended allowlist (15 two-letter names) is the established pattern (`verify_surfaces.py:139-145`).
- Trap B (pre-existing near-vacuity, NOT a C1 regression): `literal_present` on `loader-literal`/`loader-config` rows probes generic tokens (`rules` ×3 `surfaces-baseline.json:64,71,106`, `prompts`, `skills`, `AGENTS.md`); the BASE run reports all 33 omp literals present while 0 shapes extract. Only the 8 `loader-group` rows are truly discriminated. Do not count `literal_present` PASS as evidence of re-derivation.

### F5 — pins: re-pinning is inherently a copy; the launderable parts are WHICH binary and WHEN (freshness, operability)
- Wrapper pin is vacuous (demonstrated): baseline pinning `opencode_binary_sha256=b240efa9…` (sha of the 1460-byte bash wrapper) + `--opencode-binary ~/.local/bin/opencode` → `OK 3/3 pins hold`, exit 0, independent of the ELF that actually runs.
- Legit target holds: omp `fdbc8136…` + mtime `2026-10-21T03:30:38.135013187-03:00` + opencode `179ca421…` → 3/3 exit 0 both against the npx ELF and the frozen snapshot (snapshot is a separate inode with identical mtime; `sha256sum -c` 4/4 OK).
- Duplicate authority: the opencode path lives in three constants — `verify_surfaces.py:128-131`, `check_substrate_pins.py:61-64`, `verify_harness_claims.py:52,55` (pins docstring :40-43 claims they are "the same constants"). Re-pinning one and not the others splits the substrate identity across gates.
- Moving target: `/home/vgpnk/.npm/_npx/e2094862b59aac7b/…/opencode-linux-x64/bin/opencode` (mtime 2026-10-20 18:33, link count 2) is overwritten whenever anyone runs `opencode` and a newer `latest` exists. That is correct drift behaviour for a pin, but the pinned sha MUST equal the sha of the binary the extraction was derived from (SHA256SUMS), or the pin certifies a binary nobody re-derived. [INFERENCE] the npx dir hash is a function of the package spec and stays stable; not verified.

### F6 — is 7/7 + 3/3 the right after-target?
Necessary, not sufficient. 7 is the CHECK count (`CHECK_IDS` :174-182), invariant to the class set: removing a dead class from baseline+census together keeps 7/7, so "never silently dropped" (plan :26) has no machine witness. 3/3 is satisfiable by pure copy (F5). Add a **class ledger** to the after-target: for each BASE opencode id (5: project/AGENTS, config/AGENTS, read-hook/AGENTS, api-entries/instructions, config/instructions[excluded]) and each census-retired id (:172-174, 7 ids) a verdict ∈ {retained+re-anchored, re-verdicted, retired, resurrected} with the frozen-dump count command (Q14, `corpus/QUALITY.md:25`). Expected class count after is likely ≠ 5 [INFERENCE from F2]; a ledger that ends at exactly the BASE 5 ids with no resurrected/re-verdicted entry should be treated as suspect.

## Minimum evidence for "re-derived, not copied"

1. **2×2 matrix on the frozen dumps** (`--omp-strings/--opencode-strings` = shared snapshot): {BASE code, AFTER code} × {BASE baseline+census, AFTER baseline+census}. Only AFTER×AFTER may exit 0. The discriminating cell is **AFTER code × BASE data → must be red**; under F1's laundering it is exit 0 (observed).
2. **Flip probes** (red at BASE, green after, and green *only because* of the re-derivation) — `probes.py` P-A…P-F:
   - P-A every backticked anchor in a census opencode evidence cell occurs in the 1.19.3 dump (BASE red: `ConfigInstructionPlugin.projectSource`, `j5(r.config,"AGENTS.md")`, `ReadTool.Plugin`, `SessionInstructions.load`, `session.instructions.entry.put`, …; laundering: red).
   - P-B census-retired anchors with non-zero counts each have a re-verdicted class (BASE red; laundering red).
   - P-C no `excluded` reason contradicted by the dump (`config/instructions` consumer) (BASE red; laundering red).
   - P-D the AFTER rules must NOT accept both the v2.0.26 fixture (`fixtures/surfaces/strings-opencode-clean.txt`, header "round 18 — v2.0.26 rule set") and the 1.19.3 dump (dual-generation laundering: red; single: green).
   - P-E derive-not-witness: plant `"GUIDE.md"` into the 1.19.3 priority array `y=[…,"CONTEXT.md"]` → must go red naming an undeclared class (laundering: stays exit 0 → red probe).
   - P-F drop `"CONTEXT.md"` from that array → the failure must name a CONTEXT.md class, not misattribute to `read-hook/AGENTS.md` (laundering: misattributes → red probe).
3. **Must-stay-red mutations** (run on AFTER code+data; meaningful only once the unmutated run is exit 0): M1 delete the two `"gemini", "GEMINI.md"` call lines → `literal_present` names `omp:gemini/GEMINI.md`; M2 omp dump truncated to 1% → red; M3 rename `Xl/Fo/lq(u,`→`Zq(u,` → red (unless Trap A is an explicit decision); M4 re-kind `omp:gemini/GEMINI.md` → `doc` in baseline+census → `->doc` laundering FAIL; plus per-new-OC-anchor drop → named FAIL; plus empty opencode dump → vacuity FAIL. All four M-probes stay red under BOTH laundering patches — they guard regressions but do NOT prove re-derivation.
4. **Pins provenance**: pinned shas == `/fast/scratch/kotoba-r47/shared/SHA256SUMS` lines for the dumped binaries; opencode default path is an ELF (`file` says ELF), never the wrapper; the three path constants agree; mtime pin has 9 fractional digits.

What a vacuous pass looks like here: 7/7 + 3/3 + self-test green with `git diff c61a973b -- verifiers/surfaces-baseline.json corpus/knowledge/instruction-surface-census-round13.md` touching no opencode row, OC rules OR-ing old and new anchors, `opencode:config/instructions` still "no loader consumer proven", and no `"CONTEXT.md"`/`.claude`/`https://` class verdict.

## Falsification checklist for wave 2
Run in a scratch clone of the integrated head; `S=/fast/scratch/kotoba-r47/shared`.
1. `python3 -B verifiers/verify_surfaces.py --json` (default resolution) → exit 0, 7 PASS; and with `--omp-strings $S/omp-18.12.5.strings --opencode-strings $S/opencode-1.19.3.strings` → same verdicts (default path dumps the same binary).
2. `python3 -B verifiers/check_substrate_pins.py` → `OK 3/3`; shas equal SHA256SUMS lines 1–2; `file` on the opencode default path → ELF.
3. `rg -n 'opencode/bin/opencode|_npx|\.local/bin/opencode' verifiers/*.py` → one value, in all three constants (or one shared constant).
4. 2×2 matrix: AFTER verifier with BASE `surfaces-baseline.json` + census (via `--baseline/--inventory` from `git show c61a973b:…`) → must be exit ≠ 0.
5. `python3 -B probes.py <head>` (from `C1CriticRepin.probes.patch`) → P-A…P-F green; adapt P-B/P-C/P-F class names to the ledger's chosen ids, never their semantics.
6. P-D: AFTER code on `fixtures/surfaces/strings-opencode-clean.txt` must fail, or the fixture set must be re-derived for 1.19.3 with a v2.0.26 fixture kept as a must-fail generation probe.
7. M1–M4 + per-OC-anchor drop + empty opencode dump → each red, naming its class.
8. Class ledger present (report or census append-only errata): every BASE opencode id and every census :172-174 id has verdict + count command + count on the frozen dump; no id silently absent from both baseline and ledger.
9. Census edits are append-only errata on § B (like :163-175), not rewrites of the v2.0.26 text.
10. `--self-test` for both verifiers exit 0, and the self-test contains at least one 1.19.3-shaped opencode fixture plus an `Xl/Fo/lq` omp fixture.
11. Trap A: if the callee allowlist became a wildcard, the report states that Q09 rename-red is traded away and names what now turns red on a rename (pins only).

## Smallest safe correction
Keep the omp half as an allowlist append (`Xl|Fo|lq`) plus a fixture. For opencode, re-derive the rule set from the 1.19.3 shapes in F2 *with* a baseline+census re-verdict (not constants only). Make OC-1/OC-4 DERIVE names from the priority array (as the round-14 `OC_MD_NAME_RE` at :361 intended), so P-E and P-F can discriminate. Re-verdict `config/instructions` and `api-entries/instructions`. Re-anchor or re-derive OC-2 off `r.config`. Pin the npx ELF in all three constants. Ship the class ledger. If that is out of round scope, C1 is honest only as "omp re-derived + re-pinned; opencode re-pinned with extraction RED (Q09 debt)", not 7/7.

## Commands run (exit codes)
- `git rev-parse HEAD` → c61a973b… (0); `sha256sum -c SHA256SUMS` in shared → 4 OK (0).
- BASE `verify_surfaces.py --omp-strings … --opencode-strings …` → 4 PASS / 3 FAIL (1); `--self-test` → 0/87 failures (0).
- BASE `check_substrate_pins.py` → DRIFT 3/3, UNREADABLE opencode (2); `--opencode-binary $S/bin/opencode-1.19.3` → DRIFT 3/3 (1); `--self-test` → 0/62 (0).
- scratch single re-anchor: live 7/7 (0); self-test 4 failures (1). Dual-generation: live 7/7 (0); self-test 0/87 (0).
- `probes.py` → BASE (1) red P-A,P-B,P-C,P-F (M4 red only because BASE extraction is blind); single (1) red P-A,P-B,P-C,P-E,P-F; dual (1) red P-A,P-B,P-C,P-D,P-E,P-F. M1–M3 red-as-required in all three.
- pins with temp baselines: legit vs npx ELF (0), legit vs snapshot (0), wrapper pin vs wrapper (0 — counterexample).
- `omp --version` → omp/18.12.5 (0). `rg -c/-o` anchor counts on the frozen dumps as quoted above (0).

## Addendum — RevPinsContract-9 cross-check (verified in scratch, BASE code)
- Confirmed: `check_substrate_pins.py:77-78` `DISCOVER_RE` kind class `[A-Za-z0-9]+` excludes `_`. With the legit pins plus `opencode_binary_resolved_sha256 = "0"*64` the guard prints `OK 3/3 pins hold`, exit 0, so the 4th key is silently unenforced. `opencode_binary_path` → `UNSUPPORTED 1/4`, exit 2. `opencode_launcher_binary_sha256` → `UNSUPPORTED 1/4`, exit 2 (it fails closed until the guard registers that substrate). Added to the wave-2 checklist: (12) no `measured_against` key matching `_binary_` is absent from the guard's verdict list (count keys vs `--json` `checks`), and a planted compound-kind key must not leave the guard green.
- Confirmed exec path: the wrapper's `which opencode-ai` finds no shim (`.bin/` has only `opencode`), so it falls back to `which opencode`. That resolves to `node_modules/.bin/opencode -> ../opencode-ai/bin/opencode.exe`, inode 43795736, link count 2, the same inode as `opencode-linux-x64/bin/opencode`, sha `179ca421…`. Pin `opencode-ai/bin/opencode.exe` as the default (same bytes, but it is the path that actually runs). F5 is refined, not reversed. Pinning the wrapper *instead of* the ELF is vacuous. Pinning it *in addition* as a separate launcher substrate is sound and closes a hole F5 left open: a wrapper edit that changes which artifact runs.

## Addendum 2 — review of `RevPinsContract.patch` (scratch clone of BASE)
- `git apply --check` exit 0; applied `--self-test` → 0 failures / 78 (exit 0). The kind widening works as claimed: `opencode_binary_resolved_sha256` and `omp_binary_sha256_r47` → UNSUPPORTED exit 2. Mis-cased `opencode_Launcher_binary_sha256` → mis-cased UNSUPPORTED exit 2. `binary_omp_sha256` → `OK 4/4`, exit 0, which is the documented residual (not `<prefix>_binary_<kind>`-shaped). Acceptable: such a key is not a pin under the contract. Narrow checklist item 12 to "every `<prefix>_binary_<kind>`-shaped key".
- **C1 target conflict:** the patch adds `opencode_launcher_binary_sha256` to `EXPECTED_PINS`. A baseline holding C1's three pins then fails as `PIN_ABSENT 1/4`, exit 1. If integrated, the plan's C1 after-target must read **pins 4/4**, and the re-pin must record the launcher sha `b240efa9…` taken from the same host state as the derivation.
- **Not in the patch:** `BINARIES["opencode"]` is still `/home/vgpnk/.opencode/bin/opencode` (patched file lines 92-94). Under the patch the BASE default run is still exit 2 UNREADABLE. The integrator must separately repoint it to `…/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe`, and keep the same value in `verify_surfaces.py:128-131` and `verify_harness_claims.py:55` (F5 duplicate authority).
- Residuals (accepted, named): the npm cache root relocation via `NPM_CONFIG_CACHE` or `~/.npmrc` (not live here); and the wrapper's runtime selection `mise where node@latest` is unpinned, so a node change can alter npx resolution without changing the launcher sha.

## Not checked
- Runtime liveness of either opencode loader generation (no opencode execution permitted; strings only).
- Whether `opencode-ai@latest` has moved since the snapshot (no network/npx run).
- That the npx cache dir hash is spec-stable (inference).
- `RevPinsContract.md` §2.1 discrimination table (only the patch itself was exercised);
- `verify_harness_claims.py` / `verify_harness_independent.py` behaviour after any re-pin; C2/C3; r46 residuals (mirror opt-out, NaN keys, row `kind`, etc.).
- omp non-registry loaders beyond the `Xl/Fo/lq` call shapes (e.g. walk-up, `RULES.md`), whose rows are discriminated only by generic literal presence (Trap B).
- No production file was modified; scratch clones at `/fast/scratch/kotoba-r47/C1CriticRepin/{base,single,lane}`.
