# F04CheckviewEntry — round 77 w2 — entry provenance and clip/first-sentence values

Date: 2026-10-27. Lane tip examined: `6523aced1ee0ebe07dca996213bdc645a6acbd1e` (r77 freeze; `master`, clean).
Base: `2f675548eaad2a037a899d39247c1fd7a88aaf48`. Seat scope: falsify entry provenance (conjunct (f)) and the
clip / first-sentence audit values (conjunct (d)) for the C1 entry, plus the quote/citation provenance the
entry claims for itself. No subagents, no background jobs, no pacman, no lane/git/jj writes, no tool installs
(used system `python3`, `git`, and the already-present system PyYAML 3.14 site-package; nothing installed).

## 1. BLOCKER — the claim data is not committed at the examined tip

`git ls-tree --name-only HEAD corpus/knowledge/` lists no `description-craft-round76.md`; `git log --oneline -3`
shows the only r77 commit is the freeze (`6523ace round-77: freeze plan, base receipts`). No branch or ref
carries the entry either (`git branch -a --contains 12ae9c3` empty; the only extra commits, `12ae9c3`/`522103b`/`7fe585d`/`f2f3a86`,
are unreachable jj-side duplicates of the freeze patch — `git show 12ae9c3 --stat` = the same 5 freeze files,
130 insertions; `git diff 6523ace 12ae9c3 --stat` = exactly those 5 files, 72 deletions — no hidden data).

Re-run of both frozen counters at the tip (scratch clone `git clone --shared`, user configured before any
scratch state; `git rev-parse --show-toplevel` = the clone; counters byte-checked in the clone first — both
sha256 equal the plan pins `cf3c45d9…b9e` / `989203c4…a63`):

- `python3 -B verifiers/check_desc_craft.py --repo $S/clone --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e`
  → six `fail` lines, final line `description craft backed 0 of 6`, captured `exit=1`.
- `python3 -B verifiers/check_r75_routed_repairs.py --repo $S/clone --rev 6523aced…`
  → `R1–R4: open`, final line `r75 routed repairs closed 0 of 4`, captured `exit=1`.

Wave-1's green receipt `receipts/E06EntryVerify.c1-tip-6of6.txt` names `measured-rev: d97d5bd61c092a44141fb2491e3a504c1babbb19`,
a scratch commit that exists nowhere in lane history. So the w1 green is a scratch-clone result, not a landed
one. **No claim may be reported verified against the lane until the L1 lands the data and a counter receipt at
that landed rev exists.**

## 2. Landed provenance that IS at the tip — verified, no defect

- Counter bytes at HEAD and in the clone both hash to the two plan pins (commands above; `sha256sum`).
- `python3 -B verifiers/check_desc_craft.py --self-test` → `self-test: 0 failure(s) over 53 assertions`, `exit=0`
  (matches the plan's pinned self-test shape).
- Base receipts `receipts/c1-base-2f675548….txt` / `c2-base-2f675548….txt` match the plan's claimed text
  (`0 of 6` / `0 of 4`, exit 1, counter sha256 lines present).
- Snapshot chain: `sha256sum` of the three snapshot files equals `MANIFEST.sha256` lines and `fetch-record.json`
  (HTTP 200, `fetched_at 2026-10-27T16:57:56Z`, 13,403 bytes for optimizing-descriptions); the
  optimizing-descriptions digest is `7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837`, matching
  the plan's pinned `7cc54fbb…bd837` and the counter's own table. Snapshot is 196 lines / 13,403 bytes; first
  heading at line 5 (`# Optimizing skill descriptions`).

## 3. Clip / first-sentence values (conjunct (d) core)

Convention check against the frozen counter's code (`render_description`, `description_measures`): clip = folded
render with the terminal newline kept (default chomping appends `\n`); stripped = `len(value.strip())`; first
sentence = `value.find(". ") + 1` (period included). This is exactly plans/round-76-addendum-1 (clip-preserving)
and addendum-4 (first `. `, period included). Independent recompute with real PyYAML over the committed bytes
(`yaml.safe_load` of the frontmatter document, opening `---` dropped, closing kept):

- freeze tip `6523ace` and r77 base `2f675548` both: **clip 1022 / stripped 1021 / first 151** — identical to the
  counter's `description_measures` on the same bytes, and to the draft entry's audit table (1022, with the
  stripped variant 1021 named in the how-cell; 151). My first PyYAML probe printed 1021 only because my harness
  fed YAML without the closing document terminator — rerun with the terminator, real YAML clip chomping keeps the
  newline: 1022. No off-by-one survives.
- The entry's Limits claim "`check_sibling_census.py` `description_of` … returns 1021 for these bytes" verified:
  `len(check_sibling_census.description_of(SKILL.md @ 6523ace))` = 1021.
- The entry's supporting audit-table claims all recomputed true: sentence 7 is 87 characters
  (`Note: shokunin files sit outside … never reads this text.`); the description holds 7 sentences (6 `. `
  boundaries + terminal period); 8 quoted trigger phrases, inner lengths summing to 108; 5 of the 8 contain
  `skill` case-insensitively, 1 more names the field (`frontmatter description`), and only `trigger words` and
  `prompt craft` name neither; `git diff --stat 2f675548 6523ace -- SKILL.md` prints nothing (identical bytes),
  so both revisions measure the same.
- Data-side mutation (gate bites on my two numbers): editing only the value cell 1022→1021 makes conjunct (d)
  FAIL (`rendered description length [1021] does not equal the recomputed clip render 1022`); 151→150 FAILS
  (`first-sentence length [150] does not equal the recomputed 151`). The as-is draft passes.

## 4. Draft-entry provenance and quote falsification (E06EntryVerify.description-craft-round76.md)

Conjunct (f): the draft opens `source: S213 — Agent Skills — Optimizing skill descriptions — https://agentskills.io/skill-creation/optimizing-descriptions.md …`,
then `verified-at: 2026-10-27`, `recheck: 90d — …` (names the lane root, a runnable nine-token loop, rev
`6523aced`, date). Counter's `entry_head` parses all three; S213 + exact URL present. PASS.

Conjunct (b), simulated with the counter's own `Snapshots`/`quote_spans` rules against the committed snapshots:
**11 counted quotes** (floor 4), each ≤25 words, each verbatim inside ONE physical line, all after the first
heading, all page-unique (0 occurrences in evaluating-skills / best-practices), each with its cited line. Cited
line numbers checked against the bytes: head quote 20 words at `:9` ✓; table quotes at `:25`, `:26`, `:27`, `:27`,
`:28` ✓; caveat 17 words at `:19` ✓; ceiling quote at `:28` ✓; `§ Writing effective descriptions` = `:21`–`:28`
(heading at `:21`) ✓. My per-quote table matches seat E06's committed `quotes-verified.txt` row-for-row
(including "counted quotes: 11"). Independent confirmations of the ground line: `git grep -il -F` at `6523ace`
for the five rule phrasings → exit 1, zero files each; SOURCES row S213's anchor is the "Running multiple times"
subsection and its `used-by` is only `skill-eval-artefacts-round70.md` (so "no entry carried the writing
principles" holds); the quoted `frontmatter-trigger-surface.md:153`–`:154` sentence joins across exactly those two
lines; all four `Related` files exist. The lesson draft `SC01Lesson76.round-76.md` `## Gate` carries URL, access
date 2026-10-27 (matches the fetch record), the digest, and a 10-word located quote — conjunct (a)'s
lesson-record arm is satisfiable as drafted.

## 5. DEFECT found — E06 draft, "Two further sentences" paragraph (line 28)

> "the trigger-burden sentence at `:17` and the page's own caveat at `:19` … appear in § Limits"

False on either reading. Snapshot `:17` is "This means the description carries the entire burden of triggering.
If the description doesn't convey when the skill is useful, the agent won't know to reach for it." — neither of
its sentences appears anywhere in the draft (0 hits for "entire burden" / "won't know to reach"), and § Limits
quotes only the `:19` caveat. The trigger-burden sentence the draft actually quotes is the `:9` under/over
sentence, per its own head. So either the `:17` citation points at the wrong line for a quoted sentence, or it
cites a sentence that is claimed "quoted" but is not. Minimal repair (pick one): (i) rewrite to name the `:19`
caveat as the only further sentence quoted in § Limits and drop the `:17` clause; or (ii) actually quote the
`:17` sentence beside its citation. Harm to other axes: none — conjunct (b) already counts 11 quotes without it,
(d)/(f) are untouched, freshness/consistency unaffected; repair (ii) would add a 12th counted quote (still
harmless). This is exactly the quote/citation-mismatch family the r76 closure chased; fix before landing.

## 6. Other observations (not defects)

- Three candidate entries exist (E06 draft, X01Simplifier.entry.md, r76 build/entry-draft.md); all three pass
  (b)/(d)/(f) with identical audit numbers (1022/151) — no calibration divergence. The L1 must land exactly one
  at `corpus/knowledge/description-craft-round76.md`; X01/r76-draft quote the description's sentence 1 with
  backticked `SKILL.md` (cosmetic; the span then reads 19 words instead of 24, still under the 25 cap).
- The C1 predicate reads SKILL.md at `--rev`; the planned § Body craft row is body text, so the 1022/151 values
  survive landing only while the description block stays untouched — headroom to the 1,024 ceiling is 2
  characters (clip convention); any description edit breaks both the ceiling and conjunct (d).
- Diagnostics note: no `lsp` device is mounted in this session, so caller/definition checks were done by reading
  and executing the counter's own code paths (stronger than text grep); grep was used only as the literal
  fallback where noted.

## 7. Residual risk and gaps

- I did not re-fetch S213 live; freshness of the page rests on S01Reopen1/S02Reopen2's same-day re-opens
  (digest-agreeing per the lesson draft) and is F03CheckopenS213's seat scope.
- Conjuncts (c)/(e) and the C2 repairs have nothing landed to check; E07/E05 drafts were not falsified here
  (other seats' items).
- The w1 green receipts (c1-tip-6of6) were produced at scratch rev `d97d5bd…`; the L1 must re-issue them at the
  landed tip after integration, or the SCORECARD row would cite an unverifiable revision.

VERDICT: Landed tip is data-free — C1/C2 re-run red at 6523ace (0 of 6 / 0 of 4, exit 1 each); the draft entry's provenance, quotes, and 1022/1021/151 clip/first-sentence values all verify against committed bytes and real PyYAML, with one prose-citation defect (the `:17` "quoted in § Limits" claim) to repair before landing.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w2/F04CheckviewEntry.md
