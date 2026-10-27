# Kb79R03FactoryRow — S228 Factory (`docs.factory.ai`), C2 source row

Round 79 / w1 / seat Kb79R03FactoryRow (leaf). Surface `factory`, registry id S228. Draft only: no
lane file outside `.ufo/waves/round-79/` was written, `corpus/SOURCES.md` and the C2 entry were not
touched, and no counter was run (nothing is scored on the C2 counter before the L1 freezes it).

## Behavior

Opened `https://docs.factory.ai/cli/configuration/skills` twice with
`curl -sSL -A 'Mozilla/5.0' --max-time 60` and the `.md` route twice, located the frontmatter
reference row for `allowed-tools` and the `## Declare intended tools` section, and produced the
registry row (11 cells), the entry table row, the Q53 byte proof, the Q70 cross-page check, the
reading, the injection sweep, the snapshot, its manifest pin and its fetch record.

## Gates and measurements (command, exit status, result)

All commands ran in `/fast/scratch/hyaku/kotoba-r79/Kb79R03FactoryRow` (TMPDIR set inside it, now
removed); each status is the command's own, captured as `cmd > out 2>&1; rc=$?`.

1. HTML route, two fetches: `curl -sSL -A 'Mozilla/5.0' --max-time 60 -o fN.out -w "%{http_code}
   %{size_download} %{url_effective}"` → `200 341235 https://docs.factory.com/harness/skills`,
   rc=0 both times; sha256 `81457fbf081aceaa5b90c50a8d7685450dc8801229f9a9202e40acde8fa201fa`
   identical in both fetches. Not committed (the `.md` text form is the cited snapshot); its
   hash is recorded in `S228.fetch.json` `note`.
2. `.md` route, two fetches: → `200 17567 https://docs.factory.com/harness/skills.md`, rc=0 both;
   sha256 `81409d890cb1b07f6a5a85db19610d4706866e5f4f668d4e26dd032002fed0c9` in both, `cmp`
   clean (byte-identical). Fetch window recorded as `2026-10-27T21:41:37Z` for both.
3. Header chain of the `.md` route (`curl -sSL -D - -o /dev/null`): `HTTP/2 308` →
   `https://docs.factory.com/cli/configuration/skills.md`, `HTTP/2 308` → `/harness/skills.md`,
   `HTTP/2 200`, `content-type: text/markdown; charset=utf-8`, `etag:
   "e322e6b7e64dcde5326acf10e5740f7e"`; **no** `Last-Modified`.
4. Snapshot installed: `sha256sum -c S228.manifest` → `S228-factory.md: OK`, rc=0; `wc -c -l` →
   17567 B / 354 lines.
5. Targeted greps on the snapshot (`grep -n -F`): `allowed-tools` 8 hits (lines 235, 254, 264,
   282, 285, 291, 298, 339), `experimental` 0 hits, `does not add tools` 1 hit (254),
   `does not grant new tools` 1 hit (339), `not a runtime sandbox` 1 hit (282), `sandbox` 2 hits.
6. Quote check: `printf '%s' "$Q" | wc -w` → 22; `grep -c -F "$Q" S228-factory.md` → 1 (exact
   byte substring of line 282, no whitespace collapse needed). Token occurrence counts with the
   round-73 counter's ASCII-word-boundary regex: `allowed-tools` 8, `Grep` 2, `metadata` 8.
7. Q70: two other surfaces fetched in scratch —
   `https://agentskills.io/specification.md` (HTTP 200, 7608 B, `grep -c -F` quote → **0**) and
   `https://code.claude.com/docs/en/skills.md` (HTTP 200, 117962 B, `grep -c -F` quote → **0**).
   Both pages do discuss the field (`allowed-tools` hits 4 and 21), so the zero is about the
   quote, not the topic.
8. Row shape: the registry row parsed to **11 cells** (python split on the markdown row) and the
   entry row to 5 cells (`awk -F'|'` NF=7); no `|` occurs inside any cell, and the quote contains
   none.

## Touched surfaces

- `.ufo/waves/round-79/snapshots/S228-factory.md` (new, 17567 B, the `.md` text view as fetched)
- `.ufo/waves/round-79/snapshots/S228.manifest` (new, one line: sha256 + basename)
- `.ufo/waves/round-79/snapshots/S228.fetch.json` (new: id, url, final_url, http, bytes, sha256,
  fetched_utc, ua, note)
- `.ufo/waves/round-79/build/Kb79R03FactoryRow.rows.md` (new: registry row, entry row, the entry
  `source:` line draft, Q53, Q70, reading, injection sweep, validation)
- `.ufo/waves/round-79/w1/Kb79R03FactoryRow.md` (this report)

No commit, no patch, no scratch clone (no working tree was needed), no counter invocation, no
`corpus/` write, no `MANIFEST.json`/`templates/`/`scripts/`/`.ufo/state/` write, no tool installed.

## Findings

**F1 — the assigned URL is a redirect to a different host and a different path (Q32 decision for
the L1).** `docs.factory.ai/cli/configuration/skills` answers `308` to
`docs.factory.com/cli/configuration/skills`, then `308` to `docs.factory.com/harness/skills`. The
frozen surface host is `docs.factory.ai`, so the row's `source` cell keeps the assigned URL (that is
what makes conjunct (b)'s host+path-prefix test pass) and the anchor cell plus `S228.fetch.json`
record the `final_url`. I did not invent a host change and did not edit the frozen table; if the L1
prefers the row to cite what was actually read, the surface's frozen host must be re-decided as
`docs.factory.com/harness/` and the two cannot both be true. The bytes are the same page across the
redirect (`text/markdown`, 17567 B, stable across two fetches). **Decision taken by L1
`KotobaR79` on 2026-10-27:** the frozen Factory host moves to `docs.factory.com` and the allowed-host
check binds a cited row to the recorded `final_url`. The draft therefore carries a second, canonical
11-cell row (source cell `https://docs.factory.com/harness/skills`) plus its matching entry `source:`
line at the end of `Kb79R03FactoryRow.rows.md` § Host amendment variant; quote, tokens, grant cell,
snapshot, pin and fetch record are unchanged.

**F2 — RESOLVED pre-data: the frozen factory grounding token is `metadata`.** (Original form of
the finding, kept for the record: the plan had asked the row's quote to carry `does not add tools`;
that token exists once, at line 254, inside the `allowed-tools` table row, behind `| No | None |`.
The shortest contiguous text-view span holding both `allowed-tools` and `does not add tools` is 26
words — over the cap — and would put `|` inside a cell, which the SOURCES contract and the entry's
5-column table forbid.) The L1's pre-data amendment (message from `KotobaR79`, 2026-10-27, in
`plans/round-79.md` § C2) replaces the token with `metadata`, which the submitted quote carries:
"`allowed-tools` records the tools the skill is designed to use. Droid stores it as skill metadata
and shows it in skill surfaces" — 22 words, pipe-free, snapshot line 282 byte columns 1-128,
`grep -c -F` = 1, word-bounded `metadata` hits in the snapshot 8. The amendment's own example
string "`allowed-tools` records the tools the skill is designed to use. It is metadata for review"
is **not** an exact substring of the page (`grep -c -F` = 0): it splices line 282's first sentence
onto line 254's "Declares the tools the skill is designed to use. It is metadata for review,
packaging, and UI display", so the submitted exact quote is used instead. No change to the entry
row's `grant` cell (`metadata-only`) or to the three page tokens is needed.

**F3 — the value form differs from the open specification.** Factory prints `allowed-tools` as a
YAML block sequence (`- Read`, `- Grep`, `- Glob`, lines 235-238, repeated 284-288), where the open
specification's form is a space-separated string. The page never states that the string form is
rejected, so this is a documented form, not a documented refusal — worth one line in the entry but
no claim beyond the page.

**F4 — the frozen label `metadata-only` is true of this page.** The page says of its own field: "It
is metadata for review, packaging, and UI display; it does not add tools or sandbox standard skill
invocation." (line 254), reinforced at 282 ("not a runtime sandbox"), 298 ("Do not rely on
`allowed-tools` as a security boundary"), 339 ("does not grant new tools"). No contradicting line
was found; no label change is proposed. The page never says a listed tool is the only one allowed,
never states inheritance for subagents, and never states what an unknown tool name does.

**F5 — freshness handle is the ETag only.** The response carries no `Last-Modified`, no build date,
no version or commit for the page itself (only the example frontmatter's `version: 1.0.0`), so the
row's revision is the snapshot sha256 and the ETag `e322e6b7e64dcde5326acf10e5740f7e` is the only
server-side change handle. `recheck: 90d` is set accordingly.

**F6 — prompt-injection sweep is clean.** The page's only imperative-looking prose is about its own
slash-command tokens (lines 309-313) and its code blocks (`mkdir -p .factory/skills/summarize-diff`
at line 21, YAML examples). Nothing in the page was executed or followed; no credentials, session
URLs or `op://` references appear in the page or in this draft.

## Out of scope / known limits

- Did not write `corpus/SOURCES.md`, `corpus/knowledge/allowed-tools-surfaces-round79.md`, `SKILL.md`,
  `PROVINCE.md`, `MANIFEST.sha256` or the C2 counter; the L1 stitches and pins.
- Did not run `check_allowed_tools.py` (not frozen yet) or score any surface; no claim data is scored
  by this seat.
- The quote was chosen from the paragraph at line 282, so the literal `does not add tools` token is
  not inside it (F2); if the L1's counter requires that token in the quote, this row is the one to
  adjust, not the page.
- One page read; the other five surfaces were not re-opened here except the two used for Q70.

VERDICT: S228 (Factory) is backed — the page's own words make `allowed-tools` review/UI metadata that grants and sandboxes nothing (label `metadata-only` true), the submitted 22-word pipe-free quote is an exact substring of line 282 carrying the amended grounding token `metadata`, and the only open item is F1, the assigned URL's 308 redirect to host `docs.factory.com/harness/` (a Q32 decision for the L1).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79R03FactoryRow.rows.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/snapshots/S228-factory.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/snapshots/S228.manifest, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/snapshots/S228.fetch.json, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/w1/Kb79R03FactoryRow.md
