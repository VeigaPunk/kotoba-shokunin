# Kb82E11Loader — C1 independent extraction probe, group `gemini`

Round 82 · seat Kb82E11Loader (leaf) · base `47dbe8781657de563ff867caca6244d28e3db504`
Scope: C1 freshness — INDEPENDENT extraction probe for loader group `gemini` on
the current host omp 18.14.0 ELF. No production edit; probe + receipts only.

## Host substrate measured (read-only)

- Path: `/home/vgpnk/.local/bin/omp` — ELF 64-bit x86-64, **276,244,656 bytes**,
  mtime 2026-10-29 23:19:46 -0300, version string `18.14.0` present in dump
  (`version: "18.14.0"`).
- sha256 **before** probe: `e7dd2b606c4ebe9d1a7bcfad1b8820db968cd6b05409fed1c6bc8db0b6a95a8f`
- sha256 **after** probe: `e7dd2b606c4ebe9d1a7bcfad1b8820db968cd6b05409fed1c6bc8db0b6a95a8f`
  → **unchanged** (probe opened the binary read-only; receipts
  `build/omp.sha256.before.txt`, `build/omp.sha256.after.txt`).
- Dump: `strings -n 4` exactly as the documented grammar states (with and
  without `-a` produced byte-identical dumps on this host): 2,546,731 lines,
  47,434,077 bytes, sha256 `81277d3572277febcaf0853f10cf8778c64920f58a13fba98ef0accbb70a8319`,
  3,261 module-marker lines (module scoping applicable).

## Method

Independent re-implementation of the documented extraction grammar
(`verify_surfaces.py` docstring §1 + `OMP_GENERIC_CALL_RE` / `ASSIGN_RE` /
`MODULE_MARKER_RE` / `PARAM_HEADER_RE` semantics), written from the
documentation only — the verifier is **not imported** by the probe
(`build/Kb82E11Loader_probe_gemini.py`). Module-scoped identifier resolution:
dump-wide first-seen/drop-on-conflict table wins where it settles a name;
otherwise the call's own module-scope table decides; function-parameter
identifiers never resolve (fail-closed). Baseline for comparison:
`verifiers/surfaces-baseline.json` at base (via read-only `git show`, sha256
`6b23c3d1c8766e4effea9f5502b638de7b22cd0d61be20426ba99482c7d1260b`;
identical to the working tree).

## Findings (bounded)

1. **gemini extraction = declared set, exactly.** Probe extracted pairs for
   group `gemini`: `(gemini, GEMINI.md)`, `(gemini, SYSTEM_TEMPLATE.md)`,
   `(gemini, system.md)` — **3/3 = the base baseline's declared omp
   loader-group gemini pairs**. `found-not-declared: []`,
   `declared-not-found: []`. Raw shape rule == round-52 callee-admission rule
   == declared set.
2. **Full sweep (no group assumed):** 11 registration-shape calls on the dump;
   8 distinct (group, file) pairs, all 8 matching the baseline's declared omp
   loader-group set (`agents-md/AGENTS.md`, `claude-md/CLAUDE.md`,
   `gemini/GEMINI.md`, `gemini/SYSTEM_TEMPLATE.md`, `gemini/system.md`,
   `github/copilot-instructions.md`, `opencode/AGENTS.md`,
   `windsurf/memories/global_rules.md`). 0 unresolved group tokens (all
   identifier-bound groups — `agents-md`, `claude-md` — resolved via const
   tables; all 6 gemini calls are quoted-literal).
3. **Source anchors:** all 6 gemini calls sit in one module,
   `// packages/coding-agent/src/discovery/gemini.ts` — `Qne` (GEMINI.md,
   user `Ac` / project `ts`, dump lines 976407/976418) and `nre`
   (SYSTEM_TEMPLATE.md + system.md, user/project, lines 976543–976546, in the
   documented wrapped form `R(ts(u,"gemini","SYSTEM_TEMPLATE.md"),"project","template")`).
   Bounded excerpt: `build/Kb82E11Loader_anchors_excerpt.txt`.
4. **Callee names rotated again.** 18.14.0's registration callees are `Ac`/`ts`;
   the round-72 pin's `Kl`/`Ho`/`bq` still grep 60× on this dump (minifier name
   reuse by unrelated functions) — evidence that name-allowlist extraction is
   dead on this binary and the round-52 callee-admission rule is what carries
   the extraction. The default path problem named in the plan stands: the
   tree's `DEFAULT_BINARIES["omp"]` is `~/.local/bin/omp.real`, which is
   absent; this probe measured the installed ELF directly.
5. **Literal census (gemini literals):** GEMINI.md 5 dump occurrences (2 on
   extracted call lines; the rest are display strings/doc text, e.g.
   `"Load GEMINI.md context files"`), SYSTEM_TEMPLATE.md 19 (2 call lines),
   system.md 23 (2 call lines).
6. **Documented boundary holds:** non-`.md` gemini registrations exist on this
   build — `Ac/ts(u,"gemini","settings.json")`, `Ac/ts(u,"gemini","extensions")`,
   `ts(u,"gemini","")` — and are correctly NOT extracted (they are the census's
   hand-declared excluded classes); the probe did not widen the set.

## False-match decoys (synthetic fixture, run embedded in probe)

All assertions true (`decoy_fixture` in the JSON report): prompt prose,
template lists, bare assignments, true 2-arg calls, unquoted file args,
non-`.md` files rejected; alias callee `q(u,"gemini","FAKE.md")` appears under
the raw rule but is dropped by callee admission; cross-module name conflict
resolves by the call's OWN module (`g`→`title` in one module, `g`→`gemini` in
another — no dump-wide laundering); function-parameter shadow
(`function q(e){…e…"GEMINI.md"}`) stays `<unresolved-var:e>`.

## Control worlds (read-only; explicitly authorized, not after-scores)

- **Parity:** base-tree (`git archive 47dbe87 verifiers corpus`) verifier's own
  `extract_classes(dump, "omp", declared=…)` on identical dump bytes ==
  probe's full pair set and gemini subset, exactly (exit 0;
  `build/Kb82E11Loader_parity.txt`).
- **Gate self-test** (base tree, fixtures only): `0 failure(s) over 218
  assertions`, exit 0 (`build/Kb82E11Loader_gate_selftest.txt`).
- **Loader checks on the live dump** (base tree, `--omp-strings` supplied dump,
  read-only): `surfaces.literal_present` PASS (39 loader-kind entries),
  `surfaces.no_uncovered_class` PASS (all 8 extracted loader classes declared),
  exit 0 (`build/Kb82E11Loader_gate_loaderchecks.json.txt`). Control-world
  measurement only; the C1 counter target (3/3, 7/7, 3/3) is L1's to land.

## Risks / notes for L1

- The 3,261 module markers mean module scoping is active on this dump; no
  single-scope fallback was triggered.
- groups `cursor` (rules) and `vscode` (mcp.json) documented as hand-declared
  excluded classes were not re-verified here (out of this seat's gemini scope);
  the full sweep found no other `.md` registration groups.
- No installs/upgrades performed (none needed). Pacman untouched. Disk guard
  was 47% used / 429G free at start. Contention: ≤2 processes, all runs ≤3s
  (strings dump 1.9s).

VERDICT: host omp 18.14.0 (sha256 e7dd2b60…5a8f, unchanged by measurement)
independently re-derives group gemini as exactly the 3 declared loader-group
pairs {GEMINI.md, SYSTEM_TEMPLATE.md, system.md}, anchored in
packages/coding-agent/src/discovery/gemini.ts (callees Ac/ts); extraction
identical to the base-tree verifier on identical dump bytes; decoy fixture
proves false-match discrimination. Observed absence of any additional gemini
pair + full 11-call pattern sweep is the bounded result; C1 counter landing
remains L1's integration step (no production after-value claimed by this seat).

DELIVERABLES:
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82E11Loader.md
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E11Loader_probe_gemini.py
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E11Loader_probe_gemini.json
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E11Loader_parity.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E11Loader_gate_selftest.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E11Loader_gate_loaderchecks.json.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E11Loader_gate_loaderchecks.stderr.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E11Loader_anchors_excerpt.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E11Loader.sha256.receipts.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/omp.sha256.before.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/omp.sha256.after.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/omp-18.14.0.strings.sha256.txt
