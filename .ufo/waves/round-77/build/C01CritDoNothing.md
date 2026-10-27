# C01CritDoNothing — do-nothing falsification of the frozen C1 / C2 counters (round 77 w1)

FINDING FIRST: **both counters are reached by worlds that skip the claimed work.** Target 6 of 6 / 4 of 4 certifies form (presence, page-membership, recomputed numbers), not substance. These are fixable only by narrowing what the headline claims and by non-counter checks in the data, because the counter bytes are frozen (sha256 below, verified in scratch).

Counters (sha256 re-checked): C1 cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e; C2 989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63. Base = lane HEAD 6523aced1ee0ebe07dca996213bdc645a6acbd1e. Every world = one scratch commit atop HEAD in `git clone --shared` (toplevel asserted equal to the clone dir; user.name/email scratch set first). Exit codes are the counter subprocess's own returncode (python subprocess, no pipeline). Full printed output of all 34 runs: `C01CritDoNothing.receipts.txt`; reproducible diffs: `C01CritDoNothing.c1-worlds.patch`, `C01CritDoNothing.c2-worlds.patch`.

## C1 (description craft) — worlds and printed lines

| world | what it skips | printed | exit |
|---|---|---|---|
| C1-W0 base | (control) | `description craft backed 0 of 6` | 1 |
| **C1-W1 minimal stub** | 489-byte entry = provenance trio + 4 quote strings with `:25`..`:28` cites + 2-row table (1022 / 151); one 171-byte SKILL row in § Body craft (S213 + entry path + 2 page fragments); used-by appended; 334-byte lesson (URL, date, quote, 8-hex digest prefix, one old->new line). No rule reading, no audit, no description action; SKILL.md frontmatter byte-identical to base | **`6 of 6`** | **0** |
| C1-V3 3-word quote fragments ("Err on the side", "Keep it concise"...) | n/a | `5 of 6` ((b) fails, 0 counted quotes; I did not diagnose which sub-test rejected each fragment, only that the four short fragments did not count) | 1 |
| **C1-V4 lying audit** | W1 + prose "every rule met; description 400 characters" (only table cells are read) | `6 of 6` | 0 |
| **C1-V8 held-half** | all 4 entry quotes, row fragments and Gate quote come from the eval-loop half (lines 138-163: "Five iterations is usually enough", "you risk overfitting"...) the plan says is HELD/not admitted | `6 of 6` | 0 |
| **C1-V9 nonsense row** | SKILL row cell text is just `x`; lesson (e) line is `S213 description-craft-round76.md old new` | `6 of 6` | 0 |
| **C1-V5a used-by REPLACED** | S213 used-by drops the r70 path (`skill-eval-artefacts-round70.md`) instead of appending (lesson still says old -> new) | `6 of 6` | 0 |
| **C1-V5b "told ... new"** | lesson line `S213 corpus/knowledge/description-craft-round76.md told us something new.` — no old path, no arrow ("told" contains "old") | `6 of 6` | 0 |
| ablations of W1 | one arm each: digest 8-hex wrong / 3 quotes / no SKILL row / audit 1021+150 / no used-by / no verified-at / quotes cited `:3` | each `5 of 6`, exit 1 | 1 |

Which arm let it through:
- (b) `conjunct_b`: any >=3-word, <=25-word double-quoted span that is on one page line after the first heading, absent from the two sibling pages and on a line the entry cites (`:N` shorthand is read from anywhere). Nothing ties it to the four writing principles (`:25`-`:28`); the eval-loop half passes (V8). Citation arm is satisfied by citing the line it quotes.
- (c): row needs only S213 + entry path + two >=3-word backtick/quote spans that occur on the page; no rule content (V9).
- (d): reads only table cells whose first cell says "description ... length"/"first ... sentence ... length"; recompute is of SKILL.md, which the claim never changes; values equal base numbers (W1, V4). A script-only world reaches (d), as the plan already concedes.
- (e): `"old" in low and ("new" in low or "->")` are substrings ("told", "knew"); membership-only on used-by, so replacing the r70 path (V5a) passes — and would make `check_skill_evals_v2.py` F7 fail on exact-member match.
- (a): digest in the Gate may be any >=8-hex prefix of the pinned digest (`_digest_mentioned`); the date check is skipped if the fetch record has no dates (it has).

## Draft-pipeline defect found (real, not a do-nothing world)
- **C1-V7**: r76 drafts pasted verbatim (entry-draft, skill-patch Pin 1 row, sources-patch new line 153, lesson-draft with the build comment dropped) = `5 of 6`, exit 1: `(a) the lesson Gate carries no <=25-word quote located in the optimizing-descriptions snapshot`. Cause: lesson-draft Gate quote is `"`A few sentences to a short paragraph is usually right`"` — the backticks inside the quote marks are not page bytes, so the span fails the verbatim lookup. **C1-V7b** (same drafts, only the backticks inside that quote removed) = `6 of 6`, exit 0. Entry, SKILL row and sources line from r76 drafts pass (b)(c)(d)(e)(f) on the frozen counter; (d) uses base values 1022/151 (SKILL.md frontmatter unchanged).

## C2 (r75 routed repairs) — worlds and printed lines

| world | what it does | printed | exit |
|---|---|---|---|
| C2-W0 HEAD | control | `closed 0 of 4` | 1 |
| **C2-W1 cheap pasted** | R1: base lesson + appended block quoting the base row/gate lines + "1,022 ... 4-18 ... spotcheck"; R1 receipt hand-typed (rev, clip 1022, stripped 1021, 4-18); R2 receipt = TIP line + the REAL gate stdout (exit 0 each, produced by the counter's own sandbox at ac9f295); R3 note names seat/path, `63 of 64`, "absent", 40-char excerpt; 3 LOG lines | **`closed 4 of 4`** | **0** |
| C2-W2 forged R2 green text | R2 = "all checks pass PASS exit=0" with no real stdout | `3 of 4` (R2: transcript != normalized re-run) | 1 |
| C2-W3 base RED stdout relabelled at r75 tip | | `3 of 4` (DRIFT + mismatch) | 1 |
| C2-W4 both gate names on one line (block-splitter probe) | | `3 of 4` | 1 |
| **C2-W5 R1 receipt names HEAD** | any ancestor with a 1022 render | `4 of 4` | 0 |
| **C2-W9 generic excerpt** | R3 "excerpt" = first 20 chars of the results output (`{\n  "verdict": "R75Facet28 survived with` opener) | `4 of 4` | 0 |
| **C2-W11 token + windows** | R1 appended text = one line of the six tokens/numbers + a 30-char window of base row + of base gate (no prose) | `4 of 4` | 0 |
| C2-W10 token line without windows | | `3 of 4` | 1 |
| W6/W7/W8 | no LOG cites / no closing line / lesson edited in place | `2/3/3 of 4` | 1 |

Which arm: R1a (30-char window, token presence) and R3 (any >=20-char window) are presence floors the docstring already discloses (Q33/Q58); R4 recomputes counts from committed w2 data (a true line is needed but a pasted one suffices). **R2 held**: the only way to R2-green is real gate stdout at ac9f295, which the counter re-runs and compares — copied real stdout is honest reproduction (the gates exit 0 at the tip; verified), so R2 is not a loophole; forged and relabelled receipts fail.

## Impacted axes and smallest safe correction (counters frozen, so these go into plan/data, not the counter)
- depth / calibration: state in a pre-data r77 addendum that `6 of 6` certifies admission + located quotes + matching audit table only (already the r76 plan's wording) and that three conditions are NOT counter-enforced and must be checked by w2 non-author seats and the closure: (1) the entry's quotes come from `:25`-`:28` (not the held loop half, V8); (2) the SKILL row states an actual rule (V9); (3) S213 used-by keeps the r70 path (V5a) and the lesson line contains the old path (V5b).
- consistency: C2 counts R1/R3 as closed on window/token presence; require the landed correction/note to be real prose (w2 reviewer read), disclose that W9/W11 reach 4 of 4.
- operability: the r76 lesson-draft Gate quote must be landed WITHOUT backticks inside the quotation marks (V7 5 of 6 -> V7b 6 of 6); everything else in the r76 drafts passes as-is.
- Do not edit the counters (sha pinned); a rewritten stricter counter would be a new claim.
- Verdict on do-nothing: a do-nothing world reaches the target on both counters -> report scores must say "counter-reachable by form; substance judged by named non-author seats".
