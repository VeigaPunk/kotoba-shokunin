# R75Facet52 — Q70's three-locus pin, applied to the round-70 page-evidence gate

Seat `R75Facet52` (leaf, read-only, no delegation, no live fetch, no installs). Axes: **calibration** and
**freshness**. Measured revision `65a5c7a663249e0522cc49e4a148424200d9ddfe` (`git rev-parse HEAD`); every
cited path is clean against it (`git status --porcelain -- SKILL.md corpus/QUALITY.md corpus/SOURCES.md
corpus/knowledge/skill-eval-artefacts-round70.md verifiers/check_skill_evals*.py verifiers/check_spec_craft.py
.ufo/waves/round-70/snapshots .ufo/waves/round-70/receipts` printed nothing), so working-tree bytes = committed
bytes. No scratch dir was needed; nothing was written outside this report.

## Facet

`corpus/QUALITY.md:86` (Q70) now requires, for a counter over fetched pages, **three pinning loci** for a
snapshot's sha256 (the counter, the *cited registry row's anchor*, a fetch record reading HTTP 200) plus two
content-position conjuncts (a counted token is page-unique; a counted quote's line is after the page's first
heading and outside its subtitle block), and an error-body world. The lane's live page-evidence gate for the
round-70 entry — the instrument the entry's own `recheck:` names, `corpus/knowledge/skill-eval-artefacts-round70.md:8`
→ `verifiers/check_skill_evals.py`, registered as a `gate` at `SKILL.md:503` — satisfies **only the counter
locus**. The rule is enforced prospectively (r74's `check_spec_craft.py`) and not on the instrument a reader is
still told to re-run.

## Evidence (observation)

**1. The counter locus holds.** `verifiers/check_skill_evals.py:47-54` pins the three full sha256 digests;
`snapshot()` hashes the committed bytes and raises `snapshot_tampered` on mismatch (`:89,95-96`). The v2
successor pins the same digests under S212/S213 (`verifiers/check_skill_evals_v2.py:78-82,148,156`). Measured
from committed bytes: `git show 65a5c7a:.ufo/waves/round-70/snapshots/S209-evaluating-skills.md | sha256sum` →
`a799805f3a28…b684`; S210 → `7cc54fbb6abb…d837` — equal to the constants.

**2. The cited-registry-row locus is unmet (measured 0 of 2).**
```
$ grep -nE '^\| S(212|213) \|' corpus/SOURCES.md | grep -c 'a799805f\|7cc54fbb'
0
$ grep -n 'a799805f\|7cc54fbb' corpus/SOURCES.md
(no output)
```
`corpus/SOURCES.md:152-153` (the rows that "supersede S209/S210 for citation") carry the canonical URL, an
upstream-commit anchor (`69ef37e9…`) and the quote — no snapshot digest. The digest lives in the entry head
(`corpus/knowledge/skill-eval-artefacts-round70.md:1-3`, truncated to 8 hex) and in the two counters, never in
the row anchor Q70 names. Q70 expects **2**.

**3. The fetch-record locus is unmet (no committed record reads HTTP 200).**
```
$ grep -rn 'HTTP 200\|200 OK' .ufo/waves/round-70/receipts/    # no output
$ ls .ufo/waves/round-70/snapshots/                            # 3 snapshots only, no manifest, no fetch log
```
The only fetch receipt records quote presence, not a status: `.ufo/waves/round-70/receipts/C2-measure-tip.txt:4-5`
→ `live quotes found 8 of 8` / `exit=0`; `:9` records the counter sha256 `fc768197…` (frozen at `53de0ac`,
`SCORECARD.md:448`). Contrast the r74 set: `.ufo/waves/round-74/snapshots/{MANIFEST.sha256,FETCH-LOG.tsv}`, the
latter `page url status bytes sha256 date` with `status 200` — exactly the shape `verifiers/check_spec_craft.py:47-61,199`
enforces for the newer counter.

**4. Both content-position conjuncts are unimplemented.**
```
$ grep -n 'heading\|other page\|unique\|banner\|subtitle' verifiers/check_skill_evals.py verifiers/check_skill_evals_v2.py
(no output)
```
The quote conjunct is a bare membership test — `quote not in norm(repo.snapshot(sid))`
(`check_skill_evals.py:160`) and `word_bounded(quote, norm(repo.snapshot(sid)))` (`check_skill_evals_v2.py:275`).
The shared-text premise is measurable in the committed page set: each agentskills.io snapshot opens with the same
3-line banner block `:1-3` (`grep -c 'Documentation Index' .ufo/waves/round-70/snapshots/S209-… .ufo/waves/round-70/snapshots/S210-…`
→ `1`, `1`), and `grep -c 'Fetch the complete documentation index at: https://agentskills.io/llms.txt'` → `1`, `1`.
Line layout: banner `:1-3`, first `# ` heading `:5`, subtitle `:7` (S210 also has a second `# ` at `:102`).

**5. The current eight facts pass the position/uniqueness conjuncts by construction (not by enforcement).**
Measured on committed bytes (one pass over the entry's F-rows):

| fact | row cited | words | snapshots containing the quote | line in own snapshot | first heading |
|---|---|---|---|---|---|
| F1 | S212 | 9 | S209 only | 86 | 5 |
| F2 | S212 | 13 | S209 only | 86 | 5 |
| F3 | S212 | 13 | S209 only | 52 | 5 |
| F4 | S212 | 7 | S209 only | 170 | 5 |
| F5 | S212 | 10 | S209 only | 172 | 5 |
| F6 | S212 | 5 | S209 only | 144 | 5 |
| F7 | S213 | 17 | S210 only | 92 | 5 |
| F8 | S211 | 5 | S211 only | 232 | — (code file) |

So the gap is **latent, not active**: the eight quotes happen to be unique and after the first heading, and the
`KEY_TERMS` conjunct (`check_skill_evals.py:58-67`) independently blocks a banner or subtitle substitution for
these eight facts. Nothing in the counter keeps that true for a ninth fact or a re-pin.

**6. The freshness half cannot detect page drift.**
`live_fetch` compares only quote presence — `quote in pages[url]` (`check_skill_evals.py:178-190`;
`check_skill_evals_v2.py:321-334`) — with no status recorded and no comparison of live bytes to the pinned digest,
although the entry promises "a changed page is a re-open, never a silent snapshot swap"
(`skill-eval-artefacts-round70.md:8`). `[INFERENCE]` A page that gains, loses or rewrites material outside the
eight quoted sentences reads `live quotes found 8 of 8`, exit 0. The snapshot hash protects the archive against
tampering at the measured rev (Q70's counter locus); it does not protect the freshness claim. This matters more
than usual here because the r70 receipt itself labels the reading "met-on-a-hollow-counter, not a verified
measurement" (`C2-measure-tip.txt:10`; `corpus/lessons/round-70.md:270-277`, M119: 11 of 13 junk worlds reached
`8 of 8` on the frozen v1).

**7. Prose defect in the successor counter (Q31 class).**
`verifiers/check_skill_evals_v2.py:35-40` states that the superseding rows carry "fetched sha256 in the anchor
cell". The committed rows do not (§2: 0 hits), and the only enforced anchor test is A9 — an `upstream commit`
token, `UPSTREAM_REV_RE` at `:86`, check at `:295-308`. A reader of the docstring is told a cell is pinned that
the code never reads. `SKILL.md:505`'s registry description is narrower and accurate ("carry an upstream-commit
anchor"); the docstring is the overclaim.

## Axes read

- **Calibration — candidate, high confidence.** Q70 is a sourced, falsifiable rule (grounded in M137,
  `corpus/lessons/round-74.md:90`, W2/W5/W6: shared banner, subtitle, 404 body). It is demonstrated in
  `check_spec_craft.py` (arms `(a')`,`(c')`,`(d')`,`(e')`, `:47-61`) but **not** in the gate the older entry's
  `recheck:` still names. Two of the three loci measure false today, and neither positional conjunct exists.
- **Freshness — candidate, and the weaker axis.** The `recheck: 90d` (`verified-at: 2026-10-25`, due
  2027-01-23) is a quote-presence probe over pages with no fetch log and no live-digest comparison; the entry's
  own wording about re-opening changed pages is unimplemented.

## Concrete checks / controls

**A. Committed-bytes audit (fails today; cheap, no network).**
```
grep -c 'a799805f3a285390c1b6e906b691f56684fa1031b499d177f664f464d99fb684' verifiers/check_skill_evals.py   # 1 (counter locus OK)
grep -nE '^\| S(212|213) \|' corpus/SOURCES.md | grep -cE 'a799805f|7cc54fbb'                                 # want 2; today 0
test -e .ufo/waves/round-70/snapshots/FETCH-LOG.tsv                                                          # want 0; today 1 (absent)
grep -cE '^S(209|210)\t.*\t200\t(16973|13403)\t' .ufo/waves/round-70/snapshots/FETCH-LOG.tsv                 # want 2; file absent
```
Expected post-fix: 2 / 0 / 2. Each line is independent, so a partial fix shows as a partial score.

**B. Counter arms for the successor (v3) — offline fixtures, no fetch.**
- `(a')` page-unique token: at least one 5-word shingle of the quote is word-bounded in exactly one snapshot of
  the set. The arm must fire on position/uniqueness, not on key terms, so the fixture page carries a pinned key
  term in its **subtitle** (the technique `check_spec_craft.py:1067-1069` already uses).
- `(d')` position: quote offset > offset of the first `^# ` line, and outside the leading `>` banner block and
  the subtitle line. Mutant: quote = subtitle sentence (`…/S210-optimizing-descriptions.md:7`) → exit 1.
- `(e')` anchor digest: the cited row's anchor cell contains the 64-hex snapshot digest. Mutant: S212 anchor with
  the correct upstream commit but no digest → exit 1. This is the only arm that makes Q70 §2 enforceable.
- `(f')` fetch record: `FETCH-LOG.tsv` row `status 200` and bytes/sha equal to the snapshot, else exit 2; a `404`
  row or a body whose digest differs → exit 1. Arm the missing-file case to exit 2 (could-not-evaluate), not 1.
- `(g')` drift world: two snapshots, one with a paragraph added and all eight quotes intact. Offline form:
  point the manifest at digest A while the snapshot bytes hash to B → today's sha conjunct already exits 2, but
  record that the `--fetch` half still prints `8 of 8`; that is the half Q70's fetch-record locus is meant to
  close and the half this seat cannot observe without a live fetch.

**C. Where the lands must go.** v1 is frozen (`SCORECARD.md:448`, sha256 `fc768197…`) — Q73/Q28 forbid widening
it after data. The arms belong in a successor counter plus, if a claim is made, the cited rows' anchor cells and
a `FETCH-LOG`-shaped record for the three r70 snapshots.

## Risks and limits

- **Secondary risk, not judged here:** `SKILL.md:503` presents v1 as a live `gate` with "`8 of 8` at the measured
  rev and `0 of 8` at the pinned base" and no `claim withdrawn` annotation (`sed -n '503p' SKILL.md | grep -c
  'claim withdrawn'` → `0`), while the receipt labels that reading hollow. Whether Q46 requires an annotation is a
  disposition for the r70/r71 record owners; only the byte fact is recorded here.
- The positional conjuncts are satisfied by the current data, so this facet is an **enforcement** defect, not a
  false fact (`[INFERENCE]` on reachability via a future fact row).
- No live fetch was performed (seat bound): statements about the live half come from reading
  `live_fetch` in both counters, plus the committed receipts.
- The digest truncation in the entry head (`a799805f…`) is not a defect for Q70 — the full digest is in the
  counter — but a reader cannot verify from the entry alone.

## Retained evidence

Commands above run at `65a5c7a`; outputs retained in this report. Line anchors: `corpus/QUALITY.md:86` (Q70);
`corpus/knowledge/skill-eval-artefacts-round70.md:1-8`; `corpus/SOURCES.md:150-157`; `SKILL.md:503,505`;
`verifiers/check_skill_evals.py:47-54,58-67,89-96,160,178-190`; `verifiers/check_skill_evals_v2.py:35-40,
78-82,86,148-156,275,295-308,321-334`; `verifiers/check_spec_craft.py:47-61,199,1067-1069`;
`.ufo/waves/round-70/receipts/C2-measure-tip.txt:1-10`; `corpus/lessons/round-70.md:238-241,270-277`;
`corpus/lessons/round-74.md:90`; `SCORECARD.md:448`; `.ufo/waves/round-74/snapshots/FETCH-LOG.tsv:1-4`.
