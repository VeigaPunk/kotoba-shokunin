# B04QuotesScribe — S213 located quotes (round 76, w1)

Verdict: `B04QuotesScribe: DONE — 13 page-unique located quotes (3–23 words, lines 17–159) verified against snapshot bytes sha256 7cc54fbb…bfd837; 2 requested rule families absent from S213 and reported absent`.

Role: scribe (report-only). Item: extract located quotes for S213's description-craft rules and
write them as build input. No claim data written; no counters run; no git/jj writes.

## Behavior

1. **Snapshot absent at start** (13:56 local): `ls .ufo/waves/round-76/snapshots/` →
   `No such file or directory` (exit 2), and there was no `build/` dir either. Per the item's
   fallback, I fetched the three pages myself into
   `/fast/scratch/hyaku/kotoba-r76/B04QuotesScribe/`.
2. **Fetch** (`curl -sS -L`, HTTP code via `-w '%{http_code}'`), 2026-10-27 ~16:57Z:

   | page | http | bytes | sha256 |
   |---|---|---|---|
   | optimizing-descriptions.md | 200 | 13403 | `7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837` |
   | evaluating-skills.md | 200 | 16973 | `a799805f3a285390c1b6e906b691f56684fa1031b499d177f664f464d99fb684` |
   | best-practices.md | 200 | 15060 | `ab9f3b6091a0f24816b52cd7b90a3fdf53e621f47dba13b36694be272b87fb41` |

   `curl -sSI -L` on the quoted URL: `HTTP/2 200`, `content-type: text/markdown; charset=utf-8`.
3. **B03's snapshots landed at 13:57** as `.md` (not `.html`). Re-ran everything against those bytes:
   `sha256sum` gives the same three digests; `cmp -s` against my fetch of
   optimizing-descriptions.md → clean → `OPT IDENTICAL` (exit 0), 196 lines. So the line numbers I
   report are B03's snapshot line numbers, not just my own fetch's.
4. **Extraction + verification** in one pass over the snapshot bytes: exact-substring `in` test,
   `len(quote.split()) ≤ 25`, line = 1 + count of `\n` before the match, nearest preceding `#`
   heading, occurrence count in the page, membership in both sibling snapshots, and absence from the
   page's 3-line docs-index chrome block (lines 1–3).
5. **Wrote** `.ufo/waves/round-76/build/quotes-s213.md` (table + machine-readable JSON + absence
   findings + limits), then **re-verified the written file**: parsed its JSON block, re-derived line
   and word count for all 13 quotes → `quotes: 13 bad: []`, all 13 table rows present, each table
   quote cell occurs in the snapshot; the sha256 line is present.
6. **Calibration call to B13SkillPatch** (its row cites this file): confirmed all three fragments B13
   uses are exact, page-unique substrings at L27/L159/L157, and warned that "front-loading the use
   case" and "self-contained first sentence" are **not** on S213 so must not be attributed to it.

## Quotes (all 13 verified; full table + JSON in the artifact)

| Rule | Line | Heading | Words | Quote |
|---|---|---|---|---|
| imperative phrasing | 25 | `## Writing effective descriptions` | 3 | Use imperative phrasing. |
| imperative phrasing | 25 | `## Writing effective descriptions` | 18 | Frame the description as an instruction to the agent: "Use this skill when..." rather than "This skill does..." |
| user intent | 26 | `## Writing effective descriptions` | 13 | Describe what the user is trying to achieve, not the skill's internal mechanics. |
| pushy | 27 | `## Writing effective descriptions` | 7 | Err on the side of being pushy |
| pushy | 27 | `## Writing effective descriptions` | 17 | Explicitly list contexts where the skill applies, including cases where the user doesn't name the domain directly |
| trigger-surface burden | 17 | `## How skill triggering works` | 10 | This means the description carries the entire burden of triggering. |
| trigger-surface coverage | 45 | `### Should-trigger queries` | 9 | These test whether the description captures the skill's scope. |
| trigger-surface coverage | 155 | `## The optimization loop` | 23 | If should-trigger queries are failing, the description may be too narrow. Broaden the scope or add context about when the skill is useful. |
| length | 28 | `## Writing effective descriptions` | 10 | A few sentences to a short paragraph is usually right |
| length | 28 | `## Writing effective descriptions` | 19 | long enough to cover the skill's scope, short enough that it doesn't bloat the agent's context across many skills |
| length (hard ceiling) | 28 | `## Writing effective descriptions` | 7 | enforces a hard limit of 1024 characters. |
| length (growth) | 159 | `## The optimization loop` | 16 | Check that the description stays under the 1024-character limit — descriptions tend to grow during optimization. |
| anti-overfit | 157 | `## The optimization loop` | 7 | Avoid adding specific keywords from failed queries |

Uniform per-row facts: occurrences in page = 1; absent from evaluating-skills.md and
best-practices.md bodies (`in_evaluating/in_best_practices = false`); line > first heading (line 5);
no chrome-block hit.

## Findings

- **F1 (operability) — RESOLVED by B03, verified here.** At my first look (13:56) the snapshots dir
  did not exist; at 13:59 the three `.md` files landed without manifest/record; re-checked at 14:00
  and both are present. `sha256sum -c MANIFEST.sha256` in
  `.ufo/waves/round-76/snapshots/` → `optimizing-descriptions.md: OK`, `evaluating-skills.md: OK`,
  `best-practices.md: OK`, exit 0; `fetch-record.json` carries three records with `http_status: 200`
  and digests/byte counts identical to my independent fetch (`7cc54fbb…`/13403, `a799805f…`/16973,
  `ab9f3b60…`/15060). Conjunct (a)'s remaining piece is the in-counter digest table (B06).
- **F2 (calibration, material to the headline): S213 does not teach "front-loading the use case" or
  "self-contained first sentence".** `grep -in` over the snapshot for `front-load`, `front load`,
  `use case`, `lead with`, `starts with`, `opening`, `single sentence`, `one-sentence`,
  `first sentence`, `self-contained`, `self contained` → zero hits on all eleven patterns. Its
  worked "After" example (lines 179–190) leads with capability clauses and puts `Use this skill when`
  second, and line 192 explains the improvement as *more specific about what it does* + *broader
  about when it applies*. Any entry/row wording that credits S213 with front-loading or a
  self-contained first sentence is an unsourced upgrade; the four sourced families are imperative
  phrasing, pushiness/breadth, trigger-surface coverage, and length (incl. the 1024-character
  ceiling).
- **F3 (freshness dependency):** the located quotes are line-numbered against snapshot bytes
  `7cc54fbb…`. Any re-fetch that changes those bytes invalidates every line number here; the
  `cmp`/`sha256sum` of `.ufo/waves/round-76/snapshots/optimizing-descriptions.md` must stay
  `7cc54fbb…` for the entry's citations to remain true.
- **F4 (consistency, minor):** B13's draft row quotes "Err on the side of being pushy",
  "descriptions tend to grow during optimization", "Avoid adding specific keywords from failed
  queries" — all verified exact and page-unique (L27/L159/L157). Its "imperative" claim is prose
  only; a fourth fragment (e.g. `Use imperative phrasing.`, L25, 3 words) would make the row quote
  the rule it asserts. Conjunct (c)'s ≥2-fragment bar is already met either way.
- **F5 (limits):** documentary quotes only — no agent client run, no trigger-rate measurement, so
  eval fidelity stays held (plan C1 / r75 Gate untouched). The chrome check is against the two
  sibling `.md` bodies plus this page's 3-line docs-index block; rendered-site nav chrome was not
  fetched this round and is not excluded by this method.

## Gates / conformance

- Writes: only `.ufo/waves/round-76/build/quotes-s213.md` and this report. Scratch under
  `/fast/scratch/hyaku/kotoba-r76/B04QuotesScribe/` removed at exit. Nothing under `/tmp`, no fleet
  repo file, no `~/.local/bin` change, no pacman, no tool installs (curl/python3 were already
  present).
- No git/jj writes; the only git-family calls were none (read-only inspection used `ls`/`sha256sum`/
  `cmp`/`grep`/python).
- No subagents, no background jobs beyond one `curl` batch; at most 4 concurrent processes.
- No claim data, counter, SKILL.md, registry, lesson or LOG bytes touched — pre-freeze drafts only.

## Touched surfaces (absolute)

- `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-76/build/quotes-s213.md` (new, 11672 bytes)
- `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-76/w1/B04QuotesScribe.md` (this report)
- message to `agent://B13SkillPatch` (fragment confirmation + absence warning)

Read-only inputs: `.ufo/waves/round-76/snapshots/{optimizing-descriptions,evaluating-skills,best-practices}.md`,
`.ufo/waves/round-76/{w1-spec.json,base-battery/base-battery.txt}`, `plans/round-76.md`,
`.ufo/waves/round-76/build/skill-patch.md`.

## Out of scope (not done here, by seat design)

`snapshots/MANIFEST.sha256` + `snapshots/fetch-record.json` (B03); `corpus/knowledge/description-craft-round76.md`
(B12); `verifiers/check_desc_craft.py` (B06); S213 `used-by` cell (B14); § Body craft row application
(L1 integration); SCORECARD/LOG/lesson rows (B08/B17–B19).
