# ReviewerPlanR74 — independent re-measurement of the round-74 plan's base readings, and the plan attacks

Seat: ReviewerPlanR74 (kotoba round 74, hyaku run 7, attempt 1, wave 1). Read-only: no tracked lane
file was edited; no lane gate was run inside a bare clone; both sandboxes were built per the contract
(`/tmp/k74w1-ReviewerPlanR74.*`, `/tmp/k74fleet-ReviewerPlanR74.*`, deleted before return). Base
`1e03d1991bc02281b00a5b7a5e00c9d5d5d72908`; plan commit `329e7d91d7d750031c35d264f0e34af1d0ce8385`.
No tool was installed or upgraded.

## Verdict

**The plan's before-values re-derive: all nine figures I could recompute agree with
`plans/round-74.md` § Before-values at `1e03d19` (census 148 rows by three patterns; 15 of 20 sibling
drift and the five byte-equal lanes by blob id; 0 held rows and 0 phrase hits for the three
skill-creation pages; SKILL.md 570 lines / 74,174 B / 74 over-length lines; 20 collisions `S203`–`S222`;
quarantine slice 13 rows; 20 W04 warnings; the base corpus drift 139/138, 97/95, unindexed 1).**

**The plan text does not survive its own attacks.** Three defects are blocking because they make a
frozen predicate or a promised no-harm reading false as written:

1. the no-harm item `check_sibling_census.py on the r49 entry and --province` (plan:158) is made red by
   C2's own predicate (d): I measured `province rows 20 matched 4`, exit 1, on a re-pinned PROVINCE.md;
2. C2 predicate (e) (plan:133) is stricter than the base checker it binds in (a) and rejects `tabi`'s
   `none` row on a code-span occurrence of `kotoba` — N=20 becomes unreachable except by an
   unjustified reclassification that would drag SKILL.md into C2;
3. C1's cheapest shortcut is a copy of the staged package entry (the plan's own assimilation source),
   and no clause in (a)–(f) distinguishes it from a seat that opened the three pages.

Seven further defects (Q33 trust anchor, Q26 headline, axis label, Q55 timestamp, id spaces,
reproducibility of one before-value command, one unclaimed landing and one-way separability) are listed
below by severity. Every finding carries the command and its observed output; nothing here rests on
another seat's report or on the plan's own statement.

---

## 1. Before-values, independently re-derived

| item | plan's figure | my command | observed | verdict |
|---|---|---|---|---|
| census rows | 148 | `git show 1e03d19:corpus/SOURCES.md \| grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` | `148` | agrees |
| census rows, second pattern | 148 | `… \| awk -F'\|' '/^[ ]{0,3}\|[ ]*S[0-9][0-9][0-9]/ {n++} END{print n}'` | `148` | agrees |
| census rows, third pattern (distinct ids) | 148 | strip leading `\|`, split on `\|`, field 1 matching `^S[0-9]{3}$`, `sort -u \| wc -l` | `148` (`S001`–`S222`; 152 `^|` lines = 148 rows + 2 header/separator pairs) | agrees |
| census warnings | 20 W04 | `grep -c W04 .ufo/waves/round-74/receipts/census-before.txt`; re-run `cd /home/vgpnk/Projects/shokunin && ./scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` | `20`; re-run exit 0, `20`, last line `kotoba ok …/corpus/SOURCES.md` | agrees |
| sibling drift | 15 of 20 | per row: `git -C ../<lane>-shokunin rev-parse <pin>:SKILL.md <pin>:PROVINCE.md` vs `rev-parse <freeze-head>:…` | **15 DRIFT / 5 byte-equal**; equal lanes `audio, game-dev-2d, game-dev-3d, kagi, lore`; drifted-only-in-PROVINCE: `revenger, souji, tabi, kotodama`; drifted-only-in-SKILL.md: `chousa` | agrees |
| five unchanged lanes byte-equal | yes | blob-id equality at both ends (`audio` and `game-dev-2d` have no `SKILL.md` at either end; their `PROVINCE.md` blobs are equal) | all five equal on both files | agrees |
| pins 50–312 behind | 50–312 | `git rev-list --count <pin>..<branch>` (receipt) restricted to the 15 | min `kasegi` 50, max `mori` 312 | agrees |
| freeze file is the true head | — | `rev-parse refs/heads/<branch>` vs the tsv `head40`; and tsv blob cells vs `rev-parse <head40>:SKILL.md/PROVINCE.md` | 20/20 blob cells `ok`; 16/20 heads still the branch head — `kake, kasegi, kotodama, souji` moved after the 01:25:43Z freeze, all four freeze heads still ancestors (`merge-base --is-ancestor` exit 0) | agrees, plus a live-dependency finding (F6) |
| held skill-creation rows | 0 | `git show 1e03d19:corpus/SOURCES.md \| grep -cE 'agentskills\.io/skill-creation/(best-practices\|using-scripts\|quickstart)'` | `0`; the only `skill-creation/` ids held are `evaluating-skills` and `optimizing-descriptions` (2 rows each) | agrees |
| rule-phrase sweep | 0 hits | `git grep -cniE 'calibrating control\|defaults, not menus\|favou?r procedures\|fragility of the task\|one-off commands\|using-scripts\|pipx run\|uvx ruff' 1e03d19 -- corpus SKILL.md PROVINCE.md` | no output, exit 1 (0 matches) | agrees |
| SKILL.md weight | 570 / 74,174 / 74 | `git show 1e03d19:SKILL.md \| wc -lc`; `… \| awk 'length>300' \| wc -l` | `570 74174`; `74` | agrees |
| package id collisions | 20, `S203`–`S222` | `comm -12` of lane ids (registry rows, first cell) and package ids (`grep -oE '^[ ]{0,3}\|[ ]*S[0-9]{3,}[ ]*\|' SOURCES.append.md`) | `20`, first `S203`, last `S222`; staged set is `S203`–`S390` (188 ids) | agrees |
| quarantine slice | 13 data rows | `cat .ufo/waves/round-74/assimilation/quarantine-slice \| wc -l` | `13` (7 `payload-absent` + 6 "could not be fetched"); **ids are campaign round-scoped, not the package's** — F7 | count agrees, ids do not |
| base corpus drift (the battery's red) | 139/138, 97/95, unindexed 1 | fleet-shaped sandbox at base: `python3 -B verifiers/verify_corpus_integrity.py` | `DRIFT corpus.index.tracked_files: observed=139 expected=138` / `DRIFT corpus.index.unindexed: observed=1 expected=0` / `DRIFT corpus.pointers.report_total: observed=97 expected=95`; `6/9 checks pass` | agrees |
| gate registry at base | 58 of 58 (+2 = 60 of 60) | `python3 -B verifiers/check_gate_registry.py --rev 1e03d19` | `gate registry rows conformant 58 of 58 lane verifiers; phantom 0`; `git ls-tree 1e03d19 verifiers/` `.py`/`.sh` count `58` | agrees — plan:158's `60 of 60` is arithmetically right |
| Q65 line budget | 590 of 600 | `570 + 14 + 2 + 4` | `590`; cap `600` is stated in `corpus/QUALITY.md:81` (Q65) and the base is `570` | agrees |
| watchdog claim | 1 launch, 0 lane-dead | `grep -c 'launch kotoba round=74' .ufo/watchdog.log; grep -c 'lane-dead-no-report kotoba round=74' .ufo/watchdog.log` | `1`, `0` (launch at `2026-10-25T22:05:09-03:00`) | agrees |
| base commit author | `protocol-shokunin` | `git log -1 --format='%an <%ae> \| %s' 1e03d19` | `protocol-shokunin <protocol@shokunin.local> \| round-73 verifier spot-check (integrator, hyaku): non-author admit/reject` | agrees |

Not re-measured, and why: the full `check_tip_battery.py --rev <rev>` self-run (236.6 s at base, my
assignment did not ask for it and the L1 receipt is what it is — see § 4 gap 2); the
`verify_harness_claims.py` 17-of-28 figure (126 s, declared "information, not a claim"); the
`compare_harness_independent.py` timeout (>250 s).

---

## 2. Findings by severity

### F1 — BLOCKING. The no-harm item `check_sibling_census.py on the r49 entry and --province` cannot stay green once C2 lands (plan:158)

Plan:158 promises the no-harm battery includes "`check_sibling_census.py` on the r49 entry and
`--province`". C2's predicate (d) (plan:132) requires `PROVINCE.md` § Adjacent at `--rev` to carry the
**freeze-head** commit, and the r49 census entry carries the **r49 pin**. The base checker requires the
two to be equal (`verifiers/check_sibling_census.py` docstring, "each row's classification and commit
must equal the census row's").

Base (green, the control):

```
$ python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md
rows 20 verified 20
province rows 20 matched 20
exit=0
```

After bumping only the 20 `## Adjacent` commit cells to the freeze heads in a `/tmp` copy of
`PROVINCE.md` (no other change):

```
$ python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md \
    --province /tmp/k74w1-ReviewerPlanR74.dXl9/PROVINCE-new.md
FAIL province row 15 (line 27): lane mori commit 24ebc7991e90 does not match the census 28b79d3d1b76
FAIL province row 18 (line 30): lane tabi commit 856fa9e12021 does not match the census e3cf4e0d30bb
… (16 FAIL lines) …
rows 20 verified 20
province rows 20 matched 4
exit=1
```

Repair: name the entry in the no-harm bullet — run the base checker on the **r74** entry with
`--province PROVINCE.md` (green by construction from (a)+(d)), and keep the r49 entry checked
**without** `--province` (a row-shape regression check). If the intent is that the r49 entry stays the
province's authority, then C2 predicate (d) must be dropped instead — the two cannot both hold. State
which, in the plan, before data.

### F2 — BLOCKING. C2 predicate (e) rejects `tabi`'s `none` row on a code-span occurrence, contradicting (a) and forcing an unjustified reclassification (plan:133)

Plan:133: "(e) no `none` row exists for a lane whose pinned `SKILL.md` or `PROVINCE.md` contains the
whole word `kotoba` (recomputed by the counter)". Plan:124-126 (a) binds each row to "the **base's**
`check_sibling_census.py` row checks". The base checker's `none` rule reads the **frontmatter
description** and `PROVINCE.md` only (`verifiers/check_sibling_census.py:380` `description_of`,
`:595-604` `if classification == "none": … problems.append("classified none, but the sibling's
description or PROVINCE.md at the pin names kotoba …")`).

`tabi` is a `none` row and its bytes at the freeze head:

```
$ git -C tabi-shokunin grep -niw kotoba 856fa9e1 -- SKILL.md
856fa9e1:SKILL.md:1313:  `LANES="protocol aggregator kasegi kengaku kake kumitate kotoba kagi kama"`
856fa9e1:SKILL.md:1450:  `LANES="…kumitate kotoba kagi kama"`.
$ git -C tabi-shokunin show 856fa9e1:SKILL.md | sed -n '1,3p' | grep -ciw kotoba
0
$ git -C tabi-shokunin grep -niw kotoba 856fa9e1 -- PROVINCE.md
(no output)
```

So tabi's row **passes** the base row checks (a) and **fails** (e): the same row is both required and
forbidden. Reaching 20 therefore requires reclassifying tabi `none`→`adjacent`, and
`check_sibling_census.py --skill` then requires the lane to be named in kotoba's description
(`SKILL.md:9-13` does not name `tabi`), i.e. C2 would edit `SKILL.md` — flatly contradicting plan:154
("C2 touches `PROVINCE.md` § Adjacent and its entry") and the budget bookkeeping at plan:159.

Repair: (e) must be the base rule, in the base rule's terms — "whose pinned frontmatter description or
`PROVINCE.md` names `kotoba`" — implemented on `description_of()` plus the `PROVINCE.md` bytes, never a
whole-file `grep -w`. If a broader rule is genuinely wanted, it must (i) exclude fenced/code-span text,
(ii) state that tabi's reclassification and a description edit are expected work, and (iii) move
`SKILL.md` into C2's surface list with its line budget.

### F3 — BLOCKING. The cheapest shortcut world is declared able to meet the target, and C1's cheapest world is not in the control list (plan:91-96, plan:138-141; Q37)

Q37 (prompt §9): "Before freezing, build the cheapest control that skips the claimed work, score it with
the frozen counter … **if it meets the target, the counter or target is wrong — fix it before data**."

- **C2.** Plan:138-141 pre-declares the carry-forward world ("the same plus `delta` cells computed by
  script") as "*measured and reported*, not asserted below 20, because a mechanical re-pin with
  recomputed cells is the lowest honest re-verification of the mechanical facts". That is the cheapest
  skip-world reaching the target, which Q37 says must be fixed before data, not exempted. The
  exemption is also self-defeating for C1/C2 symmetry: the same sentence concedes the counter cannot
  tell a script from a seat.
- **C1.** Plan:91-96 lists nine control worlds; none is the cheapest one — the staged package entry
  copied. `/home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/spec-script-craft-rules.md`
  already carries dated `source:` lines (`fetched as .md 12 078 B on 2026-10-23` for using-scripts,
  `4 080 B` for quickstart), `verified-at:`/`recheck:`, an id per page, and rule tokens per page. I
  checked those tokens against the live pages today:

  ```
  $ curl -sL --max-time 60 -A 'Mozilla/5.0' -o /tmp/k74-using-scripts.txt https://agentskills.io/skill-creation/using-scripts.md
    HTTP 200, 12 078 B, sha256 2cd7727106b423a758b4b6b1ab3545da74845a98e68e6718279846f89d62ad1f  (2026-10-25)
  $ curl … best-practices.md   HTTP 200, 15 060 B, ab9f3b6091a0f24816b52cd7b90a3fdf53e621f47dba13b36694be272b87fb41
  $ curl … quickstart.md       HTTP 200,  4 080 B, 7c480b447edac58fd8ff8f250c471dfc7d4621155b91fabed46379075c32bffb
  $ grep -c 'One-off commands' /tmp/k74-using-scripts.txt            -> 1
  $ grep -c '# Create the skill' /tmp/k74-quickstart.txt             -> 1
  $ grep -c '.agents/skills/' /tmp/k74-quickstart.txt                -> 3   (0 in using-scripts)
  ```

  Clauses (a)/(c)/(d)/(e) all key off the *snapshot*, never off the reading act, so a copied body with
  lane ids, registry rows and per-page tokens scores 3 of 3 with no page opened. Four of the five
  best-practices phrases the plan itself lists (`calibrating control`, `defaults, not menus`,
  `favor procedures`, `fragility of the task`) are one `grep` away in
  `/tmp/k74-best-practices.txt` — the "0 held" baseline is a baseline about the lane, not a barrier
  to a copy.

Repair (C1): add a clause the copy cannot satisfy — the entry's `## Gate` block must carry the lane's
own fetch receipt per page (URL, HTTP status, `date -I` access date, byte count, sha256) and those
values must equal the committed snapshot's size and its pre-data pinned hash (see F4). The campaign's
staged header has no status field and no sha256 and is dated 2026-10-23, so the copy world fails.
Add it as control world #10 and require it below 3. Repair (C2): either rename the claim to what the
counter measures (F6) and cite the carry-forward world as the *declared upper bound* in the receipt,
or add a clause a script cannot satisfy; do not leave the kill rule and Q37 contradicting each other.

### F4 — HIGH. Q33: both counters take their expected hash from the revision they measure (plan:78-79, plan:118-120)

C1 (c): "P's snapshot … has a sha256 equal to the pin in the committed manifest
`snapshots/MANIFEST.sha256`". The manifest is read at `--rev`; a seat that lands snapshot + manifest in
the same commit satisfies (c) tautologically — the check proves only that the snapshot was not edited
*after* the manifest, never that the snapshot is the page. C2 avoids this by convention (the freeze
file is committed before data, plan:117) but its predicate does not say the counter reads the freeze
file **at the base revision** or against a pre-data constant; the same tautology applies to
`sibling-heads-freeze.tsv` if a landing commit can rewrite it.

Repair: copy C2 (a)'s own good pattern (plan:124-126, "run from the base copy of that checker
(sha256-pinned in the counter), not from the measured revision") to both claims: pin the three
snapshot sha256 values and the freeze file's sha256 as constants in each counter's source (or in the
plan commit's receipt), and compare the measured revision's bytes against those constants. Then a
measured revision cannot supply its own trust anchor.

### F5 — HIGH. Axis label: C1's predicate counts new pages held, which AXES calls `coverage`, not `depth` (plan:52-61, plan:76-84)

`AXES.md:21`: "Expansion ↔ `coverage` + `adjacency`; quality ↔ `depth` + `freshness` + `operability`" and
`AXES.md:11` (depth) = "Verifiable technical detail — decision tables with real thresholds … A reader can
act on SKILL.md alone". C1's counted clauses are: (b) three **new** registry rows for pages the lane
held 0 of (the frontier→core move), (a) an entry row per page, (c) a snapshot per page — those are the
coverage surface by AXES' own mapping. The only depth-shaped clause is (e) (two table rows per page,
action cell ≥ 5 words + a token). Plan:60-61 defends the label by assimilation ("a knowledge entry that
never reaches SKILL.md's guidance is depth the executing agent cannot use"), which is an argument about
the *action*, not a threshold measurement.

The round still satisfies AXES' lowest-axis obligation through C2 (freshness, 8), so this is not a
trade — it is a mislabel of the kind the sizing list penalises ("Name the axis by the surface the round
changes, not by the number it produces").

Repair: add one clause only a depth move satisfies — e.g. each page's SKILL.md action cell must carry a
numeric bound or a named decision threshold that occurs in the snapshot (best-practices carries
`calibrating control` and explicit step counts; using-scripts carries version pins such as
`pipx run 'black==24.10.0' .`) — or declare the axis `coverage` and keep the assimilation argument in
the lesson.

### F6 — MEDIUM. Q26: C2's headline says "re-read" for a counter that reads cells, and one clause needs live fleet state (plan:101, plan:114, plan:127-128)

The counter per (a)-(e) measures: cell non-emptiness, a 40-hex commit, quote location within ±2 lines
at the pinned commit, recomputed `delta`, PROVINCE row equality, and the mechanical `none` rule. It does
not read for meaning — plan:145 concedes exactly that. The headline (`sibling rows re-pinned and
re-read N of 20`, plan:114) asserts more than the counter measures; the bound is honest but the
headline is what a reader and SCORECARD record.

Second half of the same finding: (b) requires "that commit is an ancestor of the lane's branch head **at
measurement**", i.e. the counter reads 20 live sibling repos at run time, not the frozen record. A
sibling force-push makes a row permanently 0 through no fault of the lane. Today this is satisfiable —
I checked the four freeze heads that already trail their branch head:

```
$ for lane in kake kasegi kotodama souji; do git -C ../$lane-shokunin merge-base --is-ancestor <freeze-head> refs/heads/<branch> && echo "$lane: ancestor"; done
kake: ancestor
kasegi: ancestor
kotodama: ancestor
souji: ancestor
```

Repair: headline → "re-pinned and mechanically re-located at the frozen fleet heads"; (b) → "ancestor of
the branch head **recorded in the freeze file**" (closed over the frozen record) with the live-ancestry
variant kept as a separate probe whose result is reported, not counted.

### F7 — MEDIUM. Three id spaces; the quarantine slice is in the campaign's round-scoped numbering, and the plan reads it as the package's (plan:56, plan:166)

Plan:56 cites "staged S236, S237" for using-scripts/quickstart; plan:166 says "Quarantine slice (13 data
rows): any row an admitted entry cites is hand-checked this round". The committed slice's `S236`/`S237`
carry the campaign's **round-10** rows, whose URLs are `https://skills.sh/docs` and
`https://skills.sh/audits`:

```
$ python3 - <<'EOF'   # over /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/quote-lint-full-v5.json
… findings with lane=='kotoba' and verdict=='fetch-failed'
fetch-failed round10 S236 https://skills.sh/docs
fetch-failed round10 S237 https://skills.sh/audits
fetch-failed round10 S238 https://code.claude.com/docs/en/security.md
fetch-failed round10 S239 https://skills.sh/agent
fetch-failed round10 S243 https://skills.sh/docs/api
fetch-failed round5  S169 https://ai.google.dev/gemini-api/docs/coding-agents
EOF
```

while the package's `SOURCES.append.md` `S236`/`S237` are the agentskills.io pages:

```
40:| S236 | Agent Skills — Using scripts in skills — https://agentskills.io/skill-creation/using-scripts.md | docs | A | …
41:| S237 | Agent Skills — Quickstart: Create your first Agent Skill — https://agentskills.io/skill-creation/quickstart.md | docs | A | …
36:| S232 | Agent Skills — Best practices for skill creators — https://agentskills.io/skill-creation/best-practices.md | docs | A | …
```

Consequence: as written, a reader concludes C1's two most load-bearing rows are quarantined as
unfetchable. They are not — all three pages return HTTP 200 today (F3's fetch receipt), and the campaign
itself recorded `12 078 B` / `4 080 B` for two of them on 2026-10-23, byte-count-identical to my fetch.

Repair: key the slice by URL, or add a mapping column (campaign round + id → package global id → URL);
say in the plan that the slice is quoted in the campaign's round-scoped numbering, and that C1's
`S232`/`S236`/`S237` are not in the fetch-failed class. Also state the three id spaces once
(lane `S001`–`S222`; campaign per-round ids; package `S203`–`S390`, 20 of them colliding — plan:30).

### F8 — MEDIUM. Q55: the base-battery receipt's timestamp postdates the commit that carries it (`.ufo/waves/round-74/receipts/base-battery-l1.txt:1`)

```
$ head -1 .ufo/waves/round-74/receipts/base-battery-l1.txt
# L1 run at round-74 start (2026-10-25 ~22:3x -03), lane root, base 1e03d1991bc02281b00a5b7a5e00c9d5d5d72908
$ git log -1 --format='%ci' 329e7d9
2026-10-25 22:27:29 -0300
$ grep 'launch kotoba round=74' ../.ufo/watchdog.log
2026-10-25T22:05:09-03:00 launch kotoba round=74 pgid=1711177 driver=hyaku-inline attempt=1
```

The receipt records `wall 236.6s`; a run of that length cannot start at 22:3x and be committed at
22:27:29. The round start is 22:05:09, not "~22:3x". Repair: state the measured window (e.g.
`started 22:23:0x, wall 236.6 s`) or drop the clock label and keep `date -I`.

### F9 — LOW. The census before-value command is fleet-relative inside a table of lane-relative commands (plan:20)

```
$ git ls-tree 1e03d19 --name-only scripts/ | wc -l
0
```

`scripts/sources-census.sh` does not exist in the lane at any revision; the row's neighbours
(`python3 -B verifiers/check_tip_battery.py`, `wc -lc SKILL.md`) are lane-relative, so a reader
re-running from the lane root gets ENOENT. It works only from `/home/vgpnk/Projects/shokunin` (I ran it
there: exit 0, 20 W04, `kotoba ok`). Repair: write the host-absolute
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh …`, the convention the lane already uses for
fleet paths elsewhere.

### F10 — LOW. The two new gates' floors rows are never claimed (plan:156-159)

`check_gate_registry.py` requires a `gate` to declare a `--self-test` flag ("A `gate` may not say
`none`", `verifiers/check_gate_registry.py:33`), and `check_assertion_floors.py` is the anti-shrink
guard for exactly that (`instrument_total 15`, 15 instruments at base; its docstring records round 58's
routed defect R3: "correction_sweep at 25 (its self-test was unfloored, so a dropped case … still read
green)"). The no-harm list promises `60 of 60` on the gate registry (correct: universe `58` + 2) but
never a floors-registry row per new counter. An unfloored `--self-test` on the two new counters is the
R3 defect re-created. Repair: add to the no-harm list "+2 `verifiers/floors-registry.json` rows with
their observed self-test assertion counts, `instrument_total` 15 → 17", and record the added floors wall
time (base 215.5 s inside a 236.6 s battery run under `timeout 280` — 43 s headroom).

### F11 — LOW. Separability is proved only in one direction, and the touch lists omit the registry rows (plan:153-159)

Plan:155: "Each verifies with the other not landed (commit order proves it: the C2 commit is made first
and measured at its own revision)". That proves C2 verifies without C1. It does **not** prove C1
verifies without C2, because C1 is then measured at a revision that already contains C2's entry and
§ Adjacent rows — `AXES.md` ("Claims must be causally separable — each verifiable without the others
having landed"). Separately, plan:153-154 says "C2 touches `PROVINCE.md` § Adjacent and its entry",
while plan:159 books both new gate-registry rows in SKILL.md against C1's budget: each new counter's
`## Gate registry` row belongs to the commit that lands that counter, so C2's commit also edits
`SKILL.md` (§ Gate registry) and `verifiers/floors-registry.json` — the touch list is wrong in the
mechanical sense even where the counters do not read each other's bytes.

Repair: measure each counter at a revision with the other claim's files absent (land C1's `SKILL.md`
subsection, entry, snapshots, `§ Core` and its gate row first; measure C1 there; then land C2 and
measure C2) **or** revert the sibling claim's files in a fleet-shaped sandbox and record both readings.
And write the touch lists as: C1 → `SKILL.md` (§ body-craft subsection, frame sentence, its own gate
row), `PROVINCE.md` § Core, `corpus/SOURCES.md`, `corpus/knowledge/`, `snapshots/`, floors row;
C2 → `PROVINCE.md` § Adjacent, its entry, its own gate row, floors row.

---

## 3. Plan text checked against the protocol, item by item

- **PROTOCOL/AXES admission** (`AXES.md` "A round is admitted only if every claim verifies and no axis
  is harmed"): 2 claims, 2 axes ✔; lowest non-retired axis worked (C2, freshness 8) ✔; predicate frozen
  with one sentence in plan/counter/receipt ✔; no target narrowing after landing (Q28) ✔; strict
  control worlds enumerated ✔ with the F3 exception.
- **Universal clauses without an enumerating command** (§9): none found that is not enumerated — (e) C2
  is a universal negative over exactly the 20-lane universe the counter walks, and `_skill`/lane-set
  checks in the base checker enforce set equality (`rows 20 verified 20` at base). C1's "the guides'
  body-craft rules reach SKILL.md" is universal in rhetoric but counted per-page ✔. The one unenumerated
  universal is in prose only ("every cited page is re-opened this round", plan:57) — that is F3's gap.
- **Q33 trust boundaries**: C2 (a) is the good pattern (base copy of the checker, sha256-pinned); C1
  (a)-(f) and C2's freeze-file read take the anchor from the measured revision → F4.
- **Q45 census**: the wave-1 census is the right control and its lowering rule is pre-data. Margin risk
  worth naming to the census seat: `quickstart` is only 4,080 B with 48 backticks (24 code spans) vs
  15,060 B/168 and 12,078 B/254 for the other two — the page most likely to fall short of two locatable
  rule tokens is the one C1 needs for N=3. My own token probe found `.agents/skills/` (3 hits) and
  `# Create the skill` (1 hit) there, so 3 looks reachable — but the census, not this report, is the
  measurement.
- **Q55 chronology**: F8; every other timestamp I checked is at or before its commit (freeze
  `2026-10-26T01:25:43Z` = `22:25:43 -03` < plan commit `22:27:29 -03` ✔).
- **Arithmetic** (Q65): 570 + 14 + 2 + 4 = 590 ≤ 600 ✔; gate registry 58 + 2 = 60 of 60 ✔; collisions
  20 `S203`–`S222` ✔; quarantine 13 ✔ (count).

## 4. Residual risk and verification gaps

1. **Not re-run by me**: the full tip battery at the tip (`6 of 6` promise, plan:156-157) and its two
   invocation forms; `verify_corpus_integrity`/`verify_corpus_independent` at the **plan commit** (I
   measured only base, where I reproduced the same 139/138, 97/95, unindexed 1). Note for the
   closure: the base red was closed partly by raising `corpus-baseline.json` `expect` 138→139 and
   95→97 in the plan commit — disclosed in the file's `round74_start` note, so Q65's "named red" is
   satisfied, but the 6-of-6 reading at the tip will rest on an expectation bump landed in the same
   commit as the base receipt.
2. **`check_tip_battery.py` instrument pins**: `verifiers/corpus-baseline.json` is not among the six
   `INSTRUMENT_PINS` (`verifiers/check_tip_battery.py:125-138`), so the plan-commit baseline edit should
   not trip `instrument-pin`; the size guard's cap is 40 lines and the edit is +3/−2. I did not run the
   battery to confirm.
3. **C2's live dependency** (F6) survives repair only if (b) is closed over the freeze record; four
   freeze heads already trail their branch heads, all still ancestors today.
4. **Snapshot provenance** is unrecoverable in principle (a committed snapshot cannot be authenticated as
   the page); the strongest available bound is the lane's own fetch receipt (status, bytes, sha256) plus
   a pre-data hash pin — F3/F4.
5. **Classification correctness** is bound out by design (plan:145-149) and assigned to wave 2. My
   reading of the 20 rows found no lane whose *description* now names kotoba (only tabi's body, in a
   code span — F2), so no `none`→`adjacent` move is forced by the base rule at the freeze heads, on the
   bytes I read.
6. Sibling reads are read-only git against 20 lane repos at their freeze commits; four branch heads have
   moved since the freeze, so a wave-2 re-read must use the freeze file, not the branch heads.
