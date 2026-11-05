# ScribeEntry summary — round-88 w1

Written: `corpus/knowledge/omp-root-semantics-round88.md` (150 lines; body 147 ≤ 160; untracked, not committed).
Report: `.ufo/waves/round-88/w1/ScribeEntry.md`.

Handoffs: `SOURCE_READY`, `ELF_MAP_READY`, `C2_READY` present; `C1_READY` and `FORGERY_READY` absent after the 45-minute window. `ExecForgeryWorlds/matrix.tsv` exists (before measured, after `NOT_RUN`).

Entry contents, each with its command or receipt:
- Provenance trio: S257 row and upstream URL with sha256 `976360…`; ELF sha256 `6737ee…b7b0f`; verified at `4df1e80…`; recheck commands for both v2 gates.
- v2 root counter: five conjuncts and why each exists; binding token candidates (ELF_MAP col 7); freeze digest still `PENDING`.
- Upstream bound: S257 line 149 quote, line 144 exclusion, ELF offsets 173865771 / 173865668.
- Forged worlds: before 0 of 4 (r87 record, `forgery-worlds.txt` lines 15/31/47/63); after not measured (v2 does not parse); cross-check 10/10/9/9 of 12 from ReviewerC1 (not the frozen counter).
- Honest bounds: 12 ledgered + 6 unledgered = 18 roots (ELF_MAP lines 15–20); r87 counter frozen (sha `6e826f3b…8922`).
- C2 pointer: `closed 5 of 5` at tip; self-test `1 failure(s) over 16`.

Not admitted: C1. The v2 counter raised `UnboundLocalError` at sha `506a2ba9…`, and does not parse at sha `892404e3…`; binary check reports 0 of 12 against an independent 12 of 12; binding sets unfrozen; no floors row.

Census: before `E11 S257 missing used-by …round88.md` + 33 W04, exit 1; after 33 W04, exit 0.

Tooling: none installed or upgraded.
