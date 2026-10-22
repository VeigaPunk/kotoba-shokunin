# MutSurfacesBase — baseline mutation probe of `verifiers/verify_surfaces.py` (C1 freshness)

**HOLDS-BOUNDED** — at base `43ca0bfb` the C1 fixture detector
(`python3 -B verifiers/verify_surfaces.py --self-test`, 99 assertions) kills **17 of 27** mutants;
**10 survive**. Every survivor is a *fixture-coverage gap*, not a contract change: the callee
allowlist pin, the alias-decoy guard and the var-bound group resolution are genuinely witnessed
(M01/M02/M03/M23 killed), but the literal-absence probe, the constant-table conflict policy, the
call-terminator lookahead, the `<unresolved-var:>` fallback, the OC-1 gate conjunct and
`surfaces.kind_parity` itself are **not** witnessed by any committed fixture. Advisory input for
the C1 re-pin (18.12.6) and for the falsify wave.

## Setup

- private clone `/fast/scratch/hyaku/kotoba-r51/build/MutSurfacesBase/lane` (clone of the lane
  repo, `HEAD` = `43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10`); target
  `verifiers/verify_surfaces.py`, pristine sha256
  `1856675d9415b6be968b3001aaa5b926934925bfcfd9488c39ac360de9df0b5a`.
- expected detector for every mutant: `python3 -B verifiers/verify_surfaces.py --self-test`
  (fixture-only; no network, no host binary). Pristine baseline: exit **0**, `0 failure(s) over 99
  assertions`.
- driver `/fast/scratch/hyaku/kotoba-r51/build/MutSurfacesBase/mutate.py` (sha256
  `1ffd50a703bba1d1e7ac6e1369ff0f45edf8aa57b2fd8930f0c8f1981bf31e0a`); byte-exact old/new per
  mutant in `appendix.txt`, line-anchored index in `compact.txt`; logs `run.log`, `results.json`,
  `coverage.log` (same dir).
- procedure per mutant: apply one text substitution → run the detector → restore with
  `git -C <clone> checkout -- verifiers/verify_surfaces.py` (inside the clone only) → re-hash. All
  27 mutants were applied one at a time; the file was restored to the pristine sha256 after every
  one of them.

## Mutants, verdicts and the failing assertions

Base line numbers are those of the pristine file; the exact old/new bytes are in `appendix.txt`.

| id | base lines | mutant | verdict | failing assertions |
|---|---|---|---|---|
| M01 | 157 | drop callee `Fo` from `OMP_CALL_RE` | **killed** (1) | `18.12.5-callees: exit 0`; `18.12.5-callees: PASS literal_present`; `18.12.5-callees: PASS no_uncovered_class, all 8 pairs` |
| M02 | 157 | widen the callee allowlist to `[A-Za-z$_]{1,3}` | **killed** (1) | `18.12.5-callees: exit 0`; `18.12.5-callees: PASS no_uncovered_class, all 8 pairs` |
| M03 | 157 | drop the `(?<![A-Za-z0-9_$])` lookbehind (alias-decoy guard) | **killed** (1) | `clean: exit 0`; `clean: PASS surfaces.no_uncovered_class`; `new-callees: exit 0`; `new-callees: PASS surfaces.no_uncovered_class`; `oc-extra: exit 0` |
| M04 | 308-310 | `constant_table` keeps the **first** binding on a conflicting rebind | survived (0) | — |
| M05 | 306-312 | `constant_table` keeps the **last** binding on a conflicting rebind | survived (0) | — |
| M06 | 156-160 | drop the `(?=\s*[,)])` call-terminator lookahead in `OMP_CALL_RE` | survived (0) | — |
| M07 | 579-584 | remove the literal-presence probe from `check_literal_present` | survived (0) | — |
| M08 | 579 | invert the literal-present condition (`not in` → `in`) | **killed** (1) | `clean: exit 0`; `clean: PASS surfaces.literal_present`; `new-callees: PASS literal_present`; `18.12.5-callees: PASS literal_present`; `rekind-partial: gemini row untouched … literal_present green`; `oc-extra: exit 0` |
| M09 | 629-634 | remove the zero-extraction **vacuity** arm of `check_no_uncovered_class` | **killed** (1) | `extract-vacuity: FAIL no_uncovered_class names vacuity`; `blind-dead-dump: vacuity named` |
| M10 | 635-644 | remove the extractor-blind arm of `check_no_uncovered_class` | **killed** (1) | `extractor-blind: exit 1`; `extractor-blind: FAIL no_uncovered_class names blindness`; `extractor-blind: names omp:gemini/GEMINI.md` |
| M11 | 650-659 | remove the kind-laundering arm of `check_no_uncovered_class` | **killed** (1) | `rekind-doc: exit 1`; `rekind-doc: FAIL no_uncovered_class names laundering`; `rekind-doc: names omp:gemini/GEMINI.md->doc`; `rekind-doc: names omp:claude-md/CLAUDE.md->doc`; `rekind-partial: names omp:claude-md/CLAUDE.md->doc` |
| M12 | 680-682 | remove the empty-baseline vacuous guard of `check_table_parity` | **killed** (1) | `vacuous-parity: FAIL table_parity` |
| M13 | 779-784 | make `check_kind_parity` a no-op (always PASS) | survived (0) | — |
| M14 | 810-811 | make `check_excluded_reason` a no-op | **killed** (1) | `noreason: exit 1`; `noreason: FAIL excluded_reason`; `noreason: names omp:claude-md/CLAUDE.md`; `missing-excluded-row: FAIL excluded_reason` |
| M15 | 696-699 | make `check_literal_parity` a no-op | **killed** (1) | `literal-drift: FAIL literal_parity`; `no-literal-cell: FAIL literal_parity`; `id-not-first: FAIL literal_parity`; `vacuous-parity: FAIL literal_parity` (+ their `exit 1` / naming arms) |
| M16 | 739-740 | **skip the opencode extraction** (`check_opencode_extract` always PASS) | **killed** (1) | 24 failing assertions: every `strings-opencode-drop-oc*.txt: FAIL opencode_extract`, `oc-zero-extraction: says vacuity`, `oc-v2.0.26-generation: FAIL opencode_extract`, `oc-planted-name: names opencode:instructions/GUIDE.md undeclared`, `oc-empty-baseline: FAIL opencode_extract` |
| M17 | 458-460 | OC-1 stops deriving names from the priority array | **killed** (1) | `oc-planted-name: exit 1`; `oc-planted-name: names opencode:instructions/GUIDE.md undeclared` |
| M18 | 480-481 | drop the OC-3b render-token conjunct (`OC_REMOTE_RENDER`) | survived (0) | — |
| M19 | 402-405 | loosen `OC_REMOTE_FILTER_RE` (drop the `.filter(` requirement, round-47 tightening) | survived (0) | — |
| M20 | 480-481 + 402-405 | weaken OC-3b to the OC-3a shape (M18 **and** M19 together) | **killed** (1) | `strings-opencode-drop-oc3b.txt: exit 1`; `…: FAIL opencode_extract`; `…: names opencode:config/instructions-remote` |
| M21 | 168 | widen `ASSIGN_RE` value bound 80 → 200 | survived (0) | — |
| M22 | 330-331 | unresolved identifier group falls back to the raw identifier | survived (0) | — |
| M23 | 328-331 | identifier groups are never resolved through the constant table | **killed** (1) | `clean: PASS surfaces.literal_present`; `clean: PASS surfaces.no_uncovered_class`; `18.12.5-callees: PASS no_uncovered_class, all 8 pairs`; `new-callees: PASS literal_present` (+ their `exit 0` arms) |
| M24 | 742-746 | remove the zero-extraction vacuity arm of `check_opencode_extract` | **killed** (1) | `oc-zero-extraction: says vacuity` |
| M25 | 457 | drop the OC-1 `disableClaudeCodePrompt` gate conjunct | survived (0) | — |
| M26 | 477 | drop the OC-3a declared-list-loop anchor (`OC_DECLARED_RE`) | **killed** (1) | `strings-opencode-drop-oc3a.txt: exit 1`; `…: FAIL opencode_extract`; `…: names opencode:config/instructions`; `oc-zero-extraction: says vacuity` |
| M27 | 624-625 | `check_no_uncovered_class` skips the omp harness | **killed** (1) | `extra-class: FAIL no_uncovered_class`; `extra-class: names omp:foo/FOO.md`; `extractor-blind: names omp:gemini/GEMINI.md`; `rekind-doc: names omp:gemini/GEMINI.md->doc` (+ 12 more) |

Mutated-file sha256 prefixes (the restored sha256 = pristine for every mutant): M01 `b888e670c9` · M02
`532db1d78c` · M03 `a5f9d86056` · M04 `553fa3e0f9` · M05 `c2b5153a67` · M06 `dc1e4cc405` · M07
`f0de63c5a4` · M08 `f713156669` · M09 `817158d674` · M10 `b4a4569040` · M11 `7d7a644033` · M12
`4ed5ff901f` · M13 `0df7391eba` · M14 `7b82be4189` · M15 `d63d0f969c` · M16 `fe0c8b2513` · M17
`750e93249a` · M18 `3d0c1fea93` · M19 `4a366667b1` · M20 `921de5cd5a` · M21 `63138d18ce` · M22
`759fd92921` · M23 `bd3d4db520` · M24 `bd7df72b1d` · M25 `6b595e151e` · M26 `66430dedd5` · M27
`afd106a9c3`.

## Findings (coverage gaps behind the 10 survivors)

1. **M07 — the literal-absence probe is unwitnessed (C1-relevant, highest priority).** Every declared
   literal is present in its dump fixture (`coverage.log`: `omp literals absent from dump: []` for
   both `baseline-clean.json`/`strings-omp-clean.txt` and `baseline-18.12.5.json`/
   `strings-omp-18.12.5.txt`), so deleting the probe changes nothing. The failure mode C1 must fix
   at base — `surfaces.literal_present: 8 loader literals not verifiable` on the live 18.12.6 dump —
   is exercised by **no fixture**. A fixture whose declared literal is absent from the dump would
   witness it.
2. **M04/M05 — the `constant_table` conflict policy is unwitnessed.** No fixture rebinds an
   identifier to a different string (`coverage.log`, "conflicting rebinds per fixture" is empty), so
   drop-on-conflict, keep-first and keep-last are indistinguishable. This matters for the C1 re-pin:
   the 18.12.5/18.12.6 dumps use var-bound groups (`f$`, `m$`); if the new dump rebinds one of
   them, the current policy drops the binding and the extractor emits `<unresolved-var:NAME>`, which
   no fixture would show.
3. **M13 — `surfaces.kind_parity` has zero self-test arms (pre-existing).** The check is one of the
   seven `CHECK_IDS` and the module docstring advertises it, but no fixture drives it: its only
   fixture, `verifiers/fixtures/surfaces/inventory-kind-drift.md`, is **orphaned** — `grep -rn
   "kind-drift" verifiers/` returns 0 hits (referenced only in `.ufo/round-22/scouts/P3.md`,
   `.ufo/round-23/scouts/G6.md`, `.ufo/round-24/scouts/S4.md`, `.ufo/round-26/scouts/S7.md`,
   `.ufo/round-32/scouts/S8.md`, `.ufo/waves/round-47/falsify/W2FixtureWorld.md` — carried since
   round 14). Run by hand it is a single-cause kind-drift arm: exit **1**, `FAIL
   surfaces.kind_parity: 1 census row kind(s) disagree with the baseline: omp:gemini/GEMINI.md
   (line 9: census kind 'loader-literal' != baseline context_kind 'loader-group')` with every other
   check PASS. Adopting it as an arm is a one-line change (`run(inventory=fx +
   "/inventory-kind-drift.md")` + one `rec(...)`) and would kill M13.
4. **M18/M19 — OC-3b's two anchors are removed together.** `strings-opencode-drop-oc3b.txt` drops
   both the filter shape and the render token (`grep -c '\.filter('` = 0, `grep -c 'Instructions
   from'` = 0; the clean fixture has 1 and 1), so neither conjunct of `remote = (filter AND render)`
   is individually load-bearing; only the joint weakening (M20) is killed. Two single-anchor
   fixtures would separate them.
5. **M22 — the `<unresolved-var:NAME>` fallback never fires.** Every identifier group in every omp
   fixture resolves (`coverage.log`: `unresolved=[]` for `strings-omp-clean.txt`, `-newcallees`,
   `-18.12.5`, `-blind`), so the "unresolvable ones surface as a marker" guarantee is untested.
6. **M25 — the OC-1 gate conjunct never discriminates.** Every fixture that carries the priority
   array also carries `disableClaudeCodePrompt` (`coverage.log`, array=True/gate=True for all nine
   opencode fixtures); no fixture has the array without the gate.
7. **M06/M21 — equivalent on the current fixture set.** Strict and lookahead-free `OMP_CALL_RE`
   produce identical match sets on all four omp fixtures (2/2, 2/2, 8/8, 0/0), and the longest
   `ASSIGN_RE` binding in the fixture set is 9 characters against a bound of 80.

Not fixed here: a surviving mutant is a coverage finding, not a licence to change the contract. The
fixes are fixture additions inside `verifiers/fixtures/surfaces/` plus self-test arms; they belong
to whoever owns the C1 verifier change.

## Evidence (commands and exit codes, all run in the private clone)

```
$ git -C lane rev-parse HEAD
43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10
$ sha256sum lane/verifiers/verify_surfaces.py
1856675d9415b6be968b3001aaa5b926934925bfcfd9488c39ac360de9df0b5a
$ python3 -B verifiers/verify_surfaces.py --self-test          # pristine
0 failure(s) over 99 assertions                                 # exit 0
$ python3 -B mutate.py                                          # 27 mutants, one at a time
SUMMARY killed=17 survived=10 error=0 total=27                 # exit 0
$ sha256sum lane/verifiers/verify_surfaces.py                   # after the last restore
1856675d9415b6be968b3001aaa5b926934925bfcfd9488c39ac360de9df0b5a
$ git -C lane status --porcelain                                # empty (byte-exact restore)
$ python3 -B verifiers/verify_surfaces.py --self-test          # after all restores
0 failure(s) over 99 assertions                                 # exit 0
$ python3 -B verifiers/verify_surfaces.py --repo verifiers/fixtures/surfaces \
    --omp-strings …/strings-omp-clean.txt --opencode-strings …/strings-opencode-clean.txt \
    --baseline …/baseline-clean.json --inventory …/inventory-kind-drift.md
FAIL surfaces.kind_parity: 1 census row kind(s) disagree with the baseline: omp:gemini/GEMINI.md
    (line 9: census kind 'loader-literal' != baseline context_kind 'loader-group')   # exit 1
```
The driver asserts the pristine sha256 after **every** restore; all 27 restores matched
`1856675d9415b6be968b3001aaa5b926934925bfcfd9488c39ac360de9df0b5a`, and the working tree is clean.

## Reproduction for the falsify wave, and scope

`mutate.py` is self-contained: it clones nothing, mutates only
`<clone>/verifiers/verify_surfaces.py`, restores with `git -C <clone> checkout --` inside the
clone, and re-hashes after each mutant. On the round's head the same 27 substitutions re-run
verbatim; mutants whose base line numbers moved are located by their **exact old text**
(`appendix.txt`), not by line number. M20 = M18 + M19 (the only way OC-3b is killable) is the one
composite mutant; the rest are single-site edits. `coverage.log` re-derives every coverage claim
above from the committed fixtures alone. Read-only on the lane checkout: the only file written
there is this report; no git/jj write ran in the lane repo, the fleet repo or any sibling lane;
all writes happened in `/fast/scratch/hyaku/kotoba-r51/build/MutSurfacesBase/`. No tool was
installed or upgraded (none needed); no web source was consulted.
