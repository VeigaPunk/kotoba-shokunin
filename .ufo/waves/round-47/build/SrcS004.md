verdict: still-holds — S004's anchor and teaches cell are confirmed verbatim on the live page (HTTP 200, 2026-10-21T15:54:15Z); no status/recheck/used-by change is warranted, but the raw-byte hash is a bad freshness oracle for this page.

## Row at BASE

`corpus/SOURCES.md:17` (BASE c61a973b2e02e1ded169703ddcb06466f4edd8bd):

| field | value |
|---|---|
| source | AGENTS.md — open format site — https://agents.md/ |
| kind / tier | spec / A |
| scope | Always-on context-file precedence convention |
| anchor | § FAQ "What if instructions conflict?"; live page opened 2026-10-19 |
| teaches | Conflict rule for always-on files: the closest AGENTS.md to the edited file wins and explicit user chat prompts override everything |
| status / opened / recheck / used-by | queued / 2026-10-19 / 90d / — |

Shape check at BASE: `awk -F'|' ... NF=13` (exit 0); duplicate-id sweep over `corpus/SOURCES.md` printed nothing (exit 0). Worktree tracked files are clean; only untracked `.ufo/waves/` and `plans/round-47.md` exist.

## Fresh re-open (observed)

Access time **2026-10-21T15:54:15Z** (`date -u` at 15:54:09Z; file mtime 15:54:15Z).

```
curl -sS -L -D hdr.txt -o agents.md.html https://agents.md/   # exit 0
http_code=200 size=81690 remote_ip=64.239.109.1
sha256 b0a63496f7c71419d2df378246ce9e7fe4501a849818a941cc7f424c0559125b
etag "27xowvmrnt1r0m" · server Vercel · server Date: 2026-10-20T19:00:00Z
x-vercel-cache: HIT · age: 75254s · content-type text/html; charset=utf-8
```

The response is a Vercel edge cache entry generated 2026-10-20T19:00Z, ~20.9 h before access. Three repeats — `Cache-Control: no-cache` (15:54:51Z), a browser UA (15:59:28Z), and a cache-busted `?r47probe=1` (15:59:28Z) — all returned 200/81690 bytes and were byte-identical (`cmp` exit 0; still `x-vercel-cache: HIT`, same ETag). Metadata only was saved to the lane; the body lives in `/tmp/s004probe/`.

## Anchor and teaches: still hold

- **Anchor section present.** `What if instructions conflict?` appears exactly **once** in the raw HTML as an `<h3>` under the FAQ list. It carries **no fragment id**, so the row's `§ FAQ "..."` is a textual section reference, and that is what the page still supports.
- **Quote (14 words), exact location: FAQ section, heading "What if instructions conflict?", first answer sentence** (raw-HTML char offset 66467, single occurrence):
  > The closest AGENTS.md to the edited file wins; explicit user chat prompts override everything.
- The row's `teaches` cell matches that sentence without overreach: it adds nothing about global/user-level AGENTS.md files, which the page also does not define.
- Adjacent claim, consistent not contradictory: How-to § 4 says "Agents automatically read the nearest file in the directory tree, so the closest one takes precedence".
- Tier/kind still fit: the site is the open format's own page (signature-free, vendor-neutral), not a secondary write-up.

**Upstream corroboration** (independent of the rendered page): `git ls-remote` → HEAD `d001185d792eb6402a58e4cbef1c228b309ec25d` (2026-09-10); shallow clone (exit 0, 38 commits, root `ba9474a` 2025-08-19) places the sentence in `components/FAQSection.tsx:18-20`, and `git log -S'The closest AGENTS.md to the edited file wins'` returns **only** the 2025-08-19 initial commit. The taught sentence has therefore been unchanged for ~14 months, across a repo whose HEAD predates round 46. The "stewarded by the Agentic AI Foundation" note (`components/AboutSection.tsx:23`) arrived 2025-12-11, so it is not drift since the row was written.

## Counterexample: raw hash differs while content does not

Round-46 recorded `e3a5b9a4825ed894447dec3dbd96b8d73f1aa84dce19a1964642d63e2c3c9c75` (`corpus/lessons/round-46.md:66`, `.ufo/round-46/evidence/w2/sources/fetch-log.json` S004). This round: `b0a63496…`. Hashes differ; the taught text does not. The HTML embeds per-deployment build tokens — `__NEXT_DATA__…"buildId":"DyM2DITjzBZhj49DSSTvz"`, 26 `dpl_` occurrences, build-time GitHub avatar URLs (`?v=4`) and label totals (`"total":8`) — so any redeploy changes the bytes without changing the FAQ. `[INFERENCE]` the Oct-19→Oct-20 delta is deploy noise, because the Oct-19 bytes could not be retrieved (Wayback timed out, see below); the content-level conclusion does not depend on that inference.

Calibration consequence: a round-47 freshness gate that tests raw-byte equality for unversioned live pages will false-positive. Test the quoted sentence (and record ETag/buildId or upstream commit) instead; keep the SHA as drift evidence only.

## Recommended changes (old→new)

| field | old | new | rationale |
|---|---|---|---|
| status | `queued` | `queued` | No knowledge entry or lesson cites it as a source; contract rule 2 allows in-place change only for status/recheck/used-by, and none is earned. |
| recheck | `90d` | `90d` | Taught sentence unchanged since 2025-08-19; keep the cadence. Next due 2027-01-17 from `opened`, 2027-01-19 from this re-open. |
| used-by | `—` | `—` | Precedent: the round-46 lesson's sources table lists S004 (`corpus/lessons/round-46.md:66`) yet the row stayed `queued`/`—`; recording this re-open in the round-47 `## Gate` is evidence, not a citation. |

Anchor revision: the contract wants a revision in `anchor`, and this page has no version; the best revision markers are ETag `"27xowvmrnt1r0m"`, buildId `DyM2DITjzBZhj49DSSTvz`, and repo commit `d001185d`. `anchor` is outside the append-only mutable set, and the content claim is unchanged, so **do not** open a supersedes row for this. Apply the lesson to future rows: record the revision at write time.

## Commands and exit codes

- `git rev-parse HEAD` → `c61a973…` (0); `git status --porcelain` → only the two untracked paths (0)
- `date -u` → `2026-10-21T15:54:09Z` (0)
- curl fetch (0), sha256sum (0), `cmp` repeats (0, identical) — numbers above
- extraction script → 146 non-empty text lines; heading count 1; quote count 1 (0); `grep -o 'id="…conflict…"'` → no match (1, expected: no fragment id)
- `git ls-remote` (0) → `d001185d…`; `git clone --depth 100` (0); `git rev-list --count HEAD` → 38 (0); `git log -S…` → one commit (0)
- `git show c61a973b:corpus/SOURCES.md | grep -n S004` → line 17 (0); NF check → 13 (0); duplicate-id sweep → empty (0)
- `curl archive.org/wayback/available…` → curl exit 28, HTTP code 000 (timeout)

No tools installed or upgraded; all work stayed in `/tmp/s004probe/` plus the two permitted lane files (`.ufo/waves/round-47/build/SrcS004.md`, `SrcS004.json`, 7.3 KB). No fleet-root, index, jj, or sibling-lane writes.

## What I did NOT check

- Archived 2026-10-19 bytes (Wayback timed out), so the exact cause of the raw-hash delta remains inference, not a byte diff.
- Geo/edge variants: one egress only (`64.239.109.1`); other Vercel regions not sampled.
- Whether the live deployment builds from `main` HEAD or another branch; the README places the website in `agentsmd/agents.md`, but the deploy source is not observable from here.
- Client-side rendering: static SSG HTML only (`__N_SSG:true`), no browser execution.
- Any downstream consumer of the precedence rule: no `corpus/knowledge/` entry cites S004 at BASE, so "unused" is a grep-level observation over the lane, not a semantic proof of non-use elsewhere.

```json
{"row":"S004","verdict":"still-holds","access_utc":"2026-10-21T15:54:15Z","http_status":200,"sha256":"b0a63496f7c71419d2df378246ce9e7fe4501a849818a941cc7f424c0559125b","bytes":81690,"changes":{"status":"queued->queued","recheck":"90d->90d","used_by":"—->—"}}
```
