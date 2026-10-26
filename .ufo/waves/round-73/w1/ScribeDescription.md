# ScribeDescription — round 73, wave 1 (C2 replacement: SKILL.md's own description)

**Verdict.** Three replacement `description` drafts built, all three gate-clean, one picked (B). The pick is
`build/ScribeDescription/description.md`. Two wave-1 findings ride with it: (1) the seat item's "exactly 18
lines" is off by one against the observed base (19) and against the addendum's own line-count guard, so the
deliverable keeps 19 lines and ships 18-line variants only as a switchable alternative; (2) the frozen R1 has a
fallback that a run-on description passes, so a shortcut world scores 3 of 3 under the predicate as written —
this must be fixed before any C2 data, per the addendum's own kill rule.

Everything below is re-measured here, not inherited. No lane file was modified; no counter exists yet
(`verifiers/check_own_description.py` absent at the tip), so the frozen predicate itself was **not run**.

## 0. Surfaces read

- `plans/round-73.md` (C2 as originally written), `plans/round-73-addendum-1.md` (E1, replaces C2).
- `corpus/knowledge/frontmatter-trigger-surface.md:60-130` (render measurement + rules 1-12).
- `verifiers/check_sibling_census.py` (`description_of`, `split_clauses`, `marker_in`,
  `skill_description_failures` — read, not modified).

## 1. Base state, re-measured

```
$ python3 -B -c 'import re,pathlib;s=pathlib.Path("SKILL.md").read_text().split("\n");e=s.index("---",1);d=re.sub(r"\s+"," "," ".join(s[3:e])).strip();m=re.search(r"[.:]\s+(?=[A-Z])",d);f=d[:m.start()+1] if m else d[:99];print("folded=%d lines=%d first_sentence=%d quotes_in_first99=%s prompt_word=%s skill_word=%s" % (len(d), e+1, len(f), re.findall(r"\"([^\"]*)\"", d[:99]), bool(re.search(r"(?<![a-z0-9-])prompt(?![a-z0-9])", d[:99], re.I)), bool(re.search(r"(?<![a-z0-9-])skill(?![a-z0-9])", d[:99], re.I))))'
folded=1019 lines=19 first_sentence=151 quotes_in_first99=[] prompt_word=True skill_word=True
```

Reading: the base fails R1 (first sentence 151 > 99) and fails R2 on the quoted-string half only (the first 99
contains `Prompt` and `skill` as whole words, case-insensitively, but no double-quoted span). R3 holds — the
census gate exits 0 at the base (§3). So the addendum's do-nothing figure `1 of 3` is reproduced from the rule
text, not from a counter. The base is also the current text: `git diff 072048fa…..HEAD -- SKILL.md` is empty,
and `md5sum` of `SKILL.md` in a `--shared` sandbox of `072048f` equals the live file
(`fb278ea01f3b3e36d5aa48f8b64693f0` both).

## 2. Finding F1 — line count: the base is 19, not 18

`lines=19` above, and `s.index("---",1)` = 18 ⇒ fences + `name:` + `description: >` + **15** folded body lines
= 19. The seat item says "exactly 18 lines"; 18 forces a 14-line body. Frontmatter-only diff against the base
(`head -19 SKILL.md` vs `head -19`/`head -18` of each draft, `git diff --no-index --numstat`):

```
A          inserted=15 deleted=15 net=0
B          inserted=15 deleted=15 net=0
C          inserted=15 deleted=15 net=0
A_18line   inserted=14 deleted=15 net=-1
B_18line   inserted=13 deleted=14 net=-1
C_18line   inserted=11 deleted=12 net=-1
```

The addendum's guard is net-zero, not zero-insertions: `plans/round-73-addendum-1.md:47` — sed output:
`Guard the counter prints but the predicate does not count: the frontmatter keeps its line count, so every`
(and the next line continues `SKILL.md:<line> citation after it stays valid`). Its stated purpose is to keep
every `SKILL.md:<line>` citation valid; a net −1 line does exactly the damage the guard names. **Decision:** the
deliverable keeps 19 lines (net 0). The 18-line variants are built, measured and gate-tested
(`candidates/*-18line.md`, identical folded length, same exit 0) so the L1 can switch if the counter as landed
literally checks 18. This is a conflict between the item and the frozen addendum, recorded, not silently
resolved.

## 3. The three candidates

Common rewrap: 2-space indent, `textwrap` width chosen so the body is exactly 15 lines; folded text is
wrap-invariant (asserted `' '.join(lines) == folded`).

Counts (`python3 -B -c` on the deliverable files, exact output):

```
candidates/A.md          lines=19 body=15 folded=1002
candidates/B.md          lines=19 body=15 folded=1015
candidates/C.md          lines=19 body=15 folded=992
candidates/A-18line.md   lines=18 body=14 folded=1002
candidates/B-18line.md   lines=18 body=14 folded=1015
candidates/C-18line.md   lines=18 body=14 folded=992
description.md           lines=19 body=15 folded=1015
```

First sentences / first-99 evidence (same metrics routine as §1):

| draft | folded | first sentence | chars | quoted span in first 99 | in Triggers list |
|---|---|---|---|---|---|
| A | 1002 | `Rewrites a skill or prompt for trigger fidelity on "skill file".` | 64 | `"skill file"` | yes |
| B | 1015 | `Audits a skill or prompt file's trigger surface — ask "audit this skill".` | 73 | `"audit this skill"` | yes |
| C | 992 | `Audits a skill or prompt for trigger fidelity — start at "prompt craft".` | 72 | `"prompt craft"` | yes |

All three: whole words `skill` and `prompt` in the first 99 (lower-case `prompt` — so R2 holds under a
case-sensitive or a case-insensitive reading); `Triggers:` list with its 8 quoted strings intact;
`Anti-triggers:` clause intact; the nine adjacent lanes each inside a clause carrying an ownership/routing
marker; the omp-discovery-roots `Note:` intact; folded ≤ 1024.

### Candidate A — closest to the base (1002)

```
Rewrites a skill or prompt for trigger fidelity on "skill file". Also audits AGENTS.md, dispatch prompts and system prompts for decision density. Triggers: "skill file", "SKILL.md", "frontmatter description", "trigger words", "prompt craft", "write a skill", "audit this skill", "skill quality". Anti-triggers: general prompt engineering for model outputs (not skill files), runtime code changes, and domain content inside a skill's reference/ tree. Sibling boundary: kagi, kake, kasegi, kengaku and kumitate own their SKILL.md content; this skill audits and reports; fixes route to the owner. chousa owns the research method; kama owns endpoint verification; kengaku owns measured capability effects of prompt format; tameshi owns the fixture and mutation method. NOT kotodama-shokunin: kotodama owns naming and language for fictional worlds despite the similar name. Note: shokunin files sit outside the omp skill discovery roots, so this text never reaches the omp router — craft here is audit-side.
```

### Candidate B — trigger-first (picked; 1015)

```
Audits a skill or prompt file's trigger surface — ask "audit this skill". Writes and rewrites SKILL.md, AGENTS.md, dispatch and system prompts for decision density. Triggers: "skill file", "SKILL.md", "frontmatter description", "trigger words", "prompt craft", "write a skill", "audit this skill", "skill quality". Anti-triggers: general prompt engineering for model outputs (not skill files), runtime code changes, and domain content inside a skill's reference/ tree. Sibling boundary: kagi, kake, kasegi, kengaku and kumitate own their SKILL.md content; audits and reports here, fixes route to the owner. chousa owns the research method; kama owns endpoint verification; kengaku owns measured capability effects of prompt format; tameshi owns the fixture and mutation method. NOT kotodama-shokunin: kotodama owns naming and language for fictional worlds despite the similar name. Note: shokunin files sit outside the omp skill discovery roots, so this text never reaches the omp router — craft here is audit-side.
```

### Candidate C — tightened (992)

```
Audits a skill or prompt for trigger fidelity — start at "prompt craft". Then checks SKILL.md, AGENTS.md, dispatch and system prompts for decision density. Triggers: "skill file", "SKILL.md", "frontmatter description", "trigger words", "prompt craft", "write a skill", "audit this skill", "skill quality". Anti-triggers: general prompt engineering for model outputs (not skill files), runtime code changes, and domain content in a skill's reference/ tree. Sibling boundary: kagi, kake, kasegi, kengaku and kumitate own their SKILL.md content; audits and reports here, fixes route to the owner. chousa owns the research method; kama owns endpoint verification; kengaku owns measured capability effects of prompt format; tameshi owns the fixture and mutation method. NOT kotodama-shokunin: kotodama owns naming and language for fictional worlds (similar name). Note: shokunin files sit outside the omp skill discovery roots, so this text never reaches the omp router — craft here is audit-side.
```

### Gate runs (fleet-shaped sandbox, `--skill` = the deliverable file)

Sandbox: `P=$(mktemp -d /tmp/k73fleet-ScribeDescription.XXXX)`; every entry of `/home/vgpnk/Projects/shokunin`
except `kotoba-shokunin` symlinked in; `git clone --shared -q --no-checkout … $P/kotoba-shokunin`;
`git -C $P/kotoba-shokunin checkout -q 072048f…`; `git rev-parse HEAD` = `072048fa8e8a52c707d25f7079772fa317244eb7`;
`git status --porcelain` empty. Run from `$P/kotoba-shokunin`:

```
$ python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill "$B/candidates/B.md"
rows 20 verified 20
province rows 20 matched 20
skill description names 9 of 9 non-none lanes
skill description length 1015 of 1024
exit=0
```

Per file, exit and last three lines (each run re-executed after the deliverable copy, not transcribed):

```
A         exit=0  9 of 9 non-none lanes / length 1002 of 1024
B         exit=0  9 of 9 non-none lanes / length 1015 of 1024
C         exit=0  9 of 9 non-none lanes / length 992 of 1024
A-18line  exit=0  9 of 9 non-none lanes / length 1002 of 1024
B-18line  exit=0  9 of 9 non-none lanes / length 1015 of 1024
C-18line  exit=0  9 of 9 non-none lanes / length 992 of 1024
description.md exit=0  9 of 9 non-none lanes / length 1015 of 1024
```

Reference arm: the base `SKILL.md` without `--skill` also exits 0 (`rows 20 verified 20`, `province rows 20
matched 20`), so the census itself is unmoved. One hermetic arm (`--fleet $P`) on B: identical output, exit 0.

## 4. The gate is live on these drafts (negatives, all exit 1)

Mutations were applied to the *folded* text and re-wrapped, so the change was guaranteed present. First attempt
failed for a boring reason worth recording: two replacements were no-ops because the literal straddled a wrap
boundary (length stayed 1015) — a pass from a no-op mutation is not evidence, so they were re-issued.

| world | change | observed |
|---|---|---|
| `mut_nokotodama` | delete ` NOT kotodama-shokunin: …` | `FAIL skill description does not name the non-none census lane kotodama`, `names 8 of 9`, exit 1 |
| `mut_nomarker` | three lanes to a bare list `kama, kengaku, tameshi` | `FAIL … lane kama, but no clause that names it carries an ownership or routing marker …`, `FAIL … lane tameshi …`, `names 7 of 9`, exit 1 |
| `mut_long` | pad folded text to 1036 | `FAIL skill description length 1036 is outside 1-1024 characters (S018…)`, exit 1 |
| `mut_renamed` | `kake` → `kabuki` | `FAIL skill description does not name the non-none census lane kake`, `names 8 of 9`, exit 1 |

So the 9-of-9 and the length line are measurements of the drafts, not of an inert gate. (`mut_nomarker` naming
only two lanes is the checker's documented lexical approximation in the other direction: `kengaku` also sits in
the sibling-boundary clause, which carries `own`, so it still counts — dumped clauses:
`kengaku -> [('Sibling boundary: kagi, kake, kasegi, kengaku and kumitate own their S', True), ('kama, kengaku, tameshi.', False)]`.)

## 5. Pick — B, and what a reader loses against the base

Chosen: **B**. Ground: `corpus/knowledge/frontmatter-trigger-surface.md:68-69` (sed) —

```
deterministic truncator keeps at most 99 chars — first sentence wins if ≥40
chars, else last-space cut + `…`. Measured over the live 17-skill omp
```

— and `:119-120` (sed):

```
   is 55–96 (last-space back-off). Put the capability clause + the most
   match-critical WHEN material in the first ≤99 chars; everything later is
```

B's 73-char first sentence renders whole whenever the truncator (not the compressor) renders, and it is the only
one of the three whose surviving hint carries an invocation-shaped literal (`"audit this skill"`) rather than a
topic noun. The base's first 99 chars carried **no** quoted span at all (§1).

Cost, stated plainly:

- The base's rendered hint named the four artefact types (`SKILL.md / AGENTS.md / dispatch prompts / system
  prompts`) and the audit-write-rewrite triad. B moves the artefact list into sentence 2 — invisible under the
  truncator, reachable only if the session's compressor row exists (rule 8's caveat) — and drops the words
  `trigger fidelity` from sentence 2 because sentence 1 already says `trigger surface`.
- B is the tightest of the three against the cap: 1015 leaves 9 characters under 1024 (A 22, C 32). Any future
  edit to B must be funded by a deletion.
- C is the better choice if headroom or a tighter folded body is valued over the invocation-shaped hint; its
  price is compressing the kotodama disambiguation to `(similar name)`, losing the reason (`despite the similar
  name`).
- A is the closest to the base clause for clause (triggers, anti-triggers, sibling clause, note), but not
  verbatim: the 1024 cap funded the new first sentence with two trims — `own their own` → `own their` and
  `the owning lane` → `the owner` — and the old first sentence was re-cut into `Rewrites …` + `Also audits …`.
  Its hint verb `Rewrites` narrows a lane that audits and reports; the audit framing survives only below the
  cliff, which is the worse side of the trade.

**Calibration:** the choice between A, B and C is *not* distinguished by any frozen rule — all three score
R1/R2/R3 (§6, F3). The pick is craft, and should be reviewed as craft.

## 6. Wave-1 attacks on C2's predicate

### F2 (must be fixed before data) — R1's fallback makes a run-on pass

`plans/round-73-addendum-1.md:39-40` (sed of both lines, dropping the leading `- **R1** the first sentence of
D` prefix so the quote stays under 25 words):

```
the text before the first `. ` or `: ` followed by an uppercase letter, else
the first 99 characters
```

R1 in full: that span "is between 40 and 99 characters long" (same lines).

World `D'` = B with every post-period capital lowercased (so no `[.:] ` + uppercase exists anywhere) and the
`NOT kotodama-shokunin` prefix folded into its clause (folded 1016, 15 body lines):

```
{"folded_len": 1016, "sentence_split_found": false, "first_sentence_len": 99,
 "first_sentence": "Audits a skill or prompt file's trigger surface — ask \"audit this skill\". writes and rewrites SKILL",
 "rules": {"R1": true, "R2": true, "R3_len": true}}
```

Shaping note: the printed JSON is condensed here — `first99` dropped (it equals the truncated
first-sentence text), keys pulled onto one line, `\u2014` rendered as the em dash. `$S` in the next command is
the deleted scratch dir (`/tmp/k73w1-ScribeDescription.yf8p`); the world was a 19-line frontmatter block.

And its R3 second half, run in the fleet-shaped sandbox of `072048f`:

```
$ python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill "$S/SKILL_D_shortcut_runon.md"
province rows 20 matched 20
skill description names 9 of 9 non-none lanes
skill description length 1016 of 1024
exit=0
```

N = 3. A single run-on sentence whose rendered hint dies mid-phrase (`…writes and rewrites SKILL`) satisfies
the rules as written. Under the addendum's kill rule ("any shortcut world scoring 3 means the counter is wrong;
fixed before data") this is a counter defect, not data. Suggested tightening (L1's call): R1 fails when no
`[.:] ` + uppercase end exists inside the first 99, i.e. drop the fallback-pass and treat absence of a sentence
end as a miss: without the fallback, R1's lower bound (≥40) is still testable, and its upper bound stops being
satisfiable by a truncation artefact. This is a counter fix, not a rule edit — the addendum's R1 sentence is
what would change, so it belongs to the L1 before data.
No such world was scored as claim data; nothing here edits the addendum.

### F3 — R2 cannot see trigger quality, so the three drafts are score-identical

R2 accepts *any* member of the `Triggers:` list inside the first 99, so a topic noun (`"skill file"`,
`"prompt craft"`) passes as fully as an imperative (`"audit this skill"`). The predicate therefore does not test
the craft the lane teaches (rule 3 implicit-intent, rule 11 invocation-shaped triggers). Consequence for wave 2:
do not grade the description drafts by the counter alone; the drafts' difference is unmeasured by design.

### F4 — untested controls, declared as untested

The addendum's shortcut world "the first sentence made short by inserting a period mid-phrase while the old
151-character sentence continues after it" (judged by a non-author reviewer for hollowness) was **not** built
here. Not built = not claimed. The do-nothing world was checked only via §1's rule reimplementation, because the
frozen command does not exist:

```
$ git cat-file -e HEAD:verifiers/check_own_description.py ; echo exit=$?
fatal: path 'verifiers/check_own_description.py' does not exist in 'HEAD'
exit=128
```

## 7. Bounds, provenance, cleanup

- Read-only on every committed lane file: `git diff --stat` in the lane is empty after all work; `SKILL.md`
  md5 unchanged; no git or jj write outside the throwaway sandbox (clone/checkout happened only inside
  `$P/kotoba-shokunin`); no network fetch; no tool installed or upgraded.
- Scratch: `S=/tmp/k73w1-ScribeDescription.yf8p` (builders, candidate bodies, mutants),
  `P=/tmp/k73fleet-ScribeDescription.SGpu` (fleet-shaped sandbox). Both removed before returning.
- Deliverables (sha256):
  - `build/ScribeDescription/description.md` = `00961b3c21a32831281bb3a136fb7eb0a2e8b2f7dda610913be3449f2bb643c3`
  - `candidates/A.md` `15b36d61…`, `B.md` `00961b3c…` (same bytes as `description.md`), `C.md` `832a4bd1…`
  - `candidates/A-18line.md` `36881cc8…`, `B-18line.md` `b0dd15dd…`, `C-18line.md` `8864e29c…`
- Process discipline: one gate at a time; observed wall times 2.65 s (single census run with rule eval) and
  8.43 s (seven census runs); nothing approached the 120 s contention cap.
- Quotes above are sed output of the named lines, each ≤25 words; the corpus quote spans lines 68-69 and
  119-120 (the line break is part of the source, not dropped), the addendum quote spans 39-40. No
  `byte-exact` claim is made for the folded descriptions: they are my text, and their equality to the
  deliverables is by sha256, not by quote.
