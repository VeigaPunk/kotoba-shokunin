# S05DeadSeats seat report (R76-D5)

Deliverables: `build/S05DeadSeats.md` (analysis, 64-row table, parse recipe), `build/S05DeadSeats.parse_results.py`, `build/S05DeadSeats.r76-table.txt` (raw script output).

Commands run (all read-only on lane inputs; exit 0 each):
- `python3 -B build/S05DeadSeats.parse_results.py ../round-76/w1-results.json` → exit=0, output saved to r76-table.txt.
- python json inspection of results/dispatch/spec; `ls w1`; grep of the 12 absent names in build/receipts/w1; `git ls-files verifiers | grep -E 'desc_craft|r75_routed'`.

Findings: 64 results == 64 dispatched == 64 spec; 52 report files, 12 absent. No status field exists in results.json (`note` null x64, registry `agentId` null x64). 0 of 64 final outputs has a top-level `VERDICT:` line (57 JSON, 5 narration, 2 `<think>`). Dead seats (unyielded, no file) = 6: B06, B07, A04, A07, A23, B28; plus B11 unyielded but with its report. The other 6 absentees returned blocked/inconclusive JSON inline because counters/D4 floors/freeze receipts did not yet exist in the lane tree (attackers dispatched concurrently with builders). Status counts: DONE 45, BLOCKED 8, NOVERDICT 4, UNYIELDED 7. Full detail and per-seat table in the build doc. Cause of the 6 unyielded deaths is [INFERENCE] (no error object recorded).

Tooling installed: none. Scratch: none left (/fast/scratch/hyaku/s05.out removed).

VERDICT: 12 report-less seats = 6 dead (unyielded) + 6 blocked-inline (inputs absent); no status field exists, 0/64 outputs had a plain VERDICT line; parser built and run on r76 (exit 0, 64 rows)
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/S05DeadSeats.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/S05DeadSeats.parse_results.py, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/S05DeadSeats.r76-table.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/S05DeadSeats.md
