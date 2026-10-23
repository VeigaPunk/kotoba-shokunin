# RevClaimSeparation — kotoba round 62, wave 1 (`rev claim separation` seat)

Seat: `KotobaR62.RevClaimSeparation` (reviewer, leaf). Date: 2026-10-23.
Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin` (READ-ONLY to this seat; the only
write is this file). No dispatch, no subagent, no ask tool, no git/jj mutation, no lane
write. All evidence below is re-derived from committed bytes only; scratch
(`/fast/scratch/hyaku/kotoba-r62/RevClaimSeparation/`) is untrusted and is never cited as
evidence — the fenced commands/outputs here are the deliverable.

Task (verbatim): *Verify causal separability and before→after honesty of the two claims
before data. For C1: list the exact command(s) that verify it with C2 not landed (and vice
versa); confirm no shared file is required by both new instruments. For each claim,
re-derive the declared before value from committed bytes only: C1's `0 of 5` … and C2's
`frozen dishonest accepted 6 of 6; honest 1 of 2` (import the frozen function and score the
plan's D/H trees yourself). Paste commands/outputs. File any claim whose before value is not
re-derivable or whose after value depends on the other claim's files.*

---

## 0. Measurement context (ground)

- Lane tip at dispatch: `45a7ecfac9e203297f3146c45d63f5e79367470c` (round-62 plan + census
  before freeze). HEAD at review time: `a1cb8abc3911a5df3a2877915509118e384651a4`
  (round-62 wave-1 evidence commit `07c8167` + an integrator spot-check commit landed after
  dispatch). Both tips measured where noted.
- Frozen counters (bytes identical at `45a7ecf`, `a745411c`, and HEAD):
  - `verifiers/check_scoped_rules.py` sha256 `5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91` (r61 freeze; matches the plan's pin `5a5adc94…`).
  - `verifiers/check_routed_repairs.py` sha256 `95ade9be1ed1930266bce4b98c8c593fff1feba89e2cf25763f0aa83f206cb88` (r61 frozen six; never edited).
- Evidence paths are clean vs HEAD (`git --no-optional-locks status --porcelain` on
  `.ufo/waves/round-61`, `verifiers`, `plans`, `corpus` → only one untracked file,
  `verifiers/check_seat_counts.py`, which is **not** one of the four declared instruments, is
  not referenced by either claim, and is flagged in §6).
- The three new-instrument files are **absent** at review time (all three `test -f` →
  absent; `.ufo/waves/round-62/w1/ExecNoHarm62.md` and `ScoutRepairsApi.md` record the same
  absence earlier in the wave). This seat therefore verifies the verification commands'
  *contracts* (plan §C1/§C2 + wave-1 briefs, all committed bytes) and the before-values
  *empirically* against frozen bytes; the after-values are verified to be causally
  independent (no required file of either claim is read by the other).

---

## 1. C1 — before value `0 of 5` re-derived from committed bytes

**What the census counts.** Per erratum class of the matrix (E2, E2b, E2c, E2e, E2f): a
committed r61 receipt that measures the erratum's attack instances against the **landed**
counter (sha `5a5adc94…`) at arm level. The five classes and their r61 attack seats are
named in the r61 report (`/home/vgpnk/Projects/shokunin/.ufo/reports/round-61/kotoba.md:9`):
E2↔MutA3 (A3 `url_key`), E2b↔MutFixtures S1 (rendering alias), E2c↔MutA4 (A4 full-sha
alias), E2e↔MutA1 (guarded A1), E2f↔MutA2 (guarded A2; also r61 plan `plans/round-61.md:241`
E2f addendum).

**Canonical census commands and outputs** (committed bytes at HEAD; read-only):

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
$ git --no-optional-locks grep -l 5a5adc94 HEAD -- .ufo/waves/round-61
HEAD:.ufo/waves/round-61/C1-v3-measure.txt
HEAD:.ufo/waves/round-61/controls/C1-base.txt
HEAD:.ufo/waves/round-61/receipts/C1-worlds.txt
HEAD:.ufo/waves/round-61/wave/ExecCounterV3.md

$ git --no-optional-locks grep -nE "MutA1|MutA2|MutA3|MutA4|MutFixtures|E2b|E2c|E2e|E2f|erratum" HEAD -- .ufo/waves/round-61/receipts .ufo/waves/round-61/controls .ufo/waves/round-61/C1-v3-measure.txt
HEAD:.ufo/waves/round-61/receipts/C1-worlds.txt:7:# world definitions: in-counter self-test worlds W0-W7 (plans/round-61.md errata E2-E2e; synthetic per ExecCounterV3 5.8)

$ git --no-optional-locks grep -c 5a5adc94 HEAD -- .ufo/waves/round-61/wave/
HEAD:.ufo/waves/round-61/wave/ExecCounterV3.md:5

$ git --no-optional-locks grep -n E2f HEAD -- .ufo/waves/round-61 .ufo/reports plans/round-61.md
HEAD:.ufo/waves/round-61/wave/ExecReceiptsDesign.md:691:  E  ...    pre-data errata (E1..E2f) - already landed as lane commits;
HEAD:plans/round-61.md:241:### E2f addendum — A2 is the guarded form, with a declared bound (same pre-data window)
```

(date -u: 2026-10-23T21:02:30Z; census block exit 0.)

Additionally, the six attack-seat reports reference the **v2** counter sha
`ca2585a4…` (not the landed `5a5adc94…`): `grep -rl ca2585a4 .ufo/waves/round-61/wave/`
returns 24 files including `MutA1.md`, `MutA2.md`, `MutA3.md`, `MutA4.md`,
`MutFixtures.md`, `MutFixtureEscape.md`, `MutV2Regress.md`, `ExecSelftestArms.md`.
`5a5adc94` occurs in exactly one wave file, `ExecCounterV3.md` (the draft that became the
landed file; recorded runs are the identical self-test and the same 4-of-4/base commands,
not the five attack tables). The r61 report itself names the sha in prose provenance only
(`kotoba.md:9`, `:28`); no per-erratum arm-level result appears there.

**Per-erratum census table (this seat's derivation).**

| erratum | class | r61 seat | committed receipt measuring **landed** counter at arm level? |
|---|---|---|---|
| E2 | A3 `url_key` | MutA3 | no — MutA3 measured v2 bytes / draft predicate text (v2 sha in report); receipts/controls hit 0 |
| E2b | A3(b) rendering alias | MutFixtures S1 | no — MutFixtures scored v2's `action_conjunct`/draft; no E2b receipt hit |
| E2c | A4(iv) full-sha alias | MutA4 | no — MutA4 measured v2/draft and its alias-matrix receipt is scratch (never committed); no receipt hit |
| E2e | A1 guarded key form | MutA1 | no — MutA1 ran the v2 counter (`ca2585a4…`) over mutants; E2e receipt hit 0 |
| E2f | A2 guarded action | MutA2 / addendum | no — E2f appears only in `plans/round-61.md:241` (addendum prose) and `ExecReceiptsDesign.md:691` (prose); zero receipts |

Count: **0 of 5**. The only erratum-adjacent line anywhere in receipts/controls/measures is
`C1-worlds.txt:7` — a *provenance comment* that the world definitions derive from "errata
E2-E2e"; the receipt's results are keyed by world (W0–W7), not by erratum, they are the
counter's **own synthetic** self-test worlds (built by `ExecCounterV3`), not any seat's
attack instances, and no receipt contains a guard-disable (mutation) direction. Under the
plan's own definition ("per-erratum arm-level results … against the landed counter's arms
against the seat's attack classes"), the census is 0 of 5. **Before value re-derivable ✓.**

Nearest-miss note (honesty): `receipts/C1-worlds.txt` does contain world-keyed, arm-attributed
reject lines from the landed counter (e.g. `W2 … arm=A3 … rendering alias`). A reviewer who
read "per-erratum arm-level results" to include the counter's own self-test worlds would count
some E2/E2b/E2c/E2e classes as "measured". The claim's `0 of 5` is therefore *definition-
dependent*: it is correct for "per-erratum receipts measuring the seat attack classes with a
guard-disable direction", which is exactly how the matrix defines its own measurement (fresh
instances + guard mutation + control pairs). If the receipt had used per-erratum world ids and
run the guard-mutation direction, the ambiguity would not exist. **This is filed as a
definitional fragility, not a defect**: the absorption instrument itself (per its brief)
must fail closed on the guard-mutation direction, and its before-receipt must record the exact
census command + the definition.

**C1 verification commands, with C2 not landed** (from plan §C1 lines 29/79 + w1 briefs;
none of these commands reads any C2 file — see §4):

```
python3 -B verifiers/check_erratum_absorption.py --self-test
python3 -B verifiers/check_scoped_rules_v31.py --self-test
```

The C1 instrument imports only the pinned committed counter `verifiers/check_scoped_rules.py`
(importlib, sha asserted `5a5adc94…`; `w1-spec.json` ExecAbsorbInstrument brief) and the v31
successor is a self-contained copy of it. Neither references `check_routed_repairs*.py`.

---

## 2. C2 — before value re-derived from committed bytes (frozen function imported; plan D/H trees scored)

Method: the frozen counter was copied byte-for-byte from committed bytes
(`git show HEAD:verifiers/check_routed_repairs.py`, sha256 `95ade9be…` verified at
2026-10-23T20:58:55Z) into scratch; `check_repairs()` was imported in-process. Six D trees
were built exactly as declared by `plans/round-62.md` §C2 (D1 stale count, D2 negated
correction, D3 inverted R-c pointer, D4 bodyless census, D5 substring ids, D6 unowned-exit
ancestry), each dishonest in exactly its declared class and otherwise complete, using the
measured bypass shapes from the committed r61 `ExecC2Audit.md` catalogue (B2/B5/B6/B10/B11/B13)
so the trees are grounded in committed bytes, not invented. H1 is the same six repairs in the
lane's house style (`exit=0` in census/ancestry; R-c pointers split across two adjacent lines;
asserted, never negated). H2 is the measured tip tree via the lane CLI at both the dispatch
tip `45a7ecf` and HEAD `a1cb8ab`.

Scoring script: `/fast/scratch/hyaku/kotoba-r62/RevClaimSeparation/score_dh.py` (scratch;
untrusted, never cited as evidence — the outputs are the evidence).

```
$ python3 -B /fast/scratch/hyaku/kotoba-r62/RevClaimSeparation/score_dh.py
frozen counter bytes: /fast/scratch/hyaku/kotoba-r62/RevClaimSeparation/frozen_check_routed_repairs.py

== six dishonest trees under the FROZEN counter (check_repairs, in-process) ==
D1 stale count (tree-derived 30, line says 29): 6 of 6  ACCEPTED
D2 negated correction: 6 of 6  ACCEPTED
D3 inverted R-c pointer: 6 of 6  ACCEPTED
D4 bodyless census: 6 of 6  ACCEPTED
D5 substring ids (Q560/M910): 6 of 6  ACCEPTED
D6 unowned exit ancestry: 6 of 6  ACCEPTED

== honest trees under the FROZEN counter ==
H1 house-style six repairs: 4 of 6  FAILED (rejected by frozen counter)
    R-c base-measure pointer: missing      <- pointers split across two adjacent lines
    R-f controls-ancestry receipt: missing <- house-style "exit=0" vs frozen "exit 0"

H2 measured tip tree --rev 45a7ecfac9e2…: exit=0: routed repairs verified 6 of 6  passed
H2 measured tip tree --rev a1cb8abc3911…: exit=0: routed repairs verified 6 of 6  passed
base control --rev f3246d1493b6…: exit=1: routed repairs verified 0 of 6  (0 of 6 as declared)

=== RE-DERIVED BEFORE VALUE (frozen counter, committed bytes only) ===
frozen dishonest accepted 6 of 6; honest passed 1 of 2; base 0 of 6
plan §C2 declares:            frozen dishonest accepted 6 of 6; honest passed 1 of 2; base 0 of 6
```

(script exit 0; date -u: 2026-10-23T21:01:36Z.)

Findings:
- **Dishonest accepted 6 of 6** ✓ — every D tree scores 6 of 6 under the frozen counter
  (each is a vacuous substring/line pass; exactly the defect the successor must close).
- **Honest passed 1 of 2** ✓ — H1 scores 4 of 6 (R-c fails: split lines; R-f fails:
  `exit=0` house style ≠ frozen `exit 0`; why-lines shown), H2 scores 6 of 6 via the CLI at
  the tip. Counted once per the plan (probed at two tip revisions for robustness; both
  agree).
- **Base 0 of 6** ✓ — `--rev f3246d1493b60ea1c0d947a19c39f9e08e92f326` exits 1 with `0 of 6`.
- **Before value fully re-derivable from committed bytes ✓.** No claim value needed any
  uncommitted or other-claim file.

H2/tip caveat: "tip" is defined by the plan as the round-62 **data** revision; before data,
the repairs are already landed at the dispatch tip, so the before-phase H2 value (6 of 6,
exit 0) holds at `45a7ecf` and HEAD. The success `tip 6 of 6` will be re-measured at the data
revision; that is an after-value, not part of the declared before value.

---

## 3. Causal separability — C1 vs C2

**Required-file sets (from plan §C1/§C2 + wave-1 briefs; all committed bytes):**

| | C1 instruments | C2 instrument |
|---|---|---|
| new files | `verifiers/check_erratum_absorption.py`, `verifiers/check_scoped_rules_v31.py` | `verifiers/check_routed_repairs_v2.py` |
| reads (required) | `verifiers/check_scoped_rules.py` (pinned sha `5a5adc94…`) + its own inline instances/controls | `verifiers/check_routed_repairs.py` (frozen six, imported in-process) + git blobs of the measured rev: `LOG.md`, `corpus/QUALITY.md`, `corpus/lessons/round-61.md`, `.ufo/waves/round-61/census-after.txt`, `.ufo/waves/round-61/receipts/controls-ancestry.txt`, and `git ls-tree -- .ufo/waves/round-60/build` (G-a) |
| writes | `.ufo/waves/round-62/controls/absorption-{before,hollow}.txt` | `.ufo/waves/round-62/controls/frozen-repairs-dishonest.txt` |

**Intersection of required files: empty.** Neither claim's verification command reads any file
the other claim creates or modifies. The frozen counter each imports is a distinct file and
neither claim edits any frozen file (`check_scoped_rules.py` stays byte-identical per Q28;
`check_routed_repairs.py` stays byte-identical per the plan and `CriticE1Class.md`).

**Exact commands, with the other claim not landed:**
- C1 verifiable with C2 not landed: `python3 -B verifiers/check_erratum_absorption.py --self-test`
  and `python3 -B verifiers/check_scoped_rules_v31.py --self-test`. Neither reads/imports any
  `check_routed_repairs*.py` path (w1 briefs: absorption imports only `check_scoped_rules.py`;
  v31 is a copy of the scoped counter).
- C2 verifiable with C1 not landed: `python3 -B verifiers/check_routed_repairs_v2.py --self-test`
  (imports frozen `check_routed_repairs.py` only) plus the base/tip arms
  `python3 -B verifiers/check_routed_repairs.py --rev f3246d1493b60ea1c0d947a19c39f9e08e92f326`
  (exit 1, `0 of 6`) and `python3 -B verifiers/check_routed_repairs.py --rev <data tip>`
  (exit 0, `6 of 6`). None reads the absorption instrument, the v31 copy, or C1's controls.

**After-value independence.** The only shared object is the lane repo: both claims are measured
at the same (round-62 data) revision (commit-order step 5), and C2's CLI/`git` arms read repo
blobs. Checked for causal dependence of each after value on the other claim's *files*:
- C1's after (matrix line + v31 `worlds reject 7 of 7; eligible rows pass 4 of 4; survivors
  closed S of S`) depends only on C1 files + the frozen scoped counter; C2's files are never
  read.
- C2's after (`successor: …` + `tip 6 of 6`) reads the six blob paths listed above — all
  r61-owned. The round-62 data commit adds C1's files and the round-62 LOG entry; C1's LOG
  additions can only **add** substring matches to R-a/R-b/R-c (the frozen checks are presence
  tests), so they cannot flip a 6-of-6 tip to a lower score, and C1 writes nothing under
  `.ufo/waves/round-60/build` (G-a's count source). Hence C2's after value does not depend on
  C1's files, only on the shared revision. Co-timing is not coupling.
- The r62 no-harm battery (`verifiers` wave brief `ExecNoHarm62.md`) references **both** new
  instruments as optional self-test arms (skip-with-note when absent). That is a shared
  *reader* (a report-only no-harm arm), not a required file of either claim and not part of
  either frozen predicate; it does not create a dependency between the claims.

**Conclusion: no shared file is required by both new instruments; both before values are
re-derivable from committed bytes; neither after value depends on the other claim's files.**
No claim is filed on separability grounds.

---

## 4. Findings by severity

- **No HIGH findings.** Both declared before values re-derived exactly from committed bytes
  (C1: `0 of 5`; C2: `dishonest accepted 6 of 6; honest passed 1 of 2; base 0 of 6`);
  verification commands of each claim are disjoint from the other claim's files; the after
  values are causally independent.
- **MEDIUM-1 — C1 before-census definitional fragility (+ ambiguity in the plan).** The plan's
  "0 of 5" census is definition-dependent (see §1 nearest-miss): `receipts/C1-worlds.txt`
  contains landed-counter, arm-attributed, world-keyed rejects (with a provenance comment
  naming "errata E2-E2e") for the counter's own synthetic worlds. The census is correct under
  the plan's own definition (per-erratum receipts of the seat attack classes + guard-disable
  direction) — which is exactly what the absorption matrix implements — but the wording
  "per-erratum arm-level results" is ambiguous without that definition. **Action:** the
  `absorption-before.txt` receipt must record the exact census command AND a one-line
  definition ("per-erratum = fresh attack instances of the five mutation seats' classes,
  scored through the landed counter with a guard-disable direction"); the L1's report should
  cite that definition. Otherwise the before value is not robustly assertable.
- **MEDIUM-2 — C1 plan self-contradiction (already amended pre-data, still flagged).** The
  plan section §C1 frozen predicate `surviving 2` (line 35) vs its expected-result paragraph
  `surviving 1` (line 69) — lines 235–273 (erratum E1) already correct this pre-data: the
  counted after-line becomes computed `absorbed K of 5; surviving N` and ≥ two survivors are
  expected (E2c/E2e/E2f per addendum at lines 278–293). This seat confirms the amendment is
  pre-data and the frozen line in the plan still carries the contradiction; the data receipt
  must print the computed K/N. No data has run (matrices are drafts). Not a defect of the
  claim; it is a plan-text consistency item the L1 has already accepted an amendment for.
- **LOW-1 — untracked file `verifiers/check_seat_counts.py`** present in the lane working tree
  (untracked; not one of the four declared instruments; referenced by no brief). Flagged for
  the L1 to remove or commit deliberately; it does not affect either claim.
- **LOW-2 — `verifiers/__pycache__/check_routed_repairs.cpython-314.pyc`** exists (a peer
  import wrote it; `__pycache__/` is gitignored so the tree stays clean). No action needed;
  all future runs should use `python3 -B`.

---

## 5. Residual risk / verification gaps

- The three new instruments are not yet landed; the verification commands listed in §1/§3 are
  verified at **contract level** (plan + wave-1 briefs, committed bytes) plus the before-values
  empirically. The empirical "green with the other claim absent" runs can only be executed once
  the drafts land; the contracts contain no cross-import, so the gap is small.
- C2's `tip 6 of 6` after-value is only checkable at the data revision; its before-phase value
  is verified at dispatch tip and HEAD.
- The G-a self-derived count for the successor: this seat verified the frozen counter's reading
  paths, not the successor's G-a implementation (successor absent). The count source
  (`.ufo/waves/round-60/build`, pattern incl. `^(Conn|Critic|Exec|Mut|Review|Scout|Scribe|Sentinel|Src)[A-Za-z0-9]+\.md$`) is disjoint from C1's files; no coupling.
- I did not re-run the (live) `--fetch` arms; not needed for these two claims' before-values.

---

## 6. What this seat attacked / produced

Attacked: C1's declared `0 of 5` before census (re-derived from committed r61 bytes; census
commands + per-erratum table) and C2's declared `frozen dishonest accepted 6 of 6; honest
passed 1 of 2; base 0 of 6` (frozen `check_repairs` imported; plan D/H trees scored
in-process + tip/base CLI). Produced: separability proof (disjoint required-file sets, exact
verification command lists both directions, after-value independence). Findings: 0 high;
2 medium (C1 census definitional fragility; C1 plan line contradiction already amended
pre-data); 2 low (untracked `check_seat_counts.py`; pycache).

Installs: none (no tool inserted or updated; python3 only). Blockers: none.
