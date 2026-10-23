# ScoutS049

role: scout
item: ScoutS049 — S049 Cursor `.md` rejection reason (spot-check defect 3)

No tools installed.

## Findings

1. The probe-dependent rejection sentence is the Cursor clause of one Gate bullet, committed at `corpus/lessons/round-62.md:19` (introducing commit `e6da78bbe420722dd18a13182a7c4b64ce02f005`, ancestor of base `35d44b4b4dcdda234b5dbff7af37e432fec55f05`; `git show 35d44b4b:corpus/lessons/round-62.md` line 19 is byte-identical to the worktree). The S047 clause in the same bullet is a separate, agreed 404 (spot-check §4 row above). Exact Cursor sentence:

   > Cursor's `https://cursor.com/docs/rules.md` and `https://cursor.com/docs/reference/plugins.md` `.md` forms also returned HTTP 404, with response headed `# Page not found`. These are dead URLs, not usable sources (`ScoutKeyPagesA.md:143-152,162-169,220-225`).

   Evidence: `git blame -L 19,19 -- corpus/lessons/round-62.md` → `e6da78b … 19 19`. `corpus/knowledge/erratum-absorption-round62.md` has no `S049` and no `## Gate` (the only r62 lesson Gate is `corpus/lessons/round-62.md`).

2. The seat already named the header; the lesson dropped it. `ScoutKeyPagesA.md:162-169` records the 404 under `Accept: text/markdown, text/plain;q=0.9, */*;q=0.8`: `http=404 bytes=389`, sha256 `4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1`, head `# Page not found`. `:171` says the `llms.txt` link `…/rules.md` is served, with that Accept, at `https://cursor.com/docs/rules` (already S108). `:225` is the census line the lesson compressed into "dead URLs".

3. Spot-check §4 (`corpus/lessons/round-62-verifier-spotcheck.md:133`, present at base) disagrees on the reason only:

   `| S049 Cursor `rules.md` + `reference/plugins.md` (`.md` forms) | reject | `curl` with `Accept: */*` → HTTP 200 `text/markdown` (17,252 B / 30,324 B); with `Accept: text/markdown` (the seat's header) → HTTP 404, 389 B `# Page not found` | disagree on the reason | the 404 is content-negotiation-dependent, not a dead URL; the decision (not a distinct source — S115 already holds `/docs/rules`) still holds. Routed (§6.3) |`

   §5 (`:157`) calls it "one probe-dependent rejection reason". §6.3 (`:170-172`) routes: name the `Accept: text/markdown` condition in the lesson Gate / rejection reason, and re-open whether S049's `.md` URL is minable as `text/markdown` (or state why `/docs/rules` remains canonical). The decision (reject; not a distinct source) is not routed for reversal.

4. Fresh probe, `date -u` `2026-10-23T23:04:35Z`, Chrome 131 UA, bodies in `/tmp/scout-s049` (not the lane). Same split as §4, and the two spellings are one document:

   | tag | Accept | URL | HTTP | bytes | sha256 | first line |
   |---|---|---|---|---|---|---|
   | rules_md_star | `*/*` | `…/docs/rules.md` | 200 | 17252 | `dae9d3ecd7e389fc94ee57d87911fe8d54bae1f00ce451d44303616648247ce0` | `# Rules` |
   | rules_md_md | `text/markdown` | same | 404 | 389 | `4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1` | `# Page not found` |
   | rules_md_seat | `text/markdown, text/plain;q=0.9, */*;q=0.8` | same | 404 | 389 | same `4f98eb06…` | `# Page not found` |
   | rules_seat | seat header | `…/docs/rules` | 200 | 17252 | same `dae9d3ec…` | `# Rules` |
   | plugins_md_star | `*/*` | `…/reference/plugins.md` | 200 | 30324 | `3bbf36f3320382adb68509aa758e2e764fd31c5de5f5c70c6af1683497b11204` | `# Plugins reference` |
   | plugins_md_md | `text/markdown` | same | 404 | 389 | same `4f98eb06…` | `# Page not found` |
   | plugins_seat | seat header | `…/reference/plugins` | 200 | 30324 | same `3bbf36f3…` | `# Plugins reference` |

   `rules_md_star` == `rules_seat` and `plugins_md_star` == `plugins_seat` (byte-identical). The 404 sha matches the seat's recorded body. `ctype=text/markdown; charset=utf-8` on both 200 and 404. The `.md` URL is minable as `text/markdown` only when `Accept` is not `text/markdown`. Under the counter/seat header it is not.

5. S049's `.md` URL does not become the canonical fetch URL, and the row is not retargeted. `corpus/SOURCES.md:62` source cell stays `https://cursor.com/docs/rules.md`. Its own anchor (do not rewrite):

   > § Project rules (`rules.md:32,42`), § Importing rules from a repository (`:311-313`), § Referencing files from a rule (`:127`), § Best practices (`:155,160`), § Team Rules precedence (`:307`), § AGENTS.md (`:317,321,342,357`), § FAQ (`:375`); markdown route fetched 2026-10-22T20:09:33Z (17,403 B, sha256 `884c67ca…`)

   Those line numbers still land on the live 394-line, 17,252 B body (`rules.md:32` "Project rules live in `.cursor/rules`…", `:321` "Cursor supports AGENTS.md…", `:375` "Yes. Mention a file by path…"). The anchor names the document `rules.md`; it does not claim the `.md` HTTP route is what the counter can fetch. Canonical fetch URL remains `https://cursor.com/docs/rules`, already held by S115 (`SOURCES.md:127`, teaches `re-opens S108`) which re-opens S108 (`:120`, teaches `re-opens S049`, URL `https://cursor.com/docs/rules`). Live bytes drifted off S115's recorded `884c67ca…` / 17,403 B; the anchor lines did not. `url_key` already folds one trailing `.md` (`MutFixtures.md:108-109`: both spellings → `//cursor.com/docs/rules`), so a second row for the `.md` spelling would not be a distinct source.

## Artifacts

Minimal edit: append one Gate bullet after `corpus/lessons/round-62.md:19`. Do not edit line 19, do not flip reject→admit, do not change S049's URL cell.

```markdown
- Appended (r63; the reject on the line above is unchanged): the Cursor `.md` HTTP 404 is conditional on `Accept: text/markdown` (seat header `Accept: text/markdown, text/plain;q=0.9, */*;q=0.8`, `ScoutKeyPagesA.md:162`). Re-probe 2026-10-23T23:04:35Z: `Accept: */*` returns HTTP 200 `text/markdown` (17,252 B, sha256 `dae9d3ec…` for `rules.md`; 30,324 B, sha256 `3bbf36f3…` for `reference/plugins.md`); `Accept: text/markdown` returns HTTP 404, 389 B, sha256 `4f98eb06…`, body headed `# Page not found`. They are not dead URLs. The decision stands: not a distinct source — S115 already holds `https://cursor.com/docs/rules`, and that URL under the seat header is byte-identical to the `*/*` `.md` body. SOURCES note, appended not rewritten: S049 (`corpus/SOURCES.md:62`) keeps `https://cursor.com/docs/rules.md`; its anchor still cites `rules.md:32,42` … `:375`. Canonical fetch URL under the counter's Accept remains `https://cursor.com/docs/rules`.
```

## Verdict

PROPOSES the append above. The reject stands; `/docs/rules` (S115) stays the canonical fetch URL; S049's row and `.md` URL cell stay.

Change my mind if `Accept: text/markdown` on `https://cursor.com/docs/rules.md` returns HTTP 200 with the rules body, or if `*/*` on the `.md` URL and the seat-header fetch of `/docs/rules` stop being the same bytes.
