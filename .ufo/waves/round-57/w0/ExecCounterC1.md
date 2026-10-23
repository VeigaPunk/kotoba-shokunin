Result: DONE — v2 of the round-57 C1 counter (pre-data erratum, strictly stricter; seven rules E1–E7, after CtlC1RealNoForm, CtlC1DoNothingJunk and CtlC1Fabricated) is delivered as `check_plugin_manifests_v2.py`, sha256 `bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e`. The base and every control world fail it with exit 1: CtlC1RealNoForm; DoNothingJunk worlds A, B and C; and Fabricated worlds W1–W5 (v1 scored Fabricated W5 7 of 7, new ground 3, exit 0). Its self-test passes 235 of 235, and 72 of 73 guard mutations are killed; the survivor is a proven equivalent mutant.

# Round 57, w0 — C1 counter (executor ExecCounterC1)

v1 (§1–§6 below, sha256 `2ac51d2a…`) is kept unchanged as the record of what CtlC1RealNoForm broke. v2 is in §7.

## 1. Delivered file

| item | value |
|---|---|
| path | `.ufo/waves/round-57/w0/check_plugin_manifests.py` (the L1 copies it into `verifiers/`) |
| sha256 | `2ac51d2a2f50d85590c307e6ef5aab05a0b660de42a33e5657011ecc05d6305b` |
| bytes / lines | 74479 / 1598 |
| interpreter | `python3 -B`, Python 3.14.8, stdlib only (`argparse contextlib hashlib html io json re string subprocess sys tempfile urllib pathlib`) |
| shebang | `#!/usr/bin/env python3`, mode 0755 |
| sandbox clone | `/fast/scratch/hyaku/kotoba-r57/ExecCounterC1` at the base revision (every run below happened there) |

The frozen spec is stated in the module docstring (lines 26–136) and the predicate label at
line 136. Everything the item kept from round-56 v1.3 is v1.3 code: `HOSTS`, the SOURCES row
parsing (`sources_table` and its 13-pipe rule, `source_ids`, `urls_of`, `url_key`
with errata 1–3, `base_url_keys`), tier `A` + status `mined`, new-row-id and base-URL
re-citation rejection, the pinned-host map with segment-exact host/path matching
(`host_ok`, including the `..` escape rule), tracker rejection (`url_is_tracker`), the
`kind == docs` rule, the redirect checks in `fetch` (pinned hosts + base URL after redirects,
30 s timeout, 5 MiB cap, one retry), quote normalisation (`_plain`/`norm`/`norm_page`), the
`## Gate` quote requirement, and `token_at_boundary` with both left and right boundaries.

Changes the item names, all implemented: `BASE = 47c0555…`; heading
`### Plugin manifests by client` with header `| Client | Plugin manifest | What a plugin can
ship | Action |`; entry `corpus/knowledge/plugin-manifests-round57.md` with header `| Client |
Manifest | Source | Quote |`; lesson `corpus/lessons/round-57.md` `## Gate`; opened date
`2026-10-23` (a one-element tuple, so a substring such as `2026-10-2` cannot pass); the new
token grammar (plugin/extension word segment, no `marketplace` segment); the foreign-name
guard replacing `OWN_ROOTS`; `normalise()` with case preserved; the quote rules
(3–25 words, case-sensitive token containment, plugin/extension word outside the span);
`--fetch` with case-sensitive token boundaries; `G` counted over held occurrences in the
base tree; the exact output lines and the `F >= 5 and G >= 3` predicate.

Two round-56 defects are structurally fixed: the held-ground count is case-sensitive end to
end (R4), and the token search for `--fetch` is case-sensitive on a case-preserving page
rendering (the quote is still matched on the v1.3 lower-cased rendering).

### Pre-freeze change (L1 instruction, applied before any content exists)

G counts DISTINCT `casefold(normalise(token))` values, so `.Claude-Plugin/plugin.json` and
`.claude-plugin/plugin.json` on two found clients count ONCE. The held-ground test is
unchanged: it is a case-sensitive `held_in_base` lookup keyed by the case-preserved
`normalise(token)`. The implementation is the named function `new_ground(norms, held)` at
line 928, called from `main`; its exact rule is

*select the found clients whose own spelling has ZERO held occurrences, then count the
distinct casefolded values among them.*

Consequence, stated so the L1 can object before the round rather than after: when one
spelling is held at base and the other is not, the unheld spelling still contributes its
(shared) key once — the case-sensitive held test is what decides, exactly as instructed. The
self-test arms for this are "ground: two spellings of one token count once", "…a
case-sensitive held occurrence drops its own spelling", "…two different tokens count twice",
"…a held token is not new ground" and "…nothing found is zero"; mutants G53 (count
case-preserved values) and G54 (drop the zero-held filter) are both killed.

## 2. Behaviour

* First stdout line is always `counter sha256 <hex>` — `self_sha()` reads `__file__` with
  `open(..., "rb")`; it is never `sys.stdin` or a pipe. Verified equal to `sha256sum` below.
* A measured run prints `counter rev <rev>` second.
* Then `plugin manifests found on the live page F of K; new ground G` (with `--fetch`) or
  `plugin manifests backed B of K; new ground not computed (needs --fetch)` (without).
* Then one `reject <client>: <reasons>` line per rejected client, and a `BACKED` detail line
  per backed client.
* Exit 0 iff `--fetch` and `F >= 5 and G >= 3`; otherwise 1; 2 for a `--rev` that is not a
  full 40-hex hash or does not resolve to a commit, and for git/unreadable-file failures —
  message on stderr, no traceback.

## 3. Evidence (commands run in `/fast/scratch/hyaku/kotoba-r57/ExecCounterC1`)

### A. `--self-test` — exit 0

```
$ python3 -B verifiers/check_plugin_manifests.py --self-test ; echo exit=$?
counter sha256 2ac51d2a2f50d85590c307e6ef5aab05a0b660de42a33e5657011ecc05d6305b
self-test: 0 failure(s) over 184 assertions
exit=0
```

The self-test runs entirely in process. Its only filesystem work is a `tempfile` git
repository (`held_world`, line 939): five blobs plus one gitlink prove `.ufo/` exclusion,
binary skipping, case sensitivity, and the gitlink (non-blob) filter; `verify_rev` and
`git_show` are probed there too. No network.

### B. Base run without `--fetch` — exit 1

```
$ python3 -B verifiers/check_plugin_manifests.py --rev 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a ; echo exit=$?
counter sha256 2ac51d2a2f50d85590c307e6ef5aab05a0b660de42a33e5657011ecc05d6305b
counter rev 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a
plugin manifests backed 0 of 0; new ground not computed (needs --fetch)
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit=1
```

### C. Base run with `--fetch` — exit 1, and no network call

```
$ python3 -B verifiers/check_plugin_manifests.py --rev 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a --fetch ; echo exit=$?
counter sha256 2ac51d2a2f50d85590c307e6ef5aab05a0b660de42a33e5657011ecc05d6305b
counter rev 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a
plugin manifests found on the live page 0 of 0; new ground 0
reject Claude Code: … (the same seven reject lines as B)
exit=1
```

`0 of 0; new ground 0` is the specified expectation: with no content the predicate fails on
both terms. `--fetch` only fetches for BACKED clients, and there are none, so nothing is
downloaded and `held_in_base` is never called on the base tree.

### D. The delivered copy, run from the lane (read-only git)

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
$ python3 -B .ufo/waves/round-57/w0/check_plugin_manifests.py --rev 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a
counter sha256 2ac51d2a2f50d85590c307e6ef5aab05a0b660de42a33e5657011ecc05d6305b
counter rev 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a
plugin manifests backed 0 of 0; new ground not computed (needs --fetch)
… the same seven reject lines as B …
exit=1
```

The sha line equals the file's `sha256sum`, so the copy in the lane is the measured file.

`lane_dir()` resolves the repository from the report directory by walking up for
`SKILL.md` + `corpus/SOURCES.md`; once the L1 places the file in `verifiers/` the parent is
used directly.

### E. Base-tree scan on the real tree (measured, not inferred)

```
$ python3 -B - (imports the counter, calls ls_tree_blobs + held_in_base at BASE)
entries: 519
{'.ufo/waves': True, '.invented-round57/plugins': False, '.claude/agents': True}
0.05s
```

519 non-`.ufo` blobs, matching `git ls-tree -r 47c0555 | awk '$4 !~ /^\.ufo\//' | wc -l` =
519, total 3 745 962 bytes; the whole scan takes 0.05 s. A real base string
(`.claude/agents`) is held; an invented one is not.

### F. `--rev` guards — exit 2, no traceback

```
$ … --rev master
counter sha256 f37a01a6…
could-not-evaluate: --rev 'master' is not a full 40-hex commit hash
exit=2
$ … --rev 0000000000000000000000000000000000000000
could-not-evaluate: revision '0000000000000000000000000000000000000000' is not a commit in /fast/scratch/hyaku/kotoba-r57/ExecCounterC1
exit=2
$ … --rev 47c0555 --fetch
could-not-evaluate: --rev '47c0555' is not a full 40-hex commit hash
exit=2
```

### G. sha256 of the delivered bytes

```
$ sha256sum verifiers/check_plugin_manifests.py
2ac51d2a2f50d85590c307e6ef5aab05a0b660de42a33e5657011ecc05d6305b  verifiers/check_plugin_manifests.py
$ cmp verifiers/check_plugin_manifests.py .ufo/waves/round-57/w0/check_plugin_manifests.py ; echo $?
0
```

The runtime `counter sha256` line and `sha256sum` agree (both `f37a01a6…`).

## 4. R5 — guard mutation kill table

Harness: `/fast/scratch/hyaku/kotoba-r57/ExecCounterC1/mutate_guards.py` (scratch only, not
delivered). For each guard it copies the delivered bytes, applies one delete-or-negate
patch (the anchor must occur exactly once), runs `python3 -B <mutant> --self-test`, and
records the exit status: `killed` = non-zero, `SURVIVED` = still 184/184 passing.

Result: **54 killed, 0 survived, 0 not run**.

| guard | mutation | result | arm that killed it (or crash) |
|---|---|---|---|
| G01 | rev_ok: 40-hex REV_RE match | killed | a branch name is not a revision |
| G02 | verify_rev: unknown revision raises EnvError | killed | verify_rev rejects an unknown revision |
| G03 | git_show: missing path returns None | killed | git_show returns None for a missing path |
| G04 | token_well_formed: TOKEN_RE match | killed | a space makes it not well-formed |
| G05 | token_well_formed: no marketplace segment | killed | marketplace manifest is not well-formed |
| G06 | token_well_formed: plugin/extension word | killed | .claude/agents/ is not (no plugin/extension word) |
| G07 | normalise: strip one leading `~/` or `./` | killed | normalise strips one leading `~/` |
| G08 | normalise: strip ONE trailing slash | killed | normalise strips ONE trailing slash only |
| G09 | normalise: case preserved | killed | normalise PRESERVES case |
| G10 | foreign_marker: another client's marker only | killed | a .claude token is not foreign to Claude Code |
| G11 | foreign_marker: marker containment | killed | a .claude token is foreign to VS Code |
| G12 | token_span: case-sensitive find | killed | the token match is case-sensitive |
| G13 | token_span: normalised form is tried | killed | the normalised form is matched too |
| G14 | plugin_word_outside: outside the token span | killed | only the token carries the plugin word |
| G15 | quote: MIN_WORDS lower bound | killed | a two-word quote is not backed |
| G16 | quote: MAX_WORDS upper bound | killed | a 26-word quote is not backed |
| G17 | strip_quotes: surrounding pair | killed | strip straight quotes |
| G18 | entry: the quote must be recorded in the Gate | killed | a quote missing from the Gate is not backed |
| G19 | sources: an S### already at base is rejected | killed | an S### already at base is not backed |
| G20 | sources: an absent/malformed row is rejected | killed | TypeError ('NoneType' not subscriptable) on the absent-row arm |
| G21 | sources: kind docs | killed | a non-docs kind is not backed |
| G22 | sources: tier A | killed | a tier B row is not backed |
| G23 | sources: status mined | killed | a queued row is not backed |
| G24 | sources: opened date | killed | another opened date is not backed |
| G25 | sources: the row holds a URL | killed | a source cell without a URL is reported as such |
| G26 | sources: a base URL is rejected | killed | a base URL is not backed |
| G27 | sources: the host is pinned for the client | killed | an off-host URL is not backed |
| G28 | sources: tracker pages are rejected | killed | a tracker URL on a pinned host is not backed |
| G29 | judge: exactly one SKILL.md row per client | killed | a duplicate SKILL.md row disqualifies the client |
| G30 | judge: a backticked manifest token exists | killed | IndexError on the no-backtick arm (`spans[0]`) |
| G31 | judge: the foreign-name guard | killed | a token carrying another client's marker is not backed |
| G32 | judge: the action cell holds >= 3 words | killed | a two-word action cell is not backed |
| G33 | judge: no entry row is a rejection | killed | no entry row for the client is not backed |
| G34 | entry: the source cell is one S### id | killed | an entry source cell that is not one S### id |
| G35 | found_on_page: the quote is on the page | killed | found: quote absent from the page |
| G36 | token_at_boundary: the left boundary | killed | found: token only inside a URL is rejected |
| G37 | token_at_boundary: the right boundary | killed | a singular token inside the plural is not found |
| G38 | held_in_text: the left boundary | killed | held: a letter before it does not hold it |
| G39 | held_right_ok: word characters end the match | killed | held: a letter suffix does not hold it |
| G40 | held_right_ok: a dot before a word character | killed | held: a .md suffix does not hold the bare token |
| G41 | held_in_blob: binary blobs are skipped | killed | `.copilot-plugin/plugin.json` flips to True (binary blob scanned) |
| G42 | ls_tree_blobs: paths under `.ufo/` are skipped | killed | `.claude-plugin/plugin.json` flips to True (the `.ufo/` blob is scanned) |
| G43 | ls_tree_blobs: non-blob entries are skipped | killed | `.opencode/plugins` flips to True (the gitlink's blob is scanned) |
| G44 | parse_batch: only well-formed blob headers | killed | IndexError on the `… missing` header |
| G45 | predicate: F >= 5 | killed | predicate: fetch, 4 of 7, ground 3, fails |
| G46 | predicate: G >= 3 | killed | predicate: fetch, 5 of 7, ground 2, fails |
| G47 | predicate: no `--fetch` always exits 1 | killed | predicate: no fetch always fails |
| G48 | self_sha: sha256 of this file | killed | the own sha256 is 64 hex |
| G49 | summary_line: the non-fetch wording | killed | non-fetch summary line |
| G50 | main: a non-40-hex `--rev` exits 2 | killed | the usage failure is named, not a traceback |
| G51 | entry: a missing token span is a rejection | killed | TypeError on the token-less quote; world no longer backs |
| G52 | judge: the no-backtick-token rejection | killed | a manifest cell without a backticked token is reported as such |
| G53 | new_ground: distinct values are casefolded | killed | ground: two spellings of one token count once (got 2) |
| G54 | new_ground: a held spelling is not new ground | killed | ground: a held token is not new ground (got 1) |

Six rows are killed by an exception rather than a wrong value (G20, G30, G44, G51 and partly
G03/G41). The exception always lands on the exact arm input, so the mutant cannot pass; the
receipt states the mechanism rather than claiming a value-level kill.

### Guards outside the table, with reasons

1. `fetch()`'s three rejection guards (redirected off the pinned hosts, redirected onto a
   base URL, page over 5 MiB): they need a cooperating HTTP server that redirects or serves
   >5 MiB — not hermetically killable without network. They are v1.3 code, unchanged.
2. `git()`'s `OSError → EnvError` wrapper, `ls_tree_blobs`' unreadable-record guard,
   `parse_batch`'s truncated-body guard, and `lane_dir`'s not-found guard: environment
   failures that require git to be absent or to emit malformed output; not hermetically
   killable. They map to exit 2, never to a verdict.
3. Usage paths (`--rev` absent, `--self-test` combined with `--rev`/`--fetch`/`--json`):
   argparse errors, exit 2 by construction; not content rejections.
4. Non-rejection permissive branches: `token_span`'s raw-token alternative (provably
   equivalent — `normalise(t)` is always a substring of `t`, so the raw form can never be the
   only match) and `quote_in_gate`'s `gate_raw` alternative (provably equivalent — the
   backtick-stripped side is a superset of the raw side). Both are kept because the frozen
   spec names them; deleting either cannot change a verdict, so no arm can distinguish them.

## 5. Risks a reviewer should weigh

* The counter can only be validated against real content once the round-57 C1 files exist.
  Today K = 0 by construction; the judge itself is exercised only by the synthetic worlds in
  the self-test (two backed clients, one per mutation family).
* `--fetch`'s token comparison is case-sensitive against a case-preserving rendering of the
  page, while the quote is matched on the v1.3 lower-cased rendering. Consequence: a manifest
  token containing uppercase letters (e.g. `.Claude-Plugin/plugin.json`) is only FOUND if the
  page spells it identically. That is the literal reading of item 8 ("raw or normalised,
  case-sensitive") and is strictly the safer direction, but it is a deliberate choice, not an
  accident.
* G is casefold-deduplicated but the held test is not, so a round that writes both
  spellings of one manifest gets one ground value, and a base tree that already carries the
  lowercase spelling does not block the uppercase one. That is the instructed split; it means
  `G` measures "distinct manifest paths as this round spells them", not "paths absent under
  any casing".
* `skill_rows` reads only the FIRST table of the section (spec item 2), while `entry_rows`
  takes the first table that carries the entry header (spec item 3, v1.3 behaviour). A
  preamble table before the frozen SKILL header silently reads no rows.
* The SOURCES row must split into exactly 13 pipe-separated fields to be readable (v1.3); a
  row written with a different cell count is reported as "absent or malformed", not parsed.
* No install or upgrade was needed (nothing installed, no pacman transaction attempted). No
  network access was made: the base run has no backed clients, so `fetch()` was never called.

## 6. Blockers

None.

## 7. v2 — pre-data erratum after CtlC1RealNoForm (L1 instruction, 2026-10-23)

### What broke v1

The control `.ufo/waves/round-57/controls/CtlC1RealNoForm.md` met the frozen v1 predicate (`found on the live page 5 of 7; new ground 4`, exit 0). It used real text from pinned hosts but hollow tokens: a bare `plugin.json` from a CHANGELOG bullet, the nav word `Extensions`, the source file `extension.ts`, the link filename `writing-extensions.md`, and `plugins`. G also counted `Extensions` as new, because v1's held test was case-sensitive while the base holds `extensions`.

### Delivered file

| item | value |
|---|---|
| path | `.ufo/waves/round-57/w0/check_plugin_manifests_v2.py` (meant to replace v1 at `verifiers/check_plugin_manifests.py` when integrated; the docstring and predicate keep that name) |
| sha256 | `bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e` |
| bytes / lines | 91273 / 1862 |
| built from | v1, sha256 `2ac51d2a2f50d85590c307e6ef5aab05a0b660de42a33e5657011ecc05d6305b`; v1's w0 file is left untouched |

The docstring now opens with a `VERSION 2` block that names the control and the three changes. The spec text is updated where each change lands: the token grammar and its examples, a new BACKED bullet for E3, the redirect list, and the NEW GROUND paragraph with its self-test arms.

### The three changes (each only adds a way to fail)

* **E1, token grammar** (`token_well_formed(token, client)`, which now takes the row's client). A token must also have a final path segment that ends with `.json` and itself holds the plugin/extension word (split on `-`, `.`, `_`). It must also have at least two path segments after stripping one `~/` or `./`, or contain the row's own client marker (case-insensitive). Two reading choices go beyond the instruction's wording, and both are stricter:
  * A trailing `/` leaves an empty final segment, so a directory never qualifies.
  * `.json` is matched case-sensitively, so `plugin.JSON` is rejected.

  Keeps `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, `.github/plugin/plugin.json`, and `gemini-extension.json` (Gemini CLI only). Rejects `plugin.json`, `Extensions`, `extension.ts`, `writing-extensions.md`, `plugins` and `.opencode/plugins/`.
* **E2, held test** (`held_in_text`). The match is now case-insensitive. Both sides are casefolded and the boundaries are read on the casefolded line, so `.claude/AGENTS.md` still does not hold `.claude/agents` (that arm is kept). G is still the number of distinct casefold values.
* **E3, change-note URLs** (`url_is_change_note`, checked in `entry_row_verdict`). A counted row is rejected if its SOURCES URL path, percent-decoded and lower-cased, contains `changelog`, `release`, `releases`, `news` or `blog` as a substring. Only the path is checked, so a query such as `?from=blog` does not reject a docs page. I also applied the same check in `fetch` to the URL reached after redirects, so a docs URL that redirects to a changelog is not found. That adds one more way to fail and nothing else.

### Evidence (sandbox `/fast/scratch/hyaku/kotoba-r57/ExecCounterC1`)

```
$ python3 -B verifiers/check_plugin_manifests_v2.py --self-test
counter sha256 bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e
self-test: 0 failure(s) over 235 assertions
exit=0

$ python3 -B verifiers/check_plugin_manifests_v2.py --rev 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a
counter sha256 bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e
counter rev 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a
plugin manifests backed 0 of 0; new ground not computed (needs --fetch)
reject <each of the 7 clients>: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit=1

$ python3 -B verifiers/check_plugin_manifests_v2.py --rev 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a --fetch
counter sha256 bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e
counter rev 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a
plugin manifests found on the live page 0 of 0; new ground 0
reject <the same 7 lines>
exit=1

$ sha256sum .ufo/waves/round-57/w0/check_plugin_manifests_v2.py      (lane copy; cmp with sandbox = identical)
bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e
```

The lane copy's `--self-test` was also run from the lane: 235 assertions, 0 failures, exit 0.

**Control replay.** I fetched sandbox `a656c692be00793edb8c0b7296e32cdca0def688` (/fast/scratch/hyaku/kotoba-r57/CtlC1RealNoForm) into my clone and ran v2 on it. Both runs print `0 of 0` (no `--fetch`: `backed 0 of 0`; `--fetch`: `found on the live page 0 of 0; new ground 0`) and exit 1. With no client backed, nothing is fetched.

```
reject Claude Code: SKILL.md manifest token 'plugin.json' is not well-formed; entry row S101: S101 URL 'https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md' is a changelog/release/news/blog page, not documentation
reject Codex: SKILL.md manifest token 'Extensions' is not well-formed; entry row S102: S102 URL 'https://developers.openai.com/codex/changelog' is a changelog/release/news/blog page, not documentation
reject VS Code: SKILL.md manifest token 'extension.ts' is not well-formed
reject Copilot CLI: SKILL.md manifest token 'extensions' is not well-formed; no entry row names the client
reject Gemini CLI: SKILL.md manifest token 'writing-extensions.md' is not well-formed
reject Cursor: SKILL.md manifest token 'plugin' is not well-formed; entry row S105: quote holds no plugin/extension word outside the token; S105 URL 'https://cursor.com/changelog' is a changelog/release/news/blog page, not documentation
reject opencode: SKILL.md manifest token 'plugins' is not well-formed; entry row S106: S106 URL 'https://raw.githubusercontent.com/sst/opencode/dev/CHANGELOG.md' is a changelog/release/news/blog page, not documentation
```

**E2 on the base tree** (v2 `held_in_base` at `47c0555…`):

```
HELD 'extensions' held=True    HELD 'Extensions' held=True    HELD 'plugins' held=True
HELD 'plugin.json' held=False  HELD 'extension.ts' held=False HELD 'writing-extensions.md' held=False
G over the control's five found tokens: 3   (v1 counted 4)
```

**Is G ≥ 3 still reachable?** None of these well-formed real manifest paths is held at base under the case-insensitive test: `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, `.github/plugin/plugin.json`, `gemini-extension.json`, `.cursor-plugin/plugin.json`, `.vscode/extensions.json`.

### R5 on v2: 72 killed, 1 survived, 0 not run, of 73 guards

The harness is `mutate_guards_v2.py` (scratch only), run on the v2 bytes. Rows G01–G54 are the v1 guards, re-anchored where v2 changed the code. All of them are killed except G06, which is explained after the table. G04 (`TOKEN_RE`) survived the first pass: E1 already rejected the old "space" arm, so that arm no longer tested `TOKEN_RE` on its own. Two new arms (`.claude-plugin//plugin.json` and `@x/.claude-plugin/plugin.json`) fail only `TOKEN_RE`, and G04 is now killed. New and changed rows:

| guard | mutation | result | arm that killed it |
|---|---|---|---|
| G04 | drop the `TOKEN_RE` match | killed | an empty middle segment is not well-formed (TOKEN_RE alone) |
| G06 | drop the v1 "some segment has the word" check | **survived: equivalent** | none can (see below) |
| G55 | E1: drop the `.json` suffix | killed | `.JSON` in upper case is not `.json` |
| G56 | E1: drop the "final segment has the word" check | killed | the plugin word must sit in the final segment (`.claude-plugin/config.json`) |
| G57 | E1: drop "≥ 2 segments or own marker" | killed | bare `plugin.json` is not well-formed |
| G58 | E1: drop the own-marker alternative | killed | `gemini-extension.json` is well-formed for Gemini CLI |
| G59 | E1: count `~/` / `./` as a segment | killed | a leading `~/` is not a path segment |
| G60 | E2: make the held test case-sensitive again | killed | `.Claude-Plugin/plugin.json` holds lowercase (plus the `Extensions` and control-world G = 3 arms) |
| G61 | E3: drop the judge's change-note rejection | killed | a changelog URL is not backed |
| G62 | E3: match whole path segments instead of substrings | killed | a changelog URL (`changelog.md`) is not backed |
| G63 | E3: skip percent-decoding and lower-casing | killed | a change-note URL (`CHANGELOG.md`) is reported as such |

**G06 is equivalent, by proof.** E1 requires the final segment to end in `.json`, so the final segment is never empty and is one of the token's segments. E1 also requires that final segment to hold the plugin/extension word. So "some segment holds the word" is always true whenever E1 passes, and removing the v1 check cannot change any verdict. I kept it because the frozen spec lists it.

**Not hermetically killable** (in addition to v1's list): the E3 redirect check inside `fetch`. Like v1's other redirect guards, testing it needs a live server that redirects.

### Risks for the L1

* **VS Code** [INFERENCE]: E1 accepts `.vscode/extensions.json`, which is VS Code's workspace list of recommended extensions, not an extension manifest (the manifest is `package.json`). A data seat could count it unless the quote/page rules catch it. A per-client allow-list would close this, but that is a different rule and I did not add it.
* **opencode** [INFERENCE]: opencode plugins are documented as JS/TS modules in `.opencode/plugins/`. If no `.json` plugin manifest exists, opencode cannot count under E1. With VS Code also doubtful, F ≥ 5 may need all five of Claude Code, Codex, Copilot CLI, Gemini CLI and Cursor, which leaves no slack.
* **E3 false positives**: matching by substring rejects any docs path containing `news`, `blog` or `release`, e.g. a page named `release-notes-for-plugins` or `prerelease-plugins`. That is stricter, as instructed, but it can reject a genuine docs page.
* **E2 and R4**: the case-insensitive held test still keeps the segment boundary (arm: `my.Claude-Plugin/plugin.json` is not held), and the `.claude/AGENTS.md` vs `.claude/agents` arm still passes. So the round-56 R4 false match does not come back.

No installs or upgrades. No network access: neither world has a backed client, so `fetch()` was never called.

### 7b. v2 addendum after CtlC1DoNothingJunk (L1 instruction, binding)

Control `.ufo/waves/round-57/controls/CtlC1DoNothingJunk.md` world C (sandbox `f004025e98da24ca5a4559d3a22b7211e2ff4a8b`, /fast/scratch/hyaku/kotoba-r57/KotobaR57.CtlC1DoNothingJunk) met v1 with exit 0. It used bare-word tokens, quotes of 3–5 words, entry `Manifest` cells that disagreed with SKILL.md, and one token (`Extensions`) for two clients. Three more rules went into the same v2 file, in place. Each only adds a way to fail:

* **E4, entry `Manifest` cell** (`manifest_cell_matches`, checked first in `entry_row_verdict`). The cell, with backticks stripped and spaces trimmed, must exactly equal (case-sensitive) the SKILL.md token or its `normalise()` form. Otherwise that entry row is rejected with `entry Manifest cell … is not the SKILL.md token …`.
* **E5, one token per client** (`shared_tokens`, checked in `judge`). Each SKILL.md table row's first backticked span is keyed by `casefold(normalise())`. If rows of two or more distinct client names use the same key, every listed client using it is rejected with `… is shared by rows …`. I counted rows of any client name, including names outside the seven, which is stricter. Two rows for the same client are not a share; v1's duplicate-row rule already disqualifies that client.
* **E6, quote length** (`MIN_WORDS = 6`, was 3). The upper bound stays 25.

The docstring's VERSION 2 block now lists E1–E6 and names both controls. The BACKED list states E4, E5 and E6.

**Self-test** (after 7b; 235 of 235 after 7c): 227 of 227 pass, exit 0. Two v1 arms had to change. The "three words pass" arm became six-pass and five-fail arms. The foreign-marker arm now uses `.claude-plugin/other-plugin.json`, because reusing Claude's own token now trips E5 as well. New arms:
* **E4**: a mismatched cell; the mismatch reason text; a backticked cell; the `./` raw form; the normalised form; a cell that differs only in case; an empty cell; and the trim behaviour.
* **E5**: both rows disqualified; the otherwise-backed row lost; a casefold/`normalise()` share (`~/.Claude-Plugin/plugin.json/` against `.claude-plugin/plugin.json`); a row of an unlisted client name counting as a user; a duplicate row of the same client not counting as a share; distinct tokens not counting as shared.
* **E6**: a five-word quote is rejected and a six-word quote is backed.

**R5 rows for E4–E6** (the full sweep after 7b was 69 killed, 1 survived, of 70; after 7c it is 72 of 73; the survivor is still G06, the equivalent mutant explained above):

| guard | mutation | result | arm that killed it |
|---|---|---|---|
| G64 | E4: never compare the Manifest cell | killed | an entry Manifest cell that differs from SKILL.md is not backed |
| G65 | E4: accept only the raw token | killed | the normalised form of a `./` token still backs |
| G66 | E4: do not strip backticks | killed | a backticked Manifest cell still backs |
| G67 | E5: never disqualify a shared token | killed | a token shared with another client disqualifies both rows |
| G68 | E5: key on the raw span, not `casefold(normalise())` | killed | sharing is judged on `casefold(normalise())` |
| G69 | E5: count rows, not client names | killed | a token shared with another client disqualifies both rows (plus the same-client arm) |
| G70 | E6: `MIN_WORDS = 3` | killed | five words fail |

**Runs** (sandbox clone; I fetched the three DoNothingJunk sandbox commits into it). The four `--fetch` runs below were bracketed by `date -u` lines `Fri 23 Oct 2026 04:30:14 AM UTC` and `04:30:15 AM UTC`:

| world | revision | without `--fetch` | with `--fetch` |
|---|---|---|---|
| base | `47c05558…` | `backed 0 of 0`, exit 1 | `found 0 of 0; new ground 0`, exit 1 |
| CtlC1RealNoForm | sandbox `a656c692…` | `backed 0 of 0`, exit 1 | `found 0 of 0; new ground 0`, exit 1 (nothing fetched) |
| DoNothingJunk A, no sources | sandbox `e0467875…` | `backed 0 of 5`, exit 1 | not run (nothing backed) |
| DoNothingJunk B, 7 junk sources | sandbox `d6705829…` | `backed 5 of 5`, exit 1 | `found 0 of 5; new ground 0`, exit 1 |
| DoNothingJunk C, bare words | sandbox `f004025e…` | `backed 2 of 3`, exit 1 | `found 0 of 3; new ground 0`, exit 1 |

In world C, each of the five rows that v1 found now fails at least one of E1, E4, E5 or E6; the exact rejection lines are in the run output. In world B, all five fetches returned without a fetch error, and no backed row was found. That is the live-page arm working, as the control showed for v1.

**Risk (B-type worlds).** The grammar accepts invented but well-shaped paths, for example `.vscode-plugin/plugin.json` for VS Code and `.copilot-plugin/plugin.json` for Copilot CLI, because each holds its own marker or has two segments. Only the requirement that the quote and the token both appear on the cited page rejects them. That is by design, but it means the offline count (`backed`) is not evidence that a path is real.

**Out of the counter's scope; still the L1's to resolve.** The control's SKILL.md 600-line box (598 lines at freeze; a 7-row table adds 10–12 lines) is a landing blocker that this counter cannot see.

### 7c. v2 addendum 2 after CtlC1Fabricated (L1 instruction, binding)

Control `.ufo/waves/round-57/controls/CtlC1Fabricated.md` world W5 (sandbox `d450efef4944248296523f2d2e3b49d10e3f1e76`, /fast/scratch/hyaku/kotoba-r57/CtlC1Fabricated) met v1 with `7 of 7; new ground 3`, exit 0. Its rows used bare words and page-navigation strings as tokens. W4 used host and path strings as tokens, for example `agent-plugins.org/schemas/1.0.0/plugin.schema.json`.

* **E7, no host or version segment** (in `token_well_formed`). After stripping one `~/` or `./`, no path segment other than the last may contain a dot anywhere except as its first character. `.claude-plugin` and `.github` are allowed; `opencode.ai`, `agent-plugins.org` and `1.0.0` are not. I followed the instruction literally: the segment `.` alone (a dot as the first character only) is still allowed. The docstring's VERSION 2 block now lists E1–E7, and the grammar paragraph states E7.

**Self-test**: 235 of 235 pass, exit 0. The new must-fail arms:
* `Plugins` and `Extensions`. E1 already rejects both; they are now explicit arms.
* `opencode.ai/docs/plugin.json`, `agent-plugins.org/spec/plugin.json`, `opencode.ai/docs/plugins.json` and `~/opencode.ai/plugin.json`.
* `.cursor/1.0.0/plugin.json`, a version segment.

The new must-pass arm keeps `.claude-plugin/plugin.json`. The four host+path tokens pass every other rule, so E7 alone rejects them. W4's Cursor token also passes E1 and is rejected by E7 alone; I verified this on the delivered file.

**R5 for E7** (the full sweep is 72 killed, 1 survived, of 73; the survivor is still the equivalent mutant G06):

| guard | mutation | result | arm that killed it |
|---|---|---|---|
| G71 | drop E7 | killed | `opencode.ai/docs/plugin.json` is not well-formed (host segment) |
| G72 | also forbid a leading dot | killed | `.claude-plugin/plugin.json` is well-formed |
| G73 | also check the final segment | killed | `.claude-plugin/plugin.json` is well-formed |

**Runs**. I fetched the five Fabricated sandbox commits into my clone. The worlds' `--fetch` runs were bracketed by `date -u` lines `Fri 23 Oct 2026 04:32:11 AM UTC` and `04:32:23 AM UTC`; the base runs came after that.

| world | revision | without `--fetch` | with `--fetch` | exit |
|---|---|---|---|---|
| base | `47c05558…` | `backed 0 of 0; new ground not computed (needs --fetch)` | `found 0 of 0; new ground 0` | 1 / 1 |
| W1, 404 pages | sandbox `cde106783537ebb4d3784e91a8101b9b0abe48dd` | backed 6 of 6 | found 0 of 6; new ground 0 | 1 / 1 |
| W2, off-pin redirects | sandbox `04fc043e833971d54fc683b726b93cf8779d8b07` | backed 5 of 6 (Codex rejected by E3: a `/releases/` URL) | found 0 of 6; new ground 0 | 1 / 1 |
| W3, quote absent | sandbox `ca2a6f611e2f6def1a35ceac160f2c00eabaefbb` | backed 6 of 6 | found 0 of 6; new ground 0 | 1 / 1 |
| W4, token inside a URL | sandbox `2575a43eeb8a36cc1d4bb9487767e06cde1349df` | backed 4 of 4 (`plugin.json` rejected by E1; the Cursor host+path token by E7) | found 0 of 4; new ground 0 | 1 / 1 |
| W5, bare words | sandbox `d450efef4944248296523f2d2e3b49d10e3f1e76` | backed 0 of 0 | found 0 of 0; new ground 0 (every row rejected by E1, and the `Plugins`/`Extensions` rows also by E5) | 1 / 1 |

In W1–W4 the offline count still reaches 4–6, because those worlds use well-shaped invented paths such as `.vscode-plugin/plugin.json`. The live-page check is what drops them to 0, as in v1. This is the same B-type risk recorded in 7b.
