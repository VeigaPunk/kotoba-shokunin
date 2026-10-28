# Seat report — Kb80N01Sentinel (round 80 w1, leaf sentinel)

Source-stability sentinel for the C2 population (S226–S231). Task: fetch the six
pages at START, fetch again at END, diff, and give the L1 a per-page
STABLE/VARIED(bytes, class) verdict plus a variance report for anything that
moved. Also watch the negative-sweep pages the NegSweep seat flags unstable.

Base: `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`. Lane root
`/home/vgpnk/Projects/shokunin/kotoba-shokunin` (lane HEAD at my start:
`c2f69d4f7b5887c409d7c3975d6aebc2e312c406`; lane worktree clean apart from the
untracked `.ufo/waves/round-80/` wave dirs).

## Method

Every page fetched with the same shape the r79 fetch records used:

```
curl -sSL -A 'Mozilla/5.0' --max-time 60 -o <file> \
     -w '%{http_code}|%{url_effective}|%{num_redirects}|%{size_download}' <url>
```

Per page I recorded: UTC instant, curl exit, HTTP status, final URL, redirect
count, bytes (`wc -c`), sha256 (`sha256sum`). Two independent fetches per page at
START (23:12:44Z–23:13:51Z) so an intra-session change could not be mistaken for
a snapshot drift. Tooling: curl 8.23.0, Python 3.14.8 — nothing installed.

## START result — six C2 pages

| id | snapshot | snap bytes | snap sha256 (= manifest pin) | live bytes | live sha256 | verdict |
|---|---|---|---|---|---|---|
| S226 | S226-spec.md | 7608 | `9a67de89…a8dfde16` | 7608 | `9a67de89…a8dfde16` | **STABLE** |
| S227 | S227-claude.md | 117962 | `31623035…015712f9` | 117962 | `31623035…015712f9` | **STABLE** |
| S228 | S228-factory.md | 17567 | `81409d89…2fed0c9` | 17567 | `81409d89…2fed0c9` | **STABLE** |
| S229 | S229-msaf.html | 157339 | `34016233…6de548d2` | 157339 | `20fd76d8…77bd1e2` | **VARIED** |
| S230 | S230-pi.md | 4793 | `5b980552…456469e5` | 4793 | `5b980552…456469e5` | **STABLE** |
| S231 | S231-vibe.md | 77634 | `fc48a5db…2cb016b0` | 77634 | `fc48a5db…2cb016b0` | **STABLE** |

Full 64-hex digests and per-fetch status/redirect rows:
`build/Kb80N01Sentinel-fetch-start.txt` (pass 1),
`build/Kb80N01Sentinel-fetch-start-second.txt` (pass 2),
`build/Kb80N01Sentinel-start-table.txt` (the table above, machine-generated from
the fetched bytes). All six: HTTP 200, curl rc=0.

Two notes that keep this table honest:

1. **S228 is compared on its Markdown route only.** The assigned URL
   `https://docs.factory.ai/cli/configuration/skills` with `-L` lands on the
   **HTML** page `docs.factory.com/harness/skills` (341384 B, 2 redirects) —
   a different representation, not a different page, and not what the snapshot
   is. The snapshot is the `.md` route (`docs.factory.ai/cli/configuration/skills.md`
   → 2 redirects → `docs.factory.com/harness/skills.md`, 17567 B,
   `text/markdown`), which is why the like-for-like comparison above is
   byte-identical. I did not diff HTML against Markdown; that comparison would be
   meaningless.
2. **All six rows above are computed from fetched bytes**, not copied from
   `S2xx.manifest`. Independently, `sha256sum -c` against the six per-page
   manifests passes for all six (`…: OK`, rc=0), so the committed snapshots are
   self-consistent with their pins.

## Variance report — S229 (the only C2 page that moved)

Shape: **same length, different digest** — 157339 B both sides, exactly **22
differing bytes**, clustering into 10 contiguous runs at **4 logical sites**
(0-based offsets 6776, 8202, 8430, 157160; `cmp -l` reports them 1-based as 6777,
8203, 8431, 157161). No length change anywhere.

| site | offset | snapshot | live | what it is |
|---|---|---|---|---|
| 1 | 6777 | `0.4.03574.8308-9505b1c8` | `0.4.03585.8328-71cc54cb` | learn.microsoft.com static-asset build stamp in the `<link rel=stylesheet>` href |
| 2 | 8203 | same stamp | same stamp | the same stamp in the `index-docs.js` `<script src>` |
| 3 | 8431 | `akam/13/41ddb17` | `akam/13/41ddb15` | Akamai bot-manager script path |
| 4 | 157161 | `akam/13/41ddb17` | `akam/13/41ddb15` | the bot-manager `<noscript><img … pixel_…>` |

Class: **infrastructure-only substitution (site redeploy + Akamai bot-manager
id), content bytes unchanged.** Proof, not assertion:

- Normalizing exactly those two token classes (`0\.4\.0\d+\.\d+-[0-9a-f]{8}` →
  `<BUILDSTAMP>`, `akam/13/[0-9a-f]+` → `<AKAM>`, `pixel_[0-9a-f]+` → `pixel_<AKAM>`)
  makes the two byte strings **equal**, both hashing to
  `08284beefd5399c5cc38e6ed7e8dbf56e6a2196b5a4361c99a29e936d5cb7430`, 157315 B.
- The page's own content anchors are byte-identical across the pair:
  `ms.date" content="2026-10-23T00:00:00Z"`,
  `git_commit_id" content="d34f426053dba6703197776e7aad4d30fd4d06f5"`, and the
  single `allowed-tools` occurrence all match.
- Third and fourth fetches at 23:13:16Z returned `20fd76d8…` again, identical to
  my START fetch. So the rotation is **per-deploy, not per-request**: the page
  was stable across my whole session and had been redeployed between the r79
  snapshot (2026-10-27T21:41:02Z) and my first fetch (23:12:45Z).
- **Independent cross-check:** `Kb80R03ReopenSix` fetched the same six pages at
  23:13:48Z–23:15:03Z (`.ufo/waves/round-80/build/Kb80R03ReopenSix-S2xx.fetch.json`)
  and its six digests are identical to mine — S229 included (`20fd76d8…`) — with
  the same Akamai classification (4 changed line-pairs). Two seats, disjoint
  instants, same numbers: the variance belongs to the page, not to one seat's
  fetch.
- **Branch-versus-artifact stability (S230).** I resolved the served refs myself
  with `git ls-remote`: `badlogic/pi-mono` `refs/heads/main` =
  `85c2ee3e761e4fc4f901ff0ed584fb2465aa552e` (the r79 fetch record named
  `bb65e3e4…`), and `mistralai/mistral-vibe` `refs/heads/main` =
  `7bb48f213ac677f943d5c791199ed3dddf302f00` (unchanged since r79). So pi's
  **branch moved while its file bytes did not** — a `main` URL is a moving
  pointer even when the artefact is stable, and only the snapshot pin makes the
  S230 row reproducible. That is the argument for pinning bytes, not refs.

Offsets: `build/Kb80N01Sentinel-S229-cmp-offsets.txt` (`cmp -l` output, rc=1,
22 lines). This is the class the brief called "S229's Akamai class" — confirmed,
and now measured rather than assumed.

### What S229's variance means for the C2 pins (the decision the L1 needs)

The counter resolves a row's pin as `MANIFEST.sha256[snapshot]` and then requires
the row's anchor cell sha256 to **equal that pin** (`row_[5]`, evidence in the
next section). It never fetches. So:

- **Pin S229 at the snapshot bytes `34016233…`** and write the anchor as
  `fetched 2026-10-27T21:41:02Z, HTTP 200, 157339 B, sha256 34016233…`. This is
  correct and it is what the current snapshot supports. The live page is
  content-identical, so the entry's `verified-at: 2026-10-27` claim remains true.
- **Do not** write today's live instant/digest (`2026-10-27T23:12:45Z`,
  `20fd76d8…`) into the anchor: the counter would red with
  "`anchor sha256 20fd76d8dea5... is not the snapshot's pin 34016233a42a...`".
  Recording a fresh live fetch is only valid together with a re-snapshot of the
  page and a matching new pin — a data change the wave has not declared.
- **The recheck cell must test content, not a digest.** A recheck that compares
  sha256 against a live fetch will be red on S229 on every future deploy
  regardless of content. The r79 skeleton's recheck already does the right thing
  (quote-occurrence counts); I ran it live today and it prints exactly `1 1 2 1 1 1`,
  its frozen expectation, across all six pages — the freshness contract is
  operable, and it is content-based by construction.

## Do the pins still ground the labels? (yes — measured on live bytes)

A snapshot pin is only worth something if the bytes it pins still carry the text
the row quotes. Counting each surface's counter-side grant token in the bytes I
fetched today against the committed snapshot:

| id | surface | counter grant token | live | snapshot | `allowed-tools` in live |
|---|---|---|---|---|---|
| S226 | spec | `Experimental` | 2 | 2 | 4 |
| S227 | claude | `without prompting you for approval` | 1 | 1 | 23 |
| S228 | factory | `metadata` | 8 | 8 | 8 |
| S229 | msaf | `Experimental` | 1 | 1 | 1 |
| S230 | pi | `Experimental` | 1 | 1 | 1 |
| S231 | vibe | `allowed-tools:` | 1 | 1 | 1 |

Every count is equal on both sides, S229 included — the redeploy changed
instrumentation only, so no row's located quote has gone stale. The two
occurrence-count quirks are properties of the pages, not defects: `Experimental`
appears twice on the specification page, and `metadata` eight times on Factory's.

## Negative-sweep watch set

The brief said "the four negative-sweep pages the NegSweep seat flags as
unstable". `Kb80R01NegSweep` (`.ufo/waves/round-80/w1/Kb80R01NegSweep.md`) flags
**one**, not four: `amp` (`ampcode.com/docs/customize/skills`), "3 rotating CSP
`<script nonce=` attribute values (content identical)"; 11/12 were byte-identical
across its two passes. I report the mismatch rather than invent a fourth page,
and I watched `amp` plus all five pages whose URL redirected (a redirect is the
other way a snapshot can stop matching its recorded page identity).

| page | my pass A (23:16:43Z) | my pass 3 (23:19:12Z) | NegSweep p1 | verdict |
|---|---|---|---|---|
| amp (no redirect) | `5a5c794c…`, and `f01931dd…` in the same second | `3c73a8a4…` | `d8a8eeb0…` | **VARIED** — per-request CSP nonce |
| codex → learn.chatgpt.com/docs/build-skills (1×301) | `e657e0e3…` | `c4d4c5a9…` | `e657e0e3…` | **VARIED** — Vercel deployment id + Astro asset hashes |
| vscode → …/docs/agent-customization/agent-skills (1×301) | `4b40d645…` | `f2a28cfb…` | `4b40d645…` | **VARIED** — `awa-expId` A/B assignment |
| ghcopilot → …/customizations/agent-skills (1×301) | `e99da060…` | `e99da060…` | `e99da060…` | STABLE |
| cursor → cursor.com/docs/skills (1×301) | `abb0613a…` | `abb0613a…` | `abb0613a…` | STABLE |
| roo → roocodeinc.github.io/Roo-Code/features/skills/ (2×301) | `fe801910…` | `fe801910…` | `fe801910…` | STABLE |

**My first pass called codex and vscode STABLE and that was wrong** — they matched
NegSweep's pass-1 only because both samples fell inside the same short window.
Three minutes later both had moved, with **unchanged byte counts** (417416 B,
157102 B). Classes, each proven by a normalisation that makes the pair equal:

- `amp`: 4 `nonce="…"` attributes, one value per response
  (`4foML/7ntDth56lZaR4LFQ==` vs `wvGcb/iw2M5CVtScl9tBNA==`), **84** differing
  bytes; nonce-normalised bytes equal (`4e7b7047…`). Rotates per request.
- `codex`: `/_astro/….Qncnqoy_.js?dpl=dpl_HEZ81NcnrJCVNuJdNyKiPTTVP9Zp` vs
  `….CGmaVkTC.js?dpl=dpl_4YvAspsmP43reDUMSFWeDV23zx7R` — **687** differing bytes.
  The edge serves the same page from **two concurrent Vercel deployments**, each
  with its own asset hash and `dpl_` id; normalising
  `\.[A-Za-z0-9_-]{8}\.(js|css)` and `dpl_[A-Za-z0-9]+` makes the pair equal
  (`aae5c4dd…`). Rotates per edge/cache hit, not per deploy.
- `vscode`: `<meta name="awa-expId" content="tv-downloadv2:1469049;68097614:1474476;">`
  vs `…;9ec16314:1474477;` — **7** differing bytes, an A/B experiment id and
  assignment counter; normalising the `awa-expId` content makes the pair equal
  (`91d3676a…`). Rotates per request.

**Calibration consequence for the S232+ rejection rows:** `Kb80R01NegSweep`'s
"11/12 byte-identical across passes" is true only of its ~30 s window; over
~3 min two more pages rotate. Its *negative* finding is untouched (the greps are
0 hits on every pass I and it ran, and content is normalised-equal), but the
words "stable page" must not be written. Say "0 hits, content-stable", and never
cite a live digest in a rejection row — on `amp`, `codex` and `vscode` a
digest-equality recheck is red on most requests.

## C2 pin prerequisites — four measured blockers for `check_allowed_tools.py`

While establishing that the live bytes are what the pins claim, I measured the
pin chain itself, because a wrong pin is a source-stability defect even when the
page is fine. Four findings, each with its command and exit code. These go to
`Kb80E08C2Entry`/`Kb80E07C2Counter` and the L1; I changed nothing.

**First, the part that is already sound.** For all six ids the recorded chain
agrees end to end: `sha256(snapshot bytes)` == the `.manifest` pin == the
`.fetch.json` `sha256`, and `.fetch.json` `bytes` == the snapshot's size with
`http: 200`; `sha256sum -c` against all six `.manifest` files passes (rc=0).
So findings (1) and (3) below are about **aggregation and presentation**, not
about wrong recorded evidence — the underlying snapshot set is honest.

**(1) `.ufo/waves/round-79/snapshots/MANIFEST.sha256` does not exist at base, and
the counter hard-codes it.** The r79 counter declares
`SNAPDIR = ".ufo/waves/round-79/snapshots"`, `MANIFEST = SNAPDIR + "/MANIFEST.sha256"`
(sha256 of the counter I read: `74e067ccad7813d91826ee503c8ee93ba47d3a4a05b12ec67a82791d93f722a6`,
which matches the freeze receipt's value for the r79 draft). At base only the six
per-page `S2xx.manifest` + `S2xx.fetch.json` + snapshot files are committed:

```
git -C <lane> cat-file -e 398cbe1:.ufo/waves/round-79/snapshots/MANIFEST.sha256
fatal: path '...MANIFEST.sha256' does not exist in '398cbe1...'   (rc=128)
```

The missing file is **latent at base**: the counter returns before reading it,
because the entry is absent first —

```
python3 -B .ufo/waves/round-79/build/check_allowed_tools.py --repo <lane> --rev 398cbe1…
allowed-tools surfaces backed 0 of 6      script-only world: 0 of 6
  entry corpus/knowledge/allowed-tools-surfaces-round79.md absent at 398cbe1… 
exit=1        (build/Kb80N01Sentinel-counter-base-r79draft.txt)
```

— and it **fires at any tip that carries the entry**. Proven in a scratch clone
(throwaway commits only): a conformant entry head + one spec row at the frozen
entry path exits **2**:

```
environment error: no manifest at .ufo/waves/round-79/snapshots/MANIFEST.sha256
at <rev>: the snapshots are unpinned, so (c) cannot be evaluated
exit=2        (build/Kb80N01Sentinel-probe2-usedby-fixed.txt)
```

Adding a 6-line `MANIFEST.sha256` (content = the six per-page `.manifest` files,
verbatim) clears that gate and the counter advances to per-row pin resolution
(`build/Kb80N01Sentinel-probe3-manifest-added.txt`). The proposed file is
published as `build/Kb80N01Sentinel-MANIFEST.proposed`; it is a *data* file the
counter reads, not the counter, so adding it does not drift the freeze.

**(2) The r79 entry skeleton, dropped in verbatim, exits 2 on pin ambiguity.**
`snapshot_name()` collects, for every backticked token on a line that cites
`S###`, the basenames that appear in the manifest; more than one candidate for the
same sid is an `EnvError`. The skeleton's own required shaping paragraph names
five snapshot basenames in backticks on a line that also carries `S226`:

```
- **Snapshot forms differ…** `S229-msaf.html` is the raw served HTML … the other
  five snapshots are Markdown (`S226-spec.md`, `S227-claude.md`, `S231-vibe.md`, …)
  or a Markdown route (`S228-factory.md` is …)
```

→ `environment error: S226: the entry names 5 pinned snapshots
(S229-msaf.html, S226-spec.md, S227-claude.md, S231-vibe.md, S228-factory.md) —
the pin of one row is ambiguous`, exit=2
(`build/Kb80N01Sentinel-probe4-ambiguity.txt`). Un-backticking those basenames on
that one line resolves it and the counter proceeds to the anchor/quote checks
(`build/Kb80N01Sentinel-probe5-ambiguity-fixed.txt`, exit=1 with row findings).
**Constraint for the entry author:** a line that cites a sid may name at most one
pinned snapshot basename in backticks — or must name none, so the sid-prefix
fallback resolves it.

**(3) All six base anchor cells use a date-only fetch record and fail the
counter's own regex.** The free-text anchor cell is `row_[5]`; the counter
requires `fetched <ISO8601 with T…Z>, HTTP 200, <bytes> B, sha256 <hex>`
(`FETCHED_RE`). Every base row reads `fetched 2026-10-27, HTTP 200, … B, sha256
`9a67de…`` — no `T…Z` — so `FETCHED_RE` matches **False for all six** (measured
against each row line). The per-page `.fetch.json` files already carry the
full instants, so the correction is mechanical. Verified per-row proposals
(each matches `FETCHED_RE`, and its sha256 equals the pin, and its byte count
equals the snapshot size) are in
`build/Kb80N01Sentinel-C2-pin-prerequisites.txt`, e.g.:

```
S229 | 11 | anchor_matches_FETCHED_RE_now=False | opened=2026-10-27
     | used_by_now=corpus/lessons/round-79.md
     | OK fetched 2026-10-27T21:41:02Z, HTTP 200, 157339 B,
          sha256 34016233a42a2191e319bb6ed49362956c6a6e86bbe64f2fa2e370326de548d2
```

Cell map (0-based over the 11 content cells, confirmed against the counter's own
index reads): `0` id, `1` source, `2` kind, `3` tier, `4` scope, **`5` anchor**,
`6` teaches, `7` status, `8` opened, `9` recheck, `10` used-by.

**(4) All six `used-by` cells name the r79 lesson, not the C2 entry.** The
counter requires `ENTRY` in `row_[10]`; at base all six read
`corpus/lessons/round-79.md`. My probe reproduces the exact finding
(`spec: S226: used-by 'corpus/lessons/round-79.md' does not list
corpus/knowledge/allowed-tools-surfaces-round79.md`,
`build/Kb80N01Sentinel-probe1-entry-head.txt`). Round 80 plans this move
(plan § Frontier step), so this is a reminder with the exact cell, not a new
defect.

Consolidated: (1) and (3) are hard — without them no tip can print
`documented 6 of 6` or exit 0, and (1) fails as exit 2, not the declared exit 1.
(2) and (4) are entry-authoring traps that cost an exit-2 round if missed.

## The landed round-80 counter does not yet match the frozen predicate

As of 2026-10-27T23:22Z, `build/check_allowed_tools.py` is **byte-identical to
the r79 draft**: sha256 `74e067ccad7813d91826ee503c8ee93ba47d3a4a05b12ec67a82791d93f722a6`,
103590 B. Consequences, all checkable without running anything:

- The frozen predicate quotes `allowed-tools surfaces documented N of 6` and
  `generator world: M of 6`. The landed file prints `allowed-tools surfaces
  backed {n} of 6` and `script-only world: {m} of 6`; the strings `allowed-tools
  surfaces documented` and `generator world:` occur **0 times each**.
- `TARGET = 5` and the exit is `ok = n >= TARGET and m < TARGET and …`, so
  exit 0 is reachable at **5 of 6** — the plan's `exit 0 iff N == 6` would be
  false of these bytes.
- `ENTRY` is still `corpus/knowledge/allowed-tools-surfaces-round79.md`; the
  round-80 entry is `…round80.md`.

Its base run prints `backed 0 of 6`, exit 1
(`build/Kb80N01Sentinel-landed-counter-base.txt`). The **number** matches the
declared base figure; the **string does not**. Because the number is right and
the string is wrong, this is the kind of mismatch a quoted command output
invites: a reader who compares the claim's text to this artifact's text sees a
difference that is not a measurement error. It needs the round-80 bytes
(print strings, `TARGET = 6`, entry path) before the freeze; until then the C2
predicate cannot be satisfied by what is in the tree. I did not edit it — the
counter is E07's artifact and `verifiers/` is patch-only for me.

## Recheck tool — the variance findings made operable

The output the L1 has to decide recheck cells with is not the verdict alone but a
runnable test, so I published one:
`build/Kb80N01Sentinel-recheck-c2-stability.py` (7698 B). It fetches the six
pages, compares each to its committed pin, and **normalises only a per-page
declared token class** — S229's asset stamp + Akamai id; nothing for the other
five, so any byte change there is a content verdict. Exit `0` when every page is
STABLE or VARIED(known class); `3` on any content change; `2` on environment
error.

Two runs, both captured:

```
$ python3 -B build/Kb80N01Sentinel-recheck-c2-stability.py
S226 STABLE  7608 9a67de89 -
S227 STABLE  117962 31623035 -
S228 STABLE  17567 81409d89 -
S229 VARIED  157339 20fd76d8  msft-asset-stamp+akam
S230 STABLE  4793 5b980552 -
S231 STABLE  77634 fc48a5db -
C2 stability: 5 stable, 1 varied (known class), 0 content change(s)      exit=0

$ python3 -B build/Kb80N01Sentinel-recheck-c2-stability.py --selftest
S229 VARIED  157339 20fd76d8  CONTENT DIFFERS
C2 stability: 5 stable, 0 varied (known class), 1 content change(s)
selftest PASS: the content-change state is reachable, so a real run would exit 3
exit=0   (the selftest's own success code; the payload verdict is exit 3)
```

The `--selftest` path flips one content byte of a copied S229 snapshot and
rebuilds that copy's pin, so the red is attributable to content and not to a pin
mismatch — this is the round's own M80-1 discipline applied to my own check: a
check I have not shown able to fail is not a check. Receipts:
`build/Kb80N01Sentinel-recheck-live.txt`,
`build/Kb80N01Sentinel-recheck-selftest.txt`.

Caveat for its users: the classes are deliberately narrow and page-scoped. If a
page starts rotating a new token, the tool goes red rather than green — that is
the intended direction. Widening a class to make a page pass is the laundering
the r79 pin guard exists to prevent; it needs a measurement, not an edit.

## What I did not do, and why

- I did not edit the lane, any `verifiers/` file, `corpus/`, `SKILL.md`,
  `PROVINCE.md` or `plans/`. All probes ran in a throwaway clone under
  `/fast/scratch/hyaku/kotoba-r80/Kb80N01Sentinel/`; the lane's only writes are my
  own report and `Kb80N01Sentinel-*` receipts under `build/`.
- I did not score any claim after-value, and I did not treat C2 as passing: the
  base figure `documented 0 of 6` is my measurement of the r79 draft counter at
  base, not of the round-80 counter at the round-80 tip.
- I did not compare the S228 HTML page to its Markdown snapshot, and I did not
  treat `amp`'s per-request nonce as instability of content.
- I did not run the C1 tip battery (not my item; ~104 s heavy pass).

## END

END pass fetched 2026-10-27T23:22:03Z–23:22:05Z. Window covered:
**23:12:44Z → 23:22:05Z = 9 m 21 s**, with 4 fetches per C2 page (5 for S229)
and 3–4 per watched page.

| id | END bytes | END sha256 (16) | START == END | vs committed snapshot | verdict |
|---|---|---|---|---|---|
| S226 | 7608 | `9a67de89132948b2` | identical | identity | **STABLE** |
| S227 | 117962 | `31623035b25ac7e6` | identical | identity | **STABLE** |
| S228 | 17567 | `81409d890cb1b07f` | identical | identity (`.md` route) | **STABLE** |
| S229 | 157339 | `20fd76d8dea592cb` | identical | normalized-equal, msft-asset-stamp+akam | **VARIED** |
| S230 | 4793 | `5b9805525b194474` | identical | identity | **STABLE** |
| S231 | 77634 | `fc48a5dbafe572fe` | identical | identity | **STABLE** |

`all six: START == END = True`; `all six: live content == snapshot content =
True`. No C2 page moved during the wave window. Receipt:
`build/Kb80N01Sentinel-fetch-end.txt`.

### Per-page verdict (the list the L1 asked for)

```
S226  STABLE          7608 B    byte-identical to snapshot, 4/4 fetches
S227  STABLE        117962 B    byte-identical to snapshot, 4/4 fetches
S228  STABLE         17567 B    byte-identical to snapshot, 4/4 fetches (.md route)
S229  VARIED        157339 B    class: msft asset build stamp x2 + Akamai bot-manager id x2,
                                22 bytes / 4 sites, normalized-equal content, per-deploy
S230  STABLE          4793 B    byte-identical to snapshot, 4/4 fetches
S231  STABLE         77634 B    byte-identical to snapshot, 4/4 fetches

amp        VARIED    105308 B   class: 4 CSP script nonces, per request, normalized-equal
codex      VARIED    417416 B   class: Vercel dpl_ id + Astro asset hash, two concurrent deployments
vscode     VARIED    157102 B   class: awa-expId A/B experiment assignment, per request
ghcopilot  STABLE    566781 B   byte-identical across every pass and NegSweep pass-1
cursor     STABLE    490061 B   byte-identical across every pass and NegSweep pass-1
roo        STABLE     71129 B   byte-identical across every pass and NegSweep pass-1
```

### State of the wave at my END (scoped honesty about what this verdict covers)

- `build/check_allowed_tools.py` was still the r79 draft byte-for-byte
  (`74e067cc…`); **no round-80 C2 entry and no C2 worlds had landed** (`.ufo/waves/round-80/build/`
  had no `allowed-tools-surfaces-round80.md`, no E09 outputs). So my verdict is a
  verdict on the **sources and their pins**, not on the C2 claim, and it holds
  regardless of when the entry lands.
- The six C2 pages are safe to pin as they stand; S229 is the only one whose
  recheck needs the class-aware test, and `build/Kb80N01Sentinel-recheck-c2-stability.py`
  is that test (run it at closure: `exit 0` = 5 stable + 1 known class).
- If any page moves after 23:22:05Z the L1 should run the recheck tool rather
  than re-derive the class by hand; it prints the verdict and the exit code.

## Addendum — the `commit_unresolvable` pair, and a provenance defect inside it

Measured with the gates' own `--json` on a base clone (receipt
`build/Kb80N01Sentinel-commit-unresolvable-truth.txt`), because a broadcast and
the plan disagreed and only the gate bytes settle it.

At base `398cbe1`, `verify_corpus_integrity.py` reports `commit_total = 46`,
`commit_quoted_excluded = 6`, `commit_unresolvable = 2`, and the two are:

```
corpus/SOURCES.md:171: 7bb48f213ac677f943d5c791199ed3dddf302f00
corpus/SOURCES.md:172: 7bb48f213ac677f943d5c791199ed3dddf302f00
```

So the plan's § Trigger sentence is wrong about which tokens are unresolvable:
`google-gemini/gemini-cli@451a02ff` and `zed-industries/zed@cfb894a5` are
`commit_quoted` and already excluded (they appear in the quoted detail list,
e.g. `corpus/lessons/round-53.md:44: cfb894a5 (quoted meta-finding)` and
`corpus/lessons/round-54-verifier-spotcheck.md:147: 451a02ff`). The real pair is
the *same* hex twice, at lines 171 (S230) and 172 (S231).

**And the two occurrences are not the same kind of thing:**

- `SOURCES.md:172` is the S231 row — Mistral Vibe. `7bb48f21…` is genuinely
  mistral-vibe's commit (I verified `refs/heads/main` by `git ls-remote`, and
  `S231.fetch.json` recorded the same). Legitimate third-repo citation.
- `SOURCES.md:171` is the S230 row — **pi-mono**. Its own fetch record says
  "`main` at fetch time = `bb65e3e49710fbd14f10c7792d0eaa6e2b2c5923`", and the
  round-80 entry's line 124 states that same `bb65e3e4…`. So S230's anchor cell
  carries **another repository's commit id**. That is a provenance error in a
  mined row, not an external-commit citation.

Consequence for C1's repair 5, which is the reason I am writing it down: a
grammar class that classifies both occurrences as "external commit, INFO" would
turn C1 green while leaving a false provenance fact in `corpus/SOURCES.md`. The
S230 value needs correcting to `bb65e3e4…` in the data (it is already being
rewritten this round for the `FETCHED_RE` form — see prerequisite (3) above), so
the class ends up carrying only genuine third-repo citations.

**The class cannot be dodged by rewording the entry.** Four measured worlds:

| world | commit_unresolvable | new site |
|---|---|---|
| base only | 2 | — |
| base + the r80 C2 entry landed | **3** | `…/allowed-tools-surfaces-round80.md:125` |
| …entry:125 reworded with `mistralai/mistral-vibe` | **3** | unchanged |
| …entry:125 given a commit-pinned raw URL for that commit | **3** | unchanged |

Adding an `owner/repo` token and adding a commit-pinned URL both leave it red, so
the gates have no external-commit concept at all and no entry wording clears it —
E05's class is mandatory, and it must live in the gate, not in the citation.

Design constraint that follows, stated as a test obligation: the new class must
have a **negative arm** — a fabricated hex on a line that does carry a
third-repo marker must still be counted unresolvable. Otherwise "explicit
third-repository citation" becomes a blanket exemption for any hex preceded by
any repo name, which is exactly how a wrong commit like S230's would survive.
I did not write or edit either gate; this is handed to E05 and the L1.

## Addendum 2 — msaf is unquotable under the current heading heuristic, and fixing it unmasks the generator

`Kb80E08C2Entry` reported that S229 cannot satisfy Q70 for structural reasons. I
verified it with the counter's own `text_view()` and the numbers are decisive:

- 1550 view lines; **23 lines start with `#`**; the **first is view idx 168**
  = `# Auto-approve load_skill and read_skill_resource, but not run_skill_script.`
  — a Python comment inside a code sample, not a heading.
- `allowed-tools` occurs **once** in the raw HTML and on **exactly one** view
  line, **idx 95**.
- Q70 rejects `idx <= first_head + 1` = `<= 169`, so the admissible set is
  **empty**: `[i for i in hits if i > 169] == []`.

Classification: **counter defect, not a quote choice.** The text view strips tags
(including `<h1>`), then guesses headings with a Markdown `#`-prefix convention.
On an HTML page that convention finds a Python comment first; the page's real
anchor is `<h1 id="agent-skills">` in raw and `Agent Skills` at view idx 38, so
idx 95 *is* after the real first heading and the intended Q70 is satisfiable.
Fixing the heuristic implements Q70; moving the quote would dodge it. E08's
refusal to move the quote is correct.

**The hazard nobody had stated:** `first_head` is used **twice** — at the Q70
check and in `_mech_quote()`, where it sets the generator's body window
(`body = lines[first_head + 2:]`).

- As coded on S229 the window starts at 170, the field is only at 95, so
  `_mech_quote(...)` returns **`None`** — the generator currently gets nothing
  for msaf (measured).
- With a corrected window (after view idx 38), the same no-judgement 25-word
  scrape yields: *"allowed-tools No Space-delimited list of pre-approved tools the
  skill may use. Experimental - support may vary between agent implementations.
  Recognized top-level field names must use"* — carrying `allowed-tools`,
  `space-delimited`, `pre-approved` **and** `Experimental`, i.e. every token role
  the msaf row needs.

So the Q70 bug is currently *masking* the generator's reach on msaf. Under the
r80 counter's `ok = n >= TARGET and m < TARGET` with `TARGET = 6`, an `M` of 6
makes the counter print its own defect line and exit 1. **E07 must fix
`first_head` and re-measure `M`; if `M` reaches 6, C2 stops** — the plan forbids
repairing that by narrowing. What I measured is the mechanical quote's content;
what I did **not** measure is the resulting `M` (the counter is frozen and
`SELF_SHA`-guarded, so only the counter seat can run it). Stated this way on
purpose.

Also verified for E08, so the record has it: their current entry
(sha256 `037c3b61…`, 24726 B) landed in a base clone leaves
`commit_total = 46`, `commit_unresolvable = 2` — **it adds no commit token**
(the third unresolvable I measured on the earlier draft is gone) — and across 74
sid-citing lines **zero** carry more than one backticked pinned basename, with
each of S226–S231 binding to exactly one snapshot.

## Tooling

No installs or upgrades. curl 8.23.0 and Python 3.14.8 were already present and
sufficed; nothing was taken from pacman (host-wide pause respected), `uv`, or any
release channel.

## Scratch

`/fast/scratch/hyaku/kotoba-r80/Kb80N01Sentinel/` (fetch bodies, probe clone,
probe commits), `/fast/scratch/hyaku/kotoba-r80/Kb80N01Sentinel2/` and
`…/Kb80N01Sentinel3/` (base clones for the corpus-gate and text-view
measurements). All removed and verified gone; the receipts in `build/` are the
only persisted artifacts.

VERDICT: Sources STABLE, pins unsound — over 2026-10-27T23:12:44Z–23:22:05Z all six C2 pages returned identical bytes START==END (S226 7608, S227 117962, S228 17567 md-route, S229 157339, S230 4793, S231 77634) and only S229 VARIED vs its committed snapshot (157339 B, per-deploy class: msft asset build stamp ×2 + Akamai bot-manager id ×2, 22 bytes/4 sites, normalized-equal 08284bee…, content identical); C2 cannot reach `documented 6 of 6` on the bytes in the tree — `.ufo/waves/round-79/snapshots/MANIFEST.sha256` is absent at base (`git cat-file -e` rc=128) and the counter exits 2 without it, the landed `build/check_allowed_tools.py` is the r79 draft byte-for-byte (74e067cc…) printing `backed`/`script-only world` with TARGET=5, all six SOURCES anchor cells are date-only and fail FETCHED_RE, all six used-by cells still name the r79 lesson, and the r79 entry skeleton trips an exit-2 pin ambiguity on its own shaping paragraph; and the C1 blocker is mis-specified by the plan — the real `commit_unresolvable` pair is the same hex `7bb48f21…` at SOURCES.md:171/:172 (not gemini-cli@451a02ff/zed@cfb894a5, which are commit_quoted), where :172 is mistral-vibe's commit and correct while :171 sits in the pi-mono row whose own fetch record and the r80 entry (line 124) both say `bb65e3e4…`, so a line-scope external-citation class would launder a provenance error; landing the entry adds a third unresolvable at entry:125 and neither an owner/repo token nor a commit-pinned URL clears it (both tested), so the class must live in the gate with a negative arm; and msaf (S229) cannot satisfy Q70 under the current bytes — the text view's first `#`-prefixed line is view idx 168, a Python comment in a code sample, while the field occurs on one line only, idx 95, and Q70 needs idx > 169, so the admissible set is empty: that is a counter defect (Markdown heading convention applied to a tag-stripped HTML view) rather than a quote choice, and because the same `first_head` sets the generator's body window, fixing it also enables the no-judgement scrape on msaf (whose 25-word mechanical quote carries `allowed-tools`, `space-delimited`, `pre-approved` and `Experimental`), so `M` must be re-measured or C2 trips its own `m < TARGET` rule; negative-sweep watch: amp VARIED (per-request CSP nonce), codex VARIED (two concurrent Vercel deployments), vscode VARIED (awa-expId A/B) — NegSweep's "11/12 byte-identical" holds only for its ~30 s window, so rejection rows must say "0 hits, content-stable" and never cite a live digest; I corrected my own first-pass STABLE calls for codex/vscode.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80N01Sentinel.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80N01Sentinel-fetch-start.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80N01Sentinel-fetch-end.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80N01Sentinel-start-table.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80N01Sentinel-S229-cmp-offsets.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80N01Sentinel-C2-pin-prerequisites.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80N01Sentinel-MANIFEST.proposed; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80N01Sentinel-recheck-c2-stability.py; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80N01Sentinel-recheck-live.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80N01Sentinel-recheck-selftest.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80N01Sentinel-landed-counter-base.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80N01Sentinel-commit-unresolvable-truth.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80N01Sentinel-msaf-q70-measurement.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80N01Sentinel-watch-pass-a.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80N01Sentinel-watch-pass3.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80N01Sentinel-watch-classes.txt
