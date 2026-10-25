# CriticProvenance — round 67 wave 1

## Measured object and review axes

- **Review target:** the read-only package file
  `/home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/instruction-authority-ladder.md`
  (`ENTRY` below), sha256 `cfa0ab9f77f58c2450fa593220eb70a55b484fd1a92dcc09339006cad2090122`.
  This is a package artifact, **not a committed lane revision**.
- **Pinned base:** `2a8eba56b3f9321b70c569fa2816d42237ca49a2`. My read-only
  `git rev-parse master` and `git rev-parse HEAD` both printed that hash. Base-only comparisons used a
  `git archive` of that commit extracted under `/tmp/critic-provenance-r67-base`; I did not treat later
  working-tree files as base evidence.
- **Axes attacked:** depth/actionable craft, claim-source consistency, province/adjacency, and source
  freshness. I did not run either frozen C1/C2 predicate and make no round or tip verdict.
- **Candidate disposition:** **refuse verbatim; admit-bounded after the corrections below.** The defects
  are in the proposed text, not in the goal of holding instruction-authority craft. No content sentence
  earns an unqualified `admit` in the package as written; several have a sound bounded core.

## Province answer

The **host-specific, documented mapping of a skill body to an invocation path and instruction slot** is
inside kotoba's prompt-and-skill-craft province (`PROVINCE.md:3-6`). A craft rule that tells an author to
identify the client, loading slot, invocation path, and any delegation before relying on precedence is
also inside it.

The entry does **not** absorb chousa's research method: it does not teach chousa's question → source
hierarchy → citation chain → claim-vs-source procedure. The citation repairs below come from kotoba's own
`QUALITY.md` and the fleet corpus contract, not a second research method (`PROVINCE.md:49`;
`CORPUS.md:119-122`).

It **does absorb kengaku ground** when it reports generic model-benchmark design and frontier-model
performance as corpus knowledge (`ENTRY:26-30`). `PROVINCE.md:57` assigns LLM/model research and
evaluation, including measured capability effects, to kengaku. A bounded pointer to an external paper to
explain why a craft mapping is not established is distinguishable; restating `12` levels, `853` tasks,
`46` agents, and `~40%` frontier accuracy is the clear cross-boundary sentence. Report that measurement
to the orchestrator/kengaku rather than absorbing it. The runtime-sounding obedience claims are acceptable
only as explicitly attributed client documentation, not observed cross-client runtime behaviour; kotoba
owns prompt wording, not the orchestration runtime (`PROVINCE.md:59`).

## Strongest counterexamples

1. **The description is not the universal gate to a skill.** The entry says it “decides whether the
   skill is entered at all” (`ENTRY:20-22`). Yet its own inline Qwen source documents direct user
   invocation: “If you want to invoke a Skill explicitly, type it as a slash command” and “Skills are
   user-invocable by default” (S125, fetched page, `How Skills are invoked` and `Optional: control user
   and model invocation`; text extraction `/tmp/critic-provenance-r67-s125.txt:865-879,1123-1126`).
   It also says a user path can run a path-gated body regardless of activation state (`:1116`). This is a
   documented counterexample, not an inference. Even S124 limits its statement to whether **Claude
   invokes** a skill and separately says task simplicity/complexity affects consultation
   (`/tmp/critic-provenance-r67-s124.md:335,396-400`).

2. **S123 contains the rung the entry omits, and it governs the retrieved-content question.** Under
   `The chain of command`, S123 says: “No Authority: assistant and tool messages; quoted/untrusted text
   and multimodal data in other messages” (`/tmp/critic-provenance-r67-s123.txt:2557-2580`). Its
   `Ignore untrusted data by default` section says tool outputs have no authority **by default**, while
   allowing authority to be delegated (`:6455-6463,6479-6502`). Thus the entry's five-rung list is
   incomplete for its stated purpose, and S129 does not justify a categorical claim that no fixed
   skill/retrieved-document ordering can be assumed. Under S123 the answer depends on message role,
   quoting/trust, and delegation; a host that puts skill bytes in an unquoted developer message gives
   them developer authority under that spec. That is a role-mapping counterexample to intrinsic file
   privilege, not a claim that any particular skill client was observed doing so.

3. **S129 is not a measurement of S123 or of `SKILL.md`.** S123 is OpenAI's normative model contract;
   S129 proposes and measures ManyIH on generic agentic tasks. The entry's final phrase “a rule plus
   **its measurement**” (`ENTRY:35-37`) falsely makes the latter sound like a validation of the former.
   The package's own S123 row says it makes no claim that any skill client implements the spec, and its
   S129 row says the paper does not prescribe a ladder (`SOURCES.append.md:7,13`). Those bounds must
   survive into the entry.

## Sentence-by-sentence verdicts

Line references are to `ENTRY`. “Bounded” below means both a scope correction and the located-quote
repair needed for the attributed rule; merely adding more citations to the universal wording is unsafe.

### 1. The ladder

**S1 — `ENTRY:11-13` — refuse as written.**

> OpenAI's Model Spec (2026/08/18) assigns every instruction a level of authority and states the override rule: "Instructions with higher authority override those with lower authority."

The quoted override sentence is exact and admissible **for OpenAI's contract**. “Every instruction” is
not: the source says each instruction *in that document* plus user/developer instructions, and separately
classifies assistant/tool messages and quoted/untrusted content as `No Authority`. Replace the first
clause with that actual population; do not turn it into a property of every skill host.

**S2 — `ENTRY:13-14` — admit-bounded.**

> The levels it defines, in order, are Root, System, Developer, User, Guideline.

The named subsection does list those five in that order. The entry also cites `The chain of command`,
whose ordering adds `No Authority`. Say “five named levels under the first heading, plus No Authority in
the chain-of-command ordering”; the omission is material because tool/retrieved content is the entry's
next topic.

**S3 — `ENTRY:14` — admit-bounded.**

> Root cannot be overridden by system, developer or user messages.

S123 directly supports this, including the stronger “system (or any other) messages” wording
(`/tmp/critic-provenance-r67-s123.txt:2243-2252`). Keep it explicitly OpenAI/Model-Spec-scoped and add a
located quote such as “Root: Fundamental root rules that cannot be overridden by system messages,
developers or users.” It does not establish that a skill body is Root.

**S4 — `ENTRY:14-15` — admit-bounded.**

> Guideline sits below user and is implicitly overridable from contextual cues.

S123 supports Model Spec **guideline sections**, not any informal guideline written by a skill author.
Its exact text includes “guidelines can be overridden implicitly (e.g., from contextual cues, background
knowledge, or user history)” (`:2298-2304`; also `:2586`). Name that limited referent and quote it.

### 2. Why it matters to skill craft

**S5 — `ENTRY:17-18` — refuse as written.**

> A `SKILL.md` body is not a privileged instruction; it is text that a model reads and may or may not obey.

A filename has no intrinsic authority level. Qwen supports the narrower statement that its body is prompt
text and following it depends on the model; S123 instead assigns authority according to the containing
message. Replace the universal with per-client documentation: client, invocation route, message/loading
slot, and any documented delegation. “Not privileged” is not an actionable or portable craft rule without
those fields.

**S6 — `ENTRY:18-20` — refuse as written; the quoted trigger clause is admit-bounded.**

> Anthropic's own reference skill treats the description as the thing that actually governs behaviour: the description field is "the primary mechanism that determines whether Claude invokes a skill."

The quoted fragment genuinely occurs at pinned S124 line 335, but it concerns **model-triggering**, not
“behaviour” as a whole and not every invocation route. The safe claim is: in this pinned Anthropic
reference skill, the description is the primary mechanism determining whether Claude invokes a skill.
Do not expand it to body compliance, all clients, or user invocation.

**S7 — `ENTRY:20-22` — refuse.**

> So the craft surface splits cleanly in two — the *description* decides whether the skill is entered at all, and the *body* is obeyed only to the extent the model chooses to obey it.

The first clause is falsified by Qwen's documented user-invocation route and overreads S124; the second is
only Qwen-scoped evidence, not a clean cross-client split. The word “cleanly” hides precisely the host,
route, and task-dependence distinctions an author must check.

**S8 — `ENTRY:22-24` — admit-bounded.**

> Qwen Code states the second half in vendor prose (S125): "Everything in a SKILL.md body is an instruction to the model: it is prompt text."

Qwen does state the model-dependence claim, but the presented quotation silently replaces the source's
comma with a full stop and drops “so following it depends on the model.” The entry's punctuated sentence
is not an exact substring of the fetched page. Add S125 to the opening provenance, preserve the shaping
explicitly or use the exact short quote “it is prompt text, so following it depends on the model.” Keep
the claim Qwen-only.

### 3. Measurement and retrieval

**S9 — `ENTRY:26-28` — admit-bounded as an attributed external pointer, not as lane-owned model research.**

> ManyIH (S129) argues the dominant fixed few-level paradigm is inadequate for agentic settings, where conflicts also arrive from tool outputs, sub-agent feedback and retrieved material.

The abstract supports the attributed fixed-small-set critique and names tool outputs and other agents.
The cited `# abstract` does not contain “retrieved material”; “sub-agent feedback” is also a paraphrase of
“other agents,” not a quotation. Use an exact abstract quote, preserve “real-world agentic settings,” and
state that this is generic agent research with no demonstrated `SKILL.md` mapping. Delete the unsupported
retrieval clause or ground it separately. This sentence is fixable; the performance census in S10 is the
province tradeoff.

**S10 — `ENTRY:28-30` — refuse from this kotoba entry.**

> Its benchmark requires navigating up to 12 levels of conflicting instructions across 853 agentic tasks spanning 46 real-world agents, and frontier models score roughly 40%.

The abstract does support the broad figures, including “up to,” but the entry supplies no direct quote and
no `<number> — <command> <date>` for these counts as `QUALITY.md` Q13 requires. It also drops the
abstract's qualifier “when instruction conflict scales” from the `~40%` result. More fundamentally, this
is model-evaluation content for kengaku, not an action a skill-craft reader can take. Route it; do not try
to cure the province breach solely by adding a citation.

**S11 — `ENTRY:30-32` — refuse.**

> So the ladder is not a solved problem: skill authors cannot assume their instruction outranks, or is outranked by, a retrieved document.

S129 does not test `SKILL.md` placement or client-specific retrieval precedence, so this transfer is
unmeasured. S123 supplies a default (`No Authority` for tool/quoted content) plus delegation, which is
more precise than “cannot assume either.” The portable craft rule is: **do not infer precedence from the
filename; record the host's documented slot/trust/delegation rule, and mark it unheld when undocumented.**
That is actionable without fabricating a universal ladder.

### 4. Consequence and historical claim

**S12 — `ENTRY:34-35` — admit-bounded.**

> Any future claim of the form "a skill body may instruct X" must name the authority level it is speaking at.

This is a useful craft instinct but an insufficient and potentially misleading admission rule: a host may
have no documented OpenAI-style level to name. Require **client/host, invocation path, message/loading
slot, trust/quoting and delegation, and the source for that mapping**; if no mapping is documented, say
`unheld` rather than inventing a level. Use OpenAI's labels only for S123's own context.

**S13 — `ENTRY:35-37` — refuse as written.**

> The lane previously had no row for this at all — S123 and S129 open that layer, and they open it as a *rule plus its measurement*, not as a slogan.

There are two independent defects. First, the negative has no sweep as Q14 requires and “row” is
undefined. The pinned base already contains related instruction-surface and skill-selection knowledge
(`corpus/README.md:40-41`; `knowledge/skill-selection-rules-round50.md:18-25`) and lists Model Spec and
ManyIH as **unopened leads** (`corpus/SOURCES.md:226,268`). Those facts do not disprove a narrowly worded
“no admitted coverage-map entry for cross-source instruction authority,” but they defeat “no prior
mention/ground at all.” Narrow the object, cite the base sweep, and move the historical commentary to the
round lesson. Second, S129 is not a measurement *of* S123, as counterexample 3 explains.

The metadata sentence `ground: ... previously unheld` (`ENTRY:9`) has the same negative-claim defect and
needs the same bounded wording and sweep; it is not a substitute for that evidence.

## Citation and provenance audit

This is the complete citation-level accounting for `ENTRY`.

| citation | quoted versus asserted | disposition and required repair |
|---|---|---|
| **S123** (`source:` line 4; prose 11-15) | **Mixed.** The higher-authority override sentence is quoted exactly. “Every instruction,” the level inventory, Root, and Guideline are asserted paraphrases without their own located quotes. | **Admit-bounded core.** Correct the population, add `No Authority` and delegation, and quote the Root/Guideline rules relied on. The row's `teaches` phrase “outer bound on what a skill body may assert” also exceeds the same row's express scope (“no claim ... any skill client implements it”); do not import that phrase. |
| **S124** (`source:` line 5; prose 17-22) | **Mixed.** “The primary mechanism ... Claude invokes a skill” is a real quote. “Actually governs behaviour” and the “cleanly in two” synthesis are asserted, not quoted, and are broader than the source. | **Refuse the synthesis; admit-bounded trigger claim.** The staged row's anchor quotes “Create 20 eval queries ...,” not the trigger quote used by this entry (`SOURCES.append.md:8`). Align the entry and row with the exact relevant quote; an unrelated eval quote does not ground this prose. |
| **S125** (inline only at 23-24) | **Shaped quotation plus missing provenance.** There is no opening `source:` line, URL, or anchor for S125. The entry changes the source's comma after “prompt text” to a full stop and omits the model-dependence continuation. The package row's `used-by` also omits `instruction-authority-ladder.md` (`SOURCES.append.md:9`). | **Admit-bounded Qwen claim only.** Add the full provenance line and back-reference, use an exact located quote or document shaping under Q42/Q53, and retain the source's scope as one vendor rather than a cross-client contract. |
| **S129** (`source:` line 6; prose 26-37) | **Entirely asserted in the entry.** None of the three S129 prose sentences contains a direct abstract quote. The fixed-IH and broad numeric paraphrases mostly track the abstract; “retrieved material” is not in the cited abstract, and the `~40%` paraphrase loses its scaling condition. “Its measurement” is unsupported by either source. | **Refuse the metric absorption and the claimed validation relation.** If a craft-only pointer remains, pin the revision, use an exact abstract quote, and state explicitly that it does not measure S123 or skill bodies. |

Additional provenance defects that a verbatim copy would carry:

- **Stale revision check:** the arXiv page opened this round identifies **v4**, submitted as v1 on
  2026-04-10 and last revised 2026-09-04 (`/tmp/critic-provenance-r67-s129.txt:114-140,160-168`). The
  package recheck says to look “for a v2” (`ENTRY:8`). Pin v4 if that is the evidence used and check for
  later revisions, not the already-superseded v2 threshold.
- **Recheck does not cover the claims made:** `ENTRY:8` checks five levels and S124's held-out split, but
  the entry uses neither the sixth rung nor the held-out split as its craft content; it omits S125 entirely
  and does not re-check S129's 46-agent/~40% statements. If S125 remains, its staged row uses a 30-day
  cadence, so an entry-wide 90-day check is not sufficient for that source.
- **Round grounding is not a date substitution:** package `verified-at: 2026-10-23` is not the frozen C2
  round's `2026-10-24` grounding. I re-opened all four URLs on 2026-10-24 as recorded below; integration
  still must adopt only the exact located quotes and corrected claims, not merely bump the date.
- **C2 quote alignment:** the plan requires each cited source's entry quote to occur in that source row's
  anchor (`plans/round-67.md:83-90`). As packaged, S124's used quote is absent from its row anchor and
  S129 has no entry quote at all. This is observed content evidence, not a claim that I ran or scored the
  frozen counter.

## Smallest safe correction

1. **Cheapest province-safe path:** remove S10 and the “rule plus its measurement” synthesis and route the
   ManyIH performance result to the orchestrator/kengaku. If no bounded craft pointer to S129 is needed,
   drop S129 from this entry and do not append it as a `mined` row for this entry. If a pointer is kept,
   pin v4, use one exact abstract quote, and say only that generic agent research does not establish a
   skill-client mapping.
2. **Bound S123 to OpenAI and complete its own model:** replace “every instruction” with the source's
   population; include `No Authority`; explain that tool/quoted content defaults to no authority unless
   delegated. Never infer a skill body's level from its filename.
3. **Replace the universal skill-body/trigger split with per-client statements:** S124 supports a primary
   Claude **model-invocation** mechanism only; S125 supports Qwen prompt-text/model-dependent following
   and also documents direct user invocation. These sources do not make one cross-vendor authority law.
4. **Make the craft consequence checkable:** require client/host + invocation path + loading/message slot
   + trust/quoting/delegation + located source, with `unheld` when the mapping is absent. This preserves
   the useful depth without forcing a false OpenAI label onto every client.
5. **Repair provenance before adoption:** add S125's opening row and `used-by` back-reference; use exact
   located quotes; align S124's row anchor; make recheck cover every retained source/claim and its actual
   cadence; re-ground at the round date rather than copying `2026-10-23`.
6. **Delete or narrow the historical novelty sentence:** if retained in the lesson, define “row” as the
   coverage-map object, acknowledge the base's related entries and unopened leads, and attach the base
   sweep required by Q14. Do not claim S129 measured S123.

These are fixable text/provenance defects except for the model-evaluation absorption: that is a province
tradeoff that citation polish cannot make kotoba-owned. Removing the unsupported universals improves
depth rather than reducing it, because the remaining claims become actionable and falsifiable.

## Sources actually opened by this seat

All four fetches returned HTTP 200 on 2026-10-24. Snapshots were written only under `/tmp`; no package or
lane production bytes were mutated.

| id | URL opened | bytes | sha256 |
|---|---|---:|---|
| S123 | `https://model-spec.openai.com/2026-08-18` | 2662295 | `72db50e5063c3c8942671c3ce6e30d0dd643de558eefd690aab127ec53bf4e5a` |
| S124 | `https://raw.githubusercontent.com/anthropics/skills/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/SKILL.md` | 33168 | `dcd4803e61e913e6fc27294184cd3a71f09f5e924ff20c8a9a20173e7b3c2bcf` |
| S125 | `https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/` | 606421 | `52461383332301e627b661fb156817bec3ba7a046ef94b2cee06cb3748cdd2a6` |
| S129 | `https://arxiv.org/abs/2604.09443` | 43281 | `3d3ca32cdfb668da9f554f0a75070d4784db8a780393bbf74987700028b45209` |

HTML was converted to text for location and containment checks; S124 was checked as raw Markdown.
No quote here is claimed byte-exact against HTML source encoding. The direct containment check printed:

```text
S123 override exact: True
S123 No Authority exact: True
S124 trigger quote exact: True
S125 entry punctuated quote exact: False
S125 omitted continuation exact: True
S129 v4 record: True
S129 retrieved material phrase: False
```

The last result is bounded to the fetched arXiv abstract page cited by `ENTRY`, not a claim about every
page of the paper. No tools were installed or upgraded; fetches used `curl`, and checks/conversion used
Python 3 stdlib, `sha256sum`, `wc`, read-only `git archive`/`rev-parse`, and the file-search tools.
