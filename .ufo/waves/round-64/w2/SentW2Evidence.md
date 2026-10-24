# SentW2Evidence — wave-1 evidence integrity

## Result
No wave-1 report-integrity or dispatch-artifact defect found at measured tip `c019919c97ab5fe98e87a7754b4449ea4e699c99`. This was a read-only check; I did not run the UFO runtime/validator or dispatch a wave. No tools were installed.

## 1. Wave-1 reports — INFO, no integrity fault observed

**Exploit path considered:** a report could be omitted from the integration commit or changed after it, in the index, or in the working tree. **Impact:** none observed; all 32 Markdown reports are in the measured tree and the wave-1 subtree has no diff through current `HEAD` or the working tree. **Smallest remediation:** none.

Evidence (lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin`):

```text
$ git log --format='%h %s' -1 -- .ufo/waves/round-64/w1/
c019919 round-64: wave-1 integration — C1 G7 span_missing pinning arms (223 assertions, hardened arm 4), C2 r64 routed-repairs counter (32-assertion self-test), LOG corrections block + round-64 entry, S120+entry+lesson+Q60, inherited MutW2SplitClauses edit + ExecW2E2Patch drift note, w1 evidence + controls
log-exit=0

$ git rev-parse HEAD
b99fb79c27042e0f8a598cbbb4d81479a806b518

$ git ls-tree -r --name-only c019919c97ab5fe98e87a7754b4449ea4e699c99 -- .ufo/waves/round-64/w1/ | [count paths ending .md]
32
pipeline-exit=0

$ git status --porcelain --untracked-files=all -- .ufo/waves/round-64/w1/
[no output]
status-exit=0

$ git diff --quiet c019919c97ab5fe98e87a7754b4449ea4e699c99 HEAD -- .ufo/waves/round-64/w1/
measured-to-current-tree-exit=0
$ git diff --quiet HEAD -- .ufo/waves/round-64/w1/
current-index-worktree-exit=0
```

The measured-tip tree lists 33 paths total: these 32 reports plus `swarm-registry.json`. Report basenames: `ConnSibling.md`, `CriticC1Bound.md`, `CriticC2Bound.md`, `ExecCalibVerify.md`, `ExecCensusAfter.md`, `ExecGateRow.md`, `ExecNoHarmBase.md`, `ExecR64Counter.md`, `ExecReceiptTemplates.md`, `ExecSeatDriftFix.md`, `ExecSpanArms.md`, `ExecSpanBefore.md`, `MutR64Counter.md`, `MutSpanArms.md`, `RevC1Predicate.md`, `RevC2Checks.md`, `RevSourcesGate.md`, `RevSpotcheckCrosswalk.md`, `ScoutQualityDebt.md`, `ScoutReceiptSweep.md`, `ScoutS049.md`, `ScoutS120.md`, `ScoutS120Alt.md`, `ScoutSiblingOverlap.md`, `ScribeEntry.md`, `ScribeLOGCorr.md`, `ScribeLesson.md`, `ScribeQ60.md`, `ScribeReportSkeleton.md`, `ScribeSCORECARD.md`, `ScribeSHONEN.md`, `ScribeSOURCESRow.md`.

I discarded an initial `git ls-tree` `:(glob)` attempt: `ls-tree` rejected that magic pathspec and the downstream `wc` misleadingly printed zero. The successful count above enumerated the whole committed directory and counted `.md` suffixes; the rejected result is not evidence.

## 2. Spec / dispatch / registry schema join — INFO, consistent

**Exploit path considered:** malformed JSON, drifted wave/report paths, missing or renamed seat entries, or a malformed operator-note value. **Impact:** none observed in these artifacts. **Smallest remediation:** none.

`jq`/jaq parsed all three files as JSON objects (each exit 0). The following read-only cross-check returned the shown results:

```json
{
  "spec_wave": "kotoba-r64-w1",
  "dispatch_wave": "kotoba-r64-w1",
  "registry_wave": "kotoba-r64-w1",
  "spec_items": 32,
  "dispatch_spawn": 32,
  "dispatch_resume": 0,
  "dispatch_total": 32,
  "dispatch_tasks": 32,
  "persisted_registry_members": 32,
  "embedded_registry_members": 32,
  "names_match": true,
  "report_dirs_match": true,
  "registry_schema_match": true,
  "path_match": true,
  "taskCall_shape": true,
  "dispatch_schema": "ufo-swarm-wave-dispatch-v1",
  "note_type": "string",
  "resumeSends": 0
}
```

Additional checks returned `name_role_spec_dispatch=true`, `name_role_spec_registry=true`, `task_rows_welltyped=true`, `note_string=true`, `note_bytes=277`. All three JSON parse/type commands exited 0. The note's exact parsed value (277 ASCII/UTF-8 bytes, excluding a newline) is:

```text
Issue exactly one batched task call with taskCall ({context, tasks}); never split a wave into multiple task calls (one-swarm-per-wave). Then one hub send per resumeSends entry: hub send --to <entry.resume> --message <entry.message> (entry.name is bookkeeping, not a hub field).
```

Schema basis read locally, not executed: `ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs` lines 1292–1315 emits `ufo-swarm-wave-dispatch-v1`, spawn `taskCall {context,tasks}`, `resumeSends`, and a note; `scripts/ufo-swarm-wave.test.mjs` lines 106–120 checks the dispatch/task record shape, and lines 251–264 explicitly require only that `note` be a string (wording intentionally unpinned). `ufo-swarm-registry.mjs` line 27 defines `ufo-swarm-registry-v1`. The observed note therefore has the required shape; its wording is not treated as a separate validator contract.

No wave-1 resume leg exists (`counts.resume=0`, `resumeSends=[]`), so this artifact surface exercises no `resume_continuity_v1` rejection or mutation path.

## 3. `w1-dispatch.err` — INFO, empty/harmless

**Exploit path considered:** hidden dispatcher diagnostics in the captured stderr file. **Impact:** none visible in this file; an empty stderr alone does not prove dispatch success. **Smallest remediation:** none.

```text
$ wc -c < .ufo/waves/round-64/w1-dispatch.err
0
$ sha256sum .ufo/waves/round-64/w1-dispatch.err
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  .ufo/waves/round-64/w1-dispatch.err
$ test -r .ufo/waves/round-64/w1-dispatch.err; echo $?
0
```

## 4. Round-directory and fleet-root status — INFO, no Kotoba-R64 root stray observed

The lane status is **not clean overall**: the read-only `git status --porcelain --untracked-files=all -- .ufo/waves/round-64` snapshot (exit 0) showed one modified `receipts/noharm-tip.txt` and untracked W2 artifacts: `ConnW2Fleet.md`, `CriticW2Frontier.md`, `CriticW2NoHarm.md`, `ExecW2Gates.md`, `ExecW2MidHistory.md`, `ScoutW2CensusAfter.md`, `ScoutW2QualityDebt2.md`, `ScoutW2SiblingVerify.md`, `SentW2Scope.md`, and `swarm-registry.json`. No W1 path appears. These are outside the W1 subtree; W2 artifacts are in the declared W2 area. This is a status snapshot before this report was written; this report itself is another declared W2 file.

The requested full fleet-root command `/home/vgpnk/Projects/shokunin`:

```text
$ git -C /home/vgpnk/Projects/shokunin status --porcelain
 M .ufo/state/chousa.report-baseline
 M .ufo/state/kagi.report-baseline
 M .ufo/state/kaidoku.report-baseline
 M .ufo/state/kake.report-baseline
 M .ufo/state/kama.report-baseline
 M .ufo/state/kengaku.report-baseline
 M .ufo/state/kumitate.report-baseline
 M .ufo/state/mado.report-baseline
 M .ufo/state/mori.report-baseline
 M .ufo/state/souji.report-baseline
 M .ufo/state/tameshi.report-baseline
 M .ufo/state/tsukuroi.report-baseline
 M .ufo/watchdog.log
 M SCORECARD.md
?? .omp/mcp.json
?? .ufo/state/kotoba.report-baseline
?? .ufo/state/kotodama.report-baseline
?? .ufo/state/revenger.report-baseline
?? .ufo/waves/hyaku/inline-run-20261023.md
?? AGENTS.md
?? bm.json
?? live.html
?? live_s228.html
?? nama.html
?? s395.txt
?? scripts/hyaku/append-closure.py.bak-20261023T040735Z
?? scripts/hyaku/fleet-commit.sh.bak-20261023T040735Z
?? tf_bavelas.html
?? unblob.log
?? wb2.html
?? write
?? xc.xml
fleet-status-exit=0

$ git -C /home/vgpnk/Projects/shokunin status --porcelain --untracked-files=all -- ':(glob)**/*kotoba-r64*'
[no output]
fleet-kotoba-r64-filter-exit=0
```

No `kotoba-r64` seat/report path appears in the root status. The only `kotoba`-named status path is `?? .ufo/state/kotoba.report-baseline`; it is not a `kotoba-r64` report. **[INFERENCE]** Path-only evidence cannot attribute that baseline file to this round, so I do not classify it as a misrooted W1/W2 seat report. I made no changes outside this report.