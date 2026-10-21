verdict: The fleet L0 channel carries 7 lines naming kotoba — 2 open operator-only (kotoba r13 axis-accounting, kotoba r22 r16adj), 1 partially ruled (aggregator r6/D-78), 1 answered by protocol ruling (kengaku r10), 3 incidental or moot — plus 2 kotoba round-46 axis questions that were filed only in the round-46 report and never appended to the channel; round 47's report must carry the r13 line and both unqueued r46 questions, and should record the r22 durability closure.

# L0 open-line census for kotoba (round 47 build, scout)

## Basis (measured, not inferred)

- Lane repo `kotoba-shokunin`, BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`: `git rev-parse HEAD` → `c61a973b…` (exit 0); only untracked paths are `?? .ufo/waves/`, `?? plans/round-47.md`.
- Target file is **outside** the lane repo: fleet root `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md`, fleet HEAD `f06d385504df72934b461d4c35e583bc33c01b05` (clean: `git status --porcelain -- .ufo/l0-questions.md` → empty, exit 0).
- File identity at measurement: 82 lines, 63,497 bytes, sha256 `c13d612b01718232b9f5a62ee8ff84675b1da6261659ab81786b5dd51eb125a1`; `git hash-object` == `git rev-parse HEAD:.ufo/l0-questions.md` == `8005e36e4e5b5d29f3221594d27831f1a15d0a62` (worktree byte-identical to HEAD).
- **Citation rule conflict, resolved:** `../PROTOCOL.md:524-530` says cite an L0 question by **lane + round + opening words, never by line number** ("the queue grows, so every line number moves"). This report therefore keys every row by lane|round|opening words and gives the line number only as a measurement stamp at the 82-line/`8005e36e` state above.
- Membership measured with `grep -in 'kotoba' ../.ufo/l0-questions.md` → lines 6, 7, 11, 12, 17, 40, 50 (exit 0; case-insensitive set identical).
- Answer-line control: `grep -c '^operator' ../.ufo/l0-questions.md` → `0` (exit 1). Inline answers exist only at lines 52, 53 (`L0 ANSWER`, other lanes), 75 (`SUPERSEDES`, tsukuroi), 77 (`RESOLVED-BY-RULING`, tabi). **No kotoba line has an inline answer.**
- I read all 82 lines of the channel, plus the aggregator's L0 triage table and the D-78 ruling cell.

## A. Required set — the 7 fleet-channel lines naming kotoba

State vocabulary: **OPEN** (no answer, no superseding record) · **PARTIALLY-RULED** · **ANSWERED-BY-RULING** (not by operator) · **MOOT** (premise false at HEAD) · **UNQUEUED** (exists outside the channel).
Carry vocabulary: **YES** = omitting it makes a round-47 claim unverifiable or repeats a false record; **CONDITIONAL** = carry only if round-47's claim language touches that surface; **NO** = fleet/operator-side, no lane obligation.

| # | Key (lane \| round \| opening words) | Stamp | State + evidence | Carry in r47 report? |
|---|---|---|---|---|
| 1 | aggregator \| round-6 \| "Axis vocabulary split (ledger row D-78)…" | `../.ufo/l0-questions.md:6` | **PARTIALLY-RULED, operator open.** `../.ufo/reports/AGGREGATE.md:1236` → "RULED-partially … scores are calibration defects until the vocabulary exists; operator action owed (`AXES.md` is operator-side). L0 line 6 stands"; `:1811` → "open, operator-only". `grep -n 'novelty\|consistency' ../AXES.md` → exit 1 (none); `../MISSION.md:27` still assigns "depth + consistency". Lane's remedy is on record: `SCORECARD.md:7-15` declares `consistency` a calibration sub-axis, which satisfies `../PROTOCOL.md:513-516` (an axis not in AXES is worked only if its row carries the mapping). | **CONDITIONAL** — C3 is a calibration claim and consistency is its declared sub-axis, so one line should state the mapping is unchanged and the operator remap stays open; not a blocker and not a new claim. |
| 2 | kengaku \| round-10 \| "Promote the gate convention (exit 0/1/2 + --selftest…)…" | `:7` | **ANSWERED-BY-RULING.** `../.ufo/reports/AGGREGATE.md:1812` → "answered by protocol ruling, not by the operator — §Gate standard (`dddb4ec`) pins `0=clean`/`1=failed` … Remaining residue is adoption, not decision (D-137…D-140)". `git cat-file -t dddb4ec` → `commit`, dated 2026-09-28; rule text at `../PROTOCOL.md:375-410`. kotoba-specific residue: `AGGREGATE.md:1682-1683` classifies `verifiers/verify_surfaces.py` and `verify_harness_claims.py` as **probe** until a registry row + frozen run exist (**D-140**). | **CONDITIONAL (D-140 only)** — C1 re-pins `verify_surfaces.py`; if the report calls any verifier a *gate*, the §Gate standard's registry/two-evidence clause applies and D-140 must be named. The L0 question itself owes no operator answer. |
| 3 | kotoba \| round-13 \| "Axis-accounting ratification, two items…" | `:11` | **OPEN, operator-only.** `../.ufo/reports/AGGREGATE.md:1815` → "open, operator-only; both halves evidenced (advisory-axis legality; D-78 fold of `consistency` into `calibration`) — a lane does not retire a mission-assigned axis on its own word". No answer line; `:40` re-asserts "Existing kotoba round-13 axis-accounting questions remain open". Item 1 (may a lane work an advisory axis as its lowest-axis move) is **directly engaged by round 47**: `plans/round-47.md:20` labels C1 freshness "lowest non-retired axis, 8.0; tie with adjacency", and `SCORECARD.md:101` says "lowest non-retired axis **under the all-axes reading**". The lane's owned non-retired lowest is depth 9 (`SCORECARD.md:28`), so C1 meets the all-axes/SCORECARD-lowest readings but **not** the owned-only reading (`SCORECARD.md:274`: "Advisory axes … are outside the line's scope"). | **YES** — the C1 move-selection record must state the reading and that r13 item 1 is unratified. Precedent: `../.ufo/reports/round-13/kotoba.md:139-140`, `../.ufo/reports/round-16/kotoba.md:98-99`, `LOG.md:538-539` ("recorded, not re-litigated"). |
| 4 | aggregator \| round-9 \| "CORPUS.md amendment set — four measured conflicts…" | `:12` | **OPEN, operator-side.** Fleet corpus-policy text; kotoba appears only as an occurrence count (`kotoba` corpus at `63ceba7`). `../.ufo/reports/AGGREGATE.md:1817` publishes it as an appended operator-side set; no answer. | **NO** — no r47 claim touches `CORPUS.md` rule text. (C3's corpus index work touches `corpus/README.md`/index, not this line.) |
| 5 | kama \| round-1 \| "Fleet hygiene gap … .gitignore lines 1-6 list … but OMIT kama-shokunin/…" | `:17` | **MOOT** — premise false at fleet HEAD. `../.gitignore:1` is now the glob `*-shokunin/`; `git check-ignore -v kama-shokunin` → `.gitignore:1:*-shokunin/` (exit 0), and the same for `kotoba-shokunin` (exit 0). kotoba is named only as one of the previously listed lanes. | **NO.** If mentioned at all, mark the line stale (premise no longer true). |
| 6 | kotoba \| round-16 \| "Reconcile the relaunched round namespace and craft-batch contract…" | `:40` | **OPEN, non-blocking.** No answer and no inline resolution. Operationally moot: the steered numbering has run 16→46 continuously (`SCORECARD.md:98` round 46 completed; `:100` "Next: round 47"), and round 47 is the next number in lane order — no counter or report collision. | **NO** — no r47 claim depends on it. Optional only in a carried-open footnote. |
| 7 | kotoba \| round-22 \| "r16adj owner packets across the five siblings…" | `:50` | **OPEN (0 ack) but DURABILITY CLOSED.** Ack still 0: `grep 'r16adj'` over `../LOG.md`, `../.ufo/reports/AGGREGATE.md`, `../MANIFEST.json` → 0 rows; lane's sixth measure 0/5 at `SCORECARD.md:34`. Durability: `git log --all -S'r16adj' -- .ufo/l0-questions.md` → `31baf5c`; `git merge-base --is-ancestor 31baf5c HEAD` → exit 0. Commit `31baf5cb07049637a09e18cc421535e376beecd1`, 2026-10-19T17:03:23-03:00. The lane's earlier "uncommitted" records (`LOG.md:1243`, `LOG.md:1265`; `SCORECARD.md:34` round-26 segment) are append-only historical and now **superseded**. | **CONDITIONAL (record hygiene)** — no r47 claim is adjacency, but C3 claims records match repo state; if the report or its LOG entry touches L0/adjacency it must use the closed state (31baf5c) and not repeat "uncommitted". |

## B. The two unqueued kotoba round-46 questions (the operative gap)

Both are filed in `../.ufo/reports/round-46/kotoba.md` § L0 questions and **not** in the fleet channel: `grep -c 'round-46' ../.ufo/l0-questions.md` → `0` (exit 1); `grep -n '^kotoba |'` → only 11, 40, 50. Fleet L0 commit `543f06e` (2026-10-21) added only kake r25 and tsukuroi r21, so the omission was not repaired. That is a conformance gap against `../PROTOCOL.md:524-530` (lanes append; the aggregator surfaces what is in the file) — a question living only in a report is never surfaced and never durable in the channel.

| # | Key | Stamp | State | Carry in r47 report? |
|---|---|---|---|---|
| 8 | kotoba \| round-46 \| "Does AXES.md's 'lowest non-retired axis' range over advisory axes?…" | `../.ufo/reports/round-46/kotoba.md:141` | **UNQUEUED / OPEN.** It is the exact reading question for r47 C1. Its own note says "r47's C1 is freshness, so it meets both readings" — **false under the owned-only reading** (lowest owned non-retired is depth 9; freshness is advisory), true only for the all-axes and SCORECARD-lowest readings. | **YES** — C1's lowest-axis compliance rests on this reading; the report must name the reading and correct/qualify the "both readings" sentence. Recommend the L1 append one consolidated L0 line for Q1+Q2. |
| 9 | kotoba \| round-46 \| "Can a lane amend an append-only LOG citation that later goes dead (`LOG.md:2111` → never-committed runner)?…" | `../.ufo/reports/round-46/kotoba.md:142`; target line `LOG.md:2111` (verified: the 19:38:15Z bullet recording "referenced runners are absent") | **UNQUEUED / OPEN; round 47 is implementing option 1 without a ruling.** `plans/round-47.md:35-38` (C3) builds "a pinned, fail-closed erratum registry for recorded absences (LOG.md:2111 …)", and `SCORECARD.md:104` already words the standing debt as "needs a gate erratum mechanism or the runner re-derived". No operator answer exists on any tracked surface. Honest counterargument: the registry records the erratum **in the gate**, not as an edit to `LOG.md`, so it may be lane-local gate design rather than a use of the contested amendment authority — but the report must say which reading it takes, because the question as filed offers exactly these two branches and was never answered. | **YES** — C3 must name the unqueued question and the branch chosen, and must not present the registry as an operator ruling. |

## C. Adjacent axis-accounting lines (outside the required set; no kotoba mention)

Listed so the L0 carrier does not silently conflate them with kotoba's:
- `:31` kama r1 — "MISSION operability+freshness assignment versus the generated prompt's operability+calibration": the same MISSION-vs-prompt axis path drift as D-78, for a different lane; open, non-blocking for kotoba.
- `:35` kengaku r13 — advisory-axis tie-break ("Coverage and novelty tie at 7; coverage is selected…"): the kengaku analogue of kotoba r13 item 1; open.
- `:47` kotodama r11 — freshness recheck threshold recalibration ("Freshness axis-move claims are paused until ruled"): bears on any lane's freshness scoring, not on kotoba's C1 beyond the advisory reading.
- `:73` kengaku r25 — novelty verdict conversion: D-78 family, kengaku-owned.

Round 47's mission prompt (C1 freshness / C2 operability / C3 calibration) is a **third** axis combination not identical to MISSION.md's kotoba assignment (`depth + consistency`, `../MISSION.md:27`) — same class as line 31, and further evidence that the prompt's axis labels are not derived from MISSION.md. This is why the reading must be recorded in the report rather than assumed.

## D. Rule derivation for the carry verdicts

- `../PROTOCOL.md:173-175` requires every dispatched lane's report to list a stale **mission** (>2 driver ticks) and say progressing/silent — it is not a general L0-rectal clause. No rule requires restating every open L0 line.
- `../PROTOCOL.md:524-530` makes L0 a lane-append + aggregator-surface channel; the integrator owns durability. So an operator-side line with no answer creates no per-round report duty **by itself**.
- The carry duties above come from the claims, not from the channel: `../AXES.md:33` ("at least one claim works the lane's lowest-scoring non-retired axis"), `../AXES.md:70-72` (nudge), `SCORECARD.md:271-274` (owned-only scope), and `../PROTOCOL.md:513-516` (undefined axis names need an in-row mapping). C1 engages rows 3 and 8; C3 engages rows 1, 7, 9; C2 engages nothing in the L0 set.
- `../PROTOCOL.md:375-410` (§Gate standard) is the answered residue of row 2; `AGGREGATE.md:1896-1899` (D-140) names kotoba's specific gap.

## E. Counterexamples (records that are now false, or readings that do not hold)

1. **"L0 line 50 is uncommitted"** (`LOG.md:1243`, `LOG.md:1265`, `SCORECARD.md:34` round-26 segment) — false at fleet HEAD `f06d3855`: committed by `31baf5c`, ancestor check exit 0, worktree == HEAD blob `8005e36e`. Rounds 23–35 scouts repeatedly re-measured the old state; round 47 must not.
2. **"r47's C1 is freshness, so it meets both readings"** (`../.ufo/reports/round-46/kotoba.md:141`) — false for the owned-only reading: depth (9) is the lowest owned non-retired axis (`SCORECARD.md:28`); consistency is retired at 10 (`:29`). It meets the all-axes and SCORECARD-lowest readings only.
3. **Line 7 treated as a live operator question** — it was answered by protocol ruling `dddb4ec` on 2026-09-28 (`AGGREGATE.md:1812`); the live residue is adoption, kotoba's being D-140 (probe, no registry row, no frozen run). Filing it as unanswered would misfile the decision.
4. **Line 17's gitignore premise** — `.gitignore:1` is `*-shokunin/`; `git check-ignore -v kama-shokunin` exits 0. The line is stale, not pending.
5. **Line 40's namespace collision** — no collision at round 47: `SCORECARD.md:98` records round 46 complete, `:100` names round 47 next, and the lane LOG/report sequence is continuous 16→47.

## F. Commands run (exit codes and key output)

| Command (cwd) | Exit | Key output |
|---|---|---|
| `git rev-parse HEAD` (lane) | 0 | `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (BASE); status: `?? .ufo/waves/`, `?? plans/round-47.md` |
| `git rev-parse HEAD` (fleet) | 0 | `f06d385504df72934b461d4c35e583bc33c01b05` |
| `sha256sum .ufo/l0-questions.md`; `wc -l -c` | 0 | `c13d612b…`; `82 63497`; terminal byte `0a` |
| `git hash-object` vs `git rev-parse HEAD:.ufo/l0-questions.md` (fleet) | 0 / 0 | both `8005e36e…`; `git status --porcelain` empty |
| `grep -in 'kotoba' .ufo/l0-questions.md` | 0 | lines 6, 7, 11, 12, 17, 40, 50 |
| `grep -c '^operator' .ufo/l0-questions.md` | 1 | `0` (no operator answer lines) |
| `grep -c 'round-46' .ufo/l0-questions.md` | 1 | `0` (r46 questions unqueued) |
| `grep -n 'L0 ANSWER\|RESOLVED\|SUPERSEDES' .ufo/l0-questions.md` | 0 | 52, 53, 75, 77 — none kotoba |
| `git log --all --oneline -S'r16adj' -- .ufo/l0-questions.md` | 0 | `31baf5c` |
| `git merge-base --is-ancestor 31baf5c HEAD` | 0 | ancestor |
| `git log -1 --format='%H %cI %s' 31baf5c` | 0 | `31baf5cb…` 2026-10-19T17:03:23-03:00 |
| `git check-ignore -v kama-shokunin` / `kotoba-shokunin` | 0 / 0 | `.gitignore:1:*-shokunin/` |
| `git cat-file -t dddb4ec` | 0 | `commit` (2026-09-28) |
| `grep -n 'D-78' ../.ufo/reports/AGGREGATE.md` | 0 | 1236 (RULED-partially), 1811 (open, operator-only) |
| `grep -n 'kotoba r13' ../.ufo/reports/AGGREGATE.md` | 0 | 1815 (open, operator-only) |
| `grep -n 'D-140' ../.ufo/reports/AGGREGATE.md` | 0 | 1682-1683, 1899 (probe until registry + frozen run) |
| `grep -in 'kotoba\|AXES\|MISSION\|lowest' .ufo/l0-questions.md` | 0 | required set + axis lines 31/35/47/73 |
| `sed -n '2111p' LOG.md` (lane) | 0 | the 19:38:15Z bullet: runners absent, exit 2 |
| `grep -n 'still unanswered\|recorded, not re-litigated' LOG.md` | 0 | 538-539 |
| `grep -rn 'l0-questions' --include='*.md' .` (lane, excluding waves) | 0 | carried in LOG.md:536,779,1221,1243,1265; SCORECARD.md:15,34; two knowledge notes |
| `grep -nE 'l0-questions\|L0\|lowest\|D-78' ../.ufo/reports/round-46/kotoba.md` | 0 | 139-142 (§ L0 questions) |
| `grep -n 'l0-questions\|L0\|AXES.md' .ufo/reports/round-4{3,4,5}/kotoba.md` (lane) | 1 | no matches — carriage lapsed after round 16 |

## G. What I did NOT check

- Did not run any lane verifier/gate (`verify_skill_checklist.py`, `verify_surfaces.py`, `check_substrate_pins.py`, corpus verifiers) — outside this item and not read-only in intent.
- No host-private surfaces: no session transcripts, tokens, auth files, or operator console. Absence of an answer is measured **only** on tracked fleet/lane surfaces (L0 file, fleet LOG/AGGREGATE/MANIFEST, lane reports/LOG/SCORECARD).
- Did not semantically adjudicate the non-kotoba L0 lines beyond the marker scan and the four adjacent axis rows; e.g. kasegi/kama/tsukuroi open items were not re-verified.
- Did not verify D-137..D-139 or any sibling's gate registry; only kotoba's D-140 classification.
- Did not test the round-47 claims themselves (C1 re-pin, C2 description check, C3 erratum registry) — other seats own those.
- Did not check whether an answer exists in the operator's chat or an untracked prompt; line numbers are measurement stamps, not the protocol citation key.

## H. Remaining unknowns

- Whether the operator's D-78 partial ruling (`AGGREGATE.md:1236`, "scores are calibration defects until the vocabulary exists") is intended to override `PROTOCOL.md:513-516`'s in-row mapping remedy now carried at `SCORECARD.md:7-15` — the two records can be read as compatible (mapping satisfies the process rule; the vocabulary defect stays operator-side) but no text resolves it. [INFERENCE]
- Whether the round-46 Q1/Q2 report-local filing was deliberate or an omission; no commit message or note says.
- Whether round-47's C3 erratum-registry design was cleared with the operator outside tracked surfaces — none found.
- Whether an acknowledgment for r16adj exists in a surface I did not read (sibling working trees were not re-swept this round; the lane's last live measure was 0/5 at `SCORECARD.md:34`).

Confidence: high on all measured states, file identities, and commit relationships; medium on the carry verdicts in §A/§B, which are derived from AXES/PROTOCOL/SCORECARD rather than from an explicit "reports must list open L0 lines" clause (no such clause exists).
