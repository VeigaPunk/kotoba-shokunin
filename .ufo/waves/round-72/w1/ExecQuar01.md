# ExecQuar01 — quarantine hand-check, register slice row 1 of 13 (campaign id S151)

## Verdict

**`absent` → REFUSE (fabrication class).** Row 1 of 13 is not adoptable: the span the register files
against `https://agentskills.io/skill-creation/optimizing-descriptions.md` is not on that page in any
fold, and the span is traceable to a *different* source — a paraphrase of the arXiv 2603.22455 (v5)
abstract sentence about a 37-44 percentage-point drop in routing accuracy, which the lane already holds
as its own unopened lead note at `corpus/SOURCES.md:238` and `:280` and stages as **S210**.

Line for the L1's verdict table (13 rows):

```
S151 | agentskills.io/skill-creation/optimizing-descriptions.md | ABSENT | refuse — fabrication class:
span is not on the cited page (0 hits for metadata-only / 37 / 44 / 80K / routing / registry) and is a
paraphrase of arXiv 2603.22455v5's abstract (staged S210), i.e. mis-attributed, not merely stale
```

The row's own class cell `payload-absent` is correct as a class; the defect is worse than "payload
absent" — the quote field of this row is not a quote of the cited URL at all (see §5).

## 1. Row as given, and the staged id

Slice row, verbatim (`sed -n '1p'`, byte length from `awk 'NR==1{print length($0)}'` = **159**):

```
| `kotoba` | round3 | S151 | `payload-absent` | https://agentskills.io/skill-creation/optimizing-descriptions.md | `metadata-only routing loses 37–44 points at
```

The row is **truncated mid-span** by construction (the file's line lengths are 120–253, not a fixed
width: `awk '{print NR": "length($0)}'` → `1: 159  2: 181  3: 232  4: 126  5: 147  6: 253  7: 208
8: 120  9: 122  10: 141  11: 121  12: 124  13: 148`). The full registered span was recovered from the
register's own source, `quote-lint-full-v5.json`:

```
$ cd /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1 && \
  jq -r '.findings[] | select(.lane=="kotoba" and .id=="S151") | "---\nverdict=\(.verdict) fold=\(.fold)\nurl=\(.url)\nquote=\(.quote)\nline=\(.line)"' quote-lint-full-v5.json > s151.txt
$ sed -n '1,6p' s151.txt        # first of the 5 kotoba S151 records; 2072 bytes total
---
verdict=ABSENT fold=null
url=https://agentskills.io/skill-creation/optimizing-descriptions.md
quote=metadata-only routing loses 37–44 points at
    ~80K skills
line=`corpus/SOURCES.md:207` still reads "metadata-only routing loses 37–44 points at
```

So the registered span is `metadata-only routing loses 37–44 points at ~80K skills`, wrapped inside the
register cell (newline + 4 spaces before `~80K skills`); the slice kept only the first physical line —
that is the exact truncation mechanism. The `37–44` separator in the register is U+2013:
`... | grep -o '37.44' | od -An -tx1` → `33 37 e2 80 93 34 34 0a`.

**Staged id (by URL, host+path):**

- `https://agentskills.io/skill-creation/optimizing-descriptions.md` → **S231**, exact URL match
  (`grep -n 'optimizing-descriptions' /home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md` →
  hits on line 35 `| S231 |` and line 89 `| S285 |`).
- **S285** is the same document at the raw `.mdx` path
  (`raw.githubusercontent.com/agentskills/agentskills/main/docs/skill-creation/optimizing-descriptions.mdx`),
  i.e. the same page's source file, not a second page.
- **S151 is not a staged id.** `grep -n '^| S151 |' SOURCES.append.md` → no output; the staged file
  holds 188 `| S…` rows. S151 is a register/campaign id only, as the seat brief says.

## 2. Fetch receipts (access date 2026-10-25, UTC 21:37–21:43)

| # | URL | method | HTTP | final URL | bytes | sha256 |
|---|---|---|---|---|---|---|
| a | `https://agentskills.io/skill-creation/optimizing-descriptions.md` | `curl -fsSL`-equivalent, `-A 'Mozilla/5.0'` | **200** | same | **13403** | `7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837` |
| b | `https://raw.githubusercontent.com/agentskills/agentskills/main/docs/skill-creation/optimizing-descriptions.mdx` | same | **200** | same | **13151** | `5d6f72364f819399d07887843519d3ac037131778a5776584e5e6118d479a492` |
| c | `https://agentskills.io/skill-creation/optimizing-descriptions` (HTML, no `.md`) | same | **200** | same | 339483 | — (searched, 0 hits) |
| d | `https://web.archive.org/web/20260426113825id_/…optimizing-descriptions.md` | same | **200** | as given | 13307 | — (0 hits) |
| e | `https://web.archive.org/web/20260317151627id_/…optimizing-descriptions.md` | same | **200** | as given | 5834 | — (0 hits) |
| f | `http://archive.org/wayback/available?url=…` | same | **429** | as given | 117 | rate-limited; replaced by CDX |
| g | `http://web.archive.org/cdx/search/cdx?url=…optimizing-descriptions.md&output=json&limit=5` | same | **200** | as given | 922 | 2 snapshots: `20260317151627`, `20260426113825` |

Command form used for (a):

```
curl -sS -A 'Mozilla/5.0' -o row1.md -w 'HTTP=%{http_code} FINAL=%{url_effective} SIZE=%{size_download} TYPE=%{content_type}\n' --max-time 45 'https://agentskills.io/skill-creation/optimizing-descriptions.md'
HTTP=200 FINAL=https://agentskills.io/skill-creation/optimizing-descriptions.md SIZE=13403 TYPE=text/markdown; charset=utf-8
```

The page is **reachable and quotable** (see §7), so this row is `absent`, not `unreachable` and not
`unverifiable-class`. The `.mdx` byte size fetched now, 13151, is **exactly** the size the staged row
S285 records ("file as served from `main` at 13151 bytes"), which corroborates that the fetch target is
the document the register means.

The URL is not a `web.archive.org` redirect, so the archive form was optional; (d)/(e) were fetched
anyway and are the page-drift control: **0** hits for `metadata-only` and for `37` in both snapshots,
so the absence is not caused by the live page having changed since April.

## 3. Span search — every fold tried, all zero

Working copy: 196 lines, 13403 bytes (§2a).

```
$ grep -n -i 'metadata-only\|37\s*[–—-]\s*44\|44 points\|points at\|routing loses' row1.md
(no output; exit 1)
$ grep -n -i 'metadata' row1.md            → (no output)
$ grep -n '\b37\b\|\b44\b' row1.md         → (no output)
$ grep -n -i '80k\|80,000\|tens of thousands' row1.md → (no output)
$ grep -n -i 'routing\|registry\|registries' row1.md  → (no output)
$ grep -n -i 'los[est]\|loses\|points' row1.md
50:* **Complexity**: vary the number of steps and decision points. Include single-step tasks alongside multi-step workflows to test whether the agent can discern the skill is relevant when the task it addresses is buried in a larger chain.
$ grep -n -i 'drop\|degrad\|accuracy' row1.md
11:This guide covers how to systematically test and improve your skill's description for triggering accuracy.
```

Folds named and exhausted: (i) exact; (ii) case-insensitive; (iii) dash variants U+2013/U+2014/U+002D
inside `37…44`; (iv) whitespace/line-wrap fold (the span wraps in the register itself); (v) bare digit
tokens `37` / `44` anywhere in the file — **zero**, so no fold can rescue the span; (vi) scale token
`80K` / `80,000` — zero; (vii) topic tokens `routing` / `registry` — zero. The same two token classes are
also zero in the `.mdx` variant: `grep -c -i 'metadata' row1.mdx` → `0`, `grep -c '37\|44' row1.mdx` → `0`.

## 4. Anchors — what the page actually contains

Heading map (`grep -n '^#\|^##' row1.md`): H1 `# Optimizing skill descriptions` at line 5; H2 at
13 `## How skill triggering works`, 21 `## Writing effective descriptions`, 30 `## Designing trigger eval
queries`, 77 `## Testing whether a description triggers`, 136 `## Avoiding overfitting with
train/validation splits`, 149 `## The optimization loop`, 169 `## Applying the result`, 194 `## Next
steps`; H3 at 43 `### Should-trigger queries`, 54 `### Should-not-trigger queries`, 68 `### Tips for
realism`, 88 `### Running multiple times`. (Line 97 `#!/bin/bash` is inside the fenced example at
96–135, not a heading.)

No section of this page reports routing measurements at registry scale. The conceptually nearest text is
§`How skill triggering works` (line 13), whose operative sentence is line 17 — quoted at 10 words,
dropped trailing 67 bytes of the 165-byte line:

```
$ sed -n '17p' row1.md
This means the description carries the entire burden of triggering. If the description doesn't convey when the skill is useful, the agent won't know to reach for it.
```

That is a mechanism statement, not a measurement; it cannot carry a `37–44 points` figure. Anchor for the
row, if the L1 ever re-files the claim against the page: **none** — no heading corresponds to it.

## 5. Where the span really comes from (the fabrication reason)

1. The lane's own lead note uses this exact wording, twice:
   ```
   $ sed -n '238p;280p' corpus/SOURCES.md
   - SkillRouter (arXiv 2603.22455) — metadata-only routing loses 37–44 points at ~80K skills.
   - SkillRouter (arXiv 2603.22455) — metadata-only routing loses 37–44 points at ~80K skills.
   ```
2. The register's S151 quote field is that lead-note sentence, not a sentence of the cited page — the
   `quote` value in `quote-lint-full-v5.json` (§1) is byte-identical to the lead note apart from the
   wrap, and the register's own `line` field for the same finding begins
   `` `corpus/SOURCES.md:207` still reads "metadata-only routing loses 37–44 points at `` — the linter
   was quoting the lane's own corpus line.
3. The number itself is real, but belongs to the paper. arXiv 2603.22455's **current** abs page is v5
   (`grep -o 'arXiv:2603.22455v[0-9]'` → `arXiv:2603.22455v5`; submission history lists v1–v5), and its
   abstract says, verbatim (14 words):
   ```
   hiding the skill body causes a 37-44 percentage point drop in routing accuracy
   ```
   and elsewhere, verbatim (4 words): `approximately 80K candidate skills`. The paper's separator is a
   hyphen (`0x2d`), the register's is an en dash (`e2 80 93`) — a paraphrase, not a quote.
4. Revision control on the number: the **v2** abs page says `hiding the skill body causes a 31--44
   percentage point drop in routing accuracy`. That is where staged S210's "31–44" comes from, and it
   explains why the lane's lead note (37–44, v5) and S210 (31–44, v2) disagree while both being
   "the abstract". Not my row, but it is the reason the register cell looks internally contradictory.
5. The same register cell is garbled beyond this one span: `quote-lint-full-v5.json` holds **five**
   kotoba S151 findings, all `ABSENT` against the same URL — the other four quote fields are lane
   narrative prose (`; the paper says 31–44 percentage points, overall gap +37.8. The replacement text
   is specified in \`CANNOT-ANSWER.md\` …`, `— unknown frontmatter fields are ignored (S150)…`), one
   Japanese sentence that belongs to a vendor page (`不明なフロントマターフィールドは無視されます`), and
   the phrase `faithful translation`. A cell that concatenates a paper paraphrase, lane commentary and
   another vendor's Japanese text under one URL is a generator defect, not a fetch failure.

## 6. Slice defect handed to the L1

- `quarantine-slice-full.txt` line 1 is 159 bytes and stops mid-span (`… points at`). Any seat that
  quotes "the row verbatim" from the slice can only quote a fragment; the adoptable text is the
  register's `quote` field, which wraps at exactly that point.
- The 13 slice rows are truncated per-cell (lengths 120–253, §1), so the truncation is cell-driven
  (first physical line of a wrapped register cell), not a fixed column width.
- Recommendation: the round-72 verdict table should carry the full span from
  `quote-lint-full-v5.json` for this row, and note that rows 8–13 are the prose class
  (`the cited source could not be fetched, so no quote was checked`) — those are `unverifiable`, which
  is a different class from this row's `absent`.

## 7. Calibration controls

- **Fetch is sound, row is not.** The staged row S231's own quote is verbatim on the fetched page:
  ```
  $ grep -n 'under-specified description' row1.md
  9:A skill only helps if it gets activated. … An under-specified description means the skill won't trigger when it should; an over-broad description means it triggers when it shouldn't.
  ```
  Quoted at 20 words, dropping the 184 leading bytes of the 323-byte line; the quoted sentence is the
  line's final 139 bytes. This rules out "the page moved / the fetch was wrong" as an explanation for
  row 1.
- **`.md` vs `.mdx` are the same document.** `diff row1.md row1.mdx` differs only in the header block
  (`.md` carries the `> ## Documentation Index` banner; `.mdx` carries `title/sidebarTitle/description`
  frontmatter) and in link style (`https://agentskills.io/specification.md#progressive-disclosure` vs
  `/specification#progressive-disclosure`). The body content searched in §3 is common to both, so the
  zero-hit result is not an artefact of picking the wrong export.
- **Host-substrate dumps not used.** `/tmp/k72-omp-strings.txt` and `/tmp/k72-oc-strings.txt` are
  irrelevant to this row (no host-binary claim is involved); I did not open them, so nothing in this
  report rests on them.

## 8. Bounds, hygiene, tooling

- Lane tracked files: **none modified**. This report is the only file I wrote inside the lane. Scratch
  lived in `mktemp -d /tmp/k72w1-ExecQuar01.gVGk` and was deleted before returning (§9).
- No `git` write, no `jj`, no fleet-repo or `shokuknow` write (the `quote-lint-full-v5.json` and
  `SOURCES.append.md` reads were read-only), no subagents spawned, no background jobs beyond single
  short curls (all < 3 s wall each; the longest single command was 22.6 s for the fleet-wide grep).
- Tool installs/upgrades: **none**. No `pacman`, no `uv tool`, no `npx`. Nothing outside `curl`, `jq`,
  `grep`, `sed`, `awk`, `od`, `sha256sum`, `wc`, `diff`, `find`, `python3` (stdlib only).

## 9. Cleanup

```
$ rm -rf /tmp/k72w1-ExecQuar01.gVGk && test ! -e /tmp/k72w1-ExecQuar01.gVGk && echo GONE
GONE
```

## 10. Risks / blockers

- **Not blocked.** The row is fully decided.
- `archive.org` availability API returned **429** (rate limit) on first try; the CDX endpoint answered 200
  and supplied the same two snapshot timestamps, so the drift control still ran. Recorded as an observed
  transient, not a finding.
- The register's other four S151 findings (lane prose, opencode-ja sentence, "faithful translation") are
  outside my row but belong to the same garbled cell; whoever owns cell-level cleanup should treat S151 as
  one defective cell rather than five independent absences.
- If the L1 wants the S210 number pinned, note the revision split I measured: v5 abstract = 37-44,
  v2 abstract = 31--44. A future row quoting "the abstract" without a revision is ambiguous by
  construction.
