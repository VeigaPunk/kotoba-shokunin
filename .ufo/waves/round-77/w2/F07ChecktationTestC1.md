# F07ChecktationTestC1 — w2 falsification: mutation-test of the C1/C2 counter gate paths (round 77)

Seat: F07ChecktationTestC1 (leaf, no subagents, no background jobs). Round 77 wave w2.
Lane: /home/vgpnk/Projects/shokunin/kotoba-shokunin. Scratch: /fast/scratch/hyaku/kotoba-r77/F07Mutation-TestC1/ (removed before yield).
Axes attacked (judged axes named): **depth + consistency** (gate sensitivity on real claim bytes), **calibration** (floors/tolerances quantified), **freshness** (committed-vs-draft state of the claim data), **operability** (runtime tamper-evidence asymmetry C1 vs C2).

## 0. Prime finding — the claim data is NOT committed (blocker, reported, not pretended)

- Lane HEAD during this seat: `6523aced1ee0ebe07dca996213bdc645a6acbd1e` = the freeze commit ("freeze plan, base receipts"). `git log` shows **no commit after the freeze**; landing-order steps 2–3 (controls, data) are not landed.
- `git status --porcelain` counted 35 untracked/modified paths at seat start (w1 receipts, build/ drafts, wave state), and **52 by seat end** — the wave tree churned while w2 ran. Concrete drift observed: `.ufo/waves/round-77/build/E06EntryVerify.commands.txt` appeared in a directory listing and was gone (read: "No such file or directory") minutes later, mid-seat.
- Consequence: at the landed tip the frozen counters are red exactly as pinned — nothing is falsifiably "landed" for C1/C2 yet. Every data-side probe below therefore ran against w1 **draft** bytes assembled in my own scratch clone (pinned by sha256 below), never against a lane commit. No lane file was written by this seat.

## 1. Pristine baselines (each gate's own exit status captured; no `| tail` pipelines)

Commands run in the lane tree; outputs kept in scratch (inlined here):

```
$ python3 -B verifiers/check_desc_craft.py --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e --work <scratch>/work
  ... (a)–(f) each "fail" ...
description craft backed 0 of 6
exit=1
$ python3 -B verifiers/check_r75_routed_repairs.py --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e --work <scratch>/work
  ... R1–R4 each "open" ...
r75 routed repairs closed 0 of 4
exit=1
$ python3 -B verifiers/check_desc_craft.py --self-test        -> self-test: 0 failure(s) over 53 assertions ; exit=0
$ python3 -B verifiers/check_r75_routed_repairs.py --self-test --repo <lane> --work <scratch>/work
                                                                -> self-test: 0 failure(s) over 27 assertions ; exit=0
$ python3 -B verifiers/check_desc_craft.py --print-self-sha   -> d5a06d6e89c7515e46096515f631a921377252fe574153b266a8beeae96c9da1
```

- HEAD red receipts match the committed base receipts (`receipts/c1-base-2f67554….txt`, `c2-base-2f67554….txt`: `0 of 6` / `0 of 4`, exit 1) — HEAD carries no data, so red is the honest state, and the counters are not vacuously green.
- Counter bytes match the plan pins: `cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e` (C1), `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63` (C2). C1's `--print-self-sha` equals its in-file `SELF_SHA` (guard armed).
- The counter's `PAGE_SHA` pins were re-hashed against the committed snapshots: optimizing-descriptions `7cc54fbb…bfd837` MATCH, evaluating-skills `a799805f…fb684` MATCH, best-practices `ab9f3b60…fb41` MATCH — the S213 digest pin holds on committed bytes (fresh URL re-opening is the reopen seats' duty, not re-run here).

## 2. Independent data-tip assembly (scratch clone; the only git writes of this seat)

`git clone --shared` of the lane; `user.name=scratch-r77`, `user.email=scratch@example.invalid` set before the first commit; `git rev-parse --show-toplevel` == the clone dir; all four w1 patches applied cleanly at `6523aced` (`git apply --check` ok ×4). Inputs pinned by sha256 (build/ was churning, so bytes were copied into scratch first): entry `8d648442a7f1d…`, skill.patch `1122809b94ae…`, SOURCES.patch `2a05870c2064…`, r1 patch `125b0e691f5b…`, r1 receipt `d9bcb5e1be4b…`, noharm receipt `bb81f3d0fff0…`, LOG patch `b309250214f0…`, w2 note `07d72021e036…`, lesson-76 `e111ef4f8b60…`.

Scratch data tip `55d5691fb4d42d97e49d307d6c70fec0e28dcddf` (one commit on the freeze):

```
C1 at 55d5691f: (a)–(f) all pass — description craft backed 6 of 6 ; exit=0
C2 at 55d5691f: R1–R4 all closed — r75 routed repairs closed 4 of 4 ; exit=0
```

This independently reproduces w1's E06 (`c1-tip-6of6`) and E05 (`c2-after-r3r4`) claims from the draft bytes — at a scratch tip. It is not a lane commit.

## 3. C1 counter mutation battery

Method: single-point source mutants of the frozen counter, built in scratch only; except C1-M1 each is **counterpinned** (mutant's own blanked sha written into its `SELF_SHA` line) so the drift guard does not mask logic; detector = `--self-test` (pristine: `0 failure(s) over 53 assertions`, exit 0) and, for survivors, a measurement run at the data tip.

| ID | Mutation (one point) | Detector result | Verdict |
|---|---|---|---|
| C1-M1 | comment-only byte change, NOT counterpinned, `--rev 55d5691f` | `environment error: counter drifted -- the running file is not the frozen counter …`, exit 2 | KILLED (guard fires) |
| C1-M2 | `MIN_QUOTES = 4` → `2` | 4 failure(s) / 53, exit 1 | KILLED — via the pinned finding text "of the required 4"; **no world has 2–3 counted quotes** |
| C1-M3 | `TOTAL = 6` → `5` | 18 failure(s) / 53, exit 1 | KILLED |
| C1-M4 | `return 0 if held == TOTAL` → `held >= TOTAL - 1` | 15 failure(s) / 53, exit 1 | KILLED (5-of-6 worlds must exit 1) |
| C1-M5 | verdict `backed` → `bound` | 18 failure(s) / 53, exit 1 | KILLED (verdict line is pinned by every world) |
| C1-M7 | delete the "(f) no recheck field" world (compile-checked mutant) | `0 failure(s) over 50 assertions`, exit 0 | **SURVIVED** — self-test floor `assertions >= 30` accepts a suite shrunk to 30; only the plan's pinned 53 catches shrinkage |
| C1-M8 | `MAX_QUOTE_WORDS = 25` → `400` | 0/53, exit 0; at data tip `6 of 6` exit 0 | **SURVIVED** (independently confirms w1 M01's M04) |
| C1-M9 | `if len(counted) < MIN_QUOTES` → `<=` | 0/53, exit 0; at data tip `6 of 6` exit 0 | **SURVIVED** (independently confirms w1 M01's M30; no world has exactly 4 counted) |

## 4. C2 counter mutation battery

C2 has **no drift guard**, so mutants run directly; detector = `--self-test` (pristine `0 failure(s) over 27 assertions`, exit 0).

| ID | Mutation | Detector result | Verdict |
|---|---|---|---|
| C2-M1 | innocuous byte change, `--rev 55d5691f` | measures normally: `4 of 4`, exit 0, no drift error | **SURVIVED (runs unguarded)** — only the plan's sha256 pin detects tamper, post hoc |
| C2-M2 | `TOTAL = 4` → `3` | 25 failure(s) / 27, exit 1 | KILLED |
| C2-M3 | `RENDER_CLIP = 1022` → `1023` | 3 failure(s) / 27, exit 1 | KILLED (R1b recomputes the render from bytes) |
| C2-M4 | R4 proximity `if max(idxs) - min(idxs) > 3:` → `> 1000:` | 0/27, exit 0 | **SURVIVED** — no world spreads the settlement lines apart; independently confirms w1 M02's M28 (omission operator) with a threshold operator |
| C2-M5 | `ABSENT_WORDS` drop `"absent"` | 2 failure(s) / 27, exit 1 | KILLED |

## 5. Data-side mutants (gates pristine; claim bytes mutated; each one commit, then `git reset --hard 55d5691f`)

| ID | Defect (one logical point) | Gate result | Verdict |
|---|---|---|---|
| D-A | "Err on the side of being pushy" misquoted → "pushx" in **all 3** entry occurrences (body quote + recheck token list + table cell) | C1: `description craft backed 6 of 6`, exit 0 — unchanged | TOLERATED — conjunct (b) is a floor: ≥4 located quotes of 11 counted; single-phrase corruption cannot flip it. Predicate property, not a gate defect; the independent all-quotes review is the real control |
| D-B | Body-craft row removed from SKILL.md (skill patch reversed) | `5 of 6`, exit 1 — "(c) no Body craft row cites both …" | KILLED |
| D-C | entry claims 1023 instead of 1022 (3 occurrences) | `5 of 6`, exit 1 — "(d) … does not equal the recomputed clip render 1022 (stripped variant 1021)" | KILLED |
| D-D | S213 used-by reverted (SOURCES patch reversed) | `5 of 6`, exit 1 — "(e) row S213's used-by cell does not list …" | KILLED |
| D-F | entry `recheck:` line dropped | `5 of 6`, exit 1 — "(f) the entry carries no `recheck:` field" | KILLED |
| D-E | no-harm receipt exit token 0→1 (integrity block) | C2: `3 of 4`, exit 1 — "R2: … records no exit code 0 for verify_corpus_integrity.py" | KILLED |
| D-G | w2 note path `w2/R75Attack28.md` → `w2/R75Attack-28.md` | C2: `3 of 4`, exit 1 — "R3: the note does not name the absent report path …" | KILLED |

## 6. Findings and minimal repairs (harm analysis)

1. **[blocker, process] Claim data uncommitted.** Repair: L1 lands step-2/3 commits (controls, then data) per the plan's landing order; w2 verdicts should cite the landed hash, not draft bytes. Harms none; unblocks the round.
2. **[coverage, C1] Self-test assertion floor too low** (`>= 30` vs 53 actual): world deletion survives (C1-M7). Repair: raise the floor to the suite's own count (pin 53) in a **pre-data addendum + counter re-pin** (bytes are frozen this round); otherwise record as an accepted blind spot in the round lesson. Self-test-only change; harms no axis.
3. **[coverage, C1] No world with exactly 4 counted quotes; no >25-word quote world** (C1-M8/M9). Same disposition and repair path (add two worlds). Self-test-only; harms none.
4. **[operability, C2] No runtime drift guard** (C2-M1): a mutated C2 measures normally; only the plan's sha256 pin detects, post hoc. Repair path: mirror C1's `SELF_SHA` blanked-sha guard in a future frozen-counter revision; this round, verify the pin before every receipted run (the plan already pins it). Harms none.
5. **[coverage, C2] R4 proximity check untested** (C2-M4). Same disposition (add a spread world). Self-test-only; harms none.
6. **[calibration, disclosed] Data-side floor tolerance** (D-A): the counter is a floor instrument (4-of-11 quotes, 2-of-3 fragments); single-point claim corruption inside the slack is invisible to it by design. Keep the independent quote/row reviewers in w2; do not widen the counter.
7. **[freshness] build/ churned during w2** (E06 receipt file vanished mid-seat; status 35→52). Repair: L1 should commit or freeze build/ bytes before w2 verdicts cite them; this report pins the sha256s it used.

No mutation flipped a red claim green on honest bytes; every non-tolerance mutant of the landed gates was killed. The four counter-side survivors are self-test coverage gaps, not contract breaks; none warrants editing the frozen counters this round.

## 7. Restoration evidence

- Lane counter sha256 before and after the seat (identical): `cf3c45d9…b9e` (C1), `989203c4…a63` (C2). Lane HEAD unchanged: `6523aced1ee0ebe07dca996213bdc645a6acbd1e`. Lane writes by this seat: none (the status delta 35→52 is sibling w2 traffic).
- Scratch clone ended clean (`git status --porcelain` = 0 lines) at `55d5691f…` — exactly one documented scratch commit on top of the freeze; all mutant/data commits were `reset --hard` back to the data tip or the freeze during the battery.
- Tools installed: none. pacman: not used (paused host-wide). Scratch dir removed before yield.

VERDICT: C1/C2 gate paths held — 12/16 mutants killed incl. all 6 targeted data-side kills on real draft bytes (independently re-assembled to 6 of 6 / 4 of 4 at scratch tip 55d5691f); 4 self-test coverage survivors documented with repairs; BUT no claim data is committed at lane HEAD 6523aced, so C1/C2 remain red-by-design at the landed tip and the round's claims are not yet landed — L1 must land controls+data before w2 closure.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w2/F07ChecktationTestC1.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w2/F07Mutation-TestC1.md
