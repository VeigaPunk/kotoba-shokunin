# ScoutRepairsApi — G-a..G-f against the frozen routed-repairs checker

Seat: `KotobaR62.ScoutRepairsApi`. Date: 2026-10-23. Lane read-only. Successor file `verifiers/check_routed_repairs_v2.py` was absent (`test -f` exit 1 at 2026-10-23T20:52:05Z). This report does not propose editing `verifiers/check_routed_repairs.py`. The six frozen checks stay the r61 instrument; every hardened form below is a new file.

## Identity

| item | observed |
|---|---|
| checker | `verifiers/check_routed_repairs.py`, symbol `check_repairs` |
| worktree sha256 | `95ade9be1ed1930266bce4b98c8c593fff1feba89e2cf25763f0aa83f206cb88` |
| git blob | `56b86f61004ff2e9d319d8cc87459b5cd702b51f` at HEAD `a1cb8abc3911a5df3a2877915509118e384651a4` and at dispatch tip `45a7ecfac9e203297f3146c45d63f5e79367470c` (same blob; `git diff --stat HEAD --` that path empty) |
| r61 audit sha | ExecC2Audit measured `9ee77d47…` and an unguarded `[-1]` at its then-line 89. Current line 99 is `census_lines[-1] … if census_lines else False`. B18's `IndexError` is not this file. Not re-diffed against `9ee77d47`. |

r62 letters are the wave-spec slice (`/.ufo/waves/round-62/w1-spec.json` ExecSuccessorC2), not ExecC2Audit's G-a..G-i. Audit G-f is exact ids only; audit G-g is owned exit; audit G-h is the `exit=0` spelling. r62 G-f bundles ids + owned exit + two distinct 40-hex operands. Audit G-h is not a r62 letter; H1 still requires the spelling.

## Frozen commands (this seat, lane cwd)

`date -u`: Fri 23 Oct 2026 08:49:55 PM UTC.

```
$ python3 -B verifiers/check_routed_repairs.py --self-test
self-test all-repairs: 6 of 6 (want 6) ok
self-test base-world: 0 of 6 (want 0) ok
self-test no-log: 3 of 6 (want 3) ok
self-test no-quality: 5 of 6 (want 5) ok
self-test without-round-61.md: 5 of 6 (want 5) ok
self-test without-census-after.txt: 5 of 6 (want 5) ok
self-test without-controls-ancestry.txt: 5 of 6 (want 5) ok
self-test ra-without-command: 5 of 6 (want 5) ok
self-test rb-missing: 5 of 6 (want 5) ok
self-test ra-without-count: 5 of 6 (want 5) ok
self-test rc-without-c1-pointer: 5 of 6 (want 5) ok
self-test ancestry-without-merge-base: 5 of 6 (want 5) ok
self-test: 0 failure(s)
EXIT=0
```

```
$ python3 -B verifiers/check_routed_repairs.py --rev f3246d1493b60ea1c0d947a19c39f9e08e92f326
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after file: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
EXIT=1
```

Same clock, `--rev a1cb8abc3911a5df3a2877915509118e384651a4` (HEAD): all six `ok`, `routed repairs verified 6 of 6`, EXIT=0. That tip is a frozen-passing tree. It is not the house-style H1 (see F2/F3).

## What each frozen check actually tests

| repair | lines | predicate in `check_repairs` |
|---|---|---|
| R-a | 77–82 | file-wide `in`: `build reports`, `claimed 32`, `committed 29`, `.ufo/waves/round-60/build`. No command, no line bound, no polarity, no derived count. |
| R-b | 85 | both filenames anywhere in `LOG.md` |
| R-c | 88–91 | some single line contains both `receipts/freeze2-selftest.txt` and `C1-measure.txt` |
| R-d | 94–99 | blob present and last non-empty line is exactly `exit=0` (empty/whitespace → False, no throw) |
| R-e | 102–108 | `Q56` and `byte-exact` anywhere in QUALITY; lesson blob contains `M91` |
| R-f | 111–116 | ancestry blob contains `merge-base --is-ancestor` and `exit 0` (space). `exit=0` does not match. |

Docstring lines 20–22 say R-a is "on one line". The code is not. Self-test arm `ra-without-command` (`:206–211`) scores 5 only because that fixture drops `.ufo/waves/round-60/build`. A log with the four substrings and no command scores **6 of 6** (measured). The frozen self-test does not already implement G-a or G-b.

## Roster the successor must derive (G-a)

Pattern `^(Conn|Critic|Exec|Mut|Review|Scout|Scribe|Sentinel|Src)[A-Za-z0-9]+\.md$` on **basenames** of `git ls-tree -r --name-only <rev> -- .ufo/waves/round-60/build`.

`date -u` bracket: roster Fri 23 Oct 2026 08:51:19 PM UTC; HEAD recount in the following cell, before 20:52:05Z.

| rev | entries | `*.md` | basename pattern | full-path `^` pattern | md that miss the pattern |
|---|---:|---:|---:|---:|---|
| `f3246d1493b6` | 33 | 30 | **29** | **0** | `check_word_counts.fixture.md` |
| `a1cb8abc3911` | 33 | 30 | **29** | **0** | same one file |

Anchoring `^` on the ls-tree path matches nothing. End-anchored search on the full path matches 29, same as the basename. The plan's "tree-derived 30" is the all-markdown count, not the pattern count. ExecDishonestTrees' "30 pattern-matching names" is a **synthetic list**. Using the live tree as D1 does not fail G-a: pattern count is already 29, so a LOG that says `committed 29` is equal.

Audit G-a (swarm-registry.json members minus missing md → 29) was not re-run here. The r62 command is the ls-tree pattern, not that JSON.

`claimed` must exceed the derived count (plan §C2). D1 with derived 30 and a line that still says `claimed 32` / `committed 29` fails **equality**, not the exceed conjunct (32 > 30).

## In-process frozen scores

Imported `check_repairs` from the lane file. No git object written. Honest skeleton (self-test shape: one-line R-c, ancestry `exit 0`, census body + `exit=0`, exact `Q56`/`M91`) scores 6 of 6. Cell output sits between the 20:51:19Z roster stamp and the 20:52:05Z HEAD stamp. Successor column is **expected, not run**.

| guard | frozen check | minimal mutant | frozen (measured) | successor (expected) | F2/F3 fixed? |
|---|---|---|---|---|---|
| G-a self-derived count | R-a `:77–82` | **D1.** LOG still says `committed 29` (and `claimed 32`). `build_paths` is 30 basenames matching the pattern. Frozen never sees `build_paths`. Live tree is not this mutant. | **6 of 6** (R-a ok) | **5 of 6** (R-a equality fails). Exceed conjunct stays true. | no |
| G-b assertion direction | R-a `:77–82` (same `in`) | **D2 distinguisher is not the plan's literal `"did not claim 32"`.** That string does **not** contain `claimed 32` → frozen **5 of 6**, R-a already missing. The mutant that frozen still accepts is audit B2: keep the substring, e.g. `were NOT claimed 32` or `did not honestly record that we claimed 32`. | **6 of 6** (substring kept); **5 of 6** (plan's literal phrase) | **5 of 6** on the substring-keeping negation | no |
| G-c bounded landed-scope window | R-b `:85` | **No D1..D6 recipe.** Measured stand-in (audit B4): both names present, cue replaced by `deliberately EXCLUDED from scope`. | **6 of 6** (R-b ok) | **5 of 6** only if G-c is really implemented. The C2 six-tree predicate does not force it. | no |
| G-d R-c direction, adjacent lines ok | R-c `:88–91` | **D3.** One line: base is `C1-measure.txt`, not `receipts/freeze2-selftest.txt`. Both substrings co-occur, so direction is invisible to frozen. | **6 of 6** (R-c ok) | **5 of 6** (direction fails) | **F3 yes.** F2 no. |
| G-e census body | R-d `:94–99` | **D4.** Census blob is exactly `exit=0` (with or without trailing newline). | **6 of 6** (R-d ok) | **5 of 6** (no body) | no. Census already accepts `exit=0`. F2 is R-f. |
| G-f exact ids + owned exit + two distinct 40-hex | R-e `:102–108` **and** R-f `:111–116` | **D5** and **D6 are different repairs.** D5: `Q560` and `M910` (still contain `Q56`/`M91`), `byte-exact` kept. D6: `exit 0` belongs to `git rev-parse`, merge-base left as TODO, no two distinct 40-hex operands. | each **6 of 6** | each **5 of 6** (D5 drops R-e only; D6 drops R-f only) | **F2 only if** an owned exit may be spelled `exit=0`. F3 no. |

One mutant does not cover G-f's three conjuncts. D5 leaves R-f honest. D6 leaves R-e honest.

### F2 / F3 / H1 (measured on the same skeleton)

| variant | change vs honest skeleton | frozen |
|---|---|---|
| F2 | ancestry result line `exit=0` instead of `exit 0`; R-c still one line | **5 of 6**, R-f missing. ExecC2Audit.md:256–265. |
| F3 | correct direction split across two adjacent lines (`…freeze2-selftest.txt` / `and not C1-measure.txt`); ancestry still `exit 0` | **5 of 6**, R-c missing. ExecC2Audit.md:267–274. |
| H1 | F2 and F3 together (plan's house style) | **4 of 6**, R-c and R-f missing. Matches plan §C2 "frozen counter scores 4 of 6". |

Expected successor: H1 **6 of 6**. That is the only named tree that forces both relaxations. HEAD does not.

## Landed tip is H2-shaped for the frozen checker, and it constrains the successor

HEAD `a1cb8abc` blobs (git show), the lines that made 6 of 6:

- R-a `LOG.md:2540` — one line with `build reports`, `claimed 32`, `` `committed 29` ``, path `.ufo/waves/round-60/build`, and the basename grep. Positive assertion. Pattern count 29 at both revs above, so G-a passes this line if it counts basenames at the measured rev.
- R-b `LOG.md:2541` — one line beginning `R-b landed scope` containing both required names. G-c's cue is present. B4 is not this line.
- R-c `LOG.md:2542` — **one line**, correct direction, but not the audit's example phrase. The bytes are `committed at `.ufo/waves/round-60/receipts/freeze2-selftest.txt`, NOT in `.ufo/waves/round-60/C1-measure.txt``. Measured: `not C1-measure.txt` is **absent**, `NOT C1-measure.txt` is **absent**, `rather than C1-measure.txt` is **absent**, `NOT in` is present. A direction test copied from ExecC2Audit.md:402–404 false-negatives this tip. Material is allowed between the negation and `C1-measure.txt`, and the freeze2 path carries a `.ufo/waves/round-60/` prefix. F3's two-line form is **not** this tip.
- R-d census-after — 17 non-empty lines: 15 `W04` duplicate-url rows, `kotoba ok`, tail `exit=0`. No `git `, `date`, `UTC`, `2026`, `rev`, `census`, or `validate`. Audit G-e's provenance line (command + revision + UTC) would reject this honest file. r62's smallest G-e (a body before the tail) accepts it. The body does not contain the token `DRIFT`.
- R-e — QUALITY row starts `| Q56 |` and contains `byte-exact` and `literal`. Lesson `M91` is the token `**M91 —`, not `M910`.
- R-f ancestry — two distinct 40-hex hashes `b4a8d2ee79a6190cf5ece5d11395544876e1fc8a` and `43fe01804708d65e53965b4be31e9dc7dce793e4`. Three different `exit 0` occurrences: `exit 0 (hashes differ)` under `test … != …`, a bare `exit 0` on the line after `git merge-base --is-ancestor <those two>`, and a bare `exit 0` under `git cat-file -e`. G-f must treat "there exists an owned merge-base exit whose operands are those two distinct hashes" as pass. "Every `exit 0` belongs to merge-base" rejects this tip.

Whitespace-only census on an otherwise-passing blob map: frozen **5 of 6**, R-d missing, no exception (current `:99`).

## Letter crosswalk (do not implement the audit's extra letters as the r62 six)

| r62 guard | audit section it shrinks | what the smallest form is | what would fail H1 or the tip |
|---|---|---|---|
| G-a | audit G-a, but ls-tree basename pattern, not registry JSON | `committed <n>` equals pattern count; claimed count exceeds that count | full-path `^` (count 0); counting all md (30) against a true `committed 29` |
| G-b | audit G-b's polarity half only | the correction asserts; negation that still contains `claimed 32` fails | treating plan-literal `did not claim 32` as the frozen-pass D2 (frozen already scores it 5) |
| G-c | audit G-c | both names inside a landed-scope window | none of D1..D6 drop R-b, so omitting G-c still satisfies the printed predicate |
| G-d | audit G-d plus its F3 sentence | direction, and the two pointers may sit on adjacent lines | contiguous `not C1-measure.txt`; requiring one physical line (fails H1/F3, not the tip) |
| G-e | audit G-e body bullet only | more than the tail token | requiring a command/revision/UTC line (tip census has none) |
| G-f | audit G-f + G-g; spelling from audit G-h via H1 | token-boundary `Q56`/`M91`; an exit owned by `merge-base --is-ancestor`; two distinct 40-hex operands; H1's `exit=0` must count | `Q56`/`M91` as bare `in`; requiring the only `exit 0` in the file to be the merge-base's (tip has three) |

## Confidence and gaps

- Frozen line ranges, command exits, in-process D/F/H scores, basename counts, and the HEAD repair lines: **high** (read or run this seat).
- Successor scores: **expected from the plan's `< 6` / H1 `6 of 6` rule, not executed**. `check_routed_repairs_v2.py` was not on disk.
- Window width for G-c and G-d is not a number in the plan or the wave spec. Adjacent (F3's two lines, and the tip's one line) is the measured requirement; a wider window is unspecified.
- Audit's registry-json derivation of 29 was not re-run.
- The LOG's phrase "r60 close commit" was not resolved to a third hash. Pattern count is 29 at `f3246d14` and at HEAD.

**Installs:** none. No pacman. No package was missing.

**Blockers:** none.

**Attacked:** frozen `check_repairs` (R-a..R-f) against r62 G-a..G-f, D1..D6, and F2/F3; successor not edited and not run.
