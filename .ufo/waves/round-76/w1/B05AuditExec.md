# B05AuditExec — kotoba's own description audited against S213

Round 76, wave w1, seat B05AuditExec (executor). **Report only — no lane-file edits.**

Receipt (the citable artifact, every command + output + exit code):
`.ufo/waves/round-76/receipts/description-audit-4de12b61f75c73e3675ef0e422cc2be0f7da8960.txt`
(439 lines, 29552 bytes, sha256 `332530f770c9502aabd595740bdded18c5fe618a3417ce5a7959f6f3ca017ddd`).

## VERDICT

Kotoba's own committed `description` is **COMPLIANT with S213's hard 1024-character
ceiling** (1022 used, 2 chars headroom) and **does state its scope and list its trigger
contexts explicitly** (8 literal trigger strings + an anti-trigger clause). It **FAILS
S213's imperative-phrasing rule** — no imperative trigger clause exists anywhere in the
description — and **FAILS S213's user-intent rule** (410 chars of the 1021-char text,
40.16%, are internal lane-roster and host mechanics once the S213-endorsed boundary clause
is carved out). It is **PARTIAL** on S213's pushy/breadth rule (contexts are listed; the
"user doesn't name the domain directly" half is missing), and it sits at the very top of
the length band.

Measured rev: `4de12b61f75c73e3675ef0e422cc2be0f7da8960`. The `SKILL.md` blob is
`26ce572ed8dad7625083b09236e3a7943bdbbe47` — byte-identical at the round-76 base, the r75
closure tip, the measured rev and the current HEAD, so every number below is
rev-independent for the frontmatter and holds at whatever tip the counters measure.

## The measures (seat spec)

| measure | value |
|---|---|
| rendered length, clip-preserving (the frozen convention) | **1022 chars** |
| rendered length, stripped variant | 1021 chars |
| first-sentence length, excluding terminal period | **150 chars** |
| first-sentence length, including terminal period | **151 chars** |
| first sentence is imperative | **NO** |
| literal trigger string list present | **YES** — 8 literals |
| char budget vs 1024 | **1022 used, 2 headroom (99.80%)** |
| folded description block | **frontmatter lines 4-18 (15 lines)**; line 19 is the closing `---` |
| internal-mechanics span (lane roster + host note) | **410 chars of the 1021-char text (40.16%)**; 411 chars of the 1022-char clip-preserving render (40.22%) |

First sentence (verbatim): *"Prompt & skill craft — audits, writes, and rewrites SKILL.md /
AGENTS.md / dispatch prompts / system prompts for trigger fidelity and decision density"*.
Lead word `prompt` — a label-dash headline, not an imperative verb. `Use this skill when`
does not occur; **0 of 7** sentences lead with an imperative verb.

Literal trigger strings found: `skill file`, `SKILL.md`, `frontmatter description`,
`trigger words`, `prompt craft`, `write a skill`, `audit this skill`, `skill quality`.

## Correction (geometry label) — routed from seat B12EntryDraft

B12 found an off-by-one in my receipt's geometry label: it printed
`description_body_lines = 4-17 (14 lines)` where the committed bytes give **4-18 (15
lines)** — line 17 ends "…omp never reads this", line 18 is `"  text."`, line 19 is the
closing `---`. My own `frontmatter_close_line = 19` already agreed, so the defect was the
`close-4` count expression, not the measurement. **Confirmed and fixed**: the receipt was
regenerated from the scripts (not hand-edited) and now prints
`description_body_lines  = 4-18 (15 lines)` plus `body last line = '  text.'`, and the
summary line carries `folded description block = frontmatter lines 4-18 (15 lines)`.

This matters because C2's R1 names "frontmatter block lines 4–18" and the entry draft
states lines 4–18 too; the receipt label had to agree. **Every measured value is
unaffected** by the fix — 1022/1021, 150/151, 7 sentences, 8 quoted literals, 99.80%,
headroom 2 all reproduce identically, and the r75 closure's own wording ("the folded block
runs lines 4–18 (15 lines)") now matches the receipt exactly.

## Correction (character count) — routed from seat B12EntryDraft

B12 found a second one-character divergence in the same family: I reported the host note
sentence as **88 chars**; the sentence proper is **87**. My 88 included the block's terminal
newline. B12's method was right: `re.split(r'(?<=\.)\s+', desc.strip())`, last element.

Verified against the committed bytes: the note sentence is 87 chars (15 whitespace-separated
words); the same span measured from `Note:` to end-of-render is 88, the extra character
being the folded block's terminal newline — which, per the frozen clip-preserving
convention, belongs to the block, not to the sentence.

**Fix:** regenerated the receipt from the scripts again (not hand-edited) and, rather than
just swapping 88 for 87, made **every** boundary in the internal-mechanics split carry its
own named convention, so no figure in this audit can be read under the wrong rule:

| segment | text proper | as rendered |
|---|---|---|
| `Sibling boundary: kagi, kake, … to the owning lane.` | 154 | 155 (with trailing space) |
| lane roster `chousa owns … tsukuroi owns host package and initramfs hooks` | 322 | 323 (with separating space) |
| host note `Note: shokunin files sit outside … this text.` | **87** | 88 (with block's terminal newline) |

Internal mechanics totals: **410 chars of the 1021-char text (40.16%)**, or **411 chars of
the 1022-char clip-preserving render (40.22%)** — the same span under each convention,
named beside the number. The entry's 87 now matches the receipt's 87.

**No other measure changed:** 1022/1021, 150/151, 7 sentences, 8 quoted literals, 99.80%,
headroom 2 all reproduce identically.

## C1/C2 collision on 1022 — independently verified

Seat B12EntryDraft flagged that C1 and C2 collide on the same number: C2's R1 pins the
description's clip-preserving render at **1022** at the measured tip, so the description
cannot be rewritten this round without breaking R1. I verified this by simulating edits
against the committed bytes and re-rendering each:

| edit to the committed frontmatter | render | R1's "prints 1022" |
|---|---|---|
| baseline (unchanged) | 1022 | HOLDS |
| +1 trailing space on line 4 | 1023 | **FAILS** |
| +1 word on line 4 | 1024 | **FAILS** |
| replace the lead with an imperative clause | 1042 | **FAILS** |
| imperative clause **and** sentence 7 cut | 969 | **FAILS** |
| sentence 7 cut only | 949 | **FAILS** |

**Consequence: the description must not be edited at all this round**, and any future
repair must land on *exactly* 1022 — a cut that over-corrects fails R1 just as surely as an
addition that over-shoots. The entry's "cheapest cut is sentence 7" is therefore a
*repair-shape* note for a future round, not an action for this one; B12's draft records the
same conclusion. This is why C1 as planned admits the rule set and adds a body-craft rule
row while leaving the frontmatter byte-identical, and it is why my findings above are
stated as the measured state of the committed description rather than as a defect to be
fixed here.

## The 1021/1022 fork — independently reproduced

Two YAML render paths over the *same* committed bytes differ by exactly one character (the
folded block's trailing newline). Four independent paths were run:

| path | len |
|---|---|
| P1 naive `split('---', 2)` | 1022 |
| P2 line-join, trailing newline dropped | **1021** |
| P3 faithful document bytes (each body line newline-terminated) | **1022** |
| P4 raw slice keeping line ends | 1022 |

The lane's own `verifiers/verify_skill_checklist.py` prints `description 1021 chars` (it
strips); the frozen predicates keep the newline and read **1022**. This is exactly the fork
`plans/round-76-addendum-1.md` § "Render-length convention (off-by-one closure)" closes —
**clip-preserving = 1022**. My run reproduces the L1's numbers and the r75 closure's
measurement (`corpus/lessons/round-75-verifier-spotcheck.md:63`, "renders **1,022 chars**
… first sentence **151 chars**"). The receipt prints **both** variants and names the
convention, per that addendum.

**Actionable for the counters:** `check_desc_craft.py` conjunct (d) and
`check_r75_routed_repairs.py` R1 must recompute with the **clip-preserving** convention to
print 1022. A counter that strips will print 1021 and fail its own frozen target. The
`check_sibling_census.py` `description_of` helper also strips — it is a different guard for
a different purpose and must not be copied as the C1 (d) recompute.

## Rules verified against the pinned bytes

`build/quotes-s213.md` (seat B04) existed, so I used it — and independently re-verified it.
All **13/13** located rules occur verbatim in the pinned snapshot
`.ufo/waves/round-76/snapshots/optimizing-descriptions.md`
(sha256 `7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837`, 13403 bytes),
matching `snapshots/MANIFEST.sha256` and the HTTP-200 record in `snapshots/fetch-record.json`.
My own independent fetch of the URL returned HTTP 200 and a **byte-identical** digest.

I also fetched the page myself (as the seat brief allows when the build file is absent) and
confirmed the rules in the source text rather than trusting the table.

## Verdict table (rule -> measure -> verdict)

| S213 rule | verdict |
|---|---|
| 1-2 imperative phrasing (L25) | **FAIL** — no imperative trigger clause anywhere (not merely not-first) |
| 3 user intent, not implementation (L26) | **FAIL**, with a documented carve-out (see below) |
| 4-5 pushy / breadth (L27) | **PARTIAL** — contexts listed; "even if the user doesn't name it" clause absent |
| 6-8 triggering burden / scope coverage (L17, L45, L155) | **PASS in kind**; the eval-driven half is not evaluable (plan holds the experiment) |
| 9-10 concision (L28) | **FAIL (marginal)** — 7 sentences, 99.80% of cap, 2 chars headroom |
| 11-12 hard ceiling 1024 (L28, L159) | **PASS** — 1022 ≤ 1024 |
| 13 anti-overfit (L157) | **PASS, no violation observed** — the 8 literals are hand-authored scope labels, not harvested from failed queries |

**Calibration on rule 3.** The description splits into (A) scope + trigger list 456 chars,
(B) the S213-style boundary clause `Sibling boundary: kagi, kake, … to the owning lane.`
154 chars (text proper) — 155 with its trailing space, (C) lane roster `chousa owns the
research method … tsukuroi owns host package and initramfs hooks` 322 chars (text proper)
— 323 including the separating space, (D) host note `Note: shokunin files sit outside the
omp discovery roots, so omp never reads this text.` **87 chars** (the sentence proper,
15 words) — 88 as rendered, including the block's terminal newline.

Internal mechanics therefore totals **410 chars on the text basis** (roster 322 + 1
separating space + note 87, of the 1021-char text) = **40.16%**, and **411 chars on the
render basis** (roster..end of the clip-preserving render, including the terminal newline,
of the 1022-char render) = **40.22%**. Each figure is quoted under its own convention so
the two cannot be conflated — the same discipline the 1022/1021 fork required.

S213 itself endorses a boundary clause at page L156 ("Add specificity about what the skill
does *not* do, or clarify the boundary between this skill and adjacent capabilities"), so
the `Sibling boundary:` clause is S213-consistent and is **not** counted against the
description; the roster + host note are.

**Calibration on rule 1.** `build/quotes-s213.md` records "front-loading the use case" and
"self-contained first sentence" as **ABSENT** from S213, and S213's own worked example puts
the imperative clause *second*. The failure is therefore not "not first" but "**absent
entirely**" — the description has no imperative trigger clause in any position.

## Lane's own checklist (house measures on the same text)

`python3 -B verifiers/verify_skill_checklist.py --json` → **pass 11, fail 0, exit 0**.
Trigger boxes: `frontmatter_parses` PASS ("description 1021 chars" — the stripped
convention), `literal_trigger_string` PASS ("carries literal 'Triggers:'"),
`anti_trigger_clause` PASS (vocabulary test only — the guard's own docstring says a vacuous
exclusion passes and an unlisted real exclusion fails), `line_budget` PASS (590 ≤ 600),
`no_xml_tag` PASS, `name_directory` PASS, `no_placeholder` PASS, `command_binary_resolves`
PASS, `citation_resolves` PASS.

Note the lane's `anti_trigger_clause` is a **vocabulary** test, so it cannot distinguish a
real exclusion from a token — the semantic quality of the anti-trigger list is outside what
the committed guards measure.

## Risks

1. **Headroom risk (live).** 2 chars under the spec cap. S213 warns "descriptions tend to
   grow during optimization". Any future addition breaches the ceiling; an eval-driven
   rewrite is the most likely trigger. This is the one finding that could turn a PASS into a
   FAIL without anyone editing deliberately.
2. **Conjunction risk on the C1 (d) recompute.** The counter must use the clip-preserving
   convention. A stripping implementation prints 1021 and fails its own frozen target —
   exactly the M75-1 off-by-one family the addendum closed.
3. **Import risk in the entry.** If `corpus/knowledge/description-craft-round76.md` writes
   "front-load the use case" or "self-contained first sentence" as sourced rules, that is an
   unsourced upgrade — `quotes-s213.md` records both as ABSENT from S213. Strike them or mark
   `[INFERENCE]`.
4. **Eval claims stay held.** Rule 8's eval-driven half and S213's trigger-rate protocol
   remain unevaluated; the round-76 plan holds them. Nothing in this audit should be read as
   a trigger-rate measurement.
5. **The description is frozen this round by C2's R1 pin.** Verified above: any edit to the
   frontmatter breaks R1's 1022 predicate unless it lands exactly on 1022. The imperative-gap
   and user-intent findings are therefore real but *unfixable this round*; they route to a
   future round, and the repair must be sized to land on 1022 exactly.

## Scope and honesty

- Report-only seat. **No lane file was edited.** The two files written are this report and
  the receipt, both inside `.ufo/waves/round-76/`.
- Every number in this report and in the receipt comes from a command that was actually
  executed and captured in the receipt with its output and exit code (17 command/exit-code
  pairs recorded). Nothing is transcribed by hand.
- Read-only git only (`rev-parse`, `log`, `status`, `diff`, `show`). No commit, push, add,
  stash or checkout anywhere. No jj write. No fleet-root file touched.
- Tools installed: none. No `pacman`, no `uv tool install`, no downloads beyond the two
  `curl` fetches of the S213 URL (HTTP 200, digest already pinned by the lane).
- Scratch used: `/fast/scratch/hyaku/kotoba-r76/B05AuditExec/` (audit scripts + fetched
  page). **Removed before yield** — see the cleanup note below.

## Files written

- `.ufo/waves/round-76/receipts/description-audit-4de12b61f75c73e3675ef0e422cc2be0f7da8960.txt`
- `.ufo/waves/round-76/w1/B05AuditExec.md` (this file)

## Check the main agent should run

The frozen counters, on the tip rev, once the L1 has landed the wave:

```
python3 -B verifiers/check_desc_craft.py --rev <tip>        # expect: description craft backed 6 of 6, exit 0
python3 -B verifiers/check_r75_routed_repairs.py --rev <tip> # expect: r75 routed repairs closed 4 of 4, exit 0
```

and, for the C1 (d) recompute specifically, confirm the counter prints **1022** (not 1021)
for the description length and that the entry's audit table carries the same two numbers
(1022 clip-preserving, 1021 stripped) and the same convention name. My receipt § 2 and § 3
give the exact values to compare against.
