# Round 71 lessons — kotoba

## Gate

S212 and S213 are the S209/S210 agentskills.io guides cited with their upstream revision:
`agentskills/agentskills@69ef37e9424c0a7ea9dd2293b559e43ec8176379` (`git ls-remote`, equal to
`main` on 2026-10-25). The upstream tree carries `docs/skill-creation/evaluating-skills.mdx` and
`docs/skill-creation/optimizing-descriptions.mdx`; each quote was re-located on the upstream file
(`evals/evals.json` author-by-hand line, the produced-files sentence, the twice/with-and-without
line, the PASS/FAIL evidence sentence, the scripts-over-LLM-judgment sentence, the
not-everything-needs-an-assertion sentence, the 0.5-threshold should-trigger sentence — all in
`evaluating-skills.mdx`; `did_pass = trigger_rate >= trigger_threshold` stays in
`anthropics/skills@dbd4588f9e1033efb41dad4bef2f7947c8993d44`). Located quotes: S212
`"The main file you author by hand is evals/evals.json."` (9 words); S213
`"A should-trigger query passes if its trigger rate is above a threshold (0.5 is a reasonable
default)."` (17 words).

Dispositions and re-opens: none refused this round. Id collision: S212/S213 were the next free
ids (registry went 209–211 → 209–213); `grep -n '^| S21[0-9]' corpus/SOURCES.md` shows no
collision. Census after: exit 0 (`.ufo/waves/round-71/receipts/census-after.txt`).

## Mistakes

- **M121 — class: evidence (control worlds that never became committed objects).** Evidence:
  the r70 controls lived only as seat-scratch clones (the 254 MB mirror was deleted uncommitted;
  M109 recorded the symptom). Captured by: the round-71 prompt's routed defect "control worlds
  as committed bundles" and QUALITY's receipt rule — a control that exists only in `/tmp` cannot
  be re-derived. **Fix (shown able to fail):** control worlds are committed file bundles under
  `.ufo/waves/round-71/controls/` materialized by each counter's own `--self-test` real-git arm
  over a clone of the pre-data commit `a647fa7`; the receipts
  `.ufo/waves/round-71/receipts/c{1,2}-junk-world.txt` record the junk commits and the red exits
  before data landed.
- **M122 — class: presence-floor (a gate invoked without pinning which gate).** Evidence:
  r70's K69-11 ran `verify_skill_checklist.py` from the measured checkout — a revision could
  carry a stub gate that reports its own PASS. Captured by: `RevC1Counter` HIGH-2 and the r70
  spot-check routing. **Fix (shown able to fail):** the successor reads the checklist blob at
  `--rev` and requires membership in `CHECKLIST_ALLOWED` (pre-edit `508512da…`, post-edit
  `8d44c06…`); the selftest's rev-controlled-stub arm exits non-zero on any other blob.
- **M123 — class: boundary (word-boundary regex that matched inside words).** Evidence:
  `(?<![\s])`/`(?![\s])` lookarounds are inverted — they require whitespace neighbours instead of
  word boundaries, so a quote inside a longer word passed. Captured by: W08's mid-word quote arm.
  **Fix (shown able to fail):** `(?<![\w])`/`(?![\w])` lookarounds; the W08 arm cuts the quote
  inside the word `main` and the counter rejects it.

## Status changes

S212, S213 mined at landing (superseding S209/S210 for citation; the superseded rows stay with
their upstream-commit anchor cells). K69-11 measured closed by C1's successor counter at the tip
(blob `8d44c06`, `governance.citation_resolves` PASS).
