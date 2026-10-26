---
author: kotoba L1 (hyaku run 7, round 74, attempt 1)
date: 2026-10-25
round: 74
lane: kotoba
---

# Round 74 lessons — kotoba

Claims (frozen in `plans/round-74.md` at `329e7d91d7d750031c35d264f0e34af1d0ce8385`; errata E1 in `plans/round-74-addendum-1.md`,
committed with the counters at `d919179c63925e27f0d047ccccfc30b49cfe9766` before any data): **C1 coverage** (sourced, assimilation):
the Agent Skills `skill-creation/` guides best-practices, using-scripts and quickstart, counted by `verifiers/check_spec_craft.py --rev <rev>`
(`spec craft pages backed N of 3`); **C2 freshness**: the sibling census re-pinned at the frozen fleet heads, counted by
`verifiers/check_sibling_reread.py --rev <rev>` (`sibling rows re-pinned, re-located and re-diffed at the frozen fleet heads N of 20`).
C1 was declared `depth` in the plan and relabelled `coverage` by E1.1 before data (`ReviewerPlanR74` F5: the counted clauses are new held
ground). Round shape: two v1 waves.

## Gate

Assimilation theme (addendum §10; nothing written, run or fetched inside `/home/vgpnk/Projects/shokuknow`): **the Agent Skills
`skill-creation/` authoring guides** from `merge/kotoba/` (the read-only package at `/home/vgpnk/Projects/shokuknow/merge/kotoba/`) — staged
entries `spec-script-craft-rules.md` and `spec-description-trigger-discipline.md`, staged rows S232, S236, S237.

**Id collision check** (`.ufo/waves/round-74/assimilation/`): the lane registry held 148 ids (`reg-ids`), the package stages 188
(`staged-ids`), `collisions` lists 20 — `S203`–`S222`, the lane's own rows from rounds 69–73, which the package numbered earlier. **Guard proof:**
`assimilation/guard-proof/guard-proof.txt` (a scratch registry with an indented row `  | S234 | indented |`: the 0–3-space pattern finds it, the
column-zero pattern does not). **Renumber map, by document (URL), not arithmetic** (`ExecIdsR74`, `assimilation/` and
`w1/build/ExecIdsR74/renumber-map-final.tsv`): staged S232 `agentskills.io/skill-creation/best-practices.md` → **S223**; staged S237
`…/quickstart.md` → **S224**; staged S236 `…/using-scripts.md` → **S225**. Staged rows are campaign-schema: the lane rows were rewritten in the
11-column schema (no `|` in a cell, `recheck` `90d`, `used-by` the one admitted entry, `opened` 2026-10-25, the anchor carries the snapshot
sha256). The staged rows' own `scope`, `anchor` and `teaches` cells were not copied: they carry the package's 2026-10-23 opening. Scratch
validation before the append: `w1/build/ExecIdsR74/mirror-final-census.txt` (`sources-census.sh validate --file` exit 0 on the mirror); the
round-end command `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` is in the report.

**Rows opened this round** (each fetched by two wave-1 seats and by the L1 — HTTP 200, sha256 identical in every fetch — and re-read against
the committed snapshot, `.ufo/waves/round-74/snapshots/`; access date 2026-10-25; the page `.md` route, upstream
`agentskills/agentskills@69ef37e` as for S212/S213):

- **S223** — https://agentskills.io/skill-creation/best-practices.md; `snapshots/best-practices.md:96`; 15,060 B, sha256 `ab9f3b60…`; quote:
  "Match the specificity of your instructions to the fragility of the task.".
- **S224** — https://agentskills.io/skill-creation/quickstart.md; `snapshots/quickstart.md:21`; 4,080 B, sha256 `7c480b44…`; quote:
  "VS Code looks for skills in `.agents/skills/` by default." (the code span is the page's own).
- **S225** — https://agentskills.io/skill-creation/using-scripts.md; `snapshots/using-scripts.md:13`; 12,078 B, sha256 `2cd77271…`; quote:
  "When an existing package already does what you need, you can reference it directly in your `SKILL.md` instructions without a `scripts/`
  directory." (code spans are the page's own).

Quote lines were re-read by `sed -n '96p'`, `'21p'` and `'13p'` on the snapshots (no byte dropped but the surrounding sentences on the
same physical line). Fetch record: `snapshots/FETCH-LOG.tsv`; pins: `snapshots/MANIFEST.sha256` and the `PAGE_SHA` constants of the counter.

**Admitted:** `corpus/knowledge/spec-skill-creation-craft-round74.md` (three rows; documentary evidence only), acted on in `SKILL.md` § Body craft
— the specification's skill-creation guides. Expansion credit: ground the coverage map did not hold — at base the three URLs had 0 registry rows
and the rule-phrase sweep (`calibrating control|defaults, not menus|favor procedures|fragility of the task|one-off commands|pipx run|uvx ruff`)
printed `hits=0` over `corpus SKILL.md PROVINCE.md` (`receipts/base-sweeps.txt`).
**Dropped from the staged entries on the live bytes** (`ScribeEntrySpecR74` § Dropped): the vendor comparison around `.agents/skills/` (lane-owned,
S217–S222); "the last unheld page" (an inventory claim, not a page claim); a quoted TRAE sentence the page does not carry (`grep -c -F 'code logic'
using-scripts.md` → 0); the eval-design numbers that rest on S231 = the held S213; the staged `recheck` dates and byte counts.
**Rejected, with reason and flip** (Q62: each on an observed fact): (1) staged `spec-description-trigger-discipline.md`: its source row S231 is
`agentskills.io/skill-creation/optimizing-descriptions.md`, a URL the lane already holds as S213 (`grep -c 'optimizing-descriptions' corpus/SOURCES.md` → 2),
so appending it would add a W04 duplicate-URL row, and its three-way tension rests on TRAE and Chiba pages another lane's ground (translation) —
flip: a page of the specification that states a trigger rule S213 does not. (2) staged `skill-invocation-is-the-bottleneck.md` (S248 Vercel, S253
Anthropic): its substance is a measured non-invocation rate, kengaku's ground (measured capability effects) and the same refusal as round 72 for
S248/S254 — flip: a craft rule that cannot be stated without the figure. (3) Staged rows not appended: S231 (held as S213) and every other row of the
package; no admitted entry cites them (CORPUS rule 4).

**Quarantine** (`assimilation/quarantine-slice`, 13 data rows, re-derived; `w1/ExecQuarR74.md`, evidence `w1/build/ExecQuarR74/`): the register's
`S236`/`S237` are the campaign's per-round ids for `skills.sh/docs` and `skills.sh/audits`, **not** the package's using-scripts and quickstart rows
(F7 of `ReviewerPlanR74`; the plan's quarantine reading by id is struck in E1.4). Fresh fetches this round: 8 rows `adoptable`, 5 `refused` as quotes,
0 `unverifiable`; six verdicts differ from round 72's (`unverifiable` → `adoptable`, the sources fetch today). No quarantined row is cited by the
admitted entry, so none is appended. Of the round-68 refusal S168 (Vercel): the staged span `section:` is a heading-fold artifact and the page carries
the 56% sentence verbatim (HTTP 200, `ExecQuarR74`; round 72 had already corrected it) — recorded, not adopted.

**considerthese:** `considerthese/2026-10-25.md` § Self-improvement suggestions **item 4** worked: the SKILL.md intro said "the two harnesses here
show it differently" while the lane maps 7+ clients by documentation; `SKILL.md:24-25` now says the two harnesses this lane can observe (omp,
opencode) show it differently and 11 clients are mapped by documentation (11 — the distinct names of the seven client tables plus TRAE, CodeBuddy,
Kimi Code, Zhipu: `{ grep -oE '^\| (Claude Code|Codex|VS Code|Copilot CLI|Gemini CLI|Cursor|opencode) ' SKILL.md; grep -oE 'TRAE|CodeBuddy|Kimi Code|Zhipu'
PROVINCE.md; } | sed -E 's/^\| //; s/ $//' | sort -u | wc -l` → 11). Items 1, 2 and 5 stay open (item 2 is an L0 question since round 73; item 3 landed in round 72).

**Spot-check sample for the non-author closure (≥ 1 admit, ≥ 1 reject):** admit S225 (using-scripts: `snapshots/using-scripts.md:13`) and S224
(quickstart: `:21`); reject the staged `spec-description-trigger-discipline.md` (flip above) and the staged `skill-invocation-is-the-bottleneck.md`.
Also for the closure: the one judged classification change, **tsukuroi `none` → `adjacent`** (basis kotoba: `SKILL.md:127` and
`corpus/knowledge/hook-files-round59.md:20`), and the `SKILL.md` description clause it forced.

## Mistakes

| id | class | evidence | captured-by | fix |
|---|---|---|---|---|
| M134 | predicate contradicts its own binding | plan § C2 (e) (a whole-file `kotoba` clause) against (a) (the base checker's `none` rule reads the description and `PROVINCE.md` only): tabi's honest `none` row passed (a) and failed (e) (`w1/ScoutSibSoujiTabiR74.md` Finding 1; `w1/build/ExecSibCounterR74/` calibration: `19 of 20`, `FAIL: lane tabi`) | Q45 (target at or below the reachable population) — the plan's census covered C1 only; no seat counted C2's population under (e) before the freeze | E1.2 withdrew (e); the final counter prints tabi's body mention and does not count it; red-before = the draft counter at `w1/build/ExecSibCounterR74/check_sibling_reread.py` (tabi FAIL), green-after `20 of 20` (`receipts/c2-data-<rev>.txt`) |
| M135 | false premise in a control design | plan § C2: "quotes die at moved lines for the changed lanes" — measured false: all 20 round-49 quotes still locate at the same lines at the frozen heads (`w1/CriticClaimsR74.md` C2-2); a commit-bump alone scored 19 of 20, with the mechanical cells 20 of 20 | Q37 (the cheapest real-input shortcut is built and scored before the freeze) — I wrote the control by assertion and never ran it | `receipts/c2-carry-forward-<rev>.txt`: the carry-forward world (tsukuroi left `none`, evidence recomputed) scores **20 of 20** on the final counter — the counter measures the mechanical re-verification and the claim says so (`## Falsify corrections`, Q71) |
| M136 | no-harm line made red by the claim | plan § no-harm: "`check_sibling_census.py` on the r49 entry and `--province`" while C2 (d) re-pins `PROVINCE.md`: measured `province rows 20 matched 4`, exit 1 (`w1/ReviewerPlanR74.md` F1) | Q65 (a plan's no-harm battery is run at its post-state shape before it freezes) — run at base only | E1.3: the base checker runs on the r74 entry with `--province` and on the r49 entry without it; `receipts/noharm-<rev>.txt` |
| M137 | counter admits site chrome and error bodies | the frozen C1 predicate read `3 of 3` on worlds built from real page bytes: the documentation-index banner shared by all three pages (W2), the page subtitle (W5), a wrong registry id (W3), a token-stuffed action cell (W4) and a 404 body (W6) (`w1/CriticClaimsR74.md` C1-1…C1-4) | Q37 — the plan's control list held fabricated worlds and none of these real-text ones | E1.1 (a′)–(e′): page-unique tokens, quote line rules, digest in the anchor and the fetch log, filler list; each arm in `check_spec_craft.py --self-test` (250 assertions) reads exit 1 or 2 where the frozen predicate read 3 of 3 — `receipts/c1-selftest-freeze.txt` |
| M138 | a frozen claim counter's no-harm conjunct pins what a later legitimate claim rewrites | `verifiers/check_province_core.py` (round 69) requires `## Adjacent` byte-identical to `a5f7459f`; C2 re-pins that section by design: `province core rows 0 of 2`, finding `§ Adjacent differs from the base`, at `2c81137` and `559ee76` (`receipts/noharm-2c81137ba1a7888e9fe096e5f0c810221830fad7.txt`, `receipts/noharm-559ee76a9bcf3bccd374776a3ae5f0f1dcba47dd.txt`); found by `ConnOverlapR74` and the L1's first post-landing run, not by the plan | none — the guard is not in the tip battery and the plan's no-harm line did not name it | `ADJACENT_ERRATA`, an append-only sha256 ledger in the counter with a reason, plus two `--self-test` arms (a ledgered rewrite is accepted, an unledgered one still rejected; `python3 -B verifiers/check_province_core.py --self-test` → `0 failure(s) over 12 assertions`); red-before is the receipt above, green-after is `receipts/noharm-<final tip>.txt`; Q73 |
| M139 | data landed before the post-state gates ran | the first data commit `2c81137` read `gate registry rows conformant 58 of 60`, a checklist `trigger.citation_resolves` FAIL (`corpus/knowledge/chinese-vendor-skill-surfaces-round73.md:26,35-36` is not one resolvable token), a 1,027-character description (cap 1,024) and `corpus.pointers.commit_total` drift 42 vs 41; `559ee76` repaired them (`receipts/noharm-2c81137ba1a7888e9fe096e5f0c810221830fad7.txt` for the rev-based gate) | Q72 (this round's own row, written after the first landing) and Q65 — the plan's no-harm battery was run at base, never on the post-state shape before the commit | the gates now run in a plumbing sandbox commit before each landing (`/var/tmp` and `--shared --no-checkout` clones; the lane's `.ufo/` made `git checkout` impractical); Q72 names the command |

M134, M135 and M137 each had a criterion that should have caught them (Q45, Q37) and did not because the step was not run: the recurrence class is
"a criterion exists and a plan skips its mechanical step". QUALITY rows Q70–Q72 below name the commands (a census command, a built control, a post-state
no-harm run), not the principle.

## Routed defects (r73 spot-check § 6)

1. Falsify wave (second ask): wave 2 of this round, lane-unique seat names (`…R74`), total in the report.
2. Index the closure file in the first commit: done (`corpus/README.md` row, plan commit `329e7d9`); the corpus baseline re-recorded there.
3. D2/D3: SKILL.md at `1e03d19` is 570 lines — `git show 1e03d19:SKILL.md | wc -l`; the r73 M128 sentence "green-after … cited in the report" is corrected in
   the r74 report; `check_report_pointers.py` is run on the r74 report and its `unresolved 0` cited there.
4. M129 structural guard: **not built**; the r73 "fix" label for M129 is retracted — a fix counts once shown able to fail (CORPUS additional rules).
5. Fold r73 C1 into SKILL.md: one decision row (`SKILL.md:79-81`, cross-vendor `.agents/skills/` root) and the package path named in full.
6. `compare_harness_independent.py` exit 2: diagnosed, not a claim — `verify_harness_claims.py` prints `17/28 checks pass` because `verifiers/baseline.json`
   pins the round-18 catalogue of 7 skills as constants while the host offers 75 (216 cache rows) and the comparer then times out above 250 s
   (`plans/round-74.md` § Before-values); an L0 question is appended.
7. SHONEN boxes stay `[~]` (no non-author verifier is available to the lane).

## Falsify corrections

Filled from wave 2 (see the report); none before the wave settled.

## Status changes

S223, S224, S225 `mined` at landing (new rows). No other `status`, `recheck` or `used-by` cell changes.
