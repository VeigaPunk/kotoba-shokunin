# ScoutS210Live — round 70 wave 1 (S210 re-opened live)

**Verdict: S210 HOLDS.** The live page is byte-identical to the committed snapshot. F7's quote appears
verbatim at page line 92. Ten of the eleven S210-cited prose claims state the page faithfully. One
sentence overclaims: entry line 44, "the specification states it independently". Two wording points
are minor drifts, not falsifications: F7's "0.5 by default", and the `source:` header omitting
§ The optimization loop. One structural gap: no verifier guards the prose claims (lines 40–44). C2's
`check_skill_evals.py` counts only the eight quotes.

Measured at tip `16b212a390c7ce68b6bce49b2c3766b154fbcbae` (equal to the lane HEAD). The entry and
SOURCES.md have no diff against the tip (`git diff --stat 16b212a… -- corpus/knowledge/skill-eval-artefacts-round70.md corpus/SOURCES.md` printed nothing).

## 1. The live page equals the snapshot

```
$ D=$(mktemp -d /tmp/k70w1-ScoutS210Live.XXXX); curl -fsSL https://agentskills.io/skill-creation/optimizing-descriptions.md -o $D/page.md; echo exit=$?
exit=0                                   (fetched Sun 25 Oct 2026 11:56:04 UTC)
$ wc -c page.md       -> 13403
$ sha256sum page.md   -> 7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837
$ sha256sum .ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md -> 7cc54fbb…bfd837 (same)
$ cmp snapshot page.md && echo IDENTICAL -> IDENTICAL
```

The size (13 403 B) and the sha256 prefix `7cc54fbb…` match the entry's `source:` line 2 and SOURCES.md row
S210 (line 151). Every page line number below therefore applies to the committed snapshot too.

```
$ python3 -B verifiers/check_skill_evals.py --rev 16b212a390c7ce68b6bce49b2c3766b154fbcbae --fetch; echo exit=$?
measured-rev: 16b212a390c7ce68b6bce49b2c3766b154fbcbae
skill eval facts backed 8 of 8
live quotes found 8 of 8
exit=0
```

## 2. Claim-by-claim (page line numbers come from `grep -nF … page.md` on the live fetch)

Page headings: `## Designing trigger eval queries` L30, `## Testing whether a description triggers` L77,
`### Running multiple times` L88, `## Avoiding overfitting with train/validation splits` L136,
`## The optimization loop` L149.

| # | Entry claim (file:line) | Page line (verbatim) | Verdict |
|---|---|---|---|
| 1 | F7 quote, entry:25 `"A should-trigger query passes if its trigger rate is above a threshold (0.5 is a reasonable default)."` | L92 "A should-trigger query passes if its trigger rate is above a threshold (0.5 is a reasonable default)." | **Verbatim.** 17 words, matching SOURCES row S210's "(17 words)". The location "Running multiple times subsection of Testing whether a description triggers" is correct (L88 under L77). |
| 2 | F7 fact, entry:25: "…a should-not-trigger query passes below it." | L92 "A should-not-trigger query passes if its trigger rate is below that threshold." | **Faithful.** |
| 3 | F7 fact, entry:25: "…trigger rate over repeated runs…" | L90 "Run each query multiple times (3 is a reasonable starting point) and compute a **trigger rate**: the fraction of runs where the skill was invoked." | **Faithful.** Support comes from L90, outside the quote. |
| 4 | F7 fact, entry:25: "the threshold, 0.5 by default" | L92 "(0.5 is a reasonable default)" | **Minor drift (low).** The page recommends 0.5 as a reasonable choice and configures nothing. "by default" can read as a normative default. Suggested wording: "0.5 suggested as a reasonable default". This doesn't change the F7/F8 disagreement, which depends on "above" against `>=`, not on the value 0.5. |
| 5 | entry:40 "About 20 queries" | L41 "Aim for about 20 queries: 8-10 that should trigger and 8-10 that shouldn't." | **Faithful.** |
| 6 | entry:40–41 "8–10 that should trigger and 8–10 that should not" | L41 (same line) | **Faithful.** |
| 7 | entry:41 "each with `should_trigger`" | L32 "realistic user prompts labeled with whether they should or shouldn't trigger your skill"; L36–37 `"should_trigger": true` / `false` | **Faithful.** |
| 8 | entry:41 "run each about 3 times and score the rate (F7)" | L90 "(3 is a reasonable starting point)"; also L94 "With 20 queries at 3 runs each, that's 60 invocations" and L100 `RUNS=3` | **Faithful.** "about 3" is a fair reading of "a reasonable starting point". The pointer is loose: the 3-runs evidence is L90, while F7's quote (L92) contains no run count. |
| 9 | entry:42 "keep ~40% as a validation set" (the ~60/40 split) | L142 "**Train set (\~60%)**: the queries you use to identify failures and guide improvements."; L143 "**Validation set (\~40%)**: queries you set aside and only use to check whether improvements generalize." | **Faithful.** |
| 10 | entry:42 "…that never guides edits" | L153 "Only use train set failures to guide your changes — whether you're revising the description yourself or prompting an LLM, keep validation set results out of the process." | **Faithful.** The page still *evaluates* validation every iteration (L151 "Evaluate the current description on both *train and validation sets*"); it just never uses those results to guide changes, so the entry's wording holds. |
| 11 | entry:42–43 "pick the best iteration by validation pass rate, not the last one" | L161 "**Select the best iteration** by its validation pass rate — the fraction of queries in the *validation set* that passed. Note that the best description may not be the last one you produced; an earlier iteration might have a higher validation pass rate than later ones that overfit to the train set." | **Faithful,** read as "rather than defaulting to the last one". The page says the best *may not be* the last. A reader taking the entry as "never the last" would overread it, but the selection rule itself is stated correctly. |
| 12 | entry:43 citation "(S210 § Avoiding overfitting, § The optimization loop)" | L136 and L149 both exist | **Correct citation, header gap (low).** The entry's `source:` line 2 lists only § Designing trigger eval queries, § Testing whether a description triggers and § Avoiding overfitting. It omits § The optimization loop (L149), which the body relies on for claim 11 (L161) and claim 10 (L153). |
| 13 | entry:43–44 "This matches the skill-creator loop the lane already held (S124) — the specification states it independently." | L166–167 "> [!TIP] … The [`skill-creator`](https://github.com/anthropics/skills/tree/main/skills/skill-creator) Skill automates this loop end-to-end: it splits the eval set, evaluates trigger rates in parallel, proposes description improvements using Claude, and generates a live HTML report you can watch as it runs." | **OVERCLAIM (moderate).** The "matches" half holds. SOURCES row S124 (line 135) reads "held-out eval loop: 20 labelled queries, a 60/40 train/test split, 3 runs per query, up to 5 iterations", and S210 states the same numbers (L41, L90, L142–143, plus L163 "Five iterations is usually enough"). The "independently" half is contradicted by the page itself: S210 names skill-creator and links to it as the automation of *this* loop. The two sources are linked, not independent, so their agreement is one protocol stated twice, not corroboration. Suggested wording: "the specification states the same protocol and names skill-creator as its automation (S210 L167)". |

The F7/F8 disagreement section (entry:47–56) cites S210 only for the strict "above"/"below" wording, and
L92 is faithful there. S210's own example script (L97–129) computes `trigger_rate` (L128) but applies no
pass rule, so the page holds no second rule that conflicts with L92. The disagreement stands as written
on the S210 side. I did not re-open S211's `>=` (lines 230–234) or its default (line 266); that is outside
this item.

## 3. Structural gap: the prose claims are unguarded

```
$ sed -n '195,235p;270,300p' verifiers/check_skill_evals.py
```

`SNAP_TEXT["S210"]` (around line 206) and `HONEST_QUOTES["F7"]` (line 218) carry only the F7 quote. The
broken-world table (lines 270–300) mutates quotes, rows and the `source:` line, but no claim in entry
lines 40–44 has a check. If someone edited "8–10" to "5–6" or "~40%" to "~20%", the count would still
read `8 of 8`. C2 counts facts F1–F8 by design (plan C2), so this is a scope note, not a C2 failure. The
claims in rows 5–13 above are backed only by this report and the snapshot.

## 4. Observed vs. inferred vs. unresolved

- **Observed:** live fetch = snapshot (sha256 + `cmp`); every page line quoted above (from `grep -nF` on the
  live file); verifier `8 of 8`, `live quotes found 8 of 8`, exit 0; S124 row text (SOURCES.md:135).
- **Inferred (reading):** claim 4's "by default" drift and claim 11's "not the last one" reading are
  judgements about wording. Claim 13's overclaim rests on page L167, which I observed; that the sources
  are therefore not independent evidence is my inference from it.
- **Unresolved:** I did not re-fetch S124's skill-creator `SKILL.md` to confirm the row's "60/40 train/test" text
  against the upstream file. I relied on the SOURCES.md row text.

## Tooling

No installs or updates. I used curl, sha256sum, cmp, grep, git (read-only) and python3, all already present.
Scratch dir `/tmp/k70w1-ScoutS210Live.UgFq` was deleted before returning. No committed lane file was modified.
