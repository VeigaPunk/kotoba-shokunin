# F12CheckviewRound77 — round-77 lesson "Mistakes demonstrated-fix bar" (wave w2 falsify)

Seat: F12CheckviewRound77 (leaf reviewer; no subagents). Date: 2026-10-27.
Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Attacked item: the round-77 lesson draft
`.ufo/waves/round-77/build/SC02Lesson77.round-77.md` (landing target `corpus/lessons/round-77.md`),
specifically its `## Mistakes` rows M77-1/M77-2 against the demonstrated-fix bar — fleet
`CORPUS.md:179-182`: "A fix is shown able to fail before it counts … the observed failure text is
committed" — plus the round's frozen C1/C2 counter state at the landed tip. Scratch work was done
only under `/fast/scratch/hyaku/kotoba-r77/F12ReviewRound-77/` (removed before this report; see §6).

## 0. Landed state — claim data is NOT committed (blocker, stated plainly)

- Lane tip: `6523aced1ee0ebe07dca996213bdc645a6acbd1e` ("round-77: freeze plan, base receipts").
  `git status --porcelain` shows no claim data: w1/w2 build outputs and receipts are **untracked**
  working-tree files; the freeze commit carries only `plans/round-77.md` and four base receipts
  (`c1-base-2f675548….txt`, `c2-base-2f675548….txt`, `census-before.txt`, `selftests-base.txt`).
  `git cat-file -e 6523ace:corpus/lessons/round-76.md` → exit 128 (lesson absent, as the plan's
  R76-D2 record and my own run confirm).
- Scratch verification (clone `--shared` from the lane, `user.name scratch-r77`,
  `user.email scratch@example.invalid` set before anything else, `rev-parse --show-toplevel` asserted
  equal to the clone dir, every git call naming `-C`):
  - `python3 -B verifiers/check_desc_craft.py --repo $S/clone --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e`
    → conjunct lines (a)–(f) all `fail`; final line `description craft backed 0 of 6`; **own exit=1**.
  - `python3 -B verifiers/check_r75_routed_repairs.py --repo $S/clone --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e --work $S/work`
    → `R1: open … R4: open`; final line `r75 routed repairs closed 0 of 4`; **own exit=1**.
  - Both captured with the gate's own exit status (`cmd > out 2>&1; echo "exit=$?" >> out`), no pipelines.
- Counter bytes at 6523ace equal the plan's pins exactly: `check_desc_craft.py` sha256
  `cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e`; `check_r75_routed_repairs.py`
  sha256 `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63`. Self-tests at the tip:
  C1 `self-test: 0 failure(s) over 53 assertions`, exit 0; C2 `0 failure(s) over 27 assertions`, exit 0
  (matches the committed `selftests-base.txt` expectation 53/27).
- The committed base receipts measure the r77 **base** `2f675548eaad2a037a899d39247c1fd7a88aaf48`
  (`0 of 6` / `0 of 4`, exit 1 each — bytes read at 6523ace and quoted in §1/§5 of my check notes);
  my independent runs at the **freeze tip** reproduce the same K=0/0-of-4 verdicts.

Consequence for the wave: **neither C1 nor C2 is verified or landed at this tip.** Falsification here
therefore attacks the freeze-tip state and the w1 drafts; nothing below may be read as a claim pass.

## 1. M77-1 (class `landing`) — every measured fact reproduces; one path defect

Draft claim: the r76 plan promised the declined-proposal reasons would be "recorded in the round-76
lesson Gate", but `corpus/lessons/round-76.md` does not exist at the r77 base; the frozen C1 counter
fails conjunct (a) on exactly that absence.

Verified against committed bytes at 6523ace:
- `git cat-file -e 6523ace:corpus/lessons/round-76.md` → exit 128 (`fatal: path … does not exist`).
- Both plans name the path: `plans/round-76.md` (touch list: `corpus/lessons/round-76.md`) and
  `plans/round-77.md` § Trigger (R76-D2). Present in both files I read at the tip.
- Committed receipt `.ufo/waves/round-77/receipts/c1-base-2f675548….txt` line: `(a)
  corpus/lessons/round-76.md is not committed at the measured revision`, final line `description
  craft backed 0 of 6`, `exit=1`, `measured-rev: 2f675548…`, counter sha256 `cf3c45d9…`. My own tip
  run reproduced the same (a) message at 6523ace.
- check2 (the row's proposed fix, script pinned in `build/SC02Lesson77.red-before.txt` §3) reproduced
  by me from scratch at 6523ace: `MISSING corpus/knowledge/description-craft-round76.md` +
  `MISSING corpus/lessons/round-76.md`, `checked 9 plan-named corpus paths`, **exit=1**; lesson arm
  (`corpus/lessons/*.md` only): `MISSING corpus/lessons/round-76.md`, `checked 3`, **exit=1**.
  Green-after with the existence fixture as the only delta (my own scratch commit
  `7dc4aa5e4187862fb914be4f51a4c586afbf9a0a`): lesson arm `checked 3`, **exit=0**, while the
  all-paths run correctly stays exit=1 (C1 entry still absent — freeze discipline respected).

**DEFECT F1 (medium, must fix before landing).** The M77-1 evidence pointer cites a doubled path:
`.ufo/waves/round-77/receipts/.ufo/waves/round-77/receipts/c1-base-2f675548eaad2a037a899d39247c1fd7a88aaf48.txt`
(exact bytes in the draft; one occurrence, `grep -c 'receipts/\.ufo/waves'` → 1). No such path exists
on disk (`ls` → ENOENT) or in `git ls-tree -r 6523ace`. The committed receipt is
`.ufo/waves/round-77/receipts/c1-base-2f675548….txt`. A lesson row that mines a typo'd root
(M77-2) must not itself carry a typo'd path. **Minimal repair:** delete the duplicated
`.ufo/waves/round-77/receipts/` prefix inside the M77-1 cell. **Harm:** none — pure citation fix; no
conjunct, counter, or other row depends on the malformed string.

## 2. M77-2 (class `reference-drift`) — every measured fact reproduces; no defect found

Verified against committed bytes at 6523ace:
- Tracked stray paths are exactly: `kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md` and
  `kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md` (`git ls-tree -r --name-only 6523ace |
  grep '^kotoba-shokukin/'`).
- `.ufo/waves/round-76/w1/A18ScoutSnapshot.md` and its stray twin are byte-identical, both sha256
  `ae39b182e2bf4b95b7337f65fb6ceb4cb423e5b37fd4c0ffb9e49de9238118fb` (as the row states).
- `kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md` is the **only** copy; sha256
  `a419cc6f2513d0a5a6bf0887e3694445ffd04cbaa3872c47053c3f96f4c9fdd9` matches the row's `a419cc6f…fdd9`;
  declared path `.ufo/waves/round-75/w1/R75Facet48.md` absent (`git cat-file -e` → exit 128).
- `corpus/lessons/round-75.md:12` (attribution row) really says "Copied byte-exact to the same
  relative lane path, verified with `cmp`" — while the tree never carried the declared path. Quote accurate.
- `corpus/lessons/round-75-verifier-spotcheck.md:44` really reads "Misroot `R75Facet48` recovered:
  `git diff --numstat` carries `22 0 kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md`;
  `git ls-tree -r ac9f295…` confirms it; no fleet-root `kotoba-shokukin` remains." — the closure
  checked the tree against the diff's own typo spelling, exactly as the row argues. Quote accurate.
- Provenance: `ac9f295` added the R75Facet48 stray (22 insertions, matching the numstat `22 0`);
  `6ce2724` added the A18 stray.
- check1 (the row's proposed fix, allowlist pinned in red-before §2) reproduced by me: at 6523ace it
  prints `kotoba-shokukin` + `FAIL check1: top-level path outside the declared lane roots`, **exit=1**;
  after my scratch fix A (restore R75Facet48 to its declared path — sha256 equal — then `git rm -r
  kotoba-shokukin`, commit `270869ba4f0553ce3a930a542ce05a6b29ec453f`) it prints `ok check1 …`,
  **exit=0** with fix A as the only delta. **Mutation test:** reintroducing a stray top-level root in
  the scratch clone makes check1 fail again (prints `mutant-root`, **exit=1**) — the proposed gate
  kills the defect class it claims, and the allowlist matches the lane's 13 real top-level entries.

## 3. Demonstrated-fix bar (CORPUS.md:179-182) — verdict per row

- Red-before: same command non-clean for the named reason at the r77 base — demonstrated for both
  rows (check2 exit=1 naming both missing paths; check1 exit=1 naming `kotoba-shokukin`), by SC02's
  receipt and independently by me.
- Fix as the only delta: demonstrated (my scratch commits `270869ba…` and `7dc4aa5e…` changed exactly
  the named paths; check1/check2 flipped to green on the defect's own arm).
- Mutation: check1 survives a reintroduced stray root attack (fails it). check2's red state is itself
  the defect re-appearing (existence check). Bar met.
- **Landing requirement (not a draft defect):** CORPUS.md:181 requires "the observed failure text is
  committed". `build/SC02Lesson77.red-before.txt` is untracked at 6523ace. The L1 must commit it with
  the wave-evidence commit before or with the lesson; until then the bar is met only in draft.

## 4. Other checks on the draft's cites (all pass)

- `CORPUS.md:171-172` carries the "One row per / mistake:" convention (line-wrapped; the draft's
  plain quote is accurate). Classes `landing` and `reference-drift` are in the CORPUS.md:173-175
  vocabulary. The fix bar sits at `CORPUS.md:179` as cited.
- `corpus/SOURCES.md:153` is the S213 row as cited; its used-by cell is the single member
  `corpus/knowledge/skill-eval-artefacts-round70.md` (awk field $12; the row has 11 content cells —
  the draft's "12th cell" is field-numbering; phrasing nit F3, no repair required).
- `.ufo/waves/round-77/receipts/census-before.txt`: last two lines are `kotoba ok …` and `exit=0`;
  W04 warning lines counted = 20, matching the draft's Gate census paragraph.
- The draft's follow-up flag is accurate: `plans/round-77.md` § Trigger asserts R76-D1 "stray
  `kotoba-shokukin/` path removed" while the base tree still carries it (§2 above); the sentence
  becomes true only via the restore+delete landing, not by wording.
- Red-before receipt's sandbox commit `a0c4762fa55492277828a6fa8b7e65c20aa3b9d5` is absent from the
  lane (`git cat-file -e` → exit 1), as its "exists nowhere in the lane" note claims.

## 5. Findings by severity

- **F1 (medium, fix before landing):** doubled receipt path in the M77-1 evidence pointer (§1).
  Minimal repair: drop the duplicated `.ufo/waves/round-77/receipts/` prefix. Harms no axis.
- **F2 (landing requirement):** red-before failure text (`build/SC02Lesson77.red-before.txt`) must be
  committed at the wave-evidence landing to satisfy CORPUS.md:181 (§3). Harms none; pure process step.
- **F3 (nit):** "12th cell of the row" vs 11 content cells (§4). Optional rewording. Harms none.
- No defect found in M77-2's six cells; its quotes and hashes are byte-accurate. No fabricated
  output, hash, or quote found anywhere in the two rows I attacked.

## 6. Residual risk and verification gaps

- I did not re-open S213 on the web (S01/S02 own it); the pinned digest `7cc54fbb…bd837` is unverified
  by this seat. I did not run the full no-harm battery (E12/wave item); my lane access was read-only
  (`git status` after my session shows only the pre-existing untracked wave files) and all my commits
  were scratch-only, now removed (`/fast/scratch/hyaku/kotoba-r77/F12ReviewRound-77/` deleted;
  cleanup exit 0). M77-3+ and the Gate/Spot-check `[[SLOT: …]]` cells are unfilled by design
  (freeze discipline: the L1 fills them at landing). Tooling: no installs (nothing needed beyond the
  present git/python3; pacman paused host-wide and not touched).

VERDICT: M77-1/M77-2 meet the demonstrated-fix bar with independently reproduced red-before/green-after and a mutation-killing stray-root check, but M77-1's evidence pointer carries a doubled receipt path (F1, minimal repair: drop the duplicated prefix); C1 prints `description craft backed 0 of 6` exit 1 and C2 prints `r75 routed repairs closed 0 of 4` exit 1 at tip 6523ace — claim data is not committed, so neither claim is verified (blocker honestly recorded).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w2/F12CheckviewRound77.md (mirror pointer at /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w2/F12ReviewRound-77.md)
