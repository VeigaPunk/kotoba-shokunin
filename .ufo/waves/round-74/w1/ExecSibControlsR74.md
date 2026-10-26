# ExecSibControlsR74 — C2 shortcut worlds for the round-74 sibling re-read

**Verdict: nine worlds built and measured with the real counter; none of the
eight non-carry-forward worlds reaches 20, so the C2 kill rule is not
triggered. The carry-forward world scores 18 of 20 (measured), one mechanical
cell set away from 19 — and the plan's stated failure mode for world 1, "quotes
die at moved lines", did not happen: all 20 round-49 quotes re-locate at the
same line numbers at the freeze heads. Two frozen-conjunct hazards are visible
before data: conjunct (e) rejects the honest `none` row for `tabi` on a shell
snippet — tabi is the single row that blocks a fully mechanical 20 — and
`revenger` gained a `SKILL.md` at its freeze head, so its round-49 `NONE` cells
are stale.**

Seat: `ExecSibControlsR74`. Wrote only under
`.ufo/waves/round-74/w1/build/ExecSibControlsR74/` and this report. No lane
file, sibling repo, fleet repo or jj state touched; all git writes happened
inside `mktemp` sandboxes.

## Deliverable

`.ufo/waves/round-74/w1/build/ExecSibControlsR74/` (bundle README has the full
index): nine `world-*/` bundles + `diag-2b-recomputed/`, each with
`overlay/{corpus/knowledge/sibling-overlap-census-round74.md,PROVINCE.md,.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv}`
and a README replay; `build_worlds.py` (the generator, so world 2 is an actual
script, not a hand edit), `analyze.py` + `lanes.json` (per-lane facts at the
freeze heads), `emulate_reread.py` (expected-score emulator),
`score_worlds.sh`, `collect_expected.py`, `record_measured.py`, `logs/`.

## Measured scores (counter present and run)

Counter: `.ufo/waves/round-74/w1/build/ExecSibCounterR74/check_sibling_reread.py`
(sha256 `0042cb42d7ef92b51e0f376a144dfbed9dd47355b656be0ac52b466bd5042074`; not
yet landed at `verifiers/check_sibling_reread.py` at measurement time).

```
$ .ufo/waves/round-74/w1/build/ExecSibControlsR74/score_worlds.sh \
    .ufo/waves/round-74/w1/build/ExecSibCounterR74/check_sibling_reread.py \
    /home/vgpnk/Projects/shokunin --diag
# mode: measured with .../check_sibling_reread.py
world-1-bump-only 0 of 20 1
world-2-carry-forward 18 of 20 1
world-3-missing-row 17 of 20 1
world-4-duplicate-row 17 of 20 1
world-5-not-freeze-head 17 of 20 1
world-6-quote-absent 17 of 20 1
world-7-province-unchanged 4 of 20 1
world-8-none-names-kotoba 17 of 20 1
world-9-delta-wrong-numbers 17 of 20 1
diag-2b-recomputed 19 of 20 1
```

Each replay is a fresh fleet-shaped sandbox: every fleet entry except
`kotoba-shokunin` symlinked, `git clone --shared --no-checkout` of the lane,
`checkout 1e03d199`, the overlay copied over it, one commit under a throwaway
identity in the sandbox, then
`python3 -B <counter> --repo <sandbox> --rev HEAD`. Wall time 25–41 s for all
ten bundles; each counter invocation is one process and under the 300 s bound.

Two of these are easy to mislabel, so, exactly: **19 (`diag-2b-recomputed`)** is
world 2's overlay — `PROVINCE.md` already re-pinned, quotes re-located, deltas
computed — with **only** `revenger`'s three mechanical entry cells recomputed;
nothing else is. **4 (`world-7-province-unchanged`)** is that same world-2 entry
against the base `PROVINCE.md` § Adjacent, so it isolates the province conjunct
and no other difference.

The same nine numbers were produced before the counter landed by
`./score_worlds.sh --emulate` (the plan's conjuncts applied with the base copy
of `check_sibling_census.py`), which is why they are quoted as expected in the
per-world READMEs' history.

## Findings

### F1. No round-49 quote dies at its freeze head — the plan's world-1 rationale is falsified

`analyze.py` re-locates every round-49 quote at the pinned head (single lines,
then windows of up to six lines for folded paragraphs): all 20 are found, and
all 20 sit at the **same** line as the round-49 citation (`lanes.json`:
`quote_new_line == cited` for 20 of 20).

Independent confirmation from the base checker, run in a sandbox over
world-1-bump-only (nine-cell table, commits bumped only), logged at
`logs/world-1-bump-only.base-census.log`:

```
FAIL row 16 (census line 84) (lane revenger): SKILL.md exists at the pin but the skill cell says NONE
FAIL row 16 (census line 84) (lane revenger): names-kotoba cell 'no SKILL.md' but the pinned description gives 'no'
FAIL row 16 (census line 84) (lane revenger): arbitration cell 'no SKILL.md' but the pinned description gives 'no'
rows 20 verified 19
province rows 20 matched 20
```

So the plan's sentence "quotes die at moved lines for the changed lanes"
(§ C2 shortcut controls) is not true at these heads: quoting survives the
re-pin. World 1 scores 0 for a different reason (F2), and any reviewer who
reads world 1's 0 as "the quotes died" would record the wrong mechanism.

### F2. World 1's 0 is a table-shape failure, not a content failure

```
$ sed -n '4,6p' logs/world-1-bump-only.log
base census: rows 0 verified 0 (delta cell stripped, base-row checks)
note entry has no census table with 10 cells and a trailing `delta` cell (round-49 nine-cell row shape plus delta)
FAIL census-wide census table not found in corpus/knowledge/sibling-overlap-census-round74.md at 62b9975a3211 (no ten-cell row)
```

(the first three log lines are the resolved repo, freeze file and fleet; the
sandbox commit id differs per replay because the commit carries a timestamp).

The counter's `parse_entry` requires ten cells with a trailing `delta` header,
so the literal "copy with commits bumped and nothing else" is refused before
any row is read. Consequence for the plan: world 1 as written cannot test what
it was meant to test (quote death); its low score is carry-over from the shape.

### F3. Carry-forward = 18 of 20; two rows cost it, and both are named by the counter

```
$ grep ': FAIL' logs/world-2-carry-forward.log
lane revenger: FAIL base row check: row 16 (census line 20) (lane revenger): SKILL.md exists at the pin but the skill cell says NONE; ...
lane tabi: FAIL classified none, but SKILL.md at the frozen head 856fa9e12021 names kotoba whole-word
$ grep -c ': ok$' logs/world-2-carry-forward.log
18
```

Per-conjunct survival for the carry-forward (emulator; the counter's two
failure lines above are the same two lanes, so the measured per-conjunct
counts agree): **(a) 19/20, (b) 20/20, (c) 20/20, (d) 20/20, (e) 19/20.**
Lanes whose quotes die: **none**. Lanes failing (a): `revenger` only. Lanes
failing (e): `tabi` only.

`revenger`: the mechanical cells changed, not the quote.

Run from `/home/vgpnk/Projects/shokunin`:

```
$ git -C revenger-shokunin cat-file -e 876630db:SKILL.md   # r49 pin in the census row
fatal: path 'SKILL.md' exists on disk, but not in '876630db'   # exit 128
$ git -C revenger-shokunin cat-file -e 6da884c6:SKILL.md   # freeze head
# exit 0
```

The honest r74 row must read `SKILL.md | no | no` for revenger (from
`lanes.json` `mechanical_cells_at_head`); a script that only bumps commits
carries `NONE | no SKILL.md | no SKILL.md` and loses the row. With those three
cells recomputed the same overlay scores **19** (`diag-2b-recomputed`, measured
above, only `tabi` left).

### F4. Conjunct (e) as frozen fires on a body-only `kotoba` token — the honest `none` row for `tabi` cannot pass

Run from `/home/vgpnk/Projects/shokunin`:

```
$ git -C tabi-shokunin grep -w -in kotoba 856fa9e1 -- SKILL.md PROVINCE.md
856fa9e1:SKILL.md:1313:  `LANES="protocol aggregator kasegi kengaku kake kumitate kotoba kagi kama"`
856fa9e1:SKILL.md:1450:  `LANES="protocol aggregator kasegi kengaku kake kumitate kotoba kagi kama"`.
```

Both hits are a shell `LANES=` list inside a code snippet, not a scope
statement. The round-49 census classes `tabi` `none` on its rule, and its own
falsify correction keeps the wave-report split out of the scope surfaces. The
base checker's `none` rule (frontmatter description + `PROVINCE.md`) passes
tabi; the round-74 counter's (e) — "the pinned `SKILL.md` **or** `PROVINCE.md`
contains the whole word `kotoba`" — refuses it. What (e) forbids is narrow and this is the
measured statement: **the counter refuses tabi as `none`**, so tabi is the one
row that blocks a fully mechanical 20 (`diag-2b-recomputed` = 19, tabi the only
failure). N == 20 is still counter-reachable by classifying tabi `adjacent` or
`contested` with a PROVINCE row that agrees — the counter accepts any of the
three classes. Whether that reclassification is honest is not mine to call: the
round-49 entry records that tabi's split "never reached tabi's scope surfaces,
so the row stays `none`"
(`corpus/knowledge/sibling-overlap-census-round49.md`, falsify corrections,
tabi bullet), and the plan assigns classification judgement to the wave-2
seats. So the L1 has two live options before data — narrow (e) to the base
description+PROVINCE rule (or ignore fenced code), or reclassify tabi and
defend it in wave 2 — and they are not equivalent: the first keeps the census's
substance, the second buys the count with a class the rule does not support.
This is the one place where the controls measured a predicate question rather
than a counter question, and the plan's before-data window is the only place it
can be settled.

### F5. Each control isolates exactly one conjunct (measured)

The only constant failures across worlds 2–9 are `revenger` (a) and `tabi`
(e); every world adds exactly its intended lane:

| world | extra failing lane | counter line (`logs/<world>.log`) |
|---|---|---|
| 3 missing row | `lore` | `FAIL census-wide lane set: 1 sibling lane(s) never surveyed: lore` |
| 4 duplicate row | `lore` | `FAIL census-wide census table: lane lore appears in more than one row (rows 13 (line 17), 21 (line 25))` |
| 5 not freeze head | `kumitate` | `lane kumitate: FAIL commit cell fac39171ac28 is not the frozen head 2ca91a0c8154` |
| 6 quote absent | `kagi` | `lane kagi: FAIL base row check: row 5 (census line 9) (lane kagi): quote not found at SKILL.md:3 (+/-2 lines)` |
| 8 none names kotoba | `kagi` | `lane kagi: FAIL classified none, but SKILL.md at the frozen head 69b61db46be4 names kotoba whole-word` |
| 9 delta wrong numbers | `kake` | `lane kake: FAIL delta cell '+954/-5' but the recomputation gives '+955/-5' ...` |

World 7 (`PROVINCE.md` unchanged) passes exactly the four lanes whose round-49
pin already equals the freeze head:

```
$ grep ': ok$' logs/world-7-province-unchanged.log | awk '{print $2}' | tr -d ':' | tr '\n' ' '
audio game-dev-2d game-dev-3d lore
```

The 16 failures are exactly the 16 lanes whose round-49 pin differs from the
freeze head (`kagi` is among them: pin `899c50b4`, head `69b61db4`, six
commits), so the `## Adjacent` table is load-bearing for 16 of 20 lanes: an
entry-only landing scores 4.

### F6. Two measurement traps found while replaying (both worked around, none affecting the scores)

1. The counter resolves the lane from **its own file path**, not from cwd
   (`resolve_repo`: `start = Path(__file__).resolve().parent`). A first run of
   `score_worlds.sh` measured the live lane at `329e7d91` and printed 0 for
   every world:

   ```
   # mode: measured with .../check_sibling_reread.py
   world-1-bump-only 0 of 20 1
   ... (all worlds 0)
   $ head -4 logs/world-2-carry-forward.log
   repo /home/vgpnk/Projects/shokunin/kotoba-shokunin rev 329e7d91d7d7 base 1e03d1991bc0
   note entry absent at the measured revision
   ```

   `score_worlds.sh` now passes `--repo <sandbox> --rev HEAD`. At the intended
   landing path (`verifiers/`) the default resolves correctly, so this is a
   sandbox trap, not a counter defect — but it makes a silent 0 look like a
   real measurement, which is exactly the failure mode the worlds exist to
   catch.
2. The freeze receipt is not in the base worktree
   (`git cat-file -e 1e03d199:.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv`
   → absent; present at `329e7d91`), so every overlay copies it in. That copy is
   **not necessary**, and my first draft of this report said it was: the counter
   falls back to `git rev-list --all -- <path>` and reads the receipt from the
   object store. Measured with the same world-2 overlay and no worktree receipt:

   ```
   $ (cd $P/kotoba-shokunin && python3 -B .../check_sibling_reread.py --repo $P/kotoba-shokunin --rev HEAD)
   freeze .../sibling-heads-freeze.tsv (pinned, object store at 329e7d91d7d7), 20 lanes, sha256 6e6012fc800d0f8da9666a2c1ad42934c6de4c0225d97391ae72c97ecdee195d
   base census: rows 20 verified 19 (delta cell stripped, base-row checks)
   sibling rows re-pinned and re-read 18 of 20
   # counter exit=1
   ```

   Same 18. The copy stays because it makes a sandbox self-contained, not
   because the counter needs it.

## Peer cross-check (reported by `ExecSibCounterR74`, not re-run by this seat)

The counter's author re-ran the three facts above and agreed with two of them:
`resolve_repo` (their sandbox copies the counter into `$P/kotoba-shokunin/verifiers/`,
so the default already resolved to the sandbox) and revenger's mechanical change
(`--emit-cells` names revenger the only lane whose columns differ from r49). They
corrected my F4 wording, and the correction is in F4 above: (e) forbids only a
`none` row, so 20 stays reachable by classifying tabi non-`none`.

They also confirmed independently, from the base copy's `mechanical_findings`,
that revenger fails three cells at `6da884c6708f` and that setting only
`path=SKILL.md` still fails the row.

Their numbers, quoted as reported and not re-run here: base control 0 of 20 exit
1 (live tree and sandbox at base); self-test 34 assertions, 0 failures, exit 0;
the base checker's own bytes on their fixture green 20 of 20, delta world 19,
quote world 19; carry-forward variants 4 / 5 / 19 of 20 (province unchanged /
deltas claimed `none` / entry and province both recomputed); gate universe 58 at
base, so 58 + 2 = 60 of 60. Reconciled after their check, and the premise is
measurable rather than a matter of wording: recomputing *every* mechanical cell
changes exactly one lane. `lanes.json`: 19 of 20 lanes' round-49 mechanical
cells already equal the head derivation, and `revenger` is the only lane that
moves (`NONE | no SKILL.md | no SKILL.md` → `SKILL.md | no | no`). So their
all-recomputed carry-forward and my `diag-2b-recomputed` hold the same row cells
and the same deltas — the equal 19 is a second measurement of the same fact, not
two different worlds. The same holds for the 4: my
`world-7-province-unchanged` and their `W_d` are the same construction, the one
where conjunct (d) decides. The counter's sha256 is unchanged (`0042cb42…`) and the
landing copy must be byte-identical; `verifiers/check_sibling_reread.py` did not
exist at measurement time, so every score above is against the draft path.

## What this means for the C2 landing

- The carry-forward is **not** a 20: the mechanical re-pin plus script-computed
  deltas reaches 18, or 19 once `revenger`'s three cells are recomputed. The one
  row that a mechanical carry-forward cannot fix is `tabi`, and it fails on a
  frozen-conjunct over-reach (F4), not on the census's substance.
- Therefore the honest entry's remaining work over the shortcut is: recompute
  `revenger`'s mechanical cells, and resolve tabi's (e) status before data.
  Everything else the plan expected a re-read to buy is already carried by the
  script.
- The worlds also show the counter counts what the plan says it counts: shape
  (F2), missing/duplicate/commit/delta/quote/none each cost exactly one lane,
  and no world other than the carry-forward reaches 20.

## Bound

These worlds test one counter over one freeze. They say nothing about whether
any classification (`adjacent`/`contested`/`none`) is the right call, whether a
boundary sentence reads correctly, or whether the sibling heads have moved since
`2026-10-26T01:25:43Z`. The freeze file is the authority for pins, and a row is
valid at its frozen head, not at the round end. No external source was fetched;
no tool was installed; no lane or sibling file was written.
