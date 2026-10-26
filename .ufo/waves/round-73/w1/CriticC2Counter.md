# CriticC2Counter — attack on the replacement C2 predicate (round 73, wave 1)

**Verdict: REFUTE before freeze.** The frozen R1–R3 (`plans/round-73-addendum-1.md`) can print
`own-description rules held 3 of 3` for at least nine descriptions that leave the reader-facing render
equal or worse than the base. The cheapest 3-of-3 world inserts one period and a quoted repeat of
`SKILL.md`, then trims 24 characters of domain text (W3B, §F5); a six-edit punctuation/case world changes
the render by two characters (W6, §F1). The cause is structural: R1 measures a sentence definition the
documented truncator never uses, R2's 99-character window is not the render window, and R3 is a tree gate
that is already true at the base (so the claim's real denominator is *two* description rules, not three).
The do-nothing verdict (`1 of 3`) is correct, but its two stated numbers (`151`, `1,019`) come from two
different folds (§F7). The frontmatter-line guard is print-only while 83 `SKILL.md:<line>` citations past
line 19 are content-unchecked by any gate (§F8). As frozen, the claim measures cosmetics, not depth (§F9).

All worlds and scripts: `.ufo/waves/round-73/w1/build/CriticC2Counter/` (`eval_c2.py`, `run_worlds.py`,
`world-walk.txt`, `base-control-recompute.txt`, `counter-world-scores.txt`, `worlds/*.description.txt`).
R3 was evaluated by copying each world's `SKILL.md` into a fleet-shaped sandbox clone of `072048f` and
running the tree's own `check_sibling_census.py` (the construction at `verifiers/check_tip_battery.py:168`),
so every "gate exit" line below is a real gate run, not a reading of the predicate. The drafted counter
itself was also run (drafted in parallel by the ExecDescCounter seat at
`.ufo/waves/round-73/w1/build/ExecDescCounter/check_own_description.py`): every 3-of-3 world below was
committed in the scratch clone and scored by that counter — **all nine read `own-description rules held 3
of 3`, exit 0**, so these are defects of the implemented counter, not of my literal reimplementation
(the scratch clone was deleted after the run; `counter-world-scores.txt` holds the captured output):

```
$ python3 -B .ufo/waves/round-73/w1/build/ExecDescCounter/check_own_description.py \
    --rev <world commit> --repo /tmp/k73w1-.../kotoba-shokunin --fleet /home/vgpnk/Projects/shokunin
== W7_TRIGGER_AFTER_FS  exit=0
R1 pass: first sentence 62 characters is inside 40-99
R2 pass: whole words skill+prompt yes; quoted trigger "skill file", "SKILL.md" (in the Triggers list)
R3 pass: description 931 <= 1024; verifiers/check_sibling_census.py exit 0
frontmatter lines 19->16 (inserted 12, deleted 15 inside the frontmatter)
own-description rules held 3 of 3
== W6_FALLBACK_VACUOUS  exit=0
R1 pass: first sentence 99 characters is inside 40-99
R2 pass: ... quoted trigger "SKILL.md" (in the Triggers list)
R3 pass: description 1021 <= 1024; verifiers/check_sibling_census.py exit 0
frontmatter lines 19->17 (inserted 13, deleted 15 inside the frontmatter)
own-description rules held 3 of 3
== W3B_PUNCT_TRIMMED  exit=0
R1 pass: first sentence 51 characters is inside 40-99
R2 pass: ... quoted trigger "SKILL.md" (in the Triggers list)
R3 pass: description 1010 <= 1024; verifiers/check_sibling_census.py exit 0
own-description rules held 3 of 3
```

(Base with the same harness: `own-description rules held 1 of 3`, exit 1.)

```
$ python3 .ufo/waves/round-73/w1/build/CriticC2Counter/run_worlds.py
== BASE                 N=1 len=1019 R1=False fslen=150 R2=False R3=True
   render : 'Prompt & skill craft — audits, writes, and rewrites SKILL.md / AGENTS.md / dispatch prompts /…'
   gate   : exit=0 rows 20 verified 20 | skill description names 9 of 9 non-none lanes | skill description length 1019 of 1024
== W1_QUOTELIST         N=3 len=960  R1=True fslen=91  R2=True R3=True
   fs     : '"skill file", "prompt craft", "audit this skill", "skill quality" are prompt-craft triggers'
   render : '"skill file", "prompt craft", "audit this skill", "skill quality" are prompt-craft triggers.'
   gate   : exit=0 ... length 960 of 1024
== W2_DOMAIN_EVICTED    N=3 len=1023 R1=True fslen=47  R2=True R3=True
   render : 'Skill and prompt craft for "skill file" authors.'
   gate   : exit=0 ... length 1023 of 1024
== W3_PUNCT_MIN         N=2 len=1031 R1=True fslen=51  R2=True R3=False   (fails only the 1024 cap)
== W3B_PUNCT_TRIMMED    N=3 len=1010 R1=True fslen=51  R2=True R3=True
   fs     : 'Prompt & skill craft — audits, writes, and rewrites'
   render : 'Prompt & skill craft — audits, writes, and rewrites.'
== W4_STUFFED           N=3 len=959  R1=True fslen=90  R2=True R3=True
   render : '"skill file" "skill file" ... skill prompt.'
== W5_TRIGGERS_SHRUNK   N=3 len=897  R1=True fslen=47  R2=True R3=True
   render : 'Skill and prompt craft for "skill file" authors.'   (7 of 8 triggers deleted)
== W6_FALLBACK_VACUOUS  N=3 len=1021 R1=True fslen=99  R2=True R3=True
   render : 'Prompt & skill craft — audits, writes, and rewrites "SKILL.md" / AGENTS.md / dispatch prompts /…'
== W7_TRIGGER_AFTER_FS  N=3 len=931  R1=True fslen=62  R2=True R3=True
   render : 'Prompt and skill craft — audits, writes, and rewrites SKILL.md.'   (no quoted trigger)
== W8_BOUND_99          N=3 len=941  R1=True fslen=99  R2=True R3=True
   render : 'Skill and prompt craft for "skill file" authors who audit and rewrite skill files with care and…'
== W9_QUOTE_ONLY        N=2 len=1021 R1=False fslen=152 R2=True R3=True
== S1A_QUOTE_AFTER_FS   N=3 len=928  R1=True fslen=59  R2=True R3=True   (control wording is false, §F3)
== S1_NOQUOTE           N=2 ... R2=False   S2_UNDER40 N=2 ... R1=False
== S3_NOTINLIST         N=2 ... R2=False   S4_CUT99 N=1 ... R2=False R3=False
== S5_OVER1024          N=0 ... R3=False
3-of-3 worlds: ['W1_QUOTELIST','W2_DOMAIN_EVICTED','W3B_PUNCT_TRIMMED','W4_STUFFED','W5_TRIGGERS_SHRUNK',
                'W6_FALLBACK_VACUOUS','W7_TRIGGER_AFTER_FS','W8_BOUND_99','S1A_QUOTE_AFTER_FS']
W3 frontmatter lines: 16 (base 19, delta -3) -> body citations shift +3
```

The render simulator implements the documented mechanism verbatim
(`corpus/knowledge/render-mechanism-round7.md:17-19`): `s=t.slice(0,99)` then
`o = s.match(/^.*?[.!?](?=\s|$)/)`; "first sentence wins if ≥40 chars" and "else cut `s` at last ASCII
space and append U+2026" (quotes are from that span; dropped bytes between them: the wire code and
`NO ellipsis`). The craft rule the claim cites is `corpus/knowledge/frontmatter-trigger-surface.md:120`
("match-critical WHEN material in the first ≤99 chars", dropped bytes: the rest of rule 8's sentence).

## F1 — R1's fallback is vacuous: any boundary-free description ≥ 99 chars passes R1

R1 says "else the first 99 characters", and the first 99 characters are *always* 99 characters long
when D ≥ 99, i.e. always inside the 40–99 band. W6 is the base description with six case/punctuation
edits and one quote pair (no sentence boundary at all). The counter's own R1 reads the fallback and
passes; the render is 96 characters against the base's 94 — no reader-facing change.

```
== W6_FALLBACK_VACUOUS  N=3 len=1021 R1=True fslen=99 R2=True R3=True
   fs     : 'Prompt & skill craft — audits, writes, and rewrites "SKILL.md" / AGENTS.md / dispatch prompts / sys'
   render : 'Prompt & skill craft — audits, writes, and rewrites "SKILL.md" / AGENTS.md / dispatch prompts /…'
```

The drafted counter prints the same thing on that world: "R1 pass: first sentence 99 characters is inside
40-99" (§ counter output above).

The mechanism's fallback is the opposite: a last-space cut with `…`, which is the failure R1 should be
catching. **Addendum sentence to change:** replace R1's "else the first 99 characters" with
"else the truncator returns a last-space cut, which FAILS R1" and define R1 on the render (see F2).

## F2 — R1's sentence definition is not the truncator's: it passes cuts (W8) and fails good renders (S6)

The mechanism takes `s = D[:99]` *first*, then matches `[.!?]` followed by whitespace or end. R1 instead
searches the whole D for `. ` or `: ` followed by an uppercase letter. Three consequences, each observed:

- W8: a 99-character first sentence whose terminal period sits at offset 99 passes R1 (`fslen=99`) while
  the period is outside `slice(0,99)`; the mechanism returns a last-space cut. 3 of 3 with a cut render.
- S6: `Skill and prompt craft: audits, … "skill file".` has a coherent 94-character render, but R1 reads
  the colon as a sentence end, gets 23 characters and fails (N=1). A legitimate description is punished.
- `!` and `?` are invisible to R1 though the mechanism accepts `[.!?]`.

**Addendum sentence to change:** replace the whole R1 definition with: "R1: run the documented truncator
on D (ws-collapse; return D when `len(D) <= 100`; else `s = D[:99]`, `o = s.match(/^.*?[.!?](?=\s|$)/)`;
return `o` when `len(o) >= 40`, else last-space cut + `…`). R1 holds iff the render is a sentence (`o`
won, no `…` cut) and not a fragment." That single change kills W1/W2/W3B/W6/W7/W8 at once.

## F3 — R2's 99-character window is not the render window; a 3-of-3 description can render zero triggers

When the render is the first sentence (which R1 *forces* by demanding 40–99), every character after that
sentence is discarded, so a quoted trigger at offset 60–99 is counted by R2 and never rendered.

```
== W7_TRIGGER_AFTER_FS  N=3 len=931 R1=True fslen=62 R2=True R3=True
   fs     : 'Prompt and skill craft — audits, writes, and rewrites SKILL.md'
   render : 'Prompt and skill craft — audits, writes, and rewrites SKILL.md.'   (no quoted trigger)
== S1A_QUOTE_AFTER_FS   N=3 len=928 R1=True fslen=59 R2=True R3=True
```

S1A also shows the addendum's shortcut control "a 99-character first sentence with no quoted trigger" is
ambiguous: read as "the first sentence carries no quoted trigger" it is **false** — a 59-character
quote-free first sentence with the trigger at offset ~70 reads 3 of 3.

**Addendum sentences to change:** R2 → "the render contains the whole words `skill` and `prompt` and at
least one double-quoted string that is a member of the Triggers list"; control → "no quoted trigger
anywhere in the first 99 characters".

## F4 — Nothing requires the capability clause, so a trigger-list or a stuffed window scores full

W1's first sentence is only a quoted trigger list; W2 evicts the domain statement (render 48 characters
against the base's 94, which carries `audits, writes, and rewrites … dispatch prompts`); W4 repeats one
quote until the window is stuffed. All read 3 of 3. The rule the claim cites is a *content* rule
("capability clause + match-critical WHEN material"), and none of R1/R2 checks content.

**Addendum sentence to change:** add to R1/R2: "the render contains the capability clause (what the skill
audits/writes) and at least one match-critical WHEN token". This kills W1/W2/W4.

## F5 — The punctuation control (§ Shortcut controls #6) contradicts the kill rule: it reads 3

The addendum says the period-insertion world "must read below 3" and also that it is "judged by the
non-author reviewer for hollowness". Both cannot hold: the frozen rules score it 3 once it fits the cap.
W3 (untrimmed) reads R1=True, R2=True and fails R3 **only** on 1031 > 1024; W3B trims 24 characters of
domain text and reads 3 of 3 with a 51-character fragment render:

```
== W3B_PUNCT_TRIMMED    N=3 len=1010 R1=True fslen=51 R2=True R3=True
   fs     : 'Prompt & skill craft — audits, writes, and rewrites'
   render : 'Prompt & skill craft — audits, writes, and rewrites.'
```

The old 150-character sentence continues after the inserted period (`SKILL.md "SKILL.md" / AGENTS.md / …`),
so the full text is a fragment and the render loses the object of `rewrites`. **Addendum sentence to
change:** keep the control, but state that it must read below 3 **under the render-based R1/R2** (where the
render carries no quoted trigger and no domain statement) and delete the "judged by the non-author
reviewer" hedge — a human judgement is not a counter rule and cannot satisfy "the counter is wrong".

## F6 — R3 is a tree gate already true at base; the claim's real denominator is 2, and R3 is time-varying

`1 of 3` is `R3 only`. R3 is not a description rule and cannot be improved by description craft; it also
duplicates its own length check (`check_sibling_census.py` G4 tests 1–1024 itself), so the counter's
`len(D) <= 1024` never fires independently (S5_OVER1024 fails through R3). The gate also compares the
census lane set to the **live** `*-shokunin` directories under the fleet root (`fleet_lanes` in
`verifiers/check_sibling_census.py`), so the same rev can read 3 today and 2 tomorrow if a lane directory
is added or removed.

```
$ (sandbox of 072048f) python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md
rows 20 verified 20
province rows 20 matched 20
skill description names 9 of 9 non-none lanes
skill description length 1019 of 1024
exit=0
```

The 9 lanes are all `adjacent` (census rows: chousa, kagi, kake, kama, kasegi, kengaku, kotodama,
kumitate, tameshi), so "all 9 `adjacent` lanes" is accurate. **Addendum sentence to change:** either drop
R3 from the count (then the claim is `0 of 2` at base and `2 of 2` is reachable only by the description
rules), or state it as a precondition identical at base and **pin the fleet lane set in the receipt**; and
delete the counter's own `len(D) <= 1024` from R3 so the length rule is one authority, not two. With the
R4 suggested in F8 the count becomes `of 3` (R1, R2, R4) if R3 is dropped, `of 4` if kept.

## F7 — The do-nothing control's two numbers come from two different folds

```
$ python3 (check_sibling_census.description_of on 072048f:SKILL.md)
gate fold (drops block indicator, strips)    len=1019 first-sentence=150 R1=False
fold keeps ">"                               len=1020 first-sentence=151 R1=False
base R2: quotes in first 99 of gate fold: []
```

`151` exists only if the fold keeps the `>` block-scalar indicator — and that fold gives **1020**, not
`1,019`. The addendum's fold ("every whitespace run → one space; the value ends at the first column-0
line") does not say the indicator is dropped or that the value is stripped, although the gate it names
does both (`check_sibling_census.py:391-400`). The drafted counter prints 150 and the ExecDescCounter seat
reached the same correction independently; the addendum text is still the frozen predicate, so it must
carry the reading the counter prints. The verdict is right (R1 fail, R2 fail, R3 exit 0 → 1 of 3) but the
receipt cannot reproduce the stated arithmetic from one fold. **Addendum sentence to change:**
"fold exactly as `check_sibling_census.description_of` (block-scalar indicator dropped, whitespace
collapsed, stripped); at base this gives 150 and 1,019".

## F8 — The frontmatter-line guard is uncounted, and no gate content-checks the 83 line citations

The addendum says "the frontmatter keeps its line count … inserted − deleted lines inside the frontmatter
must be 0; the counter prints `frontmatter lines base→rev`" and, in the next breath, "Guard the counter
prints but the predicate does not count". A print is not a guard: a 3-of-3 world may rewrap the
description and shift every body line while exiting 0.

```
$ grep -rnoE 'SKILL\.md:[0-9]+' corpus PROVINCE.md | awk -F: '{if ($NF>19) c++} END{print c}'
83
$ grep -n 'UFO_POINTER_RE = ' -A 2 verifiers/verify_corpus_integrity.py
146:UFO_POINTER_RE = re.compile(
147-    r"(?<![\w.\-/])((?:/|~|(?:\.\.?/)*)[^\s`\"]*?\.ufo/reports/round-\d+/[^\s`\"]*\.md)"
148-)
```

`verify_corpus_integrity.py:citation_findings` resolves `.ufo/reports/round-N/*.md` pointers and commit
ids; it does not read `SKILL.md:<n>` line numbers at all (and `check_sibling_census.split_path_line` only
parses census-table cells). `verify_skill_checklist.py:1083` does match `file:line`, but only to strip the
anchor (`strip_token_dressing`) before testing that the *path* exists — it never reads the line. Direct
test: add three description lines to the sandbox and the integrity gate's output is byte-identical
(exit 1 both runs; the failure list does not move):

```
$ (sandbox of 072048f) python3 -B verifiers/verify_corpus_integrity.py   # base
base exit=1
$ (same, SKILL.md frontmatter +3 lines) python3 -B verifiers/verify_corpus_integrity.py
shift exit=1
$ diff <(sed 's/:[0-9]*:/:N:/' base.out) <(sed 's/:[0-9]*:/:N:/' shift.out)
(no output)
```

W3B's natural rewrap is 16 frontmatter lines against the base's 19 → −3, which moves all 83 citations.
The drafted counter's own module docstring says this explicitly — "It never changes N or the exit code" —
and the run above prints `frontmatter lines 19->17 (inserted 13, deleted 15 inside the frontmatter)` while
still printing `own-description rules held 3 of 3`, exit 0. **Addendum sentence to change:** "R4: `git diff --numstat <base> <rev> -- SKILL.md` shows 0 inserted and
0 deleted lines inside the frontmatter; the counter exits 1 otherwise."

## F9 — Axis: as frozen this is cosmetics, not depth

`AXES.md:11` defines depth as "Verifiable technical detail — decision tables with real thresholds, named
error signatures, cited sources" with the signal "A reader can act on SKILL.md alone; no filler" (quotes
from that line; dropped bytes: the table-cell separators). The frontmatter description is not the body a
reader acts on, and the addendum itself says the claim "says nothing about any router". The measured delta
is punctuation: W6 changes the render by 2 characters; W3B inserts a period, duplicates `SKILL.md` in
quotes and deletes 24 characters of domain text. Under a render-based R1/R2 the claim *can* be a depth
claim — a reader acting on the description alone then gets the capability clause and one WHEN — but the
frozen rules do not measure that artifact. If the claim is relabelled "consistency" (which is what a
self-audit is), it collides with C3 (consistency) and the plan's "three claims on distinct axes" fails.
**Addendum sentence to change:** state
the depth signal as "the render (first ≤99 chars) states the capability and at least one WHEN, so a
consumer acting on the description alone can route", and measure the render.

## Verified-good (no action)

- Base control verdict: R1 fail (150 > 99), R2 fail (no quoted string in the first 99), R3 exit 0 → `1 of 3`.
- The census gate at `072048f` exits 0 with `rows 20 verified 20`, `9 of 9 non-none lanes`, length 1019.
- The shortcut controls hold when the whole window is controlled: S1 (99-char quote-free sentence)
  2, S2 (first sentence < 40) 2, S3 (quote not in the list) 2, S4 (cut to 48) 1, S5 (1054 chars) 0.
- R2's word requirement is free: the base opener already contains `skill` and `prompt`; W9 shows R2 passes
  from a two-character quote alone, so R2's only cost is quoting an existing member (`SKILL.md`).

## Smallest safe correction (one sentence set, before freeze)

R1 = the documented truncator returns a sentence (not a last-space cut) and the sentence contains the
capability clause. R2 = that render contains the whole words `skill` and `prompt` and a quoted member of
the Triggers list, and the Triggers list still holds the base's eight members. R3 = the sibling-census
gate exits 0 **with the fleet lane set recorded in the receipt**; R4 = frontmatter inserted − deleted
lines = 0. Fold = `check_sibling_census.description_of` exactly; base = 150 / 1,019 / 1 of 4. Drop the
"judged by the non-author reviewer" hedge from shortcut control #6 and make it a counter-kill control.

No files outside `build/CriticC2Counter/` and this report were written; the `/tmp` sandbox was removed.
No tools were installed.
