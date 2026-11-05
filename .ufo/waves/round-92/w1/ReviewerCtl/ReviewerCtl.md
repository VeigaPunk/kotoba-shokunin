# ReviewerCtl findings — /skill:godspeed (2026-11-05)

**Axes** (Godspeed): correctness of the candidate build, attack coverage with recorded rc/stdout, bound compliance, evidence quality — byte-level and cited.

**Log stream**: the mid-run transcript is approximate in ordering (parallel capture); the on-disk artifacts in this directory are the source of truth for every reading below. [INFERENCE where stream-order is cited.]

---

## Scope-integrity first

In-scope: candidate `af857a3588d908d91accba8158008c2a5209e4fc` (freeze `e073723ae667b64e534f8621bddb83ad12ad0e71` + `ExecCtlWorlds.patch`) built in my scratch clone; attacks (a)–(f) per the item; the old-control re-run (d) in a fresh clone; findings filed under `.ufo/waves/round-92/w1/ReviewerCtl/ReviewerCtl.md` only.

Out-of-scope and left untouched: `SKILL.md` (600/600 frozen), corpus spotcheck files, all frozen instruments (`check_r86_routed_repairs_v3.py`, `verify_corpus_integrity.py`, `corpus-baseline.json`, `check_gate_registry.py`, `verify_skill_checklist.py`), `verifiers/fixtures/round-91/` (byte-identical), the plan and controls docs, and the round-92 C1/C2 finished-state file ownership (ExecCtlWorlds/ExecKillPin/ExecLadderR92/ScribeCorpusR92). No edits were made by me to any of those paths. All commit-like operations I performed are scratch-clone commits under `/fast/scratch/hyaku/kotoba-r92/ReviewerCtl/` with identity `scratch <scratch@invalid>`, never in the lane, and only to name attack-world revisions.

Bounds kept: no `agent://all` broadcasts (message channel respected — though [INFERENCE from log stream: no DM was ultimately needed, so none was sent]); no host-wide risk surface touched; reports written only at `w1/ReviewerCtl/…`.

---

## R1 — HIGH — C2-shortcut refusal line does not byte-match the frozen §C1 predicate sentence

**Where**: `verifiers/fixtures/round-92/ctl-c2-capline-only-v2.sh` (line: `echo "C2-SHORTCUT-REFUSED: instrument-pin admission missing ($finding)"`, where `$finding` is the raw tip-battery `FAIL guard instrument-pin: …` sentence) vs `plans/round-92.md` §C1.

**Frozen predicate sentence (plan §C1)**: `C2-SHORTCUT-REFUSED: instrument-pin admission missing (blob <sha> unpinned; guards G of 5)`.

**Observed (e073723ae66… candidate, attack a run + solo reruns)**:
```
C2-SHORTCUT-REFUSED: instrument-pin admission missing (FAIL guard instrument-pin: verifiers/check_assertion_floors.py blob a189e61be79828fa856a1fdc900dcec10801a1af at <worldrev> is not a pinned blob)
```
Byte-level (`od -c`) verification shows the token `unpinned` is absent and the pattern `guards G of 5` is absent — the line interpolates the full `FAIL guard instrument-pin: <path> blob <sha> at <rev> is not a pinned blob` finding instead, with no guard-tally fragment.

**Impact**: the plan's per-script refusal-sentence wording is not byte-reproduced by the shipped control. §C1's frozen counting command's overall line (the one loaded into scores) **is** byte-exact (see R6), so the top-level predicate still resolves; the per-script sentence text is what reads off-key.

**Severity rationale**: the plan's §C1 predicate says "each refused world's stdout names its missing conjunct" — and it does name the pin admission — but its own quoted per-script sentence is not the printed one; a downstream byte-check against the plan text would flag this.

**Suggested disposition**: either (a) an L1 addendum to plans/round-92 §C1 replacing the quoted refusal sentence with the script's actual output pattern, or (b) a one-line edit to `ctl-c2-capline-only-v2.sh` interpolating `blob <sha> unpinned; guards <held> of 5` from the tip-battery output. I recommend (b) — the script can plausibly compose it from its captured `$out` (the `guards G of 5` fragment appears in the tip battery's `fleet root …; guards 4 of 5; …` line).

---

## R2 — MEDIUM — `ctl-c2-honest` in no-argument form resolves `HEAD` and fails opaque on anything but slot 0

**Where**: `verifiers/fixtures/round-92/ctl-c2-honest.sh` — `${1:-$(git -C "$LANE" rev-parse HEAD)}`.

**Observed**: running `ctl-c2-honest.sh` with no argument while my working clone was mid-attack (HEAD at forged world `4e62ab17c5c0…` from the repo — my fault, worth stating precisely) produced `C2-PREDICATE-UNMET: cap+admission conjunct rc=1; tip battery pin guard unread-or-failing rc=1` plus `admission conjunct: floors blob … in INSTRUMENT_PINS: False`. Re-running the identical world against the *candidate* state (`af857a35…` at HEAD) produced `C2-PREDICATE-MET` as expected. So the control is not wrong — it faithfully reflects HEAD — but the no-arg form's semantics (bind whatever HEAD is) work only when mutation state is paused. A safer default would be `rev-parse <candidate sha>` per §C1's own frozen base, or an explicit "no-arg binds slot 0" assertion. Not a defect in the byte-sense, but a fragile interface.

---

## R3 — MEDIUM — exit-code ladders of the v2 controls are structural, not byte-asserted

**Where**: `controls-run.sh`.

The runner uses `MET[i]` as counting state, driven by (loop condition) `rc == want` AND a `grep -qF -- "$named"` match on each step's output, i.e., a *counting* criterion, not a byte-exact per-script verdict check. Then:
- In the missing-script sub-check (`missing_run.log`), C2-honest rc=127 → met=no → observing `observed: shortcuts refused 2 of 2; honest held 1 of 2`, exit 1 — correctly refused, never "2 of 2".
- In the exit-2 sub-check (`exit2_run.log`, script body `exit 2`), C1-honest rc=2 → met=no → same observed line, exit 1.

So (f) PASSES for both scenarios: >2/2 requires exactly all four (rc==want AND locked-token-present) — missing and exit-2 cannot inflate it. **But**: the `met` logic is count-based and the per-world stdout is only echoed (always to stderr when running under `2>&1` as the log stream shows — the per-script receipts are not machine-diffed inside the runner). A future edit to one script's verdict sentence (e.g., the R1 mismatch) cannot break `2 of 2` **as long as** the grep host fragments (`C2-SHORTCUT-REFUSED: instrument-pin admission missing`, `C2-PREDICATE-MET`, `C1-SHORTCUT-REFUSED: rows committed and read; instrument cannot evaluate (rc 2)`, `C1-PREDICATE-MET`) stay byte-stable — those fragments ARE the grep anchors and they match the plan wording for three of the four cases. Only R1's spacing differs (trailing detail portion, not the anchor). Residual risk: LOW for the counting claim; R1 covers the wording finding.

---

## R4 — HIGH — stale-blob admission does NOT defeat the pin guard (attack c: refusal held)

**Commands + observations** (all runs logged in this directory):

1. Forge C (rev `4e62ab17c5c09eead1c0346cb2416aa60e15b539`): `check_assertion_floors.py` is the C-postimage (`SELF_TEST_TIMEOUT_S = 340`), `INSTRUMENT_PINS = {"verifiers/check_assertion_floors.py": (6 blobs, ending "…1111111111111111111111111111111111111111", "1e75039b2865d547a23de0dfdac31c6893ec449d")}` — i.e., the pins admission *contains* the stale freeze-base sha `6f2c52fb…` in its earlier-slot entries, and the actual postimage blob that the pin guard resolves at the rev is `1e75039b2865…`.
2. `python3 -B verifiers/check_tip_battery.py --rev 4e62ab17c5c09eead1c0346cb2416aa60e15b539` →
   `FAIL guard instrument-pin: verifiers/check_assertion_floors.py blob 1e75039b2865d547a23de0dfdac31c6893ec449d at 4e62ab17c5c09eead1c0346cb2416aa60e15b539 is not a pinned blob`, exit code 1 (`forgeC_tip.log`).
3. `ctl-c2-honest.sh 4e62ab17c5c09eead1c0346cb2416aa60e15b539` →
   `admission conjunct: floors blob 1e75039… in INSTRUMENT_PINS: False` … `C2-PREDICATE-UNMET: cap+admission conjunct rc=1; tip battery pin guard unread-or-failing rc=1`, script exit 1 (`forgeC_honest.log`).
4. Restored working-tree control check (unmodified candidate pins + candidate HEAD), `forgeC_tip_restore.log`: guard FAIL verdict identical on the same rev → the refusal was caused by the forge (stale-admission world), not by incidental working-tree state.

**Conclusion**: the pin guard refuses on blob equality against the pin set — the frozen §C1 mechanism — so a stale freeze-base sha in an *earlier tuple slot* does NOT launder the postimage into admission. Verdict: attack c REJECTED, predicate holds.

---

## R5 — HIGH — fabricated/claimed-but-absent admission does NOT pass the pin guard; C1-shortcut refused under the forged pin set (attack b: refusal held)

**Commands + observations** (all runs logged in this directory):

1. Forge B (rev `e70f61a99c92dcf7b21822aeff8b8d0bb5449ecf`): `check_assertion_floors.py` postimage with cap `SELF_TEST_TIMEOUT_S = 330`, `INSTRUMENT_PINS` admission set to `{6f2c52fb…, 1111111111111111111111111111111111111111}` — i.e., the fabricated sha `1111…` is claimed for the floors blob but the *real* postimage blob is `a189e61be79828fa856a1fdc900dcec10801a1af`.
2. `python3 -B verifiers/check_tip_battery.py --rev e70f61a99c92dcf7b21822aeff8b8d0bb5449ecf` →
   `FAIL guard instrument-pin: verifiers/check_assertion_floors.py blob a189e61be79828fa856a1fdc900dcec10801a1af at e70f61a… is not a pinned blob`, guard tally `guards 4 of 5`, exit 1 (`forgeB_tip.log`).
3. `bash verifiers/fixtures/round-92/ctl-c2-capline-only-v2.sh` (world ups a cap-only worlds copy on top of the forged pins) →
   `C2-SHORTCUT-REFUSED: instrument-pin admission missing (FAIL guard instrument-pin: … blob a189e61… is not a pinned blob)`, exit 1 (`forgeB_ctl.log`). *Note*: the embedded "world rev" of the scratch state inside this shell was `0bccec70…` (fresh date-dependent scratch sha; it contains the same 8-byte addressable content — the pin-set + cap state, not the candidate head).
4. Determinism cross-check: my world rev `0bccec708e54d…` (forge B, this directory reproduces our world copy byte-identically) vs builder `df50ddcc…` — the 8-byte addressable contents match (postimage `a189e61b…` with cap 330); only scratch stamp bytes differ. [INFERENCE from builder `probe.txt` correspondence of steps — see the `0bccec70…`/`df50ddcc…`/`16722316…` rev readings in this directory for provenance.]

**Conclusion**: attack b REJECTED — presence of a pin *entry* does not launder; the equality check of the actual rev blob against the admitted set is the mechanism the frozen predicate names, and it holds.

---

## R6 — attack (a) passed twice — `round-92 controls: shortcuts refused 2 of 2; honest held 2 of 2`, exit 0, byte-identical replay

**Command**: `HYAKU_SCRATCH=$S/hyaku-scratch TMPDIR=$S bash verifiers/fixtures/round-92/controls-run.sh` (candidate, twice: `candidate_run.log` and `candidate_run2.log`).

**Both runs**: `CRC=0`, all four steps `met=yes` (rc: C2-shortcut 1, C2-honest 0, C1-shortcut 1, C1-honest 0), counting line `round-92 controls: shortcuts refused 2 of 2; honest held 2 of 2` — `od -c` confirms it is byte-identical on the second run (`grep -c '^round-92 controls: shortcuts refused 2 of 2; honest held 2 of 2$' candidate_run2.log` = 1).

C2-shortcut reconcile against builder: builder probe.txt refusal line `C2-SHORTCUT-REFUSED: instrument-pin admission missing (FAIL guard instrument-pin: … blob a189e61be79828fa856a1fdc900dcec10801a1af at df50ddcc… is not a pinned blob)` and mine `… at 0bccec70… / at 16722316…` — differ mid-line by scratch-commit sha only; the 8-byte postimage and the verdict host fragment are identical. [INFERENCE: scratch stamp; all three revs' commits are filesystem-ephemeral.]

---

## R7 — attack (d) — old round-91 controls reproduce their frozen red-before receipts at the round-92 base

**Commands + observations** (this directory):

- Fresh clone `$D2` at base bytes (`e073723ae66…`), then `bash verifiers/fixtures/round-91/ctl-c2-capline-only.sh` →
  `SELF_TEST_TIMEOUT_S=360` / `C2-PREDICATE-MET` / exit 0 — matches redbefore receipt `.ufo/waves/round-92/receipts/redbefore-ctl-c2.txt` byte-for-behavior (`SELF_TEST_TIMEOUT_S=360`, `C2-PREDICATE-MET`, rc=0).
- `HYAKU_SCRATCH=$S/hyaku-scratch TMPDIR=$S bash verifiers/fixtures/round-91/ctl-c1-manifest-only.sh` →
  `G3 registry presence PASS: 1 SKILL.md line(s) name check_mutation_battery.py`
  `mutation battery killed 14 of 14 kill-set; equivalents survived 6 of 6; disclosed survivors 0 of 0`
  `C1-PREDICATE-UNMET` / exit 1 — matches redbefore receipt `.ufo/waves/round-92/receipts/redbefore-ctl-c1.txt` byte-for-behavior (rc=1).

**Conclusion**: round-91 controls' red-before state is unchanged at the round-92 base bytes (MET exit 0 / UNMET exit 1, as frozen). The red-before evidence remains valid; C1's targeted-fix motivation holds.

---

## R8 — attack (c), honest-control path — final acceptance reading at candidate

`ctl-c2-honest` on the candidate bytes: `admission conjunct: floors blob 6f2c52fb… in INSTRUMENT_PINS: True` + tip battery `guard instrument-pin PASS` → `C2-PREDICATE-MET`, exit 0. Consistent with §C1's honest-wrt-conjuncts design; C2-honest accepted the candidate state exactly when the pins admission equals the actual postimage blob at the rev (freeze base postimage `6f2c52fb…` is in the pin tuple — legitimate r91 admission — and matches the blob at HEAD). Fits R4's equality conclusion.

[INFERENCE from log-stream reordering — the R4/R5/R6 reads were intermingled in the stream; on-disk artifact per entry is the source of truth.]

---

## R9 — sentinel probe result (in passing) — `1111…` never resolves as a tip-battery rev

`python3 -B verifiers/check_tip_battery.py --rev 1111111111111111111111111111111111111111` →
`could-not-evaluate: cannot check out 1111111111111111111111111111111111111111 in the sandbox: fatal: unable to read tree (1111111111111111111111111111111111111111)`, exit 2 (`sentinel_tip.log`). The sentinel losing-sha candidate was rejected cheaply by the sandbox tree read, not wrongly accepted — corroborates R5's mechanism (pin-guard equality happens only after a rev is resolvable).

---

## R10 — MEDIUM — scratch shas are date-dependent and not byte-pinned (world-rev volatility)

Observations across runs of the same logical worlds (refusal-content identical modulo rev): my duplicated C2-shortcut runs cite world revs `0bccec708e54d…`, `16722316d46f25a…`; builder's own probe cites `df50ddcccb729e…`; the C1-honest battery logs show `killed 17 of 17` with 23-mutant/3-revision copy integrity — but the *scratch* world-revs differ from run to run purely from scratch-commit metadata. The runner's per-world "world rev <sha>" echo is the unstable part. This is [INFERENCE from the three revs' content-identical postimage + differing shas + G2's sha256-adopted copies]; the honest mechanism is scratch identity + always-fresh mktemp commit stamp bakes the rev text differently each time. Not a predicate violation — the tip-battery machine reads the *rev itself* — but the C1 WORLD-rev publication practice would benefit from a normalized tag (or content-only statement) in future probe receipts.

---

## R11 — LOW — backup-name cleanup side effects during sub-check (b)2)

During the missing-script sub-check I renamed `ctl-c2-honest.sh` → `ctl-c2-honest.sh.bak`, ran, then renamed back, but the `mv` restore and `echo restored-ok` used `$F.bak` in-place where `$F` was still the renamed state — the candidate working tree was momentarily showing `ctl-c2-honest.sh.bak` instead of `ctl-c2-honest.sh` (the listing in that transaction shows `.bak` present). Immediately cleaned up: `mv "$F.bak" "$F"` + `chmod +x` + `git checkout HEAD -- verifiers/fixtures/round-92/` → final state has all five scripts and `git status --porcelain` empty. Was MY working-tree fragility, not a candidate defect — but reporting for transparency since the item says runs happen "in YOUR clone" (they did; all damage was local scratch and cleaned up).

The exit-2 sub-check's `ctl-c1-honest.sh.orig` leftover also exists on disk next to the restored original — also cleaned up (`rm … .orig`, status clean). Both now fully restored (`ls repo/verifiers/fixtures/round-92/` shows exactly the five shipped scripts, no .bak/.orig).

---

## Residual risks, in severity order

1. **R1 (HIGH)**: one per-script refusal sentence does not byte-match its §C1 quoted text. Predicate intact via anchor-grep; wording is what reads off-key. Needs addendum or script recurrence fix (I suggest the script fix).
2. **R2 (MEDIUM)**: `ctl-c2-honest` no-arg binds HEAD, which is fragile mid-mutation. Not a scoring defect this round (scored runs operated on slot-0/baserev bytes); a robustness note for future rounds.
3. **R3 (resolved both ways)**: count-based met logic with byte anchors for three of four per-script verdict host-fragments; only R1's world-tip fragment is off. Cannot fake the count via missing/exit-2 scripts, and cannot inflate honest held (needs all four) — (f) attack REJECTED on the substance both ways.
4. **R10**: world-rev shas are scratch-stamp volatile; content-determinism was verified in R5/R6 by postimage comparison, but not automatable from the printed line alone.

Not finding-grade observations: my own typo'd python (`"floors preamble"`) and the accidental extra python invocations during forge-world construction left no residue on the lane; all corrected in-session and the affected files were re-forged from clean candidate state (`git status --porcelain` clean throughout).

---

## Files written in this lane by this seat

- `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-92/w1/ReviewerCtl/ReviewerCtl.md` (this report)
- `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-92/w1/ReviewerCtl/redbefore-ctl-c1.txt` / `redbefore-ctl-c2.txt` / `freeze-gate-r92.txt` (copies of the three referenced lane receipts)

Witness artifacts in this report directory (copied from the run area):

- `forgeB_tip.log`, `forgeB_ctl.log` — attack b
- `forgeC_tip.log`, `forgeC_honest.log`, `forgeC_tip_restore.log` — attack c
- `candidate_run.log`, `candidate_run2.log` — attack a (both runs)
- `missing_run.log`, `exit2_run.log` — attack f (rename, exit-2 sub-checks)
- `sentinel_tip.log` — R9
- `shortcutC2.log` — solo C2-shortcut rerun for line-level (e) verification

## R12 — MEDIUM — three receipts cited by the frozen plan are absent from the freeze commit tree

`git ls-tree --name-only e073723ae667b64e534f8621bddb83ad12ad0e71 -- .ufo/waves/round-92/receipts/` lists 20 files; absent are:

- `census-before.txt` — cited in plans/round-92.md § Frontier step ("receipt `.ufo/waves/round-92/receipts/census-before.txt`") and named in the wave dispatch's inventory of base receipts.
- `nowork-c1-controls.txt` — cited in plans/round-92.md § C1 do-nothing control ("receipt `.ufo/waves/round-92/receipts/nowork-c1-controls.txt`").
- `q73-sweep.txt` — cited in plans/round-92.md § Frozen-instrument risk ("receipts `q73-sweep.txt`"); only `q73-sweep-raw.txt` is committed.

Present and load-bearing for the C1 predicate: `redbefore-ctl-c1.txt` and `redbefore-ctl-c2.txt` ARE committed (verified), so the C1 red-before conjunct itself holds. The missing three are cited receipts for the do-nothing control, the census baseline and the risk-sweep; before anyone scores against them, the L1 should either land the receipts or amend the plan's citations. Nobody but the L1 may write those paths.

---

## No findings that block the candidate; scoring kept 10/9 held as planned

The counting predicate (the scored line) holds byte-exactly. The R1 wording defect in `ctl-c2-capline-only-v2.sh` is real and should be fixed via an addendum that amends the script (recurrence) or the plan (wording), but it does not weaken the C1 condition that both shortcut worlds are refused via the public gates over committed bytes.

— ReviewerCtl, 2026-11-05
