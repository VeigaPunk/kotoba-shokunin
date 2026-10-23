# Round 57, w0 — C1 counter (executor ExecCounterC1)

Result: DONE — the frozen round-57 C1 counter and this receipt are delivered; it runs at
`47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a` as `backed 0 of 0` and `found on the live page 0 of
0; new ground 0` (exit 1 both ways, as specified for a base with no content), its self-test
passes 184 of 184 assertions, and all 54 guard mutations are killed by it.

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
