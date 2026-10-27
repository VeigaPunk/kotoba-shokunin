# Kb79R06VibeRow — C2 source row for surface `vibe` (Mistral Vibe), S231

Seat: leaf executor, round 79 w1. Lane repo `/home/vgpnk/Projects/shokunin/kotoba-shokunin`
(base `b10bcbc6b00f8f56b202ccbadca311007b5b463c`, plan commit
`2c56622375641193a03bb97c0624e6536f3dffba`). No lane file was edited; only the paths this item
names were written. No tool was installed or upgraded (nothing needed). One post-hoc revision: the
C2 text view was amended by the L1 before any data (`d9d01c2`, `60ba11f`), and this seat re-derived
its quote in the amended view after `Kb79X01CounterBuild` stated the transformation — § "Amendment"
below.

## Fetches (each `curl -sSL -A 'Mozilla/5.0' --max-time 60`, own exit status captured)

| # | URL | UTC | HTTP | bytes | sha256 | rc |
|---|---|---|---|---|---|---|
| 1 | `https://raw.githubusercontent.com/mistralai/mistral-vibe/main/README.md` | 2026-10-27T21:41:26Z | 200 | 77634 | `fc48a5dbafe572fedd1457cffba8442aacd296dddaf50833ac3104252cb016b0` | 0 |
| 2 | same | 2026-10-27T21:41:27Z | 200 | 77634 | same sha256 | 0 |
| 3 | `https://raw.githubusercontent.com/mistralai/mistral-vibe/7bb48f213ac677f943d5c791199ed3dddf302f00/README.md` | 2026-10-27T21:42:25Z | 200 | 77634 | same sha256 | 0 |
| 4 | `https://api.github.com/repos/mistralai/mistral-vibe/commits/main` | 2026-10-27T21:43:03Z | 200 | 1331925 | (metadata only) | 0 |

Fetches 1 and 2 are byte-identical (`sha256sum` equal), so the page **did not change between
fetches**. `git ls-remote … refs/heads/main` at 2026-10-27T21:43:03Z (rc=0) printed
`7bb48f213ac677f943d5c791199ed3dddf302f00`, and fetch 3 at that commit is byte-identical to the
`main` fetch — the row records revision `7bb48f2` (commit date 2026-10-26T21:37:45Z). The page states
no last-modified.

## Located quote (amended text view) and its location

The sole `allowed-tools` occurrence on the page is L725, inside the `code-review` skill example under
`### Creating Skills` (L714-L734), written as a YAML block list:

```
724  user-invocable: true
725  allowed-tools:
726    - read
727    - grep
728    - ask_user_question
729  ---
```

## Amendment (recorded, not worked around)

`plans/round-79.md` § C2 line 42 as committed at `c469863` (amendments `d9d01c2` "clarify markdown
snapshot text view before data", `60ba11f` "freeze exact S226 transformed quote before scoring")
freezes the text view: for Markdown snapshots "delete every backtick byte and remove an unordered-list
marker by `(?m)^[ \t]{0,3}[*+\-][ \t]+`; then collapse whitespace", fences not stripped. Consequences
this seat verified on its own snapshot bytes:

- pre-amendment `allowed-tools: - read - grep - ask_user_question` is **not** in the amended view
  (markers deleted) — it cannot be used;
- the key-anchored `allowed-tools: read grep ask_user_question` is **4** whitespace tokens — under
  the 5-word floor — so it cannot be used either;
- the quote must span the preceding line. Frozen form used in both the registry row and the entry
  row: `user-invocable: true allowed-tools: read grep ask_user_question` — 6 tokens, exactly one
  occurrence in the amended view, contains `allowed-tools` word-bounded, carries the frozen vibe page
  token `allowed-tools:`, and spans raw L724-L728 (all body lines; no heading line, not the
  first-heading block).

Shaping applied, exactly: backtick deletion (none in L724-728), unordered-marker removal (the two
spaces + `- ` on each of L726-728, 4 bytes per line), whitespace collapse of the newlines ending
L724-728. No tags stripped, no entities decoded, no case folding (raw Markdown, no HTML in the span).

## The two deliverables

Registry row (11 cells, `status` mined, tier **B** because this is one vendor's README for its own
CLI, not the format authority — the open specification S226 is the tier-A ground it delegates to at
L712; `opened` 2026-10-27, `recheck` 90d, `used-by` the frozen entry path, anchor cell carrying the
section, the commit, the transformed-form quote and `fetched 2026-10-27T21:41:26Z, HTTP 200, 77634 B,
sha256 fc48a5db…`) and the entry row in the frozen header with surface `Mistral Vibe`, source `S231`,
page tokens `` `allowed-tools` `allowed-tools:` `ask_user_question` `user-invocable` ``, grant
`unstated` (plain, not backticked) and the located quote above — both written verbatim in
`build/Kb79R06VibeRow.rows.md` §1-§2. All four tokens verified ASCII-word-bounded in the amended view;
the registry row parses as exactly 11 cells (`|`-split, naive NF 13), the entry row as exactly 5.

## Findings (what the page does and does not say)

- The page names the open specification as its format authority (L712: "Vibe follows the [Agent
  Skills specification](https://agentskills.io/specification) for skill format and structure.") and
  then prints `allowed-tools` as a **YAML block list** (L725-728) — the spec writes a space-separated
  string. A skill that copies this example uses a value form the named authority does not describe.
- It states **no semantics** for the field: no restriction, no pre-approval, no enforcement, no
  ignore. The contrast inside the page is sharp: the next paragraph defines `user-invocable` and
  `disable-model-invocation` explicitly (L736-745), and the page documents a full
  `permission = "always" | "ask"` tool model for config and MCP tools (L964-1187) — none of that
  vocabulary is attached to `allowed-tools`. The sweep
  `grep -n -i -E 'permission|pre-approv|experimental'` prints 24 hits, only one inside the skills
  section (L777, a `disabled_skills = ["experimental-*"]` glob example).
- Judgement on the frozen chip: **`unstated` is true of this page.** Nuance for the L1/reviewer
  (does not flip it): L712 delegates the format to the spec, so a reviewer preferring a
  "delegated-to-spec" reading has a line to cite; this seat did not change the label.
- Q70 (amended quote): 0 occurrences in the amended view and 0 in the raw bytes of all five other
  surfaces fetched here (spec 7 608 B, claude 117 962 B, pi 4 793 B Markdown; factory 341 235 B,
  msaf 157 339 B HTML), and `allowed-tools` appears once on this page outside the title/TOC — not a
  banner line and not a line another snapshot carries.
- Prompt injection: none found. Sweep
  `grep -n -i -E 'ignore (all|previous|prior|the above)|disregard .*instruction|you must (now|ignore)|system prompt says|reveal .*(prompt|secret)|exfiltrat|instruction injection|prompt injection'`
  → 0 lines, rc=1. The page's `system prompt` sections (L870-885) are product docs about
  `AGENTS.md`/`prompts/cli.md`; treated as data, nothing followed.

## Counter-state note

`check_allowed_tools.py` still does not exist in the lane tree (`ls verifiers/check_allowed_tools.py`
→ No such file or directory), so no claim number here comes from a frozen counter; the draft build
(`.ufo/waves/round-79/build/check_allowed_tools.py`) is the L1's to freeze. Messaged
`Kb79X01CounterBuild` (quote form, token roles, the fence/text-view constraint) and
`Kb79A02EntrySkeleton` (the transformed-form quote its `source:` lines must carry, so the entry and
the table row cannot disagree at freeze).

## Verification run (commands and own exit status)

- `sha256sum`/`wc -c`/`cmp` on the saved snapshot vs the fetch buffer → `fc48a5db…`, 77634 B,
  `cmp identical`.
- Python, amended view: quote present once, 6 words; four tokens ASCII-word-bounded → True;
  pre-amendment quote absent; key-anchored form = 4 words (floor breach recorded).
- `S231.fetch.json` sha/bytes equal the file → True; `S231.manifest` line matches → True.
- Cross-page: transformed-view `count()` = 0 and raw `grep -c -F` = 0 on spec, claude, pi, factory,
  msaf.
- Row parse: registry row 11 cells, entry row 5 cells, no `|` inside any cell.
- Not run by me (out of scope): the census, the no-harm battery, and any scoring on the frozen C2
  counter.

## Freeze hygiene

All scratch lived in `/fast/scratch/hyaku/kotoba-r79/Kb79R06VibeRow/` (`TMPDIR` set there) and was
removed before this report; no git/jj mutation was run anywhere (only `git ls-remote` / `git show`
reads, in the lane and against GitHub). `pacman` was never invoked. No credentials, cookies, tokens
or `op://` references are in any output.

VERDICT: S231 draft row + entry row produced from a twice-fetched, commit-pinned page (main = 7bb48f2, 77634 B, sha256 fc48a5db…); under the L1's pre-data text-view amendment the quote is `user-invocable: true allowed-tools: read grep ask_user_question` (6 words, one occurrence, 0 on five other surfaces) and the `unstated` label is true of the page, which prints the field only as a YAML list inside a fenced example.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79R06VibeRow.rows.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/snapshots/S231-vibe.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/snapshots/S231.manifest, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/snapshots/S231.fetch.json, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/w1/Kb79R06VibeRow.md
