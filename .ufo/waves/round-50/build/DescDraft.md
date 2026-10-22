# DescDraft — C1 description draft (kotoba)

Seat: KotobaR50.DescDraft (build wave, round 50). Lane base `f30464660c675d1c1e2851a3bf0366a3aaffe5a8`.
Scratch: `/fast/scratch/hyaku/kotoba-r50/build/DescDraft/` (clone `kotoba-shokunin/`, `base/` at the base
commit, `out/` gate captures, `patch.diff`). Lane file touched: `SKILL.md` (frontmatter only) plus this
report. No tool installed. No jj/git write command run in the lane, the fleet repo or a sibling lane.

## Result

**The draft passes the landed guard at 9 of 9 and 1018 parsed characters.** The L1 landed a different
description at `956ee167` while this seat was drafting; the draft below is an independent variant that
satisfies the same steer and passes the same instrument. **Recommendation: keep the landed
description** (see the comparison paragraph); the draft is delivered as a verified alternative, not as a
request to replace the landed text.

## The draft (exact YAML block, between the `---` lines)

```yaml
---
name: kotoba-shokunin
description: >
  Prompt & skill craft — audits, writes, and rewrites SKILL.md / AGENTS.md /
  dispatch prompts / system prompts for trigger fidelity and decision density.
  Triggers: "skill file", "SKILL.md", "frontmatter description", "trigger
  words", "prompt craft", "write a skill", "audit this skill", "skill quality".
  Anti-triggers: general prompt engineering for model outputs (not skill files),
  runtime code changes, and domain content inside a skill's reference/ tree.
  Sibling boundary: each lane owns its own SKILL.md content; this skill audits
  and reports; fixes route to the owning lane. chousa owns source research; kagi
  owns secrets and vault ops; kake owns web publishing; kama owns endpoint
  health; kasegi owns bounty research; kengaku owns prompt-format effects;
  kotodama owns fictional-world words, routes prompt/skill craft to kotoba,
  names collide; kumitate owns orchestration and tooling; tameshi owns the
  fixture and mutation method. Note: shokunin files are not in an omp skill
  discovery root, so no router sees them.
---
```

**Character count.** `python3 -c "import yaml; ..."` on the block above: parsed `description` value
**1019 characters** (the folded scalar's trailing newline included), **1018** with `.strip()`. The
guard's own reader (`description_of`, which collapses whitespace and does not take the newline) reports
`skill description length 1018 of 1024`. Both are ≤ the 1024 cap (S018 `specification.md:101`).

## Constraint check (each measured, not asserted)

| Requirement | Measure | Result |
|---|---|---|
| 9 non-`none` census lanes named as whole tokens | plan counter on the clone (below) | **9** |
| Each lane bound to an ownership/routing word in its own clause | landed guard `G1` | 9 of 9 |
| Parsed length ≤ 1024 | `yaml.safe_load` → `len()` | 1019 (1018 stripped) |
| First 99 characters unchanged (omp truncator keep) | `draft[:99] == base[:99]` | True |
| Sibling clause before the discovery-root note | `d.index('Sibling boundary:') < d.index('Note:')` | True |
| Existing triggers kept | `"Triggers:"` + all 8 quoted spans | kept verbatim |
| Existing anti-triggers kept | `"Anti-triggers:"` clause | kept verbatim |
| Discovery-root note kept | `"not in an omp skill discovery root"` | kept |
| Third person | no `you` / `your` / `yours` in the value | True |
| `trigger.no_xml_tag` | checklist gate | PASS |

Split wording per lane follows `corpus/knowledge/sibling-overlap-census-round49.md` (census scope
quotes) and `PROVINCE.md` § Adjacent: chousa = source research (deep-research method); kagi = secrets
and vault ops; kake = web publishing (web properties and publishing); kama = endpoint health
(endpoint verification; only the admitted side, per the steer); kasegi = bounty research (bounty and
security research); kengaku = prompt-format effects (measured effects of prompt format; only the
admitted side); kotodama = fictional-world words + routes prompt/skill craft to kotoba + the name
collision; kumitate = orchestration and tooling; tameshi = the fixture and mutation method. The
kotodama clause states the routing ("routes prompt/skill craft to kotoba") and the collision
("names collide"), per the steer.

## Gates — before and after (clone, exit codes verbatim)

Baseline = the landed tree at `956ee167` in the scratch clone (`before2`); after = the same clone with
this draft applied to `SKILL.md` (`after`). Both captured by `run-checks.sh <label> <clone>`.

| Command | Before (`956ee167`) | After (draft applied) |
|---|---|---|
| `python3 -B verifiers/verify_skill_checklist.py --json` | exit **1** — 9 PASS / 2 FAIL | exit **1** — 9 PASS / 2 FAIL |
| `python3 -B verifiers/verify_skill_checklist.py --self-test` | exit **0** — `0 failure(s) over 1851 assertions` | exit **0** — `0 failure(s) over 1851 assertions` |
| `python3 -B verifiers/verify_corpus_integrity.py --json` | exit **1** — 8 PASS / 1 DRIFT (`corpus.index.tracked_files` 67 vs 66) | exit **1** — same |
| `python3 -B verifiers/verify_corpus_independent.py` | exit **1** — 1 DRIFT (`corpus.pointers.report_dead` 2) | exit **1** — same |
| `python3 -B verifiers/verify_harness_claims.py` | exit **1** — 21/28 pass, 7 DRIFT (omp substrate) | exit **1** — identical |

**Checks that change: exactly one.** A line-by-line diff of all five stdout/stderr captures shows a
single changed line — `trigger.frontmatter_parses` detail: `description 1008 chars` → `description
1018 chars`. Every other check, count, DRIFT and exit code is byte-identical before and after.

The two `verify_skill_checklist.py` FAILs (`trigger.citation_resolves` at line 529,
`governance.citation_resolves` on `LOG.md:177`) are **clone-location artifacts**, not draft defects:
they are `../.ufo/reports/...` paths that resolve from the lane root but not from
`/fast/scratch/...`. The corpus-integrity and harness DRIFTs are pre-existing at the landed tree
(untracked corpus file; omp substrate drift) and are unchanged by the edit.

**Guard on the draft:** `python3 -B verifiers/check_sibling_census.py
corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md` → exit **0**,
`rows 20 verified 20`, `province rows 20 matched 20`, `skill description names 9 of 9 non-none lanes`,
`skill description length 1018 of 1024`. Guard self-test: `0 failure(s) over 68 assertions`, exit 0.

**Plan counter on the clone** (`plans/round-50.md` pipeline, verbatim):
`awk 'NR==1&&/^---$/{f=1;next} f&&/^---$/{exit} f' SKILL.md | grep -oiwE
'chousa|kagi|kake|kama|kasegi|kengaku|kotodama|kumitate|tameshi' | sort -u | wc -l` → **9**. With the
critic's F1 case-fold (`| tr '[:upper:]' '[:lower:]' |`) → **9** as well.

**Patch deliverable:** `/fast/scratch/hyaku/kotoba-r50/build/DescDraft/patch.diff` — unified diff of
`SKILL.md` against `f30464660c675d1c1e2851a3bf0366a3aaffe5a8` (10 insertions, 8 deletions; frontmatter
only, no body change).

## Comparison with the landed description (`956ee167`)

The landed text parses to **1009** characters (1008 by the guard's reader) and also passes the guard at
9 of 9. It differs from this draft in three ways. (1) Structure: the landed text keeps the base
sentence "kagi, kake, kasegi, kengaku and kumitate own their own SKILL.md content" as one shared clause
and then adds per-lane clauses only for chousa, kama, kengaku and tameshi, with kotodama written as a
`NOT kotodama-shokunin:` refusal. This draft gives every one of the nine lanes its own ownership clause
and states the kotodama routing positively ("routes prompt/skill craft to kotoba") plus the collision,
which the steer asked for; the landed text states the collision but not the routing, and its
"NOT kotodama-shokunin" form carries the `NOT` marker the guard accepts. (2) Length: the landed text
is 11 characters shorter, which buys margin under the 1024 cap — that margin is the main argument for
keeping it, since my own draft had to compress the note to "no router sees them" to fit. (3) Coverage of
the `kasegi` split: the landed text does not name kasegi's split at all (kasegi appears only inside the
shared five-lane clause), so kasegi's clause binding rests on "own their own SKILL.md content" rather
than on its bounty/security-research ground; this draft gives kasegi "owns bounty research" explicitly.
Both texts are third-person, keep the trigger and anti-trigger spans verbatim, keep the discovery-root
note, keep the first 99 characters unchanged, and put the sibling clause before the note. Given that
the landed text is already integrated and passes the same instrument with more headroom, this seat
recommends keeping it and records the draft as the verified alternative.

## Finding (not mine to fix — reported, not edited)

The landed tree's census append states the line pin wrong. `corpus/knowledge/sibling-overlap-census-round49.md:243-244`
says "the round-50 description moved that note to lines 15-17", but in the landed `SKILL.md` the note
("Note:" through "not router-visible.") occupies **lines 16-18** — `grep -n "Note:\|omp skill discovery
roots\|omp router" SKILL.md` prints 16, 17, 18. The pin is off by one line; the census entry is
append-only and owned by another seat, so this seat did not edit it. The same file's line 39 citation
`../SKILL.md:12-15` refers to the base description and is qualified by the line-243 correction, so it
is not itself wrong.

## Out of scope / not done

- The census append (line pin), `PROVINCE.md` § Adjacent boundary text and `SCORECARD.md` are other
  seats' files; not edited here.
- No new `corpus/SOURCES.md` row was opened by this seat (S018 already carries the 1024 cap; S022
  re-opened by seat `SrcReopenS022` confirms Claude Code has no field cap, only a 1,536 listing cap).
- The description carries no source ids: they cost characters against the 1024 cap and do nothing for
  triggering.
- No trigger-precision claim is made: kake and kasegi are named for the adjacency axis, and per the
  round-49 falsify finding their own descriptions carry none of kotoba's trigger words.
