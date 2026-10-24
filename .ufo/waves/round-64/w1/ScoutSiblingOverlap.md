# ScoutSiblingOverlap

role: scout (leaf; no subagent dispatch; read-only outside this file)
item: Sibling-overlap scan for round 64's planned new artifacts (PROVINCE.md § Adjacent). Knowledge entry `g7-span-pinning` (or similar), verifier `verifiers/check_r64_routed_repairs.py`, lesson `round-64`.
axes: **adjacency** only. This scan does not move C1's four `span_missing` arms or C2's four-check counter.
tools installed: none
date: 2026-10-24
confidence: high on the six-term corpus scan and on every file that was opened; non-text asset bodies (wav and similar) were not byte-scanned

## Question

Do any sibling corpora already hold the planned artifacts, or the lesson row `(t)` / `(t+1)` content, such that the entry, the counter, or the lesson should be rerouted?

Strict hit = the file is the same claim or the same artifact (G7 `span_missing` pinning / `g7_conjunct` arms; the r64 routed-repairs counter over the four r63 spot-check defects; kotoba lesson row `(t)`). A shared fleet phrase is not a strict hit. Every non-zero term hit and every filename near-miss below was opened.

## Scope

Home lane `kotoba-shokunin` excluded from the sibling set. Twenty sibling corpora (every `*-shokunin` directory that has `corpus/`). No `corpus/`: `kaidoku-sh2`, `mori-shokukin`, `tameshi-shokukin`. `aggregator-shokunin` is not a directory (`Path.exists()` is false).

Text walk: extensions `.md .py .txt .json .yml .yaml .toml .rst .csv .tsv .sh .html`, files at most 8 MiB, hidden directories skipped. Eleven larger text files were byte-scanned separately (audio receipt JSON and tar-diffs; game-dev-2d lstree/extracted dumps). All eleven: zero needles.

## Search

Case-sensitive Grep over the twenty `corpus/` trees, patterns `span_missing`, `g7_conjunct`, `check_r64`, `temporal mismatch`: no matches. Same tool, pattern `routed repairs`: the lowercase hits listed under candidates (it does not match a heading whose only form is `Routed repairs`). Same tool, pattern `citation freshness`: no matches. The one live line is title case `Citation freshness`.

Authoritative recount (Python, stdlib, case-folded for the two phrases, exact for the symbols), siblings only:

```text
span_missing: 0
g7_conjunct: 0
routed repairs (case-folded): 22
routed_repairs: 0
routed-repairs: 0
check_r64: 0
citation freshness (case-folded): 1
temporal mismatch (case-folded): 0
g7-span-pinning / g7_span / span-pinning / span_pinning: 0
exfiltrates credentials: 0
```

Filename walk of each sibling `verifiers/`, `corpus/knowledge/`, `corpus/lessons/`: no `check_r64*`, no `g7-span*`, no `span-pinning` / `span_pinning`.

Positive control, same counter, `kotoba-shokunin/corpus` on `*.md` / `*.py` / `*.txt`: `span_missing` 2 (`lessons/round-63.md`, `lessons/round-63-verifier-spotcheck.md`), `g7_conjunct` 1 (`lessons/round-63.md`). `check_r64` 0 in that corpus (the verifier is planned, not yet a corpus string). `temporal mismatch` 0 in that corpus; the marker is `.ufo/waves/round-63/w2/MutW2SplitClauses.md:728` ("was a **temporal mismatch** on my part"), not a sibling corpus line.

## Hit counts per lane

Counts are case-folded occurrence counts in the text walk. `files` is the number of text files read. Every other assignment term is 0 in every lane.

| lane | files | span_missing | g7_conjunct | routed repairs | check_r64 | citation freshness | temporal mismatch |
|---|---:|---:|---:|---:|---:|---:|---:|
| audio-shokunin | 18210 | 0 | 0 | 0 | 0 | 0 | 0 |
| chousa-shokunin | 253 | 0 | 0 | 0 | 0 | 0 | 0 |
| game-dev-2d-shokunin | 4179 | 0 | 0 | 0 | 0 | 0 | 0 |
| game-dev-3d-shokunin | 1091 | 0 | 0 | 0 | 0 | 0 | 0 |
| kagi-shokunin | 101 | 0 | 0 | 0 | 0 | 0 | 0 |
| kaidoku-shokunin | 1833 | 0 | 0 | 0 | 0 | 0 | 0 |
| kake-shokunin | 108 | 0 | 0 | 6 | 0 | 1 | 0 |
| kama-shokunin | 74 | 0 | 0 | 5 | 0 | 0 | 0 |
| kasegi-shokunin | 74 | 0 | 0 | 0 | 0 | 0 | 0 |
| kengaku-shokunin | 350 | 0 | 0 | 0 | 0 | 0 | 0 |
| kotodama-shokunin | 452 | 0 | 0 | 1 | 0 | 0 | 0 |
| kumitate-shokunin | 121 | 0 | 0 | 3 | 0 | 0 | 0 |
| lore-shokunin | 1859 | 0 | 0 | 0 | 0 | 0 | 0 |
| mado-shokunin | 79 | 0 | 0 | 4 | 0 | 0 | 0 |
| mori-shokunin | 129 | 0 | 0 | 1 | 0 | 0 | 0 |
| revenger-shokunin | 391 | 0 | 0 | 0 | 0 | 0 | 0 |
| souji-shokunin | 44 | 0 | 0 | 0 | 0 | 0 | 0 |
| tabi-shokunin | 2465 | 0 | 0 | 0 | 0 | 0 | 0 |
| tameshi-shokunin | 89 | 0 | 0 | 1 | 0 | 0 | 0 |
| tsukuroi-shokunin | 129 | 0 | 0 | 1 | 0 | 0 | 0 |
| siblings |  | 0 | 0 | 22 | 0 | 1 | 0 |

`routed repairs` file:count — kake `lessons/round-32.md:1`, `round-37.md:1`, `round-37-verifier-spotcheck.md:1`, `round-38.md:1`, `round-43.md:2`; kama `lessons/round-28.md:1`, `round-29.md:1`, `round-29-verifier-spotcheck.md:2`, `round-30.md:1`; kotodama `lessons/round-14.md:1`; kumitate `lessons/round-45.md:1`, `round-46.md:1`, `round-47.md:1` (heading form `Routed repairs` only); mado `lessons/round-25.md:1`, `round-25-verifier-spotcheck.md:2`, `round-26-verifier-spotcheck.md:1`; mori `lessons/round-35-verifier-spotcheck.md:1`; tameshi `lessons/round-24-verifier-spotcheck.md:1`; tsukuroi `SOURCES.md:1`.

## STRICT_HITS

**STRICT_HITS = 0.** No sibling file is the G7 pinning entry, the `check_r64_routed_repairs.py` counter, or kotoba lesson row `(t)`.

Row `(t)` lives only in `kotoba-shokunin/corpus/lessons/round-63.md:96`: the E3 G7 `span_missing` branch unpinned (4 of 6 mutants survive 219 assertions), deferred to round 64, SM5 arm must call `g7_conjunct` directly. There is no row `(t+1)` in that table (`t` is the last falsify-correction row). Neither `span_missing` nor `g7_conjunct` occurs in any sibling corpus. The C2 check-1 marker `temporal mismatch` occurs in no sibling corpus.

Verdict for all three planned artifacts: **keep** (do not reroute).

## Candidates read (string or filename), not strict

| lane | file | why it looked close | verdict |
|---|---|---|---|
| kake | `corpus/SOURCES.md:147` | Title-case `Citation freshness — S014`. C2 defect 2 is the M95 class (report names `@ 35d44b4b` while the files were committed at `8c4cefa` / `cbbee56`). | **keep.** S014 (`SOURCES.md:22`) is "own-work: freshness-sweep §paths": a citing-line ±2 window that blanks citation text before absence vocabulary. `corpus/knowledge/freshness-sweep.md:5` is "the standing-claim drift instrument" for kake's own claims. Not a committing-rev counter. Not `check_r64`. |
| kake | `corpus/lessons/round-32.md:8`, `round-37.md:112`, `round-37-verifier-spotcheck.md:129`, `round-38.md:84`, `round-43.md:7` and `:53` | Phrase `routed repairs` | **keep.** kake's own spot-check follow-ups (mutant m3, source_recheck fixtures, SCORECARD robots rows, registry arithmetic). No G7, no kotoba r63/r64 defects. |
| kama | `corpus/lessons/round-28.md:4`, `round-29.md:4`, `round-29-verifier-spotcheck.md:36` and `:70`, `round-30.md:4` | Same phrase | **keep.** kama's round-27/28/29 spot-check items (KQ38/KQ39, echo-recheck, timestamp falsifier). |
| kotodama | `corpus/lessons/round-14.md:1` | Title contains `routed repairs` | **keep.** "gate-keeper survey: receipt preservation, routed repairs, retrospective" for kotodama rounds 8–12. |
| kotodama | `corpus/lessons/round-64.md:1-20` | Same lesson filename the round plans | **keep.** Kotodama's own round 64 (base `ff30a205`, 2026-10-23): linguistics entry `language-socialization-and-acquisition.md`, predicates `ACCEPT-C-64` / `ACCEPT-O-64` / `ACCEPT-CA-64`, their closure defects 1–4 and 7–10. Zero of the six needles. Not row `(t)`. |
| kumitate | `corpus/lessons/round-45.md:89`, `round-46.md:64`, `round-47.md:64` | Headings `Routed repairs (round-4N …)` | **keep.** Kumitate R44–R46 dispositions (QUALITY Q30/Q33/Q35, SCORECARD "13 rows were rewritten, not 15"). |
| mado | `corpus/lessons/round-25.md:25`, `round-25-verifier-spotcheck.md:185`, `round-26-verifier-spotcheck.md:189` | Phrase, including "5 of 6 routed repairs closed" | **keep.** mado Hyprland/Q36 receipt repairs. |
| mori | `corpus/lessons/round-35-verifier-spotcheck.md:76` | `### Round-34 routed repairs` | **keep.** mori's own r34 §6 items, re-judged by MoriR35Repairs. |
| tameshi | `corpus/lessons/round-24-verifier-spotcheck.md:30` | "Not eleven independent trials or eleven historical routed repairs." | **keep.** tameshi's frozen-counter bound on their K1–K11 receipt. Nearest province, not an owner: kotoba `PROVINCE.md` § Adjacent classes tameshi `adjacent` because tameshi owns the fixture/mutation method and "every lane's gate remains its own". This corpus has no `span_missing`, `g7_conjunct`, or `check_r64`. The four arms stay a mutation of kotoba's gate. |
| tsukuroi | `corpus/SOURCES.md:258` | "support the routed repairs?" | **keep.** Round-20 curation of tsukuroi's own object-identity/audit-map corrections (S077–S080). |
| chousa | `corpus/knowledge/long-span-argv-r34.md:1`, `corpus/lessons/2026-10-15-claims-span-fidelity.md:1`, `corpus/fixtures/archives-r9/controls/A-r9-span-not-found.md:1` | Filename contains `span` (the six terms are absent) | **keep.** chousa's research-gate: `tok_span_at` vs `MAX_ARG_STRLEN` / PCRE2, claim-span fidelity, and a negative control whose one span ("four" to "five") is absent from archive A. Not a backticked-span guard on scoped-rule Action cells, not `g7_conjunct`. |
| audio | `corpus/live/r79-boundary/r79b-g7.json:2` and `g7*.wav` names | Filename `g7` | **keep.** `"group": "g7-self-binding"` — PipeWire sink/capture probes. Homonym. |
| audio | `corpus/live/r65-boundary/…/coll_gsrt_g726.wav*` | Filename contains `g7` as a substring of `g726` | **keep.** Codec probe logs. Not read as text; the name is G.726, not guard G7. |

## Claims

Supports the plan's expected adjacency result. Does not falsify C1 or C2.

- **C1 keep.** No sibling corpus names `span_missing`, `g7_conjunct`, `g7-span-pinning`, or `exfiltrates credentials`. The entry stays kotoba's.
- **C2 keep.** No sibling corpus names `check_r64` or `temporal mismatch`. The 22 `routed repairs` lines and kake's `Citation freshness` line are other lanes' own instruments. The counter stays kotoba's.
- **Lesson keep.** Row `(t)` is only `corpus/lessons/round-63.md:96`. Kotodama `corpus/lessons/round-64.md` is that lane's lesson. Do not treat the shared filename as an overlap.

## Unknowns

- Non-text bodies under `audio-shokunin/corpus` and `game-dev-*-shokunin/corpus` (wav and other assets) were not scanned. Filename hits that contain `g7` were classified from the names and from `r79b-g7.json`'s `group` field.
- Sibling `.ufo/` trees and verifier bodies (beyond filenames under `verifiers/`) were not grepped. The assignment's root is `*/corpus`. A sibling could still mention the four r63 defects in a wave report. [INFERENCE] That would be a citation of kotoba's open item, not ownership of the entry or the counter; it was not checked here.
- `check_r64_routed_repairs.py` does not exist yet in kotoba either (corpus control count 0). Absence in siblings cannot collide with a file that has not been added.
