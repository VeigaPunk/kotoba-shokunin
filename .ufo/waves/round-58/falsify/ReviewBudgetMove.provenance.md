# Provenance — `ReviewBudgetMove.md` (round-58 falsify seat, misrooted)

Round-58 falsify seat `ReviewBudgetMove` wrote its report into the fleet root at
`/home/vgpnk/Projects/shokunin/.ufo/waves/round-58/falsify/ReviewBudgetMove.md` (untracked; 10,299 B; mtime
2026-10-23 05:34:09 -0300), not into this lane. The round-58 report did not account for it (routed defect R1,
`corpus/lessons/round-58-verifier-spotcheck.md` § 7).

Round 59 (L1 `KotobaR59`, 2026-10-23) copied it byte-exact to `.ufo/waves/round-58/falsify/ReviewBudgetMove.md`:
`cmp` exit 0; sha256 `c288bbd8427b38cda487b6693fe3a3774a674d9dcff944dd7f27fa7d9295cb8d`. The fleet-root copy is left in
place: the spot-check names its removal as operator-side. The content is the seat's own and unedited.
