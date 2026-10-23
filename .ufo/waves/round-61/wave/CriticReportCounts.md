# CriticReportCounts — measured-number ledger and counterexamples

Date: 2026-10-23. Seat: `kotoba-r61-wave-CriticReportCounts-3`. Scope: calibration; secondary risk to operability and the credibility of the depth/adjacency claims. This is advisory evidence, not a verdict, admission, integration, or authorization to change the frozen predicates.

Read first: `plans/round-61.md`. The lane and fleet were read-only throughout; the only write by this seat is this report. No dispatch, index operation, git/jj mutation, lane verifier, live fetch, build, test, lint, or formatter was executed. The commands below are read-only counting programs; their successful exit codes are not C1/C2/C3 pass codes.

## Answer: reusable count list, with provenance boundaries

Each figure below comes from the pasted command/output ledger. A source identifier, revision, date, or frozen predicate literal is not itself a measured result. Every measurement resolves `master` once and then reads that commit; the full resolved revision is in its output. `master` advanced during this review, so do not silently combine snapshots or describe them as a final integrated state.

| Quantity | Grounded value | What it does and does not establish |
|---|---|---|
| Frozen claim headings | 3 | Plan inventory, not verified claims (`ReportMetadata`). |
| Wave manifest members | 68 | Spec, rendered task payload, and registry agree; this is declared work, not a census of successfully started or finished agents (`Seats`). |
| Roles | connector 1; critic 9; executor 8; mutation-tester 11; revenger 1; reviewer 16; scout 6; scribe 12; sentinel 3; simplifier 1 | Same role histogram in spec, payload, and registry (`Seats`). Do not count L1 as a swarm role. |
| Conservative attack slice | 36 / 68 = 52.94% | Explicitly only critic + mutation-tester + reviewer; no extra credit assumed for revenger/sentinel/scout (`Seats`). |
| Registry assigned agent identities | 0 non-null agent IDs | The committed/rendered registry is not evidence of actual launch success or absence. This is not a dead-seat count (`Seats`). |
| Report inventory during wave | 0 committed expected reports at the `Seats` revision; 11 expected reports visible in the working directory at that observation | Not the eventual report count; the command lists their names. The working count precedes this report's creation and is not a closure claim (`Seats`). |
| Frozen arms and world slots | 4 arms; 7 attack-world labels; W0 is an extra slot, giving 8 slots including it | Declared universe only, not observed rejections (`WorldsAndEligibility`). |
| Current decision-table population | 7 client rows: 4 eligible and 3 directory-scoped negatives | Eligible entry rows: Claude Code/S103, VS Code/S105, Copilot CLI/S106, Cursor/S108. Negative clients: Codex, Gemini CLI, opencode (`WorldsAndEligibility`). |
| Decision cells / keys | 21 structural decision cells; 4 client-key bindings but 3 distinct spellings (`applyTo`, `globs`, `paths`) | Neither cell count nor key spelling count verifies semantics (`DecisionCardinalities`). |
| C2 repair universe / base receipt | 6 labels; committed base receipt says `routed repairs verified 0 of 6`, `base-exit=1` | Documentary re-read only; this seat did not execute the checker (`WorldsAndEligibility`). |
| Historical build correction | 32 declared build tasks, 29 matching committed reports, 3 missing reports | Missing: `ExecBudgetMove`, `ExecGateRegistry`, `ExecShonenPointer`. These are missing reports, not proved dead seats (`HistoricalReports`, `HistoricalCountEdges`). |
| Historical directory-count traps | 33 committed build files; 30 Markdown files; 29 actual manifest-matched reports | The extra Markdown file is a fixture. Full nonreport list is in `HistoricalCountEdges`; directory cardinality is not report cardinality. |
| Historical visible-call roster | 64 tasks in the named call artifacts, 59 matching committed reports | Components: W0 10; W0b 3; controls 8; controls-v2 3; build 32; residual 8. The old report asserts W0 11 and total 65; those are documentary assertions, not re-derived totals (`HistoricalReports`, `HistoricalCountEdges`). |
| Historical source rows | 101 → 110; 9 added IDs, S103–S111 | Revisions are printed in `Sources`; the addition is tier A by the actual row histograms. |
| Round-61 source rows at the observed tip | 110 → 110 from the round base; 0 added, removed, or changed existing rows | This is the current committed comparison, not a prediction of integration (`Sources`). |
| Current source histogram | tiers A=108, B=1, C=1; statuses mined=102, queued=7, rejected=1 | Same at the round base and the observed tip; malformed rows=0 (`Sources`). |
| Source IDs are not row counts | Highest ID S111, but 110 rows; S092 is absent | Count rows, not the suffix of the last ID (`Sources`). |
| Frozen new-source intent | 5 distinct IDs: S112, S113, S114, S115, S117 | The inclusive S112–S117 range has length 6, but S116 is not named by the frozen sourced-claim sentence. If these alone were added, 115 is the arithmetic total, not an observed after result (`Sources`). |
| C3 observation | source match count 0; entry not committed; README matching-line count 0 | No C3 after result yet (`Sources`, `ReportMetadata`). |
| Existing score fields / checklist | depth 9; consistency 10; adjacency 8.0 (historical field also says was 7.5); 4 SHONEN `[~]` marks and 0 `[x]` marks | Existing record text only, not a new score or judgment (`ReportMetadata`). |
| Other optional report numbers | SKILL.md 591 lines; census-before receipt has 13 W04 lines and ends `exit=0`; r60 freeze receipt says 318 assertions and 0 failure(s) | Line count / receipt extraction only. The census and self-test were not rerun (`ReportMetadata`, `WorldsAndEligibility`). |

The committed scoped-rules counter still has the v2 digest printed in `ReportMetadata`. Therefore neither this review nor the plan wording supplies a v3 self-test result, a v3 base/tip fetch result, a post-repair C2 result, a C3 after count, a final report total, a dead/cancelled-seat total, or any residual-call total. Those remain unavailable at this stage and must not be filled with planned values. The L1 must produce a new pinned measurement receipt after integration before such numbers enter the final report; that later receipt is a new list observation, not retroactive meaning assigned to this one.

## Counterexamples, evidence, impacted axes, smallest safe corrections

### Directory counts can make the R-a correction itself false

**Counterexample.** `verifiers/check_routed_repairs.py:166-170` supplies the example counting command `ls .ufo/waves/round-60/build | wc -l` next to `committed 29`. The committed directory actually contains 33 files. Even an unrestricted Markdown count gives 30, because `check_word_counts.fixture.md` is data, not a seat report. `HistoricalCountEdges` records the complete nonreport set: `ExecIndexCorpus.patch`, `check_word_counts.fixture.md`, `check_word_counts.py`, and `swarm-registry.json`.

**Evidence.** `HistoricalReports` joins the build-spec names to committed report paths and obtains 29 reports from 32 declared tasks. `HistoricalCountEdges` independently exposes the file/Markdown/report cardinality split. The frozen R-a implementation (`check_routed_repairs.py:69-74`) checks substring presence, not whether the attached counting command returns the asserted value. A token-based R-a pass must not be described as proof that report counting is now automatically guarded.

**Impacted axes.** Calibration directly; operability if a reader executes a command that contradicts its claimed result.

**Smallest safe correction.** In the appended LOG erratum and final report, use the actual manifest-to-committed-path join below and name its measured revision/date/output. Do not use the counter's directory-count example as the receipt. Preserve the frozen counter for its declared measurement; any hardening is a separately identified measurement, not a silent replacement. No task-content trade is needed.

### The frozen source range is not a six-row acquisition

**Counterexample.** `plans/round-61.md:94` explicitly names S112–S115 and S117. The source-producing seats match that set. The `ScribeLesson` prompt in the wave spec nevertheless says “every new row S112-S117,” a range which includes S116. Reading the range as a count would turn the actual frozen set into an extra source row with no corresponding opened-source evidence. The existing registry already demonstrates the general error: highest ID S111, row count 110.

**Evidence.** `Sources` derives the unique planned ID set from the committed plan sentence, prints its count 5, prints the range length 6 and the omitted S116, and separately measures the current committed row count.

**Impacted axes.** Calibration and adjacency provenance; depth if a fabricated row becomes evidence for the canonical key set.

**Smallest safe correction.** Enumerate actual new IDs in the Gate, derive added-by-tier from the committed before/after row maps, and leave S116 unclaimed unless it gains real opened-source evidence through the integrator's authorized work. Do not create a row merely to make the numerical interval contiguous. Do not publish 115 as an observed after count: it is explicitly conditional arithmetic here.

### The r60 total is not re-derived by repeating the closure's total

**Counterexample.** The old fleet report says W0 census 11 and round total 65 (`.ufo/reports/round-60/kotoba.md:65-66`, fleet). The visible `w0-call.json` has 10 named tasks, with matching committed reports. Summing the distinct call files gives 64 tasks and 59 report files. The r60 closure repeats 59/65 and calls its dispatch arithmetic consistent (`corpus/lessons/round-60-verifier-spotcheck.md:120-124`), but that statement is not an independent missing-task receipt.

**Evidence.** `HistoricalReports` names every included call file and prints its role/task/report histogram. `HistoricalCountEdges` extracts the contradictory historical assertions without treating them as measured truth. The W0 names are the client census seats plus `ExecC1Counter`, `ConnSiblingScoped`, and `ExecR1Recount`; the command inventories the actual JSON arrays rather than the report prose.

**Impacted axes.** Calibration and report provenance.

**Smallest safe correction.** Retain the frozen R-a repair (32 vs 29) exactly. For any optional r60 overall-total discussion, say “64 tasks recoverable from the named call artifacts; historical report asserted 65” unless the L1 has a separate actual-dispatch receipt for the missing seat. Do not silently rewrite the closure or infer an absent agent/death from this discrepancy. The discrepancy is a fixable evidence/wording defect; an unsupported stronger historical-total claim is for the canonical judge to reject, not for this seat to admit.

### Manifest size is not completion, and missing reports are not deaths

**Counterexample.** The wave registry/payload names 68 members, yet the observed registry carries no non-null agent IDs. At the `Seats` snapshot, the committed-report inventory is empty while reports are still appearing in the working directory. Both “68 completed, 0 dead” and “none launched” would be unsupported by these artifacts.

**Evidence.** `Seats` prints spec/payload/registry agreement, the role histogram, assigned-ID count, committed report count, and the names of visible working reports. `corpus/QUALITY.md` Q06 requires completed/declared accounting and distinguishes scout-file counts; Q27/Q40 require the last-write output sweep.

**Impacted axes.** Calibration and operability.

**Smallest safe correction.** Label 68 as the manifest/payload size. Bind actual-start/completion/cancellation statements to the L1's observed task-return evidence; at close, join expected report names to committed paths and record any missing/late-report disposition. Include any residual call only after it has its own observed roster and receipt. Do not turn this mid-wave inventory into the final number, and do not derive a death count from missing Markdown.

### World labels, rescore revisions, and live verdicts have different denominators

**Counterexample.** The plan's seven labels are not seven already-run fixtures. W0 is explicitly extra. The old v1 summary has 8 control entries but only 6 completed and 2 cancelled; the old rescore table has 13 concrete revision rows plus 2 missing-world rows, including restored/baseline variants. Counting the rescore table as the frozen W1–W7 universe silently changes identity and denominator. The four eligible entry rows likewise do not mean the v3 checker passed them live.

**Evidence.** `WorldsAndEligibility` derives each cardinality separately from its own committed source. `plans/round-61.md:41-59` freezes the world identities and requires measured outputs; `.ufo/waves/round-60/controls-v2/CtlRescoreV2.md:88-104` exposes the distinct revision rows.

**Impacted axes.** Calibration; depth if a fixture tally is substituted for the declared rejection predicate.

**Smallest safe correction.** Keep a world-ID-to-fixture-to-observed-result receipt. Print `worlds reject 7 of 7; eligible rows pass 4 of 4` as a result only when the frozen integrated self-test actually produces it, with the separate live/base measurements and exit codes required by the plan. The seven-world universe is not widened or reduced by this review. An unrun predicate is not a passed predicate.

## Counting command receipts — exact commands and pasted output

All following `date -u` outputs were collected immediately before the corresponding command. Exit codes are the command process return codes. Commands are intentionally embedded here rather than cited through scratch. No scratch artifact is evidence.

Diagnostic qualifications: the first `HistoricalReports` output's `build_nonreport_artifact_paths` used a stem comparison and omitted a patch sharing a report stem. Its report count was unaffected; use the complete suffix-aware inventory in `HistoricalCountEdges`, not that initial diagnostic list. `ReportMetadata` scans all scorecard tables and also captures a later historical `depth | unchanged` row; that extra text is not a second current axis score or an instruction to alter the axis table.

### Seats

```sh
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-10-23T19:12:33Z
$ python3 -B - <<'PY'
import collections, json, pathlib, subprocess
lane = pathlib.Path('/home/vgpnk/Projects/shokunin/kotoba-shokunin')
tip = subprocess.check_output(['git','-C',str(lane),'rev-parse','--verify','master'], text=True).strip()
def blob(path):
    return subprocess.check_output(['git','-C',str(lane),'show',f'{tip}:{path}'], text=True)
root = '.ufo/waves/round-61/'
spec = json.loads((lane/(root+'wave-spec.json')).read_text())
dispatch = json.loads((lane/(root+'wave-dispatch.json')).read_text())
registry = json.loads((lane/(root+'wave/swarm-registry.json')).read_text())
def histogram(roles):
    return dict(sorted(collections.Counter(roles).items()))
roles = histogram(x['role'] for x in spec['items'])
attack_roles = ['critic','mutation-tester','reviewer']
attack = sum(roles.get(x,0) for x in attack_roles)
paths = subprocess.check_output(['git','-C',str(lane),'ls-tree','-r','--name-only',tip,'--',root+'wave'], text=True).splitlines()
expected = {x['name'] for x in spec['items']}
committed = {pathlib.PurePosixPath(p).stem for p in paths if pathlib.PurePosixPath(p).suffix == '.md'}
working = {p.stem for p in (lane/(root+'wave')).glob('*.md')}
print('tip='+tip)
print(json.dumps({
    'spec_members':len(spec['items']),
    'spec_roles':roles,
    'dispatch_counts':dispatch['counts'],
    'dispatch_tasks':len(dispatch['taskCall']['tasks']),
    'dispatch_roles':histogram(x['agent'] for x in dispatch['taskCall']['tasks']),
    'registry_members':len(registry['members']),
    'registry_roles':histogram(x['role'] for x in registry['members'].values()),
    'registry_nonnull_agentIds':sum(x.get('agentId') is not None for x in registry['members'].values()),
    'conservative_attack_roles':attack_roles,
    'conservative_attack_seats':attack,
    'conservative_attack_denominator':len(spec['items']),
    'conservative_attack_percent':round(100*attack/len(spec['items']),2),
    'committed_expected_reports':len(expected & committed),
    'working_expected_reports':len(expected & working),
    'working_expected_report_names':sorted(expected & working),
    'unexpected_committed_markdown':sorted(committed-expected),
    'spec_equals_dispatch_name_role_pairs':sorted((x['name'],x['role']) for x in spec['items'])==sorted((x['name'],x['agent']) for x in dispatch['taskCall']['tasks'])
}, indent=2))
PY
```

Pasted stdout:
```text
tip=7827628a939b0333c89892dfcedc72e390ccfb60
{
  "spec_members": 68,
  "spec_roles": {
    "connector": 1,
    "critic": 9,
    "executor": 8,
    "mutation-tester": 11,
    "revenger": 1,
    "reviewer": 16,
    "scout": 6,
    "scribe": 12,
    "sentinel": 3,
    "simplifier": 1
  },
  "dispatch_counts": {
    "spawn": 68,
    "resume": 0,
    "total": 68
  },
  "dispatch_tasks": 68,
  "dispatch_roles": {
    "connector": 1,
    "critic": 9,
    "executor": 8,
    "mutation-tester": 11,
    "revenger": 1,
    "reviewer": 16,
    "scout": 6,
    "scribe": 12,
    "sentinel": 3,
    "simplifier": 1
  },
  "registry_members": 68,
  "registry_roles": {
    "connector": 1,
    "critic": 9,
    "executor": 8,
    "mutation-tester": 11,
    "revenger": 1,
    "reviewer": 16,
    "scout": 6,
    "scribe": 12,
    "sentinel": 3,
    "simplifier": 1
  },
  "registry_nonnull_agentIds": 0,
  "conservative_attack_roles": [
    "critic",
    "mutation-tester",
    "reviewer"
  ],
  "conservative_attack_seats": 36,
  "conservative_attack_denominator": 68,
  "conservative_attack_percent": 52.94,
  "committed_expected_reports": 0,
  "working_expected_reports": 11,
  "working_expected_report_names": [
    "CriticC3Axis",
    "ScoutAdjacency",
    "ScoutCounterexample",
    "ScoutFixtureBytes",
    "ScoutPriorCounters",
    "ScribeC3",
    "ScribeLogScore",
    "ScribeQuality",
    "ScribeReportSkeleton",
    "ScribeShonen",
    "ScribeSkillReg"
  ],
  "unexpected_committed_markdown": [],
  "spec_equals_dispatch_name_role_pairs": true
}
```

Exit code: `0`.

### Sources

```sh
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-10-23T19:13:12Z
$ python3 -B - <<'PY'
import collections, json, re, subprocess
lane = '/home/vgpnk/Projects/shokunin/kotoba-shokunin'
tip = subprocess.check_output(['git','-C',lane,'rev-parse','--verify','master'], text=True).strip()
base = 'f3246d1493b60ea1c0d947a19c39f9e08e92f326'
def blob(rev,path):
    return subprocess.check_output(['git','-C',lane,'show',f'{rev}:{path}'], text=True)
def rows(rev):
    found = []
    for line in blob(rev,'corpus/SOURCES.md').splitlines():
        if re.match(r'^ {0,3}\|\s*S[0-9]{3,}\s*\|',line):
            found.append([c.strip() for c in line.strip().split('|')[1:-1]])
    return found
summaries = []
for name,rev in [('r60_base','31092dc6f875370bddd6eb1e4da4ca0d210c56af'),('r60_close','79cf263800552812ce6a45f4bb0313668b576749'),('r61_base',base),('tip',tip)]:
    rs=rows(rev)
    ids=[r[0] for r in rs]
    nums=[int(i[1:]) for i in ids]
    summaries.append({'name':name,'rev':rev,'rows':len(rs),'unique_ids':len(set(ids)),
        'highest_id':max(ids),'missing_ids_below_highest':[f'S{i:03d}' for i in range(1,max(nums)+1) if f'S{i:03d}' not in ids],
        'tiers':dict(sorted(collections.Counter(r[3] for r in rs).items())),
        'statuses':dict(sorted(collections.Counter(r[7] for r in rs).items())),
        'malformed_rows':sum(len(r)!=11 for r in rs),
        'C3_matching_lines':sum('self-assessment-at-writing' in line for line in blob(rev,'corpus/SOURCES.md').splitlines())})
before={r[0]:r for r in rows(base)}
after={r[0]:r for r in rows(tip)}
added=sorted(after.keys()-before.keys())
changed=sorted(i for i in before.keys()&after.keys() if before[i]!=after[i])
r60_before={r[0] for r in rows('31092dc6f875370bddd6eb1e4da4ca0d210c56af')}
r60_after={r[0] for r in rows('79cf263800552812ce6a45f4bb0313668b576749')}
plan=blob(tip,'plans/round-61.md')
source_line=next(line for line in plan.splitlines() if line.startswith('- Sourced claim:'))
refs=[]
for first,last in re.findall(r'S(\d+)\u2013S(\d+)',source_line):
    refs += [f'S{i:03d}' for i in range(int(first),int(last)+1)]
refs += re.findall(r'S\d{3,}',re.sub(r'S\d+\u2013S\d+','',source_line))
planned=sorted(set(refs))
print(json.dumps({'tip':tip,'sources':summaries,
    'r60_added_ids':sorted(r60_after-r60_before),'r60_added_count':len(r60_after-r60_before),
    'r61_added_ids':added,'r61_added_count':len(added),
    'r61_added_by_tier':dict(sorted(collections.Counter(after[i][3] for i in added).items())),
    'r61_removed_ids':sorted(before.keys()-after.keys()),
    'r61_changed_existing_ids':changed,'r61_changed_existing_count':len(changed),
    'frozen_plan_source_sentence':source_line,
    'frozen_plan_unique_source_ids':planned,'frozen_plan_unique_source_count':len(planned),
    'arithmetic_only_rows_if_these_are_the_only_new_ids':len(before)+len(set(planned)-before.keys()),
    'S112_through_S117_inclusive_span_length':117-112+1,
    'source_ids_not_named_by_frozen_claim_sentence_within_that_span':[f'S{i:03d}' for i in range(112,118) if f'S{i:03d}' not in planned]
},indent=2))
PY
```

Pasted stdout:
```text
{
  "tip": "c630c4cbc01ff5e5438ab0033cfadd6e19382ab1",
  "sources": [
    {
      "name": "r60_base",
      "rev": "31092dc6f875370bddd6eb1e4da4ca0d210c56af",
      "rows": 101,
      "unique_ids": 101,
      "highest_id": "S102",
      "missing_ids_below_highest": [
        "S092"
      ],
      "tiers": {
        "A": 99,
        "B": 1,
        "C": 1
      },
      "statuses": {
        "mined": 93,
        "queued": 7,
        "rejected": 1
      },
      "malformed_rows": 0,
      "C3_matching_lines": 0
    },
    {
      "name": "r60_close",
      "rev": "79cf263800552812ce6a45f4bb0313668b576749",
      "rows": 110,
      "unique_ids": 110,
      "highest_id": "S111",
      "missing_ids_below_highest": [
        "S092"
      ],
      "tiers": {
        "A": 108,
        "B": 1,
        "C": 1
      },
      "statuses": {
        "mined": 102,
        "queued": 7,
        "rejected": 1
      },
      "malformed_rows": 0,
      "C3_matching_lines": 0
    },
    {
      "name": "r61_base",
      "rev": "f3246d1493b60ea1c0d947a19c39f9e08e92f326",
      "rows": 110,
      "unique_ids": 110,
      "highest_id": "S111",
      "missing_ids_below_highest": [
        "S092"
      ],
      "tiers": {
        "A": 108,
        "B": 1,
        "C": 1
      },
      "statuses": {
        "mined": 102,
        "queued": 7,
        "rejected": 1
      },
      "malformed_rows": 0,
      "C3_matching_lines": 0
    },
    {
      "name": "tip",
      "rev": "c630c4cbc01ff5e5438ab0033cfadd6e19382ab1",
      "rows": 110,
      "unique_ids": 110,
      "highest_id": "S111",
      "missing_ids_below_highest": [
        "S092"
      ],
      "tiers": {
        "A": 108,
        "B": 1,
        "C": 1
      },
      "statuses": {
        "mined": 102,
        "queued": 7,
        "rejected": 1
      },
      "malformed_rows": 0,
      "C3_matching_lines": 0
    }
  ],
  "r60_added_ids": [
    "S103",
    "S104",
    "S105",
    "S106",
    "S107",
    "S108",
    "S109",
    "S110",
    "S111"
  ],
  "r60_added_count": 9,
  "r61_added_ids": [],
  "r61_added_count": 0,
  "r61_added_by_tier": {},
  "r61_removed_ids": [],
  "r61_changed_existing_ids": [],
  "r61_changed_existing_count": 0,
  "frozen_plan_source_sentence": "- Sourced claim: C1 rests on S112\u2013S115 opened this round; C3 rests on S117.",
  "frozen_plan_unique_source_ids": [
    "S112",
    "S113",
    "S114",
    "S115",
    "S117"
  ],
  "frozen_plan_unique_source_count": 5,
  "arithmetic_only_rows_if_these_are_the_only_new_ids": 115,
  "S112_through_S117_inclusive_span_length": 6,
  "source_ids_not_named_by_frozen_claim_sentence_within_that_span": [
    "S116"
  ]
}
```

Exit code: `0`.

### HistoricalReports

```sh
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-10-23T19:13:12Z
$ python3 -B - <<'PY'
import collections, json, pathlib, re, subprocess
lane = '/home/vgpnk/Projects/shokunin/kotoba-shokunin'
tip = subprocess.check_output(['git','-C',lane,'rev-parse','--verify','master'], text=True).strip()
def blob(path):
    return subprocess.check_output(['git','-C',lane,'show',f'{tip}:{path}'],text=True)
root='.ufo/waves/round-60/'
paths=subprocess.check_output(['git','-C',lane,'ls-tree','-r','--name-only',tip,'--',root],text=True).splitlines()
pathset=set(paths)
spec=json.loads(blob(root+'build-spec.json'))
build_call=json.loads(blob(root+'build-taskcall-sent.json'))
expected={i['name'] for i in spec['items']}
build_reports={pathlib.PurePosixPath(p).stem for p in paths if p.startswith(root+'build/') and p.endswith('.md') and p != root+'build/check_word_counts.fixture.md'}
all_build_files=[p for p in paths if p.startswith(root+'build/')]
summary=[]
for directory,callfile in [('w0','w0-call.json'),('w0b','w0b-call.json'),('controls','controls-call.json'),('controls-v2','controls-v2-call.json'),('build','build-taskcall-sent.json'),('residual','residual-call.json')]:
    call=json.loads(blob(root+callfile))
    tasks=call['tasks']
    expected_paths={root+directory+'/'+i['name']+'.md' for i in tasks}
    present=sorted(expected_paths&pathset)
    extra=sorted(p for p in paths if p.startswith(root+directory+'/') and p.endswith('.md') and p not in expected_paths and not p.endswith('/SUMMARY.md') and not p.endswith('/check_word_counts.fixture.md'))
    summary.append({'directory':directory,'call':root+callfile,'declared_seats':len(tasks),'roles':dict(sorted(collections.Counter(i['agent'] for i in tasks).items())),
        'committed_expected_reports':len(present),'missing_report_names':[pathlib.PurePosixPath(p).stem for p in sorted(expected_paths-pathset)],
        'extra_committed_report_paths':extra,'extra_committed_reports':len(extra),
        'all_committed_reports':len(present)+len(extra)})
print(json.dumps({'tip':tip,
    'build_spec_seats':len(spec['items']),'build_sent_task_count':len(build_call['tasks']),
    'build_spec_roles':dict(sorted(collections.Counter(i['role'] for i in spec['items']).items())),
    'build_committed_report_count':len(build_reports),
    'build_expected_reports_present':len(expected&build_reports),
    'build_missing_expected_report_names':sorted(expected-build_reports),
    'build_extra_committed_report_names':sorted(build_reports-expected),
    'build_all_committed_file_count':len(all_build_files),
    'build_all_committed_markdown_count':sum(p.endswith('.md') for p in all_build_files),
    'build_nonreport_artifact_paths':[p for p in all_build_files if pathlib.PurePosixPath(p).stem not in build_reports],
    'by_call':summary,
    'declared_round_seats':sum(x['declared_seats'] for x in summary),
    'committed_round_expected_reports':sum(x['committed_expected_reports'] for x in summary),
    'committed_round_all_reports':sum(x['all_committed_reports'] for x in summary)
},indent=2))
PY
```

Pasted stdout:
```text
{
  "tip": "c630c4cbc01ff5e5438ab0033cfadd6e19382ab1",
  "build_spec_seats": 32,
  "build_sent_task_count": 32,
  "build_spec_roles": {
    "connector": 1,
    "critic": 4,
    "executor": 7,
    "mutation-tester": 1,
    "reviewer": 3,
    "scout": 1,
    "scribe": 14,
    "sentinel": 1
  },
  "build_committed_report_count": 29,
  "build_expected_reports_present": 29,
  "build_missing_expected_report_names": [
    "ExecBudgetMove",
    "ExecGateRegistry",
    "ExecShonenPointer"
  ],
  "build_extra_committed_report_names": [],
  "build_all_committed_file_count": 33,
  "build_all_committed_markdown_count": 30,
  "build_nonreport_artifact_paths": [
    ".ufo/waves/round-60/build/check_word_counts.fixture.md",
    ".ufo/waves/round-60/build/check_word_counts.py",
    ".ufo/waves/round-60/build/swarm-registry.json"
  ],
  "by_call": [
    {
      "directory": "w0",
      "call": ".ufo/waves/round-60/w0-call.json",
      "declared_seats": 10,
      "roles": {
        "connector": 1,
        "executor": 2,
        "scout": 7
      },
      "committed_expected_reports": 10,
      "missing_report_names": [],
      "extra_committed_report_paths": [],
      "extra_committed_reports": 0,
      "all_committed_reports": 10
    },
    {
      "directory": "w0b",
      "call": ".ufo/waves/round-60/w0b-call.json",
      "declared_seats": 3,
      "roles": {
        "scout": 3
      },
      "committed_expected_reports": 3,
      "missing_report_names": [],
      "extra_committed_report_paths": [],
      "extra_committed_reports": 0,
      "all_committed_reports": 3
    },
    {
      "directory": "controls",
      "call": ".ufo/waves/round-60/controls-call.json",
      "declared_seats": 8,
      "roles": {
        "executor": 4,
        "mutation-tester": 4
      },
      "committed_expected_reports": 6,
      "missing_report_names": [
        "CtlInventedAction",
        "CtlWrongKey"
      ],
      "extra_committed_report_paths": [],
      "extra_committed_reports": 0,
      "all_committed_reports": 6
    },
    {
      "directory": "controls-v2",
      "call": ".ufo/waves/round-60/controls-v2-call.json",
      "declared_seats": 3,
      "roles": {
        "executor": 1,
        "mutation-tester": 2
      },
      "committed_expected_reports": 3,
      "missing_report_names": [],
      "extra_committed_report_paths": [],
      "extra_committed_reports": 0,
      "all_committed_reports": 3
    },
    {
      "directory": "build",
      "call": ".ufo/waves/round-60/build-taskcall-sent.json",
      "declared_seats": 32,
      "roles": {
        "connector": 1,
        "critic": 4,
        "executor": 7,
        "mutation-tester": 1,
        "reviewer": 3,
        "scout": 1,
        "scribe": 14,
        "sentinel": 1
      },
      "committed_expected_reports": 29,
      "missing_report_names": [
        "ExecBudgetMove",
        "ExecGateRegistry",
        "ExecShonenPointer"
      ],
      "extra_committed_report_paths": [],
      "extra_committed_reports": 0,
      "all_committed_reports": 29
    },
    {
      "directory": "residual",
      "call": ".ufo/waves/round-60/residual-call.json",
      "declared_seats": 8,
      "roles": {
        "critic": 1,
        "reviewer": 7
      },
      "committed_expected_reports": 8,
      "missing_report_names": [],
      "extra_committed_report_paths": [],
      "extra_committed_reports": 0,
      "all_committed_reports": 8
    }
  ],
  "declared_round_seats": 64,
  "committed_round_expected_reports": 59,
  "committed_round_all_reports": 59
}
```

Exit code: `0`.

### WorldsAndEligibility

```sh
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-10-23T19:14:07Z
$ python3 -B - <<'PY'
import ast, json, re, subprocess
lane='/home/vgpnk/Projects/shokunin/kotoba-shokunin'
tip=subprocess.check_output(['git','-C',lane,'rev-parse','--verify','master'],text=True).strip()
def blob(path):
    return subprocess.check_output(['git','-C',lane,'show',f'{tip}:{path}'],text=True)
plan=blob('plans/round-61.md')
worldtext=plan.split('Frozen worlds',1)[1].split('\nBefore',1)[0]
worldids=sorted(set(re.findall(r'\bW[1-7]\b',worldtext)))
armids=re.findall(r'^- \*\*(A[1-4])\b',plan,re.M)
def table(text,header):
    section=text.split(header,1)[1]
    result=[]
    for line in section.splitlines():
        if line.startswith('|---') or not line.strip():
            continue
        if not line.startswith('|'):
            break
        result.append([c.strip() for c in line.split('|')[1:-1]])
    return result
entry=table(blob('corpus/knowledge/scoped-rules-round60.md'),'| Client | Rule files | Source | Quote |')
skill=table(blob('SKILL.md'),'| Client | Rule files | Scope key | Action |')
eligible=[r[0] for r in entry]
negatives=[r[0] for r in skill if r[0] not in eligible]
v1rows=table(blob('.ufo/waves/round-60/controls/SUMMARY.md'),'| control | role | S (snapshots) | F (live) | exit | predicate |')
v2rows=table(blob('.ufo/waves/round-60/controls-v2/SUMMARY.md'),'| control | role | worlds | result under v2 | predicate |')
rescore=table(blob('.ufo/waves/round-60/controls-v2/CtlRescoreV2.md'),'| control | world rev | S | F | exit | predicate under v2 |')
paths=subprocess.check_output(['git','-C',lane,'ls-tree','-r','--name-only',tip,'--','.ufo/waves/round-61/'],text=True).splitlines()
ctype=ast.parse(blob('verifiers/check_routed_repairs.py'))
repairfn=next(n for n in ctype.body if isinstance(n,ast.FunctionDef) and n.name=='check_repairs')
repairlabels=[]
for n in ast.walk(repairfn):
    if isinstance(n,ast.JoinedStr) and n.values and isinstance(n.values[0],ast.Constant) and isinstance(n.values[0].value,str) and re.match(r'^R-[a-f] ',n.values[0].value):
        repairlabels.append(n.values[0].value)
base=blob('.ufo/waves/round-61/controls/C2-base.txt')
census=blob('.ufo/waves/round-61/census-before.txt')
print(json.dumps({'tip':tip,
    'frozen_arms':armids,'frozen_arm_count':len(armids),
    'frozen_attack_world_ids':worldids,'frozen_attack_world_count':len(worldids),
    'frozen_extra_world_ids':['W0'] if 'W0' in worldtext else [],
    'frozen_total_world_slots_including_W0':len(worldids)+int('W0' in worldtext),
    'entry_eligible_clients':eligible,'entry_eligible_count':len(eligible),
    'entry_source_ids':[r[2] for r in entry],
    'skill_client_count':len(skill),'skill_negative_clients':negatives,'skill_negative_count':len(negatives),
    'v1_control_summary_rows':len(v1rows),
    'v1_control_summary_completed_rows':sum('cancelled' not in r[5] for r in v1rows),
    'v1_control_summary_cancelled_rows':sum('cancelled' in r[5] for r in v1rows),
    'v2_control_summary_outcome_groups':len(v2rows),
    'v2_control_summary_groups_marked_MET':sum(r[-1]=='**MET**' for r in v2rows),
    'rescore_concrete_revision_rows':sum(bool(re.fullmatch(r'`[0-9a-f]{40}`',r[1])) for r in rescore),
    'rescore_missing_world_rows':sum(r[1]=='**none**' for r in rescore),
    'frozen_C2_repair_labels':sorted(repairlabels),'frozen_C2_repair_count':len(repairlabels),
    'C2_base_committed_receipt_summary':[line for line in base.splitlines() if line.startswith(('routed repairs','base-exit='))],
    'census_before_recorded_W04_lines':sum('\tW04\t' in line for line in census.splitlines()),
    'census_before_recorded_final_line':census.splitlines()[-1],
    'committed_r61_files_outside_wave':[p for p in paths if not p.startswith('.ufo/waves/round-61/wave/')],
    'v3_world_rejections_and_live_passes_executed_by_this_seat':False
},indent=2))
PY
```

Pasted stdout:
```text
{
  "tip": "c630c4cbc01ff5e5438ab0033cfadd6e19382ab1",
  "frozen_arms": [
    "A1",
    "A2",
    "A3",
    "A4"
  ],
  "frozen_arm_count": 4,
  "frozen_attack_world_ids": [
    "W1",
    "W2",
    "W3",
    "W4",
    "W5",
    "W6",
    "W7"
  ],
  "frozen_attack_world_count": 7,
  "frozen_extra_world_ids": [
    "W0"
  ],
  "frozen_total_world_slots_including_W0": 8,
  "entry_eligible_clients": [
    "Claude Code",
    "VS Code",
    "Copilot CLI",
    "Cursor"
  ],
  "entry_eligible_count": 4,
  "entry_source_ids": [
    "S103",
    "S105",
    "S106",
    "S108"
  ],
  "skill_client_count": 7,
  "skill_negative_clients": [
    "Codex",
    "Gemini CLI",
    "opencode"
  ],
  "skill_negative_count": 3,
  "v1_control_summary_rows": 8,
  "v1_control_summary_completed_rows": 6,
  "v1_control_summary_cancelled_rows": 2,
  "v2_control_summary_outcome_groups": 6,
  "v2_control_summary_groups_marked_MET": 2,
  "rescore_concrete_revision_rows": 13,
  "rescore_missing_world_rows": 2,
  "frozen_C2_repair_labels": [
    "R-a count correction: ",
    "R-b landed-scope names: ",
    "R-c base-measure pointer: ",
    "R-d census-after file: ",
    "R-e byte-exact criterion + M91: ",
    "R-f controls-ancestry receipt: "
  ],
  "frozen_C2_repair_count": 6,
  "C2_base_committed_receipt_summary": [
    "routed repairs verified 0 of 6",
    "base-exit=1"
  ],
  "census_before_recorded_W04_lines": 13,
  "census_before_recorded_final_line": "exit=0",
  "committed_r61_files_outside_wave": [
    ".ufo/waves/round-61/census-before.txt",
    ".ufo/waves/round-61/controls/C2-base.txt",
    ".ufo/waves/round-61/wave-dispatch.json",
    ".ufo/waves/round-61/wave-spec.json"
  ],
  "v3_world_rejections_and_live_passes_executed_by_this_seat": false
}
```

Exit code: `0`.

### HistoricalCountEdges

```sh
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-10-23T19:14:07Z
$ python3 -B - <<'PY'
import json, pathlib, re, subprocess
lane='/home/vgpnk/Projects/shokunin/kotoba-shokunin'
tip=subprocess.check_output(['git','-C',lane,'rev-parse','--verify','master'],text=True).strip()
root='.ufo/waves/round-60/build/'
paths=subprocess.check_output(['git','-C',lane,'ls-tree','-r','--name-only',tip,'--',root],text=True).splitlines()
nonreports=[p for p in paths if not p.endswith('.md') or p.endswith('/check_word_counts.fixture.md')]
report=pathlib.Path('/home/vgpnk/Projects/shokunin/.ufo/reports/round-60/kotoba.md').read_text()
claim_total=re.search(r'Round total: (\d+) seats',report).group(1)
claim_w0=re.search(r'W0 census (\d+)',report).group(1)
spec=json.loads(subprocess.check_output(['git','-C',lane,'show',tip+':.ufo/waves/round-60/build-spec.json'],text=True))
committed_reports={pathlib.PurePosixPath(p).stem for p in paths if p not in nonreports}
expected={i['name'] for i in spec['items']}
print(json.dumps({'tip':tip,
    'build_committed_nonreport_paths':nonreports,'build_committed_nonreport_count':len(nonreports),
    'build_naive_file_count':len(paths),'build_naive_markdown_count':sum(p.endswith('.md') for p in paths),
    'build_manifest_matched_report_count':len(expected&committed_reports),
    'build_missing_report_count':len(expected-committed_reports),
    'file_minus_report_count':len(paths)-len(expected&committed_reports),
    'markdown_minus_report_count':sum(p.endswith('.md') for p in paths)-len(expected&committed_reports),
    'historical_fleet_report_asserted_W0_seats':int(claim_w0),
    'historical_fleet_report_asserted_total_seats':int(claim_total)
},indent=2))
PY
```

Pasted stdout:
```text
{
  "tip": "c630c4cbc01ff5e5438ab0033cfadd6e19382ab1",
  "build_committed_nonreport_paths": [
    ".ufo/waves/round-60/build/ExecIndexCorpus.patch",
    ".ufo/waves/round-60/build/check_word_counts.fixture.md",
    ".ufo/waves/round-60/build/check_word_counts.py",
    ".ufo/waves/round-60/build/swarm-registry.json"
  ],
  "build_committed_nonreport_count": 4,
  "build_naive_file_count": 33,
  "build_naive_markdown_count": 30,
  "build_manifest_matched_report_count": 29,
  "build_missing_report_count": 3,
  "file_minus_report_count": 4,
  "markdown_minus_report_count": 1,
  "historical_fleet_report_asserted_W0_seats": 11,
  "historical_fleet_report_asserted_total_seats": 65
}
```

Exit code: `0`.

### ReportMetadata

```sh
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-10-23T19:14:51Z
$ python3 -B - <<'PY'
import hashlib, json, pathlib, re, subprocess
lane='/home/vgpnk/Projects/shokunin/kotoba-shokunin'
tip=subprocess.check_output(['git','-C',lane,'rev-parse','--verify','master'],text=True).strip()
def raw(path):
    return subprocess.check_output(['git','-C',lane,'show',f'{tip}:{path}'])
def blob(path):
    return raw(path).decode()
axes=[]
for line in blob('SCORECARD.md').splitlines():
    if line.startswith('|'):
        fields=[c.strip() for c in line.split('|')[1:-1]]
        if fields and fields[0] in ('depth','consistency (calibration sub-axis)','adjacency (advisory)'):
            axes.append({'axis':fields[0],'recorded_score':fields[1]})
marks=re.findall(r'^- \[([ x~])\]',blob('SHONEN.md'),re.M)
paths=set(subprocess.check_output(['git','-C',lane,'ls-tree','-r','--name-only',tip],text=True).splitlines())
entry='corpus/knowledge/writing-revision-calibration-round61.md'
source=blob('corpus/SOURCES.md')
lesson=blob('.ufo/waves/round-60/receipts/freeze2-selftest.txt')
readme=blob('corpus/README.md')
print(json.dumps({'tip':tip,
    'frozen_claim_heading_count':len(re.findall(r'^### C[1-3] ',blob('plans/round-61.md'),re.M)),
    'recorded_scores_not_new_verdicts':axes,
    'SHONEN_box_count':len(marks),
    'SHONEN_asserted_marks':marks.count('~'),
    'SHONEN_non_author_checked_marks':marks.count('x'),
    'skill_line_count':len(blob('SKILL.md').splitlines()),
    'C3_source_match_count':sum('self-assessment-at-writing' in line for line in source.splitlines()),
    'C3_entry_committed':entry in paths,
    'C3_README_matching_lines':sum(pathlib.PurePosixPath(entry).name in line for line in readme.splitlines()),
    'scoped_rules_counter_committed_sha256':hashlib.sha256(raw('verifiers/check_scoped_rules.py')).hexdigest(),
    'routed_repairs_counter_committed_sha256':hashlib.sha256(raw('verifiers/check_routed_repairs.py')).hexdigest(),
    'r60_freeze_receipt_documentary_lines':[line for line in lesson.splitlines() if line.startswith(('self-test:','scoped rule files','exit','base-exit'))],
    'no_lane_verifier_executed_by_this_seat':True
},indent=2))
PY
```

Pasted stdout:
```text
{
  "tip": "c630c4cbc01ff5e5438ab0033cfadd6e19382ab1",
  "frozen_claim_heading_count": 3,
  "recorded_scores_not_new_verdicts": [
    {
      "axis": "depth",
      "recorded_score": "9"
    },
    {
      "axis": "consistency (calibration sub-axis)",
      "recorded_score": "10"
    },
    {
      "axis": "adjacency (advisory)",
      "recorded_score": "8.0 \u2014 was 7.5"
    },
    {
      "axis": "depth",
      "recorded_score": "unchanged"
    }
  ],
  "SHONEN_box_count": 4,
  "SHONEN_asserted_marks": 4,
  "SHONEN_non_author_checked_marks": 0,
  "skill_line_count": 591,
  "C3_source_match_count": 0,
  "C3_entry_committed": false,
  "C3_README_matching_lines": 0,
  "scoped_rules_counter_committed_sha256": "ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a",
  "routed_repairs_counter_committed_sha256": "61d8c5831d1904cba921ccc547b8308753c1726e704d4cc2b5cec10d60c77356",
  "r60_freeze_receipt_documentary_lines": [
    "self-test: 0 failure(s) over 318 assertions",
    "exit 0",
    "exit 1",
    "scoped rule files backed on committed snapshots 0 of 0; live not run"
  ],
  "no_lane_verifier_executed_by_this_seat": true
}
```

Exit code: `0`.

### DecisionCardinalities

```sh
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-10-23T19:15:29Z
$ python3 -B - <<'PY'
import collections, json, re, subprocess
lane='/home/vgpnk/Projects/shokunin/kotoba-shokunin'
tip=subprocess.check_output(['git','-C',lane,'rev-parse','--verify','master'],text=True).strip()
def blob(path):
    return subprocess.check_output(['git','-C',lane,'show',f'{tip}:{path}'],text=True)
skill=blob('SKILL.md').split('| Client | Rule files | Scope key | Action |',1)[1].split('\n## ',1)[0]
rows=[[c.strip() for c in l.split('|')[1:-1]] for l in skill.splitlines() if l.startswith('|') and not l.startswith('|---')]
keys=[]
for r in rows:
    key=re.match(r'^`([^`]+)`',r[2])
    if key:
        keys.append({'client':r[0],'key':key.group(1)})
spec=json.loads(blob('.ufo/waves/round-60/build-spec.json'))
paths=set(subprocess.check_output(['git','-C',lane,'ls-tree','-r','--name-only',tip,'--','.ufo/waves/round-60/build'],text=True).splitlines())
returned=[i for i in spec['items'] if '.ufo/waves/round-60/build/'+i['name']+'.md' in paths]
print(json.dumps({'tip':tip,
    'scoped_rule_client_rows':len(rows),
    'decision_columns_per_client':3,
    'decision_cells_structural_not_semantically_verified':sum(len(r)-1 for r in rows),
    'scope_key_client_bindings':keys,'scope_key_client_binding_count':len(keys),
    'distinct_scope_key_spellings':sorted({x['key'] for x in keys}),
    'distinct_scope_key_spelling_count':len({x['key'] for x in keys}),
    'r60_build_committed_report_roles':dict(sorted(collections.Counter(i['role'] for i in returned).items())),
    'r60_build_missing_expected_report_roles':dict(sorted(collections.Counter(i['role'] for i in spec['items'] if i not in returned).items()))
},indent=2))
PY
```

Pasted stdout:
```text
{
  "tip": "3dbf00776a491626558a8ca4b56b193fd376bf01",
  "scoped_rule_client_rows": 7,
  "decision_columns_per_client": 3,
  "decision_cells_structural_not_semantically_verified": 21,
  "scope_key_client_bindings": [
    {
      "client": "Claude Code",
      "key": "paths"
    },
    {
      "client": "VS Code",
      "key": "applyTo"
    },
    {
      "client": "Copilot CLI",
      "key": "applyTo"
    },
    {
      "client": "Cursor",
      "key": "globs"
    }
  ],
  "scope_key_client_binding_count": 4,
  "distinct_scope_key_spellings": [
    "applyTo",
    "globs",
    "paths"
  ],
  "distinct_scope_key_spelling_count": 3,
  "r60_build_committed_report_roles": {
    "connector": 1,
    "critic": 4,
    "executor": 4,
    "mutation-tester": 1,
    "reviewer": 3,
    "scout": 1,
    "scribe": 14,
    "sentinel": 1
  },
  "r60_build_missing_expected_report_roles": {
    "executor": 3
  }
}
```

Exit code: `0`.

## Disposition

This seat produced the scoped numerical ledger and attacked the strongest local count/provenance substitutions. No production source, fixture, LOG, lesson, row, fleet report, or frozen predicate was edited. No checks are represented as passed beyond the counting commands whose receipts are pasted above. Integration-time measurements and task-disposition evidence belong to the L1, not to this read-only review.

Installs: no installs.
Blockers: none for this scoped review; final integration-time outcomes are explicitly unobserved, not invented.
Attacked: report-count denominators, declared-versus-committed seats, source-row interval inflation, and world-label-versus-measured-result substitution.
