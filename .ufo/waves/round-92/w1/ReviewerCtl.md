# ReviewerCtl — scoped findings (2026-11-05)

Item-payload and full evidence live at `.ufo/waves/round-92/w1/ReviewerCtl/ReviewerCtl.md` (with witness logs in the same directory). Summary for the validator-rendered path:

- (a) counting command held twice: `round-92 controls: shortcuts refused 2 of 2; honest held 2 of 2`, exit 0, byte-identical both runs.
- (b) FORGE (cap raised + fabricated pin admission `1111…`, real floors blob `a189e61b…`): tip battery `FAIL guard instrument-pin`, C2-shortcut stays REFUSED exit 1. Presence of a pin entry does not launder — blob equality holds.
- (c) FORGE (stale freeze-base admission `6f2c52fb…` while new postimage `1e75039b…`): still refused — `FAIL guard instrument-pin`, `C2-PREDICATE-UNMET`. Stale-blob admission from an older rev does NOT pass.
- (d) old controls at base bytes: `SELF_TEST_TIMEOUT_S=360 C2-PREDICATE-MET rc=0`; `C1-PREDICATE-UNMET rc=1 (killed 14 of 14)` — both byte-for-behavior matching the frozen red-before receipts.
- (e) four of five verdict strings byte-match frozen §C1; **FINDING R1 (HIGH)**: the C2-shortcut refusal prints `…admission missing (FAIL guard instrument-pin: …blob <sha> at <rev> is not a pinned blob)` — the tokens `unpinned` and `guards G of 5` from the plan's quoted sentence are absent. Scored counting line unaffected; needs script fix or plan addendum.
- (f) missing-script (rc 127) and exit-2 injected script both yield `observed: shortcuts refused 2 of 2; honest held 1 of 2`, exit 1 — the runner cannot print 2 of 2 in either failure mode.
- **R12 (MEDIUM)**: `census-before.txt`, `nowork-c1-controls.txt`, `q73-sweep.txt` are cited by the frozen plan/dispatch but absent from the freeze commit tree (verified via `git ls-tree e073723…`). L1 disposition needed before scoring against them.
- Findings R2–R12 (severity-ranked) in the full report; candidate CONFORMS on the scored predicate; scoring held at 10/9.
