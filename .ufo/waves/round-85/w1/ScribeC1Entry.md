# ScribeC1Entry — round 85, wave 1 (C1's sourced knowledge entry)

Seat: `ScribeC1Entry`. Round 85 attempt 1, lane kotoba, host linux, date 2026-11-04.
**One file written, one lane file, nothing else.** No git write, no sibling-lane write, no
write to `shokuknow`, no write to the fleet root.

## 1. Behavior

Wrote `corpus/knowledge/description-trigger-discipline-round85.md` — the C1 sourced entry
(R8 `sourced_entry`). It is a **documentary note**: it states what S213's page says about
description authoring and trigger-eval design, and what the lane's own committed
description does and does not yet do. It claims no production change and no observed
trigger behaviour.

Structure, per the seat item: title, `source:` naming S213 with the URL and the fetch
provenance, `verified-at: 2026-11-04`, a `recheck:` value, a `ground:` line, five findings
sections, a `Limits` section, and the closing counter pointer.

## 2. Gates this seat ran (and what they read)

| check | command | observed |
|---|---|---|
| R8 structural (frozen counter's own `rule_r8`) | `python3 -B` load of `.ufo/waves/round-85/frozen/check_description_render.py`, `rule_r8(kb)` | `R8: ok \| source S213, verified-at 2026-11-04, recheck present, 15 quote(s) in range` |
| every S213 page quote located verbatim | per-quote substring search against `.ufo/waves/round-76/snapshots/optimizing-descriptions.md` | 13 quoted spans in the 3–25-word range, all `OK` at their cited page line (9, 15, 17, 19, 25 ×2, 26, 27, 28, 41, 52, 56, 60) |
| page digest still current (the `recheck:` command itself) | `curl -sL https://agentskills.io/skill-creation/optimizing-descriptions.md \| sha256sum` | `7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837` — matches the pinned digest, 13 403 B, HTTP 200 |
| base description, measured with the lane's own helper | `verifiers/check_sibling_census.py`'s `description_of()` on `SKILL.md` | parsed length **1021**, first sentence **150** (151 incl. the period); `Triggers:` at offset 152, `Anti-triggers:` at 302, `Sibling boundary:` at 456; first 99 chars carry the domain words but not the trigger surface |
| sibling guard on the base | `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md --province PROVINCE.md --skill SKILL.md` | exit 0, `skill description names 10 of 10 non-none lanes`, `skill description length 1021 of 1024` |
| sibling guard on the candidate | same, `--skill .ufo/waves/round-85/frozen/fixtures/candidate-SKILL.md` | exit 0, `skill description names 10 of 10 non-none lanes`, `skill description length 876 of 1024` |
| candidate payload | plan block vs `w1/ExecC1Eval/candidate-description.txt` vs the frozen fixture's parsed description | all three byte-equal at **876** characters; first sentence **64**; **10** clauses (6 of them sibling-ownership clauses) |
| eval-set shapes (both artifacts) | row counts / indirect-positive count / shared-token check | ExecC1Eval TSV: pos 9, neg 9, indirect 5, 0 negatives without a shared ≥4-char word; the counter's own committed fixture: pos 9, neg 10, indirect 8, 0 without — both inside the frozen 8–10 band |
| entry cross-references | existence check on all 10 cited paths | all `OK` |

Receipt: `.ufo/waves/round-85/w1/ScribeC1Entry/receipt.txt` (byte counts, sha256 of the
entry, per-quote locations, all measurements above).

## 3. Touched surfaces

- `corpus/knowledge/description-trigger-discipline-round85.md` — **new**, this seat's only
  production file (11594 B, sha256 `d9041c6b6c70c2b006177c674c4c791809fb756bdd6b38ba6bc08865eb6df345`).
- `.ufo/waves/round-85/w1/ScribeC1Entry/receipt.txt` — **new**, this seat's own wave dir.
- `.ufo/waves/round-85/w1/ScribeC1Entry.md` — **new**, this seat's report.
- Scratch `/fast/scratch/hyaku/kotoba-r85/ScribeC1Entry/` — removed before yield.
- Read-only: `plans/round-85.md`, `.ufo/waves/round-85/claims.json`,
  `.ufo/waves/round-85/w1/ScoutSource/{fetch-record.txt,source-packet.md}`,
  `.ufo/waves/round-85/w1/ReviewerC1.md`, `.ufo/waves/round-85/frozen/QUARANTINE.txt`,
  `.ufo/waves/round-85/w1/ExecC1Eval/*`, `.ufo/waves/round-73/w1/{ConnScopeSiblings,ReviewerPackage}.md`,
  `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md`, `corpus/lessons/round-74.md`,
  `corpus/SOURCES.md`, `corpus/README.md`, `SKILL.md`, `verifiers/check_sibling_census.py`,
  and (read-only, per the bounds) the staged package under `/home/vgpnk/Projects/shokuknow/merge/kotoba/`.

## 4. Out of scope — deliberately not done

- **No `corpus/README.md` coverage-map row.** `corpus/README.md` is ScribeSources' file
  (file ownership in the seat item); the coverage row for the new entry belongs to that
  seat. Checked here for information only: no `knowledge/` glob row exists, so the new
  file needs its own row before `verify_corpus_integrity.py`'s `corpus.index.unindexed`
  gate is satisfied — it reads `git ls-files corpus/`, so an untracked file is not yet
  counted either way.
- **No `corpus/SOURCES.md` edit.** S213's row exists and its `used-by` cell is
  ScribeSources' to update; this seat cites S213 without minting a row.
- **No edit to `SKILL.md`.** The production description is unchanged at 1021 characters.
  The 876-character candidate was never applied and this seat does not claim it was.
- **No edit to the counter.** `verifiers/check_description_render.py` was quarantined by
  the L1 at `47085c8` and its bytes now live under `.ufo/waves/round-85/frozen/`; C1 is
  killed, and the entry says so.
- **No lesson, no `LOG.md`, no `SCORECARD.md`.** Owned by ScribeLesson and the L1.

## 5. Findings

1. **The page's own model is two-sided and single-field.** Under-specification misses,
   over-broadness over-fires, and both are repaired in the description because the agent
   sees only `name` and `description` at startup. Every rule the page gives (imperative
   framing, user-intent-not-mechanics, pushy context listing including cases that never
   name the domain, the 1 024-character ceiling) targets that one field.
2. **The eval design is where the negatives belong.** The page puts near-miss negatives
   in the labelled set (≈20 rows, 8–10 each way), values indirect positives over obvious
   ones, and states the caveat that bounds any such measurement: an agent may handle a
   task alone and never consult a skill, so a trigger miss has two causes and an eval set
   that does not separate them measures neither.
3. **The lane's committed description violates the rule the page states.** 1 021 of 1 024
   characters; first sentence 150, past omp's offset-99 listing cut; `Triggers:` at
   offset 152, `Anti-triggers:` at 302, sibling clauses from 456 — all of it invisible to
   a cut listing, while the description sits three characters under a ceiling it does not
   need. It has no `Use this skill when` string, which is the page's first authoring rule.
4. **The candidate measures well and is not applied.** 876 characters, 64-character first
   sentence, 10 clauses, 10 of 10 non-none lanes named by the round-74 sibling guard
   (exit 0). The eval set is 9+9 with 5 indirect positives and every negative sharing a
   ≥4-character word with the description.
5. **The three-way negative-condition tension is three things, and only one of them is
   S213's.** Stated as separate positions with their own locators: negative *scope* in the
   description (TRAE's position — the lane's round-73 wave record, not a lane `source:`
   row; `grep -c "ide_best-practice-for-how-to-write-a-good-skill" corpus/SOURCES.md` → 0),
   the *eval set* as the test (the specification's own position, carried by S213), and a
   negative *directive* in the body (Chiba Prefecture — quoted by the round-73 review and
   recorded there as **unsourced**; `grep -c "pref.chiba" corpus/SOURCES.md` → 0). They are
   not averaged. The lane's reading: keep an `Anti-triggers:` scope clause in the
   description, put near-miss negatives in the eval set.
6. **Two corrections to the brief's own premises, recorded rather than smoothed over.**
   (a) The seat item located TRAE's negative scope at
   `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md`; that file carries TRAE's
   frontmatter keys and body shape (描述 / 使用场景 / 指令 / 示例) but **no** negative-boundary
   wording — the wording is in the round-73 wave record `ConnScopeSiblings.md:119`. The
   entry says so and cites the actual location. (b) The item's "R6 requires a 9+9 eval
   set" is narrower than the frozen rule: the counter's band is 8–10 per label
   (`EVAL_ROWS_MIN = 8`, `EVAL_ROWS_MAX = 10`), and the counter's own committed fixture is
   9+10 with 8 indirect positives. The entry states the band and reports both artifacts'
   actual shapes rather than the 9+9 of the wave artifact alone.

## 6. Risks

- **The entry is untracked.** `git ls-files corpus/` does not yet list it, so no corpus
  gate sees it yet, and `corpus/README.md` has no row for it (ScribeSources' file). If the
  L1 commits it without a coverage-map row, `verify_corpus_integrity.py`'s
  `corpus.index.unindexed` check will go red on the next commit.
- **The counter is quarantined, so the entry cannot be scored by a live gate.** R8 was
  exercised against the frozen instrument's own `rule_r8()` function and reads green, but
  that instrument was killed for reasons the entry itself records (R6 accepts duplicate
  positives and incidental-token negatives; R1 accepts abbreviation terminators; R5
  executes revision-selected Python). No after-value is claimed, so nothing depends on it.
- **Section 4's two non-S213 legs are lane wave records, not held sources.** If a later
  round reads them as page claims of S213, that is a misreading of this entry's own
  explicit labelling. The Chiba quotation is itself flagged unsourced by the round-73
  review; it is quoted here as that review's quotation, with the review's pointer.
- **The `recheck:` line carries a 90-day cadence on a live page.** If the page moves, the
  digest check fails and the entry needs a re-open, not a silent snapshot swap; the
  command was run today and reproduces the pinned digest.
- **No tooling was installed or upgraded** under the operator directive (curl, coreutils
  and the lane's own Python were sufficient), so there is no install to record.

## 7. L1 integration — what changed in the entry after this seat's write

After this seat's write and on the L1's instruction to stop production edits, the L1
replaced the entry's § 4 and parts of § 3 and § 5 with its own text. The entry's final
bytes are **8 682 B, sha256 `48c8869698a85988a420234f01c68b799f545fed9a3388f4dd66fb99a27f4ad8`**
(against this seat's 11 594 B / `d9041c6b…`). This seat's receipt was regenerated against
those final bytes and every measurement below was re-verified on them; the measurements
are unchanged by the rewrite.

What the L1 changed, and why it is right:

1. **§ 4 no longer claims S213 puts negatives only in the eval set.** My § 4 said "The
   page puts the negative cases in the **eval set**, not in the description … That is one
   position and it is the only one this page carries." That was an overreach, and the
   page refutes it at line 156: "If should-not-trigger queries are false-triggering, the
   description may be too broad. Add specificity about what the skill does *not* do, or
   clarify the boundary between this skill and adjacent capabilities." The L1's § 4 states
   the opposite and correct thing — S213 does not prohibit negative scope wording — and
   keeps this lane's `Anti-triggers:` clause without attributing a positive-only rule to
   S213. **Note for the record:** the packet does not carry line 156 as a located quote,
   so the L1's wording is a paraphrase with a locator, not a quoted sentence.
2. **The TRAE/Chiba comparison is now refused rather than asserted.** The L1's § 4
   refuses the staged package's comparison (its cited page identities were not re-opened
   for this entry) and states a flip: open the original sources in a later round, locate
   the relevant text, and evaluate each claim separately. This supersedes my § 4, which
   named both positions as lane wave records — a defensible reading, but one that put
   two unheld pages inside a sourced entry, which the refusal avoids.
3. **The trigger-miss claim is now labelled as the lane's inference.** My § 3 concluded
   from page line 19 that "an eval set that does not separate the two measures neither."
   The L1 renders the same point as "**Lane inference:** a trigger miss alone cannot
   identify a wording defect; the task's need for specialist knowledge also matters." —
   the page states the caveat, not the inference, and the packet refuses the inference
   as a page claim (its verdict row 11).
4. **The renderer cut is now qualified.** My § 5 said the first sentence "runs past omp's
   offset-99 listing cut (`SKILL.md:30`)". The L1's § 5 says the trigger-bearing clauses
   "lie beyond the cache-miss renderer's 99-UTF-16-unit prefix for long descriptions; the
   renderer may shorten that prefix further at a sentence or word boundary. A cached
   one-liner bypasses that branch", pointing at `.ufo/waves/round-85/w1/RevengerRender/probe.md`,
   and infers no universal live-listing ceiling. That matches the round-85 renderer
   finding recorded at `SKILL.md:30` (`k=100`, `slice(0,k-1)`, UTF-16 units, not bytes) and
   the round-7 note that the loss figures describe the cache-miss path only.

Final state of the entry as integrated (all re-verified on the final bytes): `source:`
names S213, `verified-at: 2026-11-04` and a `recheck:` value are present, 13 quoted
spans of which **12 are S213 page quotes, each located verbatim at its cited page line**
(9, 15, 17, 19, 25, 26, 27, 28, 41, 52, 56, 60) and all 3–25 words; the thirteenth is
the sibling guard's own output line. The frozen counter's `rule_r8()` reads
`R8: ok | source S213, verified-at 2026-11-04, recheck present, 13 quote(s) in range`.
