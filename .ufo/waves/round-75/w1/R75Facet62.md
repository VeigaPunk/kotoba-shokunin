# R75 facet 62 — Q73: the byte-identical-pin sweep and its in-counter ledger

## Axes
- **calibration** — does Q73's own detector actually see the class it names, and can it be shown to fail (Q20 two-direction measurement, Q25 counter-can-fail)?
- **operability** — does the command in the rule run as pasted, and is the ledger property it promises ("append-only") held by anything?

## Target rule
`corpus/QUALITY.md:89` (Q73), a 5-cell row, grounded in `corpus/lessons/round-74.md:91` (M138) and landed with
`plans/round-74-addendum-1.md:130`. It is the last row of the admission bar and the only row whose criterion cell carries a
`\|` byte. Everything below is read at lane `HEAD 65a5c7a663249e0522cc49e4a148424200d9ddfe` (clean tree; only
`.ufo/waves/round-75/` untracked).

## Observations (committed bytes)

1. **Grounding is real.** `corpus/lessons/round-74.md:91` records M138 with two named receipts
   (`receipts/noharm-2c81137….txt`, `receipts/noharm-559ee76….txt`), states `province core rows 0 of 2` with finding
   `§ Adjacent differs from the base`, and states the guard is *not* in the tip battery and *not* named by the plan —
   i.e. the rule was written from a post-landing detection, not a pre-freeze one. `plans/round-74-addendum-1.md:130`
   records the erratum and the added ledger. This is an observation; the rule's prospective half is an inference from it.

2. **The mechanism Q73 promises exists in the exemplar counter.** `verifiers/check_province_core.py:45-51` carries the
   comment and `ADJACENT_ERRATA = {<sha256>: <reason>}` with exactly one entry at `HEAD` (one entry; the dict is absent at
   `2c81137`, so it grew in `88f18cd`). The accept path is `:104-109`; the two self-test arms are
   `:158-170` ("ledgered Adjacent rewrite is accepted", "an unledgered Adjacent rewrite is still rejected"); the print at
   `:179` reports `len(broken) + 3` = **12** assertions.

3. **The sweep command is literal and measurable — raw form.** `grep -n 'differs from the base\|byte-identical'
   verifiers/*.py` → **16 matches in 8 files**:
   `check_province_core.py:24,45,48,108`, `check_tip_battery.py:50,54,122,328` (these 2 files are genuine base-pin
   conjuncts); `check_substrate_pins.py:86` (pin-key comment); `check_assertion_floors.py:1132` (self-test comment);
   `check_r68_routed_repairs.py:36` (docstring); `check_scoped_rules.py:1988`, `…_v31.py:2058,2062`, `…_v32.py:2306,2310`
   (alias-reason strings). Measured precision: **2 of 8 files** (3 if `check_substrate_pins` counts) are the class the rule
   targets; **7 of 16 matches** are prose/comments/alias text and cannot indicate a base-section pin.

4. **The same command, pasted from the rendered page, returns nothing.** `corpus/QUALITY.md:89` is the only row in the file
   containing a literal backslash-pipe (`grep -Fc '\|' corpus/QUALITY.md` → `1`; all other 72 `| Q…` rows carry 6 pipe
   bytes, Q73 carries 7). GFM consumes `\|` as an escaped pipe inside a cell, so the rendered command is
   `grep -n 'differs from the base|byte-identical' verifiers/*.py`; under BRE that is a *literal* string. Measured:
   **no output, exit 1** — a silent "no pins found" pass. The same row also presents 6 cells to any naive
   `split("|")` reader, where its siblings present 5; 28 verifier files use `split("|")` on table rows (e.g.
   `verifiers/check_author_rules.py:246`, `check_command_files.py:379`, `check_client_trust_gates.py:104`, and
   `check_province_core.py:87-90`). Current QUALITY readers survive because they are line-based
   (`verifiers/check_r68_routed_repairs.py:289-291` matches `^\| Q\d+ \|`), so this is a latent, not an active, defect.

5. **Recall gap: the pin family held in JSON files is outside the glob and the vocabulary.** `SKILL.md:226-229` states
   that `verifiers/checklist-baseline.json` pins *every* checklist box by its normalized text hash and that "a reworded,
   added, or removed box FAILs the run". The JSON carries `schema: kotoba-checklist-v1`, `file: SKILL.md`, and per-box
   `text_sha256` entries; `verifiers/verify_skill_checklist.py` fails on reword (self-test arm `map-box-reworded`, `:2076`)
   and `verifiers/check_alwayson_boxes.py:213` reads the same baseline **at the measured rev**. Neither file is named by
   Q73's sweep (both are outside `verifiers/*.py`, and a 0-hit grep for either phrase in `verifiers/*.json` is measured).
   The same shape holds for `surfaces-baseline.json`, `corpus-baseline.json` and `floors-registry.json`. So an r75 edit to
   a SKILL.md checklist box (or to the pin data itself) is a Q73-class event the prescribed sweep cannot surface.

6. **"Append-only" is asserted, not held.** `ADJACENT_ERRATA` appears only in `verifiers/check_province_core.py` and in the
   two prose records (`round-74.md:91`, `round-74-addendum-1.md:130`); no gate compares its key set across revisions.
   `check_province_core.py` is **not** one of the six battery instruments (`verifiers/check_tip_battery.py:144-151`) and
   **not** in `verifiers/floors-registry.json` (32 instruments; name absent). And the self-test cannot detect a dropped
   committed entry: `selftest()` writes its own digest (`:159`), clears the dict in `finally` (`:172`) and never reads the
   committed key — deleting the committed `c41f7b54…` entry leaves `--self-test` green. Only a `--rev` run at a revision
   whose `## Adjacent` still differs from base would notice.

7. **"Never edited to widen its target" is under-defined against Q73's own remedy.** The remediation itself adds one
   digest to the accepted set (`:106`), i.e. the accepted input set *strictly grew*; `plans/round-74-addendum-1.md:130`
   asserts "the r69 claim's predicate is not widened" without a measurement of that set. The two readings — "target" =
   the counted rows (2 of 2, unchanged) versus "target" = accepted inputs (widened by one ledgered rewrite) — are not
   distinguished, and Q73 does not name Q28 (judgment tables frozen at the plan commit) although the ledger key set is
   exactly such a table, written after the freeze.

8. **Table continuity.** `corpus/QUALITY.md` is one logical table split into four Markdown segments (breaks at `:69`, prose
   `:71-73`, blank `:77`); 73 `| Q…` rows total, Q73 last. Line-based readers are safe; block-table readers would see only
   Q01–Q57. No verifier currently parses the table as a block, and no gate counts QUALITY rows.

## Assessment (inference)

- **Sourced depth / factual support: high.** The rule is tied to a named mistake, named receipts, and a code mechanism
  that exists and can be read; nothing in the row is unsupported.
- **Falsifiability: partial.** The sweep half is a public command whose output I measured in both directions (2 true-pin
  files vs 6 prose matches; 0 hits in the rendered form). The other two conjuncts — "found before the plan freezes, named
  in the plan's touch list" and "append-only sha256 ledger" — have no gate and no comparison across revisions, so they are
  currently *prose obligations*. A rule whose third conjunct cannot fail is a Q25/Q26-shaped weakness in the bar itself.
- **Scope: one drift.** Q73 says "a file section that an earlier claim's counter pins byte-identical". The confirmed r75
  pin on a SKILL.md section (`checklist-baseline.json`) is a *text-hash* pin, not a section sha256, and lives in data, not
  in a counter script. Read literally, Q73 does not cover it; read by intent, it must.
- **Concrete r75 relevance:** the milestone is a description audit. `SKILL.md` is 590 lines against the 600 cap, and the
  checklist-baseline pin is the nearest historical constraint on any SKILL.md box add/reword. Any r75 claim that edits a
  checklist box or its baseline is a Q73 event with a *silent* sweep.

## Concrete control for an r75 claim (design; not executed here)

A pre-freeze, read-only checker `verifiers/check_pin_sweep.py --rev <rev> --plan <path>` with four arms, each able to fail:

- **(a) Raw-byte sweep, widened universe and vocabulary.** Grep `verifiers/*.py` **and** `verifiers/*.json` for both phrase
  families plus the pin-data keys (`text_sha256`, `"floor"`, `blob`), printing `path:line`. Must-fail arm: delete
  `check_province_core.py:108` in a fixture and require the hit to disappear from the output.
- **(b) Escape-aware paste check.** For every fenced/backticked command in `corpus/QUALITY.md`, split on unescaped pipes;
  require **5 cells per `| Q…` row** and require the two sweep forms (raw bytes, rendered text) to produce the **same hit
  count**. Must-fail arm: the Q73 line as committed (raw 8 files / rendered 0) must read red.
- **(c) Ledger monotonicity.** `ADJACENT_ERRATA` keys at `git show <base>:verifiers/check_province_core.py` ⊆ keys at
  `--rev`; a removed key is exit 1 with the key printed. Must-fail arm: the fixture with the committed entry deleted
  (which today leaves `--self-test` green — observation 6).
- **(d) Touch-list binding.** Every path from (a) appears verbatim in the plan's touch list; a hit absent from the plan is
  exit 1. This is the only mechanical reading of "named in the plan's touch list".

Cheap manual pre-freeze equivalent, if the checker is not built this round:

```
grep -n 'differs from the base\|byte-identical' verifiers/*.py verifiers/*.json   # expect the full pin set
grep -n 'differs from the base|byte-identical'  verifiers/*.py verifiers/*.json   # must NOT be empty
grep -c 'text_sha256' verifiers/checklist-baseline.json                           # 45 boxes → pin data exists
git show <base>:verifiers/check_province_core.py | grep -c '"[0-9a-f]\{64\}"'    # ⊆ HEAD's count (1)
```

The second line is the falsifier: if it is empty while the first is not, the markdown escape ate the alternation and the
sweep in the bar is dead. Expected at `HEAD`: 16 matches / 8 files; rendered form empty, exit 1.

## Risks / unknowns

- **No gate was run** (wave rules): every number above comes from `grep`/`git show`/`awk` over committed bytes at
  `65a5c7a`. `check_province_core.py --rev` and `--self-test` were read, not executed; observations 6 and 7 are code-path
  readings, not receipts.
- The 12 phrase-less base-reading verifiers were **not** individually classified as content-pin vs do-nothing baseline; only
  the JSON-baseline family (observation 5) was confirmed as a content pin. Do not read "6 of 8 prose matches" as "the sweep
  misses 6 counters".
- `plans/round-75.md` does not exist yet (`plans/` ends at `round-74-addendum-1.md`), so conjunct (d) cannot be checked and
  the r74 plan is historical, not an r75 claim.
- Whether an r75 description-audit claim touches a checklist box, the description frontmatter (`SKILL.md:1-22`) or only
  prose is undecided; `check_description_thresholds.py` carries no base pin, so a description edit alone would not be a Q73
  event — only the box/baseline family is.
- This facet makes no claim that r75 has a pin conflict; it reports the sweep's measured reach and a control design.

## Evidence commands (exact; run from the lane root at `65a5c7a`)

- `awk 'NR==89' corpus/QUALITY.md` — Q73's five cells; 7 raw pipe bytes vs 6 on all 72 sibling rows
  (`awk '/^\| Q[0-9]/ {n=gsub(/\|/,"|"); print n}' corpus/QUALITY.md | sort | uniq -c` → `72 × 6`, `1 × 7`).
- `grep -Fc '\|' corpus/QUALITY.md` → `1`; `grep -n 'differs from the base|byte-identical' verifiers/*.py` → no output,
  exit 1.
- `grep -n 'differs from the base\|byte-identical' verifiers/*.py` → 16 matches / 8 files (listing above).
- `grep -n 'text_sha256\|checklist-baseline' verifiers/checklist-baseline.json SKILL.md` → `SKILL.md:226-229`,
  `checklist-baseline.json` box entries; `grep -n 'map-box-reworded' verifiers/verify_skill_checklist.py` → `:2076`.
- `sed -n '104,110p;158,180p' verifiers/check_province_core.py` — accept path, ledger arms, `:172` clear, `:179` 12.
- `sed -n '144,151p' verifiers/check_tip_battery.py` — the six battery instruments (province_core absent).
- `python3 -c "import json;d=json.load(open('verifiers/floors-registry.json'));print('province_core' in json.dumps(d))"`
  → `False`.
- `git show 2c81137:verifiers/check_province_core.py | grep -c ADJACENT_ERRATA` → `0`; at `HEAD` → `49,106,159,172`
  (1 entry).
- `sed -n '89,93p' corpus/lessons/round-74.md`; `sed -n '130p' plans/round-74-addendum-1.md` — grounding and erratum.

Report: .ufo/waves/round-75/w1/R75Facet62.md
