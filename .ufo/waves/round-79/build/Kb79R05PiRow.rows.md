# Kb79R05PiRow — S230 `pi` row draft (C2, surface `pi`)

Seat Kb79R05PiRow, round 79 wave w1. Draft only: the L1 stitches into `corpus/SOURCES.md` and
`corpus/knowledge/allowed-tools-surfaces-round79.md`; this seat wrote neither. Snapshot
`.ufo/waves/round-79/snapshots/S230-pi.md` (4793 B, 93 lines), pin
`sha256 5b9805525b194474ef1fe5455a0917ef15ed7f710aa9bec2eee11879556469e5`, manifest
`.ufo/waves/round-79/snapshots/S230.manifest` (`sha256sum -c` → `S230-pi.md: OK`), fetch record
`.ufo/waves/round-79/snapshots/S230.fetch.json`.

Text view used below: the amended C2 rule (`plans/round-79.md` § C2, commits `d9d01c2` +
`60ba11f`) — for a Markdown snapshot delete every backtick byte, remove a leading unordered-list
marker by `(?m)^[ \t]{0,3}[*+\-][ \t]+`, then collapse whitespace. Measured on the snapshot:
`raw.replace('`','')` then the marker regex then `re.sub(r'\s+',' ', ...)`.

## (1) Registry row for corpus/SOURCES.md — 11 cells

| S230 | pi coding agent (pi-mono) — Skills — https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/skills.md | docs | B | what pi's own coding-agent documentation states about the `allowed-tools` frontmatter field: one frontmatter-table line that names the field and calls its value an Experimental pre-approved tool list, plus the page's deferral of every field definition to the Agent Skills specification (tier B: one harness vendor's documentation of its own product, not the open specification and no conformance claim; the page prints no value syntax and no enforcement statement, and no pi page or pi skill in the repository prints one either) | § Write portable frontmatter (heading at line 67), the frontmatter table row at line 78 whose first cell is the field name (backticked in the raw bytes; the amended Markdown text view deletes those backticks) and whose second cell reads "Experimental pre-approved tool list" (the located quote is those two cells joined by the table's cell delimiter, which this registry row cannot carry because the SOURCES contract forbids the vertical bar inside a cell; both cells are recorded verbatim here and are kept verbatim, separated by single spaces, in the entry's quote); served blob 19d2bf28910ce49caaaf4dde86d1e96330ca7b31 for main bb65e3e49710fbd14f10c7792d0eaa6e2b2c5923 (last commit touching this path 25cc5c7bf4cbc76b2e134c729eb8d57d521ed749, 2026-09-22; the page states no revision of its own, and the `badlogic/pi-mono` alias still serves HTTP 200 with no redirect while the GitHub API canonicalises the repository to `earendil-works/pi`); fetched 2026-10-27T21:41:14Z, HTTP 200, 4793 B, sha256 5b9805525b194474ef1fe5455a0917ef15ed7f710aa9bec2eee11879556469e5 | an author learns that pi lists the field and hands its meaning to the Agent Skills specification, so neither a value form (space-separated string or YAML list) nor an enforcement promise can be read off the pi page itself | mined | 2026-10-27 | 90d | corpus/knowledge/allowed-tools-surfaces-round79.md |

## (2) Entry table row (frozen header `| surface | source | page tokens | grant | located quote |`)

| pi | S230 | `allowed-tools`, `pre-approved`, `Experimental` | experimental | located quote "allowed-tools \| Experimental pre-approved tool list" |

Token roles: `allowed-tools` is the field-name token; `pre-approved` is nominated as the value-form
token (see the measured negative below — it is the page's only wording about the value);
`Experimental` is the grant-semantics token that grounds the frozen label `experimental`
(conjunct (f), which names `Experimental` as pi's grounding token).

Grounding in the amended text view, ASCII-word-bounded counts with the round-73 counter's regex
`(?<![A-Za-z0-9_-])TOK(?![A-Za-z0-9_-])`:

```
allowed-tools: 1
Experimental: 1
pre-approved: 1
pre-approved tool list: 1        (offered only as a longer alternative span)
quote: allowed-tools | Experimental pre-approved tool list   -> occurrences in view: 1, words: 6
```

Quote length 6 words (cap 5–25); it contains `allowed-tools` and the grounding token
`Experimental` (word-bounded, case-insensitive for the (f) check).

**Hazard 1 — the quote crosses a table-cell delimiter, and the amended view deletes backticks.**
The page names the field exactly once, inside a markdown table row
(`| \`allowed-tools\` | Experimental pre-approved tool list |`), so every 5–25-word quote
containing the field's name necessarily contains the row's vertical bar. Two consequences, both
measured on this file:

- The vertical bar cannot live inside a registry cell or a five-column entry cell; the row above
  writes it as the Markdown escape `\|`. Escape-aware split of the row (`(?<!\\)\|`) → 5 cells;
  naive `split('|')` → 6. Per the counter seat (`Kb79X01CounterBuild`, in-band), the C2 counter
  splits escape-aware, treats `\|` as cell content, and drops the backslash before the (d)
  comparison, so the row reads 5 cells and the quote is compared against the view's literal `|`.
  The same seat also retries a backticked quote cell once with every backtick byte deleted
  (documented READING), so formatting cannot sink a correct quote.
- The amended Markdown view deletes every backtick byte, so the quote is written **without**
  backticks and matches the view (`view_hits=1`), while the raw-bytes form with backticks no
  longer matches anything in the view (`raw_hits=0`). Compare the raw with the view in (3).

**Hazard 2 — pi prints no value form, and this is a measured negative, not an omission.** The
frozen token rule asks the `pi` row for a value-form token of the kind the spec page prints
(`space-separated`). No such token exists on this page or anywhere else in the repository that
this seat could reach:

```
44 files of packages/coding-agent/docs at main, fetched (curl -sSL --max-time 45, batch rc=0,
  0 files were 404 bodies, 480 K): grep -l -F 'allowed-tools' *  ->  skills.md only (1 of 44)
.pi/skills/{add-llm-provider,github-work,interactive-testing,release}.md, AGENTS.md,
  packages/coding-agent/README.md, README.md at main (7 fetches, all HTTP 200, 0 missing):
  grep -c -F 'allowed-tools' -> 0 in each
packages/coding-agent/schemas -> keybindings, models, settings, theme only; no skill schema
```

The single occurrence in the whole probe is `skills.md:78`, whose value cell is the words
"Experimental pre-approved tool list" — a description, not a syntax: no example value, no
`allowed-tools:` line with tools, no bracketed or space-separated list. The counter seat's
`token_role` classifies a non-key, non-grant bare word (`^[A-Za-z][A-Za-z0-9_.@/-]*$`) as the
value-form role, so `pre-approved` fills that role legally and no relaxation is needed; the seat
reports the row backed and verified as a permanent self-test arm (`.ufo/waves/round-79/build/selftest.txt`
line 70 `PASS S230 row shape: a pipe-bearing table-row quote with a bare word as the value form`,
honest world 6 of 6, 0 failures over 231 assertions in 80 worlds). The measured negative stays in
the entry as content: pi prints the field's value as words, never as a syntax, and nothing about
that is inferred from the spec page.

## (3) Q53 — the quote's source bytes

```
$ grep -n -F 'allowed-tools' .../.ufo/waves/round-79/snapshots/S230-pi.md
78:| `allowed-tools` | Experimental pre-approved tool list |
rc=0

$ sed -n '78p' .../S230-pi.md
| `allowed-tools` | Experimental pre-approved tool list |

$ sed -n '78p' .../S230-pi.md | od -c | sed -n '1,9p'
0000000   |       `   a   l   l   o   w   e   d   -   t   o   o   l   s
0000020   `       |       E   x   p   e   r   i   m   e   n   t   a   l
0000040       p   r   e   -   a   p   p   r   o   v   e   d       t   o
0000060   o   l       l   i   s   t       |  \n

$ sed -n '78p' .../S230-pi.md | grep -c '&'
0
```

What was shaped, exactly, for the quote as written in (2):

- **Dropped: exactly two bytes**, both `0x60` (backtick), the pair that bounds `allowed-tools` in
  the row's first cell — dropped by the amended Markdown view, not by this seat's choice.
- **Kept verbatim:** the row's own single spaces, the vertical bar between the two cells, and every
  letter of both cells. No code-span stripping, no case folding, no entity decoding (the line
  holds no `&`), no tag stripping (the snapshot is the raw `.md` response).
- **Joined:** nothing; the quote lies inside one line. **Outside the span:** the row's leading
  `| ` and its trailing ` |` plus the newline — the two delimiters that bound the row, which is
  why the quote starts at `allowed-tools` and ends at `list`.
- **Prefix check:** line 78 is the whole table row, so nothing of that line follows the quote.

The raw-format alternative, if a consumer compares against bytes rather than the view, is
`` `allowed-tools` | Experimental pre-approved tool list `` — one `grep -c -F` hit in the raw
snapshot, zero in the view.

## (4) Q70 — the quote is not another page's text

Measured against the five sibling C2 snapshots already written under
`.ufo/waves/round-79/snapshots/` (same day, same fetch recipe), searching both the raw bytes and
the amended text view:

```
$ Q='allowed-tools | Experimental pre-approved tool list'
S226-spec.md       7608 B  raw 0  view 0
S227-claude.md   117962 B  raw 0  view 0
S228-factory.md   17567 B  raw 0  view 0
S229-msaf.html   157339 B  raw 0  view 0
S231-vibe.md      77634 B  raw 0  view 0
S230-pi.md         4793 B  raw 0  view 1
```

Q70's second clause holds structurally: line 78 sits inside § Write portable frontmatter (heading
line 67), between the section's opening sentence (line 69) and its closing paragraph (line 81); it
is not the `# Skills` preamble (lines 1–7), and the token occurs once on the page
(`grep -c -F 'allowed-tools'` → 1), so the quote is not a banner, a subtitle or a repeated header.

## (5) What the page says and does not say; is `experimental` true of it

The page mentions the field once, in "Write portable frontmatter" (line 67), under the sentence
"The Agent Skills specification defines these fields:" (line 69). Its table row reads
"`allowed-tools` \| Experimental pre-approved tool list" (line 78). The page's own frame is the
deferral: "Pi implements the [Agent Skills specification]" (line 7) and "The Agent Skills
specification defines these fields" (line 69) — pi names the field as a spec field it recognises,
labels the value experimental and pre-approved, and says nothing more. What the page does **not**
say: it prints no value form (no space-separated string, no YAML list, no example — and the
44-page docs sweep plus the seven repo files probed in (2) found no second occurrence, so no pi
document prints one); it never states that pi enforces, filters, narrows or pre-approves tools
named there, nor that a tool outside the list is blocked; it states no scope (per-skill,
per-session, per-turn), no precedence against `disable-model-invocation` (the neighbouring row it
does explain at line 53), and no behaviour for an unknown tool name; and it claims nothing about
sandboxing. Its only Limits wording is generic: "Most invalid fields produce warnings rather than
stopping startup" (line 7) — a statement about invalid fields, not about `allowed-tools`
semantics. Its one security sentence is about project skills, not the field: "Project skills can
instruct the model to run scripts or modify files. Review unfamiliar skills and their supporting
files before granting project trust" (line 65). The frozen label `experimental` is **true of the
page**: the page's own word for the value is "Experimental" (line 78), the same label the open
specification uses, and no contradicting line was found — so no label change is proposed. For the
L1's cross-check: pi's line is the open specification's own wording carried into a vendor table,
so this surface confirms the spec's label and adds no client-side semantics.

## (6) Prompt-injection sweep

Sweep over the committed snapshot (93 lines), 2026-10-27:

```
$ grep -n -iE 'ignore (all|previous)|disregard|you are an? (ai|agent|assistant)|system prompt|curl |wget |run the following|execute the following|api[_-]?key|op://|secret|password|BEGIN [A-Z ]*PRIVATE' S230-pi.md
43:At startup, Pi scans configured skill locations and adds each skill's name, description, and path to the system prompt. It does not add the full instructions.
rc=0
```

The single hit is product prose describing pi's own loading behaviour ("adds ... to the system
prompt"), not an instruction. Nothing in the page addresses a fetcher, a model or a tool-runner;
the page contains two `text` blocks (a directory tree and a `/skill:pdf-tools extract report.pdf`
invocation) and two `markdown` blocks (a sample `SKILL.md`), none executed. No credential
material, no session or private URL, no `op://` reference appears in the page or in this draft.
Nothing in the page was followed as an instruction.
