Result: HOLDS — the frozen C2 counter rejects all four skip-family controls (best 72/120, exit 1); no do-nothing/junk/fabricated/shortcut instrument in this family meets the predicate, so the claim is not gameable by skipping the info-less fence surface.

# C2 pre-freeze control — skip instruments on info-less fences

Seat: CtlC2SkipInfoless. Time box: 25 min. No data seat: every control below is deliberately hollow (it removes
coverage; none is a fix meant for landing) and no C1/C2 content was written anywhere.

## Identity

- Frozen counter: `verifiers/check_infoless_fences.py` at `ee50d8fa7b5d260fff8bc332f4a90513bee518ff`, sha256
  `b3dbe72fd9383b6d404160a7f81a7630f3bfe915520dad85a7f1e008faf5d1ac` (copied unmodified into the sandbox scratch
  dir; the copy's `--self-test` printed `self-test: 0 failure(s) over 105 assertions`, exit 0).
- Sandbox clone: `/fast/scratch/hyaku/kotoba-r57/CtlC2SkipInfoless`, base `ee50d8fa…`; every control commit changes
  exactly one file, `verifiers/verify_skill_checklist.py` (`git show --stat`: 1 file changed each).
- Command per control (exit 1 every time):
  `timeout 900 python3 -B _scratch/check_infoless_fences.py --repo /fast/scratch/hyaku/kotoba-r57/CtlC2SkipInfoless --rev <sandbox commit>`
- Raw receipt: `.ufo/waves/round-57/controls/CtlC2SkipInfoless.txt` (344 lines, sha256
  `e5cb9e6e324020c0aef76b33558edf2e31de19e8dc9620b19ebc30838dcbc698`); each section carries the counter's own
  `counter sha256`, `measured`, `instrument sha256`, tally line and the shell `exit=`.

| # | control | sandbox commit | instrument sha256 | tally (pass / hard) | exit |
|---|---|---|---|---|---|
| 1 | skip every info-less fence | sandbox `3c73c8ad771d3425753090e8dc93044d3dda4f50` (/fast/scratch/hyaku/kotoba-r57/CtlC2SkipInfoless) | `f18556d5…` | 12/120 (0/60, 12/60) | 1 |
| 2 | info-less fence read like inline spans (vocab heads only) | sandbox `2ef8c8596a9de6313fd7820dbdfe606f48a69c94` (/fast/scratch/hyaku/kotoba-r57/CtlC2SkipInfoless) | `2951e47e…` | **72/120 (60/60, 12/60)** | 1 |
| 3 | skip info-less fence holding `\|`/`+`/box char/`key:` first token | sandbox `4231a1fd259b2e7521e63acc75cf5ae6184f78c1` (/fast/scratch/hyaku/kotoba-r57/CtlC2SkipInfoless) | `82290233…` | 48/120 (0/60, 48/60) | 1 |
| 4 | skip whole fence on first non-shell-looking line (+ U+2192 arrow) | sandbox `298453c30d6f6a6cee36e2a1741071e9467a0533` (/fast/scratch/hyaku/kotoba-r57/CtlC2SkipInfoless) | `408a2886…` | 48/120 (0/60, 48/60) | 1 |

Base reference (committed do-nothing receipt, not rerun by this seat): `.ufo/waves/round-57/controls/C2-base.txt`
— 48 of 120 (0/60, 48/60), exit 1, instrument `629867d1…`.

## Counterexamples per control

**1 — skip every info-less fence: 12/120.** The only surviving correct cases are the twelve H5 cases, the single
class the counter tags `bash` (`check_infoless_fences.py:368` sets `info = "bash" if cls == "H5" else ""`). Every
other case falls to `N/A` because the skipped block yields no segments
(`CtlC2SkipInfoless.txt:21,23,30` — `status=N/A`). Read: the 120 cases isolate the info-less surface exactly; an
instrument that makes info-less fences ineligible scores the tagged control case and nothing else.

**2 — info-less fences read like inline spans: 72/120, the strongest shortcut.** It takes the entire pass half
(60/60) with a 34-line patch that never resolves a non-vocabulary head, because every pass case's only vocabulary
head is the inserted real command (`ls -la` / `git --version`, both in
`verifiers/checklist-command-vocabulary.json`). It then loses four of five hard-negative classes, and one of those
losses is worse than a miss: `wrong 11 H2 skill-421ebc23 status=PASS` (`CtlC2SkipInfoless.txt:133,134,138,142`).
H2 is `ls | tok`; under the vocab-only rule the `ls` segment is a subject and resolves, the bogus piped head `tok`
is silently dropped, and the check reports PASS — a true positive converted into a false negative, not merely a
skipped case. H1/H3/H4 become `N/A` (`:135-137`).

**3 and 4 — shape-keyed fence skips: 48/120, exactly the base tally.** They change which cases are wrong (the live
false-FAIL shapes P1/P2/P3/P5, and P4 for control 4, become `N/A`; base had them `FAIL`) without moving the score,
because the same shapes carry true positives: H3 is a table plus a bogus command line. Skipping the table fence
deletes H3 (control 3 section, twelve H3 `N/A`, first at `CtlC2SkipInfoless.txt:192`; control 4 first at `:272`).
H1/H2/H4/H5 stay correct. A shape-keyed fence skip is
therefore score-neutral at best and would remove the live sites from the gate without gaining a single case
([INFERENCE] for the three live sites the plan names: I did not read them in this control).

## Why the family cannot meet the predicate (mechanism, not luck)

The frozen rule is `case_correct` (`check_infoless_fences.py:448-455`): a pass case needs `status == "PASS"`; a hard
negative needs `status == "FAIL"` **and** `case.head in detail`. A fence-level skip produces one of two states, and
both are wrong for hard negatives:

- zero segments → `check_commands` returns `N/A` ("0 segments: no shell-fenced block lines…",
  `verify_skill_checklist.py:1733-1735`), whose detail never contains the drawn head;
- a vocabulary head inside the fence (only H2 has one, via `ls | tok`) → `PASS`, which is also not `FAIL`.

So no skip can reach `N=T`. The counter also anchors every skip trigger with a hard negative that uses the same
shape: H1 plain head, H2 pipeline, H3 after a table, H4 colon inside an argument, H5 info-bearing fence. That is the
structural reason control 2 tops out at 72 and controls 1/3/4 at base level.

## Premature saturation / partial credit

Control 2 shows the "stop the false FAILs" half of the claim is fully reachable (60/60) with no true-positive work.
The single total (`N of T`) plus the printed split (`pass-expected X of 60; hard negatives Y of 60`) is what prevents
that patch from looking done; keep both in the receipt. A claim scored only on pass-expected cases would have been
met by a shortcut.

## Impacted axes

- **Operability (the axis C2 works):** controls 1/3/4 would turn the live false-FAIL sites into `N/A` rather
  than fixing them ([INFERENCE] from the plan's description of kasegi `SKILL.md:39`, tameshi `:255`, tsukuroi `:263`;
  those files were not read by this seat); on a live run the check's output changes from FAIL to N/A, so the plan's
  byte-identical live-run guard (`plans/round-57.md`, C2 trust boundary) is the second, independent net.
- **Consistency:** control 2 gives the same text two reading rules — inline spans gated on declared vocabulary,
  info-less fences gated on it too — which makes a pipeline inside an info-less fence weaker than the same text
  inline (H2 PASS). That divergence is the hidden regression to reject.
- **Coverage:** a fence-level `shell` gate removes an entire fence class from the gate; the counter's H-classes show
  the loss is not recoverable by any other case.

## Smallest safe correction

None to the frozen counter or the predicate — they hold against this family, and no erratum is needed. The smallest
safe guard is the rejection rule for the falsify wave, already implied by the plan sentence ("must stop those false
FAILs while a real missing command … after a table … still FAILs"): reject any C2 instrument diff that sets the
info-less fence eligibility flag false in `fenced_regions` or filters whole blocks there; the change must be
per-line eligibility inside an info-less fence. Evidence that this is the right line to draw: H3+P1 are only jointly
satisfiable by making table rows non-subjects — raising the four-item detail cap (`verify_skill_checklist.py:1747`)
alone passes H3 but leaves P1 failing, and skipping the fence passes P1 but kills H3.

## Notes

- No tool installs or upgrades (nothing was needed; pacman is paused host-wide).
- No real C2 fix, no real C1 content, no lane edits: only this report and the named raw receipt were written in the
  lane; all code execution happened in the sandbox clone.
