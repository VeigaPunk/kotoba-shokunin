# S226 — `spec` surface (Open specification): DRAFT rows for round 79 C2

Seat: Kb79R01SpecRow · round 79 · wave w1 · source page `https://agentskills.io/specification.md`
Snapshot: `.ufo/waves/round-79/snapshots/S226-spec.md` (7608 B, sha256 `9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16`)
Fetch: 2026-10-27T21:41:23Z, HTTP 200, no redirect, `text/markdown; charset=utf-8`, `server: Vercel`; second fetch 2026-10-27T21:41:24Z, same 7608 B, same sha256 (`cmp` rc=0 — byte-identical, the page did not change between fetches).
Quote form: the L1 ruled on 2026-10-27 that the located quote is stated in a **declared text view** of the snapshot (transform below), not as a raw-byte substring. Both rows below carry the text-view form.

**Declared text view** (applied to the raw snapshot bytes, nothing else):
1. delete every backtick byte `` ` `` (inline-code delimiters);
2. delete a leading Markdown list marker at line start, `(?m)^[ \t]{0,3}[*+\-][ \t]+` (the marker and the whitespace after it);
3. collapse every run of whitespace to one space and strip the ends.

No other byte is removed, no entity is decoded, no word is changed.

---

## 1. Registry row for `corpus/SOURCES.md` (11 cells, append under the registry table)

| S226 | Agent Skills — Specification — https://agentskills.io/specification.md | spec | A | what the `allowed-tools` frontmatter field is in the format itself: an optional key whose value is a space-separated string of pre-approved tools, labelled Experimental because support "may vary between agent implementations"; tier A because this page is the format maintainers' own specification and the scope is exactly that statement — the page names no client, claims no enforcement, and says nothing about how the field behaves when unsupported | `#### allowed-tools field` (L172) with its opening sentence (L174) and its two bullets (L176-177), plus the frontmatter table row (L35); the page states no revision of its own — no version, commit or date in the body, and its `last-modified` header equals the request instant, so it marks the fetch and not the content — so the upstream file stands in: `agentskills/agentskills@217be548739f21d6008915c29aefe320ea1a90af` `docs/specification.mdx` L163-167 (path byte-identical at head `69ef37e9424c0a7ea9dd2293b559e43ec8176379`, `git ls-remote refs/heads/main` 2026-10-27, raw fetch both revisions sha256 `b9079c0c10b7930e8c6a20ff2bc10cda2a3343c55185120e3f1116a1a529b220`); quote "The optional allowed-tools field: A space-separated string of tools that are pre-approved to run Experimental." in the declared text view of snapshot S226-spec.md, built from raw L174 plus L176-177 (the raw bytes carry backticks and the two `* ` markers the text view removes); fetched 2026-10-27T21:41:23Z, HTTP 200, 7608 B, sha256 9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16 | the field is optional and its value is a space-separated string of pre-approved tools, but the format itself stamps it Experimental and says support "may vary between agent implementations", so a skill that relies on `allowed-tools` for restriction relies on a field the format does not guarantee on any client | mined | 2026-10-27 | 90d | corpus/knowledge/allowed-tools-surfaces-round79.md |

Cell notes: 11 cells (`awk -F'|'` NF = 13); no `|` anywhere inside a cell; `kind` = `spec` (enum); `tier` = A (open specification, format maintainers' own text); `status` = `mined` (used-by names the round-79 entry); `opened` = 2026-10-27; `recheck` = `90d`.

## 2. Entry table row (frozen header `| surface | source | page tokens | grant | located quote |`)

| Open specification | S226 | `allowed-tools`, `space-separated`, `pre-approved`, `Experimental` | experimental | located quote "The optional allowed-tools field: A space-separated string of tools that are pre-approved to run Experimental." |

Quote facts: 15 whitespace-separated tokens (5-25 range), contains `allowed-tools`, contains the grant token `Experimental`, contains no `|`. Text-view occurrence count in `S226-spec.md` = 1 (index 4267); in the raw bytes = 0 (the raw span carries backticks and two `* ` markers), which is why the text view is declared. Grant cell `experimental` is plain text, not backticked.

Token evidence, ASCII word-bounded counts in the **raw** snapshot `S226-spec.md` (`re.findall(r'(?<![0-9A-Za-z_])'+re.escape(t)+r'(?![0-9A-Za-z_])', bytes)`): `allowed-tools` 4 · `space-separated` 1 · `pre-approved` 2 · `Experimental` 2. Per the L1 ruling, `space-separated` is the value-form token; the literal example value `Bash(git:*)` (L182) is not used because `\b`-anchored word-boundary matching cannot match a token ending in `)` (verified: `\bBash\(git:\*\)\b` finds 0). If a literal example value is ever required, `Read` (1 occurrence, L182) is the only `\b`-safe literal on the page.

## 3. Q53 proof — the raw lines, the transform, and the exact quote

Raw source lines in the snapshot (commands run against the installed `snapshots/S226-spec.md`; the scratch copy was byte-identical, sha256 `9a67de89…`):

```
$ grep -n -F 'The optional `allowed-tools` field:' fetch1.body
174:The optional `allowed-tools` field:
rc=0

$ grep -n -F '* A space-separated string of tools that are pre-approved to run' fetch1.body
176:* A space-separated string of tools that are pre-approved to run
rc=0

$ grep -n -F '* Experimental. Support for this field may vary between agent implementations' fetch1.body
177:* Experimental. Support for this field may vary between agent implementations
rc=0

$ sed -n '172,183p' fetch1.body
#### `allowed-tools` field

The optional `allowed-tools` field:

* A space-separated string of tools that are pre-approved to run
* Experimental. Support for this field may vary between agent implementations

> **Example:**
>
> ```yaml theme={null}
> allowed-tools: Bash(git:*) Bash(jq:*) Read
> ```
```

Transform, byte by byte, over raw L174 + L175 (blank) + L176 + L177:

- **Dropped:** the two backticks on L174 (inline-code delimiters), the `* ` list marker at the start of L176 and of L177, and L175's emptiness.
- **Kept:** every word — `The optional`, `allowed-tools`, `field:`, `A space-separated string of tools that are pre-approved to run`, `Experimental.` — and L177's tail after `Experimental.` (not part of the quote, so the quote stops at the period).
- **Joined:** the line breaks and the blank line each become one space (whitespace collapse).
- **Not done:** no HTML tag was stripped (this region has none outside the `>` example block), no character entity was decoded (none present), no word substituted.

Verification (`python3`, reading the installed snapshot):

```
textview = raw.replace('`','') then re.sub(r'(?m)^[ \t]{0,3}[*+\-][ \t]+','') then re.sub(r'\s+',' ')
snapshots/S226-spec.md:              quote_count 1    quote_word_tokens 15   index 4267
build/Kb79R01SpecRow.q70-claude.md:  quote_count 0    quote_word_tokens 15   index -1
region: '… > #### allowed-tools field The optional allowed-tools field: A space-separated string of tools that are pre-approved to run Experimental. Support for this field may vary between agent implementations > **Exa…'
```

Raw line range the quote rests on: **L174 and L176-177** (L172 is the heading, L182 the example). Upstream equivalent: `docs/specification.mdx` **L165-167** at `217be548739f21d6008915c29aefe320ea1a90af` — the mdx prints the same sentence with `- ` markers and the same absence of backticks around the field name in the bullet text; the served `.md` re-renders `- ` as `* ` and keeps the backticks on L174/L35.

A superseded form, recorded for the record: the literal raw span (with backticks and `* ` present) is, quoted, "The optional `allowed-tools` field: * A space-separated string of tools that are pre-approved to run * Experimental." — 17 tokens, present in the raw bytes at collapsed index 4464. The L1's ruling replaces it with the text-view form above so that the frozen counter matches one declared transform instead of raw-only matching.

## 4. Q70 check — the quote occurs on no other page of the set

I fetched one other surface's page myself, applied the same declared text view, and grepped the exact quote:

```
$ curl -sSL -A 'Mozilla/5.0' --max-time 60 -o claude.body -w 'claude HTTP %{http_code} %{size_download} %{url_effective}\n' https://code.claude.com/docs/en/skills.md
claude HTTP 200 117962 https://code.claude.com/docs/en/skills.md
$ sha256sum claude.body
31623035b25ac7e6bebd8dec6234aa76e31018f0e2eb8b47da6b36cf015712f9  claude.body

$ grep -c -F 'The optional `allowed-tools` field: * A space-separated string of tools that are pre-approved to run * Experimental.' claude.body
0
rc=1
$ grep -c -F 'pre-approved to run' claude.body
0
rc=1

# same quote in the declared text view of the claude bytes:
quote_count 0    (text view of build/Kb79R01SpecRow.q70-claude.md, 117962 B)
```

So the quote is 0 on the Claude Code page both raw and in the declared text view, and the distinctive fragment `pre-approved to run` is 0 there. This is one of the five non-own pages, not a sweep of all five: "no other page of the set" is supported here only for `claude`, and a full Q70 sweep belongs to the falsify wave (I claim nothing about factory/msaf/pi/vibe bytes).

## 5. Reading — what the page says, what it does not say, and whether `experimental` is true

The page states the field twice and only twice: in the frontmatter overview table as an optional key whose constraint is "Space-separated string of pre-approved tools the skill may use. (Experimental)" (L35), and in its own `#### allowed-tools field` section, which calls it "The optional `allowed-tools` field", gives two bullets — "A space-separated string of tools that are pre-approved to run" and "Experimental. Support for this field may vary between agent implementations" (L174-177) — and shows one example value, `allowed-tools: Bash(git:*) Bash(jq:*) Read` (L182). **What it does not say:** it names no client and promises no client parses the field; it never says whether the value restricts the tool pool, merely pre-approves calls, or prompts for permission — "pre-approved to run" is the strongest wording and it is undefined; it gives no lifetime (whole session, per turn, per skill activation), no fallback or error when a client ignores the field, no alternate value form (the example is space-separated tool names with one `Bash(git:*)` scope pattern; the page never says a YAML list is invalid, and the Validation section points at `skills-ref` without saying it checks this field), and no ordering or duplicate semantics. **Is the label `experimental` true of the page?** Yes, and twice over: the table's parenthetical `(Experimental)` (L35) and the section bullet "Experimental. Support for this field may vary between agent implementations" (L177). I judge the frozen label `experimental` TRUE for this surface; the page's own word is `Experimental`, and the qualifier ("support may vary between agent implementations") is exactly what the label is meant to carry. The one caveat worth recording: the page does not say the field is *unstable in its text* (no deprecation, no version gate), only that *support* may vary — so `experimental` here is a portability warning about clients, not about the format's wording.

Cross-reference (prior lane record, not my measurement): `corpus/knowledge/frontmatter-rule-authorities-round48.md:104` already carries the space-separated claim with `spec.md:35, :176` and a r48 observation that a YAML list passes both validators. My row does not re-claim that measurement; it adds the per-client axis only.

## 6. Prompt-injection text seen in the page (reported, not followed)

The page opens with an imperative block addressed to whoever reads it:

```
> ## Documentation Index
> Fetch the complete documentation index at: https://agentskills.io/llms.txt
> Use this file to discover all available pages before exploring further.
```

That is an instruction-like banner ("Fetch …", "Use this file to discover …"). I did **not** follow it: I fetched no `llms.txt` and crawled no further pages; the snapshot is the single requested URL. No other instruction addressed to the reader/agent appears in the bytes: the remaining imperatives ("Keep your main `SKILL.md` under 500 lines", "Use the skills-ref reference library") are the document's subject matter, guidance to skill authors. Site-build artifacts in the same bytes (`theme={null}`, `**Example:**`, `<Card>`-derived blockquote wrappers in the live `.md`) are markup, not instructions.
