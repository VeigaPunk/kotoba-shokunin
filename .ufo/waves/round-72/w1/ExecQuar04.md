# ExecQuar04 — quarantine hand-check, register slice row 4 of 13 (campaign `S172`, Junie)

## Verdict

**`present-after-fold(register-side truncation at `user-le` + elision of two inline `<code>` parentheticals + double-space collapse)` — adopt, do not carry `payload-absent` as a fabrication verdict.**

The register row's class cell reads `payload-absent` with reason *"cited source, companion URLs and
local artifacts were all checked; the quote is in none of them"*. That reason is false for the
substance: the sentence the row names exists on the cited page today, and its **16-word tail is
byte-exact present, 1× live and 1× in Wayback**. What the literal test cannot pass is caused by the
register's own write: the quote cell is truncated mid-word at `user-le`, and the page interposes two
inline `<code>` parentheticals the register quote omits. So: **not fabrication; a fold artifact.**

- Campaign id `S172` → staged id **`S252`** (same URL, `SOURCES.append.md:56`).
- The page is **already held by the lane as `S206`** (`corpus/SOURCES.md:147`, tier A, `mined`,
  `used-by corpus/knowledge/skill-name-precedence-round69.md`) whose quote is the same sentence's
  11-word contiguous tail. Adopting `S252` as a new row would be a duplicate URL **and** a duplicate
  claim; the substance of row 4 is already landed.

---

## 1. Row identity — the slice row is not the full row

Slice file, row 4 (127 bytes, `cat -A` shows no trailing content):

```
| `kotoba` | round5 | S172 | `payload-absent` | https://junie.jetbrains.com/docs/agent-skills.html | `If a project-level and a$
```

Original register (`/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md`,
read-only), lines 111–113 — the row **wraps across three lines**:

```
$ awk 'NR>=111 && NR<=113 {printf "%d[%d]: %s\n", NR, length($0), $0}' absent-defect-register.md
111[126]: | `kotoba` | round5 | S172 | `payload-absent` | https://junie.jetbrains.com/docs/agent-skills.html | `If a project-level and a
112[87]: user-level skills share the same name, the project-level skill takes precedence and the
113[108]: user-le` | cited source, companion URLs and local artifacts were all checked; the quote is in none of them |
```

```
$ diff <(awk 'NR==111' absent-defect-register.md) <(awk 'NR==4' .../quarantine-slice-full.txt) && echo IDENTICAL
IDENTICAL
```

So the slice kept only line 111 of a 3-line row: the quote cell as the slice shows it is a **5-word
fragment** (`If a project-level and a`), and the class reason cell (line 113) is absent from the
slice entirely. I hand-checked the **full** row (111–113), as the item requires.

**Calibration finding for the whole 13-row pass (not only my row):** the slice systematically keeps
only the first physical line of wrapped rows. Verified for three rows:

```
$ diff <(awk 'NR==108' absent-defect-register.md) <(awk 'NR==2' .../quarantine-slice-full.txt) && echo IDENTICAL
IDENTICAL            # S167 wraps to line 109
$ diff <(awk 'NR==114' absent-defect-register.md) <(awk 'NR==5' .../quarantine-slice-full.txt) && echo IDENTICAL
IDENTICAL            # S176 wraps to line 115
$ awk 'NR>=108 && NR<=115 {printf "%d[%d]\n", NR, length($0)}' absent-defect-register.md
108[181] 109[160] 110[232] 111[126] 112[87] 113[108] 114[147] 115[129]
```

Any seat that hand-checks the slice text alone is checking a truncated quote. Rows 2, 4 and 5 are
affected; the other slice rows are single-line in the register (S151, S168, S180, S185, S236–S243,
S169).

## 2. Fetch record (all run 2026-10-25)

Live fetch, `curl -fsSL -A 'Mozilla/5.0'`:

```
$ curl -sS -A 'Mozilla/5.0 (X11; Linux x86_64) ... Chrome/124.0 Safari/537.36' \
    -o /tmp/k72w1-junie.html -w 'HTTP=%{http_code} FINAL=%{url_effective} SIZE=%{size_download} CT=%{content_type}\n' \
    -L 'https://junie.jetbrains.com/docs/agent-skills.html'
HTTP=200 FINAL=https://junie.jetbrains.com/docs/agent-skills.html SIZE=38509 CT=text/html
$ sha256sum /tmp/k72w1-junie.html
b3c676900e3de8a0d34754bb223685e1734c95ecc635280d8b8b159928f5a915
```

Headers:

```
$ curl -sSI -A 'Mozilla/5.0' https://junie.jetbrains.com/docs/agent-skills.html | grep -iE 'HTTP/|last-modified|etag|content-length|date:'
HTTP/2 200
date: Sun, 25 Oct 2026 21:39:10 GMT
content-length: 38509
last-modified: Fri, 23 Oct 2026 18:43:22 GMT
etag: "6adbaaca-966d"
```

`.md` export — **404**, so no markdown source to compare:

```
$ curl ... -o /tmp/k72w1-junie-md.out -w 'HTTP=%{http_code} FINAL=%{url_effective} SIZE=%{size_download}\n' -L 'https://junie.jetbrains.com/docs/agent-skills.md'
HTTP=404 FINAL=https://junie.jetbrains.com/docs/agent-skills.md SIZE=153
sha256 9f6d0b634cab6787cdebb2a02e08a2e2ff6d8863344e46aa7bf387e607b827c3   (153 B "<title>404 Not Found</title>")
```

Wayback form (the URL is not itself an archive redirect; fetched anyway for a dated cross-check):

```
$ curl ... -L 'https://web.archive.org/web/2026/https://junie.jetbrains.com/docs/agent-skills.html'
HTTP=200 FINAL=https://web.archive.org/web/20260909095632/https://junie.jetbrains.com/docs/agent-skills.html SIZE=41007
sha256 b2e4238c28be2d4cbced42123bcb4908725de55a3a8300c96d992b4ab74a246b
```

Snapshots retained as drafts (bytes copied, shas re-checked after copy):

```
b3c676900e3de8a0d34754bb223685e1734c95ecc635280d8b8b159928f5a915  build/ExecQuar04/junie-agent-skills-live-2026-10-25.html   38509
b2e4238c28be2d4cbced42123bcb4908725de55a3a8300c96d992b4ab74a246b  build/ExecQuar04/junie-agent-skills-wayback-20260909095632.html  41007
```

Access date for every probe: **2026-10-25**.

## 3. Locate — literal test, then the fold test

Raw-byte literal tests (`grep -Fc`, count of matching lines):

```
$ grep -Fc "If a project-level and a"                                          k72w1-junie.html   -> 0
$ grep -Fc "skills share the same name, the project-level skill takes precedence and the user-level skill is ignored."  -> 1
$ grep -Fc "the project-level skill takes precedence and the user-level skill is ignored."                              -> 1
```

So the register's literal text (even its 5-word prefix) is **not contiguous in the served bytes**:
the page puts two inline `<code>` parentheticals between `project-level` and `and a`. The sentence
starts at raw byte offset **15824**; the whole sentence is 321 bytes (15824–16145). It sits on line
**27**, column **9987** (line 27 spans 5838–16471, 10 633 bytes).

`sed -n '27p'` paste, columns 9987–10315, i.e. the sentence start through its full stop (bytes before
col 9987 and after col 10315 on that line dropped; the closing `</p></aside>` is included as served):

```
If a project-level (<code class="code" id="-jqc5nu_131">&lt;projectRoot&gt;/.junie/skills/&lt;skill-name&gt;/</code>) and a user-level (<code class="code" id="-jqc5nu_132">~/.junie/skills/&lt;skill-name&gt;/</code>) skills share the same name, the project-level skill takes precedence and the user-level skill is ignored.</p></as
```

Anchor — the heading immediately before the sentence is an **h3**, not the h2 round 69 recorded:

```
$ sed -n '27p' k72w1-junie.html | cut -c6988-7062
<h3 id="skill-location" data-toc="skill-location">Skill location</h3><p id=
```

and the sentence is inside a note box:

```
$ sed -n '27p' k72w1-junie.html | cut -c9935-9986
Scope priority" id="-jqc5nu_95"><p id="-jqc5nu_130">
```

**Anchor to record:** chapter `Skill location` (`<h3 id="skill-location" data-toc="skill-location">`
at offset 12825), note box `Scope priority` (`<aside class="prompt" data-type="note"
data-title="Scope priority" id="-jqc5nu_95">` at 15772). The next chapter heading after the sentence
is `<h3 id="skill-directory-structure">`, so the sentence is inside the `Skill location` chapter.
The page's `<h2 id="skill-locations-and-configuration">` (offset 22228) is a **different** section
and does not contain this sentence.

Fold test matrix (each a full-file count):

| test | count |
|---|---|
| raw bytes, register text as written | 0 |
| tag-stripped only | 0 |
| tag-stripped + the two `<code>` parentheticals elided (leaves `project-level  and`) | 0 |
| parentheticals elided + `[ \t]+` collapsed | **1** |
| 16-word contiguous tail, raw bytes | **1** |
| 16-word contiguous tail, Wayback `20260909095632` | **1** |
| 22-word derived sentence (register with parentheticals elided), Wayback | 0 (same parentheticals there) |

Word counts: register-with-parentheticals-elided sentence **22 words**; contiguous tail
`skills share the same name, the project-level skill takes precedence and the user-level skill is
ignored.` **16 words** (`printf '%s' "…" | wc -w` → 16).

## 4. Staged mapping and lane collision

Same URL, host+path `junie.jetbrains.com/docs/agent-skills.html`, in the staged package:

```
$ sed -n '56p' /home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md
| S252 | Junie — Agent Skills — https://junie.jetbrains.com/docs/agent-skills.html | docs | B | … | "Skill locations" and "Frontmatter fields" sections; quote "If a project-level and a user-level skills share the same name, the project-level skill takes precedence and the user-level skill is ignored."; also the `--skill-default-locations false` lever and the frontmatter table; retrieved 2026-10-23 | …
```

- Staged id: **S252**, present in `.ufo/waves/round-72/assimilation/staged-ids`. Not `not staged`.
- `S252` appears in **no** row of the round's declared theme entries:
  `$ grep -c "S252" knowledge/corpus/knowledge/skill-vs-always-on-boundary.md` → `0`;
  `$ grep -c "S252" knowledge/corpus/knowledge/context-rot-and-always-on-context.md` → `0`.
  It is cited only by `client-frontmatter-and-discovery-divergence.md:5` and
  `client-loading-and-distribution-models.md:6`, so it is outside this round's theme.
- The staged quote is the **22-word derived form** (parentheticals elided, 0 raw matches). Appending
  it as a quote cell would create a quote no literal gate can locate.
- Duplicate URL: the lane already holds this page as `S206`, tier **A** (staged row is tier **B**):

```
$ sed -n '147p' corpus/SOURCES.md
| S206 | Junie — Agent Skills — https://junie.jetbrains.com/docs/agent-skills.html | docs | A | … | the "Skill location" section, the sentence on project-level and user-level skills sharing a name; quote "the project-level skill takes precedence and the user-level skill is ignored." (11 words) | … | mined | 2026-10-25 | 90d | corpus/knowledge/skill-name-precedence-round69.md |
```

  S206's 11-word quote is byte-exact present 1× in today's bytes (table above), and its anchor
  `the "Skill location" section` is the h3 I located.

## 5. Disposition

1. Row 4 is **not** a fabrication row: the register's `payload-absent` reason ("the quote is in none
   of them") is falsified by the cited source itself. Record the cause as register-side truncation +
   inline-code elision, not an absent payload.
2. **Adopt** only the byte-exact 16-word tail, anchor `Skill location` / note box `Scope priority`.
   Do not adopt the 22-word parenthetical-stripped form as a quote (0 raw matches).
3. No new registry row is needed for this substance: `S206` already carries it at tier A, mined,
   with the same page. Adopting `S252` would add a duplicate URL (census W04 class) and a duplicate
   claim.
4. If the L1 wants the register's literal 5-word fragment repaired, the honest repair is to the
   16-word contiguous tail above, with the fold named — never to the register's truncated string.

## 6. Risks and unknowns

- Only the served HTML was probed; no JS-rendered or A/B edge variant was sampled. The page ships
  its prose in the served bytes (the sentence is in the static HTML, not a script payload), and
  `ETag "6adbaaca-966d"` / `Last-Modified 2026-10-23` match the body length, so the probe is on real
  content.
- Wayback cross-check is one snapshot (`20260909095632`), older than the page's `Last-Modified`; it
  proves the sentence pre-dates the current bytes, not that every intermediate revision carried it.
- Round 69's `ScoutQuarantine.md` calls the anchor an "h2 at raw offset 12 825"; the bytes are an
  `<h3 id="skill-location">` at that offset. Anchor name and offset agree, tag level does not — I
  recorded the bytes, not the earlier report.
- The `.md` export does not exist (404), so there is no canonical markdown to test whitespace folds
  against; the whitespace collapse in my fold test is applied to tag-stripped HTML text.

## 7. Bounds observed

- No installs, no pacman, no `jj`, no git writes. Read-only `git`/`awk`/`diff`/`grep`/`curl` only.
- Wrote only: this report, `build/ExecQuar04/` (two fetched snapshots + shas), and `/tmp` scratch
  (`/tmp/k72w1-junie*`, deleted before return).
- No committed lane file, no fleet repo file, no `/home/vgpnk/Projects/shokuknow` file modified.
