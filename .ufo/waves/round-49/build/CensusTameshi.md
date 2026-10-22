ROW | tameshi | master (detached HEAD) | 3b20f073c7305a582562cd323982991464c324f3 | SKILL.md | adjacent | no | yes | PROVINCE.md:3-5 | "Domain: verification-fixture craft — the reusable method of honest checks: hermetic suites, mutation testing, fail-closed arms, verdict-line discipline, no-permissiveness audits, before/after proof."

## Findings

1. **Pin.** `tameshi-shokunin` HEAD is detached at the master tip: `rev-parse master`
   and `rev-parse HEAD` both return `3b20f073c7305a582562cd323982991464c324f3`;
   `symbolic-ref -q HEAD` exits 1 (detached), `git branch --contains` lists `master`
   and `(no branch)`. Commit date 2026-10-22 06:36:44 -0300, subject "round-25:
   seventeen traced L1 source re-anchors appended to the cold-read ledger".
2. **Skill file.** Exactly one SKILL.md exists at the pin, top-level `SKILL.md`
   (2084 lines, 159719 bytes, sha256 `7d3a9e29…be4a`). Its frontmatter is four
   lines: `name: tameshi-shokunin` (:2) and one quoted `description:` (:3).
3. **Description asks.** It names **no** lane's territory as its own; it names kotoba
   zero times. It **does** carry a concrete sibling arbitration clause: "Anti-trigger:
   product behavior or endpoint health; route those to the product lane or **kama**."
   Named sibling: kama (plus the generic "product lane"). It also carries `Rank: shonen`.
4. **PROVINCE.md** (105 lines, sha256 `5d56df9b…f939`). Domain (:3-5) is
   verification-fixture craft; Owns (:7-12) "the method, documented from the fleet's
   existing gates as primary surfaces"; Refuses (:14-18) "product domains — every
   lane's gate remains its own … Never edits a sibling's gate code (read-only probes;
   recommendations travel in round reports)". § Adjacent (:44-47) names sibling gate
   code, kagi, kama, the UI lanes and the game lanes — **kotoba is not named** (0 hits).
5. **Classification: adjacent.** The shared boundary is instruments-versus-craft:
   kotoba owns the SKILL.md / prompt / AGENTS.md checklist instruments and their
   disposition map; tameshi owns the fixture-and-mutation method that can be pointed
   at gates, and it explicitly leaves kotoba's instrument to kotoba. tameshi's own
   committed fleet overlap study, row O-08 (`.ufo/waves/round-16/w1/Overlap1.md:106`),
   classes kotoba **complementary** and its finding F4 (:136) states the boundary in
   tameshi's words: "kotoba owns the SKILL-checklist instrument; C2 must not conflate
   it." Its summary (:123) records **0 ownership contests** across 23 lanes, the single
   claim contest being O-07 kumitate. The kill-rate ledger's boundary block treats
   kotoba `verifiers/*` as a **sighting, not a queued gate** — "file existence is O,
   their gate-ness is U" (`corpus/knowledge/fleet-kill-rate-ledger.md:127-128`), and U8
   (:233-234) repeats it.
6. **Not contested.** No tameshi governance text claims to write or audit another
   lane's SKILL.md, prompts or AGENTS.md. The overlap sweep's 10 matches over the five
   top-level governance files are: its own description (:3); four ledger "trigger" hits
   that are the re-pin triggers T1–T3, not skill-selection triggers
   (:1015, :1069, :1252, :1290); three self-anchoring references to its own bytes
   (:1717, :1719, :1720, plus errata row :1738); and `README.md:12` describing its own
   SKILL.md. `AGENTS.md`, `MINT.md` and `PROVINCE.md` contribute 0 matches.
7. **Adjacency is mutual but asymmetric in placement.** kotoba's PROVINCE.md:32 (at
   lane base `a5adc146`) already says "tameshi — verification-fixture craft and mutation
   testing." tameshi records the same relation only in its wave report and kill-rate
   ledger, not in PROVINCE.md § Adjacent.
8. **Negative claim and its sweep (Q14).** kotoba appears nowhere in tameshi's
   governance files; it appears only in retained evidence and two corpus knowledge
   entries. Sweeps below carry their commands and date.

## Evidence

All commands run 2026-10-22 (UTC) from `/home/vgpnk/Projects/shokunin/tameshi-shokunin`,
read-only via `git show` / `git grep` at the pinned commit; no lane write, no jj.

```
git -C /home/vgpnk/Projects/shokunin/tameshi-shokunin rev-parse master
  -> 3b20f073c7305a582562cd323982991464c324f3                 exit 0
git -C ... symbolic-ref -q HEAD                                exit 1 (detached)
git -C ... rev-parse HEAD                                      -> same 40-hex, exit 0
git -C ... branch --contains <40>  -> "* (no branch)", "master"  exit 0
git -C ... show -s --format='%H %ci %s' <40>
  -> 3b20f073... 2026-10-22 06:36:44 -0300 round-25: seventeen traced ...  exit 0
git ls-tree --name-only <40>   -> .gitignore .ufo AGENTS.md LOG.md MINT.md PROVINCE.md
  README.md SCORECARD.md SHONEN.md SKILL.md considerthese corpus plans reports tools  exit 0
git ls-tree -r --name-only <40> | grep -E '^(skills?/[^/]+/)?SKILL\.md$'
  -> SKILL.md (one line)                                       exit 0
```

Pins (sha256 of the blob at the pin, `git show <40>:<path> | sha256sum`):

| Path | Lines | Bytes | sha256 |
|---|---|---|---|
| SKILL.md | 2084 | 159719 | `7d3a9e2907fcb9fc1cb2ce6dee95f38e3c28cc07c974bfadc5feab022f07be4a` |
| PROVINCE.md | 105 | 5618 | `5d56df9bb86f1a27aeb095f2b169fe413770f9e0d7ad4d42fc7ef2abd1ecf939` |

Counts, each `<number> — <command> <date>` (Q13):

- 0 — `git show 3b20f073:SKILL.md | grep -c kotoba` (exit 1) 2026-10-22.
- 0 — `git show 3b20f073:PROVINCE.md | grep -c kotoba` (exit 1) 2026-10-22.
- 0 — `git show 3b20f073:README.md | grep -c kotoba` (exit 1) 2026-10-22.
- 0 each — same `grep -c kotoba` over `AGENTS.md`, `MINT.md`, `LOG.md`, `SCORECARD.md`,
  `SHONEN.md` 2026-10-22.
- 10 — overlap sweep line count 2026-10-22:

  ```
  for f in SKILL.md PROVINCE.md README.md AGENTS.md MINT.md; do git show 3b20f073:$f; done \
    | grep -Eic 'SKILL\.md|prompt|AGENTS\.md|frontmatter|trigger|description|kotoba'   -> 10
  per file: SKILL.md 9, README.md 1, PROVINCE.md 0, AGENTS.md 0, MINT.md 0
  ```
- 75 files / 130 lines — `git grep -Iil kotoba 3b20f073 | wc -l` and
  `git grep -Ii kotoba 3b20f073 | wc -l` 2026-10-22; every hit is under `.ufo/`
  evidence or waves except `corpus/knowledge/fleet-kill-rate-ledger.md` (2) and
  `corpus/knowledge/fleet-suite-census.md` (1), checked with
  `git grep -Iic kotoba 3b20f073 -- corpus tools` 2026-10-22.
- 1 — `grep -n 'tameshi' /home/vgpnk/Projects/shokunin/kotoba-shokunin/PROVINCE.md | head -5`
  → `32:- tameshi — verification-fixture craft and mutation testing.` 2026-10-22.

Quotes, located at the pin (bold emphasis markers present in the file are stripped
from the quoted text; the words are verbatim):

- Scope, `PROVINCE.md:3-5`: "Domain: verification-fixture craft — the reusable method
  of honest checks: hermetic suites, mutation testing, fail-closed arms, verdict-line
  discipline, no-permissiveness audits, before/after proof." (21 words)
- Overlap, `.ufo/waves/round-16/w1/Overlap1.md:136`: "F4 — kotoba owns the
  SKILL-checklist instrument; C2 must not conflate it." (12 words; the row it explains
  is O-08 at `:106`, class "complementary"; summary "0 ownership contests" at `:123`.)

## Inference and unknowns

- [INFERENCE] The relation is a true shared boundary rather than no-overlap because
  both lanes ship executable instruments over claim/checklist text: kotoba's
  `verifiers/verify_skill_checklist.py` (disposition map `executed:|delegated:|unexecuted:`)
  and tameshi's mutation/coverage gates measure the same class of object with different
  methods. tameshi's ledger calls kotoba's verifiers' gate-ness "U" (U8), which is an
  explicit deferral, not a claim.
- Unknown, unresolvable read-only: whether tameshi will admit kotoba `verifiers/*` into
  a future sweep; its ledger leaves it unqueued at this pin.
- Line drift to record: tameshi's O-08 cites kotoba's adjacency at `PROVINCE.md:30`;
  at kotoba base `a5adc146` the sentence is at `:32`. Same sentence, no semantic change.
- No tools installed or upgraded this session; no network fetch.
