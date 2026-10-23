# FalsifyS118 — re-open of https://code.claude.com/docs/en/memory.md

Seat: `L1kotoba62.FalsifyS118`. Axis: freshness. Lane tip `e6da78bbe420722dd18a13182a7c4b64ce02f005`. Read-only except this report. No installs. One fetch.

## Verdict

**no drift.** Fresh body sha256 `02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801`, 55,354 B, `cmp` exit 0 against `.ufo/waves/round-62/snapshots/S118.page`. Worktree blob `3760e93bda82ec0565b692694995b90f9cc7fec5` is the blob at `HEAD` for that path.

Line 250 of the snapshot is the source-quoted table row, byte-identical to the fresh file. `wc -w` of that line is **23** (≤25). Pipes included. Excluding the four `|` tokens leaves 19. Both counts are ≤25.

Separate failed claim (not page drift): the landed Gate and knowledge quotes are not that table row and are not substrings of line 250. See § Landed quote.

## Fetch (once)

Access file mtime `2026-10-23 18:32:51 -0300` (`/tmp/S118.page.fresh`). UA `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36`. `--max-time 30`. Body via `-o` (write-out went to stdout, not the file).

```sh
curl -sS -L -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36" --max-time 30 -w "\nHTTP_CODE:%{http_code}\nSIZE:%{size_download}\n" -o /tmp/S118.page.fresh "https://code.claude.com/docs/en/memory.md"; echo EXIT:$?; sha256sum /tmp/S118.page.fresh; wc -c /tmp/S118.page.fresh; sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-62/snapshots/S118.page; wc -c /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-62/snapshots/S118.page; cmp -s /tmp/S118.page.fresh /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-62/snapshots/S118.page; echo CMP_EXIT:$?
```

```text
HTTP_CODE:200
SIZE:55354
EXIT:0
02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801  /tmp/S118.page.fresh
55354 /tmp/S118.page.fresh
02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801  /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-62/snapshots/S118.page
55354 /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-62/snapshots/S118.page
CMP_EXIT:0
```

`diff -q` of the two files also exited 0 (no output). Prefix `02632438` matches the claimed digest. Committed identity:

```text
e6da78bbe420722dd18a13182a7c4b64ce02f005
3760e93bda82ec0565b692694995b90f9cc7fec5
100644 blob 3760e93bda82ec0565b692694995b90f9cc7fec5	.ufo/waves/round-62/snapshots/S118.page
```

(`git -C <lane> rev-parse HEAD`; `git hash-object` of the worktree snapshot; `git ls-tree -r HEAD` of the same path. hash-object equals the index blob.)

## Line 250 — quoted table row

`sed -n '250p'` on the snapshot and on `/tmp/S118.page.fresh` both print:

```text
| `paths` | No | Glob patterns that [scope the rule to matching files](#path-specific-rules). Accepts a YAML list or a comma-separated string |
```

That string is the unjoined row quoted at `.ufo/waves/round-62/w1/SrcRulesFrontmatter.md:35` and again at `ScribeSourcesS118.md:44`. Python `line ==` that row is True for the snapshot and for the fresh file (`FULL_ROW_EXACT True`, `FRESH_LINE_EQ True`). Heading at snapshot line 244 is `#### Rule frontmatter reference`. The row sits under `| Field | Required | Description |` / `| :- | :- | :- |` (lines 248–249).

Word count of the full line (`sed -n '250p' | wc -w`, and the same line written to `/tmp/S118.line250`):

```text
23
WC_EXIT:0
```

```text
 23 /tmp/S118.line250
```

Whitespace tokens (23), pipes marked:

1. `|`
2. `` `paths` ``
3. `|`
4. `No`
5. `|`
6. `Glob`
7. `patterns`
8. `that`
9. `[scope`
10. `the`
11. `rule`
12. `to`
13. `matching`
14. `files](#path-specific-rules).`
15. `Accepts`
16. `a`
17. `YAML`
18. `list`
19. `or`
20. `a`
21. `comma-separated`
22. `string`
23. `|`

23 ≤ 25. Dropping `|` tokens: 19 ≤ 25. The source seat's claim that this line is under 25 words holds on both counts.

## Landed quote — failed verbatim location

`CORPUS.md:113-114` requires the lesson Gate to record a ≤25-word quote with its location. The page did not drift. The quotes that landed are a shaped fragment, not the table row, and neither fragment occurs on line 250.

`corpus/lessons/round-62.md:14` curly span (period outside the quotes):

```text
Glob patterns that scope the rule to matching files
```

`wc -w` = 9. `span in line 250` = False. Line 250 has `Glob patterns that [scope the rule to matching files](#path-specific-rules)`. The brackets and the `(#path-specific-rules)` anchor were dropped. That is shaping, not a contiguous quote.

`corpus/knowledge/erratum-absorption-round62.md:43` curly span (period inside the quotes):

```text
Glob patterns that scope the rule to matching files.
```

`wc -w` = 9. `span in line 250` = False. The sentence says the snapshot line "says" that span. It does not.

So: **no drift** on the fetched page versus the committed snapshot. The source-quoted table row is on line 250 and is ≤25 words. The Gate and knowledge quotations of that line fail as verbatim quotes.

## Not run

No second fetch. No census. No lane product edit.
