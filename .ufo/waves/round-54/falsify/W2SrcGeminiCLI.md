# W2SrcGeminiCLI — falsify C1's Gemini CLI rows (S057, entry row, Gate row, SKILL.md row)

Result: MIXED — every attacked cell holds verbatim and within evidence except one: entry § Findings item 3 drops the banner's "Unpaid tier and Google One users" scope when it says "Gemini CLI was replaced by Antigravity CLI on 2026-06-18" (minor, wording only; proposed fix below).

Scope attacked: `corpus/SOURCES.md:70` (S057), `corpus/knowledge/skill-listing-thresholds-round54.md` (Findings 3, Per-client record Gemini row, Limits line), `corpus/lessons/round-54.md:27` (Gate row), `SKILL.md:189` (Description thresholds row), all at landed tip `58db81c4465b0e9b07ef2485b87d8970683afac6`. Sandbox: `/fast/scratch/hyaku/kotoba-r54/W2SrcGeminiCLI/` (clone at tip, fetches under `fetch/`). No lane writes; no installs (system `curl`, `python3`, `git` only).

## Counter re-run (sandbox clone at tip)

```
$ python3 -B verifiers/check_description_thresholds.py --rev 58db81c4465b0e9b07ef2485b87d8970683afac6
Gemini CLI   BACKED        description thresholds backed 7 of 7 clients   rc=0
$ python3 -B verifiers/check_description_thresholds.py --rev 58db81c4... --fetch
Gemini CLI   BACKED found=True   backed 7 of 7; found on the live page 7 of 7   rc=0
```
Plan erratum 3 guard (a): `git show e3371548:corpus/SOURCES.md | grep -c S057` → 0 (row opened this round). Guard (c): `--fetch` finds the quote live. Guard (b) is a ≥2-clients aggregate; for Gemini alone, `git show e3371548:SKILL.md | grep -c -F '100'` = 4, so `~100 words` is not itself a new-to-SKILL.md token — not a defect, the guard is claimed at the claim level and other clients supply it.

## My re-open of the source (2026-10-22T22:02–22:09Z, curl, no browser)

| URL | UTC | HTTP | bytes | sha256 |
|---|---|---|---|---|
| https://geminicli.com/docs/cli/skills-best-practices.md | 22:02:31Z | 200 | 3,257 | `612c3b8396fdc6669702127975c5d4ec5ce59bd8355fdbfb837fdd83d3d524c3` — **byte-identical to the row's record** |
| https://geminicli.com/docs/cli/skills-best-practices/ | 22:02:31Z | 200 | 104,469 | `40bb440debc96489a6ce663571dcfaab87290fb630a80b6f86d64856f66230f0` — identical to record; no-slash route 301 → slash (47 B) |
| https://raw.githubusercontent.com/google-gemini/gemini-cli/451a02ff03f1d2a8fe870c120fd5342cfd6f9fd1/docs/cli/skills-best-practices.md | 22:03:36Z | 200 | 3,258 | `a064fd7f…` — `cmp` vs served: identical except served lacks trailing newline, as recorded |
| raw `docs/cli/skills.md` @451a02ff | 22:03:36Z | 200 | 5,740 | `51e8573e…`; served `skills.md` re-fetch 5,763 B `8e1b4cbe…` — both match the seat record |
| raw `skillLoader.ts`, `snippets.ts`, `promptProvider.ts`, `skillsCommand.ts` @451a02ff | 22:03:36Z | 200 | 6,560 / 70,505 / 11,751 / 11,017 B | `8bce3215…` (loader; matches seat), `b2cccbd0…`, … |
| served `creating-skills.md`, `using-agent-skills.md`, `cli-reference.md`, `changelogs/latest.md` | 22:06–22:08Z | 200 | 6,705 / 3,052 / 16,561 / 4,140 B | `b7061545…`, `9e61fb7c…`, `2d445008…`, `f3821508…` — all match the seat record |

## Per-cell verdicts

**SOURCES S057 row (corpus/SOURCES.md:70): HOLDS.** 11 cells (verified, 12 pipes), tier A, kind docs, status mined, opened 2026-10-22, used-by names the entry; sits in order between S056 and S058. Question cell bounds itself ("vendor documentation of a soft budget, not a measurement of any installed binary"). Anchor verified in full: fetch stamp/status/bytes/hash all byte-exact; byte-identical-modulo-newline claim reproduced by `cmp`; slash-route hash reproduced; "S029 already cites this page at `:24`" confirmed (SOURCES.md:42 teaches cell ends "`skills-best-practices.md:24`"). Teaches cell ("always in context as metadata budgeted at about 100 words") is a fair restatement of line 24; "budgeted" is an interpretive word for a bare "(~100 words)", but the seat disclosed "a size, not a limit" in the entry Findings — borderline, disclosed, holds.

**Gate row (corpus/lessons/round-54.md:27): HOLDS.** URL, UTC (21:16:27Z), `3,257 B, sha256 612c3b83…` all match my re-fetch exactly; quote and location match the entry row, which the counter requires verbatim.

**Entry Per-client record row (:43): HOLDS.**
- Quote `Metadata (name + description): Always in context (~100 words).` is verbatim at `skills-best-practices.md:24` of the fetched bytes: the fetched line is `1.  **Metadata (name + description)**: Always in context (~100 words).` — the quote drops only the list ordinal `1.` and the `**` emphasis (markup, not words; 9 words, `100` a whole token under the counter's boundary regex; seat disclosed the mechanics at `SrcGeminiCLI.md:67`).
- Number is about the `description` (with `name`): the level-1 metadata item is explicitly "name + description", and `skills.md:20-22` (verified) says the name and description of all enabled skills are injected into the system prompt at session start. No other-field confusion (cf. the rejected Copilot plugin-cap row at lesson:42).
- Reading cell stays inside evidence: "soft per-skill listing budget" is the disclosed reading; "the client documents nothing" past it is backed by the three-leg Q30 sweep (`SrcGeminiCLI.md` §6) plus my own re-sweep (`creating-skills.md`, `using-agent-skills.md`, `cli-reference.md` carry zero numeric skill limits; best-practices has only `:24` and the `<5k words` body figure at `:25`); "the description reaches the prompt whole" is code reading at the pinned commit, which I reproduced: `skillLoader.ts:211` `description: frontmatter.description,` (only transforms: quote-strip and multi-line join — no truncation); `snippets.ts:320` `<description>${skill.description}</description>` (exact line confirmed); `promptProvider.ts:120-126,166-173` passes `description: s.description` through; `skillsCommand.ts` `nodesc` affects only the `/skills list` UI. The entry's preamble (:8) licenses source-reading statements, and the seat marked runtime behavior [INFERENCE] (:169). "cost is context tokens" follows from "always in context".

**SKILL.md row (:189): HOLDS.** Threshold cell has exactly one number token (`100`) matching the quote token; cells are labeled "metadata (name + description)", not misread as a description-only cap; "Nothing is cut … spends context tokens" matches the verified code path; action cell's "loads only after activation (`skills-best-practices.md:24-25`)" is verbatim-supported (`:25` "Loaded only after the skill triggers"). No contradiction with older SKILL.md content (`:94` instructions-placement row cites S036; `:435` disable-command row; portability floor mentions no Gemini cap).

**Entry Findings item 3 (:27-30): one BREAKS (minor).**
- "name plus description are always in context at '~100 words' (S057); seat SrcGeminiCLI read the loader at 451a02ff and found no cut" — HOLDS.
- "The docs host now carries a banner saying Gemini CLI was replaced by Antigravity CLI on 2026-06-18" — BREAKS in scope: the banner's actual text (re-fetched 22:02:31Z, sha `40bb440d…`) is "**Unpaid tier and Google One users:** Gemini CLI was replaced by Antigravity CLI on June 18th, 2026." The finding drops the scope qualifier, recording a blanket replacement. Under Q31 (a statement may say no more than its evidence) this is an over-wide record, same class as rounds 50-53 recurrences — small, since the cited seat did label it "site chrome only" and the inference (short recheck cadence) is unaffected.
  Proposed fix text: `The docs host now carries a banner saying "Unpaid tier and Google One users: Gemini CLI was replaced by Antigravity CLI on June 18th, 2026." (seat ScribeS046Fix, site chrome only), so the recheck cadence for S057 should be short.`
- Limits line (:66) "no client was run … comes from reading source, not from a run" — HOLDS, matches the seat's own marking.

**Contradiction check vs older lane rows/entries: HOLDS.** S029 (`SOURCES.md:42`, the same page family) already records "the soft budget is \"~100 words\" of metadata, `skills-best-practices.md:24`" and "`1024` → 0" — S057 is consistent and is honestly framed as confirmation, not discovery (anchor + Findings + `SrcGeminiCLI.md` §F2). S029's used-by entries (`sibling-overlap-census-round49.md:218-220`, `skill-selection-rules-round50.md:23`, `skill-overlap-levers-round51.md:25`) hold only precedence/lever claims; none states a description size or cut, so nothing is contradicted. `alwayson-rule-files-round53.md` and `mcp-server-instructions-round52.md` mention Gemini CLI on unrelated surfaces.

## Residual risk / gaps

- "Budget" (SOURCES teaches, entry reading) is interpretation of a bare "(~100 words)"; the lane mitigates by labeling it "soft" and "a size, not a limit". I judge this disclosed and within the record.
- `promptProvider.ts` snippet: the unfiltered `s.description` pass-through is verified; whether `withSection('agentSkills', …)` or a later model-side stage truncates is not measured — the entry says "reaches the prompt", which is exactly as far as the code evidence goes; borderline wording, backed by named shipped source per the entry preamble.
- Nothing else in scope found attackable: verbatim quote, byte-identical fetch receipts, exact code line numbers, counter and `--fetch` reproduced 7 of 7 with Gemini BACKED.
