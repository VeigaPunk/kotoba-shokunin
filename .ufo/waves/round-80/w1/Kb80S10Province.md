# Kb80S10Province — PROVINCE.md `## Core` bullet for C2 conjunct (h)

Round 80 w1 (v2, 64 seats), kotoba lane. Seat role: scribe. Base `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`.
Leaf seat: no subagent dispatch, no lane write, no commit.

## Behavior

Drafted the single `PROVINCE.md` `## Core` bullet that C2's conjunct (h) reads, and
verified it against (i) the published counter's (h) predicate (absent from disk; see
Limits) and (ii) `check_sibling_census.py`, plus every other gate that parses
PROVINCE.md. Nothing in the lane tree was written: the edit is a one-hunk patch and a
draft `.md`.

The bullet (exact line, inserted as the new `PROVINCE.md:34`, after the round-74
sibling-census bullet at base `:33`, directly above `## Frontier`):

```
- Allowed-tools surfaces by client (round 80, depth): where the Open specification, Claude Code, Factory, Microsoft Agent Framework, pi and Mistral Vibe document the `allowed-tools` frontmatter field — the value form each page prints and the grant each states (`pre-approves`, `metadata-only`, `experimental`, `unstated`), each read from a snapshot-pinned located quote, form-level documentation only; the grant-semantics matrix is exploratory, reviewed by the round-80 non-author closure spot-check (S226–S231; the six pages re-opened live 2026-10-27) — `corpus/knowledge/allowed-tools-surfaces-round80.md`, counted by `verifiers/check_allowed_tools.py --rev <rev>`.
```

Style: matches the existing Core bullets' shape (`- <topic> (round N, axis): <what it
holds> — `<entry>`, counted by `<counter> --rev <rev>``), names the six surfaces with
the counter's frozen display strings, and carries the C2 claim split in prose
(form-level measured; grant semantics exploratory with a named reviewer class), so
Core does not overclaim the exploratory rider.

## Gates (exact commands, own exit status, no pipelines)

All runs on a `/fast/scratch/hyaku/kotoba-r80/Kb80S10Province/` clone of the lane at
base; the scratch commit carrying only this bullet is
`aeb7d8cb76d8c0e19d8b027d28ee35adef5423aa`. Receipts:
`.ufo/waves/round-80/build/Kb80S10Province-receipts.txt`.

1. **(h) text-match** — the round-80 `check_allowed_tools.py` was not on disk at any
   poll (see Limits), so the r79 draft's own functions were run with `ENTRY` rebound
   to `corpus/knowledge/allowed-tools-surfaces-round80.md` (importlib load of
   `.ufo/waves/round-79/build/check_allowed_tools.py`; `province_state`):
   - base PROVINCE, r80 ENTRY → `(0, 0)` (no bullet; red before)
   - edited PROVINCE, r80 ENTRY → `(1, 6)` (exactly one naming bullet; six surfaces)
   - edited PROVINCE, draft's literal r79 ENTRY → `(0, 0)` (constants differ —
     expected, not a defect)
   - per-surface read-out on the bullet: spec True / claude True / factory True /
     msaf True / pi True / vibe True (`surfaces_named` = 6).
   **Verbatim runs of the published counter** (it arrived at 20:19; scratch clone
   `db47373c59d6d38a00eab901fb1d428aff432b73` = base + this patch + the published
   entry at `corpus/knowledge/allowed-tools-surfaces-round80.md`):
   - published bytes as they stand → **exit 1**, `province surfaces named 0 of 6`,
     `0 ## Core bullet(s) name the entry`, `entry …round79.md absent` — because
     `sha256 74e067ccad7813d91826ee503c8ee93ba47d3a4a05b12ec67a82791d93f722a6`
     is byte-identical to the r79 draft and its line 190 still reads
     `ENTRY = "corpus/knowledge/allowed-tools-surfaces-round79.md"` (r79 output
     wording too: `backed`, `script-only world`). A counter-publication defect,
     reported to its author and the C1 battery seat.
   - same bytes with only `ENTRY` corrected to the round-80 path and `SELF_SHA`
     refilled by the module's own `_blanked_sha` (the freeze step the file documents;
     scratch variant, unpublished) → **exit 1** (other conjuncts open),
     `opened this round 6 of 6`, **`province surfaces named 6 of 6`**, and NO (h)
     finding. That is the verbatim confirmation of the bullet against the counter's
     own arm; the remaining findings (`used-by` still `corpus/lessons/round-79.md` on
     all six rows; `skill rule line MISSING` / `registry home MISSING` because the
     SKILL.md patch was not applied in my scratch tree) belong to other conjuncts.
2. **`check_sibling_census.py`** (census = `corpus/knowledge/sibling-overlap-census-round74.md`;
   the script has no default positional — without one it exits 2 usage):
   - `--province PROVINCE.md` → exit 0, `rows 20 verified 20`, `province rows 20 matched 20`
   - `--province <edited>` → exit 0, same two lines; `diff` of the outputs: IDENTICAL
   - with `--skill SKILL.md`, both files → exit 0, `rows 20 verified 20`,
     `province rows 20 matched 20`, `skill description names 10 of 10 non-none lanes`,
     `skill description length 1021 of 1024`; outputs IDENTICAL.
   The script reads only `## Adjacent` (ends at the next `## ` heading), so a Core
   insertion is outside its parse by construction and measurably inert.
3. **Other PROVINCE-reading gates** (`grep -ln "PROVINCE.md" verifiers/*.py` → 6
   files; 3 parse content and were run at base rev and scratch rev):
   - `check_province_core.py --repo <clone> --rev` → exit 0 both, `province core rows 2 of 2`;
     output identical except `measured-rev`. Its § Frontier/§ Adjacent byte pins are
     untouched by a Core-only insertion.
   - `check_cn_vendor_surfaces.py --repo <clone> --rev` → exit 0 both,
     `province surfaces named 4 of 4`; identical except `measured-rev`.
   - `check_spec_craft.py --repo <clone> --rev` → exit 1 both, same three base-red
     findings (`corpus/SOURCES.md is not census-conformant … (conjunct (b))`), and
     `province core names the entry: yes` at both revs; identical except `measured-rev`.
4. **Corpus integrity observation** (not a repair seat; harm check only):
   `verify_corpus_integrity.py --repo <patched clone> --no-baseline --json` → exit 1
   with exactly the base drift set (`tracked_files 152`, `unindexed 1`,
   `report_total 109`, `report_dead 1`, `commit_total 46`, `commit_unresolvable 2`;
   `stale_patterns`/`missing_paths`/`commit_nonhash` 0 PASS). PROVINCE.md is not in
   `verifiers/corpus-baseline.json` (`grep -c PROVINCE` = 0), so a Core bullet moves
   no expected observation.
5. **Patch mechanics**: `Kb80S10Province.patch` — one hunk, `PROVINCE.md` only;
   `git -C <base clone> apply --check` exit 0, `git apply` exit 0; result
   `PROVINCE.md` 22285 bytes, sha256 `83f1ea44bddac1cc05aedb72f5d2c875f71429b669ee3e4010a00db058d9ff43`
   (base 22049 bytes). Patch sha256
   `6f342703f4e5568f2cdc3079a247704c596c2769a4b0d621f3ab34f3a4798179` (2579 bytes).
   No other round-79/80 build patch touches `PROVINCE.md` (`grep -l PROVINCE.md
   .ufo/waves/round-{79,80}/build/*.patch` hits only prose inside
   `Kb79E01Registry.patch`/`Kb79E06ControlsB.WB5.patch`, both `a/SKILL.md` patches),
   so merge order against the other C1/C2 patches is free.

## Touched surfaces

Written (lane, inside the round-80 wave dir only):
- `.ufo/waves/round-80/build/Kb80S10Province.md` — draft + verification record
- `.ufo/waves/round-80/build/Kb80S10Province.patch` — `PROVINCE.md` bullet, one hunk
- `.ufo/waves/round-80/build/Kb80S10Province-receipts.txt` — gate outputs and hashes
- `.ufo/waves/round-80/w1/Kb80S10Province.md` — this report

Not touched: `PROVINCE.md` itself, `SKILL.md`, `corpus/`, `verifiers/`, `MANIFEST.json`,
`plans/`, the lane git index, and every path outside the wave dir. Scratch clone (and
its receipts) lived under `/fast/scratch/hyaku/kotoba-r80/Kb80S10Province/` and was
removed before yield. No tool was installed or upgraded (nothing was needed).

## Findings

1. **The r79 draft's `ENTRY` constant is the round-79 path.** A verbatim run of the
   draft against the round-80 tree cannot text-match the round-80 bullet; the (h)
   arm must be measured with `ENTRY` rebound (or with the published round-80 counter,
   whose `ENTRY` is the round-80 path). This is a porting note for whoever re-runs
   the (h) arm from the r79 draft.
2. **`check_sibling_census.py` has no default census positional.** The plan's no-harm
   battery writes the command as `check_sibling_census.py --skill SKILL.md`, which
   exits 2 (usage). The working form names the census explicitly:
   `check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md
   --province PROVINCE.md --skill SKILL.md`. The round-49 census does **not** match the
   current § Adjacent table (2 rows fail on `tameshi` commit and `tsukuroi`
   classification); the round-74 census does (20/20).
3. **The published round-80 counter is the r79 draft, unchanged — a real
   publication defect.** Absent at 20:14 and through a 180 s bounded wait; at 20:19
   `build/check_allowed_tools.py` appeared with
   `sha256 74e067ccad7813d91826ee503c8ee93ba47d3a4a05b12ec67a82791d93f722a6`, i.e.
   byte-identical to `.ufo/waves/round-79/build/check_allowed_tools.py`, `ENTRY` at
   line 190 still `…allowed-tools-surfaces-round79.md`, and the r79 output strings
   (`backed N of 6`, `script-only world: M of 6`) instead of the plan's frozen
   `documented N of 6` / `generator world: M of 6`. Consequences, both measured:
   the published bytes give `province surfaces named 0 of 6` and
   `0 ## Core bullet(s) name the entry` on a correct round-80 tree; with only
   `ENTRY` corrected (and `SELF_SHA` refilled) the same code gives
   `province surfaces named 6 of 6` and no (h) finding. The L1 must not freeze the
   current file; reported to Kb80E07C2Counter and Kb80E10Battery.
4. **`check_spec_craft.py` is red at base** (`corpus/SOURCES.md` census conjunct (b))
   and stays red identically after the edit; my bullet does not touch it. Named for
   the L1's battery so it is not mistaken for a round-80 regression.
5. **Stray empty directory in the lane tree, not mine**: `git status --porcelain`
   at the lane root shows `?? .ufo/wapes` (an empty dir, 4.0K, no files —
   `find .ufo/wapes -maxdepth 3` lists only itself). Looks like a seat's typo'd
   `mkdir -p`. Left in place (outside my write scope); the L1 can `rmdir` it. It is
   untracked and empty, so it moves no gate.

## Out of scope (reported, not done)

- Conjuncts (a)–(g) of C2: the entry file, its 11-cell rows, snapshot pins,
  `SKILL.md` rule line and gate-registry row — other seats; I did not create
  `corpus/knowledge/allowed-tools-surfaces-round80.md` nor run the published counter
  end to end.
- C1 repairs (registry rows, symlink, index/baseline, E04 pointer, external-commit
  grammar class): not mine; no C1 patch is produced by this seat.
- § Adjacent rows: unchanged by design; verified byte-inert via the census gate.

VERDICT: PROVINCE `## Core` bullet drafted and verified — (h) reads `(1, 6)` on the edited text vs `(0, 0)` at base, and the counter's own arm prints `province surfaces named 6 of 6` with no (h) finding once its `ENTRY` is the round-80 path; `check_sibling_census.py` exit 0 with 20/20 rows and 20/20 province rows, identical to base; three other PROVINCE-reading gates unmoved. The published `build/check_allowed_tools.py` is the r79 draft byte-for-byte (sha256 74e067cc…, `ENTRY` still round-79), so it reads (h) 0 on a correct round-80 tree — a counter republication is required before freeze.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80S10Province.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80S10Province.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80S10Province-receipts.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80S10Province.md
