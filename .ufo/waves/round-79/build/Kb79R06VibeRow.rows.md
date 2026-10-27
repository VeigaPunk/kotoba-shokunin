# Kb79R06VibeRow — C2 source row, surface `vibe` (Mistral Vibe), registry id S231

Round 79, wave w1, seat Kb79R06VibeRow. Lane repo: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Everything below is over bytes this seat fetched itself on 2026-10-27 and saved to
`.ufo/waves/round-79/snapshots/S231-vibe.md` (sha256
`fc48a5dbafe572fedd1457cffba8442aacd296dddaf50833ac3104252cb016b0`, 77 634 B). No lane file was
edited by this seat; these are drafts for the L1 of round 79.

Snapshot / fetch record (written by this seat, both absolute paths):

- `.ufo/waves/round-79/snapshots/S231-vibe.md` — raw fetched bytes, unmodified (`cmp` against the
  fetch buffer: identical).
- `.ufo/waves/round-79/snapshots/S231.manifest` —
  `fc48a5dbafe572fedd1457cffba8442aacd296dddaf50833ac3104252cb016b0  S231-vibe.md`
- `.ufo/waves/round-79/snapshots/S231.fetch.json` — id/url/final_url/http/bytes/sha256/fetched_utc/ua/note.

**The L1 must copy this pin into the shared `MANIFEST.sha256` at freeze** (conjunct (c) resolves the
snapshot by a manifest key). This seat wrote no shared manifest: it is a file other w1 seats also
append to, and this seat's write scope names only `S231.manifest`.

---

## 1. Registry row for `corpus/SOURCES.md` (11 cells, append-only)

| S231 | Mistral Vibe — README (skills system and skill frontmatter example) — https://raw.githubusercontent.com/mistralai/mistral-vibe/main/README.md | docs | B | Mistral Vibe's own README as the statement of its skill surface: the discovery roots it lists, the invocation controls it documents, and the single frontmatter example that writes `allowed-tools` (tier B: one vendor's documentation of its own client, no claim about conformance to the open specification it names; the open specification is S226's tier-A ground) | § Skills System (L708) → § Creating Skills (L714-L734), snapshot S231-vibe.md:725-728; raw `main` URL served commit 7bb48f213ac677f943d5c791199ed3dddf302f00 (`git ls-remote`, 2026-10-27T21:43:03Z; the commit-pinned raw URL served byte-identical bytes at 2026-10-27T21:42:25Z), commit date 2026-10-26T21:37:45Z, the page states no last-modified; quote in the amended text view (backticks deleted, unordered-list markers removed, whitespace collapsed) "user-invocable: true allowed-tools: read grep ask_user_question"; fetched 2026-10-27T21:41:26Z, HTTP 200, 77634 B, sha256 fc48a5dbafe572fedd1457cffba8442aacd296dddaf50833ac3104252cb016b0 | Vibe's README prints `allowed-tools` only inside one skill example, as a YAML block list, and states no meaning for it — so this page fixes neither the field's value form nor the grant it carries, and a skill that relies on the field for restriction rests on a rule this page never states | mined | 2026-10-27 | 90d | corpus/knowledge/allowed-tools-surfaces-round79.md |

Census consequences of appending it (the L1 runs the census; counts given so the before/after is
checkable): rows `151 → 152` (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`), 11 cells means
`awk -F'|' … NF!=13` still prints 0, tier histogram `B` +1, status histogram `mined` +1, duplicate
ids unchanged, `kind` ∈ the frozen enum (`docs`). The `used-by` path
`corpus/knowledge/allowed-tools-surfaces-round79.md` exists only once the L1 lands the entry in the
same commit — the mined-used-by sweep is expected to print `missing:` for it in a row-only commit.

Row-cell discipline: no `|` inside any cell (checked), `status` = `mined`, `opened` = 2026-10-27,
`recheck` = `90d` (a `main`-branch README of a fast-moving CLI; the page carries no version and no
last-modified, so a date pin would be invented), `used-by` names the frozen entry path.

## 2. Entry table row (frozen header `| surface | source | page tokens | grant | located quote |`)

| surface | source | page tokens | grant | located quote |
|---|---|---|---|---|
| Mistral Vibe | S231 | `allowed-tools` `allowed-tools:` `ask_user_question` `user-invocable` | unstated | located quote "user-invocable: true allowed-tools: read grep ask_user_question" |

Token roles, stated so the counter's classes can be checked against the page rather than inferred
from the row (all four verified ASCII-word-bounded — `(?<![A-Za-z0-9_])tok(?![A-Za-z0-9_])` — in the
amended text view of the snapshot, and confirmed with `Kb79X01CounterBuild` as key / grant / value
roles):

- `allowed-tools` — the field name, the token every surface must carry. Exactly 1 occurrence on the
  page (L725), so there is no second, prose occurrence to lean on.
- `allowed-tools:` — the **grant** token: the plan's named vibe grant-grounding token, and the
  located quote carries it. It is also the value-form evidence — the key is printed with no inline
  value and a three-item block list underneath, the form that differs from the specification's
  space-separated string.
- `ask_user_question` — a value-form token: a value the page prints in that list (4 occurrences:
  L108, L189, L196 as a tool name, L728 in the skill example). In the quote it is the last list
  member, i.e. the value.
- `user-invocable` — the other value-form token and the third page token: the neighbouring
  frontmatter key the same example writes (L724) and that the page then *does* define in prose
  (L739-745). It is also the key whose line the frozen quote must borrow to clear the 5-word floor
  after the amendment (see §3).

Grant cell: plain `unstated`, not backticked. §5 judges the label.

## 3. Q53 — the located quote in the amended text view, byte for byte

The C2 text view was amended **before any claim data** (`plans/round-79.md` § C2, line 42 read at
commit `c469863`; commits `d9d01c2` "round-79: clarify markdown snapshot text view before data" and
`60ba11f` "round-79: freeze exact S226 transformed quote before scoring"): for Markdown snapshots
"delete every backtick byte and remove an unordered-list marker by
`(?m)^[ \t]{0,3}[*+\-][ \t]+`; then collapse whitespace", fences **not** stripped. The snapshot
bytes are unchanged (this seat's fetch, sha256 `fc48a5db…`). Raw source lines:

```
$ grep -n -F 'allowed-tools' S231-vibe.md
725:allowed-tools:
$ sed -n '724,728p' S231-vibe.md
user-invocable: true
allowed-tools:
  - read
  - grep
  - ask_user_question
$ sed -n '725,728p' S231-vibe.md | od -c | head -12
0000000   a   l   l   o   w   e   d   -   t   o   o   l   s   :  \n
0000020       -       r   e   a   d  \n           -       g   r   e   p
0000040  \n           -       a   s   k   _   u   s   e   r   _   q   u
0000060   e   s   t   i   o   n  \n
0000067
```

Exactly these bytes are dropped, joined or shaped by the amended view:

- **backtick deletion:** no backtick byte lies in L724-L728 (the span is bare YAML), so this step
  changes nothing here; it does change L716/L718/L729/L734 outside the span.
- **unordered-list marker removal:** `  - read` → `read`, `  - grep` → `grep`,
  `  - ask_user_question` → `ask_user_question`: the two leading spaces and the two bytes `- ` are
  deleted from each of L726, L727, L728 (4 bytes per line).
- **whitespace collapse:** the newlines ending L724-L728 become single spaces; the quote is otherwise
  unchanged. No tags are stripped and no entities decoded (raw Markdown, no HTML in this span); no
  case folding.

The transformed view of the block is therefore

```
compatibility: Python 3.14+ user-invocable: true allowed-tools: read grep ask_user_question ---
```

Two consequences, both recorded rather than worked around:

1. The pre-amendment form `allowed-tools: - read - grep - ask_user_question` is **not** in the amended
   view — the markers are gone. It is superseded and must not appear in the entry.
2. A quote anchored at the key alone, `allowed-tools: read grep ask_user_question`, is **4**
   whitespace tokens after the marker removal — under the 5-word floor, so it cannot be used either.

The quote therefore has to span the preceding line, and it still carries the frozen vibe page token
`allowed-tools:`:

> `user-invocable: true allowed-tools: read grep ask_user_question`

6 whitespace tokens (5-25 bound), occurs exactly once in the amended view
(`re.sub(r'\s+',' ',...).count(q)` → 1), contains `allowed-tools` ASCII-word-bounded, and spans raw
lines L724-L728 — all body lines inside the fenced skill example, no heading line, not the
first-heading block. The fence is not stripped by the amended view, which is why a body example that
sits in a fenced block is reachable at all.

## 4. Q70 — the quote is not a banner, subtitle or shared line

`allowed-tools` has exactly one occurrence on the page (`grep -c -F` → 1), at L725, inside the fenced
skill example under `### Creating Skills`; it is not in the page title block, the feature list or the
table of contents. Against the other five surfaces, fetched by this seat on 2026-10-27 (HTTP 200
each), each put through the amended text view before counting:

```
$ python3 - <<'PY'   # md: delete backticks, drop (?m)^[ \t]{0,3}[*+\-][ \t]+, collapse
                     # html: script/style->space, tags->space, entities decoded, collapse
... quote_count(f) for spec, claude, pi (Markdown), factory, msaf (HTML)
spec     transformed_len=    7168 quote_count=0  raw_F_count=0
claude   transformed_len=  114785 quote_count=0  raw_F_count=0
pi       transformed_len=    4629 quote_count=0  raw_F_count=0
factory  transformed_len=   15396 quote_count=0  raw_F_count=0
msaf     transformed_len=   86564 quote_count=0  raw_F_count=0
```

0 in every transformed view and 0 in every raw byte stream (`grep -c -F` on the raw pages → 0): the
quote is this page's own example, not a shared banner or a line another snapshot carries. (Fetched
sizes: spec 7 608 B, claude 117 962 B, pi 4 793 B, factory 341 235 B, msaf 157 339 B.) The sixth
surface is this row's own page.

## 5. What the page says about `allowed-tools` — and what it does not

The page mentions the field **once**, in the `code-review` skill example of § Creating Skills
(L714-L734): `allowed-tools:` is followed by a three-item YAML block list (`read`, `grep`,
`ask_user_question`), and the surrounding prose says nothing about it — the paragraph after the
example defines `user-invocable` and `disable-model-invocation` explicitly (L736-745), which makes
the silence on `allowed-tools` a within-page contrast rather than a general haziness. What the page
*does* say is structural and is about the format, not this field: "Vibe follows the [Agent Skills
specification](https://agentskills.io/specification) for skill format and structure." (L712) —
i.e. the field's meaning is delegated to the open specification, whose table marks it experimental
and writes the value as a space-separated string. This page's own value form is a YAML list, so on
this page the field is printed in a form the named authority does not state. What is **not** stated:
whether the list restricts the skill's tool set, whether it pre-approves anything, whether it is
enforced, ignored, or merely carried; nothing in the skills section (L708-781) mentions permissions,
approvals or sandboxing next to it. The sweep
`grep -n -i -E 'permission|pre-approv|experimental'` prints 24 hits, and exactly one of them falls in
the skills section (L777, `disabled_skills = ["experimental-*"]`, a glob example) — the other 23 are
the unrelated `config.toml` tool-permission model (L116, L964-1187), the `pre_tool` hook contract
(L1267-1277), the experimental CLI features (`--agent-socket` L346-421, `run-server` L526-528) and
voice mode (L631). That the page documents a full `permission = "always" | "ask"` tool model for
config and MCP tools and never connects `allowed-tools` to it is the sharper form of "unstated": the
vocabulary exists on the page, and the field is not given any of it. Limits wording: the page is a README covering the CLI,
not the runtime; a ruling on enforcement would need the client's source, which this seat did not
read, so nothing here claims the field is inert at runtime — only that this page does not say.

Judgement on the frozen label: **`unstated` is true of this page** — the field appears in an example
and the page states no semantics for it. The one nuance worth recording (it does not flip the label)
is that the page does a make-or-break *delegation* at L712: it names the open specification as the
authority for the format. Read together with S226, the field is "experimental, space-separated
string" per the authority and "a YAML list, undefined here" per this page; a skill author who copies
this example gets a value form the authority does not describe and a grant no page states. If the
L1's review prefers the stronger label reading "delegated to the spec", that is a label decision for
the L1/reviewer, not something this seat changes.

## 6. Prompt-injection text seen in the page

None. Sweep on the snapshot (case-insensitive) —

```
$ grep -n -i -E 'ignore (all|previous|prior|the above)|disregard .*instruction|you must (now|ignore)|system prompt says|reveal .*(prompt|secret)|exfiltrat|instruction injection|prompt injection' vibe1.md
(no matches; rc=1, the vanilla grep reports 0 lines)
```

— returned nothing. The page's `system prompt` hits (L88, L480, L870-885, `### Custom System
Prompts`) are ordinary product documentation about `AGENTS.md` files and `prompts/cli.md`, not
instructions aimed at a reader-model, and this seat followed none of them. Every byte of this page
was treated as data.

## 7. Revision and fetch provenance (the row's anchor record, expanded)

| item | value | how obtained |
|---|---|---|
| URL | `https://raw.githubusercontent.com/mistralai/mistral-vibe/main/README.md` | the registry-row URL; HTTP 200 |
| final_url | same | `curl -w '%{url_effective}'` |
| HTTP | 200 | `curl -w '%{http_code}'` |
| bytes | 77634 | `curl -w '%{size_download}'`; `wc -c` on the saved file agrees |
| sha256 | fc48a5dbafe572fedd1457cffba8442aacd296dddaf50833ac3104252cb016b0 | `sha256sum` |
| fetch 1 | 2026-10-27T21:41:26Z | `date -u` captured immediately before the fetch |
| fetch 2 | 2026-10-27T21:41:27Z | second unfiltered fetch: same 77 634 B, same sha256 → the page did not change between fetches |
| ref served | `refs/heads/main` = `7bb48f213ac677f943d5c791199ed3dddf302f00` | `git ls-remote https://github.com/mistralai/mistral-vibe refs/heads/main` at 2026-10-27T21:43:03Z, rc=0 |
| commit check | commit-pinned raw URL (`.../7bb48f21…/README.md`) → HTTP 200, 77 634 B, sha256 identical | 2026-10-27T21:42:25Z |
| commit date | 2026-10-26T21:37:45Z (author = committer) | `api.github.com/repos/mistralai/mistral-vibe/commits/main`, HTTP 200, 1 331 925 B |
| UA | `Mozilla/5.0` | `curl -A` |
| last-modified stated by page | none | the README carries no version, date or commit line |

`--repo`-relative form of the artefacts the L1 will commit: `snapshots/S231-vibe.md`,
`snapshots/S231.manifest`, `snapshots/S231.fetch.json`, this draft
`build/Kb79R06VibeRow.rows.md`.

## 8. Freeze-discipline notes for the L1

1. The counter is not frozen yet and this seat scored nothing on it: no claim number above comes
   from `check_allowed_tools.py` (which does not exist at this revision — `ls
   verifiers/check_allowed_tools.py` → No such file or directory).
2. Conjunct (c) needs the pin in the committed `MANIFEST.sha256`; the line is in §1/§7 and in
   `S231.manifest`.
3. Conjunct (a)/(d) match on the **amended** text view (Markdown: delete every backtick byte,
   remove `(?m)^[ \t]{0,3}[*+\-][ \t]+`, collapse; fences kept — `d9d01c2`/`60ba11f`). This seat
   re-derived the quote in that view after `Kb79X01CounterBuild` reported the amendment: the
   marker-bearing form is gone from the view and the key-anchored form is 4 words, so the frozen
   quote must span L724-L728 as in §3. The sole `allowed-tools` occurrence still sits inside a
   fenced example, so a counter that strips fenced code cannot back this surface on a real page;
   the amendment keeps fences, which is what makes the row evaluable rather than a permanent
   `0 of 6`.
4. Conjunct (b) host+path-prefix: `raw.githubusercontent.com` + `/mistralai/mistral-vibe` — the row
   URL is `.../mistralai/mistral-vibe/main/README.md`, so an exact-identity check that includes the
   full path prefix passes; a sibling-host control (`.../mistral-vibe-evil`) would not match by
   prefix.
5. This seat fetched the other five surfaces' pages only as the Q70 cross-check in §4 (spec, claude,
   pi, factory, msaf; transformed-view quote count 0 on each); their registry rows and quotes stay
   with their own seats.
