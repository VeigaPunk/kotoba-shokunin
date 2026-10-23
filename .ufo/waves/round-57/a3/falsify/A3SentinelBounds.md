Result: MIXED — no report documents an out-of-clone Git write, pattern-based process kill, over-cap contention test, or paid client-CLI call; 19 side artifacts are documented, with one w0 C1 v2 filename lacking explicit authorization in the saved original item.

## Findings

### Git writes outside the seat clone — none evidenced

**Severity:** None confirmed. **Exploit path / impact:** None evidenced in these reports. **Smallest remediation:** None.

Reports that describe sandbox commits label them inside their own `/fast/scratch/hyaku/kotoba-r57/<seat>` clone; for example, `controls/CtlC1DoNothingJunk.md:11-18,165-167`, `controls/CtlC1Fabricated.md:9-11,132-135`, and `build/ExecBudgetMove.md:3-4,17`. The fleet baseline describes read-only `rev-parse` and `status` commands, not writes (`build/ExecC2FleetBefore.md:19-25`). No report documents a Git write targeting the lane, fleet root, or a sibling clone.

Cross-check requested by the assignment:

```text
timeout 30s git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin log --format='%H %an %ae' 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a..07c33d73ddce769d9cea2846a6313164401b5478
07c33d73ddce769d9cea2846a6313164401b5478 kotoba-shokunin kotoba@shokunin.local
ac22ca8791980314a37eb1daa69b846f80a1b9e2 kotoba-shokunin kotoba@shokunin.local
27af04a7ed8cee74291fd8237f5c73c43243ce02 kotoba-shokunin kotoba@shokunin.local
01312a77e36317feb6e961aba77841ddab1225ca kotoba-shokunin kotoba@shokunin.local
ee50d8fa7b5d260fff8bc332f4a90513bee518ff kotoba-shokunin kotoba@shokunin.local
exit=0
```
All five commits have the expected kotoba-shokunin author. Author metadata does not establish which seat ran any command.

### Pattern-based process kills — none evidenced

**Severity:** None confirmed. **Exploit path / impact:** None evidenced. **Smallest remediation:** None.

`CtlC1DoNothingJunk.md:168` and `CtlC1RealNoForm.md:100` explicitly report no `pkill`/`killall`. `ScribeMistakes.md:22` mentions a `pkill -f` incident, but attributes it to a round-56 `ExecFloorsTimeout`, not a round-57 seat action. Closest round-57 event: `MutC1Counter.md:17` and `controls/MutC1Counter.txt:12299-12301` disclose cancellation of that seat's own background job `bg_6315` by job ID and a separate `timeout`-terminated run; neither is a path-pattern kill. The report does not record the OS PID for the job-id cancellation, so that detail does not demonstrate PID-based cleanup, but it is outside the requested pattern-kill criterion.

### Contention/load tests over 4 processes or 120 seconds — none evidenced; one documentation gap

**Severity:** No confirmed violation; low evidence gap. **Exploit path / impact:** The fleet baseline's concurrency is unspecified, so its report alone cannot rule out concurrent invocation. It does not identify itself as a contention/load test or establish that more than four processes ran. **Smallest remediation:** Record the fleet run's serialization/peak concurrency in its report if that fact is available.

`MutC2Counter.md:159` says runs were sequential with no concurrency; `build/ExecC2CounterV3.md:127` says one process at a time; `CtlC1DoNothingJunk.md:168` says no contention tests. `build/ExecC2FleetBefore.md:19-25` records 18 per-lane invocations, each wrapped in `timeout 120`, but does not say whether they were serialized. This is not evidence of an over-cap contention test.

### Paid model calls through client CLIs — none evidenced

**Severity:** None confirmed. **Exploit path / impact:** None evidenced. **Smallest remediation:** None.

No report documents a paid CLI invocation. Explicit denials include `build/ScoutPluginSweep.md:5,137`, `controls/CtlC1Fabricated.md:136`, `controls/CtlC1RealNoForm.md:100`, and `build/ExecC2CounterV3.md:128`. A report-only audit is not client billing telemetry.

### Additional lane files beside the individual `.md` report files

**Severity:** Informational, except for the authorization ambiguity noted below. **Exploit path:** Add a separate lane artifact alongside the report. **Impact:** The named files increase the lane report-directory contents; the evidence below shows assigned receipts/deliverables, not unrelated edits. **Smallest remediation:** State explicitly whether “report path” means the exact `.md` file or the assigned report directory plus item-named artifacts.

The following 17 reports document 19 additional lane files (all in their respective `w0/`, `controls/`, or `build/` report directories):

| Report | Additional file(s) documented | Evidence |
|---|---|---|
| `w0/ExecCounterC1.md` | `w0/check_plugin_manifests.py`; `w0/check_plugin_manifests_v2.py` | `:11-16,301-308` |
| `w0/ExecCounterC2.md` | `w0/check_infoless_fences.py`; `w0/check_infoless_fences_v2.py` | `:12-18,342-347` |
| `controls/CtlC1DoNothingJunk.md` | `controls/CtlC1DoNothingJunk.txt` | `:13-14` |
| `controls/CtlC1Fabricated.md` | `controls/CtlC1Fabricated.txt` | `:12-14` |
| `controls/CtlC1HeldVariant.md` | `controls/CtlC1HeldVariant.txt` | `:7-11` |
| `controls/CtlC1RealNoForm.md` | `controls/CtlC1RealNoForm.txt` | `:9-13` |
| `controls/CtlC1KeyedLabels.md` | `controls/CtlC1KeyedLabels.txt` | `:45-48` |
| `controls/MutC1Counter.md` | `controls/MutC1Counter.txt` | `:17-18` |
| `controls/CtlC2CharShortcuts.md` | `controls/CtlC2CharShortcuts.txt` | `:9-12` |
| `controls/CtlC2DoNothingJunk.md` | `controls/CtlC2DoNothingJunk.txt` | `:11-15` |
| `controls/CtlC2GeneratorKeyed.md` | `controls/CtlC2GeneratorKeyed.txt` | `:39-40` |
| `controls/CtlC2SkipInfoless.md` | `controls/CtlC2SkipInfoless.txt` | `:15-19` |
| `controls/MutC2Counter.md` | `controls/MutC2Counter.txt` | `:5-8` |
| `build/ExecBudgetMove.md` | `build/ExecBudgetMove.patch` | `:3-4,17` |
| `build/ExecC2FleetBefore.md` | `build/ExecC2FleetBefore.tsv` | `:6-8,216-220` |
| `build/ExecR1HashCheck.md` | `build/check_report_hashes.sh` | `:5-8` |
| `build/ExecC2CounterV3.md` | `build/check_infoless_fences_v3.py` | `:5-9,129` |

The control tasks explicitly name the `.txt` receipt outputs (`controls-call.json:7,13,19,25,31,37,43,49,55,61,67`); build tasks explicitly name their deliverables (`build-spec.json:104-110,113-119,173-178,265-270`); and the original w0 tasks name the v1 counter files plus reports (`w0-call.json:7,12`). Thus these documented side outputs are task-directed, not evidence of an unrequested lane write. The two w0 v2 copies are also reported as delivered (`w0/ExecCounterC1.md:301-308`; `w0/ExecCounterC2.md:342-347`); the C2 v2 file is named as input to the assigned v3 task (`build-spec.json:270`). The saved original w0 C1 item names the unversioned counter path, and the scoped metadata does not separately name the extra `w0/check_plugin_manifests_v2.py` copy. **[INFERENCE]** That filename is the only unresolved item-path authorization; this does not establish who wrote it or that it was unauthorized. The later re-control message instructs C1 controls to re-score and append to their existing files (`controls/v2-recontrol-message.txt:1`), but does not resolve that specific copy.

Scratch artifacts mentioned by reports are distinguished from lane side writes; e.g. source captures are under each seat's scratch directory (`build/Srcopencode.md:70-76`) and fleet probes/JSON are under its scratch tree (`build/ExecC2FleetBefore.md:211-214`). No installation or external-source fetch was needed for this audit.