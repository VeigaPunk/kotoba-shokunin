# CritC2Control — cheapest worlds that meet C2 (8 of 8) without the claimed work

**Verdict: the C2 counter's 8 of 8 is reachable without the claimed work.** Eleven of thirteen
junk worlds score `skill eval facts backed 8 of 8` (exit 0) on the frozen counter. The cheapest
starts at the pre-data commit `a647fa7` and adds 13 lines: a nine-line entry with no fact text,
three `x`-filled SOURCES rows, and one bare path line in SKILL.md. The census and no-harm battery
pass on eight of the eleven.

The quote half of the counter holds: every key term occurs exactly once in the pinned snapshots,
and a changed snapshot exits 2. Everything else is unchecked: the fact text, the SKILL citation,
the SOURCES row content, and whether any of it renders. So N == 8 measures "eight pinned quotes
located in pinned bytes, plus registry bookkeeping". It does not measure facts backed, and it does
not measure depth.

The committed controls (`controls/C2-junk-control.txt`, `controls/C2-forged-control.txt`) attack
only the two conjuncts that hold: key terms and membership in the snapshot. No control attacks the
fact cell, the SKILL line, the SOURCES row content or rendering, so the controls cannot tell the
counter apart from a quote grep.

Calibration: the real tip `16b212a` is not shown to be junk. Its counter file is byte-identical to
the frozen one (sha256 `fc768197…` matches `controls/freeze-receipt.txt`, and
`git log 53de0ac^..16b212a -- verifiers/check_skill_evals.py` lists only `53de0ac`). What this
report shows is that the counter's 8 cannot tell the tip apart from W01, W05 or W12. The depth
judgement of the tip rests entirely on the non-author spot-check.

## Setup

- Sandbox: `git clone --shared` of the lane under `/tmp/k70w1-CritC2Control.T0cy/kotoba-shokunin`.
  It is named `kotoba-shokunin` because the checklist's `trigger.name_directory` check fails on any
  other directory name. Each world is a branch off `16b212a` (W12 and W00 branch off `a647fa7`).
  Scratch was deleted after the run.
- Per world:
  - `python3 -B <sandbox>/verifiers/check_skill_evals.py --repo <sandbox> --rev <world>`, the
    sandbox counter.
  - The lane's frozen counter `python3 -B /home/vgpnk/…/kotoba-shokunin/verifiers/check_skill_evals.py --repo <sandbox> --rev <world>`.
  - `sources-census.sh validate <sandbox>`.
  - `verify_skill_checklist.py --json`, compared against the sandbox base failure set.
  - `verify_corpus_integrity.py`, `verify_corpus_independent.py --json` and
    `check_gate_registry.py --rev <world>`.
- Sandbox base at `16b212a`: the counter prints `skill eval facts backed 8 of 8`, exit 0. The
  checklist has exactly two non-PASS checks, `trigger.citation_resolves` and
  `governance.citation_resolves` (FAIL). Both come from the `/tmp` sandbox environment, per lesson
  M116; the "beyond base" column below excludes them.
- `check_assertion_floors.py` was run once at the base (34 s). It shows `FAIL checklist … self_test_failures=1`
  in the sandbox, which is the same environmental cause. It counts self-test assertions, does not
  read the corpus, and was not run per world.

## Worlds

"Same" in the frozen-counter column means the frozen counter printed the same verdict as the
sandbox counter.

| world | rev | diff vs start | sandbox counter | frozen counter | census validate | checklist beyond base | integrity / independent / gate |
|---|---|---|---|---|---|---|---|
| W01 bare | `0fca413` | 3 files +13 −69 | **8 of 8**, exit 0 | same | exit 0 | none | 0 / 0 / 0 |
| W02 contradict | `ccb270a` | 2 files +9 −9 | **8 of 8**, exit 0 | same | exit 0 | none | 0 / 0 / 0 |
| W03 absurd scope | `fd9078c` | 1 file +3 −3 | **8 of 8**, exit 0 | same | exit 0 | none | 0 / 0 / 0 |
| W04 absurd enums | `5c3c7b2` | 1 file +3 −3 | **8 of 8**, exit 0 | same | **exit 1**: E05 ×3, E06 ×3, E08 ×3 | none | 0 / 0 / 0 |
| W05 hidden | `a7168a4` | 3 files +10 −1 | **8 of 8**, exit 0 | same | exit 0 | none | 0 / 0 / 0 |
| W06 negated | `7ab1b3e` | 3 files +14 −69 | **8 of 8**, exit 0 | same | exit 0 | none | 0 / 0 / 0 |
| W07 shadow rows | `0eeedff` | 1 file +6 −3 | **8 of 8**, exit 0 | same | **exit 1**: E12 ×3 | none | 0 / 0 / 0 |
| W08 mid-word quotes | `089006a` | 1 file +3 −3 | **8 of 8**, exit 0 | same | exit 0 | none | 0 / 0 / 0 |
| W09 rotated facts | `492c5e0` | 1 file +8 −8 | **8 of 8**, exit 0 | same | exit 0 | none | 0 / 0 / 0 |
| W10 fenced, off-topic | `7d22fe2` | 3 files +17 −67 | **8 of 8**, exit 0 | same | exit 0 | none | 0 / 0 / 0 |
| W11 counter swap | `695ea91` | 3 files +2 −66 | **8 of 8**, exit 0 (entry absent) | **0 of 8**, exit 1 | exit 1: E11 ×3 | none | 1 / 1 / 0 |
| W00 predata no-op (control) | `2358582` | empty | 0 of 8, exit 1 | same | exit 0 | none | 1 / 1 / 1 (inherited) |
| W12 predata bare | `1390984` | 3 files +13 −0 | **8 of 8**, exit 0 | same | exit 0 | none | 1 / 1 / 1 (inherited, as W00) |
| W13 snapshot tamper | `9f20a38` | 1 byte | exit 2 `environment error: snapshot_tampered: S211-run_eval.py.txt` | — | — | — | — |

Exact bytes of the key worlds, from `git show <branch>:<path>`:

- **W01 / W12 entry (whole file, 9 lines).** There is no fact text, no prose, no title and no
  `verified-at` line:
  ```
  source: S209 S210 S211
  | F1 | S209 "The main file you author by hand is evals/evals.json." |
  …
  | F8 | S211 "did_pass = trigger_rate >= trigger_threshold" |
  ```
- **W01 / W12 SOURCES row.**
  `| S209 | x | docs | A | x | x | x | mined | 2026-10-25 | 90d | corpus/knowledge/skill-eval-artefacts-round70.md |`
  The source and URL, scope, anchor and teaches cells are all `x`. Census validate exits 0.
- **W01 / W12 SKILL line.** Line 241 is the bare path `corpus/knowledge/skill-eval-artefacts-round70.md`.
  W12's SKILL.md is 598 lines, so the checklist's 600-line cap holds.
- **W02.**
  - Fact cells: `| F3 | Each case runs once, with the skill only; there is no baseline. | S209 | "run each test case twice: once with the skill and once without it" |`
    and `| F8 | run_eval.py uses `>` exactly like the specification; there is no disagreement. | S211 | "did_pass = trigger_rate >= trigger_threshold" |`.
  - The SKILL line inverts the finding: "The spec passes … at `>=` 0.5 and … `run_eval.py` only
    *above* it, so keep the run count even".
  - `--fetch` on W02 prints `live quotes found 8 of 8`, so the second evidence does not separate
    this world either.
- **W05.** The SKILL line is `<!-- corpus/knowledge/skill-eval-artefacts-round70.md -->`. The entry
  and the three SOURCES rows are wrapped in `<!--` … `-->`, so the rendered page shows none of the
  claim.
- **W06.**
  - The entry is headed `RETRACTED — every row below is false; do not use.`
  - Its source line is `source: none — S209 S210 S211 were all refused`.
  - The SKILL line is ``- Never consult `corpus/knowledge/skill-eval-artefacts-round70.md`: retracted, every fact in it is false.``
  - An earlier variant (`cb15f35`) also set used-by to `not <entry> (retracted)`. It still scored
    8 of 8, because the counter checks used-by by substring; census caught it as E11 ×3.
- **W08.** Quotes cut mid-word (`"ain file you author by hand is evals/evals.json."`,
  `"un each test case twice: …"`, `"id_pass = trigger_rate >= trigger_threshold"`) pass. The match
  is a raw substring, not bounded at word edges.
- **W10.** The entry is titled `# Sourdough starter maintenance`, and all rows sit inside a
  ` ```text ` fence.
- **W11.** The committed counter gets one added line, `+        n = TOTAL`. The entry is deleted.

The quotes are tight. Each key-term site occurs exactly once in the normalised S209 and S210
snapshots ("by hand", "twice", "LLM judgment", "with specific evidence", "above a threshold": count
1 each). In S211, `trigger_rate >= trigger_threshold` is only at `S211-run_eval.py.txt:232`; line
234 is the `<` branch. So no world can swap in a quote from a different context.

## Findings

### 1. The fact cell is never read (W01, W02, W06, W09, W12)

- **Defect:** `check()` collects `sids` and `quotes` from every cell (`check_skill_evals.py:144-145`)
  and never reads the fact text. A row may have no fact cell (W01), or one that contradicts its quote
  (W02) or belongs to another fact (W09).
- **Tradeoff or defect:** the docstring declares prose fidelity out of bounds (`check_skill_evals.py:23-25`),
  so W02 and W09 are a declared tradeoff. But the plan's predicate says "Fact Fi … is backed"
  (`plans/round-70.md:84`), and the printed verdict is `skill eval facts backed`. A row with no fact
  is not a backed fact, so W01 and W12 are a fixable defect. The verdict wording is a calibration
  overclaim.
- **Axes:** depth, calibration.
- **Smallest safe fix:** require the four-cell shape `| Fi | fact | S### | "quote" |`, with the
  quote and the source ID only in their own columns and a fact cell of at least about 8 words that is
  not itself the quote. This kills W01, W06's bare rows, W10 and W12. W02 and W09 need the
  spot-check's fact-against-quote reading, which should be named as a required C2 conjunct in the
  report rather than left implicit.

### 2. Non-rendered text counts (W05, W10)

- **Defect:** `fact_rows`, `source_rows`, the `source:` scan and `ENTRY in skill`
  (`check_skill_evals.py:107-135`) parse raw lines. HTML comments and fenced blocks are included,
  and census validate does not object either.
- **Axes:** depth, consistency.
- **Fix:** strip `<!-- … -->` and fenced code blocks from the entry, SKILL.md and SOURCES.md before
  parsing.

### 3. The SKILL "citation" is a substring (W01, W05, W06, W12)

- **Defect:** `skill_ok = ENTRY in skill` (`check_skill_evals.py:135`). A bare path, a comment or a
  "never consult" line all satisfy it, and the plan's "SKILL.md at --rev cites the entry path"
  (`plans/round-70.md:91`) is met by a line that tells the reader to ignore the entry.
- **Axes:** depth (assimilation into SKILL is the point of the claim), calibration.
- **Fix:** require a rendered list-item line that names the path and the three source IDs (S209,
  S210, S211). The tip's line 241 already does. Polarity cannot be checked mechanically; the
  spot-check owns it.

### 4. The SOURCES check duplicates census authority, weaker (W03, W04, W06 variant, W07)

- **Defect:** the counter checks only `len(row) == 11`, `row[7] == "mined"` and
  `ENTRY in row[10]` (`check_skill_evals.py:164-168`).
  - The dict keeps the last duplicate ID (`:112`), so W07's rejected originals are shadowed by junk
    rows at EOF.
  - Invalid enums and future dates pass (W04).
  - A used-by of `not <entry>` passes (variant `cb15f35`).
  - Census validate catches W04 (E05, E06, E08), W07 (E12) and the `cb15f35` variant (E11) that the
    counter accepts. It does not catch W03's absurd scope or teaches cells, or W01's `x` cells.
- **Assessment:** two authorities over one row, and the counter is the looser one.
- **Axes:** consistency, calibration.
- **Fix:** make `sources-census.sh validate` exit 0 a C2 conjunct (it already is in the no-harm
  battery), or reject duplicate IDs, require an exact used-by match, and require a URL in the source
  cell. Scope and teaches sanity (W03) stays with the spot-check.

### 5. Quote matching is not bounded at word edges (W08)

- **Defect:** `quote not in norm(snapshot)` (`check_skill_evals.py:160`) is a plain substring test,
  so mid-word fragments pass.
- **Severity:** low, since the key terms still bind the subject.
- **Axes:** calibration.
- **Fix:** match with `\b` or space anchors on the normalised text.

### 6. The counter's own provenance (W11)

- **What W11 shows:** the counter that runs is the measured tree's file. A world that edits it scores
  8 of 8 with the entry absent; the frozen lane counter on the same rev prints 0 of 8, and the
  sandbox file's sha256 no longer matches `controls/freeze-receipt.txt`.
- **Not a defect at the real tip:** the file there is unchanged since `53de0ac` and its sha matches.
  It is a trust-boundary fact the judge must enforce.
- **Axes:** consistency.
- **Fix:** the receipt should run `git show 53de0ac:verifiers/check_skill_evals.py`, or check the
  freeze sha before reading the verdict.

### 7. The controls are blind and not reproducible by commit

- **What the controls cover:** `controls/C2-junk-control.txt` and `controls/C2-forged-control.txt`
  each break one quote conjunct; the self-test (`check_skill_evals.py:277-293`) adds the
  removal-style mutants. No control or self-test case covers a missing or contradicting fact cell,
  a non-rendered row, a negated or bare SKILL line, duplicate or invalid SOURCES rows, or a swapped
  counter.
- **Not reproducible:** the control commits named in the receipts are absent from the lane object
  store. `git -C <lane> cat-file -t 20a6e597…` (and the same for `4e088afd…` and `c3fb277d…`)
  printed `fatal: git cat-file: could not get object info`. The controls can only be re-derived,
  never re-run by commit.
- **Axes:** calibration.
- **Fix:** add the W01 and W05 shapes to the self-test as must-be-below-8 worlds, and keep control
  worlds as a committed patch or bundle.

## What 8 of 8 proves (the trust boundary, measured)

**Proven by N == 8:**
- Eight quotes of 5–25 words, each carrying its pinned key terms, occur in three snapshots whose
  sha256 matches the counter's pins. W13 shows a changed snapshot exits 2.
- Three SOURCES lines exist with `mined` in cell 8 and the entry path somewhere in cell 11.
- Some line beginning `source:` names the three IDs.
- The entry path occurs somewhere in SKILL.md.

**Not proven by N == 8:**
- That any fact text exists, or agrees with its quote (W01, W02, W09).
- That the entry is about the subject, or renders at all (W05, W10).
- That SKILL.md assimilates the finding, or does not contradict it (W02, W06).
- That the SOURCES rows are census-valid, unique, scoped or even sourced (W01, W03, W04, W07).
- That the counter that ran is the frozen one (W11). This needs the external sha check.
- That the claim is deep. W12 reaches 8 of 8 from the pre-data commit with +13 lines and zero
  sentences of knowledge.

C2 as frozen is a sourcing-hygiene claim (quotes bound to pinned bytes) wearing a depth label. The
round report should say so, and the tip's depth reading must cite the non-author spot-check of
fact against quote, not N.

## Tooling

None installed or upgraded.
