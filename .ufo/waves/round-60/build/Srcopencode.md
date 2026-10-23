Result: DONE — saved the exact opencode rules page as S109 and prepared the requested source, Gate, SKILL, and entry-note text for L1 integration.

## Findings and provenance

The W0 census classifies opencode as NOT ELIGIBLE: `AGENTS.md` guidance is directory-scoped, and the `instructions` setting adds files rather than scoping a rule to matching work files (`.ufo/waves/round-60/w0/Censusopencode.md`). Re-opened the census URL, `https://opencode.ai/docs/rules.md`, with a browser User-Agent and saved the response bytes directly to `.ufo/waves/round-60/snapshots/S109.page`.

- `timeout 10 date -u` → exit 0; stdout: `Fri 23 Oct 2026 12:09:00 PM UTC`.
- `timeout 60 curl -sSL --max-time 30 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' -w '\n%{http_code} %{size_download} %{url_effective}\n' -o /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/snapshots/S109.page https://opencode.ai/docs/rules.md` → exit 0; stdout: `200 6684 https://opencode.ai/docs/rules.md`.
- `timeout 10 sh -c 'wc -c < /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/snapshots/S109.page; sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/snapshots/S109.page'` → exit 0; stdout: `6684` and `dfb242d9a8c0cfb1c97cee74a895b56ba72cba64b558200f06eede4f5f93cb54  /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/snapshots/S109.page`.
- `timeout 10 sed -n '64p' /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/snapshots/S109.page` → exit 0; stdout: `Place an `AGENTS.md` in your project root for project-specific rules. These only apply when you are working in this directory or its sub-directories.`
- `timeout 10 sh -c 'sed -n "64p" /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/snapshots/S109.page | wc -w'` → exit 0; stdout: `23`.
- `timeout 10 sh -c 'test -s /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/snapshots/S109.page; rc=$?; printf "test_exit=%s\n" "$rc"; exit "$rc"'` → exit 0; stdout: `test_exit=0`.

The 23-word quote is unshaped: it is the complete fetched line `rules.md:64` (saved snapshot `S109.page:64`). At `rules.md:104,111`, the page describes custom instruction files and shows the `instructions` array listing paths; the page does not describe that setting as work-file matching scope [INFERENCE].

## Exact text for L1 integration

### SOURCES row S109

```text
| S109 | opencode — Rules (served docs page) — https://opencode.ai/docs/rules.md | docs | A | opencode's documented project rule-file scope and custom-instruction file list (vendor documentation, not a runtime test) | § Types → § Project (`rules.md:64`); § Custom Instructions (`:102-111`); fetched 2026-10-23T12:09:00Z (HTTP 200, 6684 B, sha256 `dfb242d9a8c0cfb1c97cee74a895b56ba72cba64b558200f06eede4f5f93cb54`) | re-opens S045 — opencode's project AGENTS.md guidance applies by directory; its `instructions` setting lists additional instruction files rather than scoping a rule to matching work-file paths | mined | 2026-10-23 | 90d | corpus/knowledge/scoped-rules-round60.md, corpus/lessons/round-60.md |
```

### Gate line for `corpus/lessons/round-60.md`

```text
- **S109 opencode** — https://opencode.ai/docs/rules.md — accessed Fri 23 Oct 2026 12:09:00 PM UTC (HTTP 200, 6684 B, sha256 `dfb242d9a8c0cfb1c97cee74a895b56ba72cba64b558200f06eede4f5f93cb54`) — `rules.md:64`: "Place an `AGENTS.md` in your project root for project-specific rules. These only apply when you are working in this directory or its sub-directories."
```

### SKILL row

Rule files cell begins with plain text, not a backticked path token; it therefore does not claim a counter token.

```text
| opencode | no scoped rule file: AGENTS.md guidance is directory-scoped, not matching-work-file scoped (S109 :64) | none (directory placement governs scope, S109 :64) | Place AGENTS.md in the project root; its guidance applies in that directory and its subdirectories (S109 :64) |
```

### Two-line entry note

```text
- **opencode (not eligible).** Project `AGENTS.md` guidance applies by directory: the project root and its subdirectories (S109 `rules.md:64`).
  The `instructions` setting names custom instruction files (S109 `rules.md:104,111`); the docs do not describe it as matching-work-file scope [INFERENCE].
```

## Gates, surfaces, and limits

- The row is explicitly an ineligible reviewer-facing record, not one of the three counted C1 rows. Its SKILL Rule files cell deliberately contains no backticked path token.
- This is vendor documentation evidence, not a runtime test. No client CLI, counter, build, or other test was run. The frozen counter was read before drafting; the opencode row is not eligible and does not claim a scoped rule token.
- This seat wrote only this report and the required S109 snapshot. SOURCES.md, `corpus/lessons/round-60.md`, `SKILL.md`, and the knowledge entry were not edited; the exact proposed text above is for L1 integration.
- No tools were installed or updated.

## Artifact paths

- Snapshot: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/snapshots/S109.page` — 6,684 bytes; sha256 `dfb242d9a8c0cfb1c97cee74a895b56ba72cba64b558200f06eede4f5f93cb54`.
- Report: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/build/Srcopencode.md`.
