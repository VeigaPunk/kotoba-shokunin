# RevW2C2Interim

role: reviewer (UFO-FSD attack seat, wave 2 — falsify)
item: Attack the C2 counter's committed-byte honesty at `cbbee56e9a3589b0b46736ad36f1b77701def80e`.
Re-run both counting commands; audit `verifiers/check_r63_routed_repairs.py` for worktree reads
(MutCalibInstrument M1 class); verify check 4 implements erratum E1 (prefix AND grew_by>=1);
verify checks 2/3/5 scope matching to the appended suffix; report any worktree read with the
exact line.
Axes exercised: calibration (does the printed count reflect committed bytes at `<rev>`), depth
(does each check compute evidence rather than label).

Object under attack: `verifiers/check_r63_routed_repairs.py` at `cbbee56e` (373 lines).
Integrity of the audited copy: `git show cbbee56e…:verifiers/check_r63_routed_repairs.py | diff -
verifiers/check_r63_routed_repairs.py` → `IDENTICAL-to-worktree` (the bytes I audited are the
committed bytes; 373 lines both ways).

## Attack 1 — reproduce both counting commands (verbatim)

```
$ python3 -B verifiers/check_r63_routed_repairs.py --rev cbbee56e9a3589b0b46736ad36f1b77701def80e
PASS late-write-tracked   tracked at cbbee56e9a3589b0b46736ad36f1b77701def80e
PASS receipt-rev-named    LOG names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a on 1 line(s)
PASS entry-size-named     LOG states 64 lines / 1044 words on 1 line(s)
PASS append-only          prefix=True grew_by=9 line(s)
PASS noharm-arms-named    LOG names reg_gate 36 of 38 + corpus-idx on 1 line(s)
r62 routed defects closed 5 of 5
EXIT=0

$ python3 -B verifiers/check_r63_routed_repairs.py --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05
FAIL late-write-tracked   not a tracked blob at 35d44b4b4dcdda234b5dbff7af37e432fec55f05
FAIL receipt-rev-named    LOG never names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a
FAIL entry-size-named     LOG never states 64 lines / 1044 words for corpus/knowledge/erratum-absorption-round62.md
FAIL append-only          prefix=True grew_by=0 line(s)
FAIL noharm-arms-named    LOG does not name reg_gate 36 of 38 + corpus-idx
r62 routed defects closed 0 of 5
EXIT=1
```

Both directions reproduce the declared baseline exactly — including the E1-sensitive line
`prefix=True grew_by=0` failing check 4 at the do-nothing tip.

Extra probe (free; runs only in `tempfile.mkdtemp`, never the lane):

```
$ python3 -B verifiers/check_r63_routed_repairs.py --self-test
self-test: 0 failure(s) over 15 assertions
EXIT=0
```

## Attack 2 — worktree-read audit (MutCalibInstrument M1 class)

Full-file read plus mechanical sweep. Every evidence read in the check path goes through git
object-store commands on `<rev>`:

- `git()` helper (line ~72): `subprocess.run(["git", "-C", str(root)] + args)` — only.
- `show()` (line 75): `git show <rev>:<path>` → `check_receipt_rev` (lines 96 receipt / 103 LOG),
  `check_entry_size` (111 ENTRY / 116 LOG), `check_append_only` (126 `R62_TIP` / 127 `<rev>`),
  `check_noharm` (138 NOHARM / 152 LOG).
- `check_late_write` (~84–95): `git ls-tree -r <rev> -- LATE` plus `git cat-file -s <rev>:LATE`
  with a `>0` substance floor.

Sweep results (`grep -n -E 'os\.path|open\(|read_text|write_text|exists\(|LANE|Path\(|\.iterdir|glob'`):

```
52:LANE = Path(__file__).resolve().parent.parent
188:    p.write_text(text)                          # _write — self-test fixture only
219:    _write(root, LOG, (root / LOG).read_text() …)  # _repaired — self-test temp tree only
236:    tmp = Path(tempfile.mkdtemp(prefix="r63-c2-"))
266:            len((base / ENTRY).read_text().splitlines())  # self-test, temp ENTRY
267:            len((base / ENTRY).read_text().split())
276:        global R62_TIP                           # self-test monkey-patch, restored in finally
315:            _write(base, ENTRY, …)               # self-test M3 arm
353:    ap.add_argument("--root", default=str(LANE)…)  # repo root for `git -C`, not a file read
361:    root = Path(args.root).resolve()
362:    if not (root / ".git").exists():              # env precondition → exit 2, feeds no check
```

**No `os.path.exists`/`open()`/`read_text` on the lane worktree participates in any check.**
Every `read_text`/`write_text` lives inside `_write`/`_repaired`/`self_test` and operates on the
`mkdtemp` scratch repo (line 236). The only filesystem predicate outside the self-test —
`(root / ".git").exists()` at line 362 — is a precondition that returns exit 2; it is env
validation, not counted evidence. The self-test's first arm (lines ~247–250) constructs an
untracked copy of `LATE` on disk at a rev where it is untracked and asserts check 1 stays
`False` — the exact M1 mutation, killed by arm, not prose. Additional assurance: `git show`/
`ls-tree`/`cat-file` never apply worktree smudge/textconv filters; `R62_TIP` (line 53) is a
pinned 40-hex constant so check 4's baseline cannot drift with `--rev`; `--rev` is constrained
to full 40-hex (`REV_RE`, line 359) and lowercased (line 366).

## Attack 3 — check 4 vs erratum E1

Plan E1 (`plans/round-63.md:150-159`) requires two conjuncts, both reported separately:
r62-tip bytes are a byte-prefix of `<rev>`'s LOG **and** `<rev>`'s LOG adds ≥1 line.

Committed implementation (`check_append_only`, lines ~124–134):

```python
base_log = show(root, R62_TIP, LOG)          # baseline pinned to the frozen control rev
rev_log  = show(root, rev, LOG)
…
prefix = rev_log.startswith(base_log)        # byte-prefix conjunct
grew   = len(rev_log.splitlines()) > len(base_log.splitlines())  # grew_by >= 1
return prefix and grew, ("prefix=%s grew_by=%d line(s)" % …)
```

E1 is implemented verbatim: both conjuncts, both printed. Empirically the growth conjunct is
load-bearing — at `35d44b4b` the run prints `prefix=True grew_by=0` and the check fails,
yielding the declared `0 of 5` (the pre-E1 single conjunct would print `1 of 5`;
MutCalibInstrument F1 independently confirmed this on a `--pre-e1` faithful clone). The
self-test's `rewrite` arm (a rewritten LOG at equal length) kills the prefix-conjunct-evasion
mutant M4. **Faithful.**

## Attack 4 — checks 2/3/5 and the appended suffix

Code reality: all three scan **every line** of `LOG@<rev>` — `check_receipt_rev`
(`named = [line for line in log.splitlines() if token in line and "receipt" in line.lower()]`,
lines ~103–106), `check_entry_size` (`hits = [line … ENTRY in line and str(lines) in line and
str(words) in line]`, ~116–119), `check_noharm` (`named = [line … "reg_gate" in line and
"corpus-idx" in line and count_token in line]`, ~152–155). None restricts the match to bytes
appended after the `R62_TIP` prefix. The plan says "appended correction line" for check 2
(`plans/round-63.md:99-101`) and the counter docstring repeats "appended line" for check 2 only;
RevCalibChecks F6c recommended suffix scoping for all three and it was not adopted in code.

**Why it is provably equivalent to suffix scoping on committed bytes** (the reason this is a
bound, not a defect):

1. If check 4 passes, `LOG@<rev>` is `LOG@35d44b4b` followed by ≥1 appended line — so any
   matching line either is a prefix line or contains appended bytes.
2. The 0/5 control run was executed on `LOG@35d44b4b` itself and proves **no single prefix
   line satisfies each check's full conjunction**: `LOG never names 3f911504…` (check 2 needs
   token + `receipt` on one line), `LOG never states 64 lines / 1044 words for …` (check 3 needs
   the entry path + both numbers on one line), `LOG does not name reg_gate 36 of 38 + corpus-idx`
   (check 5 needs all three on one line).
3. Therefore, whenever the counter can print `5 of 5`, every line satisfying checks 2/3/5
   necessarily contains appended bytes — an appended correction is genuinely required.

Sharpened evidence from the token sweep: `LOG@35d44b4b` does contain loose tokens — the entry
path itself at line 2557 (`…corpus/knowledge/erratum-absorption-round62.md…`, inside the R-b
landed-scope bullet) and `1044` inside a SHA-256 at line 1793 (`…ed41044b…`) — yet no *single
line* carries each check's conjunction. Per-token presence in the prefix is real;
per-conjunction presence is what the checks test, and it is absent at the tip.

Verified the satisfying lines at `cbbee56e` are the genuinely appended correction bullets
(`git diff 35d44b4b cbbee56e -- LOG.md` → `9 insertions, 0 deletions`, pure append):
defect-2a bullet names `receipt_rev=3f911504ce76d9ca186f297d6d4a9cd8ed77508a` + "receipt";
defect-2b bullet names the entry path + `64 lines / 1044 words`; defect-4 bullet names
`FAIL reg_gate` + `corpus-idx` + `36 of 38`. The receipts those tokens are extracted from are
committed bytes at `<rev>`: `receipt_rev=3f911504ce76d9ca186f297d6d4a9cd8ed77508a` at line 2 of
`C2-successor-measure.txt`; the `36 of 38` count sits on the `tip:` detail line between the
`FAIL reg_gate` and `FAIL corpus-idx` verdict lines in `noharm-tip.txt` — exactly the block the
code slices (`receipt[reg.end():idx.start()]`), and the first `N of M` in that block is `36 of 38`.

wc-parity check: `ENTRY` at `cbbee56e` ends with `\n`, so Python `splitlines()`/`split()` give
64/1044 — identical to the plan's `wc -l`/`wc -w` wording (`wc -lw` prints `64 1044`).

## Findings by severity

**No defect.** No worktree read exists in the check path; both commanded runs reproduce the
declared baseline verbatim; E1 is implemented exactly.

**LOW (latent, not reachable on committed bytes) — checks 2/3/5 match the whole LOG, not the
appended suffix.** Code is weaker than the plan/docstring "appended line" wording. On every rev
where the counter can print 5 of 5 the equivalence is forced by check 4 + pinned `R62_TIP` +
verified conjunction-absence in the prefix (above) — but the equivalence is inherited from the
conjunction of checks, not enforced inside checks 2/3/5. On a rev where check 4 already fails,
checks 2/3/5 could still pass off prefix lines and inflate a losing count (never a false
verdict: headline stays <5, exit stays 1). Bound: safe unless `R62_TIP` or the tip's LOG bytes
are ever re-pointed; those are frozen constants/immutable objects.

**LOW — check 3 uses bare substring matching for the counts.** `str(64) in line` and
`str(1044) in line` match inside superstrings (`640`, the `ed41044b` SHA substring). Same-line +
entry-path conjunction plus the verified prefix absence makes accidental satisfaction
implausible; a deliberate writer could satisfy the check with superstring digits without ever
stating the true counts. Committed data carries the true line, so the verdict is unchanged.

**LOW — check 1's substance floor is `size > 0`, not content.** A one-byte tracked blob at the
late-write path passes (MutCalibInstrument F8 recommended ≥1024 B + content markers); also
`ls-tree -r` + `cat-file -s` would pass a non-blob (tree/commit) at that path. Committed entry
is `100644 blob`, 10,224 B — real evidence, outcome unchanged. Adopted floor honestly matches
the plan wording ("is a tracked blob … is committed as wave evidence").

**BOUND (declared in the counter's own docstring) — the five checks do not map 1:1 to the five
routed defects.** Check 4 is a method guard, not a routed defect; routed defects 2c (post-report
child-commit claim) and 3 (probe-dependent Cursor reason) are corrected in the appended block
(defect-2c and defect-3 bullets verified present) but bound by no check — already reported as
MutCalibInstrument F9 / RevCalibChecks F6e; docstring declares this ("checks 2, 3 and 5 are
token linkage … a correction that names the right tokens with wrong prose are outside it").
`5 of 5` means the five declared checks, not five distinct routed defects.

## Smallest safe correction / explicit bound

The counter is the frozen declared predicate — any in-place change is a second measurement, so
**no correction to the committed file is safe or needed**; the honest move is the residual-risk
statement above. If a v2 counter is ever authored, the exact tightening text:

```python
def _appended_lines(root: Path, rev: str) -> list[str] | None:
    """Lines of LOG.md at <rev> strictly beyond the R62_TIP byte-prefix."""
    base = show(root, R62_TIP, LOG)
    log = show(root, rev, LOG)
    if base is None or log is None or not log.startswith(base):
        return None
    return log[len(base):].splitlines()
```

with `log.splitlines()` replaced by `_appended_lines(root, rev) or []` inside
`check_receipt_rev`, `check_entry_size`, `check_noharm`; and for check 3,
`str(n) in line` replaced by `re.search(r"(?<![0-9a-zA-Z])%d(?![0-9a-zA-Z])" % n, line)`
(kills the `ed41044b`-style SHA collision); and for check 1,
`git cat-file -t <rev>:LATE` required `== "blob"` plus a documented size floor.

## Residual risk / verification gaps

- `--rev` accepts any 40-hex including tree objects (`git ls-tree -r <tree>` resolves); harmless
  because the predicate measures whatever object is named, and the frozen command names commits.
- `git show` output decoded with `text=True`: a non-UTF-8 evidence blob at a future rev raises
  `UnicodeDecodeError` (uncaught → traceback, exit 1, not a per-check FAIL). All evidence files
  are UTF-8 on committed data.
- Environment-level trust (`git` on PATH, `.git` object store integrity) is outside the counter's
  scope; `(root / ".git").exists()` at line 362 touches the worktree filesystem but gates only
  the exit-2 precondition, never a check.
- Not re-audited here (out of scope): whether the *correction prose* is true — the counter
  counts token linkage only (declared bound). The defect-2c/3 corrections read as accurate in
  the appended block but no check binds them.

## Verdict

**NO DEFECT — the committed counter is honest.** The two commanded runs reproduce exactly
(`5 of 5` exit 0 at `cbbee56e`; `0 of 5` exit 1 at `35d44b4b`, with `prefix=True grew_by=0`
failing check 4 as E1 requires). Zero worktree reads in the check path (M1 class excluded by
code and by a dedicated self-test arm). Check 4 implements E1 verbatim. Checks 2/3/5 are
unscoped in code but provably equivalent to suffix-scoped on committed bytes — the one wording-
vs-code looseness is a declared-bound residual, recorded with proposed tightening text for any
future v2.

## Tooling record

No tools installed or upgraded (python3, git, xxd, wc, grep — all pre-existing system binaries;
pacman untouched per host-wide pause). All lane operations read-only; the only lane write is
this report.
