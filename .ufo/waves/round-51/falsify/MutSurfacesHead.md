# MutSurfacesHead — mutation probe of `verifiers/verify_surfaces.py` at HEAD (C1 freshness, falsify)

**HOLDS-BOUNDED** — at HEAD `59903b26` the C1 fixture detector (`python3 -B
verifiers/verify_surfaces.py --self-test`, 115 assertions) kills **20 of 27** re-applied base
mutants (**7 survive**, down from 10: M04/M05/M22 are now killed) and kills **7 of 9** new
round-51 mutants. The two new survivors are coverage gaps, not contract breaks: the `--json`
`substrate` block (N08) is unwitnessed by `--self-test`, and the round-50-allowlist must-fail arm
(N09) is self-referential — deleting it leaves the suite green. The surviving base mutants are the
same unwitnessed corners as at base (M06/M07/M13/M18/M19/M21/M25). The 18.12.6 re-pin's load-bearing
behavior — the `Kl|Ho|bq` additions (N01-N03), the module-scope rule and its first/last/global
fallbacks (N04-N07) — is killed everywhere it is bytes.

## Setup

- private clone `/fast/scratch/hyaku/kotoba-r51/falsify/MutSurfacesHead/lane`, HEAD
  `59903b2637689739a5b9901956301da72d0effe1` (cloned from the lane, `git checkout -q <rev>`).
- target `verifiers/verify_surfaces.py`, pristine sha256
  `2669a621dd7ec1418e1a9fda72a21e74c038b57825e0ed6b6273a921e16504b7`.
- detector per mutant: `python3 -B verifiers/verify_surfaces.py --self-test` (fixture-only).
  Pristine baseline: exit **0**, `0 failure(s) over 115 assertions`.
- driver `/fast/scratch/hyaku/kotoba-r51/falsify/MutSurfacesHead/mutate.py`; byte-exact old/new
  per mutant; logs `run.log`, `results.json`, per-mutant `out/<id>.txt` (exit + full stdout).
  Restore: `git -C lane checkout -- verifiers/verify_surfaces.py` (inside the clone only); the
  driver asserts the pristine sha256 after every restore — all 36 matched.
- Base appendix (MutSurfacesBase.md → `MutSurfacesBase/appendix.txt`) applied verbatim except
  M01/M02/M03/M06, whose `OMP_CALL_RE` anchor gained `Kl|Ho|bq` at HEAD — same defect, adapted
  text (drop one pinned callee / widen to `[A-Za-z$_]{1,3}` / drop the lookbehind / drop the
  call-terminator lookahead). Every other anchor matched the HEAD byte exactly.

## Base mutants re-run at HEAD (verdict vs the base table; rows flipped since base in bold)

| id | verdict | failing assertions (deduped) |
|---|---|---|
| M01 | killed (3) | 18.12.5-callees: exit 0; PASS literal_present; PASS no_uncovered_class, all 8 pairs |
| M02 | killed (2) | 18.12.5-callees: exit 0; PASS no_uncovered_class, all 8 pairs |
| M03 | killed (5) | clean: exit 0, PASS no_uncovered_class; new-callees: exit 0, PASS no_uncovered_class; oc-extra: exit 0 |
| M04 | **killed (10)** | 18.12.6-callees×3; fx-renamed-var×3; ambiguous-rebind: claude-md NOT resolved; S$ surfaces unresolved; ambiguous-rebind CLI: unresolved var named; cross-module conflict not settled; own-module binding settles the call |
| M05 | **killed (9)** | as M04 minus "own-module binding settles the call" |
| M06 | survived (0) | — |
| M07 | survived (0) | — |
| M08 | killed (12) | clean/new-callees/18.12.5/18.12.6/fx-renamed-var: exit 0 + literal_present; oc-extra: exit 0; rekind-partial: literal_present green |
| M09 | killed (3) | extract-vacuity: FAIL no_uncovered_class names vacuity; blind-dead-dump: vacuity named; 18.12.6-round50-allowlist: vacuity named |
| M10 | killed (3) | extractor-blind: exit 1, FAIL no_uncovered_class names blindness, names omp:gemini/GEMINI.md |
| M11 | killed (6) | rekind-doc: exit 1, FAIL names laundering, names gemini+claude-md->doc; rekind-partial: exit 1, names claude-md->doc |
| M12 | killed (1) | vacuous-parity: FAIL table_parity |
| M13 | survived (0) | — |
| M14 | killed (4) | noreason: exit 1, FAIL excluded_reason, names claude-md; missing-excluded-row: FAIL excluded_reason |
| M15 | killed (10) | literal-drift/no-literal-cell/id-not-first/vacuous-parity FAIL literal_parity arms |
| M16 | killed (24) | every opencode-extract arm (strings-opencode-drop-oc*.txt, oc-planted-name, oc-v2.0.26-generation, oc-empty-baseline, oc-zero-extraction) |
| M17 | killed (2) | oc-planted-name: exit 1, names GUIDE.md undeclared |
| M18 | survived (0) | — |
| M19 | survived (0) | — |
| M20 | killed (3) | strings-opencode-drop-oc3b.txt: exit 1, FAIL opencode_extract, names instructions-remote |
| M21 | survived (0) | — |
| M22 | **killed (3)** | ambiguous-rebind: S$ surfaces unresolved; ambiguous-rebind CLI: unresolved var named; cross-module conflict not settled |
| M23 | killed (19) | clean/new-callees/18.12.5/18.12.6/fx-renamed-var PASS arms (+exit), own-module binding settles, rekind-doc/partial names |
| M24 | killed (1) | oc-zero-extraction: says vacuity |
| M25 | survived (0) | — |
| M26 | killed (4) | strings-opencode-drop-oc3a.txt×3; oc-zero-extraction: says vacuity |
| M27 | killed (19) | extra-class×3; 18.12.5/18.12.6/fx-renamed-var no_uncovered_class; extract-vacuity/blind-dead-dump vacuity; rekind-doc/partial; extractor-blind×3; 18.12.6-round50-allowlist; ambiguous-rebind CLI |

## New mutants of the round-51 code

| id | mutant | verdict | failing assertions |
|---|---|---|
| N01 | drop `Kl` from the allowlist | killed (6) | 18.12.6-callees×3; fx-renamed-var×3 |
| N02 | drop `Ho` from the allowlist | killed (6) | same as N01 |
| N03 | drop `bq` from the allowlist | killed (10) | as N01 + ambiguous-rebind×2, CLI×3, cross-module×2, own-module |
| N04 | module-scope resolution keeps the FIRST in-module binding | killed (5) | ambiguous-rebind: claude-md NOT resolved; S$ surfaces unresolved; CLI×3 |
| N05 | module-scope resolution keeps the LAST in-module binding | killed (2) | ambiguous-rebind: S$ surfaces unresolved; CLI: unresolved var named |
| N06 | ignore module boundaries (whole dump one scope) | killed (7) | 18.12.6-callees×3; fx-renamed-var×3; own-module binding settles the call |
| N07 | resolve conflicted names from the nearest preceding binding anywhere | killed (3) | ambiguous-rebind: S$ surfaces unresolved; CLI: unresolved var named; cross-module conflict not settled |
| N08 | remove the `substrate` block from `--json` | survived (0) | — |
| N09 | remove the round-50-allowlist must-fail arm (b2e) | survived (0) | — |

## Findings

1. **M07 still survives**: every declared literal is present in every fixture, so the literal-absence
   probe is unwitnessed at HEAD too. The 18.12.6 fixture witnesses the extraction side of
   `literal_present` (its loader-group/pair conjunct), not the absence probe. A fixture with a
   declared literal absent from its dump would kill it.
2. **M04/M05 are now killed** — the `constant_table` conflict policy is witnessed by the new
   b2d/b2f/b2g/b2h arms (real-fixture S$ rebind, renamed-variable control, in-module ambiguity,
   cross-module controls). This was the base wave's top C1-relevant gap; it is closed.
3. **M22 is now killed**: the `<unresolved-var:NAME>` fallback is exercised by b2g/b2h.
4. **N08 survives (new gap)**: the round-51 `substrate` block (`binary_digest`/`substrate_identity`,
   the `--json` payload's sha256/mtime/size) has no `--self-test` arm; only the live `--json` gate
   exercises it. If the counter's C1 claim includes the substrate block, that part is fixture-unwitnessed.
5. **N09 survives (new gap)**: removing the whole b2e must-fail arm leaves the suite green — the arm
   is the only witness of the "round-50 list must FAIL on 18.12.6" discriminator. Self-referential:
   it tests the swap, not its own presence.
6. **M13/M06/M18/M19/M21/M25 survive as at base**: `surfaces.kind_parity` still has no self-test
   arm (inventory-kind-drift.md still orphaned); OC-3b's two conjuncts are still only jointly
   witnessed (M20); OMP call-terminator lookahead, ASSIGN_RE bound, and the OC-1 gate conjunct are
   still equivalent on the current fixtures.

## Evidence (all commands in the private clone)

```
$ git -C lane rev-parse HEAD
59903b2637689739a5b9901956301da72d0effe1
$ sha256sum lane/verifiers/verify_surfaces.py
2669a621dd7ec1418e1a9fda72a21e74c038b57825e0ed6b6273a921e16504b7
$ python3 -B verifiers/verify_surfaces.py --self-test          # pristine
0 failure(s) over 115 assertions                                 # exit 0
$ python3 -B mutate.py                                          # 36 mutants, one at a time
M01 exit=1 killed=True failures=3 ... N09 exit=0 killed=False failures=0   # exit 0
$ sha256sum verifiers/verify_surfaces.py                        # after the last restore
2669a621dd7ec1418e1a9fda72a21e74c038b57825e0ed6b6273a921e16504b7
$ git -C lane status --porcelain                                # empty (byte-exact restore)
$ python3 -B verifiers/verify_surfaces.py --self-test          # after all restores
0 failure(s) over 115 assertions                                 # exit 0
```

Mutated-file sha256 prefixes for every mutant are in `results.json` (M01 `5138dc4f` … N09
`6a6e931f`); the restored sha256 equaled the pristine value after every one of the 36 restores.
Read-only on the lane checkout: the only file written there is this report; no git/jj write ran in
the lane, the fleet repo or any sibling lane. No tool was installed or upgraded; no web source was
consulted.
