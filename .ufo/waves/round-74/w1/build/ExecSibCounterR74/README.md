# C2 frozen counter — `check_sibling_reread.py` (round 74, wave 1)

Draft for `verifiers/check_sibling_reread.py`. Seat `ExecSibCounterR74`.
Nothing in this directory is landed; the L1 copies the counter to `verifiers/`
and registers it (see § Integration, below).

## Predicate (frozen in the round-74 plan § C2)

```
python3 -B verifiers/check_sibling_reread.py --rev <rev>
    -> prints "sibling rows re-pinned and re-read N of 20", exit 0 when N == 20
```

Lane `L` of the 20 frozen in `.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv`
is re-pinned and re-read at `--rev` iff (a) its row in
`corpus/knowledge/sibling-overlap-census-round74.md` is the only row for `L` and
passes the BASE copy of `verifiers/check_sibling_census.py`'s row checks, (b) its
commit cell is exactly the frozen head and that commit is an ancestor of the
lane's frozen branch, (c) its `delta` cell equals the counter's recomputation of
`git diff --shortstat <r49 pin> <freeze head> -- SKILL.md PROVINCE.md`, (d)
`PROVINCE.md` § Adjacent at `--rev` carries the same commit and classification,
(e) a `none` row's pinned `SKILL.md`/`PROVINCE.md` does not name `kotoba`.

## Replay

```sh
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin

# the measurement (from the committed path, after the L1 lands it)
python3 -B verifiers/check_sibling_reread.py --rev <rev>
# 0 of 20 and exit 1 at the round-74 base (the entry does not exist there)

# Q66 relative-repository arm
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
python3 -B verifiers/check_sibling_reread.py --rev HEAD --repo . --fleet /home/vgpnk/Projects/shokunin

# the mechanical cells an entry author copies (frozen head, skill file,
# names-kotoba, arbitration, delta); the counter never accepts these as a verdict
python3 -B verifiers/check_sibling_reread.py --emit-cells --repo .

# the self-test on a throwaway fixture fleet
python3 -B verifiers/check_sibling_reread.py --self-test
# -> "self-test: 0 failure(s) over 34 assertions", exit 0

# a seat measuring a different base copy / another freeze file
python3 -B verifiers/check_sibling_reread.py --rev <rev> --freeze <path>
```

Exit ladder: `0` N == 20 and the base census-wide checks clean; `1` N < 20 or a
census-wide refusal; `2` could-not-evaluate (bad arguments, the repository is
not the lane, the base checker absent or its sha256 not the pin, the freeze file
absent / sha-mismatched / not 20 lanes).

**`--repo` is not the cwd.** With no `--repo` the counter measures the git
toplevel of *its own file's directory* (Q33: the committed path decides), so a
draft copy sitting under the live lane keeps measuring the live lane even when
you `cd` into a sandbox. A sandbox replay from a draft copy must pass
`--repo <sandbox> --rev HEAD --fleet <fleet-or-sandbox-parent>`; a copy landed at
`verifiers/` inside the sandbox needs no flag. A silent `0 of 20` is the
signature of the wrong repository, not of a measurement.

**Conjunct (e) and `tabi` (pre-data decision for the L1).** At the frozen head
`856fa9e12021…` tabi's `SKILL.md` carries the whole word `kotoba` at lines 1313
and 1450 inside a shell snippet (`LANES="… kotoba …"`), while its frontmatter
description does not name kotoba. The base checker's `none` rule therefore
passes an r49-style `none` row for tabi and conjunct (e) refuses it. N == 20 is
reachable by classifying tabi non-`none` (with a boundary sentence, PROVINCE
agreeing), or by a **pre-data** amendment of (e) that ignores fenced code —
that choice is the L1's, not the counter's. See the seat report § Calibration.

## Pins (constants in the file; no CLI flag sets them)

| pin | value |
|---|---|
| `BASE_REV` | `1e03d1991bc02281b00a5b7a5e00c9d5d5d72908` |
| `BASE_CHECKER_SHA256` | `2f9d8a88b1d3dd8562455006d5ea89ec02546a1ecb9d023f327d88e5502eedc7` |
| `FREEZE_SHA256` | `6e6012fc800d0f8da9666a2c1ad42934c6de4c0225d97391ae72c97ecdee195d` |
| `FREEZE_LANES` | `20` |

The base checker's bytes are fetched with `git show BASE_REV:verifiers/check_sibling_census.py`
from the measured repository, hashed, refused when they differ from the pin, and
imported from a temporary copy: the measured revision supplies bytes, never code
(Q33). `--freeze PATH` overrides the file (the default path is sha-pinned).

## Entry row shape the counter accepts

Ten cells, the round-49 nine in order plus a trailing `delta`:

```
| lane | branch | commit | skill file | classification | names kotoba | arbitration | scope quote at | scope quote | delta |
```

* `commit` — the frozen head, all 40 hex characters, exact (a prefix fails (b)).
* `delta` — `+<insertions>/-<deletions>` summed over `SKILL.md` and `PROVINCE.md`
  between the r49 pin and the frozen head, or `none` when the diff is empty.
  `+30/-0` is written with the zero; `0` insertions is never omitted.
* `skill file`, `names kotoba`, `arbitration` — copy `--emit-cells`; a lane with
  no `SKILL.md` at the frozen head reads `NONE` / `no SKILL.md` / `no SKILL.md`.
* The tenth cell is stripped before the nine are handed to the base copy of
  `check_sibling_census.py`; that file's bytes are never edited, and its
  census-wide lane-set and duplicate-row checks are its own.

Real-fleet cells at the freeze heads (`--emit-cells`, 2026-10-25): 15 lanes have
a non-`none` delta (chousa `+187/-20`, kaidoku `+447/-2`, kake `+955/-5`, kama
`+417/-8`, kasegi `+72/-1`, kengaku `+30/-0`, kotodama `+85/-0`, kumitate
`+106/-12`, mado `+118/-0`, mori `+462/-15`, revenger `+618/-0`, souji `+2/-2`,
tabi `+89/-0`, tameshi `+108/-43`, tsukuroi `+872/-0`); the other 5 (audio,
game-dev-2d, game-dev-3d, kagi, lore) read `none`.

## Integration (L1)

1. `cp .ufo/waves/round-74/w1/build/ExecSibCounterR74/check_sibling_reread.py verifiers/`.
2. One `## Gate registry` row in `SKILL.md`, eight cells:
   `| \`verifiers/check_sibling_reread.py\` | gate | \`python3 -B verifiers/check_sibling_reread.py --rev <rev>\` | 0=clean, 1=failed, 2=could-not-evaluate | \`--self-test\` | \`verifiers/check_sibling_census.py\`, \`.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv\` | none (read-only) | kotoba |`
   (both pinned-values paths exist at the measured revision; the self-test cell
   names the exact `add_argument` flag).
3. Optional but recommended: a `check_assertion_floors.py` `INSTRUMENTS` row
   (`("verifiers/check_sibling_reread.py", 34, r"(?m)^self-test:\s*(\d+) "
   r"failure\(s\) over (\d+) assertions$", 2, 1)`) so silent arm deletion is a
   floors FAIL; the self-test prints the lane-convention summary line.

## Limits (Q26/Q51, named in the counter's docstring)

The counter measures pins, one shortstat delta, the cells, quote location and the
mechanical `none` rule. It does not measure whether `adjacent`/`contested`/`none`
is the right classification, nor whether a boundary sentence reads correctly: that
is a reviewer judgement for named non-author wave-2 seats. Siblings keep moving
after the freeze; a row is valid at its frozen head, not at the round end.
