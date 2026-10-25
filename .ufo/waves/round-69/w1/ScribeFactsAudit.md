# Scribe facts audit — round 69 wave 1 (kotoba, hyaku run 6, attempt 2)

Seat: `L1Kotoba69-2.ScribeFactsAudit`. Date: 2026-10-25. Lane root:
`/home/vgpnk/Projects/shokunin/kotoba-shokunin`.

Scope: verify the countable facts the round report will claim, against the lane alone. Nothing
here is a claim about intent or quality; every value below comes with the command that produced
it. Lane files were not modified; the only writes are this report and the `/tmp` sandbox named in
§5. No installs, no package transactions. At most two processes ran at once.

## 1. The four enumerated measurements

### (1) `git status --porcelain` — round-68 and round-69 paths

Command: `git -C ~/Projects/shokunin/kotoba-shokunin status --porcelain`

- Total lines: **42** (17 ` M`, 25 `??`).
- Round-68 wave paths: **24** — exactly the frozen count, and exactly the composition the plan
  states: **10 modified** (`.ufo/waves/round-68/w1/drafts/check_client_trust_gates.py` + the nine
  `logs/*.log` in `CriticC1Predicate`, `CriticC2Predicate`, `ExecC1CounterTest`, `ExecC1Fetch`,
  `ExecR67Repairs`, `MutC1Counter`, `MutR67Repairs`, `ReviewC1Entry`, `ScribeC2Index`) and
  **14 untracked** (7 seat reports `.md`, `controls/c2falsify-clone/`, `controls/c2falsify2.py`,
  4 `drafts/*`, `seat-results.json`).
- Round-69 wave paths: **9 untracked** under `.ufo/waves/round-69/` — `assimilation/append-block.md`,
  `assimilation/entry-draft.md`, `assimilation/validate-census.txt`, `assimilation/validate/`,
  `recapture/`, `w1-dispatch.err`, `w1-dispatch.json`, `w1-spec.json`, `w1/`.
- Remaining 9 lines are round-69 content draft: ` M PROVINCE.md`, ` M SKILL.md`,
  ` M corpus/QUALITY.md`, ` M corpus/README.md`, ` M corpus/SOURCES.md`,
  ` M corpus/knowledge/client-trust-gates-round68.md`, ` M verifiers/check_r67_routed_repairs.py`,
  `?? corpus/knowledge/skill-name-precedence-round69.md`, `?? corpus/lessons/round-69.md`.
- 24 + 9 + 9 = 42, so no status line is unaccounted for.
- The clone carries its own `.git` (`test -d .ufo/waves/round-68/w1/controls/c2falsify-clone/.git`
  → yes) and `du -sh` → **269M**.

### (2) `corpus/SOURCES.md` line count and the census

- `wc -l corpus/SOURCES.md` → **353** (at base `a5f7459`: `git show a5f7459:corpus/SOURCES.md | wc -l`
  → **347**).
- Registry rows `^\| *S[0-9]{3}` → **134** now, **128** at base: **+6** rows, and the added ids are
  exactly `S203 S204 S205 S206 S207 S208` (`git diff -U0 corpus/SOURCES.md | grep -cE '^\+\| *S[0-9]{3}'`
  → 6). Five are the C1 clients; `S208` is the D5 supersede row.
- Census before, per the committed control `.ufo/waves/round-69/controls/census-before.txt`:
  **16** `W04` lines, `exit=0`, `measured-rev: a5f7459f…`, run as
  `scripts/sources-census.sh validate --root … kotoba`.
- Census now, run read-only on the lane file:
  `scripts/sources-census.sh validate --file …/corpus/SOURCES.md` → **18** `W04` lines, `exit=0`.
  The two new warnings are this round's rows: `S207 duplicate url opencode.ai/docs/skills`
  (the URL already appears as `S024`, `S039`) and `S208 duplicate url
  learn.microsoft.com/en-us/agent-framework/agents/skills` (same page as `S201`, which S208
  necessarily supersedes). `W04` is non-fatal; the file still validates `ok`.
- The scratch mirror receipt `.ufo/waves/round-69/assimilation/validate-census.txt` shows **17**
  `W04` (only `S207`) and `exit=0`, but it is **not byte-identical to what was appended**:
  `diff` shows the mirror has 352 lines / `S203–S207` / strength cell `A` / anchors ending
  "page as served 2026-10-25", while the lane file has 353 lines / `S203–S208` / strength cell `B`
  / shorter anchors. The plan's "validate `--file` exit 0 before the first registry append" is
  satisfied for the scratch transform; it is not evidence about the appended bytes.

### (3) `jj-lane.sh state`

Command: `~/Projects/shokunin/scripts/hyaku/jj-lane.sh state ~/Projects/shokunin/kotoba-shokunin`

```
state branch=master local=a238989a96cb0d2b939679126b832d75b861ca6e remote=a238989a96cb0d2b939679126b832d75b861ca6e ahead=0 behind=0 head=detached tracked=17 untracked=25
```

- The branch is `master`; local and remote are equal, `ahead=0 behind=0`; the working tree is
  dirty (`tracked=17 untracked=25`, which matches `git status`'s 17 modified and 25 untracked
  lines exactly).
- **The tip is not `a5f7459`.** It is `a238989a96cb0d2b939679126b832d75b861ca6e` — the round-69
  plan-freeze commit "round-69: frozen plan, three counters (C1 skill precedence, C2 r68 routed
  repairs, C3 province core) and base/junk controls", author `kotoba-shokunin
  <kotoba@shokunin.local>`, whose parent (`%P`) is `a5f7459f99bb27bf697e9438362e75ac5833eca8`.
  `a5f7459` is correctly described by the plan as the round-68 closure spot-check authored
  `protocol-shokunin <protocol@shokunin.local>`.
- Consequence for wording: "base lane tip `a5f7459`" is accurate as the round's *base*; "lane tip
  is `a5f7459`" is false now. The three counters do not exist at `a5f7459`
  (`git cat-file -e a5f7459:verifiers/<counter>` → absent for all three); they enter at `a238989`,
  so every `--rev a5f7459` control is the `a238989` counter measuring base bytes.

### (4) Freeze receipt sha256s

Command: `sha256sum` of the three counter files at the branch tip, plus
`git show HEAD:<path> | sha256sum`:

| counter | receipt line | `git show HEAD:` hash | worktree `sha256sum` | match |
|---|---|---|---|---|
| `verifiers/check_skill_precedence.py` | `9c796574c2d588f27869e0e14289c1be8f0b3f3e56f785d68eb64ee5e756da48` | identical | identical | yes |
| `verifiers/check_r68_routed_repairs.py` | `320254996e49f48cd757532be31b330f73545f5ec50ff8b32f34779d9fe0dcf2` | identical | identical | yes |
| `verifiers/check_province_core.py` | `c85f9d7533fbc4b9ec0ba844004e475952fe1eb39d435b810ab4be88967a6c5a` | identical | identical | yes |

All three match at `a238989` and in the worktree. The receipt file
`.ufo/waves/round-69/controls/freeze-receipt.txt` is committed (9 files under
`.ufo/waves/round-69/controls/` are tracked at HEAD). One stale line inside the receipt itself:
its `check_skill_precedence --self-test` block records `selftest setup failed: the entry is not
present in the working tree` / `exit=2`. That was true at freeze time; it is not the current
state (see §2).

## 2. Draft state, measured in a `/tmp` shared clone

The counters read **committed** bytes at `--rev`, and the entry, lesson, recapture receipts and
census mirror are all still untracked — at `a238989` the truthful committed verdict is therefore
the base controls (`C1 0 of 5`, `C2 0 of 8`, `C3 0 of 2`), not the draft. To measure the draft I
scratched a throwaway commit, as the controls themselves do.

Sandbox: `git clone --shared <lane> /tmp/r69-facts/repo`, overlaid with the lane working tree
(`rsync -a`, excluding `.git` and the 269 MB `c2falsify-clone/`), then
`git -c user.name=ScribeFactsAudit … commit` → `fbf56aaf6dc0700795883fb728d09c0d800a809e`,
clean tree. Counters run **in that clone**, never in the lane.

| claim | command | measured |
|---|---|---|
| C1 depth | `python3 -B verifiers/check_skill_precedence.py --rev fbf56aa` | `skill precedence backed 5 of 5`, exit 0 |
| C1 self-test | `python3 -B verifiers/check_skill_precedence.py --self-test` | `self-test: 0 failure(s) over 18 assertions`, exit 0 (17 broken worlds incl. honest world and missing-entry classification) |
| C2 consistency | `python3 -B verifiers/check_r68_routed_repairs.py --rev fbf56aa` | `r68 routed defects closed 4 of 8`, **exit 1** |
| C3 coverage | `python3 -B verifiers/check_province_core.py --rev fbf56aa` | `province core rows 2 of 2`, exit 0 |

C2's four open defects, verbatim from the counter, each reproduced against the draft bytes:

```
- D3: verifiers/check_r67_routed_repairs.py still runs `git checkout` (a git write in the lane)
- D6: corpus/lessons/round-69.md § Mistakes has no row naming R68-6 and S201
- D7: .ufo/waves/round-68/w1/controls/c2falsify-clone/ is neither committed nor dispositioned
- D8: baseline corpus.index.tracked_files expects 124, the gate measures 127 (+ unindexed 0→1,
      report_total 85→87, commit_total 38→39)
```

C2's D1, D2, D4, D5 close in the draft: all nine named receipts parse with `measured-rev` +
`exit=`, `C1-selftest.txt` carries `over 12 assertions`, `C2-routed-selftest.txt` carries
`over 6 assertions` with `exit=0`, § Gate names `S200 <code>` and `S202 **`, and `S208` carries
`supersedes S201 —` with the approval sentence in its anchor and is named by the round-68 entry.

## 3. Calibrations for the report (each is a wording trap)

1. **`D3` cannot pass with the current repair.** The frozen predicate is
   `re.search(r"[\"']checkout[\"']", src)`. The diff shows the lane `git checkout <rev> -- corpus
   verifiers` was correctly replaced by `git clone --shared -q --no-checkout` plus
   `git -C <clone> checkout -q <rev>` at line 101 of `verifiers/check_r67_routed_repairs.py`.
   The lane write is gone, but the quoted token in the `/tmp` clone still trips the frozen regex.
   The fix must materialize the revision without a quoted `"checkout"` token (e.g. `git show`
   writes, or `read-tree`), or the frozen counter is unsatisfiable as written. A report claiming
   "D3 closed" on the current draft is false; a report claiming "the lane write is gone" is true
   and is a different sentence.
2. **`D6` fails on line wrapping, not substance.** `corpus/lessons/round-69.md:102` carries
   `M111 … (R68-6)`; `S201` first appears at line 103. The frozen test is per physical line
   (`"R68-6" in l and "S201" in l`), so the row exists but does not count. One line carrying both
   tokens closes it.
3. **`D7` fails on the elided disposition path.** The frozen path is
   `.ufo/waves/round-68/w1/controls/c2falsify-clone/`; the lesson's fix text at
   `corpus/lessons/round-69.md:117` writes `disposition: removed .../c2falsify-clone/`. The regex
   captures `.../c2falsify-clone/`, which never equals the path, and the 269 MB clone is still
   untracked. The disposition line needs the full path (or the clone must actually be committed).
4. **`D8` is unrecorded.** `verifiers/corpus-baseline.json` is unmodified in the worktree
   (`expect` = 124 / 0 / 85 / 38); the gate in the draft sandbox measures 127 / 1 / 87 / 39.
   Re-recording must come from the gate's own `--no-baseline --json` at the measured revision, so
   the numbers are commit-dependent, not the 127/1/87/39 above.
5. **"Nine receipts" is right; the directory shows ten files.** `RECEIPTS` in the frozen counter
   has nine keys; the tenth file, `recapture/r67-repairs-base.txt`, is the D3 base-control receipt
   and is required separately. List them as "nine named re-captures plus the D3 base receipt" if
   the report enumerates them.
6. **Census did not stay flat.** 16 `W04` before → 18 `W04` now on the lane file (17 on the
   scratch mirror), `exit=0` throughout. The two additions are `S207` and `S208`, i.e. this
   round's own rows duplicating existing URLs (`S024`/`S039`; `S201`). "Census clean, exit 0" is
   true of the exit code; "census unchanged" is false.
7. **The `validate-census.txt` receipt does not describe the appended bytes** (5 rows/strength A/
   "page as served" vs the lane's 6 rows/strength B/shorter anchors). If the report cites it as
   evidence for the registry as appended, that is an upgrade of what the artifact shows.
8. **The freeze receipt's C1 self-test `exit=2` is stale.** The same command in the draft sandbox
   is `0 failure(s) over 18 assertions`, exit 0. Do not quote the receipt's exit=2 as the current
   state, and do not claim the freeze-time self-test passed.

## 4. Countable side-facts checked

- Assimilation collision arithmetic: `reg-ids` 128, `staged-ids` 188, `collisions` 0 — matches the
  plan. Guard proof: `guard-proof/reg-ids` 129 (the indented `  | S203 |` added),
  `guard-proof/collisions` 1, `guard-proof/collisions-col0` 0, `guard-proof/reg-ids-col0` 128 —
  matches "collides under the 0–3-space pattern, 0 under column-zero".
- Quarantine slice: 13 rows.
- Round-68 wave path arithmetic: 10 modified + 14 untracked = 24, and the `status` listing agrees
  path-for-path with `MODIFIED`/`UNTRACKED` in the frozen C2 counter.
- `PROVINCE.md` delta is exactly the two § Core bullets (round 67 ladder + round 68 trust gates);
  C3's byte-identity requirement on § Frontier/§ Adjacent is satisfied (counter passes).

## 5. Out of scope / not verified here

- C1 substance (whether each client's rule is quoted faithfully, whether the ten-word/25-word
  quote bounds hold, whether the entry's prose is accurate) — reviewer/critic seats' ground; I
  only ran the counter and opened the entry's row ids as reported above.
- `--fetch` against live pages (network, and outside the four enumerated measurements).
- Whether the wave-1 commit that lands these bytes will preserve the numbers: D8's baseline and
  the census row count are commit-dependent and must be re-measured at the landing revision.
- The judge/frontier band, band moves, and any axis score.
- Installs/updates: none performed.

Artifacts: `/tmp/r69-facts/repo` (sandbox commit `fbf56aa…`), `/tmp/r69-facts/c2.txt`,
`/tmp/r69-facts/c3.txt`, `/tmp/r69-facts/c1-selftest.txt`. Lane writes: this report only.
