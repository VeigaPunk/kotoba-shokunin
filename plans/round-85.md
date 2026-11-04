# Round 85 — plan (kotoba, hyaku run 15, attempt 1; Linux host)

Date: 2026-11-04. Base: `1c8f37edf2e5ac0fb3c2be1c88e32406313fe47b` (lane `master`; `state` prints
`local=1c8f37e… remote=1c8f37e… ahead=0 behind=0`, tracked=0 untracked=0). Author: L1 `KotobaR85`.
Round shape: ONE v1 wave of 16 seats (band 8–16, run-15 block), 6 attack seats (37.5 %).

Two claims on distinct axes: **C1 depth** (the lowest owned axis, 9) and **C2 freshness**
(the tied-lowest advisory axis, 8.0). The lane's two-readings L0 question stays open and is routed
around, not assumed: under the owned-axes reading the lowest axis is depth (C1 works it); under the
all-axes reading freshness 8.0 and adjacency 8.0 tie low (C2 works freshness). The stagnation nudge
is dormant (depth 9 < saturation line 10.0), so no waiver is claimed.

## Trigger (measured at base, this host, this tree)

- `python3 -B verifiers/check_substrate_pins.py` → `UNREADABLE 2/3 pins failed:
  omp_binary_sha256, omp_binary_mtime`, exit 2: the pin names `/home/vgpnk/.local/bin/omp.real`,
  a Windows-era wrapper-target path this host does not have.
- `python3 -B verifiers/verify_surfaces.py --json` → `"error": "omp binary not found:
  /home/vgpnk/.local/bin/omp.real"`, exit 2. A probe run with the host's real ELF
  (`--omp-binary /home/vgpnk/.local/bin/omp`, omp 18.15.0, sha256 `6737ee24…`) already reads
  `pass 7, fail 0`, exit 0 — the extraction survives the 18.12.6→18.15.0 drift; the pin path does not.
- `SKILL.md` frontmatter: the parsed `description` is 1,021 of 1,024 characters and its first
  sentence is 150 characters, while this lane's own SKILL.md § Router model records that omp cuts the
  listing at offset 99 (`_8n=100`; `SKILL.md:30`, `SKILL.md:169`, `SKILL.md:587`) — the lane's own
  frontmatter violates the render rule the lane documents, and there is no committed trigger eval set.
- `bash scripts/sources-census.sh validate --root <fleet> kotoba` → exit 1, 180 E12 rows
  (`S001`…`S254` "row outside Registry section"): the committed `corpus/SOURCES.md` is CRLF, the
  census's `## Registry` heading test compares a `\r`-suffixed heading and never enters the section.
- Pre-existing reds this round does not claim (recorded, not harmed): `verify_skill_checklist.py`
  exit 1 (`governance.citation_resolves`: 11 lane-relative tokens naming fleet-repo paths, a
  Windows-host-era citation form), `verify_corpus_integrity.py` / `verify_corpus_independent.py`
  exit 1 (baseline refresh + 7 unindexed corpus files), `check_sibling_census.py` with the round-49
  census exit 1 (`province rows 20 matched 4`; PROVINCE was re-pinned at round 74 — the round-74
  census is the current base and reads `20 matched 20`, exit 0).

## C1 — depth (owned lowest axis, 9; sourced): the lane's own description obeys the render rule the lane documents, with an eval set

Frozen predicate (the same sentence in this plan, the counter's label and the SCORECARD row):

> `python3 -B verifiers/check_description_render.py --rev <rev>` (NEW counter, round-85 bytes; frozen
> by this plan's commit before any after-value exists) prints `description render rules met N of 8`
> and exits 0 iff N == 8.

Rules, exact (the counter's `R<k>` labels are the same strings):

- **R1 `first_sentence_le_99`** — the first sentence of the parsed `description` (text up to the first
  `.` that is followed by a space or the end) is ≤ 99 characters (omp's measured listing cut,
  `SKILL.md:30`).
- **R2 `prefix_carries_triggers`** — the first 99 characters of the parsed description contain
  `skill` and one of `prompt`, `SKILL.md` (case-insensitive): what a cut listing shows still identifies
  the domain.
- **R3 `spec_max_1024`** — the parsed description is 1–1024 characters (spec/vendor ceiling, S018).
- **R4 `imperative_invocation`** — the parsed description contains `use this skill when`
  (case-insensitive) and the literal `Triggers:` clause (the checklist's `trigger.literal_trigger_string`
  rule is preserved).
- **R5 `sibling_clauses`** — `python3 -B verifiers/check_sibling_census.py
  corpus/knowledge/sibling-overlap-census-round74.md --province PROVINCE.md --skill SKILL.md`
  exits 0 and prints `skill description names 10 of 10 non-none lanes`.
- **R6 `eval_set_shape`** — `verifiers/fixtures/description-eval-round85.tsv` has header
  `label<TAB>query`; 8–10 `should-trigger` rows and 8–10 `should-not-trigger` rows; ≥ 5
  `should-trigger` rows contain none of the description's declared trigger terms (indirect positives);
  every `should-not-trigger` row shares ≥ 1 lowercased alphanumeric word of ≥ 4 characters with the
  parsed description (near-miss negatives). Source: S213 (opened this round).
- **R7 `no_xml_tag`** — the parsed description contains no `<` or `>` (the packager rule, S019).
- **R8 `sourced_entry`** — `corpus/knowledge/description-trigger-discipline-round85.md` exists at the
  measured rev with `source:` naming `S213`, `verified-at: 2026-11-04`, a `recheck:` value, and a
  located quote of ≤ 25 words.

Base values are measured, never assumed: the counter is run at the base rev and its receipt committed.
Expected base < 8 (R2/R3/R5/R7 are already satisfied by the base description; R1/R4/R6/R8 are not);
the target is exactly `8 of 8`.

**Candidate payload (frozen here, unmeasured; 876 characters, parsed; verified against R1/R2/R3/R4/R7
and the round-74 sibling guard — `10 of 10`, exit 0 — before this plan's commit):**

```
Use this skill when auditing or rewriting a skill file or prompt. Triggers: "skill file", "SKILL.md", "frontmatter description", "trigger words", "prompt craft", "write a skill", "audit this skill", "skill quality". Anti-triggers: general prompt engineering for model outputs (not skill files), runtime code changes, and domain content inside a skill's reference/ tree. Sibling boundary: kagi, kake, kasegi, kengaku and kumitate own their own SKILL.md content — this skill audits and reports; fixes route to the owning lane. chousa owns the research method; kama owns endpoint verification; tameshi owns the fixture and mutation method; tsukuroi owns host package and initramfs hooks. NOT kotodama-shokunin: kotodama owns naming and language for fictional worlds despite the similar name. Note: shokunin files sit outside the omp discovery roots, so omp never reads this text.
```

**Controls, committed before any after-value:**
- `W0` base bytes scored by the frozen counter — must read < 8 (expect 4 of 8).
- `W1` naive cut: the base description truncated to its first 99 characters — must read < 8.
- `W2` token dump: a description made of the trigger list and the ten lane names without clauses —
  must read < 8 (R5).
- Each rule also carries a `--self-test` mutation arm that must turn that rule red.

**Kill rule:** if any control world reaches `8 of 8`, the counter is wrong and the claim stops before
data; if the after-value is < `8 of 8`, the claim is an honest miss as declared (no narrowing).

## C2 — freshness (advisory tied-lowest axis, 8.0): the substrate pin names this host's omp and the loader census re-derives across the 18.12.6 → 18.15.0 drift

Frozen predicate (same sentence in this plan, the receipt labels and the SCORECARD row):

> `python3 -B verifiers/check_substrate_pins.py` exits 0 printing `OK 3/3 pins hold`, AND
> `python3 -B verifiers/verify_surfaces.py --json` exits 0 with `"pass": 7` and `"fail": 0`.

Bindings of the predicate (all measured at the tip, not asserted):
- the omp pin path resolves to `/home/vgpnk/.local/bin/omp` (this host's ELF, `omp/18.15.0`);
- `omp_binary_sha256` == the ELF's sha256; `omp_binary_mtime` == its ns-exact ISO stamp;
- the surfaces run reads the same path (no `--omp-binary` override needed) and its class inventory
  still matches `verifiers/surfaces-baseline.json` (42 ids, 8 extracted loader classes).

Base values (measured, exit 2 both) are the do-nothing control. Additional controls, committed before
the pin values land: a scratch baseline carrying the opencode sha256 under `omp_binary_sha256` must
exit 1 (`DRIFT`), and a baseline with the omp pin deleted must exit 1 (absent pin, never a silent
pass). Must-fail arm: the same baseline scored against a *different* ELF (`--omp-binary` of the
opencode binary) must exit 1.

**Kill rule:** if a wrong-binary or deleted pin still exits 0, the guard is vacuous and C2 stops
before the pin values land.

## Frontier step (§2b)

- `corpus/SOURCES.md`: census before at round start (`.ufo/waves/round-85/receipts/census-round-start.txt`,
  exit 1, 180 E12 — the CRLF defect above). This round: **no new row** (S213 already holds the page;
  a new row would be a W04 duplicate — the round-74 rejection reason), S213 re-opened live this round
  (HTTP status, bytes, sha256, located quote, access date) and its `used-by` gains the new entry
  (old→new logged in the lesson). Rows added: 0. Rows touched: S213 (`used-by`), plus a byte-level
  line-ending normalization of the whole file (cells byte-identical; disclosed in the report).
- Round-end census must exit 0: the CRLF normalization is what makes the registry parse on this host.
- Mine one mistake: the r84-D1 numeric-wording defect (a count carried without a counting command) and
  the CRLF/host-dependent parse class; both enter `corpus/lessons/round-85.md` § Mistakes with
  class · evidence pointer · captured-by · fix.
- Sourced claim: C1 (R8 binds the entry citing S213, opened this round).
- Assimilation: `merge/kotoba/` — the round-74-rejected `spec-description-trigger-discipline.md` is
  adopted through this lane's own gate as the round-85 entry, re-grounded on S213 (the row the
  package's S231 duplicates); refused material (its best-practices half, already carried by S223)
  stays refused with the reason recorded.
- `considerthese/2026-10-26.md` proposal 3 (the description audit, raised four days running) is
  executed by C1; proposals 1 and 2 (byte ceiling, registry move) are sized out as a separate round.

## Conformance repairs (not claims; required for round-end gates)

1. `corpus/SOURCES.md` CRLF → LF (content byte-identical modulo `\r`); census `--file` exit 0.
2. Coverage-map index rows for the 7 unindexed corpus files (round-81…round-84 lessons and
   spot-checks), then `refresh-corpus-baseline.py` at the final pre-report commit.
3. `corpus/lessons/round-84.md` gains an append-only correction block (r84-D1).
4. Pre-existing reds named above stay red or are repaired as reported; none is claimed.

## Wave plan (one v1 wave, 16 seats)

Build (10): ScoutSource, ScoutSubstrate, ExecC1Counter, ExecC1Eval, ExecC1Desc, ExecC2Pin,
ScribeC1Entry, ScribeSources, ScribeLesson, Connector.
Attack (6, 37.5 %): ReviewerC1, ReviewerC2, Critic, MutTester, Labrat, Sentinel.
Residual call: none. The validator rejects `planner`; the L1 holds that seat (this plan is its output).
