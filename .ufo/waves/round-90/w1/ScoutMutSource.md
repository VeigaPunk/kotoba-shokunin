# ScoutMutSource — round 90 w1 (S260 — the mutation-testing practice source)

Seat: **ScoutMutSource**. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Scope: open ONE mutation-testing practice primary source grounding C1's mutant / killed / survived
vocabulary and the equivalent-mutant (or mutation-score) notion; record the route ledger with ≥1
rejection; hand off the URL via `SOURCE_READY`.

Full evidence (snapshots, response headers, `sed -n '<L>p'` outputs, `wc -w` counts, byte-shaping
statements, rejected-route bodies) is under
`.ufo/waves/round-90/w1/ScoutMutSource/` — start at **`s260-notes.md`**.

---

## Result

**S260 opened and grounded.** Adopted source:

- primary: `https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/`
  — HTTP **200**, **27068 B**, title `Mutant states and metrics | Stryker Mutator`,
  fetch-time sha256 `8641c389…`
- sibling anchor (same doc set): `https://stryker-mutator.io/docs/mutation-testing-elements/equivalent-mutants/`
  — HTTP **200**, **38687 B**, title `Equivalent mutants | Stryker Mutator`,
  fetch-time sha256 `b71ae157…`

Per r89 spot-check note 1 the digests are **fetch-time metadata only**; the quotes are grounded in
**line anchors + byte size + page title**, never in the digest.

### The two legs, located

| leg | quote (`wc -w`) | file | line |
|---|---|---|---|
| (i) killed | "When at least one test failed while this mutant was active, the mutant is killed." (15) | `s260-snapshot.html` | 12 |
| (i) survived | "When all tests passed while this mutant was active, the mutant survived." (12) | `s260-snapshot.html` | 14 |
| (ii) score definition | "The total percentage of mutants that were detected. The higher, the better!" (12) | `s260-snapshot.html` | 52 |
| (ii) score formula | "detected / valid * 100" (5) | `s260-snapshot.html` | 51 |
| (ii) equivalent-mutant notion | "It is called equivalent mutant. There is no definitive way for Stryker to find and ignore them." (17) | `s260-snapshot-equivalents.html` | 16 |

All five `sed -n '<L>p'` outputs and the byte-shaping statement for each are pasted verbatim in
`s260-quote-receipts.txt`. Four of the five quoted segments are contiguous raw-byte substrings of
their named lines (**no bytes shaped**); only Q3 crosses an `<em>…</em>` markup boundary, and the
only bytes removed there are those two literal tag sequences — no word altered.

### Route ledger (honest)

- **(a) mutmut docs index** `https://mutmut.readthedocs.io/en/latest/` — HTTP **200**, 51074 B.
  **Partial support only**: grounds killed/survived vocabulary (lines 157, 537–538) but has **zero**
  occurrences of "equivalent" and its only "mutation score" mention (line 545) is a
  `mutmut badge` / `export-cicd-stats` command pair, not a definition. Not usable as sole support.
- **(a′) mutmut "How it works" / glossary subpages — HTTP 404 on all 15 probes.** The Sphinx build
  has exactly one document (`en/latest/searchindex.js` → `docnames: ['index']`); no such page exists.
- **(a″) mutmut repo README.rst** — HTTP 200, 22381 B; `docs/index.rst` is
  `.. include:: ../README.rst`, so the same sentences sit at the same line numbers (617–618 ≡ 537–538).
- **(b) Stryker docs entry** `https://stryker-mutator.io/docs/` — HTTP 200, 30253 B; grounds
  killed/survived at line 5 and links to both adopted sub-pages.

### Rejections (for the lesson `## Gate`)

1. **ACM DL DOI `10.1145/2382577.2382594` — HTTP 403** (Cloudflare "Just a moment…" JS/cookie
   challenge, 5471 B). No quote may be taken from bytes that are not the article.
   **Flip:** re-open via an open-access/institutional mirror or the publisher PDF endpoint.
2. **Wikipedia "Mutation testing" — HTTP 200 but tier C**, lead only; may not be sole support for a
   tier-A-scoped claim. **Flip:** stays a lead; re-open the cited paper directly if a paper is needed.
3. **Route (a) mutmut docs — HTTP 200 but refused as sole support** (see above).
   **Flip:** if mutmut's docs gain a glossary naming equivalent mutants and the score formula, mutmut
   becomes a valid second tier-A source and this flips to "admitted".

### Why this vocabulary is the right ground for C1

`mutation score = detected / valid * 100` where `detected = killed + timeout`; an **equivalent
mutant** is indistinguishable from the original program, so it **survives by construction** and
cannot be automatically ignored. Therefore C1's frozen predicate — `killed K of M`,
`equivalents survived E of E`, `disclosed survivors S of S` — is counting three different things:
the score-detected class, the class that survives by construction (a property of the generated
mutants, **not** a gap in the suite), and the genuinely-undisclosed class. The score ceiling of a
battery that contains E equivalents is 100 % minus E/valid — so "equivalents survived E of E" is a
pass, not a red.

### Proposed S260 row (ScribeCorpus owns `corpus/SOURCES.md`; content measured by this seat)

kind `docs` · tier **A** scoped to *the mutation-testing vocabulary and metric definitions as the
tool's own documentation states them* (not this lane's battery mechanics — those are S261) ·
anchor: `§ Mutant states: Killed (HTML line 12), Survived (line 14); § Metrics: Mutation score
detected / valid * 100 (line 51) + definition (line 52); "Equivalent mutants" § Equivalent mutants
(HTML line 16)`, each with its page's own `<title>` and byte size as the fetch anchor ·
opened 2026-11-05 · recheck 180d · used-by `corpus/knowledge/mutation-battery-round90.md`.
The full row table is in `s260-notes.md` §5.

---

## Findings and risks

- **Finding (route availability, informational):** mutmut's readthedocs build is a single
  `index` document — there is no "How it works" or glossary page, so a plan that assumes one
  would have to probe for it. The equivalent-mutant notion is simply absent from mutmut's docs.
- **Risk (tier discipline):** both Wikipedia and the ACM landing page are unusable as S260
  support; if the scribe wants the *peer-reviewed* wording of the equivalent-mutant definition,
  the DOI must be re-opened through an accessible mirror. As opened, S260 rests on vendor
  documentation (tier A for its own terminology) and stays scoped to that.
- **Risk (row anchor):** the Stryker docs are a live site behind a CDN cache
  (`x-proxy-cache: HIT`, `last-modified: 2026-11-04`); line numbers are anchors into the bytes this
  seat saved, not stable upstream coordinates. The recheck cadence is set to 180d accordingly, and
  the quote grounding is line-anchor + size + title, per r89 note 1.
- **No defect in the plan or controls was found.** The plan's "S260 = external mutation-testing
  practice source" is satisfiable as written; the two prescribed routes and both rejected routes
  are recorded above.

## Constraints honoured

Writes confined to `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-90/w1/ScoutMutSource/`
plus this seat's report file and the mandated `SOURCE_READY` handoff marker. No git or jj write was
run against the lane, the fleet root, or any sibling lane; no file outside the seat's scope was
modified; no tool was installed this seat (`curl 8.23.0` and `python3` from the system were used).
