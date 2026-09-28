# Cold run — `verifiers/verify_corpus_integrity.py` — round 11

**NON-AUTHOR cold run.** The runner (lane `ColdRunRecord`) did **not** author
`verifiers/verify_corpus_integrity.py`, did not draft it, and had no part in
producing `verifiers/corpus-baseline.json`. Everything below was executed from
outside the repo (`cd /tmp`) against the worktree at HEAD `d49dfa54b6887de834477928cfa83fb50c3e2205`.

- Date: 2026-09-28 (coherent capture at 19:26:41-03:00; earlier agreeing capture ~19:24-03:00)
- Runner: `ColdRunRecord` (round-11 non-author cold-run lane)

## 1. Artifact identity (sha256 gate)

```
$ sha256sum <repo>/verifiers/verify_corpus_integrity.py
631569277d112e8effab3428ca89af53cbcf09f85ad5dad714827deefa2eb4aa  <repo>/verifiers/verify_corpus_integrity.py
```

Gate: **PASSED** — equals the round-11 brief's `631569277d112e8effab3428ca89af53cbcf09f85ad5dad714827deefa2eb4aa`; the artifact did not move, so the record stands.

Baseline identity: `verifiers/corpus-baseline.json` sha256
`bcbcfee1d8b66ef78fa24a5a52cd96654603c3a3c1f728601bb006d1f3da0e6e` — the DRAFT
recorded before the round-11 prose landed (per the round-11 brief it will be
re-recorded by L1; treat its numbers as provisional). I listed its compared keys
directly: `corpus.index.tracked_files`, `corpus.index.unindexed`,
`corpus.index.stale_patterns`, `corpus.index.missing_paths`,
`corpus.pointers.commit_total`, `corpus.pointers.commit_unresolvable`,
`corpus.pointers.commit_nonhash`, `corpus.pointers.report_dead`. It has **no
`corpus.pointers.report_total` key**, which is why that check reads
`expected=None` below — a provisional-baseline artifact, not a check failure.

Worktree note (matters for reading the numbers): the round-11 prose is
mid-landing. `git status --porcelain` during the capture window showed, besides
sibling prose edits: `?? corpus/knowledge/corpus-integrity-round11.md`,
`?? corpus/lessons/round-11.md`, `?? verifiers/verify_corpus_integrity.py`,
`?? verifiers/corpus-baseline.json` — the verifier and its baseline are
themselves untracked at this instant.

## 2. Cold run — exact commands, verbatim output, exit code

Capture discipline: the window was guarded — `md5sum corpus/README.md` plus
`git status --porcelain` hashed immediately before and after the run + all
spot-checks; identical (`GUARD: coherent`), so every number in §2–§3 is one
pinned instant: 2026-09-28T19:26:41-03:00.

### 2a. Plain mode

```
$ cd /tmp && sha256sum /home/vgpnk/projects/shokunin/kotoba-shokunin/verifiers/verify_corpus_integrity.py && git -C /home/vgpnk/projects/shokunin/kotoba-shokunin rev-parse HEAD && python3 /home/vgpnk/projects/shokunin/kotoba-shokunin/verifiers/verify_corpus_integrity.py --repo /home/vgpnk/projects/shokunin/kotoba-shokunin ; echo exit=$?
631569277d112e8effab3428ca89af53cbcf09f85ad5dad714827deefa2eb4aa  /home/vgpnk/projects/shokunin/kotoba-shokunin/verifiers/verify_corpus_integrity.py
d49dfa54b6887de834477928cfa83fb50c3e2205
corpus.index    tracked=33 unindexed=0 stale=2 missing=0  (36 FILE-column patterns over 33 md files)
corpus.pointers report_dead=1/20 commit_total=21 unresolvable=0 nonhash=0 (shapes [relative=0, absolute=19, tilde=1, bare=0], quoted-excluded=1, pointer-excluded=1; sites in --json)
           stale_patterns: corpus/README.md:35: knowledge/corpus-integrity-round11.md
           stale_patterns: corpus/README.md:40: lessons/round-11.md
           report_dead: corpus/README.md:40: /home/vgpnk/projects/shokunin/.ufo/reports/round-11/kotoba.md
           report_pointers_excluded: corpus/knowledge/dispatch-prompt-audit-round7.md:42: .ufo/reports/round-1/<lane>.md
           commit_quoted: corpus/lessons/round-6-aggregator-audit.md:45: round-N (quoted meta-finding)
DRIFT   corpus.index.stale_patterns: observed=2 expected=0 / empty
DRIFT   corpus.pointers.report_total: observed=20 expected=None
DRIFT   corpus.pointers.report_dead: observed=1 expected=0 / empty
6/9 checks pass; DRIFT: corpus.index.stale_patterns, corpus.pointers.report_total, corpus.pointers.report_dead
exit=1
```

### 2b. JSON mode

```
$ cd /tmp && python3 <repo>/verifiers/verify_corpus_integrity.py --repo <repo> --json ; echo exit=$?
```

`observed`: `tracked_files=33, index_patterns=36, unindexed=0, stale_patterns=2
(corpus/README.md:35 → knowledge/corpus-integrity-round11.md; corpus/README.md:40 →
lessons/round-11.md), missing_paths=0, report_total=20,
report_pointers_excluded=1, report_dead=1 (corpus/README.md:40:
/home/vgpnk/projects/shokunin/.ufo/reports/round-11/kotoba.md),
commit_total=21, commit_unresolvable=0, commit_nonhash=0,
commit_quoted_excluded=1, report_pointer_shapes={relative=0, absolute=19,
tilde=1, bare=0}, corpus_md_files=33`. `results`: 6 PASS, 3 DRIFT
(`corpus.index.stale_patterns`, `corpus.pointers.report_total`,
`corpus.pointers.report_dead`). `exit=1`. (Full JSON captured verbatim in the
runner transcript; every field is restated here.)

### 2c. Earlier capture (pre-round-11-landing tree, ~19:24-03:00)

Same command shape, run before the round-11 README rows landed; verbatim plain output:

```
corpus.index    tracked=33 unindexed=0 stale=0 missing=0  (32 FILE-column patterns over 33 md files)
corpus.pointers report_dead=0/19 commit_total=21 unresolvable=0 nonhash=0 (shapes [relative=0, absolute=18, tilde=1, bare=0], quoted-excluded=1, pointer-excluded=1; sites in --json)
           report_pointers_excluded: corpus/knowledge/dispatch-prompt-audit-round7.md:42: .ufo/reports/round-1/<lane>.md
           commit_quoted: corpus/lessons/round-6-aggregator-audit.md:45: round-N (quoted meta-finding)
DRIFT   corpus.pointers.report_total: observed=19 expected=None
8/9 checks pass; DRIFT: corpus.pointers.report_total
exit=1
```

This reproduces the author's recorded dispatch observations **exactly**
(`tracked=33 unindexed=0 stale=0 missing=0`; `report_dead=0/19`; shapes
`[relative=0, absolute=18, tilde=1, bare=0]`; `quoted-excluded=1`;
`pointer-excluded=1`). The delta to §2a is concurrent sibling edits landing the
round-11 prose between the two captures — tree movement, not a change in
verifier behavior.

## 3. Independent spot-checks (own commands, not the script's)

### (a) FILE-column pattern count and tracked-corpus-file count

```
$ git -C <repo> ls-files corpus/ | wc -l
33
$ awk -F'|' '/^\|/ { if (NF>=4 && $3 !~ /^[-:[:space:]]*$/) print $3 }' <repo>/corpus/README.md | grep -oP '`[^`]*`' | wc -l
36
```

Independent awk extraction of column 2 (File) of the coverage-map table yields
**36** backticked tokens vs the script's `index_patterns=36`; **33** tracked
corpus files vs `tracked_files=33`. AGREE.

### (b) Every checked report pointer resolves from its citing file's directory

Harvest (population per the script docstring: `.ufo/reports/round-N/*.md` in any
shape, excluding placeholder/glob/whitespace/ellipsis tokens), then resolve with
`test -e` — rooted forms as-is, `~` against `$HOME`, others from the citing
file's directory. Implemented in my own checker (quoted in §5; logic: grep-style
regex `(?<![\w.\-/])((?:/|~|(?:\.\.?/)*)[^\s`]*?\.ufo/reports/round-\d+/[^\s`]*\.md)`,
exclusion marks `<>*`/whitespace/`..`-after-leading-hops, `os.path.exists`).

```
pointers: raw=21 checked=20 dead=1 excluded=1
shapes: absolute=19 tilde=1 relative=0 bare=0
DEAD corpus/README.md:40: /home/vgpnk/projects/shokunin/.ufo/reports/round-11/kotoba.md
EXCLUDED corpus/knowledge/dispatch-prompt-audit-round7.md:42: .ufo/reports/round-1/<lane>.md
```

The one dead pointer confirmed by hand: `test -e` fails at both plausible roots —
the probe root named by the finding (the `$HOME` root's `reports/round-11/`)
held no `kotoba.md`, and its repo-root candidate
`<repo>/.ufo/reports/round-11/kotoba.md` is a placeholder form, excluded by
design. The other 19 pointers resolve. AGREE with `report_dead=1/20`, shapes, and
`pointer-excluded=1`. (The absent token was rewritten as prose at landing — a
live pointer to an absent path is exactly what this check must flag; see §7.)

### (c) Every commit citation (`commit <hex>`) resolves; count matches own regex count

Own regex `(?<![A-Za-z0-9_-])commit[ \t]+`([^`\n]+)`` over tracked corpus
`*.md`; a citation fully enclosed in double quotes on its line is a quoted
meta-finding (context); the rest must be 7–40 hex and resolve via
`git cat-file -e <tok>^{commit}`:

```
commits: raw=22 quoted_excluded=1 checked=21 nonhash=0 unresolvable=0
QUOTED corpus/lessons/round-6-aggregator-audit.md:45: round-N
```

Own regex count of checked citations = **21** = the script's `commit_total=21`;
all 21 pass `git cat-file -e <hex>^{commit}` (rc=0 each) =
`commit_unresolvable=0`; 0 non-hash = `commit_nonhash=0`; the single quoted
exclusion matches `commit_quoted: round-6-aggregator-audit.md:45: round-N`. AGREE.

## 4. Discrepancies

**none found** — between the verifier's claims and the three independent
spot-checks at the pinned instant there is no discrepancy; every DRIFT was
re-derived independently and is genuine current-tree state:

- `stale_patterns=2`: both tokens name files that exist on disk but are
  untracked (`git status --porcelain`: `??`), so they match no tracked file —
  correct detection of mid-landing prose, confirmed via `git ls-files corpus/ | grep -c round-11` → `0` plus `test -e` EXISTS on both paths.
- `report_dead=1`: the round-11 lane report has not been written yet (ABSENT at
  both roots, §3b) while README already advertises it — real, correctly flagged.
- `report_total` DRIFT (`observed=20 expected=None`): the draft baseline lacks
  the key (§1); provisional by design, to be re-recorded by L1.

Also none found in the sense of instrument authorship: the runner authored
neither script nor baseline, and the non-author path reproduced the author's
recorded verdict on the pre-edit tree (§2c) and correctly tracked the moving
tree afterwards.

## 5. Reproducibility

Scratch lives under `/tmp/round11/` (volatile — the directory was wiped at
19:22 per the round-11 disk-quota lesson and is being recreated per-author; the
checker below was written and executed *after* that wipe, 19:25–19:26). The
spot-check (b)/(c) implementation in full, so the check survives /tmp:

```python
# /tmp/round11/spot_checks.py — NON-AUTHOR independent implementation; shares
# no code with the verifier. Population definitions from the script docstring.
import os, re, subprocess
R = "/home/vgpnk/projects/shokunin/kotoba-shokunin"
tracked = [t for t in subprocess.run(["git","-C",R,"ls-files","corpus/"],
           capture_output=True,text=True,check=True).stdout.split() if t.endswith(".md")]
# (b)
PTR = re.compile(r"(?<![\w.\-/])((?:/|~|(?:\.\.?/)*)[^\s`]*?\.ufo/reports/round-\d+/[^\s`]*\.md)")
raw=[]; shapes={"absolute":0,"tilde":0,"relative":0,"bare":0}; exc=chk=dead=0
for f in tracked:
    for i,line in enumerate(open(os.path.join(R,f),encoding="utf-8"),1):
        for m in PTR.finditer(line): raw.append((f,i,m.group(1)))
for f,ln,tok in sorted(raw):
    if any(c in tok for c in "<>*") or any(c.isspace() for c in tok): exc+=1; continue
    if ".." in re.sub(r"^(?:\.{1,2}/)+","",tok).lstrip("/~"): exc+=1; continue
    chk+=1
    if   tok.startswith("/"):   shapes["absolute"]+=1; p=tok
    elif tok.startswith("~"):   shapes["tilde"]+=1;    p=os.path.expanduser(tok)
    else:
        shapes["relative" if tok.startswith(("./","../")) else "bare"]+=1
        p=os.path.join(R,os.path.dirname(f),tok)
    ok=os.path.exists(p); dead += 0 if ok else 1
    print(("OK   " if ok else "DEAD ")+f"{f}:{ln}: {tok}")
print(f"pointers: raw={len(raw)} checked={chk} dead={dead} excluded={exc}")
print("shapes: "+" ".join(f"{k}={v}" for k,v in shapes.items()))
# (c)
COMMIT = re.compile(r"(?<![A-Za-z0-9_-])commit[ \t]+`([^`\n]+)`")
HEX = re.compile(r"\A[0-9a-fA-F]{7,40}\Z")
raw=[]
for f in tracked:
    for i,line in enumerate(open(os.path.join(R,f),encoding="utf-8"),1):
        for m in COMMIT.finditer(line):
            raw.append((f,i,m.group(1),m.start(1),m.end(1),line.rstrip("\n")))
q=chk=nh=ur=0
for f,ln,tok,s,e,txt in sorted(raw,key=lambda x:(x[0],x[1])):
    if txt.count('"',0,s)%2==1 and '"' in txt[e:]: q+=1; print(f"QUOTED {f}:{ln}: {tok}"); continue
    chk+=1
    if not HEX.match(tok): nh+=1; continue
    if subprocess.run(["git","-C",R,"cat-file","-e",tok+"^{commit}"]).returncode: ur+=1
print(f"commits: raw={len(raw)} quoted_excluded={q} checked={chk} nonhash={nh} unresolvable={ur}")
```

Guard used around the capture (one pinned instant):

```bash
pre=$( (md5sum "$R/corpus/README.md"; git -C "$R" status --porcelain) | md5sum )
# ... cold run + spot-checks ...
post=$( (md5sum "$R/corpus/README.md"; git -C "$R" status --porcelain) | md5sum )
[ "$pre" = "$post" ] && echo "GUARD: coherent"   # → GUARD: coherent
```

## Verdict

COLD RUN: 1 / 9 checks — agrees with the author's recorded verdict (the
pre-edit capture reproduced the author's recorded dispatch observations exactly,
§2c; the three DRIFTs at the coherent capture are real, independently
re-derived round-11-mid-landing tree state, not verifier error; the only
`expected=None` DRIFT traces to the provisional draft baseline, which L1 will
re-record).

## 6. Re-gate after L1's comment-only edit

The shipped artifact moved after the §2 capture. Fresh pinned instant
2026-09-28T19:33:29-03:00, same guard as §2 (`md5sum corpus/README.md` +
`git status --porcelain` identical before/after — `GUARD: coherent`).

```
$ sha256sum <repo>/verifiers/verify_corpus_integrity.py
2f07179c07d19f96da822cea2d9cc945184ac94132cbcd05d9cd75169fc0f510  <repo>/verifiers/verify_corpus_integrity.py
```

Differs from the §1 gate value `631569277d…` — comment-only claim verified
independently, not taken on trust: (i) the changed line is visible as prose —
`verify_corpus_integrity.py:113` now reads `# the relative form alone: the
repair moved 9 README pointers to host-absolute,` (the corrected count; the
pre-edit file said 18); (ii) behavior pinned on the new sha:

```
$ cd /tmp && python3 <repo>/verifiers/verify_corpus_integrity.py --repo <repo> --no-baseline ; echo exit=$?
corpus.index    tracked=33 unindexed=0 stale=2 missing=0  (36 FILE-column patterns over 33 md files)
corpus.pointers report_dead=0/20 commit_total=21 unresolvable=0 nonhash=0 (shapes [relative=0, absolute=19, tilde=1, bare=0], quoted-excluded=1, pointer-excluded=1; sites in --json)
           stale_patterns: corpus/README.md:35: knowledge/corpus-integrity-round11.md
           stale_patterns: corpus/README.md:40: lessons/round-11.md
           report_pointers_excluded: corpus/knowledge/dispatch-prompt-audit-round7.md:42: .ufo/reports/round-1/<lane>.md
           commit_quoted: corpus/lessons/round-6-aggregator-audit.md:45: round-N (quoted meta-finding)
OBSERVE corpus.index.tracked_files: observed=33 expected=baseline
DRIFT   corpus.index.stale_patterns: observed=2 expected=0 / empty
OBSERVE corpus.pointers.report_total: observed=20 expected=baseline
OBSERVE corpus.pointers.commit_total: observed=21 expected=baseline
8/9 checks pass; DRIFT: corpus.index.stale_patterns
exit=1

$ cd /tmp && python3 <repo>/verifiers/verify_corpus_integrity.py --repo <repo> --self-test ; echo exit=$?
self-test: 0 failure(s) over 80 assertions
exit=0
```

Independent spot-checks re-run on the new sha, identical verdicts to §3:
(a) tracked=33, File-column tokens=36; (b) `pointers: raw=21 checked=20
dead=0 excluded=1`, shapes absolute=19/tilde=1/relative=0/bare=0; (c)
`commits: raw=22 quoted_excluded=1 checked=21 nonhash=0 unresolvable=0`,
single QUOTED `round-N`.

Numbers moved since §2a and why — only the tree moved, not the edit:
`report_dead` 1→0 because
`/home/vgpnk/projects/shokunin/.ufo/reports/round-11/kotoba.md` landed between
19:26 and 19:33 (confirmed `test -e` EXISTS at the repo `.ufo` root), so all 20
checked pointers now resolve; (the bare form as written in the capture was
re-presented at landing as the host-absolute path it names — round-12 landing
edit, see §7); everything else is byte-identical (33/36, stale=2
— the two round-11 corpus files are still untracked, 21/0/0 commits, quoted=1,
excluded=1). The `DRIFT`→`OBSERVE` relabeling on the equal checks is the
`--no-baseline` flag Main specified for this re-run, not a check change; the
lone remaining DRIFT (`stale_patterns=2`) is the baseline-independent
zero-violation for the still-untracked round-11 files and survives
`--no-baseline` by design.

COLD RUN (re-gate): 1 / 9 checks — agrees with the author's recorded verdict;
the comment-only edit is behavior-neutral on every observable surface
(self-test 80/80, all three spot-checks identical), and the sole delta traces
to tree movement.


## 7. Round-12 landing note (declared)

The round-11 landing was interrupted before its commit; the round-12 respawn
resolved the working tree. Two site classes were re-presented so the landed tree
passes the check this capture is about — presentation only, no number, command,
or exit code changed, and the shipped script is byte-identical to the §6 re-gate
sha256 (`2f07179c…`), so that gate still holds:

- §3(b): the reported-ABSENT token is now prose — the probe root and the missing
  file are named without a literal pointer. A live pointer to an absent path is
  exactly what this check must flag, so it cannot stay in the token class.
- §6: the bare form as captured is now the host-absolute path it names, so the
  "it landed" claim is also a resolving pointer.

Re-verified after the edits: `test -e` still ABSENT at the prose-named probe
root, EXISTS for the host-absolute path; the landing tree is green
(`corpus/lessons/round-11.md` carries the landed counts).
