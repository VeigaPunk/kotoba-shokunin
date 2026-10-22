FAILS — C1 as landed, on its classification layer: the stated rule is misapplied (kake and kasegi are `none` although kotoba's own description states the split), and the content guard passes a pair whose 20 classifications are all wrong. HOLDS-BOUNDED for the narrower facts: 20 pinned rows exist, every scope quote re-reads at its pin, and the mechanical columns are correct.

Seat: KotobaR49.CriticC1Landed (critic, leaf). Judged bytes: master `c48793dbe5eb30cd661f42ecad7399ae94e3d7ad` (base `a5adc146`). Scratch: `/fast/scratch/hyaku/kotoba-r49/falsify/CriticC1Landed/` (private clone checked out at `c48793db`; `mutate.py`, `recompute.py`, `mut-allnone/`, `mut-worst/`). Date 2026-10-22, 11:25Z–11:50Z. Tools installed or upgraded: none.

## Findings

F1 — The guard does not close the content-blind gap for the claimed content, the classification (impacted axes: adjacency, calibration; Q25).
The claim is "classified, pinned rows". The guard checks three things: that each census scope quote is a substring of the cited line (plus or minus 2 lines) at the pin, that the lane set is the full fleet, and that each PROVINCE row's classification and commit equal the census row's. Nothing ties a classification to evidence. Counterexamples were built from the landed files in scratch:
- `mut-allnone`: all 7 `adjacent` rows flipped to `none` in both files. Guard exit 0, `rows 20 verified 20`, `province rows 20 matched 20`. Row counter: 20.
- `mut-worst`: all rows `none`; every quote cut to its first 3 characters (chousa, kengaku and kotodama all read `Dom`); `names kotoba` is `no` for kengaku and kotodama (truly `yes`); `arbitration` is `no` everywhere; the skill-file cell is `NONE` for all 20 (17 have `SKILL.md`); every PROVINCE boundary cell is `x`. Guard exit 0, `rows 20 verified 20`, `province rows 20 matched 20`. Row counter: 20.
The lesson's must-fail evidence (M29: "kasegi reclassified `adjacent`" exits 1) mutates one side only. It shows the guard enforces agreement between the two files, not that the classification is correct. Q25 asks for "a content guard whose exit code changes on that mutant" with the claimed content falsified. A two-sided falsification leaves the exit code unchanged.
Further gaps in the same instrument:
- (a) The docstring says "the path part of `path:line` is one of the skill file(s) the row names". The code at `check_sibling_census.py:410-413` deliberately skips that check, and `mut-worst` passes with `NONE` everywhere. This is false provenance inside the instrument.
- (b) There is no minimum quote length. A 3-character substring counts as a located scope quote.
- (c) The `names kotoba` and `arbitration` columns, which the entry calls "mechanical", are never recomputed.
- (d) The PROVINCE boundary cell, which holds every overlap citation (for example kagi `corpus/README.md:97` and kama `cross-lane-scope.md:29`), is unchecked.
- (e) The scope quote is each sibling's own domain line, so even a verified quote is no evidence for the classification.

F2 — The classification rule is not applied consistently (adjacency).
The entry's rule reads: `adjacent` = "either side's committed scope surfaces (SKILL.md, PROVINCE.md, corpus files) state a split of one artifact, function or trigger area between the sibling and kotoba". kotoba's own `SKILL.md` description (lines 10-12 at `c48793db`) reads: "Sibling boundary: the five `*-shokunin` domain skills (kagi, kake, kasegi, kengaku, kumitate) own their own SKILL.md content — this skill audits and reports; fixes route to the owning lane." That sentence is a split of one artifact, stated on kotoba's own scope surface, and it names kake and kasegi. Under the stated rule both rows must be `adjacent`; both are `none` ("no claim on kotoba ground").
Both sides corroborate the split:
- kotoba's corpus names kake in 20 files and kasegi in 21 files outside the census entry and the round-49 lesson.
- kake `corpus/lessons/round-5-aggregator-mirror-pathless-cli-invocation.md:4` and kasegi `corpus/lessons/round-5-aggregator-mirror-ambiguous-citation-base.md:4` both record "Filed by: kotoba round-5 report … Cross-domain observations to relay", an audit of their own SKILL.md.
The kotodama override follows the opposite reading. It counts a one-sided refusal by name ("NOT prompt/skill craft (kotoba-shokunin)") as a published split. The same one-sided reading applied to kotoba's description flips kake and kasegi. Either reading changes the table: with the either-side reading, adjacent becomes at least 9 (kake and kasegi added). The override's justification is sound only if it is applied symmetrically, and it was not.

F3 — tameshi's `adjacent` call rests on a surface the rule excludes (adjacency; false provenance, bounded).
The PROVINCE row cites `tameshi .ufo/waves/round-16/w1/Overlap1.md:136`, a wave report, not a SKILL.md, PROVINCE.md or corpus file. The seat itself says: "tameshi records the same relation only in its wave report and kill-rate ledger, not in PROVINCE.md § Adjacent" (`CensusTameshi.md:44-45`). tameshi's corpus places kotoba's instruments outside its universe: "Out of the census universe (sightings only, not queued, not surveyed): … kotoba `verifiers/*`" (`fleet-suite-census.md:623-625` at `3b20f073`). On kotoba's side, the only surface outside the census that names tameshi is `PROVINCE.md` itself, the row being written. That support is circular, and it is the same kind of support the round withdrew for kasegi. tameshi may well be `adjacent`, but the stated rule does not derive it from the cited bytes.

F4 — Is this an adjacency move or an inventory? Partly real, mostly inventory (adjacency).
AXES.md:16 reads: "evidence belonging to another domain reported, not absorbed | Lane reports name contested scope; integrator arbitrates".
Real moves:
- The unsourced kasegi "prompt-injection" clause is withdrawn (M30).
- kama is newly `adjacent`, with a sourced split (kama `cross-lane-scope.md:29`, verified).
- The kotodama non-reciprocity is found.
- The kagi `$HOME/.config/opencode` owner and the kaidoku/revenger overlap are named.
Inventory: 13 of 20 rows say "no claim on kotoba ground" with no evidence the guard can check. 0 rows are `contested`, so no lane report names contested scope.
The PROVINCE kaidoku row claims "open arbitration … reported to the integrator". At `c48793db` there is no round-49 report under kotoba `.ufo/reports/` (latest is `round-45`), and the fleet `.ufo/l0-questions.md` has no kotoba line about kaidoku/revenger or the opencode owner. [INFERENCE] The phrase may refer to kaidoku's own records; no kotoba-side report was observed.

F5 — Learning claim: holds-bounded, but Core and Frontier now contradict each other (duplicate authority).
New admitted knowledge exists: the Gate admits 1 entry, and the entry carries the swept negative finding "no documented tie-break" from S022, S023 and S018. `PROVINCE.md:17` adds Core "Sibling arbitration (round 49, moved from Frontier)". However:
- `PROVINCE.md:23` Frontier still lists "sibling arbitration clauses".
- The Core line itself says "Still open: kotoba's own description names 5 of 20 siblings".
- `corpus/README.md:113-122` keeps the area as a Known gap with an append.
The area is claimed held and open at once (premature saturation). Most of the Core content is a fleet inventory at moving pins; the transferable knowledge is the tie-break finding.

## Smallest safe correction
1. State one rule and re-derive all 20 rows from it. Under the either-side reading, kake and kasegi become `adjacent`. Under a sibling-side-only reading, re-justify kotodama from kotodama's bytes (it holds) and tameshi from a corpus or scope file (currently it does not). Re-declare the count from the result.
2. Guard: add a per-row evidence cell for `adjacent` and `contested` rows (`repo@commit:path:line` + quote, either side) that the guard re-reads. For `none` rows, add a sweep command whose 0 the guard re-runs. Recompute the two mechanical columns. Set a minimum quote length. Either implement the docstring's path-cell check or delete the sentence. Show must-fail on a two-sided flip.
3. Remove "sibling arbitration clauses" from the PROVINCE Frontier list or narrow the Core line. File the kaidoku/revenger and opencode-owner items in a round-49 lane report or L0 line, or drop "reported to the integrator".
All three are fixable defects, not tradeoffs, but the claim as written ("classified" rows guarded against false content) should not be admitted as is.

## Evidence (commands run; exit codes verbatim)
- Guard on the landed pair (scratch clone at `c48793db`): `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` → `rows 20 verified 20`, `province rows 20 matched 20`, exit=0.
- Self-test: `python3 -B verifiers/check_sibling_census.py --self-test` → `self-test: 0 failure(s) over 39 assertions`, exit=0. No two-sided-flip arm.
- `python3 mutate.py <clone> mut-allnone allnone`, then the guard on `mut-allnone/census.md --province mut-allnone/PROVINCE.md` → `rows 20 verified 20`, `province rows 20 matched 20`, exit=0. Row counter (the plan's awk/grep command on `mut-allnone/PROVINCE.md`) → 20.
- The same for `mut-worst` → `rows 20 verified 20`, `province rows 20 matched 20`, exit=0. Row counter → 20. `grep -E '^\| (kengaku|kotodama|chousa) ' mut-worst/census.md` shows `| NONE | none | no | no | … | Dom |`.
- `python3 -B recompute.py <census>` (recomputes `names kotoba` and `arbitration` from each pinned description) → `mismatches 0`, exit=0. The landed mechanical values are correct; the guard just does not check them.
- `sed -n 1,20p SKILL.md` (kotoba, lane checkout at `c48793db`) shows the "Sibling boundary: … (kagi, kake, kasegi, kengaku, kumitate) own their own SKILL.md content — this skill audits and reports" text.
- Per lane, `git grep -l -w -i <lane> c48793db -- SKILL.md PROVINCE.md 'corpus/*' ':!corpus/knowledge/sibling-overlap-census-round49.md' ':!corpus/lessons/round-49.md' | wc -l` → kake 20, kasegi 21, every other `none` lane 1–4 (exit 0).
- `git -C kake-shokunin grep -n -i kotoba e73d48bb -- … 'corpus/*'` and the same for kasegi `1fafde8f` show the "Filed by: kotoba round-5 report" lines (exit 0).
- `git -C tameshi-shokunin show 3b20f073:corpus/knowledge/fleet-suite-census.md | sed -n 620,627p` shows "Out of the census universe … kotoba `verifiers/*`".
- `git grep -l -i -w tameshi c48793db -- SKILL.md PROVINCE.md 'corpus/*' ':!corpus/knowledge/sibling-overlap-census-round49.md'` → `PROVINCE.md` only.
- Boundary citations re-read at the pins with `git show <pin>:<path> | sed -n`: kagi `corpus/README.md:97`, kama `cross-lane-scope.md:29`, kumitate `PROVINCE.md:27` and kotodama `MINT.md:20` hold. tameshi's citation resolves to a wave report.
- `ls .ufo/reports/round-49` → "No such file or directory" (exit 2). `grep -n -i -E 'revenger|kotodama' /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` shows no kotoba round-49 line.
- `git show c48793db:PROVINCE.md` shows line 17 (Core, "moved from Frontier") and line 23 (Frontier still listing "sibling arbitration clauses").
Lane writes: this report only. No git write or jj commands were run anywhere.
