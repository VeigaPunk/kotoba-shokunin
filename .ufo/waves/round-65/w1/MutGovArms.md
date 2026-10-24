# MutGovArms — round-65 W1: GOVERNANCE_CORRECTIONS mutation probe

Seat: `MutGovArms` (mutation-tester, leaf). Scope: challenge the round-65 C2 claim
that the `GOVERNANCE_CORRECTIONS` mechanism is fail-closed, with **8 single-string
mutants** of `correction_problems` / its excusal filter in
`verifiers/verify_skill_checklist.py`, and either kill each with a landed
`--self-test` arm or name a new lane. **8 mutants run: 5 killed, 3 survived →
3 named lanes, each demonstrated to kill.** No repo byte outside this file was
written; no `git`/`jj` command was run; no package was installed (pacman paused,
nothing needed); no host service touched.

## 1. Isolation and detector

- Scratch: `/tmp/mutgov-r65-f70918f5/fleet/kotoba-shokunin`, an `rsync -a` copy of
  the lane tree (`.git`, `.jj` excluded so `DEFAULT_REPO` resolution is unchanged),
  with the fleet-root ancestry mirrored by read-only symlinks under
  `/tmp/mutgov-r65-f70918f5/fleet/` (needed for the `../` half of
  `citation_resolve`). `.git`/`.jj` were deliberately **not** mirrored: linking
  `.git` re-rooted `DEFAULT_REPO` one level up and made the pristine baseline red
  (observed, then corrected).
- Pristine target bytes = lane bytes:
  `sha256(verifiers/verify_skill_checklist.py) = 86d8b1584242ccaa096ac9a17e83be28c49e88a21c90bfb7b7ffddfa94bb25f1`
  (`cmp` against the lane file: identical; `LOG.md`, `SCORECARD.md` identical).
- Detector, same command on pristine / mutated / restored bytes, cwd = scratch repo:
  ```
  python3 -B verifiers/verify_skill_checklist.py --self-test   # kill battery
  python3 -B verifiers/verify_skill_checklist.py --json        # live end-state, context
  ```
  Every mutant is one contiguous string replacement, exactly one occurrence,
  `py_compile`-clean; pristine bytes are re-copied and sha-verified before and
  after every mutant.

### Baseline (pristine), actual output

```
$ python3 -B verifiers/verify_skill_checklist.py --self-test        # mirror
exit=0   0 failure(s) over 1862 assertions
$ python3 -B verifiers/verify_skill_checklist.py --self-test        # lane (host)
exit=0   0 failure(s) over 1862 assertions
$ python3 -B verifiers/verify_skill_checklist.py --json             # lane tip 0e104f49
exit=0   fail 0 pass 11
         PASS governance.citation_resolves | 1206 governance citation token(s) resolve
         across 2 files; 10 quoted meta-finding(s), 3 schematic token(s) excluded,
         1 recorded absence(s) excused, 3 recorded correction(s) excused
```
Baseline is green in mirror and lane, so a mutant failure is attributable to the
mutant (a baseline failure would have been inconclusive).

## 2. Results — 8 mutants

| # | single-string mutation | arm expected to kill | actual detector output | verdict |
|---|---|---|---|---|
| M1 | `elif not citation_resolve(corrected, repo):` → `elif False:` (skip corrected-token resolve) | "correction corrected token dead fails closed" | self exit 0, **no FAIL line**; json PASS | **SURVIVED → lane L-M1** |
| M2 | `if hashlib.sha256(...) != digest:` → `if False:` (skip line-sha pin) | "correction line drift fails closed" | self exit 1: `self-test FAIL: governance: correction line drift fails closed: got ('PASS', 1, …1 recorded correction(s) excused)` | **KILLED** |
| M3 | excusal filter keyed by `(source, line)` instead of `(source, line, token)` | none landed (nearest "never masks another dead subject" uses a *different* token) | self exit 0, no FAIL line; json PASS | **SURVIVED → lane L-M3** |
| M4 | bound `min(horizon, len(log_lines))` → `min(horizon + 1000, …)` | "correction past horizon fails closed" | self exit 1: `… got ('PASS', 1, …1 recorded correction(s) excused)` | **KILLED** |
| M5 | row unpack `… sline, stale, corrected` → `… sline, corrected, stale` | "pinned correction excuses the named stale subject" | self exit 1, 4 FAIL arms: pinned-correction, restored-token-stale, never-masks, live-round-65 (`names no live red subject` ×3); json **fail 1** | **KILLED** |
| M6 | excusal filter keyed by `token` only | none landed (nearest arm uses a different token) | self exit 0, no FAIL line; json PASS | **SURVIVED → lane L-M6** |
| M7 | `elif stale not in text or corrected not in text:` → `elif stale not in text:` | "correction wording fails closed" (needle `wording`) | self exit 1: `… got ('FAIL', 2, "… corrected token 'corpus/x.md' does not resolve; …")` — fails for the *wrong branch*, so the arm's needle assertion fails ⇒ killed by attribution | **KILLED (attribution)** |
| M8 | `elif citation_resolve(stale, repo):` → `elif False:` (skip stale-still-red) | "correction for a restored token is stale" | self exit 1: `… got ('PASS', 1, …1 recorded correction(s) excused)` | **KILLED** |

Mutated-byte shas (full, from `results.json`) and restoration:

```
M1 a2ccb80f359548647f420b58da03c0dcfe5bfa2df741c0ca0a69f27bdaae2719  restored exact true
M2 8318d62e2046c06c45c35b111a9b78b4cd7517d8d72182db24f6e1d0a0cd2883  restored exact true
M3 b8cf80a6b2e062839cedf4c7e87792cb6399394e715dea4e05f82d0aae2f88a2  restored exact true
M4 b16a471d8619bf554d6d531b0f8880b431b8b0c0c8a6c7d69ec742f4a65d6fe2  restored exact true
M5 9d0abd6ef51333c8c2a3974ff8155179230f7568f733f85eb18ab9c707107515  restored exact true
M6 b8b98806c9308e028c32cd2fd41f4d6c77c0dd2baacb13c086c013e72e218e25  restored exact true
M7 48e6382858445ada6dcfb1d60052401198f7b19f12f670c9a9da0dc1cac23dfb  restored exact true
M8 229cb48e5e239abad49e103aa3189c89df7559ef8f5ecd5e9d79e0b3df9ba613  restored exact true
```

`M7` note: the mutant still exits 1, but at the *corrected-token* branch instead
of the wording branch, so the landed arm's needle (`wording`) is absent and the
arm fails. That is a kill by attribution only — the wording guard itself is not
independently pinned by the arm's expected string.

## 3. The three survivors are equivalence-breaking, not equivalent mutants

Witnesses (`witness.py`, module imported by path; fixtures under temp dirs; a
live subject `corpus/live.md` keeps `evaluated > 0`):

```
### W1 (M1) notice names a dead corrected token, on the notice line
pristine -> FAIL (2) correction LOG.md:2 SCORECARD.md:1 'corpus/gone.md':
            corrected token 'corpus/absent-xyz.md' does not resolve; …
M1       -> PASS (1) … 1 recorded correction(s) excused
### W3 (M3) a second dead token sits on the excused line
pristine -> FAIL (2) SCORECARD.md:1: 'corpus/dead-two.md' does not resolve …
M3       -> PASS (1) … 1 recorded correction(s) excused
### W6 (M6) the excused token recurs, dead, on another line
pristine -> FAIL (2) SCORECARD.md:2: 'corpus/gone.md' does not resolve …
M6       -> PASS (1) … 1 recorded correction(s) excused
```
Each mutant accepts a defect the landed bytes reject, so all three are genuine
coverage gaps (S121's non-equivalent class), not redundant mutants.

### Why M1 survives — reproduced at branch level

The landed arm was labelled `("corrected token dead", crow[:5] + ("corpus/absent-xyz.md",), 2, "does not resolve")`
but its notice line is `… "corpus/gone.md" -> "corpus/live.md" (round-65 notice).`,
which does **not** contain `corpus/absent-xyz.md`. The wording branch fires first;
the needle `does not resolve` is then satisfied by the trailing re-scan of the
still-red stale subject. Reproduced against pristine and M1 with the arm's exact
fixture:

```
pristine -> FAIL 2 | branch: wording-branch
  correction LOG.md:2 SCORECARD.md:9 'corpus/gone.md': correction wording not on
  the line; SCORECARD.md:9: 'corpus/gone.md' does not resolve …
M1       -> FAIL 2 | branch: wording-branch   (identical)
```
So the landed arm labelled "corrected-token-does-not-resolve" never exercises the
`not citation_resolve(corrected, repo)` guard: it is satisfied by an unrelated
residual string. The guard's only *reachable* witness is one where the corrected
token is on the notice line (W1), which the battery does not have.

### Named new lanes (arm text as built and run)

All three inserted inside the governance fixture block of `self_test()`, after
the "live round-65 corrections land" arm; fixture `gov_repo`, `log_path`,
`scorecard` reused, `log_path`/`scorecard` rewritten:

```python
        # L-M1: dead corrected token ON the notice line
        log_path.write_text("`corpus/live.md`\n"
                            "SCORECARD.md:9 token \"corpus/gone.md\" -> "
                            "\"corpus/absent-xyz.md\" (round-65 notice).\n")
        scorecard.write_text("padding line\n" * 8 + "`corpus/gone.md`\n")
        notice = log_path.read_text().splitlines()[1]
        dead_fix = (2, sha256(notice), "SCORECARD.md", 9,
                    "corpus/gone.md", "corpus/absent-xyz.md")
        status, evaluated, detail = check_governance_citations(
            gov_repo, errata=(), corrections=(dead_fix,), corrections_horizon=2)
        rec("governance: correction with a dead corrected token is rejected, "
            "not excused",
            status == "FAIL" and "corrected token" in detail, (status, evaluated, detail))

        # L-M3: a second dead token on the same line survives the excusal
        … row good = (2, sha256(notice), "SCORECARD.md", 9, "corpus/gone.md", "corpus/live.md")
        scorecard.write_text("padding line\n" * 8
                             + "`corpus/gone.md` `corpus/dead-two.md`\n")
        rec("governance: correction excuses only its named token on the line",
            status == "FAIL" and "corpus/dead-two.md" in detail, …)

        # L-M6: the excused token stays red on another line
        scorecard.write_text("padding line\n" * 8 + "`corpus/gone.md`\n"
                             "`corpus/gone.md`\n")
        rec("governance: correction excuses only its named line for the token",
            status == "FAIL" and "SCORECARD.md:10" in detail, …)
```
(`sha256(notice)` = `hashlib.sha256(notice.encode("utf-8")).hexdigest()`; the
exact runnable block is `/tmp/mutgov-r65-f70918f5/armed.py`, `ARMS`.)

### Armed-battery kill matrix (measured, `armed-results.json`)

Armed pristine (pristine + the 3 lanes): `exit=0  0 failure(s) over 1865 assertions`
(1862 + 3 — the lanes are additive, no landed arm disturbed).

```
M1 -> exit 1  fired: correction with a dead corrected token is rejected, not excused
M2 -> exit 1  fired: correction line drift fails closed
M3 -> exit 1  fired: correction excuses only its named token on the line
M4 -> exit 1  fired: correction past horizon fails closed
M5 -> exit 1  fired: 5 arms (pinned-correction, restored-stale, never-masks,
                      live-round-65, dead-corrected-token)
M6 -> exit 1  fired: correction excuses only its named line for the token
M7 -> exit 1  fired: correction wording fails closed
M8 -> exit 1  fired: correction for a restored token is stale
RESTORED: exit=0  0 failure(s) over 1862 assertions  sha=86d8b1584242ccaa…
```
With the three lanes, the mechanism is **8/8 mutant-complete** for this probe set,
and each survivor dies by the arm named for it (exactly one failure each).

## 4. Live relevance of the three gaps (calibration)

Measured on the lane's own governance files with the pristine module:

```
subjects (after quoted/schematic exclusion): 1210
(source, token) pairs repeated within one file: 202
(source, line) carrying > 1 subject: 258
'.ufo/reports/round-60/kotoba.md' dead at: [('LOG.md', 2533), ('SCORECARD.md', 158)]
'.ufo/watchdog.log'             dead at: [('LOG.md', 2580)]
```
- L-M6 is not hypothetical: the token `.ufo/reports/round-60/kotoba.md` is dead on
  **two** lines in **two** files, currently covered by **two** separate rows
  (LOG.md:2619, SCORECARD.md:2621). Under M6 either row would excuse both — the
  exact "one notice masks the other filename's red cell" failure the mechanism
  exists to prevent. [INFERENCE] It is dormant today only because both cells were
  corrected in the same round.
- L-M3 has 258 live lines it would over-excuse; today each of the three corrected
  lines (LOG.md:2533, LOG.md:2580, SCORECARD.md:158) carries exactly one subject,
  so M3 is dormant on current bytes.
- L-M1 is dormant on current bytes (all three corrected tokens resolve); it is the
  fail-open shape that would hide a typo in a future correction.
- None of M1/M3/M6 changes today's verdict: `--json` stays `fail 0` (so the live
  end-state claim is untouched); M2/M4/M7/M8 likewise stay `fail 0`; M5 makes the
  live check FAIL (`fail 1`, `0 recorded correction(s) excused`) — a second,
  independent kill channel for M5.

## 5. Claims supported / falsified

- **Supported:** C2's landed guards for *line-sha drift*, *horizon*, *row token
  order*, *wording presence*, and *stale-must-still-be-red* are each pinned by an
  arm that actually fails on the mutated bytes (M2, M4, M5, M7, M8).
- **Supported:** the live mechanism is correct on today's bytes — lane tip
  `0e104f49` reproduces `fail 0`, 11/11,
  `1206 … 3 recorded correction(s) excused`; self-test `1862` assertions, exit 0.
- **Falsified (strong reading of C2's "self-test arms (each shown able to fail)"):**
  the corrected-token-resolve guard is **not** shown able to fail by the landed
  battery — the arm carrying that label fires the *wording* branch and its needle
  is satisfied by an unrelated residual scan (reproduced, §3). 3 of 8 probed
  guards are unpinned: corrected-resolve (M1), excusal-key narrowness by line
  (M3), excusal-key narrowness by token (M6).
- **Not falsified:** the live `GOVERNANCE_CORRECTIONS` rows are correct as landed;
  every survivor is a kill-power finding, not a red cell. No contract change
  follows from it.
- Attribution caveat inherited from `RevReceiptRevs` F4: this probe measures
  kill-power at the mirrored location; the *green* end-state is location-bound,
  which is why the mirror reproduced `1862`/`11/11` before any mutant ran.

## 6. Sibling scan (overlap check, read-only)

- `.ufo/waves/round-65/w1/MutNewLanes.md`: no `correction`/`GOVERNANCE_CORRECTIONS`
  lane (grep: no match) — the three lanes here are new.
- `.ufo/waves/round-65/w1/RevReceiptRevs.md`: flags C2 rev-attribution and
  location-binding (F2/F3/F4), not arm sensitivity — complementary, no conflict.

## 7. Restoration evidence

- Per mutant: pristine re-copied before, sha verified (`86d8b158…`), mutated sha
  recorded, pristine re-copied after, sha equal to pristine every time
  (`restored_exact: true` ×8, `results.json`).
- After the battery: `--self-test` on restored bytes `exit=0  0 failure(s) over
  1862 assertions  sha=86d8b1584242ccaa…`; `--json` `fail 0`.
- Lane file never touched: lane
  `sha256(verifiers/verify_skill_checklist.py) = 86d8b1584242ccaa096ac9a17e83be28c49e88a21c90bfb7b7ffddfa94bb25f1`
  before and after; mtime unchanged (Oct 24 03:00). No `git`/`jj` invocation.

## 8. Reproduce

```
# scratch (kept): /tmp/mutgov-r65-f70918f5
cd /tmp/mutgov-r65-f70918f5/fleet/kotoba-shokunin
python3 -B verifiers/verify_skill_checklist.py --self-test   # 0 failures / 1862
python3 /tmp/mutgov-r65-f70918f5/probe.py     # 8 mutants -> results.json
python3 /tmp/mutgov-r65-f70918f5/witness.py   # 3 survivor witnesses
python3 /tmp/mutgov-r65-f70918f5/armed.py     # 3 lanes -> 8/8 killed, armed-results.json
```
Assertion counts: landed `1862`; armed (landed + 3 lanes) `1865`. If the lanes are
adopted, the floors/registry bump must move `1852 → 1862` to `→ 1865` in step
(bump-in-step rule); that sizing is a lane decision, not taken here.

**Tooling:** none installed or upgraded; pacman not invoked (host pause respected).

**Report:** `.ufo/waves/round-65/w1/MutGovArms.md`
