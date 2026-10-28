# Kb80S10Province — PROVINCE.md `## Core` bullet for C2 conjunct (h)

Base: `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93` (kotoba lane). Scope: exactly one
`## Core` bullet naming `corpus/knowledge/allowed-tools-surfaces-round80.md`, in the
style of the existing Core bullets. No other line of PROVINCE.md is touched.

## The bullet (exact line to insert)

Insert immediately after the round-74 sibling-census bullet (base `PROVINCE.md:33`,
the last `## Core` bullet, which ends `... beside the base
\`verifiers/check_sibling_census.py --province PROVINCE.md\`.`), i.e. as the new
`PROVINCE.md:34`, directly above `## Frontier`:

```
- Allowed-tools surfaces by client (round 80, depth): where the Open specification, Claude Code, Factory, Microsoft Agent Framework, pi and Mistral Vibe document the `allowed-tools` frontmatter field — the value form each page prints and the grant each states (`pre-approves`, `metadata-only`, `experimental`, `unstated`), each read from a snapshot-pinned located quote, form-level documentation only; the grant-semantics matrix is exploratory, reviewed by the round-80 non-author closure spot-check (S226–S231; the six pages re-opened live 2026-10-27) — `corpus/knowledge/allowed-tools-surfaces-round80.md`, counted by `verifiers/check_allowed_tools.py --rev <rev>`.
```

One physical line (no continuation), so the counter's continuation-join path is not
exercised; sentence shape mirrors the existing bullets (`- <topic> (round N, axis):
<what it holds> — \`entry\`, counted by \`counter --rev <rev>\``). It names no lane in
§ Adjacent, no report pointer and no four-hop path.

### Why these words

- The entry path `corpus/knowledge/allowed-tools-surfaces-round80.md` is the literal
  string conjunct (h) matches (a Core bullet must contain it).
- The six surfaces are named with the counter's own frozen display strings (spec =
  "Open specification", claude = "Claude Code", factory = "Factory", msaf =
  "Microsoft Agent Framework", pi = "pi", vibe = "Mistral Vibe"), so
  `surfaces_named` reads 6 of 6 on this bullet; the counter prints that count as
  INFORMATION only (not gated), but naming all six costs nothing and makes the
  bullet answer "which clients" without opening the entry.
- `form-level documentation only` + `the grant-semantics matrix is exploratory,
  reviewed by the round-80 non-author closure spot-check` reproduce the C2 claim
  split (plan § C2, Q71/Q74) inside the bullet so Core does not overclaim: the
  measured part is form, the semantics rider is exploratory with a named reviewer
  class.
- `S226–S231` are the C2 source ids (plan § C2; two of the six are re-opened rows,
  the rest rejection/new rows are not C2 surfaces).

## Verification A — (h) text-match

The round-80 counter (`build/check_allowed_tools.py`, Kb80E07C2Counter) was **not on
disk** at this seat's first checks (absent at 20:14 and after a 180 s bounded wait,
though its author confirmed in IRC that it was published and that the (h) arm is
IDENTICAL to the r79 draft). The first measurement therefore runs the r79 draft's
own functions (`.ufo/waves/round-79/build/check_allowed_tools.py`) with `ENTRY`
rebound to the round-80 path — the draft's literal `ENTRY` is the round-79 path, so
the rebound is the only difference from the published predicate. After the file
appeared (20:19, 103590 B) the verbatim run was taken too; see
§ Verbatim run of the published counter below, which also records a publication
defect in those bytes.

Command (scratch, `python3 - <<'PY'`, importlib load of the draft, exact):

```
spec = importlib.util.spec_from_file_location("alt", "<lane>/.ufo/waves/round-79/build/check_allowed_tools.py")
m = module_from_spec(spec); spec.loader.exec_module(m)
base = <lane>/PROVINCE.md ; edit = $S/PROVINCE-edited.md
m.province_state(base)   # draft ENTRY (round-79 path)
m.province_state(edit)
m.ENTRY = "corpus/knowledge/allowed-tools-surfaces-round80.md"
m.province_state(base)   # round-80 ENTRY, red-before arm
m.province_state(edit)   # round-80 ENTRY, after arm
```

Observed (exit 0; all four calls printed):

| call | ENTRY | (bullets naming the entry, surfaces named) |
|---|---|---|
| base PROVINCE | draft r79 path | `(0, 0)` |
| edited PROVINCE | draft r79 path | `(0, 0)` — expected: the constant differs, not a defect |
| base PROVINCE | r80 path | `(0, 0)` — red before |
| edited PROVINCE | r80 path | `(1, 6)` — exactly one bullet, six surfaces |

Per-surface read-out on the inserted bullet (`surfaces_named` = 6):
spec display True / key False; claude True/True; factory True/True; msaf True/False;
pi True/True; vibe True/True.

(g)-analogue sanity: the same bullet would also satisfy a ≥3-surface requirement;
the published (h) arm needs only the one naming bullet, and `province_bullets`
reads the file's `## Core` section up to the next `## ` heading, so placement above
`## Frontier` is what puts it in scope.

### Verbatim run of the published counter, and the defect in its bytes

`build/check_allowed_tools.py` appeared at 20:19 (103590 B). Two runs, each with its
own exit capture, against a scratch clone at base + this PROVINCE patch + the
published entry (`build/allowed-tools-surfaces-round80.md`, copied to
`corpus/knowledge/`), commit `db47373c59d6d38a00eab901fb1d428aff432b73`:

**(1) the published bytes as they stand** —
`python3 -B build/check_allowed_tools.py --repo <clone> --rev db47373` → **exit 1**:

```
allowed-tools surfaces backed 0 of 6
script-only world: 0 of 6
opened this round 0 of 6
held at base: 5
province surfaces named 0 of 6
skill rule line MISSING
registry home MISSING
  entry corpus/knowledge/allowed-tools-surfaces-round79.md absent at db47373… (the frozen path is the entry's only home)
  0 ## Core bullet(s) name the entry (want exactly 1)
```

These bytes are the **r79 draft unchanged**: `sha256 74e067ccad7813d91826ee503c8ee93ba47d3a4a05b12ec67a82791d93f722a6`
= `.ufo/waves/round-79/build/check_allowed_tools.py` byte-for-byte;
`ENTRY = "corpus/knowledge/allowed-tools-surfaces-round79.md"` at the file's line
190; and the output still uses the r79 wording (`backed N of 6`, `script-only
world`) instead of the round-80 plan's frozen `documented N of 6` / `generator
world: M of 6`. So the published file does not implement the plan's round-80
predicate, and its (h) arm reads 0 for any tree that carries the round-80 bullet.
That is a counter-publication defect (the author reported publishing it; the bytes
say otherwise) — **not** a defect in this bullet. Reported to Kb80E07C2Counter and
to the C1 battery seat.

**(2) the same bytes with only `ENTRY` corrected to the round-80 path**, `SELF_SHA`
refilled by the module's own `_blanked_sha` — exactly the freeze step the counter
file itself documents ("the L1 refills it at freeze"); the variant is
`counter-r80.py` in scratch, not published:
`python3 -B counter-r80.py --repo <clone> --rev db47373` → **exit 1** (other
conjuncts still open), and the province line is:

```
opened this round 6 of 6
province surfaces named 6 of 6
skill rule line MISSING
registry home MISSING
  spec: S226: used-by 'corpus/lessons/round-79.md' does not list corpus/knowledge/allowed-tools-surfaces-round80.md
  ... (all six rows, same used-by finding)
```

**No (h) finding appears** — the counter's own arm reads this bullet as exactly one
naming bullet with six surfaces. The remaining findings belong to other conjuncts
and to files absent from my scratch tree by construction (`SKILL.md` rule line and
registry row were not applied there; `used-by` in `corpus/SOURCES.md` is the C2
census seat's edit).

## Verification B — `check_sibling_census.py` stays green (base vs edited)

Run from the lane root, census = `corpus/knowledge/sibling-overlap-census-round74.md`
(the census the § Adjacent rows are pinned to; the script has no default positional,
so an explicit path is required — without it, exit 2 usage):

```
python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md --province PROVINCE.md
python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md --province <scratch>/PROVINCE-edited.md
```

| input | exit | stdout |
|---|---|---|
| base PROVINCE.md | 0 | `rows 20 verified 20` / `province rows 20 matched 20` |
| edited PROVINCE.md | 0 | `rows 20 verified 20` / `province rows 20 matched 20` |

`diff` of the two outputs: IDENTICAL. The `--skill SKILL.md` form the plan's no-harm
battery names, run the same way on both files, is also identical and green:

```
rows 20 verified 20
province rows 20 matched 20
skill description names 10 of 10 non-none lanes
skill description length 1021 of 1024
```
exit 0 for base and for edited. The script reads only the `## Adjacent` section of
PROVINCE.md (ends at the next `## ` heading), so a `## Core` insertion is outside
its parse by construction — and measurably inert.

## Verification C — corpus integrity observation is unchanged

`python3 -B verifiers/verify_corpus_integrity.py --repo <scratch clone with the
bullet applied> --no-baseline --json` → exit 1, results identical to the base drift
set named in the plan (no new observation class, no count moved):

```
corpus.index.tracked_files 152 OBSERVE
corpus.index.unindexed 1 DRIFT
corpus.index.stale_patterns 0 PASS
corpus.index.missing_paths 0 PASS
corpus.pointers.report_total 109 OBSERVE
corpus.pointers.report_dead 1 DRIFT
corpus.pointers.commit_total 46 OBSERVE
corpus.pointers.commit_unresolvable 2 DRIFT
corpus.pointers.commit_nonhash 0 PASS
```

(PROVINCE.md is not in `verifiers/corpus-baseline.json`: `grep -c PROVINCE
verifiers/corpus-baseline.json` = 0.)

## Verification D — the other gates that read PROVINCE.md are unmoved

`grep -ln "PROVINCE.md" verifiers/*.py` → `check_cn_vendor_surfaces.py`,
`check_correction_sweep.py`, `check_province_core.py`, `check_sibling_census.py`,
`check_sibling_reread.py`, `check_spec_craft.py`. Four of them parse PROVINCE
content; three were run at both revs (`--repo <scratch clone>`, base `398cbe1b` vs
patched `aeb7d8c`, the scratch commit carrying only this bullet):

| gate | base exit | patched exit | stdout diff |
|---|---|---|---|
| `check_province_core.py --rev` | 0 | 0 | none but `measured-rev`; `province core rows 2 of 2` both |
| `check_cn_vendor_surfaces.py --rev` | 0 | 0 | none but `measured-rev`; `province surfaces named 4 of 4` both |
| `check_spec_craft.py --rev` | 1 (base-red: `corpus/SOURCES.md is not census-conformant … (conjunct (b))`) | 1 same findings | none but `measured-rev`; `province core names the entry: yes` both |

`check_province_core.py` additionally pins `§ Frontier` and `§ Adjacent`
byte-identical to its round-69 BASE: this edit leaves both sections untouched and
the gate stays at `2 of 2`, exit 0. `check_correction_sweep.py`'s PROVINCE entries
are frozen slices of earlier rounds' text; the inserted bullet adds no frozen id
and no amended line. `check_sibling_census.py` / `check_sibling_reread.py` read only
`§ Adjacent` (Verification B).

## Patch provenance

- Patch: `.ufo/waves/round-80/build/Kb80S10Province.patch`, one hunk, `PROVINCE.md`
  only, `git -C <base clone> apply --check` → exit 0; `git apply` → exit 0.
- Patch sha256: `6f342703f4e5568f2cdc3079a247704c596c2769a4b0d621f3ab34f3a4798179`
  (2579 bytes).
- Applied `PROVINCE.md` sha256: `83f1ea44bddac1cc05aedb72f5d2c875f71429b669ee3e4010a00db058d9ff43`
  (22285 bytes; base is 22049).
- No other round-79/round-80 patch in `.ufo/waves/round-{79,80}/build/*.patch`
  touches `PROVINCE.md` (`grep -l PROVINCE.md` hits only prose mentions inside
  `Kb79E01Registry.patch`/`Kb79E06ControlsB.WB5.patch`, both `diff --git a/SKILL.md`
  single-file patches), so merge order against the other C1/C2 patches is free.

## Limits

- The counter arrived late and **wrong**: absent at 20:14 and through a 180 s
  bounded wait (exit 2 on `ls`), then published at 20:19 — byte-identical to the r79
  draft (`sha256 74e067cc…`), `ENTRY` still the round-79 path, r79 output wording.
  A verbatim run of those bytes prints `province surfaces named 0 of 6` and
  `0 ## Core bullet(s) name the entry` for the correct round-80 tree (Verification A,
  run 1); with only `ENTRY` corrected and `SELF_SHA` refilled as the file's own
  freeze step documents, the same code prints `province surfaces named 6 of 6` with
  no (h) finding (run 2). The bullet is verified against the plan's frozen predicate
  (round-80 path), not against the published bytes as they stand; the publication
  defect is reported to Kb80E07C2Counter and the C1 battery seat, and the L1 must
  not freeze `build/check_allowed_tools.py` without the `ENTRY` correction and the
  plan's `documented N of 6` / `generator world: M of 6` wording.
- No claim is made here about conjuncts (a)–(g); they belong to the entry and
  SKILL.md seats. This seat wrote no lane file: `PROVINCE.md` is returned as a
  patch for the L1 to integrate.
- Scratch clone and all receipts lived under
  `/fast/scratch/hyaku/kotoba-r80/Kb80S10Province/` and were removed before yield.
