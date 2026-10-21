verdict: two tier-A own-work SOURCES rows drafted and shape-checked (S012 substrate snapshot, S013 C2 frontmatter gate), both queued; BASE c61a973b still has no XML-tag rule and the omp/opencode pins fail 3/3 against the frozen snapshot, so the rows record the gap rather than a pass.

# Scope

Own-work SOURCES rows for the round-47 C1 substrate re-census and the C2 checklist check. Drafts only: production `corpus/SOURCES.md` is untouched. The integrator appends the rows; the Search log and Gate entries required by contract rules 1 and 5 are also the integrator's.

Contract read: `/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md` (fleet root, read only). Shape: 11 cells between leading and trailing `|`, NF==13 under `awk -F'|'`, no `|` inside a cell, `kind=own-work`, `tier=A` for "the lane's own re-runnable gate output", `status=queued` until a knowledge entry cites the row.

# Draft rows

Provisional ids S012 and S013: BASE `corpus/SOURCES.md` registry ends at S011 (line 24). The integrator confirms the next unused ids at apply time.

```
| S012 | kotoba own work — `sha256sum -c SHA256SUMS` in /fast/scratch/kotoba-r47/shared (frozen omp 18.12.5 and opencode 1.19.3 snapshot) — run 2026-10-21, exit 0 | own-work | A | Identity of the substrate binaries the round-47 instruction-surface census measures | SHA256SUMS lines `bin/omp-18.12.5` fdbc8136… and `bin/opencode-1.19.3` 179ca421…; `omp --version` reports omp/18.12.5; live `command -v omp` sha256 equals the snapshot | A substrate pin is the binary's sha256, not its version string or path: pointed at the frozen snapshot, check_substrate_pins.py fails 3/3 (omp pinned 9513ef9f… vs fdbc8136…; opencode pinned d9123b9b… vs 179ca421…) and exits 2 at default resolution because the pinned opencode path is absent | queued | 2026-10-21 | on-release | — |
| S013 | kotoba own work — verifiers/verify_skill_checklist.py — --self-test exit 0 and --json on SKILL.md in a fleet-shaped scratch tree at BASE c61a973b, run 2026-10-21 | own-work | A | The lane's frontmatter gate has no XML-tag rule, so a tagged description passes it | Self-test final line "0 failure(s) over 1597 assertions"; --json trigger.frontmatter_parses PASS "description 814 chars"; SKILL.md:14 carries the `<skills>` token inside the frontmatter block (lines 1-16) | trigger.frontmatter_parses PASSes this lane's SKILL.md while its description still carries `<skills>`, so the Anthropic no-XML-tag rule (corpus/SOURCES.md S003) is unenforced until a description check lands; a tag-free fixture is the control that keeps the check honest | queued | 2026-10-21 | on-commit | — |
```

Patch of the drafts applied to a scratch copy of `corpus/SOURCES.md` (2 insertions after line 24): `.ufo/waves/round-47/build/SrcOwnWorkSubstrate.patch`.

Validation of the patched scratch copy (contract census commands, run in `/fast/scratch/kotoba-r47/SrcOwnWorkSubstrate/lane`):
- rows: 13 (was 11); malformed (NF!=13): 0; new rows NF=13 each, i.e. 11 cells each; duplicate ids: none; enum violations: none (exit 0).
- tier histogram: A=12, C=1. Status histogram: mined=4, queued=8, rejected=1.

# Evidence (commands, exit codes, key output)

BASE: `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD` → `c61a973b2e02e1ded169703ddcb06466f4edd8bd`.

Snapshot identity:
- `cd /fast/scratch/kotoba-r47/shared && sha256sum -c SHA256SUMS` → bin/omp-18.12.5 OK, bin/opencode-1.19.3 OK, both .strings OK; exit 0.
- `stat`: omp-18.12.5 mtime 2026-10-21 03:30:38 -0300 (matches plan/round-47.md:4-6); opencode-1.19.3 mtime 2026-10-20 18:33:42 -0300.
- `omp --version` → `omp/18.12.5`, exit 0. `command -v omp` → `/home/vgpnk/.local/bin/omp`, a regular file (readlink -f unchanged), sha256 `fdbc8136084c9a10439569157b2af62312e2b0d801cab54c73e89476da798e7e`, equal to the snapshot.
- `~/.local/bin/opencode`: 1460-byte Bourne-Again shell script (`file`), not the 1.19.3 ELF. Not executed (contract). `grep -c '1\.19\.3' opencode-1.19.3.strings` → 2; `opencode/1.19.3` present in the strings dump. Version read from the snapshot, not from running it.

Pins (`verifiers/baseline.json` and `verifiers/check_substrate_pins.py`, in the scratch clone at BASE):
- `baseline.json:5` omp_binary_sha256 `9513ef9f…`; `:6` omp_binary_mtime `2026-10-19T12:35:55.628149917-03:00`; `:7` omp_round21_note; `:8` omp_round44_note (re-pinned at omp/18.12.2); `:9` opencode_binary_sha256 `d9123b9b…`; `:11` round18_move (opencode replaced by v2.0.26, sha d9123b9b).
- `check_substrate_pins.py:63` opencode default path `/home/vgpnk/.opencode/bin/opencode`; `:73-75` pin kinds.
- `python3 -B verifiers/check_substrate_pins.py` (default) → exit 2: `ERROR UNREADABLE opencode_binary_sha256 … /home/vgpnk/.opencode/bin/opencode`; `DRIFT 3/3 pins failed`. Output: `.ufo/waves/round-47/build/SrcOwnWorkSubstrate.pins-snapshot.txt` covers the override run below.
- `python3 -B verifiers/check_substrate_pins.py --omp-binary <snapshot omp> --opencode-binary <snapshot opencode>` → exit 1: omp sha drift expect `9513ef9f…` got `fdbc8136…`; omp mtime drift (delta_ns=140082506863270); opencode sha drift expect `d9123b9b…` got `179ca421…`; `DRIFT 3/3`.

Checklist gate (BASE, in the scratch clone at c61a973b, under `/fast/scratch/kotoba-r47/SrcOwnWorkSubstrate/fleet/kotoba-shokunin` with `.ufo` and `PROTOCOL.md` symlinked from the fleet root, read only):
- `python3 -B verifiers/verify_skill_checklist.py --self-test` → final line `0 failure(s) over 1597 assertions`; exit 0 (run three times across the scratch trees, same result).
- `python3 -B verifiers/verify_skill_checklist.py --skill SKILL.md --json` → exit 1; 9 PASS / 1 FAIL: `checklist.box_map_complete` PASS 41 mapped (8 executed, 0 delegated, 33 unexecuted); `trigger.frontmatter_parses` PASS `name='kotoba-shokunin', description 814 chars`; the only FAIL `governance.citation_resolves` 805 evaluated, LOG.md:2111 `.ufo/round-45/drafts/v10/post-r44-hunt.py` does not resolve. This matches S010's recorded "9 PASS / 1 FAIL" exactly.
- `--check trigger.frontmatter_parses` → PASS (stdout captured; exit code not captured, so no exit claim).
- Frontmatter: `SKILL.md:1` and `:16` delimit the block; `sed -n '/^---$/,/^---$/p' SKILL.md | grep -c '<skills>'` → 1 (exit 0); the token is at `SKILL.md:14`. `SKILL.md:151` states the repair is planned for round 47 and "This file's own description still carries `<skills>`".
- XML rule absence: `grep -n -i 'xml' verifiers/verify_skill_checklist.py` returns only cmark references (`:1551`, `:1894`), no description/tag rule. The frontmatter contract is `:67-76` ("a structural parse, not semantic YAML validation"); `parse_frontmatter` at `:472`, `check_frontmatter` at `:1176` (checks presence and non-emptiness of name and description only).
- `LOG.md:2111` (BASE) is the governance citation the S010 row names; its runner path is absent, as the line itself records.

# Findings and counterexamples

1. The plan's "re-pin" framing needs a correction: the BASE opencode pin is `d9123b9b…` for opencode v2.0.26 (baseline.json:9, :11), not for 1.19.3. The frozen 1.19.3 snapshot (`179ca421…`) is a new pin, not a re-pin of an existing measured value. The S012 teaches cell states the drift as observed; it does not claim the pin is current.
2. The substrate pin guard fails closed at BASE in both modes: exit 2 at default resolution (absent opencode path), exit 1 against the snapshot (3/3 drift). A green S012 row therefore cannot be produced by the BASE tree; it requires the C1 re-pin that another seat owns. I did not run `verify_surfaces.py` (C1's gate) and did not re-pin anything.
3. Checklist location sensitivity (counterexample to S010's implicit reproducibility):
   - clone directory named `lane` → `trigger.name_directory` FAIL (`name 'kotoba-shokunin' != directory 'lane'`), JSON exit 1, 7 PASS / 3 FAIL.
   - clone directory named `kotoba-shokunin` without fleet parent → `trigger.citation_resolves` and `governance.citation_resolves` FAIL on `../.ufo/reports/...` (the reports dir is untracked in the production tree), 8 PASS / 2 FAIL.
   - the fleet-shaped tree (`../` resolves to a fleet root with `.ufo` and `PROTOCOL.md`) → 9 PASS / 1 FAIL, matching S010. S013 therefore names "fleet-shaped scratch tree" in its source cell rather than a bare clone.
4. S013 is a true-negative demonstration: the gate PASSes a description that still carries an XML-shaped token. The row records that as the gap; it is not a regression introduced by this round.
5. The S012 row's "fails 3/3" is a BASE observation, not a passing gate. If C1 re-pins before the integrator applies the row, the teaches cell must be rewritten (not appended) per contract rule 2.
6. Rule 1 (Gate entry) and rule 5 (Search log) are not drafted into the production file here. Suggested Search log bullet for the integrator: `2026-10-21 — own-work gate selection for round 47 substrate and checklist. Identified 2 candidates (snapshot sha256 check, verify_skill_checklist.py); screened 2; included 2; excluded 0. Stop rationale: the C1 and C2 claims rest on these two instruments.`

# Not checked

- Did not run `verify_surfaces.py`, `verify_harness_claims.py`, `verify_corpus_*`, or any C1/C3 gate (owned by other seats). No surfaces re-census.
- Did not execute either snapshot binary or the `~/.local/bin/opencode` wrapper; opencode version rests on `strings` and the sha256 match only.
- Did not verify the 2.0.26 claim in baseline.json:11 beyond reading it.
- Did not open any web source (own-work rows only); did not check `corpus/knowledge/` for citing entries (`used-by` = `—` for both rows).
- Did not re-check the SOURCES contract's full census in production; ran it on the patched scratch copy only.
- Did not confirm the live gate result in the production working tree (scratch reproduction only); production has untracked `?? .ufo/waves/` and `?? plans/round-47.md` (pre-existing, read-only observation).

# Tooling

No installs or upgrades. Tools used: `sha256sum`, `stat`, `awk`, `grep`, `git clone`/`checkout` (scratch only), `python3 -B`, `omp --version`.

# Artifacts (all under .ufo/waves/round-47/build/)

- `SrcOwnWorkSubstrate.md` (this report)
- `SrcOwnWorkSubstrate.patch` (3536 bytes; 2 added lines to `corpus/SOURCES.md`, from scratch `lane` clone)
- `SrcOwnWorkSubstrate.checklist-fleet.json` (fleet-shaped `--skill SKILL.md --json`, exit 1, 9 PASS / 1 FAIL)
- `SrcOwnWorkSubstrate.selftest.txt` (`--self-test` tail: `0 failure(s) over 1597 assertions`)
- `SrcOwnWorkSubstrate.pins-snapshot.txt` (`check_substrate_pins.py` against snapshot binaries, exit 1, DRIFT 3/3)
