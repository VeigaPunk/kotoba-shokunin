# RevFabrication — round 67 wave 1

## Scope and method

Reviewed the staged entry and exactly the three provenance-header rows requested:

- entry: `/home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/instruction-authority-ladder.md`
- rows: S123, S124 and S129 in `/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md:7,8,13`.

The entry also makes an inline fourth citation, S125, at lines 22–24. I opened that source only to audit this sentence; I did not audit all of row S125. The three requested sources were re-opened on 2026-10-24. I also read the original round-1 fetch ledger and cached bytes from 2026-10-23, so the findings do not depend solely on today's live rendering.

Verdicts below mean:

- **SUPPORTED**: the cited anchor explicitly supports the statement, with its stated scope.
- **PARTIAL**: part is supported, but the sentence as written is broader, narrower, or missing a material condition; it is therefore **not supported as written**.
- **NOT SUPPORTED**: none of the cited anchors establishes the statement. This is not a claim that no other document could establish it.
- **INFERENCE**: a lane conclusion, not a fact stated or measured by the anchor.
- **LANE-LOCAL**: a fact about the lane/package, for which the external anchor is not evidence; I name separate local evidence where present.

Only literal text search was available for local cross-reference and provenance searches. Those results are reported as byte occurrences, not semantic reference analysis. The support findings below come from reading the opened source text, not from filename or heading matches.

## Main observed divergences

1. S123 supports the five positive privilege levels and the override sentence, but the anchored `The chain of command` list also contains **No Authority** for assistant/tool messages and quoted/untrusted/multimodal content. The entry's apparently exhaustive five-item enumeration is incomplete.
2. S124 is about triggering and description optimization. It does not assign authority to a skill body or describe description as governing all behaviour. It says **primary** trigger mechanism, and its `How skill triggering works` paragraph names task difficulty as another trigger condition.
3. The entry's universal skill-body authority claims cross S123's express scope boundary. S123 says the row makes no claim that any skill client implements the Model Spec. The original round-1 report separately records that no opened document states how a skill body's authority compares with a tool output, retrieved document, or sub-agent message.
4. S129's abstract supports the 853 / up-to-12 / 46 / approximately-40%-accuracy figures. It does not support the staged quote verbatim: the abstract says `requires`, not `requiring`, and the ellipsis replaces `with varying privileges, comprising` without a shaping note.
5. The entry cites S125 inline but omits S125 from its `source:` header. S125's `used-by` cell likewise omits this entry. The Qwen sentence is semantically supported, but its entry quotation changes the source's comma after `prompt text` to a period.
6. The entry's recheck says to check arXiv:2604.09443 `for a v2`. The abstract page and API identify v4; v4 dates to 2026-09-04, before the original 2026-10-23 opening.

## Entry: every factual statement against its cited anchor

### Provenance and framing

| Entry location | Statement | Verdict and evidence |
|---|---|---|
| Title | `the boundary it draws around skill bodies` | **NOT SUPPORTED as a sourced boundary.** S123 is OpenAI-scoped, S124 is trigger-scoped, and S129's abstract does not mention skills. No cited anchor maps a skill body into the ladder. |
| Lines 4–6 | S123 URL and Model Spec version 2026/08/18; S124 pinned file/tree; S129 arXiv id and abstract anchor | **SUPPORTED.** The Model Spec cache has `data-model-spec-version="2026-08-18"` and `August 18, 2026`; the pinned S124 file exists at the named commit; arXiv:2604.09443v4 has the quoted abstract. |
| Line 7 | `verified-at: 2026-10-23` | **LANE-LOCAL, corroborated for the original package round.** Original `SOURCES-PROPOSED.md:3,7,30–41` records the 2026-10-23 opening. This is not a round-67 verification date. |
| Line 8 | Recheck the five levels and held-out split; `re-check arXiv:2604.09443 for a v2 (ran 2026-10-23)` | **PARTIAL / stale target.** The five named levels and the S124 split exist. The `v2` target is not the current or original-round latest revision: `https://arxiv.org/abs/2604.09443v4` and the arXiv API identify v4, with v2/v3/v4 submission dates of 2026-04-13, 2026-04-14 and 2026-09-04. The original fetch ledger corroborates an opening on 2026-10-23, not a reason to expect only v2. |
| Line 9 | The instruction-authority layer was `previously unheld` in the lane | **LANE-LOCAL, corroborated; not established by the external anchors.** Original `SEARCH-LOG.md:41–44` identifies the Model Spec/ManyIH material as unopened leads, and `:115` calls the layer empty before that round. |

### Body

| Entry location and row | Factual statement (verbatim from the entry) | Verdict and anchor comparison |
|---|---|---|
| Lines 11–13, S123 | `OpenAI's Model Spec (2026/08/18) assigns every instruction a level of authority and states the override rule: "Instructions with higher authority override those with lower authority."` | **PARTIAL.** The override quotation is exact and supported. `Every instruction` is broader than the anchor's wording: `each instruction in this document, as well as those from users and developers` (`modelspec.txt:256–260`). The chain also assigns **No Authority** to other content (`:382–399`). |
| Lines 13–14, S123 | `The levels it defines, in order, are Root, System, Developer, User, Guideline.` | **PARTIAL — incomplete if exhaustive.** Those five occur in that order, but the same anchored chain immediately adds `No Authority: assistant and tool messages; quoted/untrusted text and multimodal data in other messages` (`modelspec.txt:382–394`; live Model Spec, `The chain of command`). |
| Line 14, S123 | `Root cannot be overridden by system, developer or user messages.` | **SUPPORTED.** `modelspec.txt:262–266` states this and strengthens it to system `(or any other)` messages. |
| Lines 14–15, S123 | `Guideline sits below user and is implicitly overridable from contextual cues.` | **SUPPORTED.** The order is at `:383–394`; implicit override from contextual cues is explicit at `:279–282`. |
| Lines 17–18, S123/S124/S129; compare inline S125 | `A SKILL.md body is not a privileged instruction; it is text that a model reads and may or may not obey.` | **NOT SUPPORTED as a universal statement.** No three-header source assigns a skill body's authority. S124 discusses invocation, not body obedience. Qwen's S125 supports the narrower client-specific statement that body text is prompt text and following it depends on the model (`qwen_en_skills.txt:115–116`); it does not establish `not privileged` or a cross-client rule. |
| Lines 18–20, S124 | `Anthropic's own reference skill treats the description as the thing that actually governs behaviour: the description field is "the primary mechanism that determines whether Claude invokes a skill."` | **PARTIAL.** The quoted fragment is exact (`skill-creator-SKILL.txt:333–335`), but it governs **whether Claude invokes a skill**, not behaviour generally. `The thing that actually governs behaviour` is not supported. |
| Lines 21–24, S124 and inline S125 | `So the craft surface splits cleanly in two — the description decides whether the skill is entered at all, and the body is obeyed only to the extent the model chooses to obey it.` | **PARTIAL / clean split is INFERENCE.** S124 says **primary** mechanism, and says simple tasks may not trigger even with a perfect description while Claude consults skills for tasks it cannot easily handle (`skill-creator-SKILL.txt:396–398`). Thus description alone does not decide entry. The body-dependence clause is supported only for Qwen by S125, not universally or by S124. |
| Lines 22–24, S125 | `Qwen Code states the second half in vendor prose (S125): "Everything in a SKILL.md body is an instruction to the model: it is prompt text."` | **SUPPORTED semantically, with quotation and provenance defects.** Qwen says exactly that fragment followed by `, so following it depends on the model.` (`qwen_en_skills.txt:115–116`). The entry substitutes a period inside the quotation. S125 is absent from the entry header and its row's `used-by` omits this entry. |
| Lines 26–28, S129 | `ManyIH (S129) argues the dominant fixed few-level paradigm is inadequate for agentic settings, where conflicts also arrive from tool outputs, sub-agent feedback and retrieved material.` | **PARTIAL.** The fixed-small-set inadequacy and tool outputs are explicit. The abstract says `other agents`, not specifically `sub-agent feedback`; it does not name `retrieved material`. Treating other agents/tool outputs as those two specific channels would be inference, not abstract text. |
| Lines 28–30, S129 | `Its benchmark requires navigating up to 12 levels of conflicting instructions across 853 agentic tasks spanning 46 real-world agents, and frontier models score roughly 40%.` | **PARTIAL.** Up to 12, 853 and 46 are explicitly supported. The performance statement needs the abstract's metric and condition: `current frontier models perform poorly (~40% accuracy) when instruction conflict scales`; it is not an unqualified overall score. |
| Lines 30–32, S129 | `So the ladder is not a solved problem: skill authors cannot assume their instruction outranks, or is outranked by, a retrieved document.` | **NOT SUPPORTED for the skill/retrieval comparison.** The abstract measures agentic instruction conflicts, not skill bodies or a skill-versus-retrieved-document authority relation. The opening difficulty conclusion is **INFERENCE** from poor results; the named skill-author rule does not follow from the benchmark. |
| Lines 34–35 | `Any future claim of the form "a skill body may instruct X" must name the authority level it is speaking at.` | **POLICY**, not a factual source claim. None of the sources imposes this lane rule; it must stand as a declared lane convention if used. |
| Lines 35–37, S123/S129 | `The lane previously had no row for this at all — S123 and S129 open that layer, and they open it as a rule plus its measurement, not as a slogan.` | **LANE-LOCAL + SUPPORTED characterization.** The prior absence is corroborated by original `SEARCH-LOG.md:41–44,115`, not by the sources. S123 does supply a normative rule and S129 an empirical measurement. This does not validate the stronger skill-body `outer bound` wording in S123's `teaches` cell. |

## Row-by-row claim audit

Curation labels (`kind`, `tier`, `status`) are package decisions rather than statements made by the external sources. I checked their internal references separately instead of attributing them to an anchor.

### S123 — OpenAI Model Spec

| Row claim | Verdict and evidence |
|---|---|
| Source title, URL and document version 2026/08/18 | **SUPPORTED.** Original HTML has the same version and date (`modelspec.html:1401,1869`). |
| `The normative authority ladder OpenAI trains against` | **SUPPORTED with the document's own caveat.** The overview says OpenAI is training models to align with the Model Spec (`modelspec.txt:189–191`); it also says production models do not yet fully reflect it. The row calls it normative, not a claim of complete deployed compliance. |
| Scope limited to ladder/override; no claim about non-OpenAI clients or skill-client implementation | **Internally supported scope.** This limitation is explicit in the row. Later skill-body claims must not silently exceed it. |
| Anchor headings, five named levels, override quote | **SUPPORTED but incomplete as a full chain inventory.** The quote is exact; the chain also contains No Authority. |
| `one ordered privilege ladder (root > system > developer > user > guideline) and the rule that higher authority wins` | **SUPPORTED for those positive privilege levels.** The source states both. |
| `— the outer bound on what a skill body may assert` (the final clause of the `teaches` sentence) | **NOT SUPPORTED.** The Model Spec does not mention `SKILL.md`, and this same row disclaims skill-client implementation. This clause also conflicts with the original round's unresolved-boundary note at `final_turn_001.md:230–234`. |
| `mined` and `used-by` names `instruction-authority-ladder.md` | **Internally consistent.** The staged entry cites S123. |
| Opened/recheck date 2026-10-23 | **Corroborated for original round 1.** `SOURCES-PROPOSED.md:30–41`, `SEARCH-LOG.md:74` (F8), and cached files timestamped 2026-10-23. Not a round-67 access date. |

### S124 — Anthropic skill-creator at `dbd4588…`

| Row claim | Verdict and evidence |
|---|---|
| Anthropic's own reference skill at the named full commit; tree date 2026-10-09 | **SUPPORTED.** The pinned file is present. GitHub's commit API returned SHA `dbd4588f9e1033efb41dad4bef2f7947c8993d44` and author/committer date `2026-10-09T18:45:49Z`. |
| Same tree pin as lane S012, same repo but different file | **LANE-LOCAL, supported.** Lane `corpus/SOURCES.md` S012 names the same full tree hash and `quick_validate.py`; this row names `SKILL.md`. |
| Scoped to Anthropic's description/trigger procedure, not other clients | **Supported scope.** The source is Claude-specific in the anchored passages. |
| Anchor sections and quote `Create 20 eval queries — a mix of should-trigger and should-not-trigger.` | **SUPPORTED and verbatim.** `skill-creator-SKILL.txt:333–339`. |
| `the description field is the trigger mechanism` | **PARTIAL — not supported as written if read as sole mechanism.** The source says **the primary mechanism** (`:335`). Dropping `primary` strengthens the claim. |
| `trigger fidelity is optimised by a held-out eval loop: 20 labelled queries, 60/40 train/test split, 3 runs per query, up to 5 iterations` | **SUPPORTED.** The 20 mixed labels are at `:337–339`; the 60% train / 40% held-out test, three runs and five iterations are explicit at `:394`. |
| `used-by` names this entry and `description-writing-and-trigger-testing.md` | **Internally consistent.** Both staged entries have S124 source lines. |
| Opened/recheck date 2026-10-23 | **Corroborated for original round 1.** `SOURCES-PROPOSED.md:30–41`, `SEARCH-LOG.md:73` (F7), and the 33,168-byte cache timestamped 2026-10-23. Not a round-67 access date. |

### S129 — ManyIH abstract

| Row claim | Verdict and evidence |
|---|---|
| Paper title and arXiv URL | **SUPPORTED.** The current versioned page is `https://arxiv.org/abs/2604.09443v4`. |
| Empirical instruction-conflict measurement rather than a normative fixed ladder; evidences difficulty and does not prescribe a concrete ladder | **SUPPORTED with scope.** The abstract proposes a ManyIH paradigm and benchmark, not a fixed Root/System/Developer-style ordering. Calling it a paradigm proposal is different from prescribing a concrete ladder. |
| Anchor quote `requiring models to navigate up to 12 levels of conflicting instructions … 853 agentic tasks` | **NOT SUPPORTED as a verbatim quote from the anchored abstract.** Actual text: `ManyIH-Bench requires models to navigate up to 12 levels of conflicting instructions with varying privileges, comprising 853 agentic tasks (427 coding and 426 instruction-following).` Besides the ellipsis, `requiring` differs from `requires`. No shaping note names the removed bytes. |
| `fixed few-tier instruction hierarchy is inadequate for agentic settings` | **SUPPORTED.** This closely tracks the abstract's fixed, small-set inadequacy statement. |
| `853 tasks over 12 privilege levels and 46 real-world agents` | **PARTIAL.** 853 and 46 are supported; the source says **up to 12** levels, not that every task or the benchmark uniformly has exactly 12. Preserve `up to`. |
| `frontier models at roughly 40% accuracy` | **PARTIAL.** Supported only with the abstract's condition `when instruction conflict scales`. |
| `mined` and `used-by` names this entry | **Internally consistent.** The staged entry cites S129. |
| Opened/recheck date 2026-10-23 | **Corroborated for original round 1.** `SOURCES-PROPOSED.md:30–41` and `SEARCH-LOG.md:81,85–88` (F15: full papers via `aaron papers fetch`). Not a round-67 access date. |

## Required quote, pipe and access-date checks

The counts below are actual `wc -w` results on the exact staged quote strings. The standalone em dash/ellipsis each count as a whitespace-delimited token; excluding them would only lower the counts.

| Row | `wc -w` | Over 25 words? | Literal or backslash-escaped pipe inside quote? | Verbatim at cited anchor? |
|---|---:|---|---|---|
| S123 | 9 | No | No | Yes — checked against original `modelspec.txt`. |
| S124 | 11 | No | No | Yes — checked against original pinned `skill-creator-SKILL.txt`. |
| S129 | 15 | No | No | **No** — see the `requires` / `requiring` and omission finding above. |

Commands run and observed outputs:

```text
wc -w <<< 'Instructions with higher authority override those with lower authority.'
9
wc -w <<< 'Create 20 eval queries — a mix of should-trigger and should-not-trigger.'
11
wc -w <<< 'requiring models to navigate up to 12 levels of conflicting instructions … 853 agentic tasks'
15
```

A normalized-text check over `https://arxiv.org/abs/2604.09443v4` printed:

```text
staged_quote_verbatim=False
actual_sentence_present=True
v4_marker_present=True
```

A separate pipe check over the three parsed anchor cells printed `literal-pipe=False` and `backslash-pipe=False` for each quote. Table-delimiter pipes outside the quotations are not quote content.

**Access dates:** none of the three quotations itself names an access date. All three rows' `opened` cells say 2026-10-23, and that is consistent with the original corpus-expansion-1 round record and fetch ledger. I found **no fabricated original-round access date**. S124's `2026-10-09` is a commit date, not an access date, and it is corroborated by GitHub's API.

For round 67, the distinction is different: the staged dates and entry `verified-at: 2026-10-23` are prior-round dates, not this round's required 2026-10-24 re-grounding. I re-opened all three sources on 2026-10-24 for this review. Thus the old dates are valid original provenance but must not be represented as the round-67 opening.

For completeness, the inline S125 quotation in the entry is not one of the three requested row quotes. Its row's unterminated fragment is verbatim, but the entry's version ending `prompt text.` is not: the source continues `prompt text, so following it depends on the model.` The local exact check printed `S125-row quote_verbatim=True` and `S125-entry quote_verbatim=False`.

## Evidence chain and last-known-good boundary

Original, durable evidence read:

- `/home/vgpnk/Projects/shokuknow/lanes/kotoba/SOURCES-PROPOSED.md:3–9,16–22,28–52` — original round/date, all three rows and opening attestation.
- `/home/vgpnk/Projects/shokuknow/lanes/kotoba/SEARCH-LOG.md:63–88` — F7 S124, F8 S123 and F15 S129 fetch records.
- `/home/vgpnk/Projects/shokuknow/lanes/kotoba/.deepresearch/raw-20261023_171642/modelspec.txt:252–287,373–399` — exact S123 wording, five levels plus No Authority and default treatment of other content.
- `/home/vgpnk/Projects/shokuknow/lanes/kotoba/.deepresearch/raw-20261023_171642/skill-creator-SKILL.txt:333–339,394–398` — primary trigger mechanism, eval numbers and the extra task-difficulty condition.
- `/home/vgpnk/Projects/shokuknow/lanes/kotoba/.deepresearch/raw-20261023_171642/qwen_en_skills.txt:9–13,115–116` — Qwen-only body dependence and explicit/model invocation distinction.
- `/home/vgpnk/Projects/shokuknow/lanes/kotoba/.deepresearch/20261023_171642_kotoba-corpus/final_turn_001.md:216–234` — the original unresolved-boundary statement.
- Public current sources: `https://model-spec.openai.com/2026-08-18`, the pinned S124 GitHub URL, `https://arxiv.org/abs/2604.09443v4`, and `https://export.arxiv.org/api/query?id_list=2604.09443`.

The last-known-good source-scope invariant visible in the package is: **S123 supplies an OpenAI normative ladder; S124 supplies Anthropic trigger procedure; S129 supplies an abstract-level agentic measurement; none supplies a client-independent skill-body authority mapping.** The original round report preserves that invariant at lines 230–234. The staged entry and S123's final `teaches` clause diverge where they assert an `outer bound` and universal skill-body authority/trigger conclusions.

## Confidence and bounds

- **High confidence** for quotation mismatches, source wording, numeric qualifications, the No Authority omission, the S125 header/`used-by` mismatch, revision v4 and quote/date checks: each was directly read or mechanically checked.
- **High confidence** that S123/S124/S129 do not directly support the universal skill-body authority mapping. This is an anchor-scope finding, not a claim that such a mapping is false everywhere.
- **Moderate-to-high confidence** for original access-date corroboration. S123/S124 also have original cached bytes; S129's date rests on the original row, opening attestation and F15 fetch ledger rather than a located raw arXiv cache in that directory.
- `PARTIAL` and `INFERENCE` explicitly mark reviewer interpretation where the source supports a narrower statement. No judgment is made about the other 161 staged rows, the full ManyIH paper beyond its anchored abstract, production integration, or either frozen C1/C2 counter.

No tools were installed or updated. No git/jj write command was run. No package, domain, corpus-production, index, or lane-state file was modified; this report is the only written artifact.
