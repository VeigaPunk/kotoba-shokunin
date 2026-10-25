# ExecQuar10 — quarantine hand-check, register slice row 10 of 13

**Verdict: `unverifiable-class`** — the row carries no quoted span, only the prose class cell "the
cited source could not be fetched, so no quote was checked". Per addendum §10 this is **not**
fabrication and the row is **not adopted** (nothing to adopt). Secondary, and the actionable part:
the class premise is **false today** — the cited URL fetches cleanly (HTTP 200, 15,462 bytes) — and
the same document is **staged as S318**, whose anchor bullet I located. So the row's own flip
condition ("the source becomes fetchable and the quote is then checked") is half-satisfied: the
source is fetchable, but the row states no quote to check.

Seat is read-only. Nothing committed. Scratch: `/tmp/k72w1-ExecQuar10.*` (deleted before return).
No tool installed or upgraded.

## F1 — the register row, verbatim, and why it has no quote

```
$ sed -n '10p' .ufo/waves/round-72/assimilation/quarantine-slice-full.txt | cat -A
| `kotoba` | round10 | S238` | the cited source could not be fetched, so no quote was checked | https://code.claude.com/docs/en/security.md |$
$ sed -n '10p' .ufo/waves/round-72/assimilation/quarantine-slice-full.txt | wc -c
142
$ awk -F'|' '{printf "row%d fields=%d\n", NR, NF-2}' .ufo/waves/round-72/assimilation/quarantine-slice-full.txt
row1 fields=5
row2 fields=5
row3 fields=7
row4 fields=5
row5 fields=5
row6 fields=7
row7 fields=7
row8 fields=5
row9 fields=5
row10 fields=5
row11 fields=5
row12 fields=5
row13 fields=5
```

Row 10 is a **5-cell** row: `kotoba` | `round10` | `S238\`` | prose-meaning | URL. The id cell ends
in a stray backtick and there is no class cell and no quote cell; the quote-bearing rows in the same
slice are the 7-cell ones (rows 3, 6, 7). Source register line, identical text:

```
$ grep -n 'security.md' /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md
329:| `kotoba` | round10 | S238` | the cited source could not be fetched, so no quote was checked | https://code.claude.com/docs/en/security.md |
```

Register header, lines 9–15, defines the class vocabulary — `payload-absent` is "the fabrication
class", `unreachable` is "re-fetch, or mark the row unverifiable — do NOT call it a fabrication".
These 6 rows sit outside that table (its Totals list only `payload-absent`), so the class is prose,
not a token. Consequence: no quoted span exists between backticks to search for. Verdict class:
`unverifiable-class`.

## F2 — staged id by URL: **S318**; and the id-namespace trap

```
$ grep -c 'code.claude.com/docs/en/security.md' /home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md
1
$ sed -n '122p' .../SOURCES.append.md | cut -c1-1200
| S318 | Claude Code — Security — https://code.claude.com/docs/en/security.md | docs | B | Anthropic's own client security documentation; ... | the trust-verification bullet in the workspace-trust section | ... | mined | 2026-10-24 | 90d — re-fetch the page and confirm the trust-verification bullet is unchanged | corpus/knowledge/installer-security-guidance-round10.md |
```

So the register's campaign id `S238` maps, **by URL**, to staged **S318** (mined 2026-10-24). The
campaign id must not be resolved as a staged id: staged **S238** is a different document —

```
$ grep -n 'S238' /home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md
42:| S238 | moonshotai/kimi-cli — CHANGELOG.md — https://raw.githubusercontent.com/moonshotai/kimi-cli/main/CHANGELOG.md | ...
```

A hand-check that resolved this row by id would have checked the Kimi CLI changelog instead of the
security page. (This id-vs-URL divergence is campaign-wide for the round-10 block: the slice ids
`S236`–`S243` are campaign ids, not staged ids.)

## F3 — fetch: the class premise ("could not be fetched") is false today

All fetches `curl -fsSL -A 'Mozilla/5.0'`, access date **2026-10-25T21:37:36Z**:

| URL | status | final URL | bytes | sha256 |
|---|---|---|---|---|
| `https://code.claude.com/docs/en/security.md` (the cited URL) | 200 | same | 15,462 | `3d516a197892dc41847431f83ee8bb1357fd819fca3f0c1426c6e095d135586f` |
| `https://code.claude.com/docs/en/security` (extensionless HTML) | 200 | same | 454,029 | `d33e375e06d8a6ca2f0f4ce27139c8f36e4076fd108d9e4ddc08ad09564c83bd` |
| same `.md`, **no** user-agent | 200 | same | 15,462 | — |
| `https://code.claude.com/docs/llms.txt` (index the page points at) | 200 | — | — | — |

```
$ curl -sSL -A 'Mozilla/5.0' -o security.md -w 'status=%{http_code} final=%{url_effective} size=%{size_download}\n' 'https://code.claude.com/docs/en/security.md'
status=200 final=https://code.claude.com/docs/en/security.md size=15462
$ sha256sum security.md
3d516a197892dc41847431f83ee8bb1357fd819fca3f0c1426c6e095d135586f  security.md
```

The URL is not a web.archive redirect, so no archive form was needed; the `.md` export is the
primary fetch and it is the one that worked. Calibration: the register's "could not be fetched" was
true at some earlier time or under some other fetch policy (unobserved — I cannot reconstruct the
round-10 fetch), but it is **not** a property of the URL now. A row classed unreachable that is now
reachable should be re-derived on its quote, and this row supplies none.

## F4 — nothing to locate in the row; the staged S318 anchor *is* locatable, but its section label is wrong

Since row 10 has no quoted span, step (3) has no target. Supplementary check on staged S318's stated
anchor ("the trust-verification bullet in the workspace-trust section"):

```
$ grep -n '^#\+ ' security.md
5:# Security   39:## Protect against prompt injection   43:### Core protections
9:## How we approach security   48:### Privacy safeguards   58:### Additional safeguards
11:### Security foundation   87:## MCP security   93:## IDE security   97:## Cloud execution security
15:### Permission-based architecture   113:## Security best practices   115:### Working with sensitive code
24:### Built-in protections   122:### Team security   130:### Reporting security issues
35:### User responsibility   139:## Related resources
$ sed -n '62p' security.md   # line number verified with sed -n '58,64p' | nl -ba -v58
* **Trust verification**: In an interactive session, Claude Code shows the workspace trust dialog when you start it in a folder you haven't trusted. Servers in a project's `.mcp.json` have their own approval prompt, and [Project scope](https://code.claude.com/docs/en/mcp.md#project-scope) lists the sessions that skip it
```

Anchor located: the bullet at **line 62** of the fetched `.md`, under `## Protect against prompt
injection` (line 39) → `### Additional safeguards` (line 58). There is **no heading** containing
"workspace trust" anywhere in the page (`grep -n -i 'workspace' security.md` returns only line 62);
the phrase "workspace trust dialog" is *inside* the bullet. So the staged row's section label names
a section that does not exist — the anchor is the bullet, not a section. A 17-word span from the
fetched bytes, for the lesson's gate table if the L1 adopts S318:

> Claude Code shows the workspace trust dialog when you start it in a folder you haven't trusted

(That span is a literal substring of line 62; the bytes I dropped from the line are the leading
`* **Trust verification**: In an interactive session, ` and everything from ` . Servers in a
project's` onward. No fold applied.)

## F5 — nothing in the lane already holds this URL, so no duplicate risk

```
$ grep -rn 'code.claude.com/docs/en/security' corpus/
corpus/lessons/round-68.md:111:| S238 | unreachable | code.claude.com/docs/en/security.md | unverifiable — same class |
$ grep -c '^| S' corpus/SOURCES.md
139
$ ls -la corpus/knowledge/installer-security-guidance-round10.md
ls: cannot access 'corpus/knowledge/installer-security-guidance-round10.md': No such file or directory
```

The lane registry (139 rows) has **no row** for this page; the only lane mention is the round-68
lesson table, which already recorded it as `unreachable` / "unverifiable — same class"
(`corpus/lessons/round-68.md:111`). The staged row's `used-by` entry
(`corpus/knowledge/installer-security-guidance-round10.md`) does **not** exist in the lane, so S318
is staged-only and adopting it would require creating that entry. Prior-round consistency: the
round-68 lesson's flip condition is exactly "the source becomes fetchable and the quote is then
checked — an unreachable row is never a fabrication claim", and round-70's scout already recorded
the stray-backtick 5/6-cell quirk for this block (`.ufo/waves/round-70/w1/ScoutQuarantine.md:30-32`)
— my row reproduces both, so no new defect class is claimed.

## F6 — adjacent observed state (not my seat's claim, recorded because it bears on C1 A4)

```
$ ls -la .ufo/waves/round-72/snapshots/
total 0   (empty)
```

C1 rule A4 requires a committed, sha256-pinned snapshot under `.ufo/waves/round-72/snapshots/`; the
directory is empty at the time of this check. Flagged for the L1/ExecC1Replay seats; I made no
change.

## Recommendations to the L1 (one line each)

1. Land row 10 in the lesson's quarantine table as **`unverifiable-class`** with the reason "no
   quoted span in the row; prose class cell", and note that the URL is now fetchable (200, 15,462 B,
   sha256 `3d516a19…`) — do not call it fabrication.
2. Record that register id `S238` is a **campaign** id whose document is staged **S318** (URL match),
   and that staged `S238` is the Kimi CLI changelog — id-based resolution would mis-bind.
3. If S318 is adopted, cite the bullet at fetched line 62 under `### Additional safeguards` and
   **not** a "workspace-trust section", which does not exist on the page.

## Frontier note

Cheapest next probe if anyone re-opens this row: the register's own generator
(`absent-defect-register.py`, header line 3) is what produced the prose class; re-running the quote
census over the round-10 rows with the now-fetchable URLs would convert `unreachable` rows into
checkable ones — a campaign-side action, outside this lane's write bounds.
