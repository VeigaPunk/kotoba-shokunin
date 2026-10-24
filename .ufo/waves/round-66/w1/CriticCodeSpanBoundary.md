# CriticCodeSpanBoundary — `inside_code_span` boundary attack (round 66 w1)

Seat: critic (leaf, no subagent dispatch). Assigned item only: `inside_code_span`
(`verifiers/verify_corpus_integrity.py:321-341`) — unmatched, escaped, and nested
single-vs-double backticks, and live `commit `<hex>`` citation syntax. Read-only review:
no claim, counter, threshold, plan, receipt, or lane file was changed. All runs were
in-process imports; no sandbox mutation was needed. This is observed evidence for the
canonical judge, not a rubric ruling.

## Revisions

| item | value |
|---|---|
| plan base (pinned) | `11385e04e368c1e94ab1a5a89d7439033eb1f855` — `inside_code_span` does **not** exist at this revision; only `inside_quotes` (line 313) |
| measured tip | `2a8eba56b3f9321b70c569fa2816d42237ca49a2` — `inside_code_span` added at `806b53b` ("round-66: land G9 coupling and integrity fixes") |
| counterpart authority | `verifiers/verify_corpus_independent.py:162-189` `code_span_spans` (round-66-aligned pairing semantics) |

## Answer to the posed question

**Yes — as measured, the r54 meta-finding is excluded while ordinary live citations
still count.** On the literal bytes of `corpus/lessons/round-54-verifier-spotcheck.md:147`
(`` `` commit `451a02ff` `` grammar in the new entry) was fixed in `cae8f2ea`…``):

- `COMMIT_RE` matches `commit `451a02ff`` at `[3,20)`; `inside_code_span` returns `True`
  (outer w2 run `[0,2)` opens, w2 run `[21,23)` closes); `citation_findings` records it as
  `commit_quoted_detail` → `...:147: 451a02ff (quoted meta-finding)`.
- Corpus-wide at tip: exactly **one** token relies solely on the code-span exclusion
  (the r54 token); five more are quote-excluded; **38 live** `commit `<hex>`` citations
  count, `unresolvable=0`, `nonhash=0` — matching the landed `--json` run exactly.
- At the pinned base (no `inside_code_span`) the same line counted as live and
  `451a02ff` was one of the three `commit_unresolvable` rows (C2-before control);
  `MutC2CodeSpan` independently confirmed the exclusion is load-bearing for this token.
- The other two former unresolvable rows (`round-62:13`, `round-65:11`) are a different
  class — lane-absent objects resolvable only via the fleet hop, not code-span findings.

So the intended boundary works: grammar-quoted citations are context, authored
`commit `hash`` citations are counted.

## Counterexample (the attack finding)

**`inside_code_span` over-excludes: a backtick run already consumed by an earlier span —
a real span's closer, or a w≥2 run inside a real span — is re-tried as an opener and
paired with the next equal-width run, fabricating a phantom code span that swallows a
live citation.** CommonMark pairing consumes each run once; `code_span_spans` honors
this (`i = j + 1`), `inside_code_span` does not (its outer loop advances only `index+1`).

Concrete minimal cases (all observed; `deadbeef` etc. are unresolvable in lane+fleet,
so a false exclusion is undetectable in `unresolvable`):

| line | CommonMark/independent | `inside_code_span` |
|---|---|---|
| ` ``a`` commit `deadbeef` `` ` | LIVE (trailing ` `` ` is literal) | **excluded** — closer `[3,5)` pairs dangling `[24,26)` |
| ` `` `a` `` commit `deadbeef` `` `x` `` ` | LIVE | **excluded** — closer `[7,9)` pairs the ` `x` ` span's opener `[28,30)` |
| ` ``a`` ``b`` commit `deadbeef` `` ` | LIVE | **excluded** — second consumed closer `[9,11)` pairs dangling `[30,32)` |
| ` ``` ``x`` ``` commit `deadbeef` `` ` | LIVE | **excluded** — w2 *content* run `[7,9)` inside the w3 span pairs dangling `[32,34)` |
| ` `` ``inner`` `` commit `deadbeef` `` ` | LIVE | **excluded** — consumed closer `[13,15)` of the second span pairs dangling `[34,36)` |

Mechanism: the inner loop `break`s on the first equal-width run, but the outer loop then
re-scans every earlier run. For a run already consumed before `start`, `open_end <= start`
passes and any later equal-width run becomes its "closer". A width-1 run cannot phantom
over a `COMMIT_RE` match because the citation's own open delimiter is the first
equal-width run and fails containment — **the bug fires only for runs of width ≥ 2,
exactly the delimiter class the r54 exclusion depends on**.

The function is asymmetrically safe in the other direction: it never under-excludes
(a real enclosing span's opener pairs with its first equal-width run, which is by
definition its true closer). Unmatched runs (`unmatched ` tick commit `deadbeef``),
escaped openers/ closers (`\` commit `deadbeef` ``), width mismatch (`` ``commit
`deadbeef``` ``), and partial-wrap shapes all behave correctly in both implementations.

Adjacent surface (not the assigned item, noted for the planner): `inside_quotes` has the
same over-exclusion shape — raw parity counting treats a `"` *inside* a code span as
literal text for Markdown purposes but as a parity flip here. ` ``` " ``` commit
`deadbeef` " ` is excluded although CommonMark sees one real span plus one dangling
quote. Both directions on plain `"` quotes behave correctly.

## Empirical status

- Zero divergences between `inside_code_span` and `code_span_spans` over all 118 tracked
  corpus `*.md` commit-citation lines at tip — the defect is **latent**, no live victim.
- `verify_corpus_integrity.py --self-test`: 0 failures / 161 assertions;
  `verify_corpus_independent.py --self-test`: 103 assertions, 0 failures.
- Neither self-test exercises the consumed-run case: both fixtures cover only an
  *unconsumed* w2 opener wrapping the citation (the r54 shape) plus a plain live
  citation. The defect class is unguarded on both instruments.
- `check_r66_routed_repairs.py` requires only the literal string `"inside_code_span"`
  in the blob — presence, not behavior; the committed-byte `commit_total=37` pin is what
  bounds functional drift.

## Impacted axes

- **C2 consistency (calibration)**: the round's stated goal was to make the two
  integrity instruments agree on code-span context. On the defect class above they now
  disagree — primary excludes, independent counts. A corpus line in this shape would
  silently depress `commit_total` under the primary gate while the independent gate
  flags `unresolvable`: a cross-instrument inconsistency inside the just-closed D2
  surface. Fixable defect, not a tradeoff the judge must reject; nothing in the claim
  requires closing the residual line class, and tip is strictly better than base.
- **C1 depth**: unaffected (G9 clause coupling untouched).

## Smallest safe correction

Mirror `code_span_spans` consumption semantics: when an opener's inner loop selects run
`j` as the closer (whether or not containment holds), resume the outer scan at `j+1`
instead of `index+1` — i.e., materialize consumed-through indices. One-line-shape change
inside `inside_code_span`; no signature or caller change. Pin with two new self-test
arms in the existing `commit-context` fixture family:

1. ` ``a`` commit `451a02ff` `` ` → `commit_quoted_excluded == 0`, `commit_total == 1`
   (consumed-closer case, currently excluded).
2. ` ``` ``x`` ``` commit `451a02ff` `` ` → live (consumed-content case).

Optionally apply the same treatment to `inside_quotes` parity (quotes inside code spans
are literal) — a separate, adjacent fix.

## Tooling

No installs or upgrades performed; nothing to record.
