# FalsifyV31G7TooStrong — G7 rejects an honest expanded abbreviation

Seat: `L1kotoba62.FalsifyV31G7TooStrong` — scoped critic, round-62 wave 2, 2026-10-23.
Reviewed commit: `e6da78bbe420722dd18a13182a7c4b64ce02f005`.
Axes: **depth** (assigned), with **consistency/calibration** implications.

## Finding and counterexample

**Observed false positive; fixable implementation defect.** The successor rejects a
supported non-event Action cell solely because a backticked abbreviation is absent
as literal text from the evidence. The abbreviation is explicitly expanded in the
cell; it neither invents a vendor identifier nor asserts a new loading event.

Exact Action-cell bytes (no trailing newline):

```python
b'Scope rules to specific files using `YFM` (YAML frontmatter); apply only when matching specified patterns. (S103 :194)'
```

`YFM` means **YAML frontmatter**, as stated immediately in parentheses. The rest
is the existing Claude Code Action in the scoped-rule table at
`/home/vgpnk/Projects/shokunin/kotoba-shokunin/SKILL.md:141`.
The scope key remains `paths`; this does not claim that `YFM` is a frontmatter key,
API, or event. Its instruction and condition are supported by the cited vendor
sentence. A reader can expand the abbreviation without changing the action.

Exact cited page-line bytes, including the trailing LF:

```python
b'Rules can be scoped to specific files using YAML frontmatter with the `paths` field. These conditional rules only apply when Claude is working with files matching the specified patterns.
'
```

The full-page probe used **the entire committed S103 snapshot**, not merely this
excerpt, obtained with the absolute-repository `git show` command in Appendix A.
That command's measured SHA-256 is
`82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7`.
Appendix A includes the complete reproducible extraction, input byte counts,
full-page absence test, exact reason lists, and actual process exit code.

For an independently inlined complete page, Appendix A also runs a distilled
arm-level fixture whose **entire page** is exactly the byte string above. Its
cell is exactly:

```python
b'Scope rules to specific files using `YFM` (YAML frontmatter); apply only when matching specified patterns. (S900 :1)'
```

`S900 :1` is the explicitly synthetic fixture citation, not a claim that the
vendor sentence occurs at the first line of S103. The principal counterexample
uses the real `S103 :194` citation and the whole committed page.

### Exact reason list

Both the full-page and distilled probes return this successor reason list:

```json
["A2 G7: backticked identifier(s) YFM occur in neither the cited line nor the committed snapshot"]
```

The frozen r61 `action_conjunct` returns `[]` for the same cell/page. The successor
returns `[]` for the original Action and for the otherwise identical expanded
abbreviation with its backticks removed. Thus the observed difference is caused
by formatting the descriptive abbreviation as a code span, not by changing the
stated behavior. This is an arm-level measurement; no mutated full-tree CLI
verdict or new backed-row total is claimed.

The Appendix A command computes identical content-word sets for these variants,
forward support `11` with required minimum `8`, reverse support `11` with required
minimum `5`, and `page_missing=[]`. Its raw substring checks return
`YFM_in_raw_line=False YFM_in_raw_page=False`. The other A2 conjuncts are therefore
not the source of rejection; the separate direct G7 call returns the same reason.

## Why this is over-strong for the r61 A2 contract

Contract evidence, opened before the probe:

- `/home/vgpnk/Projects/shokunin/kotoba-shokunin/plans/round-61.md:30-31`:
  “every load/event claim in the Action cell must be supported by text on the
  committed snapshot page (not vocabulary matching alone).”
- Its E2f addendum at `:241-254` makes G7 a **raw load/event claim** guard, explicitly
  says not to demand all words on one line for **non-claim cells**, and explicitly
  excludes `apply` from the claim-verb set to preserve the Claude Code positive.
  It requires raw tokenization so backticks cannot hide an actual event claim.
- `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-61/wave/MutA2.md:214-224`
  distinguishes legitimate paraphrases from invented event claims, and explains
  why raw claim detection is necessary. That report is evidence, not an alternate
  contract or an instruction source.

The counterexample introduces no raw load/event claim. Its expanded descriptive
abbreviation cannot turn `apply` into an event trigger. The contract does not
state that every code span in a non-claim Action must be the vendor's exact
identifier spelling.

Implementation evidence:
`/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules_v31.py:405,1046-1058,1088`.
The identifier regex is `` `([A-Za-z_][A-Za-z0-9_]*)` ``. G7 tests every match for
literal substring presence in the raw line/page; `action_conjunct` calls it after
the support fractions with **no raw load/event-claim precondition**. It does not
inspect whether the token is an API/event name or an explicitly expanded label.
The committed-source SHA-256 in Appendix A is
`a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858`.

Calling all such code spans exact vendor identifiers would add a new authoring
restriction, not establish the meaning of the frozen semantic-action contract.
The baseline/plain-abbreviation pair is the strongest local control: the
successor already accepts the same meaning, and all measured semantic support
inputs are unchanged.

## Predicate reruns and source reopening

Both commands in the landed successor receipt
`/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-62/C1-v31-successor.txt`
were rerun with the assigned committed successor in a revision-pinned sandbox
under `/tmp`, with every command limited to 120 seconds. Exact commands, complete
outputs and exit codes are in Appendices B and C:

- Self-test: `worlds reject 7 of 7; eligible rows pass 4 of 4`,
  `survivors closed 5 of 6`, `self-test: 0 failure(s) over 201 assertions`, exit `0`.
- The receipt's `--rev 43fe01804708d65e53965b4be31e9dc7dce793e4 --fetch`:
  `scoped rule files backed on committed snapshots 4 of 4; found on the live page 4 of 4`,
  exit `0`.

These measured finite positive sets pass; they do **not** cover the legitimate
expanded-abbreviation cell. Their success does not refute the false positive.

S118 was reopened at [the vendor memory reference](https://code.claude.com/docs/en/memory.md)
using the static reader, and its registry row was read in full at
`/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md:129`.
The same scoped-rules sentence was inspected in
`/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-62/snapshots/S118.page:194`,
along with its rule-frontmatter reference at `:244-250`. The live reader still
states that rules can be scoped using YAML frontmatter and the `paths` field,
and that `paths` accepts a YAML list or comma-separated string. This is a semantic
reopening, **not** a new raw-fetch digest or an assertion that the live response
matches the recorded snapshot bytes. The executable counterexample deliberately
uses the committed r61 page required by the eligible row.

## Impacted axes and smallest safe correction

- **Depth:** the newly implemented arm does not preserve the semantic distinction
  between unsupported event claims and legitimate non-claim paraphrases. It
  substitutes literal code-span membership for the frozen event-claim condition.
- **Consistency/calibration:** the gate disagrees on equivalent supported actions
  based on backtick formatting. Reporting only the unchanged original positives
  as a general no-harm result would overstate the measured acceptance surface.

This is a **fixable predicate defect**, not evidence that C1's separate absorption
matrix counting command failed. The round-62 plan's E1 amendment at `:265-270`
explicitly moves this successor out of C1's counted predicate. No round admission,
axis score, canonical Rust judgment, or formal verdict is issued here. If the
unconditional literal restriction were deliberately retained, its false-rejection
cost must be presented as a tradeoff to that judge, not silently treated as no harm.

Smallest safe correction for the integrator: retain the existing A2 support
fractions, but activate the raw G7 load/event evidence guard only for an actual
raw load/event claim, honoring the frozen exclusion of `apply`. Do not impose
exact vendor-token membership on descriptive code spans in a non-claim action.
Add the expanded-abbreviation positive and its baseline/plain controls beside
the existing backticked-event negative. Keep detecting genuine event claims from
raw text, including code spans. Do **not** fix this with a `YFM` allowlist, by
stripping backticks before claim detection, or by deleting event validation.
This is a correction request, not an implemented or verified patch.

## Execution and write bounds

All product bytes used in the counterexample were loaded through `git show` at
the assigned revision. Source paths in the transcripts are absolute. No lane
product, frozen verifier, corpus, index, sibling file, fleet file, or `.ufo/state`
was changed. Only this assigned report is written. No subagent, model call,
canonical judgment runtime, tool installation/update, or pacman transaction was
invoked. No installation record is needed because nothing was installed.

An initial **unpinned sandbox setup check failed**: the concurrent lane HEAD had
advanced to `3f911504ce76d9ca186f297d6d4a9cd8ed77508a`; the Eval cell stopped with
`RuntimeError: Sandbox does not match the assigned commit` and exit `1`, before
any counter ran from that clone. Setup was then corrected with
`git clone --revision=e6da78bbe420722dd18a13182a7c4b64ce02f005` into a different
sandbox. Appendix D preserves both setup transcripts. No check from the wrong
revision is counted. The temporary sandbox trees were removed after capturing
the inline evidence; no report evidence depends on their continued existence.

## Appendix A — committed-byte false-positive probe

This subprocess does not write files or alter guard functions. It imports the
committed modules under non-main names and calls the actual action/G7 functions.

```sh
python3 -B -c 'import hashlib, json, subprocess, sys, types
lane = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
rev = "e6da78bbe420722dd18a13182a7c4b64ce02f005"
def get(path):
    cmd = ["git", "-C", lane, "show", rev + ":" + path]
    p = subprocess.run(cmd, capture_output=True, timeout=120)
    print("input_command=" + json.dumps(cmd) + " exit=" + str(p.returncode))
    p.check_returncode()
    print("input_sha256=" + hashlib.sha256(p.stdout).hexdigest() + " bytes=" + str(len(p.stdout)))
    return p.stdout
def load(name, path):
    blob = get(path)
    m = types.ModuleType(name)
    m.__file__ = lane + "/" + path
    sys.modules[name] = m
    exec(compile(blob, m.__file__, "exec"), m.__dict__)
    return m
old = load("g7_review_old", "verifiers/check_scoped_rules.py")
new = load("g7_review_new", "verifiers/check_scoped_rules_v31.py")
b = get(".ufo/waves/round-60/snapshots/S103.page")
page = b.decode("utf-8")
lines = page.splitlines()
base = "Scope rules to specific files using YAML frontmatter; apply only when matching specified patterns. (S103 :194)"
cell = "Scope rules to specific files using `YFM` (YAML frontmatter); apply only when matching specified patterns. (S103 :194)"
plain = cell.replace("`YFM`", "YFM")
w, lw = new.content_words(cell), new.content_words(lines[193])
print("page_line_194_bytes=" + repr(b.splitlines(keepends=True)[193]))
for label, value in [("baseline_cell_bytes", base.encode()), ("abbreviation_cell_bytes", cell.encode()), ("plain_abbreviation_cell_bytes", plain.encode())]:
    print(label + "=" + repr(value))
print("W=" + json.dumps(sorted(w)))
print("L=" + json.dumps(sorted(lw)))
print("content_words_unchanged=" + str(w == new.content_words(base) == new.content_words(plain)))
print("forward_covered=" + str(new.covered(w, lw)) + " need=" + str(new.fwd_need(len(w))))
print("reverse_covered=" + str(new.covered(lw, w)) + " need=" + str(new.rev_need(len(lw))))
print("page_missing=" + json.dumps(sorted(x for x in w if not new.supported(x, new.page_words(page)))))
print("YFM_in_raw_line=" + str("YFM" in lines[193]) + " YFM_in_raw_page=" + str("YFM" in page))
print("frozen_abbreviation_reasons=" + json.dumps(old.action_conjunct(lines, cell, 194, page)))
print("v31_baseline_reasons=" + json.dumps(new.action_conjunct(lines, base, 194, page)))
print("v31_abbreviation_reasons=" + json.dumps(new.action_conjunct(lines, cell, 194, page)))
print("v31_plain_abbreviation_reasons=" + json.dumps(new.action_conjunct(lines, plain, 194, page)))
print("G7_abbreviation_reasons=" + json.dumps(new.g7_conjunct(lines, cell, 194, page)))
small = b.splitlines(keepends=True)[193]
small_page = small.decode("utf-8")
small_cell = cell.replace("(S103 :194)", "(S900 :1)")
print("minimal_page_bytes=" + repr(small))
print("minimal_cell_bytes=" + repr(small_cell.encode()))
print("minimal_frozen_reasons=" + json.dumps(old.action_conjunct(small_page.splitlines(), small_cell, 1, small_page)))
print("minimal_v31_reasons=" + json.dumps(new.action_conjunct(small_page.splitlines(), small_cell, 1, small_page)))
'
```
Working directory: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.

Exact stdout:

```text
input_command=["git", "-C", "/home/vgpnk/Projects/shokunin/kotoba-shokunin", "show", "e6da78bbe420722dd18a13182a7c4b64ce02f005:verifiers/check_scoped_rules.py"] exit=0
input_sha256=5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91 bytes=124987
input_command=["git", "-C", "/home/vgpnk/Projects/shokunin/kotoba-shokunin", "show", "e6da78bbe420722dd18a13182a7c4b64ce02f005:verifiers/check_scoped_rules_v31.py"] exit=0
input_sha256=a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858 bytes=132256
input_command=["git", "-C", "/home/vgpnk/Projects/shokunin/kotoba-shokunin", "show", "e6da78bbe420722dd18a13182a7c4b64ce02f005:.ufo/waves/round-60/snapshots/S103.page"] exit=0
input_sha256=82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7 bytes=54043
page_line_194_bytes=b'Rules can be scoped to specific files using YAML frontmatter with the `paths` field. These conditional rules only apply when Claude is working with files matching the specified patterns.\n'
baseline_cell_bytes=b'Scope rules to specific files using YAML frontmatter; apply only when matching specified patterns. (S103 :194)'
abbreviation_cell_bytes=b'Scope rules to specific files using `YFM` (YAML frontmatter); apply only when matching specified patterns. (S103 :194)'
plain_abbreviation_cell_bytes=b'Scope rules to specific files using YFM (YAML frontmatter); apply only when matching specified patterns. (S103 :194)'
W=["apply", "files", "frontmatter", "matching", "patterns", "rules", "scope", "specific", "specified", "using", "yaml"]
L=["apply", "claude", "conditional", "field", "files", "frontmatter", "matching", "patterns", "rules", "scoped", "specific", "specified", "using", "working", "yaml"]
content_words_unchanged=True
forward_covered=11 need=8
reverse_covered=11 need=5
page_missing=[]
YFM_in_raw_line=False YFM_in_raw_page=False
frozen_abbreviation_reasons=[]
v31_baseline_reasons=[]
v31_abbreviation_reasons=["A2 G7: backticked identifier(s) YFM occur in neither the cited line nor the committed snapshot"]
v31_plain_abbreviation_reasons=[]
G7_abbreviation_reasons=["A2 G7: backticked identifier(s) YFM occur in neither the cited line nor the committed snapshot"]
minimal_page_bytes=b'Rules can be scoped to specific files using YAML frontmatter with the `paths` field. These conditional rules only apply when Claude is working with files matching the specified patterns.\n'
minimal_cell_bytes=b'Scope rules to specific files using `YFM` (YAML frontmatter); apply only when matching specified patterns. (S900 :1)'
minimal_frozen_reasons=[]
minimal_v31_reasons=["A2 G7: backticked identifier(s) YFM occur in neither the cited line nor the committed snapshot"]
```

Stderr: empty.

Exit code: `0`.

## Appendix B — successor self-test rerun

Any shortened diagnostic strings below were emitted by the counter itself; the captured stdout is unabridged.

```sh
env TMPDIR=/tmp/kotoba62-g7-review-p4w6tntw/worlds python3 -B /tmp/kotoba62-g7-review-p4w6tntw/assigned/verifiers/check_scoped_rules_v31.py --self-test
```
Working directory: `/tmp/kotoba62-g7-review-p4w6tntw/assigned`.

Exact stdout:

```text
counter sha256 a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858
world W1: Claude Code reject=True arm=A4 line='entry row S900: A4: snapshot sha256 06277eb1ae94... is already recorded by base row S010 and the teaches cell declares no supersedes'
world W2: Claude Code reject=True arm=A3 line="entry row S900: A3: URL 'https://code.claude.com/docs/de/memory.md' is a rendering alias of the committed row S112 URL 'https://code.claude.com/docs/e"
world W3: Cursor reject=True arm=A1 line="entry row S903: A1: scope key 'rules' is not a canonical key for Cursor (canonical: globs); S903 URL 'https://cursor.com/docs/rules' is already a base"
world W4: Cursor reject=True arm=live line='live page: not found'
world W5: Claude Code reject=True arm=A1 line="entry row S900: A1: scope key 'patterns' is not a canonical key for Claude Code (canonical: paths)"
world W6: Claude Code reject=True arm=A2 line='entry row S900: snapshot .ufo/waves/round-60/snapshots/S900.page: A2: action cell supports 5 of its 8 content word(s) at line 6 (need >= 6)'
world W7: all reject=True arm=A1
world W0: exit=1
worlds reject 7 of 7; eligible rows pass 4 of 4
survivor e2c-wrong-supersedes-target: before accepted; after rejected
survivor e2c-supersedes-with-fresh-fetch: before accepted; after rejected
survivor e2e-negated-path-key: before accepted; after rejected
survivor e2e-commented-equals-key: before accepted; after rejected
survivor e2f-backticked-event-claim: before accepted; after rejected
survivor e2f-compound-purpose-outside-citation: before accepted; after accepted
survivors closed 5 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
bound: G9 remains unimplemented; e2f-compound-purpose-outside-citation survives per CriticC1Hollow.
self-test: 0 failure(s) over 201 assertions
```

Stderr: empty.

Exit code: `0`.

## Appendix C — landed live no-harm command rerun

```sh
python3 -B /tmp/kotoba62-g7-review-p4w6tntw/assigned/verifiers/check_scoped_rules_v31.py --rev 43fe01804708d65e53965b4be31e9dc7dce793e4 --fetch
```
Working directory: `/tmp/kotoba62-g7-review-p4w6tntw/assigned`.

Exact stdout:

```text
scoped rule files backed on committed snapshots 4 of 4; found on the live page 4 of 4
counter sha256 a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858; rev 43fe01804708d65e53965b4be31e9dc7dce793e4
canonical scope keys (S112/S113/S114/S115): Claude Code=paths; VS Code=applyTo; Copilot CLI=applyTo; Cursor=globs
reject Codex: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject Gemini CLI: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client
```

Stderr: empty.

Exit code: `0`.

## Appendix D — sandbox setup and revision guard

The first setup stopped at the failed assignment-revision guard described above. The second clone was explicitly revision-pinned.

```sh
git clone --quiet --shared --no-hardlinks /home/vgpnk/Projects/shokunin/kotoba-shokunin /tmp/kotoba62-g7-review-p4w6tntw/lane
```
Exact stdout:

```text
```

Stderr: empty.

Exit code: `0`.

```sh
git -C /tmp/kotoba62-g7-review-p4w6tntw/lane rev-parse HEAD
```
Exact stdout:

```text
3f911504ce76d9ca186f297d6d4a9cd8ed77508a
```

Stderr: empty.

Exit code: `0`.

```sh
git clone --quiet --shared --no-hardlinks --revision=e6da78bbe420722dd18a13182a7c4b64ce02f005 /home/vgpnk/Projects/shokunin/kotoba-shokunin /tmp/kotoba62-g7-review-p4w6tntw/assigned
```
Exact stdout:

```text
```

Exact stderr:

```text
Note: switching to 'e6da78bbe420722dd18a13182a7c4b64ce02f005'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

```

Exit code: `0`.

```sh
git -C /tmp/kotoba62-g7-review-p4w6tntw/assigned rev-parse HEAD
```
Exact stdout:

```text
e6da78bbe420722dd18a13182a7c4b64ce02f005
```

Stderr: empty.

Exit code: `0`.

