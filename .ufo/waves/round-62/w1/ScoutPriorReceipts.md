# ScoutPriorReceipts — C1 before-state (round 62 wave 1)

Seat: `KotobaR62.ScoutPriorReceipts`. Date of census: 2026-10-23. Lane read-only.
Question: of the five erratum classes that r61 says forced an arm amendment, how many have a **committed** measurement that scores the **landed** v3 counter (sha256 `5a5adc94…`) against that seat's attack table?

**Result: 0 of 5.** No file under `.ufo/waves/round-61/receipts/`, `.ufo/waves/round-61/controls/`, or `C1-v3-measure.txt` names `MutA1`, `MutA2`, `MutA3`, `MutA4`, or `MutFixtures`, and none scores those seats' attack rows. The sha is named in four r61 artifacts; every one of those namings is a world-level / fetch / base-exit measurement, not an arm-level re-score of the attack tables. Do not read the synthetic W1–W7 self-test as covering these classes.

## Table

| erratum | seat | attack count | against draft/landed | committed receipt? |
|---|---|---|---|---|
| E2 (A3 `url_key`) | MutA3 | 19 | draft sentence (v2 `ca2585a4` as oracle only) | no |
| E2b (A3(b) rendering alias) | MutFixtures | 1 (seam S1) | draft sentence (no counter CLI) | no |
| E2c (A4(iv) full-sha alias) | MutA4 | 12 + 3 | draft/plan text via a reference detector | no |
| E2e (guarded A1) | MutA1 | 15 | v2 bytes `ca2585a4` + scratch guard; not landed v3 | no |
| E2f (guarded A2) | MutA2 | 10 | v2 bytes `ca2585a4`; no v3 source existed | no |

0 of 5 committed receipts. The r61 report's line "each forced by a measured attack (MutA3, MutFixtures, MutA4 ×3 seams, MutA1, MutA2)" (`.ufo/reports/round-61/kotoba.md:40`, fleet) names the forcing seats. It does not claim those attacks were re-run on the landed counter.

## Attack tables (seat reports)

Line ranges are in the committed wave reports. "Attack count" is the seat's own counted rows that the r61 erratum cites, not a re-run.

### E2 — `wave/MutA3.md` lines 125–145 (19 data rows)

Section "3. Expected verdicts, one line per variant" starts at line 117. The table header is line 125, the separator line 126, data rows 127–145 (cases 1–19: 1 exact accept, 11 canonical-equivalence spellings at rows 2–12, 4 alias/redirect rows 13–16, 3 eligible rows 17–19).

What was executed: a scratch candidate of the **frozen A3 sentence** (`a3_spec.py` / `a3_impl.py`), with committed v2 helpers as the oracle. Seat text:

- lines 24–30: lane still carried counter v2 sha256 `ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a`; "no v3 source existed to run"; "attacked the **frozen A3 sentence itself**".
- lines 468–471: "No integrated v3 source existed at read time; I did not run v3".

`5a5adc94` occurrences in this file: **0**. `ca2585a4` occurrences: **4**.

### E2b — `wave/MutFixtures.md` lines 560–568 (1 seam)

The erratum (`plans/round-61.md:147–158`) cites seam **S1** only. S1 is the bullet at lines 560–568 ("W2 is not covered by A3 as worded" — recorded W2 rows are fresh, so amended A3 never evaluates them). That is a design judgment, not a counter run.

The §6 summary table at lines 603–615 has **11** design rows (W1–W7 and A1–A4). Lines 14–16 and 619–621 say no counter CLI and no `--self-test` was run, and "the per-item verdicts above are design judgments against the frozen sentences, not observed v3 output." Those 11 rows are not a measurement.

`5a5adc94` occurrences: **0**. `ca2585a4` occurrences: **2** (the v2 file that was read, not scored as v3).

### E2c — `wave/MutA4.md` lines 298–309 (12) and 356–357 plus 370–373 (3 seams)

The r61 report's "MutA4 ×3 seams" is the plan's seam 1 / seam 2 / seam 3 (`plans/round-61.md:228–232`), not a count of attacks re-scored on v3.

- Alias matrix, fenced block lines 297–310, **12** result lines (298–309): A0–A5, each `unanchored` and `anchored`. The seat calls the receipt `…/receipts/alias-matrix.txt` (line 295). That path is scratch. It is not a file in `.ufo/waves/round-61/receipts/` (that directory has exactly two files; neither is `alias-matrix.txt`).
- Three seams: A7 and A8 at lines 356–357 (`alias-seams.txt`, scratch); the fetch-cell seam is A9/A10 at lines 370–373 (lines 367–369 are A8 scan modes of the same seam; `fetch-claim-scope.txt`, scratch).

Also measured, same seat, same limit (not landed v3, not a committed receipt): date-clause mode table lines 121–131 (**9** worlds, W1a passes) and mutation table lines 141–145 (**3** mutants M1–M3). Those are the original date clause, which E2c then extended. They do not add a committed v3 receipt.

Seat text that fixes "draft", not "landed counter":

- line 45: "no v3 source exists at the tip; the counter is still `ca2585a4…`".
- line 69: "every verdict is an **A4-spec projection measured on a reference implementation**, not the frozen CLI's output."
- line 477: "Every A4/A4(iv) verdict is a projection on a reference detector… E2c is plan text, not code."

The word "landed" in the report title (line 1) and in §7 (line 277) means the **plan addendum** (`daf4ad7` / `511aff7d` / `921c2512` / `e2132443`), not `verifiers/check_scoped_rules.py`.

`5a5adc94` occurrences: **0**. `ca2585a4` occurrences: **3**.

### E2e — `wave/MutA1.md` lines 121–138 (15 mutants)

Section "3. The fifteen mutants" starts at line 113. Table header line 121, separator 122, data lines 123–138 = **16** rows. Fifteen are mutants (V1, V1b, V2, V2b, V13, V3, V3b, V5, V6, V7, V8, V9, V10, V11, V12). V0 on line 130 is the baseline real row, which the seat does not count in the fifteen (`plans/round-61.md:198` "measured 15 key-form mutants"; seat lines 140–142 and 599–600 "16 worlds (baseline + 15 mutants)").

What was executed: the committed **v2** CLI (`ca2585a4`, lines 15–16, 78, 626) plus a scratch guarded proposal (§5, lines 436–443, "a *proposal* for the v3 arm, not integrated code"). Lines 587–590: "No v3 counter existed… They are not a measurement of the integrated v3."

`5a5adc94` occurrences: **0**. `ca2585a4` occurrences: **3**.

### E2f — `wave/MutA2.md` lines 201–210 (10 cells)

The erratum (`plans/round-61.md:243`) cites **ten** invented-action cells. Those are the attack rows of the word-level table: header line 195, separator 196, four pristine controls 197–200, ten attacks 201–210 (F1, F2a, F2a-plain, F2b, F3, F3b, F4, F5, F6, W6-sib).

The end-to-end table at lines 137–144 is a **subset**: header, separator, and 6 data rows (pristine + F1, F2a, F3, F4, F6). It is not the ten. F2b, F3b, F5, and W6-sib were word-level only.

What was executed: the committed **v2** counter. Lines 447–451: "No v3 draft source was published… All measurements are against the committed v2 counter… the guard matrix is a prototype on the committed pages, not the draft's code." Counter sha printed in the transcripts is `ca2585a4…` (lines 8, 62, 98, 161, 469).

`5a5adc94` occurrences: **0**. `ca2585a4` occurrences: **10**.

## Where `5a5adc94` actually appears

Working-tree pin, read-only, not a re-score of the attacks:

```
$ sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py
5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91  verifiers/check_scoped_rules.py
EXIT:0
date -u: Fri 23 Oct 2026 08:52:54 PM UTC
```

Committed r61 files that name that prefix (full tree walk of `.ufo/waves/round-61/`; four files, 11 hits):

| file | hits | what the file scores |
|---|---|---|
| `receipts/C1-worlds.txt` | 3 (lines 6, 14, 52) | `--self-test` of synthetic W0–W7. Counted line: `worlds reject 7 of 7; eligible rows pass 4 of 4`, exit 0. One stdout line per world (lines 15–22). |
| `controls/C1-base.txt` | 1 (line 6) | `--rev f3246d14` → `0 of 4`, exit 1 (E2d: empty canonical key set). |
| `C1-v3-measure.txt` | 2 (lines 4, 7) | `--rev 43fe0180… --fetch` → `4 of 4` snapshots and `4 of 4` live, exit 0. |
| `wave/ExecCounterV3.md` | 5 (lines 4, 84, 118, 144, 313) | the draft that **is** the landed file (same sha). Its recorded runs are the same self-test and the same 4-of-4 / base commands, not the five attack tables. |

`receipts/controls-ancestry.txt` (21 lines) and `controls/C2-base.txt` (8 lines): **0** hits of the sha, **0** hits of the five seat names.

`wave/` is 66 files, 23036 lines. The sha occurs in `ExecCounterV3.md` only. The five attack seats contribute 0.

### Why `C1-worlds.txt` is not 1-of-5, or 4-of-5, or 5-of-5

It names the landed sha and it runs the landed counter. It does **not** run these attack tables. Counts inside the five committed measure files (`C1-worlds.txt`, `controls-ancestry.txt`, `C1-base.txt`, `C2-base.txt`, `C1-v3-measure.txt`):

| needle | count |
|---|---|
| `MutA1`, `MutA2`, `MutA3`, `MutA4`, `MutFixtures` | 0 each |
| `E2b`, `E2c`, `E2f` | 0 each |
| `E2e` | 1, and it is the character sequence inside the comment `errata E2-E2e` on `C1-worlds.txt:7`, not an A1-mutant score |
| `V1b`, `F2a`, `A0-alias`, `A7-declaration`, `url_key` | 0 each |
| `5a5adc94` | 6, all in the three files in the table above |

Line 7 of `C1-worlds.txt` says the worlds are "in-counter self-test worlds W0–W7 (plans/round-61.md errata E2-E2e; synthetic per ExecCounterV3 5.8)". "Synthetic" and the range stopping at E2e are in the receipt. The seven counted stdout lines are one S900-style world each:

- W1 `arm=A4` — one synthetic sha-alias line, not MutA4's 12 matrix rows or 3 seams.
- W2 `arm=A3` — one synthetic rendering-alias line, not MutA3's 19 URL rows and not MutFixtures S1.
- W5 `arm=A1` — one `patterns` key, not MutA1's 15 key-form mutants.
- W6 `arm=A2` — reject text is `action cell supports 5 of its 8 content word(s) at line 6 (need >= 6)`. That is a word-support count. It is not MutA2's ten cells, and it is not a G7 raw-tokenizer or G9 compound-purpose result.
- W3/W4/W7 are held-key, live-miss, and rescore worlds. They are not among the five errata.

The fleet r61 report (`.ufo/reports/round-61/kotoba.md`, 53 lines) names the sha twice (lines 9 and 28) and the five seats on lines 9 and 40 (10 seat-name matches, 5 per line). Line 9 attaches the sha to "drafted by wave seat ExecCounterV3 (integrated unmodified)". Line 28 attaches it to the self-test / `--fetch` / base receipts. Line 40 calls the five amendments "pre-data" attacks. None of the three lines is a re-score of the attack rows against the landed bytes.

## Commands (counts)

Census command, exit 0, `date -u` `Fri 23 Oct 2026 08:52:33 PM UTC` (the `date` line printed first; python then printed the counts below). Needles were counted with `str.count` over the five committed measure files listed above.

```
receipts: files=2 lines=74
controls: files=2 lines=23
wave: files=66 lines=23036
C1-v3-measure.txt: files=1 lines=12
r61 report kotoba.md: files=1 lines=53

5a5adc94 under .ufo/waves/round-61/:
  2  C1-v3-measure.txt
  1  controls/C1-base.txt
  3  receipts/C1-worlds.txt
  5  wave/ExecCounterV3.md

seat-name / erratum-id hits inside receipts/ + controls/ + C1-v3-measure.txt:
  only receipts/C1-worlds.txt:7  (the "errata E2-E2e" comment)
  MutA1=0 MutA2=0 MutA3=0 MutA4=0 MutFixtures=0
  E2b=0 E2c=0 E2f=0 E2e=1 (substring of that same comment)

5a5adc94 in the five seat reports: 0, 0, 0, 0, 0
ca2585a4 in the five seat reports: MutA1=3 MutA2=10 MutA3=4 MutA4=3 MutFixtures=2

attack-table data rows (pipe tables; alias matrix is a fence, counted by line):
  MutA1 121-138: 16 data rows (15 mutants + baseline V0)
  MutA2 137-144: 6 data rows (pristine + 5); word table 195-210: 14 data rows (4 pristine + 10 attacks)
  MutA3 125-145: 19 data rows
  MutA4 mode 121-131: 9; mutants 141-145: 3; alias fence 298-309: 12
  MutFixtures summary 603-615: 11 design rows (not executed)
```

Grep-tool passes that match this (same trees, same absence): `5a5adc94` under `kotoba-shokunin/.ufo/waves/round-61/` hits only the four files above; `E2b|E2c|E2e|E2f|MutA1|MutA2|MutA3|MutA4|MutFixtures` under `receipts/` hits only `C1-worlds.txt:7`; the same pattern under `controls/` and under `C1-v3-measure.txt` hits nothing.

## Not claimed

- Not claimed: that the landed counter lacks the amended arms. `ExecCounterV3.md:17` says the draft implemented errata E2, E2b, E2c, and E2d, and the self-test stdout shows some A1/A2/A3/A4 reject lines on synthetic worlds. That is a different instrument from these five tables. This census did not re-execute `--self-test` and did not read the counter source for guard presence.
- Not claimed: that scratch files `alias-matrix.txt`, `alias-seams.txt`, or `fetch-claim-scope.txt` were never written. The seat cites them. They are not in the committed receipts directory, so they are not a committed receipt.
- Not claimed: a new absorption score. Before-state only.

installs: no installs
blockers: none
Produced the C1 before-state census: 0 of 5 erratum classes have a committed arm-level receipt against landed counter sha `5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91`.
