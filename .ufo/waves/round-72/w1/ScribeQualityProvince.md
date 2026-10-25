# ScribeQualityProvince — round 72 wave 1 report

**Verdict:** the three draft blocks are complete and grounded — PROVINCE.md § Core bullet (round 72), corpus/README.md § Frontier note (round 72), and the SHONEN evidence-line pointers. Deliverables: `.ufo/waves/round-72/w1/build/ScribeQualityProvince/blocks.md` (40 lines all told). No lane file was edited; no tool installed (none needed; pacman untouched). All counts below were observed by me this session; the C1/C2/C3 result values in the drafts are `<<…>>` placeholders by instruction (wave-2 data not yet produced).

## Findings (command → observed)

1. **Base SKILL.md measure.** `git -C …/kotoba-shokunin cat-file -s c69711ee08279609374d895bb0f3c8c18ccf15c9:SKILL.md` → `72688`; `git -C … show c69711e…:SKILL.md | wc -l` → `600`. Matches `.ufo/waves/round-72/receipts/base-battery.txt:41` (`SKILL.md lines: 600  bytes: 72688`).

2. **Base battery receipt (C3 control).** Read `receipts/base-battery.txt`; the six C3 gates: `check_gate_registry` exit 1 (`:13`), `check_assertion_floors` 1 (`:7`), `verify_skill_checklist` 0 (`:39`), `verify_corpus_integrity` 1 (`:36`), `verify_corpus_independent` 1 (`:35`), `check_correction_sweep` 0 (`:10`) → `2 of 6` at base, matching the frozen do-nothing control.

3. **omp host identity (C2 omp half).** `sha256sum ~/.local/bin/omp ~/.local/bin/omp.real` → `ed62a41e…` vs `85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4`; `stat` → wrapper 1,680 B, mtime `2026-10-23 20:47:22.557636701 -0300`, real binary 256,702,432 B, mtime `2026-10-21 20:37:24.615549837 -0300`. Read `~/.local/bin/omp` (Bourne: `#!/usr/bin/env bash`, "crash-restart wrapper (installed 2026-10-23…", `BIN="${OMP_REAL:-$HOME/.local/bin/omp.real}"`). `verifiers/baseline.json` pins `omp_binary_sha256 85d9daf3…` and `omp_binary_mtime 2026-10-21T20:37:24.615549837-03:00` — byte-exact equal to `omp.real`, not to the wrapper. So the omp drift is path-only (wrapper in front of the pinned binary).

4. **opencode lineage (C2 opencode half).** `grep -c '2\.1\.4' /tmp/k72-oc-strings.txt` → `1`; contexts include `opencode/latest/2.1.4/cli --use-system-ca…` and `var ca="2.1.4",eA="latest"…`; `grep -c '1\.19\.4'` → `0`. `grep 'CONTEXT\.md' /tmp/k72-oc-strings.txt` → `No matches found` (literal `CONTEXT.md` absent). `grep -c 'AGENTS\.md'` → 13, `'CLAUDE\.md'` → 3. Host binary `~/.opencode/bin/opencode` reported by verify_surfaces as sha256 `ca9b3ee2…` (matches the frozen plan's host fact).

5. **Substrate pins at base (own re-run).** `python3 -B verifiers/check_substrate_pins.py --json` → omp `sha256` DRIFT (observed `ed62a41e…`), omp `mtime` DRIFT, opencode npm path `…/.npm/_npx/e2094862…/opencode.exe` missing → pins 0/3.

6. **r53 re-pin counter at base (own re-run).** `python3 -B verifiers/check_opencode_repin.py --rev c69711e…` → `opencode re-pin: surfaces pass 0 of 7 (opencode_extract ABSENT); pins OK 0/3; opencode classes kept 9 of 9`.

7. **Surfaces with explicit host binaries (own re-run, 18 s).** `python3 -B verifiers/verify_surfaces.py --json --omp-binary ~/.local/bin/omp.real --opencode-binary ~/.opencode/bin/opencode` → `pass 5, fail 2, exit_code 1`. Failing ids: `surfaces.literal_present` — `1 loader literal(s) not verifiable: opencode:instructions/CONTEXT.md (literal 'CONTEXT.md' absent from opencode dump)`; `surfaces.opencode_extract` — `vacuity: extraction produced 0 class(es) from 7 rule(s)…` with OC-1…OC-6 matching nothing. This is the exact pre-re-pin state the C2 predicate targets.

8. **C1 entry grounding (own re-open).** `grep 'S123|S129' corpus/knowledge/instruction-authority-ladder-round67.md` → source rows `S123`/`S129` present (`:1,3`); `S198|S199|S200|S201|S202|S208` in `client-trust-gates-round68.md` → all six present (`:1-6`); `S203…S207` in `skill-name-precedence-round69.md` → all five present (`:1-5`). Files exist at base (glob).

9. **New counters absent at base.** glob of `verifiers/check_author_rules.py`, `check_substrate_repin_v2.py`, `check_tip_battery.py` → `Path not found` — the named counters are wave-1/2 build deliverables, so the bullets name them as the to-land instruments.

10. **Gate-registry block size (lead anchor).** `## Gate registry` begins at `SKILL.md:464`; next `## ` heading is `## Sources` at `:524`; verifier-prefixed rows: 49 (awk count); table bodies 17,393 B; whole section 17,849 B. The considerthese 2026-10-25 proposal 2 quoted 16,025 B at its earlier read — the lead says “~17 KB (~24%) at base”, measured.

11. **Province guard shape.** `verifiers/check_province_core.py` docstring (`:2-33`): reads `province core rows 2 of 2`; an area is held when one § Core bullet names entry (repo path) + counter (repo path) + round, and the entry has a coverage-map row in `corpus/README.md`; no-harm conjunct: PROVINCE `## Frontier`/`## Adjacent` byte-identical to base. SHONEN box-4 pointer cites this guard at the new tip.

## Confidence / limits
- All facts itemized above are observed (commands listed). The only plan-sourced numbers I did not re-derive are the two `verify_skill_checklist`/`check_correction_sweep` exits (receipt read, not re-run) and the snapshot hashes for A4 (wave-2); the draft blocks carry `<<…>>` placeholders there.
- No credential material, session URLs or `op://` references.
- Report trailer relative to lane root: `.ufo/waves/round-72/w1/ScribeQualityProvince.md`; drafts at `.ufo/waves/round-72/w1/build/ScribeQualityProvince/blocks.md`.
