# CriticClaimR98 — falsification of the two frozen claims (round 98, wave r98-w1)

Seat: CriticClaimR98 (leaf critic; no subagent dispatch). Lane:
`/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Freeze/base:
`63cd48d9de2c44eb40691ca05d3a41cc2f9a3248`. Scratch clone:
`/fast/scratch/hyaku/kotoba-r98/CriticClaimR98/repo` (checked out at the freeze).

Status: **COMPLETE** — candidate built (`f297a4b4`, freeze + both patches); C1 MET under v6 and
v5; C2 v6 MET at the freeze; the v5 do-nothing and v6-as-v5 cause controls both reproduce
`refused 3 of 5` (g10/g11 MET); r97c1/r96c1/r95c1 MET; live run equal; census rc 0 with one new
W04.

## Readings

| reading | command | result |
|---|---|---|
| C2 v6 at the freeze | `forgery-controls.py v6 63cd48d9…` | `forgeries refused 5 of 5; honest held 2 of 2; bound g2b MET`, `C2-PREDICATE-MET`, rc 0 (receipt `c2-v6-freeze.txt`) |
| C2 v6-as-v5 cause control | `forgery-controls.py v6-as-v5 63cd48d9…` | g10/g11 read `R96C1-PREDICATE-MET` rc 0; `C2 v6-as-v5: forgeries refused 3 of 5; honest held 2 of 2; bound g2b MET`, `C2-PREDICATE-UNMET`, rc 1 (receipt `c2-v6-as-v5-freeze.txt`) — the refusal is rules 8–9 |
| C2 v5 do-nothing | `forgery-controls.py v5 63cd48d9…` | g3/g7/g8 refused, **g10 and g11 read `R96C1-PREDICATE-MET` rc 0**; `C2 v5: forgeries refused 3 of 5; honest held 2 of 2; bound g2b MET`, `C2-PREDICATE-UNMET`, rc 1 (receipt `c2-v5-freeze.txt`) — the pre-data receipt reproduces |
| instrument bytes | `git show 63cd48d9:…/selftest-kills.py \| sha256sum` | `2f31fe040c9e0ad7ae2fd87441531610e76c2ac48fa0789d5fb83519d205bd8f` = receipt |
| C2 runner bytes | `sha256sum verifiers/fixtures/round-98/forgery-controls.py` | `c4710da772f1c723f3c5449ca37da38a0886f42325e3cd8fe884c033c05c5fdc` = receipt |
| C1 at my candidate `f297a4b4` (v6) | `selftest-kills.py c1 f297a4b4 $D` | `C1 targets killed 9 of 9 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 9 of 9; code decoys held 9 of 9`, `C1-PREDICATE-MET`, rc 0 (receipt `c1-candidate-v6.txt`) |
| C1 at my candidate `f297a4b4` (v5) | same, `--rules v5` | identical tally, `C1-PREDICATE-MET`, rc 0 (receipt `c1-candidate-v5.txt`) — separability holds |
| C1 do-nothing | `selftest-kills.py c1 a33f262f <lane>` | `C1 targets killed 0 of 9`, `C1-PREDICATE-UNMET`, rc 1 (receipt `c1-donothing-freeze.txt`) — the pre-data receipt reproduces |
| r97c1 at the candidate | `selftest-kills.py r97c1 f297a4b4 $D` | `R97C1 targets killed 13 of 13 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 13 of 13; code decoys held 13 of 13`, `R97C1-PREDICATE-MET`, rc 0 (receipt `r97c1-candidate-v6.txt`) |
| census at the candidate | `sources-census.sh validate --file $D/corpus/SOURCES.md` | rc 0, **35 W04** (base 34; the new one is S277's duplicate URL) — receipt `census-candidate.txt` |
| r96c1 at the candidate | `selftest-kills.py r96c1 f297a4b4 $D` | `R96C1 targets killed 11 of 11 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 11 of 11; code decoys held 11 of 11`, `R96C1-PREDICATE-MET`, rc 0 (receipt `r96c1-candidate-v6.txt`) |
| r95c1 at the candidate | `selftest-kills.py r95c1 f297a4b4 $D` | `R95C1 targets killed 3 of 3 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 3 of 3; code decoys held 3 of 3`, `R95C1-PREDICATE-MET`, rc 0 (receipt `r95c1-candidate-v6.txt`) |
| candidate self-test | `python3 -B verifiers/verify_dispatch_prompts.py --self-test` | `0 failure(s) over 128 assertions`, rc 0 |
| candidate box proof | `python3 -B verifiers/verify_dispatch_prompts.py --box-proof` | `boxes proven 2`, rc 0 |
| live run base vs candidate | `--json` on both, fleet prompts | verdict/status/detail lines equal |
| S277 re-open | `curl -sS -L` docs.python.org/3/library/subprocess.html | 200, 208648 B, sha256 `86b575bf…65c5`, lines 881–883 carry the quoted clause verbatim (14 words) |
| S278 re-open | `curl -sS -L` git-scm.com/docs/git-archive | 200, 50116 B, sha256 `fc4bbcf…2d66`, lines 1708–1710 carry the quoted sentence verbatim — **23 words**, not the receipt's 22 |
| S279 re-open | `curl -sS -L` man7.org/…/proc_pid_environ.5.html | 200, 7747 B, sha256 `93394d9…2c46`, lines 90–91 carry the quoted clause verbatim — **14 words**, not the receipt's 15 |

The three access records reproduce exactly (HTTP code, byte count, sha256, line excerpt).

## C1 — mutant classification (own probe, `probe_verdicts.py` / `probe_t07.py` / `probe_proof.py`)

Behavioural probe on the freeze instrument: each frozen mutant is applied to a copy, both copies are
imported, and the production helpers are called on a fixture built for that mutant.

| target | honest | mutant | class |
|---|---|---|---|
| t01 lane-suffix-unanchored | `.bak` out of scope, `evaluated 0` | `.bak` evaluated, `evaluated 1` | verdict-bearing (evaluated set) |
| t02 dirs-first-only | `filename_report_dir_round_equal` **FAIL** | **PASS** | verdict-bearing (false green) |
| t03 verdict-first-file | `_verdict_of` finds the second file | `None` | verdict-bearing (proof lookup) |
| t04 proof-disposition-unenf | `box_proof` rc 1, `boxes proven 0` | rc 0, `boxes proven 2` | verdict-bearing (proof) |
| t05 proof-live-hash-unenf | `box_proof` rc 1, live-hash problem | rc 0, `boxes proven 2` | verdict-bearing (proof) |
| t06 fence-any-close | box map `{}` / box after the fence mis-assigned | box inside the fence hashed | verdict-bearing (box map) |
| t07 legacy-exists | `state_source` `none`; dispatch.08 **N/A** | `state_source` `stale`; dispatch.08 **N/A** | **reporting-only** (detail only) |
| t08 prompts-include-dirs | `evaluated 1` | `EnvError: Is a directory` | verdict-bearing (false red / crash) |
| t09 md-uppercase | `report_stem_is_lane_id` **FAIL** | **PASS** | verdict-bearing (false green) |

t07 changes the conjunct *detail* only: `round_le_latest_dispatched` is N/A under both `none` and
`stale`, and the file/check status is N/A both ways (probe `probe_t07.py`, no-baseline fixture with a
directory `kote.round`). It is the same class as m34, which the plan excludes by rule.

## C2 — reading and attack

- **v6 at the freeze reads MET** (own run, `c2-v6-freeze.txt`): g3/g7/g8/g10/g11 all
  `R96C1-PREDICATE-UNMET` rc 1; h1/h2 MET rc 0; g2b bound MET.
- **Cause control** (own run `c2-v6-as-v5-freeze.txt`; pre-data `c2-v6-as-v5.txt` agrees): refused
  3 of 5 (g10/g11 MET) — the refusal comes from rules 8–9, not from a table, marker or schedule
  change.
- **Do-nothing control** (own run `c2-v5-freeze.txt`; pre-data `c2-before-v5.txt` agrees): refused
  3 of 5 (g10/g11 MET), `C2-PREDICATE-UNMET` rc 1.
- **ExecForgeryV6 g13** (`g13-ppid-cmdline-ref.counter-v6.txt`): a forgery that reads
  `/proc/<ppid>/cmdline`, parses REV+REPO and `git show`s the committed reference reads
  `R96C1-PREDICATE-MET` rc 0 under v6. This is exactly the plan's disclosed bound ("/proc/<ppid>/cmdline
  … names the counter path, REV and REPO"); it is a disclosed finding, not a rescue.
- **ExecForgeryV6 g14** (`g14-ppid-environ-seed.counter-v6.txt`): the environ-seed forgery reads
  UNMET — rule 9's non-dumpable counter holds.

## Static findings

- **F-A (m32/m34 exclusion is honest).** `report_paths` consumers are `evaluate_dispatch_04`
  (`stems` set, `bad` detail order) and `evaluate_dispatch_08` (`dirs` set); no consumer reads
  list order into a status. `_finish`'s `fails[:12]` is detail-only. Excluding both by rule
  matches round-97 closure defect 6.
- **F-B (t07 is reporting-only in the box, like m34).** See the C1 table above. The plan calls the
  nine "verdict-bearing"; t07 (m27) is observable-only. This repeats routed defect 6's class for one
  of the nine.
- **F-C (C2 is pre-landed).** The v6 counter and the C2 runner are the instrument commit
  `a060b450` (after the round base `a33f262f`, before the freeze). No wave seat builds C2; the
  landing reading is a re-read of bytes that cannot change without failing the kill rule. The
  claim's delta is real against the round base (v5 → v6), but the wave cannot distinguish a
  do-nothing wave from a working one for C2.
- **F-D (separability holds for the rules, not for the table).** C1 under `--rules v5` uses the
  same new `CLAIMS["c1"]` table in the round-98 counter file; C1 therefore still depends on the
  instrument commit's table, not on rules 8–10. The plan's separability sentence is about rules
  8–10 only, which is accurate.
- **F-E (S279 over-attribution in the frozen plan).** The plan says proc_pid_environ(5) "grounds the
  non-dumpable counter". The page names the `PTRACE_MODE_READ_FSCREDS` check; it carries no denial
  sentence (`grep -i "dumpable\|EPERM\|EACCES\|errno"` → no match). The denial is ptrace(2) step (4),
  which the plan did not open. The scribe's S279 row and the scout's report correct the attribution;
  the frozen plan's sentence is not corrected (no addendum).
- **F-F (two receipt word counts are wrong).** S278: 22 recorded, 23 measured. S279: 15 recorded, 14
  measured. The scribe's rows carry the measured counts. The plan's `sources-opened.txt` keeps the
  wrong counts (frozen).
- **F-G (S277 duplicate URL → one new census W04).** S277 joins S263/S265 on the subprocess URL; the
  scribe's census reads `34 → 35` W04 and the READY discloses it. The scribe's item said "no new
  W04"; the frozen plan names S277, so the conflict is real and recorded, not hidden.
- **F-H (assertion floor carried).** `verifiers/floors-registry.json` still floors `dispatch_prompts`
  at 56 while the candidate observes 128 assertions. The plan carries the raise (round-97 routed
  defect 5); the floor does not guard the new arms.

## Verdicts

- **C1 as frozen: MET** on my own candidate build `f297a4b4` (freeze + ExecArmsR98.patch
  `27b412a5…` + ScribeCorpusR98.patch `6eae5cf2…`): 9 of 9 killed, positive 1 of 1, honest CLEAN,
  decoys 9 of 9, rc 0, under **both** v6 and v5. The do-nothing control reproduces 0 of 9, UNMET.
  The nine kills are behavioural (own probe: eight verdict/status-bearing, t07 detail-only).
- **C2 as frozen: MET** at the freeze (own run; the landing re-read is the same bytes unless the
  landing changes the instrument, which the kill rule forbids). The v5 do-nothing control reads
  `refused 3 of 5` (g10/g11 MET) and the v6-as-v5 cause control reads `refused 3 of 5` — the
  refusal comes from rules 8–9, and both pre-data receipts reproduce.
- **Candidate scope:** the diff is add-only (470 insertions, 0 deletions) across four files;
  `verify_dispatch_prompts.py` prefix (through `run_checks()`) and suffix (from `box_proof()`) are
  byte-identical to the freeze; both patches apply cleanly on a second fresh clone; the live
  dispatch run's verdict lines are equal to the base's; SKILL.md, the plan, the v6 counter, the C2
  runner, the v5 counter and the floors registry are byte-identical to the freeze.
- **No-harm deltas:** the census reads rc 0 with **35 W04** (base 34; D3); the assertion floor
  stays 56 against 128 observed (D2). Everything else in the plan's no-harm list is unchanged by
  the candidate (the gates, the tip battery red set, the round-96/95 pins).

## Defects

- **D1 (label, not predicate) — t07 is reporting-only.** `probe_t07.py`: a directory `<lane>.round`
  gives `state_source` `none` honest vs `stale` mutant, but `evaluate_dispatch_08` is **N/A** under
  both (`round_le_latest_dispatched` N/A, file verdict N/A, check status N/A; only the detail string
  changes). The plan and the frozen counter header call the nine "verdict-bearing"; t07 (m27) is the
  same class as m34, which the plan excludes by rule. The kill is legitimate and behavioural, and the
  frozen predicate (9 of 9) is met; the label is off by one and repeats round-97 closure defect 6.
  Smallest safe correction: the L1's landing report/lesson labels t07 observable-only (the plan and
  the counter header are frozen; no predicate change).
- **D2 (carried no-harm) — the assertion floor stays 56.** `verifiers/floors-registry.json` line 50
  `"floor": 56`; the candidate observes **128** assertions. The plan carries round-97 routed defect
  5's raise. The floor does not guard the 23 new arms. Smallest safe correction: the L1 raises the
  floor at the landing (an L1 no-harm act; the registry is not a wave seat's file).
- **D3 (disclosed census delta) — W04 34 → 35.** My census at the candidate: rc 0, **35 W04**; the
  new one is `S277 duplicate url docs.python.org/3/library/subprocess.html across scopes` (S263/S265
  already hold the URL). The scribe's seat item requires "no new W04"; the frozen plan names S277.
  The scribe wrote the row as the plan declares and recorded the conflict in the lesson; the READY
  states `W04 34->35`. Smallest safe correction: the L1 either accepts the W04 (and amends the
  no-harm line in the landing report) or issues `plans/round-98-addendum-*.md` folding S277 into
  S265 before the scored reading.
- **D4 (receipt counts) — S278 22 vs 23, S279 15 vs 14 words.** The scribe's rows carry the measured
  counts and the lesson's `§ Corrections C98-1/C98-2` are append-only; the frozen receipt keeps the
  wrong counts. Smallest safe correction: the L1 cites C98-1/C98-2 in the landing report.
- **D5 (source over-attribution) — S279 does not ground the non-dumpable denial.** The plan's C2
  "Sourced" line says proc_pid_environ(5) "grounds the non-dumpable counter"; the page names the
  `PTRACE_MODE_READ_FSCREDS` check and carries no denial sentence (`grep -i
  "dumpable\|EPERM\|EACCES\|errno"` → no match). The denial is ptrace(2) step (4), which the plan
  did not open. The scribe's S279 row and the scout's report correct the attribution; the frozen plan
  is not edited. Smallest safe correction: the L1 cites the scribe's bounded row and defers the
  ptrace(2) admit to the next round (the scout's judged-ADMIT).
- **D6 (routed defect 7 only forward-applied) — S273's row is unchanged.** The plan's item 7 says
  "this round's access records carry the HTTP code, size, sha256 AND a line excerpt"; S273's row
  still carries the non-reproducible whole-page sha256 and no excerpt (the scribe's patch appends
  S277–S280 only). The forward policy is honest; the old record remains unverifiable. Smallest safe
  correction: the L1 records S273's status (re-fetch with an excerpt, or mark the page dynamic).
- **D7 (frontier-step fix incomplete in the candidate) — the Q87 amendment row is not in the
  patches.** The plan's frontier step says the fix is "v6 rules 8–9 plus a Q87 amendment row"; the
  candidate patches touch only `verify_dispatch_prompts.py`, `corpus/SOURCES.md`,
  `corpus/lessons/round-98.md` and `corpus/README.md`. `corpus/QUALITY.md` Q87 is unchanged. The L1
  lands QUALITY at integration, so this is a landing requirement, not a candidate defect.

## Bounds and risks

- **g13 reads MET under v6 (disclosed bound).** `ExecForgeryV6/g13-ppid-cmdline-ref.counter-v6.txt`:
  a forgery that reads `/proc/<ppid>/cmdline`, parses REV+REPO and `git show`s the committed
  reference reads `R96C1-PREDICATE-MET` rc 0. This is exactly the plan's disclosed bound
  ("/proc/<ppid>/cmdline … names the counter path, REV and REPO"); it is a finding, not a rescue,
  and the C2 predicate is met as frozen. A complete close needs a filesystem sandbox or a different
  uid.
- **C2 is pre-landed (F-C).** The v6 counter and C2 runner are the instrument commit `a060b450`
  (after the round base `a33f262f`, before the freeze). The wave's C2 work is verification, not
  construction; the landing reading is a re-read of bytes that cannot change without failing the
  kill rule. The plan discloses the pre-data reading.
- **C1/C2 separability holds for rules 8–10.** C1 is MET under `--rules v5` as well as v6, so the
  arms do not depend on the new isolation rules. C1 still depends on the instrument commit's
  `CLAIMS["c1"]` table (the counter file), which is the measuring instrument, not the candidate.
- **t05 arm's SKILL.md-text dependency.** The arm rewrites the literal `"or unsubstituted\n"` in the
  proof tree's SKILL.md copy; a future SKILL.md edit that removes the string would make the honest
  self-test fail (the arm's first assertion expects rc 1). SKILL.md is frozen this round (600/600
  lines, no seat edits), so the risk is deferred, not live.
- **The g2b bound reads MET** under both v5 and v6 (the guard-aware code-object sniffer); the plan
  reports it, not scores it.
