# ExecQuar02 — quarantine hand-check, register slice row 2 of 13 (S167)

## Verdict
**absent → refuse as fabrication class.** The registered quote cell holds register-internal lane
prose ("The lane holds this page as S002; this row records only that …"), not text from the cited
page; the span is absent from the fetched source (0 hits) and cannot be anchored. Nothing appendable.

## 1. Register row read (verbatim, slice line 2)

```
| `kotoba` | round4 | S167 | `payload-absent` | https://agentskills.io/client-implementation/adding-skills-support.md | `The lane holds this page as S002; this row records only that
```

Command: `sed -n '2p' .ufo/waves/round-72/assimilation/quarantine-slice-full.txt` (the `cat -A`
dump ends the line at `that$`). Row is 181 bytes, 7 cells by `awk -F'|'`, and the quote cell is
**truncated** (no closing backtick, no trailing `|`, next row starts on line 3). The `round4` id
`S167` is not a lane registry row: `grep 'S167' corpus/SOURCES.md` and `grep -n S167
.ufo/waves/round-72/assimilation/reg-ids` both return nothing (reg-ids has 139 rows, S002 at index 2).
The lane *does* hold this page as **S002** (SOURCES.md line 15, URL without `.md`).

## 2. Staged row by URL (host+path)

`grep -n 'adding-skills-support' /home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md`
→ the URL `https://agentskills.io/client-implementation/adding-skills-support.md` appears in two
staged rows: **S247** (line 51, trust-gate paragraph; description mentions "the round-4 row S164")
and **S256** (line 60, loading/validation/disclosure sections). So: staged id = `S247`, `S256`
(both); the register's campaign id S167 is not itself staged.

## 3. Fetch

`curl -fsSL -A 'Mozilla/5.0' -o /tmp/k72-S167-page.md -w 'HTTP_STATUS=%{http_code}\nFINAL_URL=%{url_effective}\nSIZE=%{size_download}\n' https://agentskills.io/client-implementation/adding-skills-support.md`
- HTTP status: **200**; final URL: same (`https://agentskills.io/client-implementation/adding-skills-support.md`)
- Size: **20,446 bytes**; sha256: **07511caadbe1bad84d81477d0efce87bc2c7eaff562179522c083910586dfb06**
- Access date: **2026-10-25T21:40:27Z**; 337 lines.
- Also fetched the `.md`-less URL (200; 388,444 bytes HTML) — same content source.

## 4. Span location

Registered quote span: `The lane holds this page as S002; this row records only that` (truncated in
the slice). `grep -n` on the fetched page: `The lane holds` → 0 hits, `S002` → 0 hits.
**Absent.** The span is self-referential campaign prose (a lane-side note about the lane's own S002
row) leaked into the quote column — not source text. No anchor exists for it.

Cross-check (prior rounds, same row): `corpus/lessons/round-68.md` line 102 records the full
untruncated span and the same verdict: `| S167 | payload-absent | agentskills.io/.../adding-skills-support.md | refused — the quoted span is a campaign note about the lane's own S002, not a source quotation; nothing appendable |`.
`corpus/lessons/round-70.md` line 111 also lists S167 under `payload-absent`. The round-68
ScoutQuarantine1.log (lines 59, 84, 129, 133, 185–187) fetched the page and confirmed the span is
lane prose, not page text, plus the truncated `\n`-wrapped quote artifact.

## Notes (unobserved / docs)
- The slice file's row is truncated (181 bytes, unterminated quote cell) — the full registered quote
  per round-68 log is "The lane holds this page as S002; this row records only that paragraph, which
  no lane entry cites. Re-check: refetch the …". Either way the span is absent from the source.
- The staged S247 description cites "the round-4 row S164" while this register row says S167 — id
  inconsistency between the staged package and the register; noted, not adjudicated here.
- No file was edited; report only.
