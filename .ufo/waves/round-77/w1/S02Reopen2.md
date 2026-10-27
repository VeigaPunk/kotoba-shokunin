# S02Reopen2 — independent re-open of S213 (optimizing-descriptions.md)

## Fetch (urllib, not curl)
`python3` `urllib.request.urlopen` with User-Agent `S02Reopen2-urllib`, 2026-10-27: HTTP 200, `text/markdown; charset=utf-8`, no redirect, 13403 bytes, 196 lines, sha256 `7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837` = the pin. `cmp` against `.ufo/waves/round-76/snapshots/optimizing-descriptions.md`: byte-identical. The three snapshot hashes in MANIFEST.sha256 match fetch-record.json. The page was served live with a Last-Modified equal to the fetch Date, so I cannot use that header for page age; the digest equality is the evidence.

## Different quote, by line
"The agent is deciding whether to act, so tell it when to act." — `optimizing-descriptions.md:25` (last sentence of the "Use imperative phrasing" bullet), 13 words, one matching line, absent from `evaluating-skills.md` and `best-practices.md` (grep -c 0/0). Not in the r76 table.

## The five rules in the r76 entry-draft table (literal substring checks, script over the fetched bytes)
| draft quote | stated line | found at |
|---|---|---|
| Frame the description as an instruction to the agent | 25 | 25 |
| Describe what the user is trying to achieve, not the skill's internal mechanics. | 26 | 26 |
| Err on the side of being pushy | 27 | 27 |
| Explicitly list contexts where the skill applies, including cases where the user doesn't name the domain directly | 27 | 27 |
| A few sentences to a short paragraph is usually right | 28 | 28 |

Token cells (`Use imperative phrasing` :25, `Focus on user intent, not implementation` :26, `Keep it concise` :28) also exist at the stated lines. Other cites check: the line 1 quote (:9, 20 words) found; caution (:19) found; "hard limit of 1024 characters" :28; "burden of triggering" :17; the absence sweep (`front-load`, `front load`, `use case`, `lead with`, `starts with`, `first sentence`, `self-contained`) returns 0 lines on the page. Every table quote is absent from the other two snapshots.

## Overclaims (rule attributed to the page that the page does not state)
None among the five rules. Page-stated content = the quoted sentences. Not page text, only draft gloss (flag if C1 counts the "action" column as sourced): "a missed context costs the whole skill" (:27 row), "a description that needs the full character allowance is a finding, not a fit" (:28 row), and the rule labels "err toward over-inclusion of contexts" (the page says "pushy" + list contexts; a fair paraphrase, not a quote).

## Minor imprecision (not overclaim)
- Draft cites the worked example as `:184`–`:188`; the "After" description runs :184–:189 (the "even if they don't explicitly mention" tail is on :189). The "imperative clause second" reading ("Use this skill when…" at :186–:187) stands.
- The draft's "four principles ... (`:17`)": the principles are the four bullets :25–:28 (intro :23); :17 is the "burden of triggering" sentence. Cite :23–:28 for the principles.
- The page's `:19` caution is about whether agents consult skills at all; the draft states it correctly as a limit.

Tools installed: none.

VERDICT: S213 re-opened via urllib — HTTP 200, 13403 bytes, sha256 equals the pin; all five description-writing rules found at the draft's stated lines (:25,:26,:27,:27,:28); no overclaim, two minor line-cite imprecisions (:184–:188 vs :189; :17 vs :23–:28).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/S02Reopen2.access-record.txt /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/S02Reopen2.md
