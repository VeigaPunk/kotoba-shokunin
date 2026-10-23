Result: HOLDS — all 13 self-test-surviving counter defects leave the declared real-data summary and exit code unchanged at c63ccc6823e1f6a8577acbb43d19551eadbbee9a; each was restored byte-exactly.

# MutC1Survivors — real-world relevance of the self-test gaps

## Scope and answer

- Attacked thing: whether the 13 defect candidates marked `SURVIVED` in `.ufo/waves/round-59/build/MutC1Counter.md:37-64` change the declared C1 measurement on the actual committed data, with live `--fetch`. This is not a judgment of the whole round or of hook-event semantics.
- Axes: measurement-path relevance, behavioral discrimination, exact input provenance, and no-harm restoration.
- **Changes this measurement: 0/13. Does not: 13/13.** Behavioral comparison verdicts: **13 SURVIVED, 0 KILLED, 0 INCONCLUSIVE**. All pristine and restored baselines succeeded; there was no baseline failure to mislabel as a kill.
- Important literal-output distinction: **every mutant changes the second stdout line's counter SHA-256**, as it must. None changes the first, declared measurement line, the exit code, or the rejection diagnostic. The ledger below classifies measurement behavior, not the intentional provenance-hash delta.
- This narrows the earlier report's conditional risks: none was realized in these live probes. It does not make the defects equivalent, validate their behavior on other worlds, or repair their self-test coverage gaps. No change to the counter, rule, targets, or lane data is proposed or integrated.

## Isolation, frozen inputs, and detector

Sandbox: `/fast/scratch/hyaku/kotoba-r59/MutC1Survivors`. It was created with these commands, both exit 0:

```sh
timeout 120 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r59/MutC1Survivors
timeout 30 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /fast/scratch/hyaku/kotoba-r59/MutC1Survivors checkout -q c63ccc6823e1f6a8577acbb43d19551eadbbee9a
```

Only the sandbox counter was mutated, one original report mutant at a time. Every mutant's digest matched that report's digest, so these were the same defects, not approximations. No sandbox commit was created. No lane Git/JJ write, sibling-source write, dispatch, runtime/client invocation, or integration was performed. The only lane file written by this seat is this report.

Frozen counter at the measured revision: `verifiers/check_hook_files.py`; **B** = `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71`. Lines 253-254 actually read `TARGET = 4`, `NEW_TARGET = 5`. The summary and predicate are at lines 1232-1251; the live measurement path is at 2383-2425. `plans/round-59.md:93-98` explicitly leaves event semantics to separate semantic review; this probe makes no stronger Events claim.

The identical bounded behavioral detector in every pristine/mutated/restored phase, from the sandbox root, was:

```sh
timeout 650 python3 -B verifiers/check_hook_files.py --rev c63ccc6823e1f6a8577acbb43d19551eadbbee9a --fetch
```

Each invocation was recorded by the following command, with `<ID>` and `<phase>` replaced by each ledger row and `pristine`, `mutated`, `restored` respectively:

```sh
timeout 700 python3 -B .survivor-probe/run.py <ID> <phase>
```

All **39 recording-helper commands exited 0**, and all **39 detector commands exited 0**. All detector stderr was empty. Each detector made exactly six ordinary live curl GETs, one successful first attempt per backed client: **234 GETs, all curl exit 0 / HTTP 200**. No mocked responses, fixture worlds, cached-response substitutions, or data mutations were used. The adjacent restored/pristine pair was allowed to run concurrently only while the counter was pristine; no counter edit overlapped either run. Mutants themselves ran alone.

A scratch-only executable `.survivor-probe/bin/curl` on the detector's PATH transparently resolved curl to `/usr/bin/curl`, kept every original argument, and forwarded stdout/stderr byte-for-byte with the original curl return code. It retained actual response bytes plus curl's status/effective-URL trailer, UTC timestamps and the actual `date -u` line. It neither changed a header nor replayed a response. This makes the fetch audit observable without a second change to the counter. The detector's outer 650-second cap also bounded M17, whose single intended mutation removes curl's own cap. Git/Python environment overrides were cleared; temporary directories were confined to the sandbox.

Probe interval: `2026-10-23T09:54:20.103845+00:00` through `2026-10-23T09:58:26.329473+00:00`. Example actual `date -u` output from the first detector receipt:

```text
Fri Oct 23 09:54:20 AM UTC 2026
```

## Actual output, common to all 39 measurements

The first stdout line was exactly this in every phase, including all mutants:

```text
hook files backed on committed snapshots 6 of 6; found on the live page 6 of 6; new ground 6
```

Full pristine/restored stdout, detector exit **0**, stderr empty:

```text
hook files backed on committed snapshots 6 of 6; found on the live page 6 of 6; new ground 6
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev c63ccc6823e1f6a8577acbb43d19551eadbbee9a
reject opencode: SKILL.md hook config cell holds no backticked token; no entry row names the client
```

Every mutated stdout had those same first and third lines; its second line contained its actual full mutant digest from the hash ledger below, followed by the same revision. All raw stdout/stderr and exit codes are retained in the per-phase receipts. These observations reproduce `.ufo/waves/round-59/C1-measure.txt:3-12`, not merely its exit status.

Expected behavioral detector: compare the exact first stdout line and process exit against successful pristine/restored runs. A differing summary or exit is `changes this measurement`; identical summary and exit is `does not`. The conditions in the next table explain what would have to become active for each particular missing check to matter; none was artificially introduced here.

## Per-survivor classifications

All line numbers refer to `verifiers/check_hook_files.py` at the measured revision. `P/M/R` means pristine/mutated/restored detector exits. The after-column records actual restoration, not a promised cleanup.

| ID | Smallest mutation applied | Expected distinguishing condition; actual observation | Classification | P/M/R | Behavioral verdict | After / no harm |
|---|---|---|---|---|---|---|
| M06 | 2391: live `page_why(..., r["events"])` becomes `page_why(..., [])` | Would differ if a live event check rejected a page. Pristine, mutant and restored all found all six; the fetched bodies were identical for all three phases. | does not | 0/0/0 | SURVIVED | exact B; 6/6/6 summary retained |
| M09 | 2378-2379: snapshot loader reads working-tree bytes instead of `git_show_bytes(lane, args.rev, ...)` | Would differ if working-tree snapshots diverged from the measured commit. All six snapshot files were left untouched and byte-equal to that commit; their exact comparison is retained in `summary.json`. | does not | 0/0/0 | SURVIVED | exact B; committed data unchanged |
| M12 | 1096: accept status 201 as well as 200 | Would differ on an otherwise accepted 201. Every real response in all three phases was 200. | does not | 0/0/0 | SURVIVED | exact B; same summary/exit |
| M13 | 1098: prefix final-host rejection condition with `False and` | Would differ on an otherwise accepted off-pin effective URL. All effective URLs equaled their requested URLs and stayed on their pinned hosts. | does not | 0/0/0 | SURVIVED | exact B; same summary/exit |
| M14 | 1100: prefix final-URL BASE-source rejection with `False and` | Would differ on an otherwise accepted reused BASE URL. Effective URLs were unchanged, and the pristine/restored final-URL checks accepted all six. | does not | 0/0/0 | SURVIVED | exact B; same summary/exit |
| M15 | 1067: frozen Accept becomes `Accept: */*` | Actually changed Cursor's fetched representation: 69,145 bytes became 1,307,361 bytes, with a different digest. Despite that real transport difference, all six quote/token/Events checks still passed, and the summary/exit did not change. Other five response bodies were identical. | does not | 0/0/0 | SURVIVED | exact B; Cursor returned to original 69,145-byte body |
| M16 | 1066: browser UA becomes `kotoba-check-hook-files` | Would differ if the bot response changed page acceptance. All six responses were 200 with the exact same bodies as pristine/restored in this probe. No general vendor-UA equivalence is claimed. | does not | 0/0/0 | SURVIVED | exact B; same summary/exit |
| M17 | 1065: curl `--max-time` becomes `0` | Would affect a request exceeding the frozen cap. The mutated whole detector completed in 0.993 seconds; no cap was reached in this triplet. The operational-bound defect remains, but was not activated. | does not | 0/0/0 | SURVIVED | exact B; frozen per-attempt cap restored |
| M18 | 1093: three-attempt loop becomes one attempt | Would differ on a transient failure requiring a retry. All three phases had exactly one successful attempt for each of six pages. | does not | 0/0/0 | SURVIVED | exact B; retry loop restored |
| M19 | 1104: prefix 5-MiB body rejection with `False and` | Would differ on an oversized otherwise-valid body. The largest body in this triplet was 274,129 bytes, below 5,242,880. | does not | 0/0/0 | SURVIVED | exact B; byte limit restored |
| M24 | 253: `TARGET = 4` becomes `TARGET = 3` | F=6 and G=6 satisfy both target versions. [INFERENCE] With G<=F and frozen G target 5, this isolated F reduction is redundant on valid main-path worlds, not an independent demonstrated acceptance weakness. | does not | 0/0/0 | SURVIVED | exact B; TARGET=4 restored |
| M25 | 254: `NEW_TARGET = 5` becomes `NEW_TARGET = 4` | G=6 satisfies both versions; this data world is not on the altered G boundary. [INFERENCE] It could matter at G=4, but no such world was substituted for the assigned committed data. | does not | 0/0/0 | SURVIVED | exact B; NEW_TARGET=5 restored |
| M26 | 1249: target sentinel guard uses `and` instead of `or` | Would differ with just one target None. Actual measured targets were the integers 4 and 5 in all three phases, so both guard spellings were false. | does not | 0/0/0 | SURVIVED | exact B; original guard restored |

### Exact counter hashes

Every phase receipt records before/after source hashes and whether the bytes equal `git show c63ccc6823e1f6a8577acbb43d19551eadbbee9a:verifiers/check_hook_files.py`. The detector never changed its own bytes. Each mutant was restored before the next was applied.

| ID | Pristine before/after | Mutated before/after SHA-256 | Restored before/after |
|---|---|---|---|
| M06 | B / B | `ecf537ce022dea605125cf2f808dbc086e6c5ed1e992775733a1174d73b84591` | B / B, byte-exact |
| M09 | B / B | `90df42174e1fa6f563b4c45175bbc06a0a3dabedcef957067d36a3389870d244` | B / B, byte-exact |
| M12 | B / B | `88058c04574c8ef094db49979c128f58aecb7a38972fb363331e4912788fdfe1` | B / B, byte-exact |
| M13 | B / B | `0f3ec68648291a705c72ef563a2f4924e7e23ea1faba2441180bcba14a0b55a1` | B / B, byte-exact |
| M14 | B / B | `73c933847d523d4ddc8e7f6921542cec7fb53e66de3d3bccdb125ffd315cd03d` | B / B, byte-exact |
| M15 | B / B | `bb45e0c65739ab594c1ffc9b75c6391c344524f9b860c604884b21572ffa08cf` | B / B, byte-exact |
| M16 | B / B | `c8dfbc4542721886fe667492518daee7b1164916955758e7a9ccdd83b206f222` | B / B, byte-exact |
| M17 | B / B | `231c1cdafd57efed60522b6ce30965845c45d6b219af7c56344e3a1459973970` | B / B, byte-exact |
| M18 | B / B | `2b84afb13fce4027d0925dcc38442045899d7d46a2b6d106dd93631f4588d2ef` | B / B, byte-exact |
| M19 | B / B | `8cd5753778b3f8901137c733a4a18ebbd66f5cdef941f5029390464abd2d0a5b` | B / B, byte-exact |
| M24 | B / B | `44cd50ec859cc72478e9150fc1dd8b8e5772e5193faeca16e7053b69b52b790f` | B / B, byte-exact |
| M25 | B / B | `6eb61db6e362d5772059ffec2e178f9625b6d05f7e3e1cb4bc9997877627070b` | B / B, byte-exact |
| M26 | B / B | `00b24f7222080e63fa863a932ba5c8c73776a776f044c506e04091a9a110b0ee` | B / B, byte-exact |

## Live-fetch audit

All URLs below were actually opened by the detector through ordinary curl. All statuses were HTTP 200 and effective URLs equaled requested URLs, with curl exit 0. In the table, the bytes/digest occurred in every one of the 39 phases except where stated. Each phase's six JSON fetch records include the actual UTC start/end, verbatim `date -u` output, argv, URL, effective URL, status, byte count, SHA-256, stderr and path to the exact fetched body. No external-document quotation is used in this report, so no quote shaping was performed.

| Source / URL | Body bytes | Body SHA-256 | Occurrences |
|---|---:|---|---:|
| S096 https://code.claude.com/docs/en/hooks.md | 274129 | `c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8` | 39 |
| S097 https://learn.chatgpt.com/docs/hooks.md | 47133 | `57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92` | 39 |
| S098 https://code.visualstudio.com/docs/agent-customization/hooks.md | 15152 | `98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08` | 39 |
| S099 https://docs.github.com/en/copilot/concepts/customizations/hooks.md | 8428 | `23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4` | 39 |
| S100 https://geminicli.com/docs/hooks/best-practices.md | 17650 | `fb44fbcfaccc3cdb7895d989f3808bed66cfa6516411535c4c4d9077d242e7bc` | 39 |
| S101 https://cursor.com/docs/hooks, frozen Accept | 69145 | `8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d` | 38 |
| S101 https://cursor.com/docs/hooks, M15 `Accept: */*` | 1307361 | `380c5a72c14ca5d72cfbc91f90bf7d285c2d2f1652588c4aa7dfcfe5dcdc8bd3` | 1 |

For example, M15's actual Cursor access record contains this `date -u` output, HTTP 200, 1,307,361 bytes and the last digest above:

```text
Fri Oct 23 09:56:17 AM UTC 2026
```

The ordinary frozen-header body digests also equal the six committed snapshot digests. M15 is therefore a concrete transport-representation difference with **no observed declared-measurement difference**, not evidence that Accept is inert.

## Evidence map and restoration

All raw evidence is under `/fast/scratch/hyaku/kotoba-r59/MutC1Survivors/.survivor-probe/`:

- `run.py`: bounded detector recorder; it does not edit the counter or data.
- `bin/curl`: transparent curl audit wrapper.
- `receipts/<ID>.pristine.json`, `receipts/<ID>.mutated.json`, `receipts/<ID>.restored.json`: all 39 actual commands, return codes, complete stdout/stderr, exact diffs, timestamps and before/after counter hashes.
- `fetches/<ID>.<phase>/*.json` and sibling `*.body`: all 234 actual fetch audit records and exact response bodies. The phase receipt embeds its six fetch records too, so the receipt alone carries the required network metadata.
- `summary.json`: final counter byte-equality evidence and exact working-tree/committed comparisons for SKILL, entry, SOURCES, lesson and all six snapshots. All ten files were byte-equal to the assigned data commit.

The detector run for `M26 restored` observed the final counter before/after as B, `matches_frozen_before: true`, `matches_frozen_after: true`, and exit 0 with the same 6/6/6 summary. Final independent byte comparison against `git show c63ccc6823e1f6a8577acbb43d19551eadbbee9a:verifiers/check_hook_files.py` also returned true with digest B. No mutation remains. The receipt-analysis helper initially misspelled `S096.page` as `S96.page`; that read-only metadata step failed with git exit 128, was corrected, and completed. It did not run a detector, change data, invalidate a baseline, or cause a detector rerun.

Tools observed: Python 3.14.8 and curl 8.23.0. Tools installed/upgraded: none. No checks outside the assigned mutation/measurement and restoration evidence were run. No semantic hook-event review or client runtime test is claimed.

Report: .ufo/waves/round-59/falsify/MutC1Survivors.md
