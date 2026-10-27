Seat F20CheckcomputeW1 — recomputation of w1 dead seats

Observed lane HEAD: `6523aced1ee0ebe07dca996213bdc645a6acbd1e`, matching the stated freeze. Read-only `git status --short` reports 35 untracked paths including the w1 outputs and w2 dispatch materials; claim data is not present as committed lane bytes at HEAD. This is the freeze/base, not a landed claim-data revision.

The round-77 plan requires attacking the landed tip and running counters against it. Since claim data is not committed, I did not run either counter against an invented or scratch revision and do not claim C1 or C2 verified. The w1 verdicts are reports, not a committed artifact; the plan’s counters remain frozen.

Dead-seat recomputation: not performed. The assignment's prescribed evidence inputs (`w1-results.json` and w1 reports) exist only as untracked wave files at the freeze, and the required claim-data landing is absent. Hence no independently auditable, landed w1 result set can be recomputed from committed bytes. This remains a blocker rather than a guessed dead-seat count.

Exact checks performed:
- `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD` → `6523aced1ee0ebe07dca996213bdc645a6acbd1e`.
- `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin status --short` → clean index/worktree plus 35 untracked paths, including `.ufo/waves/round-77/w1-results.json`, `.ufo/waves/round-77/w1/`, and w2 dispatch files.
- C1 counter: not run; no landed data revision to test.
- C2 counter: not run; no landed data revision to test.

Minimal unblock: land the frozen w1 claim data at the intended lane tip, then recompute seat counts from the committed w1 result JSON and report files and run the exact pinned C1/C2 commands with their own exit statuses. This does not harm any axis; it is required evidence, not an axis tradeoff.

VERDICT: BLOCKED — claim data is not committed at lane HEAD 6523aced1ee0ebe07dca996213bdc645a6acbd1e; neither counters nor dead-seat claims can be verified against a landed revision.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w2/F20CheckcomputeW1.md