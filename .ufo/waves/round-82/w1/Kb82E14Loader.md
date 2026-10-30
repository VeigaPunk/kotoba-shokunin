# Kb82E14Loader — C1 independent extraction probe, loader group `windsurf` (harness omp)

Seat: Kb82E14Loader (leaf, no subagents). Round 82, wave 1. Axis: freshness (C1 host
loader re-derivation input). Base: `47dbe8781657de563ff867caca6244d28e3db504`.
Assignment: inspect `verify_surfaces.py`'s documented extraction grammar and the current
host ELF via `strings`; write a bounded Python probe extracting calls/literals for THIS
group with module-scoped variable resolution and source anchors; output distinct pairs
vs `surfaces-baseline.json` at base, sha256 of the binary before/after, and false-match
decoys. No production edit; probe + receipts only.

## Inputs (read-only, from base)

- `verifiers/verify_surfaces.py` @47dbe878 (sha256 `df0c7cca…f8bab`). Grammar drift
  base→HEAD(`006a834`): **empty** — the extraction grammar is unchanged at HEAD; only the
  world moved (HEAD default still names the now-absent `~/.local/bin/omp.real`; the
  installed `~/.local/bin/omp` is an ELF, version 18.14.0).
- `verifiers/surfaces-baseline.json` @47dbe878 (sha256 `6b23c3d1…260b`): 42 classes,
  33 omp, 8 omp `loader-group` classes.
- Host substrate: `/home/vgpnk/.local/bin/omp` sha256
  `e7dd2b60…5a8f`, 276244656 bytes, mtime 2026-10-29 23:19:46 -0300.

## Documented grammar (restated from the base verifier, round-52 "declared" mode)

dump = `strings -n 4 <binary>`; module spans opened by `//<path>.[cm]?[jt]sx?` comment
lines; identifier→string bindings first-seen-wins with conflicting rebinds dropped
(dump-wide table), per-module scope table as fallback (dump-wide wins on overlap); a
group identifier that is a parameter of the nearest preceding function header in the
call's own module never resolves (fail-closed); call shape
`<callee>(<v>, <group>, "<file>.md")` with `<group>` a quoted lowercase word or an
identifier, lookahead `[,)]`; ANY callee is admitted only if one of its sites registers
a pair the baseline declares for omp (class-id parsed, any kind), and every pair of an
admitted callee is extracted; unresolved-var groups may admit via a declared file.
`windsurf` is declared at base as:
`omp:windsurf/memories/global_rules.md` (loader-group, governed) and
`omp:windsurf/rules` (loader-literal, governed).

## Probe (independent reimplementation, stdlib-only, bounded)

`build/Kb82E14Loader_probe.py` re-implements the grammar itself (does NOT import the
reference for its own result), then cross-checks against the reference functions.
One `strings` pass (exit 0, 2 s, dump 2546730 lines, sha256 `81277d35…a8319`); one probe
run (exit 0, ~20 s, single process, TMPDIR in seat scratch). Binary sha256 **before ==
after** (`e7dd2b60…5a8f`, same size/mtime/inode) — extraction mutated nothing.

### Result for group windsurf on omp 18.14.0

The group EXISTS (observed presence + full pattern sweep; absence would also have been
a valid result, but the loader is present and live):

| item | value |
|---|---|
| declared pairs at base | `(windsurf, memories/global_rules.md)` [loader-group], `(windsurf, rules)` [loader-literal] |
| extracted pairs, documented `.md` pass | `(windsurf, memories/global_rules.md)` — exactly the declared loader-group pair |
| distinct pairs only in extraction | **none** under the documented grammar |
| distinct pairs only in baseline | `(windsurf, rules)` — expected: kind `loader-literal` is probed by literal presence, not by the `.md` call shape; anchor call witnessed by the bounded extension below |
| literal presence | `memories/global_rules.md`: 4 dump occurrences; `rules`: 423 substring occurrences (generic word — presence check is weak by design for this entry, which is why the census carries the description-vs-code caveat) |

Source anchors (all four windsurf registration calls sit in one module):
module `// packages/coding-agent/src/discovery/windsurf.ts` (dump line 977739):

- line 977764 `const k = Ac(u, "windsurf", "mcp_config.json");`
- line 977767 `ts(u, "windsurf", "mcp_config.json")`
- line 977791 `const k = Ac(u, "windsurf", "memories/global_rules.md");`  ← documented extraction
- line 977802 `const A = ts(u, "windsurf", "rules");`

Module-scoped resolution: implemented per grammar (dump-wide first-seen table with
conflict-drop, per-module fallback table, nearest-preceding-header param shadowing
fail-closed). On 18.14.0 all four calls use **quoted** groups, so the identifier path
is unexercised on the live dump; the bindings `var rh = "windsurf"` / `var vF =
"Windsurf"` (lines 977740–977741) exist but no call references them. The resolution
machinery is instead validated on the committed fixture generations (below).

Bounded extension (same call shape, non-`.md` file arg; group-scoped, labeled as beyond
the documented grammar): `(windsurf, mcp_config.json)` ×2 calls and
`(windsurf, rules)` ×1 call. `mcp_config.json` is **not** declared in
`surfaces-baseline.json` — it is MCP-server config, not an instruction surface, so its
absence from the surfaces census is scope-consistent, NOT drift. Flagged for L1; no
surfaces-check failure is claimed or implied.

### Callee re-derivation evidence (the freshness payload)

The minified callee names rotated again; the static allowlist `OMP_CALL_RE`
(…`Kl|Ho|bq`, round 18.12.6) matches **nothing** on 18.14.0:

| generation | admitted callees (probe == reference) |
|---|---|
| 18.12.5 fixture (`strings-omp-18.12.5.txt`) | `Fo`, `Xl`, `lq` |
| 18.12.6 fixture (`strings-omp-18.12.6.txt`) | `Ho`, `Kl`, `bq` |
| 18.14.0 live dump | `Ac`, `ts`, `F9` |

`F9` registers `(agents-md, AGENTS.md)` and `(claude-md, CLAUDE.md)`; `Ac`/`ts` carry
the windsurf/gemini/github/opencode registrations. This is the re-derivation data the
C1 re-pin needs: extraction on 18.14.0 survives **only** via the round-52
declared-admission mode, exactly as the plan anticipated.

### Parity checks

- All-groups documented extraction on the live dump: exactly the 8 declared omp
  loader-group classes, **no undeclared `.md` pair** (vacuity guard satisfied).
- Probe vs reference `extract_classes` on the live dump: **8 == 8, only-in-reference ∅,
  only-in-probe ∅**.
- Probe vs reference on both committed fixture generations: equal, both fixtures.
- Reference `check_literal_present` over the two windsurf entries on the live dump:
  **PASS** — "2 loader-kind entries verified against the dumps".

### False-match decoys

`windsurf` (case-insensitive) occurs on 47 dump lines; the census classifies all of
them (`probe-output.json → decoy_census`). Exactly 4 lines are registration-call shapes;
the other 43 are decoys the grammar rejects:

| decoy class | lines | witness |
|---|---|---|
| chunk paths (`windsurf-cpgn0s20.js`) | 5 | 611286, 698733, 1346880, 2544100–2544101 |
| description strings | 4 | 655715, 977815 (`Load MCP servers from Windsurf config (mcp_config.json)`), 977821 (`Load rules from Windsurf (…, .windsurfrules)`) — **`.windsurfrules` lives only in description prose** (documented description-vs-code gap); 939889 |
| provider enable-set literal | 2 | 939396 `windsurf: true` inside `var me = {cursor, codex, claude, claude-plugins, gemini, opencode, windsurf, github}` (the census provider-gate set — project-level paths never gated); 939987 `windsurf: {userBase/userAgent/projectDir}` |
| env/telemetry idents + enum mappings | 17 | `WINDSURF_REVIEW`, `WINDSURF_SENTRY_SAMPLE_RATE`, `ANTHROPIC_WINDSURF_*`, `hasUsedWindsurf`, `windsurfProTrialEndTime`, … |
| module map key / dynamic import | 3 | 693698, 1349003 (`@oh-my-pi/pi-coding-agent/discovery/windsurf`) |
| identifier bindings (not calls) | 2 | 977740 `var rh = "windsurf";`, 977741 `var vF = "Windsurf";` |
| prose mentions (string-table, paths) | 10 | 655713–655716, 665544–665549 (`.codeium/windsurf`, `.windsurf`) |
| module marker | 1 | 977739 `// packages/coding-agent/src/discovery/windsurf.ts` |

A naive `grep -i windsurf` (47 hits) or a quoted-`"windsurf"` grep cannot separate
loader from decoy; the call shape + module-scope resolution + quoted-args/lookahead
conjuncts reject all 43.

## Risks / notes

- The `rules` literal probe is substring-weak (423 hits); the anchor call at line
  977802 is the load-bearing evidence, and the census already carries the caveat.
- `strings`-only evidence is the documented limit of this extractor (a loader reached
  through a differently-minified shape would be out of set); no runtime discovery is
  claimed.
- The `(windsurf, mcp_config.json)` registration is real but outside the surfaces
  census scope; reported for L1 disposition, not as a defect.
- Disk guard checked before work (exit 0); pacman untouched (host-wide pause); no
  installs this seat; contention cap respected (≤1 process per step, longest 20 s).

## VERDICT: group windsurf loader PRESENT and EXTRACTABLE on omp 18.14.0 (e7dd2b60…);
## independent probe == reference on live dump and both fixture generations; declared
## pair (windsurf, memories/global_rules.md) reproduced, (windsurf, rules) literal-probed;
## callees re-derived to Ac/ts/F9 (allowlist Kl/Ho/bq matches nothing); no undeclared .md
## pair; 43/47 token lines are decoys, all rejected; binary sha256 unchanged before/after.

## DELIVERABLES:
## /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E14Loader_probe.py
## /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E14Loader_probe-output.json
## /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E14Loader_fixture-crosscheck.json
## /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E14Loader_binary-identity.txt
## /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E14Loader_receipt.txt
