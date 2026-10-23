# FalsifyC2Mutants — C2 mutation probe (round-62 wave 2)

Seat `L1kotoba62.FalsifyC2Mutants`, 2026-10-23. Leaf seat: no subagent dispatch, no
background jobs, no git/jj writes in the lane, no installs (nothing needed; pacman is
paused host-wide and was not touched).

Target: `verifiers/check_routed_repairs_v2.py` at the bytes round 62 names — sha256
`de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7` — and the frozen
counter `verifiers/check_routed_repairs.py` sha256
`95ade9be1ed1930266bce4b98c8c593fff1feba89e2cf25763f0aa83f206cb88` (imported, never edited).

## 0. Measured bytes

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && git rev-parse HEAD                 # seat start
e6da78bbe420722dd18a13182a7c4b64ce02f005
$ sha256sum verifiers/check_routed_repairs_v2.py verifiers/check_routed_repairs.py
de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7  verifiers/check_routed_repairs_v2.py
95ade9be1ed1930266bce4b98c8c593fff1feba89e2cf25763f0aa83f206cb88  verifiers/check_routed_repairs.py
$ git show 3f911504ce76d9ca186f297d6d4a9cd8ed77508a:verifiers/check_routed_repairs_v2.py | sha256sum
de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7  -
$ git show 3f911504ce76d9ca186f297d6d4a9cd8ed77508a:verifiers/check_routed_repairs.py | sha256sum
95ade9be1ed1930266bce4b98c8c593fff1feba89e2cf25763f0aa83f206cb88  -
```

The lane advanced from `e6da78b` to `3f91150` (wave-2 dispatch commit) while this seat ran;
the two verifier blobs are identical at both revisions. **After** the mutation runs the
lane *working tree* copy of `check_routed_repairs_v2.py` changed to an uncommitted draft
(801 lines, sha256 `604ae4fb41779874eb420e8a904cb2ebdd953fa41dfc5f270ece53562b5c414d`,
`git diff --stat` = `1 file changed, 157 insertions(+), 6 deletions(-)` vs `HEAD`). All
verdicts below are for the assigned `de5e3471` bytes; §5 is a clearly-labelled observation
on the uncommitted draft, not a verdict on landed bytes.

Scratch copies (lane read-only):

```
$ git clone --shared --quiet /home/vgpnk/Projects/shokunin/kotoba-shokunin /tmp/r62c2/base
$ cd /tmp/r62c2/base && git cat-file -t f3246d1493b60ea1c0d947a19c39f9e08e92f326
commit
$ git cat-file -t 45a7ecfac9e203297f3146c45d63f5e79367470c
commit
$ git cat-file -t 3e7aed9b61bbfd83e0c800213b6dfc6da6191f85
commit
```

Each mutant is a `cp -a base <name>` with exactly one edit applied to
`<name>/verifiers/check_routed_repairs_v2.py`. Runs are sequential (≤4 processes).

## 1. Detectors — the same text on pristine, mutated and restored bytes

* **D-A** `python3 -B <copy>/verifiers/check_routed_repairs_v2.py --self-test` — the
  committed detector; record final line and exit code.
* **D-B** `/tmp/r62c2/probe.py <copy>` — per-D-tree score table computed *by the copy's
  own* `dishonest_fixture_maps()` + `check_repairs()`, with the frozen counter's score
  cross-checked from the same blob map. Needed because D-A only prints an aggregate
  (`rejected k of 6`); this names which tree flipped.
* **D-C** `/tmp/r62c2/probe2.py <copy>` — five-tree constructed variant (C7–C11) used only
  for the window/cue guard family (§3.3), scored the same way.

## 2. Baseline (pristine copy)

```
$ cd /tmp/r62c2/base && python3 -B verifiers/check_routed_repairs_v2.py --self-test; echo "EXIT=$?"
G-a paired population control: 29 names/committed 29=6; 30 names/committed 29=5; 30 names/committed 30=6; frozen=6/6/5
label-only constants fail controls: constant 6 vs base 0; constant 0 vs H1 6; constant 0 vs H2 6
frozen counter before: D1 6 of 6; D2 6 of 6; D3 6 of 6; D4 6 of 6; D5 6 of 6; D6 6 of 6; H1 4 of 6; H2 tip 6 of 6
...
self-test CLI exits: base rev f3246d1493b60ea1c0d947a19c39f9e08e92f326 exit 1; tip rev 45a7ecfac9e203297f3146c45d63f5e79367470c exit 0; unreadable rev routed-repairs-v2-no-such-revision exit 2
successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6
EXIT=0
```

```
$ python3 -B probe.py /tmp/r62c2/base
D1: successor 5 of 6 REJECTED; frozen 6 of 6; missing=['R-a count correction']
D2: successor 5 of 6 REJECTED; frozen 6 of 6; missing=['R-a count correction']
D3: successor 5 of 6 REJECTED; frozen 6 of 6; missing=['R-c base-measure pointer']
D4: successor 5 of 6 REJECTED; frozen 6 of 6; missing=['R-d census-after body']
D5: successor 5 of 6 REJECTED; frozen 6 of 6; missing=['R-e byte-exact criterion + M91']
D6: successor 5 of 6 REJECTED; frozen 6 of 6; missing=['R-f controls-ancestry receipt']
EXIT=0
```

Baseline is green (exit 0) and every D tree fails exactly one repair. The baseline is
therefore a valid reference: a mutant that flips one row to `6 of 6 ACCEPTED` is killed by
D-A only if D-A's exit turns 1.

**Guard-label caveat.** The plan (`plans/round-62.md:139`) says "G-a is the self-derived
count … the other hardened forms are ExecC2Audit's G-b/G-c/G-d/G-e/G-f, each in its
smallest form (assertion direction, bounded window, census body, exact ids, owned exit)",
while `ExecC2Audit` labels G-c=R-b landed scope, G-d=R-c direction, G-e=R-d census,
G-f=R-e ids, G-g=R-f ancestry. The two schemes do not agree, so the table is keyed by
**code site**; the plan label and the ExecC2Audit label are both given where one exists.

| site (function) | plan label | ExecC2Audit | mutation (smallest disable) | mutant sha256 | D flipped | D-A exit |
|---|---|---|---|---|---|---|
| `r_a_count_correction` derived-count equality | G-a | G-a | drop `committed == derived_count` | `f443a45df8eb` | **D1** | 1 killed |
| `affirmed_count` negation rejection | G-b | G-b | return match unconditionally | `f3332e0674c0` | **D2** | 1 killed |
| `r_b_landed_scope` window-8 | G-c | G-c (window half) | window 8 → whole section | `110e9860eac0` | none | 0 **survived** |
| `r_b_landed_scope` landing cue | G-c | G-c (cue half) | drop `LANDING_CUE_RE` requirement | `fc0ee0a1e1a5` | none | 0 **survived** |
| `r_c_pointer_direction` pair window 2 | G-c (bounded window) | G-d (window half) | window 2 → whole section | `c347feb41a51` | none | 0 **survived** |
| `round_61_section` scope (R-a/R-b/R-c) | G-b/G-c | G-b/G-i | scan whole LOG, not the r61 entry | `19046bc9898c` | none | 0 **survived** |
| `r_d_census_body` body requirement | G-d | G-e | last line `exit=0`, no body | `cac40e7d2d5b` | **D4** | 1 killed |
| `exact_quality_row` + `r_e_exact_ids` token bounds | G-e | G-f | `Q56`/`M91` as substrings | `44487ae35fac` | **D5** | 1 killed |
| `r_f_owned_ancestry` owned exit | G-f | G-g | any `exit 0` line | `ac7b5b671ef9` | **D6** | 1 killed |
| `r_c_pointer_direction` direction sub-checks | *(unnamed)* | G-d (direction half) | guard body → frozen co-occurrence | `5066d79a036a` | **D3** | 1 killed |

Full mutant hashes (`sha256sum <copy>/verifiers/check_routed_repairs_v2.py` after the edit):

```
f443a45df8eb2274319eed745e5f895770bce8dea9be9593c29aca9368f68f4a  MGa
f3332e0674c023b483f72c92e572675bb136e559c84241d1474cd420097af9f6  MGb
c347feb41a511b963cd15af83ef24fcc05e57e689bb08df9c0d1b32716a8a041  MGc   (r_c window)
110e9860eac040e32fdb6f7b02f00efd5d195012b07e618cdad31f6dda31454e  MGc2  (r_b window)
19046bc9898cb24788224afc134c895579714cdfbae13d05dcb285f9f39b71b1  MGc3  (section scope)
fc0ee0a1e1a57ed60c07395ec55119eb83876da4cf82edef9905726cdb0f7045  MGc4  (landing cue)
cac40e7d2d5b9a802ed51fc9559dac9993acaefc25e6f648a0d332782e3c4458  MGd
44487ae35facf61341a286da1279df6ceb9fd618ba120dc3c3426d794865cad5  MGe
ac7b5b671ef974f09b43ed24e5043edb4563860492fe2a608f87548b0ce33cff  MGf
63496dae221c9cd91e2c58eae44fca827e545b69353f8c9e8613bbce57c68957  MGdir   (denial -> False, negative control)
56798a2b98ff1f7e78012c2bc0f66c2800cc6e332ddd6f66469af9ff035a0b3f  MGdir2  (C1 skip removed)
cc3801b470bd8e13453ff1e9f84d8403a257c73c876ca51c106afd5f99eb8640  MGdir3  (denial -> True)
87d0006d97c7b1ff5ad246376a51a26219ccd3cce69950847bdd4ae7c108cb9d  MGdirBoth (both single halves)
5066d79a036a308dc6ad562f5f24c3a464dc3c6eb72eb75b9f3ac37dbb006518  MGdir4  (guard-level)
1bdd8a7115d959fd099472cf9ad1b63dc7e0a883c7e46c1d4ffab6ad47f6330d  Msplit
```

### 3.1 G-a — self-derived count (`r_a_count_correction`, line 176)

Edit: remove `and int(committed.group(1)) == derived_count` from the conjunction.

```
$ python3 -B probe.py /tmp/r62c2/MGa
D1: successor 6 of 6 ACCEPTED; frozen 6 of 6; missing=[]
D2..D6: successor 5 of 6 REJECTED   (identical to baseline rows)
$ python3 -B MGa/verifiers/check_routed_repairs_v2.py --self-test   ; exit 1
self-test: D1: successor scored 6, expected <6
self-test: G-a paired population control did not score 29/pass, 30/stale/fail, 30/declared/pass
self-test: dishonest rejected 5 of 6, expected 6
```

**Killed.** D1 (tree 30 names, line claims `committed 29`) stops being rejected. The
paired-population control is a second, independent detector of this same defect.

### 3.2 G-b — assertion direction (`affirmed_count`, line 168)

Edit: `return None if NEGATION_RE.search(neighborhood) else match` → `return match`.

```
$ python3 -B probe.py /tmp/r62c2/MGb
D2: successor 6 of 6 ACCEPTED; frozen 6 of 6; missing=[]
D1,D3..D6: successor 5 of 6 REJECTED   (unchanged)
$ python3 -B MGb/verifiers/check_routed_repairs_v2.py --self-test   ; exit 1
self-test: D2: successor scored 6, expected <6
self-test: dishonest rejected 5 of 6, expected 6
```

**Killed.** D2 (the negated "were NOT claimed 32") stops being rejected. Isolation holds:
D1 still fails on the derived count.

### 3.3 G-c — bounded window / scope family: SURVIVED at all four sites

Four single-site disables, each run through D-A and D-B:

```
$ python3 -B probe.py /tmp/r62c2/MGc     # r_c pair window 2 -> section
D1..D6: successor 5 of 6 REJECTED ... (all six rows identical to baseline)
$ python3 -B probe.py /tmp/r62c2/MGc2    # r_b window 8 -> section
D1..D6: successor 5 of 6 REJECTED ... (all six rows identical to baseline)
$ python3 -B probe.py /tmp/r62c2/MGc3    # round_61_section -> whole LOG
D1..D6: successor 5 of 6 REJECTED ... (all six rows identical to baseline)
$ python3 -B probe.py /tmp/r62c2/MGc4    # drop LANDING_CUE_RE requirement
D1..D6: successor 5 of 6 REJECTED ... (all six rows identical to baseline)
$ for m in MGc MGc2 MGc3 MGc4; do python3 -B $m/verifiers/check_routed_repairs_v2.py --self-test; echo exit=$?; done
successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6
exit=0
(repeated four times; no `self-test:` failure lines in any run)
```

No committed D tree depends on a window or a section bound. That is a coverage gap, not a
free pass for the guard: four constructed trees that the **frozen** counter scores 6 of 6
and pristine v2 scores 5 of 6 flip to 6 under exactly the matching mutant (D-C):

```
$ python3 -B probe2.py /tmp/r62c2/base
C7 ancient-section R-a: successor 5 of 6 missing=['R-a count correction']; frozen 6 of 6 missing=[]
C8 distant R-b names:   successor 5 of 6 missing=['R-b landed-scope names']; frozen 6 of 6 missing=[]
C9 three-line R-c pair: successor 5 of 6 missing=['R-c base-measure pointer']; frozen 5 of 6 missing=['R-c base-measure pointer']
C10 inverted+split R-c: successor 5 of 6 missing=['R-c base-measure pointer']; frozen 6 of 6 missing=[]
C11 no landed-scope cue: successor 5 of 6 missing=['R-b landed-scope names']; frozen 6 of 6 missing=[]

$ python3 -B probe2.py /tmp/r62c2/MGc3   (section scope removed)
C7 ancient-section R-a: successor 6 of 6 missing=[]; frozen 6 of 6 missing=[]
C8 distant R-b names:   successor 5 of 6 missing=['R-b landed-scope names']; frozen 6 of 6 missing=[]
C9 three-line R-c pair: successor 5 of 6 missing=['R-c base-measure pointer']; frozen 5 of 6 missing=['R-c base-measure pointer']
C10 inverted+split R-c: successor 5 of 6 missing=['R-c base-measure pointer']; frozen 6 of 6 missing=[]
C11 no landed-scope cue: successor 5 of 6 missing=['R-b landed-scope names']; frozen 6 of 6 missing=[]

$ python3 -B probe2.py /tmp/r62c2/MGc2   (r_b window removed)
C7 ancient-section R-a: successor 5 of 6 missing=['R-a count correction']; frozen 6 of 6 missing=[]
C8 distant R-b names:   successor 6 of 6 missing=[]; frozen 6 of 6 missing=[]
C9 three-line R-c pair: successor 5 of 6 missing=['R-c base-measure pointer']; frozen 5 of 6 missing=['R-c base-measure pointer']
C10 inverted+split R-c: successor 5 of 6 missing=['R-c base-measure pointer']; frozen 6 of 6 missing=[]
C11 no landed-scope cue: successor 5 of 6 missing=['R-b landed-scope names']; frozen 6 of 6 missing=[]

$ python3 -B probe2.py /tmp/r62c2/MGc    (r_c pair window removed)
C7 ancient-section R-a: successor 5 of 6 missing=['R-a count correction']; frozen 6 of 6 missing=[]
C8 distant R-b names:   successor 5 of 6 missing=['R-b landed-scope names']; frozen 6 of 6 missing=[]
C9 three-line R-c pair: successor 5 of 6 missing=['R-c base-measure pointer']; frozen 5 of 6 missing=['R-c base-measure pointer']
C10 inverted+split R-c: successor 6 of 6 missing=[]; frozen 6 of 6 missing=[]
C11 no landed-scope cue: successor 5 of 6 missing=['R-b landed-scope names']; frozen 6 of 6 missing=[]

$ python3 -B probe2.py /tmp/r62c2/MGc4   (cue requirement removed)
C7 ancient-section R-a: successor 5 of 6 missing=['R-a count correction']; frozen 6 of 6 missing=[]
C8 distant R-b names:   successor 5 of 6 missing=['R-b landed-scope names']; frozen 6 of 6 missing=[]
C9 three-line R-c pair: successor 5 of 6 missing=['R-c base-measure pointer']; frozen 5 of 6 missing=['R-c base-measure pointer']
C10 inverted+split R-c: successor 5 of 6 missing=['R-c base-measure pointer']; frozen 6 of 6 missing=[]
C11 no landed-scope cue: successor 6 of 6 missing=[]; frozen 6 of 6 missing=[]
```

The flippers are isolated: C7 flips only under MGc3, C8 only under MGc2, C10 only under MGc,
C11 only under MGc4; every other row above stays `5 of 6`.
C7/C8/C10/C11 are **my constructed trees, not committed fixtures**; they show the guards
carry rejection weight against frozen-6 dishonest classes the committed D universe omits.
C9 (three-line split) is scored 5 of 6 by the frozen counter too, so it cannot be a member
of the D universe as the plan defines it (`frozen 6 of 6` required) — recorded to show the
universe's membership rule, not as a mutant flipper.

**Verdict: G-c SURVIVED (coverage finding).** The committed `--self-test` passes with a
window/scope/cue guard removed and no committed D tree notices.

### 3.4 G-d — census body (`r_d_census_body`, line 239)

Edit: `return len(lines) >= 2 and lines[-1] == "exit=0" and any(...)` → `return bool(lines) and lines[-1] == "exit=0"`.

```
$ python3 -B probe.py /tmp/r62c2/MGd
D4: successor 6 of 6 ACCEPTED; frozen 6 of 6; missing=[]
$ python3 -B MGd/verifiers/check_routed_repairs_v2.py --self-test   ; exit 1
self-test: D4: successor scored 6, expected <6
self-test: dishonest rejected 5 of 6, expected 6
```

**Killed.** D4 (census file containing only `exit=0`).

### 3.5 G-e — exact ids (`exact_quality_row` line 248, `r_e_exact_ids` line 288)

Edits: `^\s*\|\s*Q56\s*\|` → `^\s*\|\s*Q56`; `(?<![A-Za-z0-9])M91(?![A-Za-z0-9])` → `M91`.

```
$ python3 -B probe.py /tmp/r62c2/MGe
D5: successor 6 of 6 ACCEPTED; frozen 6 of 6; missing=[]
$ python3 -B MGe/verifiers/check_routed_repairs_v2.py --self-test   ; exit 1
self-test: D5: successor scored 6, expected <6
self-test: dishonest rejected 5 of 6, expected 6
```

**Killed.** D5 (`Q560`, `M910`).

### 3.6 G-f — owned exit (`r_f_owned_ancestry`, line 290)

Edit: replace the command/operand/adjacent-exit loop with
`return any(EXIT_ZERO_RE.fullmatch(line) for line in lines)`.

```
$ python3 -B probe.py /tmp/r62c2/MGf
D6: successor 6 of 6 ACCEPTED; frozen 6 of 6; missing=[]
$ python3 -B MGf/verifiers/check_routed_repairs_v2.py --self-test   ; exit 1
self-test: D6: successor scored 6, expected <6
self-test: dishonest rejected 5 of 6, expected 6
```

**Killed.** D6 (the `exit 0` belongs to `git rev-parse HEAD`, operands are not hashes).

### 3.7 Unnamed seventh site — R-c direction: D3's only owner

There is a hardening site the plan's G-a…G-f list does not name: `r_c_pointer_direction`
(line 231) beyond its window — `freeze_pointer_asserted` (no C1 or negation between the
base mention and the freeze pointer) plus `c1_pointer_denied`. D3 is the tree that only this
site rejects. Guard-level disable (body → frozen co-occurrence):

```
$ python3 -B probe.py /tmp/r62c2/MGdir4
D3: successor 6 of 6 ACCEPTED; frozen 6 of 6; missing=[]
$ python3 -B MGdir4/verifiers/check_routed_repairs_v2.py --self-test   ; exit 1
self-test: D3: successor scored 6, expected <6
self-test: dishonest rejected 5 of 6, expected 6
self-test: H1: successor scored 5, expected 6
self-test: honest passed 1 of 2, expected 2
```

Two **single sub-check** disables do not flip D3, because D3 is rejected twice over: the
inverted sentence carries `C1-measure.txt` *and* the word `not` between the base mention and
the freeze pointer, and it never denies C1.

```
$ python3 -B probe.py /tmp/r62c2/MGdir2   # remove the C1-between skip
D3: successor 5 of 6 REJECTED; ...        (all rows unchanged)
$ python3 -B MGdir2/verifiers/check_routed_repairs_v2.py --self-test ; exit 0 (no failure lines)
$ python3 -B probe.py /tmp/r62c2/MGdir3   # force c1_pointer_denied() -> True
D3: successor 5 of 6 REJECTED; ...        (all rows unchanged)
$ python3 -B MGdir3/verifiers/check_routed_repairs_v2.py --self-test ; exit 0 (no failure lines)
```

A wrong-direction mutant that forces `c1_pointer_denied()` → `False` (sha `63496dae…`) does
not flip D3 either; it breaks the honest arms instead (exit 1; `H1: successor scored 5`,
`H2 tip CLI: exit 1, score 5`, `honest passed 0 of 2`) — a negative control showing the
denial sub-check is load-bearing for honest trees, not a guard disable.

**Verdict:** D3 is killed only by a guard outside the plan's six labels; D3 is
over-determined by two redundant sub-checks, so no single-site sub-mutation isolates it.

## 4. Split-evaluator hollow — the public CLI wired to the frozen counter

Edit in `main()` (line 793): `score, why = check_repairs(blobs, tree_names, census_regular)`
→ `score, why = frozen.check_repairs(blobs)`. Mutant sha256
`1bdd8a7115d959fd099472cf9ad1b63dc7e0a883c7e46c1d4ffab6ad47f6330d`.

```
$ python3 -B Msplit/verifiers/check_routed_repairs_v2.py --self-test; echo "EXIT=$?"
G-a paired population control: 29 names/committed 29=6; 30 names/committed 29=5; 30 names/committed 30=6; frozen=6/6/5
label-only constants fail controls: constant 6 vs base 0; constant 0 vs H1 6; constant 0 vs H2 6
frozen counter before: D1 6 of 6; ...; H2 tip 6 of 6
self-test base CLI output:
... routed repairs verified 0 of 6
self-test tip CLI output:
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after file: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
self-test CLI exits: base rev f3246d14... exit 1; tip rev 45a7ecfa... exit 0; unreadable rev ... exit 2
successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6
EXIT=0
```

**The tip arm still prints `6 of 6`, the whole self-test still exits 0, and the frozen
predicate line is unchanged.** The only difference in the entire self-test output is the
CLI's R-d label — `census-after body` (hardened) vs `census-after file` (frozen):

```
$ diff -u base.restored.out Msplit.selftest.out
@@ -5,7 +5,7 @@   (base CLI block)
-R-d census-after body: missing
+R-d census-after file: missing
@@ -13,7 +13,7 @@  (tip CLI block)
-R-d census-after body: ok
+R-d census-after file: ok
```

Direct CLI, same mutant:

```
$ python3 -B Msplit/verifiers/check_routed_repairs_v2.py --rev f3246d14...     ; exit 1   "routed repairs verified 0 of 6"
$ python3 -B Msplit/verifiers/check_routed_repairs_v2.py --rev 45a7ecfa...     ; exit 0   "routed repairs verified 6 of 6"
$ python3 -B Msplit/verifiers/check_routed_repairs_v2.py --rev 3e7aed9b...     ; exit 0   "routed repairs verified 6 of 6"
$ python3 -B Msplit/verifiers/check_routed_repairs_v2.py                      ; exit 0   "routed repairs verified 6 of 6"  (clone master = e6da78b)
```

Why it is blind: the D/H1/population arms call the module-level `check_repairs` directly and
never through `main`; the two CLI arms are base (frozen and hardened both score 0) and tip
(frozen and hardened both score 6 — and the self-test *asserts* `frozen.check_repairs(tip_blobs) == 6`
at lines 519/527, i.e. it requires the two evaluators to agree there). Neither the CLI's
`why` text nor its labels are compared to expected text anywhere. The "label-only constants
fail controls" line is literal-constant vs measured-value comparisons; it detects a constant
6 at base and a constant 0 at H1/H2, but a frozen evaluator agrees at base and tip and passes.

**Verdict: SURVIVED — split-evaluator hollow confirmed for the `de5e3471` bytes.** A public
CLI that no longer uses the hardened evaluator still prints `base 0 of 6; tip 6 of 6`, still
prints the frozen predicate line, and still exits 0.

## 5. Observation on the uncommitted working-tree draft (not a verdict)

While this seat ran, the lane's working-tree v2 changed (uncommitted) to sha256
`604ae4fb41779874eb420e8a904cb2ebdd953fa41dfc5f270ece53562b5c414d`, `+157/−6` vs `HEAD`
(`de5e3471`, which is still the committed blob at `3f91150`). Snapshot at
`2026-10-23T21:39:33Z`; the draft may have been mid-edit, so this is an observation only.

```
$ cp verifiers/check_routed_repairs_v2.py /tmp/r62c2/wt-v2-604ae4fb.py
$ sha256sum /tmp/r62c2/wt-v2-604ae4fb.py
604ae4fb41779874eb420e8a904cb2ebdd953fa41dfc5f270ece53562b5c414d
$ (pristine draft snapshot) python3 -B Mdraft/verifiers/check_routed_repairs_v2.py --self-test ; exit 0
successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6
$ (same snapshot + the §4 split edit) python3 -B Mdraft/verifiers/check_routed_repairs_v2.py --self-test ; exit 1
self-test: CLI dependency arm: a zero-score scorer must make the tip CLI exit 1, score 0 (observed exit 0, score 6)
self-test: CLI dependency arm: a six-score scorer must make the base CLI exit 0, score 6 (observed exit 1, score 0)
```

The draft adds a CLI-dependency arm (stub the module-level `check_repairs` and require
`cli_measurement` to follow it) which rejects the split mutant. Its final printed line under
the mutant is still `... base 0 of 6; tip 6 of 6` — the line alone is not the detector; the
exit code is. I ran the split probe on the snapshot only; I make no verdict on the draft,
which was uncommitted and possibly changing while this seat ran.

## 6. Restoration

```
$ for m in <all copies>; do cp -f base/verifiers/check_routed_repairs_v2.py $m/verifiers/check_routed_repairs_v2.py; done
$ for m in base MGa MGb MGc MGc2 MGc3 MGc4 MGd MGe MGf MGdir MGdir2 MGdir3 MGdirBoth MGdir4 Msplit; do
    printf "%s %s\n" "$(sha256sum $m/verifiers/check_routed_repairs_v2.py | cut -d' ' -f1)" "$m"; done
de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7 base
de5e3471... MGa / MGb / MGc / MGc2 / MGc3 / MGc4 / MGd / MGe / MGf / MGdir / MGdir2 / MGdir3 / MGdirBoth / MGdir4 / Msplit   (16/16 identical)
$ for m in <all copies>; do python3 -B $m/verifiers/check_routed_repairs_v2.py --self-test >/dev/null 2>&1; printf "%s exit=%s\n" "$m" "$?"; done
base exit=0 ... Msplit exit=0        (16/16 exit 0; final line in every case:
                                     "successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6")
$ python3 -B probe.py /tmp/r62c2/Msplit      (restored copy)
D1..D6: successor 5 of 6 REJECTED ... (identical to pristine baseline)
$ cp -f wt-v2-604ae4fb.py Mdraft/verifiers/check_routed_repairs_v2.py && sha256sum Mdraft/verifiers/check_routed_repairs_v2.py
604ae4fb41779874eb420e8a904cb2ebdd953fa41dfc5f270ece53562b5c414d  Mdraft/verifiers/check_routed_repairs_v2.py
   (the §5 snapshot copy restored to its source bytes; this copy is not part of the assigned target)
```

Lane untouched by this seat:

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && sha256sum verifiers/check_routed_repairs_v2.py verifiers/check_routed_repairs.py
604ae4fb41779874eb420e8a904cb2ebdd953fa41dfc5f270ece53562b5c414d  verifiers/check_routed_repairs_v2.py   (uncommitted draft, §5; HEAD blob = de5e3471, seat-start tree = de5e3471)
95ade9be1ed1930266bce4b98c8c593fff1feba89e2cf25763f0aa83f206cb88  verifiers/check_routed_repairs.py     (unchanged; never edited)
$ git status --porcelain -- verifiers/
 M verifiers/check_routed_repairs_v2.py                (not this seat's write: §5 draft appeared after the mutation runs)
```

## 7. Verdicts

| probe | expected detector | actual | verdict |
|---|---|---|---|
| G-a derived count removed | D1 rejected / D-A exit 1 | D1 accepted 6/6; exit 1; D1+population-control failures | killed |
| G-b negation removed | D2 rejected | D2 accepted 6/6; exit 1 | killed |
| G-c window / scope / cue (4 sites) | some D rejected | no D row changes; exit 0 at all four; constructed C7/C8/C10/C11 flip only under their own site | **survived (coverage)** |
| G-d census body removed | D4 rejected | D4 accepted 6/6; exit 1 | killed |
| G-e exact ids loosened | D5 rejected | D5 accepted 6/6; exit 1 | killed |
| G-f owned exit removed | D6 rejected | D6 accepted 6/6; exit 1 | killed |
| unnamed R-c direction guard disabled | D3 rejected | D3 accepted 6/6; exit 1 (single sub-check disables: survived, D3 still rejected — redundant) | killed (guard-level) |
| public CLI → frozen `check_repairs` | self-test detects the swap | tip arm prints 6 of 6; exit 0; only the R-d label differs | **survived (hollow)** |

Findings for the L1 (not contract changes):

1. The committed D universe covers one hardening mechanism each for R-a count, R-a
   assertion, R-d body, R-e ids, R-f ancestry, and the R-c direction guard — but **no D tree
   exercises any window/scope/cue bound** (four independent disables survive the self-test).
   Constructed frozen-6 trees (C7 ancient-section markers, C8 distant R-b names, C10
   inverted+split R-c, C11 no landing cue) are rejected by pristine v2 and accepted when the
   matching bound is removed; they are the missing D-classes.
2. `--self-test` cannot tell a public CLI wired to the frozen counter from the hardened one:
   the D/H1 arms bypass `main`, and the two CLI arms are the two points where the evaluators
   agree by construction (0 at base, 6 at tip, with the tip frozen score separately asserted).
   The frozen predicate line and exit 0 are therefore insufficient evidence for the CLI path.
3. D3's rejection is over-determined inside R-c (C1-between *and* negation-between *and* the
   C1-denial requirement); it cannot attribute to one named guard, and the plan's G-a…G-f
   list does not name the direction guard at all.

## 8. Bounds

* Verdicts are for the bytes sha256 `de5e3471…` (blob at `e6da78b` and `3f91150`). They do
  not apply to the uncommitted draft `604ae4fb…`; §5 is a snapshot observation only.
* Not attacked here (other wave-2 seats): `check_erratum_absorption.py`,
  `check_scoped_rules_v31.py`, the receipt numbers themselves, the registry/rows.
* `TIP_REV` in the instrument is the plan-freeze commit `45a7ecfa`, not the data revision
  `3e7aed9b`; I measured the CLI at base, `45a7ecfa`, `3e7aed9b` and the clone's `master`
  (`e6da78b`) separately.
* No installs or updates were made (nothing needed). No git/jj write, no `.ufo/state`, no
  lane product/verifier/corpus/fleet/MANIFEST edit; the only lane write is this report.
