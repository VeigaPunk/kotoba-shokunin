# Kb81E07C2Worlds — C2 control worlds (C0–C4) for kotoba round 81, w1

Seat: leaf executor, no subagents, no background jobs. Lane `kotoba-shokunin`, base
`b284223105f4d106f7e8f56ed4fd296c643cda0e` (tree `d3be81e55b457c2a2e6dc65c026005b30dd770d3`). Lane git was read-only
throughout (no add/commit/stash/checkout); every write is under `.ufo/waves/round-81/` and scratch under
`/fast/scratch/hyaku/kotoba-r81/Kb81E07C2Worlds/` (deleted before yield). Skill read first: `skill://godspeed`.

**Headline: all five plan controls are REFUSED by the frozen counter (C0/C2/C4 `0 of 1` exit 1; C1/C3 exit 2,
`could-not-evaluate`), and the two oracles that carry the wave's own published artifacts are CERTIFIED
(`sdk allowed-tools surface documented 1 of 1`, exit 0).** The controls therefore falsify nothing in the claim and the
counter is not vacuous; three findings change what the L1 must land and how the exit classes are read.

## 1. What I built

| file (under `.ufo/waves/round-81/build/`) | sha256 | what it is |
|---|---|---|
| `c2_controls.py` | `ed1d0416627f609af534ebbd53216b1d3d22172f0af91b5a7c895c429ca0bc01` | the generator: builds every world as an isolated scratch git repo at the base and runs the frozen counter |
| `c2_controls.txt` | `09a1962d0610999a38e4acafcc6663873d4a3e292bf5f1b463331c10ccc855f6` | the published run: 8 worlds, 8 PASS, per-world exact lines, exit, expected vs observed, class, PASS/FAIL |
| `Kb81E07C2Worlds.provenance.txt` | — (self-hash cannot be inline) | fixture provenance, the three counter blobs measured, the two pre-registration revisions, reproducibility |
| `Kb81E07C2Worlds.ref-counter.py` | `df5282eb71862d985795fe2b9da120bd01a81b7a83c6cde7a2dd51ce82ab5fc8` | my **PROVISIONAL** inline reference counter (conjuncts a–g per the plan), written while seat `Kb81E09C2Counter` had published nothing; **not used for the published run** — the published counter landed at 02:36 and is what `c2_controls.txt` measures |

Method (all in `c2_controls.py`): each world is its own repo — `git init` in a fresh mktemp dir under `--work`, one
`objects/info/alternates` line to a read-only `git clone --shared` of the lane at the base, `read-tree <base>`, fixtures as
blobs (`hash-object`/`update-index`), `write-tree` + `commit-tree -p <base>` with fixed author/committer dates,
`rev-parse --show-toplevel` asserted equal to the world dir. The counter is invoked exactly as the claim will be
(`python3 -B <counter> --repo <world> --rev <commit>`, cwd = world), and the counter's own exit and printed lines are
captured verbatim. No network. Runtime of a full suite: ~2 s. Suite exit codes: 0 all worlds match, 1 divergence,
2 unmeasurable (counter absent, unfrozen, or unable to evaluate any world).

## 2. Results (published run, FINAL counter `739a71810453f83c94468db25fc39c55f3bfbfdb224894a630d91e5aea86f985`)

The counter measured is the **final frozen** blob the counter seat announced (1,638 lines): its `SELF_SHA` (`38ac8513…`)
equals the hash of its own blanked bytes. Two earlier frozen blobs (`8e15a117…` `SELF_SHA 56cd3223…`, then `eb71aa23…`
`SELF_SHA 87e91917…`) were also measured as they landed; normalised diffs between all three runs change no count, class,
exit or finding on any of the 8 worlds (only the counter-sha line, the lesson fixture size and added tree-identity lines).

| world | role | what it breaks / asserts | observed (counter's own line) | exit | pre-registered | verdict |
|---|---|---|---|---|---|---|
| C0 | control | base copy (tree = base tree) | `sdk allowed-tools surface documented 0 of 1` | 1 | 0 of 1, exit 1 | **PASS** |
| C1 | control | honest world, snapshot bytes tampered against the pin | `environment error: snapshot_tampered: … hashes to 1e10f237…, the counter pin is ac62c2df…` | **2** | 0 of 1, exit 1 | **PASS** (refused; class differs — F1) |
| C2 | control | honest world, S248 `used-by` left `—` | `… documented 0 of 1`; `(e) S248: used-by '—' does not list corpus/knowledge/allowed-tools-sdk-round81.md` | 1 | 0 of 1, exit 1 | **PASS** |
| C3 | control | honest world, snapshot only untracked in the worktree | `environment error: .ufo/waves/round-81/snapshots/S249.md is not committed at …` | **2** | 0 of 1, exit 1 | **PASS** (refused; class differs — F1) |
| C4 | control | prose asserts `1 of 1`, no evidence files | `… documented 0 of 1`; all seven conjuncts FAIL | 1 | 0 of 1, exit 1 | **PASS** |
| N1 | diagnostic | honest world **minus** `corpus/lessons/round-81.md` | `… documented 0 of 1`; `(e) corpus/lessons/round-81.md absent at …: the S248 used-by old->new move is not logged` | 1 | 0 of 1, exit 1 | **PASS** |
| H1 | oracle | full honest shape, **corpus seat's** S249/S248 rows | `sdk allowed-tools surface documented 1 of 1`; `conjuncts: a ok … g ok` | 0 | 1 of 1, exit 0 | **PASS** |
| R1 | oracle | full honest shape, **entry seat's** S249 row (`integration-cells.md` §1) | `sdk allowed-tools surface documented 1 of 1`; `conjuncts: a ok … g ok` | 0 | 1 of 1, exit 0 | **PASS** |

Suite verdict line: `suite: 8 worlds, 8 PASS, 0 DIVERGE, 0 BUILD-ERROR` / `verdict: CONTROLS-HOLD — every control refused,
every oracle certified`. No control reached the target. The plan's C2 shape is satisfiable — H1 and R1 are two complete
honest fixtures, one per candidate row — and every control differs from them by exactly the broken conjunct named.

Fixtures are the wave's own published artifacts, committed byte-for-byte (not paraphrases):
`build/allowed-tools-sdk-round81.md` (entry, 16,254 B, `fe57322c…`) → `corpus/knowledge/allowed-tools-sdk-round81.md`;
`build/Kb81S01Lesson.md` (21,522 B at the published run) → `corpus/lessons/round-81.md`;
`build/Kb81E08C2Entry.integration-cells.md` (`d04387ec…`) → SKILL.md sentence + counter row, README row, PROVINCE bullet;
`build/Kb81S05SourcesEdits.md` (`a7905496…`) → S249 row + S248 `used-by`; `.ufo/waves/round-81/snapshots/S249.md`
(`ac62c2df…`, 28,395 B) → the pinned snapshot. No world carries the counter file itself (reading the frozen counter showed
conjunct (f)'s registry check reads `SKILL.md` only; an earlier revision embedded it and the embedding was removed as dead
weight).

## 3. Findings

**F1 — tamper and uncommitted-snapshot refusals are exit 2, not exit 1 (class, not substance).** C1 and C3 are refused with
`environment error:` and exit 2; the plan's controls say "→ red" and my pre-registration read red as exit 1. The counter's
own docstring declares the policy ("(c) is exit 2 when the committed snapshot is absent … when it does not hash to the pin
(`snapshot_tampered`) … exit 1 when the ROW's anchor record disagrees"). Both classes are refusals, so no control is
credited; the class is reported in `c2_controls.txt` beside the pre-registered exit. The counter seat's own announcement of
the final bytes states the same split (sha mismatch on the committed snapshot → exit 2 `snapshot_tampered`; a wrong ROW
anchor digest → exit 1; quote without committed snapshot bytes → exit 2), and its real-byte mutation receipt
`build/Kb81E09C2Counter-realbytes.txt` is the independent second measurement of that policy. **What the L1 must not write:** a claim
text or SCORECARD note implying that a tampered-pin world yields exit 1 — it yields 2 and prints no headline. The registry
row's `0=clean, 1=failed, 2=could-not-evaluate` already covers this; the plan's C1 sentence is the only place that reads as
exit 1.

**F2 — conjunct (e) has two arms: the S248 cell AND a lesson line, and the second is load-bearing.** N1 (everything
honest except the lesson) is refused `0 of 1` on `(e) corpus/lessons/round-81.md absent at <rev>: the S248 used-by old->new
move is not logged`; C2 (lesson present, cell stale) is refused on the cell. Consequence for integration: the lesson must
land in the **same commit** as the S248 cell, and its line must name S248, the entry path and an arrow. The published lesson
line satisfies this (the lesson's `- S248 used-by — → corpus/knowledge/allowed-tools-sdk-round81.md (round-81 C2; …)`
line), and C2's receipt shows `s248 old->new logged in the lesson ok`. This arm appeared in my rev-1 run as an oracle divergence
(`conjuncts: a ok, b ok, c ok, d ok, e FAIL, f ok, g ok`) — it is a reading of the plan's own parenthetical, not a counter
invention, and it is exactly what control worlds are for.

**F3 — the counter's own generator world reaches 1 of 1 (reported as the plan's rule requires; the counter seat declares
it the Q74 reading, not a defect).** The counter prints `generator world: M of 1` and, in four of my worlds — C2 and N1
(both *refused* by the counter itself) and the two oracles — `M = 1`, with the note `the generator world reaches the target
(1 of 1): the headline measures the FORM of the evidence shape, not the sourcing judgement (generated mechanically from the
measured bytes)`. The counter seat confirms this is intended: the generator writes the complete shape from the measured
bytes (including the S248 cell it then reads), so it reaches 1 wherever a pin-matching snapshot is committed, which is why
its score is printed and never gated. Two consequences for the L1/critics, stated rather than acted on: (a) the C2 headline
is a **form** claim — a tree fabricated mechanically from the committed snapshot satisfies all seven conjuncts, so
`1 of 1` must not be cited as semantic proof that the SDK grant channel is *sourced*; the entry's documentary work carries
that; (b) a world reaching the target while the measured tree is refused (C2, N1) proves the generator score is not the
measured tree and must never be read as an after-value. The plan's rule ("a world reaching a target is reported as a
counter defect, never repaired by narrowing") is why it is reported; whether the Q74 declaration satisfies that rule is the
L1's call, and I make no defect claim of my own here.

**F4 — the two candidate S249 rows are both admissible.** H1 (corpus seat's row: tier A, `used-by` = entry + lesson,
anchor with the ISO instant and the full digest) and R1 (entry seat's `integration-cells.md` §1 row: tier B, `fetched
2026-10-27`, `used-by` = entry) each reach `1 of 1` exit 0. The row choice is therefore **not** counter-load-bearing; the
census and the other corpus gates decide it. Also measured: the corpus seat's anchor rendering now conforms to the counter's
fetch-record grammar (the `(host-local date …)` parenthetical sits after the digest); earlier in the wave it sat between the
instant and `HTTP 200`, which the r80 `FETCHED_RE` grammar would have rejected — the suite keeps a normaliser that matched
nothing on the current row and prints `verbatim (the anchor normaliser matched nothing)`.

**F5 — `PROVINCE.md` (g) requires exactly one `## Core` bullet naming the entry** (`province_state`: `len(naming) != 1` is
a failure, and that one bullet must name the SDK channel). H1/R1 satisfy it with a new bullet (`province bullets naming the
entry: 1`). *Reading, not a measurement:* the S10 seat's proposal extends the round-80 bullet instead; that also yields one
naming bullet, but I did not build a world for it. If the L1 lands both a new bullet and an extended old one, (g) fails.

**F6 — counter freeze churn inside the wave, with no behavioural change.** The path went through three frozen blobs while
this seat worked: `8e15a117…` (`SELF_SHA 56cd3223…`, measured 02:37–02:40), `eb71aa23…` (`SELF_SHA 87e91917…`, measured
02:40–02:41), and the final `739a7181…` (`SELF_SHA 38ac8513…`, 1,638 lines, announced final by the counter seat and the blob
the published receipt measures). Normalised diffs across the three runs show no count, class, exit or finding change on any
world; all three are recorded in the provenance file.

## 4. Operability (how the L1 re-runs this)

```
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build
python3 -B c2_controls.py --list                        # the pre-registration table, no measurement
python3 -B c2_controls.py --work /fast/scratch/<you>/c2 > c2_controls.txt 2>&1; echo $?
```
Defaults: counter = `build/check_sdk_allowed_tools.py` if present, else the PROVISIONAL reference (and every result is then
marked PROVISIONAL); `--counter <path>` overrides; `--keep` keeps the world repos for inspection; `--work` defaults to
`$TMPDIR` or the seat scratch path. The suite refuses to run (exit 2) if the fixture snapshot's sha256/size differ from the
pin, if the base tree already carries any claim path, or if the base S248 `used-by` is not `—`. Two clean runs in the same fixture revision were byte-identical modulo the run timestamp and mktemp directory names (same
world commits for identical fixture bytes); a fixture revision changes the commits, never the verdicts. The published
run's commits, each a child of the base: C0 `37e4ee31…`, C1 `de50eb07…`, C2 `5ae50703…`, C3 `2b5ef375…`, C4 `5e007cc2…`,
N1 `e99d85ab…`, H1 `90c12176…`, R1 `c4444888…`.

## 5. What I did not do

* No edit to `verifiers/`, `corpus/`, `SKILL.md`, `PROVINCE.md`, `plans/`, or any lane file outside `.ufo/waves/round-81/`.
* No counter or corpus repair, no narrowing of any world. C1/C3 keep their measured exit-2 class visible rather than being
  relabelled to match the pre-registration.
* No after-value scored: every world is a fixture on the base revision; H1/R1 are oracles, not the landed tip.
* No network access; no tool installs or upgrades (nothing was needed; `python3` and `git` only).
* No claim that the S10 PROVINCE variant works — named as a reading (F5), not measured.

## 6. Risks / blockers

* **Not blocking.** Fixture fidelity is pinned to the three seats' published bytes; if the L1 lands different texts, re-run
  the suite (cheap, ~2 s) before quoting any number from `c2_controls.txt`.
* **Landing order risk (F2).** Lesson + S248 cell + entry must be in the same commit as the other cells; N1 is the receipt
  that a missing lesson alone costs the claim its `1 of 1`.
* **Reading risk (F1/F3).** If a critic reads the plan's C1/C3 "→ red" as exit 1, or reads `generator world: 1 of 1` as an
  after-value, this receipt is the evidence against both.
* The counter blob can be refrozen again (F6). The receipt names the blob it measured; any later blob needs a re-run before
  it can be cited.

## 7. Coordination

Consumed, all from `.ufo/waves/round-81/build/`: `check_sdk_allowed_tools.py` (frozen, seat Kb81E09C2Counter),
`allowed-tools-sdk-round81.md` + `Kb81E08C2Entry.integration-cells.md` (Kb81E08C2Entry), `Kb81S01Lesson.md` (Kb81S01Lesson),
`Kb81S05SourcesEdits.md` (Kb81S05SourcesEdits), and the committed snapshot `../snapshots/S249.md`. Nothing I needed was
absent at the published run; the PROVISIONAL reference counter was written before the counter seat published and is kept
only as a diffable fallback (it is not a proposal for `verifiers/`).

VERDICT: All plan C2 controls refused by the frozen counter (C0/C2/C4 exit 1 `0 of 1`; C1/C3 exit 2 `could-not-evaluate`), both oracles with the wave's published artifacts certified `1 of 1` exit 0; findings: exit-class reading (F1), the load-bearing lesson arm of conjunct (e) (F2), and the counter's own generator world reaching 1 of 1 (F3).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/c2_controls.py; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/c2_controls.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E07C2Worlds.provenance.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E07C2Worlds.ref-counter.py; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81E07C2Worlds.md
