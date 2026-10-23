Result: DONE — The frozen C2 readings are narrower lexical/structural proxies for several box clauses, and passing their generated cases does not establish full box execution; C2 remains withdrawn.

# Scope and evidence

Seat: KotobaR56.C2RedesignReading. Target axis: operability; associated risks: coverage, consistency and calibration. This is redesign input for a later round, not a claim verdict, admission, implementation or measurement of round-56 content.

Reviewed revision: `e02f5f5d2f37427e8a77b1c3efb45f84b78c67c8`. References below are repo-relative. The C2 withdrawal is `plans/round-56.md:113-123`; neither its counter nor its dispositions should change this round.

Read-only commands run from the lane, all exit 0:

```text
timeout 10s git --no-optional-locks show e02f5f5d2f37427e8a77b1c3efb45f84b78c67c8:verifiers/check_agentdef_boxes.py
  Output: frozen source, including operational readings at lines 68-130.
timeout 10s git --no-optional-locks show e02f5f5d2f37427e8a77b1c3efb45f84b78c67c8:SKILL.md
  Output: box texts at lines 316-344.
timeout 10s git --no-optional-locks show e02f5f5d2f37427e8a77b1c3efb45f84b78c67c8:verifiers/check_agentdef_boxes.py | timeout 5s sha256sum
  Output: 8aeb9bcf611decdba9e1027c435c3f268e5c51112706f43d76f284ae05aeb8fe  -
timeout 5s date -u
  Output: Fri 23 Oct 2026 02:46:59 AM UTC
```

The hash matches the counter hash recorded in `controls/CtlC2Heuristics.txt:465` (paths under `.ufo/waves/round-56/`). I opened the existing receipt; I did not rerun it. New witness outcomes below are explicitly **[INFERENCE: static derivation, not executed]**. No fresh runtime claim or source-fetch claim is made.

# Strongest existing local falsifier

**Yes: an instrument meeting the counter can still miss defects explicitly named by the boxes.** This is already witnessed, not merely hypothetical. Existing receipt `.ufo/waves/round-56/controls/CtlC2Heuristics.txt:462-524` records sandbox revision `40c2b5eb530fac42f26abc7d391651ef9caf92bd`, the matching counter hash, and `agent-definition boxes executed and discriminating 5 of 9`, exit 0, for each recorded sample. The same receipt then records:

| Box | Direct input defect | Recorded result | Receipt lines |
|---|---|---|---|
| .01 | `alpha.md` declares `beta`; `beta.md` declares `alpha` | PASS, exit 0 | 529-555 |
| .02 | Enrolled `alpha` lists `beta`; existing `gamma` is neither enrolled nor reachable | PASS, exit 0 | 591-622 |
| .05 | Frontmatter contains `updated: November 1` | PASS, exit 0 | 672-691 |
| .06 | Body says `Once only, sweep the queue.` | PASS, exit 0 | 693-711 |

These contradict both the box texts and the frozen operational readings. They establish a **generated-case coverage defect** independently of the additional **reading-versus-box gaps** below. Do not confuse those two defects: implementing the docstring exactly would fix neither the docstring's omissions nor its semantic over-flags.

# Comparing the five readings with their boxes

## agentdef.01 — the missing-name clause becomes conditional

Box: `SKILL.md:316-317`. Rule: `verifiers/check_agentdef_boxes.py:68-77`.

The box calls absence a latent defect and says it is “still a defect when every sibling declares it.” The counter instead makes a nonempty, otherwise-declaring sibling set a **necessary** condition for treating absence as defective. “Still” is not “only if”; the nonempty requirement is also added by the counter.

The frozen generator itself supplies the first falsifier: `:453-461` requires PASS when neither of two files declares `name:`, but FAIL after one missing declaration is supplied. Thus adding the second missing declaration can make a defective roster appear repaired. A singleton without `name:` also passes the declared rule. Multiple unnamed files among named files evade its latent clause for the same reason.

**[INFERENCE: box interpretation]** This is narrower than the box's ordinary reading of latent absence. If the intended box actually means only inconsistent omission, that must be settled explicitly before a later freeze, not inferred from the counter as a second authority. The direct swapped-name witness above needs no such interpretation: the current generator also fails to establish each file's own stem/name binding.

## agentdef.02 — sound graph definition, insufficient exercise of it

Box: `SKILL.md:318-320`; introductory artifacts: `:310-312`. Rule: counter `:79-91`.

The least-fixed-point rule faithfully captures enrollment or enrollment-rooted transitive roster reachability. I found no necessary narrower/wider semantic reading within that abstract graph model. An unenrolled parent's roster does not create a root; this is correctly stated and tested at `:508-521`.

However, the generated graphs at `:480-544` exercise direct enrollment and one-hop parent/child links only. They do not establish arbitrary-depth traversal, rooted/unrooted cycles, or detection of an orphan alongside an unrelated reachable roster. The recorded `gamma` witness demonstrates the last omission.

The common-file contract also promises comma-separated inline `subagents` lists (`:63-65`), but the generators use block sequences. The reference fixture wraps a scalar roster in a one-element list without splitting it (`:1147-1153`). **[INFERENCE: static derivation]** A reachable parent with `subagents: beta, gamma` can therefore lose both child edges in that fixture while all generated cases remain satisfiable. This is a contract/fixture coverage defect, not evidence that the box requires only one-hop reachability.

Choosing declared `name:` before the stem is a stated identity assumption (`:82-83`), not a proof of harness resolution or valid, unique enrollment. Schema/key validity belongs to .04 (`SKILL.md:325-331`); do not silently credit .02 with it.

## agentdef.05 — date recognition omits live operational state

Box: `SKILL.md:332-336`. Rule: counter `:93-105`.

The box explicitly includes **live seat assignments** and says frontmatter holds stable policy. The rule recognizes particular date/round forms, not live state. **[INFERENCE: static derivation]** A quoted description saying `Current review seat is Finch; route all reviews to Finch until reassigned.` passes the rule despite being precisely a live assignment. Relative expiry such as `until tomorrow`, a numeric slash-form date, and other unlisted date/round spellings can also pass.

The rule is simultaneously wider in another direction: it rejects *any* recognized date token without asking whether it is operational state. **[INFERENCE: semantic counterexample, not executed]** The stable policy `Require report dates to match ISO format, for example 2000-01-01.` is rejected solely because its timeless format example contains a date. Calling that a dated operational assignment changes the box's meaning.

Reading coverage is itself broader than fixture coverage: `:547-613` generates ISO dates/timestamps and `PROPOSE round`, but not month-name dates or numeric round-index variants. The observed month-date miss above is therefore not cured merely by quoting the fuller docstring.

Ignoring the body in .05 is **not by itself a defect**: the box routes dated body anecdotes to .06. The missing handoff is described next.

## agentdef.06 — a finite vocabulary is not persistent identity

Box: `SKILL.md:337-339`, with the dated-body handoff at `:335-336`. Rule: counter `:107-115`.

The box excludes per-task job text and instructions that stale between delegations. The reading substitutes a finite vocabulary. **[INFERENCE: static derivation]** Both of these body instructions pass its stated tests:

- `Repair ticket KOT-123 and return its patch before the next handover.`
- `Use Finch as the review seat until 2025-01-01.`

The first is a particular job without the marker phrases. The second is an expired operational assignment with no recognized current-task, numeric-round or one-shot marker. .05 ignores its body, and .06 does not inspect dates or expiry, so the stated cross-box staleness handoff has no detector. The .05 generator even puts a dated historical anecdote in a mandatory-PASS .05 case (`:555,590-600`); there is no paired .06 staleness case.

Conversely, **[INFERENCE: semantic counterexample]** the durable constraint `Reject one-shot assignments from persistent agent definitions.` is flagged merely for mentioning the prohibited class. The reading does not distinguish a transient instruction from a rule prohibiting or quoting one.

The generated .06 failures (`:616-673`) use only current-task, numeric-round and `one-shot` forms. They do not establish the other listed one-shot forms; the existing `Once only` witness demonstrates this gap. There is also a small internal authority mismatch: the reference fixture shares .05's `ROUND_RE`, including `PROPOSE round` (`:1047,1188`), although .06's reading lists numeric round indices only. Its regex permits at most one separator before the digits, so the promised `round #12` spelling is not recognized by that fixture **[INFERENCE: static derivation; not run]**. Neither boundary is exercised by its .06 generator.

## agentdef.07 — paragraphs and headings cover only some blocks

Box: `SKILL.md:340-344`. Rule: counter `:117-130`; reference section analysis: `:1195-1249`.

The box says the same paragraph must not appear twice and explicitly names repeated line runs and same-name conflicting blocks. The reading adds a 40-character minimum, requires an entire normalized paragraph to repeat, and recognizes names only as Markdown ATX heading titles.

**[INFERENCE: static derivation]** Each following body can evade that model while retaining a named box defect:

1. Two blank-separated copies of `Preserve source attribution.`: a substantive duplicated paragraph, but below the threshold. The generator's hard negative (`:714-722`) protects the trivial `- yes` example; it does not justify treating every substantive short paragraph as harmless.
2. A repeated multi-line instruction run embedded in otherwise different paragraphs: the whole paragraphs differ, so the repeated-run defect is not detected. For example, different opening/closing sentences can surround the same `Preserve evidence.` / `Record every decision.` run.
3. Two plain-label blocks with differing payloads, rather than heading titles:

```text
DESPAWN:
- Preserve the completed report after the worker exits.

DESPAWN:
- Delete the completed report after the worker exits.
```

Those paragraphs differ and no heading is recognized. The conflict is the template's shared name, not paragraph equality.

4. The reference analyzer also closes a section at **every** heading, losing parent/child block structure. This body has two conflicting DESPAWN parent blocks, but both parent contents are recorded as empty; child names and paragraphs are distinct:

```text
## DESPAWN
### Keep
Retain the completed report.

## DESPAWN
### Purge
Erase the completed report.
```

The generated same-name case (`:696-712`) has flat headings with direct content, so it cannot expose this. Conversely, the analyzer treats the same title in separate ancestor scopes as one global name. Whether that is a conflict must be specified before a later claim; the current data does not establish a safe scoped-name policy.

# Copy-ready “what it does not measure” statements

These statements describe limitations, not permissions to label complete boxes executed. They can be selected verbatim for a later claim's limits line; removing a limit requires evidence that the later instrument covers it.

1. **Aggregate:** “Passing N>=3 establishes success on at least three generated box case sets, not all five generated readings, all nine boxes, or the live agent roster; .03, .04, .08 and .09 have no generators.”
2. **.01 latent absence:** “Missing `name:` is tested as defective only with a nonempty sibling set whose other files all declare names; singleton, all-unnamed and multiple-unnamed rosters are not treated as latent missing-name defects.”
3. **.01 identity coverage:** “The cases do not establish each declaration's binding to its own file stem when declared names are permuted across files.”
4. **.02 reachability coverage:** “The cases do not establish arbitrary-depth or cyclic roster reachability, inline comma-separated rosters, or orphan detection alongside an unrelated reachable roster; they do not verify live harness enrollment or identity resolution.”
5. **.05 transient state:** “The lexical frontmatter reading does not detect live seat assignments, relative expiry or unlisted date/round spellings unless they also contain a recognized date/round token.”
6. **.05 meaning:** “Date-token rejection does not distinguish dated operational state from a timeless policy example or other non-operational use of the same token.”
7. **.05 reading coverage:** “Generated cases do not establish the promised month-name-date and numeric-round forms, nor detection independently of frontmatter key ordering or defect position.”
8. **.06 transient meaning:** “The body reading does not establish persistent identity or detect per-task assignments, expiry and stale dated anecdotes outside its listed phrase/round patterns.”
9. **.06 context:** “Phrase matching does not distinguish issuing a transient instruction from quoting or prohibiting that instruction, and the cases do not establish every listed one-shot or round spelling.”
10. **.07 short duplication:** “The duplicate-paragraph test excludes normalized paragraphs shorter than 40 characters, including substantive short paragraphs.”
11. **.07 repeated runs:** “The paragraph test does not detect repeated instruction runs embedded inside otherwise different paragraphs.”
12. **.07 named blocks:** “The heading-based conflict test does not cover non-ATX named blocks, and its flat reference section model does not establish conflicts whose differing content lies in nested subsections or distinguish globally repeated titles from scoped block identities.”
13. **Input scope:** “The generated simple-frontmatter Markdown files and JSON enrollment maps do not establish support for all target-harness file/schema/roster encodings or actual loading and delegation.”

# Impact and smallest safe correction

- **Operability:** a successful generated-case result can leave explicitly named defects undetected. Merely executing the instrument is not executing each full box.
- **Coverage:** finite vocabulary, paragraph/heading boundaries and graph fixtures omit defect classes; adding random stems does not expand those semantic relations.
- **Consistency:** box prose, operational docstring, generated expectations and reference fixture are separate authorities unless their differences are made explicit. .01's conditional absence and .02's inline roster promise are concrete examples.
- **Calibration:** N=5 would be saturation of these case families, not saturation of agent-definition fidelity. No axis score or canonical verdict is assigned here.

**Smallest safe action now:** keep C2 withdrawn, retain frozen counter/box/map bytes, and use the exact limits above only as redesign notes. No delegate or disposition patch is supplied.

**For a later freeze:** either claim bounded lexical/graph subchecks explicitly, leaving the omitted box clauses under reviewer judgment, or resolve the semantic boundaries and add independent red/green cases before claiming the full boxes. The minimal relevant boundaries are missing-name policy; orphan-plus-unrelated-roster and deeper/inline traversal; date-less live seats versus stable date examples; unmarked/dated one-off jobs versus durable prohibitions; and short, embedded, non-heading and nested conflicting blocks. Existing pre-freeze shortcut receipts remain necessary controls, not evidence that these semantic clauses are covered.

The missing cases and parser/section boundaries are fixable measurement defects. Replacing them with blanket bans on dates, trigger words or repeated heading titles would exchange missed defects for false reds on stable policy: that is a trade, not a safe correction or a basis for silently crediting operability. Q23 requires run counterexamples in both directions before calling the later approximation stricter/looser; Q26/Q31 prohibit describing checks it does not run; Q28 bars revising the frozen judgment after data (`corpus/QUALITY.md:34,37,39,42`). This seat offers no admission judgment.

# Hygiene

Only this report was written in the lane. No lane code, map disposition, counter, box text, jj state or Git index was changed. No sandbox, commit, test, probe, counter execution, source fetch, model call, other runtime, tool installation or background process was started. Static witnesses remain unexecuted; the only runtime findings cited above belong to the explicitly identified existing control receipt. A reader-output inconsistency was reported through `xd://report_issue`; it did not affect the source-line evidence used here.
