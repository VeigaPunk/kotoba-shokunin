# Round 72 lessons — kotoba

Claims (frozen in `plans/round-72.md` at `7b229a1889bd87d53902150d4f4658dc0c1117b6`, errata E1–E4 in
`plans/round-72-addendum-1.md`): **C1 depth** (sourced, assimilation): four author-facing rules in
`SKILL.md` § Trigger-fidelity checklist; **C2 freshness**: host substrate re-derived and re-pinned;
**C3 consistency**: the six-gate tip battery. Round shape: wave 1 only (53 seats, 53 settled, 0 dead);
wave 2 (the falsify wave) was **not run** — see § Round honesty.

## Gate

Assimilation theme (addendum §10; nothing written, run or fetched inside `/home/vgpnk/Projects/shokuknow`):
**the resident-index versus on-demand rung**, from `merge/kotoba/` — staged entries
`skill-vs-always-on-boundary.md` and `context-rot-and-always-on-context.md`.

**Id collision check** (`.ufo/waves/round-72/assimilation/`): the lane registry holds 139 ids
(`reg-ids`), the package stages 188 (`staged-ids`), `collisions` lists 11 — `S203`–`S213`, the lane's
own rows from rounds 69–71, which the package numbered earlier. **Guard proof:** a scratch registry
with the indented row `  | S234 | indented |` yields `S203…S213 S234` under the 0–3-space pattern and
`S203…S213` (no `S234`) under the column-zero pattern
(`assimilation/guard-proof/SOURCES-with-indented-S234.md`). **Renumber map, by document:** staged
S262 (`docs.factory.ai/cli/configuration/skills`) → **S214**; staged S263 (pi `skills.md` raw) →
**S215**; staged S264 (Hermes Agent skills) → **S216**. Staged S261 Letta, S248 Vercel, S254 Chroma,
S255 and S256 are not appended (below).

**Rows opened this round** (each by a wave-1 seat and re-checked by the L1 against the committed
snapshot; access date 2026-10-25; quotes copied from the snapshot bytes, shaping named):

- **S214** — https://docs.factory.ai/cli/configuration/skills (308 → docs.factory.com/harness/skills),
  snapshot `.ufo/waves/round-72/snapshots/S262-factory-droid-skills.md:9`, sha256 `81409d89…`:
  "Use skills when instructions are too specific for always-on `AGENTS.md`, too structured for a
  one-off prompt, and useful enough to reuse." (21 words; the `AGENTS.md` code span is the page's own).
- **S215** — https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/skills.md,
  snapshot `S263-pi-skills.md:5`, sha256 `5b980552…`: "Use a skill when a workflow needs more context
  than a prompt template but does not need a new executable integration point." (21 words, verbatim).
- **S216** — https://hermes-agent.nousresearch.com/docs/user-guide/features/skills, snapshot
  `S264-hermes-skills.md:610-612`, sha256 `fb06e67d…`: "memory stores small durable facts that should
  always be in context, while skills store longer procedures that should load only when relevant"
  (22 words; whitespace collapsed across two source lines).

**Admitted:** `corpus/knowledge/resident-index-and-rungs-round72.md` (three rows, the rung rule: expansion
on ground the coverage map did not hold — `grep -rn 'middle rung\|one-off prompt\|three rungs'
corpus/ SKILL.md` printed nothing at the base, `ScribeEntryRung`'s sweep).
**Rejected, with reason and flip** (Q62: each on an observed fact): (1) staged
`context-rot-and-always-on-context.md` (S248 Vercel, S254 Chroma): its substance is measured
degradation and pass-rate figures — capability measurement, kengaku-adjacent ground
(`w1/ConnScopeSiblings.md`); the craft sentence it carries is already carried by S215/S216; flip: a
craft rule that cannot be stated without the figure. (2) S261 Letta: the staged entry says six named
agents, the page names five (`w1/ExecSrcLetta.md`), and the portability sentence is a vendor assertion
about its own family, not rung evidence; flip: a rule that needs a first-party portability statement.
(3) S255/S256: no admitted entry cites them (CORPUS rule 4). Also found and recorded (not adopted):
the staged Factory cell is a 10-word prefix that is not contiguous in the snapshot (code span), the
staged Hermes cell fails on a link target — the entry uses the contiguous sentences.

**Quarantine slice** (`assimilation/quarantine-slice-full.txt`, 13 data rows, re-derived this round;
hand-checks `w1/ExecQuar01…13.md`): 01 (S151) absent — span not on the cited page, traceable to
arXiv 2603.22455, refused as fabrication class; 02 (S167) absent — the quote cell holds lane
prose, refused; 03 (S168) declared span `section:` absent, but the row's real quote (the page H2) is
present after a markdown-heading fold — a parser artifact, **not** fabrication (Q62), corrected not
refused; 04 (S172) present after fold (register-side truncation at `user-le`, two `<code>` spans) —
adoptable, not needed by an admitted entry; 05 (S176) absent — referent present, staged as S256, refused for
its quote; 06 (S180) absent — names a section the page never had, refused; 07 (S185) absent, refused;
08–13 (S169, S236–S239, S243) prose class cell "could not be fetched" → `unverifiable`, not fabrication;
the sources fetch today (HTTP 200), so the class premise is stale. No refused row is appended.

**considerthese:** `considerthese/2026-10-25.md` § Self-improvement suggestions item 3 (route each
entry's author bullets into the audit checklist) is the one proposal worked: boxes A1–A3 cite the
r67/r68/r69 entries, A4 the new entry. Proposals 1, 2, 4, 5 (byte ceiling, registry move, intro frame,
description self-audit) are not worked — one per round; the byte/line-length measure is a Frontier lead.

## Mistakes

- **M124 — class: stale-premise (record vs tree).** Evidence: `plans/round-71.md` § No-harm battery
  promised `check_gate_registry.py` `53 of 53` and a battery run; at `c69711e` it reads `51 of 53`,
  floors `1`, corpus integrity `1` (`.ufo/waves/round-72/receipts/base-battery.txt`). Captured by: Q50
  (tip receipts) — r71 committed receipts only for its two counters. Fix: C3's counter
  (`check_tip_battery.py`, `2 of 6` at base).
- **M125 — class: reference-drift.** Evidence: the checklist self-test arm "live round-65 corrections
  land, only LOG.md:2678 red" went stale when the r71 errata row retired that red
  (`receipts/base-outputs/check_assertion_floors.out`: `self_test_failures=1`). Captured by: none →
  Q65. Fix: the arm asserts the live state and a regression arm fails when the errata row is dropped
  (`w1/ExecArmFix.md`; checklist floor 1862 → 1863).
- **M126 — class: stale-premise (substrate).** Evidence: the omp wrapper (2026-10-23) and opencode
  v2.1.4 left four instruments red with no freshness receipt (`base-battery.txt`: pins 2, surfaces 2,
  harness claims 2). Captured by: Q09 (named, not enforced). Fix: C2's counter and re-pin.
- **M127 — class: environment variance.** Evidence: the C3 counter's sandbox run of the unchanged base
  read `verify_skill_checklist.py` exit 0 in the wave-1 seat's run and exit 1 in two L1 runs, while the
  same checklist run by hand in an identical fleet-shaped sandbox exits 0 (`receipts/c3-base.txt`).
  Unresolved this round — recorded, not explained.

## Round honesty

The round budget was exhausted before wave 2: no falsify wave ran, so the round is 53 seats against the
64-seat floor, the three counters were not attacked by fresh seats, and the two seat findings that
changed the counters (E1–E3) came from wave 1. No claim here carries a non-author verdict.

## Status changes

S214, S215, S216 `mined` at landing. No other `status`, `recheck` or `used-by` cell changes.
