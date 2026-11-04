source: S213 — Agent Skills — Optimizing skill descriptions — https://agentskills.io/skill-creation/optimizing-descriptions.md — § How skill triggering works, § Writing effective descriptions, § Designing trigger eval queries — re-opened live 2026-11-04 (HTTP 200, 13 403 B, sha256 `7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837`; byte-identical to the committed snapshot `.ufo/waves/round-76/snapshots/optimizing-descriptions.md`; fetch record `.ufo/waves/round-85/w1/ScoutSource/fetch-record.txt`, located quotes `.ufo/waves/round-85/w1/ScoutSource/source-packet.md`)
verified-at: 2026-11-04
recheck: 90d — `curl -sL https://agentskills.io/skill-creation/optimizing-descriptions.md | sha256sum` must print `7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837`; re-open and relocate each quoted passage before relying on it (ran 2026-11-04). A changed digest requires review, not automatic rejection of the current page.
ground: S213's description-authoring guidance is re-opened and connected to this lane's unchanged description and rejected round-85 counter. This documentary note does not establish trigger accuracy or a runtime improvement.

# Description trigger discipline — the specification's own page, and what the lane's description still violates (round 85)

Documentary note. Page quotations below are located in S213's bytes re-opened on
2026-11-04 (`.ufo/waves/round-85/w1/ScoutSource/source-packet.md`).
No client trigger evaluation was run: the page supplies authoring guidance and an
eval design, not evidence that this lane's proposed description triggers better.

## 1. The description carries the whole triggering burden

The page opens with a two-sided error model: "An under-specified description means the skill won't trigger when it should; an over-broad description means it triggers when it shouldn't." (page line 9). The mechanism it names is progressive disclosure — at startup the agent loads "only the `name` and `description` of each available skill — just enough to decide when a skill might be relevant" (page line 15) — so the conclusion is that "the description carries the entire burden of triggering" (page line 17). Both halves of the error model are therefore repaired in the same field: the description must be specific enough not to miss and narrow enough not to over-fire.

## 2. The authoring rules the page states

- **Imperative, addressed to the agent.** “**Use imperative phrasing.** Frame the description as an instruction to the agent: "Use this skill when..." rather than "This skill does..."” (page line 25). The agent is deciding whether to act, so the text tells it when to act.
- **User intent, not mechanics.** "Describe what the user is trying to achieve, not the skill's internal mechanics." (page line 26) — the agent matches against what the user asked for.
- **Pushy, including cases that never name the domain.** "Explicitly list contexts where the skill applies, including cases where the user doesn't name the domain directly" (page line 27).
- **Inside the ceiling.** "The [specification](https://agentskills.io/specification.md#description-field) enforces a hard limit of 1024 characters." (page line 28). The page's own closing checklist repeats the ceiling as a step to verify, not a target to approach.

## 3. The eval design, and the caveat that bounds it

The page specifies a labelled eval set: "Aim for about 20 queries: 8-10 that should trigger and 8-10 that shouldn't." (page line 41). Two clauses say which rows matter. The valuable positives are the indirect ones — "The most useful should-trigger queries are ones where the skill would help but the connection isn't obvious from the query alone." (page line 52). The valuable negatives are the near-misses — "The most valuable negative test cases are **near-misses** — queries that share keywords or concepts with your skill but actually need something different." (page line 56) — because an obviously irrelevant query is wasted: “`"Write a fibonacci function"` — obviously irrelevant, tests nothing.” (page line 60).

The page also says "agents typically only consult skills for tasks that require knowledge or capabilities beyond what they can handle alone" (page line 19). **Lane inference:** a trigger miss alone cannot identify a wording defect; the task's need for specialist knowledge also matters.

## 4. Negative boundaries: do not infer a prohibition

S213 recommends near-miss negative queries in the eval set. It does **not** prohibit
negative scope wording in a description: its optimization-loop section explicitly
suggests clarifying what a skill does not do when false triggers occur. This lane
therefore retains its existing `Anti-triggers:` clause without attributing a
positive-only description rule to S213.

The staged package's TRAE/Chiba comparison is **not adopted**. Its cited page identities
were not re-opened for this entry, and the old wave records do not supply current
source-registry grounding for those positions. Flip: open the original sources in a
later round, locate the relevant text, and evaluate each claim separately.

## 5. This lane's own before, and the candidate it did not take

The production `SKILL.md` description parses to **1 021 characters**, with a **150-character first sentence** (151 including its period), using `verifiers/check_sibling_census.py`'s `description_of()` helper (`.ufo/waves/round-85/w1/ScribeC1Entry/receipt.txt`, 2026-11-04). `Triggers:` starts at offset 152 and `Anti-triggers:` at 302. These lie beyond the cache-miss renderer's 99-UTF-16-unit prefix for long descriptions; the renderer may shorten that prefix further at a sentence or word boundary. A cached one-liner bypasses that branch. See `.ufo/waves/round-85/w1/RevengerRender/probe.md`; no universal live-listing ceiling is inferred.

The round-85 plan's candidate payload is **876 characters** with a **64-character first sentence** and **ten clauses**, six of them sibling-ownership clauses naming all ten non-none lanes: the sibling guard reads "skill description names 10 of 10 non-none lanes" and exits 0 on a file carrying that description (`verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md --province PROVINCE.md --skill <file>`), and the description's first sentence now carries `Use this skill when` and fits inside the listing cut. Its eval set carries **9 should-trigger and 9 should-not-trigger rows** with 5 indirect positives and every negative sharing a word of 4 or more characters with the description — inside the rule's 8–10-per-label band.

**None of it is applied.** The production `SKILL.md` description is unchanged at 1 021 characters with a 150-character first sentence, and both the candidate and its eval set live only under `.ufo/waves/round-85/w1/ExecC1Eval/`. The round-85 C1 counter was killed before any after-value existed: the reviewer's attack showed the frozen R6 accepted nine identical positives and irrelevant negatives with incidental token overlap (`.ufo/waves/round-85/w1/ReviewerC1.md`, findings High and Medium), the instrument was quarantined as historical bytes with its own fixture set (`.ufo/waves/round-85/frozen/QUARANTINE.txt`), and C1 is an honest miss, not a narrowing. This entry is the documentary half of that round: the rules the page states, and the measurement of what the lane's own description does and does not yet do.

## Limits

- Documentary evidence only. S213's page was fetched and quoted; no agent, harness or client was run, and no trigger, load or routing decision was observed here.
- No production change is claimed. The 876-character candidate was never applied, the eval set is a wave artifact, and the counter that would have scored them is quarantined, not an active gate.
- The TRAE/Chiba comparison and the duplicate best-practices half of the staged package are refused here. Neither is silently admitted under S213's authority.
- The 1 021 / 150 / 876 / 64 / ten-clause / 9+9 figures are this lane's own measurements of the committed description and of the plan's frozen candidate, reproducible with the commands named in the text; the counter's own committed fixture carries a different 9+10 split, also inside the band.

## Counter

`python3 -B verifiers/check_description_render.py --rev <rev>`

The counter is the frozen round-85 C1 instrument; its bytes are preserved at
`.ufo/waves/round-85/frozen/check_description_render.py` with
`.ufo/waves/round-85/frozen/QUARANTINE.txt`, and it is **not an active gate** — C1 was
killed before any after-value existed, and the production `SKILL.md` description is
unchanged.
