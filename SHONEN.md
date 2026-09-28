# kotoba-shokunin — Promotion checklist

Promotion to shokunin requires all of (verifier attribution per PROTOCOL.md
round-6: `[x]` externally verified, `[~]` lane-asserted):

- [~] kotoba-self (L1): SKILL.md contains real decision tables, error patterns,
  checklists, cited sources — evidence: `SKILL.md` (~487 lines) holds a 7-row
  anatomy table, a 5-row decision-table table, four checklists (13-item
  trigger-fidelity, 9-item agent-definition, 12-item dispatch-prompt, 8-item
  always-on), a 22-row anti-pattern table, and a cited Sources list.
- [~] kotoba-self (L1): at least one end-to-end domain task executed and
  logged — evidence: round-5 fleet audit (`corpus/knowledge/
  fleet-skill-audit-round5.md`); round-6 agent-def audit + miss proxy;
  round-7 dispatch-prompt audit (43 files, `dispatch-prompt-audit-round7.md`)
  and self-audit (`alwayson-checklist-round7.md`). Note: all reviewer lanes
  so far were L1-dispatched — asserted, not external.
- [~] kotoba-self (L1): instructions executable without oral context — an
  L2 reviewer lane ran the checklist verbatim against 5 files with zero
  clarification requests; round-7 replicated with a blank-context reviewer
  on this repo's own SKILL.md (13 verdicts + meta-findings, zero questions).
  Still asserted until an external verifier runs it.
- [~] kotoba-self (L1): no cross-domain bleed — round-7 defects found in
  `.ufo/prompts/`, `~/.config/opencode/`, and `scripts/shokunin-watchdog.sh`
  were audited-and-reported (see `corpus/knowledge/dispatch-prompt-audit-round7.md`
  defect tables + connector routing map), not fixed; PROVINCE.md unchanged.
