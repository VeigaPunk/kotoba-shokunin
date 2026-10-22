# RowKengaku — falsify of census row `kengaku` and PROVINCE.md:46

VERDICT: FAILS for PROVINCE.md:46 (kengaku boundary note; its "route telemetry" clause presents a surface the sibling says is absent). HOLDS-BOUNDED for census row `kengaku` in corpus/knowledge/sibling-overlap-census-round49.md (classification `adjacent` holds on the rule's scope-surface reading, but the row's "not contested" rationale is wrong and the guard does not check its mechanical cells). HOLDS for the commit, branch, scope quote and both mechanical cells (re-derived from pinned bytes).

Judged: kotoba-shokunin master c48793db (private clone /fast/scratch/hyaku/kotoba-r49/falsify/RowKengaku/kotoba-shokunin). Sibling pin: kengaku-shokunin 1f3b0f1ec41ec297130e8944ff97968d32324632.

Path convention: `PROVINCE.md:46`, `corpus/knowledge/sibling-overlap-census-round49.md`, `verifiers/…` and `.ufo/waves/round-49/…` are kotoba's (c48793db). Unprefixed paths in findings 1-8 (`PROVINCE.md:3/8/15`, `SKILL.md:3`, `plans/…`, `SCORECARD.md`, `corpus/…`, `.ufo/waves/round-25/…`) are inside kengaku-shokunin at the pin.

## Findings (severity order)

1. MAJOR — PROVINCE.md:46 states an absent surface as current scope.
   Note: "LLM and model evaluation and route telemetry; kengaku keeps measured capability effects of prompt format, kotoba owns the craft rules (kengaku description, `SKILL.md:3`)".
   - Sibling's committed bytes say route telemetry is not live. SKILL.md:3: "route telemetry (~/Projects/bounties/ledger/telemetry.jsonl) are historical, absent since 2026-10-15". PROVINCE.md:8 header: "route telemetry absent". PROVINCE.md:15: "Route telemetry | ... — **ABSENT**, reconfirmed round 14 ... never treat the path as live".
   - Only PROVINCE.md:3 (Domain line) still says "scopes ... route telemetry". The kotoba note copied that stale half and dropped the ABSENT qualifier.
   - Inherited: kotoba base a5adc146 PROVINCE.md:31 read "- kengaku — LLM/model evaluation and route telemetry." The rewrite kept the phrase.
   - Guard does not catch it: mutation M4 (row text changed to "... and prompt-craft ownership") exits 0.
   - Fix: delete "and route telemetry", or write "route telemetry ABSENT since 2026-10-15 (kengaku SKILL.md:3)".

2. MAJOR — the row's "not contested" rationale is contradicted by committed sibling bytes.
   - CensusKengaku.md Finding 5 says "no craft artifact authoring or auditing" and that the only prompt/skill-instrument path is probeC_prompt_check.py. Its sweep was path-name only (`git ls-tree -r --name-only … | grep -icE '(prompt|skill).*(verify|check|audit)'`). A path sweep cannot see content.
   - `.ufo/waves/round-25/build/FrontmatterScout.md:14-17` audits 19 lanes' SKILL.md frontmatter ("Census (observed, 19 lanes)"; "kengaku 0/3, 0 quoted"). Line 59 gives a conformance verdict that names kotoba ("kotoba and souji conform"). That is an audit of other lanes' SKILL.md, including kotoba's.
   - `plans/round25_census.sh:112-115` reads `SKILL.md` in the cwd and counts quoted triggers (`skill_frontmatter_triggers`). `.ufo/waves/round-25/build/CensusScriptExec.md:48` predicts running it in `<lane>` for chousa, mori, kotoba, lore and tameshi.
   - Scope surfaces call that tool kengaku's own: `plans/round25_census.sh:2` ("kengaku round-25 census — run from the lane root"), `SCORECARD.md:658`, `corpus/README.md:192`.
   - Consequence: "adjacent" holds if only scope-surface claims count, which is how the rule is worded ("committed scope surfaces claim"). If activity over other lanes' SKILL.md counts ("auditing other lanes' SKILL.md … or the instruments over them"), kengaku is `contested`. The census does not state which reading it uses. Fix: name these artifacts in the row's rationale and state the reading.

3. MODERATE — the arbitration convention is inconsistent with the guard's sibling set.
   - Census cell: `yes: chousa, kama, kotoba, kumitate, tameshi` (kotoba included; the kotodama row does the same).
   - Guard `verifiers/check_sibling_census.py:254`: "The sibling-lane set: `*-shokunin` dirs under fleet_root, minus kotoba."
   - Census rule (lines 50-52) does not say whether kotoba counts as a sibling name. Under the guard's set, the cell would be `yes: chousa, kama, kumitate, tameshi`. Pick one convention and write it down.

4. MODERATE — the two mechanical cells are not guarded.
   - Census Limits says "the two mechanical columns are not [judgment]", implying they are checked. The guard only checks non-empty cells, classification membership, commit format and the quote location.
   - M1 (kengaku "names kotoba" yes→no and arbitration→no): exit 0, "rows 20 verified 20".
   - M3 (classification `contested` in both census and PROVINCE): exit 0. The classification rule is not encoded (expected for a judgment, but the census says the guard verifies rows).
   - M5 (last word of quote cut, "verdicts"→"verdict"): exit 0, because the quote check is a substring match.

5. MODERATE — the sibling's own committed label "Contested" is not recorded.
   - `corpus/evidence/round9-fleet/sibling-overlap.md:12` (lane-map row kotoba, cell 4): "**Contested** — prompt format is a treatment in kengaku experiments, while prompt construction is kotoba's province."
   - Ruling (a) at `:21` resolves it to a split ("Kotoba owns the reusable craft/render/trigger implications").
   - The build cites `:53` ("High") and never mentions `:12`. Record the label and say why the content rule still gives `adjacent`.

6. MINOR — PROVINCE.md:28-33 says the guard "checks that these rows match the census". It checks lane set, classification and commit only (M4 exit 0).

7. MINOR — word count. The build's "29 words" for the round-9 supporting quote counts the bullet label. The quoted sentence is 24 words. Command: `python3 -c` whitespace split → 24 for the quoted sentence, 29 with "High — prompt-craft vs eval boundary:".

8. Sibling-side, for the integrator (not kotoba's to fix): kengaku PROVINCE.md:3 (Domain, "route telemetry") contradicts PROVINCE.md:15 (ABSENT). The kotoba note inherited the first.

## What holds (re-derived)

- Commit exists: `git -C kengaku-shokunin cat-file -t 1f3b0f1e…` → `commit`, exit 0.
- Branch cell "master": `git rev-parse master` → 1f3b0f1e…, exit 0. `git symbolic-ref -q HEAD` → exit 1 (detached). `git branch -a --contains 1f3b0f1e…` → `master`, `remotes/origin/master`, exit 0.
- Pinned SKILL.md: 60414 bytes, sha256 08527e28401f9d5e…, 703 lines (`git show … | wc -l`). Line 3 is 901 bytes (902 with newline, matching the build).
- Scope quote: the census quote is a substring of line 3 at index 14 (Python `in`, exit 0; em dashes compared). It occurs only on line 3, inside the ±2 window. The census quote cell equals the pinned text exactly.
- Mechanical columns (Python on `git show 1f3b0f1e…:SKILL.md`; the description has 0 inner `"` and 0 `\`; whole-token, case-insensitive, hyphen-aware, over the 21 lane names): hits chousa, kama, kengaku (self), kotoba, kumitate, tameshi. "names kotoba" = yes. Arbitration (self excluded) = chousa, kama, kotoba, kumitate, tameshi. Both match the census cells.
- Classification `adjacent` (split stated on both sides): SKILL.md:3 "Sibling arbitration: kotoba owns prompt and skill craft (kengaku keeps only measured capability effects)". PROVINCE.md:138 quote matches (`grep -c` → 1). PROVINCE.md:30-32 routes out. Further split statements: `corpus/knowledge/webarena-task-spec-audit.md:164-165` ("prompt-writing advice stays kotoba"), `corpus/lessons/round-27.md:81` ("format craft to kotoba"), `corpus/lessons/round-28.md:82-83`. Kotoba's own description names kengaku (`SKILL.md:11` at c48793db, `sed -n 1,16p | grep -c -i kengaku` → 1).
- No `verifiers/`, `skills/`, `agents/` directory at the pin (archive listing; the `ls -d` returned exit 2).
- Build's cross-tree claim: `corpus/knowledge/skill-activation-telemetry.md` and `render-mechanism-round7.md` are absent at the pin (`git cat-file -e` → rc 128) and present at kotoba a5adc146 (rc 0). The overlap map cites them at `:12` without a prefix. Confirmed.
- Build's base claim: `git show a5adc146:PROVINCE.md | sed -n 31p` → "- kengaku — LLM/model evaluation and route telemetry." Confirmed.
- Guard: `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` in the private clone → "rows 20 verified 20", "province rows 20 matched 20", exit 0. Census and PROVINCE.md in the clone are byte-identical to the lane (`cmp` exit 0 for both).

## PROVINCE.md:46 — statement by statement

| Statement | Pinned source | Verdict |
|---|---|---|
| Lane kengaku, `adjacent`, commit 1f3b0f1e… | census row; guard province check (exit 0) | holds |
| "LLM and model evaluation" | SKILL.md:3 "LLM/model research & evaluation" | holds (paraphrase) |
| "route telemetry" as current scope | SKILL.md:3 "historical, absent since 2026-10-15"; PROVINCE.md:8 and :15 ABSENT | FAILS |
| "kengaku keeps measured capability effects of prompt format" | SKILL.md:3 "keeps only measured capability effects"; PROVINCE.md:30-32 | holds (drops "only") |
| "kotoba owns the craft rules" | SKILL.md:3 "kotoba owns prompt and skill craft"; PROVINCE.md:138 | holds |
| "(kengaku description, `SKILL.md:3`)" | line 3 is the description at the pin | holds |

## Mutation runs (scratch copies; guard exit codes)

- M0 control (unchanged): exit 0.
- M1 mechanical cells of kengaku changed to "no": exit 0.
- M2 census class `none`, PROVINCE `adjacent`: exit 1, "FAIL province row 10 (line 20): lane kengaku classification 'adjacent' does not match the census 'none'".
- M3 `contested` in both files: exit 0.
- M4 PROVINCE row text changed to a false claim: exit 0.
- M5 quote last word cut: exit 0.
- M6 "blind shim-cascade" → "blind shim cascade": exit 1, "quote not found at SKILL.md:3 (+/-2 lines)".
- M7 em dash → hyphen in the quote: exit 1, same message.

## Tooling, bounds, disclosures

- Installs or upgrades: none. No web fetches. Python 3 (system) and git only.
- Lane: no writes. One `git -C <lane> rev-parse --short …` with three revs failed ("Needed a single revision", no output). One `git status --porcelain --ignore-working-copy` in the lane was run by mistake (`--ignore-working-copy` is a jj flag, not git's); git exits 129 at option parsing ("unknown option"), verified with the same command in the scratch clone (exit 129), so no status scan ran. Other lane reads were `cmp`/`grep` on files.
- Sibling repo: `cat-file`, `rev-parse`, `symbolic-ref`, `branch --contains`, `log`, `show`, `ls-tree`, `grep` (via `git archive` into scratch). One `git status --porcelain | wc -l` → 0, exit 0, in kengaku-shokunin is not on the allowed list; it is read-only in intent but may refresh that repo's index stat cache. Disclosed.
- Scratch only: /fast/scratch/hyaku/kotoba-r49/falsify/RowKengaku/ (kotoba-shokunin clone at c48793db; kengaku-pin extraction; guard-mut/ mutation copies).
- Only file written in the lane: this report.

## Residual risk and gaps

- The classification verdict depends on the scope-surface reading of the rule. I did not find a fuller rule source.
- I read the guard in part (lines 1-130, 253-254, 325-460, 478-527). The mutation runs cover the paths that matter for this row. I did not run the guard's own selftest.
- I read three round-25 wave reports (FrontmatterScout, CensusScriptExec, RevFrontmatter) and the round-9 overlap map. I did not read every round-25 or round-29 wave report.
- Pins are as of 2026-10-22. Sibling tip movement after this is not covered.
