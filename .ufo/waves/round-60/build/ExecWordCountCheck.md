Result: DONE — `check_word_counts.py` is delivered (199 lines, sha256 `aa909434…`, already committed at `.ufo/waves/round-60/build/`, bytes identical at tip `7b80ae8`), `--self-test` green over 20 assertions, the mined `round-59.md:27` flagged at exit 1 and a commanded fixture clean at exit 0; two limits are measured rather than assumed — the requested **probe-kind registry row is non-conformant** under the lane's frozen `check_gate_registry.py` at the tip (conformant `gate` row delivered beside it), and the check **over-reports on the fixed `round-60.md`** at lines 41 and 52 under its forward-only window.

# ExecWordCountCheck — round-60 build wave

Assignment: a stdlib check `verifiers/check_word_counts.py` (`--self-test`, exit 0/1/2) that, for a lesson file at a revision (`--rev <rev> --file <path>`), flags every line stating `<N> words` / `<N>-word` whose line or the next 2 lines carry no `wc -w` command. Run it on `corpus/lessons/round-59.md` @ `31092dc6…` (expect exit 1 naming the 29-words line) and on a fixture that carries the command (exit 0). Deliver the file, its sha256, both outputs, and a Gate-registry row (probe kind). Under 200 lines.

Everything below was run in my own sandbox clone `/fast/scratch/hyaku/kotoba-r60/ExecWordCountCheck` (reset to sandbox commit `aaee79b`, which holds the delivered bytes). Lane reads were `git --no-optional-locks … show` only; no git write, no jj command, and no checkout ran in the lane.

## 1. Delivered files

| File | sha256 | Bytes | Lines |
|---|---|---|---|
| `.ufo/waves/round-60/build/check_word_counts.py` | `aa909434ef078f9964fe8541b0c27be91561cdccd30ba79ecd08bfbd715fe991` | 9,279 | 199 |
| `.ufo/waves/round-60/build/check_word_counts.fixture.md` | `66d07e37531d3e68b6c65f36122f71dfd660afff82a4b2eb1df5ce0d07bbca22` | 428 | 8 |

```
$ sha256sum .ufo/waves/round-60/build/check_word_counts.py .ufo/waves/round-60/build/check_word_counts.fixture.md
aa909434ef078f9964fe8541b0c27be91561cdccd30ba79ecd08bfbd715fe991  .ufo/waves/round-60/build/check_word_counts.py
66d07e37531d3e68b6c65f36122f71dfd660afff82a4b2eb1df5ce0d07bbca22  .ufo/waves/round-60/build/check_word_counts.fixture.md
$ wc -l .../check_word_counts.py
199 .../check_word_counts.py
```

The delivered `.py` is byte-identical to `verifiers/check_word_counts.py` in sandbox `aaee79b` (`sha256sum` of both prints `aa909434…`). Bound "under 200 lines" holds at 199.

The fixture is a receipt file my item names, in the report dir, so the exit-0 run is re-runnable without inventing a lane path. Its body (the exit-0 evidence depends on these exact bytes):

```
# Fixture — a stated word count that carries its counting command.

The same shape as the mined line, with the command the rule asks for.

- **Gemini CLI hooks-overview quote** — reject: 29 words, above the 25-word cap; the counting command is pasted on the next line.
  `sed -n 94,97p` cut at the token | `wc -w` -> 25

- **best-practices quote** — admit: a 10-word quote, counted by `printf %s '<quote>' | wc -w` -> 10.
```

## 2. What the check does (lexical, and named as lexical)

- **Claim form** — `COUNT_RE = (?<![0-9A-Za-z])(\d+)(?:[ \t]+words\b|[ \t]*-[ \t]*words?\b)`: the plural space-separated form (`29 words`) and the hyphen form (`25-word`, `10-word`, `25-words`).
- **Command form** — `WC_RE = \bwc[ \t]+-\w*w\b`: `wc -w`, `wc  -w`, `wc -lw`. `wc -c` and `wc -l` deliberately do **not** count as the counting command (both asserted in the self-test).
- **Window** — `WINDOW = 2`; the check joins `lines[i:i+3]`, i.e. the line itself plus the next two. A command on the fourth line does not rescue the claim (asserted).
- **Reads committed bytes** — `git --no-optional-locks -C <repo> show <rev>:<path>`. A bad revision or absent path is exit 2 with the git error on stderr, never a silent pass.
- **Repo resolution** — `--repo`, else the first `.git` walking up from `__file__`, else from cwd. Verified cwd-independent: running the delivered copy from `/tmp` still finds the lane and exits 1 with the same finding.
- **Exit map** — 0 = clean, 1 = a stated count carries no counting command, 2 = could-not-evaluate. Stdlib only (`argparse`, `contextlib`, `io`, `re`, `subprocess`, `sys`, `tempfile`, `pathlib`).

It is **not** a truth test: it does not re-count anything and does not decide whether a stated number is right. It decides only whether a stated number is accompanied by the command that produced it — which is exactly the M85 / round-59-R1 class.

## 3. Required outputs

### RUN A — `corpus/lessons/round-59.md` @ `31092dc6f875370bddd6eb1e4da4ca0d210c56af` → exit 1, naming the 29-words line

```
$ python3 -B verifiers/check_word_counts.py --rev 31092dc6f875370bddd6eb1e4da4ca0d210c56af --file corpus/lessons/round-59.md
corpus/lessons/round-59.md:27: stated word count (29 words, 25-word, 10-word) with no `wc -w` command on this line or the next 2
    - **Gemini CLI hooks-overview quote** — reject: 29 words, above the 25-word cap (`CensusGeminiCLI`); the best-practices page carries a 10-word quote.
stated word counts without a counting command: 1 of 1 claimed lines
EXIT=1
```

Line 27 is the mined line; the check names it and lists all three counts it states. `round-59.md` at that revision states exactly one word-count line and it is this one (`1 of 1 claimed lines`), so the finding is the whole class, not a sample.

### RUN B — fixture that carries the command → exit 0

```
$ python3 -B verifiers/check_word_counts.py --rev aaee79bf8c5649860958353a315c882fcad4ca29 --file verifiers/fixtures/check_word_counts/with-command.md
stated word counts without a counting command: 0 of 2 claimed lines
EXIT=0
```

`aaee79b` is the sandbox commit (`/fast/scratch/hyaku/kotoba-r60/ExecWordCountCheck`) that holds the fixture at `verifiers/fixtures/check_word_counts/with-command.md`. Both claimed lines pass: line 5 has `wc -w` two lines down, line 7 has it on the same line.

### RUN C — could-not-evaluate holds

```
$ python3 -B verifiers/check_word_counts.py --rev deadbeefdeadbeefdeadbeefdeadbeefdeadbeef --file corpus/lessons/round-59.md
could-not-evaluate: git show deadbeef…:corpus/lessons/round-59.md failed: fatal: path 'corpus/lessons/round-59.md' exists on disk, but not in 'deadbeef…'
EXIT=2
```

A missing path also exits 2 (same shape, `does not exist in '<rev>'`).

## 4. Shown able to fail — self-test and two mutants

```
$ python3 -B verifiers/check_word_counts.py --self-test
self-test: 0 failure(s) over 20 assertions
EXIT=0
```

The 20 assertions cover: same-line command clean; command on next line clean; command two lines down clean; command three lines down flagged; hyphen form flagged; prose with no number clean; `600 lines, 8 columns, 2 seats` clean; `wc -c` and `wc -l` do not rescue; the mined line flagged once at line 1 with `['29 words', '25-word', '10-word']`; a clean file flags nothing while still counting one claimed line; command four lines down flagged.

Three are **main-path arms** over a real temp git repo (`git init`/`commit` under `$TMPDIR`, removed) calling `main()` and asserting the returned code — the M71 lesson: a self-test that never runs the successful main path proves nothing. Pinned: `bad.md` → 1, `good.md` → 0, `absent.md` → 2, and `"bad.md:1"` appears in the captured output.

Mutants (both show the check is load-bearing, not decorative):

```
$ # M1: WINDOW 2 -> 0
$ python3 -B /tmp/mut.py --rev aaee79b… --file verifiers/fixtures/check_word_counts/with-command.md
verifiers/fixtures/check_word_counts/with-command.md:5: stated word count (29 words, 25-word) with no `wc -w` command on this line or the next 0
    - **Gemini CLI hooks-overview quote** — reject: 29 words, above the 25-word cap; the counting command is pasted on the next line.
stated word counts without a counting command: 1 of 2 claimed lines
MUT_EXIT=1
```

```
$ # M2: search the whole file for the command instead of the 2-line window
$ python3 -B /tmp/mut2.py --self-test
FAIL command three lines down: got [], expected [1]
FAIL command four lines down: got [], expected [1]
self-test: 2 failure(s) over 20 assertions
MUT2_SELFTEST_EXIT=1
```

M2 is the important one: the mutant's *live* run on `round-59.md` still exits 1 (that file has no `wc -w` anywhere), so the live run alone would not have caught it. The self-test does. That is why the window assertions are pinned rather than sampled.

## 5. The Gate-registry row — the requested probe kind is measured non-conformant

The assignment asks for a **probe-kind** row. The lane's frozen `verifiers/check_gate_registry.py` rejects a probe row whose verdict map declares `1=failed` **or** whose source has an exact active `--self-test` handler. The check needs both (the assignment requires `--self-test` and exit 1 = failed), so the two requirements are in direct conflict. I measured every configuration instead of guessing; each is a real sandbox commit run through the frozen counter.

| # | Configuration | Counter exit | Per-row verdict |
|---|---|---|---|
| A | **probe**, cell `` `--self-test` ``, map declares `1=failed` | **1** | `probe verdict map declares 1=failed; probe script has an exact --self-test handler` — 33 of 34 |
| B | **probe**, cell `none`, map without `1=failed` | **1** | `probe script has an exact --self-test handler` — 33 of 34 |
| C | **gate**, cell `` `--self-test` ``, file live under `verifiers/` | **0** | `OK` — **34 of 34**, phantom 0 |
| D | gate row, but the check delivered only to the wave dir | **1** | `PHANTOM verifiers/check_word_counts.py` — 33 of 33, phantom 1 |
| E | probe row naming the **wave-dir** path, check only in the wave dir | **0** | 33 of 33, phantom 0 — the row is outside the counter's universe, so it is neither checked nor flagged |
| F | baseline, no new verifier | **0** | 33 of 33 |
| G | **probe**, script's flag spelled `--selftest`, cell `` `--selftest` `` | **0** | `OK` — **34 of 34** (variant `--selftest` exit 0, 20 assertions) |
| H | **probe**, script's flag spelled `--selftest`, cell `none` | **0** | `OK` — **34 of 34** |

Reproduce A–F with `python3 -B /fast/scratch/hyaku/kotoba-r60/measure_registry.py`; G–H with `measure_probe_selftest.py` (both scripts kept outside the clone so `git clean` cannot eat them).

### 5.1 At the current lane tip — the actionable numbers

The lane advanced while I worked: tip is now `7b80ae8` (`round-60: C1 data — SKILL § Scoped rule files by client, …`), which **already commits my check** at `.ufo/waves/round-60/build/check_word_counts.py` (bytes identical: `sha256sum` of the committed blob and of the worktree file both print `aa909434…`). It has **not** been landed under `verifiers/` and there is **no** `check_word_counts` row in `SKILL.md`. `SKILL.md` is 591 lines, `verifiers/` holds 34 blobs (the L1 added `verifiers/check_scoped_rules.py`), and the frozen counter reads 34 of 34, phantom 0.

Measured against that tip (`python3 -B /fast/scratch/hyaku/kotoba-r60/measure_at_tip.py`):

| # | State at tip `7b80ae8` | Counter exit | Output | SKILL.md |
|---|---|---|---|---|
| I | unchanged: check only in the wave dir, no row | **0** | `34 of 34 … phantom 0` | 591 |
| J | **probe** row pasted, check **not** under `verifiers/` | **1** | `PHANTOM verifiers/check_word_counts.py`; 34 of 34, phantom 1 | 592 |
| K | **gate** row pasted, check **not** under `verifiers/` | **1** | `PHANTOM verifiers/check_word_counts.py`; 34 of 34, phantom 1 | 592 |
| L | **gate** row pasted **and** check+fixture landed under `verifiers/` | **0** | `verifiers/check_word_counts.py OK`; **35 of 35**, phantom 0 | 592 |
| M | **probe** row pasted **and** check landed under `verifiers/` | **1** | `probe verdict map declares 1=failed; probe script has an exact --self-test handler`; 34 of 35 | 592 |

So the two failure modes are independent and both real at this tip: **J/K** — a row without its file is a phantom whatever the kind; **M** — the file with a probe row is a non-conformant row whatever the file's location. Only **L** leaves the frozen counter green, and **L** is the `gate` kind. The requested probe kind has no conformant landing at this tip; this is the M70/M77 shape the lane already carries.

**Reading of the matrix.**

- A and B: a probe row naming `verifiers/check_word_counts.py` is rejected **whichever** way the row is written, because the rejection is keyed on the *source*, not the cell. Dropping `1=failed` (B) only removes one of the two reasons.
- C: the conformant row for this script is `gate`. This is the row I deliver as the primary.
- D: if the L1 lands the check **only** in `.ufo/waves/round-60/build/` but adds a row naming `verifiers/check_word_counts.py`, the counter reads a **phantom** and goes to 33 of 33, exit 1. Row and file must land together, or the row must name the wave path (E).
- E: a row naming the wave path is invisible to the counter — it neither conforms nor is flagged. That is a *silent* row, not a passing one; it registers nothing.
- G/H: the only way to make a **probe** row conform is the other self-test spelling PROTOCOL § Gate standard allows (`--selftest`), because the frozen rule matches the literal string `--self-test`. That is a spelling coincidence, not a semantic difference — I do not recommend using it to get a probe label, because the check genuinely fails (§4) and PROTOCOL defines a probe as "a tool that cannot fail".

**Rows, ready to paste into `SKILL.md` § Gate registry immediately after the `check_sweep_mutants.py` row (alphabetical: `check_sources_append_only` … `check_substrate_pins`, `check_sweep_mutants`, `check_word_counts`, `compare_harness_independent`):**

Primary — the row that measures conformant (C):

```
| `verifiers/check_word_counts.py` | gate | `python3 -B verifiers/check_word_counts.py --rev <rev> --file <path>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none; read-only | kotoba |
```

The row the assignment literally asked for (probe), **measured non-conformant** at the tip (config M: 34 of 35, exit 1) — do not land it unless the L1 also accepts `check_gate_registry.py` going to exit 1:

```
| `verifiers/check_word_counts.py` | probe | `python3 -B verifiers/check_word_counts.py --rev <rev> --file <path>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none; read-only | kotoba |
```

Alternative that keeps the probe label and conforms (G, measured at the base rev) — requires also renaming the flag in the script, body identical otherwise:

```
| `verifiers/check_word_counts.py` | probe | `python3 -B verifiers/check_word_counts.py --rev <rev> --file <path>` | 0=clean, 2=could-not-evaluate | `--selftest` | in-file | none; read-only | kotoba |
```

I deliver the primary (`gate`) row; the other two are here so the L1 can choose with the measurement in hand rather than on my recommendation alone. This is the M70/M77 shape the lane already carries: the plan's `probe` relabel fails the registry gate. Note that whichever row is chosen, configs J/K hold: **the row and `verifiers/check_word_counts.py` must land in the same commit**, and the fixture should land with them.

**Budget cost.** The row is one line, measured: `SKILL.md` is 591 lines at tip `7b80ae8` and 592 with the row (table §5.1). The `trigger.line_budget` box states 600, so the row fits with 8 lines to spare — but if `ExecBudgetMove` sized its move-out against the old 587 figure it must re-check, because the C1 landing already spent 4 of those lines. At the freeze `b1cd64bb…` and at the base `31092dc6…` the file was 587 (`git --no-optional-locks show <rev>:SKILL.md | wc -l` → 587 both).

## 6. Scope and limits, stated plainly

- **It flags the fixed lesson. Measured, and the most important limit here.** At lane tip `7b80ae8`, where `corpus/lessons/round-60.md` carries the R1 correction and M86, the check exits **1** with two findings — and **both are false positives** under the rule's own intent:

```
$ python3 -B .ufo/waves/round-60/build/check_word_counts.py \
    --repo /fast/scratch/hyaku/kotoba-r60/ExecWordCountCheck \
    --rev 7b80ae80cda69a95b6fc90879395113a99a57912 --file corpus/lessons/round-60.md
corpus/lessons/round-60.md:41: stated word count (10-word) with no `wc -w` command on this line or the next 2
    and a list item), not on the cap; the unshaped 10-word `best-practices.md:413` quote names the same token.
corpus/lessons/round-60.md:52: stated word count (29 words, 25-word, 10-word) with no `wc -w` command on this line or the next 2
    - **Gemini CLI hooks-overview quote** — reject: 29 words, above the 25-word cap (`CensusGeminiCLI`); the best-practices page carries a 10-word quote.
stated word counts without a counting command: 2 of 6 claimed lines
EXIT=1
```

  - **Line 41** is the tail of the R1 correction bullet. Its counts *are* commanded — `sed -n '94,97p' hooks.md | wc -w` at lines 37 and 38 — but the bullet wraps, so the command sits three lines above the claim and the **forward-only** window (41, 42, 43) cannot see it.
  - **Line 52** is the mined line quoted **verbatim** inside the M86 evidence fence (fence opens line 50, closes line 54), reproducing the check's own output as "shown able to fail". Its `wc -w` text is on line 51 — one line *above* — so the forward window (52, 53, 54) misses it, and lines 53/54 are the output summary and the fence.
  Consequence: **the check cannot be used as a gate over `corpus/lessons/round-60.md` at this tip** without one of (a) a symmetric window covering the enclosing bullet, (b) skipping fenced blocks that quote the checker's own output, or (c) accepting a command anywhere in the bullet. I did **not** widen the rule: the assignment fixed it as "the line or the next 2 lines", and a check that quietly redefines its own window is not the artifact that was asked for. The two instances are named so the L1 can decide — the rule is right for the class and wrong for long wrapped bullets and quoted evidence.
- **The lesson cites an older copy of this check.** `corpus/lessons/round-60.md` at `7b80ae8` records "The tested checker copy had sha256 `10323e55eefdd61d7e723f4d159acb7c83785cdbccd503e82b64c5c1a4a3b644`". That is the 175-line intermediate (`--self-test`: 16 assertions, pre-main-path arms), **not** the delivered artifact (`aa909434…`, 199 lines, 20 assertions). The quoted output in the lesson is byte-identical to what the delivered check prints (RUN A), so no claim in the lesson is wrong — but the sha no longer names the shipped file, and the lesson's own hedge ("not claimed as … that seat's final artifact") should be replaced with `aa909434…` at integration.
- **Lexical, and it over-reports one further shape.** A *cap* or a *size estimate* is flagged like a measured count: `round-54-verifier-spotcheck.md:181` (~100 words is a size estimate) and `round-54-verifier-spotcheck.md:218` are flagged. Deliberate for this class — M85 asks for a command beside every stated count — but it cannot replace a reviewer's judgement on `~N` and "at the cap" wording.
- **One finding per line, not per count.** Line 27 of `round-59.md` states three counts and is flagged once with all three listed. The verdict is per line, matching the assignment's wording.
- **Adjacent lines share a window.** If line *i* and line *i+1* both claim counts and one `wc -w` sits two lines below *i*, both pass. This is the stated rule, not a bug, but it is the way the check is weakest (the mirror image of the line-41 miss above).
- **Scope measured only where I ran it.** I ran it on `round-59.md` (the mined file), on the commanded fixture, and on `round-60.md` at the tip. The base-rev sweep found **no** committed lane file that exits 0 *with* a claimed count, which is why the fixture is a delivered file rather than an existing path; corpus files with 0 claimed lines (e.g. `round-1.md`, `round-58.md`) exit 0 vacuously and are not evidence. A narrower "N of M" line on `round-54`/`round-55`/`round-59-verifier-spotcheck.md` also fires (9, 2 and 2 lines respectively) — those are real under the rule, unchecked by me line-by-line.

## 7. Files changed

- `.ufo/waves/round-60/build/check_word_counts.py` — new; the L1 has since committed it at tip `7b80ae8`, bytes identical (199 lines, sha256 `aa909434…`).
- `.ufo/waves/round-60/build/check_word_counts.fixture.md` — new, the commanded fixture the exit-0 run reads (sha256 `66d07e37…`); still untracked at `7b80ae8`.
- `.ufo/waves/round-60/build/ExecWordCountCheck.md` — this report; still untracked at `7b80ae8`.

Nothing else was written in the lane; no lane file was edited by me (the L1 integrates — the row texts in §5 are for you to paste, and the check file is for you to `cp` to `verifiers/check_word_counts.py`). Sandbox-only artefacts, not deliverables: `/fast/scratch/hyaku/kotoba-r60/ExecWordCountCheck` (clone; commits `sandbox 60b6f98`, `sandbox aaee79b`, plus the throwaway measurement commits named in §5/§5.1), `measure_registry.py`, `measure_probe_selftest.py`, `measure_at_tip.py`, `/tmp/mut.py`, `/tmp/mut2.py`, `/tmp/variant_selftest.py`, `/tmp/wc_bundle/`.

No tool was installed or upgraded.

## 8. Blockers and risks

- **No blocker.** The one decision that is not mine: the probe-vs-gate row kind (§5, §5.1). The measurement is complete and the conformant row is delivered; at the current tip the probe row costs `check_gate_registry.py` exit 1 (34 of 35, config M).
- **Risk if the row is landed before the file** — configs J and K, both exit 1 with `PHANTOM verifiers/check_word_counts.py`. `verifiers/check_word_counts.py` and the row must land in the same commit, and `check_gate_registry.py --rev <tip>` must be re-run after both.
- **Risk of the exit-0 fixture going stale** — the fixture must travel with the check; if only the check is committed, RUN B has no revision to read and the exit-0 evidence cannot be re-run. Land `verifiers/fixtures/check_word_counts/with-command.md` too, or keep the delivered fixture beside the check.
- **Risk if `--self-test` is renamed to `--selftest` just to win the probe label** — §5 G/H show it conforms, but the check then still fails on a violation (exit 1), which contradicts PROTOCOL § Gate standard's "a tool that cannot fail is a probe". I recommend `gate` and did not ship the renamed variant.
