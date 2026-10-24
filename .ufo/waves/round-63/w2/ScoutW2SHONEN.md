# ScoutW2SHONEN — SHONEN four-box audit at cbbee56e

- role: scout
- item: ScoutW2SHONEN
- judged on: calibration
- rev: `cbbee56e9a3589b0b46736ad36f1b77701def80e` (`git rev-parse HEAD` equals that object; `git status --porcelain -- SHONEN.md` empty)
- axes: pointer resolution; live-claim drift; grade honesty (`[x]` only from a named non-author; this seat cannot mint one); `[~]` re-assertable this round
- tools installed: none

`SHONEN.md` at this rev is four `[~]` boxes, zero `[x]`. All four evidence paths are in the tree. Two live claims inside those evidence lines are false at this rev (box 1's present-tense source count; box 4's `PROVINCE.md:33` anchor). Boxes 2 and 3 re-assert `[~]` with no text change.

## Attack

Pinned reads are `git show cbbee56e9a3589b0b46736ad36f1b77701def80e:<path>`. Working tree was not the source of the verdicts.

```
$ git ls-tree -r --name-only cbbee56e -- \
    .ufo/round-46/scouts/B2.md \
    corpus/knowledge/anatomy-and-compression.md \
    corpus/knowledge/cold-run-round11.md \
    corpus/lessons/round-8-aggregator-box3-coldrun.md \
    PROVINCE.md \
    .ufo/round-46/scouts/w2-connector.md \
    corpus/knowledge/sibling-overlap-census-round49.md
.ufo/round-46/scouts/B2.md
.ufo/round-46/scouts/w2-connector.md
PROVINCE.md
corpus/knowledge/anatomy-and-compression.md
corpus/knowledge/cold-run-round11.md
corpus/knowledge/sibling-overlap-census-round49.md
corpus/lessons/round-8-aggregator-box3-coldrun.md
```

Box 1 — the awk cited in `SHONEN.md:6`, plus the checklist markers:

```
$ git show cbbee56e:SKILL.md | awk '/^## Sources/{p=1;next} /^## /{p=0} p && /^- /' | wc -l
18

$ git show cbbee56e:SKILL.md | awk '
  /^## / {sec=$0}
  /^- \[[ xX]\]/ {c[sec]++}
  END {for (s in c) print c[s], s}'
15 ## Trigger-fidelity checklist
9 ## Agent-definition fidelity checklist
9 ## Dispatch-prompt fidelity checklist
8 ## Always-on constraint-file checklist (AGENTS.md-class)
```

Same awk at older commits: `07c33d73` → 33 (round-57 recount, true then); `c63ccc68` → 20 (round 59 already recorded that `SHONEN.md:6` still said 33; `.ufo/waves/round-59/falsify/ReviewBudgetMove.md:74`); `35d44b4b` and `8c4cefa8` → 18. Round 63's `SKILL.md` diff is two gate-registry rows inserted at line 491, after `SKILL.md:241`, so it did not move the decision-table pointer and did not change the source count.

`SKILL.md:241` still points at `corpus/knowledge/anatomy-and-compression.md` § Decision tables. Data rows are `:104-108` (5); the table block including the header is `:102-108`. Anatomy's 7 data rows (numbered 0–6) are `:130-136`, pointed from `SKILL.md:58` (moved round 58; the SHONEN evidence line never says so). Anti-patterns: `SKILL.md:435` → `corpus/knowledge/fail-closed-and-anti-patterns.md` § Anti-pattern table (full) at `:58`; that table's data rows are `:67-86` (20). `B2.md:44` still says the round-46 inventory was 41 boxes (15/9/9/8), seven anatomy rows, five decision rows, 38 Sources entries.

Box 2 — `cold-run-round11.md:72` is `exit=1` (6/9, DRIFT). `:376` is `9/9 checks pass` after the round-12 repair recorded in §7. `LOG.md:287-288` names that file under the round-11 entry. The file's own header says "NON-AUTHOR"; `SHONEN.md:8` already classifies the runner as lane-dispatched. No new drift.

Box 3 — `round-8-aggregator-box3-coldrun.md:41` is the `[~]` verdict on B1+B2. `LOG.md:398` is the round-13 heading; `:423-426` records the B1 catalogue-bearing rule and the B2 mutating label. Live: B1 is `SKILL.md:162-166` (`catalogue-bearing`, `omp.catalogue_path`). B2 is `verifiers/README.md:44` (`**Mutating — not a smoke check**`). `git ls-tree -r --name-only cbbee56e` names only two cold-run files: `corpus/knowledge/cold-run-round11.md` and `corpus/lessons/round-8-aggregator-box3-coldrun.md`. No later box-3 cold run is in the tree. Spot-checks through round 53 still say box 3 rests on the round-8 run (`corpus/lessons/round-53-verifier-spotcheck.md:220`).

Box 4 — `## Adjacent` line by commit:

```
07c33d73  adjacent_line=31  line33=Sibling-owned ground (report, don't absorb). Rewritten round 49 …
c63ccc68  adjacent_line=33  line33=## Adjacent
35d44b4b  adjacent_line=34  line33=<blank>
8c4cefa8  adjacent_line=34  line33=<blank>
cbbee56e  adjacent_line=35  line33=- Loader-rule freshness: the omp 18.12.3 substrate drift …
```

`79cf263` (round-60 close, the same commit that repointed `SKILL.md:241`) inserted one Core bullet and moved `## Adjacent` off line 33. `cbbee56e` inserted the round-63 Core bullet (`PROVINCE.md` +1 vs parent) and moved the heading to `:35`. At this rev `:33` is a Frontier bullet, not § Adjacent. The rewrite sentence is `:37`. Both cited files still exist: `.ufo/round-46/scouts/w2-connector.md`, `corpus/knowledge/sibling-overlap-census-round49.md`.

```
$ python3 -B verifiers/check_sibling_census.py \
    corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md
rows 20 verified 20
province rows 20 matched 20
EXIT:0
```

The guard checks lane set, classification and commit against the census. It does not check boundary prose (`PROVINCE.md:41`).

## Verdict on the committed bytes

| box | mark now | pointer resolves? | `[~]` this round? | drift |
|---|---|---|---|---|
| 1 decision tables / error patterns / checklists / sources | `[~]` | `B2.md` yes; `SKILL.md:241` yes; `:102-108` yes | yes, as lane-run | **yes** — `SHONEN.md:6` says § Sources **holds 33**; the cited awk prints **18**. Anatomy's round-58 move is unstated (historical B2 parenthetical is still true of `B2.md:44`) |
| 2 end-to-end task logged | `[~]` | `cold-run-round11.md` yes; LOG yes | yes | no |
| 3 executable without oral context | `[~]` | round-8 lesson `:41` yes; fixes still present | yes | no (B2's label now lives in `verifiers/README.md:44`, which the evidence line does not cite; the "fixed in round 13" claim is still true) |
| 4 no cross-domain bleed | `[~]` | section yes at `:35`; **`:33` does not name it** | yes, census guard exit 0 | **yes** — `PROVINCE.md:33` |

No box is `[x]`. No named non-author verifier graded these four boxes at this rev. This seat is lane-dispatched.

## Four lines the L1 can file

```
- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `.ufo/round-46/scouts/B2.md:44` (lane-run). Live at `cbbee56e`: checklists 15/9/9/8; anatomy 7 rows `corpus/knowledge/anatomy-and-compression.md:130-136` (`SKILL.md:58`); decision rows `:104-108` (`SKILL.md:241`); anti-patterns `SKILL.md:435`; Sources awk **18**, not the 33 in `SHONEN.md:6`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `corpus/knowledge/cold-run-round11.md` (red `exit=1` at `:72`; `9/9 checks pass` at `:376`) and `LOG.md:287-288`. Lane-dispatched `ColdRunRecord`.
- [~] Instructions executable by an agent without oral context — `corpus/lessons/round-8-aggregator-box3-coldrun.md:41`. B1 still `SKILL.md:162-166`; B2 label still `verifiers/README.md:44`. No second cold-run file in the tree.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:35` (§ Adjacent). `PROVINCE.md:33` is the Frontier loader-rule bullet at `cbbee56e`. Census guard: `rows 20 verified 20` / `province rows 20 matched 20`, exit 0.
```

## Smallest safe correction

Do not change any `[~]` mark. Replace only the two drifted evidence sentences.

`SHONEN.md:6` proposed text:

```
  evidence: `.ufo/round-46/scouts/B2.md:44` (round-46 lane-run inventory: 7 anatomy rows, 5 decision rows, 41 checklist boxes 15/9/9/8, 38 Sources entries). Live at `cbbee56e`: checklists still 15/9/9/8; the 7 anatomy rows are `corpus/knowledge/anatomy-and-compression.md:130-136` (pointer `SKILL.md:58`, moved round 58); the 5 decision rows are `:104-108` (table block `:102-108`, pointer `SKILL.md:241`); § Sources top-level entries are 18, not 33 (`awk '/^## Sources/{p=1;next} /^## /{p=0} p && /^- /' SKILL.md | wc -l` → 18; 33 was `07c33d73`, 20 was `c63ccc68`).
```

`SHONEN.md:12` proposed text:

```
  evidence: `PROVINCE.md` § Adjacent (heading `PROVINCE.md:35` at `cbbee56e`; `:33` was that heading at `c63ccc68` and is the Frontier loader-rule bullet after the round-60 and round-63 Core inserts). The round-46 list this section replaced is `.ufo/round-46/scouts/w2-connector.md`; rewritten round 49 from `corpus/knowledge/sibling-overlap-census-round49.md`. `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` → `rows 20 verified 20` / `province rows 20 matched 20`, exit 0.
```

Boxes 2 and 3: no SHONEN text change. Bound: box 3's B2 label is `verifiers/README.md:44`, not a `SKILL.md` line; box 2's green line is the round-12 repair in the same file (`:376`), not the round-11 capture (`:72`).
