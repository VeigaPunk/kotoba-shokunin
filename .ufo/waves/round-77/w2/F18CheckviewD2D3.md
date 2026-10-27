# F18CheckviewD2D3 — round 77 w2 falsification: r74 D2/D3 hygiene changes and prior art

Seat: reviewer (leaf), kotoba round 77 wave 2. Lane tip attacked: `6523aced1ee0ebe07dca996213bdc645a6acbd1e`
(r77 freeze). Scratch clones (since removed): `/fast/scratch/hyaku/kotoba-r77/F18CheckviewD2D3/{kotoba-shokunin,cloneA,cloneB}`,
all `git clone --shared`, `user.name scratch-r77`, `user.email scratch@example.invalid`, and
`git rev-parse --show-toplevel` asserted equal to the clone before every scratch commit. No lane file
was written; no lane git/jj state touched (read-only `log`/`show`/`cat-file`/`merge-base`/`diff`/`status`
only). No tools installed (none needed); pacman not run. The `lsp` device is not present in this seat's
tool inventory (checked before falling back to byte/git-level checks); every claim below is grounded in
named committed bytes or pasted command output. The seat-shape text names the report
`F18ReviewD2/D3.md`; the dispatch Report line names `F18CheckviewD2D3.md` (this file, matching the seat
id) — that is the canonical deliverable.

## 0. Scope fact first: D2/D3 are NOT landed at the attacked tip

- `grep -c d5aebcf LOG.md` → `0`, grep exit 1 (defect D2 still present at the tip).
- `grep -c 'round-74\|Round 74' corpus/knowledge/sibling-overlap-census-round49.md` → `0`, grep exit 1
  (defect D3 still present at the tip).
- `git status --porcelain` shows **zero modified tracked files** (`MODCOUNT=0`); all round-77 wave
  content is untracked. `git show --stat 6523ace` = plan + 4 receipt files only. `git diff --stat
  2f67554 6523ace -- LOG.md` is empty.
- The hygiene deliverable exists solely as the untracked draft
  `.ufo/waves/round-77/build/E09D2D3Hygiene.patch` (sha256 verified below) plus r76 prior art under
  `.ufo/waves/round-76/build/B10RepairD2D3.*`. Likewise **no claim data is committed** (no
  `corpus/knowledge/description-craft-round76.md`, no SKILL.md row, no `corpus/lessons/round-77.md`,
  no R1–R4 repairs, no index/baseline repair): both frozen counters are red at the tip, as § 2 shows.

Per the wave mandate this is reported as the landing blocker, not papered over: **there are no landed
D2/D3 bytes to falsify — the attack below targets the draft bytes and the prior art.** This matches the
plan's landing order (freeze → controls → data), so it is a state fact, not an accusation.

## 1. What the draft and the prior art claim (re-derived, not trusted)

- r74 closure (`corpus/lessons/round-74-verifier-spotcheck.md`): § 1 D2 (:38-40) — `d5aebcf` sits
  between `d919179` and `2c81137` on master, absent from the report's Landed table and from `LOG.md`;
  § 5 item 2 (:137) — list it in the round-74 record as a **LOG appended correction** (non-landing
  commit); § 5 item 3 (:138) — append a forward pointer in the round-49 census entry to its round-74
  re-pin. All three quotes re-read at the tip: verbatim present.
- Draft under test: `E09D2D3Hygiene.patch` (E09, w1) = LOG.md +4 lines (`## Round 74 correction
  (append-only, routed D2)`) + census-round49 +15 lines (`## Round 74 forward pointer (append-only,
  routed D3)`), chosen as "FormB" over the r76 FormA insertion.
- Prior art: `.ufo/waves/round-76/build/B10RepairD2D3.formA.patch` (mid-file insertion after
  `LOG.md:2803`), `…formB.patch` (tail correction, drafted against the r76 base), plus
  `R04RevHygiene.verdict.md` (w1 reviewer: reject FormA, formB stale at r77 freeze).

## 2. Frozen counters — exact commands, output, exit, revision

Counter bytes verified against the plan pins at the tip:
`sha256sum verifiers/check_desc_craft.py verifiers/check_r75_routed_repairs.py` →
`cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e` (C1, = pin) and
`989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63` (C2, = pin). **Counters unedited.**

Attacked item for both: the r77 base-red claim and the no-harm of the D2/D3 draft on the frozen
counters. `$C` = my scratch clone; `$R` = `6523aced1ee0ebe07dca996213bdc645a6acbd1e` (base);
`$A` = `cc9eb63e4ce2309cb6b085805f777400ff8e0bae` (scratch commit with the draft applied).

| # | command (run in `$C`) | output (gate's own exit captured as `cmd > out 2>&1; echo "exit=$?" >> out`) |
|---|---|---|
| 1 | `python3 -B verifiers/check_desc_craft.py --repo $C --rev $R --work $S/work` | `description craft backed 0 of 6` … `(f) corpus/knowledge/description-craft-round76.md is not committed at the measured revision`, **exit=1** |
| 2 | `python3 -B verifiers/check_r75_routed_repairs.py --repo $C --rev $R --work $S/work` | `r75 routed repairs closed 0 of 4` (R1–R4 each fail), **exit=1** |
| 3 | same as 1 at `--rev $A` | `description craft backed 0 of 6`, **exit=1** (only `measured-rev:` differs) |
| 4 | same as 2 at `--rev $A` | `r75 routed repairs closed 0 of 4`, **exit=1** |

Verdict: the frozen predicate's base-red half holds under my own re-run (matches the plan's base
receipts), and the D2/D3 draft does not move either counter — correct, since the plan discloses this
work as outside both counters' scope.

## 3. Draft falsification — every measured property held

`sha256sum .ufo/waves/round-77/build/E09D2D3Hygiene.patch` →
`e366ac06f22d2963e7962cadd563d68127f28457f251ebfc2b429185aaf63410` = E09's claimed digest.

Facts asserted by the draft's D2 line, each re-verified at the tip:

- `git cat-file -t d5aebcf` → `commit`; `git log -1 --format='%H|%an|%ad|%s' --date=iso` →
  `d5aebcf51c394435e768461001a2d0cc8f67fe3a|kotoba-shokunin|2026-10-25 23:16:44 -0300|hyaku run 7
  interrupted: in-flight snapshot committed by the orchestrator (not a landing); lane L1 resumes from
  here` — subject/author/date in the draft are byte-accurate; `git show --name-only --format='' d5aebcf
  | grep -c .` → `394` files.
- parent `git log -1 --format='%P' d5aebcf` → `d919179c…`; `git merge-base --is-ancestor d919179
  d5aebcf` → exit 0; `git merge-base --is-ancestor d5aebcf 2c81137` → exit 0 ("sits between" holds).
- "The Round 74 record above lists `d919179` and `2c81137` and not this commit": `LOG.md:2803` names
  both, and `grep -c d5aebcf LOG.md` → 0. True at the tip.
- D3 pointer claims: cited ranges `:43-64` / `:246-295` / `:416-458` match the round-74 entry's own
  citations (`sibling-overlap-census-round74.md:8-9`) and the actual headings (`:43` Classification
  rule, `:246` Round 50 precedence, `:416` Round 51 status, next heading at `:459`); counts "10
  adjacent, 10 none, 0 contested (round 49: 9 adjacent, 11 none)" and tsukuroi `none` → `adjacent`
  match the round-74 entry's § body; `README.md:146` and `PROVINCE.md:33,52` indeed already carry the
  round-74 pointer the r49 entry lacked.

Gates at base vs after (all exits captured gate-own, no pipelines):

| check | base `$R` | after `$A` |
|---|---|---|
| `git apply --check E09D2D3Hygiene.patch` | exit 0 (applies cleanly at the freeze tip) | — |
| byte-prefix: `cmp -n <basesize> base-LOG LOG.md` | — | exit 0 (**LOG append-only from the r77 base holds**); same for census-round49 (exit 0) |
| `check_r63_routed_repairs.py --root $C --rev <rev>` | (baseline accounting) | `PASS append-only prefix=True grew_by=256`, `r62 routed defects closed 5 of 5`, exit 0 |
| `check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` | `rows 20 verified 20`, `province rows 20 matched 4`, 16 FAIL lines, exit 1 | `rows 20 verified 20`, `matched 4`, FAIL set byte-identical (`diff` of sorted FAIL lines: empty), exit 1 |
| `check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md --province PROVINCE.md` | `rows 20 verified 20`, `province rows 20 matched 20`, exit 0 | unchanged (D3 append is in the other file) |
| `check_sibling_reread.py --rev <rev>` | `sibling rows re-pinned, re-located and re-diffed at the frozen fleet heads 20 of 20`, exit 0 | 20 of 20, exit 0 |
| `check_gate_registry.py --rev <rev>` | `gate registry rows conformant 60 of 62 lane verifiers; phantom 0`, exit 1 | identical (pre-existing red, unchanged) |
| `verify_skill_checklist.py --json --repo $C` | pass 10 / fail 1, FAIL `LOG.md:2818` (`.ufo/reports/round-76/kotoba.md` does not resolve lane-relatively), exit 1 | identical: pass 10 / fail 1, `LOG.md:2818` |
| `wc -l SKILL.md` | 590 (≤600 budget per plan) | — |

No gate's verdict moved. The two red gates (registry 60/62, checklist citation) are red at the base —
E09 surfaced them as F1/F2 and my re-run confirms both independently; see Findings.

## 4. Mutation tests (gates around D2/D3)

- **Stale prior art (formB):** in a fresh clone at `$R`, `git apply --check
  B10RepairD2D3.formB.patch` → exit 1, `error: patch failed: LOG.md:2808` — the r76 FormB draft does
  not apply at the r77 freeze; R04's "rebase before integration" is confirmed. The E09 draft is the
  rebased form and applies (exit 0, § 3).
- **FormA insertion (the rejected alternative):** formA `--check` exit 0 at `$R`; applied and
  committed (scratch `fdf6d000c18490a712fbdc897e6424c55984c95f`): LOG first difference vs base at
  char 560525 (= byte 560524, as E09 measured), growth 740 bytes, `## Round 75` heading shifts
  `:2805` → `:2807` — **prefix-from-base broken** — yet `check_r63_routed_repairs.py --rev` still
  prints `PASS append-only prefix=True grew_by=254`, `5 of 5`, exit 0. The append-only counter is
  blind to mid-file insertions after its r62 baseline (see Finding F-B).
- **Apply-order hazard (replicated):** appending a dummy `## Round 77` tail section first, then
  `git apply --check E09D2D3Hygiene.patch` → exit 1, `error: patch failed: LOG.md:2816` (E09's exact
  number); `git apply --3way` → exit 1, `error: LOG.md: does not match index` **while applying the
  census hunk cleanly** — i.e. `--3way` can leave a half-applied hybrid. Integration must apply the
  patch before the round-77 LOG entry, or hand-append the section bytes; never `--3way`.
- **Nothing counts D2:** `grep -rn 'd5aebcf' verifiers/` and `grep -rn 'Round 74 correction'
  verifiers/` → no hits; no verifier parses the new sections. Correct per plan ("None of these is
  claimed as an axis move"), and consistent with my § 2 result that the frozen counters ignore the
  hygiene — but it also means the append-only/prefix property of the landing has **no machine gate**
  (Finding F-B).

## 5. Findings

- **BLOCKER (wave state, not a draft defect):** neither the D2/D3 hygiene nor any r77 claim data is
  committed at `6523ace`. All "landed" language for round 77 must wait for the L1 integration commit;
  w2 seats can only falsify drafts. (Stated in § 0 with evidence; this is my report's headline.)
- **F-A (draft, minor, no repair needed beyond landing):** the D2 line's trail says "landed in round
  77 as this appended correction" — prospective while it is still a draft. It becomes true exactly at
  integration; no text change needed, but the integrator should not cite this patch as landed until
  the landing commit exists.
- **F-B (calibration, pre-existing, out of my write scope):** the only byte-shape guard on `LOG.md`
  (`check_r63_routed_repairs.py` conjunct 4) baselines at the r62 tip, so it passes FormA's
  mid-file insertion while prefix-from-the-current-base is broken (§ 4). FormB's correctness currently
  rests on choice and review, not on a gate. Minimal hardening (suggestion only, harms no axis): a
  base-relative "LOG tail is a byte-prefix at every tip" floor, or a one-line landing note in the
  round-77 LOG entry recording the append-only discipline. Not required for C1/C2.
- **F-C (pre-existing, confirmed):** `check_gate_registry.py` = 60 of 62 at the tip — the two frozen
  counters have no registry rows; the plan's own battery includes this gate, so it stays red at the
  data tip unless rows are added. **F-D (pre-existing, confirmed):** checklist fail at
  `LOG.md:2818` — `.ufo/reports/round-76/kotoba.md` exists only in the fleet repo, not lane-relative.
  Both were surfaced by E09 (F1/F2); they block a clean battery, not the D2/D3 content.
- **F-E (operational):** apply-order coupling of the patch to the LOG tail (§ 4) — integration owner
  must sequence it before the round-77 LOG entry.

## 6. Residual risk and verification gaps

- I did not re-open S213 live or audit C1's six conjunct interiors, C2's R1–R4 interiors, the entry
  text, lessons, or the full battery — those are the assigned seats (S213 re-openers, C1/C2 reviewers,
  mutation-testers, E10/E12). My C1/C2 runs establish base-red and hygiene-no-harm only.
- My scratch clones were removed after the evidence was pasted here; the receipt-grade transcripts
  therefore live in this file, not in `receipts/` (my item names only this report as deliverable).
- FormA/FormB figures beyond my own runs (E09's 560524 byte offset, R04's 740-byte growth) matched my
  measurements exactly; no figure in either w1 report failed re-measurement.

VERDICT: D2/D3 exist only as an unlanded draft at tip 6523ace (headline blocker, no claim data committed); the E09D2D3Hygiene.patch draft itself survives falsification — digest, facts, clean apply, LOG/census byte-prefix, r63 5/5, identical census FAIL set, frozen counters still 0 of 6 / 0 of 4 — while r76 FormA is confirmed broken and FormB stale, and the r63 counter is confirmed blind to mid-file insertions.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w2/F18CheckviewD2D3.md
