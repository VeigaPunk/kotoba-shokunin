# R75Facet61 — Q70's token-uniqueness and error-body clauses versus the landed counter

Seat `R75Facet61` (leaf, read-only, no delegation). Measured revision:
`git rev-parse HEAD` → `65a5c7a663249e0522cc49e4a148424200d9ddfe`. Every cited lane path is
committed at that revision (`git status --porcelain -- <path>` printed nothing; only
`.ufo/waves/round-75/` and a sibling's `corpus/lessons/round-75.md` are untracked). No lane
file was edited, no self-test was run, no page fetched, no model experiment.

Axes named: **depth** (is the bar's rationale tied to an observed failure?), **calibration**
(does the bar state the rule the landed instrument enforces?), **consistency** (do the bar,
the registry row and the code say the same thing?). No claim of improvement or harm to
freshness, operability or adjacency beyond the observations below.

## Facet

`corpus/QUALITY.md:86` — **Q70**, verbatim (folded only at cell boundaries):

> A counter's token and quote conjuncts are run against what every page of the source shares
> (site banner, page subtitle, navigation) and against an error body: **a counted token
> occurs in the claimed page and in no other page of the set**, a counted quote's line lies
> after the page's first heading and outside its subtitle block, and a snapshot's sha256 is
> pinned in the counter, in the cited registry row's anchor and in a fetch record that reads
> HTTP 200.

`applies to`: "claim counters over fetched pages". Grounded in M137
(`corpus/lessons/round-74.md:90`: "counter admits site chrome and error bodies … the frozen
C1 predicate read `3 of 3` … (W2), the page subtitle (W5), a wrong registry id (W3), a
token-stuffed action cell (W4) and a 404 body (W6)"), with the fix named as E1.1 (a′)–(e′)
and the receipt `receipts/c1-selftest-freeze.txt`.

This facet is the **token conjunct and the error-body clause** of that row. The quote-line
clause (d′) and the digest clause (c′) are observed here only to separate them from what the
token conjuncts actually enforce.

## Observed (committed bytes)

1. **The instrument enforces the existential, not the universal.**
   `verifiers/check_spec_craft.py:895-899` requires *each* token to occur in the claimed
   page; `:903-906` then requires **at least one** of the located tokens to be page-unique:
   `if located and not any(page_unique(t, snap, others) for t in located)`.
   `page_unique` (`:760-762`) is occurrence in the own snapshot and in none of the other two.
   The same `any()` shape governs the SKILL.md action cells at `:806`. There is no `all()`
   over the token cell anywhere in the file.
2. **The registry row states the existential, correctly.** `SKILL.md:511` describes the
   counter as "one rule row with ≥2 tokens (**≥1 page-unique**)". So `SKILL.md:511` matches
   the code; `corpus/QUALITY.md:86` states a different, stronger rule.
3. **The self-test has no mixed-token world.** `verifiers/check_spec_craft.py:1694-1697`
   is the only token-uniqueness arm and its label is "*every* located token is shared site
   text" (tokens `SKILL.md` + the banner sentence); `:1751-1755` is the (e′) analogue (one
   action cell whose only token is shared). `receipts/c1-selftest-freeze.txt:75` records that
   arm passing, and `:92` records `self-test: 0 failure(s) over 250 assertions`.
4. **The 404 arm is a fetch-record status arm, not an error-body token/quote arm.**
   `verifiers/check_spec_craft.py:1722-1725` rewrites `\t200\t` → `\t404\t` in `FETCH-LOG`
   and expects `fetch record status '404'`. `grep -rn 'error body\|error-body' verifiers/*.py`
   prints nothing; the only committed error-body bytes sit in the pre-freeze seat tree
   `.ufo/waves/round-74/w1/build/CriticClaimsR74/c1worlds/W6_404_snapshot/snapshots/`
   (first lines: `## Documentation Index` / `Fetch the documentation index at: …` /
   `Use this file to discover all available pages before exploring further.`), built by
   `w1/build/CriticClaimsR74/probe_c1_predicate.py:591-601`.
5. **The three digest pins agree.** `sha256sum .ufo/waves/round-74/snapshots/*.md` equals
   `PAGE_SHA` (`verifiers/check_spec_craft.py:203-210`) equals the sha256 column of
   `snapshots/FETCH-LOG.tsv` (all three rows `200`). The anchor-cell check is `:909-914`,
   the fetch-record check `:915-931`. Q70's third clause is implemented as written.
6. **Today's entry would survive either reading.** Measured with the counter's own
   `word_bounded`/`page_unique` over the committed snapshots (all nine tokens of
   `corpus/knowledge/spec-skill-creation-craft-round74.md:86-90`):

   ```
   best-practices  references/api-errors.md                      own=1 others={0,0} unique=True
   best-practices  python scripts/migrate.py --verify --backup    own=1 others={0,0} unique=True
   best-practices  references/schema.yaml                        own=1 others={0,0} unique=True
   using-scripts   uvx ruff@0.8.0 check .                         own=1 others={0,0} unique=True
   using-scripts   pipx run 'black==24.10.0' .                    own=1 others={0,0} unique=True
   using-scripts   npx package@version                            own=1 others={0,0} unique=True
   quickstart      .agents/skills/roll-dice/SKILL.md              own=3 others={0,0} unique=True
   quickstart      .agents/skills/                                own=1 others={0,0} unique=True
   quickstart      /skills                                        own=1 others={0,0} unique=True
   ```

   So the divergence is not a red today; it is a divergence in what the bar promises.
7. **A mixed token cell is accepted.** Same helpers, real snapshots:

   ```
   tokens ['SKILL.md', 'references/api-errors.md']   rule_a=True rule_a_prime=True q70_literal=False
   tokens ['SKILL.md', 'scripts/validate.py']        rule_a=True rule_a_prime=True q70_literal=False
   tokens ['description', 'references/schema.yaml']  rule_a=True rule_a_prime=True q70_literal=False
   ```

   (`description` occurs 1/1/5 times across the three snapshots, `SKILL.md` 5/6/6 — measured
   in this seat.) A cell pairing one chrome-shared token with one page-unique token counts as
   a rule row, while Q70's literal sentence ("a counted token occurs … in no other page")
   is false of it.
8. **Scope cell vs the other fetched-page gates.** `grep -c 'page-unique' verifiers/check_skill_evals.py
   verifiers/check_skill_evals_v2.py verifiers/check_spec_craft.py` → `0 0 7`. Both
   `SKILL.md:503` (`check_skill_evals.py`) and `SKILL.md:505`
   (`check_skill_evals_v2.py`) are live `gate` rows over fetched snapshots; neither carries
   a page-uniqueness, heading, subtitle or chrome guard (`grep -n 'heading\|subtitle\|blockquote\|chrome'`
   in v2 prints nothing). No lane record annotates them as pre-Q70 and exempt.

## What this is worth

- **Falsifiable as a bar, not as landed.** Q70's token conjunct as written is decidable on a
  fixture (`all()` vs `any()`), and the two diverging surfaces (`QUALITY.md:86` vs
  `SKILL.md:511` + code) are the falsifier. The rule is *not* presently demonstrated by any
  shipped arm in either direction: no world passes with a mixed cell (would print the
  divergence as exit 0), and no world fails a mixed cell under a corrected predicate.
- **Depth is real.** M137 is an observed mistake with committed worlds and a pre-freeze
  measurement (`w1/CriticClaimsR74.md:92-132,151-161`), not a hypothesis. Q70's rationale is
  sourced; the defect is in its wording and in the arm set, not in the motivation.
- **The error-body clause is attributed to the wrong conjunct.** Q70 says the *token and
  quote conjuncts* are run against an error body. In the shipped instrument an error-body
  snapshot is refused by the constant digest `PAGE_SHA` (`:552`, exit 2
  `snapshot_pin_mismatch`; arm `:1735-1739`) and by the `status != "200"` check (`:922`).
  The token and quote conjuncts never see error-body text; the only committed error-body
  world (W6) was scored on the seat's `probe_c1_predicate.py`, not on the counter. The
  clause is therefore true of the *system* and false of the *conjuncts it names* — a
  calibration defect a reader would inherit if they cloned the row into a new counter.
- **A description audit must not cite Q70 on the strength of this counter.** What is
  actually enforced per row: ≥2 tokens, each present in the claimed page, ≥1 page-unique;
  exactly one 5–25-word quote, found verbatim after whitespace collapse, after the first
  `# ` heading, not a heading, not the subtitle blockquote, not a cross-page link; digest in
  counter + anchor + 200 recording. That is what an r75 description-audit claim may assert.
  "Every counted token is page-unique", "the counter tests an error body with its token and
  quote conjuncts", and "all lane counters over fetched pages meet Q70" are **not**
  supported.

## Concrete checks and controls (cheap, read-only)

| # | Check | Expected today | Purpose |
|---|---|---|---|
| C1 | Add a self-test world `(a') mixed token cell` whose `best-practices` tokens are `` `SKILL.md`, `references/api-errors.md` `` (fixture analogue: `` `SKILL.md`, `scripts/validate.py` ``) and assert the current verdict | exit 0, `3 of 3` unchanged — no finding line | records that the instrument passes a cell Q70's literal sentence rejects; assertion count goes 250 → 251 |
| C2 | Same world under a corrected predicate (every located token page-unique) | exit 1 with `no page-unique token among` / `carries a shared token` wording | the must-fail arm Q70 needs before it can be cited as enforced |
| C3 | Error-body arm: quote cell = `Use this file to discover all available pages before exploring further.` from the committed W6 body, snapshot unchanged | exit 1 at `not found in best-practices.md after whitespace collapse` | shows error-body text is refused by (d) presence, not by any error-body-specific clause |
| C4 | Error-body arm: snapshot replaced by the W6 bytes, manifest/anchor/fetch re-signed with a 200 record | exit 2 `snapshot_pin_mismatch` | the only error-body refusal that exists is (c′) constant-pin |
| C5 | `grep -c 'page-unique' verifiers/check_skill_evals.py verifiers/check_skill_evals_v2.py verifiers/check_spec_craft.py` | `0 0 7` | scope: the row's `applies to` class is wider than its only implementation |

Running C1–C4 requires `--self-test` execution and was deliberately **not** done in this
read-only seat; the code paths quoted above make the verdicts deterministic (C1 exits 0
because `any()` is satisfied at `:905`; C2 exits 1 on the `all()` reading; C3/C4 follow from
`:933-948` and `:552`).

## Risks

- **False red if the bar is implemented literally.** A future description-audit counter that
  copies Q70's sentence would refuse an honest row whose token cell carries shared-but-real
  page text (`SKILL.md`, `description`, `agentskills.io`), which today's rejection classes do
  not require (Q18/Q05: a new false red is harm). The current entry is safe only because all
  nine of its tokens happen to be page-unique — a property of the data, not of the rule.
- **Bookkeeping direction.** QUALITY rows are append-only and are never rewritten
  (`corpus/QUALITY.md:1-6`); reconciling the wording with the code is a new superseding row
  plus an appended note, i.e. an L1 decision. This seat records it, it does not edit it.
- **Freshness.** The r74 wave that was supposed to attack Q70–Q72 was never dispatched:
  `.ufo/waves/round-74/w2/` holds only `swarm-registry.json`, there is no `w2-results.json`,
  and HEAD `65a5c7a` is titled "mark the never-taken w2 wave abandoned so no dispatcher
  spawns it". `grep -rn 'Q70' corpus/lessons/` finds only the pointer at
  `corpus/lessons/round-74.md:95` and the spot-check's "Q70–Q73 each rest on a recorded
  mistake" (`corpus/lessons/round-74-verifier-spotcheck.md:132`); no text in the lane
  critiques the row's wording. This finding is not a repeat.

## Evidence commands

- `sed -n '86p' corpus/QUALITY.md` and `git show HEAD:corpus/QUALITY.md | sed -n '86p'` — Q70 as committed.
- `awk 'NR>=895&&NR<=907' verifiers/check_spec_craft.py` — (a) presence loop and the `any()` (a′) check.
- `sed -n '760,762p;806p' verifiers/check_spec_craft.py` — `page_unique` and the (e′) `any()`.
- `sed -n '203,210p;909,931p' verifiers/check_spec_craft.py` — `PAGE_SHA` and the anchor/fetch-log conjuncts.
- `sed -n '1694,1697p;1722,1725p;1735,1739p;1751,1755p' verifiers/check_spec_craft.py` — the four arms relied on here.
- `sed -n '511p' SKILL.md` — registry row: "≥2 tokens (≥1 page-unique)".
- `sha256sum .ufo/waves/round-74/snapshots/*.md` vs `PAGE_SHA` vs `snapshots/FETCH-LOG.tsv`.
- `grep -n 'assertions' .ufo/waves/round-74/receipts/c1-selftest-freeze.txt` → `:92` `0 failure(s) over 250 assertions`.
- `grep -c 'page-unique' verifiers/check_skill_evals.py verifiers/check_skill_evals_v2.py verifiers/check_spec_craft.py` → `0 0 7`.
- `sed -n '86,90p' corpus/knowledge/spec-skill-creation-craft-round74.md` — the nine committed tokens measured in §6.
- `ls .ufo/waves/round-74/w1/build/CriticClaimsR74/c1worlds/` — W0–W8 worlds, incl. `W6_404_snapshot`.

## Limits

No `--self-test` run, no `--fetch`, no live page. The C1–C4 verdicts are derived from the
committed code paths and are marked as such; the mixed-cell and token-uniqueness figures are
computed from committed snapshot bytes with the counter's own helper functions (imported
read-only; the resulting gitignored `verifiers/__pycache__/check_spec_craft.cpython-314.pyc`
was removed). This report makes no claim about any current r75 description, and none about
which of the two readings the L1 intends to keep.
