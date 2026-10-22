Result: DONE — 15 single-rule mutants were probed; 11 were killed and 4 survived, and the verifier was restored byte-for-byte.

## Detector and restoration

Target: `e33715486a45a4a857b64c30e6b695f7995858b8`, isolated clone under `/fast/scratch/hyaku/kotoba-r54/MutDescThresholds`.

Baseline command: `python3 -B /fast/scratch/hyaku/kotoba-r54/MutDescThresholds/verifiers/check_description_thresholds.py --self-test` → exit 0; `self-test: 0 failure(s) over 22 assertions`.

The same `--self-test` command was run once for each mutant, then again after restoring that single changed line. Every restored run reported exit 0 and `self-test: 0 failure(s) over 22 assertions`. The initial and final `sha256sum` for the target file were both `4edad582973786a8b46c7a948edc5ec8f7df7e6911d6ea7e982e7834a8e32aa0`. The source remains unchanged in the scratch clone; only the requested report and patch were written in the lane.

## Mutation outputs

All rows used `python3 -B .../check_description_thresholds.py --self-test`; the output below is the observed output, with its exit code.

| Mutant (target rule) | Observed output | Exit | Verdict |
|---|---|---:|---|
| Opened date check skipped (`:282`) | `FAIL source opened another day fails: got ['Claude Code', 'Codex'], expected ['Codex']`; `self-test: 1 failure(s) over 22 assertions` | 1 | Killed |
| Tier-A check skipped (`:276`) | `FAIL tier B fails: got ['Claude Code', 'Codex'], expected ['Codex']`; `self-test: 1 failure(s) over 22 assertions` | 1 | Killed |
| Kind whitelist skipped (`:278`) | `self-test: 0 failure(s) over 22 assertions` | 0 | Survived |
| Mined-status check skipped (`:280`) | `FAIL status queued fails: got ['Claude Code', 'Codex'], expected ['Codex']`; `self-test: 1 failure(s) over 22 assertions` | 1 | Killed |
| Used-by check skipped (`:284`) | `FAIL used-by without the entry fails: got ['Claude Code', 'Codex'], expected ['Codex']`; `self-test: 1 failure(s) over 22 assertions` | 1 | Killed |
| Host-pin condition removed (`:288`) | `FAIL off-host URL fails: got ['Claude Code', 'Codex'], expected ['Codex']`; `self-test: 1 failure(s) over 22 assertions` | 1 | Killed |
| Quote word-count condition skipped (`:294`) | `self-test: 0 failure(s) over 22 assertions` | 0 | Survived |
| Gate quote equality skipped (`:298`) | `FAIL quote not recorded in the Gate fails: got ['Claude Code', 'Codex'], expected ['Codex']`; `FAIL Gate fragment does not stand for the quote: got ['Claude Code', 'Codex'], expected ['Codex']`; `self-test: 2 failure(s) over 22 assertions` | 1 | Killed |
| Number-token whole-match weakened to substring (`:220`) | `FAIL partial number token 1,53 does not match 1,536: got ['Claude Code', 'Codex'], expected ['Codex']`; `FAIL number 536 inside 1,536 is not a whole token: got ['Claude Code', 'Codex'], expected ['Codex']`; `self-test: 2 failure(s) over 22 assertions` | 1 | Killed |
| Action-cell check skipped (`:257`) | `FAIL empty action cell fails: got ['Claude Code', 'Codex'], expected ['Codex']`; `self-test: 1 failure(s) over 22 assertions` | 1 | Killed |
| Duplicate SKILL rows allowed (`:250`) | `FAIL duplicate SKILL row fails: got ['Claude Code', 'Codex'], expected ['Codex']`; `self-test: 1 failure(s) over 22 assertions` | 1 | Killed |
| Duplicate entry rows allowed (`:260`) | `FAIL duplicate entry row fails: got ['Claude Code', 'Codex'], expected ['Claude Code']`; `self-test: 1 failure(s) over 22 assertions` | 1 | Killed |
| Heading comparison made case-insensitive (`:148`) | `self-test: 0 failure(s) over 22 assertions` | 0 | Survived |
| Header anchor reduced to first cell (`:162`) | `FAIL wrong SKILL header is not read: got ['Claude Code', 'Codex'], expected []`; `self-test: 1 failure(s) over 22 assertions` | 1 | Killed |
| Target changed from 4 to 2 (`:81`) | `self-test: 0 failure(s) over 22 assertions` | 0 | Survived |

Rule locations are in `verifiers/check_description_thresholds.py`; the full contract is also stated in its docstring at lines 19–44. The existing self-tests are at lines 307–388.

## Self-test cases for survivors

These are the added self-test arms in `.ufo/waves/round-54/build/MutDescThresholds.patch`. Each is designed to fail for the corresponding surviving mutant.

```python
check("unsupported source kind fails",
      backed(so=sources.replace("| docs | A |", "| note | A |", 1)), ["Codex"])
```

```python
overlong_quote = '"text is truncated at 1,536 characters in the skill listing ' + "w " * 16 + '"'
check("26-word quote fails when Gate records the full quote",
      backed(
          en=entry.replace('"text is truncated at 1,536 characters in the skill listing"', overlong_quote),
          le=lesson.replace('"text is truncated at 1,536 characters in the skill listing"', overlong_quote)),
      ["Codex"])
```

```python
check("heading case must be exact",
      backed(sk=skill.replace("### Description thresholds by client",
                              "### description thresholds by client")), [])
```

```python
check("target remains pinned at four", TARGET, 4)
```

The patch contains only additions to `self_test()`; no judging logic was changed. It was not applied or executed, leaving the L1 to decide whether post-freeze self-test additions are allowed.
