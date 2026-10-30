# Kb82M01Loader — round 82 C1 loader re-derivation and mutation test

Seat: Kb82M01Loader (leaf member, no subagent dispatch). Base `47dbe8781657de563ff867caca6244d28e3db504`.
Axes judged: freshness, operability. Milestone: C1 freshness host loader re-pin.

Scope note: this is scratch-candidate evidence only. No production file, corpus, SKILL, verifier, plan or lane git/jj state was changed. The candidate commit `6f9e6d9443118b25ad07341f80b335b63c3cf92d` lived only in the seat scratch clone, which is now deleted; the candidate is preserved as a patch (below). No freeze receipt exists in this seat, so nothing here is a production after-value.

## 1. Host loader re-derivation (S251 input)

| item | value | source |
|---|---|---|
| path | `/home/vgpnk/.local/bin/omp` (ELF, dynamically linked, not a wrapper) | `file`, stat, 2026-10-30 |
| `omp.real` | absent (`ls: cannot access`) | `ls -la`, 2026-10-30 |
| size | 276244656 bytes | `stat -c %s` |
| mtime | 2026-10-29 23:19:46.168359786 -0300 (epoch ns 1793326786168359786) | `stat`; pins script observed value |
| sha256 | `e7dd2b606c4ebe9d1a7bcfad1b8820db968cd6b05409fed1c6bc8db0b6a95a8f` | `sha256sum` |
| version | 18.14.0 (`var A0 = "18.14.0"` in `strings -n 4` dump) | strings dump, sha256 `81277d3572277febcaf0853f10cf8778c64920f58a13fba98ef0accbb70a8319` (2,546,730 lines) |

Loader-group registration calls on the 18.14.0 bytes (regex over the dump, then the verifier's own `extract_classes`):

- 11 raw call shapes; the 8 declared omp loader-group pairs are all extracted.
- Callees changed: `F9` (agents-md/AGENTS.md via `nD`, claude-md/CLAUDE.md via `rD`), `Ac` (gemini GEMINI.md, system.md, SYSTEM_TEMPLATE.md; opencode AGENTS.md; windsurf memories/global_rules.md), `ts` (gemini x2 via `ts`; github copilot-instructions.md). Previous lineage was `lq/Xl/Fo` (18.12.5) and `Kl/Ho/bq` (18.12.6).
- Because the omp extractor is callee-rename-robust (`OMP_GENERIC_CALL_RE`, round 52), a callee change alone does not require a code or baseline change.

Measured on the unchanged base (host bytes, read-only instruments):

- `verify_surfaces.py --json --omp-binary ~/.local/bin/omp --opencode-binary ~/.opencode/bin/opencode`: exit 0, `pass 7 fail 0`. Receipt `Kb82M01Loader-surf_host_base.json`.
- `check_substrate_pins.py --json` (same binaries): exit 1, `pins 1/3`. omp sha DRIFT (expect 85d9…, observed e7dd…), omp mtime DRIFT; opencode PASS. Receipt `Kb82M01Loader-pins_host_base.json`.
- `verify_surfaces.py` with the base default `omp.real`: exit 2 (`omp binary not found`). Matches the round-82 before-state.

## 2. Candidate patch (scratch only)

Changed files (3 files, +11/-12; `Kb82M01Loader-candidate.patch`, sha256 `982f5469cf99d82dcf7734ee75437513b317eae6900da6bece6a250f3d6fb57e`):

1. `verifiers/verify_surfaces.py` `DEFAULT_BINARIES["omp"]` → `/home/vgpnk/.local/bin/omp`.
2. `verifiers/check_substrate_pins.py` `BINARIES["omp"]` → `/home/vgpnk/.local/bin/omp`.
3. `verifiers/baseline.json` `measured_against`: `omp_binary_sha256` → `e7dd2b…`; `omp_binary_mtime` → `2026-10-29T23:19:46.168359786-03:00`; new `omp_round82_note`. The opencode pin is unchanged.

Not changed, deliberately:

- `verifiers/surfaces-baseline.json` and `corpus/knowledge/instruction-surface-census-round13.md`: the surfaces gate is green on unchanged declarations. No census class was added or removed.
- `verifiers/census-removals.json` and `FROZEN_REMOVALS`: opencode-only ledger; unchanged.
- `verifiers/check_substrate_repin_v2.py`: frozen counter; bytes untouched.
- `OMP_CALL_RE` / `OMP_CALLEE_NAMES_ROUND50` comments: historical allowlist, still not updated for `F9/Ac/ts` (documentation drift only; the generic extractor does not read it in declared mode).

Frozen counter on the candidate (scratch rev `6f9e6d94…`, `--repo` = scratch clone), receipts `Kb82M01Loader-counter_cand.{out,err}`:

    exit 0
    host substrate re-derived: pins OK 3/3; surfaces pass 7 of 7; removal ledger 3 of 3 verified
    substrate opencode: /home/vgpnk/.opencode/bin/opencode sha256 ca9b3ee2… bytes 240416944 strings 1237844

Frozen counter on base `47dbe878…` (before control), receipt `Kb82M01Loader-counter_base.{out,err}`: exit 2, `cannot evaluate: ... omp.real; pins 1/3 PASS, surfaces 0/0`. Matches the round-82 before-state.

## 3. Mutation test of the candidate

Each mutant is one commit on top of the candidate in the scratch clone; the frozen counter runs twice on the mutant revision, then the clone is hard-reset to the candidate. Stability is byte equality of stdout and stderr across the two runs. Patches: `Kb82M01Loader-mut_<name>.patch`; outputs: `Kb82M01Loader-mut_<name>.run{1,2}.{out,err}`; runner: `Kb82M01Loader-run_mutant.sh`.

| mutant | class | edit | counter exit | finding (stderr, run 1) | stable | verdict |
|---|---|---|---|---|---|---|
| M1 | wrong path | both omp defaults → `omp.real` | 2 | `cannot evaluate: ... omp binary not found: /home/vgpnk/.local/bin/omp.real; pins 1/3` | yes | RED |
| M1b | wrong path/binary | pins omp default → `~/.opencode/bin/opencode` | 1 | `FAIL pins: 1 of 3 row(s) hold` | yes | RED |
| M2 | wrong group binding (first draft) | baseline class `omp:claude-md/CLAUDE.md` → `omp:claude-dir/CLAUDE.md` | 2 | `cannot evaluate ... exit_code 3: classes[17]: duplicate class_id 'omp:claude-dir/CLAUDE.md'` | yes | RED (guard; id collided with an existing row, so not a clean binding test) |
| M2b | wrong group binding | baseline class → `omp:claude-group/CLAUDE.md` (non-colliding) | 1 | `FAIL surfaces: 4 of 7 check(s) PASS` | yes | RED |
| M3 | stale pin (sha) | `omp_binary_sha256` → `85d9daf3…` (18.12.6) | 1 | `FAIL pins: 2 of 3 row(s) hold` | yes | RED |
| M3b | stale pin (mtime) | `omp_binary_mtime` → `2026-10-21T20:37:24.615549837-03:00` | 1 | `FAIL pins: 2 of 3 row(s) hold` | yes | RED |
| M4 | removed class | baseline row `omp:gemini/system.md` cut (not ledgered; the ledger is opencode-only) | 1 | `FAIL surfaces: 5 of 7 check(s) PASS` | yes | RED |
| M5 | removed pin | `omp_binary_sha256` key cut | 1 | `FAIL pins: 2 of 3 row(s) hold` (PIN_ABSENT) | yes | RED |
| R1 | rename-equivalent | callee call sites `F9→Qzk1`, `Ac→Vnk2`, `ts→Wqk3` in a copy of the 18.14.0 dump (call-site only; 8/28/57 sites; sha256 of renamed dump `4ce3d5b2…`) | — | `verify_surfaces` exit 0, `pass 7 fail 0`; extracted pairs identical to the original (8 declared, `equal True`) | yes | GREEN (honest) |
| R1-ctl | control, original dump | same `verify_surfaces` on unrenamed dump | — | exit 0, `pass 7 fail 0` | — | GREEN (control) |

Each red mutant fails at the conjunct it targets. The counter's other conjuncts stay as they were; for example, M4 keeps the removal ledger at `3 of 3`. Red by construction, not by a shared failure.

The rename-equivalent is green only because the extractor is callee-rename-robust (round 52), and the extraction-equality check proves the same (group, file) set. The rename is on call sites only (`name(` not preceded by an identifier character, `.` or quote). Definitions and non-call references are not renamed; the extractor reads call shapes only, so this is the honest scope. A binary-level rename is not possible on the live host.

## 4. Findings and residuals

- C1 candidate: the frozen counter returns the target line and exit 0 on the scratch candidate. This is one measurement on one revision, not a production after-value, not a shortcut-world result (other seats own those), and not a score.
- The only substrate changes needed for 18.14.0 are the omp default path and the omp pins. The loader-group extraction and the surfaces baseline needed no change.
- Residual defaults outside the counter predicate, still pointing at `omp.real`: `verifiers/verify_harness_claims.py:53` (`OMP_BIN`, plus its `~/.local/bin/omp` docstring line 14) and `verifiers/verify_harness_independent.py:124` (`DEFAULT_OMP_BINARY`). They are not read by `check_substrate_repin_v2.py`. Moving them is a separate change for the owning lane; not done here.
- `verify_harness_claims.py` executes the binary; it was not run by this seat.
- Counter docstring line 13 and `check_substrate_pins.py` docstring line 41 still mention `omp.real`; the counter is frozen, so this stays.
- No omp census-removal mechanism exists: M4 shows that a removed omp class fails loud, which is the intended behaviour. Any future omp removal needs a new ledger, not a silent cut.
- Install/update record: none. No tool was installed or upgraded. No pacman transaction, service restart, or privilege change.

## 5. Mistakes

| # | mistake | effect | disposition |
|---|---|---|---|
| 1 | First rename of F9/Ac/ts was word-bounded and renamed string/prose tokens (231/136/504 sites) | would have over-stated the rename | discarded; replaced with call-site-only rename and extraction-equality proof |
| 2 | M2 used `omp:claude-dir/CLAUDE.md`, which already exists in the baseline | red by duplicate-id guard, not by binding | kept as a labelled finding; M2b added as the clean binding mutant |
| 3 | Edit-tool first attempt used the wrong range (163-169 instead of 163-171) | rejected by the tool; nothing written | re-issued with correct range; no partial state |

Process: all tool calls checked toplevel before mutation; no git writes outside the scratch clone; no fleet-root tracked file written; scratch removed after receipts were copied.

## 6. Receipts

Build directory `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/`, prefix `Kb82M01Loader-`, all sha256-listed in `Kb82M01Loader-SHA256SUMS.txt`:

- `Kb82M01Loader-candidate.patch` (sha256 `982f5469…`), `Kb82M01Loader-candidate.diffstat.txt`
- `Kb82M01Loader-counter_cand.{out,err}`, `Kb82M01Loader-counter_base.{out,err}`
- `Kb82M01Loader-surf_host_base.json`, `Kb82M01Loader-pins_host_base.json`
- `Kb82M01Loader-mut_<M1|M1b|M2|M2b|M3|M3b|M4|M5>_*.patch` and `.run{1,2}.{out,err}`
- `Kb82M01Loader-rename_green.json` (sha256 `89391c5e…`), `Kb82M01Loader-orig_control.json` (sha256 `98c8cbe9…`)
- `Kb82M01Loader-omp.strings.sha256.txt` (`81277d35…`), `Kb82M01Loader-run_mutant.sh`

Report: .ufo/waves/round-82/w1/Kb82M01Loader.md

VERDICT: C1 loader candidate is green on scratch (frozen counter exit 0, `pins OK 3/3; surfaces pass 7 of 7; removal ledger 3 of 3 verified`); 8 red mutants (M1, M1b, M2, M2b, M3, M3b, M4, M5) each red and stable across two runs; rename-equivalent green. No production after-value and no freeze receipt in this seat; residual omp.real defaults in verify_harness_claims.py and verify_harness_independent.py are outside the counter and not moved.

DELIVERABLES:
/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82M01Loader.md
/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82M01Loader-candidate.patch
/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82M01Loader-SHA256SUMS.txt
