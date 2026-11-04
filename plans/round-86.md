# kotoba — round 86 plan (frozen before any candidate data)

- Host: Linux (`omp/18.15.0`, ELF `/home/vgpnk/.local/bin/omp`, sha256
  `6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f`).
- Round base: `e5d966b51494f4177868ad5f46806a204783ef6c` (`master`, remote equal).
- Previous round: r85 closed `rejected-honest-stop` (C1 depth killed before data; C2
  freshness improved). Its spot-check routes D1–D7 (§ Routed defects below).
- Planner seat: held by the L1 (the validator rejects `planner`); the bounded planning
  data-walk rides the two scouts and the connector.

## Axis choice

Scores at base (`SCORECARD.md` § axes): depth 9 (owned), consistency 10 (owned,
calibration sub-axis), coverage 8.5, operability 8.5, calibration 8.5, **freshness 8**,
**adjacency 8.0**. Lowest non-retired: freshness and adjacency, tied at 8. This round
declares **one claim, on freshness** (the stagnation nudge is not invoked). One claim is
deliberate: the claim is the whole round's work, and a second claim would not change
admission (every claim must verify).

## C1 — freshness: the lane's omp catalogue model re-derived against omp 18.15.0

**Surface changed:** the lane's executable model of how omp builds the `<skills>`
catalogue a model sees — `verifiers/verify_harness_claims.py` (`WALKUP_REL`,
`USER_ROOTS`, `discover_skills`, `parse_frontmatter`, `omp_key`, `preview`) plus a new
roots ledger `verifiers/omp-skill-roots.tsv` whose every row cites a quote located in
the omp 18.15.0 ELF. The model was last derived against omp at rounds 7–13 (four user
roots, "verified 2026-09-28 against the 17-name catalogue"); `SKILL.md` § Router model
still describes that state.

**Why it is drift (measured at base, before any candidate):** the newest real omp
catalogue on this host (session `KakeR90.jsonl`, rendered 2026-11-04T21:55:22.890Z, cwd
`/home/vgpnk/Projects/shokunin`) lists **215** skills; the lane model discovers 84 of
which 83 appear, and reproduces **83 of 215** lines byte for byte — every line it
models is right (0 `render-differs`), and **132 lines come from roots the model does not
know** (`.ufo/waves/round-86/receipts/c1-K0-base.txt`: 132 `MISS … not-discovered`).
omp 18.15.0's own source, embedded in the ELF, shows the render rule unchanged
(`skill-descriptions.ts`: `k = 100`, `E = 40`, `T = 160`, `_ = 12`, sentence back-off,
`…` word cut; key = sha256(prompt ‖ 0 ‖ name ‖ 0 ‖ description)) and new discovery
settings (`cfgSkillsEnableClaudeProject`, `…ClaudeUser`, `…CodexUser`, `…PiProject`,
`…PiUser`, `…AgentsProject`, `…AgentsUser`, `cfgSkillsCustomDirectories`) — a
source-located, falsifiable drift.

**Frozen predicate** (the same sentence here, in the counter's docstring and in every
receipt):

    python3 -B verifiers/check_omp_catalogue_repro.py --rev <rev>
        -> prints "omp catalogue lines reproduced N of 215", exit 0 iff N >= 205
           and guards G1-G4 all PASS; exit 1 otherwise; exit 2 = could-not-evaluate.

- Counter: `verifiers/check_omp_catalogue_repro.py` at the freeze commit (sha256 in
  `.ufo/waves/round-86/receipts/c1-counter-selftest.txt`); self-test `0 failure(s) over
  34 assertions`, exit 0.
- Fixture: `verifiers/fixtures/omp-catalogue-r86/catalogue.json`, sha256
  `0b3443e1058fffa75a287faca7d839d4bbfa3b7cd6f672783e1b0e70d714b488` (215 entries, the
  228 cache rows, the 273-byte keyed prompt, session path/line/cwd/timestamp).
- Guards: G1 no-echo (no transcript/cache tokens in the model's discovery functions; no
  render ≥ 40 chars hardcoded anywhere in the module); G2 provenance (each reproduced
  name's SKILL.md resolves outside the lane, the fixture and every scratch root, and its
  mtime and ctime precede the render); G3 fixture pin; G4 roots ledger (every reproduced
  name's root matches a ledger pattern whose quote is located in the pinned ELF).
- Isolation: the scored module runs only inside bwrap with the session transcripts, the
  description cache, the agent/history DBs, the fleet tree, `/fast/scratch`, `/tmp` and
  `/var/tmp` hidden; the guards run in the parent on its JSON output.

**Target:** N ≥ 205 of 215 with G1–G4 PASS. **Base:** 83 of 215, G4 FAIL, exit 1.

**Controls executed before this freeze** (receipts in `.ufo/waves/round-86/receipts/`,
modules in `.ufo/waves/round-86/controls/`):

| id | world | expected | observed |
|---|---|---|---|
| K0 | do-nothing: the round base's model | below target, exit 1 | `83 of 215`, G4 FAIL (no ledger), exit 1 (`c1-K0-base.txt`) |
| K1 | echo forgery: reads the fixture or the newest transcript (tokens obfuscated past G1), writes fake SKILL.md files with the observed renders, backdates mtime | refused | sandbox denies both reads and the write: `83 of 215`, exit 1 (`c1-K1-forgery.txt`); run unsandboxed during the build it reached 57 and G2 FAILed on ctime |
| K2 | answer-key forgery: all 215 renders as a module literal | refused | G1 FAIL (215 hardcoded literals), exit 1 (`c1-K2-hardcode.txt`) |
| S | self-test worlds: good (exit 0), empty roots, echo token, answer key, wrong back-off floor, provenance, fixture pin, no cache, scratch root, post-render ctime, broken module, hidden root (bwrap), no ledger, unlocated quote, uncovered root, bad header, glob and `{cwd}` patterns (exit 0) | as labelled | `0 failure(s) over 34 assertions` (`c1-counter-selftest.txt`) |

**What a mechanical world can reach (Q71 disclosure, before data):** a brute-force root
search (every host directory holding a same-named SKILL.md, first match wins) could
reproduce lines without reading omp; it fails G4 unless each root cites a located ELF
quote. G4 checks location, not meaning: whether each cited quote is the code that makes
omp read that root is assigned to named non-author review (the reviewer seat in this
round's wave, and the closure). The critic seat scores the brute-force world on this
counter and reports its N with and without a ledger; that number is reported beside the
target, whatever it is.

**Kill rule:** any of — N < 205 at the landing commit; any guard FAIL; the counter, its
fixture or its pins changed after this freeze; the after model reaching N only through a
root the reviewer finds omp 18.15.0 does not read — and C1 is an honest stop. No
narrowing of the target after data.

**No-harm battery (Q65/Q72), run at base and on the post-state before landing:**
`check_gate_registry.py --rev <rev>` (66/66 at base → must read 67/67 with the new row);
`verify_harness_claims.py --self-test`; `verify_surfaces.py --json` (7/7);
`check_substrate_pins.py` (3/3); `verify_corpus_integrity.py --json`;
`verify_skill_checklist.py`; `sources-census.sh validate --root … kotoba` (exit 0);
`check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md --province
PROVINCE.md --skill SKILL.md` (20/20, 10/10). Base reds carried, not claimed: tip battery
`2 of 6` (assertion floors timeout; checklist, corpus integrity, corpus independent exit 1)
and `verify_harness_claims.py` `16/28` DRIFT against round-13 expectations.

## Frontier step (CORPUS.md contract v1)

- Census at round start: exit 0, 33 `W04` (`receipts/census-round-start.txt`).
- Sourced claim: C1 rests on a row opened this round — the omp 18.15.0 source embedded in
  the installed ELF (`kind: code`, tier A for "what this host's omp does"), plus the
  upstream repository if its tag for 18.15.0 is reachable; the new knowledge entry cites
  that S-id.
- Mined mistake: candidates — the lane's catalogue check assumed "every line of the
  newest block must byte-equal a cached description" (`verify_harness_claims.py:371-379`,
  true at round 9, false since: 15 of 215 lines are cached), so the model's discovery
  drift stayed invisible behind a DRIFT count; or an r85 routed defect.
- Assimilation: one `merge/kotoba/` theme only if it bears on C1 (connector decides);
  else `Assimilation: none`. considerthese: proposals 1–2 of `2026-10-26.md` remain open
  and untouched (registry move blocked on L0 `round-73`).

## Routed defects from the r85 spot-check (status-neutral; addressed, not claimed)

D1 count without its selection rule → corrected count in `corpus/lessons/round-85.md`
append-only block; D2 tip after-value without receipt → stated; D3 baseline note subject →
additive note in `verifiers/corpus-baseline.json`; D4 LOG range → corrected citation; D5
size pair → corrected wording; D6 truncated capture line → re-captured K4 line; D7 WAVE-DONE
unartifacted → this round commits `<wave>-wavedone.txt` with the orchestrator message.
