# ExecSrcVercel — round 72 wave 1: open S248 (Vercel AGENTS.md eval) and hand-check S168

## Verdict

**S248 is confirmed and adoptable.** The page is live (`HTTP 200`, no redirect), every figure the
staged row and its two citing entries assert is located verbatim on it (56% non-invocation, 53/53/79/100%
pass rates, +0/+26/+47pp, 40KB→8KB / 80% reduction), and the source publishes a **byte-stable `.md`
export** — the form to pin. **S168 is an anchor defect, not a source defect**: its registered quote is the
one-word fragment `section:`, which occurs **0 times** in the rendered page text, the `.md` export *and*
the 901 KB raw HTML; the URL itself is fully reachable and carries the S248 quotes. Two entry-level
defects found: `skill-invocation-is-the-bottleneck.md` says the explicit instruction "recovers two-thirds
of the gap" where the page's own numbers give **55.3%** (26/47), and the S248 `used-by` cell omits the
amendment entry that cites S248 by id. One integration hazard: the **HTML** export is not byte-stable
across requests — pinning it would make a sha256 check flaky on a healthy source.

## Fetch evidence (access date 2026-10-25, all UTC)

Scratch: `mktemp -d /tmp/k72w1-ExecSrcVercel.XXXX` → `/tmp/k72w1-ExecSrcVercel.SjII` (deleted before return).

Rendered page:

```
$ curl -fsSL -A 'Mozilla/5.0' -w 'HTTP %{http_code} FINAL %{url_effective} SIZE %{size_download} TYPE %{content_type}\n' \
    'https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals' -o page.html
HTTP 200 FINAL https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals SIZE 901177 TYPE text/html; charset=utf-8
$ sha256sum page.html
afcb3de65015ad5aca7ff826a24bc19717bd80bb122da39a36d8039bc7ef5e37  page.html
```

Markdown export (exists — `text/markdown`, not an HTML rendering):

```
$ curl -sS -A 'Mozilla/5.0' -w '\nHTTP %{http_code} FINAL %{url_effective} SIZE %{size_download} TYPE %{content_type}\n' \
    'https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals.md' -o page.md
HTTP 200 FINAL https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals.md SIZE 11843 TYPE text/markdown; charset=utf-8
$ sha256sum page.md
d9c8dbd5cd080dab56554be7069eeecb8c7d357e2d7366a1ed9add10f91464dc  page.md
```

Byte-stability probe (second fetch of each, ~60 s later):

```
$ sha256sum page.md page2.md page.html page2.html
d9c8dbd5cd080dab56554be7069eeecb8c7d357e2d7366a1ed9add10f91464dc  page.md
d9c8dbd5cd080dab56554be7069eeecb8c7d357e2d7366a1ed9add10f91464dc  page2.md
afcb3de65015ad5aca7ff826a24bc19717bd80bb122da39a36d8039bc7ef5e37  page.html
25ea84d45f7eefbe9e78184a8bdec5778712de29231f8a92fe5e1d49272ca12c  page2.html
$ cmp page.md page2.md && echo 'MD IDENTICAL'; cmp page.html page2.html || echo 'HTML DIFFERS'
MD IDENTICAL
page.html page2.html differ: char 8622, line 1
```

The HTML delta is per-request chrome: a `<meta name="initiator-trace" …>` element, a
`data-flag-values` JSON blob that differs on every render, and renumbered React hydration ids
(`"139:…"` → `"13a:…"`). Body text is unchanged. **`page.md` is byte-identical; `page.html` is not.**

Headers / canonical:

```
$ curl -sSI -A 'Mozilla/5.0' '<url>' | grep -i '^HTTP/\|^etag\|^content-type\|^cache-control\|^age'
HTTP/2 200
age: 35
cache-control: public, max-age=0, must-revalidate
content-type: text/html; charset=utf-8
etag: "bcg8h47ch9jbgu"
$ grep -o '<link rel="canonical" href="[^"]*"' page.html
<link rel="canonical" href="https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals"
```

Byline: `**Published:** January 27, 2026 | **Authors:** Jude Gao` (`page.md:3`), closing
`*Research and evals by *[*Jude Gao*]…` (`page.md:195`) — the row's "post by Jude Gao (Vercel)" is
correct.

## Snapshots committed (only writes outside my report/build dir)

| path | bytes | sha256 | pinned |
|---|---|---|---|
| `.ufo/waves/round-72/snapshots/S248-vercel-agents-md.md` | 11 843 | `d9c8dbd5cd080dab56554be7069eeecb8c7d357e2d7366a1ed9add10f91464dc` | **yes** — `.ufo/waves/round-72/snapshots/S248.sha256` |
| `.ufo/waves/round-72/snapshots/S248-vercel-agents-md.html` | 901 177 | `afcb3de65015ad5aca7ff826a24bc19717bd80bb122da39a36d8039bc7ef5e37` | **no — deliberately unpinned** (not reproducible; see probe) |

Pin verifies: `cd .ufo/waves/round-72/snapshots && sha256sum -c S248.sha256` →
`S248-vercel-agents-md.md: OK`. Sidecar format copied from the sibling `S262.sha256`
(`<sha256>  <filename>`), but with the HTML line omitted for the reason above.

The `.md` is a **complete** text export, not an excerpt: 198 lines, all 11 `##` sections from
`The problem we were trying to solve` (`:13`) to `What this means for framework authors` (`:178`),
both code blocks, both results tables, both image captions.

## Located sentences — staged row S248

Snapshot line numbers are lines of `S248-vercel-agents-md.md`; quotes are pasted from
`sed -n '<L>p' <snapshot>`.

| # | quoted item (as registered) | located | heading | line | verbatim | dropped bytes |
|---|---|---|---|---|---|---|
| 1 | `Skills weren't being triggered reliably` | **yes** | `## **Skills weren't being triggered reliably**` | 36 | `## **Skills weren't being triggered reliably**` (heading markup `## **`/`**`) | none — 5-word heading text |
| 2 | `In 56% of eval cases, the skill was never invoked.` | **yes** | same | 38 | `In 56% of eval cases, the skill was never invoked.` (10 words) | tail of the same line: ` The agent had access to the documentation but didn't use it. Adding the skill produced no improvement over baseline:` |
| 3 | `A compressed 8KB docs index embedded directly in `AGENTS.md` achieved a 100% pass rate, while skills maxed out at 79%` | **yes, truncated** | lead paragraph (before the first `##`) | 9 | `A compressed 8KB docs index embedded directly in `AGENTS.md` achieved a 100% pass rate, while skills maxed out at 79%` (20 words) | tail of the same line: ` even with explicit instructions telling the agent to use them. Without those instructions, skills performed no better than having no documentation at all.` — **material**: 79% was reached *only* with the explicit instruction |
| 4 | `53/53/79/100%` and `+0pp/+26pp/+47pp` | **yes** | `## **The results surprised us**` | 118–122 (interim tables at `:40–42` and `:59–62`) | `\| **`AGENTS.md`**** docs index** \| **100%** \| **+47pp** \|` and `\| Skill with explicit instructions \| 79% \| +26pp \|`, `\| Skill (default behavior) \| 53% \| +0pp \|`, `\| Baseline (no docs) \| 53% \| — \|` | table pipes/emphasis retained; nothing semantic dropped |
| 5 | `40KB→8KB` compression | **yes** | `## **Addressing the context bloat concern**` | 146 | `The initial docs injection was around 40KB. We compressed it down to 8KB (an 80% reduction) while maintaining the 100% pass rate.` (22 words) | tail of the same line: ` The compressed format uses a pipe-delimited structure that packs the docs index into minimal space:` |

Supporting sentences also located for the entries (same snapshot):

- `:44` — `…the skill actually performed worse than baseline on some metrics (58% vs 63% on tests)…`
  (quote `the skill actually performed worse than baseline on some metrics (58% vs 63% on tests)`,
  15 words; dropped prefix `Zero improvement. The skill existed, the agent could use it, and the agent
  chose not to. On the detailed Build/Lint/Test breakdown, ` and suffix `, suggesting that an unused
  skill in the environment may introduce noise or distraction.`)
- `:57` — `This improved the trigger rate to 95%+ and boosted the pass rate to 79%.` (14 words, whole
  line, nothing dropped)
- `:129–130` — Build/Lint/Test table: `| Skill with explicit instructions | 95% | 100% | 84% |`,
  `| **`AGENTS.md`** | **100%** | **100%** | **100%** |`; baseline row `| Baseline | 84% | 95% | 63% |` at `:127`.

Occurrence check (word-bounded, whole snapshot):

```
$ python3 -c … (count per quote)
Q1 count= 1 words= 10 first_occ= 38
Q2 count= 1 words= 20 first_occ= 9
Q3 count= 1 words= 14 first_occ= 57
Q4 count= 1 words= 22 first_occ= 146
Q5 count= 1 words= 15 first_occ= 44
Q6 count= 1 words= 5  first_occ= 36
Q8 count= 1 words= 9  first_occ= 122
```

All row quote cells are inside the plan's 5–25-word window (10 and 20 words); the heading anchor is 5.

## Which form the quote lives in

Both. The `.md` carries the **backticked** form (`embedded directly in `AGENTS.md``, `page.md:9`); the
rendered page renders that span as a `<code>` element, so its extracted text splits the sentence into
`A compressed 8KB docs index embedded directly in` / `AGENTS.md` / `achieved a 100% pass rate, …`
(`page.txt:120–122`). A literal backtick-bearing quote therefore matches only the `.md`; the word
sequence matches both. `In 56% of eval cases, …` and `The initial docs injection was around 40KB. …`
are single text nodes in both forms.

## Claim verdicts

### Staged row S248 (`SOURCES.append.md:52`, 11 cells — verified by pipe count `cells= 11`)

| claim in the row | verdict |
|---|---|
| section `Skills weren't being triggered reliably` | **confirmed** (`.md:36`) |
| quote `In 56% of eval cases, the skill was never invoked.` | **confirmed** (`.md:38`) |
| quote `A compressed 8KB docs index … while skills maxed out at 79%` | **confirmed-after-shaping** — verbatim prefix; the qualifier `even with explicit instructions telling the agent to use them` is dropped without an ellipsis |
| four-configuration table, `53/53/79/100`, `+0/+26/+47pp` | **confirmed** (`.md:118–122`) |
| `40KB→8KB` compression | **confirmed** (`.md:146`) |
| `post by Jude Gao (Vercel)` | **confirmed** (`.md:3`, `:195`) |
| `retrieved 2026-10-23` / `recheck … (ran 2026-10-23)` | **self-attestation, not re-verifiable**; I re-ran it today (2026-10-25) and every figure is unchanged |
| status `mined`, tier `B` | as registered; tier rationale (one team's eval, one framework, one setup) is consistent with `.md:180` ("Skills aren't useless… Skills work better for vertical, action-specific workflows") |

### Entry `corpus/knowledge/skill-invocation-is-the-bottleneck.md`

| claim | verdict |
|---|---|
| `"In **56% of eval cases, the skill was never invoked**. The agent had access to the documentation but didn't use it."` | **confirmed** (`.md:38`; bold is the entry's) |
| `baseline (no docs) 53%`, `skill with default behaviour 53% — +0pp`, `79% (+26pp)`, `100% (+47pp)` | **confirmed** (`.md:60–62`, `118–122`) |
| `On the Build/Lint/Test breakdown the skill was even worse than baseline on one metric (58% against 63% on tests)` | **confirmed-after-shaping** — page: `worse than baseline on some metrics (58% vs 63% on tests)`; `some`→`one` is a narrowing the single cited metric supports |
| `This improved the trigger rate to 95%+ and boosted the pass rate to 79%.` | **confirmed**, literal (`.md:57`) |
| `an initial docs injection of about 40 KB compressed to 8 KB — an 80% reduction — while holding the 100% pass rate` | **confirmed-after-shaping** — page: `around 40KB` / `compressed it down to 8KB (an 80% reduction) … maintaining the 100% pass rate` |
| `Telling the agent to use the skill recovers two-thirds of the gap — 53% to 79%` | **absent as a source statement; the entry's own arithmetic is wrong.** `grep -c "two-thirds\|two thirds" snapshot` → `0`; `grep -in recover` → no line. The page's numbers give 26/47 = **55.3%**, not 66.7%. Fix the prose or drop the fraction |
| `Vercel built an eval suite on Next.js 16 APIs that postdate the models' training cutoff` | **confirmed** (`.md:7` "After building evals focused on Next.js 16 APIs"; `.md:82` "tests targeting Next.js 16 APIs that aren't in model training data") |

### Entry `corpus/knowledge/context-rot-and-always-on-context.md` (S248-citing parts only)

| claim | verdict |
|---|---|
| source anchor `` `# Skills weren't being triggered reliably` `` | **confirmed** (`.md:36`) |
| `Vercel's eval says an always-on `AGENTS.md` index beats an on-demand skill decisively (100% against 53% or 79%)` | **confirmed** (`.md:118–122`) |
| `40 KB down to 8 KB, an 80% reduction, with the 100% pass rate intact` | **confirmed-after-shaping** (same paraphrase as above) |
| `56% in Vercel's eval` | **confirmed** (`.md:38`) |

### Entry `corpus/knowledge/skill-vs-always-on-boundary.md` — uncited dependency

Line 20 reads `Round 5's Vercel eval put numbers on the comparison the ladder implies: a compressed
always-on index reached 100% where a skill reached 53% without an instruction to use it and 79% with
one.` Numbers **confirmed** against `.md:118–122`. But its `source:` lines name only S261–S264 — no
S248 — while the S248 row's `used-by` cell lists only
`skill-invocation-is-the-bottleneck.md, context-rot-and-always-on-context.md`. The entry uses S248's
figures without citing the row, and the row does not list the entry: the two records disagree.

## Quarantine hand-check — S168 (same URL)

Register row, verbatim (`/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md:110`):

```
| `kotoba` | round5 | S168 | `payload-absent` | https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals | `section:` | cited source, companion URLs and local artifacts were all checked; the quote is in none of them |
```

The registered quote is the fragment `section:` — 1 word, ending in a colon, with no continuation line
(the neighbouring S172/S176 rows do wrap onto following lines; this one does not). Search of today's
bytes:

```
$ grep -c "section:" page.md page.txt page.html
page.md:0
page.txt:0
page.html:0
$ grep -o "section" page.html | wc -l
15
```

So the span is absent from the rendered text, the `.md` export **and** the raw HTML — the r68 seat's
explicit caveat ("this fetch returned extracted main text, not raw HTML, so a match inside markup
attributes cannot be excluded with my toolset", `.ufo/waves/round-68/w1/logs/ScoutQuarantine1.log`)
is now closed in the same direction: still absent.

**Verdict on the two S168 claims, separately:**
1. *The registered quote is absent from the cited source* — **confirmed** (`section:` 0 occurrences
   anywhere in the fetched bytes). The row's `payload-absent` class is literally right.
2. *That this makes the source a fabrication* — **not supported.** The class is an artifact of a
   truncated quote cell (the campaign generator leaking/losing the cell, the same defect the r68 log
   found in S151 and S167). The source is fully reachable today and its S248 quotes all locate. Do not
   carry S168 forward as a refused *source*; carry it as a refused *anchor*, and let S248 stand on the
   same URL with the located quotes above.

## URL surface for duplicate detection

- Host + path: **`vercel.com` + `/blog/agents-md-outperforms-skills-in-our-agent-evals`** (canonical
  tag agrees; no redirect, no trailing slash, no query).
- Lane registry at base `c69711e`: **0 rows** mention `vercel.com` (`grep -c "vercel.com" corpus/SOURCES.md`
  → `0`), 139 data rows, tail ids `S211`, `S212`, `S213` — **S248 is a free id and a new host**.
- Same URL elsewhere in the lane: exactly one place, `corpus/lessons/round-68.md:103` (the S168 refusal
  line). Staged package: exactly one row (`SOURCES.append.md:52`). Register: exactly one row (S168).
- Consequence: appending S248 will **not** trip the census W04 duplicate-URL check (the lane registry
  has no row for the URL), but the r68 lesson will then hold a refusal and the registry an adoption of
  the same URL under two ids. The lesson must record that S168 was an anchor defect — otherwise the
  next quarantine pass re-refuses the URL S248 depends on.

## Risks / notes for the L1

1. **Pin the `.md`, never the `.html`.** Two consecutive HTML fetches differ (`901177` vs `901400`
   bytes, different sha256) on per-request chrome; the `.md` is byte-identical. A sha256 pin on the
   HTML would fail on a healthy source. `S248.sha256` contains the `.md` line only.
2. **The HTML snapshot (901 KB) is unpinned evidence, not a pin.** It exists so the `section:`-in-raw-
   HTML check above is re-runnable. Drop it if the committed tree's size matters more than that check.
3. **`used-by` cell is incomplete.** `client-implementation-loading-model-amendment-2026-10-23.md:42`
   cites `Vercel's eval (round 5, S248)` by id; `skill-vs-always-on-boundary.md` uses the figures with
   no id. Either add both paths to cell 11 or make the boundary entry cite S248 in a `source:` line.
4. **"two-thirds" is wrong** (55.3%). It contradicts the entry's own `+26pp` / `+47pp` cells.
5. **Quote-cell truncation without an ellipsis** (row quote 3) drops the qualifier that makes 79% the
   *with-instruction* result. The full sentence is 30 words, so it does **not** fit the plan's C1(d)
   window (5–25); the fit-and-honest forms are the registered 20-word prefix with an explicit `…`
   marker, or the 24-word contiguous cut ending `…while skills maxed out at 79% even with explicit
   instructions`.
6. No credential material, session URL or `op://` reference was read or written. No tool installed.
   No lane file, index, jj state or sibling repo was modified; the only writes are the two snapshot
   files, the pin sidecar and this report.
