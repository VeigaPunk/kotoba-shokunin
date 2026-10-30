# Kb82E15Loader — C1 independent extraction probe, group `cline`

Seat: Kb82E15Loader (leaf; no subagents, no background jobs). Wave: round-82 w1.
Base: `47dbe8781657de563ff867caca6244d28e3db504` (scratch clone, shared,
`git -C` asserted toplevel before use). Scope: extraction probe + receipts
only — **no production edit**, no seat commit, no scoring of after-values.

## Assignment

C1 independent extraction probe for group **cline**: inspect the documented
extraction grammar of `verifiers/verify_surfaces.py` and the current host ELF
via `strings`; write a bounded Python probe extracting calls/literals for this
group with module-scoped variable resolution and source anchors; output
distinct pairs vs `surfaces-baseline.json` at base; sha256 the binary
before/after; include false-match decoys. Observed absence plus a full pattern
sweep is a valid result — and that is what the host produced.

## Method

1. Grammar read from `verifiers/verify_surfaces.py` @ base (clone):
   `OMP_GENERIC_CALL_RE` (line 239, round-52 callee-rename-robust
   registration-call shape), `MODULE_MARKER_RE` (248), `ASSIGN_RE` (251),
   `CLASS_ID_RE` (254), `PARAM_HEADER_RE` (510), `constant_table` (443),
   `module_scopes` (459), `scope_of` (474), `scope_table` (480),
   `param_shadowed` (517), admission per `extract_classes` (536) and
   `declared_loader_pairs` (587). The probe re-implements this grammar
   verbatim (it does not import the gate) and adds per-call source anchors
   (the module's source-path comment).
2. Host dump: `strings -n 4 /home/vgpnk/.local/bin/omp` (the documented dump
   command), exit 0 — 2,546,730 lines / 47,434,077 bytes,
   sha256 `81277d3572277febcaf0853f10cf8778c64920f58a13fba98ef0accbb70a8319`
   (receipt: `Kb82E15Loader-receipt-strings.txt`).
3. Probe run over the dump, six sections: A exact `cline` extractions;
   B substring pair sweep over all extracted groups; C identifier→string
   binding sweep (dump-wide + per-module); D raw token sweep (52 distinct
   tokens containing `cline`, classified exact-vs-substring with first-line
   anchors); E distinct-pair comparison vs baseline; F six synthetic decoy
   fixtures.

## Findings

### A. Group `cline` extraction: observed absence (valid result)

- Registration-shape calls in the 18.14.0 dump: **11 total**, all anchored in
  `// packages/coding-agent/src/discovery/{agents-md,claude-md,gemini,opencode,github,windsurf}.ts`.
  Calls inside `discovery/cline.ts`: **0**
  (artifact: `Kb82E15Loader-host-calls-anchors.json`).
- Extracted pairs with group exactly `cline`: **0**. Extracted pairs whose
  group contains substring `cline` (covers the `clinerules` decoy family):
  **0**.
- Why, with evidence: the 18.14.0 bundle **does** bind `var tk = "cline";`
  in `// packages/coding-agent/src/discovery/cline.ts` (dump line 975286),
  but that module loads `.clinerules` through a discovery walk
  (`R.find((_) => _.name === ".clinerules")`), not through the documented
  registration-call shape — so the grammar extracts nothing from it, loudly
  (no shape match) rather than silently. This is the module-scoped-resolution
  path doing exactly what the round-51 rule says: a binding only becomes a
  group when a registration call consumes it in-shape.
- The other cline bindings are Cline-provider identity, not instruction
  surfaces: `ove = "https://api.cline.bot/api/v1"`, `Wl = "cline-pass"`,
  `cd = "cline-pass/"`, and provider config `cline: {userBase: ".cline",
  userAgent: ".cline", projectDir: null}` (dump lines 939993–939994).

### B. Token sweep — the false-match decoy field

52 distinct dump tokens contain `cline`. Exactly **one** is the bare token
`cline` (5 occurrences, first at line 655645). The top decoys a naive
substring probe would mis-report as "cline": `declined` (23), `cline-pass`
(18), `.clinerules` (7), `clinepass` (5), `/$bunfs/root/chunks/cline-*` (4
each), `.cline` (3), `//api.cline.bot/api/v1` (3). The probe classifies all
52; only exact-token `cline` is marked `exact-token`.

### C. Baseline comparison at base (distinct pairs, both directions)

- Baseline `omp` declared pairs total: 33. Baseline pairs for group `cline`
  (exact): **∅** — both directions agree: extraction ∅, baseline ∅.
- Baseline substring family: `("clinerules", ".clinerules")` = the governed
  class `omp:clinerules/.clinerules` (loader-literal) — **not** present in
  the 18.14.0 extraction either (context for L1's re-pin; no group named
  `cline` is hidden inside it: `cline` is a *prefix* of `clinerules`, which
  is exactly why substring matching is the decoy, not the rule).
- Extracted-minus-baseline cline family: ∅. Baseline-minus-extracted cline
  family: `[("clinerules", ".clinerules")]`.

### D. Cross-check against the gate's own extractor (independent agreement)

On the same dump, `verify_surfaces.extract_classes` (declared mode, baseline
omp pairs): **8 pairs**; probe admitted set: **8 pairs**; sets equal,
symmetric difference empty. The gate's historical allowlist mode
(`OMP_CALL_RE`, round-50/51 callee names) extracts **0 pairs** on 18.14.0 —
every pre-18.13 minified callee name is gone from the bundle, so the round-52
generic shape is the only live extraction path on this host. Neither mode
yields any `cline` pair, and no `<unresolved-var:*>` group survives
(artifact: `Kb82E15Loader-crosscheck-gate.json`). The 8 agreed pairs:
`agents-md/AGENTS.md`, `claude-md/CLAUDE.md`, `gemini/{GEMINI.md,
SYSTEM_TEMPLATE.md, system.md}`, `github/copilot-instructions.md`,
`opencode/AGENTS.md`, `windsurf/memories/global_rules.md`.

### E. Decoy fixtures: 6/6 pass

F1 quoted `("cline","OK.md")` call is extracted (probe would catch a real
cline registration); F2 `("clinerules",…)` is **not** reported as cline;
F3 one minified name bound to `"cline"` in module A and `"other"` in module B
resolves per its own module scope with correct anchors; F4 a parameter-
shadowed identifier stays fail-closed unresolved; F5 an alias callee with no
declared pair is never admitted while a real callee's extra pair surfaces;
F6 an unbound identifier surfaces as `<unresolved-var:NAME>` (never guessed,
never dropped).

## Binary identity (before/after)

`/home/vgpnk/.local/bin/omp`, `omp/18.14.0` (`--version` exit 0), ELF 64-bit
x86-64, not stripped, 276,244,656 bytes. sha256 before:
`e7dd2b606c4ebe9d1a7bcfad1b8820db968cd6b05409fed1c6bc8db0b6a95a8f`;
sha256 after: identical (receipt: `Kb82E15Loader-receipt-binary-sha.txt`).
The probe did not modify the substrate.

## Risks / limits / blockers

- This is an extraction-grammar probe, not existential completeness (the
  verifier's own documented limit): a cline loader minified into a different
  shape would be out of the rule set by design. Mitigation: the full token
  sweep independently covers every `cline` byte in the dump, and the
  discovery-walk mechanism it found is named and line-anchored.
- The 8/33 host-vs-baseline pair context is L1's re-pin work; I report the
  measurement, I do not re-pin (seat boundary).
- No installs/upgrades performed; pacman untouched; disk-guard exit 0 before
  heavy work; contention kept to single bounded probe runs (≤4 procs).

VERDICT: group `cline` is **observed-absent** from both the 18.14.0 host
extraction and the base baseline, with a full pattern sweep, module-scoped
resolution, source anchors, 6/6 decoy discrimination, and gate/probe
8-pair set equality as the retained evidence.

DELIVERABLES:
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82E15Loader.md
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E15Loader-probe-cline.py
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E15Loader-probe-cline-report.json
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E15Loader-crosscheck-gate.json
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E15Loader-host-calls-anchors.json
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E15Loader-receipt-strings.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E15Loader-receipt-binary-sha.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E15Loader-receipt-probe.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E15Loader-receipt-crosscheck.txt
