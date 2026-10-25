# ExecQuar07 — quarantine hand-check, register slice row 7 of 13

**Verdict: `absent`.** Register row 7 (`round6 | S185 | payload-absent | https://docs.roocode.com/features/skills | Skill locations`) **holds** — the quoted span does not occur in the cited URL's served bytes, nor in any of the three archived content snapshots I opened. **Do not adopt.** Staged id for the URL: **S265** (`/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md:69`) — and that staged row carries **the same bad anchor** ("the \"Skill locations\" section"), so the anchor must be re-pointed before S265 is ever appended; its payload quote, by contrast, *is* present (see §4).

## 1. Register row, as read

`.ufo/waves/round-72/assimilation/quarantine-slice-full.txt:7`

```
| `kotoba` | round6 | S185 | `payload-absent` | https://docs.roocode.com/features/skills | `Skill locations` | cited source, companion URLs and local artifacts were all checked; the quote is in none of them |
```

Quoted span under test: `Skill locations` (15 characters, no trailing punctuation).

## 2. Staged row lookup (by URL host+path)

```
$ grep -rn -i 'roocode' /home/vgpnk/Projects/shokuknow/merge/kotoba
./SOURCES.append.md:69:| S265 | Roo Code Documentation — Skills — https://docs.roocode.com/features/skills | docs | B | ... | the "Skill locations" section; quote "Roo-specific (higher priority)"; also the scope line "Project skills override global skills, mode-specific override generic" | ...
./knowledge/corpus/knowledge/skill-paths-and-precedence.md:6:source: S265 — https://docs.roocode.com/features/skills — the "Skill locations" section — retrieved 2026-10-23
```

**Staged id: `S265`** (`SOURCES.append.md:69`). Its `source:` line is repeated in the staged knowledge entry `knowledge/corpus/knowledge/skill-paths-and-precedence.md:6`. Both attribute the content to a **"Skill locations" section that the page does not have**.

The lane's own committed id for the same URL is different: `corpus/SOURCES.md:144` → **S203**, anchored to "the \"What Skills Let You Do\" section" — that anchor *is* correct (see §4). So the lane already holds a sound row for this page; S265 is the staged duplicate and is the one carrying the bad anchor.

## 3. Fetch — cited URL

```
$ curl -fsSL -A 'Mozilla/5.0' -o /tmp/k72q07-roocode.html -w 'status=%{http_code} final=%{url_effective} size=%{size_download}\n' 'https://docs.roocode.com/features/skills'
status=200 final=https://roocodeinc.github.io/Roo-Code/features/skills/ size=71129
$ sha256sum /tmp/k72q07-roocode.html
fe801910f82e07631b3b5af3a2349fd75950eaabeda0280348b51c1aa92753e2  /tmp/k72q07-roocode.html
$ date -u +%FT%TZ
2026-10-25T21:37:00Z
```

Access date **2026-10-25**, HTTP **200**, final URL `https://roocodeinc.github.io/Roo-Code/features/skills/`, **71,129 bytes**, sha256 `fe801910f82e07631b3b5af3a2349fd75950eaabeda0280348b51c1aa92753e2`.

Redirect chain (the docs domain moved to GitHub Pages):

```
$ curl -sS -A 'Mozilla/5.0' -o /dev/null -D - -w 'num_redirects=%{num_redirects}\n' 'https://docs.roocode.com/features/skills'
HTTP/2 301
location: https://roocodeinc.github.io/Roo-Code/features/skills
```

`.md` export attempt (the assignment's alternate form) does not exist for this host:

```
$ curl -fsSL -A 'Mozilla/5.0' -o /tmp/k72q07-roocode.md -w 'status=%{http_code} final=%{url_effective} size=%{size_download}\n' 'https://docs.roocode.com/features/skills.md'
curl: (22) The requested URL returned error: 404
status=404 final=https://roocodeinc.github.io/Roo-Code/features/skills.md size=0
```

## 4. Span location attempt

**Live bytes — 0 hits, exact and case-insensitive, raw HTML and tag-stripped text.**

```
$ grep -c 'Skill locations' /tmp/k72q07-roocode.html
0
$ grep -c -i 'skill locations' /tmp/k72q07-roocode.html
0
$ sed -e 's/<[^>]*>//g' /tmp/k72q07-roocode.html > /tmp/k72q07-roocode.txt   # 13937 bytes, sha256 f6d2e9f0…
$ grep -c -i 'skill locations' /tmp/k72q07-roocode.txt
0
$ grep -n -i 'locations' /tmp/k72q07-roocode.txt | cut -c1-300
76:When skills with the same name exist in multiple locations, this priority applies (highest to lowest). .roo/ paths always take precedence over .agents/ paths at the same project level:
172:Roo-specific locations: .roo/skills/, ~/.roo/skills/ (higher priority)
173:Cross-agent locations: .agents/skills/, ~/.agents/skills/ (shared with other agent tools)
```

The word `locations` occurs on exactly three lines of the whole served document and is never preceded by `Skill`. No anchor id matches either:

```
$ grep -o 'id="[^"]*skill[^"]*"' /tmp/k72q07-roocode.html
id="what-skills-let-you-do" … id="mode-specific-skills" … id="skill-discovery" … id="skill-loads-but-doesnt-help" … id="skills-vs-custom-instructions-vs-slash-commands" … id="skill-specification"
```

**Full heading inventory of the page** (`grep -o '<h[1-4][^>]*>[^<]*'`), which is the set a section-anchor quote must come from:

```
h1 Skills
h2 Why It Matters | What Skills Let You Do | How Skills Work | Creating Your First Skill
h4 1. Choose a location | 2. Create the skill directory and file | 3. Write the SKILL.md file | 4. Test the skill
h2 Directory Structure | Override Priority | Skill Discovery | Troubleshooting
h4 Basic structure | Mode-specific skills | Symlink support | Skill isn't loading | Skill loads but doesn't help
   | Multiple skills conflict | Can't share skills with team
h2 Skills vs Custom Instructions vs Slash Commands | Skill Specification | See Also
h4 Roo-specific enhancements
```

There is **no `Skill locations` heading**. The nearest heading is `1. Choose a location` (h4) — a singular noun inside a step title, not the phrase.

**Archived snapshots — 0 hits in every content state I could open.** CDX inventory first:

```
$ curl -fsSL -A 'Mozilla/5.0' 'http://web.archive.org/cdx/search/cdx?url=docs.roocode.com/features/skills&output=json&fl=timestamp,original,statuscode,digest&collapse=digest&limit=40'
["20260101234333", …, "200", "UFW5R33U4JYTYQYWW5G6UFWDB6NRBNKS"]
["20260115183009", …, "200", "AB3HRZTJYV4L67HVAY3MEARITNNPGQFK"]
["20260117172126", …, "200", "LAQVIAGULY3A2UA2KSYLRXON3RGUD3TB"]
["20260221201028", …, "200", "47A76S6GF252SMZK4JKQ2LXGTFHGFCZW"]
["20260411150854", …, "200", "HG3GDCVWBMKG64NENXHCOR2NV3E2ZQWU"]
["20260620122805", …, "301", "OQ3OBNFR7DBCFQ4ANGEQW5P2FOXZZJRA"]
```

Three opened with `id_` (raw capture), each grepped for `skill locations` case-insensitively:

| capture | transport | bytes | sha256 (content) | `skill locations` hits |
|---|---|---|---|---|
| 20260101234333 | gzip (18,694 B raw) | 78,610 B gunzipped | `3a1967f542a3d55f4675daa5a6030a00b59d1a08da5da935f8b4845a951c8fcf` | **0** |
| 20260221201028 | gzip (18,761 B raw) | 81,576 B gunzipped | `1e09e4f0f8017efd8bdbc2d3e121eafea989ec28c5d6c59805e2545991708750` | **0** |
| 20260411150854 | plain | 81,576 B | `1e09e4f0f8017efd8bdbc2d3e121eafea989ec28c5d6c5985e2545991708750` | **0** |

The 2026-02-21 and 2026-04-11 captures are **byte-identical** (same sha256 `1e09e4f0…`), so the effective content states are two archived plus live. The 2026-01-01 and 2026-02/04 heading sets are identical to the live one quoted above (same h2/h4 list, only the CSS-module hash suffix differs: `anchorTargetStickyNavbar_Vzrq` / `_sDfD` / `_ZB1J`), and neither contains `Skill locations`. The last capture, `20260620122805`, is the **301** that produced the live redirect, so it has no body to quote.

**Folds tested and named** (none rescues the phrase):

- case fold (`Skill Locations`, `skill locations`) — 0 hits, live and both archived states.
- whitespace/markdown fold (heading split by inline markup, e.g. `Skill <code>locations</code>`) — the tag-stripped text is 13,937 B and holds 0 hits, so no split variant exists.
- `_`/`-` id fold (`#skill-locations`) — no such anchor id on the page.
- *Rejected as a fold:* `Skill locations` → `1. Choose a location`. This is a different string (plural→singular, noun phrase→step title), not case/whitespace/markdown. It is a near-miss anchor, not an admissible fold; I do not count it.

## 5. What the page *does* say (so the row's payload is not lost, only mis-anchored)

Both quoted spans in the **staged** S265 row are present in the live bytes, under different anchors:

```
$ sed -n '40p' /tmp/k72q07-roocode.txt | cut -c1-160
# Linux/macOS — Roo-specific (higher priority)~/.roo/skills/{skill-name}/SKILL.md# Linux/macOS — cross-agent (shared with other agent tools)~/.agents/ski
$ sed -n '42p' /tmp/k72q07-roocode.txt | cut -c1-160
# Roo-specific (higher priority)&lt;project-root&gt;/.roo/skills/{skill-name}/SKILL.md# Cross-agent (shared with other agent tools)&lt;project-root&gt;/.agen
$ sed -n '28p' /tmp/k72q07-roocode.txt | cut -c1-200
Override Control: Project skills override global skills, mode-specific override generic
$ sed -n '76p' /tmp/k72q07-roocode.html | cut -c1-300
<p>When skills with the same name exist in multiple locations, this priority applies (highest to lowest). <code>.roo/</code> paths always take precedence over <code>.agents/</code> paths at the same project level:</p>
$ sed -n '172p' /tmp/k72q07-roocode.html | cut -c1-300
<li class=""><strong>Roo-specific locations</strong>: <code>.roo/skills/</code>, <code>~/.roo/skills/</code> (higher priority)</li>
```

Correct anchors for S265, if the L1 ever lands it: **`Override Priority`** (h2, `#override-priority`; precedence paragraph at HTML line 76, text line 28 carries the scope quote) and **`Roo-specific enhancements`** (h4, `#roo-specific-enhancements`, HTML line 169; the `Roo-specific locations … (higher priority)` bullet at HTML line 172). The exact string `Roo-specific (higher priority)` appears only inside the bash code blocks at HTML lines 40 and 42 — both of which are the comment lines of the location listings, which is where the staged row's quote actually comes from.

Note for calibration: the phrase **`Skill locations` is a real heading on a *sibling* page** — Junie, `https://junie.jetbrains.com/docs/agent-skills.html` (200, 38,509 B, sha256 `b3c676900e3de8a0d34754bb223685e1734c95ecc635280d8b8b159928f5a915`, fetched 2026-10-25):

```
$ grep -o 'id="skill-locations"[^>]*>[^<]*' /tmp/k72q07-junie.html
(no output — the id is skill-locations-and-configuration)
$ sed -n '67p' /tmp/k72q07-junie.html | cut -c1-200
… data-toc="skill-locations-and-configuration">Skill locations and configuration</h2><p id="-jqc5nu_196">By default, Junie
```

Junie's heading is `Skill locations and configuration` — so even there the bare phrase is not a heading, only a prefix. That is consistent with the register's own separate S172 row for Junie and is *out of my slice*; I record it only because it is the cheapest available explanation of where the phrase could have been transposed from. goose (`S266`, `SOURCES.append.md:70`) also claims a "Skill Locations" section — I did not open goose, so that stays **unobserved** here.

## 6. Verdict and disposition

- **`Skill locations` → absent** (payload-absent confirmed; not fabrication-class on my side — I did not have to invoke it, the source fetched fine with 200, so `unreachable` and `unverifiable-class` do not apply).
- Register row 7 **stands as written**; nothing to adopt. If the register's `payload-absent` class means "refuse as fabrication", the refusal is correct on the evidence: the phrase exists in **no** byte I fetched from that URL, in three content states spanning 2026-01-01 → 2026-10-25.
- **Actionable defect found next door (staged, not committed):** `SOURCES.append.md:69` (S265) and the staged knowledge header `knowledge/corpus/knowledge/skill-paths-and-precedence.md:6` both cite a "Skill locations" section that does not exist. If S265 is appended in wave 2, its anchor must be rewritten to `Override Priority` + `Roo-specific enhancements` (§5). The lane's committed `corpus/SOURCES.md:144` (S203) is already anchored correctly to "What Skills Let You Do" and needs no change.
- No committed lane file was touched; no gate was run (my item is a hand-check, and the L1 owns gates). Nothing installed, nothing upgraded. All scratch lived under `/tmp/k72q07-*` and was deleted before return.

### Retained evidence (re-fetchable)

| artifact | how to reproduce | sha256 |
|---|---|---|
| live page | `curl -fsSL -A 'Mozilla/5.0' https://docs.roocode.com/features/skills` | `fe801910f82e07631b3b5af3a2349fd75950eaabeda0280348b51c1aa92753e2` |
| live page, tag-stripped | `sed -e 's/<[^>]*>//g'` on the above | `f6d2e9f0f7a8fac3acc0caabda7de1bed39fd37d4bdc274191a893b3aaab9c9f` |
| capture 2026-01-01 (gunzipped) | `curl -fsSL 'https://web.archive.org/web/20260101234333id_/https://docs.roocode.com/features/skills' \| gunzip` | `3a1967f542a3d55f4675daa5a6030a00b59d1a08da5da935f8b4845a951c8fcf` |
| capture 2026-02-21 (gunzipped) = capture 2026-04-11 (plain) | `…/20260221201028id_/…` gunzipped; `…/20260411150854id_/…` as-is | `1e09e4f0f8017efd8bdbc2d3e121eafea989ec28c5d6c5985e2545991708750` |
| Junie page (out-of-slice corroboration) | `curl -fsSL -A 'Mozilla/5.0' https://junie.jetbrains.com/docs/agent-skills.html` | `b3c676900e3de8a0d34754bb223685e1734c95ecc635280d8b8b159928f5a915` |

### Risks / limits

- Only three of the five `200` captures were opened; `20260115183009` and `20260117172126` were not, because their CDX digests differ from each other and from the ones I opened. Residual risk that the phrase appeared in a narrow window between 2026-01-01 and 2026-02-21 and vanished — low, since the heading set is stable across both endpoints I did open, and the register's own claim is that the *cited source* holds no such quote today.
- I did not check the page's client-side search index or any Roo "llms.txt" export as a companion artifact: `https://roocodeinc.github.io/Roo-Code/llms.txt` and `/llms-full.txt` both return **404** (15,599 B 404 body, 0 hits) and `https://docs.roocode.com/llms.txt` returns **301** to the same host, so no text export exists to cross-check.
- Verdict is a statement about bytes I fetched on 2026-10-25, not about the page as of round 6.
