# Round 94 — kotoba (Linux host, omp): lesson

Author: **ScribeCorpusR94** (scribe seat). This file is the round-94 **scaffold**: the Gate record,
the Mistakes row and the Considerthese entry below are written; **the L1 completes the settlement**
(the seat record, the claim verdicts, the wave disposition and the final numbers).
Round: 94, plan `plans/round-94.md` (frozen at `edc731a91a956f6df20c27a74fb981b286f6ba58`), base
`4d3e8e4d290d67ecf94a019059f434c71f399919`.
Pre-data receipts (frozen with the plan, before any scored reading):
`.ufo/waves/round-94/receipts/redbefore-c1-base.txt` (`C1-PREDICATE-UNMET` at the base),
`redbefore-c2-base.txt` (`C2-PREDICATE-UNMET` at the base), `forgery-c1-run.txt`
(`C1-PREDICATE-UNMET` via the forgery world), `forgery-c2-run.txt` (`C2-PREDICATE-UNMET` via the
forgery world) and `census-before.txt` (rc 0, 33 pre-existing `W04` warnings, no `E`-code).

## Gate

Candidates considered, with the decision and the reason:

- **S269** — PIT (pitest) documentation, "Basic concepts"
  (`https://pitest.org/quickstart/basic_concepts/`). **Admitted** as tier A, kind `docs`, status
  `mined`, opened 2026-11-05, recheck `90d`, used-by `corpus/lessons/round-94.md,plans/round-94.md`.
  - Access record (rule 1): access date 2026-11-05; HTTP 200; 12155 B; sha256
    `c51d8423f5a75e00c7039463f8a5992ef8f1f92b994d69f67d212ff7bfd92b3a`. The trailing-slash URL and
    the slash-less URL return byte-identical bodies (same sha256, same byte count) —
    `curl -sS -o pit.html -w '%{http_code} %{size_download}' -L <url>` then `sha256sum pit.html`
    over both forms, read 2026-11-05; the same bytes and digest are kept by the scout under
    `.ufo/waves/round-94/w1/ScoutMutSources/pitest-basic_concepts.html`.
  - Located quote: "Killed means a test caught the mutation successfully." — **8 words**
    (`printf '%s\n' "Killed means a test caught the mutation successfully." | wc -w` → 8), at
    **HTML line 175** of the fetched bytes, quote-equal after removing the `<strong>` tags from
    `<p><strong>Killed</strong> means a test caught the mutation successfully.</p>`. The unshaped
    upstream form is `**Killed** means a test caught the mutation successfully.` at markdown line
    107 of `quickstart/basic_concepts.markdown` in hcoles/pitest-site at commit
    e8995cd59e3cf1b1a35a979b3e735bc2fe413fea (2025-10-24), sha256
    `2d2b7f5d3d27ace19949b4cc1948193e23cc901335c0dc8f0a24415b67613a13` (4371 B), and the same commit
    is the one that renamed the class `Lived` to `Survived` (the commit's own patch, read at the
    GitHub commits API).
  - **What this row adds to S262** (which holds the same URL): S262 holds the outcome-**vocabulary**
    list and the equivalent-mutation grounds; S269 holds what each class **means** for a kill rule
    — the Killed and Survived sentences at HTML lines 175 and 177, the timed-out sentence at lines
    181-182, the non-viable sentence at lines 184-185, the outcome-class list at lines 166-172, the
    page's sha256 (S262 records the byte count only) and the upstream commit that renamed `Lived` to
    `Survived`. **The census therefore records one new `W04`** (the same URL across scopes) — the
    same warning class the lane already carries 33 times.
  - **FINDING for the L1 (conflict, recorded verbatim, not resolved here):** the plan's §Frontier
    step says "S269 (PIT basic concepts) opened this round", but the registry already held this URL
    as **S262** (row 203, kind `docs`, tier A, `mined`), which quotes the same two sentences at the
    same HTML lines — the scout states it in `.ufo/waves/round-94/w1/ScoutMutSources.md` §2
    ("S262 already holds that URL and quotes the same two sentences") and in its §5 risk 1
    ("do not add a second PIT row"). The plan is frozen and names S269 in two places
    (`plans/round-94.md` §C1 "Sourced" and §Frontier), so the row is written as the plan declares it;
    **S262's own row bytes were not touched** (this seat's ownership of `corpus/SOURCES.md` is
    append-rows-only), and folding S269 into S262 is an L1 act by addendum, not a scribe act.
  - **Why this row grounds C1** — the frozen counting command's outcome classes follow the Killed
    definition (a mutant is killed when a test catches it) and the separate `Non viable` and
    `Timed Out` classes, which is why a mutant whose instrument does not compile is
    could-not-evaluate and never a kill (`plans/round-94.md` §Shared counting command; the same
    rule in the header of `verifiers/fixtures/round-94/selftest-kills.py`).
- **Rejected candidate — the mutmut documentation index**
  (`https://mutmut.readthedocs.io/en/latest/`). **Rejected.** Access 2026-11-05; HTTP 200;
  51074 B; sha256 `07453b3fdb3b962a4cc5aff66d7614a11016c9ce0ea482654c99e17688ec9cad`. The fetched
  bytes carry **0** occurrences of "equiv" (`grep -ic equiv` → 0) and no occurrence of "killed" or
  "survived"; the only outcome-adjacent text is a timeout configuration formula. Reason: the index
  names no outcome class and no equivalent-mutant definition, so it grounds no claim the counter's
  classes rest on — this re-probe reproduces the round-90 rejection of the same URL. **Flip
  condition:** a glossary or a how-it-works subpage under the same host that defines killed and
  survived, opened and quoted at ≤25 words with its line.
- **Rejected candidate — the Cosmic Ray documentation**
  (`https://cosmic-ray.readthedocs.io/en/latest/theory.html` and
  `https://cosmic-ray.readthedocs.io/en/latest/concepts.html`). **Rejected as support for the
  counter's outcome classes.** Access 2026-11-05; HTTP 200; 5939 B and 18482 B; sha256
  `a72ab7cf9c4acdeba9cfa5138150592ac5ce4544889ac819ce3dd60bcc0db6e3` and
  `d4da7008e4b3bc094608dc6ece72f18d751f562c53a874d9238ee10254adae7f`. Located quotes: theory.html
  HTML line 41 "we say the mutant is “incompetent”." (6 words) and concepts.html HTML lines
  175-176 "the test is killed, and the mutant is marked incompetent." (10 words). Reason: Cosmic Ray's
  class set is not the PIT class set the counter reads — it folds a timeout into `incompetent` and
  calls a crash `incompetent` — so it cannot ground the Killed / Non viable / Timed Out
  distinction, and admitting it as support would widen S269's scope past the counter's classes.
  **Flip condition:** a versioned Cosmic Ray page that separates its outcome enum, admitting it as
  a tier-A row scoped to the Cosmic Ray tool only.

**Census before → after.** Rows: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
corpus/SOURCES.md` → **194** before this round (receipt
`.ufo/waves/round-94/receipts/census-before.txt`, rc 0 with the 33 pre-existing `W04`
duplicate-URL warnings) and **195** after — the one row appended above (S269), no row dropped, no
row rewritten. Validation: `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate
--file corpus/SOURCES.md` → exit 0, the 33 pre-existing `W04` warnings **plus one new `W04`** for
the same URL across scopes (S269 against S262), and no `E`-code (receipt
`.ufo/waves/round-94/w1/ScribeCorpusR94/census-after.txt`). The new row is an ordinary append, not a
correction, so no row's `teaches` cell opens `supersedes S0NN — ` and the append-only gate
(`python3 -B verifiers/check_sources_append_only.py`) has no protected-cell rewrite to see.

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| `receipt-header-fail-open`: the receipt-revision check silently drops a header-shaped declaration it cannot parse instead of failing on it — a 41-hex `REV=` header matches no 40-hex window, and a declaration indented with leading whitespace is not `^`-anchored, so neither is ever resolved-checked; a file carrying such a line beside a valid one exits 0 (false green) | `.ufo/waves/round-93/w1/CriticClaimsR93/CriticClaimsR93.md` defects **D2** (a 41-hex header is silently dropped) and **D3** (an indented declaration is ignored) | `none` | `verifiers/fixtures/round-93/check-receipt-revs.sh` gains a **MALFORMED** rule: a header-shaped line whose hex run is not 40 characters, or which carries leading whitespace before the declaration, is reported `MALFORMED <path>:<line> <reason>`, counted, and the run exits 1 on any MALFORMED or UNRESOLVED — shown able to fail by the ExecReceiptHeaders receipts under `.ufo/waves/round-94/w1/ExecReceiptHeaders/` (that seat's report reads `Status: DONE`), read 2026-11-05: `before-hex41.txt` reads `receipt revisions: 0 resolved, 0 unresolved over 1 files` and `EXIT=2` (the header silently dropped), while `after-hex41.txt` reads `MALFORMED …/hex41/headers.txt:1 hex run is 41, not 40`, `malformed declarations: 1`, `EXIT=1`; `before-indented.txt` reads `EXIT=2`, while `after-indented.txt` reads two `MALFORMED … leading whitespace before the declaration` lines, `malformed declarations: 2`, `EXIT=1`; the no-harm legs are unchanged (`after-good.txt` `4 resolved, 0 unresolved`, `EXIT=0`; `after-round92-landing.txt` `1 resolved, 5 unresolved over 18 files`, `EXIT=1`; `after-round93-receipts.txt` `9 resolved, 0 unresolved over 19 files`, `EXIT=0` — the round-93 landing receipts still read `9 resolved, 0 unresolved`, rc 0, as the plan's Frontier step requires). The round-94 settlement numbers: `L1 fills at settlement` |

## Status changes

- **S269 — new row**, `mined` at opening (2026-11-05), tier A, kind `docs`, recheck `90d`, used-by
  `corpus/lessons/round-94.md,plans/round-94.md`. No prior row's `status`, `recheck` or `used-by`
  cell changed — the registry is append-only and this seat's ownership of `corpus/SOURCES.md` is
  append-rows-only. Because this lesson cites S262 (the same URL, §Gate above), the L1 may add
  `corpus/lessons/round-94.md` to S262's `used-by` cell at settlement; that is a permitted in-place
  change and would be logged old→new there.

## Sources

- **S269** — PIT (pitest) documentation, "Basic concepts"; URL
  `https://pitest.org/quickstart/basic_concepts/`; access 2026-11-05; HTTP 200; 12155 B; sha256
  `c51d8423f5a75e00c7039463f8a5992ef8f1f92b994d69f67d212ff7bfd92b3a`; the page carries **no
  version or date pin** (no "updated", "version" or "20xx" string in the fetched bytes); the
  located quote "Killed means a test caught the mutation successfully." (8 words) at HTML line 175,
  quote-equal after tag-stripping; the unshaped upstream form at markdown line 107 of
  `quickstart/basic_concepts.markdown` in hcoles/pitest-site at commit
  e8995cd59e3cf1b1a35a979b3e735bc2fe413fea (2025-10-24), sha256
  `2d2b7f5d3d27ace19949b4cc1948193e23cc901335c0dc8f0a24415b67613a13` (4371 B), the commit that
  renamed the class `Lived` to `Survived`. Tier A scoped to what each outcome class means for a kill
  rule; the outcome vocabulary list and the equivalent-mutation grounds are held by S262. Status
  `mined`; used-by `corpus/lessons/round-94.md,plans/round-94.md`.

## Considerthese

`considerthese/2026-10-26.md` was re-read (proposals only; nothing implemented).

- **No proposal implemented this round.** Both claims are instrument-deepening with frozen
  predicates — C1 is behavioural self-test arms in the mutation battery and C2 is the six-key
  coverage behaviour in the tip battery — and the mined-mistake fix is a repair to a round-93
  fixture, so no proposal of this file is inside either claim's scope, and no proposal is
  implemented outside them.
- **Proposal 3** (land the page round 74 rejected and use it on the skill's own description) stays
  carried and is **still unimplemented**: it needs a `SKILL.md` description rewrite, and `SKILL.md`
  is already 600 lines / 92 672 B at the freeze, so a rewrite of the frontmatter description has to
  be paid for by lines saved elsewhere — and the wave context gives the 600-line skill budget to no
  seat this round, so this claim-adjacent edit is not available.
- **Proposal 2** (move `## Gate registry` out of `SKILL.md`) stays an L0 question rather than a
  claim (`corpus/QUALITY.md` Q67: a move that takes a protocol-named home elsewhere is an L0
  question).
- **Proposals 1, 4 and 5** are carried unchanged from the previous rounds; proposals 1 and 5 are
  already mined as criteria Q78 and Q82 and are not re-mined here.

## Settlement

L1 settlement (KotobaR94): the seat record, the C1/C2 claim verdicts with their landing revision,
the wave disposition and the mined-mistake numbers are filled **at settlement** — `L1 fills at
settlement`.
