# Kb82K02Mistakes — cross-round mistake-class connection, r79→r82

Seat: leaf connector. Axes judged: **freshness**, **operability**. No subagents, no clone (analysis-only seat; clones are for code work), no production gates rerun, no after-values scored, no installs, no pacman activity. Disk guard checked (`/tmp 25%, /var/tmp 41%, /fast/scratch/hyaku 47%`). All evidence is read-only git/grep over the lane at base `47dbe8781657de563ff867caca6244d28e3db504` plus the round-82 committed before-receipts. Commands and exits: `.ufo/waves/round-82/build/Kb82K02Mistakes-commands.txt`; structured evidence: `.ufo/waves/round-82/build/Kb82K02Mistakes-evidence.json`.

## 0. Headline findings

1. **The r82 plan does not repeat the stale-premise class on its headline befores.** All six checked premises match committed receipts or blobs (§A, table). The class is nonetheless uncaptured at the mechanism level: M81-3 (reading a live worktree plan as a measurement source) has no Q row, and nothing mechanically binds a plan's before-text to a receipt.
2. **The C2 failure is the M125 class recurring, not a new class.** The failing arm pins a live verdict (`verify_skill_checklist.py:2524-2528`, reading `live_repo` at :2522); its literal exception counts ("2 recorded absence(s) excused, 4 recorded correction(s) excused") still match the receipt — the live SCORECARD merely gained new dead subjects during r80/r81. Q65's remedy ("re-run whenever the record it reads changes") failed operationally because no owner re-runs it between rounds. **Genuinely new mechanism needed: a selftest-hermeticity rule** — no `--self-test` arm may read live mutable state (§B). No QUALITY row says this (`grep -in 'hermetic\|isolat' corpus/QUALITY.md` → 0 hits).
3. **There is a second live-dependent arm the plan's C2 text does not name.** `verify_skill_checklist.py:2531-2542` ("governance: LOG.md:2678 erratum is load-bearing") also evaluates against `live_repo`. Isolating only the failing arm leaves the selftest non-hermetic (independently flagged by peer `Kb82R02Checklist.md` §Source trace point 8).
4. **The r82 provenance control (SHA-checked counter bytes and gate blobs in predata receipts) is same-class, not new mechanism.** It applies the existing Q24/Q73/Q75 pinning pattern. The standing hazard from r81 connector review persists: pins certify bytes, not logic — the r80 E05 pinned blob was killed on logic — so the freeze receipt should name a non-author reviewer for the C1 gate-diff review or state self-review explicitly.
5. **Open residues in the same class:** the r81 landed `verifiers/external-commits.json` manifest remains unpinned (routed duty 3a, disposition "retained open" per `Kb82R06Routed.md`), and the W-A/W-C "padded-report target" is the ≥400-byte size-arm class that Q75's marker-substitution control already covers in principle.

## A. Class 1 — stale planned premise

Recurrence (each instance a plan asserting base truth that measurement contradicts):

| round | instance | evidence | captured by |
|---|---|---|---|
| r47 | M20 `stale planned premise` (class origin) | `corpus/lessons/round-47.md` | **Q19** |
| r72 | M124 `stale-premise (record vs tree)`: r71 plan promised `53 of 53` registry, measured `51 of 53` at `c69711e` | `corpus/lessons/round-72.md:77` | Q50 / Q65 clause |
| r80 | plan named `google-gemini/gemini-cli@451a02ff` and `zed-industries/zed@cfb894a5` as the red pair; measured reds were the bare `7bb48f21…` tokens at `corpus/SOURCES.md:171-172` | `.ufo/waves/round-80/w1/Kb80K02Patterns.md` §0.1; `Kb80C01C1.md:66` | Q19/Q36 require re-measurement; plan text itself unchecked |
| r81 | plan asserted independent gate `report_dead 1`; measured 0 (the r80 K02 correction was never cited in the r81 plan) | `.ufo/waves/round-81/w1/Kb81K02Patterns.md` §0.1, §1 | same |
| r81 | M81-3: `plans/round-81.md` read twice from the **live worktree** carried `LINE_CAP 40 → 140`, which never froze (frozen `e6d48e6` reads `40→900`); seat brief quoted 140 too | `corpus/lessons/round-81.md:43` | **none** — "no criterion says an uncommitted worktree file is not a measurement source (Q51 binds *counters* to committed bytes)" |
| r82 | **this plan's before-premises** | see table below | seat-verified |

**r82 premise verification (this seat's measurements):**

| plan premise | measured | verdict |
|---|---|---|
| pins before: 1 PASS, 2 UNREADABLE, exit 2 (`before-pins.txt`) | omp.real sha256/mtime UNREADABLE ×2, opencode sha256 PASS, exit_code 2 | MATCH |
| selftest before: `1 failure(s) over 1863 assertions`, exit 1 | identical line, sole failing arm named, exit=1 | MATCH |
| public gate reports `governance.citation_resolves` FAIL | `before-checklist.txt`: FAIL, evaluated 1363, same 4 dead occurrences, overall exit 1 | MATCH |
| counter is the unchanged round-72 counter | blob `e25442db…f5ab5` identical at `30d27da` (r72 freeze 2) and base `47dbe87`; `git log --follow` shows a single commit touching the file | VERIFIED |
| skill line budget base 597/600 | `git show 47dbe87:SKILL.md \| wc -l` → 597 | MATCH |
| C2 floor: N ≥ 1863 | current count 1863 | MATCH (must not be reduced) |

**Same-class Q criteria vs new mechanism.** Same-class and sufficient *in principle*: Q19 (carried/planned before-value re-measured at round start; copied values struck), Q36 (receipt names its revision), Q50, Q55. Genuinely uncovered: the M81-3 shape — a seat (or seat brief) quoting a **live worktree file** as if it were the frozen plan. Q51 binds counters to committed bytes, not seat readings. A new mechanism would be a binding of plan-before-text to committed receipts (e.g. every before-claim in a plan carries its receipt path and a checker diffs claim vs receipt), but the r82 plan does not need it to proceed: its premises are receipt-cited, and this seat verified all six. **Verdict: same-class, operationally recurring (4 rounds), one uncaptured sub-shape (worktree-as-source). Recommend: land a Q row for M81-3 (worktree bytes are never a measurement source; `git show <freeze>:<path>` or a committed snapshot sha is), rather than a new instrument.**

## B. Class 2 — live-dependent selftest (C2's actual failure)

Timeline:

- **r65 (`80bb892`)**: arm `governance: live round-65 corrections land, errata-excused` introduced; it evaluates `check_governance_citations` against the **live repo** and asserts PASS with pinned excused-counts.
- **r72 (M125, `reference-drift`)**: the arm went stale when the r71 errata retired its expected red; the r72 fix re-anchored constants to the live state and added a load-bearing regression arm, floor 1862→1863, and the class was captured by **Q65** ("a self-test arm that pins a live verdict is re-run whenever the record it reads changes").
- **r82 (recurrence)**: during r80/r81 the live SCORECARD gained four new dead-subject occurrences (three unique tokens: `.ufo/wapes` at `SCORECARD.md:480`, `corpus/lessons/round-80-verifier-spotcheck.md:30,37` at :482, `.ufo/reports/round-81/kotoba.md` ×2 at :484). The arm's expected literal counts (2 absences, 4 corrections) **still match** the receipt — the mechanism works; the pinned live verdict drifted. Q65's remedy failed operationally: nothing re-runs the arm when the record changes, so it drifted twice in ten rounds.

Code: `verifiers/verify_skill_checklist.py` — `live_repo = Path(__file__).resolve().parent.parent` at **line 2522**; failing arm at **2524-2528**; **second** live-dependent arm at **2531-2542** (`governance: LOG.md:2678 erratum is load-bearing`, also reading `live_repo`).

**Same-class Q criteria vs new mechanism.** Same-class: Q65 (the capturing row — but its remedy is a maintenance duty with no owner, i.e. it converts a design defect into permanent toil), Q48 (self-test must drive `main()` with exact-line assertions — silent on fixture hermeticity), Q63 (a fake-repo self-test does not stand in for an honest real-world run — adjacent, about counters running lane gates). None requires `--self-test` fixtures to be isolated from live mutable state; `grep -in 'hermetic\|isolat' corpus/QUALITY.md` → 0 hits. **Verdict: genuinely new mechanism.** The r82 plan's C2 design — replace the live arm with isolated fixture evidence; discriminators (valid correction green; missing correction red; restored stale target red; unrelated dead subject red; unrelated live-governance edits must not change fixture results); disable-the-guard-and-show-the-fixture-fails — *is* that mechanism, and its disable/reenable discriminator is Q57-shaped two-sided evidence already required by existing criteria. What is missing is **landing it as a Q row** so the next instrument does not re-create the class: propose Q77 (number after Q75; the Q76 draft name is already reserved by the never-landed stray-artifact row — `grep -c '^| Q76 ' corpus/QUALITY.md` → 0 at base and worktree): *a self-test arm never reads live mutable repo state; assertions about live content belong to the public gate with committed receipts, and a self-test's result must be invariant under edits to live governance/corpus files outside the fixture.*

**Operability risk to flag for L1:** the plan's C2 names only the failing arm. The LOG.md:2678 load-bearing arm (2531-2542) is equally live-dependent; if the C2 patch isolates only :2524-2528, the selftest remains one live edit away from red. Required discriminator to add: "editing live LOG.md/SCORECARD.md with a new dead subject must not change `--self-test` exit" — which the plan's "modifying unrelated live governance must not change fixture self-test results" already covers if applied to *both* arms.

## C. Class 3 — counterfeit report / provenance controls

Recurrence:

| round | instance | control born |
|---|---|---|
| r79 | M79-1: counter's own in-file script-only world scored 1/6 while an **independent mechanical generator** reached 6/6 | Q71 (name the script-only world's score), Q74 (independent generator before semantic admission) |
| r80 | M80-4 W8-W10: real lane commit with lane marker classified external; fabricated absent lane hash in a lane-URL row classified external; **seven-byte marker at the fleet report path passed the existence check**; all reached 6/6 | Q75 (bind identity/content, not path existence; marker-substitution control must stay red) |
| r81 | R1 (`## SHONEN` substring + ≥400 B) and R2 (committed manifest + receipt) re-created marker/self-attested classes; predictions in `Kb81K02Patterns.md` §2 (W11/W12 controls suggested; plan listed W0-W9/C0-C4 only) | plan-level, honest stop |
| r81 | Landed R2: `verifiers/external-commits.json` + committed fetch/ls-remote receipts (marker grammar no longer sufficient cause; W6/W7 worlds) — `corpus/lessons/round-81.md:13` | E6 `INSTRUMENT_PINS` tight tuples `(<r72 base blob>, <reviewed r81 blob>)` |
| r81 | M81-5: W-A forged repository binding and W-C padded report both reached `6 of 6`, stopped honestly, not scored | frozen kill rule in plan |
| r82 | plan control: "Counter bytes and proposed gate blobs are SHA-checked and committed with the predata control receipts before scoring either after-value"; freeze receipt must exist before after-scoring | this round |

**Same-class Q criteria vs new mechanism.** Same-class, no new mechanism: Q22 (a byte-hash match establishes byte identity only, not custody), Q24 (receipt's instrument hash checked against committed instrument bytes), Q34 (SOURCES append-only with its checker), Q37 (cheapest real-input shortcut controls, incl. marker variants, committed before data), Q57 (disable-guard admittance as two-sided evidence), Q73 (append-only sha256 ledger inside a counter with an unledgered-rewrite self-test arm), Q75 (marker substitution at the report path must stay red). The r82 freeze-receipt pattern (sha-checked counter bytes + gate blobs, committed predata) is a direct application of Q24 + Q73 + the Q65 "freeze before data" protocol sentence.

Two standing hazards, both previously named, neither a new mechanism:
1. **Pins certify bytes, not logic** (`Kb81K02Patterns.md` §2, on E6): the r80 E05 blob was published as an `INSTRUMENT_PINS` value and then killed on logic by W8-W10. The r82 plan's C1 "review gate diffs without running revised code" names no reviewer. The freeze receipt should name the non-author reviewer of the gate diffs/pin updates or state that the review is self-review (Q16 non-author marks; Q51 judgment assignment).
2. **The r81 landed manifest is unpinned** (routed duty 3a): `verifiers/external-commits.json` has no sha pin in a counter/freeze receipt, so a seat can still edit the exemption data without an instrument-pinned edit. Disposition per `Kb82R06Routed.md`: "retained open unless separately repaired." This is the Q73-shaped gap inside the r81 repair itself; repairing it is in scope for r82's routed duties, not for C1/C2's predicates.

## D. Same-class vs new mechanism — verdict table

| class | same-class Q criteria | captured? | new mechanism needed? |
|---|---|---|---|
| stale planned premise | Q19, Q36, Q50, Q55 (+Q65/M124) | yes for receipt-cited befores; **no for worktree-as-source (M81-3)** | no new instrument; **one new Q row** for the M81-3 sub-shape |
| live-dependent selftest | Q65 (remedy = unowned toil), Q48, Q63 (adjacent) | partially — Q65 captured the r72 instance and its remedy failed operationally | **yes: selftest hermeticity** (no live mutable reads inside `--self-test`); r82 C2 implements it as a one-off — land it as a Q row; isolate **both** live arms (2524-2528 and 2531-2542) |
| counterfeit report/provenance | Q22, Q24, Q34, Q37, Q57, Q73, Q75 | yes | no; apply Q24/Q73/Q75 pinning; close the two named residues (unnamed freeze reviewer; unpinned external-commits.json) |

## E. Recommendations to L1 (no edits made by this seat)

1. C2 scope: isolate **both** live arms (`verify_skill_checklist.py:2522-2542`), not only the named failing one; add the "live-governance edit invariance" discriminator covering the LOG.md:2678 arm.
2. Land two Q rows with the round-82 lesson: (a) M81-3 worktree-as-measurement-source; (b) selftest hermeticity. The Q76 draft name is consumed by the stray-artifact row; use the next free number and note Q76's never-landed status in the lesson.
3. Freeze receipt: name the non-author reviewer for the C1 gate-diff/pin review, or state self-review (bytes-pinned ≠ logic-reviewed, per the r80 E05 precedent).
4. Routed duty 3a (unpinned `external-commits.json`): repair with a Q73-style sha256 ledger + unledgered-rewrite self-test arm, or keep "retained open" explicit in the final report — do not let the landed r81 binding read as closed by implication.
5. Keep the C2 assertion floor at N ≥ 1863 (verified current count 1863): replacing a live arm with fixture arms must net-add or hold, never drop.

## F. Limits

- I ran no production gate except none: every measurement above is either a committed round-82 before-receipt, a read-only `git show/rev-parse/log -S`, or a grep over base bytes. No after-values scored; no scratch worlds built (attack seats own those).
- Peer files `Kb82R02Checklist.md` and `Kb82R06Routed.md` were read once as running-seat snapshots; their content may evolve.
- The r79 in-file-fixture row and r80 W-world rows are cited from lessons and prior connector reports (`Kb80K02Patterns.md`, `Kb81K02Patterns.md`), not re-executed.
- Q-criteria quotes were read from `corpus/QUALITY.md` at the worktree (base-identical for the rows cited; the only worktree delta known to this seat is unrelated S-source churn).

VERDICT: Three classes connected across r79-r82. Stale-premise: r82 plan's six headline premises all match committed receipts/blobs (counter blob e25442db… unchanged since r72 freeze 30d27da; SKILL.md 597; pins 1+2/exit 2; selftest 1/1863/exit 1; public governance.citation_resolves FAIL) — same-class under Q19/Q36/Q50/Q55, one uncaptured sub-shape (M81-3 worktree-as-source, needs a Q row, not an instrument). Live-dependent selftest: C2's failure is M125 recurring (arm literals still match; live SCORECARD drifted) — Q65's re-run remedy failed operationally; genuinely new mechanism required (selftest hermeticity; no QUALITY row mentions hermetic/isolated), and the fix must isolate BOTH live arms at verify_skill_checklist.py:2522-2542 including the unnamed LOG.md:2678 arm. Counterfeit report/provenance: r82's SHA-checked predata receipts are same-class (Q22/Q24/Q34/Q37/Q57/Q73/Q75), not a new mechanism; two residues to close or keep explicitly open: unnamed freeze reviewer (bytes≠logic, r80 E05 precedent) and the unpinned r81 external-commits.json manifest.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82K02Mistakes.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82K02Mistakes-evidence.json, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82K02Mistakes-commands.txt
