author: hyaku closure (non-author integrator, @m_zfl)

# kotoba round 86 — verifier spot-check (non-author closure)

Closure judge: hyaku closure, fresh session, did not author this round. Lane repo
`/home/vgpnk/Projects/shokunin/kotoba-shokunin` (branch `master`, jj-colocated, git HEAD
detached at the branch commit). Base `e5d966b51494f4177868ad5f46806a204783ef6c` → lane tip
`4212b6930fa2a424b2c794ab9724384c4f93b7b4`. Method: index-free git (`rev-parse`,
`cat-file`, `show`, `ls-tree`, `diff`, `merge-base --is-ancestor`, `ls-remote`), the
`jj-lane.sh state` helper (pure git, read-only), plain counting over committed bytes, one
`mmap` re-open of the installed ELF, one live HTTP re-open, and an independent host census.
No lane-authored file was edited; no sibling gate was executed — gate claims were verified
from their committed evidence per `PROTOCOL.md` § Gate standard (Closure consequence).

## 1. Conformance results

| Check | Command | Observed | Result |
|---|---|---|---|
| Report committed by the lane identity | `git -C <fleet> log --format='%an %H' -- .ufo/reports/round-86/kotoba.md` | `kotoba-shokunin 4932e3c66de042a5ca9a1f990264747e44ad9397` (pointer fix) and `kotoba-shokunin dec29519383c8d0141104b35435903bbf57b1786` | PASS |
| Report lands last | commit times | lane tip `4212b69` 2026-11-04 19:46:10 -0300; report commits 19:46:42 / 19:47:26 (later) | PASS |
| `SHONEN` heading, one line per box | `grep -c '^## SHONEN'`; box-line count vs `SHONEN.md` | `1`; four `[~]` lines with pointers; `SHONEN.md` carries exactly four boxes | PASS |
| Cited commits exist and are ancestors of the branch | `git cat-file -t <h>` + `git merge-base --is-ancestor <h> master` for `e5d966b ecfad51 b9ee548 04647b0 99c2174 4212b69` | all six resolve as commits; `ancestor=yes` for all six; every 40-hex hash in the report is in this set | PASS |
| Lane pushed, no leftovers | `jj-lane.sh state <lane>`; `git status --porcelain` | `ahead=0 behind=0 tracked=0 untracked=0`; porcelain empty | PASS |
| Remote equals local tip | `git ls-remote origin refs/heads/master` | `4212b6930fa2a424b2c794ab9724384c4f93b7b4` = local `master` | PASS |
| Prompt carries the template contract | `.ufo/prompts/kotoba-round-86.md` (830 lines, commit `dc1fd024`, kotoba identity); line-by-line against `templates/round-prompt.md` | 105 non-placeholder template lines, **0 missing**; no unfilled `{{…}}`; §1, §2, §2b, §3, §4, §5 plus the §6 hyaku addendum; §3 L2 floor "≥8 in ONE batched AgentSwarm call" matches `MISSION.md` §L2; no model alias hardcoded | PASS |
| L2 floor and seat mix | `r86-w1-results.json`; `w1/` | 13 rows: scout 2, executor 1, scribe 3, connector 1, reviewer 2, critic 1, mutation-tester 1, sentinel 1, revenger 1; strict attack set (reviewer/critic/mutation-tester) = 4/13 = 30.8 % ≥ 25 %; connectors 1 (≤2) | PASS |
| Wave settlement | `w1/*.md` + `w1/<seat>/*.md` | 13 seat reports present (12 at `w1/*.md`, `w1/MutTester/MutTester-2/` inside its dir); WAVE-DONE marker committed with provenance; `output: null` on all 13 rows, disclosed | PASS |
| Round work range | `git diff --shortstat e5d966b 4212b69` | `184 files changed, 24143 insertions(+), 61 deletions(-)` | PASS |
| Append-only files held | `git diff --numstat e5d966b 4212b69 -- LOG.md SCORECARD.md corpus/lessons/round-85.md corpus/lessons/round-86.md corpus/SOURCES.md corpus/README.md corpus/QUALITY.md` | `61 0`, `26 0`, `33 0`, `186 0`, `1 0`, `5 0`, `2 0` — no deletions | PASS |
| `SHONEN.md` / `PROVINCE.md` untouched | same diff | neither path appears | PASS |
| Deletions are intended only | `git diff --numstat … \| awk '$2>0'` | only `SKILL.md` (1, registry row replaced), `verifiers/corpus-baseline.json` (re-record), `verifiers/verify_harness_claims.py` (52, the preview fix) | PASS |
| Stale-lane duty | `.ufo/watchdog.log` digest (mutable; copied): `2026-11-04T18:49:04-03:00 launch kotoba round=86 pgid=1366877 driver=hyaku-inline attempt=1`; `2026-11-04T19:48:17-03:00 complete kotoba round=86; hyaku-inline attempt=1`; no `lane-dead-no-report` line for round 86 | one mission, progressing, no respawn; no other kotoba mission open | PASS |
| Misroot sweep | `git -C <fleet> status --porcelain \| grep -i kotoba` | nothing; the modified `.ufo/reports/round-84/kama.md`, `.ufo/l0-questions.md`, `.scratch/*` and untracked `after` belong to other actors | PASS |
| L0 side channel | `grep -nE 'kotoba *\| *round-86' .ufo/l0-questions.md` | `0` new lines; cited open items `round-73` (:174) and `round-82` (:219, :249) resolve | PASS |

Status: `ok`. Defects are listed in §6 and are status-neutral.

## 2. Claim re-check

One claim, C1 **freshness** (tied-lowest non-retired axis with adjacency, both 8). The claim
rests on a lane-owned gate, so its verdict is **evidence-verified, not executed**
(`PROTOCOL.md` § Gate standard, Closure consequence). Before→after was additionally
**re-derived by plain measurement of committed bytes and of the live host**.

### C1 — freshness — **improved**

Reported: base `83 of 215`, G4 FAIL, exit 1 → landing `04647b0` `215 of 215`, G1–G4 PASS,
exit 0; target N ≥ 205.

| Step | Command | Observed |
|---|---|---|
| Before, from committed bytes | `git show e5d966b:verifiers/verify_harness_claims.py \| sed -n '60,69p'` | four `USER_ROOTS` (`.agents/skills`, `.omp/agent/skills`, `.config/opencode/skills`, `.claude/skills`), dated 2026-09-28; **no** omp plugin root |
| Before, independent census of the live host | `python3`: basenames under `~/.agents/skills/*` and `~/.omp/plugins/node_modules/*/skills/*`, intersected with the 215 fixture names | `agents skills dirs 83`; `plugin skill dirs 132`; catalogue names in agents **83**; in plugins **132**; union **215**; unresolved **0** |
| Fixture integrity | `python3 -c` over `verifiers/fixtures/omp-catalogue-r86/catalogue.json` | `entries` 215 (215 distinct names), `cache_rows` 228; `git show <rev>:… \| sha256sum` = `0b3443e1058fffa75a287faca7d839d4bbfa3b7cd6f672783e1b0e70d714b488` at `ecfad51`, `b9ee548` and `4212b69` (unchanged) |
| After, independent render account | `python3`: for each of the 215 names, `preview(frontmatter description)` vs the fixture render, else membership in the captured cache set | 215/215 SKILL.md found under the two roots; **133** renders equal the file's own preview; **82** are present verbatim in the committed cache set; **0** unexplained |
| Gate evidence — self-test tally | `.ufo/waves/round-86/receipts/c1-counter-selftest-a1.txt` (`sha256sum` = `45bfe56b…f5fb`, matching the lesson table) | `0 failure(s) over 46 assertions`, `exit=0`, counter sha256 `39a014f2…4520` printed in-receipt |
| Gate evidence — frozen-run verdict | `.ufo/waves/round-86/receipts/c1-after.txt` at `04647b0` | `guard G1 no-echo PASS`, `G2 provenance PASS`, `G3 fixture PASS`, `G4 roots PASS`, `omp catalogue lines reproduced 215 of 215`, `exit=0` |
| Gate evidence — revision measured | `git diff --stat 04647b0 4212b69 -- verifiers/verify_harness_claims.py verifiers/omp-skill-roots.tsv verifiers/check_omp_catalogue_repro.py verifiers/fixtures/` | **empty** — the scored model, counter and fixture are byte-identical from the landing commit to the tip, so the landing reading carries to `4212b69` |
| Counter/fixture pins at both revisions | `git show <rev>:verifiers/check_omp_catalogue_repro.py \| sha256sum` | `39a014f2f3142096b43031faedb0ea9819995fb2926138c3ebf2b194002e4520` at `b9ee548` **and** at `4212b69`; original freeze `ecfad51` = `2390eec2…6514` |
| Control receipts unaltered | `sha256sum .ufo/waves/round-86/receipts/c1-*.txt` | all eleven digests equal the lesson's table (`ec418646…`, `0397427a…`, `cfdfa951…`, `ea77630f…`, `cd66a106…`, `64297079…`, `39db3422…`, `2076b9a0…`, `5cef9c3d…`, `45bfe56b…`) |
| Base reading, plain count | `grep -c '^MISS' …/c1-K0-base-a1.txt`; `grep -c 'not-discovered' …`; `grep -c 'render-differs' …` | `132`; `132`; `0` — every modelled line was right and the 132 misses are `not-discovered` |
| False-green bound is real | `.ufo/waves/round-86/receipts/c1-K3-critic-wild-a1.txt` tail | `guard G4 roots FAIL (216): ledger line 2: quote does not name '.zcode' …`, `215 of 215`, `exit=1` — the F1 world is refused by the amended counter, and the report says so |

Verdict: `improved`. The before→after is real on two independent measurements (the lane's
frozen counter at the landing revision, and my own census: 83 names under `~/.agents/skills`
plus 132 under the one omp plugin root, union exactly 215, nothing reached through a root omp
does not read). The number alone is **not** offered as the evidence: post-data worlds that
read no omp source reach the target (Critic-2 F5, MutTester-2 / Sentinel-3 F6), so the
semantic half rests on the non-author ELF review `w1/ReviewerRoots/review.md` (`C1 roots:
sound`) and on this check. The `preview` fix (`o >= E` last-space rule, absent from the base
model) is a genuine correctness delta against the ELF quote, not a cosmetic one.

### Ruling on the kill-rule clause (requested by the lane)

`plans/round-86.md` § Kill rule reads: "… the counter, its fixture or its pins changed after
this freeze …". Addendum 1 (`b9ee548`) changed the counter after the freeze commit
`ecfad51`. **Ruling: admissible, not a kill.** Basis, each verifiable:

1. The freeze's own stated boundary is *candidate data*: the plan heads it "Freeze committed
   before any candidate data", the addendum is titled "before any candidate data", and the
   kill paragraph's purpose clause is "No narrowing of the target after data".
2. No candidate was scored before the amendment: `git diff --stat e5d966b b9ee548 --
   verifiers/verify_harness_claims.py` is **empty** (the candidate model is byte-identical to
   the base at the addendum commit), and the ExecModel artifacts first appear at `99c2174`.
3. The amendment left the predicate sentence, the 215 total, the 205 target and the fixture
   sha256 unchanged; it **tightened** G4 (dot-directory rule), the sandbox (allowlist,
   `--unshare-*`, `--clearenv`) and added parent-side re-derivation. It cannot have rescued a
   failing candidate (none existed) and cannot have widened the target.
4. The amendment shipped its own re-run controls (self-test 34 → 46 assertions, K0–K4, K4
   sandbox probe) and a documented HOLD on ExecModel.
5. The lane disclosed the conflict verbatim in the lesson and the report and assigned the
   ruling here, rather than self-attesting it.

Residual risk, named for the operator: a literal reading of "after this freeze" would make
C1 an honest stop. I did not take that reading because the clause's function is to bind the
instrument against post-data manipulation, and the record shows none. The precedent the lane
cites (`plans/round-74-addendum-1.md`) is a principle, not an identity: round 74's addendum
was errata with the counter sha unchanged. Routed in §6.

## 3. Spot-check table (discernment, `LEARNING.md`)

The round's `## Gate` records one admit (S255) and **no reject** — a round with a single
candidate that cleared the bar has no rejection to log, so the reject sample was taken from
the round's other recorded gate decision, the non-author roots review, which rejects three
ledger citations with reasons. Every row was re-opened at its own source.

| # | item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|---|
| 1 | **S255** — omp 18.15.0 TypeScript embedded in the installed ELF, tier A, `mined`, opened 2026-11-04 (new `corpus/SOURCES.md` row, 1/0) | **admit** | `mmap` of `/home/vgpnk/.local/bin/omp` (sha256 `6737ee24…b7b0f`, 276 785 328 B, `omp --version` = `omp/18.15.0`) at byte offset **178770368**; upstream `raw.githubusercontent.com/can1357/oh-my-pi/v18.15.0/packages/coding-agent/src/extensibility/skill-descriptions.ts` | **agree** | the row's ≤25-word quote `const c = o >= E ? r.slice(0, o).trimEnd() : r;` is verbatim at the stated offset (11 tokens, 1 occurrence in the ELF); the module header `// packages/coding-agent/src/extensibility/skill-descriptions.ts` is at 178767936 (2 occurrences, as the lesson states); upstream re-open: **HTTP 200, 16 687 B, sha256 `7321adfc…f6ee`** — exactly the row's figures, with `MIN_PREVIEW_CUT` present |
| 2 | **roots-ledger row 9** (`~/.omp/plugins/node_modules/*/skills`) — citation `var Gh = ".omp";` | **reject** (ReviewerRoots: "located but irrelevant") | ELF offset **166884553**; sweep for `.omp/plugins` and `omp/plugins`; sweep for the code that reads the root | **agree** | the quote is the bare config-dir constant (`var Gh = ".omp"; var dg = ["config.yml", …]`) — no `plugins`, no `node_modules`, no `skills`; the ELF contains **0** occurrences of `.omp/plugins` and **0** of `omp/plugins`, so no code quote can satisfy G4's dot rule for this row (root cause confirmed); the real reader is `dir: Zo.join(R.path, "skills"),` (1 occurrence). The *root* is sound — I measured its 132 catalogue names myself — so the rejection of the citation is right and the root verdict stands |
| 3 | **roots-ledger row 1** (`{cwd}/.omp/skills`) — citation `Native OMP configuration from ~/.omp and .omp/` | **reject** (ReviewerRoots: "located but irrelevant") | ELF string table | **agree** | the string occurs 2× and is the native provider's generic description; it never mentions skills or a `.omp/skills` walk-up, so it grounds the provider but not the root |
| 4 | S255 `used-by` resolution (census) | **admit** | `bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` | **agree** | `exit=0`, last line `kotoba ok …/corpus/SOURCES.md`, `33` `W04` warnings, **0** `E` rows — S255's `used-by` paths exist |

Agreement: 4/4 (1 admit, 1 reject, plus a quote and a census check). No disagreement.

## 4. Per-axis verdicts

| Axis | Verdict | Evidence |
|---|---|---|
| depth | `unchanged` | additive only: knowledge entry `corpus/knowledge/omp-catalogue-model-round86.md` (182 lines), SKILL.md 2/1 (registry row + render note); no depth score move claimed; score 9 held |
| consistency (calibration sub-axis) | `unchanged` | gate registry `66 of 67` at `04647b0` → `67 of 67` at `4212b69` by the pinned-values cell fix (`git show 99c2174:SKILL.md \| sed -n 522p` vs `4212b69`); score 10 held; my own count: 67 registry rows ↔ 67 lane verifier artifacts (66 `.py` + `fault_injection_corpus.sh`), 0 phantom |
| coverage | `unchanged` | no new coverage-map ground admitted; the round-86 note is an append-only advance on the existing loader-rule row (`corpus/README.md:263`); PROVINCE untouched |
| operability | `unchanged` | the counter is the claim's instrument, not a capability row (`capabilities_added` empty); no checklist item made executable |
| freshness | `improved` | `83 of 215`, G4 FAIL, exit 1 → `215 of 215`, G1–G4 PASS, exit 0; independently corroborated (83 + 132 = 215 at the two roots omp reads); the `o >= E` preview deviation fixed |
| calibration | `unchanged` | self-assessment is unusually honest (F5/F6 bounds, Q71/Q74 disclosure, kill-rule conflict handed to the judge), but two record defects remain (§6.1, §6.2); no calibration score move |
| adjacency | `unchanged` | `PROVINCE.md` untouched; `check_sibling_census.py … --province PROVINCE.md` receipt `20 matched 20`, `10 of 10`; Connector's no-absorb line (the `~/.omp/agent` inventory and the `.agents/skills` symlink provenance belong to kumitate) honoured |

No axis is `harmed`. Every deletion in the round diff is intended (registry row replaced,
baseline re-recorded, preview function fixed).

## 5. Trend verdicts

- **expansion — `improved`.** One tier-A `mined` row added (S255, `corpus/SOURCES.md` 180 →
  181 rows, `git diff --numstat` = `1 0`), one frontier row advanced (`corpus/README.md:263`),
  and the lane's model now governs a root class it never held — the omp plugin root, 132 of
  the 215 catalogue lines. S255 is also a new *kind* of source for this lane: code read in
  place out of an installed binary by `mmap`.
- **quality — `improved`.** The loader-rule entry was re-verified and superseded by a stronger
  one: reproduction moved 83 → 215 of 215 and a real deviation from omp's `o >= E` rule was
  fixed. No admitted entry was found false or stale and left unmarked; the one known stale
  surface (`verify_harness_claims.py` main mode, `16/28` on round-13 expectations) is
  unchanged before and after (`w1/ExecModel/cli-base.txt` vs `cli-after.txt`) and is carried,
  not hidden.
- **discernment — `improved`.** Three attack seats falsified the lane's own frozen counter
  **before data** (F1 `*` ledger row + unread root, F2 request dumps readable in the sandbox,
  F3 encoded answer key); the lane amended with an addendum, a HOLD and re-run controls
  instead of self-attesting a pass, and reported two post-data doors (F5, F6) as bounds on
  the claim rather than patching the instrument after data. `QUALITY.md` gained Q77 from
  M86-1, shown able to fail at base (`83 of 215`). This spot-check agrees on 4/4 sampled
  decisions.

## 6. Routed defects (status-neutral; the lane's next round)

1. **Tip after-values without a committed receipt (r85 D2 recurrence).** The report's C1
   table rows for tip `4212b69` (`215 of 215`, registry `67 of 67`) say "re-run at report
   time" and cite no receipt; `.ufo/waves/round-86/receipts/tip-remeasure.txt` (committed at
   `4212b69`) carries the `99c2174` runs only — including `66 of 67`, `exit=1`. Both values
   are corroborated here (model/counter/fixture byte-identical `04647b0` → `4212b69`; 67
   registry rows ↔ 67 verifier artifacts), but the lane's own evidence chain has the gap r85
   D2 named. Fix: commit a `--rev 4212b69` receipt for the counter and the registry gate.
2. **Planner seat not dispatched, reason unverified.** `.ufo/prompts/kotoba-round-86.md` §3
   requires `1× planner`; the wave ran 13 seats with none, the L1 holding the duty. The
   report's reason ("the validator rejects `planner`") is not confirmed here:
   `scripts/hyaku/ufo-wave-policy.json` and `…-v2.json` both carry a `planner` role. Fix:
   either dispatch the seat or cite the rejecting validator and its error verbatim.
3. **`## Gate` carries no reject row.** The section records the S255 admit and no rejection,
   so the round's rejections (ReviewerRoots rows 1/8/9, the K3 world) live only in seat
   reports. `CORPUS.md` § Layout asks the Gate section for "candidates, admitted, rejected
   with reasons". Fix: record the round's rejections in `## Gate`, not only in `w1/`.
4. **Kill-rule wording does not name the data boundary.** "the counter, its fixture or its
   pins changed after this freeze" forced a judicial reading (this §2 ruling). Fix: state the
   boundary as "changed after the first candidate score", so a pre-data addendum is
   conformant by construction.
5. **The r85 precedent cited for the addendum is weaker than claimed.** `plans/round-74-addendum-1.md`
   amended the *plan* (errata), not the counter — the round-74 counter sha256 is identical in
   both freeze receipts. Fix: cite the principle ("amended before any data") or name a
   precedent where the instrument itself changed pre-data.
6. **Counter holes confirmed and carried, not patched** (agrees with the report): G4 checks
   quote location, not meaning (CF1 — no code quote can satisfy the dot rule for the plugin
   root); `{cwd}/` expands to every ancestor including `$HOME` (CF2); the sandbox hides the
   plugin registry files, so the scored branch is the model's non-omp fallback, not the
   registry branch (CF3/P4); `/run/docker.sock` reachable in the sandbox (Sentinel S4);
   15 of 26 counter mutants survive the self-test. The round-87 items the report already
   routed (normalise roots before matching, forbid `..`, per-root code quotes, hide the
   sockets, add self-test arms for the sandbox flags / G3 total / rebind list, bind the
   plugin registry files) are the right fix list — carried as the queue of record.
7. **Carried base reds, not new harm** (recorded for the aggregator ledger):
   `verify_corpus_integrity.py` `8/9` with `corpus.pointers.commit_unresolvable 1` at
   `corpus/lessons/round-81.md:8`; `verify_skill_checklist.py`
   `governance.citation_resolves` FAIL (1 470 evaluations, `+9 more`); both present in the
   round-85 record (`corpus/lessons/round-85-verifier-spotcheck.md:90-91`,
   `.ufo/waves/round-85/receipts/before-gates.txt:27`).

## 7. Verdict

C1 freshness **improved**, independently corroborated; no axis harmed; discernment 4/4
agree. Round 86: **admitted**.
