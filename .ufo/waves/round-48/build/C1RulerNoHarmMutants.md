# C1 ruler no-harm mutation probes — findings

Seat `KotobaR48.C1RulerNoHarmMutants`, round-48 build wave, hyaku session 2026-10-22.
Private clone: `/fast/scratch/hyaku/kotoba-r48-a2/seats/C1RulerNoHarmMutants/clone` at base
`75f671b109d8eddd0d64c1429bd6379fe577175a` + C1 candidate patch
(`c1-candidate.patch`, consumer sha256 `2d824c0b…`). No lane mutation; lane checkout
untouched by this seat.

## Findings

1. **All four mandated no-harm mutants are caught by `behavioral_mismatches`** (exit 1,
   verdict `failed`, target failures 0) on both the plan-declared candidate and the landed
   lane consumer (`d1ae458`). (a) non-target value shift, (b) status flip, (c) dropped check
   id, (d) added check id all fail the ruler.
2. **The baseline-receipt arm is load-bearing**: mutants (a) and (E) are detected *only* by
   the "baseline … changed" comparisons, not by the same-run/control comparisons. The ruler
   structurally cannot run a non-BASE revision without the committed before receipt
   (`--baseline-receipt` missing → exit 2 "non-BASE revision requires the committed before
   receipt"), so this arm is always present.
3. **Four silent-pass mutants found** (exit 0, verdict `clean`, no mismatches):
   - F: evidence-text drift on the target row (value untouched) — the ruler never compares
     `evidence` strings, only check ids, statuses, values.
   - G: recursive enumeration (`rglob("SKILL.md")`) — the oracle matrix has no nested
     SKILL.md case, so "direct-child only" is not discriminated.
   - I: dropping one scoped-out probe block — the `scoped_out_probes` channel contents are
     not validated against the rows.
   - J: name identity switched to frontmatter `name` — the matrix generates SKILL.md with
     `name == dir name`, so the identity rule cannot be distinguished.
4. Structural inconsistency (results `value` split from `re_derived`) is correctly
   short-circuited as `could-not-evaluate` (exit 2), not a behavioral verdict.

## Evidence

Ruler command (per mutant commit `REV`, consumer sha from `git show`):
`python3 -B .ufo/round-48/tools/config-root-ruler.py --repo . --revision $REV
--consumer-sha256 $CS --oracle .ufo/round-48/oracle/config-root-cases.json --oracle-sha256
1d09a38ce04d6c0ab9a1c4edd7f4255978a0c2b8d44ce037d10fcd37d756b883 --scratch
/fast/scratch/hyaku/kotoba-r48-a2/seats/C1RulerNoHarmMutants/ruler-N --baseline-receipt
.ufo/round-48/verification/before-configured-root.json --baseline-sha256
8bec447aa538446e84b7cb87b902c5f1021c42bd7a01f81ea14313262f7e2312`

### Pristine controls
- Candidate base `07f851d3c4b16641aa24efd0537b62f9674b2165` (consumer 2d824c0b…):
  exit 0, verdict `clean`, 13 settled, tf=0 bm=0.
- Landed lane consumer `d1ae45830235c38320b31032b57a8323cbf90b17` (consumer d67b1b6e…):
  exit 0, verdict `clean`, tf=0 bm=0.

### Mandated mutants (on candidate base)
| mutant | commit | exit | verdict | tf | bm | mismatch kinds |
|---|---|---|---|---|---|---|
| (a) non-target value +1 (`omp.db.rows`) | b5508996… | 1 | failed | 0 | 13 | baseline non-target changed: omp.db.rows ×13 |
| (b) status DERIVED→UNLANDED (`omp.db.rows`) | 33c7a37… | 1 | failed | 0 | 26 | original check/status population changed ×13; baseline population changed ×13 |
| (c) drop id `omp.descriptions.unmodelled` | 34e8a3c… | 1 | failed | 0 | 26 | original check/status population changed ×13; baseline population changed ×13 |
| (d) add id `oc.roots.configured_dirs_count` | 4fd8a02d… | 1 | failed | 0 | 51 | original check/status population changed ×13; baseline population changed ×13; baseline non-target changed ×13; non-target value changed ×12 |

### Same four on the landed lane consumer
| mutant | exit | verdict | tf | bm |
|---|---|---|---|---|
| (a) landed | 1 | failed | 0 | 13 |
| (b) landed | 1 | failed | 0 | 26 |
| (c) landed | 1 | failed | 0 | 26 |
| (d) landed | 1 | failed | 0 | 51 |

### Extra probes
- E (status swap preserving 24 DERIVED/4 SCOPED_OUT, 49bca2e…): exit 1, failed, tf=0,
  bm=13 all "baseline population changed" — caught by baseline arm only.
- F (evidence drift, 32a216e…): **exit 0, clean, silent pass** (finding 3).
- G (recursive enumeration, 6766820…): **exit 0, clean, silent pass** (finding 3).
- H (results value/re_derived split, 342e5c2…): exit 2, `could-not-evaluate`,
  ee=13 "consumer channels: results value/re_derived type or value split".
- I (drop scoped-out probe, d41cd26…): **exit 0, clean, silent pass** (finding 3).
- J (frontmatter name identity, 85a9110…): **exit 0, clean, silent pass** (finding 3).
- L (enumerate every child dir, 8d604df…): exit 1, failed, tf=2
  (non-skill-child-files, skill-named-directory), bm=0 — target-side discrimination works.

### Restoration evidence
Working tree restored to pristine candidate branch `r48/noharm-base`; consumer sha256
`2d824c0b3d4954c9a01868ee7c9b44c72b77bb5054419cf0539f6e4082f1b88a` (matches base candidate),
`git status` clean. Lane checkout untouched by this seat (only lane-side reads).

Receipts: `ruler-0` … `ruler-L`, `ruler-landed*` under the seat scratch dir.
