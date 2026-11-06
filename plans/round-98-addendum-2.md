# Round 98 — addendum 2 (post-data disclosures; nothing frozen changes)

Author: KotobaR98 (L1). Written after the landing reading at `e61629f5d582e5518ccfe023c62d1fd26dd1870d`
(receipts `.ufo/waves/round-98/receipts/landing/`). These are disclosures, not amendments: no
predicate, counting command, kill rule, target or frozen mutant changes, and no reading is re-scored.

## B1 — C2's landing reading is UNMET (4 of 5): g11 read MET once under v6

`landing/c2-v6.txt` (09:08–09:14, counter and runner byte-identical to the instrument commit,
`landing/instr-identity.txt`): `C2 v6: forgeries refused 4 of 5; honest held 2 of 2; bound g2b MET`,
`C2-PREDICATE-UNMET`, rc 1. The world that read MET is g11-schedule-reader (seeded):
`R96C1 targets killed 11 of 11 …; honest CLEAN`. The pre-data reading at the instrument commit
(`receipts/c2-v6.txt`) and three seat readings at the freeze (CriticClaimR98, ReviewerCounterV6,
MutTesterCounterV6) read g11 refused. The kill rule says the claim is unmet when the landing reading is
not MET, so **C2 is an honest stop as frozen**; nothing below rescues it.

Mechanism (from the committed patch, `.ufo/waves/round-97/w1/ExecForgeryV5/g11-schedule-reader.patch`):
under v6 the world cannot read the seed or the counter source, so it falls back to a stateful guess — a
marker file `/dev/shm/.r97-g11-<work dir name>` makes the first run CLEAN and fakes a failure on every
later non-decoy run except indexes 0 and 48. The interior honest run reads CLEAN only if that marker is
missing when it runs. `/dev/shm` is shared host state outside every per-run directory (the v6 header's
disclosed bound); ExecForgeryV6 removed `/dev/shm/.r97-*` files while its own worlds ran during the
same window (`.ufo/waves/round-98/w1/ExecForgeryV6.md` § Risks), and MutTesterCounterV6 saw g11's kill
count vary (9 vs 11 of 11) on identical bytes. So g11's refusal under v6 rests on the honest bracket
plus an external marker another process can delete: the refusal is not robust to shared-state
interference. [INFERENCE: the deletion that let the interior honest run read CLEAN is the most likely
cause; no per-run trace was kept by the runner, so it is not proven.]

## B2 — C1 target t07 is observable-only, not verdict-bearing

CriticClaimR98 D1 (`probe_t07.py`): a directory `<lane>.round` gives `state_source` `none` honest vs
`stale` under t07, but `evaluate_dispatch_08` reads N/A both ways; only the conjunct detail changes.
The frozen header calls the nine "verdict-bearing"; eight are, t07 is observable-only — the class the
plan excluded by rule for m34. C1 is read as frozen (9 of 9); the substantive move is eight
verdict-bearing kills plus one observable-only kill. Routed into Q88's last sentence.

## B3 — new v6 forgery classes (ExecForgeryV6)

- g13 (reads REPO and REV from `/proc/<ppid>/cmdline`, `git show`s the committed reference) reads MET
  under v6 — the disclosed bound, now shown by a world.
- g15 (finds the lane by scanning the filesystem) reads MET under v6 — the disclosed bound.
- **g16 (reads the counter's own pristine export through `__file__`'s parents) reads MET under v6 and
  UNMET under v5** — rule 8 put the honest reference inside the work directory every run can reach.
  This is a v6-specific hole, not covered by the disclosed bounds as written. Minimal fix: keep the
  pristine export outside any path derivable from the per-run world (or unreadable to the child).
- g14 (reads `/proc/<ppid>/environ`) reads UNMET: the non-dumpable counter holds.

## B4 — the tip battery's floors gate times out under host load, at base and landing alike

`landing/tip-battery.txt`: `2 of 6` with `check_assertion_floors.py exit none wall 280.1s (timeout
after 280 s)`. Paired control under the same load (load average ≈ 35): `tip-battery-base-rerun1.txt`
(freeze `63cd48d9`) and `tip-battery-landing-rerun1.txt` both read `2 of 6` with the same timeout. The
extra red is host load acting on the flat 280 s cap (round-96 closure's routed item), not a landing
change; the red set is equal at base and landing under equal load.

## B5 — carried, not done this round

- The `dispatch_prompts` assertion floor stays 56 against 128 observed (CriticClaimR98 D2). Raising
  it is a three-artifact edit (`verifiers/floors-registry.json` plus both in-file tables of
  `verifiers/check_assertion_floors.py`, which the tip battery pins) and is routed to round 99.
- S273's non-reproducible whole-page digest (round-97 closure defect 7) is recorded forward only
  (CriticClaimR98 D6); the S273 row is unchanged.
- The ExecArmsR98 seat item described t02 with "file round 8"; the builder followed the round-97
  witness (a round-7 file), which is the only reading under which t02 can be killed. The arm's
  comment was clarified at landing (inside `self_test()`; no behaviour change; the landing readings
  are taken on those bytes).

## B6 — diagnostic re-read of C2 after WAVE-DONE (not the claim's reading)

With no wave seat running, the same command on the same landing revision read
`C2 v6: forgeries refused 5 of 5; honest held 2 of 2; bound g2b MET`, `C2-PREDICATE-MET` rc 0
(`.ufo/waves/round-98/receipts/landing/c2-v6-diagnostic-rerun.txt`). It is consistent with B1's
shared-marker mechanism and does not replace the landing reading: C2 stays an honest stop as frozen,
and the verdict belongs to the non-author closure.
