# B21RevMethod — how a 15-line folded block was counted as 6 frontmatter lines

VERDICT: M75-1's five numbers reproduce byte-exactly and its conclusion is false; the description renders **1022** characters (YAML `>` clip newline kept) and **1021** stripped, identical at all four revisions (r75 base/tip, r76 base/tip); the `awk NR>=3&&NR<=8` window measured **372 of 1022** value characters (36.4 %); the generalizable shape is **layout-window substitution for a rendered value**, and the frozen R1 label ("1022") is reachable only under the clip convention — naive frontmatter slicing prints 1021. Proposed Q74 row and M76-1 row in §7; four convention alerts sent (§8).

Report: .ufo/waves/round-76/w1/B21RevMethod.md

## Axes

Consistency (the axis the r75 closure harmed and C2 repairs), calibration (why the lane's own Q74/M76-1 must name a surface, not a habit), coverage (four revisions measured, three renderers, one falsification experiment), operability (a 2-line red/green detector a plan can run before freeze), adjacency (the lane's existing G4 guard already measures 1021 — the two conventions are already live side by side).

## 1. The two contracts that were confused

There are two different objects in this file and they have different extents:

| object | extent in `SKILL.md` | what it is |
|---|---|---|
| YAML **source layout** of the description | page lines 3–18 (marker + 15 content lines), closing fence line 19 | syntax: an indicator, 2-space indents, line breaks at a wrap column chosen by the author |
| YAML **rendered value** of `description` | 1022 chars (1021 stripped) | the payload a router ingests — on opencode "the full `description` byte-for-byte", on omp the key of the `(name, description-as-loaded)` preview row |

The r75 lesson measured the first and reported it as the second. Every downstream sentence in that row and in the `## Gate` reject candidate is a consequence of that substitution:

- `corpus/lessons/round-75.md:11` (M75-1, class `stale-premise`): "current committed SKILL frontmatter (master 65a5c7a, lines 3–18) is substantially shorter; direct `awk 'NR>=3&&NR<=8{print NR ":" length($0) ":" $0}'` yields 14,76,78,73,79,72 for frontmatter lines 3–8."
- `corpus/lessons/round-75.md:5` (`## Gate`, reject candidate): "any claim that the 1021-character description size reported in `considerthese/2026-10-26.md` remains current; current frontmatter is materially shorter."

Note the row already names the correct extent — "lines 3–18" — and then measures 3–8. The command and the extent it claims to cover disagree inside one cell, and nothing in the lane recomputes a lesson premise from bytes, so it survived to closure.

## 2. Evidence chain (commands as run, exit codes observed)

Working tree `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, tip `4de12b61f75c73e3675ef0e422cc2be0f7da8960`; measured revisions `65a5c7a6…` (r75 base), `ac9f2951…` (r75 tip), `b7f13f4b…` (r76 base), `4de12b61…` (r76 tip).

```
$ awk 'NR>=3&&NR<=8{print NR ":" length($0) ":" $0}' SKILL.md        # exit 0
3:14:description: >
4:76:  Prompt & skill craft — audits, writes, and rewrites SKILL.md / AGENTS.md /
5:78:  dispatch prompts / system prompts for trigger fidelity and decision density.
6:73:  Triggers: "skill file", "SKILL.md", "frontmatter description", "trigger
7:79:  words", "prompt craft", "write a skill", "audit this skill", "skill quality".
8:72:  Anti-triggers: general prompt engineering for model outputs (not skill
```

```
$ for r in 65a5c7a6… ac9f2951… b7f13f4b… 4de12b61…; do git show "$r:SKILL.md" | python3 -B -c "
import sys,yaml
raw=sys.stdin.read(); L=raw.split('\n'); end=L.index('---',1)
a=yaml.safe_load('\n'.join(L[1:end])+'\n')['description']   # clip newline kept
b=yaml.safe_load('\n'.join(L[1:end]))['description']        # naive slice
print('clip=%d stripped=%d bytes=%d fence_line=%d'%(len(a),len(b),len(a.encode()),end+1))"; done   # exit 0
65a5c7a6 clip=1022 stripped=1021 bytes=1026 fence_line=19
ac9f2951 clip=1022 stripped=1021 bytes=1026 fence_line=19
b7f13f4b clip=1022 stripped=1021 bytes=1026 fence_line=19
4de12b61 clip=1022 stripped=1021 bytes=1026 fence_line=19
```

Both measures on the current `SKILL.md`, as the seat requires them printed:

- **line window** `awk NR>=3&&NR<=8` → `14,76,78,73,79,72`, sum **392**;
- **YAML folded render, whole block** → **1022** characters (clip), **1021** stripped, **1026** UTF-8 bytes (clip) / 1025 stripped; first sentence **151** chars; marker line 3, content lines **4–18** (15), closing fence 19; `SKILL.md` is 590 lines.

Line 8 ends mid-sentence (`… (not skill`) and line 9 is indented — the window provably stops inside the block. First sentence measured:

```
Prompt & skill craft — audits, writes, and rewrites SKILL.md / AGENTS.md / dispatch prompts / system prompts for trigger fidelity and decision density.
```
151 chars, so `considerthese/2026-10-26.md:17`'s "about 150 chars" is also current, and the omp render cliff (99) cuts this sentence 52 chars before its end.

## 3. Mechanism, step by step

1. **Anchor on the marker, guess the end, pick a round window.** `description: >` is page line 3; the author took `NR<=8`, i.e. six lines, a number with no relation to the block. The block's end is line 18 (closing fence 19). Rationale for 6 is unrecorded — [INFERENCE] it was a "few lines is enough to see it's short" sample.
2. **Count source lines, not the value.** `length($0)` returns characters of the *source line*, so the measure includes (i) the marker line `description: >` — 14 chars of YAML syntax that are never in the value, and (ii) the 2-space indent on each of the 15 content lines — 30 chars of layout. It excludes (iii) the 14 join spaces folding inserts and (iv) the clip newline.
3. **Truncate silently.** The window captures content lines 4–8 only. Rendered, that is 76+78+73+79+72 = 378 raw, minus 10 indent chars = 368, plus 4 join spaces = **372 value characters — 36.4 % of 1022**. The remaining 10 content lines (≈650 value chars: anti-triggers, sibling boundary, NOT-kotodama note) never entered the sum.
4. **Compare across surfaces.** 392 (a partial sum of source lines) was read as "the description is materially shorter" than considerthese's 1021 (a whole rendered value). The two operands differ in extent *and* unit; the comparison is not a measurement of anything.
5. **Label the class from the conclusion.** Because the number came out small, the row was classified `stale-premise` — "the proposal's imported observation is stale". The actual class is a measurement-method error; nothing was stale. The mislabel is why R1 routes to quality/calibration rather than to a source problem.
6. **No recompute anywhere.** The row's `captured-by` cell names three criteria that *do not* catch it (Q67, Q54, Q60) and no criterion that does — the cell records the absence of a guard. The fix cell ends "This lesson-only repair is not claimed as a guard until a failing fixture demonstrates it", so the false premise shipped with a note promising a guard that no round built. Q74 is that guard.

Exact arithmetic of the right measure, so the counter can be written dependency-free:

```
content stripped chars = 1007   (15 content lines, indents removed)
folding joins          =   14   (one space per line break)
clip trailing newline  =    1
                       ----
render                 = 1022   ; stripped = 1021 ; UTF-8 bytes = 1026 (2 em dashes × 3 B = +4)
raw sum 3–18           = 1051   (= 1007 + 30 indents + 14 marker)
```

A coincidence worth naming: the marker line is 14 chars and the block has 14 joins, so `raw − error terms` lands on 1021 by accident for *this* block. A spot-check that only checks the final digit will "confirm" the wrong method; on any block whose marker length ≠ join count it drifts.

## 4. Why the rendered value is the correct measure

**(4.1) It is the payload the contract is about.** The lane's own rule is that the frontmatter `description` is "the only part any router ingests" (`SKILL.md:21-23`); on opencode it renders "the full `description` byte-for-byte". Source line lengths are not ingested by anything. A measure of an artefact must be a function of the artefact, not of its typesetting.

**(4.2) Reflow falsification — decisive.** I rebuilt the same value at four wrap widths and measured both ways:

```
rewrap width= 60: raw-line sum(marker+content)=1055  render=1022  identical_value=True
rewrap width= 72: raw-line sum(marker+content)=1052  render=1022  identical_value=True
rewrap width= 76: raw-line sum(marker+content)=1051  render=1022  identical_value=True
rewrap width=100: raw-line sum(marker+content)=1047  render=1022  identical_value=True
```

The raw sum moves 1047→1055 with no change to a single character of the value; the render is constant at 1022. A quantity that changes when the artefact does not is a function of the layout, so it cannot be the measure of the description. (Width 76 reproduces the shipped file's own 1051, which is why the incorrect method looks stable in place.)

**(4.3) Three independent renderers agree.** PyYAML 6.0.3 (`yaml.safe_load`), Ruby Psych (`ruby -ryaml`), and a hand fold (strip indent, join with single spaces, append the clip newline) all give 1022 / 1021. Note *no verifier in `verifiers/` imports yaml* — `grep -n "import yaml" verifiers/*.py` is empty and the lane hand-parses block scalars (`check_sibling_census.description_of`, `SKILL.md`-reading guards). The hand fold is therefore the house-compatible implementation.

**(4.4) The two live conventions, and the off-by-one that repeats the defect.** YAML `>` is clip-chomped: the value keeps exactly one trailing line break, so a file-faithful parse yields 1022. Two everyday implementations print 1021:

- the naive frontmatter slice `"\n".join(lines[1:end])` — drops the break before the closing fence;
- the lane's existing G4 guard, `check_sibling_census.description_of()`, which collapses whitespace and `.strip()`s, and prints **1021** for these bytes at every revision I measured (its cap is `SKILL_DESCRIPTION_MAX = 1024`, `check_sibling_census.py:418` — so headroom is 2 chars clip / 3 stripped).

Frozen R1 requires the receipt to print **1022**. A counter that slices naively prints 1021 and fails the frozen label while having measured the same bytes correctly-in-spirit; a counter that hardcodes 1022 without recomputing turns a measurement into a literal. Both failure modes are the M75-1 family one level down, so the convention must be *named* beside the number, and the number *recomputed*. I sent the recipe and both values to B07 (repair counter), B06 (desc counter), B08 (lesson correction) and the L1; B13 was told the cap headroom in case the description is edited.

## 5. Divergences recorded (not repaired by this seat)

| # | divergence | evidence | disposition |
|---|---|---|---|
| D-a | M75-1 measured a truncated window and called it the description | §2, §3 | R1 repair in flight (B08 correction + B07 counter) |
| D-b | M75-1's class label `stale-premise` is wrong; the premise was current | 1021/1022 vs considerthese's 1021 | R1; Q74's grounding should name the misclassification so the class is not inherited |
| D-c | the row names the extent "lines 3–18" and measures 3–8 in the same cell | `round-75.md:11` | R1 correction should name this self-contradiction explicitly — it is the cheapest tell |
| D-d | `captured-by` cell names criteria that do not catch the defect, i.e. it records the absence of a guard | `round-75.md:11` | Q74 (this round) |
| D-e | R1 "prints 1022" vs the lane's own G4 "1021" for identical bytes — two conventions, one char apart | §4.4 | **closed at freeze**: `plans/round-76-addendum-1.md` § "Render-length convention (off-by-one closure)", committed `7eed80e9`, fixes the frozen convention as clip-preserving = 1022 and requires every receipt to print both variants (clip 1022 / stripped 1021), naming the convention; predicates unmoved |

## 6. Mechanical detector (red at the r75 window, green at the block)

Two lines, no parser, usable by any plan before freeze — a sampled window is complete only if the line after it starts at column 0:

```
$ sed -n '9p' SKILL.md | grep -qc '^ ' ; echo $?     # window 3-8  -> 0  = truncated (line 9 is indented)
$ sed -n '19p' SKILL.md | grep -qc '^ ' ; echo $?    # window 3-18 -> 1  = complete (line 19 is `---`)
```

Generalized form: for a sampled window `[a,b]` over a block scalar, assert `lines[b]` (1-based) is empty or starts at column 0. Combined with "the marker line is syntax, not value" and "measure the render", this kills the class without a YAML dependency. A counter-level version (Q74) should also recompute the value and refuse a claimed number that differs from it by >0 chars — not ±1 — since ±1 is precisely the tolerated slop that let this through.

## 7. Generalizable failure shape → Q74 and M76-1 (proposed text; owned by other seats)

**Name:** *layout-window substitution for a rendered value* — a measure taken on a fixed window of a structured artefact's **source lines** is reported as a measure of the artefact's **rendered value**, and then compared against a whole-value number from a different surface. Five sub-classes, all present in M75-1:

1. **truncated window** — end chosen by habit, not by the block boundary (3–8 vs 3–18);
2. **syntax in the measure** — the `description: >` indicator and the 2-space indents counted as content (1051 raw vs 1022 value);
3. **unit drift** — characters vs bytes (1022 vs 1026; the two em dashes account for +4 B);
4. **slice off-by-one** — clip newline dropped (1021 vs 1022), which is how a correct implementation can still miss a frozen label;
5. **cross-surface comparison** — partial sum vs whole value, concluded as "materially shorter".

**Proposed M76-1 row** (`corpus/lessons/round-76.md` § Mistakes; owner B17/B08, not written by me):

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| `layout-window-counted-as-value` | `corpus/lessons/round-75.md:11` measured the description with `awk 'NR>=3&&NR<=8'` (6 of the block's 16 source lines, 372 of 1022 rendered chars) and `:5` rejected considerthese's 1021 on that basis; committed bytes render 1022 clip / 1021 stripped at 65a5c7a, ac9f295, b7f13f4b and 4de12b61 (block lines 4–18). The reflow test moves the raw sum 1047→1055 with an identical value. | Q74 (a measure names its surface and unit; a sampled window must end at a block boundary and be recomputed from the rendered value) | Recompose the number from the render at a named revision (hand fold: strip indent, join with one space, append the clip newline) and state the convention beside it; the detector is `sed -n '<b+1>p' | grep -qc '^ '` → exit 0 means the window is truncated. |

**Proposed Q74 row** (`corpus/QUALITY.md`; next free id is Q74 — highest present is Q73; owner B17/B05, not written by me):

| id | criterion | applies to | grounded in | supersedes |
|---|---|---|---|---|
| Q74 | A count of a structured field is taken on the **rendered value at a named revision**, never on a fixed window of its source lines: for a block scalar the counter strips the indent, joins continuation lines, keeps the clip newline, and prints the convention (`clip` / `stripped`) beside the number; a sampled line window must end at a block boundary (`sed -n '<b+1>p' … | grep -qc '^ '` exits 1) or the measurement is refused, and a lesson/Gate premise that consumes an imported figure carries that recomputation, not a prose assertion. Extends Q13 (a count carries its command) with the missing half — the command must measure the same surface as the claim — and does not supersede it. | lesson/plan/entry counts of YAML or JSON fields; self-audit tables | M76-1 `layout-window-counted-as-value` (`corpus/lessons/round-76.md`); `corpus/lessons/round-75.md:11` M75-1 was itself misclassified `stale-premise`; `corpus/lessons/round-75-verifier-spotcheck.md` §4 DISAGREE row | — |

Why this is not Q13 again: Q13 makes a count publish its command; M75-1 published its command and the command measured a different object than the sentence claimed. Q74 binds the command's *surface* to the claim's surface, and adds the boundary test that would have failed at `NR<=8`.

## 8. Coordination sent (4 messages, no lane writes)

| to | content |
|---|---|
| `B07RepairCounter` | R1 recipe: keep the clip newline (`+ "\n"`) → 1022; naive slice → 1021; dependency-free fold 1007+14+1; suggested receipt wording |
| `B06DescCounter` | C1 (d) must pin the convention; 1022 clip / 1021 stripped / 1026 B; G4 already prints 1021; no verifier imports yaml |
| `B08LessonDrafts` | exact numbers for the R1 correction, the two distortions in one sentence, and the "do not write 1021 alone" warning |
| `KotobaR76` (L1) | decision datum: R1's 1022 is attainable only under the clip convention → L1 committed `plans/round-76-addendum-1.md` at `7eed80e9` naming the convention (clip 1022 / stripped 1021, both printed per receipt), predicates unmoved |

## 9. Coverage, limits, calibration

- **Measured, not inferred:** the awk window, the render at four revisions, first-sentence length, byte counts, the reflow experiment, the detector's exit codes, G4's 1021, `SKILL.md` = 590 lines, absence of a yaml import in `verifiers/`.
- **Inference, marked:** the motive for `NR<=8` (§3.1); that a description edit is optional for C1 (§8).
- **Not measured by this seat:** S213 itself (not fetched here — C1's sourced half belongs to the fetch/quote seats); the frozen counters (`verifiers/check_desc_craft.py`, `verifiers/check_r75_routed_repairs.py` are **absent** at tip `4de12b61` — verified by `ls`), so no counter verdict is claimed; no gate was run beyond the two one-line detectors.
- **Freshness:** all four revisions measured today; frontmatter bytes identical across them, so this seat's numbers hold for r75 and r76 alike and do not decay while the description is untouched.
- **Confidence:** high on the mechanism and on both numbers (three renderers, one falsification experiment, arithmetic closes to the character). Medium on the *intent* of the r75 window choice — marked as inference; it does not affect the repair.
- No scratch dir was created (no clone needed; all reads were `git show`/`read`), nothing installed, no git/jj writes, no lane file edited.

## 10. Pointer hygiene (Q68/Q60, measured not assumed)

Three of my backticked pointers name artefacts that do not exist at the revision I measured — they are this round's planned outputs, and I say so rather than hide it:

```
$ python3 -B verifiers/check_report_pointers.py --report .ufo/waves/round-76/w1/B21RevMethod.md \
    --repo /home/vgpnk/Projects/shokunin/kotoba-shokunin --rev 4de12b61… --round 76   # exit 0
report pointers resolved 17 of 23; unresolved 6
$ … --rev 7eed80e9                                                                    # exit 0
report pointers resolved 19 of 23; unresolved 4
```

Unresolved at `7eed80e9`: `corpus/lessons/round-76.md` (lines 143, 153 — the row I *propose*, owned by B17/B08) and `verifiers/check_desc_craft.py` / `verifiers/check_r75_routed_repairs.py` (line 170 — the counters I measured as **absent**, §9). `plans/round-76-addendum-1.md` resolves at `7eed80e9` (`git cat-file -e 7eed80e9:plans/round-76-addendum-1.md` exit 0) and does not exist at the measured rev (`exit 128`), so per Q60 it is cited by its committing rev, never as a bare pin at `4de12b61`. Nothing else is unresolved.

## 11. Reproduce (single block, exit 0)

```
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
awk 'NR>=3&&NR<=8{print NR ":" length($0)}' SKILL.md                # 3:14 4:76 5:78 6:73 7:79 8:72  (sum 392)
python3 -B - <<'PY'
import yaml
L=open("SKILL.md",encoding="utf-8").read().split("\n"); end=L.index("---",1)
a=yaml.safe_load("\n".join(L[1:end])+"\n")["description"]   # clip newline kept
b=yaml.safe_load("\n".join(L[1:end]))["description"]        # naive slice
print("render", len(a), "stripped", len(b), "bytes", len(a.encode()), "block 4 -", end)
PY                                                                    # render 1022 stripped 1021 bytes 1026 block 4 - 18
sed -n '9p' SKILL.md | grep -qc '^ '; echo "window 3-8 truncated=$?"  # 0
sed -n '19p' SKILL.md | grep -qc '^ '; echo "window 3-18 truncated=$?" # 1
```
