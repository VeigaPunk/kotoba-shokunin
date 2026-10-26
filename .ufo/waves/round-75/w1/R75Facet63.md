# R75Facet63 — Q70's error-body clause: what the counter actually rejects

## Axes
Round axes: depth, freshness, consistency, calibration, operability, adjacency
(`.ufo/waves/round-75/w1-spec.json:1`). This facet bears on **depth** (is the rule's claim
carried by a mechanism?) and **operability** (can an operator run the missing check with the
harness already in the file?). No other axis is claimed improved or harmed.

## Facet (one rule, one clause)
`corpus/QUALITY.md:86` (Q70), error-body clause, verbatim:

> A counter's token and quote conjuncts are run against what every page of the source shares
> (site banner, page subtitle, navigation) **and against an error body**: a counted token
> occurs in the claimed page and in no other page of the set, a counted quote's line lies
> after the page's first heading and outside its subtitle block, and a snapshot's sha256 is
> pinned in the counter, in the cited registry row's anchor and in a fetch record that reads
> HTTP 200.

Grounded in `corpus/lessons/round-74.md:90` (M137, "counter admits site chrome and error
bodies", worlds W2/W5/W3/W4/W6) and in `plans/round-74-addendum-1.md:30-32`, which states the
mechanism: "(c′) … `FETCH-LOG.tsv` … records … status `200` … (**kills the 404-body snapshot**
and the self-attested pin, C1-4)".

## Observation (committed bytes)
1. The three content/pin conjuncts are implemented. `verifiers/check_spec_craft.py:901-907`
   (page-unique token, message `no page-unique token among`), `:714-748` (`quote_line_problems`:
   pre-H1 refusal at `:730-735`, heading at `:737`, subtitle blockquote at `:739-743`,
   cross-page link at `:744`), `:909-926` (anchor digest at `:912-915`, `fetch record status`
   at `:923`),
   `:203-211` (`PAGE_SHA`, the Q33 constant pin).
2. The only *error-body* world in the lane is the critic's committed world
   `.ufo/waves/round-74/w1/build/CriticClaimsR74/c1worlds/W6_404_snapshot/` — one 705-byte
   body (`sha256 5694925680c9842fc9631f25ba7cf2a881ddf1503173d5237e16455144dfebad`, matching
   `w1/CriticClaimsR74.md:45`) stored under **all three** page names, with
   `snapshots/FETCH.tsv:1-3` recording status `404` for each page.
3. That world therefore trips three conjuncts at once (`w1/CriticClaimsR74.md:427-428`:
   `(a') no page-unique token; (d') line 3 precedes the H1; (c') snapshot sha256 not recorded
   in the row anchor`). The lane's own attribution is the status cell, not the bytes
   (`plans/round-74-addendum-1.md:30-32`).
4. The gate's own self-test has **no** error-body snapshot world. The only 404 arm is a log-cell
   flip: `verifiers/check_spec_craft.py:1722-1725`, label `(c') a fetch record with HTTP 404 does
   not back a page`, implemented as `.replace("\t200\t", "\t404\t", 1)` on `_fetchlog()`.
   `grep -n "Page Not Found\|could not be found" verifiers/check_spec_craft.py` → no match.
5. The committed 404 body is *page-shaped* enough for the content guards: it has an H1
   (`# Page Not Found`, line 6) and a plain, non-blockquote, non-link line after it
   (`The requested page could not be found.`, line 8). Against the three honest snapshots that
   sentence occurs **0** times (`grep -c` on `.ufo/waves/round-74/snapshots/{best-practices,
   using-scripts,quickstart}.md` → `0 0 0`), so stored for a single page it is page-unique.

## Finding (scope of Q70's error-body clause)
Q70 as written says the **token and quote conjuncts** are run against an error body, i.e. that
they are what refuses one. The r74 evidence does not establish that: W6's body is refused
because the same bytes sit under three names (killing (a′)) and because the fetch log says
`404` (killing (c′)) — the addendum names (c′) as the killer. The body's own line 8 passes (d′)
by the code at `:730-748` (line index 7 > first `# ` at index 5, not a heading, not inside the
H1→H2 blockquote block, no `skill-creation/` link), and its uniqueness is an accident of W6
duplicating one body across three pages.

**[INFERENCE]** (not executed in this read-only seat) A world that stores the same committed
705-byte 404 body as **one** page's snapshot, records status `200` for it (a soft-404 — common
on docs hosts), and re-signs manifest, fetch log, registry anchor and `PAGE_SHA`, would read
that page as *backed*: (a′) passes on the line-8 sentence, (d′) passes as above, (c′) agrees
because all three pins are re-signed to the same bytes. The counter would print
`spec craft pages backed 3 of 3`, exit 0. Only the three frozen `PAGE_SHA` constants stop this
for the round-74 pages; a later counter over newly fetched pages, pinned from a soft-404, has
no body-level guard. Q70's clause is thus scoped wider than its mechanism, and the addendum's
"kills the 404-body snapshot" is true only of a **recorded** 404.

Secondary scope note: "navigation" is narrower than the clause implies — only a quote on a line
matching `\]\([^)]*skill-creation/` is refused (`check_spec_craft.py:744`); a nav/breadcrumb
line without such a link is admitted by (d′), and nav *tokens* are held back only by the
uniqueness rule, never by a nav test.

## Concrete control (both directions, using existing harness)
Add one self-test arm to `check_spec_craft.py`; no new plumbing is needed:
`_repin` (`:1200-1215`) already rebuilds `MANIFEST`, `FETCH-LOG.tsv` (default status `200`,
`:1186`) and swaps the registry digest in `SOURCES` for the changed snapshot, and `_run_spec`
(`:1776-1797`) re-pins `PAGE_SHA` in `world` mode.

```
ERROR_BODY = <the committed 705-byte body from
              .ufo/waves/round-74/w1/build/CriticClaimsR74/c1worlds/W6_404_snapshot/snapshots/quickstart.md>
world = _repin(_mutate(honest, **{
    f"{SNAPDIR}/quickstart.md": ERROR_BODY,
    ENTRY: _entry_text(tokens={"quickstart": '<line-8 sentence> + one more token'},
                       quotes={"quickstart": "The requested page could not be found."})}))
add(dict(label="(a')/Q70 an error body stored for one page is not backed",
         files=world, code=1, line="spec craft pages backed 2 of 3"))
```

* Red direction (expected today, per the code read): `3 of 3`, exit 0 — the arm fails, and Q70's
  error-body clause is shown to be a status-cell approximation that must be re-worded or guarded.
* Green direction (a real guard): refuse a snapshot whose first H1 is an error title. Cheapest
  form consistent with the file's own Q33 pattern: pin each page's first H1 as a constant
  (`# Best practices for skill creators` — `snapshots/best-practices.md:5`; `# Using scripts in
  skills` — `:5`; `# Quickstart` — `:5`) beside `PAGE_SHA:203-211` and require equality; the
  404 body's `# Page Not Found` (line 6) then exits 1 with a named finding.
* Both-direction duty (Q18/Q20): a title-constant guard false-reds a legitimate upstream title
  rename, so it must ship with the rename path (re-pin the title constant in the same commit)
  and a self-test arm that an unchanged page with a renamed title is refused until re-pinned.

## Risks
- I did not execute `check_spec_craft.py` or any gate (wave rule; no harness run, no fetch, no
  install). The `3 of 3` prediction is a reading of `quote_line_problems`, `page_unique`,
  `token_occurrences` and `_repin` against committed bytes; it is inference, and the control
  above is how to settle it.
- The round-74 C1 verdict is unaffected: those three pages are held by the frozen constants and
  were re-fetched byte-identical by the non-author closure
  (`corpus/lessons/round-74-verifier-spotcheck.md:32-40`). Q70 binds future counters, which is
  why the soft-404 shape matters (e.g. any r75 description-audit counter over fetched vendor
  doc pages, the same surface that produced S209/S210/S212/S213).
- Do not widen the guard to reject any page lacking a banner or any blockquote after the H1:
  the honest quickstart places a legitimate `> [!NOTE]` blockquote after `## Prerequisites`
  (`snapshots/quickstart.md:15-17`), which the (d′) block already permits.

## Evidence commands (read-only, run)
- `sed -n '86p' corpus/QUALITY.md`; `sed -n '88,96p' corpus/lessons/round-74.md`
- `sed -n '714,748p;901,935p;1200,1215p;1722,1725p;1776,1797p;203,211p' verifiers/check_spec_craft.py`
- `nl -ba .ufo/waves/round-74/w1/build/CriticClaimsR74/c1worlds/W6_404_snapshot/snapshots/best-practices.md`
- `cat -A .ufo/waves/round-74/w1/build/CriticClaimsR74/c1worlds/W6_404_snapshot/snapshots/FETCH.tsv`
- `grep -c "The requested page could not be found" .ufo/waves/round-74/snapshots/{best-practices,using-scripts,quickstart}.md` → `0 0 0`
- `grep -n "^# " .ufo/waves/round-74/snapshots/*.md`
- `sha256sum .ufo/waves/round-74/w1/build/CriticClaimsR74/c1worlds/W6_404_snapshot/snapshots/best-practices.md` → `5694925680c9842fc9631f25ba7cf2a881ddf1503173d5237e16455144dfebad`, 705 bytes

Report trailer: `Facet 63; evidence committed bytes at the cited paths/lines at 65a5c7a663249e0522cc49e4a148424200d9ddfe; no edits, no gate run, no live fetch, no install, no scratch left behind.`
