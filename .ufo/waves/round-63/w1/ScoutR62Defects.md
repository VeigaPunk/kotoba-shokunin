# ScoutR62Defects

role: scout
item: ScoutR62Defects — map the five §6 routed defects in `corpus/lessons/round-62-verifier-spotcheck.md` onto committed bytes at `35d44b4b4dcdda234b5dbff7af37e432fec55f05`

Axes used: citation fidelity (named rev vs receipt bytes), completeness (omitted interim reds; untracked late write), append-only (corrections must not rewrite committed LOG lines).

Scope note: lane tip `35d44b4b` does **not** contain `.ufo/reports/round-62/kotoba.md`. That report is fleet-only, blob at `def4b9fffbf59e9e121b89ef73fbeb89426bd614` (2026-10-23 18:56:15 -0300). Lane citations below are `git show 35d44b4b:<path>`. Working-tree HEAD has since moved to `8c4cefa` (r63 plan); it does not change these r62 bytes. No installs.

C2's five machine checks (plan) cover defects 1, 2a, 2b, the append-only method, and 4. Defect 2c, defect 3, and defect 5 are real §6 items and are **not** those five checks.

## Findings

1. **Defect 1 — untracked late write.** Sentence (`round-62-verifier-spotcheck.md:161-165`): commit or revert `.ufo/waves/round-62/w2/FalsifyC2HonestH1.md`; if committed, fold the H1-narrowness finding. At `35d44b4b` the path is absent (`git ls-tree` prints nothing; `git cat-file -e` → `exists on disk, but not in '35d44b4b'`). Working tree: `??`, 158 lines. No committed sentence claims it is tracked. Fleet report `:110` still lists `FalsifyC2HonestH1` among seats "not settled at close" whose later write "is a late write … not evidence this round counts" — true only while the file stays untracked. The on-disk finding (not a committed claim) is `:60-74`: the lane's real R-c bullet uses `` `**not**` ``, which fails v2's `\b(?:not|…)\s+` denial; honest variants M-a/M-b/M-e/M-j drop the successor from 6 to 5 (2-line window, `base`-before-ref, bare name + final period).

   Command: `git ls-tree -r 35d44b4b -- .ufo/waves/round-62/w2/FalsifyC2HonestH1.md | wc -c` → `0`.

   Correction target (plan check `late-write-tracked`): commit the file as wave evidence so `git ls-tree -r <rev> --` that path is non-empty. Folding the regex bound into the entry/Q57 is the spot-check's extra conditional; check 1 does not read it.

2. **Defect 2a — C2 `receipt_rev`.** Sentence (`:166-167`): fix the C2 `receipt_rev` (actual `3f911504…`, re-recorded at `e424f2a4`). Two wrong citations, one truth.

   - Fleet report `:58` (commit `def4b9ff`): `receipt_rev `e6da78bb``. `e6da78bb` is the corpus/v3.1 commit, never the receipt field.
   - Lane `LOG.md:2552` at `35d44b4b`: `` receipt rev `3e7aed9b` ``. That was `receipt_rev` only in the file created at `f9ab081`. `git log -L 2,2:.ufo/waves/round-62/C2-successor-measure.txt` shows `e424f2a4` replacing `receipt_rev=3e7aed9b61bbfd83e0c800213b6dfc6da6191f85` with `receipt_rev=3f911504ce76d9ca186f297d6d4a9cd8ed77508a`. The LOG bullet was not updated. `git grep 3f911504 35d44b4b -- LOG.md` → no hit.

   Truth at tip: `C2-successor-measure.txt:2` = `receipt_rev=3f911504ce76d9ca186f297d6d4a9cd8ed77508a`.

   Command: `git show 35d44b4b:.ufo/waves/round-62/C2-successor-measure.txt | sed -n '2p'`.

   Correction target (check `receipt-rev-named`): **append** a Round-62 LOG line that contains the exact token `3f911504ce76d9ca186f297d6d4a9cd8ed77508a`. Do not edit `:2552` in place (check `append-only`).

3. **Defect 2b — entry size.** Sentence (`:167`, and `:45-46`): the report's "723 words, 50 lines" is narrower at tip (`wc -lw` → 64 lines / 1,044 words); the figure was true at `e6da78bb`.

   - Wrong claim: fleet report `:23` — `` (723 words, 50 lines per `wc`) ``. Not in the lane tree.
   - Measured: `git show <rev>:corpus/knowledge/erratum-absorption-round62.md | wc -lw` → `e6da78bb` `50 723`; `e424f2a4` `55 920`; `e53b6e5c` and `35d44b4b` `64 1044`. Round-62 LOG has no `1044` in the r62 entry.

   Correction target (check `entry-size-named`): the same appended LOG line must state both tip numbers **64** and **1044** (the counter's `wc -l` / `wc -w`, not the comma form).

4. **Defect 2c — claimed post-report child.** Sentence (`:167-168`, spelled at `:48-50`): the compliance line claims a final sweep commit rewriting `FalsifyC2Mutants.md` follows the report as a child; "no child exists — the cited tip is the tip."

   - Wrong claim: fleet report `:122` — "a final sweep commit for a late rewrite of `FalsifyC2Mutants.md` follows the report as a child commit". Not in the lane tree.
   - Cited tip `e53b6e5c` (2026-10-23 18:56:08 -0300) is the parent of the fleet report commit seven seconds later. Last `FalsifyC2Mutants.md` change is `d519047c` (18:50:24), `merge-base --is-ancestor` of `e53b6e5c` (exit 0). `git log e53b6e5c..35d44b4b --` that path is empty. `git diff --stat e53b6e5c 35d44b4b` is only `corpus/lessons/round-62-verifier-spotcheck.md` (+182). Other children of `e53b6e5c` (`30854071` empty; `7bd8faa` / `79fa59b` / `35d44b4b` spot-check copies) do not touch the mutants file.

   Correction target: the appended LOG line should say no such child exists. Not a separate machine check. Do not rewrite report `:122` from the lane (fleet file; append-only preference).

5. **Defect 3 — Cursor `.md` rejection reason (not in the 5-of-5 counter).** Sentence (`:170-172`): name the `Accept: text/markdown` condition in the lesson Gate, and re-open whether S049's `.md` URL is minable as `text/markdown` or state why `/docs/rules` stays canonical. Plan: re-probe both `Accept` forms; correct the r62 lesson Gate; append the SOURCES note, do not rewrite the row.

   - Wrong claim today: `corpus/lessons/round-62.md:19` at `35d44b4b` (blob `a95325fa…`): Cursor's `https://cursor.com/docs/rules.md` and `https://cursor.com/docs/reference/plugins.md` "also returned HTTP 404, with response headed `# Page not found`. These are dead URLs, not usable sources".
   - Spot-check `:133` already disagrees on the reason: `Accept: */*` → HTTP 200 `text/markdown`; `Accept: text/markdown` → HTTP 404. Decision (not a distinct source; S115 holds `/docs/rules`) still holds.
   - Canonical bytes already mined: `SOURCES.md:127` S115 and `:120` S108 are `https://cursor.com/docs/rules` (no `.md`), sha256 `884c67ca…`, 17,403 B. S049 (`:62`) is the `.md` URL, same size/sha, fetched 2026-10-22. The Gate sentence calls that URL dead while S049 remains a mined row.

   Correction target: append a Gate sentence on `round-62.md` naming the `Accept` condition and stating why `/docs/rules` (S115) stays canonical, or that the `.md` URL is minable under `Accept: */*`. Do not rewrite `:19` or the S049 cells in place.

6. **Defect 4 — no-harm summary omits two interim reds.** Sentence (`:173-175`): record the receipt's two interim reds at `3e7aed9b` (`reg_gate` 36 of 38; `corpus-idx` round-61 spot-check) as fixed-at-tip.

   Receipt (still the committed measurement; these lines are true for that rev, not the "wrong claim"):

   - `.ufo/waves/round-62/noharm-tip.txt:1` `Measured revision: 3e7aed9b61bbfd83e0c800213b6dfc6da6191f85`
   - `:12` `FAIL  reg_gate    expected exit 0 in both columns, got base=0 tip=1`
   - `:13-14` unregistered `check_erratum_absorption.py` and `check_routed_repairs_v2.py`
   - `:15` `tip: gate registry rows conformant 36 of 38 lane verifiers; phantom 0`
   - `:17` `FAIL  corpus-idx  tip leaves new corpus file(s) unindexed: corpus/lessons/round-61-verifier-spotcheck.md`
   - `:23` `Battery exit code: 124`

   Summaries that omit both tokens:

   - Lane `LOG.md:2566`: "No-harm. `.ufo/waves/round-62/noharm-tip.txt` at the measured tip (battery arms as printed; …)." `git grep '36 of 38' 35d44b4b -- LOG.md` → no hit.
   - Fleet report `:99`: claims the re-run gates "are green where reported (registry `39 of 39`, corpus index `unindexed 0 …`)" and never names `36 of 38` or the round-61 spot-check path.

   Fixed-at-tip evidence already committed (do not re-run): `FalsifyGateRegress.md:13` registry `39 of 39` at `e6da78bb`; `:26` `corpus-idx` PASS at `e6da78b` (`unindexed` 1→0); `:39` the wave-1 `FAIL reg_gate` was the missing rows, fixed by `e6da78b`. At `35d44b4b`, `SKILL.md:488-491` are the four new rows and `corpus/README.md:108` indexes `lessons/round-61-verifier-spotcheck.md`.

   Correction target (check `noharm-arms-named`): appended LOG line naming both arm tokens `reg_gate` and `corpus-idx` and the measured `36 of 38`, and that both were fixed by `e6da78bb`. Do not rewrite `noharm-tip.txt` or `:2566`.

7. **Defect 5 — SHONEN, no change.** Sentence (`:176-177`): the four boxes remain `[~]` with resolvable pointers; promotion is operator-owned; no `[x]` written. At `35d44b4b`, `SHONEN.md:5,7,9,11` are the four `[~]` marks (zero `[x]`). Fleet report `:75-78` repeats four `[~]` with r62 pointers. Not one of the five counter checks. Correction target: none.

8. **Append-only constraint (counter check 4, already true at this tip).** `git diff --stat e53b6e5c 35d44b4b` does not touch `LOG.md`, so `e53b6e5c:LOG.md` is a byte-prefix of `35d44b4b:LOG.md`. Spot-check `:50-52` records that `e424f2a4` already rewrote this round's own LOG bullets in place, while `a745411c→e53b6e5c` is 23 insertions / 0 deletions of pre-round text. A r63 edit of any existing LOG line fails check 4 even if the five content tokens are present.

## Artifacts

Proposed appended LOG lines (not applied). One block can satisfy checks 2, 3, and 5; check 1 is the git add of the late write; check 4 is "append only".

```text
- **r63 correction (r62 spot-check §6, appended; prior bullets unchanged).**
  C2 receipt field is `receipt_rev=3f911504ce76d9ca186f297d6d4a9cd8ed77508a`
  (re-recorded at `e424f2a4`). The report's `receipt_rev e6da78bb` and this
  entry's `receipt rev 3e7aed9b` name other commits.
  `corpus/knowledge/erratum-absorption-round62.md` at `35d44b4b` is 64 lines
  and 1044 words (`wc -lw`); 50 lines / 723 words was true only at `e6da78bb`.
  No post-report child rewrites `.ufo/waves/round-62/w2/FalsifyC2Mutants.md`:
  last change `d519047c` is an ancestor of cited tip `e53b6e5c`.
  No-harm receipt `.ufo/waves/round-62/noharm-tip.txt` at `3e7aed9b` records
  `FAIL reg_gate` (`36 of 38`) and `FAIL corpus-idx`
  (`corpus/lessons/round-61-verifier-spotcheck.md`); both fixed by `e6da78bb`
  (registry 39 of 39; spot-check lesson indexed).
```

```text
- **r63 correction (S049 `.md` reason, Gate append).** `https://cursor.com/docs/rules.md`
  and `…/reference/plugins.md` 404 only under `Accept: text/markdown` (body `# Page not found`);
  `Accept: */*` returns HTTP 200 `text/markdown`. Not dead URLs. `/docs/rules` (S115)
  stays canonical: same 17,403 B / sha256 `884c67ca…`, and S115 already holds that URL.
```

## Verdict

INFORMS. At `35d44b4b` the counter's four content checks are red for the reasons above (late write absent; LOG names neither `3f911504ce76d9ca186f297d6d4a9cd8ed77508a` nor `64`/`1044`; LOG names neither `reg_gate`/`corpus-idx` nor `36 of 38`); append-only is already green. I would change the map if `git ls-tree 35d44b4b` listed `FalsifyC2HonestH1.md`, if `C2-successor-measure.txt:2` were not `receipt_rev=3f911504…`, if `wc -lw` at that rev were not `64 1044`, or if a child of `e53b6e5c` changed `FalsifyC2Mutants.md`.
