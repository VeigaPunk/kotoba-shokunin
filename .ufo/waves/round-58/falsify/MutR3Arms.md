Result: MIXED — three of eight new mutants survived --self-test; five were killed, and all eight were restored byte-exactly.

# Scope and detector
- Seat: KotobaR58.MutR3Arms; R3 repair operability only. No C1 or round-level judgment.
- Content revision: `46b4a7061c688cefd3e3ec9cbb655130ba1aafbe`.
- Isolated clone and command cwd: `/fast/scratch/hyaku/kotoba-r58/MutR3Arms`.
- Axes: behavioral self-test sensitivity; sandbox isolation; exact restoration.
- Clone/check-out command (exit 0, no stdout/stderr):

```sh
timeout 90 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r58/MutR3Arms && timeout 90 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /fast/scratch/hyaku/kotoba-r58/MutR3Arms checkout -q 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe
```
- Same detector for every pristine, mutated and restored phase (24 runs total):

```sh
timeout 30 python3 -B verifiers/check_correction_sweep.py --self-test
```
- Every detector inherited an environment with `GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE` removed, `TMPDIR=/fast/scratch/hyaku/kotoba-r58/MutR3Arms`, and `PYTHONDONTWRITEBYTECODE=1`. All temporary fixtures, shims and frozen-counter repositories therefore remained inside this sandbox; runs were sequential.
- Each mutant was applied alone with a surgical edit, tested, then reverted before the restored test and the next pristine test. No mutant was stacked.
- Pristine/restored target (`verifiers/check_correction_sweep.py`), 18,199 bytes: **B = `df66b485cc00a5058643b387882abe648d6e83b66d68a5865596e88515309c2f`** (SHA-256). Each restored phase also compared equal to the original byte string, not merely its hash.
- Novelty checked against all 16 rows in the requested lane catalogue `.ufo/waves/round-58/sweep-mutants.json` (SHA-256 `cf2fa97a7a385a00aab60e52a58211982e80c7194d6ddd3de751e2f144d6bfbf`): none of the eight old/new transformations appears there. The frozen catalogue and counters were not edited.

# Findings: survivors
1. **N01 — r53 correction specificity is not tested.** At `verifiers/check_correction_sweep.py:51-53`, shortening the dated correction pattern to `round-53` survives: exit 0, `0 failure(s) over 25 assertions`. The r53 semantic cases at `:214-220` supply either no correction label or the complete correction. [INFERENCE] They cannot distinguish a mere round label from the required dated correction; a stale statement carrying only `round-53` would be accepted by this mutant.
2. **N02 — the r53 corrected file count can be erased undetected.** At `verifiers/check_correction_sweep.py:58-61`, replacing `held 17 `AGENTS\.md` files` with `files` survives: exit 0, `0 failure(s) over 25 assertions`. The stale pattern itself contains `files`. [INFERENCE] This mutant therefore treats that stale statement as its own declaration, without the corrected count. The r53 fixture block at `:212-228` exercises semantics and the baseline pointer, not this six-file row.
3. **N07 — table-row isolation has no discriminating arm.** Removing the `\|` new-item alternative at `verifiers/check_correction_sweep.py:103` survives: exit 0, `0 failure(s) over 25 assertions`. [INFERENCE] Adjacent table rows now accumulate in the same `cur` block (`:104-117`), so a declaration in a different row can satisfy the stale row. The existing cross-block negative at `:199-205` is a list-item case, not a neighboring-table-row case.

These are coverage findings, not changes to the correction contract, frozen counter, rules, targets or withdrawn C2 status. Distinguishing stimuli for the L1 are: an r53 bare-round negative, an r53 six-file stale-only negative, and a two-row table with the declaration only in the other row. No repair was integrated.

# Results and hashes
All pristine/restored phases exited 0 and printed exactly `0 failure(s) over 25 assertions` with empty stderr. No baseline was inconclusive; no run timed out. B below is the full pristine SHA-256 defined above.

| Mutant | Pristine exit/hash | Mutated exit | Verdict | Restored exit/hash | Mutated SHA-256 |
|---|---|---:|---|---|---|
| N01 | 0 / B | 0 | SURVIVED | 0 / B | `c98fad189d6d542b6bdde3419851939cf54e537c9622acd127b21407db51653d` |
| N02 | 0 / B | 0 | SURVIVED | 0 / B | `cb2ed0ccafa17fb4557a67e1cf19708dfd422df0a0fbd0d13b9a45bc2c6f7533` |
| N03 | 0 / B | 1 | KILLED | 0 / B | `f9c3fb894e14776652ba8083aa8ae04be0e3b82384b9f17c10808942f11c4ebb` |
| N04 | 0 / B | 1 | KILLED | 0 / B | `45c6d09bfc0559e7db8dcf7cd5202fe75c73fe4193ee4baa9ec76428920db3c9` |
| N05 | 0 / B | 1 | KILLED | 0 / B | `638a77df92c8232e0a8e1bc60235757d425d03d6a561df033607250a1d19d009` |
| N06 | 0 / B | 1 | KILLED | 0 / B | `0da4ee41e94130db7ae0c535fccae3413daf895f166f6e082460b79a35282c07` |
| N07 | 0 / B | 0 | SURVIVED | 0 / B | `492bc566ee3d631d2bfec676b123696e4eff70de0759a29713ac8d926ec0e3e3` |
| N08 | 0 / B | 1 | KILLED | 0 / B | `144795aeee7de8cd27a030776e8da51206bbc02fbbe67cb69fd3049fb7538df6` |

## Per-phase UTC receipts

| Mutant | Pristine UTC | Mutated UTC | Restored UTC |
|---|---|---|---|
| N01 | 2026-10-23T08:26:40.041405+00:00 | 2026-10-23T08:26:45.379594+00:00 | 2026-10-23T08:26:52.846523+00:00 |
| N02 | 2026-10-23T08:26:53.001601+00:00 | 2026-10-23T08:27:08.564669+00:00 | 2026-10-23T08:27:14.321637+00:00 |
| N03 | 2026-10-23T08:27:14.498890+00:00 | 2026-10-23T08:27:22.243704+00:00 | 2026-10-23T08:27:28.209931+00:00 |
| N04 | 2026-10-23T08:27:28.385184+00:00 | 2026-10-23T08:27:33.363332+00:00 | 2026-10-23T08:27:39.362043+00:00 |
| N05 | 2026-10-23T08:27:39.509724+00:00 | 2026-10-23T08:27:44.739111+00:00 | 2026-10-23T08:28:05.311983+00:00 |
| N06 | 2026-10-23T08:28:05.452159+00:00 | 2026-10-23T08:28:11.092850+00:00 | 2026-10-23T08:28:17.041801+00:00 |
| N07 | 2026-10-23T08:28:17.179730+00:00 | 2026-10-23T08:28:22.428364+00:00 | 2026-10-23T08:28:28.600150+00:00 |
| N08 | 2026-10-23T08:28:28.761592+00:00 | 2026-10-23T08:28:36.674101+00:00 | 2026-10-23T08:28:43.955313+00:00 |

## Exact mutation definitions and observed mutant output

All line references are against the pristine content revision. Each expected detector is the same bounded `--self-test` command above; a covered behavioral defect should produce a nonzero exit. These are eight independent transformations, not one cumulative patch.

### N01 — Weaken r53 Claude-MD declared correction to a bare round label

Target: `verifiers/check_correction_sweep.py:53`. Expected discrimination: A bare round-53 label without the declared dated correction must still be rejected.

Before (N01 includes its row-id context to identify one of two identical declared lines):

```python
    {"id": "r53-c2-claudemd-semantics", "file": "corpus/knowledge/claude-md-surface.md",
     "stale": r"Same load semantics as AGENTS\.md",
     "declared": r"round-53 correction \(2026-10-22\)", "lead": False},
```

After:

```python
    {"id": "r53-c2-claudemd-semantics", "file": "corpus/knowledge/claude-md-surface.md",
     "stale": r"Same load semantics as AGENTS\.md",
     "declared": r"round-53", "lead": False},
```

Observed detector exit: **0**; verdict: **SURVIVED**. Stdout, verbatim:

```text
0 failure(s) over 25 assertions
```

Stderr: empty.

### N02 — Weaken r53 six-file declared result to files

Target: `verifiers/check_correction_sweep.py:61`. Expected discrimination: The stale six-file statement without held 17 AGENTS.md files must still be rejected.

Before:

```python
     "declared": r"held 17 `AGENTS\.md` files", "lead": False},
```

After:

```python
     "declared": r"files", "lead": False},
```

Observed detector exit: **0**; verdict: **SURVIVED**. Stdout, verbatim:

```text
0 failure(s) over 25 assertions
```

Stderr: empty.

### N03 — Disable lead on the SCORECARD registry row

Target: `verifiers/check_correction_sweep.py:35`. Expected discrimination: The existing red scorecard fixtures must detect a declared result placed after the stale headline.

Before:

```python
     "stale": r"`7 of 7`, exit 0 @ `34cfffbb`", "declared": r"4 of 7", "lead": True},
```

After:

```python
     "stale": r"`7 of 7`, exit 0 @ `34cfffbb`", "declared": r"4 of 7", "lead": False},
```

Observed detector exit: **1**; verdict: **KILLED**. Stdout, verbatim:

```text
2 failure(s) over 25 assertions
FAIL red both: got ['r51-c2-readme corpus/README.md:1 stale claim without the declared result']
FAIL declared after the stale lead fails: got []
```

Stderr: empty.

### N04 — Delete the new round-58 R2 README registry row

Target: `verifiers/check_correction_sweep.py:82-84`. Expected discrimination: r58 readme plugin sources red must report r58-r2-readme-plugin-sources.

Before:

```python
    {"id": "r58-r2-readme-plugin-sources", "file": "corpus/README.md",
     "stale": r"the plugin half is recorded, not held as a verified claim",
     "declared": r"S086–S088", "lead": False},
```

After: **delete only the block above**.

Observed detector exit: **1**; verdict: **KILLED**. Stdout, verbatim:

```text
1 failure(s) over 25 assertions
FAIL r58 readme plugin sources red: got []
```

Stderr: empty.

### N05 — Delete the new round-58 R2 red case, retaining the expected-case guard

Target: `verifiers/check_correction_sweep.py:263-264`. Expected discrimination: The expected-case guard must reject the missing red arm.

Before:

```python
    case("r58 readme plugin sources red", r57_note, "| d | 9 | x |\n",
         ["r58-r2-readme-plugin-sources"])
```

After: **delete only the block above**.

Observed detector exit: **1**; verdict: **KILLED**. Stdout, verbatim:

```text
1 failure(s) over 24 assertions
FAIL cases run ['correction in another block is not a correction', 'declared after the stale lead fails', 'green both', 'no stale claim: clean', 'r52 silent negative with S041 passes', 'r52 silent negative without S041 fails', 'r53 baseline pointer green', 'r53 baseline pointer red', 'r53 claude-md semantics green', 'r53 claude-md semantics red', 'r57 quote notes green', 'r57 quote notes red', 'r57 singular agent clause green', 'r57 singular agent clause red', 'r58 readme plugin sources green', 'r58 s076 bare round red', 'r58 s078 bare round red', 'r58 singular bare path red', 'r58 singular wrong line red', 'red both'], expected ['correction in another block is not a correction', 'declared after the stale lead fails', 'green both', 'no stale claim: clean', 'r52 silent negative with S041 passes', 'r52 silent negative without S041 fails', 'r53 baseline pointer green', 'r53 baseline pointer red', 'r53 claude-md semantics green', 'r53 claude-md semantics red', 'r57 quote notes green', 'r57 quote notes red', 'r57 singular agent clause green', 'r57 singular agent clause red', 'r58 readme plugin sources green', 'r58 readme plugin sources red', 'r58 s076 bare round red', 'r58 s078 bare round red', 'r58 singular bare path red', 'r58 singular wrong line red', 'red both']
```

Stderr: empty.

### N06 — Delete the new round-58 R2 green case, retaining the expected-case guard

Target: `verifiers/check_correction_sweep.py:265-267`. Expected discrimination: The expected-case guard must reject the missing green arm.

Before:

```python
    case("r58 readme plugin sources green",
         r57_note + "Round 58 correction: the entry also rests on S086–S088 (correction rows).\n",
         "| d | 9 | x |\n", [])
```

After: **delete only the block above**.

Observed detector exit: **1**; verdict: **KILLED**. Stdout, verbatim:

```text
1 failure(s) over 24 assertions
FAIL cases run ['correction in another block is not a correction', 'declared after the stale lead fails', 'green both', 'no stale claim: clean', 'r52 silent negative with S041 passes', 'r52 silent negative without S041 fails', 'r53 baseline pointer green', 'r53 baseline pointer red', 'r53 claude-md semantics green', 'r53 claude-md semantics red', 'r57 quote notes green', 'r57 quote notes red', 'r57 singular agent clause green', 'r57 singular agent clause red', 'r58 readme plugin sources red', 'r58 s076 bare round red', 'r58 s078 bare round red', 'r58 singular bare path red', 'r58 singular wrong line red', 'red both'], expected ['correction in another block is not a correction', 'declared after the stale lead fails', 'green both', 'no stale claim: clean', 'r52 silent negative with S041 passes', 'r52 silent negative without S041 fails', 'r53 baseline pointer green', 'r53 baseline pointer red', 'r53 claude-md semantics green', 'r53 claude-md semantics red', 'r57 quote notes green', 'r57 quote notes red', 'r57 singular agent clause green', 'r57 singular agent clause red', 'r58 readme plugin sources green', 'r58 readme plugin sources red', 'r58 s076 bare round red', 'r58 s078 bare round red', 'r58 singular bare path red', 'r58 singular wrong line red', 'red both']
```

Stderr: empty.

### N07 — Remove the table-row alternative from blocks() new-item recognition

Target: `verifiers/check_correction_sweep.py:103`. Expected discrimination: A declaration in another table row must not cure the stale row; a multirow negative fixture should kill this change.

Before:

```python
        new_item = bool(re.match(r"^(?:[-*] |\d+\. |\|)", ln)) or ln.startswith("#")
```

After:

```python
        new_item = bool(re.match(r"^(?:[-*] |\d+\. )", ln)) or ln.startswith("#")
```

Observed detector exit: **0**; verdict: **SURVIVED**. Stdout, verbatim:

```text
0 failure(s) over 25 assertions
```

Stderr: empty.

### N08 — Invert the declared-before-stale comparison

Target: `verifiers/check_correction_sweep.py:132`. Expected discrimination: The existing positive and negative lead-order fixtures must detect the reversed ordering.

Before:

```python
            if not d or (e["lead"] and d.start() > m.start()):
```

After:

```python
            if not d or (e["lead"] and d.start() < m.start()):
```

Observed detector exit: **1**; verdict: **KILLED**. Stdout, verbatim:

```text
4 failure(s) over 25 assertions
FAIL red both: got ['r51-c2-readme corpus/README.md:1 stale claim without the declared result']
FAIL green both: got ['r51-c2-scorecard-lead SCORECARD.md:1 stale claim without the declared result leading']
FAIL correction in another block is not a correction: got ['r51-c2-readme corpus/README.md:1 stale claim without the declared result', 'r51-c2-scorecard-lead SCORECARD.md:1 stale claim without the declared result leading']
FAIL declared after the stale lead fails: got []
```

Stderr: empty.

# Frozen catalogue rerun — record only
The pre-existing C2 counter remains withdrawn (`plans/round-58.md:86-95`). This observation is not offered as a claim or as evidence that the broader repair is fully covered.

```sh
timeout 180 python3 -B verifiers/check_sweep_mutants.py --rev 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe
```

Started UTC: `2026-10-23T08:29:03.242225+00:00`; cwd/environment as above. Counter SHA-256: `f7664401095948fd84889de1767e4fa6a32b7dc25cb50f49de2c981543d3241f`. Observed exit: **0**. Stdout, verbatim:

```text
M01 mutant killed exit=1
M02 mutant killed exit=1
M03 mutant killed exit=1
M04 mutant killed exit=1
M05 mutant killed exit=1
M06 mutant killed exit=1
M07 mutant killed exit=1
M08 mutant killed exit=1
M09 mutant killed exit=1
M10 mutant killed exit=1
M11 mutant killed exit=1
E1 equivalent survived exit=0
E2 equivalent survived exit=0
E3 equivalent survived exit=0
E4 equivalent survived exit=0
E5 equivalent survived exit=0
sweep mutants killed 11 of 11; equivalents survived 5 of 5
```

Stderr: empty.

# Restoration and write-scope evidence
- Each of the eight restored runs observed SHA-256 B (`df66b485cc00a5058643b387882abe648d6e83b66d68a5865596e88515309c2f`), an exact comparison to the original 18,199 bytes, exit 0 and the original 25-assertion output.
- After the frozen rerun, target SHA-256 remained `df66b485cc00a5058643b387882abe648d6e83b66d68a5865596e88515309c2f`; exact original-byte comparison was `True`.
- Mutations were confined to the assigned sandbox target. No sibling source, lane source, lane Git index, jj state, frozen catalogue, frozen counter or fleet state was changed. This report is the only lane write. No sandbox commits or pushes were made.
- No external sources were fetched; no client/model CLI or other agent runtime was invoked. No tools were installed or updated.
