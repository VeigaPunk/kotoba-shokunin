# SentWaveSpecs — wave evidence dir: secrets + context-bounds sentences (calibration axis)

Seat: sentinel, wave `kotoba-r65-w1`, 2026-10-24. Lane bounds respected: read-only on
the lane/fleet tree and on lane Git/jj state (only `git show` / `git ls-files` /
`git status` reads); all scratch under `/tmp`; no subagent dispatch.

Assigned surface only: (A) no secrets under `.ufo/waves/round-65`, (B) the prepared
wave contexts carry the absolute-path bounds sentence, (C) `grep -c 'Kill only by the
PIDs you started'` = 1 per context. Everything else here is labelled as an adjacent
observation, not a judgment.

## Verdicts

| # | Check | Verdict | Severity |
|---|---|---|---|
| A | No secrets in `.ufo/waves/round-65` | **PASS** — zero credential hits across 14 classes, 28 files + PDF/txt snapshot | none |
| B | Contexts carry the absolute-path bounds sentence | **PASS on presence** (1 per context, byte-identical in w1/w2) — **MEDIUM gap** in operability: 16 prompts route through bare lane-relative tokens while the seat's ambient cwd is the fleet root, where `LOG.md`/`SCORECARD.md`/`.ufo/watchdog.log` exist as *different* documents | medium |
| C | Q44 kill-cap sentence = 1 per context | **PASS on the shared-context reading** (1/1 in both waves); **2** in the assembled payload of the two seats that quote the rule (w1 #23, w2 #28); the counting command itself is line-based and self-referential | low–medium (calibration) |

Nothing in this seat falsifies C1 or C2's counted predicates. It does falsify the
implicit claim that the Q44 sentence is a single-valued, self-checking invariant.

## A. Secrets sweep — PASS

Scope at sweep time: the dir grew from 25 files (03:15) to 28 (04:36–04:38, sibling
reports) while this seat read it; the sweep covers all 28 files, including
`.ufo/waves/round-65/w1/{ScoutS121Reopen,ScoutS049Recheck,ScoutLessonBacklog}.md`.

```
$ find .ufo/waves/round-65 -type f | wc -l
28
$ find .ufo/waves/round-65 -name '.*' -o -perm -o+w -o -perm -4000
(no output)                      # no dotfiles, no world-writable, no setuid
$ find .ufo/waves/round-65 -type l -ls
(no output)                      # no symlinks -> no path escape into $HOME
$ stat -c '%s %n' .ufo/waves/round-65/w{1,2}-dispatch.err
0 .ufo/waves/round-65/w1-dispatch.err
0 .ufo/waves/round-65/w2-dispatch.err
```

Credential sweep (python, 14 classes; exit 0). Classes: AWS `AKIA/ASIA`, GitHub
`gh[pousr]_`/`github_pat_`, `sk-`, Slack `xox[baprs]-`, PEM private key, `Bearer`,
JWT triple, `password|secret|api_key|access_token|client_secret|auth_token|private_key|
passphrase` `[:=]` assignments, `~/.ssh|id_rsa|id_ed25519|.netrc|.aws/credentials|
.config/gh/hosts|/etc/shadow`, URL userinfo (`scheme://user:pass@`), npm
`_authToken`, `pypi-`, env-dump lines (`^[A-Z][A-Z0-9_]{2,}=…`).

```
classes hit: NONE
```

Secondary high-entropy scan (len ≥ 24, H > 4.35, must contain alpha+digit): 28 flags,
every one a *path* (e.g. `…/.ufo/waves/round-65/w1/SentWaveSpecs.md`) — no unlabeled
secret. The only 64-hex tokens in the dir are the receipt shas (expected).

Snapshot artifact (`snapshots/S121.pdf`, 1,126,684 B,
sha256 `bad1b681b1d6d6cea09f0c1e4701618b88dc175b713689c2a6ac43aba07418a3` — matches the
plan's anchor cell) checked for active/embedded content:

```
/JavaScript 0  /OpenAction 0  /AA 0  /Launch 0  /EmbeddedFile 0
/URI 0         /RichMedia 0   /XFA 0 /AcroForm 0  /SubmitForm 0
/ImportData 0  /GoToR 0       /Annots 0  /Encrypt 0
/JS 1  -> offset 887182, context b"\x8f\xd0p\xdc\xeb\xd8 ... \xc6\xb8\n\x16/JS\xe6w\x9d..."
metadata: Title / Subject / Keywords / Creator "LaTeX with hyperref package" / Producer "pdfTeX-1.40.14"
```

[INFERENCE] The lone `/JS` byte pair sits inside a FlateDecode stream among random
non-ASCII bytes and is not a PDF name object — corroborated by `/OpenAction`,
`/AA`, `/AcroForm`, `/Annots` all being 0. No execution path from the snapshot.

Exposure checks: the real hostname (`plazir27`) appears in no wave file
(`grep -rl plazir27 …` → rc=1); the only e-mail in the whole tree is the paper's public
corresponding-author address inside `snapshots/S121.txt`
(`lech.madeyski@pwr.wroc.pl`) — artifact data, not fleet credential material. Every
absolute path in the tree is either the lane root or `/home/vgpnk/.omp/agent/RULES.md`:

```
$ grep -rhoE '/(home|root|etc|srv|opt|var|mnt|media)/[A-Za-z0-9._/-]+' .ufo/waves/round-65 \
    --exclude='S121.pdf' | sort | uniq -c | awk '$2 !~ /kotoba-shokunin/'
      4 /home/vgpnk/.omp/agent/RULES.md
```

All 25 prepared artifacts are tracked at HEAD (`git ls-files .ufo/waves/round-65 | wc -l`
→ 25 at 03:15; sibling reports are the untracked additions). Nothing secret was
committed, and nothing can leak through an untracked file here that the sweep missed.

## B. Absolute-path bounds sentence — present, but not self-enforcing

The `# Write bounds` paragraph is byte-identical in both contexts:

```
$ python3 -c "import json;[print(p, json.load(open(p))['context'].count('Read-only outside your own report file')) for p in ('.ufo/waves/round-65/w1-spec.json','.ufo/waves/round-65/w2-spec.json')]"
.ufo/waves/round-65/w1-spec.json 1
.ufo/waves/round-65/w2-spec.json 1
rc=0
```

Verbatim (both waves, identical):

> Read-only outside your own report file — the landed bytes are the attack surface; never
> mutate the fleet repo, sibling lanes, lane jj state or the lane Git index; never run
> git/jj writes. All paths absolute under /home/vgpnk/Projects/shokunin/kotoba-shokunin.
> Scratch work only under /tmp. Kill only by the PIDs you started; cap any contention at
> 4 processes and 120 s.

It carries all three clauses (read-only scope, no git/jj writes, absolute-path + `/tmp`
scratch), and the report clause is coherent: the context maps the relative
`Report:` trailer (`Report: write your scoped findings to .ufo/waves/round-65/w1/<Name>.md`,
shape verified identical for all 64 seats) onto the absolute lane path.

**Falsifier — the operative instructions contradict the sentence.** 16 of 64 task prompts
route reads through bare lane-relative tokens, and no prompt supplies a cwd:

```
w1: 11 of 32 prompts carry relative tokens (14 tokens)
    ScoutQualityDebt3  LOG.md, corpus-idx, corpus_integrity
    ConnSibling2       corpus/knowledge/g7-span-closure-round65.md, corpus/lessons/round-65.md
    ExecKillReverify   verifiers/check_scoped_rules_v32.py
    ExecGovProbe       verifiers/verify_skill_checklist.py
    ScribeEntryCheck   corpus/knowledge/g7-span-closure-round65.md
    ScribeLessonCheck  corpus/lessons/round-65.md
    … (+5)
w2: 5 of 32 prompts carry relative tokens
    MutW2GovLanes      LOG.md
    ScoutW2AppendOnly  LOG.md/SCORECARD.md/corpus/
    RevW2EntryTruth    corpus/knowledge/g7-span-closure-round65.md
    RevW2Plan          plans/round-65.md
    ScoutW2State       .ufo/watchdog.log
context itself: .ufo/waves/round-64/w2/MutW2M7M22.md, .ufo/waves/round-65/receipts/C1-close-measure.txt,
                corpus/knowledge/g7-span-closure-round65.md, corpus/lessons/round-65.md
```

This seat's own shell cwd is `/home/vgpnk/Projects/shokunin` (the **fleet** root), and the
dispatch template contains no `cwd` field (`grep -o '"cwd"[^,]*' w1-dispatch.json` → no
match). Resolution at that root:

```
$ cd /home/vgpnk/Projects/shokunin
LOG.md           EXISTS (regular file 99844)        lane: 540335 B  sha 0f665b6e…  <- DIFFERENT DOCUMENT
SCORECARD.md     EXISTS (regular file 73649)        lane: 189808 B  sha 839dd685…  <- DIFFERENT DOCUMENT
.ufo/watchdog.log EXISTS (regular file 110240)      lane: ABSENT (ls: No such file or directory)
scripts          EXISTS (directory)                 corpus/ plans/ verifiers/  -> absent (read fails loudly)
$ ls -ld /home/vgpnk/Projects/shokunin/.ufo/waves/round-65
ls: cannot access '/home/vgpnk/Projects/shokunin/.ufo/waves/round-65': No such file or directory
```

Exploit path (no malice required, just following the prompt):
`ScoutW2State` is told to read `.ufo/watchdog.log`; that file is absent in the lane and
present at the fleet root, so the seat silently audits a *different* 110 KB log and can
report PASS/FAIL on bytes the lane does not contain. Same class for `MutW2GovLanes` /
`ScribeScorecardCheck` / `ScoutW2AppendOnly` (`LOG.md`, `SCORECARD.md` differ in size and
sha). Relative `Report:` writes would target
`/home/vgpnk/Projects/shokunin/.ufo/waves/round-65/w1/` — which does not exist — i.e. a
write outside the lane repo; the absolute report path in the context is the only thing
preventing it.

Impact: silent wrong-file evidence (contamination that reads as a clean PASS), not lane
mutation. Smallest remediation: one sentence appended to the bounds paragraph — "Resolve
every path below against the lane root; the shell cwd is not the lane root" — or prefix
the 16 tokens with `/home/vgpnk/Projects/shokunin/kotoba-shokunin/`.

## C. Q44 kill-cap sentence — 1 per context, 2 per judged seat

Per shared `context` field (the reading the criterion can actually enforce):

```
$ python3 -c "import json;[print(p,'kill =',json.load(open(p))['context'].count('Kill only by the PIDs you started')) for p in ('.ufo/waves/round-65/w1-spec.json','.ufo/waves/round-65/w2-spec.json')]"
.ufo/waves/round-65/w1-spec.json kill = 1
.ufo/waves/round-65/w2-spec.json kill = 1
rc=0
```

Contexts are byte-identical to the dispatch payloads after JSON load
(`w1: True, w2: True`), and all 32 prompt/name pairs match their rendered tasks by name
with the expected `context + /skill:godspeed + Lane bounds + Report:` template.

Flat-file `grep -c` returns **2** in all four files, because the sentence is quoted as
the judged subject inside the judge's own prompt:

```
$ grep -n 'Kill only by the PIDs you started' w1-spec.json w2-spec.json w1-dispatch.json w2-dispatch.json
w1-spec.json:11      "context": "… Kill only by the PIDs you started; cap any contention …"
w1-spec.json:203       "prompt": "Verify … (grep -c 'Kill only by the PIDs you started' = 1 per context)."
w2-spec.json:12      "context": "…"
w2-spec.json:244       "prompt": "Check … (grep -c 'Kill only by the PIDs you started' on each spec context = 1) …"
w1-dispatch.json:357 "context": "…"        w1-dispatch.json:477 "task": "/skill:godspeed\n\nVerify …"
w2-dispatch.json:357 "context": "…"        w2-dispatch.json:502 "task": "/skill:godspeed\n\nCheck …"
```

Per-seat assembled payload (`context + task`, what a dispatched seat actually receives):

```
w1-dispatch.json: seats with assembled kill != 1: [('SentWaveSpecs', 2)]
w2-dispatch.json: seats with assembled kill != 1: [('ConnW2Fleet2', 2)]
```

i.e. 62 of 64 seats see exactly 1; the two sentinel/connector seats told to *verify* the
rule see 2 — the counting subject contains its own counter. The bounds sentence has no
such duplication (0 occurrences in any task; assembled count 1 for all 64).

The command itself is line-based, so it can pass vacuously on a compact serialization of
the same content (`grep -c` counts lines; `grep -o` counts occurrences):

```
$ python3 (dumps the same w1 spec to /tmp, indent=2 vs separators=(',',':'))
/tmp/pretty-spec.json  grep -c lines = 2 | grep -o occurrences = 2
/tmp/compact-spec.json grep -c lines = 1 | grep -o occurrences = 2
```

So the acceptance criterion is unsound in both directions: it fails a compliant shared
context when run on the flat file (2), and it can pass a duplicated context once a
producer compacts the JSON (1 with 2 occurrences). Correct instrument: count per field
(`json … ['context'].count(S)`) or `grep -o … | wc -l`.

Convention drift across rounds (flat `grep -c` per spec file): round-62 = 1, round-63 = 0,
round-64 = 0, round-65 = 2 (the per-task quote is new this round). Round-66/w1-spec = 0 —
noted only because it is the same predicate on the live sibling wave; out of this seat's
judged surface and not judged here.

## Adjacent observation (not judged): the harness the seats re-run contradicts the cap

`receipts/kill_battery.py` is the artifact W2 seats are told to re-run, so its own
boundedness matters to the Q44 sentence:

```
$ grep -n 'timeout=' .ufo/waves/round-65/receipts/kill_battery.py
71:  cwd=TREE, capture_output=True, text=True, timeout=180)
$ head -3 .ufo/waves/round-65/receipts/kill_battery.py
# Usage: git archive <rev> | tar -x -C /tmp/tree && cd /tmp/tree && python3 kill_battery.py
$ grep -n '^TREE\|^CAND' .ufo/waves/round-65/receipts/kill_battery.py
13:TREE = Path('/tmp/r65work/tree')
14:CAND = TREE / 'check_scoped_rules_v32.py'
```

- `timeout=180` exceeds the 120 s contention cap the same context imposes.
- The documented usage extracts to `/tmp/tree`, the constant reads `/tmp/r65work/tree`;
  and `CAND` (tree *root*) is not producible by `git archive` at any rev — the root copy
  is untracked (`git ls-tree 80bb8921 | grep check_scoped` → 0 root entries). A fresh
  extraction per the comment therefore crashes (clean) or, if `/tmp/r65work/tree`
  survives, silently measures **stale bytes**.
- Provenance is currently honest, so this is a latent hazard, not a false receipt:
  the tree copy sha `b6cfc764…` equals `git show {80bb8921,0e104f49,5253b281}:verifiers/check_scoped_rules_v32.py`,
  and that copy prints `self-test: 0 failure(s) over 234 assertions`, matching
  `C1-close-kill.txt`. Script body is bounded (`subprocess.run`, `cwd=TREE`, restores
  `CAND` in `finally`); no network, no `eval`, no `rm`, no `os.system`.

Smallest remediation: derive `TREE` from the extraction path, assert the extracted blob
sha against the claimed rev before running, set `timeout=120`, drop the root-copy path.

Reproducibility note for W2 "re-run every count at tip+base" seats: HEAD has advanced to
round 66 (`git log -1` → `2a8eba5 round-66 verifier spot-check`), and the live
`verifiers/check_scoped_rules_v32.py` is `97d89716…` at **240** assertions, while the
round-65 pin is `b6cfc764…` at **234** @ `80bb8921`. Re-running in the working tree
returns 240 and will read as a C1 mismatch unless the seat uses `git show <rev>:…`. This
is round-66 drift, not a round-65 defect.

## Claims supported / falsified

- **Supports:** "the wave evidence dir contains no secrets" (A, PASS, 28 files, 14
  classes, PDF structurally inert); "each prepared context carries the bounded-scope and
  Q44 sentences" (B, C on the shared-context reading, 1/1 in both waves).
- **Falsifies:** the unstated assumption that `grep -c 'Kill only by the PIDs you started'`
  is a well-defined 1-per-context predicate — on these bytes it yields 2 (flat file and
  assembled seat payload) and 1 vacuously under compaction; the assumption that the
  absolute-path bounds sentence makes the payload path-safe — 16 prompts still resolve
  against an ambient fleet-root cwd where three same-named documents differ or exist only
  there.

## Gaps / residual unknowns

- [INFERENCE] That dispatched seats inherit this session's cwd (`/home/vgpnk/Projects/shokunin`)
  rather than a lane cwd: inferred from this seat's own environment plus the dispatch
  having no `cwd` field; the host mapping is not otherwise observable from the artifacts.
- The dir is live (25 → 28 files during the sweep); verdict A is timestamped at
  2026-10-24 04:38 -03 and does not cover reports written after it.
- Round-66's wave spec was not audited beyond the one count above (out of judged surface).

## Tooling

No installs or upgrades this seat (python3, grep, stat, sha256sum all pre-installed;
pacman pause respected).
