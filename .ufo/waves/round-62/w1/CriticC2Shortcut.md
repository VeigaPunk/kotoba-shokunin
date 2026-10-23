# CriticC2Shortcut — C2 shortcut attack

Seat: `KotobaR62.CriticC2Shortcut`. Assigned axis: **calibration** (consistency sub-axis).

## Result

**A D/H-name lookup reproduces all four numbers without reading any repair bytes.** A constant transcript printer also reproduces the self-test line and both revision CLI observations. These are counterexamples to treating the printed signature as sufficient evidence, **not** evidence that they satisfy the full frozen contract: the plan already forbids asserted rather than blob-computed D/H scores (`plans/round-62.md:150-152`). An independent control must enforce that clause; another success message printed by the candidate itself does not enforce it.

The other requested shortcuts do not reproduce the signature when their scores are actually evaluated:

| Built shortcut | Dishonest rejected /6 | Honest passed /2 | Base /6 | Tip /6 |
|---|---:|---:|---:|---:|
| Constant score 6 | 0 | 2 | 6 | 6 |
| D/H-name lookup | **6** | **2** | **0** | **6** |
| Import frozen `check_repairs` unchanged | 0 | 1 | 0 | 6 |
| Reject every tree | 6 | 0 | 0 | 0 |
| Independent minimal hardening reference | **6** | **2** | **0** | **6** |

**H1 and the pinned dispatch tip both score 6/6 under the minimal hardened forms tested here.** H1 scores 4/6 under the frozen checker, as required. This is a measured independent reference, **not a claim about the eventual integrated v2**. No `check_routed_repairs_v2.py` or published `ExecSuccessorC2.md` draft was available at discovery; neither the integrated successor nor the eventual round-62 data revision was measured.

**D1's count basis is stable:** the actual round-60 close, the declared base, and the dispatch tip contain the identical build subtree `b5602fbf5401390f760228a605670cde076f4d41`. All have 33 entries, 30 Markdown files, but **29 names matching the frozen seat-report regex**. D1 must add an actual matching report name to obtain 30; counting the existing Markdown fixture is not a valid D1.

No judgment/admission/axis re-score was performed. No lane implementation was edited. The only lane write is this report. No git/jj mutation, dispatch, installation, or fleet/sibling/state/index write was performed. Experiments used in-memory synthetic tree data and scratch Python source; scratch is untrusted and is not cited as evidence. The evidence is the inline command output below.

## 1. Contract and local evidence

Read first: `plans/round-62.md`, especially C2 lines 109–152. Relevant local sources:

- `verifiers/check_routed_repairs.py:71-119`: frozen substring/co-occurrence scoring; `:142-158`: revision CLI blob inputs and exit rule.
- `.ufo/waves/round-61/wave/ExecC2Audit.md:251-277`: the `exit=0` and adjacent-line false negatives; `:331-362`: 29 seat reports versus 30 Markdown files; `:366-445`: proposed hardened forms.
- `LOG.md:2540-2542`: actual asserted correction, landed-scope line, and correctly directed base pointer.
- `.ufo/waves/round-61/census-after.txt:1-17`: real census body and `exit=0`.
- `.ufo/waves/round-61/receipts/controls-ancestry.txt:10-21`: commented command prompt followed by that command's exit, distinct full hashes.
- `corpus/QUALITY.md:67`: literal-equality Q56 criterion.
- `corpus/lessons/round-60-verifier-spotcheck.md:6-7,117-124`: round-60 close identity and the routed count/pointer defects.

Pinned measurement revisions:

```text
r60 close  79cf263800552812ce6a45f4bb0313668b576749
declared base f3246d1493b60ea1c0d947a19c39f9e08e92f326
dispatch tip 45a7ecfac9e203297f3146c45d63f5e79367470c
```

The frozen repairs checker SHA-256 is `95ade9be1ed1930266bce4b98c8c593fff1feba89e2cf25763f0aa83f206cb88`. The experiment imported its **committed bytes at the dispatch revision**, verified this hash, and used its unchanged `check_repairs`. It also checked that the working-tree file used for the real-revision CLI runs had the same hash. Neither frozen counter was modified; the scoped-rules counter was not run or changed.

### Exact fixture construction

All D/H fixtures start from the dispatch tip's five real input blobs and its `git ls-tree` build listing; the complete builder source is included below. No synthetic fixture was committed.

| Tree | Only relevant change from the tip | Frozen | Reference | Failing reference arm |
|---|---|---:|---:|---|
| D1 | Add `build/CriticShortcut62.md` with a body, preserving the LOG's `committed 29`: derived count becomes 30 | 6 | 5 | R-a |
| D2 | Replace R-a with an explicitly negated correction, retaining the exact frozen `claimed 32` marker | 6 | 5 | R-a |
| D3 | Replace R-c with `base measurement is C1-measure.txt, not receipts/freeze2-selftest.txt` | 6 | 5 | R-c |
| D4 | Census is just `exit=0\n` | 6 | 5 | R-d |
| D5 | Replace exact Q56/M91 ids with Q560/M910 | 6 | 5 | R-e |
| D6 | `exit 0` belongs to `git rev-parse`; malformed merge-base operands have their own `exit=1` | 6 | 5 | R-f |
| H1 | Split the actual R-c at `, NOT in`; replace **all** ancestry `exit 0` spellings with `exit=0` | 4 | 6 | None |
| H2 | Unchanged dispatch tip | 6 | 6 | None |

D2 detail: literal `did not claim 32` alone does **not** contain frozen marker `claimed 32`. The measured D2 includes `it is false that they claimed 32`, so it really meets the required frozen-before score. This avoids accidentally testing a tree already rejected by the old checker.

H1 detail: replacing only the merge-base exit is insufficient to reproduce frozen 4/6: the real ancestry receipt has other `exit 0` tokens, including a commented distinctness-test result. All were changed to the honest equals spelling; otherwise the frozen R-f substring can remain satisfied by an unrelated exit.

## 2. Counterexample and smallest safe correction

### F1 — identity leakage / candidate-owned proof (fixable defect)

The name shortcut is exactly:

```python
if name in {"D1", "D2", "D3", "D4", "D5", "D6", "base"}:
    return 0
return 6 if name in {"H1", "H2", "tip"} else 0
```

It has the complete numerical signature. It then rejects a byte-identical honest H1 renamed D1, and accepts a byte-identical stale-count D1 renamed H1. An opaque name shared by two newly generated payloads also exposes it: the honest payload should pass and the stale-count payload should fail, but the shortcut returns the same answer for both.

The constant transcript script reads zero blobs. It prints the exact success line under `--self-test`, returns `0 of 6`, exit 1 for the declared base hash, and `6 of 6`, exit 0 for other revisions. The printed/CLI observations alone cannot distinguish it from an implementation that performed the work. The full plan's computation requirement rules this out; this report does not waive that requirement or alter the frozen predicate.

**Impacted axis:** calibration/consistency. Numeric success without a causal input test would falsely credit a repair measurement. This is a fixable evidence/control defect, not an unavoidable tradeoff.

**Smallest safe correction — draft only, exact implementation target `verifiers/check_routed_repairs_v2.py`:**

1. The common scoring function receives only the blob map and the tree-listing input (`check_repairs(blobs, build_paths)`), **not** a fixture name, revision, or expected score. The CLI resolves a revision to these bytes outside the scorer. All six arm booleans and the sum are returned from actual checks; the D/H totals and final line are computed from those returns. The self-test independently invokes the frozen imported scorer on each D fixture and H1, rather than asserting its before-scores.
2. Add the identity-cross controls measured here: H1 bytes under D1's name must still pass; D1 bytes under H1's name must still fail. Add a **fresh positive/negative pair not named in the plan**, sharing one newly generated opaque name: new benign LOG bytes with 29 counted reports, then the same payload plus one counted report while keeping `committed 29`. Expect 6 then <6. The fresh positive matters: an unknown-tree default-reject shortcut must not receive credit for rejecting only a fresh negative.
3. Exercise those controls **outside the candidate's own success transcript**, using the same scorer called by its CLI, and retain the command/output as a pre-data control receipt. An exact proposed receipt target is `.ufo/waves/round-62/controls/c2-shortcuts.txt`. The full measured independent harness below supplies the construction and assertions; no permanent second authority or alternate repair counter is proposed.
4. Split D6's two defects into extra unnamed arms: valid distinct full hashes with someone else's successful exit; equal full hashes with the merge-base command's own successful exit. A single doubly-bad D6 can be rejected by just one conjunct, concealing an unimplemented other conjunct. Both isolated arms measured frozen 6, reference 5 here.

The existing numerical signature stays unchanged. The independent guard counted 6, 4, 8, and 4 failures for constant-six, name-lookup, frozen-unchanged, and reject-all respectively; the reference had 0. Its arithmetic and controls are included in the full harness, not merely described.

### F2 — do not overstate the bounded repair (judgment reserved)

Passing these controls establishes the listed byte/listing predicates on these inputs. It does not authenticate that a receipt's command really ran, prove wall-clock dispatch order from commit ancestry, or prove general prose honesty. The reference deliberately implements the plan's small forms, not ExecC2Audit's strongest optional re-execution/provenance proposals. Claims extending to those properties need different evidence; whether a bounded calibration claim warrants a canonical Rust judgment is not decided by this seat. Fresh controls also are not a tamper-proof proof against an adversary allowed to rewrite the entire evaluator and its independent receipt.

## 3. Measurements — pasted output

Command (working directory is the seat's scratch directory):

```sh
python3 -B /fast/scratch/hyaku/kotoba-r62/CriticC2Shortcut/critic_c2_shortcuts.py
```

Date from `date -u`: **2026-10-23T20:53:43Z**. Experiment exit: **0**. Child commands and their exits are in the pasted output. Parent/child processes were sequential; no more than the harness, one child Python, and that child's git process were needed. The command deadline was 120 seconds; this run completed within the same UTC second. An earlier run without the additional fresh/D6-isolation controls ran at 20:52:30–20:52:31Z; the complete result below is the expanded experiment, not a fabricated replacement for a failing run.

```text
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-10-23T20:53:43Z
exit=0
$ /usr/bin/python3 --version
Python 3.14.8
exit=0
frozen sha256 95ade9be1ed1930266bce4b98c8c593fff1feba89e2cf25763f0aa83f206cb88

SYNTHETIC TREE SCORES (arm order R-a..R-f)
name derived frozen hardened arms payload-sha16
D1 30 6 5 011111 b6c8593bb7d693a0
D2 29 6 5 011111 33443f33e1def12d
D3 29 6 5 110111 ddec4f831688d7b3
D4 29 6 5 111011 a4ab0a6a11ab1b2f
D5 29 6 5 111101 5929b7d7d1177098
D6 29 6 5 111110 ca0bdc465defa08b
H1 29 4 6 111111 e16904fec7747fad
H2 29 6 6 111111 3b04d1ddf45f94fe
base 29 0 0 000000 15ca0c09c7185517
tip 29 6 6 111111 3b04d1ddf45f94fe

SHORTCUT SIGNATURES
scorer dishonest-rejected/6 honest-passed/2 base/6 tip/6 numeric-signature
constant-six 0 2 6 6 not-matched
D/H-name-lookup 6 2 0 6 MATCH
frozen-unchanged 0 1 0 6 not-matched
reject-every-tree 6 0 0 0 not-matched
reference-hardening 6 2 0 6 MATCH

UNNAMED / IDENTITY-CROSS CONTROLS
input payload-sha16 name-lookup hardened expected
unlisted-tree-7f18c9 e16904fec7747fad 0 6 6
unlisted-tree-7f18c9 b6c8593bb7d693a0 0 5 5
D1 e16904fec7747fad 0 6 6
H1 b6c8593bb7d693a0 6 5 5

FRESH BYTES, SAME UNPUBLISHED NAME
fresh-c920394472412f38 a6457a61359f87b5 0 6 6
fresh-c920394472412f38 3a0499a5b4f7e504 0 5 5

D6 CONJUNCTS SPLIT (valid hashes; no malformed-operand shortcut)
fresh-owned-exit-c920394472412f38 frozen 6 hardened 5
fresh-distinctness-c920394472412f38 frozen 6 hardened 5

INDEPENDENT GUARD RESULTS
constant-six guard-failures 6
D/H-name-lookup guard-failures 4
frozen-unchanged guard-failures 8
reject-every-tree guard-failures 4
reference-hardening guard-failures 0

H1 EXACT HOUSE-STYLE CHANGES
- R-c erratum: the r60 base measurement (base `31092dc6`, exit 1) is committed at `.ufo/waves/round-60/receipts/freeze2-selftest.txt`,
  NOT in `.ufo/waves/round-60/C1-measure.txt` (after-only, both runs at `7b80ae80`) — the r60 report's joint citation conflated them.
#   $ git merge-base --is-ancestor b4a8d2ee79a6190cf5ece5d11395544876e1fc8a 43fe01804708d65e53965b4be31e9dc7dce793e4
exit=0

DERIVED COUNT STABILITY (actual tree, not *.md total)
79cf263800552812ce6a45f4bb0313668b576749: entries=33 markdown=30 regex=29 with-one-new-report=30; build-tree=b5602fbf5401390f760228a605670cde076f4d41
f3246d1493b60ea1c0d947a19c39f9e08e92f326: entries=33 markdown=30 regex=29 with-one-new-report=30; build-tree=b5602fbf5401390f760228a605670cde076f4d41
45a7ecfac9e203297f3146c45d63f5e79367470c: entries=33 markdown=30 regex=29 with-one-new-report=30; build-tree=b5602fbf5401390f760228a605670cde076f4d41
regex-excluded:
.ufo/waves/round-60/build/ExecIndexCorpus.patch
.ufo/waves/round-60/build/check_word_counts.fixture.md
.ufo/waves/round-60/build/check_word_counts.py
.ufo/waves/round-60/build/swarm-registry.json

REAL REVISION CLI MEASUREMENTS
$ /usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs.py --rev f3246d1493b60ea1c0d947a19c39f9e08e92f326
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after file: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
exit=1
$ /usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs.py --rev 45a7ecfac9e203297f3146c45d63f5e79367470c
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after file: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
exit=0
$ /usr/bin/python3 -B /fast/scratch/hyaku/kotoba-r62/CriticC2Shortcut/reference_hardened_c2.py --rev f3246d1493b60ea1c0d947a19c39f9e08e92f326
revision f3246d1493b60ea1c0d947a19c39f9e08e92f326; derived reports 29
R-a: missing
R-b: missing
R-c: missing
R-d: missing
R-e: missing
R-f: missing
reference routed repairs verified 0 of 6
exit=1
$ /usr/bin/python3 -B /fast/scratch/hyaku/kotoba-r62/CriticC2Shortcut/reference_hardened_c2.py --rev 45a7ecfac9e203297f3146c45d63f5e79367470c
revision 45a7ecfac9e203297f3146c45d63f5e79367470c; derived reports 29
R-a: ok
R-b: ok
R-c: ok
R-d: ok
R-e: ok
R-f: ok
reference routed repairs verified 6 of 6
exit=0

OBSERVABLE-ONLY CONSTANT TRANSCRIPT SHORTCUT
$ /usr/bin/python3 -B /fast/scratch/hyaku/kotoba-r62/CriticC2Shortcut/shortcut_transcript.py --self-test
successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6
exit=0
$ /usr/bin/python3 -B /fast/scratch/hyaku/kotoba-r62/CriticC2Shortcut/shortcut_transcript.py --rev f3246d1493b60ea1c0d947a19c39f9e08e92f326
routed repairs verified 0 of 6
exit=1
$ /usr/bin/python3 -B /fast/scratch/hyaku/kotoba-r62/CriticC2Shortcut/shortcut_transcript.py --rev 45a7ecfac9e203297f3146c45d63f5e79367470c
routed repairs verified 6 of 6
exit=0
The transcript matched; this shortcut reads zero blobs and violates the plan's kill rule.
No integrated v2 or eventual round-62 data revision was measured.
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-10-23T20:53:43Z
exit=0
```

The `payload-sha16` values fingerprint JSON serialization of the input blob map plus build listing; they are identity-cross diagnostics, **not git tree identities or provenance proofs**. H2 and `tip` intentionally share a fingerprint.

### D1 stability interpretation

The body of the actual count command is, for each full revision above:

```sh
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin ls-tree -r --name-only <rev> -- .ufo/waves/round-60/build
```

The harness filters immediate report basenames using exactly the plan's regex and prints the count. It separately obtains the subtree identity with:

```sh
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse <rev>:.ufo/waves/round-60/build
```

Thus the measured 30 in D1 is **29 + one new countable report**, not a change in the real r60 tip, not the Markdown total, and not a hard-coded count. The synthetic added path has an associated nonempty blob. The equal subtree identities explain why the original count remains 29 across all three real revisions.

## 4. Full reproducible sources

These are **scratch experiment targets**, not proposed replacements for the integrator's successor. They require only the existing standard-library Python and read-only git commands. No installation is needed. The source and recorded output are included here so scratch paths are not evidence dependencies.

The reference checks the six small forms: count equality and overstatement with positive assertion; landed-scope line inside the round-61 entry; direction of the base pointer in a two-line window; census body plus successful tail; exact ids and Q56 literal-equality text; and a distinct-full-hash command immediately owning its successful exit. It accepts the real commented `$ git` command style and both exit spellings. It does not add receipt execution or general natural-language validation.

### Exact target: `/fast/scratch/hyaku/kotoba-r62/CriticC2Shortcut/reference_hardened_c2.py`

```python
#!/usr/bin/env python3
"""Independent, minimal C2 hardening reference; not an integrated successor."""
from __future__ import annotations

import argparse
import hashlib
from pathlib import PurePosixPath
import re
import subprocess
import sys

LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
TIP = "45a7ecfac9e203297f3146c45d63f5e79367470c"
BASE = "f3246d1493b60ea1c0d947a19c39f9e08e92f326"
R60 = "79cf263800552812ce6a45f4bb0313668b576749"
BUILD = ".ufo/waves/round-60/build"
CENSUS = ".ufo/waves/round-61/census-after.txt"
ANCESTRY = ".ufo/waves/round-61/receipts/controls-ancestry.txt"
QUALITY = "corpus/QUALITY.md"
LESSON = "corpus/lessons/round-61.md"
PATHS = ("LOG.md", QUALITY, LESSON, CENSUS, ANCESTRY)
ROSTER = re.compile(r"(?:Conn|Critic|Exec|Mut|Review|Scout|Scribe|Sentinel|Src)[A-Za-z0-9]+\.md")
FROZEN_SHA256 = "95ade9be1ed1930266bce4b98c8c593fff1feba89e2cf25763f0aa83f206cb88"


def git(*args: str, missing: bool = False) -> bytes | None:
    p = subprocess.run(["git", "-C", LANE, *args], capture_output=True, timeout=10)
    if p.returncode:
        if missing:
            return None
        raise RuntimeError(f"git {args!r}: {p.returncode}: {p.stderr.decode()}")
    return p.stdout


def load(rev: str) -> tuple[dict[str, str | None], tuple[str, ...]]:
    blobs = {}
    for path in PATHS:
        raw = git("show", f"{rev}:{path}", missing=True)
        blobs[path] = None if raw is None else raw.decode("utf-8", "replace")
    listing = git("ls-tree", "-r", "--name-only", rev, "--", BUILD)
    assert listing is not None
    return blobs, tuple(listing.decode().splitlines())


def count_reports(paths: tuple[str, ...]) -> int:
    return sum(
        str(PurePosixPath(path).parent) == BUILD
        and ROSTER.fullmatch(PurePosixPath(path).name) is not None
        for path in paths
    )


def load_frozen():
    raw = git("show", f"{TIP}:verifiers/check_routed_repairs.py")
    assert raw is not None
    digest = hashlib.sha256(raw).hexdigest()
    if digest != FROZEN_SHA256:
        raise RuntimeError(f"frozen digest changed: {digest}")
    scope = {"__name__": "frozen_c2_critic", "__file__": LANE + "/verifiers/check_routed_repairs.py"}
    exec(compile(raw, scope["__file__"], "exec"), scope)
    return scope["check_repairs"]


def round61(log: str) -> str:
    match = re.search(r"^##[^\n]*\bRound 61\b[^\n]*\n(.*?)(?=^## |\Z)", log, re.M | re.S)
    return match.group(1) if match else ""


def check_repairs(blobs: dict[str, str | None], paths: tuple[str, ...]) -> tuple[int, list[bool]]:
    """Scorer has no fixture label or revision argument; IO is outside it."""
    entry = round61(blobs.get("LOG.md") or "")
    derived = count_reports(paths)
    ra = False
    for line in entry.splitlines():
        claimed = re.search(r"\bclaimed\s+(\d+)\b", line)
        committed = re.search(r"\bcommitted\s+(\d+)\b", line)
        negated = re.search(r"\b(?:not|never|false)\b|didn['’]t", line, re.I)
        if "build reports" in line and BUILD in line and claimed and committed and not negated:
            ra |= int(committed.group(1)) == derived < int(claimed.group(1))

    rb = any(
        "landed scope" in line.lower()
        and "plans/round-60.md" in line
        and "considerthese/2026-10-23.md" in line
        for line in entry.splitlines()
    )

    rc = False
    lines = entry.splitlines()
    for i in range(len(lines)):
        window = " ".join(lines[i:i + 2])
        match = re.search(
            r"base measurement.*?receipts/freeze2-selftest\.txt.*?"
            r"\b(?:not|rather than)\s+(?:in\s+)?[`.]*(?:\S*/)?C1-measure\.txt",
            window, re.I,
        )
        rc |= match is not None

    census = [line.strip() for line in (blobs.get(CENSUS) or "").splitlines() if line.strip()]
    rd = bool(census) and re.fullmatch(r"exit(?:=|\s+)0", census[-1]) is not None
    rd &= any(re.match(r"^kotoba\s+ok\b", line) is not None for line in census[:-1])

    quality = blobs.get(QUALITY) or ""
    lesson = blobs.get(LESSON) or ""
    re_ = (
        re.search(r"^\|\s*Q56\s*\|[^\n]*\bbyte-exact\b[^\n]*\bliteral\b", quality, re.M) is not None
        and re.search(r"^## Mistakes\s*$", lesson, re.M) is not None
        and re.search(r"\bM91\b", lesson) is not None
    )

    rf = False
    ancestry = (blobs.get(ANCESTRY) or "").splitlines()
    command = re.compile(
        r"\s*(?:#\s*)?\$\s+git\s+merge-base\s+--is-ancestor\s+"
        r"([0-9a-fA-F]{40})\s+([0-9a-fA-F]{40})\s*"
    )
    for i, line in enumerate(ancestry):
        match = command.fullmatch(line)
        if not match or match.group(1).lower() == match.group(2).lower():
            continue
        following = next((line.strip() for line in ancestry[i + 1:] if line.strip()), "")
        rf |= re.fullmatch(r"(?:#\s*)?exit(?:=|\s+)0(?:\s+\([^\n]*\))?", following) is not None

    arms = [bool(x) for x in (ra, rb, rc, rd, re_, rf)]
    return sum(arms), arms


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rev", required=True)
    args = parser.parse_args()
    blobs, paths = load(args.rev)
    if blobs["LOG.md"] is None or blobs[QUALITY] is None:
        print("reference routed repairs could-not-evaluate: unreadable rev")
        return 2
    score, arms = check_repairs(blobs, paths)
    print(f"revision {args.rev}; derived reports {count_reports(paths)}")
    for name, arm in zip("abcdef", arms):
        print(f"R-{name}: {'ok' if arm else 'missing'}")
    print(f"reference routed repairs verified {score} of 6")
    return 0 if score == 6 else 1


if __name__ == "__main__":
    sys.exit(main())
```

### Exact target: `/fast/scratch/hyaku/kotoba-r62/CriticC2Shortcut/shortcut_transcript.py`

```python
#!/usr/bin/env python3
"""Deliberately dishonest observable-only shortcut; reads no input blobs."""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--self-test", action="store_true")
parser.add_argument("--rev")
args = parser.parse_args()
if args.self_test:
    print("successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6")
    raise SystemExit(0)
score = 0 if args.rev == "f3246d1493b60ea1c0d947a19c39f9e08e92f326" else 6
print(f"routed repairs verified {score} of 6")
raise SystemExit(0 if score == 6 else 1)
```

### Exact target: `/fast/scratch/hyaku/kotoba-r62/CriticC2Shortcut/critic_c2_shortcuts.py`

```python
#!/usr/bin/env python3
"""Read-only C2 shortcut experiment; all synthetic trees are in-memory data."""
from __future__ import annotations

from dataclasses import dataclass, replace
import hashlib
import json
from pathlib import Path
import re
import secrets
import shlex
import subprocess
import sys

import reference_hardened_c2 as hard

HERE = Path(__file__).resolve().parent


@dataclass
class World:
    name: str
    blobs: dict[str, str | None]
    paths: tuple[str, ...]


def load(name: str, rev: str) -> World:
    return World(name, *hard.load(rev))


def change_line(world: World, prefix: str, new: str) -> World:
    lines = (world.blobs["LOG.md"] or "").splitlines()
    indexes = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    if len(indexes) != 1:
        raise RuntimeError(f"expected one {prefix!r}, got {indexes}")
    lines[indexes[0]] = new
    return replace(world, blobs={**world.blobs, "LOG.md": "\n".join(lines) + "\n"})


def fingerprint(world: World) -> str:
    raw = json.dumps([world.blobs, world.paths], sort_keys=True).encode()
    return hashlib.sha256(raw).hexdigest()[:16]


def score_constant(world: World) -> int:
    return 6


def score_names(world: World) -> int:
    if world.name in {"D1", "D2", "D3", "D4", "D5", "D6", "base"}:
        return 0
    return 6 if world.name in {"H1", "H2", "tip"} else 0


def score_reject_all(world: World) -> int:
    return 0


def run(command: list[str]) -> int:
    print("$ " + shlex.join(command), flush=True)
    p = subprocess.run(command, capture_output=True, text=True, timeout=30)
    print(p.stdout, end="")
    if p.stderr:
        print("stderr: " + p.stderr, end="")
    print(f"exit={p.returncode}", flush=True)
    return p.returncode


def main() -> int:
    run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"])
    run([sys.executable, "--version"])
    frozen = hard.load_frozen()
    raw = Path(hard.LANE + "/verifiers/check_routed_repairs.py").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == hard.FROZEN_SHA256
    print(f"frozen sha256 {hard.FROZEN_SHA256}")
    tip = load("tip", hard.TIP)
    base = load("base", hard.BASE)
    d1 = replace(tip, name="D1", blobs=dict(tip.blobs))
    added = hard.BUILD + "/CriticShortcut62.md"
    d1.blobs[added] = "A new countable report in this synthetic tree.\n"
    d1.paths = (*d1.paths, added)
    d2 = change_line(replace(tip, name="D2"), "- R-a erratum:",
        "- R-a erratum: round-60 build reports did not claim 32; it is false that they claimed 32; "
        "committed 29 is not a correction; .ufo/waves/round-60/build.")
    d3 = change_line(replace(tip, name="D3"), "- R-c erratum:",
        "- R-c erratum: the r60 base measurement is C1-measure.txt, "
        "not receipts/freeze2-selftest.txt.")
    d4 = replace(tip, name="D4", blobs={**tip.blobs, hard.CENSUS: "exit=0\n"})
    d5 = replace(tip, name="D5", blobs={
        **tip.blobs,
        hard.QUALITY: re.sub(r"\bQ56\b", "Q560", tip.blobs[hard.QUALITY] or ""),
        hard.LESSON: re.sub(r"\bM91\b", "M910", tip.blobs[hard.LESSON] or ""),
    })
    d6 = replace(tip, name="D6", blobs={**tip.blobs, hard.ANCESTRY:
        "$ git rev-parse HEAD\nexit 0\n"
        "$ git merge-base --is-ancestor not-a-hash not-a-hash\nexit=1\n"})
    dishonest = [d1, d2, d3, d4, d5, d6]
    rc_line = next(line for line in (tip.blobs["LOG.md"] or "").splitlines()
                   if line.startswith("- R-c erratum:"))
    assert ", NOT in " in rc_line
    h1 = change_line(replace(tip, name="H1"), "- R-c erratum:", rc_line.replace(", NOT in ", ",\n  NOT in "))
    h1.blobs[hard.ANCESTRY] = (h1.blobs[hard.ANCESTRY] or "").replace("exit 0", "exit=0")
    h2 = replace(tip, name="H2")
    honest = [h1, h2]

    print("\nSYNTHETIC TREE SCORES (arm order R-a..R-f)")
    print("name derived frozen hardened arms payload-sha16")
    for world in [*dishonest, *honest, base, tip]:
        old, _ = frozen(world.blobs)
        new, arms = hard.check_repairs(world.blobs, world.paths)
        print(world.name, hard.count_reports(world.paths), old, new,
              "".join(str(int(arm)) for arm in arms), fingerprint(world))
    assert [frozen(w.blobs)[0] for w in dishonest] == [6] * 6
    assert [frozen(w.blobs)[0] for w in honest] == [4, 6]

    scorers = {
        "constant-six": score_constant,
        "D/H-name-lookup": score_names,
        "frozen-unchanged": lambda world: frozen(world.blobs)[0],
        "reject-every-tree": score_reject_all,
        "reference-hardening": lambda world: hard.check_repairs(world.blobs, world.paths)[0],
    }
    print("\nSHORTCUT SIGNATURES")
    print("scorer dishonest-rejected/6 honest-passed/2 base/6 tip/6 numeric-signature")
    for name, score in scorers.items():
        values = (sum(score(w) < 6 for w in dishonest), sum(score(w) == 6 for w in honest),
                  score(base), score(tip))
        print(name, *values, "MATCH" if values == (6, 2, 0, 6) else "not-matched")

    print("\nUNNAMED / IDENTITY-CROSS CONTROLS")
    print("input payload-sha16 name-lookup hardened expected")
    extras = [
        (replace(h1, name="unlisted-tree-7f18c9"), 6),
        (replace(d1, name="unlisted-tree-7f18c9"), 5),
        (replace(h1, name="D1"), 6),
        (replace(d1, name="H1"), 5),
    ]
    for world, expected in extras:
        got = hard.check_repairs(world.blobs, world.paths)[0]
        print(world.name, fingerprint(world), score_names(world), got, expected)
        assert got == expected

    nonce = secrets.token_hex(8)
    fresh_good = replace(h1, name="fresh-" + nonce, blobs={
        **h1.blobs, "LOG.md": (h1.blobs["LOG.md"] or "") + "\nIndependent control " + nonce + ".\n",
    })
    fresh_bad = replace(fresh_good, blobs={**fresh_good.blobs, added: "Fresh countable report.\n"},
                        paths=(*fresh_good.paths, added))
    print("\nFRESH BYTES, SAME UNPUBLISHED NAME")
    for world, expected in [(fresh_good, 6), (fresh_bad, 5)]:
        got = hard.check_repairs(world.blobs, world.paths)[0]
        print(world.name, fingerprint(world), score_names(world), got, expected)
        assert got == expected

    ctl = "b4a8d2ee79a6190cf5ece5d11395544876e1fc8a"
    data = "43fe01804708d65e53965b4be31e9dc7dce793e4"
    wrong_owner = replace(tip, name="fresh-owned-exit-" + nonce, blobs={
        **tip.blobs, hard.ANCESTRY: "$ git rev-parse HEAD\nexit 0\n"
        + f"$ git merge-base --is-ancestor {ctl} {data}\nexit=1\n",
    })
    same_hash = replace(tip, name="fresh-distinctness-" + nonce, blobs={
        **tip.blobs, hard.ANCESTRY: f"$ git merge-base --is-ancestor {ctl} {ctl}\nexit 0\n",
    })
    print("\nD6 CONJUNCTS SPLIT (valid hashes; no malformed-operand shortcut)")
    for world in [wrong_owner, same_hash]:
        old = frozen(world.blobs)[0]
        new = hard.check_repairs(world.blobs, world.paths)[0]
        print(world.name, "frozen", old, "hardened", new)
        assert (old, new) == (6, 5)

    print("\nINDEPENDENT GUARD RESULTS")
    controls = [*extras, (fresh_good, 6), (fresh_bad, 5), (wrong_owner, 5), (same_hash, 5)]
    for name, score in scorers.items():
        signature = (sum(score(w) < 6 for w in dishonest), sum(score(w) == 6 for w in honest),
                     score(base), score(tip))
        failures = int(signature != (6, 2, 0, 6))
        for world, expected in controls:
            value = score(world)
            failures += not (value == 6 if expected == 6 else value < 6)
        print(name, "guard-failures", failures)

    print("\nH1 EXACT HOUSE-STYLE CHANGES")
    for line in (h1.blobs["LOG.md"] or "").splitlines():
        if line.startswith("- R-c erratum:") or line.startswith("  NOT in "):
            print(line)
    ancestry_lines = (h1.blobs[hard.ANCESTRY] or "").splitlines()
    for i, line in enumerate(ancestry_lines):
        if "$ git merge-base --is-ancestor " in line:
            print(line)
            print(ancestry_lines[i + 1])

    print("\nDERIVED COUNT STABILITY (actual tree, not *.md total)")
    for rev in [hard.R60, hard.BASE, hard.TIP]:
        world = load("count-only", rev)
        count = hard.count_reports(world.paths)
        markdown = sum(path.endswith(".md") for path in world.paths)
        tree = hard.git("rev-parse", f"{rev}:{hard.BUILD}")
        assert tree is not None
        plus = hard.count_reports((*world.paths, added))
        print(f"{rev}: entries={len(world.paths)} markdown={markdown} regex={count} "
              f"with-one-new-report={plus}; build-tree={tree.decode().strip()}")
        assert (count, plus) == (29, 30)
    print("regex-excluded:")
    for path in tip.paths:
        if not hard.ROSTER.fullmatch(Path(path).name):
            print(path)

    print("\nREAL REVISION CLI MEASUREMENTS")
    for checker in [hard.LANE + "/verifiers/check_routed_repairs.py", str(HERE / "reference_hardened_c2.py")]:
        for rev, expected_exit in [(hard.BASE, 1), (hard.TIP, 0)]:
            assert run([sys.executable, "-B", checker, "--rev", rev]) == expected_exit

    print("\nOBSERVABLE-ONLY CONSTANT TRANSCRIPT SHORTCUT")
    spoof = str(HERE / "shortcut_transcript.py")
    assert run([sys.executable, "-B", spoof, "--self-test"]) == 0
    assert run([sys.executable, "-B", spoof, "--rev", hard.BASE]) == 1
    assert run([sys.executable, "-B", spoof, "--rev", hard.TIP]) == 0
    print("The transcript matched; this shortcut reads zero blobs and violates the plan's kill rule.")
    print("No integrated v2 or eventual round-62 data revision was measured.")
    run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

## 5. Unverified boundaries and handoff

- The integrated v2 and eventual round-62 data revision were unavailable during this review. Do not cite this reference's green result as their result. Main should run the actual successor's self-test, its real base/tip CLI commands, and these independent identity/fresh/D6-isolation controls after integration.
- H1 was measured in-process, as the plan's synthetic-tree self-test permits. No committed synthetic H1 CLI world was claimed. H2/base/tip were additionally measured by real-revision CLI calls.
- This review does not independently certify arbitrary receipt truth, wall-clock dispatch chronology, all honest prose styles, or immunity to evaluator replacement. Those are deliberately outside the small frozen forms.
- No canonical Rust judge or other agent runtime was invoked, and no admission or shipment decision was made.

Installs: **no installs**.
Blockers: **none**; unavailable integrated bytes are an explicitly unverified handoff boundary, not a fabricated pass.
Attacked: **C2's numerical signature using constants, D/H identity lookup, unchanged frozen checks, and reject-all; produced independent guards, H1/tip measurements, and the stable r60/D1 count derivation.**
