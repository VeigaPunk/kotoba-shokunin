# CriticC2Bound — C2 predicate, pin, four-check bound, and append-only harm

Role: independent critic; calibration review only. No admission/judgment, integration, production edit, git/jj write, or production verifier execution. Axes: **consistency/calibration** (predicate/provenance accuracy); **depth** only for the C1-versus-C2 routing distinction. No tool installs or upgrades.

Read first: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/plans/round-64.md`, frozen C2 at lines 89–161. Evidence also read in full: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_r63_routed_repairs.py` (651 lines) and `/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/lessons/round-63-verifier-spotcheck.md` (190 lines), including routed items 1–6 and the entire Lowest-axis parenthetical note.

Dependency boundary: the file-discovery tool found **no** `/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/*r64*` file, and the wave-1 report directory contained only `swarm-registry.json` on the reads used for this review. Thus the r64 counter and proposed LOG block were unavailable; the findings below distinguish frozen requirements, observed r63 implementation, and [INFERENCE] about the required r64 implementation. This is not a claim that an unfinished peer implementation failed a test. No wait on another seat was needed.

## 1. Constant headlines are blocked by the second conjunct; base-aware labels still meet the two-output predicate

**Counterexample and result.** Constructed and executed two scratch-only counters (complete source and exact outputs below). The unconditional counter prints `r63 routed defects closed 4 of 4`, exit 0 for every `--rev`, without reading any repository. It satisfies the first output conjunct but **does not satisfy the complete frozen two-conjunct predicate**: at the literal base it prints 4, not 0, and exits 0, not nonzero. Do not repeat the older, pre-E2 assertion that this exact unconditional shortcut satisfies the hardened predicate's letter.

The stronger counterexample special-cases only the literal base: print 0/exit 1 there; print 4/exit 0 everywhere else. It reads no evidence and meets **both output/exit conjuncts** at an unchanged old revision and the specified base. This falsifies sufficiency of the two printed outputs **alone**, not the complete C2 requirement that each check be computed from committed bytes. The plan separately requires computation at lines 120–145 and hardening at lines 153–157; the frozen command text itself does not run `--self-test`.

**Which arm kills which shortcut (observed r63 E2 model → required r64 analogue):**

| Shortcut | Actual r63 mechanism / exact source location | Required r64 discriminating world or arm |
|---|---|---|
| Always print the full headline | `LABEL_ONLY_SRC`, lines 217–228; process arm `("label-only", "base", ...)`, lines 574–585; auditor requires red base, lines 291–314 | Uncorrected committed base must reject the full headline and nonzero-exit mismatch. Also require the declared exact base count **0 of 4**, not merely `<4`. |
| Base-aware label, or "seat path exists + LOG changed means all repairs" fingerprint | `FINGERPRINT_SRC`, lines 230–258; partial world has tracked evidence + appended LOG but no measured correction, lines 395–413; process audit at lines 586–588 | A distinct, committed **partial** revision must remain red despite the seat marker and LOG growth. Run a base-aware label-only candidate against it too. A base/target pair alone does not kill this shortcut. |
| Read dirty worktree instead of `<rev>` | Dirty untracked-copy check at lines 442–446; target world commits the seat file then deletes its worktree copy, lines 399–416; worktree process arm at lines 578–591 | Dirty marker present only on disk must not close check 1; committed marker must still count after removing/changing the worktree copy. |
| Compare LOG with hardcoded measured values, never read their source | r63 entry-size shift, lines 506–511; LOG-side receipt token/count substitutions, lines 513–524; **source-side** token/count substitutions, lines 526–544; missing receipt, lines 481–486 | For r64: change each control file's creating commit independently while preserving LOG; change owned scores/ownership while preserving the axis correction; change r63 self-test tally while preserving the seat's number. Each relevant check must turn red. Add converse correction-side mismatches too. Porting r63's literal receipt paths would not test r64's different dependencies. |
| Count old LOG text, partial hex/number substrings, or a rewritten LOG | r63 `_suffix_lines` requires original LOG prefix, lines 171–176; `_tok_re` uses non-hex boundaries, lines 179–181; rewrite check at lines 488–497 | Old-prefix-only matches must not count; correct-looking values embedded in longer hex/numeric tokens must not count; rewriting one historical LOG byte then appending otherwise valid correction lines must reject. |

**Missing/uncertified arms.** No r64 implementation was available, so no r64 arm is certified present or killed here. In the **r63 self-test source**, the process classes are present, but there is no separately named base-aware-label candidate, no direct old-prefix-only/embedded-token negative assertion, and no forced-green `base_control` assertion. The r63 scan code implements prefix/boundary guards; that is not itself evidence those guards have discriminating self-test arms. The new counter needs actual adapted source-side substitution arms; “receipt-side” in a docstring is insufficient.

**Smallest safe disposition.** Fixable calibration defect: keep the frozen two-conjunct text, explicitly describe it as an output condition rather than a proof of computation; deliver the declared self-test/process receipts on the same committed counter bytes and include the partial-world/base-aware attack. Do not advertise finite arms as proof against an arbitrarily fixture-aware replacement program. No canonical verdict is offered here.

**Impacted claim/axis:** C2, consistency/calibration. C1 unaffected.

### Scratch source and observed output

`/tmp/kotoba-r64-CriticC2Bound-label-only.py`:

```python
#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--rev", required=True)
parser.add_argument("--root")
parser.parse_args()
print("r63 routed defects closed 4 of 4")
raise SystemExit(0)
```

`/tmp/kotoba-r64-CriticC2Bound-base-aware.py`:

```python
#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--rev", required=True)
parser.add_argument("--root")
args = parser.parse_args()
base = "078eec4a1f6a41c64ff8806f58b46a67cd413bfc"
closed = 0 if args.rev.lower() == base else 4
print("r63 routed defects closed %d of 4" % closed)
raise SystemExit(0 if closed == 4 else 1)
```

Executed as Python subprocesses from the tool; stdout and each subprocess's actual return code:

```text
$ python3 -B /tmp/kotoba-r64-CriticC2Bound-label-only.py --rev 38defdc58acc970810bc677da41f714f211713ac
r63 routed defects closed 4 of 4
EXIT=0
$ python3 -B /tmp/kotoba-r64-CriticC2Bound-label-only.py --rev 078eec4a1f6a41c64ff8806f58b46a67cd413bfc
r63 routed defects closed 4 of 4
EXIT=0
$ python3 -B /tmp/kotoba-r64-CriticC2Bound-base-aware.py --rev 38defdc58acc970810bc677da41f714f211713ac
r63 routed defects closed 4 of 4
EXIT=0
$ python3 -B /tmp/kotoba-r64-CriticC2Bound-base-aware.py --rev 078eec4a1f6a41c64ff8806f58b46a67cd413bfc
r63 routed defects closed 0 of 4
EXIT=1
```

The first revision is deliberately an old committed revision, not evidence of repairs. Neither program even opens it. No production counter/self-test was run.

## 2. Refuse-to-certify prevents a green control, not arbitrary source-pin relocation

**Observed mechanism.** In `/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_r63_routed_repairs.py`:

- Lines 77–82 set `BASE_REV_LITERAL = "35d44b4b4dcdda234b5dbff7af37e432fec55f05"`, `BASE_REV = BASE_REV_LITERAL`, and `R62_TIP = BASE_REV_LITERAL`.
- `base_control(root)` at lines 269–280 calls every check at **the current `BASE_REV`**, returning the number closed.
- `run()` at lines 323–328 refuses certification if `base_closed >= total`, returning 1 **before printing the summary headline**.
- Lines 330–335 additionally make measuring `BASE_REV` itself non-certifying even if its count were otherwise sufficient.
- The CLI at lines 614–644 exposes `--rev`, `--root`, `--self-test`, and `--base-arm`, **not a control-revision override**. `--base-arm` succeeds when `closed < total`, not only when `closed == 0`.

**Strongest counterexample from the code.** [INFERENCE] Moving `BASE_REV` to a repaired all-green revision triggers refusal as claimed. Moving it to **another red/partial revision** does not: the guard checks `<total`, not identity with the frozen literal, and not an exact zero. Source constants are editable; the guard follows the edited constant. It therefore cannot be cited as a mechanism that prevents *any later edit moving BASE_REV*. Neither a missing control object nor a partial score is automatically rejected by this numerical guard; individual checks must surface that failure, and the external exact base conjunct remains important.

**Smallest safe disposition.** Narrow the prose: “No CLI override; any all-green pinned control blocks certification.” Keep the original literal base in the independently replayed frozen conjunct and record the committed counter revision/hash that produced both receipts. That frozen plan/receipt identity is the authority for detecting pin drift; a second editable in-file constant is not an independent safeguard. Add a forced-green-base process arm that requires nonzero exit/refusal, so deleting the guard is detectable. A claim of immutable source pins would be an unsupported stronger claim, not a harmless wording variation.

**Impacted claim/axis:** C2, consistency/calibration (control identity and provenance). This is fixable without changing the four routed repairs or harming another axis.

## 3. Four C2 defect categories are the right bound; item 5 is real lane work but belongs to C1

**Full six-item crosswalk.** `/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/lessons/round-63-verifier-spotcheck.md:162–187`:

1. Uncommitted seat edit → C2 `seat-edit-committed`.
2. Two wrong control-file committing-revision citations → C2 `control-revs-named` (one routed category, two source revisions).
3. Incorrect lowest-axis parenthetical → C2 `lowest-axis-corrected`.
4. Stale seat assertion count (21 versus 23) → C2 `assertion-count-named`; the outside spot-check explicitly says the main report's 23 is correct.
5. **Deferred G7 pinning arms** → a further lane-owned action, but explicitly and prominently covered by **C1** at `/home/vgpnk/Projects/shokunin/kotoba-shokunin/plans/round-64.md:29–87`. It was not silently dropped or counted as a fifth C2 paperwork repair.
6. SHONEN promotion → explicitly **operator-owned**, not a lane-side repair; keep `[~]`, do not self-promote.

The complete **Lowest-axis** note (spot-check lines 174–177) says depth 9 is below consistency 10 and **“The rule is satisfied because C1 targets depth”**. It does not route a second, hidden lowest-axis violation. `/home/vgpnk/Projects/shokunin/kotoba-shokunin/SCORECARD.md:3–15,24–29` confirms lane ownership and the two scores; the plan at lines 6–12 correctly keeps stagnation dormant because depth is below 10. No saturation waiver follows from consistency reaching 10.

**Smallest safe disposition.** Bound C2 as **four routed paperwork/calibration defects**, not “all lane-side actions in the spot-check.” State item 5 is discharged under C1 and item 6 remains operator-owned. Under that crosswalk there is no fifth **omitted** lane-side repair in the six-item list. Saying “there were only four lane-side actions” would be inaccurate because item 5 is lane work. The incomplete Acta re-open in the discernment table is disclosed as an abstention, not a fifth routed repair.

**Impacted claims/axes:** supports C2's four-check scope and C1's separate depth obligation; consistency/calibration would be harmed by either omitting C1 or overstating the universe.

## 4. Appending the LOG block is safe; rewriting already-committed r63 prose is not

**Evidence and counterexample.** The actual r62 precedent is stronger than a net additions-only diff. `/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/lessons/round-62-verifier-spotcheck.md:45–52` records an in-place rewrite of already-committed **same-round** LOG bullets at `e424f2a4`, even though the overall base→tip LOG diff had 23 insertions and zero deletions. Lines 166–169 explicitly prefer appended corrections. Thus “no pre-round deletions” or “net additions only” does not establish append-only discipline at each commit boundary.

`/home/vgpnk/Projects/shokunin/kotoba-shokunin/LOG.md:2568–2576` supplies the safe r63 precedent: append a named correction block; then append **a correction to that block** saying the committed lines above stand, rather than editing the false clauses in place. The existing round-63 entry is at lines 2578–2588 and should remain byte-preserved.

The r63 code's `check_append_only()` at lines 153–162 requires prefix preservation **and growth**; `_suffix_lines()` at lines 171–176 rejects all suffix matches if the prefix is not preserved. [INFERENCE] Adapting `_suffix_lines()` to the literal r64 base makes rewriting any base LOG byte fail r64 checks 2–3 even if a valid-looking new correction block is appended. It does **not** detect editing a correction line that was first committed after that base while retaining the base prefix; the r62 incident shows why the writer must append again after each commit.

**Smallest safe disposition.** The L1 should append a clearly headed r64 erratum identifying the two r63 report statements it supersedes, including the correct committing revisions plus pinned base and depth 9/consistency 10. Do not edit the original r63 LOG entry or filed report parenthetical/citations in place. After any correction block has been committed, further corrections are new appended entries. Keep the one-byte historical rewrite + otherwise-valid-suffix negative arm from finding 1. The proposed LOG block was unavailable, so this review supports the append-only design, not a claim that a particular pending patch is safe.

**Impacted claim/axis:** C2, consistency/calibration and historical provenance. An in-place rewrite would be a real harm/trade, not a cosmetic cleanup the canonical judge should silently waive. An appended, explicitly superseding correction is the smallest no-trade fix.

## Handoff boundary

Only the four scratch subprocess runs above were exercised. Production self-tests, mutant kills, the r64 before/after measurements, and any LOG-prefix check remain **unrun by this critic**. Suggested main-agent evidence: exact 0-of-4 base/4-of-4 target receipts on pinned committed counter bytes; adapted per-source and process self-test receipts (especially partial/base-aware and forced-green control); preservation of the frozen-base LOG prefix and append-only commit discipline. No production patch is claimed or required from this read-only review.
