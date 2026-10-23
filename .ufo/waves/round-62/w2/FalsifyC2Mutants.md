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

The lane advanced from `e6da78b` to `f60590a` while this seat ran: `3f91150` (wave-2
dispatch; verifier blobs still `de5e3471`/`95ade9be`) → `e424f2a` (wave-2 falsification;
commits the hardened v2 `604ae4fb`, `+157/−6`) → `91fecae`/`f60590a` (late seat writes). At
HEAD `f60590a`, measured:

```
$ git show HEAD:verifiers/check_routed_repairs_v2.py | sha256sum
604ae4fb41779874eb420e8a904cb2ebdd953fa41dfc5f270ece53562b5c414d  -
$ git show HEAD:verifiers/check_routed_repairs.py | sha256sum
95ade9be1ed1930266bce4b98c8c593fff1feba89e2cf25763f0aa83f206cb88  -
```

§3/§4 give the verdicts for the **assigned** `de5e3471` bytes (the sha the plan and the C2
receipt name). §3.8 and §4b re-run the **identical** mutations on the landed `604ae4fb`
bytes (its six guard functions are unchanged — the landed diff adds self-test arms and
their helpers, plus two imports: CLI-dependency, invariance/transcript/lookup, `score_with`
constants); those are the verdicts for the file at tip.

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

### 3.1 G-a — self-derived count (`r_a_count_correction`, line 174)

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

### 3.2 G-b — assertion direction (`affirmed_count`, line 166)

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

### 3.4 G-d — census body (`r_d_census_body`, line 237)

Edit: `return len(lines) >= 2 and lines[-1] == "exit=0" and any(...)` → `return bool(lines) and lines[-1] == "exit=0"`.

```
$ python3 -B probe.py /tmp/r62c2/MGd
D4: successor 6 of 6 ACCEPTED; frozen 6 of 6; missing=[]
$ python3 -B MGd/verifiers/check_routed_repairs_v2.py --self-test   ; exit 1
self-test: D4: successor scored 6, expected <6
self-test: dishonest rejected 5 of 6, expected 6
```

**Killed.** D4 (census file containing only `exit=0`).

### 3.5 G-e — exact ids (`exact_quality_row` line 246, `r_e_exact_ids` line 272)

Edits: `^\s*\|\s*Q56\s*\|` → `^\s*\|\s*Q56`; `(?<![A-Za-z0-9])M91(?![A-Za-z0-9])` → `M91`.

```
$ python3 -B probe.py /tmp/r62c2/MGe
D5: successor 6 of 6 ACCEPTED; frozen 6 of 6; missing=[]
$ python3 -B MGe/verifiers/check_routed_repairs_v2.py --self-test   ; exit 1
self-test: D5: successor scored 6, expected <6
self-test: dishonest rejected 5 of 6, expected 6
```

**Killed.** D5 (`Q560`, `M910`).

### 3.6 G-f — owned exit (`r_f_owned_ancestry`, line 286)

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
(line 229) beyond its window — `freeze_pointer_asserted` (no C1 or negation between the
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

### 3.8 Re-run on the landed successor `604ae4fb`

The six guard functions are unchanged between `de5e3471` and `604ae4fb` (the landed diff
adds self-test arms and their helpers, plus two imports; no guard-function change). The
identical disables were re-applied to copies of the landed bytes and run through the same
detectors:

```
$ python3 -B nbase/verifiers/check_routed_repairs_v2.py --self-test
CLI scorer-dependency: zero-scorer tip exit=1 score=0; six-scorer base exit=0 score=6
invariance controls: real passes; call-order transcript rejected=True; fingerprint lookup rejected=True (8 memorized inputs)
successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6
exit=0
```

| site | mutant sha256 | D flipped | self-test exit |
|---|---|---|---|
| G-a derived count | `4a10477fc02c` | D1 → 6 of 6 accepted | 1 |
| G-b negation | `30015cf1bc53` | D2 → 6 of 6 accepted | 1 |
| G-c window/scope/cue, 4 sites | `06374e646fed` / `799d7d0bd1d4` / `b356ded1d1e6` / `db99b134b423` | none | 0 |
| G-d census body | `c6ae622f98eb` | D4 → 6 of 6 accepted | 1 |
| G-e exact ids | `8346fa7a9709` | D5 → 6 of 6 accepted | 1 |
| G-f owned exit | `87cfe5f27048` | D6 → 6 of 6 accepted | 1 |
| R-c direction guard (unnamed) | `5a6ee91e734c` | D3 → 6 of 6 accepted | 1 (D3 + H1) |
| public CLI → frozen `check_repairs` | `d716b1c15c69` | — | 1 (§4b) |

Full landed-mutant hashes:

```
4a10477fc02c058cf4ea010c69f4f1d2557d64688e1f802a5587140adf7671ba  nGa
30015cf1bc53da01c70353fed0ae8c182b6c0b6101980ed40713561ca5c2881a  nGb
06374e646fedda66765f423bc2d9e05df1d203a660e7b5c72479bbc99ce46109  nGc
799d7d0bd1d48333d88c396abf9448cf120c3f7baa4821353820b74b98152fbe  nGc2
b356ded1d1e611c285a4c44dd325803b303a9e64f0979259de210e4099810ea4  nGc3
db99b134b4239a0fe7333dca9f8f5cb3120672d69ae6c285b2bd182d72dcd76e  nGc4
c6ae622f98eb69137affa4d7ebecb0c7736838964e1ab481de2899c49fc6a029  nGd
8346fa7a9709f1ef5063a8edc057a9679330378919aa94439beae688bbf141b8  nGe
87cfe5f27048016965661369674073833dc310d65f121b91c441e8b962e01402  nGf
5a6ee91e734c2b5ccfefa81064e3f27048eaae69d56a6d7ba0a8832e887b3389  nGdir4
d716b1c15c6997f9dcbf2ccefe3a200ef4d7025270aafb1d040b20974f747582  nSplit
```

Failure lines for the killed mutants (same shape as §3):

```
self-test: D1: successor scored 6, expected <6          (nGa)
self-test: D2: successor scored 6, expected <6          (nGb)
self-test: D4: successor scored 6, expected <6          (nGd)
self-test: D5: successor scored 6, expected <6          (nGe)
self-test: D6: successor scored 6, expected <6          (nGf)
self-test: D3: successor scored 6, expected <6          (nGdir4)
self-test: H1: successor scored 5, expected 6           (nGdir4)
```

The four window/scope/cue mutants still exit 0 with no `self-test:` failure lines, and the
constructed flippers still flip (probe2 on the landed bytes):

```
$ python3 -B probe2.py /tmp/r62c2/nbase
C7 ancient-section R-a: successor 5 of 6; C8 distant R-b names: 5 of 6;
C9 three-line R-c pair: 5 of 6; C10 inverted+split R-c: 5 of 6; C11 no landed-scope cue: 5 of 6
$ probe2.py nGc3 → C7 6 of 6 (only);  nGc2 → C8 6 of 6 (only);
  nGc → C10 6 of 6 (only);           nGc4 → C11 6 of 6 (only)
```

**Verdicts on the landed `604ae4fb` bytes:** G-a/G-b/G-d/G-e/G-f killed (same D tree each),
direction guard killed (D3, with H1 collateral), **G-c window/scope/cue still survived at all
four sites**. The landed hardening does not close the window coverage gap.

## 4. Split-evaluator hollow — the public CLI wired to the frozen counter

Edit in `main()` (line 642): `score, why = check_repairs(blobs, tree_names, census_regular)`
→ `score, why = frozen.check_repairs(blobs)`. Mutant sha256
`1bdd8a7115d959fd099472cf9ad1b63dc7e0a883c7e46c1d4ffab6ad47f6330d`.

```
$ python3 -B Msplit/verifiers/check_routed_repairs_v2.py --self-test; echo "EXIT=$?"
G-a paired population control: 29 names/committed 29=6; 30 names/committed 29=5; 30 names/committed 30=6; frozen=6/6/5
label-only constants fail controls: constant 6 vs base 0; constant 0 vs H1 6; constant 0 vs H2 6
frozen counter before: D1 6 of 6; D2 6 of 6; D3 6 of 6; D4 6 of 6; D5 6 of 6; D6 6 of 6; H1 4 of 6; H2 tip 6 of 6
self-test base CLI output:
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after file: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
self-test tip CLI output:
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after file: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
self-test CLI exits: base rev f3246d1493b60ea1c0d947a19c39f9e08e92f326 exit 1; tip rev 45a7ecfac9e203297f3146c45d63f5e79367470c exit 0; unreadable rev routed-repairs-v2-no-such-revision exit 2
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

### 4b. The same mutation on the landed bytes is killed — the hollow is closed in `604ae4fb`

```
$ python3 -B nSplit/verifiers/check_routed_repairs_v2.py --self-test ; exit 1
self-test: CLI dependency arm: a zero-score scorer must make the tip CLI exit 1, score 0 (observed exit 0, score 6)
self-test: CLI dependency arm: a six-score scorer must make the base CLI exit 0, score 6 (observed exit 1, score 0)
successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6
```

Mutant sha256 `d716b1c15c6997f9dcbf2ccefe3a200ef4d7025270aafb1d040b20974f747582`
(`604ae4fb` with the same one-line `main` edit). The printed predicate line is still
identical under the split — detection is the exit code plus the stderr CLI-dependency arm.
The §4 hollow is therefore a property of the assigned `de5e3471` bytes; it is closed at the
landed `604ae4fb`.

## 5. Observation on the draft that became `604ae4fb` (snapshot, not the §4 verdict)

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
the mutant is still `successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6`
— the line alone is not the detector; the exit code is. The snapshot was later committed as
`604ae4fb` at `e424f2a`; §3.8/§4b carry the verdicts for those landed bytes.

## 6. Restoration

```
$ for m in <all copies>; do cp -f base/verifiers/check_routed_repairs_v2.py $m/verifiers/check_routed_repairs_v2.py; done
$ for m in base MGa MGb MGc MGc2 MGc3 MGc4 MGd MGe MGf MGdir MGdir2 MGdir3 MGdirBoth MGdir4 Msplit; do
    printf "%s %s\n" "$(sha256sum $m/verifiers/check_routed_repairs_v2.py | cut -d' ' -f1)" "$m"; done
de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7 base
de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7 MGa
de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7 MGb
de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7 MGc
de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7 MGc2
de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7 MGc3
de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7 MGc4
de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7 MGd
de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7 MGe
de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7 MGf
de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7 MGdir
de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7 MGdir2
de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7 MGdir3
de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7 MGdirBoth
de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7 MGdir4
de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7 Msplit
$ for m in base MGa MGb MGc MGc2 MGc3 MGc4 MGd MGe MGf MGdir MGdir2 MGdir3 MGdirBoth MGdir4 Msplit; do
    python3 -B $m/verifiers/check_routed_repairs_v2.py --self-test > /tmp/r62c2/$m.restored.out 2>&1
    printf "%s exit=%s\n" "$m" "$?"; done
base exit=0
MGa exit=0
MGb exit=0
MGc exit=0
MGc2 exit=0
MGc3 exit=0
MGc4 exit=0
MGd exit=0
MGe exit=0
MGf exit=0
MGdir exit=0
MGdir2 exit=0
MGdir3 exit=0
MGdirBoth exit=0
MGdir4 exit=0
Msplit exit=0
   (final line in every one: "successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6")
$ python3 -B probe.py /tmp/r62c2/Msplit      (restored copy)
D1..D6: successor 5 of 6 REJECTED ... (identical to pristine baseline)
$ cp -f wt-v2-604ae4fb.py Mdraft/verifiers/check_routed_repairs_v2.py && sha256sum Mdraft/verifiers/check_routed_repairs_v2.py
604ae4fb41779874eb420e8a904cb2ebdd953fa41dfc5f270ece53562b5c414d  Mdraft/verifiers/check_routed_repairs_v2.py
   (the §5 snapshot copy restored to its source bytes; this copy is not part of the assigned target)
```

Landed-byte copies (§3.8/§4b), restored to `604ae4fb`:

```
$ for m in nGa nGb nGc nGc2 nGc3 nGc4 nGd nGe nGf nGdir4 nSplit; do cp -f nbase/verifiers/check_routed_repairs_v2.py $m/verifiers/check_routed_repairs_v2.py; done
$ for m in nbase nGa nGb nGc nGc2 nGc3 nGc4 nGd nGe nGf nGdir4 nSplit; do
    printf "%s %s\n" "$(sha256sum $m/verifiers/check_routed_repairs_v2.py | cut -d' ' -f1)" "$m"; done
604ae4fb41779874eb420e8a904cb2ebdd953fa41dfc5f270ece53562b5c414d nbase
604ae4fb41779874eb420e8a904cb2ebdd953fa41dfc5f270ece53562b5c414d nGa
604ae4fb41779874eb420e8a904cb2ebdd953fa41dfc5f270ece53562b5c414d nGb
604ae4fb41779874eb420e8a904cb2ebdd953fa41dfc5f270ece53562b5c414d nGc
604ae4fb41779874eb420e8a904cb2ebdd953fa41dfc5f270ece53562b5c414d nGc2
604ae4fb41779874eb420e8a904cb2ebdd953fa41dfc5f270ece53562b5c414d nGc3
604ae4fb41779874eb420e8a904cb2ebdd953fa41dfc5f270ece53562b5c414d nGc4
604ae4fb41779874eb420e8a904cb2ebdd953fa41dfc5f270ece53562b5c414d nGd
604ae4fb41779874eb420e8a904cb2ebdd953fa41dfc5f270ece53562b5c414d nGe
604ae4fb41779874eb420e8a904cb2ebdd953fa41dfc5f270ece53562b5c414d nGf
604ae4fb41779874eb420e8a904cb2ebdd953fa41dfc5f270ece53562b5c414d nGdir4
604ae4fb41779874eb420e8a904cb2ebdd953fa41dfc5f270ece53562b5c414d nSplit
$ for m in nbase nGa nGb nGc nGc2 nGc3 nGc4 nGd nGe nGf nGdir4 nSplit; do
    python3 -B $m/verifiers/check_routed_repairs_v2.py --self-test > /tmp/r62c2/$m.restored.out 2>&1
    printf "%s exit=%s\n" "$m" "$?"; done
nbase exit=0 ... nSplit exit=0   (12/12 exit 0; each prints
                                 "successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6")
```

Lane verifiers at seat end (HEAD `f60590a`):

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && sha256sum verifiers/check_routed_repairs_v2.py verifiers/check_routed_repairs.py
604ae4fb41779874eb420e8a904cb2ebdd953fa41dfc5f270ece53562b5c414d  verifiers/check_routed_repairs_v2.py   (committed at HEAD; was de5e3471 at e6da78b/3f91150)
95ade9be1ed1930266bce4b98c8c593fff1feba89e2cf25763f0aa83f206cb88  verifiers/check_routed_repairs.py     (unchanged throughout; never edited)
$ git status --porcelain -- verifiers/
(empty)
```

During the mutation runs the v2 working-tree copy held `604ae4fb` uncommitted (§5); the
integrator committed it at `e424f2a`. This seat never wrote either verifier — its only lane
write is this report.

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

Re-run on the landed `604ae4fb` (§3.8/§4b): the same rows with one change — the
public-CLI→frozen swap is **killed** (exit 1, CLI-dependency arm); G-c's four sites still
exit 0 (**survived**); every other row is unchanged (killed, same D tree).

Findings for the L1 (not contract changes):

1. The committed D universe covers one hardening mechanism each for R-a count, R-a
   assertion, R-d body, R-e ids, R-f ancestry, and the R-c direction guard — but **no D tree
   exercises any window/scope/cue bound** (four independent disables survive the self-test on
   both `de5e3471` and the landed `604ae4fb`). Constructed frozen-6 trees (C7 ancient-section
   markers, C8 distant R-b names, C10 inverted+split R-c, C11 no landing cue) are rejected by
   pristine v2 and accepted when the matching bound is removed; they are the missing D-classes.
2. For the assigned `de5e3471` bytes, `--self-test` cannot tell a public CLI wired to the
   frozen counter from the hardened one: the D/H1 arms bypass `main`, and the two CLI arms are
   the two points where the evaluators agree by construction (0 at base, 6 at tip, with the tip
   frozen score separately asserted). The landed `604ae4fb` closes this with a CLI-dependency
   arm (§4b), but the printed predicate line alone still does not detect the swap — the exit
   code is the detector.
3. D3's rejection is over-determined inside R-c (C1-between *and* negation-between *and* the
   C1-denial requirement); it cannot attribute to one named guard, and the plan's G-a…G-f
   list does not name the direction guard at all.

## 8. Bounds

* Verdicts are given for the assigned bytes sha256 `de5e3471…` (§3/§4; blob at `e6da78b`
  and `3f91150`) and re-run on the landed bytes `604ae4fb…` (§3.8/§4b; HEAD `f60590a`).
  The two sets differ only in self-test arms, not in the six guard functions.
* Not attacked here (other wave-2 seats): `check_erratum_absorption.py`,
  `check_scoped_rules_v31.py`, the receipt numbers themselves, the registry/rows.
* `TIP_REV` in the instrument is the plan-freeze commit `45a7ecfa`, not the data revision
  `3e7aed9b`; I measured the CLI at base, `45a7ecfa`, `3e7aed9b` and the clone's `master`
  (`e6da78b`) separately.
* No installs or updates were made (nothing needed). No git/jj write, no `.ufo/state`, no
  lane product/verifier/corpus/fleet/MANIFEST edit; the only lane write is this report.
