# FalsifyMatrixRerun — C1 counted predicate re-run + receipt attack (wave 2, falsify)

Seat: FalsifyMatrixRerun (kotoba round 62, hyaku run 5 attempt 2, wave 2). Date 2026-10-23.
Lane tip verified before work: `git rev-parse HEAD` → `e6da78bbe420722dd18a13182a7c4b64ce02f005`
(matches the assigned tip). Working tree clean for every file this seat attacks
(`git status --porcelain` on the instrument, counter and C1 receipt: empty).

Scope: re-run the C1 counted predicate, diff line-for-line against the committed receipt,
recompute `guard flips` and the survivor list independently, decide whether
`absorbed 2 of 5; surviving 6` is forced by the instance verdicts or can drift, and attack
the receipt's provenance (`receipt_rev 3e7aed9b…`, instrument sha `afb4ff74…`).

---

## 1. Fresh run at the tip (counted predicate, full stdout + exit)

Command (at the lane root):
`python3 -B verifiers/check_erratum_absorption.py --self-test; echo "exit=$?"`

```
counter sha256 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91
instances per direction: committed attacks 10; guard-disabled 10 per sweep (50 total); controls 4 committed + 4 disabled; content variant 2
guard flips: E2 2; E2b 2; E2c 0; E2e 0; E2f 0
errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2
survivor E2c e2c-wrong-supersedes-target: []
survivor E2c e2c-supersedes-with-fresh-fetch: []
survivor E2e e2e-negated-path-key: []
survivor E2e e2e-commented-equals-key: []
survivor E2f e2f-backticked-event-claim: []
survivor E2f e2f-compound-purpose-outside-citation: []
exit=0
```

stderr empty; 10 stdout lines (`wc -l`).

## 2. Line-for-line diff against the receipt

Command: `awk '/^\$ python3 -B verifiers\/check_erratum_absorption.py --self-test$/{f=1;next}
/^exit=/{f=0} f' .ufo/waves/round-62/C1-absorb-measure.txt > /tmp/absorb_receipt_block.txt &&
diff -u /tmp/absorb_receipt_block.txt /tmp/absorb_fresh_stdout.txt`

Result: **byte-identical** (diff exit 0, no output). The receipt's single `exit=0` line
matches the fresh exit 0 (`grep -c '^exit=0$'` → 1). A second fresh run the same session
diffed identical to the first (rerun exit=0) — deterministic, no hash-order nondeterminism
in the scoring path (ERRATA is a tuple; base dicts are single-entry).

The receipt's own arithmetic also checks: committed attacks 10 = 5 errata × 2 frozen
instances; guard-disabled 10 per sweep × 5 sweeps = 50; controls 4 committed + 4 disabled
= 2 seeded pairs × 2 instances × 2 directions; content variant 2 scorings.

## 3. Independent recompute of guard flips and the survivor list

I did not trust the instrument's `summarize()`: the probe at `/tmp/recompute_absorb.py`
loads the frozen catalogue (`ERRATA`) from the committed instrument, scores every instance
raw against the pinned counter, rescoring all classes under each guard patch, and does the
flips/absorbed/survivors/isolation/controls arithmetic itself (run via
`python3 -B /tmp/recompute_absorb.py`, exit 0):

```
baseline (True=rejected): E2 (T,T); E2b (T,T); E2c (F,F); E2e (F,F); E2f (F,F)
flips: E2 2; E2b 2; E2c 0; E2e 0; E2f 0
absorbed 2 of 5; surviving 6
survivors: E2c e2c-wrong-supersedes-target; E2c e2c-supersedes-with-fresh-fetch;
           E2e e2e-negated-path-key; E2e e2e-commented-equals-key;
           E2f e2f-backticked-event-claim; E2f e2f-compound-purpose-outside-citation
isolation ok: True   (no mutation changes another class's verdicts)
controls: absorbed-control before (T,T) after (F,F); surviving-control (F,F) both directions
```

Every printed number in the receipt is reproduced by independent arithmetic, in the same
order the receipt prints them (ERRATA order E2, E2b, E2c, E2e, E2f; survivors in catalogue
order within each class).

Source-level confirmation the six survivors are genuine (the landed counter really accepts
these, from `verifiers/check_scoped_rules.py`):
- **E2c** (`alias_sha_why` :1186-1199): `SUPERSEDES_RE = ^supersedes\s+(S\d{3,})\b` (:333)
  matches both teaches cells, so a sha already in the base table is waved through — the
  named S096 is never checked against the base row (S043) that actually holds the sha
  (condition 5), and the trailing `fetched 2026-10-23T12:00:00Z` is never inspected
  (condition 6). Both instances return `[]`.
- **E2e** (`path_site`/`scope_conjunct` :1043-1116): `KEY_SUFFIX_RE` (:397) accepts `=`,
  there is no negation clause (`Do not use paths: src/legacy/**/*.ts` scores a path-like
  value), and a leading `# ` comment is invisible to `key_occurrences`. `a1_conjunct`
  passes because `paths` is canonical for `Claude Code`. Both return `[]`.
- **E2f** (`action_conjunct` :1010-1040): `content_words` (:972) strips backticked spans
  *before* word extraction, so the invented `InstructionsLoaded` event token never reaches
  the page-support check (instance 1). Instance 2 passes the forward threshold exactly
  (`covered = 7` of 10 cell words vs `fwd_need(10) = 7`) and its compound-purpose words
  (`secretly`, `uploads`, `files`) are page-supported from the *unrelated section* the
  citation never names — no compound-purpose conjunct exists (G9). Both return `[]`.

## 4. Is `absorbed 2 of 5; surviving 6` forced by the instance verdicts, or can it drift?

**Forced, in the landed bytes.** The chain is closed:

1. `main()` prints `summary.absorbed` and `len(summary.survivors)` — the only source of
   those two numbers on the success path (`check_erratum_absorption.py:472-475`).
2. `summarize()` computes them solely from observed verdict lists: `absorbed` counts
   classes where all baseline reasons are non-empty **and** all guard-disabled reasons are
   empty; a survivor is appended for every baseline instance with an empty reason list.
   No constant feeds the line. The only literal `absorbed 2 of 5; surviving 6` in the file
   is `hollow_label_auditor()`'s decoy string, which is never printed and which
   `self_test` proves `summarize()` rejects with `MatrixFailure` (a str is not a
   `MatrixRun`) — so the printed line cannot be confused with, or replaced by, the decoy.
3. Therefore the counts cannot drift *from the verdicts*: change a verdict → the printed
   number changes with it, or a structural gate fires (exit 1). Verdict data is frozen:
   `validate_run` requires the exact frozen instance ids per class; the isolation loop in
   `summarize()` fails if any guard mutation changes another class's verdicts; the
   content-variant arm fails if relabelling the E2 URL (`…/b` → `…/a.md`, expected flip
   rejected→accepted) does not change the verdict — so a label/constant table keyed by
   instance id cannot score the arms; the label-scorer and reject-only arms must fail.
4. Exit code: 0 iff `measured == 5` and `controls == 2`. K/N are deliberately *not*
   exit-gated — that is the plan's E1 amendment item 1 (the fixed after-value is
   `errata measured 5 of 5; controls 2 of 2`, with K/N computed and every survivor
   printed). So "exit 0" alone never authenticates the counts; the counts are
   authenticated by re-running at the pinned bytes, which this seat did.

**The residual drift channel is mutation of the instrument's print path, not drift of the
verdicts.** A sibling wave-2 seat (F4, `.ufo/waves/round-62/w2/FalsifyMatrixMutants.md`,
recorded in `corpus/lessons/round-62.md` § Falsify corrections) already demonstrated that
a *mutated copy* can hardcode the headline above the computed survivor rows and still exit
0 — nothing parses the public stdout back against the Summary (Q48 class). I confirm that
bound from code reading: the exit gate does not check the printed headline. In the
pristine landed bytes no such hardcode exists on the print path, and my recompute
reproduces the headline from raw verdicts; the bound is a *tooling* bound (no committed
stdout-vs-summary checker), not a data defect in this receipt.

## 5. Provenance attack

Verified facts (all via read-only git at the lane):

- `git cat-file -t 3e7aed9b61bbfd83e0c800213b6dfc6da6191f85` → commit;
  `git merge-base --is-ancestor 3e7aed9b… HEAD` → ancestor of tip. ✓
- Instrument bytes at `3e7aed9b` = `afb4ff74c266803f4d6007407775a5c44387c84bf49b9ac1a9059d375178d56b`
  (`git show 3e7aed9b…:verifiers/check_erratum_absorption.py | sha256sum`) — equals the
  receipt's `instrument=` line, the working tree, and tip (`sha256sum` + clean status).
- Counter bytes at `3e7aed9b` and tip = `5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91`
  — equals the receipt's `counter=` line and the instrument's `COUNTER_SHA256` pin
  (double-checked in-process by `load_counter` hash + imported `self_sha()`).
- **Naming wrinkle: `receipt_rev=3e7aed9b…` does NOT carry the receipt.** `git show
  3e7aed9b…:.ufo/waves/round-62/C1-absorb-measure.txt` → "exists on disk, but not in
  …". The receipt first lands in `f9ab0812a574c369aa5cb94616e6ddffd1c5202b`
  (2026-10-23 18:22:43 -0300), the only commit that ever touched it, and is byte-identical
  from `f9ab0812` through tip (`sha256 e5a7d26795b4c1660400b4ef0d2f2d653a40de3745b4377332a16c13b521227b`
  at both; `git status` clean). So `receipt_rev` denotes the *measured code revision*,
  not the receipt's own commit. LOG.md:2548 says "Measured at `3e7aed9b`" — accurate for
  the code state, and the measured bytes never changed after it, but the header invites
  the misreading; see findings.
- Timeline is coherent and satisfies the strict controls-before-data order (E1 addendum 2):
  pre-data controls `9f03dcd7` 17:58:03 → E1 addendum 2 `9228be47` 17:58:17 → instrument +
  hollow control committed `3e7aed9b` 18:21:06 (= 21:21:06Z) → receipt's `date -u`
  2026-10-23T21:21:15Z (data run 9 s after the controls commit) → data receipt commit
  `f9ab0812` 21:22:43Z. The controls were run *and* committed before the data run.
- `controls/absorption-hollow.txt` (committed at tip, `sha256 5fcee82a…`, worktree ==
  tip): hollow variant exits 1 (`guard-mutation direction is missing…`), label variant
  exits 1 (`seeded controls did not classify…`), real path green — matching the
  in-instrument negative arms. Its `measured-at-branch-tip=9228be47…` is the E1-addendum-2
  commit, where `git ls-tree 9228be47 verifiers/` shows `check_erratum_absorption.py` **not
  yet committed** — the green-path arm ran against the working-tree draft 40 s before the
  data run and ~1 min before first commit. Honest (the receipt's own comment says the
  variants are /tmp copies "never in the lane", and the draft's sha is pinned in the same
  file), but it means the hollow receipt's green block is attested by the sha line, not by
  a commit containing the file at run time.

## 6. Findings

**Critical:** none. The counted predicate reproduces byte-identically at the assigned tip,
exit 0; every printed count is forced by independently recomputed instance verdicts; the
provenance chain (instrument sha, counter pin, receipt bytes, commit order) verifies.

**Major:** none.

**Minor / observations:**

1. `receipt_rev=3e7aed9b…` names a revision that does not contain the receipt file
   (receipt first lands at `f9ab0812`, 97 s later). The bytes are coherent — the named
   revision carries exactly the instrument/counter shas the receipt claims — but a reader
   who interprets `receipt_rev` as "the commit carrying this receipt" hits a hard error.
   Suggest a one-line header comment (`receipt_rev = code revision measured; receipt
   committed at <f9ab0812>`). No data defect.
2. The instrument pins the counter bytes twice and fails closed (exit 2) on mismatch, but
   has **no self-pin**: a mutated instrument cannot fail closed on its own bytes, and the
   exit code does not gate the printed K/N (by E1 design). Combined with sibling F4 (no
   stdout↔Summary binding), the headline is authenticated only by re-running the
   sha-pinned bytes — which is exactly what this seat did, and what the receipt + git
   history support. Residual tooling bound, already named by F4; nothing new to fix in
   the data.
3. `guard flips` is gated by `if all(before.reasons) else 0` and counts only an erratum's
   own instances under its own patch; a hypothetical mixed-baseline class would print
   flips 0, be counted in neither absorbed nor survivors, and its rejected instance's
   reasons would never be printed (baseline reject reasons are not printed per-instance —
   only survivors' empty lists are). Latent reporting blind spot only; all five classes
   here are uniform (2/2 rejected or 2/2 accepted), so nothing is hidden in this receipt.
4. The hollow-control receipt's green-path run executed pre-commit against the uncommitted
   draft (tip `9228be47` lacks the file). Bound by the sha line in the same receipt;
   recorded here so the ordering is not later misread as "ran from a committed gate".

## 7. Residual risk and verification gaps

- I re-ran and attacked only the C1 matrix receipt. The v3.1 successor gate
  (`check_scoped_rules_v31.py`, `survivors closed 5 of 6`) and the C2 successor receipt
  belong to sibling seats; not re-run here.
- Sibling F5's hash-then-import TOCTOU on the counter pin stands as a named bound; my
  reads confirm `load_counter` hashes, imports, then re-hashes via the module's own
  `self_sha()` — consistent with F5, no independent exploit attempted.
- `check_content_variant` asserts exactly one catalogue variant exists
  (`require(len(variants) == 1)`); if a future class adds a variant the instrument fails
  closed rather than misreporting — acceptable, noted for maintainers.
- The probe at `/tmp/recompute_absorb.py` reuses the instrument's catalogue and
  `patched()` (the frozen instance definitions are the object under audit); only the
  summary arithmetic was re-derived independently. A fully independent instance
  reconstruction would duplicate the ERRATA bytes and was judged out of scope for a
  re-run seat.

## Appendix — commands behind every number

| Number | Command |
|---|---|
| tip `e6da78b…` | `git rev-parse HEAD` |
| instrument `afb4ff74…`, counter `5a5adc94…`, successor `a07c2269…` (worktree) | `sha256sum verifiers/check_erratum_absorption.py verifiers/check_scoped_rules.py verifiers/check_scoped_rules_v31.py` |
| fresh stdout + exit §1 | `python3 -B verifiers/check_erratum_absorption.py --self-test; echo exit=$?` |
| byte-identical diff §2 | `awk` block-extract from receipt + `diff -u` (exit 0) |
| determinism | second fresh run `diff`ed against the first (exit 0) |
| recompute §3 | `python3 -B /tmp/recompute_absorb.py` (exit 0) |
| receipt absent at `3e7aed9b` | `git show 3e7aed9b…:.ufo/waves/round-62/C1-absorb-measure.txt` (fatal: not in rev) |
| receipt unique + stable | `git log --format='%H %ci %s' -- <receipt>` → only `f9ab0812`; sha equal at `f9ab0812`, HEAD, worktree |
| instrument/counter at `3e7aed9b` | `git show 3e7aed9b…:<file> | sha256sum` |
| commit chain timestamps | `git log --format='%H %ci %s' -1 <rev>` for `9f03dcd7`, `9228be47`, `3e7aed9b`, `f9ab0812` |
| ancestor checks | `git merge-base --is-ancestor <rev> HEAD` (and `…9f03dcd7 3e7aed9b…`) |
| `9228be47` lacks the instrument | `git ls-tree 9228be47… verifiers/ --name-only` |
| hollow receipt committed/stable | `git show HEAD:<controls/absorption-hollow.txt> | sha256sum` == `sha256sum` worktree == `5fcee82a…` |
