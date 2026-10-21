verdict: HOLDS — every opencode class id declared anywhere in the census/baseline git history (12 distinct ids) has a round-47 ledger row with a verdict, and each verdict matches the current baseline; no id is silently absent from both. Calibration caveat: that completeness is prose-only, and a census edit that deletes a ledger row passes every gate.

# Target

`git log -p -- corpus/knowledge/instruction-surface-census-round13.md verifiers/surfaces-baseline.json` vs the round-47 ledger at `corpus/knowledge/instruction-surface-census-round13.md:305-321` (revision `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`).

Claim tested (census:305-306): "Class ledger (round 47; every id the census ever declared for opencode)" — every historical opencode id carries a round-47 verdict.

# Findings

## F1 — HOLDS: 12/12 ids covered, 1:1, nothing unaccounted

Population derived independently of the ledger:

- census file: 8 commits on the master history (`5cc1340`, `ae3bbb4`, `29c17be`, `02302c5`, `4b50d8d`, `4c1c2cf`, `a46321c`, `7ad7fad`) plus 4 off-history commits that touch the file (`4a9b05d`, `5bdec9a`, `a6fe869`, `bc8c049`, none an ancestor of 7ad7fad);
- baseline file: 4 commits (`5cc1340`, `29c17be`, `02302c5`, `7ad7fad`);
- union, brace-aware (the census writes `opencode:instructions/{AGENTS,CLAUDE,CONTEXT}.md`, which expands to three ids): **12 ids**;
- baseline union: **12 ids**;
- ledger rows at census:310-321: **12**;
- `union − ledger` = `[]`; `ledger − union` = `[]` (no invented rows).

| id | first declared | current baseline | ledger row | verdict |
|---|---|---|---|---|
| `opencode:project/AGENTS.md` | 02302c5 (r18) | absent | :310 | retired |
| `opencode:config/AGENTS.md` | 5cc1340 (r13) | governed | :311 | retained, re-anchored |
| `opencode:read-hook/AGENTS.md` | 02302c5 (r18) | absent | :312 | retired |
| `opencode:api-entries/instructions` | 02302c5 (r18) | absent | :313 | retired |
| `opencode:config/instructions` | 5cc1340 (r13) | governed | :314 | re-verdicted governed |
| `opencode:instructions/AGENTS.md` | 5cc1340 (r13) | governed | :315 | resurrected |
| `opencode:instructions/CLAUDE.md` | 5cc1340 (r13) | governed | :316 | resurrected |
| `opencode:instructions/CONTEXT.md` | 5cc1340 (r13) | governed | :317 | resurrected |
| `opencode:claude-home/CLAUDE.md` | 5cc1340 (r13) | governed | :318 | resurrected |
| `opencode:config/instructions-remote` | 5cc1340 (r13) | governed | :319 | resurrected |
| `opencode:read-hook/instructions` | 5cc1340 (r13) | governed | :320 | resurrected |
| `opencode:instruction-context/AGENTS.md` | 29c17be (r14) | governed | :321 | resurrected |

The 4 off-history round-47 working commits declare the same 12 ids and nothing else, so a stricter "ever declared anywhere" reading also closes at 12.

**No id silently absent from both baseline and ledger.** The only apparent hits in a corpus-wide `opencode:` grep are not ids: `opencode:instructions/GUIDE.md` is a *planted undeclared name* in the verifier's must-fail self-test (`verifiers/verify_surfaces.py:1069-1070`), and the `…z` tokens (`opencode:project/AGENTS.mdNz`, `opencode:config/instructionsz`, `opencode:config/AGENTS.mdz`) are Python bytecode string-table artifacts in `verifiers/__pycache__/verify_surfaces.cpython-314.pyc`, not source declarations.

## F2 — HOLDS: every verdict cross-checks against the files it names

- Current baseline has exactly the 9 live ids, all `verdict: governed` (`verifiers/surfaces-baseline.json:245,252,259,266,273,280,287,294,301`). The 3 `retired` ids are absent from it. Ledger live set = 3 retired + 9 live = 12.
- The 9 live ids equal the § B′ inventory table (`census:249-257`) id-for-id.
- The `round-46 state` column is accurate against the actual BASE document (`c61a973`), not just asserted: BASE has the same 7 ids in its historical note (`c61a973:census:168-174`), the same 4 rows in § B under the v2.0.26 model (`c61a973:census:206-209`), and `config/instructions` in § C as `excluded` (`c61a973:census:223`). New doc: 4 rows at `census:296-299`, § C row at `census:303`, ledger at `census:310-321`.
- The "moved, byte-identical" claim (`census:164-167`) holds: for all five moved rows, the BASE line is an exact member of the new file's lines (checked by string equality, not substring).
- Verdict change is disclosed, not silent: `config/instructions` re-verdict appears in the § B′ prose (`census:240-241`) and in the baseline as `governed` (line 280), while the superseded row keeps its old exclusion reason under a section explicitly titled "Superseded class rows … (not inventory)" (`census:287-289`). A reader who stops at line 303 can see a stale reason, but the doc labels the section and the live row carries the correction.

## F3 — HOLDS: the ledger's anchor counts reproduce on the frozen dump

`sha256sum -c /fast/scratch/kotoba-r47/shared/SHA256SUMS` → exit 0, 4/4 OK (`bin/opencode-1.19.3` = `179ca421…`, matching `census:215`). All ledger anchors counted with the documented command (`census:306`), on `opencode-1.19.3.strings`:

| anchor | count | ledger row |
|---|---|---|
| `ConfigInstructionPlugin.projectSource` | 0 | :310 |
| `X.join(r.config,"AGENTS.md")` | 1 | :311 |
| `j5(r.config,` (round-18 anchor) | 0 | :311 |
| `ReadTool.Plugin` | 0 | :312 |
| `SessionInstructions.load` | 0 | :312 |
| `session.instructions.entry.put` | 0 | :313 |
| `instructions:{entry:{list:` | 1 | :313 |
| `for(let O of T.instructions)` | 1 | :314 |
| `y=["AGENTS.md",` ("priority array") | 1 | :315 |
| `disableClaudeCodePrompt` | 3 | :316 |
| `CONTEXT.md` | 1 | :317 |
| `X.join(r.home,".claude","CLAUDE.md")` | 1 | :318 |
| `Instructions from: ` | 4 | :319 |
| `fn("Instruction.resolve")` | 1 | :320 |
| `fn("ReadTool.execute")` | 1 | :320 |
| `InstructionContext.observe` | 1 | :321 |
| `system-context-builtins` | 1 | :321 |

Semantics spot-checked in the dump, not just counted: `Instruction.resolve` walks `while(G.startsWith(N)&&G!==N)` with `N = X.resolve(yield*J.directory)` (the instance directory, i.e. *inside*, matching the ledger's `read-hook/instructions` resurrection and the retirement of `read-hook/AGENTS.md`); `Instruction.systemPaths` contains `for(let O of T.instructions)` feeding `e.glob(...)` (the proven consumer that re-verdicts `config/instructions`); `n=[X.join(r.config,"AGENTS.md"), ... .claude/CLAUDE.md]` and `y=["AGENTS.md", … "CLAUDE.md", "CONTEXT.md"]` are both present in the `@opencode/Instruction` service. At default resolution in a canonical scratch clone at 7ad7fad, `python3 verifiers/verify_surfaces.py` exits 0 with `opencode extraction 9/9 declared class(es) from 7/7 rules`, `table_parity 42 ids`, `excluded_reason 8`; `check_substrate_pins.py` exits 0 with `OK 3/3 pins hold`.

## F4 — FALSIFIED (operability/calibration): the ledger's completeness claim has no machine guard

No gate parses the ledger. `verifiers/verify_surfaces.py:171` defines the only census parse boundary as `SECTION_HEADING_RE = ^##\s+Class inventory\b` and the section "runs to the next `^##` heading" (`:45`, `:507-518`). The ledger lives under `## Superseded class rows and the round-47 opencode ledger` (`census:287`), outside that boundary, so deleting ledger rows is invisible to every check.

Two mutations, committed in the scratch clone, both survive:

```bash
# M1: remove ledger row :310 only
sed -i '/^| `opencode:project\/AGENTS.md` | governed (OC-1, v2.0.26) | retired/d' \
  corpus/knowledge/instruction-surface-census-round13.md
git commit -qam mut1
python3 verifiers/verify_surfaces.py;                echo $?   # 0 (0 FAIL lines)
python3 verifiers/verify_corpus_integrity.py;        echo $?   # 0
python3 verifiers/verify_corpus_independent.py;      echo $?   # 0
python3 verifiers/verify_skill_checklist.py;         echo $?   # 0
python3 verifiers/check_assertion_floors.py;         echo $?   # 0

# M2: also remove the superseded row :296 — id now appears nowhere in the census
#     (0 occurrences of opencode:project/AGENTS.md remain)
python3 verifiers/verify_surfaces.py;                echo $?   # 0
python3 verifiers/verify_corpus_integrity.py;        echo $?   # 0
python3 verifiers/verify_corpus_independent.py;      echo $?   # 0
python3 verifiers/verify_skill_checklist.py;         echo $?   # 0
python3 verifiers/check_assertion_floors.py;         echo $?   # 0 on rerun (9/9 floors PASS)
```

The first `check_assertion_floors` run on M2 exited 2, but only on `FAIL harness_independent self-test timed out after 120s (hung?)`; an immediate rerun in the same mutated tree exits 0 with `PASS harness_independent observed=104 floor=104` and all nine floors PASS. That is a flaky self-test timeout, not a census signal — its floors count assertions inside the verifier scripts (e.g. `surfaces observed=99 floor=99`), not doc rows.

Consequence: the claim is true at 7ad7fad, but nothing prevents a later round from dropping a historical id while every gate stays green. The ledger should either be regenerated by a committed script or pinned by a fixture (the way the v2.0.26 generation is pinned as a must-fail fixture). `corpus/README.md:40` indexes the census for the corpus-count gate, but that gate checks index completeness/counts, not ledger content — the M1/M2 deletions passed it.

## F5 — minor: the documented reproducibility command does not reproduce the population

`census:305-306` states the id population and then gives a count command for *anchors* (`d.count("<anchor>")`), not for ids. There is no command in the doc that enumerates the 12 ids; reproducing them requires walking git history (the only script that does so is this lane's `.ufo/waves/round-47/falsify/W2LedgerComplete.matrix.json`). One anchor is also implicit: row :315 says "priority array 1"; the concrete literal is `y=["AGENTS.md",` (count 1), named only in § B′ at `census:249`.

# Commands (all paths at 7ad7fad unless noted)

| command | exit | key output |
|---|---|---|
| `git log -p --format='===COMMIT %H %ad %s' --date=short -- corpus/knowledge/instruction-surface-census-round13.md` | 0 | 8 commits |
| `git log -p … -- verifiers/surfaces-baseline.json` | 0 | 4 commits |
| per-version id enumeration (Python, brace-aware) over both histories | 0 | census union 12, baseline union 12, unaccounted `[]`, ledger-only `[]` |
| `sha256sum -c /fast/scratch/kotoba-r47/shared/SHA256SUMS` | 0 | 4/4 OK |
| 17 anchor counts via the `census:306` command | 0 | table in F3 |
| `python3 verifiers/verify_surfaces.py` (scratch clone at 7ad7fad) | 0 | `9/9 … from 7/7 rules`, `42 ids`, `8 excluded` |
| `python3 verifiers/check_substrate_pins.py` | 0 | `OK 3/3 pins hold` |
| M1 + M2 mutation suite (above) | 0 | all census-relevant gates green |
| `python3 verifiers/verify_harness_claims.py` (pristine and mutated) | 1 | identical 7 DRIFT lines on live `~/.omp` state both runs — pre-existing/environmental, unrelated to the census |
| `python3 verifiers/compare_harness_independent.py` in the first batch | timeout | interrupted at 300 s; no result claimed |

Tooling: nothing installed or upgraded.

# What I did NOT check

- The omp half of the census inventory/ledger (out of scope; only `opencode:` ids were assigned).
- C2 (`trigger.no_xml_tag`) and the C3 corpus-index/report counts as independent claims; I only observed that those gates ran green.
- Runtime injection for any resurrected class: all evidence is strings/decompile-shape, so "governed" here means a loader shape exists, not that a file reaches a prompt.
- The v2.0.26 binary is gone (census:216-218 says the channel was removed 2026-10-20), so `retired` is verified as "absent from the 1.19.3 dump", not as "never loaded in 2.0.26"; the round-46 state column was checked against the BASE document text, not re-derived from that binary.
- Anchor semantics beyond the three contexts quoted in F3; the remaining anchors are count-only.
- `verify_harness_independent.py` and a completed `compare_harness_independent.py` run (first batch timed out before them).
- Whether the corpus-count gate hashes doc bodies individually; the M1/M2 mutations passing it shows it does not hash census content for this change, which is all the argument needs.
