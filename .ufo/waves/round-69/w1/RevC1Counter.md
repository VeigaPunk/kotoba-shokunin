# RevC1Counter — attack on `verifiers/check_skill_precedence.py` (C1)

Seat: `L1Kotoba69-2.RevC1Counter` · round 69 wave 1 · leaf member, no subagent dispatch.
Target: the committed frozen counter, `a238989:verifiers/check_skill_precedence.py`,
sha256 `9c796574c2d588f27869e0e14289c1be8f0b3f3e56f785d68eb64ee5e756da48` (working-tree
copy byte-identical — no drift between freeze and attack).

Sandbox: `git clone --shared` at `/tmp/c1-sandbox` (committed state, tip
`a238989a96cb0d2b939679126b832d75b861ca6e`), and `/tmp/c1-work` (read-only rsync of
`corpus/` + `verifiers/`, i.e. the L1 content draft at 07:08). Mutation worlds under
`/tmp/c1-attack/<name>/`; every check executed outside the lane. Lane left untouched:
`git -C …/kotoba-shokunin status --porcelain | wc -l` = 42 before and after,
`rev-parse master` = `a238989…`, no write to the lane index, jj state or working tree except
this report. No tool installs were needed.

## Reproduced controls (all hold)

| control | command | observed |
|---|---|---|
| base | `python3 -B verifiers/check_skill_precedence.py --rev a5f7459f99bb27bf697e9438362e75ac5833eca8` | `measured-rev: a5f7459…` / `skill precedence backed 0 of 5` / `- entry missing: corpus/knowledge/skill-name-precedence-round69.md` / exit **1** |
| committed tip | `… --rev a238989a96cb0d2b939679126b832d75b861ca6e` | `skill precedence backed 0 of 5` / exit **1** (entry not committed yet) |
| unknown rev | `… --rev deadbeef…` | `environment error: unknown revision …` / exit **2** |
| self-test on draft | `cd /tmp/c1-work && … --self-test` | 18 PASS lines, `self-test: 0 failure(s) over 18 assertions`, exit **0** |
| honest draft | `… --repo /tmp/c1-work` | `skill precedence backed 5 of 5`, exit **0** |
| fetch arm | `… --fetch` (working tree) | `fetch S203..S207: found`, `live quotes found 5 of 5`, exit **0**, 3.5 s |
| junk control (reconstructed) | junk provenance trio + quote + index row | `skill precedence backed 0 of 5`, `- the entry does not open with 'source:' lines naming S### ids`, exit **1** — matches `controls/C1-junk-control.txt` |

The honest 5/5 is **content-earned**, verified without the counter's parser: each of S203–S207
is an 11-cell `mined` row opened `2026-10-25`, `used-by` names the entry, its claim quote is
present both in the entry and verbatim in the row's anchor, each id has one 4-cell table row,
the five clients are `Roo Code / Amp / Deep Code / Junie / opencode`, and the README coverage row
has the entry path in column 2.

## Findings (severity order)

### F1 — HIGH: a row with an empty **rule** cell scores 5/5

Frozen contract (plan C1 and the counter docstring §6): “exactly one per-client table row per id
carries that quote **with a client and a rule cell**”. `check()` never reads the table header; it
hard-checks positions 0 and 1 only (`verifiers/check_skill_precedence.py:226`), and matches the
quote anywhere in the row (`:229`). Move the quote into cell 1 and blank cell 2 — the row still
satisfies both tests.

```
python3 -B verifiers/check_skill_precedence.py --repo /tmp/c1-attack/M3-empty-rule
measured-rev: working-tree
skill precedence backed 5 of 5
exit=0
```
World: each table row rewritten `| <client> | "<quote>" | | <sid> |`. The entry's own header
still says column 2 is `located quote` and column 3 the rule — so “rule cell filled” is false and
the quote cell is empty, yet the counter passes. The self-test has no world for an empty
client/rule cell, so “one broken world per conjunct” does not cover this conjunct’s weakest leg.

### F2 — HIGH: the “five distinct clients” check is vacuous when the client cell holds the id

`clients.append(cells[0].lower())` (`:232`) assumes cell 0 is a client name and never validates
it. Put the id in cell 0 and the distinctness test collapses to “five distinct ids”, which is
guaranteed by provenance.

```
python3 -B verifiers/check_skill_precedence.py --repo /tmp/c1-attack/M2-client-is-id
skill precedence backed 5 of 5
exit=0
```
World: `| S203 | <rule> | "<quote>" | S203 |` … `| S207 | … |`. No row names a client; the
contract’s “the five table rows name five distinct clients” is violated and the counter cannot
see it.

### F3 — HIGH: `--self-test` crashes (exit 1) on partial states, cannot be rev-pinned, and is unverifiable at the committed tip

`selftest()` assumes the working tree is already a *complete* honest world before it can build any
broken world (`:313` `first = next(iter(src))`; `:315` `row = rows[first]`), and `main()` returns
`selftest(repo)` before revision resolution (`:380`).

* Entry present, registry rows not yet appended (exactly the build order this round):
  ```
  python3 -B verifiers/check_skill_precedence.py --repo /tmp/c1-attack/M15-entry-only --self-test
  File "…/check_skill_precedence.py", line 315, in selftest
      row = rows[first]
  KeyError: 'S203'
  exit=1
  ```
  `check()` on the same world is clean (`backed 0 of 5`, five `no 11-cell row` findings, exit 1):
  the crash is confined to the self-test.
* Junk entry (no `source:` lines): `StopIteration` at `:313`, exit 1.
* Uncaught Python exceptions exit **1**, the same code as a content verdict — a crash is not
  distinguishable from `0 of 5` by exit code, and neither is exit 2 as the docstring’s
  environment classification requires.
* At the frozen tip `--self-test` exits **2** (`selftest setup failed: the entry is not present in
  the working tree`) because the entry is uncommitted; and `--self-test --rev a5f7459…` from the
  draft tree still runs 18 assertions against the *working tree*, exit 0 — `--rev` is silently
  dropped. So the plan’s self-test conjunct is not reproducible from `--rev <tip>`; it only exists
  against the uncommitted draft.

### F4 — MEDIUM: the coverage-map index check is context-blind

`_indexed()` (`:169–174`) accepts **any** README line whose second cell equals the needle. In
`/tmp/c1-attack/M16-junk-index-row` the real coverage-map row is deleted and replaced by
`| superseded by round 70 | 'knowledge/skill-name-precedence-round69.md' | not coverage |` under a
new `## Removed entries` heading:

```
python3 -B verifiers/check_skill_precedence.py --repo /tmp/c1-attack/M16-junk-index-row
skill precedence backed 5 of 5
exit=0
```
`M8-index-removed-row` (same row, first cell rewritten to `REMOVED — superseded, not coverage`)
also yields `5 of 5`. Contract: “the entry is indexed in the coverage map” — neither world has a
coverage-map row. The check never verifies the table, section or round cell.

### F5 — MEDIUM: the located quote is chosen by a **global longest-character match**, producing both false positives and false negatives

`quotes = _quoted(_norm(entry))` takes every double-quoted ≤25-word span in the whole entry
(source lines, table, prose, Limits section); `_row_quote` (`:178–181`) returns
`max(matched, key=len)` — longest by **characters**, not words, and not tied to the `located
quote` field or the table’s quote column.

* False positive: replace Deep Code’s claim with the anchor’s own section title
  `"Scan Locations"` → `5 of 5`. A section name, not a rule, backs the client.
  ```
  python3 -B verifiers/check_skill_precedence.py --repo /tmp/c1-attack/M5-title-quote
  skill precedence backed 5 of 5
  ```
* False negative: a row whose source line **and** table row both carry a short quote that *is*
  in the anchor (`"Override Control"`) is rejected because a longer heading phrase already quoted
  in the entry’s Limits prose (`"Roo-specific (higher priority)"`, 29 chars) wins the match:
  ```
  python3 -B verifiers/check_skill_precedence.py --repo /tmp/c1-attack/M12-short-claim-hijack
  skill precedence backed 0 of 5
    - S203: the per-client table row does not carry the located quote
  exit=1
  ```
  (`M7-section-titles` shows the same hijack: S203’s row carries its own title but the counter
  demands the Limits-prose heading.) Verdicts therefore depend on unrelated text elsewhere in the
  entry — a determinism defect, not only a permissiveness one.

### F6 — MEDIUM: conjunct 4 is a vacuous substring test

`if row[1] not in tail` (`:216`) is satisfied by an empty source cell, and by any trivial prefix.
With S205’s `source` cell blank, or set to the single letter `a`:

```
python3 -B verifiers/check_skill_precedence.py --repo /tmp/c1-attack/M13-empty-source-cell   → 5 of 5, exit 0
python3 -B verifiers/check_skill_precedence.py --repo /tmp/c1-attack/M14-trivial-source-cell → 5 of 5, exit 0
```
A registry row that no longer names its source still backs the id. The test needs a non-empty
cell and, better, equality or exact-URL matching rather than `in`.

### F7 — MEDIUM: a one-character “quote” backs all five ids, and `--fetch` confirms it

Replace every double-quoted span in the entry with `"a"`:

```
python3 -B verifiers/check_skill_precedence.py --repo /tmp/c1-attack/M1-one-char-quote --fetch
skill precedence backed 5 of 5
  fetch S203..S207: found
live quotes found 5 of 5
exit=0
```
The `≤25`-word filter has no lower bound (`_quoted`, `:155`), and the fetch arm’s substring test
finds `a` on any page, so the live-quote conjunct inherits the same hole. The counter is
non-vacuous only because the current draft happens to carry full sentences.

### F8 — MEDIUM-LOW: duplicate registry id is silently shadowed (last row wins)

`_source_rows` does `rows[cells[0]] = cells` (`:121`). Appending a second 11-cell `S203` row with
the same `source` cell and a different anchor still yields:

```
python3 -B verifiers/check_skill_precedence.py --repo /tmp/c1-attack/M6-dup-registry-row
skill precedence backed 5 of 5
exit=0
```
The canonical row is never consulted; no duplicate finding is raised. The registry gate may catch
this, but C1’s counter alone cannot.

### F9 — MEDIUM-LOW: client distinctness is raw `.lower()` only

`M4-dup-client-space` rewrites the Amp row’s client cell to `Roo  Code` (one doubled internal
space) — semantically the same client as row 1 — and scores `5 of 5`. `.lower()` does not
normalize whitespace; the distinctness test needs `_norm(cell).casefold()`.

### F10 — LOW: unreadable repository is classified as a content verdict

`check()` tests `entry_path.is_file()` first (`:186`) and returns before the SOURCES/README
environment check:

```
python3 -B verifiers/check_skill_precedence.py --repo /tmp/no-such-repo
measured-rev: working-tree
skill precedence backed 0 of 5
  - entry missing: corpus/knowledge/skill-name-precedence-round69.md
exit=1
```
Docstring: “a genuinely unreadable ENVIRONMENT (… unreadable repository …) is exit 2.” It is not.
(`--rev` on a nonexistent repo does exit 2, so the frozen predicate is unaffected.)

### F11 — LOW/DOC: the trust-boundary sentence overstates what `--rev` measures

“the counter runs the measured revision’s own bytes … a revision that rewrites the instrument can
change the verdict.” With `--rev X` invoked from a checkout at `Y`, the *content* is X’s but the
*instrument* is Y’s. The statement is true only when the checkout is at X. The base control is
itself such a case: the counter does not exist at `a5f7459`, yet it is run there by the new
script. Not a soundness break, but the receipt should not read as if X’s counter executed.

## Direct answers to the posed questions

* **Could a malformed entry still score 5/5?** Yes, many ways: empty rule cell (F1), id in the
  client cell with no client names (F2), junk/removed README row (F4), section title as the
  “located quote” (F5), empty source cell (F6), one-letter quote (F7), duplicate registry row
  (F8), a second row for the same client with different whitespace (F9). Eight distinct worlds,
  all exit 0, all reproduced above.
* **Does a quote match that should not?** Yes. The quote universe is the whole entry and the
  selection is longest-by-character, so anchor metadata wins over the claim when it is longer
  (F5/M5, F7). It also cancels a genuinely correct row (F5/M12).
* **Does the per-client table test check the right cells?** No. It checks positions 0 and 1 and
  never reads the header (`:226`), so “rule cell filled” can be satisfied by the quote cell
  (F1), and “client cell” can be satisfied by the id (F2). It also matches the quote anywhere in
  the row (`:229`) rather than the quote column.

## Verdict

**Not sound as frozen — defect with reproduction.** The counter is directionally right and its
frozen base control (`0 of 5`, exit 1), missing-entry classification, junk control, honest 5/5
and live `--fetch` 5/5 all reproduce exactly. But two of its own stated conjuncts are unchecked in
practice (rule cell, client identity — F1, F2), the index conjunct is context-blind (F4), quote
selection is non-deterministic against surrounding prose (F5), and the self-test crashes on the
partial states this round actually passes through (F3). The current draft’s 5/5 is earned by its
content, so C1’s claim is not inflated *today*; the counter simply cannot falsify a malformed
variant of it.

Residual risk / gaps: I did not judge the documentary semantics of the five quotes (the critics’
scope) — I verified only presence and placement; `--fetch` was exercised once (5/5, 2026-10-25)
and its redirect/encoding edge cases were not swept; no concurrency or process-contention testing
was performed. `--fetch` result is live-page state, not frozen.
