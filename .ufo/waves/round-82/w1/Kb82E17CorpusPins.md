# Kb82E17CorpusPins — round-82 C1 host-loader re-pin: census + ledger anchor recompute

Seat: Kb82E17CorpusPins (leaf; no subagent dispatch, no background jobs, no installs)
Base: `47dbe8781657de563ff867caca6244d28e3db504`; counter frozen base `c69711ee08279609374d895bb0f3c8c18ccf15c9`
Scratch clone: `/fast/scratch/hyaku/kotoba-r82/Kb82E17CorpusPins/clone` (`--shared`, checkout 47dbe87, toplevel asserted before any git call)
Full evidence: `.ufo/waves/round-82/build/Kb82E17CorpusPins-census-ledger-evidence.txt`

## Assignment executed

1. **Unchanged base class census recomputed from committed bytes.** `git show <rev>:verifiers/surfaces-baseline.json` at both the frozen r72 base and the r82 base gives byte-identical files (sha256 `6b23c3d1…` both). The 9 `harness == "opencode"` classes are set-identical and signature-identical (literal, context_kind, verdict) across the round range. The census baseline is unchanged — nothing to re-ledger.

2. **Three removal-ledger anchors recomputed from committed bytes.** `verifiers/census-removals.json` at base (sha256 `c8944913…`) names exactly the frozen set `opencode:instructions/CONTEXT.md`, `opencode:instructions/CLAUDE.md`, `opencode:claude-home/CLAUDE.md`, and every `absent_anchors` entry is string-equal to the counter's `FROZEN_REMOVALS` (check_substrate_repin_v2.py:139-149). Ledger conjunct shape is exactly as frozen by errata E1.

3. **Live host opencode strings compared.** `strings -n 4 /home/vgpnk/.opencode/bin/opencode` (exit 0, 1,237,844 lines) hashes to `020fb25393e5…`, identical to the ledger's recorded `dump_sha256` — the live dump is byte-identical to the round-72 measurement. All four frozen anchors match **nothing** in the live dump; the three removed classes remain absent (no drift, no silent deletion — kept set is 9/9, no extras, no unkept). Literal counts: CONTEXT.md 0, disableClaudeCodePrompt 0, CLAUDE.md 3 (prose/string-table only, per the ledger's stated reason), AGENTS.md 15.

4. **Frozen counter run at base with direct exit — expected unevaluable, recorded as such.** `python3 -B verifiers/check_substrate_repin_v2.py --repo <clone> --rev 47dbe87…` exits **2**: `cannot evaluate: verify_surfaces.py reported 0 row(s) (exit_code 2: omp binary not found: /home/vgpnk/.local/bin/omp.real); pins 1/3 row(s) PASS, surfaces 0/0 check(s) PASS`. This reproduces `receipts/before-c1-counter.txt` exactly. The base tree's instruments default `omp` to the absent `omp.real` (check_substrate_pins.py:68, verify_surfaces.py:169), so the surfaces instrument reports zero rows and the counter's empty-report guard returns exit 2 rather than a fake `0 of 7`. Unevaluable ≠ zero; the pins conjunct still measures opencode PASS 1/3.

5. **omp-update/opencode-behavior detection: NO change.** The opencode binary sha256 (`ca9b3ee2…`) and dump sha256 (`020fb253…`) are both unchanged vs the round-72 pins — the omp 18.14.0 install (new Bun-compiled ELF, sha256 `e7dd2b60…`, `omp --version` = `omp/18.14.0`, mtime 2026-10-29 23:19:46 -0300) did not touch the opencode substrate. The new omp's opencode mentions (178 lines) are provider/registry integration only (chunks `opencode-*.js`, `opencode-go`/`opencode-zen` cases, `commands.enableOpencode*`, `~/.config/opencode/AGENTS.md`); `grep '\.opencode/bin'` over omp's 2,546,730 strings finds **0** references — omp cannot reach the opencode binary's loader. Census literals inside the new omp: CONTEXT.md 0, disableClaudeCodePrompt 0, CLAUDE.md 18, AGENTS.md 41 — omp carries its own CLAUDE.md/AGENTS.md loader strings (e.g. `var IQ = "CLAUDE.md"`, `Fr.join(k, "CLAUDE.md")`, `for (const s of ["AGENTS.md", "CLAUDE.md"])`), which is re-derivation material for the C1 omp half, not an opencode-dump change.

## Consequences for C1

- The opencode half of C1 needs **no** re-pin: opencode bytes and dump are byte-identical to the frozen pins; the removal ledger and class census remain exactly valid against the live dump.
- The omp half is where the substrate moved: `omp.real` is gone and the installed ELF is now `~/.local/bin/omp` 18.14.0 (`e7dd2b60…`). Its loader-group calls and instruction literals (its own AGENTS.md/CLAUDE.md surfaces, listed above) are what a re-pin must re-derive; the unchanged counter's base-tree defaults still point at `omp.real`, which is precisely why the base remains exit-2 unevaluable until defaults/pins move.
- No baseline changes made; no production files touched; no commits.

VERDICT: Base census unchanged (9/9 opencode classes byte-identical r72→r82 base); the three ledger anchors recompute exactly from committed bytes and all remain absent from the live opencode dump (dump sha256 identical to the recorded round-72 dump); the frozen counter at base rev exits 2 with the expected "cannot evaluate" (empty surfaces instrument, not a measured 0/7), reproducing the before receipt; the omp 18.14.0 update did NOT change opencode behavior (opencode binary and dump byte-identical, no `.opencode/bin` reference in omp). No baseline changes; no 6/6 tip-battery claim.

DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82E17CorpusPins.md ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E17CorpusPins-census-ledger-evidence.txt
