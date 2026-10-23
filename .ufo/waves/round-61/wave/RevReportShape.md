# RevReportShape — round-61 report audit checklist (pre-flight, L1 applies before fleet-commit)

Seat `kotoba-r61-wave-RevReportShape` (reviewer, leaf). Scope: the tick-list the L1 runs on
the drafted `.ufo/reports/round-61/kotoba.md` **after the final lane push, before**
`scripts/hyaku/fleet-commit.sh`. Ground: r60 closure `corpus/lessons/round-60-verifier-spotcheck.md`
§1 (conformance table) + §7 (defect classes), the r61 driver `.ufo/prompts/kotoba-round-61.md`,
`plans/round-61.md` including erratum E1, and the committed wave evidence.

A tick that fails means the report text (or the missing receipt/commit) is fixed first —
this checklist audits the report's conformance and wording; it does not re-measure C1/C2.

Notation: `<tip>` = the pushed lane branch tip the report cites; `<lane>` =
`/home/vgpnk/Projects/shokunin/kotoba-shokunin`; `<fleet>` = `/home/vgpnk/Projects/shokunin`.
Base = `f3246d1493b60ea1c0d947a19c39f9e08e92f326`. Freeze commit (plan+checker+C2 base control+
census-before+wave spec/dispatch) = `7827628a939b0333c89892dfcedc72e390ccfb60`. Erratum E1 =
`c630c4cbc01ff5e5438ab0033cfadd6e19382ab1`.

## Facts already verified by this seat (inputs to the checklist)

- `git merge-base --is-ancestor f3246d14 master` → exit 0; base..tip currently holds exactly
  `7827628a` (freeze) + `c630c4cb` (E1). `verifiers/check_routed_repairs.py` and
  `plans/round-61.md` are **absent at base** — they land at `7827628a`/`c630c4cb`.
- `.ufo/waves/round-61/controls/C2-base.txt` bytes (verified): per-repair `missing` lines and
  `routed repairs verified 0 of 6`, `base-exit=1`.
- `.ufo/waves/round-61/census-before.txt`: 13 W04 rows, `kotoba ok`, `exit=0` (committed).
- `wave-spec.json`: 68 items; role counts — executor 8, scribe 12, scout 6, connector 1,
  mutation-tester 11, reviewer 16, critic 9, sentinel 3, revenger 1, simplifier 1.
  `wave/swarm-registry.json` lists 68 members. Freeze-commit message states "68 seats, 46 attack".
- `diff` r60→r61 driver prompts: only round-number/attempt/lesson-filename substitutions —
  the §1–§5 contract text is byte-identical otherwise.
- Watchdog (`.ufo/watchdog.log:951`): exactly one `launch kotoba round=61 … attempt=1` line,
  no `lane-dead-no-report kotoba round=61` at check time. If one appears before report, the
  inherited-state item below becomes mandatory, not optional.
- E1 (`plans/round-61.md` Erratum E1, `c630c4cb`): **C3 is withdrawn as a counted claim before
  data** (CriticC3Axis hollow counterexample — a presence counter cannot back an adjacency
  claim, mined as M92). Round claims are now **C1 (depth) + C2 (calibration)**; S117 curation
  continues as frontier-step work reported under Sources & frontier.

## A. Required report sections (driver §4, verbatim order)

- [ ] A1 `## Work performed` — **opens by naming the declared claims and their axes:
  C1 (depth) and C2 (calibration) only.** Any line naming C3 as a claim = fail (E1). Then one
  bullet per work item, each carrying an evidence pointer (path:line, command output, or hash).
- [ ] A2 `## Landed changes` — every change tied to a LOG.md entry and the commit hash carrying it.
- [ ] A3 `## Before → after measurements` — one per claim (C1, C2), each with the counting
  command, the measured commit, pasted output, `date -u`, exit code.
- [ ] A4 `## Sources & frontier` — rows before→after with counting command, rows added by tier,
  rows touched old→new, frontier rows advanced; census before+after pasted with exit codes.
  Must **not** use `SOURCES: unchanged —` (that line is main-repo lanes only).
- [ ] A5 `## Trend verdicts` — one verdict each for expansion, quality, discernment ∈
  {improved, harmed, unchanged, unprovable-but-better}, each with evidence; no scalar.
- [ ] A6 `## SHONEN` — one line per SHONEN.md box (lane file has 4 boxes, all `[~]`); each `[~]`
  carries a resolvable pointer; **no `[x]`** (promotion is operator-owned; a `[x]` without a
  named non-author verifier = fail).
- [ ] A7 Marker rule — no placeholder text; every required heading present (missing `Sources &
  frontier` or `Trend verdicts` = conformance defect to log, not a pass).
- [ ] A8 Extras (driver §6.6 + §6.1): `Stale-lane` line; tool installs line ("none" allowed);
  open-L0-questions line (`kotoba | round-55 |` carried, any new ones named); closure-duty line
  ("driver completion is not admission"); **Round shape, seats, dead seats** section; planner-seat
  mapping line (the L1 holds the canonical §3 planner seat); report timestamp taken before the
  fleet commit and **Lane HEAD line citing the pushed tip hash** (M87).

## B. r60-closure §1 conformance, adapted to r61

- [ ] B1 Report committed by lane identity —
  `git -C <fleet> log -1 --format='%an %ae %H' -- .ufo/reports/round-61/kotoba.md` →
  author/committer `kotoba-shokunin <kotoba@shokunin.local>`; the commit is on the pushed
  fleet branch (`git -C <fleet> merge-base --is-ancestor <h> origin/master` after fetch).
  The report commit's name-status lists **exactly** `.ufo/reports/round-61/kotoba.md`
  (`git -C <fleet> show --name-only --format= <h>`); l0-questions appends ride their own commit.
- [ ] B2 SHONEN form — report §SHONEN: 4 `[~]` lines, each pointer resolves at `<tip>`
  (`git show <tip>:<path>` then check the cited line range). No `[x]`.
- [ ] B3 Cited commits exist + are ancestors — for **every** hash cited in the report
  (expected minimum set: base `f3246d14`, freeze `7827628a`, E1 `c630c4cb`, each integration
  commit, the C1 data commit, the measured `<tip>`):
  `git -C <lane> cat-file -e <h>^{commit}` and
  `git -C <lane> merge-base --is-ancestor <h> master` both exit 0. Read the tip as
  `git rev-parse master` or `jj-lane.sh state`'s `local=` — **never `@{u}`/`HEAD`** (git HEAD
  is detached under jj). Only `landed <hash>` lines may be cited; a `rewritten` hash = fail.
- [ ] B4 Lane clean + pushed at report time —
  `bash <fleet>/scripts/hyaku/jj-lane.sh state <lane>` → `ahead=0 behind=0 tracked=0
  untracked=0`, and `git -C <lane> status --porcelain` empty; `local=` equals `remote=` equals
  the `<tip>` the report cites.
- [ ] B5 Prompt carries template contract — `.ufo/prompts/kotoba-round-61.md` still holds all
  5 child-lane items (report path `…/round-61/kotoba.md`, commit-before-report, SHONEN
  heading rule, hash-citation rule, write scope) + round-level items (mission/axes binding,
  L2 minimum, commit-then-push, push scope, L0 side channel) verbatim. Cheap re-verify:
  `diff .ufo/prompts/kotoba-round-60.md .ufo/prompts/kotoba-round-61.md` shows only the
  round-60→61 / attempt-2→1 / `round-59-verifier-spotcheck`→`round-60-verifier-spotcheck`
  substitutions (already confirmed identical otherwise at check time).
- [ ] B6 Dispatch digest — `grep 'kotoba.*round=61' .ufo/watchdog.log`: one `launch` line
  (`attempt=1`). If a `lane-dead-no-report` line exists by report time, the report MUST carry
  the inherited-state clause naming reused vs discarded `.ufo/waves/round-61/` leftovers;
  otherwise the report's "attempt 1, no inherited state" phrasing must match a clean log.

## C. r60-closure §7 defect classes, reworded as pre-flight checks

- [ ] C1 Scope disclosure — build the actual round scope:
  `git -C <lane> diff --name-only f3246d1493b60ea1c0d947a19c39f9e08e92f326 <tip>`.
  Every path in that list is named in `Landed changes`/`Work performed`. Expected members that
  must not be silently omitted (the r60 miss was `plans/` + `considerthese/`):
  `plans/round-61.md`, `verifiers/check_routed_repairs.py`, `verifiers/check_scoped_rules.py`
  (v3), every `.ufo/waves/round-61/*` (census-before, census-after, controls/, receipts/,
  wave spec+dispatch+registry, seat reports, fixtures), `corpus/SOURCES.md`,
  `corpus/README.md`, `corpus/QUALITY.md` (Q56), `corpus/lessons/round-61.md`,
  `corpus/knowledge/writing-revision-calibration-round61.md` (frontier work, not a claim),
  `LOG.md`, `SCORECARD.md`, `SHONEN.md`, `PROVINCE.md` if touched, and any `considerthese/*`
  or sibling-list file changed in range.
- [ ] C2 Evidence pointer precision — for every measurement pointer in `Before → after`,
  `git show <tip>:<cited-path> | grep -F '<exact output line>'` hits. Base and after receipts
  are cited **separately, by the file that actually holds each run** (the r60 defect was a
  joint citation implying one file held both). Required pair shapes:
  C1-after names the committed `--fetch` receipt at the data rev (`… 4 of 4 … exit 0`-line
  per the integrated counter's print contract); C1-base names the committed receipt holding
  the base `--rev f3246d14 --fetch` exit 1 (a receipts/ or controls/ file, NOT the after file);
  C1-self-test names the receipt holding `worlds reject 7 of 7; eligible rows pass 4 of 4`
  exit 0; C2-after names the tip `routed repairs verified 6 of 6` receipt; C2-base names
  `.ufo/waves/round-61/controls/C2-base.txt` (bytes already verified: `0 of 6`, `base-exit=1`).
- [ ] C3 Seat-report count honesty — count committed reports at `<tip>`:
  `git -C <lane> ls-tree -r --name-only <tip> .ufo/waves/round-61/wave/ | grep -c '\.md$'`
  (exclude `swarm-registry.json`; add `.ufo/waves/round-61/residual/*.md` if a residual call
  ran). The report's "N reports" claim must equal this number, and "0 dead" may only be
  written when N equals dispatched seats (68 wave members + residual seats). Every spec
  member lacking a committed `.md` is named dead **with its last error text**; cancelled
  seats name the cancellation; no seat was replaced. Reported refusals (job-cap "Background
  job limit reached") carry their error text.
- [ ] C4 Census-after file — `git show <tip>:.ufo/waves/round-61/census-after.txt` exists and
  its last non-empty line is `exit=0` (this is also counter conjunct R-d). The report pastes
  before (`census-before.txt`: 13 W04, `kotoba ok`, `exit=0`) and after outputs with exit codes.
- [ ] C5 "Byte-exact" wording reservation — `grep -n 'byte-exact\|byte-identical' <report>`:
  every hit is either (a) literal equality verified by `cmp`/sha256 with the command named, or
  (b) quoting the frozen A3 arm spec (`URL byte-identical to its base row`). Any shaped quote
  (escape like `&#124;`, whitespace normalization, truncation) is worded as shaped/normalized —
  never "byte-exact". This pairs with landed R-e: `corpus/QUALITY.md` Q56 reserving the word +
  `corpus/lessons/round-61.md` mining M91.

## D. Round-61-specific checks (plan + E1 + frozen predicates)

- [ ] D1 E1 conformance — claims named are C1+C2 only; C3 withdrawn-before-data is stated with
  the `c630c4cb` pointer; S117 row + `writing-revision-calibration-round61.md` + README index
  row + lesson Gate appear under Sources & frontier as frontier work; M92 is in
  `corpus/lessons/round-61.md ## Mistakes`; no C3 verdict/count is reported as a claim.
  Tier honesty: any reliance on the kama file is labeled tier-B, scope
  "writing-revision calibration for prompt-craft self-assessment", kind own-work, and never
  sole support for a claim.
- [ ] D2 C1 predicate sentence identity — the sentence in the report/LOG equals the frozen one
  (`plans/round-61.md` §C1): `--self-test` prints `worlds reject 7 of 7; eligible rows pass
  4 of 4` exit 0; `--rev <tip> --fetch` exit 0; same command at `f3246d14` exit 1 — same words
  in plan, counter label, receipt (kumitate-r42 rule; any post-data rule text change = fail).
- [ ] D3 C1 kill rule stated honestly — the report names each of the 7 worlds' outcome and the
  4 eligible rows' outcome; if any world exited 0, any eligible row failed, or base did not
  exit 1, the report says C1 failed — not prettified.
- [ ] D4 Counter freeze + sha — report cites the frozen v3 counter sha256 and the commit that
  froze it; `git -C <lane> diff <freeze-commit> <tip> -- verifiers/check_scoped_rules.py`
  is empty after integration; the counter file committed at tip equals the sha cited.
- [ ] D5 M90 control chronology — `.ufo/waves/round-61/receipts/controls-ancestry.txt` exists at
  tip containing `merge-base --is-ancestor` and `exit 0` (counter conjunct R-f); semantically it
  must show the control-receipts commit (C2-base `7827628a` and the C1 fixture/self-test receipts
  commit) **precedes the C1 data commit** — verify the two hashes it names and their order, not
  just the file's existence.
- [ ] D6 C2 repair substance — counter counts bytes; the report shouldn't over-claim. Spot-check
  LOG.md at tip carries the three one-line repairs the report names: R-a line containing
  `build reports` + `claimed 32` + `committed 29` + `.ufo/waves/round-60/build`; R-b naming both
  `plans/round-60.md` and `considerthese/2026-10-23.md`; R-c line with both
  `receipts/freeze2-selftest.txt` and `C1-measure.txt`. Q56 + `byte-exact` in
  `corpus/QUALITY.md`; M91 + M92 in `corpus/lessons/round-61.md`.
- [ ] D7 Sourced-claim rule — C1 rests on S112–S115 (opened this round): the report names them
  and the lesson `## Gate` records URL, access date, ≤25-word located quote for each new row.
- [ ] D8 Do-nothing controls — C2 do-nothing = base run, receipt `controls/C2-base.txt` (0 of 6,
  exit 1). C1 W0 do-nothing world is counted as an extra arm, not inside the frozen `7 of 7`.

## E. Wave-shape honesty (driver §6.2 + plan wave shape)

- [ ] E1 Shape named — "one v2 wave" (`kotoba-r61-wave`, policy v2, band 64–128; plan says
  64–96 — 68 satisfies both); round total = 68 wave seats + residual seats ≤ 8, and ≤ 128.
- [ ] E2 Role mix + attack share — report's per-role counts equal `wave-spec.json`'s (executor 8,
  scribe 12, scout 6, connector 1, mutation-tester 11, reviewer 16, critic 9, sentinel 3,
  revenger 1, simplifier 1); the ≥25%-attack sentence names which roles it counts and shows the
  arithmetic (core-attack reading reviewer+critic+mutation-tester+labrat = 36/68 ≈ 53%; the
  freeze commit's "46 attack" additionally counts scout+sentinel+revenger — either counting set
  passes, but the report must not silently mix them).
- [ ] E3 Residual call — if dispatched, named as one ordinary `task` call of ≤8 reviewer/critic
  seats, its reports committed under `.ufo/waves/round-61/residual/`, counted in the total.
- [ ] E4 L2 floor — minimum role split is met inside the wave (≥3 executor, ≥1 scribe, ≥1 scout,
  ≥1 reviewer, ≥1 critic, 1 connector; planner = L1 canonical, mapping recorded in report).
- [ ] E5 Honesty of seat outcomes — every wave report file carries its installs/blockers/
  attacked-produced trailer lines per the wave context; sample-check that attack-seat reports
  name what they attacked.

## F. Commit/push/misroot hygiene

- [ ] F1 Misroot sweep before report — `git -C <fleet> status --porcelain` shows no
  `.ufo/waves/round-61/*` or seat note at fleet root authored by kotoba seats; any found were
  copied byte-exact into the lane (`cmp` receipt) and deleted, recorded under `## Mistakes`
  (M79 class). The report records the sweep outcome.
- [ ] F2 Report cites the pushed lane tip — the `landed <hash>` it names equals `remote=` from
  `jj-lane.sh state`; report written-timestamp precedes the fleet commit (M87).
- [ ] F3 No out-of-scope lane writes — `git -C <lane> diff --name-only f3246d14 <tip>` contains
  no `.ufo/state/`, no fleet paths, no sibling paths, no MANIFEST.json.
- [ ] F4 Watchdog/marker sanity — report contains real committed work (marker rule); Sources &
  frontier + Trend verdicts present even if thin (conformance, not marker).

## G. Honesty floor (driver §6.8 + plan honesty rule)

- [ ] G1 Every pass/predicate word in the report is backed by a pasted run or a committed
  receipt the reader can re-derive with one command over committed bytes; nothing described as
  verified is unrun.
- [ ] G2 No exploratory claim is declared (both claims measured; E1 retired the third).
- [ ] G3 Verdicts reported as measured — if any kill-rule clause fired, the report says failed;
  harmed/unprovable outcomes are named, not omitted.
- [ ] G4 Measurements carry command + pasted output + `date -u` + measured commit + exit code.

Installs: none (read-only audit work; pacman untouched, host-wide pause respected).
Blockers: none.
Produced: the pre-fleet-commit audit tick-list above — sections A–G, adapted from r60 closure
§1 + §7 to round 61 including the E1 C3-withdrawal and the frozen C1/C2 predicates.
