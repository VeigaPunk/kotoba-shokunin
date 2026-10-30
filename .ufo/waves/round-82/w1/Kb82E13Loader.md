# Kb82E13Loader — round-82 C1 independent loader-group extraction probe

Seat: Kb82E13Loader (leaf). Scope: C1 freshness support — an INDEPENDENT
extraction probe for the omp loader-group cursor on the CURRENT host binary
(omp 18.14.0). No production files mutated; no seat commits; patch-only
deliverables under the named build paths.

## Base and inputs

- Base: `47dbe8781657de563ff867caca6244d28e3db504` (scratch `--shared` clone,
  toplevel asserted: `/fast/scratch/hyaku/kotoba-r82/Kb82E13Loader/clone`).
- Documented grammar source: `verifiers/verify_surfaces.py` (base tree) —
  the round-52 callee-rename-robust declared-admission rule
  (`OMP_GENERIC_CALL_RE`), round-51 module scopes (`MODULE_MARKER_RE`,
  `scope_table`), round-51 param-shadow guard (`PARAM_HEADER_RE`),
  `ASSIGN_RE` constant tables, and the admission rule (a callee is admitted
  when one of its call sites registers a baseline-declared `loader-group`
  pair; all pairs of admitted callees are extracted).
- Host binary: `/home/vgpnk/.local/bin/omp` (ELF, 276244656 bytes,
  sha256 `e7dd2b606c4ebe9d1a7bcfad1b8820db968cd6b05409fed1c6bc8db0b6a95a8f`,
  mtime epoch 1793326786 = 2026-10-29 23:19:46 -0300, `omp --version` ->
  `omp/18.14.0`). `omp.real` ABSENT (as the before-pins receipt records).
- Dump: `strings -n 4` (GNU binutils 2.47), 2546730 lines / 47434077 bytes,
  dump sha256 `81277d3572277febcaf0853f10cf8778c64920f58a13fba98ef0accbb70a8319`.

## Probe

`build/Kb82E13Loader-probe.py` re-implements the documented grammar from
scratch (imports nothing from the verifier), runs it over the dump, and
reports: declared pairs, admitted extraction, full no-filter shape sweep,
allowlist-mode (historical callee names) arm, per-pair source anchors, and
synthetic decoy guards. Run: exit 0.

## Findings

1. **Extraction parity, both directions empty.** All 8 baseline omp
   `loader-group` pairs (at base) are extracted from the 18.14.0 dump, and
   nothing else is:
   `(agents-md,AGENTS.md) (claude-md,CLAUDE.md) (gemini,GEMINI.md)
   (gemini,SYSTEM_TEMPLATE.md) (gemini,system.md)
   (github,copilot-instructions.md) (opencode,AGENTS.md)
   (windsurf,memories/global_rules.md)`.
   `distinct.in_extracted_not_baseline = []`,
   `distinct.in_baseline_not_extracted = []`.
2. **Full pattern sweep == admitted set.** 11 call-shape matches total
   (callees Ac ×5, F9 ×2, ts ×4); 8 distinct pairs; the no-admission-filter
   sweep produces exactly the same 8 pairs — no undeclared registration call
   exists anywhere in the dump. Observed absence is not in play for the group
   cursor: the group EXISTS on this binary.
3. **Callee re-pin required for any allowlist consumer.** Admitted callees
   are `Ac`, `F9`, `ts` — all NEW minified names. Every historical allowlist
   name (Id/Cl/jDe/jDf/Tl/dr/GW/Co/Dl/Hj/I5/Gl/Mo/lq/Xl/Fo/Kl/Ho/bq,
   rounds 18–72) matches 0 call sites (`allowlist_mode_pairs: []`). The live
   declared-admission rule is callee-rename-robust and unaffected.
4. **Module-scoped resolution.** Two group idents resolve through bindings:
   `nD = "agents-md"` (dump line 972667, module marker line 972666
   `// packages/coding-agent/src/discovery/agents-md.ts`) and
   `rD = "claude-md"` (line 972678, marker 972677
   `// packages/coding-agent/src/discovery/claude-md.ts`). Six groups are
   quoted literals. Zero `<unresolved-var:...>` groups.
5. **Source anchors** (dump lines, callee, module) for every pair are in the
   probe report `anchors` map, e.g. `(gemini,GEMINI.md)` at lines 976407/976418
   in `// packages/coding-agent/src/discovery/gemini.ts` (callees Ac and ts).
6. **Decoys reproduce documented semantics.** Alias decoy `q(u,"evil","EVIL.md")`
   is shape-detected but never admitted; a group ident that is an enclosing
   function parameter stays unresolved (shadow guard fires); a name bound in
   two modules resolves in the call's own module (own-scope value wins over
   the dump-wide table); quoted groups are taken literally; wrong-arity,
   unquoted-file, trailing-space and empty-arg shapes do not match at all.
7. **Binary unchanged by this seat.** sha256 before == after
   (`e7dd2b60…95a8f`), mtime/size identical; the probe is read-only.

## Production-gate cross-check (read-only, explicit flags)

Base-tree `verify_surfaces.py --repo . --omp-strings <dump>
--opencode-strings <dump> --check surfaces.literal_present
--check surfaces.no_uncovered_class --json` -> exit 0:
`PASS surfaces.literal_present (39 loader-kind entries verified)`;
`PASS surfaces.no_uncovered_class (all 8 extracted loader class(es)
declared)`. The frozen gate's own code agrees with the independent probe on
the loader cursor. (The opencode dump slot was fed the same dump for this
loader-only cross-check; the opencode rule arm belongs to other seats.)

## Boundaries / non-claims

- This is an extraction-grammar parity probe, not a runtime-discovery or
  prompt-effectiveness claim.
- `loader-literal` / `loader-config` kinds and the opencode rule set are out
  of this seat's scope (cross-check arm only).
- Pin JSON / defaults / census updates are L1 integration work; this seat
  returns probe + receipts only.
- Existing reds (before-pins 1 PASS + 2 UNREADABLE exit 2; before-counter
  cannot-evaluate exit 2) remain named reds; nothing here scores an after-value.

## Receipts / artifacts

- `.ufo/waves/round-82/build/Kb82E13Loader-probe.py`
  sha256 `55d861a95e4bb81a11251dd581b9503f218fbf2e35b60cf4dfc384bfddda46de`
- `.ufo/waves/round-82/build/Kb82E13Loader-probe-report.json`
  sha256 `ffe9b28eff52c3413dd0abd3decb900f649e1b8edab7b13df50d765f54361a58`
- `.ufo/waves/round-82/build/Kb82E13Loader-crosscheck-surfaces.json`
  sha256 `4e2357e6c310af8f561823fae6fc11ecb071f342aa310af7600a0b14d038cdbd`
- `.ufo/waves/round-82/build/Kb82E13Loader-receipts.txt` (command-owned exits,
  exact outputs, before/after hashes; tool installs this seat: NONE)
- Tool versions: GNU strings 2.47, Python 3.14.8 (pre-existing; pacman paused).

VERDICT: independent probe on current host omp 18.14.0 reproduces the 8/8
baseline loader-group pairs exactly (distinct both ways empty, sweep ==
admitted, 0 unresolved); admitted callees are newly minified Ac/F9/ts with
all historical allowlist names absent; binary sha256 unchanged; production
gate cross-check passes the two loader checks on the same dump.

DELIVERABLES:
/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82E13Loader.md
/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E13Loader-probe.py
/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E13Loader-probe-report.json
/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E13Loader-crosscheck-surfaces.json
/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E13Loader-receipts.txt
