# ScribeCorpusR96 — SOURCES rows S271/S272, round-96 lesson scaffold, README index row

Seat: **ScribeCorpusR96** (scribe, wave `r96-w1`, round 96). Report written before the final answer.
Lane repo: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Scratch clone (the only repo written):
`/fast/scratch/hyaku/kotoba-r96/ScribeCorpusR96/repo`, `git clone --shared` + `checkout -q
679775abb9277a7b8d17f060b0f5b4ced2b127b6`, `git rev-parse --show-toplevel` printed the clone path
before staging.

## Behaviour

1. **`corpus/SOURCES.md` — two appended rows, no other change.**
   - **S271** PIT (pitest) "Mutation operators", `https://pitest.org/quickstart/mutators/`, kind
     `docs`, tier A, status `mined`, opened 2026-11-06, recheck `180d`, used-by
     `corpus/lessons/round-96.md,plans/round-96.md`. Scope: the documented boundary-mutation class a
     kill counter's relational mutant belongs to (grounds `t04-le-to-lt`). Anchor: § Conditionals
     Boundary Mutator, heading HTML line 313; located quote 16 words at HTML lines 317-319; the
     operator table's `<=` → `<` row at HTML lines 333-336.
   - **S272** POSIX.1-2024 XCU chapter 2, `https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html`,
     kind `spec`, tier A, status `mined`, opened 2026-11-06, recheck `on-release`, used-by
     `corpus/lessons/round-96.md,plans/round-96.md`. Scope: which textual forms count as an
     unsubstituted shell variable (`${name}`, `$name`) — grounds `t01`–`t03`. Anchor: § 2.6.2
     Parameter Expansion, heading HTML line 777; located quote 22 words at HTML lines 790-791.
   - Both rows are single lines, `NF=13`, no `|` inside any cell, no `<`/`<=` list written with
     pipes.
2. **`corpus/lessons/round-96.md` — new scaffold (206 lines, author ScribeCorpusR96)** with
   `## Gate` (S271/S272 access records; two same-round rejects — mutmut and the gnu.org Bash manual —
   each with reason and flip condition; BASH(1) recorded as a corroboration witness with no row;
   Stryker "Supported mutators" recorded as not-written-this-round; the round-95 Ant reject reason
   amended append-only), `## Mistakes` (one row, `decoy-builder-cuts-elif-chain`), `## Status
   changes` (none — append-only), `## Considerthese` (re-read `considerthese/2026-10-26.md`;
   proposals 1–3 measured and carried, none implemented), `## Settlement` (L1 placeholder).
3. **`corpus/README.md` — one index row** for `lessons/round-96.md`, shaped like the round-95 row,
   placed directly after it (no blank line inside the table).

## Gates

| gate | command | observed |
|---|---|---|
| census validate (patched tree) | `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file "$D/corpus/SOURCES.md"` | **rc 0**, **34 `W04`** (identical to `receipts/census-before.txt`), **0 `E`-codes**, last line `file ok …/corpus/SOURCES.md` |
| census validate (fresh clone + patch) | same, `--file "$V/corpus/SOURCES.md"` | **rc 0**, 34 `W04`, 0 `E` |
| row count | `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` | **196** at `679775ab` → **198** patched (two rows, none dropped or rewritten) |
| row shape | `awk -F'\|' '/^\|S27[12]/{print $2" NF="NF}'` | `S271 NF=13`, `S272 NF=13` |
| duplicate URL | `grep -c 'pitest.org'`, `grep -c opengroup` at `679775ab` | 2 (both `basic_concepts`), 0 — neither new URL is held, so no new `W04` |
| patch applies on a second fresh clone at the freeze commit | `git clone --shared … && checkout 679775ab && git apply --check <patch>` | `APPLY-CHECK-OK`, then `APPLIED`; census on that tree rc 0 |
| quote-equal (S271) | strip tags, unescape entities, collapse whitespace over HTML lines 313-320 | `True` |
| quote-equal (S272) | same over HTML lines 777-792 | `True` |
| word counts | `printf '%s\n' "<quote>" \| wc -w` | S271 **16**, S272 **22**, BASH(1) corroboration **16** |

Patch: `.ufo/waves/round-96/w1/ScribeCorpusR96/ScribeCorpusR96.patch`, 237 lines,
sha256 `6cb886c3db99eaef7f89d744f47f395624ed31fefeeb3456c30899c0ec1289dd`,
`git diff --cached --binary 679775abb9277a7b8d17f060b0f5b4ced2b127b6` → 3 files, **+209 / −0**.

## Touched surfaces

- `corpus/SOURCES.md` (+2 lines: S271, S272)
- `corpus/lessons/round-96.md` (new, 206 lines)
- `corpus/README.md` (+1 line: the round-96 index row)
- Receipts (this seat's dir only): `ScribeCorpusR96/census-after.txt`,
  `ScribeCorpusR96/census-applied.txt`, `ScribeCorpusR96/fetch-receipts.txt`,
  `ScribeCorpusR96/ScribeCorpusR96.patch`.

Nothing else was written in the lane, the fleet root, `considerthese/`, `.ufo/state/`, `scripts/`,
`templates/`, `MANIFEST.json`, `SKILL.md`, any verifier, or any other seat's file. No git/jj write
outside the scratch clone (no commit was needed; the patch is a working-tree diff from the freeze
commit).

## Findings

1. **Number drift in a frozen receipt (recorded, not rescued).**
   `receipts/sources-opened.txt` records the S272 located quote as "19 words"; the quote string it
   carries measures **22** by `wc -w` (this seat and the scout measured 22 independently). The quote
   is unchanged and still ≤25 words, so the admission is unaffected; the frozen receipt was not
   edited. The true count (22) is what S272's row and the lesson Gate carry.
2. **PIT quote is not byte-exact** — the sentence is split across two `<p>` elements (HTML lines 317
   and 319, blank line 318 between them). It is quote-equal after documented shaping (Q56); the row
   and the Gate say so rather than implying a contiguous byte run.
3. **`gnu.org` is unreachable from this host** (scout: two `curl: (28)` timeouts, HTTP 000, 0 B). The
   reachable BASH(1) page at `tiswww.case.edu` carries the same optionality rule and is recorded as a
   corroboration witness with no row (Q23 sweep), keeping the registry at the two rows this seat owns.
4. **mutmut does not state the `<=` → `<` direction** (its only relational example is `<` → `<=`,
   HTML line 523; it defers the full list to `node_mutation.py`, line 527) — the same-round reject.
5. **Both admitted sources are byte-identical across three independent fetches** (this seat, the L1's
   `sources-opened.txt`, the scout): 67033 B / `a31331da…b2da2` and 357953 B / `0889867a…1acd`.
6. **Ant amendment verified against my own fetch**: HTTP 200, 33365 B, sha256
   `3f1ee369…c4a1`, `grep -ic 'unexpected exception'` → 0, `haltonerror` at HTML line 94,
   `errorproperty` at 98, `haltonfailure` at 104 — the reject stands on "no definition of an error".

## Out of scope (deliberately not done)

- No edit to `SKILL.md` (600/600 lines), `plans/round-96.md`, the counter, the builder, the forgery
  patches, `verifiers/*`, `corpus/QUALITY.md`, `corpus/lessons/round-95*.md`, or any frozen receipt.
- No third SOURCES row (Stryker "Supported mutators" and BASH(1) are recorded as candidates, not
  rows) — ownership is exactly S271 and S272.
- No `## Sources` section in the lesson: the Gate carries the access records, and the item names the
  five sections this file has.
- No claim judgment, no counter reading, no settlement — `## Settlement` is the L1's.

## Artifact paths

- `.ufo/waves/round-96/w1/ScribeCorpusR96.md` (this report)
- `.ufo/waves/round-96/w1/ScribeCorpusR96/ScribeCorpusR96.patch`
- `.ufo/waves/round-96/w1/ScribeCorpusR96_READY`
- `.ufo/waves/round-96/w1/ScribeCorpusR96/census-after.txt`
- `.ufo/waves/round-96/w1/ScribeCorpusR96/census-applied.txt`
- `.ufo/waves/round-96/w1/ScribeCorpusR96/fetch-receipts.txt`
