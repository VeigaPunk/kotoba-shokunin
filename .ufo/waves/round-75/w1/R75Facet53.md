---
seat: R75Facet53
round: 75
lane: kotoba
mode: read-only research (no lane edit, no commit, no spawn)
measured-at: 2026-10-27
lane-tip: 65a5c7a663249e0522cc49e4a148424200d9ddfe
---

# Facet 53 — `SKILL.md:166` credits the whole description-threshold table to a counter that reads one column of it

## The rule under audit (verbatim, `SKILL.md:166`)

> A documented maximum is not a render cut: four clients state 1,024 and none documents a cut there, Claude Code and Codex cut or budget the listing, omp cuts at 99 (§ Router model). Basis: `corpus/knowledge/skill-listing-thresholds-round54.md` (S053–S059, S062–S064), **checked by `verifiers/check_description_thresholds.py`**.

The row text itself is sound; I checked the one I expected to be weakest (`SKILL.md:176`, opencode) against its receipts and it holds. What does **not** hold is the word "checked": the counter reads two of the table's four columns and one token of one entry column, and the token test is satisfied by any number that shares a digit with the cell.

## Observation, with exact evidence

| # | observation | evidence (observed) |
|---|---|---|
| O1 | The five-column table exists at `SKILL.md:168-176`; `SKILL.md:166` names the counter as its check. | `grep -n "Description thresholds by client" -A 14 SKILL.md` |
| O2 | The counter reads, per client: `sr[1]` (threshold cell) for numbers, `sr[3]` (action cell) for **non-emptiness only**. `sr[2]` — the whole *Past the threshold* column — is never read; the entry's `reading` column (`r[4]`) is never read. | `verifiers/check_description_thresholds.py:297-330`; the only two `sr` uses are `tokens = NUM_RE.findall(sr[1])` and `if clean(sr[3]) in ("", "-", "—", "–")` |
| O3 | The number conjunct is **any-token**: `if tokens and not has_token(quote, tokens)`. `has_token` returns true on the first matching token of the cell's number list. | `:245-250` (`has_token`), `:323` (conjunct), `:109` (`NUM_RE`) |
| O4 | The number list is extracted from the *whole* cell, so version labels and a cell's second threshold enter it. Measured token lists: opencode `['1','1024','1','2']` (the trailing `1`,`2` are `v1`/`v2`); Claude Code `['1,536','1%','0.01']`. | in-memory rejudge of the committed bytes at the tip (script below) |
| O5 | The gate exits 0 at **4** backed clients but prints "of 7": `TARGET = 4`, `len(CLIENTS) = 7`, exit rule `value >= TARGET`. | `:83`, `:86`, `:509`, `:514`; plan froze it: `plans/round-54.md:26` ("`backed 4 of 7 clients` or more and exits 0") |
| O6 | Today's honest world is 7 of 7, exit 0. | `python3 -B verifiers/check_description_thresholds.py --rev 65a5c7a6…` → `description thresholds backed 7 of 7 clients`, exit 0 |
| O7 | The registry's declared entry command carries no `--fetch`; `value = found` (page-byte conjunct) only when `--fetch` is passed, and even then the exit rule is `found >= 4`. | `SKILL.md:464`; `:511-516` |
| O8 | The entry's Limits disclose "does not check that the number is about `description`" — but not that the number test is any-token, nor that version labels feed it. | `corpus/knowledge/skill-listing-thresholds-round54.md:62-67` |
| O9 | The round-54 mutation receipt probed 15 arms; none removes the claimed number while leaving another number of the same cell in the quote. The receipt's own line numbers predate the r56 shift (`:220` there = `:245` now). | `.ufo/waves/round-54/build/MutDescThresholds.md` § Mutation outputs |
| O10 | Counter bytes unchanged since round 56, so the finding is live at the tip; instrument sha256 `15fdf83b…` from `git show <tip>:verifiers/check_description_thresholds.py \| sha256sum` equals `sha256sum verifiers/check_description_thresholds.py`. | `git log --oneline -1 -- verifiers/check_description_thresholds.py` → `250e302` |

## Two falsifier worlds, measured (not inferred)

Both worlds take the **committed bytes at the tip** and change only the entry's quote cell plus the matching `## Gate` row in `corpus/lessons/round-54.md` (the counter requires the quote to be recorded there, so a self-consistent wrong row is the realistic shortcut). The counter then reports **7 of 7, exit 0** in both.

- **W1 — a different number of the same cell.** Claude Code's quote (`"…truncated at 1,536 characters in the skill listing"`) is replaced by the cell's other fact, `"past a listing budget of 1% of the context window"` (10 words, within bounds). Result: `Claude Code present: True`, backed 7. The row's claimed per-entry cap is not in the quote, but `1%` is in the token list.
- **W2 — a version label plus the wrong field.** opencode's quote (`"`description` must be 1-1024 characters."`) is replaced by S064's own sentence about **`name`**: `"V2 currently does not enforce this pattern, the 1–64 character recommendation, or a maximum description length."` (17 words). Result: `opencode present: True`, backed 7 — the `1` of `1–64` matches the `1` that the cell's `v1` label contributes to its token list.

Replay (read-only; no lane write):

```bash
python3 -B - <<'PY'
import importlib.util, subprocess
LANE="/home/vgpnk/Projects/shokunin/kotoba-shokunin"; REV="65a5c7a663249e0522cc49e4a148424200d9ddfe"
spec=importlib.util.spec_from_file_location("cdt", LANE+"/verifiers/check_description_thresholds.py")
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
show=lambda p: subprocess.run(["git","-C",LANE,"show","%s:%s"%(REV,p)],capture_output=True,text=True,check=True).stdout
sk,en,so,le=show("SKILL.md"),show(m.ENTRY),show(m.SOURCES),show(m.LESSON)
old1='"the combined `description` and `when_to_use` text is truncated at 1,536 characters in the skill listing"'
old2='"`description` must be 1-1024 characters."'
def world(o,n):
    print(n, "->", [r["client"] for r in m.judge(sk, en.replace(o,n), so, le.replace(o,n)) if r["backed"]])
world(old1,'"past a listing budget of 1% of the context window"')
world(old2,'"V2 currently does not enforce this pattern, the 1\u201364 character recommendation, or a maximum description length."')
PY
```

Observed output: both lists contain all seven clients.

## Why this matters for a round-75 description-audit claim

A description audit is likely to say something of the form "the per-client `description` limits in `SKILL.md` are machine-backed". Three separable clauses would go into that headline, and only one is carried:

| clause | carried by the counter? |
|---|---|
| a table row exists per client with a number and a non-empty action | yes (`:309-318`) |
| the quote supports **that row's** claimed number | **no** — any cell token (W1) |
| the row's *Past the threshold* claim (the part an author acts on) | **no** — column never read (O2) |
| the number is about `description` and present on the page | no at gate time (no `--fetch` in the registry command, O7); disclosed at entry `:64-65` |

So a r75 claim may cite the counter for **row existence, source-row metadata and quote provenance**, and must say so; it may not cite it for "the seven thresholds are correct". Both halves are cheap to state, which is the point of the facet.

## Concrete control (costs nothing on today's honest world)

Freeze a **primary token per client** and require that one, after masking version labels. Measured: every one of the seven current quotes already contains its primary token, so the tightened rule still reads **7 of 7** on honest bytes.

| client | primary token | present in today's quote |
|---|---|---|
| Claude Code | `1,536` | yes |
| Codex | `2%` | yes |
| VS Code | `1024` | yes |
| Copilot CLI | `1024` | yes |
| Gemini CLI | `100` | yes |
| Cursor | `1,024` | yes |
| opencode | `1024` | yes |

Implementation sketch for a **successor** counter or a committed control file (the frozen counter must not be edited — QUALITY Q28/Q73: a frozen counter's judgment table is not widened after the fact):

1. `PRIMARY = {"Claude Code":"1,536", …}`; require `has_token(quote, [PRIMARY[client]])` instead of the whole cell list.
2. Mask version labels before extraction: `NUM_RE.findall(re.sub(r"\bv\d+(?:\.\d+)*\b", " ", cell))` — kills the `v1`/`v2` digits that supply `1` and `2` today.
3. Two must-fail arms, exactly W1 and W2 above, asserting the named client is **absent** from the backed list (the existing self-test has no such arm: `MutDescThresholds.md` rows 9 and the added patch arms cover token weakening, word count, kind, heading case and `TARGET`, not a same-cell different-number quote).
4. Two must-pass arms: honest tip backs 7 of 7; `TARGET` printed as 7 (or the claim text bounded to `4 of 7`).
5. If the claim needs page bytes: run `--fetch` and commit a receipt with `description thresholds found on the live page 7 of 7` — the declared gate command does not do this, and `--fetch` still exits 0 at `found >= 4` (`:515-516`).

## Risks and limits of this facet

- **Scope of the falsifiers.** W1/W2 mutate two lane files together (entry quote + Gate row). They model a seat that writes a wrong-but-self-consistent row, not a one-file adversarial edit; a reviewer may call them weaker than a pure single-file shortcut. They are still cheaper than fabricated input and pass the frozen predicate, which is the Q37 test.
- **No live fetch.** Per the seat boundary I did not fetch any page, so I make no claim about web bytes; W2's sentence is quoted from the lane's own committed Gate record (`corpus/lessons/round-54.md:34`) and `Srcopencode.md:18`, not from a fetch I ran.
- **In-memory rejudge.** The two worlds were judged by importing the committed counter module and calling `judge()`; the module sha256 matches the committed file, and `main()` was also run directly at the tip (O6). I did not build a git sandbox, so the worlds are not commit-shaped receipts — a r75 build that wants one must construct them as files.
- **Prose is not the defect.** The opencode row's own three claims hold at their receipts (S059 quote at Gate `:29`; S064 at `:34`; code tags `v1.19.4 148842ef…` / `v2.1.3 bb25a2f4…` at `.ufo/waves/round-54/build/Srcopencode.md:22-26`), and the round-54 falsify seat's one BREAKS on that row's Action cell (`.ufo/waves/round-54/falsify/W2Srcopencode.md:5`) was corrected in `cae8f2e` and summarised at fleet report `round-54/kotoba.md:77` ("three over-wide C1 cells corrected before closure") — the correction is recorded, though by aggregate, and it carries no counter arm (the action-cell test is non-emptiness only). That last point is the same weakness as O2, not a second defect.

## Status

No files edited; no commits; no spawns; no installs. Scratch `/fast/scratch/hyaku/kotoba-r75/R75Facet53/` used for the four probes and removed on exit. Verified against committed bytes at lane tip `65a5c7a663249e0522cc49e4a148424200d9ddfe` on 2026-10-27. All readings used `git show <rev>:<path>`, so the untracked `corpus/lessons/round-75.md` that appeared in the working tree during this wave (a sibling seat's output, not mine) cannot affect them.
