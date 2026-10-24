# RevW2Intent — lineage audit: r64 C2 counter vs its r63 E2-hardened ancestor

role: revenger (wave-2 falsify, independent leaf; no subagent dispatch)
round: 64, wave 2, 2026-10-24
tip measured: `c019919c97ab5fe98e87a7754b4449ea4e699c99` (base `078eec4a1f6a41c64ff8806f58b46a67cd413bfc`)
question: is `verifiers/check_r64_routed_repairs.py` a genuine descendant of the
E2-hardened `verifiers/check_r63_routed_repairs.py`, or a cargo-cult copy — and
did any r63 arm lose its meaning in translation?
lane writes: this file only. All probes were `git show`/`git log` reads or
self-tests that build their own `/tmp` worlds. No tool installs or upgrades
(nothing needed beyond system `python3`/`git`); pacman pause not exercised.
lsp device unavailable in this seat's inventory — structural claims below cite
read line ranges on committed bytes, not semantic proof.

---

## 0. Re-run of the counting commands at the measured tip (this wave's duty)

```
$ python3 -B verifiers/check_r64_routed_repairs.py --rev c019919c97ab5fe98e87a7754b4449ea4e699c99
PASS seat-edit-committed    marker=True added-marker=True added-lines=82 (need >=60)
PASS control-revs-named     round-64 LOG line names committed controls 8c4cefa8 + cbbee56e and base 35d44b4b
PASS lowest-axis-corrected  round-64 LOG suffix names depth 9 < consistency 10 as lowest
PASS assertion-count-named  runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23; added patch line names 23 assertions
r63 routed defects closed 4 of 4
exit=0

$ python3 -B verifiers/check_r64_routed_repairs.py --rev 078eec4a1f6a41c64ff8806f58b46a67cd413bfc
… all four FAIL … r63 routed defects closed 0 of 4
the pinned do-nothing control at 078eec4a… is never a certification
exit=1

$ python3 -B verifiers/check_r64_routed_repairs.py --self-test
self-test: 0 failure(s) over 32 assertions
exit=0

$ python3 -B verifiers/check_r63_routed_repairs.py --self-test
self-test: 0 failure(s) over 23 assertions
exit=0
```

Both counters hold their frozen headlines at the measured tip. The r64
self-test's own transcripts (printed above the tally) are the kill matrix this
report reasons from:

```
label-only:      base rc=0 count=4 (want <4)      → killed by the base world
fingerprint:     look-alike rc=0 count=4 (want <4) → killed by the look-alike world
worktree-read:   target rc=1 count=3 (want rc=0)   → killed by the target world
hardcoded-count: substituted-source rc=0 count=4 (want <4) → killed
honest:          base rc=1 count=0; look-alike rc=1 count=3; target rc=0 count=4 → passes all
```

## 1. Structural diff of the two counters

| aspect | r63 `check_r63_routed_repairs.py` (E2-hardened) | r64 `check_r64_routed_repairs.py` |
|---|---|---|
| checks | 5: late-write-tracked, receipt-rev-named, entry-size-named, append-only, noharm-arms-named | 4: seat-edit-committed, control-revs-named, lowest-axis-corrected, assertion-count-named |
| suffix anchor | `_suffix_lines`: LOG bytes **appended after the pinned base prefix** (`log.startswith(base)`), the same prefix check 4 (append-only) proves | `_r64_suffix_lines`: lines **strictly after the first `## 2026-10-24 — Round 64` heading**, exact-or-header+space (a bare startswith that `Round 64b` would satisfy is rejected; parenthetical headings accepted) |
| token matching | `_tok_re`: non-hex boundaries | `_hash_token_re` (same) + `_number_token_re` (digit boundaries, sentence dots allowed) + `_matches_hash_prefix` (7–40 hex run that the **computed** hash startswith) |
| control rule | refuse iff `base_closed >= total` (only when ALL checks close at base); `rev == BASE_REV` refused; BASE_REV pinned in code; `--base-arm` CLI flag | refuse unless `base_closed == 0` exactly; `rev == BASE_REV` refused; BASE_REV pinned in code; **no** base CLI flag (`--base` exits 2, pinned by `_assert_argparse_rejects_base`) |
| dishonest counters | LABEL_ONLY_SRC, FINGERPRINT_SRC, M1_CHECK (worktree) — 3 process arms in one loop (2 sites × 3 arms) | LABEL_ONLY_SOURCE, FINGERPRINT_SOURCE, WORKTREE_CHECK_SOURCE, **HARDCODED_COUNT_CHECK_SOURCE** — 4 mutants, each audited over **all three worlds** in one repo, plus honest counter re-run per arm |
| worlds | three purpose-built world repos: base, **partial** (append with no measured values), target (committed then unlinked from disk); one specialized world per mutant | one world repo, worlds (base, look-alike = wrong-value suffix line, target with seat file unlinked); plus refuse arms: partial-base (repointed at the look-alike), green control, source-repointed BASE_REV; plus baseline-leak and Round-64b arms |
| self-test tally | 23 assertions (17 fixed + 2×3 loop) — **the r64 counter statically pins this exact shape** (`EXPECTED_STATIC_SHAPE = (17, 2, 3)`) | 32 assertions, no self-shape pin |
| in-file mutants | demonstrated in /tmp by the E2 seat (M-A stubs, M-B fingerprint), killed by the refuse rule / static tally | escalated to self-test arms: `_green_control_source` (all-green stubs → refuse) and `_replace_function` + hardcoded-count world |

## 2. Lineage table — what each r63 wave-2 falsification taught, and where it landed

| r63 w2 attack (seat) | Teaching | r64 defense | Verdict |
|---|---|---|---|
| Label-only counter certifies any rev incl. a garbage rev (RevCalibChecks F1 → ExecW2E2Patch RED-BEFORE 1; r63 arm 1) | A headline+exit predicate is satisfied by a counter that reads no bytes | LABEL_ONLY_SOURCE process arm + refuse-unless-base-0 + 40-hex `fullmatch` argparse | Genuine; r64 kills it at **two** layers (base arm and process arm) and adds `0 <= count < 4`, so a counter that prints no parseable headline can't sneak through as silent-failure |
| Fingerprint counter: 0-of-5 at base, 5-of-5 at tip (RED-BEFORE 2; r63 arm 2) | **The base conjunct alone does not kill fingerprint** — only a mid-score look-alike world separates honest from fingerprint | FINGERPRINT_SOURCE audited over base + **look-alike** (wrong committing rev in an otherwise complete token line) + target; killed at look-alike (`rc=0 count=4` vs honest `rc=1 count=3`) | Genuine and **upgraded**: r63's partial world lacked the measured values; r64's look-alike carries the complete token shape with one wrong value — strictly harder to reject, and the honest counter demonstrably rejects it |
| Worktree-read counter scores the file from disk (MutCalibInstrument M1 → RED-BEFORE 3; r63 M1_CHECK arm 3) | Commit the target, then remove it from the working tree; a counter reading `<rev>` and one reading the worktree diverge exactly there | WORKTREE_CHECK_SOURCE (replaces `check_seat_edit` with a `(root / SEAT_EDIT).read_text()` body); `(root / SEAT_EDIT).unlink()` before the arms; mutant mis-scores target (`rc=1 count=3`) while the honest counter certifies target from git bytes | Genuine — same mechanism, one check replaced, same unlink trick |
| M2/M5 survive the r63 self-test because the substitution hit the wrong side of the relation (MutW2C2Counter §4; receipt-token-swap + noharm-count-swap arms landed in r63) | The self-test must substitute **the side the check reads** | r64 check-4 arms substitute the *source* (`_r63_fixture_source(fixed_calls=18)` → true tally 24), the *patch receipt* (24), and a boundary case (23 inside 123); plus the in-file HARDCODED_COUNT mutant is killed exactly at the substituted-source world | Genuine — the wrong-side lesson generalized from receipt-vs-LOG to source-vs-receipt |
| Whole-LOG substring credit: base-line credit and mid-insert passes (RevW2SpecPrec (c); fix `_suffix_lines` landed) | Token checks must scan only the provably-new lines | `_r64_suffix_lines` — but re-anchored to the round-64 heading because the leak moved **into history**: `LOG.md:2576` at base already co-locates `8c4cefa`/`cbbee56`/`35d44b4b`, so any whole-LOG (or post-r63-heading) scan false-greens check 2 at base | Adapted translation, not a copy: same intent (new-lines-only credit), new anchor mechanism, plus arms r63 never needed — baseline-leak, parenthetical heading, Round-64b anti-collision |
| Missing token boundaries: `64` inside `b64d`, `1044` inside `ed41044b`, `36 of 38` inside `136 of 381` (RevW2SpecPrec (b); fix `_tok_re` landed) | Values need non-hex/non-digit boundaries | `_hash_token_re`/`_number_token_re`/`_matches_hash_prefix` + embedded-hash arm (`_embedded_hash` builds hex runs that must fail) + 23-in-123 arm | Genuine, and it fixes the mirror bug RevC2Checks named: r63's exact-token shape would reject a truthful **full** hash naming a short token; r64 accepts both full and ≥7-hex prefixes of the computed value |
| In-file all-green stubs (M-A) and in-file fingerprint (M-B) still certifying the tip (ExecW2E2Patch §2: "protection is two-sided") | The refuse rule kills stubs; the self-test kills in-file cheats; neither alone suffices | `_green_control_source` arm (green pinned control refuses certification) + `_replace_function` mutation mechanics + hardcoded-count world; static AST cross-check pins the r63 counter's arm shape (17,2,3) so a deleted r63 arm flips r64 check 4 red | Genuine; r64 escalated in-file mutation from a one-off /tmp demonstration to a standing self-test arm |
| Refuse rule `base_closed >= total` + BASE_REV pinned in code (r63 E2 patch) | No caller may point the control at a revision the counter would close | Strengthened to refuse unless `base_closed == 0` (RevC2Checks measured that vacuous token scans score **1 of 4** at base via the `LOG.md:2576` leak, satisfying both predicate conjuncts under the r63 rule) + partial-base arm + source-repointed-BASE_REV arm + `--base` CLI rejected (exit 2) | Genuine descendant with a **measured** strengthening, not a ritual copy |

r64-native (no r63 ancestor, none claimed): the check-1 60-line numstat floor
(kills a marker-only note — the F_LABEL "label-only tree" class of
MutW2C2Counter §6a, applied to check 1), the `## axes` section-bounded parse
with the Move-log table-collision arm, and check 4's static AST reconstruction —
which is a meta-arm: it pins the ancestor counter's own arm inventory, so
removing an r63 process arm breaks the r64 counter.

## 3. Orphans and lost-in-translation findings

**F1 (the orphan arm): append-only invariance was dropped, and the suffix
anchor silently weakened it.** r63 carried `check_append_only` as a check
(byte-prefix + growth, r63's own E1 added the growth conjunct because
"without the second conjunct the check is vacuous at the tip") and anchored
its suffix scan on that same proven prefix; its self-test carried the rewrite
arm ("a rewritten LOG fails the prefix conjunct", from r63 w2 F_RW). r64 has
no append-only check — append-only is not one of the four routed defects, and
the plan's bound names exactly those four — but `_r64_suffix_lines` anchors on
a **content marker, not an invariance proof**: nothing requires `LOG.md` at
`<rev>` to be a prefix-extension of the base LOG. A revision that rewrites the
round-64 entry in place, or rewrites an earlier entry to carry the round-64
heading plus credit lines, passes checks 2 and 3 unchanged. The r63 teaching
(RevW2SpecPrec probe `c-mid-insert`: "per-check credit never required
appending") was answered in r63 by keeping the append-only conjunct; in r64
the marker heading is movable and the lines after it rewriteable. This is the
one r63 arm that lost its meaning in translation. [INFERENCE on intent: the
drop is consistent with the declared four-defect bound, but the bound sentence
nowhere records that the "only new lines credit" property is now advisory —
and this wave's job is exactly to name where a held invariant quietly
downgraded.] Suggested disposition: one bound sentence in the round-64 report
("the r64 suffix is content-anchored, not append-anchored; a rewritten-entry
LOG is outside the counter's bound"), or a cheap prefix arm.

**F2 (coverage gap, wave-1 demanded arm not landed): the control-blob
base-substitution arm is missing.** RevC2Checks §check-2 required six
self-test arms; five landed (look-alike, one-sided, wrong rev, LOG-side
repinned base, empty derivation, full/short hash). The missing one: rewrite
the two **control files** at a constructed rev so they pin a different base
while the LOG still names `35d44b4b` — check 2 must fail via `_control_base`'s
computed intersection. The check body itself fails closed (intersection must
be exactly one hash and must start with `EXPECTED_PINNED_BASE_PREFIX`), so
this is self-test coverage, not soundness — but it is precisely the r63
MutW2C2Counter lesson ("substitute the side the check reads") applied to the
one input r64 never substitutes: the only `_write(root, CONTROL_PATHS[n], …)`
calls are in `_new_world` (source lines 560, 562; grep confirms no later
rewrite). The landed "wrong pinned base fails" arm substitutes only the LOG
side. Every other computed input of check 4 has a substitution arm; check 2's
derivation input has none.

**F3 (not an orphan): the r63 `--base-arm` CLI flag was removed, deliberately.**
The r64 base control runs inline on every invocation, and
`_assert_argparse_rejects_base` pins that no `--base` flag exists (exit 2 =
could-not-evaluate, never a certification). Removal is defended by an arm —
the opposite of cargo cult.

## 4. Verdict

Genuine descendant, not a cargo cult. All three r63 process arms
(label-only / fingerprint / worktree-read) survive with their killing worlds
intact or hardened; the r63 wave-2 teachings (look-alike worlds, wrong-side
substitution, scope+boundary token credit, in-code pinned control) each map to
a named r64 arm, and the r64 additions (refuse-unless-0, hardcoded-count
mutant, static shape pin, header anti-collision) answer attacks that postdate
r63's landing. Two residues, both this report's findings: **F1** — the
append-only invariance arm is gone and the content anchor is strictly weaker
(unnamed in the bound); **F2** — one wave-1-required substitution arm
(control-blob base pin) never landed. Both are candidates for the round-64
report's bound/Next line rather than predicate changes: the frozen C2
predicate holds at the measured tip exactly as declared (4 of 4 / 0 of 4, both
self-tests green).

Report: `.ufo/waves/round-64/w2/RevW2Intent.md`
