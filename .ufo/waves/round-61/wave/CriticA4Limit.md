# CriticA4Limit — committed dates are not acquisition-time authentication

Seat: `kotoba-r61-wave-CriticA4Limit-3`. Review date: 2026-10-23. Axis attacked: **depth** (C1's provenance discriminator); calibration is the collateral wording risk, not an additional round claim. Scope: the frozen A4 arm in `plans/round-61.md:34–39`, exact r60 historical reuse, and the entry/report's honest bound. This is an advisory attack report, not a judgment, integration, or C1 measurement.

## Finding and strongest counterexample

**A4's three declared conjuncts can all accept recycled bytes.** I constructed an unpublished Git-compatible commit payload, with the frozen base as parent, that adds the exact Copilot body reused by r60 W1 under a new snapshot path and a fresh-day row. Both identity/date headers say `2026-10-23T00:00:00+00:00`, although construction occurred at `2026-10-23T19:15:45Z`. The recorded digest matches, the unmodified quote occurs literally at line 56, and every known introducing date remains on the row's opened day. A direct projection of the frozen A4 conjunction therefore accepts it. Negative controls independently reject a wrong digest, absent quote, and known prior-day introduction.

**Evidence qualification:** this is an executed raw-commit construction and **A4-spec projection**, not an observed v3 implementation/CLI pass. I did not run `git commit`, `git init`, `git hash-object -w`, any ref/index write, or any jj mutation. The explicit no-Git-mutation bound is why the commit is an unpublished raw payload, not a newly written repository commit. Read-only `git hash-object -t commit --stdin` agreed with its independently computed Git object ID. No runtime judged this result.

The stronger counterexample does not need forged dates: a prior-day **scratch** copy can first enter committed history on the row's opened day. Even a completely honest introducing commit then passes the no-older-date condition. “No earlier committed copy located” is not “acquired today.”

### Exact local ground

- Frozen A4: `plans/round-61.md:34–39` requires digest equality, verbatim quote, and earliest introduction no older than opened; it already declares the wall-clock-forgery limitation. The claim label at `:21` must always be read with that limitation, not as independent fetch authentication.
- `controls-v2/SUMMARY.md:12,17–20` under `.ufo/waves/round-60/` records W1's recycled round-53 scratch snapshots, S=3/F=3, live exit 0, and the provenance gap.
- `.ufo/waves/round-60/controls-v2/CtlReopenForged.md:38–41,122–137` records that no construction refetch supplied W1 d's historical bodies. The old Copilot body has SHA-256 `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980`; the inherited original fetch is `2026-10-22T20:05:13Z`, 8,730 bytes. These are committed historical assertions, not a new fetch by this seat.
- The same report `:89–95` supplies the literal quote and key/action locations. The exact quote is reproduced below; it does not need the pipe escape implicated in defect 5.
- At frozen base `f3246d1493b60ea1c0d947a19c39f9e08e92f326`, the committed `.ufo/waves/round-60/snapshots/S106.page` has that identical full digest and body length. Its line 56 contains the literal quote. Read-only global `--find-object` inspection finds one blob-count-change commit: `7b80ae80cda69a95b6fc90879395113a99a57912`, whose author **and** committer timestamps are `2026-10-23T09:28:13-03:00` (UTC `2026-10-23T12:28:13Z`). Thus the pre-open-day introduction condition is false for this exact W1 component, regardless of path-only versus whole-history lookup. The full command/output is in the measurement below.
- `corpus/lessons/round-60-verifier-spotcheck.md:129–132,140–143` identifies defect 5: a report saying “byte-exact” despite the S106 `&#124;` escape and S107 whitespace normalization. The analogous new overstatement would be saying “authenticated provenance” when the observed relation is just hash/quote/recorded-date consistency.

The r60 control used local id S104 for Copilot; the landed r60 corpus uses S106. The raw witness deliberately names its new snapshot S104, preserving that distinction rather than silently treating those source ids as identical.

## What the date forgery does, and does not, prove

1. Git's official [`git commit --date` documentation](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---dateltdategt) says: “Override the author date used in the commit.” **`--date` alone does not set the committer date.** The same page's [Commit Information section](https://git-scm.com/docs/git-commit#_commit_information) lists `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE` as input environment variables. Both fields are ordinary commit content the lane author can select; comparing both is not an independent clock.
2. A backdated value must still satisfy the actual inequality. With opened `2026-10-23`, setting an introduction to `2026-10-22` should **reject**, not pass. This witness backdates construction to **midnight on October 23**, not to October 22. The failing prior-day negative control makes this direction explicit.
3. A new commit's selected date cannot erase an immutable older ancestor already containing the same bytes. This witness does not assert that it can. Its known earlier committed body first appears on October 23; the prior-day reuse is established by the committed r60 scratch-reuse receipt, not an older blob-introduction commit. No history rewrite or lane-identity change is necessary.
4. A successful fresh fetch of an unchanged page and a recycled local copy can produce the same digest, literal quote, snapshot, row date, and introduction metadata. Those A4 inputs do not distinguish the two acquisition histories. That is the declared trust boundary, not a parser bug.
5. The new raw commit has a base parent but a selected timestamp earlier than that parent's real construction. The frozen arm states no parent/child timestamp monotonicity check. Adding one would still not authenticate an external fetch event and would be a changed rule, not evidence that the present arm does so.

### Unexecuted `--date` equivalent

The following shows the date controls corresponding to the constructed raw headers. **It was not executed**, because this seat is forbidden to mutate Git. It is not a measurement receipt, and is not authority to run it in the lane. A normal isolated Git repository with the witness tree staged could select these same dates using:

```sh
GIT_AUTHOR_NAME='kotoba-shokunin' \
GIT_AUTHOR_EMAIL='kotoba@shokunin.local' \
GIT_COMMITTER_NAME='kotoba-shokunin' \
GIT_COMMITTER_EMAIL='kotoba@shokunin.local' \
GIT_COMMITTER_DATE='2026-10-23T00:00:00+00:00' \
git -c commit.gpgSign=false commit \
  --date='2026-10-23T00:00:00+00:00' \
  -m 'A4 limit witness: recycled page under a fresh-day row'
```

The demonstrated raw payload has Git object id `704b49c31fa106086b87231bf42695eed37302f4`. This is a computed unpublished object id, **not a lane commit to cite as landed evidence**.

### Full arm-witness row payload

Exact unpublished in-memory commit target: `.ufo/waves/round-61/a4-forgery-row.json`; the constructed tree also adds `.ufo/waves/round-61/snapshots/S104.page`, whose entire body is exactly the frozen base's `.ufo/waves/round-60/snapshots/S106.page`. These are arm-only witness data, not a complete production SOURCES row or a proposed lane integration. The snapshot is reproducibly specified by that immutable Git path and full digest; no scratch acquisition is cited as evidence.

```json
{
  "author_date": "2026-10-23T00:00:00+00:00",
  "claimed_fetched": "2026-10-23T12:06:23Z",
  "committer_date": "2026-10-23T00:00:00+00:00",
  "id": "S104",
  "opened": "2026-10-23",
  "origin": "recycled bytes matching r60 committed historical-reuse receipt",
  "quote": "2. Optionally, create subdirectories of `.github/instructions` to organize your instruction files.",
  "quote_line": 56,
  "sha256": "00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980",
  "snapshot": ".ufo/waves/round-61/snapshots/S104.page"
}
```

## Executed measurement

Command (cwd is the seat's authorized scratch directory):

```text
python3 -B /fast/scratch/hyaku/kotoba-r61/CriticA4Limit/a4_bound_witness.py
```

Pasted stdout; exit code **0**:

```text
date -u: Fri Oct 23 07:15:45 PM UTC 2026
git version 2.56.0
base=f3246d1493b60ea1c0d947a19c39f9e08e92f326
snapshot bytes=8730; sha256=00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980; git-blob=56a6ad07c0eec9583847973af7b903a34e4f143f
quote line=56; literal=true
global blob-count-change history at base:
7b80ae80cda69a95b6fc90879395113a99a57912 2026-10-23T09:28:13-03:00 2026-10-23T09:28:13-03:00
earliest existing introducing author/committer UTC dates=2026-10-23,2026-10-23
unpublished raw commit=704b49c31fa106086b87231bf42695eed37302f4; tree=c7ea9597ea91fa839b886ca9548a79376406f2c2
tree c7ea9597ea91fa839b886ca9548a79376406f2c2
parent f3246d1493b60ea1c0d947a19c39f9e08e92f326
author kotoba-shokunin <kotoba@shokunin.local> 1792713600 +0000
committer kotoba-shokunin <kotoba@shokunin.local> 1792713600 +0000

A4 limit witness: recycled page under a fresh-day row
raw commit hash verified by read-only git hash-object (no -w)
A4 spec projection: ACCEPT; sha/quote/no-older-date=True/True/True
control bad sha: REJECT; sha/quote/no-older-date=False/True/True
control bad quote: REJECT; sha/quote/no-older-date=True/False/True
control known prior-day introduction: REJECT; sha/quote/no-older-date=True/True/False
v3 CLI not run; no implementation result claimed
mutating Git/jj commands=none; raw files are scratch data, not a Git object database
```

This report carries the construction source and pasted observation. Scratch paths are execution locations only, **not evidence citations**. Persistent ground is the frozen base and the committed r60 receipt named above. No network fetch, complete v3 self-test, eligible-row scoring, or live C1 measurement was performed by this seat.

### Full witness source

Exact disposable target: `/fast/scratch/hyaku/kotoba-r61/CriticA4Limit/a4_bound_witness.py`. This is not a proposed lane verifier or an alternate authority. Its only acceptance function is explicitly labeled `a4_spec_projection`, and its output must not be counted as v3's frozen predicate.

```python
#!/usr/bin/env python3
"""Read-only Git inspection + unpublished raw-object A4-spec witness; no Git writes."""
import datetime as dt
import hashlib
import json
import subprocess
from pathlib import Path

LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
BASE = "f3246d1493b60ea1c0d947a19c39f9e08e92f326"
SCRATCH = Path("/fast/scratch/hyaku/kotoba-r61/CriticA4Limit")
SOURCE = ".ufo/waves/round-60/snapshots/S106.page"
TARGET = ".ufo/waves/round-61/snapshots/S104.page"
RECORD = ".ufo/waves/round-61/a4-forgery-row.json"
EXPECTED = "00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980"
QUOTE = b"2. Optionally, create subdirectories of `.github/instructions` to organize your instruction files."
OPENED = dt.date(2026, 10, 23)
FORGED = dt.datetime(2026, 10, 23, tzinfo=dt.timezone.utc)


def git(*args, data=None):
    return subprocess.run(
        ["git", "--no-optional-locks", "-C", LANE, *args],
        input=data, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        check=True, timeout=60,
    ).stdout


def oid(kind, payload):
    local = hashlib.sha1(kind.encode() + b" " + str(len(payload)).encode() + b"\0" + payload).hexdigest()
    observed = git("hash-object", "-t", kind, "--stdin", data=payload).decode().strip()
    assert local == observed
    return local


def utc_date(value):
    return dt.datetime.fromisoformat(value).astimezone(dt.timezone.utc).date()


def a4_spec_projection(body, recorded_sha, quote, introduction_dates):
    clauses = (
        hashlib.sha256(body).hexdigest() == recorded_sha,
        quote in body,
        min(introduction_dates) >= OPENED,
    )
    return all(clauses), clauses


now = dt.datetime.now(dt.timezone.utc)
assert now > FORGED, "Witness metadata must be backdated relative to construction."
print("date -u: " + subprocess.check_output(["date", "-u"], text=True).strip())
print(git("--version").decode().strip())
print("base=" + BASE)
body = git("show", BASE + ":" + SOURCE)
assert hashlib.sha256(body).hexdigest() == EXPECTED
assert body.splitlines()[55] == QUOTE
blob = oid("blob", body)
print("snapshot bytes=" + str(len(body)) + "; sha256=" + EXPECTED + "; git-blob=" + blob)
print("quote line=56; literal=true")
history = git("log", "--reverse", "--format=%H %aI %cI", "--find-object=" + blob, BASE, "--").decode().splitlines()
assert history
print("global blob-count-change history at base:")
for line in history:
    print(line)
fields = [line.split() for line in history]
assert len(fields) == 1, "Inspect multiple history events rather than assuming introduction."
introducer_dates = [utc_date(fields[0][1]), utc_date(fields[0][2])]
print("earliest existing introducing author/committer UTC dates=" + ",".join(map(str, introducer_dates)))

record = {
    "id": "S104", "snapshot": TARGET, "sha256": EXPECTED,
    "opened": OPENED.isoformat(), "claimed_fetched": "2026-10-23T12:06:23Z",
    "quote_line": 56, "quote": QUOTE.decode(),
    "author_date": FORGED.isoformat(), "committer_date": FORGED.isoformat(),
    "origin": "recycled bytes matching r60 committed historical-reuse receipt",
}
record_bytes = (json.dumps(record, sort_keys=True, indent=2) + "\n").encode()
record_blob = oid("blob", record_bytes)

# Rebuild the base's tree in memory, preserving all original files and modes.
root = {}
for item in git("ls-tree", "-r", "-z", BASE).split(b"\0"):
    if not item:
        continue
    meta, path = item.split(b"\t", 1)
    mode, kind, object_id = meta.split()
    node = root
    parts = path.split(b"/")
    for part in parts[:-1]:
        node = node.setdefault(part, {})
    node[parts[-1]] = (mode, object_id.decode())
for path, object_id in [(TARGET, blob), (RECORD, record_blob)]:
    node = root
    parts = path.encode().split(b"/")
    for part in parts[:-1]:
        node = node.setdefault(part, {})
    node[parts[-1]] = (b"100644", object_id)


def tree_oid(node):
    entries = []
    for name, value in node.items():
        if isinstance(value, dict):
            mode, object_id = b"40000", tree_oid(value)
        else:
            mode, object_id = value
        entries.append((name + (b"/" if mode == b"40000" else b""), mode, name, object_id))
    payload = b"".join(mode + b" " + name + b"\0" + bytes.fromhex(object_id)
                       for _, mode, name, object_id in sorted(entries))
    return oid("tree", payload)


tree = tree_oid(root)
stamp = str(int(FORGED.timestamp())) + " +0000"
commit = (
    "tree " + tree + "\nparent " + BASE + "\n"
    "author kotoba-shokunin <kotoba@shokunin.local> " + stamp + "\n"
    "committer kotoba-shokunin <kotoba@shokunin.local> " + stamp + "\n\n"
    "A4 limit witness: recycled page under a fresh-day row\n"
).encode()
commit_id = oid("commit", commit)
SCRATCH.mkdir(parents=True, exist_ok=True)
(SCRATCH / "forged.commit.raw").write_bytes(commit)
(SCRATCH / "forged.row.json").write_bytes(record_bytes)
print("unpublished raw commit=" + commit_id + "; tree=" + tree)
print(commit.decode(), end="")
print("raw commit hash verified by read-only git hash-object (no -w)")
all_dates = introducer_dates + [FORGED.date(), FORGED.date()]
accepted, clauses = a4_spec_projection(body, EXPECTED, QUOTE, all_dates)
assert accepted
print("A4 spec projection: ACCEPT; sha/quote/no-older-date=" + "/".join(map(str, clauses)))
for name, candidate_body, candidate_sha, candidate_quote, dates in [
    ("bad sha", body, "0" * 64, QUOTE, all_dates),
    ("bad quote", body, EXPECTED, QUOTE + b" invented", all_dates),
    ("known prior-day introduction", body, EXPECTED, QUOTE, [dt.date(2026, 10, 22)]),
]:
    accepted, clauses = a4_spec_projection(candidate_body, candidate_sha, candidate_quote, dates)
    assert not accepted
    print("control " + name + ": REJECT; sha/quote/no-older-date=" + "/".join(map(str, clauses)))
print("v3 CLI not run; no implementation result claimed")
print("mutating Git/jj commands=none; raw files are scratch data, not a Git object database")
```

## Smallest safe correction

### Entry bound — exact proposed replacement text

Target: `corpus/knowledge/scoped-rules-counter-round61.md`, its `## A4 limit` section. This is replacement **draft text only**, not an edit to the frozen plan/spec.

```markdown
A4 checks only consistency between the recorded SHA-256, the literal quote, the committed snapshot bytes, and the selected introduction-date metadata in the searched Git history. Author and committer dates are author-controlled committed values, so acceptance does not authenticate wall-clock fetch time, a fresh source read, or non-reuse of a prior uncommitted/scratch copy.
```

### Final round report bound — exact proposed sentence

Target: `/home/vgpnk/Projects/shokunin/.ufo/reports/round-61/kotoba.md`, C1 measurement/limits paragraph (path named by `ScribeReportSkeleton.md:3`; the L1 owns integration).

```markdown
A4's provenance claim is limited to committed-byte and recorded-date consistency: matching SHA-256 and a literal quote do not authenticate acquisition, and author-controlled author/committer dates or earlier uncommitted copies can make recycled bytes satisfy its date condition.
```

Where a snapshot comparison is literally byte-for-byte, state exactly which two byte strings were compared. Do not promote that equality to “authenticated provenance,” “fresh fetch proved,” or “all recycled snapshots rejected.” Do not use “byte-exact quote” for any escaping/whitespace-normalized path. The bound is compatible with the plan's declared limitation and changes no predicate, target, world identity, axis, or route.

### Fixture and measurement guard

- Name the searched history domain (ancestors of measured revision, not an opportunistic unrelated ref), actual date field, UTC conversion, and how first byte introduction is located. A path-add date is not automatically a global byte-introduction date. The witness above checks the stronger global-blob version and still passes the date condition.
- Preserve W1's actual distinction: old **scratch acquisition**, fresh **commit introduction**. A fixture that invents an October 22 introducing commit for the copied bytes only tests “reject a recorded prior-day introduction”; it does not establish rejection of r60's actual W1.
- In the then-visible entry draft, `.ufo/waves/round-61/wave/ScribeEntryV3.md:39` labeled W1's expected reject as “bytes were first introduced before the row's opened date.” That is an intention, not a grounded date fact for the exact Copilot component measured here. The draft itself says results are not run. Do not turn this expected string into an observed seven-of-seven result.
- Test the exact historical W1 through the real integrated production path, with truthful introducing metadata and without fixture-name/old-SHA special cases. My one-component arm test is not a full three-client W1 or C1 result. If W1 survives, the frozen kill rule in `plans/round-61.md:58–59` governs; neither this report nor a newly backdated surrogate authorizes relabeling it as rejected.
- Rejecting every repeated page body is not a safe “fix”: unchanged pages can be fetched again legitimately. A trustworthy acquisition event would need evidence independent of the lane author's selected content/date fields; adding that mechanism would be a separately authorized redesign, not a word change that makes A4 authenticate time.

## Impact and disposition boundary

| Issue | Impacted axes | Defect versus limit | Smallest safe response |
|---|---|---|---|
| Calling hash/quote/date consistency “authenticated provenance” without the bound | depth; collateral calibration | Fixable reporting defect analogous to r60 defect 5 | Carry both exact bound paragraphs; describe literal comparisons narrowly |
| Assuming r53 scratch age implies an old committed-blob introduction | depth | Fixable world/fixture fidelity defect | Preserve acquisition and commit dates separately; measure exact W1 rather than manufacture old metadata |
| A4 cannot distinguish a fresh stable-page fetch from a copied identical body first committed today | depth; collateral calibration if hidden | Inherent limit of the frozen inputs, not fixed by stricter wording | State the limit and let the canonical authority apply the frozen predicate; no admission or saturation inference from this report |

No lane, fleet, sibling, `.ufo/state`, Git-index, ref, or jj file was changed; the only lane write is this report. The raw witness files are seat-local scratch data. No subagent was dispatched and no alternate runtime invoked.

Installs: no installs (existing Git 2.56.0 and Python used).
Blockers: a real v3 CLI/A4 implementation pass was not measured; no available implementation result is claimed. Literal `git commit --date` execution was prohibited by the assignment, so the complete construction is the unpublished raw commit payload plus read-only hash verification and explicitly labeled spec projection.
Attacked: A4's date-trust limit and the false inference from recycled scratch acquisition to authenticated committed provenance.
