# ConnectorOverlapR100 — overlap scan and planning data-walk (round 100, wave r100-w1)

Seat: ConnectorOverlapR100 (connector, leaf — no subagent dispatch). **Read-only**: no repo writes.
Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Base `7b449a637c03d9b4c43a81b4df37cb38c2ea89ee`,
instrument `d1e1170d950fc378bb6a28bbfc5a62802669be86`, freeze `03a98eb78b63bf9895cbe00ba0f3c8b0e53aa687`.
Scratch: `/fast/scratch/hyaku/kotoba-r100/ConnectorOverlapR100` (TMPDIR/HYAKU_SCRATCH exported; removed before yield).

Method: read the two counters' headers in full, then read the four instruments' code paths the two
claims touch (`verify_dispatch_prompts.py`, `verify_skill_checklist.py`, `check_tip_battery.py`,
`check_assertion_floors.py`), and **measure** the couplings instead of inferring them: two self-test
runs, one delegation experiment in a scratch copy, one `git archive` export of the round-99 base, and
one read-only cross-lane scan that reuses kotoba's own `index_findings`.

---

## Part 1 — cross-claim overlap: does C1's change move any C2 reading, and vice versa?

### 1.1 The delegation edge that exists (and why it does not carry C1's change)

The checklist gate does delegate the dispatch boxes to the C1 file — measured, not inferred:

```
$ python3 -B verifiers/verify_skill_checklist.py --check checklist.box_map_complete
PASS checklist.box_map_complete: evaluated 45 — 45 boxes mapped (8 executed, 4 delegated, 33 unexecuted);
  delegated verifiers/verify_dispatch_prompts.py: --box-proof exit 0: boxes proven 2;
  delegated verifiers/verify_alwayson.py: --box-proof exit 0: boxes proven 2      rc=0
```

The edge, line by line:

| hop | file:line | text |
|---|---|---|
| map row | `verifiers/checklist-baseline.json:196`, `:220` | `"disposition": "delegated:verifiers/verify_dispatch_prompts.py"` (dispatch.04, dispatch.08) |
| gate runs the proof | `verifiers/verify_skill_checklist.py:1114` | `argv = cmd + [BOX_PROOF_FLAG]` |
| non-zero is red | `verifiers/verify_skill_checklist.py:1130-1136` | `if proc.returncode != 0:` → `problem` → `FAIL checklist.box_map_complete` |
| the instrument's dispatch | `verifiers/verify_dispatch_prompts.py:1963-1964` | `if args.self_test: return self_test()` |
| | `verifiers/verify_dispatch_prompts.py:1965-1968` | `if args.box_proof: … return box_proof(map_path, fixtures)` |

**C1's admitted region is `self_test()` (`verifiers/verify_dispatch_prompts.py:679-1794`), and
`main()` reaches it only under `--self-test` (`:1963`), never under `--box-proof` (`:1965`).**
`box_proof()` is a separate function at `:1796`. Therefore **C1's change cannot move the checklist
gate's delegated-proof reading**, which is the only place the two files meet at runtime.

### 1.2 Reading-by-reading table

C2 readings (`verifiers/fixtures/round-100/anchor-lists.py`):

| C2 conjunct | counter lines | touches C1's file? | why |
|---|---|---|---|
| `mismatches` (r01–r14 × 2 public paths) | `:230-246` | **no** | hermetic fixture world + the REV *checklist* module only; `check_governance_citations` / `check_citation_resolves` never import the dispatch instrument |
| `gate` (checklist, no args, fleet-shaped sandbox) | `:248-267` | **only through `--box-proof`** | see 1.1 — `self_test()` is not on that path |
| `selftest` (checklist `--self-test`, floor 1864) | `:269-275` | no | checklist module only |
| `kill` (revert `FIX_LINE`→`BASE_LINE`, on disk) | `:277-292` | no | checklist `strip_token_dressing`, `:1148` |
| `frozen` 1 (checklist confinement) | `:294-296` | no | checklist bytes |
| `frozen` 2 (battery outside `INSTRUMENT_PINS`) | `:297-303` | no | C1 does not touch `check_tip_battery.py` |
| `frozen` 3 (corpus instruments byte-identical) | `:304-310` | no | C1 does not touch them |
| `battery` | `:312-321` | **partially — and the counter does not read it** | see 1.3 |

C1 readings (`verifiers/fixtures/round-100/selftest-kills.py`, `CLAIMS["c1"]` at `:125-157`,
`"instrument": DP` at `:127`):

| C1 conjunct | touches C2's files? | why |
|---|---|---|
| `honest` (DP `--self-test`, 3 runs) | **no** | `grep -n "verify_skill_checklist\|check_tip_battery" verifiers/verify_dispatch_prompts.py` → **1 hit, a docstring** (`:286` "The normalisation mirrors verifiers/verify_skill_checklist.py"); the file never opens it |
| `targets` t01–t06 | **no** | every anchor is a DP line: `main()`'s not-a-directory return (`:1982-1984`), the `EnvError` return (`:1988-1994`), the `--json` payload (`:1979-1981`), `if not path.is_dir():` (`:1976`), `read_text`'s `encoding="utf-8"` (`:161`), `for cid in wanted:` (`:567`, inside `run_checks`) |
| `positive` p00 | no | DP `stem = stem[:-3]` |
| decoys (comment + code) | no | DP |
| kill rule's `--box-proof` → `boxes proven 2` (L1 check, not the counter) | no | reads `verifiers/checklist-baseline.json` + `SKILL.md`; C2 changes neither |

**Answer: no C2 reading changes under C1's patch; no C1 reading changes under C2's patch.** The
separability sentence in `plans/round-100.md` holds at the code level, and I could not construct a
path where it fails.

### 1.3 The one place they *do* share a process — and why it is inert

`check_assertion_floors.py` is battery gate 2 (`verifiers/check_tip_battery.py:185`) and it executes
**both** self-tests as children: `INSTRUMENTS["dispatch_prompts"]` (`check_assertion_floors.py:257`,
floor **56**) and `INSTRUMENTS["checklist"]` (`:247`, floor **1863**). So C1's new arms and C2's new
arms both run inside C2's `battery` measurement.

It is inert for three measured reasons:

1. **The C2 counter does not read the battery total.** `anchor-lists.py:314-317`:
   `gm = re.findall(r"guards (\d+) of (\d+)", out)` … `bat_ok = bool(gm) and gm[-1] == ("5","5") and ck_gate`,
   where `ck_gate` is only `^gate verifiers/verify_skill_checklist.py exit 0 `. Gates 1, 2, 4, 5 and 6
   may fail and C2 still reads MET. (This is the frozen predicate, not a defect: the plan's C2 sentence
   says "guards 5 of 5 and its checklist gate exits 0".)
2. **The battery's own guards never look at either claim's file.** `BATTERY`
   (`check_tip_battery.py:183-190`) is the six scripts; `verify_dispatch_prompts.py` is **not** one of
   them. `INSTRUMENT_PINS` (`:132-181`) has no key for it, and the "unpinned instrument" check
   (`:354-357`) iterates `scripts`, i.e. the six. So **C1 needs no battery pin**; C2 needs exactly the
   one admission the plan names for `verify_skill_checklist.py` (`:157-167`).
3. **Neither count is near a cap.** Measured at `03a98eb`:
   `verify_dispatch_prompts.py --self-test` → `0 failure(s) over 154 assertions` (0.07 s);
   `verify_skill_checklist.py --self-test` → `0 failure(s) over 1864 assertions` (0.23 s). The child
   cap is `child_timeout_s(360, load)` and the battery's per-gate cap is `GATE_TIMEOUT_S = 280`
   (`check_tip_battery.py:113`). No timeout risk from either patch.
   Instrument-size headroom at `03a98eb` versus the battery's `BASE = 072048fa`
   (`check_tip_battery.py:330-346`, `LINE_CAP = 900`): **added 644, deleted 66** — 256 added lines of
   room for C2's arm.

### 1.4 Two holes this scan found on the C1→C2 edge (findings, not claims)

**H1 — a `delegated:` box can silently stop being proven and the gate stays green.**
`supports_box_proof` (`verify_skill_checklist.py:1071-1092`) probes `--help` by **substring**; when the
flag is absent, `delegated_box_proof` returns a *note*, not a *problem* (`:1111-1113`), so
`check_box_map_complete` stays PASS. Demonstrated in a scratch copy of `verifiers/` + `SKILL.md`
(no lane writes):

```
# every literal "--box-proof" removed from verify_dispatch_prompts.py (docstring included)
PASS checklist.box_map_complete: evaluated 45 — 45 boxes mapped (8 executed, 4 delegated, 33 unexecuted);
  delegated verifiers/verify_dispatch_prompts.py: no --box-proof support
  (the --help probe does not advertise --box-proof), not run; …            rc=0
```

Two partial mutations did **not** skip silently — renaming the argparse flag while leaving the
docstring's `--box-proof` mentions kept the probe "supported" and then reddened the gate
(`failed its --box-proof (exit 2)`, rc 1). So the hole needs a patch that removes *every* mention,
which is exactly what a careless "delete the flag" cleanup does. This round the only guard is the
plan's kill rule ("production code of `verify_dispatch_prompts.py` outside `self_test()` changes" →
unmet). The **gate** does not hold it.

**H2 — the dispatch self-test's own arms are unpinned.** `check_assertion_floors.py:257` and
`verifiers/floors-registry.json` both carry floor **56**; the observed count is **154** at `03a98eb`
and was **128** at the round-99 base `52e8e95a` (measured from a `git archive` export in scratch:
`0 failure(s) over 128 assertions`). So **98 assertions can be deleted from the very surface C1
improves with every gate still green** — the r62 F17 class, and round 100's C1 *widens* it by however
many assertions it adds. This is Part 3 item 1.

### 1.5 Measured on the actual candidate (both delivered patches, in a scratch export)

Both builder patches existed when this seat ran, so the cross-claim question was measured on the real
combined tree (`git archive 03a98eb` → scratch, then `git apply` ExecAnchorR100.patch, then
ExecArmsR100.patch; both applied cleanly):

| reading | base `03a98eb` | C2 patch only (seat receipt) | **combined candidate** |
|---|---|---|---|
| `verify_dispatch_prompts.py --self-test` | `0 failure(s) over 154` | — | **`0 failure(s) over 168`** |
| `verify_skill_checklist.py --self-test` | `0 failure(s) over 1864` | `0 failure(s) over 1886` | **`0 failure(s) over 1886`** |
| `verify_dispatch_prompts.py --box-proof` | `boxes proven 2` rc 0 | — | **`boxes proven 2` rc 0** |
| checklist `checklist.box_map_complete` | `PASS … delegated … --box-proof exit 0: boxes proven 2` | — | **identical detail, rc 0** |
| frozen-anchor multiplicity (c1, r99c1, r98c1, r97c1, r96c1 + positives) | 1 each | — | **1 each, 0 problems** |

So C1's patch adds **14** assertions and C2's adds **22**, and neither moves the other's reading. The
checklist *gate* (no args) cannot be read from a flat export — it resolves `../.ufo/...` against the
tree's parent, so it reds on `trigger.citation_resolves` / `governance.citation_resolves` when the
export has no fleet-shaped sibling. That is a location artifact, not a candidate defect; the C2
counter's `gate` conjunct builds the fleet-shaped sandbox (`anchor-lists.py:248-267`) and the seat's
receipt reads `gate GREEN`. Anyone re-running the gate by hand from a scratch export will see the two
false reds and should use the counter instead.

---

## Part 2 — sibling lanes (read-only; cross-lane findings, no writes)

### 2.1 Copies or ports of `strip_token_dressing` / a `:\d+(-\d+)?$` line-anchor strip

Searched every `*-shokunin` lane for the function name and for the regex shape.

- **Live copies: exactly one, in this lane.** `kotoba-shokunin/verifiers/verify_skill_checklist.py:1144-1149`
  (`m = re.match(r"^(.+\.\w+):\d+(-\d+)?$", tok)` at `:1148`). No other lane has a `verifiers/`
  directory at all (`ls */verifiers/*.py` → only kotoba, 73 files), so no sibling ships a live gate
  with this defect.
- **Evidence-only copies** (wave receipts, mutants, probes — not gates, no shared red):
  `chousa-shokunin/.ufo/waves/round-63/w1/MutPre12/mutants/N01-g01-registry-absent-env.py:108`,
  `kaidoku-shokunin/.ufo/waves/round-41/w2/artifacts/R41W2Calib/tokens.py:33`,
  `kake-shokunin/.ufo/waves/round-93/c93_selfassess.py:168`,
  `kama-shokunin/.ufo/waves/round-43/frontier/sid-prototype.py:12`,
  `kumitate-shokunin/.ufo/waves/round-79/w1/K79ScoutOpen/refs-measure-v2.py:31`,
  `tameshi-shokunin/.ufo/evidence/round-43/calibration/measure.py:224`.
- **The defect class is live one file over, in this same lane, unclaimed by C2.**
  `kotoba-shokunin/verifiers/check_report_pointers.py:161`
  `LOCATOR_SUFFIX = re.compile(r":\d+(?:-\d+)?$")`, applied at `:315` in `classify_token`. Measured:

  ```
  classify_token("corpus/lessons/x.md:42")              -> ('tree', 'corpus/lessons/x.md')
  classify_token("corpus/lessons/x.md:42-45")           -> ('tree', 'corpus/lessons/x.md')
  classify_token("corpus/lessons/x.md:30,37")           -> ('tree', 'corpus/lessons/x.md:30,37')   # path does not exist
  classify_token("corpus/lessons/x.md:10,18,34,40-42")  -> ('tree', 'corpus/lessons/x.md:10,18,34,40-42')
  classify_token("LOG.md:1699,1908")                    -> None                                  # silently unchecked
  ```

  This is a SKILL.md gate (`SKILL.md:507`, `--report <path> … --round <N>`), so a kotoba report that
  cites `file.md:30,37` — the form SKILL.md itself uses (`S090 :10,18,34,40-42`) — either reads
  unresolved or is dropped. **Latent, not live**: `grep -E '`[^`]*\.(md|py|json|txt|sh|out):[0-9]+,[0-9]+'`
  over `.ufo/reports/round-9*/kotoba.md` finds none. Sibling lanes *do* write such pointers in their
  reports (`.ufo/reports/round-92/lore.md:201` `LOG.md:1699,1908,2256,2414`;
  `.ufo/reports/round-90/lore.md:334` `SHONEN.md:5,6,8,9`), so the class is real in the fleet.

### 2.2 Closure-landed spot-check lessons that leave a lane's corpus index red at the next round base

Method: for every lane whose `corpus/README.md` carries a `## Coverage map` section (19 of 21 lanes),
run kotoba's own `verify_corpus_integrity.index_findings` over that lane's `corpus/README.md` and its
`git ls-files corpus` set, and ask whether the lane's **most recent**
`corpus/lessons/round-N-verifier-spotcheck.md` is covered.

```
lane                      latest spot-check lesson                       verdict
audio-shokunin            lessons/round-101-verifier-spotcheck.md        UNINDEXED
chousa-shokunin           lessons/round-80-verifier-spotcheck.md         UNINDEXED
game-dev-2d-shokunin      lessons/round-105-verifier-spotcheck.md        UNINDEXED
game-dev-3d-shokunin      lessons/round-108-verifier-spotcheck.md        UNINDEXED
kagi-shokunin             lessons/round-45-verifier-spotcheck.md         UNINDEXED
kaidoku-shokunin          lessons/round-99-verifier-spotcheck.md         UNINDEXED
kake-shokunin             lessons/round-99-verifier-spotcheck.md         UNINDEXED
kama-shokunin             lessons/round-87-verifier-spotcheck.md         UNINDEXED
kasegi-shokunin           lessons/round-78-verifier-spotcheck.md         UNINDEXED
kengaku-shokunin          lessons/round-99-verifier-spotcheck.md         UNINDEXED
kotoba-shokunin           lessons/round-99-verifier-spotcheck.md         UNINDEXED  (measured red: unindexed=1)
kumitate-shokunin         lessons/round-91-verifier-spotcheck.md         UNINDEXED
lore-shokunin             lessons/round-103-verifier-spotcheck.md        UNINDEXED
mado-shokunin             lessons/round-87-verifier-spotcheck.md         covered — only by a `**` row
mori-shokunin             lessons/round-99-verifier-spotcheck.md         UNINDEXED
revenger-shokunin         lessons/round-99-verifier-spotcheck.md         UNINDEXED
tabi-shokunin             lessons/round-68-verifier-spotcheck.md         UNINDEXED
tameshi-shokunin          lessons/round-87-verifier-spotcheck.md         UNINDEXED
tsukuroi-shokunin         lessons/round-83-verifier-spotcheck.md         UNINDEXED
```

**18 of 19 read UNINDEXED.** kotoba is the only lane where this is a *measured gate red* today
(`receipts/c2-base.txt` / `corpus.index unindexed=1` for
`corpus/lessons/round-99-verifier-spotcheck.md`; the coverage map's last spot-check row is
`corpus/README.md:208`, round-98). `mado-shokunin` is "covered" only because its map carries a `**`
wildcard at `corpus/README.md:101`, which covers every tracked file and leaves 354 stale patterns —
a degenerate map, not an index.

Bound: the other lanes' gates are not kotoba's instrument (only kotoba has `verifiers/`), so for them
this is a **pattern** finding — the row is absent under kotoba's parser, and whether their own gate
reds is per-lane and unmeasured here. The kotoba instance is measured.

---

## Part 3 — what remains open after round 100 (each with a falsifiable before→after)

### 1. The dispatch self-test floor (the strongest item; C1 widens it)

- **Before:** `check_assertion_floors.py:257` `("verifiers/verify_dispatch_prompts.py", 56, …)` and
  `verifiers/floors-registry.json` (`dispatch_prompts: {floor: 56}`) against an observed **154**
  (`03a98eb`) and **168** with C1's patch applied (measured, §1.5) — **112 assertions deletable with
  `check_assertion_floors.py` still exiting 0**. Round-99 base `52e8e95a` observed 128, so round 99's
  C1 landing consumed 26 of its own headroom and round 100's C1 consumes 14 more.
- **After (round 101):** floor = the landed count (168 + whatever the reviewers require) in **both**
  in-file places and the registry, plus a new `check_assertion_floors.py` blob admitted in
  `check_tip_battery.py:132-181` (the pin is load-bearing: `FAIL guard instrument-pin` otherwise),
  plus the docstring's floor list. Then a control world that deletes **one** `rec(...)` arm from
  `verify_dispatch_prompts.py` prints `FAIL dispatch_prompts observed=<landed-1> floor=<landed>`,
  exit 1.
- **Do-nothing control:** that same arm-deleted tree at `03a98eb` prints
  `PASS dispatch_prompts observed=153 floor=56`, exit 0.
- **Same change, second surface — and it is exploitable today, measured:** the checklist floor is
  1863 against an observed 1886 (`check_assertion_floors.py:247`), so the C2 arms have a 23-assertion
  window. `MutTesterAnchorR100` part (b) walks through it: **A1** deletes the 11 governance arms and
  the self-test still reads `SURVIVED` at **1879** assertions while the counter reads MET (the `kill`
  conjunct only needs the trigger-side arms); **A2** (both red-token loops) survives at **1871**;
  **A3** (arms replaced by a source sniff) survives at **1865**. Bump the checklist floor in the same
  step (the C2 counter's own `SELFTEST_FLOOR = 1864` at `anchor-lists.py:88` is tighter but still
  below 1886, so it does not close A1 either — the counter's `selftest` conjunct is `n >= 1864`).
- **Why it cannot be done this round:** `verifiers/floors-registry.json` is frozen for every seat and
  `check_assertion_floors.py` is not in any seat's file ownership. It needs an L1-owned item.
- **Ordering:** take the floor **after** ExecArmsR100's arms land (154 → **168**, measured; 1864 →
  **1886** for the checklist), one bump, per the BUMP-IN-STEP rule in the registry's `$comment`.

### 2. The v7 kill counter for g11/g16 (carried from round 98 and 99)

- **Before:** `selftest-kills.py r96c1 <g16-work-pristine-ref world>` reads `R96C1-PREDICATE-MET`
  (rc 0) under v6 (`.ufo/waves/round-98/w1/ExecForgeryV6.md` F1/F2, receipts
  `g16-work-pristine-ref.counter-v6.txt`, `g13-ppid-cmdline-ref.counter-v6.txt`), and two readings of
  the same g11 world at one revision disagree because the refusal rests on a `/dev/shm` marker another
  process can delete (`corpus/lessons/round-99-verifier-spotcheck.md:88-89`).
- **After:** a v7 counter whose per-run scratch is private, whose out-of-scratch sweep is
  before/after, whose pristine tree is removed before the child starts, and whose child argv carries
  no REV/REPO reads `refused 1 of 1` twice on g11 and `refused 1 of 1` on g16/g13, while
  `forgeries refused 5 of 5; honest held 2 of 2` and `r96c1`/`r95c1`/`r97c1` stay MET.
- **Do-nothing control:** v6 at `03a98eb` reads MET on g16/g13 and disagrees on g11.
- Source: my predecessor's proposal, `.ufo/waves/round-99/w1/ConnectorOverlapR99.md:147-176`
  (Candidate A). Not re-measured here.

### 3. The C2 counter holes of round 99 (`carried-reds.py` v1 — not reused this round)

Four forged worlds read MET under v1 (`corpus/lessons/round-99-verifier-spotcheck.md:209-215`):
in-place governance rewrite; an unbound correction target; a correction row pinned to a pre-existing
line; a wildcard index row.

- **Before:** each of the four worlds, built after the freeze, reads `C2-PREDICATE-MET` under
  `carried-reds.py` v1.
- **After:** each reads `C2-PREDICATE-UNMET` with a named conjunct (in-place rewrite refused by a
  byte-identity conjunct on the governance files; unbound target refused by requiring the corrected
  token to resolve; pre-existing-line pin refused by a horizon conjunct; wildcard row refused by a
  no-glob conjunct), and the five frozen controls still read UNMET.
- **Do-nothing control:** v1 at the round-99 landing reads MET on all four (receipts
  `post-hoc-holes.txt`, cited at `:120`).

### 4. The delegation-skip hole (new; measured today — see H1)

- **Before:** with every `--box-proof` mention removed from `verify_dispatch_prompts.py`,
  `verify_skill_checklist.py --check checklist.box_map_complete` reads **PASS rc 0** and the detail
  says "no --box-proof support … not run" (measured, scratch copy).
- **After:** a map row whose disposition is `delegated:<target>` and whose instrument does not
  advertise `--box-proof` is a **FAIL naming the target**; a row with an `unexecuted:` disposition
  keeps today's PASS (that is the round-50 D2 behaviour the four existing arms assert). Control: the
  `NO_PROOF_STUB` arm in `verify_skill_checklist.py:2772-2777` must be re-pointed at an
  `unexecuted:` map row, not at a `delegated:` one.
- **Do-nothing control:** the measured PASS above, at `03a98eb`.

### 5. `check_report_pointers.py` comma anchors (new — see 2.1)

- **Before:** `classify_token("corpus/lessons/x.md:30,37")` → `('tree', 'corpus/lessons/x.md:30,37')`
  (unresolved) and `classify_token("LOG.md:1699,1908")` → `None` (silently unchecked).
- **After:** both classify as the path, and `classify_token("corpus/lessons/x.md:30,abc")` still reads
  unresolved (the negative control). The fix is the same shape as C2's, at
  `check_report_pointers.py:161`.
- **Do-nothing control:** the two measured tuples above.

### 6. Survivors the mutation seats find (both reports landed after the first draft)

**C1 — `w1/MutTesterDispatchR100.md` F1: 13 of 16 new mutants survive at the candidate.** The patch
moves none of them (`KILLED 3, SURVIVED 13, RUN-ERROR 0` at both revisions; honest CLEAN 3 of 3 at
154 and 168 assertions; decoys 16/16 both). The three kills (w10, w13, w14) come from round-99 arms;
the new `r100-t06`/`r100-t02` arms add incidental kill evidence only. Verdict-bearing survivors a
successor round can target, with the seat's own minimal-arm sketch:

| survivor | surface | before → after |
|---|---|---|
| w01-substrate-state-fleet-unchecked | `main()`'s three-entry substrate loop checks only `--prompts` | plain file as `--state-dir` → `PASS` rc 0 today; after an arm, rc 2 + `not a directory`, and the counter tally moves `killed 6 of 6` → `killed 7 of 7` |
| w03/w04/w05/w06/w07 | the `--json` payload (success `exit_code`, `na`/`pass`/`fail` counts, the EnvError `exit_code`) | payload fields unread today; after arms, a FAILing tree's payload asserts `exit_code == 1` and `fail == 1`, a mode-000 prompt's asserts `exit_code == 2` and a non-empty `error` |
| w09-readtext-errors-replace | `read_text`'s decode error mode (t05 closes the encoding, not the mode) | invalid UTF-8 returns `'caf\ufffd'` today; after an arm, `UnicodeDecodeError` propagates |
| w11/w12/w16 | parser defaults and `--check` choices (dead under the harness) | `--box-proof` with no `--map` reads `boxes proven 2` honest vs `cannot read the box map` mutant — real behaviour, unobserved |

w02 (message label), w08 (error text) and w15 (JSON key order) are output-only and stay excluded by
the round-97 no-verdict rule; w04/w05/w06 are payload-consumer verdict-bearing on the same rationale
that admitted m03.

**C2 — `w1/MutTesterAnchorR100.md`: three counter worlds read MET at the candidate, and the arms
cannot see their own weakening.**

- **F1 `w5-dynamic-pin` (new hole, medium):** the admitted `INSTRUMENT_PINS` entry written as a
  *computed* expression (sha1 of the file's bytes) reads `frozen 3 of 3` and `guards 5 of 5`, so the
  pin admits any checklist blob. Before → after: `anchor-lists.py <w5>` MET today; after requiring
  every element of every pin tuple to be an `ast.Constant` 40-hex string and the set difference from
  the base block to be exactly those literals, the same world reads UNMET (frozen).
- **F3 `w3b-blind-window-extra` (new hole, low-medium):** `SELFTEST_RE` deletes up to the next
  top-level `def `, so module-level code between `self_test`'s `return` and `def build_parser()` is
  invisible to `checklist_confined` while it executes at import. Before → after: a module-level
  `strip_token_dressing` lambda reads `confined=True`, `frozen 3 of 3`, MET today; after bounding the
  window with `ast.parse` + `node.end_lineno`, the same world reads UNMET (bytes outside).
- **F2 `w2-source-sniff-arm`:** MET, but this is the counter header's disclosed bound (the kill
  conjunct is on-disk only). The landed arm is behavioural, so the disclosure stays honest; no action.
- **Part (b) regex mutants:** 8 of 10 killed; R5 (`,\s*`) and R9 (`(,\d+(-\d+)?)*,?`) survive but are
  provably equivalent on the reachable surface (citation tokens are `\S+` splits; `rstrip` removes the
  trailing comma first). Named, not excused, and not worth a target.
- **Part (b) arm mutants (the floor item, measured):** A1 drops the 11 governance arms → self-test
  `SURVIVED` at **1879** assertions and the counter still reads MET; A2 drops both `red_tokens` loops →
  SURVIVED at **1871**; A3 replaces the arms with a source sniff → SURVIVED at **1865**. So the
  checklist's 22 new assertions have a **7-assertion window that is exploitable today**, because the
  `kill` conjunct only needs the trigger-side arms. This is Part 3 item 1's second surface, now with a
  witness: behind A1, a governance-only defect (`check_governance_citations` resolving comma tokens
  raw) survives. Before → after: A1's tree reads `self-test HELD` + `C2-PREDICATE-MET` today; with the
  checklist floor at the landed count (1886), the same tree reads `FAIL checklist observed=1879
  floor=1886`, and the C2 counter's `selftest` conjunct reads BROKEN.

`CriticClaimR100` owns the separability reading (single-patch candidates), so a successor round should
not re-claim it. `ExecArmsR100_READY` landed (patch sha256 `7b4e2dbc…`), and its candidate rev
`a2918960` reads `0 failure(s) over 168 assertions` — the same count this seat measured independently
in §1.5.

### 7. Closed by this round's plan (recorded so it is not re-carried)

- **S279 superseding row** (round-99 routed defect 2) → S285 `ptrace(2)` row, `plans/round-100.md`
  § Frontier step.
- **`strip_token_dressing` comma-anchor fix** (round-98/99 defect) → this round's C2.
- **Lesson pointer drift** (round-99 routed defect 1) → C100-1 in `corpus/lessons/round-100.md`,
  scribe-owned.

---

## The one bounded move (connector function)

**Synthesis: one floor bump holds both claims' new arms — and it is the only change that converts
either claim from "measured once by a counter" into "held by a gate every round".**

Measured state after both patches (section 1.5): the dispatch self-test is at **168** assertions
against a floor of **56** (`check_assertion_floors.py:257`, `floors-registry.json`), and the checklist
self-test is at **1886** against a floor of **1863** (`check_assertion_floors.py:247`) and a counter
floor of **1864** (`anchor-lists.py:88`). Both self-tests are children of battery gate 2
(`check_tip_battery.py:185`), so the battery already runs them every round — it just does not care how
much of them survives. A single change (two floor values in one file, the registry rows, the docstring
list, and one `check_assertion_floors.py` blob admitted in `check_tip_battery.py:132-181`) makes the
deletion of any one new arm a red gate for **both** surfaces at once, and it is the same change for
both, which is why it is a synthesis rather than two items.

- **Axes:** improves C1 depth *and* C2 consistency (both become gate-held, not counter-held) and harms
  neither: no claim's predicate reads the floors registry, and the C2 counter's `frozen` conjunct 2
  only requires the battery to be identical **outside** `INSTRUMENT_PINS`, which this change is.
- **Why it is the right move and not a bookkeeping one:** the window is not hypothetical. A1/A2/A3
  (`MutTesterAnchorR100` part (b)) delete 7, 15 and 21 assertions from the landed C2 arms and the
  *counter* still reads MET, because its `kill` conjunct only needs the trigger-side arms; and the
  dispatch window is 112 assertions wide. The floor is the only mechanism in the tree that makes an
  arm's deletion a red gate rather than a silent one.
- **Not available to any seat this round:** `verifiers/floors-registry.json` is frozen for every seat
  and `check_assertion_floors.py` is in no seat's file ownership. It needs an L1-owned item in round
  101, taken **after** the arms land (168 and 1886 are the post-landing counts) and in one step per
  the registry's BUMP-IN-STEP rule.
- **Verification:** delete one `rec(...)` arm from `verify_dispatch_prompts.py` in a scratch clone at
  the landing → `check_assertion_floors.py` must print `FAIL dispatch_prompts observed=167
  floor=168`, exit 1; the same tree at `03a98eb` prints `PASS dispatch_prompts observed=153 floor=56`,
  exit 0.

**A second move was proposed and is already implemented — recorded so it is not re-proposed.** I
intended to ask ExecAnchorR100 to carry the frozen truth table's negative rows (r10–r14) in the new
arm, because control **f1** (`receipts/c2-ctl-f1.txt`) shows a sloppy `:.*$` regex reading
`gate GREEN; self-test HELD` and being refused only by the counter's frozen tally. The delivered
patch already does this: its `red_tokens` are `missing.md:30,37`, `x.md:30,abc`, `x.md:30,,37`,
`x.md:,30` (r08, r10, r11, r13), and under `:.*$` the last three strip to `x.md` and resolve, so the
arm fails and the self-test reds. Residual: r12 (`x.md:5-`) and r14 (`x.md:abc`) are not asserted;
both would also discriminate under `:.*$`, but the three present tokens already carry the kill, so the
marginal value is low and the patch should not be reopened for it.

---

## Evidence (commands and the observed lines)

| # | command | observed |
|---|---|---|
| 1 | `python3 -B verifiers/verify_dispatch_prompts.py --self-test` | `0 failure(s) over 154 assertions`, 0.07 s |
| 2 | `python3 -B verifiers/verify_skill_checklist.py --self-test` | `0 failure(s) over 1864 assertions`, 0.23 s |
| 3 | `git archive 52e8e95a … \| tar -x -C $S/r99base && python3 -B verifiers/verify_dispatch_prompts.py --self-test` | `0 failure(s) over 128 assertions` |
| 4 | `python3 -B verifiers/verify_skill_checklist.py --check checklist.box_map_complete` | `PASS … 4 delegated … delegated verifiers/verify_dispatch_prompts.py: --box-proof exit 0: boxes proven 2`, rc 0 |
| 5 | `python3 -B verifiers/verify_dispatch_prompts.py --box-proof` | `boxes proven 2`, rc 0 |
| 6 | scratch copy, all `--box-proof` mentions removed from DP, then #4 | `PASS … no --box-proof support (…), not run`, rc 0 → **H1** |
| 7 | `git diff --numstat 072048fa 03a98eb -- <six battery scripts>` | added 98+166+210+170 = **644**, deleted 9+31+10+16 = **66** (cap 900) |
| 8 | `python3 -c` over `verifiers/floors-registry.json` | `checklist floor 1863`, `dispatch_prompts floor 56`, 19 rows |
| 9 | `classify_token(...)` over five comma tokens | `:30,37` and `:10,18,34,40-42` keep the anchor; `LOG.md:1699,1908` → `None` |
| 10 | cross-lane `index_findings` scan (19 lanes) | 18 UNINDEXED for the latest spot-check; kotoba `unindexed=1` |
| 11 | `grep -rn strip_token_dressing` across `*-shokunin` | one live hit, `kotoba-shokunin/verifiers/verify_skill_checklist.py:1144` |
| 12 | `grep -n "verify_skill_checklist\|check_tip_battery" verifiers/verify_dispatch_prompts.py` | 1 hit, docstring only (`:286`); no read, no import |
| 13 | `git archive 03a98eb \| tar -x` → `git apply` ExecAnchorR100.patch → `git apply` ExecArmsR100.patch | both applied cleanly |
| 14 | combined candidate: DP `--self-test` / checklist `--self-test` / DP `--box-proof` | `0 failure(s) over 168 assertions` / `0 failure(s) over 1886 assertions` / `boxes proven 2` rc 0 |
| 15 | anchor multiplicity over `CLAIMS[c1,r99c1,r98c1,r97c1,r96c1]` + positives, base and candidate | `anchor check: 0 problems` (every anchor exactly 1) |
| 16 | combined candidate: checklist `--check checklist.box_map_complete` | `PASS … delegated verifiers/verify_dispatch_prompts.py: --box-proof exit 0: boxes proven 2`, rc 0 |

## Risks / limits of this report

- Part 2's cross-lane index verdicts use **kotoba's** parser; sibling lanes have no `verifiers/`, so
  their own gates were not run. Only the kotoba instance is a measured gate red.
- Part 3 item 2 and item 3 are cited from committed round-98/99 evidence, not re-measured by this seat.
- Part 3 item 6 was first written as a status (the mutation seats had not reported); both reports
  landed before this seat finished and item 6 now carries their measured survivor lists. The §1.5
  candidate measurement used `ExecArmsR100.patch` as delivered at 12:38, whose sha256 matches the one
  in `ExecArmsR100_READY`.
- The checklist **gate** (no args) is not readable from a flat scratch export: `../.ufo/...` tokens
  resolve against the export's parent, so `trigger.citation_resolves` and
  `governance.citation_resolves` red for a reason unrelated to the candidate. The C2 counter's
  fleet-shaped sandbox is the correct measurement; §1.5 therefore reports the delegated-proof detail
  rather than the whole gate from the export.
- The H1 experiment mutated a **scratch copy** only; no lane file was written, and the scratch dir is
  removed before yield. The `full` export (344 MB) is also removed.
- Tooling: no installs, no upgrades, no pacman transaction (host pause respected).
