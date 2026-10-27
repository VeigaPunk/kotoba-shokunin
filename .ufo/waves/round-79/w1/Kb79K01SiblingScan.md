# Kb79K01 sibling-overlap scan (round 79 w1)

Axes considered: C1 consistency/calibration (tip-battery result matches lane state); C2 depth (sourced per-client `allowed-tools` semantics). This is an overlap/boundary scan, not a claim-score or counter run.

## Scope and method

Read `plans/round-79.md` first (absolute lane path); read `PROVINCE.md` § Adjacent and `corpus/knowledge/sibling-overlap-census-round74.md`, including the recorded 20-row pins and boundary descriptions. The path sweep was over every sibling `*-shokunin` repository except kotoba, selecting `SKILL.md`, `PROVINCE.md`, `corpus/README.md`, and files directly in `corpus/knowledge/` (1,031 files). Command, run from `/home/vgpnk/Projects/shokunin`:

```sh
python3 -c 'import glob,re,os; root="/home/vgpnk/Projects/shokunin"; p=re.compile(r"allowed-tools|allowed_tools|tip battery|corpus-baseline|corpus integrity",re.I); files=[]
for lane in glob.glob(root+"/*-shokunin"):
 if lane.endswith("/kotoba-shokunin"): continue
 files += [x for x in [lane+"/SKILL.md",lane+"/PROVINCE.md",lane+"/corpus/README.md"] if os.path.isfile(x)]+glob.glob(lane+"/corpus/knowledge/*")
h=[]
for x in files:
 try:
  for i,s in enumerate(open(x,errors="replace"),1):
   if p.search(s): h.append((x,i,s.strip()))
 except OSError: pass
for x,i,s in h: print(f"{x}:{i}:{s}")
print("FIELD_OR_BATTERY_HITS",len(h))'
```

Observed output: `FIELD_OR_BATTERY_HITS 0`. This exact targeted sweep supports no hits for the C2 field-name variants or the C1 verifier/baseline terms in the selected sibling files. A broader exploratory regex sweep including generic `frontmatter` produced 42 hits; those are mostly unrelated frontmatter mentions in kumitate's Kimi agent/plugin documentation, kagi config-layering, tameshi fixture notes, and other unrelated corpus records. It did not reveal an `allowed-tools`/`allowed_tools` field semantics hit. The exploratory scan was a Python walk of the same path selection with `allowed-tools|allowed_tools|frontmatter|tip battery|corpus-baseline|corpus integrity` (case-insensitive), reporting full absolute path and line. Do not infer absence outside this specified selection.

The requested shell-style search `grep -rlE 'allowed-tools|allowed_tools'` was not run; the Python sweep above is the actual evidence and exact command. A separate tool search for the field and battery terms over sibling roots returned `No matches found` (tool glob scope `/home/vgpnk/Projects/shokunin/*-shokunin`).

## Hits and boundary implications

No sibling hit for `allowed-tools` / `allowed_tools`, `tip battery`, `corpus-baseline`, or `corpus integrity` occurred in the selected files, hence there are no such hit lines to cite. The already-pinned adjacent boundary rows relevant to likely neighbors remain:

- kumitate adjacent: `PROVINCE.md:67` records dispatch/orchestration tooling and routes prompt/skill craft to kotoba; this is a tooling/runtime boundary, not the client-facing meaning of a skill's `allowed-tools` field.
- tameshi adjacent: `PROVINCE.md:74` records reusable fixture/mutation method while each lane retains its gate; no field semantics claim.
- chousa adjacent: `PROVINCE.md:57` records research method ownership; no field semantics claim.
- kagi adjacent: `PROVINCE.md:60` records secrets/vault scope; no field semantics claim.

These are the current kotoba PROVINCE rows, not newly inspected sibling bytes or fresh re-pins. The round-74 census text says classifications/pins and the counter validate their row data; it also states that classification judgment is not measured (`sibling-overlap-census-round74.md:139-142`). Thus this scan finds no basis to change a sibling class or boundary. It does not contradict the round-79 claim: a new per-client documentation map is compatible with the census's general skill-craft ownership, and no sibling in this sweep holds that field-specific claim. No duplicate field-specific held claim was found.

For shared-verifier concern: the target sweep returned zero for `tip battery`, `corpus-baseline`, and `corpus integrity`; it did not sweep sibling `verifiers/` directories, so it cannot establish their absence there. C1's plan explicitly scopes repair to kotoba and the tip battery evaluates the measured lane repo; no shared sibling path was identified by this assignment's file scope. Do not claim a repository-wide verifier-path audit from these results.

## PROVINCE/Core interaction and recommendation

The sibling re-read counter is explicitly `verifiers/check_sibling_reread.py --rev <rev>` and its entry names that recheck in `sibling-overlap-census-round74.md:3,158-164`. Its implementation parses the `## Adjacent` table and compares province rows (`check_sibling_reread.py:139-151,377-418,709-735`); it does not require `PROVINCE.md` byte identity or inspect `## Core` as a byte-equality condition. The requested Q73 grep was performed with the regex `differs from the base|byte-identical` against `verifiers/*.py`; relevant output is `verifiers/check_province_core.py:24-26,45-50,103-108`, not a condition in `check_sibling_reread.py`.

A round-79 `## Core` bullet therefore does not, by itself, trip the sibling reread counter's identity/adjacent-row conditions. Separate no-harm caveat: `check_province_core.py` says `## Frontier` and `## Adjacent` must match base (with its explicit Adjacent errata SHA exception) at lines 23-26, 44-50, and enforces that at 103-108; it then counts Core bullets naming entry/counter/round at 109-125. Additions confined to Core do not alter those sections. Another tree-level scope caveat from the round-79 plan: C2's own counter requires a Core bullet naming its entry path (plan § C2, line 44), so the intended Core addition is relevant to C2 but is not a sibling-census change.

Recommendation: report-only for `PROVINCE.md` § Adjacent. Add no new sibling row, classification, or boundary statement for this field absent an actual sibling ownership claim. A C2 Core bullet may be warranted by C2's own declared predicate, but it belongs in `## Core`, not § Adjacent.

## Evidence / verification

- Read: `plans/round-79.md`; `PROVINCE.md` lines 41-75; `corpus/knowledge/sibling-overlap-census-round74.md` lines 1-11, 139-164; `verifiers/check_sibling_reread.py`; `verifiers/check_province_core.py`.
- Search: targeted sibling sweep command above, output `FIELD_OR_BATTERY_HITS 0`; broader terms sweep found generic frontmatter hits but no allowed-tools field semantics. `grep -n 'differs from the base\|byte-identical' verifiers/*.py` equivalent search was run via repository regex search; relevant hit locations are `check_province_core.py:24-26,45-50,103-108` and `check_tip_battery.py:50-57,121-124,328-331`. The latter confirms tip-battery instrument-pin and spotcheck identity language, not sibling-path sharing.
- No sibling files were edited and no counters or tests were run.

VERDICT: No sibling holds `allowed-tools` semantics or the searched C1 battery/baseline terms in the scoped files; retain the 20-row Adjacent census unchanged; Core-only addition does not violate adjacent-section identity.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/w1/Kb79K01SiblingScan.md