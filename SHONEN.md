# kotoba-shokunin — Promotion checklist

Promotion to shokunin requires all of (verifier attribution per PROTOCOL.md
round-6: `[x]` externally verified, `[~]` lane-asserted):

- [~] kotoba-self (L1): SKILL.md contains real decision tables, error patterns,
  checklists, cited sources — evidence: `SKILL.md` (339 lines) holds a 7-row
  anatomy table, a 5-row decision-table table, a 13-item trigger-fidelity
  checklist, a 9-item agent-definition checklist, an 18-row anti-pattern
  table, and a 20-entry cited Sources list.
- [~] kotoba-self (L1): at least one end-to-end domain task executed and
  logged — evidence: round-5 fleet audit applied the 13-item checklist to the
  five sibling `*-shokunin/SKILL.md` files (`corpus/knowledge/
  fleet-skill-audit-round5.md`); round-6 adds the 9-item agent-definition
  checklist + 18-file audit (`corpus/knowledge/agent-def-audit-round6.md`)
  and the literal-trigger miss proxy over opencode.db. Note: the round-5
  reviewer lane was L1-dispatched — asserted, not external.
- [~] kotoba-self (L1): instructions executable without oral context — an
  L2 reviewer lane ran the checklist verbatim against 5 files with zero
  clarification requests; but the lane was self-dispatched, so this stays
  asserted until an external verifier runs it.
- [~] kotoba-self (L1): no cross-domain bleed — round-6 defects found in
  `opencode/agents/*.md` were audited-and-reported, not fixed; PROVINCE.md
  unchanged and still matches landed work.
