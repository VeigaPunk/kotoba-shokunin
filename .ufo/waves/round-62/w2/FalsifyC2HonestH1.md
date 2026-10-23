# FalsifyC2HonestH1 — H1 honest-tree verification + house-style/strawman attack

Seat: `L1kotoba62.FalsifyC2HonestH1` (leaf; no dispatch). Date: 2026-10-23.
Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. READ-ONLY honored: no lane file
written; all probes ran in `/tmp` (`/tmp/falsify_h1.py`, `/tmp/laneclone` sandbox clone,
`/tmp/v2old/`). No git/jj mutation in the lane (clone only under `/tmp`).

**Re-base notice.** The assignment pinned tip `e6da78bbe420722dd18a13182a7c4b64ce02f005`.
The lane advanced mid-flight to `f60590a1c95886aa54350b1c15e286baa8d5df42` (commits
`e424f2a`, `91fecae`, `f60590a` — a wave-2 falsification landing + hardening). The v2
verifier moved sha256 `de5e3471…` → `604ae4fb41779874eb420e8a904cb2ebdd953fa41dfc5f270ece53562b5c414d`,
and `C2-successor-measure.txt` was re-recorded at `receipt_rev=3f911504…`. I verified H1
against **both** v2 revisions: `de5e3471` bytes extracted at `e6da78b` into
`/tmp/v2_de5e3471.py`, and `604ae4fb` at the live tip. `diff` of the two revisions shows
the six `check_repairs` checks and the H1 fixture bytes are identical; only the
constants/lookup/invariance/CLI-dependency control arms were added. Frozen counter
`verifiers/check_routed_repairs.py` sha256 `95ade9be…` is unchanged.

## Verify H1 — REPRODUCED, exact

Commands run (all outputs observed, nothing assumed):

1. `python3 -B verifiers/check_routed_repairs_v2.py --self-test` at tip `f60590a`
   (hardened bytes `604ae4fb`): prints
   `frozen counter before: … ; H1 4 of 6; H2 tip 6 of 6` and
   `successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6`,
   `EXIT=0` — matches the live receipt `.ufo/waves/round-62/C2-successor-measure.txt`.
2. Byte-faithful run of the **frozen-predicate bytes** `de5e3471` on a sandbox clone
   (`git clone /tmp/laneclone`; the only modified file is the v2 file replaced by the
   `de5e3471` bytes so `LANE` resolves to real history): identical line,
   `H1 4 of 6`, `honest passed 2 of 2`, `EXIT=0` — matches the pre-hardening receipt
   verbatim (which named `receipt_rev=3e7aed9b`).
3. Fixture-blob reproduction independent of the self-test harness: the probe
   `exec`s the committed `h1 = make_fixture_blob_map(29)` … ancestry-assignment block
   out of the `de5e3471` source (and calls `honest_fixture_map()` on `604ae4fb`;
   the two maps are byte-identical across revisions), then calls
   `frozen.check_repairs(h1)` and `check_repairs(h1, fixture_tree_names(h1))`:

   ```
   frozen 4/6  (fails: R-c base-measure pointer; R-f controls-ancestry receipt)
   v2(de5e3471) 6/6   v2(604ae4fb) 6/6
   ```

   Frozen loses exactly R-c (pointers on two lines; frozen requires both names on one
   line) and R-f (`exit=0`; frozen requires the substring `exit 0`). R-a/R-b/R-d/R-e
   pass under both. The control receipt `controls/frozen-repairs-dishonest.txt`'s
   `frozen scores: [6,6,6,6,6,6,4]` and `H1 honest repairs in house style: 4 of 6`
   are confirmed by my own run (same vector).

4. G-a sanity: `git ls-tree -r --name-only 45a7ecfa… -- .ufo/waves/round-60/build` piped
   through the seat-name pattern prints **29**, matching `committed 29` in H1's LOG line.
   H1's census blob has ≥2 non-empty lines ending `exit=0` (v2 R-d wants a body — passes);
   its ancestry blob is `$ git merge-base --is-ancestor <two distinct 40-hex>` + `exit=0`
   (passes the owned-exit form). Nothing in H1 is dishonest: declared count exceeds the
   derived count, both pointers named with correct roles, real 40-hex pair, real
   exit marker. **H1 is genuinely honest** — the question is whether it is *house style*.

## Findings (by severity)

### HIGH — F1: H1's "house style" is a regex-shaped construct; the lane's actual R-c phrasing fails the successor

Measured, not inferred (`python3 -B -` heredoc importing `check_routed_repairs_v2`,
`604ae4fb`; identical on `de5e3471` — the regexes did not change):

- The lane's **own real R-c bullet** for this very erratum, in the committed round-62
  LOG (`LOG.md` L2558 at `f60590a`):
  `… is in `.ufo/waves/round-60/receipts/freeze2-selftest.txt`, **not** `.ufo/waves/round-60/C1-measure.txt` …`
  → `r_c_pointer_direction` = **False**. `freeze_pointer_asserted` = True but
  `c1_pointer_denied` = False: `C1_DENIED_RE` requires literal whitespace after
  `not` (`\b(?:not|…)\s+`), so the lane's idiomatic `**not**` markdown emphasis fails.
  The lane's own real phrasing of this repair would be **rejected** by the successor.
  (The r61 real bullet L2542 — bare `, NOT in \`…\`` — does pass: `r_c_pointer_direction`=True.
  So the pass region contains exactly the r61 wording and the fixture's, not the r62
  wording.) An honest repair written in the style the lane actually used this round
  scores 5/6.
- Mutation sweep on H1 (each variant honest — correct pointers, correct roles, real
  markers; scored under both v2 revisions, identical results):

  | variant | frozen | v2 | failing check |
  |---|---|---|---|
  | H1 as committed | 4 | 6 | — |
  | M-a: blank line between the two pointer lines (separate bullets) | 4 | **5** | v2 R-c (window is 2 lines) |
  | M-b: `receipts/freeze2-selftest.txt is the base measurement` (ref before "base") | 4 | **5** | v2 R-c (`base` must precede the ref within 180 chars) |
  | M-c: `C1-measure.txt records the after-run only.` (no literal `not`) | 4 | **5** | v2 R-c (denial required) |
  | M-d: `C1-measure.txt` never named | 4 | **5** | v2 R-c (denial required) |
  | M-e: same-line `…, not C1-measure.txt.` (bare name + sentence-final period) | 5 | **5** | v2 R-c — see F2 |
  | M-j: pointers 3 lines apart | 4 | **5** | v2 R-c (window is 2 lines) |
  | M-f: `$ git merge-base … # strict-ancestor test` (trailing comment) | 4 | **5** | v2 R-f (`ANCESTRY_COMMAND_RE` ends at the 2nd hash, `$` anchored) |
  | M-h: `exit=0 ` (trailing space) | 4 | 6 | — passes (EXIT_ZERO_RE tolerates trailing space) |

  Every honest variant that deviates from the fixture's exact shape is rejected.
  The "house style" attribute is overstated:

  - **Two-line pointer split is not an observed lane convention.** All 893 LOG.md
    bullets at tip are single-line (longest 1,943 chars); the real r61 and r62 R-c
    bullets are each one line. The split exists only as ExecC2Audit's hypothetical
    F3 "correct prose" false negative (`.ufo/waves/round-61/wave/ExecC2Audit.md`
    §3 F3, attempt FN-B) — the fixture writes exactly the shape the *successor's*
    2-line window accepts (adjacent lines, freeze first then denial on the next).
    Genuine F3-prose split by a blank line or a 3-line gap — equally "correct prose" —
    is rejected. H1 occupies the narrowest point of the successor's accept region.
  - **`exit=0` ancestry is a mixed-style choice.** `exit=0` is genuine house style for
    census files (`census-after/before` r61/r62, r47/48/59 census files) and the C2
    base control receipt (`base-exit=1`). But the **real r61 controls-ancestry receipt
    itself uses `exit 0`** (space, comment-prefixed `$ git merge-base …` line) — H1's
    `exit=0` is the census spelling transplanted onto an ancestry receipt, i.e. the
    hypothetical F2 shape, not the receipt's own style. (v2 accepts both, and the real
    receipt passes `r_f_owned_ancestry` — confirmed by direct call.)

  Corollary: the hardened v2 (`604ae4fb`) names this fixture `honest_fixture_map()`
  with docstring "the way the lane actually writes it" (`check_routed_repairs_v2.py:445-446`)
  — refuted by the evidence above: the lane writes R-c as a single bullet, and the
  lane's own `**not**` emphasis fails `C1_DENIED_RE`. The docstring asserts the
  house-style claim the fixture does not support.

  Verdict: H1 is honest but **strawman-shaped** — constructed to instantiate the
  frozen counter's two known false negatives while landing inside the successor's
  narrowest accept windows. It demonstrates `4→6` on one point of the honest space;
  it does not demonstrate that the successor accepts honest repairs generally
  (M-a/M-b/M-e/M-f/M-j and the real r62 bullet all fail). The claim's letter holds;
  its "house style" framing oversells the calibration evidence.

### MEDIUM — F2: `C1_DENIED_RE` fails on a sentence-final period after a bare filename

`not C1-measure.txt.` → no match (the `(?![\w.-])` lookahead counts `.` as a path
continuation); `not C1-measure.txt, …` → match. Denial detection depends on whether
the sentence ends with a comma or a period — and on backticks. Combined with F1's
`**not**` failure, the R-c denial arm is punctuation/typography-sensitive in ways
unrelated to honesty. (Dishonest D3 is still correctly rejected — this is a
false-negative brittleness, not a hole admitting dishonesty.)

### LOW — F3: plan/prose misdescribes the successor's R-c requirement

`plans/round-62.md` §C2 (and the assignment text) describe H1 as "asserted rather
than negated". Measured requirement is the opposite on the denial side: the
successor **requires** an explicit `not`-style denial of `C1-measure.txt`
(`c1_pointer_denied` must fire) — a negation-free honest pointer (M-c/M-d) is
rejected. "Asserted" applies only to the freeze-pointer half. The sentence the
predicate scores is *stricter* than the prose describes. Cosmetic in the plan,
but it is the same description other seats cite.

## Residual risk / gaps

- I did not re-run the six dishonest trees (owned by FalsifyC2Mutants/FalsifyC2RejectAll);
  their frozen=6 scores appear in my own run's `frozen counter before` line only as
  reproduced fixture scores for context.
- `census_is_regular` (the `git_regular_blob` arm) is only exercised via the CLI path;
  the H1 in-process path passes `True` by default — unprobed here (out of H1 scope).
- The H2 half of "honest passed 2 of 2" was confirmed only via the self-test runs
  above (tip CLI 6/6 at `45a7ecfa` and `3f911504`), which is the receipt's own method.

## Tooling

No installs needed or performed (python3 + git only). Pacman untouched (paused).
Probe artifacts: `/tmp/falsify_h1.py`, `/tmp/laneclone`, `/tmp/v2old`, `/tmp/v2_*.py`
— all outside the lane.

Report: `.ufo/waves/round-62/w2/FalsifyC2HonestH1.md`
