# ScoutRegistry — round 62 registry and census (read-only)

Lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Measured revision `master` = `3e7aed9b61bbfd83e0c800213b6dfc6da6191f85` (`git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse master`). No install. No SKILL.md / SOURCES.md / git / jj mutation.

## 1. Gate-registry schema (what a new row must pass)

Source: `verifiers/check_gate_registry.py` header and `judge_row` (lines 16-43, 178-224). Header pinned in the checker, not read from the measured revision (Q28). Universe: every blob directly under `verifiers/` ending `.py` or `.sh` at `--rev` (`git ls-tree`, no recursion).

A row is conformant iff exactly one row in the first table under `## Gate registry` has name cell `verifiers/F`, and:

| clause | rule |
|---|---|
| kind | `gate` or `probe` |
| entry command | cell contains the text `verifiers/F` |
| verdict map | at least one `<code>=<class>` (`=`, `->`, or `→`); class one of `clean`, `failed`, `could-not-evaluate`; no code twice; a `gate` declares `0=clean` and `1=failed` |
| self-test | `none` or one or more backticked flags; each flag an exact active handler (`add_argument` string or shell `case` arm). A `gate` may not say `none` |
| probe (not used here) | rejected if the map declares `1=failed` or the script has an exact `--self-test` handler |
| pinned values | `none`, `in-file`, or backticked repo-relative paths that `git cat-file -e <rev>:<path>` accepts (no leading `/`, no `..`). A `gate` may not say `none` |
| write scope | non-empty and not `-` / em dash / en dash |
| owner | `kotoba` |

Output line: `gate registry rows conformant <K> of <M> lane verifiers; phantom <P>`. Exit 0 iff `K == M` and `P == 0`. A `verifiers/...` name outside the universe is a phantom.

**Q35** (`corpus/QUALITY.md` line 46): every `.py`/`.sh` under `verifiers/` has exactly one Gate registry row, and a `gate` row names a self-test flag the script handles itself. Check: `verifiers/check_gate_registry.py`.

**Q46** (`corpus/QUALITY.md` line 57): a withdrawn claim keeps its row only with an in-cell `claim withdrawn` annotation saying it is not a claim gate until redesigned and re-controlled. The `gate` kind alone reads as a live claim gate. A `probe` relabel is checked against this counter first (a probe that still has `--self-test` fails). These two candidates are live claim gates: no `claim withdrawn` gloss, no `probe` relabel.

Row order is not checked. A blank line after the table ends it (`registry_rows`); the new rows must sit inside the existing table.

Both candidate files are blobs on this `master` (`git ls-tree --name-only master verifiers/` prints both). `verifiers/check_scoped_rules_v31.py` is absent from that listing and from the working tree (`ls` -> `No such file or directory`).

### Row — `verifiers/check_erratum_absorption.py`

CLI (`main`, lines 464-496): only `--self-test` (`parser.add_argument("--self-test", action="store_true")`); missing it is `parser.error`. Exit `2` on `CounterPinMismatch`, `1` on `MatrixFailure` / `OSError` / `ImportError` / `AttributeError` or when `measured != 5` or `controls != 2`, else `0`. Exit 0 does not require `absorbed == 5` (survivors still print and the process returns 0). Pin is the in-file constant `COUNTER_SHA256` (line 15) checked against `check_scoped_rules.py` bytes and `self_sha()`; not a separate pinned path. Writes: none. Guard disable is `setattr` on the imported module inside `patched` (lines 276-287), restored in `finally`; `sys.dont_write_bytecode = True` (line 80). No `open` / temp directory.

Must pass: Q35 (exactly one row; `--self-test` handler exists), gate `0=clean` and `1=failed`, pinned not `none`, write scope non-empty, owner `kotoba`, and not a phantom (the blob is already in the universe, so the row is required now). Do not add a Q46 withdrawal annotation.

```
| `verifiers/check_erratum_absorption.py` | gate | `python3 -B verifiers/check_erratum_absorption.py --self-test` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none (read-only) | kotoba |
```

Suggested neighbor (unchecked): after `verifiers/check_description_thresholds.py`.

### Row — `verifiers/check_routed_repairs_v2.py`

CLI (lines 10-12, 611-646): `--rev` and `--self-test`, both `add_argument`. CLI exit `0` iff score `== 6`, `1` otherwise, `2` on unreadable rev/tree (`could-not-evaluate`). Self-test returns `0` or `1`. Pins are in-file `BASE_REV` and `TIP_REV` (lines 30-31). No `open` / temp directory; git is read-only `show` / `ls-tree`. Registry intro says `<rev>` is a full hash, never a moving ref, so the entry names `--rev <rev>` (the script's default is `master`).

Same checks as the absorption row. Live gate: no Q46 withdrawal annotation, no `probe` relabel.

```
| `verifiers/check_routed_repairs_v2.py` | gate | `python3 -B verifiers/check_routed_repairs_v2.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none (read-only) | kotoba |
```

Suggested neighbor (unchecked): immediately after `verifiers/check_routed_repairs.py`.

### `check_scoped_rules_v31.py` — no row now

Recommend no row until the blob lands in the same revision the registry measures. It is not on disk and not in `git ls-tree master verifiers/`. A row naming `verifiers/check_scoped_rules_v31.py` before that blob exists is a phantom (`P > 0`, exit 1). Plan section E1 moved the successor out of C1's counted predicate; it is not a gate until it lands. When `verifiers/check_scoped_rules_v31.py` is a blob at the measured rev, Q35 requires exactly one `gate` row in that same revision (a row committed earlier is a phantom; a blob without a row is `registry rows naming it: 0`). Do not relabel it `probe` if the file grows an exact `--self-test` handler.

## 2. Census

Round-start receipt `.ufo/waves/round-62/census-before.txt` (lines 3-20): same command, `exit=0`, **15** `W04` lines (lines 4-18), final `kotoba	ok	…/corpus/SOURCES.md`. No `E11`.

Re-run:

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
kotoba	W04	S018 duplicate url agentskills.io/specification across scopes
kotoba	W04	S019 duplicate url platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices across scopes
kotoba	W04	S021 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S054 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S055 duplicate url code.visualstudio.com/docs/agent-customization/agent-skills across scopes
kotoba	W04	S056 duplicate url docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference across scopes
kotoba	W04	S065 duplicate url code.claude.com/docs/en/skills.md across scopes
kotoba	W04	S086 duplicate url developers.openai.com/plugins/build/plugins.md across scopes
kotoba	W04	S103 duplicate url code.claude.com/docs/en/memory.md across scopes
kotoba	W04	S104 duplicate url learn.chatgpt.com/docs/agent-configuration/agents-md.md across scopes
kotoba	W04	S106 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba	W04	S110 duplicate url code.claude.com/docs/en/hooks.md across scopes
kotoba	W04	S111 duplicate url learn.chatgpt.com/docs/hooks.md across scopes
kotoba	W04	S114 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba	W04	S115 duplicate url cursor.com/docs/rules across scopes
kotoba	W04	S118 duplicate url code.claude.com/docs/en/memory.md across scopes
kotoba	E11	S118 missing used-by corpus/lessons/round-62.md
kotoba	E11	S118 missing used-by corpus/knowledge/erratum-absorption-round62.md
exit=1
```

**W04 count: 15 -> 16 (delta +1).** The only new W04 line is:

```
kotoba	W04	S118 duplicate url code.claude.com/docs/en/memory.md across scopes
```

Cause (`scripts/sources-census.sh` lines 643-645): W04 fires when the URL was already seen and the `(url, scope)` pair was not. S118's source cell is `https://code.claude.com/docs/en/memory.md` (`corpus/SOURCES.md` line 129), the same URL as S103 (line 115) and S043 (line 56). S118's scope cell is different (`Current Claude Code `.claude/rules/` `paths` frontmatter matching syntax`); teaches says `re-opens S103`, not `supersedes S###`, so a same-scope repeat would have been E04. It is W04, across scopes, by design (plan frontier step: S118 re-opens the page S103 already cites for the `paths` frontmatter text). Comment at script line 33: W04 does not by itself fail a clean lane. **Exit 1 is the two E11 lines**, not the new W04. E11 (`usedby_findings`, lines 560-567) splits the mined used-by cell on commas and tests `[ ! -e ]`. S118 used-by (line 129) is exactly `corpus/lessons/round-62.md, corpus/knowledge/erratum-absorption-round62.md`. Neither path exists (`ls` on both -> `No such file or directory`).

## 3. Registry gate and seat-count self-test

```
$ python3 -B verifiers/check_gate_registry.py --rev $(git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse master)
```

`--rev` resolved to `3e7aed9b61bbfd83e0c800213b6dfc6da6191f85`. cwd: lane root.

```
verifiers/box_proof_case_deletion.py         OK 
verifiers/check_agent_definitions.py         OK 
verifiers/check_agentdef_boxes.py            OK 
verifiers/check_alwayson_boxes.py            OK 
verifiers/check_assertion_floors.py          OK 
verifiers/check_callee_rename.py             OK 
verifiers/check_command_files.py             OK 
verifiers/check_correction_sweep.py          OK 
verifiers/check_could_not_evaluate.py        OK 
verifiers/check_description_thresholds.py    OK 
verifiers/check_erratum_absorption.py        no registry rows naming it: 0 (need 1)
verifiers/check_explicit_invocation.py       OK 
verifiers/check_gate_finding_delta.py        OK 
verifiers/check_gate_registry.py             OK 
verifiers/check_hook_files.py                OK 
verifiers/check_infoless_fences.py           OK 
verifiers/check_mcp_instructions.py          OK 
verifiers/check_opencode_repin.py            OK 
verifiers/check_overlap_levers.py            OK 
verifiers/check_plugin_manifests.py          OK 
verifiers/check_routed_repairs.py            OK 
verifiers/check_routed_repairs_v2.py         no registry rows naming it: 0 (need 1)
verifiers/check_scoped_rules.py              OK 
verifiers/check_seat_counts.py               OK 
verifiers/check_sibling_census.py            OK 
verifiers/check_sources_append_only.py       OK 
verifiers/check_substrate_pins.py            OK 
verifiers/check_sweep_mutants.py             OK 
verifiers/compare_harness_independent.py     OK 
verifiers/fault_injection_corpus.sh          OK 
verifiers/verify_alwayson.py                 OK 
verifiers/verify_corpus_independent.py       OK 
verifiers/verify_corpus_integrity.py         OK 
verifiers/verify_dispatch_prompts.py         OK 
verifiers/verify_harness_claims.py           OK 
verifiers/verify_harness_independent.py      OK 
verifiers/verify_skill_checklist.py          OK 
verifiers/verify_surfaces.py                 OK 
gate registry rows conformant 36 of 38 lane verifiers; phantom 0
exit=1
```

The two missing rows are the only failures. Phantom 0 (v31 has no row and no blob). Working-tree `SKILL.md` section Gate registry likewise has no row for either name (read lines 470-507).

```
$ python3 -B verifiers/check_seat_counts.py --self-test
self-test complete: (3, [], []) (want (3, [], [])) ok
self-test one-missing: (2, ['Beta']) (want (2, ['Beta'])) ok
self-test registry-is-not-a-seat: [] (want []) ok
self-test round61-shape: (1, ['Beta', 'Gamma'], ['Note.md']) (want (1, ['Beta', 'Gamma'], ['Note.md'])) ok
self-test empty-spec-raises: True (want True) ok
seat reports committed 1 of 3; missing 2: Beta, Gamma; unmatched 1: Note.md
self-test arm-count: 5 (want 5) ok
self-test: 0 failure(s)
exit=0
```

## 4. `corpus/README.md` index

**Yes, one coverage-map row per new tracked file, in the same landing as the file — not before.** `verifiers/verify_corpus_integrity.py` (`corpus.index.unindexed`, lines 7-10 and 443-444) requires every tracked `corpus/` path except `README.md` to match a File-column pattern. `corpus.index.stale_patterns` (lines 11-12) fails a corpus-internal File pattern that matches no tracked file. A row now, while both paths are absent, is a stale pattern; a later commit of the files without rows is `unindexed` (the README itself records that failure at lines 98, 101, and 71: lessons that landed without a row turned the gate red with `unindexed 1`).

The two paths S118 already names, both absent:

- `corpus/knowledge/erratum-absorption-round62.md` (the entry)
- `corpus/lessons/round-62.md` (the lesson)

Shape: **one line per file**, not two. Lines 104-106 are three such rows (two knowledge entries, then the lesson). Columns are `Area | File | Basis`. The File cell is one backticked corpus-relative path. Verbatim (`corpus/README.md:104-106`):

```
| Scoped-rules counter v3 (round 61) | `knowledge/scoped-rules-counter-round61.md` | the provenance-authenticating redesign of the r60 exploratory counter: guarded A1 canonical scope keys (read from committed S112–S115 rows at the measured rev), guarded A2 action support, A3 url_key identity + fresh-row rendering-alias rejection, A4 four conjuncts incl. the full-64-hex alias arm; seven r60 worlds reject under v3 (receipt `.ufo/waves/round-61/receipts/C1-worlds.txt`); sources S112–S115 |
| Writing-revision calibration for prompt-craft self-assessment (round 61) | `knowledge/writing-revision-calibration-round61.md` | practice-level borrowing from sibling source S117: check a self-assessment against its writing revision rather than read-time state; P/H/N/C/T/Q as a claim-shape taxonomy pattern for `SKILL.md`/`SCORECARD.md`; no kama domain content imported |
| Round-61 lessons | `lessons/round-61.md` | `## Gate` S112–S115 + S117 with access records, the named S116 gap, status change S117 queued→mined; `## Mistakes` M91 (report-evidence overstatement) + M92 (presence-counter axis claim); `## Falsify corrections` |
```

## Confidence and gaps

- High: schema, both row texts, registry `36 of 38` / exit 1, seat-count exit 0, census 15 to 16 W04 plus two E11 / exit 1, S118 URL identity with S103 and S043, v31 absent.
- Not run: `verify_corpus_integrity.py` (not in the assignment). The index conclusion is from that checker's documented checks plus the missing paths, not from a live unindexed count.
- Unresolved: the exact Area/Basis prose for the two future README rows (files do not exist yet). The File cells are fixed by S118's used-by: `` `knowledge/erratum-absorption-round62.md` `` and `` `lessons/round-62.md` ``.
