# kotoba-shokunin — Promotion checklist

Promotion to shokunin requires all of:

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  evidence: SKILL.md — 7-row anatomy table, 5-row decision-table table, four fidelity checklists (13/9/9/8 boxes: `git show HEAD:SKILL.md | awk '/^## /{h=$0} /^- \[ \]/{c[h]++} END{print c[h]}'` → 13/9/9/8; the dispatch audit artifact numbers the same set as 12 items), 20-data-row anti-pattern table (`… | awk '/^## Anti-patterns/,/^## Refusals/' | grep -c '^|'` → 22 lines incl. header+separator), cited Sources list. Round-10 corrected the two counts this line previously carried (22 rows, 13/9/12/8) — aggregator audit r6 defects 1/9.
- [~] At least one end-to-end domain task executed and logged in LOG.md
  evidence: LOG.md round-5 fleet SKILL.md audit (5 siblings, 13-item checklist); round-7 dispatch-prompt audit of 43 files; round-10 harness-claim verifier (`verifiers/verify_harness_claims.py`, 27 checks, exit 0 on the live host) — `corpus/knowledge/harness-verifier-round10.md`.
- [~] Instructions executable by an agent without oral context
  evidence: LOG.md round-7 — a blank-context L2 reviewer ran the 13-item trigger-fidelity checklist on SKILL.md with zero clarification requests (13 verdicts + meta-findings); round-10 made the harness half of the file executable rather than prose (same verifier).
- [~] No cross-domain bleed (PROVINCE.md still accurate)
  evidence: LOG.md round-7 — cross-domain defects in .ufo/prompts/, ~/.config/opencode/, scripts/shokunin-watchdog.sh audited and reported, not fixed; round-10 aggregator audit adopted as-is and its kotoba-owned defects closed inside this repo; PROVINCE.md unchanged.

Verifier note: every check in this file is lane-run — therefore `[~]`, and a
`[x]` box still requires a reviewer who did not author the round.
