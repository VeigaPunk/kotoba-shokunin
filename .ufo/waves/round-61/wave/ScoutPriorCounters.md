# ScoutPriorCounters — readers of `verifiers/check_scoped_rules.py`

Seat: `kotoba-r61-wave-ScoutPriorCounters`. Lane read-only. Census time: `2026-10-23T19:11:07Z` (`date -u '+%Y-%m-%dT%H:%M:%SZ'`, exit 0). Base named by the plan: `f3246d1493b60ea1c0d947a19c39f9e08e92f326`. Counter read: `verifiers/check_scoped_rules.py` (v2; this seat did not execute it).

Question: which lane readers invoke the counter or consume its stdout (registry row, self-test line, summary line), and what breaks if v3 changes the summary line or adds `worlds reject 7 of 7; eligible rows pass 4 of 4`.

## Verdict

No other gate parses the live summary line or the self-test line. The only executable matcher of the summary grammar is the counter's own `--self-test`. `check_gate_registry.py` consumes the SKILL.md **row cells**, not stdout. `check_assertion_floors.py` and `floors-registry.json` do not name this script. The lane has no `scripts/` directory (`test -d …/scripts` → ABSENT, exit 0).

v3 can add the worlds sentence on the `--self-test` path without breaking another gate, **if** it keeps the existing last line `self-test: N failure(s) over M assertions` and does **not** make the worlds sentence line 0 of a `--rev` / `--fetch` run. Changing `summary_line()` without moving the in-file asserts makes `--self-test` exit 1. That is an internal pin, not an external gate.

The r61 predicate (`plans/round-61.md:50-54`) does not require a new `--fetch` summary. It requires `--self-test` to print the worlds sentence and exit 0, and `--rev <tip> --fetch` to exit 0 while the same command at base exits 1.

## Output grammar the counter prints today

Observed in `verifiers/check_scoped_rules.py`.

| mode | order | shape |
|---|---|---|
| `--self-test` | `main` then `self_test` | line 1 `counter sha256 <64hex>` (`:2508`, no `; rev`); optional `FAIL …` (`:1280`); last line `self-test: N failure(s) over M assertions` (`:2487`) |
| `--rev` | `main` | line 1 `summary_line` (`:2548`); line 2 `counter sha256 <hex>; rev <rev>` (`:2549`); `reject <client>: …` for unbacked rows (`:2556`) |
| `--rev --fetch` | same | line 1 `scoped rule files backed on committed snapshots S of K; found on the live page F of K` (`:1233-1236`); rejects skip rows that are backed and found (`:2551-2554`) |
| `--rev` without `--fetch` | same | line 1 `scoped rule files backed on committed snapshots S of K; live not run` (`:1237-1238`); exit is always 1 (`predicate`, `:1245-1249`) |
| `--json` | after the text lines | one JSON object keys `backed`, `of`, `found`, `target`, `receipt`, `clients` (`:2557-2560`). No lane caller passes `--json` (the flag appears only in this file's usage string and the two round-60 draft copies under `.ufo/waves/round-60/w0/`). |
| `TARGET is None` | after JSON if any | `target not frozen` (`:2561-2562`) |
| could not evaluate | stderr | `could-not-evaluate: …`, exit 2 (`:2503`, `:2513`, `:2530`) |

`RECEIPT = "C1 predicate: --fetch exit 0 (F>=TARGET)"` (`:259`) is pinned by the self-test (`:1538-1539`) and copied into the JSON `receipt` field. No other gate reads that string. The r61 predicate sentence is the worlds line plus the two exit checks, not a replacement of `RECEIPT`. Replacing `RECEIPT` without moving `:1538-1539` fails `--self-test`.

## Executable readers

### 1. The counter's own self-test (breaks if the summary line moves)

These asserts compare exact strings. A worlds line inserted as `lines[0]` of `--rev` / `--fetch`, or a rewrite of `summary_line()`, fails them until they are edited in the same change.

| site | what it pins |
|---|---|
| `:1532-1536` | `summary_line(True, 0, 0, 0)` and `summary_line(False, 2, 7, 0)` |
| `:1537` | `reject Cursor: a; b` |
| `:1538-1539` | `RECEIPT` text above |
| `:2314-2317` | satisfying world: `lines[0]` is `… 4 of 4; found on the live page 4 of 4`; `lines[1]` is `counter sha256 <own>; rev <measured>` |
| `:2325` | working-tree junk does not change `lines[0]` |
| `:2332-2335` | live key miss: exit 1 and `… 4 of 4; found on the live page 3 of 4` |
| `:2351-2353` | HTTP 404: `… 4 of 4; found on the live page 0 of 4` |
| `:2363-2365` | curl failure: same `0 of 4` live count |
| `:2414-2416` | broken world: `… 3 of 4; found on the live page 3 of 4` |
| `:2478-2480` | v2 re-open world: `… 3 of 3; found on the live page 3 of 3` |

Nothing in `self_test()` captures the `--self-test` process stdout, so an **extra** print of `worlds reject 7 of 7; eligible rows pass 4 of 4` inside `self_test()` (before or after `:2487`) does not fail an existing assert. Replacing `:2487` does not fail an existing assert either, and no external gate reads that line today (next section). Keep `:2487` anyway: it is the shape every floored sibling uses, and a later floor row would need it.

### 2. `verifiers/check_gate_registry.py` — row cells, not stdout

Does not run this counter and does not read its summary. Universe is top-level `verifiers/*.py` and `verifiers/*.sh` blobs only (`Tree.universe`, `ls-tree` of `verifiers/` without `-r`, `:118-129`). Exactly one `## Gate registry` row whose name cell, backticks stripped and lower-cased, equals `verifiers/check_scoped_rules.py` (`:227-234`). Current row, `SKILL.md:486`:

```
| `verifiers/check_scoped_rules.py` | gate | `python3 -B verifiers/check_scoped_rules.py --rev <rev> --fetch` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | self-test repos under `$TMPDIR` (removed); `--fetch` reads the network | kotoba |
```

`judge_row` (`:178-224`) will reject a "v3 note" that does any of these:

- Puts a raw `|` in any cell (`cells()` splits on `|`, `:139-143`). A worlds-line note must not contain `|`.
- Drops `verifiers/check_scoped_rules.py` from the entry-command cell (`:183-184`).
- Drops `0=clean` or `1=failed`, or repeats a numeric code (`PAIR_RE` at `:74`, checks `:185-192`). Extra prose in the verdict cell is otherwise ignored. The infoless-fences row (`SKILL.md:487`) already carries a prose tail after `2=could-not-evaluate` and stays one pair-set.
- Changes the self-test cell so it has no backticked `--flag`, or backticks a flag that is not an exact `add_argument` string (`FLAG_RE` `:75`, `has_flag_handler` `:78-90`). `` `--self-test` `` must remain. Do not backtick `--worlds` or `--fetch` in that cell unless v3 adds that exact `add_argument`.
- Changes pinned-values away from the exact token `in-file` without naming a backticked path that exists at the measured rev (`:209-219`).
- Empties the write-scope cell (`:220-221`).
- Changes owner away from `kotoba` (`:222-223`).
- Adds a second row for the same path, or adds a new top-level `verifiers/*.py` / `*.sh` (a worlds helper, a fixture runner) without its own conformant row. Nested `verifiers/fixtures/` blobs are outside the universe.

A worlds sentence in the write-scope cell, with no extra `|` and no new backticked flag, does not fail this gate. The summary-line grammar is not in the row.

### 3. `verifiers/check_assertion_floors.py` + `verifiers/floors-registry.json` — not a reader

`INSTRUMENTS` (`check_assertion_floors.py:191-220`) has 14 rows. `floors-registry.json` has `"instrument_total": 14` and the same 14 paths. `check_scoped_rules.py` is in neither. The guard reruns only those paths with `--self-test` and `re.search`es a per-row pattern (`:599-610`). A miss counts as 0 assertions and fails the floor.

Conditional, only if the L1 adds a floor row in the same integration (the plan's "registry/index" commit does not name `floors-registry.json`):

- Pattern siblings use is `self-test:\s*(\d+) failure\(s\) over (\d+) assertions` (group 2 = assertions, group 1 = failures). `re.search` allows an extra worlds line **as long as `:2487` remains**.
- Replacing `:2487` with only `worlds reject 7 of 7; eligible rows pass 4 of 4` makes a new floor row fail (no match → 0 assertions).
- A worlds-only pattern would be a new regex, and the bump-in-step rule in `floors-registry.json` `$comment` requires the JSON, both in-file tables, and the guard docstring together. This seat does not recommend adding the floor; the r60 receipt records 318 assertions (`freeze2-selftest.txt`) and that count is not floored.

### 4. `verifiers/check_could_not_evaluate.py` — not a reader

`GATES` (`:92-108`) is 13 names. `check_scoped_rules.py` is not among them. The S control (`:173`) checks `--self-test` **exit 0** for those 13 only; it does not parse their stdout. Changing this counter's summary or adding a worlds line does not move that gate.

### 5. `verifiers/check_routed_repairs.py` — not a reader of this counter

R-a..R-f (`:20-32`, `:69-110`) look at `LOG.md`, `corpus/QUALITY.md`, `corpus/lessons/round-61.md`, census-after, and controls-ancestry. R-c requires one LOG line containing both `receipts/freeze2-selftest.txt` and `C1-measure.txt`. It does not run `check_scoped_rules.py` and does not match `scoped rule files backed` or `worlds reject`. Its own self-test line is `self-test: N failure(s)` (`:210`), a different grammar; do not copy that shape onto the scoped-rules counter.

No other file under `verifiers/` names `check_scoped_rules` (grep of `verifiers/` hits only `check_scoped_rules.py` itself).

## Invocations that are not gates

These cite the command or paste historical stdout. None re-parse a future run.

| path | what it holds |
|---|---|
| `.ufo/waves/round-60/receipts/freeze2-selftest.txt:5,9` | v2 self-test `self-test: 0 failure(s) over 318 assertions`; non-fetch `scoped rule files backed on committed snapshots 0 of 0; live not run` |
| `.ufo/waves/round-60/receipts/freeze-selftest.txt:5,8` | v1, 302 assertions, same non-fetch line |
| `.ufo/waves/round-60/C1-measure.txt` | `--fetch` `4 of 4` / `found on the live page 4 of 4`, exit 0; non-fetch exit 1 |
| `.ufo/waves/round-60/controls/*.md`, `controls/SUMMARY.md`, `controls-v2/` | pasted v1/v2 stdout; not inputs to a counter |
| `.ufo/waves/round-60/receipts/noharm-base-selftests.txt` | registry self-test sweep at a pre-counter rev; this script is absent from that table |
| `corpus/lessons/round-60-verifier-spotcheck.md:42-46` | closure record of the digest, the `0 of 0; live not run` line, and `318` assertions. Historical. Do not rewrite to the worlds sentence. |
| `corpus/README.md:102` and `:182` | index / frontier prose naming the command, not the summary grammar |
| `corpus/knowledge/scoped-rules-round60.md:4` | `recheck: python3 -B verifiers/check_scoped_rules.py --rev <rev> --fetch` (command only) |
| `LOG.md:2528`, `SCORECARD.md:28`, `plans/round-60.md` | round-60 claim text quoting the v2 command and, in LOG, the `4 of 4` summary |
| `.ufo/waves/round-61/wave-spec.json` / `wave-dispatch.json` | this wave's prompts, including ScribeRegistry's instruction to note v3 on the SKILL row |

`plans/round-61.md:50-54` is the new required print. It is not a parser.

## What the L1 should land so nothing else goes red

1. On `--self-test`, print `worlds reject 7 of 7; eligible rows pass 4 of 4` **and** keep `self-test: N failure(s) over M assertions` as its own line. Do not use the routed-repairs shorter form.
2. Leave `--rev` / `--fetch` line 1 as `summary_line()` and line 2 as `counter sha256 <hex>; rev <rev>` unless every assert in the table above moves in the same edit. The r61 predicate does not ask for a new live summary.
3. If the SKILL registry row is annotated, obey the cell rules in §2. No raw `|`. Keep `` `--self-test` ``, `in-file`, `0=clean`, `1=failed`, the path in the entry cell, and owner `kotoba`.
4. Do not add a top-level `verifiers/*.py` without a conformant registry row. Do not add a floors row unless `:2487` stays and the bump-in-step rule is followed. Not required for C1.
5. Do not retarget `RECEIPT` unless `:1538-1539` and the plan sentence are updated together. The worlds line is not that label.
6. Leave round-60 receipts and `round-60-verifier-spotcheck.md` as records of v2 output.

## Not verified

This seat did not run `check_scoped_rules.py`, `check_gate_registry.py`, or `check_assertion_floors.py`. The "would exit 1" claims are from the asserts and `judge_row` as read, not from an executed mutant. No fleet-repo `scripts/` walk; the lane has no `scripts/` directory. `--json` has no in-lane caller; an out-of-tree caller that `json.loads` the whole stdout would already fail today because text lines precede the JSON.

installs: no installs
blockers: none
Attacked: readers of `verifiers/check_scoped_rules.py` stdout and the SKILL registry row, for a v3 summary-line or worlds-line change.
