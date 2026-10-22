# kotoba round 49 plan (attempt 1; hyaku session 2026-10-22)

Lane base: branch `master` at `a5adc146a2995dcc5a95a6d8db6e5674f75191ac` (round 48 admitted,
MANIFEST rounds[442]). No earlier attempt of round 49 exists (`.ufo/watchdog.log` has no
`lane-dead-no-report kotoba round=49` line). No private trees, prereg packets or approval windows.

Drift guard (session note): rounds 47 and 48 both claimed freshness on the SKILL.md frontmatter and
instrument surface. This round works two other frontier areas on other axes and does not edit the
SKILL.md frontmatter.

Lowest-scoring non-retired axes at base: freshness 8 and adjacency 8.0 (`SCORECARD.md` axes table).
The stagnation nudge does not apply (owned axis depth is 9, below the 10.0 saturation line). C1 works
adjacency, one of the two lowest.

## Claims (two, causally separable, distinct axes)

### C1 — adjacency (lowest, 8.0): fleet sibling-overlap census (frontier area: sibling arbitration)

New knowledge entry `corpus/knowledge/sibling-overlap-census-round49.md`: for each of the 20 sibling
lane repos under `/home/vgpnk/Projects/shokunin/*-shokunin`, the pinned commit, the skill file(s), a
located quote of the sibling's own scope, and a classification against kotoba's province
(`contested`, `adjacent` or `none`, the last with its sweep), plus whether the sibling's description
carries an arbitration clause. Sourced on primary docs opened this round on how a harness picks one
skill among overlapping descriptions (new `SOURCES.md` rows). `PROVINCE.md` § Adjacent is rewritten
from the census so it names every sibling lane with its classification.

- Before (Q19, measured 2026-10-22 at `a5adc146`): sibling lanes named in `PROVINCE.md` § Adjacent
  = **10** of 20.
- After (declared): **20**.
- Command: `awk '/^## Adjacent/,0' PROVINCE.md | grep -oE '\b(audio|chousa|game-dev-2d|game-dev-3d|kagi|kaidoku|kake|kama|kasegi|kengaku|kotodama|kumitate|lore|mado|mori|revenger|souji|tabi|tameshi|tsukuroi)\b' | sort -u | wc -l`
- Content guard (routed defect R2, counter able to fail on empty content): the entry's `recheck:`
  is a committed script that re-reads every census quote at its pinned commit and exits non-zero
  when a quote is missing; it is shown failing on a mutated quote.

**Re-sizing before any landing (09:50Z, critic `CriticC1Sizing`, `.ufo/waves/round-49/build/CriticC1Sizing.md`):**
the name count above is satisfied by a bare list of 20 names, and its awk range runs to the end of
the file. That repeats routed defect R2. The declared after-value is replaced, before anything
lands, by a row count that needs a classification and a pinned commit per sibling inside the
section only. The name count stays a secondary observable.

- Before (Q19, `a5adc146`): **0** classified, pinned rows in `PROVINCE.md` § Adjacent.
- After (declared): **20**.
- Command: `awk '/^## Adjacent/{f=1;next} /^## /{f=0} f' PROVINCE.md | grep -cE '^\| (audio|chousa|game-dev-2d|game-dev-3d|kagi|kaidoku|kake|kama|kasegi|kengaku|kotodama|kumitate|lore|mado|mori|revenger|souji|tabi|tameshi|tsukuroi) \| (contested|adjacent|none) \| [0-9a-f]{40} \|'`
- Content guard: `verifiers/check_sibling_census.py --province PROVINCE.md` joins those rows to the
  entry (same lanes, classifications and commits) and re-reads every quote at its pinned commit;
  a heading line is refused as a scope quote; fewer rows than the sibling set fail.

### C2 — operability (8.5): dispatch-prompt checklist boxes executed (frontier area: executed checklist coverage)

New instrument `verifiers/verify_dispatch_prompts.py` executes two dispatch-prompt checklist boxes
over a prompts directory: `dispatch.04` (the report path is literal and its file name is the lane
id) and `dispatch.08` (the round token is identical across file name, role line and report path,
and is at most the lane's state round). It has a `--self-test` with must-fail fixtures, and the two
boxes move from `unexecuted:` to `delegated:verifiers/verify_dispatch_prompts.py` in
`verifiers/checklist-baseline.json`. The capability runs over the fleet's `.ufo/prompts/` this round
and enters the SCORECARD capabilities table with its output.

- Before (Q19, measured at `a5adc146`): dispatch-prompt boxes with an `executed:` or `delegated:`
  disposition = **0** of 9.
- After (declared): **2**.
- Command: `jq '[.boxes[]|select((.box_id|startswith("dispatch.")) and (.disposition|test("^(executed|delegated):")))]|length' verifiers/checklist-baseline.json`

**Re-sizing before any landing (10:00Z, critic `CriticC2Sizing`, `.ufo/waves/round-49/build/CriticC2Sizing.md`):**
the disposition count reads 2 when both boxes are mapped to an unrelated instrument or to a
ten-byte shell stub, and the map check passes. It measures map entries, not execution. The declared
after-value is replaced, before anything lands, by the instrument's box proof over committed
fixtures; the disposition count stays a labelled supporting number ("map entries").

- Before (Q19, `a5adc146`): **0** (the instrument and fixtures do not exist; nothing proves a
  dispatch box).
- After (declared): `boxes proven 2`.
- Command: `python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json`
  — prints `boxes proven N` and exits 0 only when N is 2. A box counts only when the map delegates
  it to this instrument, its text hash equals the instrument's pinned hash, every control fixture
  passes and every per-conjunct mutant fixture fails on its named conjunct.
- The full `dispatch.08` box is executed, state clause included; its live failures are findings.

## Routed defects from the round-48 spot-check (fix or explain)

- R1: fix in `verifiers/verify_harness_independent.py` (configured roots keyed by frontmatter name,
  as S016 states), with a must-fail arm; not a claim, reported as a routed-defect repair.
- R2: answered by this round's counters (content guard above) and lesson M29 with criterion Q25.
- R3: appended correction under `SCORECARD.md` `Next: round 49`.
- R4: append-only count-provenance section in the round-48 entry; this round's lesson `## Gate`
  carries an explicit admit line.
- R5: explained and carried (prospective oracle amendment; built-in marker definition).

## Frontier step

Census start `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`:
exit 0, `kotoba ok`, three W04 warnings (S018, S019, S021). New rows only for sources opened this
round; mined mistake M29 (content-blind counter) into `corpus/lessons/round-49.md`.

## Shape

Default two v1 waves: wave 1 build (36 seats), wave 2 falsify (32–64 seats) over wave 1's output.
The L1 holds the planner seat; the bounded planning data-walk rides scout `PlanDataWalk`.
