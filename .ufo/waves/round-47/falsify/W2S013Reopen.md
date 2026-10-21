verdict: PARTIAL — S013's taught facts survive a byte-identical live re-open, but the row's `anchor` cell and the lesson Gate's quote location name a section that does not contain the budget/shortening sentence, and the seat receipt records the compressed wire size as the markdown byte count.

# W2S013Reopen — OpenAI "Build skills" (SOURCES S013) at `7ad7fad`

Scope: re-open `https://learn.chatgpt.com/docs/build-skills` (the 308 target of
`developers.openai.com/codex/skills`), and check the landed row
`corpus/SOURCES.md:26` and its Gate record `corpus/lessons/round-47.md:36` against the
live page and `SOURCES-CONTRACT-v1` (`.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`).
Read-only against the fleet lane; mutations performed only in the private clone
`/fast/scratch/kotoba-r47/w2/W2S013Reopen/kotoba-shokunin` at `7ad7fad`.
Access window: `2026-10-21T16:54:47Z`–`16:56Z` (response `date` headers).

## Target question — answered YES

The page still states the initial-list budget and description-first shortening,
verbatim, in the `.md` representation and the server-rendered HTML:

- `s013-page.md:38-39` — "this list uses at most 2% of the model's context window,
  or 8,000 characters when the context window is unknown."
- `s013-page.md:40` — "If many skills are installed, Codex shortens skill
  descriptions first."
- `s013-page.md:99-103` — implicit invocation "matches the skill `description`" /
  "Because implicit matching depends on `description`"; `:218`
  `allow_implicit_invocation` (default `true`).

Freshness is exact, not approximate. The live fetch reproduces the wave-1 bytes:

| representation | live now | recorded in `.ufo/waves/round-47/build/SrcNewCodexSkills.json` |
|---|---|---|
| HTML decoded | 417,112 B, sha256 `78abf995…e81`, ETag `W/"ffc66e55…dc7"`, Last-Modified `2026-10-21T15:05:00Z` | identical (`SrcNewCodexSkills.json:57-68`) |
| markdown | 11,035 B, 232 lines, sha256 `ed6e324f…9d5` | sha256/lines identical; **bytes recorded as 3,970** |

So the content claim of S013 holds; the defects below are citation/record accuracy,
not source drift.

## F1 — the row's section anchor and the Gate's quote location are wrong (calibration; contract rule 1)

`corpus/SOURCES.md:26` anchors the row at "§ How ChatGPT and Codex use skills".
`corpus/lessons/round-47.md:36` grounds the budget quote at "(§ How ChatGPT and Codex
use skills)". That heading is at `s013-page.md:91`; the quoted sentence is at
`s013-page.md:38`, in the page intro under the H1, **53 lines before the section**.
Rendered HTML agrees: the budget sentence starts at byte offset 322,603; the
`<h2 id="how-chatgpt-and-codex-use-skills">` starts at 334,649; the nearest preceding
heading is the H1 at 293,715.

Of the three facts in `teaches`, only description-gated implicit invocation lives in
the named section; the budget and the "shortens skill descriptions first" sentence do
not. A re-checker following the Gate's location into that section will not find the
quoted sentence.

The seat receipt is self-contradictory on exactly this point:
`.ufo/waves/round-47/build/SrcNewCodexSkills.md:29` records the anchor at `md:89/91`, while `:67` says the
quote is located at "§ How ChatGPT and Codex use skills, md lines 37–39" — lines
37–39 precede line 89. The line span is roughly right; the section label is not.

Repro (clone root; any thrown-away dir works):

```
$ curl -sS -L --compressed -o s013-page.md https://learn.chatgpt.com/docs/build-skills.md   # exit 0
$ curl -sS -L --compressed -o s013.md https://learn.chatgpt.com/docs/build-skills            # exit 0
$ grep -n 'at most 2% of the model\|^## How ChatGPT and Codex use skills' s013-page.md
38:this list uses at most 2% of the model's
91:## How ChatGPT and Codex use skills
$ python3 -c "h=open('s013.md').read(); i=h.find('at most 2% of the model'); j=h.find('<h2 id=\"how-chatgpt-and-codex-use-skills\"'); print(i,j,i<j)"
322603 334649 True
```

Contract basis: `anchor` is "exact section / heading / page / line plus revision"
(`SOURCES-CONTRACT-v1.md` § Shape) and rule 1 requires the Gate's "≤25-word quote with
its location grounding `teaches`". The quote is 20 words (§ Gate, counted) and is
verbatim after whitespace normalisation, so only the location fails. Rule 2 forbids an
in-place anchor edit; the S001 precedent in the same Gate (a wrong anchor label recorded
in the lesson, correction deferred to a superseding row) is the model for the fix.

Minor cell nuance in the same row: `teaches` says the list is "cap[ped] … at 2% of
context" without "by default". The page immediately documents the override —
`skills.max_context_tokens`, "a different budget, up to 10,000 tokens"
(`s013-page.md:42-44`). The summary is true of the default and false for a configured
client, so it should carry "by default" if it is ever re-stated.

## F2 — receipt records the br-compressed transfer size as the markdown byte count (evidence record)

`.ufo/waves/round-47/build/SrcNewCodexSkills.json:41` and `:73` say `"bytes": 3970`
for the markdown whose `"sha256"` (`:40`, `:75`) is `ed6e324f…` and whose `"lines"` is
232. Same hash with a different byte count is impossible: the decoded markdown is
**11,035 B** (both hosts, both with and without `--compressed`). The number 3,970 is
exactly the compressed download size:

```
$ curl -sS -o /dev/null --compressed -w 'size_download=%{size_download}\n' https://learn.chatgpt.com/docs/build-skills.md
size_download=3970
$ curl -sS --compressed https://learn.chatgpt.com/docs/build-skills.md | wc -c
11035
$ curl -sS -L --compressed -o dev.md https://developers.openai.com/codex/skills.md && sha256sum dev.md && wc -c < dev.md
ed6e324f747d47adf6f60ee1fca13ba469b3671f55f58c3a78f35947af6919d5
11035
```

The receipt's own HTML object distinguishes `curl_size_download` (61,806) from
`decoded_bytes` (417,112) (`SrcNewCodexSkills.json:57-68`); the markdown object has no
`decoded_bytes` field, so the wire size landed under `bytes`. [INFERENCE] the seat copied
`size_download` into `bytes`; the observable facts are the 3,970 wire size, the 11,035
decoded size, and the identical hash. The report table repeats it
(`SrcNewCodexSkills.md:24`, `:65`, `:138`). This is the M20/Q19 class: an auditor
comparing a re-fetch's `wc -c` (11,035) against the record (3,970) could infer drift that
the hash disproves. It does not touch any `SOURCES.md` cell — the row cites no byte count.

## F3 — the Gate's evidence path points at a receipt whose draft row has a different id (low)

The Gate's `record` for S013 is `.ufo/waves/round-47/build/SrcNewCodexSkills.md`
(tracked at `7ad7fad`: `git cat-file -e HEAD:.ufo/waves/round-47/build/SrcNewCodexSkills.md`
→ exit 0). That receipt opens "ADMIT S012" and drafts `| S012 | OpenAI …`
(`:40`); in the landed registry `S012` is the anthropics/skills row
(`corpus/SOURCES.md:25`) and the OpenAI row is `S013` (`:26`). The receipt does warn
about the collision ("ID caveat … the integrator must re-key one of them", §2), but the
artifact was not updated. The row body is id-independent and the Gate table lists the
correct ids, so this is a record-reading hazard, not a registry defect.

## Contract and census checks that held

Run from the clone at `7ad7fad` with the fleet script
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh` (fleet-root tool; the lane repo
has no `scripts/`):

```
$ sources-census.sh validate --file corpus/SOURCES.md --today 2026-10-21 --verbose
file	ok	…/corpus/SOURCES.md                                   exit 0
$ sources-census.sh census --file corpus/SOURCES.md --today 2026-10-21
file rows 15 · tier.A 14 · tier.C 1 · status.queued 8 · status.mined 6 · status.rejected 1 · missing 0   exit 0
$ sources-census.sh overdue --file corpus/SOURCES.md --today 2026-10-21 | grep S013
file	cadence	S013 recheck=90d opened=2026-10-21                exit 0 (not due)
```

The contract's own snippets agree: rows 15, malformed rows 0, duplicate ids none,
enum/tier violations none, mined `used-by` missing none. S013 is NF=13, `kind docs`,
`tier A`, `status queued`, `opened 2026-10-21`, `recheck 90d`, `used-by —` — all legal
values; `used-by —` is consistent with `queued` (the Gate table is a creation record, not
a citation; S014 is treated the same way). The row is append-only: the BASE→HEAD diff
adds S012–S015 and modifies no existing row (the four `-` lines in
`git diff — corpus/SOURCES.md` are prose: the header's access-evidence sentence and two
leads that became rows). Base had 11 rows, HEAD has 15, matching `LOG.md:2325`.
The 308 redirect is live (`HTTP/2 308 → learn.chatgpt.com/docs/build-skills`), and the
budget quote is 20 words, within the ≤25-word rule.

## What I did NOT check

- No Codex/ChatGPT run: the 2% budget, description shortening, and implicit-invocation
  gate are documentation claims only; I did not observe routing or `skills.max_context_tokens`
  in any client binary.
- Only S013. S014/S015 and the re-opened S001–S008 were not re-verified here.
- No lane-wide gate battery (surfaces/pins/checklist/corpus/fault-harness); this report
  exercises only the SOURCES census and the S013 row.
- No JS-rendered/DOM-mutated or localised variant of the page; server HTML and the
  advertised `.md` were the representations checked.
- No page history: no version control or body-level date is exposed, so "still states"
  is a two-point comparison (wave-1 receipt vs now, same sha256), not a full history.
- No credential material read, no session launched, no tool installed or upgraded
  (nothing needed installation).
