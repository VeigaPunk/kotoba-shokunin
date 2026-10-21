verdict: S008 still holds — the live https://yaml.org/spec/1.2.2/ is byte-identical to the round-46 fetch (sha256 2fe1bf40…), anchor §7.3.3 Plain Style and the teaches cell both match the served text; keep `mined` / `on-release` / `SKILL.md`; the §8.1.3 folded-scalar fact this round touches would be a new row, not an in-place edit.

# S008 — YAML Specification 1.2.2 (frontier re-open, round 47)

Target at BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`: `corpus/SOURCES.md:21`.

## Observed — fetch

| field | value |
|---|---|
| URL | `https://yaml.org/spec/1.2.2/` (no redirect) |
| UTC access | 2026-10-21T15:54:20Z (second GET 15:58:04Z, identical) |
| HTTP status | 200, `text/html; charset=utf-8` |
| bytes | 383078 |
| sha256 | `2fe1bf40792df22ef8b8a5972a34c48e639969222e0bbae605aa9bb2ca85e9ab` |
| Last-Modified | Wed, 30 Sep 2026 21:04:48 GMT |
| ETag | `"6abd7970-5d866"` (0x5D866 = 383078 bytes) |
| server | GitHub.com |

The hash equals the S008 record in `.ufo/round-46/evidence/w2/sources/fetch-log.json` and `corpus/lessons/round-46.md:70` (`2fe1bf40792df22e…`) — no content drift in two days. Page title: `YAML Ain’t Markup Language (YAML™) revision 1.2.2`; the revision subtitle is `<h2 class="subtitle" id="revision-122-2021-10-01">Revision 1.2.2 (2021-10-01)</h2>` at byte 1021 (frozen revision, not a rolling page).

Fetched bytes stayed in `/tmp/yaml1222.html`; nothing large was written to the lane. Metadata record: `.ufo/waves/round-47/build/SrcS008.json` (6443 bytes, valid JSON).

## Observed — anchor holds

Live HTML: `<h3 id="733-plain-style">7.3.3. Plain Style</h3>` at byte offset 232188; in-page anchors `#733-plain-style` and `#plain-style` both resolve. The row's anchor cell `§7.3.3 Plain Style` (`corpus/SOURCES.md:21`) names the exact heading. **Holds, no change.**

## Observed — teaches holds (quote ≤25 words)

§7.3.3, byte 233947 (paragraph after production `[126] ns-plain-first`):

> “Plain scalars must never contain the “: ” and “ #” character combinations. Such combinations would cause ambiguity with mapping key/value pairs and comments.” — 22 words

The row's teaches (“…colon-space or space-hash combinations, since both are ambiguous with key/value pairs and comments”, `corpus/SOURCES.md:21`) is a faithful paraphrase: `colon-space` = `: `, `space-hash` = ` #`, and the ambiguity clause is the spec's own sentence. **Holds, no change.**

## Observed — folded block scalars §8.1.3 (the round-47-relevant section)

Heading `<h3 id="813-folded-style">8.1.3. Folded Style</h3>` at byte 298697; first paragraph at byte 298749:

> “The folded style is denoted by the “>” indicator. It is similar to the literal style; however, folded scalars are subject to line folding.” — 24 words

This is the form the lane actually uses: `description: >` at `SKILL.md:3`; the C2 draft patch (`.ufo/waves/round-47/build/C2SkillRewrite.patch`) keeps the `>` indicator and only replaces the `<skills>` phrase on the line at `SKILL.md:14`.

Measured against `SKILL.md` at BASE with PyYAML 6.0.3: loaded description = **815 chars** (814 stripped, 0 internal newlines, 1 trailing newline), 4 occurrences of `: `, 0 of ` #`, one angle token `<skills>`. `SKILL.md:456` already states the loader-normalization rule (“`>`/`|` keep a trailing newline, `>-`/plain strip it”) — 815 vs 814 is that rule, observed. `verifiers/verify_skill_checklist.py:1190` reports the stripped 814 (`trigger.frontmatter_parses` detail in `KnowDescriptionRule.checklist.json`), and its `parse_frontmatter` (`verifiers/verify_skill_checklist.py:472-533`) is explicitly a structural, not semantic, YAML parse — so no gate currently sees the difference.

## Counterexamples / empirical scalar tests (PyYAML 6.0.3, exit 0)

| input | result |
|---|---|
| `description: Triggers: "skill file" audit` (plain) | `ScannerError: mapping values are not allowed here` — strict loader rejects |
| `description: craft audit # not a comment` (plain) | value silently truncated to `craft audit` |
| `description: never reach the <skills> router` (plain) | parsed verbatim — `<skills>` is **legal YAML** |
| `description: >` holding both `: ` and ` #` lines | both preserved, folded to one space-joined line + trailing newline |

Two calibration consequences:

1. **The XML-tag ban is S003's, not S008's.** `corpus/SOURCES.md:16` (S003) carries “The description cannot contain XML tags”; the YAML spec has no such rule and `<`/`>` are unconstrained in plain and folded scalars. The round-47 C2 lesson should cite S003 for the tag removal and must not cite S008. `SKILL.md:151` already attributes it correctly (S001, S002, S003, S008 as a group, with “no XML tags (Anthropic rule)”).
2. **`SKILL.md:151`'s wording “quoted when it holds `: ` or ` #`” is narrower than the live file's form.** The live description holds `: ` four times and is a `>` block scalar, where quoting is neither possible nor needed; the plain-scalar restriction simply does not bind. Recommend (production edit, not mine to make): “…quoted, or written as a `>`/`|` block scalar, when it holds `: ` or ` #` …”. The §8.1.3 fact is **not** an in-place row change: `SOURCES-CONTRACT-v1.md:38-49` (fleet `.ufo/waves/kaika/`) allows only `status`, `recheck` and `used-by` to change in place, a correction is a new row whose `teaches` opens `supersedes S0NN —`, and `opened` is immutable. Since the current row is accurate for its scope, an extension would need a **new row** — proposed `S0NN`: scope `folded block-scalar form for a multi-line frontmatter description`; anchor `§8.1.3 Folded Style`; teaches `a folded > scalar folds single line breaks to spaces and (clip) keeps one final line break, so the ': ' / ' #' restriction binds only the plain form`; tier A, kind `spec`, recheck `on-release`, source `https://yaml.org/spec/1.2.2/`, supported by the 24-word quote above. Not required to close S008.

## Freshness of the version pin (on-release check)

| probe | result |
|---|---|
| `/spec/1.2/` | 200, 355 bytes — JS + meta-refresh redirect to `/spec/1.2.2/` |
| `/spec/1.2.1/` | 200, 805798 bytes, sha256 `638e172d…`, title “Version 1.2” — different document |
| `/spec/1.2.2/` | 200, 383078 bytes (pinned row) |
| `/spec/1.2.3/` | **404** — no newer patch release |

So 1.2.2 is both the current unversioned target and a distinct frozen document; the version-specific URL in the row is doing real work. `recheck: on-release` remains the right value and fires only on a new release (currently testable only by the 404 probe — no release feed was found on the yaml.org front page or `/spec/` index; the index itself is stale, “Last Updated On 2009-09-29”, and links only `/spec/1.2/`).

## Recommended row changes (old→new)

| column | old | new | basis |
|---|---|---|---|
| status | `mined` | `mined` (no change) | used at `SKILL.md:151`; content unchanged |
| recheck | `on-release` | `on-release` (no change) | 1.2.3 = 404; `/spec/1.2/` → 1.2.2 |
| used-by | `SKILL.md` | `SKILL.md` (no change) | no new consumer; the C2 tag check is S003-sourced, and `verify_skill_checklist.py` remains a structural parse |
| opened | `2026-10-19` | `2026-10-19` (no change) | the round-46 hour defect (`round-46.md:77`) does not touch the date column; contract rule 2 makes `opened` immutable |

Suggested round-47 lesson line (Sources section): “S008 re-opened 2026-10-21T15:54:20Z, HTTP 200, sha256 `2fe1bf40…` identical to round 46; §7.3.3 and §8.1.3 both present; row unchanged (`mined`/`on-release`/`SKILL.md`).”

## Commands run (all exit 0 unless noted)

- `date -u +%Y-%m-%dT%H:%M:%SZ` → `2026-10-21T15:54:09Z` (pre-fetch), `15:54:20Z` (post-fetch), `15:58:04Z` (second fetch).
- `curl -sS -L --max-time 45 -A … -o yaml1222.html -w '…' https://yaml.org/spec/1.2.2/` → `http_status=200`, `size=383078`, `time_total=0.948`; `sha256sum` → `2fe1bf40792df22e…`.
- `curl -sS -I … https://yaml.org/spec/1.2.2/` → 200, `last-modified: Wed, 30 Sep 2026 21:04:48 GMT`, `etag: "6abd7970-5d866"`.
- Second GET to `/spec/1.2.2/` → 200, 383078 bytes, same sha256.
- HEAD/GET probes `/spec/1.2/` 200 (355 B), `/spec/1.2.1/` 200 (805798 B), `/spec/1.2.3/` 404.
- `python3` + PyYAML 6.0.3 scalar tests above; `python3 -c json.load(SrcS008.json)` → ok.
- `grep -n` for `SOURCES.md:21`, `SKILL.md:3,151,456`, `verifiers/verify_skill_checklist.py:1190`, `round-46.md:70,77` → all found.

No tools were installed or upgraded; no pacman transaction was attempted.

## Not checked

- The omp/opencode JavaScript YAML loader (js-yaml) was not exercised; the 815-vs-814 measurement is PyYAML 6.0.3 only. The omp caching claim at `SKILL.md:456` is taken as the lane's earlier finding, not re-derived here.
- No lane gate was run (per contract, only read-only verifiers named in my item; `verify_skill_checklist.py` was read, not executed).
- The YAML spec errata page / yaml-test-suite were not consulted for §7.3.3 or §8.1.3.
- The cause of the 2026-09-30 `Last-Modified` (assumed a GitHub Pages rebuild; [INFERENCE]) was not verified, and the page's JSON-LD/history was not inspected.
- No check for a YAML 1.3 draft outside yaml.org's `/spec/1.2.3/` URL.
- The 1.2.1 document body was not compared section-by-section; only title, size and hash were recorded.
