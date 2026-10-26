# R75Facet64 — the aggregate sentence over the description-thresholds table

Seat `R75Facet64` (leaf; read-only; no delegation, no edits, no live fetch, no installs, no git/jj mutation).
Measured revision: `65a5c7a663249e0522cc49e4a148424200d9ddfe` (`git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD`;
`git log -1 --format='%H %ci'` → `2026-10-26 09:05:54 -0300`). Lane tree untouched by this seat; at measurement
`git status --porcelain` showed only the pre-existing untracked `.ufo/waves/round-75/` (and a sibling seat's
`corpus/lessons/round-75.md`, not mine).

Named axes: **calibration** (does the sentence's credit line measure what the sentence asserts), **depth**
(a reader acting on the sentence gets an unqualified count) and **freshness** (the basis is a 2026-10-22
live read with no committed page bytes). No claim about operability, adjacency or consistency.

Distinct from `w1/R75Facet49.md` (that seat audits the **Gemini CLI row**, `SKILL.md:174`, and its code-level
negative). This seat audits the **one sentence above the table** and the counter floor behind it.

## Facet under audit

`SKILL.md:166`, the paragraph between the heading `### Description thresholds by client` (`SKILL.md:164`) and
the seven-client table (`SKILL.md:168-176`):

> A documented maximum is not a render cut: four clients state 1,024 and none documents a cut there, Claude
> Code and Codex cut or budget the listing, omp cuts at 99 (§ Router model). Basis:
> `corpus/knowledge/skill-listing-thresholds-round54.md` (S053–S059, S062–S064), checked by
> `verifiers/check_description_thresholds.py`.

Three claims and one credit: (i) the count **four clients state 1,024**; (ii) the negative **none documents
a cut there**; (iii) the two cut/budget facts (Claude Code, Codex) and omp's 99; (iv) **checked by**
`verifiers/check_description_thresholds.py`.

## Observed (committed bytes)

| # | observation | evidence |
|---|---|---|
| O1 | The sentence is original to round 54 and unchanged since: one commit ever introduced the phrase. | `git log --oneline -S'four clients state 1,024' -- SKILL.md` → `5a097e1` only; `git blame -L 166,166 --date=short -- SKILL.md` → `5a097e1 (kotoba-shokunin 2026-10-22 …)`; `git log -1 --format='%h %ci %s' 5a097e1` → `5a097e1 2026-10-22 18:38:22 -0300 round-54: C1 — description thresholds by client…` |
| O2 | The count is true of the table at HEAD: exactly four of the seven `Documented threshold` cells state 1024. | parse of `SKILL.md:164-176` (cells split on `\|`): `VS Code` `:172` "maximum 1024 characters", `Copilot CLI` `:173` "max 1024 characters", `Cursor` `:175` "1,024 characters", `opencode` `:176` "1-1024 characters (v1 docs page; the v2 page says it enforces no maximum)" → 4 rows; Claude Code `1,536`, Codex `2%…8,000`, Gemini `~100 words` → none |
| O3 | The entry supports the count in prose on four tier-A rows, and scopes the count to "their pages". | `corpus/knowledge/skill-listing-thresholds-round54.md:15-19` — "**An authoring maximum is not a render cut.** Four clients document 1,024 characters for `description` (VS Code S055, Copilot CLI S056, Cursor S058, opencode S059 as `1-1024`). None of their pages documents a cut at that number." |
| O4 | The credited counter **never reads the value 1024** and never prints a count of clients stating it. | `grep -c '1024' verifiers/check_description_thresholds.py` → `0`. Its printed quantities: `description thresholds backed %d of %d clients` (`:509`) and exit on `value >= TARGET` (`:514`) with `TARGET = 4` (`:83`). It reads the threshold cell only for **number tokens** to match against the entry quote (`:281`, `:323`). |
| O5 | The counter's own docstring disclaims exactly the clause (ii) judgement and the reading behind it. | `verifiers/check_description_thresholds.py:46-48`: "The counter does not judge whether the number is a render cut, a budget or an authoring maximum: that reading is the entry's and the reviewer's, not a check this file runs (Q31)." |
| O6 | The round-54 plan's frozen C1 statement is a **floor**, not this count, and it names the same not-measured list. | `plans/round-54.md:24-26` — statement is "`description thresholds backed 4 of 7 clients` **or more** and exits 0"; `:34-36` — "What the counter does not measure: whether a number is a render cut, a listing budget or an authoring maximum (entry and reviewer reading, Q31)…" |
| O7 | Mutant **M1** (the sentence's count falsified, `four`→`seven`, nothing else changed) leaves the credited counter green. | scratch copy via `git -C <lane> archive HEAD \| tar -x -C tree`; `sed -i 's/four clients state 1,024/seven clients state 1,024/' tree/SKILL.md`; `python3 -B tree/verifiers/check_description_thresholds.py --root tree` → `description thresholds backed 7 of 7 clients`, **rc 0** |
| O8 | Mutant **M2** (one of the four 1024 rows falsified: `VS Code` `1024`→`1,536`, entry row left contradicting it) is still green under the floor. | `sed -i 's/\| VS Code \| `description` maximum 1024 characters/\| VS Code \| `description` maximum 1,536 characters/' tree/SKILL.md`; counter → `VS Code      no quote holds none of the threshold numbers ['1,536', '64']` · `description thresholds backed 6 of 7 clients`, **rc 0**. Only three clients then state 1,024, and the SKILL.md cell contradicts `corpus/knowledge/skill-listing-thresholds-round54.md:42`'s quote "Maximum 1024 characters." |
| O9 | Mutants **M3** (sentence deleted) and **M4** (negative inverted: "and each documents a cut there") also leave it green. | M3: `sed -i '/^A documented maximum is not a render cut:/d' tree/SKILL.md` → `7 of 7`, rc 0. M4: `sed -i 's/and none documents a cut there/and each documents a cut there/'` → `7 of 7`, rc 0. |
| O10 | The counter's only page check is quote presence, not bytes: the recorded fetch hashes are never compared. | docstring `:50-53` and code `:495-496` (`found = norm(r["quote"]) in page`) under `--fetch`; no sha256 read anywhere (`grep -n 'sha256\|hashlib' verifiers/check_description_thresholds.py` → no match). A page that adds a truncation sentence while keeping the quoted cap line would pass. |
| O11 | None of the four pages (nor the other three) exists as committed bytes; the fetch record is per-page sha256 in the round-54 lesson, and one of the four is truncated to 8 hex in **both** places. | `git ls-files '.ufo/waves/*/snapshots/*' \| wc -l` → `149` (rounds 59–74); `ls .ufo/waves/round-54/` → `build/`, `falsify/` and dispatch files only, no `snapshots/`. `corpus/lessons/round-54.md:25,26,28` carry full 64-hex hashes for S055, S056, S058; `:29` carries `f10ced73971c…` for S059, and `corpus/SOURCES.md:72` repeats the same 8-hex truncation (`sha256 `f10ced73…``). |
| O12 | The sentence is the only SKILL.md line that names this counter outside the Gate registry, and the registry row itself reports the network surface. | `grep -n 'description_thresholds' SKILL.md` → `:166` and `:464`; `:464` — "`gate` · … · `--self-test` · in-file · none; `--fetch` reads the network". |
| O13 | The basis entry carries no provenance trio, and the lane's trio gate does not cover it. | `grep -n 'recheck\|verified-at\|^source:' corpus/knowledge/skill-listing-thresholds-round54.md` → only the prose sentence at `:31`; `verifiers/check_author_rules.py:485-488` pins four entries (`round-67`…`round-72`), not this one. Row-level cadence exists: `corpus/SOURCES.md` S053–S059 `recheck` = `90d`. |

## Assessment

**Factual support — holds, on a narrower scope than the sentence states.** O2 and O3: four rows, four tier-A
rows, quotes recorded in `corpus/lessons/round-54.md:23-29`. The count is not invented and is re-derivable by
hand from committed bytes. `[INFERENCE]` I cannot say the pages still say it today: no page bytes are committed
(O11) and this seat is barred from live fetch.

**Scope — the population is unstated and two qualifiers are dropped.** The "four" is a count over the **seven
table rows**, yet the sentence reads as a statement about clients in general; `SKILL.md:162` separately credits
the **spec** (`corpus/SOURCES.md` S018) with the same 1,024 floor, so a reader counting "clients that state
1,024" from the file's own authorities can reach five. The `opencode` cell qualifies its 1-1024 to the **v1**
page and records that v2 "enforces no maximum" (`SKILL.md:176`); the sentence drops that qualifier while keeping
the client in the four. Both are wording, not data, faults — but they are what a description audit would trip on.

**Falsifiability — the credit line is false for two of the sentence's three claims.** The sentence says
"checked by `verifiers/check_description_thresholds.py`". O4/O5/O6 and mutants M1–M4 show the counter reads
neither the 1,024 value, nor the count, nor the negative; deleting the sentence leaves it green. The sentence's
credit is therefore a Q31 defect ("prose that describes what a counter checks names only the cells and tests its
code reads; a check the counter does not run is named as reviewer judgment") and a Q26 defect for the count
clause ("a clause neither turns on is dropped from the statement or the statement is bounded"). Mutant **M2** is
the sharper case: the credited gate exits 0 in a world where the sentence is already false and one SKILL.md cell
contradicts its own entry quote.

**Control weakness — the floor, not the count, is what is green.** `TARGET = 4` (`:83`) was frozen in round 54
as a plan floor (`plans/round-54.md:26`), not as the sentence's count; today the counter prints 7 of 7 and would
still exit 0 with three clients unbacked, or with a column's contents falsified (M2). The two numbers "4" are
coincident and unrelated, which is precisely how a green gate gets mistaken for support for the sentence.

**Freshness — live-only page evidence, five days old at the measured revision.** Opened 2026-10-22, measured
2026-10-26: no committed snapshot (O11), no hash comparison in the gate (O10), no `verified-at`/`recheck` on the
entry (O13). Row cadence is `90d`, so nothing forces a re-read before mid-January even though S059's own note
says opencode's v2 page changed the rule and `recheck: on-release` applies only to S062/S064.

## Concrete check and control (proposal, not landed)

New second measurement, never an edit to the frozen counter (Q28):

```
python3 -B verifiers/check_description_threshold_count.py --rev <rev>
  -> prints "description threshold rows stating 1,024: N of 7" and "cell/row contradictions: C", exit 0 iff N == 4 and C == 0
```

Rule: a row counts iff the **first** number token of its `Documented threshold` cell is `1024`/`1,024`, or its
first token is a range whose upper bound is 1024 (the `opencode` form); the row must also carry the v1/v2
qualifier that its entry reading states. A row whose cell number differs from the number in its entry quote
counts as a contradiction `C`.

Must-fail arms (each already exercised as a scratch world, so the arms are known to be reachable):

| arm | world (all run on the scratch copy) | required result |
|---|---|---|
| a1 | `VS Code` cell `1024`→`1,536` (M2 world) | `N = 3`, `C = 1`, exit 1 — today's gate: `6 of 7`, rc 0 |
| a2 | `four`→`seven` (M1) | unchanged `N = 4`, but the sentence/credit guard must go red: the sentence must cite the count guard, and the count guard must read the sentence's number (a `headline` arm: `grep -c 'four clients state 1,024'` = 1 **and** N = 4) |
| a3 | a fifth row also stating 1,024 | `N = 5`, exit 1 (pins the set; does not accept "≥ 4") |
| a4 | cell text "not 1024, see S018" | must not count (token must be the threshold's first number) |
| a5 | sentence deleted (M3) | headline arm exit 1 (the sentence is part of the claim surface, not optional) |
| a6 | negative inverted (M4) | the negative is **not** machine-checkable from quotes; assign it to a named non-author reviewer, and require the entry to carry its sweep (Q14/Q30: the four pages' changelog/release notes, the current docs tree, and a lane-corpus grep) with the command printed |

Two supporting controls, both cheap:
1. **Byte pin.** Commit snapshots for S055, S056, S058, S059 (rounds 59–74 set the pattern, `149` files) or
   record full 64-hex hashes: S059's is 8 hex in `corpus/lessons/round-54.md:29` and `corpus/SOURCES.md:72`, so
   even the non-snapshot drift check cannot run for the one page whose rule already changed between v1 and v2.
2. **Credit-line bound.** Either the sentence drops "checked by …" for clauses (i)–(ii) and names the count
   guard plus the reviewer seat, or the counter's docstring and registry row (`SKILL.md:464`) gain the count
   clause and print it. Today the sentence's credit and the counter's printed line disagree by construction.

## Risks and limits

- Raising `TARGET` 4→7 edits a frozen judgment table; that must be a **new** measurement in a new counter, with
  the old floor disclosed, or it repeats M35/Q28. My `a3` arm is designed to pin the set, not to widen a target.
- The count is table-scoped and can legitimately change (a vendor page edit, a new client row). The guard must
  therefore pin the seven-row population in the plan and read it from `--rev` bytes, not from a repo-global sweep.
- The negative (ii) is not decidable from committed quotes. Any "closed" form of this facet requires the
  snapshots plus a named reviewer; a quote-presence `--fetch` (today's mechanism) cannot falsify it.
- This seat did not fetch pages, so every freshness statement above is about committed bytes and recorded
  hashes; what the pages say **now** is unmeasured here.
- Mutant worlds live only in `/fast/scratch/hyaku/kotoba-r75/R75Facet64/` and are removed on exit; their exact
  commands and outputs are inlined in O7–O9 so the wave can reproduce them from `git archive HEAD`.

Report: .ufo/waves/round-75/w1/R75Facet64.md
