# ScribeDispositions — round-65 wave-1 recon: wave-2 disposition table skeleton

Seat: `ScribeDispositions` (scribe, axis calibration). Item: w1 spec index 28 —
"Prepare the wave-2 disposition table skeleton: list every attack item in both
prepared specs with columns attack / claimed-finding / disposition — fill what the
L1's receipts already settle and leave orchestrator-dispatched rows open for the
closure."

Status: **skeleton + settlement ledger**. 64 attack items listed (w1 32, w2 32).
Nothing here is a wave-2 verdict: rows marked `O` are the closure's dispatch set.
No counter was re-run beyond the commands pasted in §1 (two v32 runs, one
checklist self-test, three registry row counts, the snapshot byte/quote checks);
no mutation, probe, fetch or gate battery was executed by this seat.

---

## 0. Provenance and measured state

Lane repo `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. All revs below were
resolved read-only (`git cat-file -e`, `git log`, `git merge-base
--is-ancestor`); no jj/git write was issued and the lane index was not touched.

| Rev | Date (-0300) | Subject (truncated) | Role |
|---|---|---|---|
| `c98d137` | 01:55:13 | round-64 verifier spot-check | base (r64 close) |
| `2fdfc1f` | 02:42:52 | round-65: plan freeze + before-controls + S121 snapshot | plan freeze |
| `80bb892` | 03:01:30 | C1 closing package (7 package arms + 4 new judge-lane arms, 223→234) | implementation |
| `5253b28` | 03:03:37 | measurement receipts at 80bb8921 | receipts |
| `0e104f4` | 03:10:39 | frontier step (S121 row + snapshot, g7-span-closure entry, lesson M99–M101, census-after 119 rows) + SCORECARD r65 annotations/Next-66 + SHONEN refresh | the rev my brief calls "tip" |
| `484d325` | 03:15:23 | prepared-but-undispatched L2 waves (w1+w2 specs + dispatch payloads + harness) | wave prep |
| `4a2defd` | 03:15:50 | floors-guard before-control receipt | r65 final lane tip per the integrator spot-check |
| `11385e0` | 03:24:36 | round-65 verifier spot-check (integrator, non-author) | non-author closure evidence |
| `2a8eba5` | 04:26:20 | round-66 verifier spot-check | live HEAD |

- Live `HEAD` = `2a8eba56b3f9321b70c569fa2816d42237ca49a2`; `0e104f49` is an
  ancestor, **10 commits back** (`git rev-list --count 0e104f49..HEAD` → 10).
  The working tree is dirty with round-66 w1 seat reports and a modified
  `.ufo/waves/round-65/w1/swarm-registry.json` (`git status --porcelain`).
- Wave state: `.ufo/waves/round-65/w1/swarm-registry.json` lists **32 `spawn`
  members** (`createdAt 2026-10-24T06:15:11Z`, `updatedAt 07:36:33Z`); my live
  peer roster carries agents with those exact ids. `w1-dispatch.err` and
  `w2-dispatch.err` are 0 bytes; each dispatch payload declares
  `{"spawn":32,"resume":0,"total":32}`. [INFERENCE] w1 is dispatched and in
  flight now; w2 has a rendered payload but no registry/ids, so w2 is still
  undispatched.
- The wave specs + payloads are committed bytes (first added in `484d325`,
  present at `4a2defd`); they are **not** in `0e104f49`'s tree
  (`git ls-tree 0e104f49 .ufo/waves/round-65/` shows only census/controls/
  receipts/snapshots).
- A non-author spot-check of round 65 already exists at HEAD:
  `corpus/lessons/round-65-verifier-spotcheck.md` (committed `11385e0`, lesson
  file re-committed at `2a8eba5`). It recomputed the C1/C2 pins and the three
  line-sha pins from committed bytes but **did not execute the lane's gates**
  (its own words). I cite it only as corroboration, never as execution.

## 1. Commands this seat ran (real output, exit codes)

```
$ git show 0e104f49:verifiers/check_scoped_rules_v32.py | sha256sum
b6cfc7644b609f120f69b638d45d3253f07758f9dfa02e8252e2aeaad2183e8d  -     # = receipt pin
$ rm -rf /tmp/r65tip && mkdir -p /tmp/r65tip && git archive 0e104f49 | tar -x -C /tmp/r65tip
$ cd /tmp/r65tip && TMPDIR=/tmp python3 -B verifiers/check_scoped_rules_v32.py --self-test | grep -E 'worlds reject|survivors closed|self-test:'
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
self-test: 0 failure(s) over 234 assertions
exit=0
$ cd <lane> && TMPDIR=/tmp python3 -B verifiers/check_scoped_rules_v32.py --self-test | tail -2
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 240 assertions
live-tree-exit=0                                            # HEAD is round-66 bytes
$ TMPDIR=/tmp python3 -B verifiers/verify_skill_checklist.py --self-test | tail -1
0 failure(s) over 1862 assertions
exit=0
$ for r in c98d137 0e104f49; do git show $r:corpus/SOURCES.md | grep -cE '^\| S[0-9]+ \|'; done
118
119
$ git show HEAD:corpus/SOURCES.md | grep -cE '^\| S[0-9]+ \|'
120
$ sha256sum .ufo/waves/round-65/snapshots/S121.pdf ; stat -c '%s bytes' …
bad1b681b1d6d6cea09f0c1e4701618b88dc175b713689c2a6ac43aba07418a3  …/S121.pdf
1126684 bytes
# whitespace-normalized substring counts in S121.txt
gate quote occurrences: 1 | words: 16
support quote occurrences: 1 | words: 24
```

Other read-only facts established by direct inspection (commands abbreviated in
place; outputs pasted in the rows/defects):

- `git diff --numstat c98d137..0e104f49` — deletions exist in exactly 5 files
  (registry 59, checklist 7, floors guard 6, SCORECARD 1, SHONEN 1); the other
  changed files are pure additions. See D6.
- Floors registration at `0e104f49`: registry has 15 instruments (14 at base),
  key delta is exactly `scoped_rules_v32`; guard's `EXPECTED_INSTRUMENTS` line
  172 and `INSTRUMENTS` line 231 both carry 234; docstring line 11 names it.
- Receipt rev-header audit: the `receipts/` dir holds 9 `.txt` receipts plus
  `kill_battery.py`; **6 of the 9** name a rev (`@ <40-hex>`), 3 do not (D2).
  Of the 3 controls, all name `@ c98d137`; the two census files name no rev.
- Kill receipt enumeration: 17 kill lanes by name, 2 equivalents, 5 control
  worlds, `RESULT: ALL OK`, `harness_exit=0`.
- Wave-context audit: `grep -c 'Kill only by the PIDs you started'` = 1 in each
  spec context; `All paths absolute under` = 1 in each; each dispatch payload
  carries the Q44 sentence twice.
- `check_scoped_rules_v32.py` at tip imports `subprocess` (l.299) and
  `urllib.parse` (l.302) only; its `git()` (l.479–481) calls
  `subprocess.run([...])` with **no timeout**.

## 2. Legend

`S` — the committed artifact contains the output the claim asserts. **It does not
mean this seat re-executed it.** Pointer given.
`S†` — settled by this seat's own read/spot-check from committed bytes (command in
§1 or the row).
`P` — partially settled: the row says exactly which half is covered and which is
not.
`O` — open: nothing in the round's committed artifacts settles it; needs the
orchestrator-dispatched seat.
`X` — contradicted / defect found by inspection (named as a D-item in §7).
`SELF` — this report.

## 3. Receipt coverage (Q36 / Q11 audit)

| Artifact | Rev named internally? | What it settles |
|---|---|---|
| `controls/C1-before.txt` | yes `@ c98d137` | v32 223, sha `f8f69cad…`, exit 1 world |
| `controls/C2-before.txt` | yes `@ c98d137` | checklist 10/1 exit 1; three failing cells named |
| `controls/FLOORS-before.txt` | yes `@ c98d137` | 14 instruments, no v32 row |
| `receipts/C1-close-measure.txt` | yes `@ 80bb8921` | 234, sha `b6cfc764…`, 7/7 + 4/4 + 6/6, exit 0 |
| `receipts/C1-close-kill.txt` | yes `@ 80bb8921` | 17 kills w/ attribution, M19/M22 green, pkg7 control 230 |
| `receipts/C2-governance-measure.txt` | yes `@ 80bb8921` | 11/11 exit 0, `3 recorded correction(s) excused`, 1862 |
| `receipts/C2-selfreference-redbefore.txt` | **no** | backticked-notice FAIL vs quoted-notice PASS (fixture world) |
| `receipts/M99-fixture-leak.txt` | **no** | erratum leak + subject-line mismatch both FAIL with classes |
| `receipts/FLOORS-after.txt` | **no** | 15 rows PASS incl v32 234; checklist 1852 (see D3) |
| `receipts/FLOORS-noharm.txt` | yes `@ 0e104f49` | 15 rows PASS; checklist 1862; floors_guard 165≥150 |
| `receipts/REGRESSION-probes.txt` | yes `@ 80bb8921` | r64 43, r63 `5 of 5`, corpus_integrity `exit None` |
| `receipts/noharm-tip.txt` | yes `@ 0e104f49` | v32 234, checklist 11/0, r64 43, r63 5/5, gate 42/42 |
| `census-before/after.txt` | **no** (path only) | 16 W04 each + `ok <SOURCES.md>`; no row count, no exit code |

## 4. W1 disposition table (32 items)

| # | seat (axis) | claimed finding | disposition |
|---|---|---|---|
| 0 | ScoutS121Reopen (freshness) | live S121 bytes reproduce snapshot sha `bad1b681…`/1,126,684 B and both quotes; arXiv:1309.4818 is not the mutation paper | `P†` snapshot+size+sha and both quotes reproduce from the committed snapshot (gate 16 words ×1, support 24 words ×1); **no live fetch receipt exists in this round** → live half is `O` (w2[8]). Rejection is recorded (lesson Gate M101, plan, `corpus/README.md:116`) |
| 1 | ScoutReceiptSweep (calibration) | each receipt command reproduces at the tip (234, 11/11, 1862, r64 43, r63 5/5, gate 42/42, census 0) | `P†` I reproduced v32 at the **frozen** tip (`0e104f49` archive): 234, exit 0, sha `b6cfc764…`; checklist self-test 1862 at the live tree. The other five commands rest on L1 receipts only. **Must pin `0e104f49`** — the live tree prints 240 (D1) |
| 2 | ScoutQualityDebt3 (freshness) | the carry-forward debt (SentBounds baseline, helper-invocation receipts, r62-w2 remainder, corpus_integrity re-record) is still open | `P` presence is recorded in the tip's `Next: round 66` block (it names the W8/M7–M22 close plus the survivor debt) and re-carried at HEAD's `Next: round 67`; per-item status unverified. The integrity numbers have **no** receipt: `REGRESSION-probes.txt` prints `corpus_integrity exit None fail None` (D12) |
| 3 | ConnSibling2 (adjacency) | `check_sibling_census.py --province PROVINCE.md` reports `STRICT_HITS` | `O` — no `STRICT_HITS` output exists anywhere under `.ufo/waves/round-65/` or in the closure report; the closure report only asserts the conclusion |
| 4 | ExecKillReverify (depth) | 17 single-string mutants each exit 1 with arm-attributed FAIL; M19/M22 survive; pkg7 control admits SPAN_FIRST/SPAN_LAST/M20 | `S` `receipts/C1-close-kill.txt` — enumerated independently by me: 17 kill lanes by name, 2 equivalents at exit 0, control world 230 assertions, `RESULT: ALL OK`. **Independent rebuild is `O`** (w2[2]; harness rerun w1[29]) |
| 5 | ExecFloorsProbe (operability) | arm deletion → guard FAILs naming `observed<N floor 234`; row deletion → anchor drift; live walk all-PASS; guard self-test 165 | `P†` registration is real: registry row (`floor 234`), both in-file tables (l.172, l.231) and docstring at tip; `FLOORS-noharm @0e104f49` is all-PASS with `floors_guard observed=165 floor=150`. The two **deletion probes** have no receipt → `O` (w2[27]) |
| 6 | ExecGovProbe (calibration) | every fail-closed shape FAILs with its named class; honest world PASSes; `corrections=()` do-nothing fails on the three cells | `P` two shapes receipted: past-horizon + no-live-red-subject (`M99-fixture-leak.txt`), self-referential notice (`C2-selfreference-redbefore.txt`). Line-drift, wording, corrected-dead, stale-restored, never-masks and the tip-level `corrections=()` run have no receipt → `O` (w2[6]) |
| 7 | ScribeEntryCheck (depth) | entry commands exist in receipts with matching output; measured-record block matches; provenance trio; S121 anchors match the row | `P†` measured-record block matches `C1-close-measure.txt` (7/7, 4/4, 6/6, three must-fails, 234); `source:`/`verified-at:`/`recheck:` all present; anchor cells (16/24 words, sha, bytes) match the row. Not exhaustive: every narrative command in the entry was not mapped to a receipt line |
| 8 | ScribeLessonCheck (calibration) | Gate carries URL/date/bytes/sha/≤25-word quote; M-rows carry class/evidence/captured-by/fix; both red-before receipts exist and show their claim; S121 `mined` named | `S†` all present at tip; quotes are 16 and 24 words (my count); `M99-fixture-leak.txt` shows two FAIL classes, `C2-selfreference-redbefore.txt` shows FAIL vs PASS; status change names S121 `mined`. **M101's "evidence" is the plan + Gate, not a receipt** (D8) |
| 9 | ScribeScorecardCheck (calibration) | frozen predicate sentence identical in plan/annotation/receipts; `c98d137 → 80bb8921` ancestors of master; Next-66 rename consumed exactly the round-65 debt | `P†` ancestors verified (`c98d137`→`80bb8921`; `0e104f49`→HEAD). "Identical" holds only **modulo N**: plan says `over N assertions`, annotation says `234` (D7). Debt-by-debt consumption of the Next block is `O` |
| 10 | ScribeSHONEN2 (calibration) | box-1 commands at `0e104f49` print 18 Sources entries and gate registry 42/42; evidence lines name real revs; box-2/3 pointers resolve | `P†` I counted 18 Sources entries at `0e104f49` (`awk` section count); `42 of 42` is in `noharm-tip.txt @0e104f49`; the SHONEN line names rev `80bb8921` (real ancestor; SKILL.md unchanged tip→HEAD). box-2/3 pointer resolution not checked → `O` half |
| 11 | ScribeSourcesRow2 (freshness) | S121 row: 11 well-formed cells, enums, tier scoped, used-by paths exist, exactly one added line | `S†` `git diff --numstat c98d137..0e104f49 -- corpus/SOURCES.md` = `1 0`; 11 cells; `paper`/`A`/`mined`; recheck `180d`; used-by = the knowledge entry + lesson (both added in the same commit); `census-after.txt` carries no E11 |
| 12 | RevC1Predicate2 (depth) | no dishonest counter prints 234/exit 0 with the span branch gutted; kill conjunct exercises the branch; receipts pin `(sha256,234)`; floors row makes deletion loud | `P` pins settled (`b6cfc764…`, 234, recomputed by me at tip); SM1 dies with 5 span-arm FAILs per receipt; floors row + tables land. The **universal** ("a dishonest counter") is *not* settled: the entry's own Limits say the guard detects silent arm deletion, not a counter that prints a fake count |
| 13 | RevC1Arms (depth) | 11 new arms are non-vacuous and non-redundant; each fails ≥1 mutant and passes honest | `P` the pkg7 control (230 = 234−4) proves SPAN_FIRST/SPAN_LAST/M20 load-bearing (each survives without its arm) and M11 is a witness only (fails as collateral). The 7 package arms have **no** control world proving each is load-bearing → `O` (w1[20]) |
| 14 | RevC2Mechanism (calibration) | no laundering door: excuse a never-red subject, two subjects, a subject outside the two files, or ride a line that introduces a new dead token | `P` two doors closed by receipt: never-red subject (`M99` bug B) and a backticked new dead token on the notice (`C2-selfreference-redbefore` shows the notice line itself scanned). Multi-subject / outside-file / plain-text-token doors have no receipt → `O` |
| 15 | RevReceiptRevs (calibration) | every receipt names its measured rev internally; SCORECARD citations match | `X` **falsified**: `C2-selfreference-redbefore.txt`, `FLOORS-after.txt`, `M99-fixture-leak.txt` carry no `@ <rev>` (grep audit, §3); `FLOORS-after.txt` additionally records checklist 1852 while `80bb8921`'s checklist is 1862 (D2, D3) |
| 16 | CriticC1Bound (depth) | the C1 headline asserts only what the counter measures; the "17 named lanes" are enumerated; two-sided evidence exists | `P†` 17 kill rows are enumerated by name between the baseline and the equivalents in the receipt (25 `==` rows total); M19/M22 carry the surviving-equivalent side; the Q26 bound (headline vs measurement) is critic judgment → `O` |
| 17 | CriticC2Bound (calibration) | the governance PASS is a function of the corrections; `corrections=()` at tip FAILs; self-test arms are load-bearing | `O` — the only red-before is the *pre-gate* world `C2-before @c98d137` (three cells named at `LOG.md:2533`, `LOG.md:2580`, `SCORECARD.md:158`); no `corrections=()`-at-tip run and no arm-deletion run exist |
| 18 | CriticFrontier (coverage) | S121 tier-A defensible as author-hosted preprint; teaches scoped; sourced claim honest; census exit 0 holds | `P` row read: `paper`/`A`/`mined`, teaches scoped to the second-order design claim; census files exist but carry **no exit code** (D4) — exit 0 is asserted in commit message/report/spot-check, not in the receipt; tier judgment is `O` |
| 19 | CriticReceipts (calibration) | mutants are exactly one-string replacements (5/17 re-derived); pkg7 control is "candidate minus four arms"; self-reference red-before FAIL names the notice token | `P` the self-reference receipt is a **fixture-world** reproduction (`LOG.md:2`, token `corpus/gone.md`), not the live `LOG.md:2619–2621` red (D14); the 5-of-17 re-derivation and independent pkg7 rebuild are `O` |
| 20 | MutNewLanes (depth) | 10 fresh span-branch mutants, each killed by a named arm or named a new lane | `O` — no receipt |
| 21 | MutGovArms (calibration) | 8 correction-mechanism mutants, each killed by a named arm | `O` — no receipt (two shapes are covered by M99/selfref) |
| 22 | SentScope (operability) | verifiers make no network calls / no shell-outs to untrusted paths; `--rev` boundary unchanged; r64 sandbox+timeouts debt status | `P†` grep: v32 imports `subprocess` + `urllib.parse` only (no `urllib.request`/`socket`/`http.client`); checklist's subprocess calls handle `TimeoutExpired`; **v32's `git()` has no timeout** → the r64 timeouts debt is still open (D13); full boundary re-audit `O` |
| 23 | SentWaveSpecs (calibration) | the wave dir holds no secrets; each context carries the bounds sentence and the Q44 kill-cap sentence exactly once | `P†` Q44 = 1 and `All paths absolute under` = 1 per spec context (jq+grep); payloads carry Q44 twice; **secrets scan not performed** → that half `O` |
| 24 | RevNoHarm (calibration) | noharm battery green at tip; SCORECARD/LOG diffs append-only except the recorded rename + SHONEN refresh | `P†` `noharm-tip.txt` + `FLOORS-noharm.txt @0e104f49` green; my numstat confirms LOG `+8/−0`, SCORECARD `+3/−1`, SHONEN `+1/−1`, v32 `+92/−0`; **registry `+63/−59` is a whole-file reindent**, so "append" wording overstates (D6). Full battery rerun is the seat's → `O` half |
| 25 | ScoutS049Recheck (freshness) | both Accept profiles reproduce 17,252 B / `dae9d3ec…`, or a recheck note is due | `O` — no receipt; network not exercised by this seat |
| 26 | ScoutLessonBacklog (depth) | every M-row cites resolving evidence; Gate quotes ≤25 words | `P†` quotes 16 and 24 words; M99/M100 evidence receipts exist at tip; M101 cites plan+Gate, no receipt (D8) |
| 27 | CriticPlanFreeze (calibration) | plan `2fdfc1fd` precedes implementation `80bb8921`; predicate identical; no after-count before the freeze | `P†` order verified: `2fdfc1fd` is an ancestor of `80bb8921` (02:42:52 < 03:01:30) and receipts `5253b281` follow the implementation; predicate caveat D7. "No after-count ran before freeze" is not falsifiable from committed bytes (only from wall-clock) |
| 28 | ScribeDispositions (calibration) | this table | `SELF` |
| 29 | ExecHarnessArchive (depth) | `kill_battery.py` prints `RESULT: ALL OK` from a fresh archive; divergence vs receipt | `P` harness committed (7,353 B) and its header pins `TREE=/tmp/r65work/tree`, "never the live lane tree"; the receipt tail carries `RESULT: ALL OK` / `harness_exit=0` — **that is the L1's run**; independent run `O` |
| 30 | CriticPlanSizing (calibration) | each after-state is one concrete value; §9 shortcut controls were built before data and committed; predicate identical | `P†` the three before-controls were added in `2fdfc1fd` (`git log --diff-filter=A`), before `80bb8921`; the predicate caveat is D7; `M99-fixture-leak.txt` is a **post-hoc regeneration** of a bug shape, not a pre-data control |
| 31 | ScribeCensusCheck (freshness) | census files committed, both exit 0, 118→119 rows, 16 W04 both, format matches the frozen census section | `P†/X` committed at tip, 16 W04 each (my count); 118/119 reproduced by my SOURCES.md count, **not present in the files**; no exit code in the files (D4); the script and `CORPUS.md` are fleet-side and absent at `0e104f49` (D5) |

## 5. W2 disposition table (32 items)

Every w2 row is a falsification seat. "Recorded" means the round-65 receipt
already prints the value the seat is meant to re-derive; none of these was
re-executed by me except where marked `†`.

| # | seat (axis) | claimed finding | disposition |
|---|---|---|---|
| 0 | RevW2C1Count (depth) | 234/exit 0 @tip vs 223/exit 0 @`c98d137`; sha pair `(b6cfc764…, 234)` | `P†` tip half re-derived by me (234, exit 0, sha `b6cfc764…` at `0e104f49`); base 223 not re-run → `O` half |
| 1 | RevW2C2Count (calibration) | `--json` 11/11 exit 0 @tip with `3 recorded correction(s) excused`; 10/1 exit 1 @base | `P` recorded in `C2-governance-measure.txt` / `C2-before.txt` (detail string present); not re-run → `O` |
| 2 | RevW2Kill (depth) | full 17-mutant battery re-derived; equivalents survive; pkg7 control admits 3 arms | `O` |
| 3 | MutW2NewLanes (depth) | judge-level witnesses the four new arms miss | `O` |
| 4 | MutW2GovLanes (calibration) | three live-repo notice mutations fail closed; in-place fix makes the row stale | `O` |
| 5 | CriticW2Dishonest (depth) | cheapest dishonest world meeting C1: padding fails the kill conjunct; floors 999 named | `O` |
| 6 | CriticW2GovDishonest (calibration) | each single revert (resolve / sha) reddens a **named** arm | `O` |
| 7 | ScoutW2Census (freshness) | 119 rows, histograms, duplicate-id scan, S121 used-by | `O` — and now ambiguous: HEAD registry is 120 rows (D1) |
| 8 | ScoutW2S121Live (freshness) | fresh curl byte-identical to the snapshot | `O` (network) |
| 9 | ScoutW2ReceiptPaths (calibration) | every path cited by SCORECARD/lesson exists at tip | `O` |
| 10 | ScoutW2AppendOnly (calibration) | append-only sweeps green except the two recorded renames | `P†` my numstat covers the shape (see w1[24]); the script itself not run |
| 11 | ExecW2RedoMeasure (depth) | both frozen sentences reproduce byte-exact from a clean archive | `P†` C1 reproduced (234, exit 0); C2 not re-measured |
| 12 | ScribeW2Report (calibration) | 32 w2 rows each cited to a receipt or marked open | `O` — this table is its skeleton |
| 13 | ScribeW2LessonAddendum (calibration) | addendum skeleton for dispatched results | `O` |
| 14 | RevW2EntryTruth (depth) | every falsifiable sentence in the entry supported by bytes | `P` measured-record, attribution and pkg7 description match the receipt on my read; sentence-by-sentence pass `O` |
| 15 | RevW2ScorecardTruth (calibration) | every cited rev is an ancestor; consumed debt matches a landed change; carried debt verbatim | `P†` ancestors verified; debt mapping `O` |
| 16 | RevW2NoHarm2 (calibration) | six prior gates re-run and compared to their pins | `O` |
| 17 | CriticW2FrontierBound (coverage) | S121 on uncovered ground; sourced-claim binds C1 honestly | `O` |
| 18 | CriticW2Q47 (depth) | surviving-equivalent set is measurement-time, not a fixed list; M22 truly semantics-preserving | `O` |
| 19 | SentW2Scope2 (operability) | sandbox/timeout debt not worse; recommendation status | `P†` v32 `git()` is still unbounded (D13); "not worse" `O` |
| 20 | SimpW2DeadWeight (depth) | no arm/receipt/prose duplicating a pin; deletions named | `O` |
| 21 | RevengerGovIntent (calibration) | ERRATA/CORRECTIONS split consistent with round-47 intent | `O` |
| 22 | MutW2LabEquiv (depth) | hypothesis: the M20 arm alone kills the M20 mutant | `P` both legs are in the kill receipt: `control+M20-page-content-words` (control world, no new arms) exits **0** — the mutant survives without the arm — and `M20-page-content-words` (candidate) exits **1** with two FAILs: the M20 arm first, plus the M11-exact-case arm as collateral. So the arm is load-bearing; strict "alone" is touched by the M11 collateral. Independent re-run `O` |
| 23 | ScoutW2Spotcheck (calibration) | re-open commands for the two gate decisions, ready to run | `O` — no material file written |
| 24 | CriticW2SHONEN (calibration) | box-1 prints what the line claims at `0e104f49`; "18 at 80bb8921" real; no `[x]` without a non-author verifier | `P†` 18 verified at `0e104f49`; SHONEN line names `80bb8921`; box audit `O` |
| 25 | RevW2Plan (calibration) | landed work matches frozen predicates; disposition the SPAN two-arm deviation | `O` — note the plan lists SPAN_FIRST/SPAN_LAST as **one** bullet containing two arms; the deviation is arguable only through the N-measured-at-landing clause (D7) |
| 26 | ScribeW2ReceiptAudit (calibration) | every receipt names its rev; bundle sized to claims; split respected | `P†` rev audit done (3 missing, D2); sizing/split `O` |
| 27 | MutW2Floors (operability) | each single-artifact deletion named by drift checks; floor 233 FAILs | `O` |
| 28 | ConnW2Fleet2 (adjacency) | specs free of sibling scope; Q44 = 1 per context; bounds present | `P†` Q44 = 1 and bounds = 1 per spec context (measured); sibling-scope audit `O` |
| 29 | CriticW2Mistakes (calibration) | M99–M101 are real classes with shown-able-to-fail fixes; M101 honestly caught before data; minimality | `P†` M99/M100 receipts demonstrate their FAILs; M101's evidence is the plan text naming the rejection before data (no receipt, by design); minimality `O` |
| 30 | ScoutW2State (operability) | ahead=0, clean tree, no stray files, watchdog untouched | `O` — and the premise has moved: HEAD is round-66 and `.ufo/waves/round-65/w1/swarm-registry.json` is modified in the working tree |
| 31 | RevW2FrontierGate (freshness) | Gate quote ≤25 words; access line complete; rejected candidate has reason+flip; search log names the round-65 search | `P†` 16/24 words counted; access line carries URL+date+bytes+sha; rejection reason recorded in the lesson Gate. **No SOURCES search-log note exists for round 65** (D9) |

## 6. Counts and the closure's dispatch set

| Wave | `S`/`S†` | `P` family (`P`, `P†`, `P†/X`) | `O` | `X` | `SELF` | total |
|---|---|---|---|---|---|---|
| w1 | 3 (idx 4, 8, 11) | 22 | 5 (idx 3, 17, 20, 21, 25) | 1 (idx 15) | 1 (idx 28) | 32 |
| w2 | 0 | 13 | 19 | 0 | 0 | 32 |

Counts are machine-tallied from the two tables above. The closure's open set is
the **24 `O` rows** plus the open halves named inside the `P` rows (each `P` row
names its uncovered half). Only 3 rows are settled outright by committed
artifacts (all in w1), and only through L1-authored receipts; nothing in this
round has been independently re-executed except the checks in §1.

## 7. Defects and observations found by inspection

- **D1 — "the tip" is no longer `0e104f49`.** `HEAD` is `2a8eba56` (round-66
  spot-check), 10 commits ahead. v32 prints **240** at the live tree vs **234**
  at `0e104f49` (both exit 0, my runs); `corpus/SOURCES.md` is **120** rows at
  HEAD vs 119 at tip. Any w1/w2 item that says "at the tip" without pinning
  `0e104f49` will measure round-66 bytes and may report false drift (a `tip`
  regex hits 5 w1 and 7 w2 prompts). Affects w1[1], w2[0], w2[7], w2[11],
  w2[30] first.
- **D2 — three receipts carry no internal rev** (falsifies w1[15] as written):
  `C2-selfreference-redbefore.txt`, `FLOORS-after.txt`, `M99-fixture-leak.txt`.
- **D3 — `FLOORS-after.txt` is unrev'd and internally inconsistent with the
  landing:** it records `checklist observed=1852 floor=1852` while
  `80bb8921`'s committed checklist self-test is 1862. It cannot be tied to a
  commit; `FLOORS-noharm.txt @0e104f49` supersedes it (checklist 1862, v32 234,
  floors_guard 165).
- **D4 — census receipts carry neither row count nor exit code.** Both files are
  17 lines: 16 `W04` + `ok …/corpus/SOURCES.md`. The plan's "118 rows"/"119 rows"
  re-derives from the registry (my counts), not from the receipt; the census
  script's `validate` mode prints findings only (its own header, ll. 21–27).
- **D5 — census provenance is fleet-side:** `scripts/sources-census.sh` and
  `CORPUS.md` live in `/home/vgpnk/Projects/shokunin`; neither path exists at
  `0e104f49`, and the receipt does not record cwd or script path.
- **D6 — the floors-registry diff is a whole-file reindent:** `+63/−59`,
  `instrument_total` 14→15, key delta exactly `scoped_rules_v32`. The substance
  (one row added, bump-in-step) is right, but any "append-only" phrasing over
  this file is false.
- **D7 — the frozen predicate is "identical" only modulo N:** plan says `over N
  assertions` (N measured at landing), the annotation says `234`, receipts print
  outputs. Items demanding byte-identity (w1[9], [27], [30], w2[25]) need the
  N-instantiation wording.
- **D8 — M101 has no receipt:** its evidence is the plan text and the Gate
  (caught before data). w1[26]'s "every M-row cites evidence that resolves" holds
  only if plan/Gate count as evidence.
- **D9 — no SOURCES search-log note for round 65.** The plan says the rejection
  is "recorded in the search log"; the record exists in `plans/round-65.md`,
  `corpus/lessons/round-65.md` and `corpus/README.md:116`, but `corpus/SOURCES.md`
  has no round-65 search note at the tip. (Round-63/48 lessons treat the SOURCES
  note as "the search log".)
- **D10 — closure report wave histogram undercounts:** its w2 line reads
  "mutation-tester 3" while the spec has 4 (MutW2NewLanes, MutW2GovLanes,
  MutW2LabEquiv, MutW2Floors); the line's numbers sum to 31, not the declared 32
  (`/home/vgpnk/Projects/shokunin/.ufo/reports/round-65/kotoba.md:57`).
- **D11 (positive) — the C1 floors registration is real at the tip:** registry
  row `floor 234`, both in-file tables (guard ll. 172/231), docstring l. 11;
  `FLOORS-noharm` 15/15 PASS, `floors_guard observed=165 floor=150`.
- **D12 — the integrity debt has no receipt in this round:**
  `REGRESSION-probes.txt` prints `corpus_integrity exit None fail None`, so the
  claimed red numbers (113 vs 81, unindexed 3, 76 vs 51, 37 vs 32,
  commit_unresolvable 2) appear only in the report/spot-check, not in a
  measurement artifact.
- **D13 — the r64 sandbox/timeouts debt is still open on v32:** its `git()`
  helper (ll. 479–481) runs `subprocess.run([...])` with no timeout; the
  checklist's subprocess calls do catch `TimeoutExpired`.
- **D14 — the self-reference red-before is a sandbox reproduction,** not the live
  red: the receipt's FAIL names `LOG.md:2` and `corpus/gone.md`, not the live
  `LOG.md:2619–2621` notice lines.

## 8. What this table supports and falsifies, per claim

- **C1 frozen sentence — SUPPORTED at `0e104f49` by my own run:** the three
  predicate lines print (`worlds reject 7 of 7; eligible rows pass 4 of 4`,
  `survivors closed 6 of 6`, `self-test: 0 failure(s) over 234 assertions`),
  exit 0, instrument sha `b6cfc764…` recomputed from committed bytes. The
  **kill conjunct** is supported only by the L1-authored battery (17 named
  lanes, equivalents green, pkg7 control 230) — not independently re-executed
  here.
- **C1 floors registration — SUPPORTED:** row + both tables + docstring, guard
  green with 165 observations against floor 150.
- **C2 frozen sentence — RECORDED but not independently verified:** 11/11 exit 0,
  1862 assertions, `3 recorded correction(s) excused` live only in
  `C2-governance-measure.txt`; base 10/1 in `C2-before.txt`. My own checklist run
  covers the self-test count only (1862, exit 0).
- **Receipt discipline (Q36) — FALSIFIED for 3 of the 9 receipt `.txt` files**
  (D2); the rev-less `FLOORS-after` also contradicts the landing's checklist
  count (D3).
- **Census (frontier) — PARTIALLY SUPPORTED:** 118→119 rows re-derived from the
  registry; the receipts that should carry the count and exit code do not (D4,
  D5).
- **Frontier gate — PARTIALLY SUPPORTED from committed bytes:** snapshot sha
  `bad1b681…`/1,126,684 B reproduce and both quotes occur exactly once
  whitespace-normalized (16/24 words). I did **not** re-read the PDF's DOI/
  venue header, the live URL, or a search-log record; those remain open
  (w2[8], D9).
- **Non-author closure already on record:** `corpus/lessons/round-65-verifier-spotcheck.md`
  (integrator, commits `11385e0`/`2a8eba5`) recomputed the C1/C2 pins and the
  three line-sha pins and admits both claims "evidence-verified; gates not
  executed". That corroborates the pins; it does not substitute for the w2
  execution set.

## 9. Bounds observed / not done

- Read-only outside this file; no jj/git write, no lane index change, no fleet
  repo mutation. Scratch only under `/tmp/r65tip` (git-archive extraction of
  `0e104f49`) and `/tmp` for Python temp files; at most 2 concurrent processes;
  each run bounded by `timeout 120`.
- Not done: any network fetch (S121 live, arXiv, S049), any mutant/probe
  construction, any gate battery rerun beyond the seven commands in §1, any
  secrets scan, any jj state check.
- Tool installs/updates: **none** (no package manager invoked; pacman paused per
  the orchestrator ruling).

## 10. Artifact

`Report: .ufo/waves/round-65/w1/ScribeDispositions.md`

Sibling w1 seat reports were appearing in the same directory while this table was
written (`ConnSibling2.md`, `CriticFrontier.md`, `CriticPlanFreeze.md`,
`MutNewLanes.md`, `RevReceiptRevs.md`, `ScoutLessonBacklog.md`,
`ScoutQualityDebt3.md`, `ScoutS049Recheck.md`, `ScoutS121Reopen.md`,
`ScribeCensusCheck.md`, `ScribeSHONEN2.md`, `ScribeSourcesRow2.md`,
`SentWaveSpecs.md`). They are the dispatched seats' own outputs and are **not
consumed here** — this table is built from the L1's committed receipts and my own
read-only spot-checks, so the closure should take any `O`/`P` row's newest value
from the seat report where one exists.
