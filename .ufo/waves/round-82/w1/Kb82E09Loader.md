# Kb82E09Loader — C1 independent extraction probe, group `agents-md`

Seat: round-82 build+attack wave, C1 freshness outside guard (independent host
loader re-derivation).  Base `47dbe8781657de563ff867caca6244d28e3db504`.
Scope: bounded extraction probe + receipts only — no production edit, no
production after-score.  All work in scratch
`/fast/scratch/hyaku/kotoba-r82/Kb82E09Loader/`; fleet tree written only at
this report and the sibling `build/Kb82E09Loader*` artifacts.

## Host substrate measured

- Binary: `/home/vgpnk/.local/bin/omp` — ELF x86-64, **omp/18.14.0**,
  size 276244656, mtime 2026-10-29 23:19:46 -0300.
- sha256 **before** probe: `e7dd2b606c4ebe9d1a7bcfad1b8820db968cd6b05409fed1c6bc8db0b6a95a8f`
- sha256 **after** probe:  `e7dd2b606c4ebe9d1a7bcfad1b8820db968cd6b05409fed1c6bc8db0b6a95a8f`
  (identical — the probe is read-only; receipts
  `build/Kb82E09Loader_binary-{before,after}.txt`).
- Dump: `strings -n 4` of the ELF, 2546731 lines, 3261 module-marker
  (`// …​.ts`) lines; dump sha256 `81277d3572277febcaf0853f10cf8778c64920f58a13fba98ef0accbb70a8319`
  (kept in scratch; reproducer command in receipts).

## Probe (independent re-derivation of the documented grammar)

`build/Kb82E09Loader_probe.py` re-implements the extraction grammar documented
in `verifiers/verify_surfaces.py` (round-51 module-scope resolution, round-52
callee admission against declared pairs, round-51 param-shadow guard) without
importing the verifier, and applies it to the dump.  Baseline used:
`verifiers/surfaces-baseline.json` at base (sha256
`6b23c3d1c8766e4effea9f5502b638de7b22cd0d61be20426ba99482c7d1260b`, 42 classes;
identical to the current fleet worktree copy).

### Result — group `agents-md` EXISTS on the current host ELF

Exactly one registration call for the group, at dump line 972670, module
anchor `// packages/coding-agent/src/discovery/agents-md.ts`:

```
// packages/coding-agent/src/discovery/agents-md.ts
var nD = "agents-md";
var AQ = "AGENTS.md";
async function U3t(u) {
  return F9(u, nD, "AGENTS.md");
```

- Callee `F9` (minified; 18.12.6 used Kl/Ho/bq — the expected churn the
  round-52 admission design absorbs), group identifier `nD` bound once in the
  whole dump (`var nD = "agents-md"`, line 972667) → resolved via the dump-wide
  table; the call's own module scope binds it identically (audit in
  `build/Kb82E09Loader_probe-output.json`).
- Extracted pair: **(`agents-md`, `AGENTS.md`)** — declared at base as
  `omp:agents-md/AGENTS.md` (loader-group, governed).  Distinct pairs for this
  group: 1 extracted, 1 declared, 0 undeclared.

### Full sweep vs `surfaces-baseline.json` at base

- 11 shape calls, 3 distinct callees (`F9`, `Ac`, `ts`), 8 distinct pairs —
  **exactly the 8 omp `loader-group` classes declared at base**
  (agents-md/AGENTS.md, claude-md/CLAUDE.md, gemini/GEMINI.md,
  gemini/SYSTEM_TEMPLATE.md, gemini/system.md, github/copilot-instructions.md,
  opencode/AGENTS.md, windsurf/memories/global_rules.md).
- `extracted_not_declared`: **none** — no undeclared class surfaces.
- `declared_not_extracted`: 25 pairs — all `loader-literal`/`loader-config`/
  `excluded` kinds, outside the documented `(group, "<file>.md")` call set by
  design; every one of their literals still occurs in the dump
  (`build/Kb82E09Loader_literal-audit.txt`).

### Control-world cross-check

`build/Kb82E09Loader_crosscheck_verifier.py` (scratch clone at base) ran the
frozen verifier's own `extract_classes` on the same dump: 8 pairs,
**agree=true** with the independent probe; `agents-md/AGENTS.md` present in
both.  This is a control-world agreement check, not a production after-score.

### False-match decoys

`build/Kb82E09Loader_decoy_battery.py` — 8 synthetic fixtures through the same
implementation, 8/8 pass (`build/Kb82E09Loader_decoy-output.json`):

1. alias callee with no declared pair (`q(u,"evil","EVIL.md")`) → never admitted;
2. param-shadowed group ident (`function load(u,nD){F9(u,nD,"AGENTS.md")}`) →
   `<unresolved-var:nD>`, never resolves to agents-md;
3. cross-module rebind (a.ts binds `nD="agents-md"`, b.ts `nD="title"`, call in
   b.ts) → resolves to `title`, no false agents-md match;
4. non-`.md` file (`F9(u,nD,"rules")`) → outside the set;
5. quoted group positive control → matches;
6. no module markers + conflicting rebind → conservative unresolved;
7. wrapped call `s(F9(...), "project", "text")` → matches (bundle norm);
8. member-expression callee (`c.reg(...)`) → rejected by the `(?<![A-Za-z0-9_$.])`
   lookbehind.

## Risks / notes

- The probe proves set parity over the documented extraction for the
  agents-md group on omp 18.14.0 — not existential completeness (documented
  limits of the grammar stand).
- Callee names are minification-volatile; the round-52 admission path is what
  makes this re-derivation stable.  No pin/pins.json edit was made or scored
  here — L1/integration owns the counter and pins.
- `strings` stderr empty; dump command exit 0 (receipt
  `build/Kb82E09Loader_strings-stderr.txt`).

VERDICT: agents-md group independently re-derived on host omp 18.14.0 — 1 distinct pair (`agents-md`,`AGENTS.md`), matching base declaration, zero undeclared pairs, decoy battery 8/8, probe/verifier extraction agree, binary sha256 unchanged by measurement.

DELIVERABLES:
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82E09Loader.md
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E09Loader_probe.py
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E09Loader_decoy_battery.py
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E09Loader_crosscheck_verifier.py
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E09Loader_probe-output.json
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E09Loader_decoy-output.json
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E09Loader_crosscheck-output.json
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E09Loader_binary-before.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E09Loader_binary-after.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E09Loader_strings-stderr.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E09Loader_literal-audit.txt
