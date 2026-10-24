---
seat: RevC2Checks
role: reviewer (independent leaf)
round: 64
wave: 1
date: 2026-10-24
base: 078eec4a1f6a41c64ff8806f58b46a67cd413bfc (freeze c04fffbe, branch master)
scope: plans/round-64.md § C2 — computability and robustness of the four listed checks
verdicts: check 1 fix-required (blob-witness gap) · check 2 fix-required (look-alike + base-token literal) · check 3 fix-required (table collision, weak score tokens) · check 4 fix-required (stated count method is arithmetically false) · refusal rule fix-required
---

# Round 64 C2 — computed review of the four routed-defect checks

Measured at `c04fffbe` (plan freeze) with `git show`/`git log` only; the working
tree carries one inherited seat edit and no other modification (`git status
--porcelain`: ` M .ufo/waves/round-63/w2/MutW2SplitClauses.md` plus the
untracked round-64 dispatch files). `verifiers/check_r64_routed_repairs.py` does
**not exist** at `c04fffbe` (`ls` exit 2), so every verdict below is a verdict on
the *specification in § C2* plus the inherited E2 model in
`verifiers/check_r63_routed_repairs.py`, not on landed r64 bytes. ExecR64Counter
was live while this was written; re-run these probes against the landed file.

Tooling: `lsp` device is not exposed in this seat's tool inventory
(`read xd://lsp` unavailable; the workspace devices are `ast_edit` and `debug`),
so caller/definition/diagnostic checks were done from committed bytes with
`git show`/`grep`/`python3 ast` — recorded as an unavailability, not as semantic
proof. No tool installs or upgrades were made. No lane gate was executed; the
one program run was `verifiers/check_r63_routed_repairs.py --self-test`, which
creates its own `tempfile.mkdtemp(prefix="r63-c2-")` worlds and touches no lane
path (`_base_tree`/`_commit` at source lines 349–413).

Peer corroboration, independently measured and convergent: `ScribeLesson` (items
a/b/c) and `CriticC2Bound` (weak refuse-to-certify rule) reached the same three
boundaries I measured before their messages arrived.

---

## Verdict table

| # | Check | Fails at 078eec4 for the stated reason? | Lie-proof? | Verdict |
|---|---|---|---|---|
| 1 | `seat-edit-committed` | **yes** (marker 0 at 078eec4/38defdc, 1 in worktree) | **no** — a 1-line note commits the marker without the 82-line edit | **fix-required** |
| 2 | `control-revs-named` | yes, but **only because the suffix is empty** — whole-LOG scan is already green at base (LOG.md:2576) | **no** — incidental/quotable prose names all three tokens; pinned base is a literal | **fix-required** |
| 3 | `lowest-axis-corrected` | yes (no suffix line; no "lowest owned" line in base LOG) | weak — single-digit score tokens | **fix-required** (parse must be anchored; scores anchored to axis names) |
| 4 | `assertion-count-named` | yes for the ExecW2E2Patch half; **the stated tally method is false** (text count = 20, AST = 19, true tally = 23) | medium — a standalone `23` unconnected to assertions satisfies the file half | **fix-required** |
| — | refuse-to-certify rule if copied from r63 (`base_closed >= total`) | — | **no** — three vacuous LOG checks give base 1 of 4, target 4 of 4, both conjuncts pass | **fix-required** |

---

## Check 1 — `seat-edit-committed`

### Base failure, measured

```
$ git show 38defdc:.ufo/waves/round-63/w2/MutW2SplitClauses.md | grep -n 'temporal mismatch'
exit=1
$ git show 078eec4:.ufo/waves/round-63/w2/MutW2SplitClauses.md | grep -c 'temporal mismatch'
0
exit=1                      # grep -c exits 1 on zero matches
$ git show c04fffbe:.ufo/waves/round-63/w2/MutW2SplitClauses.md | grep -n 'temporal mismatch'
exit=1
$ grep -n 'temporal mismatch' .ufo/waves/round-63/w2/MutW2SplitClauses.md
728:   was a **temporal mismatch** on my part.
```

The marker is an added line of the inherited edit:

```
$ git diff 38defdc -- .ufo/waves/round-63/w2/MutW2SplitClauses.md | grep -n '^[+-].*temporal'
59:+   was a **temporal mismatch** on my part.
$ git diff --numstat 38defdc -- .ufo/waves/round-63/w2/MutW2SplitClauses.md
82      29      .ufo/waves/round-63/w2/MutW2SplitClauses.md
$ git hash-object .ufo/waves/round-63/w2/MutW2SplitClauses.md
df8cb8d4e641e467005a01bb04c9f24b555784cc
$ git rev-parse 38defdc:.ufo/waves/round-63/w2/MutW2SplitClauses.md
04bd23512cfc3f002c2c338407e447d7a37172c6
$ sha256sum .ufo/waves/round-63/w2/MutW2SplitClauses.md
e51509ff37b32948005151496a615db3159326056b903b64dc44aaff4336ba3c
```

So the base arm is red for exactly the stated reason, and the blob that would
close it is `df8cb8d4…` / sha256 `e51509ff…`.

### Lie surface

1. **One marker line credits an 82-line change.** The marker is one of 82 added
   lines. A commit that appends a sentence such as "the earlier comparison was a
   temporal mismatch" to the file — without adopting the seat correction — turns
   check 1 green. The review already has the phrase in prose form twice in the
   frozen plan (`git grep -n 'temporal mismatch' c04fffbe -- .` →
   `plans/round-64.md:24` and `:125`), i.e. the phrase is copy-pasteable from a
   committed file. That makes accidental and deliberate crediting equally cheap.
2. **Repo-scope leak at base.** Because the phrase exists in `plans/round-64.md`
   at base, any implementation that greps the worktree or the repo (rather than
   `git show <rev>:<path>`) passes check 1 at `078eec4`. The r63 model's M1 arm
   (`worktree:` arm, source lines 209–215) is exactly this class; r64 must carry
   the same arm.

### Fix text (exact, applies to the r64 counter)

Replace the check body with:

```python
SEAT_EDIT = ".ufo/waves/round-63/w2/MutW2SplitClauses.md"
SEAT_MARKER = "temporal mismatch"
SEAT_EDIT_BLOB_SHA256 = ("e51509ff37b32948005151496a615db3159326056b903b64"
                         "dc44aaff4336ba3c")   # the inherited seat edit, measured
                                              # at plan freeze from `git hash-object`
SEAT_PRIOR = "38defdc"                        # its committed predecessor

def check_seat_edit(root: Path, rev: str) -> tuple[bool, str]:
    blob = git(root, ["show", "%s:%s" % (rev, SEAT_EDIT)])
    if blob.returncode != 0:
        return False, "%s absent at %s" % (SEAT_EDIT, rev)
    body = blob.stdout
    if SEAT_MARKER not in body:
        return False, "marker %r absent at %s" % (SEAT_MARKER, rev)
    if hashlib.sha256(body.encode()).hexdigest() != SEAT_EDIT_BLOB_SHA256:
        return False, ("marker present but the blob at %s is not the seat edit "
                       "(sha256 mismatch)" % rev)
    added = [l for l in _diff_added_lines(root, SEAT_PRIOR, rev, SEAT_EDIT)
             if SEAT_MARKER in l]
    return bool(added), ("seat edit committed at %s (blob pin, %d marker "
                         "addition(s) vs %s)" % (rev, len(added), SEAT_PRIOR))
```

where `_diff_added_lines` parses `git diff -U0 <a> <b> -- <path>` and returns
`+` lines. If the L1 decides the pin is too tight (any later touch of that file
is then a new measurement), the *minimum* admissible weakening is: drop the
sha256 clause and require **all three** of (marker present) ∧ (the marker line
is a `+` line vs `38defdc`) ∧ (`≥ 60` added lines vs `38defdc`); 60 is a floor
under the measured 82 and is not satisfiable by notes alone. Do not ship the
marker-only form.

### Routed-input correction (calibration)

The spot-check's routed defect 1 quotes the edit as "41 insertions/13 deletions".
Measured at the freeze: **82 insertions / 29 deletions** (`git diff --numstat`,
above); the plan's § Inherited state already says 82+/29-. The seat file's mtime
is `2026-10-24 00:12:59` and the spot-check was committed at `00:20:12`
(`git log -1 --format='%ci' 078eec4`), so the 41/13 figure was not a later drift
of the file — it is a mismeasurement in the routed input. The round-64 lesson
should record the corrected figures (this is a *new* stale-citation instance, not
a fifth defect: check 1 does not cite the number).

---

## Check 2 — `control-revs-named`

### True committing revisions — three independent derivations, all agreeing

```
$ git log --diff-filter=A --format='%H' -1 -- .ufo/waves/round-63/controls/C1-do-nothing-v31.txt
8c4cefa8e1b751d5f93dbcc65349b8e985b102d8
$ git log --diff-filter=A --format='%H' -1 -- .ufo/waves/round-63/controls/C2-before-r62tip.txt
cbbee56e9a3589b0b46736ad36f1b77701def80e

# method B: full per-path history (only one commit each; .tail(-1) = add commit)
$ git log --follow --format='%H' -- <C1 path> | tail -1   -> 8c4cefa8e1b751d5f93dbcc65349b8e985b102d8
$ git log --follow --format='%H' -- <C2 path> | tail -1   -> cbbee56e9a3589b0b46736ad36f1b77701def80e
# (every touching commit: C1 = 1 commit 8c4cefa; C2 = 1 commit cbbee56)

# method C: rev-list walk, oldest touching commit, bounded by a rev
$ git rev-list c04fffbe -- <C1 path> | tail -1            -> 8c4cefa8e1b751d5f93dbcc65349b8e985b102d8
$ git rev-list c04fffbe -- <C2 path> | tail -1            -> cbbee56e9a3589b0b46736ad36f1b77701def80e

# also stable under --first-parent
$ git log --first-parent --diff-filter=A -1 c04fffbe -- <both paths>  -> same two revs
```

The spot-check's two revs are the true ones, so a LOG naming them is *truthful*.
The lie surface is not the value but the **context**:

### The base-look-alike (hard evidence)

`LOG.md` at base contains one committed line that satisfies every token of
check 2 at once:

```
$ git show c04fffbe:LOG.md | awk '{ if (index($0,"8c4cefa")&&index($0,"cbbee56")&&index($0,"35d44b4b")) print NR": "$0 }'
2576: - **Corrections to this block (appended in round 63; the committed lines above stand).** ... `8c4cefa8` (this round's plan-freeze commit) and `cbbee56e` (the wave-1 build) both descend from `e53b6e5c` ... "at report time only `35d44b4b` was a child ..."
```

Under the plan's own token rule (≥7 hex, non-hex boundaries, prefix match against
the computed rev) this line yields:

```
C1-do-nothing-v31.txt  prefix-hits: ['8c4cefa8']     (9 hex, prefix of 8c4cefa8e1…)
C2-before-r62tip.txt   prefix-hits: ['cbbee56e']     (9 hex, prefix of cbbee56e9a…)
base token 35d44b4b present, hex-bounded: True
control basenames present: False False
```

Consequences:

* A **whole-LOG** scan makes check 2 green at BASE_REV. The plan's hardening
  sentence ("whole-LOG substring matches do not count") is therefore
  load-bearing, not decorative: without suffix scoping the do-nothing control
  would print `1 of 4` instead of `0 of 4` for the wrong reason.
* Even **suffix-scoped**, the same prose copied into a round-64 corrections block
  ("the r63 plan-freeze and wave-1 commits 8c4cefa8/cbbee56e both descend from
  e53b6e5c; only 35d44b4b was a child") credits check 2 while saying nothing
  about which revision committed the two controls. That is the M95 class in a new
  costume: tokens right, claim absent.
* The pinned base is specified as a **literal** (`35d44b4b`). Both control files
  carry the full hash internally and agree on it:
  `C1-do-nothing-v31.txt:2: at: 35d44b4b4dcdda234b5dbff7af37e432fec55f05`;
  `C2-before-r62tip.txt:1: FAIL late-write-tracked … at 35d44b4b4dcdda…`. A
  literal here is exactly the "hardcoded value the bytes no longer say" defect
  the counter exists to catch.

### Derivation failure modes, measured

```
$ git log 8c4cefa --diff-filter=A --format='%H' -1 -- .ufo/waves/round-63/controls/C2-before-r62tip.txt
(empty)  exit=0
$ git show 8c4cefa:verifiers/check_r63_routed_repairs.py >/dev/null ; echo $?
128   fatal: path 'verifiers/check_r63_routed_repairs.py' exists on disk, but not in '8c4cefa'
$ git show deadbeef:verifiers/check_r63_routed_repairs.py >/dev/null ; echo $?
128   fatal: invalid object name 'deadbeef'.
```

An empty derivation exits 0: the counter must map *empty* to FAIL, not to
"no expected value, skip". A rev must be 40-hex (r63 `REV_RE =
^[0-9a-fA-F]{40}$`, `main()` exits 2 on a malformed `--rev`); otherwise
`deadbeef` reaches `git show` and the counter dies with a traceback instead of
`error: could not evaluate` (r63 `main()` lines 641–648 catch
`SubprocessError`/`OSError` → exit 2).

### Fix text (exact)

```python
CONTROLS = (
    (".ufo/waves/round-63/controls/C1-do-nothing-v31.txt", "C1-do-nothing-v31"),
    (".ufo/waves/round-63/controls/C2-before-r62tip.txt",  "C2-before-r62tip"),
)

def committing_rev(root: Path, rev: str, path: str) -> str | None:
    p = git(root, ["log", rev, "--diff-filter=A", "--format=%H", "-1", "--", path])
    out = p.stdout.strip()
    return out.splitlines()[-1] if out else None      # empty derivation -> FAIL

def check_control_revs(root: Path, rev: str) -> tuple[bool, str]:
    derived, bases = {}, []
    for path, base_name in CONTROLS:
        r = committing_rev(root, rev, path)
        if r is None:
            return False, "no committing revision for %s at or before %s" % (path, rev)
        blob = show(root, rev, path)
        if blob is None:
            return False, "%s absent at %s" % (path, rev)
        b = re.findall(r"(?<![0-9a-fA-F])([0-9a-f]{40})(?![0-9a-fA-F])", blob)
        if len(set(b)) != 1:
            return False, "%s does not pin exactly one base revision" % path
        derived[base_name] = r
        bases.append(b[0])
    if len(set(bases)) != 1:
        return False, "the two controls pin different base revisions"
    base = bases[0]
    # boundary-tightened, suffix-scoped, ONE line must carry the whole claim
    named = []
    for line in _suffix_lines(root, rev):          # suffix vs BASE_REV, never whole LOG
        ok = all(_hex_prefix_re(t).search(line) for t in derived.values())
        ok = ok and _hex_prefix_re(base).search(line)
        ok = ok and all(name in line for _, name in CONTROLS)
        ok = ok and ("committed" in line.lower() or "added in" in line.lower())
        if ok:
            named.append(line)
    return bool(named), ("LOG names %s + base %s… on %d line(s)"
                         % (", ".join(sorted(derived.values())), base[:8], len(named))
                         if named else "LOG never names both control commits + base")

def _hex_prefix_re(full: str) -> "re.Pattern[str]":
    # >=7 hex chars, hex-bounded, and a prefix of the computed full hash
    return re.compile(r"(?<![0-9a-fA-F])(%s[0-9a-f]{0,33})(?![0-9a-fA-F])"
                      % re.escape(full[:7]))
```

The `_hex_prefix_re` construction must be implemented as "maximal hex run
`t`, `len(t) >= 7`, `full.startswith(t)`" (a run may be 7…40 chars); the regex
above is the equivalent bounded form for the 7-char stem and must be validated
by the self-test arms below, because the 9-hex look-alike tokens
(`8c4cefa8`, `cbbee56e`) must still match when the *claim* is right and must not
credit when the control basenames are absent.

Required self-test arms for check 2 (all constructed, none using the lane repo):

1. **look-alike:** copy base `LOG.md` line 2576's prose into the suffix, with the
   correct derived revs and base → check must stay **red** (no control basenames).
2. **one-sided:** a suffix line naming only `8c4cefa8` and the base → red.
3. **wrong rev:** a suffix line naming a *different* 40-hex rev with both control
   basenames → red.
4. **pinned-base substitution:** rewrite the two control blobs at a constructed
   rev so they pin `deadbeef…`; a LOG naming `35d44b4b` and both control basenames
   → red (the base is computed, not literal).
5. **empty derivation:** a constructed rev at which the C2 control does not exist
   (`git log` exits 0, prints nothing) → red, no exception.
6. **full-hash and short-hash both accepted:** a suffix line naming the full
   40-hex revs and a suffix line naming 7-hex prefixes must both pass, proving the
   boundary rule does not reject truthful full hashes (the r63 `_tok_re` exact-token
   shape would reject a 40-hex name of a 7-hex token, which is the mirror bug).

---

## Check 3 — `lowest-axis-corrected`

### Base failure, measured

At `078eec4`/`c04fffbe` the LOG suffix is **empty by construction** — the
plan-freeze commit touched only `plans/round-64.md` and
`.ufo/waves/round-64/census-before.txt`:

```
$ git diff --stat 078eec4 c04fffbe
 .ufo/waves/round-64/census-before.txt |  17 +++
 plans/round-64.md                     | 197 ++++++++++++++++++++++++++++++++++
 2 files changed, 214 insertions(+)
$ python3 … (LOG at c04fffbe vs 078eec4): startswith=True base lines 2588 tip lines 2588 suffix lines 0
$ git show c04fffbe:LOG.md | grep -in 'lowest owned'
(no output)
```

So check 3 is red at base — but, like check 2, *only* because the suffix is
empty. The base arm carries no discriminating power for the token scan.

### The parse is computable but not as "parse the axes table" naively

Exact row shapes at the freeze (`## axes` heading at line 24, next heading
`## planned` at line 38):

```
L27 header: axis='Axis' score='Score' owned='Owned?' lastchg='Last change'
L28        axis='depth'                  score='9'            owned='owned'  cells=5
L29        axis='consistency (calibration sub-axis)' score='10' owned='owned' cells=5
L30        axis='coverage'               score='8.5 — was 8.0' owned="advisory (…)" cells=5
L31        axis='operability (advisory)' score='8.5 — was 8.0' owned="grep -c '<skills>'` …" cells=6
L32        axis='freshness (advisory)'   score='8'            owned='Ho'     cells=9
L33        axis='calibration (advisory)' score='8.5 — was 8.0' owned='advisory' cells=5
L34        axis='adjacency (advisory)'   score='8.0 — was 7.5' owned="grep -cE '^\" …" cells=14
```

Two concrete hazards:

1. **There is a second axis table.** Under `## Move log` (heading at line 185)
   there is a table `| Axis | Verdict | Evidence and limit |` whose rows also
   begin with `depth`, `coverage`, `operability`, `freshness`,
   `calibration / owned consistency sub-axis`, `adjacency` (lines 260–266). An
   unanchored "parse the axes table" scan picks the **last** `depth` row — line
   262, three cells, no score (my naive scan did exactly this and printed
   `(262, None, '', 3) depth`). The parse must be bounded to `## axes` …
   next `##`.
2. **The evidence cell contains `|`**, so row cell counts run 5–14 and the
   `Owned?` cell is only at index 3 for the two owned rows today. The owned set
   must come from the header sentence (`Axes owned by this lane: **depth +
   consistency**`, line 3, verified: `owned sentence: depth + consistency`) and
   the score from `cells[1]` (which precedes the first embedded pipe and is
   stable), not from a positional `cells[3]` walk over all rows.
3. **Score cells are prose** (`8.5 — was 8.0`); take `re.match(r'\d+(?:\.\d+)?',
   cells[1])`. The minimum over the owned set at base is `min(9, 10) = 9` →
   depth. A future `9.5`/`10` pair must move the answer; the counter must not
   hardcode "depth".

### Weak token shape

"both scores named" with single-digit `9` means the LOG line's credit rests on a
one-character token. With a hex-boundary rule, any suffix line containing a
standalone `9` and `10` (e.g. "9 gate rows, 10 arms") plus the words `depth` and
`lowest` passes. The base LOG alone has 23 standalone `23`-style numeric tokens
in unrelated prose, so incidental numbers in a corrections block are the norm,
not the exception.

### Fix text (exact)

```python
AXES_HEADING = "## axes"
OWNED_RE = re.compile(r"Axes owned by this lane:\s*\*\*(.+?)\*\*")

def axes_scores(root: Path, rev: str) -> dict[str, float]:
    sc = show(root, rev, "SCORECARD.md")
    if sc is None:
        raise EnvError("SCORECARD.md absent at %s" % rev)
    sec = sc.split(AXES_HEADING, 1)
    if len(sec) != 2:
        raise EnvError("no %r section" % AXES_HEADING)
    body = sec[1].split("\n## ", 1)[0]          # stop at the next ## heading
    m = OWNED_RE.search(sc)
    if not m:
        raise EnvError("owned-axis sentence absent")
    owned = [a.strip() for a in m.group(1).split("+")]
    out = {}
    for line in body.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        axis, cell = cells[0], cells[1]
        if axis in ("Axis", "---") or not re.match(r"-?\d+(?:\.\d+)?", cell):
            continue
        for want in owned:
            if axis == want or axis.startswith(want + " "):
                out[want] = float(re.match(r"-?\d+(?:\.\d+)?", cell).group(0))
    if set(out) != set(owned):
        raise EnvError("owned axis rows missing: %s" % (set(owned) - set(out)))
    return out

def check_lowest_axis(root: Path, rev: str) -> tuple[bool, str]:
    scores = axes_scores(root, rev)
    lowest = min(scores, key=lambda a: (scores[a], a))
    low_val, other = scores[lowest], scores[[a for a in scores if a != lowest][0]]
    num = r"(?<![0-9A-Za-z.])%s(?![0-9A-Za-z.])"
    named = [l for l in _suffix_lines(root, rev)
             if re.search(r"(?i)lowest", l)
             and re.search(r"(?i)\bdepth\b", l)
             and re.search(r"(?i)\bconsistency\b", l)
             and re.search(num % re.escape(_fmt(low_val)), l)
             and (re.search(num % re.escape(_fmt(other)), l)
                  or re.search(num % re.escape(_fmt(scores["consistency"])), l))]
    return bool(named), ("LOG states depth is the lowest owned axis with %s and %s "
                         "on %d line(s)" % (_fmt(low_val), _fmt(other), len(named))
                         if named else "LOG never states the lowest owned axis")
```

with `_fmt(x)` emitting `9`/`10`/`9.5` (no trailing `.0`) and `lowest` derived
from the parse (do not assert depth by name in code; assert it in the *self-test*
arm that plants `depth 9 / consistency 10`). If the frozen predicate's wording
"state that depth is the lowest owned axis" is read as requiring the *name*
depth in the line, the regex above already enforces `depth` and `consistency`
plus `lowest`; what it forbids is crediting a line that only says "9 and 10".

Required check-3 self-test arms:

1. planted SCORECARD where `consistency` is 9 and `depth` is 9.5 → the counter's
   computed lowest is `consistency`; a LOG line naming depth as lowest must be red.
2. planted SCORECARD with an advisory row scoring 8.0 and an embedded `|` in its
   evidence cell → the advisory row must not enter the minimum.
3. the `## Move log` table copied *above* `## axes` in a constructed SCORECARD →
   the parse must still find the `## axes` table (anchoring arm).
4. a suffix line "9 gate rows, 10 arms; lowest" → red (numbers not axis-anchored).
5. a suffix line "depth is the lowest owned axis (9); consistency (10)" → green.

---

## Check 4 — `assertion-count-named`

### The stated computation is arithmetically false

The plan says the counter computes the r63 C2 counter's self-test tally "by
counting `check(` invocations in `verifiers/check_r63_routed_repairs.py` at
`<rev>` (expected 23…)". Measured on the committed bytes (blob identical at both
claim-relevant revs):

```
$ git show c04fffbe:verifiers/check_r63_routed_repairs.py | grep -c 'check('
20
$ python3 -c "…ast.walk… isinstance(n.func, ast.Name) and n.func.id=='check'…"
AST check-call sites (excludes def): 19
lines: [444, 450, 452, 454, 456, 458, 460, 476, 478, 485, 497, 510, 517, 523, 533, 543, 550, 595, 601]
```

`20` includes the `def check(...)` at line 427; `19` is the AST call-site count.
Neither is `23`. The true tally is `17` fixed sites (lines 444–550) **plus** the
two loop-body sites (595, 601) executed once per arm **times 3 arms**
(`for arm_label, mode, cand_src, cand_name in (("label-only",…),
("fingerprint",…), ("worktree-read",…))`, source lines 578–582) = `17 + 6 = 23`.
So "count `check(` invocations" yields 19 or 20 at **every** rev; a counter
implementing the plan's sentence literally cannot print 23, and a counter that
hardcodes 23 after a text count is the M95 class.

### The correct computation, measured (materialization)

Run the materialized blob as a process and parse its tally line:

```
$ mkdir -p /tmp/r64rev
$ git show 078eec4:verifiers/check_r63_routed_repairs.py > /tmp/r64rev/078eec4.py
$ git show c04fffbe:verifiers/check_r63_routed_repairs.py > /tmp/r64rev/c04fffb.py
$ sha256sum of both git blobs: b9e627371cfc5e83a5bbde2b2ab455c819cc9419eafded5c5671bf35d66ed105 (both)

$ time python3 -B /tmp/r64rev/078eec4.py --self-test ; echo EXIT=$?
real 0m0.519s   ...  self-test: 0 failure(s) over 23 assertions      EXIT=0
$ time python3 -B /tmp/r64rev/c04fffb.py --self-test ; echo EXIT=$?
real 0m0.521s   ...  self-test: 0 failure(s) over 23 assertions      EXIT=0
$ diff /tmp/r64rev/078eec4_st.txt /tmp/r64rev/c04fffb_st.txt && echo IDENTICAL
IDENTICAL
$ time python3 -B verifiers/check_r63_routed_repairs.py --self-test   (in-lane copy)
real 0m0.520s   self-test: 0 failure(s) over 23 assertions   EXIT=0
```

Determinism: identical stdout at three runs across two revs; runtime ≈0.52 s;
the self-test builds its own `tempfile.mkdtemp` git worlds with pinned
`GIT_AUTHOR_DATE`/`GIT_COMMITTER_DATE` (source lines 349–362), so results do not
depend on the host clock, the lane working tree, or `git config user.*`. Running
the copy from `/tmp` works because `--self-test` never consults `LANE`
(`LANE = Path(__file__).resolve().parent.parent` is only `--root`'s default).
That satisfies "computable from committed bytes at `<rev>`" honestly: the code
*executed* is the blob at `<rev>`.

Failure modes at arbitrary revs (measured):

```
$ git show 8c4cefa:verifiers/check_r63_routed_repairs.py >/dev/null ; echo $?
128   fatal: path 'verifiers/check_r63_routed_repairs.py' exists on disk, but not in '8c4cefa'
$ git show deadbeef:verifiers/check_r63_routed_repairs.py >/dev/null ; echo $?
128   fatal: invalid object name 'deadbeef'.
$ python3 -B /tmp/r64rev/… --self-test  (missing git binary / non-git PATH)
  -> raises (subprocess FileNotFoundError) — the counter must catch OSError and exit 2
```

So the counter must: (a) read the blob with `git show`; (b) treat a missing path
or invalid rev as FAIL/exit 2, never a traceback; (c) not run the *worktree* copy
under any circumstances (r63's M1 arm is the model — an r64 arm must swap the
worktree copy for a "20 assertions" source and prove check 4 still reads the
rev's bytes).

### Boundary rules — and whether `23` disambiguates

Measured on `.ufo/waves/round-63/w2/ExecW2E2Patch.md` at `c04fffbe`:

```
23 substring count: 13
23 maximal-hex-run exact matches: 0
21 maximal-hex-run exact matches: 11      (the 11 stale "21 assertions" tokens)

runs containing 23: ['323', '35d44b4b4dcd…']  (hashes such as …da234b…)
```

So yes — at base the `23` substrings are all *inside* longer hex runs
(`323`, `da234b`, `35d44b4b…`), and a hex-bounded exact-token rule yields 0;
the boundary rule does disambiguate, and the file half of check 4 is red at base
for the stated reason. Two residual credit paths remain:

* A standalone `23` **not about assertions** (a section number, a count of
  mutants, a line reference). At base there are no standalone `23` tokens, so
  this is future-proofing: require the number adjacent to `assertions`.
* The amendment can name `23` while **all 11 `21 assertions` tokens stay**, so
  the file then asserts both. The plan's wording ("amended … to name that exact
  number") permits this; the routed defect (a stale seat number) is then only
  contradicted, not removed. If the lane wants the stronger half, add: no line in
  the amended file may say `21 assertions` *unless* it is inside a correction
  block that names 23 (i.e. the token `21` may survive only on a line that also
  names `23`).

### Fix text (exact)

```python
EXEC_PATCH = ".ufo/waves/round-63/w2/ExecW2E2Patch.md"
R63_COUNTER = "verifiers/check_r63_routed_repairs.py"
TALLY_RE = re.compile(r"self-test: \d+ failure\(s\) over (\d+) assertions")

def r63_tally(root: Path, rev: str) -> tuple[int | None, str]:
    blob = git(root, ["show", "%s:%s" % (rev, R63_COUNTER)])
    if blob.returncode != 0:
        return None, "%s absent at %s" % (R63_COUNTER, rev)
    static = _static_tally(blob.stdout)          # see below
    tmp = Path(tempfile.mkdtemp(prefix="r64-tally-"))
    try:
        p = tmp / "cnt.py"
        p.write_text(blob.stdout)
        proc = subprocess.run([sys.executable, "-B", str(p), "--self-test"],
                              capture_output=True, text=True, timeout=120,
                              cwd=str(tmp))      # never the lane worktree
        m = TALLY_RE.search(proc.stdout)
        if proc.returncode != 0 or m is None:
            return None, "the counter at %s did not print a tally" % rev
        runtime = int(m.group(1))
        if static is None or static != runtime:
            return None, ("tally disagreement at %s: static=%s runtime=%s"
                          % (rev, static, runtime))
        return runtime, "tally %d at %s (static = runtime)" % (runtime, rev)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

def _static_tally(src: str) -> int | None:
    # 17 fixed call sites + 2 loop-body sites * 3 arms; the loop table is
    # parsed as the tuple of 3 (label, mode, src, name) rows under
    # `for arm_label, mode, cand_src, cand_name in (`.
    tree = ast.parse(src)
    loop_calls, fixed = 0, 0
    for fn in ast.walk(tree):
        if isinstance(fn, ast.FunctionDef) and fn.name == "self_test":
            for node in ast.walk(fn):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
                        and node.func.id == "check":
                    fixed += 1
    # `fixed` counts all sites (19).  Subtract the two sites inside the arms
    # loop and add them back multiplied by the number of arm rows.
    arms = _arm_rows(src)                       # 3 at cbbee56 and at tip
    if arms is None:
        return None
    return (fixed - 2) + 2 * arms
```

`_arm_rows` must count the tuples in the `for arm_label, mode, cand_src,
cand_name in (` block (3 measured), not a hardcoded 3; if the block shape is not
recognized it returns `None` and check 4 must FAIL with "tally not computable"
rather than guess. The check then requires an `EXEC_PATCH` line at `<rev>` that
matches `(?<![0-9A-Za-z])<tally>(?![0-9A-Za-z])` **and** contains `assertions`,
and that line must be an addition relative to `BASE_REV` (so a pre-existing
coincidence can never satisfy it).

Cost: one subprocess ≈0.5 s plus ~6 `git` calls; acceptable. Timeout 120 s guards
a future pathological self-test. If the lane judges executing the historical
counter too heavy or too trusting, the *minimum* honest alternative is `_static_tally`
alone **with** the arm-row parse and a "shape unrecognized → FAIL" branch — but
then the plan sentence "counting `check(` invocations" must be rewritten, because
the bare text count is 19/20 and will never be 23.

Required check-4 self-test arms:

1. substituted source at a constructed rev with 20 `check(` call sites and a
   printed tally of 20 → the amended-file line naming 23 must not credit.
2. the amended file naming `123 assertions` → red (boundary: `123`).
3. the amended file naming `23` in a hash (`…da234b…`) only → red (this is the
   base state, measured).
4. the amended file naming `23` on a line without `assertions` → red.
5. the worktree copy of `ExecW2E2Patch.md` amended but the rev's blob not →
   red (blob-read arm).
6. the r63 counter blob absent at the constructed rev → red, no traceback.

---

## The do-nothing control and refuse-to-certify rule

### Base arm at `078eec4` — measured, and weaker than it looks

```
$ git show 078eec4:LOG.md | wc -l   -> 2588
$ git show c04fffbe:LOG.md | wc -l  -> 2588   ; suffix vs 078eec4 = 0 lines
```

Check 1 fails at base because the *committed* file lacks the marker (verified
above). Checks 2–4 fail at base **only because the LOG suffix is empty**; their
input files all exist at base (controls at `8c4cefa`/`cbbee56`, SCORECARD rows,
`check_r63_routed_repairs.py` with 23 runtime assertions). Therefore the frozen
second conjunct (`--rev 078eec4` → `0 of 4`, exit nonzero) cannot distinguish a
counter that computes checks 2–4 from one where they are `return True, "ok"`.

### Why the r63 refusal rule is not enough for r64

`check_r63_routed_repairs.py` refuses only when `base_closed >= total`
(source line 331). For r64, `total = 4` and checks 2–4 all read one source (the
LOG suffix): a counter with three vacuous token checks plus a real check 1
prints `1 of 4` at the base (so the base conjunct *fails* — but only on the
count) and `4 of 4` at the target, passing **both** frozen conjuncts while
computing nothing. The process-audit arms (label-only, fingerprint,
worktree-read) are what make the r63 rule bite; the r64 counter must carry them
*and* a **partial-world** arm where the suffix exists and names wrong values
(r63's `partial` world is the model: honest counter prints `2 of 5` there).

### Fix text (exact)

```python
def base_control(root: Path) -> tuple[int, int]:
    return sum(1 for _, fn in CHECKS if fn(root, BASE_REV)[0]), len(CHECKS)

# in run():
base_closed, total = base_control(root)
if base_closed != 0:                     # NOT `>= total`
    print("base arm failed: the do-nothing control at %s closed %d of %d; "
          "the counter refuses to certify any revision"
          % (BASE_REV, base_closed), file=sys.stderr)
    return 1
```

and `--base-arm` must exit 0 only when the printed count is exactly `0 of 4`.
Add a self-test arm that plants a suffix matching **only** checks 2–4 with wrong
values in a constructed world and asserts the candidate is rejected at *both* the
base world (`1 of 4`, must not be `0 of 4` — proving the check is not vacuous)
and the target world (`4 of 4` printed but the base refusal fires).

Also pin the base immutably: `BASE_REV_LITERAL` must be a 40-hex literal equal to
`078eec4a1f6a41c64ff8806f58b46a67cd413bfc`, and the self-test must assert
`BASE_REV == BASE_REV_LITERAL == "078eec4…"` **and** that a constructed world in
which `BASE_REV` is repointed at a rev where checks 2–3 would pass is refused
(the CriticC2Bound point — a `>= total` rule does not catch a partial base). The
cleanest immutable pin is a second literal `FROZEN_BASE = "078eec4a…"` compared
against `BASE_REV` at import; the self-test mutates `BASE_REV` in a subprocess
copy and requires the refusal.

---

## Residual risk

1. **Single-line kitchen-sink credit.** Checks 3 and 4 each scan one line; one
   round-64 LOG/corrections line can satisfy check 3 and a second can satisfy
   check 4 while the prose around it is wrong. The predicates are token
   predicates (as in r63); the plan's bound says that is acceptable, but the
   receipt should say so explicitly so the non-author closure does not read
   `4 of 4` as prose-correctness.
2. **`--rev` and the base conjunct's identity.** The frozen predicate's second
   command uses the full 40-hex base. If a caller passes the short `078eec4`,
   r63's `REV_RE` exits 2; the r64 counter must use the same rule so the control
   cannot be run against a different revision by abbreviation.
3. **Historical-code execution.** Check 4's runtime tally executes the blob at
   `<rev>` in a temp dir. That is the honest reading of "computed from committed
   bytes", but it trusts the historical counter not to write outside its cwd.
   The measured r63 counter confines itself to `tempfile.mkdtemp`; a future rev's
   counter is a different measurement (the static cross-check is the guard).
4. **Check 1's blob pin** makes any later touch of `MutW2SplitClauses.md` a new
   measurement. That is the intended cost; if the L1 rejects it, use the 60-line
   floor variant named above.
5. **The spot-check's 41+/13- figure** (routed defect 1) is wrong against the
   measured 82+/29-. Record it in the round-64 lesson; do not let it propagate
   into the LOG correction.

## Verification gaps

* `verifiers/check_r64_routed_repairs.py` was absent at `c04fffbe`; all verdicts
  are on the specification + inherited model. Re-run each probe against the
  landed file (I have named the exact probes: `grep -c 'check('`, the AST site
  list, `git log --diff-filter=A` on both controls, the `## axes` section parse,
  the base-LOG look-alike at line 2576, and the two `git show` failure revs).
* No `lsp` server device was available, so no semantic reference check was
  possible; all caller/definition claims are from committed bytes.
* I did not execute any lane gate; the only program run was the r63 counter's
  own `--self-test` (tempdir-only, exit 0, 0.52 s).

## Claims this report supports / falsifies

* **Supports** C2's *declared before data* base expectation (`0 of 4` at
  `078eec4`): every one of the four checks is red there for the stated reason
  (check 1 by committed bytes; checks 2–4 by empty suffix).
* **Falsifies** the plan's check-4 mechanism sentence ("counting `check(`
  invocations … expected 23"): the text/AST counts are 19/20; the tally 23 needs
  loop multiplicity or a runtime parse.
* **Falsifies** the safety of a whole-LOG scan for check 2: `LOG.md:2576` at base
  already names both committing revs and the pinned base.
* **Supports** the r63 spot-check's check-2/4 *values* (revs 8c4cefa/cbbee56,
  assertion count 23) with three independent derivations and a measured runtime
  tally, and **falsifies** its defect-1 size quote (41+/13- vs 82+/29-).
