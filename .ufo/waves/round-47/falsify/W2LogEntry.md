verdict: PARTIAL — the round-47 LOG entry's seat counts, role mix, and before→after instrument numbers reproduce exactly, but three of its factual claims do not hold at 7ad7fad: the governance "evaluated 804" figure (actually 848), the "9 ids re-instituted" census gloss (the ledger says 7 resurrected), and the C3 "answers the sentinel's blocker" attribution (the sentinel named 7 wave-2 probe groups; the landed in-source registry implements 1 of them, and the file named is a *critic* design, not the sentinel's blocker answer).

Target: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/LOG.md` round-47 entry, lines 2317–2326 at `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`.
Method: re-ran every counting command named in the entry in a canonical-layout clone at `7ad7fad`; re-derived the seat/role counts from the tracked dispatch artifacts; mutation-tested the C3 errata gate; cross-checked every "before" value against `.ufo/waves/round-47/before/SUMMARY.md` and the wave-1 reports it cites.
Scratch clone (all measurements): `/fast/scratch/kotoba-r47/w2/W2LogEntry/kotoba-shokunin` (detached at `7ad7fad`, `git status --porcelain` empty at every checkpoint).
Lane repo: read-only. `git status --porcelain` in `/home/vgpnk/Projects/shokunin/kotoba-shokunin` shows only untracked `.ufo/waves/round-47/{after,falsify*}`. No Git index/ref/jj mutation; no `git add/commit/stash/checkout/switch/reset/pull/push` in the lane repo.
Tools installed/updated: none. No pacman transaction. No `opencode`/`~/.local/bin/opencode` execution; the frozen snapshot `/fast/scratch/kotoba-r47/shared/` was read only (its `SHA256SUMS` was re-verified by `sha256sum -c` semantics only via the pinned values already in `verifiers/baseline.json`).

---

## F1 — HIGH — `LOG.md:2323` "governance evaluated 804" is FALSE at the landed tree; the real figure is 848

**Claim under test** (`LOG.md:2323`, verbatim):
> `Checklist `--json` exit 1, 9 PASS / 1 FAIL → exit 0, 11/11 (governance evaluated 804, 1 recorded absence excused)`

**Repro (exit codes + key output).** In the canonical-layout clone at `7ad7fad`:

```
$ cd /fast/scratch/kotoba-r47/w2/W2LogEntry/kotoba-shokunin
$ PYTHONDONTWRITEBYTECODE=1 python3 -B verifiers/verify_skill_checklist.py \
    --repo "$PWD" --skill "$PWD/SKILL.md" --json
exit=0
  PASS governance.citation_resolves | evaluated 848 | 848 governance citation
  token(s) resolve across 2 files; 9 quoted meta-finding(s), 3 schematic token(s)
  excluded, 1 recorded absence(s) excused
```

The round's **own** after-battery artifact says the same thing, so the entry contradicts a file committed in the same wave:

```
$ python3 -c "import json;d=json.load(open('.ufo/waves/round-47/after/verify_skill_checklist.json'));\
  print([ (c['id'],c['evaluated'],c['detail']) for c in d['checks'] if c['id']=='governance.citation_resolves'])"
[('governance.citation_resolves', 848, '848 governance citation token(s) resolve across 2 files; 9 quoted meta-finding(s), 3 schematic token(s) excluded, 1 recorded absence(s) excused')]
```

**Root cause — 804 is a pre-landing-tree number.** `804` reproduces only against the **BASE** `LOG.md` + BASE `SCORECARD.md`; every other pairing gives a different number:

| LOG.md | SCORECARD.md | `governance.citation_resolves` evaluated |
|---|---|---|
| BASE `c61a973` | BASE `c61a973` | **804** ← the figure the entry quotes |
| BASE `c61a973` | landing `7ad7fad` | 815 |
| landing `7ad7fad` | BASE `c61a973` | 837 |
| landing `7ad7fad` | landing `7ad7fad` | **848** ← the actual landed value |

The landing itself adds the 44 missing subjects: the round-47 entry appends 11 lines to `LOG.md` (2317–2326) and the round-47 `SCORECARD.md` rows add more, each new path token becoming a governance subject. So the entry reports a number that **its own text invalidated**. This is the same class of defect the round itself wrote a lesson about: `corpus/lessons/round-47.md:19` (M20) — *"Stale planned premise (before-values copied, not re-measured)"* — and `corpus/QUALITY.md:30` (Q19) — *"a value copied from an earlier record is struck, never scored against."* The `804` figure was copied from `C3CriticDesign.md`'s probe table (`.ufo/waves/round-47/build/C3CriticDesign.md:97,119`, "PASS, 804") and re-published as a landing measurement.

**Counterexample for a reader who re-runs it.** Any reviewer following the entry's own pointer (`.ufo/waves/round-47/build/C3CriticDesign.md`) re-runs the checklist and gets 848, not 804, and cannot reproduce the quoted number from the landed tree. The wave's after-battery (`.ufo/waves/round-47/after/verify_skill_checklist.json`, mtime `2026-10-21 13:46:43`, i.e. **30 s after** the landing commit at `13:46:13`) already carried 848.

**Why this matters for calibration.** The C3 claim is "the governance gate's one false red is excused by a pinned, fail-closed erratum". The mechanism does hold (see F5). But the receipt published for it states a governance-subject count that is wrong by 44 at the tree it describes, in a round whose own lesson and quality criterion exist specifically to forbid copying a pre-landing count. The `SCORECARD.md:33` row says the same thing more carefully — it says "exit 1, 9/1 → exit 0, 11/11" and never quotes 804, so the number propagated into `LOG.md` alone.

**Does the wrong number falsify C3?** No. The design's own falsification criterion (`C3CriticDesign.md:119`) is *"C3 is falsified if evaluated is below 804"* — 848 ≥ 804, so the criterion is not tripped and the erratum still excuses exactly one subject with one recorded absence. The defect is a false receipt, not a false gate. That distinction is the whole of the finding.

---

## F2 — MEDIUM — `LOG.md:2321` "9 ids re-instituted" is not what the census ledger says

**Claim under test** (`LOG.md:2321`):
> `9 ids re-instituted, 3 v2.0.26 ids retired, `config/instructions` re-verdicted governed`

**What the census actually records.** `corpus/knowledge/instruction-surface-census-round13.md:310-321` — the "Class ledger (round 47; every id the census ever declared for opencode)" — has **12** rows whose round-47 verdict column reads:

| verdict | count | ids |
|---|---|---|
| `retired` | 3 | `project/AGENTS.md`, `read-hook/AGENTS.md`, `api-entries/instructions` |
| `resurrected` | 7 | `instructions/{AGENTS,CLAUDE,CONTEXT}.md`, `claude-home/CLAUDE.md`, `config/instructions-remote`, `read-hook/instructions`, `instruction-context/AGENTS.md` |
| `retained, re-anchored` | 1 | `config/AGENTS.md` |
| `re-verdicted governed` | 1 | `config/instructions` |

So "3 v2.0.26 ids retired" is **exactly right** (3). But "9 ids re-instituted" is a gloss the census does not make: only **7** ids were resurrected from `historical`. The 9 that appear in the § B′ live table (census lines 249–257) are 7 resurrected + 1 re-anchored + 1 re-verdicted. `config/AGENTS.md` was never `historical` — it was already `governed (OC-2)` at round 18 and was only re-anchored to a new string; calling it "re-instituted" mislabels a row that was never de-instituted.

```
$ python3 -c "import collections;..."   # census lines 310-321, verdict column
{'retired': 3, 'retained, re-anchored': 1, 're-verdicted governed': 1, 'resurrected': 7}
$ grep -c "re-instituted\|reinstated\|re-instat" corpus/knowledge/instruction-surface-census-round13.md
0        # the census never uses the word the LOG uses
```

The same phrase appears in `SCORECARD.md:32` ("9 opencode ids re-instated anchor by anchor"), so this is a shared, propagated wording rather than a transcription slip in one file. `config/instructions` re-verdicted governed **is** correct (census:314 and the § B′ table at census:254 both say so).

**Severity.** Calibration: the *count* of retired ids and the *verdict* on `config/instructions` are right; the "9 ids re-instituted" gloss overstates the resurrection set by two and asserts a vocabulary the census does not use. A reader auditing the ledger row-by-row finds 7, not 9, against that word.

---

## F3 — MEDIUM — `LOG.md:2323` "answers the sentinel's blocker" overstates what landed

**Claim under test** (`LOG.md:2323`):
> in-source `GOVERNANCE_ERRATA` row pinning `LOG.md:2111` … (`.ufo/waves/round-47/build/C3CriticDesign.md`; **answers the sentinel's blocker** `.ufo/waves/round-47/build/C3SentinelErrata.md`)

**What the sentinel actually asked for.** `.ufo/waves/round-47/build/C3SentinelErrata.md:35-45` lists **seven** numbered wave-2 probe groups:
1. honest pinned control (805 raw candidates → 1 registered exception → 804 remaining, zero unresolved, PASS; *"An absent registry or removed row must leave the original citation failing"*);
2. same cap, different target → FAIL;
3. self-issued absence → FAIL;
4. binding mutations (wrong source/line/token, off-by-one line, stale hash, path alias, second token on the line, a target that now exists) → each FAIL;
5. bad registry data (missing reason, wrong type, unknown key, invalid JSON/hash, duplicate member/row, unused row, more than one row) → fail closed with a named diagnostic;
6. round/absence semantics (entries for rounds 46/48 do not apply to round 47; expired rows are not silently carried; a dangling symlink is not proof of absence);
7. existing exclusion controls (quoted-dead and `round-N` schematic cases reported separately).

**What landed.** `verifiers/verify_skill_checklist.py:377-383` is a **hard-coded tuple** in the instrument source:

```python
GOVERNANCE_ERRATA_HORIZON = 2315
GOVERNANCE_ERRATA = (
    (2111,
     "7dcbf123313d46c469cab9f5dac2daa7567e54ac1ddf7cffdd1fd38c74200135",
     ".ufo/round-45/drafts/v10/post-r44-hunt.py",
     "each exited 2 because the referenced runners are absent"),
)
```

There is no registry file, no schema, no per-row `id`/`reason`/`evidence` fields, and no row/round/expiry semantics — so sentinel probe groups 2, 3, 5 and 6 are **not implemented in any form** and cannot be: a single inline tuple admits one row, has no reason field to validate, carries no round, and has no expiry. Probe 7 (the two pre-existing exclusion classes reported separately) is met in the detail string (`9 quoted meta-finding(s), 3 schematic token(s) excluded`) but is not a control.

**What *is* met, verified by mutation (all exit 1, gate fails closed as required):**

| probe | command | exit | observed detail |
|---|---|---|---|
| 1 (registry removed) | mutate `GOVERNANCE_ERRATA = ()` | **1** | `LOG.md:2111: '.ufo/round-45/drafts/v10/post-r44-hunt.py' does not resolve …` |
| 4 (line drift) | 1-byte edit of `LOG.md:2111` | **1** | `erratum LOG.md:2111 …: line text drifted` |
| 4 (past horizon) | row line → 2316 | **1** | `erratum LOG.md:2316 … is past horizon 2315 or absent` |
| 4 (appended copy) | append a line citing the same token | **1** | `LOG.md:2327: '.ufo/round-45/drafts/v10/post-r44-hunt.py' does not resolve` |
| 4 (restored runner) | create the path | **1** | `erratum LOG.md:2111 …: stale, the path now resolves` |

And the append-only prefix holds: `git show c61a973:LOG.md | cmp - <(head -n 2315 LOG.md)` → exit 0; `git diff c61a973 -- LOG.md | grep -c '^-[^-]'` → 0.

**So the mechanism is sound and the erratum is genuinely fail-closed**, but the *attribution* is a false statement about scope: the sentinel's blocker was a multi-arm wave-2 probe program (7 groups, registry-file semantics, round/expiry semantics, bad-data diagnostics), and the landed artifact answers 1 of 7 groups (probe 1's "absent registry must fail" clause) plus parts of group 4. Calling it "answers the sentinel's blocker" — in a LOG entry that simultaneously claims a falsification wave is next — will make a wave-2 reviewer believe those seven probe groups are already discharged. The `SCORECARD.md:33` row is more careful: it enumerates *"in-place launderings, a restored runner, an appended copy and past-horizon rows all FAIL"* — exactly the arms I reproduced — and says nothing about a registry, bad data, or round semantics.

---

## F4 — LOW — `LOG.md:2319` "the planning data-walk rode scout/connector items (`ConnClaimSeparability`, `RevPlanCalibration`)" — the two cited seats did not report, and one of them was a reviewer

**The sentence** (`LOG.md:2319`): *"The L1 held the §3 planner seat; the planning data-walk rode scout/connector items (`ConnClaimSeparability`, `RevPlanCalibration`)."*

Three checks:

1. **"§3 planner seat"** — there is no §3 in `plans/round-47.md` (its headings are `## Starting point` / `## Claims` / `## Not claimed` / `## Waves` / `## Replacement coordinator note`, lines 8/18/41/50/55) and no numbered-section convention anywhere in the lane. `PROTOCOL.md` uses named `§` forms only (`§Appendix`, `§Evidence standard`, `§Gate standard`, `§Invariants`, `§Capabilities`, `§Push scope`, `§Round-robin step`) — `grep -n "§3" PROTOCOL.md MISSION.md AXES.md CORPUS.md` → 0 hits. The plan says *"L1 holds the planner seat"* (`plans/round-47.md:52`), unnumbered. "§3" is an unresolvable pointer.

2. **"scout/connector items"** — `build-dispatch.json:842` gives `ConnClaimSeparability` role `connector` ✓, but `build-dispatch.json:890` gives **`RevPlanCalibration` role `reviewer`**, not scout or connector. The entry mislabels one of its own two cited items.

3. **The "data-walk rode" claim is unverifiable and self-contradicting** — `RevPlanCalibration` produced **zero artifacts** in `build/` (`ls build/ | grep -i RevPlan` → empty) and is one of the 20 seats the *next* sentence lists as dead. `ConnClaimSeparability` produced only `ConnClaimSeparability.patch` — a patch that was **not integrated**: it proposes `verifiers/errata-registry.json` (a registry *file*), corpus-baseline `58 → 59` (landed is `58 → 60`), a `trigger.description_no_xml_tag` check id (landed is `trigger.no_xml_tag`), and a differently-worded `corpus/README.md` row (landed row is titled *"Round-46 non-author spot-check (integrator)"*, not *"Round-46 verifier spot-check"*). The landed `fault_injection_corpus.sh` change matches `ExecFaultBaseline.whatif-planter-fix.patch` byte-for-byte (`index 1d0d77a..30d3fc1`), **not** `CritNoHarm.planter.patch` (`index 1d0d77a..d401a2a`) — so the fault-harness fix the entry attributes to `ExecFaultBaseline.md` is correctly attributed. But `ConnClaimSeparability`'s row, registry and check id are all absent from the landing.

**Severity.** Low. The entry's substantive C3/C2 numbers are unaffected; this is a provenance sentence that mislabels a role and cites two seats, one of which contributed nothing integrated.

---

## F5 — SURVIVES — the C3 errata gate is genuinely fail-closed on every arm I could construct

The one C3 claim I could most plausibly break did not break. `verifiers/verify_skill_checklist.py:1519-1530` (`errata_problems`) requires **all four** of: the row line exists and is `<= GOVERNANCE_ERRATA_HORIZON` (2315), the line's sha256 matches the pinned digest, the absence wording is present on that line, the row names a subject that is actually on that line, **and** the token still does not resolve. Any one failure makes the whole gate exit 1.

Verified at `7ad7fad` (canonical clone), each mutation applied to the clone and reverted:

| arm | exit | first diagnostic |
|---|---|---|
| unmutated landing tree | **0** | `PASS … 848 … 1 recorded absence(s) excused` |
| row removed from the source tuple | 1 | `LOG.md:2111: … does not resolve` |
| 1-byte edit of `LOG.md:2111` | 1 | `erratum LOG.md:2111 …: line text drifted` |
| row line moved to 2316 (past horizon) | 1 | `erratum LOG.md:2316 … is past horizon 2315 or absent` |
| same token appended on a new line | 1 | `LOG.md:2327: … does not resolve` |
| the cited runner path recreated | 1 | `erratum LOG.md:2111 …: stale, the path now resolves` |
| `LOG.md:2111` sha256 re-derived | — | matches the pinned `7dcbf123…` exactly (line-level pin holds) |

Append-only prefix: `git show c61a973:LOG.md | cmp - <(head -n 2315 LOG.md)` → **exit 0**; `git diff c61a973 -- LOG.md | grep -c '^-[^-]'` → **0**. The entry's own claim that the entry sits at the tail of `LOG.md` and leaves `LOG.md:2111` unmoved is **true**.

The `SCORECARD.md:33` sentence — *"in-place launderings, a restored runner, an appended copy and past-horizon rows all FAIL"* — is **fully accurate**; I reproduced all four.

---

## F6 — SURVIVES — seat counts, role mix and refusal ledger reproduce exactly

Every number in `LOG.md:2320` checks out against the tracked dispatch artifacts, not against a narrative.

**92 seats.** `build-spec.json` `items` = 92; `build-dispatch.json` `counts.spawn` = 92, `registry.members` = 92; `build/swarm-registry.json` `members` = 92. Consistent, and the entry's "one validated 92-seat call" is exact.

**Role mix.** `build-dispatch.json` registry roles, counted:

```
scout 39, executor 17, reviewer 10, scribe 8, connector 6, critic 5,
revenger 2, sentinel 2, mutation-tester 2, simplifier 1     → 92
```

Byte-for-byte the entry's list, and it sums to 92.

**"72 seats reported" / 20 dead.** 92 registry members minus those with no `<SeatName>.md` in `build/` = **72** members with a report; exactly **20** lack one, and the entry's 20 names match that set exactly (no extras, no omissions):

```
C1OpencodeResolve, C1OcRuleRederive, C1PinsRepin, C1SelfTestFloors,
C1OmpLoaderRE, C1OcLoaderRE, C1CensusDocRows, C1DepthNoHarm, C2CheckImpl,
C2Battery, C2TriggerFidelity, C2FloorsBoxes, C3ErrataImpl, C3Residuals,
ConnClaimSeparability, RevPlanCalibration, CritNoHarm, RevHarnessIndependentNote,
RevSurfacesFixtures, ExecErrataAlt
```

The other 4 `.md` files in `build/` (`KnowDescriptionRule.s001/s002/s003`, `RevLogAppend.proposed-entry`) are sub-artifacts of two seats that *did* report, so 72 + 20 = 92 with nothing unaccounted.

**"Their partial artifacts were not integrated"** — true, and I checked each surviving patch:
- `C2CheckImpl.patch` proposes check id `trigger.description_no_xml_tag`, regex `</?[A-Za-z][^>\n]*>`, fixtures `desc-*`, floor **1971**. Landed: `trigger.no_xml_tag`, fixtures `xml-tag-*`, floor **1845**. Not integrated.
- `C2CheckImpl.floor.patch` → floor 1971; landed floor is 1845 (`verifiers/floors-registry.json`, `check_assertion_floors.py:119,140`). Not integrated.
- `ConnClaimSeparability.patch` → `verifiers/errata-registry.json` + `58→59` + `trigger.description_no_xml_tag` + a differently-worded README row. Landed uses an in-source tuple + `58→60` + `trigger.no_xml_tag` + a differently-worded row. Not integrated.
- `CritNoHarm.planter.patch` (`index 1d0d77a..d401a2a`) vs landed (`index 1d0d77a..30d3fc1`) — different blobs; the landed one is `ExecFaultBaseline.whatif-planter-fix.patch` verbatim. Not integrated.
- `C2Battery.json` (76 rows) → 0 of 76 values appear verbatim in the landed verifier. Not integrated.

**"spawned on gate try 9 after 8 job-cap refusals"** — `build-refusals.json` has 9 attempts; attempts 1–8 each `refused: 92`, attempt 9 `refused: 0` with a granted slot. Attempts 2–8 record a granted slot *and* a refusal, so the "8 refusals then a grant" reading is right, but only attempt 1 carries an explicit error string (`"Background job limit reached (100)"`); attempts 2–8 record `refused: 92` with a `slot: granted` line and no `error` field. The entry's characterisation ("8 job-cap refusals") is a reasonable reading of the ledger — the refusals are per-seat under a granted lane slot — and the `8`/`9` counts are exact. Not a finding; noted so the reader knows the file has no per-attempt error text for 2–8.

---

## F7 — SURVIVES — the before→after instrument numbers reproduce exactly

Re-run at `7ad7fad` in the canonical-layout clone, against `.ufo/waves/round-47/before/SUMMARY.md` for the before column:

| entry claim | re-measured at `7ad7fad` | before (`before/SUMMARY.md`) |
|---|---|---|
| `verify_surfaces.py --json` exit 2 → exit 0, **7/7** | exit **0**, `pass 7 fail 0` | exit 2 (opencode binary not found) |
| `check_substrate_pins.py` exit 2 (DRIFT 3/3) → exit 0, **3/3** | exit **0**, `OK 3/3 pins hold` | exit 2 DRIFT 3/3 |
| checklist `--json` exit 1 (9/1) → exit 0, **11/11** | exit **0**, `pass 11 fail 0` | exit 1, 9 PASS/1 FAIL `LOG.md:2111` |
| corpus integrity exit 1 → exit 0, **9/9** | exit **0**, 9 checks all PASS (`tracked_files 60`) | exit 1, `tracked_files 59!=58, unindexed 1` |
| corpus independent exit 1 → exit 0 | exit **0**, 9 checks (6 PASS / 3 INFO) | exit 1, unindexed |
| fault harness exit 1 → exit 0, **ALL PASS** | exit **0**, `verdict: ALL PASS` | exit 1, `verdict: FAILURES PRESENT` |
| surfaces `--self-test` 87 → **99** assertions, 0 failures | `0 failure(s) over 99 assertions` | 87 (floor) |
| checklist `--self-test` 1597 → **1845** assertions, 0 failures | `0 failure(s) over 1845 assertions` | 1597 (floor) |

Both self-test counts reproduce the floors registered in `verifiers/floors-registry.json` and `verifiers/check_assertion_floors.py:119,140` (`surfaces 87→99`, `checklist 1597→1845`), and `check_assertion_floors.py` itself reports all 9 instruments at floor.

**Two "before" values are re-measured, not copied, and hold:** the fault-harness before (exit 1) I re-ran at BASE in a canonical-layout clone (`/fast/scratch/kotoba-r47/w2/W2LogEntryBase`) → exit **1**, `verdict: FAILURES PRESENT`, with `fault-d1`/`fault-d2` WRONG-CLASS — matching `ExecFaultBaseline.md`'s BASE measurement. And the "AFTER code with the BASE baseline+census → exit 1" discriminating cell reproduces:

```
$ python3 -B verifiers/verify_surfaces.py --json \
    --baseline <BASE surfaces-baseline.json> --inventory <BASE census>
exit=1
  FAIL surfaces.opencode_extract | declared opencode class(es) produced by no rule:
  opencode:api-entries/instructions, opencode:project/AGENTS.md, opencode:read-hook/AGENTS.md;
  extracted opencode class(es) undeclared in baseline: …
```

**The C1/C2 "before" column in `LOG.md` is weaker than the wave-1 evidence the same round produced.** The entry says surfaces "exit 2 → exit 0, 7/7" and pins 3/3 — both true. But `before/SUMMARY.md:4` records the *substantive* before: `surfaces --opencode-binary <npx 1.19.3>: 4 PASS / 3 FAIL (literal_present, no_uncovered_class vacuity 0/8, opencode_extract OC-1/OC-4/OC-6)`, and `plans/round-47.md:22-23` repeats it. The entry quotes only the "binary not found" exit 2, so the reader sees no evidence that the extractor was substantively red (0/8 loader classes, three OC rules matching nothing) rather than merely unable to find its input. This is a **calibration gap in the receipt, not a false statement** — every number quoted is correct.

---

## F8 — SURVIVES — the C2 and C3 implementation claims match the landed bytes

- **Check id and scope.** `verifiers/verify_skill_checklist.py:97` documents `trigger.no_xml_tag`; `:310` registers it; `:1304` implements it over `name` and `description`. The live check reports `evaluated 2` (both fields non-empty) and PASS. The entry's "`trigger.no_xml_tag`" and "parsed name+description" are exact.
- **Four fixtures.** `verifiers/fixtures/checklist/xml-tag-{codespan,control,dq-escape,split}` — exactly 4, exactly the names the entry implies. The landed `trigger.no_xml_tag` detector (`XML_TAG_RE` at `:404`, `YAML_ANGLE_ESCAPE_RE` at `:409`) is **byte-identical** to `C2CriticRule.patch`'s detector (I applied `C2CriticRule.patch` to BASE and diffed: the only differences against the landing are the C3 governance hunks, `@@ -189,8 +189,12 @@` … `@@ -2125,12 +2182,58 @@` — the XML-tag hunk is *not* among them). So "reference design `C2CriticRule.md`" is exactly right.
- **The rejected alternative.** `ExecDescriptionCheckAlt.md`'s verdict line says it checks *"the strict-YAML-loaded description"* only, with check id `trigger.description_no_xml_tags` — i.e. description-only, exactly as the entry says ("it scans `description` only"). The landed tree has no such id and no `description_no_xml_tag*` fixture. Correctly characterised and correctly not taken.
- **"SKILL.md description `<skills>` → `omp skills router`".** `SKILL.md:14` reads `never reach the omp skills router — craft here is audit-side, not`; frontmatter `<skills>` count is **0** (whole-file count is 6, all in the body — the entry scopes its claim to the description, correctly). `before/SUMMARY.md:10` records the before as 1. Exact.
- **The C3 errata shape.** Line sha256, token and absence wording are all present and match (`sha256(LOG.md:2111)` = `7dcbf123…`, token `.ufo/round-45/drafts/v10/post-r44-hunt.py`, quote `each exited 2 because the referenced runners are absent` all present on the line). Horizon 2315 is `verifiers/verify_skill_checklist.py:377` and equals the BASE `LOG.md` line count — i.e. the errata can never excuse a line the round-47 entry itself appends, which is the fail-closed property. Exact.
- **corpus-baseline re-record.** `verifiers/corpus-baseline.json` `checks["corpus.index.tracked_files"].expect` = 60, was 58 at BASE; the `notes.round47` text says `58 -> 60` and names both indexed files. Matches.
- **Census row moves.** The five v2.0.26 loader rows are byte-identical between BASE and landing (I diffed row-by-row on the 5 class ids: `byte-identical in new: True` for all five), and the § B table body is now empty with the rows relocated to `## Superseded class rows…` (census:287-303) — "moved v2.0.26 rows byte-identical" is exact.
- **Frontier rows.** `corpus/SOURCES.md` goes 11 → 15 rows at `7ad7fad`; S012 = `code`/A/mined, S013 = `docs`/A/queued, S014 = `docs`/A/queued, S015 = `own-work`/A/mined. All four match the entry verbatim. A `2026-10-21 — round-47 sources sweep` search-log entry exists.
- **Lessons/quality.** `corpus/lessons/round-47.md` has M20, M21, M22 and a `## Gate` section; `corpus/QUALITY.md:30` has Q19. Exact.
- **"Not claimed: `verify_harness_claims.py` 21/28 before and after (same seven DRIFT ids; three host skills born 2026-10-20 — Q09 debt)"** — 21/28 both before and after, same seven DRIFT ids (`omp.db.rows`, `omp.offered.skills`, `omp.cache.misses`, `omp.catalogue.total`, `omp.catalogue.missing_names`, `omp.cache.verified_skills`, `oc.roots.names_plus_builtin`) ✓. The three host skills are real and dated 2026-10-20: `create-toolset` (btime 2026-10-20 13:50:21), `unreal-mcp` (13:50:21), `unreal-skill` (13:50:21). Note the observed `oc.roots.names_plus_builtin` moved 10 → 11 between the before and after runs (a fourth root appeared mid-round) — the *id set* and the 21/28 count are unchanged, so the entry's claim holds, but a reader comparing raw outputs will see the observed value differ. Also note `before/SUMMARY.md:9` and the after output show `names+builtin=10` vs `11` respectively.

**One small wording note (not a finding):** the entry says the harness-claims residual is "three host skills born 2026-10-20"; the DRIFT that needs Q09 debt is `omp.db.rows 17≠14` / `omp.offered.skills 10≠7` / `omp.cache.misses 3≠0` / `omp.catalogue.*` — driven by those three new skills — plus `oc.roots.names_plus_builtin`. The entry's "three host skills" is the `unreal-*`/`create-toolset` triple, which is right for the omp side.

---

## F9 — LOW — the entry's "Not claimed" residual list drops one residual the plan and the wave-1 draft both carried

`plans/round-47.md:46-47` and `.ufo/waves/round-47/build/RevLogAppend.proposed-entry.md:18` both list **six** r46 spot-check residuals:

> mirror opt-out, missing verdict, NaN/case-variant keys, row `kind`, payload-selectable committed scope-outs, **the printed C1 counting command exit 2**

The landed `LOG.md:2326` lists only **five** — *"round-46 residuals carried (mirror opt-out, missing verdict, NaN/case-variant keys, row `kind`, payload-selectable committed scope-outs)"* — omitting *"the printed C1 counting command exit 2"*.

That residual is **live at the landing commit**, not closed. Re-running the r46 command as printed in `.ufo/round-46/scouts/T1.md:10` at `7ad7fad`:

```
$ python3 verifiers/compare_harness_independent.py --expect-n 28 --cwd "$PWD" \
    --scope-file verifiers/harness-independent-scope.json --no-stamp \
    --report /tmp/…/rows.md --json --receipt /tmp/…/receipt.json
exit=2
  compare_harness_independent: ERROR: false blocker: scoped row omp.catalogue.found
  declares observable {"candidate_blocks": 24227, …} but recomputation gives {"candidate_blocks": 24231, …}
  (same for omp.catalogue.matched, omp.catalogue.missing_names)
```

The r46 spot-check file itself still lists it as carried-open (`corpus/lessons/round-46-verifier-spotcheck.md`, "Open residuals (carried): … the printed C1 counting command exits 2 as written"). So the landing's "Not claimed" list is **incomplete relative to the plan it claims to execute**, and the omitted item is the one that is still red. This is the same omission pattern as the plan's own M21 ("Corpus file landed without its index row") — a residual that exists in the evidence but does not appear in the receipt.

Note this is a *documentation-completeness* defect, not a false statement: everything the entry does list is accurate.

---

## Residual risk and verification gaps

**Residual risks a wave-2 reviewer should carry forward**
1. **F1 is the only number in the entry that is wrong at the landed tree.** Because it is wrong in the *direction* of a stale pre-landing copy, treat every other "after" number in `LOG.md` as "verified by re-measurement" only where I list it in F7 — I re-ran all nine instrument pairs, and all others reproduce.
2. **The C3 errata is a single hard-coded tuple, not a registry** (F3). A future line at `LOG.md` ≤ 2315 that names a *second* dead path cannot be excused at all; a future line that re-cites the *same* token below 2315 would be excused only if it also matches the pinned sha — the pin is per-line, so this is tight, but the *capability* the sentinel asked for (multiple rows, round scoping, expiry) does not exist. Any claim that C3 is "a pinned erratum registry" is currently true only of one row.
3. **The `corpus/README.md` r46 spot-check row wording in the landing matches neither wave-1 proposal** (F4): landed = *"Round-46 non-author spot-check (integrator)"*; `C3CorpusIndex.patch` proposed *"Round-46 verifier spot-check"*; `ConnClaimSeparability.patch` proposed *"Round-46 verifier spot-check"* with different prose. The landed wording is integrator-authored. Harmless for the gate (the index check is token-based) but it means the "reference design" pointer in the entry covers only the errata row, not the corpus-index row.
4. **`verify_harness_claims.py`'s observed `oc.roots.names_plus_builtin` moved 10 → 11 mid-round** (F8). A reviewer re-running the harness-claims gate today sees 11, not 10. The 21/28 count and the id set are stable; the observed root count is not. That is Q09-class substrate drift, correctly declared as debt.

**What I did NOT check**
- **I did not run the falsification wave-2 battery** (the `falsify-spec.json` matrix) — only the instruments the LOG entry names, plus four hand-built mutation arms of the C3 gate. I did not attempt the sentinel's probe groups 2/3/5/6 (they are unimplementable against a one-row inline tuple — F3) nor its group-7 quoted-dead / literal-`round-N` controls, which the sentinel assigned to wave 2.
- **I did not verify the C1 opencode rule re-derivation against the frozen dump line by line** (the census's anchor counts: `ConfigInstructionPlugin 0`, `X.join(r.config,…) 1`, `for(let O of T.instructions) 1`, …). I confirmed the *shape* of the claims (rule ids OC-1..OC-6 present, `OC-3b` requires `.filter(`, `OC-4` includes `fn("ReadTool.execute")`, § B′ has 9 live rows) and that `verify_surfaces.py` re-derives them at runtime (exit 0, 7/7, `9/9 declared class(es) from 7/7 rules`). I did not re-count the strings in `/fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings` myself. I also did not re-derive the omp `lq`/`Xl`/`Fo` callee allowlist against `omp-18.12.5.strings` beyond confirming the regex/allowlist in the landed source and the 18.12.5 fixture's presence and PASS.
- **I did not check `SHONEN.md`** — it is not in the round-47 record list I was given, and it is not mentioned in the entry.
- **I did not audit the `SCORECARD.md` / `PROVINCE.md` / `plans/round-47.md` records themselves** beyond checking that the three round-47 rows the entry points at exist and that the two claims most likely to drift (F1's 804; F2's "9 ids re-instated" at `SCORECARD.md:32`) are or are not present. `SCORECARD.md:32` does carry the "9 opencode ids re-instated" phrasing (F2).
- **I did not re-run the 20 dead seats' partial artifacts for behavioural equivalence** — only byte-level integration checks (patch applicability / blob hashes / string presence). In particular I did not execute `C2CheckImpl.patch` or `CritNoHarm.planter.patch` to see what they *would* have produced.
- **I did not test the C3 errata against a symlink or an unreadable path** (sentinel probe 6, "a dangling symlink, unreadable path, or resolver error is not proof of absence") — the landed `errata_problems` calls `citation_resolve(token, repo)`, whose behaviour on a dangling symlink I did not inspect.
- **I did not check whether `LOG.md:2326`'s "Falsification wave and landing pin follow in the next entry" was honoured** — at `7ad7fad` there is no next entry; `LOG.md` ends at 2326. That is expected for a landing commit and this falsify wave is the next step, but the promised "landing pin" entry does not yet exist.
- **I did not verify the `before/SUMMARY.md` raw outputs** beyond reading them; I re-derived the fault-harness before-value myself at BASE rather than trusting the file, and the file has no fault-harness line at all (its 12 lines cover census/surfaces×2/pins/checklist/corpus×2/harness-claims/frontmatter/omp/opencode).

**Note on scope discipline.** All production files under `/home/vgpnk/Projects/shokunin/kotoba-shokunin` are read-only to me. Every mutation I ran (the four C3 arms, the `GOVERNANCE_ERRATA = ()` arm, the `SCORECARD.md`/`LOG.md` swap-backs, the `cmp` prefix test) was applied in `/fast/scratch/kotoba-r47/w2/W2LogEntry/kotoba-shokunin`, a scratch clone, and each was reverted immediately; the clone's `git status --porcelain` was empty at every checkpoint. The `~/.npm/_npx/.../opencode.exe` path was never executed — only its sha256 was read from `verifiers/baseline.json` and the frozen `SHA256SUMS`.
