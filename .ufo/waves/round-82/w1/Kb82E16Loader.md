# Kb82E16Loader — C1 independent extraction probe, harness group `opencode`

Seat: Kb82E16Loader (leaf, round-82 w1). Scope: independent extraction probe for
the **opencode** group of `verifiers/verify_surfaces.py`'s documented extraction
grammar against the **current host opencode ELF**. No production edit; probe +
receipts only. Base: `47dbe8781657de563ff867caca6244d28e3db504`.

## Assignment axes

- Freshness: is the pinned opencode extraction grammar still an accurate map of
  the live host substrate? (opencode half of C1; the omp 18.14.0 half is other seats.)
- Operability: does an independently coded probe reproduce the documented
  grammar's verdicts on the live dump and on the committed false-match decoys?

## Method

1. Scratch clone `--shared` at `/fast/scratch/hyaku/kotoba-r82/Kb82E16Loader/clone`,
   checked out at base `47dbe8781657de563ff867caca6244d28e3db504` (toplevel asserted
   before any command; no commits).
2. Read the documented grammar in `verifiers/verify_surfaces.py` (registration-call
   shapes with module-scoped variable resolution: `MODULE_MARKER_RE` spans,
   `ASSIGN_RE` constant tables with conflicting-rebind-drop, dump-wide table wins,
   `PARAM_HEADER_RE` param-shadow guard; the opencode OC-1..OC-6 rule set with its
   per-generation anchors).
3. Wrote a standalone probe `Kb82E16Loader-probe.py` (no import of
   verify_surfaces for the extraction itself) that: dumps the host ELF via
   `strings -n 4`; sha256s the binary before and after; runs the full generic
   call-shape sweep with module-scoped resolution; re-derives OC-1..OC-6 with
   per-rule anchor evidence; checks the census-removal ledger absent-anchors;
   diffs distinct extracted pairs/class ids against `verifiers/surfaces-baseline.json`
   **at base**; and runs the whole battery over all 40 committed `fixtures/surfaces/*.txt`
   worlds.
4. Cross-checked every probe verdict against the production module (read-only
   import of the base revision) on the same live dump and every fixture.

## Live-host result (evidence: `Kb82E16Loader-live.json`, `-live.stdout.txt`)

- Host binary `/home/vgpnk/.opencode/bin/opencode`: sha256
  `ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7`
  **before and after** the probe (byte-identical; the binary is untouched).
  This is the same sha256 the round-72 ledger records — the opencode substrate
  is unchanged since round 72.
- `strings -n 4` dump: 1,237,845 lines, sha256
  `020fb25393e5ce881ac2da70222acedebc5cef2d3810d07e4625b2cde885b089` —
  identical to the round-72 measured dump digest in
  `verifiers/census-removals.json`.
- **Call sweep (observed absence + full pattern sweep):** the documented
  registration-call shape `(callee)(<const>, <group|"group"|ident>, "<file>.md")`
  matched **0 call sites** on the live dump; distinct (group, file) pairs: **[]**;
  unresolved groups: **[]**. The historical opencode callee allowlist
  (Id/Cl/jDe/jDf/Tl/dr/GW) matched **0** call shapes either — the bare names do
  occur as ordinary minified callees (Id 11×, Cl 12×, Tl 35×, dr 66×, GW 4×,
  jDe/jDf 0×) but never in the registration shape, exactly the documented
  position ("opencode's loaders are list/join shapes governed by the OC-1..OC-6
  rules instead"). Module markers: 10 `// ….(ts|tsx|js…)` source-path scopes;
  581 `// @bun` separators.
- **OC rule extraction (probe, independent):** OC-1 ✓ (owns
  `opencode:instructions/AGENTS.md`), OC-2 ✓ (`opencode:config/AGENTS.md`),
  OC-3a ✓ (`opencode:config/instructions`), OC-3b ✓
  (`opencode:config/instructions-remote`), OC-4 ✓ (`opencode:read-hook/instructions`),
  OC-5 ✓ (shape witness, owns no id), OC-6 ✓ (`opencode:instruction-context/AGENTS.md`).
  Extracted ids = **6/6 declared-minus-excused**, missing 0, extra 0.
- **Ledger:** all 3 removal rows honoured (absent_anchors match nothing):
  `opencode:instructions/CONTEXT.md`, `opencode:instructions/CLAUDE.md`,
  `opencode:claude-home/CLAUDE.md`.
- **Distinct-pair diff vs `surfaces-baseline.json` at base:** declared opencode
  ids 9; excused 3; effective declared 6 = extracted 6; no extra, no missing.
  The (group, file) registration-pair set for opencode is empty on this lineage
  by construction of the grammar (valid absence result, sweep included).

Source anchors (all on the documented dump lines — `Kb82E16Loader-anchor-evidence.json`):
OC-1 target list `"AGENTS.md"` at dump line 708687 inside
`c("ConfigInstructionPlugin.projectSource")…up({targets:[…]})`; OC-2 `path` join
alias `Ip` (line 701606) joining `r.config` → `AGENTS.md` at line 708687 inside
the `id:"opencode.config.instruction"` + `globalSource` plugin region; OC-6
classes `p2`/`WT`/`fI`/`JT` at lines 708288/708288/708294/708343 with the
SessionContext deps composition `['VT','yP','DA','Sue','M6',…]`; OC-4 service
`sl extends U()("@opencode/SessionInstructions")` and read plugin
`{id:"opencode.tool.read",…}` at lines 708687/708708 within one `// @bun` module
starting at line 708530.

## Cross-check against production and the transcription defect

The first probe run disagreed with production on OC-6 only. Diagnosis
(`Kb82E16Loader-transcription-defect.stdout.txt`): all 13 OC-6 regex patterns
compared byte-identical except one invisible difference — my probe had
transcribed the builtins class constant as `@opencode/InstructionBuiltins`
(lowercase "ins") while the grammar pins `@opencode/InstructionBuiltIns`
(byte 125: `I` vs `i`). The live binary genuinely ships
`class fI extends U()("@opencode/InstructionBuiltIns")` (line 708294). After
aligning the constant to the documented grammar, the probe agrees with the
production `extract_opencode_classes` on the live dump **and on all 40 fixture
worlds, 0 mismatches** (`Kb82E16Loader-battery-crosscheck.json`,
`Kb82E16Loader-production-live.stdout.txt`). The defect was probe-side, not a
host divergence — recorded here as the probe's own Mistakes-table entry.

## False-match decoy verdicts (battery of 40 committed fixture worlds)

- v2.1.4 OC-4 decoys (walk/render/target/load/publish): all extract **nothing** —
  each broken conjunct fails the rule; the clean `strings-opencode-v2.1.4-oc4.txt`
  anchor extracts exactly `opencode:read-hook/instructions`.
- OC-2 decoy-moved (join outside the plugin region): extracts nothing; anchor
  extracts exactly `opencode:config/AGENTS.md`.
- `strings-opencode-v2.1.4-decoy.txt` (skills plugin carrying the same config
  join tokens): extracts only OC-1's `opencode:instructions/AGENTS.md` — the
  plugin-region binding works as documented.
- 1.19.x OC-4/OC-6 decoys (oc4, oc4-delivery, oc6, oc6-target): the targeted
  rule fails while the rest of that generation's witness still extracts; the
  1.19.4 anchors fixture extracts all 9 1.19.x ids.
- `strings-opencode-v2.0.26.txt` (retired lineage): extracts nothing — the
  must-fail generation stays dead.
- planted-name: derives `opencode:instructions/GUIDE.md` identically to
  production (a genuine derivation of a planted loader name, not a false match);
  drop-oc1..oc6 each drop exactly their rule's ids; extra adds nothing beyond
  the 1.19.x set; all omp fixtures (`strings-omp-*.txt`) extract **0 opencode
  ids** under the OC rules, and the omp pairs the generic sweep sees (e.g.
  `(opencode, AGENTS.md)` from the omp bundle) are never admitted as opencode
  harness classes by the documented two-way parity.

## Findings for L1

1. The opencode half of the C1 substrate is **fresh and pin-consistent at base**:
   live binary and dump byte-identical to the round-72 measurements, extraction
   grammar reproduces 6/6 declared-minus-excused ids with 0 extra, ledger 3/3
   honoured. No opencode-side re-pin is required by this probe.
2. Independent-derivation value: the probe caught its own one-byte constant
   transcription error (`InstructionBuiltIns`) that a looser re-derivation would
   have shipped as a false "host drift" claim — cross-checking against the
   production module on the same dump is what separated the two; the documented
   anchors are exact.
3. The documented "observed absence" position for opencode registration calls is
   confirmed by the full sweep with module-scoped resolution: 0 call sites, 0
   distinct pairs, 0 unresolved groups.

## Risks / blockers

- None blocking. The probe is bounded read-only analysis; no production file,
  sibling, lane git/jj state, or host binary was modified (binary sha256
  before == after; only `strings` read it).
- No tool installs or upgrades were needed (nothing recorded).
- Scratch clone and dumps deleted after receipt copy (see DELIVERABLES); the
  live-dump text itself was not retained (its sha256 and all extracted anchors
  are in the receipts).

VERDICT: opencode group extraction independently reproduced — live host binary
sha256 ca9b3ee2…d2e7 unchanged before/after, dump sha256 020fb253…85b089 matches
round-72 pin, OC-1..OC-6 all match with 6/6 declared-minus-excused ids, 0 extra,
removal ledger 3/3 honoured, registration-call sweep 0 sites (documented
absence), 40/40 fixture worlds incl. all false-match decoys agree with
production, probe-side one-byte transcription defect found and fixed (no host
divergence).

DELIVERABLES:
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82E16Loader.md
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E16Loader-probe.py
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E16Loader-live.json
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E16Loader-live.stdout.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E16Loader-battery-crosscheck.json
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E16Loader-anchor-evidence.json
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E16Loader-host-opencode-sha256.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E16Loader-production-live.stdout.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E16Loader-transcription-defect.stdout.txt
