# Kb79R03FactoryRow — S228 Factory row draft (C2, surface `factory`)

Seat: Kb79R03FactoryRow (round 79, wave w1). Draft only — the L1 stitches into
`corpus/SOURCES.md` and `corpus/knowledge/allowed-tools-surfaces-round79.md`; this seat wrote
neither. Snapshot: `.ufo/waves/round-79/snapshots/S228-factory.md` (354 lines, 17567 B),
pin `sha256 81409d890cb1b07f6a5a85db19610d4706866e5f4f668d4e26dd032002fed0c9`,
manifest `.ufo/waves/round-79/snapshots/S228.manifest`, fetch record
`.ufo/waves/round-79/snapshots/S228.fetch.json`.

## (1) Registry row for corpus/SOURCES.md — 11 cells

| S228 | Factory — Skills — https://docs.factory.ai/cli/configuration/skills | docs | B | what the page states about the `allowed-tools` frontmatter field: the value form it prints, the metadata-only semantics it claims, and the security boundary it refuses (tier B: one vendor's documentation of its own product, not the open specification and no conformance claim) | § Frontmatter reference, the `allowed-tools` row at snapshot `S228-factory.md:254`, and § Declare intended tools at snapshot `S228-factory.md:280-298`; the assigned URL redirects to https://docs.factory.com/harness/skills (`final_url` in S228.fetch.json); fetched as the `.md` route (the clean text form; two 308 hops, docs.factory.com/cli/configuration/skills.md then /harness/skills.md) and the response carries no Last-Modified, only ETag e322e6b7e64dcde5326acf10e5740f7e, so the revision is the snapshot sha256; quote "`allowed-tools` records the tools the skill is designed to use. Droid stores it as skill metadata and shows it in skill surfaces" (22 words); fetched 2026-10-27T21:41:37Z, HTTP 200, 17567 B, sha256 81409d890cb1b07f6a5a85db19610d4706866e5f4f668d4e26dd032002fed0c9 | Factory calls `allowed-tools` review, packaging and UI metadata that does not add tools or sandbox standard skill invocation, prints it as a YAML block sequence rather than a space-separated string, and tells authors not to rely on it as a security boundary | mined | 2026-10-27 | 90d | corpus/knowledge/allowed-tools-surfaces-round79.md |

Cell count check (contract census rule, `NF=13` for 11 cells): the row above is one line; see
§ Validation for the awk output.

Entry-side `source:` line the L1 can use (url kept at the assigned host so the counter's
entry↔row URL binding holds; the redirect is recorded in the row's anchor and in fetch.json).
This is the pre-amendment shape: after the L1's 2026-10-27 host decision, paste the canonical-URL
row and source line from § Host amendment variant instead.

```
source: S228 — Factory — Skills — https://docs.factory.ai/cli/configuration/skills — § Frontmatter reference and § Declare intended tools — located quote "`allowed-tools` records the tools the skill is designed to use. Droid stores it as skill metadata and shows it in skill surfaces" (snapshot `S228-factory.md:282`)
```

## (2) Entry table row (frozen header `| surface | source | page tokens | grant | located quote |`)

| Factory | S228 | `allowed-tools`, `Grep`, `metadata` | metadata-only | located quote "`allowed-tools` records the tools the skill is designed to use. Droid stores it as skill metadata and shows it in skill surfaces" |

Token grounding in the snapshot's text view (ASCII-word-bounded occurrence counts, same regex the
round-73 counter documents):

```
$ for t in allowed-tools Grep metadata; do printf '%s: ' "$t"; grep -oE "(^|[^[:alnum:]_-])$t([^[:alnum:]_-]|$)" S228-factory.md | wc -l; done
allowed-tools: 8
Grep: 2
metadata: 8
```

`Grep` is the value-form token: the page prints `allowed-tools:` followed by a YAML block
sequence whose items are `Read`, `Grep`, `Glob` (`S228-factory.md:235-238`, repeated at
`:284-288`). `metadata` is the grant-semantics token — and, per the pre-data amendment in
`plans/round-79.md` § C2 (message from L1 `KotobaR79`, 2026-10-27), the frozen factory
quote-grounding token: the submitted quote contains it ("Droid stores it as skill metadata and
shows it in skill surfaces", word-bounded `metadata` hits in the snapshot: 8). The amendment's
example string "`allowed-tools` records the tools the skill is designed to use. It is metadata for
review" is **not** an exact substring (0 hits): it splices line 282's first sentence onto line 254's
"Declares the tools the skill is designed to use. It is metadata for review, packaging, and UI
display". The submitted quote is exact instead — 22 words, line 282, byte columns 1-128 of 255,
`grep -c -F` = 1.

## (3) Q53 — the quote's source bytes

```
$ grep -n -F 'records the tools the skill is designed to use' S228-factory.md
282:`allowed-tools` records the tools the skill is designed to use. Droid stores it as skill metadata and shows it in skill surfaces, but standard skill invocation is not a runtime sandbox. A skill cannot add tools that are unavailable in the current session.

$ sed -n '282p' S228-factory.md
`allowed-tools` records the tools the skill is designed to use. Droid stores it as skill metadata and shows it in skill surfaces, but standard skill invocation is not a runtime sandbox. A skill cannot add tools that are unavailable in the current session.

$ Q='`allowed-tools` records the tools the skill is designed to use. Droid stores it as skill metadata and shows it in skill surfaces'
$ printf '%s' "$Q" | wc -w
22
$ grep -c -F "$Q" S228-factory.md
1
```

What was shaped: **nothing**. The quote is an exact byte substring of line 282 of the committed
snapshot — `grep -c -F` finds it once, with no whitespace collapse needed (the line carries single
spaces only). No tags were stripped (the snapshot is the `.md` route, not HTML, and this line holds
no MDX component), no HTML entities were decoded, no bytes were dropped from inside the span, and
no bytes were joined. The only thing not carried is what follows the span in the same sentence:
`, but standard skill invocation is not a runtime sandbox. A skill cannot add tools that are
unavailable in the current session.` — i.e. the quote is a prefix truncation at a sentence
boundary, not a reshaped string.

## (4) Q70 — the quote is not another page's text

Two other surfaces of the set were fetched into scratch on 2026-10-27 and grepped for the exact
22-word string (`grep -c -F`, literal, no case folding):

```
https://agentskills.io/specification.md            -> HTTP 200, 7608 B,   grep -c -F quote: 0
https://code.claude.com/docs/en/skills.md          -> HTTP 200, 117962 B, grep -c -F quote: 0
```

Both pages discuss the field (4 and 21 `allowed-tools` hits respectively), so the zero is a
statement about this quote, not about the topic. The quote names Droid and the skill-surface
display rule, which only the Factory page states.

## (5) What the page says, what it does not, and whether `metadata-only` is true of it

Factory documents `allowed-tools` in two places. The frontmatter reference row calls it optional,
with a description that is the whole of the page's semantic claim: "Declares the tools the skill is
designed to use. It is metadata for review, packaging, and UI display; it does not add tools or
sandbox standard skill invocation." (`S228-factory.md:254`). Its own section, `## Declare intended
tools` (`:280-298`), repeats that "Droid stores it as skill metadata and shows it in skill
surfaces, but standard skill invocation is not a runtime sandbox. A skill cannot add tools that
are unavailable in the current session." (`:282`), gives the review use cases (read-only audits,
no-edit workflows, no-external-system workflows, narrow team-shared capability sets, `:291-296`),
and closes with the enforcement path: "Do not rely on `allowed-tools` as a security boundary for
skills. To enforce tool access, use a custom droid with a tool policy or run the workflow in a
restricted subagent." (`:298`). A troubleshooting item repeats the negative — "`allowed-tools`
does not grant new tools." (`:339`) — and the page marks the older `tools` key as deprecated
metadata (`:259`). The value form the page prints is a YAML block sequence (`:235-238`,
`:284-288`), not the open specification's space-separated string.

What the page does **not** say: it never states that a tool outside the list is blocked, never
states a precedence or inheritance rule for a subagent or for a project-over-user scope, never
states what happens to an unrecognised tool name, and never uses the word "experimental" (0 hits).
Its Limits wording is the pair of negatives above — no sandbox, no grant — plus "not a security
boundary".

The frozen label `metadata-only` is **true of this page**: the page's own words are that the field
"is metadata for review, packaging, and UI display; it does not add tools or sandbox standard skill
invocation". No contradicting line was found, so no label change is proposed.

RESOLVED by the pre-data amendment (`plans/round-79.md` § C2, L1 `KotobaR79`, 2026-10-27): the
frozen factory quote-grounding token is now `metadata`, which the submitted quote carries — see §(2).
The earlier shape conflict is kept below as the record of why the token moved. The old token
`does not add tools` exists in the snapshot once, at `:254`, but it is
separated from `allowed-tools` by the two intervening table cells (`| No | None |`) plus the row's
first sentence. The shortest contiguous span of the text view holding **both** `allowed-tools` and
`does not add tools` is 26 words (24 without counting the three pipe cells) — past the 5–25 word
cap — and it would also put `|` characters in a table cell, which both the SOURCES contract ("No
`|` inside any cell") and the entry's 5-column table forbid. The quote submitted therefore carries
`allowed-tools` and the metadata semantics (`Droid stores it as skill metadata and shows it in
skill surfaces`), and the literal token `does not add tools` is one line away at `:254` for a
counter that checks the snapshot rather than the quote span. Exact candidate rejected for length:
"`allowed-tools` | No | None | Declares the tools the skill is designed to use. It is metadata for
review, packaging, and UI display; it does not add tools" (26 words, 29 shape-tokens with the pipe
cells).

## (6) Prompt-injection sweep

The page is product documentation and carries no instruction addressed to a fetcher or an agent.
Sweep over the committed snapshot for `ignore (all|previous)`, `disregard`, `you are an? (ai|agent|
assistant)`, `system prompt`, `curl `, `run the following`, `execute the following`, `api[_-]?key`,
`token`: the only hits are the word "token" in the slash-command prose at `:309-313` ("Droid sends
your prompt exactly as typed…", "Recognized skill tokens are highlighted…", "A token activates a
skill only when it is a whole word"), which describes the product's own invocation parsing. The
page contains one bash code block (`mkdir -p .factory/skills/summarize-diff`, `:21`) and one YAML
block; neither was executed. No credential material, session URL or `op://` reference appears in
the page or in this draft. Nothing in the page was followed as an instruction.

## Validation

```
$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {print NF}' <row file>   # 13 = 11 cells
13
$ sha256sum -c S228.manifest
S228-factory.md: OK
```

## Host amendment variant (L1 decision 2026-10-27: frozen host moves to `docs.factory.com`)

Same 11 cells, same quote, source cell now cites the canonical final URL so a host+path-prefix
check binds the row to what was actually fetched. Snapshot provenance: the HTML route ends at
`https://docs.factory.com/harness/skills` (HTTP 200, 341235 B, sha256 `81457fbf…01fa`), and the
committed snapshot is that page's `.md` route `https://docs.factory.com/harness/skills.md`
(`text/markdown`, HTTP 200, 17567 B, sha256 `81409d89…0fed0c9`, two fetches byte-identical).

```
| S228 | Factory — Skills — https://docs.factory.com/harness/skills | docs | B | what the page states about the `allowed-tools` frontmatter field: the value form it prints, the metadata-only semantics it claims, and the security boundary it refuses (tier B: one vendor's documentation of its own product, not the open specification and no conformance claim) | § Frontmatter reference, the `allowed-tools` row at snapshot `S228-factory.md:254`, and § Declare intended tools at snapshot `S228-factory.md:280-298`; opened at the canonical final URL, where the assigned https://docs.factory.ai/cli/configuration/skills answers 308 twice; the response carries no Last-Modified, only ETag e322e6b7e64dcde5326acf10e5740f7e, so the revision is the snapshot sha256; quote "`allowed-tools` records the tools the skill is designed to use. Droid stores it as skill metadata and shows it in skill surfaces" (22 words); fetched 2026-10-27T21:41:37Z, HTTP 200, 17567 B, sha256 81409d890cb1b07f6a5a85db19610d4706866e5f4f668d4e26dd032002fed0c9 | Factory calls `allowed-tools` review, packaging and UI metadata that does not add tools or sandbox standard skill invocation, prints it as a YAML block sequence rather than a space-separated string, and tells authors not to rely on it as a security boundary | mined | 2026-10-27 | 90d | corpus/knowledge/allowed-tools-surfaces-round79.md |
```

Matching entry-side `source:` line for this variant:

```
source: S228 — Factory — Skills — https://docs.factory.com/harness/skills — § Frontmatter reference and § Declare intended tools — located quote "`allowed-tools` records the tools the skill is designed to use. Droid stores it as skill metadata and shows it in skill surfaces" (snapshot `S228-factory.md:282`)
```

