Result: DONE — all 10 surviving counter mutants kept the landed tip passing and all 21 reachable C1 control worlds failing; M04 changed only K, while a later Cursor HTTP 403 reduced counts on both mutated and restored bytes.

## Scope and detector

Axes: C1 depth/provenance discrimination, counter sensitivity, live-source availability, and exact-byte restoration. This report attacks only the ten survivors identified in `.ufo/waves/round-58/build/MutC1Counter.md:264-1238`. It does not adjudicate C1, integrate a change, alter the frozen counter/rules/targets, score withdrawn C2, or invoke another runtime.

Read-only lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. All execution, mutations, temporary repositories, HTTP captures, and Git writes were confined to `/fast/scratch/hyaku/kotoba-r58/MutC1Survivors`. The only lane write is this requested report. No subagents, client model calls, browser/challenge bypass, installs, or tool updates. Existing Python: `timeout 10 python3 --version` exited 0 and printed `Python 3.14.8`.

Setup, exit 0, no output:

```sh
timeout 120 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r58/MutC1Survivors && timeout 120 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /fast/scratch/hyaku/kotoba-r58/MutC1Survivors checkout -q 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe
```

Each mutant is exactly the original report's single-line substitution, with the identical mutated SHA-256. The working counter was not committed. All world documents are read by `--rev`; checking out each control is unnecessary. Control objects were read-only-fetched from their report-named sandbox clones into this clone's `refs/sandbox/controls/<group>/<name>`; all five fetch commands exited 0. Each source commit was first checked with `timeout 15 git --no-optional-locks -C <origin> cat-file -t <rev>`: all exited 0 and printed `commit`. No control needed rebuilding.

**Expected detector:** run the same `--self-test` and live-fetch score suite on pristine (P), one-mutant (M), and exactly restored (R) bytes. A failed self-test, tip exit changing from 0, or a control exit changing from 1 is a kill by this bounded verdict detector. K-only changes are diagnostics, not a bypass of F/G. A network-driven score change is not credited as killing a mutant. The immediately preceding restoration suite also supplies the next mutant's pristine suite; this is explicit reuse of the same actual invocation, not a fabricated rerun.

Actual score command for every world, cwd the isolated clone:

```sh
timeout 180 python3 -B verifiers/check_command_files.py --rev <full-world-revision> --fetch
```

Actual self-test command in each suite:

```sh
timeout 180 python3 -B verifiers/check_command_files.py --self-test
```

Each suite was invoked as `timeout 800 python3 -B .probe/probe.py <stage> <expected-counter-sha256>` (21 commands, all exit 0). At most four ordinary scoring commands ran concurrently; there was no contention/load probe. Child environments removed `GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE`, set `PYTHONDONTWRITEBYTECODE=1`, and kept `TMPDIR` in `.probe/tmp`. Every child had a 180-second timeout and a 185-second parent deadline. No timeout occurred.

`PYTHONPATH=.probe/audit` supplied the same passive `sitecustomize.py` receipt hook for all stages. It delegates the original `urllib.request.urlopen` request/timeout/redirect handling, returns the original read bytes unchanged, and saves only bytes the counter already consumed. There is no cache, alternate source, quote rewriting, response stub, or change to the counter's `fetch` function. This is instrumentation, not a second mutant. Full code: `.probe/audit/sitecustomize.py:1-61`; runner: `.probe/probe.py:1-91`. Every actual request has its requested/final URL, literal `date -u` output, HTTP status, consumed byte count, hash and raw-body path in that stage/world's `http/requests.jsonl`. HTTP-error bodies were not consumed; their body/hash are explicitly unavailable.

Observed totals: **21 suites; 462 live-fetch scores plus 21 self-tests = 483 counter invocations**. Every self-test exited 0 and printed `self-test: 0 failure(s) over 244 assertions`; every tip score exited 0; all 441 control scores exited 1. All 483 stderr strings were empty. Scoring dates ran from `Fri Oct 23 08:29:00 AM UTC 2026` through `Fri Oct 23 08:34:18 AM UTC 2026`.

## World identities and reachability

Paths in the remaining report beginning `.probe/` are relative to the isolated clone, not the lane. The landed content revision is `46b4a7061c688cefd3e3ec9cbb655130ba1aafbe`. Every C-row revision below is an explicitly labelled **sandbox** identity, imported without rebuilding its documents. Its command/output revision uses that same identity.

| ID | Origin report / world | Imported identity |
|---|---|---|

| C01 | `CtlC1DoNothing.md` / `base` | sandbox f56f6e191762c27c1aa2af11a204db9e2ca4edec (/fast/scratch/hyaku/kotoba-r58/MutC1Survivors) |

| C02 | `CtlC1DoNothing.md` / `counters_only` | sandbox 3de87aad29e960c95ed35840442f424c48c29729 (/fast/scratch/hyaku/kotoba-r58/MutC1Survivors) |

| C03 | `CtlC1DoNothing.md` / `empty_table` | sandbox ebc9e9947085d5b77f895e168efb31994d8d7ccc (/fast/scratch/hyaku/kotoba-r58/MutC1Survivors) |

| C04 | `CtlC1Fabricated.md` / `fabricated` | sandbox 6a3f2d35ee73014dcafb445a21c73b74a26e99c5 (/fast/scratch/hyaku/kotoba-r58/MutC1Survivors) |

| C05 | `CtlC1Junk.md` / `junk_w1` | sandbox a6dae8c45a4d7c5f3f50c2822db4b633003f37e2 (/fast/scratch/hyaku/kotoba-r58/MutC1Survivors) |

| C06 | `CtlC1Junk.md` / `junk_w2` | sandbox 22669956159b03b81dac2dee2da924e08ee9e21a (/fast/scratch/hyaku/kotoba-r58/MutC1Survivors) |

| C07 | `CtlC1OffTopic.md` / `offtopic_w1` | sandbox 39903415a7ec14fc090bc59fe949b49db76a5557 (/fast/scratch/hyaku/kotoba-r58/MutC1Survivors) |

| C08 | `CtlC1OffTopic.md` / `offtopic_w2` | sandbox b5799ce55965d7879c41af980885f6420b81a790 (/fast/scratch/hyaku/kotoba-r58/MutC1Survivors) |

| C09 | `CtlC1SharedLabel.md` / `a_copilot_only_offtopic` | sandbox 9093047e690c030d1d85228799afae0fbe8fbe6e (/fast/scratch/hyaku/kotoba-r58/MutC1Survivors) |

| C10 | `CtlC1SharedLabel.md` / `a_shared_exact` | sandbox baa3870f7efb68d71d5c22d77387cfe724dc53f7 (/fast/scratch/hyaku/kotoba-r58/MutC1Survivors) |

| C11 | `CtlC1SharedLabel.md` / `a_shared_alias_misspelled` | sandbox 766911e38dc70e0ba40896db7085de93576dc92f (/fast/scratch/hyaku/kotoba-r58/MutC1Survivors) |

| C12 | `CtlC1SharedLabel.md` / `b_foreign_marker` | sandbox 0775e66751c6bc854d6e7fa954d968f5a2e7a2a0 (/fast/scratch/hyaku/kotoba-r58/MutC1Survivors) |

| C13 | `CtlC1SharedLabel.md` / `c_misspelled_names` | sandbox 14de5f157be2817b09d24d35160fde6e4a564123 (/fast/scratch/hyaku/kotoba-r58/MutC1Survivors) |

| C14 | `CtlC1SharedLabel.md` / `c_duplicated_skill_names` | sandbox 77487eb659f5b8487ddaec9e6a6ec5648cfe5923 (/fast/scratch/hyaku/kotoba-r58/MutC1Survivors) |

| C15 | `CtlC1SharedLabel.md` / `d_entry_case_mismatch` | sandbox e17d7c1bb0b116e7c7a9a6e30c67a179c130a25d (/fast/scratch/hyaku/kotoba-r58/MutC1Survivors) |

| C16 | `CtlC1SharedLabel.md` / `d_entry_added_slash` | sandbox 318a4b941160bd6ef7985a21b2db56a292d264c4 (/fast/scratch/hyaku/kotoba-r58/MutC1Survivors) |

| C17 | `CtlC1SharedLabel.md` / `d_entry_allowed_normalisation` | sandbox d567a698a60630c36f970f1bceeb48ab395acc69 (/fast/scratch/hyaku/kotoba-r58/MutC1Survivors) |

| C18 | `CtlC1SharedLabel.md` / `e_reused_base_url` | sandbox 87745a7fa9aef36db8626ffefceec2e46d6e5c95 (/fast/scratch/hyaku/kotoba-r58/MutC1Survivors) |

| C19 | `CtlC1SharedLabel.md` / `e_reused_base_url_corrected` | sandbox d215313554339b3710e92aa93064991fffe619a6 (/fast/scratch/hyaku/kotoba-r58/MutC1Survivors) |

| C20 | `CtlC1SharedLabel.md` / `c_duplicate_entry_names_corrected` | sandbox 0ccd7e5848e6daedb859f1e803914cb6d9bcafb8 (/fast/scratch/hyaku/kotoba-r58/MutC1Survivors) |

| C21 | `CtlC1SharedLabel.md` / `c_duplicate_entry_names` | sandbox fddfe2a47c83273edd0765fdeae1b8133b99b137 (/fast/scratch/hyaku/kotoba-r58/MutC1Survivors) |


All 13 SharedLabel worlds were included, including the two initial fixtures and the two corrections. The initial `c_duplicate_entry_names` hash is absent from the report's truncated embedded transcript; it is supplied by the explicitly named reproduction artifact `/fast/scratch/hyaku/kotoba-r58/CtlC1SharedLabel/control-worlds.json` (`name`/`rev` pair), and was reachable. This increases coverage rather than silently omitting that world. The other source identity pointers are `CtlC1DoNothing.md:9-13`, `CtlC1Fabricated.md:9`, `CtlC1Junk.md:7-8`, `CtlC1OffTopic.md:11-12`, and `CtlC1SharedLabel.md:194-555`. Immutable manifest: `.probe/worlds.json`.

## Per-survivor outcomes

Tuples are **F/K/G**, not F/G/K. Every P/M/R tip exit below is **0/0/0**, every control exit **1/1/1**, and every self-test exit **0/0/0**. `SURVIVED` means the requested verdict detector did not distinguish the defect; it is not a claim of equivalence or adequate coverage.

| Mutant / counter line | Defect | Tip P → M → R | Observable diagnostic / verdict |
|---|---|---|---|

| M04 / `:583` | Permit a single dot-led segment | 6/6/4 → 6/6/4 → 6/6/4 | C05 K=6 → 7 → 6, F=G=0 throughout. SURVIVED for the frozen predicate; K exposes the grammar defect. |

| M06 / `:292` | Omit plural plugins from banned words | 6/6/4 → 6/6/4 → 6/6/4 | No score or verdict change. SURVIVED. |

| M07 / `:291` | Omit singular skill from banned words | 6/6/4 → 6/6/4 → 6/6/4 | No score or verdict change. SURVIVED. |

| M08 / `:589` | Check banned words only in non-final segments | 6/6/4 → 6/6/4 → 6/6/4 | No score or verdict change. SURVIVED. |

| M09 / `:585` | Skip the first segment in the E7 dot check | 6/6/4 → 5/6/3 → 5/6/3 | Cursor HTTP 403 starts in M and persists in R; C17/C20 also lose their one Cursor count. SURVIVED for verdict; count-level causal comparison is INCONCLUSIVE, not a kill. |

| M11 / `:876` | Allow a digit directly after a quoted/page token | 5/6/3 → 5/6/3 → 5/6/3 | No score or verdict change relative to P/R. SURVIVED; Cursor fetch unavailable in all three stages. |

| M14 / `:298` | Drop word boundaries from the outside command-word regex | 5/6/3 → 5/6/3 → 5/6/3 | No score or verdict change relative to P/R. SURVIVED; Cursor fetch unavailable in all three stages. |

| M16 / `:673` | Ignore token-sharing rows with an empty client name | 5/6/3 → 5/6/3 → 5/6/3 | No score or verdict change relative to P/R. SURVIVED; Cursor fetch unavailable in all three stages. |

| M19 / `:303` | Admit a hyphen as a held left boundary | 5/6/3 → 5/6/3 → 5/6/3 | No score or verdict change relative to P/R. SURVIVED; Cursor fetch unavailable in all three stages. |

| M20 / `:1007` | Lowercase instead of casefold the held text | 5/6/3 → 5/6/3 → 5/6/3 | No score or verdict change relative to P/R. SURVIVED; Cursor fetch unavailable in all three stages. |


The explicit answer to the assignment is **no observed tip verdict change and no observed control meeting F ≥ 4 and G ≥ 3 for any survivor**. All ten also continue to survive `--self-test` on the landed counter bytes. This is bounded to these worlds and observed HTTP responses; it is not evidence against the already demonstrated synthetic coverage witnesses, and no rule/target change is proposed.

### Complete control score matrix

Every cell is the actually emitted F/K/G tuple and has exit 1. P0 is initial pristine S00; Rfinal is final restored S20. Each mutant column is its actual mutated-stage score. The complete intermediate P/R receipts are retained as mapped below. Maximum control F=1 and maximum control G=1; no row approaches both thresholds.


| Control | P0 | M04 | M06 | M07 | M08 | M09 | M11 | M14 | M16 | M19 | M20 | Rfinal |

|---|---|---|---|---|---|---|---|---|---|---|---|---|

| C01 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 |

| C02 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 |

| C03 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 |

| C04 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 |

| C05 | 0/6/0 | 0/7/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 |

| C06 | 0/7/0 | 0/7/0 | 0/7/0 | 0/7/0 | 0/7/0 | 0/7/0 | 0/7/0 | 0/7/0 | 0/7/0 | 0/7/0 | 0/7/0 | 0/7/0 |

| C07 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 |

| C08 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 |

| C09 | 1/1/0 | 1/1/0 | 1/1/0 | 1/1/0 | 1/1/0 | 1/1/0 | 1/1/0 | 1/1/0 | 1/1/0 | 1/1/0 | 1/1/0 | 1/1/0 |

| C10 | 0/2/0 | 0/2/0 | 0/2/0 | 0/2/0 | 0/2/0 | 0/2/0 | 0/2/0 | 0/2/0 | 0/2/0 | 0/2/0 | 0/2/0 | 0/2/0 |

| C11 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 |

| C12 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 |

| C13 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 |

| C14 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 |

| C15 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 |

| C16 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 | 0/6/0 |

| C17 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 |

| C18 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 |

| C19 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 |

| C20 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 |

| C21 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 |


On unmutated bytes, C17/C20 each counted a real Cursor row before the HTTP 403 and neither did afterwards. C09's existing Copilot-labelled IDE row remained F=1/K=1/G=0 throughout. Neither behavior is a newly demonstrated mutant-induced predicate bypass. Zero-backed worlds do not cause the counter to fetch their URLs; an invocation carrying `--fetch` is not proof that every rejected row's page was opened.

## Exact mutation, stage, and restoration receipts

`H0 = aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c` is the complete original target's SHA-256. For every row below, P-before=P-after=R-before=R-after=H0, while M-before=M-after is the listed hash. Every child invocation also hashes before and after. There was exactly one changed behavior-bearing line at a time, no self-test edit, and no additional counter edit.

| Mutant | P stage | M stage | R stage | M-before = M-after SHA-256 |
|---|---|---|---|---|

| M04 | `S00-pristine` | `S01-M04` | `S02-restored-M04` | `4b209061919a3fc2bb193736bc488f12871f20ec6cf52cd18835f3cc29de3700` |

| M06 | `S02-restored-M04` | `S03-M06` | `S04-restored-M06` | `c65dbc4078ee10ca85fb7d0769d0f814d3422995683c3eea8e25fadf94ee8ff4` |

| M07 | `S04-restored-M06` | `S05-M07` | `S06-restored-M07` | `795113943962c4d1a0a34d950640db1afbc2b1159b8fe0aa12722e7a4abb8b8f` |

| M08 | `S06-restored-M07` | `S07-M08` | `S08-restored-M08` | `59ce0a6bdf0521c045ae7847f1a0ace2b045b1ffa693206508fd62c4d2eb2dc7` |

| M09 | `S08-restored-M08` | `S09-M09` | `S10-restored-M09` | `25309a2cb777116051679464ad6a6f9620029e0de00f33cb30feb96db7000e9b` |

| M11 | `S10-restored-M09` | `S11-M11` | `S12-restored-M11` | `35261698018f91ab347c3e58564ca6be1a3c79b7c6d441dac3b78184671a32f1` |

| M14 | `S12-restored-M11` | `S13-M14` | `S14-restored-M14` | `4fdee19a1146a798f3dc9cc274104ad7a9aaced6e40c0a27e5f2df34bf5de842` |

| M16 | `S14-restored-M14` | `S15-M16` | `S16-restored-M16` | `6c69b32881d1c09a65ff11f093ff972994fb3ab961ec4ab38605e3bd39cfda42` |

| M19 | `S16-restored-M16` | `S17-M19` | `S18-restored-M19` | `d8446cd4301463a2a93037f2c4eca39f1742c95fbe636f235797e07e8af755a4` |

| M20 | `S18-restored-M19` | `S19-M20` | `S20-restored-M20` | `7c10f0ddbd9bd4e774978d4012970aedbe03ec4e667f87b0e6965a32f0a8c2c6` |


For any stage/world, exact argv, observed exit, UTC date, F/K/G, stdout, stderr, and before/after hashes are in `.probe/runs/<stage>/<ID>.json`; exact raw text is in `<ID>.stdout` and `<ID>.stderr`; complete stage data is `suite.json`. Thus e.g. `.probe/runs/S01-M04/C05.stdout:1-10` is the K-only witness, and `.probe/runs/S02-restored-M04/C05.stdout:1-10` is its restoration. The immutable substitutions are also retained in `.probe/mutations.json`.

Final observed in-memory comparison of the restored entire file with the original captured byte string: `True`. Final SHA-256: `aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c`. The final restored detector again executed all 22 worlds and the self-test; it was not merely a hash-only restoration check. No lane content, lane index, jj state, fleet state, or sibling working tree was modified. No sandbox commit was created or pushed.

### M04 — actual substitution and landed-tip output

Mutation point: `verifiers/check_command_files.py:583`. Exact original and mutant lines:

```python
# original
    if len(parts) < 2 or not parts[0].startswith("."):
# mutant
    if len(parts) < 1 or not parts[0].startswith("."):
```


Mutated stage `S01-M04`, date `Fri Oct 23 08:29:16 AM UTC 2026`, observed exit 0:

```sh
timeout 180 python3 -B verifiers/check_command_files.py --rev 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe --fetch
```

Verbatim stdout (`.probe/runs/S01-M04/T.stdout:1-10`); stderr empty:

```text
counter sha256 4b209061919a3fc2bb193736bc488f12871f20ec6cf52cd18835f3cc29de3700
counter rev 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe
custom command files found on the live page 6 of 6; new ground 4
Claude Code  BACKED token=.claude/commands/ norm=.claude/commands found=yes held-at-base=no
Codex        BACKED token=~/.codex/prompts/ norm=.codex/prompts found=yes held-at-base=yes
VS Code      BACKED token=.github/prompts norm=.github/prompts found=yes held-at-base=yes
reject Copilot CLI: SKILL.md command token ':456' is not well-formed; no entry row names the client
Gemini CLI   BACKED token=~/.gemini/commands/ norm=.gemini/commands found=yes held-at-base=no
Cursor       BACKED token=.cursor/commands norm=.cursor/commands found=yes held-at-base=no
opencode     BACKED token=.opencode/commands/ norm=.opencode/commands found=yes held-at-base=no
```


### M06 — actual substitution and landed-tip output

Mutation point: `verifiers/check_command_files.py:292`. Exact original and mutant lines:

```python
# original
                               "rules", "plugin", "plugins", "extension",
# mutant
                               "rules", "plugin", "extension",
```


Mutated stage `S03-M06`, date `Fri Oct 23 08:29:46 AM UTC 2026`, observed exit 0:

```sh
timeout 180 python3 -B verifiers/check_command_files.py --rev 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe --fetch
```

Verbatim stdout (`.probe/runs/S03-M06/T.stdout:1-10`); stderr empty:

```text
counter sha256 c65dbc4078ee10ca85fb7d0769d0f814d3422995683c3eea8e25fadf94ee8ff4
counter rev 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe
custom command files found on the live page 6 of 6; new ground 4
Claude Code  BACKED token=.claude/commands/ norm=.claude/commands found=yes held-at-base=no
Codex        BACKED token=~/.codex/prompts/ norm=.codex/prompts found=yes held-at-base=yes
VS Code      BACKED token=.github/prompts norm=.github/prompts found=yes held-at-base=yes
reject Copilot CLI: SKILL.md command token ':456' is not well-formed; no entry row names the client
Gemini CLI   BACKED token=~/.gemini/commands/ norm=.gemini/commands found=yes held-at-base=no
Cursor       BACKED token=.cursor/commands norm=.cursor/commands found=yes held-at-base=no
opencode     BACKED token=.opencode/commands/ norm=.opencode/commands found=yes held-at-base=no
```


### M07 — actual substitution and landed-tip output

Mutation point: `verifiers/check_command_files.py:291`. Exact original and mutant lines:

```python
# original
NOT_COMMAND_WORDS = frozenset(("skill", "skills", "agent", "agents", "rule",
# mutant
NOT_COMMAND_WORDS = frozenset(("skills", "agent", "agents", "rule",
```


Mutated stage `S05-M07`, date `Fri Oct 23 08:30:17 AM UTC 2026`, observed exit 0:

```sh
timeout 180 python3 -B verifiers/check_command_files.py --rev 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe --fetch
```

Verbatim stdout (`.probe/runs/S05-M07/T.stdout:1-10`); stderr empty:

```text
counter sha256 795113943962c4d1a0a34d950640db1afbc2b1159b8fe0aa12722e7a4abb8b8f
counter rev 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe
custom command files found on the live page 6 of 6; new ground 4
Claude Code  BACKED token=.claude/commands/ norm=.claude/commands found=yes held-at-base=no
Codex        BACKED token=~/.codex/prompts/ norm=.codex/prompts found=yes held-at-base=yes
VS Code      BACKED token=.github/prompts norm=.github/prompts found=yes held-at-base=yes
reject Copilot CLI: SKILL.md command token ':456' is not well-formed; no entry row names the client
Gemini CLI   BACKED token=~/.gemini/commands/ norm=.gemini/commands found=yes held-at-base=no
Cursor       BACKED token=.cursor/commands norm=.cursor/commands found=yes held-at-base=no
opencode     BACKED token=.opencode/commands/ norm=.opencode/commands found=yes held-at-base=no
```


### M08 — actual substitution and landed-tip output

Mutation point: `verifiers/check_command_files.py:589`. Exact original and mutant lines:

```python
# original
    return not any(w in NOT_COMMAND_WORDS for seg in parts for w in seg_words(seg))
# mutant
    return not any(w in NOT_COMMAND_WORDS for seg in parts[:-1] for w in seg_words(seg))
```


Mutated stage `S07-M08`, date `Fri Oct 23 08:30:43 AM UTC 2026`, observed exit 0:

```sh
timeout 180 python3 -B verifiers/check_command_files.py --rev 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe --fetch
```

Verbatim stdout (`.probe/runs/S07-M08/T.stdout:1-10`); stderr empty:

```text
counter sha256 59ce0a6bdf0521c045ae7847f1a0ace2b045b1ffa693206508fd62c4d2eb2dc7
counter rev 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe
custom command files found on the live page 6 of 6; new ground 4
Claude Code  BACKED token=.claude/commands/ norm=.claude/commands found=yes held-at-base=no
Codex        BACKED token=~/.codex/prompts/ norm=.codex/prompts found=yes held-at-base=yes
VS Code      BACKED token=.github/prompts norm=.github/prompts found=yes held-at-base=yes
reject Copilot CLI: SKILL.md command token ':456' is not well-formed; no entry row names the client
Gemini CLI   BACKED token=~/.gemini/commands/ norm=.gemini/commands found=yes held-at-base=no
Cursor       BACKED token=.cursor/commands norm=.cursor/commands found=yes held-at-base=no
opencode     BACKED token=.opencode/commands/ norm=.opencode/commands found=yes held-at-base=no
```


### M09 — actual substitution and landed-tip output

Mutation point: `verifiers/check_command_files.py:585`. Exact original and mutant lines:

```python
# original
    if any("." in seg[1:] for seg in parts[:-1]):
# mutant
    if any("." in seg[1:] for seg in parts[1:-1]):
```


Mutated stage `S09-M09`, date `Fri Oct 23 08:31:11 AM UTC 2026`, observed exit 0:

```sh
timeout 180 python3 -B verifiers/check_command_files.py --rev 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe --fetch
```

Verbatim stdout (`.probe/runs/S09-M09/T.stdout:1-10`); stderr empty:

```text
counter sha256 25309a2cb777116051679464ad6a6f9620029e0de00f33cb30feb96db7000e9b
counter rev 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe
custom command files found on the live page 5 of 6; new ground 3
Claude Code  BACKED token=.claude/commands/ norm=.claude/commands found=yes held-at-base=no
Codex        BACKED token=~/.codex/prompts/ norm=.codex/prompts found=yes held-at-base=yes
VS Code      BACKED token=.github/prompts norm=.github/prompts found=yes held-at-base=yes
reject Copilot CLI: SKILL.md command token ':456' is not well-formed; no entry row names the client
Gemini CLI   BACKED token=~/.gemini/commands/ norm=.gemini/commands found=yes held-at-base=no
Cursor       BACKED token=.cursor/commands norm=.cursor/commands found=no
opencode     BACKED token=.opencode/commands/ norm=.opencode/commands found=yes held-at-base=no
```


### M11 — actual substitution and landed-tip output

Mutation point: `verifiers/check_command_files.py:876`. Exact original and mutant lines:

```python
# original
        right_ok = j >= len(text) or not (text[j] in ASCII_ALNUM or text[j] in "_-")
# mutant
        right_ok = j >= len(text) or not (text[j] in string.ascii_letters or text[j] in "_-")
```


Mutated stage `S11-M11`, date `Fri Oct 23 08:31:51 AM UTC 2026`, observed exit 0:

```sh
timeout 180 python3 -B verifiers/check_command_files.py --rev 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe --fetch
```

Verbatim stdout (`.probe/runs/S11-M11/T.stdout:1-10`); stderr empty:

```text
counter sha256 35261698018f91ab347c3e58564ca6be1a3c79b7c6d441dac3b78184671a32f1
counter rev 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe
custom command files found on the live page 5 of 6; new ground 3
Claude Code  BACKED token=.claude/commands/ norm=.claude/commands found=yes held-at-base=no
Codex        BACKED token=~/.codex/prompts/ norm=.codex/prompts found=yes held-at-base=yes
VS Code      BACKED token=.github/prompts norm=.github/prompts found=yes held-at-base=yes
reject Copilot CLI: SKILL.md command token ':456' is not well-formed; no entry row names the client
Gemini CLI   BACKED token=~/.gemini/commands/ norm=.gemini/commands found=yes held-at-base=no
Cursor       BACKED token=.cursor/commands norm=.cursor/commands found=no
opencode     BACKED token=.opencode/commands/ norm=.opencode/commands found=yes held-at-base=no
```


### M14 — actual substitution and landed-tip output

Mutation point: `verifiers/check_command_files.py:298`. Exact original and mutant lines:

```python
# original
COMMAND_WORD_RE = re.compile(r"\b(?:commands?|prompts?)\b", re.IGNORECASE)
# mutant
COMMAND_WORD_RE = re.compile(r"(?:commands?|prompts?)", re.IGNORECASE)
```


Mutated stage `S13-M14`, date `Fri Oct 23 08:32:41 AM UTC 2026`, observed exit 0:

```sh
timeout 180 python3 -B verifiers/check_command_files.py --rev 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe --fetch
```

Verbatim stdout (`.probe/runs/S13-M14/T.stdout:1-10`); stderr empty:

```text
counter sha256 4fdee19a1146a798f3dc9cc274104ad7a9aaced6e40c0a27e5f2df34bf5de842
counter rev 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe
custom command files found on the live page 5 of 6; new ground 3
Claude Code  BACKED token=.claude/commands/ norm=.claude/commands found=yes held-at-base=no
Codex        BACKED token=~/.codex/prompts/ norm=.codex/prompts found=yes held-at-base=yes
VS Code      BACKED token=.github/prompts norm=.github/prompts found=yes held-at-base=yes
reject Copilot CLI: SKILL.md command token ':456' is not well-formed; no entry row names the client
Gemini CLI   BACKED token=~/.gemini/commands/ norm=.gemini/commands found=yes held-at-base=no
Cursor       BACKED token=.cursor/commands norm=.cursor/commands found=no
opencode     BACKED token=.opencode/commands/ norm=.opencode/commands found=yes held-at-base=no
```


### M16 — actual substitution and landed-tip output

Mutation point: `verifiers/check_command_files.py:673`. Exact original and mutant lines:

```python
# original
        if spans:
# mutant
        if spans and client_name(r[0]):
```


Mutated stage `S15-M16`, date `Fri Oct 23 08:33:21 AM UTC 2026`, observed exit 0:

```sh
timeout 180 python3 -B verifiers/check_command_files.py --rev 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe --fetch
```

Verbatim stdout (`.probe/runs/S15-M16/T.stdout:1-10`); stderr empty:

```text
counter sha256 6c69b32881d1c09a65ff11f093ff972994fb3ab961ec4ab38605e3bd39cfda42
counter rev 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe
custom command files found on the live page 5 of 6; new ground 3
Claude Code  BACKED token=.claude/commands/ norm=.claude/commands found=yes held-at-base=no
Codex        BACKED token=~/.codex/prompts/ norm=.codex/prompts found=yes held-at-base=yes
VS Code      BACKED token=.github/prompts norm=.github/prompts found=yes held-at-base=yes
reject Copilot CLI: SKILL.md command token ':456' is not well-formed; no entry row names the client
Gemini CLI   BACKED token=~/.gemini/commands/ norm=.gemini/commands found=yes held-at-base=no
Cursor       BACKED token=.cursor/commands norm=.cursor/commands found=no
opencode     BACKED token=.opencode/commands/ norm=.opencode/commands found=yes held-at-base=no
```


### M19 — actual substitution and landed-tip output

Mutation point: `verifiers/check_command_files.py:303`. Exact original and mutant lines:

```python
# original
HELD_PREV = frozenset("`\"'([</~=")
# mutant
HELD_PREV = frozenset("`\"'([</~=-")
```


Mutated stage `S17-M19`, date `Fri Oct 23 08:33:44 AM UTC 2026`, observed exit 0:

```sh
timeout 180 python3 -B verifiers/check_command_files.py --rev 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe --fetch
```

Verbatim stdout (`.probe/runs/S17-M19/T.stdout:1-10`); stderr empty:

```text
counter sha256 d8446cd4301463a2a93037f2c4eca39f1742c95fbe636f235797e07e8af755a4
counter rev 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe
custom command files found on the live page 5 of 6; new ground 3
Claude Code  BACKED token=.claude/commands/ norm=.claude/commands found=yes held-at-base=no
Codex        BACKED token=~/.codex/prompts/ norm=.codex/prompts found=yes held-at-base=yes
VS Code      BACKED token=.github/prompts norm=.github/prompts found=yes held-at-base=yes
reject Copilot CLI: SKILL.md command token ':456' is not well-formed; no entry row names the client
Gemini CLI   BACKED token=~/.gemini/commands/ norm=.gemini/commands found=yes held-at-base=no
Cursor       BACKED token=.cursor/commands norm=.cursor/commands found=no
opencode     BACKED token=.opencode/commands/ norm=.opencode/commands found=yes held-at-base=no
```


### M20 — actual substitution and landed-tip output

Mutation point: `verifiers/check_command_files.py:1007`. Exact original and mutant lines:

```python
# original
    for line in text.casefold().splitlines():
# mutant
    for line in text.lower().splitlines():
```


Mutated stage `S19-M20`, date `Fri Oct 23 08:34:04 AM UTC 2026`, observed exit 0:

```sh
timeout 180 python3 -B verifiers/check_command_files.py --rev 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe --fetch
```

Verbatim stdout (`.probe/runs/S19-M20/T.stdout:1-10`); stderr empty:

```text
counter sha256 7c10f0ddbd9bd4e774978d4012970aedbe03ec4e667f87b0e6965a32f0a8c2c6
counter rev 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe
custom command files found on the live page 5 of 6; new ground 3
Claude Code  BACKED token=.claude/commands/ norm=.claude/commands found=yes held-at-base=no
Codex        BACKED token=~/.codex/prompts/ norm=.codex/prompts found=yes held-at-base=yes
VS Code      BACKED token=.github/prompts norm=.github/prompts found=yes held-at-base=yes
reject Copilot CLI: SKILL.md command token ':456' is not well-formed; no entry row names the client
Gemini CLI   BACKED token=~/.gemini/commands/ norm=.gemini/commands found=yes held-at-base=no
Cursor       BACKED token=.cursor/commands norm=.cursor/commands found=no
opencode     BACKED token=.opencode/commands/ norm=.opencode/commands found=yes held-at-base=no
```


## Live-source limitation: HTTP 403 is not a killed mutant

The first nine suites (through S08-restored-M08) scored the tip 6/6/G4. S09-M09 and every later suite scored 5/6/G3, still exit 0. Cursor is the sole lost tip row. Its two ordinary GET attempts returned HTTP 403, and the same failure persisted after exact restoration.

Evidence:

- `.probe/runs/S08-restored-M08/T/http/requests.jsonl:5`: Cursor HTTP 200, 5,972 bytes, sha256 `7ceb657892bdfa5d7a32f1168411fcaeb63c2f6ab41a5f0c45116a0a3f3a6bf4`; date `Fri Oct 23 08:30:59 AM UTC 2026`.
- `.probe/runs/S09-M09/T/http/requests.jsonl:5-6`: the same URL returns `HTTP Error 403: Forbidden` twice; date `Fri Oct 23 08:31:12 AM UTC 2026`.
- `.probe/runs/S10-restored-M09/T/http/requests.jsonl:5-6`: exact H0 restoration still returns 403 twice; date `Fri Oct 23 08:31:28 AM UTC 2026`.

No attempt was made to bypass the refusal, fetch an alternate page to prop up the score, or treat the unchanged/restored failure as evidence that M09 caused the loss. Later Cursor-specific count sensitivity is limited by this unavailable source. All pristine tip predicate baselines nevertheless passed.

### HTTP receipt inventory

There were 363 actual counter HTTP attempts: 267 HTTP 200 reads and 96 HTTP 403 failures. The following table records each distinct URL/status/body identity, with the literal first-access `date -u` line. The per-attempt JSONL files preserve every timestamp, final URL, status, byte count, SHA-256 and raw-body path; dates below are not substituted for those per-attempt records. No source quotation is reproduced or shaped in this report.

| Requested URL | First `date -u` | HTTP | Bytes consumed | SHA-256 / evidence |
|---|---|---:|---:|---|

| <https://code.claude.com/docs/en/slash-commands.md> | `Fri Oct 23 08:29:00 AM UTC 2026` | 200 | 114542 | `6b070e872dea28905a7ea7f45c4d5960f5bdf28cc73ac808799af6d50435ffbd`; `.probe/runs/S00-pristine/C04/http/requests.jsonl:1` |

| <https://learn.chatgpt.com/docs/custom-prompts.md> | `Fri Oct 23 08:29:00 AM UTC 2026` | 200 | 3357 | `d6f7cf8dd9f31d2faf5604ef3a6f8322132a7b66fa50823109cb681e372a0fa9`; `.probe/runs/S00-pristine/C04/http/requests.jsonl:2` |

| <https://code.visualstudio.com/docs/agent-customization/prompt-files.md> | `Fri Oct 23 08:29:01 AM UTC 2026` | 200 | 13729 | `4ad1b2bcaf78c9166b1609610f354d9cb8b1ff9c9e7cf643c443fad04dac6685`; `.probe/runs/S00-pristine/C04/http/requests.jsonl:3` |

| <https://geminicli.com/docs/cli/custom-commands.md> | `Fri Oct 23 08:29:01 AM UTC 2026` | 200 | 12129 | `8f3295e8ca502b0c70bb3bf672f0dc0130ecb868fad4a88d5cac0f36ac6f3872`; `.probe/runs/S00-pristine/C04/http/requests.jsonl:4` |

| <https://cursor.com/docs/reference/deeplinks.md> | `Fri Oct 23 08:29:01 AM UTC 2026` | 200 | 5972 | `7ceb657892bdfa5d7a32f1168411fcaeb63c2f6ab41a5f0c45116a0a3f3a6bf4`; `.probe/runs/S00-pristine/C04/http/requests.jsonl:5` |

| <https://opencode.ai/v2/docs/commands/> | `Fri Oct 23 08:29:01 AM UTC 2026` | 200 | 32304 | `32591ac3db0056fdbf3b5e20b78e70514da0d7306707cbf7c412ca19276640e0`; `.probe/runs/S00-pristine/C04/http/requests.jsonl:6` |

| <https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/your-first-prompt-file.md> | `Fri Oct 23 08:29:00 AM UTC 2026` | 200 | 3039 | `117468ccb3abe5d07ae8f76a309f291b0fb93dae6d06de789feb9b90aa87b0ed`; `.probe/runs/S00-pristine/C09/http/requests.jsonl:1` |

| <https://raw.githubusercontent.com/anomalyco/opencode/4e0bc52216d91c3a8d10035837b1b6f9b82fd1d3/services/www/src/docs/content/commands.mdx> | `Fri Oct 23 08:29:01 AM UTC 2026` | 200 | 7242 | `dda6bba03043afff71a0bec4f0cfa40aaac12d53c1b20358df15e557c1a7ec11`; `.probe/runs/S00-pristine/T/http/requests.jsonl:6` |

| <https://cursor.com/docs/reference/deeplinks.md> | `Fri Oct 23 08:31:12 AM UTC 2026` | 403 | 0 | unavailable: HTTP-error body not consumed; `.probe/runs/S09-M09/C04/http/requests.jsonl:5` |


For successful attempts the raw file named in each JSONL record is in that same `http/` directory. No captured body was modified. Errors record no consumed body rather than inventing a checksum. The one truncated tool response for S11-M11 was recovered from the already-written `suite.json` (not by rerunning the detector); the tool inconsistency was reported via `xd://report_issue`.

## Disposition

Stopped after the assigned ten survivor probes. The surviving-self-test finding remains real, but this follow-up found no verdict-changing consequence on the landed tip or these reachable hollow controls. M04 has a reproducible K-only consequence; the M09 count drop is HTTP-limited and not a kill. The counter is restored exactly. No repair, integration, frozen-counter change, or canonical claim judgment was attempted.
