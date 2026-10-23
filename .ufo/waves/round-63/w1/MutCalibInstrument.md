# MutCalibInstrument

role: mutation tester (UFO-FSD) — one probe: does the C2 counter design's counted predicate
discriminate the five defects named in the plan's own wording?
item: mutation-test the C2 counter design: minimal implementation of the five checks in /tmp,
five mutants (M1 worktree read, M2 literal `3f911504`, M3 hardcoded sizes, M4 line-count-only,
M5 grep `36 of 38`); for each, does the do-nothing rev `35d44b4b` still fail it and does a
label-only tree pass; report which mutants the plan wording admits and the exact assertion
that kills each.

Lane read-only: the only lane write is this file. All fixture refs and the harness live in
`/tmp/mutcalib` (`clone` refs `lbl/tok/sz/rw/nh/lbl0`; lane `for-each-ref refs/heads/` shows
only `hyaku/*` + `master`). Net: `git rev-parse HEAD` = `8c4cefa8…` before and after.

## Findings

1. **The plan's pre-erratum control arithmetic is unattainable; E1 (`plans/round-63.md:150-159`)
   is necessary and is confirmed.** A faithful implementation of the pre-E1 check 4
   (`git show e53b6e5c:LOG.md` byte-prefix of `git show <rev>:LOG.md`) passes at `35d44b4b`
   because the two LOGs are byte-identical (`sha256 611aee11…` both), so the counter prints
   **1 of 5**, not the `0 of 5` declared at `plans/round-63.md:112`. With E1's second conjunct
   (the rev's LOG grows by ≥1 line) the same run prints **0 of 5**. Output:
   ```
   $ python3 check_r63_routed_repairs.py --rev 35d44b4b --pre-e1
   ... append-only: ok  [byte-prefix of 514498 B (pre-E1)] ... closed 1 of 5   exit=1
   $ python3 check_r63_routed_repairs.py --rev 35d44b4b
   ... append-only: missing  [prefix=True grew_by=0 line(s)] ... closed 0 of 5  exit=1
   ```
   The paragraph at `:110-117` still states both "0 of 5" and "4 passes"; only E1 reconciles
   them. The landed draft and `controls/C2-before-r62tip.txt` already implement E1.

2. **No mutant is killed by the do-nothing rev.** Post-E1 the honest counter and all five
   mutants print `closed 0 of 5`, exit 1 at `35d44b4b` (each fails checks 1,2,3,4,5 for
   reasons unrelated to its mutation). The control therefore tests *reachability of 0*, not
   the *method* of any check. Matrix (`--pre-e1` in parentheses where it differs; every cell
   is the printed `closed N of 5`):
   ```
   fixture | honest |  M1 |  M2 |  M3 |  M4 |  M5
   F0      |   0(1) | 0(1)| 0(1)| 0(1)| 0(1)| 0(1)
   LBL     |      5 |   5 |   5 |   5 |   5 |   5
   TOK     |      4 |   4 |   5 |   4 |   4 |   4
   SZ      |      4 |   4 |   4 |   5 |   4 |   4
   RW      |      4 |   4 |   4 |   4 |   5 |   4
   NH      |      4 |   4 |   4 |   4 |   4 |   5
   ```
   Full transcripts: `/tmp/mutcalib/matrix_e1.txt` (minimal counter, sha256 `873a8de7…`) and
   `/tmp/mutcalib/draft_matrix.txt` (landed draft, sha256 `1963f6cb…`).

3. **M1 survives; in the lane it *passes* the defect being counted.** `--rev 35d44b4b` run
   from the lane worktree, where `.ufo/waves/round-62/w2/FalsifyC2HonestH1.md` exists untracked
   (`sha256 6ccdc25b…`, 10,224 B): honest draft `FAIL late-write-tracked — not a tracked blob
   at 35d44b4b` (0 of 5); mutant `PASS late-write-tracked — worktree has …` (1 of 5). Both
   exit 1, so the headline control does not distinguish them. The landed draft's self-test also
   does not: `self-test: 0 failure(s) over 10 assertions`. Kill assertion:
   per-check, not headline — `check_late_write(LANE, "35d44b4b…") is False` while the path is
   present on disk; equivalently the evidence path must never be opened via `os.path.exists`.

4. **M2 survives.** The draft's receipt-absent "shortcut" arm (self-test deletes the receipt)
   does not kill it, because the item's mutant keeps the `receipt is None` guard and only
   substitutes the token source. Measured: draft self-test `0 failure(s)`; fixture TOK
   (receipt `receipt_rev=cafebabe…`, LOG names `3f911504…`) — honest 4 of 5
   (`LOG never names cafebabe…`), M2 5 of 5. Kill assertion: the *substitution* tree must fail
   `receipt-rev-named`; asserting only the absent-receipt tree is insufficient.

5. **M3 is killed by the landed draft's self-test, but not by any real-rev control.** Draft
   self-test with M3: `2 failure(s)` (the synthetic entry is 2 lines / 4 words, so a 64/1044
   hardcode fails the repaired arm). At the real revs the literal coincides (erratum is
   64/1044 at `35d44b4b` and at `8c4cefa`), so the only direct control is the size-shift
   fixture SZ (erratum +1 line = 65/1052, LOG still 64/1044): honest 4 of 5
   (`LOG never states 65 lines / 1052 words`), M3 5 of 5.

6. **M4 is killed by the landed draft's self-test, and by fixture RW at rev level.** RW
   rewrites one already-committed r62 LOG bullet in place at equal line count (2567 = 2567):
   honest `FAIL append-only — prefix=False grew_by=1`, M4 `PASS append-only — grew_by=1` (5 of 5).
   Draft self-test with M4: `1 failure` on `rewrite: a rewritten LOG fails the prefix conjunct`.
   The kill is the prefix conjunct, not the growth conjunct.

7. **M5 survives, and it is the one mutant the plan's prose admits.** `plans/round-63.md:109`
   names the value as a literal ("including the measured `36 of 38`"), so a reader can
   implement `"36 of 38" in line` and be faithful to the sentence. Draft self-test with M5:
   `0 failure(s)`; fixture NH (receipt says `37 of 38`, LOG says `36 of 38`): honest 4 of 5
   (`LOG does not name reg_gate 37 of 38 + corpus-idx`), M5 5 of 5 (`LOG names reg_gate 37 of
   38 + corpus-idx` — the grep matched the LOG's stale 36). Kill assertion: read the count
   token from `noharm-tip.txt` at `<rev>` and require *that* token on the LOG line.

8. **A label-only tree passes — both counters, 5 of 5.** LBL commits a 68-byte placeholder at
   the late-write path plus one appended LOG line carrying every literal token
   (`receipt_rev=3f911504…`, `corpus/knowledge/erratum-absorption-round62.md` + `64 lines` +
   `1044 words`, `reg_gate`/`corpus-idx` + `36 of 38`). Nothing was read from the receipts at
   build time. Honest minimal counter 5 of 5; landed draft 5 of 5. A **zero-byte** blob at the
   late-write path (fixture `lbl0`) also prints 5 of 5 on both. So the counted predicate
   verifies token identity, not that the untracked 158-line/10,224-byte H1 finding (14 `R-c`
   and 7 `ancestry` hits) was folded into the bound: `: > .ufo/waves/round-62/w2/
   FalsifyC2HonestH1.md` satisfies check 1. Kill assertion: check 1 must require blob substance
   (e.g. `len(blob) >= 1024 and b"R-c" in blob and b"ancestry" in blob`), or check 2 must
   require the appended line to name the H1-narrowness bound.

9. **Spot-check defect 2's third citation is counted by no check.** §6.2 routes three errors:
   `receipt_rev`, entry size, and "the compliance line that claims a post-report child commit"
   (`corpus/lessons/round-62-verifier-spotcheck.md:166-168`). Checks 2 and 3 cover the first
   two; check 4 is a method guard, not a defect. `grep -n child verifiers/check_r63_routed_repairs.py`
   → `259:  "- No post-report child commit exists.\n"` — the sentence exists only in the
   self-test fixture text and is consumed by no assertion. LBL omits it entirely and still
   scores 5 of 5, so the counter can print "r62 routed defects closed 5 of 5" with the
   child-commit claim uncorrected. Kill assertion: remove that sentence from the repaired
   fixture and require the counter to lose a check; or require the correction line to state
   "no post-report child commit" (draft:259 already has the wording).

10. **Integration constraints for the L1's correction line.** The landed draft is stricter
    than the plan prose in three places, so the real line must carry, per line:
    `receipt` + the full 40-hex token (check 2); the `corpus/knowledge/
    erratum-absorption-round62.md` path + both numbers (check 3); `reg_gate` + `corpus-idx` +
    the measured count (check 5). Current worktree `git diff --numstat e53b6e5c -- LOG.md`
    = `9 0 LOG.md` (append-only intact; check 4 will pass on growth). Any in-place rewrite of
    an already-committed LOG line anywhere between `e53b6e5c` and the measured rev — including
    a seat "fixing" an r62 bullet — drops the predicate to 4 of 5.

11. **Restoration and isolation.** No lane file was modified by this probe; the fixtures are
    commits in `/tmp/mutcalib/clone` only and no lane ref names them. The lane worktree's
    concurrent changes (`M LOG.md`, `M SKILL.md`, `M corpus/README.md`, `M corpus/SOURCES.md`,
    `M plans/round-63.md`, new untracked r63 files) are other seats' writes, present in the
    status before and after my runs. No tools installed (uv/npx/pacman: none used).

## Artifacts

Minimal faithful counter (the five checks; `/tmp/mutcalib/check_r63_routed_repairs.py`,
sha256 `873a8de7…`, 164 lines; `--mutant M1..M5`, `--pre-e1`):

```python
R62_TIP = "e53b6e5c0aaa1ef2b0861b9399fef44f8b907f02"
LATE = ".ufo/waves/round-62/w2/FalsifyC2HonestH1.md"
RECEIPT = ".ufo/waves/round-62/C2-successor-measure.txt"
NOHARM = ".ufo/waves/round-62/noharm-tip.txt"
ERRATUM = "corpus/knowledge/erratum-absorption-round62.md"
LOG = "LOG.md"
HARD_TOKEN = "3f911504ce76d9ca186f297d6d4a9cd8ed77508a"
HARD_LINES, HARD_WORDS = 64, 1044
PRE_E1 = False  # True reproduces the plan's pre-erratum check 4 (prefix only)

def appended_corrections(rev):
    rev_log, tip_log = blob(rev, LOG), blob(R62_TIP, LOG)
    if rev_log is None or tip_log is None: return []
    tip_lines, lines = tip_log.splitlines(), rev_log.splitlines()
    suffix = lines[len(tip_lines):] if lines[:len(tip_lines)] == tip_lines else lines
    return [ln for ln in suffix if re.search(r"correction", ln, re.I)]

def check1(rev, mutant):
    if mutant == "M1":  # defect: consults the worktree, not the tree at <rev>
        return os.path.exists(LATE), "worktree"
    _, out = git("ls-tree", "-r", rev, "--", LATE)
    return bool(out.strip()), "ls-tree"

def check2(rev, mutant):
    token = HARD_TOKEN
    if mutant != "M2":  # defect: literal instead of the receipt's own token
        rec = blob(rev, RECEIPT)
        if rec is None: return False, "receipt absent"
        m = re.search(r"^receipt_rev=(\S+)", rec, re.M)
        if not m: return False, "receipt_rev absent"
        token = m.group(1)
    return any(token in ln for ln in appended_corrections(rev)), token

def check3(rev, mutant):
    if mutant == "M3":  # defect: sizes never computed from <rev>
        lines, words = HARD_LINES, HARD_WORDS
    else:
        body = blob(rev, ERRATUM)
        if body is None: return False, "erratum absent"
        lines, words = len(body.splitlines()), len(body.split())
    for ln in appended_corrections(rev):
        if (re.search(rf"\b{lines}\b", ln) and re.search(rf"\b{words}\b", ln)
                and re.search(r"line", ln, re.I) and re.search(r"word", ln, re.I)):
            return True, f"{lines} lines / {words} words"
    return False, f"{lines} lines / {words} words"

def check4(rev, mutant):
    tip, cur = blob(R62_TIP, LOG), blob(rev, LOG)
    if tip is None or cur is None: return False, "log absent"
    if mutant == "M4":  # defect: line count only; an in-place rewrite survives
        return len(cur.splitlines()) > len(tip.splitlines()), (
            f"{len(cur.splitlines())} > {len(tip.splitlines())} lines")
    prefix = cur.startswith(tip)
    if PRE_E1: return prefix, f"byte-prefix of {len(tip.encode())} B (pre-E1)"
    grew = len(cur.splitlines()) > len(tip.splitlines())
    return prefix and grew, (f"prefix={prefix} grew_by="
                             f"{len(cur.splitlines()) - len(tip.splitlines())} line(s)")

def check5(rev, mutant):
    lines = appended_corrections(rev)
    if mutant == "M5":  # defect: literal grep, receipt never read
        return any("36 of 38" in ln for ln in lines), "grep 36 of 38"
    body = blob(rev, NOHARM)
    if body is None: return False, "noharm receipt absent"
    reg_status, _ = _arm(body, "reg_gate")
    idx_status, idx_tail = _arm(body, "corpus-idx")
    m = re.search(r"conformant (\d+ of \d+)", body)
    if reg_status is None or idx_status is None or not m:
        return False, "noharm arms unparseable"
    phrase = m.group(1)
    idx_path = re.search(r"unindexed:\s*(\S+)", idx_tail)
    need = ["reg_gate", "corpus-idx", reg_status, idx_status, phrase]
    if idx_path: need.append(idx_path.group(1))
    for ln in lines:
        if all(tok in ln for tok in need):
            return True, f"reg_gate={reg_status} {phrase}; corpus-idx={idx_status}"
    return False, f"need {need}"
```

Fixture recipe (all commits in `/tmp/mutcalib/clone`, parent `35d44b4b`; refs are not in the
lane):

```text
LBL  commit 68-byte placeholder at LATE + append one LOG line with the literal tokens
     (receipt_rev=3f911504ce76d9ca186f297d6d4a9cd8ed77508a; erratum path + 64 lines /
     1044 words; reg_gate FAIL (36 of 38 ...) and corpus-idx FAIL (corpus/lessons/
     round-61-verifier-spotcheck.md ...)).  rev 3459e0fc…
TOK  from LBL: receipt_rev= -> cafebabecafebabecafebabecafebabecafebabe         rev 975f72d3…
SZ   from LBL: append one line to the erratum (65 lines / 1052 words)            rev 1f54c642…
RW   from LBL: rewrite one committed r62 LOG bullet in place (attempt 2 -> 3),
     line count unchanged at 2567                                                rev c4f8cb5e…
NH   from LBL: noharm-tip.txt 36 of 38 -> 37 of 38, LOG still 36 of 38           rev 0bbd38f8…
LBL0 from LBL: LATE truncated to 0 bytes                                         rev bb6deb88…
```

Mutations applied to the landed draft (`verifiers/check_r63_routed_repairs.py`, worktree
sha256 `1963f6cb…`, 327 lines; copies under `/tmp/mutcalib/draft/`):

```text
M1 check_late_write: ls-tree body -> tracked = (root / LATE).exists()
M2 check_receipt_rev: drop RECEIPT_REV_RE.findall; token = "3f911504ce76…" (receipt guard kept)
M3 check_entry_size: lines = len(...); words = len(...) -> lines, words = 64, 1044
M4 check_append_only: return prefix and grew -> return grew
M5 check_noharm: `and count_token in line` -> `and "36 of 38" in line`
```

Draft self-test verdicts (`--self-test`): honest `0 failure(s) over 10 assertions`;
M1 `0`; M2 `0`; M3 `2`; M4 `1`; M5 `0`.

Kill assertions (each kills exactly one mutant; the honest counter must reject each fixture):

```python
assert not check_late_write(LANE, F0)            # M1: path exists untracked in the lane
assert not check_receipt_rev(TOK)                # M2: receipt token substituted
assert not check_entry_size(SZ)                  # M3: erratum size shifted at the rev
assert not check_append_only(RW)                 # M4: in-place rewrite, equal line count
assert not check_noharm(NH)                      # M5: receipt count substituted
assert not check_late_write(LBL0)                # check-1 substance: zero-byte blob
```

## Verdict

**ATTACKS.** The C2 predicate as frozen (target `5 of 5` plus the `35d44b4b` control) does not
discriminate any of the five mutants: all print the same headline as the honest counter on
both named revs, and a label-only tree — even with a zero-byte late-write blob — scores
`5 of 5`. The landed draft already kills M3 and M4 inside its self-test, but M1 (worktree),
M2 (literal token with the receipt guard kept) and M5 (literal count) survive it and reach
`5 of 5` on substitution fixtures. I would change this verdict if the landed self-test gained,
per check, a substitution arm — dirty worktree at a rev lacking the path, receipt-token swap,
erratum-size shift, equal-line-count rewrite, no-harm count swap — with the honest counter
required to reject each; plus a substance floor on check 1 and a check that consumes the
child-commit correction (draft:259), which no check currently reads.
