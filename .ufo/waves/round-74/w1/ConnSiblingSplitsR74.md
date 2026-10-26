# ConnSiblingSplitsR74 — cross-lane pattern scan for C2 (freshness / adjacency)

**Seat:** `ConnSiblingSplitsR74` (connector). Lane `kotoba-shokunin`, round 74, wave 1.
**Scope of this seat:** the C2 sibling split-statement scan the plan assigns to the connector —
read the committed bytes at the 20 frozen fleet heads, find every place a sibling names `kotoba`,
prompt craft, SKILL.md authorship, frontmatter or descriptions, classify each hit, and say per
lane whether the hits change the round-49 classification rule outcome.

**Verdict:** the round-49 **classification rule outcome** (contested / adjacent / none) is
**unchanged for all 20 lanes** — 0 lanes become `contested`, 0 lanes change class. What changes is
the **row content** the new entry must carry: exactly **one** lane's row changes (revenger, whose
`SKILL.md` was created after the r49 pin), and exactly **one** lane (tabi) is a `none` row whose
`SKILL.md` body names kotoba — a lane the plan's predicate (e) would refuse and the base rule does
not. The plan's frozen predicate for C2 has **two construction defects** (§3.1, §3.2) and **two
traps** (§3.3, §3.4) that a counter built naively on the plan text would inherit. Each is stated
below with the command that shows it.

---

## 1. The sweep (the command that found everything)

Sweep command, run once per lane, at the frozen head40 from
`.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv`:

```
git -C /home/vgpnk/Projects/shokunin/<lane>-shokunin grep -n -w -i kotoba <head40> -- .
```

The `.ufo/` and `LOG.md` hits are excluded from the scope surface set (r49 rule:
"Wave reports and run logs (`.ufo/`, `reports/`) are not scope surfaces") and are reported
separately in §5. Every lane's head40 resolves:

```
$ tail -n +3 .ufo/waves/round-74/receipts/sibling-heads-freeze.tsv | while IFS=$'\t' read -r lane branch head skill prov; do
    R=/home/vgpnk/Projects/shokunin/${lane}-shokunin
    git -C "$R" rev-parse --verify --quiet "$head^{commit}" >/dev/null && printf '%s\t%s\n' "$lane" head_ok
  done
```
→ 20 of 20 `head_ok` (output verified; every lane's head40 resolves to a commit).

Per-lane hit counts at the frozen heads (tree-wide, `git grep -n -w -i kotoba <head40> -- .`):

| lane | tree (excl. `.ufo`/`LOG.md`) | `.ufo`+`LOG.md` | scope surfaces (SKILL.md / PROVINCE.md / corpus/) |
|---|---|---|---|
| audio | 0 | 0 | 0 |
| chousa | 2 | 153 | 0 |
| game-dev-2d | 3 | 0 | 0 |
| game-dev-3d | 2 | 0 | 0 |
| kagi | 43 | 385 | 31 |
| kaidoku | 2 | 87 | 0 |
| kake | 2 | 176 | 2 |
| kama | 13 | 295 | 11 |
| kasegi | 4 | 252 | 4 |
| kengaku | 99 | 1047 | 91 |
| kotodama | 105 | 111 | 6 |
| kumitate | 4 | 510 | 3 |
| lore | 1 | 16 | 0 |
| mado | 0 | 137 | 0 |
| mori | 38 | 338 | 37 |
| revenger | 1 | 40 | 1 |
| souji | 315 | 116 | 0 |
| tabi | 10 | 107 | 5 |
| tameshi | 4 | 264 | 4 |
| tsukuroi | 3 | 64 | 3 |

Full hit list with the token test per line:
`.ufo/waves/round-74/w1/build/ConnSiblingSplitsR74/kotoba-hits-frozen-heads.tsv`
(651 rows, 246 KB; `.ufo`/`LOG.md` counts summarised in its header).

**Token-test note (Q14/negative claims):** the sweep uses GNU `grep -w`, whose word-boundary
rules differ from the base checker's `token_in()`. GNU `grep -w kotoba` matches `makura-kotoba`
because `-` is a non-word character; the checker's `token_in` rejects it:

```
$ printf 'makura-kotoba\n' | grep -ow kotoba
kotoba
$ python3 -c "import importlib.util;s=importlib.util.spec_from_file_location('c','verifiers/check_sibling_census.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m);print([(x,m.token_in('kotoba',x)) for x in ('kotoba-shokunin','makura-kotoba','kakekotoba','Hanakotoba','kotoba')])"
[('kotoba-shokunin', True), ('makura-kotoba', False), ('kakekotoba', False), ('Hanakotoba', False), ('kotoba', True)]
```

Consequence, measured: on scope surfaces, `grep -w` yields **198** hits fleet-wide of which **3 are
hyphen false positives**, all in kotodama's Japanese-language corpus
(`corpus/knowledge/linguistics/orality-formulaic-language.md:59` and `:77` — `makura-kotoba`,
`kakekotoba`; `corpus/knowledge/linguistics/sociolinguistics-registers.md:104` — `Onna-kotoba`).
Every other lane's scope hits are real tokens. **Any C2 counter that greps rather than using the
base checker's `token_in` will over-count kotodama by 3 and could fabricate a `none`-row violation
for a lane whose tree contains a Japanese literary term.**

---

## 2. Per-lane table: hits, hit kinds, reclassification

Hit kinds: **(a)** split statement (the sibling states who owns what) · **(b)** mere citation ·
**(c)** claim over kotoba's core. Reclassification is measured against
`corpus/knowledge/sibling-overlap-census-round49.md` § Classification rule (the `contested` /
`adjacent` / `none` arms and the wave-report exclusion).

| lane | r49 class | scope hits | hit kinds | reclassification? | evidence (path:line at frozen head) |
|---|---|---|---|---|---|
| audio | none | 0 | — | **no** | 0 hits tree-wide; `SKILL.md` absent at pin (freeze `skill_md_blob` = `-`) |
| chousa | adjacent | 0 (scope) | (b) ×2 tree | **no** | `MINT.md:52` "Rejected recipients for this material: lore, kotoba, kasegi, kama, kumitate,"; `SCORECARD.md:479` "prospectively at round 12 (kotoba reading" |
| game-dev-2d | none | 0 (scope) | (b) ×3 tree | **no** | all three in `reports/round-10{2,3,5}/` — wave reports, excluded by the r49 rule |
| game-dev-3d | none | 0 (scope) | (b) ×2 tree | **no** | `reports/round-101/r101-scout-roster.md:106`, `reports/round-104/skill/bleed.md:139` — wave reports |
| kagi | adjacent | 31 | (a) ×27, (b) ×4 | **no** (still `adjacent`) | `corpus/README.md:97` "kotoba owns the checklist/shape reading"; `corpus/adjacency.tsv:84` "`$HOME/.agents/AGENTS.md` kotoba shared-read"; `corpus/knowledge/adjacency-scope.md:66`, `:76` |
| kaidoku | none | 0 (scope) | (b) ×2 tree | **no** | `EXAMPLE.kama.md:51` "| kotoba | prompt & skill craft | instruction surfaces, not services |" — a **copy of kama's MINT table** (see §3.3) |
| kake | adjacent | 2 | (b) ×2 | **no** | `corpus/lessons/round-5-aggregator-mirror-pathless-cli-invocation.md:4,6` — "Filed by: kotoba round-5 report" (aggregator-owned, **not** a sibling-stated split) |
| kama | adjacent | 11 | (a) ×9, (b) ×2 | **no** (still `adjacent`) | `corpus/knowledge/cross-lane-scope.md:29` "**Kotoba** owns the instruction/agent surface and its model/fallback wording"; `MINT.md:42` |
| kasegi | adjacent | 4 | (b) ×4 | **no** | `corpus/lessons/round-5-aggregator-mirror-ambiguous-citation-base.md:4,6,18` — same aggregator-mirror shape |
| kengaku | adjacent | 91 | (a) ×7, (b) ×84 | **no** (still `adjacent`) | `PROVINCE.md:138` "| **kotoba** | prompt- and skill-craft rules —"; `PROVINCE.md:30` "- **kotoba:** prompt- and skill-craft rules"; `SKILL.md:3` frontmatter names kotoba |
| kotodama | adjacent | 6 | (a) ×3, (b) ×1, **false-positive** ×3 | **no** (still `adjacent`) | `PROVINCE.md:20` "(kake); prompt/skill craft (kotoba)."; `MINT.md:20,30`; `SKILL.md:3` anti-trigger "NOT prompt/skill craft (kotoba-shokunin)" |
| kumitate | adjacent | 3 | (a) ×2, (b) ×1 | **no** (still `adjacent`) | `PROVINCE.md:28` "Local model serving and endpoints → kama. Prompt and skill craft → kotoba." |
| lore | none | 0 (scope) | (b) ×1 tree | **no** | `reports/round-1/r1-current-scribe.md:73` — wave report |
| mado | none | 0 | — | **no** | **0 hits tree-wide**; negative claim carried by the sweep in §1 |
| mori | none | 37 | (b) ×37 | **no** | all `corpus/evidence/*.log` "SURFACE lane.kotoba: progressing" lines + `corpus/knowledge/roster-truth-r12.md:9` roster IDs — observability records, **no scope statement** |
| revenger | none | 1 | (b) ×1 | **no** (class unchanged) | `corpus/lessons/round-69.md:217` "kotoba's and tabi's seats" — a wave-seat reference |
| souji | none | 0 (scope) | (b) ×315 tree | **no** | 315 hits, **all** in `census/`, `results/`, `tests/vault/fixture-src-*` — fleet-hygiene census artifacts naming a lane directory |
| tabi | none | 5 | (b) ×5 | **no** (class unchanged) | `SKILL.md:1313,1450` "`LANES=\"protocol aggregator kasegi kengaku kake kumitate kotoba kagi kama\"`" — a roster string |
| tameshi | adjacent | 4 | (b) ×4 | **no** | `corpus/knowledge/fleet-kill-rate-ledger.md:127` "kotoba `verifiers/*` — file existence"; `:233` "**U8** — sightings (kake, kama, kotoba) have unresolved gate-ness" |
| tsukuroi | none | 3 | (b) ×3 | **no** | `corpus/knowledge/adjacency-anchors-r19.md:116` "\| IN-021 \| `kotoba:.ufo/round-22/scouts/A6.md:47`" — an anchor index |

**Summary of the classification question asked.** Under the r49 rule, `adjacent` requires a **split
of one artifact, function or trigger area** stated on a scope surface; `contested` requires a
**claim over kotoba's core**. Across 20 lanes at the frozen heads:

- **0 lanes** become `contested`. No sibling's scope surface claims kotoba's core.
- **0 lanes** change class. The 9 `adjacent` rows stay `adjacent`; the 11 `none` rows stay `none`.
- The `none` rows stay `none` **because every one of their scope-surface hits is a mere citation**
  (roster strings, observability logs, seat references, aggregator mirrors) and **none names kotoba
  in its `SKILL.md` or `PROVINCE.md`**, which is the r49 `none` condition.

The one `none` row that comes closest is **tabi**, and it is worth stating precisely because the
plan's predicate (e) depends on it: tabi's `SKILL.md` does contain the whole word `kotoba` at
`:1313` and `:1450`. But the base checker's `none` rule reads the **frontmatter description** and
`PROVINCE.md`, not the body:

```
$ git -C tabi-shokunin show 856fa9e1202179f5cfbd28c1f0efdd4eb1f426bb:SKILL.md | sed -n '1,6p'
---
name: tabi-shokunin
description: Domain specialist — browser & web-interaction craft. Rank: shonen (probation).
---
$ git -C tabi-shokunin show 856fa9e1202179f5cfbd28c1f0efdd4eb1f426bb:PROVINCE.md | grep -c -w -i kotoba
0
```

and the checker's own `mechanical_findings()` is what decides — it reads
`description_of(skill_text)` and `PROVINCE.md`, never the body of `SKILL.md`
(`verifiers/check_sibling_census.py:595-601`). So tabi stays `none` **under the base's rule**,
while the plan's predicate (e) ("no `none` row exists for a lane whose pinned `SKILL.md` or
`PROVINCE.md` contains the whole word `kotoba`") would read tabi's body hits and forbid the row.
**This is a contradiction between the plan's predicate (e) and the base rule the plan says to
apply. See §3.1.**

---

## 3. Construction defects and traps the C2 counter must not inherit

These are the findings that change what the counter should be. Each is measured, not asserted.

### 3.1 The plan's predicate (e) is wider than the base rule it must satisfy, and the difference is load-bearing

The plan's C2 predicate (e) reads:

> (e) no `none` row exists for a lane whose pinned `SKILL.md` or `PROVINCE.md` contains the whole
> word `kotoba` (recomputed by the counter).

The base rule the plan mandates for the row checks (predicate (a): "that row passes the **base's**
`check_sibling_census.py` row checks … a `none` row names no `kotoba` in the sibling's
**description** or `PROVINCE.md`") reads the **description**, not the whole file.

Measured at the frozen heads, the two disagree for exactly one lane:

```
$ (none-lane sweep)  # whole-word kotoba in SKILL.md or PROVINCE.md of every `none`-classed lane
tabi         SKILL.md  2 hit(s): L1313; L1450
```

tabi's two hits are the **watchdog `LANES` roster string** quoted as evidence that *tabi itself* is
absent from the roster — a fleet-roster quote, not a statement about kotoba's ownership:

```
$ git -C tabi-shokunin show 856fa9e1202179f5cfbd28c1f0efdd4eb1f426bb:SKILL.md | sed -n '1311,1314p'
- Fleet-level, reported not absorbed (carried from r5): tabi is still absent from
  the watchdog `LANES` roster — `scripts/shokunin-watchdog.sh:14` →
  `LANES="protocol aggregator kasegi kengaku kake kumitate kotoba kagi kama"`
```

**Consequence.** A counter that implements predicate (e) against the *whole* `SKILL.md` will refuse
tabi's `none` row, and the C2 score caps at **19 of 20** — not because a sibling moved, but because
the predicate is stricter than the rule it is supposed to re-derive. A counter that implements (e)
against the **description** (the base's semantics) scores 20 of 20 with tabi `none`, which is what
the r49 classification rule actually supports (§2).

**The move:** predicate (e) must be scoped to *the description or `PROVINCE.md`* — the base
checker's own `mechanical_findings` surface — or tabi must be reclassified, and §2 shows
reclassifying it is not supported by any hit. **The counter must not implement (e) as the plan
words it.** This is the second-order effect that the plan's own wording hides: it looks like a
"re-pin and re-read" predicate and is in fact a *stricter classification rule* wearing a
freshness predicate's clothes. Left as written, the C2 counter measures kotoba's own reading of a
sibling's prose rather than the sibling's bytes.

Note also the counter's scope: the base checker resolves sibling bytes with
`git_show(repo, commit, path)` (`verifiers/check_sibling_census.py:145-152`) — it never touches the
live working tree. Any C2 counter that greps a sibling's *checkout* instead of `git show` at the
pinned commit re-introduces the exact staleness the claim is meant to remove, because three lanes
have already advanced past the freeze (kake +1, kasegi +2, kotodama +2, souji +2 commits at
sweep time — `git -C <lane> rev-list --count <head40>..refs/heads/<branch>`).

### 3.2 The base checker's table shape is 9 columns, so a `delta` cell cannot live in the census table

The plan's predicate (c) requires "the row's `delta` cell". The base checker selects the census
table by **exact column count** (`CENSUS_COLUMNS = 9`, `verifiers/check_sibling_census.py:20`), and
`_select_table` falls back to "any row with that column count" only. A 10-column census table is
therefore **not found at all** — the checker reports zero rows and exits 1:

```
$ python3 -B verifiers/check_sibling_census.py worldA_delta.md
FAIL census table not found: no 9-column markdown table with a separator row in worldA_delta.md
rows 0 verified 0
exit=1
```

(world A = the r49 table with the commit cell bumped to the freeze head **and** a 10th `delta`
column added.)

The same file shape with the delta in a **separate 2-column table** works, because the 9-column
census table is still selected:

```
$ python3 -B verifiers/check_sibling_census.py worldD_census.md --province worldD_province.md
rows 20 verified 20
province rows 20 matched 20
exit=0
```

(world D = 9-column census table with the skill-file / names-kotoba / arbitration cells
**recomputed** at the frozen heads, plus a separate `| lane | delta |` table, plus a matching
`PROVINCE.md` § Adjacent table carrying the freeze commits.)

**Consequence.** "The row's `delta` cell" is not implementable inside the census table the base
checker reads. The r74 entry must carry the delta either (i) in a separate table beside the census
table, or (ii) in a column the counter itself adds **after** running the base row checks — and the
base row checks must be run against the **base's copy** of the checker, sha256-pinned
(`sha256(verifiers/check_sibling_census.py)` at base `1e03d1991bc02281b00a5b7a5e00c9d5d5d72908` =
`2f9d8a88b1d3dd8562455006d5ea89ec02546a1ecb9d023f327d88e5502eedc7`, unchanged at HEAD
`329e7d91d7d750031c35d264f0e34af1d0ce8385` — verified identical).

### 3.3 A cross-lane copy pattern worth recording: kama's MINT table is duplicated verbatim into kaidoku

`kaidoku/EXAMPLE.kama.md:51` carries kama's MINT province table verbatim, including the
`| kotoba | prompt & skill craft | instruction surfaces, not services |` row:

```
$ git -C kaidoku-shokunin show 3b1ab3c9d248b7afbf7fc5e5507d76cd87e26c3c:EXAMPLE.kama.md | sed -n '49,53p'
| kumitate | orchestration & tooling (ufo-fsd runtime, dispatch) | owns *how* routes are resolved, not *what a resolved endpoint serves* |
| kotoba | prompt & skill craft | instruction surfaces, not services |
| kagi | secrets & vault ops | owns credential hygiene *to* endpoints, not endpoint identity/liveness |
```

and kama's own copy:

```
$ git -C kama-shokunin show 3e6fdbe9e0ca1ca5b633d0b312d5561301e924c4:MINT.md | sed -n '42p'
| kotoba | prompt & skill craft | instruction surfaces, not services |
```

This matters for the C2 counter because **kaidoku's `none` row rests on a negative claim, and the
file that could break it is not in kaidoku's scope surfaces** (`EXAMPLE.kama.md` is at the repo
root, not `SKILL.md`/`PROVINCE.md`/`corpus/`). Under the r49 rule kaidoku is `none` because its
scope surfaces state no split; the copied table states kotoba's *ownership* but kaidoku does not
assert it. The counter must not widen kaidoku's scope set to `EXAMPLE.kama.md` — and must not
narrow it either. **The same table appears in three lanes' trees** (kama `MINT.md:42`, kotodama
`MINT.md:30`, kaidoku `EXAMPLE.kama.md:51`), so any sweep that treats "a sibling names kotoba" as
a split statement will produce three hits for one statement.

### 3.4 The arbitration-cell universe must include `kotoba` itself, or two rows false-fail

The base checker computes the arbitration cell against `expected | {SELF_LANE}`
(`verifiers/check_sibling_census.py:746`) — i.e. the 19 sibling lanes **plus kotoba**. A counter
that recomputes the cell against the 19 siblings only will false-fail exactly the two rows whose
descriptions name kotoba. Measured both ways at the frozen heads:

```
# universe WITHOUT kotoba (wrong):  kengaku  arbitration cell 'yes: chousa, kama, kotoba, kumitate, tameshi'
#                                       but the pinned description gives 'yes: chousa, kama, kumitate, tameshi'
#                                       kotodama arbitration cell 'yes: chousa, kotoba, lore'
#                                       but the pinned description gives 'yes: chousa, lore'
# universe WITH kotoba (correct):    both rows OK
```

Both rows' r49 arbitration cells are **correct as written** and survive the re-pin unchanged:
kengaku `yes: chousa, kama, kotoba, kumitate, tameshi`, kotodama `yes: chousa, kotoba, lore`. The
r49 cell for kengaku carries kotoba precisely because the checker's universe includes it. A counter
built on `fleet_lanes()` alone would report these two lanes as broken — a false alarm that would
send wave-2 falsifiers after two healthy rows.

---

## 4. The 15 lanes whose `SKILL.md`/`PROVINCE.md` moved — what actually moved

`sibling-staleness-base.tsv` says 15 of 20 differ between the r49 pin and the lane head. Recomputed
at the **frozen heads** (not the branch heads), the delta per lane:

| lane | r49 pin | `git diff --shortstat <pin> <head40> -- SKILL.md PROVINCE.md` |
|---|---|---|
| audio | `7a2fcd4f` | none |
| chousa | `6c5eb146` | 1 file changed, 187 insertions(+), 20 deletions(-) |
| game-dev-2d | `7753d49b` | none |
| game-dev-3d | `89dd182b` | none |
| kagi | `899c50b4` | none |
| kaidoku | `08c7a729` | 2 files changed, 447 insertions(+), 2 deletions(-) |
| kake | `e73d48bb` | 2 files changed, 955 insertions(+), 5 deletions(-) |
| kama | `c808ba07` | 2 files changed, 417 insertions(+), 8 deletions(-) |
| kasegi | `1fafde8f` | 2 files changed, 72 insertions(+), 1 deletion(-) |
| kengaku | `1f3b0f1e` | 2 files changed, 30 insertions(+) |
| kotodama | `35f0d49f` | 1 file changed, 85 insertions(+) |
| kumitate | `fac39171` | 2 files changed, 106 insertions(+), 12 deletions(-) |
| lore | `380ef3ab` | none |
| mado | `e33ea304` | 2 files changed, 118 insertions(+) |
| mori | `28b79d3d` | 2 files changed, 462 insertions(+), 15 deletions(-) |
| revenger | `876630db` | 1 file changed, 618 insertions(+) |
| souji | `4edb25df` | 1 file changed, 2 insertions(+), 2 deletions(-) |
| tabi | `e3cf4e0d` | 1 file changed, 89 insertions(+) |
| tameshi | `3b20f073` | 2 files changed, 108 insertions(+), 43 deletions(-) |
| tsukuroi | `22fd1642` | 2 files changed, 872 insertions(+) |

**All 20 r49 quotes still locate at the frozen heads, all on the same line as recorded.** The
r49 scope quotes are top-of-file domain lines that survived every lane's edits:

```
audio        recorded=PROVINCE.md:3  located_at_frozen=3  SAME-LINE
chousa       recorded=PROVINCE.md:3  located_at_frozen=3  SAME-LINE
game-dev-2d  recorded=PROVINCE.md:3  located_at_frozen=3  SAME-LINE
game-dev-3d  recorded=PROVINCE.md:3  located_at_frozen=3  SAME-LINE
kagi         recorded=PROVINCE.md:3  located_at_frozen=3  SAME-LINE
kaidoku      recorded=SKILL.md:3    located_at_frozen=3  SAME-LINE
kake         recorded=PROVINCE.md:3  located_at_frozen=3  SAME-LINE
kama         recorded=SKILL.md:8    located_at_frozen=8  SAME-LINE
kasegi       recorded=PROVINCE.md:3  located_at_frozen=3  SAME-LINE
kengaku      recorded=SKILL.md:3    located_at_frozen=3  SAME-LINE
kotodama     recorded=SKILL.md:8    located_at_frozen=8  SAME-LINE
kumitate     recorded=PROVINCE.md:3  located_at_frozen=3  SAME-LINE
lore         recorded=PROVINCE.md:3  located_at_frozen=3  SAME-LINE
mado         recorded=SKILL.md:8    located_at_frozen=8  SAME-LINE
mori         recorded=PROVINCE.md:3  located_at_frozen=3  SAME-LINE
revenger     recorded=PROVINCE.md:3  located_at_frozen=3  SAME-LINE
souji        recorded=PROVINCE.md:3  located_at_frozen=3  SAME-LINE
tabi         recorded=PROVINCE.md:3  located_at_frozen=3  SAME-LINE
tameshi      recorded=PROVINCE.md:3  located_at_frozen=3  SAME-LINE
tsukuroi     recorded=PROVINCE.md:3  located_at_frozen=3  SAME-LINE
exact-same-line 20, moved-within-tolerance 0, dead 0
```

**This is a finding about the plan's own shortcut-control design.** The plan's shortcut controls
include "the r49 entry copied with every commit cell bumped to the freeze heads and nothing else
(quotes die at moved lines for the changed lanes)". **Measured: the quotes do not die.** They all
survive at the same line. A counter that only re-locates quotes will score that pure carry-forward
world at **19 of 20** — and the one row it loses is *not* a quote failure. Let me be exact about
which row the carry-forward loses and why:

```
$ python3 -B verifiers/check_sibling_census.py worldB_carry.md
FAIL row 16 (census line 20) (lane revenger): SKILL.md exists at the pin but the skill cell says NONE
FAIL row 16 (census line 20) (lane revenger): names-kotoba cell 'no SKILL.md' but the pinned description gives 'no'
FAIL row 16 (census line 20) (lane revenger): arbitration cell 'no SKILL.md' but the pinned description gives 'no'
rows 20 verified 19
exit=1
```

The carry-forward loses **revenger**, because **revenger gained a `SKILL.md` after the r49 pin**:

```
$ git -C revenger-shokunin show 876630dbb4d630e016d7d8c32a19ea04c646cbae:SKILL.md >/dev/null 2>&1 && echo yes || echo NO
NO
$ git -C revenger-shokunin show 6da884c6708fa25a7af013b6fc6802492e3264fa:SKILL.md | head -1
# SKILL — revenger saved-ledger evidence craft
$ git -C revenger-shokunin show 6da884c6708fa25a7af013b6fc6802492e3264fa:SKILL.md | grep -c '^---'
0
```

revenger's new `SKILL.md` has **no YAML frontmatter at all** (0 `---` lines), so
`description_of()` returns `""` and the recomputed cells are skill=`SKILL.md`, names-kotoba=`no`,
arbitration=`no` — the r49 row said `NONE`/`no SKILL.md`/`no SKILL.md`. That is the *only* row a
mechanical carry-forward loses, and it is a **real** staleness signal, not a quote artefact.

**Consequence for the counter's control set.** The plan's carry-forward control is *measured and
reported, not asserted below 20* (plan §C2 shortcut controls) — but the reason it does not reach 20
is not the one the plan names. The honest description is: **the carry-forward loses exactly the
rows whose mechanical cells changed, which at the frozen heads is revenger alone.** The counter
should be built so that this is visible (report the failing row and the failing cell, not just the
count), and the wave-2 falsifier should be told that a carry-forward scoring 19 is *expected* and
*correct*, not a counter bug.

### The 15 moved lanes, one by one — what the movement actually was

- **revenger** — `+618` lines: a new `SKILL.md` with **no frontmatter** (§4 above). The r49 row's
  skill-file cell is now wrong; nothing else in revenger's scope surfaces names kotoba
  (`corpus/lessons/round-69.md:217` is a wave-seat reference). **Row content changes; class stays
  `none`.**
- **tsukuroi** — `+872` lines, all in `corpus/knowledge/adjacency-anchors-r19.{md,json}` (an
  index of *historical* anchors, one of which points at `kotoba:.ufo/round-22/scouts/A6.md:47`).
  Pure citation; `none` holds.
- **kake** — `+955`: `corpus/lessons/round-5-aggregator-mirror-*.md` — a **kotoba-filed,
  aggregator-owned** lesson. Per the r50 falsify correction this is *not* a sibling-stated split,
  so kake's `adjacent` rests on kotoba's own description, not on kake. Unchanged.
- **mori** — `+462`: observability logs and `corpus/knowledge/roster-truth-r12.md`. Pure citation;
  `none` holds.
- **kama** — `+417`: `corpus/knowledge/cross-lane-scope.md` **is** a sibling-stated split
  (`:29`, quoted in §2). kama's `adjacent` basis is sibling-side and is **confirmed at the frozen
  head**. This is the one lane whose `adjacent` class the moved bytes actively re-establish.
- **tameshi** — `+108 / −43`: `corpus/knowledge/fleet-kill-rate-ledger.md` — "kotoba `verifiers/*`
  — file existence" and "**U8** — sightings (kake, kama, kotoba) have unresolved gate-ness". The
  ledger names kotoba's verifiers but explicitly **does not claim** them ("file existence is O,
  their gate-ness is U until a survey admits them"). Not a claim over kotoba's core; `adjacent`
  stands on tameshi's own split (`PROVINCE.md:14-17`, present at the frozen head).
- **kumitate** — `+106 / −12`: `PROVINCE.md:28` "Prompt and skill craft → kotoba" — the split
  statement **is present at the frozen head**, one line lower than at the pin (`:27` → `:28`).
  Verified: the quote relocates within the ±2 tolerance, so the base checker passes.
- **kotodama** — `+85`: `PROVINCE.md:20` "prompt/skill craft (kotoba)" and `MINT.md:20,30` — the
  split is **confirmed**, and the frontmatter anti-trigger still names kotoba.
- **kasegi** — `+72 / −1`: aggregator-mirror lesson only.
- **kengaku** — `+30`: `PROVINCE.md:138` "prompt- and skill-craft rules" and `PROVINCE.md:30` —
  split confirmed; `SKILL.md:3` frontmatter still names kotoba.
- **chousa** — `+187 / −20`: `MINT.md:52` "Rejected recipients for this material: lore, kotoba,
  kasegi, kama, kumitate," — a **rejection list**, not a split statement. chousa's `adjacent` rests
  on kotoba's description (basis kotoba) and stays.
- **kaidoku** — `+447`: `EXAMPLE.kama.md` is a **copy of kama's MINT table** (§3.3). kaidoku
  `none` holds because that file is outside kaidoku's scope surfaces.
- **mado** — `+118`: `SKILL.md:402,943` reference `~/.agents/skills/omarchy/SKILL.md` — **not** a
  fleet lane's file, and kotoba is not named in mado's tree at all (0 hits, §2).
- **tabi** — `+89`: the `LANES` roster string (§3.1).
- **souji** — `+2 / −2`: 315 tree hits, **all** in `census/`, `results/`, `tests/vault/fixture-src-*`.
  souji's scope surfaces carry **0** hits.

**The three lanes whose `SKILL.md`/`PROVINCE.md` did *not* move** (audio, game-dev-2d, game-dev-3d
— plus kagi and lore, which also read `none` in the base receipt) are unchanged by construction,
and their rows carry `delta=none`.

---

## 5. `.ufo/` and `LOG.md` hits, reported separately

Per the r49 rule these are **not scope surfaces** ("Wave reports and run logs (`.ufo/`,
`reports/`) are not scope surfaces"). Whole-word `kotoba` hit counts at the frozen heads, excluded
from every classification judgement above:

| lane | `.ufo/` | `LOG.md` | total |
|---|---|---|---|
| audio | 0 | 0 | 0 |
| chousa | 153 | 0 | 153 |
| game-dev-2d | 0 | 0 | 0 |
| game-dev-3d | 0 | 0 | 0 |
| kagi | 379 | 6 | 385 |
| kaidoku | 87 | 0 | 87 |
| kake | 174 | 2 | 176 |
| kama | 295 | 0 | 295 |
| kasegi | 250 | 2 | 252 |
| kengaku | 1044 | 3 | 1047 |
| kotodama | 111 | 0 | 111 |
| kumitate | 509 | 1 | 510 |
| lore | 16 | 0 | 16 |
| mado | 137 | 0 | 137 |
| mori | 338 | 0 | 338 |
| revenger | 39 | 1 | 40 |
| souji | 116 | 0 | 116 |
| tabi | 107 | 0 | 107 |
| tameshi | 264 | 0 | 264 |
| tsukuroi | 64 | 0 | 64 |

(Counts are **matching lines**, summed per file with `git grep -c … | awk -F: '{s+=$NF}'`.
kama is the only lane where the two grep methods disagree, because
`.ufo/waves/round-34/w1/out/ConnSiblingScope/seat.log` is a **binary** file: `grep -n` prints one
"Binary file … matches" line where `grep -c` counts 3 matching lines. Reconciled lane by lane —
`grep -n` lines vs `grep -c` line-count — kama is the sole lane with a non-zero difference (306 vs
308, diff 2) and all 19 other lanes agree exactly. The tree-wide total is therefore **4 749**
matching lines, of which **198** are scope-surface hits.)

**Why this matters for C2.** 4 098 of the 4 749 fleet-wide hits live in `.ufo/`+`LOG.md`, and the
r49 rule excludes them from scope surfaces — but the *counter* the plan describes recomputes
"skill-file, names-kotoba and arbitration cells … from the pinned `SKILL.md`", i.e. from the
description only. A counter that swept the whole tree for `kotoba` would find 4 749 hits and would
have to re-derive the exclusion itself; one that sweeps the scope surfaces finds **198**, of which
**3 are hyphen false positives** (§1), leaving **195** real tokens. **The 198-vs-195-vs-4 749 gap is
the counter's real measurement surface: a factor of 24 smaller than the tree, and 3 of the 198 are
not lane references at all.**

---

## 6. The one non-obvious move this seat recommends

**Do not let the C2 counter implement the plan's predicate (e) as written.** Narrow it to the base
checker's surface — *the frontmatter description or `PROVINCE.md`* — and have the counter report
**which rows it recomputed and which it carried**, not only the count.

Why this is the right move rather than a nit:

1. It is the difference between a C2 counter that can reach 20 of 20 and one that caps at 19
   (§3.1, tabi). The cap is caused by the predicate's own wording, not by any sibling having
   moved — so the "staleness" the claim measures would be an artefact of the measurement.
2. It keeps the C2 counter on the **freshness** axis and off the **classification** axis, which
   the plan explicitly bounds ("the counter does **not** measure whether `adjacent`/`contested`/
   `none` is the right classification"). Predicate (e) as written *is* a classification rule: it
   forbids a `none` row on a criterion the classification rule does not use. Implementing it would
   silently move the C2 counter onto the adjacency axis and make C2 a partial re-classification
   claim — an axis-crossing that would harm the claim's own separability.
3. It costs nothing on the axis C2 is actually for: the counter still re-pins the commit cell, still
   recomputes the delta, still recomputes the three mechanical cells at the frozen head, and still
   re-locates the quote. Every one of the 20 quotes survives (§4), so the quote re-location arm
   carries no weight at this freeze and the *cell recomputation* is the arm that does the work.
   Reporting which rows were recomputed makes the counter's own evidence legible to the wave-2
   falsifiers instead of hiding a 19-vs-20 artefact behind a number.

**Second-order effects traced:** runtime (the counter must `git show` at the pinned commit, never
read a checkout — **four** lanes are already past the freeze: kake +1, kasegi +2, kotodama +2,
souji +2 commits at sweep time, §3.1); contract (the base checker's
sha256 is pinned and unchanged at HEAD, §3.2, so the counter may import it but must not modify it);
substrate (the `delta` cell cannot live inside the 9-column census table, §3.2 — it needs a
separate table or a post-check column); verification (the carry-forward control is expected to
score **19**, losing revenger on the skill-file cell, not on a quote, §4 — the wave-2 falsifier
must be told this in advance or it will read 19 as a counter bug).

**Not proposed, and why:** no lane is reclassified (§2 — no hit supports one); no sibling is
contacted (the lane never edits a sibling, and no sibling file was written by this seat); the
r49 census and `PROVINCE.md` were not modified (read-only attack seat).

---

## 7. Unobserved / bounds

- **Unobserved:** whether any sibling would *agree* with kotoba's reading of a split. The r49
  classification is kotoba's own rule; the wave-2 seats own that judgement (plan §C2 bound). This
  seat derived the classification-rule outcome from committed bytes only.
- **Unobserved:** whether the four lane heads that moved past the freeze (kake +1, kasegi +2,
  kotodama +2, souji +2) changed their split statements after the freeze. The freeze is the
  measurement surface; the plan already records that "siblings keep moving after the freeze".
  The four lanes' *current* `SKILL.md`/`PROVINCE.md` bytes were not swept for this seat's table.
- **Not run:** no lane gate was executed (this seat is a read-only attacker and the plan assigns
  gate runs to the L1 and the executor seats); no `jj` command was run; no sibling repo was
  written to; no file under the lane's tracked tree was modified by this seat.
- **Tooling:** no tool was installed or upgraded by this seat — the work needed only `git`,
  `python3` (stdlib only) and `grep`, all already present.
- **Scratch:** a scratch directory `/tmp/k74w1-ConnSiblingSplitsR74.*` was used for the probe
  scripts and the world A–D fixtures, and was removed before this report was written. The only
  files this seat wrote are this report and the deliverable
  `.ufo/waves/round-74/w1/build/ConnSiblingSplitsR74/kotoba-hits-frozen-heads.tsv`.

## 8. Report pointer

`.ufo/waves/round-74/w1/ConnSiblingSplitsR74.md`
