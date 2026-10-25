# ScribeBoxesB — draft boxes A3 (install-path trust) and A4 (rung) for SKILL.md § Trigger-fidelity checklist

Insertion point: end of `## Trigger-fidelity checklist` (base SKILL.md:253-327), i.e. after base line
326 (the last continuation of the `trigger.no_placeholder` box at 323-326) and before the blank line
327 / the `## Agent-definition fidelity checklist` heading at 328. Four lines per box, 6-space
continuation indent, matching the section's style. Verified at that index: 608 lines, 43 boxes,
0 near-misses, both boxes in section `Trigger-fidelity checklist`.

## Verbatim boxes

```markdown
- [ ] The install path is declared and its trust level stated: the same body
      is untrusted data in one client and a gated capability in another, and
      a project or remote path runs no embedded command in at least one client.
      (sourced: S198, S199, S200, S202; entry: corpus/knowledge/client-trust-gates-round68.md)
- [ ] Content sits on the right rung: a skill holds what is too specific
      for an always-on file and too shaped for a one-off prompt, and the
      always-resident surface is an index, not a payload.
      (sourced: S2XX; entry: corpus/knowledge/resident-index-and-rungs-round72.md)
```

Line lengths (chars, indent included): A3 `76 / 76 / 79 / 94`; A4 `72 / 72 / 57 / 82`. Bound was
≤4 lines of ≤96 chars; max observed 94.

## Box A3 — install-path trust

- **Frozen token set** (whole words, case-sensitive, all lowercase in the text): `install`, `trust`,
  `command`.
- **Observable test** (reading only, no runtime — the section's own contract): open the `SKILL.md`;
  for each fenced or inline command the body carries, the file names the install path the skill is
  discovered from (project root, remote URL, user directory) and the gate that path gets. FAIL when
  a command appears with no path statement, or the path is named but its trust is left implicit
  ("installed normally").
- **Checklist-baseline classification text:**
  `unexecuted:the install path is discovery-time state, not file text; partially covered by trigger.command_binary_resolves`
- **Sourcing:** all four cited rows verified in `corpus/SOURCES.md` — S198, S199, S200, S202: status
  `mined`, tier `B`, `used-by` = `corpus/knowledge/client-trust-gates-round68.md`. The cited entry
  carries its provenance trio: `source:` lines 1-6, `verified-at:` line 7, `recheck:` line 8.
- **Rows left out for the line bound:** S201 and S208. Five ids on the tail line exceed 96 chars
  (`(sourced: S198, S199, S200, S202, S208; …)` = 99 with the 6-space indent); S208 is the approval
  shape (the load succeeds, tool calls are approved) and S201's anchor is superseded by S208, so the
  four install-path/gating rows are the ones that carry the rule.

## Box A4 — rung (resident index vs on-demand payload)

- **Frozen token set** (whole words, case-sensitive): `prompt`, `always-on`, `skill`, `index`.
- **Observable test** (reading only): for each block in the file, name its rung — prompt (one task),
  skill (too specific for an always-on file and too shaped for a one-off prompt), always-on (every
  session). FAIL when a skill body carries content that would sit unchanged in an always-on file, or
  when the always-resident surface carries the payload instead of an index.
- **Checklist-baseline classification text:**
  `unexecuted:rung placement is a content judgement (too specific, too shaped); no length or token proxy separates the rungs`
- **Id slot:** `S2XX` is a placeholder. The frozen predicate matches `S###`, so the L1 must substitute
  the concrete id at landing; the tail then reads `(sourced: S2NN; entry: corpus/knowledge/resident-index-and-rungs-round72.md)`.
- **Sourcing gap the L1 must close:** `index` is not grounded by the four staged rows the entry is
  drafted from (Factory/pi/Hermes/Letta). It is grounded by the Vercel eval row staged as `S248`
  ("A compressed 8KB docs index embedded directly in `AGENTS.md` achieved a 100% pass rate, while
  skills maxed out at 79%", 20 words) — so the resident-index entry needs a `source:` line for that
  row (and a snapshot for it, predicate (d)) or the `index` clause is unsourced.

## checklist-baseline.json entries (hashes from the lane's own extractor)

```json
{"box_id": "trigger.16", "section": "Trigger-fidelity checklist", "text_sha256": "c056e5ada8f1569ea74b99ccd29c532357c29f998f6d8a6a19123f17e16f3ee3", "disposition": "unexecuted:the install path is discovery-time state, not file text; partially covered by trigger.command_binary_resolves"},
{"box_id": "trigger.17", "section": "Trigger-fidelity checklist", "text_sha256": "285c577c0bfe8a674e7e329dd9cca265fcaa1fa0cc1950e26395c8ca202b4679", "disposition": "unexecuted:rung placement is a content judgement (too specific, too shaped); no length or token proxy separates the rungs"}
```

`box_id` must be the next free numbers in file order (if A1/A2 land before these, they take .16/.17).
The A4 hash changes when `S2XX` is replaced — recompute with the extractor, do not reuse it.

## Landing constraints measured at base

1. `verifiers/checklist-baseline.json` `box_total` is 41 and `load_map` raises `MapError` (exit 3)
   when `box_total < len(boxes-entries)`; two new entries make 43, so `box_total` must rise to the
   entry count in the same commit.
2. `SKILL.md` is 600 lines and the `trigger.line_budget` box states 600; these two boxes add 8 lines
   (608), so ≥8 lines must be freed elsewhere in the same commit (more once A1/A2 land).
3. Both boxes are `unexecuted:` and carry no `(executed: …)` annotation — the map check fails a box
   whose annotation and disposition disagree.
