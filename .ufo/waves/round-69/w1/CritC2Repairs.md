---
seat: CritC2Repairs
round: 69
wave: 1
lane: kotoba
axis: consistency
claim: C2
base: a5f7459f99bb27bf697e9438362e75ac5833eca8
plan-tip: a238989a96cb0d2b939679126b832d75b861ca6e
date: 2026-10-25
---

# C2 attack — does `r68 routed defects closed 8 of 8` close the eight routed defects?

## Verdict

**No.** Four of the eight checks (D3, D5, D6, D7) are weaker than the routed defect they claim
to close, and two of those (D3, D6) make the frozen predicate **unreachable** at the draft tip.
A sandbox reproduction of the lane's current working tree prints:

```
measured-rev: e13cb47bb298a216859dd8e416182eb2edaab6e3     (sandbox-only commit of the working tree)
r68 routed defects closed 4 of 8
  - D3: verifiers/check_r67_routed_repairs.py still runs `git checkout` (a git write in the lane)
  - D6: corpus/lessons/round-69.md § Mistakes has no row naming R68-6 and S201
  - D7: .ufo/waves/round-68/w1/controls/c2falsify-clone/ is neither committed nor dispositioned
  - D8: baseline corpus.index.tracked_files expects 124, the gate measures 127   (+3 more D8 drifts)
exit=1
```

The counter's own `--self-test` **does** pass at the branch tip (`a238989`):
`self-test: 0 failure(s) over 23 assertions`, exit 0. It cannot catch any finding below, because
its honest world is a dict whose receipts, entry, lesson and tracked set are all hand-shaped to
the checks.

## Method

- Read `plans/round-69.md` (frozen), `corpus/lessons/round-68-verifier-spotcheck.md` § Routed
  defects, `verifiers/check_r68_routed_repairs.py` (483 lines, both halves read), the repaired
  `verifiers/check_r67_routed_repairs.py`, the draft `corpus/lessons/round-69.md`,
  `corpus/SOURCES.md` S198–S208, `corpus/README.md`, `corpus/QUALITY.md`,
  `corpus/knowledge/client-trust-gates-round68.md`, all ten `recapture/*.txt`, and both C2 controls.
- Ran `--self-test` at `a238989` in a `git clone --shared` sandbox under `/tmp` (never in the lane).
- Re-ran six receipts at their cited revisions; re-ran both r67 counter arms at `e94ae32`/`2cf0d99`;
  reproduced the base control (`0 of 8`, exit 1).
- Built the repaired tip **in /tmp** (`git clone --shared`, then the lane's working tree copied in,
  `git add -A`, throwaway commit `e13cb47`) and ran the counter and the corpus gate against it.
  The lane's index, working tree and jj state were never written.
- Proved each check hole with the counter's own `FakeRepo`/`_honest()` harness and with a real
  one-line git commit in a throwaway clone.

## Per-defect verdicts — closure wording vs the check

| # | Routed defect (closure's words) | Counter check | Verdict |
|---|---|---|---|
| R68-1 | "Every round-68 receipt … names no revision it measured … Re-capture each with the measured sha printed inside the receipt." | D1: each of nine `recapture/*.txt` committed, `measured-rev: <40-hex>` an ancestor of `--rev`, an `exit=` line, expected verdict line; C1-base must name `e94ae32a` | **CLOSES**, two mechanical holes (F6) |
| R68-2 | "`C2-routed-selftest.txt` records a failed invocation … the receipt was never re-captured. Re-capture it, revision-pinned." | D2: re-capture committed, `measured-rev`, `exit=0`, `0 failure(s) over 6 assertions`, no `unrecognized arguments` | **CLOSES** |
| R68-3 | "Either classify a missing records file as a content verdict or restate the contract, and ship the base-control receipt." (+ the lane `git checkout` write found at round start) | D3: no quoted `checkout` token in the r67 counter source; base receipt shows `0 of 4` at `e94ae32`; sandbox base run exits 1 with `0 of 4`; tip run exits 0 with `4 of 4` | **BLOCKING** — false positive on the sanctioned sandbox checkout (F1) |
| R68-4 | "S200's located quote drops `<code>` … S202's drops `**` bold; neither row nor the lesson's Gate names the removed bytes. The Q42 note is owed." | D4: `round-69.md` § Gate carries a line with S200 and `<code>`, and a line with S202 and `**` | **CLOSES** (presence floor, disclosed); narrower than "row or Gate" (F8) |
| R68-5 | "… supported outside the cited line. Quote the approval sentence in the row (it exists, ≤25 words) or bound the cell; the entry's `## Limits` names S199/S200 shaping but not this." | D5: a `mined` 2026-10-25 row whose `teaches` opens `supersedes S201 —` and whose anchor carries the approval sentence; the r68 entry mentions the row id **anywhere** | **WEAKER** — a bare mention passes while the entry's citations still point at S201 (F3) |
| R68-6 | "Mine this as a mistake row — a refusal whose reason is wrong teaches the gate the wrong lesson — and add the grounded criterion to `corpus/QUALITY.md`." | D6: § Mistakes has **a single line** containing `R68-6` and `S201`; QUALITY has a `\| Q… \|` row citing `round-69.md` | **WEAKER + BROKEN** — passes a row that restates the false reason, and fails the draft's correctly wrapped row (F2) |
| R68-7 | "24 lane-authored paths … uncommitted at the tip (10 modified …, `4081` insertions / `251` deletions, 14 untracked) … Commit or disposition each path." | D7: each of the 24 tracked at `--rev` (modified ones with a blob ≠ the base blob), or named on a literal `disposition: removed <path>` line and untracked | **WEAKER** — any one-line change passes for a 251-line drift; elided disposition paths are not recognised (F4, F5) |
| R68-8 | "… until round 69 adds the coverage-map row and re-records the baseline from the gate's own measurement." | D8: README row for the spot-check; four baseline `expect` values == the sandbox gate's `--no-baseline --json` observation | **CLOSES** (four-field arm; full-gate green rides predicate conjunct 2). Currently red: not re-recorded (F7) |

## Findings

### F1 — BLOCKING · D3 rejects the sanctioned sandbox checkout (false positive)

**Counterexample.** `D3` scans the committed r67 counter for the quoted token `checkout`
(`re.search(r"[\"']checkout[\"']", src)`). The repaired counter's only checkout is inside its own
`/tmp` clone:

```
verifiers/check_r67_routed_repairs.py:101
        proc = subprocess.run(["git", "-C", str(clone), "checkout", "-q", rev],
```

The regex matches (`True`), so D3 prints *"still runs `git checkout` (a git write in the lane)"* —
a false statement — and `8 of 8` is unreachable. All other D3 arms pass (verified):

```
repaired r67 at e94ae32 → r67 routed defects closed 0 of 4   exit=1   (content verdict, not env error)
repaired r67 at 2cf0d99 → r67 routed defects closed 4 of 4   exit=0
```

**Second direction.** The proxy is also blind: a lane write via `git restore`, `read-tree`,
`reset --hard`, `apply`, `add` or a `shutil` write passes D3 untouched.

**Impacted axes.** consistency (claim truth), operability (the counter cannot be satisfied).

**Smallest safe correction.** Stop scanning for a token; reject a git *write* subcommand only when
its operand is the measured lane repo. Minimal form: forbid `checkout|restore|read-tree|reset|apply|add|commit`
co-occurring with `str(repo)`/`args.repo`/`self.path` in the same `subprocess.run([...])`, and
permit `str(clone)`/`tempfile` targets. Equivalent behavioural form: hash the lane's index and
`git status --porcelain` before/after the two sandbox runs and require both unchanged.

### F2 — BLOCKING (state) · D6 is line-granular and its content arm is a presence floor

**Counterexample A (false negative).** The draft lesson has the row; it wraps, so no single line
carries both tokens:

```
corpus/lessons/round-69.md § Mistakes
- **M111 — class: a refusal whose reason is false (R68-6).** Evidence: `corpus/lessons/round-68.md`
  § Gate refused the staged S201 quote "All three skill tools require approval by default" …
```

`"R68-6" in line and "S201" in line` is false for every line → D6 fails, and the simulated tip
prints `4 of 8` partly because of it. Markdown wrapping is normal prose; the defect is the check's
line model, not the row.

**Counterexample B (false positive), proved with the counter's own harness.** Replacing the row
with one that **restates the false reason** still closes D6 (score unchanged; the only finding is
the unrelated D7 clone):

```
"## Mistakes\n- M111 R68-6 S201: the page did not carry the staged words at all.\n"
→ closed 8 of 8
```

So D6 cannot distinguish the correct lesson ("the words are verbatim, twice; the anchor was wrong")
from the defect it is supposed to teach against.

**Impacted axes.** consistency, calibration (a presence floor over the lane's own records is
disclosed, but a floor that also *fails* the correct record is a defect).

**Smallest safe correction.** Join wrapped bullets before matching (`re.split(r"\n(?=- )", mistakes)`),
then require one bullet to name `R68-6` and `S201` **and** carry the observed fact token
(`verbatim`); and require the QUALITY evidence cell to name the true defect (anchor/mangled copy),
not merely cite `round-69.md`.

### F3 — HIGH · D5 passes on a bare mention; the G9 condition still obtains

**Counterexample, in the draft itself.** D5 requires only `re.search(rf"\b{cells[0]}\b", entry)`.
The entry has **no `source: S208` line** (five `source:` lines, S198–S202), its per-client table
still ends the Microsoft row `| S201 |`, and its shape #3 is labelled
`**Approval and review (S201).**` while asserting "the three skill tools require approval by
default". The chapter's only S208 occurrence is the amendment prose, whose claim is false:

```
corpus/knowledge/client-trust-gates-round68.md:82
this entry's approval claim (section "Approval and review", S201) therefore cites S208.
```

It does not cite S208 anywhere a reader or a guard would resolve a citation — the citation is still
S201, whose located quote is the `Security best practices` sentence. The G9 condition the closure
named ("supported outside the cited line") therefore persists at the bytes D5 certifies as closed;
`## Limits` also still names only S199/S200 shaping (the closure's explicit second ask).
Harness proof that the check is satisfied by mention alone:

```
entry := "Nothing changed; see S208 in passing.\n"  → closed 8 of 8
```

**Impacted axes.** consistency (the claim), depth (the entry's citation hygiene), calibration
(an amendment that misdescribes its own entry is the Q60/M95 self-description class).

**Smallest safe correction.** Require all three: (a) a `source: S208` line in the r68 entry;
(b) the shape/table citation that carries the approval clause to be S208 (label or source cell);
(c) a `## Limits` bullet naming the S201/S208 anchor shaping. Or bound the cell as the routed
defect's alternative ("or bound the cell") and say so in the amendment.

### F4 — HIGH · D7 accepts a magnitude-free stand-in for the quantified drift

**Counterexample.** D7's modified-path arm is only `blob(path, rev) != blob(path, R69_BASE)`.
Replacing `logs/MutR67Repairs.log` — 251 drifted lines — with the base blob plus one appended line
and committing it in a throwaway clone yields:

```
numstat vs a5f7459:  1  1  .ufo/waves/round-68/w1/logs/MutR67Repairs.log
D7 findings for that path: NONE (accepts the one-line version)
```

The routed defect's substance is that the *measured* drift landed; the closure quantified it
(`4081` / `251`). Verified at the lane's working tree today: the same 10 files still carry exactly
`4081` insertions / `251` deletions and the status is exactly 24 paths — so the anchor is available.

**Impacted axes.** consistency (landed-means-committed, Q03), calibration.

**Smallest safe correction.** Hold the closure's aggregate: sum `git diff --numstat R69_BASE..rev`
over the ten `MODIFIED` paths and require `insertions ≥ 4081` and `deletions ≥ 251` (growth from
later seat appends passes; a trimmed commit fails). Per-path minima are better if the L1 records
the round-start numstats — they are not recorded now.

### F5 — MEDIUM (state) · D7 does not recognise the elided disposition path

The lesson's M112 fix line writes the clone as an elision inside backticks:

```
disposition: removed .../c2falsify-clone/
```

`re.findall(r"disposition: removed \`?([^\`\s]+)\`?")` captures `['.../c2falsify-clone/']`, which
is not `.ufo/waves/round-68/w1/controls/c2falsify-clone/`; D7 therefore reports the clone as
"neither committed nor dispositioned" (observed in the simulated tip). Not a check weakness on its
own (a literal path is the right contract), but the draft and the counter do not agree today.

**Smallest safe correction.** Write the full path on the disposition line (one edit to the lesson).
If abbreviations are wanted, teach D7 a `.../`-prefixed glob anchored at `.ufo/waves/round-68/w1/`.

### F6 — MEDIUM · D1's verdict arms are weaker than the receipts it certifies

Two holes, both proved with the counter's own `FakeRepo`:

```
C1-fetch.txt := "measured-rev: e94ae32a…\nlive quotes found 0 of 5\nexit=0\n"     → closed 8 of 8
C1-base.txt  := "measured-rev: e94ae32a…\nclient trust gates backed 0 of 5\nexit=0\n" → closed 8 of 8
```

- `C1-fetch.txt`'s pattern is `live quotes found \d of 5`, so `0 of 5` (the opposite verdict) passes.
- No receipt's `exit=` value is compared with its verdict, so `backed 0 of 5` + `exit=0` passes.

The receipts themselves are faithful where I re-ran them (see below), so this is a check defect, not
a lane falsehood.

**Smallest safe correction.** Pin the exit per receipt (`C1-base` 1, the other eight 0) and spell
`live quotes found 5 of 5`.

### F7 — STATE (expected mid-flight) · D8 red, and predicate conjunct 2 is red too

At the simulated tip (working tree as of this seat's snapshot):

```
baseline expects 124 / 0 / 85 / 38 ; the gate measures 127 / 1 / 87 / 39
unindexed_detail: ['corpus/lessons/round-69.md']
verify_corpus_integrity.py → 5/9 checks pass; exit 1
```

So both the D8 arm and the predicate's second conjunct fail. The L1 owes: a coverage-map row for
`lessons/round-69.md` (unindexed=1) and a baseline re-record from `--no-baseline --json` at the tip.
D8's own design is adequate for R68-8 — the four fields it compares are the four the routed defect
names, and full-gate green is carried by the separate conjunct, so this is not scored as a check
weakness.

### F8 — LOW · D4 is narrower than the routed defect

R68-4 allows the note in "row **or** the lesson's Gate"; D4 accepts only a § Gate line. A repair
that satisfied R68-4 by annotating the SOURCES row would be rejected. Over-strict, not weaker;
noted for symmetry with F3 (where the counter is too loose).

### Note (low, consistency) · the D3 repair adds behaviour with no self-test arm

The repaired r67 counter still defines five broken worlds (six assertions, matching the
re-captured `C2-routed-selftest.txt`), and none models the new "missing records file is a content
verdict" classification. R68-3's ask is met by the behavioural receipt
(`recapture/r67-repairs-base.txt`, verified), but the claim that the shared counter's self-test
carries one world per routed defect no longer holds for the new behaviour.

## What the counter gets right (re-run, not accepted)

Every one of these was executed by this seat at the cited revision in a `/tmp` shared clone:

| Receipt | Re-run | Matches |
|---|---|---|
| `C1-base.txt` | `check_client_trust_gates.py --rev e94ae32` → `backed 0 of 5`, exit 1 | yes |
| `C1-after.txt` | `--rev 2cf0d99` → `backed 5 of 5`, exit 0 | yes |
| `C2-integrity-after.txt` | `verify_corpus_integrity.py --json` at `2cf0d99` → 124/0/85/38, exit 0 | yes |
| `gate-registry.txt` | `check_gate_registry.py --rev 2cf0d99` → `46 of 46 … phantom 0` | yes |
| `C2-routed-measure.txt` | r67 counter **as committed at** `2cf0d99` → `4 of 4`, exit 0 | yes |
| `C2-routed-selftest.txt` | same script `--self-test` → `over 6 assertions` | yes |
| `r67-repairs-base.txt` | repaired r67 counter at `e94ae32` → `0 of 4`, exit 1, content verdict | yes |

Controls reproduce: base `0 of 8` exit 1 (`--rev a5f7459` with the plan's counter); the cheap control's
shape (commit paths + one index row only → `0 of 8`) is consistent with D1/D2/D4/D5/D6/D8 all being
unmet, and its D7 arm would close once the clone is dispositioned — consistent with the reported
`0 of 8`.

## Impacted axes

- **consistency (judged axis): harmed.** The claim is the consistency claim, and four of eight
  closures are weaker than the defect. `closed 8 of 8` at the draft tip is not merely unreachable
  (D3, D6, D7, D8 fail) — it would also be *unearned* if reached by the present checks (D5, D6, D7
  holes are all provable).
- **depth / coverage: not touched** by these findings; C1/C3 belong to their own seats.
- **calibration: unchanged, on condition** that the report records D1/D3/D5/D6/D7 as check defects
  rather than as lane misses; the entry's false amendment sentence (F3) is a lane-side
  self-description defect and belongs in § Mistakes if the round keeps M111 as its class.

## Peer input recorded, not absorbed

`ScoutJunie` (F3 in `.ufo/waves/round-69/w1/ScoutJunie.md`): the campaign register's S172 row is
labelled `payload-absent` on a truncated, tag-elided span while the payload is verbatim on the
page — a Q62-class false refusal reason. Confirmed relevant here: Q62's scope cell covers
"source refusals in lessons and SOURCES rows", not campaign register rows, and D6 is a presence
floor, so no instrument rejects it. It is an absorption/lesson-wording item, not a C2 predicate
failure.

## Bounds of this report

- The simulated-tip numbers (127/1/87/39, `4 of 8`, `5/9`) are a point-in-time snapshot of a
  working tree that other seats are still writing to; the tip will differ.
- No network was used: the `--fetch` arm of `C1-fetch.txt` and the SOURCES quote re-openings were
  not re-executed (they belong to C1's seats); only the receipt's textual claim was checked.
- No tool was installed. Nothing under `/home/vgpnk/Projects/shokunin` was written except this
  report path; all clones, commits and counter runs lived under `/tmp`.
