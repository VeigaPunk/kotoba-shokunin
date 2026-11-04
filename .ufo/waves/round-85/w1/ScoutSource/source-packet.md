# ScoutSource — S213 opened live (round 85, w1)

Seat: `ScoutSource`. Round 85 attempt 1, lane kotoba, host linux, date 2026-11-04.
This seat **opens S213 live**. It mints no SOURCES row (S213 already holds this URL; a new row
would be a W04 duplicate — the round-74 rejection reason). No write anywhere in shokuknow.

## 1. Source identity

| field | value |
|---|---|
| url | https://agentskills.io/skill-creation/optimizing-descriptions.md |
| lane source id | **S213** (supersedes S210 for citation; S210 is the same URL, earlier row) |
| access date | 2026-11-04 |
| HTTP status | **200** |
| bytes | **13 403** (13403) |
| sha256 | **7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837** |
| lines | 196 |
| exact fetch command | `curl -sL -o "$S/page.md" -w 'HTTP %{http_code} size %{size_download}\n' https://agentskills.io/skill-creation/optimizing-descriptions.md` |
| fetch output | `HTTP 200 size 13403` |
| byte-identity | `cmp` exit 0 vs the lane's committed snapshot `.ufo/waves/round-76/snapshots/optimizing-descriptions.md` (same sha256); same digest pinned at round 77 (`.ufo/waves/round-77/w1/S01Reopen1.md`). **S213 has not moved.** |

Fetch record with the full command/output transcript: `.ufo/waves/round-85/w1/ScoutSource/fetch-record.txt`.

Supporting fetch for the staged entry's second half (best-practices.md): HTTP 200, 15 060 B,
sha256 `ab9f3b6091a0f24816b52cd7b90a3fdf53e621f47dba13b36694be272b87fb41` — identical to the
round-77 pin. (Not minted as a row; the lane already holds it as **S223**.)

Line numbers below are `grep -n` line numbers of the **live fetched bytes** (196-line file), the
same bytes as the committed r76 snapshot.

## 2. The five required quotes (verbatim, ≤ 25 words each)

| # | need | page line | quote (verbatim) | words | what it grounds |
|---|---|---|---|---|---|
| a | description carries the burden of triggering | **17** | `This means the description carries the entire burden of triggering.` | **10** | The lane's core claim that the description is the whole trigger mechanism — the premise of C1 (the description must be rewritten, not just documented). |
| b | imperative "Use this skill when…" authoring form | **25** | `**Use imperative phrasing.** Frame the description as an instruction to the agent: "Use this skill when..." rather than "This skill does..."` | **21** | The authoring form of C1's candidate description and of rule **R4 `imperative_invocation`** (the literal `Use this skill when` string). |
| c | trigger-eval design | **41** | `Aim for about 20 queries: 8-10 that should trigger and 8-10 that shouldn't.` | **13** | Rule **R6 `eval_set_shape`** — the 8–10 / 8–10 split and the ≈20-query budget of the eval set. |
| c2 | trigger-eval design (near-miss negatives) | **56** | `The most valuable negative test cases are **near-misses** — queries that share keywords or concepts with your skill but actually need something different.` | **23** | R6's second half — that the negatives must share vocabulary with the description (near-miss) rather than being obviously irrelevant. |
| d | the 1024-character description limit | **28** | `The [specification](https://agentskills.io/specification.md#description-field) enforces a hard limit of 1024 characters.` | **9** | Rule **R3 `spec_max_1024`** — the spec/vendor ceiling the lane's 1 021-char description is measured against. |
| e | caveat: agents consult skills only for knowledge beyond them | **19** | `One important nuance: agents typically only consult skills for tasks that require knowledge or capabilities beyond what they can handle alone.` | **21** | The trigger-miss caveat — bounds what a description can achieve, so trigger-miss data cannot be read as a description defect without separating "wrong description" from "task needed no skill". |

Supplementary located quotes (also ≤ 25 words, for the entry scribe and the counter's fixture):

| page line | quote (verbatim) | words | grounds |
|---|---|---|---|
| 9 | `An under-specified description means the skill won't trigger when it should; an over-broad description means it triggers when it shouldn't.` | 20 | The two-sided error model: the lane's `Triggers:` + `Anti-triggers:` structure in the candidate description. |
| 26 | `Describe what the user is trying to achieve, not the skill's internal mechanics.` | 13 | Why the candidate description names user situations rather than mechanics. |
| 27 | `Explicitly list contexts where the skill applies, including cases where the user doesn't name the domain directly` | 17 | The "pushy / even if they don't name it" requirement — the indirect positives R6 asks for (≥5 should-trigger rows containing none of the declared trigger terms). |
| 52 | `The most useful should-trigger queries are ones where the skill would help but the connection isn't obvious from the query alone.` | 21 | Directly grounds R6's "indirect positives" clause. |
| 60 | `` `"Write a fibonacci function"` — obviously irrelevant, tests nothing. `` | 9 | Why the negatives must be near-misses: an obviously irrelevant query tests nothing. |
| 159 | `Check that the description stays under the 1024-character limit — descriptions tend to grow during optimization.` | 16 | Why R3's ceiling must be re-checked after every edit, and the reason the 1 021/1 024 headroom is a live risk. |
| 174 | `Verify the description is under the [1024-character limit](https://agentskills.io/specification.md#description-field).` | 8 | The apply-the-result checklist item for R3. |
| 92 | `A should-not-trigger query passes if its trigger rate is below that threshold.` | 12 | The pass criterion for negatives (complements the S213 quote already in the row). |
| 15 | `At startup, they load only the `name` and `description` of each available skill — just enough to decide when a skill might be relevant.` | 24 | The progressive-disclosure mechanism behind quote (a). Within the 25-word cap, so usable as a located quote if the entry wants it. |

Note: every quote listed here is within the 25-word cap, and quotes (a)–(e) are the five the seat
spec asked for. Word counts are whitespace token counts of the quoted string as it appears in the
page bytes.

best-practices.md (lane row S223), located quotes for the staged entry's second half:

| page line | quote (verbatim) | words |
|---|---|---|
| 96 | `Match the specificity of your instructions to the fragility of the task.` | 12 |
| 147 | `A skill should teach the agent *how to approach* a class of problems, not *what to produce* for a specific instance.` | 21 |
| 129 | `When multiple tools or approaches could work, pick a default and mention alternatives briefly rather than presenting them as equal options.` | 21 |

## 3. Staged-claim verdict table

Staged entry (read-only, never modified):
`/home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/spec-description-trigger-discipline.md`
Rejection row (read-only):
`corpus/lessons/round-74-verifier-spotcheck.md:116` — *"staged `spec-description-trigger-discipline.md` | reject | … the URL is already held twice (S210, S213), so the row would be a W04 duplicate; its best-practices half (staged S232) is now carried by the admitted S223 entry; flip stated"*.

Verdict rule applied: **survives** = the staged claim's substance is located in the live bytes
(quote found, verbatim, within the word cap, at the stated place) **or** is a plain inference from
a located quote with no contradicting text on the page. **Refused** = the quote is not present, or
the page says otherwise, or the claim is not carried by S213/S223 at all.

| # | staged claim | verdict | reason (page line, or why refused) |
|---|---|---|---|
| 1 | "An under-specified description means the skill won't trigger when it should; an over-broad description means it triggers when it shouldn't." | **survives** | verbatim at page line **9**, 20 words (≤25). |
| 2 | "the description carries the entire burden of triggering" (because the agent loads only `name` and `description` at startup) | **survives** | verbatim at page line **17** (10 words); the `name`/`description`-only startup loading is at page line **15** (prose support). |
| 3 | Frame the description as an instruction — "Use this skill when…" rather than "This skill does…" | **survives** | verbatim at page line **25**, 21 words (≤25). |
| 4 | Describe what the user is trying to achieve, not the skill's internal mechanics | **survives** | verbatim at page line **26**, 13 words. |
| 5 | Be pushy; list the contexts where the skill applies, including cases where the user never names the domain | **survives** | verbatim at page line **27**, 17 words. |
| 6 | Keep the description inside the 1024-character limit the specification enforces | **survives** | verbatim at page line **28**, 9 words; reinforced at **159** and **174**. |
| 7 | About 20 labelled queries, 8–10 should trigger and 8–10 should not | **survives** | verbatim at page line **41**, 13 words. |
| 8 | Should-trigger queries vary phrasing, explicitness, detail and complexity; the valuable ones are those where the connection is not obvious from the query alone | **survives** | the four variation axes at page lines **47–51**; the "connection isn't obvious" sentence at **52**, 21 words. |
| 9 | The negatives must be near-misses (share keywords/concepts, need something different); an obviously irrelevant query "tests nothing" and only measures breadth | **survives** | near-miss sentence at page line **56**, 23 words; "tests nothing" at **60**, 9 words. The clause "only measures breadth" is the staged entry's own paraphrase — page line 56 says the near-misses "test whether the description is precise, not just broad"; the paraphrase is consistent, but it is **not** a quote and must not be carried as one. |
| 10 | Agents "typically only consult skills for tasks that require knowledge or capabilities beyond what they can handle alone"; a one-step request like "read this PDF" may not trigger a PDF skill even if the description matches perfectly | **survives** | verbatim at page line **19**, 21 words (≤25); the "read this PDF" example is in the same sentence. |
| 11 | Trigger-miss telemetry that does not separate "the description was wrong" from "the task did not need the skill" will misattribute cause | **refused (as a page claim)** | The page contains **no** telemetry sentence — `grep -n "telemetry\|misattribut" page.md` → no match. The claim is a sound inference from quote (e), but it is **not** carried by S213; it must be labelled as the lane's inference in the re-grounded entry, never cited to the page. |
| 12 | Best-practices half: "Match the specificity of your instructions to the fragility of the task"; give a default rather than a menu of equal options; "a skill should teach the agent *how to approach* a class of problems, not *what to produce* for a specific instance" | **survives, but stays refused material** | All three quotes located verbatim on best-practices.md (lines **96**, **129**, **147**; 12/21/21 words). But this half is the round-74 refusal: it is already carried by the admitted lane entry behind **S223**, so the round-85 entry must **not** restate it — recorded here as located-and-refused, with the reason (already carried; duplicate). |
| 13 | Three-way tension about negative conditions (specification = pushy positive + negatives in the eval set; ByteDance TRAE = both forms in the description; Chiba = negative forms are hard to convey) | **refused (not a S213/S223 claim)** | The TRAE and Chiba positions are cited by the staged entry to "wave-2 rows", not to S213 or S223; neither page says anything about negative *directives* in a body. This material is out of the re-grounding scope of this seat and must not be folded into the round-85 S213 entry. |

### Registry-id mapping the re-grounded entry must respect

The staged entry cites the two pages as **S231** and **S232** — ids from the *shokuknow package's*
`SOURCES.append.md`, not from this lane's `corpus/SOURCES.md`. In **this** lane:

| staged id | same URL | **lane id (use this)** |
|---|---|---|
| S231 | `…/optimizing-descriptions.md` | **S213** (supersedes S210, which is the same URL) |
| S232 | `…/best-practices.md` | **S223** |

In the lane's own `corpus/SOURCES.md`, `S231` is a different row entirely (Mistral Vibe README,
line 172) and `S232` is OpenAI Codex Skills (line 173). A round-85 entry that copied the staged
`source:` ids verbatim would therefore point at the wrong rows. The round-85 entry must cite
**S213** (and, only if it restates the best-practices half — which it must not — S223).

### Byte-count cross-check against the staged entry

The staged entry records the page as "fetched as `.md` 13 403 B on 2026-10-23". Today's live fetch is
**13 403 B**, sha256 `7cc54fbb…`, byte-identical to the lane's committed r76 snapshot and to the
round-77 pin. The staged entry's fetch record is therefore **current**, and its `recheck:` clause
("confirm the quoted rules and the 20-query / 8-10 figures are unchanged") is satisfied by today's
re-fetch: all quoted rules and the 8–10/8–10 figures are unchanged.

## 4. What this seat hands to C1

- **R3** `spec_max_1024` → grounded, page line 28.
- **R4** `imperative_invocation` → grounded, page line 25 (the literal `Use this skill when` string).
- **R6** `eval_set_shape` → grounded, page lines 41, 52, 56, 60 (the 8–10/8–10 split, the
  indirect-positive clause, the near-miss-negative clause).
- **R8** `sourced_entry` → the re-grounded entry can name **S213**, `verified-at: 2026-11-04`, a
  `recheck:` value, and carry a located quote within the cap — quote (b) (21 words) or quote (a)
  (10 words) both satisfy the ≤25-word located-quote requirement.
- **R1/R2/R5/R7** are not sourced to this page and are not claimed here (R5 is the sibling-census
  guard, R7 the packager rule).

## 5. Provenance

- Fetch: `curl` (already present; no tool installed or upgraded — nothing to record under the
  operator tooling directive).
- Scratch: `/fast/scratch/hyaku/kotoba-r85/ScoutSource` (created with `mkdir -p`, used as TMPDIR for
  the fetches, removed with `trap 'rm -rf -- "$S"' EXIT` before yielding).
- Writes, all inside the lane and only under this seat's own wave dir:
  `.ufo/waves/round-85/w1/ScoutSource/fetch-record.txt`,
  `.ufo/waves/round-85/w1/ScoutSource/source-packet.md`,
  `.ufo/waves/round-85/w1/ScoutSource.md`.
- shokuknow: **read-only** — two files read, zero writes.
