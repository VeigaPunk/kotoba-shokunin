Result: DONE — `verifiers/check_hook_files.py` built to the `plans/round-59.md` § C1 row rule (sha256 `cfeb915de1597148dce659effb3eb2ebd5f5c25893b5aa9b8d1302fd850c0112`, 2,429 lines), self-test `0 failure(s) over 323 assertions` exit 0, base run `0 of 0` exit 1, delivered to `.ufo/waves/round-59/w0/check_hook_files.py`; 21 of 21 named mutants killed, including all 10 round-58 survivors.

# C1 counter — build receipt (wave W0, seat `ExecC1Counter`)

## 1. What was built, and where

- Lane (read-only to me): `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, my sandbox clone
  `/fast/scratch/hyaku/kotoba-r59/ExecC1Counter`, checkout `a3e70a303bab75671272498156099a65fe9b688e`
  (`git clone` then `git checkout -q a3e70a3`; `git log --oneline -1` printed
  `a3e70a3 round-59: plan draft (C1 hook files row rule, targets TBD), R1 misroot copy, bounds, census start`).
- Derived from `verifiers/check_command_files.py` at `a975cbbf`: 1,968 lines, sha256
  `aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c` (matches the sha named in my item).
- Delivered file: `.ufo/waves/round-59/w0/check_hook_files.py`, 119,123 bytes,
  sha256 `cfeb915de1597148dce659effb3eb2ebd5f5c25893b5aa9b8d1302fd850c0112`,
  byte-identical to the sandbox copy (`sha256sum` on both printed the same digest).
- Nothing else was written in the lane. No lane git write, no jj command, no fleet-root write, no
  sibling-lane write. The only lane paths I created are the two named in this item (the counter copy and
  this report). Scratch: `/fast/scratch/hyaku/kotoba-r59/ExecC1Counter/` (clone, `probe_mutants.py`,
  `.probe-mutants.txt`, `.probe-tmp/`).
- Tools installed or updated: none (no pacman, uv, npm or cargo transaction; `python3` and `curl` were
  already present; `python3 --version` not needed beyond the runs below).

## 2. The rule as implemented (constant by constant)

`SKILL.md` § `### Hook files by client`, first table `| Client | Hook config | Events | Action |`; entry
`corpus/knowledge/hook-files-round59.md`, first table `| Client | Hook config | Source | Quote |`; lesson
`corpus/lessons/round-59.md`; `BASE = a975cbbf00534443c49bf02e29c813a3db0bf0f8`; `OPENED = ("2026-10-23",)`;
`TARGET = NEW_TARGET = None`; snapshots at `.ufo/waves/round-59/snapshots/<S###>.page`.

| conjunct | implementation (line = first line of the rule) |
|---|---|
| token = first backticked span of the Hook config cell | `judge()` :892 |
| token grammar (≥2 segments, dot-led first, NOT-words in ANY segment, E7) | `token_well_formed()` :602; `NOT_HOOK_WORDS` :298; the round-58 final-segment command/prompt requirement is gone, the NOT-word ban now covers every segment |
| foreign marker / E5 | `foreign_marker()` :624; `shared_tokens()` :774; `judge()` :905 |
| Events cell: ≥2 distinct spans, each `^[A-Za-z][A-Za-z0-9_.:-]*$` | `event_spans()` :705; `events_cell_why()` :715 |
| event found on a page: case-sensitive, neighbours outside `[A-Za-z0-9_]` | `event_text()` :728; `first_event_boundary()` :743; `page_why()` :1042 |
| entry cell equals the token (E4) | `hook_cell_matches()` :768 |
| 6–25 words (E6) | `MIN_WORDS`/`MAX_WORDS` :255; `entry_row_verdict()` :806 |
| quote holds the token at segment boundaries, case-sensitive | `token_span()` :647; `first_boundary()` :980 |
| quote holds `(?i)\bhooks?\b` **outside** the token span | `HOOK_WORD_RE` :305 (with `\b`); `hook_word_outside()` :664 |
| new tier-A `mined` docs row, opened 2026-10-23, pinned host, not a base URL, not a tracker, not a change note (E3) | `entry_row_verdict()` :818 |
| quote recorded in `## Gate` | `gate_section()` :690; `quote_in_gate()` :685 |
| snapshot exists at the rev, sha256 equals the row's first full 64-hex digest, quote+token+every event on it | `row_sha()` :510; `snapshot_path()` :395; `git_show_bytes()` :377; `entry_row_verdict()` :848 |
| live page: curl `-sSL`, browser UA, Accept md, 3 attempts, HTTP 200, final URL pinned, not a base URL, not a change note, ≤5 MiB; quote+token+every event | `run_curl()` :1058; `fetch()` :1085; `page_why()` :1042 |
| G over FOUND rows, casefolded, zero held hits in the base tree outside `.ufo/` | `held_in_base()` :1211; `new_ground()` :1254; `main()` :2401 |

## 3. What changed against `check_command_files.py` (the item's change list)

1. **Renames/constants** — `BASE`, `SKILL_HEADING`, `SKILL_HEADER ("client","hook config","events","action")`,
   `ENTRY`, `ENTRY_HEADER ("client","hook config","source","quote")`, `LESSON`, `OPENED`, `SNAPSHOT_DIR`.
   `HOSTS`, `MARKERS`, E5, E7, the foreign-name guard, the host pin, tracker/change-note rejection, the
   Gate-quote check, `held_in_base`, `normalise`, `url_key`, `token_span` are carried unchanged.
2. **Token grammar** — final-segment command/prompt word dropped; `NOT_COMMAND_WORDS` → `NOT_HOOK_WORDS`
   applied to every segment (the M07/M08/M06 holes closed, see §6).
3. **Quote word** — `COMMAND_WORD_RE` → `HOOK_WORD_RE = re.compile(r"\bhooks?\b", re.IGNORECASE)`, still
   applied outside the token span (so `hooks` inside `.gemini/hooks/` does not count).
4. **Events cell** — new span parse, the ≥2-distinct + identifier rule, and a page scan at
   `[A-Za-z0-9_]` boundaries (`_` kept in the page text: `event_text` drops only tags, comments,
   script/style bodies, entities, `*` and backticks).
5. **Snapshot** — `git show <rev>:<path>` **bytes**, sha256 compared with the first full 64-hex digest in
   the SOURCES row (an ellipsis digest is no pin), then quote/token/event checks on the decoded text.
6. **Live fetch** — `urllib.request` removed; `run_curl()` runs
   `curl -sSL --max-time 30 -A '<browser UA>' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8'
   -w '\n%{http_code} %{url_effective}'`, no shell, and reads status + effective URL from the write-out
   trailer; 3 attempts; 200 required.
7. **Output/exit** — first line the exact summary, second line `counter sha256 <hex>; rev <rev>`, then one
   `reject <client>: <reasons>` per non-found row, then `targets not frozen` while either target is
   `None`. Exit 1 without `--fetch`; exit 1 (never 0) while either target is `None`; 2 = could not
   evaluate, which now **includes a SKILL.md missing at the revision** (base treated it as empty text).
   `--json` survives as a trailing machine block and never replaces the two contract lines.

## 4. Evidence (commands, exit codes, output)

All runs in `/fast/scratch/hyaku/kotoba-r59/ExecC1Counter`, `env -u GIT_DIR -u GIT_WORK_TREE
-u GIT_INDEX_FILE`, `PYTHONDONTWRITEBYTECODE=1`.

### 4.1 Self-test — `timeout 600 python3 -B verifiers/check_hook_files.py --self-test`

```
counter sha256 cfeb915de1597148dce659effb3eb2ebd5f5c25893b5aa9b8d1302fd850c0112
self-test: 0 failure(s) over 323 assertions
exit=0
```

### 4.2 Base run — `timeout 300 python3 -B verifiers/check_hook_files.py --rev a975cbbf00534443c49bf02e29c813a3db0bf0f8`

```
hook files backed on committed snapshots 0 of 0; live not run; new ground 0
counter sha256 cfeb915de1597148dce659effb3eb2ebd5f5c25893b5aa9b8d1302fd850c0112; rev a975cbbf00534443c49bf02e29c813a3db0bf0f8
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
targets not frozen
exit=1
```

`0 of 0` at the base is correct: `SKILL.md` at `a975cbbf` has no `### Hook files by client` section (the
claim's own new-ground statement, `plans/round-59.md:28-29`), so no client has a token.

### 4.3 Delivered copy — `timeout 600 python3 -B .ufo/waves/round-59/w0/check_hook_files.py --self-test`
(run from the lane root, `TMPDIR` pointed into my sandbox)

```
counter sha256 cfeb915de1597148dce659effb3eb2ebd5f5c25893b5aa9b8d1302fd850c0112
self-test: 0 failure(s) over 323 assertions
exit=0
```

### 4.4 Live curl path, once, on a pinned host (ordinary `curl`, read-only)

`date -u` → `Fri 23 Oct 2026 09:13:56 AM UTC`; one `run_curl('https://code.claude.com/docs/en/hooks.md')`:

```
status 200
effective https://code.claude.com/docs/en/hooks.md
bytes 274129
sha256 c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8
pin ok: True
PreToolUse on page: True
PostToolUse on page: True
exit=0
```

This is the only network call I made. It proves the argv, the write-out trailer split, the pin check and
the event scan against a real page; it measured no claim row.

### 4.5 Mutation battery — `timeout 900 python3 -B probe_mutants.py` (sandbox script, exit 0)

Every probe applies one named source substitution to `verifiers/check_hook_files.py`, runs the in-file
self-test, and restores the pristine bytes (hash checked after each restore). `killed 21 of 21; survived
0; pristine restored yes`. Pristine hash in the transcript: `cfeb915d…`.

Named mutations required by the item, each killed by its own arm:

| mutation | verdict | killing assertion (first) |
|---|---|---|
| events cell with 1 span (`< 2` → `< 1`) | KILLED | `one span does not pass the events cell` |
| events not checked on the page (`for name in []`) | KILLED | `page_why names the missing event` |
| event right boundary opened (`right = True`) | KILLED | `event NOT found inside a longer identifier (letter)` |
| `_` dropped from the boundary set | KILLED | `event NOT found inside a longer identifier (underscore)` |
| snapshot missing not checked | KILLED | `a missing snapshot is not backed` |
| snapshot sha not compared | KILLED | `a snapshot whose sha256 differs from the SOURCES row is not backed` |
| SOURCES row without a full 64-hex sha accepted | KILLED | `a SOURCES row without a full 64-hex sha256 is not backed` |
| hook-word-outside not checked | KILLED | `a quote without a hook word outside the token is not backed` |
| NOT-words not checked | KILLED | `red segment word: .claude/skills/hooks.json` |
| live failure counted as found | KILLED | `main: an HTTP 404 drops F to 0 and exits 1` |
| `None` targets returning 0 | KILLED | `predicate: no targets is a 1, never a 0` |

Round-58 survivors (`/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-58/build/MutC1Counter.md`
§ Surviving mutants), all ten still applicable to the derived code and all now closed:

| id | round-58 gap | this counter | killing assertion |
|---|---|---|---|
| M04 | single dot-led segment admitted | KILLED | `red segments: .hooks is one dot-led segment` |
| M06 | plural `plugins` not banned | KILLED | `red segment word: .claude-plugins/hooks.json (plural)` |
| M07 | singular `skill` not banned | KILLED | `red segment word: .claude/skill/hooks.json (singular)` |
| M08 | banned words only outside the final segment | KILLED | `red segment word: .claude/skills.json (the FINAL segment counts)` |
| M09 | E7 skips the first segment | KILLED | `red E7: .claude.local/hooks.json (the first segment too)` |
| M11 | digit allowed after a quoted/page token | KILLED | `a token followed by a digit is not spanned`, `found: a digit after the token is rejected` |
| M14 | no word boundary on the outside keyword | KILLED | `hooky is not the whole word hook` |
| M16 | E5 ignores rows with an empty client cell | KILLED | `E5: a row with an empty client cell also counts as a user` |
| M19 | hyphen accepted as a held left boundary | KILLED | `held: a hyphen before it does not hold it` |
| M20 | `lower()` used instead of `casefold()` | KILLED | `held: the casefold, not lower(), matches a long s` |

Not re-probed because the code they mutate no longer exists: **M01, M02, M03** (final-segment
command-word set and its search) — the round-59 grammar has no final-segment command/prompt word, so
those mutants have no analogue; they were killed in round 58 anyway. M05, M10, M12, M13, M15, M17, M18
were killed in round 58 and their arms are carried here (the same assertions are present and pass).

### 4.6 Lesson M71 — a successful `main()` path, end to end, on a temp repo

`corpus/lessons/round-58.md:55` (M71 `self-test-no-successful-main-path`). The self-test builds a
throw-away git repo with a base commit, a measured commit (SKILL section, entry, two SOURCES rows whose
`sha256` fields are the digests of the two committed `.ufo/waves/round-59/snapshots/S90{0,1}.page`
files, a lesson Gate) and then runs the real `main()` with `BASE`/`TARGET`/`NEW_TARGET` patched and
`run_curl` stubbed for both pins. Asserted: exit 0, the exact summary line
`hook files backed on committed snapshots 2 of 2; found on the live page 2 of 2; new ground 2`, the
exact second line, no reject line for a found row; then an HTTP 404 and a raised `OSError` each keep
S = 2 and drop F to 0 (exit 1) with the failure named on the reject line; `None` targets exit 1 with the
same summary printed; the no-`--fetch` run prints `live not run; new ground 0` and exits 1; a revision
without `SKILL.md` exits 2 and names it; and a broken Gate in a third commit exits 1 with
`1 of 2 … 1 of 2 … new ground 1` and
`reject Claude Code: entry row S900: round-59 Gate does not record this quote`.

## 5. SKILL.md § Gate registry row (exact text)

Modelled on the `check_command_files.py` row (`SKILL.md:450`), to be inserted in the same alphabetical
position (after `verifiers/check_gate_registry.py`, before `verifiers/check_infoless_fences.py`):

```
| `verifiers/check_hook_files.py` | gate | `python3 -B verifiers/check_hook_files.py --rev <rev> --fetch` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | self-test repos under `$TMPDIR` (removed); `--fetch` reads the network | kotoba |
```

Checked with the lane's own row judge rather than by eye: I imported `verifiers/check_gate_registry.py`,
read the row through `registry_rows()` and judged it against the delivered bytes —

```
rows read: 1
why: []
exit=0
```

(`judge_row` finds `0=clean` and `1=failed` for a `gate`, an exact active `--self-test` handler, `in-file`
pinned values, a non-empty non-dash write scope and owner `kotoba`.) The row must land in the same commit
as the file, or `check_gate_registry --rev` reports the file as a verifier without a row.

## 6. `verifiers/floors-registry.json` — is an entry needed?

**No.** `verifiers/check_assertion_floors.py` compares only the instruments declared in its own two
tables (`EXPECTED_INSTRUMENTS` :151, `INSTRUMENTS` :191) with `verifiers/floors-registry.json`
(`instrument_total: 14`); it has no coverage rule over `verifiers/*.py`. `check_command_files.py`,
`check_plugin_manifests.py`, `check_gate_registry.py` and the other round-58 counters have no entry
either (`grep -n "check_command_files" verifiers/check_assertion_floors.py` → no output, exit 1). So the
new counter needs no floors entry and no in-file floor.

If the L1 later wants this self-test floored, the bump-in-step rule
(`verifiers/floors-registry.json` `$comment`) needs all four edits in one change: `instrument_total`
14 → 15, a new `"hook_files": {"floor": 323, "path": "verifiers/check_hook_files.py"}` entry, a matching
row in **both** in-file tables, and the docstring's floor list. That is a deliberate, separate decision —
I did not make it, because the counter's assertion count may move when the census fixes the row set.

## 7. Risks and what the L1 must do

1. **Nothing is committed and `verifiers/` is untouched.** Integrate by copying
   `.ufo/waves/round-59/w0/check_hook_files.py` to `verifiers/check_hook_files.py` (byte-identical to
   `cfeb915d…`) and adding the § 5 row in the same commit.
2. **Targets are `None`**, as the item requires. Until the L1 sets both at freeze, the predicate is 1 and
   the run prints `targets not frozen`; a pre-freeze `--fetch` run therefore exits 1 by construction, not
   because a row failed.
3. **Worst-case wall clock of a `--fetch` run**: 7 rows × 3 attempts × `--max-time 30` = 630 s, before
   `held_in_base`. The plan pins 3 attempts and 30 s, so I did not add a global deadline. If the L1 wants
   the run bounded well under 900 s, that is a rule change to make at freeze, not a silent code change.
4. **The snapshot conjunct is unforgiving by design**: a page re-fetched after the row's digest was
   written fails as a sha mismatch even when the quote is present. The measuring seat must write the row's
   `sha256` from the exact bytes committed at `.ufo/waves/round-59/snapshots/<S###>.page`.
5. **The Events cell is also a constraint on the page**: every backticked span of the cell must appear on
   the snapshot and the live page at `[A-Za-z0-9_]` boundaries, so a cell that lists an extra illustrative
   name (or a name the page prints only inside a longer token) back-fires. This is the frozen rule
   (`plans/round-59.md:49-50`), not a counter preference.
6. **Snapshot pages must be committed, not merely written.** The counter reads them with
   `git show <rev>:.ufo/waves/round-59/snapshots/<S###>.page`, so a page that exists only in the working
   tree is "missing at the revision". `.ufo/waves/...` is **not** git-ignored here
   (`git --no-optional-locks check-ignore -v .ufo/waves/round-59/w0/ExecC1Counter.md` → no output, exit 1;
   `.ufo/waves/round-59/bounds.md` is tracked), so a plain `git add` carries them; the self-test uses
   `add -A -f` only as belt-and-braces inside its temp repo.
7. `--fetch` judges the *effective* URL, not the cited one, and never re-checks the cited URL on the live
   fetch; the cited URL is checked once, against the pin, in the backing step (round-58 behaviour).

## 8. Report file

`ls -l` on both delivered paths, captured at 06:17Z. The report's own size and mtime moved
after that capture (this section was rewritten once more), so re-run the same command for the
return-time listing; the counter's line is final (its bytes are not edited again).

```
$ ls -l /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/w0/ExecC1Counter.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/w0/check_hook_files.py
-rw-r--r-- 1 vgpnk vgpnk  18453 Oct 23 06:17 /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/w0/ExecC1Counter.md
-rwxr-xr-x 1 vgpnk vgpnk 119123 Oct 23 06:15 /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/w0/check_hook_files.py
```
