Result: DONE — `verifiers/check_scoped_rules.py` (amendment A1) built, self-test 0 failures over 302 assertions (exit 0), base revision `0 of 0` (exit 1), delivered at `.ufo/waves/round-60/w0/check_scoped_rules.py` sha256 `6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440`; all 12 still-applicable round-59 survivors are killed by named assertion failures.

# ExecC1Counter — C1 counter build (round 60, W0)

Seat `KotobaR60.ExecC1Counter`, leaf. No lane content was written, no lane commit, no push, no client CLI
call, no paid model call, no tool installed or upgraded. Everything below was run in the sandbox clone
`/fast/scratch/hyaku/kotoba-r60/ExecC1Counter` (checkout `b8b2a7a271fa2dab7b679c7f3968a9e4705a1397`); the
lane was read only (`git --no-optional-locks show`, `read`, `grep`). `date -u` taken before this report:
`Fri 23 Oct 2026 10:42:30 AM UTC`.

## Delivered files

| file | sha256 | notes |
|---|---|---|
| `.ufo/waves/round-60/w0/check_scoped_rules.py` | `6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440` | 2359 lines; byte-identical to the sandbox file `verifiers/check_scoped_rules.py` (same sha256 checked on both paths) |
| `.ufo/waves/round-60/w0/ExecC1Counter.md` | this report | |

Parent file: `verifiers/check_hook_files.py` at the base, sha256
`f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71` (`sha256sum` in the sandbox). Everything
the plan does not rename is that counter's behaviour: HOSTS, MARKERS, SOURCES row parsing, `url_key`, tracker and
change-note rejection, the `## Gate` quote requirement, the token regex/segment/E7 grammar, page normalisation,
the curl header set, 3 attempts, HTTP 200, the redirect host pin, the base-URL and change-note checks, the 5 MiB
bound, and the read-only-git lane access.

## What the counter implements (draft row rule + amendment A1)

- **Table anchors**: section heading exactly `### Scoped rule files by client`; first table header
  `| Client | Rule files | Scope key | Action |`; entry header `| Client | Rule files | Source | Quote |`;
  ENTRY `corpus/knowledge/scoped-rules-round60.md`; LESSON `corpus/lessons/round-60.md`; BASE
  `31092dc6f875370bddd6eb1e4da4ca0d210c56af`; snapshots `.ufo/waves/round-60/snapshots/<S###>.page`.
- **Token**: first backticked span of the Rule files cell; path regex; ≥ 2 segments after one leading `~/`/`./`;
  dot-led first segment; no skill/agent/command/prompt/plugin/extension/hook word in any segment (`rule`,
  `rules`, `instructions` allowed); E7; foreign-marker guard. **E5 is dropped** — two rows may share a token.
- **Scope key (A1)**: first backticked span K of the Scope key cell must match `^[A-Za-z][A-Za-z0-9_-]*$` and be
  cited `S### :L`/`S###:L` to the row's own source. Line L must hold K in **key form** (K at an identifier
  boundary + optional closing `"`/`'`/backtick + spaces + `:`/`=`); value V = rest of L, or — when V is empty or
  only `[`/`|`/`>` — the **first** nonblank line among the next 3, which must begin (after spaces) with `-` or a
  quote; after stripping leading `-`, `[`, quotes and spaces, V's **first token** (to whitespace, comma or a
  closing quote/bracket) must contain `*` and consist only of `[A-Za-z0-9_./*{},!-]`. Table-cell form and the
  glob/pattern-word alternative are **removed**.
- **Action (A1)**: W = distinct content words of the cell (lowercase `[a-z]{4,}` outside backticks and
  `S### :L` citations, minus STOPWORDS); need `|W| >= 3` and at least `max(2, ceil(|W|/2))` of W on the cited
  line of the same snapshot.
- **Removed entirely**: the Events cell and its page check; the new-ground G scan (no `held_*`, `new_ground`,
  `G` in output, JSON or predicate).
- **Live (`--fetch`)**: found iff backed **and** the quote **and** a key-form site for K at **any** line are on
  the live page (same `curl -sSL`, browser UA, `Accept`, ≤ 3 attempts, HTTP 200, pinned final host, base-URL and
  change-note rejection, 5 MiB).

### Output and predicate (frozen strings)

```
scoped rule files backed on committed snapshots S of K; found on the live page F of K     # --fetch
scoped rule files backed on committed snapshots S of K; live not run                     # without --fetch
counter sha256 <hex>; rev <rev>
reject <client>: <reasons>                                                              # one per non-found row
```

Exit 0 iff `--fetch` and `TARGET` is set and `F >= TARGET`; else 1; 2 = could-not-evaluate (non-40-hex `--rev`,
unknown revision, git failure, `SKILL.md` missing, unreadable file) with no traceback. `TARGET = None` returns 1,
never 0, and still prints. Receipt label constant `RECEIPT = "C1 predicate: --fetch exit 0 (F>=TARGET)"` (also in
`--json`).

### Pinned STOPWORDS (the Action conjunct's filter)

```
about above after again against also always among another because been before being below between both
cannot could does doing down during each either else even ever every from further have having here into
itself just like many more most much must need never only other otherwise over same shall should since
some such than that their them then there these they this those through thus under until upon very what
when where whether which while will with within without would your yours
```

Domain words (`scope`, `files`, `pattern`, `rule`, `globs`) are deliberately **not** listed — dropping them would
let an invented action share words with any English line.

### `TARGET = 3` — a divergence from the ticket text, taken from the plan

The ticket said “Leave `TARGET = None`”; the plan working copy now fixes the freeze record: “**Target (frozen by
the formula): T_F = 3.** Counter `verifiers/check_scoped_rules.py` with `TARGET = 3` (built by `ExecC1Counter`;
COUNTER_LINE)” (`plans/round-60.md`, freeze-record paragraph). The interjection told me to implement the working
copy. I shipped `TARGET = 3`. If the L1 wants the counter to ship unfrozen instead, the change is one line
(`TARGET = 3` → `TARGET = None` at the constants block); the None path is implemented and armed
(“predicate: no target is a 1, never a 0”), so the behaviour is proven either way. Changing it changes this
file's sha256, and this report's sha is for `TARGET = 3`.

## Evidence (commands, exit codes, observed output)

### 1. Self-test (required)

```
$ cd /fast/scratch/hyaku/kotoba-r60/ExecC1Counter
$ TMPDIR=$PWD/.tmp timeout 600 python3 -B verifiers/check_scoped_rules.py --self-test
counter sha256 6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440
self-test: 0 failure(s) over 302 assertions
exit=0
```

`python3 -m py_compile verifiers/check_scoped_rules.py` → `compile ok`. All self-test git worlds are temporary
repositories under `$TMPDIR` (`tempfile.TemporaryDirectory`, removed on exit); the self-test writes nothing in
the lane.

### 2. Base revision (required)

```
$ TMPDIR=$PWD/.tmp timeout 300 python3 -B verifiers/check_scoped_rules.py --rev 31092dc6f875370bddd6eb1e4da4ca0d210c56af
scoped rule files backed on committed snapshots 0 of 0; live not run
counter sha256 6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440; rev 31092dc6f875370bddd6eb1e4da4ca0d210c56af
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit=1
```

At the base, `SKILL.md` has no `### Scoped rule files by client` section, so K = 0 and S = 0; the seven reject
lines are the honest “nothing read” state, not a pass.

### 3. Required arm coverage (each named mutation turns one or more arms red)

| required arm | assertion(s) in the self-test | expected |
|---|---|---|
| scope key `description` cited at a line with no pattern | `key form: description at a line with no pattern fails`; `a scope key on a line with no pattern drops the row`; `the no-pattern key is reported with its key and line` | False / row dropped |
| A1 extra: `description: "Applies to **/*.ts"` | `key form: an assigned sentence mentioning a pattern fails`; `a description whose value mentions a pattern still fails` | False |
| A1 extra: Cursor table-cell line | `key form: the Cursor table-cell line fails for {description,alwaysApply,globs}`; two judge arms | False |
| A1 extra: census lines pass | `the Cursor census line passes` (`globs: src/components/**/*.tsx`), `the Claude memory block passes` (`paths:` + `  - "src/api/**/*.ts"`), `the VS Code census line passes` (`applyTo: '**/*.py'`), `the Copilot census line passes` (`applyTo: "app/models/**/*.rb"`) | True |
| key present but cited line wrong (off by one) | `key form: an off-by-one to a line without the key fails`; `an off-by-one citation to a line without the key drops the row` | False / dropped |
| block value 4 lines down fails / 2 down passes | `key form: a block value four lines down fails`, `key form: a block value two lines down passes`, `key form: an unrelated first nonblank line leaves no value`; judge arms `a block value four lines down drops the row` / `a block value two lines down backs in the judge` | False / True |
| key only inside a longer identifier | `key form: a key inside a longer identifier fails`, `key form: a key followed by an identifier fails`; judge arm `a key only inside a longer identifier drops the row` | False / dropped |
| citation to another row's source id | `citation: another row's id is a named failure`; `a scope key citing another row's source is not backed`; `an action citing another row's source is not backed` | dropped |
| Action sharing 1 content word fails / 2 passes | `an action sharing one content word is not backed`; `action: one shared word fails`; `action: two shared words pass`; `the action shortfall is reported with its counts` | 1 fails, 2 passes |
| Action cell with no citation | `an action with no citation is not backed`; `an action on a citation line out of range is not backed` | dropped |
| snapshot sha256 mismatch | `a snapshot whose sha256 differs is not backed`; `a snapshot sha mismatch is reported as such`; `a SOURCES row without a full 64-hex sha256 is not backed` | dropped |
| quote without a rule/instruction word outside the token | `a quote without a rule word outside the token is not backed`; `the missing rule word is reported as such`; `rulebook is not the whole word rule`; `hook is not a rule word` | dropped |
| token with a NOT word (hook) | `red segment word: .claude/hooks/rules.md`, `.claude/hooks.json`, `.claude/HOOKS.json`; judge arm `a hook token is not well-formed (A1 NOT-words)` | not well-formed / dropped |
| two rows sharing a token both backed (E5 dropped) | `E5 dropped: two rows may share a token and both back` (VS Code + Copilot CLI on `.github/instructions/`) | both backed |
| successful `main()` returning 0, TARGET patched (Q48), exact line | `main: the satisfying world exits 0`, `main: the exact summary line is the first line` (`scoped rule files backed on committed snapshots 4 of 4; found on the live page 4 of 4`), `main: the second line names the counter and the rev` | exit 0 |
| live curl failure drops F while S holds | `a curl failure drops F while S holds`, `a curl failure keeps S at 4 and F at 0`, `a curl failure names the backed rows`; 404 twin arms | S=4, F=0 |
| `TARGET = None` returns 1 | `predicate: no target is a 1, never a 0`; `the unfrozen sentinel is a 1, never a 0`; `target not frozen` printed | 1 |

A1 threshold arms: `action need: {3,4,5,6,7} content words need {2,2,3,3,4}`; `a longer action needs half of its
words, not two` + `the half threshold is reported with its counts` (shares 2 of 6, needs 3).

### 4. Round-59 surviving mutants (13): what still applies and how it is killed

Probe: `/fast/scratch/hyaku/kotoba-r60/ExecC1Counter/.mutants/probe.py` — each mutant is one text substitution in
a copy of the delivered file, run as `timeout 300 python3 -B <copy> --self-test`; pristine sha before and after
was `6aea3be0…` (`identical True`). Full log `.mutants/final-probe.txt`.

| M | round-59 defect | applies here? | mutation probed | result |
|---|---|---|---|---|
| M06 | live Events checking omitted | no — the Events cell is removed by the plan; the live **semantic** conjunct is the analogue | `live_why(page, quote, None)` in `main` | KILLED, 2 assertion failures (`main: a live page without the key site drops F, not S`, `…the live key failure is named`) |
| M09 | working tree instead of measured revision | yes | `snapshot_of` reads `lane / path` | KILLED, 10 assertion failures (`main: a divergent working tree does not substitute (M09)`) |
| M12 | HTTP 201 accepted | yes | `status not in (200, 201)` | KILLED, 1 (`fetch: HTTP 201 is not 200`) |
| M13 | redirect host pin dropped | yes | `if False and pins …` | KILLED, 1 (`fetch: a redirect off the pinned hosts fails`) |
| M14 | redirect to a base URL allowed | yes | `if False and base_keys …` | KILLED, 1 (`fetch: a redirect to a base SOURCES URL fails`) |
| M15 | frozen Accept replaced | yes | `Accept: */*` | KILLED, 1 (`curl: the Accept header`) |
| M16 | bot User-Agent | yes | `-A kotoba-check-scoped-rules` | KILLED, 1 (`curl: the browser User-Agent`) |
| M17 | curl max-time disabled | yes | `--max-time 0` | KILLED, 1 (`curl: the 30 s cap`) |
| M18 | one attempt only | yes | `range(1)` | KILLED, 2 (`fetch: a transient failure is retried`, `…the retry took two calls`) |
| M19 | 5 MiB bound dropped | yes | `if False:` | KILLED, 1 (`fetch: a body over the byte bound fails`) |
| M24 | frozen F target lowered | yes — the target is now a frozen integer again | `TARGET = 2` | KILLED, 1 (`TARGET is the frozen census target: got 2, expected 3`) |
| M25 | frozen G target lowered | no — the G target does not exist in this claim (G removed) | — | not applicable |
| M26 | unfrozen guard weakened to “both None” | yes, as the single-target guard | `if not fetching and TARGET is None` | KILLED, 4 (`predicate: no fetch always fails`, `predicate: no target is a 1, never a 0`, `predicate: a frozen integer target still gates the count`, `the unfrozen sentinel…`) |

## Integration asks

### `SKILL.md` § Gate registry row (exact text, modelled on `SKILL.md:471`)

Insert after the `check_overlap_levers.py` row (the table is alphabetical by file name, so this row belongs
between `check_plugin_manifests.py` and `check_sibling_census.py`):

```
| `verifiers/check_scoped_rules.py` | gate | `python3 -B verifiers/check_scoped_rules.py --rev <rev> --fetch` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | self-test repos under `$TMPDIR` (removed); `--fetch` reads the network | kotoba |
```

Checked against `verifiers/check_gate_registry.py`'s rule: kind `gate`; entry command contains the path; verdict
map declares `0=clean` and `1=failed` once each; `--self-test` is an exact `add_argument` handler in the file;
pinned values `in-file` (allowed for a gate, `none` is not); non-empty write scope; owner `kotoba`.

### `verifiers/check_gate_registry.py` — an entry IS required

Its universe is “every blob directly under `verifiers/` at the revision whose name ends in `.py` or `.sh`”. Once
`verifiers/check_scoped_rules.py` lands, a missing (or non-conformant) registry row makes the counter print
`gate registry rows conformant K of M` with K < M and exit 1. Hence the row above is mandatory at integration.

### `verifiers/floors-registry.json` — no entry required

Read both the registry (`instrument_total: 14`; instruments `alwayson, checklist, compare_harness_independent,
corpus_independent, corpus_integrity, correction_sweep, dispatch_prompts, floors_guard, harness,
harness_independent, overlap_levers, pins, sibling_census, surfaces`) and `verifiers/check_assertion_floors.py`
(`EXPECTED_INSTRUMENTS` at :151, `INSTRUMENTS` at :191, cross-checked against the JSON at :418). Neither lists
`check_hook_files.py` nor `check_command_files.py`, so claim counters are not floored by that guard. Adding one is
a four-place bump-in-step edit (`floors-registry.json` + `instrument_total`, both in-file tables, and the guard's
own docstring/count) — optional, and I did not do it. The self-test prints `302 assertions` if the L1 later wants
the floor.

## Risks and limits

- **`TARGET`**: shipped as `3` per the plan's freeze record (see above). The predicate is therefore live: a
  `--fetch` run with F ≥ 3 exits 0. If the L1 meant the counter to ship unfrozen, flip the constant before the
  freeze commit and re-issue the sha.
- **A1 removes the table-cell key form**: a Markdown-table key line (`| `alwaysApply` | `description` | `globs` |`)
  can never be a key site. That is the amendment's intent (it kills the Cursor :65 false pass), but it also means
  a client page that documents its key only inside a table cell cannot count.
- **The key/value test is line-based on the raw page bytes** ([INFERENCE]): a live HTML page that splits the key
  and its value across tags/lines fails unless the block-line rule applies; the committed snapshot and the live
  page are held to the same test, so a snapshot taken from an HTML page can fail where a Markdown page passes.
  The census lines the L1 listed are Markdown frontmatter, so this does not affect the recorded eligible rows.
- **Live quote requirement is strict**: the live page must still carry the 6–25-word verbatim quote; a page that
  rewords prose between the snapshot and the measured run drops F while S holds.
- **No live fetch was made by this seat** (the self-test mocks `run_curl`; no C1 run with `--fetch` was issued
  against the network). F is unmeasured here by design; the census and the L1's fetch records are the evidence
  for the pages.
- **Action conjunct limit** (stated in the plan itself, not mine): a cell built from the cited line's own words
  passes even if it inverts the line's meaning; the `Cells<Client>` falsify seats own that reading.
- The `--json` projection carries `backed`, `of`, `found`, `target`, `receipt` and the per-client report; no G.

Report: .ufo/waves/round-60/w0/ExecC1Counter.md
