# Fleet SKILL.md audit — first end-to-end domain task

Audited 2026-09-28 (round 5). Subject: the 5 sibling shokunin SKILL.md files —
the nearest real customer of this domain's checklist, per the round-1
aggregator audit's recommendation.

- Method: independent L2 `reviewer` lane applied the 13-item trigger-fidelity
  checklist verbatim (strict reading) to each file; L1 independently verified
  the frontmatter items and all cited-defect lines.
- Files: `kagi` 110, `kake` 179, `kasegi` 240, `kengaku` 246, `kumitate` 283
  lines (`wc -l`).

## Verdict table (strict checklist reading)

| Item | kagi | kake | kasegi | kengaku | kumitate | Aggregate |
|------|------|------|--------|---------|----------|-----------|
| 1 name matches dir | P | P | P | P | P | 5/5 |
| 2 quoted triggers | F | F | F | F | F | **0/5** |
| 3 anti-trigger in desc | F | F | F | F | F | **0/5** |
| 4 sibling arbitration | F | F | F | F | F | **0/5** |
| 5 body opens w/ role | P | P | P | P | P | 5/5 |
| 6 fail-closed prereqs | F | F | P | P | P | 3/5 |
| 7 table rows → action | F | F | F | F | F | **0/5** |
| 8 cmds runnable as pasted | N/A | N/A | N/A | N/A | N/A | no fenced shell blocks in any file |
| 9 failure signatures | P | P | P | P | P | 5/5 |
| 10 citations resolve | F | P | F | P | P | 3/5 |
| 11 stale-risk pinned | P | P | P | P | P | 5/5 |
| 12 ≤600 lines | P | P | P | P | P | 5/5 |
| 13 no TODO/placeholder | P | P | P | P | P | 5/5 |

## Fact — the shonen mint template produces non-conformant frontmatter

All five descriptions share one shape:
`Domain specialist — <domain> — scopes <paths>. Rank: shonen.`
Capability + scope only: zero quoted trigger strings, zero anti-triggers,
zero sibling arbitration. This is a *template-level* defect, not five
independent mistakes — the trigger surface was never populated at mint.
Cross-domain relay: each sibling lane (or the orchestrator) owns its own
frontmatter fix; the checklist exists to verify it.

## Fact — named sibling overlaps exist but are unarbitrated

Concrete overlaps the audit found in-body:

- `kagi` ↔ `kake`: both describe CDP-bridge flows (kagi L31–32/L71–72 vs
  kake L84–87); neither description names the other.
- `kengaku` ↔ `bailian-docs-llm-wiki`: kengaku L240 cites the bailian wiki
  for model data with no arbitration clause for model-query overlap.

This resolves the round-4 README gap "no named rival exists in-registry":
rivals exist; the arbitration clauses don't.

## Fact — per-file defects worth fixing in place

| File | Defect | Evidence |
|------|--------|----------|
| kagi L53–54 | `handoff-status.json` cited bare; real file is `~/.local/state/tac/handoff-status.json` | `ls` shows no such file under skill repo |
| kagi L26 | `op.env` prerequisite lacks fail-closed stop path | body text |
| kake L46 | `webzites` invoked bare; `command -v webzites` → empty; bin lives at `~/Projects/webzites/bin/webzites.mjs` | L161 names the bin path but no prereq step declares it |
| kasegi L86 | `corpus/knowledge/claim-gates.md` resolves under the skill repo but L8 sets the reader's base to `~/Projects/bounties` — ambiguous cwd | `ls` both trees |

## Meta-findings — checklist defects the audit exposed

Strict application produced five ambiguities; SKILL.md was updated this round:

1. **Item 4 scope.** PROVINCE.md "report to orchestrator" is boundary text but
   doesn't name siblings — checklist now states arbitration must live in the
   `description` of the routed file when a named overlap exists.
2. **Item 6 "every prerequisite" undefined.** Now defined: any binary, file,
   env var, or sibling artifact the body's commands assume, declared or
   implied.
3. **Item 7 strict last-column rule over-fails.** Tables whose decision cell
   sits mid-row (kagi: task→command→notes) fail the letter but pass the
   intent. Rule rewritten: every row must contain an action cell; trailing
   evidence columns allowed only if an action cell exists earlier.
4. **Item 8 "command block" ambiguous.** Covers inline commands too; runnable
   means the binary resolves on PATH or a declared location.
5. **Item 10 citation base unstated.** Relative paths must resolve from a
   base the file names (repo-relative default, or explicit root).

## Self-audit note

kotoba's own SKILL.md under strict item 7: the "when to use a decision table"
table ends in an `Evidence` column — same over-fail. The refined wording
(action cell must exist, not be last) fixes the rule, not the example. No
other checklist regressions found on self-read.
