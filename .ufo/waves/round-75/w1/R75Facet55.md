# R75Facet55 — facet 55: the round-74 spot-check's D1 (falsify wave / seat accounting) and the dispatch evidence under it

Seat `R75Facet55`, leaf, read-only, no delegation, no spawn. Measured revision
`65a5c7a663249e0522cc49e4a148424200d9ddfe` (`git rev-parse HEAD`); `git status --porcelain` printed only
`?? .ufo/waves/round-75/` (this wave's own directory), so every path below is working-tree = committed bytes at
that revision. No install, no scratch directory, no file written outside this report; commands ran in ephemeral
shells only.

## Facet under audit

| element | location |
|---|---|
| paragraph | `corpus/lessons/round-74-verifier-spotcheck.md:34-37` (D1 — L2 floor and falsify wave) |
| neighbouring claim, checked for contrast | `corpus/lessons/round-74-verifier-spotcheck.md:38-41` (D2 — unlisted commit) |
| plan premise it scores | `plans/round-74.md:13`, `plans/round-74.md:172-174` (§ Seat plan) |
| wave artifacts | `.ufo/waves/round-74/{w1,w2}-spec.json`, `w1.ready.dispatched`, `w2.ready.dispatched`, `w1/swarm-registry.json`, `w2/swarm-registry.json`, `w1/*.md` (34), `w2/*` |
| the lane's own instrument for this count | `verifiers/check_seat_counts.py` (registry row `SKILL.md:479`) |

D1 makes four assertions: (i) `34 seats against the 64-seat floor`; (ii) wave 2, "the falsify wave, 33 seats",
"was never dispatched"; (iii) it is "the third kotoba round in a row without a falsify wave"; (iv) the lane
disclosed it in the report header, the lesson and `SCORECARD.md`.

## Observations (each from committed bytes; command → observed)

| # | what | command | observed |
|---|---|---|---|
| O1 | declared vs completed, wave 1 | `python3 -c` over `w1-spec.json` names vs direct `.md` children of `w1/` | declared 34, reports 34, committed 34, missing 0, unmatched 0 → `34 of 34` |
| O2 | declared vs completed, wave 2 | same, `w2-spec.json` / `w2/` | declared 33, reports 0, committed 0, missing 33 (`ConnCrossW2R74.md`, `ConnSeatAccountW2R74.md`, `CriticC1CounterW2R74.md`, …) → `0 of 33` |
| O3 | spec identity | `json.load(w2-spec.json)['milestone']` | `Round-74 wave 2 (falsify): attack the landed C1 spec-craft entry, rows, SKILL.md text and …`; roles reviewer 13, critic 5, mutation-tester 4, executor 4, scout 3, connector 2, scribe 2 = 33 |
| O4 | the existing instrument | read `verifiers/check_seat_counts.py:12-20,59-91` | universe = `items[].name` → `<name>.md` **directly** under the report dir, `swarm-registry.json` excluded, recursive listing depth-filtered at `:59-71`; both r74 specs carry `name` on every item, so the counter applies unchanged |
| O5 | dispatch markers differ in kind | `cat .ufo/waves/round-74/w1.ready.dispatched`; `cat .ufo/waves/round-74/w2.ready.dispatched` | w1 = a bare timestamp `2026-10-25T22:42:46`; w2 = 185 B prose `2026-10-26T09:04:54 ABANDONED by hyaku run-8 orchestrator cleanup: no seat was spawned (stale: round 74 closed, wave never taken). A retry dispatches these seats under a new wave name.` (sha256 `dd7f094a75f3ac5b11cb172aa5eb15df59fed1a1f9241c58880ce8d5592ff5e7`) |
| O6 | that marker's provenance | `git show --stat 65a5c7a` | one file, `+1`, committer date `2026-10-26 09:05:54 -0300` — 60 s after the timestamp inside the file; written by the *salvage* after the round closed (`2026-10-26T01:03:32-03:00 complete`) and after D1's commit `314e4a1a` (`2026-10-26 01:15:38`) |
| O7 | wave registries are plan manifests, not execution records | `python3 -c` over both `swarm-registry.json` | w1: 34 members, w2: 33 members; **every** member in both has `agentId: null`, no `status`/`state` key, `kind: "spawn"`, and `createdAt == updatedAt` (w1 `2026-10-26T01:31:25.231Z`, w2 `2026-10-26T02:33:36.869Z`). The run wave and the abandoned wave are shape-identical |
| O8 | the persisted before-value of (iii) | `grep -n falsify` in r68–r74 reports/lessons/plans | r68 report `:82` "The wave-2 falsify wave was **not dispatched**" (and `:108` carries it to r69); r70 plan `:8-9` "wave 2 falsify only if wave 1 yields ≥32 distinct attack items", r70 report `:146` "No wave 2"; r71 plan `:8` "default v1, wave 1 only"; r72 lesson `:7`,`:92`; r73 spot-check `:32`,`:34` ("second round running"); r74 lesson `:100`,`:113`; r74 report `:5-7`; `SCORECARD.md:467` |
| O9 | falsify-seat reports committed, r68–r74 | `git ls-tree -r --name-only 65a5c7a -- .ufo/waves/round-$r/w2 .ufo/waves/round-$r/falsify \| grep -c '\.md$'` | `0` for every round 68…74 |
| O10 | plan-side seat arithmetic | `plans/round-74.md:172` vs spec vs report | plan: `35 seats … executors (sources ×3, counters ×2, controls ×2, heads/rows ×4, assimilation ×2, base) 16` — the parenthetical enumerates `3+2+2+4+2+1 = 14`; frozen `w1-spec.json` carries **15** executors; fleet report `:20` records "34 dispatched, 34 settled — executor 15" |
| O11 | disclosure assertion (iv) | `grep -n falsify` in fleet report, lesson, SCORECARD | report `.ufo/reports/round-74/kotoba.md:5-7`; `corpus/lessons/round-74.md:100,113`; `SCORECARD.md:467` — all three present |
| O12 | D2's arithmetic | `git show d5aebcf --name-only \| grep -c .`; `git merge-base --is-ancestor` both ways; `git grep -c d5aebcf 65a5c7a -- .ufo/reports/round-74/kotoba.md LOG.md` | 394 files; `d919179 < d5aebcf < 2c81137` both `ok`; 0 hits in both files — D2 holds |

## Findings

### F1 (scope + falsifiability, main) — "the third kotoba round in a row" is a carried prose counter with no class definition and no command

D1 `:36` and `corpus/lessons/round-74.md:100` both say *third*, and the r73 spot-check `:34` said *second*. The
successor value is the predecessor's value plus one (O8), not a recomputation — the class Q19 binds
("a value copied from an earlier record is struck, never scored against") and the form Q13 binds for lesson prose
("`<number> — <command> <date>`"). Recompute it and the number depends entirely on an unstated class:

| class | members with committed evidence | count |
|---|---|---|
| (A) a falsify wave **declared in a committed plan or spec and not dispatched** | r68 (report:82), r72 (lesson:7), r73 (spot-check:32), r74 (D1) — and r70's *conditional* wave-2 falsify (plan:9, report:146) if a conditional declaration counts | 4, or 5 |
| (B) **no falsify seat reports committed** under `w2/` or `falsify/` | r68, r69, r70, r71, r72, r73, r74 (O9) | 7 |
| (C) rounds since the defect was **routed** (r72's spot-check routed it) | r72, r73, r74 | 3 |

Only class (C) yields 3, and it is "rounds since routing", not "rounds without a falsify wave" — the sentence's
words. Under its own words the r74 round is at least the fourth (r68's report states an undispatched falsify wave
two rounds before r72), and the r73 spot-check's "second" is already short by the same test. Nothing in the round
tests either number, so the streak could not fail: no arm, no receipt, no command.

Concrete check (the one D1 should have carried, and the one a r75 claim can freeze):

```
python3 - <<'PY'
import subprocess
for r in range(68, 75):
    n = subprocess.run(["git","ls-tree","-r","--name-only","<rev>","--",
                        f".ufo/waves/round-{r}/w2", f".ufo/waves/round-{r}/falsify"],
                       capture_output=True, text=True).stdout
    print(r, sum(1 for l in n.splitlines() if l.endswith(".md")))
PY
```

with the class written above it. That prints `0` for all seven rounds (O9) — the sweep that produces the absence,
which Q14 requires and this sentence does not carry.

### F2 (control weakness) — two artifacts in the abandoned wave directory read as dispatch evidence, and no gate reads either

D1 `:35` rests the "never dispatched" verdict on `w2-spec.json` and `w2.ready` — the two artifacts that exist
*because* the wave was prepared. The committed post-state now also holds:

- `w2.ready.dispatched` — a file whose *name* asserts dispatch. Its content contradicts the name (O5), and it was
  written by the salvage commit 8 h after D1 (O6). A presence test (`[ -f w2.ready.dispatched ]`) reads
  "dispatched" for a wave that spawned zero seats; the w1 twin is a bare timestamp, so the marker has no uniform
  shape a parser can key on.
- `w2/swarm-registry.json` — 33 members, the declared seat count, in the same 33 that D1's "33 seats" names
  (O3, O7). A membership count reads 33 *spawned*; the file contains no spawn record at all, because every
  `agentId` is `null` in **both** waves — including the wave that did run 34 seats (O7). The registry cannot
  discriminate, so it must not be cited as evidence in either direction.

The lane's own instrument is not at fault but was not used: `verifiers/check_seat_counts.py` excludes
`swarm-registry.json` by name and counts only `<name>.md` seats (`:18-20`, `:59-91`), i.e. exactly the right
universe. Re-deriving its predicate over the committed tree rather than running it (the gate stays with the
parent): w1 → `seat reports committed 34 of 34; missing 0: none; unmatched 0: none`, exit 0; w2 →
`seat reports committed 0 of 33; missing 33: …; unmatched 0: none`, exit 1. Neither number appears in D1.

Residual gap the existing gate does not close: it has no marker arm and no "expected absent" mode, so on the
honest abandoned wave it exits **1** — the verdict map's `1=failed` (`SKILL.md:479`) would score an honestly
skipped wave as a defect (the Q18 false-red class). A r75 control must declare the expected verdict per wave
(w1: 0; w2: 1 with `missing 33` exactly), never bind the bare exit code.

Concrete control (design, not built here) — a seat-accounting receipt with three arms, one must-fail mutant:

| arm | fixture | required verdict |
|---|---|---|
| a | marker present, content `ABANDONED … no seat was spawned`, 0 seat reports, registry 33 | `spawned 0; declared 33; status abandoned` |
| b | 3 seat reports, **no** marker | `spawned 3` (Q27: a seat write outranks a return/cancellation marker) |
| c | registry with 33 members, 0 reports | `spawned 0` — membership never counts |
| mutant | copy w1's bare-timestamp marker into w2 | verdict unchanged (`spawned 0`) — a counter that changes here is reading the name, not the bytes |

### F3 (Q65 arithmetic) — the plan's seat tally does not close, and the frozen spec did not reproduce it

`plans/round-74.md:172` states 35 wave-1 seats with "executors … 16", but its own parenthetical enumerates 14
(`3+2+2+4+2+1`), the frozen `w1-spec.json` carries 15 executors and 34 items, and the fleet report records 34
dispatched / 34 settled (O10). The totals `16+4+11+2+2 = 35` are internally consistent only because the executor
line is taken on trust; the component sum is two seats short. Q65 requires a promised row add to be checked
arithmetically against the budget before it is promised, and the seat budget is that same kind of promise. The
check is one line and was never run:

```
python3 -c "print(3+2+2+4+2+1)"                                     # 14
python3 -c "import json,collections;print(collections.Counter(i['role'] for i in json.load(open('.ufo/waves/round-74/w1-spec.json'))['items']))"
```

D1's own figure ("34 seats") is correct against both the spec and the fleet report — the defect is upstream, in
the number the plan froze, and it is the reason "34" and "35" can both be read as the round's declared size.

### F4 (Q06, minor) — D1 gives completed only against a floor, never completed/declared

`34 seats against the 64-seat floor` prints the numerator and a policy-derived floor. Q6 asks for
`completed/declared` from the claims file: wave 1 is `34 of 34` (O1) and the round is `34 of 67`
(34 + the 33 declared in `w2-spec.json`). The 64 floor is itself an inference from `waveMinLanes: 32` × two waves
(`scripts/hyaku/ufo-wave-policy.json:89`; plan `:13` "band 32–64 each") — not stated in D1, though it is derivable.
The abandoned wave's own spec carried the seat that would have produced exactly this line: `ConnSeatAccountW2R74`
(prompt: "Seat and receipt accounting for the round, read-only. (1) Wave 1: …/w1-spec.json (34 items) … count
completed/declared (Q06) …"). The accounting D1 lacks was planned, then never spawned.

## What holds (checked, no finding)

- D1's verdict on spawning is true: 0 seat reports under `w2/` (O2), and the round's own report `:5-7` and lesson
  `:113` state the same, undisputed by any committed artifact.
- The disclosure assertion (iv) is verified at three surfaces (O11).
- D2 is verified in all three parts (O12): 394 files, both ancestry legs, 0 hits in report and `LOG.md`.
- The 33-seat composition and the falsify character of wave 2 match `w2-spec.json` (O3).
- `check_seat_counts.py`'s depth filter (`:59-71`) does exclude `w1/build/**`'s 151 sandbox `.md` files — the
  r74 wave shape does not break the instrument, so the counter is usable as-is for O1/O2.

## Risks and blockers

1. **Marker provenance.** `w2.ready.dispatched` is post-hoc salvage paperwork, committed 8 h after the round and
   after D1; any r75 record MUST cite its content and sha256 (`dd7f094a…`), never its existence or name, and never
   as `… @ <round rev>` (Q60: the path does not exist at the round tip).
2. **Timestamp form.** Its content timestamp is local `2026-10-26T09:04:54` with no offset, 60 s before the
   committer date of the commit that ships it — legal under Q55, but only if read with `%ci`, not `%ai`
   (`%ai` = `01:15:38`, which would make it look future-dated).
3. **Expectation, not exit code.** Binding `check_seat_counts.py` to a claim without a per-wave expected verdict
   turns the honest abandoned wave (exit 1) into a claimed defect — the Q18 false-red class, and the reason F2's
   control needs arm (a).
4. **Lesson is append-only.** A correction to D1 must be an appended erratum with its own registered sweep
   (Q29), not a rewrite of `:34-37`.
5. **Concurrency.** `w2/swarm-registry.json` sits in the wave directory and is easy to sweep in as a seat or a
   report; O7 shows it is a plan manifest with `agentId: null` throughout, so it is evidence of nothing spawned.

## Candidate for r75 (bounded, if the lane takes it)

Axis `calibration` (or `consistency`): *wave-seat accounting is computed at the frozen revision, and an
abandoned wave reads abandoned, not failed.* Frozen predicate over committed bytes only:

- w1 at the frozen rev: `seat reports committed 34 of 34; missing 0: none; unmatched 0: none` (exit 0),
  re-derived with `check_seat_counts.py`'s own predicate;
- w2 at the same rev: `0 of 33`, the 33 missing names equal to `w2-spec.json`'s names, exit **expected 1**;
- marker arm (a/c/mutant above) run against committed bytes;
- the streak number printed with the class and the sweep command of F1, so "third" cannot be carried again.

Do-nothing control: at `65a5c7a` no committed artifact prints either count or the class (O1/O2 are my
re-derivation) — target 0 of 3 before the claim lands.
